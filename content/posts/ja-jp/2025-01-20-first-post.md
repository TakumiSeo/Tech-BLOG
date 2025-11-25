Title: 最初の検証ログ
Date: 2025-01-20
Slug: first-post
Lang: ja-jp
Category: notebook
Tags: azure,static-web-apps,pelican
Summary: Cloud Diaries: Azure Edition の実験環境を紹介するキックオフ記事です。

Pelican 4.9 とカスタムテーマの組み合わせで、軽量かつ柔軟なブログ環境を用意しました。`codehilite` と Pygments により、コンソール出力や構成スクリプトも読みやすさを保ったまま貼り付けられます。

## サンプルスニペット
最初の自動デプロイでは、GitHub Actions のワークフローが Azure Static Web Apps に必要なアーティファクトを確実に生成することを検証します。

```yaml
name: azure-static-web-apps
on:
  push:
    branches: ["main"]
```

## 次のステップ
1. デスクトップとモバイル両方でダークモード表示を確認する。
2. CI 内で `npx swa build` を実行するスモークテストを追加する。
3. ARM/Bicep ベースのステージング環境構築について掘り下げる。
