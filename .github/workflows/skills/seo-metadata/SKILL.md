---
name: seo-metadata
description: SEO optimization rules for blog post metadata including title length, summary/description, slug conventions, and structured data considerations. Use when generating or reviewing blog post frontmatter for search engine visibility.
metadata:
  author: takumiseo
  version: "1.0"
---

# SEO Metadata Skill

Rules for optimizing blog post metadata for search engine discovery.

## Title Rules

| Rule | Japanese (ja-jp) | English (en-us) |
| ---- | ---------------- | ---------------- |
| Max length | 60 characters (30 全角) | 60 characters |
| Include primary keyword | Within first 30 chars | Within first 30 chars |
| Avoid | Clickbait, ALL CAPS, excessive punctuation | Same |
| Structure | `{Primary Topic}（{Context/Technology}）` | `{Primary Topic} — {Context/Technology}` |

### Good Title Examples

- ja-jp: `AKS 監視構成レビュー（Azure Monitor / Prometheus）`
- en-us: `AKS Monitoring Architecture Review — Azure Monitor / Prometheus`

### Bad Title Examples

- `すごい！AKSの監視について調べてみた！！！` (clickbait, vague)
- `REVIEW OF ALL THE MONITORING OPTIONS FOR AKS` (ALL CAPS)

## Summary / Meta Description Rules

| Rule | Guideline |
| ---- | --------- |
| Length | 120-160 characters (50-80 全角 for Japanese) |
| Content | Answer "what will the reader learn?" |
| Include | Primary keyword + value proposition |
| Avoid | Repeating the title verbatim |
| Tone | Factual, not promotional |

### Good Summary Examples

- ja-jp: `AKS の監視構成案3パターンについて Azure Monitor 観点で実現性・コスト最適化ポイントを整理。Microsoft Learn 根拠のみ。`
- en-us: `Review of three AKS monitoring architecture proposals from Azure Monitor perspective. Covers feasibility, cost optimization, and caveats based on Microsoft Learn.`

## Slug Rules

| Rule | Guideline |
| ---- | --------- |
| Format | Lowercase, hyphen-separated |
| Length | 3-7 words (max 60 chars) |
| Language | Always English (even for ja-jp posts) |
| Include | Primary keyword |
| Avoid | Stop words (the, a, an, of), dates, numbers unless essential |
| Consistency | Same slug for ja-jp and en-us versions |

### Good Slugs

- `aks-monitoring-architecture-review`
- `finops-ai-agent`
- `azure-managed-grafana-setup`

### Bad Slugs

- `2026-03-05-aks-review` (date in slug)
- `azuremonitor_azuremanagedvisualisation` (underscore, overly long)
- `post-1` (meaningless)

## Tags Rules

| Rule | Guideline |
| ---- | --------- |
| Format | Lowercase, comma-separated |
| Count | 3-8 tags per post |
| Specificity | Mix of broad (`azure`) and specific (`azure-monitor`) |
| Consistency | Reuse existing tags; check `content/posts/` for established tags |

### Established Tags (check and reuse)

Common tags in this blog: `azure`, `aks`, `finops`, `aiops`, `pelican`, `static-web-apps`, `sre-agent`, `azure-monitor`, `prometheus`, `grafana`, `observability`

## Heading Structure (for SEO)

- Use exactly one `## ` (H2) per major section in the article body (Pelican uses Title as H1).
- Use `### ` (H3) for subsections.
- Include keywords naturally in headings.
- Keep heading hierarchy strict: H2 → H3 → H4 (no skipping levels).

## Image Alt Text

- Every image must have descriptive alt text.
- Include relevant keywords naturally.
- Example: `![AKS monitoring data flow from Container Insights to Log Analytics](images/aks-monitoring/architecture.drawio.svg)`
