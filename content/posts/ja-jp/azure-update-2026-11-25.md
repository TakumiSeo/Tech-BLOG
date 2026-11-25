Title: Azure Update (2026/11/17 - 2026/11/24)
Date: 2026-11-25
Slug: azure-update-2026-11-25
Lang: ja-jp
Category: notebook
Tags: ai-machine-learning, analytics, application-gateway, azure, azure-ai-content-safety, azure-backup, azure-cosmos-db, azure-database-for-postgresql, azure-databricks, azure-disk-storage, azure-firewall, azure-front-door, azure-functions, azure-horizondb, azure-kubernetes-service-aks, azure-site-recovery, azure-sql-database, azure-updates, compute, containers, databases, hybrid-multicloud, internet-of-things, management-and-governance, microsoft-foundry, migration, networking, security, storage, virtual-machines, web-application-firewall
Summary: 2026年11月17日〜11月24日の Azure Update まとめ。GA 19件、パブリックプレビュー 26件、リタイア 2件、その他 3件の計50件。

2026年11月17日〜11月24日の Azure Update のまとめです。

| 分類 | 件数 |
| --- | --- |
| GA (一般提供) | 19 |
| パブリックプレビュー | 26 |
| リタイア | 2 |
| その他 | 3 |
| **合計** | **50** |

## GA (一般提供)

- **Generally Available: Azure Site Recovery support for zonal disaster recovery for Ultra disks**[^1]
    - Azure Site Recovery now supports Zone-to-Zone Disaster Recovery (Zonal DR) for Azure Ultra disks. Customers can protect performance-intensive virtual machines across Availability Zones against zonal...

- **Generally Available: Use Azure Storage permissions in Azure AI Search and Foundry IQ**[^2]
    - Azure AI Search and Foundry IQ in Microsoft Foundry can use supported Azure Storage permissions to control access to search results. Once configured, search applications and AI agents return content...

- **Public Preview: Style and instruction control for HD V3 voices in Azure Speech in Foundry Tools**[^3]
    - Azure Speech in Foundry Tools provides HD V3 voices with style and instruction control in public preview. Use supported controls to shape voice delivery for voice agents, narration, and other speech...

- **Generally Available: Agent insights in Microsoft Foundry**[^4]
    - In Microsoft Foundry, insights analyze agent traces to surface recurring patterns and group related issues. Review an insight and its supporting traces to investigate common failures and decide what...

- **Generally Available: Files knowledge source for Foundry IQ**[^5]
    - Upload files directly to a managed knowledge source in Foundry IQ. Foundry IQ processes and indexes the files for retrieval through a knowledge base, so you don't need to provision a storage account...

- **Generally Available: Model router now supports the Responses API protocol in Microsoft Foundry**[^6]
    - Model router in Microsoft Foundry now supports the Responses API protocol in general availability on both resource and project endpoints. Set model to your model router deployment name to add...

- **Generally Available: Deploy hosted agents from your own container registry in Foundry Toolkit for VS Code**[^7]
    - Foundry Toolkit for Visual Studio Code now deploys hosted agents from prebuilt images in customer-managed container registries, including registries other than Azure Container Registry. Choose the...

- **Generally Available: Wildcard domain support in Azure Firewall network rules**[^8]
    - Wildcard domain support in Azure Firewall network rules is now generally available. This capability enables customers to use wildcard patterns, such as *.contoso.com, when defining FQDN-based network...

- **Generally Available: WAF Insights for Azure Application Gateway**[^9]
    - WAF Insights for Azure Application Gateway Web Application Firewall (WAF) is now generally available. WAF Insights is a built-in experience in the WAF policy that brings WAF logs and metrics together...

- **Generally Available: WAF Insights for Azure Front Door**[^10]
    - WAF Insights is now generally available for Azure Front Door Web Application Firewall (WAF). WAF Insights is a built-in experience in the WAF policy that brings WAF logs and metrics together in...

- **Generally Available: Governance policy guidance in Foundry Canvas and VS Code**[^11]
    - Microsoft Foundry governance guidance is now available in Foundry Canvas and the Foundry Toolkit for Visual Studio Code. As developers build agents, both experiences surface relevant policies for...

- **Generally Available: Azure Cobalt 200 Arm-based Dpsv7, Dplsv7, Epsv7, Mpsv4, and Lpsv5-series Virtual Machines**[^12]
    - The general purpose Dpsv7 and Dplsv7, memory-optimized Epsv7, high-memory Mpsv4, and dense storage Lpsv5 VMs are now generally available. These virtual machines deliver significant enhancements over...

- **Generally Available: Soft delete in Azure Compute Gallery**[^13]
    - Soft delete in Azure Compute Gallery is now generally available, so you can recover image versions that were deleted by accident. You can set a retention period of 7 to 365 days. During retention,...

- **Generally Available: Cross-subscription backup for Azure Virtual Machines in Azure Backup**[^14]
    - Azure Backup now supports cross-subscription backup for Azure Virtual Machines, enabling customers to protect VMs using a Recovery Services vault located in a different Azure subscription within the...

- **Generally Available: Intel and AMD v6 with temp disk for Azure Database for PostgreSQL**[^15]
    - Azure Database for PostgreSQL Flexible Server is announcing the general availability of Intel and AMD v6 compute tiers with local temporary disk. The new v6 generation expands the Flexible Server...

- **Generally Available: Intel and AMD v5 diskless tier for Azure Database for PostgreSQL**[^16]
    - Azure Database for PostgreSQL Flexible Server is announcing the general availability of Intel and AMD V5 diskless compute. These new options expand the v5 compute portfolio with General Purpose and...

- **Generally Available: Cobalt 200 compute for Azure Database for PostgreSQL**[^17]
    - Azure Database for PostgreSQL Flexible Server is announcing the general availability of Cobalt 200 ARM-based compute. Cobalt 200 expands the Flexible Server compute portfolio with Microsoft-designed...

- **Generally Available: Geo-redundant backup and restore for Azure HorizonDB**[^18]
    - Geo-redundant backup and restore for Azure HorizonDB is now available. You can use geo-redundant backups to strengthen data protection and restore your HorizonDB deployment in another Azure region...

- **Generally Available: Throughput buckets in Azure Cosmos DB**[^19]
    - We're excited to announce the general availability of throughput buckets in Azure Cosmos DB. You can manage the resource consumption of multiple workloads using the same container by limiting the...

## パブリックプレビュー

- **Public Preview: Optimize agents from insights in Foundry Agent Service**[^20]
    - Optimization from insights is in public preview in Foundry Agent Service. In the Foundry portal, start from an eligible insight in a prompt-agent trace to generate and evaluate candidate changes to...

- **Public Preview: Govern MCP tools with your own gateway in Microsoft Foundry Agent Service**[^21]
    - In public preview, Microsoft Foundry Agent Service lets you route MCP tool traffic through existing AI Gateway or Azure API Management endpoints that your organization manages. Configure the MCP...

- **Public Preview: Native A2A passthrough for hosted agents in Foundry Agent Service**[^22]
    - Bring your existing Agent2Agent (A2A) agents to Agent Service without a protocol conversion layer. Previously, Agent Service converted incoming A2A requests to the Responses protocol. With A2A...

- **Public Preview: Azure Developer CLI extension for Azure Document Intelligence and Content Understanding in Foundry Tools**[^23]
    - Within Microsoft Foundry, use azd ai cu commands to analyze documents with Azure Document Intelligence and Content Understanding in Foundry Tools. The extension for Azure Developer CLI ( azd ) can...

- **Public Preview: Cost controls for model and agent spending in Microsoft Foundry**[^24]
    - Within Microsoft Foundry, cost controls set a spending or token budget for a Foundry resource or project. When usage reaches a threshold that you set, a cost control sends an alert through Azure...

- **Public Preview: Central governance of hosted-agent outbound domains in Foundry Agent Service**[^25]
    - Administrators can use Azure Policy to govern outbound destinations for hosted agents in Foundry Agent Service. Agent authors configure and attach a compliant egress policy before creating an agent...

- **Public Preview: Enterprise Knowledge Graph in Foundry IQ**[^26]
    - Foundry IQ adds Enterprise Knowledge Graph as a knowledge source for questions that depend on relationships across your content. During indexing, it extracts entities and relationships from...

- **Public Preview: Updated Guardrails experience in Microsoft Foundry**[^27]
    - In Microsoft Foundry, Guardrails helps developers configure runtime safety controls for agents, including classifiers, deterministic rules, and LLM-based judges. When an administrator policy requires...

- **Public Preview: IQ Retriever Zero in Foundry IQ**[^28]
    - Foundry IQ can use an iterative retrieval model to break complex questions into focused searches. The model reviews search results and searches again when needed, within a configured budget, then...

- **Public Preview: Human annotation for agent evaluations in Microsoft Foundry**[^29]
    - Human annotation for agent evaluations is in public preview in Microsoft Foundry, as announced in the Microsoft IQ launch blog . Reviewers can add ratings, tags, comments, and expected outputs to...

- **Public Preview: Call model router without a deployment in Microsoft Foundry**[^30]
    - Microsoft Foundry now lets you use model router without deploying it first. In a region that supports model router, set model to auto in a Responses or Chat Completions request to your Foundry...

- **Public Preview: Use the Messages API with model router in Microsoft Foundry**[^31]
    - Model router in Microsoft Foundry supports the Messages API in public preview. Messages-based applications and coding tools can use automatic model selection while keeping the Anthropic request and...

- **Public Preview: Use your model deployments with model router in Microsoft Foundry**[^32]
    - Model router in Microsoft Foundry can use your existing model deployments to serve routed requests, in public preview. This helps you use capacity you already have while model router selects a model...

- **Public Preview: Use model router with AI Gateway**[^33]
    - Automatic model selection in AI Gateway uses model router from Microsoft Foundry to rank the models behind a model alias for each request. The gateway combines that ranking with the alias's...

- **Public Preview: Azure Database for PostgreSQL enhanced Burstable tier (Basv2)**[^34]
    - Enhanced Burstable tier (Basv2) builds on the existing burstable model with improved performance predictability and more efficient burst utilization, delivering a better cost-performance balance. Now...

- **Public Preview: Microsoft Copilot harness support in Foundry Toolkit for VS Code**[^35]
    - Agent Builder in Microsoft Foundry Toolkit for Visual Studio Code supports prompt agents that use the Microsoft Copilot harness in public preview. Developers can configure tools and skills, edit...

- **Public Preview: Programmed Training in Microsoft Foundry**[^36]
    - Programmed Training, an API for building your own post-training loop over open-weight models, is available in public preview in Microsoft Foundry. Access is available by request through the preview...

- **Public Preview: Multi-turn evaluation in Microsoft Foundry**[^37]
    - Multi-turn evaluation is now in public preview in Microsoft Foundry. You can assess complete agent conversations against your quality standards, not only individual responses. A response can look...

- **Public Preview: Azure Firewall for Containers**[^38]
    - Azure Firewall for Containers extends Azure Firewall protection to containerized workloads, providing a centralized approach to securing network traffic for container environments. Customers can use...

- **Public Preview: PostgreSQL 19 on Azure Database for PostgreSQL**[^39]
    - You can now try PostgreSQL 19 in public preview on Azure Database for PostgreSQL – Flexible Server in the East Asia region. With this preview, you can provision new PostgreSQL 19 servers through the...

- **Public Preview: Zone resilience for Azure VMs**[^40]
    - Zone resilience for Azure VMs, now in public preview, lets you recover an eligible zonal VM in another availability zone in the same region, retaining the existing VM resource and configuration. ZRS...

- **Public Preview: Database Agent for Azure Database for PostgreSQL**[^41]
    - Database Agent helps you detect, understand, and respond to database health and performance issues more quickly in Azure Database for PostgreSQL. It proactively monitors database health to identify...

- **Public Preview: AI bot ruleset for Azure Front Door Premium WAF**[^42]
    - Announcing the public preview of the AI bot ruleset for Azure Web Application Firewall (WAF) on Azure Front Door Premium. AI crawlers and agents visit your site for different reasons, and you may...

- **Public Preview: AI-powered application and database modernization with Modernize CLI**[^43]
    - Modernize CLI brings application and database modernization together as one connected, agentic journey. It assesses application architecture, dependencies, and cloud readiness while discovering the...

- **Public Preview: Immutable snapshots for Azure Disk Storage**[^44]
    - Immutable snapshots for Azure Disk Storage are now available in public preview. You can now apply an immutability policy to snapshots of any Azure disk type to prevent deletion for up to 90 days....

- **Generally Available: Customize backup retention from 1 to 35 days in Azure HorizonDB**[^45]
    - You can now configure backup retention for your Azure HorizonDB deployments from 1 to 35 days, giving you greater flexibility to align backup retention with your application and data protection...

## リタイア

- **Retirement: Azure AI Content Safety selected features will be retired on April 30, 2027**[^46]
    - The following Azure AI Content Safety preview capabilities will retire on April 30, 2027: Analyze Multimodal Custom categories (rapid), including text and image Connected containers for Text, Image,...

- **Retirement: Support for Azure Functions OpenAI Extension ends on April 20, 2027**[^47]
    - Support for Azure Functions OpenAI extension will end on April 20, 2027. Please migrate to OpenAI, Microsoft Foundry, or Azure AI Search SDKs directly, depending on your scenario, by that date. Until...

## その他

- **Announcing: Multiparty private offers in Microsoft Marketplace expands to Malaysia and Saudi Arabia**[^48]
    - Multiparty private offers give Microsoft partners a way to procure third-party cloud and AI solutions for customers through Marketplace. Software companies can expand into new markets by working with...

- **Announcing: The new Azure Databricks on Azure Government is now in Beta**[^49]
    - A new Azure Databricks environment is now available in Beta on Microsoft Azure Government. It brings the modern data and AI platform from global Azure to U.S. public sector agencies and their...

- **Announcing: Azure Boost observability for NVMe disks**[^50]
    - Azure Boost observability for NVMe disks is an open-source command-line tool that you run inside compatible Azure VMs. Backed by Azure Boost, the tool provides remote disk I/O and latency metrics and...

[^1]: Generally Available: Azure Site Recovery support for zonal disaster recovery for Ultra disks, https://azure.microsoft.com/ja-jp/updates/v2/582171
[^2]: Generally Available: Use Azure Storage permissions in Azure AI Search and Foundry IQ, https://azure.microsoft.com/ja-jp/updates/v2/581303
[^3]: Public Preview: Style and instruction control for HD V3 voices in Azure Speech in Foundry Tools, https://azure.microsoft.com/ja-jp/updates/v2/581353
[^4]: Generally Available: Agent insights in Microsoft Foundry, https://azure.microsoft.com/ja-jp/updates/v2/581363
[^5]: Generally Available: Files knowledge source for Foundry IQ, https://azure.microsoft.com/ja-jp/updates/v2/581368
[^6]: Generally Available: Model router now supports the Responses API protocol in Microsoft Foundry, https://azure.microsoft.com/ja-jp/updates/v2/581393
[^7]: Generally Available: Deploy hosted agents from your own container registry in Foundry Toolkit for VS Code, https://azure.microsoft.com/ja-jp/updates/v2/581478
[^8]: Generally Available: Wildcard domain support in Azure Firewall network rules, https://azure.microsoft.com/ja-jp/updates/v2/582030
[^9]: Generally Available: WAF Insights for Azure Application Gateway, https://azure.microsoft.com/ja-jp/updates/v2/579280
[^10]: Generally Available: WAF Insights for Azure Front Door, https://azure.microsoft.com/ja-jp/updates/v2/579285
[^11]: Generally Available: Governance policy guidance in Foundry Canvas and VS Code, https://azure.microsoft.com/ja-jp/updates/v2/581463
[^12]: Generally Available: Azure Cobalt 200 Arm-based Dpsv7, Dplsv7, Epsv7, Mpsv4, and Lpsv5-series Virtual Machines, https://azure.microsoft.com/ja-jp/updates/v2/564451
[^13]: Generally Available: Soft delete in Azure Compute Gallery, https://azure.microsoft.com/ja-jp/updates/v2/581907
[^14]: Generally Available: Cross-subscription backup for Azure Virtual Machines in Azure Backup, https://azure.microsoft.com/ja-jp/updates/v2/581048
[^15]: Generally Available: Intel and AMD v6 with temp disk for Azure Database for PostgreSQL, https://azure.microsoft.com/ja-jp/updates/v2/579590
[^16]: Generally Available: Intel and AMD v5 diskless tier for Azure Database for PostgreSQL, https://azure.microsoft.com/ja-jp/updates/v2/579595
[^17]: Generally Available: Cobalt 200 compute for Azure Database for PostgreSQL, https://azure.microsoft.com/ja-jp/updates/v2/579585
[^18]: Generally Available: Geo-redundant backup and restore for Azure HorizonDB, https://azure.microsoft.com/ja-jp/updates/v2/574168
[^19]: Generally Available: Throughput buckets in Azure Cosmos DB, https://azure.microsoft.com/ja-jp/updates/v2/571488
[^20]: Public Preview: Optimize agents from insights in Foundry Agent Service, https://azure.microsoft.com/ja-jp/updates/v2/581483
[^21]: Public Preview: Govern MCP tools with your own gateway in Microsoft Foundry Agent Service, https://azure.microsoft.com/ja-jp/updates/v2/581498
[^22]: Public Preview: Native A2A passthrough for hosted agents in Foundry Agent Service, https://azure.microsoft.com/ja-jp/updates/v2/581313
[^23]: Public Preview: Azure Developer CLI extension for Azure Document Intelligence and Content Understanding in Foundry Tools, https://azure.microsoft.com/ja-jp/updates/v2/581318
[^24]: Public Preview: Cost controls for model and agent spending in Microsoft Foundry, https://azure.microsoft.com/ja-jp/updates/v2/581323
[^25]: Public Preview: Central governance of hosted-agent outbound domains in Foundry Agent Service, https://azure.microsoft.com/ja-jp/updates/v2/581328
[^26]: Public Preview: Enterprise Knowledge Graph in Foundry IQ, https://azure.microsoft.com/ja-jp/updates/v2/581333
[^27]: Public Preview: Updated Guardrails experience in Microsoft Foundry, https://azure.microsoft.com/ja-jp/updates/v2/581338
[^28]: Public Preview: IQ Retriever Zero in Foundry IQ, https://azure.microsoft.com/ja-jp/updates/v2/581343
[^29]: Public Preview: Human annotation for agent evaluations in Microsoft Foundry, https://azure.microsoft.com/ja-jp/updates/v2/581358
[^30]: Public Preview: Call model router without a deployment in Microsoft Foundry, https://azure.microsoft.com/ja-jp/updates/v2/581378
[^31]: Public Preview: Use the Messages API with model router in Microsoft Foundry, https://azure.microsoft.com/ja-jp/updates/v2/581383
[^32]: Public Preview: Use your model deployments with model router in Microsoft Foundry, https://azure.microsoft.com/ja-jp/updates/v2/581388
[^33]: Public Preview: Use model router with AI Gateway, https://azure.microsoft.com/ja-jp/updates/v2/581398
[^34]: Public Preview: Azure Database for PostgreSQL enhanced Burstable tier (Basv2), https://azure.microsoft.com/ja-jp/updates/v2/574535
[^35]: Public Preview: Microsoft Copilot harness support in Foundry Toolkit for VS Code, https://azure.microsoft.com/ja-jp/updates/v2/581468
[^36]: Public Preview: Programmed Training in Microsoft Foundry, https://azure.microsoft.com/ja-jp/updates/v2/581713
[^37]: Public Preview: Multi-turn evaluation in Microsoft Foundry, https://azure.microsoft.com/ja-jp/updates/v2/581746
[^38]: Public Preview: Azure Firewall for Containers, https://azure.microsoft.com/ja-jp/updates/v2/581963
[^39]: Public Preview: PostgreSQL 19 on Azure Database for PostgreSQL, https://azure.microsoft.com/ja-jp/updates/v2/574587
[^40]: Public Preview: Zone resilience for Azure VMs, https://azure.microsoft.com/ja-jp/updates/v2/581254
[^41]: Public Preview: Database Agent for Azure Database for PostgreSQL, https://azure.microsoft.com/ja-jp/updates/v2/579579
[^42]: Public Preview: AI bot ruleset for Azure Front Door Premium WAF, https://azure.microsoft.com/ja-jp/updates/v2/581604
[^43]: Public Preview: AI-powered application and database modernization with Modernize CLI, https://azure.microsoft.com/ja-jp/updates/v2/579943
[^44]: Public Preview: Immutable snapshots for Azure Disk Storage, https://azure.microsoft.com/ja-jp/updates/v2/581503
[^45]: Generally Available: Customize backup retention from 1 to 35 days in Azure HorizonDB, https://azure.microsoft.com/ja-jp/updates/v2/574163
[^46]: Retirement: Azure AI Content Safety selected features will be retired on April 30, 2027, https://azure.microsoft.com/ja-jp/updates/v2/577474
[^47]: Retirement: Support for Azure Functions OpenAI Extension ends on April 20, 2027, https://azure.microsoft.com/ja-jp/updates/v2/579952
[^48]: Announcing: Multiparty private offers in Microsoft Marketplace expands to Malaysia and Saudi Arabia, https://azure.microsoft.com/ja-jp/updates/v2/580700
[^49]: Announcing: The new Azure Databricks on Azure Government is now in Beta, https://azure.microsoft.com/ja-jp/updates/v2/581645
[^50]: Announcing: Azure Boost observability for NVMe disks, https://azure.microsoft.com/ja-jp/updates/v2/581227
