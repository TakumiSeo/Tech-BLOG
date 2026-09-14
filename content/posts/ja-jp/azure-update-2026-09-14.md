Title: Azure Update (2026/09/05 - 2026/09/14)
Date: 2026-09-14
Slug: azure-update-2026-09-14
Lang: ja-jp
Category: notebook
Tags: azure, azure-update, ga, public-preview, retirement, azure-functions, azure-copilot, azure-blob-storage, virtual-machines, azure-load-testing, azure-developer-cli, azure-storage-mover, azure-kubernetes-service
Summary: 2026年9月5日〜9月14日の Azure Update まとめ。Azure Functions Flex Consumption の TLS サポート GA や Azure Linux with OS Guard の廃止告知など計8件。

2026年9月5日〜9月14日に更新された Azure Update のまとめです。

## GA

- **Azure Developer CLI (azd) Extension Framework**[^1] — Azure Developer CLI (azd) の拡張フレームワークが一般提供開始。
- **Playwright Workspaces in Australia East, Japan East, and Switzerland North**[^2] — Azure Load Testing の Playwright Workspaces が Australia East・Japan East・Switzerland North リージョンで利用可能に。
- **Azure Ephemeral OS Disk with full caching for VM/VMSS**[^3] — 仮想マシンおよび VMSS 向けのエフェメラル OS ディスクがフルキャッシュ対応で一般提供開始。
- **User-bound user delegation SAS for Azure Storage**[^4] — Azure Blob Storage のユーザー委任 SAS がユーザーバインドに対応し一般提供開始。
- **Azure Copilot Troubleshooting Agent**[^5] — Azure Copilot のトラブルシューティングエージェントが一般提供開始。
- **TLS/SSL certificate and end-to-end TLS encryption support for Azure Functions Flex Consumption**[^6] — Azure Functions Flex Consumption で TLS/SSL 証明書およびエンドツーエンド TLS 暗号化が一般提供開始。

## Public Preview

- **Agentless migration of on-premises SMB file shares to Azure Files (SMB)**[^7] — Azure Storage Mover によるオンプレミス SMB ファイル共有から Azure Files (SMB) へのエージェントレス移行がパブリックプレビュー。

## Retirement

- **Azure Linux with OS Guard in Azure Kubernetes Service**[^8] — AKS における Azure Linux with OS Guard が 2026年12月10日に廃止予定。

[^1]: Generally Available: Azure Developer CLI (azd) Extension Framework, https://azure.microsoft.com/updates/v2/azd-Extension-Framework

[^2]: Generally Available: Playwright Workspaces in Australia East, Japan East, and Switzerland North, https://azure.microsoft.com/updates/v2/Playwright-Testing-Workspaces-New-Regions

[^3]: Generally Available: Azure Ephemeral OS Disk with full caching for VM/VMSS, https://azure.microsoft.com/updates/v2/Azure-Ephemeral-OS-Disk-Full-Caching

[^4]: Generally Available: User-bound user delegation SAS for Azure Storage, https://azure.microsoft.com/updates/v2/User-Bound-User-Delegation-SAS

[^5]: Generally Available: Azure Copilot Troubleshooting Agent, https://azure.microsoft.com/updates/v2/Azure-Copilot-Troubleshooting-Agent

[^6]: Generally Available: TLS/SSL certificate and end-to-end TLS encryption support for Azure Functions Flex Consumption, https://azure.microsoft.com/updates/v2/Azure-Functions-Flex-Consumption-TLS-Support

[^7]: Public Preview: Agentless migration of on-premises SMB file shares to Azure Files (SMB), https://azure.microsoft.com/updates/v2/Storage-Mover-Agentless-SMB-Migration

[^8]: Retirement: Azure Linux with OS Guard in Azure Kubernetes Service, https://azure.microsoft.com/updates/v2/Azure-Linux-OS-Guard-AKS-Retirement
