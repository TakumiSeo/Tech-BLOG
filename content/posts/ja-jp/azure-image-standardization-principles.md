Title: Azure VM イメージ標準化で考えるべきこと — Cloud Adoption Framework の観点で整理
Date: 2026-06-02
Slug: azure-image-standardization-principles
Lang: ja-jp
Category: notebook
Tags: azure, cloud-adoption-framework, virtual-machines, golden-image, azure-policy, compliance, governance
Summary: Azure における VM イメージ標準化（ゴールデンイメージ）を、Cloud Adoption Framework の Govern / Manage / Secure / Ready 観点と、Azure アーキテクチャ センターの参照アーキテクチャを根拠に一般論として整理。設計前に押さえるべき論点をまとめる。

「イメージの標準化」を進めようとすると、まず「何をどこまで標準化するのか」「どの順序で進めるのか」「作ったあと守らせる仕組みをどうするのか」で手が止まりがちです。本記事では特定環境の事情に依存しない**一般論**として、Azure における **VM（IaaS）のイメージ標準化** で考えるべきことを、Microsoft の Cloud Adoption Framework（CAF）と Azure アーキテクチャ センターの公式ガイダンスに基づいて整理します。

> 本記事のスコープは VM ゴールデンイメージ（OS イメージ）に絞ります。コンテナイメージ・AKS ノードイメージ・AVD イメージは設計原則も統制点も別物のため、別途整理が必要です。

## 1. そもそも「イメージ標準化」とは何か

「イメージ標準化」は単一の作業ではなく、**3 つのレイヤ**の組み合わせとして捉えると議論が噛み合います。

| レイヤ | 内容 | 代表的な成果物 |
|--------|------|----------------|
| L1: 中身の標準化 | OS バージョン、導入エージェント、設定、ハードニングを揃える | ベースライン仕様、イメージ ビルド テンプレート |
| L2: 配布・バージョニングの標準化 | どこに置き、どう versioning し、どうレプリケートするか | Azure Compute Gallery、バージョン規約 |
| L3: 利用統制の標準化 | 「承認済みイメージしか使わせない」をどう強制するか | Azure Policy、コンプライアンス ダッシュボード |

3 レイヤすべてを設計しないと「作ったが守られない」状態になります。**標準化 = L1（中身を揃える）だけ**と誤解されやすいため、最初に全体像を共有することが重要です。

## 2. Cloud Adoption Framework はこれをどう位置づけているか

「CAF に書いてあるか?」への答えは **Yes** です。ただし CAF 本体は**原則・プロセス**を方法論（メソドロジ）横断で示し、**具体的な実装パターン**は Azure アーキテクチャ センターの参照アーキテクチャが担う、という役割分担になっています[^1][^2]。

イメージ標準化に関係する CAF の主な接点は以下です。

- **Govern（統制）**: 組織標準とポリシーを定義し、準拠状況を監視・是正する。「承認済みイメージの強制」「設定ドリフトの検知」はここに属します[^3]。
- **Manage（運用）**: 運用ベースラインの一部として、パッチ・構成・コンプライアンスを継続的に維持する[^4]。
- **Secure（セキュリティ）**: 「整合性（integrity）の原則」として、**自動構成管理**と**自動パッチ管理**を継続的に行うことを求めています。新規システムを自動で登録し、ポリシーに沿って継続管理する考え方です[^5]。
- **Ready（ランディング ゾーン）**: 管理・運用コンプライアンスの設計領域で、イメージや構成の標準化を土台として扱います[^1]。

そして、これらの原則を **VM 向けに具体化した参照アーキテクチャ**が、Azure アーキテクチャ センターの「Manage virtual machine compliance（VM コンプライアンスの管理）」です。Azure VM Image Builder・Azure Compute Gallery・Azure Policy を組み合わせ、**DevOps の俊敏性を損なわずに**コンプライアンスを担保する設計を示しています[^2]。

## 3. 標準化の全体像 — 2 つのプロセス

公式の参照アーキテクチャは、イメージ標準化を**2 つのプロセス**に分解しています[^2]。

### 3.1 ゴールデンイメージ発行プロセス

1. **ベースイメージの取得**: 毎月、Marketplace の**最新**ベースイメージを起点にする（最新には既定のセキュア設定が反映されるため）。
2. **カスタマイズ**: Azure VM Image Builder で OS ハードニング・エージェント導入・社内 CA 証明書の組み込みなどを適用する。
3. **イメージ タトゥーイング**: 出自・バージョン・発行日などの版情報をイメージに刻む。
4. **自動テスト**: 公開前に検証する。失敗したらカスタマイズ工程へ差し戻す。
5. **発行**: 完成版を Azure Compute Gallery に発行し、DevOps チームへ提供する。

### 3.2 VM コンプライアンス追跡プロセス

1. Azure Policy が VM にポリシー定義を割り当て、準拠状況を評価する。
2. 評価結果を Azure Policy のコンプライアンス ダッシュボードに公開し、組織全体で可視化する[^2][^6]。

## 4. 設計で考えるべき論点（一般論）

以下は環境に依存しない、設計前に必ず検討すべき論点です。すべて公式ガイダンスに根拠があります。

### 4.1 Pets と Cattle を区別する

VM を **Pets（個別管理・代替困難）** と **Cattle（同質・容易に再作成可能）** に分類します。Cattle は定期的に作り直して準拠を保てますが、Pets はリフレッシュが難しく、可視化と個別追跡が必要です。分類によってリフレッシュ戦略と統制の重さが変わります[^2]。

### 4.2 ベースは「Marketplace 最新 + カスタマイズ」

ゴールデンイメージは Marketplace の最新イメージにカスタマイズを重ねて作ります。DevOps チームには **Marketplace イメージの直接利用を許可せず**、Compute Gallery 発行のイメージのみを許可するのが原則です[^2]。

### 4.3 イメージの中身（L1）

カスタマイズ内容は組織ごとに異なりますが、一般的には次が含まれます[^2]。

- OS ハードニング（CIS / Microsoft セキュリティ ベースライン等の基準に準拠）
- 監視・セキュリティ・バックアップ等のエージェント導入
- 社内 CA ルート証明書の組み込み

> 注意: Azure の仮想ネットワークは既定で送信接続を持ちません。VM Image Builder のビルドで更新ダウンロード等の送信が必要な場合は、対象サブネットで送信アクセスを明示的に構成する必要があります[^2]。

### 4.4 Trusted Launch でハードウェア起点の信頼を確立する

第 2 世代 VM ではゴールデンイメージに **Trusted Launch** を組み込み、起動から実行までの信頼の連鎖を確立します。**Secure Boot**（署名済みローダ/カーネルのみ起動）、**vTPM**（鍵・証明書・起動測定値の保護）、**Boot Integrity Monitoring**（Microsoft Defender for Cloud へのテレメトリ）を有効化します。ただし対応する VM サイズ・OS イメージが限られるため、**検証工程で互換性を確認**します[^7][^2]。

### 4.5 イメージ タトゥーイング（版情報の刻印）

トラブルシュートと監査のため、イメージの出自・OS バージョン・カスタムイメージ版・発行日などを記録します。Windows ではレジストリ、Linux では環境変数や `/etc/` 配下のファイルにキーバリューで保存し、Azure Policy で追跡・レポートできる形にします[^2]。

### 4.6 SBOM（ソフトウェア部品表）を生成する

タトゥーイングが「イメージの出自（メタデータ）」を記録するのに対し、**SBOM はイメージの中身**（OS パッケージ、エージェント、ライブラリ、パッチ）を記録します。SBOM は次に効きます[^2]。

- **CVE への迅速な対応**: 重大脆弱性公表時に、影響を受ける版を即座に特定できる。
- **規制対応**: SBOM を要求する標準・法規制への準拠。
- **監査の追跡性**: タトゥーイングと組み合わせ、どの VM がどの版で何を含むかを完全に提示できる。

SBOM は VM Image Builder のパイプラインで**カスタマイズ直後・検証前**に生成し、オープンソースの Microsoft SBOM tool で SPDX 形式で出力、署名してイメージと一緒に保管します[^2][^8]。

### 4.7 自動テストで「常に最新」を保つ

通常はゴールデンイメージを**月次**でリフレッシュします。発行前に新規 VM をデプロイして自動テスト（起動時間の検証、カスタマイズ/エージェントの確認など）を実行し、失敗したらプロセスを止めて原因を是正してから再実行します[^2]。

### 4.8 発行・バージョニング・ライフサイクル（L2）

- Compute Gallery に**マネージド イメージ**として発行し、古い版は順次廃止（EoL）する[^2]。
- 誤削除に備え、Compute Gallery の**論理削除（soft delete）**を検討する（7 日間の回復ウィンドウ。プレビュー）[^2]。
- 最新イメージを**必要リージョンへレプリケート**し、ライフサイクルを Compute Gallery で管理する[^2][^9]。

### 4.9 リフレッシュ戦略

- **Cattle**: 計画メンテナンス ウィンドウで定期的に作り直す。
- **Pets**: 廃止がアプリ障害やスケールアウト失敗につながるため慎重に。Pet 用タグを付与し、Azure Policy でリフレッシュ時に考慮する。
- VM Image Builder の**トリガー**で月次の自動イメージ作成を構成できる[^2]。

### 4.10 緊急パッチ（OOB）プロセス

月次サイクルは定常更新向けで、重大 CVE はサイクルを待てません。**帯域外（OOB: out-of-band）の緊急パッチ プロセス**を月次とは独立に用意します[^2]。

1. 影響を受けた版は Compute Gallery で `excludeFromLatest` を `true` にし、「最新」要求時に選ばれないようにする。
2. 同じ VM Image Builder パイプラインをオンデマンドで起動し、修正を適用する。
3. **検証を省略しない**（月次と同じ自動テストを実行）。
4. パッチ済み版を発行し全リージョンへレプリケート。タトゥーに CVE 識別子・パッチ日・OOB フラグを記録する。

> OOB は月次サイクルを**補完**するものであり、置き換えではありません。累積更新を取り込むため月次リフレッシュは継続します[^2]。

### 4.11 統制（L3）— 承認イメージの強制とドリフト検知

- **承認イメージの強制**: Azure Policy のカスタム ポリシーで「Compute Gallery 発行イメージ以外からの VM 作成」を拒否する（`allowed-image-publishers` のサンプルが公開）[^2][^10]。
- **設定ドリフトの検知**: Azure Policy の **マシン構成（machine configuration）** 機能で、イメージが確立した OS 設定を監査し、ドリフト発生時に非準拠としてマークする[^2][^11]。

### 4.12 パッチ運用 — Azure Update Manager

イメージのリフレッシュ（再焼き）とは別に、**稼働中 VM のランタイム パッチ**が必要です。CAF Secure の「整合性の原則」が求める**自動パッチ管理**の実装として、Azure Update Manager でメンテナンス構成・適用・準拠状況の可視化を行います[^5][^12]。「イメージ更新」と「ランタイム パッチ」の役割分担を明確にすることが設計のポイントです。

## 5. 進める順序（段階導入の一般論）

一度に全部をやろうとせず、段階的に進めるのが定石です。

1. **可視化フェーズ**: 現状のイメージ・OS を棚卸しし、Compute Gallery と Azure Policy（**Audit モード**）を用意して逸脱を観測する。
2. **パイプライン フェーズ**: VM Image Builder で発行を自動化し、最初の版を本番へ段階適用。Update Manager の基本構成を整える。
3. **統制強化フェーズ**: 承認イメージ強制の Azure Policy を **Audit → Deny** へ昇格。ただし昇格は「期間」ではなく、例外申請プロセス・承認イメージの供給・既存パイプライン改修・可視化が整った**準備度（Readiness）**で判断する。

## 6. まとめ — 設計前チェックリスト

- [ ] 標準化を L1（中身）/ L2（配布）/ L3（統制）の 3 レイヤで設計しているか
- [ ] Pets / Cattle を区別し、リフレッシュ戦略を分けているか
- [ ] ベースは Marketplace 最新 + カスタマイズになっているか
- [ ] Trusted Launch（Secure Boot / vTPM）を Day1 で検討したか
- [ ] イメージ タトゥーイングと SBOM で追跡性を確保しているか
- [ ] 発行前の自動テストと、月次リフレッシュ + OOB 緊急パッチを用意したか
- [ ] Azure Policy で承認イメージを強制し、マシン構成でドリフトを検知しているか
- [ ] Azure Update Manager でランタイム パッチを自動化したか
- [ ] Audit → Deny の昇格を準備度ベースで判断する計画があるか

イメージ標準化は「きれいなイメージを 1 つ作る」ことではなく、**作り続け・配り続け・守らせ続ける仕組み**を CAF の Govern / Manage / Secure の原則に沿って構築することだと言えます。

---

[^1]: Cloud Adoption Framework の概要, https://learn.microsoft.com/azure/cloud-adoption-framework/overview

[^2]: Manage virtual machine compliance（Azure アーキテクチャ センター）, https://learn.microsoft.com/azure/architecture/example-scenario/security/virtual-machine-compliance

[^3]: Securely govern your cloud estate（CAF Secure: Govern）, https://learn.microsoft.com/azure/cloud-adoption-framework/secure/govern

[^4]: Manage your cloud operations（CAF Manage）, https://learn.microsoft.com/azure/cloud-adoption-framework/manage/ready-cloud-operations

[^5]: Perform your cloud adoption securely — Adopt the principle of integrity（CAF Secure）, https://learn.microsoft.com/azure/cloud-adoption-framework/secure/adopt#adopt-the-principle-of-integrity

[^6]: Azure Policy の概要, https://learn.microsoft.com/azure/governance/policy/overview

[^7]: Azure VM の Trusted Launch, https://learn.microsoft.com/azure/virtual-machines/trusted-launch

[^8]: Microsoft SBOM tool, https://github.com/microsoft/sbom-tool

[^9]: Azure Compute Gallery の概要, https://learn.microsoft.com/azure/virtual-machines/azure-compute-gallery

[^10]: Azure Policy サンプル: allowed image publishers, https://github.com/Azure/azure-policy/tree/master/samples/Compute/allowed-image-publishers

[^11]: Azure Policy のマシン構成機能, https://learn.microsoft.com/azure/governance/machine-configuration/overview

[^12]: Azure Update Manager の概要, https://learn.microsoft.com/azure/update-manager/overview
