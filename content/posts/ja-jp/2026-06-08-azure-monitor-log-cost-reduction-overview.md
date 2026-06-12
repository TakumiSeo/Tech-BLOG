Title: Azure Monitor ログコスト削減 総まとめ — 6 テーブル横断分析とレイヤー別の打ち手
Date: 2026-06-08
Slug: azure-monitor-log-cost-reduction-overview
Lang: ja-jp
Category: notebook
Tags: azure, azure-monitor, log-analytics, application-insights, cost-optimization, observability
Summary: Application Insights / App Service / API Management 環境で Log Analytics のインジェストコストを押し上げる 6 テーブル（AppTraces / FunctionAppLogs / AppServiceHTTPLogs / AppServiceIPSecAuditLogs / AppDependencies / AppRequests）を横断分析した総まとめ。テーブルごとの性質・削減レバーの違いと、「1 リクエストが複数レイヤー・複数テーブルに分散課金される」構造、発生源（APIM / Function / SDK サンプリング）で抑える考え方を Microsoft Learn 根拠で整理。

Log Analytics のインジェストコストを分析していくと、コストの大半は少数の大きなテーブルに集中していることが分かります。本記事は、`AppTraces` を起点に 6 つのテーブルを横断分析した結果を統合し、**テーブルごとに削減の打ち手が違う理由**と、**1 つのリクエストが複数テーブルに分散課金される構造**を整理する総まとめです。各テーブルの詳細手順は個別記事にまとめています。

## 1. 分析対象の 6 テーブル

ログコスト分析でインジェストの大半を占めることが多いのが次の 6 テーブルです。本記事ではこれらを横断的に扱います。

| テーブル | 何を記録するか | 経路 | 個別記事 |
|---|---|---|---|
| `AppTraces` | アプリのトレース ログ（`ILogger` / `TrackTrace`） | Application Insights | [AppTraces 削減手順](apptraces-ingest-reduction.html) |
| `FunctionAppLogs` | Azure Functions のホスト / ユーザー ログ | 診断設定 | [FunctionAppLogs 削減手順](functionapplogs-ingest-reduction.html) |
| `AppServiceHTTPLogs` | App Service への受信 HTTP（Web サーバー ログ） | 診断設定 | [AppServiceHTTPLogs 削減手順](appservicehttplogs-ingest-reduction.html) |
| `AppServiceIPSecAuditLogs` | アクセス制限（IP Rules）の評価結果 | 診断設定 | [AppServiceIPSecAuditLogs 削減手順](appserviceipsecauditlogs-ingest-reduction.html) |
| `AppDependencies` | アプリからの送信呼び出し（HTTP / SQL など） | Application Insights | [AppDependencies 削減手順](appdependencies-ingest-reduction.html) |
| `AppRequests` | アプリへの受信リクエストのテレメトリ | Application Insights | [AppRequests 削減手順](apprequests-ingest-reduction.html) |

## 2. 大前提: コストの主役は「データインジェスト」

Log Analytics のコスト構造を整理すると、要素は大きく以下に分かれます[^1]。

| コスト要素 | 説明 |
| --- | --- |
| データインジェスト料金 | ワークスペースに取り込まれるデータ量に対する課金。通常、全体コストの大部分 |
| データ保持料金 | 既定の無料保持期間（31 日）を超える分への課金 |
| クエリ料金 | Basic / Auxiliary Logs テーブルへのクエリ実行時の課金 |

**コストの大半はデータインジェスト料金**であり[^1]、まずは「いかに取り込み量を適正化するか」が軸になります。本記事の 6 テーブルはいずれもインジェスト量で課金されます。

## 3. テーブルごとに「削減レバー」が違う理由

同じ「ログ削減」でも、テーブルの経路と性質によって効く打ち手が変わります。これが横断分析でいちばん重要な発見です。

| テーブル | 削減の主役 | ログレベル | Basic Logs | 向き |
|---|---|---|---|---|
| `AppTraces` | SDK ログレベル / サンプリング | あり（SeverityLevel） | **対応** | ログ |
| `FunctionAppLogs` | host.json ログレベル | あり（LevelId） | 非対応 | ログ |
| `AppServiceHTTPLogs` | transformation 行/列フィルタ | **なし** | 非対応 | 受信 |
| `AppServiceIPSecAuditLogs` | transformation（Denied 保持） | なし | 非対応 | アクセス制限 |
| `AppDependencies` | SDK サンプリング | なし | 非対応 | 送信 |
| `AppRequests` | SDK サンプリング | なし | 非対応 | 受信 |

### 3.1 「ログレベル」があるテーブル

`AppTraces` と `FunctionAppLogs` は**ログレベルの概念**を持つため、「出力元でレベルを上げて減らす」のが最優先です。

- `AppTraces`: `appsettings.json` の `Logging:ApplicationInsights:LogLevel`[^2]
- `FunctionAppLogs`: host.json の `logging.logLevel`[^3]

> 注意: `AppTraces` の `SeverityLevel` は `Information=1`、`FunctionAppLogs` の `LevelId` は `Information=2` と**マッピングが異なります**[^4][^5]。KQL でレベル フィルタを書く際は要注意です。

### 3.2 「ログレベルがない」テーブル

`AppServiceHTTPLogs` / `AppServiceIPSecAuditLogs` は **HTTP リクエスト 1 件 = 1 行**で、ログレベルがありません[^6][^7]。減らすには「**どの行を残すか**」を Workspace transformation DCR で決めるのが中心になります[^8][^9]。

### 3.3 Application Insights 経路のテーブル

`AppDependencies` / `AppRequests` は Application Insights のテレメトリで、**SDK サンプリング**が主役です[^10][^11]。サンプリングは `OperationId` 単位で関連テレメトリ（リクエスト・依存・トレース）をまとめて保持/破棄するため、分散トレースの相関が維持されます[^11]。

## 4. 横断で見えた構造: 1 リクエストが複数テーブルに分散課金される

個別テーブルを見るだけでは気づきにくいのが、**1 つの業務リクエストが複数のレイヤー・複数のテーブルに分散して課金される**という構造です。

```
[クライアント] → [API Management] → [Function / App Service] → [外部 API / SQL]

  API Management         → AppRequests（APIM 視点）
  Function / App Service → AppRequests（バックエンド視点）
                        → AppServiceHTTPLogs（Web サーバー受信）
                        → AppServiceIPSecAuditLogs（アクセス制限評価）
                        → AppDependencies（下流への送信呼び出し）
                        → AppTraces（処理中の ILogger / HttpClient ログ）
                        → FunctionAppLogs（Functions のホスト/ユーザー ログ）
```

これらは多くの場合**重複ではなく階層**です。`OperationId` で相関しており、「この受信リクエストが遅いのは、この下流呼び出しが遅いから」というエンドツーエンドの追跡を可能にしています。実際、受信（`AppRequests`）と送信（`AppDependencies`）を `OperationId` で突き合わせると、ほぼ全ての依存呼び出しが受信リクエストの子として紐づくことが確認できます。

### 4.1 「同じに見える」が「同じではない」

`AppServiceHTTPLogs`（受信）と `AppDependencies`（送信）は、エンドポイント名が似て見えても**向きが逆**です。前者は自分が受けたパス、後者は自分が呼んだ先のパスです[^6][^12]。`Name` の文字列一致だけで「重複」と判断せず、`OperationId` / `Target` / 件数の 3 軸で検証する必要があります。

### 4.2 だからこそ「発生源」で抑えるのが効率的

分散課金の構造が分かると、削減は**個別テーブルではなくレイヤーの発生源**で捉えるのが効率的だと分かります。

| レイヤー | 発生源での打ち手 | 効く範囲 |
|---|---|---|
| API Management | 診断の `Sampling (%)` を下げる[^13] | APIM 分の `AppRequests` |
| Function / App Service（App Insights） | OpenTelemetry サンプリング（`SamplingRatio`）[^10] | `AppRequests` / `AppDependencies` / `AppTraces` が相関維持で一括減 |
| Function（ログ） | host.json の `logging.logLevel`[^3] | `FunctionAppLogs` |
| App Service（診断ログ） | 診断設定 / transformation[^8][^9] | `AppServiceHTTPLogs` / `AppServiceIPSecAuditLogs` |

特に **OpenTelemetry サンプリングは 1 設定で 3 テーブル（`AppRequests` / `AppDependencies` / `AppTraces`）を相関維持のまま削減**できるため、個別に transformation を書くより効率的です[^10][^11]。

## 5. 「犯人」の典型パターン（横断的に頻出するもの）

6 テーブルを分析する中で繰り返し現れた「コストの犯人」パターンを整理します。

### 5.1 `IHttpClientFactory` の標準ログ

`IHttpClientFactory` 経由で作った `HttpClient` は、全リクエストについて `Start processing HTTP request` / `Sending HTTP request` を **Information レベル**で出力します[^14]。これが `AppTraces` / `FunctionAppLogs` を膨らませる典型です。外部 API を高頻度に呼ぶアプリで顕著で、`System.Net.Http.HttpClient` カテゴリを Warning に下げる、または `RemoveAllLoggers()` で対処します[^14][^15]。

> 重要: 失敗した HTTP 呼び出しの可視化は `AppDependencies`（依存関係テレメトリ）側で維持されるため[^12]、HttpClient のトレース ログ（`AppTraces`）を絞っても障害調査の可視性はほぼ失われません。

### 5.2 構造化ログの JSON 文字列化

アプリ（または共通ロギング基盤）が構造化ログを **JSON 文字列化して 1 メッセージに詰め込む**と、`AppTraces` の課金サイズが膨らみます。課金サイズは列の文字列表現から算出されるため[^16]、巨大な JSON 文字列がそのまま課金量になります。本来の `ILogger` はメッセージ テンプレートとパラメータを分けて渡すと、パラメータを `customDimensions` として構造化保持します[^17]。

### 5.3 監視・ヘルスチェック・合成トラフィック

`AppServiceHTTPLogs` / `AppRequests` では、ウォームアップ ping（`/robots933456.txt`）、ヘルスチェック（`/health` 等）、外形監視（`SyntheticSource`）がノイズの主因になりやすい部分です[^9][^18]。transformation で取り込み前に落とせます。

> 注意: App Service の Health check（`/health`）の ping は内部送信のため、`AppServiceHTTPLogs`（Web サーバー ログ）には現れません[^19]。HTTP ログのノイズはウォームアップ ping や外部監視である可能性が高い点に注意が必要です。

### 5.4 「監査ログ」だが削減余地があるもの

`AppServiceIPSecAuditLogs` は「Audit」という名前ですが、アクセス制限ルールにマッチした **allow / deny の両方**を記録します[^7]。監査の本質は `Denied`（拒否＝不正アクセス試行）であり、`Allowed`（正常）やヘルス プローブは削減余地が大きい部分です。「Audit だから触れない」ではなく「**本質（Denied）を残し、ノイズを削る**」が正しいアプローチです。

### 5.5 業務 API そのものが多い（技術判断の限界）

ノイズではなく、**業務 API の正常リクエストそのものが多い**ケースもあります。この場合、特定エンドポイントの狙い撃ち除外は業務影響があるため、一律サンプリングが現実解になります。ただし「正常リクエストをどこまで間引いてよいか」「監査・保持要件があるか」は技術データだけでは決められず、**顧客の利用目的の確認が必須**です。

## 6. 共通の制約（横断的に効く前提）

すべてのテーブルに共通する制約を整理します。

- **transformation のコスト**: Analytics テーブルでは、取り込み量を 50% を超えて削減するとデータ処理料金が発生します（計算式 `[削減 GB] − [受信 GB] / 2`）。ただし Microsoft Sentinel 有効ワークスペースの Analytics テーブルでは、いくら削減してもこの処理料金は発生しません[^9][^20]。
- **Basic Logs の可否**: `AppTraces` のみ Basic Logs 対応。他の 5 テーブルは非対応で、残量の単価最適化は**コミットメント階層**が主手段です[^4][^21]。
- **サンプリングとメトリクス**: サンプリングしてもメトリクス（事前集計）は影響を受けず、正確な値が維持されます。クエリの件数は `count()` ではなく `sum(ItemCount)` で補正します[^11]。
- **診断設定の粒度**: 診断設定はカテゴリ単位でしか選択できず、カテゴリ内の粒度フィルタ（特定パス / ステータス / レベルの除外）は transformation で行います[^8]。

## 7. 推奨アプローチ（横断的な優先順位）

個別テーブルの手順を統合すると、横断的な優先順位は次のようになります。

1. **現状把握**: `Usage` テーブルでテーブル別インジェスト量を可視化し、大きいテーブルから着手する[^1]。
2. **発生源を特定**: `AppRoleName`（APIM / Function / App Service のどれか）、`OperationId` 相関、カテゴリ / Name / Result でコストの「犯人」を絞り込む。
3. **発生源で抑える**:
   - Application Insights 系（`AppRequests` / `AppDependencies` / `AppTraces`）は **OpenTelemetry サンプリング**で一括削減[^10][^11]。
   - APIM が発生源なら **APIM 診断の `Sampling (%)`** を下げる[^13]。
   - ログ系は **host.json / appsettings.json のログレベル**を見直す[^2][^3]。
4. **取り込み時フィルタで補助**: コード変更が難しい場合や、特定の行 / 列だけ落としたい場合は **Workspace transformation DCR**[^8][^9]。
5. **残量を単価最適化**: 削減後に 100 GB/day 以上で安定するなら **コミットメント階層**[^21]。
6. **顧客確認が必要な判断**: 業務 API のサンプリング率、監査・保持要件、二重記録テーブルの取捨は、技術データだけでは決められないため顧客の利用目的を確認する。

## 8. まとめ

ログコスト削減は「テーブルを 1 つずつ削る」のではなく、「**1 リクエストが複数レイヤー・複数テーブルに分散課金される構造を理解し、発生源で抑える**」のが本質です。

- テーブルの**経路**（Application Insights / 診断設定）と**性質**（ログレベルの有無 / 受信か送信か）で削減レバーが変わる。
- Application Insights 系は **サンプリング**が、診断ログ系は **transformation** が、ログ系は **ログレベル** が主役。
- **OpenTelemetry サンプリング**と **APIM の Sampling (%)** は、それぞれ複数テーブルや発生源に一括で効く強力な打ち手。
- 「監査だから」「業務 API だから」で思考停止せず、**性質を理解した上で本質を残しノイズを削る**。最終的な可否判断（業務影響・監査要件）は顧客の利用目的を確認する。

各テーブルの具体的な手順・KQL・transformation の例は、第 1 章の個別記事を参照してください。

---

[^1]: Azure Monitor Logs cost calculations and options（コスト構造、インジェストが最大要因）, https://learn.microsoft.com/azure/azure-monitor/logs/cost-logs

[^2]: Monitor .NET and Node.js applications with Application Insights（ILogger 構成、Logging:ApplicationInsights:LogLevel）, https://learn.microsoft.com/azure/azure-monitor/app/ilogger

[^3]: How to configure monitoring for Azure Functions — Configure log levels（host.json logging.logLevel）, https://learn.microsoft.com/azure/azure-functions/configure-monitoring

[^4]: AppTraces — Azure Monitor Logs reference（SeverityLevel、Basic log 対応）, https://learn.microsoft.com/azure/azure-monitor/reference/tables/apptraces

[^5]: FunctionAppLogs — Azure Monitor Logs reference（Level / LevelId、Basic log 非対応）, https://learn.microsoft.com/azure/azure-monitor/reference/tables/functionapplogs

[^6]: AppServiceHTTPLogs — Azure Monitor Logs reference（Web サーバー ログ、列定義）, https://learn.microsoft.com/azure/azure-monitor/reference/tables/appservicehttplogs

[^7]: Azure App Service access restrictions — Diagnostic logging（IPSecurity Audit logs: allow / deny 両方を記録）, https://learn.microsoft.com/azure/app-service/overview-access-restrictions

[^8]: Diagnostic settings in Azure Monitor — Controlling costs（カテゴリ単位のみ、粒度フィルタは transformation）, https://learn.microsoft.com/azure/azure-monitor/platform/diagnostic-settings

[^9]: Transformations in Azure Monitor — Workspace transformation DCR / Cost for transformations, https://learn.microsoft.com/azure/azure-monitor/data-collection/data-collection-transformations

[^10]: Sampling in Azure Monitor Application Insights with OpenTelemetry（SamplingRatio、既定で無効）, https://learn.microsoft.com/azure/azure-monitor/app/opentelemetry-sampling

[^11]: Sampling in Application Insights（OperationId 単位で関連項目をまとめて選択、メトリクスは再正規化、ItemCount）, https://learn.microsoft.com/azure/azure-monitor/app/sampling-classic-api

[^12]: Dependency tracking in Application Insights（依存関係 = 送信呼び出し、DependencyTrackingTelemetryModule）, https://learn.microsoft.com/azure/azure-monitor/app/dependencies

[^13]: How to integrate Azure API Management with Azure Application Insights（Sampling (%)、既定 100%、Always log errors）, https://learn.microsoft.com/azure/api-management/api-management-howto-app-insights

[^14]: Make HTTP requests with IHttpClientFactory in ASP.NET Core — Logging（既定で全リクエストを Information で記録）, https://learn.microsoft.com/aspnet/core/fundamentals/http-requests

[^15]: HTTP client logging in .NET（既定ロガーの差し替え / 無効化）, https://learn.microsoft.com/dotnet/core/extensions/httpclient-logging

[^16]: Azure Monitor Logs cost calculations and options — Data size calculation（課金サイズは列の文字列表現から算出）, https://learn.microsoft.com/azure/azure-monitor/logs/cost-logs

[^17]: Logging in .NET — Log message template（テンプレートとパラメータを分けて構造化保持）, https://learn.microsoft.com/dotnet/core/extensions/logging

[^18]: Filter Azure Monitor OpenTelemetry — Filter telemetry at ingestion using DCR（ヘルスチェック / 合成トラフィック除外の DCR サンプル）, https://learn.microsoft.com/azure/azure-monitor/app/opentelemetry-filter

[^19]: Monitor App Service instances by using Health check — FAQ（Health check の ping は Web サーバー ログに現れない）, https://learn.microsoft.com/azure/app-service/monitor-instances-health-check

[^20]: Transformations in Azure Monitor — Cost for transformations（50% ルール、Sentinel 例外）, https://learn.microsoft.com/azure/azure-monitor/data-collection/data-collection-transformations

[^21]: Azure Monitor Logs cost calculations and options — Commitment tiers, https://learn.microsoft.com/azure/azure-monitor/logs/cost-logs
