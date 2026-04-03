---
name: mermaid-diagram
description: Generate Mermaid diagrams for blog posts including flowcharts, sequence diagrams, and state diagrams. Use for simple visualizations where draw.io would be overkill. Provides syntax references, styling guidelines, and Pelican integration instructions.
metadata:
  author: takumiseo
  version: "1.0"
---

# Mermaid Diagram Skill

Generate Mermaid diagrams for lightweight visualizations in blog posts.

## When to Use Mermaid vs draw.io

| Use Mermaid | Use draw.io |
| ----------- | ----------- |
| Flowcharts (< 10 nodes) | Complex architecture with cloud icons |
| Sequence diagrams | Multi-layer network diagrams |
| State diagrams | Diagrams requiring precise positioning |
| Simple ER diagrams | Diagrams needing cloud-provider icons |
| Decision trees | Diagrams with > 15 components |

## Pelican Integration

### Option 1: Inline with pelican-mermaid plugin

If the `pelican-mermaid` plugin is installed, use fenced code blocks:

````markdown
```mermaid
graph TD
    A[User] --> B[Front Door]
    B --> C[App Service]
```
````

### Option 2: Pre-rendered SVG

Generate SVG via Mermaid CLI and embed as image:

```bash
npx -p @mermaid-js/mermaid-cli mmdc -i diagram.mmd -o content/images/<slug>/diagram.svg
```

Then reference in the post:
```markdown
![Diagram description](images/<slug>/diagram.svg)
```

## Diagram Types & Syntax

### Flowchart (Top-Down)

```mermaid
graph TD
    A[Start] --> B{Decision}
    B -->|Yes| C[Action 1]
    B -->|No| D[Action 2]
    C --> E[End]
    D --> E
```

### Flowchart (Left-Right)

```mermaid
graph LR
    A[Client] --> B[Load Balancer]
    B --> C[App Server 1]
    B --> D[App Server 2]
    C --> E[(Database)]
    D --> E
```

### Sequence Diagram

```mermaid
sequenceDiagram
    participant U as User
    participant A as App Service
    participant D as Cosmos DB
    U->>A: HTTP Request
    A->>D: Query data
    D-->>A: Return results
    A-->>U: HTTP Response
```

### State Diagram

```mermaid
stateDiagram-v2
    [*] --> Pending
    Pending --> Running: start
    Running --> Succeeded: complete
    Running --> Failed: error
    Failed --> Pending: retry
    Succeeded --> [*]
```

### Gantt Chart (for timelines)

```mermaid
gantt
    title Project Timeline
    dateFormat YYYY-MM-DD
    section Phase 1
    Research       :a1, 2026-03-01, 7d
    Implementation :a2, after a1, 14d
    section Phase 2
    Testing        :b1, after a2, 7d
    Deployment     :b2, after b1, 3d
```

## Styling Rules

### Node Shapes

| Shape | Syntax | Use for |
| ----- | ------ | ------- |
| Rectangle | `[Text]` | Services, components |
| Rounded | `(Text)` | Processes, actions |
| Diamond | `{Text}` | Decisions |
| Cylinder | `[(Text)]` | Databases |
| Stadium | `([Text])` | Start/End |
| Hexagon | `{{Text}}` | Conditions |

### Color Theming (Azure-aligned)

```mermaid
graph TD
    classDef azure fill:#0078D4,stroke:#005A9E,color:#fff
    classDef data fill:#7FBA00,stroke:#5E8A00,color:#fff
    classDef security fill:#DD344C,stroke:#B02A3D,color:#fff
    classDef monitoring fill:#E7157B,stroke:#B81162,color:#fff

    A[App Service]:::azure --> B[(Cosmos DB)]:::data
    A --> C[Key Vault]:::security
    A --> D[Monitor]:::monitoring
```

### Guidelines

- Max 15 nodes per diagram. Split complex flows into multiple diagrams.
- Use descriptive node labels (not abbreviations).
- Add edge labels for protocols/actions: `-->|HTTPS:443|`
- Use consistent direction: `TD` for hierarchies, `LR` for flows.
- Keep node IDs short but meaningful: `app`, `db`, `lb` (not `a1`, `b2`).
