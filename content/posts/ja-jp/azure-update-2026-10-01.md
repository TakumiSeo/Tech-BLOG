Title: Azure Update (2026/09/22 - 2026/10/01)
Date: 2026-10-01
Slug: azure-update-2026-10-01
Lang: ja-jp
Category: notebook
Tags: azure, azure-arc, azure-backup, azure-communication-services, azure-container-apps, azure-copilot, azure-database-for-postgresql, azure-disk-storage, azure-elastic-san, azure-extended-zones, azure-functions, azure-horizondb, azure-iot-central, azure-kubernetes-service, azure-monitor, azure-netapp-files, azure-sql-database, azure-sql-managed-instance, azure-update, application-insights, dotnet, ga, node-js, powershell, public-preview, retirement, sql-server, virtual-machines
Summary: 2026年9月22日〜10月1日の Azure Update まとめ。GA 19件、パブリックプレビュー 16件、リタイア 12件、その他 1件の計48件。

本記事は Azure Updates の週次まとめです（対象期間: 2026年9月22日〜10月1日）。

## GA（一般提供）: 19件

1. **Storage optimized Lasv5 and Laosv5 Azure VM series** — ストレージ最適化 Lasv5 / Laosv5 Azure VM シリーズが一般提供開始[^1]。
2. **Azure Arc-enabled SQL Server in Germany West Central** — Azure Arc 対応 SQL Server がドイツ中西部で利用可能に[^2]。
3. **Azure Arc-enabled SQL Server Available in Italy North** — Azure Arc 対応 SQL Server がイタリア北部で利用可能に[^3]。
4. **Azure SQL updates for late-September 2026** — Azure SQL Database の 2026年9月下旬アップデート（GA）[^4]。
5. **Azure Database for PostgreSQL Flexible Server supports cross-tenant CMK** — Azure Database for PostgreSQL Flexible Server がクロステナントのカスタマーマネージドキー（CMK）に対応[^5]。
6. **SQL Server on Azure Local Disconnected (ALDO)** — SQL Server on Azure Local Disconnected（ALDO）が一般提供開始[^6]。
7. **SQL Server support on Azure Local connected mode** — SQL Server が Azure Local 接続モードで利用可能に[^7]。
8. **Database DevOps in SSMS powered by SQL projects** — SSMS で SQL プロジェクトを活用した Database DevOps が一般提供開始[^8]。
9. **SQL Formatter** — SQL Formatter が一般提供開始[^9]。
10. **SQL Migration Agent Skills** — SQL Migration Agent Skills（評価・移行・検証）が一般提供開始[^10]。
11. **Support for large volume breakthrough mode** — Azure NetApp Files で大容量ボリュームのブレークスルーモードをサポート[^11]。
12. **Storage with cool access enhancement** — Azure NetApp Files のクールアクセスストレージ強化が一般提供開始[^12]。
13. **Vector search and vector indexes in Azure SQL** — Azure SQL でベクトル検索およびベクトルインデックスが一般提供開始[^13]。
14. **Azure SQL Managed Instance updates for late-September 2026** — Azure SQL Managed Instance の 2026年9月下旬アップデート[^14]。
15. **Luxembourg - Azure Extended Zones** — ルクセンブルクが Azure Extended Zones として利用可能に[^15]。
16. **Azure Backup for Elastic SAN** — Azure Backup が Elastic SAN に対応し一般提供開始[^16]。
17. **Instant Access for VM restore points** — VM 復元ポイントのインスタントアクセスが一般提供開始[^17]。
18. **Azure Container Apps Sandboxes** — Azure Container Apps Sandboxes が一般提供開始[^18]。
19. **Azure Container Apps Express** — Azure Container Apps Express が一般提供開始[^19]。

## パブリックプレビュー: 16件

1. **SQL performance monitoring for SQL Server on Azure Virtual Machines** — SQL Server on Azure Virtual Machines 向け SQL パフォーマンスモニタリングがパブリックプレビュー[^20]。
2. **Ubuntu 26.04 support in AKS** — AKS で Ubuntu 26.04 サポートがパブリックプレビュー[^21]。
3. **Automatic Zone Placement for Virtual Machine Scale Sets** — Virtual Machine Scale Sets の自動ゾーン配置がパブリックプレビュー[^22]。
4. **Azure Database for PostgreSQL Ultra Disk** — Azure Database for PostgreSQL で Ultra Disk がパブリックプレビュー[^23]。
5. **SQL Performance Monitoring for Azure SQL Database** — Azure SQL Database の SQL パフォーマンスモニタリングがパブリックプレビュー[^24]。
6. **Performance monitoring for Azure Arc-enabled SQL Server** — Azure Arc 対応 SQL Server のパフォーマンスモニタリングがパブリックプレビュー[^25]。
7. **Script-based deployment for SQL Server on Linux Azure VM** — Linux Azure VM 上の SQL Server のスクリプトベースデプロイがパブリックプレビュー[^26]。
8. **Azure SQL updates for late-September 2026 (Preview)** — Azure SQL の 2026年9月下旬アップデート（プレビュー）[^27]。
9. **Azure SQL Database Hyperscale Serverless auto-pause and auto-resume** — Azure SQL Database Hyperscale Serverless の自動一時停止/自動再開がパブリックプレビュー[^28]。
10. **Migrate directly from Azure Arc to Azure SQL Database, including Hyperscale** — Azure Arc から Azure SQL Database（Hyperscale 含む）への直接移行がパブリックプレビュー[^29]。
11. **Microsoft SQL Agent Skills** — Microsoft SQL Agent Skills がパブリックプレビュー[^30]。
12. **Long-term retention (LTR) v2 for Azure Database for PostgreSQL** — Azure Database for PostgreSQL の長期保持（LTR）v2 がパブリックプレビュー[^31]。
13. **Microsoft Entra Kerberos authentication for Azure NetApp Files** — Azure NetApp Files で Microsoft Entra Kerberos 認証がパブリックプレビュー[^32]。
14. **Azure SQL Dev Hub** — Azure SQL Dev Hub がパブリックプレビュー[^33]。
15. **Azure HorizonDB supports PostgreSQL 18** — Azure HorizonDB が PostgreSQL 18 をサポート（パブリックプレビュー）[^34]。
16. **Flex Nodes for AKS** — AKS 向け Flex Nodes がパブリックプレビュー[^35]。

## リタイア: 12件

1. **NVv3-series Azure Virtual Machines** — NVv3 シリーズ Azure Virtual Machines のリタイア[^36]。
2. **NVv4-series Azure Virtual Machines** — NVv4 シリーズ Azure Virtual Machines のリタイア[^37]。
3. **Dv3, Dsv3, Ev3, and Esv3 Azure VMs** — Dv3 / Dsv3 / Ev3 / Esv3 シリーズ Azure VM のリタイア[^38]。
4. **Azure Monitor Application Insights single-step availability testing** — Azure Monitor Application Insights のシングルステップ可用性テストが 2028年9月30日にリタイア[^39]。
5. **Azure Functions v1 hosting model on Azure Container Apps** — Azure Container Apps 上の Azure Functions v1 ホスティングモデルがリタイア[^40]。
6. **Azure Arc enabled System Center Virtual Machine Manager** — Azure Arc 対応 System Center Virtual Machine Manager が 2029年9月30日にリタイア[^41]。
7. **Microsoft HPC Pack** — Microsoft HPC Pack がリタイア[^42]。
8. **Azure IoT Central** — Azure IoT Central が 2029年9月20日にリタイア[^43]。
9. **Azure Communication Services (ACS) standalone services** — Azure Communication Services（ACS）スタンドアロンサービスが 2028年9月30日にリタイア[^44]。
10. **Support for PowerShell 7.4 ends on November 10, 2026** — PowerShell 7.4 のサポートが 2026年11月10日に終了[^45]。
11. **Support for .NET 8 and .NET 9 ends on November 10, 2026** — .NET 8 / .NET 9 のサポートが 2026年11月10日に終了。.NET 10 へのアップグレードを推奨[^46]。
12. **Support for Node.js 22 ends on April 30, 2027** — Node.js 22 のサポートが 2027年4月30日に終了[^47]。

## その他: 1件

1. **Azure canvases for GitHub Copilot** — GitHub Copilot 向けの Azure Canvases が発表[^48]。

[^1]: Generally Available: Storage optimized Lasv5 and Laosv5 Azure VM series, https://azure.microsoft.com/updates/v2/storage-optimized-lasv5-and-laosv5-azure-vm-series
[^2]: Generally Available: Azure Arc-enabled SQL Server in Germany West Central, https://azure.microsoft.com/updates/v2/Azure-Arc-enabled-SQL-Server-in-Germany-West-Central
[^3]: Generally Available: Azure Arc-enabled SQL Server Available in Italy North, https://azure.microsoft.com/updates/v2/Azure-Arc-enabled-SQL-Server-Available-in-Italy-North
[^4]: Generally Available: Azure SQL updates for late-September 2026, https://azure.microsoft.com/updates/v2/Azure-SQL-updates-for-late-September-2026
[^5]: Generally Available: Azure Database for PostgreSQL Flexible Server supports cross-tenant customer-managed keys (CMK), https://azure.microsoft.com/updates/v2/Azure-Database-for-PostgreSQL-Flexible-Server-supports-cross-tenant-customer-managed-keys-CMK
[^6]: Generally Available: SQL Server on Azure Local Disconnected (ALDO), https://azure.microsoft.com/updates/v2/SQL-Server-on-Azure-Local-Disconnected-ALDO
[^7]: Generally Available: SQL Server support on Azure Local connected mode, https://azure.microsoft.com/updates/v2/SQL-Server-support-on-Azure-Local-connected-mode
[^8]: Generally Available: Database DevOps in SSMS powered by SQL projects, https://azure.microsoft.com/updates/v2/Database-DevOps-in-SSMS-powered-by-SQL-projects
[^9]: Generally Available: SQL Formatter, https://azure.microsoft.com/updates/v2/SQL-Formatter
[^10]: Generally Available: SQL Migration Agent Skills for assessment, migration, and validation, https://azure.microsoft.com/updates/v2/SQL-Migration-Agent-Skills-for-assessment-migration-and-validation
[^11]: Generally Available: Support for large volume breakthrough mode, https://azure.microsoft.com/updates/v2/Support-for-large-volume-breakthrough-mode
[^12]: Generally Available: Storage with cool access enhancement, https://azure.microsoft.com/updates/v2/Storage-with-cool-access-enhancement
[^13]: Generally Available: Vector search and vector indexes in Azure SQL, https://azure.microsoft.com/updates/v2/vector-search-and-vector-indexes-in-azure-sql
[^14]: Generally Available: Azure SQL Managed Instance updates for late-September 2026, https://azure.microsoft.com/updates/v2/Azure-SQL-Managed-Instance-updates-for-late-September-2026
[^15]: Generally Available: Luxembourg - Azure Extended Zones, https://azure.microsoft.com/updates/v2/Luxembourg-Azure-Extended-Zones
[^16]: Generally Available: Azure Backup for Elastic SAN, https://azure.microsoft.com/updates/v2/Azure-Backup-for-Elastic-SAN
[^17]: Generally Available: Instant Access for VM restore points, https://azure.microsoft.com/updates/v2/Instant-Access-for-VM-restore-points
[^18]: Generally Available: Azure Container Apps Sandboxes, https://azure.microsoft.com/updates/v2/Azure-Container-Apps-Sandboxes
[^19]: Generally Available: Azure Container Apps Express, https://azure.microsoft.com/updates/v2/Azure-Container-Apps-Express
[^20]: Public Preview: SQL performance monitoring for SQL Server on Azure Virtual Machines, https://azure.microsoft.com/updates/v2/SQL-performance-monitoring-for-SQL-Server-on-Azure-Virtual-Machines
[^21]: Public Preview: Ubuntu 26.04 support in AKS, https://azure.microsoft.com/updates/v2/Ubuntu-26-04-support-in-AKS
[^22]: Public Preview: Automatic Zone Placement for Virtual Machine Scale Sets, https://azure.microsoft.com/updates/v2/Automatic-Zone-Placement-for-Virtual-Machine-Scale-Sets
[^23]: Public Preview: Azure Database for PostgreSQL Ultra Disk, https://azure.microsoft.com/updates/v2/Azure-Database-for-PostgreSQL-Ultra-Disk
[^24]: Public Preview: SQL Performance Monitoring for Azure SQL Database, https://azure.microsoft.com/updates/v2/SQL-Performance-Monitoring-for-Azure-SQL-Database
[^25]: Public Preview: Performance monitoring for Azure Arc–enabled SQL Server, https://azure.microsoft.com/updates/v2/Performance-monitoring-for-Azure-Arc-enabled-SQL-Server
[^26]: Public preview: Script-based deployment for SQL Server on Linux Azure VM, https://azure.microsoft.com/updates/v2/Script-based-deployment-for-SQL-Server-on-Linux-Azure-VM
[^27]: Public Preview: Azure SQL updates for late-September 2026, https://azure.microsoft.com/updates/v2/Azure-SQL-updates-for-late-September-2026-Preview
[^28]: Public Preview: Azure SQL Database Hyperscale Serverless auto-pause and auto-resume, https://azure.microsoft.com/updates/v2/Azure-SQL-Database-Hyperscale-Serverless-auto-pause-and-auto-resume
[^29]: Public Preview: Migrate directly from Azure Arc to Azure SQL Database, including Hyperscale, https://azure.microsoft.com/updates/v2/Migrate-directly-from-Azure-Arc-to-Azure-SQL-Database-including-Hyperscale
[^30]: Public Preview: Microsoft SQL Agent Skills, https://azure.microsoft.com/updates/v2/Microsoft-SQL-Agent-Skills
[^31]: Public Preview: Long-term retention (LTR) v2 for Azure Database for PostgreSQL, https://azure.microsoft.com/updates/v2/Long-term-retention-LTR-v2-for-Azure-Database-for-PostgreSQL
[^32]: Public Preview: Microsoft entra kerberos authentication for Azure NetApp Files, https://azure.microsoft.com/updates/v2/Microsoft-entra-kerberos-authentication-for-Azure-NetApp-Files
[^33]: Public Preview: Azure SQL Dev Hub, https://azure.microsoft.com/updates/v2/Azure-SQL-Dev-Hub
[^34]: Public Preview: Azure HorizonDB supports PostgreSQL 18, https://azure.microsoft.com/updates/v2/Azure-HorizonDB-supports-PostgreSQL-18
[^35]: Public Preview: Flex Nodes for AKS, https://azure.microsoft.com/updates/v2/Flex-Nodes-for-AKS
[^36]: Retirement: NVv3-series Azure Virtual Machines, https://azure.microsoft.com/updates/v2/NVv3-series-Azure-Virtual-Machines
[^37]: Retirement: NVv4-series Azure Virtual Machines, https://azure.microsoft.com/updates/v2/NVv4-series-Azure-Virtual-Machines
[^38]: Retirement: Dv3, Dsv3, Ev3, and Esv3 Azure VMs, https://azure.microsoft.com/updates/v2/Dv3-Dsv3-Ev3-and-Esv3-Azure-VMs
[^39]: Retirement: Transition to using standard tests for single-step availability testing in Azure Monitor application insights by September 30, 2028, https://azure.microsoft.com/updates/v2/transition-to-using-standard-tests-for-singlestep-availability-testing-in-azure-monitor-application-insights-by-30-september
[^40]: Retirement: Azure Functions v1 hosting model on Azure Container Apps, https://azure.microsoft.com/updates/v2/Azure-Functions-v1-hosting-model-on-Azure-Container-Apps
[^41]: Retirement: Azure Arc enabled System Center Virtual Machine Manager will be retired September 30, 2029, https://azure.microsoft.com/updates/v2/Azure-Arc-enabled-System-Center-Virtual-Machine-Manager-will-be-retired-September-30-2029
[^42]: Retirement: Microsoft HPC Pack, https://azure.microsoft.com/updates/v2/Microsoft-HPC-Pack
[^43]: Retirement: Azure IoT Central will be retired on September 20, 2029, https://azure.microsoft.com/updates/v2/Azure-IoT-Central-will-be-retired-on-September-20-2029
[^44]: Retirement: Azure Communication Services (ACS) standalone services will be retired on September 30, 2028, https://azure.microsoft.com/updates/v2/Azure-Communication-Services-ACS-standalone-services-will-be-retired-on-September-30-2028
[^45]: Retirement: Support for PowerShell 7.4 ends on November 10, 2026, https://azure.microsoft.com/updates/v2/Support-for-PowerShell-7-4-ends-on-November-10-2026
[^46]: Retirement: Support for .NET 8 and .NET 9 ends on November 10, 2026—upgrade your apps to .NET 10, https://azure.microsoft.com/updates/v2/Support-for-NET-8-and-NET-9-ends-on-November-10-2026-upgrade-your-apps-to-NET-10
[^47]: Retirement: Support for Node.js 22 ends on April 30, 2027, https://azure.microsoft.com/updates/v2/Support-for-Node-js-22-ends-on-April-30-2027
[^48]: Announcing: Azure canvases for GitHub Copilot, https://azure.microsoft.com/updates/v2/Azure-canvases-for-GitHub-Copilot
