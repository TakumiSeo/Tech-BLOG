Title: AppRequests のインジェストを削減する手順（Application Insights / Log Analytics）
Date: 2026-06-08
Slug: apprequests-ingest-reduction
Lang: ja-jp
Category: notebook
Tags: azure, azure-monitor, application-insights, log-analytics, cost-optimization, observability
Summary: Application Insights の AppRequests テーブル（受信リクエストのテレメトリ）が大きなインジェストを占める環境向けに、SDK サンプリング / ヘルスチェック・合成トラフィックの除外 / 失敗・遅延のみ保持 / DCR 変換 / コミットメント階層までを Microsoft Learn 根拠で順序立てて整理。AppDependencies と OperationId で対をなす受信側テレメトリ特有の削減ルートを扱う。

ログ コスト分析の最後として、Application Insights の `AppRequests` テーブルを扱います。`AppDependencies`（送信＝外部呼び出し）と OperationId で対をなす、**受信リクエストのテレメトリ**です。本記事では Microsoft Learn 公式ドキュメントに基づき、**効果が大きく実装コストが低い順**に削減手順を整理します。

> 前提の整理: `AppRequests` は **アプリが受信した HTTP リクエストのテレメトリ**（`requests` テーブル）です[^1][^2]。`AppServiceHTTPLogs`（Web サーバー ログ）と同じく「受信」を記録しますが、こちらは Application Insights の経路で、**OperationId による分散トレース相関**を持ちます。同じ受信を `AppServiceHTTPLogs` と二重計上している可能性があり、削減判断ではその棚卸しも重要です。`AppTraces` / `AppDependencies` と同じ Application Insights 経路のため、削減の主役は **SDK サンプリング**です。

## 1. AppRequests とは何か（前提整理）

`AppRequests` は Application Insights の **リクエスト テレメトリ**（`requests` テーブル）を Log Analytics 側から参照するテーブル名です。「アプリへの受信 HTTP リクエストによってトリガーされた論理的な実行シーケンス」を表し、**リクエスト 1 件 = 1 行**で記録されます[^1][^2]。

### 1.1 何が記録されるか

リクエスト テレメトリは、Web ベース サービスのパフォーマンスと成否を監視するための情報です[^2]。

- アプリが受信した HTTP リクエスト（`Name` = `GET /values/{id}` のようなメソッド + ルート テンプレート）[^2]
- 実行の成否（`Success`）、結果コード（`ResultCode`）、所要時間（`DurationMs`）[^2]
- `OperationId` による相関（その処理中に発生した依存呼び出し `AppDependencies` や例外 `AppExceptions` と紐づく）[^1]

> 補足: `AppRequests`（受信テレメトリ）と `AppServiceHTTPLogs`（Web サーバー ログ）は**どちらも受信を記録**しますが、経路が異なります。前者は Application Insights（アプリ視点・相関あり・サンプリング可）、後者は App Service 診断ログ（Web サーバー視点・相関なし）。同じリクエストが両方に出ていることがあり、二重計上の棚卸し対象です。

### 1.2 AppRequests の主なフィールド

| 列 | 内容 |
|---|---|
| `Name` | リクエスト名（`GET /values/{id}` のようなメソッド + ルート テンプレート。低カーディナリティ）[^2] |
| `Url` | 全クエリ文字列付きのリクエスト URL[^2] |
| `Success` | アプリがリクエストを正常処理したか（bool）[^1][^2] |
| `ResultCode` | 結果コード（HTTP ステータス）[^1][^2] |
| `DurationMs` | 処理所要時間（ミリ秒）[^1] |
| `OperationId` / `Id` / `ParentId` | 相関 ID（依存・例外・トレースと紐づく）[^1] |
| `OperationName` | 操作名（通常 `Name` と一致）[^1] |
| `SyntheticSource` | 合成トラフィック（外形監視・可用性テストなど）の発生源[^1] |
| `Source` | リクエスト元（接続文字列や呼び出し元 IP）[^2] |
| `ItemCount` | 1 サンプル項目が表す実テレメトリ件数（サンプリング補正に使用）[^1] |
| `AppRoleName` / `AppRoleInstance` | アプリのロール名 / インスタンス[^1] |
| `ClientIP` / `ClientCity` 等 | クライアント情報[^1] |
| `_BilledSize` / `_IsBillable` | 課金サイズ / 課金対象フラグ |

コスト分析では `_BilledSize` / `_IsBillable` が中心指標で、`Url`（全クエリ文字列付き）や `Properties` が 1 件のサイズを押し上げやすい列です。

### 1.3 テーブルの機能サポート（重要な制約）

| 項目 | 値 | 影響 |
|---|---|---|
| Basic Logs プラン | **非対応（No）** | `AppRequests` は Basic Logs への切り替えはできない[^3] |
| Ingestion-time DCR transformation | **対応（Yes）** | Workspace transformation DCR で取り込み時の行・列フィルタが可能[^3] |

## 2. 削減アプローチの優先順位（Microsoft Learn ベストプラクティス）

Microsoft の Application Insights コスト最適化チェックリストでは、優先度の高いものから次が挙げられています[^4]。

1. **ワークスペース ベース Application Insights への移行**（Basic Logs / コミットメント階層などのコスト機能を利用可能にする）[^4]
2. **サンプリングでデータ量を調整**（OpenTelemetry サンプリングが「主要なツール」と明記）[^4][^5]
3. **不要なモジュール（計装）を無効化**[^4]
4. 更新された SDK の使用[^4]

`requests` に固有の論点として、**ヘルスチェックや合成トラフィックの抑制**が効果的です（手順 2・3）。

## 3. 推奨削減手順（優先度高 → 低）

### 手順 0 — 現状把握用 KQL クエリ

ワークスペース全体のテーブル別課金ボリュームの推移（直近 31 日）[^3]:

```kusto
Usage
| where TimeGenerated > ago(32d)
| where StartTime >= startofday(ago(31d)) and EndTime < startofday(now())
| where IsBillable == true
| summarize BillableDataGB = sum(Quantity) / 1000. by bin(StartTime, 1d), DataType
| render columnchart
```

`AppRequests` を成否 × 合成有無で集計[^1]:

```kusto
AppRequests
| where TimeGenerated > ago(1d)
| where _IsBillable == true
| summarize Records = count(), BillableGB = sum(_BilledSize)/1024/1024/1024
        by Success, IsSynthetic = isnotempty(SyntheticSource)
| order by BillableGB desc
```

サンプリングが既に効いているかの確認（`ItemCount` から保持率を逆算）[^5]:

```kusto
AppRequests
| where TimeGenerated > ago(1d)
| summarize RetainedPercentage = 100.0 / avg(ItemCount) by bin(TimeGenerated, 1h)
| render timechart
```

`RetainedPercentage` が 100 未満なら、すでにサンプリングされています[^5]。

### 手順 1 — SDK サンプリングを有効化 / 強化する（最優先・効果最大）

Microsoft はサンプリングを「テレメトリ量・データ コスト・ストレージ コストを削減しつつ、統計的に正しい分析を保つ**推奨手段**」と位置づけています[^6]。サンプリング フィルターは**関連項目（リクエスト・依存関係・例外・トレース）を同じ `OperationId` 単位でまとめて保持/破棄**するため、分散トレースの整合性が維持されます[^6]。

> 重要: **OpenTelemetry Distro では既定でサンプリングは有効化されていません**[^5]。一方、最新の ASP.NET / ASP.NET Core SDK と **Azure Functions では adaptive sampling が既定で有効**です[^6]。

#### 1.1 OpenTelemetry Distro でのサンプリング設定（.NET）[^5]

```csharp
builder.Services.AddOpenTelemetry().UseAzureMonitor(o =>
{
    o.SamplingRatio = 0.1F;   // 約 10% を保持
});
```

> 注: クエリで件数を数える際は、サンプリング後は `count()` ではなく `sum(ItemCount)` を使う必要があります（`ItemCount` が 1 サンプルあたりの実件数を表す）[^1][^6]。

### 手順 2 — ヘルスチェック / 合成トラフィックを抑制する

`requests` は「ヘルスチェック」と「外形監視（合成トラフィック）」がノイズの主因になりやすいテーブルです。

#### 2.1 Java: サンプリング オーバーライドでヘルスチェックを抑制[^9]

Java エージェントでは、ヘルスチェックへのリクエストを `percentage: 0` で抑制できます。**その配下の下流依存（dependencies）も同時に抑制**されます[^9]。

```json
{
  "sampling": {
    "overrides": [
      {
        "telemetryType": "request",
        "attributes": [
          { "key": "url.path", "value": "/health-check", "matchType": "strict" }
        ],
        "percentage": 0
      }
    ]
  }
}
```

#### 2.2 合成トラフィックの確認

可用性テストや外形監視は `SyntheticSource` に値が入ります[^1]。これが大きな割合なら、取り込み前に落とす候補です（手順 3.3）。

### 手順 3 — Workspace transformation DCR（取り込み時の行・列フィルタ）

SDK 変更が難しい場合は、Workspace transformation DCR で取り込み時に処理します。`AppRequests` は transformation 対応テーブルで、Microsoft 公式に**専用のサンプル**が用意されています[^7]。ストリーム名は `Microsoft-Table-AppRequests` を使います[^7]。

#### 3.1 ヘルスチェック リクエストを除外[^7]

`/health` `/healthz` `/ready` `/readyz` `/live` `/livez` などのヘルス エンドポイントを落とします[^7]。

```kusto
source
| extend url = tolower(tostring(Url))
| where not(url contains '/health' or url contains '/healthz'
         or url contains '/ready' or url contains '/readyz'
         or url contains '/live'  or url contains '/livez')
| project-away url
```

#### 3.2 失敗したヘルスチェックだけ残す（成功ヘルスチェックを除外）[^7]

ヘルスチェックの失敗は監視価値があるため、成功だけを落とす折衷案です[^7]。

```kusto
source
| extend url = tolower(tostring(Url))
| where not((url contains '/health' or url contains '/healthz'
          or url contains '/ready' or url contains '/readyz'
          or url contains '/live'  or url contains '/livez') and Success == true)
| project-away url
```

#### 3.3 合成トラフィックを除外[^7]

`SyntheticSource` が入っているレコード（外形監視・可用性テスト）を落とします[^7]。

```kusto
source
| where isempty(SyntheticSource)
```

#### 3.4 失敗または遅いリクエストだけ残す[^7]

正常・高速リクエストを落とし、失敗（`Success == false`）と遅延（`DurationMs >= 1000`）だけ保持します[^7]。

```kusto
source
| where Success == false or DurationMs >= 1000
```

#### 3.5 特定アプリ（AppRoleName）に絞って適用[^7]

複数アプリがワークスペースを共有している場合、特定アプリだけに条件を適用できます[^7]。

```kusto
source
| where AppRoleName == "<app-role-name>"
| where Success == false or DurationMs >= 1000
```

### 手順 4 — Daily Cap / Commitment Tier（ワークスペース レベル）

- **Daily Cap**: 予期しないスパイクへのセーフティ ネット。サンプリングの代替ではなく最終手段[^5]
- **Commitment Tier**: 削減後に残った取り込み量が 100 GB/day 以上で安定していれば、Pay-as-you-go から移行して単価を下げられる[^8]

> 注: `AppRequests` は **Basic Logs 非対応**[^3]のため、Basic Logs で単価を下げる手段は使えません。残量に対してはコミットメント階層が主な単価最適化手段になります。

## 4. 推奨実行順序（まとめ表）

| # | アクション | 効果 | リスク |
|---|---|---|---|
| 1 | 現状把握 KQL（手順 0） | — | なし |
| 2 | OpenTelemetry サンプリング（`SamplingRatio`）の有効化・強化[^5] | **大** | メトリクスは ItemCount 補正で維持。高サンプリング率でクエリ精度低下[^6] |
| 3 | ヘルスチェック抑制（SDK or DCR）[^7][^9] | 中〜大 | 失敗ヘルスチェックも消える場合あり（3.2 で回避） |
| 4 | DCR 変換: 合成トラフィック除外（`SyntheticSource`）[^7] | 中 | 可用性テストの記録が消える |
| 5 | DCR 変換: 失敗 / 遅延のみ保持（`Success==false or DurationMs>=N`）[^7] | 大 | 正常・高速リクエストの網羅性が下がる |
| 6 | DCR 変換: 列削減（`Url` / `Properties`）[^7] | 中（1 件のサイズ減） | その列での調査ができなくなる |
| 7 | Commitment Tier に移行[^8] | 中（単価引き下げ） | 31 日コミット |
| — | Basic Logs への切り替え | **不可**（テーブル非対応）[^3] | — |

## 5. transformation のコスト（重要）

| テーブル プラン | Transformation のコスト |
|---|---|
| **Analytics**（`AppRequests` は Basic 非対応のため通常こちら） | Transformation 自体は通常無料。ただし**取り込みデータ量を 50% を超えて削減した場合、超過分はデータ処理料金として課金**。計算式: `[削減した GB] − ([受信 GB] / 2)` |
| Microsoft Sentinel が有効な場合 | Analytics テーブルへの transformation は**金額がいくら削減されても無料** |

> 「失敗/遅延のみ保持」のような行フィルタは容易に 50% を超えるため、データ処理料金の対象になりやすいです。まず SDK サンプリングで全体量を下げ、transformation は補助的に使うのが合理的です[^4][^7]。

## 6. 「犯人」を特定する KQL クエリ集

`AppRequests` の `_BilledSize` / `_IsBillable` / `Name` / `Url` / `Success` / `DurationMs` / `SyntheticSource` / `AppRoleName` は公式スキーマに存在します[^1]。

### 6.1 Name（エンドポイント）別の課金量（パレート確認）

```kusto
AppRequests
| where TimeGenerated > ago(7d)
| where _IsBillable == true
| summarize BillableGB = sum(_BilledSize)/1024/1024/1024, Records = count()
        by Name
| top 50 by BillableGB desc
```

特定のエンドポイント（ヘルスチェック / 高頻度ポーリング / 監視）が突出していないかを見ます。

### 6.2 成否 × 所要時間の分布（失敗/遅延のみ残せるか判断）

```kusto
AppRequests
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

`Success == true` かつ短時間が大半なら、手順 3.4（失敗/遅延のみ保持）が大きく効きます。

### 6.3 ヘルスチェック / 合成トラフィックの割合

```kusto
AppRequests
| where TimeGenerated > ago(1d)
| where _IsBillable == true
| extend url = tolower(tostring(Url))
| extend Bucket = case(
        url contains '/health' or url contains '/ready' or url contains '/live', "healthcheck",
        isnotempty(SyntheticSource), "synthetic",
        "normal")
| summarize BillableGB = sum(_BilledSize)/1024/1024/1024, Records = count() by Bucket
| order by BillableGB desc
```

`healthcheck` / `synthetic` が大きな割合なら、手順 2・3 で大きく削減できます。

### 6.4 AppRoleName 別（どのアプリが出しているか）

```kusto
AppRequests
| where TimeGenerated > ago(7d)
| where _IsBillable == true
| summarize BillableGB = sum(_BilledSize)/1024/1024/1024, Records = count()
        by AppRoleName
| order by BillableGB desc
```

### 6.5 AppServiceHTTPLogs との二重計上の確認

同じ受信を `AppServiceHTTPLogs` と `AppRequests` の両方で記録していないか、件数規模を突き合わせます。

```kusto
AppServiceHTTPLogs
| where TimeGenerated > ago(1d)
| summarize Http = count() by Path = tostring(CsUriStem)
| join kind=fullouter (
    AppRequests
    | where TimeGenerated > ago(1d)
    | summarize Req = count() by Path = tostring(Name)
) on Path
| project Path, Http, Req
| order by Req desc
```

件数が近く、両方をアラート/ダッシュボードで使っていないなら、片方（典型的には `AppServiceHTTPLogs`）を Storage アーカイブに回す選択肢があります。ただし用途（IP/UA は HTTPLogs、相関は AppRequests）が異なるため、顧客の利用目的の確認が前提です。

## 7. 実例: API Management が AppRequests の大半を占めていたケース

実環境で `AppRequests` を分析したところ、削減の本丸が **アプリの SDK ではなく Azure API Management（APIM）** だった、というケースがありました。`AppRequests` の削減を考えるとき、発生源が APIM かバックエンドかで打ち手が変わる重要な例です。

### 7.1 成否 × 合成: 99% が正常・非合成

手順 0 の集計（マスク値）:

| Success | IsSynthetic | Records | BillableGB |
|---|---|---|---|
| **true** | false | 5,606,743 | **6.75** |
| false | false | 19,853 | 0.020 |
| false | true | 24,643 | 0.018 |

課金の約 99.4% が「成功・非合成」の正常リクエスト。合成トラフィックはほぼ無く（0.3%）、手順 3.3（合成除外）の効果は限定的です。

### 7.2 成否 × 所要時間: 成功・高速が本丸、「失敗/遅延のみ」は過激

手順 6.2 の分布（マスク値）:

| Success | Duration | BillableGB | Records |
|---|---|---|---|
| **true** | <100ms | **4.41** | 3,658,947 |
| true | 100-500ms | 1.47 | 1,220,955 |
| true | 500ms-1s | 0.54 | 445,774 |
| true | >=1s | 0.34 | 281,099 |
| false | <100ms | 0.034 | 40,481 |
| false | その他 | ~0.003 | 数百〜数千 |

成功・高速（<100ms）だけで 4.41 GB（全体の約 65%）。ここで手順 3.4（`Success==false or DurationMs>=1000`）を当てはめると、残るのは約 0.38 GB（失敗全部 + 成功で 1 秒以上）で、**6.4 GB（94%）が消えます**。一見効果絶大ですが、これは**正常・高速な業務リクエストを 94% 捨てる**ことを意味し、アクセス実績や正常時ベースラインが失われます。失敗が 0.6% しかない健全なシステムほど、このフィルタは過激になります。

より実用的な折衷は「失敗全件 + 遅延全件 + 成功高速はサンプリング」です。

```kusto
source
| where Success == false           // 失敗は全件（障害調査）
    or DurationMs >= 1000           // 遅延は全件（性能調査）
    or hash(OperationId, 10) == 0   // 残り（成功・高速）は約 10%
```

### 7.3 AppRoleName: APIM が 99.7% を占める

手順 6.4 を `AppRoleName` で集計すると、課金の大半が **API Management** でした（マスク値）。

| RoleClass | BillableGB | Records |
|---|---|---|
| **APIM** | **1.22** | 1,012,757 |
| app-...-staging | 0.0011 | 1,553 |
| Function | 0.0008 | 664 |
| その他 staging | わずか | 数百 |

約 99.7% が APIM 発信で、バックエンド（Function / App Service）の `AppRequests` は誤差レベルでした。`OperationId` で確認すると、1 つの OperationId に **APIM とバックエンド（`func-...`）の両方の AppRoleName** が現れ、同一リクエストが両レイヤーで相関していました（二重記録の構造はあるが、量的には APIM 単独問題）。

```kusto
AppRequests
| where TimeGenerated > ago(1h)
| summarize Roles = make_set(AppRoleName) by OperationId
| where array_length(Roles) > 1
| take 20
```

### 7.4 削減: APIM 診断の Sampling (%) を下げる

発生源が APIM だと分かったので、削減は **APIM の Application Insights 連携のサンプリング設定**が直接的かつ最も効きます。

- APIM 診断には **`Sampling (%)`** 設定があり、**既定は 100%（全リクエストをログ）**、0% で記録なし[^11]
- Microsoft 自身が「Application Insights は監査システムではなく、高ボリューム API で個々のリクエストを記録する用途には不向き」と明記[^11]
- 全ログ有効時は **1,000 req/s 超でスループットが 40〜50% 低下**するため、サンプリングは性能面でも推奨[^11]
- **`Always log errors` を有効化**すれば、サンプリングしてもエラーは常に記録される[^11]

設定場所: APIM ポータル → **APIs** → 対象 API（または **All APIs**）→ **Settings** → **Diagnostics Logs** → Application Insights → **Sampling (%)**。裏では `applicationinsights` という Diagnostic エンティティが作成されます[^11]。

```
推奨設定:
  Sampling (%)       : 100 → 10（例）
  Always log errors  : 有効（エラーは全件維持）
  ペイロード ログ      : 既定 0 のまま（ヘッダー/ボディは記録しない）
```

これで `AppRequests`(APIM) は約 1/10 に減り、エラーの監視価値は保たれ、APIM のスループットも改善します。バックエンドの `AppRequests` は誤差なので、まずは APIM の設定が最優先です。

> 補足: APIM の `Sampling (%)` は**バックエンド アプリの SDK サンプリング（`SamplingRatio` 等）とは別系統**です。この環境のように APIM が発生源なら APIM 側を、バックエンドのトレース/依存（`AppTraces` / `AppDependencies`）も重いなら各アプリの SDK サンプリングを、それぞれ設定します。

### 7.5 横断的な気づき（1 リクエストの多テーブル分散）

この環境では、1 つの業務リクエストが複数レイヤー・複数テーブルに分散して記録されていました。

| 発生源 | テーブル |
|---|---|
| APIM | `AppRequests`（APIM 分。本ケースの主因） |
| Function App（`func-...`） | `AppRequests`（バックエンド分）/ `AppDependencies`（下流 HTTP）/ `AppTraces`（HttpClient + 自前ログ）/ `FunctionAppLogs` |
| App Service | `AppServiceHTTPLogs` / `AppServiceIPSecAuditLogs` |

コスト最適化は個別テーブルではなく、**レイヤー（APIM / Function / App Service）ごとの発生源**で捉えるのが要点です。`AppRequests` に関しては、その発生源が APIM だったため、APIM 診断のサンプリングが最短の打ち手になりました。

## 8. 注意点（横断的な制約まとめ）

- **リクエスト = アプリへの受信**: `AppDependencies`（送信）とは向きが逆。`OperationId` で親子相関する[^1][^2]。
- **サンプリングが主役**: Application Insights 経路のため、SDK サンプリングが最優先のレバー。`OperationId` 単位で関連テレメトリをまとめて保持/破棄するため相関が維持される[^4][^5][^6]。
- **Azure Functions / ASP.NET Core は既定で adaptive sampling 有効**: OpenTelemetry Distro は既定で無効なので、計装方式によって現状が異なる[^5][^6]。
- **メトリクスはサンプリングの影響を受けない**: 事前集計メトリクスで正確な値が維持される[^6]。クエリの件数は `sum(ItemCount)` で補正[^1][^6]。
- **ヘルスチェック / 合成トラフィックが主なノイズ**: `requests` 固有の削減ポイント[^7][^9]。
- **`AppRequests` は Basic Logs 非対応**: 単価を下げる主手段はコミットメント階層[^3][^8]。
- **transformation × Microsoft Sentinel**: Sentinel 有効ワークスペースの Analytics テーブルでは transformation のデータ処理料金は発生しない。
- **二重計上の可能性**: 同じ受信が `AppServiceHTTPLogs`（Web サーバー ログ）と `AppRequests`（テレメトリ）の両方に出ていることがある。横断で棚卸しするとよい。

---

[^1]: AppRequests（テーブル リファレンス: 列定義、Name/Url/Success/ResultCode/DurationMs/SyntheticSource/ItemCount、Basic log 非対応、Ingestion-time DCR 対応）, https://learn.microsoft.com/azure/azure-monitor/reference/tables/apprequests

[^2]: Application Insights telemetry data model — Request telemetry（受信リクエストの定義、Name=メソッド+ルート テンプレート、Success/ResultCode/Duration）, https://learn.microsoft.com/azure/azure-monitor/app/data-model-complete

[^3]: AppRequests — Table attributes（Basic log No, Ingestion-time DCR support Yes）, https://learn.microsoft.com/azure/azure-monitor/reference/tables/apprequests

[^4]: Cost optimization in Azure Monitor — Application Insights（設計チェックリスト: ワークスペース ベース移行、サンプリング、不要モジュール無効化）, https://learn.microsoft.com/azure/azure-monitor/fundamentals/best-practices-cost

[^5]: Sampling in Azure Monitor Application Insights with OpenTelemetry（既定で無効、SamplingRatio、RetainedPercentage 確認、ingestion sampling は非推奨）, https://learn.microsoft.com/azure/azure-monitor/app/opentelemetry-sampling

[^6]: Sampling in Application Insights（推奨手段、OperationId 単位で関連項目をまとめて選択、ASP.NET Core/Functions は adaptive 既定有効、ItemCount、メトリクスは常に保持）, https://learn.microsoft.com/azure/azure-monitor/app/sampling-classic-api

[^7]: Filter Azure Monitor OpenTelemetry — Filter telemetry at ingestion using DCR（AppRequests の transformKql サンプル: ヘルスチェック除外、失敗ヘルスチェックのみ保持、合成除外、失敗/遅延フィルタ、AppRoleName スコープ、Microsoft-Table-AppRequests）, https://learn.microsoft.com/azure/azure-monitor/app/opentelemetry-filter

[^8]: Azure Monitor Logs cost calculations and options — Commitment tiers, https://learn.microsoft.com/azure/azure-monitor/logs/cost-logs

[^9]: Configure Azure Monitor Application Insights for Java — Sampling overrides（ヘルスチェックの抑制 percentage:0、配下の下流依存も抑制）, https://learn.microsoft.com/azure/azure-monitor/app/java-standalone-config

[^11]: How to integrate Azure API Management with Azure Application Insights（Sampling (%) 設定、既定 100%、Always log errors、監査用途には不向き、全ログ有効時のスループット 40-50% 低下、applicationinsights Diagnostic エンティティ）, https://learn.microsoft.com/azure/api-management/api-management-howto-app-insights
