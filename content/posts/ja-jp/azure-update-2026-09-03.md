Title: Azure Update (2026/08/25 - 2026/09/03)
Date: 2026-09-03
Slug: azure-update-2026-09-03
Lang: ja-jp
Category: notebook
Tags: azure, azure-update, ga, public-preview, azure-front-door, azure-database-for-mysql, azure-container-apps, azure-kubernetes-service, azure-firewall, azure-monitor, azure-copilot, azure-disk-storage, azure-expressroute, azure-files, azure-vm-image-builder, azure-bastion, azure-sre-agent, virtual-machines, web-application-firewall
Summary: 2026年8月25日〜9月3日の Azure Update まとめ。Azure Front Door の WAF ポリシー強化や Azure Database for MySQL の Reader Endpoint など計23件。

2026年8月25日〜9月3日に公開・更新された Azure Update のまとめです。

## GA (16件)

1. **Microsoft Defender for Cloud の Azure Container Apps 対応 (Serverless Containers Posture)**  — Azure Container Apps 向けのセキュリティ態勢管理が一般提供開始[^1]。
2. **Windows Server 2025 on AKS** — AKS で Windows Server 2025 ノードが一般提供開始[^2]。
3. **Artifact Streaming on AKS** — AKS で Artifact Streaming が一般提供。コンテナーイメージの取得を高速化[^3]。
4. **Confidential VMs for Azure Linux** — Azure Linux 上の Confidential VM が一般提供開始[^4]。
5. **Purchase order mapping in Microsoft Marketplace** — Microsoft Marketplace で発注書マッピングが利用可能に[^5]。
6. **Azure Firewall auto-learn SNAT routes** — Azure Firewall が SNAT ルートを自動学習する機能が一般提供開始[^6]。
7. **Azure Copilot Observability Agent — Basic/Auxiliary テーブルプラン対応** — Azure Copilot Observability Agent が Basic および Auxiliary テーブルプランに対応[^7]。
8. **Azure Monitor Auxiliary Logs Plan — Azure Government/China リージョン** — Azure Monitor の Auxiliary Logs Plan が Azure Government と China リージョンで利用可能に[^8]。
9. **Azure Monitor Auxiliary Logs Plan — Azure テーブル/プラン切り替え対応** — Azure Monitor Auxiliary Logs Plan で Azure テーブルのサポートとプラン切り替え機能が一般提供開始[^9]。
10. **Workload identity support for Azure Files CSI driver (SMB)** — Azure Files CSI ドライバー (SMB) でワークロード ID が一般提供開始[^10]。
11. **Azure VM Image Builder in sovereign and air-gapped clouds** — ソブリンおよびエアギャップクラウドで Azure VM Image Builder が利用可能に[^11]。
12. **Azure Bastion shareable link expiration** — Azure Bastion の共有リンクに有効期限設定が一般提供開始[^12]。
13. **Connect to AKS clusters using Azure Bastion** — Azure Bastion 経由で AKS クラスターへの接続が一般提供開始[^13]。
14. **Azure SRE Agent VNet Integration** — Azure SRE Agent の VNet 統合が一般提供開始[^14]。
15. **Azure SRE Agent 30-Day Trial** — Azure SRE Agent の 30 日間無料トライアルが利用可能に[^15]。
16. **Azure 248 and 372 vCPU sizes for D/E v7 series VMs** — D/E v7 シリーズ VM に 248 および 372 vCPU サイズが一般提供開始[^16]。

## Public Preview (6件)

1. **Azure Front Door profile and route level WAF policies** — Azure Front Door でプロファイルおよびルートレベルの WAF ポリシーがパブリックプレビュー開始[^17]。
2. **Reader Endpoint for Azure Database for MySQL** — Azure Database for MySQL で Reader Endpoint がパブリックプレビュー開始[^18]。
3. **Per-disk resiliency for Azure VMs** — Azure VM のディスク単位の回復性がパブリックプレビュー開始[^19]。
4. **Azure Multicloud Interconnect** — Azure Multicloud Interconnect がパブリックプレビュー開始[^20]。
5. **IPv6 dual-stack support for Azure Bastion** — Azure Bastion の IPv6 デュアルスタック対応がパブリックプレビュー開始[^21]。
6. **Introducing Live Reports for Azure SRE Agent** — Azure SRE Agent の Live Reports 機能がパブリックプレビュー開始[^22]。

## Other (1件)

1. **Aspire 13.5 has shipped** — .NET Aspire 13.5 がリリース[^23]。

[^1]: Generally Available: Microsoft Defender for Cloud support for Azure Container Apps (Serverless Containers Posture), https://azure.microsoft.com/updates/570282
[^2]: Generally Available: Windows Server 2025 on AKS, https://azure.microsoft.com/updates/570090
[^3]: Generally Available: Artifact Streaming on AKS, https://azure.microsoft.com/updates/570095
[^4]: Generally Available: Confidential VMs for Azure Linux, https://azure.microsoft.com/updates/570100
[^5]: Generally Available: Purchase order mapping available in Microsoft Marketplace, https://azure.microsoft.com/updates/569700
[^6]: Generally Available: Azure Firewall auto-learn SNAT routes, https://azure.microsoft.com/updates/570474
[^7]: Generally Available: Azure Copilot Observability Agent supports Basic and Auxiliary table plans, https://azure.microsoft.com/updates/570250
[^8]: Generally Available: Azure Monitor Auxiliary Logs Plan in Azure Government and China regions, https://azure.microsoft.com/updates/569899
[^9]: Generally Available: Azure Monitor Auxiliary Logs Plan support for Azure tables and plan switching, https://azure.microsoft.com/updates/569904
[^10]: Generally Available: Workload identity support for Azure Files CSI driver (SMB) in Azure, https://azure.microsoft.com/updates/570120
[^11]: Generally Available: Azure VM Image Builder in sovereign and air-gapped clouds, https://azure.microsoft.com/updates/570105
[^12]: Generally Available: Azure Bastion shareable link expiration, https://azure.microsoft.com/updates/570020
[^13]: Generally Available: Connect to AKS clusters using Azure Bastion, https://azure.microsoft.com/updates/570030
[^14]: Generally Available: Azure SRE Agent VNet Integration, https://azure.microsoft.com/updates/569695
[^15]: Generally Available: Azure SRE Agent 30-Day Trial, https://azure.microsoft.com/updates/569760
[^16]: Generally Available: Azure 248 and 372 vCPU sizes for D/E v7 series VMs, https://azure.microsoft.com/updates/569546
[^17]: Public Preview: Azure Front Door profile and route level WAF policies, https://azure.microsoft.com/updates/569804
[^18]: Public Preview: Reader Endpoint for Azure Database for MySQL, https://azure.microsoft.com/updates/569653
[^19]: Public Preview: Per-disk resiliency for Azure VMs, https://azure.microsoft.com/updates/569711
[^20]: Public Preview: Azure Multicloud Interconnect, https://azure.microsoft.com/updates/570364
[^21]: Public Preview: IPv6 dual-stack support for Azure Bastion, https://azure.microsoft.com/updates/570025
[^22]: Public Preview: Introducing Live Reports for Azure SRE Agent, https://azure.microsoft.com/updates/569690
[^23]: Announcing: Aspire 13.5 has shipped, https://azure.microsoft.com/updates/569910
