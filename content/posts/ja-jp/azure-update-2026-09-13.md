Title: Azure Update (2026/09/04 - 2026/09/13)
Date: 2026-09-13
Slug: azure-update-2026-09-13
Lang: ja-jp
Category: notebook
Tags: azure, azure-update, ga, public-preview, retirement, azure-functions, azure-copilot, azure-blob-storage, virtual-machines, azure-load-testing, azure-developer-cli, azure-storage-mover, azure-kubernetes-service
Summary: 2026年9月4日〜9月13日の Azure Update まとめ。Azure Storage Mover のエージェントレス SMB 移行のパブリックプレビューや Azure Linux with OS Guard の廃止告知など計8件。

2026年9月4日〜9月13日に更新された Azure Update の中から主要なアナウンスをまとめます。

## GA (一般提供)

- **TLS/SSL certificate and end-to-end TLS encryption support for Azure Functions Flex Consumption**[^1] — Azure Functions Flex Consumption プランで TLS/SSL 証明書およびエンドツーエンド TLS 暗号化がサポートされました。
- **Azure Copilot Troubleshooting Agent**[^2] — Azure Copilot にトラブルシューティングエージェントが一般提供されました。
- **User-bound user delegation SAS for Azure Storage**[^3] — Azure Storage でユーザーバウンドのユーザー委任 SAS が一般提供されました。
- **Azure Ephemeral OS Disk with full caching for VM/VMSS**[^4] — VM/VMSS 向けにフルキャッシュ付きエフェメラル OS ディスクが一般提供されました。
- **Playwright Workspaces in Australia East, Japan East, and Switzerland North**[^5] — Azure Load Testing の Playwright Workspaces が Australia East、Japan East、Switzerland North リージョンで利用可能になりました。
- **Azure Developer CLI (azd) Extension Framework**[^6] — Azure Developer CLI (azd) の拡張フレームワークが一般提供されました。

## パブリックプレビュー

- **Agentless migration of on-premises SMB file shares to Azure Files (SMB)**[^7] — Azure Storage Mover でオンプレミスの SMB ファイル共有を Azure Files へエージェントレスで移行する機能がパブリックプレビューになりました。

## 廃止 (Retirement)

- **Azure Linux with OS Guard in Azure Kubernetes Service**[^8] — AKS における Azure Linux with OS Guard は 2026年12月10日に廃止予定です。代替として Azure Container Linux への移行が推奨されています。

[^1]: Generally Available: TLS/SSL certificate and end-to-end TLS encryption support for Azure Functions Flex Consumption, https://azure.microsoft.com/updates/v2/TLS-SSL-certificate-and-end-to-end-TLS-encryption-support-for-Azure-Functions-Flex-Consumption

[^2]: Generally Available: Azure Copilot Troubleshooting Agent, https://azure.microsoft.com/updates/v2/Azure-Copilot-Troubleshooting-Agent

[^3]: Generally Available: User-bound user delegation SAS for Azure Storage, https://azure.microsoft.com/updates/v2/User-bound-user-delegation-SAS-for-Azure-Storage

[^4]: Generally Available: Azure Ephemeral OS Disk with full caching for VM/VMSS, https://azure.microsoft.com/updates/v2/Azure-Ephemeral-OS-Disk-with-full-caching-for-VM-VMSS

[^5]: Generally Available: Playwright Workspaces in Australia East, Japan East, and Switzerland North, https://azure.microsoft.com/updates/v2/Playwright-Workspaces-in-Australia-East-Japan-East-and-Switzerland-North

[^6]: Generally Available: Azure Developer CLI (azd) Extension Framework, https://azure.microsoft.com/updates/v2/Azure-Developer-CLI-azd-Extension-Framework

[^7]: Public Preview: Agentless migration of on-premises SMB file shares to Azure Files (SMB), https://azure.microsoft.com/updates/v2/Agentless-migration-of-on-premises-SMB-file-shares-to-Azure-Files-SMB

[^8]: Retirement: Azure Linux with OS Guard in Azure Kubernetes Service, https://azure.microsoft.com/updates/v2/Azure-Linux-with-OS-Guard-in-Azure-Kubernetes-Service
