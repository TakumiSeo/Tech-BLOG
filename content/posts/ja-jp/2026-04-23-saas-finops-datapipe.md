Title: マルチクラウド/SaaS 請求データ可視化基盤 ご提案アジェンダ（スモールスタート: Azure → New Relic）
Date: 2026-04-23
Slug: saas-finops-datapipe
Lang: ja-jp
Category: notebook
Tags: finops, focus, new-relic, azure, cost-management, data-pipeline
Status: draft
Summary: 複数 SaaS / Cloud の請求データを FOCUS で統一し New Relic で横断可視化する基盤について、スモールスタート (Azure 先行) の方針合意を取るためのディスカッションアジェンダ。

# 1. 本日のゴールと目的

- **目的**: 複数 SaaS / Cloud の請求データを **FOCUS 形式** に統一し、**New Relic** で横断可視化する基盤の方針合意
- **本日のゴール**:
  - スモールスタートの範囲 (= Azure 先行) について合意
  - 次フェーズまでの意思決定事項を洗い出し
- **成功指標の仮置き**:
  - **日次**で New Relic に最新のコストデータが反映される
  - コスト按分に必要な粒度（サービス / タグ / プロジェクト）で NRQL 集計ができる

# 2. 全体骨格（To-Be アーキテクチャ：想定案）

本セクションは **想定 To-Be の位置づけ**。当日の議論で調整する前提で叩き台として提示する。

- 対象データソース: **Azure / New Relic / Akamai / PagerDuty**
- 統一フォーマット: **FOCUS**
  - ターゲット: **1.2**（`ProviderName` / `InvoiceId` / `PricingCategory` / `CommitmentDiscountStatus` 等が揃い、可視化時の自前マッピングが最小化される）
  - ただし **Azure Cost Management の FOCUS Export は 1.2 がまだ preview**。バージョン選定は次項の論点とする
- データレイヤー:
  - **Bronze**: 各ソースの生データを ADLS Gen2 に日付パーティションで保持
  - **Silver**: FOCUS スキーマに正規化（Parquet / Delta）
  - **Gold**: **FOCUS フォーマットで統合された、New Relic に送信可能な状態のデータ**（明細粒度を保持）。集計・加工は New Relic 側で NRQL により実施する
- 可視化・加工: **New Relic 側で NRQL により実施**（集計ロジックをパイプラインに固定化しない）
- 図: 別紙アーキテクチャ（draw.io）

## 2.1 【論点】FOCUS のバージョン選定

### 2.1.1 FOCUS 1.0 / 1.2 の位置づけ（FinOps Foundation 公式）

| 項目 | FOCUS 1.0 (GA) | FOCUS 1.2 (GA) |
| --- | --- | --- |
| 発表時期 | 2024/06 | 2025/06 |
| 主対象 | CSP 請求データ（AWS / Azure / GCP / OCI）横断 | CSP に加え **SaaS プラットフォーム**を正式に含む[^1] |
| 主な狙い | Cloud billing の共通言語確立 | **マルチ通貨 / 仮想通貨（トークン・クレジット）課金の表現** |
| 設計原則の言及 | — | §1.4.4 "foundational support for SaaS platforms, including normative columns for pricing currencies, effective cost, and contracted pricing in non-monetary units such as credits or tokens"[^1] |

### 2.1.2 1.2 で追加された主要カラム（SaaS 文脈）

1.2 で追加された 7 カラムのうち、SaaS コンテキストの中核は `PricingCurrency` 系 4 カラム[^2]。

| 概念 | 1.0（Billing 通貨建てのみ） | 1.2 で追加（Pricing 通貨建て） | SaaS での意味 |
| --- | --- | --- | --- |
| 通貨コード | `BillingCurrency` | **`PricingCurrency`** | "USD" / "JPY" 等に加え **"Tokens" / "Credits"** が入る |
| 定価 | `ListUnitPrice` | **`PricingCurrencyListUnitPrice`** | 元通貨での割引前単価 |
| 契約単価 | `ContractedUnitPrice` | **`PricingCurrencyContractedUnitPrice`** | 元通貨での交渉後単価 |
| 実効コスト | `EffectiveCost` | **`PricingCurrencyEffectiveCost`** | トークン/クレジット消費量そのもの |

1.2 ではさらに次も追加（SaaS 契約構造の明示に必要）[^2]:

- `InvoiceId`: 月次 invoice + 年次 prepay が混在する SaaS 契約の突合 ID
- `BillingAccountType` / `SubAccountType`: SaaS のテナント / ワークスペース等の階層区別

### 2.1.3 SaaS ごとの表現可否（1.0 vs 1.2）

| 対象 SaaS | 課金モデル | 1.0 で表現可能か | 1.2 で表現可能か |
| --- | --- | --- | --- |
| Azure / AWS / GCP | 金銭（USD 等）| ✅ | ✅ |
| New Relic | User / Host / GB ライセンス + USD 請求 | △（通貨単一の場合のみ）| ✅ |
| Akamai | 帯域 / リクエスト量 + USD 請求 | ✅ | ✅ |
| PagerDuty | User ライセンス + USD 請求 | ✅ | ✅ |
| Snowflake | **Credit 課金** | ❌（Credit 概念が不在）| ✅ `PricingCurrency="Credits"` |
| OpenAI / LLM SaaS | **Token 課金** | ❌ | ✅ `PricingCurrency="Tokens"` |

→ 本件スコープ（Azure / New Relic / Akamai / PagerDuty）は **全て 1.0 でも表現可能**。ただし将来 AI SaaS / Snowflake 等の追加可能性があるなら 1.2 前提が安全。

### 2.1.4 プロバイダー側の対応状況（2026/04 時点）

| プロバイダー | FOCUS 1.0 | FOCUS 1.2 |
| --- | --- | --- |
| Azure Cost Management Exports | **GA（1.0r2）** | **Preview** |
| AWS CUR 2.0 (Data Exports) | GA | GA |
| GCP Billing Detailed Export | 未ネイティブ（要変換） | 未ネイティブ |

→ **Azure 側の 1.2 は preview** が意思決定の最大論点。

### 2.1.5 採用方針の選択肢

| 案 | メリット | デメリット / リスク | 推奨シーン |
| --- | --- | --- | --- |
| **A. FOCUS 1.0 GA で固定** | Azure 側 GA、サポート対象。仕様安定 | 将来 SaaS 拡張時に 1.2 への再設計必要 | 本番運用を急ぐ / スコープを CSP + 金銭課金 SaaS に限定 |
| **B. FOCUS 1.2 preview を採用** | マルチ通貨 / 仮想通貨を最初から表現可能 | Azure 側仕様変更リスク、サポート範囲確認要 | AI / Snowflake 等の将来取り込みを見据える |
| **C. 1.0 ベース + 1.2 相当列を `x_` カスタム列で先行実装**（推奨）| Azure GA を維持しつつ、将来の 1.2 移行コストを最小化 | アダプタ層の実装・保守が必要 | 本件のように **SaaS 拡張を将来見据えつつ本番安定も必要**なケース |

### 2.1.6 本件の推奨（議論のたたき台）

- **Phase 1（Azure のみ）**: 案 A（FOCUS 1.0 GA）で開始。Azure ネイティブ Export をそのまま活用
- **Phase 2 以降**（New Relic / Akamai / PagerDuty 取り込み時）: Silver 層スキーマを **案 C に昇格**（`PricingCurrency`, `PricingCurrencyEffectiveCost` 等を `x_` 付きで先行導入）
- **1.2 GA 化時点**（Azure）で `x_` を外して正式 1.2 スキーマに移行

### 2.1.7 前提認識 — FOCUS 準拠は "ゴール" ではなく "共通語彙"

本件で取り扱う 4 ソースのうち、**FOCUS フォーマットでデータを直接出力できるのは Azure のみ**。New Relic / Akamai / PagerDuty は現時点で FOCUS ネイティブ出力を持たず、**各社独自スキーマからの変換処理を自前で実装する必要がある**。この事実はバージョン 1.0 / 1.2 のいずれを採用しても変わらない。

したがって本件の本質的な設計論点は「どちらのバージョンを選ぶか」ではなく、**変換層（Silver 層）の運用品質をどう担保するか**にある。FOCUS 準拠はあくまで "可視化の共通語彙" を揃えるための手段であり、到達目標ではない。

| 観点 | 本件での帰結 |
| --- | --- |
| データ取得 | 各 SaaS 固有の API / CSV / BigQuery 等からの取得処理を個別に実装・保守 |
| スキーマ変換 | 各ソースのネイティブスキーマ → FOCUS Mandatory カラム（`BilledCost`, `ChargePeriodStart/End`, `ServiceName`, `ProviderName` 等）へのマッピングを **個別設計** |
| 仕様変更追従 | 各 SaaS の請求スキーマは独立に進化する → **変更検知・リグレッションテスト**が必須 |
| 値の正規化 | `ProviderName` 等の表記ゆれ吸収、通貨・タイムゾーン統一、重複排除を変換層で実装 |
| 監視・品質 | 日次突合（<1% 誤差）、欠損検知、スキーマドリフトアラートを運用フローに組み込む |

**示唆**:

- **カスタマイズ前提**のプロジェクトであることを関係者全員で合意する必要がある
- 変換ロジックは **ソース別モジュール化 + 契約テスト**（各ソースのサンプルデータで FOCUS 出力を検証）で保守性を確保
- FOCUS バージョン選定（2.1.5）よりも、**変換層の設計原則・テスト戦略・運用体制**のほうが成果を左右する

[^1]: FOCUS Specification v1.2 §1.4.4 Extensibility, https://focus.finops.org/focus-specification/v1-2/
[^2]: FinOps Open Cost and Usage Specification Changelog (v1.2 Added), https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/blob/working_draft/CHANGELOG.md

# 3. スモールスタート方針

## 3.1 フェーズ分割

- **Phase 1（今回）: Azure 請求 → New Relic 可視化**
  - 1 ソースに絞ってパイプライン骨格を確立
- **Phase 2**: New Relic 自身のコスト
- **Phase 3**: Akamai / PagerDuty

## 3.2 【論点】New Relic 純正の Azure Cost Management 連携を使うかどうか

New Relic には [Azure Cost Management 連携](https://docs.newrelic.com/jp/docs/infrastructure/microsoft-azure-integrations/azure-integrations-list/azure-cost-management-monitoring-integration/) があり、Azure に Billing Reader を付与するだけでコストデータを `AzureCostManagementSample` イベントとして取り込める。

| 観点 | 純正連携 | 自前 FOCUS パイプライン |
| --- | --- | --- |
| 対応ソース | **Azure のみ** | 全 SaaS 共通 |
| スキーマ | `AzureCostManagementSample`（NR 独自 / FOCUS ではない） | FOCUS 1.x |
| 粒度 | サービス / ロケーション / RG / 指定タグ | 明細レベル |
| 導入コスト | 低（設定のみ） | 中（パイプライン構築） |
| Phase 2/3 への転用 | 不可 | 可 |

**提案**: Phase 1 を以下 2 ステップに分けるのが合理的。

- **Phase 1a**: 純正連携で早期に可視化感をお客様と共有（PoC 的位置づけ）
- **Phase 1b**: FOCUS Export + パイプラインに正式移行。純正連携は将来 Off。

## 3.3 Phase 1 の Exit Criteria（本番移行判断基準）

- **Azure の日次コストが New Relic 上で突合誤差 < 1% で再現できること**（仮置き）

# 4. Azure 請求データ → New Relic の具体設計

## 4.1 データフロー

```
Azure Cost Management (FOCUS Export, 日次)
   ↓
Azure Storage (ADLS Gen2, Bronze: 生データ)
   ↓
変換処理 (Silver: FOCUS スキーマに正規化)
   ↓
Gold: New Relic 投入可能な FOCUS 形式データ(明細粒度)
   ↓
New Relic Events API (POST)
   ↓
NRQL で集計・可視化・ダッシュボード化
```

> **集計は New Relic 側で実施**。Gold 層は「FOCUS 準拠の明細データがそろって送信キューに乗る状態」を指し、パイプライン側で日次サマリ等に事前集計はしない。

## 4.2 取得元

- **Azure Cost Management Exports**（FOCUS フォーマット、日次スケジュール）
- 2.1 の論点で選定したバージョンを採用

## 4.3 変換処理

- 2.1 で **A 案（1.0 GA）** を選ぶ場合: `ProviderName` / `InvoiceId` / `PricingCategory` 等を付与するアダプタが必要
- 2.1 で **B 案（1.2 preview）** を選ぶ場合: **変換不要**。そのまま使えることを preview 採用のメリットとして整理

## 4.4 New Relic 側の設計

**※ 本セクションは New Relic 公式ドキュメントに基づく情報。お客様環境の最終構成は New Relic パートナー様と合わせて確定する**

### 4.4.1 投入方式: Events API（Custom Event）

- エンドポイント: `https://insights-collector.newrelic.com/v1/accounts/<ACCOUNT_ID>/events`
- 認証: `X-Insert-Key` ヘッダーに Insert API Key を設定
- ペイロード制限:
  - 1 回の POST あたり **最大 1 MB**（gzip 圧縮推奨）
  - UTF-8 エンコード必須
  - 1 データ型あたり属性数 **最大 254**
- 送信例（イメージ）:

```http
POST /v1/accounts/<ACCOUNT_ID>/events HTTP/1.1
Host: insights-collector.newrelic.com
X-Insert-Key: <INSERT_KEY>
Content-Type: application/json
Content-Encoding: gzip

[
  {
    "eventType": "FocusBillingDaily",
    "ProviderName": "Microsoft",
    "ServiceName": "Azure Virtual Machines",
    "BilledCost": 123.45,
    "BillingCurrency": "JPY",
    "ChargePeriodStart": "2026-04-22T00:00:00Z",
    "ChargePeriodEnd": "2026-04-23T00:00:00Z",
    "ResourceId": "/subscriptions/.../virtualMachines/vm-01",
    "tag.env": "prod"
  }
]
```

> **集約は New Relic 側で NRQL により実施する方針**のため、送信データは FOCUS 明細粒度を保持する。1 POST あたり 1 MB 上限があるため、パイプライン側では **明細レコードをバッチ分割 + gzip 圧縮して送信**する（事前集約はしない）。

### 4.4.2 クエリ（NRQL）サンプル

- Provider / Service 別の日次コスト推移:

```sql
SELECT sum(BilledCost) 
FROM FocusBillingDaily 
FACET ProviderName, ServiceName 
TIMESERIES 1 day 
SINCE 30 days ago
```

- タグ別のコスト按分:

```sql
SELECT sum(BilledCost) 
FROM FocusBillingDaily 
FACET `tag.env`, `tag.project` 
SINCE this month
```

- ダッシュボードは FACET 属性で **フィルター連携**可能（Provider を選ぶと他ウィジェットも絞り込まれる構成）

### 4.4.3 決めておくこと（New Relic 側）

- 投入先 New Relic アカウントと Insert API Key の発行元
- イベント保持期間
- Custom Event 追加によるライセンス / データ取り込み課金への影響試算

# 5. データパイプライン選定

| 観点 | 候補 | 推奨 |
| --- | --- | --- |
| オーケストレーション | Azure Data Factory / Logic Apps / Fabric Data Pipelines | **ADF**（既存運用に乗せやすい） |
| 実行環境 | Functions / Container Apps Jobs / Databricks | **Functions 起点、増えたら Container Apps Jobs** |
| ストレージ | ADLS Gen2（Parquet / Delta） | 同左 |
| シークレット | Key Vault + Managed Identity | 同左 |
| 監視 | Azure Monitor + Application Insights | 同左 |

> データ量が小さい（数百万行 / 月以下）なら Spark 不要。ADF + Functions + ADLS で十分。

# 6. リスク・前提条件

- **Azure の FOCUS 1.2 Export は preview**。本番運用前に GA 化を確認、もしくは 1.0 + アダプタで代替
- **New Relic 側のデータ取り込み課金**（Custom Event 量 × 単価）を試算する必要あり
- **シークレット管理 / 権限境界**（Azure テナント横断、子サブスクリプション、New Relic API Key）の設計
- **請求データはセンシティブ情報**のため、Storage / New Relic / ダッシュボードのアクセス権限設計が必要
- Preview 機能 / API 仕様変更への追従ポリシー

# 7. 決めなければならないこと（Next Actions）

| カテゴリ | 決定事項 | オーナー候補 |
| --- | --- | --- |
| スコープ | Phase 1 対象サブスクリプション範囲 | 情シス / FinOps |
| スキーマ | FOCUS バージョン（1.0 GA + アダプタ / 1.2 preview） | FinOps |
| 進め方 | 純正 Azure Cost Management 連携を Phase 1a として使うか | FinOps / New Relic 担当 |
| New Relic | 投入先アカウント / Insert API Key / 保持期間 / 課金影響 | New Relic 管理者 |
| Azure | FOCUS Export 作成権限（Billing Reader 以上） | Azure 管理者 |
| 運用 | 平日夜間障害時の一次受け / 再実行担当 | 運用チーム |
| コスト | パイプライン予算上限 / New Relic 課金増加の許容額 | FinOps |
| スケジュール | PoC 完了期日 / 本番リリース想定時期 | PM |

# 8. ご提案スケジュール（たたき台）

- W0–W1: 要件確定 / アクセス準備
- W2–W3: Azure Export + ADLS + 変換実装
- W4: New Relic 投入 / NRQL ダッシュボード
- W5: 突合検証 / Exit Criteria 確認
- W6: Phase 2 計画（New Relic 自身のコスト取り込み）

---

## 参考

- Azure Cost Management FOCUS Export スキーマ: https://learn.microsoft.com/azure/cost-management-billing/dataset-schema/cost-usage-details-focus
- FOCUS Specification v1.2: https://focus.finops.org/focus-specification/v1-2/
- New Relic Azure Cost Management 連携: https://docs.newrelic.com/jp/docs/infrastructure/microsoft-azure-integrations/azure-integrations-list/azure-cost-management-monitoring-integration/
- New Relic Custom Event データ制限: https://docs.newrelic.com/docs/data-apis/custom-data/custom-events/data-requirements-limits-custom-event-data/
