Title: AI for FinOps ~ AI Agent で FinOps を強化する ~
Date: 2025-01-20
Slug: finops-ai-agent
Lang: ja-jp
Category: notebook
Tags: azure,FinOps
Summary: Cloud Diaries: AI Agent を使用した FinOps のアプローチ手法に関して解説する記事です。

## 1: FinOps × AI の現状
本ブログでは AI Agent を使用した FinOps のアプローチ手法に関して解説します。

現在生成AI（GenAI）の急速な台頭により、未管理のままでは「スピンドパニック」（spend panic）を引き起こし、AIの導入を遅らせる原因になると警告されています。

クラウド支出が10年かけて6000億ドルに到達したのに対し、GenAIは2025年に同規模に到達する見込みであり、その成長速度は非常に速くなっています。
つまり AI の支出の管理に今後焦点を当てる必要性が出てきており、FinOps Foundation の 2025 のアップデートでも Scope として AI シナリオが追加されました。

![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/693422/47247280-2ea4-48c6-990d-fee492096569.png)

そこで今後議論にするべきことは 2 つの側面です：

* FinOps for AI（AI 活用のための FinOps）：AI のコスト管理を支援する。
* AI for FinOps（FinOps 活動のための AI 活用）：予測精度の向上、異常検知、コストの理解を AI によって高度化する。

この2つは、現在の FinOps 実践において共に重要な柱となっています。
本ブログは後者の **AI for FinOps** に焦点を当てます。

また今 **FinOps × AI で何が重要視されているか？** 
こちらは [State of FinOps](https://data.finops.org/?_gl=1*1auhbod*_ga*MTk4Mjg5MDk4OS4xNzEzMTg5OTA2*_ga_GMZRP0N4XX*czE3NTA2ODgwMjAkbzE4JGcwJHQxNzUwNjg4MjkyJGo2MCRsMCRoMA..) でも紹介されている通り、
AI を管理するうえで特に重要なのは、「クラウド利用とコストの理解」と「ビジネス価値の定量化」という FinOps の2つの領域に関わる活動です。
配分、データ取り込み、レポーティング、異常検知、予算策定・予測といった Capabilityを見ても、「AIのコストが今どうなっているのか」をまずは把握するニーズがとても強いことがわかります。
![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/693422/13cc485a-5dc8-4702-9576-1b13f10ef35f.png)

一方で、AI における最適化（Optimization）の優先度は今のところ高くありません。
ただし今後、各組織がコストの可視化という基盤を整えて、AIのコストをビジネス価値に結びつけていくフェーズに進むにつれて、最適化の重要性も増していくと見込まれています。

## 2: FinOps × AI Agent
FinOps を実践する人たちは、複雑なコストデータをビジネス視点の行動につなげることに苦戦しているはずです。

FinOps hubs は FinOps Framework に基づいた分析準備がされたデータ基盤を提供しますが、今まで実際に分析を行うには KQL やスキーマの知識が必要でした。

**ここで、GitHub Copilot (自然言語で言われた質問を分析クエリに変換) を VS Code で使い、Azure MCP サーバー 経由で FinOps hubs 0.11 に接続することで、高度な分析を自然言語で実現できるようになりました!**

<https://techcommunity.microsoft.com/blog/finopsblog/whats-new-in-finops-toolkit-0-11-%E2%80%93-may-2025/4420719>

> ☞ ノート:
Model Context Protocol (MCP) は、AI エージェントが外部データソースと安全に接続するためのオープンスタンダードです。
Azure MCP Server は Microsoft の実装で、GitHub Copilot などの AI エージェントが Azure リソースに接続するのを可能にします。

---

### FinOps hubs とは
FinOps hubs は、複数クラウド、請求アカウント、テナントをまたいで統一されたコストと利用情報のプラットフォームです。
GitHub Copilot + Azure MCP Server と連携することで、プラクティショナーの質問を KQL クエリに変換し、技術的な障壁なしで分析を行えます。

![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/693422/9d853989-9414-4a0e-bbde-6b0a27ef9bb3.png)

また FinOps hubs によって提供される主要機能は以下が挙げられています

* 📊 **Data foundation**: 複数クラウドや組織営域をまたいだ統一データ
* 🔗 **Integration**: Power BI / Microsoft Fabric / 直接 KQL / GitHub Copilot 等の多様なアクセス方法
* ⚙️ **Architecture**: Azure MCP サーバーが AI agent の質問を KQL に変換（セキュリティベースを保ちながら実行）
---
### FinOps hubs のデプロイ

FinOps hubs は Cost Management を拡張し、Microsoft Fabric、Azure Data Explorer、GitHub Copilot などのツールを使用して、高度なデータレポートと分析のためのスケーラブルなプラットフォームを提供します。 
Azure ネイティブの Cost Management と比較してメリットはいくつか挙げられますが以下を参考にしてください。

<https://learn.microsoft.com/ja-jp/cloud-computing/finops/toolkit/hubs/finops-hubs-overview#benefits>

大きなメリットを挙げると以下 2 点があると思います。
・💰 FinOps Open Cost and Usage Specification (FOCUS) との完全なアラインメントによるマルチクラウド環境でのコスト分析が可能です 
>  ☞ 2025/6 時点で最新バージョンは 1.2 です。Azure でも Preview としてエクスポート可能になっています。

・🧠 GitHub Copilot などの AI を利用したツールを活用するか、カスタム エージェントを構築して、FinOps を理解し、データにシームレスに接続する MCP サーバーを使用して FinOps タスクを高速化します

またデプロイのテンプレートは以下にアクセスすることで可能です:

<https://aka.ms/finops/hubs/deploy>

詳細はドキュメントを参照してください。

<https://learn.microsoft.com/ja-jp/cloud-computing/finops/toolkit/hubs/deploy?tabs=azure-portal%2Cadx-dashboard>

> ☞ ノート: FinOps hubs ではコストデータとして FOCUS を使用しています。
FOCUS フォーマットを使用することで、[さまざまなプロバイダーのコストデータを収集可能です](https://learn.microsoft.com/ja-jp/cloud-computing/finops/toolkit/hubs/deploy?tabs=azure-portal%2Cadx-dashboard#ingest-from-other-data-sources)。

---

### AI Agent の構成 (VS Code)
公式ガイドはこちらです。

<https://learn.microsoft.com/ja-jp/cloud-computing/finops/toolkit/hubs/configure-ai#configure-github-copilot-in-vs-code>

ドキュメントに従い、FinOps hubs の GitHub Copilot の手順をダウンロードし、.github フォルダーに内容を含めると以下のようなファイル構成になります。

📁 .github  
├── 📁 prompts  
└── 📄 copilot-instructions.md

ここで copilot-instructions.md をそのままで動かすとエラーや不安定さが見受けられるので工夫として以下の点を確認してください。
* Azure Data Explorer (ADX) が所属する Subscription ID を事前に記述しておく
* ADX で クエリする際デフォルトだと認証の失敗が起こるため auth-method を 0 と指定しておく (Entra ID 認証と指定できます)
* ADX のクエリをする Database の Hub 配下の Costs_v1_0 を指定しておく (時々他の Functions に対して Agent がクエリをするためです)

```yaml
- auth-method: 0 
- Subscription Id: ********************
- Tenant Id: ********************
- Resource Group: ********************
- Location: ********
- Cluster URI: **********************************************
- Database: Hub
- Functions: Costs/Costs_v1_0
``` 

* また工夫として FOCUS カラムを正しく認識できていない場合があったため、json で参照できるようにファイル配置と copilot-instructions.md に以下を追記しました。
```yaml
## Need Data Columns list?
- **[Check Database Guide](https://learn.microsoft.com/cloud-computing/finops/toolkit/hubs/data-model)**
- **[View FinOps Hubs Schema](FocusCost_1.0.json)**
---
```
📁 .github  
├── 📁 prompts  
└── 📄 copilot-instructions.md
└── 📄 FocusCost_1.0.json
>FOCUS メタデータは以下からダウンロード可能です。
<https://learn.microsoft.com/ja-jp/cloud-computing/finops/focus/metadata>
---
### 接続確認

1: Copilot Chat インターフェースを開き (Ctrl+Shift+I)、 Agent Mode を ON にする

![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/693422/6436b2a0-d180-4be0-a7a8-dbd5cdb67f11.png)

>☞ 検証においては GPT-4.1 の精度が一番高いと感じました。

2: MCP Server が Running 状態であることを確認します
![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/693422/14d9e428-fc36-4183-8894-5a12077d92d8.png)
> ☞ [こちら](https://insiders.vscode.dev/redirect/mcp/install?name=Azure%20MCP%20Server&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40azure%2Fmcp%40latest%22%2C%22server%22%2C%22start%22%5D%7D)から Azure MCP サーバーのインストールが可能かつ Runnning 状態にできます
> ☞ Tool の数が 128 を超えると Agent が使用できない為必要のない Tool のチェックマークを外しておくことを推奨します
![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/693422/b4480061-0927-46dc-bd4b-9e114de566c7.png)

3: 接続の確認
Agent モードで以下を入力し、FinOps hubs のインスタンス(ADX) に接続を要求します。
```yaml
/ftk-hubs-connect
```
> ☞ copilot-instructions.md を参照し ADX に繋ぎに行きます。

以下のようなアウトプットが返ってきます。

![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/693422/b42f126c-364a-4418-9983-be2a82d114a8.png)

詳細を開くと自然言語のプロンプトが KQL に変換されて要求を行っていることを確認できます。
![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/693422/859aab9c-0d93-436a-b7ed-4eeb89a50939.png)


---
### AI Agent で FOCUS の分析
まずどの FinOps Capability の強化が可能かいくつかシナリオを示します。

#### 💰 コストの可視化とアロケーションパターン

| 分析ニーズ                          | FinOps フレームワークとの整合性                         | 検証済みの自然言語クエリ |
|-----------------------------------|---------------------------------------------------------|---------------------------|
| エグゼクティブ向けコスト傾向レポート | [Reporting and analytics](https://www.finops.org/framework/capabilities/reporting-and-analytics/) | "Show monthly billed and effective cost trends for the last 12 months." |
| リソースグループごとのコストランキング | [Allocation](https://www.finops.org/framework/capabilities/allocation/) | "What are the top resource groups by cost last month?" |
| 四半期ごとの財務レポート            | [Allocation](https://www.finops.org/framework/capabilities/allocation/) / [Reporting and analytics](https://www.finops.org/framework/capabilities/reporting-and-analytics/) | "Show quarterly cost by resource group for the last 3 quarters." |
| サービスレベルのコスト分析         | [Reporting and analytics](https://www.finops.org/framework/capabilities/reporting-and-analytics/) | "Which Azure services drove the most cost last month?" |
| 組織的なコスト配分                 | [Allocation](https://www.finops.org/framework/capabilities/allocation/) / [Reporting and analytics](https://www.finops.org/framework/capabilities/reporting-and-analytics/) | "Show cost allocation by team and product for last quarter." |

#### 🧠異常検知とモニタリングパターン

| 分析ニーズ                        | FinOps フレームワークとの整合性                                                                 | 検証済みの自然言語クエリ |
|----------------------------------|--------------------------------------------------------------------------------------------------|---------------------------|
| コストスパイクの特定             | [Anomaly management](https://www.finops.org/framework/capabilities/anomaly-management/)        | "Find any unusual cost spikes or anomalies in the last 30 days." |
| 予算差異分析                     | [Budgeting](https://www.finops.org/framework/capabilities/budgeting/)                          | "Show actual vs. budgeted costs by resource group this quarter." |
| トレンド分析                     | [Reporting and analytics](https://www.finops.org/framework/capabilities/reporting-and-analytics/) | "Identify resources with consistently increasing costs over the last 6 months." |
| しきい値モニタリング             | [Anomaly management](https://www.finops.org/framework/capabilities/anomaly-management/)        | "Alert me to any single resources costing more than $5,000 monthly." |

など考えられます。他の Capability に対するプロンプトの例などか以下を参照してください。

<https://techcommunity.microsoft.com/blog/finopsblog/a-practitioners-guide-to-accelerating-finops-with-github-copilot-and-finops-hubs/4420302>

---
ここから出力の例になります。
####  [検証] 予測

３か月後のコスト予測をさせました。ここでは Agent が何度かトライしてクエリを書き直し結果を出力している様子が見えます。

![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/693422/e9aecfb2-9d91-4c6d-b4be-1cc681a6c9be.png)

![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/693422/ca42ddd2-7730-424d-9db0-de9cdc6a2a16.png)

---
####  [検証] コストスパイク (Anomaly)

![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/693422/f9522169-22ae-4dd9-8293-f48a0629f4ba.png)
>↓出力結果を抜粋しています。

Confidence: High  
Scope: Last 6 months, all resources

💰 **Key finding:**  
No unusual cost spikes detected—only one month of cost data is available (`June 2025: $1,888.55`). Month-over-month analysis is not possible with a single data point.

Recommendations

1. **Immediate:**  
   - Continue monitoring as more months of data accumulate.
2. **Next:**  
   - Set up automated monthly trend analysis to catch future spikes as soon as new data is available.
---
#### [検証] 最適化
copilot-instructions.md の Excucution Framwork で
THINK → PLAN → VERIFY → EXECUTE → VALIDATE
の順で実行され、いきなりクエリを実行するのではなく、まず「THINK」で目的を明確にし、「VERIFY」でスキーマを確認することで、無駄な作業やエラーを防げます。
また「VALIDATE」で“本当に効果があるか”を確認することで、単なるデータ分析ではなく、実際のコスト削減アクションに直結する提案を手助けしてくれます。

![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/693422/9f1ad90f-de6a-4cce-a17f-884973ee6946.png)

最適化アクションを求めると推奨事項が提示されます。
コスト支出の高い Top 3 のリソースで絞りました。
>VM に関しては検証用 AVD のため 1日1回ほどのログインの為、size や電源管理が必要な旨が推奨されています。 

![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/693422/83b3539a-f304-4440-941e-5593cd557283.png)

:::note
1. THINK（目的の明確化）
目的は「アクション可能なコスト最適化提案」を得ること。
例: 高コストリソースの特定、未使用リソースの検出、SKU の見直しなど。
2. PLAN（計画）
Costs テーブルを中心に、以下のような観点でクエリを設計：
高コストリソースの抽出（例: 上位10件）
使用率が低い SKU の特定
リザーブドインスタンス未使用のリソース
リージョンや SKU の変更によるコスト削減可能性
3. VERIFY（検証）
スキーマやデータの整合性を確認。
クエリを実行する前に、Agent にクエリを提示してレビューを受ける。
4. EXECUTE（実行）
Agent にクエリを実行させるか、FinOps Hub 上で実行。
結果をもとに、どのリソースに対してアクションを取るべきかを判断。
5. VALIDATE（検証）
提案されたアクションが実際にコスト削減につながるかを確認。
:::
---
最後にクエリ最適化ベストプラクティス として以下のことが挙げれていますので、今時点では制限により工夫が必要です。

:::note warn
Azure Data Explorer にはデフォルトで 64MB の結果制限があります。適切なクエリの最適化により、タイムアウトを回避し、信頼性の高いパフォーマンスを確保できます。Power BI を使用する場合は、データに接続する際に DirectQuery を使用してください。
:::


大規模データセットによるタイムアウト
- **問題**: 大きなデータセットを対象としたクエリでタイムアウトエラーが発生
- **解決策**: 時間フィルター（期間指定）を追加する

✅ 推奨: `"直近30日間のコストを表示"`  
❌ 避けるべき: `"すべてのコストを表示"`

- **FinOps Frameworkとの整合性**: [Data ingestion](https://www.finops.org/framework/capabilities/data-ingestion/)

---

メモリ制限例外
- **問題**: Azure Data Explorer の 64MB 結果制限を超えてエラーが発生
- **解決策**: 集計関数を使用する

✅ 推奨: `"月ごとのコストを集計して表示"`  
❌ 避けるべき: `大規模期間での日次粒度データ取得`

- **ベストプラクティス**: 要約→詳細への段階的ドリルダウンを実装する

---

スキーマ検証エラー
- **問題**: クエリ結果が空になる、または予期しないカラムが返ってくる
- **解決策**: データベースガイドを参照して、Hubのスキーマバージョンとの互換性を確認

- **検証方法**: クエリカタログ内の既知のクエリを使ってテスト

---

時間フィルタリング
✅ `"2025年Q1の月次コストを表示"`  
❌ `"すべての過去のコストを日次で表示"`

集約優先アプローチ
✅ `"コストの高いリソースグループTOP10を表示"`  
❌ `"すべてのリソースとその個別コストを表示"`

マルチサブスクリプションの取り扱い
✅ `"本番環境のサブスクリプションごとのコストを表示"`  
❌ `"すべてのサブスクリプションのコストをフィルターなしで表示"`

---
### 3: Wrap up

AI の爆発的な成長に伴い、FinOps における AI の活用はますます重要になっています。特に「AI のコストがどこにかかっているのか？」という基本的な理解を深めるために、AI Agent の活用が有効であることを本記事では示しました。

GitHub Copilot と FinOps hubs、Azure MCP Server を組み合わせることで、専門的なクエリ言語の知識がなくても、自然言語によるコスト分析が可能になります。

一方で、現時点では AI Agent の動作において不安定な点も見られ、クエリの失敗や応答の揺らぎなど、ツールとしての成熟には今後の改善が必要です。

AI for FinOps は、まだ発展途上の分野ではありますが、組織の FinOps Capability を強化する重要な手段となることは間違いありません。今後も継続的に検証を重ねていくことで、より確かな活用方法が見えてくるでしょう。

ではでは。
