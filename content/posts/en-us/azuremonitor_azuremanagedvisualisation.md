Title: Review of AKS Monitoring Architecture Proposals (Azure Monitor / Managed Prometheus / Azure Managed Grafana / New Relic)
Date: 2026-03-05
Slug: azuremonitor_azuremanagedvisualisation
Lang: en-us
Category: notebook
Tags: azure, azure-monitor, aks, prometheus, grafana, new-relic, observability
Summary: Review of customer proposals (Proposal 1-3) from Azure Monitor / Azure Monitor managed service for Prometheus / Azure Managed Grafana / Azure Native New Relic Service perspectives (Microsoft Learn references only).


## 0. Purpose and assumptions

This note reviews three monitoring architecture proposals (Proposal 1-3) shared by the customer, focusing on the **Azure-side** design points:

- Feasibility (whether the connectivity is supported)
- Permissions (RBAC) and networking (Private Link, etc.)
- Data duplication (double ingestion) and cost
- AKS pitfalls around log categories (especially control plane / resource logs)

Constraint: All factual statements are based on **Microsoft Learn**. No vendor-specific docs or external references.

> Note: This is a design review memo. Cost estimates depend on actual ingestion volume (logs, Prometheus samples), query patterns, and retention, so a separate sizing/estimation exercise is required.

---

## 1. First principles: Azure Monitor data types and “what drives cost”

### 1.1 Metrics (platform metrics / Prometheus metrics)

- **Platform metrics**
	- Platform metrics are collected from Azure resources with **no configuration** and **no cost**.
	- Retention is **93 days**.
	- While metrics are stored for 93 days, the Azure portal Metrics chart can query **up to 30 days per chart**.
	- References:
		- https://learn.microsoft.com/azure/azure-monitor/metrics/data-platform-metrics
		- https://learn.microsoft.com/azure/azure-monitor/metrics/data-platform-metrics#retention-of-metrics

- **Prometheus metrics (Azure Monitor managed service for Prometheus)**
	- Prometheus metrics are stored in an **Azure Monitor workspace**.
	- Retention is **up to 18 months** with **no cost for storage**, and pricing is primarily based on **ingestion and query**.
	- A single PromQL query can span **up to 32 days**.
	- References:
		- https://learn.microsoft.com/azure/azure-monitor/essentials/prometheus-metrics-overview


### 1.2 Logs (Azure Monitor Logs / Log Analytics)

- Container insights and AKS control plane/resource logs typically send data to a Log Analytics workspace. The cost grows with log ingestion volume.
- AKS control plane logs are implemented as Azure Monitor **resource logs** and exported via diagnostic settings.
	- Reference: https://learn.microsoft.com/azure/aks/monitor-aks#aks-control-planeresource-logs

---

## 2. Review of Proposal 1-3 (Azure-side discussion points)

This section assumes the connectivity and roles shown in the customer diagram(s) and highlights what is supported and what to watch for.

---

### Proposal 1: Cost Effective Design (New Relic + Azure Monitor + Managed Prometheus + Azure Managed Grafana)

Interpretation of the diagram intent:

- Application/AKS sends telemetry to New Relic via OTEL (APM)
- AKS Prometheus metrics collected by Azure Monitor managed service for Prometheus (stored in Azure Monitor workspace)
- Other Azure resources (Storage/Network, etc.) use Azure Monitor platform metrics
- Visualization via Azure Managed Grafana (queries both Azure Monitor and the Prometheus data in Azure Monitor workspace)

**Feasibility**

- Azure Managed Grafana can visualize Azure Monitor data (Azure Monitor data source) as documented.
	- Reference: https://learn.microsoft.com/azure/azure-monitor/visualize/visualize-use-managed-grafana-how-to

- Prometheus metrics collected by Azure Monitor managed service for Prometheus are stored in Azure Monitor workspace and can be connected to Azure Managed Grafana.
	- References:
		- https://learn.microsoft.com/azure/azure-monitor/essentials/prometheus-metrics-overview
		- https://learn.microsoft.com/azure/managed-grafana/how-to-connect-azure-monitor-workspace

**RBAC (minimum you need to plan for)**

- Azure Managed Grafana needs read permissions (via managed identity or app registration) to query Azure Monitor data.
	- Reference: https://learn.microsoft.com/azure/azure-monitor/visualize/visualize-use-managed-grafana-how-to

- To read Prometheus data from an Azure Monitor workspace, assign **Monitoring Data Reader** on the Azure Monitor workspace to the Azure Managed Grafana managed identity (Standard tier required).
	- Reference: https://learn.microsoft.com/azure/managed-grafana/how-to-connect-azure-monitor-workspace

**Networking (when private connectivity is required)**

- Azure Managed Grafana supports creating **managed private endpoints** to connect to data sources privately.
	- Reference: https://learn.microsoft.com/azure/managed-grafana/how-to-connect-to-data-source-privately

**Cost / duplication risk (common pitfall in this proposal)**

- Microsoft Learn Kubernetes monitoring best practices warn that when using Managed Prometheus, sending Prometheus metrics to Log Analytics can be redundant and increase cost. It also notes you may want to scope Container insights to **Logs and events only** depending on your goals.
	- Reference: https://learn.microsoft.com/azure/azure-monitor/containers/best-practices-containers#cost-optimization

- Platform metrics are “no configuration / no cost” with 93-day retention, while Prometheus metrics are ingestion/query priced with up to 18-month retention.
	- References:
		- https://learn.microsoft.com/azure/azure-monitor/metrics/data-platform-metrics#retention-of-metrics
		- https://learn.microsoft.com/azure/azure-monitor/essentials/prometheus-metrics-overview

**Clarifying the arrows in the diagram**

- Azure Managed Grafana typically **queries and visualizes** data from data sources; it is not primarily a long-term data store.
	- Reference: https://learn.microsoft.com/azure/azure-monitor/visualize/visualize-use-managed-grafana-how-to

---

### Proposal 2: Convenient for Visualization and Troubleshooting (New Relic + Azure Monitor + Azure Managed Grafana, without Managed Prometheus)

Interpretation of the diagram intent:

- Use Azure Monitor as the central place for Azure resource telemetry and visualize in Azure Managed Grafana
- Do not use Prometheus metrics (Managed Prometheus is not enabled)

**Feasibility**

- Using Azure Managed Grafana with Azure Monitor data source is supported.
	- Reference: https://learn.microsoft.com/azure/azure-monitor/visualize/visualize-use-managed-grafana-how-to

**Key caution (AKS monitoring depth)**

- This proposal is simpler to start because it leans on platform metrics, but it makes it harder to leverage Prometheus-based dashboards/queries for deep Kubernetes troubleshooting.
- If deeper AKS visibility is needed, plan for adding Managed Prometheus later (Proposal 1 elements), and pre-align RBAC/network/cost controls to avoid duplicate ingestion.
	- Reference: https://learn.microsoft.com/azure/azure-monitor/essentials/prometheus-metrics-overview

---

### Proposal 3: Forward Azure Monitor logs to New Relic (Azure Native New Relic Service / partner integration)

**Feasibility (Azure-side scope)**

- Azure Monitor diagnostic settings support sending data to **partner solutions** as a destination.
	- Reference: https://learn.microsoft.com/azure/azure-monitor/essentials/diagnostic-settings#destinations

- Microsoft Learn includes troubleshooting guidance for Azure Native New Relic Service, such as verifying whether diagnostic settings are sending logs to New Relic.
	- Reference: https://learn.microsoft.com/azure/partner-solutions/new-relic/troubleshoot#logs-arent-being-sent-to-new-relic

**Important constraints (diagnostic settings / partner integration)**

- Diagnostic settings have a maximum of **five** settings per resource.
- Partner integration limitations include that metrics can be unsupported in some partner-forwarding scenarios (design tends to be log-centric).
	- Reference: https://learn.microsoft.com/troubleshoot/azure/partner-solutions/log-limitations

**Operational cautions (lock / duplicate forwarding / unexpected costs)**

- Learn troubleshooting notes scenarios where diagnostic settings can remain active (e.g., due to locks) even after disabling a New Relic resource, which can keep forwarding (and cost) running.
	- Reference: https://learn.microsoft.com/azure/partner-solutions/new-relic/troubleshoot#diagnostic-settings-are-active-even-after-disabling-the-new-relic-resource-or-applying-necessary-tag-rules

- Learn management guidance also discusses multi-subscription monitoring and warns about duplicate log forwarding if not configured carefully.
	- Reference: https://learn.microsoft.com/azure/partner-solutions/new-relic/manage#monitor-multiple-subscriptions

---

## 3. AKS control plane/resource logs (diagnostic settings): common pitfalls

AKS control plane logs are Azure Monitor **resource logs** exported via diagnostic settings.

- Example categories listed on Learn:
	- `kube-apiserver`
	- `kube-audit`
	- `kube-audit-admin`
	- `kube-controller-manager`
	- `kube-scheduler`
	- `cluster-autoscaler`
	- `guard`
	- Reference: https://learn.microsoft.com/azure/aks/monitor-aks#aks-control-planeresource-logs

- Cost note (especially `kube-audit`)
	- Learn explicitly cautions that `kube-audit` can generate high volume and become costly; use it only when needed and consider `kube-audit-admin` to reduce volume.
	- Reference: https://learn.microsoft.com/azure/aks/monitor-aks#aks-control-planeresource-logs

---

## 4. A ready-to-use response template for the customer (Q1-Q3)

### Q1) Considerations / cautions for each proposal

- Separate your design by data type:
	- Metrics: platform metrics vs Prometheus metrics
	- Logs: Container insights logs/events vs AKS control plane/resource logs
- Align retention and pricing characteristics:
	- Platform metrics: 93-day retention, no configuration, no cost
	- Prometheus metrics: up to 18-month retention, priced by ingestion/query
	- Logs: priced primarily by ingestion volume
	- References:
		- https://learn.microsoft.com/azure/azure-monitor/metrics/data-platform-metrics#retention-of-metrics
		- https://learn.microsoft.com/azure/azure-monitor/essentials/prometheus-metrics-overview

- When using Managed Prometheus, avoid redundant Prometheus-metrics ingestion into Log Analytics unless you have an explicit reason.
	- Reference: https://learn.microsoft.com/azure/azure-monitor/containers/best-practices-containers#cost-optimization

### Q2) Connectivity cautions (Azure Monitor ↔ Azure Managed Grafana / Managed Prometheus ↔ Azure Managed Grafana)

- Azure Managed Grafana typically queries data sources for visualization; ensure:
	- RBAC: assign the required built-in roles (e.g., Monitoring Data Reader for Azure Monitor workspace)
	- Network: use managed private endpoints when private connectivity is required
	- References:
		- https://learn.microsoft.com/azure/azure-monitor/visualize/visualize-use-managed-grafana-how-to
		- https://learn.microsoft.com/azure/managed-grafana/how-to-connect-azure-monitor-workspace
		- https://learn.microsoft.com/azure/managed-grafana/how-to-connect-to-data-source-privately

### Q3) Microsoft Learn references to share

- AKS monitoring (includes control plane/resource logs)
	- https://learn.microsoft.com/azure/aks/monitor-aks
- Kubernetes monitoring best practices (cost optimization / duplication avoidance)
	- https://learn.microsoft.com/azure/azure-monitor/containers/best-practices-containers
- Azure Monitor managed service for Prometheus (overview)
	- https://learn.microsoft.com/azure/azure-monitor/essentials/prometheus-metrics-overview
- Connect Azure Monitor workspace to Azure Managed Grafana (Prometheus)
	- https://learn.microsoft.com/azure/managed-grafana/how-to-connect-azure-monitor-workspace
- Azure Monitor Metrics (93-day retention; portal 30-day per-chart query; PromQL 32-day max)
	- https://learn.microsoft.com/azure/azure-monitor/metrics/data-platform-metrics
- Diagnostic settings (partner solution destination)
	- https://learn.microsoft.com/azure/azure-monitor/essentials/diagnostic-settings
- Azure Native New Relic Service (overview/manage/troubleshoot)
	- https://learn.microsoft.com/azure/partner-solutions/new-relic/overview
	- https://learn.microsoft.com/azure/partner-solutions/new-relic/manage
	- https://learn.microsoft.com/azure/partner-solutions/new-relic/troubleshoot
