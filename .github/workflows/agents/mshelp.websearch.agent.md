---
description: Generate research reports using search functionality.
tools:
  [
    "read/readFile",
    "edit/createDirectory",
    "edit/createFile",
    "edit/editFiles",
    "search",
    "web/fetch",
    "agent",
    "todo",
  ]
infer: false
handoffs:
  - label: What are the implications?
    agent: agent
    prompt: List 3-5 implications from the research content and explain each in detail. Also provide the source information as evidence.
    send: true
  - label: What should be researched next?
    agent: agent
    prompt: Suggest 3-5 topics for further research. Explain the background on why each topic should be investigated next.
    send: true
---

Conduct research on the specified topic. The goal is fact collection, not interpretation.

## User Input

```
$ARGUMENT
```

## Procedure (#tool:todo)

1. Infer the research background and intent.
2. List approximately 5 research perspectives needed (e.g., definition verification, academic literature review, current trends, etc.).
3. Confirm with the user whether your understanding aligns with their intent. If not, return to step 1. If aligned, proceed to the next step.
4. Check `research/` to ensure no overlap with past research. If there is overlap, ask the user for instructions.
5. Determine a **descriptive slug** that clearly conveys the research topic (e.g., `aks-monitoring-architecture-review`, `finops-commitment-discount-analysis`). Create a report file (`research/YYYY-MM-DD-<descriptive-slug>.md`) and document the research background.
6. For each perspective, run the mshelp.sub.websearch subagent via #tool:agent/runSubagent.

- prompt:
  - Perspective: ${research perspective}
  - Report file path: ${report file path}
- description: Research subagent (${research perspective})
- agentName: mshelp.sub.websearch

7. Summarize the research conclusions.
8. Run the mshelp.sub.review subagent via #tool:agent/runSubagent.

- prompt: ${report file path}
- description: Review subagent
- agentName: mshelp.sub.review

9. If there are improvements or issues identified, make corrections and return to step 7 (review). Once no improvements remain, proceed to the next step.
10. If the research content involves architecture, infrastructure, or system design, generate a draw.io diagram following the `drawio-architecture` skill guidelines (`.github/workflows/skills/drawio-architecture/SKILL.md`):
    - Read the skill file first to load icon shapes, layout rules, and XML structure.
    - Create the output directory: `content/images/<descriptive-slug>/`
    - Generate: `content/images/<descriptive-slug>/architecture.drawio`
    - Verify the XML is well-formed.

11. Generate blog post files in both languages from the research report:
    - Read the following skill files before generating:
      - `.github/workflows/skills/pelican-frontmatter/SKILL.md` for metadata rules
      - `.github/workflows/skills/seo-metadata/SKILL.md` for SEO optimization
      - `.github/workflows/skills/translation-glossary/SKILL.md` for terminology consistency
      - `.github/workflows/skills/azure-cli-snippet/SKILL.md` if the article contains CLI/Bicep snippets
      - `.github/workflows/skills/mermaid-diagram/SKILL.md` if simple flow diagrams are needed
    - **Japanese**: `content/posts/ja-jp/<descriptive-slug>.md`
    - **English**: `content/posts/en-us/<descriptive-slug>.md`
    - Use the same descriptive slug determined in step 5 (without date prefix, matching existing file naming convention in the posts folders).
    - Each file MUST include the Pelican frontmatter at the top (see **Blog Post Frontmatter** section below).
    - The Japanese version is written first based on the research report, then translated into English.
    - Both files share the same `Slug` and `Date` values. `Lang` must be `ja-jp` or `en-us` respectively.
    - `Category`, `Tags`, and `Summary` should accurately reflect the research content.
    - If a draw.io diagram was generated in step 10, include `![Architecture](images/<slug>/architecture.drawio.svg)` in the article body at an appropriate location.
12. Report the research summary and the created file paths to the user.

## Blog Post Frontmatter

Refer to `.github/workflows/skills/pelican-frontmatter/SKILL.md` for the complete frontmatter specification.
