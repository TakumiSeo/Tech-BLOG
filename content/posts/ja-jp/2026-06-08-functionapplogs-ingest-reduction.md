Title: FunctionAppLogs のインジェストを削減する手順（Azure Functions / Log Analytics）
Date: 2026-06-08
Slug: functionapplogs-ingest-reduction
Lang: ja-jp
Category: notebook
Tags: azure, azure-monitor, azure-functions, log-analytics, cost-optimization, observability
Summary: Azure Functions の診断設定で収集される FunctionAppLogs テーブルが大きなインジェストを占める環境向けに、host.json ログレベル / 診断設定のカテゴリ選択 / Workspace transformation DCR / コミットメント階層までを Microsoft Learn 根拠で順序立てて整理。AppTraces とは異なる「リソース ログ（診断設定）」特有の削減ルートを扱う。

`AppTraces`（Application Insights）の削減に続いて、ログ コスト分析で 2 番目に大きくなりがちなのが Azure Functions の `FunctionAppLogs` テーブルです。本記事では、Microsoft Learn 公式ドキュメントに基づいて、**効果が大きく実装コストが低い順**に削減手順を整理します。

> 前提の違い: `AppTraces` は Application Insights のテレメトリ経路でしたが、**`FunctionAppLogs` は診断設定（diagnostic settings）経由で収集される「リソース ログ」テーブル**です[^2][^3]。このため削減の主役は SDK サンプリングではなく、**host.json のログレベル**と**診断設定 / Workspace transformation DCR** に移ります。

## 1. FunctionAppLogs とは何か（前提整理）

`FunctionAppLogs` は **Function App（`microsoft.web/sites`）の診断設定** で `FunctionAppLogs` カテゴリを Log Analytics ワークスペースへ送ったときに作成されるテーブルです。**Functions ホストが出力するログと、ユーザー コードが出力するログの両方**を含みます[^1][^3]。

### 1.1 収集経路（AppTraces との最大の違い）

リソース ログは**診断設定を作成して送信先（Log Analytics / Storage / Event Hubs）へルーティングするまで収集・保存されません**[^2]。つまり、

- 収集を止める / 送信先を変える操作が**診断設定の構成だけ**で完結する
- 一方で、診断設定は**カテゴリ単位でしか選択できず、カテゴリ内部の粒度フィルタ（ログレベル等）はできない**[^8]

という性質を持ちます。粒度フィルタは host.json（出力元）か Workspace transformation DCR（取り込み時）で行うことになります。

### 1.2 ログ レベル（Level / LevelId）の定義

`FunctionAppLogs` の `Level`（文字列）と `LevelId`（整数）は以下です[^1]。

| LevelId | Level |
|---|---|
| 0 | Trace |
| 1 | Debug |
| 2 | Information |
| 3 | Warning |
| 4 | Error |
| 5 | Critical |

> 重要: これは `AppTraces` の `SeverityLevel`（`1 = Information`）とは**マッピングが異なります**。`FunctionAppLogs` では **`Information` は `LevelId == 2`** です。KQL で Verbose / Debug / Information を除外する場合は `LevelId >= 3`（Warning 以上）が基準になります[^1]。
>
> host.json 側の `LogLevel` 列挙（`Trace=0, Debug=1, Information=2, Warning=3, Error=4, Critical=5, None=6`）とも一致します[^4]。

### 1.3 FunctionAppLogs の主なフィールド

`AppName`、`FunctionName`、`Category`、`Level`、`LevelId`、`Message`、`HostInstanceId`、`RoleInstance`、`FunctionInvocationId`、`ExceptionType` / `ExceptionMessage` / `ExceptionDetails`、`_BilledSize`、`_IsBillable` 等を持ちます[^1]。コスト分析では `_BilledSize` と `_IsBillable` が中心指標です。

### 1.4 テーブルの機能サポート（重要な制約）

| 項目 | 値 | 影響 |
|---|---|---|
| Basic Logs プラン | **非対応（No）** | `AppTraces` と異なり **Basic Logs への切り替えはできない**[^1][^3][^11] |
| Ingestion-time DCR transformation | **対応（Yes）** | Workspace transformation DCR で取り込み時フィルタが可能[^1][^11] |

> したがって `FunctionAppLogs` では「Basic Logs で単価を下げる」という `AppTraces` の手段が使えません。**取り込み量そのものを減らす**施策（host.json / 診断設定 / transformation）の比重が相対的に高くなります。

## 2. 削減アプローチの優先順位（Microsoft Learn ベストプラクティス）

Microsoft のコスト最適化ガイダンスは、リソース ログ（診断設定）について次を挙げています[^9][^8]。

1. **必要なログ カテゴリだけを収集する**（診断設定で不要カテゴリを送らない）[^9]
2. **出力元でログ量を減らす**（Azure Functions では host.json の `logging.logLevel`）[^4]
3. **Workspace transformation DCR で取り込み時フィルタ**（診断設定はカテゴリ内の粒度フィルタができないため）[^8][^9][^10]
4. 残った量に対して**コミットメント階層**で単価を最適化[^13]

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

`FunctionAppLogs` を `LevelId` 別に集計（`_BilledSize`, `_IsBillable` は全テーブル共通の標準列）[^1]:

```kusto
FunctionAppLogs
| where TimeGenerated > ago(1d)
| where _IsBillable == true
| summarize Records = count(), BillableGB = sum(_BilledSize)/1024/1024/1024
        by LevelId, Level
| order by LevelId asc
```

`AppName` / `FunctionName` / `Category` 別の課金ボリューム（上位）[^1][^7]:

```kusto
FunctionAppLogs
| where TimeGenerated > ago(7d)
| where _IsBillable == true
| summarize BillableGB = sum(_BilledSize)/1024/1024/1024, Records = count()
        by AppName, FunctionName, Category
| top 50 by BillableGB desc
```

典型的なデバッグ環境では、`LevelId == 2`（Information）が大半を占めることが多く、その場合の目標は「**どの Function / Category が Information を出しているか**を特定し、その対象だけログレベルを上げる」ことになります（→ 手順 1、第 6 章）。

### 手順 1 — host.json でログ レベルを調整する（最優先・効果最大）

Azure Functions では、**host.json の `logging.logLevel`** が「functions アプリがどれだけログを出すか」を決めます。カテゴリごとに送信する**最小ログ レベル**を指定します[^4][^5]。

#### 1.1 既定を Warning に下げ、必要カテゴリのみ Information を残す

`default` を `Warning` にして不要カテゴリの過剰ログを抑え、Function 実行に必要なカテゴリだけ `Information` に設定する例（v2.x 以降）[^4]:

```json
{
  "logging": {
    "fileLoggingMode": "debugOnly",
    "logLevel": {
      "default": "Warning",
      "Host.Aggregator": "Trace",
      "Host.Results": "Information",
      "Function": "Information"
    }
  }
}
```

特定の Function だけ詳細度を変えることもできます（`Function.<関数名>`）。`None` を指定するとそのカテゴリのログを完全に停止できます[^4][^5]。

```json
{
  "logging": {
    "logLevel": {
      "default": "Warning",
      "Function.NoisyFunction": "Error"
    }
  }
}
```

> 注意（メトリクス喪失のリスク）: `Host.Aggregator` / `Host.Results` のレベルを **`Information` より高く**設定すると、関数実行のメトリクス / パフォーマンス データや成功実行の表示が失われる可能性があります[^4]。これらは下げ過ぎないでください。

#### 1.2 再デプロイせずにアプリ設定で上書きする

host.json を変更せずに本番のログ挙動を即時に変えたい場合、`AzureFunctionsJobHost__logging__logLevel__<path>` 形式のアプリ設定で host.json 値を上書きできます（ドット `.` は二重アンダースコア `__` に置換）[^6]。

```azurecli
az functionapp config appsettings set \
  --name MyFunctionApp --resource-group MyResourceGroup \
  --settings "AzureFunctionsJobHost__logging__logLevel__default=Warning"
```

> 注: アプリ設定による host.json 上書きは **Function App を再起動**します。また、Linux の Elastic Premium / Dedicated（App Service）プランでは**ピリオドを含むアプリ設定がサポートされない**ため、その場合は host.json ファイルを使用してください[^6]。

### 手順 2 — 診断設定を見直す（カテゴリ選択 / 送信先）

リソース ログのコストは送信先と量で決まります。Microsoft は診断設定のコスト管理として次を挙げています[^8][^9]。

1. **各サービスで必要なログ カテゴリだけを収集する**（`FunctionAppLogs` が本当に必要か棚卸し）
2. プラットフォーム メトリクスは、ログ クエリでの複雑な分析が必要でない限り収集しない（メトリクスは診断設定なしで Metrics Explorer から利用可能）
3. カテゴリ内の粒度フィルタは診断設定ではできないため、**transformation を使う**（手順 3）

監査アーカイブ等「即時のログ検索やアラートには使わないが保管したい」ログは、**Log Analytics への送信を止めて Storage アーカイブのみに切り替える**選択肢もあります[^8]。

### 手順 3 — Workspace transformation DCR（取り込み時フィルタ）

診断設定で送られるリソース ログは通常の DCR を使わない収集経路のため、Microsoft は **Workspace transformation DCR**（ワークスペースに直接適用される特別な DCR）でフィルタ / 変形することを推奨しています[^10][^9]。

- `FunctionAppLogs` は **ingestion-time DCR transformation 対応テーブル**[^1][^11]
- Workspace DCR はワークスペースごとに **1 つ**で、複数テーブルの transformation を含められる[^10]
- 既定の Azure ポータル ウィザード（`Log Analytics workspace > Tables > Create transformation`）から構成可能[^10]

Verbose / Debug / Information を取り込み前に除外する例（Warning 以上のみ保持）[^14]:

```kusto
source
| where LevelId >= 3     // 0=Trace, 1=Debug, 2=Information を除外
```

特定の Function だけ Information を残し、それ以外は Warning 以上に絞る例:

```kusto
source
| where LevelId >= 3 or FunctionName == "OrderProcessor"
```

#### 3.1 Transformation のコスト（重要）[^12]

| テーブル プラン | Transformation のコスト |
|---|---|
| **Analytics**（`FunctionAppLogs` は Basic 非対応のため通常こちら） | Transformation 自体は通常無料。ただし**取り込みデータ量を 50% を超えて削減した場合、超過分はデータ処理料金として課金**。計算式: `[削減した GB] - ([受信 GB] / 2)` |
| **Auxiliary Logs** | 受信データ全量にデータ処理料金が課金され、加えて取り込み後の量に取り込み料金が課金 |
| Microsoft Sentinel が有効な場合 | Analytics テーブルへの transformation は**金額がいくら削減されても無料**[^12] |

計算例[^12]: 受信 20 GB に対し 12 GB を削減 → 取り込み 8 GB / データ処理課金 2 GB（= 12 − 20/2）/ 取り込み課金 8 GB。

> したがって、**まず host.json と診断設定で出力元の量を減らし、transformation は補助的に使う**のがコスト構造上も合理的です[^9][^12]。

### 手順 4 — Daily Cap / Commitment Tier（ワークスペース レベル）

`FunctionAppLogs` 固有の手段を尽くした後は、ワークスペース全体の施策に移ります。

- **Daily Cap**: 予期しないスパイクへのセーフティ ネット。コスト削減の主要手段ではない[^9]
- **Commitment Tier**: 削減後に残った取り込み量が 100 GB/day 以上で安定していれば、Pay-as-you-go から移行して単価を下げられる。`Usage and estimated costs` 画面に各階層の推定が表示される[^13]

> 注: `FunctionAppLogs` は **Basic Logs 非対応**[^1][^11]のため、`AppTraces` で使えた「デバッグ用テーブルを Basic Logs に切り替えて単価を下げる」手段は適用できません。残量に対してはコミットメント階層が主な単価最適化手段になります。

## 4. 推奨実行順序（まとめ表）

| # | アクション | 効果 | リスク |
|---|---|---|---|
| 1 | 現状把握 KQL（手順 0） | — | なし |
| 2 | host.json `logging.logLevel` の `default` を `Warning` に、ノイズの多い `Function.<名前>` を `Error` に[^4] | **大**（出力元で Verbose / Debug / Information を破棄） | `Host.Aggregator` / `Host.Results` を上げ過ぎるとメトリクス喪失[^4] |
| 3 | 診断設定で不要カテゴリを停止 / 監査ログは Storage アーカイブへ[^8] | 中〜大 | 監視 / トラブルシュート可視性の低下 |
| 4 | Workspace transformation DCR で `LevelId < 3` を除外[^10] | 中 | 50% 超の削減で transformation 料金（手順 3.1）[^12] |
| 5 | Commitment Tier に移行[^13] | 中（単価引き下げ） | 31 日コミット |
| — | Basic Logs への切り替え | **不可**（テーブル非対応）[^1][^11] | — |

## 5. Function / Category 別に「犯人」を特定する KQL クエリ集

現状把握で `LevelId == 2`（Information）が支配的な場合、ゴールは「**どの Function / Category が Information を出しているか**を特定して、その対象だけ host.json でレベルを上げる」ことです。`AppName` / `FunctionName` / `Category` / `_BilledSize` / `_IsBillable` は `FunctionAppLogs` の公式スキーマに存在します[^1]。

### 5.1 FunctionName ごとの課金量（パレート確認）

```kusto
FunctionAppLogs
| where TimeGenerated > ago(7d)
| where _IsBillable == true
| summarize BillableGB = sum(_BilledSize) / 1024 / 1024 / 1024,
            Records   = count()
        by FunctionName
| order by BillableGB desc
```

### 5.2 FunctionName × LevelId のクロス集計

```kusto
FunctionAppLogs
| where TimeGenerated > ago(7d)
| where _IsBillable == true
| summarize BillableGB = sum(_BilledSize) / 1024 / 1024 / 1024
        by FunctionName, Level
| evaluate pivot(Level, sum(BillableGB))
| order by Information desc
```

どの Function が Information を大量に出しているかが一目で分かります。

### 5.3 Category 別（ホスト ログかユーザー ログかの判別）

```kusto
FunctionAppLogs
| where TimeGenerated > ago(1d)
| where _IsBillable == true
| where LevelId == 2          // Information
| summarize BillableGB = sum(_BilledSize) / 1024 / 1024 / 1024,
            Records   = count()
        by Category
| top 30 by BillableGB desc
```

`Host.*`（ホスト発）か `Function.<名前>`（ユーザー コード発）かで、host.json のどのカテゴリを絞るべきかが決まります[^4][^15]。

### 5.4 Message パターン（同一メッセージの量産検出）

```kusto
FunctionAppLogs
| where TimeGenerated > ago(1d)
| where _IsBillable == true
| where LevelId == 2
| extend MsgHead = substring(Message, 0, 80)
| summarize BillableMB = sum(_BilledSize) / 1024 / 1024,
            Records   = count()
        by FunctionName, MsgHead
| top 50 by BillableMB desc
```

`Executed '...' (Succeeded ...)` のような実行結果ログ（`Host.Results` / `Function.*` 由来）や、バインディング / リトライの定型ログを炙り出せます[^7]。

### 5.5 時系列（デプロイ後スパイクの確認）

```kusto
FunctionAppLogs
| where TimeGenerated > ago(7d)
| where _IsBillable == true
| summarize BillableGB = sum(_BilledSize) / 1024 / 1024 / 1024
        by bin(TimeGenerated, 1h), FunctionName
| render timechart
```

### 5.6 Information 偏重環境の次アクション例

`LevelId == 2` が支配的な環境では、次の順序が最短です。

1. 5.1 / 5.2 で上位の `FunctionName`、5.3 で `Category` を特定
2. host.json の `default` を `Warning` に下げ、必要な Function だけ `Information` を維持[^4]:

   ```json
   {
     "logging": {
       "logLevel": {
         "default": "Warning",
         "Host.Results": "Information",
         "Function.CriticalFunction": "Information"
       }
     }
   }
   ```

   Information 比率が高い環境では、この設定だけで `FunctionAppLogs` の取り込み量を大幅に削減できます。
3. 「特定メッセージだけ消したい」ケースは、5.4 で特定したメッセージを Workspace transformation DCR で除外（手順 3 参照）[^10][^12]

## 6. 実ケース: `IHttpClientFactory` の標準ログが取り込みの大半を占めていた事例

実環境で 5.3 / 5.4 のクエリを実行したところ、課金量の上位がすべて**特定ジョブのユーザー カテゴリ**で、各ジョブが約 4.5 GB / 約 1,280 万レコードに達していた、というケースがありました（以下はマスク値）。

| Category | BillableGB | Records |
|---|---|---|
| `Function.NotifyJobA.User` | 4.57 | 12,817,621 |
| `Function.NotifyJobB.User` | 4.52 | 12,820,290 |
| `Function.NotifyJobC.User` | 4.49 | 12,820,251 |
| `Function.NotifyJobD.User` | 4.46 | 12,816,184 |
| ...（同形の Notify 系ジョブが続く） | 約 4.3〜4.4 | 約 1,280 万 |
| `Function.GetResult.User` | 0.014 | 25,753 |
| `Function.NotifyJobA`（`.User` なし） | 0.013 | 30,266 |

### 6.1 読み取れること

- カテゴリ末尾の **`.User` はユーザー コードの `ILogger` 出力**を表す。`.User` の付かない `Function.<名前>`（ホスト実行ログ）は各 0.013 GB と桁違いに小さく、**ほぼ全量がユーザー カテゴリ側**だった。
- 上位ジョブの `Message` を 5.4 で確認すると、内容は `Start processing HTTP request POST ...` と `Sending HTTP request POST https://...` のペアだった。

### 6.2 犯人は「自前の LogInformation」ではなく `IHttpClientFactory` の標準ログ

この 2 つのメッセージは、開発者が書いた `LogInformation(...)` ではなく、**`IHttpClientFactory` 経由で作成した `HttpClient` が全リクエストに対して既定で出力する標準ログ**です。公式ドキュメントは「`IHttpClientFactory` 経由で作成したクライアントは全リクエストのログ メッセージを記録する。既定のログ メッセージを見るには適切な Information レベルを有効化する」と明記しています[^16]。つまりこれらは **Information レベル**で出力されます[^16]。

メッセージとログ カテゴリの対応は次の通りです[^16]。

| メッセージ | ログ カテゴリ | 出力タイミング |
|---|---|---|
| `Start processing HTTP request ...` | `System.Net.Http.HttpClient.<クライアント名>.LogicalHandler` | ハンドラー パイプラインの外側 |
| `Sending HTTP request ...` | `System.Net.Http.HttpClient.<クライアント名>.ClientHandler` | パイプライン内側・送信直前 |

1 リクエストにつき処理開始・送信・応答で複数行が Information で出るため、外部 API を高頻度に呼ぶジョブでは数千万レコード規模に膨らみます。Azure Functions ではこれらが**関数実行中の `ILogger` ログとして `Function.<関数名>.User` カテゴリに集約**されて `FunctionAppLogs` に記録されるため、集計上は `System.Net.Http.HttpClient.*` ではなく `Function.*.User` として現れます[^15]。

### 6.3 対処 A — host.json で発生源を抑制（コード変更が可能なら最短）

発生源のカテゴリを Warning に下げます。`FunctionAppLogs` テーブル上の `.User` 集計を確実に止めるため、HttpClient カテゴリと対象ジョブのプレフィックスの両方を指定すると堅実です[^4]。

```json
{
  "logging": {
    "logLevel": {
      "default": "Information",
      "System.Net.Http.HttpClient": "Warning",
      "Function.Notify": "Warning"
    }
  }
}
```

- `System.Net.Http.HttpClient: Warning` … HttpClient 標準ログを発生源で抑制（他の関数にも横断的に効く）[^4][^16]
- `Function.Notify: Warning` … 前方一致で `Function.Notify*Job` 系をまとめて抑制（`.User` 配下を含む）[^4]

### 6.4 対処 B — DCR transformation で取り込み時に除外（コード変更が難しい場合）

アプリの再デプロイや host.json 変更が難しい場合は、**Workspace transformation DCR で取り込み時に落とす**のが現実的です。`FunctionAppLogs` は ingestion-time DCR transformation 対応テーブルなので適用できます[^1][^11]。`Log Analytics workspace > Tables > FunctionAppLogs > Create transformation` から構成します[^10]。

HttpClient の正常系ログ（Information かつ該当メッセージ）だけを狙い撃ちで除外する例:

```kusto
source
| where not(LevelId == 2 and (Message startswith "Start processing HTTP request"
                          or Message startswith "Sending HTTP request"
                          or Message startswith "Received HTTP response"
                          or Message startswith "End processing HTTP request"))
```

メッセージ文字列に依存させたくない場合は、対象ジョブの Information を一括除外する例（Warning 以上と他関数の Information は保持）:

```kusto
source
| where not(LevelId == 2 and Category startswith "Function.Notify")
```

> コスト上の注意（手順 3.1 再掲）: transformation で**取り込み量を 50% 超削減すると、超過分にデータ処理料金**がかかります（計算式 `[削減 GB] − [受信 GB] / 2`）。今回のように Notify 系だけで全体の大半を占める場合は 50% を超えやすいので、可能なら host.json（対処 A）で先に削ってから transformation を補助に使うとデータ処理料金を避けられます。Microsoft Sentinel 有効ワークスペースの Analytics テーブルなら、この処理料金は発生しません[^12]。

### 6.5 対処 C — クライアント単位でログを無効化（根本対応・任意）

コード変更が可能なら、対象クライアントの標準ログだけを除去する方法もあります（.NET 8 以降）[^17]。

```csharp
builder.Services.AddHttpClient("Notify")
    .RemoveAllLoggers();
```

これなら正常系の通信ログだけが消え、失敗やタイムアウトは自前の例外処理で引き続き捕捉できます。なお、リクエスト単位の追跡が本当に必要な場合は、`FunctionAppLogs` の Information を量産するのではなく Application Insights の依存関係テレメトリ（`AppDependencies`）で見るのが本来の置き場所です。

### 6.6 適用後の効果測定 KQL

```kusto
FunctionAppLogs
| where TimeGenerated > ago(1d)
| where _IsBillable == true
| where Category startswith "Function.Notify"
| summarize BillableGB = sum(_BilledSize)/1024/1024/1024, Records = count()
        by bin(TimeGenerated, 1h)
| render timechart
```

host.json 反映（最大数分の再起動）または transformation 反映（最大 90 分[^8]）の後、この線が落ちれば成功です。

## 7. 注意点（横断的な制約まとめ）

- **診断設定はカテゴリ内の粒度フィルタができない**。ログレベル単位のフィルタは host.json（出力元）か transformation（取り込み時）で行う[^8]。
- **メトリクス / パフォーマンス データの喪失**: host.json で `Host.Aggregator` / `Host.Results` を `Information` より高くすると失われる[^4]。
- **`FunctionAppLogs` は Basic Logs 非対応**: 単価を下げる主手段はコミットメント階層[^1][^11][^13]。
- **transformation × Microsoft Sentinel**: Sentinel が有効なワークスペースの Analytics テーブルでは transformation のデータ処理料金は発生しない[^12]。
- **診断設定の反映遅延**: 設定後、データ送信開始まで最大 90 分かかることがある[^8]。

---

[^1]: FunctionAppLogs（テーブル リファレンス: 列定義、Level/LevelId、Basic log 非対応、Ingestion-time DCR 対応）, https://learn.microsoft.com/azure/azure-monitor/reference/tables/functionapplogs

[^2]: Monitor Azure Functions（Azure Monitor resource logs / 診断設定でのルーティング）, https://learn.microsoft.com/azure/azure-functions/monitor-functions

[^3]: Azure Functions monitoring data reference（Resource logs: FunctionAppLogs カテゴリ, Basic log No / transformation Yes）, https://learn.microsoft.com/azure/azure-functions/monitor-functions-reference

[^4]: How to configure monitoring for Azure Functions — Configure log levels（host.json logging.logLevel, レベル表, カテゴリ）, https://learn.microsoft.com/azure/azure-functions/configure-monitoring

[^5]: host.json reference for Azure Functions 2.x and later — logging, https://learn.microsoft.com/azure/azure-functions/functions-host-json

[^6]: How to configure monitoring for Azure Functions — Overriding monitoring configuration at runtime（AzureFunctionsJobHost__logging__logLevel 上書き）, https://learn.microsoft.com/azure/azure-functions/configure-monitoring

[^7]: Queries for the FunctionAppLogs table（サンプル クエリ）, https://learn.microsoft.com/azure/azure-monitor/reference/queries/functionapplogs

[^8]: Diagnostic settings in Azure Monitor — Controlling costs, https://learn.microsoft.com/azure/azure-monitor/platform/diagnostic-settings

[^9]: Cost optimization in Azure Monitor（Collect only critical resource log data / workspace transformation）, https://learn.microsoft.com/azure/azure-monitor/fundamentals/best-practices-cost

[^10]: Transformations in Azure Monitor — Workspace transformation DCR, https://learn.microsoft.com/azure/azure-monitor/data-collection/data-collection-transformations

[^11]: Supported logs for Microsoft.Web/sites（FunctionAppLogs: Basic log No, transformation Yes）, https://learn.microsoft.com/azure/azure-monitor/reference/supported-logs/microsoft-web-sites-logs

[^12]: Transformations in Azure Monitor — Cost for transformations（50% ルール, 計算式, Sentinel 例外）, https://learn.microsoft.com/azure/azure-monitor/data-collection/data-collection-transformations

[^13]: Azure Monitor Logs cost calculations and options — Commitment tiers, https://learn.microsoft.com/azure/azure-monitor/logs/cost-logs

[^14]: Sample transformations in Azure Monitor — Reduce data costs（where による行フィルタ）, https://learn.microsoft.com/azure/azure-monitor/data-collection/data-collection-transformations-samples

[^15]: Monitor executions in Azure Functions — Log levels and categories, https://learn.microsoft.com/azure/azure-functions/functions-monitoring

[^16]: Make HTTP requests with IHttpClientFactory in ASP.NET Core — Log messages and response status（既定で全リクエストを Information で記録、LogicalHandler / ClientHandler カテゴリ）, https://learn.microsoft.com/aspnet/core/fundamentals/http-requests

[^17]: HTTP client logging in .NET（既定ロガーの差し替え / 無効化、AddExtendedHttpClientLogging）, https://learn.microsoft.com/dotnet/core/extensions/httpclient-logging
