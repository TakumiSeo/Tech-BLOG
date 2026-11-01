Title: Azure Update (2026/10/01 - 2026/10/30)
Date: 2026-11-01
Slug: azure-update-2026-11-01
Lang: ja-jp
Category: notebook
Tags: ai-machine-learning, analytics, api-management, app-service, application-gateway, azure, azure-backup, azure-blob-storage, azure-container-apps, azure-cosmos-db, azure-data-lake-storage, azure-database-for-mysql, azure-database-for-postgresql, azure-databricks, azure-deployment-environments, azure-dns, azure-files, azure-front-door, azure-horizondb, azure-kubernetes-service-aks, azure-monitor, azure-nat-gateway, azure-private-link, azure-site-recovery, azure-sql-database, azure-stack-hub, azure-updates, compute, containers, databases, developer-tools, devops, hybrid-multicloud, identity, integration, internet-of-things, key-vault, management-and-governance, microsoft-azure-portal, microsoft-dev-box, microsoft-entra-id-formerly-azure-ad, microsoft-fabric, microsoft-foundry, migration, mobile, network-watcher, networking, sdks, security, sql-server-on-azure-virtual-machines, storage, traffic-manager, virtual-desktop-infrastructure, virtual-network, web, web-application-firewall
Summary: 2026年10月1日〜10月30日の Azure Update まとめ。GA 27件、パブリックプレビュー 12件、リタイア 7件、その他 4件の計50件。

2026年10月1日〜10月30日の Azure Update のまとめです。

| 分類 | 件数 |
| --- | --- |
| GA (一般提供) | 27 |
| パブリックプレビュー | 12 |
| リタイア | 7 |
| その他 | 4 |
| **合計** | **50** |

## GA (一般提供)

- **Generally Available: Large OS Disk Encryption for Azure Confidential VM migrations**[^1]
    - Large OS Disk Encryption (LOSDE) is now generally available for Azure Confidential VM migration scenarios. Organizations can move larger, production-scale workloads into confidential computing with...

- **Generally Available: HTTP DDoS ruleset for Azure Front Door Premium WAF**[^2]
    - Announcing the general availability of the HTTP DDoS ruleset for Azure Web Application Firewall (WAF) on Azure Front Door Premium. HTTP-layer DDoS attacks remain a leading cause of application...

- **Generally Available: Azure MCP Server 3.0**[^3]
    - Azure MCP Server 3.0 is now generally available, expanding how AI agents and developer tools interact with Azure through the open Model Context Protocol (MCP). This release introduces new and...

- **Generally Available: Marketplace private offer enhancements**[^4]
    - Private offers through Microsoft Marketplace help you optimize your spending power with pricing and terms aligned to your organization’s needs, including flexible billing, custom contract lengths,...

- **Generally Available: Higher limit of Azure Blob Storage accounts per region per subscription**[^5]
    - Higher Azure Storage account resource quotas are now generally available, supporting up to 1,000 storage accounts with standard endpoints per region, per subscription, up from the default of 250....

- **Generally Available: Cost management and tagging for Claude models in Microsoft Foundry**[^6]
    - Microsoft Foundry now brings Claude models into Azure Cost Management alongside the rest of your Foundry spend, generally available. Until now, Claude charges appeared under SaaS rather than under...

- **Generally Available: Azure Front Door profile and route level WAF policies**[^7]
    - Announcing the general availability of profile and route level policies for Azure Web Application Firewall (WAF) on Azure Front Door Premium. WAF policies are no longer limited to individual domains:...

- **Generally Available: Network Watcher VNet flow logs filtering**[^8]
    - Azure Network Watcher VNet flow logs filtering is now generally available, enabling you to control which network traffic flows are logged based on specific criteria such as IP addresses, ports,...

- **Generally Available: Item Level Recovery for Azure VMs with Premium SSDv2 and Ultra Disks in Azure Backup**[^9]
    - Azure Backup now supports Item-Level Recovery (ILR) for Azure virtual machines using Premium SSD v2 and Ultra disks with both 512 byte and 4KB logical sector sizes. You can now recover individual...

- **Generally Available: ABFS Vectored Read for Azure Data Lake Storage**[^10]
    - ABFS Vectored Read helps compatible analytics engines reduce request overhead for selective reads in Azure Data Lake Storage. By combining nearby file ranges into fewer storage requests and executing...

- **Generally Available: Azure Cosmos DB Safe Key Rotation**[^11]
    - Safe Key Rotation for Azure Cosmos DB is now generally available. You can view timestamp metadata showing when each account key was last used, helping you identify active keys before rotating or...

- **Generally Available: Service tag match condition for Azure Front Door Premium WAF**[^12]
    - Announcing the general availability of the service tag match condition for Azure Web Application Firewall (WAF) custom rules on Azure Front Door Premium. Service tags represent groups of IP address...

- **Generally Available: Keyless TLS on Application Gateway with Azure Key Vault Managed HSM**[^13]
    - Azure Application Gateway now supports keyless TLS termination using certificates whose private keys stay in Azure Key Vault Managed HSM. Each TLS handshake signature is performed inside the HSM, and...

- **Generally Available: Advanced platform metrics for Azure Monitor**[^14]
    - Advanced platform metrics for Azure Monitor are now generally available. Advanced platform metrics provide finer-grained signals that help customers more quickly and accurately identify changes and...

- **Generally Available: Metrics usage insights for Azure Monitor workspace**[^15]
    - Metrics usage insights is now generally available, giving you greater visibility into what’s driving metrics usage across your Azure Monitor workspace. Monitor workspace utilization, identify unused...

- **Generally Available: Azure DNS enables DNS-based load balancing through Traffic Manager linked records**[^16]
    - Azure DNS now provides DNS based load balancing by seamless integration with Azure Traffic Manager. Customers can directly associate an Azure DNS record set with a Traffic Manager profile,...

- **Generally Available: External key management for Azure Key Vault Managed HSM**[^17]
    - External key management for Azure Key Vault Managed HSM is now generally available in all Azure public regions. For organizations with regulatory or sovereignty requirements to retain physical...

- **Generally Available: Standard service endpoint**[^18]
    - Standard service endpoint, a new capability in the Azure Private Link family, provides a scalable and secure approach for connecting Azure IaaS workloads to Azure PaaS services. Standard service...

- **Generally Availabile: Automatic zone balance for Virtual Machine Scale Sets**[^19]
    - Automatic zone balance for Virtual Machine Scale Sets is now generally available. This feature continuously monitors scale sets deployed across availability zones and automatically redistributes VM...

- **Generally Available: Azure Cloud HSM hardware audit logging**[^20]
    - Hardware Audit Logging for Azure Cloud HSM provides hardware-generated audit records for supported HSM management operations, helping organizations strengthen security monitoring, compliance...

- **Generally Available: Azure Site Recovery Support for Azure ARC-enabled Windows VMWare/Physical servers**[^21]
    - Azure Site Recovery (ASR) now supports disaster recovery for Azure ARC-enabled Windows VMWare virtual machines and on-premise physical servers. Customers can protect ARC-managed machines with ASR...

- **Generally Available: Managed StandardV2 NAT Gateway for AKS**[^22]
    - AKS will now provision and manage a StandardV2 NAT Gateway for clusters using an AKS-managed virtual network. StandardV2 is now the default managed NAT Gateway SKU for new clusters in supported...

- **Generally Available: Azure Database for PostgreSQL flexible server in East US 3**[^23]
    - Now you can deploy Azure Database for PostgreSQL flexible server in the East US 3 Azure region. Learn more .

- **Generally Available: Exceptions in WAF for Azure Application Gateway and Azure Front Door**[^24]
    - Announcing the general availability of exceptions for Web Application Firewall on Azure Application Gateway and Azure Front Door. Azure Web Application Firewall (WAF) helps protect your web...

- **Generally Available: Anyscale on Azure**[^25]
    - Anyscale on Azure is now Generally Available. Anyscale on Azure is a managed platform for running distributed Python workloads on Ray. It deploys directly onto your Azure Kubernetes Service (AKS)...

- **Generally Available: Enabling the Bulk admin role for SQL Server on Linux**[^26]
    - Starting with SQL Server 2025 CU9 and SQL Server 2022 CU27, SQL Server on Linux supports the bulkadmin fixed server role and the ADMINISTER BULK OPERATIONS permission for performing bulk data import...

- **Generally Available: SQL Server on Azure Virtual Machines in Azure Bleu**[^27]
    - SQL Server on Azure Virtual Machines is now available in Azure Bleu, enabling you to deploy and manage SQL Server workloads in France's sovereign cloud environment while meeting data residency and...

## パブリックプレビュー

- **Public Preview: Support database-level managed identity (including FIC) in Create Database Scoped Credential T-SQL**[^28]
    - With database-level managed identity in Azure SQL Database, you can use a user-assigned managed identity for each database to query files in Azure Blob Storage and Azure Data Lake Storage Gen2...

- **Public Preview: Cross Tenant Restore with Azure Backup**[^29]
    - Cross-Tenant Restore (CTR) helps organizations establish an independent recovery path by enabling Azure VM backups to be restored into a separate Azure tenant. It strengthens cyber resilience while...

- **Public Preview: Disable VNet peering route**[^30]
    - Announcing the public preview of disable VNet peering route, a route-table capability that gives you more control over traffic between peered virtual networks. DPR suppresses system-generated peering...

- **Public Preview: Azure Databricks Private network gateway**[^31]
    - Private network gateway for Azure Databricks is now in Public Preview, enabling serverless compute to connect to resources in your virtual network (VNet) and transitively connected networks through a...

- **Public Preview: Azure Files cross-region data copy and synchronization with Azure Storage Mover**[^32]
    - Azure Files customers can now copy and synchronize file share data across storage accounts, Azure regions, and subscriptions within the same tenant using Azure Storage Mover. Schedule incremental...

- **Public Preview: Microsoft Agent 365 integration with Azure API Management**[^33]
    - The integration between Microsoft Agent 365 and Azure API Management is now available in public preview, helping organizations connect centralized governance with runtime enforcement for MCP servers...

- **Public Preview: AKS on bare metal now on Ubuntu**[^34]
    - Running Kubernetes on-premises often means adding a virtualization layer, adapting to unfamiliar infrastructure, or giving up control over the hardware and software your applications depend on. For...

- **Public Preview: Azure HorizonDB expands to additional regions**[^35]
    - Azure HorizonDB is expanding to additional Azure regions, giving you greater flexibility to deploy PostgreSQL workloads closer to your applications and users. With expanded regional availability, you...

- **Public Preview: Azure Backup for PostgreSQL flexible server and elastic cluster (v2)**[^36]
    - Azure Backup for PostgreSQL flexible server and elastic cluster (v2) preview brings enterprise-grade long-term retention to PostgreSQL. Backups are taken as physical backups from managed disk...

- **Public Preview: IPv6 Support for Application Gateway WAF**[^37]
    - Announcing the Public Preview of IPv6 support for Application Gateway WAF. Application Gateway Web Application Firewall (WAF) now supports inspection and enforcement for IPv6 traffic in Public...

- **Public Preview:  Major version upgrades (MVU) for Azure Database for PostgreSQL elastic clusters**[^38]
    - MVUs are now available for elastic clusters in Azure Database for PostgreSQL. You can upgrade an existing elastic cluster to a supported newer PostgreSQL version in place without provisioning a...

- **Public Preview: Reader Endpoint for Azure Database for MySQL**[^39]
    - We’re happy to announce the public preview of reader endpoint support to simplify connection management when using multiple replicas in Azure Database for MySQL - Flexible Server. A reader endpoint...

## リタイア

- **Retirement: Azure Key Vault Secrets Provider Extension for Azure Arc enabled Kubernetes clusters**[^40]
    - The Azure Key Vault Secrets Provider Extension for Azure Arc-enabled Kubernetes will be retired on October 9, 2027. Customers currently using the extension should plan to migrate to the Azure Key...

- **Retirement: Microsoft Dev Box will be retired on September 18, 2028**[^41]
    - Microsoft Dev Box will retire on September 18, 2028. Beginning on September 14, 2026, Microsoft Dev Box will begin the closing-down process. After retirement, Microsoft Dev Box will no longer be...

- **Retirement: Azure Deployment Environments will be retired on February 22, 2027**[^42]
    - Azure Deployment Environments will retire on February 22, 2027. Beginning on September 14, 2026, Azure Deployment Environments will begin the closing-down process. After retirement, the service will...

- **Retirement: Pod name dimension in AKS pod platform metrics**[^43]
    - Beginning September 30, 2027, support for the pod name dimension on the following Azure Monitor platform metrics is retiring, and these metrics are transitioning to aggregate pod counters: Number of...

- **Retirement: Azure App Service on Azure Stack Hub**[^44]
    - Azure App Service on Azure Stack Hub will be retired on September 30, 2029 . Starting September 30, 2026 , new installations will no longer be supported, and no new product releases, features, or...

- **Retirement: Support for Java 8, 11 and 17 will end on September 1, 2027**[^45]
    - On September 1, 2027 support for Java 8, 11 and 17 will end. Your apps that are hosted on App Service will continue to run, but security updates will no longer be available, and we’ll no longer...

- **Retirement: Always Encrypted with Intel SGX Enclaves**[^46]
    - Always Encrypted with Intel SGX enclaves in Azure SQL Database will retire on October 31, 2027 as support for SGX-enabled DC-series hardware is phased out. Customers should transition to...

## その他

- **Announcing: Migrate Azure Container Apps logging destination from Log Analytics to Azure Monitor**[^47]
    - The Log Analytics logging destination for Azure Container Apps is now a legacy logging option. Existing environments configured with the Log Analytics logging destination will continue to function...

- **Announcing: Choose Your Own Telephony (CYOT) for Microsoft Entra**[^48]
    - What and why Starting October 30, 2026, Microsoft Entra ID will make the Choose Your Own Telephony Provider experience available. This feature enables organizations to use a supported third-party...

- **Announcing: Multiparty private offers in Microsoft Marketplace expands to Hong Kong**[^49]
    - Multiparty private offers give Microsoft partners a way to procure third-party cloud and AI solutions for customers through Marketplace. Software companies can expand into new markets by working with...

- **Announcing: Table discovery in OneLake Catalog search**[^50]
    - Starting October 15, 2026, Search in Microsoft Fabric will return tables from semantic models, lakehouses, and mirrored databases as individual results. Users can search by table name or description,...

[^1]: Generally Available: Large OS Disk Encryption for Azure Confidential VM migrations, https://azure.microsoft.com/ja-jp/updates/v2/578850
[^2]: Generally Available: HTTP DDoS ruleset for Azure Front Door Premium WAF, https://azure.microsoft.com/ja-jp/updates/v2/578681
[^3]: Generally Available: Azure MCP Server 3.0, https://azure.microsoft.com/ja-jp/updates/v2/578662
[^4]: Generally Available: Marketplace private offer enhancements, https://azure.microsoft.com/ja-jp/updates/v2/576547
[^5]: Generally Available: Higher limit of Azure Blob Storage accounts per region per subscription, https://azure.microsoft.com/ja-jp/updates/v2/578358
[^6]: Generally Available: Cost management and tagging for Claude models in Microsoft Foundry, https://azure.microsoft.com/ja-jp/updates/v2/577260
[^7]: Generally Available: Azure Front Door profile and route level WAF policies, https://azure.microsoft.com/ja-jp/updates/v2/578153
[^8]: Generally Available: Network Watcher VNet flow logs filtering, https://azure.microsoft.com/ja-jp/updates/v2/577782
[^9]: Generally Available: Item Level Recovery for Azure VMs with Premium SSDv2 and Ultra Disks in Azure Backup, https://azure.microsoft.com/ja-jp/updates/v2/577963
[^10]: Generally Available: ABFS Vectored Read for Azure Data Lake Storage, https://azure.microsoft.com/ja-jp/updates/v2/577618
[^11]: Generally Available: Azure Cosmos DB Safe Key Rotation, https://azure.microsoft.com/ja-jp/updates/v2/576716
[^12]: Generally Available: Service tag match condition for Azure Front Door Premium WAF, https://azure.microsoft.com/ja-jp/updates/v2/577156
[^13]: Generally Available: Keyless TLS on Application Gateway with Azure Key Vault Managed HSM, https://azure.microsoft.com/ja-jp/updates/v2/577130
[^14]: Generally Available: Advanced platform metrics for Azure Monitor, https://azure.microsoft.com/ja-jp/updates/v2/575329
[^15]: Generally Available: Metrics usage insights for Azure Monitor workspace, https://azure.microsoft.com/ja-jp/updates/v2/577165
[^16]: Generally Available: Azure DNS enables DNS-based load balancing through Traffic Manager linked records, https://azure.microsoft.com/ja-jp/updates/v2/573917
[^17]: Generally Available: External key management for Azure Key Vault Managed HSM, https://azure.microsoft.com/ja-jp/updates/v2/574296
[^18]: Generally Available: Standard service endpoint, https://azure.microsoft.com/ja-jp/updates/v2/571025
[^19]: Generally Availabile: Automatic zone balance for Virtual Machine Scale Sets, https://azure.microsoft.com/ja-jp/updates/v2/576334
[^20]: Generally Available: Azure Cloud HSM hardware audit logging, https://azure.microsoft.com/ja-jp/updates/v2/576377
[^21]: Generally Available: Azure Site Recovery Support for Azure ARC-enabled Windows VMWare/Physical servers, https://azure.microsoft.com/ja-jp/updates/v2/576214
[^22]: Generally Available: Managed StandardV2 NAT Gateway for AKS, https://azure.microsoft.com/ja-jp/updates/v2/574430
[^23]: Generally Available: Azure Database for PostgreSQL flexible server in East US 3, https://azure.microsoft.com/ja-jp/updates/v2/573691
[^24]: Generally Available: Exceptions in WAF for Azure Application Gateway and Azure Front Door, https://azure.microsoft.com/ja-jp/updates/v2/574343
[^25]: Generally Available: Anyscale on Azure, https://azure.microsoft.com/ja-jp/updates/v2/573744
[^26]: Generally Available: Enabling the Bulk admin role for SQL Server on Linux, https://azure.microsoft.com/ja-jp/updates/v2/573443
[^27]: Generally Available: SQL Server on Azure Virtual Machines in Azure Bleu, https://azure.microsoft.com/ja-jp/updates/v2/571499
[^28]: Public Preview: Support database-level managed identity (including FIC) in Create Database Scoped Credential T-SQL, https://azure.microsoft.com/ja-jp/updates/v2/577491
[^29]: Public Preview: Cross Tenant Restore with Azure Backup, https://azure.microsoft.com/ja-jp/updates/v2/577117
[^30]: Public Preview: Disable VNet peering route, https://azure.microsoft.com/ja-jp/updates/v2/576242
[^31]: Public Preview: Azure Databricks Private network gateway, https://azure.microsoft.com/ja-jp/updates/v2/576556
[^32]: Public Preview: Azure Files cross-region data copy and synchronization with Azure Storage Mover, https://azure.microsoft.com/ja-jp/updates/v2/576542
[^33]: Public Preview: Microsoft Agent 365 integration with Azure API Management, https://azure.microsoft.com/ja-jp/updates/v2/574204
[^34]: Public Preview: AKS on bare metal now on Ubuntu, https://azure.microsoft.com/ja-jp/updates/v2/573782
[^35]: Public Preview: Azure HorizonDB expands to additional regions, https://azure.microsoft.com/ja-jp/updates/v2/572940
[^36]: Public Preview: Azure Backup for PostgreSQL flexible server and elastic cluster (v2), https://azure.microsoft.com/ja-jp/updates/v2/573425
[^37]: Public Preview: IPv6 Support for Application Gateway WAF, https://azure.microsoft.com/ja-jp/updates/v2/573861
[^38]: Public Preview:  Major version upgrades (MVU) for Azure Database for PostgreSQL elastic clusters, https://azure.microsoft.com/ja-jp/updates/v2/571504
[^39]: Public Preview: Reader Endpoint for Azure Database for MySQL, https://azure.microsoft.com/ja-jp/updates/v2/569653
[^40]: Retirement: Azure Key Vault Secrets Provider Extension for Azure Arc enabled Kubernetes clusters, https://azure.microsoft.com/ja-jp/updates/v2/570313
[^41]: Retirement: Microsoft Dev Box will be retired on September 18, 2028, https://azure.microsoft.com/ja-jp/updates/v2/567933
[^42]: Retirement: Azure Deployment Environments will be retired on February 22, 2027, https://azure.microsoft.com/ja-jp/updates/v2/567934
[^43]: Retirement: Pod name dimension in AKS pod platform metrics, https://azure.microsoft.com/ja-jp/updates/v2/570232
[^44]: Retirement: Azure App Service on Azure Stack Hub, https://azure.microsoft.com/ja-jp/updates/v2/568178
[^45]: Retirement: Support for Java 8, 11 and 17 will end on September 1, 2027, https://azure.microsoft.com/ja-jp/updates/v2/568585
[^46]: Retirement: Always Encrypted with Intel SGX Enclaves, https://azure.microsoft.com/ja-jp/updates/v2/569236
[^47]: Announcing: Migrate Azure Container Apps logging destination from Log Analytics to Azure Monitor, https://azure.microsoft.com/ja-jp/updates/v2/577689
[^48]: Announcing: Choose Your Own Telephony (CYOT) for Microsoft Entra, https://azure.microsoft.com/ja-jp/updates/v2/577273
[^49]: Announcing: Multiparty private offers in Microsoft Marketplace expands to Hong Kong, https://azure.microsoft.com/ja-jp/updates/v2/571831
[^50]: Announcing: Table discovery in OneLake Catalog search, https://azure.microsoft.com/ja-jp/updates/v2/573875
