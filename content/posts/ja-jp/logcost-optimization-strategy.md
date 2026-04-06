Title: Log Analytics ログコスト最適化 — 提案戦略と打ち手
Date: 2026-04-06
Slug: logcost-optimization-strategy
Lang: ja-jp
Category: notebook
Tags: azure, azure-monitor, log-analytics, cost-optimization, finops
Summary: Log Analytics のアプリケーションログコスト肥大化に対し、開発者のトラブルシューティング能力を維持しながらコストを最適化する戦略と打ち手の提案。

## 背景と課題

アプリケーションの Log Analytics ワークスペースにおいて、開発者がデバッグ用のログ（Verbose / Debug レベル）を含むすべてのログを収集しているため、インジェスト量が肥大化しコストが増大している。一方、この収集方針は開発者のトラブルシューティングを容易にするという意図があり、単純なログ削減は運用品質に影響する可能性がある。

## 提案の進め方

### Phase 0: 現状把握（提案前の準備）

顧客に提案する前に、以下のデータを取得して定量的な根拠を作る。

**テーブル別インジェスト量の可視化**[^1]

```kusto
Usage
| where TimeGenerated > ago(30d)
| where IsBillable == true
| summarize TotalGB = sum(Quantity) / 1000 by DataType
| sort by TotalGB desc
| take 20
```

**Advisor のコスト推奨事項の確認**

Log Analytics ワークスペースの「概要 > 推奨事項」または「Advisor recommendations」から、Basic Logs への変更提案やコミットメント レベルの変更提案が出ていないか確認する[^2]。

### Phase 1: ステークホルダーの巻き込み

| 観点 | 顧客への説明 |
| --- | --- |
| 目的 | 「ログを減らす」ではなく「必要なログを適切なコストで保持する」 |
| 招集すべき人 | ログを出力しているアプリの **開発者**、日常的にログを参照する **運用者**、コストを管理する **インフラ/FinOps 担当** |
| 議論のゴール | テーブルごとに「誰が・いつ・どの頻度で参照するか」を明確にし、テーブルプランと保持期間を決定する |
| 合意形成のポイント | 開発者のトラブルシューティング能力を維持しつつコストを下げる打ち手があることを示す（Basic Logs, DCR Transformation 等） |

### Phase 2: 4 段階の最適化戦略

添付のスライド画像にもある通り、最適化の大枠は以下の 4 段階で進める[^3]。

#### ① ログ出力量や頻度を減らす

| 打ち手 | 内容 | 効果 |
| --- | --- | --- |
| アプリ側のログレベル見直し | 本番環境では `Warning` 以上のみ出力し、`Debug` / `Verbose` は開発・ステージング環境に限定する | インジェスト量の削減（最も直接的） |
| DCR Transformation（インジェスト時フィルタ） | Data Collection Rule (DCR) の KQL 変換で、ワークスペースに到達する前に不要レコードを除外する[^4] | アプリ側の変更なしにフィルタ可能 |
| Diagnostic Settings の見直し | Azure リソースの診断設定で、不要なログカテゴリの送信を停止する[^5] | リソースログの無駄な収集を排除 |

**DCR Transformation の例**: Warning 以上のトレースのみ保持[^6]

```json
{
  "streams": ["Microsoft-Table-AppTraces"],
  "destinations": ["laDest"],
  "transformKql": "source | where SeverityLevel >= 2"
}
```

**DCR Transformation の例**: 失敗または遅延リクエストのみ保持[^6]

```json
{
  "streams": ["Microsoft-Table-AppRequests"],
  "destinations": ["laDest"],
  "transformKql": "source | where Success == false or DurationMs >= 1000"
}
```

#### ② 不要なログを収集対象から除外

| 打ち手 | 内容 | 効果 |
| --- | --- | --- |
| テーブル別の利用状況棚卸し | 各テーブルを「誰が・いつ・どの頻度で参照するか」で分類する | 除外判断の根拠を作る |
| Health check エンドポイントの除外 | `/health`, `/readyz`, `/livez` 等のリクエストを DCR で除外する[^6] | ノイズの多い定型リクエストを排除 |
| 未使用テーブルの特定・停止 | 過去 30 日間クエリされていないテーブルのデータ収集を停止する | 完全に不要なデータの排除 |

#### ③ 保持期間の最適化とアーカイブ

| 打ち手 | 内容 | 効果 |
| --- | --- | --- |
| インタラクティブ保持期間の短縮 | デフォルト 31 日を超える保持はコストがかかるため、テーブルごとに適切な期間を設定する[^7] | 不要な長期保持コストの削減 |
| 長期保持（アーカイブ）の活用 | 最大 12 年まで低コストで保持可能。必要時に Search Job や Restore でアクセスする[^7] | コンプライアンス要件を満たしつつコスト削減 |
| Blob Storage へのエクスポート | 長期保管が必要だがクエリ不要なデータは Blob にエクスポートし、Log Analytics の保持期間を短くする[^3] | 最も安価な長期保管 |

#### ④ 残るデータ量に対する料金最適化

| 打ち手 | 内容 | 効果 |
| --- | --- | --- |
| Basic Logs テーブルプランの適用 | デバッグ・トラブルシューティング・監査用テーブルを Basic Logs に変更する。インジェスト単価が大幅に低下し、クエリ時に GB 単位で課金される[^8] | **開発者のトラブルシューティング能力を維持しつつインジェストコストを削減** |
| Summary Rules の活用 | 大量のログデータを定期的に集約し、集約結果を Analytics テーブルに保存する。元データは Basic / Auxiliary プランで安価に保持する[^9] | ダッシュボード・レポート用途を維持しつつ raw データのコストを削減 |
| コミットメント レベルの検討 | 日次インジェストが 100 GB/日 以上であれば、従量課金より最大 30% 安いコミットメント レベルを適用する[^10] | 大容量環境での単価削減 |
| Daily Cap の設定 | 予算超過の防止策として日次上限を設定する（本番ワークロードでは慎重に）[^2] | 予期しないコスト急増の防止 |

### Phase 3: 実行ロードマップ（提案例）

| ステップ | 期間目安 | 内容 | 必要なロール |
| --- | --- | --- | --- |
| 1. 現状分析 | 1 週間 | テーブル別インジェスト量・クエリ頻度・保持期間の棚卸し | インフラ担当 |
| 2. 棚卸し会議 | 半日 | 開発者・運用者を招集し、テーブルごとの必要性を判定 | 開発者 + 運用者 + インフラ |
| 3. Quick Win 実施 | 1〜2 週間 | Diagnostic Settings の不要カテゴリ停止、Basic Logs への変更、コミットメント レベル変更 | インフラ担当 |
| 4. DCR Transformation 導入 | 2〜3 週間 | アプリログの SeverityLevel フィルタ、Health check 除外等を DCR で実装 | インフラ担当 + 開発者レビュー |
| 5. アプリ側ログレベル調整 | スプリント単位 | 本番環境の出力レベルを Warning 以上に変更（開発者チームの合意後） | 開発者 |
| 6. 保持期間・アーカイブ最適化 | 1 週間 | テーブルごとにインタラクティブ保持と長期保持を再設定 | インフラ担当 |
| 7. 継続モニタリング | 継続 | Azure Advisor アラート + Usage テーブルの定期レビュー | FinOps 担当 |

### 顧客への提案時のポイント

| 観点 | 説明 |
| --- | --- |
| 開発者の懸念への対処 | 「ログを消す」のではなく「**Basic Logs / Summary Rules により安くトラブルシューティング用データを維持する**」と伝える |
| 段階的アプローチ | いきなり全テーブルを変更せず、Quick Win（Diagnostic Settings 整理・コミットメント レベル）から着手し、効果を可視化する |
| 定量的根拠 | 「テーブル X は月 Y GB インジェストされているが、過去 30 日間のクエリ回数は Z 回」という事実で判断を促す |
| 責任分界 | インフラ側で DCR Transformation を実装すれば、アプリ側の変更なしにフィルタできることを強調する |

## 参考リソース

[^1]: "Understand and mitigate high data consumption in Log Analytics", https://learn.microsoft.com/troubleshoot/azure/azure-monitor/log-analytics/configure-and-manage-log-analytics-tables/understand-and-mitigate-high-data-consumption-log-analytics

[^2]: "Cost optimization in Azure Monitor", https://learn.microsoft.com/azure/azure-monitor/fundamentals/best-practices-cost

[^3]: "Architecture best practices for Log Analytics - Cost Optimization", https://learn.microsoft.com/azure/well-architected/service-guides/azure-log-analytics#cost-optimization

[^4]: "Transformations in Azure Monitor", https://learn.microsoft.com/azure/azure-monitor/data-collection/data-collection-transformations

[^5]: "Diagnostic settings in Azure Monitor", https://learn.microsoft.com/azure/azure-monitor/essentials/diagnostic-settings#controlling-costs

[^6]: "Filter Azure Monitor OpenTelemetry - ingestion-time DCR samples", https://learn.microsoft.com/azure/azure-monitor/app/opentelemetry-filter#filter-telemetry-at-ingestion-using-data-collection-rules

[^7]: "Best practices for Azure Monitor Logs - Data retention and archiving", https://learn.microsoft.com/azure/azure-monitor/logs/best-practices-logs#cost-optimization

[^8]: "Select a table plan based on data usage in a Log Analytics workspace", https://learn.microsoft.com/azure/azure-monitor/logs/logs-table-plans

[^9]: "Aggregate data in a Log Analytics workspace by using summary rules", https://learn.microsoft.com/azure/azure-monitor/logs/summary-rules

[^10]: "Azure Monitor Logs cost calculations and options - Commitment tiers", https://learn.microsoft.com/azure/azure-monitor/logs/cost-logs#commitment-tiers
