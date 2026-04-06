Title: Log Analytics ワークスペース ログコスト最適化ご提案
Date: 2026-04-06
Slug: logcost-optimization-strategy
Lang: ja-jp
Category: notebook
Tags: azure, azure-monitor, log-analytics, cost-optimization, finops
Summary: Log Analytics ワークスペースのインジェストコスト最適化に向けた段階的アプローチのご提案。過去支援実績に基づく具体的な打ち手と実行ロードマップを提示。

---

**Log Analytics ワークスペース ログコスト最適化ご提案書**

---

## 1. はじめに

本書は、Azure Monitor Log Analytics ワークスペースにおけるログインジェストコストの最適化について、段階的なアプローチと具体的な打ち手をご提案するものです。

昨今、クラウド環境の拡大に伴い、Azure Monitor に収集されるログデータ量は増加傾向にあります。特に、アプリケーションログ（Application Insights）やネットワーク系リソース（Front Door、Application Gateway、Azure Firewall）の診断ログは、インジェスト量全体の大部分を占めるケースが多く、コストの主要因となっています。

本提案では、**開発者のトラブルシューティング能力を維持しながら**、データインジェストコストを最適化する手法を体系的にご説明いたします。

## 2. コスト構造の概要

Log Analytics ワークスペースのコストは、主に以下の要素で構成されます[^1]。

| コスト要素 | 説明 |
| --- | --- |
| **データインジェスト料金** | ワークスペースに取り込まれるデータ量に対する課金。通常、全体コストの大部分を占める |
| **データ保持料金** | デフォルトの無料保持期間（31 日）を超える分に対する課金 |
| **クエリ料金** | Basic Logs / Auxiliary Logs テーブルに対するクエリ実行時の課金 |
| **アラート料金** | ログ検索アラートルールの実行に対する課金 |

過去の支援実績においても、**コストの大半がデータインジェスト料金**であることが確認されています。したがって、最適化の重点は「いかにインジェスト量を適正化するか」に置くことが効果的です。

## 3. 最適化フレームワーク: 4 段階アプローチ

ログコスト最適化は、以下の 4 段階で体系的に進めます[^2]。

```
① ログ出力量や頻度を減らす
② 不要なログを収集対象から除外する
③ 保持期間を最適化し、不要な長期保持を見直す
④ 残るデータ量に対して料金プランを最適化する
```

各段階の詳細を以下にご説明いたします。

### 3.1 第 1 段階：ログ出力量・頻度の削減

最も直接的かつ効果の大きい施策です。

#### 3.1.1 アプリケーション側のログレベル見直し

本番環境では `Warning` 以上のログのみを出力し、`Debug` / `Verbose` レベルのログは開発・ステージング環境に限定することを推奨します。

#### 3.1.2 データ収集ルール（DCR）変換によるインジェスト時フィルタ

Data Collection Rule（DCR）の KQL 変換機能を使用することで、**アプリケーション側のコード変更なしに**、ワークスペースに到達する前の段階で不要なレコードを除外できます[^3]。

**適用例：Warning 以上のトレースのみ保持**

```json
{
  "streams": ["Microsoft-Table-AppTraces"],
  "destinations": ["laDest"],
  "transformKql": "source | where SeverityLevel >= 2"
}
```

**適用例：失敗リクエストまたは遅延リクエストのみ保持**

```json
{
  "streams": ["Microsoft-Table-AppRequests"],
  "destinations": ["laDest"],
  "transformKql": "source | where Success == false or DurationMs >= 1000"
}
```

**適用例：ヘルスチェックエンドポイントの除外**

```json
{
  "streams": ["Microsoft-Table-AppRequests"],
  "destinations": ["laDest"],
  "transformKql": "source | where Name !contains '/health' and Name !contains '/readyz'"
}
```

> **注意事項**: DCR 変換をサポートするテーブルは限定されています。対象テーブル一覧は Microsoft Learn の公式ドキュメントをご確認ください[^3]。

#### 3.1.3 診断設定の見直し

Azure リソースの診断設定において、不要なログカテゴリの送信を停止します[^4]。

### 3.2 第 2 段階：不要なログの収集対象からの除外

#### 3.2.1 診断設定によるストレージアカウントへのオフロード

監査目的のアーカイブや、必要時にのみ分析が必要なログ（アラートでの利用や通常運用でのログ即時検索が不要なログ）は、**Log Analytics ワークスペースへの送信を停止し、ストレージアカウントへのアーカイブのみ**に変更することで、インジェストコストを削減できます。

#### 3.2.2 テーブル別利用状況の棚卸し

各テーブルについて「誰が・いつ・どの頻度で参照するか」を明確にし、以下の観点で分類します。

| 分類 | 対応方針 |
| --- | --- |
| アラート・ダッシュボードで常時利用 | Analytics（分析）プランを継続 |
| トラブルシューティング時のみ参照 | Basic（基本）プランへの変更を検討 |
| ほぼ参照されていない | 収集停止またはストレージへのオフロードを検討 |

**棚卸し用クエリ**[^5]：

```kusto
Usage
| where TimeGenerated > ago(30d)
| where IsBillable == true
| summarize TotalGB = sum(Quantity) / 1000 by DataType
| sort by TotalGB desc
| take 20
```

### 3.3 第 3 段階：保持期間の最適化

#### 3.3.1 インタラクティブ保持期間の見直し

デフォルトの 31 日を超えてインタラクティブ保持期間を延長している場合、テーブルごとに適切な期間を再設定します[^6]。

#### 3.3.2 長期保持（アーカイブ）の活用

コンプライアンス要件等で長期保管が必要なデータについては、Log Analytics の長期保持機能（最大 12 年）を活用します。アーカイブされたデータは、必要時に Search Job や Restore 機能でアクセス可能です[^6]。

#### 3.3.3 Blob Storage へのエクスポート

クエリが不要な長期保管データは、Blob Storage へエクスポートすることで最も安価に保管できます。

### 3.4 第 4 段階：料金プランの最適化

#### 3.4.1 Basic Logs テーブルプランの適用

トラブルシューティングやインシデント対応用途のテーブルは、Basic（基本）ログプランへの変更を検討します[^7]。

| 項目 | Analytics（分析）プラン | Basic（基本）プラン |
| --- | --- | --- |
| インジェスト単価 | 標準料金 | 大幅に割引 |
| クエリ | 無料・制限なし | 従量課金・単一テーブルのみ |
| アラート | 利用可能 | **利用不可** |
| 保持期間 | 31 日〜2 年 | 30 日固定 |

> **ポイント**: Basic Logs は「ログを削除する」のではなく、「**安価なプランでデータを維持する**」手法です。開発者はトラブルシューティング時に引き続きクエリ可能であり、運用品質を損なうことなくコストを削減できます。

#### 3.4.2 Summary Rules の活用

大量のログデータを定期的に集約し、集約結果を Analytics テーブルに保存する仕組みです[^8]。ダッシュボードやレポート用途で必要な集計データは Summary Rules で維持しつつ、元の Raw データは Basic / Auxiliary プランで安価に保持できます。

#### 3.4.3 コミットメント レベルの検討

日次インジェスト量が安定して 100 GB/日以上の場合、コミットメント レベル（予約料金）の適用により最大 30% のコスト削減が見込めます[^9]。

> **注意事項**: インジェスト最適化の施策（第 1〜第 3 段階）を先に実施し、その結果を踏まえてコミットメント レベルの適用要否を判断することを推奨します。最適化によりインジェスト量が減少した場合、コミットメント レベルの効果が薄れる、または超過分が従量課金となる可能性があります。

#### 3.4.4 Daily Cap の設定

予算超過の防止策として、ワークスペースに日次上限（Daily Cap）を設定できます[^1]。ただし、本番ワークロードでは上限到達後にログが収集されなくなるため、慎重な設計が必要です。

## 4. 過去支援実績に基づくケーススタディ

以下は、過去に実施した Log Analytics ワークスペースのコスト最適化支援（全 4 回セッション）の概要です。

### 4.1 背景

- 本番環境の Log Analytics ワークスペースコストの大半がデータインジェスト料金で構成されていた
- インジェスト量全体の 95% を占める上位 10 テーブルに対して最適化施策を検討

### 4.2 分析結果

データインジェスト量の上位テーブルを分析した結果、以下の傾向が確認されました。

| 順位 | テーブル | 主な出力元 | 月間インジェスト量（概算） |
| --- | --- | --- | --- |
| 1 位 | AzureDiagnostics | Front Door、Application Gateway、MySQL | 約 1,070 GB |
| 2 位 | AppTraces | Application Insights | 約 632 GB |
| 3 位 | AppRequests | Application Insights | 約 520 GB |
| 4 位 | Perf | Azure Arc Kubernetes | 約 244 GB |
| 5 位 | ContainerLogV2 | Azure Arc Kubernetes | 約 186 GB |
| 6 位 | ContainerInventory | Azure Arc Kubernetes | 約 186 GB |
| 7 位 | AZFWApplicationRule | Azure Firewall | 約 129 GB |
| 8 位 | ApiManagementGatewayLogs | API Management | 約 113 GB |

### 4.3 実施した打ち手

テーブルごとに以下の 4 つの打ち手を組み合わせて適用しました。

**打ち手 ①：ストレージアカウントへのオフロード**

アラートでの利用がない診断ログ（Front Door Access Log、Front Door Health Probe Log、Application Gateway の各種ログ等）について、Log Analytics ワークスペースへの送信を停止し、ストレージアカウントへのアーカイブのみに変更しました。

**打ち手 ②：DCR 変換によるフィルタリング**

DCR 変換をサポートするテーブルに対して、以下を実施しました。

- テーブル定義から運用上不要な列の削除
- 運用上必須または優先度の高いログのみへのフィルタ・絞り込み
- アラートルールのクエリに合致するログのみにインジェストを限定

**打ち手 ③：サンプリング機能の適用**

Application Insights からの出力（AppTraces、AppRequests 等）について、サンプリング設定の適用を検討しました。

**打ち手 ④：Basic Logs プランの適用**

Container Insights 関連テーブル（ContainerLogV2 等）について、Basic Logs プランへの変更によるインジェストコスト削減を適用しました。

### 4.4 成果

| 環境 | 削減見込み |
| --- | --- |
| 本番環境 | 月間約 500K 円程度（約 4 割削減） |
| 検証環境 | 月間約 100K 円程度（約 2〜3 割削減） |

### 4.5 コミットメント レベルに関する判断

当該環境では「100 GB/日」のコミットメント レベルが推奨されていましたが、以下の理由から Tier 変更は見送りました。

- 直近の実績では 100 GB/日を下回る日が多数存在
- 上記施策の実施により、さらにインジェスト量が減少することが見込まれる

このように、**コミットメント レベルの検討はインジェスト最適化の施策後に行うことが重要**です。

### 4.6 得られた知見

| 知見 | 詳細 |
| --- | --- |
| ステークホルダーの巻き込みが不可欠 | 運用部隊への診断設定ログの利用用途ヒアリングが施策判断の根拠となった |
| Azure Arc / Container Insights は個別対応が必要 | DCR 変換の適用可否やサポートチケット（SR）を通じた確認が必要なケースがあった |
| 段階的な実施が効果的 | 全 4 回のセッションに分け、ヒアリング → 分析 → 打ち手提案 → 対応確認のサイクルを回した |
| Application Insights は別途検討が望ましい | AppTraces / AppRequests は出力量が大きく、サンプリングや DCR 変換の影響範囲も広いため、独立したテーマとして扱うことを推奨 |

## 5. 推奨実行ロードマップ

本提案の実施にあたり、以下のロードマップを推奨いたします。

| ステップ | 内容 | 参加者 |
| --- | --- | --- |
| **Step 1: 現状分析** | テーブル別インジェスト量・クエリ頻度・保持期間の棚卸し | インフラ担当 |
| **Step 2: 棚卸し会議** | 開発者・運用者を招集し、テーブルごとの利用状況と必要性を判定 | 開発者 + 運用者 + インフラ |
| **Step 3: Quick Win 実施** | 診断設定の不要カテゴリ停止、ストレージへのオフロード、Basic Logs への変更 | インフラ担当 |
| **Step 4: DCR 変換導入** | アプリログの SeverityLevel フィルタ、Health check 除外等を DCR で実装 | インフラ担当 + 開発者レビュー |
| **Step 5: アプリ側ログレベル調整** | 本番環境の出力レベルを Warning 以上に変更 | 開発者 |
| **Step 6: 保持期間・アーカイブ最適化** | テーブルごとにインタラクティブ保持と長期保持を再設定 | インフラ担当 |
| **Step 7: 料金プラン最適化** | コミットメント レベルの検討（Step 3〜6 の効果測定後） | インフラ + FinOps 担当 |
| **Step 8: 継続モニタリング** | Azure Advisor アラート + Usage テーブルの定期レビュー | FinOps 担当 |

## 6. 参考情報

[^1]: "Cost optimization in Azure Monitor", https://learn.microsoft.com/azure/azure-monitor/fundamentals/best-practices-cost

[^2]: "Architecture best practices for Log Analytics - Cost Optimization", https://learn.microsoft.com/azure/well-architected/service-guides/azure-log-analytics#cost-optimization

[^3]: "Transformations in Azure Monitor", https://learn.microsoft.com/azure/azure-monitor/data-collection/data-collection-transformations

[^4]: "Diagnostic settings in Azure Monitor", https://learn.microsoft.com/azure/azure-monitor/essentials/diagnostic-settings#controlling-costs

[^5]: "Understand and mitigate high data consumption in Log Analytics", https://learn.microsoft.com/troubleshoot/azure/azure-monitor/log-analytics/configure-and-manage-log-analytics-tables/understand-and-mitigate-high-data-consumption-log-analytics

[^6]: "Best practices for Azure Monitor Logs - Data retention and archiving", https://learn.microsoft.com/azure/azure-monitor/logs/best-practices-logs#cost-optimization

[^7]: "Select a table plan based on data usage in a Log Analytics workspace", https://learn.microsoft.com/azure/azure-monitor/logs/logs-table-plans

[^8]: "Aggregate data in a Log Analytics workspace by using summary rules", https://learn.microsoft.com/azure/azure-monitor/logs/summary-rules

[^9]: "Azure Monitor Logs cost calculations and options - Commitment tiers", https://learn.microsoft.com/azure/azure-monitor/logs/cost-logs#commitment-tiers