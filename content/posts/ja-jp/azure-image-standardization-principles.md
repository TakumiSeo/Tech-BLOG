Title: Azure VM イメージ標準化で考えるべきこと — Cloud Adoption Framework の観点で整理
Date: 2026-06-02
Modified: 2026-06-02
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

## 5. 現行で CIS イメージを使っている場合の考え方

すでに CIS のハードン済みイメージ（CIS Hardened Image）を使っている場合、その投資を活かしつつ標準化の 3 レイヤに正しく載せ直すことが論点になります。CIS イメージは強力ですが、**「使っていること」自体が標準化の完成を意味しない**点に注意します。

### 5.1 CIS イメージは「予防（L1）」であって全体ではない

CIS イメージが担うのは **L1（中身を強化した状態で生む）= 予防的コントロール**です。配布・バージョニング（L2）と利用統制・ドリフト検知（L3）は別途設計しないと、「強い状態で生まれたが、運用中に劣化・逸脱する」状態になります。CIS イメージを使っていても、Compute Gallery への取り込み・バージョニング・Azure Policy による強制は引き続き必要です。

### 5.2 固定版を使い続けない（最新版をパイプラインに取り込む）

CIS イメージを**ある時点の版で固定したまま使い続けるのはアンチパターン**です。CIS は基準改訂と OS 更新に合わせてイメージを更新するため、**最新の CIS Hardened Image を月次でゴールデンイメージ パイプラインに取り込み**、§4.7 / §4.8 の発行・バージョニングに乗せてリフレッシュします。古い版は `excludeFromLatest` で除外します（§4.10）。

### 5.3 予防だけで終わらせず、Defender for Cloud で「測り続ける」

CIS イメージで生まれた VM も、運用中に設定が**ドリフト**します。これを検知するのが **L3 = 検出的コントロール**で、Azure Policy のマシン構成（§4.11）と **Microsoft Defender for Cloud の規制コンプライアンス評価**が担います。CIS イメージ（予防）と Defender for Cloud（検出）は**補完関係**であり、両方そろって「準拠を作り、保つ」が成立します。

### 5.4 Level 1 / Level 2 の適用範囲を決める

CIS Benchmark の **Level 1（機能を壊しにくい最低ライン）/ Level 2（多層防御だが互換性を犠牲にしうる）**のどちらをどこまで当てるかを決めます。実務では **Level 1 を全面適用 → Level 2 は対象を選んで段階適用**が定石で、Level 2 は必ず検証環境で互換性を確認します。

### 5.5 将来の選択肢 — 「標準イメージ + Defender」への寄せ替え

CIS イメージにはライセンス料と更新サイクルの第三者依存が伴います。内製でハードニングを維持できる余力が付けば、**標準イメージ + マシン構成 + Defender for Cloud** へ寄せてコストと依存を減らす移行も選べます。どちらを採るにせよ Defender for Cloud による継続監視は共通して必要です。

> CIS 標準イメージで準拠する方法と、標準イメージ + Defender for Cloud で準拠させる方法のメリット・デメリット比較は、別記事「[CIS 準拠をどう作るか — CIS 標準イメージと Defender for Cloud の使い分け]({filename}azure-cis-compliance-defender-for-cloud.md)」で詳しく整理しています。

## 6. 進める順序（段階導入の一般論）

一度に全部をやろうとせず、段階的に進めるのが定石です。

1. **可視化フェーズ**: 現状のイメージ・OS を棚卸しし、Compute Gallery と Azure Policy（**Audit モード**）を用意して逸脱を観測する。
2. **パイプライン フェーズ**: VM Image Builder で発行を自動化し、最初の版を本番へ段階適用。Update Manager の基本構成を整える。
3. **統制強化フェーズ**: 承認イメージ強制の Azure Policy を **Audit → Deny** へ昇格。ただし昇格は「期間」ではなく、例外申請プロセス・承認イメージの供給・既存パイプライン改修・可視化が整った**準備度（Readiness）**で判断する。

### 6.1 「VM Image Builder で発行を自動化する」とは

ここで言う「発行の自動化」とは、**人手でイメージを作って手動アップロードする**運用をやめ、**毎月（または必要時）に起動する一連のパイプライン**として、ベースイメージ取得からカスタマイズ・検証・Compute Gallery への発行までを**機械的に回す**ことを指します。Azure VM Image Builder（AIB）は、この「カスタマイズして発行する」工程を宣言的なテンプレートで定義し、トリガーで自動実行できるマネージド サービスです[^2][^13]。

具体的には、§3.1 のゴールデンイメージ発行プロセスを次のように一本のパイプラインにします[^2]。

![VM Image Builder による発行自動化フロー](/images/azure-image-standardization-principles/aib-publish-flow.png)

（編集ソース：[/images/azure-image-standardization-principles/aib-publish-flow.drawio](/images/azure-image-standardization-principles/aib-publish-flow.drawio) ／ ベクター版：[aib-publish-flow.drawio.svg](/images/azure-image-standardization-principles/aib-publish-flow.drawio.svg)）

1. **月次トリガー**でパイプラインを起動する（VM Image Builder のトリガー機能、またはスケジューラ）[^2]。
2. **Marketplace の最新ベースイメージ**を取得する（最新のセキュア設定を起点にするため）。
3. **VM Image Builder でカスタマイズ**する（OS ハードニング・エージェント導入・社内 CA 証明書の組み込みなど）。
4. **タトゥーイング**で版情報を刻み、**SBOM** で中身を記録する。
5. **自動テスト**として一時 VM をデプロイし検証する。**失敗したらカスタマイズ工程へ差し戻す**（発行しない）。
6. 合格版を **Azure Compute Gallery へ発行**する。
7. **必要リージョンへレプリケート**する。
8. **DevOps チームは Compute Gallery 発行イメージのみを利用**し、Marketplace 直接利用は **Azure Policy で禁止**する（§4.11）。

重要なのは、**この自動化により「常に最新・常に検証済み・常に承認済み」のイメージだけが流通する**状態を作れる点です。緊急の重大 CVE に対しては、月次サイクルとは独立に**同じパイプラインをオンデマンドで起動**して帯域外（OOB）パッチを当て、脆弱版は `excludeFromLatest=true` で「最新」要求から除外します（§4.10）。

### 6.1.1 「クリーンなベース ＋ customize でハードニング」を当てる — テンプレートの具体例

§3.1 の「Marketplace 最新を起点にカスタマイズを重ねる」を AIB で実装する基本形は、**ハードニング済みの第三者イメージを起点にするのではなく、素の Marketplace イメージを `source` にして、`customize` でハードニング（OS 設定・エージェント導入・証明書組み込みなど）を当てる**という構成です。AIB テンプレートは `source`（起点）/ `customize`（加工）/ `distribute`（発行先）/ `identity`（実行 ID）の 4 ブロックで構成されます[^13][^23]。

#### customize ブロックの仕様（事実）

`customize` は配列で、次の仕様があります[^23]。

- サポートされる customizer タイプは **`File` / `PowerShell` / `Shell` / `WindowsRestart` / `WindowsUpdate`** の 5 種類。
- customizer は**テンプレートに記述した順に実行**され、**1 つでも失敗すると customize 全体が失敗**してエラーを返す（＝検証で落ちれば発行されない）。
- **`Shell` は Linux、`PowerShell` は Windows** 用。**Linux 用の再起動 customizer は存在しない**（Windows の再起動は `WindowsRestart`）。
- `scriptUri` で外部スクリプトを参照する場合、**スクリプトは公開アクセス可能**であるか、**ユーザー割り当て ID（MSI）を構成**してアクセスさせる必要がある。
- **`inline` コマンドはテンプレート定義の一部として保存され、ダンプすると閲覧できる**。パスワード・SAS トークン・認証トークンなどの**機密値は inline に書かず**、Azure Storage 上のスクリプトに移して ID 認証で取得する。
- `scriptUri` を使う場合は **`sha256Checksum`** を**ローカルで生成**して指定する（Linux/Mac では `sha256sum <fileName>`）。AIB 側でチェックサムを検証する。

#### 例 1: Linux（素の Ubuntu ＋ Shell でハードニング スクリプトを適用）

```json
{
  "type": "Microsoft.VirtualMachineImages/imageTemplates",
  "apiVersion": "2022-02-14",
  "location": "japaneast",
  "identity": {
    "type": "UserAssigned",
    "userAssignedIdentities": { "<user-assigned-identity-resource-id>": {} }
  },
  "properties": {
    "source": {
      "type": "PlatformImage",
      "publisher": "Canonical",
      "offer": "0001-com-ubuntu-server-jammy",
      "sku": "22_04-lts-gen2",
      "version": "latest"
    },
    "customize": [
      {
        "type": "Shell",
        "name": "applyOsHardening",
        "scriptUri": "https://<storage-account>.blob.core.windows.net/scripts/harden.sh",
        "sha256Checksum": "<sha256sum harden.sh で生成した値>"
      }
    ],
    "distribute": [
      {
        "type": "SharedImage",
        "galleryImageId": "<compute-gallery-image-definition-id>",
        "runOutputName": "linuxHardened",
        "replicationRegions": [ "japaneast", "japanwest" ]
      }
    ]
  }
}
```

`scriptUri` が指す `harden.sh` は、たとえば次のように書きます。スーパー ユーザー権限が必要な処理は **`sudo` を前置**します（AIB が文書化している記法）[^23]。

```bash
#!/bin/bash -e

# 例: SSH の root ログインを無効化する（組織のベースラインで実際の項目を定義する）
echo "Hardening: disable SSH root login"
sudo sed -i 's/^#\?PermitRootLogin.*/PermitRootLogin no/' /etc/ssh/sshd_config

# 例: 不要サービスを停止・無効化する
echo "Hardening: disable unused service"
sudo systemctl disable --now avahi-daemon || true
```

> ハードニングの**中身（どの設定をどう変えるか）は組織のセキュリティ ベースラインで定義する**ものです。AIB が担保するのは「そのスクリプトを順序どおり実行し、失敗したら発行しない」という**実行と検証のメカニズム**です。

#### 例 2: Windows（素の Windows Server ＋ PowerShell・最新更新・再起動）

Windows では `PowerShell` でスクリプトを当て、`WindowsUpdate` で最新更新を取り込み、`WindowsRestart` で再起動します。`PowerShell` の `runElevated`/`runAsSystem` で昇格実行を指定できます[^23]。

```json
"source": {
  "type": "PlatformImage",
  "publisher": "MicrosoftWindowsServer",
  "offer": "WindowsServer",
  "sku": "2022-datacenter-azure-edition",
  "version": "latest"
},
"customize": [
  {
    "type": "PowerShell",
    "name": "applyOsHardening",
    "runElevated": true,
    "scriptUri": "https://<storage-account>.blob.core.windows.net/scripts/Harden.ps1",
    "sha256Checksum": "<生成した sha256 値>"
  },
  {
    "type": "WindowsUpdate",
    "searchCriteria": "IsInstalled=0",
    "filters": [ "exclude:$_.Title -like '*Preview*'", "include:$true" ],
    "updateLimit": 40
  },
  {
    "type": "WindowsRestart",
    "restartTimeout": "10m"
  }
]
```

`WindowsUpdate` customizer の `searchCriteria` / `filters` / `updateLimit` は、適用する更新の検索条件・絞り込み・上限件数を指定するプロパティです[^23]。

このように、**ベースは常にクリーンな Marketplace 最新**にしておき、組織固有のハードニングや構成は **`customize` のスクリプトとして外出し**して当てるのが基本形です。スクリプトを差し替えるだけで内容を更新でき、ベースの更新（`version: latest`）とハードニング内容の更新を独立して回せます。

### 6.2 「運用フェーズで自動的に行われること」— パッチ適用とプレイベント バックアップ

§6.1 のイメージ パイプラインが**ビルド時の自動化**（常に正しいイメージで VM を生む）だとすると、運用フェーズでは**ランタイムの自動化**（稼働中 VM に安全にパッチを当てる）が走ります。Azure Update Manager のスケジュール（メンテナンス構成）には**プレ イベント / ポスト イベント**を紐づけられ、メンテナンス ウィンドウの開始前・終了後に独立したタスクを自動実行できます[^21]。プレ イベントは Event Grid 経由で Webhook（Automation Runbook など）を起動できるため、**「パッチを当てる前に必ず復旧ポイントを取得する」**といった運用を自動化できます[^21][^22]。

下図は、その「運用で自動的に行われていること」を一般化したフローです。

![スケジュール パッチ適用とプレイベント自動バックアップの自動化フロー](/images/azure-image-standardization-principles/patch-automation-flow.png)

（編集ソース：[/images/azure-image-standardization-principles/patch-automation-flow.drawio](/images/azure-image-standardization-principles/patch-automation-flow.drawio) ／ ベクター版：[patch-automation-flow.drawio.svg](/images/azure-image-standardization-principles/patch-automation-flow.drawio.svg)）

1. **メンテナンス構成**（ゲスト パッチ スケジュール）が、メンテナンス開始前に**プレ メンテナンス イベント**を発行する[^21]。
2. **Event Grid**（システム トピック → Webhook）がイベントを受け、**Automation Runbook**（PowerShell）を起動する[^22]。
3. Runbook は **Azure Resource Graph** と Managed Identity を使い、今回の対象 VM を解決する（スケジュールの相関 ID を手がかりにする）。
4. プレイベントの自動処理として、①**凍結（ブラックアウト）期間の確認** → ②**対象 VM の解決** → ③**オンデマンド バックアップ（Backup Now）** → ④**バックアップ完了の監視** → ⑤**スナップショット取得（Instant Restore＝復旧ポイント確保）** → ⑥**パッチ適用へ続行**、と進める。
5. **凍結期間中**や**失敗・タイムアウト時**は、キャンセル ウィンドウ内に**スケジュールをキャンセル**してパッチを止める。
6. 結果は **Logic App / Webhook / アラート**で通知する。

ポイントは、**パッチ適用の前に復旧ポイント（バックアップ／スナップショット）を自動取得しておく**ことで、適用に失敗しても素早くロールバックできる状態を運用が自動で作る点です。なお、プレ イベントには**実行時間の上限（キャンセル ウィンドウ）**があるため、重い処理は時間内に収まるよう設計する（あるいは非同期に逃がす）必要があります[^21]。

> この図は「ランタイム パッチを安全に自動化する」運用パターンの一般例です。§4.12 で触れた「イメージ更新」と「ランタイム パッチ」の役割分担のうち、後者を具体化したものに当たります。

### 6.3 全体像（ビルド時 ＋ 運用時 ＋ 統制の一枚絵）

§6.1（ビルド時のイメージ パイプライン）と §6.2（運用時のパッチ自動化）は、**Azure Policy / Defender for Cloud による統制・可視化**を挟んで一つのライフサイクルとしてつながります。下図はその全体像を 1 枚にまとめたものです。

![イメージ標準化とパッチ運用の全体像](/images/azure-image-standardization-principles/standardization-patch-overview.png)

（編集ソース：[/images/azure-image-standardization-principles/standardization-patch-overview.drawio](/images/azure-image-standardization-principles/standardization-patch-overview.drawio) ／ ベクター版：[standardization-patch-overview.drawio.svg](/images/azure-image-standardization-principles/standardization-patch-overview.drawio.svg)）

- **① ビルド時**: Marketplace 最新ベース → VM Image Builder でカスタマイズ → 自動テスト → Azure Compute Gallery へ発行・レプリケート → DevOps が**承認イメージのみ**で VM を展開する（§3 / §6.1）。
- **② 統制・可視化**: **Azure Policy** が承認イメージを強制し、マシン構成で**ドリフトを検知**する。**Microsoft Defender for Cloud** が規制コンプライアンスを評価し**準拠を可視化**する（§4.11 / §5.3）。この層がビルドと運用の両方を横断して見張る。
- **③ 運用時**: 稼働中 VM に対し Azure Update Manager のスケジュールが**プレ メンテナンス イベント**を発行 → Event Grid → Automation Runbook が**凍結確認・対象解決・オンデマンド バックアップ・スナップショット（Instant Restore）**を行ってから**パッチ適用**へ進む。凍結中・失敗時はキャンセルし、結果を通知する（§4.12 / §6.2）。

ポイントは、**「正しいイメージで生む（ビルド時）」→「正しく動き続けさせる（運用時）」→「常に測って強制する（統制）」**の 3 つが途切れずに回ることです。イメージ標準化とパッチ運用は別々の作業ではなく、この一つのライフサイクルの異なる局面だと捉えると、設計の優先順位と役割分担が整理しやすくなります。

## 7. 設計前のヒアリング項目（Microsoft ドキュメント準拠）

設計に着手する前に確認すべき項目を、本記事が参照する Microsoft の公式ドキュメントが**設計上の決定事項として挙げているもの**に絞って整理します。責任分界（RACI）・体制・期限・台数といった**組織固有の事情や推測は含めません**（それらは公式ドキュメントの設計事項ではないため本節の対象外）。

### 7.1 全体スコープと前提

- 対象のサブスクリプション / **管理グループ階層**と環境分離（本番 / 検証 / 開発）。Azure ランディング ゾーンは、管理グループ階層で環境・ワークロードを分離する設計を示しています[^14]。
- 準拠の判定基準（ベンチマーク）をどれにするか。Azure では **Microsoft クラウド セキュリティ ベンチマーク（MCSB）** が既定の評価基準として提供されます[^15]。CIS など別基準を使う場合はその版も確認します（§5）。
- 標準化を新規 VM のみに効かせるか、既存 VM も対象にするか（コンプライアンス追跡プロセスの適用範囲、§3.2）。

### 7.2 イメージの中身（L1）

- 標準イメージに含める必須エージェント:
  - 監視: **Azure Monitor Agent**[^16]
  - セキュリティ: **Microsoft Defender for Servers**[^17]
  - バックアップ: **Azure Backup**（VM 拡張 / MARS）[^18]
- ハードニング基準（MCSB / CIS / STIG）と適用 Level（§5.4）。MCSB を基準にする場合は Defender for Cloud で評価できます[^15]。
- **Trusted Launch**（Secure Boot / vTPM）を既定にするか[^7]。

### 7.3 ビルド・配布（L2）

- **ビルド（作る）**: イメージの**カスタマイズと検証を自動化**するか。**Azure VM Image Builder（AIB）**は、ベースイメージ取得・カスタマイズ・検証を宣言的テンプレートで実行するマネージド サービスです[^13]。
- **配布（届ける）**: 完成イメージの**発行・バージョニング・レプリケーション**をどう行うか。**Azure Compute Gallery** が発行先・版管理・リージョン配布を担います[^9]。AIB と Compute Gallery は択一ではなく、**AIB でビルドした成果物を Compute Gallery に発行する**補完関係です[^2]。
- 必要リージョンとレプリケーション数（Compute Gallery のレプリカ設計）[^9]。
- ネットワーク制約。AIB は staging リソース グループに Azure Container Instance を展開し、既存 VNet / サブネットへ関連付ける設計が必要なため、閉域・Private 構成では事前確認が要ります[^20]。

### 7.4 利用統制（L3）

- 承認イメージの強制方針と、Audit から Deny への昇格をどう判断するか（§4.11 / §6）。評価・強制は **Azure Policy** で行います[^6]。
- 設定ドリフトの検知に **Azure Policy のマシン構成**を使うか[^11]。

### 7.5 パッチ運用

- ランタイム パッチに **Azure Update Manager** を使うか。AUM は定期評価・スケジュール適用（メンテナンス構成）・準拠状況の可視化を提供します[^12]。
- 「イメージ再焼き」と「ランタイム パッチ」の役割分担を決めているか（§4.12）。

### 7.6 ライセンス・コスト

- Windows Server / SQL で **Azure Hybrid Benefit** を適用するか[^19]。
- Compute Gallery のレプリカ・ストレージ増分コスト（レプリカ数とリージョン数に比例）[^9]。

## 8. まとめ — 設計前チェックリスト

- [ ] 標準化を L1（中身）/ L2（配布）/ L3（統制）の 3 レイヤで設計しているか
- [ ] Pets / Cattle を区別し、リフレッシュ戦略を分けているか
- [ ] ベースは Marketplace 最新 + カスタマイズになっているか
- [ ] Trusted Launch（Secure Boot / vTPM）を Day1 で検討したか
- [ ] イメージ タトゥーイングと SBOM で追跡性を確保しているか
- [ ] 発行前の自動テストと、月次リフレッシュ + OOB 緊急パッチを用意したか
- [ ] Azure Policy で承認イメージを強制し、マシン構成でドリフトを検知しているか
- [ ] Azure Update Manager でランタイム パッチを自動化したか
- [ ] Audit → Deny の昇格を準備度ベースで判断する計画があるか
- [ ] （CIS イメージ利用時）固定版を使い続けず最新版をパイプライン取り込みし、Defender for Cloud で準拠を測り続けているか

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

[^13]: Azure VM Image Builder の概要, https://learn.microsoft.com/azure/virtual-machines/image-builder-overview

[^14]: 管理グループ（Azure ランディング ゾーンの設計領域）, https://learn.microsoft.com/azure/cloud-adoption-framework/ready/landing-zone/design-area/resource-org-management-groups

[^15]: Microsoft クラウド セキュリティ ベンチマークの概要, https://learn.microsoft.com/security/benchmark/azure/introduction

[^16]: Azure Monitor Agent の概要, https://learn.microsoft.com/azure/azure-monitor/agents/azure-monitor-agent-overview

[^17]: Microsoft Defender for Servers プランの有効化, https://learn.microsoft.com/azure/defender-for-cloud/tutorial-enable-servers-plan

[^18]: Azure VM のバックアップの概要, https://learn.microsoft.com/azure/backup/backup-azure-vms-introduction

[^19]: Azure Hybrid Benefit（Windows VM のライセンス）, https://learn.microsoft.com/azure/virtual-machines/windows/hybrid-use-benefit-licensing

[^20]: Azure VM Image Builder のネットワーク オプション, https://learn.microsoft.com/azure/virtual-machines/linux/image-builder-networking

[^21]: Azure Update Manager のプレ イベントとポスト イベントの概要, https://learn.microsoft.com/azure/update-manager/pre-post-scripts-overview

[^22]: チュートリアル: Runbook を使った Webhook でプレ / ポスト イベントを実行する（Azure Update Manager）, https://learn.microsoft.com/azure/update-manager/tutorial-webhooks-using-runbooks

[^23]: Azure Image Builder の Bicep / ARM テンプレート（properties.customize）, https://learn.microsoft.com/azure/virtual-machines/linux/image-builder-json
