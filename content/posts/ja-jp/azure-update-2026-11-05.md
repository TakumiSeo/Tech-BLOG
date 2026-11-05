Title: Azure Update (2026/10/08 - 2026/11/04)
Date: 2026-11-05
Slug: azure-update-2026-11-05
Lang: ja-jp
Category: notebook
Tags: ai-machine-learning, analytics, application-gateway, application-insights, azure, azure-arc, azure-backup, azure-blob-storage, azure-container-apps, azure-cosmos-db, azure-data-lake-storage, azure-database-for-postgresql, azure-databricks, azure-disk-storage, azure-dns, azure-files, azure-firewall, azure-fluid-relay, azure-front-door, azure-kubernetes-service-aks, azure-migrate, azure-monitor, azure-nat-gateway, azure-private-link, azure-route-server, azure-site-recovery, azure-sql-database, azure-sql-managed-instance, azure-storage-actions, azure-storage-discovery, azure-updates, compute, containers, databases, developer-tools, devops, hybrid-multicloud, identity, integration, internet-of-things, key-vault, management-and-governance, microsoft-azure-portal, microsoft-entra-id-formerly-azure-ad, microsoft-foundry, migration, network-watcher, networking, sdks, security, service-bus, storage, storage-accounts, traffic-manager, virtual-machines, virtual-network, web, web-application-firewall
Summary: 2026年10月8日〜11月4日の Azure Update まとめ。GA 30件、パブリックプレビュー 13件、リタイア 4件、その他 3件の計50件。

2026年10月8日〜11月4日の Azure Update のまとめです。

| 分類 | 件数 |
| --- | --- |
| GA (一般提供) | 30 |
| パブリックプレビュー | 13 |
| リタイア | 4 |
| その他 | 3 |
| **合計** | **50** |

## GA (一般提供)

- **Generally Available: Azure Database for PostgreSQL stable REST API version 2026-10-01**[^1]
    - The Azure Database for PostgreSQL Flexible Server REST API version 2026-10-01 is now generally available. This stable API release introduces expanded capabilities for maintenance management,...

- **Generally Available: Enhanced Azure Site Recovery support for VMSS Flex**[^2]
    - Azure Site Recovery now offers an enhanced disaster recovery experience for virtual machines in Virtual Machine Scale Sets with flexible orchestration. The update improves target configuration and...

- **Generally Available: Change from virtual network integration to a private endpoint capable network configuration in Azure Database for PostgreSQL flexible server**[^3]
    - You now have greater flexibility in network design for Azure Database for PostgreSQL Flexible Server workloads. Now you can change existing VNet-integrated servers from delegated-subnet networking to...

- **Generally Available: Azure Storage Actions adds automatic task updates, execution controls, and case-sensitive matching**[^4]
    - Azure Storage Actions is introducing three enhancements to simplify task management and give you more control over automated data operations across Azure Blob and Data Lake Storage: Automatic...

- **Generally Available: Restart databases in Azure SQL DB via the Azure portal**[^5]
    - You can now restart or fail over databases directly from the Azure portal, including single databases, Hyperscale databases, and databases in elastic pools, without writing scripts against the Rest...

- **Generally Available: Geo-Replication on partitioned namespaces for Azure Service Bus Premium**[^6]
    - Geo-Replication on partitioned namespaces for Azure Service Bus Premium is now generally available. You can now combine the throughput benefits of partitioning with the reliability of replicating...

- **Generally Available: Azure Site Recovery for Azure Local**[^7]
    - Azure Site Recovery support for Azure Local is now generally available, making enterprise-grade disaster recovery simpler, accessible, easier to setup and secure than ever before. Customers can...

- **Generally Available: Large OS Disk Encryption for Azure Confidential VM migrations**[^8]
    - Large OS Disk Encryption (LOSDE) is now generally available for Azure Confidential VM migration scenarios. Organizations can move larger, production-scale workloads into confidential computing with...

- **Generally Available: HTTP DDoS ruleset for Azure Front Door Premium WAF**[^9]
    - Announcing the general availability of the HTTP DDoS ruleset for Azure Web Application Firewall (WAF) on Azure Front Door Premium. HTTP-layer DDoS attacks remain a leading cause of application...

- **Generally Available: Azure MCP Server 3.0**[^10]
    - Azure MCP Server 3.0 is now generally available, expanding how AI agents and developer tools interact with Azure through the open Model Context Protocol (MCP). This release introduces new and...

- **Generally Available: Marketplace private offer enhancements**[^11]
    - Private offers through Microsoft Marketplace help you optimize your spending power with pricing and terms aligned to your organization’s needs, including flexible billing, custom contract lengths,...

- **Generally Available: Higher limit of Azure Blob Storage accounts per region per subscription**[^12]
    - Higher Azure Storage account resource quotas are now generally available, supporting up to 1,000 storage accounts with standard endpoints per region, per subscription, up from the default of 250....

- **Generally Available: Cost management and tagging for Claude models in Microsoft Foundry**[^13]
    - Microsoft Foundry now brings Claude models into Azure Cost Management alongside the rest of your Foundry spend, generally available. Until now, Claude charges appeared under SaaS rather than under...

- **Generally Available: Azure Front Door profile and route level WAF policies**[^14]
    - Announcing the general availability of profile and route level policies for Azure Web Application Firewall (WAF) on Azure Front Door Premium. WAF policies are no longer limited to individual domains:...

- **Generally Available: Network Watcher VNet flow logs filtering**[^15]
    - Azure Network Watcher VNet flow logs filtering is now generally available, enabling you to control which network traffic flows are logged based on specific criteria such as IP addresses, ports,...

- **Generally Available: Item Level Recovery for Azure VMs with Premium SSDv2 and Ultra Disks in Azure Backup**[^16]
    - Azure Backup now supports Item-Level Recovery (ILR) for Azure virtual machines using Premium SSD v2 and Ultra disks with both 512 byte and 4KB logical sector sizes. You can now recover individual...

- **Generally Available: ABFS Vectored Read for Azure Data Lake Storage**[^17]
    - ABFS Vectored Read helps compatible analytics engines reduce request overhead for selective reads in Azure Data Lake Storage. By combining nearby file ranges into fewer storage requests and executing...

- **Generally Available: Azure Cosmos DB Safe Key Rotation**[^18]
    - Safe Key Rotation for Azure Cosmos DB is now generally available. You can view timestamp metadata showing when each account key was last used, helping you identify active keys before rotating or...

- **Generally Available: Service tag match condition for Azure Front Door Premium WAF**[^19]
    - Announcing the general availability of the service tag match condition for Azure Web Application Firewall (WAF) custom rules on Azure Front Door Premium. Service tags represent groups of IP address...

- **Generally Available: Keyless TLS on Application Gateway with Azure Key Vault Managed HSM**[^20]
    - Azure Application Gateway now supports keyless TLS termination using certificates whose private keys stay in Azure Key Vault Managed HSM. Each TLS handshake signature is performed inside the HSM, and...

- **Generally Available: Advanced platform metrics for Azure Monitor**[^21]
    - Advanced platform metrics for Azure Monitor are now generally available. Advanced platform metrics provide finer-grained signals that help customers more quickly and accurately identify changes and...

- **Generally Available: Metrics usage insights for Azure Monitor workspace**[^22]
    - Metrics usage insights is now generally available, giving you greater visibility into what’s driving metrics usage across your Azure Monitor workspace. Monitor workspace utilization, identify unused...

- **Generally Available: Azure DNS enables DNS-based load balancing through Traffic Manager linked records**[^23]
    - Azure DNS now provides DNS based load balancing by seamless integration with Azure Traffic Manager. Customers can directly associate an Azure DNS record set with a Traffic Manager profile,...

- **Generally Available: External key management for Azure Key Vault Managed HSM**[^24]
    - External key management for Azure Key Vault Managed HSM is now generally available in all Azure public regions. For organizations with regulatory or sovereignty requirements to retain physical...

- **Generally Available: Standard service endpoint**[^25]
    - Standard service endpoint, a new capability in the Azure Private Link family, provides a scalable and secure approach for connecting Azure IaaS workloads to Azure PaaS services. Standard service...

- **Generally Availabile: Automatic zone balance for Virtual Machine Scale Sets**[^26]
    - Automatic zone balance for Virtual Machine Scale Sets is now generally available. This feature continuously monitors scale sets deployed across availability zones and automatically redistributes VM...

- **Generally Available: Azure Cloud HSM hardware audit logging**[^27]
    - Hardware Audit Logging for Azure Cloud HSM provides hardware-generated audit records for supported HSM management operations, helping organizations strengthen security monitoring, compliance...

- **Generally Available: Azure Site Recovery Support for Azure ARC-enabled Windows VMWare/Physical servers**[^28]
    - Azure Site Recovery (ASR) now supports disaster recovery for Azure ARC-enabled Windows VMWare virtual machines and on-premise physical servers. Customers can protect ARC-managed machines with ASR...

- **Generally Available: Managed StandardV2 NAT Gateway for AKS**[^29]
    - AKS will now provision and manage a StandardV2 NAT Gateway for clusters using an AKS-managed virtual network. StandardV2 is now the default managed NAT Gateway SKU for new clusters in supported...

- **Generally Available: Azure Database for PostgreSQL flexible server in East US 3**[^30]
    - Now you can deploy Azure Database for PostgreSQL flexible server in the East US 3 Azure region. Learn more .

## パブリックプレビュー

- **Public Preview: Azure Firewall IPv6 now supports application rules**[^31]
    - Azure Firewall now supports application rules in IPv6 Public Preview, enabling layer 7 filtering for IPv6 HTTP and HTTPS traffic. The enhancement extends application-level controls to IPv6 and...

- **Public Preview: Multi-disk crash-consistent VM restore points for Premium SSD v2 and Ultra Disks on VMs with SCSI disk controller**[^32]
    - Multi-disk crash-consistent restore points for Azure virtual machines with Premium SSD v2 and Ultra data disks are now available in public preview on VMs with SCSI disk controllers. You can use this...

- **Public Preview: JWT validation for Application Gateway for Containers**[^33]
    - Application Gateway for Containers now supports centralized JSON Web Token validation through the AuthPolicy custom resource. Teams can validate a token signature, issuer, lifetime, and configured...

- **Public Preview: MCP gateway for Application Gateway for Containers**[^34]
    - Application Gateway for Containers now supports Model Context Protocol routing through the new MCPRoute custom resource. Platform teams can publish MCP servers behind a stable hostname and path while...

- **Public Preview: Private ingress for Application Gateway for Containers**[^35]
    - Application Gateway for Containers now supports private frontends that are reachable only through approved Azure Private Link private endpoints. This enables organizations to keep internal...

- **Public Preview: Advanced capacity insights are now available in Azure Storage Discovery**[^36]
    - Advanced capacity insights are now available for preview in Azure Storage Discovery. Storage Discovery now provides greater visibility into storage usage through insights such as access patterns,...

- **Public Preview: Extend immutability for PITR backups for Azure SQL Database and Azure SQL Managed Instance**[^37]
    - With this enhancement, you have the ability to lock your retention to the configured PITR retention, beyond the default 7 days of immutable backups that are already available. This is especially...

- **Public Preview: On-prem NAS share discovery and assessment are now available using Azure Migrate**[^38]
    - Azure Migrate now supports discovery and assessment for network-attached storage, allowing customers and partners to plan migrations of Dell PowerScale (OneFS) and NetApp ONTAP storage to Azure. The...

- **Public Preview: Support database-level managed identity (including FIC) in Create Database Scoped Credential T-SQL**[^39]
    - With database-level managed identity in Azure SQL Database, you can use a user-assigned managed identity for each database to query files in Azure Blob Storage and Azure Data Lake Storage Gen2...

- **Public Preview: Cross Tenant Restore with Azure Backup**[^40]
    - Cross-Tenant Restore (CTR) helps organizations establish an independent recovery path by enabling Azure VM backups to be restored into a separate Azure tenant. It strengthens cyber resilience while...

- **Public Preview: Disable VNet peering route**[^41]
    - Announcing the public preview of disable VNet peering route, a route-table capability that gives you more control over traffic between peered virtual networks. DPR suppresses system-generated peering...

- **Public Preview: Azure Databricks Private network gateway**[^42]
    - Private network gateway for Azure Databricks is now in Public Preview, enabling serverless compute to connect to resources in your virtual network (VNet) and transitively connected networks through a...

- **Public Preview: Azure Files cross-region data copy and synchronization with Azure Storage Mover**[^43]
    - Azure Files customers can now copy and synchronize file share data across storage accounts, Azure regions, and subscriptions within the same tenant using Azure Storage Mover. Schedule incremental...

## リタイア

- **Retirement: Transition to Entra ID (formerly known as Azure AD) to query data from Azure Monitor application insights by March 31, 2027**[^44]
    - *Note: We have extended the retirement date to March 31, 2027. On March 31, 2027 API keys used query application insights will be retired. You'll need to transition to Microsoft Entra ID (formerly...

- **Retirement: OT security in Microsoft Defender for IoT**[^45]
    - This is the formal notice that Microsoft plans to deprecate the operational technology (OT) security component of Microsoft Defender for IoT. The service will be fully deprecated in October 2029,...

- **Retirement: Azure Fluid Relay**[^46]
    - On February 2, 2027, we will retire Azure Fluid Relay. After this date, Azure Fluid Relay will reach end of availability, and workloads that continue to depend on the service may experience...

- **Retirement: Azure Key Vault Secrets Provider Extension for Azure Arc enabled Kubernetes clusters**[^47]
    - The Azure Key Vault Secrets Provider Extension for Azure Arc-enabled Kubernetes will be retired on October 9, 2027. Customers currently using the extension should plan to migrate to the Azure Key...

## その他

- **Generally Available: Route maps for Azure Route Server**[^48]
    - Route maps for Azure Route Server are now generally available in the Azure public cloud. Route maps provide fine-grained control over inbound and outbound routing across hybrid connections. Customers...

- **Announcing: Migrate Azure Container Apps logging destination from Log Analytics to Azure Monitor**[^49]
    - The Log Analytics logging destination for Azure Container Apps is now a legacy logging option. Existing environments configured with the Log Analytics logging destination will continue to function...

- **Announcing: Choose Your Own Telephony (CYOT) for Microsoft Entra**[^50]
    - What and why Starting October 30, 2026, Microsoft Entra ID will make the Choose Your Own Telephony Provider experience available. This feature enables organizations to use a supported third-party...

[^1]: Generally Available: Azure Database for PostgreSQL stable REST API version 2026-10-01, https://azure.microsoft.com/ja-jp/updates/v2/579300
[^2]: Generally Available: Enhanced Azure Site Recovery support for VMSS Flex, https://azure.microsoft.com/ja-jp/updates/v2/578926
[^3]: Generally Available: Change from virtual network integration to a private endpoint capable network configuration in Azure Database for PostgreSQL flexible server, https://azure.microsoft.com/ja-jp/updates/v2/574541
[^4]: Generally Available: Azure Storage Actions adds automatic task updates, execution controls, and case-sensitive matching, https://azure.microsoft.com/ja-jp/updates/v2/578628
[^5]: Generally Available: Restart databases in Azure SQL DB via the Azure portal, https://azure.microsoft.com/ja-jp/updates/v2/577992
[^6]: Generally Available: Geo-Replication on partitioned namespaces for Azure Service Bus Premium, https://azure.microsoft.com/ja-jp/updates/v2/579021
[^7]: Generally Available: Azure Site Recovery for Azure Local, https://azure.microsoft.com/ja-jp/updates/v2/579111
[^8]: Generally Available: Large OS Disk Encryption for Azure Confidential VM migrations, https://azure.microsoft.com/ja-jp/updates/v2/578850
[^9]: Generally Available: HTTP DDoS ruleset for Azure Front Door Premium WAF, https://azure.microsoft.com/ja-jp/updates/v2/578681
[^10]: Generally Available: Azure MCP Server 3.0, https://azure.microsoft.com/ja-jp/updates/v2/578662
[^11]: Generally Available: Marketplace private offer enhancements, https://azure.microsoft.com/ja-jp/updates/v2/576547
[^12]: Generally Available: Higher limit of Azure Blob Storage accounts per region per subscription, https://azure.microsoft.com/ja-jp/updates/v2/578358
[^13]: Generally Available: Cost management and tagging for Claude models in Microsoft Foundry, https://azure.microsoft.com/ja-jp/updates/v2/577260
[^14]: Generally Available: Azure Front Door profile and route level WAF policies, https://azure.microsoft.com/ja-jp/updates/v2/578153
[^15]: Generally Available: Network Watcher VNet flow logs filtering, https://azure.microsoft.com/ja-jp/updates/v2/577782
[^16]: Generally Available: Item Level Recovery for Azure VMs with Premium SSDv2 and Ultra Disks in Azure Backup, https://azure.microsoft.com/ja-jp/updates/v2/577963
[^17]: Generally Available: ABFS Vectored Read for Azure Data Lake Storage, https://azure.microsoft.com/ja-jp/updates/v2/577618
[^18]: Generally Available: Azure Cosmos DB Safe Key Rotation, https://azure.microsoft.com/ja-jp/updates/v2/576716
[^19]: Generally Available: Service tag match condition for Azure Front Door Premium WAF, https://azure.microsoft.com/ja-jp/updates/v2/577156
[^20]: Generally Available: Keyless TLS on Application Gateway with Azure Key Vault Managed HSM, https://azure.microsoft.com/ja-jp/updates/v2/577130
[^21]: Generally Available: Advanced platform metrics for Azure Monitor, https://azure.microsoft.com/ja-jp/updates/v2/575329
[^22]: Generally Available: Metrics usage insights for Azure Monitor workspace, https://azure.microsoft.com/ja-jp/updates/v2/577165
[^23]: Generally Available: Azure DNS enables DNS-based load balancing through Traffic Manager linked records, https://azure.microsoft.com/ja-jp/updates/v2/573917
[^24]: Generally Available: External key management for Azure Key Vault Managed HSM, https://azure.microsoft.com/ja-jp/updates/v2/574296
[^25]: Generally Available: Standard service endpoint, https://azure.microsoft.com/ja-jp/updates/v2/571025
[^26]: Generally Availabile: Automatic zone balance for Virtual Machine Scale Sets, https://azure.microsoft.com/ja-jp/updates/v2/576334
[^27]: Generally Available: Azure Cloud HSM hardware audit logging, https://azure.microsoft.com/ja-jp/updates/v2/576377
[^28]: Generally Available: Azure Site Recovery Support for Azure ARC-enabled Windows VMWare/Physical servers, https://azure.microsoft.com/ja-jp/updates/v2/576214
[^29]: Generally Available: Managed StandardV2 NAT Gateway for AKS, https://azure.microsoft.com/ja-jp/updates/v2/574430
[^30]: Generally Available: Azure Database for PostgreSQL flexible server in East US 3, https://azure.microsoft.com/ja-jp/updates/v2/573691
[^31]: Public Preview: Azure Firewall IPv6 now supports application rules, https://azure.microsoft.com/ja-jp/updates/v2/579507
[^32]: Public Preview: Multi-disk crash-consistent VM restore points for Premium SSD v2 and Ultra Disks on VMs with SCSI disk controller, https://azure.microsoft.com/ja-jp/updates/v2/579162
[^33]: Public Preview: JWT validation for Application Gateway for Containers, https://azure.microsoft.com/ja-jp/updates/v2/576382
[^34]: Public Preview: MCP gateway for Application Gateway for Containers, https://azure.microsoft.com/ja-jp/updates/v2/576388
[^35]: Public Preview: Private ingress for Application Gateway for Containers, https://azure.microsoft.com/ja-jp/updates/v2/576393
[^36]: Public Preview: Advanced capacity insights are now available in Azure Storage Discovery, https://azure.microsoft.com/ja-jp/updates/v2/578655
[^37]: Public Preview: Extend immutability for PITR backups for Azure SQL Database and Azure SQL Managed Instance, https://azure.microsoft.com/ja-jp/updates/v2/579305
[^38]: Public Preview: On-prem NAS share discovery and assessment are now available using Azure Migrate, https://azure.microsoft.com/ja-jp/updates/v2/577975
[^39]: Public Preview: Support database-level managed identity (including FIC) in Create Database Scoped Credential T-SQL, https://azure.microsoft.com/ja-jp/updates/v2/577491
[^40]: Public Preview: Cross Tenant Restore with Azure Backup, https://azure.microsoft.com/ja-jp/updates/v2/577117
[^41]: Public Preview: Disable VNet peering route, https://azure.microsoft.com/ja-jp/updates/v2/576242
[^42]: Public Preview: Azure Databricks Private network gateway, https://azure.microsoft.com/ja-jp/updates/v2/576556
[^43]: Public Preview: Azure Files cross-region data copy and synchronization with Azure Storage Mover, https://azure.microsoft.com/ja-jp/updates/v2/576542
[^44]: Retirement: Transition to Entra ID (formerly known as Azure AD) to query data from Azure Monitor application insights by March 31, 2027, https://azure.microsoft.com/ja-jp/updates/v2/transition-to-azure-ad-to-query-data-from-azure-monitor-application-insights-by-31-march-2026
[^45]: Retirement: OT security in Microsoft Defender for IoT, https://azure.microsoft.com/ja-jp/updates/v2/576255
[^46]: Retirement: Azure Fluid Relay, https://azure.microsoft.com/ja-jp/updates/v2/570498
[^47]: Retirement: Azure Key Vault Secrets Provider Extension for Azure Arc enabled Kubernetes clusters, https://azure.microsoft.com/ja-jp/updates/v2/570313
[^48]: Generally Available: Route maps for Azure Route Server, https://azure.microsoft.com/ja-jp/updates/v2/578966
[^49]: Announcing: Migrate Azure Container Apps logging destination from Log Analytics to Azure Monitor, https://azure.microsoft.com/ja-jp/updates/v2/577689
[^50]: Announcing: Choose Your Own Telephony (CYOT) for Microsoft Entra, https://azure.microsoft.com/ja-jp/updates/v2/577273
