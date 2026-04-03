---
name: translation-glossary
description: Japanese-English translation glossary for technical blog posts. Ensures consistent terminology across ja-jp and en-us bilingual articles. Use when translating research reports into blog posts or reviewing translated content.
metadata:
  author: takumiseo
  version: "1.0"
---

# Translation Glossary Skill

Terminology glossary for consistent ja-jp ↔ en-us translation in this blog.

## Usage

When translating content between Japanese and English:
1. Check this glossary for established translations.
2. Use the listed term consistently throughout the article.
3. If a term is not listed, add it after establishing the translation.

## Azure Services & Features

| Japanese | English | Notes |
| -------- | ------- | ----- |
| 仮想マシン | Virtual Machine (VM) | |
| 仮想ネットワーク | Virtual Network (VNet) | |
| リソースグループ | Resource Group | |
| サブスクリプション | Subscription | |
| 可用性ゾーン | Availability Zone (AZ) | |
| マネージド ID | Managed Identity | |
| サービスプリンシパル | Service Principal | |
| キーコンテナー | Key Vault | |
| ストレージアカウント | Storage Account | |
| コンテナーレジストリ | Container Registry | |
| ロードバランサー | Load Balancer | |
| アプリケーションゲートウェイ | Application Gateway | |
| プライベートエンドポイント | Private Endpoint | |
| ネットワークセキュリティグループ | Network Security Group (NSG) | |
| 診断設定 | Diagnostic Settings | |
| アクティビティログ | Activity Log | |
| プラットフォームメトリクス | Platform Metrics | |
| リソースログ | Resource Logs | |
| マネージド Prometheus | Azure Monitor managed service for Prometheus | フルネームを初出時に使用 |
| マネージド Grafana | Azure Managed Grafana | |

## Monitoring & Observability

| Japanese | English | Notes |
| -------- | ------- | ----- |
| 監視 | Monitoring | |
| 可観測性 | Observability | |
| メトリクス | Metrics | |
| ログ | Logs | |
| トレース | Traces | |
| アラート | Alert | |
| アラートルール | Alert Rule | |
| アクショングループ | Action Group | |
| ダッシュボード | Dashboard | |
| ブック / ワークブック | Workbook | Azure Monitor Workbooks |
| データ収集ルール | Data Collection Rule (DCR) | |
| データ収集エンドポイント | Data Collection Endpoint (DCE) | |
| 保持期間 | Retention Period | |
| サンプリング | Sampling | |
| 取り込み | Ingestion | |
| クエリ | Query | |

## FinOps & Cost

| Japanese | English | Notes |
| -------- | ------- | ----- |
| コスト最適化 | Cost Optimization | |
| 予約 | Reservation | Azure Reservations |
| 節約プラン | Savings Plan | |
| 従量課金 | Pay-as-you-go / Consumption | |
| 要求ユニット | Request Units (RU) | Cosmos DB |
| スループット | Throughput | |
| 課金 | Billing | |
| 見積もり | Estimate / Sizing | |
| 料金レベル | Pricing Tier | |

## Architecture & Design

| Japanese | English | Notes |
| -------- | ------- | ----- |
| 構成案 | Architecture Proposal | |
| 構成図 | Architecture Diagram | |
| 冗長化 | Redundancy | |
| 高可用性 | High Availability (HA) | |
| 災害復旧 | Disaster Recovery (DR) | |
| スケーラビリティ | Scalability | |
| スケールアウト | Scale Out | |
| スケールアップ | Scale Up | |
| データ重複 | Data Duplication | |
| 二重収集 | Double Ingestion | |
| パーティションキー | Partition Key | |

## AKS / Kubernetes

| Japanese | English | Notes |
| -------- | ------- | ----- |
| コントロールプレーン | Control Plane | |
| ノードプール | Node Pool | |
| ポッド | Pod | |
| ワークロード | Workload | |
| 名前空間 | Namespace | |
| コンテナーインサイト | Container Insights | |
| イングレスコントローラー | Ingress Controller | |

## General Technical Terms

| Japanese | English | Notes |
| -------- | ------- | ----- |
| 実現性 | Feasibility | |
| 注意点 | Caveats / Considerations | |
| 前提 | Prerequisites / Assumptions | |
| 権限 | Permissions | RBAC context |
| 根拠 | Evidence / Reference | |
| 手順 | Procedure / Steps | |
| 構築 | Build / Deploy / Provision | Context-dependent |
| 検証 | Verification / Validation | |
| 整理 | Organize / Summarize | |

## Translation Guidelines

1. **Service names**: Keep Azure service names in English even in Japanese text (e.g., 「Azure Monitor」not「アジュールモニター」).
2. **First mention**: On first mention of a technical term in Japanese, include the English in parentheses: `可観測性（Observability）`.
3. **Abbreviations**: Spell out on first use, then abbreviate: `ネットワークセキュリティグループ (NSG)` → subsequent uses: `NSG`.
4. **Consistency**: Use the same translation throughout a single article. Do not alternate between synonyms.
5. **Proper nouns**: Microsoft product names are never translated: Azure Monitor, Entra ID, Cosmos DB.
