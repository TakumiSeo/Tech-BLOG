Title: Azure Update (2026/11/17 - 2026/11/21)
Date: 2026-11-21
Slug: azure-update-2026-11-21
Lang: ja-jp
Category: notebook
Tags: ai-machine-learning, analytics, azure, azure-backup, azure-bastion, azure-cosmos-db, azure-database-for-postgresql, azure-databricks, azure-disk-storage, azure-documentdb, azure-elastic-san, azure-expressroute, azure-firewall, azure-front-door, azure-functions, azure-horizondb, azure-kubernetes-service-aks, azure-private-link, azure-sql-database, azure-sql-managed-instance, azure-updates, compute, containers, databases, hybrid-multicloud, internet-of-things, management-and-governance, microsoft-foundry, networking, security, sql-server-on-azure-virtual-machines, storage, virtual-machines, web-application-firewall
Summary: 2026年11月17日〜11月21日の Azure Update まとめ。GA 17件、パブリックプレビュー 28件、プライベートプレビュー 1件、リタイア 1件、その他 3件の計50件。

2026年11月17日〜11月21日の Azure Update のまとめです。

| 分類 | 件数 |
| --- | --- |
| GA (一般提供) | 17 |
| パブリックプレビュー | 28 |
| プライベートプレビュー | 1 |
| リタイア | 1 |
| その他 | 3 |
| **合計** | **50** |

## GA (一般提供)

- **Generally Available: Governance policy guidance in Foundry Canvas and VS Code**[^1]
    - Microsoft Foundry governance guidance is now available in Foundry Canvas and the Foundry Toolkit for Visual Studio Code. As developers build agents, both experiences surface relevant policies for...

- **Generally Available: Azure Cobalt 200 Arm-based Dpsv7, Dplsv7, Epsv7, Mpsv4, and Lpsv5-series Virtual Machines**[^2]
    - The general purpose Dpsv7 and Dplsv7, memory-optimized Epsv7, high-memory Mpsv4, and dense storage Lpsv5 VMs are now generally available. These virtual machines deliver significant enhancements over...

- **Generally Available: Soft delete in Azure Compute Gallery**[^3]
    - Soft delete in Azure Compute Gallery is now generally available, so you can recover image versions that were deleted by accident. You can set a retention period of 7 to 365 days. During retention,...

- **Generally Available: Cross-subscription backup for Azure Virtual Machines in Azure Backup**[^4]
    - Azure Backup now supports cross-subscription backup for Azure Virtual Machines, enabling customers to protect VMs using a Recovery Services vault located in a different Azure subscription within the...

- **Generally Available: Intel and AMD v6 with temp disk for Azure Database for PostgreSQL**[^5]
    - Azure Database for PostgreSQL Flexible Server is announcing the general availability of Intel and AMD v6 compute tiers with local temporary disk. The new v6 generation expands the Flexible Server...

- **Generally Available: Intel and AMD v5 diskless tier for Azure Database for PostgreSQL**[^6]
    - Azure Database for PostgreSQL Flexible Server is announcing the general availability of Intel and AMD V5 diskless compute. These new options expand the v5 compute portfolio with General Purpose and...

- **Generally Available: Cobalt 200 compute for Azure Database for PostgreSQL**[^7]
    - Azure Database for PostgreSQL Flexible Server is announcing the general availability of Cobalt 200 ARM-based compute. Cobalt 200 expands the Flexible Server compute portfolio with Microsoft-designed...

- **Generally Available: Geo-redundant backup and restore for Azure HorizonDB**[^8]
    - Geo-redundant backup and restore for Azure HorizonDB is now available. You can use geo-redundant backups to strengthen data protection and restore your HorizonDB deployment in another Azure region...

- **Generally Available: Throughput buckets in Azure Cosmos DB**[^9]
    - We're excited to announce the general availability of throughput buckets in Azure Cosmos DB. You can manage the resource consumption of multiple workloads using the same container by limiting the...

- **Generally Available: Semantic Reranker in Azure Cosmos DB**[^10]
    - Semantic Reranker in Azure Cosmos DB improves search relevance by reordering candidate results based on the meaning of the search text and surrounding context. It uses an AI model to evaluate...

- **Generally Available: Database Hub real-time performance dashboards**[^11]
    - Database Hub in Microsoft Fabric gives you built-in, real-time performance dashboards for Microsoft SQL, Azure Database for PostgreSQL flexible server, and Azure Cosmos DB in one place. From the...

- **Generally Available: Near-instant provisioning for Azure DocumentDB clusters**[^12]
    - Now the M10 to M30 computer tiers are available for near-instant provisioning. Historically, the free tier in Azure DocumentDB was made available for instant provisioning. The goal was to help you...

- **Generally Available: Network egress controls for hosted agents in Microsoft Foundry**[^13]
    - Network egress controls for hosted agents in Foundry Agent Service are now generally available. Create rules that allow or deny destinations, or rewrite destinations. Audit mode logs deny decisions...

- **Generally Available: MCP server knowledge sources in Foundry IQ**[^14]
    - Foundry IQ supported Model Context Protocol (MCP) servers as federated knowledge sources, is generally available. Customers register an MCP server as a read-only knowledge source in Foundry IQ. MCP...

- **Generally Available: Semantic chunking and image descriptions with Azure Content Understanding in Foundry IQ**[^15]
    - Foundry IQ—formerly Azure AI Search—now offers generally available semantic chunking and optional AI-generated image descriptions through the Azure Content Understanding skill. The skill uses...

- **Generally Available: Snapshot backup for SQL Server in Azure VMs**[^16]
    - Azure Backup now supports snapshot-based backup for SQL Server running on Azure Virtual Machines. This new capability uses Azure disk snapshots combined with native SQL transaction log backups to...

- **Generally Available: Confidential VMs with Intel TDX support on AKS**[^17]
    - Customers standardized on Intel Trust Domain Extensions (TDX) for attestation and hardware confidentiality can't run those workloads on AKS Confidential VM node pools today, because CVM node images...

## パブリックプレビュー

- **Public Preview: Microsoft Copilot harness support in Foundry Toolkit for VS Code**[^18]
    - Agent Builder in Microsoft Foundry Toolkit for Visual Studio Code supports prompt agents that use the Microsoft Copilot harness in public preview. Developers can configure tools and skills, edit...

- **Public Preview: Programmed Training in Microsoft Foundry**[^19]
    - Programmed Training, an API for building your own post-training loop over open-weight models, is available in public preview in Microsoft Foundry. Access is available by request through the preview...

- **Public Preview: Multi-turn evaluation in Microsoft Foundry**[^20]
    - Multi-turn evaluation is now in public preview in Microsoft Foundry. You can assess complete agent conversations against your quality standards, not only individual responses. A response can look...

- **Public Preview: Azure Firewall for Containers**[^21]
    - Azure Firewall for Containers extends Azure Firewall protection to containerized workloads, providing a centralized approach to securing network traffic for container environments. Customers can use...

- **Public Preview: PostgreSQL 19 on Azure Database for PostgreSQL**[^22]
    - You can now try PostgreSQL 19 in public preview on Azure Database for PostgreSQL – Flexible Server in the East Asia region. With this preview, you can provision new PostgreSQL 19 servers through the...

- **Public Preview: Zone resilience for Azure VMs**[^23]
    - Zone resilience for Azure VMs, now in public preview, lets you recover an eligible zonal VM in another availability zone in the same region, retaining the existing VM resource and configuration. ZRS...

- **Public Preview: Database Agent for Azure Database for PostgreSQL**[^24]
    - Database Agent helps you detect, understand, and respond to database health and performance issues more quickly in Azure Database for PostgreSQL. It proactively monitors database health to identify...

- **Public Preview: AI bot ruleset for Azure Front Door Premium WAF**[^25]
    - Announcing the public preview of the AI bot ruleset for Azure Web Application Firewall (WAF) on Azure Front Door Premium. AI crawlers and agents visit your site for different reasons, and you may...

- **Public Preview: AI-powered application and database modernization with Modernize CLI**[^26]
    - Modernize CLI brings application and database modernization together as one connected, agentic journey. It assesses application architecture, dependencies, and cloud readiness while discovering the...

- **Public Preview: Immutable snapshots for Azure Disk Storage**[^27]
    - Immutable snapshots for Azure Disk Storage are now available in public preview. You can now apply an immutability policy to snapshots of any Azure disk type to prevent deletion for up to 90 days....

- **Generally Available: Customize backup retention from 1 to 35 days in Azure HorizonDB**[^28]
    - You can now configure backup retention for your Azure HorizonDB deployments from 1 to 35 days, giving you greater flexibility to align backup retention with your application and data protection...

- **Limited Preview: AI model management in Azure HorizonDB**[^29]
    - AI model management in Azure HorizonDB is now in limited preview, designed to simplify how you bring AI into your database. With just a single step, you can provision fully managed AI models for...

- **Public Preview: Pod Sandboxing kata-vm-isolation-v2 runtime class**[^30]
    - Isolated pods should not force a tradeoff between security and startup performance. With classic sandboxed pod flows, every pod boots a new Kata VM, which adds cold-start latency and extra memory...

- **Pulic Preview: Azure Elastic SAN Next Generation**[^31]
    - Azure Elastic SAN Next Generation is now in public preview. Elastic SAN Next Generation keeps the core benefits customers value in Elastic SAN today: a single SAN resource hierarchy to consolidate...

- **Limited Preview: Azure Workload Center for SAP and Azure Copilot Run SAP Agent**[^32]
    - Azure Workload Center for SAP, together with the Azure Copilot Run SAP Agent, is a workload-aware experience, powered by Workload Virtual Instance (WVI) for operating SAP workloads on Azure. Azure...

- **Limited Preview: Azure Workload Center for Oracle and Azure Copilot Run Oracle Agent**[^33]
    - Azure Workload Center for Oracle, together with the Azure Copilot Run Oracle Agent, is a workload-aware experience, powered by Workload Virtual Instance (WVI) for operating Oracle workloads on Azure....

- **Public Preview: Database Agent for SQL with contextual Copilot**[^34]
    - Database Agent now gives you AI-generated, evidence-grounded recommendations for detected database issues, including why the issue matters, the likely cause, and the recommended next step....

- **Public Preview: Azure SQL DB Hyperscale Cross Database Querying**[^35]
    - Native cross-database queries in Azure SQL Database Hyperscale let applications access and join data across databases in the same Hyperscale elastic pool on a logical server, using familiar T-SQL...

- **Public Preview: Confidential VMs with OS Disk Encryption support on AKS**[^36]
    - Regulated customers running AKS Confidential VM node pools protect workloads in memory today, but the OS disk isn't encrypted at rest, so they have to close the data-at-rest gap outside the platform....

- **Generally Available: Private endpoint support for Azure HorizonDB clusters**[^37]
    - You can now connect to Azure HorizonDB clusters privately through Azure Private Link, using a private IP address from your virtual network. Private DNS integration makes connection setup easier,...

- **Public Preview: Service tags for inbound rules in network security perimeter**[^38]
    - Announcing the public preview of 'service tags as inbound rules' support for third-party customers in network security perimeter. This new capability simplifies how customers manage access to in...

- **Public Preview: Perimeter link (cross perimeter) in network security perimeter**[^39]
    - This capability enables secure connectivity between resources protected by different network security perimeters, while maintaining strong perimeter-based access controls. With this release,...

- **Public Preview: Agent Grid helping secure AI agent communications**[^40]
    - Agent Grid is now in public preview, bringing identity-based Zero Trust network security to AI agents on supported Azure environments. Security teams can govern communications among agents, models,...

- **Public Preview: Azure Adaptive Virtual Patching**[^41]
    - Azure Adaptive Virtual Patching introduces an AI-orchestrated Adaptive Shield designed to reduce exposure to new, emerging, and newly disclosed zero-day vulnerabilities while customers test and...

- **Public Preview: AI Security add-on for Azure Firewall Premium**[^42]
    - AI Security, a new add-on for Azure Firewall Premium, is now in public preview. Announced at Microsoft Ignite, it introduces five capabilities to help you protect AI applications, safeguard sensitive...

- **Public Preview: Azure Bastion RDP and SSH vision**[^43]
    - Azure Bastion RDP and SSH vision is now in public preview, bringing AI-assisted review to recorded privileged sessions. Security and operations teams can use session summaries and insights into...

- **Public Preview: Agent Sandbox cluster extension**[^44]
    - Running AI agents that execute untrusted, model-generated code requires isolated environments for each session. Today, teams building on Kubernetes assemble their own sandbox lifecycle, storage, and...

- **Public Preview: Scale ExpressRoute Direct connectivity with link groups**[^45]
    - Azure ExpressRoute is introducing link groups for ExpressRoute Direct, enabling high-throughput workloads to scale network connectivity while reducing operational complexity. Instead of managing...

## プライベートプレビュー

- **Private Preview: Azure DH/EHasv8 VMs based on 6th Gen AMD EPYC™ (“Venice”) processors**[^46]
    - We are announcing the preview of the new Azure DHasv8, DHalsv8 and EHasv8-series virtual machines (VMs), powered by 6th Generation AMD EPYC™ (“Venice”) processors. Designed for the next generation of...

## リタイア

- **Retirement: Support for Azure Functions OpenAI Extension ends on April 20, 2027**[^47]
    - Support for Azure Functions OpenAI extension will end on April 20, 2027. Please migrate to OpenAI, Microsoft Foundry, or Azure AI Search SDKs directly, depending on your scenario, by that date. Until...

## その他

- **Announcing: Multiparty private offers in Microsoft Marketplace expands to Malaysia and Saudi Arabia**[^48]
    - Multiparty private offers give Microsoft partners a way to procure third-party cloud and AI solutions for customers through Marketplace. Software companies can expand into new markets by working with...

- **Announcing: The new Azure Databricks on Azure Government is now in Beta**[^49]
    - A new Azure Databricks environment is now available in Beta on Microsoft Azure Government. It brings the modern data and AI platform from global Azure to U.S. public sector agencies and their...

- **Announcing: Azure Boost observability for NVMe disks**[^50]
    - Azure Boost observability for NVMe disks is an open-source command-line tool that you run inside compatible Azure VMs. Backed by Azure Boost, the tool provides remote disk I/O and latency metrics and...

[^1]: Generally Available: Governance policy guidance in Foundry Canvas and VS Code, https://azure.microsoft.com/ja-jp/updates/v2/581463
[^2]: Generally Available: Azure Cobalt 200 Arm-based Dpsv7, Dplsv7, Epsv7, Mpsv4, and Lpsv5-series Virtual Machines, https://azure.microsoft.com/ja-jp/updates/v2/564451
[^3]: Generally Available: Soft delete in Azure Compute Gallery, https://azure.microsoft.com/ja-jp/updates/v2/581907
[^4]: Generally Available: Cross-subscription backup for Azure Virtual Machines in Azure Backup, https://azure.microsoft.com/ja-jp/updates/v2/581048
[^5]: Generally Available: Intel and AMD v6 with temp disk for Azure Database for PostgreSQL, https://azure.microsoft.com/ja-jp/updates/v2/579590
[^6]: Generally Available: Intel and AMD v5 diskless tier for Azure Database for PostgreSQL, https://azure.microsoft.com/ja-jp/updates/v2/579595
[^7]: Generally Available: Cobalt 200 compute for Azure Database for PostgreSQL, https://azure.microsoft.com/ja-jp/updates/v2/579585
[^8]: Generally Available: Geo-redundant backup and restore for Azure HorizonDB, https://azure.microsoft.com/ja-jp/updates/v2/574168
[^9]: Generally Available: Throughput buckets in Azure Cosmos DB, https://azure.microsoft.com/ja-jp/updates/v2/571488
[^10]: Generally Available: Semantic Reranker in Azure Cosmos DB, https://azure.microsoft.com/ja-jp/updates/v2/577520
[^11]: Generally Available: Database Hub real-time performance dashboards, https://azure.microsoft.com/ja-jp/updates/v2/579644
[^12]: Generally Available: Near-instant provisioning for Azure DocumentDB clusters, https://azure.microsoft.com/ja-jp/updates/v2/579349
[^13]: Generally Available: Network egress controls for hosted agents in Microsoft Foundry, https://azure.microsoft.com/ja-jp/updates/v2/571821
[^14]: Generally Available: MCP server knowledge sources in Foundry IQ, https://azure.microsoft.com/ja-jp/updates/v2/563411
[^15]: Generally Available: Semantic chunking and image descriptions with Azure Content Understanding in Foundry IQ, https://azure.microsoft.com/ja-jp/updates/v2/563661
[^16]: Generally Available: Snapshot backup for SQL Server in Azure VMs, https://azure.microsoft.com/ja-jp/updates/v2/564668
[^17]: Generally Available: Confidential VMs with Intel TDX support on AKS, https://azure.microsoft.com/ja-jp/updates/v2/581130
[^18]: Public Preview: Microsoft Copilot harness support in Foundry Toolkit for VS Code, https://azure.microsoft.com/ja-jp/updates/v2/581468
[^19]: Public Preview: Programmed Training in Microsoft Foundry, https://azure.microsoft.com/ja-jp/updates/v2/581713
[^20]: Public Preview: Multi-turn evaluation in Microsoft Foundry, https://azure.microsoft.com/ja-jp/updates/v2/581746
[^21]: Public Preview: Azure Firewall for Containers, https://azure.microsoft.com/ja-jp/updates/v2/581963
[^22]: Public Preview: PostgreSQL 19 on Azure Database for PostgreSQL, https://azure.microsoft.com/ja-jp/updates/v2/574587
[^23]: Public Preview: Zone resilience for Azure VMs, https://azure.microsoft.com/ja-jp/updates/v2/581254
[^24]: Public Preview: Database Agent for Azure Database for PostgreSQL, https://azure.microsoft.com/ja-jp/updates/v2/579579
[^25]: Public Preview: AI bot ruleset for Azure Front Door Premium WAF, https://azure.microsoft.com/ja-jp/updates/v2/581604
[^26]: Public Preview: AI-powered application and database modernization with Modernize CLI, https://azure.microsoft.com/ja-jp/updates/v2/579943
[^27]: Public Preview: Immutable snapshots for Azure Disk Storage, https://azure.microsoft.com/ja-jp/updates/v2/581503
[^28]: Generally Available: Customize backup retention from 1 to 35 days in Azure HorizonDB, https://azure.microsoft.com/ja-jp/updates/v2/574163
[^29]: Limited Preview: AI model management in Azure HorizonDB, https://azure.microsoft.com/ja-jp/updates/v2/563097
[^30]: Public Preview: Pod Sandboxing kata-vm-isolation-v2 runtime class, https://azure.microsoft.com/ja-jp/updates/v2/581120
[^31]: Pulic Preview: Azure Elastic SAN Next Generation, https://azure.microsoft.com/ja-jp/updates/v2/581634
[^32]: Limited Preview: Azure Workload Center for SAP and Azure Copilot Run SAP Agent, https://azure.microsoft.com/ja-jp/updates/v2/581209
[^33]: Limited Preview: Azure Workload Center for Oracle and Azure Copilot Run Oracle Agent, https://azure.microsoft.com/ja-jp/updates/v2/581214
[^34]: Public Preview: Database Agent for SQL with contextual Copilot, https://azure.microsoft.com/ja-jp/updates/v2/580091
[^35]: Public Preview: Azure SQL DB Hyperscale Cross Database Querying, https://azure.microsoft.com/ja-jp/updates/v2/579221
[^36]: Public Preview: Confidential VMs with OS Disk Encryption support on AKS, https://azure.microsoft.com/ja-jp/updates/v2/581125
[^37]: Generally Available: Private endpoint support for Azure HorizonDB clusters, https://azure.microsoft.com/ja-jp/updates/v2/574153
[^38]: Public Preview: Service tags for inbound rules in network security perimeter, https://azure.microsoft.com/ja-jp/updates/v2/579201
[^39]: Public Preview: Perimeter link (cross perimeter) in network security perimeter, https://azure.microsoft.com/ja-jp/updates/v2/579206
[^40]: Public Preview: Agent Grid helping secure AI agent communications, https://azure.microsoft.com/ja-jp/updates/v2/580684
[^41]: Public Preview: Azure Adaptive Virtual Patching, https://azure.microsoft.com/ja-jp/updates/v2/580689
[^42]: Public Preview: AI Security add-on for Azure Firewall Premium, https://azure.microsoft.com/ja-jp/updates/v2/580694
[^43]: Public Preview: Azure Bastion RDP and SSH vision, https://azure.microsoft.com/ja-jp/updates/v2/580699
[^44]: Public Preview: Agent Sandbox cluster extension, https://azure.microsoft.com/ja-jp/updates/v2/580916
[^45]: Public Preview: Scale ExpressRoute Direct connectivity with link groups, https://azure.microsoft.com/ja-jp/updates/v2/580926
[^46]: Private Preview: Azure DH/EHasv8 VMs based on 6th Gen AMD EPYC™ (“Venice”) processors, https://azure.microsoft.com/ja-jp/updates/v2/581308
[^47]: Retirement: Support for Azure Functions OpenAI Extension ends on April 20, 2027, https://azure.microsoft.com/ja-jp/updates/v2/579952
[^48]: Announcing: Multiparty private offers in Microsoft Marketplace expands to Malaysia and Saudi Arabia, https://azure.microsoft.com/ja-jp/updates/v2/580700
[^49]: Announcing: The new Azure Databricks on Azure Government is now in Beta, https://azure.microsoft.com/ja-jp/updates/v2/581645
[^50]: Announcing: Azure Boost observability for NVMe disks, https://azure.microsoft.com/ja-jp/updates/v2/581227
