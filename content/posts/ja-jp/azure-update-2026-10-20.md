Title: Azure Update (2026/09/29 - 2026/10/19)
Date: 2026-10-20
Slug: azure-update-2026-10-20
Lang: ja-jp
Category: notebook
Tags: api-management, app-service, application-gateway, application-insights, azure-arc, azure-backup, azure-container-apps, azure-copilot, azure-database-for-mysql, azure-database-for-postgresql, azure-databricks, azure-deployment-environments, azure-dns, azure-files, azure-front-door, azure-horizondb, azure-kubernetes-service-(aks), azure-monitor, azure-nat-gateway, azure-private-link, azure-site-recovery, azure-sql-database, azure-stack-hub, key-vault, linux-virtual-machines, microsoft-dev-box, microsoft-fabric, sql-server-on-azure-virtual-machines, traffic-manager, virtual-machines, web-application-firewall, windows-virtual-machines
Summary: 2026年09月29日〜2026年10月19日の Azure Update まとめ。GA 18件、パブリックプレビュー 16件、リタイア 13件、その他 3件の計50件。

## 概要

2026年09月29日から2026年10月19日にかけての Azure Update をまとめました。

| カテゴリ | 件数 |
| --- | --- |
| GA (一般提供) | 18 |
| パブリックプレビュー | 16 |
| リタイア | 13 |
| その他 | 3 |
| **合計** | **50** |

## GA (一般提供)

- **Generally Available: Metrics usage insights for Azure Monitor workspace**[^1]
    - Metrics usage insights is now generally available, giving you greater visibility into what’s driving metrics usage across your Azure Monitor workspace. Monitor workspace utilization, identify unuse...

- **Generally Available: Azure DNS enables DNS-based load balancing through Traffic Manager linked records**[^2]
    - Azure DNS now provides DNS based load balancing by seamless integration with Azure Traffic Manager. Customers can directly associate an Azure DNS record set with a Traffic Manager profile, eliminat...

- **Generally Available: External key management for Azure Key Vault Managed HSM**[^3]
    - External key management for Azure Key Vault Managed HSM is now generally available in all Azure public regions. For organizations with regulatory or sovereignty requirements to retain physical cont...

- **Generally Available: Standard service endpoint **[^4]
    - Standard service endpoint, a new capability in the Azure Private Link family, provides a scalable and secure approach for connecting Azure IaaS workloads to Azure PaaS services. Standard service en...

- **Generally Availabile: Automatic zone balance for Virtual Machine Scale Sets**[^5]
    - Automatic zone balance for Virtual Machine Scale Sets is now generally available. This feature continuously monitors scale sets deployed across availability zones and automatically redistributes VM...

- **Generally Available: Azure Cloud HSM hardware audit logging**[^6]
    - Hardware Audit Logging for Azure Cloud HSM provides hardware-generated audit records for supported HSM management operations, helping organizations strengthen security monitoring, compliance report...

- **Generally Available: Azure Site Recovery Support for Azure ARC-enabled Windows VMWare/Physical servers**[^7]
    - Azure Site Recovery (ASR) now supports disaster recovery for Azure ARC-enabled Windows VMWare virtual machines and on-premise physical servers. Customers can protect ARC-managed machines with ASR w...

- **Generally Available: Managed StandardV2 NAT Gateway for AKS**[^8]
    - AKS will now provision and manage a StandardV2 NAT Gateway for clusters using an AKS-managed virtual network.StandardV2 is now the default managed NAT Gateway SKU for new clusters in supported regi...

- **Generally Available: Azure Database for PostgreSQL flexible server in East US 3 **[^9]
    - Now you can deploy Azure Database for PostgreSQL flexible server in the East US 3 Azure region. Learn more.

- **Generally Available: Exceptions in WAF for Azure Application Gateway and Azure Front Door**[^10]
    - Announcing the general availability of exceptions for Web Application Firewall on Azure Application Gateway and Azure Front Door.Azure Web Application Firewall (WAF) helps protect your web applicat...

- **Generally Available: Anyscale on Azure**[^11]
    - Anyscale on Azure is now Generally Available. Anyscale on Azure is a managed platform for running distributed Python workloads on Ray. It deploys directly onto your Azure Kubernetes Service (AKS) c...

- **Generally Available: Enabling the Bulk admin role for SQL Server on Linux**[^12]
    - Starting with SQL Server 2025 CU9 and SQL Server 2022 CU27, SQL Server on Linux supports the bulkadmin fixed server role and the ADMINISTER BULK OPERATIONS permission for performing bulk data impor...

- **Generally Available: SQL Server on Azure Virtual Machines in Azure Bleu **[^13]
    - SQL Server on Azure Virtual Machines is now available in Azure Bleu, enabling you to deploy and manage SQL Server workloads in France's sovereign cloud environment while meeting data residency and ...

- **Generally Available: Storage optimized Lasv5 and Laosv5 Azure VM series **[^14]
    - The Laosv5 series and Lasv5 storage optimized VMs, based on the 5th Gen AMD EPYC™ processor (Turin), are now generally available.Lasv5 and Laosv5 VMs have sizes ranging from 2-160 vCPUs, with 8GiB ...

- **Generally Available: Azure Arc-enabled SQL Server in Germany West Central**[^15]
    - Azure Arc-enabled SQL Server is now available in Germany West Central, enabling you to connect SQL Server instances to Azure Arc and take advantage of Azure-based inventory, governance, security, a...

- **Generally Available: Azure Arc-enabled SQL Server Available in Italy North**[^16]
    - Azure Arc-enabled SQL Server is now available in Italy North, enabling you to connect SQL Server instances to Azure Arc and take advantage of Azure-based inventory, governance, security, assessment...

- **Generally Available: Azure SQL updates for late-September 2026**[^17]
    - The following updates and enhancements were made to Azure SQL: Scale larger workloads on Azure SQL Database Hyperscale Premium series with new 160-vCore and 192-vCore options, delivering up to 50% ...

- **Generally Available: Azure Database for PostgreSQL Flexible Server supports cross-tenant customer-managed keys (CMK) **[^18]
    - Azure Database for PostgreSQL Flexible Server now supports cross-tenant customer-managed keys (CMK). You can encrypt your data using keys stored in an Azure Key Vault or Azure Managed HSM that resi...

## パブリックプレビュー

- **Public Preview: Azure Databricks Private network gateway**[^19]
    - Private network gateway for Azure Databricks is now in Public Preview, enabling serverless compute to connect to resources in your virtual network (VNet) and transitively connected networks through...

- **Public Preview: Azure Files cross-region data copy and synchronization with Azure Storage Mover**[^20]
    - Azure Files customers can now copy and synchronize file share data across storage accounts, Azure regions, and subscriptions within the same tenant using Azure Storage Mover. Schedule incremental t...

- **Public Preview: Microsoft Agent 365 integration with Azure API Management**[^21]
    - The integration between Microsoft Agent 365 and Azure API Management is now available in public preview, helping organizations connect centralized governance with runtime enforcement for MCP server...

- **Public Preview: AKS on bare metal now on Ubuntu**[^22]
    - Running Kubernetes on-premises often means adding a virtualization layer, adapting to unfamiliar infrastructure, or giving up control over the hardware and software your applications depend on. For...

- **Public Preview: Azure HorizonDB expands to additional regions**[^23]
    - Azure HorizonDB is expanding to additional Azure regions, giving you greater flexibility to deploy PostgreSQL workloads closer to your applications and users.With expanded regional availability, yo...

- **Public Preview: Azure Backup for PostgreSQL flexible server and elastic cluster (v2)**[^24]
    - Azure Backup for PostgreSQL flexible server and elastic cluster (v2) preview brings enterprise-grade long-term retention to PostgreSQL. Backups are taken as physical backups from managed disk snaps...

- **Public Preview: IPv6 Support for Application Gateway WAF **[^25]
    - Announcing the Public Preview of IPv6 support for Application Gateway WAF.Application Gateway Web Application Firewall (WAF) now supports inspection and enforcement for IPv6 traffic in Public Previ...

- **Public Preview:  Major version upgrades (MVU) for Azure Database for PostgreSQL elastic clusters **[^26]
    - MVUs are now available for elastic clusters in Azure Database for PostgreSQL. You can upgrade an existing elastic cluster to a supported newer PostgreSQL version in place without provisioning a rep...

- **Public Preview: Reader Endpoint for Azure Database for MySQL **[^27]
    - We’re happy to announce the public preview of reader endpoint support to simplify connection management when using multiple replicas in Azure Database for MySQL - Flexible Server. A reader endpoint...

- **Public Preview: SQL performance monitoring for SQL Server on Azure Virtual Machines **[^28]
    - The public preview of Microsoft-managed performance monitoring for SQL Server on Azure Virtual Machines is now available. You can now monitor SQL Server on Azure Virtual Machines without building c...

- **Public Preview: Ubuntu 26.04 support in AKS**[^29]
    - Teams running Ubuntu node pools on AKS need to stay current with Ubuntu LTS releases, but each OS transition can introduce package footprint, security, and compatibility concerns. Ubuntu 26.04 supp...

- **Public Preview: Automatic Zone Placement for Virtual Machine Scale Sets**[^30]
    - Automatic Zone Placement for VM Scale Sets (Public Preview) enables Azure to automatically select the best availability zones for your scale set based on SKU availability, capacity, and placement r...

- **Public Preview: Azure Database for PostgreSQL Ultra Disk **[^31]
    - Ultra Disk support is now available in public preview for Azure Database for PostgreSQL flexible server. You can use Azure’s highest-performance managed disk option for I/O-intensive and transactio...

- **Public Preview: SQL Performance Monitoring for Azure SQL Database**[^32]
    - The public preview of Microsoft-managed performance monitoring for Azure SQL Database is now available. You can now monitor Azure SQL Database without building custom collection scripts or correlat...

- **Public Preview: Performance monitoring for Azure Arc–enabled SQL Server **[^33]
    - The preview of performance monitoring for SQL Server enabled by Azure Arc is expanding with more flexible ways to explore and visualize your performance data. You can query Microsoft-managed monito...

- **Public preview: Script-based deployment for SQL Server on Linux Azure VM **[^34]
    - A new deployment experience for SQL Server on Linux Azure Virtual Machines (VMs) replaces legacy marketplace images with automated script-based provisioning. This release provides greater flexibili...

## リタイア

- **Retirement: Azure Key Vault Secrets Provider Extension for Azure Arc enabled Kubernetes clusters**[^35]
    - The Azure Key Vault Secrets Provider Extension for Azure Arc-enabled Kubernetes will be retired on October 9, 2027.Customers currently using the extension should plan to migrate to the Azure Key Va...

- **Retirement: Microsoft Dev Box will be retired on September 18, 2028**[^36]
    - Microsoft Dev Box will retire on September 18, 2028. Beginning on September 14, 2026, Microsoft Dev Box will begin the closing-down process. After retirement, Microsoft Dev Box will no longer be av...

- **Retirement: Azure Deployment Environments will be retired on February 22, 2027**[^37]
    - Azure Deployment Environments will retire on February 22, 2027. Beginning on September 14, 2026, Azure Deployment Environments will begin the closing-down process. After retirement, the service wil...

- **Retirement: Pod name dimension in AKS pod platform metrics**[^38]
    - Beginning September 30, 2027, support for the pod name dimension on the following Azure Monitor platform metrics is retiring, and these metrics are transitioning to aggregate pod counters:Number of...

- **Retirement: Azure App Service on Azure Stack Hub**[^39]
    - Azure App Service on Azure Stack Hub will be retired on September 30, 2029. Starting September 30, 2026, new installations will no longer be supported, and no new product releases, features, or enh...

- **Retirement: Support for Java 8, 11 and 17 will end on September 1, 2027**[^40]
    - On September 1, 2027 support for Java 8, 11 and 17 will end. Your apps that are hosted on App Service will continue to run, but security updates will no longer be available, and we’ll no longer pro...

- **Retirement: Always Encrypted with Intel SGX Enclaves**[^41]
    - Always Encrypted with Intel SGX enclaves in Azure SQL Database will retire on October 31, 2027 as support for SGX-enabled DC-series hardware is phased out. Customers should transition to Virtualiza...

- **Retirement: DCsv3 and DCdsv3-series Azure Virtual Machines will be retired on October 31, 2029**[^42]
    - On October 31, 2029, DCsv3 and DCdsv3-series Azure Linux, Windows and Dedicated Host virtual machines will be retired. After that date, they will no longer be available for use or purchase. Before ...

- **Retirement: NVv3-series Azure Virtual Machines**[^43]
    - On September 30, 2026, Microsoft Azure retired the Standard_NV12s_v3, Standard_NV12hs_v3, Standard_NV24s_v3, Standard_NV24ms_v3, Standard_NV32ms_v3, and Standard_NV48s_v3 virtual machines (VMs) in ...

- **Retirement: NVv4-series Azure Virtual Machines**[^44]
    - On September 30, 2026, Microsoft Azure retired the Standard_NV4as_v4, Standard_NV4ahs_v4, Standard_NV8as_v4, Standard_NV8ahs_v4, Standard_NV16as_v4, Standard_NV16ahs_v4, Standard_NV32as_v4, and Sta...

- **Retirement: Dv3, Dsv3, Ev3, and Esv3 Azure VMs **[^45]
    - As part of the Microsoft Azure VM lifecycle policy, Microsoft is announcing the retirement of the Dv3, Dsv3, Ev3, and Esv3 Azure VM series in public cloud Azure regions. These VMs will enter the En...

- **Retirement: Transition to using standard tests for single-step availability testing in Azure Monitor application insights by September 30, 2028**[^46]
    - URL ping tests in Application Insights were originally planned for retirement on September 30, 2026. In response to customer feedback requesting more time to complete migration, the retirement date...

- **Retirement: Functions on Azure Container Apps V1 **[^47]
    - The Functions on Azure Container Apps (ACA) V1 will be retired on September 29, 2027. After this date, existing Functions on ACA V1 Apps will stop running and no longer process requests or event-dr...

## その他

- **Announcing: Multiparty private offers in Microsoft Marketplace expands to Hong Kong**[^48]
    - Multiparty private offers give Microsoft partners a way to procure third-party cloud and AI solutions for customers through Marketplace. Software companies can expand into new markets by working wi...

- **Announcing: Table discovery in OneLake Catalog search**[^49]
    - Starting October 15, 2026, Search in Microsoft Fabric will return tables from semantic models, lakehouses, and mirrored databases as individual results. Users can search by table name or descriptio...

- **Announcing: Azure canvases for GitHub Copilot**[^50]
    - Discover Azure canvases for GitHub Copilot, interactive shared workspaces that bring Azure tools, dashboards, and guided workflows directly alongside your Copilot conversations. Explore Azure resou...

---

[^1]: Generally Available: Metrics usage insights for Azure Monitor workspace, https://azure.microsoft.com/ja-jp/updates/v2/577165/
[^2]: Generally Available: Azure DNS enables DNS-based load balancing through Traffic Manager linked records, https://azure.microsoft.com/ja-jp/updates/v2/573917/
[^3]: Generally Available: External key management for Azure Key Vault Managed HSM, https://azure.microsoft.com/ja-jp/updates/v2/574296/
[^4]: Generally Available: Standard service endpoint , https://azure.microsoft.com/ja-jp/updates/v2/571025/
[^5]: Generally Availabile: Automatic zone balance for Virtual Machine Scale Sets, https://azure.microsoft.com/ja-jp/updates/v2/576334/
[^6]: Generally Available: Azure Cloud HSM hardware audit logging, https://azure.microsoft.com/ja-jp/updates/v2/576377/
[^7]: Generally Available: Azure Site Recovery Support for Azure ARC-enabled Windows VMWare/Physical servers, https://azure.microsoft.com/ja-jp/updates/v2/576214/
[^8]: Generally Available: Managed StandardV2 NAT Gateway for AKS, https://azure.microsoft.com/ja-jp/updates/v2/574430/
[^9]: Generally Available: Azure Database for PostgreSQL flexible server in East US 3 , https://azure.microsoft.com/ja-jp/updates/v2/573691/
[^10]: Generally Available: Exceptions in WAF for Azure Application Gateway and Azure Front Door, https://azure.microsoft.com/ja-jp/updates/v2/574343/
[^11]: Generally Available: Anyscale on Azure, https://azure.microsoft.com/ja-jp/updates/v2/573744/
[^12]: Generally Available: Enabling the Bulk admin role for SQL Server on Linux, https://azure.microsoft.com/ja-jp/updates/v2/573443/
[^13]: Generally Available: SQL Server on Azure Virtual Machines in Azure Bleu , https://azure.microsoft.com/ja-jp/updates/v2/571499/
[^14]: Generally Available: Storage optimized Lasv5 and Laosv5 Azure VM series , https://azure.microsoft.com/ja-jp/updates/v2/572630/
[^15]: Generally Available: Azure Arc-enabled SQL Server in Germany West Central, https://azure.microsoft.com/ja-jp/updates/v2/570696/
[^16]: Generally Available: Azure Arc-enabled SQL Server Available in Italy North, https://azure.microsoft.com/ja-jp/updates/v2/570763/
[^17]: Generally Available: Azure SQL updates for late-September 2026, https://azure.microsoft.com/ja-jp/updates/v2/571643/
[^18]: Generally Available: Azure Database for PostgreSQL Flexible Server supports cross-tenant customer-managed keys (CMK) , https://azure.microsoft.com/ja-jp/updates/v2/571783/
[^19]: Public Preview: Azure Databricks Private network gateway, https://azure.microsoft.com/ja-jp/updates/v2/576556/
[^20]: Public Preview: Azure Files cross-region data copy and synchronization with Azure Storage Mover, https://azure.microsoft.com/ja-jp/updates/v2/576542/
[^21]: Public Preview: Microsoft Agent 365 integration with Azure API Management, https://azure.microsoft.com/ja-jp/updates/v2/574204/
[^22]: Public Preview: AKS on bare metal now on Ubuntu, https://azure.microsoft.com/ja-jp/updates/v2/573782/
[^23]: Public Preview: Azure HorizonDB expands to additional regions, https://azure.microsoft.com/ja-jp/updates/v2/572940/
[^24]: Public Preview: Azure Backup for PostgreSQL flexible server and elastic cluster (v2), https://azure.microsoft.com/ja-jp/updates/v2/573425/
[^25]: Public Preview: IPv6 Support for Application Gateway WAF , https://azure.microsoft.com/ja-jp/updates/v2/573861/
[^26]: Public Preview:  Major version upgrades (MVU) for Azure Database for PostgreSQL elastic clusters , https://azure.microsoft.com/ja-jp/updates/v2/571504/
[^27]: Public Preview: Reader Endpoint for Azure Database for MySQL , https://azure.microsoft.com/ja-jp/updates/v2/569653/
[^28]: Public Preview: SQL performance monitoring for SQL Server on Azure Virtual Machines , https://azure.microsoft.com/ja-jp/updates/v2/571894/
[^29]: Public Preview: Ubuntu 26.04 support in AKS, https://azure.microsoft.com/ja-jp/updates/v2/573214/
[^30]: Public Preview: Automatic Zone Placement for Virtual Machine Scale Sets, https://azure.microsoft.com/ja-jp/updates/v2/571075/
[^31]: Public Preview: Azure Database for PostgreSQL Ultra Disk , https://azure.microsoft.com/ja-jp/updates/v2/571909/
[^32]: Public Preview: SQL Performance Monitoring for Azure SQL Database, https://azure.microsoft.com/ja-jp/updates/v2/571867/
[^33]: Public Preview: Performance monitoring for Azure Arc–enabled SQL Server , https://azure.microsoft.com/ja-jp/updates/v2/571904/
[^34]: Public preview: Script-based deployment for SQL Server on Linux Azure VM , https://azure.microsoft.com/ja-jp/updates/v2/571810/
[^35]: Retirement: Azure Key Vault Secrets Provider Extension for Azure Arc enabled Kubernetes clusters, https://azure.microsoft.com/ja-jp/updates/v2/570313/
[^36]: Retirement: Microsoft Dev Box will be retired on September 18, 2028, https://azure.microsoft.com/ja-jp/updates/v2/567933/
[^37]: Retirement: Azure Deployment Environments will be retired on February 22, 2027, https://azure.microsoft.com/ja-jp/updates/v2/567934/
[^38]: Retirement: Pod name dimension in AKS pod platform metrics, https://azure.microsoft.com/ja-jp/updates/v2/570232/
[^39]: Retirement: Azure App Service on Azure Stack Hub, https://azure.microsoft.com/ja-jp/updates/v2/568178/
[^40]: Retirement: Support for Java 8, 11 and 17 will end on September 1, 2027, https://azure.microsoft.com/ja-jp/updates/v2/568585/
[^41]: Retirement: Always Encrypted with Intel SGX Enclaves, https://azure.microsoft.com/ja-jp/updates/v2/569236/
[^42]: Retirement: DCsv3 and DCdsv3-series Azure Virtual Machines will be retired on October 31, 2029, https://azure.microsoft.com/ja-jp/updates/v2/569592/
[^43]: Retirement: NVv3-series Azure Virtual Machines, https://azure.microsoft.com/ja-jp/updates/v2/573414/
[^44]: Retirement: NVv4-series Azure Virtual Machines, https://azure.microsoft.com/ja-jp/updates/v2/573415/
[^45]: Retirement: Dv3, Dsv3, Ev3, and Esv3 Azure VMs , https://azure.microsoft.com/ja-jp/updates/v2/572346/
[^46]: Retirement: Transition to using standard tests for single-step availability testing in Azure Monitor application insights by September 30, 2028, https://azure.microsoft.com/ja-jp/updates/v2/transition-to-using-standard-tests-for-singlestep-availability-testing-in-azure-monitor-application-insights-by-30-september/
[^47]: Retirement: Functions on Azure Container Apps V1 , https://azure.microsoft.com/ja-jp/updates/v2/570800/
[^48]: Announcing: Multiparty private offers in Microsoft Marketplace expands to Hong Kong, https://azure.microsoft.com/ja-jp/updates/v2/571831/
[^49]: Announcing: Table discovery in OneLake Catalog search, https://azure.microsoft.com/ja-jp/updates/v2/573875/
[^50]: Announcing: Azure canvases for GitHub Copilot, https://azure.microsoft.com/ja-jp/updates/v2/573385/
