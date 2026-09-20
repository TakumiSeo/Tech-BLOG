Title: Azure Update (2026/09/11 - 2026/09/20)
Date: 2026-09-20
Slug: azure-update-2026-09-20
Lang: ja-jp
Category: notebook
Tags: azure, azure-update, ga, public-preview, retirement, announcement, microsoft-foundry, azure-database-for-postgresql, azure-virtual-network-manager, virtual-machines, azure-payments-hsm, azure-sql-database, azure-red-hat-openshift, application-gateway, azure-storage-mover, azure-virtual-desktop
Summary: 2026年9月11日〜9月20日の Azure Update まとめ。GA 6件、パブリックプレビュー 9件、リタイア 2件、その他 1件の計18件。

2026年9月11日〜9月20日における Azure Update のまとめです。

## GA

1. **Enable and disable controls for Microsoft Foundry agents in Agent 365** — Microsoft Foundry エージェントの有効化・無効化制御が一般提供開始[^1]。
2. **Publishing Microsoft Foundry agents to Microsoft 365 Copilot and Teams** — Microsoft Foundry エージェントを Microsoft 365 Copilot および Teams に公開する機能が GA[^2]。
3. **Logical replication slot sync status metric for Azure PostgreSQL Flexible Server** — Azure Database for PostgreSQL Flexible Server の論理レプリケーションスロット同期ステータスメトリックが GA[^3]。
4. **New and improved troubleshooting guides for Azure Database for PostgreSQL** — Azure Database for PostgreSQL のトラブルシューティングガイドが刷新・改善され GA[^4]。
5. **PG18 support for Azure Database for PostgreSQL elastic clusters** — Azure Database for PostgreSQL エラスティッククラスターで PG18 がサポート開始[^5]。
6. **High-scale mesh in Azure Virtual Network Manager** — Azure Virtual Network Manager のハイスケールメッシュが一般提供開始[^6]。

## パブリックプレビュー

1. **Foundry Routines in Foundry Agent Service** — Foundry Agent Service で Foundry Routines がパブリックプレビュー[^7]。
2. **Mdsv4 and Msv4 Series Virtual Machines for SAP** — SAP 向け Mdsv4 および Msv4 シリーズ仮想マシンがパブリックプレビュー[^8]。
3. **Network egress controls for hosted agents in Microsoft Foundry** — Microsoft Foundry のホステッドエージェント向けネットワークエグレス制御がパブリックプレビュー[^9]。
4. **Azure Payments HSM v2** — Azure Payments HSM v2 がパブリックプレビュー[^10]。
5. **Azure SQL updates for mid-September 2026** — 2026年9月中旬の Azure SQL Database アップデートがパブリックプレビュー[^11]。
6. **Azure Red Hat OpenShift with hosted control planes** — ホステッドコントロールプレーン対応の Azure Red Hat OpenShift がパブリックプレビュー[^12]。
7. **PostgreSQL skills and MCP plugin for Azure Database for PostgreSQL** — Azure Database for PostgreSQL 向け PostgreSQL スキルおよび MCP プラグインがパブリックプレビュー[^13]。
8. **HTTP/3 over QUIC support in Azure Application Gateway** — Azure Application Gateway で HTTP/3 over QUIC がパブリックプレビュー[^14]。
9. **Agentless migration of on-premises SMB file shares to Azure Files (SMB)** — オンプレミス SMB ファイル共有の Azure Files (SMB) へのエージェントレス移行がパブリックプレビュー[^15]。

## リタイア

1. **SAP container images removed October 14, 2026** — SAP コンテナーイメージが 2026年10月14日に削除予定[^16]。
2. **Azure Linux with OS Guard in Azure Kubernetes Service** — Azure Kubernetes Service における Azure Linux with OS Guard がリタイア[^17]。

## その他

1. **New Windows App client-side endpoints for Azure Virtual Desktop** — Azure Virtual Desktop 向け Windows App クライアントサイドエンドポイントの更新が発表[^18]。

[^1]: Generally Available: Enable and disable controls for Microsoft Foundry agents in Agent 365, https://azure.microsoft.com/updates/v2/enable-disable-foundry-agents-agent-365

[^2]: Generally Available: Publishing Microsoft Foundry agents to Microsoft 365 Copilot and Teams, https://azure.microsoft.com/updates/v2/publish-foundry-agents-m365-copilot-teams

[^3]: Generally Available: Logical replication slot sync status metric for Azure PostgreSQL Flexible Server, https://azure.microsoft.com/updates/v2/logical-replication-slot-sync-status-metric-postgres

[^4]: Generally Available: New and improved troubleshooting guides for Azure Database for PostgreSQL, https://azure.microsoft.com/updates/v2/new-troubleshooting-guides-postgresql

[^5]: Generally Available: PG18 support for Azure Database for PostgreSQL elastic clusters, https://azure.microsoft.com/updates/v2/pg18-postgresql-elastic-clusters

[^6]: Generally Available: High-scale mesh in Azure Virtual Network Manager, https://azure.microsoft.com/updates/v2/high-scale-mesh-avnm

[^7]: Public Preview: Foundry Routines in Foundry Agent Service, https://azure.microsoft.com/updates/v2/foundry-routines-agent-service

[^8]: Public Preview: Mdsv4 and Msv4 Series Virtual Machines for SAP, https://azure.microsoft.com/updates/v2/mdsv4-msv4-vms-sap

[^9]: Public Preview: Network egress controls for hosted agents in Microsoft Foundry, https://azure.microsoft.com/updates/v2/network-egress-foundry-hosted-agents

[^10]: Public Preview: Azure Payments HSM v2, https://azure.microsoft.com/updates/v2/azure-payments-hsm-v2

[^11]: Public Preview: Azure SQL updates for mid-September 2026, https://azure.microsoft.com/updates/v2/azure-sql-mid-september-2026

[^12]: Public Preview: Azure Red Hat OpenShift with hosted control planes, https://azure.microsoft.com/updates/v2/aro-hosted-control-planes

[^13]: Public Preview: PostgreSQL skills and MCP plugin for Azure Database for PostgreSQL, https://azure.microsoft.com/updates/v2/postgresql-skills-mcp-plugin

[^14]: Public Preview: HTTP/3 over QUIC support in Azure Application Gateway, https://azure.microsoft.com/updates/v2/http3-quic-application-gateway

[^15]: Public Preview: Agentless migration of on-premises SMB file shares to Azure Files (SMB), https://azure.microsoft.com/updates/v2/agentless-smb-migration-azure-files

[^16]: Retirement Update: SAP container images removed October 14, 2026, https://azure.microsoft.com/updates/v2/sap-container-images-removed

[^17]: Retirement: Azure Linux with OS Guard in Azure Kubernetes Service, https://azure.microsoft.com/updates/v2/azure-linux-os-guard-aks

[^18]: Announcing: New Windows App client-side endpoints for Azure Virtual Desktop, https://azure.microsoft.com/updates/v2/windows-app-endpoints-avd
