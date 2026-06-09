Title: AppTraces 2TB のインジェストを削減する手順（Application Insights / Log Analytics）
Date: 2026-05-26
Slug: apptraces-ingest-reduction
Lang: ja-jp
Category: notebook
Tags: azure, azure-monitor, application-insights, log-analytics, cost-optimization, observability
Summary: Application Insights の AppTraces テーブルが月 2TB に達した環境向けに、SDK ログレベル変更 / サンプリング / DCR 変換 / Basic Logs / Daily Cap / コミットメント階層までを Microsoft Learn 根拠で順序立てて整理。

開発者デバッグ用にすべてのトレースを Application Insights に送り続けた結果、`AppTraces` テーブルだけで月 2TB のインジェストが発生する、という状態は珍しくありません。本記事では、Microsoft Learn 公式ドキュメントに基づいて、**効果が大きく実装コストが低い順**に削減手順を整理します。

## 1. AppTraces とは何か（前提整理）

`AppTraces` は Application Insights の **Trace（トレース ログ）テレメトリ** が格納されるテーブルです。Application Insights 内部では `traces` テーブルとして扱われ、Log Analytics 側で `AppTraces` として参照されます[^1][^2]。

### 1.1 主な発生源

Trace テレメトリは「printf スタイルのトレース ステートメント」を表し、以下から生成されます[^2][^3]。

- `TelemetryClient.TrackTrace()`（Classic SDK の直接呼び出し）
- `ILogger<T>` 経由のログ出力（`Microsoft.Extensions.Logging.ApplicationInsights` プロバイダーが ILogger 呼び出しを `TraceTelemetry` に変換）
- `System.Diagnostics.Trace` / log4net / NLog などのレガシー ロギング API
- `EventSource` / `DiagnosticSource` / ETW イベント（対応モジュール経由）

### 1.2 SeverityLevel の定義

`Microsoft.ApplicationInsights.DataContracts.SeverityLevel` 列挙体[^5]：

| 値 | 名前 |
|---|---|
| 0 | Verbose |
| 1 | Information |
| 2 | Warning |
| 3 | Error |
| 4 | Critical |

> 注: `ILogger` 経由で送信される場合、`Microsoft.Extensions.Logging.ApplicationInsights` プロバイダーの**既定の最低ログレベルは `Warning`** です。`Information` 以下を送信するには `appsettings.json` で明示的にオーバーライドする必要があります[^3]。

### 1.3 AppTraces の主なフィールド

`Message`、`SeverityLevel`（int）、`SDKVersion`、`OperationName`、`AppRoleName`、`AppRoleInstance`、`ItemCount`、`_BilledSize`、`_IsBillable` 等のフィールドを持ちます[^4]。コスト分析では `_BilledSize` と `_IsBillable` が中心的な指標になります。

## 2. 削減アプローチの優先順位（Microsoft Learn ベストプラクティス）

Microsoft の公式コスト最適化ガイダンスでは、Application Insights のコスト削減として優先順位の高いものから以下が挙げられています[^6]。

1. ワークスペース ベースの Application Insights への移行（Basic Logs、コミットメント階層、テーブル単位の保持などのコスト機能を利用可能にする）
2. **サンプリング**（OpenTelemetry サンプリングが「主要なツール」と明記）
3. 不要な計装の無効化
4. 更新された SDK の使用
5. **ログ レベルによる不要な trace ログの抑制**（"Limit unwanted trace logging" — 本記事の中心トピック）

加えて、Application Insights 公式の OpenTelemetry サンプリング ドキュメントは、ログに関する一般ガイダンスとして「**アプリのログ設定で ERROR のみをエクスポートし、必要な場合のみ WARN を追加する**」ことを推奨しています[^1]。

## 3. 推奨削減手順（優先度高 → 低）

### 手順 0 — 現状把握用 KQL クエリ

`Usage` テーブルおよび `AppTraces` 自体に対してクエリを実行し、削減効果が高い箇所を特定します[^7]。

ワークスペース全体のテーブル別課金ボリュームの推移（直近 31 日）[^7]:

```kusto
Usage
| where TimeGenerated > ago(32d)
| where StartTime >= startofday(ago(31d)) and EndTime < startofday(now())
| where IsBillable == true
| summarize BillableDataGB = sum(Quantity) / 1000. by bin(StartTime, 1d), DataType
| render columnchart
```

Application Insights テーブル別の課金ボリューム（過去 7 日）[^7]:

```kusto
union AppAvailabilityResults, AppBrowserTimings, AppDependencies, AppExceptions,
      AppEvents, AppMetrics, AppPageViews, AppPerformanceCounters, AppRequests,
      AppSystemEvents, AppTraces
| where TimeGenerated >= startofday(ago(7d)) and TimeGenerated < startofday(now())
| summarize sum(_BilledSize) by _ResourceId, bin(TimeGenerated, 1d)
```

AppTraces を SeverityLevel 別に集計（`_BilledSize`, `_IsBillable` は全テーブル共通の標準列）[^7][^4]:

```kusto
AppTraces
| where TimeGenerated > ago(1d)
| where _IsBillable == true
| summarize Records = count(), BillableGB = sum(_BilledSize)/1024/1024/1024
        by SeverityLevel
| order by SeverityLevel asc
```

AppTraces 上位の `AppRoleName` / `OperationName` / `SDKVersion`:

```kusto
AppTraces
| where TimeGenerated > ago(1d)
| where _IsBillable == true
| summarize BillableGB = sum(_BilledSize)/1024/1024/1024, Records = count()
        by AppRoleName, OperationName, SDKVersion
| top 50 by BillableGB desc
```

サンプリングが有効かどうかの確認（`itemCount` から保持率を逆算）[^1]:

```kusto
union requests, dependencies, pageViews, browserTimings, exceptions, traces
| where timestamp > ago(1d)
| summarize RetainedPercentage = 100 / avg(itemCount) by bin(timestamp, 1h), itemType
```

`RetainedPercentage` が 100 未満であれば、そのテレメトリ タイプは既にサンプリングされています[^1]。

### 手順 1 — SDK 側でログ レベルを調整する（最優先・効果最大）

Microsoft の最終的な推奨事項は「**アプリ ログは ERROR のみをエクスポートし、WARN は実行可能（actionable）なものだけ追加する**」です[^1]。

#### 1.1 ASP.NET Core（`ILogger` + `appsettings.json`）

Application Insights プロバイダーは `Logging:LogLevel` セクションとは別に、**`Logging:ApplicationInsights:LogLevel` セクションでオーバーライド可能**です。明示的な指定がない場合、AI プロバイダーは Warning 以上のみをキャプチャします[^3]。

既定では Warning、AI には Error のみを送信する例:

```jsonc
{
  "Logging": {
    "LogLevel": {
      "Default": "Information"
    },
    "ApplicationInsights": {
      "LogLevel": {
        "Default": "Error"
      }
    }
  },
  "ApplicationInsights": {
    "ConnectionString": "<YOUR-CONNECTION-STRING>"
  }
}
```

> 注意: 以下の設定は **AI に Information を送信しません**。AI 側のフィルターは独立しており、明示的なオーバーライドが必要です[^3]。
>
> ```jsonc
> { "Logging": { "LogLevel": { "Default": "Information" } } }
> ```

カテゴリ単位のフィルタ（コード）。AI プロバイダーのみに対して粒度を絞れます[^3]:

```csharp
builder.Logging.AddApplicationInsights(...);
builder.Logging.AddFilter<ApplicationInsightsLoggerProvider>(
    "Microsoft.AspNetCore", LogLevel.Warning);
```

#### 1.2 Azure Functions / その他のホスト固有のログ

Microsoft はホスト側のログにも目を向けるよう明記しており、AKS の Control Plane / Data Plane ログ、Azure Functions のログレベル / スコープも見直し対象としています[^6]。

### 手順 2 — サンプリングを有効化する

公式の Application Insights サンプリング ガイドでは、サンプリングがテレメトリ削減・コスト削減・データ保持のバランスを取る「**推奨手段**」と位置付けられています[^1][^8]。

> 重要: **Azure Monitor OpenTelemetry Distro では既定でサンプリングは有効化されていません**。明示的に有効化と設定が必要です[^1]。

#### 2.1 OpenTelemetry Distro でのサンプリング設定（.NET / ASP.NET Core）[^9]

Fixed-rate（固定割合）:

```csharp
builder.Services.AddOpenTelemetry().UseAzureMonitor(o =>
{
    o.SamplingRatio = 0.1F;   // 約 10% を保持
});
```

Rate-limited（レート制限）:

```csharp
builder.Services.AddOpenTelemetry().UseAzureMonitor(o =>
{
    o.TracesPerSecond = 1.5;  // 1.5 traces/sec
});
```

サンプリング有効時は、トレースに紐づくログのうち、**サンプリングされなかったトレースに属するログは既定で破棄されます**（trace-based sampling for logs。オプトアウト可能）[^9][^1]。

#### 2.2 サンプリングの種類と適用範囲[^8]

| 種類 | 適用箇所 | 対応 SDK |
|---|---|---|
| Adaptive sampling | SDK 側（自動調整） | ASP.NET / ASP.NET Core / Azure Functions（既定で有効） |
| Fixed-rate sampling | SDK 側（固定割合） | ASP.NET / ASP.NET Core / Java / JavaScript / Python |
| Ingestion sampling | Application Insights サービス エンドポイント | 全 SDK（他のサンプリングが無効な場合のみ） |

**Ingestion sampling** は SDK の変更なしに即時に効くため最後の手段として有用ですが、公式ガイドは「**推奨しない**」と明記しています。理由は、保持するトレースを制御できず broken trace の可能性が高まるためです[^1]。Azure Portal の **Application Insights > Usage and estimated costs > Data Sampling** から設定します[^1]。

#### 2.3 サンプリングの影響（注意点）[^1][^8]

- **Metrics は決してサンプリングされません**（アラート用に信頼できる）[^1]
- ポータルでは `itemCount` を用いてメトリクス値を再正規化し、統計を補正します[^8]
- 関連するテレメトリ（リクエスト、依存関係、例外、トレース）は同じ Operation ID で一括して保持 / 破棄されるため、分散トレースの整合性が維持されます[^8]
- クエリでカウントを取る場合は `count()` ではなく `summarize sum(itemCount)` を使う必要があります[^8]
- Live Metrics との互換性のため、OpenTelemetry Distro では Application Insights カスタム サンプラーが使用されます[^1]

### 手順 3 — Telemetry Processor / Initializer で個別フィルタ（Classic SDK のみ）

サンプリングが「統計的に正しい削減」なのに対し、**Telemetry Processor (`ITelemetryProcessor`)** は「完全に制御してテレメトリを破棄 / 変更する」手段です[^10]。

- **Telemetry Processor**: テレメトリを完全に置換または破棄できる（フィルタリング用途）[^10]
- **Telemetry Initializer (`ITelemetryInitializer`)**: テレメトリのプロパティを追加 / 変更（必ず実行される）[^10]
- 用途の使い分け: **エンリッチには Initializer、フィルタには Processor**[^10]

> 警告: Processor によるフィルタリングは「ポータルで表示される統計を歪め、関連する項目間のナビゲーションを困難にする可能性がある」ため、**まずサンプリングを検討するよう公式に注意喚起されています**[^10]。

### 手順 4 — Workspace transformation DCR（取り込み時フィルタ）

Application Insights のテレメトリは通常の DCR を使用しないデータ収集経路であるため、Microsoft は「**workspace transformation DCR**」という特別な DCR を用意しています。これは Log Analytics ワークスペースに直接適用される DCR で、`AppTraces` のようなテーブルに到達する前に KQL でフィルタ / 変形できます[^11]。

- **`AppTraces` は ingestion-time DCR transformation 対応テーブル**として明示されています[^4][^12]
- ワークスペース DCR はワークスペースごとに **1 つ**で、複数テーブルの transformation を含められます[^11]
- 既定の Azure ポータル ウィザード（`Log Analytics workspace > Tables > Create transformation`）から構成可能[^13]

Verbose / Information を取り込み前に除外する例:

```kusto
source
| where SeverityLevel >= 2     // 0=Verbose, 1=Information を除外
```

#### 4.1 Transformation のコスト（重要）[^14]

| テーブル プラン | Transformation のコスト |
|---|---|
| **Analytics / Basic Logs** | Transformation 自体は通常無料。ただし**取り込みデータ量を 50% を超えて削減した場合、超過分はデータ処理料金として課金**。計算式: `[削減した GB] - ([受信 GB] / 2)` |
| **Auxiliary Logs** | **受信データ全量にデータ処理料金が課金され、加えて取り込み後の量に対し取り込み料金が課金** |
| Microsoft Sentinel が有効な場合 | Analytics テーブルへの transformation は**金額がいくら削減されても無料**[^14] |

計算例[^14]: 受信 20 GB に対し 12 GB を transformation で破棄 → 取り込み 8 GB / データ処理課金 2 GB / 取り込み課金 8 GB。

> したがって、**SDK 側のログ レベル変更とサンプリングで先に削減してから transformation を補助的に使う**のが、コスト構造上も合理的です[^6][^14]。

### 手順 5 — Basic Logs プランへの切り替え

`AppTraces` は **Basic Logs プランをサポートする Application Insights テーブル** として公式リストに掲載されています[^15][^4]（`Basic log: Yes`）。デバッグ用途で「取り込みは多いがクエリ頻度は低い」場合に有効です。

Microsoft のコスト最適化ガイドは「デバッグ・トラブルシューティング・監査用テーブルは Basic Logs に構成する」ことを推奨しています[^6]。

#### 5.1 Basic Logs の制約[^16]

- KQL の制約: `join`、`find`、`search`、`externaldata` は**使用不可**
- `lookup` / `union` は Analytics テーブル最大 5 個まで
- ユーザー定義関数、クロスサービス / クロスリソース クエリは使用不可
- **時間範囲は過去 30 日まで**（それ以前のデータは search job が必要）
- 同時クエリ数: ユーザーあたり最大 2
- アラート / Azure Monitor Dashboards 非対応（Workbooks / Grafana は対応）
- データのパージ不可
- **クエリ実行時にスキャンしたデータ量に応じた課金**（取り込み量とは別）[^16]

#### 5.2 切り替え手順[^17]

- ポータル: `Log Analytics workspace > Tables > [対象テーブル] > Manage table > Table plan = Basic`
- CLI:

  ```bash
  az monitor log-analytics workspace table update \
    --resource-group <RG> --workspace-name <WS> \
    --name AppTraces --plan Basic
  ```

- プランの切り替えは**週 1 回まで**。Analytics → Basic に切り替えると 30 日以上前のデータは長期保持データとして扱われます[^17]。

### 手順 6 — Daily Cap を「セーフティ ネット」として設定

Microsoft は Daily Cap を「**予期しないスパイクへの保護策**」と位置付け、コスト削減の主要手段としては推奨していません[^18]。

- 上限に達するとビルブルなデータ収集が **24 時間停止**し、監視機能が機能しなくなります[^18]
- ワークスペース ベースの Application Insights では、Application Insights 側と Log Analytics 側の両方を設定でき、**実効値は両者のうち低い方**になります[^18]
- 上限到達時刻は構成不可（ワークスペースごとに固定）[^18]
- 上限 80–90% で別途アラート ルールを設定して通知することが推奨されています[^6][^18]

### 手順 7 — Commitment Tier の検討（取り込み量を削減した後）

サンプリングや SDK 変更で削減した後、残った取り込み量が **100 GB/day 以上で安定している場合**は Commitment Tier に移行することで Pay-as-you-go と比較して最大 30% のコスト削減が可能です[^19]。

- 開始単位: 100 GB/day から[^19]
- コミット期間: 31 日（その期間中はティアを下げられない）[^19]
- 超過分は同じティア単価で課金（例: 200 GB ティアで 300 GB 取り込み → 1.5 単位として課金）[^19]
- ティアが間違って設定された場合は構成後 6 時間以内ならリセット可、それ以外は Microsoft サポート連絡が必要[^19]

## 4. 推奨実行順序（まとめ表）

| # | アクション | 効果 | リスク |
|---|---|---|---|
| 1 | 現状把握 KQL（手順 0） | — | なし |
| 2 | `appsettings.json` で `Logging:ApplicationInsights:LogLevel` を `Error` または `Warning` に[^3] | **大**（Verbose / Information を SDK で破棄） | 開発者デバッグ情報の喪失 |
| 3 | OpenTelemetry サンプリング（fixed-rate or rate-limited）[^9] | 大 | メトリクスは影響なし。ItemCount で統計補正されるためマイナー[^1][^8] |
| 4 | Workspace transformation DCR で `SeverityLevel < 2` を除外[^11] | 中 | 50% 超の削減で transformation 料金（手順 4.1 参照）[^14] |
| 5 | `AppTraces` を Basic Logs プランに切り替え[^15][^17] | 中（残り取り込み分の単価が下がる） | KQL の機能制限、30 日保持、クエリ単位課金[^16] |
| 6 | Daily Cap をスパイク保護として設定[^18] | 限定的（予防） | 上限到達時は監視停止 |
| 7 | Commitment Tier に移行[^19] | 中（単価最大 30% 引き） | 31 日コミット |

## 5. 注意点（横断的な制約まとめ）

- **サンプリング × Ingestion sampling**: SDK 側で adaptive / fixed-rate を有効にすると、そのテレメトリ タイプに対する Ingestion sampling は自動的に無効化されます[^8]。
- **メトリクスとパフォーマンス カウンター**: サンプリングや Telemetry Processor 適用後も保持されます[^8][^1]。
- **DCR transformation × Microsoft Sentinel**: Sentinel が有効なワークスペースの Analytics テーブルでは、transformation のデータ処理料金は発生しません[^14]。
- **Daily Cap の到達**: 上限超過分も「いくらかは課金される可能性がある」と明記されています（厳密に上限で止まるわけではない）[^18]。
- **`AppTraces` の特性**: Basic Logs 対応、ingestion-time DCR 対応の双方を満たしているため、削減オプションの選択肢が広いテーブルです[^4]。

## 6. AppRoleName 別に「犯人」を特定する KQL クエリ集

現状把握で `SeverityLevel` 分布を見ると、典型的なデバッグ目的の環境では **Information（`SeverityLevel == 1`）が 99% 前後**を占めることが多くあります。この場合のゴールは「**どの AppRoleName が Information を出しているか**を特定して、その App のみ SDK ログレベルを上げる」ことです。以下のクエリを順に実行することで犯人を絞り込めます。`AppRoleName` / `OperationName` / `SDKVersion` / `_BilledSize` / `_IsBillable` は `AppTraces` の公式スキーマに存在するフィールドです[^4]。

### 6.1 AppRoleName ごとの課金量（パレート確認）

```kusto
AppTraces
| where TimeGenerated > ago(7d)
| where _IsBillable == true
| summarize BillableGB = sum(_BilledSize) / 1024 / 1024 / 1024,
            Records   = count()
        by AppRoleName
| order by BillableGB desc
```

通常は上位 3 〜 5 個の AppRoleName が全体の大半を占めます。

### 6.2 AppRoleName × SeverityLevel のクロス集計

```kusto
AppTraces
| where TimeGenerated > ago(7d)
| where _IsBillable == true
| summarize BillableGB = sum(_BilledSize) / 1024 / 1024 / 1024
        by AppRoleName, SeverityLevel
| extend Sev = case(
        SeverityLevel == 0, "0:Verbose",
        SeverityLevel == 1, "1:Information",
        SeverityLevel == 2, "2:Warning",
        SeverityLevel == 3, "3:Error",
        SeverityLevel == 4, "4:Critical", "?")
| evaluate pivot(Sev, sum(BillableGB))
| order by ['1:Information'] desc
```

どの AppRoleName が Information を大量に出しているかが一目で分かります。

### 6.3 AppRoleName × OperationName（何の処理が出しているか）

```kusto
AppTraces
| where TimeGenerated > ago(1d)
| where _IsBillable == true
| where SeverityLevel == 1
| summarize BillableGB = sum(_BilledSize) / 1024 / 1024 / 1024,
            Records   = count()
        by AppRoleName, OperationName
| top 30 by BillableGB desc
```

`GET /health` や `GET /metrics` のような頻発エンドポイントの Information ログを発見できます。

### 6.4 AppRoleName × Message パターン（同一メッセージの量産検出）

```kusto
AppTraces
| where TimeGenerated > ago(1d)
| where _IsBillable == true
| where SeverityLevel == 1
| extend MsgHead = substring(Message, 0, 80)
| summarize BillableMB = sum(_BilledSize) / 1024 / 1024,
            Records   = count()
        by AppRoleName, MsgHead
| top 50 by BillableMB desc
```

EF Core の SQL ロギング、HTTP client のリクエストロギングなど、同一文言の量産パターンを炙り出せます。

### 6.5 AppRoleName × 時系列（スパイクの確認）

```kusto
AppTraces
| where TimeGenerated > ago(7d)
| where _IsBillable == true
| summarize BillableGB = sum(_BilledSize) / 1024 / 1024 / 1024
        by bin(TimeGenerated, 1h), AppRoleName
| render timechart
```

デプロイ後にスパイクしている AppRoleName を特定できます。

### 6.6 AppRoleName × SDKVersion（Classic SDK / OTel の判別）

```kusto
AppTraces
| where TimeGenerated > ago(1d)
| where _IsBillable == true
| summarize BillableGB = sum(_BilledSize) / 1024 / 1024 / 1024
        by AppRoleName, SDKVersion
| order by BillableGB desc
```

`SDKVersion` の値で対応方法が変わります。`ai.` プレフィックス = Classic SDK、`azmon-` / `otel` = OpenTelemetry Distro。これにより手順 1（`appsettings.json`）か手順 2（OTel `SamplingRatio`）のどちらに進むかが決まります[^4]。

### 6.7 Information 偏重環境の次アクション例

`SeverityLevel == 1` が支配的な環境では、次の順序が最短です。

1. 6.1 / 6.2 で上位 3 件の AppRoleName を特定
2. 対象アプリの `appsettings.json` に以下を追加（既定で Warning 以上のみ送信）[^3]:

   ```jsonc
   "Logging": {
     "ApplicationInsights": {
       "LogLevel": {
         "Default": "Warning"
       }
     }
   }
   ```

   Information 比率が 99% の場合、理論上はこの設定だけで `AppTraces` 全体の取り込み量を約 99% 削減できます。
3. 残った Information のうち「特定メッセージだけ消したい」ケースがあれば、6.4 で特定したメッセージを Workspace transformation DCR で除外（手順 4 参照）[^11][^14]

## 7. AppRoleName が空になる場合の対処（Classic .NET Core SDK ケース）

実環境で `AppTraces` を集計すると、`AppRoleName` がほぼすべて空、というケースがあります。SDK が `dotnetc:2.20.0-103` のような Classic Application Insights .NET Core SDK[^1] で AKS / コンテナ / Worker Service / コンソール アプリのように **App Service / Cloud Service の自動検出が効かない環境**で発生します[^4]。

### 7.1 AppRoleName が空になる理由

Classic SDK は `cloud.role_name` を以下のいずれかから自動設定します。該当する経路がなければ空になります[^4]。

| 環境 | 自動設定元 |
|---|---|
| App Service | `WEBSITE_SITE_NAME` 環境変数 |
| Azure Cloud Service | Role 名 |
| ASP.NET Core ホスト（特定条件） | `AspNetCoreEnvironmentTelemetryInitializer` |
| AKS / コンテナ / Worker Service / コンソール | **自動設定なし → 空** |

### 7.2 AppRoleName が空でも犯人を絞り込む代替集計

`_ResourceId` 別（複数 AI リソースを 1 ワークスペースに集約している場合）:

```kusto
AppTraces
| where TimeGenerated > ago(1d)
| where _IsBillable == true
| summarize BillableGB = sum(_BilledSize)/1024/1024/1024,
            Records   = count()
        by _ResourceId
| order by BillableGB desc
```

`AppRoleInstance` 別（ホスト名 / コンテナ / Pod 名）。`AppRoleName` が空でも値が入っていることが多い[^4]:

```kusto
AppTraces
| where TimeGenerated > ago(1d)
| where _IsBillable == true
| summarize BillableGB = sum(_BilledSize)/1024/1024/1024,
            Records   = count()
        by AppRoleInstance
| top 30 by BillableGB desc
```

`OperationName` 別（HTTP メソッド + ルート）。エンドポイント名からアプリを推測できる:

```kusto
AppTraces
| where TimeGenerated > ago(1d)
| where _IsBillable == true
| where SeverityLevel == 1
| summarize BillableGB = sum(_BilledSize)/1024/1024/1024,
            Records   = count()
        by OperationName
| top 30 by BillableGB desc
```

`Properties` 内のカスタム ディメンションを覗いて識別子を探す:

```kusto
AppTraces
| where TimeGenerated > ago(10m)
| where _IsBillable == true
| where SeverityLevel == 1
| project TimeGenerated, AppRoleInstance, OperationName, Message, Properties
| take 20
```

`Properties` に `CategoryName`（ILogger のカテゴリ）や `AspNetCoreEnvironment` などが入っていることがあります[^4]。

### 7.3 AppRoleName を埋める（並行対応）

Classic SDK では `ITelemetryInitializer` を実装して `Cloud.RoleName` を明示設定するのが標準手順です[^10]:

```csharp
public class CloudRoleNameInitializer : ITelemetryInitializer
{
    private readonly string _roleName;
    public CloudRoleNameInitializer(string roleName) => _roleName = roleName;

    public void Initialize(ITelemetry telemetry)
    {
        if (string.IsNullOrEmpty(telemetry.Context.Cloud.RoleName))
        {
            telemetry.Context.Cloud.RoleName = _roleName;
        }
    }
}

// Program.cs
builder.Services.AddSingleton<ITelemetryInitializer>(
    new CloudRoleNameInitializer("orders-api"));
```

AKS では環境変数 / Downward API から Pod 名 / Deployment 名を取得し `RoleName` に設定します。

### 7.4 Classic SDK 2.20.0 環境での削減アクション（このケース固有）

SdkVersion `dotnetc:` は Classic SDK（OpenTelemetry Distro ではない）であるため、削減ルートは以下が確定的に効きます。

| 優先度 | アクション | 効き方 |
|---|---|---|
| 1 | `appsettings.json` に `Logging:ApplicationInsights:LogLevel:Default = "Warning"` を追加[^3] | Information を SDK 側で破棄。Information が 99% を占める環境では `AppTraces` 取り込み量を約 99% 削減見込み |
| 2 | Classic SDK の adaptive sampling 設定を確認・強化（`MaxTelemetryItemsPerSecond`）[^8] | 既定でも有効だが trace への効きは環境依存 |
| 3 | `ITelemetryProcessor` で頻発メッセージを明示破棄[^10] | 6.3 / 6.4 で特定したパターンに対するピンポイント対応 |
| 4 | Workspace transformation DCR で `SeverityLevel < 2` を除外[^11][^14] | SDK 配布が困難な共有環境の救済策 |

> Classic SDK 2.20.x はメンテナンス フェーズに入っているバージョン系列であり、長期的には Microsoft は **OpenTelemetry Distro への移行**を推奨ルートとしています[^1][^9].

## 8. 実例: HttpClient ロガー / MSAL / Azure SDK が支配的なケース

`AppTraces` の `Message` 先頭を集計したとき、次のようなパターンが大半を占めることがあります。

```
Start processing HTTP request GET https://login.microsoftonline.com/...
Sending HTTP request GET https://login.microsoftonline.com/...
Start processing HTTP request POST https://<downstream-api>/...
Sending HTTP request POST https://<downstream-api>/...
```

これは **`IHttpClientFactory` の標準ログ（`Microsoft.Extensions.Http`）**が出力しているメッセージです[^20]。

### 8.1 出力元とロガー カテゴリ

| メッセージ | 出力元クラス | ロガーカテゴリ | 既定レベル |
|---|---|---|---|
| `Start processing HTTP request {Method} {Uri}` | `LoggingScopeHttpMessageHandler` | `System.Net.Http.HttpClient.{name}.LogicalHandler` | **Information** |
| `End processing HTTP request after {Elapsed}ms - {StatusCode}` | `LoggingScopeHttpMessageHandler` | 同上 | Information |
| `Sending HTTP request {Method} {Uri}` | `LoggingHttpMessageHandler` | `System.Net.Http.HttpClient.{name}.ClientHandler` | **Information** |
| `Received HTTP response headers after {Elapsed}ms - {StatusCode}` | `LoggingHttpMessageHandler` | 同上 | Information |

**HTTP リクエスト 1 回につき Information ログが最低 4 件**出力されます[^20]。Web アプリ / API バックエンドで `HttpClient` を多用すると Information の大半を占めるのは典型的です。

リクエスト先のドメインからおおよその発信元が推測できます。

- `login.microsoftonline.com` → MSAL / Azure.Identity / Microsoft.Identity.Web のトークン取得
- 業務 API ホスト名 → アプリから下流サービスへの呼び出し

### 8.2 直接効くフィルタ設定（`appsettings.json`）

`Logging:ApplicationInsights:LogLevel` セクションでカテゴリ名プレフィックスでフィルタできます[^3]。`Logging:LogLevel` とは独立に評価される点に注意してください[^3]。

```jsonc
{
  "Logging": {
    "LogLevel": {
      "Default": "Information"
    },
    "ApplicationInsights": {
      "LogLevel": {
        "Default": "Information",
        "System.Net.Http.HttpClient": "Warning",
        "Microsoft.Identity": "Warning",
        "Azure.Core": "Warning",
        "Azure.Identity": "Warning"
      }
    }
  }
}
```

| カテゴリ | 抑制対象 |
|---|---|
| `System.Net.Http.HttpClient` | `IHttpClientFactory` の上記 4 種のログをまとめて Warning に[^20][^3] |
| `Microsoft.Identity` | Microsoft.Identity.Web / MSAL のログ |
| `Azure.Identity` | Azure.Identity の認証フローログ |
| `Azure.Core` | Azure SDK の HTTP パイプライン ログ |

特定の HttpClient 名だけ消したい場合は、`AddHttpClient("downstream-api")` の名前単位で粒度を下げられます[^20][^3]。

```jsonc
"ApplicationInsights": {
  "LogLevel": {
    "Default": "Information",
    "System.Net.Http.HttpClient.downstream-api.LogicalHandler": "Warning",
    "System.Net.Http.HttpClient.downstream-api.ClientHandler": "Warning"
  }
}
```

### 8.3 自前の `TrackTrace` 呼び出し（例: `CustomApimTrace`）

ロガー カテゴリに該当しない独自文字列（例: `CustomApimTrace`）が大量に出ている場合は、**`TelemetryClient.TrackTrace(...)` を直接呼んでいる自前コード**が発信元です。次のクエリで `Properties` / `OperationName` から発信元を特定します。

```kusto
AppTraces
| where TimeGenerated > ago(1h)
| where Message startswith "CustomApimTrace" or Message contains "CustomApimTrace"
| project TimeGenerated, AppRoleInstance, OperationName, Message, Properties, SeverityLevel
| take 20
```

特定後の対応は次のいずれかです[^10]。

- コード側で送信レベルを上げる、または送信を止める
- 残す必要がある場合は `ITelemetryProcessor` で `SeverityLevel` や `Message` ベースに破棄する

### 8.4 期待される削減効果

`System.Net.Http.HttpClient` カテゴリのみを Warning に上げただけで、HttpClient を多用するアプリでは Information の 70 〜 95% が消えるのが一般的です。Information が全体 99% を占める環境では、`AppTraces` 全体で 1.5 〜 1.9 TB / 月規模の削減が現実的に見込めます。

### 8.5 ロールアウト手順（推奨）

1. `appsettings.json` を §8.2 のとおり更新
2. ステージング 1 台で 30 分稼働させ、§8.3 の確認クエリで残ったメッセージを再点検
3. `AppRoleInstance` 別の `_BilledSize` 推移を 1 時間以内に確認（§6.5 のクエリ）
4. 問題なければ全環境ロールアウト
5. `CustomApimTrace` 等の自前ログはコード調査の上、別途対処

### 8.6 `System.Net.Http.HttpClient` を Warning 化したときの影響範囲

このフィルタの効き方を正確に把握しておくことは運用上重要です。

#### 8.6.1 フィルタは全 HttpClient インスタンスに波及

ILogger のフィルタは**最長プレフィックス マッチ**で評価されます[^21]。`"System.Net.Http.HttpClient": "Warning"` を設定すると、認証系（MSAL / Azure.Identity の HTTP 呼び出し）だけでなく、以下を含む**アプリ内のすべての `HttpClient` / `IHttpClientFactory` 利用箇所**の Information ログが消えます。

- 業務 API への下流呼び出し
- 外部 SaaS API（任意の REST クライアント）
- gRPC クライアント（内部で HttpClient を使う）
- SignalR / WebSocket（HTTP ハンドシェイク部分）
- ヘルスチェックの外部 HTTP プローブ
- Azure SDK（Storage / Service Bus / Cosmos など、内部で HttpClient を使うもの）

#### 8.6.2 失われる情報

`IHttpClientFactory` 標準ロガーが Information で出すメッセージはすべて消えます[^20]。

| EventId | EventName | Message |
|---|---|---|
| 100 | `RequestStart` | `Sending HTTP request {HttpMethod} {Uri}` |
| 101 | `RequestEnd` | `Received HTTP response headers after {ElapsedMilliseconds}ms - {StatusCode}` |
| 100 | `RequestPipelineStart` | `Start processing HTTP request {HttpMethod} {Uri}` |
| 101 | `RequestPipelineEnd` | `End processing HTTP request - {StatusCode}` |

> 重要: `IHttpClientFactory` の標準ロガーは **Warning / Error レベルのイベントを発行しません**。HTTP リクエストが失敗（4xx / 5xx）してもこれらのメッセージは Information で出力されるため、「Warning に上げれば失敗時だけ残る」ということには**なりません**（HttpClient ファクトリの直接ログは全部消えます）[^20]。

#### 8.6.3 失われない情報（観測性はほぼ維持される）

HttpClient ロガーの Information を消しても、以下は別経路で記録され続けます。

| 機能 | 格納先テーブル | 影響 |
|---|---|---|
| HTTP 依存関係の追跡（URL / 所要時間 / ステータス / 成功失敗） | `AppDependencies` | **影響なし**[^22] |
| HTTP 例外（ネットワークエラー / タイムアウト / `HttpRequestException`） | `AppExceptions` | 影響なし |
| 失敗した HTTP 呼び出しの可視化（`Success == false`） | `AppDependencies` | 影響なし。Application Map / End-to-end トランザクション ビューでそのまま確認可能[^22] |
| Polly の retry / circuit breaker ログ | `Polly.*` カテゴリ（独立） | 影響なし |
| gRPC のアプリレベルログ | `Grpc.Net.Client.*` カテゴリ | 影響なし |
| 自分の `ILogger.LogInformation()` 呼び出し | `AppTraces`（自カテゴリ） | 影響なし（呼び出し側のカテゴリ次第） |

Application Insights は `DependencyTrackingTelemetryModule` で HTTP 依存関係を自動収集しており、これは `ILogger` の設定とは独立しています[^22]。Application Map・依存マップ・End-to-end トランザクション図は失敗呼び出しも含めて引き続き機能します。

#### 8.6.4 注意すべきトレードオフ

| 項目 | 影響 |
|---|---|
| 「あの API を呼んだか」を `AppTraces` の Message 全文検索で追う運用 | 不可になる → `AppDependencies` ベースの調査に切り替え必要 |
| `AppTraces` の Message に対する Log Search Alert | 該当メッセージで作成済みのアラートは沈黙する。事前に棚卸し |
| ヘッダー / ボディの詳細ログ | 既に Trace レベルなので元から `AppTraces` に出ていない。影響なし[^20] |
| HTTP のレイテンシ追跡 | `AppDependencies.DurationMs` で代替可能 |
| 障害解析のフロー変更 | 「ログを grep」から「AppDependencies を KQL」へ移行が必要 |

#### 8.6.5 障害解析時の代替クエリ（AppDependencies 利用）

失敗した HTTP 呼び出しを見る:

```kusto
AppDependencies
| where TimeGenerated > ago(1h)
| where Type == "Http"
| where Success == false
| project TimeGenerated, AppRoleInstance, Name, Target, ResultCode, DurationMs, Properties
| order by TimeGenerated desc
```

特定 URL への呼び出し量・成功率・レイテンシ:

```kusto
AppDependencies
| where TimeGenerated > ago(1d)
| where Type == "Http"
| where Target == "mcapi.example.com"
| summarize Calls = count(),
            Failures = countif(Success == false),
            P95 = percentile(DurationMs, 95),
            AvgMs = avg(DurationMs)
        by bin(TimeGenerated, 5m)
| render timechart
```

タイムアウト / 接続エラー:

```kusto
AppExceptions
| where TimeGenerated > ago(1d)
| where Type in ("System.Net.Http.HttpRequestException",
                 "System.Threading.Tasks.TaskCanceledException",
                 "System.TimeoutException")
| summarize Count = count() by Type, bin(TimeGenerated, 1h)
```

#### 8.6.6 段階的に効かせる場合

「全 HttpClient 一括」が不安なら、認証系から順に絞ることもできます。

```jsonc
"ApplicationInsights": {
  "LogLevel": {
    "Default": "Information",
    "System.Net.Http.HttpClient.IdentityServerClient": "Warning",
    "System.Net.Http.HttpClient.OAuthClient": "Warning",
    "Microsoft.Identity": "Warning",
    "Azure.Identity": "Warning"
  }
}
```

その後、`AppTraces` の Message 集計（§6.4）で残りボリュームを見ながら順次広げていくのが安全です。

#### 8.6.7 注意: `AppDependencies` に HTTP 依存関係が無い場合

`AppDependencies` テーブルを `Type` 別に集計したときに **`Http` 行が 1 件も存在しない**ケースがあります。この場合、HttpClient ロガーの Information ログが **アプリ内で外部 HTTP 呼び出しを観測できる唯一の手段**になっており、Warning 化は可視性を全面的に失わせるため、そのままでは実行できません。

確認用クエリ:

```kusto
AppDependencies
| where TimeGenerated > ago(7d)
| where _IsBillable == true
| summarize Calls       = count(),
            BillableGB  = sum(_BilledSize)/1024/1024/1024,
            SampleName  = take_any(Name),
            SampleTarget= take_any(Target)
        by Type
| order by BillableGB desc
```

`Type` 一覧に `Http` が現れない場合の代表的原因は次のとおりです[^22]。

| 原因 | 確認・対処 |
|---|---|
| `EnableDependencyTrackingTelemetryModule = false` を `ApplicationInsightsServiceOptions` で明示設定 | コード確認の上、削除または `true` に変更 |
| `Microsoft.ApplicationInsights.DependencyCollector` パッケージ未参照（Worker / Console で単体 SDK 利用） | `Microsoft.ApplicationInsights.AspNetCore` または `Microsoft.ApplicationInsights.WorkerService` に切り替える |
| カスタム `ITelemetryProcessor` で `DependencyTelemetry` を破棄 | 該当処理を見直し、HTTP は通すように修正 |
| AKS / コンテナで自動計装エージェントと SDK の二重計装による競合 | 自動計装エージェントを無効化、または SDK 側を撤去 |

##### 修復が短期で難しい場合の暫定削減策

(1) **Workspace Transformation DCR でノイズのみ破棄**（認証系の高頻度メッセージだけ落とす）[^11][^14]:

```kusto
source
| where not(
    Message startswith "Sending HTTP request" and Message contains "login.microsoftonline.com"
    or Message startswith "Start processing HTTP request" and Message contains "login.microsoftonline.com"
    or Message startswith "End processing HTTP request" and Message contains "login.microsoftonline.com"
    or Message startswith "Received HTTP response headers" and Message contains "login.microsoftonline.com"
  )
```

業務 API への HttpClient ログは可視性を維持しつつ、認証ループだけを落とせます。Transformation の課金は 50% を超えた分のみ発生する仕様[^14]。

(2) **Classic SDK の adaptive sampling を強化**[^8]:

```csharp
services.Configure<TelemetryConfiguration>(config =>
{
    var builder = config.DefaultTelemetrySink.TelemetryProcessorChainBuilder;
    builder.UseAdaptiveSampling(
        maxTelemetryItemsPerSecond: 1,
        excludedTypes: "Event;Exception",
        includedTypes: "Trace;Dependency;Request");
    builder.Build();
});
```

統計的可視性は ItemCount 補正で維持されます[^8]。

##### 推奨対応順序

```
1. §8.6.7 冒頭のクエリで Type 別内訳を確定
2. 上記 (1) Transformation DCR で認証系ノイズを即時削減
3. 並行して HTTP 追跡を修復（EnableDependencyTrackingTelemetryModule の有効化など）
4. 修復確認後、HttpClient 全体を Warning へ移行
```

## 9. 実例: 構造化ログを JSON 文字列化して `Message` に詰め込んでいるケース

セクション 8 の HttpClient ロガーは「**小さい Information レコードが大量に出る**」パターンでしたが、もう一つの典型は「**1 レコードが大きい Information が実行のたびに出る**」ケースです。`AppTraces` の `Message` をパターン集計したとき、次のように **`Message` が JSON 丸ごと**になっていることがあります（以下はマスク値）。

```
{"Date":"2026-06-08 11:34:32.300","LogLevel":"INFO","ExecutionId":"I9990007","ProcessingSystem":"SYS-A", ...}
{"Date":"2026-06-08 11:34:32.298","LogLevel":"INFO","ExecutionId":"D9990001","ProcessingSystem":"SYS-A", ...}
```

### 9.1 読み取れること

| 観点 | 内容 |
|---|---|
| `Message` が JSON 丸ごと | アプリ（または共通ロギング基盤）が、構造化ログを **JSON 文字列化して 1 メッセージとして出力**している |
| `LogLevel":"INFO"` | メッセージ本体が INFO。実行のたびに必ず出るため、**トラフィックに比例して青天井**に伸びる |
| `ExecutionId` の接頭辞 `I` / `D` / `E` | 発信元が **3 系統**に分かれている（システム別プレフィックス） |
| 1 件のサイズ | 約 1,743 B。`AppTraces` の課金サイズは **各列の文字列表現から算出**されるため、巨大な JSON 文字列がそのまま課金量になる[^23] |
| 合計 | 1,743 B × 約 6,802 万件 ≈ **110 GB**（I / D / E の 3 系統合計） |

> HttpClient ログとの違い: HttpClient ログは「件数が多い」ことが主因でしたが、このケースは「**1 件あたりが大きい**」ことも重なっています。そのため対処は「件数を減らす（レベル / 頻度）」だけでなく「**1 件のサイズを縮める**」という軸も効きます。

### 9.2 犯人を確定させる KQL

#### (a) メッセージを正規化してパターン別に集計（どのテンプレートが支配的か）

数値や ID を伏字化（`{n}` / `{id}`）して「メッセージ テンプレート単位」で課金量を集計すると、文言が微妙に違うだけの同型ログをまとめて炙り出せます[^4]。特定のリソースに絞り込まず、`_ResourceId` を `by` 句に含めることで、**どのリソースがどれだけ課金量を生んでいるか**をリソース横断で比較できます。

```kusto
AppTraces
| where TimeGenerated > ago(7d)
| where SeverityLevel == 1
| extend Norm = replace_regex(Message, @'\d+', '{n}')
| extend Norm = replace_regex(Norm, @'[0-9a-fA-F-]{8,}', '{id}')
| summarize
    SizeGB = round(sum(_BilledSize)/1024.0/1024/1024, 2),
    Count = count(),
    SampleMessage = take_any(Message)   // 代表原文を 1 件
  by _ResourceId, Pattern = substring(Norm, 0, 80)
| sort by SizeGB desc
| take 20
```

`_ResourceId` × `Pattern` の組み合わせで `SizeGB` 上位を見ることで、「どのリソースのどのテンプレートが犯人か」を一度に把握できます。リソース単位の合計だけが欲しい場合は `by _ResourceId` のみにします。`SampleMessage` で代表原文を 1 件確認できます。

#### (b) JSON 文字列化された Message を構造化して中身を確認

`Message` が JSON で始まるレコードを `parse_json` で展開し、`LogLevel` / `Category` / `EventName` / `Message` などのキーを取り出して発信元を特定します。

```kusto
AppTraces
| where TimeGenerated > ago(1d)
| where _ResourceId =~ "<対象リソースID>"
| where SeverityLevel == 1
| where Message startswith "{"
| extend J = parse_json(Message)
| project
    LogLevel  = tostring(J.LogLevel),
    Category  = tostring(J.Category),
    EventName = tostring(J.EventName),
    Msg       = tostring(J.Message)
| take 20
```

#### (c) `ExecutionId` 接頭辞（I / D / E）別の内訳と 1 件サイズ

「大きいログか／多いログか」を判別するため、系統別に件数・課金量・平均サイズを見ます[^4][^23]。

```kusto
AppTraces
| where TimeGenerated > ago(1d)
| where _ResourceId =~ "<対象リソースID>"
| where SeverityLevel == 1
| where Message startswith "{"
| extend ExecPrefix = extract("\"ExecutionId\":\"([A-Za-z])", 1, Message)
| summarize Records    = count(),
            BillableGB = round(sum(_BilledSize)/1024.0/1024/1024, 2),
            AvgBytes   = avg(_BilledSize)
        by ExecPrefix
| order by BillableGB desc
```

### 9.3 対処 A — アプリ側（根本対応）

このアンチパターンの本質は「**構造化ログを自前で JSON 文字列化して `Message` に詰めている**」ことです。本来の `ILogger` はメッセージ テンプレートとパラメータを分けて渡すと、パラメータ部分を `customDimensions`（`AppTraces.Properties`）として構造化保持します[^24]。

推奨は次のいずれかです。

1. **出力レベルの見直し**: この INFO がデバッグ目的なら `Debug` に格下げし、本番は `Warning` 以上のみ送信（§8.2 の `appsettings.json` と同じ考え方）[^3]
2. **出力頻度の見直し**: 「実行のたびに必ず 1 件」をやめ、サマリ / 集計ログに変更する
3. **JSON 文字列化をやめる**: `_logger.LogInformation("{@Context}", ctx)` のように構造化ログとして渡し、`Message` 本体を短くする[^24]
4. **サンプリング**: そのまま残す必要があるなら OpenTelemetry / Classic SDK のサンプリングで保持率を下げる[^1][^8]

### 9.4 対処 B — DCR transformation（コード変更が難しい場合）

アプリ改修が難しい場合は、Workspace transformation DCR で取り込み時に処理します。`AppTraces` は transformation 対応テーブルです[^11][^12]。このケースでは **2 つのアプローチ**があります。

#### (1) 不要な系統・レベルの行ごと除外（件数を減らす）

INFO の JSON ログのうち、特定系統（例: `D` 系統）だけを取り込み前に落とす例[^11][^14]:

```kusto
source
| where not(Message has "\"LogLevel\":\"INFO\"" and Message matches regex "\"ExecutionId\":\"D")
```

#### (2) `Message` を切り詰めて 1 件のサイズを縮める（件数は保ちつつ課金量を下げる）

課金サイズは列の文字列表現から算出されるため[^23]、巨大な `Message` を transformation で短縮すればその分だけ課金が下がります。ログの存在（件数）は残しつつ、本文を先頭数百バイトに切り詰める例:

```kusto
source
| extend Message = substring(Message, 0, 300)
```

より良いのは、JSON から必要なキーだけを抽出して別列に移し、`Message` 本体を落とすアプローチです（transformation は列の抽出・再構成にも使えます[^11]）。

```kusto
source
| extend ExecutionId = extract("\"ExecutionId\":\"([^\"]+)", 1, Message)
| extend ProcessingSystem = extract("\"ProcessingSystem\":\"([^\"]+)", 1, Message)
| extend Message = ""
```

> コスト上の注意（§4.1 再掲）: transformation で取り込み量を 50% 超削減した場合、超過分にデータ処理料金がかかります（計算式 `[削減 GB] − [受信 GB] / 2`）。Message 切り詰めは 1 件あたり 1,743 B → 数百 B と大幅に削るため 50% を超えやすく、データ処理料金の対象になります。Microsoft Sentinel 有効ワークスペースの Analytics テーブルならこの処理料金は発生しません[^14]。

### 9.5 推奨対応順序

```
1. §9.2 (a) のパターン正規化で支配的テンプレートを特定
2. §9.2 (b)(c) で JSON 中身と I/D/E 内訳・1 件サイズを確定
3. アプリ改修が可能なら §9.3（出力レベル / 頻度 / JSON 文字列化の見直し）を最優先
4. 改修が難しい間は §9.4 (2) で Message を切り詰めて即時にサイズを削る
5. 不要系統があれば §9.4 (1) で行ごと除外
```

## 10. デバッグ用途のログをどう残すか（実務的な落としどころ）

開発者のデバッグ目的ですべてのトレースを取得していたケースでは、以下の組み合わせが現実的です。

1. **本番**: SDK 側で `Error` 以上のみエクスポート、加えて OpenTelemetry サンプリング 10%
2. **ステージング / 一部本番リソース**: `Warning` 以上 + サンプリング 50%（再現確認用）
3. **開発・障害調査時のみ**: `appsettings.json` を切り替えて一時的に `Information` / `Verbose` を有効化、調査終了後にロールバック
4. デバッグ向けに残したい大量の trace は `AppTraces` テーブルを **Basic Logs に切り替えて単価を下げる**[^15][^17]

このように「環境別のログレベル」と「テーブル プラン」を組み合わせることで、開発者の調査能力を一定維持しつつ、インジェスト料金の主要因である `AppTraces` の課金量を段階的に削減できます。

## 脚注

[^1]: Sampling in Azure Monitor Application Insights with OpenTelemetry, Microsoft Learn, https://learn.microsoft.com/en-us/azure/azure-monitor/app/opentelemetry-sampling

[^2]: Application Insights telemetry data model, Microsoft Learn, https://learn.microsoft.com/en-us/azure/azure-monitor/app/data-model-complete

[^3]: Monitor .NET and Node.js applications with Application Insights (Classic API 2.x) — ILogger 構成、`appsettings.json` の `Logging:ApplicationInsights:LogLevel`、既定で Warning 以上のみ送信される旨を含む, Microsoft Learn, https://learn.microsoft.com/en-us/azure/azure-monitor/app/ilogger

[^4]: AppTraces — Azure Monitor Logs reference, Microsoft Learn, https://learn.microsoft.com/en-us/azure/azure-monitor/reference/tables/apptraces

[^5]: SeverityLevel Enum (Microsoft.ApplicationInsights.DataContracts), Microsoft Learn, https://learn.microsoft.com/en-us/dotnet/api/microsoft.applicationinsights.datacontracts.severitylevel

[^6]: Cost optimization in Azure Monitor — Application Insights のチェックリストおよび推奨事項, Microsoft Learn, https://learn.microsoft.com/en-us/azure/azure-monitor/best-practices-cost

[^7]: Analyze usage in a Log Analytics workspace — Usage テーブル クエリ、Application Insights テーブル別ボリューム KQL, Microsoft Learn, https://learn.microsoft.com/en-us/azure/azure-monitor/logs/analyze-usage

[^8]: Sampling in Application Insights (Classic SDK) — Adaptive / Fixed-rate / Ingestion sampling の解説, Microsoft Learn, https://learn.microsoft.com/en-us/azure/azure-monitor/app/sampling-classic-api

[^9]: Configuring OpenTelemetry in Application Insights — `SamplingRatio` / `TracesPerSecond` のコード例, Microsoft Learn, https://learn.microsoft.com/en-us/azure/azure-monitor/app/opentelemetry-configuration

[^10]: Monitor .NET and Node.js applications with Application Insights — Filter and preprocess telemetry — `ITelemetryProcessor` / `ITelemetryInitializer`, Microsoft Learn, https://learn.microsoft.com/en-us/azure/azure-monitor/app/api-filtering-sampling

[^11]: Transformations in Azure Monitor — Workspace transformation DCR の仕様, Microsoft Learn, https://learn.microsoft.com/en-us/azure/azure-monitor/data-collection/data-collection-transformations

[^12]: Tables that support transformations in Azure Monitor Logs — `AppTraces` を含むサポート テーブル一覧, Microsoft Learn, https://learn.microsoft.com/en-us/azure/azure-monitor/logs/tables-feature-support

[^13]: Tutorial: Add a transformation in a workspace data collection rule by using the Azure portal, Microsoft Learn, https://learn.microsoft.com/en-us/azure/azure-monitor/logs/tutorial-workspace-transformations-portal

[^14]: Transformations in Azure Monitor — Cost for transformations, Microsoft Learn, https://learn.microsoft.com/en-us/azure/azure-monitor/data-collection/data-collection-transformations#cost-for-transformations

[^15]: Tables that support the Basic table plan in Azure Monitor Logs — Application Insights セクションに `AppTraces` を明記, Microsoft Learn, https://learn.microsoft.com/en-us/azure/azure-monitor/logs/basic-logs-azure-tables

[^16]: Query data in a Basic and Auxiliary table in Azure Monitor Logs — Basic Logs の KQL 制約・時間範囲・課金, Microsoft Learn, https://learn.microsoft.com/en-us/azure/azure-monitor/logs/basic-logs-query

[^17]: Select a table plan based on data usage in a Log Analytics workspace — プラン切り替え手順, Microsoft Learn, https://learn.microsoft.com/en-us/azure/azure-monitor/logs/basic-logs-configure

[^18]: Set daily cap on Log Analytics workspace — Daily Cap はコスト削減の主要手段ではなく予防策である旨を含む, Microsoft Learn, https://learn.microsoft.com/en-us/azure/azure-monitor/logs/daily-cap

[^19]: Azure Monitor Logs cost calculations and options — Commitment tiers, Microsoft Learn, https://learn.microsoft.com/en-us/azure/azure-monitor/logs/cost-logs

[^20]: Logging in IHttpClientFactory — HTTP requests with IHttpClientFactory, Microsoft Learn, https://learn.microsoft.com/en-us/aspnet/core/fundamentals/http-requests#logging-in-ihttpclientfactory

[^21]: Logging in .NET — How filtering rules are applied（最長プレフィックス マッチの仕様）, Microsoft Learn, https://learn.microsoft.com/en-us/dotnet/core/extensions/logging#how-filtering-rules-are-applied

[^22]: Dependency tracking in Azure Application Insights — `DependencyTrackingTelemetryModule` による HTTP 依存関係の自動収集（ILogger 構成と独立して動作）, Microsoft Learn, https://learn.microsoft.com/en-us/azure/azure-monitor/app/asp-net-dependencies

[^23]: Azure Monitor Logs cost calculations and options — Data size calculation（課金サイズは列の文字列表現から算出される）, Microsoft Learn, https://learn.microsoft.com/en-us/azure/azure-monitor/logs/cost-logs#data-size-calculation

[^24]: Logging in .NET — Log message template（メッセージ テンプレートとパラメータを分けて構造化保持する）, Microsoft Learn, https://learn.microsoft.com/en-us/dotnet/core/extensions/logging#log-message-template
