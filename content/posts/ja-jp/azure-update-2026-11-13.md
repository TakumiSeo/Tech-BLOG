Title: Azure Update (2026/10/20 - 2026/11/12)
Date: 2026-11-13
Slug: azure-update-2026-11-13
Lang: ja-jp
Category: notebook
Tags: ai-machine-learning, analytics, application-gateway, application-insights, azure, azure-arc, azure-backup, azure-blob-storage, azure-container-apps, azure-container-storage, azure-cosmos-db, azure-data-lake-storage, azure-database-for-postgresql, azure-disk-storage, azure-firewall, azure-fluid-relay, azure-front-door, azure-functions, azure-kubernetes-service-aks, azure-migrate, azure-monitor, azure-route-server, azure-site-recovery, azure-sql-database, azure-sql-managed-instance, azure-storage-actions, azure-storage-discovery, azure-updates, compute, containers, databases, developer-tools, devops, hybrid-multicloud, identity, integration, internet-of-things, management-and-governance, microsoft-azure-portal, microsoft-entra-id-formerly-azure-ad, microsoft-foundry, migration, network-watcher, networking, sdks, security, service-bus, static-web-apps, storage, storage-accounts, virtual-machines, virtual-network, web, web-application-firewall
Summary: 2026年10月20日〜11月12日の Azure Update まとめ。GA 24件、パブリックプレビュー 18件、リタイア 4件、その他 4件の計50件。

2026年10月20日〜11月12日の Azure Update のまとめです。

| 分類 | 件数 |
| --- | --- |
| GA (一般提供) | 24 |
| パブリックプレビュー | 18 |
| リタイア | 4 |
| その他 | 4 |
| **合計** | **50** |

## GA (一般提供)

- **Generally Available: Azure Front Door mutual TLS authentication**[^1]
    - Mutual TLS (mTLS), also known as client certificate authentication, is now generally available on Azure Front Door Premium. Use X.509 client certificates to help protect sensitive applications and...

- **Generally Available: Azure Functions support for .NET 11**[^2]
    - Azure Functions support for .NET 11 is now generally available. You can now build Azure Functions apps targeting .NET 11 using the isolated worker model, while continuing to use the Azure Functions...

- **Generally Available: Azure Front Door edge actions**[^3]
    - Announcing the general availability of Azure Front Door edge actions (serverless compute at the edge). With edge actions, customers can execute lightweight JavaScript functions during Azure Front...

- **Generally Available: Azure Front Door TLS key exchange policy with post-quantum support**[^4]
    - Azure Front Door now supports configurable TLS key exchange policies, including hybrid post-quantum key exchange, to help you prepare for evolving cryptographic threats while meeting your security...

- **Generally Available: Azure Database for PostgreSQL stable REST API version 2026-10-01**[^5]
    - The Azure Database for PostgreSQL Flexible Server REST API version 2026-10-01 is now generally available. This stable API release introduces expanded capabilities for maintenance management,...

- **Generally Available: Enhanced Azure Site Recovery support for VMSS Flex**[^6]
    - Azure Site Recovery now offers an enhanced disaster recovery experience for virtual machines in Virtual Machine Scale Sets with flexible orchestration. The update improves target configuration and...

- **Generally Available: Change from virtual network integration to a private endpoint capable network configuration in Azure Database for PostgreSQL flexible server**[^7]
    - You now have greater flexibility in network design for Azure Database for PostgreSQL Flexible Server workloads. Now you can change existing VNet-integrated servers from delegated-subnet networking to...

- **Generally Available: Azure Storage Actions adds automatic task updates, execution controls, and case-sensitive matching**[^8]
    - Azure Storage Actions is introducing three enhancements to simplify task management and give you more control over automated data operations across Azure Blob and Data Lake Storage: Automatic...

- **Generally Available: Restart databases in Azure SQL DB via the Azure portal**[^9]
    - You can now restart or fail over databases directly from the Azure portal, including single databases, Hyperscale databases, and databases in elastic pools, without writing scripts against the Rest...

- **Generally Available: Geo-Replication on partitioned namespaces for Azure Service Bus Premium**[^10]
    - Geo-Replication on partitioned namespaces for Azure Service Bus Premium is now generally available. You can now combine the throughput benefits of partitioning with the reliability of replicating...

- **Generally Available: Azure Site Recovery for Azure Local**[^11]
    - Azure Site Recovery support for Azure Local is now generally available, making enterprise-grade disaster recovery simpler, accessible, easier to setup and secure than ever before. Customers can...

- **Generally Available: Large OS Disk Encryption for Azure Confidential VM migrations**[^12]
    - Large OS Disk Encryption (LOSDE) is now generally available for Azure Confidential VM migration scenarios. Organizations can move larger, production-scale workloads into confidential computing with...

- **Generally Available: HTTP DDoS ruleset for Azure Front Door Premium WAF**[^13]
    - Announcing the general availability of the HTTP DDoS ruleset for Azure Web Application Firewall (WAF) on Azure Front Door Premium. HTTP-layer DDoS attacks remain a leading cause of application...

- **Generally Available: Azure MCP Server 3.0**[^14]
    - Azure MCP Server 3.0 is now generally available, expanding how AI agents and developer tools interact with Azure through the open Model Context Protocol (MCP). This release introduces new and...

- **Generally Available: Marketplace private offer enhancements**[^15]
    - Private offers through Microsoft Marketplace help you optimize your spending power with pricing and terms aligned to your organization’s needs, including flexible billing, custom contract lengths,...

- **Generally Available: Higher limit of Azure Blob Storage accounts per region per subscription**[^16]
    - Higher Azure Storage account resource quotas are now generally available, supporting up to 1,000 storage accounts with standard endpoints per region, per subscription, up from the default of 250....

- **Generally Available: Cost management and tagging for Claude models in Microsoft Foundry**[^17]
    - Microsoft Foundry now brings Claude models into Azure Cost Management alongside the rest of your Foundry spend, generally available. Until now, Claude charges appeared under SaaS rather than under...

- **Generally Available: Azure Front Door profile and route level WAF policies**[^18]
    - Announcing the general availability of profile and route level policies for Azure Web Application Firewall (WAF) on Azure Front Door Premium. WAF policies are no longer limited to individual domains:...

- **Generally Available: Network Watcher VNet flow logs filtering**[^19]
    - Azure Network Watcher VNet flow logs filtering is now generally available, enabling you to control which network traffic flows are logged based on specific criteria such as IP addresses, ports,...

- **Generally Available: Item Level Recovery for Azure VMs with Premium SSDv2 and Ultra Disks in Azure Backup**[^20]
    - Azure Backup now supports Item-Level Recovery (ILR) for Azure virtual machines using Premium SSD v2 and Ultra disks with both 512 byte and 4KB logical sector sizes. You can now recover individual...

- **Generally Available: ABFS Vectored Read for Azure Data Lake Storage**[^21]
    - ABFS Vectored Read helps compatible analytics engines reduce request overhead for selective reads in Azure Data Lake Storage. By combining nearby file ranges into fewer storage requests and executing...

- **Generally Available: Azure Cosmos DB Safe Key Rotation**[^22]
    - Safe Key Rotation for Azure Cosmos DB is now generally available. You can view timestamp metadata showing when each account key was last used, helping you identify active keys before rotating or...

- **Generally Available: Service tag match condition for Azure Front Door Premium WAF**[^23]
    - Announcing the general availability of the service tag match condition for Azure Web Application Firewall (WAF) custom rules on Azure Front Door Premium. Service tags represent groups of IP address...

- **Generally Available: Keyless TLS on Application Gateway with Azure Key Vault Managed HSM**[^24]
    - Azure Application Gateway now supports keyless TLS termination using certificates whose private keys stay in Azure Key Vault Managed HSM. Each TLS handshake signature is performed inside the HSM, and...

## パブリックプレビュー

- **Public Preview: JWT validation with Azure Front Door Auth Policy**[^25]
    - JSON Web Token (JWT) validation through Azure Front Door Auth Policy is now in public preview on Azure Front Door Premium. Validate bearer tokens issued by Microsoft Entra ID at the edge before...

- **Public Preview: Auto scaling of ingestion limits in Azure Monitor workspace**[^26]
    - Auto scaling introduces a per-workspace capability in Azure Monitor Workspace (AMW) to automatically scale ingestion limits based on observed usage patterns. When enabled, the system dynamically...

- **Public Preview: SQL performance monitoring for Azure SQL Managed Instance**[^27]
    - The public preview of Microsoft-managed performance monitoring for Azure SQL Managed Instance is now available. Customers monitoring business-critical SQL Managed Instance workloads often rely on...

- **Public Preview: Rate limit grouping for Azure Front Door Premium WAF**[^28]
    - Announcing the public preview of rate limit grouping for Azure Web Application Firewall (WAF) on Azure Front Door Premium. By default, a rate limit rule counts requests separately for each client IP...

- **Public Preview: Distributed accelerator for cloud storage on AKS**[^29]
    - Distributed accelerator for cloud storage (DACS) is now in public preview for AI workloads running on Azure Kubernetes Service (AKS). DACS is a distributed read-through cache that runs within your...

- **Public Preview: Azure Front Door adds native gRPC support**[^30]
    - Announcing the public preview of gRPC support in Azure Front Door. Build and deliver gRPC applications through Azure Front Door Standard and Premium. Now in preview, gRPC support lets you route calls...

- **Public Preview: Modernize Arc-enabled Windows Servers with Azure File Sync**[^31]
    - Azure File Sync provides hybrid access or seamless migration of data from Windows Server to Azure Files while preserving the familiar local file server experience for users and applications. Now in...

- **Public Preview: Azure Firewall IPv6 now supports application rules**[^32]
    - Azure Firewall now supports application rules in IPv6 Public Preview, enabling layer 7 filtering for IPv6 HTTP and HTTPS traffic. The enhancement extends application-level controls to IPv6 and...

- **Public Preview: Multi-disk crash-consistent VM restore points for Premium SSD v2 and Ultra Disks on VMs with SCSI disk controller**[^33]
    - Multi-disk crash-consistent restore points for Azure virtual machines with Premium SSD v2 and Ultra data disks are now available in public preview on VMs with SCSI disk controllers. You can use this...

- **Public Preview: JWT validation for Application Gateway for Containers**[^34]
    - Application Gateway for Containers now supports centralized JSON Web Token validation through the AuthPolicy custom resource. Teams can validate a token signature, issuer, lifetime, and configured...

- **Public Preview: MCP gateway for Application Gateway for Containers**[^35]
    - Application Gateway for Containers now supports Model Context Protocol routing through the new MCPRoute custom resource. Platform teams can publish MCP servers behind a stable hostname and path while...

- **Public Preview: Private ingress for Application Gateway for Containers**[^36]
    - Application Gateway for Containers now supports private frontends that are reachable only through approved Azure Private Link private endpoints. This enables organizations to keep internal...

- **Public Preview: Advanced capacity insights are now available in Azure Storage Discovery**[^37]
    - Advanced capacity insights are now available for preview in Azure Storage Discovery. Storage Discovery now provides greater visibility into storage usage through insights such as access patterns,...

- **Public Preview: Extend immutability for PITR backups for Azure SQL Database and Azure SQL Managed Instance**[^38]
    - With this enhancement, you have the ability to lock your retention to the configured PITR retention, beyond the default 7 days of immutable backups that are already available. This is especially...

- **Public Preview: On-prem NAS share discovery and assessment are now available using Azure Migrate**[^39]
    - Azure Migrate now supports discovery and assessment for network-attached storage, allowing customers and partners to plan migrations of Dell PowerScale (OneFS) and NetApp ONTAP storage to Azure. The...

- **Public Preview: Support database-level managed identity (including FIC) in Create Database Scoped Credential T-SQL**[^40]
    - With database-level managed identity in Azure SQL Database, you can use a user-assigned managed identity for each database to query files in Azure Blob Storage and Azure Data Lake Storage Gen2...

- **Public Preview: Cross Tenant Restore with Azure Backup**[^41]
    - Cross-Tenant Restore (CTR) helps organizations establish an independent recovery path by enabling Azure VM backups to be restored into a separate Azure tenant. It strengthens cyber resilience while...

- **Public Preview: Disable VNet peering route**[^42]
    - Announcing the public preview of disable VNet peering route, a route-table capability that gives you more control over traffic between peered virtual networks. DPR suppresses system-generated peering...

## リタイア

- **Retirement: Support for .NET 8 and .NET 9 on Static Web Apps is ending November 10, 2026**[^43]
    - Support for .NET 8 and .NET 9 will end on November 10, 2026. Please transition your managed Functions APIs to .NET 10 by that date. Your apps will continue to operate, but security updates will no...

- **Retirement: Transition to Entra ID (formerly known as Azure AD) to query data from Azure Monitor application insights by March 31, 2027**[^44]
    - *Note: We have extended the retirement date to March 31, 2027. On March 31, 2027 API keys used query application insights will be retired. You'll need to transition to Microsoft Entra ID (formerly...

- **Retirement: OT security in Microsoft Defender for IoT**[^45]
    - This is the formal notice that Microsoft plans to deprecate the operational technology (OT) security component of Microsoft Defender for IoT. The service will be fully deprecated in October 2029,...

- **Retirement: Azure Fluid Relay**[^46]
    - On June 2, 2027, we will retire Azure Fluid Relay. After this date, Azure Fluid Relay will reach end of availability, and workloads that continue to depend on the service may experience disruption....

## その他

- **Public Preview: Azure Route Server dual-stack IPv4/IPv6 support**[^47]
    - Azure Route Server now supports IPv4/IPv6 dual-stack mode in public preview, enabling route exchange for both address families across supported hybrid networking connections. Existing IPv4...

- **Generally Available: Route maps for Azure Route Server**[^48]
    - Route maps for Azure Route Server are now generally available in the Azure public cloud. Route maps provide fine-grained control over inbound and outbound routing across hybrid connections. Customers...

- **Announcing: Migrate Azure Container Apps logging destination from Log Analytics to Azure Monitor**[^49]
    - The Log Analytics logging destination for Azure Container Apps is now a legacy logging option. Existing environments configured with the Log Analytics logging destination will continue to function...

- **Announcing: Choose Your Own Telephony (CYOT) for Microsoft Entra**[^50]
    - What and why Starting October 30, 2026, Microsoft Entra ID will make the Choose Your Own Telephony Provider experience available. This feature enables organizations to use a supported third-party...

[^1]: Generally Available: Azure Front Door mutual TLS authentication, https://azure.microsoft.com/ja-jp/updates/v2/577678
[^2]: Generally Available: Azure Functions support for .NET 11, https://azure.microsoft.com/ja-jp/updates/v2/578773
[^3]: Generally Available: Azure Front Door edge actions, https://azure.microsoft.com/ja-jp/updates/v2/579310
[^4]: Generally Available: Azure Front Door TLS key exchange policy with post-quantum support, https://azure.microsoft.com/ja-jp/updates/v2/577668
[^5]: Generally Available: Azure Database for PostgreSQL stable REST API version 2026-10-01, https://azure.microsoft.com/ja-jp/updates/v2/579300
[^6]: Generally Available: Enhanced Azure Site Recovery support for VMSS Flex, https://azure.microsoft.com/ja-jp/updates/v2/578926
[^7]: Generally Available: Change from virtual network integration to a private endpoint capable network configuration in Azure Database for PostgreSQL flexible server, https://azure.microsoft.com/ja-jp/updates/v2/574541
[^8]: Generally Available: Azure Storage Actions adds automatic task updates, execution controls, and case-sensitive matching, https://azure.microsoft.com/ja-jp/updates/v2/578628
[^9]: Generally Available: Restart databases in Azure SQL DB via the Azure portal, https://azure.microsoft.com/ja-jp/updates/v2/577992
[^10]: Generally Available: Geo-Replication on partitioned namespaces for Azure Service Bus Premium, https://azure.microsoft.com/ja-jp/updates/v2/579021
[^11]: Generally Available: Azure Site Recovery for Azure Local, https://azure.microsoft.com/ja-jp/updates/v2/579111
[^12]: Generally Available: Large OS Disk Encryption for Azure Confidential VM migrations, https://azure.microsoft.com/ja-jp/updates/v2/578850
[^13]: Generally Available: HTTP DDoS ruleset for Azure Front Door Premium WAF, https://azure.microsoft.com/ja-jp/updates/v2/578681
[^14]: Generally Available: Azure MCP Server 3.0, https://azure.microsoft.com/ja-jp/updates/v2/578662
[^15]: Generally Available: Marketplace private offer enhancements, https://azure.microsoft.com/ja-jp/updates/v2/576547
[^16]: Generally Available: Higher limit of Azure Blob Storage accounts per region per subscription, https://azure.microsoft.com/ja-jp/updates/v2/578358
[^17]: Generally Available: Cost management and tagging for Claude models in Microsoft Foundry, https://azure.microsoft.com/ja-jp/updates/v2/577260
[^18]: Generally Available: Azure Front Door profile and route level WAF policies, https://azure.microsoft.com/ja-jp/updates/v2/578153
[^19]: Generally Available: Network Watcher VNet flow logs filtering, https://azure.microsoft.com/ja-jp/updates/v2/577782
[^20]: Generally Available: Item Level Recovery for Azure VMs with Premium SSDv2 and Ultra Disks in Azure Backup, https://azure.microsoft.com/ja-jp/updates/v2/577963
[^21]: Generally Available: ABFS Vectored Read for Azure Data Lake Storage, https://azure.microsoft.com/ja-jp/updates/v2/577618
[^22]: Generally Available: Azure Cosmos DB Safe Key Rotation, https://azure.microsoft.com/ja-jp/updates/v2/576716
[^23]: Generally Available: Service tag match condition for Azure Front Door Premium WAF, https://azure.microsoft.com/ja-jp/updates/v2/577156
[^24]: Generally Available: Keyless TLS on Application Gateway with Azure Key Vault Managed HSM, https://azure.microsoft.com/ja-jp/updates/v2/577130
[^25]: Public Preview: JWT validation with Azure Front Door Auth Policy, https://azure.microsoft.com/ja-jp/updates/v2/577673
[^26]: Public Preview: Auto scaling of ingestion limits in Azure Monitor workspace, https://azure.microsoft.com/ja-jp/updates/v2/578207
[^27]: Public Preview: SQL performance monitoring for Azure SQL Managed Instance, https://azure.microsoft.com/ja-jp/updates/v2/574158
[^28]: Public Preview: Rate limit grouping for Azure Front Door Premium WAF, https://azure.microsoft.com/ja-jp/updates/v2/580155
[^29]: Public Preview: Distributed accelerator for cloud storage on AKS, https://azure.microsoft.com/ja-jp/updates/v2/578454
[^30]: Public Preview: Azure Front Door adds native gRPC support, https://azure.microsoft.com/ja-jp/updates/v2/579383
[^31]: Public Preview: Modernize Arc-enabled Windows Servers with Azure File Sync, https://azure.microsoft.com/ja-jp/updates/v2/579854
[^32]: Public Preview: Azure Firewall IPv6 now supports application rules, https://azure.microsoft.com/ja-jp/updates/v2/579507
[^33]: Public Preview: Multi-disk crash-consistent VM restore points for Premium SSD v2 and Ultra Disks on VMs with SCSI disk controller, https://azure.microsoft.com/ja-jp/updates/v2/579162
[^34]: Public Preview: JWT validation for Application Gateway for Containers, https://azure.microsoft.com/ja-jp/updates/v2/576382
[^35]: Public Preview: MCP gateway for Application Gateway for Containers, https://azure.microsoft.com/ja-jp/updates/v2/576388
[^36]: Public Preview: Private ingress for Application Gateway for Containers, https://azure.microsoft.com/ja-jp/updates/v2/576393
[^37]: Public Preview: Advanced capacity insights are now available in Azure Storage Discovery, https://azure.microsoft.com/ja-jp/updates/v2/578655
[^38]: Public Preview: Extend immutability for PITR backups for Azure SQL Database and Azure SQL Managed Instance, https://azure.microsoft.com/ja-jp/updates/v2/579305
[^39]: Public Preview: On-prem NAS share discovery and assessment are now available using Azure Migrate, https://azure.microsoft.com/ja-jp/updates/v2/577975
[^40]: Public Preview: Support database-level managed identity (including FIC) in Create Database Scoped Credential T-SQL, https://azure.microsoft.com/ja-jp/updates/v2/577491
[^41]: Public Preview: Cross Tenant Restore with Azure Backup, https://azure.microsoft.com/ja-jp/updates/v2/577117
[^42]: Public Preview: Disable VNet peering route, https://azure.microsoft.com/ja-jp/updates/v2/576242
[^43]: Retirement: Support for .NET 8 and .NET 9 on Static Web Apps is ending November 10, 2026, https://azure.microsoft.com/ja-jp/updates/v2/575106
[^44]: Retirement: Transition to Entra ID (formerly known as Azure AD) to query data from Azure Monitor application insights by March 31, 2027, https://azure.microsoft.com/ja-jp/updates/v2/transition-to-azure-ad-to-query-data-from-azure-monitor-application-insights-by-31-march-2026
[^45]: Retirement: OT security in Microsoft Defender for IoT, https://azure.microsoft.com/ja-jp/updates/v2/576255
[^46]: Retirement: Azure Fluid Relay, https://azure.microsoft.com/ja-jp/updates/v2/570498
[^47]: Public Preview: Azure Route Server dual-stack IPv4/IPv6 support, https://azure.microsoft.com/ja-jp/updates/v2/579746
[^48]: Generally Available: Route maps for Azure Route Server, https://azure.microsoft.com/ja-jp/updates/v2/578966
[^49]: Announcing: Migrate Azure Container Apps logging destination from Log Analytics to Azure Monitor, https://azure.microsoft.com/ja-jp/updates/v2/577689
[^50]: Announcing: Choose Your Own Telephony (CYOT) for Microsoft Entra, https://azure.microsoft.com/ja-jp/updates/v2/577273
