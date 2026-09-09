Title: Azure Update (2026/08/31 - 2026/09/09)
Date: 2026-09-09
Slug: azure-update-2026-09-09
Lang: ja-jp
Category: notebook
Tags: azure, azure-update, ga, public-preview, private-preview, azure-load-testing, azure-developer-cli, azure-virtual-network-manager, azure-site-recovery, azure-front-door, web-application-firewall, azure-database-for-mysql, azure-container-apps, azure-kubernetes-service, azure-firewall, azure-monitor, azure-copilot, azure-disk-storage, azure-expressroute, virtual-machines, azure-functions
Summary: 2026年8月31日〜9月9日の Azure Update まとめ。Playwright Workspaces のリージョン拡大や Azure Developer CLI 拡張フレームワークの GA など計17件。

2026年8月31日〜9月9日に発表された Azure Update のまとめです。

## GA

1. **Playwright Workspaces が Australia East、Japan East、Switzerland North で利用可能に** — Azure Load Testing の Playwright Workspaces が3つの新リージョンで一般提供開始[^1]。
2. **Azure Developer CLI (azd) Extension Framework が一般提供開始** — azd の拡張フレームワークが GA。Azure Container Apps、Azure Functions、Blob Storage など複数サービスとの統合を強化[^2]。
3. **Azure Virtual Network Manager IPAM のリージョン拡大** — Azure Virtual Network Manager の IP アドレス管理 (IPAM) 機能が追加リージョンで一般提供開始[^3]。
4. **Azure Site Recovery が NVMe ディスクコントローラーを搭載した Linux Azure VM をサポート** — NVMe ディスクコントローラーを使用する Linux VM の災害復旧が一般提供開始[^4]。
5. **Microsoft Defender for Cloud が Azure Container Apps をサポート** — サーバーレスコンテナーのセキュリティポスチャ管理が一般提供開始[^5]。
6. **Windows Server 2025 が AKS で一般提供開始** — Azure Kubernetes Service で Windows Server 2025 ノードが利用可能に[^6]。
7. **Artifact Streaming が AKS で一般提供開始** — コンテナーイメージの遅延読み込みによりポッド起動時間を短縮[^7]。
8. **Confidential VMs for Azure Linux が一般提供開始** — Azure Linux 上の機密仮想マシンが AKS で利用可能に[^8]。
9. **Microsoft Marketplace で購入オーダーマッピングが利用可能に** — Marketplace の購入に対して注文書番号のマッピングが可能に[^9]。
10. **Azure Firewall の SNAT ルート自動学習が一般提供開始** — Azure Firewall が SNAT ルートを自動学習し、ネットワーク構成の管理を簡素化[^10]。
11. **Azure Copilot Observability Agent が Basic および Auxiliary テーブルプランをサポート** — Azure Monitor の Copilot Observability Agent が Basic・Auxiliary テーブルプランに対応[^11]。
12. **Azure Monitor Auxiliary Logs Plan が Azure Government および China リージョンで利用可能に** — Auxiliary Logs Plan が政府およびソブリンクラウドリージョンに拡大[^12]。
13. **Azure Monitor Auxiliary Logs Plan が Azure テーブルおよびプラン切り替えをサポート** — Azure テーブルの Auxiliary Logs Plan への移行とプラン間切り替えが一般提供開始[^13]。

## Public Preview

14. **Azure Front Door のプロファイルおよびルートレベル WAF ポリシー** — Azure Front Door でプロファイル単位およびルート単位で WAF ポリシーを設定可能に[^14]。
15. **Azure VM のディスク単位レジリエンシー** — 仮想マシンのディスクごとに復元性を設定するパブリックプレビュー[^15]。
16. **Azure Multicloud Interconnect** — Azure ExpressRoute を活用したマルチクラウド接続のパブリックプレビュー[^16]。

## Private Preview

17. **Azure Database for MySQL の Reader Endpoint** — Azure Database for MySQL でリーダーエンドポイントのプライベートプレビューが開始[^17]。

[^1]: Generally Available: Playwright Workspaces in Australia East, Japan East, and Switzerland North, https://azure.microsoft.com/updates/v2/Playwright-Workspaces-in-Australia-East-Japan-East-and-Switzerland-North
[^2]: Generally Available: Azure Developer CLI (azd) Extension Framework, https://azure.microsoft.com/updates/v2/Azure-Developer-CLI-azd-Extension-Framework
[^3]: Generally Available: Azure Virtual Network Manager IPAM in additional Azure regions, https://azure.microsoft.com/updates/v2/Azure-Virtual-Network-Manager-IPAM-in-additional-Azure-regions
[^4]: Generally Available: Azure Site Recovery support for Linux Azure VMs with NVMe disk controllers., https://azure.microsoft.com/updates/v2/Azure-Site-Recovery-support-for-Linux-Azure-VMs-with-NVMe-disk-controllers
[^5]: Generally Available: Microsoft Defender for Cloud support for Azure Container Apps (Serverless Containers Posture), https://azure.microsoft.com/updates/v2/Microsoft-Defender-for-Cloud-support-for-Azure-Container-Apps-Serverless-Containers-Posture
[^6]: Generally Available: Windows Server 2025 on AKS, https://azure.microsoft.com/updates/v2/Windows-Server-2025-on-AKS
[^7]: Generally Available: Artifact Streaming on AKS, https://azure.microsoft.com/updates/v2/Artifact-Streaming-on-AKS
[^8]: Generally Available: Confidential VMs for Azure Linux, https://azure.microsoft.com/updates/v2/Confidential-VMs-for-Azure-Linux
[^9]: Generally Available: Purchase order mapping available in Microsoft Marketplace, https://azure.microsoft.com/updates/v2/Purchase-order-mapping-available-in-Microsoft-Marketplace
[^10]: Generally Available: Azure Firewall auto-learn SNAT routes, https://azure.microsoft.com/updates/v2/Azure-Firewall-auto-learn-SNAT-routes
[^11]: Generally Available: Azure Copilot Observability Agent supports Basic and Auxiliary table plans, https://azure.microsoft.com/updates/v2/Azure-Copilot-Observability-Agent-supports-Basic-and-Auxiliary-table-plans
[^12]: Generally Available: Azure Monitor Auxiliary Logs Plan in Azure Government and China regions, https://azure.microsoft.com/updates/v2/Azure-Monitor-Auxiliary-Logs-Plan-in-Azure-Government-and-China-regions
[^13]: Generally Available: Azure Monitor Auxiliary Logs Plan support for Azure tables and plan switching, https://azure.microsoft.com/updates/v2/Azure-Monitor-Auxiliary-Logs-Plan-support-for-Azure-tables-and-plan-switching
[^14]: Public Preview: Azure Front Door profile and route level WAF policies, https://azure.microsoft.com/updates/v2/Azure-Front-Door-profile-and-route-level-WAF-policies
[^15]: Public Preview: Per-disk resiliency for Azure VMs, https://azure.microsoft.com/updates/v2/Per-disk-resiliency-for-Azure-VMs
[^16]: Public Preview: Azure Multicloud Interconnect, https://azure.microsoft.com/updates/v2/Azure-Multicloud-Interconnect
[^17]: Private Preview: Reader Endpoint for Azure Database for MySQL, https://azure.microsoft.com/updates/v2/Reader-Endpoint-for-Azure-Database-for-MySQL
