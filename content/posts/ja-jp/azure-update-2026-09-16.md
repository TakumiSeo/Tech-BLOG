Title: Azure Update (2026/09/07 - 2026/09/16)
Date: 2026-09-16
Slug: azure-update-2026-09-16
Lang: ja-jp
Category: notebook
Tags: azure, azure-update, ga, public-preview, retirement, announcement, azure-functions, azure-copilot, azure-blob-storage, virtual-machines, azure-load-testing, azure-developer-cli, azure-storage-mover, azure-kubernetes-service, application-gateway, azure-virtual-desktop
Summary: 2026年9月7日〜9月16日の Azure Update まとめ。GA 6件、パブリックプレビュー 2件、リタイア 1件、その他 1件の計10件。

2026年9月7日〜9月16日に公開・更新された Azure Update のまとめです。

## 一般提供開始（GA）

- **Azure Developer CLI (azd) Extension Framework**
  azd の拡張フレームワークが一般提供開始。カスタムコマンドやワークフローを拡張可能に[^1]。

- **Playwright Workspaces in Australia East, Japan East, and Switzerland North**
  Azure Load Testing の Playwright Workspaces が Australia East、Japan East、Switzerland North リージョンで利用可能に[^2]。

- **Azure Ephemeral OS Disk with full caching for VM/VMSS**
  VM/VMSS 向けエフェメラル OS ディスクのフルキャッシュ対応が一般提供開始[^3]。

- **User-bound user delegation SAS for Azure Storage**
  Azure Storage のユーザー委任 SAS がユーザーバインドに対応し、セキュリティが強化[^4]。

- **Azure Copilot Troubleshooting Agent**
  Azure Copilot のトラブルシューティングエージェントが一般提供開始[^5]。

- **TLS/SSL certificate and end-to-end TLS encryption support for Azure Functions Flex Consumption**
  Azure Functions Flex Consumption プランで TLS/SSL 証明書およびエンドツーエンド TLS 暗号化をサポート[^6]。

## パブリックプレビュー

- **Agentless migration of on-premises SMB file shares to Azure Files (SMB)**
  オンプレミスの SMB ファイル共有を Azure Files (SMB) へエージェントレスで移行する機能がパブリックプレビュー[^7]。

- **HTTP/3 over QUIC support in Azure Application Gateway**
  Application Gateway で HTTP/3 over QUIC のサポートがパブリックプレビュー開始[^8]。

## リタイア

- **Azure Linux with OS Guard in Azure Kubernetes Service**
  AKS における Azure Linux with OS Guard のリタイアが発表。2026年12月10日に廃止予定[^9]。

## その他

- **New Windows App client-side endpoints for Azure Virtual Desktop**
  Azure Virtual Desktop のクライアント側サービストラフィック向けに新しいワイルドカード FQDN が追加。2026年10月より適用開始[^10]。

[^1]: Generally Available: Azure Developer CLI (azd) Extension Framework, https://azure.microsoft.com/updates/v2/azd-extension-framework
[^2]: Generally Available: Playwright Workspaces in Australia East, Japan East, and Switzerland North, https://azure.microsoft.com/updates/v2/Playwright-Workspaces-Australia-East-Japan-East-Switzerland-North
[^3]: Generally Available: Azure Ephemeral OS Disk with full caching for VM/VMSS, https://azure.microsoft.com/updates/v2/Azure-Ephemeral-OS-Disk-with-full-caching-for-VM-VMSS
[^4]: Generally Available: User-bound user delegation SAS for Azure Storage, https://azure.microsoft.com/updates/v2/user-bound-user-delegation-sas
[^5]: Generally Available: Azure Copilot Troubleshooting Agent, https://azure.microsoft.com/updates/v2/Azure-Copilot-Troubleshooting-Agent
[^6]: Generally Available: TLS/SSL certificate and end-to-end TLS encryption support for Azure Functions Flex Consumption, https://azure.microsoft.com/updates/v2/TLS-SSL-certificate-and-end-to-end-TLS-encryption-support-for-Azure-Functions-Flex-Consumption
[^7]: Public Preview: Agentless migration of on-premises SMB file shares to Azure Files (SMB), https://azure.microsoft.com/updates/v2/agentless-smb-migration
[^8]: Public Preview: HTTP/3 over QUIC support in Azure Application Gateway, https://azure.microsoft.com/updates/v2/HTTP3-QUIC-support-in-Application-Gateway
[^9]: Retirement: Azure Linux with OS Guard in Azure Kubernetes Service, https://azure.microsoft.com/updates/v2/Azure-Linux-with-OS-Guard-in-Azure-Kubernetes-Service-retirement
[^10]: Announcing: New Windows App client-side endpoints for Azure Virtual Desktop, https://azure.microsoft.com/updates/v2/New-Windows-App-client-side-endpoints-for-Azure-Virtual-Desktop
