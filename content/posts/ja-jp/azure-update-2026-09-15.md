Title: Azure Update (2026/09/06 - 2026/09/15)
Date: 2026-09-15
Slug: azure-update-2026-09-15
Lang: ja-jp
Category: notebook
Tags: azure, azure-update, ga, public-preview, retirement, announcement, azure-functions, azure-copilot, azure-blob-storage, virtual-machines, azure-load-testing, azure-developer-cli, azure-storage-mover, azure-kubernetes-service, application-gateway, azure-virtual-desktop
Summary: 2026年9月6日〜9月15日の Azure Update まとめ。Application Gateway の HTTP/3 対応パブリックプレビューや Azure Virtual Desktop の新エンドポイント告知など計10件。

## GA

- **Azure Developer CLI (azd) Extension Framework**  
  Azure Developer CLI (azd) の拡張フレームワークが GA。azd のワークフローを拡張するカスタム拡張機能の作成・利用が可能に[^1]。

- **Playwright Workspaces in Australia East, Japan East, and Switzerland North**  
  Azure Load Testing の Playwright Workspaces が Australia East・Japan East・Switzerland North リージョンで GA[^2]。

- **Azure Ephemeral OS Disk with full caching for VM/VMSS**  
  VM/VMSS 向けエフェメラル OS ディスクのフルキャッシュ機能が GA。ローカルストレージを活用した高速起動とコスト削減を実現[^3]。

- **User-bound user delegation SAS for Azure Storage**  
  Azure Storage のユーザー委任 SAS がユーザーバインドに対応し GA。より細かいアクセス制御が可能に[^4]。

- **Azure Copilot Troubleshooting Agent**  
  Azure Copilot のトラブルシューティングエージェントが GA。Azure リソースの問題診断を AI が支援[^5]。

- **TLS/SSL certificate and end-to-end TLS encryption support for Azure Functions Flex Consumption**  
  Azure Functions Flex Consumption プランで TLS/SSL 証明書およびエンドツーエンド TLS 暗号化のサポートが GA[^6]。

## Public Preview

- **Agentless migration of on-premises SMB file shares to Azure Files (SMB)**  
  オンプレミスの SMB ファイル共有を Azure Files (SMB) へエージェントレスで移行する機能がパブリックプレビュー。Azure Storage Mover を使用[^7]。

- **HTTP/3 over QUIC support in Azure Application Gateway**  
  Azure Application Gateway で HTTP/3 over QUIC のサポートがパブリックプレビュー。QUIC プロトコルにより接続確立の高速化・レイテンシ削減・耐障害性の向上を実現[^8]。

## Retirement

- **Azure Linux with OS Guard in Azure Kubernetes Service**  
  Azure Kubernetes Service における Azure Linux with OS Guard の廃止が告知された。2026年12月10日に廃止予定[^9]。

## その他

- **Announcing: New Windows App client-side endpoints for Azure Virtual Desktop**  
  Azure Virtual Desktop 向け Windows App のクライアント側エンドポイントに新しいワイルドカード FQDN が追加される。2026年10月初旬から有効化予定。ネットワーク制御を適用している環境では事前の許可設定が必要[^10]。

[^1]: Generally Available: Azure Developer CLI (azd) Extension Framework, https://azure.microsoft.com/updates/v2/azd-extension-framework
[^2]: Generally Available: Playwright Workspaces in Australia East, Japan East, and Switzerland North, https://azure.microsoft.com/updates/v2/Playwright-Workspaces-in-Australia-East-Japan-East-and-Switzerland-North
[^3]: Generally Available: Azure Ephemeral OS Disk with full caching for VM/VMSS, https://azure.microsoft.com/updates/v2/Azure-Ephemeral-OS-Disk-with-full-caching-for-VM-VMSS
[^4]: Generally Available: User-bound user delegation SAS for Azure Storage, https://azure.microsoft.com/updates/v2/User-Bound-User-Delegation-SAS
[^5]: Generally Available: Azure Copilot Troubleshooting Agent, https://azure.microsoft.com/updates/v2/Azure-Copilot-Troubleshooting-Agent
[^6]: Generally Available: TLS/SSL certificate and end-to-end TLS encryption support for Azure Functions Flex Consumption, https://azure.microsoft.com/updates/v2/TLS-SSL-certificate-and-end-to-end-TLS-encryption-support-for-Azure-Functions-Flex-Consumption
[^7]: Public Preview: Agentless migration of on-premises SMB file shares to Azure Files (SMB), https://azure.microsoft.com/updates/v2/agentless-migration-smb-file-shares-to-azure-files
[^8]: Public Preview: HTTP/3 over QUIC support in Azure Application Gateway, https://azure.microsoft.com/updates/v2/HTTP-3-over-QUIC-support-in-Azure-Application-Gateway
[^9]: Retirement: Azure Linux with OS Guard in Azure Kubernetes Service, https://azure.microsoft.com/updates/v2/Azure-Linux-with-OS-Guard-in-Azure-Kubernetes-Service
[^10]: Announcing: New Windows App client-side endpoints for Azure Virtual Desktop, https://azure.microsoft.com/updates/v2/New-Windows-App-client-side-endpoints-for-Azure-Virtual-Desktop
