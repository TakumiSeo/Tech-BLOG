Title: Azure Update (2026/09/21 - 2026/09/30)
Date: 2026-09-30
Slug: azure-update-2026-09-30
Lang: ja-jp
Category: notebook
Tags: azure, azure-arc, azure-backup, azure-container-apps, azure-communication-services, azure-database-for-postgresql, azure-disk-storage, azure-elastic-san, azure-extended-zones, azure-functions, azure-horizondb, azure-iot-central, azure-kubernetes-service, azure-netapp-files, azure-sphere, azure-sql-database, azure-sql-managed-instance, azure-update, dotnet, ga, node-js, powershell, public-preview, retirement, sql-server, virtual-machines, visual-studio-code
Summary: 2026年9月21日〜9月30日の Azure Update まとめ。GA 21件、パブリックプレビュー 15件、リタイア 8件の計44件。

2026年9月21日〜9月30日に発表された Azure Update のまとめです。

## GA

1. **Storage optimized Lasv5 and Laosv5 Azure VM series**[^1] - ストレージ最適化 Lasv5 および Laosv5 Azure VM シリーズが一般提供開始。
2. **Azure Arc-enabled SQL Server in Germany West Central**[^2] - Azure Arc 対応 SQL Server がドイツ西中部リージョンで利用可能に。
3. **Azure Arc-enabled SQL Server Available in Italy North**[^3] - Azure Arc 対応 SQL Server がイタリア北部リージョンで利用可能に。
4. **Azure SQL updates for late-September 2026**[^4] - Azure SQL Database の2026年9月下旬アップデート。
5. **Azure Database for PostgreSQL Flexible Server supports cross-tenant customer-managed keys (CMK)**[^5] - Azure Database for PostgreSQL フレキシブルサーバーがクロステナントのカスタマーマネージドキー (CMK) をサポート。
6. **SQL Server on Azure Local Disconnected (ALDO)**[^6] - SQL Server on Azure Local Disconnected (ALDO) が一般提供開始。
7. **SQL Server support on Azure Local connected mode**[^7] - Azure Local 接続モードでの SQL Server サポートが一般提供開始。
8. **Database DevOps in SSMS powered by SQL projects**[^8] - SQL プロジェクトを活用した SSMS でのデータベース DevOps が一般提供開始。
9. **SQL Formatter**[^9] - SQL Formatter が一般提供開始。
10. **SQL Migration Agent Skills for assessment, migration, and validation**[^10] - 評価・移行・検証のための SQL Migration Agent Skills が一般提供開始。
11. **Support for large volume breakthrough mode**[^11] - Azure NetApp Files の大容量ボリューム ブレークスルーモードのサポートが一般提供開始。
12. **Storage with cool access enhancement**[^12] - Azure NetApp Files のクールアクセス強化によるストレージが一般提供開始。
13. **Vector search and vector indexes in Azure SQL**[^13] - Azure SQL でのベクトル検索およびベクトルインデックスが一般提供開始。
14. **Azure SQL Managed Instance updates for late-September 2026**[^14] - Azure SQL Managed Instance の2026年9月下旬アップデート。
15. **Luxembourg - Azure Extended Zones**[^15] - ルクセンブルクが Azure Extended Zones として一般提供開始。
16. **Azure Backup for Elastic SAN**[^16] - Azure Elastic SAN 向け Azure Backup が一般提供開始。
17. **Instant Access for VM restore points**[^17] - VM 復元ポイントのインスタントアクセスが一般提供開始。
18. **Azure Container Apps Sandboxes**[^18] - Azure Container Apps Sandboxes が一般提供開始。
19. **Azure Container Apps Express**[^19] - Azure Container Apps Express が一般提供開始。
20. **Azure Sphere OS version 26.09**[^20] - Azure Sphere OS バージョン 26.09 が一般提供開始。
21. **Azure Functions support for PowerShell 7.6**[^21] - Azure Functions での PowerShell 7.6 サポートが一般提供開始。

## パブリックプレビュー

1. **Automatic Zone Placement for Virtual Machine Scale Sets**[^22] - Virtual Machine Scale Sets の自動ゾーン配置がパブリックプレビュー。
2. **Azure Database for PostgreSQL Ultra Disk**[^23] - Azure Database for PostgreSQL の Ultra Disk サポートがパブリックプレビュー。
3. **SQL Performance Monitoring for Azure SQL Database**[^24] - Azure SQL Database の SQL パフォーマンス監視がパブリックプレビュー。
4. **Performance monitoring for Azure Arc-enabled SQL Server**[^25] - Azure Arc 対応 SQL Server のパフォーマンス監視がパブリックプレビュー。
5. **Script-based deployment for SQL Server on Linux Azure VM**[^26] - Linux Azure VM 上の SQL Server のスクリプトベースデプロイがパブリックプレビュー。
6. **Azure SQL updates for late-September 2026**[^27] - Azure SQL の2026年9月下旬プレビューアップデート。
7. **Azure SQL Database Hyperscale Serverless auto-pause and auto-resume**[^28] - Azure SQL Database Hyperscale Serverless の自動一時停止・自動再開がパブリックプレビュー。
8. **Migrate directly from Azure Arc to Azure SQL Database, including Hyperscale**[^29] - Azure Arc から Azure SQL Database（Hyperscale 含む）への直接移行がパブリックプレビュー。
9. **Microsoft SQL Agent Skills**[^30] - Microsoft SQL Agent Skills がパブリックプレビュー。
10. **Long-term retention (LTR) v2 for Azure Database for PostgreSQL**[^31] - Azure Database for PostgreSQL の長期保持 (LTR) v2 がパブリックプレビュー。
11. **Microsoft Entra Kerberos authentication for Azure NetApp Files**[^32] - Azure NetApp Files の Microsoft Entra Kerberos 認証がパブリックプレビュー。
12. **Azure SQL Dev Hub**[^33] - Azure SQL Dev Hub がパブリックプレビュー。
13. **Azure HorizonDB supports PostgreSQL 18**[^34] - Azure HorizonDB が PostgreSQL 18 をサポート（パブリックプレビュー）。
14. **Flex Nodes for AKS**[^35] - AKS の Flex Nodes がパブリックプレビュー。
15. **Introducing a Guided Copilot Experience for Building Azure Apps in VS Code**[^36] - VS Code での Azure アプリ構築向けガイド付き Copilot エクスペリエンスがパブリックプレビュー。

## リタイア

1. **Azure Functions v1 hosting model on Azure Container Apps**[^37] - Azure Container Apps 上の Azure Functions v1 ホスティングモデルが廃止予定。
2. **Azure Arc enabled System Center Virtual Machine Manager will be retired September 30, 2029**[^38] - Azure Arc 対応 System Center Virtual Machine Manager が2029年9月30日に廃止予定。
3. **Microsoft HPC Pack**[^39] - Microsoft HPC Pack が廃止予定。
4. **Azure IoT Central will be retired on September 20, 2029**[^40] - Azure IoT Central が2029年9月20日に廃止予定。
5. **Azure Communication Services (ACS) standalone services will be retired on September 30, 2028**[^41] - Azure Communication Services (ACS) スタンドアロンサービスが2028年9月30日に廃止予定。
6. **Support for PowerShell 7.4 ends on November 10, 2026**[^42] - PowerShell 7.4 のサポートが2026年11月10日に終了。
7. **Support for .NET 8 and .NET 9 ends on November 10, 2026**[^43] - .NET 8 および .NET 9 のサポートが2026年11月10日に終了。Azure Functions アプリを .NET 10 にアップグレードが必要。
8. **Support for Node.js 22 ends on April 30, 2027**[^44] - Node.js 22 のサポートが2027年4月30日に終了。

[^1]: Storage optimized Lasv5 and Laosv5 Azure VM series, https://azure.microsoft.com/updates/572630/
[^2]: Azure Arc-enabled SQL Server in Germany West Central, https://azure.microsoft.com/updates/570696/
[^3]: Azure Arc-enabled SQL Server Available in Italy North, https://azure.microsoft.com/updates/570763/
[^4]: Azure SQL updates for late-September 2026, https://azure.microsoft.com/updates/571643/
[^5]: Azure Database for PostgreSQL Flexible Server supports cross-tenant customer-managed keys (CMK), https://azure.microsoft.com/updates/571783/
[^6]: SQL Server on Azure Local Disconnected (ALDO), https://azure.microsoft.com/updates/571836/
[^7]: SQL Server support on Azure Local connected mode, https://azure.microsoft.com/updates/571841/
[^8]: Database DevOps in SSMS powered by SQL projects, https://azure.microsoft.com/updates/571852/
[^9]: SQL Formatter, https://azure.microsoft.com/updates/571872/
[^10]: SQL Migration Agent Skills for assessment, migration, and validation, https://azure.microsoft.com/updates/571899/
[^11]: Support for large volume breakthrough mode, https://azure.microsoft.com/updates/573027/
[^12]: Storage with cool access enhancement, https://azure.microsoft.com/updates/573032/
[^13]: Vector search and vector indexes in Azure SQL, https://azure.microsoft.com/updates/571800/
[^14]: Azure SQL Managed Instance updates for late-September 2026, https://azure.microsoft.com/updates/571632/
[^15]: Luxembourg - Azure Extended Zones, https://azure.microsoft.com/updates/572968/
[^16]: Azure Backup for Elastic SAN, https://azure.microsoft.com/updates/494438/
[^17]: Instant Access for VM restore points, https://azure.microsoft.com/updates/572573/
[^18]: Azure Container Apps Sandboxes, https://azure.microsoft.com/updates/561262/
[^19]: Azure Container Apps Express, https://azure.microsoft.com/updates/559242/
[^20]: Azure Sphere OS version 26.09, https://azure.microsoft.com/updates/572579/
[^21]: Azure Functions support for PowerShell 7.6, https://azure.microsoft.com/updates/572219/
[^22]: Automatic Zone Placement for Virtual Machine Scale Sets, https://azure.microsoft.com/updates/571075/
[^23]: Azure Database for PostgreSQL Ultra Disk, https://azure.microsoft.com/updates/571909/
[^24]: SQL Performance Monitoring for Azure SQL Database, https://azure.microsoft.com/updates/571867/
[^25]: Performance monitoring for Azure Arc-enabled SQL Server, https://azure.microsoft.com/updates/571904/
[^26]: Script-based deployment for SQL Server on Linux Azure VM, https://azure.microsoft.com/updates/571810/
[^27]: Azure SQL updates for late-September 2026, https://azure.microsoft.com/updates/571846/
[^28]: Azure SQL Database Hyperscale Serverless auto-pause and auto-resume, https://azure.microsoft.com/updates/571857/
[^29]: Migrate directly from Azure Arc to Azure SQL Database including Hyperscale, https://azure.microsoft.com/updates/571795/
[^30]: Microsoft SQL Agent Skills, https://azure.microsoft.com/updates/573003/
[^31]: Long-term retention (LTR) v2 for Azure Database for PostgreSQL, https://azure.microsoft.com/updates/571914/
[^32]: Microsoft Entra Kerberos authentication for Azure NetApp Files, https://azure.microsoft.com/updates/573041/
[^33]: Azure SQL Dev Hub, https://azure.microsoft.com/updates/572998/
[^34]: Azure HorizonDB supports PostgreSQL 18, https://azure.microsoft.com/updates/573048/
[^35]: Flex Nodes for AKS, https://azure.microsoft.com/updates/571919/
[^36]: Introducing a Guided Copilot Experience for Building Azure Apps in VS Code, https://azure.microsoft.com/updates/572214/
[^37]: Azure Functions v1 hosting model on Azure Container Apps, https://azure.microsoft.com/updates/570800/
[^38]: Azure Arc enabled System Center Virtual Machine Manager retirement, https://azure.microsoft.com/updates/570283/
[^39]: Microsoft HPC Pack, https://azure.microsoft.com/updates/570046/
[^40]: Azure IoT Central retirement, https://azure.microsoft.com/updates/569914/
[^41]: Azure Communication Services (ACS) standalone services retirement, https://azure.microsoft.com/updates/557117/
[^42]: Support for PowerShell 7.4 ends on November 10, 2026, https://azure.microsoft.com/updates/572770/
[^43]: Support for .NET 8 and .NET 9 ends on November 10, 2026, https://azure.microsoft.com/updates/572838/
[^44]: Support for Node.js 22 ends on April 30, 2027, https://azure.microsoft.com/updates/572771/
