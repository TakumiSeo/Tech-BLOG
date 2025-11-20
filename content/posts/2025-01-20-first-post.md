Title: First Verification Log
Date: 2025-01-20
Slug: first-post
Category: notebook
Tags: azure,static-web-apps,pelican
Summary: Kick-off entry describing the lab stack for Cloud Diaries: Azure Edition.

Pelican 4.9 plus the Flex theme gives me a lightweight but elegant baseline. Syntax highlighting is handled by `codehilite` and Pygments, which means I can paste raw experiment output without losing clarity.

## Sample Snippet
The first automated deployment will validate that the GitHub Actions workflow produces the exact artifact Azure Static Web Apps expects.

```yaml
name: azure-static-web-apps
on:
  push:
    branches: ["main"]
```

## Next Steps
1. Validate dark-mode rendering in desktop and mobile breakpoints.
2. Extend the workflow with smoke tests using `npx swa build` as part of CI.
3. Write deeper dives on ARM-/Bicep-based staging environments.
