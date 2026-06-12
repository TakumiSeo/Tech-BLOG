Title: AI for FinOps ~ Using AI Agents to Accelerate FinOps ~
Date: 2025-01-20
Slug: finops-ai-agent
Lang: en-us
Category: notebook
Tags: azure, FinOps
Summary: Cloud Diaries: how to use AI agents to streamline FinOps operations.

## 1: FinOps meets AI
In this post I walk through how to apply FinOps practices with the help of AI agents.

GenAI adoption is exploding, and pure manual governance easily slips into "spend panic." Analysts already expect cloud spend to exceed 6 trillion yen by 2030, and GenAI is a big part of that rise. The FinOps Foundation even added "AI" as a new scope item in the 2025 framework update.

![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/693422/47247280-2ea4-48c6-990d-fee492096569.png)

From the AI boom, two patterns emerge:

* FinOps for AI: FinOps applied to AI workloads to manage AI cost.
* AI for FinOps: Using AI to improve FinOps itself through better insights and automation.

Both matter, but this post focuses on **AI for FinOps**.

Is FinOps + AI really worth it? As the [State of FinOps](https://data.finops.org/?_gl=1*1auhbod*_ga*MTk4Mjg5MDk4OS4xNzEzMTg5OTA2*_ga_GMZRP0N4XX*czE3NTA2ODgwMjAkbzE4JGcwJHQxNzUwNjg4MjkyJGo2MCRsMCRoMA..) report shows, AI-driven cost governance is now essential and sits alongside "cloud cost accountability" and "business value alignment" as core FinOps motions. Data requests, reporting, tagging hygiene, and cross-team collaboration still take time, so the more we can lean on AI, the better.

![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/693422/13cc485a-5dc8-4702-9576-1b13f10ef35f.png)

Optimization is the obvious use case, but the real value is when AI shortens the distance between questions and trusted answers, making continuous optimization practical instead of aspirational.

## 2: FinOps x AI Agent
FinOps practitioners often juggle costly data pulls and context switching. FinOps hubs can centralize FinOps Framework data, but querying still requires KQL skill.

**Good news: GitHub Copilot (with generated prompts) in VS Code plus the Azure MCP Server can now connect directly to FinOps hubs 0.11 so we can query by natural language.**

<https://techcommunity.microsoft.com/blog/finopsblog/whats-new-in-finops-toolkit-0-11-%E2%80%93-may-2025/4420719>

> Note: Model Context Protocol (MCP) connects AI agents to external data sources. The Azure MCP Server is maintained by Microsoft so Copilot and other agents can safely reach Azure resources.

---

### What are FinOps hubs?
FinOps hubs are a reference architecture and toolkit: cloud data ingestion, storage, dashboards, Power BI, Fabric, and Kusto—all wired together with a reasonable cost profile. Paired with GitHub Copilot + Azure MCP, your FinOps prompts become KQL that runs against the hub in a single flow.

![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/693422/9d853989-9414-4a0e-bbde-6b0a27ef9bb3.png)

Highlights:

* Data foundation: opinionated cloud cost ingestion and modeled data.
* Integration: Power BI, Microsoft Fabric, native KQL, GitHub Copilot.
* Architecture: Azure MCP Server auto-converts agent requests to KQL (with guardrails).

Deploy the reference template here:

<https://aka.ms/finops/hubs/deploy>

Docs:

<https://learn.microsoft.com/ja-jp/cloud-computing/finops/toolkit/hubs/deploy?tabs=azure-portal%2Cadx-dashboard>

> FinOps hubs use the FOCUS cost format. Other providers are supported via ingestion too: <https://learn.microsoft.com/ja-jp/cloud-computing/finops/toolkit/hubs/deploy?tabs=azure-portal%2Cadx-dashboard#ingest-from-other-data-sources>

---

### AI Agent setup (VS Code)
Follow the official guide:

<https://learn.microsoft.com/ja-jp/cloud-computing/finops/toolkit/hubs/configure-ai#configure-github-copilot-in-vs-code>

Once the Azure MCP Server is running and the `.github/prompts/copilot-instructions.md` is populated (subscription, tenant, cluster URI, DB, function names), Copilot can reach the hub. If the FOCUS schema JSON is missing, save `FocusCost_1.0.json` alongside instructions for schema lookup.

```yaml
- auth-method: 0
- Subscription Id: ********************
- Tenant Id: ********************
- Resource Group: ********************
- Location: ********
- Cluster URI: **********************************************
- Database: Hub
- Functions: Costs/Costs_v1_0
```

Directory example:

.github  
└─ prompts  
   ├─ copilot-instructions.md  
   └─ FocusCost_1.0.json

When ready, open Copilot Chat (Ctrl+Shift+I), turn on Agent Mode, and run the connection command:

```yaml
/ftk-hubs-connect
```

You should see the agent translate your intent into KQL and execute it against ADX.

![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/693422/b42f126c-364a-4418-9983-be2a82d114a8.png)

![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/693422/859aab9c-0d93-436a-b7ed-4eeb89a50939.png)

---

### AI Agent prompts for FOCUS
Below are example prompts mapped to FinOps capabilities.

#### Cost trends and allocation patterns

| Input need | Related FinOps capability | Example agent prompt |
|-----------|---------------------------|----------------------|
| Executive cost trend report | [Reporting and analytics](https://www.finops.org/framework/capabilities/reporting-and-analytics/) | "Show monthly billed and effective cost trends for the last 12 months." |
| Resource group cost ranking | [Allocation](https://www.finops.org/framework/capabilities/allocation/) | "What are the top resource groups by cost last month?" |
| Quarterly finance report | [Allocation](https://www.finops.org/framework/capabilities/allocation/) / [Reporting and analytics](https://www.finops.org/framework/capabilities/reporting-and-analytics/) | "Show quarterly cost by resource group for the last 3 quarters." |
| Service-level cost analysis | [Reporting and analytics](https://www.finops.org/framework/capabilities/reporting-and-analytics/) | "Which Azure services drove the most cost last month?" |
| Organizational cost allocation | [Allocation](https://www.finops.org/framework/capabilities/allocation/) / [Reporting and analytics](https://www.finops.org/framework/capabilities/reporting-and-analytics/) | "Show cost allocation by team and product for last quarter." |

#### Anomaly and budget monitoring

| Input need | Related FinOps capability | Example agent prompt |
|-----------|---------------------------|----------------------|
| Find cost spikes | [Anomaly management](https://www.finops.org/framework/capabilities/anomaly-management/) | "Find any unusual cost spikes or anomalies in the last 30 days." |
| Budget variance | [Budgeting](https://www.finops.org/framework/capabilities/budgeting/) | "Show actual vs. budgeted costs by resource group this quarter." |
| Trend detection | [Reporting and analytics](https://www.finops.org/framework/capabilities/reporting-and-analytics/) | "Identify resources with consistently increasing costs over the last 6 months." |
| Threshold monitoring | [Anomaly management](https://www.finops.org/framework/capabilities/anomaly-management/) | "Alert me to any single resources costing more than $5,000 monthly." |

More prompt ideas here: <https://techcommunity.microsoft.com/blog/finopsblog/a-practitioners-guide-to-accelerating-finops-with-github-copilot-and-finops-hubs/4420302>

---

### Example outputs
#### Cost overview

![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/693422/e9aecfb2-9d91-4c6d-b4be-1cc681a6c9be.png)

![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/693422/ca42ddd2-7730-424d-9db0-de9cdc6a2a16.png)

#### Cost spike (Anomaly)

![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/693422/f9522169-22ae-4dd9-8293-f48a0629f4ba.png)

Confidence: High  
Scope: Last 6 months, all resources  
Key finding: No unusual spikes detected—only one month of cost data exists (`June 2025: $1,888.55`), so month-over-month analysis is not yet possible.

Recommendations

1. Continue monitoring as more months of data land.  
2. Set up automated monthly trend analysis to catch spikes as soon as new data arrives.

#### Remediation example

The agent produced a prioritized action list. Example: right-sizing the top 3 most expensive resources, e.g., AVD sizing review where login count is 1:1 and SKU is oversized.

![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/693422/83b3539a-f304-4440-941e-5593cd557283.png)

:::note
Workflow used in copilot-instructions.md:
1. THINK: Clarify intent (e.g., optimize cost-effective resources).
2. PLAN: Draft queries against the Costs table—top N expensive resources, SKU mix, underutilized instances, reserved instances.
3. VERIFY: Validate schema and assumptions before execution.
4. EXECUTE: Run via FinOps Hub; for each resource, propose a right-size action.
5. VALIDATE: Check that proposed actions will reduce cost without breaking workloads.
:::

:::note warn
Azure Data Explorer has a 64 MB default result size limit. For large datasets, add time filters and aggregation, or use DirectQuery in Power BI.
:::

Time filters to keep queries healthy:
- Minimal: filter by time window to avoid result-size errors.
- Recommended: add granular time filters (weekly/daily) when exploring.

Examples: `"Show cost for the last 30 days"` vs `"Show all-time cost"`.

FinOps capability alignment: [Data ingestion](https://www.finops.org/framework/capabilities/data-ingestion/)

---

Known limitations
- Large data pulls can hit the 64 MB ADX result limit.
- Missing filters lead to slow or failed queries.

Example mitigation: `"Show projected monthly cost by workload"` vs `"List every raw cost record"`.

Best-practice workflow: iterate quickly, verify schema, and narrow scope as needed.

---

Schema validation errors
- If schema fails, check your connection metadata and run schema tests before querying.

---

Example time filters
- `"Show cost for Q1 2025"`  
- `"Show all regions for the last 90 days"`  
- `"Top 10 resource groups by cost"`  
- `"All subscriptions and their cost by service"`

---
### 3: Wrap up
AI lowers the activation energy for FinOps. With GitHub Copilot, FinOps hubs, and the Azure MCP Server, natural-language questions become KQL against your cost data—no context switching, no manual joins.

There is still engineering to do around guardrails, schema governance, and prompt design, but AI for FinOps is already practical. Start with small, verified queries, validate outputs, and expand coverage.

That is all for now.
