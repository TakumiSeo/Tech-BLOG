---
name: presentation-deck
description: Generate 16:9 PowerPoint (.pptx) speaking decks from this blog's posts, reusing existing draw.io PNG diagrams. Produces title/section/bullet/image/quote/closing slides with a consistent theme, Japanese fonts, source footers, and speaker notes via python-pptx. Use when turning a blog article (e.g., a 登壇 / executive summary) into slides, or when the user asks for "スライド", "デッキ", "登壇資料", "PowerPoint", or ".pptx".
metadata:
  author: takumiseo
  version: "1.0"
---

# Presentation Deck Skill

Turn a blog post in this repo into a clean 16:9 PowerPoint deck for talks (登壇) or executive briefings. The deck is generated from a small JSON spec by [build_deck.py](build_deck.py) using `python-pptx`, and **reuses the draw.io PNG diagrams already produced** under `content/images/<slug>/`.

> Scope: This is a repo-specific skill tuned to this blog's conventions (factual-only, cited, bilingual, draw.io PNG reuse). For advanced .pptx work — editing an existing customer template, SharePoint/OneDrive-hosted decks, complex custom layouts, or extracting text from a `.pptx` — defer to the global `pptx` skill at `~/.copilot/skills/pptx/SKILL.md`.

## Prerequisites

Already available in the repo venv (`.venv`): `python-pptx`, `Pillow`. No extra install needed. Run all commands from the repo root with the venv Python:

```powershell
.venv\Scripts\python.exe .github\skills\presentation-deck\build_deck.py <spec.json> -o decks\<slug>.pptx
```

## Output Convention

- Decks are written to `decks/<slug>.pptx` (top-level `decks/` folder).
- `decks/` is **not** in Pelican `STATIC_PATHS`, so decks never leak into the published site.
- Use the same `<slug>` as the source post for traceability (e.g., `ai-for-finops-finops-x-2026`).

## Workflow

1. **Read the source post** under `content/posts/ja-jp/<file>.md`. Extract the spine: title, key messages, section headings, and the figures it already embeds.
2. **Reuse existing diagrams.** Look in `content/images/<slug>/` for `.png` files and put them on `image` slides. Do **not** regenerate diagrams that already exist. If a new diagram is needed, use the `drawio-architecture` skill first, export to PNG, then reference it.
3. **Write a JSON spec** (see schema below). Keep one idea per slide; prefer 8–14 slides for a talk.
4. **Build:** run `build_deck.py` (command above).
5. **Preview & verify** (see Preview section). Check Japanese rendering and that no text overflows.

## Spec Schema

A spec is a JSON file (store under `.github/skills/presentation-deck/examples/` or alongside the post). See [examples/ai-for-finops.deck.json](examples/ai-for-finops.deck.json) for a complete working example.

```jsonc
{
  "meta": {
    "title": "デッキのタイトル",
    "subtitle": "サブタイトル",
    "author": "Taku Sewo",
    "date": "2026-06-12",
    "lang": "ja-jp",
    "theme": "midnight"        // midnight | teal | charcoal | berry
  },
  "slides": [ /* see slide types */ ]
}
```

### Slide types

| `type`    | Required fields            | Optional fields                          | Use for |
| --------- | -------------------------- | ---------------------------------------- | ------- |
| `title`   | `title`                    | `subtitle`, `author`, `date`, `notes`    | Opening slide (dark) |
| `section` | `title`                    | `eyebrow`, `notes`                       | Section divider (dark) |
| `bullets` | `title`, `bullets`         | `source`, `notes`                        | Key points (light) |
| `image`   | `title`, `image`           | `caption`, `source`, `notes`             | A draw.io PNG / screenshot (light) |
| `quote`   | `text`                     | `attribution`, `source`, `notes`         | A pull quote (dark) |
| `closing` | `bullets`                  | `title`, `source`, `notes`               | Call-to-action / summary (dark) |

- `bullets` items are either a string, or `{ "text": "...", "level": 1 }` for a sub-bullet.
- `image` paths are **repo-root-relative** (e.g., `content/images/<slug>/concept-map.png`). Absolute paths also work. Images are auto-scaled to fit while preserving aspect ratio.
- `source` renders as a small footer (use for citations, e.g., `出典: FinOps Foundation`).
- `notes` becomes the slide's speaker notes — use it for talk track.

### Themes

`midnight` (navy/blue), `teal`, `charcoal` (warm gold accent), `berry` (magenta). Dark slides (title/section/quote/closing) use the dark color; content slides are light. Pick a theme that matches the topic.

## Content Rules (inherit from the blog)

- **Facts only.** No opinions or invented numbers. Mirror the cited claims from the source post.
- **Cite on data slides.** Put the origin in `source` (e.g., `出典: FinOps X 2026 Day1 Keynote`). Keep full URLs in the blog post's footnotes, not on the slide.
- **Language.** Default to Japanese (`Yu Gothic UI` is applied to Latin + 日本語). For an English deck, write the spec text in English and set `meta.lang` to `en-us`.
- **One idea per slide.** Move detail into `notes` (speaker notes) rather than crowding the slide.

## Preview / Verification

Render slides to PNG to verify fonts and layout before sharing.

- **PowerPoint (Windows, preferred here):**

  ```powershell
  $deck = (Resolve-Path "decks\<slug>.pptx").Path
  $out  = (New-Item -ItemType Directory -Force -Path "decks\_preview").FullName
  $ppt = New-Object -ComObject PowerPoint.Application
  $pres = $ppt.Presentations.Open($deck, $true, $false, $false)
  $pres.SaveAs($out, 18)   # 18 = ppSaveAsPNG
  $pres.Close(); $ppt.Quit()
  ```

  View the PNGs, then delete the temp folder: `Remove-Item -Recurse -Force decks\_preview`.

- **LibreOffice (if installed):** the global pptx skill's `scripts/thumbnail.py` builds a thumbnail grid (`soffice` required).

Checklist: Japanese renders (no tofu boxes), no text overflow, images centered and uncropped, citations present on data slides.

## Extending

- **New slide layout:** add a `slide_<type>()` builder in [build_deck.py](build_deck.py) and register it in `BUILDERS`.
- **New theme:** add an entry to `PALETTES` (keys: `dark`, `light`, `accent`, `ink`, `sub`, `band`).
- **Fonts:** `DEFAULT_FONT` is `Yu Gothic UI`; the script sets the East-Asian typeface so Japanese glyphs render correctly.

## Troubleshooting

| Symptom | Fix |
| ------- | --- |
| `Image not found` | Use a repo-root-relative path (`content/images/...`) and run from the repo root. |
| Japanese shows as boxes in preview | Ensure `Yu Gothic UI` (or Meiryo) is installed; change `DEFAULT_FONT` if needed. |
| Text overflows the slide | Shorten the line or move detail to `notes`; split into two slides. |
| Diagram looks small | Diagrams are fit-to-box; crop whitespace in the source `.drawio` or export at higher scale. |
