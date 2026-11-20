Title: Azure Update (2026/11/17 - 2026/11/20)
Date: 2026-11-20
Slug: azure-update-2026-11-20
Lang: ja-jp
Category: notebook
Tags: ai-machine-learning, analytics, api-management, azure, azure-backup, azure-bastion, azure-cosmos-db, azure-database-for-mysql, azure-database-for-postgresql, azure-databricks, azure-disk-storage, azure-documentdb, azure-elastic-san, azure-expressroute, azure-firewall, azure-front-door, azure-horizondb, azure-kubernetes-service-aks, azure-private-link, azure-sql-database, azure-sql-managed-instance, azure-updates, compute, containers, databases, hybrid-multicloud, integration, internet-of-things, management-and-governance, microsoft-foundry, mobile, networking, security, sql-server-on-azure-virtual-machines, storage, virtual-machines, web, web-application-firewall
Summary: 2026年11月17日〜11月20日の Azure Update まとめ。GA 18件、パブリックプレビュー 27件、プライベートプレビュー 1件、その他 4件の計50件。

2026年11月17日〜11月20日の Azure Update のまとめです。

| 分類 | 件数 |
| --- | --- |
| GA (一般提供) | 18 |
| パブリックプレビュー | 27 |
| プライベートプレビュー | 1 |
| その他 | 4 |
| **合計** | **50** |

## GA (一般提供)

- **Generally Available: Soft delete in Azure Compute Gallery**[^1]
    - Soft delete in Azure Compute Gallery is now generally available, so you can recover image versions that were deleted by accident. You can set a retention period of 7 to 365 days. During retention,...

- **Generally Available: Cross-subscription backup for Azure Virtual Machines in Azure Backup**[^2]
    - Azure Backup now supports cross-subscription backup for Azure Virtual Machines, enabling customers to protect VMs using a Recovery Services vault located in a different Azure subscription within the...

- **Generally Available: Intel and AMD v6 with temp disk for Azure Database for PostgreSQL**[^3]
    - Azure Database for PostgreSQL Flexible Server is announcing the general availability of Intel and AMD v6 compute tiers with local temporary disk. The new v6 generation expands the Flexible Server...

- **Generally Available: Intel and AMD v5 diskless tier for Azure Database for PostgreSQL**[^4]
    - Azure Database for PostgreSQL Flexible Server is announcing the general availability of Intel and AMD V5 diskless compute. These new options expand the v5 compute portfolio with General Purpose and...

- **Generally Available: Cobalt 200 compute for Azure Database for PostgreSQL**[^5]
    - Azure Database for PostgreSQL Flexible Server is announcing the general availability of Cobalt 200 ARM-based compute. Cobalt 200 expands the Flexible Server compute portfolio with Microsoft-designed...

- **Generally Available: Geo-redundant backup and restore for Azure HorizonDB**[^6]
    - Geo-redundant backup and restore for Azure HorizonDB is now available. You can use geo-redundant backups to strengthen data protection and restore your HorizonDB deployment in another Azure region...

- **Generally Available: Throughput buckets in Azure Cosmos DB**[^7]
    - We're excited to announce the general availability of throughput buckets in Azure Cosmos DB. You can manage the resource consumption of multiple workloads using the same container by limiting the...

- **Generally Available: Semantic Reranker in Azure Cosmos DB**[^8]
    - Semantic Reranker in Azure Cosmos DB improves search relevance by reordering candidate results based on the meaning of the search text and surrounding context. It uses an AI model to evaluate...

- **Generally Available: Database Hub real-time performance dashboards**[^9]
    - Database Hub in Microsoft Fabric gives you built-in, real-time performance dashboards for Microsoft SQL, Azure Database for PostgreSQL flexible server, and Azure Cosmos DB in one place. From the...

- **Generally Available: Near-instant provisioning for Azure DocumentDB clusters**[^10]
    - Now the M10 to M30 computer tiers are available for near-instant provisioning. Historically, the free tier in Azure DocumentDB was made available for instant provisioning. The goal was to help you...

- **Generally Available: Network egress controls for hosted agents in Microsoft Foundry**[^11]
    - Network egress controls govern the outbound connections a Foundry hosted agent can make, is generally available. Ordered rules match on destination host (FQDN, with wildcards such as *.contoso.com)...

- **Generally Available: MCP server knowledge sources in Foundry IQ**[^12]
    - Foundry IQ supported Model Context Protocol (MCP) servers as federated knowledge sources, is generally available. Customers register an MCP server as a read-only knowledge source in Foundry IQ. MCP...

- **Generally Available: Semantic chunking and AI-generated image descriptions with Azure Content Understanding in Azure AI Search**[^13]
    - The Azure Content Understanding skill in Azure AI Search is generally available for semantic chunking and AI-generated image descriptions, for use with Foundry IQ and Azure AI Search. The skill...

- **Generally Available: Snapshot backup for SQL Server in Azure VMs**[^14]
    - Azure Backup now supports snapshot-based backup for SQL Server running on Azure Virtual Machines. This new capability uses Azure disk snapshots combined with native SQL transaction log backups to...

- **Generally Available: Confidential VMs with Intel TDX support on AKS**[^15]
    - Customers standardized on Intel Trust Domain Extensions (TDX) for attestation and hardware confidentiality can't run those workloads on AKS Confidential VM node pools today, because CVM node images...

- **Generally Available: User-assigned managed identity for Azure HorizonDB**[^16]
    - User-assigned managed identity (UMI) support is now generally available for Azure HorizonDB, enabling you to assign and centrally manage Azure identities for your HorizonDB clusters. With UMI, you...

- **Generally Available: Microsoft Entra authentication for Azure HorizonDB**[^17]
    - Microsoft Entra authentication is now generally available for Azure HorizonDB, providing a more secure, identity-based approach to database authentication. You can use Microsoft Entra authentication...

- **Generally Available: Azure Cosmos DB full-text search BM25 score projection**[^18]
    - Azure Cosmos DB full-text search now includes BM25 score projection, giving you clear visibility into why results appear in the order they do. Your app can now access the relevance score for each...

## パブリックプレビュー

- **Public Preview: PostgreSQL 19 on Azure Database for PostgreSQL**[^19]
    - You can now try PostgreSQL 19 in public preview on Azure Database for PostgreSQL – Flexible Server in the East Asia region. With this preview, you can provision new PostgreSQL 19 servers through the...

- **Public Preview: Zone resilience for Azure VMs**[^20]
    - Zone resilience for Azure VMs, now in public preview, lets you recover an eligible zonal VM in another availability zone in the same region, retaining the existing VM resource and configuration. ZRS...

- **Public Preview: Database Agent for Azure Database for PostgreSQL**[^21]
    - Database Agent helps you detect, understand, and respond to database health and performance issues more quickly in Azure Database for PostgreSQL. It proactively monitors database health to identify...

- **Public Preview: AI bot ruleset for Azure Front Door Premium WAF**[^22]
    - Announcing the public preview of the AI bot ruleset for Azure Web Application Firewall (WAF) on Azure Front Door Premium. AI crawlers and agents visit your site for different reasons, and you may...

- **Public Preview: AI-powered application and database modernization with Modernize CLI**[^23]
    - Modernize CLI brings application and database modernization together as one connected, agentic journey. It assesses application architecture, dependencies, and cloud readiness while discovering the...

- **Public Preview: Immutable snapshots for Azure Disk Storage**[^24]
    - Immutable snapshots for Azure Disk Storage are now available in public preview. You can now apply an immutability policy to snapshots of any Azure disk type to prevent deletion for up to 90 days....

- **Generally Available: Customize backup retention from 1 to 35 days in Azure HorizonDB**[^25]
    - You can now configure backup retention for your Azure HorizonDB deployments from 1 to 35 days, giving you greater flexibility to align backup retention with your application and data protection...

- **Limited Preview: AI model management in Azure HorizonDB**[^26]
    - AI model management in Azure HorizonDB is now in limited preview, designed to simplify how you bring AI into your database. With just a single step, you can provision fully managed AI models for...

- **Public Preview: Pod Sandboxing kata-vm-isolation-v2 runtime class**[^27]
    - Isolated pods should not force a tradeoff between security and startup performance. With classic sandboxed pod flows, every pod boots a new Kata VM, which adds cold-start latency and extra memory...

- **Pulic Preview: Azure Elastic SAN Next Generation**[^28]
    - Azure Elastic SAN Next Generation is now in public preview. Elastic SAN Next Generation keeps the core benefits customers value in Elastic SAN today: a single SAN resource hierarchy to consolidate...

- **Limited Preview: Azure Workload Center for SAP and Azure Copilot Run SAP Agent**[^29]
    - Azure Workload Center for SAP, together with the Azure Copilot Run SAP Agent, is a workload-aware experience, powered by Workload Virtual Instance (WVI) for operating SAP workloads on Azure. Azure...

- **Limited Preview: Azure Workload Center for Oracle and Azure Copilot Run Oracle Agent**[^30]
    - Azure Workload Center for Oracle, together with the Azure Copilot Run Oracle Agent, is a workload-aware experience, powered by Workload Virtual Instance (WVI) for operating Oracle workloads on Azure....

- **Public Preview: Database Agent for SQL with contextual Copilot**[^31]
    - Database Agent now gives you AI-generated, evidence-grounded recommendations for detected database issues, including why the issue matters, the likely cause, and the recommended next step....

- **Public Preview: Azure SQL DB Hyperscale Cross Database Querying**[^32]
    - Native cross-database queries in Azure SQL Database Hyperscale let applications access and join data across databases in the same Hyperscale elastic pool on a logical server, using familiar T-SQL...

- **Public Preview: Confidential VMs with OS Disk Encryption support on AKS**[^33]
    - Regulated customers running AKS Confidential VM node pools protect workloads in memory today, but the OS disk isn't encrypted at rest, so they have to close the data-at-rest gap outside the platform....

- **Generally Available: Private endpoint support for Azure HorizonDB clusters**[^34]
    - You can now connect to Azure HorizonDB clusters privately through Azure Private Link, using a private IP address from your virtual network. Private DNS integration makes connection setup easier,...

- **Public Preview: Service tags for inbound rules in network security perimeter**[^35]
    - Announcing the public preview of 'service tags as inbound rules' support for third-party customers in network security perimeter. This new capability simplifies how customers manage access to in...

- **Public Preview: Perimeter link (cross perimeter) in network security perimeter**[^36]
    - This capability enables secure connectivity between resources protected by different network security perimeters, while maintaining strong perimeter-based access controls. With this release,...

- **Public Preview: Agent Grid helping secure AI agent communications**[^37]
    - Agent Grid is now in public preview, bringing identity-based Zero Trust network security to AI agents on supported Azure environments. Security teams can govern communications among agents, models,...

- **Public Preview: Azure Adaptive Virtual Patching**[^38]
    - Azure Adaptive Virtual Patching introduces an AI-orchestrated Adaptive Shield designed to reduce exposure to new, emerging, and newly disclosed zero-day vulnerabilities while customers test and...

- **Public Preview: AI Security add-on for Azure Firewall Premium**[^39]
    - AI Security, a new add-on for Azure Firewall Premium, is now in public preview. Announced at Microsoft Ignite, it introduces five capabilities to help you protect AI applications, safeguard sensitive...

- **Public Preview: Azure Bastion RDP and SSH vision**[^40]
    - Azure Bastion RDP and SSH vision is now in public preview, bringing AI-assisted review to recorded privileged sessions. Security and operations teams can use session summaries and insights into...

- **Public Preview: Agent Sandbox cluster extension**[^41]
    - Running AI agents that execute untrusted, model-generated code requires isolated environments for each session. Today, teams building on Kubernetes assemble their own sandbox lifecycle, storage, and...

- **Public Preview: Scale ExpressRoute Direct connectivity with link groups**[^42]
    - Azure ExpressRoute is introducing link groups for ExpressRoute Direct, enabling high-throughput workloads to scale network connectivity while reducing operational complexity. Instead of managing...

- **Public Preview: Azure API Management Application**[^43]
    - The Applications feature in Azure API Management is now available in public preview to all customers, with no sign-up or registration required. Applications provide a streamlined way to organize APIs...

- **Public Preview: Windows Trusted Launch**[^44]
    - Teams running Windows workloads on AKS often need stronger boot-chain protection for regulated or security-sensitive environments, but Trusted Launch support has historically stopped short of Windows...

- **Public Preview: Azure Database for MySQL on Premium SSD v2**[^45]
    - Azure Database for MySQL now supports Premium SSD v2 (managed disks) in public preview. Premium SSD v2 provides higher performance and better price-performance compared to Premium File Share, with...

## プライベートプレビュー

- **Private Preview: Azure DH/EHasv8 VMs based on 6th Gen AMD EPYC™ (“Venice”) processors**[^46]
    - We are announcing the preview of the new Azure DHasv8, DHalsv8 and EHasv8-series virtual machines (VMs), powered by 6th Generation AMD EPYC™ (“Venice”) processors. Designed for the next generation of...

## その他

- **Announcing: Multiparty private offers in Microsoft Marketplace expands to Malaysia and Saudi Arabia**[^47]
    - Multiparty private offers give Microsoft partners a way to procure third-party cloud and AI solutions for customers through Marketplace. Software companies can expand into new markets by working with...

- **Announcing: The new Azure Databricks on Azure Government is now in Beta**[^48]
    - A new Azure Databricks environment is now available in Beta on Microsoft Azure Government. It brings the modern data and AI platform from global Azure to U.S. public sector agencies and their...

- **Announcing: Azure Boost observability for NVMe disks**[^49]
    - Azure Boost observability for NVMe disks is an open-source command-line tool that you run inside compatible Azure VMs. Backed by Azure Boost, the tool provides remote disk I/O and latency metrics and...

- **Generally Available: Cobalt 200 Arm-based Dplsv7, Dpsv7, Epsv7, Mpsv4, and Lpsv5-series Virtual Machines**[^50]
    - The general purpose Dpsv7 and Dplsv7, memory-optimized Epsv7, high-memory Mpsv4, and dense storage Lpsv5 VMs are now generally available. These virtual machines deliver significant enhancements over...

[^1]: Generally Available: Soft delete in Azure Compute Gallery, https://azure.microsoft.com/ja-jp/updates/v2/581907
[^2]: Generally Available: Cross-subscription backup for Azure Virtual Machines in Azure Backup, https://azure.microsoft.com/ja-jp/updates/v2/581048
[^3]: Generally Available: Intel and AMD v6 with temp disk for Azure Database for PostgreSQL, https://azure.microsoft.com/ja-jp/updates/v2/579590
[^4]: Generally Available: Intel and AMD v5 diskless tier for Azure Database for PostgreSQL, https://azure.microsoft.com/ja-jp/updates/v2/579595
[^5]: Generally Available: Cobalt 200 compute for Azure Database for PostgreSQL, https://azure.microsoft.com/ja-jp/updates/v2/579585
[^6]: Generally Available: Geo-redundant backup and restore for Azure HorizonDB, https://azure.microsoft.com/ja-jp/updates/v2/574168
[^7]: Generally Available: Throughput buckets in Azure Cosmos DB, https://azure.microsoft.com/ja-jp/updates/v2/571488
[^8]: Generally Available: Semantic Reranker in Azure Cosmos DB, https://azure.microsoft.com/ja-jp/updates/v2/577520
[^9]: Generally Available: Database Hub real-time performance dashboards, https://azure.microsoft.com/ja-jp/updates/v2/579644
[^10]: Generally Available: Near-instant provisioning for Azure DocumentDB clusters, https://azure.microsoft.com/ja-jp/updates/v2/579349
[^11]: Generally Available: Network egress controls for hosted agents in Microsoft Foundry, https://azure.microsoft.com/ja-jp/updates/v2/571821
[^12]: Generally Available: MCP server knowledge sources in Foundry IQ, https://azure.microsoft.com/ja-jp/updates/v2/563411
[^13]: Generally Available: Semantic chunking and AI-generated image descriptions with Azure Content Understanding in Azure AI Search, https://azure.microsoft.com/ja-jp/updates/v2/563661
[^14]: Generally Available: Snapshot backup for SQL Server in Azure VMs, https://azure.microsoft.com/ja-jp/updates/v2/564668
[^15]: Generally Available: Confidential VMs with Intel TDX support on AKS, https://azure.microsoft.com/ja-jp/updates/v2/581130
[^16]: Generally Available: User-assigned managed identity for Azure HorizonDB, https://azure.microsoft.com/ja-jp/updates/v2/575069
[^17]: Generally Available: Microsoft Entra authentication for Azure HorizonDB, https://azure.microsoft.com/ja-jp/updates/v2/575111
[^18]: Generally Available: Azure Cosmos DB full-text search BM25 score projection, https://azure.microsoft.com/ja-jp/updates/v2/577531
[^19]: Public Preview: PostgreSQL 19 on Azure Database for PostgreSQL, https://azure.microsoft.com/ja-jp/updates/v2/574587
[^20]: Public Preview: Zone resilience for Azure VMs, https://azure.microsoft.com/ja-jp/updates/v2/581254
[^21]: Public Preview: Database Agent for Azure Database for PostgreSQL, https://azure.microsoft.com/ja-jp/updates/v2/579579
[^22]: Public Preview: AI bot ruleset for Azure Front Door Premium WAF, https://azure.microsoft.com/ja-jp/updates/v2/581604
[^23]: Public Preview: AI-powered application and database modernization with Modernize CLI, https://azure.microsoft.com/ja-jp/updates/v2/579943
[^24]: Public Preview: Immutable snapshots for Azure Disk Storage, https://azure.microsoft.com/ja-jp/updates/v2/581503
[^25]: Generally Available: Customize backup retention from 1 to 35 days in Azure HorizonDB, https://azure.microsoft.com/ja-jp/updates/v2/574163
[^26]: Limited Preview: AI model management in Azure HorizonDB, https://azure.microsoft.com/ja-jp/updates/v2/563097
[^27]: Public Preview: Pod Sandboxing kata-vm-isolation-v2 runtime class, https://azure.microsoft.com/ja-jp/updates/v2/581120
[^28]: Pulic Preview: Azure Elastic SAN Next Generation, https://azure.microsoft.com/ja-jp/updates/v2/581634
[^29]: Limited Preview: Azure Workload Center for SAP and Azure Copilot Run SAP Agent, https://azure.microsoft.com/ja-jp/updates/v2/581209
[^30]: Limited Preview: Azure Workload Center for Oracle and Azure Copilot Run Oracle Agent, https://azure.microsoft.com/ja-jp/updates/v2/581214
[^31]: Public Preview: Database Agent for SQL with contextual Copilot, https://azure.microsoft.com/ja-jp/updates/v2/580091
[^32]: Public Preview: Azure SQL DB Hyperscale Cross Database Querying, https://azure.microsoft.com/ja-jp/updates/v2/579221
[^33]: Public Preview: Confidential VMs with OS Disk Encryption support on AKS, https://azure.microsoft.com/ja-jp/updates/v2/581125
[^34]: Generally Available: Private endpoint support for Azure HorizonDB clusters, https://azure.microsoft.com/ja-jp/updates/v2/574153
[^35]: Public Preview: Service tags for inbound rules in network security perimeter, https://azure.microsoft.com/ja-jp/updates/v2/579201
[^36]: Public Preview: Perimeter link (cross perimeter) in network security perimeter, https://azure.microsoft.com/ja-jp/updates/v2/579206
[^37]: Public Preview: Agent Grid helping secure AI agent communications, https://azure.microsoft.com/ja-jp/updates/v2/580684
[^38]: Public Preview: Azure Adaptive Virtual Patching, https://azure.microsoft.com/ja-jp/updates/v2/580689
[^39]: Public Preview: AI Security add-on for Azure Firewall Premium, https://azure.microsoft.com/ja-jp/updates/v2/580694
[^40]: Public Preview: Azure Bastion RDP and SSH vision, https://azure.microsoft.com/ja-jp/updates/v2/580699
[^41]: Public Preview: Agent Sandbox cluster extension, https://azure.microsoft.com/ja-jp/updates/v2/580916
[^42]: Public Preview: Scale ExpressRoute Direct connectivity with link groups, https://azure.microsoft.com/ja-jp/updates/v2/580926
[^43]: Public Preview: Azure API Management Application, https://azure.microsoft.com/ja-jp/updates/v2/581277
[^44]: Public Preview: Windows Trusted Launch, https://azure.microsoft.com/ja-jp/updates/v2/572591
[^45]: Public Preview: Azure Database for MySQL on Premium SSD v2, https://azure.microsoft.com/ja-jp/updates/v2/577515
[^46]: Private Preview: Azure DH/EHasv8 VMs based on 6th Gen AMD EPYC™ (“Venice”) processors, https://azure.microsoft.com/ja-jp/updates/v2/581308
[^47]: Announcing: Multiparty private offers in Microsoft Marketplace expands to Malaysia and Saudi Arabia, https://azure.microsoft.com/ja-jp/updates/v2/580700
[^48]: Announcing: The new Azure Databricks on Azure Government is now in Beta, https://azure.microsoft.com/ja-jp/updates/v2/581645
[^49]: Announcing: Azure Boost observability for NVMe disks, https://azure.microsoft.com/ja-jp/updates/v2/581227
[^50]: Generally Available: Cobalt 200 Arm-based Dplsv7, Dpsv7, Epsv7, Mpsv4, and Lpsv5-series Virtual Machines, https://azure.microsoft.com/ja-jp/updates/v2/581298
