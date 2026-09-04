Title: Azure Update (2026/08/26 - 2026/09/04)
Date: 2026-09-04
Slug: azure-update-2026-09-04
Lang: ja-jp
Category: notebook
Tags: azure, azure-update, ga, public-preview, azure-virtual-network-manager, azure-site-recovery, azure-front-door, azure-database-for-mysql, azure-container-apps, azure-kubernetes-service, azure-firewall, azure-monitor, azure-copilot, azure-disk-storage, azure-expressroute, azure-files, azure-vm-image-builder, azure-bastion, azure-sre-agent, virtual-machines, web-application-firewall
Summary: 2026年8月26日〜9月4日の Azure Update まとめ。Azure Virtual Network Manager IPAM のリージョン拡大や Azure Site Recovery の NVMe 対応など計23件。

2026年8月26日〜9月4日に更新された Azure Update のまとめです。

## GA (17件)

1. **Azure Virtual Network Manager IPAM が追加リージョンで一般提供開始**[^1] — Azure Virtual Network Manager の IP アドレス管理機能が新たなリージョンで利用可能に。
2. **Azure Site Recovery が NVMe ディスクコントローラー搭載 Linux VM をサポート**[^2] — NVMe ディスクコントローラーを使用する Linux Azure VM の災害復旧に対応。
3. **Microsoft Defender for Cloud が Azure Container Apps をサポート**[^3] — サーバーレスコンテナーのセキュリティポスチャ管理が一般提供開始。
4. **Windows Server 2025 が AKS で一般提供開始**[^4] — Azure Kubernetes Service で Windows Server 2025 ノードプールが利用可能に。
5. **Artifact Streaming が AKS で一般提供開始**[^5] — コンテナーイメージの効率的な配信機能が AKS で正式リリース。
6. **Azure Linux 向け Confidential VM が一般提供開始**[^6] — AKS における Azure Linux ベースの Confidential VM サポート。
7. **Microsoft Marketplace で注文書マッピングが利用可能に**[^7] — マーケットプレイス購入時の注文書マッピング機能が一般提供開始。
8. **Azure Firewall の SNAT ルート自動学習が一般提供開始**[^8] — Azure Firewall が SNAT ルートを自動的に学習する機能。
9. **Azure Copilot Observability Agent が Basic / Auxiliary テーブルプランをサポート**[^9] — Azure Monitor の Basic および Auxiliary テーブルプランに対応。
10. **Azure Monitor Auxiliary Logs Plan が Azure Government / China リージョンで利用可能に**[^10] — ソブリンクラウドでの Auxiliary Logs Plan サポート。
11. **Azure Monitor Auxiliary Logs Plan が Azure テーブルおよびプラン切替をサポート**[^11] — Azure テーブルでの Auxiliary Logs Plan 利用とプラン間の切替が可能に。
12. **Azure Files CSI ドライバー (SMB) でワークロード ID をサポート**[^12] — AKS での Azure Files SMB マウントにワークロード ID 認証が利用可能に。
13. **Azure VM Image Builder がソブリンクラウドおよびエアギャップ環境で利用可能に**[^13] — ソブリンクラウドや分離環境での VM イメージビルドに対応。
14. **Azure Bastion の共有可能リンクに有効期限設定が追加**[^14] — 共有リンクの有効期限を設定してセキュリティを強化。
15. **Azure Bastion 経由で AKS クラスターに接続可能に**[^15] — Azure Bastion を使用した AKS クラスターへのセキュアなアクセス。
16. **Azure SRE Agent VNet Integration が一般提供開始**[^16] — SRE Agent の仮想ネットワーク統合機能。
17. **Azure SRE Agent 30 日間トライアルが一般提供開始**[^17] — SRE Agent の 30 日間無料試用版が利用可能に。

## Public Preview (6件)

1. **Azure Front Door のプロファイルおよびルートレベル WAF ポリシーがプレビュー**[^18] — Azure Front Door でプロファイル・ルート単位の WAF ポリシー設定が可能に。
2. **Azure Database for MySQL の Reader Endpoint がプレビュー**[^19] — MySQL フレキシブルサーバーで読み取り専用エンドポイントが利用可能に。
3. **Azure VM のディスク単位の回復性がプレビュー**[^20] — 個別ディスクレベルでの耐障害性機能。
4. **Azure Multicloud Interconnect がプレビュー**[^21] — Azure ExpressRoute を通じたマルチクラウド接続。
5. **Azure Bastion で IPv6 デュアルスタックがプレビュー**[^22] — Azure Bastion の IPv6 デュアルスタック対応。
6. **Azure SRE Agent の Live Reports がプレビュー**[^23] — SRE Agent のライブレポート機能。

[^1]: Generally Available: Azure Virtual Network Manager IPAM in additional Azure regions, https://azure.microsoft.com/updates/v2/Azure-Virtual-Network-Manager-IPAM-additional-regions
[^2]: Generally Available: Azure Site Recovery support for Linux Azure VMs with NVMe disk controllers, https://azure.microsoft.com/updates/v2/Azure-Site-Recovery-NVMe-Linux
[^3]: Generally Available: Microsoft Defender for Cloud support for Azure Container Apps, https://azure.microsoft.com/updates/v2/Microsoft-Defender-for-Cloud-Container-Apps
[^4]: Generally Available: Windows Server 2025 on AKS, https://azure.microsoft.com/updates/v2/Windows-Server-2025-AKS
[^5]: Generally Available: Artifact Streaming on AKS, https://azure.microsoft.com/updates/v2/Artifact-Streaming-AKS
[^6]: Generally Available: Confidential VMs for Azure Linux, https://azure.microsoft.com/updates/v2/Confidential-VMs-Azure-Linux
[^7]: Generally Available: Purchase order mapping available in Microsoft Marketplace, https://azure.microsoft.com/updates/v2/Purchase-order-mapping-Marketplace
[^8]: Generally Available: Azure Firewall auto-learn SNAT routes, https://azure.microsoft.com/updates/v2/Azure-Firewall-auto-learn-SNAT-routes
[^9]: Generally Available: Azure Copilot Observability Agent supports Basic and Auxiliary table plans, https://azure.microsoft.com/updates/v2/Azure-Copilot-Observability-Agent-Basic-Auxiliary
[^10]: Generally Available: Azure Monitor Auxiliary Logs Plan in Azure Government and China regions, https://azure.microsoft.com/updates/v2/Azure-Monitor-Auxiliary-Logs-Gov-China
[^11]: Generally Available: Azure Monitor Auxiliary Logs Plan support for Azure tables and plan switching, https://azure.microsoft.com/updates/v2/Azure-Monitor-Auxiliary-Logs-tables-switching
[^12]: Generally Available: Workload identity support for Azure Files CSI driver (SMB), https://azure.microsoft.com/updates/v2/Workload-identity-Azure-Files-CSI-SMB
[^13]: Generally Available: Azure VM Image Builder in sovereign and air-gapped clouds, https://azure.microsoft.com/updates/v2/Azure-VM-Image-Builder-sovereign-clouds
[^14]: Generally Available: Azure Bastion shareable link expiration, https://azure.microsoft.com/updates/v2/Azure-Bastion-shareable-link-expiration
[^15]: Generally Available: Connect to AKS clusters using Azure Bastion, https://azure.microsoft.com/updates/v2/Connect-AKS-Azure-Bastion
[^16]: Generally Available: Azure SRE Agent VNet Integration, https://azure.microsoft.com/updates/v2/Azure-SRE-Agent-VNet-Integration
[^17]: Generally Available: Azure SRE Agent 30-Day Trial, https://azure.microsoft.com/updates/v2/Azure-SRE-Agent-30-Day-Trial
[^18]: Public Preview: Azure Front Door profile and route level WAF policies, https://azure.microsoft.com/updates/v2/Azure-Front-Door-WAF-policies
[^19]: Public Preview: Reader Endpoint for Azure Database for MySQL, https://azure.microsoft.com/updates/v2/Reader-Endpoint-Azure-Database-MySQL
[^20]: Public Preview: Per-disk resiliency for Azure VMs, https://azure.microsoft.com/updates/v2/Per-disk-resiliency-Azure-VMs
[^21]: Public Preview: Azure Multicloud Interconnect, https://azure.microsoft.com/updates/v2/Azure-Multicloud-Interconnect
[^22]: Public Preview: IPv6 dual-stack support for Azure Bastion, https://azure.microsoft.com/updates/v2/IPv6-dual-stack-Azure-Bastion
[^23]: Public Preview: Introducing Live Reports for Azure SRE Agent, https://azure.microsoft.com/updates/v2/Azure-SRE-Agent-Live-Reports
