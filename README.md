# tech-verification-blog

English technology verification blog powered by [Pelican](https://docs.getpelican.com/) and the Flex theme, targeting Azure Static Web Apps. The repository is ready for Python 3.12, Markdown authoring, responsive design, syntax highlighting, and automated deployments.

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
4. Fetch the Flex theme (navy, responsive, dark-mode friendly):
   ```pwsh
   git clone --recursive https://github.com/getpelican/pelican-themes themes
   ```
   The site loads the theme from `themes/Flex`.
5. (Optional) Install the Static Web Apps CLI for local Azure parity:
   ```pwsh
   npm install -g @azure/static-web-apps-cli
   ```

## Local Development
- Generate the site: `make html`
- Auto-regenerating dev server (port 8000 by default): `make devserver`
- Clean artifacts: `make clean`
- Production-ready build: `make publish`

After running `make devserver`, visit <http://localhost:8000>. Flex automatically adapts to light/dark mode, and `codehilite` + `pygments` provide syntax highlighting suited for verification write-ups.

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
| `pelicanconf.py` | Dev settings: author/site metadata, Flex theme selection, Markdown extensions, syntax highlight, URL rules. |
| `publishconf.py` | Production overrides such as feeds, `SITEURL`, and cleaned output folder. |
| `Makefile` | Convenience commands (`make html`, `make devserver`, `make publish`, etc.). |
| `.gitignore` | Excludes virtual environments, Pelican output, caches, and editor metadata. |
| `.github/workflows/azure-static-web-apps.yml` | GitHub Actions workflow that installs Python 3.12, builds the site, and deploys to Azure Static Web Apps. |
| `content/pages/about.md` | Sample About page. |
| `content/posts/2025-01-20-first-post.md` | Sample article showing markdown structure and code blocks. |

Update content and redeploy whenever you verify new Azure scenarios.
