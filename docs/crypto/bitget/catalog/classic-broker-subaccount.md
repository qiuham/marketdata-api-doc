---
exchange: bitget
source_url: https://www.bitget.com/docs/catalog/classic-broker-subaccount
api_type: REST
updated_at: 2026-11-28 19:00:16.579670
---

# Classic Broker Subaccount API

Classic account — broker subaccount, deposit/withdrawal and transfer endpoints.

版本: 1.0.0

## 服务地址

- `https://api.bitget.com`

## 接口列表

- `GET /api/v2/broker/account/info` — Get Broker Info
- `POST /api/v2/broker/account/modify-subaccount-email` — Modify Subaccount Email
- `POST /api/v2/broker/account/create-subaccount` — Create Subaccount
- `GET /api/v2/broker/account/subaccount-list` — Get Subaccount List
- `POST /api/v2/broker/account/modify-subaccount` — Modify Subaccount
- `GET /api/v2/broker/account/subaccount-email` — Get Subaccount Email
- `GET /api/v2/broker/account/subaccount-spot-assets` — Get Subaccount Spot Assets
- `GET /api/v2/broker/account/subaccount-future-assets` — Get Subaccount Future Assets
- `POST /api/v2/broker/account/subaccount-address` — Create Subaccount Deposit Address
- `POST /api/v2/broker/account/subaccount-withdrawal` — Subaccount Withdrawal
- `POST /api/v2/broker/account/set-subaccount-autotransfer` — Sub Deposit Auto Transfer
- `GET /api/v2/broker/subaccount-deposit` — Sub Deposit Records
- `GET /api/v2/broker/subaccount-withdrawal` — Sub Withdrawal Records
- `GET /api/v2/broker/all-sub-deposit-withdrawal` — Get Sub-accounts Deposit and Withdrawal Records
- `GET /api/v2/broker/subaccounts` — Get Broker Subaccounts
- `GET /api/v2/broker/commissions` — Get Broker Subaccounts Commissions
- `GET /api/v2/broker/trade-volume` — Get Broker Trade Volume

## Get Broker Info

`GET /api/v2/broker/account/info`

Frequency limit：10 times/1s (User ID)

Get account information of ND Brokers

Operation ID: `classicBrokerSubaccountGetBrokerAccountInfo`

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.subAccountSize | string |  | Number of sub-accounts created by the broker |
| data.maxSubAccountSize | string |  | Maximum number of sub-accounts that could be created |
| data.uTime | string |  | Update time<br><br>Unix millisecond timestamp, e.g. 1690196141868 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695783465795,
  "data": {
    "subAccountSize": "9",
    "maxSubAccountSize": "10",
    "uTime": "1691635508000"
  }
}
```

## Modify Subaccount Email

`POST /api/v2/broker/account/modify-subaccount-email`

Frequency limit：10 times/1s (User ID)

Modify subaccount email

Operation ID: `classicBrokerSubaccountModifySubaccountEmail`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| subUid | string | 是 | Subaccount user id |
| subaccountEmail | string | 是 | Subaccount email |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | string |  |  |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695784928863,
  "data": "success"
}
```

## Create Subaccount

`POST /api/v2/broker/account/create-subaccount`

Frequency limit: 1 time/1s (User ID)

Create subaccounts

Operation ID: `classicBrokerSubaccountCreateSubaccount`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| subaccountName | string | 是 | Subaccount name, i.e. email address |
| label | string |  | Remark, length < 20 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.subUid | string |  | Subaccount user id |
| data.subaccountName | string |  | Subaccount name |
| data.status | string |  | Subaccount Status<br><br>normal <br><br>freeze <br><br>del |
| data.permList | string[] |  | Permissions, separated by comma.<br><br>withdraw<br><br>transfer<br><br>spot_trade<br><br>contract_trade<br><br>read<br><br>deposit |
| data.label | string |  | Label, less than 50 characters |
| data.cTime | string |  | Creation time<br><br>Unix millisecond timestamp, e.g. 1690196141868 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695784054984,
  "data": {
    "subUid": "********",
    "subaccountName": "***********",
    "status": "normal",
    "permList": [
      "read",
      "spot_trade",
      "contract_trade",
      "transfer",
      "withdraw",
      "deposit"
    ],
    "label": "old remark",
    "cTime": "1695784057280"
  }
}
```

## Get Subaccount List

`GET /api/v2/broker/account/subaccount-list`

Frequency limit: 1 time/1s (User ID)

Get subaccount list

Operation ID: `classicBrokerSubaccountGetSubaccountList`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| limit | query | string |  | Number of results returned. Default:10 Max:100 |
| idLessThan | query | string |  | Requests the content on the page before this ID (older data), the value input should be the subUid of the corresponding interface. |
| status | query | string |  | Subaccount Status<br><br>normal <br><br>freeze <br><br>del |
| startTime | query | string |  | The start time of subaccount list. i.e., getting the subaccounts after that timestamp<br><br>Unix millisecond timestamp, e.g. 1690196141868 |
| endTime | query | string |  | The end time of subaccount list. i.e., getting the subaccounts before that timestamp<br><br>Unix millisecond timestamp, e.g. 1690196141868 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.hasNextPage | boolean |  | Whether there is a next page |
| data.idLessThan | string |  | End ID for pagination |
| data.subList | string[] |  | Subaccount List |
| data.subUid | string |  | Subaccount user id |
| data.subaccountName | string |  | Username in email format generated by subaccountName as the prefix |
| data.status | string |  | Subaccount Status<br><br>normal <br><br>freeze <br><br>del |
| data.permList | string[] |  | Permissions<br><br>withdraw<br><br>transfer<br><br>spot_trade<br><br>contract_trade<br><br>read<br><br>deposit |
| data.label | string |  | Label |
| data.cTime | string |  | Creation time<br><br>Unix millisecond timestamp, e.g. 1690196141868 |
| data.uTime | string |  | Update time<br><br>Unix millisecond timestamp, e.g. 1690196141868 |
| data.language | string |  | Subaccount language<br><br>en_US<br><br>zh_CN<br><br>ja_JP<br><br>vi_VN<br><br>zh_TW<br><br>ru_RU<br><br>es_ES<br><br>tr_TR<br><br>fr_FR<br><br>de_DE<br><br>pt_PT<br><br>th_TH |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695784474208,
  "data": {
    "hasNextPage": false,
    "idLessThan": "404",
    "subList": [
      {
        "subUid": "111111",
        "subaccountName": "**********",
        "status": "normal",
        "permList": [
          "read",
          "spot_trade",
          "contract_trade",
          "transfer",
          "withdraw",
          "deposit"
        ],
        "label": "old remark",
        "language": "en_US",
        "cTime": "1695784057280",
        "uTime": "1695784057280"
      }
    ]
  }
}
```

## Modify Subaccount

`POST /api/v2/broker/account/modify-subaccount`

Frequency limit: 1 time/1s (API Key)

Modify status and permissions of subaccounts

Operation ID: `classicBrokerSubaccountModifySuaccount`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| subUid | string | 是 | Subaccount user id |
| permList | string[] | 是 | Permissions<br><br>withdraw<br><br>transfer<br><br>spot_trade<br><br>contract_trade<br><br>read<br><br>deposit<br><br>margin_trade: spot margin |
| status | string | 是 | Subaccount Status<br><br>`normal`: normal status <br><br>`freeze`:freeze status |
| language | string |  | Subaccount language<br><br>en_US<br><br>zh_CN<br><br>ja_JP<br><br>vi_VN<br><br>zh_TW<br><br>ru_RU<br><br>es_ES<br><br>tr_TR<br><br>fr_FR<br><br>de_DE<br><br>pt_PT<br><br>th_TH<br><br>Note: When modifying `language`, `permList` must also be passed, otherwise the modification will not take effect. |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.subUid | string |  | Subaccount user id |
| data.subaccountName | string |  | Username in email format generated by subaccountName as the prefix |
| data.status | string |  | Subaccount Status<br><br>normal <br><br>freeze |
| data.permList | string[] |  | Permissions<br><br>withdraw<br><br>transfer<br><br>spot_trade<br><br>contract_trade<br><br>read<br><br>deposit |
| data.label | string |  | Label |
| data.cTime | string |  | Creation time<br><br>Unix millisecond timestamp, e.g. 1690196141868 |
| data.uTime | string |  | Update time<br><br>Unix millisecond timestamp, e.g. 1690196141868 |
| data.language | string |  | Subaccount language<br><br>en_US<br><br>zh_CN<br><br>ja_JP<br><br>vi_VN<br><br>zh_TW<br><br>ru_RU<br><br>es_ES<br><br>tr_TR<br><br>fr_FR<br><br>de_DE<br><br>pt_PT<br><br>th_TH |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695784726115,
  "data": {
    "subUid": "*********",
    "subaccountName": "**********",
    "status": "normal",
    "permList": [
      "transfer"
    ],
    "label": "old remark",
    "language": "en_US",
    "cTime": "1692008679489",
    "uTime": "1695784728684"
  }
}
```

## Get Subaccount Email

`GET /api/v2/broker/account/subaccount-email`

Frequency limit：10 times/1s (User ID)

Get subaccount email

Operation ID: `classicBrokerSubaccountGetSubaccountEmail`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| subUid | query | string | 是 | Subaccount user id |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.subUid | string |  | Subaccount user id |
| data.subaccountName | string |  | Username in email format generated by subaccountName as the prefix |
| data.subaccountEmail | string |  | Subaccount email |
| data.cTime | string |  | Creation time<br><br>Unix millisecond timestamp, e.g. 1690196141868 |
| data.uTime | string |  | Update time<br><br>Unix millisecond timestamp, e.g. 1690196141868 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695784982805,
  "data": {
    "subUid": "********",
    "subaccountName": "xxx@xx.com",
    "subaccountEmail": "xxx@xx.com",
    "cTime": "1692008679000",
    "uTime": "1695784930000"
  }
}
```

## Get Subaccount Spot Assets

`GET /api/v2/broker/account/subaccount-spot-assets`

Frequency limit：10 times/1s (User ID)

Get subaccount spot assets

Operation ID: `classicBrokerSubaccountGetSubaccountSpotAssets`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| subUid | query | string | 是 | Subaccount user id |
| coin | query | string |  | Token name, e.g. USDT |
| assetType | query | string |  | Asset type<br><br>hold_only: Position coin<br><br>all: All coins<br><br>This field is used for querying the positions of multiple coins. The default value is "hold_only"<br><br>When only assetType is entered without coin, results of all eligible coins are returned. When both coin and assetType are entered, coin has higher priority. |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.assetsList | string[] |  | Spot asset list |
| data.coin | string |  | Token name |
| data.available | string |  | Available assets |
| data.frozen | string |  | Amount of frozen assets<br><br>Usually frozen when the order is placed |
| data.locked | string |  | Amount of locked assets<br><br>Locked assests required to become a fiat merchants, etc. |
| data.uTime | string |  | Update time |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695785115457,
  "data": {
    "assetsList": [
      {
        "coin": "BTC",
        "available": "100.00000000",
        "frozen": "0.00000000",
        "locked": "0.00000000",
        "uTime": "1692105973000"
      },
      {
        "coin": "USDT",
        "available": "100.00000000",
        "frozen": "0.00000000",
        "locked": "0.00000000",
        "uTime": "1692105971000"
      },
      {
        "coin": "ETH",
        "available": "100000.00000000",
        "frozen": "0.00000000",
        "locked": "0.00000000",
        "uTime": "1695024539000"
      }
    ]
  }
}
```

## Get Subaccount Future Assets

`GET /api/v2/broker/account/subaccount-future-assets`

Frequency limit:10 times/1s (User ID)

Only applicable for ND broker main-account

Fetch the future assets of the given subaccount

Operation ID: `classicBrokerSubaccountGetSubaccountFutureAssets`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| subUid | query | string | 是 | Sub account UID |
| productType | query | string | 是 | Product type<br><br>`USDT-FUTURES` USDT-M Futures<br><br>`COIN-FUTURES` Coin-M Futures<br><br>`USDC-FUTURES` USDC-M Futures |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.assetsList | string[] |  | Asset list |
| data.marginCoin | string |  | Margin coin |
| data.frozen | string |  | Frozen amount (margin currency) |
| data.locked | string |  | Locked amount (margin currency) |
| data.available | string |  | Available balance |
| data.crossedMaxAvailable | string |  | The maximum available balance for the 'crossed' Margin Mode (margin currency) |
| data.isolatedMaxAvailable | string |  | The maximum available balance for the 'isolated' Margin Mode(margin currency) |
| data.maxTransferOut | string |  | Maximum transferable |
| data.accountEquity | string |  | Account equity (margin currency) |
| data.usdtEquity | string |  | Account equity in USDT |
| data.btcEquity | string |  | Account equity in BTC |
| data.unrealizedPL | string |  | Unrealized PnL |
| data.uTime | string |  | Updated time, ms |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695785239709,
  "data": {
    "assetsList": [
      {
        "marginCoin": "USDT",
        "available": "0.00000000",
        "frozen": "0.00000000",
        "locked": "0.00000000",
        "crossedMaxAvailable": "0.00000000",
        "isolatedMaxAvailable": "0.00000000",
        "maxTransferOut": "0.00000000",
        "accountEquity": "0.00000000",
        "usdtEquity": "0.00000000",
        "btcEquity": "0.00000000",
        "unrealizedPL": "0.00000000",
        "uTime": "1695024539000"
      }
    ]
  }
}
```

## Create Subaccount Deposit Address

`POST /api/v2/broker/account/subaccount-address`

Frequency limit:10 times/1s (User ID)

Only applicable for ND broker main-account

Create deposit address for the specified subaccount

So far the `coin` in request parameter only accepts the following coins:

BTC,ETH,USDT,USDC,TRX,XRP,LTC,SOL,BNB,FTM,DOGE,ADA,SHIB,UNI,SEI,SUI,POL,FIL,LINK,TON,ARB,OP,DOT,AVAX

Operation ID: `classicBrokerSubaccountCreateSubaccountDepositAddress`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| subUid | string | 是 | Sub account UID |
| coin | string | 是 | Coin, e.g: BTC |
| chain | string |  | Chain name, default will use the main-chain of the 'coin' |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.subUid | string |  | Sub account UID |
| data.address | string |  | Deposit address |
| data.chain | string |  | Chain name |
| data.coin | string |  | Coin, like USDT |
| data.tag | string |  | Tag value, i.e. 'memo' of 'EOS', 'comment' of 'TON' |
| data.url | string |  | Block chain address |
| data.cTime | string |  | Created Time, ms |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695785563368,
  "data": {
    "subUid": "*************",
    "coin": "ETH",
    "address": "0x1eae2xxxxxxx7360bc59d2axxxxxx0caec9e",
    "chain": "trc20",
    "tag": "address1",
    "url": "https://etherscan.io/tx/",
    "cTime": "1694966400000"
  }
}
```

## Subaccount Withdrawal

`POST /api/v2/broker/account/subaccount-withdrawal`

Rate Limit: 1 req/sec/UID

ND broker initiates on chain withdraw or internal withdraw. 

Only applicable for ND broker main-account

So far the `coin` in request parameter only accepts the following coins:

BTC,ETH,USDT,USDC,TRX,XRP,LTC,SOL,BNB,FTM,DOGE,ADA,SHIB,UNI,SEI,SUI,POL,FIL,LINK,GRAM,ARB,OP,DOT,AVAX,BGB

Operation ID: `classicBrokerSubaccountSubaccountWithdraw`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| subUid | string | 是 | Sub account UID |
| coin | string | 是 | Coin, e.g. BTC<br><br>Only accept BTC/ETH/USDT/USDC/TRX/XRP/LTC/SOL/BNB/FTM/DOGE/ADA/SHIB/UNI/SEI/SUI/POL/FIL/LINK/GRAM/ARB/OP/DOT/AVAX/BGB |
| dest | string | 是 | Withdraw type. <br><br>`on_chain`: on chain withdraw<br><br>`internal_transfer`: internal withdraw |
| chain | string |  | Chain name<br><br>It will use the main-chain of the 'coin' by default |
| address | string | 是 | Address<br><br>When `dest`==`on_chain`, it should be the chain address<br><br>When `dest`==`internal_transfer`, it should be UID |
| amount | string | 是 | Withdraw amount |
| tag | string |  | Tag value for on chain withdraw, i.e. 'memo' of 'EOS', 'comment' of 'GRAM' |
| clientOid | string |  | Client Order ID |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.orderId | string |  | Order ID |
| data.clientOid | string |  | Client Order ID |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695785738672,
  "data": {
    "orderId": "121211212122",
    "clientOid": "121211212122"
  }
}
```

## Sub Deposit Auto Transfer

`POST /api/v2/broker/account/set-subaccount-autotransfer`

Frequency limit:10 times/1s (User ID)

Only applicable for ND broker main-account

 

 After call, the fund recharge to the given subaccount will automatically transfer to the specified 'toAccountType'

Operation ID: `classicBrokerSubaccountSubaccountDepositAutoTransfer`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| subUid | string | 是 | Sub account UID |
| coin | string | 是 | Coin |
| toAccountType | string | 是 | To account type：<br><br>spot default<br><br>usdt-futures  USDT professional futures（corresponding to mix_usdt）<br><br>coin-futures  Mixed futures（corresponding to mix_usd）<br><br>usdc-futures  USDC professional futures（corresponding to mix_usdc） |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | string |  | 'success' or 'fail' |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695786112492,
  "data": "success"
}
```

## Sub Deposit Records

`GET /api/v2/broker/subaccount-deposit`

Rate limit:10 req/sec/UID

Only applicable for ND broker main-account to get ND sub-accounts deposit record

Operation ID: `classicBrokerSubaccountSubaccountDepositRecords`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| orderId | query | string |  | recordsId <br><br> orderId and userId cannot both be empty. |
| userId | query | string |  | Sub account UID  <br><br> orderId and userId cannot both be empty. |
| startTime | query | string |  | Start timestamp <br><br>Milliseconds format of timestamp Unix, e.g. 1597026383085<br><br>(The maximum time span supported is three months. The default end time is three months if no value is set for the end time. ) |
| endTime | query | string |  | End timestamp <br><br>Milliseconds format of timestamp Unix, e.g. 1597026383085<br><br>(The maximum time span supported is three months. The default start time is three months ago if no value is set for the start time. ) |
| limit | query | string |  | Number of queries: Default: 20, maximum: 100. |
| idLessThan | query | string |  | Separate page content before this ID is requested (older data), and the value input should be the end ID of the last request. |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].orderId | string |  | orderId |
| data[].txId | string |  | txId |
| data[].coin | string |  | coin |
| data[].type | string |  | type |
| data[].dest | string |  | Deposit type |
| data[].amount | string |  | Deposit amount |
| data[].status | string |  | The status of the deposit process |
| data[].fromAddress | string |  | Deposit initiator information. When recharging on the chain, this field is the initiator wallet address; when transferring internally, this field is UID |
| data[].toAddress | string |  | Deposit recipient information. When recharging on the chain, this field is the initiator wallet address; when transferring internally, this field is UID |
| data[].fee | string |  | The amount of the fee. The pricing unit is the recharge currency |
| data[].chain | string |  | Deposit network |
| data[].confirm | string |  | Confirm the number of blocks |
| data[].tag | string |  | tag |
| data[].userId | string |  | Sub-account ID |
| data[].cTime | string |  | creation time ms |
| data[].uTime | string |  | update time ms |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1689833233282,
  "data": [
    {
      "orderId": "XXXXX",
      "txId": "XXXXXXX",
      "coin": "USDT",
      "type": "deposit",
      "dest": "internal_transfer",
      "amount": "10",
      "status": "success",
      "fromAddress": "123123",
      "toAddress": "456456",
      "fee": "1",
      "chain": "erc20",
      "confirm": "3",
      "tag": "xx",
      "userId": "123456",
      "cTime": "1689833233282",
      "uTime": "1689833233282"
    }
  ]
}
```

## Sub Withdrawal Records

`GET /api/v2/broker/subaccount-withdrawal`

Frequency limit:10 times/1s (User ID)

Only applicable for ND broker main-account

 

 After call, the fund withdrawal records

Operation ID: `classicBrokerSubaccountSubaccountWithdrawalRecords`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| orderId | query | string |  | withdrawal order ID |
| userId | query | string |  | Sub account UID |
| startTime | query | string |  | Start timestamp <br><br>Milliseconds format of timestamp Unix, e.g. 1597026383085<br><br>(The maximum time span supported is three months. The default end time is three months if no value is set for the end time. ) |
| endTime | query | string |  | End timestamp <br><br>Milliseconds format of timestamp Unix, e.g. 1597026383085<br><br>(The maximum time span supported is three months. The default start time is three months ago if no value is set for the start time. ) |
| limit | query | string |  | Number of queries: Default: 20, maximum: 100. |
| idLessThan | query | string |  | Separate page content before this ID is requested (older data), and the value input should be the end ID of the last request. |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.resultList | string[] |  | Withdrawal records list |
| data.orderId | string |  | orderId |
| data.txId | string |  | txId |
| data.coin | string |  | coin |
| data.type | string |  | type |
| data.dest | string |  | Withdrawal type |
| data.amount | string |  | Withdrawal amount |
| data.status | string |  | The status of the withdrawal process<br><br>`pending`:Pending preliminary examination<br><br>`fail`:Failed<br><br>`success`:Successful |
| data.fromAddress | string |  | Withdrawal initiator information. When withdrawal on the chain, this field is the initiator wallet address; when transferring internally, this field is UID |
| data.toAddress | string |  | Withdrawal recipient information. When withdrawal on the chain, this field is the initiator wallet address; when transferring internally, this field is UID |
| data.fee | string |  | The amount of the fee. The pricing unit is the recharge currency |
| data.chain | string |  | Withdrawal network |
| data.confirm | string |  | Confirm the number of blocks |
| data.tag | string |  | tag |
| data.userId | string |  | Sub-account ID |
| data.cTime | string |  | creation time ms |
| data.uTime | string |  | update time ms |
| data.endId | string |  | End ID for pagination |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1689833233282,
  "data": {
    "resultList": [
      {
        "orderId": "XXXXX",
        "txId": "XXXXXXX",
        "coin": "USDT",
        "type": "withdraw",
        "dest": "internal_transfer",
        "amount": "10",
        "status": "success",
        "fromAddress": "123123",
        "toAddress": "456456",
        "fee": "1",
        "chain": "erc20",
        "confirm": "3",
        "tag": "xx",
        "userId": "123456",
        "cTime": "1689833233282",
        "uTime": "1689833233282"
      }
    ],
    "endId": "12345"
  }
}
```

## Get Sub-accounts Deposit and Withdrawal Records

`GET /api/v2/broker/all-sub-deposit-withdrawal`

Rate limit:5 req/sec/UID

Only applicable for ND broker main-account. 

It`s able to get ND sub-accounts deposit and withdrawal records within **90 days**

Operation ID: `classicBrokerSubaccountGetSubaccountAllDepositWithdrawalRecords`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| startTime | query | string |  | Start timestamp <br><br>Milliseconds format of timestamp Unix, e.g. 1597026383085<br><br>If both start time and end time are empty, the default query time range will be yesterday from 00:00 to 23:59 (UTC+0)<br><br>Start time and end time must either both be provided or both be empty<br><br>An error will be reported if the time range exceeds 7 days |
| endTime | query | string |  | End timestamp <br><br>Milliseconds format of timestamp Unix, e.g. 1597026383085<br><br>If both start time and end time are empty, the default query time range will be yesterday from 00:00 to 23:59 (UTC+0)<br><br>Start time and end time must either both be provided or both be empty<br><br>An error will be reported if the time range exceeds 7 days |
| limit | query | string |  | Number of data<br><br>Default: 100, maximum: 100<br><br>100 entries will be returned by default when limit is over 100 |
| idLessThan | query | string |  | Separate page content |
| type | query | string |  | Records type<br><br>`all`: Both of deposit and withdrawal records(_default_)<br><br>`deposit`: Deposit records<br><br>`withdrawal`: Withdrawal records |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.list | string[] |  | Deposit/withdrawal records list |
| data.uid | string |  | Sub-account User ID |
| data.txId | string |  | Deposit or withdrawal txId |
| data.coin | string |  | Coin name |
| data.type | string |  | Deposit or withdrawal type<br><br>`deposit`: Deposit records<br><br>`withdrawal`: Withdrawal records |
| data.subType | string |  | Deposit or withdrawal sub-type<br><br>`onchain`: Deposit on chain or Normal withdrawal<br><br>`internal`: Internal transfer<br><br>`fast`: Fast deposit or withdrawal |
| data.amount | string |  | Deposit or withdrawal amount |
| data.status | string |  | Status<br><br>`pending`: Pending preliminary examination<br><br>`fail`: Failed<br><br>`success`: Success |
| data.ts | string |  | Deposit or withdrawal update time, Unix ms |
| data.endId | string |  | Used for paginating |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1689833233282,
  "data": {
    "list": [
      {
        "uid": "XXXXX",
        "txId": "XXXXXXX",
        "type": "deposit",
        "subType": "onchain",
        "coin": "USDT",
        "amount": "10",
        "status": "success",
        "ts": "123123"
      }
    ],
    "endId": "12345"
  }
}
```

## Get Broker Subaccounts

`GET /api/v2/broker/subaccounts`

Rate limit: 5 req/sec/UID

Please contact your BD or RM to apply for access permissions

Operation ID: `classicBrokerSubaccountGetBrokerSubaccounts`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| startTime | query | string |  | Start timestamp, milliseconds. If both start and end time are empty, the default time is yesterday 00:00-23:59 (UTC+0). StartTime and endTime can only be filled in at the same time or not. If it exceeds 30 days, an error will be reported. |
| endTime | query | string |  | End timestamp, milliseconds. If both start and end time are empty, the default time is yesterday 00:00-23:59 (UTC+0). StartTime and endTime can only be filled in at the same time or not. If it exceeds 30 days, an error will be reported. |
| pageSize | query | string |  | Number of items per page, default is 100, maximum is 1000, if more than 1000 items are returned, 100 items will be returned by default |
| pageNo | query | string |  | Pagination page number, default is 1 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].uid | string |  | User ID |
| data[].asset | string |  | Asset volume, U calculation |
| data[].firstTimeDeposit | string |  | First recharge time, Unix millisecond timestamp |
| data[].firstTimeTrade | string |  | First transaction time, Unix millisecond timestamp |
| data[].registerTime | string |  | Registration time, Unix millisecond timestamp |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1720841021439,
  "data": [
    {
      "uid": "5647948008",
      "asset": "5000.0001",
      "firstTimeDeposit": "1720497029245",
      "firstTimeTrade": "1720492699403",
      "registerTime": "1720492699403"
    }
  ]
}
```

## Get Broker Subaccounts Commissions

`GET /api/v2/broker/commissions`

Rate limit: 5 req/sec/UID

Please contact your BD or RM to apply for access permissions

Operation ID: `classicBrokerSubaccountGetBrokerSubaccountsCommissions`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| startTime | query | string |  | Start timestamp, milliseconds. If both start and end time are empty, the default time is yesterday 00:00-23:59 (UTC+0). StartTime and endTime can only be filled in at the same time or not. If it exceeds 30 days, an error will be reported. |
| endTime | query | string |  | End timestamp, milliseconds. If both start and end time are empty, the default time is yesterday 00:00-23:59 (UTC+0). StartTime and endTime can only be filled in at the same time or not. If it exceeds 30 days, an error will be reported. |
| pageSize | query | string |  | Number of items per page, default is 100, maximum is 1000, if more than 1000 items are returned, 100 items will be returned by default |
| pageNo | query | string |  | Pagination page number, default is 1 |
| bizType | query | string |  | Optional, business type <br><br>- `spot`  <br><br>- `futures`  <br><br> If not filled, all types of commission information will be returne |
| subBizType | query | string |  | Optional, business subtype <br><br>- `spot_trade` <br><br>- `spot_margin` <br><br>- `usdt_futures` <br><br>- `usdc_futures` <br><br>- `coin_futures` <br><br>- - When `bizType=spot`, this parameter can be filled with `spot_trade` and `spot_margin`<br><br>- - When `bizType=future`, this parameter can be filled with `usdt_future`, `usdc_future` and `coin_future` |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].uid | string |  | User ID |
| data[].coin | string |  | Commission coin |
| data[].symbol | string |  | symbol |
| data[].dealtAmount | string |  | Transaction amount |
| data[].totalFee | string |  | Total Fee |
| data[].deductedFee | string |  | Deduction of handling fee |
| data[].paidFee | string |  | Actual paid handling fee |
| data[].markUpFee | string |  | Add some handling fee |
| data[].totalCommission | string |  | Total Commission |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1720750077022,
  "data": [
    {
      "uid": "564xxx8008",
      "coin": "BTC",
      "symbol": "BTC/USDT",
      "dealtAmount": "199.81724",
      "totalFee": "0.00000768",
      "deductedFee": "0",
      "paidFee": "0.00000768",
      "markUpFee": "0.00000603",
      "totalCommission": "0.00000686"
    }
  ]
}
```

## Get Broker Trade Volume

`GET /api/v2/broker/trade-volume`

Rate limit: 5 req/sec/UID

Please contact your BD or RM to apply for access permissions

Operation ID: `classicBrokerSubaccountGetBrokerTradeVolume`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| startTime | query | string |  | Start timestamp, milliseconds. If both start and end time are empty, the default time is yesterday 00:00-23:59 (UTC+0). StartTime and endTime can only be filled in at the same time or not. If it exceeds 30 days, an error will be reported. |
| endTime | query | string |  | End timestamp, milliseconds. If both start and end time are empty, the default time is yesterday 00:00-23:59 (UTC+0). StartTime and endTime can only be filled in at the same time or not. If it exceeds 30 days, an error will be reported. |
| pageSize | query | string |  | Number of items per page, default is 100, maximum is 1000, if more than 1000 items are returned, 100 items will be returned by default |
| pageNo | query | string |  | Pagination page number, default is 1 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].uid | string |  | User ID |
| data[].volume | string |  | Transaction amount, with 8 digits of precision |
| data[].spotVolume | string |  | Spot transaction amount, with 8-digit precision |
| data[].futureVolume | string |  | Contract transaction amount, with 8-digit precision |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1720841112418,
  "data": [
    {
      "uid": "5647948008",
      "volume": "99322.66476",
      "spotVolume": "310.66476",
      "futureVolume": "99012"
    }
  ]
}
```


---

经典账户 — 经纪商子账户、充提币与划转相关接口。

版本: 1.0.0

## 服务地址

- `https://api.bitget.com`

## 接口列表

- `GET /api/v2/broker/account/info` — 获取独立经纪商账户信息
- `POST /api/v2/broker/account/modify-subaccount-email` — 子账户绑定邮箱
- `POST /api/v2/broker/account/create-subaccount` — 创建子账户
- `GET /api/v2/broker/account/subaccount-list` — 获取子账户列表
- `POST /api/v2/broker/account/modify-subaccount` — 修改子账户状态与权限
- `GET /api/v2/broker/account/subaccount-email` — 获取子账户邮箱
- `GET /api/v2/broker/account/subaccount-spot-assets` — 获取子账户的现货账户资产信息
- `GET /api/v2/broker/account/subaccount-future-assets` — 获取子账户的合约账户资产信息
- `POST /api/v2/broker/account/subaccount-address` — 创建子账户充值地址
- `POST /api/v2/broker/account/subaccount-withdrawal` — 子账户提币
- `POST /api/v2/broker/account/set-subaccount-autotransfer` — 设置充币自动划转
- `GET /api/v2/broker/subaccount-deposit` — 获取子账户充值记录
- `GET /api/v2/broker/subaccount-withdrawal` — 获取子账户提币记录
- `GET /api/v2/broker/all-sub-deposit-withdrawal` — 获取子账户充值提币记录
- `GET /api/v2/broker/subaccounts` — 获取经纪商子账户列表
- `GET /api/v2/broker/commissions` — 获取经纪商子账户佣金记录
- `GET /api/v2/broker/trade-volume` — 获取经纪商子账户交易记录

## 获取独立经纪商账户信息

`GET /api/v2/broker/account/info`

限速规则 10次/1s (UID)

查看独立经纪商母账户的账户信息

Operation ID: `classicBrokerSubaccountGetBrokerAccountInfo`

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.subAccountSize | string |  | 当前子账户数量 |
| data.maxSubAccountSize | string |  | 最大可以创建的子账户数量 |
| data.uTime | string |  | 数据最后更新时间，毫秒时间戳 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695783465795,
  "data": {
    "subAccountSize": "9",
    "maxSubAccountSize": "10",
    "uTime": "1691635508000"
  }
}
```

## 子账户绑定邮箱

`POST /api/v2/broker/account/modify-subaccount-email`

限速规则 10次/1s (UID)

独立经纪商母账户获取子账户绑定的接收邮件的邮箱

Operation ID: `classicBrokerSubaccountModifySubaccountEmail`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| subUid | string | 是 | 子账户uid |
| subaccountEmail | string | 是 | 子账户邮箱 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | string |  |  |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695784928863,
  "data": "success"
}
```

## 创建子账户

`POST /api/v2/broker/account/create-subaccount`

限速规则 1次/1s (UID)

创建子账户

Operation ID: `classicBrokerSubaccountCreateSubaccount`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| subaccountName | string | 是 | 子账号用户名 |
| label | string |  | 备注，单个用户不能重复 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.subUid | string |  | 子账户uid |
| data.subaccountName | string |  | 用作生成子账户用户名 |
| data.status | string |  | normal 正常<br><br>freeze 冻结<br><br>del 删除 |
| data.permList | string[] |  | withdraw 提币权限<br><br>transfer 划转<br><br>spot_trade 现货交易<br><br>contract_trade 合约交易<br><br>read 读权限<br><br>deposit 充值权限 |
| data.label | string |  | 最多不超过50个字符 |
| data.cTime | string |  | 数据创建时间，毫秒时间戳 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695784054984,
  "data": {
    "subUid": "*********",
    "subaccountName": "****@*****.com",
    "status": "normal",
    "permList": [
      "read",
      "spot_trade",
      "contract_trade",
      "transfer",
      "withdraw",
      "deposit"
    ],
    "label": "old remark",
    "cTime": "1695784057280"
  }
}
```

## 获取子账户列表

`GET /api/v2/broker/account/subaccount-list`

限速规则 1次/1s (UID)

获取子账户列表

Operation ID: `classicBrokerSubaccountGetSubaccountList`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| limit | query | string |  | 默认10 最大100 |
| idLessThan | query | string |  | 上次查询lastEndId，上次查询返回的最后一个subUid，最近创建的子账户优先返回 |
| status | query | string |  | normal 正常<br><br>freeze 冻结<br><br>del 删除 |
| startTime | query | string |  | 开始时间 |
| endTime | query | string |  | 结束时间 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.hasNextPage | boolean |  | 是否有下一页 |
| data.idLessThan | string |  | 分页结束ID |
| data.subList | string[] |  | 子账户列表 |
| data.subUid | string |  | 子账户uid |
| data.subaccountName | string |  | subaccountName作为前缀生成的虚拟邮箱用户名 |
| data.status | string |  | normal 正常<br><br>freeze 冻结<br><br>del 删除 |
| data.permList | string[] |  | withdraw 提币权限<br><br>transfer 划转<br><br>spot_trade 现货交易<br><br>contract_trade 合约交易<br><br>readonly 读权限<br><br>deposit 充值权限 |
| data.label | string |  | 备注名称 |
| data.cTime | string |  | 数据创建时间，毫秒时间戳 |
| data.uTime | string |  | 数据更新时间，毫秒时间戳 |
| data.language | string |  | 子账户语言<br><br>en_US<br><br>zh_CN<br><br>ja_JP<br><br>vi_VN<br><br>zh_TW<br><br>ru_RU<br><br>es_ES<br><br>tr_TR<br><br>fr_FR<br><br>de_DE<br><br>pt_PT<br><br>th_TH |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695784474208,
  "data": {
    "hasNextPage": false,
    "idLessThan": "404",
    "subList": [
      {
        "subUid": "*******",
        "subaccountName": "****@*****.com",
        "status": "normal",
        "permList": [
          "read",
          "spot_trade",
          "contract_trade",
          "transfer",
          "withdraw",
          "deposit"
        ],
        "label": "old remark",
        "language": "en_US",
        "cTime": "1695784057280",
        "uTime": "1695784057280"
      }
    ]
  }
}
```

## 修改子账户状态与权限

`POST /api/v2/broker/account/modify-subaccount`

限速规则 1次/1s (Apikey)

修改子账户状态与权限

Operation ID: `classicBrokerSubaccountModifySuaccount`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| subUid | string | 是 | 子账号Uid |
| permList | string[] | 是 | 权限数组，枚举值：<br><br>withdraw 提币权限<br><br>transfer 划转<br><br>spot_trade 现货交易<br><br>contract_trade 合约交易<br><br>readonly 读权限<br><br>deposit 充值权限<br><br>margin_trade 杠杆交易 |
| status | string | 是 | 子账号状态<br><br>normal 正常<br><br>freeze 冻结 |
| language | string |  | 子账号语言<br><br>en_US<br><br>zh_CN<br><br>ja_JP<br><br>vi_VN<br><br>zh_TW<br><br>ru_RU<br><br>es_ES<br><br>tr_TR<br><br>fr_FR<br><br>de_DE<br><br>pt_PT<br><br>th_TH<br><br>注：修改`language`时，必须同时携带`permList`参数，否则修改不成功 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.subUid | string |  | 子账户uid |
| data.subaccountName | string |  | subaccountName作为前缀生成的虚拟邮箱用户名 |
| data.status | string |  | normal 正常<br><br>freeze 冻结 |
| data.permList | string[] |  | withdraw 提币权限<br><br>transfer 划转<br><br>spot_trade 现货交易<br><br>contract_trade 合约交易<br><br>readonly 读权限<br><br>deposit 充值权限 |
| data.label | string |  | 备注名称 3-20个字符 |
| data.cTime | string |  | 数据创建时间，毫秒时间戳 |
| data.uTime | string |  | 数据更新时间，毫秒时间戳 |
| data.language | string |  | 子账户语言<br><br>en_US<br><br>zh_CN<br><br>ja_JP<br><br>vi_VN<br><br>zh_TW<br><br>ru_RU<br><br>es_ES<br><br>tr_TR<br><br>fr_FR<br><br>de_DE<br><br>pt_PT<br><br>th_TH |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695784726115,
  "data": {
    "subUid": "*******",
    "subaccountName": "****@*****.com",
    "status": "normal",
    "permList": [
      "transfer"
    ],
    "label": "old remark",
    "language": "en_US",
    "cTime": "1692008679489",
    "uTime": "1695784728684"
  }
}
```

## 获取子账户邮箱

`GET /api/v2/broker/account/subaccount-email`

限速规则 10次/1s (UID)

独立经纪商母账户获取子账户绑定的接收邮件的邮箱

Operation ID: `classicBrokerSubaccountGetSubaccountEmail`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| subUid | query | string | 是 | 子账户uid |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.subUid | string |  | 子账户uid |
| data.subaccountName | string |  | subaccountName作为前缀生成的虚拟邮箱用户名 |
| data.subaccountEmail | string |  | 子账户绑定的邮箱，用于接收邮件等 |
| data.cTime | string |  | 数据创建时间，毫秒时间戳 |
| data.uTime | string |  | 数据更新时间，毫秒时间戳 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695784982805,
  "data": {
    "subUid": "***********",
    "subaccountName": "xxx@xx.com",
    "subaccountEmail": "xxx@xx.com",
    "cTime": "1692008679000",
    "uTime": "1695784930000"
  }
}
```

## 获取子账户的现货账户资产信息

`GET /api/v2/broker/account/subaccount-spot-assets`

限速规则 10次/1s (UID)

独立经纪商母账户获取子账户的现货账户资产信息

Operation ID: `classicBrokerSubaccountGetSubaccountSpotAssets`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| subUid | query | string | 是 | 子账户uid |
| coin | query | string |  | 币种，如BTC，详见币种列表 |
| assetType | query | string |  | 资产类型<br><br>hold_only持仓币种<br><br>all全部币种<br><br>该字段用于返回多币种持仓数据。默认值为hold_only<br><br>当不传coin，只传assetType时，则返回全部符合条件的币种。当同时传参coin及assetType时，coin优先级更高 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.assetsList | string[] |  | 现货资产列表 |
| data.coin | string |  | 币种名称 |
| data.available | string |  | 可用资产 |
| data.frozen | string |  | 冻结资产 |
| data.locked | string |  | 锁仓资产 |
| data.uTime | string |  | 更新时间 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695785115457,
  "data": {
    "assetsList": [
      {
        "coin": "BTC",
        "available": "100.00000000",
        "frozen": "0.00000000",
        "locked": "0.00000000",
        "uTime": "1692105973000"
      },
      {
        "coin": "USDT",
        "available": "100.00000000",
        "frozen": "0.00000000",
        "locked": "0.00000000",
        "uTime": "1692105971000"
      },
      {
        "coin": "ETH",
        "available": "100000.00000000",
        "frozen": "0.00000000",
        "locked": "0.00000000",
        "uTime": "1695024539000"
      }
    ]
  }
}
```

## 获取子账户的合约账户资产信息

`GET /api/v2/broker/account/subaccount-future-assets`

限速规则 10次/1s (UID)

独立经纪商母账户获取子账户的合约账户资产信息

Operation ID: `classicBrokerSubaccountGetSubaccountFutureAssets`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| subUid | query | string | 是 | 子账户uid |
| productType | query | string | 是 | 产品类型<br><br>`USDT-FUTURES` U本位合约<br><br>`COIN-FUTURES` 币本位合约<br><br>`USDC-FUTURES` USDC合约 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.assetsList | string[] |  | 各币种资产详细信息 |
| data.marginCoin | string |  | 保证金币种 |
| data.frozen | string |  | 冻结数量(保证金币种) |
| data.locked | string |  | 锁定数量(保证金币种) |
| data.available | string |  | 账户可用数量 |
| data.crossedMaxAvailable | string |  | 全仓最大可用来开仓余额(保证金币种) |
| data.isolatedMaxAvailable | string |  | 逐仓最大可用来开仓余额(保证金币种) |
| data.maxTransferOut | string |  | 最大可转出 |
| data.accountEquity | string |  | 账户权益(保证金币种) |
| data.usdtEquity | string |  | 折算USDT账户权益 |
| data.btcEquity | string |  | 折算BTC账户权益 |
| data.unrealizedPL | string |  | 未实现盈亏 |
| data.uTime | string |  | 更新时间 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695785239709,
  "data": {
    "assetsList": [
      {
        "marginCoin": "USDT",
        "available": "0.00000000",
        "frozen": "0.00000000",
        "locked": "0.00000000",
        "crossedMaxAvailable": "0.00000000",
        "isolatedMaxAvailable": "0.00000000",
        "maxTransferOut": "0.00000000",
        "accountEquity": "0.00000000",
        "usdtEquity": "0.00000000",
        "btcEquity": "0.00000000",
        "unrealizedPL": "0.00000000",
        "uTime": "1695024539000"
      }
    ]
  }
}
```

## 创建子账户充值地址

`POST /api/v2/broker/account/subaccount-address`

限速规则 10次/1s (UID)

独立经纪商母账户新增子账户的充值地址，仅适用主账户调用

目前`coin`入参只支持以下币种：

BTC,ETH,USDT,USDC,TRX,XRP,LTC,SOL,BNB,FTM,DOGE,ADA,SHIB,UNI,SEI,SUI,POL,FIL,LINK,TON,ARB,OP,DOT,AVAX

Operation ID: `classicBrokerSubaccountCreateSubaccountDepositAddress`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| subUid | string | 是 | 子账户Uid |
| coin | string | 是 | 币种，如BTC |
| chain | string |  | 链类型 如果不填该参数，则默认为币种的主链 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.subUid | string |  | 子账户Uid |
| data.address | string |  | 提币地址 |
| data.chain | string |  | 链名称 |
| data.coin | string |  | 币种名称 |
| data.tag | string |  | EOS的memo，TON的comment都会通过该字段返回，其他链同理 |
| data.url | string |  | 区块链地址 |
| data.cTime | string |  | 创建时间，毫秒时间戳 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695785563368,
  "data": {
    "subUid": "***********",
    "coin": "ETH",
    "address": "0x1eae2xxxxxxx7360bc59d2axxxxxx0caec9e",
    "chain": "trc20",
    "tag": "address1",
    "url": "https://etherscan.io/tx/",
    "cTime": "1694966400000"
  }
}
```

## 子账户提币

`POST /api/v2/broker/account/subaccount-withdrawal`

限速规则: 1次/秒/UID

独立经纪商母账户从子账户链上提币或内部提币，仅适用主账户调用。

目前`coin`入参只支持以下币种：

BTC,ETH,USDT,USDC,TRX,XRP,LTC,SOL,BNB,FTM,DOGE,ADA,SHIB,UNI,SEI,SUI,POL,FIL,LINK,GRAM,ARB,OP,DOT,AVAX,BGB

Operation ID: `classicBrokerSubaccountSubaccountWithdraw`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| subUid | string | 是 | 子账户Uid |
| coin | string | 是 | 币种，如BTC |
| dest | string | 是 | 提币方式: <br><br>on_chain 链上提币 <br><br> internal_transfer 内部转账 |
| chain | string |  | 链类型 如果不填该参数，则默认为币种的主链 |
| address | string | 是 | 当选择链上提币时，填链上地址；当选择内部转账时，填uid |
| amount | string | 是 | 提币数量 |
| tag | string |  | EOS的memo，GRAM的comment都使用该字段填入 |
| clientOid | string |  | 客户端自定义Id 唯一 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.orderId | string |  | 订单ID |
| data.clientOid | string |  | 客户自定义订单ID |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695785738672,
  "data": {
    "orderId": "121211212122",
    "clientOid": "121211212122"
  }
}
```

## 设置充币自动划转

`POST /api/v2/broker/account/set-subaccount-autotransfer`

限速规则 10次/1s (UID)

独立经纪商母账户设置子账户的充值自动划转至特定资金账户，仅适用主账户调用

Operation ID: `classicBrokerSubaccountSubaccountDepositAutoTransfer`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| subUid | string | 是 | 子账户Uid |
| coin | string | 是 | 币种 |
| toAccountType | string | 是 | 账户类型：<br><br>spot 现货<br><br>usdt-futures  USDT本位合约（对应原mix_usdt）<br><br>coin-futures  币本位合约（对应原mix_usd）<br><br>usdc-futures  USDC本位合约（对应原mix_usdc） |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | string |  | 'success' or 'fail' |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695786112492,
  "data": "success"
}
```

## 获取子账户充值记录

`GET /api/v2/broker/subaccount-deposit`

限速规则 10次/1s (UID)

独立经纪商获取子账户充值记录，仅适用主账户调用

Operation ID: `classicBrokerSubaccountSubaccountDepositRecords`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| orderId | query | string |  | 充值订单id <br><br> orderId和 userId 不能都为空 |
| userId | query | string |  | 子账户uid <br><br>  orderId和 userId 不能都为空 |
| startTime | query | string |  | 开始时间戳 <br><br>Unix时间戳的毫秒数格式，如 1597026383085<br><br>（时间跨度最大支持三个月，若不传开始时间，则默认开始时间为三个月。） |
| endTime | query | string |  | 结束时间戳 <br><br>Unix时间戳的毫秒数格式，如 1597026383085<br><br>（时间跨度最大支持三个月，若不传结束时间，则默认结束时间为三个月。） |
| idLessThan | query | string |  | 请求此ID之后（更新的数据）的分页内容，传的值为对应接口的 endId |
| limit | query | string |  | 查询条数 默认20，最大100 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].orderId | string |  | 订单ID |
| data[].txId | string |  | 交易ID |
| data[].coin | string |  | 币种名称 |
| data[].type | string |  | 类型 |
| data[].dest | string |  | 充币类型 |
| data[].amount | string |  | 充币数量 |
| data[].status | string |  | 充币流程的状态 |
| data[].fromAddress | string |  | 充币发起人信息。 链上充值时，该字段为发起人钱包地址；内部转账时，该字段为UID |
| data[].toAddress | string |  | 充币接收人信息。 链上充值时，该字段为发起人钱包地址；内部转账时，该字段为UID |
| data[].fee | string |  | 手续费数量。计价单位为充值币种 |
| data[].chain | string |  | 充币网络 |
| data[].confirm | string |  | 确认区块数量 |
| data[].tag | string |  | 标签 |
| data[].userId | string |  | 子账户ID |
| data[].cTime | string |  | 创建时间 ms |
| data[].uTime | string |  | 修改时间 ms |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1689833233282,
  "data": [
    {
      "orderId": "XXXXX",
      "txId": "XXXXXXX",
      "coin": "USDT",
      "type": "deposit",
      "dest": "internal_transfer",
      "amount": "10",
      "status": "success",
      "fromAddress": "123123",
      "toAddress": "456456",
      "fee": "1",
      "chain": "erc20",
      "confirm": "3",
      "tag": "xx",
      "userId": "123456",
      "cTime": "1689833233282",
      "uTime": "1689833233282"
    }
  ]
}
```

## 获取子账户提币记录

`GET /api/v2/broker/subaccount-withdrawal`

限速规则 10次/1s (UID)

独立经纪商获取子账户提币记录，仅适用主账户调用

Operation ID: `classicBrokerSubaccountSubaccountWithdrawalRecords`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| orderId | query | string |  | 提币订单id |
| userId | query | string |  | 子账户uid |
| startTime | query | string |  | 开始时间戳 <br><br>Unix时间戳的毫秒数格式，如 1597026383085<br><br>（时间跨度最大支持三个月，若不传开始时间，则默认开始时间为三个月。） |
| endTime | query | string |  | 结束时间戳 <br><br>Unix时间戳的毫秒数格式，如 1597026383085<br><br>（时间跨度最大支持三个月，若不传结束时间，则默认结束时间为三个月。） |
| idLessThan | query | string |  | 请求此ID之后（更新的数据）的分页内容，传的值为对应接口的 endId |
| limit | query | string |  | 查询条数 默认20，最大100 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.resultList | string[] |  | 提币记录列表 |
| data.orderId | string |  | 订单ID |
| data.txId | string |  | 交易ID |
| data.coin | string |  | 币种名称 |
| data.type | string |  | 类型 |
| data.dest | string |  | 提币类型 |
| data.amount | string |  | 提币数量 |
| data.status | string |  | 提币流程的状态<br><br>`pending` 确认中<br><br>`fail` 失败 <br><br>`success` 成功 |
| data.fromAddress | string |  | 提币发起人信息。 链上提币时，该字段为发起人钱包地址；内部转账时，该字段为UID |
| data.toAddress | string |  | 提币接收人信息。 链上提币时，该字段为发起人钱包地址；内部转账时，该字段为UID |
| data.fee | string |  | 手续费数量。计价单位为提币币种 |
| data.chain | string |  | 提币网络 |
| data.confirm | string |  | 确认区块数量 |
| data.tag | string |  | 标签 |
| data.userId | string |  | 子账户ID |
| data.cTime | string |  | 创建时间 ms |
| data.uTime | string |  | 修改时间 ms |
| data.endId | string |  | 分页结束ID |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1689833233282,
  "data": {
    "resultList": [
      {
        "orderId": "XXXXX",
        "txId": "XXXXXXX",
        "coin": "USDT",
        "type": "withdraw",
        "dest": "internal_transfer",
        "amount": "10",
        "status": "success",
        "fromAddress": "123123",
        "toAddress": "456456",
        "fee": "1",
        "chain": "erc20",
        "confirm": "3",
        "tag": "xx",
        "userId": "123456",
        "cTime": "1689833233282",
        "uTime": "1689833233282"
      }
    ],
    "endId": "12345"
  }
}
```

## 获取子账户充值提币记录

`GET /api/v2/broker/all-sub-deposit-withdrawal`

限速规则：5次/秒 (UID)

获获取独立经纪商获取子账户最近**90天**的充值、提币记录，仅适用主账户API key调用

Operation ID: `classicBrokerSubaccountGetSubaccountAllDepositWithdrawalRecords`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| startTime | query | string |  | 开始时间戳，Unix毫秒<br><br>开始与结束时间均为空默认时间为查询昨日00:00-23:59(UTC+0)数据<br><br>startTime与endTime只能同时填或不填<br><br>startTime和endTime范围不能超过7天 |
| endTime | query | string |  | 结束时间戳，Unix毫秒<br><br>开始与结束时间均为空默认时间为查询昨日00:00-23:59(UTC+0)数据<br><br>startTime与endTime只能同时填或不填<br><br>startTime和endTime范围不能超过7天 |
| limit | query | string |  | 每页数量<br><br>默认100，最大100，超过100默认返回100条 |
| idLessThan | query | string |  | 分页页码 |
| type | query | string |  | 充提类型<br><br>`all`: 全部充提记录(_默认_)<br><br>`deposit`: 充值记录<br><br>`withdrawal`: 提币记录 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.list | string[] |  | 充值提币记录列表 |
| data.uid | string |  | 子账户UID |
| data.txId | string |  | 充值提币 txId |
| data.coin | string |  | 币种名称 |
| data.type | string |  | 充提类型<br><br>`deposit`: 充值记录<br><br>`withdrawal`: 提币记录 |
| data.subType | string |  | 充提子类型<br><br>`onchain`: 链上充值或普通提币<br><br>`internal`: 内部转账<br><br>`fast`: 快速充提（链上 + 内部地址） |
| data.amount | string |  | 充提数量 |
| data.status | string |  | 状态<br><br>`pending`: 确认中<br><br>`fail`: 失败<br><br>`success`: 成功 |
| data.ts | string |  | 充提记录更新时间戳，毫秒 |
| data.endId | string |  | 用于翻页 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1689833233282,
  "data": {
    "list": [
      {
        "uid": "XXXXX",
        "txId": "XXXXXXX",
        "type": "deposit",
        "subType": "onchain",
        "coin": "USDT",
        "amount": "10",
        "status": "success",
        "ts": "123123"
      }
    ],
    "endId": "12345"
  }
}
```

## 获取经纪商子账户列表

`GET /api/v2/broker/subaccounts`

限速规则 5次/1s (UID)

请联系对接BD或者RM申请接入权限

Operation ID: `classicBrokerSubaccountGetBrokerSubaccounts`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| startTime | query | string |  | 开始时间戳，毫秒，开始与结束时间均为空默认时间为昨日00:00-23:59(UTC+0)，startTime与endTime只能同时填或不填，超出30天报错 |
| endTime | query | string |  | 结束时间戳，毫秒，开始与结束时间均为空默认时间为昨日00:00-23:59(UTC+0)，startTime与endTime只能同时填或不填，超出30天报错 |
| pageSize | query | string |  | 每页数量，默认100，最大1000，超过1000默认返回100条 |
| pageNo | query | string |  | 分页页码，默认是1 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].uid | string |  | User ID |
| data[].asset | string |  | 资产量，折U计算 |
| data[].firstTimeDeposit | string |  | 首次充值时间，Unix毫秒时间戳 |
| data[].firstTimeTrade | string |  | 首次交易时间，Unix毫秒时间戳 |
| data[].registerTime | string |  | 注册时间，Unix毫秒时间戳 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1720841021439,
  "data": [
    {
      "uid": "5647948008",
      "asset": "5000.0001",
      "firstTimeDeposit": "1720497029245",
      "firstTimeTrade": "1720492699403",
      "registerTime": "1720492699403"
    }
  ]
}
```

## 获取经纪商子账户佣金记录

`GET /api/v2/broker/commissions`

限速规则 5次/1s (UID)

请联系对接BD或者RM申请接入权限

Operation ID: `classicBrokerSubaccountGetBrokerSubaccountsCommissions`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| startTime | query | string |  | 开始时间戳，毫秒，开始与结束时间均为空默认时间为昨日00:00-23:59(UTC+0)，startTime与endTime只能同时填或不填，超出30天报错 |
| endTime | query | string |  | 结束时间戳，毫秒，开始与结束时间均为空默认时间为昨日00:00-23:59(UTC+0)，startTime与endTime只能同时填或不填，超出30天报错 |
| pageSize | query | string |  | 每页数量，默认100，最大1000，超过1000默认返回100条 |
| pageNo | query | string |  | 分页页码，默认是1 |
| bizType | query | string |  | 选填，业务类型 <br><br>- `spot` 现货 <br><br>- `futures` 合约 <br><br> 如不填，则返回全部类型佣金信息 |
| subBizType | query | string |  | 选填，业务子类型<br><br>- `spot_trade` 现货交易<br><br>- `spot_margin` 现货杠杆<br><br>- `usdt_futures` U本位合约<br><br>- `usdc_futures` USDC合约<br><br>- `coin_futures` 币本位合约<br><br>当`bizType=spot`时，该参数可填`spot_trade`及`spot_margin`<br><br> 当`bizType=future`时，该参数可填`usdt_future`,`usdc_future`及`coin_future` |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].uid | string |  | User ID |
| data[].coin | string |  | 佣金币种 |
| data[].symbol | string |  | 交易对 |
| data[].dealtAmount | string |  | 成交额 |
| data[].totalFee | string |  | 总手续费 |
| data[].deductedFee | string |  | 扣减手续费 |
| data[].paidFee | string |  | 实付手续费 |
| data[].markUpFee | string |  | 加点手续费 |
| data[].totalCommission | string |  | 总计佣金 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1720750077022,
  "data": [
    {
      "uid": "564xxx8008",
      "coin": "BTC",
      "symbol": "BTC/USDT",
      "dealtAmount": "199.81724",
      "totalFee": "0.00000768",
      "deductedFee": "0",
      "paidFee": "0.00000768",
      "markUpFee": "0.00000603",
      "totalCommission": "0.00000686"
    }
  ]
}
```

## 获取经纪商子账户交易记录

`GET /api/v2/broker/trade-volume`

限速规则 5次/1s (UID)

请联系对接BD或者RM申请接入权限

Operation ID: `classicBrokerSubaccountGetBrokerTradeVolume`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| startTime | query | string |  | 开始时间戳，毫秒，开始与结束时间均为空默认时间为昨日00:00-23:59(UTC+0)，startTime与endTime只能同时填或不填，超出30天报错 |
| endTime | query | string |  | 结束时间戳，毫秒，开始与结束时间均为空默认时间为昨日00:00-23:59(UTC+0)，startTime与endTime只能同时填或不填，超出30天报错 |
| pageSize | query | string |  | 每页数量，默认100，最大1000，超过1000默认返回100条 |
| pageNo | query | string |  | 分页页码，默认是1 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].uid | string |  | User ID |
| data[].volume | string |  | 交易额，精度为8位 |
| data[].spotVolume | string |  | 现货交易额，精度为8位 |
| data[].futureVolume | string |  | 合约交易额，精度为8位 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1720841112418,
  "data": [
    {
      "uid": "5647948008",
      "volume": "99322.66476",
      "spotVolume": "310.66476",
      "futureVolume": "99012"
    }
  ]
}
```