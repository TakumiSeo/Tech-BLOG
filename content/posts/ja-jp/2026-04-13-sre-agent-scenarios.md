Title: Azure SRE Agent シナリオ集（Reader / Monitoring Reader / Log Analytics Reader 前提）
Date: 2026-04-13
Modified: 2026-04-14
Slug: sre-agent-scenarios
Lang: ja-jp
Category: notebook
Tags: azure, sre-agent, application-gateway, azure-firewall, observability, network, security, compliance
Summary: sre-agent-poc-runbook の検証環境に合わせて、疑似障害の調査は Anthropic 系、定期ヘルスチェックやセキュリティチェックは GPT 系に寄せる運用方針を整理。変更操作は人手で runbook に沿って実施し、SRE Agent は委任された権限の範囲で切り分けと要約に専念させる。
Status: draft

本稿は [sre-agent-poc-runbook]({filename}sre-agent-poc-runbook.md) に対応する **SRE Agent 観点のシナリオ定義** です。ここでは、Azure SRE Agent に変更権限を持たせず、**Reader / Monitoring Reader / Log Analytics Reader** の 3 ロールを前提に、どこまで調査を自動化できるかを整理します。加えて、**疑似障害の調査は Anthropic 系、Scheduled Task やセキュリティチェックのような定型・高頻度タスクは GPT 系** に寄せる運用方針を明示します。[^1][^2][^3][^7][^8]

## Optional: SRE Agent に入れておくナレッジ例

環境説明を大量に入れなくても、最初に 1 枚の overview 相当ドキュメントがあると、SRE Agent の初動がかなり安定します。以下は、**この PoC が実際に稼働している前提** で SRE Agent に与える日本語ナレッジの例です。必要に応じて sre-general-poc-overview.md として Knowledge base に入れる想定です。[^10]

```text
この環境は Azure SRE Agent の検証用 PoC です。目的は、Application Gateway 系と Azure Firewall 系の疑似障害に対して、SRE Agent が委任された権限の範囲で一次切り分けできることを確認することです。

主な構成は次のとおりです。
- Resource Group: rg-sre-general-poc
- VNet: vnet-sre-general-poc (10.10.0.0/20)
- Azure Firewall: azfw-sre-general-poc
- Application Gateway: appgw-sre-general-poc
- AppVM: appvm-sgpoc
- ClientVM: clientvm-sgpoc
- Private DNS zone: sre-general-poc.internal
- Log Analytics workspace: law-sre-general-poc

この PoC では、次の通信経路を検証対象とします。
- Client -> Firewall -> Application Gateway -> Firewall -> IIS
- AppVM -> Firewall -> Internet

SRE Agent の役割は調査と要約に限定します。SRE Agent は変更操作を行いません。
各シナリオの実行は原則としてチャットを分け、1 つのチャットで 1 つの調査または 1 回の定期チェックだけを扱います。
- 許可される操作: 委任された権限の範囲でのリソース構成参照、Azure Monitor / Log Analytics の参照、ログ検索、状態要約
- 許可しない操作: Azure Firewall Policy の変更、NSG 変更、Application Gateway 設定変更、Private DNS レコード変更、VM Run Command、IIS 再起動、VM 再起動

この環境で重視する観測ポイントは次のとおりです。
- Application Gateway backend health
- AppGW 診断ログ
- Azure Firewall の AzureDiagnostics ログ
- Private DNS の A レコード
- Azure Monitor のメトリクスとアラート

Azure Firewall のログは AzureDiagnostics テーブルで確認し、メッセージ本体は主に msg_s を参照します。
Application Gateway の backend health は Healthy / Unhealthy / Unknown を確認します。

この PoC における代表的な障害シナリオは次のとおりです。
- AppGW backend Unhealthy
- Client 側 DNS 解決失敗
- AppGW backend FQDN 解決失敗
- AppVM 外向き通信障害
- 日次ヘルスチェック
- 週次セキュリティチェック
- 定期 compliance / 構成健全性チェック

モデル使い分け方針は次のとおりです。
- 疑似障害の調査、根本原因分析、ログ相関分析は Anthropic 系を優先
- 日次ヘルスチェック、週次セキュリティチェック、定期 compliance チェックは GPT 系を優先

SRE Agent が結論を返すときは、推測ではなく証拠ベースで要約し、証拠不足の場合は要追加確認として不足項目を明示します。
```

## モデル使い分け方針

この PoC では、その公式整理に合わせて次の運用ルールを採用します。

- 疑似障害の切り分け、根本原因調査、ログ相関分析は **Anthropic 系 agent** に寄せる
- 日次ヘルスチェック、週次セキュリティチェック、定期 compliance チェックは **GPT 系 agent** に寄せる
- provider は agent 単位で設定されるため、用途を明確に分けたい場合は **調査用 agent と Scheduled Task 用 agent を分離** する[^7][^8][^9]

| 用途 | 推奨 provider | 理由 |
| --- | --- | --- |
| 疑似障害の調査、根本原因分析 | Anthropic | 推論寄りで、複雑な調査を少ない推論ステップで進めやすい |
| 日次ヘルスチェック | Azure OpenAI (GPT) | 定型的な表形式サマリーや高速なツール実行と相性がよい |
| 週次セキュリティチェック | Azure OpenAI (GPT) | 高頻度で繰り返すチェックをコスト効率よく回しやすい |
| 定期 compliance チェック | Azure OpenAI (GPT) | Scheduled Task として定常運用に載せやすい |

## 基本方針
この PoC では、SRE Agent の役割を次の 2 点に限定します。
- 監視シグナル、構成情報、ログを読んで、障害箇所を絞り込む
- 実施すべき runbook の手順を人間に提示する
- 各シナリオ実行は原則として新しいチャットで開始し、前の調査文脈を持ち越さない
逆に、SRE Agent 自身には次の操作をさせません。
- Azure Firewall Policy、NSG、Application Gateway、Private DNS の変更
- VM の Run Command 実行
- IIS 再起動や VM 再起動
- DNS レコードの追加・削除
この分離により、SRE Agent は **委任された参照権限ベースの診断エージェント** として扱えます。Reader は全リソースの参照、Monitoring Reader はメトリクス・アラート・ログ検索、Log Analytics Reader はワークスペース内の監視データ検索に使います。[^1][^2][^3]
## 想定環境
| 項目 | 値 |
| --- | --- |
| Resource Group | `rg-sre-general-poc` |
| VNet | `vnet-sre-general-poc` (`10.10.0.0/20`) |
| Client subnet | `Subnet-client-001` (`10.10.0.0/25`) |
| AzureFirewallSubnet | `10.10.1.0/26` |
| AppGW subnet | `Subnet-appgw-001` (`10.10.2.0/26`) |
| VM subnet | `Subnet-vm-001` (`10.10.3.0/25`) |
| Azure Firewall | `azfw-sre-general-poc` |
| Application Gateway | `appgw-sre-general-poc` |
| AppGW private frontend | `10.10.2.10` |
| AppVM | `appvm-sgpoc` |
| ClientVM | `clientvm-sgpoc` |
| Private DNS zone | `sre-general-poc.internal` |
| AppGW FQDN | `appgw.sre-general-poc.internal` |
| App backend FQDN | `appvm.sre-general-poc.internal` |
| Log Analytics | `law-sre-general-poc` |
## 付与ロール
| ロール | 推奨スコープ | 用途 |
| --- | --- | --- |
| Reader | `rg-sre-general-poc` | AppGW、Firewall、NSG、UDR、Private DNS、VM リソース構成の参照 |
| Monitoring Reader | `rg-sre-general-poc` | Azure Monitor のメトリクス、アラート、診断設定、Logs 参照 |
| Log Analytics Reader | `law-sre-general-poc` | Log Analytics での KQL 実行 |

## プロンプト設計の基本
以下のプロンプト例は、**Agent instructions** に入れる日本語例です。Scheduled Task の時刻や頻度は別欄で設定し、ここでは **何を調べて、何を返すか** だけを簡潔かつ具体的に指示します。Azure SRE Agent の公式ドキュメントでは、Scheduled Task の指示は **concise and specific** に書くこと、セキュリティ関連では **compliance frameworks** を活用すること、曖昧なスケジュールを避けることが推奨されています。あわせて Microsoft の prompt guidance に沿って、**期待する出力形式** と **判断不能時の返し方** を明示します。[^9][^10][^11]
このため、以下の例では次を統一しています。
- 対象リソース名を明記する
- 読み取り専用であることを明記する
- 返してほしい出力形式を指定する
- 証拠が不足する場合は推測せず、追加確認項目を返させる
## 対応シナリオ
### シナリオ 1: AppGW バックエンド Unhealthy 切り分け
**対応する runbook**: シナリオ A / B / C / D
**トリガー**:
- Azure Monitor アラートで backend unhealthy を検知
- または手動で `show-backend-health` 実行結果が `Unhealthy` / `Unknown`
**SRE Agent が見るもの**:
- Application Gateway の backend health API / CLI 出力[^4]
- AppGW の診断ログ
- Azure Firewall の `AzureDiagnostics` ログ
- NSG、UDR、HTTP settings、probe 設定の構成情報
- 必要に応じて権限委任により AppGW 配下リソースの関連構成を追加確認
**SRE Agent が返すべき要約**:
- incident の概要
- 観測事実
- backend health の状態
- 影響を受けている backend
- 最有力原因候補と根拠
- 証拠不足または否定寄りの仮説
- runbook の対応シナリオ / 手順
- 要追加確認
**Response Plan 設定の要点**:
- Incident platform: `Azure Monitor`。Azure Monitor は既定の incident platform で、追加設定なしで接続されます。[^14][^15]
- Severity: `Sev1`
- Title contains: `alert-appgw-unhealthy-hosts` または `UnhealthyHostCount`
- Agent autonomy level: まず `Review`
- 同じ alert rule の再発報は同一 thread にマージされる前提で扱う[^14]
**推奨 provider**: `Anthropic`
**理由**: アラート受信後は backend health、ログ、構成を横断して仮説を絞る incident investigation であり、定型レポートより調査型ワークロードに寄ります。[^8][^12][^13][^14][^16]
**プロンプト例**:
```text
受信した Azure Monitor incident を調査してください。
まず alert details から、alert rule 名、対象リソース、発火時刻、評価期間、signal 名を確認してください。
対象が appgw-sre-general-poc の UnhealthyHostCount に関する incident であれば、読み取り専用で Application Gateway backend health、AppGW 診断ログ、Azure Firewall の AzureDiagnostics、Private DNS、NSG、UDR、probe、HTTP settings を確認してください。
日本語で次の形式で返してください。
- incident の概要
- 観測事実
- backend health の状態
- 影響を受けている backend
- 最有力原因候補を最大 3 件
- 各候補の根拠
- 証拠不足または否定寄りの仮説
- runbook の対応シナリオ / 手順
- 要追加確認
推測で断定しないでください。対象が想定外のアラートであれば、その旨を明記してください。
```
## 現時点で未対応のシナリオ
### VM 高負荷調査
**未対応理由**:
- 現行 runbook では VM の guest OS 内プロセス情報を Log Analytics に送っていない
- SRE Agent に VM Run Command 権限を与えない前提のため、OS 内で `top` / `Get-Process` のような追加採取ができない
- そのため、CPU 高負荷の **根因プロセス特定** までを読み取り専用で完結できない
**対応するなら必要な追加実装**:
- VM Insights / AMA / Perf ログの収集
- もしくは SRE Agent に別権限を与えて Run Command を許可
- もしくは別の運用フローとして、SRE Agent は高負荷アラートの通知と関連メトリクス要約だけを担当する
このため、**VM 高負荷は本稿の対象外** とし、現時点では `sre-agent-poc-runbook.md` に沿ったネットワーク / AppGW / Firewall 系シナリオに集中します。
## シナリオ対応マトリクス
| シナリオ | runbook 対応 | 推奨 provider | SRE Agent の役割 | 変更操作 |
| --- | --- | --- | --- | --- |
| 1. AppGW backend Unhealthy | A / B / C / D | Anthropic | backend health、ログ、構成の相関確認 | なし |
| 2. Client DNS 解決失敗 | E | Anthropic | DNS レコードと AppGW 健全性の切り分け | なし |
| 3. backend FQDN 解決失敗 | F | Anthropic | `Unknown` と DNS レコードの相関確認 | なし |
| 4. AppVM 外向き通信障害 | G | Anthropic | Firewall ログと Rule 名の特定 | なし |
| 5. 日次ヘルスチェック | H | Azure OpenAI (GPT) | 状態集約と通知 | なし |
| 6. 週次セキュリティチェック | 間接対応 | Azure OpenAI (GPT) | 構成レビューと逸脱候補の整理 | なし |
| 7. 定期 compliance / 構成健全性チェック | 間接対応 | Azure OpenAI (GPT) | 差分表と定期レポート生成 | なし |
| 8. AppGW unhealthy incident trigger | I | Anthropic | Azure Monitor alert 起点の自動調査 | なし |
| 9. VM 高負荷 | 対象外 | - | 未実装 | - |
## 運用上の使い分け
- 疑似障害の自動調査と要約は **Anthropic 系** に寄せる
- Scheduled Task やセキュリティ / compliance チェックは **GPT 系** に寄せる
- Azure Monitor alert を起点にした incident-triggered の自動調査は **Azure Monitor + Incident Response Plan** で起動する
- 復旧操作は **人間が runbook に沿って実施** する
- 変更権限が必要な操作は別の運用主体に分離する
この形にしておくと、SRE Agent の誤操作リスクを増やさずに、障害の一次切り分けだけを安定して自動化できます。さらに、定型チェックは GPT 系 agent に寄せることで、日常運用の回転数とコスト効率を両立しやすくなります。[^8]
[^1]: "Azure built-in roles for General - Reader", https://learn.microsoft.com/azure/role-based-access-control/built-in-roles/general
[^2]: "Roles, permissions, and security in Azure Monitor - Monitoring Reader", https://learn.microsoft.com/azure/azure-monitor/fundamentals/roles-permissions-security
[^3]: "Manage access to Log Analytics workspaces - Azure RBAC", https://learn.microsoft.com/azure/azure-monitor/logs/manage-access#azure-rbac
[^4]: "Application Gateway - Backend health", https://learn.microsoft.com/azure/application-gateway/application-gateway-backend-health
[^5]: "Monitor Azure Firewall - Legacy Azure Diagnostics logs", https://learn.microsoft.com/azure/firewall/monitor-firewall#legacy-azure-diagnostics-logs
[^6]: "Use Azure Firewall workbooks", https://learn.microsoft.com/azure/firewall/firewall-workbook
[^7]: "Model provider selection in Azure SRE Agent", https://learn.microsoft.com/azure/sre-agent/model-provider-selection
[^8]: "Pricing and billing for Azure SRE Agent", https://learn.microsoft.com/azure/sre-agent/pricing-billing#frequently-asked-questions
[^9]: "Scheduled tasks in Azure SRE Agent", https://learn.microsoft.com/azure/sre-agent/scheduled-tasks
[^10]: "Workflow automation in Azure SRE Agent", https://learn.microsoft.com/azure/sre-agent/workflow-automation#best-practices
[^11]: "Use prompts to make your agent or agent flow perform specific tasks", https://learn.microsoft.com/microsoft-copilot-studio/nlu-prompt-node#best-practices-for-prompt-instructions
[^12]: "Monitor Azure Application Gateway", https://learn.microsoft.com/azure/application-gateway/monitor-application-gateway#alerts
[^13]: "Supported metrics for Microsoft.Network/applicationgateways", https://learn.microsoft.com/azure/azure-monitor/reference/supported-metrics/microsoft-network-applicationgateways-metrics
[^14]: "Azure Monitor alerts", https://learn.microsoft.com/azure/sre-agent/azure-monitor-alerts
[^15]: "Step 4: Set up incident response in Azure SRE Agent", https://learn.microsoft.com/azure/sre-agent/tutorial-incident-response
[^16]: "Tutorial: Create an incident response plan for Azure SRE Agent", https://learn.microsoft.com/azure/sre-agent/response-plan
