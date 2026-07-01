Title: Azure VM イメージ標準化で考えるべきこと — Cloud Adoption Framework の観点で整理
Date: 2026-06-02
Modified: 2026-06-02
Slug: azure-image-standardization-principles
Lang: ja-jp
Category: notebook
Tags: azure, cloud-adoption-framework, virtual-machines, golden-image, azure-policy, compliance, governance
Summary: Azure における VM イメージ標準化（ゴールデンイメージ）を、Cloud Adoption Framework と Azure アーキテクチャ センターの参照アーキテクチャに基づき、ビルド・配布・統制・パッチ運用のライフサイクル順に整理する。

「イメージの標準化」を進めようとすると、まず「何をどこまで標準化するのか」「どの順序で進めるのか」「作ったあと守らせる仕組みをどうするのか」で手が止まりがちです。本記事では特定環境の事情に依存しない**一般論**として、Azure における **VM（IaaS）のイメージ標準化** で考えるべきことを、Microsoft の Cloud Adoption Framework（CAF）と Azure アーキテクチャ センターの公式ガイダンスに基づいて整理します。

> 本記事のスコープは VM ゴールデンイメージ（OS イメージ）に絞ります。コンテナイメージ・AKS ノードイメージ・AVD イメージは設計原則も統制点も別物のため、別途整理が必要です。

## 1. まず定義と公式根拠をそろえる

### 1.1 イメージ標準化は 3 レイヤで捉える

「イメージ標準化」は単一の作業ではなく、**3 つのレイヤ**の組み合わせとして捉えると議論が噛み合います。

| レイヤ | 内容 | 代表的な成果物 |
|--------|------|----------------|
| L1: 中身の標準化 | OS バージョン、導入エージェント、設定、ハードニングを揃える | ベースライン仕様、イメージ ビルド テンプレート |
| L2: 配布・バージョニングの標準化 | どこに置き、どう versioning し、どうレプリケートするか | Azure Compute Gallery、バージョン規約 |
| L3: 利用統制・可視化の標準化 | 「承認済みイメージしか使わせない」をどう強制し、どう逸脱を検知するか | Azure Policy、マシン構成、コンプライアンス ダッシュボード |

3 レイヤすべてを設計しないと「作ったが守られない」状態になります。**標準化 = L1（中身を揃える）だけ**と誤解されやすいため、最初に全体像を共有することが重要です。

### 1.2 CAF と Azure アーキテクチャ センターの役割

「CAF に書いてあるか?」への答えは **Yes** です。ただし CAF 本体は**原則・プロセス**を方法論（メソドロジ）横断で示し、**具体的な実装パターン**は Azure アーキテクチャ センターの参照アーキテクチャが担う、という役割分担になっています[^1][^2]。

イメージ標準化に関係する CAF の主な接点は以下です。

- **Govern（統制）**: 組織標準とポリシーを定義し、準拠状況を監視・是正する。「承認済みイメージの強制」「設定ドリフトの検知」はここに属します[^3]。
- **Manage（運用）**: 運用ベースラインの一部として、パッチ・構成・コンプライアンスを継続的に維持する[^4]。
- **Secure（セキュリティ）**: 「整合性（integrity）の原則」として、**自動構成管理**と**自動パッチ管理**を継続的に行うことを求めています。新規システムを自動で登録し、ポリシーに沿って継続管理する考え方です[^5]。
- **Ready（ランディング ゾーン）**: 管理・運用コンプライアンスの設計領域で、イメージや構成の標準化を土台として扱います[^1]。

これらの原則を **VM 向けに具体化した参照アーキテクチャ**が、Azure アーキテクチャ センターの「Manage virtual machine compliance（VM コンプライアンスの管理）」です。Azure VM Image Builder・Azure Compute Gallery・Azure Policy を組み合わせ、**DevOps の俊敏性を損なわずに**コンプライアンスを担保する設計を示しています[^2]。

### 1.3 公式参照アーキテクチャの 2 プロセス

公式の参照アーキテクチャは、イメージ標準化を**2 つのプロセス**に分解しています[^2]。

1. **ゴールデンイメージ発行プロセス**: Marketplace の最新ベースイメージを取得し、VM Image Builder でカスタマイズ、イメージ タトゥーイング、自動テストを経て、完成版を Azure Compute Gallery へ発行する。
2. **VM コンプライアンス追跡プロセス**: Azure Policy が VM にポリシー定義を割り当て、準拠状況を評価し、Azure Policy のコンプライアンス ダッシュボードに公開する[^2][^6]。

本記事では、この 2 プロセスを「ビルド時」「配布時」「統制・可視化」「運用時」に分けて整理します。

## 2. 全体像 — ビルド・配布・統制・運用を一つのライフサイクルにする

イメージ標準化とパッチ運用は別々の作業ではなく、**正しいイメージで VM を生み、稼働中も正しい状態を保ち、常に測って強制する**一つのライフサイクルとして捉えます。

![イメージ標準化とパッチ運用の全体像](/images/azure-image-standardization-principles/standardization-patch-overview.png)

（編集ソース：[/images/azure-image-standardization-principles/standardization-patch-overview.drawio](/images/azure-image-standardization-principles/standardization-patch-overview.drawio) ／ ベクター版：[standardization-patch-overview.drawio.svg](/images/azure-image-standardization-principles/standardization-patch-overview.drawio.svg)）

- **① ビルド時**: Marketplace 最新ベース → VM Image Builder でカスタマイズ → 自動テスト → Azure Compute Gallery へ発行・レプリケート → DevOps が承認イメージのみで VM を展開する。
- **② 統制・可視化**: Azure Policy が承認イメージを強制し、マシン構成で設定ドリフトを検知する。Defender for Cloud は規制コンプライアンスや脆弱性情報を可視化し、優先順位付けに使う。
- **③ 運用時**: 稼働中 VM には Azure Update Manager でランタイム パッチを適用する。パッチ前にはプレイベントで復旧ポイントを取得し、失敗時に戻せる状態を作る。

以降は、このライフサイクル順に論点を整理します。

## 3. 設計論点をライフサイクル順に整理する

### 3.1 対象 VM を Pets / Cattle に分ける

VM を **Pets（個別管理・代替困難）** と **Cattle（同質・容易に再作成可能）** に分類します。Cattle は定期的に作り直して準拠を保てますが、Pets はリフレッシュが難しく、可視化と個別追跡が必要です。分類によってリフレッシュ戦略と統制の重さが変わります[^2]。

- **Cattle**: 計画メンテナンス ウィンドウで定期的に作り直す。
- **Pets**: 廃止がアプリ障害やスケールアウト失敗につながるため慎重に扱う。Pet 用タグを付与し、Azure Policy でリフレッシュ時に考慮する[^2]。

### 3.2 L1（中身）— Marketplace 最新を起点にカスタマイズする

ゴールデンイメージは Marketplace の最新イメージにカスタマイズを重ねて作ります。DevOps チームには **Marketplace イメージの直接利用を許可せず**、Compute Gallery 発行のイメージのみを許可するのが原則です[^2]。

カスタマイズ内容は組織ごとに異なりますが、公式参照アーキテクチャでは一般例として次が挙げられています[^2]。

- OS ハードニング
- Microsoft 以外のソフトウェア用カスタム エージェントの展開
- エンタープライズ CA ルート証明書の組み込み

ビルド時にあわせて検討する代表論点は以下です。

- **Trusted Launch**: 第 2 世代 VM では Secure Boot、vTPM、Boot Integrity Monitoring により起動から実行までの信頼の連鎖を確立できます。ただし対応する VM サイズ・OS イメージが限られるため、検証工程で互換性を確認します[^7][^2]。
- **イメージ タトゥーイング**: 出自・OS バージョン・カスタムイメージ版・発行日などを、Windows ではレジストリ、Linux では環境変数や `/etc/` 配下のファイルにキーバリューで保存し、Azure Policy で追跡・レポートできる形にします[^2]。
- **SBOM（ソフトウェア部品表）**: OS パッケージ、エージェント、ライブラリ、パッチなどを記録します。Microsoft SBOM tool を使い、SPDX 形式で出力してイメージと紐づけて保管する方法が参照アーキテクチャで示されています[^2][^8]。
- **イメージ衛生**: 参照アーキテクチャは、イメージにシークレットを焼き込まない、環境ごとに変わる設定は外出しする、共通で必要なコンポーネントだけに絞る、アプリケーションコードをイメージに含めない、ビルドスクリプトを再現可能にする、という原則を挙げています[^2]。

> 送信接続の注意: AIB のカスタマイズや検証スクリプトが更新プログラムの取得などで外部接続を必要とする場合、ビルド VM / 検証 VM を置くサブネットは送信アクセスを許可する必要があります[^23]。また Azure の既定送信アクセスは暗黙的で非決定的な挙動であり、2026-03-31 後の API で作成される新規 VNet は既定で private subnet になるため、NAT Gateway など明示的な送信方式を設計するのが安全です[^24]。

### 3.3 L2（配布）— Compute Gallery で発行・版管理・リージョン配布する

Azure VM Image Builder の `distribute` は **ManagedImage / SharedImage / VHD** をサポートします。Compute Gallery に発行する場合は `SharedImage` distribution を使い、Compute Gallery の**イメージ バージョン**として配布します[^23]。

Compute Gallery は、Gallery / Image definition / Image version の階層でカスタム VM イメージを管理し、イメージ バージョンを必要リージョンにレプリケートできます[^9][^23]。

設計時に確認するポイントは以下です。

- **バージョン規約**: 自動採番にするか、明示的なバージョン番号を指定するかを決める。AIB の `galleryImageId` は自動バージョンと明示バージョンのどちらにも対応します[^23]。
- **リージョン配布**: API `2022-07-01` 以降は、`SharedImage` distribution のリージョン配布には `targetRegions` を使います。旧 `replicationRegions` は非推奨です[^23]。
- **古い版の扱い**: 古い版は EoL（end of life date）や `excludeFromLatest` を使い、「latest」要求時に選ばれないように管理します[^2][^23]。
- **誤削除対策**: Compute Gallery の soft delete はプレビュー機能で、誤って削除された ACG イメージを 7 日間の保持期間内に復旧できます[^26]。

### 3.4 L3（統制・可視化）— 承認イメージを強制し、ドリフトを検知する

承認イメージを作っても、利用側が Marketplace から直接 VM を作れる状態では標準化は維持できません。参照アーキテクチャでは、Azure Policy で DevOps チームが Compute Gallery のイメージだけを使うよう制限することを示しています[^2]。

- **承認イメージの強制**: Azure Policy のカスタム ポリシーで「承認された発行元 / 承認された Compute Gallery イメージ以外からの VM 作成」を拒否する。Microsoft は `allowed-image-publishers` のサンプルを公開しています[^2][^10]。
- **設定ドリフトの検知**: Azure Policy の **マシン構成（machine configuration）** 機能で、イメージが確立した OS 設定を監査し、ドリフト発生時に非準拠としてマークします[^2][^11]。
- **規制コンプライアンスの可視化**: Microsoft Defender for Cloud では、規制コンプライアンス標準を割り当てて準拠状況を可視化できます[^29]。
- **CVE 検知**: Microsoft Defender Vulnerability Management は、デバイスの脆弱性を CVE 単位で示し、検知ロジックも確認できます。Defender for Servers ではサーバー向けの脆弱性管理機能を利用できます[^27][^28]。

### 3.5 運用時 — Azure Update Manager と OOB を分けて考える

イメージのリフレッシュ（再焼き）とは別に、**稼働中 VM のランタイム パッチ**が必要です。CAF Secure の「整合性の原則」が求める**自動パッチ管理**の実装として、Azure Update Manager でメンテナンス構成・適用・準拠状況の可視化を行います[^5][^12]。

一方、重大 CVE が出た場合は、月次のゴールデンイメージ更新を待てません。**帯域外（OOB: out-of-band）の緊急パッチ プロセス**を月次とは独立に用意します[^2]。

| 対象 | 目的 | 主な仕組み |
|------|------|------------|
| 既存 VM | いま稼働中の VM をその場で修正する | Azure Update Manager |
| ゴールデンイメージ | これから作る VM が脆弱版から生まれないようにする | AIB パイプラインのオンデマンド実行 + Compute Gallery 新版発行 |

OOB の基本手順は次のとおりです[^2]。

1. 影響を受けたイメージ バージョンは Compute Gallery で `excludeFromLatest` を `true` にし、「latest」要求時に選ばれないようにする。
2. 同じ VM Image Builder パイプラインをオンデマンドで起動し、修正を適用する。
3. **検証を省略しない**。月次と同じ自動テストを実行する。
4. パッチ済み版を発行し、必要リージョンへレプリケートする。タトゥーに CVE 識別子・パッチ日・OOB フラグを記録する。

> OOB は月次サイクルを**補完**するものであり、置き換えではありません。累積更新を取り込むため月次リフレッシュは継続します[^2]。

## 4. 実装パターン

### 4.1 VM Image Builder で発行を自動化する

ここで言う「発行の自動化」とは、**人手でイメージを作って手動アップロードする**運用をやめ、**定期または必要時に起動する一連のパイプライン**として、ベースイメージ取得からカスタマイズ・検証・Compute Gallery への発行までを機械的に回すことを指します。Azure VM Image Builder（AIB）は、この「カスタマイズして発行する」工程を宣言的なテンプレートで定義できるマネージド サービスです[^2][^13]。

![VM Image Builder による発行自動化フロー](/images/azure-image-standardization-principles/aib-publish-flow.png)

（編集ソース：[/images/azure-image-standardization-principles/aib-publish-flow.drawio](/images/azure-image-standardization-principles/aib-publish-flow.drawio) ／ ベクター版：[aib-publish-flow.drawio.svg](/images/azure-image-standardization-principles/aib-publish-flow.drawio.svg)）

1. **スケジューラ / CI/CD / 手動実行**でパイプラインを起動する。AIB の `autoRun` はテンプレート作成時に一度だけ実行する機能です。継続的な自動ビルドには AIB trigger を使えますが、現在サポートされる trigger 種別は **SourceImage** であり、新しいソースイメージが利用可能になったときにビルドを起動します。月次など時刻ベースの運用は Azure DevOps Pipelines、GitHub Actions、Automation、Logic Apps など外部のスケジューラ / オーケストレーターで制御します[^23][^25]。
2. **Marketplace の最新ベースイメージ**を取得する。
3. **VM Image Builder でカスタマイズ**する（OS ハードニング、エージェント導入、社内 CA 証明書の組み込みなど）。
4. **タトゥーイング**で版情報を刻み、**SBOM** で中身を記録する。
5. **自動テスト**として一時 VM をデプロイし検証する。**失敗したらカスタマイズ工程へ差し戻す**（発行しない）。
6. 合格版を **Azure Compute Gallery のイメージ バージョン**として発行する。
7. **必要リージョンへレプリケート**する。
8. **DevOps チームは Compute Gallery 発行イメージのみを利用**し、Marketplace 直接利用は Azure Policy で禁止する。

重要なのは、**この自動化により「常に最新・常に検証済み・常に承認済み」のイメージだけが流通する**状態を作れる点です。

### 4.2 「クリーンなベース + customize でハードニング」を当てるテンプレート例

「Marketplace 最新を起点にカスタマイズを重ねる」を AIB で実装する基本形は、**素の Marketplace イメージを `source` にして、`customize` でハードニング（OS 設定・エージェント導入・証明書組み込みなど）を当てる**という構成です。AIB テンプレートは `source`（起点）/ `customize`（加工）/ `distribute`（発行先）/ `identity`（実行 ID）のブロックで構成されます[^13][^23]。

#### customize ブロックの仕様（事実）

`customize` は配列で、次の仕様があります[^23]。

- サポートされる customizer タイプは **`File` / `PowerShell` / `Shell` / `WindowsRestart` / `WindowsUpdate`** の 5 種類。
- customizer は**テンプレートに記述した順に実行**され、**1 つでも失敗すると customize 全体が失敗**してエラーを返す。
- **`Shell` は Linux、`PowerShell` は Windows** 用。**Linux 用の再起動 customizer は存在しない**（Windows の再起動は `WindowsRestart`）。
- `scriptUri` で外部スクリプトを参照する場合、**スクリプトは公開アクセス可能**であるか、**ユーザー割り当て ID（MSI）を構成**してアクセスさせる必要がある。
- **`inline` コマンドはテンプレート定義の一部として保存され、ダンプすると閲覧できる**。パスワード・SAS トークン・認証トークンなどの**機密値は inline に書かず**、Azure Storage 上のスクリプトに移して ID 認証で取得する。
- `scriptUri` を使う場合は **`sha256Checksum`** をローカルで生成して指定する。AIB 側でチェックサムを検証する。

#### 例 1: Linux（素の Ubuntu + Shell でハードニング スクリプトを適用）

```json
{
  "type": "Microsoft.VirtualMachineImages/imageTemplates",
  "apiVersion": "2022-07-01",
  "location": "japaneast",
  "identity": {
    "type": "UserAssigned",
    "userAssignedIdentities": {
      "<user-assigned-identity-resource-id>": {}
    }
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
        "targetRegions": [
          {
            "name": "japaneast",
            "replicaCount": 1,
            "storageAccountType": "Standard_ZRS"
          },
          {
            "name": "japanwest",
            "replicaCount": 1,
            "storageAccountType": "Standard_ZRS"
          }
        ]
      }
    ]
  }
}
```

`scriptUri` が指す `harden.sh` は、たとえば次のように書きます。スーパー ユーザー権限が必要な処理は **`sudo` を前置**します（AIB が文書化している記法）[^23]。

```bash
#!/bin/bash -e

# 例: SSH の root ログインを無効化する（実際の項目は組織のベースラインで定義する）
echo "Hardening: disable SSH root login"
sudo sed -i 's/^#\?PermitRootLogin.*/PermitRootLogin no/' /etc/ssh/sshd_config

# 例: 不要サービスを停止・無効化する
echo "Hardening: disable unused service"
sudo systemctl disable --now avahi-daemon || true
```

> ハードニングの**中身（どの設定をどう変えるか）は組織のセキュリティ ベースラインで定義する**ものです。AIB が担保するのは「そのスクリプトを順序どおり実行し、失敗したら発行しない」という**実行と検証のメカニズム**です。

#### 例 2: Windows（素の Windows Server + PowerShell・最新更新・再起動）

Windows では `PowerShell` でスクリプトを当て、`WindowsUpdate` で最新更新を取り込み、`WindowsRestart` で再起動します。`PowerShell` の `runElevated` / `runAsSystem` で昇格実行を指定できます[^23]。

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
    "updateLimit": 20
  },
  {
    "type": "WindowsRestart",
    "restartTimeout": "10m"
  }
]
```

`WindowsUpdate` customizer の `searchCriteria` / `filters` / `updateLimit` は、適用する更新の検索条件・絞り込み・上限件数を指定するプロパティです[^23]。

### 4.3 Azure Update Manager のプレイベントでパッチ前バックアップを自動化する

ビルド時のイメージ パイプラインが「常に正しいイメージで VM を生む」仕組みだとすると、運用フェーズでは「稼働中 VM に安全にパッチを当てる」仕組みが必要です。Azure Update Manager のスケジュール（メンテナンス構成）には**プレ イベント / ポスト イベント**を紐づけられ、メンテナンス ウィンドウの開始前・終了後に独立したタスクを自動実行できます[^21]。プレ イベントは Event Grid 経由で Webhook（Automation Runbook など）を起動できるため、**「パッチを当てる前に必ず復旧ポイントを取得する」**といった運用を自動化できます[^21][^22]。

![スケジュール パッチ適用とプレイベント自動バックアップの自動化フロー](/images/azure-image-standardization-principles/patch-automation-flow.png)

（編集ソース：[/images/azure-image-standardization-principles/patch-automation-flow.drawio](/images/azure-image-standardization-principles/patch-automation-flow.drawio) ／ ベクター版：[patch-automation-flow.drawio.svg](/images/azure-image-standardization-principles/patch-automation-flow.drawio.svg)）

1. **メンテナンス構成**（ゲスト パッチ スケジュール）が、メンテナンス開始前に**プレ メンテナンス イベント**を発行する[^21]。
2. **Event Grid**（システム トピック → Webhook）がイベントを受け、**Automation Runbook**（PowerShell）を起動する[^22]。
3. Runbook は **Azure Resource Graph** と Managed Identity を使い、今回の対象 VM を解決する（スケジュールの相関 ID を手がかりにする）。
4. プレイベントの自動処理として、凍結（ブラックアウト）期間の確認 → 対象 VM の解決 → オンデマンド バックアップ（Backup Now） → バックアップ完了の監視 → スナップショット取得（Instant Restore＝復旧ポイント確保） → パッチ適用へ続行、と進める。
5. **凍結期間中**や**失敗・タイムアウト時**は、キャンセル ウィンドウ内に**スケジュールをキャンセル**してパッチを止める。
6. 結果は **Logic App / Webhook / アラート**で通知する。

ポイントは、**パッチ適用の前に復旧ポイント（バックアップ / スナップショット）を自動取得しておく**ことで、適用に失敗しても素早くロールバックできる状態を運用が自動で作る点です。なお、プレ イベントには**実行時間の上限（キャンセル ウィンドウ）**があるため、重い処理は時間内に収まるよう設計する（あるいは非同期に逃がす）必要があります[^21]。

## 5. 現行で CIS Hardened Image を使っている場合の考え方

すでに CIS Hardened Image を使っている場合、その投資を活かしつつ標準化の 3 レイヤに正しく載せ直すことが論点になります。CIS Hardened Image は L1（中身を強化した状態で生む）を担う選択肢の一つですが、**「使っていること」自体が L2（配布・バージョニング）や L3（統制・可視化）の完成を意味するわけではありません**。

確認すべきことは次のとおりです。

- **発行・バージョニングに乗っているか**: CIS Hardened Image をそのまま使うのではなく、Compute Gallery に取り込み、自組織のエージェント・証明書・固有設定を上乗せしたうえで、標準の発行プロセスに合流させる。
- **更新サイクルを固定していないか**: 使っている CIS Hardened Image の版、更新頻度、基準改訂への追従方法を確認し、ゴールデンイメージの月次リフレッシュや OOB と整合させる。
- **測り続けているか**: CIS Hardened Image で生まれた VM も運用中にドリフトします。Azure Policy のマシン構成と Defender for Cloud の規制コンプライアンス評価で、設定や準拠状況を継続的に確認します[^11][^29]。
- **適用範囲を決めているか**: CIS Benchmark のプロファイルや Level、MCSB / STIG など他基準との関係を確認し、互換性検証と例外管理を設計します。
- **費用・サポート・更新主体を確認しているか**: Marketplace のイメージ利用条件、サポート条件、更新主体は契約・提供元に依存するため、設計前に確認します。

> CIS 標準イメージで準拠する方法と、標準イメージ + Defender for Cloud で準拠させる方法のメリット・デメリット比較は、別記事「[CIS 準拠をどう作るか — CIS 標準イメージと Defender for Cloud の使い分け]({filename}2026-06-02-azure-cis-compliance-defender-for-cloud.md)」で詳しく整理しています。

## 6. 進める順序（段階導入の一般論）

一度に全部をやろうとせず、段階的に進めるのが現実的です。

1. **可視化フェーズ**: 現状のイメージ・OS・利用経路を棚卸しし、Compute Gallery と Azure Policy（Audit モード）を用意して逸脱を観測する。
2. **パイプライン フェーズ**: VM Image Builder で発行を自動化し、最初の版を検証環境から段階適用する。Azure Update Manager の基本構成も整える。
3. **統制強化フェーズ**: 承認イメージ強制の Azure Policy を **Audit → Deny** へ昇格する。ただし昇格は「期間」ではなく、例外申請プロセス・承認イメージの供給・既存パイプライン改修・可視化が整った**準備度（Readiness）**で判断する。

## 7. 設計前のヒアリング項目（Microsoft ドキュメント準拠）

設計に着手する前に確認すべき項目を、本記事が参照する Microsoft の公式ドキュメントが**設計上の決定事項として挙げているもの**に絞って整理します。責任分界（RACI）・体制・期限・台数といった**組織固有の事情や推測は含めません**（それらは公式ドキュメントの設計事項ではないため本節の対象外）。

### 7.1 全体スコープと前提

- 対象のサブスクリプション / **管理グループ階層**と環境分離（本番 / 検証 / 開発）。Azure ランディング ゾーンは、管理グループ階層で環境・ワークロードを分離する設計を示しています[^14]。
- 準拠の判定基準（ベンチマーク）をどれにするか。Azure では **Microsoft クラウド セキュリティ ベンチマーク（MCSB）** が既定の評価基準として提供されます[^15]。CIS など別基準を使う場合はその版も確認します。
- 標準化を新規 VM のみに効かせるか、既存 VM も対象にするか（コンプライアンス追跡プロセスの適用範囲）。

### 7.2 イメージの中身（L1）

- 標準イメージに含める必須エージェント:
  - 監視: **Azure Monitor Agent**[^16]
  - セキュリティ: **Microsoft Defender for Servers**[^17]
  - バックアップ: **Azure Backup**（バックアップ ポリシー / Recovery Services vault / VM 拡張）[^18]
- ハードニング基準（MCSB / CIS / STIG）と適用範囲。MCSB を基準にする場合は Defender for Cloud で評価できます[^15]。
- **Trusted Launch**（Secure Boot / vTPM）を既定にするか[^7]。
- タトゥーイングと SBOM の項目・保管場所・保持期間をどうするか[^2][^8]。

### 7.3 ビルド・配布（L2）

- **ビルド（作る）**: イメージの**カスタマイズと検証を自動化**するか。**Azure VM Image Builder（AIB）**は、ベースイメージ取得・カスタマイズ・検証を宣言的テンプレートで実行するマネージド サービスです[^13]。
- **起動方式**: 月次など時刻ベースの実行は外部スケジューラ / CI/CD で制御するか。AIB trigger は現在 **SourceImage** trigger をサポートし、新しいソースイメージが利用可能になったときにビルドを起動します[^25]。
- **配布（届ける）**: 完成イメージの**発行・バージョニング・レプリケーション**をどう行うか。**Azure Compute Gallery** が発行先・版管理・リージョン配布を担います[^9]。AIB と Compute Gallery は択一ではなく、**AIB でビルドした成果物を Compute Gallery に発行する**補完関係です[^2][^23]。
- 必要リージョン、レプリカ数、ストレージ種別（`targetRegions`）をどう設計するか[^23]。
- ネットワーク制約。AIB のビルド / 検証 VM や、Isolated Builds で使う ACI サブネットが必要な通信を行えるよう、送信アクセス・サブネット委任・NSG を設計します[^20][^23][^24]。

### 7.4 利用統制・可視化（L3）

- 承認イメージの強制方針と、Audit から Deny への昇格をどう判断するか。評価・強制は **Azure Policy** で行います[^6]。
- 設定ドリフトの検知に **Azure Policy のマシン構成**を使うか[^11]。
- 規制コンプライアンス標準（MCSB / CIS など）の割り当てと、Defender for Cloud での可視化範囲をどうするか[^29]。
- Critical CVE の検知・優先度付けに Defender for Servers / Microsoft Defender Vulnerability Management を使うか[^27][^28]。

### 7.5 パッチ運用

- ランタイム パッチに **Azure Update Manager** を使うか。AUM は定期評価・スケジュール適用（メンテナンス構成）・準拠状況の可視化を提供します[^12]。
- 「イメージ再焼き」と「ランタイム パッチ」の役割分担を決めているか。
- パッチ前バックアップやスナップショット取得を、AUM のプレイベント / Event Grid / Automation Runbook で自動化するか[^21][^22]。
- OOB 緊急パッチ時に、旧版の `excludeFromLatest=true`、オンデマンド ビルド、テスト、発行、通知をどこまで自動化するか[^2][^23]。

### 7.6 ライセンス・コスト

- Windows Server / SQL で **Azure Hybrid Benefit** を適用するか[^19]。
- Compute Gallery のレプリカ・ストレージ増分コスト（レプリカ数とリージョン数に比例）[^9]。
- VM Image Builder、ストレージ、データ転送、ハイブリッド / Arc リソースの費用をどう見積もるか[^2]。

## 8. まとめ — 設計前チェックリスト

最後に、設計前レビューで確認する項目を細かく分解します。ここでは「Yes / No」で答えられる粒度に寄せ、未決ならヒアリング・設計タスクとして残せる形にします。

### 8.1 スコープと前提

- [ ] 今回の対象が **VM ゴールデンイメージ**であり、コンテナ / AKS ノード / AVD / VM Applications は対象外または別設計であることを明記したか
- [ ] 標準化を **L1（中身）/ L2（配布）/ L3（統制・可視化）** の 3 レイヤに分けて説明できるか
- [ ] 対象の管理グループ / サブスクリプション / 環境（本番・検証・開発）を確認したか
- [ ] 新規 VM のみを対象にするのか、既存 VM も対象にするのかを決めたか
- [ ] 対象 VM を **Pets / Cattle** に分類し、リフレッシュしやすい VM と個別管理が必要な VM を分けたか
- [ ] 準拠基準（MCSB / CIS / STIG など）と、その版・適用範囲を確認したか

### 8.2 L1: イメージの中身

- [ ] ベースは **Marketplace 最新 + カスタマイズ**を起点にする方針になっているか
- [ ] 対象 OS の publisher / offer / sku / generation を確認したか
- [ ] OS ハードニングで適用する基準と除外項目を定義したか
- [ ] 標準搭載するエージェント（Azure Monitor Agent / Defender for Servers / バックアップ関連）を決めたか
- [ ] 社内 CA ルート証明書など、全 VM に共通で必要な証明書・構成を整理したか
- [ ] アプリケーションコードや環境別設定をゴールデンイメージへ焼き込まない方針になっているか
- [ ] パスワード、SAS トークン、接続文字列、秘密鍵などのシークレットをイメージや inline script に含めない設計になっているか
- [ ] Trusted Launch（Secure Boot / vTPM / Boot Integrity Monitoring）の要否と、OS / VM サイズ互換性を確認したか
- [ ] イメージ タトゥーイングで記録する項目（元イメージ、OS 版、カスタムイメージ版、発行日など）を定義したか
- [ ] Windows ではレジストリ、Linux では `/etc/` 配下のファイル等、タトゥー情報の保存場所を決めたか
- [ ] SBOM の生成タイミング、形式（例: SPDX）、保管場所、保持期間を決めたか

### 8.3 AIB ビルド パイプライン

- [ ] AIB Image Template の `source` / `customize` / `distribute` / `identity` の責務を説明できるか
- [ ] `source` に PlatformImage / ManagedImage / SharedImageVersion のどれを使うか決めたか
- [ ] `customize` の各ステップを、実行順序どおりに整理したか
- [ ] Shell / PowerShell / File / WindowsUpdate / WindowsRestart のどの customizer を使うか決めたか
- [ ] 外部スクリプトを `scriptUri` で参照する場合、アクセス方式（公開 / Managed Identity）を決めたか
- [ ] `scriptUri` を使うスクリプトの `sha256Checksum` を生成・管理する手順を用意したか
- [ ] Windows Update customizer を使う場合、`searchCriteria` / `filters` / `updateLimit` を定義したか
- [ ] 再起動が必要な Windows カスタマイズに `WindowsRestart` を入れるか確認したか
- [ ] Linux には Linux 用 restart customizer がない前提で、再起動が必要な処理をどう扱うか確認したか
- [ ] ビルド / 検証 VM が必要な送信先へ到達できるよう、サブネット、NSG、NAT Gateway / Firewall 等を設計したか
- [ ] Isolated Builds を使う場合、ACI 用サブネット、委任、ビルド VM サブネットとの通信要件を確認したか
- [ ] AIB の起動方式を、外部スケジューラ / CI/CD / 手動実行 / SourceImage trigger / OOB 実行に分けて整理したか
- [ ] `autoRun` はテンプレート作成時の 1 回実行であり、継続的な月次スケジュールとは別物だと確認したか

### 8.4 自動テストと発行判定

- [ ] 発行前に一時 VM をデプロイして検証する手順を用意したか
- [ ] 起動確認、ログイン確認、エージェント起動、証明書配置、セキュリティ設定などのテスト項目を定義したか
- [ ] ハードニングがアプリ互換性に与える影響を検証する観点を入れたか
- [ ] テスト失敗時に発行せず、カスタマイズ工程へ差し戻すフローになっているか
- [ ] テスト結果、ビルドログ、生成された SBOM、タトゥー情報を追跡できるか
- [ ] 月次ビルドと OOB ビルドで、同じ自動テストを実行する方針になっているか

### 8.5 L2: Compute Gallery の配布・版管理

- [ ] Gallery / Image definition / Image version の命名規約を定義したか
- [ ] OS 種別、世代、セキュリティ機能、用途別に Image definition をどう分けるか決めたか
- [ ] Image version の採番を AIB 自動採番にするか、明示バージョンにするか決めたか
- [ ] 配布先リージョンを洗い出したか
- [ ] `targetRegions` の `name` / `replicaCount` / `storageAccountType` を設計したか
- [ ] レプリカ数とストレージ種別が、同時展開数・可用性・コストに合っているか確認したか
- [ ] 古いバージョンの EoL（end of life date）設定方針を決めたか
- [ ] `excludeFromLatest` を使う条件（脆弱版、廃止予定版、OOB 対応時など）を決めたか
- [ ] 誤削除対策として Compute Gallery soft delete（プレビュー）の利用要否を確認したか
- [ ] DevOps チームが参照すべき Gallery / Image definition / Image version を明確にしたか

### 8.6 L3: 利用統制・可視化

- [ ] Marketplace イメージの直接利用を許可するか禁止するか決めたか
- [ ] Compute Gallery 発行イメージのみを許可する Azure Policy を Audit で観測できるか
- [ ] Audit での観測期間、例外洗い出し、修正完了条件を決めたか
- [ ] Deny へ昇格する準備条件（承認イメージ供給、例外手続き、既存パイプライン改修、利用者周知）を定義したか
- [ ] Azure Policy の割り当てスコープ（管理グループ / サブスクリプション / リソース グループ）を決めたか
- [ ] Azure Policy の assignment description に、利用者向けの手順や内部ドキュメントへのリンクを載せるか決めたか
- [ ] Azure Policy のマシン構成で監査する OS 設定を決めたか
- [ ] マシン構成の remediation を自動適用するか、監査のみで始めるか決めたか
- [ ] Defender for Cloud で割り当てる規制コンプライアンス標準（MCSB / CIS など）を決めたか
- [ ] Defender for Servers / Microsoft Defender Vulnerability Management で Critical CVE を検知・優先度付けする運用を決めたか

### 8.7 ランタイム パッチと OOB

- [ ] 稼働中 VM のランタイム パッチは Azure Update Manager で管理する方針になっているか
- [ ] Azure Update Manager の評価、スケジュール、メンテナンス構成、準拠状況の確認方法を決めたか
- [ ] パッチ対象 VM の分類（OS、環境、重要度、メンテナンス ウィンドウ）を決めたか
- [ ] プレイベント / ポストイベントを使うか決めたか
- [ ] プレイベントでバックアップ、復旧ポイント、スナップショット取得を行うか決めたか
- [ ] Event Grid → Webhook → Automation Runbook の起動経路を設計したか
- [ ] 凍結（ブラックアウト）期間中にパッチを止める判定をどこで行うか決めたか
- [ ] 失敗・タイムアウト時にキャンセル ウィンドウ内で止める手順を用意したか
- [ ] パッチ結果の通知先（Logic App / Webhook / アラートなど）を決めたか
- [ ] OOB 緊急パッチで、影響を受ける Image version を特定する手順を用意したか
- [ ] OOB 時に旧版へ `excludeFromLatest=true` を設定する手順を用意したか
- [ ] OOB 用のオンデマンド AIB ビルド、テスト、発行、レプリケーション手順を用意したか
- [ ] OOB 対応後も、通常の月次リフレッシュを継続する方針になっているか

### 8.8 既存 CIS Hardened Image 利用時

- [ ] 現在使っている CIS Hardened Image の publisher / offer / sku / version を棚卸ししたか
- [ ] その CIS Hardened Image の更新頻度と、最新追従方法を確認したか
- [ ] CIS Hardened Image をそのまま使うのではなく、Compute Gallery の標準発行プロセスに載せるか決めたか
- [ ] 追加する自組織設定（エージェント、証明書、監視、バックアップ等）を整理したか
- [ ] CIS の Level / プロファイルと、アプリ互換性検証の範囲を決めたか
- [ ] Defender for Cloud / Azure Policy のマシン構成で、CIS 由来の設定が運用中にドリフトしていないか測る設計になっているか
- [ ] Marketplace の利用条件、費用、サポート条件、更新主体を確認したか

### 8.9 コスト・運用準備

- [ ] Compute Gallery のリージョン数、レプリカ数、ストレージ種別に応じたコストを見積もったか
- [ ] AIB のビルド、ストレージ、データ転送に関わるコストを見積もったか
- [ ] Defender for Cloud / Defender for Servers の有効化範囲とコストを確認したか
- [ ] Azure Hybrid Benefit を適用する OS / SQL ワークロードを確認したか
- [ ] 運用手順書に、通常ビルド、OOB、AUM パッチ、例外申請、ロールバックの手順を分けて記載したか
- [ ] 変更履歴、承認履歴、ビルド成果物、SBOM、テスト結果を監査時に提示できる形で保管するか決めたか

イメージ標準化は「きれいなイメージを 1 つ作る」ことではなく、**作り続け・配り続け・守らせ続ける仕組み**を CAF の Govern / Manage / Secure の原則に沿って構築することだと言えます。

---

[^1]: Cloud Adoption Framework の概要, <https://learn.microsoft.com/azure/cloud-adoption-framework/overview>

[^2]: Manage virtual machine compliance（Azure アーキテクチャ センター）, <https://learn.microsoft.com/azure/architecture/example-scenario/security/virtual-machine-compliance>

[^3]: Securely govern your cloud estate（CAF Secure: Govern）, <https://learn.microsoft.com/azure/cloud-adoption-framework/secure/govern>

[^4]: Manage your cloud operations（CAF Manage）, <https://learn.microsoft.com/azure/cloud-adoption-framework/manage/ready-cloud-operations>

[^5]: Perform your cloud adoption securely — Adopt the principle of integrity（CAF Secure）, <https://learn.microsoft.com/azure/cloud-adoption-framework/secure/adopt#adopt-the-principle-of-integrity>

[^6]: Azure Policy の概要, <https://learn.microsoft.com/azure/governance/policy/overview>

[^7]: Azure VM の Trusted Launch, <https://learn.microsoft.com/azure/virtual-machines/trusted-launch>

[^8]: Microsoft SBOM tool, <https://github.com/microsoft/sbom-tool>

[^9]: Azure Compute Gallery の概要, <https://learn.microsoft.com/azure/virtual-machines/azure-compute-gallery>

[^10]: Azure Policy サンプル: allowed image publishers, <https://github.com/Azure/azure-policy/tree/master/samples/Compute/allowed-image-publishers>

[^11]: Azure Policy のマシン構成機能, <https://learn.microsoft.com/azure/governance/machine-configuration/overview>

[^12]: Azure Update Manager の概要, <https://learn.microsoft.com/azure/update-manager/overview>

[^13]: Azure VM Image Builder の概要, <https://learn.microsoft.com/azure/virtual-machines/image-builder-overview>

[^14]: 管理グループ（Azure ランディング ゾーンの設計領域）, <https://learn.microsoft.com/azure/cloud-adoption-framework/ready/landing-zone/design-area/resource-org-management-groups>

[^15]: Microsoft クラウド セキュリティ ベンチマークの概要, <https://learn.microsoft.com/security/benchmark/azure/introduction>

[^16]: Azure Monitor Agent の概要, <https://learn.microsoft.com/azure/azure-monitor/agents/azure-monitor-agent-overview>

[^17]: Microsoft Defender for Servers プランの有効化, <https://learn.microsoft.com/azure/defender-for-cloud/tutorial-enable-servers-plan>

[^18]: Azure VM のバックアップの概要, <https://learn.microsoft.com/azure/backup/backup-azure-vms-introduction>

[^19]: Azure Hybrid Benefit（Windows VM のライセンス）, <https://learn.microsoft.com/azure/virtual-machines/windows/hybrid-use-benefit-licensing>

[^20]: Azure VM Image Builder のネットワーク オプション, <https://learn.microsoft.com/azure/virtual-machines/linux/image-builder-networking>

[^21]: Azure Update Manager のプレ イベントとポスト イベントの概要, <https://learn.microsoft.com/azure/update-manager/pre-post-scripts-overview>

[^22]: チュートリアル: Runbook を使った Webhook でプレ / ポスト イベントを実行する（Azure Update Manager）, <https://learn.microsoft.com/azure/update-manager/tutorial-webhooks-using-runbooks>

[^23]: Azure Image Builder の Bicep / ARM テンプレート（properties.customize / distribute / autoRun / networking）, <https://learn.microsoft.com/azure/virtual-machines/linux/image-builder-json>

[^24]: Default outbound access in Azure, <https://learn.microsoft.com/azure/virtual-network/ip-services/default-outbound-access>

[^25]: Azure Image Builder triggers, <https://learn.microsoft.com/azure/virtual-machines/image-builder-triggers-how-to>

[^26]: Soft Delete in Azure Compute Gallery, <https://learn.microsoft.com/azure/virtual-machines/soft-delete-gallery>

[^27]: Microsoft Defender Vulnerability Management のサーバー向け機能, <https://learn.microsoft.com/defender-vulnerability-management/defender-vulnerability-management-capabilities#vulnerability-management-capabilities-for-servers>

[^28]: Vulnerabilities in my organization（CVE detection logic）, <https://learn.microsoft.com/defender-vulnerability-management/tvm-weaknesses#cve-detection-logic>

[^29]: Defender for Cloud の規制コンプライアンス標準, <https://learn.microsoft.com/azure/defender-for-cloud/concept-regulatory-compliance-standards#available-compliance-standards>
