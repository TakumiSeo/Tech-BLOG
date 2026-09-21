Title: Azure Update (2026/09/12 - 2026/09/21)
Date: 2026-09-21
Slug: azure-update-2026-09-21
Lang: ja-jp
Category: notebook
Tags: azure, azure-update, ga, public-preview, retirement, announcement, microsoft-foundry, azure-database-for-postgresql, azure-virtual-network-manager, virtual-machines, azure-payments-hsm, azure-sql-database, azure-red-hat-openshift, application-gateway, azure-virtual-desktop
Summary: 2026年9月12日〜9月21日の Azure Update まとめ。GA 6件、パブリックプレビュー 8件、リタイア 1件、その他 1件の計16件。

2026年9月12日〜9月21日に更新された Azure Update のまとめです。

## GA

- **Microsoft Foundry エージェントの有効化・無効化コントロール（Agent 365）** — Agent 365 において Microsoft Foundry エージェントの有効化・無効化制御が一般提供開始[^1]。
- **Microsoft Foundry エージェントの Microsoft 365 Copilot および Teams への発行** — Microsoft Foundry で構築したエージェントを Microsoft 365 Copilot および Teams に発行する機能が一般提供開始[^2]。
- **Azure Database for PostgreSQL フレキシブルサーバーの論理レプリケーションスロット同期ステータスメトリック** — 論理レプリケーションスロットの同期状態を監視するメトリックが一般提供開始[^3]。
- **Azure Database for PostgreSQL の新しいトラブルシューティングガイド** — Azure Database for PostgreSQL 向けの改善されたトラブルシューティングガイドが一般提供開始[^4]。
- **Azure Database for PostgreSQL エラスティッククラスターの PG18 サポート** — エラスティッククラスターで PostgreSQL 18 がサポート開始[^5]。
- **Azure Virtual Network Manager のハイスケールメッシュ** — Azure Virtual Network Manager でハイスケールメッシュが一般提供開始[^6]。

## パブリックプレビュー

- **Foundry Agent Service の Foundry Routines** — Foundry Agent Service で Foundry Routines がパブリックプレビュー開始[^7]。
- **SAP 向け Mdsv4 / Msv4 シリーズ仮想マシン** — SAP ワークロード向けの Mdsv4 および Msv4 シリーズ仮想マシンがパブリックプレビュー開始[^8]。
- **Microsoft Foundry ホステッドエージェントのネットワークエグレス制御** — Microsoft Foundry のホステッドエージェントにおけるネットワークエグレス制御がパブリックプレビュー開始[^9]。
- **Azure Payments HSM v2** — Azure Payments HSM v2 がパブリックプレビュー開始[^10]。
- **Azure SQL の 2026年9月中旬アップデート** — Azure SQL Database の 2026年9月中旬のアップデートがパブリックプレビュー開始[^11]。
- **Azure Red Hat OpenShift ホステッドコントロールプレーン** — Azure Red Hat OpenShift でホステッドコントロールプレーンがパブリックプレビュー開始[^12]。
- **Azure Database for PostgreSQL の PostgreSQL スキルおよび MCP プラグイン** — Azure Database for PostgreSQL 向けの PostgreSQL スキルと MCP プラグインがパブリックプレビュー開始[^13]。
- **Azure Application Gateway の HTTP/3 over QUIC サポート** — Azure Application Gateway で HTTP/3 over QUIC がパブリックプレビュー開始[^14]。

## リタイア

- **SAP コンテナーイメージの削除（2026年10月14日）** — SAP コンテナーイメージが 2026年10月14日に削除予定[^15]。

## その他

- **Azure Virtual Desktop の新しい Windows App クライアント側エンドポイント** — Azure Virtual Desktop 向けの新しい Windows App クライアント側エンドポイントが発表[^16]。

[^1]: Generally Available: Enable and disable controls for Microsoft Foundry agents in Agent 365, https://azure.microsoft.com/updates/v2/?id=571826
[^2]: Generally Available: Publishing Microsoft Foundry agents to Microsoft 365 Copilot and Teams, https://azure.microsoft.com/updates/v2/?id=571816
[^3]: Generally Available: Logical replication slot sync status metric for Azure PostgreSQL Flexible Server, https://azure.microsoft.com/updates/v2/?id=568414
[^4]: Generally Available: New and improved troubleshooting guides for Azure Database for PostgreSQL, https://azure.microsoft.com/updates/v2/?id=571042
[^5]: Generally Available: PG18 support for Azure Database for PostgreSQL elastic clusters, https://azure.microsoft.com/updates/v2/?id=571047
[^6]: Generally Available: High-scale mesh in Azure Virtual Network Manager, https://azure.microsoft.com/updates/v2/?id=571572
[^7]: Public Preview: Foundry Routines in Foundry Agent Service, https://azure.microsoft.com/updates/v2/?id=563536
[^8]: Public Preview: Mdsv4 and Msv4 Series Virtual Machines for SAP, https://azure.microsoft.com/updates/v2/?id=571530
[^9]: Public Preview: Network egress controls for hosted agents in Microsoft Foundry, https://azure.microsoft.com/updates/v2/?id=571821
[^10]: Public Preview: Azure Payments HSM v2, https://azure.microsoft.com/updates/v2/?id=570509
[^11]: Public Preview: Azure SQL updates for mid-September 2026, https://azure.microsoft.com/updates/v2/?id=571056
[^12]: Public Preview: Azure Red Hat OpenShift with hosted control planes, https://azure.microsoft.com/updates/v2/?id=571621
[^13]: Public Preview: PostgreSQL skills and MCP plugin for Azure Database for PostgreSQL, https://azure.microsoft.com/updates/v2/?id=569664
[^14]: Public Preview: HTTP/3 over QUIC support in Azure Application Gateway, https://azure.microsoft.com/updates/v2/?id=571123
[^15]: Retirement Update: SAP container images removed October 14, 2026, https://azure.microsoft.com/updates/v2/?id=571342
[^16]: Announcing: New Windows App client-side endpoints for Azure Virtual Desktop, https://azure.microsoft.com/updates/v2/?id=571360
