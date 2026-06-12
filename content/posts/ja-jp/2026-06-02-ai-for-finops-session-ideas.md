Title: AI for FinOps 登壇アイデア集 — 秋の Microsoft AI イベントで「刺さる」セッションをチームでブレストするために
Date: 2026-06-02
Slug: ai-for-finops-session-ideas
Lang: ja-jp
Category: notebook
Tags: finops, ai, azure, cost-management, generative-ai, focus, brainstorm
Summary: 秋の Microsoft AI イベント登壇に向けて、AI × FinOps をテーマに様々な業態の顧客へ刺さるセッション案を大量に整理したブレスト用カタログ。FinOps Foundation の最新動向と Azure のコスト管理ツールを根拠に、「AI で FinOps を加速する」「AI ワークロードのコストを FinOps で管理する」の 2 軸でアイデア・デモ案・KPI・業態別フック・タイトル案をまとめる。

秋の Microsoft AI イベントでの登壇に向けて、「AI for FinOps」をテーマに**チームでブレストするためのアイデア カタログ**です。様々な業態の顧客に刺さることを狙い、**事実ベース**で幅広く列挙します。各案はそのまま採用するものではなく、チームで取捨選択・組み合わせるための叩き台です。番号を振っているので、投票や絞り込みに使ってください。

> 注意（用語の流動性）: Microsoft の AI 関連サービス名（Azure OpenAI / Azure AI Foundry / Microsoft Foundry）や RBAC ロール名は改称が進行中で、PTU/予約などの提供形態も更新されています。イベント直前に最新の公式ドキュメントで再確認してください[^13]。

## 0. なぜ今「AI × FinOps」が刺さるのか（つかみのデータ）

ブレストの出発点として、需要の大きさを示すデータを押さえます。

- FinOps 実務者の **81% が AI を実務の生産性ツールとして重要**と回答（State of FinOps 2026）[^1]。
- **98% の FinOps 実務が AI 支出を管理**しており、「FinOps for AI」は**最も優先度の高い将来テーマ**[^2]。
- AI は**データセンター・ハイパースケーラ・SaaS・モデルベンダー・"AI ネオクラウド"**を横断する**新しい粒度の支出カテゴリ**であり、従来のクラウド FinOps とは異なる課題を持つ[^5]。

→ つまり「全業態・全規模の顧客が、いま現在困っている」テーマです。登壇の訴求軸になります。

## 1. 最初に整理すべき 2 つの軸

「AI for FinOps」は混同されがちな**2 つの方向**を含みます。セッション設計では必ず分けて語ると刺さりやすくなります。

| 軸 | 意味 | 一言で |
|----|------|--------|
| **A. AI で FinOps を加速する**（AI for FinOps） | 生成 AI / エージェント AI で FinOps の実務を速く・正確に・スケールさせる | 「FinOps の仕事を AI にやらせる」 |
| **B. AI のコストを FinOps で管理する**（FinOps for AI） | トークン・GPU・PTU など AI 特有のコストを可視化・最適化・統制する | 「AI の請求書を FinOps で御す」 |

FinOps Foundation は **B（FinOps for AI）を正式な技術カテゴリ／スコープ**として公開しており[^5]、**A** は同 Foundation のエージェント活用事例[^2] と Microsoft の FinOps hub AI エージェント ガイド[^9] が具体例を与えます。**両方を 1 本に欲張らず、どちらかを主・もう一方を従にする**のが設計の勘所です。

## 2. 「刺さる」ための 5 原則（評価軸にも使える）

アイデアを評価するときのフィルタとして使えます。

1. **デモ駆動**: 「自分の請求書に質問する」ライブ デモは普遍的に強い。スライドより動くものを[^9][^10]。
2. **横断性**: 特定業界に閉じない普遍課題（無駄削減・予測・配賦）を芯に、業態別フックを枝葉に。
3. **信頼ギャップへの誠実さ**: 多くの組織はまだ AI に本番変更を委ねていない。「Human-in-the-loop」「AI は副操縦士」を前提に語ると現実味が出て刺さる[^2]。
4. **イノベーションと統制のジレンマ**: 「すべての実験に NPV を求めると革新が止まる」という逆説に触れると経営層に響く[^2]。
5. **再現性**: 公式ツール（Cost Management / FinOps toolkit / FOCUS / MCP）で再現できる構成にすると、聴衆が持ち帰れる[^9][^14][^6]。

## 3. アイデア大量カタログ — A 群「AI で FinOps を加速する」

FinOps Foundation のエージェント活用事例[^2]・MCP ユースケース[^3] と、Microsoft の FinOps hub AI エージェント[^9]・Copilot in Azure[^10] を根拠にした案です。

1. **「請求書に何でも聞く」ライブ デモ**: 自然言語でコストを問い合わせる（例「コストが高い上位のリソース グループは？」）。FinOps hub × MCP × Azure MCP server を VS Code / Teams / M365 Copilot から実演[^9]。
2. **異常検知＋"理由"の自動説明**: スパイクを検知し、根本原因を平易な言葉で説明（AI 実験由来の急増に効く）[^2][^9][^17]。
3. **自律的な無駄発見（Agentic Waste Discovery）**: 遊休リソースをエージェントが調査→所有者特定→Jira 起票まで。調査時間「15 分→ほぼ 0」の事例[^2]。
4. **NL → KQL レポート生成**: 「直近 3 か月の増減トップ 5 を％付きで」など、KQL を書けない人でも経営報告を生成[^9]。
5. **予測 Q&A**: 「今月の着地見込みは？」を自然言語で。AI の予測困難性（短い予測ウィンドウ）への回答[^5][^9][^10]。
6. **コミットメント節約額の可視化**: 「コミットと交渉割引でいくら節約した？ 実効節約率（ESR）は？」[^9]。
7. **シフトレフトのコスト ガードレール**: PR 段階でエージェントが構成を FinOps ベスト プラクティスと照合し、デプロイ前にコスト影響を提示[^2]。
8. **パーソナライズド アウトリーチ＆ゲーミフィケーション**: 最後に触ったオーナーへ Slack/Teams で個別通知。**アクション率 40〜50%** の事例。節約時にマネージャへ自動通知して好循環[^2]。
9. **タグ/配賦のクリーンアップ支援**: 未ラベルのリソースを稼働時間や接続先から文脈推定してタグ付け、showback を改善[^2][^9]。
10. **MCP = "AI の USB‑C"** という比喩でアーキを解説。CSP の課金 API に直結し、ハルシネーションを抑えて最適化提案の精度を上げる closed‑loop[^3]。
11. **Copilot in Azure のコスト シミュレーション**: 「GPT 系モデルの利用が 15% 増えたら？」「モデルを切り替えたら財務影響は？」をデモ[^10]。
12. **"オーケストレーター エージェント"パターン**: ガバナンス／異常検知／タグ ポリシーの専門サブ エージェントへセマンティック ルーティングする設計[^2]。
13. **セキュリティ スコア改善 PR の自動生成**との合わせ技で「コスト×セキュリティ」を一気に語る[^2]。
14. **"丸投げしない"運用設計**: 信頼ギャップ前提で、承認フロー・検証ステップを残す現実的な MLOps/FinOpsOps[^2]。

## 4. アイデア大量カタログ — B 群「AI のコストを FinOps で管理する」

FinOps Foundation の FinOps for AI スコープ[^5] と Microsoft の AI コスト ドキュメント[^8][^11][^12][^13] が根拠です。

15. **「FinOps for AI は新しいダッシュボードではなく新しいスコープ」**という主題で、なぜ AI 支出が独自管理を要するかを語る[^5]。
16. **トークンから FOCUS へ**: ハイパースケーラ・ネオクラウド・SaaS をまたぐ AI 課金を FOCUS で正規化（現状 AI 専用列はなく、SKU/`ConsumedUnit=Tokens` で表現）[^5][^6]。
17. **AI 特有の KPI を主役に**: Cost per Token / Cost per Inference / Training Efficiency / Inference Efficiency / Token Consumption Efficiency / Time to First Prompt / ROI vs 期待値[^5]。
18. **ユニット エコノミクスで AI 投資を比較**: 「予測1件あたりコスト」「問い合わせ1件あたりコスト」で施策を相対評価[^4][^5]。
19. **PTU か従量か**: プロビジョニング（PTU／時間課金）と Standard（トークン従量）の損益分岐をデモ。予測可能・低遅延・本番大量は PTU 有利[^11]。
20. **予約で AI 容量を割引**: Microsoft Foundry Provisioned Throughput Reservations（1か月/1年）の落とし穴（容量保証ではない・デプロイ先行・種別非互換）を実務目線で[^12]。
21. **ファインチューニングの"隠れコスト"**: ホスティングは**未使用でも時間課金**。遊休デプロイの停止を訴求[^13]。
22. **トークン使用量の可視化**: Azure OpenAI の標準監視（HTTP / Tokens / PTU 使用率 / Fine‑tuning）でモデル・デプロイ別に追跡[^18]。
23. **AI 予算は"頻繁に見直す"**: 予測が数週間しか持たないなら数か月分の予算を渡さない。Fail‑fast の増分ファンディング[^4]。
24. **ハード スペンド キャップ**: 高速・実験的ワークロードに上限を設け、ユーザーに可視化[^4]。
25. **AI Investment Council（AI 投資委員会）**: クラウド/DevOps 黎明期の Tiger Team と同様、部門横断で AI 投資を評価・統制する仕組み[^4]。
26. **RAG か ファインチューニングか**: アプローチ選定が学習コスト vs 継続推論コストを左右する設計判断[^5]。
27. **容量戦略（GenAI Capacity Options）**: バースト初期は従量、希少性が高いと予約。動的なベンダー モデル（例: スケール ティア）にも触れる[^5]。
28. **成功/失敗（ハルシネーション）の切り分け**: 見積りで「有用な出力」と「無駄な出力」を分ける新しい計測課題[^5]。
29. **FinOps hub で AI 支出を一元化**: FOCUS エクスポートを取り込み、トークン/PTU/予約/AML GPU/Search を横断レポート[^9][^14][^15]。
30. **配賦の難所を正面から**: マルチエージェント構成で「どの呼び出し元がモデル出力を消費したか」を追えない問題と対処[^5]。

## 5. ライブ デモ案（Azure で再現可能なスクリプト）

聴衆が持ち帰れる、公式機能ベースのデモ案です。サンプル プロンプトは Microsoft Learn 由来[^9][^10]。

- **D1. 自然言語でコスト分析**: 「上位リソース グループ／サブスクリプション／タグ別のコストは？」→ エージェントが KQL を提示し、各行を説明、実行リンクを返す[^9]。
- **D2. 異常の検知と説明**: 「直近 3 か月で異常なスパイクは？」→ Data Explorer の異常検知で根本原因を提示[^9][^17]。
- **D3. 着地見込み**: 「高コスト サブスクの当月着地と来月予測は？」[^9]。
- **D4. 節約の説明責任**: 「コミット＋交渉割引の総節約額と実効節約率は？」[^9]。
- **D5. AI コスト シミュレーション**: Copilot in Azure で「モデル切替／利用増の財務影響」[^10]。
- **D6. PTU 損益分岐**: 同一ワークロードを Standard と PTU で試算し、分岐点を可視化[^11][^12]。

> デモ設計のコツ（出典準拠）: エージェントに**裏側の KQL を見せ・承認させる**ことで、信頼ギャップを逆手に取った"透明な AI"を演出できる[^9]。

## 6. 業態別フック（横展開のための枝葉）

普遍課題を芯に、各業態の関心へ接続します[^5][^9]。

- **金融・銀行**: ガバナンス／コンプライアンス（PCI・モデルリスク・監査性）が最重要。取締役会向けレポートと「AI が説明する異常」がリスク委員会に刺さる。
- **ヘルスケア・ライフサイエンス**: HIPAA・データ保持を一級 KPI に。GPU 集約（画像・ゲノム）のライトサイジング、"成果1件あたりコスト"。
- **小売・EC**: 季節性・バースト推論（レコメンド／チャットボット）→ Cost per Inference、オートスケール/停止、バッチ vs リアルタイム。
- **製造**: ワークロード配置（エッジ vs クラウド）、GPU 稼働率、持続可能性（リクエスト単位の環境負荷）。
- **公共**: 主権・AI 規制、不確実な予測下の厳格な予算/配賦、非技術職への自然言語セルフサービス。
- **ISV / SaaS**: ユニット エコノミクスが死活（席課金マージン vs トークン原価）。マルチモデル ルーティング、FOCUS 横断正規化、Time to First Prompt。
- **横断**: どの業界も「非技術者が"AI 開発者"になる」新ペルソナ問題と、統制を**捨てずに**速く動く課題を抱える[^5]。

## 7. セッション タイトル案（叩き台）

- 「**FinOps for AI: 新しいダッシュボードではなく、新しいスコープ**」[^5]
- 「**請求書に何でも聞いていい時代** — MCP で実現する自然言語 FinOps」[^3][^9]
- 「**トークンから FOCUS へ** — ハイパースケーラ／ネオクラウド／SaaS をまたぐ AI 課金の正規化」[^5][^6]
- 「**AI の KPI はこれだ** — Cost per Inference / Cost per Token / Time to First Prompt」[^5]
- 「**速く動け、意図を持って使え** — AI 投資委員会と容量戦略」[^4][^5]
- 「**AI に FinOps をやらせてみた** — エージェントが無駄を見つけ、起票するまで」[^2]
- 「**PTU か従量か** — AI 本番運用のコスト分岐点」[^11][^12]

## 8. セッション形式の選択肢

- **基調デモ型**: 1 本のストーリー（"請求書に質問→異常説明→是正→節約報告"）を通しデモ。最も汎用的に刺さる。
- **顧客ストーリー型**: 実顧客の Before/After（※顧客名・固有情報は伏せる）。
- **パネル型**: 金融×製造×ISV のクロス業態で「AI コストの悩み」を語らせる。
- **ハンズオン/ワークショップ型**: FinOps toolkit・FinOps hub・FOCUS エクスポートを各自が触る[^14][^15][^6]。
- **アーキテクチャ深掘り型**: MCP／Azure MCP server／オーケストレーター エージェントの実装解説[^3][^9]。

## 9. ブレストの進め方（提案）

1. **主軸を 1 つ選ぶ**（A か B）。欲張らない。
2. §2 の 5 原則で各アイデアに 1〜5 点を付け、上位を残す。
3. **通しデモのストーリー**を 1 本決め、そこに必要なアイデアだけを束ねる。
4. **対象業態を 2〜3 に絞り**、フック（§6）を差し込む。
5. **再現可能な構成**（§5 のデモ）に落とし、持ち帰り資料を用意。

### たたき台のおすすめ構成（一例）
**主軸=A（AI で FinOps を加速）×通しデモ**。「自然言語でコスト質問（#1）→異常検知と説明（#2）→自律的な無駄発見と起票（#3）→節約のパーソナライズド通知（#8）」を 1 本のデモにし、最後に **B の KPI（#17）と AI 投資委員会（#25）**で"統制も捨てない"と締める。横断業界として**金融・小売・ISV**のフックを差す。信頼ギャップ（#14）と NPV 逆説（原則 4）を要所に置くと経営層にも刺さります。

## 10. まとめ

- 需要は全業態に存在（81% が AI を実務に、98% が AI 支出を管理、FinOps for AI が最優先テーマ）[^1][^2]。
- **A（AI で FinOps を加速）/ B（AI のコストを FinOps で管理）を分けて**設計する[^5]。
- **デモ駆動・横断性・信頼ギャップ・NPV 逆説・再現性**の 5 原則で「刺さる」を担保。
- 公式の足場（Cost Management / Copilot in Azure / FinOps toolkit・hub / FOCUS / MCP / PTU・予約）で**持ち帰れる**セッションにする[^9][^10][^14][^6][^11][^12]。

---

[^1]: AI for FinOps（FinOps Foundation トピック）, https://www.finops.org/topic/ai-for-finops

[^2]: AI for FinOps: Agentic Use Cases（FinOps Foundation）, https://www.finops.org/insights/ai-for-finops-agentic-use-cases/

[^3]: Model Context Protocol (MCP) AI for FinOps Use Case（FinOps Foundation）, https://www.finops.org/wg/model-context-protocol-mcp-ai-for-finops-use-case/

[^4]: Managing AI Value in FinOps Practice Operations（FinOps Foundation）, https://www.finops.org/wg/managing-ai-value-finops-practice-operations/

[^5]: FinOps for AI — FinOps Framework Technology Category（FinOps Foundation）, https://www.finops.org/framework/technology-categories/ai/

[^6]: FOCUS — FinOps Open Cost & Usage Specification, https://focus.finops.org/

[^8]: Plan, manage, and monitor costs for Microsoft Foundry Models / Azure OpenAI, https://learn.microsoft.com/azure/ai-foundry/openai/how-to/manage-costs

[^9]: Configure and use AI agents（FinOps hubs / FinOps toolkit）, https://learn.microsoft.com/cloud-computing/finops/toolkit/hubs/configure-ai

[^10]: Analyze, estimate, and optimize cloud costs using Microsoft Copilot in Azure, https://learn.microsoft.com/azure/copilot/analyze-cost-management

[^11]: What is provisioned throughput?（PTU）, https://learn.microsoft.com/azure/ai-foundry/openai/concepts/provisioned-throughput

[^12]: Save costs with Microsoft Foundry Provisioned Throughput Reservations, https://learn.microsoft.com/azure/cost-management-billing/reservations/azure-openai

[^13]: Introduction to cost management for AI workloads（Microsoft Learn Training）, https://learn.microsoft.com/training/modules/understand-cost-management-ai/

[^14]: Microsoft FinOps toolkit overview, https://learn.microsoft.com/cloud-computing/finops/toolkit/finops-toolkit-overview

[^15]: FinOps hubs overview, https://learn.microsoft.com/cloud-computing/finops/toolkit/hubs/finops-hubs-overview

[^17]: Identify anomalies and unexpected changes in cost, https://learn.microsoft.com/azure/cost-management-billing/understand/analyze-unexpected-charges

[^18]: Monitor Azure OpenAI, https://learn.microsoft.com/azure/ai-foundry/openai/how-to/monitor-openai
