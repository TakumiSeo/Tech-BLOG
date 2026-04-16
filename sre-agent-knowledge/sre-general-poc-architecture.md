# SRE General PoC Architecture

## Network Topology

この PoC は 1 つの VNet 内に Client、Azure Firewall、Application Gateway、AppVM を配置した構成です。

- VNet: vnet-sre-general-poc
- Address space: 10.10.0.0/20
- Client subnet: Subnet-client-001 (10.10.0.0/25)
- AzureFirewallSubnet: 10.10.1.0/26
- AppGW subnet: Subnet-appgw-001 (10.10.2.0/26)
- VM subnet: Subnet-vm-001 (10.10.3.0/25)

## Request Paths

この PoC で検証する主な経路は次のとおりです。

1. Client -> Azure Firewall -> private Application Gateway -> Azure Firewall -> AppVM IIS
2. AppVM -> Azure Firewall -> Internet

Application Gateway の private frontend IP は 10.10.2.10 です。
Application Gateway の backend pool は AppVM の private IP ではなく private DNS 上の FQDN を使用します。

## Route Tables

- udr-client-sre-general-poc
  - AppGW private frontend 10.10.2.10/32 を Azure Firewall に送ります。
- udr-appgw-sre-general-poc
  - 0.0.0.0/0 は Internet を維持します。
  - Client subnet と VM subnet 宛だけを Azure Firewall に送ります。
- udr-vm-sre-general-poc
  - AppGW subnet 宛を Azure Firewall に送ります。
  - 0.0.0.0/0 を Azure Firewall に送ります。

## Security Components

### Network Security Groups

- nsg-client-sre-general-poc
  - 管理用 RDP のみ許可します。
- nsg-appgw-sre-general-poc
  - Client subnet からの HTTP/HTTPS を許可します。
- nsg-vm-sre-general-poc
  - AppGW subnet からの probe と HTTP を許可します。

### Azure Firewall Policy

- Allow-Client-To-AppGW
  - Client subnet から AppGW private frontend への 80/TCP を許可します。
- Allow-AppGW-To-AppVM
  - AppGW subnet から VM subnet への 80/TCP を許可します。
- Allow-AppVM-To-Google
  - AppVM から google.com / www.google.com への HTTP/HTTPS を許可します。

## DNS Design

- Private DNS zone: sre-general-poc.internal
- AppGW FQDN: appgw.sre-general-poc.internal
- App backend FQDN: appvm.sre-general-poc.internal

AppGW から backend への到達は AppVM の FQDN を使います。
このため、backend DNS 解決失敗の疑似障害も再現できます。

## Application Gateway Settings

- SKU: Standard_v2
- Frontend: private only
- Backend: appvm.sre-general-poc.internal
- Health probe: HTTP, host は backend FQDN、path は /
- backend health の状態確認は Healthy / Unhealthy / Unknown を使います。

## Observability

### Log Analytics

- Workspace: law-sre-general-poc
- Azure Firewall と Application Gateway の診断ログを Log Analytics に送ります。

### Main Signals

- Application Gateway backend health
- AppGW の診断ログ
- Azure Firewall の AzureDiagnostics ログ
- Azure Monitor の metrics / alerts
- Private DNS の A レコード

### Log Notes

- Azure Firewall の legacy diagnostics では AzureDiagnostics テーブルを参照します。
- 詳細は主に msg_s フィールドに入ります。
- Resource-specific mode に切り替えた場合はテーブルが変わる可能性があります。

## Investigation Entry Points

### AppGW 側の障害で確認すること

- backend health が Healthy / Unhealthy / Unknown のどれか
- AppGW 診断ログに 502 系や probe 異常があるか
- Azure Firewall に Deny が出ていないか
- NSG と UDR が期待どおりか
- Private DNS の backend A レコードが存在するか

### 外向き通信障害で確認すること

- Azure Firewall の AzureDiagnostics に Allow / Deny があるか
- Rule Collection / Rule 名が何か
- AppVM からの通信そのものが発生しているか