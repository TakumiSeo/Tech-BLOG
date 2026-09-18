Title: Azure Update (2026/09/09 - 2026/09/18)
Date: 2026-09-18
Slug: azure-update-2026-09-18
Lang: ja-jp
Category: notebook
Tags: azure, azure-update, ga, public-preview, retirement, announcement, azure-virtual-network-manager, azure-functions, azure-copilot, azure-storage, virtual-machines, azure-payments-hsm, azure-sql-database, azure-red-hat-openshift, azure-database-for-postgresql, application-gateway, azure-storage-mover, azure-kubernetes-service, azure-virtual-desktop
Summary: 2026年9月9日〜9月18日の Azure Update まとめ。GA 5件、パブリックプレビュー 6件、リタイア 2件、その他 1件の計14件。

## GA

- **Azure Virtual Network Manager の High-scale mesh が一般提供開始**
  Connected group を使用した High-scale mesh が GA。単一のメッシュ接続構成で最大 3,000 仮想ネットワークを接続可能[^1]。

- **Azure Functions Flex Consumption で TLS/SSL 証明書およびエンドツーエンド TLS 暗号化をサポート**
  Flex Consumption プランで TLS/SSL 証明書のバインドとエンドツーエンド TLS 暗号化が GA[^2]。

- **Azure Copilot Troubleshooting Agent が一般提供開始**
  Azure Copilot のトラブルシューティングエージェントが GA[^3]。

- **Azure Storage のユーザーバインド ユーザー委任 SAS が一般提供開始**
  ユーザー委任 SAS をユーザーに紐づけることで、SAS トークンのセキュリティを強化する機能が GA[^4]。

- **Azure Ephemeral OS Disk のフルキャッシュ対応が VM/VMSS で一般提供開始**
  VM および VMSS でエフェメラル OS ディスクのフルキャッシュが GA[^5]。

## パブリックプレビュー

- **Azure Payments HSM v2 がパブリックプレビュー**
  高可用性のシングルテナント Payment HSM サービス。決済処理、PIN 処理、鍵管理、認証データ保護に対応[^6]。

- **Azure SQL の 2026 年 9 月中旬アップデート**
  Azure SQL Database に関する複数のアップデートがプレビュー提供[^7]。

- **Azure Red Hat OpenShift でホステッドコントロールプレーンをサポート**
  ホステッドコントロールプレーンにより、コントロールプレーンの管理をシンプル化[^8]。

- **Azure Database for PostgreSQL 向け PostgreSQL スキルおよび MCP プラグイン**
  PostgreSQL のスキルと MCP プラグインがプレビュー提供[^9]。

- **Azure Application Gateway で HTTP/3 over QUIC をサポート**
  Application Gateway が HTTP/3 over QUIC プロトコルに対応[^10]。

- **オンプレミス SMB ファイル共有の Azure Files (SMB) へのエージェントレス移行**
  Azure Storage Mover によるエージェントレスの SMB ファイル共有移行がプレビュー提供[^11]。

## リタイア

- **SAP コンテナーイメージが 2026 年 10 月 14 日に削除予定**
  SAP コンテナーイメージのサポートが終了し、2026 年 10 月 14 日に削除される[^12]。

- **Azure Kubernetes Service の Azure Linux with OS Guard がリタイア**
  AKS における Azure Linux with OS Guard が 2026 年 12 月 10 日にリタイア予定[^13]。

## その他

- **Azure Virtual Desktop の新しい Windows App クライアント側エンドポイント**
  Azure Virtual Desktop 向けの新しい Windows App クライアント側エンドポイントが 2026 年 10 月より適用[^14]。

[^1]: Generally Available: High-scale mesh in Azure Virtual Network Manager, https://azure.microsoft.com/updates/?id=571572

[^2]: Generally Available: TLS/SSL certificate and end-to-end TLS encryption support for Azure Functions Flex Consumption, https://azure.microsoft.com/updates/?id=570940

[^3]: Generally Available: Azure Copilot Troubleshooting Agent, https://azure.microsoft.com/updates/?id=570980

[^4]: Generally Available: User-bound user delegation SAS for Azure Storage, https://azure.microsoft.com/updates/?id=569241

[^5]: Generally Available: Azure Ephemeral OS Disk with full caching for VM/VMSS, https://azure.microsoft.com/updates/?id=570551

[^6]: Public Preview: Azure Payments HSM v2, https://azure.microsoft.com/updates/?id=570509

[^7]: Public Preview: Azure SQL updates for mid-September 2026, https://azure.microsoft.com/updates/?id=571056

[^8]: Public Preview: Azure Red Hat OpenShift with hosted control planes, https://azure.microsoft.com/updates/?id=571621

[^9]: Public Preview: PostgreSQL skills and MCP plugin for Azure Database for PostgreSQL, https://azure.microsoft.com/updates/?id=569664

[^10]: Public Preview: HTTP/3 over QUIC support in Azure Application Gateway, https://azure.microsoft.com/updates/?id=571123

[^11]: Public Preview: Agentless migration of on-premises SMB file shares to Azure Files (SMB), https://azure.microsoft.com/updates/?id=570910

[^12]: Retirement Update: SAP container images removed October 14, 2026, https://azure.microsoft.com/updates/?id=571342

[^13]: Retirement: Azure Linux with OS Guard in Azure Kubernetes Service, https://azure.microsoft.com/updates/?id=571257

[^14]: Announcing: New Windows App client-side endpoints for Azure Virtual Desktop, https://azure.microsoft.com/updates/?id=571360
