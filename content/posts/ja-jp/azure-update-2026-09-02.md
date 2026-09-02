Title: Azure Update (2026/08/24 - 2026/09/02)
Date: 2026-09-02
Slug: azure-update-2026-09-02
Lang: ja-jp
Category: notebook
Tags: azure, azure-update, ga, public-preview, retirement, azure-container-apps, azure-kubernetes-service, azure-firewall, azure-monitor, azure-copilot, azure-disk-storage, azure-expressroute, azure-files, azure-vm-image-builder, azure-bastion, azure-sre-agent, virtual-machines, azure-database-for-postgresql, application-gateway, app-service
Summary: 2026年8月24日〜9月2日の Azure Update まとめ。Microsoft Defender for Cloud の Container Apps 対応、AKS 向け Windows Server 2025 サポートなど計25件。

2026年8月24日〜9月2日に更新された Azure Update のまとめです。

## GA

1. **Microsoft Defender for Cloud support for Azure Container Apps (Serverless Containers Posture)** — Microsoft Defender for Cloud が Azure Container Apps のサーバーレス コンテナー ポスチャーに対応[^1]。
2. **Windows Server 2025 on AKS** — AKS で Windows Server 2025 が一般提供開始[^2]。
3. **Artifact Streaming on AKS** — AKS でアーティファクト ストリーミングが一般提供。コンテナー イメージの取得を高速化[^3]。
4. **Confidential VMs for Azure Linux** — Azure Linux 向け Confidential VM が一般提供開始[^4]。
5. **Purchase order mapping available in Microsoft Marketplace** — Microsoft Marketplace で購入注文マッピングが利用可能に[^5]。
6. **Azure Firewall auto-learn SNAT routes** — Azure Firewall が SNAT ルートを自動学習する機能が一般提供[^6]。
7. **Azure Copilot Observability Agent supports Basic and Auxiliary table plans** — Azure Copilot Observability Agent が Basic および Auxiliary テーブル プランに対応[^7]。
8. **Azure Monitor Auxiliary Logs Plan in Azure Government and China regions** — Azure Monitor Auxiliary Logs Plan が Azure Government および China リージョンで利用可能に[^8]。
9. **Azure Monitor Auxiliary Logs Plan support for Azure tables and plan switching** — Azure Monitor Auxiliary Logs Plan が Azure テーブルとプラン切り替えに対応[^9]。
10. **Workload identity support for Azure Files CSI driver (SMB) in Azure** — Azure Files CSI ドライバー（SMB）でワークロード ID が一般提供[^10]。
11. **Azure VM Image Builder in sovereign and air-gapped clouds** — Azure VM Image Builder がソブリンおよびエアギャップ クラウドで利用可能に[^11]。
12. **Azure Bastion shareable link expiration** — Azure Bastion の共有リンクに有効期限設定が追加[^12]。
13. **Connect to AKS clusters using Azure Bastion** — Azure Bastion 経由で AKS クラスターへ接続可能に[^13]。
14. **Azure SRE Agent VNet Integration** — Azure SRE Agent が VNet 統合に対応[^14]。
15. **Azure SRE Agent 30-Day Trial** — Azure SRE Agent の 30 日間無料トライアルが開始[^15]。
16. **Azure 248 and 372 vCPU sizes for D/E v7 series VMs** — D/E v7 シリーズ VM に 248 および 372 vCPU サイズが追加[^16]。
17. **eBPF host routing in Advanced Container Networking Services for AKS** — AKS 向け Advanced Container Networking Services で eBPF ホスト ルーティングが一般提供[^17]。
18. **Custom block response code and body for Application Gateway WAF** — Application Gateway WAF でカスタム ブロック応答コードと本文が設定可能に[^18]。

## Public Preview

1. **Per-disk resiliency for Azure VMs** — Azure VM でディスク単位のレジリエンシーがパブリック プレビュー[^19]。
2. **Azure Multicloud Interconnect** — Azure Multicloud Interconnect がパブリック プレビュー[^20]。
3. **IPv6 dual-stack support for Azure Bastion** — Azure Bastion で IPv6 デュアルスタックがパブリック プレビュー[^21]。
4. **Introducing Live Reports for Azure SRE Agent** — Azure SRE Agent にライブ レポート機能がパブリック プレビューとして追加[^22]。

## Other

1. **Aspire 13.5 has shipped** — Aspire 13.5 がリリース[^23]。
2. **Extended Support for Azure Database for PostgreSQL Flexible Server** — Azure Database for PostgreSQL Flexible Server の延長サポートが発表[^24]。
3. **Retirement: Support for Node 22 LTS ends on April 30, 2027** — App Service における Node 22 LTS のサポートが 2027 年 4 月 30 日に終了予定[^25]。

[^1]: Microsoft Defender for Cloud support for Azure Container Apps (Serverless Containers Posture), https://azure.microsoft.com/updates/v2/Defender-for-Cloud-Container-Apps-Posture
[^2]: Windows Server 2025 on AKS, https://azure.microsoft.com/updates/v2/Windows-Server-2025-on-AKS
[^3]: Artifact Streaming on AKS, https://azure.microsoft.com/updates/v2/Artifact-Streaming-on-AKS
[^4]: Confidential VMs for Azure Linux, https://azure.microsoft.com/updates/v2/Confidential-VMs-for-Azure-Linux
[^5]: Purchase order mapping available in Microsoft Marketplace, https://azure.microsoft.com/updates/v2/Purchase-order-mapping-available-in-Microsoft-Marketplace
[^6]: Azure Firewall auto-learn SNAT routes, https://azure.microsoft.com/updates/v2/Azure-Firewall-auto-learn-SNAT-routes
[^7]: Azure Copilot Observability Agent supports Basic and Auxiliary table plans, https://azure.microsoft.com/updates/v2/Azure-Copilot-Observability-Agent-Basic-Auxiliary-Plans
[^8]: Azure Monitor Auxiliary Logs Plan in Azure Government and China regions, https://azure.microsoft.com/updates/v2/Azure-Monitor-Auxiliary-Logs-Plan-Gov-China
[^9]: Azure Monitor Auxiliary Logs Plan support for Azure tables and plan switching, https://azure.microsoft.com/updates/v2/Azure-Monitor-Auxiliary-Logs-Plan-Tables-Plan-Switching
[^10]: Workload identity support for Azure Files CSI driver (SMB) in Azure, https://azure.microsoft.com/updates/v2/workload-identity-support-azure-files-csi-driver-smb
[^11]: Azure VM Image Builder in sovereign and air-gapped clouds, https://azure.microsoft.com/updates/v2/Azure-VM-Image-Builder-sovereign-air-gapped-clouds
[^12]: Azure Bastion shareable link expiration, https://azure.microsoft.com/updates/v2/Azure-Bastion-shareable-link-expiration
[^13]: Connect to AKS clusters using Azure Bastion, https://azure.microsoft.com/updates/v2/Connect-AKS-clusters-Azure-Bastion
[^14]: Azure SRE Agent VNet Integration, https://azure.microsoft.com/updates/v2/Azure-SRE-Agent-VNet-Integration
[^15]: Azure SRE Agent 30-Day Trial, https://azure.microsoft.com/updates/v2/Azure-SRE-Agent-30-Day-Trial
[^16]: Azure 248 and 372 vCPU sizes for D/E v7 series VMs, https://azure.microsoft.com/updates/v2/Azure-248-372-vCPU-sizes-D-E-v7-series-VMs
[^17]: eBPF host routing in Advanced Container Networking Services for AKS, https://azure.microsoft.com/updates/v2/eBPF-host-routing-Advanced-Container-Networking-Services-AKS
[^18]: Custom block response code and body for Application Gateway WAF, https://azure.microsoft.com/updates/v2/Custom-block-response-code-body-Application-Gateway-WAF
[^19]: Per-disk resiliency for Azure VMs, https://azure.microsoft.com/updates/v2/Per-disk-resiliency-for-Azure-VMs
[^20]: Azure Multicloud Interconnect, https://azure.microsoft.com/updates/v2/Azure-Multicloud-Interconnect
[^21]: IPv6 dual-stack support for Azure Bastion, https://azure.microsoft.com/updates/v2/IPv6-dual-stack-support-Azure-Bastion
[^22]: Introducing Live Reports for Azure SRE Agent, https://azure.microsoft.com/updates/v2/Introducing-Live-Reports-Azure-SRE-Agent
[^23]: Aspire 13.5 has shipped, https://azure.microsoft.com/updates/v2/Aspire-13-5-has-shipped
[^24]: Extended Support for Azure Database for PostgreSQL Flexible Server, https://azure.microsoft.com/updates/v2/Extended-Support-Azure-Database-PostgreSQL-Flexible-Server
[^25]: Support for Node 22 LTS ends on April 30, 2027, https://azure.microsoft.com/updates/v2/Node-22-LTS-support-ends-April-2027
