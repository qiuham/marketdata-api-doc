---
exchange: bitget
source_url: https://www.bitget.com/docs/catalog/broker
api_type: REST
updated_at: 2026-11-20 19:01:47.863751
---

# Broker

Broker sub-account creation, management, API key, deposit/withdrawal, and commission APIs.

版本: 1.0.0

## 服务地址

- `https://api.bitget.com`

## 接口列表

- `POST /api/v3/broker/create-sub` — Create Broker Sub-Account
- `POST /api/v3/broker/create-sub-apikey` — Create Broker Sub-Account API Key
- `POST /api/v3/broker/delete-sub-apikey` — Delete Broker Sub-Account API Key
- `GET /api/v3/broker/all-sub-deposit-withdrawal` — Get All Broker Sub-Account Deposit Withdrawal
- `GET /api/v3/broker/commission` — Get Broker Commission
- `GET /api/v3/broker/query-sub-apikey` — Get Broker Sub-Account API Key
- `GET /api/v3/broker/sub-list` — Get Broker Sub-Account List
- `POST /api/v3/broker/modify-sub-apikey` — Modify Broker Sub-Account API Key
- `POST /api/v3/broker/modify-sub` — Modify Broker Sub-Account
- `POST /api/v3/broker/sub-deposit-address` — Get Broker Sub-Account Deposit Address
- `POST /api/v3/broker/sub-withdrawal` — Broker Sub-Account Withdrawal
- `POST /api/v3/broker/modify-subaccount-email` — Modify Subaccount Email
- `GET /api/v3/broker/subaccount-email` — Get Subaccount Email
- `GET /api/v3/broker/trade-volume` — Get Broker Trade Volume
- `GET /api/v3/broker/total-commission` — Get Total Commission
- `GET /api/v3/broker/order-commission` — Get Order Commission
- `GET /api/v3/broker/rebate-info` — Get Rebate Info

## Create Broker Sub-Account

`POST /api/v3/broker/create-sub`

Rate limit: 20/sec/UID

Only the master account with a user type of ND Broker can call this API endpoint.

Operation ID: `brokerCreateSubaccount`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| subaccountName | string | 是 | Sub-account username. |
| label | string | 是 | label<br><br>up to a maximum of 50 characters. |

```json
{
  "subaccountName": "hunterusers182114141",
  "label": "hunterusersub21523121"
}
```

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.subUid | string |  | Sub-account UID |
| data.subaccountName | string |  | Sub-account username |
| data.subaccountEmail | string |  | Sub-account email<br><br>By default a system-generated virtual email; if an email has been bound separately, the bound email will be displayed |
| data.status | string |  | Sub-account status<br><br>`normal`<br><br>`freeze` |
| data.permList | string[] |  | Permission list<br><br>`withdraw`<br><br>`transfer`<br><br>`spot_trade` spot trading<br><br>`contract_trade` futures trading<br><br>`margin_trade` margin trading<br><br>`deposit` deposit permission |
| data.label | string |  | Label |
| data.cTime | string |  | Account creation time<br><br>Unix timestamp in milliseconds |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1767148977459,
  "data": {
    "subUid": "12345678910",
    "subaccountName": "",
    "subaccountEmail": "hun****@broker",
    "status": "normal",
    "permList": [
      "read",
      "uta_spot_trade",
      "uta_margin_trade",
      "uta_contract_trade",
      "transfer",
      "withdraw",
      "deposit"
    ],
    "label": "hunterusersub21523121",
    "cTime": "1767148977593"
  }
}
```

## Create Broker Sub-Account API Key

`POST /api/v3/broker/create-sub-apikey`

Rate limit: 20/sec/UID

Only the master account with a user type of ND Broker can call this API endpoint.

Operation ID: `brokerCreateSubaccountApikey`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| subUid | string | 是 | Sub-account UID |
| passphrase | string | 是 | Passphrase<br><br>Required to call the API. If lost, please create a new API key. |
| label | string | 是 | label |
| ipList | string[] | 是 | IP whitelist<br><br>Up to 30 entries can be provided |
| permType | string | 是 | Permission type:<br><br>`read_write` read & write<br><br>`read_only` read-only |
| permList | string[] | 是 | Permission list:<br><br>`uta_trade` UTA trading<br><br>`uta_mgt` UTA management<br><br>`withdraw` (permType must be read_write) |

```json
{
  "subUid": "12345678910",
  "passphrase": "12345678",
  "label": "338040211757111_test01",
  "permType": "read_write",
  "permList": [
    "uta_trade",
    "uta_mgt",
    "withdraw"
  ]
}
```

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.subUid | string |  | Sub-account UID |
| data.label | string |  | Label |
| data.apiKey | string |  | API Key |
| data.secretKey | string |  | Secret Key |
| data.permType | string |  | Permission type:<br><br>`read_write` read & write<br><br>`read_only` read-only |
| data.permList | string[] |  | Permission list:<br><br>`uta_trade` UTA trading<br><br>`uta_mgt` UTA management<br><br>`withdraw` (permType must be read_write) |
| data.ipList | string[] |  | IP whitelist |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1767151739925,
  "data": {
    "subUid": "12345678910",
    "label": "338040211757111_test01",
    "apiKey": "bg_12345678910",
    "secretKey": "123456789106d3",
    "permType": "read_write",
    "permList": [
      "uta_mgt",
      "uta_trade",
      "withdraw"
    ],
    "ipList": null
  }
}
```

## Delete Broker Sub-Account API Key

`POST /api/v3/broker/delete-sub-apikey`

Rate limit: 20/sec/UID

Only the master account with a user type of ND Broker can call this API endpoint.

- This endpoint has no response parameters.

- It returns the deletion result synchronously.

- Determine whether the deletion succeeded or failed (and the failure reason) based on the returned `code` and `msg`.

Operation ID: `brokerDeleteSubaccountApikey`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| subUid | string | 是 | Sub-account UID |
| apiKey | string | 是 | API Key |

```json
{
  "subUid": "12345678910",
  "apiKey": "bg_123456789109"
}
```

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  | Code |
| msg | string |  | Message |
| requestTime | integer |  | Request Time |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1767151778823
}
```

## Get All Broker Sub-Account Deposit Withdrawal

`GET /api/v3/broker/all-sub-deposit-withdrawal`

Rate limit: 20/sec/UID

Only the master account with a user type of ND Broker can call this API endpoint.

Operation ID: `brokerGetAllSubaccountDepositWithdrawal`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| startTime | query | string |  | Record start time<br><br>Unix timestamp in milliseconds. If both startTime and endTime are empty, the default query time range is yesterday 00:00–23:59 (UTC+0). The time range between startTime and endTime cannot exceed 7 days. |
| endTime | query | string |  | Record end time<br><br>Unix timestamp in milliseconds. If both startTime and endTime are empty, the default query time range is yesterday 00:00–23:59 (UTC+0). The time range between startTime and endTime cannot exceed 7 days. |
| limit | query | string |  | Number of items per page<br><br>default 100, maximum 100. |
| cursor | query | string |  | Cursor ID. |
| status | query | string |  | Status<br><br>`pending` Confirming<br><br>`fail` Failed<br><br>`success` Successful |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.list | object[] |  | Record list |
| data.list[].uid | string |  | Sub-account UID |
| data.list[].txId | string |  | Deposit/withdraw/transfer ID |
| data.list[].coin | string |  | Coin name |
| data.list[].type | string |  | Deposit/withdraw type:<br><br>`deposit` deposit record<br><br>`withdrawal` withdrawal record |
| data.list[].subType | string |  | Sub-type:<br><br>`onchain` on-chain deposit or regular withdrawal;<br><br>`internal` internal transfer;<br><br>`fast` fast deposit/withdraw (on-chain + internal address) |
| data.list[].amount | string |  | Deposit/withdraw amount |
| data.list[].status | string |  | Status<br><br>`pending` Confirming<br><br>`fail` Failed<br><br>`success` Successful |
| data.list[].ts | string |  | Record update time<br><br>Unix timestamp in milliseconds |
| data.endId | string |  | Cursor ID for next page (the smallest record ID in current page) |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1767151164765,
  "data": {
    "list": [
      {
        "uid": "12345678910",
        "txId": "1390096439417995264",
        "type": "withdrawal",
        "subType": "internal",
        "coin": "USDT",
        "amount": "10.000000000",
        "status": "fail",
        "ts": "1767150805032"
      }
    ],
    "endId": "1390096439417995264"
  }
}
```

## Get Broker Commission

`GET /api/v3/broker/commission`

Rate limit: 20/sec/UID

Only the master account with a user type of ND Broker can call this API endpoint.

Operation ID: `brokerGetBrokerCommission`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| startTime | query | string |  | Query start time<br><br>Unix timestamp in milliseconds. If both startTime and endTime are omitted, the default query range is yesterday 00:00–23:59 (UTC+0). The interval between startTime and endTime for a single query cannot exceed 30 days. |
| endTime | query | string |  | Query end time<br><br>Unix timestamp in milliseconds. If both startTime and endTime are omitted, the default query range is yesterday 00:00–23:59 (UTC+0). The interval between startTime and endTime for a single query cannot exceed 30 days. |
| pageSize | query | string |  | Number of items per page<br><br>default 100, maximum 1000 |
| pageNo | query | string |  | Page number<br><br>default 1. |
| bizType | query | string |  | Business type<br><br>`spot`<br><br>`futures`<br><br>If not provided, commission data for all types will be returned. |
| subBizType | query | string |  | Business sub-type:<br><br>`spot_trade` spot trading<br><br>`spot_margin` spot margin<br><br>`usdt_futures` USDT futures<br><br>`usdc_futures` USDC futures<br><br>`coin_futures` coin-margin futures<br><br>When `bizType=spot`, this parameter can be `spot_trade` or `spot_margin`. When `bizType=futures`, this parameter can be `usdt_futures`, `usdc_futures`, or `coin_futures`. |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].uid | string |  | User ID |
| data[].coin | string |  | Commission currency |
| data[].symbol | string |  | Symbol |
| data[].dealtAmount | string |  | Traded amount |
| data[].totalFee | string |  | Total fee |
| data[].deductedFee | string |  | Deducted fee |
| data[].paidFee | string |  | Fee paid |
| data[].markUpFee | string |  | Markup fee |
| data[].totalCommission | string |  | Total commission |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1767677788472,
  "data": [
    {
      "uid": "1359901376",
      "coin": "BTC",
      "symbol": "BTC/USDT",
      "dealtAmount": "84.346065",
      "totalFee": "0.0000005",
      "deductedFee": "0",
      "paidFee": "0.0000005",
      "markUpFee": "0",
      "totalCommission": "0.00000002"
    }
  ]
}
```

## Get Broker Sub-Account API Key

`GET /api/v3/broker/query-sub-apikey`

Rate limit: 20/sec/UID

Only the master account with a user type of ND Broker can call this API endpoint.

Operation ID: `brokerGetSubaccountApikey`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| subUid | query | string | 是 | Sub-account UID |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.subUid | string |  | Sub-account UID |
| data.label | string |  | Label |
| data.apiKey | string |  | API Key |
| data.secretKey | string |  | Secret Key |
| data.permType | string |  | Permission type:<br><br>`read_write` read & write<br><br>`read_only` read-only |
| data.permList | string[] |  | Permission list:<br><br>`uta_trade` UTA trading<br><br>`uta_mgt` UTA management<br><br>`withdraw` (permType must be read_write) |
| data.ipList | string[] |  | IP whitelist |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1767151739925,
  "data": {
    "subUid": "12345678910",
    "label": "338040211757111_test01",
    "apiKey": "bg_12345678910",
    "secretKey": "12345678910d3",
    "permType": "read_write",
    "permList": [
      "uta_mgt",
      "uta_trade",
      "withdraw"
    ],
    "ipList": null
  }
}
```

## Get Broker Sub-Account List

`GET /api/v3/broker/sub-list`

Rate limit: 20/sec/UID

Only the master account with a user type of ND Broker can call this API endpoint.

Operation ID: `brokerGetSubaccountList`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| limit | query | string |  | Number of items per page<br><br>default 10, maximum 100. |
| cursor | query | string |  | Cursor ID<br><br>Used for pagination. Omit it on the first call. For subsequent calls, pass in the last `subUid` returned by the previous query. |
| status | query | string |  | Account status:<br><br>`normal` normal<br><br>`freeze` frozen |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.subList | object[] |  | Sub-account list |
| data.subList[].subUid | string |  | Sub-account UID |
| data.subList[].subaccountName | string |  | Sub-account username |
| data.subList[].subaccountEmail | string |  | Sub-account email |
| data.subList[].status | string |  | Sub-account status:<br><br>`normal`<br><br>`freeze` |
| data.subList[].permList | string[] |  | Permission list<br><br>`withdraw`<br><br>`transfer`<br><br>`spot_trade` spot trading<br><br>`contract_trade` futures trading<br><br>`margin_trade` margin trading<br><br>`deposit` deposit permission |
| data.subList[].label | string |  | Label |
| data.subList[].cTime | string |  | Account creation time<br><br>Unix timestamp in milliseconds |
| data.subList[].uTime | string |  | Account update time<br><br>Unix timestamp in milliseconds |
| data.subList[].language | string |  | Sub-account language.<br><br>`en_US`<br><br>`zh_CN`<br><br>`ja_JP`<br><br>`vi_VN`<br><br>`zh_TW`<br><br>`ru_RU`<br><br>`es_ES`<br><br>`tr_TR`<br><br>`fr_FR`<br><br>`de_DE`<br><br>`pt_PT`<br><br>`th_TH` |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1767149918448,
  "data": {
    "subList": [
      {
        "subUid": "12345678910",
        "subaccountName": "hun****@broker_8383826362",
        "subaccountEmail": null,
        "status": "normal",
        "permList": [
          "read",
          "uta_spot_trade",
          "uta_margin_trade",
          "uta_contract_trade",
          "transfer",
          "withdraw",
          "deposit"
        ],
        "label": "hunterusersub21523121",
        "language": "zh_CN",
        "cTime": "1767148977593",
        "uTime": "1767148977593"
      }
    ]
  }
}
```

## Modify Broker Sub-Account API Key

`POST /api/v3/broker/modify-sub-apikey`

Rate limit: 20/sec/UID

Only the master account with a user type of ND Broker can call this API endpoint.

Operation ID: `brokerModifySubaccountApikey`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| subUid | string | 是 | Sub-account UID |
| passphrase | string | 是 | Passphrase<br><br>Required to call the API; if lost, please recreate the API key |
| apiKey | string | 是 | API Key |
| label | string |  | label |
| ipList | string[] |  | IP whitelist<br><br>Up to 30 entries |
| permType | string |  | Permission type:<br><br>`read_write` read & write<br><br>`read_only` read-only |
| permList | string[] |  | Permission list:<br><br>`uta_trade` UTA trading<br><br>`uta_mgt` UTA management<br><br>`withdraw` (permType must be read_write) |

```json
{
  "subUid": "12345678910",
  "passphrase": "12345678",
  "apiKey": "bg_12345678910",
  "label": "338040211757111_test01",
  "permType": "read_write",
  "permList": [
    "uta_trade",
    "uta_mgt",
    "withdraw"
  ]
}
```

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.subUid | string |  | Sub-account UID |
| data.label | string |  | Label |
| data.apiKey | string |  | API Key |
| data.permType | string |  | Permission type:<br><br>`read_write` read & write<br><br>`read_only` read-only |
| data.permList | string[] |  | Permission list:<br><br>`uta_trade` UTA trading<br><br>`uta_mgt` UTA management<br><br>`withdraw` (permType must be read_write) |
| data.ipList | string[] |  | IP whitelist |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1767151778823,
  "data": {
    "subUid": "12345678910",
    "label": "3380407571_test02update",
    "apiKey": "bg_12345678910",
    "permType": "read_write",
    "permList": [
      "uta_mgt",
      "uta_trade",
      "withdraw"
    ],
    "ipList": [
      "1.3.1.2"
    ]
  }
}
```

## Modify Broker Sub-Account

`POST /api/v3/broker/modify-sub`

Rate limit: 20/sec/UID

Only the master account with a user type of ND Broker can call this API endpoint.

Operation ID: `brokerModifySubaccount`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| subUid | string | 是 | Sub-account UID |
| status | string |  | Sub-account status:<br><br>`normal`<br><br>`freeze` |
| permList | string |  | Permission list<br><br>`withdraw`<br><br>`transfer`<br><br>`spot_trade` spot trading<br><br>`contract_trade` futures trading<br><br>`margin_trade` margin trading<br><br>`deposit` deposit permission |

```json
{
  "subUid": "1234567891",
  "status": "freeze"
}
```

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.subUid | string |  | Sub-account UID |
| data.status | string |  | Sub-account status:<br><br>`normal`<br><br>`freeze` |
| data.subaccountName | string |  | Sub-account username |
| data.label | string |  | Label |
| data.permList | string[] |  | Permission list<br><br>`withdraw`<br><br>`transfer`<br><br>`spot_trade` spot trading<br><br>`contract_trade` futures trading<br><br>`margin_trade` margin trading<br><br>`deposit` deposit permission |
| data.cTime | string |  | Account creation time<br><br>Unix timestamp in milliseconds |
| data.uTime | string |  | Account update time<br><br>Unix timestamp in milliseconds |
| data.language | string |  | Sub-account language.<br><br>`en_US`<br><br>`zh_CN`<br><br>`ja_JP`<br><br>`vi_VN`<br><br>`zh_TW`<br><br>`ru_RU`<br><br>`es_ES`<br><br>`tr_TR`<br><br>`fr_FR`<br><br>`de_DE`<br><br>`pt_PT`<br><br>`th_TH` |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1767150632929,
  "data": {
    "subUid": "1234567891",
    "subaccountName": "hun****@broker",
    "status": "freeze",
    "permList": [
      "uta_spot_trade",
      "transfer",
      "deposit"
    ],
    "label": "hunterusersub123121",
    "cTime": "1766476082509",
    "uTime": "1766476102463"
  }
}
```

## Get Broker Sub-Account Deposit Address

`POST /api/v3/broker/sub-deposit-address`

Rate limit: 20/sec/UID

Only the master account with a user type of ND Broker can call this API endpoint.

Operation ID: `brokerSubaccountDepositAddress`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| subUid | string | 是 | Sub-account UID |
| coin | string | 是 | Coin name |
| chain | string |  | Chain name<br><br>If this parameter is not provided, the default will be the coin's primary (main) chain |

```json
{
  "subUid": "12345678910",
  "chain": "ERC20",
  "coin": "USDT"
}
```

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.subUid | string |  | Sub-account UID |
| data.coin | string |  | Coin name |
| data.chain | string |  | Chain name |
| data.address | string |  | Deposit address |
| data.tag | string |  | Tag<br><br>Used for some chains (e.g., EOS memo, TON comment) |
| data.url | string |  | Custom order ID |
| data.cTime | string |  | Creation time |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1767150821166,
  "data": {
    "subUid": "12345678910",
    "coin": "USDT",
    "address": "0xe4de63ebbf937385c17e7332557fe5c3337648ca",
    "chain": "ERC20",
    "tag": null,
    "url": "https://sepolia.etherscan.io/tx/",
    "cTime": "1765987200000"
  }
}
```

## Broker Sub-Account Withdrawal

`POST /api/v3/broker/sub-withdrawal`

Rate limit: 20/sec/UID

Only the master account with a user type of ND Broker can call this API endpoint.

Broker sub-account withdrawal API has restrictions and currently supports only the following currencies:

BTC, ETH, USDT, USDC, TRX, XRP, LTC, SOL, BNB, FTM, DOGE, ADA, SHIB, UNI, SEI, SUI, POL, FIL, LINK, GRAM, ARB, OP, DOT, AVAX, BGB

Operation ID: `brokerSubaccountWithdrawal`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| subUid | string | 是 | Sub-account UID |
| coin | string | 是 | Coin name |
| dest | string | 是 | Withdrawal method:<br><br>`on_chain` on-chain withdrawal<br><br>`internal_transfer` internal transfer |
| chain | string |  | Chain name<br><br>If this parameter is not provided, it defaults to the coin's main chain |
| address | string | 是 | Withdrawal address<br><br>When using on-chain withdrawal, enter the on-chain address; when using internal transfer, enter the UID |
| amount | string | 是 | Withdrawal amount |
| tag | string |  | Tag<br><br>Used for some chains (e.g., EOS memo, GRAM comment) |
| clientOid | string |  | Custom order ID |

```json
{
  "subUid": "12345678910",
  "dest": "internal_transfer",
  "coin": "USDT",
  "address": "123456789",
  "amount": "10",
  "clientOid": "91500512549_1765977438100"
}
```

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.orderId | string |  | Order ID |
| data.clientOid | string |  | Custom order ID |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1767150755184,
  "data": {
    "orderId": "1390096439417995264",
    "clientOid": "91500512549_1765977438100"
  }
}
```

## Modify Subaccount Email

`POST /api/v3/broker/modify-subaccount-email`

Rate limit: 10/sec/UID

Modify the email bound to a sub-account.

Operation ID: `brokerModifySubaccountEmail`

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

## Get Subaccount Email

`GET /api/v3/broker/subaccount-email`

Rate limit: 10/sec/UID

Get subaccount email

Operation ID: `brokerGetSubaccountEmail`

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
    "subaccountName": "<EMAIL_ADDRESS>",
    "subaccountEmail": "<EMAIL_ADDRESS>",
    "cTime": "1692008679000",
    "uTime": "1695784930000"
  }
}
```

## Get Broker Trade Volume

`GET /api/v3/broker/trade-volume`

Rate limit: 5/sec/UID

Please contact your BD or RM to apply for access permissions

Operation ID: `brokerGetTradeVolume`

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

## Get Total Commission

`GET /api/v3/broker/total-commission`

Rate limit: 20/sec/UID

Data retention: 365 days

Historical data available from: 2025/6/1

Data granularity: daily

Data update granularity: daily, previous day’s data is updated on the current day

Time zone: UTC+8

startTime and endTime should either both be set or both left unset

This API supports retrieving data within the past 365 days (data is available starting from 2025/6/1 at the earliest)

If startTime and endTime are not set in the request, the default returned information will be for yesterday (00:00-23:

  59 UTC+8)

Data update frequency: T+1 (UTC+8)

Operation ID: `brokerGetTotalCommission`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| startTime | query | string |  | Start timestamp in milliseconds. If both startTime and endTime are empty, the default time range is yesterday 00:00–23:59 (UTC+8). startTime and endTime must either both be set or both left unset. An error will be returned if the range exceeds 180 days. |
| endTime | query | string |  | End timestamp in milliseconds. If both startTime and endTime are empty, the default time range is yesterday 00:00–23:59 (UTC+8). startTime and endTime must either both be set or both left unset. An error will be returned if the range exceeds 180 days. |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].date | string |  | Commission date |
| data[].totalTradingVolume | string |  | Broker’s total trading volume for the day |
| data[].totalActiveTraders | string |  | Number of active traders for the broker that day |
| data[].totalCommission | string |  | Total commission earned by the broker (USDT) |
| data[].spot | object |  | Spot data |
| data[].spot.spotTradingVolume | string |  | Spot trading volume (USDT) |
| data[].spot.spotTradingFee | string |  | Actual spot trading fee collected (USDT) |
| data[].spot.spotPureTradingFee | string |  | Net spot trading fee (USDT) (after deducting negative maker, etc.; used as the base for commission calculation) |
| data[].spot.spotCommission | string |  | Spot commission (USDT) |
| data[].futures | object |  | Futures data |
| data[].futures.futuresTradingVolume | string |  | Futures trading volume (USDT) |
| data[].futures.futuresTradingFee | string |  | Actual futures trading fee collected (USDT) |
| data[].futures.futuresPureTradingFee | string |  | Net futures trading fee (USDT) (after deducting negative maker, etc.; used as the base for commission calculation） |
| data[].futures.futuresCommission | string |  | Futures commission (USDT) |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 17609760000000.0,
  "data": [
    {
      "date": "17609760000000",
      "totalTradingVolume": "24679.848225",
      "totalActiveTraders": "1",
      "totalCommission": "0",
      "spot": {
        "spotTradingVolume": "419.847925",
        "spotTradingFee": "0.34999881",
        "spotPureTradingFee": "0.34999881",
        "spotCommission": "0"
      },
      "futures": {
        "futuresTradingVolume": "24260.0003",
        "futuresTradingFee": "15.5999965399983",
        "futuresPureTradingFee": "15.5999965399983",
        "futuresCommission": "0"
      }
    }
  ]
}
```

## Get Order Commission

`GET /api/v3/broker/order-commission`

Rate limit: 20/sec/UID

Data storage: 30 days

Historical data backtracking: 2025/9/1

Data granularity: daily

Data update frequency: daily, previous day's data is updated on the current day

Time zone: UTC+8

startTime and endTime should either both be set or both not set

The maximum time span supported for startTime and endTime is 30 days

This API supports retrieving data within the past 30 days

If startTime and endTime are not set in the request, the default return will be information for yesterday (00:00-23:59

  UTC+8)

This API data is updated on a T+1 basis

Transaction details only show those marked with broker channel id

Operation ID: `brokerGetOrderCommission`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| startTime | query | string |  | Start timestamp in milliseconds. If both startTime and endTime are empty, the default time range is yesterday 00:00–23:59 (UTC+8). startTime and endTime must either both be filled or both be empty. An error will be returned if the range exceeds 180 days. |
| endTime | query | string |  | End timestamp in milliseconds. If both startTime and endTime are empty, the default time range is yesterday 00:00–23:59 (UTC+8). startTime and endTime must either both be filled or both be empty. An error will be returned if the range exceeds 180 days. |
| limit | query | string |  | Pagination limit. Maximum: 500, Default: 500 |
| uid | query | string |  | UID |
| orderid | query | string |  | Order ID |
| idLessThan | query | string |  | Cursor ID for pagination. Do not pass this parameter for the first request; for subsequent requests, use the endId value from the previous response to paginate. |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.commissionlist | object[] |  | Rebate (commission) list |
| data.commissionlist[].fillId | string |  | Fill ID |
| data.commissionlist[].orderId | string |  | Order ID |
| data.commissionlist[].ts | string |  | Fill timestamp |
| data.commissionlist[].clientOid | string |  | Custom order ID |
| data.commissionlist[].bizType | string |  | Transaction type<br><br>`spot`Spot<br><br>`futures`Futures |
| data.commissionlist[].subBizType | string |  | Sub-transaction type<br><br>`spot_trade`Spot trading<br><br>`spot_margin`Spot margin<br><br>`usdt_futures`usdt futures<br><br>`coin_futures`coin futures<br><br>`usdc_futures`usdc futures |
| data.commissionlist[].symbol | string |  | Symbol |
| data.commissionlist[].volume | string |  | Trade amount<br><br> unit: USDT, with full precision |
| data.commissionlist[].fee | string |  | Total fee<br><br>unit: USDT, with full precision |
| data.commissionlist[].pureFee | string |  | Net fee<br><br>unit: USDT, with full precision |
| data.commissionlist[].rebateAmount | string |  | Broker commission<br><br>unit: USDT, with full precision |
| data.endId | string |  | Cursor ID |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695786824200,
  "data": {
    "commissionlist": [
      {
        "fillId": "121211212122",
        "orderId": "121211212122",
        "ts": "1689833233282",
        "clientOid": "121211212122",
        "bizType": "spot",
        "subBizType": "spot_trade",
        "symbol": "BTCUSDT",
        "volume": "1000",
        "fee": "1",
        "pureFee": "1",
        "rebateAmount": "0.5"
      }
    ],
    "endId": "12345"
  }
}
```

## Get Rebate Info

`GET /api/v3/broker/rebate-info`

Rate limit: 20/sec/UID

Data retention: 30 days

Real-time data

Operation ID: `brokerGetRebateInfo`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| uid | query | string | 是 | UID |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.affiliationType | string |  | Type of rebate relationship<br><br>`affiliate`Client channel<br><br>`official` Official (website) channel |
| data.userLevel | string |  | User level<br><br>`VIP0`<br><br>`VIP1`<br><br>...<br><br>`VIP7`<br><br>`PRO1`<br><br>...<br><br>`PRO6` |
| data.clientSpotRebateRatio | string |  | Spot trading rebate ratio available to the user |
| data.clientFuturesRebateRatio | string |  | Futures trading rebate ratio available to the user |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695786824200,
  "data": {
    "affiliationType": "affiliate",
    "userLevel": "VIP7",
    "clientSpotRebateRatio": "0.07",
    "clientFuturesRebateRatio": "0.08"
  }
}
```


---

经纪商子账户创建、管理、API Key、充提币与佣金相关接口。

版本: 1.0.0

## 服务地址

- `https://api.bitget.com`

## 接口列表

- `POST /api/v3/broker/create-sub` — 创建经纪商子账户
- `POST /api/v3/broker/create-sub-apikey` — 创建经纪商子账户API Key
- `POST /api/v3/broker/delete-sub-apikey` — 删除经纪商子账户API Key
- `GET /api/v3/broker/all-sub-deposit-withdrawal` — 获取经纪商子账户充提记录
- `GET /api/v3/broker/commission` — 获取经纪商子账户佣金记录
- `GET /api/v3/broker/query-sub-apikey` — 获取经纪商子账户API Key
- `GET /api/v3/broker/sub-list` — 获取经纪商子账户列表
- `POST /api/v3/broker/modify-sub-apikey` — 修改经纪商子账户API Key
- `POST /api/v3/broker/modify-sub` — 修改经纪商子账户
- `POST /api/v3/broker/sub-deposit-address` — 获取经纪商子账户充值地址
- `POST /api/v3/broker/sub-withdrawal` — 经纪商子账户提币
- `POST /api/v3/broker/modify-subaccount-email` — 子账户绑定邮箱
- `GET /api/v3/broker/subaccount-email` — 获取子账户邮箱
- `GET /api/v3/broker/trade-volume` — 获取经纪商子账户交易记录
- `GET /api/v3/broker/total-commission` — 获取经纪商佣金数据
- `GET /api/v3/broker/order-commission` — 获取经纪商订单返佣数据
- `GET /api/v3/broker/rebate-info` — 获取用户的经纪商返佣信息

## 创建经纪商子账户

`POST /api/v3/broker/create-sub`

限频: 20次/秒/UID

仅用户类型为ND Broker的母账户才能调用该接口。

Operation ID: `brokerCreateSubaccount`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| subaccountName | string | 是 | 子账户用户名 |
| label | string | 是 | 备注<br><br>最多不超过50个字符 |

```json
{
  "subaccountName": "hunterusers182114141",
  "label": "hunterusersub21523121"
}
```

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.subUid | string |  | 子账户uid |
| data.subaccountName | string |  | 子账户用户名 |
| data.subaccountEmail | string |  | 子账户邮箱<br><br>默认为系统生成的虚拟邮箱；若单独绑定过邮箱，则展示绑定邮箱 |
| data.status | string |  | 子账户状态<br><br>`normal` 正常<br><br>`freeze` 冻结 |
| data.permList | string[] |  | 权限列表<br><br>`withdraw` 提币<br><br>`transfer` 划转<br><br>`spot_trade` 现货交易<br><br>`contract_trade` 合约交易<br><br>`margin_trade` 杠杆交易<br><br>`deposit` 充值权限 |
| data.label | string |  | 备注 |
| data.cTime | string |  | 账户创建时间<br><br>Unix毫秒时间戳 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1767148977459,
  "data": {
    "subUid": "1234567891",
    "subaccountName": "",
    "subaccountEmail": "hun****@broker",
    "status": "normal",
    "permList": [
      "read",
      "uta_spot_trade",
      "uta_margin_trade",
      "uta_contract_trade",
      "transfer",
      "withdraw",
      "deposit"
    ],
    "label": "hunterusersub21523121",
    "cTime": "1767148977593"
  }
}
```

## 创建经纪商子账户API Key

`POST /api/v3/broker/create-sub-apikey`

限频: 20次/秒/UID

仅用户类型为ND Broker的母账户才能调用该接口。

Operation ID: `brokerCreateSubaccountApikey`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| subUid | string | 是 | 子账户uid |
| passphrase | string | 是 | Passphrase<br><br>passphrase是调用 API 接口的必要参数，如果遗失请重新创建API key |
| label | string | 是 | 备注 |
| ipList | string[] | 是 | IP白名单<br><br>最多传入30个 |
| permType | string | 是 | 权限类型<br><br>`read_write` 读写权限<br><br>`read_only` 只读权限 |
| permList | string[] | 是 | 权限<br><br>`uta_trade` UTA交易<br><br>`uta_mgt` UTA管理<br><br>`withdraw` 提币(permType需要为read_write类型) |

```json
{
  "subUid": "12345678910",
  "passphrase": "12345678",
  "label": "338040211757111_test01",
  "permType": "read_write",
  "permList": [
    "uta_trade",
    "uta_mgt",
    "withdraw"
  ]
}
```

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.subUid | string |  | 子账户uid |
| data.label | string |  | 备注 |
| data.apiKey | string |  | API Key |
| data.secretKey | string |  | 私钥 |
| data.permType | string |  | 权限类型<br><br>`read_write` 读写权限<br><br>`read_only` 只读权限 |
| data.permList | string[] |  | 权限<br><br>`uta_trade` UTA交易<br><br>`uta_mgt` UTA管理<br><br>`withdraw` 提币(permType需要为read_write类型) |
| data.ipList | string[] |  | IP白名单 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1767151739925,
  "data": {
    "subUid": "12345678910",
    "label": "338040211757111_test01",
    "apiKey": "bg_123456789",
    "secretKey": "123456789111111",
    "permType": "read_write",
    "permList": [
      "uta_mgt",
      "uta_trade",
      "withdraw"
    ],
    "ipList": null
  }
}
```

## 删除经纪商子账户API Key

`POST /api/v3/broker/delete-sub-apikey`

限频: 20次/秒/UID

仅用户类型为ND Broker的母账户才能调用该接口。

- 该接口无响应参数

- 该接口同步返回删除处理结果

- 根据code和msg返回删除成功及失败结果 & 失败原因

Operation ID: `brokerDeleteSubaccountApikey`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| subUid | string | 是 | 子账户uid |
| apiKey | string | 是 | API Key |

```json
{
  "subUid": "12345678910",
  "apiKey": "bg_12345678910"
}
```

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  | 状态码 |
| msg | string |  | 响应信息 |
| requestTime | integer |  | 请求时间 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1767151778823
}
```

## 获取经纪商子账户充提记录

`GET /api/v3/broker/all-sub-deposit-withdrawal`

限频规则: 20次/秒/UID

仅用户类型为ND Broker的母账户才能调用该接口。

Operation ID: `brokerGetAllSubaccountDepositWithdrawal`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| startTime | query | string |  | 记录开始时间<br><br>Unix毫秒时间戳。开始与结束时间均为空默认时间为查询昨日00:00-23:59(UTC+0)数据。startTime和endTime范围不能超过7天 |
| endTime | query | string |  | 记录结束时间<br><br>Unix毫秒时间戳。开始与结束时间均为空默认时间为查询昨日00:00-23:59(UTC+0)数据。startTime和endTime范围不能超过7天 |
| limit | query | string |  | 每页条目数<br><br>默认100，最大100 |
| cursor | query | string |  | 游标ID |
| status | query | string |  | 状态<br><br>`pending` 确认中<br><br>`fail` 失败<br><br>`success` 成功 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.list | object[] |  | 记录列表 |
| data.list[].uid | string |  | 子账户UID |
| data.list[].txId | string |  | 充值提币转账ID |
| data.list[].coin | string |  | 币种名称 |
| data.list[].type | string |  | 充提类型<br><br>`deposit` 充值记录<br><br>`withdrawal` 提币记录 |
| data.list[].subType | string |  | 充提子类型<br><br>`onchain` 链上充值或普通提币<br><br>`internal` 内部转账<br><br>`fast` 快速充提（链上 + 内部地址） |
| data.list[].amount | string |  | 充提数量 |
| data.list[].status | string |  | 状态<br><br>`pending` 确认中<br><br>`fail` 失败<br><br>`success` 成功 |
| data.list[].ts | string |  | 充提记录更新时间<br><br>Unix毫秒时间戳 |
| data.endId | string |  | 翻页游标 ID（取当前页最小记录 ID） |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1767151164765,
  "data": {
    "list": [
      {
        "uid": "12345678910",
        "txId": "1390096439417995264",
        "type": "withdrawal",
        "subType": "internal",
        "coin": "USDT",
        "amount": "10.000000000",
        "status": "fail",
        "ts": "1767150805032"
      }
    ],
    "endId": "1390096439417995264"
  }
}
```

## 获取经纪商子账户佣金记录

`GET /api/v3/broker/commission`

限频规则: 20次/秒/UID

仅用户类型为ND Broker的母账户才能调用该接口。

Operation ID: `brokerGetBrokerCommission`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| startTime | query | string |  | 查询开始时间<br><br>Unix毫秒时间戳。若开始与结束时间均不传，默认查询时间为昨日00:00-23:59(UTC+0)。单次查询的startTime与endTime间隔不超过30天 |
| endTime | query | string |  | 查询结束时间<br><br>Unix毫秒时间戳。若开始与结束时间均不传，默认查询时间为昨日00:00-23:59(UTC+0)。单次查询的startTime与endTime间隔不超过30天 |
| pageSize | query | string |  | 每页条目数<br><br>默认值为100，最大值为1000 |
| pageNo | query | string |  | 分页页码<br><br>默认值为1 |
| bizType | query | string |  | 业务类型<br><br>`spot` 现货<br><br>`futures` 合约<br><br>如不填，则返回全部类型佣金信息 |
| subBizType | query | string |  | 业务子类型<br><br>`spot_trade` 现货交易<br><br>`spot_margin` 现货杠杆<br><br>`usdt_futures` U本位合约<br><br>`usdc_futures` USDC合约<br><br>`coin_futures` 币本位合约<br><br>当`bizType=spot`时，该参数可填`spot_trade`及`spot_margin`；当`bizType=futures`时，该参数可填`usdt_futures`,`usdc_futures`及`coin_futures` |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].uid | string |  | 用户ID |
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
  "requestTime": 1767677788472,
  "data": [
    {
      "uid": "1359901376",
      "coin": "BTC",
      "symbol": "BTC/USDT",
      "dealtAmount": "84.346065",
      "totalFee": "0.0000005",
      "deductedFee": "0",
      "paidFee": "0.0000005",
      "markUpFee": "0",
      "totalCommission": "0.00000002"
    }
  ]
}
```

## 获取经纪商子账户API Key

`GET /api/v3/broker/query-sub-apikey`

限频: 20次/秒/UID

仅用户类型为ND Broker的母账户才能调用该接口。

Operation ID: `brokerGetSubaccountApikey`

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
| data.label | string |  | 备注 |
| data.apiKey | string |  | API Key |
| data.secretKey | string |  | 私钥 |
| data.permType | string |  | 权限类型<br><br>`read_write` 读写权限<br><br>`read_only` 只读权限 |
| data.permList | string[] |  | 权限<br><br>`uta_trade` UTA交易<br><br>`uta_mgt` UTA管理<br><br>`withdraw` 提币(permType需要为read_write类型) |
| data.ipList | string[] |  | IP白名单 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1767151739925,
  "data": {
    "subUid": "12345678910",
    "label": "338040211757111_test01",
    "apiKey": "bg_12345678910b",
    "secretKey": "12345678910xxx",
    "permType": "read_write",
    "permList": [
      "uta_mgt",
      "uta_trade",
      "withdraw"
    ],
    "ipList": null
  }
}
```

## 获取经纪商子账户列表

`GET /api/v3/broker/sub-list`

限频规则: 20次/秒/UID

仅用户类型为ND Broker的母账户才能调用该接口。

Operation ID: `brokerGetSubaccountList`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| limit | query | string |  | 每页条目数<br><br>默认10 最大100 |
| cursor | query | string |  | 游标ID<br><br>用于分页。首次调用不传。后续调用传入上次查询返回的最后一个subUid |
| status | query | string |  | 账户状态<br><br>`normal` 正常<br><br>`freeze` 冻结 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.subList | object[] |  | 子账户列表 |
| data.subList[].subUid | string |  | 子账户uid |
| data.subList[].subaccountName | string |  | 子账户用户名 |
| data.subList[].subaccountEmail | string |  | 子账户邮箱 |
| data.subList[].status | string |  | 子账户状态<br><br>`normal` 正常<br><br>`freeze` 冻结 |
| data.subList[].permList | string[] |  | 权限列表<br><br>`withdraw` 提币<br><br>`transfer` 划转<br><br>`spot_trade` 现货交易<br><br>`contract_trade` 合约交易<br><br>`margin_trade` 杠杆交易<br><br>`deposit` 充值权限 |
| data.subList[].label | string |  | 备注 |
| data.subList[].cTime | string |  | 账户创建时间<br><br>Unix毫秒时间戳 |
| data.subList[].uTime | string |  | 账户更新时间<br><br>Unix毫秒时间戳 |
| data.subList[].language | string |  | 子账户语言<br><br>`en_US`<br><br>`zh_CN`<br><br>`ja_JP`<br><br>`vi_VN`<br><br>`zh_TW`<br><br>`ru_RU`<br><br>`es_ES`<br><br>`tr_TR`<br><br>`fr_FR`<br><br>`de_DE`<br><br>`pt_PT`<br><br>`th_TH` |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1767149918448,
  "data": {
    "subList": [
      {
        "subUid": "12345678910",
        "subaccountName": "hun****@broker_8383826362",
        "subaccountEmail": null,
        "status": "normal",
        "permList": [
          "read",
          "uta_spot_trade",
          "uta_margin_trade",
          "uta_contract_trade",
          "transfer",
          "withdraw",
          "deposit"
        ],
        "label": "hunterusersub21523121",
        "language": "zh_CN",
        "cTime": "1767148977593",
        "uTime": "1767148977593"
      }
    ]
  }
}
```

## 修改经纪商子账户API Key

`POST /api/v3/broker/modify-sub-apikey`

限频: 20次/秒/UID

仅用户类型为ND Broker的母账户才能调用该接口。

Operation ID: `brokerModifySubaccountApikey`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| subUid | string | 是 | 子账户uid |
| passphrase | string | 是 | Passphrase<br><br>passphrase是调用 API 接口的必要参数，如果遗失请重新创建API key |
| apiKey | string | 是 | API Key |
| label | string |  | 备注 |
| ipList | string[] |  | IP白名单<br><br>最多传入30个 |
| permType | string |  | 权限类型<br><br>`read_write` 读写权限<br><br>`read_only` 只读权限 |
| permList | string[] |  | 权限<br><br>`uta_trade` UTA交易<br><br>`uta_mgt` UTA管理<br><br>`withdraw` 提币(permType需要为read_write类型) |

```json
{
  "subUid": "12345678910",
  "passphrase": "12345678",
  "apiKey": "bg_12345678910",
  "label": "338040211757111_test01",
  "permType": "read_write",
  "permList": [
    "uta_trade",
    "uta_mgt",
    "withdraw"
  ]
}
```

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.subUid | string |  | 子账户uid |
| data.label | string |  | 备注 |
| data.apiKey | string |  | API Key |
| data.permType | string |  | 权限类型<br><br>`read_write` 读写权限<br><br>`read_only` 只读权限 |
| data.permList | string[] |  | 权限<br><br>`uta_trade` UTA交易<br><br>`uta_mgt` UTA管理<br><br>`withdraw` 提币(permType需要为read_write类型) |
| data.ipList | string[] |  | IP白名单 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1767151778823,
  "data": {
    "subUid": "12345678910",
    "label": "3380407571_test02update",
    "apiKey": "bg_12345678910",
    "permType": "read_write",
    "permList": [
      "uta_mgt",
      "uta_trade",
      "withdraw"
    ],
    "ipList": [
      "1.3.1.2"
    ]
  }
}
```

## 修改经纪商子账户

`POST /api/v3/broker/modify-sub`

限频: 20次/秒/UID

仅用户类型为ND Broker的母账户才能调用该接口。

Operation ID: `brokerModifySubaccount`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| subUid | string | 是 | 子账户uid |
| status | string |  | 子账户状态<br><br>`normal` 正常<br><br>`freeze` 冻结 |
| permList | string |  | 权限列表<br><br>`withdraw` 提币<br><br>`transfer` 划转<br><br>`spot_trade` 现货交易<br><br>`contract_trade` 合约交易<br><br>`margin_trade` 杠杆交易<br><br>`deposit` 充值权限 |

```json
{
  "subUid": "1234567891",
  "status": "freeze"
}
```

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.subUid | string |  | 子账户uid |
| data.status | string |  | 子账户状态<br><br>`normal` 正常<br><br>`freeze` 冻结 |
| data.subaccountName | string |  | 子账户名称 |
| data.label | string |  | 备注 |
| data.permList | string[] |  | 权限列表<br><br>`withdraw` 提币<br><br>`transfer` 划转<br><br>`spot_trade` 现货交易<br><br>`contract_trade` 合约交易<br><br>`margin_trade` 杠杆交易<br><br>`deposit` 充值权限 |
| data.cTime | string |  | 账户创建时间<br><br>Unix毫秒时间戳 |
| data.uTime | string |  | 账户更新时间<br><br>Unix毫秒时间戳 |
| data.language | string |  | 子账户语言<br><br>`en_US`<br><br>`zh_CN`<br><br>`ja_JP`<br><br>`vi_VN`<br><br>`zh_TW`<br><br>`ru_RU`<br><br>`es_ES`<br><br>`tr_TR`<br><br>`fr_FR`<br><br>`de_DE`<br><br>`pt_PT`<br><br>`th_TH` |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1767150632929,
  "data": {
    "subUid": "12345678910",
    "subaccountName": "hun****@broker",
    "status": "freeze",
    "permList": [
      "uta_spot_trade",
      "transfer",
      "deposit"
    ],
    "label": "hunterusersub123121",
    "cTime": "1766476082509",
    "uTime": "1766476102463"
  }
}
```

## 获取经纪商子账户充值地址

`POST /api/v3/broker/sub-deposit-address`

限频: 20次/秒/UID

仅用户类型为ND Broker的母账户才能调用该接口。

Operation ID: `brokerSubaccountDepositAddress`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| subUid | string | 是 | 子账户uid |
| coin | string | 是 | 币种 |
| chain | string |  | 链名称<br><br>如果不填该参数，则默认为币种的主链 |

```json
{
  "subUid": "12345678910",
  "chain": "ERC20",
  "coin": "USDT"
}
```

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.subUid | string |  | 子账户uid |
| data.coin | string |  | 币种 |
| data.chain | string |  | 链名称 |
| data.address | string |  | 充值地址 |
| data.tag | string |  | 标识<br><br>部分链生效，如EOS的memo，TON的comment |
| data.url | string |  | 自定义订单ID |
| data.cTime | string |  | 创建时间 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1767150821166,
  "data": {
    "subUid": "12345678910",
    "coin": "USDT",
    "address": "0xe4de63ebbf937385c17e7332557fe5c3337648ca",
    "chain": "ERC20",
    "tag": null,
    "url": "https://sepolia.etherscan.io/tx/",
    "cTime": "1765987200000"
  }
}
```

## 经纪商子账户提币

`POST /api/v3/broker/sub-withdrawal`

限频: 20次/秒/UID

仅用户类型为ND Broker的母账户才能调用该接口。

Broker子账户提币接口存在限制，目前仅支持以下币种：

BTC, ETH, USDT, USDC, TRX, XRP, LTC, SOL, BNB, FTM, DOGE, ADA, SHIB, UNI, SEI, SUI, POL, FIL, LINK, GRAM, ARB, OP, DOT, AVAX, BGB

Operation ID: `brokerSubaccountWithdrawal`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| subUid | string | 是 | 子账户uid |
| coin | string | 是 | 币种 |
| dest | string | 是 | 提币方式<br><br>`on_chain` 链上提币<br><br>`internal_transfer` 内部转账 |
| chain | string |  | 链名称<br><br>如果不填该参数，则默认为币种的主链 |
| address | string | 是 | 提币地址<br><br>当选择链上提币时，填链上地址；当选择内部转账时，填uid |
| amount | string | 是 | 提币数量 |
| tag | string |  | 标识<br><br>EOS的memo，GRAM的comment都使用该字段填入 |
| clientOid | string |  | 自定义订单ID |

```json
{
  "subUid": "12345678910",
  "dest": "internal_transfer",
  "coin": "USDT",
  "address": "123456789",
  "amount": "10",
  "clientOid": "91500512549_1765977438100"
}
```

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.orderId | string |  | 订单ID |
| data.clientOid | string |  | 自定义订单ID |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1767150755184,
  "data": {
    "orderId": "1390096439417995264",
    "clientOid": "91500512549_1765977438100"
  }
}
```

## 子账户绑定邮箱

`POST /api/v3/broker/modify-subaccount-email`

限频: 10次/秒/UID

独立经纪商母账户修改子账户绑定的接收邮件的邮箱

Operation ID: `brokerModifySubaccountEmail`

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

## 获取子账户邮箱

`GET /api/v3/broker/subaccount-email`

限频: 10次/秒/UID

独立经纪商母账户获取子账户绑定的接收邮件的邮箱

Operation ID: `brokerGetSubaccountEmail`

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
    "subaccountName": "<EMAIL_ADDRESS>",
    "subaccountEmail": "<EMAIL_ADDRESS>",
    "cTime": "1692008679000",
    "uTime": "1695784930000"
  }
}
```

## 获取经纪商子账户交易记录

`GET /api/v3/broker/trade-volume`

限频: 5次/秒/UID

请联系对接BD或者RM申请接入权限

Operation ID: `brokerGetTradeVolume`

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

## 获取经纪商佣金数据

`GET /api/v3/broker/total-commission`

限速规则 20次/1s (UID)

数据存储：365天

历史数据回溯：2025/6/1

数据维度：天维度

数据更新维度：天维度，当天更新前一天数据

时区：UTC+8

startTime和endTime应该被同时设置或者同时不设置

该接口支持获取365天内数据（最早提供2025/6/1起的数据）

如果请求中不设置startTime和endTime将会默认返回昨日(00:00-23:59 UTC+8)的信息

数据更新频率：T+1 (UTC +8)

Operation ID: `brokerGetTotalCommission`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| startTime | query | string |  | 开始时间戳，毫秒，开始与结束时间均为空默认时间为昨日00:00-23:59(UTC+8)，startTime与endTime只能同时填或不填，超出180天报错 |
| endTime | query | string |  | 结束时间戳，毫秒，开始与结束时间均为空默认时间为昨日00:00-23:59(UTC+8)，startTime与endTime只能同时填或不填，超出180天报错 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].date | string |  | 返佣日期 |
| data[].totalTradingVolume | string |  | 经纪商当日交易量 |
| data[].totalActiveTraders | string |  | 经纪商当日交易人数 |
| data[].totalCommission | string |  | 经纪商总返佣（USDT） |
| data[].spot | object |  | 现货数据 |
| data[].spot.spotTradingVolume | string |  | 现货交易量（USDT） |
| data[].spot.spotTradingFee | string |  | 现货实际收取手续费（USDT） |
| data[].spot.spotPureTradingFee | string |  | 现货净手续费（USDT）（扣除负maker等计算逻辑，经纪商获取返佣的计算基数） |
| data[].spot.spotCommission | string |  | 现货返佣（USDT） |
| data[].futures | object |  | 合约数据 |
| data[].futures.futuresTradingVolume | string |  | 合约交易量（USDT） |
| data[].futures.futuresTradingFee | string |  | 合约实际收取手续费（USDT） |
| data[].futures.futuresPureTradingFee | string |  | 合约净手续费（USDT）（扣除负maker等计算逻辑，经纪商获取返佣的计算基数） |
| data[].futures.futuresCommission | string |  | 合约返佣（USDT） |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 17609760000000.0,
  "data": [
    {
      "date": "17609760000000",
      "totalTradingVolume": "24679.848225",
      "totalActiveTraders": "1",
      "totalCommission": "0",
      "spot": {
        "spotTradingVolume": "419.847925",
        "spotTradingFee": "0.34999881",
        "spotPureTradingFee": "0.34999881",
        "spotCommission": "0"
      },
      "futures": {
        "futuresTradingVolume": "24260.0003",
        "futuresTradingFee": "15.5999965399983",
        "futuresPureTradingFee": "15.5999965399983",
        "futuresCommission": "0"
      }
    }
  ]
}
```

## 获取经纪商订单返佣数据

`GET /api/v3/broker/order-commission`

限速规则 20次/1s (UID)

数据存储：30天

历史数据回溯：2025/9/1

数据维度：天维度

数据更新维度：天维度，当天更新前一天数据

时区：UTC+8

startTime和endTime应该被同时设置或者同时不设置

startTime和endTime支持的最大时间跨度为30天

该接口支持获取30天内数据

如果请求中不设置startTime和endTime将会默认返回昨日(00:00-23:59 UTC+8)的信息

该接口数据更新信息是T+1的

成交明细只展示broker channel id标记的成交明细信息

Operation ID: `brokerGetOrderCommission`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| startTime | query | string |  | 开始时间戳，毫秒，开始与结束时间均为空默认时间为昨日00:00-23:59(UTC+8)，startTime与endTime只能同时填或不填，超出180天报错 |
| endTime | query | string |  | 结束时间戳，毫秒，开始与结束时间均为空默认时间为昨日00:00-23:59(UTC+8)，startTime与endTime只能同时填或不填，超出180天报错 |
| limit | query | string |  | 分页限制 最大:500,默认: 500 |
| uid | query | string |  | 查询用户的uid |
| orderid | query | string |  | 订单id |
| idLessThan | query | string |  | 游标ID<br><br> 用于分页<br><br>首次不传。后续传参上次响应的endId进行翻页 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.commissionlist | object[] |  | 返佣列表 |
| data.commissionlist[].fillId | string |  | 成交ID |
| data.commissionlist[].orderId | string |  | 订单id |
| data.commissionlist[].ts | string |  | 成交时间 |
| data.commissionlist[].clientOid | string |  | 自定义订单ID |
| data.commissionlist[].bizType | string |  | 交易类型<br><br>`spot`现货<br><br>`futures`合约 |
| data.commissionlist[].subBizType | string |  | 子交易类型<br><br>`spot_trade`现货币币<br><br>`spot_margin`现货杠杆<br><br>`usdt_futures`U本位合约<br><br>`coin_futures`币本位合约<br><br>`usdc_futures`USDC合约 |
| data.commissionlist[].symbol | string |  | 交易对 |
| data.commissionlist[].volume | string |  | 交易金额<br><br>单位：USDT，精度不截断 |
| data.commissionlist[].fee | string |  | 总手续费<br><br>单位：USDT，精度不截断 |
| data.commissionlist[].pureFee | string |  | 净手续费<br><br>单位：USDT，精度不截断 |
| data.commissionlist[].rebateAmount | string |  | 经纪商佣金<br><br>单位：USDT，精度不截断 |
| data.endId | string |  | 游标ID |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695786824200,
  "data": {
    "commissionlist": [
      {
        "fillId": "121211212122",
        "orderId": "121211212122",
        "ts": "1689833233282",
        "clientOid": "121211212122",
        "bizType": "spot",
        "subBizType": "spot_trade",
        "symbol": "BTCUSDT",
        "volume": "1000",
        "fee": "1",
        "pureFee": "1",
        "rebateAmount": "0.5"
      }
    ],
    "endId": "12345"
  }
}
```

## 获取用户的经纪商返佣信息

`GET /api/v3/broker/rebate-info`

限速规则 20次/1s (UID)

数据存储：30天

实时的数据

Operation ID: `brokerGetRebateInfo`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| uid | query | string | 是 | 用户的uid |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.affiliationType | string |  | 返佣关系的情况<br><br>`affiliate`客户渠道<br><br>`official` 官网渠道 |
| data.userLevel | string |  | 用户等级用户等级<br><br>`VIP0`<br><br>`VIP1`<br><br>...<br><br>`VIP7`<br><br>`PRO1`<br><br>...<br><br>`PRO6` |
| data.clientSpotRebateRatio | string |  | 交易用户可获取现货返佣比例 |
| data.clientFuturesRebateRatio | string |  | 交易用户可获取合约返佣比例 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695786824200,
  "data": {
    "affiliationType": "affiliate",
    "userLevel": "VIP7",
    "clientSpotRebateRatio": "0.07",
    "clientFuturesRebateRatio": "0.08"
  }
}
```