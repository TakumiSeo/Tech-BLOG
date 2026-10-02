Title: Azure Update (2026/09/23 - 2026/10/02)
Date: 2026-10-02
Slug: azure-update-2026-10-02
Lang: ja-jp
Category: notebook
Tags: azure, application-insights, azure-arc, azure-backup, azure-communication-services, azure-container-apps, azure-copilot, azure-database-for-mysql, azure-database-for-postgresql, azure-disk-storage, azure-elastic-san, azure-extended-zones, azure-functions, azure-horizondb, azure-iot-central, azure-kubernetes-service, azure-monitor, azure-netapp-files, azure-sql-database, azure-sql-managed-instance, azure-update, dotnet, ga, powershell, public-preview, retirement, sql-server, virtual-machines
Summary: 2026年9月23日〜10月2日の Azure Update まとめ。GA 19件、パブリックプレビュー 16件、リタイア 12件、その他 1件の計48件。

本記事は、2026年9月23日〜10月2日における Azure Update の内容をまとめたものです。

## 一般提供開始（GA）- 19件

1. **Generally Available: Azure Arc-enabled SQL Server Available in Italy North** — Azure Arc 対応 SQL Server が Italy North リージョンで利用可能に[^1]。
2. **Generally Available: Azure Arc-enabled SQL Server in Germany West Central** — Azure Arc 対応 SQL Server が Germany West Central リージョンで利用可能に[^2]。
3. **Generally Available: Azure Backup for Elastic SAN** — Azure Elastic SAN 向けの Azure Backup が一般提供開始[^3]。
4. **Generally Available: Azure Container Apps Express** — Azure Container Apps Express が一般提供開始[^4]。
5. **Generally Available: Azure Container Apps Sandboxes** — Azure Container Apps Sandboxes が一般提供開始[^5]。
6. **Generally Available: Azure Database for PostgreSQL Flexible Server supports cross-tenant customer-managed keys (CMK)** — Azure Database for PostgreSQL フレキシブルサーバーでクロステナントのカスタマーマネージドキー（CMK）をサポート[^6]。
7. **Generally Available: Azure SQL Managed Instance updates for late-September 2026** — Azure SQL Managed Instance の2026年9月後半アップデート[^7]。
8. **Generally Available: Azure SQL updates for late-September 2026** — Azure SQL Database の2026年9月後半アップデート[^8]。
9. **Generally Available: Database DevOps in SSMS powered by SQL projects** — SQL プロジェクトを活用した SSMS での Database DevOps が一般提供開始[^9]。
10. **Generally Available: Instant Access for VM restore points** — VM 復元ポイントの Instant Access が一般提供開始[^10]。
11. **Generally Available: Luxembourg - Azure Extended Zones** — ルクセンブルクの Azure Extended Zones が一般提供開始[^11]。
12. **Generally Available: SQL Formatter** — SQL Formatter が一般提供開始[^12]。
13. **Generally Available: SQL Migration Agent Skills for assessment, migration, and validation** — 評価・移行・検証向けの SQL Migration Agent Skills が一般提供開始[^13]。
14. **Generally Available: SQL Server on Azure Local Disconnected (ALDO)** — Azure Local 切断モードでの SQL Server（ALDO）が一般提供開始[^14]。
15. **Generally Available: SQL Server support on Azure Local connected mode** — Azure Local 接続モードでの SQL Server サポートが一般提供開始[^15]。
16. **Generally Available: Storage optimized Lasv5 and Laosv5 Azure VM series** — ストレージ最適化 Lasv5 および Laosv5 Azure VM シリーズが一般提供開始[^16]。
17. **Generally Available: Storage with cool access enhancement** — Azure NetApp Files のクールアクセス拡張が一般提供開始[^17]。
18. **Generally Available: Support for large volume breakthrough mode** — Azure NetApp Files の大容量ボリュームブレイクスルーモードが一般提供開始[^18]。
19. **Generally Available: Vector search and vector indexes in Azure SQL** — Azure SQL でのベクトル検索およびベクトルインデックスが一般提供開始[^19]。

## パブリックプレビュー - 16件

1. **Public Preview: Microsoft Entra Kerberos authentication for Azure NetApp Files** — Azure NetApp Files で Microsoft Entra Kerberos 認証がパブリックプレビュー[^20]。
2. **Public Preview: Automatic Zone Placement for Virtual Machine Scale Sets** — Virtual Machine Scale Sets の自動ゾーン配置がパブリックプレビュー[^21]。
3. **Public Preview: Azure Database for PostgreSQL Ultra Disk** — Azure Database for PostgreSQL の Ultra Disk サポートがパブリックプレビュー[^22]。
4. **Public Preview: Azure HorizonDB supports PostgreSQL 18** — Azure HorizonDB が PostgreSQL 18 をサポート（パブリックプレビュー）[^23]。
5. **Public Preview: Azure SQL Database Hyperscale Serverless auto-pause and auto-resume** — Azure SQL Database Hyperscale サーバーレスの自動一時停止・自動再開がパブリックプレビュー[^24]。
6. **Public Preview: Azure SQL Dev Hub** — Azure SQL Dev Hub がパブリックプレビュー[^25]。
7. **Public Preview: Azure SQL updates for late-September 2026** — Azure SQL の2026年9月後半アップデート（パブリックプレビュー機能）[^26]。
8. **Public Preview: Long-term retention (LTR) v2 for Azure Database for PostgreSQL** — Azure Database for PostgreSQL の長期保有（LTR）v2 がパブリックプレビュー[^27]。
9. **Public Preview: Microsoft SQL Agent Skills** — Microsoft SQL Agent Skills がパブリックプレビュー[^28]。
10. **Public Preview: Migrate directly from Azure Arc to Azure SQL Database, including Hyperscale** — Azure Arc から Azure SQL Database（Hyperscale 含む）への直接移行がパブリックプレビュー[^29]。
11. **Public Preview: Performance monitoring for Azure Arc–enabled SQL Server** — Azure Arc 対応 SQL Server のパフォーマンス監視がパブリックプレビュー[^30]。
12. **Public Preview: Reader Endpoint for Azure Database for MySQL** — Azure Database for MySQL の Reader Endpoint がパブリックプレビュー[^31]。
13. **Public Preview: SQL Performance Monitoring for Azure SQL Database** — Azure SQL Database の SQL パフォーマンス監視がパブリックプレビュー[^32]。
14. **Public Preview: SQL performance monitoring for SQL Server on Azure Virtual Machines** — Azure VM 上の SQL Server 向け SQL パフォーマンス監視がパブリックプレビュー[^33]。
15. **Public Preview: Ubuntu 26.04 support in AKS** — AKS で Ubuntu 26.04 サポートがパブリックプレビュー[^34]。
16. **Public Preview: Script-based deployment for SQL Server on Linux Azure VM** — Linux Azure VM 上の SQL Server のスクリプトベースデプロイがパブリックプレビュー[^35]。

## リタイア - 12件

1. **Retirement: Azure Arc enabled System Center Virtual Machine Manager will be retired September 30, 2029** — Azure Arc 対応 System Center Virtual Machine Manager が2029年9月30日に廃止予定[^36]。
2. **Retirement: Azure Communication Services (ACS) standalone services will be retired on September 30, 2028** — Azure Communication Services のスタンドアロンサービスが2028年9月30日に廃止予定[^37]。
3. **Retirement: Azure IoT Central will be retired on September 20, 2029** — Azure IoT Central が2029年9月20日に廃止予定[^38]。
4. **Retirement: DCsv3 and DCdsv3-series Azure Virtual Machines will be retired on October 31, 2029** — DCsv3 および DCdsv3 シリーズの Azure VM が2029年10月31日に廃止予定[^39]。
5. **Retirement: Dv3, Dsv3, Ev3, and Esv3 Azure VMs** — Dv3、Dsv3、Ev3、Esv3 シリーズの Azure VM が廃止予定[^40]。
6. **Retirement: Functions on Azure Container Apps V1** — Azure Container Apps V1 上の Functions が廃止予定[^41]。
7. **Retirement: Microsoft HPC Pack** — Microsoft HPC Pack が廃止予定[^42]。
8. **Retirement: NVv3-series Azure Virtual Machines** — NVv3 シリーズの Azure VM が廃止予定[^43]。
9. **Retirement: NVv4-series Azure Virtual Machines** — NVv4 シリーズの Azure VM が廃止予定[^44]。
10. **Retirement: Support for .NET 8 and .NET 9 ends on November 10, 2026—upgrade your apps to .NET 10** — .NET 8 および .NET 9 のサポートが2026年11月10日に終了。.NET 10 へのアップグレードを推奨[^45]。
11. **Retirement: Support for PowerShell 7.4 ends on November 10, 2026** — PowerShell 7.4 のサポートが2026年11月10日に終了[^46]。
12. **Retirement: Transition to using standard tests for single-step availability testing in Azure Monitor Application Insights by September 30, 2028** — Azure Monitor Application Insights のシングルステップ可用性テストが2028年9月30日までに標準テストへ移行[^47]。

## その他 - 1件

1. **Announcing: Azure canvases for GitHub Copilot** — GitHub Copilot 向けの Azure canvases が発表[^48]。

[^1]: Generally Available: Azure Arc-enabled SQL Server Available in Italy North, https://azure.microsoft.com/updates/v2/Azure-Arc-enabled-SQL-Server-Available-in-Italy-North
[^2]: Generally Available: Azure Arc-enabled SQL Server in Germany West Central, https://azure.microsoft.com/updates/v2/Azure-Arc-enabled-SQL-Server-in-Germany-West-Central
[^3]: Generally Available: Azure Backup for Elastic SAN, https://azure.microsoft.com/updates/v2/Azure-Backup-for-Elastic-SAN
[^4]: Generally Available: Azure Container Apps Express, https://azure.microsoft.com/updates/v2/Azure-Container-Apps-Express
[^5]: Generally Available: Azure Container Apps Sandboxes, https://azure.microsoft.com/updates/v2/Azure-Container-Apps-Sandboxes
[^6]: Generally Available: Azure Database for PostgreSQL Flexible Server supports cross-tenant customer-managed keys (CMK), https://azure.microsoft.com/updates/v2/Azure-Database-for-PostgreSQL-Flexible-Server-supports-cross-tenant-CMK
[^7]: Generally Available: Azure SQL Managed Instance updates for late-September 2026, https://azure.microsoft.com/updates/v2/Azure-SQL-Managed-Instance-updates-for-late-September-2026
[^8]: Generally Available: Azure SQL updates for late-September 2026, https://azure.microsoft.com/updates/v2/Azure-SQL-updates-for-late-September-2026
[^9]: Generally Available: Database DevOps in SSMS powered by SQL projects, https://azure.microsoft.com/updates/v2/Database-DevOps-in-SSMS-powered-by-SQL-projects
[^10]: Generally Available: Instant Access for VM restore points, https://azure.microsoft.com/updates/v2/Instant-Access-for-VM-restore-points
[^11]: Generally Available: Luxembourg - Azure Extended Zones, https://azure.microsoft.com/updates/v2/Luxembourg-Azure-Extended-Zones
[^12]: Generally Available: SQL Formatter, https://azure.microsoft.com/updates/v2/SQL-Formatter
[^13]: Generally Available: SQL Migration Agent Skills for assessment, migration, and validation, https://azure.microsoft.com/updates/v2/SQL-Migration-Agent-Skills-for-assessment-migration-and-validation
[^14]: Generally Available: SQL Server on Azure Local Disconnected (ALDO), https://azure.microsoft.com/updates/v2/SQL-Server-on-Azure-Local-Disconnected-ALDO
[^15]: Generally Available: SQL Server support on Azure Local connected mode, https://azure.microsoft.com/updates/v2/SQL-Server-support-on-Azure-Local-connected-mode
[^16]: Generally Available: Storage optimized Lasv5 and Laosv5 Azure VM series, https://azure.microsoft.com/updates/v2/Storage-optimized-Lasv5-and-Laosv5-Azure-VM-series
[^17]: Generally Available: Storage with cool access enhancement, https://azure.microsoft.com/updates/v2/Storage-with-cool-access-enhancement
[^18]: Generally Available: Support for large volume breakthrough mode, https://azure.microsoft.com/updates/v2/Support-for-large-volume-breakthrough-mode
[^19]: Generally Available: Vector search and vector indexes in Azure SQL, https://azure.microsoft.com/updates/v2/Vector-search-and-vector-indexes-in-Azure-SQL
[^20]: Public Preview: Microsoft Entra Kerberos authentication for Azure NetApp Files, https://azure.microsoft.com/updates/v2/Microsoft-entra-kerberos-authentication-for-Azure-NetApp-Files
[^21]: Public Preview: Automatic Zone Placement for Virtual Machine Scale Sets, https://azure.microsoft.com/updates/v2/Automatic-Zone-Placement-for-Virtual-Machine-Scale-Sets
[^22]: Public Preview: Azure Database for PostgreSQL Ultra Disk, https://azure.microsoft.com/updates/v2/Azure-Database-for-PostgreSQL-Ultra-Disk
[^23]: Public Preview: Azure HorizonDB supports PostgreSQL 18, https://azure.microsoft.com/updates/v2/Azure-HorizonDB-supports-PostgreSQL-18
[^24]: Public Preview: Azure SQL Database Hyperscale Serverless auto-pause and auto-resume, https://azure.microsoft.com/updates/v2/Azure-SQL-Database-Hyperscale-Serverless-auto-pause-and-auto-resume
[^25]: Public Preview: Azure SQL Dev Hub, https://azure.microsoft.com/updates/v2/Azure-SQL-Dev-Hub
[^26]: Public Preview: Azure SQL updates for late-September 2026, https://azure.microsoft.com/updates/v2/Azure-SQL-updates-for-late-September-2026-2
[^27]: Public Preview: Long-term retention (LTR) v2 for Azure Database for PostgreSQL, https://azure.microsoft.com/updates/v2/Long-term-retention-LTR-v2-for-Azure-Database-for-PostgreSQL
[^28]: Public Preview: Microsoft SQL Agent Skills, https://azure.microsoft.com/updates/v2/Microsoft-SQL-Agent-Skills
[^29]: Public Preview: Migrate directly from Azure Arc to Azure SQL Database, including Hyperscale, https://azure.microsoft.com/updates/v2/Migrate-directly-from-Azure-Arc-to-Azure-SQL-Database-including-Hyperscale
[^30]: Public Preview: Performance monitoring for Azure Arc–enabled SQL Server, https://azure.microsoft.com/updates/v2/Performance-monitoring-for-Azure-Arc-enabled-SQL-Server
[^31]: Public Preview: Reader Endpoint for Azure Database for MySQL, https://azure.microsoft.com/updates/v2/Reader-Endpoint-for-Azure-Database-for-MySQL
[^32]: Public Preview: SQL Performance Monitoring for Azure SQL Database, https://azure.microsoft.com/updates/v2/SQL-Performance-Monitoring-for-Azure-SQL-Database
[^33]: Public Preview: SQL performance monitoring for SQL Server on Azure Virtual Machines, https://azure.microsoft.com/updates/v2/SQL-performance-monitoring-for-SQL-Server-on-Azure-Virtual-Machines
[^34]: Public Preview: Ubuntu 26.04 support in AKS, https://azure.microsoft.com/updates/v2/Ubuntu-2604-support-in-AKS
[^35]: Public Preview: Script-based deployment for SQL Server on Linux Azure VM, https://azure.microsoft.com/updates/v2/Script-based-deployment-for-SQL-Server-on-Linux-Azure-VM
[^36]: Retirement: Azure Arc enabled System Center Virtual Machine Manager will be retired September 30, 2029, https://azure.microsoft.com/updates/v2/Azure-Arc-enabled-System-Center-Virtual-Machine-Manager-will-be-retired-September-30-2029
[^37]: Retirement: Azure Communication Services (ACS) standalone services will be retired on September 30, 2028, https://azure.microsoft.com/updates/v2/Azure-Communication-Services-ACS-standalone-services-will-be-retired-on-September-30-2028
[^38]: Retirement: Azure IoT Central will be retired on September 20, 2029, https://azure.microsoft.com/updates/v2/Azure-IoT-Central-will-be-retired-on-September-20-2029
[^39]: Retirement: DCsv3 and DCdsv3-series Azure Virtual Machines will be retired on October 31, 2029, https://azure.microsoft.com/updates/v2/DCsv3-and-DCdsv3-series-Azure-Virtual-Machines-will-be-retired-on-October-31-2029
[^40]: Retirement: Dv3, Dsv3, Ev3, and Esv3 Azure VMs, https://azure.microsoft.com/updates/v2/Dv3-Dsv3-Ev3-and-Esv3-Azure-VMs
[^41]: Retirement: Functions on Azure Container Apps V1, https://azure.microsoft.com/updates/v2/Functions-on-Azure-Container-Apps-V1
[^42]: Retirement: Microsoft HPC Pack, https://azure.microsoft.com/updates/v2/Microsoft-HPC-Pack
[^43]: Retirement: NVv3-series Azure Virtual Machines, https://azure.microsoft.com/updates/v2/NVv3-series-Azure-Virtual-Machines
[^44]: Retirement: NVv4-series Azure Virtual Machines, https://azure.microsoft.com/updates/v2/NVv4-series-Azure-Virtual-Machines
[^45]: Retirement: Support for .NET 8 and .NET 9 ends on November 10, 2026—upgrade your apps to .NET 10, https://azure.microsoft.com/updates/v2/Support-for-NET-8-and-NET-9-ends-on-November-10-2026-upgrade-your-apps-to-NET-10
[^46]: Retirement: Support for PowerShell 7.4 ends on November 10, 2026, https://azure.microsoft.com/updates/v2/Support-for-PowerShell-74-ends-on-November-10-2026
[^47]: Retirement: Transition to using standard tests for single-step availability testing in Azure Monitor Application Insights by September 30, 2028, https://azure.microsoft.com/updates/v2/transition-to-using-standard-tests-for-singlestep-availability-testing-in-azure-monitor-application-insights-by-30-september
[^48]: Announcing: Azure canvases for GitHub Copilot, https://azure.microsoft.com/updates/v2/Azure-canvases-for-GitHub-Copilot
