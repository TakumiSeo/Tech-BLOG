Title: Azure Update (2026/09/29 - 2026/10/26)
Date: 2026-10-27
Slug: azure-update-2026-10-27
Lang: ja-jp
Category: notebook
Tags: ai-machine-learning, analytics, api-management, app-service, application-gateway, application-insights, azure, azure-backup, azure-blob-storage, azure-container-apps, azure-copilot, azure-cosmos-db, azure-data-lake-storage, azure-database-for-mysql, azure-database-for-postgresql, azure-databricks, azure-deployment-environments, azure-dns, azure-files, azure-front-door, azure-horizondb, azure-kubernetes-service-aks, azure-monitor, azure-nat-gateway, azure-private-link, azure-site-recovery, azure-sql-database, azure-stack-hub, azure-updates, compute, containers, databases, developer-tools, devops, hybrid-multicloud, identity, integration, internet-of-things, key-vault, linux-virtual-machines, management-and-governance, microsoft-dev-box, microsoft-entra-id-formerly-azure-ad, microsoft-fabric, migration, mobile, network-watcher, networking, security, sql-server-on-azure-virtual-machines, storage, traffic-manager, virtual-desktop-infrastructure, virtual-machines, virtual-network, web, web-application-firewall, windows-virtual-machines
Summary: 2026年9月29日〜10月26日の Azure Update まとめ。GA 21件、パブリックプレビュー 12件、リタイア 13件、その他 4件の計50件。

2026年9月29日〜10月26日の Azure Update のまとめです。

| 分類 | 件数 |
| --- | --- |
| GA (一般提供) | 21 |
| パブリックプレビュー | 12 |
| リタイア | 13 |
| その他 | 4 |
| **合計** | **50** |

## GA (一般提供)

- **Generally Available: Network Watcher VNet flow logs filtering**[^1]
    - Azure Network Watcher VNet flow logs filtering is now generally available, enabling you to control which network traffic flows are logged based on specific criteria such as IP addresses, ports,...

- **Generally Available: Item Level Recovery for Azure VMs with Premium SSDv2 and Ultra Disks in Azure Backup**[^2]
    - Azure Backup now supports Item-Level Recovery (ILR) for Azure virtual machines using Premium SSD v2 and Ultra disks with both 512 byte and 4KB logical sector sizes. You can now recover individual...

- **Generally Available: ABFS Vectored Read for Azure Data Lake Storage**[^3]
    - ABFS Vectored Read helps compatible analytics engines reduce request overhead for selective reads in Azure Data Lake Storage. By combining nearby file ranges into fewer storage requests and executing...

- **Generally Available: Azure Cosmos DB Safe Key Rotation**[^4]
    - Safe Key Rotation for Azure Cosmos DB is now generally available. You can view timestamp metadata showing when each account key was last used, helping you identify active keys before rotating or...

- **Generally Available: Service tag match condition for Azure Front Door Premium WAF**[^5]
    - Announcing the general availability of the service tag match condition for Azure Web Application Firewall (WAF) custom rules on Azure Front Door Premium. Service tags represent groups of IP address...

- **Generally Available: Keyless TLS on Application Gateway with Azure Key Vault Managed HSM**[^6]
    - Azure Application Gateway now supports keyless TLS termination using certificates whose private keys stay in Azure Key Vault Managed HSM. Each TLS handshake signature is performed inside the HSM, and...

- **Generally Available: Advanced platform metrics for Azure Monitor**[^7]
    - Advanced platform metrics for Azure Monitor are now generally available. Advanced platform metrics provide finer-grained signals that help customers more quickly and accurately identify changes and...

- **Generally Available: Metrics usage insights for Azure Monitor workspace**[^8]
    - Metrics usage insights is now generally available, giving you greater visibility into what’s driving metrics usage across your Azure Monitor workspace. Monitor workspace utilization, identify unused...

- **Generally Available: Azure DNS enables DNS-based load balancing through Traffic Manager linked records**[^9]
    - Azure DNS now provides DNS based load balancing by seamless integration with Azure Traffic Manager. Customers can directly associate an Azure DNS record set with a Traffic Manager profile,...

- **Generally Available: External key management for Azure Key Vault Managed HSM**[^10]
    - External key management for Azure Key Vault Managed HSM is now generally available in all Azure public regions. For organizations with regulatory or sovereignty requirements to retain physical...

- **Generally Available: Standard service endpoint **[^11]
    - Standard service endpoint, a new capability in the Azure Private Link family, provides a scalable and secure approach for connecting Azure IaaS workloads to Azure PaaS services. Standard service...

- **Generally Availabile: Automatic zone balance for Virtual Machine Scale Sets**[^12]
    - Automatic zone balance for Virtual Machine Scale Sets is now generally available. This feature continuously monitors scale sets deployed across availability zones and automatically redistributes VM...

- **Generally Available: Azure Cloud HSM hardware audit logging**[^13]
    - Hardware Audit Logging for Azure Cloud HSM provides hardware-generated audit records for supported HSM management operations, helping organizations strengthen security monitoring, compliance...

- **Generally Available: Azure Site Recovery Support for Azure ARC-enabled Windows VMWare/Physical servers**[^14]
    - Azure Site Recovery (ASR) now supports disaster recovery for Azure ARC-enabled Windows VMWare virtual machines and on-premise physical servers. Customers can protect ARC-managed machines with ASR...

- **Generally Available: Managed StandardV2 NAT Gateway for AKS**[^15]
    - AKS will now provision and manage a StandardV2 NAT Gateway for clusters using an AKS-managed virtual network. StandardV2 is now the default managed NAT Gateway SKU for new clusters in supported...

- **Generally Available: Azure Database for PostgreSQL flexible server in East US 3 **[^16]
    - Now you can deploy Azure Database for PostgreSQL flexible server in the East US 3 Azure region. Learn more .

- **Generally Available: Exceptions in WAF for Azure Application Gateway and Azure Front Door**[^17]
    - Announcing the general availability of exceptions for Web Application Firewall on Azure Application Gateway and Azure Front Door. Azure Web Application Firewall (WAF) helps protect your web...

- **Generally Available: Anyscale on Azure**[^18]
    - Anyscale on Azure is now Generally Available. Anyscale on Azure is a managed platform for running distributed Python workloads on Ray. It deploys directly onto your Azure Kubernetes Service (AKS)...

- **Generally Available: Enabling the Bulk admin role for SQL Server on Linux**[^19]
    - Starting with SQL Server 2025 CU9 and SQL Server 2022 CU27, SQL Server on Linux supports the bulkadmin fixed server role and the ADMINISTER BULK OPERATIONS permission for performing bulk data import...

- **Generally Available: SQL Server on Azure Virtual Machines in Azure Bleu **[^20]
    - SQL Server on Azure Virtual Machines is now available in Azure Bleu, enabling you to deploy and manage SQL Server workloads in France's sovereign cloud environment while meeting data residency and...

- **Generally Available: Storage optimized Lasv5 and Laosv5 Azure VM series **[^21]
    - The Laosv5 series and Lasv5 storage optimized VMs, based on the 5th Gen AMD EPYC™ processor (Turin), are now generally available. Lasv5 and Laosv5 VMs have sizes ranging from 2-160 vCPUs, with 8GiB...

## パブリックプレビュー

- **Public Preview: Disable VNet peering route**[^22]
    - Announcing the public preview of disable VNet peering route, a route-table capability that gives you more control over traffic between peered virtual networks. DPR suppresses system-generated peering...

- **Public Preview: Azure Databricks Private network gateway**[^23]
    - Private network gateway for Azure Databricks is now in Public Preview, enabling serverless compute to connect to resources in your virtual network (VNet) and transitively connected networks through a...

- **Public Preview: Azure Files cross-region data copy and synchronization with Azure Storage Mover**[^24]
    - Azure Files customers can now copy and synchronize file share data across storage accounts, Azure regions, and subscriptions within the same tenant using Azure Storage Mover. Schedule incremental...

- **Public Preview: Microsoft Agent 365 integration with Azure API Management**[^25]
    - The integration between Microsoft Agent 365 and Azure API Management is now available in public preview, helping organizations connect centralized governance with runtime enforcement for MCP servers...

- **Public Preview: AKS on bare metal now on Ubuntu**[^26]
    - Running Kubernetes on-premises often means adding a virtualization layer, adapting to unfamiliar infrastructure, or giving up control over the hardware and software your applications depend on. For...

- **Public Preview: Azure HorizonDB expands to additional regions**[^27]
    - Azure HorizonDB is expanding to additional Azure regions, giving you greater flexibility to deploy PostgreSQL workloads closer to your applications and users. With expanded regional availability, you...

- **Public Preview: Azure Backup for PostgreSQL flexible server and elastic cluster (v2)**[^28]
    - Azure Backup for PostgreSQL flexible server and elastic cluster (v2) preview brings enterprise-grade long-term retention to PostgreSQL. Backups are taken as physical backups from managed disk...

- **Public Preview: IPv6 Support for Application Gateway WAF **[^29]
    - Announcing the Public Preview of IPv6 support for Application Gateway WAF. Application Gateway Web Application Firewall (WAF) now supports inspection and enforcement for IPv6 traffic in Public...

- **Public Preview:  Major version upgrades (MVU) for Azure Database for PostgreSQL elastic clusters **[^30]
    - MVUs are now available for elastic clusters in Azure Database for PostgreSQL. You can upgrade an existing elastic cluster to a supported newer PostgreSQL version in place without provisioning a...

- **Public Preview: Reader Endpoint for Azure Database for MySQL **[^31]
    - We’re happy to announce the public preview of reader endpoint support to simplify connection management when using multiple replicas in Azure Database for MySQL - Flexible Server. A reader endpoint...

- **Public Preview: SQL performance monitoring for SQL Server on Azure Virtual Machines **[^32]
    - The public preview of Microsoft-managed performance monitoring for SQL Server on Azure Virtual Machines is now available. You can now monitor SQL Server on Azure Virtual Machines without building...

- **Public Preview: Ubuntu 26.04 support in AKS**[^33]
    - Teams running Ubuntu node pools on AKS need to stay current with Ubuntu LTS releases, but each OS transition can introduce package footprint, security, and compatibility concerns. Ubuntu 26.04...

## リタイア

- **Retirement: Azure Key Vault Secrets Provider Extension for Azure Arc enabled Kubernetes clusters**[^34]
    - The Azure Key Vault Secrets Provider Extension for Azure Arc-enabled Kubernetes will be retired on October 9, 2027. Customers currently using the extension should plan to migrate to the Azure Key...

- **Retirement: Microsoft Dev Box will be retired on September 18, 2028**[^35]
    - Microsoft Dev Box will retire on September 18, 2028. Beginning on September 14, 2026, Microsoft Dev Box will begin the closing-down process. After retirement, Microsoft Dev Box will no longer be...

- **Retirement: Azure Deployment Environments will be retired on February 22, 2027**[^36]
    - Azure Deployment Environments will retire on February 22, 2027. Beginning on September 14, 2026, Azure Deployment Environments will begin the closing-down process. After retirement, the service will...

- **Retirement: Pod name dimension in AKS pod platform metrics**[^37]
    - Beginning September 30, 2027, support for the pod name dimension on the following Azure Monitor platform metrics is retiring, and these metrics are transitioning to aggregate pod counters: Number of...

- **Retirement: Azure App Service on Azure Stack Hub**[^38]
    - Azure App Service on Azure Stack Hub will be retired on September 30, 2029 . Starting September 30, 2026 , new installations will no longer be supported, and no new product releases, features, or...

- **Retirement: Support for Java 8, 11 and 17 will end on September 1, 2027**[^39]
    - On September 1, 2027 support for Java 8, 11 and 17 will end. Your apps that are hosted on App Service will continue to run, but security updates will no longer be available, and we’ll no longer...

- **Retirement: Always Encrypted with Intel SGX Enclaves**[^40]
    - Always Encrypted with Intel SGX enclaves in Azure SQL Database will retire on October 31, 2027 as support for SGX-enabled DC-series hardware is phased out. Customers should transition to...

- **Retirement: DCsv3 and DCdsv3-series Azure Virtual Machines will be retired on October 31, 2029**[^41]
    - On October 31, 2029, DCsv3 and DCdsv3-series Azure Linux, Windows and Dedicated Host virtual machines will be retired. After that date, they will no longer be available for use or purchase. Before...

- **Retirement: NVv3-series Azure Virtual Machines**[^42]
    - On September 30, 2026, Microsoft Azure retired the Standard_NV12s_v3, Standard_NV12hs_v3, Standard_NV24s_v3, Standard_NV24ms_v3, Standard_NV32ms_v3, and Standard_NV48s_v3 virtual machines (VMs) in...

- **Retirement: NVv4-series Azure Virtual Machines**[^43]
    - On September 30, 2026, Microsoft Azure retired the Standard_NV4as_v4, Standard_NV4ahs_v4, Standard_NV8as_v4, Standard_NV8ahs_v4, Standard_NV16as_v4, Standard_NV16ahs_v4, Standard_NV32as_v4, and...

- **Retirement: Dv3, Dsv3, Ev3, and Esv3 Azure VMs **[^44]
    - As part of the Microsoft Azure VM lifecycle policy , Microsoft is announcing the retirement of the Dv3, Dsv3, Ev3, and Esv3 Azure VM series in public cloud Azure regions. These VMs will enter the...

- **Retirement: Transition to using standard tests for single-step availability testing in Azure Monitor application insights by September 30, 2028**[^45]
    - URL ping tests in Application Insights were originally planned for retirement on September 30, 2026. In response to customer feedback requesting more time to complete migration, the retirement date...

- **Retirement: Functions on Azure Container Apps V1 **[^46]
    - The Functions on Azure Container Apps (ACA) V1 will be retired on September 29, 2027. After this date, existing Functions on ACA V1 Apps will stop running and no longer process requests or...

## その他

- **Announcing: Choose Your Own Telephony (CYOT) for Microsoft Entra**[^47]
    - What and why Starting October 30, 2026, Microsoft Entra ID will make the Choose Your Own Telephony Provider experience available. This feature enables organizations to use a supported third-party...

- **Announcing: Multiparty private offers in Microsoft Marketplace expands to Hong Kong**[^48]
    - Multiparty private offers give Microsoft partners a way to procure third-party cloud and AI solutions for customers through Marketplace. Software companies can expand into new markets by working with...

- **Announcing: Table discovery in OneLake Catalog search**[^49]
    - Starting October 15, 2026, Search in Microsoft Fabric will return tables from semantic models, lakehouses, and mirrored databases as individual results. Users can search by table name or description,...

- **Announcing: Azure canvases for GitHub Copilot**[^50]
    - Discover Azure canvases for GitHub Copilot, interactive shared workspaces that bring Azure tools, dashboards, and guided workflows directly alongside your Copilot conversations. Explore Azure...

---

[^1]: Generally Available: Network Watcher VNet flow logs filtering, https://azure.microsoft.com/ja-jp/updates/v2/577782
[^2]: Generally Available: Item Level Recovery for Azure VMs with Premium SSDv2 and Ultra Disks in Azure Backup, https://azure.microsoft.com/ja-jp/updates/v2/577963
[^3]: Generally Available: ABFS Vectored Read for Azure Data Lake Storage, https://azure.microsoft.com/ja-jp/updates/v2/577618
[^4]: Generally Available: Azure Cosmos DB Safe Key Rotation, https://azure.microsoft.com/ja-jp/updates/v2/576716
[^5]: Generally Available: Service tag match condition for Azure Front Door Premium WAF, https://azure.microsoft.com/ja-jp/updates/v2/577156
[^6]: Generally Available: Keyless TLS on Application Gateway with Azure Key Vault Managed HSM, https://azure.microsoft.com/ja-jp/updates/v2/577130
[^7]: Generally Available: Advanced platform metrics for Azure Monitor, https://azure.microsoft.com/ja-jp/updates/v2/575329
[^8]: Generally Available: Metrics usage insights for Azure Monitor workspace, https://azure.microsoft.com/ja-jp/updates/v2/577165
[^9]: Generally Available: Azure DNS enables DNS-based load balancing through Traffic Manager linked records, https://azure.microsoft.com/ja-jp/updates/v2/573917
[^10]: Generally Available: External key management for Azure Key Vault Managed HSM, https://azure.microsoft.com/ja-jp/updates/v2/574296
[^11]: Generally Available: Standard service endpoint , https://azure.microsoft.com/ja-jp/updates/v2/571025
[^12]: Generally Availabile: Automatic zone balance for Virtual Machine Scale Sets, https://azure.microsoft.com/ja-jp/updates/v2/576334
[^13]: Generally Available: Azure Cloud HSM hardware audit logging, https://azure.microsoft.com/ja-jp/updates/v2/576377
[^14]: Generally Available: Azure Site Recovery Support for Azure ARC-enabled Windows VMWare/Physical servers, https://azure.microsoft.com/ja-jp/updates/v2/576214
[^15]: Generally Available: Managed StandardV2 NAT Gateway for AKS, https://azure.microsoft.com/ja-jp/updates/v2/574430
[^16]: Generally Available: Azure Database for PostgreSQL flexible server in East US 3 , https://azure.microsoft.com/ja-jp/updates/v2/573691
[^17]: Generally Available: Exceptions in WAF for Azure Application Gateway and Azure Front Door, https://azure.microsoft.com/ja-jp/updates/v2/574343
[^18]: Generally Available: Anyscale on Azure, https://azure.microsoft.com/ja-jp/updates/v2/573744
[^19]: Generally Available: Enabling the Bulk admin role for SQL Server on Linux, https://azure.microsoft.com/ja-jp/updates/v2/573443
[^20]: Generally Available: SQL Server on Azure Virtual Machines in Azure Bleu , https://azure.microsoft.com/ja-jp/updates/v2/571499
[^21]: Generally Available: Storage optimized Lasv5 and Laosv5 Azure VM series , https://azure.microsoft.com/ja-jp/updates/v2/572630
[^22]: Public Preview: Disable VNet peering route, https://azure.microsoft.com/ja-jp/updates/v2/576242
[^23]: Public Preview: Azure Databricks Private network gateway, https://azure.microsoft.com/ja-jp/updates/v2/576556
[^24]: Public Preview: Azure Files cross-region data copy and synchronization with Azure Storage Mover, https://azure.microsoft.com/ja-jp/updates/v2/576542
[^25]: Public Preview: Microsoft Agent 365 integration with Azure API Management, https://azure.microsoft.com/ja-jp/updates/v2/574204
[^26]: Public Preview: AKS on bare metal now on Ubuntu, https://azure.microsoft.com/ja-jp/updates/v2/573782
[^27]: Public Preview: Azure HorizonDB expands to additional regions, https://azure.microsoft.com/ja-jp/updates/v2/572940
[^28]: Public Preview: Azure Backup for PostgreSQL flexible server and elastic cluster (v2), https://azure.microsoft.com/ja-jp/updates/v2/573425
[^29]: Public Preview: IPv6 Support for Application Gateway WAF , https://azure.microsoft.com/ja-jp/updates/v2/573861
[^30]: Public Preview:  Major version upgrades (MVU) for Azure Database for PostgreSQL elastic clusters , https://azure.microsoft.com/ja-jp/updates/v2/571504
[^31]: Public Preview: Reader Endpoint for Azure Database for MySQL , https://azure.microsoft.com/ja-jp/updates/v2/569653
[^32]: Public Preview: SQL performance monitoring for SQL Server on Azure Virtual Machines , https://azure.microsoft.com/ja-jp/updates/v2/571894
[^33]: Public Preview: Ubuntu 26.04 support in AKS, https://azure.microsoft.com/ja-jp/updates/v2/573214
[^34]: Retirement: Azure Key Vault Secrets Provider Extension for Azure Arc enabled Kubernetes clusters, https://azure.microsoft.com/ja-jp/updates/v2/570313
[^35]: Retirement: Microsoft Dev Box will be retired on September 18, 2028, https://azure.microsoft.com/ja-jp/updates/v2/567933
[^36]: Retirement: Azure Deployment Environments will be retired on February 22, 2027, https://azure.microsoft.com/ja-jp/updates/v2/567934
[^37]: Retirement: Pod name dimension in AKS pod platform metrics, https://azure.microsoft.com/ja-jp/updates/v2/570232
[^38]: Retirement: Azure App Service on Azure Stack Hub, https://azure.microsoft.com/ja-jp/updates/v2/568178
[^39]: Retirement: Support for Java 8, 11 and 17 will end on September 1, 2027, https://azure.microsoft.com/ja-jp/updates/v2/568585
[^40]: Retirement: Always Encrypted with Intel SGX Enclaves, https://azure.microsoft.com/ja-jp/updates/v2/569236
[^41]: Retirement: DCsv3 and DCdsv3-series Azure Virtual Machines will be retired on October 31, 2029, https://azure.microsoft.com/ja-jp/updates/v2/569592
[^42]: Retirement: NVv3-series Azure Virtual Machines, https://azure.microsoft.com/ja-jp/updates/v2/573414
[^43]: Retirement: NVv4-series Azure Virtual Machines, https://azure.microsoft.com/ja-jp/updates/v2/573415
[^44]: Retirement: Dv3, Dsv3, Ev3, and Esv3 Azure VMs , https://azure.microsoft.com/ja-jp/updates/v2/572346
[^45]: Retirement: Transition to using standard tests for single-step availability testing in Azure Monitor application insights by September 30, 2028, https://azure.microsoft.com/ja-jp/updates/v2/transition-to-using-standard-tests-for-singlestep-availability-testing-in-azure-monitor-application-insights-by-30-september
[^46]: Retirement: Functions on Azure Container Apps V1 , https://azure.microsoft.com/ja-jp/updates/v2/570800
[^47]: Announcing: Choose Your Own Telephony (CYOT) for Microsoft Entra, https://azure.microsoft.com/ja-jp/updates/v2/577273
[^48]: Announcing: Multiparty private offers in Microsoft Marketplace expands to Hong Kong, https://azure.microsoft.com/ja-jp/updates/v2/571831
[^49]: Announcing: Table discovery in OneLake Catalog search, https://azure.microsoft.com/ja-jp/updates/v2/573875
[^50]: Announcing: Azure canvases for GitHub Copilot, https://azure.microsoft.com/ja-jp/updates/v2/573385
