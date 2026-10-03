Title: Azure Update (2026/09/24 - 2026/10/03)
Date: 2026-10-03
Slug: azure-update-2026-10-03
Lang: ja-jp
Category: notebook
Tags: application-insights, azure, azure-arc, azure-backup, azure-communication-services, azure-container-apps, azure-copilot, azure-database-for-mysql, azure-database-for-postgresql, azure-disk-storage, azure-elastic-san, azure-extended-zones, azure-horizondb, azure-iot-central, azure-kubernetes-service, azure-monitor, azure-netapp-files, azure-sql-database, azure-sql-managed-instance, azure-update, ga, public-preview, retirement, sql-server, virtual-machines
Summary: 2026年9月24日〜10月3日の Azure Update まとめ。GA 17件、パブリックプレビュー 17件、リタイア 10件、その他 1件の計45件。

2026年9月24日〜10月3日に更新された Azure Update の内容をまとめます。

## 一般提供開始 (GA) — 17件

1. Azure Arc 対応 SQL Server がイタリア北部リージョンで利用可能に[^1]
2. Azure Arc 対応 SQL Server がドイツ中西部リージョンで利用可能に[^2]
3. Azure Backup for Elastic SAN[^3]
4. Azure Database for PostgreSQL Flexible Server がクロステナントのカスタマー マネージド キー (CMK) をサポート[^4]
5. Azure SQL Managed Instance の2026年9月後半アップデート[^5]
6. Azure SQL の2026年9月後半アップデート[^6]
7. SSMS での SQL プロジェクトを活用した Database DevOps[^7]
8. VM 復元ポイントの Instant Access[^8]
9. Luxembourg — Azure Extended Zones[^9]
10. SQL Formatter[^10]
11. SQL Migration Agent Skills（アセスメント、移行、検証）[^11]
12. SQL Server on Azure Local Disconnected (ALDO)[^12]
13. SQL Server support on Azure Local 接続モード[^13]
14. ストレージ最適化 Lasv5 / Laosv5 Azure VM シリーズ[^14]
15. Azure NetApp Files のクールアクセス機能強化[^15]
16. Azure NetApp Files の大容量ボリュームブレークスルーモードサポート[^16]
17. Azure SQL のベクトル検索およびベクトルインデックス[^17]

## パブリックプレビュー — 17件

1. Azure NetApp Files の Microsoft Entra Kerberos 認証[^18]
2. Azure Database for PostgreSQL エラスティック クラスターのメジャーバージョンアップグレード (MVU)[^19]
3. Virtual Machine Scale Sets の自動ゾーン配置[^20]
4. Azure Database for PostgreSQL Ultra Disk[^21]
5. Azure HorizonDB が PostgreSQL 18 をサポート[^22]
6. Azure SQL Database Hyperscale Serverless の自動一時停止と自動再開[^23]
7. Azure SQL Dev Hub[^24]
8. Azure SQL の2026年9月後半アップデート（プレビュー）[^25]
9. Azure Database for PostgreSQL の長期リテンション (LTR) v2[^26]
10. Microsoft SQL Agent Skills[^27]
11. Azure Arc から Azure SQL Database (Hyperscale 含む) への直接移行[^28]
12. Azure Arc 対応 SQL Server のパフォーマンス監視[^29]
13. Azure Database for MySQL の Reader Endpoint[^30]
14. Linux Azure VM 上の SQL Server のスクリプトベース デプロイ[^31]
15. Azure SQL Database の SQL Performance Monitoring[^32]
16. SQL Server on Azure Virtual Machines の SQL パフォーマンス監視[^33]
17. AKS での Ubuntu 26.04 サポート[^34]

## リタイア — 10件

1. Azure Arc 対応 System Center Virtual Machine Manager は2029年9月30日に廃止[^35]
2. Azure Communication Services (ACS) スタンドアロン サービスは2028年9月30日に廃止[^36]
3. Azure IoT Central は2029年9月20日に廃止[^37]
4. DCsv3 / DCdsv3 シリーズ Azure Virtual Machines は2029年10月31日に廃止[^38]
5. Dv3, Dsv3, Ev3, Esv3 Azure VM シリーズの廃止[^39]
6. Functions on Azure Container Apps V1 の廃止[^40]
7. Microsoft HPC Pack の廃止[^41]
8. NVv3 シリーズ Azure Virtual Machines の廃止[^42]
9. NVv4 シリーズ Azure Virtual Machines の廃止[^43]
10. Azure Monitor Application Insights のシングルステップ可用性テストの標準テストへの移行（9月30日まで）[^44]

## その他 — 1件

1. Azure canvases for GitHub Copilot の発表[^45]

---

[^1]: Generally Available: Azure Arc-enabled SQL Server Available in Italy North, https://azure.microsoft.com/ja-jp/updates/v2/?id=570763

[^2]: Generally Available: Azure Arc-enabled SQL Server in Germany West Central, https://azure.microsoft.com/ja-jp/updates/v2/?id=570696

[^3]: Generally Available: Azure Backup for Elastic SAN, https://azure.microsoft.com/ja-jp/updates/v2/?id=494438

[^4]: Generally Available: Azure Database for PostgreSQL Flexible Server supports cross-tenant customer-managed keys (CMK), https://azure.microsoft.com/ja-jp/updates/v2/?id=571783

[^5]: Generally Available: Azure SQL Managed Instance updates for late-September 2026, https://azure.microsoft.com/ja-jp/updates/v2/?id=571632

[^6]: Generally Available: Azure SQL updates for late-September 2026, https://azure.microsoft.com/ja-jp/updates/v2/?id=571643

[^7]: Generally Available: Database DevOps in SSMS powered by SQL projects, https://azure.microsoft.com/ja-jp/updates/v2/?id=571852

[^8]: Generally Available: Instant Access for VM restore points, https://azure.microsoft.com/ja-jp/updates/v2/?id=572573

[^9]: Generally Available: Luxembourg - Azure Extended Zones, https://azure.microsoft.com/ja-jp/updates/v2/?id=572968

[^10]: Generally Available: SQL Formatter, https://azure.microsoft.com/ja-jp/updates/v2/?id=571872

[^11]: Generally Available: SQL Migration Agent Skills for assessment, migration, and validation, https://azure.microsoft.com/ja-jp/updates/v2/?id=571899

[^12]: Generally Available: SQL Server on Azure Local Disconnected (ALDO), https://azure.microsoft.com/ja-jp/updates/v2/?id=571836

[^13]: Generally Available: SQL Server support on Azure Local connected mode, https://azure.microsoft.com/ja-jp/updates/v2/?id=571841

[^14]: Generally Available: Storage optimized Lasv5 and Laosv5 Azure VM series, https://azure.microsoft.com/ja-jp/updates/v2/?id=572630

[^15]: Generally Available: Storage with cool access enhancement, https://azure.microsoft.com/ja-jp/updates/v2/?id=573032

[^16]: Generally Available: Support for large volume breakthrough mode, https://azure.microsoft.com/ja-jp/updates/v2/?id=573027

[^17]: Generally Available: Vector search and vector indexes in Azure SQL, https://azure.microsoft.com/ja-jp/updates/v2/?id=571800

[^18]: Public Preview: Microsoft entra kerberos authentication for Azure NetApp Files, https://azure.microsoft.com/ja-jp/updates/v2/?id=573041

[^19]: Public Preview: Major version upgrades (MVU) for Azure Database for PostgreSQL elastic clusters, https://azure.microsoft.com/ja-jp/updates/v2/?id=571504

[^20]: Public Preview: Automatic Zone Placement for Virtual Machine Scale Sets, https://azure.microsoft.com/ja-jp/updates/v2/?id=571075

[^21]: Public Preview: Azure Database for PostgreSQL Ultra Disk, https://azure.microsoft.com/ja-jp/updates/v2/?id=571909

[^22]: Public Preview: Azure HorizonDB supports PostgreSQL 18, https://azure.microsoft.com/ja-jp/updates/v2/?id=573048

[^23]: Public Preview: Azure SQL Database Hyperscale Serverless auto-pause and auto-resume, https://azure.microsoft.com/ja-jp/updates/v2/?id=571857

[^24]: Public Preview: Azure SQL Dev Hub, https://azure.microsoft.com/ja-jp/updates/v2/?id=572998

[^25]: Public Preview: Azure SQL updates for late-September 2026, https://azure.microsoft.com/ja-jp/updates/v2/?id=571846

[^26]: Public Preview: Long-term retention (LTR) v2 for Azure Database for PostgreSQL, https://azure.microsoft.com/ja-jp/updates/v2/?id=571914

[^27]: Public Preview: Microsoft SQL Agent Skills, https://azure.microsoft.com/ja-jp/updates/v2/?id=573003

[^28]: Public Preview: Migrate directly from Azure Arc to Azure SQL Database, including Hyperscale, https://azure.microsoft.com/ja-jp/updates/v2/?id=571795

[^29]: Public Preview: Performance monitoring for Azure Arc–enabled SQL Server, https://azure.microsoft.com/ja-jp/updates/v2/?id=571904

[^30]: Public Preview: Reader Endpoint for Azure Database for MySQL, https://azure.microsoft.com/ja-jp/updates/v2/?id=569653

[^31]: Public preview: Script-based deployment for SQL Server on Linux Azure VM, https://azure.microsoft.com/ja-jp/updates/v2/?id=571810

[^32]: Public Preview: SQL Performance Monitoring for Azure SQL Database, https://azure.microsoft.com/ja-jp/updates/v2/?id=571867

[^33]: Public Preview: SQL performance monitoring for SQL Server on Azure Virtual Machines, https://azure.microsoft.com/ja-jp/updates/v2/?id=571894

[^34]: Public Preview: Ubuntu 26.04 support in AKS, https://azure.microsoft.com/ja-jp/updates/v2/?id=573214

[^35]: Retirement: Azure Arc enabled System Center Virtual Machine Manager will be retired September 30, 2029, https://azure.microsoft.com/ja-jp/updates/v2/?id=570283

[^36]: Retirement: Azure Communication Services (ACS) standalone services will be retired on September 30, 2028, https://azure.microsoft.com/ja-jp/updates/v2/?id=557117

[^37]: Retirement: Azure IoT Central will be retired on September 20, 2029, https://azure.microsoft.com/ja-jp/updates/v2/?id=569914

[^38]: Retirement: DCsv3 and DCdsv3-series Azure Virtual Machines will be retired on October 31, 2029, https://azure.microsoft.com/ja-jp/updates/v2/?id=569592

[^39]: Retirement: Dv3, Dsv3, Ev3, and Esv3 Azure VMs, https://azure.microsoft.com/ja-jp/updates/v2/?id=572346

[^40]: Retirement: Functions on Azure Container Apps V1, https://azure.microsoft.com/ja-jp/updates/v2/?id=570800

[^41]: Retirement: Microsoft HPC Pack, https://azure.microsoft.com/ja-jp/updates/v2/?id=570046

[^42]: Retirement: NVv3-series Azure Virtual Machines, https://azure.microsoft.com/ja-jp/updates/v2/?id=573414

[^43]: Retirement: NVv4-series Azure Virtual Machines, https://azure.microsoft.com/ja-jp/updates/v2/?id=573415

[^44]: Retirement: Transition to using standard tests for single-step availability testing in Azure Monitor application insights by 30 September, https://azure.microsoft.com/ja-jp/updates/v2/?id=transition-to-using-standard-tests-for-singlestep-availability-testing-in-azure-monitor-application-insights-by-30-september

[^45]: Announcing: Azure canvases for GitHub Copilot, https://azure.microsoft.com/ja-jp/updates/v2/?id=573385
