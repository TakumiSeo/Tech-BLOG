Title: Azure Update (2026/08/29 - 2026/09/07)
Date: 2026-09-07
Slug: azure-update-2026-09-07
Lang: ja-jp
Category: notebook
Tags: azure, azure-update, ga, public-preview, azure-virtual-network-manager, azure-site-recovery, azure-container-apps, azure-kubernetes-service, azure-firewall, azure-monitor, azure-copilot, azure-front-door, web-application-firewall, azure-database-for-mysql, azure-disk-storage, azure-expressroute, virtual-machines
Summary: 2026年8月29日〜9月7日の Azure Update まとめ。Azure Virtual Network Manager IPAM のリージョン拡大や Azure Firewall の SNAT ルート自動学習など計15件。

2026年8月29日〜9月7日に更新された Azure Update のまとめです。

## GA

1. **Azure Virtual Network Manager IPAM が追加リージョンで一般提供開始**
   Azure Virtual Network Manager の IP アドレス管理 (IPAM) 機能が、追加の Azure リージョンで利用可能になりました[^1]。

2. **Azure Site Recovery が NVMe ディスクコントローラーを搭載した Linux Azure VM をサポート**
   NVMe ディスクコントローラーを使用する Linux Azure VM に対する Azure Site Recovery のサポートが一般提供開始されました[^2]。

3. **Microsoft Defender for Cloud が Azure Container Apps をサポート（サーバーレスコンテナーポスチャー）**
   Microsoft Defender for Cloud のサーバーレスコンテナーポスチャー機能が Azure Container Apps に対応しました[^3]。

4. **Windows Server 2025 が AKS で一般提供開始**
   Azure Kubernetes Service (AKS) で Windows Server 2025 ノードプールが利用可能になりました[^4]。

5. **Artifact Streaming が AKS で一般提供開始**
   AKS における Artifact Streaming 機能が一般提供開始され、コンテナーイメージの取得が高速化されます[^5]。

6. **Confidential VMs for Azure Linux が一般提供開始**
   Azure Linux 向けの Confidential VM が一般提供開始されました[^6]。

7. **Microsoft Marketplace で発注書マッピングが利用可能に**
   Microsoft Marketplace の購入時に発注書のマッピングが可能になりました[^7]。

8. **Azure Firewall の SNAT ルート自動学習が一般提供開始**
   Azure Firewall が SNAT ルートを自動的に学習する機能が一般提供開始されました[^8]。

9. **Azure Copilot Observability Agent が Basic および Auxiliary テーブルプランをサポート**
   Azure Copilot Observability Agent が Basic および Auxiliary テーブルプランに対応しました[^9]。

10. **Azure Monitor Auxiliary Logs Plan が Azure Government および China リージョンで一般提供開始**
    Azure Monitor の Auxiliary Logs Plan が Azure Government および中国リージョンで利用可能になりました[^10]。

11. **Azure Monitor Auxiliary Logs Plan が Azure テーブルおよびプラン切り替えをサポート**
    Azure Monitor の Auxiliary Logs Plan で Azure テーブルのサポートおよびプラン切り替え機能が一般提供開始されました[^11]。

## Public Preview

1. **Azure Front Door のプロファイルおよびルートレベル WAF ポリシー**
   Azure Front Door でプロファイルおよびルートレベルの Web Application Firewall (WAF) ポリシーがパブリックプレビューとして利用可能になりました[^12]。

2. **Azure Database for MySQL の Reader Endpoint**
   Azure Database for MySQL で Reader Endpoint がパブリックプレビューとして提供開始されました[^13]。

3. **Azure VM のディスクごとの回復性**
   Azure VM でディスクごとの回復性機能がパブリックプレビューとして利用可能になりました[^14]。

4. **Azure Multicloud Interconnect**
   Azure ExpressRoute を活用した Azure Multicloud Interconnect がパブリックプレビューとして提供開始されました[^15]。

[^1]: Generally Available: Azure Virtual Network Manager IPAM in additional Azure regions, https://azure.microsoft.com/updates/v2/Azure-Virtual-Network-Manager-IPAM-in-additional-Azure-regions
[^2]: Generally Available: Azure Site Recovery support for Linux Azure VMs with NVMe disk controllers, https://azure.microsoft.com/updates/v2/Azure-Site-Recovery-support-for-Linux-VMs-NVMe
[^3]: Generally Available: Microsoft Defender for Cloud support for Azure Container Apps, https://azure.microsoft.com/updates/v2/Defender-for-Cloud-Container-Apps-Serverless-Posture
[^4]: Generally Available: Windows Server 2025 on AKS, https://azure.microsoft.com/updates/v2/Windows-Server-2025-on-AKS
[^5]: Generally Available: Artifact Streaming on AKS, https://azure.microsoft.com/updates/v2/Artifact-Streaming-on-AKS
[^6]: Generally Available: Confidential VMs for Azure Linux, https://azure.microsoft.com/updates/v2/Confidential-VMs-Azure-Linux
[^7]: Generally Available: Purchase order mapping available in Microsoft Marketplace, https://azure.microsoft.com/updates/v2/Purchase-order-mapping-Microsoft-Marketplace
[^8]: Generally Available: Azure Firewall auto-learn SNAT routes, https://azure.microsoft.com/updates/v2/Azure-Firewall-auto-learn-SNAT-routes
[^9]: Generally Available: Azure Copilot Observability Agent supports Basic and Auxiliary table plans, https://azure.microsoft.com/updates/v2/Copilot-Observability-Agent-Basic-Auxiliary
[^10]: Generally Available: Azure Monitor Auxiliary Logs Plan in Azure Government and China regions, https://azure.microsoft.com/updates/v2/Azure-Monitor-Auxiliary-Logs-Gov-China
[^11]: Generally Available: Azure Monitor Auxiliary Logs Plan support for Azure tables and plan switching, https://azure.microsoft.com/updates/v2/Azure-Monitor-Auxiliary-Logs-tables-switching
[^12]: Public Preview: Azure Front Door profile and route level WAF policies, https://azure.microsoft.com/updates/v2/Azure-Front-Door-WAF-policies
[^13]: Public Preview: Reader Endpoint for Azure Database for MySQL, https://azure.microsoft.com/updates/v2/Reader-Endpoint-Azure-Database-MySQL
[^14]: Public Preview: Per-disk resiliency for Azure VMs, https://azure.microsoft.com/updates/v2/Per-disk-resiliency-Azure-VMs
[^15]: Public Preview: Azure Multicloud Interconnect, https://azure.microsoft.com/updates/v2/Azure-Multicloud-Interconnect
