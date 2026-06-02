Title: CIS 準拠をどう作るか — CIS 標準イメージと Defender for Cloud の使い分け
Date: 2026-06-02
Slug: azure-cis-compliance-defender-for-cloud
Lang: ja-jp
Category: notebook
Tags: azure, cis-benchmark, defender-for-cloud, compliance, hardening, golden-image, machine-configuration
Summary: Azure VM を CIS Benchmark に準拠させる 2 つのアプローチ — CIS 標準（ハードン済み）イメージで作る方法と、標準イメージ + Defender for Cloud で測りながら作る方法 — を、役割（予防 / 検出）、手順、メリット・デメリットの観点で整理する。

前回の記事（[Azure VM イメージ標準化で考えるべきこと]({filename}azure-image-standardization-principles.md)）では、イメージ標準化を **L1（中身）/ L2（配布）/ L3（統制）** の 3 レイヤで捉えました。本記事はその L1（中身のハードニング）と L3（統制・可視化）に踏み込み、**「VM を CIS Benchmark に準拠させる」具体策**を整理します。

論点は「**CIS のハードン済みイメージを買って使うか**」か「**標準イメージに自分でハードニングを当て、Defender for Cloud で測りながら準拠させるか**」です。

> CIS Benchmark の本文（具体的な設定値や推奨項目）は CIS（Center for Internet Security）の著作物です。本記事では一般的なカテゴリと考え方のみを扱い、正確な設定値は公式ベンチマークを参照してください。

## 1. 大前提 — 2 つは排他ではない

最初に誤解を解いておきます。**「CIS イメージ」と「Defender for Cloud」は二者択一ではありません。** 違いは **ハードニング（準拠状態）の出所** であり、Defender for Cloud は **どちらのアプローチでも共通して使う監視・可視化レイヤ**です。

```
準拠状態を「作る」     →  A: CIS イメージが事前提供   /  B: 標準イメージに自分で適用（Machine Configuration）
準拠状態を「測る・保つ」 →  どちらも Defender for Cloud で可視化（共通）
```

イメージ標準化の 3 レイヤに当てはめると、**A / B の違いは L1（中身の作り方）**であり、**Defender for Cloud は L3（統制・可視化）**に対応します。

## 2. 役割の整理 — 予防（L1）と検出（L3）は補完関係

| 観点 | CIS（標準）イメージ | Defender for Cloud のコンプライアンス評価 |
|------|--------------------|-------------------------------------------|
| 性質 | 予防的（preventive） | 検出的（detective） |
| いつ効くか | デプロイ前（起点を強化する） | デプロイ後（実態を継続評価する） |
| 何を保証するか | 「強化された状態で生まれる」 | 「強化された状態が保たれている／ドリフトしていない」 |
| 標準化レイヤ | L1 | L3 |

CIS イメージは「最初から強い状態で VM を生む」ための予防策、Defender for Cloud のコンプライアンス評価は「強い状態が保たれているかを測る」ための検出策です。**両方そろって初めて「準拠を作り、保つ」が成立します**。CIS イメージを使っていなくても、Defender for Cloud 側で CIS Benchmark を割り当てれば評価そのものは可能です[^1][^2]。

## 3. 方法 A：CIS 標準イメージを使用して準拠する

CIS が提供する **CIS Hardened Image**（ベンチマーク適用済みの OS イメージ）を起点にして、生まれた時点で準拠状態の VM を展開するアプローチです。

### 手順

1. Azure Marketplace から対象 OS の **CIS Hardened Image** を取得する。
2. **Azure Compute Gallery** に取り込み、自組織のエージェント・社内 CA 証明書・固有設定を**上乗せ**する（前回記事のゴールデンイメージ発行プロセスに合流させる）。
3. CIS の**最新版を継続取得**し、ゴールデンイメージを**月次でリフレッシュ**する（固定運用しない）。
4. 稼働中 VM のランタイム パッチは **Azure Update Manager** で別途適用する[^3]。
5. （推奨）Defender for Cloud で CIS 標準を割り当て、準拠状態を**監視**する[^1]。

### メリット

- **即時準拠・監査対応が速い**。CIS 認証済みのベースから始められる。
- **内製ハードニング不要**。CIS が基準改訂・項目更新をメンテナンスする。
- デプロイのたびに**同一の強化ベースライン**で一貫性が保てる。

### デメリット

- **ライセンス料**が発生する（イメージ利用料が Azure 料金に上乗せ）。
- **最新版追従が必須**。古い版を使い続けると陳腐化し、かえってリスクになる（アンチパターン）。
- **カスタム性が低い**。CIS 標準から外したい項目は結局自分で上書き調整が要る。
- **Level 2 等がアプリを壊す**リスク（後述）。結局は互換検証が必要。
- **第三者依存**。更新サイクル・項目選定を CIS に委ねることになる。

## 4. 方法 B：標準イメージ + Defender for Cloud で準拠させていく

Marketplace の標準イメージを起点にし、**Azure Machine Configuration**（旧 Guest Configuration）でハードニングを適用・監査しつつ、**Defender for Cloud** で準拠率を可視化して是正していくアプローチです。

### 手順

1. **標準 Marketplace の「最新」イメージ**を Compute Gallery に取り込む。
2. **Azure Machine Configuration** で CIS 整合のセキュア構成を**適用 + 継続監査**する。Microsoft Cloud Security Benchmark（MCSB）の PV-3 は、コンピューティング リソースのセキュア構成を Machine Configuration で定義・確立することを求めており、MCSB は CIS とも整合します[^4][^5]。
3. **Defender for Cloud の規制コンプライアンス**ダッシュボードで CIS 標準を割り当て、**準拠率・合否・非準拠コントロール**を可視化する[^1][^2][^6]。
4. 非準拠項目を是正（構成適用・修復スクリプト）し、**ドリフトは Defender / Machine Configuration で検知**する。
5. 月次リフレッシュ + Update Manager でパッチ運用を継続する[^3]。

### メリット

- **ライセンス料不要**（標準イメージ + Azure 標準機能で構成できる）。
- **制御性が高い**。CIS / STIG / 独自基準を組み合わせ、アプリ互換に合わせて項目を調整できる。
- **CI/CD・自動化と親和**。Compute Gallery / Azure Policy / Defender for Cloud で一気通貫に組める。
- **継続的な可視化・ドリフト検知**が標準で得られる。

### デメリット

- **内製の手間**。ハードニングの設計・適用・維持・テストを自前で担う必要がある。
- **初期は非準拠が多く出る**。そこから是正していく工数がかかる。
- **スキル / 工数依存**。維持を怠ると逆にドリフトする。
- **「CIS 認証イメージそのもの」は得られない**。監査がイメージ認証を要求する場合は不足になりうる。

> 注意: Defender for Cloud で CIS などの**規制コンプライアンス標準を割り当て・評価する機能は、有料の Defender プラン（Defender CSPM など）が前提**です。無料の Foundational CSPM では MCSB の評価は得られても、規制コンプライアンス標準の割り当ては対象外です。利用時は対象スコープでプランを有効化してください[^7][^8]。

## 5. 比較表

| 観点 | A: CIS 標準イメージ | B: 標準イメージ + Defender for Cloud |
|------|--------------------|--------------------------------------|
| 初期構築の手間 | 低 | 高 |
| 継続メンテ | CIS 任せで低（ただし最新追従は必要） | 自前で高 |
| コスト | イメージ ライセンス料あり | プレミアム イメージ料なし（Defender プラン費は別途） |
| カスタム性 | 低〜中 | 高 |
| アプリ互換調整 | 上乗せで対応 | 設計段階で調整可 |
| 監査対応 | CIS 認証イメージを提示できる | 準拠レポートで証明（イメージ認証は得られない） |
| 可視化 / ドリフト検知 | Defender 併用で可 | 標準で内包 |
| 向く組織 | 内製余力が乏しい／イメージ認証が監査要件 | 制御重視／コスト抑制／自動化文化 |

## 6. CIS Level 1 と Level 2 — 何が違うか

CIS Benchmark には一般に 2 つのプロファイルがあります。どちらのアプローチでも「どこまで締めるか」を決める軸になります。

- **Level 1**: 実用的な最低ラインの強化。**機能を壊しにくい**設定が中心で、まず最初に目指す基準。
- **Level 2**: 多層防御（defense in depth）を狙う強化。**機能・互換性を犠牲にしうる**ため、対象や用途を選ぶ。

Level 2 で「壊しやすい／業務影響が出やすい」代表例（一般論）:

- レガシー プロトコル / 認証の無効化（古い SMB、弱い暗号スイートなど）→ 旧クライアントやアプライアンスとの通信が切れる。
- マウント オプションの厳格化（`noexec` / `nosuid` など）→ 一時領域で実行するアプリが動かなくなる。
- スクリプト実行や周辺機器の制限 → 運用ツールや自動化が止まる。
- 詳細監査の有効化 → ログ量が増え、収集・保管コストに跳ね返る。

> 実務では「**Level 1 を全面適用 → Level 2 は対象を選んで段階適用**」が定石です。Level 2 は必ず検証環境で互換性を確認してから本番へ。具体的な設定項目・値は CIS 公式ベンチマークを参照してください。

## 7. Defender for Cloud で CIS 準拠率を測る

方法 A / B どちらでも、準拠の「ものさし」は **Defender for Cloud の規制コンプライアンス ダッシュボード**です[^6]。

- **準拠率（%）** と、コントロール単位の**合格 / 不合格**を一覧できる。
- 標準（CIS Benchmark など）を**スコープ（サブスクリプション / 管理グループ）に割り当て**て評価する[^1][^2]。
- **レポート出力**（PDF / CSV）で監査エビデンスにできる。
- 推移（Compliance over time）で改善状況を追える。

割り当ては Defender for Cloud → **規制コンプライアンス** → コンプライアンス標準の管理 → スコープを選択 → セキュリティ ポリシーで対象の **CIS Benchmark を有効化** する流れです[^1][^9]。OS ゲスト内部の設定まで評価するには、前述の **Azure Machine Configuration**（拡張機能 + マネージド ID）が必要です[^5]。

## 8. CIS「標準」を有効化／作る 3 つの方法

「自組織の CIS 標準を持つ」には大きく 3 パターンあります。

1. **組み込みの CIS 標準を Defender for Cloud で有効化**（最短）。用意済みの CIS Benchmark をスコープに割り当てるだけ[^1][^2]。
2. **Machine Configuration で OS 内部を評価・適用**。ゲスト内部の設定をベースラインとして監査・修復する[^5]。
3. **カスタム標準を作成**。組み込み標準をベースに、自組織で項目を取捨選択した独自標準を Defender for Cloud に登録する[^2]。

多くの場合、**1 + 2 の組み合わせ**（標準を割り当てて測り、Machine Configuration でゲスト内部まで踏み込む）から始め、必要に応じて 3 へ広げるのが現実的です。

## 9. 選び方とハイブリッドの落とし所

決め手は 3 つです。

1. **監査が「CIS 認証イメージそのもの」を要求するか** → Yes なら **A**。
2. **ハードニングを維持する内製余力があるか** → Yes なら **B**、No なら **A**。
3. **イメージ ライセンス料を許容できるか** → No なら **B**。

### 現実的な落とし所（ハイブリッド）

多くの環境では **「A でベースを早く準拠させ、Defender for Cloud（+ Machine Configuration）で測り続ける」**が出発点として有効です。将来的に内製力が付いたら **B へ寄せて**ライセンス料と第三者依存を減らす、という移行も取れます。

**どちらのアプローチでも、Defender for Cloud による継続監視は共通して必要**である、という点が結論です。

## 10. まとめ

- CIS イメージ（予防 / L1）と Defender for Cloud のコンプライアンス評価（検出 / L3）は**補完関係**で、二者択一ではない。
- **方法 A（CIS イメージ）**は即時準拠・低い内製負荷が利点、ライセンス料・最新追従・カスタム性が弱点。
- **方法 B（標準イメージ + Defender + Machine Configuration）**は低コスト・高い制御性・可視化内包が利点、内製の手間が弱点。
- Level 2 は多層防御の代わりにアプリ互換を犠牲にしうるため、**Level 1 全面 → Level 2 段階適用**が定石。
- 規制コンプライアンス標準の割り当ては**有料 Defender プランが前提**。OS ゲスト内部評価には **Machine Configuration** が必要。
- 迷ったら **A で早く準拠 → Defender で測り続ける → 内製力に応じて B へ寄せる**ハイブリッドが現実解。

---

[^1]: Assign regulatory compliance standards in Microsoft Defender for Cloud, https://learn.microsoft.com/azure/defender-for-cloud/assign-regulatory-compliance-standards

[^2]: Regulatory compliance standards in Microsoft Defender for Cloud, https://learn.microsoft.com/azure/defender-for-cloud/concept-regulatory-compliance-standards

[^3]: Azure Update Manager の概要, https://learn.microsoft.com/azure/update-manager/overview

[^4]: Microsoft cloud security benchmark — PV-3: Define and establish secure configurations for compute resources, https://learn.microsoft.com/security/benchmark/azure/mcsb-posture-vulnerability-management

[^5]: Azure Machine Configuration（マシン構成）の概要, https://learn.microsoft.com/azure/governance/machine-configuration/overview

[^6]: Regulatory compliance dashboard in Microsoft Defender for Cloud, https://learn.microsoft.com/azure/defender-for-cloud/regulatory-compliance-dashboard

[^7]: What is Cloud Security Posture Management (CSPM) — Plan availability, https://learn.microsoft.com/azure/defender-for-cloud/concept-cloud-security-posture-management

[^8]: Overview of Microsoft Defender for Servers, https://learn.microsoft.com/azure/defender-for-cloud/defender-for-servers-overview

[^9]: Security policies in Microsoft Defender for Cloud, https://learn.microsoft.com/azure/defender-for-cloud/security-policy-concept
