Title: AppServiceHTTPLogs のインジェストを削減する手順（Azure App Service / Log Analytics）
Date: 2026-06-08
Slug: appservicehttplogs-ingest-reduction
Lang: ja-jp
Category: notebook
Tags: azure, azure-monitor, app-service, log-analytics, cost-optimization, observability
Summary: Azure App Service の診断設定で収集される AppServiceHTTPLogs テーブルが大きなインジェストを占める環境向けに、診断設定のカテゴリ選択 / Workspace transformation DCR による行・列フィルタ / コミットメント階層までを Microsoft Learn 根拠で順序立てて整理。AppTraces / FunctionAppLogs と異なり「ログレベルの概念がなく 1 リクエスト = 1 行」という Web サーバー ログ特有の削減ルートを扱う。

`AppTraces`（Application Insights）、`FunctionAppLogs`（Azure Functions）に続いて、ログ コスト分析で大きくなりがちなのが Azure App Service の `AppServiceHTTPLogs` テーブルです。本記事では、Microsoft Learn 公式ドキュメントに基づいて、**効果が大きく実装コストが低い順**に削減手順を整理します。

> 前提の違い: `AppTraces` / `FunctionAppLogs` には「ログレベル（Information / Warning など）」があり、出力元でレベルを上げれば量を減らせました。しかし **`AppServiceHTTPLogs` は Web サーバー ログ**であり、**HTTP リクエスト 1 件につき必ず 1 行**が記録されます[^2][^3]。ログレベルの概念がないため、削減の主役は「**どの行を残すか**（診断設定 / transformation でのフィルタ）」に移ります。

## 1. AppServiceHTTPLogs とは何か（前提整理）

`AppServiceHTTPLogs` は **App Service（`microsoft.web/sites`）の診断設定** で `AppServiceHTTPLogs` カテゴリを Log Analytics ワークスペースへ送ったときに作成されるテーブルです。**Web サーバーへの受信 HTTP リクエストの生データ（W3C 拡張ログ形式）**が、リクエストごとに 1 行記録されます[^1][^2][^3]。

### 1.1 収集経路（AppTraces との最大の違い）

リソース ログは**診断設定を作成して送信先（Log Analytics / Storage / Event Hubs）へルーティングするまで収集・保存されません**[^3]。`AppServiceHTTPLogs` は次の性質を持ちます。

- 収集を止める / 送信先を変える操作が**診断設定の構成だけ**で完結する
- 診断設定は**カテゴリ単位でしか選択できず、カテゴリ内部の粒度フィルタ（特定 URL / ステータスの除外など）はできない**[^6]
- 診断設定を追加 / 変更すると App Service にアプリ設定が追加され、**アプリが再起動**する[^3]

粒度フィルタ（成功リクエストの除外、特定パスの除外など）は Workspace transformation DCR（取り込み時）で行うことになります。

### 1.2 AppServiceHTTPLogs の主なフィールド

W3C 拡張ログ形式に対応した以下の列を持ちます[^1]。

| 列 | 内容 |
|---|---|
| `CsMethod` | HTTP メソッド（GET / POST など） |
| `CsUriStem` | リクエスト対象パス |
| `CsUriQuery` | クエリ文字列 |
| `CsHost` | Host ヘッダー |
| `ScStatus` | HTTP ステータス コード（int） |
| `ScSubStatus` | サブステータス |
| `TimeTaken` | 所要時間（ミリ秒） |
| `CIp` | クライアント IP |
| `UserAgent` | User-Agent |
| `Referer` | リファラー |
| `Cookie` | リクエストの Cookie |
| `CsBytes` / `ScBytes` | 受信 / 送信バイト数 |
| `Result` | 成功 / 失敗 |
| `_BilledSize` / `_IsBillable` | 課金サイズ / 課金対象フラグ |

コスト分析では `_BilledSize` と `_IsBillable` が中心指標です。`Cookie` / `CsUriQuery` / `UserAgent` / `Referer` は 1 行あたりのサイズを押し上げやすい列で、列フィルタの候補になります（手順 3.2）。

### 1.3 テーブルの機能サポート（重要な制約）

| 項目 | 値 | 影響 |
|---|---|---|
| Basic Logs プラン | **非対応（No）** | `FunctionAppLogs` と同様、**Basic Logs への切り替えはできない**[^1][^4] |
| Ingestion-time DCR transformation | **対応（Yes）** | Workspace transformation DCR で取り込み時の行・列フィルタが可能[^1][^4] |

> `AppServiceHTTPLogs` も Basic Logs 非対応のため、「Basic Logs で単価を下げる」手段は使えません。**取り込み量そのものを減らす**施策（診断設定 / transformation）の比重が高くなります。

### 1.4 「量産」の典型的な発生源

`AppServiceHTTPLogs` はトラフィックに比例して増えるため、次のような「監視・自動化・ノイズ」トラフィックが大きな割合を占めることがよくあります。

- **ウォームアップ ping**: `WEBSITE_WARMUP_PATH` の既定値は `/robots933456.txt` で、コンテナ起動時にオーケストレーターが繰り返しリクエストします[^14]
- **Always On / 監視 ping**: 外形監視・死活監視ツールからの定期リクエスト
- **ボット / クローラー**: `UserAgent` で識別できる自動アクセス
- **静的アセット**: 画像 / CSS / JS など 2xx で返る大量の成功リクエスト
- **高頻度ポーリング エンドポイント**: SPA のステータス確認など

> 注: **App Service の Health check（`/health` 等）の ping は内部送信のため、Web サーバー ログ（`AppServiceHTTPLogs`）には現れません**[^13]。`AppServiceHTTPLogs` で見える「ヘルス チェック風」のノイズは、ウォームアップ ping（`/robots933456.txt`）や外部監視ツールのリクエストである可能性が高い点に注意してください。

## 2. 削減アプローチの優先順位（Microsoft Learn ベストプラクティス）

Microsoft のコスト最適化ガイダンスは、リソース ログ（診断設定）について次を挙げています[^7][^6]。

1. **必要なログ カテゴリだけを収集する**（診断設定で `AppServiceHTTPLogs` が本当に必要か棚卸し）[^7]
2. **Workspace transformation DCR で取り込み時に行・列フィルタ**（診断設定はカテゴリ内の粒度フィルタができないため）[^6][^7][^8]
3. 残った量に対して**コミットメント階層**で単価を最適化[^11]

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

`AppServiceHTTPLogs` をステータス クラス別に集計（成功が大半か、エラーが多いか）[^1][^5]:

```kusto
AppServiceHTTPLogs
| where TimeGenerated > ago(1d)
| where _IsBillable == true
| extend StatusClass = strcat(substring(tostring(ScStatus), 0, 1), "xx")
| summarize Records = count(), BillableGB = sum(_BilledSize)/1024/1024/1024
        by StatusClass
| order by BillableGB desc
```

`_ResourceId`（アプリ）別の課金ボリューム（上位）[^1]:

```kusto
AppServiceHTTPLogs
| where TimeGenerated > ago(7d)
| where _IsBillable == true
| summarize BillableGB = sum(_BilledSize)/1024/1024/1024, Records = count()
        by _ResourceId
| order by BillableGB desc
```

典型的な環境では、`2xx` の成功リクエストが件数・課金量の大半を占めます。その場合の目標は「**監視 / ボット / 静的アセットなど価値の低い成功リクエストを取り込み前に落とす**」ことになります（→ 手順 3）。

### 手順 1 — 診断設定を見直す（カテゴリ選択 / 送信先）

リソース ログのコストは送信先と量で決まります。Microsoft は診断設定のコスト管理として次を挙げています[^6][^7]。

1. **各サービスで必要なログ カテゴリだけを収集する**（`AppServiceHTTPLogs` が本当に Log Analytics に必要か棚卸し）
2. カテゴリ内の粒度フィルタは診断設定ではできないため、**transformation を使う**（手順 2）

監査 / アクセス記録として「即時のログ検索やアラートには使わないが保管したい」場合は、**Log Analytics への送信を止めて Storage アーカイブのみに切り替える**選択肢もあります[^3][^6]。Web サーバー ログは法令・セキュリティ要件でアクセス ログの長期保管を求められることがあり、その用途なら Storage の方が低コストです。

### 手順 2 — Workspace transformation DCR（取り込み時の行フィルタ）

診断設定で送られるリソース ログは通常の DCR を使わない収集経路のため、Microsoft は **Workspace transformation DCR**（ワークスペースに直接適用される特別な DCR）でフィルタすることを推奨しています[^8][^7]。

- `AppServiceHTTPLogs` は **ingestion-time DCR transformation 対応テーブル**[^1][^4]
- Workspace DCR はワークスペースごとに **1 つ**で、複数テーブルの transformation を含められる[^8]
- 既定の Azure ポータル ウィザード（`Log Analytics workspace > Tables > Create transformation`）から構成可能[^8]

#### 2.1 ウォームアップ ping / 監視ノイズを除外

`/robots933456.txt` などのウォームアップ ping や、特定 User-Agent の監視ツールを落とす例[^10][^14]:

```kusto
source
| where CsUriStem != "/robots933456.txt"
| where UserAgent !has "AlwaysOn"
| where UserAgent !has "HealthCheck"
```

#### 2.2 成功した静的アセットを除外（エラー・動的リクエストは残す）

2xx の静的ファイルを落とし、エラーや動的処理は可視性を維持する例[^10]:

```kusto
source
| where not(ScStatus >= 200 and ScStatus < 300
            and CsUriStem matches regex @"\.(?i)(css|js|png|jpg|jpeg|gif|svg|ico|woff2?)$")
```

#### 2.3 成功リクエストはサンプリング、エラー・遅延は全件保持

「正常系は一部だけ、異常系は全件」という方針も transformation で表現できます。`hash()` でおおよそ 10% を残す例:

```kusto
source
| where ScStatus >= 400            // エラーは全件保持
    or TimeTaken >= 1000           // 遅延リクエストは全件保持
    or hash(CIp, 10) == 0          // 正常系は約 10% をサンプリング
```

### 手順 3 — 列フィルタで 1 行のサイズを縮める（行を残しつつ削減）

`AppServiceHTTPLogs` の課金サイズは**各列の文字列表現から算出**され、`_ResourceId` / `_SubscriptionId` / `_ItemId` / `_IsBillable` / `_BilledSize` / `TenantId` / `Type` の標準列は課金対象外です[^12]。`Cookie` / `CsUriQuery` / `UserAgent` / `Referer` のような大きい列が不要なら、`project-away` で落とすことで件数を保ったまま課金量を下げられます[^10]。

```kusto
source
| project-away Cookie, CsUriQuery, Referer
```

> 注意: 列を落とすと当然その列での調査はできなくなります。`CsUriQuery` を落とすとクエリ文字列ベースの分析が、`Cookie` を落とすとセッション調査ができなくなります。残す必要がある列は慎重に選んでください。

### 手順 4 — Daily Cap / Commitment Tier（ワークスペース レベル）

`AppServiceHTTPLogs` 固有の手段を尽くした後は、ワークスペース全体の施策に移ります。

- **Daily Cap**: 予期しないスパイクへのセーフティ ネット。コスト削減の主要手段ではない[^7]
- **Commitment Tier**: 削減後に残った取り込み量が 100 GB/day 以上で安定していれば、Pay-as-you-go から移行して単価を下げられる。`Usage and estimated costs` 画面に各階層の推定が表示される[^11]

> 注: `AppServiceHTTPLogs` は **Basic Logs 非対応**[^1][^4]のため、「デバッグ用テーブルを Basic Logs に切り替えて単価を下げる」手段は適用できません。残量に対してはコミットメント階層が主な単価最適化手段になります。

## 4. 推奨実行順序（まとめ表）

| # | アクション | 効果 | リスク |
|---|---|---|---|
| 1 | 現状把握 KQL（手順 0） | — | なし |
| 2 | 診断設定で `AppServiceHTTPLogs` の要否を棚卸し / 監査用途は Storage アーカイブへ[^3][^6] | 中〜大 | アクセス ログの即時検索性が低下 |
| 3 | Workspace transformation DCR でウォームアップ ping / 監視 / ボット / 静的アセットを除外[^8][^10] | **大**（正常系ノイズを取り込み前に破棄） | 50% 超の削減で transformation 料金（手順 5） |
| 4 | 成功リクエストはサンプリング、エラー / 遅延は全件保持[^10] | 大 | 正常系の網羅性が下がる（統計は維持可能） |
| 5 | 列フィルタ（`Cookie` / `CsUriQuery` / `Referer`）で 1 行を縮める[^10][^12] | 中 | 該当列での調査ができなくなる |
| 6 | Commitment Tier に移行[^11] | 中（単価引き下げ） | 31 日コミット |
| — | Basic Logs への切り替え | **不可**（テーブル非対応）[^1][^4] | — |

## 5. transformation のコスト（重要）

transformation を主軸にする場合、コスト構造を正確に押さえておく必要があります[^9]。

| テーブル プラン | Transformation のコスト |
|---|---|
| **Analytics**（`AppServiceHTTPLogs` は Basic 非対応のため通常こちら） | Transformation 自体は通常無料。ただし**取り込みデータ量を 50% を超えて削減した場合、超過分はデータ処理料金として課金**。計算式: `[削減した GB] − ([受信 GB] / 2)` |
| **Auxiliary Logs** | 受信データ全量にデータ処理料金が課金され、加えて取り込み後の量に取り込み料金が課金 |
| Microsoft Sentinel が有効な場合 | Analytics テーブルへの transformation は**金額がいくら削減されても無料**[^9] |

計算例[^9]: 受信 20 GB に対し 12 GB を削減 → 取り込み 8 GB / データ処理課金 2 GB（= 12 − 20/2）/ 取り込み課金 8 GB。

> `AppServiceHTTPLogs` の削減は「監視 / ボット / 静的アセット」を落とすことで容易に 50% を超えるため、データ処理料金の対象になりやすいです。それでも単価次第では取り込み料金の削減が処理料金を上回ることが多く、効果は出ます。Sentinel 有効ワークスペースなら処理料金は発生しません[^9]。

## 6. 「犯人」を特定する KQL クエリ集

`2xx` の成功リクエストが支配的な場合、ゴールは「**どのパス / User-Agent / クライアントが価値の低いトラフィックを生んでいるか**を特定して、それを transformation で落とす」ことです。`CsUriStem` / `UserAgent` / `CIp` / `ScStatus` / `_BilledSize` / `_IsBillable` は `AppServiceHTTPLogs` の公式スキーマに存在します[^1]。

### 6.1 パス（CsUriStem）別の課金量（パレート確認）

```kusto
AppServiceHTTPLogs
| where TimeGenerated > ago(7d)
| where _IsBillable == true
| summarize BillableGB = sum(_BilledSize)/1024/1024/1024,
            Records   = count()
        by CsUriStem
| top 50 by BillableGB desc
```

`/robots933456.txt` や監視用エンドポイント、特定の静的ファイルが上位に来やすいです。

### 6.2 パス × ステータス クラスのクロス集計

```kusto
AppServiceHTTPLogs
| where TimeGenerated > ago(7d)
| where _IsBillable == true
| extend StatusClass = strcat(substring(tostring(ScStatus), 0, 1), "xx")
| summarize BillableGB = sum(_BilledSize)/1024/1024/1024
        by CsUriStem, StatusClass
| evaluate pivot(StatusClass, sum(BillableGB))
| order by ['2xx'] desc
```

「2xx で大量に返っているパス」＝サンプリング / 除外の最有力候補が一目で分かります。

### 6.3 User-Agent 別（ボット / 監視ツールの検出）

```kusto
AppServiceHTTPLogs
| where TimeGenerated > ago(1d)
| where _IsBillable == true
| summarize BillableGB = sum(_BilledSize)/1024/1024/1024,
            Records   = count()
        by UserAgent
| top 30 by BillableGB desc
```

監視ツール / クローラー / ヘルス プローブの User-Agent が大きな割合を占めていれば、手順 2.1 の除外対象になります。

### 6.4 クライアント IP 別（特定の発信元の偏り）

```kusto
AppServiceHTTPLogs
| where TimeGenerated > ago(1d)
| where _IsBillable == true
| summarize BillableGB = sum(_BilledSize)/1024/1024/1024,
            Records   = count()
        by CIp
| top 30 by BillableGB desc
```

外形監視サービスや特定バッチの固定 IP が突出していれば、その発信元を落とす判断ができます。

### 6.5 時系列（デプロイ / キャンペーン後スパイクの確認）

```kusto
AppServiceHTTPLogs
| where TimeGenerated > ago(7d)
| where _IsBillable == true
| summarize BillableGB = sum(_BilledSize)/1024/1024/1024
        by bin(TimeGenerated, 1h), _ResourceId
| render timechart
```

### 6.6 次アクション例

1. 6.1 / 6.2 で「2xx が大量のパス」、6.3 で「ノイズ User-Agent」、6.4 で「偏った IP」を特定
2. 手順 2.1〜2.3 の transformation でそれらを除外 / サンプリング
3. それでも 1 行が大きい場合は手順 3 の列フィルタ（`Cookie` / `CsUriQuery` / `Referer`）を併用
4. 反映後、手順 0 の Usage クエリと 6.1 で削減量を確認

## 7. 注意点（横断的な制約まとめ）

- **ログレベルの概念がない**: `AppServiceHTTPLogs` は HTTP リクエスト 1 件 = 1 行であり、`AppTraces` / `FunctionAppLogs` のような「レベルを上げて減らす」手段が使えない。減らすには行フィルタ（transformation）か収集停止（診断設定）が中心[^2][^3]。
- **診断設定はカテゴリ内の粒度フィルタができない**: 特定 URL / ステータスの除外は transformation（取り込み時）で行う[^6]。
- **`AppServiceHTTPLogs` は Basic Logs 非対応**: 単価を下げる主手段はコミットメント階層[^1][^4][^11]。
- **Health check ping は HTTP ログに出ない**: 内部送信のため `AppServiceHTTPLogs` には現れない。ノイズの正体はウォームアップ ping / 外部監視であることが多い[^13][^14]。
- **transformation × Microsoft Sentinel**: Sentinel が有効なワークスペースの Analytics テーブルでは transformation のデータ処理料金は発生しない[^9]。
- **診断設定の追加・変更でアプリ再起動**: `AppServiceHTTPLogs` の診断設定変更はアプリ設定追加を伴い、App Service が再起動する[^3]。
- **診断設定の反映遅延**: 設定後、データ送信開始まで最大 90 分かかることがある[^6]。

---

[^1]: AppServiceHTTPLogs（テーブル リファレンス: 列定義、Basic log 非対応、Ingestion-time DCR 対応）, https://learn.microsoft.com/azure/azure-monitor/reference/tables/appservicehttplogs

[^2]: Azure App Service monitoring data reference — Resource logs（AppServiceHTTPLogs = Web server logs）, https://learn.microsoft.com/azure/app-service/monitor-app-service-reference

[^3]: Enable diagnostic logs for apps in Azure App Service（Web サーバー ログ = W3C 拡張形式、診断設定追加でアプリ再起動、Storage への送信）, https://learn.microsoft.com/azure/app-service/troubleshoot-diagnostic-logs

[^4]: Supported logs for Microsoft.Web/sites（AppServiceHTTPLogs: Basic log No, transformation Yes）, https://learn.microsoft.com/azure/azure-monitor/reference/supported-logs/microsoft-web-sites-logs

[^5]: Queries for the AppServiceHTTPLogs table（サンプル クエリ: ScStatus, CsUriStem, UserAgent 等）, https://learn.microsoft.com/azure/azure-monitor/reference/queries/appservicehttplogs

[^6]: Diagnostic settings in Azure Monitor — Controlling costs（カテゴリ単位のみ選択可、粒度フィルタは transformation）, https://learn.microsoft.com/azure/azure-monitor/platform/diagnostic-settings

[^7]: Cost optimization in Azure Monitor（Collect only critical resource log data / workspace transformation）, https://learn.microsoft.com/azure/azure-monitor/fundamentals/best-practices-cost

[^8]: Transformations in Azure Monitor — Workspace transformation DCR, https://learn.microsoft.com/azure/azure-monitor/data-collection/data-collection-transformations

[^9]: Transformations in Azure Monitor — Cost for transformations（50% ルール, 計算式, Sentinel 例外）, https://learn.microsoft.com/azure/azure-monitor/data-collection/data-collection-transformations

[^10]: Sample transformations in Azure Monitor — Reduce data costs（where による行フィルタ / project-away による列フィルタ）, https://learn.microsoft.com/azure/azure-monitor/data-collection/data-collection-transformations-samples

[^11]: Azure Monitor Logs cost calculations and options — Commitment tiers, https://learn.microsoft.com/azure/azure-monitor/logs/cost-logs

[^12]: Azure Monitor Logs cost calculations and options — Data size calculation（課金サイズは列の文字列表現から算出、標準列は課金対象外）, https://learn.microsoft.com/azure/azure-monitor/logs/cost-logs#data-size-calculation

[^13]: Monitor App Service instances by using Health check — FAQ（Health check の ping は内部送信のため Web サーバー ログに現れない）, https://learn.microsoft.com/azure/app-service/monitor-instances-health-check

[^14]: Environment variables and app settings in Azure App Service（`WEBSITE_WARMUP_PATH` 既定値 `/robots933456.txt`、オーケストレーターが繰り返しリクエスト）, https://learn.microsoft.com/azure/app-service/reference-app-settings
