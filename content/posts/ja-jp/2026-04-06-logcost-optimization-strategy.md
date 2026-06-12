Title: Log Analytics ワークスペース ログコスト最適化ご提案
Date: 2026-04-06
Slug: logcost-optimization-strategy
Lang: ja-jp
Category: notebook
Tags: azure, azure-monitor, log-analytics, cost-optimization, finops
Summary: Log Analytics ワークスペースのインジェストコスト最適化に向けた段階的アプローチのご提案。過去支援実績に基づく具体的な打ち手と実行ロードマップの方向性をご相談。

---

**Log Analytics ワークスペース ログコスト最適化ご提案書**

---

## 1. はじめに

本書は、Azure Monitor Log Analytics ワークスペースにおけるログインジェストコストの最適化について、弊社が考える方向性と具体的な打ち手の選択肢をまとめたものです。

昨今、クラウド環境の拡大に伴い、Azure Monitor に収集されるログデータ量は増加傾向にあります。特に、アプリケーションログ（Application Insights）やネットワーク系リソース（Front Door、Application Gateway、Azure Firewall）の診断ログは、インジェスト量全体の大部分を占めるケースが多く、コストの主要因となりやすい領域です。

本提案では、**開発者のトラブルシューティング能力を維持しながら**コストを最適化するという方向性で、段階的なアプローチをご提案させていただきます。貴社環境の状況に合わせて、取捨選択・優先順位付けをご一緒に検討できればと考えております。

## 2. コスト構造の概要

まず、Log Analytics ワークスペースのコスト構造を整理させてください[^1]。

| コスト要素 | 説明 |
| --- | --- |
| **データインジェスト料金** | ワークスペースに取り込まれるデータ量に対する課金。通常、全体コストの大部分を占める |
| **データ保持料金** | デフォルトの無料保持期間（31 日）を超える分に対する課金 |
| **クエリ料金** | Basic Logs / Auxiliary Logs テーブルに対するクエリ実行時の課金 |
| **アラート料金** | ログ検索アラートルールの実行に対する課金 |

過去の支援実績においても、**コストの大半がデータインジェスト料金**であることが確認されています。そのため、まずは「いかにインジェスト量を適正化するか」を軸に検討を進めるのが効果的ではないかと考えております。

## 3. ご提案する最適化の方向性: 4 段階アプローチ

ログコスト最適化にあたり、以下の 4 段階で進めるフレームワークをご提案いたします[^2]。

```
① ログ出力量や頻度を減らす
② 不要なログを収集対象から除外する
③ 保持期間を最適化し、不要な長期保持を見直す
④ 残るデータ量に対して料金プランを最適化する
```

この順序で進めることで、後段の施策（特にコミットメント レベル等）の判断精度が高まると考えています。以下、各段階の打ち手をご説明いたしますので、貴社環境にどの程度フィットするかご確認いただければ幸いです。

### 3.1 第 1 段階：ログ出力量・頻度の削減

最も直接的かつ効果の大きい施策と考えられる領域です。

#### 3.1.1 アプリケーション側のログレベル見直し

本番環境で `Debug` / `Verbose` レベルのログが出力されている場合、`Warning` 以上に限定するという方向性はいかがでしょうか。開発・ステージング環境では引き続き詳細なログを維持することで、開発生産性への影響を最小限に抑えられると考えます。

#### 3.1.2 データ収集ルール（DCR）変換によるインジェスト時フィルタ

**アプリケーション側のコード変更なしに**ログのフィルタリングが可能な手法として、Data Collection Rule（DCR）の KQL 変換機能がございます[^3]。アプリ改修のハードルが高い場合、こちらのアプローチが有効ではないかと考えております。

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

> **補足**: DCR 変換をサポートするテーブルは限定されています。対象テーブル一覧は Microsoft Learn の公式ドキュメントにてご確認ください[^3]。

#### 3.1.3 診断設定の見直し

Azure リソースの診断設定において、現状送信しているログカテゴリの中に不要なものがないか、棚卸しをご一緒にさせていただければと思います[^4]。

### 3.2 第 2 段階：不要なログの収集対象からの除外

#### 3.2.1 診断設定によるストレージアカウントへのオフロード

監査目的のアーカイブや、必要時にのみ分析すればよいログ（アラートでの利用や通常運用でのログ即時検索が不要なログ）については、**Log Analytics への送信を停止し、ストレージアカウントへのアーカイブのみに切り替える**という選択肢がございます。

「このログは本当に Log Analytics 上に必要か？ストレージで十分ではないか？」という観点で、テーブルごとに整理してみてはいかがでしょうか。

#### 3.2.2 テーブル別利用状況の棚卸し

各テーブルについて「誰が・いつ・どの頻度で参照しているか」を整理し、以下のように分類する進め方をご提案します。

| 分類 | 対応方針の候補 |
| --- | --- |
| アラート・ダッシュボードで常時利用 | Analytics（分析）プランを継続 |
| トラブルシューティング時のみ参照 | Basic（基本）プランへの変更を検討 |
| ほぼ参照されていない | 収集停止またはストレージへのオフロードを検討 |

この棚卸しには、運用を担当されている方々へのヒアリングが不可欠と考えております。以下のクエリでインジェスト量の現状を可視化できますので、まずはここからスタートするのが良いかと思います[^5]。

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

デフォルトの 31 日を超えてインタラクティブ保持期間を延長しているテーブルがある場合、本当にその期間が必要かどうかを見直す余地があるかもしれません[^6]。

#### 3.3.2 長期保持（アーカイブ）の活用

コンプライアンス要件等で長期保管が必要なデータについては、Log Analytics の長期保持機能（最大 12 年）をご活用いただけます。アーカイブされたデータは、必要時に Search Job や Restore 機能でアクセス可能ですので、「普段は安く保管し、必要なときだけ取り出す」という運用が可能です[^6]。

#### 3.3.3 Blob Storage へのエクスポート

クエリが不要な長期保管データについては、Blob Storage へのエクスポートが最も安価な選択肢になります。第 2 段階でストレージへオフロードしたテーブルについては、合わせて保持期間の見直しもご検討いただければと思います。

### 3.4 第 4 段階：料金プランの最適化

#### 3.4.1 Basic Logs テーブルプランの適用

トラブルシューティングやインシデント対応用途のテーブルについて、Basic（基本）ログプランへの変更はいかがでしょうか[^7]。

| 項目 | Analytics（分析）プラン | Basic（基本）プラン |
| --- | --- | --- |
| インジェスト単価 | 標準料金 | 大幅に割引 |
| クエリ | 無料・制限なし | 従量課金・単一テーブルのみ |
| アラート | 利用可能 | **利用不可** |
| 保持期間 | 31 日〜2 年 | 30 日固定 |

> **ポイント**: Basic Logs は「ログを削除する」のではなく、「**安価なプランでデータを維持する**」手法です。開発者はトラブルシューティング時に引き続きクエリ可能ですので、「ログを消してしまうのでは」という懸念に対しては、この点をご説明できると考えています。

#### 3.4.2 Summary Rules の活用

ダッシュボードやレポート用途で集計データが必要な場合は、Summary Rules で定期的に集約結果を Analytics テーブルに保存しつつ、元の Raw データは Basic / Auxiliary プランで安価に保持するという構成も選択肢の一つです[^8]。

#### 3.4.3 コミットメント レベルの検討

日次インジェスト量が安定して 100 GB/日以上の場合、コミットメント レベル（予約料金）の適用により最大 30% のコスト削減が見込めます[^9]。

ただし、**第 1〜第 3 段階の施策を先に実施し、その結果を踏まえて判断する**ことを強くお勧めいたします。最適化によりインジェスト量が想定以上に減少した場合、コミットメント レベルが逆にコスト増につながる可能性があるためです。（この点は、後述するケーススタディでも実際に確認されています。）

#### 3.4.4 Daily Cap の設定

予算超過の防止策として、ワークスペースに日次上限（Daily Cap）を設定する選択肢もございます[^1]。ただし、本番ワークロードでは上限到達後にログが収集されなくなりますので、あくまでセーフティネットとしての位置づけが良いかと考えます。

## 4. 過去支援実績に基づくケーススタディ

ここまでの方向性の具体的なイメージとして、過去に実施した Log Analytics ワークスペースのコスト最適化支援（全 4 回セッション）の事例をご紹介いたします。

### 4.1 背景

- 本番環境の Log Analytics ワークスペースコストの大半がデータインジェスト料金であった
- インジェスト量全体の 95% を占める上位 10 テーブルに対して最適化施策を検討した

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

### 4.3 適用した打ち手

テーブルごとの利用状況を運用担当者へヒアリングしたうえで、以下の 4 つの打ち手を組み合わせて適用しました。

**打ち手 ①：ストレージアカウントへのオフロード**

アラートでの利用がない診断ログ（Front Door Access Log、Front Door Health Probe Log、Application Gateway の各種ログ等）について、Log Analytics ワークスペースへの送信を停止し、ストレージアカウントへのアーカイブのみに変更しました。

運用担当者へのヒアリングの結果、「Log Analytics に送信しないログを参照したい場合は、ストレージアカウントの Blob（JSON 形式）を直接参照すればよい」「このユースケース自体が現状の運用でほとんどない」とのご判断をいただき、オフロードを実施した事例です。

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

当該環境では「100 GB/日」のコミットメント レベルが Azure 側で推奨表示されていましたが、以下の理由から Tier 変更は見送りました。

- 直近の実績では 100 GB/日を下回る日が多数存在
- 上記施策の実施により、さらにインジェスト量が減少することが見込まれる

**インジェスト最適化を先に実施し、その後にコミットメント レベルを判断するという順序が重要**であることが、この事例からも確認できています。

### 4.6 この事例から得られた知見

| 知見 | 詳細 |
| --- | --- |
| ステークホルダーの巻き込みが不可欠 | 運用担当者への利用用途ヒアリングが、施策の判断根拠として最も重要であった |
| Azure Arc / Container Insights は個別対応が必要 | DCR 変換の適用可否やサポートチケット（SR）を通じた確認が必要なケースがあった |
| 段階的な実施が効果的 | 全 4 回のセッションに分け、ヒアリング → 分析 → 打ち手提案 → 対応確認のサイクルを回した |
| Application Insights は別途テーマとして扱うのが望ましい | AppTraces / AppRequests は出力量が大きく、サンプリングや DCR 変換の影響範囲も広いため、独立して検討する方が進めやすかった |

## 5. 進め方のご提案

以上を踏まえ、以下のような進め方はいかがでしょうか。

| ステップ | 内容 | 参加いただきたい方 |
| --- | --- | --- |
| **Step 1: 現状分析** | テーブル別インジェスト量・クエリ頻度・保持期間の棚卸し | インフラ担当 |
| **Step 2: 棚卸し会議** | 開発者・運用者を交え、テーブルごとの利用状況と必要性を整理 | 開発者 + 運用者 + インフラ |
| **Step 3: Quick Win 実施** | 効果が見えやすい施策から着手（診断設定の不要カテゴリ停止、ストレージへのオフロード、Basic Logs への変更など） | インフラ担当 |
| **Step 4: DCR 変換導入** | アプリログの SeverityLevel フィルタ、Health check 除外等を DCR で実装 | インフラ担当 + 開発者レビュー |
| **Step 5: アプリ側ログレベル調整** | 本番環境の出力レベルを Warning 以上に変更（開発者チームとの合意後） | 開発者 |
| **Step 6: 保持期間・アーカイブ最適化** | テーブルごとにインタラクティブ保持と長期保持を再設定 | インフラ担当 |
| **Step 7: 料金プラン最適化** | Step 3〜6 の効果を測定したうえで、コミットメント レベルの適用要否を判断 | インフラ + FinOps 担当 |
| **Step 8: 継続モニタリング** | Azure Advisor アラート + Usage テーブルの定期レビューにより最適化状態を維持 | FinOps 担当 |

過去の支援実績では、Step 1〜2 の棚卸しが施策の精度を大きく左右しました。まずはここから着手し、状況を見ながら次のステップに進めるという形が進めやすいのではないかと考えております。

ご不明な点や、貴社環境に即したより具体的な検討をご希望の場合は、お気軽にご相談ください。

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