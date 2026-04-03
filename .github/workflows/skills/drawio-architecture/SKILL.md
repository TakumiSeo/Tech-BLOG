---
name: drawio-architecture
description: Generate draw.io XML architecture diagrams for blog posts. Provides cloud-provider icon shape references, layout rules, container styles, and troubleshooting guidance for producing well-formed .drawio files. Use when creating architecture diagrams, system design visualizations, or infrastructure diagrams for Azure, AWS, or GCP.
metadata:
  author: takumiseo
  version: "1.0"
---

# draw.io Architecture Diagram Skill

Generate draw.io XML architecture diagrams from research or design content. The output is a `.drawio` file placed under `content/images/<slug>/architecture.drawio`.

## Prerequisites

- VS Code extension: [Draw.io Integration](https://marketplace.visualstudio.com/items?itemName=hediet.vscode-drawio) (`hediet.vscode-drawio`)

## Procedure

1. Read the source content (research report or design doc) to understand the architecture.
2. Identify key components, relationships, and logical groupings (e.g., network layers, regions, resource groups).
3. Create the output directory: `content/images/<slug>/`
4. Generate the draw.io XML file: `content/images/<slug>/architecture.drawio`
5. Verify the generated XML is well-formed by reading it back.

## draw.io XML Structure

Every `.drawio` file MUST follow this structure:

```xml
<mxfile host="app.diagrams.net" agent="copilot">
  <diagram id="architecture" name="Architecture">
    <mxGraphModel dx="1422" dy="762" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="2400" pageHeight="1800" math="0" shadow="0">
      <root>
        <mxCell id="0"/>
        <mxCell id="1" parent="0"/>
        <!-- Components go here -->
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>
```

## Layout Principles

- **Canvas size**: 2400×1800px for complex diagrams, 1200×900px for simple ones (< 5 components)
- **Component spacing**: Minimum 100px between components
- **Hierarchical layout**: Top-to-bottom flow (external → network → compute → data)
- **Grouping**: Use parent containers for logical groupings (VNet/VPC, Subnets, Resource Groups)
- **Left-to-right**: Place redundant/HA components side by side
- **Avoid overlapping lines**: Use staggered Y-coordinates for parallel components
- **Label connections**: Include protocol and port where relevant (e.g., `HTTPS:443`)
- **Max components**: 15-20 per diagram. Split into multiple diagrams if needed

## Connection Line Styles

### Color by purpose

| Purpose             | Color                     |
| ------------------- | ------------------------- |
| External (HTTPS)    | `strokeColor=#0066CC`     |
| Internal (HTTP)     | `strokeColor=#ED7100`     |
| Database            | `strokeColor=#C925D1`     |
| Security/management | `strokeColor=#DD344C`     |
| Monitoring          | `strokeColor=#E7157B`     |
| Storage             | `strokeColor=#7AA116`     |

### Edge style by type

| Type       | Style                                  |
| ---------- | -------------------------------------- |
| External   | `edgeStyle=orthogonalEdgeStyle`        |
| Internal   | `edgeStyle=curved;curved=1`           |
| Database   | `edgeStyle=elbowEdgeStyle`            |

## Azure Icon Shapes (mxgraph.azure.*)

### Compute

| Service             | Shape                                      |
| ------------------- | ------------------------------------------ |
| Virtual Machine     | `shape=mxgraph.azure.virtual_machine`      |
| AKS                 | `shape=mxgraph.azure.kubernetes`           |
| App Service         | `shape=mxgraph.azure.app_service`          |
| Functions           | `shape=mxgraph.azure.function_apps`        |
| Container Instances | `shape=mxgraph.azure.container_instances`  |

### Networking

| Service             | Shape                                         |
| ------------------- | --------------------------------------------- |
| Virtual Network     | `shape=mxgraph.azure.virtual_network`         |
| Load Balancer       | `shape=mxgraph.azure.load_balancer`           |
| Application Gateway | `shape=mxgraph.azure.application_gateway`     |
| Front Door          | `shape=mxgraph.azure.front_door`              |
| DNS Zone            | `shape=mxgraph.azure.dns`                     |
| NSG                 | `shape=mxgraph.azure.network_security_group`  |
| Private Endpoint    | `shape=mxgraph.azure.private_endpoint`        |

### Data

| Service         | Shape                                  |
| --------------- | -------------------------------------- |
| Cosmos DB       | `shape=mxgraph.azure.cosmos_db`        |
| SQL Database    | `shape=mxgraph.azure.sql_database`     |
| Storage Account | `shape=mxgraph.azure.storage`          |
| Redis Cache     | `shape=mxgraph.azure.cache_redis`      |

### Monitoring & Management

| Service              | Shape                                         |
| -------------------- | --------------------------------------------- |
| Azure Monitor        | `shape=mxgraph.azure.azure_monitor`           |
| Log Analytics        | `shape=mxgraph.azure.log_analytics`           |
| Application Insights | `shape=mxgraph.azure.application_insights`    |
| Key Vault            | `shape=mxgraph.azure.key_vaults`              |
| Managed Grafana      | `shape=mxgraph.azure.grafana`                 |

### Identity & Security

| Service          | Shape                                      |
| ---------------- | ------------------------------------------ |
| Entra ID         | `shape=mxgraph.azure.active_directory`     |
| Managed Identity | `shape=mxgraph.azure.managed_identities`   |

### Integration

| Service        | Shape                                    |
| -------------- | ---------------------------------------- |
| Event Hub      | `shape=mxgraph.azure.event_hubs`         |
| Service Bus    | `shape=mxgraph.azure.service_bus`        |
| API Management | `shape=mxgraph.azure.api_management`     |

## AWS Icon Shapes (mxgraph.aws4.*)

| Service      | Shape                                         |
| ------------ | --------------------------------------------- |
| EC2          | `shape=mxgraph.aws4.ec2`                      |
| ECS          | `shape=mxgraph.aws4.ecs`                      |
| EKS          | `shape=mxgraph.aws4.eks`                      |
| Lambda       | `shape=mxgraph.aws4.lambda_function`           |
| S3           | `shape=mxgraph.aws4.s3`                       |
| RDS          | `shape=mxgraph.aws4.rds`                      |
| CloudFront   | `shape=mxgraph.aws4.cloudfront`               |
| ALB          | `shape=mxgraph.aws4.elastic_load_balancing`    |
| VPC          | `shape=mxgraph.aws4.vpc`                      |
| Route53      | `shape=mxgraph.aws4.route_53`                 |
| ElastiCache  | `shape=mxgraph.aws4.elasticache`              |
| CloudWatch   | `shape=mxgraph.aws4.cloudwatch`               |

## Grouping Container Styles

### Azure

**Resource Group / VNet**:
```
style="rounded=1;whiteSpace=wrap;html=1;fillColor=#E6F2FA;strokeColor=#0078D4;dashed=0;verticalAlign=top;fontStyle=1;fontSize=14;"
```

**Subnet**:
```
style="rounded=1;whiteSpace=wrap;html=1;fillColor=#F0F0F0;strokeColor=#505050;dashed=1;verticalAlign=top;fontSize=12;"
```

### AWS

**Region**:
```
style="rounded=1;whiteSpace=wrap;html=1;fillColor=#E6F6F7;strokeColor=#00A4A6;verticalAlign=top;fontStyle=1;fontSize=14;"
```

**VPC**:
```
style="rounded=1;whiteSpace=wrap;html=1;fillColor=#E9F3E6;strokeColor=#248814;verticalAlign=top;fontSize=12;"
```

**Availability Zone**:
```
style="rounded=1;whiteSpace=wrap;html=1;strokeColor=#147EBA;dashed=1;verticalAlign=top;fontSize=12;"
```

## Troubleshooting Checklist

Before finalizing, verify:

- [ ] All components use proper cloud-provider icon shapes (not plain rectangles)
- [ ] No components overlap (check X/Y coordinates and sizes)
- [ ] Connection lines have labels (protocol:port)
- [ ] Lines are color-coded by purpose
- [ ] Grouping containers properly contain child components via `parent` attribute
- [ ] XML is well-formed (all tags closed, attributes quoted)

## Blog Post Integration

Reference the diagram in blog posts with:

```markdown
![Architecture](images/<slug>/architecture.drawio.svg)
```

If SVG is not supported by the site generator, export as PNG and use:

```markdown
![Architecture](images/<slug>/architecture.png)
```
