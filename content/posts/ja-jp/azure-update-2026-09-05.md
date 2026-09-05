Title: Azure Update (2026/08/27 - 2026/09/05)
Date: 2026-09-05
Slug: azure-update-2026-09-05
Lang: ja-jp
Category: notebook
Tags: azure, azure-update, ga, public-preview, azure-virtual-network-manager, azure-site-recovery, azure-container-apps, azure-kubernetes-service, azure-firewall, azure-monitor, azure-copilot, azure-files, azure-vm-image-builder, azure-front-door, web-application-firewall, azure-database-for-mysql, azure-disk-storage, azure-expressroute, virtual-machines
Summary: 2026年8月27日〜9月5日の Azure Update まとめ。Azure Virtual Network Manager IPAM のリージョン拡大や Azure Firewall の SNAT ルート自動学習など計17件。

2026年8月27日〜9月5日に更新された Azure Update のまとめです。

## GA

1. **Azure Virtual Network Manager IPAM in additional Azure regions** — Azure Virtual Network Manager の IPAM 機能が追加リージョンで一般提供開始[^1]。
2. **Azure Site Recovery support for Linux Azure VMs with NVMe disk controllers** — NVMe ディスクコントローラーを使用する Linux Azure VM の Azure Site Recovery サポートが一般提供開始[^2]。
3. **Microsoft Defender for Cloud support for Azure Container Apps (Serverless Containers Posture)** — Azure Container Apps 向け Microsoft Defender for Cloud のサーバーレスコンテナーポスチャ管理が一般提供開始[^3]。
4. **Windows Server 2025 on AKS** — AKS で Windows Server 2025 が一般提供開始[^4]。
5. **Artifact Streaming on AKS** — AKS の Artifact Streaming 機能が一般提供開始[^5]。
6. **Confidential VMs for Azure Linux** — Azure Linux 向け Confidential VM が一般提供開始[^6]。
7. **Purchase order mapping available in Microsoft Marketplace** — Microsoft Marketplace で購入オーダーマッピング機能が一般提供開始[^7]。
8. **Azure Firewall auto-learn SNAT routes** — Azure Firewall の SNAT ルート自動学習機能が一般提供開始[^8]。
9. **Azure Copilot Observability Agent supports Basic and Auxiliary table plans** — Azure Copilot Observability Agent が Basic および Auxiliary テーブルプランに対応し一般提供開始[^9]。
10. **Azure Monitor Auxiliary Logs Plan in Azure Government and China regions** — Azure Monitor Auxiliary Logs Plan が Azure Government および中国リージョンで一般提供開始[^10]。
11. **Azure Monitor Auxiliary Logs Plan support for Azure tables and plan switching** — Azure Monitor Auxiliary Logs Plan が Azure テーブルおよびプラン切り替えに対応し一般提供開始[^11]。
12. **Workload identity support for Azure Files CSI driver (SMB) in Azure** — Azure Files CSI ドライバー (SMB) のワークロード ID サポートが一般提供開始[^12]。
13. **Azure VM Image Builder in sovereign and air-gapped clouds** — Azure VM Image Builder がソブリンクラウドおよびエアギャップクラウドで一般提供開始[^13]。

## Preview

1. **Azure Front Door profile and route level WAF policies** — Azure Front Door のプロファイルおよびルートレベル WAF ポリシーがパブリックプレビュー[^14]。
2. **Reader Endpoint for Azure Database for MySQL** — Azure Database for MySQL のリーダーエンドポイントがパブリックプレビュー[^15]。
3. **Per-disk resiliency for Azure VMs** — Azure VM のディスク単位の回復性がパブリックプレビュー[^16]。
4. **Azure Multicloud Interconnect** — Azure Multicloud Interconnect がパブリックプレビュー[^17]。

[^1]: Generally Available: Azure Virtual Network Manager IPAM in additional Azure regions, https://azure.microsoft.com/updates/v2/Azure-Virtual-Network-Manager-IPAM-in-additional-Azure-regions

[^2]: Generally Available: Azure Site Recovery support for Linux Azure VMs with NVMe disk controllers, https://azure.microsoft.com/updates/v2/Azure-Site-Recovery-support-for-Linux-Azure-VMs-with-NVMe-disk-controllers

[^3]: Generally Available: Microsoft Defender for Cloud support for Azure Container Apps, https://azure.microsoft.com/updates/v2/Microsoft-Defender-for-Cloud-support-for-Azure-Container-Apps-Serverless-Containers-Posture

[^4]: Generally Available: Windows Server 2025 on AKS, https://azure.microsoft.com/updates/v2/Windows-Server-2025-on-AKS

[^5]: Generally Available: Artifact Streaming on AKS, https://azure.microsoft.com/updates/v2/Artifact-Streaming-on-AKS

[^6]: Generally Available: Confidential VMs for Azure Linux, https://azure.microsoft.com/updates/v2/Confidential-VMs-for-Azure-Linux

[^7]: Generally Available: Purchase order mapping available in Microsoft Marketplace, https://azure.microsoft.com/updates/v2/Purchase-order-mapping-available-in-Microsoft-Marketplace

[^8]: Generally Available: Azure Firewall auto-learn SNAT routes, https://azure.microsoft.com/updates/v2/Azure-Firewall-auto-learn-SNAT-routes

[^9]: Generally Available: Azure Copilot Observability Agent supports Basic and Auxiliary table plans, https://azure.microsoft.com/updates/v2/Azure-Copilot-Observability-Agent-supports-Basic-and-Auxiliary-table-plans

[^10]: Generally Available: Azure Monitor Auxiliary Logs Plan in Azure Government and China regions, https://azure.microsoft.com/updates/v2/Azure-Monitor-Auxiliary-Logs-Plan-in-Azure-Government-and-China-regions

[^11]: Generally Available: Azure Monitor Auxiliary Logs Plan support for Azure tables and plan switching, https://azure.microsoft.com/updates/v2/Azure-Monitor-Auxiliary-Logs-Plan-support-for-Azure-tables-and-plan-switching

[^12]: Generally Available: Workload identity support for Azure Files CSI driver (SMB) in Azure, https://azure.microsoft.com/updates/v2/Workload-identity-support-for-Azure-Files-CSI-driver-SMB-in-Azure

[^13]: Generally Available: Azure VM Image Builder in sovereign and air-gapped clouds, https://azure.microsoft.com/updates/v2/Azure-VM-Image-Builder-in-sovereign-and-air-gapped-clouds

[^14]: Public Preview: Azure Front Door profile and route level WAF policies, https://azure.microsoft.com/updates/v2/Azure-Front-Door-profile-and-route-level-WAF-policies

[^15]: Public Preview: Reader Endpoint for Azure Database for MySQL, https://azure.microsoft.com/updates/v2/Reader-Endpoint-for-Azure-Database-for-MySQL

[^16]: Public Preview: Per-disk resiliency for Azure VMs, https://azure.microsoft.com/updates/v2/Per-disk-resiliency-for-Azure-VMs

[^17]: Public Preview: Azure Multicloud Interconnect, https://azure.microsoft.com/updates/v2/Azure-Multicloud-Interconnect
