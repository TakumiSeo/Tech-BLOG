Title: Azure Update (2026/09/29 - 2026/10/23)
Date: 2026-10-25
Slug: azure-update-2026-10-25
Lang: ja-jp
Category: notebook
Tags: api-management, app-service, application-gateway, application-insights, azure-backup, azure-blob-storage, azure-container-apps, azure-copilot, azure-cosmos-db, azure-data-lake-storage, azure-database-for-mysql, azure-database-for-postgresql, azure-databricks, azure-deployment-environments, azure-dns, azure-files, azure-front-door, azure-horizondb, azure-kubernetes-service, azure-monitor, azure-nat-gateway, azure-private-link, azure-site-recovery, azure-sql-database, azure-stack-hub, azure-update, key-vault, linux-virtual-machines, microsoft-dev-box, microsoft-entra-id, microsoft-fabric, sql-server-on-azure-virtual-machines, traffic-manager, virtual-machines, virtual-network, web-application-firewall, windows-virtual-machines
Summary: 2026年09月29日〜2026年10月23日の Azure Update まとめ。GA 20件、パブリックプレビュー 13件、リタイア 13件、その他 4件の計50件。

## 一般提供 (GA)

### Generally Available: Storage optimized Lasv5 and Laosv5 Azure VM series [^1]

- **対象サービス**: Virtual Machines
- **更新日**: 2026-09-29

The Laosv5 series and Lasv5 storage optimized VMs, based on the 5th Gen AMD EPYC™ processor (Turin), are now generally available.Lasv5 and Laosv5 VMs have sizes ranging from 2-160 vCPUs, with 8GiB of memory and 720GB of local NVMe disk capacity per vCPU.  Both support 200Gbps of network bandwidth and deliver up to 35% better average CPU performance. The Lasv5 VMs offer up to 30.7TB of local storage capacity with 9.6M read IOPS performance, while the Laosv5 VMs offer up to 138TB of local stora...

### Generally Available: SQL Server on Azure Virtual Machines in Azure Bleu [^2]

- **対象サービス**: SQL Server on Azure Virtual Machines
- **更新日**: 2026-10-05

SQL Server on Azure Virtual Machines is now available in Azure Bleu, enabling you to deploy and manage SQL Server workloads in France's sovereign cloud environment while meeting data residency and sovereignty requirements.  Learn more.

### Generally Available: Enabling the Bulk admin role for SQL Server on Linux[^3]

- **対象サービス**: 
- **更新日**: 2026-10-07

Starting with SQL Server 2025 CU9 and SQL Server 2022 CU27, SQL Server on Linux supports the bulkadmin fixed server role and the ADMINISTER BULK OPERATIONS permission for performing bulk data import operations without requiring users to be members of the sysadmin fixed server role. 

This capability enables you to use operations such as BULK INSERT and OPENROWSET(BULK...) while following a least-privilege security model. Previously on SQL Server on Linux, these operations required sysadmin me...

### Generally Available: Anyscale on Azure[^4]

- **対象サービス**: Azure Kubernetes Service (AKS)
- **更新日**: 2026-10-07

Anyscale on Azure is now Generally Available. Anyscale on Azure is a managed platform for running distributed Python workloads on Ray. It deploys directly onto your Azure Kubernetes Service (AKS) cluster and integrates with the Azure services your team already uses. Unlike other processing engines which either only support one hardware type (e.g. CPUs) or focus on a single workload (e.g. inference), Ray turns a heterogeneous cluster of CPUs and GPUs into a single Python runtime composing data...

### Generally Available: Exceptions in WAF for Azure Application Gateway and Azure Front Door[^5]

- **対象サービス**: Application Gateway, Azure Front Door, Web Application Firewall
- **更新日**: 2026-10-08

Announcing the general availability of exceptions
for Web Application Firewall on Azure Application Gateway and Azure Front Door.Azure Web
Application Firewall (WAF) helps protect your web applications from common
threats and attacks. In some cases, WAF may block requests that are safe and
expected for your application. Existing exclusions help reduce false positives
by omitting specific request attributes, such as headers, cookies, query string
arguments, or body fields, from WAF evaluation ...

### Generally Available: Azure Database for PostgreSQL flexible server in East US 3 [^6]

- **対象サービス**: Azure Database for PostgreSQL
- **更新日**: 2026-10-08

Now you can deploy Azure Database for PostgreSQL flexible server in the East US 3 Azure region.  Learn more.

### Generally Available: Managed StandardV2 NAT Gateway for AKS[^7]

- **対象サービス**: Azure Kubernetes Service (AKS), Azure NAT Gateway
- **更新日**: 2026-10-08

AKS will now provision and manage a StandardV2 NAT Gateway
for clusters using an AKS-managed virtual network.StandardV2 is now the default managed NAT Gateway SKU for
new clusters in supported regions when using the managedNATGateway outbound
type. StandardV2 NAT Gateway provides zone redundancy by default, higher
bandwidth and throughput, and IPv6 support.Existing AKS clusters can migrate from a managed Standard
NAT Gateway or load balancer to a managed StandardV2 NAT Gateway.Learn more.

### Generally Available: Azure Site Recovery Support for Azure ARC-enabled Windows VMWare/Physical servers[^8]

- **対象サービス**: Azure Site Recovery
- **更新日**: 2026-10-14

Azure Site Recovery (ASR) now supports disaster recovery for Azure ARC-enabled Windows VMWare virtual machines and on-premise physical servers. Customers can protect ARC-managed machines with ASR while continuing to use Azure ARC for governance, inventory, monitoring and management capabilities. 

Learn more.

### Generally Available: Azure Cloud HSM hardware audit logging[^9]

- **対象サービス**: 
- **更新日**: 2026-10-14

Hardware Audit Logging for Azure Cloud HSM provides hardware-generated audit records for supported HSM management operations, helping organizations strengthen security monitoring, compliance reporting, governance, and forensic investigations. Customers can access human-readable records alongside HSM-signed binary audit data, signatures, and certificates to independently verify the authenticity and integrity of signed audit batches. Audit events are delivered to Azure Monitor Log Analytics for...

### Generally Availabile: Automatic zone balance for Virtual Machine Scale Sets[^10]

- **対象サービス**: 
- **更新日**: 2026-10-15

Automatic zone balance for Virtual Machine Scale Sets is now generally available. This feature continuously monitors scale sets deployed across availability zones and automatically redistributes VM instances when zonal imbalances occur. This helps reduce the risk that a single-zone outage disproportionately affects an application.

Automatic zone balance uses a create-before-delete approach: Azure creates a replacement VM in an under-provisioned zone and validates its health before removing a...

### Generally Available: Standard service endpoint [^11]

- **対象サービス**: Azure Private Link
- **更新日**: 2026-10-15

Standard service endpoint, a
new capability in the Azure Private Link family, provides a scalable and secure
approach for connecting Azure IaaS workloads to Azure PaaS services. Standard service
endpoint addresses the manageability, and the scale limitations of traditional
service endpoints by using Public IP addresses as network identifiers and
integrating with network security perimeter. This enables organizations to
achieve large-scale IaaS-to-PaaS connectivity while maintaining strong net...

### Generally Available: External key management for Azure Key Vault Managed HSM[^12]

- **対象サービス**: Key Vault
- **更新日**: 2026-10-16

External key management for Azure Key Vault Managed HSM is now generally available in all Azure public regions. For organizations with regulatory or sovereignty requirements to retain physical control of key-encryption keys, it lets Azure services that support customer-managed keys with Managed HSM use keys held in a customer-operated hardware security module (HSM) outside Microsoft infrastructure. Managed HSM delegates key wrap and unwrap operations through a customer-operated proxy; the ext...

### Generally Available: Azure DNS enables DNS-based load balancing through Traffic Manager linked records[^13]

- **対象サービス**: Azure DNS, Traffic Manager
- **更新日**: 2026-10-19

Azure DNS now provides DNS based load balancing by seamless
integration with Azure Traffic Manager. Customers can directly associate an
Azure DNS record set with a Traffic Manager profile, eliminating the need to
create a CNAME record pointing to the trafficmanager.net domain. This integration reduces DNS lookup latency by removing the
additional CNAME lookup and enables DNSSEC compatibility for load-balanced
records by removing the unsigned trafficmanager.net domain from the DNS
resolution c...

### Generally Available: Metrics usage insights for Azure Monitor workspace[^14]

- **対象サービス**: Azure Monitor
- **更新日**: 2026-10-19

Metrics usage insights is now generally available, giving you greater visibility into what’s driving metrics usage across your Azure Monitor workspace. Monitor workspace utilization, identify unused metrics, understand usage trends, and investigate changes in ingestion volume to help optimize costs and plan capacity.

Learn more.

### Generally Available: Advanced platform metrics for Azure Monitor[^15]

- **対象サービス**: Azure Monitor
- **更新日**: 2026-10-20

Advanced platform metrics for Azure Monitor are now generally available. Advanced platform metrics provide finer-grained signals that help customers more quickly and accurately identify changes and trends within their resources.With this release, customers can enable advanced platform metrics directly from the Azure portal, with an in-product banner prompting enablement for subscriptions where the feature is not yet enabled. Advanced platform metrics are also now available in Fairfax and Moon...

### Generally Available: Keyless TLS on Application Gateway with Azure Key Vault Managed HSM[^16]

- **対象サービス**: Application Gateway
- **更新日**: 2026-10-20

Azure Application Gateway now supports keyless TLS
termination using certificates whose private keys stay in Azure Key Vault
Managed HSM. Each TLS handshake signature is performed inside the HSM, and the
private key is never exported to the gateway. This integration helps you: 
 Maintain
     private key custody within a dedicated HSM boundary. 
 Use
     managed identities and role-based access control for key access. 
 Monitor
     signing operations through Managed HSM diagnostic logs. 
 O...

### Generally Available: Service tag match condition for Azure Front Door Premium WAF[^17]

- **対象サービス**: Azure Front Door, Web Application Firewall
- **更新日**: 2026-10-20

Announcing the general availability of the service tag match
condition for Azure Web Application Firewall (WAF) custom rules on Azure Front
Door Premium. Service tags represent groups of IP address prefixes used by
Azure services, and Microsoft updates them automatically as addresses change.
Custom rules can now match a HTTP request's source IP address against service
tags, so you can control traffic from Azure services without building and
maintaining lists of IPs.  With service tag matching...

### Generally Available: Azure Cosmos DB Safe Key Rotation[^18]

- **対象サービス**: Azure Cosmos DB
- **更新日**: 2026-10-21

Safe Key Rotation for Azure Cosmos DB is now generally available. You can view timestamp metadata showing when each account key was last used, helping you identify active keys before rotating or retiring credentials.This visibility helps reduce the risk of service disruptions caused by disabling keys that are still in use. It also gives you actionable insights to improve credential management, maintain application continuity, and support modern security and compliance practices.Learn
more.

### Generally Available: ABFS Vectored Read for Azure Data Lake Storage[^19]

- **対象サービス**: Azure Blob Storage, Azure Data Lake Storage
- **更新日**: 2026-10-22

ABFS Vectored Read helps compatible analytics engines reduce request overhead for selective reads in Azure Data Lake Storage. By combining nearby file ranges into fewer storage requests and executing reads asynchronously, it can reduce network round trips for workloads such as selective Parquet queries.Compatible Spark workloads can enable the capability through configuration, without rewriting queries or migrating data.Learn
more.

### Generally Available: Item Level Recovery for Azure VMs with Premium SSDv2 and Ultra Disks in Azure Backup[^20]

- **対象サービス**: Azure Backup
- **更新日**: 2026-10-23

Azure Backup now supports Item-Level Recovery (ILR) for Azure virtual machines using Premium SSD v2 and Ultra disks with both 512 byte and 4KB logical sector sizes. You can now recover individual files and folders from your Azure VMs with Premium SSDv2 and Ultra disks. 

You can generate a file-recovery executable or script through the Azure portal, CLI, or PowerShell, then run it on a compatible machine to access the recovery point, selectively browse, and copy individual files or folders wi...

## パブリックプレビュー

### Public Preview: Automatic Zone Placement for Virtual Machine Scale Sets[^21]

- **対象サービス**: Virtual Machines
- **更新日**: 2026-09-29

Automatic Zone Placement for VM Scale Sets (Public Preview) enables Azure to automatically select the best availability zones for your scale set based on SKU availability, capacity, and placement requirements. Instead of manually maintaining zone lists for each region, customers can use a consistent configuration across regions while Azure handles zone selection.Key benefits include:Simplified multi-region deployments with no region-specific zone management.Capacity-aware zone selection to im...

### Public Preview: Ubuntu 26.04 support in AKS[^22]

- **対象サービス**: Azure Kubernetes Service (AKS)
- **更新日**: 2026-09-30

Teams running Ubuntu node pools on AKS need to stay current with Ubuntu LTS releases, but each OS transition can introduce package footprint, security, and compatibility concerns. Ubuntu 26.04 support introduces the Ubuntu2604 OS SKU using Ubuntu Minimal as the baseline image, while preserving existing AKS create, update, and node pool workflows. You get a smaller default host footprint, Linux LTS kernel 7.0, and a controlled migration path with rollback flexibility to Ubuntu 24.04 where supp...

### Public Preview: SQL performance monitoring for SQL Server on Azure Virtual Machines [^23]

- **対象サービス**: SQL Server on Azure Virtual Machines
- **更新日**: 2026-09-30

The public preview of Microsoft-managed performance monitoring for SQL Server on Azure Virtual Machines is now available. You can now monitor SQL Server on Azure Virtual Machines without building custom collection scripts or correlating telemetry across disconnected tools. The SQL IaaS Agent extension collects performance data from your SQL Server instances and sends it to a Microsoft-managed telemetry pipeline for processing and storage. Resource-level and estate-wide dashboards help you ide...

### Public Preview: Reader Endpoint for Azure Database for MySQL [^24]

- **対象サービス**: Azure Database for MySQL
- **更新日**: 2026-10-01

We’re happy to announce the public preview of reader endpoint support to simplify connection management when using multiple replicas in Azure Database for MySQL - Flexible Server. A reader endpoint enables automatic load balancing of read-only connection traffic across multiple replicas. It simplifies application architecture by giving you a single endpoint for read operations, enhancing both scalability and fault tolerance.Azure Database for MySQL supports up to 10 read replicas per primary ...

### Public Preview:  Major version upgrades (MVU) for Azure Database for PostgreSQL elastic clusters [^25]

- **対象サービス**: Azure Database for PostgreSQL
- **更新日**: 2026-10-02

MVUs are now available for elastic clusters in Azure Database for PostgreSQL. You can upgrade an existing elastic cluster to a supported newer PostgreSQL version in place without provisioning a replacement cluster, migrating distributed data, or changing your application connection endpoint. This managed upgrade experience helps reduce the downtime, complexity, and operational effort associated with traditional migration-based upgrades. You can use MVUs to keep distributed PostgreSQL workload...

### Public Preview: IPv6 Support for Application Gateway WAF [^26]

- **対象サービス**: Application Gateway, Web Application Firewall
- **更新日**: 2026-10-05

Announcing the Public Preview of IPv6 support for Application Gateway WAF.Application Gateway Web Application Firewall (WAF) now supports inspection and enforcement for IPv6 traffic in Public Preview, marking a major step forward in modernizing the platform for dual‑stack environments. As IPv6 adoption accelerates globally due to IPv4 exhaustion and modern connectivity requirements, this enhancement enables customers to embrace IPv6 without compromising their security posture.With this update...

### Public Preview: Azure Backup for PostgreSQL flexible server and elastic cluster (v2)[^27]

- **対象サービス**: Azure Backup, Azure Database for PostgreSQL
- **更新日**: 2026-10-05

Azure Backup for PostgreSQL flexible server and elastic cluster (v2) preview brings enterprise-grade long-term retention to PostgreSQL. Backups are taken as physical backups from managed disk snapshots and vaulted in an Azure Backup vault, so protection now extends to servers of up to 32 TB on Premium SSD v1 and up to 64 TB on Premium SSD v2. The first backup is full and every backup after it is incremental, which keeps daily protection practical at multi-terabyte scale, with a recovery point...

### Public Preview: Azure HorizonDB expands to additional regions[^28]

- **対象サービス**: Azure HorizonDB
- **更新日**: 2026-10-05

Azure HorizonDB is expanding to additional Azure regions, giving you greater flexibility to deploy PostgreSQL workloads closer to your applications and users.

With expanded regional availability, you have more options when choosing where to deploy Azure HorizonDB based on your workload needs.

Learn
more.

### Public Preview: AKS on bare metal now on Ubuntu[^29]

- **対象サービス**: 
- **更新日**: 2026-10-06

Running Kubernetes on-premises often means adding a
virtualization layer, adapting to unfamiliar infrastructure, or giving up
control over the hardware and software your applications depend on. For AI
workloads, these tradeoffs can limit access to local data, reduce available
compute capacity, and restrict your choice of GPUs, drivers, and runtimes.AKS on bare metal
Ubuntu, now in public preview, brings the AKS experience directly to customer
owned Ubuntu infrastructure. Deploy a complete Kub...

### Public Preview: Microsoft Agent 365 integration with Azure API Management[^30]

- **対象サービス**: API Management
- **更新日**: 2026-10-08

The integration between Microsoft Agent 365 and Azure API Management is now available in public preview, helping organizations connect centralized governance with runtime enforcement for MCP servers and tools.With this integration, organizations can:Discover Azure API Management gateways and MCP servers in Agent 365, creating a centralized inventory of gateway-managed tools.Control access to MCP servers from Agent 365, with enforcement applied by Azure API Management at runtime.Apply tool-lev...

### Public Preview: Azure Files cross-region data copy and synchronization with Azure Storage Mover[^31]

- **対象サービス**: Azure Files
- **更新日**: 2026-10-15

Azure Files customers can now copy and synchronize file share data across storage accounts, Azure regions, and subscriptions within the same tenant using Azure Storage Mover. Schedule incremental transfers to maintain secondary copies that can support business continuity scenarios, copy data across regions, consolidate file shares, or place data closer to applications and analytics workloads. Centralized scheduling, monitoring, auditing, and metadata preservation provide a managed approach to...

### Public Preview: Azure Databricks Private network gateway[^32]

- **対象サービス**: Azure Databricks
- **更新日**: 2026-10-16

Private network gateway for Azure Databricks is
now in Public Preview, enabling serverless compute to connect to resources in
your virtual network (VNet) and transitively connected networks through a
single managed gateway. Customers can use the gateway to access multiple
private resources, route serverless egress through their own firewalls or
network security appliances, and use stable, identifiable source IP addresses. This simplifies secure connectivity for
serverless workloads while givi...

### Public Preview: Disable VNet peering route[^33]

- **対象サービス**: Virtual Network
- **更新日**: 2026-10-20

Announcing
the public preview of disable VNet peering route, a route-table capability that
gives you more control over traffic between peered virtual networks. DPR
suppresses system-generated peering routes on subnets associated with the route
table while preserving the peering connection itself.     In
large hub-and-spoke networks, you can pair this feature with a summarized
user-defined route to direct traffic through a network virtual appliance, such
as Azure Firewall, instead of maintaini...

## リタイア

### Retirement: Functions on Azure Container Apps V1 [^34]

- **対象サービス**: Azure Container Apps
- **更新日**: 2026-09-29

The Functions on Azure Container Apps (ACA) V1 will be retired on September 29, 2027. After this date, existing Functions on ACA V1 Apps will stop running and no longer process
requests or event-driven triggers. Action required Review your Azure environments and migrate all affected apps
to the Functions on Azure Container Apps(ACA) V2 hosting model before September 29, 2027 to avoid service
disruption. Functions on ACA V2 uses a native Azure Container App configured
with `kind=functionapp`. ...

### Retirement: Transition to using standard tests for single-step availability testing in Azure Monitor application insights by September 30, 2028[^35]

- **対象サービス**: Application Insights, Azure Monitor
- **更新日**: 2026-09-30

URL ping tests in Application Insights were originally planned for retirement on September 30, 2026. In response to customer feedback requesting more time to complete migration, the retirement date has been extended by 24 months to September 30, 2028. On September 30, 2028, existing URL ping tests are removed from your resources. Review the pricing for standard tests and transition to using them before September 30, 2028, to ensure you can continue to run single-step availability tests in you...

### Retirement: Dv3, Dsv3, Ev3, and Esv3 Azure VMs [^36]

- **対象サービス**: Virtual Machines
- **更新日**: 2026-09-30

As part of the Microsoft Azure VM lifecycle
policy, Microsoft is announcing the retirement of the Dv3, Dsv3, Ev3, and
Esv3 Azure VM series in public cloud Azure regions. These VMs will enter the
End-of-Life lifecycle stage and retire on November 15, 2029. We know migrating production workloads takes planning and
engineering time. To keep your applications and workloads running without
interruption, migrate any Dv3, Dsv3, Ev3, or Esv3 series VMs to a newer VM
series before November 15, 2029. A...

### Retirement: NVv4-series Azure Virtual Machines[^37]

- **対象サービス**: Virtual Machines
- **更新日**: 2026-09-30

On September 30, 2026, Microsoft Azure retired the Standard_NV4as_v4, Standard_NV4ahs_v4, Standard_NV8as_v4, Standard_NV8ahs_v4, Standard_NV16as_v4, Standard_NV16ahs_v4, Standard_NV32as_v4, and Standard_NV32ahs_v4 virtual machines (VMs) in the NVv4-series VMs. Any remaining NVv4-series VMs will be set to a deallocated state. They'll stop working and no longer incur billing charges. NVv4 will no longer be under SLA or have support included. Note: 1-year and 3-year Reserved Instance (RI) purcha...

### Retirement: NVv3-series Azure Virtual Machines[^38]

- **対象サービス**: Virtual Machines
- **更新日**: 2026-09-30

On September 30, 2026, Microsoft Azure retired the Standard_NV12s_v3, Standard_NV12hs_v3, Standard_NV24s_v3, Standard_NV24ms_v3, Standard_NV32ms_v3, and Standard_NV48s_v3 virtual machines (VMs) in the NVv3-series VMs.Any remaining NVv3-series VMs will be set to a deallocated state. They'll stop working and no longer incur billing charges. NVv3 will no longer be under SLA or have support included. Note: 1-year and 3-year Reserved Instance (RI) purchases for the NVv3-series ended on November 2,...

### Retirement: DCsv3 and DCdsv3-series Azure Virtual Machines will be retired on October 31, 2029[^39]

- **対象サービス**: Linux Virtual Machines, Virtual Machines, Windows Virtual Machines
- **更新日**: 2026-10-01

On October 31, 2029, DCsv3 and DCdsv3-series
Azure Linux, Windows and Dedicated Host virtual
machines will be retired. After that date, they will no longer be
available for use or purchase.  Before October 31, 2029, migrate your workloads to one of
the following options that best aligns with your business needs:  
 To use
     a VM-based programming model consider DCasv6/DCadsv6/DCesv6/DCedsv6
     or memory optimized ECasv6/ECadsv6/ECesv6/ECedsv6 
     series confidential VMs (CVMs),   
 For...

### Retirement: Always Encrypted with Intel SGX Enclaves[^40]

- **対象サービス**: Azure SQL Database
- **更新日**: 2026-10-06

Always Encrypted with Intel SGX enclaves in Azure SQL Database will retire on October 31, 2027 as support for SGX-enabled DC-series hardware is phased out. Customers should transition to Virtualization-Based Security (VBS) enclaves, a hardware-independent alternative, or consider SQL Server on Confidential VMs.Customer impactAfter retirement, workloads using Intel SGX enclaves will no longer have enclave functionality. Databases running on DC-series compute tiers should be migrated to support...

### Retirement: Support for Java 8, 11 and 17 will end on September 1, 2027[^41]

- **対象サービス**: App Service
- **更新日**: 2026-10-06

On September 1, 2027 support for Java 8, 11 and 17 will end. Your
apps that are hosted on App Service will continue to run, but security updates
will no longer be available, and we’ll no longer provide customer service for Java
8, 11 and 17.Required action  To avoid potential security vulnerabilities and
minimize risk for your App Service apps, follow the steps to upgrade your app to
Java 25 before September 1, 2027. 

Learn
more.

### Retirement: Azure App Service on Azure Stack Hub[^42]

- **対象サービス**: App Service, Azure Stack Hub
- **更新日**: 2026-10-06

Azure App Service on Azure Stack Hub will be retired on September
30, 2029. Starting September 30, 2026, new installations will
no longer be supported, and no new product releases, features, or enhancements
will be made available. Existing supported deployments can continue to run and
upgrade to the latest available release until retirement. Customers should begin planning migration to Azure App
Service in Azure now to continue receiving support, security updates, platform improvements,
and n...

### Retirement: Pod name dimension in AKS pod platform metrics[^43]

- **対象サービス**: Azure Kubernetes Service (AKS)
- **更新日**: 2026-10-06

Beginning September 30, 2027, support for the pod name dimension on the following Azure
Monitor platform metrics is retiring, and these metrics are transitioning to aggregate pod counters:
Number of pods by phase (kube_pod_status_phase)Number of pods in Ready state (kube_pod_status_ready)After this change:Metric names remain unchanged.Aggregate pod counts remain available.Namespace-level monitoring scenarios remain supported.The pod name dimension will no longer be available for filtering, gr...

### Retirement: Azure Deployment Environments will be retired on February 22, 2027[^44]

- **対象サービス**: Azure Deployment Environments
- **更新日**: 2026-10-08

Azure Deployment
Environments will retire on February 22, 2027. Beginning on September
14, 2026, Azure Deployment Environments will begin the closing-down
process. After retirement, the service will no longer be available. To help avoid disruption, we recommend that you begin
assessing your current usage and planning your transition now. Review the
environments, templates, and workflows in your organization that depend on
Azure Deployment Environments and identify the replacement approach tha...

### Retirement: Microsoft Dev Box will be retired on September 18, 2028[^45]

- **対象サービス**: Microsoft Dev Box
- **更新日**: 2026-10-08

Microsoft Dev Box will
retire on September 18, 2028. Beginning on September 14, 2026,
Microsoft Dev Box will begin the closing-down process. After retirement,
Microsoft Dev Box will no longer be available. Microsoft Dev Box is currently in maintenance mode, and
Microsoft’s investments for developer cloud environments are focused on Windows
365. Existing Microsoft Dev Box usage remains supported during the transition
period, and we recommend that you begin planning your migration now to avoid
...

### Retirement: Azure Key Vault Secrets Provider Extension for Azure Arc enabled Kubernetes clusters[^46]

- **対象サービス**: 
- **更新日**: 2026-10-09

The Azure Key Vault Secrets Provider Extension for Azure Arc-enabled Kubernetes will be retired on October 9, 2027.

Customers currently using the extension should plan to migrate to the Azure Key Vault Secret Store Extension before the retirement date. The Azure Key Vault Secret Store Extension provides equivalent functionality for accessing and synchronizing secrets from Azure Key Vault for workloads running on Azure Arc-enabled Kubernetes clusters. In addition, the Azure Key Vault Secret S...

## その他

### Announcing: Azure canvases for GitHub Copilot[^47]

- **対象サービス**: Azure Copilot
- **更新日**: 2026-09-30

Discover Azure canvases for GitHub Copilot, interactive shared workspaces that bring Azure tools, dashboards, and guided workflows directly alongside your Copilot conversations. Explore Azure resources, analyze costs, and build hosted skills while keeping progress, controls, and next steps visible and actionable in one workspace.Learn more.

### Announcing: Table discovery in OneLake Catalog search[^48]

- **対象サービス**: Microsoft Fabric
- **更新日**: 2026-10-05

Starting October 15, 2026, Search in Microsoft Fabric will return tables from semantic models, lakehouses, and mirrored databases as individual results. Users can search by table name or description, or find a table by an exact column-name match.  More object types will become available over time. This applies to Fabric's global search, the OneLake Catalog UI, the Search API, search in Fabric's MCP servers, the /find command in the Fabric CLI, and the discovery skill.

What you need to know: ...

### Announcing: Multiparty private offers in Microsoft Marketplace expands to Hong Kong[^49]

- **対象サービス**: 
- **更新日**: 2026-10-08

Multiparty private offers give Microsoft partners a way to procure third-party cloud and AI solutions for customers through Marketplace. Software companies can expand into new markets by working with partners that bring established customer relationships, while customers rely on their trusted partners to manage their cloud and AI initiatives.

### Announcing: Choose Your Own Telephony (CYOT) for Microsoft Entra[^50]

- **対象サービス**: Microsoft Entra ID (formerly Azure AD)
- **更新日**: 2026-10-21

What and whyStarting October 30, 2026, Microsoft Entra ID will make the Choose Your Own Telephony Provider experience available. This feature enables organizations to use a supported third-party telecommunications provider for SMS and voice authentication. Organizations select a supported provider through Microsoft Security Store and manage their commercial relationship directly with the provider.Microsoft recommends phishing-resistant authentication methods, such as passkeys, instead of SMS ...

---

[^1]: Generally Available: Storage optimized Lasv5 and Laosv5 Azure VM series , https://azure.microsoft.com/ja-jp/updates/v2/?id=572630

[^2]: Generally Available: SQL Server on Azure Virtual Machines in Azure Bleu , https://azure.microsoft.com/ja-jp/updates/v2/?id=571499

[^3]: Generally Available: Enabling the Bulk admin role for SQL Server on Linux, https://azure.microsoft.com/ja-jp/updates/v2/?id=573443

[^4]: Generally Available: Anyscale on Azure, https://azure.microsoft.com/ja-jp/updates/v2/?id=573744

[^5]: Generally Available: Exceptions in WAF for Azure Application Gateway and Azure Front Door, https://azure.microsoft.com/ja-jp/updates/v2/?id=574343

[^6]: Generally Available: Azure Database for PostgreSQL flexible server in East US 3 , https://azure.microsoft.com/ja-jp/updates/v2/?id=573691

[^7]: Generally Available: Managed StandardV2 NAT Gateway for AKS, https://azure.microsoft.com/ja-jp/updates/v2/?id=574430

[^8]: Generally Available: Azure Site Recovery Support for Azure ARC-enabled Windows VMWare/Physical servers, https://azure.microsoft.com/ja-jp/updates/v2/?id=576214

[^9]: Generally Available: Azure Cloud HSM hardware audit logging, https://azure.microsoft.com/ja-jp/updates/v2/?id=576377

[^10]: Generally Availabile: Automatic zone balance for Virtual Machine Scale Sets, https://azure.microsoft.com/ja-jp/updates/v2/?id=576334

[^11]: Generally Available: Standard service endpoint , https://azure.microsoft.com/ja-jp/updates/v2/?id=571025

[^12]: Generally Available: External key management for Azure Key Vault Managed HSM, https://azure.microsoft.com/ja-jp/updates/v2/?id=574296

[^13]: Generally Available: Azure DNS enables DNS-based load balancing through Traffic Manager linked records, https://azure.microsoft.com/ja-jp/updates/v2/?id=573917

[^14]: Generally Available: Metrics usage insights for Azure Monitor workspace, https://azure.microsoft.com/ja-jp/updates/v2/?id=577165

[^15]: Generally Available: Advanced platform metrics for Azure Monitor, https://azure.microsoft.com/ja-jp/updates/v2/?id=575329

[^16]: Generally Available: Keyless TLS on Application Gateway with Azure Key Vault Managed HSM, https://azure.microsoft.com/ja-jp/updates/v2/?id=577130

[^17]: Generally Available: Service tag match condition for Azure Front Door Premium WAF, https://azure.microsoft.com/ja-jp/updates/v2/?id=577156

[^18]: Generally Available: Azure Cosmos DB Safe Key Rotation, https://azure.microsoft.com/ja-jp/updates/v2/?id=576716

[^19]: Generally Available: ABFS Vectored Read for Azure Data Lake Storage, https://azure.microsoft.com/ja-jp/updates/v2/?id=577618

[^20]: Generally Available: Item Level Recovery for Azure VMs with Premium SSDv2 and Ultra Disks in Azure Backup, https://azure.microsoft.com/ja-jp/updates/v2/?id=577963

[^21]: Public Preview: Automatic Zone Placement for Virtual Machine Scale Sets, https://azure.microsoft.com/ja-jp/updates/v2/?id=571075

[^22]: Public Preview: Ubuntu 26.04 support in AKS, https://azure.microsoft.com/ja-jp/updates/v2/?id=573214

[^23]: Public Preview: SQL performance monitoring for SQL Server on Azure Virtual Machines , https://azure.microsoft.com/ja-jp/updates/v2/?id=571894

[^24]: Public Preview: Reader Endpoint for Azure Database for MySQL , https://azure.microsoft.com/ja-jp/updates/v2/?id=569653

[^25]: Public Preview:  Major version upgrades (MVU) for Azure Database for PostgreSQL elastic clusters , https://azure.microsoft.com/ja-jp/updates/v2/?id=571504

[^26]: Public Preview: IPv6 Support for Application Gateway WAF , https://azure.microsoft.com/ja-jp/updates/v2/?id=573861

[^27]: Public Preview: Azure Backup for PostgreSQL flexible server and elastic cluster (v2), https://azure.microsoft.com/ja-jp/updates/v2/?id=573425

[^28]: Public Preview: Azure HorizonDB expands to additional regions, https://azure.microsoft.com/ja-jp/updates/v2/?id=572940

[^29]: Public Preview: AKS on bare metal now on Ubuntu, https://azure.microsoft.com/ja-jp/updates/v2/?id=573782

[^30]: Public Preview: Microsoft Agent 365 integration with Azure API Management, https://azure.microsoft.com/ja-jp/updates/v2/?id=574204

[^31]: Public Preview: Azure Files cross-region data copy and synchronization with Azure Storage Mover, https://azure.microsoft.com/ja-jp/updates/v2/?id=576542

[^32]: Public Preview: Azure Databricks Private network gateway, https://azure.microsoft.com/ja-jp/updates/v2/?id=576556

[^33]: Public Preview: Disable VNet peering route, https://azure.microsoft.com/ja-jp/updates/v2/?id=576242

[^34]: Retirement: Functions on Azure Container Apps V1 , https://azure.microsoft.com/ja-jp/updates/v2/?id=570800

[^35]: Retirement: Transition to using standard tests for single-step availability testing in Azure Monitor application insights by September 30, 2028, https://azure.microsoft.com/ja-jp/updates/v2/?id=transition-to-using-standard-tests-for-singlestep-availability-testing-in-azure-monitor-application-insights-by-30-september

[^36]: Retirement: Dv3, Dsv3, Ev3, and Esv3 Azure VMs , https://azure.microsoft.com/ja-jp/updates/v2/?id=572346

[^37]: Retirement: NVv4-series Azure Virtual Machines, https://azure.microsoft.com/ja-jp/updates/v2/?id=573415

[^38]: Retirement: NVv3-series Azure Virtual Machines, https://azure.microsoft.com/ja-jp/updates/v2/?id=573414

[^39]: Retirement: DCsv3 and DCdsv3-series Azure Virtual Machines will be retired on October 31, 2029, https://azure.microsoft.com/ja-jp/updates/v2/?id=569592

[^40]: Retirement: Always Encrypted with Intel SGX Enclaves, https://azure.microsoft.com/ja-jp/updates/v2/?id=569236

[^41]: Retirement: Support for Java 8, 11 and 17 will end on September 1, 2027, https://azure.microsoft.com/ja-jp/updates/v2/?id=568585

[^42]: Retirement: Azure App Service on Azure Stack Hub, https://azure.microsoft.com/ja-jp/updates/v2/?id=568178

[^43]: Retirement: Pod name dimension in AKS pod platform metrics, https://azure.microsoft.com/ja-jp/updates/v2/?id=570232

[^44]: Retirement: Azure Deployment Environments will be retired on February 22, 2027, https://azure.microsoft.com/ja-jp/updates/v2/?id=567934

[^45]: Retirement: Microsoft Dev Box will be retired on September 18, 2028, https://azure.microsoft.com/ja-jp/updates/v2/?id=567933

[^46]: Retirement: Azure Key Vault Secrets Provider Extension for Azure Arc enabled Kubernetes clusters, https://azure.microsoft.com/ja-jp/updates/v2/?id=570313

[^47]: Announcing: Azure canvases for GitHub Copilot, https://azure.microsoft.com/ja-jp/updates/v2/?id=573385

[^48]: Announcing: Table discovery in OneLake Catalog search, https://azure.microsoft.com/ja-jp/updates/v2/?id=573875

[^49]: Announcing: Multiparty private offers in Microsoft Marketplace expands to Hong Kong, https://azure.microsoft.com/ja-jp/updates/v2/?id=571831

[^50]: Announcing: Choose Your Own Telephony (CYOT) for Microsoft Entra, https://azure.microsoft.com/ja-jp/updates/v2/?id=577273
