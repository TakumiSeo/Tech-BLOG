Title: AppDependencies のインジェストを削減する手順（Application Insights / Log Analytics）
Date: 2026-06-08
Slug: appdependencies-ingest-reduction
Lang: ja-jp
Category: notebook
Tags: azure, azure-monitor, application-insights, log-analytics, cost-optimization, observability
Summary: Application Insights の AppDependencies テーブル（外部呼び出しの依存関係テレメトリ）が大きなインジェストを占める環境向けに、SDK サンプリング / 不要計装の無効化 / Data 列の除去 / DCR 変換 / コミットメント階層までを Microsoft Learn 根拠で順序立てて整理。AppTraces と同じ Application Insights 経路だが「依存関係＝アプリからの送信呼び出し」特有の削減ルートを扱う。

`AppTraces`（トレース ログ）、`AppServiceHTTPLogs`（受信 HTTP）、`AppServiceIPSecAuditLogs`（アクセス制限）に続いて、Application Insights 環境でログ コストを押し上げがちなのが `AppDependencies` テーブルです。本記事では、Microsoft Learn 公式ドキュメントに基づき、**効果が大きく実装コストが低い順**に削減手順を整理します。

> 前提の整理: `AppDependencies` は **アプリが外部サービス（HTTP / SQL / Azure SDK など）を呼び出した「依存関係（dependency）テレメトリ」** です[^1][^2]。`AppServiceHTTPLogs`（=アプリへの**受信**リクエスト）とは向きが逆で、こちらは**アプリからの送信呼び出し**を記録します。`AppTraces` と同じ Application Insights のテレメトリ経路のため、削減の主役は **SDK サンプリング**になります。

## 1. AppDependencies とは何か（前提整理）

`AppDependencies` は Application Insights の **依存関係テレメトリ**（`dependencies` テーブル）を Log Analytics 側から参照するテーブル名です。「監視対象コンポーネントが、SQL や HTTP エンドポイントなどの**リモート コンポーネントと相互作用した**こと」を表します[^1][^2]。

### 1.1 何が記録されるか

依存関係テレメトリは、アプリから外部への呼び出しごとに 1 件記録され、**呼び出しの所要時間と成否**を測定します[^3]。自動収集される主な依存関係は次のとおりです[^3]。

- **HTTP / HTTPS 呼び出し**（`HttpClient` / `IHttpClientFactory` 経由の下流 API 呼び出し）
- **SQL**（SQL Database への呼び出し、`Data` にクエリ文が入る）
- **Azure SDK 呼び出し**（Storage / Service Bus / Cosmos DB など）

> 補足: 前回 `AppTraces` 分析で出た `IHttpClientFactory` の `Start processing HTTP request`（トレース ログ）と、`AppDependencies` の HTTP 依存関係は**別物**です。前者は `ILogger` のテキスト ログ（`AppTraces`）、後者は構造化された依存関係テレメトリ（`AppDependencies`）で、`DependencyTrackingTelemetryModule` が自動収集します[^3]。同じ HTTP 呼び出しが両テーブルに二重計上されている可能性があります。

### 1.2 AppDependencies の主なフィールド

| 列 | 内容 |
|---|---|
| `DependencyType` | 依存関係の種類（HTTP / SQL / Azure table など。低カーディナリティ）[^1] |
| `Target` | 呼び出し先（サーバー名 / ホスト アドレス）[^1] |
| `Name` | コマンド名（URL パス テンプレート / SQL テーブル名など。低カーディナリティ）[^1] |
| `Data` | **実行されたコマンド全体（SQL 文 / 全クエリ パラメータ付き URL）**[^1] |
| `Success` | 成否（bool）[^1] |
| `ResultCode` | 結果コード（SQL エラー / HTTP ステータス）[^1] |
| `DurationMs` | 所要時間（ミリ秒）[^1] |
| `ItemCount` | **1 サンプル項目が表す実テレメトリ件数**（サンプリング補正に使用）[^1] |
| `OperationId` / `Id` / `ParentId` | 相関 ID（リクエストや子依存と紐づく）[^1] |
| `SyntheticSource` | 合成トラフィック（外形監視など）の発生源[^1] |
| `AppRoleName` / `AppRoleInstance` | アプリのロール名 / インスタンス[^1] |
| `_BilledSize` / `_IsBillable` | 課金サイズ / 課金対象フラグ |

コスト分析では `_BilledSize` / `_IsBillable` が中心指標で、`Data`（特に SQL 文や長い URL）が 1 件のサイズを押し上げやすい列です（手順 3）。

### 1.3 テーブルの機能サポート（重要な制約）

| 項目 | 値 | 影響 |
|---|---|---|
| Basic Logs プラン | **非対応（No）** | `AppDependencies` は Basic Logs への切り替えはできない[^1] |
| Ingestion-time DCR transformation | **対応（Yes）** | Workspace transformation DCR で取り込み時の行・列フィルタが可能[^1] |

## 2. 削減アプローチの優先順位（Microsoft Learn ベストプラクティス）

Microsoft の Application Insights コスト最適化チェックリストでは、優先度の高いものから次が挙げられています[^4]。

1. **ワークスペース ベース Application Insights への移行**（Basic Logs / コミットメント階層などのコスト機能を利用可能にする）[^4]
2. **サンプリングでデータ量を調整**（OpenTelemetry サンプリングが「主要なツール」と明記）[^4][^5]
3. **不要なモジュール（計装）を無効化**[^4]
4. 更新された SDK の使用[^4]

加えて、高インジェストのトラブルシュート ガイドでは、`dependencies` テーブル固有の削減策として次が挙げられています[^6]。

- **依存関係テレメトリを生成する処理のサンプリング オーバーライド**（特定メソッドの抑制）[^6]
- **依存関係を生成する計装の無効化**[^6]（ただし下流テレメトリも失う点に注意）

## 3. 推奨削減手順（優先度高 → 低）

### 手順 0 — 現状把握用 KQL クエリ

ワークスペース全体のテーブル別課金ボリュームの推移（直近 31 日）[^1]:

```kusto
Usage
| where TimeGenerated > ago(32d)
| where StartTime >= startofday(ago(31d)) and EndTime < startofday(now())
| where IsBillable == true
| summarize BillableDataGB = sum(Quantity) / 1000. by bin(StartTime, 1d), DataType
| render columnchart
```

`AppDependencies` を `DependencyType` 別に集計（HTTP か SQL か、何が支配的か）[^1]:

```kusto
AppDependencies
| where TimeGenerated > ago(1d)
| where _IsBillable == true
| summarize Records = count(), BillableGB = sum(_BilledSize)/1024/1024/1024
        by DependencyType
| order by BillableGB desc
```

サンプリングが既に効いているかの確認（`ItemCount` から保持率を逆算）[^5]:

```kusto
AppDependencies
| where TimeGenerated > ago(1d)
| summarize RetainedPercentage = 100.0 / avg(ItemCount) by bin(TimeGenerated, 1h)
| render timechart
```

`RetainedPercentage` が 100 未満なら、すでにサンプリングされています[^5]。

### 手順 1 — SDK サンプリングを有効化 / 強化する（最優先・効果最大）

Microsoft はサンプリングを「テレメトリ量・データ コスト・ストレージ コストを削減しつつ、統計的に正しい分析を保つ**推奨手段**」と位置づけています[^7]。サンプリング フィルターは**関連項目（リクエスト・依存関係・例外・トレース）をまとめて選択**するため、診断時のナビゲーションが維持されます[^7]。

> 重要: **OpenTelemetry Distro では既定でサンプリングは有効化されていません**。明示的に有効化・設定が必要です[^5]。

#### 1.1 OpenTelemetry Distro でのサンプリング設定（.NET）[^5]

```csharp
builder.Services.AddOpenTelemetry().UseAzureMonitor(o =>
{
    o.SamplingRatio = 0.1F;   // 約 10% を保持
});
```

サンプリングは `OperationId` 単位で関連テレメトリをまとめて保持/破棄するため、依存関係・リクエスト・トレースの相関が維持されます[^5][^7]。

#### 1.2 Classic SDK で依存関係だけサンプリング対象を調整[^8]

Classic SDK では、テレメトリ種別ごとにサンプリングの対象/除外を指定できます。例えば**依存関係をサンプリング対象に含める**（または逆に重要なので除外する）といった制御が可能です[^8]。

```csharp
// adaptive sampling を 5 items/sec に設定（依存関係も対象に含める既定の挙動）
builder.UseAdaptiveSampling(maxTelemetryItemsPerSecond: 5);
```

> 注: クエリで件数を数える際は、サンプリング後は `count()` ではなく `sum(ItemCount)` を使う必要があります（`ItemCount` が 1 サンプルあたりの実件数を表す）[^1][^7]。

### 手順 2 — 不要な依存関係計装を絞る

高頻度・低価値な依存関係（例: 内部ヘルスチェックの HTTP、頻発するキャッシュ参照）が大量にある場合、**その計装をピンポイントで抑制**します[^6]。

- **Java エージェント**: サンプリング オーバーライドで特定メソッド/依存関係を抑制[^6]
- **計装の無効化**: 依存関係を生成する計装自体を無効化[^6]

> 警告: 依存関係計装を無効化すると、**Application Map から該当の依存（DB / 下流サービス）が消え、その先の下流テレメトリもすべて失われます**[^6]。可視性とのトレードオフを理解した上で行ってください。

### 手順 3 — Workspace transformation DCR（取り込み時の行・列フィルタ）

SDK 変更が難しい場合は、Workspace transformation DCR で取り込み時に処理します。`AppDependencies` は transformation 対応テーブルで、Microsoft 公式に**専用のサンプル**が用意されています[^9]。

#### 3.1 失敗または遅い依存関係だけ残す（行フィルタ）[^9]

正常・高速な依存関係を落とし、失敗（`Success == false`）と遅延（`DurationMs >= 500`）だけ保持します。

```kusto
source
| where Success == false or DurationMs >= 500
```

#### 3.2 SQL 文を `Data` 列から除去（列フィルタ・サイズ削減）[^9]

依存関係のタイミングと成否は残しつつ、サイズの大きい SQL 文を `Data` から削ります[^9]。

```kusto
source
| extend dependencyType = tolower(tostring(DependencyType))
| extend Data = iff(dependencyType == 'sql', '', Data)
| project-away dependencyType
```

#### 3.3 合成トラフィック（外形監視）を除外[^9]

`SyntheticSource` が入っているレコード（可用性テストなどの合成トラフィック）を落とします[^9]。

```kusto
source
| where isempty(SyntheticSource)
```

#### 3.4 特定アプリ（AppRoleName）に絞って適用[^9]

複数アプリがワークスペースを共有している場合、特定アプリだけに条件を適用できます[^9]。

```kusto
source
| where AppRoleName == "<app-role-name>"
| where Success == false or DurationMs >= 1000
```

### 手順 4 — Daily Cap / Commitment Tier（ワークスペース レベル）

- **Daily Cap**: 予期しないスパイクへのセーフティ ネット。サンプリングの代替ではなく最終手段[^5]
- **Commitment Tier**: 削減後に残った取り込み量が 100 GB/day 以上で安定していれば、Pay-as-you-go から移行して単価を下げられる[^10]

> 注: `AppDependencies` は **Basic Logs 非対応**[^1]のため、Basic Logs で単価を下げる手段は使えません。残量に対してはコミットメント階層が主な単価最適化手段になります。

## 4. 推奨実行順序（まとめ表）

| # | アクション | 効果 | リスク |
|---|---|---|---|
| 1 | 現状把握 KQL（手順 0） | — | なし |
| 2 | OpenTelemetry サンプリング（`SamplingRatio`）の有効化・強化[^5] | **大** | メトリクスは ItemCount 補正で維持。高サンプリング率ではログ クエリ精度が低下[^7] |
| 3 | 不要な依存関係計装の抑制（高頻度・低価値なもの）[^6] | 中〜大 | Application Map から該当依存と下流が消える[^6] |
| 4 | DCR 変換: 失敗 / 遅延のみ保持（`Success==false or DurationMs>=N`）[^9] | 大 | 正常・高速呼び出しの網羅性が下がる |
| 5 | DCR 変換: SQL 文を `Data` から除去[^9] | 中（1 件のサイズ減） | SQL 文ベースの調査ができなくなる |
| 6 | DCR 変換: 合成トラフィック除外（`SyntheticSource`）[^9] | 小〜中 | 可用性テストの記録が消える |
| 7 | Commitment Tier に移行[^10] | 中（単価引き下げ） | 31 日コミット |
| — | Basic Logs への切り替え | **不可**（テーブル非対応）[^1] | — |

## 5. transformation のコスト（重要）

| テーブル プラン | Transformation のコスト |
|---|---|
| **Analytics**（`AppDependencies` は Basic 非対応のため通常こちら） | Transformation 自体は通常無料。ただし**取り込みデータ量を 50% を超えて削減した場合、超過分はデータ処理料金として課金**。計算式: `[削減した GB] − ([受信 GB] / 2)` |
| Microsoft Sentinel が有効な場合 | Analytics テーブルへの transformation は**金額がいくら削減されても無料** |

> 行フィルタ（失敗/遅延のみ保持）は容易に 50% を超えるため、データ処理料金の対象になりやすいです。一方、SQL 文除去のような**列フィルタ**は「取り込み量を減らすが行は残す」ため、50% ルールへの当たり方が異なります。まず SDK サンプリングで全体量を下げ、transformation は補助的に使うのが合理的です[^4][^9]。

## 6. 「犯人」を特定する KQL クエリ集

`AppDependencies` の `_BilledSize` / `_IsBillable` / `DependencyType` / `Target` / `Name` / `Data` / `AppRoleName` は公式スキーマに存在します[^1]。

### 6.1 DependencyType × Target 別の課金量（パレート確認）

```kusto
AppDependencies
| where TimeGenerated > ago(7d)
| where _IsBillable == true
| summarize BillableGB = sum(_BilledSize)/1024/1024/1024, Records = count()
        by DependencyType, Target
| top 50 by BillableGB desc
```

特定の下流 API / SQL サーバーへの呼び出しが突出していないかを見ます。

### 6.2 Name（コマンド）別 — どの呼び出しが多いか

```kusto
AppDependencies
| where TimeGenerated > ago(1d)
| where _IsBillable == true
| summarize BillableGB = sum(_BilledSize)/1024/1024/1024, Records = count()
        by DependencyType, Name
| top 50 by Records desc
```

ヘルスチェックの HTTP や頻発するキャッシュ参照など、高頻度・低価値な呼び出しを発見できます。

### 6.3 成否 × 所要時間の分布（失敗/遅延のみ残せるか判断）

```kusto
AppDependencies
| where TimeGenerated > ago(1d)
| where _IsBillable == true
| summarize BillableGB = sum(_BilledSize)/1024/1024/1024, Records = count()
        by Success, DurationBucket = case(
            DurationMs < 100, "0:<100ms",
            DurationMs < 500, "1:100-500ms",
            DurationMs < 1000, "2:500ms-1s",
            "3:>=1s")
| order by Success asc, DurationBucket asc
```

`Success == true` かつ短時間の呼び出しが大半なら、手順 3.1（失敗/遅延のみ保持）が大きく効きます。

### 6.4 AppRoleName 別（どのアプリが出しているか）

```kusto
AppDependencies
| where TimeGenerated > ago(7d)
| where _IsBillable == true
| summarize BillableGB = sum(_BilledSize)/1024/1024/1024, Records = count()
        by AppRoleName
| order by BillableGB desc
```

### 6.5 SQL の `Data` サイズ確認（列フィルタ効果の見積もり）

```kusto
AppDependencies
| where TimeGenerated > ago(1d)
| where _IsBillable == true
| where tolower(tostring(DependencyType)) == "sql"
| summarize Records = count(),
            AvgDataLen = avg(strlen(Data)),
            TotalDataMB = sum(strlen(Data))/1024/1024
```

`AvgDataLen` が大きければ、手順 3.2（SQL 文除去）で 1 件あたりを縮める効果が見込めます。

## 7. 実例: HTTP 依存がほぼ全量・サンプリング無効・受信リクエストと親子相関だったケース

実環境で `AppDependencies` を分析したところ、次のような状態でした（マスク値）。これは「サンプリングが理想的に効く前提が整っているのに、有効化されていない」典型例です。

### 7.1 DependencyType 別: HTTP が支配的

| DependencyType | Records | BillableGB |
|---|---|---|
| **HTTP** | 5,656,526 | **6.88** |
| Azure blob | 104,368 | 0.12 |
| InProc \| Microsoft.Storage | 104,368 | 0.08 |
| Azure table | 8,844 | 0.009 |
| その他（Service Bus 等） | わずか | ~0 |

課金の約 96% が **HTTP 依存関係**（外部 API への送信呼び出し）。SQL は出ていないため、手順 3.2（SQL 文除去）の対象はありません。削減の主戦場は HTTP です。

### 7.2 サンプリングはほぼ効いていない

手順 0 の `RetainedPercentage` クエリ（`100.0 / avg(ItemCount)`）を時系列で見ると、値は**ほぼ 100% に張り付き**でした。ときどき谷（42% / 27% / 70% など）が現れますが、これはスパイク時に取り込み側の ingestion sampling が瞬間的に効いたもので、**定常的な SDK サンプリングは無効**と判断できます[^5]。

```kusto
AppDependencies
| where TimeGenerated > ago(7d)
| summarize Retained = 100.0 / avg(ItemCount), RealCount = sum(ItemCount)
        by bin(TimeGenerated, 1h)
| render timechart
```

谷の時間帯で `RealCount`（実件数）が跳ねていれば、「スパイク時だけ ingestion sampling が発動」した証拠で、定常的なサンプリングが無いことを裏づけます。

### 7.3 「AppServiceHTTPLogs と同じでは？」を OperationId で検証

`Name` を集計すると、受信側の `AppServiceHTTPLogs.CsUriStem`（業務 API パス）と似た文字列が並びます。「情報が重複しているのでは？」という疑問が湧きますが、**Name が似ているだけでは重複とは言えません**。`AppServiceHTTPLogs`（受信）と `AppDependencies`（送信）は向きが逆だからです（手順 7.6 / 注意点参照）。

そこで `OperationId` で両テーブルの重なりを検証します（`let` が使えない環境向けにサブクエリを直接記述）。

```kusto
AppDependencies
| where TimeGenerated > ago(1d)
| where DependencyType == "HTTP"
| summarize Deps = count() by OperationId
| join kind=fullouter (
    AppRequests
    | where TimeGenerated > ago(1d)
    | summarize Reqs = count() by OperationId
) on OperationId
| extend HasDep = isnotempty(Deps), HasReq = isnotempty(Reqs)
| summarize
    BothMatch = countif(HasDep and HasReq),
    OnlyDep   = countif(HasDep and not(HasReq)),
    OnlyReq   = countif(not(HasDep) and HasReq)
```

結果（マスク値）:

| BothMatch | OnlyDep | OnlyReq |
|---|---|---|
| **986,646** | **1** | 5,038 |

### 7.4 判定: 二重記録ではなく「正常な分散トレース階層」

- `OnlyDep` がほぼゼロ（1 件）= **依存呼び出しはほぼ全て受信リクエストの子として発生**している。
- 構造は「**1 つの受信リクエスト（`AppRequests` / `AppServiceHTTPLogs`）→ 処理中に下流 API を HTTP 呼び出し（`AppDependencies`）**」という親子の階層。
- つまり「同じ情報の二重記録」ではなく、**OperationId で相関した別レイヤーの情報**。`Name` が似て見えても、受信側は自分のエンドポイント、依存側は呼んだ先のエンドポイント（`Target` を見れば別ホスト）であり、役割が異なります[^1][^2]。

> この相関構造こそが、サンプリングを安全に効かせられる根拠です。サンプリングは `OperationId` 単位で親子をまとめて保持/破棄するため[^5][^7]、受信リクエストとその下流依存が「セットで」間引かれ、相関が壊れません。

### 7.5 このケースの削減方針（サンプリング以外も含む）

「重複だから片方消す」はできない（親子で役割が違う）と判明したので、削減は次の組み合わせで行います。

| 手段 | 効果 | コード変更 | このケースでの妥当性 |
|---|---|---|---|
| **OTel サンプリング `SamplingRatio=0.1`**[^5] | 6.88 → 約 0.7 GB | 要 | **第一手**。HTTP 96% なので全体にそのまま効く。親子セットで間引かれ相関維持 |
| **DCR: 失敗/遅延のみ保持**[^9] | 大 | 不要 | コード変更不可時の主力。`OnlyDep≈0` なので異常系は受信に紐づき全件残り、障害調査に支障が出にくい |
| 計装抑制（health 等の下流呼び出し）[^6] | 中〜大 | 要 | 価値の低い HTTP 依存に限定。Application Map から該当下流が消える点に注意 |
| DCR: 列削減（`Data` / `Properties`）[^9] | 中 | 不要 | 件数を保ちつつ 1 件サイズを縮める。HTTP の長い URL に効く |

サンプリングと DCR の使い分け:

- **横断的に全テーブルを減らしたい** → SDK サンプリング（`AppRequests` / `AppDependencies` / `AppTraces` が相関を保ったまま一括で減る）[^5][^7]
- **`AppDependencies` だけ・コードを触れない** → DCR「失敗/遅延のみ保持」（このテーブル単体に効く）[^9]

### 7.6 横断的な気づき（同じ呼び出しが複数テーブルに分散）

このケースでは、1 つの業務処理が複数テーブルに分散して記録されていました。

| テーブル | 記録される観点 | 1 受信あたり |
|---|---|---|
| `AppServiceHTTPLogs` | 受信 HTTP（IP / ステータス / 所要時間） | 1 行 |
| `AppRequests` | 受信リクエストのテレメトリ | 1 行 |
| `AppDependencies` | 処理中の下流 HTTP 呼び出し | 0〜複数行 |
| `AppTraces` | 処理中の `ILogger` / HttpClient トレース | 複数行 |

これらは重複ではなく階層ですが、**コスト最適化は個別最適ではなく横断で考えるべき**ことを示しています。OperationId 単位のサンプリングは、この階層全体を相関を保ったまま一括削減できる唯一の手段です。

## 8. 注意点（横断的な制約まとめ）

- **依存関係 = アプリからの送信呼び出し**: `AppServiceHTTPLogs`（受信）とは向きが逆。同じ HTTP でも別テーブル[^1][^2]。
- **サンプリングが主役**: Application Insights 経路のため、SDK サンプリングが最優先のレバー[^4][^5][^7]。
- **メトリクスはサンプリングの影響を受けない**: 事前集計メトリクスで正確な値が維持される[^7]。クエリの件数は `sum(ItemCount)` で補正[^1][^7]。
- **計装無効化のトレードオフ**: 依存関係計装を切ると Application Map と下流テレメトリが失われる[^6]。
- **`AppDependencies` は Basic Logs 非対応**: 単価を下げる主手段はコミットメント階層[^1][^10]。
- **transformation × Microsoft Sentinel**: Sentinel 有効ワークスペースの Analytics テーブルでは transformation のデータ処理料金は発生しない。
- **二重計上の可能性**: 同じ HTTP 呼び出しが `AppTraces`（HttpClient のトレース ログ）と `AppDependencies`（依存関係テレメトリ）の両方に出ていることがある。横断で棚卸しするとよい[^3]。

---

[^1]: AppDependencies（テーブル リファレンス: 列定義、DependencyType/Target/Data/Success/DurationMs/ItemCount、Basic log 非対応、Ingestion-time DCR 対応）, https://learn.microsoft.com/azure/azure-monitor/reference/tables/appdependencies

[^2]: Application Insights telemetry data model — Dependency telemetry（依存関係テレメトリの定義とフィールド）, https://learn.microsoft.com/azure/azure-monitor/app/data-model-complete

[^3]: Dependency tracking in Application Insights（自動収集される依存関係 HTTP/SQL/Azure SDK、DependencyTrackingTelemetryModule）, https://learn.microsoft.com/azure/azure-monitor/app/dependencies

[^4]: Cost optimization in Azure Monitor — Application Insights（設計チェックリスト: ワークスペース ベース移行、サンプリング、不要モジュール無効化）, https://learn.microsoft.com/azure/azure-monitor/fundamentals/best-practices-cost

[^5]: Sampling in Azure Monitor Application Insights with OpenTelemetry（既定で無効、SamplingRatio、RetainedPercentage 確認、ingestion sampling は非推奨）, https://learn.microsoft.com/azure/azure-monitor/app/opentelemetry-sampling

[^6]: Troubleshoot high data ingestion in Application Insights — dependencies テーブルのコスト削減（サンプリング オーバーライド、計装無効化のトレードオフ）, https://learn.microsoft.com/troubleshoot/azure/azure-monitor/app-insights/telemetry/troubleshoot-high-data-ingestion

[^7]: Sampling in Application Insights（推奨手段、関連項目をまとめて選択、メトリクスは再正規化、ItemCount、高サンプリング率でのクエリ精度低下）, https://learn.microsoft.com/azure/azure-monitor/app/sampling-classic-api

[^8]: Sampling in Application Insights — Adaptive sampling（UseAdaptiveSampling、excludedTypes で Dependency を対象/除外）, https://learn.microsoft.com/azure/azure-monitor/app/sampling-classic-api

[^9]: Filter Azure Monitor OpenTelemetry — Filter telemetry at ingestion using DCR（AppDependencies の transformKql サンプル: 失敗/遅延フィルタ、SQL 文除去、合成トラフィック除外、AppRoleName スコープ）, https://learn.microsoft.com/azure/azure-monitor/app/opentelemetry-filter

[^10]: Azure Monitor Logs cost calculations and options — Commitment tiers, https://learn.microsoft.com/azure/azure-monitor/logs/cost-logs
