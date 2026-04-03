---
name: pelican-frontmatter
description: Pelican blog post frontmatter specification and validation rules. Defines required metadata fields, naming conventions, and i18n linking rules for ja-jp/en-us bilingual blog posts. Use when generating, reviewing, or validating blog post markdown files.
metadata:
  author: takumiseo
  version: "1.0"
---

# Pelican Frontmatter Skill

Specification for blog post metadata in this Pelican-based bilingual blog.

## Required Fields

Every blog post file MUST start with the following metadata block. No `---` fences — just plain `Key: value` lines:

```
Title: {title}
Date: {YYYY-MM-DD}
Slug: {slug}
Lang: {ja-jp or en-us}
Category: {category}
Tags: {comma-separated tags}
Summary: {summary}
```

After the last metadata line, leave **one blank line**, then begin the article body.

## Field Specifications

| Field      | Required | Rules |
| ---------- | -------- | ----- |
| `Title`    | Yes      | Descriptive and concise. Written in the target language (Japanese for ja-jp, English for en-us). |
| `Date`     | Yes      | `YYYY-MM-DD` format. The date the content was written or researched. |
| `Slug`     | Yes      | Lowercase, hyphen-separated. Must be **identical** across ja-jp and en-us versions for Pelican i18n_subsites linking. Example: `finops-ai-agent` |
| `Lang`     | Yes      | Exactly `ja-jp` or `en-us`. |
| `Category` | Yes      | Default: `notebook`. Use lowercase. |
| `Tags`     | Yes      | Comma-separated, lowercase. Example: `azure, aks, monitoring` |
| `Summary`  | Yes      | 1-2 sentence abstract in the target language. |

## Optional Fields

| Field      | Usage |
| ---------- | ----- |
| `Status`   | `draft` to hide from published output. Omit for published posts. |
| `Modified` | `YYYY-MM-DD` format. Set when updating an existing post. |
| `Authors`  | Author name. Only needed if different from the default. |

## Bilingual Pairing Rules

- ja-jp and en-us versions of the same article MUST share the same `Slug` and `Date`.
- File naming: `content/posts/ja-jp/<slug>.md` and `content/posts/en-us/<slug>.md`
- No date prefix in filenames (matches existing convention).
- `Title` and `Summary` must be localized to each language — not transliterated.

## Validation Checklist

- [ ] No `---` fences around metadata
- [ ] `Date` is valid `YYYY-MM-DD`
- [ ] `Lang` is exactly `ja-jp` or `en-us`
- [ ] `Slug` is lowercase, hyphen-separated, no special characters
- [ ] `Slug` matches between ja-jp and en-us files
- [ ] `Tags` are comma-separated and lowercase
- [ ] Blank line between metadata and body
- [ ] `Summary` is present and concise

## Examples

### Japanese (ja-jp)

```
Title: AKS 監視構成案レビュー（Azure Monitor / Managed Prometheus）
Date: 2026-03-05
Slug: aks-monitoring-architecture-review
Lang: ja-jp
Category: notebook
Tags: azure, azure-monitor, aks, prometheus, grafana, observability
Summary: AKS の監視構成案について Azure Monitor 観点で実現性・注意点・コスト最適化ポイントを整理。
```

### English (en-us)

```
Title: AKS Monitoring Architecture Review (Azure Monitor / Managed Prometheus)
Date: 2026-03-05
Slug: aks-monitoring-architecture-review
Lang: en-us
Category: notebook
Tags: azure, azure-monitor, aks, prometheus, grafana, observability
Summary: Review of AKS monitoring architecture proposals from Azure Monitor perspective covering feasibility, caveats, and cost optimization.
```
