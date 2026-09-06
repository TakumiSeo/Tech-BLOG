Title: Azure Update (2026/08/28 - 2026/09/06)
Date: 2026-09-06
Slug: azure-update-2026-09-06
Lang: ja-jp
Category: notebook
Tags: azure, azure-update, ga, public-preview, azure-virtual-network-manager, azure-site-recovery, azure-container-apps, azure-kubernetes-service, azure-firewall, azure-monitor, azure-copilot, azure-files, azure-vm-image-builder, azure-front-door, web-application-firewall, azure-database-for-mysql, azure-disk-storage, azure-expressroute, virtual-machines
Summary: 2026年8月28日〜9月6日の Azure Update まとめ。Azure Virtual Network Manager IPAM のリージョン拡大や Azure Firewall の SNAT ルート自動学習など計17件。

Azure Update についてまとめる（2026/08/28 - 2026/09/06）。

## GA

1. **Azure Virtual Network Manager IPAM が追加リージョンで一般提供開始**  
   Azure Virtual Network Manager の IP アドレス管理（IPAM）機能が新たなリージョンで利用可能に[^1]。

2. **Azure Site Recovery が NVMe ディスクコントローラー搭載 Linux VM をサポート**  
   NVMe ディスクコントローラーを使用する Linux Azure VM の災害復旧が Azure Site Recovery でサポート開始[^2]。

3. **Microsoft Defender for Cloud が Azure Container Apps をサポート（サーバーレスコンテナーポスチャ）**  
   Azure Container Apps に対するセキュリティポスチャ管理が Microsoft Defender for Cloud で一般提供[^3]。

4. **Windows Server 2025 が AKS で一般提供開始**  
   Azure Kubernetes Service（AKS）で Windows Server 2025 ノードプールが利用可能に[^4]。

5. **Artifact Streaming が AKS で一般提供開始**  
   コンテナーイメージの遅延読み込みにより AKS ワークロードの起動時間を短縮する Artifact Streaming が GA[^5]。

6. **Azure Linux 向け Confidential VM が一般提供開始**  
   Azure Linux OS で Confidential VM がサポートされ、機密コンピューティングの選択肢が拡大[^6]。

7. **Microsoft Marketplace で発注書マッピングが利用可能に**  
   Marketplace の購入時に発注書（PO）番号のマッピングが可能に[^7]。

8. **Azure Firewall の SNAT ルート自動学習が一般提供開始**  
   Azure Firewall が SNAT ルートを自動的に学習し、ネットワーク構成の簡素化を実現[^8]。

9. **Azure Copilot Observability Agent が Basic / Auxiliary テーブルプランをサポート**  
   Copilot Observability Agent が Basic および Auxiliary ログテーブルプランに対応[^9]。

10. **Azure Monitor Auxiliary Logs Plan が Azure Government / China リージョンで一般提供**  
    Auxiliary Logs Plan が政府系およびソブリンクラウドリージョンで利用可能に[^10]。

11. **Azure Monitor Auxiliary Logs Plan が Azure テーブルおよびプラン切り替えをサポート**  
    既存テーブルの Auxiliary プランへの切り替えとネイティブ Azure テーブルのサポートが追加[^11]。

12. **Azure Files CSI ドライバー（SMB）でワークロード ID がサポート**  
    AKS 上の Azure Files CSI ドライバー（SMB）でワークロード ID 認証が一般提供[^12]。

13. **Azure VM Image Builder がソブリンおよびエアギャップクラウドで一般提供**  
    VM Image Builder がソブリンクラウドおよびエアギャップ環境で利用可能に[^13]。

## Preview

1. **Azure Front Door のプロファイルおよびルートレベル WAF ポリシー**  
   Azure Front Door でプロファイルレベルおよびルートレベルの Web Application Firewall ポリシーが構成可能に[^14]。

2. **Azure Database for MySQL の Reader Endpoint**  
   Azure Database for MySQL でリードレプリカ向けの Reader Endpoint がパブリックプレビュー[^15]。

3. **Azure VM のディスク単位レジリエンシー**  
   仮想マシンのディスクごとにレジリエンシー設定が可能に[^16]。

4. **Azure Multicloud Interconnect**  
   Azure と他クラウド間の相互接続を実現する Azure Multicloud Interconnect がパブリックプレビュー[^17]。

[^1]: Generally Available: Azure Virtual Network Manager IPAM in additional Azure regions, https://azure.microsoft.com/updates/v2/Azure-Virtual-Network-Manager-IPAM-additional-regions

[^2]: Generally Available: Azure Site Recovery support for Linux Azure VMs with NVMe disk controllers, https://azure.microsoft.com/updates/v2/Azure-Site-Recovery-NVMe-Linux-VM-Support

[^3]: Generally Available: Microsoft Defender for Cloud support for Azure Container Apps, https://azure.microsoft.com/updates/v2/Defender-for-Cloud-Container-Apps-Serverless-Posture

[^4]: Generally Available: Windows Server 2025 on AKS, https://azure.microsoft.com/updates/v2/Windows-Server-2025-on-AKS

[^5]: Generally Available: Artifact Streaming on AKS, https://azure.microsoft.com/updates/v2/Artifact-Streaming-on-AKS

[^6]: Generally Available: Confidential VMs for Azure Linux, https://azure.microsoft.com/updates/v2/Confidential-VMs-for-Azure-Linux

[^7]: Generally Available: Purchase order mapping available in Microsoft Marketplace, https://azure.microsoft.com/updates/v2/Purchase-order-mapping-Marketplace

[^8]: Generally Available: Azure Firewall auto-learn SNAT routes, https://azure.microsoft.com/updates/v2/Azure-Firewall-auto-learn-SNAT-routes

[^9]: Generally Available: Azure Copilot Observability Agent supports Basic and Auxiliary table plans, https://azure.microsoft.com/updates/v2/Copilot-Observability-Agent-Basic-Auxiliary

[^10]: Generally Available: Azure Monitor Auxiliary Logs Plan in Azure Government and China regions, https://azure.microsoft.com/updates/v2/Azure-Monitor-Auxiliary-Logs-Government-China

[^11]: Generally Available: Azure Monitor Auxiliary Logs Plan support for Azure tables and plan switching, https://azure.microsoft.com/updates/v2/Azure-Monitor-Auxiliary-Logs-tables-plan-switching

[^12]: Generally Available: Workload identity support for Azure Files CSI driver (SMB) in Azure, https://azure.microsoft.com/updates/v2/Workload-identity-Azure-Files-CSI-SMB

[^13]: Generally Available: Azure VM Image Builder in sovereign and air-gapped clouds, https://azure.microsoft.com/updates/v2/VM-Image-Builder-sovereign-airgapped

[^14]: Public Preview: Azure Front Door profile and route level WAF policies, https://azure.microsoft.com/updates/v2/Azure-Front-Door-WAF-policies

[^15]: Public Preview: Reader Endpoint for Azure Database for MySQL, https://azure.microsoft.com/updates/v2/Reader-Endpoint-Azure-Database-MySQL

[^16]: Public Preview: Per-disk resiliency for Azure VMs, https://azure.microsoft.com/updates/v2/Per-disk-resiliency-Azure-VMs

[^17]: Public Preview: Azure Multicloud Interconnect, https://azure.microsoft.com/updates/v2/Azure-Multicloud-Interconnect
