Title: Azure Update (2026/09/02 - 2026/09/11)
Date: 2026-09-11
Slug: azure-update-2026-09-11
Lang: ja-jp
Category: notebook
Tags: azure, azure-update, ga, public-preview, private-preview, azure-functions, azure-copilot, azure-blob-storage, virtual-machines, azure-load-testing, azure-developer-cli, azure-virtual-network-manager, azure-site-recovery, azure-front-door, web-application-firewall, azure-database-for-mysql
Summary: 2026年9月2日〜9月11日の Azure Update まとめ。Azure Functions Flex Consumption の TLS/SSL 対応や Azure Copilot Troubleshooting Agent の GA など計10件。

Azure Update の直近についてまとめます。

## GA

1. **Generally Available: TLS/SSL certificate and end-to-end TLS encryption support for Azure Functions Flex Consumption**
   Azure Functions Flex Consumption プランで TLS/SSL 証明書およびエンドツーエンド TLS 暗号化がサポートされました[^1]。

2. **Generally Available: Azure Copilot Troubleshooting Agent**
   Azure Copilot のトラブルシューティングエージェントが一般提供開始されました[^2]。

3. **Generally Available: User-bound user delegation SAS for Azure Storage**
   Azure Storage のユーザー委任 SAS にユーザーバインド機能が追加され、GA となりました[^3]。

4. **Generally Available: Azure Ephemeral OS Disk with full caching for VM/VMSS**
   VM/VMSS 向け Azure Ephemeral OS Disk で完全キャッシュがサポートされ、GA となりました[^4]。

5. **Generally Available: Playwright Workspaces in Australia East, Japan East, and Switzerland North**
   Playwright Workspaces が Australia East、Japan East、Switzerland North リージョンで利用可能になりました[^5]。

6. **Generally Available: Azure Developer CLI (azd) Extension Framework**
   Azure Developer CLI (azd) の拡張フレームワークが GA となりました[^6]。

7. **Generally Available: Azure Virtual Network Manager IPAM in additional Azure regions**
   Azure Virtual Network Manager の IPAM 機能が追加リージョンで利用可能になりました[^7]。

8. **Generally Available: Azure Site Recovery support for Linux Azure VMs with NVMe disk controllers**
   Azure Site Recovery が NVMe ディスクコントローラーを搭載した Linux Azure VM をサポートしました[^8]。

## Public Preview

1. **Public Preview: Azure Front Door profile and route level WAF policies**
   Azure Front Door のプロファイルおよびルートレベルでの WAF ポリシー設定がパブリックプレビューとなりました[^9]。

## Private Preview

1. **Private Preview: Reader Endpoint for Azure Database for MySQL**
   Azure Database for MySQL のリーダーエンドポイントがプライベートプレビューとして提供されています[^10]。

[^1]: Generally Available: TLS/SSL certificate and end-to-end TLS encryption support for Azure Functions Flex Consumption, https://azure.microsoft.com/updates/570940

[^2]: Generally Available: Azure Copilot Troubleshooting Agent, https://azure.microsoft.com/updates/570980

[^3]: Generally Available: User-bound user delegation SAS for Azure Storage, https://azure.microsoft.com/updates/569241

[^4]: Generally Available: Azure Ephemeral OS Disk with full caching for VM/VMSS, https://azure.microsoft.com/updates/570551

[^5]: Generally Available: Playwright Workspaces in Australia East, Japan East, and Switzerland North, https://azure.microsoft.com/updates/570919

[^6]: Generally Available: Azure Developer CLI (azd) Extension Framework, https://azure.microsoft.com/updates/570881

[^7]: Generally Available: Azure Virtual Network Manager IPAM in additional Azure regions, https://azure.microsoft.com/updates/570557

[^8]: Generally Available: Azure Site Recovery support for Linux Azure VMs with NVMe disk controllers, https://azure.microsoft.com/updates/565103

[^9]: Public Preview: Azure Front Door profile and route level WAF policies, https://azure.microsoft.com/updates/569804

[^10]: Private Preview: Reader Endpoint for Azure Database for MySQL, https://azure.microsoft.com/updates/569653
