# tech-verification-blog

English technology verification blog powered by [Pelican](https://docs.getpelican.com/) with a Microsoft Security Blog inspired custom theme (`themes/my-blog-template`). The repository is ready for Python 3.12, Markdown authoring, responsive design, syntax highlighting, and automated deployments to Azure Static Web Apps.

## Requirements
- Python 3.12
- Node.js 18+ (for the Azure Static Web Apps CLI)
- Git

## Initial Setup
1. Clone the repository.
2. Create and activate a virtual environment (example for PowerShell):
   ```pwsh
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```
3. Install Python dependencies:
   ```pwsh
   pip install -r requirements.txt
   ```
4. (Optional) Fetch Pelican community themes for reference:
   ```pwsh
   git clone --recursive https://github.com/getpelican/pelican-themes themes
   ```
   The site already includes a purpose-built Microsoft Security style theme under `themes/my-blog-template`.
5. (Optional) Install the Static Web Apps CLI for local Azure parity:
   ```pwsh
   npm install -g @azure/static-web-apps-cli
   ```

## Local Development
The quickest way to edit code, preview on localhost, and restart cleanly is to split build and serve into two terminals.

1. **Clean stale artifacts (optional but recommended after large edits):**
   ```pwsh
   rm -Recurse -Force output,cache,pelican.pid -ErrorAction SilentlyContinue
   ```
2. **Terminal A – continuous build with auto reload:**
   ```pwsh
   pelican content --autoreload -o output -s pelicanconf.py
   ```
   This watches `content/`, `themes/my-blog-template/`, and configuration files. Whenever you fix or tweak code, the output folder is rebuilt automatically.
3. **Terminal B – lightweight HTTP server:**
   ```pwsh
   pelican --listen
   ```
   Browse to <http://localhost:8000> to see the latest build using the Microsoft Security themed layout.
4. **Refresh after edits:** once Terminal A logs `Done`, reload the browser to view the updates.
5. **Stop (kill) running processes before restarting or switching branches:**
   ```pwsh
   # Stop whoever currently owns port 8000 (usually pelican --listen)
   Get-NetTCPConnection -LocalPort 8000 | ForEach-Object { Stop-Process -Id $_.OwningProcess }
   # Stop background pelican builders if they are still running
   Get-Process -Name pelican -ErrorAction SilentlyContinue | Stop-Process -Force
   ```

Shortcut commands remain available when you just need one-off builds:
- サイト生成 (make html 相当):
  ```pwsh
  pelican content -o output -s pelicanconf.py
  ```
- 本番ビルド (make publish 相当):
  ```pwsh
  pelican content -o output -s publishconf.py
  ```

### Theme toggle
- The Microsoft Security inspired theme ships with a light/dark toggle in the header.
- The toggle honors the OS preference first, then whatever the visitor last selected (saved in `localStorage`).
- Customize defaults by setting `THEME_DEFAULT_MODE = 'dark'` (or `'light'`) inside `pelicanconf.py`.

## Azure Static Web Apps Deployment
GitHub Actions handles builds via `.github/workflows/azure-static-web-apps.yml`:
1. Create an Azure Static Web Apps resource and note the deployment token.
2. Add the token as the secret `AZURE_STATIC_WEB_APPS_API_TOKEN` in your GitHub repository.
3. Push to the `main` branch to trigger the workflow; it runs `pelican content -o output -s publishconf.py` and uploads the `output/` directory.
4. For manual deploys or local validation, use the Static Web Apps CLI:
   ```pwsh
   npx swa build
   npx swa deploy --env production
   ```

## Writing Content
- Posts live under `content/posts/` using markdown filenames like `YYYY-MM-DD-title.md`.
- Static pages belong in `content/pages/`.
- URLs follow `posts/{slug}/`, keeping permalinks clean for testing guides.

## Project Structure
| Path | Purpose |
| --- | --- |
| `requirements.txt` | Pin Python packages (Pelican, Markdown, Pygments, Typogrify, Rich) for reproducible builds. |
| `pelicanconf.py` | Dev settings: author/site metadata, Microsoft Security inspired theme selection, Markdown extensions, syntax highlight, URL rules. |
| `publishconf.py` | Production overrides such as feeds, `SITEURL`, and cleaned output folder. |
| `Makefile` | Convenience commands (`make html`, `make devserver`, `make publish`, etc.). |
| `.gitignore` | Excludes virtual environments, Pelican output, caches, and editor metadata. |
| `.github/workflows/azure-static-web-apps.yml` | GitHub Actions workflow that installs Python 3.12, builds the site, and deploys to Azure Static Web Apps. |
| `content/pages/about.md` | Sample About page. |
| `content/posts/2025-01-20-first-post.md` | Sample article showing markdown structure and code blocks. |

Update content and redeploy whenever you verify new Azure scenarios.
