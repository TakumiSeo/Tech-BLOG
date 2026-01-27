Title: SRE Agent の資料作成ノート
Date: 2026-01-27
Slug: SRE-Agent-Planning
Lang: ja-jp
Category: notebook
Tags: azure, SRE Agent, AIOps
Summary: SRE Agent の概要資料を作成するための勉強ノート

## 画像運用（Azure Blob + Pelican）

このブログでは画像の固定 URL を
`https://technotesewo.blob.core.windows.net/image`
に統一します。

### 1. Blob 側の運用方針（公開コンテナ）

- コンテナ名: `image`（既存）
- 公開アクセス: **Blob（匿名読み取り）** を許可
- 目的: ブログからの参照は認証不要で高速に表示

> 参考: Azure Storage のコンテナ公開設定
> https://learn.microsoft.com/azure/storage/storage-explorer/vs-azure-tools-storage-explorer-blobs#set-the-public-access-level-for-a-blob-container

### 2. URL の運用ルール（固定 URL + 変更に強い）

- URL は **固定のベース** に統一
	- 例: `https://technotesewo.blob.core.windows.net/image/2026/01/diagram-v3.png`
- **更新時はファイル名でバージョン管理**
	- 例: `diagram-v3.png` のように末尾に `-vN` を付与
- 既存 URL を壊さない（過去記事の表示を保証）

### 3. Pelican の画像記法（Markdown）

#### 3-1. 標準 Markdown（推奨）

```markdown
![図の説明](https://technotesewo.blob.core.windows.net/image/2026/01/diagram-v3.png)
```

#### 3-2. HTML でサイズ指定したい場合

```html
<img src="https://technotesewo.blob.core.windows.net/image/2026/01/diagram-v3.png" alt="図の説明" width="720" height="360" loading="lazy" />
```

### 4. 画像の追加手順（運用フロー）

1. 画像を最適化（WebP/PNG、適切なサイズ）
2. Blob にアップロード（`image/2026/01/` のように年月で整理）
3. ブログ本文に URL を貼る

### 5. 注意事項

- **SAS は不要**（公開ブログ用途）
- 公開範囲を `image` コンテナに限定
- 画像の削除は慎重に（過去記事のリンク切れ防止）


