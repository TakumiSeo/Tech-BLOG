Title: How to Organize a Log Analytics Cost Optimization Discussion
Date: 2026-03-17
Slug: log-analytics-cost-optimization
Lang: en-us
Category: notebook
Tags: azure, azure-monitor, log-analytics, cost-optimization, finops, observability
Summary: A practical agenda for moving from "store everything" to a well-architected Log Analytics cost model.

## 0. What is missing in the current agenda

The current outline includes valid optimization levers such as reducing collection, shortening retention, exporting old data, and considering commitment tiers.

However, the **primary gap** is this:

> We have not yet defined which logs are required for which operational decisions.

That matters because a well-architected cost discussion should not start with "How do we make storage cheaper?"

It should start with:

1. What incidents are we trying to detect or investigate?
2. Which teams use which logs, and how often?
3. Which logs need fast interactive analysis, and which logs are only kept for audit or rare forensic use?

Without that operating model, every later action becomes guesswork. Teams often jump to retention tuning or commitment tiers too early and keep paying to collect data that nobody actually uses.

---

## 1. Recommended story line for the discussion

I would organize the theory in this order:

1. **Operational purpose first**
	Define why the workspace exists.
	Today the main use case is reactive troubleshooting after incidents, especially WAF blocks and performance degradation.

2. **Usage evidence second**
	Identify what data is actually queried, by whom, and for how long after an incident.

3. **Collection policy third**
	Decide which data should enter Log Analytics at all.

4. **Retention and table plan fourth**
	Decide which data needs Analytics access, which can move to Basic, and which should be archived or exported.

5. **Pricing optimization last**
	Only after volume and usage are understood should you discuss commitment tiers or other pricing constructs.

This sequence fits the cost pillar better because it optimizes based on **value of telemetry**, not only on raw GB volume.

---

## 2. The understandable agenda

### Agenda 1. Reconfirm the operational goal of the workspace

Start with the plain question:

**What business or operational outcomes must this workspace support?**

Based on the current answers, the honest scope is still narrow:

- Post-incident troubleshooting
- WAF block investigation
- Performance degradation analysis

Also make the current limitation explicit:

- Proactive detection is not yet mature
- Logs are being collected broadly without a clear decision standard

This gives a strong opening message:

> The current workspace behaves as a default storage destination, not yet as a deliberately designed observability platform.

### Agenda 2. Deep dive first into log value, not pricing

This should be the **first major deep dive**.

The key question is:

**Which logs are genuinely useful for detection, triage, root cause analysis, audit, or compliance, and which are not?**

Organize the discussion into four value tiers:

| Value tier | Meaning | Typical action |
|---|---|---|
| Critical operational logs | Needed for incident detection or fast troubleshooting | Keep in Log Analytics with interactive access |
| Useful but non-critical logs | Occasionally used for investigation | Consider Basic logs or shorter retention |
| Rarely used logs | Kept mostly for audit or rare forensics | Archive or export to cheaper storage |
| No demonstrated value logs | No clear user, query pattern, or response action | Stop collecting if possible |

This is the most important conversation because it converts "all logs are probably useful" into a reviewable policy.

### Agenda 3. Map actual troubleshooting workflows to required data

The customer already said the workspace is mainly used for:

- Investigating WAF blocks
- Reviewing metrics during performance degradation

That means the next step is to map each workflow to the minimum required data.

Example:

| Use case | What responders need | Questions to answer |
|---|---|---|
| WAF block investigation | WAF rule hit details, request context, time window, client/source indicators | Which tables are queried? How long after the event? Do we need full payload-level detail? |
| Performance degradation | Correlated app, platform, and dependency signals | Which logs are used versus which metrics are enough? What is the usual lookback period? |

This is where many cost programs find waste. Teams often keep detailed logs in Analytics even when the actual investigation mostly uses metrics and a narrow subset of error or access records.

### Agenda 4. Review current ingestion by source and category

Only after the value discussion should you review collection settings.

Focus on:

- Which Azure resources send diagnostic logs to the workspace
- Which categories are enabled
- Whether any high-volume categories are collected by default without an active use case
- Whether filtering can be applied before or during ingestion

The main principle is simple:

> If a team cannot explain how a log category is used, it should not automatically stay in Analytics collection.

This is the step that turns the high-level idea of "filter unnecessary logs" into an engineering backlog.

### Agenda 5. Review retention by use case, not by one global period

Retention should not be discussed as a single workspace-wide number.

Instead ask:

- How many days of interactive investigation are actually needed?
- Which tables need fast query performance for recent incidents?
- Which data only needs to be retained for audit or rare investigation?

The target model should look like this:

- Recent and high-value data stays in Analytics for fast investigation
- Infrequently queried troubleshooting or audit data moves to lower-cost plans or archive patterns
- Historical data with no frequent query need is exported or retained in cheaper long-term storage

This is the point where table-level retention review becomes meaningful.

### Agenda 6. Review table plans and access patterns

Now the team can evaluate whether some tables should remain in Analytics and whether others are better suited to Basic logs.

The practical test is:

- Is this table used for alerting?
- Is it queried interactively and frequently?
- Is it mainly used for occasional troubleshooting or audit?

If a table is rarely queried and not central to alerting, it becomes a candidate for a cheaper plan.

This is much stronger than saying "move low-value data to cheaper storage" because it ties the decision to real usage.

### Agenda 7. Define the future-state operating model

This section is important because the current problem is not only technical. It is also governance-related.

The team should agree on a lightweight policy such as:

- New log sources must have an identified owner
- Each log category must have a stated purpose: detection, troubleshooting, audit, or compliance
- Each table must have a target plan and retention period
- High-volume sources must be reviewed periodically
- Cost anomalies in ingestion must trigger review

This is the point where the workspace begins to look well-architected.

### Agenda 8. Consider pricing optimization after the design is cleaned up

Only here should you discuss commitment tiers.

Commitment tiers can be the right answer when:

- The ingestion volume is already understood
- Waste has already been reduced
- The remaining baseline volume is stable enough to commit to

Otherwise, commitment can lock in spend before the design is optimized.

So the right message is:

> Commitment tier is an optimization for a known and justified baseline, not a substitute for log governance.

---

## 3. What to deep dive first

If you want one single answer to "what should we deep dive first?", it is this:

## First deep dive: log usefulness and decision rights

The first workshop should answer the following:

1. Which incident scenarios are important enough to justify log cost?
2. Which tables and log categories are actually used in those scenarios?
3. Which teams query them, and how often?
4. What is the required investigation window: 7 days, 30 days, 90 days?
5. Which logs are kept only because "maybe they will be useful someday"?

Why this is first:

- It exposes unused ingestion
- It exposes excessive retention
- It prevents premature discussion about commitment tiers
- It creates a decision framework for all later tuning

In short, the first deep dive should answer **"What should stay in Log Analytics, and why?"**

---

## 4. A cleaner theory to present

If you need a short theory model for presentation, I would frame it like this:

## The four-layer model for log cost optimization

### Layer 1. Purpose

Define the operational outcomes the logs must support.

Examples:

- Reactive troubleshooting
- Proactive detection
- Audit and compliance
- Security investigation

### Layer 2. Value

Classify data by how much operational value it provides.

Examples:

- High-value and frequently used
- High-value but rarely used
- Low-value and rarely used
- No proven value

### Layer 3. Placement

Choose where the data should live.

Examples:

- Analytics logs for fast, frequent investigation
- Basic logs for lower-cost occasional query scenarios
- Archive or Blob export for long-term, low-touch retention

### Layer 4. Pricing

After Layers 1-3 are designed, optimize the billing model.

Examples:

- Commitment tier
- Anomaly alerts on ingestion growth
- Periodic cost review

This model is easy to explain because it separates **why we keep logs** from **where we keep them** and from **how we pay for them**.

---

## 5. A practical meeting structure

If this is for a customer workshop or architecture review, I would run it in this order.

### Part 1. Current-state review

- What are the top current use cases?
- Which incidents drove the current logging setup?
- Which logs are actually queried today?
- What are the largest cost contributors by source or table?

### Part 2. Gap analysis

- No clear logging strategy
- Collection defaults are broader than operational need
- Retention is not aligned to usage patterns
- Proactive detection use cases are underdeveloped
- Cost decisions are not yet tied to log value

### Part 3. Design decisions

- Define required use cases
- Classify log data by value
- Reduce collection scope
- Tune retention by table and purpose
- Select proper table plans
- Export or archive cold data

### Part 4. Commercial optimization

- Review whether baseline ingestion justifies commitment tier
- Set monitoring for ingestion anomalies
- Create recurring cost review ownership

---

## 6. Final message to the customer

The key message should be direct:

> The first objective is not to make Log Analytics cheaper in isolation. The first objective is to design a logging model where only operationally justified data stays in high-cost interactive analytics.

Once that is clear, the optimization sequence becomes straightforward:

1. Clarify use cases
2. Identify valuable versus unused logs
3. Reduce unnecessary ingestion
4. Align retention and table plans to access patterns
5. Use archive, export, and commitment pricing only after the baseline is clean

That is the point where the discussion becomes well-architected from a cost perspective.
