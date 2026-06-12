Title: AI for FinOps 入門 — Token Economics と Azure での実装
Date: 2026-06-12
Slug: ai-for-finops-finops-x-2026
Lang: ja-jp
Category: notebook
Tags: finops, ai, azure, token-economics, agentic-ai, cost-management, focus, generative-ai
Summary: FinOps X 2026 で中心テーマとなった「AI for FinOps」と「FinOps for AI」を概念から整理し、難解な Token Economics（トークン経済）を平易に解説。Azure / Microsoft 製品での実装と再現可能なデモ シナリオ、導入ロードマップとガバナンスまで、FinOps Foundation と Microsoft Learn を根拠にまとめます。

「AI for FinOps」を、概念から具体例、そして **Azure / Microsoft 製品での実装** まで一気通貫で落とし込むための記事です。2026 年 6 月の **FinOps X 2026** で中心テーマになった内容[^1][^2]を土台に、特に難解な **Token Economics（トークン経済）**[^3] を平易な言葉と図で解説します。抽象論で終わらせず、「Azure で何ができるか」「Microsoft 製品でどうデモするか」まで具体化します。

> 用語の流動性に関する注意: Microsoft の AI 関連サービス名（Azure OpenAI / Azure AI Foundry / Microsoft Foundry）や提供形態（PTU / 予約など）は改称・更新が進行中です。本記事は執筆時点の Microsoft Learn を根拠としていますが、実装前に必ず最新の公式ドキュメントで確認してください[^11][^12]。

## この記事の要点（先に結論）

- FinOps は「クラウド費用管理」から **AI 時代の Technology Value Management（技術投資を価値に変える実践）** へ拡張している[^1][^2]。
- 紛らわしい 2 語をまず分ける。**AI for FinOps＝AI で FinOps 業務を加速する**こと、**FinOps for AI＝AI 利用そのもののコスト・価値を管理する**こと[^4][^9]。
- **Token Economics（トークン経済）** は FinOps for AI の共通言語。「トークン＝ AI の最小単位（atomic unit）」だが、**AI コストはトークンだけではない**[^3]。
- **Agentic FinOps** は「通知から行動へ」。Crawl / Walk / Run で段階導入し、**重要な判断は人間が承認**する（Human-in-the-loop）[^2][^7]。
- Azure では **FinOps hub の AI エージェント**[^10]、**API Management の AI ゲートウェイ**[^11]、**Foundry の Model Router**[^12] などで、両方向を実装できる。

![AI for FinOps と FinOps for AI の概念整理。左が AI で FinOps 業務を加速する方向、右が AI 利用のコストと価値を管理する方向](/images/ai-for-finops-finops-x-2026/concept-map.png)

## FinOps X 2026 が示した潮流

FinOps X 2026（2026 年 6 月・サンディエゴ）の 2 日間の基調講演は、いずれも **AI** が主題でした[^1][^2]。

**Day 1「The Wild West of AI, Token Economics」**[^1]では、FinOps Foundation の J.R. Storment 氏が「**トークンは AI の最小単位（atomic unit）**」であり、トークン利用の指数的な増加と変動費的な性質が新しい課題を生むと提起しました。あわせて、FinOps Foundation と Linux Foundation が **Tokenomics Foundation** の設立意向を発表。AI 課金のオープン標準づくりを目指し、初期支援企業として Oracle、Google、Microsoft、Accenture、Booking.com、Flexera、IBM、JPMorganChase、KPMG、Nebius、Salesforce、SAP、ServiceNow が名を連ねました[^1]。

- **Microsoft（Day 1）**: Cyril Belikoff 氏が **Microsoft Fabric と Foundry** で「Agentic Decision Intelligence（エージェント型の意思決定インテリジェンス）」を実現する構想を提示。統合データ＋ AI 基盤を作り、コストを規律に直接組み込むこと、そして **FOCUS 1.4 を 2026 年にサポート**する計画を表明しました[^1]。
- **AWS（Day 1）**: Savings Plans の Target Coverage、コスト・予測の自動説明、追加のアイドル リソース推奨、Amazon Bedrock の粒度の細かいコスト配賦などに加え、自然言語クエリと安全な自律実行を備えた **AWS FinOps Agent** を発表[^1]。
- **実践者の声（Day 1）**: SAP（グローバル規模の AI FinOps 運用）、Accenture（成果コストの定義・計測・統制へ）、Prudential（従来型 FinOps は table stakes）、Shutterstock（AI 価値への道のり）[^1]。

**Day 2「From Alerts to Agents」**[^2]は、FinOps 業務そのものを AI で加速する話に踏み込みました。FinOps Foundation の Ishita Vyas 氏が **Crawl / Walk / Run** の Agentic FinOps 成熟度モデルを提示し、Mike Fuller 氏は「**AI は FinOps の仕事を奪わない。AI をより理解する FinOps 実務者が価値を高める**（Human Premium）」と強調しました[^2]。

- **Google Cloud**: FinOps AI Explainability Agent、フルスタックの AI コスト可視化、Automated Spend Caps、FOCUS 1.2 サポート[^2]。
- **IBM Cloudability**: Conversational Insights、Cloudability MCP Server、FOCUS AI Agent[^2]。
- **Pinterest**: Product AI と Internal AI を分け、最適化を積み上げる「Tokenomic Layer Cake」[^2]。
- **MetLife**:「AI is cloud all over again, only 10x faster（AI はクラウドの再来、ただし 10 倍速い）」[^2]。
- **Oracle**（FOCUS 1.3 サポート）、**Flexera**（apps・agents・models・compute を横断する AI Spend Management Platform、ProperOps+）、そして **FOCUS 1.4** の発表（FOCUS MCP Server にも言及）[^2]。

潮流をひとことで言えば、FinOps は「**何が起きたか**を見る」段階から「**なぜ起きたか・次に何をすべきか**を AI とともに扱う」段階へ移っています[^2]。

## まず分ける：AI for FinOps と FinOps for AI

最初の図のとおり、似た 2 語を分けて語ることが理解の第一歩です[^4][^9]。

| 軸 | 意味 | ひとことで | 位置づけ |
| --- | --- | --- | --- |
| **AI for FinOps** | 生成 AI / エージェント AI で FinOps 実務を速く・正確に・スケールさせる | 「FinOps の仕事を AI にやらせる」 | FinOps Foundation のトピック / 実務ガイド[^4][^5] |
| **FinOps for AI** | トークン・GPU・モデル API など AI 特有のコスト・価値を可視化・最適化・統制する | 「AI の請求書を FinOps で御す」 | FinOps Foundation の正式な技術カテゴリ / スコープ[^9] |

FinOps for AI が重要になる背景には、AI 支出が **データセンター・ハイパースケーラ・SaaS・モデルベンダー・"AI ネオクラウド"** を横断する、新しい粒度の支出だという事情があります。実験が多く支出が変動しやすいため、配賦・予測・統制のいずれもが従来のクラウド FinOps より難しくなります[^9]。State of FinOps 2026 では、AI 支出を管理する実務の割合が大きく増え、AI を実務の重要な生産性ツールと見る実務者も多数にのぼると報告されています[^4][^8]。

## Token Economics を平易に理解する

ここからが本記事の核心で、最も難解とされる **Token Economics（トークン経済）** を、できるだけ平易な言葉で整理します[^3]。

### トークンとは何か（AI の最小単位）

**トークン**とは、大規模言語モデルが読み書き・推論する最小のデータ単位です。英語ではおおむね 1,500 語が約 2,048 トークンに相当します（分割方式はモデルにより異なる）[^3]。重要なのは、暗号資産の「トークン」とは無関係で、ここでは **計算（知能）の単位** だということです。

すべての AI 利用は「**入力トークン**（プロンプト・文脈・指示・履歴）」と「**出力トークン**（回答・ツール呼び出し・推論過程）」に分解でき、多くの場合この 2 つは別単価で課金されます[^3]。Token Economics は、従来の FinOps が「変動費のクラウド資源（計算・保存・通信）と価値の関係」を扱ってきたのと同じことを、**"知能そのものの変動費"** に対して行う営みだと位置づけられます[^3]。

![トークンは入力・モデル処理・出力のすべてで消費される最小単位であり、消費を増やす5つの要因と、成果あたりコストの考え方を示した図](/images/ai-for-finops-finops-x-2026/token-atomic-unit.png)

### なぜ予測が外れるのか（消費は非線形）

トークン消費は、ユーザーの見かけの操作量に比例しません。1 リクエストあたりの消費は、主に次の 5 つで決まります[^3]。

1. **システムプロンプトの固定費**: 毎回付与される指示。長いほど固定費化する。
2. **文脈・記憶**: 取得した文書（RAG）、会話履歴、ツール定義。
3. **モデル選択**: reasoning（推論）系や大規模モデルは、同じ作業でも多くのトークンを使う。
4. **出力長**: 長文・コード・レポート生成は出力を押し上げる。
5. **再試行・オーケストレーション**: 失敗・検証・エージェント間通信といった "見えない" コスト。

これらは掛け算で効きます。RAG ＋ reasoning モデル＋複数ツール呼び出しを伴う 1 件の問い合わせは、小さなモデルへの単純なプロンプトより **1〜2 桁多い** トークンを消費し得ます。**消費はユーザー操作に対して非線形**であり、これが従来のコスト予測が AI で当たりにくい主因です[^3]。

### 2026 年の価格環境（単価は下落、総額は増加）

「トークン単価は下がり続けるから安心」という早期の語りは、もう実態に合いません[^3]。

- **補助フェーズの終わり**: フロンティア モデルの提供者は普及期に原価割れの価格を付けていました。企業の消費増が単価低下を上回り、採算が崩れ始めています。Anthropic は 2026 年 4 月、企業向けを「席料＋事前コミットのトークン消費」型へ移行しました[^3]。OpenAI の ChatGPT 製品責任者は「無制限の AI プランは無制限の電気プランと同じで成立しない」と公に述べています[^3]。
- **reasoning / agentic が消費を押し上げる**: 推論・エージェント型のワークロードは、同等のチャットより **5〜30 倍** のトークンを消費します[^3]。IEA は、AI 向けデータセンターの電力需要が 2025 年だけで約 50% 増加した（全体の電力需要は約 3%）と報告しています[^3]。
- **総量の現実**: AT&T はマルチエージェント導入後、1 日あたり約 80 億→ 270 億トークンへ拡大。Google は月あたり約 1.3 京（quadrillion）トークン、前年比約 130 倍を報告しています[^3]。

結論はシンプルです。**1 トークンは安くなり得るが、組織が実際に消費するトークン（総量）は安くならない**[^3]。

### すべてのトークンは同じではない（Goodput）

トークンを「数」だけで見るのは不十分です。秒間 5 トークンで届くトークンと 500 トークンで届くトークンは、経済的に別物だからです[^3]。ここで重要なのが **Goodput（有効スループット）**＝定義した SLO（応答開始までの時間や、ユーザーあたりの継続生成速度）を満たした出力です。企業が実際に買っているのは raw な throughput ではなく goodput です[^3]。

| ティア | 特徴 | 向くワークロード |
| --- | --- | --- |
| **Bulk トークン** | 高スループット・低速 | バッチ要約、埋め込み生成、オフライン分析 |
| **Goldilocks ゾーン** | 中程度の対話性で最適スループット | チャット・一般的な業務アプリ（経済的な中心） |
| **Premium 低レイテンシ** | 高速・低スループット | 音声エージェント、応答速度が生産性を左右する用途 |
| **Reasoning トークン** | 外部出力 1 に対し内部で多数生成 | 複雑推論。見かけは中位でも消費プロファイルは大きい |

つまり Token Economics は **量だけでなく "質"（goodput）も計測** する必要があります。量しか追わない組織は、コストを体系的に誤って配賦します[^3]。

### コストはトークンだけではない（氷山）

「AI コスト＝トークン コスト」と混同されがちですが、トークンは氷山の一角です[^3]。

![AIコストの氷山。水面上の見えやすいトークン課金に対し、水面下にクラウド計算・データセンター・ネットワーク・SaaS埋め込み・MLOps・シャドーAIなどの層が広がることを示す図](/images/ai-for-finops-finops-x-2026/token-cost-stack.png)

水面下には、クラウド計算・ストレージ（GPU/TPU・Vector DB）、自己ホスト時のデータセンター（電力・冷却。次世代 AI データセンターの建設費は 1 MW あたり 1,500〜2,000 万ドルとされる）、ネットワーク・egress、**SaaS 埋め込み AI**（席料にトークンが内包され見えにくい）、エンジニアリング・MLOps・ガバナンス、そして **シャドー AI**・データライセンスが広がります[^3]。トークンだけ見ると変動費（限界費用）しか捉えられず、投資判断に必要な固定費・準固定費が抜け落ちます[^3]。

### 3 つの提供形態と分岐点（CFO の視点）

CFO にとって重要なのは、AI の支出が **非線形・不透明・損益計算書に分散** するという 3 つの性質です[^3]。とりわけ「どの提供形態を選ぶか」は、トークン量に応じて損益分岐が動く戦略判断になります[^3]。

| 提供形態 | 導入コスト | トークン単価 / 限界費用 | 向く局面 |
| --- | --- | --- | --- |
| **SaaS 埋め込み** | 最も低い | 最も高い | 立ち上げ・小規模・実験 |
| **API 利用** | 中 | 中（提供者の価格改定に敏感・可視性は高い） | 多くの本番ワークロード |
| **自己ホスト（AI ファクトリー）** | 最も高い（資本） | 持続的大量時に最小（ただし低稼働だとリスク大） | 大量・安定・要件特化 |

これらの分岐点は、トークン需要を早めにモデル化すれば計算できますが、支出が膨らんでから考えると手遅れになりがちです。とくに自己ホストの設備投資は後戻りが難しく、**意思決定のタイミング自体が経済的に重要** です[^3]。

### トークンを価値に結びつける

Token Economics の目的は **トークンの最小化ではなく、トークン消費を価値に結びつけること** です。10 倍のトークンを使っても 100 倍の価値を生むなら、その方が経済的に優れています[^3]。実務では次のような指標で「コスト」と「価値」をつなぎます[^3][^9]。

- **Cost per inference（推論 1 件あたりコスト）**
- **Token consumption efficiency（必要 goodput における有用性あたりのトークン単価）**
- **Token yield rate（生成トークンのうち、再試行・中断・品質不合格を除いて実際に業務へ寄与した割合）**
- **Training cost efficiency / Inference efficiency**
- これらは必ず **事業側の価値指標**（売上・対応コスト削減・サイクルタイム短縮・不良率改善など）と対にする。

### エンジニアリングの削減レバー

「観察するだけでなく統制する」ための供給側の手段も成熟しています[^3]。これらのツールは AI ライフサイクル（学習・チューニング・推論・オーケストレーション）のどの段階に効くかで整理できます[^13]。後述の Azure 実装にも直結します。

- **モデルルーティング / カスケード**: 安いモデルで足り、必要なときだけ高価なモデルへ昇格。研究の FrugalGPT は最大 98%、RouteLLM は 85% 超のコスト削減を報告[^3]。
- **コンテキスト圧縮・剪定**: RAG で本当に必要なトークンは取得分のごく一部。Zilliz のセマンティック ハイライトは 70〜80% 削減、Flexpa は FHIR を SQL 化して 92% 削減を報告[^3]。
- **構造化出力・データ形式**: 関数呼び出しベースの構造化出力は自由形式 JSON より効率的。CSV/TSV や TOON は JSON 比で 30〜60% 少ないトークンで済む[^3]。
- **RAG と long context の使い分け**: 既定は RAG、取得の確信度が低いときだけ long context に昇格するハイブリッドで、純粋な long context 比 30〜65% 削減[^3]。
- **キャッシュ / モデル ティアリング / プロンプト最適化**: プロンプト キャッシュ（再利用部分を 50〜90% 削減）やセマンティック キャッシュ、最小のプロンプト整形は最も安価で過小評価されがちな手段[^3]。

## Agentic FinOps：通知から行動へ

AI for FinOps の中心が **Agentic FinOps** です。レポートを読むだけの段階から、AI が異常を調査し、所有者を探し、次の行動を準備する段階へ進みます[^2][^7]。

![Agentic FinOpsの成熟度Crawl/Walk/RunとSense-Think-Actのループ、人間の承認を挟む実行フロー、最初に自動化してよい領域と人間承認が必須の領域を示す図](/images/ai-for-finops-finops-x-2026/agentic-finops.png)

**Crawl / Walk / Run** の成熟度で段階的に広げます[^2]。Crawl は自動アラート・レポート、Walk は AI 支援の分析・推奨（自然言語 Q&A、原因仮説、PR/IaC レビュー、所有者推定）、Run はエージェントによる調査と一部実行（チケット作成、Teams 通知、タグ修正 PR、低リスク最適化）です。

中核の動きは **Sense（検知）→ Think（文脈化）→ Act（実行準備）**。ただし多くの組織は、エージェントに本番変更を完全自律で任せる段階にはありません。これが **トラスト ギャップ** で、当面の現実解は **Observe → Recommend → Approve → Act**、すなわち AI が調査・推奨・チケット/PR 作成まで行い、**人間が承認してから実行** することです[^7]。

- **最初に自動化してよい**: タグ修正候補、アイドル検出、非本番停止の提案、所有者特定、チケット作成。
- **人間承認が必須**: 本番削除、SKU 変更、契約 / コミット購入、セキュリティ設定変更、保持期間変更[^5][^7]。

### MCP は「AI の USB‑C」

エージェントを実データへ安全につなぐ標準が **Model Context Protocol（MCP）** です。LLM とツール/データを個別連携していた手間を、共通インターフェースに置き換えるもので、「AI アプリの USB‑C」と表現されます[^6]。

MCP は **Client（AI アプリ）/ Host（オーケストレーションと認証・監視・課金計測の層）/ Server（Tools・Resources・Prompts を公開）** で構成されます[^6]。FinOps から見た利点は、コンテキストのモジュール化、ツールのガバナンス、プロンプトの再利用とコスト配賦などです。一方で、**コンテキストがトークン課金を増やす**こと、スコープ分離の難しさ、認証の断片化、プロンプト インジェクションやトークン窃取などの**セキュリティ リスク**があり、外部のアクセス制御層が前提になります[^6]。FOCUS が「**何に**いくら使ったか」を標準化するのに対し、MCP は「コンテキストと行動が**どう**流れるか」を担い、両者は補完関係にあります[^6]。

## Azure でできること

ここからは Azure / Microsoft 製品での実装に絞ります。下図は、ユーザーの PDF にもあった発想を Microsoft Learn で裏取りした **参照アーキテクチャ** です。

![Azure で AI for FinOps を実装する参照アーキテクチャ。データソース、データ基盤、AIレイヤー、アクションレイヤー、全体を横断するガバナンスの5層構成](/images/ai-for-finops-finops-x-2026/azure-reference-architecture.png)

5 つの層に分けて考えると整理しやすくなります。

1. **データソース**: Cost Management エクスポート（FOCUS）、Azure Resource Graph、Azure Monitor / Log Analytics、Azure Advisor、Budgets / 異常検知。
2. **データ基盤**: Microsoft Fabric / OneLake、**FinOps hub（Azure Data Explorer / Kusto）**、Data Lake Storage、Power BI[^10]。
3. **AI レイヤー**: Azure AI Foundry、Azure OpenAI ＋ **Model Router**[^12]、Copilot Studio、**Azure MCP server**、GitHub Copilot Agent[^10][^11]。
4. **アクション レイヤー**: Logic Apps、Azure Functions、GitHub Actions / Azure DevOps、Teams、ServiceNow / Jira。
5. **ガバナンス（全層横断）**: Management Groups、RBAC / PIM、Azure Policy、Defender for Cloud、監査ログ。

### FinOps hub の AI エージェント（AI for FinOps の中核）

Microsoft FinOps toolkit の **FinOps hub** には、AI エージェント連携が公式に用意されています[^10]。構成は大きく 2 通りです。

- **GitHub Copilot（VS Code, エージェント モード）＋ Azure MCP server**: FinOps hub 用の Copilot インストラクションを `.github` に配置し、Azure MCP server をインストールすると、Copilot が hub（Azure Data Explorer）へ接続して自然言語で問い合わせできます[^10]。
- **Microsoft Copilot Studio エージェント**: Kusto Query MCP Server 経由で hub に接続するエージェントを作り、**Teams や Microsoft 365 Copilot** へ公開できます。組織全体にコスト インサイトを届けられます[^10]。

公式ドキュメントには、そのまま試せる自然言語プロンプト例が並びます[^10]。

- データ鮮度:「When was my data last refreshed?」
- 配賦:「What are the top resource groups by cost?」
- 傾向分析:「直近 3 か月のサービス支出傾向を分析し、増減トップ 5 を％付きで示して」
- 異常:「Are there any unusual spikes in cost over the last 3 months?」（Data Explorer の異常検知を利用）
- 予測:「先月・今月・当月着地見込みを、当月コスト上位サブスクリプションについて」
- レート最適化:「先月のコストとコミット割引・交渉割引の節約額、総節約額と実効節約率（ESR）」

重要なのは、複雑な分析では **Copilot が実行前に KQL の承認を求める** 点です。これは前述の Human-in-the-loop と透明性の実装そのものです[^10]。

### API Management の AI ゲートウェイ（FinOps for AI の要）

AI 利用そのもののコストを可視化・統制するなら、**Azure API Management の AI ゲートウェイ** が中心になります[^11]。モデル API の前段に置く制御面で、主な機能は次のとおりです。

- **トークンのレート制限・クォータ**（`llm-token-limit` ポリシー）: サブスクリプション キーや IP など任意のキー単位で、分間 TPM や期間別トークン クォータを強制[^11]。
- **セマンティック キャッシュ**（`llm-semantic-cache-store` / `llm-semantic-cache-lookup`）: Azure Managed Redis を使い、意味的に近いプロンプトの応答を再利用してトークン消費を削減[^11]。
- **トークン メトリックの発行**（`llm-emit-token-metric`）: クライアント IP・API・ユーザー ID などのディメンション付きで Application Insights / Azure Monitor へ送出。**配賦・チャージバックの生データ**になる[^11]。
- **コンテンツ安全性**（`llm-content-safety`）、**負荷分散 / サーキット ブレーカー**（PTU バックエンドの優先利用など）、**統合モデル API**（複数プロバイダーを 1 エンドポイントに集約）[^11]。
- **Microsoft Foundry 内の AI ゲートウェイ（プレビュー）**: Foundry 画面からモデルのトークン クォータ・レート制限を設定し、エージェントや MCP ツールを登録・統制できる[^11]。

### Model Router（モデルルーティングの Azure 実装）

Token Economics の最重要レバー「モデルルーティング」は、**Microsoft Foundry の Model Router** がそのまま実装になります[^12]。プロンプトの複雑さ・推論要否・タスク種別をリアルタイムに判定し、最適なモデルへ振り分ける単一デプロイです[^12]。

- **ルーティング モード**: `Balanced`（既定・コストと品質を動的に両立）、`Cost`（高ボリューム・予算重視）、`Quality`（精度最優先）[^12]。
- 単純なクエリは小型・安価なモデル、複雑な推論は reasoning モデルへ自動で割り当て、**品質を保ちつつコストとレイテンシを最適化**[^12]。
- **モデル サブセット**、**自動フェイルオーバー**、**プロンプト キャッシュ**に対応し、**Azure Policy** でデプロイ可能モデルを統制できる[^12]。

### AI コストの可視化と FOCUS

FinOps for AI の土台はデータです。Azure では Cost Management の **FOCUS 形式エクスポート** を FinOps hub に取り込み、Power BI / Fabric で横断レポート化できます[^10]。Microsoft は FinOps X 2026 で **FOCUS 1.4 の 2026 年サポート** を表明しています[^1]。トークン単位の利用は、現状 FOCUS 固有の AI 専用列ではなく、SKU や `ConsumedUnit=Tokens` などで表現される点に留意してください[^9]。

## Microsoft 製品で実現するデモ シナリオ

以下は、**公式に文書化された機能を組み合わせた再現可能なデモ設計案** です（既製の単一製品ではなく、引用先の機能で構成します）。スライドより「動くもの」を見せると伝わります[^10][^11][^12]。

### D1. 自然言語コスト分析（Azure Cost Copilot）

- **見せ方**:「先月コストが増えた上位要因は？」「東日本リージョンで予算超過リスクが高い RG は？」を自然言語で質問し、AI が前月比・予算比・原因仮説・所有者候補・推奨アクションを返す。
- **使う機能**: FinOps hub ＋ Azure MCP server ＋ GitHub Copilot / Copilot Studio（Teams / M365 Copilot 公開）[^10]。
- **勘所**: エージェントに **裏側の KQL を見せ・承認させる** ことで、トラスト ギャップを逆手に取った "透明な AI" を演出[^10]。

### D2. 異常のエージェント調査（Agentic Cost Anomaly Investigation）

- **見せ方**:「Storage が前週比 +80%」を起点に、Storage アカウント・Hot tier 増加・Data Factory 実行回数・関連 RG・owner タグを横断調査し、月末着地リスクとライフサイクル ポリシー / Cool・Archive 候補を提示。**削除や保持変更は実行せず、担当者確認と承認依頼まで**作成。
- **使う機能**: Budgets / 異常検知 → Resource Graph・Activity Log・Monitor → 文脈化 → Teams / ServiceNow / GitHub Issue（Logic Apps・Functions）[^10][^7]。

### D3. Right-sizing と IaC / PR ガードレール（シフトレフト）

- **見せ方**: Azure Advisor と Monitor を AI が文脈化し、VM・Azure SQL・App Service Plan・AKS ノード プール・Cosmos DB・Redis などを優先順位化。さらに Bicep / Terraform の PR 段階で、高額 SKU・タグ不足・dev/test への本番 SKU・autoscale 不足・Log Analytics 保持期間を検出して **PR コメント** する。
- **使う機能**: Advisor / Monitor ＋ GitHub Actions / Azure DevOps ＋ AI レイヤー[^5][^7]。

### D4. タグ付け・配賦・所有者推定

- **見せ方**: 未タグ リソースを、リソース グループ名・サブスクリプション・デプロイ履歴・Activity Log・接続先・周辺タグから文脈推定し、`confidence` に応じて「タグ修正 PR / 所有者確認 / 例外管理」に振り分ける。
- **使う機能**: Resource Graph ＋ AI レイヤー ＋ アクション レイヤー[^5][^7]。

### D5. トークン経済ダッシュボード（FinOps for AI）

- **見せ方**: API Management の `llm-emit-token-metric` でアプリ / チーム / モデル別のトークン消費を出し、Application Insights → Power BI / Managed Grafana で **Cost per Inference・Token Consumption Efficiency** を可視化。`llm-token-limit` で予算ガードレール、`llm-semantic-cache` でキャッシュ ヒット率と削減効果を示す。
- **使う機能**: API Management AI ゲートウェイ ＋ Application Insights ＋ Power BI[^11]。

### D6. Model Router のコスト デモ

- **見せ方**: 同一の問い合わせ群を `Quality` と `Cost`（または `Balanced`）で流し、選択モデルの内訳・レイテンシ・推定コスト差を並べて見せる。「単一モデル運用は可視的な非効率」というメッセージを実演[^3][^12]。
- **使う機能**: Foundry の Model Router（モード切替・モデル サブセット）＋ Azure ポータルのコスト監視[^12]。

## 導入ロードマップとガバナンス

抽象論で終わらせないために、**低リスクから段階導入** します[^5][^7][^10]。

| フェーズ | 主な取り組み |
| --- | --- |
| **Crawl** | Cost エクスポート有効化、タグ / 階層整理、Power BI・Fabric 集約、Advisor / Budget / 異常検知、自然言語 Q&A の PoC |
| **Walk** | Foundry / OpenAI で FinOps Copilot、Resource Graph・Logs 接続、Teams / チケット作成、IaC PR チェック、所有者推定 |
| **Run** | 異常調査の自律実行、低リスク最適化、非本番停止、タグ修正 PR、コミット推奨（いずれも人間承認付き） |

エージェントの価値は、モデル性能ではなく **安全な権限・承認・監査とセット** で決まります[^7]。

- **RBAC / PIM**: 「読み取り / 推奨 / 変更実行」を分離し、Just-in-Time 権限を使う。
- **Azure Policy**: タグ・SKU・リージョン・暗号化・ログ保持などをコード化。
- **承認ワークフロー**: Logic Apps / DevOps / ServiceNow で承認ステップを明示。
- **監査ログ**: 「誰が・どの AI が・何を見て・何を提案し・誰が承認したか」を残す。
- **Blast radius**: 最初は dev/test・単一サブスクリプション・低リスク操作に限定。**Rollback** と例外管理を用意。
- **当面は自動化しない**: 本番削除、SKU 変更、データ保持変更、RI / Savings Plan 購入、ネットワーク / セキュリティ変更[^7]。

## まとめ

- FinOps は **AI 時代の Technology Value Management** へ拡張し、FinOps X 2026 では Token Economics と Agentic FinOps が中心テーマになりました[^1][^2]。
- まず **AI for FinOps（AI で業務を加速）** と **FinOps for AI（AI のコスト・価値を管理）** を分けて語る[^4][^9]。
- **Token Economics** の要点は、「トークンは最小単位だが、AI コストはトークンだけではない」「目的は削減ではなく成果あたりコストと価値の最大化」[^3]。
- Azure では **FinOps hub の AI エージェント**[^10]、**API Management の AI ゲートウェイ**[^11]、**Foundry の Model Router**[^12] が、両方向の実装の核になります。
- 進め方は **Crawl / Walk / Run** と **Human-in-the-loop**。低リスクから、監査可能に、人間承認を前提に[^5][^7]。

---

[^1]: FinOps X 2026 Day 1 Keynote: The Wild West of AI, Token Economics and the Evolving Role of FinOps, https://www.finops.org/insights/finops-x-2026-day-1-keynote/

[^2]: FinOps X 2026 Day 2 Keynote: From Alerts to Agents, https://www.finops.org/insights/finops-x-2026-day-2-keynote/

[^3]: Token Economics: The Atomic Unit of AI Value, https://www.finops.org/insights/token-economics-the-atomic-unit-of-ai-value/

[^4]: AI for FinOps（FinOps Foundation トピック）, https://www.finops.org/topic/ai-for-finops/

[^5]: AI for FinOps Fundamentals: Use Cases and Prompt Practices, https://www.finops.org/wg/ai-finops-prompts/

[^6]: Model Context Protocol (MCP): An AI for FinOps Use Case, https://www.finops.org/wg/model-context-protocol-mcp-ai-for-finops-use-case/

[^7]: AI for FinOps: Agentic Use Cases in FinOps, https://www.finops.org/insights/ai-for-finops-agentic-use-cases/

[^8]: AI Value（FinOps for AI トピック）, https://www.finops.org/topic/ai-value/

[^9]: FinOps for AI（FinOps Framework 技術カテゴリ）, https://www.finops.org/framework/technology-categories/ai/

[^10]: Configure and use AI agents（FinOps hubs / Microsoft Learn）, https://learn.microsoft.com/en-us/cloud-computing/finops/toolkit/hubs/configure-ai

[^11]: AI gateway in Azure API Management（Microsoft Learn）, https://learn.microsoft.com/en-us/azure/api-management/genai-gateway-capabilities

[^12]: Model router for Microsoft Foundry（Microsoft Learn）, https://learn.microsoft.com/en-us/azure/ai-foundry/openai/concepts/model-router

[^13]: FinOps for AI: Tools & Services Considerations, https://www.finops.org/wg/finops-for-ai-tools-services-considerations/
