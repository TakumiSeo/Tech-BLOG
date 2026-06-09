Title: AppServiceIPSecAuditLogs のインジェストを削減する手順（Azure App Service アクセス制限の監査ログ）
Date: 2026-06-08
Slug: appserviceipsecauditlogs-ingest-reduction
Lang: ja-jp
Category: notebook
Tags: azure, azure-monitor, app-service, log-analytics, cost-optimization, security
Summary: Azure App Service のアクセス制限（IP Rules / Access Restrictions）の評価結果を記録する AppServiceIPSecAuditLogs テーブルが大きなインジェストを占める環境向けに、監査の本質（Denied）を残しつつヘルス プローブ・正常 Allowed を削る方針を Microsoft Learn 根拠で整理。「Audit だから触れない」ではなく性質を理解した削減を扱う。

`AppServiceHTTPLogs` に続いて、Azure App Service 環境でログ コストを押し上げがちなのが `AppServiceIPSecAuditLogs` テーブルです。「Audit（監査）」という名前から「触ってはいけない」と思われがちですが、本記事では Microsoft Learn 公式ドキュメントに基づき、**監査の本質を保ったまま削減できる部分**を順序立てて整理します。

> 結論を先に: `AppServiceIPSecAuditLogs` は「アクセス制限ルールにマッチした全リクエスト（**allow / deny の両方**）を記録する」ログです[^2]。つまり **リクエスト 1 件 = 1 行**で、トラフィックに比例して増えます。監査価値が高いのは `Denied`（拒否＝不正アクセス試行）であり、`Allowed`（正常）やヘルス プローブは**削減余地が大きい**部分です。

## 1. AppServiceIPSecAuditLogs とは何か（前提整理）

`AppServiceIPSecAuditLogs` は **App Service（`microsoft.web/sites`）のアクセス制限（Access Restrictions / IP Rules）の評価結果** を記録するテーブルです。App Service 診断ログのカテゴリ `IPSecurity Audit logs` を Log Analytics ワークスペースへ送ったときに作成されます[^2][^3]。

### 1.1 何が記録されるか（重要）

公式ドキュメントの記述が決定的です[^2]:

> **「unmatched rule を除き、ルールにマッチした全リクエスト（allow / deny の両方）が記録され、アクセス制限の構成検証に使える」**

ここから次のことが分かります。

- **`Allowed` も `Denied` も両方記録される**（拒否だけではない）
- **`TimeGenerated` は "Time of the Http Request"** = リクエストごとに 1 行[^1]
- 用途は本来「**アクセス制限ルールの構成検証・トラブルシュート**」[^2]
- unmatched rule（どのルールにもマッチしないデフォルト動作）の分は記録されない[^2]

つまり「監査」と名前は付いていますが、実体は **アクセス制限ルールの評価ログ**であり、トラフィック比例で青天井に増える性質を持ちます。

### 1.2 AppServiceIPSecAuditLogs の主なフィールド

| 列 | 内容 |
|---|---|
| `Result` | **Allowed / Denied**（アクセス制限の評価結果）[^1] |
| `CIp` | クライアント IP |
| `CsHost` | Host ヘッダー |
| `Details` | 追加情報（マッチしたルール等） |
| `ServiceEndpoint` | VNet サービス エンドポイント経由か |
| `XAzureFDID` | X-Azure-FDID（Azure Front Door インスタンス ID）[^1][^4] |
| `XFDHealthProbe` | **X-FD-HealthProbe（Front Door のヘルス プローブ。`1` が送られる）**[^1][^4] |
| `XForwardedFor` | X-Forwarded-For（プロキシ経由の元 IP） |
| `XForwardedHost` | X-Forwarded-Host |
| `_BilledSize` / `_IsBillable` | 課金サイズ / 課金対象フラグ |

コスト分析では `_BilledSize` / `_IsBillable` が中心指標です。削減の鍵になるのは **`Result`** と **`XFDHealthProbe`** です。

### 1.3 テーブルの機能サポート（重要な制約）

| 項目 | 値 | 影響 |
|---|---|---|
| Basic Logs プラン | **非対応（No）** | `AppServiceHTTPLogs` と同様、**Basic Logs への切り替えはできない**[^1] |
| Ingestion-time DCR transformation | **対応（Yes）** | Workspace transformation DCR で取り込み時の行フィルタが可能[^1] |

> Basic Logs 非対応のため、「Basic Logs で単価を下げる」手段は使えません。**取り込み量そのものを減らす**施策（transformation / 診断設定）が中心になります。

## 2. 「Audit だから削減できない」は誤解 — 削減できる根拠

監査ログは「触ってはいけない」と扱われがちですが、`AppServiceIPSecAuditLogs` については次の事実から**削減余地があります**。

1. **`Allowed` も記録される**[^2] — 監査・セキュリティ調査の本質的な関心は `Denied`（不正アクセス試行）であり、正常な `Allowed` を全件残す必要性は用途次第で低い。
2. **Front Door のヘルス プローブも記録される**[^1][^4] — `XFDHealthProbe` が立つプローブ リクエストは定期的に大量発生し、それも 1 行ずつ記録される。**監査価値はゼロ**。
3. **本来の用途は「ルール構成の検証・トラブルシュート」**[^2] — 恒久的なセキュリティ監査台帳というより、構成検証ツールとしての位置づけ。

> ただし慎重さも正しい: `Denied`（拒否されたアクセス＝不正アクセス試行の記録）は**セキュリティ インシデント調査の価値が高い**ため、ここは残すのが基本です。削減は「**ノイズ（プローブ・正常 Allowed）を削り、本質（Denied）を残す**」方向で行います。

## 3. 現状把握用 KQL クエリ

### 3.1 Allowed / Denied の比率（最重要）

```kusto
AppServiceIPSecAuditLogs
| where TimeGenerated > ago(1d)
| where _IsBillable == true
| summarize Records = count(), BillableGB = sum(_BilledSize)/1024/1024/1024
        by Result
| order by BillableGB desc
```

`Allowed` が大半（例: 99%）なら、そこが最大の削減対象です。

### 3.2 Front Door ヘルス プローブの割合

```kusto
AppServiceIPSecAuditLogs
| where TimeGenerated > ago(1d)
| where _IsBillable == true
| summarize Records = count(), BillableGB = sum(_BilledSize)/1024/1024/1024
        by IsHealthProbe = isnotempty(XFDHealthProbe)
```

プローブ（`XFDHealthProbe` あり）が大きな割合を占めていれば、**監査価値ゼロのノイズ**として丸ごと除外できます。

### 3.3 クライアント IP / ホスト別（偏りの確認）

```kusto
AppServiceIPSecAuditLogs
| where TimeGenerated > ago(1d)
| where _IsBillable == true
| summarize Records = count(), BillableGB = sum(_BilledSize)/1024/1024/1024
        by CIp, Result
| top 30 by BillableGB desc
```

特定の監視サービス / Front Door の固定 IP が突出していれば、その発信元を落とす判断ができます。

### 3.4 アプリ（_ResourceId）別

```kusto
AppServiceIPSecAuditLogs
| where TimeGenerated > ago(7d)
| where _IsBillable == true
| summarize BillableGB = sum(_BilledSize)/1024/1024/1024, Records = count()
        by _ResourceId
| order by BillableGB desc
```

## 4. 削減手順（優先度高 → 低）

### 手順 1 — そもそも収集が必要か（診断設定の棚卸し）

最初に問うべきは「**このログを Log Analytics に取り込む必要があるか**」です[^5][^6]。

- **アクセス制限ルールを設定していないのにこのカテゴリを送っている** → 無意味。診断設定でカテゴリ自体を停止。
- **WAF（Azure Front Door / Application Gateway）側で同等のアクセス制御ログを別途取得している** → 二重。App Service 側は停止 or Storage アーカイブ。
- **構成検証が一段落しており、恒久監視は不要** → 必要時のみ有効化する運用に変更。

監査台帳として保管義務がある場合は、**Log Analytics ではなく Storage アーカイブに送る**ことで低コストに保持できます[^5]。

### 手順 2 — Workspace transformation DCR で行フィルタ

`AppServiceIPSecAuditLogs` は **ingestion-time DCR transformation 対応テーブル**です[^1]。診断設定はカテゴリ内の粒度フィルタができないため、行フィルタは Workspace transformation DCR（取り込み時）で行います[^6][^7][^8]。`Log Analytics workspace > Tables > Create transformation` から構成できます[^8]。

#### 案 A: ヘルス プローブを除外（監査価値ゼロ・最も安全）

```kusto
source
| where isempty(XFDHealthProbe)
```

Front Door 配下では、ヘルス プローブが大量に記録されます。これは構成検証にも監査にも無価値なので、無条件で落として問題ありません[^4]。

#### 案 B: Denied のみ残す（監査の本質に絞る）※要顧客確認

```kusto
source
| where Result == "Denied"
```

`Allowed`（正常アクセス）を落とし、`Denied`（拒否＝不正アクセス試行）だけを残します。監査・セキュリティの関心に絞れますが、「正常アクセスの記録も保持したい」という要件がある場合は実施前に確認が必要です。

#### 案 C: Denied は全件 + Allowed はサンプリング

「正常アクセスも一部は残したい」場合の折衷案です。

```kusto
source
| where Result == "Denied"                 // 拒否は全件保持（監査の本質）
    or hash(CIp, 10) == 0                   // 正常 Allowed は約 10% をサンプリング
```

### 手順 3 — Daily Cap / Commitment Tier（ワークスペース レベル）

固有の手段を尽くした後は、ワークスペース全体の施策に移ります。

- **Daily Cap**: 予期しないスパイクへのセーフティ ネット。コスト削減の主要手段ではない[^6]
- **Commitment Tier**: 削減後に残った取り込み量が 100 GB/day 以上で安定していれば、Pay-as-you-go から移行して単価を下げられる[^9]

> 注: `AppServiceIPSecAuditLogs` は **Basic Logs 非対応**[^1]のため、「Basic Logs に切り替えて単価を下げる」手段は適用できません。

## 5. 推奨実行順序（まとめ表）

| # | アクション | 効果 | リスク |
|---|---|---|---|
| 1 | 現状把握 KQL（手順 3） | — | なし |
| 2 | 診断設定の棚卸し（ルール未設定 / WAF 重複なら停止、監査保管は Storage へ）[^5][^6] | 中〜大 | 構成検証の即時可視性が低下 |
| 3 | transformation 案 A: ヘルス プローブ除外[^4][^8] | 中（Front Door 配下で大） | **ほぼなし**（監査価値ゼロ） |
| 4 | transformation 案 C: Denied 全件 + Allowed サンプリング[^7] | 大 | 正常アクセスの網羅性が下がる |
| 5 | transformation 案 B: Denied のみ残す[^7] | **大** | 正常アクセス記録が消える（要顧客確認） |
| 6 | Commitment Tier に移行[^9] | 中（単価引き下げ） | 31 日コミット |
| — | Basic Logs への切り替え | **不可**（テーブル非対応）[^1] | — |

## 6. transformation のコスト（重要）

transformation を主軸にする場合、コスト構造を押さえておく必要があります[^7]。

| テーブル プラン | Transformation のコスト |
|---|---|
| **Analytics**（`AppServiceIPSecAuditLogs` は Basic 非対応のため通常こちら） | Transformation 自体は通常無料。ただし**取り込みデータ量を 50% を超えて削減した場合、超過分はデータ処理料金として課金**。計算式: `[削減した GB] − ([受信 GB] / 2)` |
| Microsoft Sentinel が有効な場合 | Analytics テーブルへの transformation は**金額がいくら削減されても無料**[^7] |

> `Allowed` やヘルス プローブが大半の環境では削減が容易に 50% を超え、データ処理料金の対象になりやすいです。それでも単価次第で取り込み料金の削減が処理料金を上回ることが多く、効果は出ます。**セキュリティ用途で Sentinel が有効なワークスペースなら、この処理料金は発生しません**[^7]。監査系ログは Sentinel 配下にあることが多いため、この例外が効くケースが多いです。

## 7. 注意点（横断的な制約まとめ）

- **「Audit」だが allow も記録される**: `Result` は Allowed / Denied の両方。監査の本質は `Denied`[^1][^2]。
- **ヘルス プローブは監査価値ゼロ**: `XFDHealthProbe` が立つ Front Door プローブは無条件で落としてよい[^4]。
- **ログレベルの概念がない**: リクエスト 1 件 = 1 行。減らすには行フィルタ（transformation）か収集停止（診断設定）が中心[^1][^2]。
- **診断設定はカテゴリ内の粒度フィルタができない**: Allowed/Denied やプローブの除外は transformation で行う[^6]。
- **Basic Logs 非対応**: 単価を下げる主手段はコミットメント階層[^1][^9]。
- **transformation × Microsoft Sentinel**: Sentinel 有効ワークスペースの Analytics テーブルでは transformation のデータ処理料金は発生しない[^7]。
- **削除前に保管義務を確認**: セキュリティ監査の保持要件がある場合、Denied の長期保持や Storage アーカイブを検討する。

---

[^1]: AppServiceIPSecAuditLogs（テーブル リファレンス: 列定義、Result=Allowed/Denied、XFDHealthProbe、Basic log 非対応、Ingestion-time DCR 対応）, https://learn.microsoft.com/azure/azure-monitor/reference/tables/appserviceipsecauditlogs

[^2]: Azure App Service access restrictions — Diagnostic logging（IPSecurity Audit logs: unmatched rule を除く allow / deny 両方を記録、構成検証に使える）, https://learn.microsoft.com/azure/app-service/overview-access-restrictions

[^3]: Azure App Service monitoring data reference — Resource logs（AppServiceIPSecAuditLogs = Requests from IP Rules）, https://learn.microsoft.com/azure/app-service/monitor-app-service-reference

[^4]: Azure App Service access restrictions — HTTP header filtering（X-FD-HealthProbe: Front Door が `1` を送りヘルス プローブを識別、X-Azure-FDID）, https://learn.microsoft.com/azure/app-service/overview-access-restrictions

[^5]: Enable diagnostic logs for apps in Azure App Service（診断設定で Storage / Event Hubs / Log Analytics へ送信、カテゴリ選択）, https://learn.microsoft.com/azure/app-service/troubleshoot-diagnostic-logs

[^6]: Diagnostic settings in Azure Monitor — Controlling costs（カテゴリ単位のみ選択可、粒度フィルタは transformation）, https://learn.microsoft.com/azure/azure-monitor/platform/diagnostic-settings

[^7]: Transformations in Azure Monitor — Cost for transformations（50% ルール, 計算式, Sentinel 例外）, https://learn.microsoft.com/azure/azure-monitor/data-collection/data-collection-transformations

[^8]: Transformations in Azure Monitor — Workspace transformation DCR, https://learn.microsoft.com/azure/azure-monitor/data-collection/data-collection-transformations

[^9]: Azure Monitor Logs cost calculations and options — Commitment tiers, https://learn.microsoft.com/azure/azure-monitor/logs/cost-logs
