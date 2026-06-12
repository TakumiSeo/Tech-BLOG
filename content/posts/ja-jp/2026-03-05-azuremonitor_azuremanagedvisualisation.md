Title: AKS 監視構成案レビュー（Azure Monitor / Managed Prometheus / Azure Managed Grafana / New Relic）
Date: 2026-03-05
Slug: azuremonitor_azuremanagedvisualisation
Lang: ja-jp
Category: notebook
Tags: azure, azure-monitor, aks, prometheus, grafana, new-relic, observability
Summary: お客様提示の「案1〜3」について、Azure Monitor / Azure Monitor managed service for Prometheus / Azure Managed Grafana / Azure Native New Relic Service の観点で実現性・注意点・コスト最適化ポイントを整理（Microsoft Learn 根拠のみ）。


## 0. このメモの目的と前提

お客様から提示された 3 つの監視構成案（案1〜3）について、主に **Azure 側の観点**（Azure Monitor と Azure のマネージド監視サービス）で、次の観点を整理します。

- 実現性（接続として成立するか）
- 権限（RBAC）/ ネットワーク（Private Link 等）
- データ重複（不要な二重収集）とコスト
- AKS の監視でハマりやすいログ種別（特に control plane ログ）

制約: **事実は Microsoft Learn 記載を根拠**にし、外部情報（ベンダー独自ドキュメント等）や推測に依存しない記述にしています。

> 注: 本稿は「設計レビューの論点整理」です。費用試算は、実際の収集量（ログ量/メトリクスのサンプル数/クエリ量）と保持期間設定に依存するため、別途見積もりが必要です。

---

## 1. 先に押さえる：Azure Monitor のデータ種別と保持/課金の勘所

### 1.1 メトリクス（Platform metrics / Prometheus metrics）

- **Platform metrics**
	- Azure リソースのプラットフォームメトリクスは「自動収集・設定不要・標準メトリクスは無償」とされています。
	- 保持期間は **93日**。
	- ただし、Azure portal のメトリクスチャートは「1つのチャートで最大 30 日分まで」など表示/クエリ上の制限があります。
	- 参照: 
		- https://learn.microsoft.com/azure/azure-monitor/metrics/data-platform-metrics
		- https://learn.microsoft.com/azure/azure-monitor/metrics/data-platform-metrics#retention-of-metrics

- **Prometheus metrics（Azure Monitor managed service for Prometheus）**
	- 収集した Prometheus メトリクスは **Azure Monitor workspace** に格納されます。
		- 保持期間は **最長 18 か月**で、保存自体の料金はかからず、課金は主に「取り込み（ingestion）とクエリ（query）」ベースです。
		- Prometheus メトリクスに対する PromQL クエリは、1 回のクエリで **最大 32 日間**の期間に制限されます。
	- 参照:
		- https://learn.microsoft.com/azure/azure-monitor/essentials/prometheus-metrics-overview


### 1.2 ログ（Azure Monitor Logs / Log Analytics）

- AKS の **Container insights** や **AKS control plane/resource logs（診断設定）** で Log Analytics ワークスペースへ送ると、ログの取り込み量に応じてコストが増えます。
- AKS control plane ログは Azure Monitor の **resource logs** として実装され、診断設定で Log Analytics などへ送ります。
	- 参照: https://learn.microsoft.com/azure/aks/monitor-aks#aks-control-planeresource-logs

---

## 2. 案1〜3レビュー（Azure 側の論点）

ここでは「お客様の図（提案1〜3）で描かれている接続」を前提に、**その接続が Azure の機能として成立するか**、成立させる際の注意点を整理します。

### 図: 推奨監視アーキテクチャ（例）

```mermaid
flowchart TB
  subgraph Application
    APP[Application]
  end

  subgraph AKS
    AKS_WORKLOADS[AKS workloads]
    AKS_CONTROL_PLANE[AKS control plane logs]
  end

  subgraph Azure_Monitor
    AMW[Azure Monitor workspace (Prometheus metrics)]
    LA[Log Analytics workspace (Logs)]
    AMM[Azure Monitor Metrics (platform metrics)]
  end

  subgraph Azure_Resources
    AZR[Storage / Network / other Azure resources]
  end

  NR[New Relic (APM)]

  APP -->|OTEL| NR
  AKS_WORKLOADS -->|Managed Prometheus| AMW
  AKS_WORKLOADS -->|Container Insights (Logs & Events only)| LA
  AKS_CONTROL_PLANE -->|Diagnostic settings| LA
  AZR -->|Platform metrics| AMM
  AZR -->|Diagnostic settings (resource logs)| LA
```

### 図: 案1〜3のデータフロー（概念図）

```mermaid
flowchart TB
  subgraph Sources
    AKS_WORKLOADS[AKS workloads]
    AKS_RESOURCE_LOGS[AKS resource logs]
    AZ_RESOURCES[Other Azure resources]
  end

  subgraph Azure_Monitor
    AM_METRICS[Platform metrics]
    LA[Log Analytics workspace (Logs)]
    AMW[Azure Monitor workspace (Prometheus metrics)]
  end

  AMG[Azure Managed Grafana]
  NR[New Relic]

  %% Ingestion / export
  AZ_RESOURCES -->|Platform metrics| AM_METRICS
  AKS_WORKLOADS -->|Container Insights| LA
  AKS_RESOURCE_LOGS -->|Diagnostic settings| LA
  AKS_WORKLOADS -->|Managed Prometheus| AMW

  %% Visualization (Grafana queries)
  AMG -->|Query| AM_METRICS
  AMG -->|Query| LA
  AMG -->|Query| AMW

  %% New Relic paths
  AKS_WORKLOADS -->|OTEL| NR
  AZ_RESOURCES -.->|Diagnostic settings (partner)| NR
```

接続の論点（チェックリスト・抜粋）

| 接続 | 何で繋ぐか（Azure 側の機能） | 主な確認ポイント |
|---|---|---|
| Azure Managed Grafana → Azure Monitor（メトリクス/ログ） | Azure Managed Grafana の Azure Monitor データソース | Grafana 側 ID の RBAC（読み取りロール）／必要なら managed private endpoint（Private Link） |
| Azure Managed Grafana → Azure Monitor workspace（Prometheus） | Azure Monitor workspace 連携（Standard tier 前提） | Grafana のマネージド ID に Monitoring Data Reader を付与／ネットワーク要件（必要なら private） |
| AKS（workloads）→ Log Analytics | Container insights（Logs and events など） | 収集範囲を絞って重複を避ける（特に Prometheus を併用する場合） |
| AKS（control plane/resource logs）→ Log Analytics | 診断設定（resource logs の出力） | 収集カテゴリ（kube-audit 等）の選定とコスト影響、診断設定の上限（1 リソース最大 5） |
| Azure resource logs → New Relic | 診断設定の宛先（partner solution） | 既存の診断設定との競合/上限、二重転送による追加課金リスク |

参照（Learn）:
- Azure Managed Grafana と Azure Monitor: https://learn.microsoft.com/azure/azure-monitor/visualize/visualize-use-managed-grafana-how-to
- Azure Monitor workspace と Azure Managed Grafana: https://learn.microsoft.com/azure/managed-grafana/how-to-connect-azure-monitor-workspace
- Azure Managed Grafana の private 接続: https://learn.microsoft.com/azure/managed-grafana/how-to-connect-to-data-source-privately
- 診断設定（宛先/上限）: https://learn.microsoft.com/azure/azure-monitor/essentials/diagnostic-settings , https://learn.microsoft.com/azure/azure-monitor/fundamentals/service-limits#diagnostic-settings
- AKS control plane/resource logs: https://learn.microsoft.com/azure/aks/monitor-aks#aks-control-planeresource-logs
- Kubernetes 監視のコスト最適化（重複回避）: https://learn.microsoft.com/azure/azure-monitor/containers/best-practices-containers#cost-optimization

---

### 案1: Cost Effective Design（New Relic + Azure Monitor + Managed Prometheus + Azure Managed Grafana）

図の読み取り（意図）: 

- アプリ/AKS から OTEL で New Relic（APM）
- AKS の Prometheus メトリクスは Azure Monitor managed service for Prometheus（= Azure Monitor workspace へ格納）
- Azure リソース（Storage/Network 等）は Azure Monitor Metrics（プラットフォームメトリクス）
- 可視化は Azure Managed Grafana（Azure Monitor と Prometheus の両方をクエリ）

**接続の実現性**

- Azure Managed Grafana で Azure Monitor を可視化する構成（Azure Monitor データソース）は Learn で手順が示されています。
	- 参照: https://learn.microsoft.com/azure/azure-monitor/visualize/visualize-use-managed-grafana-how-to

- Azure Monitor managed service for Prometheus で収集した Prometheus メトリクスは Azure Monitor workspace に格納され、Azure Managed Grafana から参照できます。
	- 参照:
		- https://learn.microsoft.com/azure/azure-monitor/essentials/prometheus-metrics-overview
		- https://learn.microsoft.com/azure/managed-grafana/how-to-connect-azure-monitor-workspace

**RBAC（最低限ここを押さえる）**

- Azure Managed Grafana が Azure Monitor データ（メトリクス/ログ）を読むため、Grafana の ID（マネージド ID など）に対象スコープの読み取り権限が必要です。
	- 参照: https://learn.microsoft.com/azure/azure-monitor/visualize/visualize-use-managed-grafana-how-to

- Azure Monitor workspace（Prometheus 格納先）から Prometheus データを収集するため、Azure Monitor workspace 側で Grafana のマネージド ID に **Monitoring Data Reader** を割り当てます（Standard tier 前提）。
	- 参照: https://learn.microsoft.com/azure/managed-grafana/how-to-connect-azure-monitor-workspace

**ネットワーク（プライベート接続が必要な場合）**

- プライベート接続が必要な場合、Azure Managed Grafana 側で **managed private endpoint** を作成してデータソースへ接続する手順が示されています。
	- 参照: https://learn.microsoft.com/azure/managed-grafana/how-to-connect-to-data-source-privately

**コスト/重複収集（この案で一番ハマりやすい点）**

- Kubernetes 監視のベストプラクティスでは、Managed Prometheus を使う場合に **Prometheus メトリクスを Log Analytics へも送る構成は冗長になり得る**こと、必要に応じて Container insights を **Logs and events のみ**に絞ることが記載されています。
	- 参照: https://learn.microsoft.com/azure/azure-monitor/containers/best-practices-containers#cost-optimization

- Platform metrics は 93 日保持で「設定不要・追加コストなし」とされています。一方で、Prometheus メトリクスは最長 18 か月保持、課金は ingestion/query ベースです。
	- 参照:
		- https://learn.microsoft.com/azure/azure-monitor/metrics/data-platform-metrics#retention-of-metrics
		- https://learn.microsoft.com/azure/azure-monitor/essentials/prometheus-metrics-overview

**補足（図の“矢印”の誤解を避ける）**

- Azure Managed Grafana は「Azure Monitor / Azure Monitor workspace（Prometheus）を **クエリして表示**する」形が基本で、Grafana 自体がデータを保管するコンポーネントではありません。
	- 参照: https://learn.microsoft.com/azure/azure-monitor/visualize/visualize-use-managed-grafana-how-to

---

### 案2: Convenient for Visualization and Troubleshooting（New Relic + Azure Monitor + Azure Managed Grafana、Managed Prometheus なし）

図の読み取り（意図）:

- Azure リソースのメトリクス/ログを Azure Monitor で集約し、Azure Managed Grafana で可視化
- AKS は（Managed Prometheus なしのため）Prometheus メトリクスは使わない

**接続の実現性**

- Azure Managed Grafana で Azure Monitor データソースを使って Azure Monitor のデータを可視化する手順が示されています。
	- 参照: https://learn.microsoft.com/azure/azure-monitor/visualize/visualize-use-managed-grafana-how-to

**注意点（AKS の監視深度）**

- この案は「Azure リソースのプラットフォームメトリクス（設定不要）」中心でシンプルに始めやすい一方、AKS の詳細メトリクス（Prometheus 前提のダッシュボード/クエリ資産）を活用しづらくなります。
- AKS を深く見る必要がある場合、Managed Prometheus（案1の要素）を後から追加する可能性を見越して、RBAC/ネットワーク/コスト設計（重複収集回避）を先に整理しておくのが安全です。
	- 参照: https://learn.microsoft.com/azure/azure-monitor/essentials/prometheus-metrics-overview

---

### 案3: Azure Monitor のログを New Relic に連携（Azure Native New Relic Service / パートナー連携で集約）

**接続の実現性（Azure 側の範囲）**

- Azure Monitor の診断設定は、Log Analytics / Storage / Event Hubs に加えて **partner solution** を宛先として選べます。
	- 参照: https://learn.microsoft.com/azure/azure-monitor/essentials/diagnostic-settings#destinations

- Azure Native New Relic Service（Azure portal 統合）に関して、Learn では「対象リソースの診断設定に New Relic 設定があるか」を確認する手順が示されています。
	- 参照: https://learn.microsoft.com/azure/partner-solutions/new-relic/troubleshoot#logs-arent-being-sent-to-new-relic

**重要な制約（診断設定/パートナー連携）**

- 診断設定は **1 リソースあたり最大 5 個**という制約があります（New Relic 連携でもここに制約されます）。
- パートナー連携では「メトリクスを診断設定で送る」ことがサポートされない旨が、トラブルシュート記事に明記されています（= ログ中心の設計になる）。
	- 参照: https://learn.microsoft.com/troubleshoot/azure/partner-solutions/log-limitations

**運用上の注意（ロック/重複課金リスク）**

- Azure Native New Relic Service のトラブルシュートでは、リソース/リソースグループにロックがあると、New Relic リソースを無効化しても診断設定が残りログ転送が継続し得る、といった注意点が挙げられています。
	- 参照: https://learn.microsoft.com/azure/partner-solutions/new-relic/troubleshoot#diagnostic-settings-are-active-even-after-disabling-the-new-relic-resource-or-applying-necessary-tag-rules

- 複数サブスクリプション監視や既存 New Relic リソースがある場合、重複したログ転送により **追加課金につながる**可能性がある旨が記載されています。
	- 参照: https://learn.microsoft.com/azure/partner-solutions/new-relic/manage#monitor-multiple-subscriptions

---

## 3. AKS control plane/resource logs（診断設定）での注意点（全案共通）

AKS の control plane ログは、Azure Monitor の **resource logs** として提供され、診断設定で Log Analytics へ送るのが基本です。

- 収集カテゴリ例（Learn に列挙）
	- `kube-apiserver`
	- `kube-audit`
	- `kube-audit-admin`
	- `kube-controller-manager`
	- `kube-scheduler`
	- `cluster-autoscaler`
	- `guard`
	- 参照: https://learn.microsoft.com/azure/aks/monitor-aks#aks-control-planeresource-logs

- コスト注意（特に `kube-audit`）
	- Learn では、`kube-audit` は **大量のデータを生成し高コストになり得る**ため、不要であれば無効化し、必要時はより低容量の `kube-audit-admin` を使うことが推奨されています。
	- 参照: https://learn.microsoft.com/azure/aks/monitor-aks#aks-control-planeresource-logs

---

## 4. お客様質問（①〜③）への回答の形（テンプレ）

### ① 各案における考慮点/注意点

- 監視対象（AKS/アプリ/周辺 Azure リソース）に対し、
	- メトリクスは「Platform metrics なのか Prometheus なのか」
	- ログは「Container insights（コンテナログ・イベント）なのか control plane logs なのか」
	を分けて、**保持期間（93日 vs 18か月）と課金（標準メトリクス無償 / Prometheus は ingestion+query / Logs は取り込み量）**に合わせて設計します。
	- 参照: https://learn.microsoft.com/azure/azure-monitor/fundamentals/cost-usage#pricing-model

- Managed Prometheus を使う場合は、Container insights で Prometheus メトリクスを Log Analytics に送る構成は冗長になり得るため避けます。
	- 参照: https://learn.microsoft.com/azure/azure-monitor/containers/best-practices-containers#cost-optimization

### ② 接続（Azure Monitor ↔ Azure Managed Grafana / Managed Prometheus ↔ Azure Managed Grafana）の注意点

Azure Managed Grafana は「データを受け取って保管する」よりも、**データソースをクエリして表示する**ため、接続の論点は基本的に **(1) ID/RBAC** と **(2) ネットワーク到達性** に集約されます。

#### ②-1. Azure Managed Grafana → Azure Monitor（メトリクス/ログ）

- **接続の形**: Azure Managed Grafana の **Azure Monitor データソース**が、Azure Monitor（メトリクス/ログ）をクエリします。
- **RBAC の考え方**:
	- Grafana 側の ID（マネージド ID など）に、Azure Monitor を読むための **読み取り権限**が必要です。
	- 「どのスコープに付与するか」が重要で、一般に “見せたいリソース/リソースグループ/サブスクリプション” に対して付与設計します。
	- 具体的なロール/付与例は Learn の手順に従います。
- **運用上の注意**:
	- 「メトリクスだけ見たい」のか「ログ（Log Analytics）もダッシュボードに出したい」のかで、必要権限とデータソースの設定が変わります。

参照:
- https://learn.microsoft.com/azure/azure-monitor/visualize/visualize-use-managed-grafana-how-to

#### ②-2. Azure Managed Grafana → Azure Monitor workspace（Managed Prometheus の格納先）

- **接続の形**: Managed Prometheus のメトリクスは **Azure Monitor workspace** に格納され、Azure Managed Grafana から接続できます。
- **Standard tier 前提**: Azure Monitor workspace 連携は Standard tier を前提にした手順が示されています。
- **RBAC（ここは具体に決めやすい）**:
	- Azure Monitor workspace に対して、Grafana のマネージド ID に **Monitoring Data Reader** を割り当てます。
- **クエリ面の注意**:
	- PromQL クエリの期間に制限（1 回のクエリで最大 32 日）があります。長期間分析はクエリ分割や設計で吸収が必要です。

参照:
- https://learn.microsoft.com/azure/managed-grafana/how-to-connect-azure-monitor-workspace
- https://learn.microsoft.com/azure/azure-monitor/essentials/prometheus-metrics-overview

#### ②-3. プライベート接続（Private Link）が必要な場合

- **接続の形**: Azure Managed Grafana 側で **managed private endpoint** を作り、対象データソースへ **Private Link** 経由で到達させます。
- **注意点**:
	- 「Grafana から見たいデータソース」が Private Link 対応であること、そして接続承認フロー（相手側の承認作業）が必要になる点を事前に確認します。

参照:
- https://learn.microsoft.com/azure/managed-grafana/how-to-connect-to-data-source-privately

#### ②-4. ありがちな落とし穴（接続が“成立しても”ハマる）

- **重複収集**: Managed Prometheus を使う場合に、Prometheus メトリクスを Log Analytics にも送ると冗長になり得ます（コスト/運用負荷増）。
	- 参照: https://learn.microsoft.com/azure/azure-monitor/containers/best-practices-containers#cost-optimization
- **診断設定の枠が埋まる**: 診断設定は 1 リソースあたり最大 5 個です。案3（partner solution）を追加する場合、既存の診断設定と競合しやすいため先に棚卸しします。
	- 参照:
		- https://learn.microsoft.com/azure/azure-monitor/essentials/diagnostic-settings
		- https://learn.microsoft.com/azure/azure-monitor/fundamentals/service-limits#diagnostic-settings

### ③ 推奨リファレンス（Microsoft Learn）

- AKS の監視（control plane logs のカテゴリ/注意点含む）
	- https://learn.microsoft.com/azure/aks/monitor-aks
- Kubernetes 監視のベストプラクティス（特にコスト最適化/二重収集回避）
	- https://learn.microsoft.com/azure/azure-monitor/containers/best-practices-containers
- Azure Monitor managed service for Prometheus（概要）
	- https://learn.microsoft.com/azure/azure-monitor/essentials/prometheus-metrics-overview
- Azure Managed Grafana（Azure Monitor workspace 連携）
	- https://learn.microsoft.com/azure/managed-grafana/how-to-connect-azure-monitor-workspace
- Azure Monitor Metrics（保持 93 日・Prometheus 18 か月、Portal 30 日制限など）
	- https://learn.microsoft.com/azure/azure-monitor/metrics/data-platform-metrics
- Azure Monitor の課金モデル（標準メトリクス無償、Prometheus は ingestion/query など）
	- https://learn.microsoft.com/azure/azure-monitor/fundamentals/cost-usage#pricing-model
- 診断設定（宛先に partner solution を含む）
	- https://learn.microsoft.com/azure/azure-monitor/essentials/diagnostic-settings
- Azure Native New Relic Service（概要/運用）
	- https://learn.microsoft.com/azure/partner-solutions/new-relic/overview
	- https://learn.microsoft.com/azure/partner-solutions/new-relic/manage
	- https://learn.microsoft.com/azure/partner-solutions/new-relic/troubleshoot

---

## 付録：監視設計ヒアリングシート（案）

以下は「設計の前提を揃える」ためのヒアリング項目です。例はあくまで記入例であり、数値は概算でも構いません。

### A. 方針・運用（優先順位 / 体制 / 目標）

| # | ヒアリング項目 | 確認したい内容 | 回答欄 |
|---:|---|---|---|
| 1 | 監視の優先順位 | 可用性・性能・セキュリティ・コストのうち、優先度はどれか | |
| 2 | 対象範囲（環境/リソース） | Prod/Stg/Dev のどこまで対象にするか。AKS 以外の対象リソースは何か | |
| 3 | SLO/SLI と運用目標 | 可用性目標、応答性能目標、MTTD/MTTR 目標はあるか | |
| 4 | アラート運用体制 | 通知先、当番体制、エスカレーションルール、夜間対応有無 | |
| 5 | ログ保持・監査要件 | テーブル別の必要保持期間、監査証跡要件、改ざん防止要件 | |
| 6 | クエリ利用実態 | 誰が、どのテーブルを、どれくらいの頻度で検索するか | |
| 7 | コスト目標と現状 | 現在の月額（New Relic/Azure Monitor/Grafana）と削減目標（率/金額） | |
| 11 | 監視データの利用者/権限 | 運用/開発/監査など、閲覧者ごとのアクセス範囲・分離要件（最小権限） | |
| 12 | インシデント運用連携 | チケット起票先（ITSM）、一次切り分け担当、Runbook/自動復旧の可否 | |
| 13 | ダッシュボード要件 | NOC/運用/開発/経営向けの必須 KPI、既存資産（Grafana/Workbook）の有無 | |
| 14 | 重複転送ポリシー | Log Analytics と New Relic の二重転送/二重保管を許容するか（対象データは何か） | |
| 15 | アラート品質方針 | ノイズ許容度、抑止（メンテ時間帯）、集約/相関、重要度定義 | |

### B. 技術・構成（収集方針 / セキュリティ / ネットワーク / 標準化）

| # | ヒアリング項目 | 確認したい内容 | 回答欄 |
|---:|---|---|---|
| 8 | AKS ログ方針 | kube-audit 必須か、kube-audit-admin 切替可否、ContainerLogV2 移行可否 | |
| 9 | セキュリティ/ネットワーク制約 | Private Link 必須有無、データ越境制約、Managed Identity 利用可否 | |
| 10 | 標準化・自動化方針 | Azure Policy / IaC（Bicep/Terraform）で設定を強制・テンプレ化するか | |
| 16 | ワークスペース設計 | 監視基盤を単一/環境別/サブスク別で分ける方針、リージョン配置、越境境界 | |
| 17 | ネットワーク経路の制約詳細 | インターネット送信可否、プロキシ要否、FW 許可方式（FQDN/宛先固定等） | |
| 18 | 収集範囲の粒度 | 対象クラスタ数、ノードプール、対象 Namespace/Workload、除外したいログ種別 | |
| 19 | 変更管理 | 監視設定変更の承認フロー、IaC 反映頻度、ロールバック要件 | |

### C. 追加で確認したい数値項目（コスト試算用）

| 項目 | 例 | 回答欄 |
|---|---|---|
| 日次取り込み量（総量） | 100 GB/日 | |
| 主要テーブルごとの取り込み量 | ContainerLogV2=40 GB/日 など | |
| Basic/Aux テーブルの想定クエリ回数 | 1日20回 | |
| クエリ1回あたりの平均スキャン量 | 2 GB/回 | |
| 変更前後で比較したい期間 | 直近3か月 | |
| クラスタ規模（概数） | クラスタ数/ノード数（通常・ピーク）/Pod数/Namespace数 | |
| ログ負荷（概数） | ノードあたり logs/sec、ピーク時間帯、平均ログ行サイズ（KB）、マルチライン有無 | |
| メトリクス規模（概数） | 対象数（node/pod/ingress等）、scrape interval、active series の概算 | |
| クエリ/ダッシュボード負荷 | 同時利用者数、ダッシュボード自動更新間隔、アラート評価頻度 | |
| テーブル設計の前提 | Analytics/Basic/Aux の使い分け方針（対象テーブル、保持期間） | |

ｋ