Title: Azure SRE Agent PoC 構築ランブック（IIS / AppGW / Firewall 疑似障害付き）
Date: 2026-04-13
Slug: sre-agent-poc-runbook
Lang: ja-jp
Category: notebook
Tags: azure, sre-agent, application-gateway, azure-firewall, iis, network, poc
Status: draft
Summary: Hub-VNet に IIS AppVM、Application Gateway、Azure Firewall を構築し、Client -> Firewall -> AppGW -> Firewall -> IIS の通信、AppGW 系の health probe/DNS 障害、AppVM の外向き通信障害を切り分けるための手順をまとめたランブック。

本稿は [sre-agent-scenarios]({filename}sre-agent-scenarios.md) で定義したシナリオを実際に動かすためのランブックです。

この runbook では、切り分けの軸を次の 3 つに分けます。

- ClientVM から Azure Firewall を経由して private AppGW に HTTP 接続する経路
- AppGW から Azure Firewall を経由して IIS backend に接続する経路
- AppVM から Azure Firewall 経由で外向き通信する経路

設計上のポイントは次のとおりです。private AppGW サブネットでは enhanced network control を前提にし、AppGW subnet には `0.0.0.0/0 -> Internet` を残したうえで client subnet と backend subnet 向けだけを Azure Firewall に送ります。VM subnet には `AppGW subnet -> Azure Firewall` と `0.0.0.0/0 -> Azure Firewall` を設定し、Client subnet には AppGW private frontend 宛のルートを設定します。これにより、この PoC では `Client -> Firewall -> AppGW -> Firewall -> IIS` と `AppVM -> Firewall -> Internet` を同時に検証できます。AppGW の backend pool は AppVM の private IP ではなく private DNS 上の FQDN を使い、backend DNS 解決失敗も再現できるようにします。[^1][^2][^3][^5][^6][^7]

> **SNAT**: Azure Firewall は宛先が IANA private IP range (RFC 1918) 内の場合 SNAT を適用しないため、VNet 内 subnet 間通信では送信元 IP が保持されます。NSG の source address prefix 指定が意図どおり機能する前提です。[^7]

- 0章: 事前準備
- 1章: 変数定義
- 2章: 環境構築
- 3章: 正常動作確認
- 4章: 疑似障害シナリオ
- 5章: クリーンアップ

## 0. 事前準備

### 0.1 Azure CLI 確認

```powershell
# Azure CLI と azure-firewall 拡張を確認します。
az version --output table
az extension add --name azure-firewall
```

### 0.2 ログインとサブスクリプション設定

```powershell
# 対象サブスクリプションにログインして切り替えます。
az login
az login --use-device-code
az account list --output table
az account set --subscription "<subscription-id>"
az account show --output table
```

### 0.3 private-only AppGW の前提機能

この runbook は private frontend only の Application Gateway を前提にします。事前に `EnableApplicationGatewayNetworkIsolation` を登録し、状態が `Registered` になるまで待ってください。[^1]

```powershell
# private-only AppGW の機能を登録します。
az feature register --name EnableApplicationGatewayNetworkIsolation --namespace Microsoft.Network
az feature show `
  --name EnableApplicationGatewayNetworkIsolation `
  --namespace Microsoft.Network `
  --query properties.state --output tsv
az provider register --namespace Microsoft.Network
```

## 1. 変数定義

```powershell
# デプロイで使う共通変数を設定します。
$RG                   = "rg-sre-general-poc"
$LOCATION             = "japaneast"
$VNET                 = "vnet-sre-general-poc"
$VNET_PREFIX          = "10.10.0.0/20"
$SUBNET_CLIENT        = "Subnet-client-001"
$SUBNET_CLIENT_PREFIX = "10.10.0.0/25"
$SUBNET_FW            = "AzureFirewallSubnet"
$SUBNET_FW_PREFIX     = "10.10.1.0/26"
$SUBNET_APPGW         = "Subnet-appgw-001"
$SUBNET_APPGW_PREFIX  = "10.10.2.0/26"
$SUBNET_VM            = "Subnet-vm-001"
$SUBNET_VM_PREFIX     = "10.10.3.0/25"
$FIREWALL             = "azfw-sre-general-poc"
$FIREWALL_POLICY      = "azfw-policy-sre-general-poc"
$APPGW                = "appgw-sre-general-poc"
$APPGW_PRIVATE_IP     = "10.10.2.10"
$CLIENT_VM            = "clientvm-sgpoc"
$CLIENT_VM_PIP        = "pip-clientvm-sgpoc"
$APP_VM               = "appvm-sgpoc"
$APP_VM_PIP           = "pip-appvm-sgpoc"
# 任意のパスワードを設定してください
$ADMIN_PASSWORD       = "<your-strong-password>"
$UDR_CLIENT           = "udr-client-sre-general-poc"
$UDR_APPGW            = "udr-appgw-sre-general-poc"
$UDR_VM               = "udr-vm-sre-general-poc"
$NSG_CLIENT           = "nsg-client-sre-general-poc"
$NSG_APPGW            = "nsg-appgw-sre-general-poc"
$NSG_VM               = "nsg-vm-sre-general-poc"
$DNS_ZONE             = "sre-general-poc.internal"
$APPGW_RECORD         = "appgw"
$APP_BACKEND_RECORD   = "appvm"
$APPGW_FQDN           = "$APPGW_RECORD.$DNS_ZONE"
$APP_BACKEND_FQDN     = "$APP_BACKEND_RECORD.$DNS_ZONE"
$APPGW_PROBE_GOOD     = "probe-http-root"
$APPGW_PROBE_BAD      = "probe-http-bad-path"
$LOG_WORKSPACE        = "law-sre-general-poc"
$OUTBOUND_TEST_URL    = "https://www.google.com"
```

## 2. 環境構築

### 2.1 リソースグループ・Log Analytics

```powershell
# リソースグループと Log Analytics を作成します。
az group create `
  --name $RG `
  --location $LOCATION

az monitor log-analytics workspace create `
  --resource-group $RG `
  --workspace-name $LOG_WORKSPACE `
  --location $LOCATION
```

### 2.2 VNet とサブネット

```powershell
# VNet と各サブネットを作成します。
az network vnet create `
  --resource-group $RG `
  --name $VNET `
  --address-prefix $VNET_PREFIX `
  --location $LOCATION

az network vnet subnet create `
  --resource-group $RG --vnet-name $VNET `
  --name $SUBNET_CLIENT --address-prefix $SUBNET_CLIENT_PREFIX
az network vnet subnet create `
  --resource-group $RG --vnet-name $VNET `
  --name $SUBNET_FW --address-prefix $SUBNET_FW_PREFIX
az network vnet subnet create `
  --resource-group $RG --vnet-name $VNET `
  --name $SUBNET_APPGW --address-prefix $SUBNET_APPGW_PREFIX
az network vnet subnet create `
  --resource-group $RG --vnet-name $VNET `
  --name $SUBNET_VM --address-prefix $SUBNET_VM_PREFIX

az network vnet subnet update `
  --resource-group $RG --vnet-name $VNET `
  --name $SUBNET_APPGW `
  --delegations Microsoft.Network/applicationGateways
```

### 2.3 NSG 作成と割り当て

```powershell
# 各サブネットに割り当てる NSG を作成します。
az network nsg create `
  --resource-group $RG --name $NSG_CLIENT
az network nsg create `
  --resource-group $RG --name $NSG_APPGW
az network nsg create `
  --resource-group $RG --name $NSG_VM

$MY_IP = (Invoke-RestMethod -Uri 'https://api.ipify.org?format=text').Trim()
az network nsg rule create `
  --resource-group $RG --nsg-name $NSG_CLIENT `
  --name Allow-RDP-Inbound `
  --priority 100 --direction Inbound `
  --source-address-prefixes $MY_IP `
  --destination-port-ranges 3389 --protocol Tcp --access Allow

az network nsg rule create `
  --resource-group $RG --nsg-name $NSG_APPGW `
  --name Allow-HTTP-FromClient `
  --priority 100 --direction Inbound `
  --source-address-prefixes $SUBNET_CLIENT_PREFIX `
  --destination-port-ranges 80 443 --protocol Tcp --access Allow

az network nsg rule create `
  --resource-group $RG --nsg-name $NSG_VM `
  --name Allow-AppGW-Probe `
  --priority 100 --direction Inbound `
  --source-address-prefixes $SUBNET_APPGW_PREFIX `
  --destination-port-ranges 80 --protocol Tcp --access Allow
az network nsg rule create `
  --resource-group $RG --nsg-name $NSG_VM `
  --name Allow-HTTP-FromAppGW `
  --priority 110 --direction Inbound `
  --source-address-prefixes $SUBNET_APPGW_PREFIX `
  --destination-port-ranges 80 --protocol Tcp --access Allow

az network vnet subnet update `
  --resource-group $RG --vnet-name $VNET `
  --name $SUBNET_CLIENT --network-security-group $NSG_CLIENT
az network vnet subnet update `
  --resource-group $RG --vnet-name $VNET `
  --name $SUBNET_APPGW --network-security-group $NSG_APPGW
az network vnet subnet update `
  --resource-group $RG --vnet-name $VNET `
  --name $SUBNET_VM --network-security-group $NSG_VM
```

### 2.4 Azure Firewall デプロイ

```powershell
# Azure Firewall と Firewall Policy を作成します。
az network firewall policy create `
  --resource-group $RG `
  --name $FIREWALL_POLICY `
  --location $LOCATION `
  --sku Standard

az network public-ip create `
  --resource-group $RG `
  --name "pip-$FIREWALL" `
  --location $LOCATION `
  --sku Standard --allocation-method Static

az network firewall create `
  --resource-group $RG `
  --name $FIREWALL `
  --location $LOCATION `
  --firewall-policy $FIREWALL_POLICY

az network firewall ip-config create `
  --resource-group $RG `
  --firewall-name $FIREWALL `
  --name "FW-config" `
  --public-ip-address "pip-$FIREWALL" `
  --vnet-name $VNET

az network firewall update `
  --resource-group $RG `
  --name $FIREWALL

$FW_PRIVATE_IP = $(az network firewall ip-config list `
  --resource-group $RG `
  --firewall-name $FIREWALL `
  --query "[?name=='FW-config'].privateIpAddress" `
  --output tsv)
Write-Host "Firewall Private IP: $FW_PRIVATE_IP"
```

```powershell
# Azure Firewall の診断ログを Log Analytics に送ります。
$LAW_RESOURCE_ID = $(az monitor log-analytics workspace show `
  --resource-group $RG `
  --workspace-name $LOG_WORKSPACE `
  --query id `
  --output tsv)
$FIREWALL_RESOURCE_ID = $(az network firewall show `
  --resource-group $RG `
  --name $FIREWALL `
  --query id `
  --output tsv)

az monitor diagnostic-settings create `
  --name "send-firewall-logs-to-law" `
  --resource $FIREWALL_RESOURCE_ID `
  --workspace $LAW_RESOURCE_ID `
  --logs "[{categoryGroup:allLogs,enabled:true}]" `
  --metrics "[{category:AllMetrics,enabled:true}]"
```

### 2.5 Firewall ポリシーと UDR

```powershell
# Firewall rule collection group を作成します。
az network firewall policy rule-collection-group create `
  --resource-group $RG `
  --policy-name $FIREWALL_POLICY `
  --name "DefaultNetworkRuleCollectionGroup" `
  --priority 200

az network firewall policy rule-collection-group create `
  --resource-group $RG `
  --policy-name $FIREWALL_POLICY `
  --name "DefaultApplicationRuleCollectionGroup" `
  --priority 300
```

```powershell
# ClientVM から private AppGW への HTTP を許可します。
az network firewall policy rule-collection-group collection add-filter-collection `
  --resource-group $RG `
  --policy-name $FIREWALL_POLICY `
  --rule-collection-group-name "DefaultNetworkRuleCollectionGroup" `
  --name "Allow-Client-To-AppGW" `
  --collection-priority 100 `
  --action Allow `
  --rule-name "Allow-HTTP" `
  --rule-type NetworkRule `
  --source-addresses $SUBNET_CLIENT_PREFIX `
  --destination-addresses $APPGW_PRIVATE_IP `
  --destination-ports 80 `
  --ip-protocols TCP
```

```powershell
# AppGW から AppVM backend への HTTP を許可します。
az network firewall policy rule-collection-group collection add-filter-collection `
  --resource-group $RG `
  --policy-name $FIREWALL_POLICY `
  --rule-collection-group-name "DefaultNetworkRuleCollectionGroup" `
  --name "Allow-AppGW-To-AppVM" `
  --collection-priority 110 `
  --action Allow `
  --rule-name "Allow-Backend-HTTP" `
  --rule-type NetworkRule `
  --source-addresses $SUBNET_APPGW_PREFIX `
  --destination-addresses $SUBNET_VM_PREFIX `
  --destination-ports 80 `
  --ip-protocols TCP
```

```powershell
# AppVM から Google への HTTP/HTTPS を許可します。
az network firewall policy rule-collection-group collection add-filter-collection `
  --resource-group $RG `
  --policy-name $FIREWALL_POLICY `
  --rule-collection-group-name "DefaultApplicationRuleCollectionGroup" `
  --name "Allow-AppVM-To-Google" `
  --collection-priority 100 `
  --action Allow `
  --rule-name "Allow-Google-Web" `
  --rule-type ApplicationRule `
  --source-addresses $SUBNET_VM_PREFIX `
  --target-fqdns "google.com" "www.google.com" `
  --protocols Http=80 Https=443
```

```powershell
# Client subnet には AppGW private frontend 宛だけ Firewall 経由の UDR を設定します。
az network route-table create `
  --resource-group $RG `
  --name $UDR_CLIENT `
  --location $LOCATION `
  --disable-bgp-route-propagation true
az network route-table route create `
  --resource-group $RG `
  --route-table-name $UDR_CLIENT `
  --name "AppGW-Via-Firewall" `
  --address-prefix "$APPGW_PRIVATE_IP/32" `
  --next-hop-type VirtualAppliance `
  --next-hop-ip-address $FW_PRIVATE_IP
az network vnet subnet update `
  --resource-group $RG --vnet-name $VNET `
  --name $SUBNET_CLIENT `
  --route-table $UDR_CLIENT
```

```powershell
# AppGW subnet には Internet 直通を残しつつ、Client subnet と backend subnet 向けを Firewall に送ります。
az network route-table create `
  --resource-group $RG `
  --name $UDR_APPGW `
  --location $LOCATION `
  --disable-bgp-route-propagation true
az network route-table route create `
  --resource-group $RG `
  --route-table-name $UDR_APPGW `
  --name "Default-Internet" `
  --address-prefix "0.0.0.0/0" `
  --next-hop-type Internet
az network route-table route create `
  --resource-group $RG `
  --route-table-name $UDR_APPGW `
  --name "ClientSubnet-Via-Firewall" `
  --address-prefix $SUBNET_CLIENT_PREFIX `
  --next-hop-type VirtualAppliance `
  --next-hop-ip-address $FW_PRIVATE_IP
az network route-table route create `
  --resource-group $RG `
  --route-table-name $UDR_APPGW `
  --name "VmSubnet-Via-Firewall" `
  --address-prefix $SUBNET_VM_PREFIX `
  --next-hop-type VirtualAppliance `
  --next-hop-ip-address $FW_PRIVATE_IP
az network vnet subnet update `
  --resource-group $RG --vnet-name $VNET `
  --name $SUBNET_APPGW `
  --route-table $UDR_APPGW
```

```powershell
# VM subnet には AppGW subnet 宛と外向き通信の両方を Firewall 経由で設定します。
az network route-table create `
  --resource-group $RG `
  --name $UDR_VM `
  --location $LOCATION `
  --disable-bgp-route-propagation true
az network route-table route create `
  --resource-group $RG `
  --route-table-name $UDR_VM `
  --name "AppGWSubnet-Via-Firewall" `
  --address-prefix $SUBNET_APPGW_PREFIX `
  --next-hop-type VirtualAppliance `
  --next-hop-ip-address $FW_PRIVATE_IP
az network route-table route create `
  --resource-group $RG `
  --route-table-name $UDR_VM `
  --name "Default-To-Firewall" `
  --address-prefix "0.0.0.0/0" `
  --next-hop-type VirtualAppliance `
  --next-hop-ip-address $FW_PRIVATE_IP
az network vnet subnet update `
  --resource-group $RG --vnet-name $VNET `
  --name $SUBNET_VM `
  --route-table $UDR_VM
```

### 2.6 AppVM / Private DNS / AppGW / ClientVM

```powershell
# AppVM を作成して IIS を有効化します。
az network public-ip create `
  --resource-group $RG `
  --name $APP_VM_PIP `
  --location $LOCATION `
  --sku Standard --allocation-method Static

az vm create `
  --resource-group $RG `
  --name $APP_VM `
  --location $LOCATION `
  --image MicrosoftWindowsServer:WindowsServer:2022-datacenter-azure-edition:latest `
  --size Standard_B2ms `
  --admin-username azureuser `
  --admin-password $ADMIN_PASSWORD `
  --vnet-name $VNET `
  --subnet $SUBNET_VM `
  --public-ip-address $APP_VM_PIP `
  --nsg """"

# IIS setup via run-command
az vm run-command invoke `
  --resource-group $RG `
  --name $APP_VM `
  --command-id RunPowerShellScript `
  --scripts "Install-WindowsFeature Web-Server -IncludeManagementTools; Set-Content -Path C:\inetpub\wwwroot\index.html -Value '<html><body><h1>AppVM IIS - OK</h1></body></html>'"

$APP_VM_IP = $(az vm list-ip-addresses `
  --resource-group $RG --name $APP_VM `
  --query "[].virtualMachine.network.privateIpAddresses[0]" `
  --output tsv)
Write-Host "AppVM Private IP: $APP_VM_IP"
```

```powershell
# Private DNS zone を作成し、AppGW 用と backend 用の名前解決基盤を用意します。
az network private-dns zone create `
  --resource-group $RG `
  --name $DNS_ZONE
az network private-dns link vnet create `
  --resource-group $RG `
  --zone-name $DNS_ZONE `
  --name "link-hub-vnet" `
  --virtual-network $VNET `
  --registration-enabled false
az network private-dns record-set a add-record `
  --resource-group $RG `
  --zone-name $DNS_ZONE `
  --record-set-name $APP_BACKEND_RECORD `
  --ipv4-address $APP_VM_IP
```

```powershell
# AppGW を作成し、backend pool には AppVM の FQDN を設定します。
az network application-gateway create `
  --resource-group $RG `
  --name $APPGW `
  --location $LOCATION `
  --sku Standard_v2 `
  --capacity 1 `
  --vnet-name $VNET `
  --subnet $SUBNET_APPGW `
  --private-ip-address $APPGW_PRIVATE_IP `
  --frontend-port 80 `
  --http-settings-port 80 `
  --http-settings-protocol Http `
  --routing-rule-type Basic `
  --servers $APP_BACKEND_FQDN `
  --priority 100

$APPGW_HTTP_SETTINGS = $(az network application-gateway http-settings list `
  --resource-group $RG `
  --gateway-name $APPGW `
  --query "[0].name" `
  --output tsv)

az network application-gateway probe create `
  --resource-group $RG `
  --gateway-name $APPGW `
  --name $APPGW_PROBE_GOOD `
  --protocol Http `
  --host $APP_BACKEND_FQDN `
  --path "/" `
  --interval 30 `
  --timeout 30 `
  --threshold 3

az network application-gateway http-settings update `
  --resource-group $RG `
  --gateway-name $APPGW `
  --name $APPGW_HTTP_SETTINGS `
  --host-name-from-backend-pool true `
  --probe $APPGW_PROBE_GOOD `
  --enable-probe true
```

```powershell
# AppGW の診断ログを Log Analytics に送ります。
$APPGW_RESOURCE_ID = $(az network application-gateway show `
  --resource-group $RG `
  --name $APPGW `
  --query id `
  --output tsv)

az monitor diagnostic-settings create `
  --name "send-appgw-logs-to-law" `
  --resource $APPGW_RESOURCE_ID `
  --workspace $LAW_RESOURCE_ID `
  --logs "[{categoryGroup:allLogs,enabled:true}]" `
  --metrics "[{category:AllMetrics,enabled:true}]"
```

```powershell
# ClientVM を作成し、AppGW の private FQDN を登録します。
az network public-ip create `
  --resource-group $RG `
  --name $CLIENT_VM_PIP `
  --location $LOCATION `
  --sku Standard --allocation-method Static
az vm create `
  --resource-group $RG `
  --name $CLIENT_VM `
  --location $LOCATION `
  --image MicrosoftWindowsServer:WindowsServer:2022-datacenter-azure-edition:latest `
  --size Standard_B2ms `
  --admin-username azureuser `
  --admin-password $ADMIN_PASSWORD `
  --vnet-name $VNET `
  --subnet $SUBNET_CLIENT `
  --public-ip-address $CLIENT_VM_PIP `
  --nsg """"

az network private-dns record-set a add-record `
  --resource-group $RG `
  --zone-name $DNS_ZONE `
  --record-set-name $APPGW_RECORD `
  --ipv4-address $APPGW_PRIVATE_IP
```

## 3. 正常動作確認

### 3.1 AppVM の IIS 確認

```powershell
# AppVM 上の IIS ローカル応答を確認します。
az vm run-command invoke `
  --resource-group $RG `
  --name $APP_VM `
  --command-id RunPowerShellScript `
  --scripts "Invoke-WebRequest -Uri http://localhost -UseBasicParsing | Select-Object StatusCode, Content"
```

期待値: `StatusCode: 200` と `AppVM IIS - OK`。

### 3.2 AppGW バックエンドヘルス確認

```powershell
# AppGW の backend health を確認します。
az network application-gateway show-backend-health `
  --resource-group $RG `
  --name $APPGW `
  --query "backendAddressPools[].backendHttpSettingsCollection[].servers[].{address:address,health:health}" `
  --output table
```

期待値: backend health が `Healthy`。

### 3.3 ClientVM からの DNS と HTTP 確認

```powershell
# ClientVM から AppGW の private FQDN 解決と HTTP 応答を確認します。
az vm run-command invoke `
  --resource-group $RG `
  --name $CLIENT_VM `
  --command-id RunPowerShellScript `
  --scripts "Resolve-DnsName $APPGW_FQDN; Invoke-WebRequest -Uri http://$APPGW_FQDN -UseBasicParsing | Select-Object StatusCode, Content"
```

期待値: `Resolve-DnsName` が `10.10.2.10` を返し、HTTP 応答が `200`。

### 3.4 AppVM からの外向き通信確認

```powershell
# AppVM から Google への HTTPS 到達性を確認します。
az vm run-command invoke `
  --resource-group $RG `
  --name $APP_VM `
  --command-id RunPowerShellScript `
  --scripts "Invoke-WebRequest -Uri $OUTBOUND_TEST_URL -UseBasicParsing | Select-Object StatusCode"
```

期待値: `StatusCode: 200`。

### 3.5 Firewall ログ確認（Azure Portal）

CLI での確認は読みにくいため、Azure Portal の **Logs** または **Workbook** で確認します。Azure Firewall の監視は Azure Monitor Logs / Workbooks で行うのが基本です。[^8][^9]

1. Azure Portal で `$FIREWALL` を開きます。
2. **Monitoring** 配下の **Logs** を開きます。
3. 時間範囲を直近 30 分に設定します。
4. 次の KQL を実行して Allow/Deny を確認します。

```kusto
AzureDiagnostics
| where TimeGenerated > ago(30m)
| where Category in ('AzureFirewallNetworkRule', 'AzureFirewallApplicationRule')
| project TimeGenerated, Category, msg_s
| order by TimeGenerated desc
```

期待値: `msg_s` に次の 3 系統の Allow を確認できます。

- Client subnet から AppGW private frontend への 80/TCP
- AppGW subnet から AppVM backend への 80/TCP
- AppVM から `www.google.com` への HTTP/HTTPS

> **注意**: Legacy Azure Diagnostics ログでは詳細は `msg_s` に入ります。Resource-Specific モードへ切り替えた場合は `AZFWNetworkRule` / `AZFWApplicationRule` テーブルで確認してください。Portal の **Workbook** も見やすい選択肢です。[^8][^9]

## 4. 疑似障害シナリオ

### シナリオ A: AppGW health probe 障害（IIS 停止）

> **注意**: health probe の interval=30s, threshold=3 のため、障害投入後 Unhealthy に遷移するまで 1-2 分かかります。少し待ってから `show-backend-health` を実行してください。

```powershell
# AppVM 上の IIS を停止して health probe を失敗させます。
az vm run-command invoke `
  --resource-group $RG `
  --name $APP_VM `
  --command-id RunPowerShellScript `
  --scripts "Stop-Service W3SVC -Force; Get-Service W3SVC | Select-Object Name, Status"

az network application-gateway show-backend-health `
  --resource-group $RG `
  --name $APPGW `
  --query "backendAddressPools[].backendHttpSettingsCollection[].servers[].{address:address,health:health}" `
  --output table
```

復旧:

```powershell
# IIS を再起動して health probe を復旧します。
az vm run-command invoke `
  --resource-group $RG `
  --name $APP_VM `
  --command-id RunPowerShellScript `
  --scripts "Start-Service W3SVC; Get-Service W3SVC | Select-Object Name, Status"
```

### シナリオ B: AppGW -> IIS 経路障害（Azure Firewall で backend HTTP を拒否）

AppGW と backend の間も Azure Firewall を経由するため、Firewall policy の誤りで backend health が崩れることを再現できます。[^5][^6]

> **注意**: health probe の interval=30s, threshold=3 のため、障害投入後 Unhealthy に遷移するまで 1-2 分かかります。少し待ってから `show-backend-health` を実行してください。

```powershell
# AppGW から AppVM への backend HTTP を Azure Firewall で拒否します。
az network firewall policy rule-collection-group collection add-filter-collection `
  --resource-group $RG `
  --policy-name $FIREWALL_POLICY `
  --rule-collection-group-name "DefaultNetworkRuleCollectionGroup" `
  --name "Deny-AppGW-To-AppVM" `
  --collection-priority 90 `
  --action Deny `
  --rule-name "Deny-Backend-HTTP" `
  --rule-type NetworkRule `
  --source-addresses $SUBNET_APPGW_PREFIX `
  --destination-addresses $SUBNET_VM_PREFIX `
  --destination-ports 80 `
  --ip-protocols TCP

az network application-gateway show-backend-health `
  --resource-group $RG `
  --name $APPGW `
  --query "backendAddressPools[].backendHttpSettingsCollection[].servers[].{address:address,health:health}" `
  --output table
```

復旧:

```powershell
# Deny コレクションを削除して backend 通信を戻します。
az network firewall policy rule-collection-group collection remove `
  --resource-group $RG `
  --policy-name $FIREWALL_POLICY `
  --rule-collection-group-name "DefaultNetworkRuleCollectionGroup" `
  --name "Deny-AppGW-To-AppVM"
```

### シナリオ C: AppGW health probe 障害（80/TCP ブロック）

> **注意**: health probe の interval=30s, threshold=3 のため、障害投入後 Unhealthy に遷移するまで 1-2 分かかります。少し待ってから `show-backend-health` を実行してください。

```powershell
# NSG で AppGW から AppVM への 80/TCP を拒否します。
az network nsg rule create `
  --resource-group $RG `
  --nsg-name $NSG_VM `
  --name "BLOCK-AppGW-HTTP" `
  --priority 50 `
  --direction Inbound `
  --source-address-prefixes $SUBNET_APPGW_PREFIX `
  --destination-port-ranges 80 `
  --protocol Tcp `
  --access Deny

az network application-gateway show-backend-health `
  --resource-group $RG `
  --name $APPGW `
  --query "backendAddressPools[].backendHttpSettingsCollection[].servers[].{address:address,health:health}" `
  --output table
```

復旧:

```powershell
# ブロック用 NSG ルールを削除します。
az network nsg rule delete `
  --resource-group $RG `
  --nsg-name $NSG_VM `
  --name "BLOCK-AppGW-HTTP"
```

### シナリオ D: AppGW health probe 障害（HTTP setting/probe 不整合）

> **注意**: health probe の interval=30s, threshold=3 のため、障害投入後 Unhealthy に遷移するまで 1-2 分かかります。少し待ってから `show-backend-health` を実行してください。

`/` は正常応答する一方で、存在しない `/does-not-exist` を probe に設定して不整合を作ります。

```powershell
# 不正な probe を作成して HTTP settings に関連付けます。
az network application-gateway probe create `
  --resource-group $RG `
  --gateway-name $APPGW `
  --name $APPGW_PROBE_BAD `
  --protocol Http `
  --host $APP_BACKEND_FQDN `
  --path "/does-not-exist" `
  --interval 30 `
  --timeout 30 `
  --threshold 3

$APPGW_HTTP_SETTINGS = $(az network application-gateway http-settings list `
  --resource-group $RG `
  --gateway-name $APPGW `
  --query "[0].name" `
  --output tsv)

az network application-gateway http-settings update `
  --resource-group $RG `
  --gateway-name $APPGW `
  --name $APPGW_HTTP_SETTINGS `
  --probe $APPGW_PROBE_BAD `
  --enable-probe true

az network application-gateway show-backend-health `
  --resource-group $RG `
  --name $APPGW `
  --query "backendAddressPools[].backendHttpSettingsCollection[].servers[].{address:address,health:health}" `
  --output table
```

復旧:

```powershell
# 正常な probe を再び HTTP settings に関連付けます。
az network application-gateway http-settings update `
  --resource-group $RG `
  --gateway-name $APPGW `
  --name $APPGW_HTTP_SETTINGS `
  --probe $APPGW_PROBE_GOOD `
  --enable-probe true
```

### シナリオ E: DNS 障害（Client の名前解決失敗）

ClientVM から参照する AppGW の A レコードを削除し、名前解決エラーを再現します。

```powershell
# ClientVM が引く AppGW の A レコードを削除します。
az network private-dns record-set a remove-record `
  --resource-group $RG `
  --zone-name $DNS_ZONE `
  --record-set-name $APPGW_RECORD `
  --ipv4-address $APPGW_PRIVATE_IP

az vm run-command invoke `
  --resource-group $RG `
  --name $CLIENT_VM `
  --command-id RunPowerShellScript `
  --scripts "Resolve-DnsName $APPGW_FQDN"
```

復旧:

```powershell
# AppGW の A レコードを戻します。
az network private-dns record-set a add-record `
  --resource-group $RG `
  --zone-name $DNS_ZONE `
  --record-set-name $APPGW_RECORD `
  --ipv4-address $APPGW_PRIVATE_IP
```

### シナリオ F: DNS 障害（AppGW backend FQDN の解決失敗）

AppGW backend は FQDN ベースです。backend A レコードを削除し、あわせて AppGW に PUT をかけて DNS キャッシュをクリアすると、backend health が `Unknown` または DNS 解決エラーになります。Application Gateway は last-known-good IP をキャッシュするため、この手順を入れています。[^4]

```powershell
# backend 用 A レコードが存在する場合だけ削除し、AppGW を更新して DNS キャッシュをクリアします。
$BACKEND_RECORD_EXISTS = az network private-dns record-set a list `
  --resource-group $RG `
  --zone-name $DNS_ZONE `
  --query "[?name=='$APP_BACKEND_RECORD'] | length(@)" `
  --output tsv

if ($BACKEND_RECORD_EXISTS -eq "1") {
  az network private-dns record-set a remove-record `
    --resource-group $RG `
    --zone-name $DNS_ZONE `
    --record-set-name $APP_BACKEND_RECORD `
    --ipv4-address $APP_VM_IP
} else {
  Write-Host "backend A record '$APP_BACKEND_RECORD' is already absent."
}

az network application-gateway update `
  --resource-group $RG `
  --name $APPGW `
  --set tags.backendDnsState=broken

az network application-gateway show-backend-health `
  --resource-group $RG `
  --name $APPGW `
  --query "backendAddressPools[].backendHttpSettingsCollection[].servers[].{address:address,health:health}" `
  --output table
```

復旧:

```powershell
# backend 用 A レコードを戻し、再度 AppGW を更新します。
az network private-dns record-set a add-record `
  --resource-group $RG `
  --zone-name $DNS_ZONE `
  --record-set-name $APP_BACKEND_RECORD `
  --ipv4-address $APP_VM_IP

az network application-gateway update `
  --resource-group $RG `
  --name $APPGW `
  --set tags.backendDnsState=healthy
```

### シナリオ G: 外向き通信障害（AppVM から Google に出られない）

AppVM サブネットは `0.0.0.0/0 -> Azure Firewall` なので、Google への outbound は Firewall policy で制御できます。

```powershell
# Google 向けの明示的 Deny コレクションを追加します。
az network firewall policy rule-collection-group collection add-filter-collection `
  --resource-group $RG `
  --policy-name $FIREWALL_POLICY `
  --rule-collection-group-name "DefaultApplicationRuleCollectionGroup" `
  --name "Deny-AppVM-To-Google" `
  --collection-priority 90 `
  --action Deny `
  --rule-name "Deny-Google-Web" `
  --rule-type ApplicationRule `
  --source-addresses $SUBNET_VM_PREFIX `
  --target-fqdns "google.com" "www.google.com" `
  --protocols Http=80 Https=443

az vm run-command invoke `
  --resource-group $RG `
  --name $APP_VM `
  --command-id RunPowerShellScript `
  --scripts "Invoke-WebRequest -Uri $OUTBOUND_TEST_URL -UseBasicParsing"
```

復旧:

```powershell
# Deny コレクションを削除して outbound を戻します。
az network firewall policy rule-collection-group collection remove `
  --resource-group $RG `
  --policy-name $FIREWALL_POLICY `
  --rule-collection-group-name "DefaultApplicationRuleCollectionGroup" `
  --name "Deny-AppVM-To-Google"
```

### シナリオ H: 日次ヘルスチェック

> **注意**: 以下の JSON にはリソース名がハードコードされています。変数ブロックの値を変更した場合はあわせて修正してください。

```json
{
  "name": "Daily PoC Health Check",
  "schedule": "0 23 * * *",
  "runMode": "Autonomous",
  "instructions": "Perform a daily health check for the PoC environment (resource group: rg-sre-general-poc).\n\n1. AppVM IIS status: Run PowerShell 'Get-Service W3SVC | Select Name,Status' on appvm-sgpoc.\n2. ClientVM DNS + HTTP check: Run PowerShell 'Resolve-DnsName appgw.sre-general-poc.internal; Invoke-WebRequest http://appgw.sre-general-poc.internal -UseBasicParsing | Select StatusCode' on clientvm-sgpoc.\n3. AppGW backend health: retrieve health state for all backends of appgw-sre-general-poc.\n4. Azure Firewall network logs: confirm Allow records for both Client subnet -> AppGW private frontend and AppGW subnet -> AppVM backend on port 80.\n5. AppVM outbound HTTPS check: Run PowerShell 'Invoke-WebRequest https://www.google.com -UseBasicParsing | Select StatusCode' on appvm-sgpoc.\n6. Azure Firewall application logs: summarize Allow/Deny counts for outbound web access during the past 24 hours.\n7. Private DNS: confirm that appgw.sre-general-poc.internal resolves to the AppGW private frontend IP and appvm.sre-general-poc.internal resolves to the AppVM private IP.\n8. Compose a Markdown summary table with columns: Component | Status | Notes.\n9. Post the summary to the Teams channel via the configured connector.",
  "connectors": ["teams-connector"]
}
```

### シナリオ I: AppGW health probe Unhealthy を Azure Monitor アラートで検知し、SRE Agent のインシデント調査を起動する

Application Gateway は `UnhealthyHostCount` メトリックで backend の probe 異常を監視できます。この PoC では backend host が 1 台なので、`avg UnhealthyHostCount > 0` をしきい値にすると、health probe が Unhealthy になった時点でアラートを発火できます。Azure SRE Agent は Azure Monitor を既定の incident platform として扱えるため、このアラートをインシデントトリガーにした自動調査を構成できます。[^10][^11][^12][^13][^14]

> **注意**: Azure Monitor 側のアラートルール作成は CLI でできますが、SRE Agent の Incident Response Plan は現時点では Azure portal の UI で作成します。Azure Monitor からの自動取り込みには agent の managed identity に監視対象サブスクリプションまたは対象 RG への Reader 権限が必要で、アラートの acknowledge / close まで扱う場合は Monitoring Contributor も必要です。[^13][^14][^15]

```powershell
# AppGW unhealthy alert 用の名前を設定します。
$APPGW_UNHEALTHY_ALERT = "alert-appgw-unhealthy-hosts"
$ALERT_ACTION_GROUP    = "ag-sre-general-poc"
$ALERT_EMAIL           = "takumiseo@microsoft.com"
$ACTION_GROUP_ID       = ""
```

```powershell
# 任意で人手通知用の Action Group を作成します。
$ACTION_GROUP_ID = $(az monitor action-group create `
  --name $ALERT_ACTION_GROUP `
  --resource-group $RG `
  --short-name "SREPOC" `
  --action email sreoncall $ALERT_EMAIL `
  --query id `
  --output tsv)
```

> **補足**: Azure SRE Agent が Azure Monitor アラートを incident として取り込むだけなら、Action Group は必須ではありません。Action Group はメールや Webhook など、人手通知を追加したい場合に使います。[^13]

```powershell
# AppGW の resource ID を取得し、UnhealthyHostCount の alert を作成します。
$APPGW_RESOURCE_ID = $(az network application-gateway show `
  --resource-group $RG `
  --name $APPGW `
  --query id `
  --output tsv)

if ([string]::IsNullOrWhiteSpace($ACTION_GROUP_ID)) {
  az monitor metrics alert create `
    --name $APPGW_UNHEALTHY_ALERT `
    --resource-group $RG `
    --scopes $APPGW_RESOURCE_ID `
    --condition "avg UnhealthyHostCount > 0" `
    --description "AppGW backend health probe unhealthy detected in PoC" `
    --severity 1 `
    --window-size 5m `
    --evaluation-frequency 1m
} else {
  az monitor metrics alert create `
    --name $APPGW_UNHEALTHY_ALERT `
    --resource-group $RG `
    --scopes $APPGW_RESOURCE_ID `
    --condition "avg UnhealthyHostCount > 0" `
    --description "AppGW backend health probe unhealthy detected in PoC" `
    --severity 1 `
    --window-size 5m `
    --evaluation-frequency 1m `
    --action $ACTION_GROUP_ID
}
```

```powershell
# 作成した alert rule を確認します。
az monitor metrics alert show `
  --name $APPGW_UNHEALTHY_ALERT `
  --resource-group $RG `
  --output table
```
1. Azure SRE Agent 側で Azure Monitor が incident platform になっていることを確認します。Azure Monitor は既定の incident platform で、追加設定なしで接続されます。[^14]
2. Azure SRE Agent の Agent Canvas または Incident response plan 画面で、新しい Incident Response Plan を作成します。[^15]
3. フィルター例:
   - Severity: `Sev1`
   - Title contains: `alert-appgw-unhealthy-hosts`
4. Customize the incident response plan (optional)を有効化します。
支持の追加で以下の指示を入力してください。(カスタマイズすることも可能です)
```text
Azure Monitor で Application Gateway の UnhealthyHostCount アラートが発火しました。
対象は rg-sre-general-poc / appgw-sre-general-poc / appvm-sgpoc です。
読み取り専用で、alert details、Application Gateway backend health、AppGW 診断ログ、Azure Firewall の AzureDiagnostics、Private DNS、NSG、UDR、probe、HTTP settings を確認してください。
日本語で次の形式で返してください。
- alert の概要
- backend health の状態
- 影響を受けている backend
- 原因候補を最大 3 件
- 各候補の根拠
- runbook の対応手順
証拠が不足する場合は推測せず、要追加確認として不足項目を列挙してください。
```
5. Generate + review をクリックします
今回の検証では自動生成されたツールをそのまま利用してください。
Teams の連携など試したい場合は、PostTeamsMessage ツールを選択かつ、コネクターで Teams と接続することで連携が可能です。その場合は Review custom incident response plan へその意図を追記することをお勧めします。
ただし実環境では、Teams 投稿用のサブエージェントを作成し、インシデント対応計画と結びつけるタスク分散をお勧めします。
5. Agent autonomy level はまず `Review` で開始し、期待どおりに調査できることを確認してから必要に応じて引き上げます。


```powershell
# 動作確認として IIS を停止し、AppGW backend health が Unhealthy になる状態を作ります。
az vm run-command invoke `
  --resource-group $RG `
  --name $APP_VM `
  --command-id RunPowerShellScript `
  --scripts "Stop-Service W3SVC -Force; Get-Service W3SVC | Select-Object Name, Status"

az network application-gateway show-backend-health `
  --resource-group $RG `
  --name $APPGW `
  --query "backendAddressPools[].backendHttpSettingsCollection[].servers[].{address:address,health:health}" `
  --output table
```

アラートが発砲されてから数分後には SRE Agent 側で原因の調査が始まります。
こちらは SRE Agent Portal のタブにある「インシデント」で確認が可能です。

復旧:

```powershell
# IIS を起動し、alert rule は削除せずに監視を継続します。
az vm run-command invoke `
  --resource-group $RG `
  --name $APP_VM `
  --command-id RunPowerShellScript `
  --scripts "Start-Service W3SVC; Get-Service W3SVC | Select-Object Name, Status"
```
## 5. リソースクリーンアップ

```powershell
# リソースグループを削除します。
az group delete `
  --name $RG `
  --yes --no-wait
```

[^1]: "Private Application Gateway deployment - Onboard to the feature", https://learn.microsoft.com/azure/application-gateway/application-gateway-private-deployment#onboard-to-the-feature
[^2]: "Private Application Gateway deployment - Route Table Control", https://learn.microsoft.com/azure/application-gateway/application-gateway-private-deployment#route-table-control
[^3]: "Deploy and configure Azure Firewall using the Azure portal - Create a default route", https://learn.microsoft.com/azure/firewall/tutorial-firewall-deploy-portal#create-a-default-route
[^4]: "Troubleshoot backend health issues in Application Gateway - Backend health status: Unknown", https://learn.microsoft.com/troubleshoot/azure/application-gateway/application-gateway-backend-health-troubleshooting#backend-health-status-unknown
[^5]: "Scenario: Secure traffic between Application Gateway and backend pools - Scenario 1 - Same VNet", https://learn.microsoft.com/azure/virtual-wan/scenario-secured-hub-app-gateway#scenario-1---same-vnet
[^6]: "Azure Firewall and Application Gateway for virtual networks - Application Gateway in front of Azure Firewall design", https://learn.microsoft.com/azure/architecture/example-scenario/gateway/firewall-application-gateway#application-gateway-in-front-of-azure-firewall-design
[^7]: "Azure Firewall SNAT private IP address ranges", https://learn.microsoft.com/azure/firewall/snat-private-range
[^8]: "Monitor Azure Firewall", https://learn.microsoft.com/azure/firewall/monitor-firewall
[^9]: "Use Azure Firewall workbooks", https://learn.microsoft.com/azure/firewall/firewall-workbook
[^10]: "Monitor Azure Application Gateway", https://learn.microsoft.com/azure/application-gateway/monitor-application-gateway#alerts
[^11]: "Supported metrics for Microsoft.Network/applicationgateways", https://learn.microsoft.com/azure/azure-monitor/reference/supported-metrics/microsoft-network-applicationgateways-metrics
[^12]: "Create a new alert rule using the CLI, PowerShell, or an ARM template", https://learn.microsoft.com/azure/azure-monitor/alerts/alerts-create-rule-cli-powershell-arm
[^13]: "Azure Monitor alerts", https://learn.microsoft.com/azure/sre-agent/azure-monitor-alerts
[^14]: "Step 4: Set up incident response in Azure SRE Agent", https://learn.microsoft.com/azure/sre-agent/tutorial-incident-response
[^15]: "Tutorial: Create an incident response plan for Azure SRE Agent", https://learn.microsoft.com/azure/sre-agent/response-plan
