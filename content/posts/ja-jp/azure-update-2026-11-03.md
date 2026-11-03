Title: Azure Update (2026/10/06 - 2026/11/02)
Date: 2026-11-03
Slug: azure-update-2026-11-03
Lang: ja-jp
Category: notebook
Tags: ai-machine-learning, analytics, api-management, app-service, application-gateway, azure, azure-arc, azure-backup, azure-blob-storage, azure-container-apps, azure-cosmos-db, azure-data-lake-storage, azure-database-for-postgresql, azure-databricks, azure-deployment-environments, azure-dns, azure-files, azure-fluid-relay, azure-front-door, azure-kubernetes-service-aks, azure-migrate, azure-monitor, azure-nat-gateway, azure-private-link, azure-site-recovery, azure-sql-database, azure-stack-hub, azure-storage-actions, azure-updates, compute, containers, databases, developer-tools, devops, hybrid-multicloud, identity, integration, internet-of-things, key-vault, management-and-governance, microsoft-azure-portal, microsoft-dev-box, microsoft-entra-id-formerly-azure-ad, microsoft-foundry, migration, mobile, network-watcher, networking, sdks, security, service-bus, storage, traffic-manager, virtual-desktop-infrastructure, virtual-network, web, web-application-firewall
Summary: 2026年10月6日〜11月2日の Azure Update まとめ。GA 31件、パブリックプレビュー 7件、リタイア 9件、その他 3件の計50件。

2026年10月6日〜11月2日の Azure Update のまとめです。

| 分類 | 件数 |
| --- | --- |
| GA (一般提供) | 31 |
| パブリックプレビュー | 7 |
| リタイア | 9 |
| その他 | 3 |
| **合計** | **50** |

## GA (一般提供)

- **Generally Available: Change from virtual network integration to a private endpoint capable network configuration in Azure Database for PostgreSQL flexible server**[^1]
    - You now have greater flexibility in network design for Azure Database for PostgreSQL Flexible Server workloads. Now you can change existing VNet-integrated servers from delegated-subnet networking to...

- **Generally Available: Azure Storage Actions adds automatic task updates, execution controls, and case-sensitive matching**[^2]
    - Azure Storage Actions is introducing three enhancements to simplify task management and give you more control over automated data operations across Azure Blob and Data Lake Storage: Automatic...

- **Generally Available: Restart databases in Azure SQL DB via the Azure portal**[^3]
    - You can now restart or fail over databases directly from the Azure portal, including single databases, Hyperscale databases, and databases in elastic pools, without writing scripts against the Rest...

- **Generally Available: Geo-Replication on partitioned namespaces for Azure Service Bus Premium**[^4]
    - Geo-Replication on partitioned namespaces for Azure Service Bus Premium is now generally available. You can now combine the throughput benefits of partitioning with the reliability of replicating...

- **Generally Available: Azure Site Recovery for Azure Local**[^5]
    - Azure Site Recovery support for Azure Local is now generally available, making enterprise-grade disaster recovery simpler, accessible, easier to setup and secure than ever before. Customers can...

- **Generally Available: Large OS Disk Encryption for Azure Confidential VM migrations**[^6]
    - Large OS Disk Encryption (LOSDE) is now generally available for Azure Confidential VM migration scenarios. Organizations can move larger, production-scale workloads into confidential computing with...

- **Generally Available: HTTP DDoS ruleset for Azure Front Door Premium WAF**[^7]
    - Announcing the general availability of the HTTP DDoS ruleset for Azure Web Application Firewall (WAF) on Azure Front Door Premium. HTTP-layer DDoS attacks remain a leading cause of application...

- **Generally Available: Azure MCP Server 3.0**[^8]
    - Azure MCP Server 3.0 is now generally available, expanding how AI agents and developer tools interact with Azure through the open Model Context Protocol (MCP). This release introduces new and...

- **Generally Available: Marketplace private offer enhancements**[^9]
    - Private offers through Microsoft Marketplace help you optimize your spending power with pricing and terms aligned to your organization’s needs, including flexible billing, custom contract lengths,...

- **Generally Available: Higher limit of Azure Blob Storage accounts per region per subscription**[^10]
    - Higher Azure Storage account resource quotas are now generally available, supporting up to 1,000 storage accounts with standard endpoints per region, per subscription, up from the default of 250....

- **Generally Available: Cost management and tagging for Claude models in Microsoft Foundry**[^11]
    - Microsoft Foundry now brings Claude models into Azure Cost Management alongside the rest of your Foundry spend, generally available. Until now, Claude charges appeared under SaaS rather than under...

- **Generally Available: Azure Front Door profile and route level WAF policies**[^12]
    - Announcing the general availability of profile and route level policies for Azure Web Application Firewall (WAF) on Azure Front Door Premium. WAF policies are no longer limited to individual domains:...

- **Generally Available: Network Watcher VNet flow logs filtering**[^13]
    - Azure Network Watcher VNet flow logs filtering is now generally available, enabling you to control which network traffic flows are logged based on specific criteria such as IP addresses, ports,...

- **Generally Available: Item Level Recovery for Azure VMs with Premium SSDv2 and Ultra Disks in Azure Backup**[^14]
    - Azure Backup now supports Item-Level Recovery (ILR) for Azure virtual machines using Premium SSD v2 and Ultra disks with both 512 byte and 4KB logical sector sizes. You can now recover individual...

- **Generally Available: ABFS Vectored Read for Azure Data Lake Storage**[^15]
    - ABFS Vectored Read helps compatible analytics engines reduce request overhead for selective reads in Azure Data Lake Storage. By combining nearby file ranges into fewer storage requests and executing...

- **Generally Available: Azure Cosmos DB Safe Key Rotation**[^16]
    - Safe Key Rotation for Azure Cosmos DB is now generally available. You can view timestamp metadata showing when each account key was last used, helping you identify active keys before rotating or...

- **Generally Available: Service tag match condition for Azure Front Door Premium WAF**[^17]
    - Announcing the general availability of the service tag match condition for Azure Web Application Firewall (WAF) custom rules on Azure Front Door Premium. Service tags represent groups of IP address...

- **Generally Available: Keyless TLS on Application Gateway with Azure Key Vault Managed HSM**[^18]
    - Azure Application Gateway now supports keyless TLS termination using certificates whose private keys stay in Azure Key Vault Managed HSM. Each TLS handshake signature is performed inside the HSM, and...

- **Generally Available: Advanced platform metrics for Azure Monitor**[^19]
    - Advanced platform metrics for Azure Monitor are now generally available. Advanced platform metrics provide finer-grained signals that help customers more quickly and accurately identify changes and...

- **Generally Available: Metrics usage insights for Azure Monitor workspace**[^20]
    - Metrics usage insights is now generally available, giving you greater visibility into what’s driving metrics usage across your Azure Monitor workspace. Monitor workspace utilization, identify unused...

- **Generally Available: Azure DNS enables DNS-based load balancing through Traffic Manager linked records**[^21]
    - Azure DNS now provides DNS based load balancing by seamless integration with Azure Traffic Manager. Customers can directly associate an Azure DNS record set with a Traffic Manager profile,...

- **Generally Available: External key management for Azure Key Vault Managed HSM**[^22]
    - External key management for Azure Key Vault Managed HSM is now generally available in all Azure public regions. For organizations with regulatory or sovereignty requirements to retain physical...

- **Generally Available: Standard service endpoint**[^23]
    - Standard service endpoint, a new capability in the Azure Private Link family, provides a scalable and secure approach for connecting Azure IaaS workloads to Azure PaaS services. Standard service...

- **Generally Availabile: Automatic zone balance for Virtual Machine Scale Sets**[^24]
    - Automatic zone balance for Virtual Machine Scale Sets is now generally available. This feature continuously monitors scale sets deployed across availability zones and automatically redistributes VM...

- **Generally Available: Azure Cloud HSM hardware audit logging**[^25]
    - Hardware Audit Logging for Azure Cloud HSM provides hardware-generated audit records for supported HSM management operations, helping organizations strengthen security monitoring, compliance...

- **Generally Available: Azure Site Recovery Support for Azure ARC-enabled Windows VMWare/Physical servers**[^26]
    - Azure Site Recovery (ASR) now supports disaster recovery for Azure ARC-enabled Windows VMWare virtual machines and on-premise physical servers. Customers can protect ARC-managed machines with ASR...

- **Generally Available: Managed StandardV2 NAT Gateway for AKS**[^27]
    - AKS will now provision and manage a StandardV2 NAT Gateway for clusters using an AKS-managed virtual network. StandardV2 is now the default managed NAT Gateway SKU for new clusters in supported...

- **Generally Available: Azure Database for PostgreSQL flexible server in East US 3**[^28]
    - Now you can deploy Azure Database for PostgreSQL flexible server in the East US 3 Azure region. Learn more .

- **Generally Available: Exceptions in WAF for Azure Application Gateway and Azure Front Door**[^29]
    - Announcing the general availability of exceptions for Web Application Firewall on Azure Application Gateway and Azure Front Door. Azure Web Application Firewall (WAF) helps protect your web...

- **Generally Available: Anyscale on Azure**[^30]
    - Anyscale on Azure is now Generally Available. Anyscale on Azure is a managed platform for running distributed Python workloads on Ray. It deploys directly onto your Azure Kubernetes Service (AKS)...

- **Generally Available: Enabling the Bulk admin role for SQL Server on Linux**[^31]
    - Starting with SQL Server 2025 CU9 and SQL Server 2022 CU27, SQL Server on Linux supports the bulkadmin fixed server role and the ADMINISTER BULK OPERATIONS permission for performing bulk data import...

## パブリックプレビュー

- **Public Preview: On-prem NAS share discovery and assessment are now available using Azure Migrate**[^32]
    - Azure Migrate now supports discovery and assessment for network-attached storage, allowing customers and partners to plan migrations of Dell PowerScale (OneFS) and NetApp ONTAP storage to Azure. The...

- **Public Preview: Support database-level managed identity (including FIC) in Create Database Scoped Credential T-SQL**[^33]
    - With database-level managed identity in Azure SQL Database, you can use a user-assigned managed identity for each database to query files in Azure Blob Storage and Azure Data Lake Storage Gen2...

- **Public Preview: Cross Tenant Restore with Azure Backup**[^34]
    - Cross-Tenant Restore (CTR) helps organizations establish an independent recovery path by enabling Azure VM backups to be restored into a separate Azure tenant. It strengthens cyber resilience while...

- **Public Preview: Disable VNet peering route**[^35]
    - Announcing the public preview of disable VNet peering route, a route-table capability that gives you more control over traffic between peered virtual networks. DPR suppresses system-generated peering...

- **Public Preview: Azure Databricks Private network gateway**[^36]
    - Private network gateway for Azure Databricks is now in Public Preview, enabling serverless compute to connect to resources in your virtual network (VNet) and transitively connected networks through a...

- **Public Preview: Azure Files cross-region data copy and synchronization with Azure Storage Mover**[^37]
    - Azure Files customers can now copy and synchronize file share data across storage accounts, Azure regions, and subscriptions within the same tenant using Azure Storage Mover. Schedule incremental...

- **Public Preview: Microsoft Agent 365 integration with Azure API Management**[^38]
    - The integration between Microsoft Agent 365 and Azure API Management is now available in public preview, helping organizations connect centralized governance with runtime enforcement for MCP servers...

## リタイア

- **Retirement: OT security in Microsoft Defender for IoT**[^39]
    - This is the formal notice that Microsoft plans to deprecate the operational technology (OT) security component of Microsoft Defender for IoT. The service will be fully deprecated in October 2029,...

- **Retirement: Azure Fluid Relay**[^40]
    - On February 2, 2027, we will retire Azure Fluid Relay. After this date, Azure Fluid Relay will reach end of availability, and workloads that continue to depend on the service may experience...

- **Retirement: Azure Key Vault Secrets Provider Extension for Azure Arc enabled Kubernetes clusters**[^41]
    - The Azure Key Vault Secrets Provider Extension for Azure Arc-enabled Kubernetes will be retired on October 9, 2027. Customers currently using the extension should plan to migrate to the Azure Key...

- **Retirement: Microsoft Dev Box will be retired on September 18, 2028**[^42]
    - Microsoft Dev Box will retire on September 18, 2028. Beginning on September 14, 2026, Microsoft Dev Box will begin the closing-down process. After retirement, Microsoft Dev Box will no longer be...

- **Retirement: Azure Deployment Environments will be retired on February 22, 2027**[^43]
    - Azure Deployment Environments will retire on February 22, 2027. Beginning on September 14, 2026, Azure Deployment Environments will begin the closing-down process. After retirement, the service will...

- **Retirement: Pod name dimension in AKS pod platform metrics**[^44]
    - Beginning September 30, 2027, support for the pod name dimension on the following Azure Monitor platform metrics is retiring, and these metrics are transitioning to aggregate pod counters: Number of...

- **Retirement: Azure App Service on Azure Stack Hub**[^45]
    - Azure App Service on Azure Stack Hub will be retired on September 30, 2029 . Starting September 30, 2026 , new installations will no longer be supported, and no new product releases, features, or...

- **Retirement: Support for Java 8, 11 and 17 will end on September 1, 2027**[^46]
    - On September 1, 2027 support for Java 8, 11 and 17 will end. Your apps that are hosted on App Service will continue to run, but security updates will no longer be available, and we’ll no longer...

- **Retirement: Always Encrypted with Intel SGX Enclaves**[^47]
    - Always Encrypted with Intel SGX enclaves in Azure SQL Database will retire on October 31, 2027 as support for SGX-enabled DC-series hardware is phased out. Customers should transition to...

## その他

- **Announcing: Migrate Azure Container Apps logging destination from Log Analytics to Azure Monitor**[^48]
    - The Log Analytics logging destination for Azure Container Apps is now a legacy logging option. Existing environments configured with the Log Analytics logging destination will continue to function...

- **Announcing: Choose Your Own Telephony (CYOT) for Microsoft Entra**[^49]
    - What and why Starting October 30, 2026, Microsoft Entra ID will make the Choose Your Own Telephony Provider experience available. This feature enables organizations to use a supported third-party...

- **Announcing: Multiparty private offers in Microsoft Marketplace expands to Hong Kong**[^50]
    - Multiparty private offers give Microsoft partners a way to procure third-party cloud and AI solutions for customers through Marketplace. Software companies can expand into new markets by working with...

[^1]: Generally Available: Change from virtual network integration to a private endpoint capable network configuration in Azure Database for PostgreSQL flexible server, https://azure.microsoft.com/ja-jp/updates/v2/574541
[^2]: Generally Available: Azure Storage Actions adds automatic task updates, execution controls, and case-sensitive matching, https://azure.microsoft.com/ja-jp/updates/v2/578628
[^3]: Generally Available: Restart databases in Azure SQL DB via the Azure portal, https://azure.microsoft.com/ja-jp/updates/v2/577992
[^4]: Generally Available: Geo-Replication on partitioned namespaces for Azure Service Bus Premium, https://azure.microsoft.com/ja-jp/updates/v2/579021
[^5]: Generally Available: Azure Site Recovery for Azure Local, https://azure.microsoft.com/ja-jp/updates/v2/579111
[^6]: Generally Available: Large OS Disk Encryption for Azure Confidential VM migrations, https://azure.microsoft.com/ja-jp/updates/v2/578850
[^7]: Generally Available: HTTP DDoS ruleset for Azure Front Door Premium WAF, https://azure.microsoft.com/ja-jp/updates/v2/578681
[^8]: Generally Available: Azure MCP Server 3.0, https://azure.microsoft.com/ja-jp/updates/v2/578662
[^9]: Generally Available: Marketplace private offer enhancements, https://azure.microsoft.com/ja-jp/updates/v2/576547
[^10]: Generally Available: Higher limit of Azure Blob Storage accounts per region per subscription, https://azure.microsoft.com/ja-jp/updates/v2/578358
[^11]: Generally Available: Cost management and tagging for Claude models in Microsoft Foundry, https://azure.microsoft.com/ja-jp/updates/v2/577260
[^12]: Generally Available: Azure Front Door profile and route level WAF policies, https://azure.microsoft.com/ja-jp/updates/v2/578153
[^13]: Generally Available: Network Watcher VNet flow logs filtering, https://azure.microsoft.com/ja-jp/updates/v2/577782
[^14]: Generally Available: Item Level Recovery for Azure VMs with Premium SSDv2 and Ultra Disks in Azure Backup, https://azure.microsoft.com/ja-jp/updates/v2/577963
[^15]: Generally Available: ABFS Vectored Read for Azure Data Lake Storage, https://azure.microsoft.com/ja-jp/updates/v2/577618
[^16]: Generally Available: Azure Cosmos DB Safe Key Rotation, https://azure.microsoft.com/ja-jp/updates/v2/576716
[^17]: Generally Available: Service tag match condition for Azure Front Door Premium WAF, https://azure.microsoft.com/ja-jp/updates/v2/577156
[^18]: Generally Available: Keyless TLS on Application Gateway with Azure Key Vault Managed HSM, https://azure.microsoft.com/ja-jp/updates/v2/577130
[^19]: Generally Available: Advanced platform metrics for Azure Monitor, https://azure.microsoft.com/ja-jp/updates/v2/575329
[^20]: Generally Available: Metrics usage insights for Azure Monitor workspace, https://azure.microsoft.com/ja-jp/updates/v2/577165
[^21]: Generally Available: Azure DNS enables DNS-based load balancing through Traffic Manager linked records, https://azure.microsoft.com/ja-jp/updates/v2/573917
[^22]: Generally Available: External key management for Azure Key Vault Managed HSM, https://azure.microsoft.com/ja-jp/updates/v2/574296
[^23]: Generally Available: Standard service endpoint, https://azure.microsoft.com/ja-jp/updates/v2/571025
[^24]: Generally Availabile: Automatic zone balance for Virtual Machine Scale Sets, https://azure.microsoft.com/ja-jp/updates/v2/576334
[^25]: Generally Available: Azure Cloud HSM hardware audit logging, https://azure.microsoft.com/ja-jp/updates/v2/576377
[^26]: Generally Available: Azure Site Recovery Support for Azure ARC-enabled Windows VMWare/Physical servers, https://azure.microsoft.com/ja-jp/updates/v2/576214
[^27]: Generally Available: Managed StandardV2 NAT Gateway for AKS, https://azure.microsoft.com/ja-jp/updates/v2/574430
[^28]: Generally Available: Azure Database for PostgreSQL flexible server in East US 3, https://azure.microsoft.com/ja-jp/updates/v2/573691
[^29]: Generally Available: Exceptions in WAF for Azure Application Gateway and Azure Front Door, https://azure.microsoft.com/ja-jp/updates/v2/574343
[^30]: Generally Available: Anyscale on Azure, https://azure.microsoft.com/ja-jp/updates/v2/573744
[^31]: Generally Available: Enabling the Bulk admin role for SQL Server on Linux, https://azure.microsoft.com/ja-jp/updates/v2/573443
[^32]: Public Preview: On-prem NAS share discovery and assessment are now available using Azure Migrate, https://azure.microsoft.com/ja-jp/updates/v2/577975
[^33]: Public Preview: Support database-level managed identity (including FIC) in Create Database Scoped Credential T-SQL, https://azure.microsoft.com/ja-jp/updates/v2/577491
[^34]: Public Preview: Cross Tenant Restore with Azure Backup, https://azure.microsoft.com/ja-jp/updates/v2/577117
[^35]: Public Preview: Disable VNet peering route, https://azure.microsoft.com/ja-jp/updates/v2/576242
[^36]: Public Preview: Azure Databricks Private network gateway, https://azure.microsoft.com/ja-jp/updates/v2/576556
[^37]: Public Preview: Azure Files cross-region data copy and synchronization with Azure Storage Mover, https://azure.microsoft.com/ja-jp/updates/v2/576542
[^38]: Public Preview: Microsoft Agent 365 integration with Azure API Management, https://azure.microsoft.com/ja-jp/updates/v2/574204
[^39]: Retirement: OT security in Microsoft Defender for IoT, https://azure.microsoft.com/ja-jp/updates/v2/576255
[^40]: Retirement: Azure Fluid Relay, https://azure.microsoft.com/ja-jp/updates/v2/570498
[^41]: Retirement: Azure Key Vault Secrets Provider Extension for Azure Arc enabled Kubernetes clusters, https://azure.microsoft.com/ja-jp/updates/v2/570313
[^42]: Retirement: Microsoft Dev Box will be retired on September 18, 2028, https://azure.microsoft.com/ja-jp/updates/v2/567933
[^43]: Retirement: Azure Deployment Environments will be retired on February 22, 2027, https://azure.microsoft.com/ja-jp/updates/v2/567934
[^44]: Retirement: Pod name dimension in AKS pod platform metrics, https://azure.microsoft.com/ja-jp/updates/v2/570232
[^45]: Retirement: Azure App Service on Azure Stack Hub, https://azure.microsoft.com/ja-jp/updates/v2/568178
[^46]: Retirement: Support for Java 8, 11 and 17 will end on September 1, 2027, https://azure.microsoft.com/ja-jp/updates/v2/568585
[^47]: Retirement: Always Encrypted with Intel SGX Enclaves, https://azure.microsoft.com/ja-jp/updates/v2/569236
[^48]: Announcing: Migrate Azure Container Apps logging destination from Log Analytics to Azure Monitor, https://azure.microsoft.com/ja-jp/updates/v2/577689
[^49]: Announcing: Choose Your Own Telephony (CYOT) for Microsoft Entra, https://azure.microsoft.com/ja-jp/updates/v2/577273
[^50]: Announcing: Multiparty private offers in Microsoft Marketplace expands to Hong Kong, https://azure.microsoft.com/ja-jp/updates/v2/571831
