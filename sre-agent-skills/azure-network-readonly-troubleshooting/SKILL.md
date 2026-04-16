---
name: azure-network-readonly-troubleshooting
description: Use when investigating Azure network or connectivity symptoms with read-only or delegated read permissions, especially Application Gateway backend unhealthy or unknown, HTTP 502, timeout, Private DNS resolution issues, Azure Firewall allow deny analysis, backend reachability checks, and cross-resource network triage without assuming the cause in advance.
tools:
  - RunAzCliReadCommands
  - microsoft-learn-docs-mcp_microsoft_code_sample_search
  - microsoft-learn-docs-mcp_microsoft_docs_fetch
  - microsoft-learn-docs-mcp_microsoft_docs_search
---

# Azure Network Read-Only Troubleshooting

この skill は、Azure のネットワーク障害や到達性異常を、委任された参照権限の範囲で一次切り分けするための再利用可能な手順です。
Application Gateway、Azure Firewall、Private DNS、NSG、UDR、Log Analytics、Azure Monitor をまたぐ確認を対象にします。

## Use This Skill When

- Application Gateway の backend health が Unhealthy または Unknown である
- HTTP 502、timeout、backend 到達性低下、名前解決失敗などの症状が出ている
- Azure Firewall の Allow / Deny や該当ルールを確認したい
- Private DNS、NSG、UDR を含めて経路を横断的に確認したい
- 読み取り専用または委任された権限で、変更を加えずに切り分けたい

## Operating Rules

1. 既知の疑似障害や runbook の想定シナリオを最初から正解として扱わない。実環境では何が起きているか未確定である前提で進める。
2. runbook や knowledge base は環境固有の事実確認に使うが、そこに書かれた障害パターンは候補例であって答えではない。
3. 観測事実、推定、未確認事項を明確に分ける。根拠のない断定はしない。
4. 変更操作は行わない。実行するのは参照、確認、比較だけに限定する。
5. Microsoft Learn は製品仕様、ログ形式、SKU 差分、probe 条件、制約事項の確認が必要な場合だけ使う。
6. 証拠が不足する場合は、結論を狭めすぎず、追加確認項目として明示する。

## Investigation Procedure

1. まず症状を整理する。何が失敗しているのかを、HTTP status、backend health、DNS、timeout、Deny、名前解決、到達性に分解する。
2. 影響範囲を確定する。単一 backend か、経路全体か、名前解決だけか、送信元限定かを切り分ける。
3. Application Gateway の backend health、HTTP settings、probe 条件を確認し、観測事実を列挙する。
4. Azure Firewall のログで送信元、宛先、ポート、Allow / Deny、該当ルール、時間相関を確認する。
5. Private DNS、NSG、UDR、関連構成を確認し、症状と整合する候補だけを残す。
6. 仮説を 2 から 3 件に絞る。各仮説に対して、どの観測事実が支持し、どの情報がまだ不足しているかを整理する。
7. 可能であれば仮説を反証する。たとえば Firewall Deny がないなら Firewall 起因説を弱める、DNS 解決が正常なら DNS 起因説を弱める。
8. Microsoft Learn で製品仕様を確認する必要がある場合だけ、観測結果と仕様を照合する。
9. 既知の runbook シナリオと一致する場合でも、「一致する可能性が高い」と表現し、観測事実を根拠として示す。
10. 結論は output-template.md の形式で返す。

## Heuristics

- backend health が Unhealthy でも、原因を即断しない。backend 応答異常、probe mismatch、途中遮断のどれが説明力を持つかを比較する。
- backend health が Unknown で backend が FQDN の場合、DNS 解決失敗は有力候補だが、名前解決以外の制御面要因も残る。
- Azure Firewall に明確な Deny があり、時刻と送信元宛先が症状と一致する場合、その仮説の優先度を上げる。
- Application Gateway v2 では PerformanceLog 前提で説明せず、backend health、metrics、診断ログを優先して扱う。
- 証拠が複数の層にまたがる場合は、単一原因と決めつけず、最も説明力の高い候補を順序付きで返す。

## Output Requirements

- 観測事実を先に示す
- 影響範囲を明示する
- 原因候補は最大 3 件までに絞る
- 各候補に根拠と不足証拠を付ける
- 弱くなった仮説や否定寄りの仮説も必要に応じて示す
- 次の read-only 確認項目と、人手で実施すべき対応を分けて書く