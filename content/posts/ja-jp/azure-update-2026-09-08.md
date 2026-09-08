Title: Azure Update (2026/08/30 - 2026/09/08)
Date: 2026-09-08
Slug: azure-update-2026-09-08
Lang: ja-jp
Category: notebook
Tags: azure, azure-update, ga, public-preview, azure-virtual-network-manager, azure-site-recovery, azure-container-apps, azure-kubernetes-service, azure-firewall, azure-monitor, azure-copilot, azure-front-door, web-application-firewall, azure-database-for-mysql, azure-disk-storage, azure-expressroute, virtual-machines
Summary: 2026年8月30日〜9月8日の Azure Update まとめ。Azure Virtual Network Manager IPAM のリージョン拡大や Azure Firewall の SNAT ルート自動学習など計15件。

2026年8月30日〜9月8日に更新された Azure Update のまとめです。

## GA

1. **Azure Virtual Network Manager IPAM が追加リージョンで利用可能に** — Azure Virtual Network Manager の IP アドレス管理 (IPAM) 機能が新たなリージョンで一般提供開始[^1]。
2. **Azure Site Recovery が NVMe ディスクコントローラー搭載 Linux VM をサポート** — NVMe ディスクコントローラーを使用する Linux Azure VM のディザスターリカバリーが一般提供[^2]。
3. **Microsoft Defender for Cloud が Azure Container Apps をサポート** — サーバーレスコンテナーのセキュリティポスチャ管理が一般提供開始[^3]。
4. **Windows Server 2025 が AKS で利用可能に** — Azure Kubernetes Service で Windows Server 2025 ノードが一般提供[^4]。
5. **Artifact Streaming が AKS で一般提供** — AKS でのコンテナーイメージの高速プルを実現する Artifact Streaming が一般提供開始[^5]。
6. **Azure Linux 向け Confidential VM が一般提供** — Azure Linux を使用した Confidential VM が一般提供開始[^6]。
7. **Microsoft Marketplace で発注書マッピングが利用可能に** — Marketplace の購入に発注書 (PO) をマッピングする機能が一般提供[^7]。
8. **Azure Firewall が SNAT ルートを自動学習** — Azure Firewall で SNAT ルートの自動学習機能が一般提供開始[^8]。
9. **Azure Copilot Observability Agent が Basic / Auxiliary テーブルプランをサポート** — Azure Copilot の Observability Agent が Basic および Auxiliary テーブルプランに対応[^9]。
10. **Azure Monitor Auxiliary Logs Plan が Azure Government / China リージョンで利用可能に** — Auxiliary Logs Plan のサポートが政府クラウドおよび中国リージョンに拡大[^10]。
11. **Azure Monitor Auxiliary Logs Plan が Azure テーブルとプラン切り替えをサポート** — Auxiliary Logs Plan で Azure テーブルのサポートおよびプラン切り替え機能が一般提供[^11]。

## Public Preview

1. **Azure Front Door でプロファイル・ルートレベルの WAF ポリシーが利用可能に** — Azure Front Door でプロファイルおよびルートレベルで Web Application Firewall ポリシーを適用可能に[^12]。
2. **Azure Database for MySQL で Reader Endpoint がプレビュー** — Azure Database for MySQL で読み取りワークロード向けの Reader Endpoint がパブリックプレビュー開始[^13]。
3. **Azure VM のディスク単位の回復性がプレビュー** — 仮想マシンのディスクごとに回復性を構成する機能がパブリックプレビュー[^14]。
4. **Azure Multicloud Interconnect がプレビュー** — Azure ExpressRoute を活用したマルチクラウド接続サービスがパブリックプレビュー開始[^15]。

---

[^1]: Generally Available: Azure Virtual Network Manager IPAM in additional Azure regions, https://azure.microsoft.com/updates/v2/azure-virtual-network-manager-ipam-additional-regions

[^2]: Generally Available: Azure Site Recovery support for Linux Azure VMs with NVMe disk controllers, https://azure.microsoft.com/updates/v2/Azure-Site-Recovery-support-for-Linux-Azure-VMs-with-NVMe-disk-controllers

[^3]: Generally Available: Microsoft Defender for Cloud support for Azure Container Apps, https://azure.microsoft.com/updates/v2/Microsoft-Defender-for-Cloud-support-for-Azure-Container-Apps-Serverless-Containers-Posture

[^4]: Generally Available: Windows Server 2025 on AKS, https://azure.microsoft.com/updates/v2/Generally-Available-Windows-Server-2025-on-AKS

[^5]: Generally Available: Artifact Streaming on AKS, https://azure.microsoft.com/updates/v2/Generally-Available-Artifact-Streaming-on-AKS

[^6]: Generally Available: Confidential VMs for Azure Linux, https://azure.microsoft.com/updates/v2/Generally-Available-Confidential-VMs-for-Azure-Linux

[^7]: Generally Available: Purchase order mapping available in Microsoft Marketplace, https://azure.microsoft.com/updates/v2/Purchase-order-mapping-available-in-Microsoft-Marketplace

[^8]: Generally Available: Azure Firewall auto-learn SNAT routes, https://azure.microsoft.com/updates/v2/azure-firewall-auto-learn-snat-routes

[^9]: Generally Available: Azure Copilot Observability Agent supports Basic and Auxiliary table plans, https://azure.microsoft.com/updates/v2/Azure-Copilot-Observability-Agent-supports-Basic-and-Auxiliary-table-plans

[^10]: Generally Available: Azure Monitor Auxiliary Logs Plan in Azure Government and China regions, https://azure.microsoft.com/updates/v2/azure-monitor-auxiliary-logs-plan-government-china-regions

[^11]: Generally Available: Azure Monitor Auxiliary Logs Plan support for Azure tables and plan switching, https://azure.microsoft.com/updates/v2/azure-monitor-auxiliary-logs-plan-support-for-azure-tables-and-plan-switching

[^12]: Public Preview: Azure Front Door profile and route level WAF policies, https://azure.microsoft.com/updates/v2/Azure-Front-Door-profile-and-route-level-WAF-policies

[^13]: Public Preview: Reader Endpoint for Azure Database for MySQL, https://azure.microsoft.com/updates/v2/Reader-Endpoint-for-Azure-Database-for-MySQL

[^14]: Public Preview: Per-disk resiliency for Azure VMs, https://azure.microsoft.com/updates/v2/Per-disk-resiliency-for-Azure-VMs

[^15]: Public Preview: Azure Multicloud Interconnect, https://azure.microsoft.com/updates/v2/Azure-Multicloud-Interconnect
