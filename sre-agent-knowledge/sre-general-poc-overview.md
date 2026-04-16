# SRE General PoC Overview

## Purpose

このドキュメントは Azure SRE Agent に環境の前提を共有するための概要資料です。
この PoC の目的は、Application Gateway 系と Azure Firewall 系の疑似障害に対して、SRE Agent が委任された権限の範囲で一次切り分けできることを確認することです。

## Scope

この PoC で主に検証する通信は次の 2 系統です。

- Client -> Firewall -> Application Gateway -> Firewall -> IIS
- AppVM -> Firewall -> Internet

## Main Resources

- Resource Group: rg-sre-general-poc
- Region: japaneast
- VNet: vnet-sre-general-poc
- Azure Firewall: azfw-sre-general-poc
- Firewall Policy: azfw-policy-sre-general-poc
- Application Gateway: appgw-sre-general-poc
- AppVM: appvm-sgpoc
- ClientVM: clientvm-sgpoc
- Private DNS zone: sre-general-poc.internal
- Log Analytics workspace: law-sre-general-poc

## Delegated Permissions

この PoC では、SRE Agent に次の権限を委任する前提です。

- Reader
- Monitoring Reader
- Log Analytics Reader

主な利用目的は次のとおりです。
- リソース構成の確認
- Azure Monitor と Log Analytics の参照
- ログ検索
- 状態要約
- runbook の参照と対応案の提示

シナリオ 1 では、backend health、AppGW 構成、関連 NSG / UDR / subnet 紐付け、診断設定などを確認するため、権限委任に基づく追加確認が発生する場合があります。

## Investigation Focus

この環境で重視する観測ポイントは次のとおりです。

- Application Gateway backend health
- AppGW 診断ログ
- Azure Firewall の AzureDiagnostics ログ
- Private DNS の A レコード
- Azure Monitor のメトリクスとアラート

## Model Selection Policy

- 疑似障害の調査、根本原因分析、ログ相関分析は Anthropic 系を優先します。
- 日次ヘルスチェック、週次セキュリティチェック、定期 compliance チェックは GPT 系を優先します。
- provider は agent 単位で設定されるため、用途を明確に分ける場合は調査用 agent と Scheduled Task 用 agent を分離します。

## Supported Scenarios

- AppGW backend Unhealthy
- Client 側 DNS 解決失敗
- AppGW backend FQDN 解決失敗
- AppVM 外向き通信障害
- 日次ヘルスチェック
- 週次セキュリティチェック
- 定期 compliance / 構成健全性チェック

## Constraints

- Azure Firewall のログは AzureDiagnostics テーブルを使用し、主に msg_s を参照します。
- Application Gateway の backend health は Healthy / Unhealthy / Unknown を確認します。
- VM 高負荷の根因プロセス特定は未対応です。
- 証拠不足の場合、SRE Agent は推測せず要追加確認として不足項目を返します。