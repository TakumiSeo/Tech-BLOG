Title: Azure Update (2026/11/17 - 2026/11/18)
Date: 2026-11-18
Slug: azure-update-2026-11-18
Lang: ja-jp
Category: notebook
Tags: ai-machine-learning, api-management, azure, azure-backup, azure-bastion, azure-cosmos-db, azure-database-for-mysql, azure-database-for-postgresql, azure-disk-storage, azure-documentdb, azure-elastic-san, azure-expressroute, azure-firewall, azure-horizondb, azure-kubernetes-service-aks, azure-managed-redis, azure-private-link, azure-sql-database, azure-sql-managed-instance, azure-updates, compute, containers, databases, hybrid-multicloud, integration, internet-of-things, management-and-governance, microsoft-foundry, mobile, networking, security, sql-server-on-azure-virtual-machines, storage, virtual-machines, web
Summary: 2026年11月17日〜11月18日の Azure Update まとめ。GA 21件、パブリックプレビュー 26件、プライベートプレビュー 1件、その他 2件の計50件。

2026年11月17日〜11月18日の Azure Update のまとめです。

| 分類 | 件数 |
| --- | --- |
| GA (一般提供) | 21 |
| パブリックプレビュー | 26 |
| プライベートプレビュー | 1 |
| その他 | 2 |
| **合計** | **50** |

## GA (一般提供)

- **Generally Available: Intel and AMD v6 with temp disk for Azure Database for PostgreSQL**[^1]
    - Azure Database for PostgreSQL Flexible Server is announcing the general availability of Intel and AMD v6 compute tiers with local temporary disk. The new v6 generation expands the Flexible Server...

- **Generally Available: Intel and AMD v5 diskless tier for Azure Database for PostgreSQL**[^2]
    - Azure Database for PostgreSQL Flexible Server is announcing the general availability of Intel and AMD V5 diskless compute. These new options expand the v5 compute portfolio with General Purpose and...

- **Generally Available: Cobalt 200 compute for Azure Database for PostgreSQL**[^3]
    - Azure Database for PostgreSQL Flexible Server is announcing the general availability of Cobalt 200 ARM-based compute. Cobalt 200 expands the Flexible Server compute portfolio with Microsoft-designed...

- **Generally Available: Geo-redundant backup and restore for Azure HorizonDB**[^4]
    - Geo-redundant backup and restore for Azure HorizonDB is now available. You can use geo-redundant backups to strengthen data protection and restore your HorizonDB deployment in another Azure region...

- **Generally Available: Throughput buckets in Azure Cosmos DB**[^5]
    - We're excited to announce the general availability of throughput buckets in Azure Cosmos DB. You can manage the resource consumption of multiple workloads using the same container by limiting the...

- **Generally Available: Semantic Reranker in Azure Cosmos DB**[^6]
    - Semantic Reranker in Azure Cosmos DB improves search relevance by reordering candidate results based on the meaning of the search text and surrounding context. It uses an AI model to evaluate...

- **Generally Available: Database Hub real-time performance dashboards**[^7]
    - Database Hub in Microsoft Fabric gives you built-in, real-time performance dashboards for Microsoft SQL, Azure Database for PostgreSQL flexible server, and Azure Cosmos DB in one place. From the...

- **Generally Available: Near-instant provisioning for Azure DocumentDB clusters**[^8]
    - Now the M10 to M30 computer tiers are available for near-instant provisioning. Historically, the free tier in Azure DocumentDB was made available for instant provisioning. The goal was to help you...

- **Generally Available: Network egress controls for hosted agents in Microsoft Foundry**[^9]
    - Network egress controls govern the outbound connections a Foundry hosted agent can make, is generally available. Ordered rules match on destination host (FQDN, with wildcards such as *.contoso.com)...

- **Generally Available: MCP server knowledge sources in Foundry IQ**[^10]
    - Foundry IQ supported Model Context Protocol (MCP) servers as federated knowledge sources, is generally available. Customers register an MCP server as a read-only knowledge source in Foundry IQ. MCP...

- **Generally Available: Semantic chunking and AI-generated image descriptions with Azure Content Understanding in Azure AI Search**[^11]
    - The Azure Content Understanding skill in Azure AI Search is generally available for semantic chunking and AI-generated image descriptions, for use with Foundry IQ and Azure AI Search. The skill...

- **Generally Available: Snapshot backup for SQL Server in Azure VMs**[^12]
    - Azure Backup now supports snapshot-based backup for SQL Server running on Azure Virtual Machines. This new capability uses Azure disk snapshots combined with native SQL transaction log backups to...

- **Generally Available: Confidential VMs with Intel TDX support on AKS**[^13]
    - Customers standardized on Intel Trust Domain Extensions (TDX) for attestation and hardware confidentiality can't run those workloads on AKS Confidential VM node pools today, because CVM node images...

- **Generally Available: User-assigned managed identity for Azure HorizonDB**[^14]
    - User-assigned managed identity (UMI) support is now generally available for Azure HorizonDB, enabling you to assign and centrally manage Azure identities for your HorizonDB clusters. With UMI, you...

- **Generally Available: Microsoft Entra authentication for Azure HorizonDB**[^15]
    - Microsoft Entra authentication is now generally available for Azure HorizonDB, providing a more secure, identity-based approach to database authentication. You can use Microsoft Entra authentication...

- **Generally Available: Azure Cosmos DB full-text search BM25 score projection**[^16]
    - Azure Cosmos DB full-text search now includes BM25 score projection, giving you clear visibility into why results appear in the order they do. Your app can now access the relevance score for each...

- **Generally Available: Azure Managed Redis database integration guidance**[^17]
    - Improved database integration guidance for Azure Managed Redis helps you add caching to applications built with Azure Database for PostgreSQL flexible server, Azure Cosmos DB, and Azure SQL. You can...

- **Generally Available: Azure Managed Redis keyspace notifications**[^18]
    - Keyspace notifications are now generally available for Azure Managed Redis, enabling your applications to receive events through pub/sub when data in your cache changes. You can configure the event...

- **Generally Available: Azure Cache for Redis to Azure Managed Redis migration tooling**[^19]
    - The general availability of built-in DNS migration tooling simplifies endpoint migration from Azure Cache for Redis Basic, Standard, and Premium tiers to Azure Managed Redis. The tooling lets you...

- **Generally Available: Azure SQL Managed Instance link support for availability groups with multiple databases**[^20]
    - You can now use a single Azure SQL Managed Instance link to extend a SQL Server Always On Availability Group with multiple databases to Azure SQL Managed Instance. You can extend an existing...

- **Generally Available: Zone-redundant Next-gen GP tier in Azure SQL Managed Instance**[^21]
    - Zone redundancy for the Next-gen General Purpose service tier helps improve the resiliency of Azure SQL Managed Instance by distributing critical service components across availability zones. This...

## パブリックプレビュー

- **Public Preview: Immutable snapshots for Azure Disk Storage**[^22]
    - Immutable snapshots for Azure Disk Storage are now available in public preview. Immutable snapshots complement Azure Backup immutable vaults. Use vaults for cost-efficient long-term retention, and...

- **Generally Available: Customize backup retention from 1 to 35 days in Azure HorizonDB**[^23]
    - You can now configure backup retention for your Azure HorizonDB deployments from 1 to 35 days, giving you greater flexibility to align backup retention with your application and data protection...

- **Limited Preview: AI model management in Azure HorizonDB**[^24]
    - AI model management in Azure HorizonDB is now in limited preview, designed to simplify how you bring AI into your database. With just a single step, you can provision fully managed AI models for...

- **Public Preview: Pod Sandboxing kata-vm-isolation-v2 runtime class**[^25]
    - Isolated pods should not force a tradeoff between security and startup performance. With classic sandboxed pod flows, every pod boots a new Kata VM, which adds cold-start latency and extra memory...

- **Pulic Preview: Azure Elastic SAN Next Generation**[^26]
    - Azure Elastic SAN Next Generation is now in public preview. Elastic SAN Next Generation keeps the core benefits customers value in Elastic SAN today: a single SAN resource hierarchy to consolidate...

- **Limited Preview: Azure Workload Center for SAP and Azure Copilot Run SAP Agent**[^27]
    - Azure Workload Center for SAP, together with the Azure Copilot Run SAP Agent, is a workload-aware experience, powered by Workload Virtual Instance (WVI) for operating SAP workloads on Azure. Azure...

- **Limited Preview: Azure Workload Center for Oracle and Azure Copilot Run Oracle Agent**[^28]
    - Azure Workload Center for Oracle, together with the Azure Copilot Run Oracle Agent, is a workload-aware experience, powered by Workload Virtual Instance (WVI) for operating Oracle workloads on Azure....

- **Public Preview: Database Agent for SQL with contextual Copilot**[^29]
    - Database Agent now gives you AI-generated, evidence-grounded recommendations for detected database issues, including why the issue matters, the likely cause, and the recommended next step....

- **Public Preview: Azure SQL DB Hyperscale Cross Database Querying**[^30]
    - Native cross-database queries in Azure SQL Database Hyperscale let applications access and join data across databases in the same Hyperscale elastic pool on a logical server, using familiar T-SQL...

- **Public Preview: Confidential VMs with OS Disk Encryption support on AKS**[^31]
    - Regulated customers running AKS Confidential VM node pools protect workloads in memory today, but the OS disk isn't encrypted at rest, so they have to close the data-at-rest gap outside the platform....

- **Generally Available: Private endpoint support for Azure HorizonDB clusters**[^32]
    - You can now connect to Azure HorizonDB clusters privately through Azure Private Link, using a private IP address from your virtual network. Private DNS integration makes connection setup easier,...

- **Public Preview: Service tags for inbound rules in network security perimeter**[^33]
    - Announcing the public preview of 'service tags as inbound rules' support for third-party customers in network security perimeter. This new capability simplifies how customers manage access to in...

- **Public Preview: Perimeter link (cross perimeter) in network security perimeter**[^34]
    - This capability enables secure connectivity between resources protected by different network security perimeters, while maintaining strong perimeter-based access controls. With this release,...

- **Public Preview: Agent Grid helping secure AI agent communications**[^35]
    - Agent Grid is now in public preview, bringing identity-based Zero Trust network security to AI agents on supported Azure environments. Security teams can govern communications among agents, models,...

- **Public Preview: Azure Adaptive Virtual Patching**[^36]
    - Azure Adaptive Virtual Patching introduces an AI-orchestrated Adaptive Shield designed to reduce exposure to new, emerging, and newly disclosed zero-day vulnerabilities while customers test and...

- **Public Preview: AI Security add-on for Azure Firewall Premium**[^37]
    - AI Security, a new add-on for Azure Firewall Premium, is now in public preview. Announced at Microsoft Ignite, it introduces five capabilities to help you protect AI applications, safeguard sensitive...

- **Public Preview: Azure Bastion RDP and SSH vision**[^38]
    - Azure Bastion RDP and SSH vision is now in public preview, bringing AI-assisted review to recorded privileged sessions. Security and operations teams can use session summaries and insights into...

- **Public Preview: Agent Sandbox cluster extension**[^39]
    - Running AI agents that execute untrusted, model-generated code requires isolated environments for each session. Today, teams building on Kubernetes assemble their own sandbox lifecycle, storage, and...

- **Public Preview: Scale ExpressRoute Direct connectivity with link groups**[^40]
    - Azure ExpressRoute is introducing link groups for ExpressRoute Direct, enabling high-throughput workloads to scale network connectivity while reducing operational complexity. Instead of managing...

- **Public Preview: Azure API Management Application**[^41]
    - The Applications feature in Azure API Management is now available in public preview to all customers, with no sign-up or registration required. Applications provide a streamlined way to organize APIs...

- **Public Preview: Windows Trusted Launch**[^42]
    - Teams running Windows workloads on AKS often need stronger boot-chain protection for regulated or security-sensitive environments, but Trusted Launch support has historically stopped short of Windows...

- **Public Preview: Azure Database for MySQL on Premium SSD v2**[^43]
    - Azure Database for MySQL now supports Premium SSD v2 (managed disks) in public preview. Premium SSD v2 provides higher performance and better price-performance compared to Premium File Share, with...

- **Public Preview: Azure Managed Redis agent kit**[^44]
    - The Azure Managed Redis agent kit makes guidance for building and operating production-ready Redis applications available directly into your AI-assisted development workflows. You get recommendations...

- **Public Preview: IP filtering in Azure Managed Redis**[^45]
    - Azure Managed Redis now supports adding firewall rules for accessing data, and it gives you greater control over network access to your caches. You can restrict connections to approved source IP...

- **Public Preview: Redis 8 in Azure Managed Redis**[^46]
    - Redis 8 is now available in Azure Managed Redis, bringing the latest Redis innovation to Azure's fully managed Redis service. With richer queries, atomic JSON updates, field-level expiration, and...

- **Public Preview: Shard-level metrics in Azure Managed Redis**[^47]
    - Azure Managed Redis now provides shard-level metrics, giving you greater visibility into the performance of individual shards. This added granularity helps you understand workload distribution,...

## プライベートプレビュー

- **Private Preview: Azure DH/EHasv8 VMs based on 6th Gen AMD EPYC™ (“Venice”) processors**[^48]
    - We are announcing the preview of the new Azure DHasv8, DHalsv8 and EHasv8-series virtual machines (VMs), powered by 6th Generation AMD EPYC™ (“Venice”) processors. Designed for the next generation of...

## その他

- **Announcing: Azure Boost observability for NVMe disks**[^49]
    - Azure Boost observability for NVMe disks is an open-source command-line tool that you run inside compatible Azure VMs. Backed by Azure Boost, the tool provides remote disk I/O and latency metrics and...

- **Generally Available: Cobalt 200 Arm-based Dplsv7, Dpsv7, Epsv7, Mpsv4, and Lpsv5-series Virtual Machines**[^50]
    - The general purpose Dpsv7 and Dplsv7, memory-optimized Epsv7, high-memory Mpsv4, and dense storage Lpsv5 VMs are now generally available. These virtual machines deliver significant enhancements over...

[^1]: Generally Available: Intel and AMD v6 with temp disk for Azure Database for PostgreSQL, https://azure.microsoft.com/ja-jp/updates/v2/579590
[^2]: Generally Available: Intel and AMD v5 diskless tier for Azure Database for PostgreSQL, https://azure.microsoft.com/ja-jp/updates/v2/579595
[^3]: Generally Available: Cobalt 200 compute for Azure Database for PostgreSQL, https://azure.microsoft.com/ja-jp/updates/v2/579585
[^4]: Generally Available: Geo-redundant backup and restore for Azure HorizonDB, https://azure.microsoft.com/ja-jp/updates/v2/574168
[^5]: Generally Available: Throughput buckets in Azure Cosmos DB, https://azure.microsoft.com/ja-jp/updates/v2/571488
[^6]: Generally Available: Semantic Reranker in Azure Cosmos DB, https://azure.microsoft.com/ja-jp/updates/v2/577520
[^7]: Generally Available: Database Hub real-time performance dashboards, https://azure.microsoft.com/ja-jp/updates/v2/579644
[^8]: Generally Available: Near-instant provisioning for Azure DocumentDB clusters, https://azure.microsoft.com/ja-jp/updates/v2/579349
[^9]: Generally Available: Network egress controls for hosted agents in Microsoft Foundry, https://azure.microsoft.com/ja-jp/updates/v2/571821
[^10]: Generally Available: MCP server knowledge sources in Foundry IQ, https://azure.microsoft.com/ja-jp/updates/v2/563411
[^11]: Generally Available: Semantic chunking and AI-generated image descriptions with Azure Content Understanding in Azure AI Search, https://azure.microsoft.com/ja-jp/updates/v2/563661
[^12]: Generally Available: Snapshot backup for SQL Server in Azure VMs, https://azure.microsoft.com/ja-jp/updates/v2/564668
[^13]: Generally Available: Confidential VMs with Intel TDX support on AKS, https://azure.microsoft.com/ja-jp/updates/v2/581130
[^14]: Generally Available: User-assigned managed identity for Azure HorizonDB, https://azure.microsoft.com/ja-jp/updates/v2/575069
[^15]: Generally Available: Microsoft Entra authentication for Azure HorizonDB, https://azure.microsoft.com/ja-jp/updates/v2/575111
[^16]: Generally Available: Azure Cosmos DB full-text search BM25 score projection, https://azure.microsoft.com/ja-jp/updates/v2/577531
[^17]: Generally Available: Azure Managed Redis database integration guidance, https://azure.microsoft.com/ja-jp/updates/v2/577553
[^18]: Generally Available: Azure Managed Redis keyspace notifications, https://azure.microsoft.com/ja-jp/updates/v2/577558
[^19]: Generally Available: Azure Cache for Redis to Azure Managed Redis migration tooling, https://azure.microsoft.com/ja-jp/updates/v2/577579
[^20]: Generally Available: Azure SQL Managed Instance link support for availability groups with multiple databases, https://azure.microsoft.com/ja-jp/updates/v2/578028
[^21]: Generally Available: Zone-redundant Next-gen GP tier in Azure SQL Managed Instance, https://azure.microsoft.com/ja-jp/updates/v2/578033
[^22]: Public Preview: Immutable snapshots for Azure Disk Storage, https://azure.microsoft.com/ja-jp/updates/v2/581503
[^23]: Generally Available: Customize backup retention from 1 to 35 days in Azure HorizonDB, https://azure.microsoft.com/ja-jp/updates/v2/574163
[^24]: Limited Preview: AI model management in Azure HorizonDB, https://azure.microsoft.com/ja-jp/updates/v2/563097
[^25]: Public Preview: Pod Sandboxing kata-vm-isolation-v2 runtime class, https://azure.microsoft.com/ja-jp/updates/v2/581120
[^26]: Pulic Preview: Azure Elastic SAN Next Generation, https://azure.microsoft.com/ja-jp/updates/v2/581634
[^27]: Limited Preview: Azure Workload Center for SAP and Azure Copilot Run SAP Agent, https://azure.microsoft.com/ja-jp/updates/v2/581209
[^28]: Limited Preview: Azure Workload Center for Oracle and Azure Copilot Run Oracle Agent, https://azure.microsoft.com/ja-jp/updates/v2/581214
[^29]: Public Preview: Database Agent for SQL with contextual Copilot, https://azure.microsoft.com/ja-jp/updates/v2/580091
[^30]: Public Preview: Azure SQL DB Hyperscale Cross Database Querying, https://azure.microsoft.com/ja-jp/updates/v2/579221
[^31]: Public Preview: Confidential VMs with OS Disk Encryption support on AKS, https://azure.microsoft.com/ja-jp/updates/v2/581125
[^32]: Generally Available: Private endpoint support for Azure HorizonDB clusters, https://azure.microsoft.com/ja-jp/updates/v2/574153
[^33]: Public Preview: Service tags for inbound rules in network security perimeter, https://azure.microsoft.com/ja-jp/updates/v2/579201
[^34]: Public Preview: Perimeter link (cross perimeter) in network security perimeter, https://azure.microsoft.com/ja-jp/updates/v2/579206
[^35]: Public Preview: Agent Grid helping secure AI agent communications, https://azure.microsoft.com/ja-jp/updates/v2/580684
[^36]: Public Preview: Azure Adaptive Virtual Patching, https://azure.microsoft.com/ja-jp/updates/v2/580689
[^37]: Public Preview: AI Security add-on for Azure Firewall Premium, https://azure.microsoft.com/ja-jp/updates/v2/580694
[^38]: Public Preview: Azure Bastion RDP and SSH vision, https://azure.microsoft.com/ja-jp/updates/v2/580699
[^39]: Public Preview: Agent Sandbox cluster extension, https://azure.microsoft.com/ja-jp/updates/v2/580916
[^40]: Public Preview: Scale ExpressRoute Direct connectivity with link groups, https://azure.microsoft.com/ja-jp/updates/v2/580926
[^41]: Public Preview: Azure API Management Application, https://azure.microsoft.com/ja-jp/updates/v2/581277
[^42]: Public Preview: Windows Trusted Launch, https://azure.microsoft.com/ja-jp/updates/v2/572591
[^43]: Public Preview: Azure Database for MySQL on Premium SSD v2, https://azure.microsoft.com/ja-jp/updates/v2/577515
[^44]: Public Preview: Azure Managed Redis agent kit, https://azure.microsoft.com/ja-jp/updates/v2/577568
[^45]: Public Preview: IP filtering in Azure Managed Redis, https://azure.microsoft.com/ja-jp/updates/v2/577589
[^46]: Public Preview: Redis 8 in Azure Managed Redis, https://azure.microsoft.com/ja-jp/updates/v2/577594
[^47]: Public Preview: Shard-level metrics in Azure Managed Redis, https://azure.microsoft.com/ja-jp/updates/v2/577599
[^48]: Private Preview: Azure DH/EHasv8 VMs based on 6th Gen AMD EPYC™ (“Venice”) processors, https://azure.microsoft.com/ja-jp/updates/v2/581308
[^49]: Announcing: Azure Boost observability for NVMe disks, https://azure.microsoft.com/ja-jp/updates/v2/581227
[^50]: Generally Available: Cobalt 200 Arm-based Dplsv7, Dpsv7, Epsv7, Mpsv4, and Lpsv5-series Virtual Machines, https://azure.microsoft.com/ja-jp/updates/v2/581298
