---
name: azure-cli-snippet
description: Quality rules for Azure CLI, PowerShell, and Bicep code snippets in blog posts. Ensures reproducibility, security, and consistent formatting. Use when writing or reviewing technical blog posts that include Azure command examples.
metadata:
  author: takumiseo
  version: "1.0"
---

# Azure CLI Snippet Skill

Standards for code snippets in technical blog posts to ensure reproducibility and security.

## General Rules

1. **Language tag**: Always specify the language in fenced code blocks (`bash`, `powershell`, `bicep`, `json`, `yaml`).
2. **One concept per block**: Don't mix unrelated commands in a single code block.
3. **Comment first**: Add a brief comment at the top of each block explaining what it does.
4. **Copy-pasteable**: Snippets should run as-is after variable substitution.

## Azure CLI (`az`) Rules

### Variables

Use shell variables at the top so readers can customise values:

```bash
# Set your resource names
RESOURCE_GROUP="rg-myapp"
LOCATION="japaneast"
AKS_NAME="aks-myapp"
```

- Use `UPPER_SNAKE_CASE` for variable names.
- Never hardcode subscription IDs, tenant IDs, or secrets.
- Use `<placeholder>` for values the reader must replace: `SUBSCRIPTION_ID="<your-subscription-id>"`

### Version Pinning

- Specify `--api-version` when using preview features.
- Note the minimum `az` CLI version if a command requires it:

```bash
# Requires az CLI 2.61+ 
az aks create ...
```

### Output Format

- Use `--output table` for human-readable examples.
- Use `--output json` or `--output tsv` when piping to other commands.
- Show expected output as a separate comment block when helpful:

```bash
az aks show --name $AKS_NAME --resource-group $RESOURCE_GROUP --output table
# Expected output:
# Name        Location    ResourceGroup    KubernetesVersion    ...
# aks-myapp   japaneast   rg-myapp         1.29.2               ...
```

### Error Handling

- Include `--only-show-errors` for cleaner output in scripts.
- Mention common errors and fixes in the article text, not in the snippet.

## Azure PowerShell Rules

- Use full cmdlet names (e.g., `Get-AzResource`), not aliases.
- Use splatting for commands with many parameters:

```powershell
$params = @{
    ResourceGroupName = "rg-myapp"
    Location          = "japaneast"
    Name              = "aks-myapp"
}
New-AzAksCluster @params
```

## Bicep Rules

- Use `param` with `@description` decorators for clarity:

```bicep
@description('The name of the AKS cluster')
param aksName string

@description('The Azure region for deployment')
param location string = resourceGroup().location
```

- Always specify `targetScope` if not `resourceGroup`.
- Use modules for reusable components.
- Never embed secrets — use Key Vault references or `@secure()` decorator.

## Security Checklist

- [ ] No secrets, keys, or tokens in snippets
- [ ] No real subscription IDs, tenant IDs, or object IDs
- [ ] Placeholder syntax `<value>` used for sensitive inputs
- [ ] `@secure()` used for Bicep parameters that accept secrets
- [ ] No `--no-verify` or similar safety bypasses

## Formatting

- Max line width: 80 characters preferred, 120 max.
- Use `\` (bash) or `` ` `` (PowerShell) for line continuation.
- Indent continuation lines by 2 spaces:

```bash
az aks create \
  --resource-group $RESOURCE_GROUP \
  --name $AKS_NAME \
  --node-count 3 \
  --generate-ssh-keys
```
