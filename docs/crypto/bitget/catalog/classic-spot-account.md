---
exchange: bitget
source_url: https://www.bitget.com/docs/catalog/classic-spot-account
api_type: REST
updated_at: 2026-11-18 08:38:04.773060
---

# Classic Spot Account API

Spot account endpoints — assets, bills, deposit, withdrawal, transfer, and sub-account management.

版本: 1.0.0

## 服务地址

- `https://api.bitget.com`

## 接口列表

- `GET /api/v2/spot/account/info` — Get Account Information
- `GET /api/v2/spot/account/assets` — Get Account Assets
- `GET /api/v2/spot/account/bills` — Get Account Bills
- `GET /api/v2/spot/account/transferRecords` — Get Transfer Record
- `GET /api/v2/spot/account/sub-main-trans-record` — Get MainSub Transfer Record
- `GET /api/v2/spot/account/subaccount-assets` — Get Sub-accounts Assets
- `GET /api/v2/spot/account/upgrade-status` — Get Upgrade Status
- `POST /api/v2/spot/account/upgrade` — Upgrade Account
- `GET /api/v2/spot/account/deduct-info` — Get BGB Deduct Info
- `POST /api/v2/spot/account/switch-deduct` — Switch BGB Deduct
- `POST /api/v2/spot/wallet/subaccount-transfer` — Sub Transfer
- `POST /api/v2/spot/wallet/transfer` — Transfer
- `GET /api/v2/spot/wallet/transfer-coin-info` — GET Transferable Coin List
- `POST /api/v2/spot/wallet/modify-deposit-account` — Modify Deposit Account
- `GET /api/v2/spot/wallet/deposit-address` — Get Deposit Address
- `GET /api/v2/spot/wallet/subaccount-deposit-address` — Get SubAccount Deposit Address
- `GET /api/v2/spot/wallet/deposit-records` — Get Deposit Records
- `GET /api/v2/spot/wallet/subaccount-deposit-records` — Get SubAccount Deposit Records
- `GET /api/v2/spot/wallet/withdrawal-records` — Get Withdrawal Records
- `POST /api/v2/spot/wallet/withdrawal` — Withdraw
- `POST /api/v2/spot/wallet/cancel-withdrawal` — Cancel Withdrawal

## Get Account Information

`GET /api/v2/spot/account/info`

Frequency limit: 1 time/1s (User ID)

Get account information

Operation ID: `classicSpotAccountGetAccountInfo`

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.userId | string |  | User ID |
| data.inviterId | string |  | Inviter's user ID |
| data.channelCode | string |  | Affiliate referral code |
| data.channel | string |  | Affiliate |
| data.ips | string |  | IP whitelist |
| data.authorities | string[] |  | Permissions. Read only: coor: futures orders / cpor: futures holdings / stor: spot trade / smor: margin trade / ttor: copy trading / wtor: wallet transfer / taxr: taxation / chor: subaccount / p2pr: P2P query. Read and Write: coow: futures orders / cpow: futures holdings / stow: spot trade / smow: margin trade / ttow: copy trading / wtow: wallet transfer / wwow: wallet withdrawl / chow: subaccount manage / p2p: P2P / pllw: Pledge Loan Write / pllr: Pledge Loan Read / taxw: Tax Read and Write |
| data.parentId | integer |  | Main account user ID |
| data.traderType | string |  | trader: Is trader, not_trader: not trader |
| data.regisTime | string |  | Register time |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695808949356,
  "data": {
    "userId": "**********",
    "inviterId": "**********",
    "ips": "127.0.0.1",
    "authorities": [
      "cpor",
      "coor"
    ],
    "parentId": 1,
    "traderType": "trader",
    "channelCode": "XXX",
    "channel": "YYY",
    "regisTime": "1246566789345"
  }
}
```

## Get Account Assets

`GET /api/v2/spot/account/assets`

Frequency limit: 10 times/1s (User ID)

Get Account Assets

Operation ID: `classicSpotAccountGetAccountAssets`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| coin | query | string |  | Token name, e.g. USDT. This field is used for querying the positions of a single coin. |
| assetType | query | string |  | Asset type. `hold_only`: Position coin / `all`: All coins. This field is used for querying the positions of multiple coins. The default value is `hold_only`. When only `assetType` is entered without coin, results of all eligible coins are returned. When both coin and `assetType` are entered, coin has higher priority. |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| message | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].coin | string |  | Token name |
| data[].available | string |  | Available assets |
| data[].frozen | string |  | Amount of frozen assets. Usually frozen when the limit order is placed or join the Launchpad |
| data[].locked | string |  | Amount of locked assets. Locked assets required to become a fiat merchants. |
| data[].limitAvailable | string |  | Restricted availability. For spot copy trading |
| data[].uTime | string |  | Update time(ms) |

```json
{
  "code": "00000",
  "message": "success",
  "requestTime": 1695808949356,
  "data": [
    {
      "coin": "usdt",
      "available": "0",
      "frozen": "0",
      "locked": "0",
      "limitAvailable": "0",
      "uTime": "1622697148"
    }
  ]
}
```

## Get Account Bills

`GET /api/v2/spot/account/bills`

Frequency limit: 10 times/1s (User ID)

Get Account Bills

Operation ID: `classicSpotAccountGetAccountBills`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| coin | query | string |  | Token name, e.g. USDT |
| groupType | query | string |  | Billing type: deposit Deposit / withdraw Withdraw / transaction Transaction / transfer Transfer / loan Pledge loan / financial Wealth management / fait Fiat currency / convert Instant swap / c2c C2C token trading / pre_c2c Pre-market trading / on_chain On-chain transaction / strategy Trading strategy / other Other |
| businessType | query | string |  | Business type: DEPOSIT: Deposit / WITHDRAW: Withdraw / BUY: Buy / SELL: Sell / DEDUCTION_HANDLING_FEE: Deduction of spot trading transaction fee / TRANSFER_IN: Transfer-in / TRANSFER_OUT: Transfer-out / REBATE_REWARDS: Rebate / AIRDROP_REWARDS: Airdrop rewards / USDT_CONTRACT_REWARDS: USDT futures promotion rewards / MIX_CONTRACT_REWARDS: Mix contract promotion rewards / SYSTEM_LOCK: System lock-up / USER_LOCK: User lock-up / STRATEGY_TRANSFER_IN: Strategy Trading Close Position |
| startTime | query | string |  | The start time of the billing history, i.e., getting the billing history after that timestamp. Unix millisecond timestamp, e.g. 1690196141868 |
| endTime | query | string |  | The end time of the billing history, i.e., getting the billing history before that timestamp. Unix millisecond timestamp, e.g. 1690196141868. The interval between startTime and endTime must not exceed 90 days. |
| limit | query | string |  | Number of results returned. Default: 100, maximum 500. |
| idLessThan | query | string |  | Requests the content on the page before this ID (older data), the value input should be the billId of the corresponding interface. |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| message | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].billId | string |  | Billing ID |
| data[].bizOrderId | string |  | Business order ID |
| data[].coin | string |  | Token name |
| data[].groupType | string |  | Billing type |
| data[].businessType | string |  | Business type of billing |
| data[].size | string |  | Quantity |
| data[].balance | string |  | The assets after transfer |
| data[].fees | string |  | Transaction fees |
| data[].cTime | string |  | Creation time |

```json
{
  "code": "00000",
  "message": "success",
  "requestTime": 1695808949356,
  "data": [
    {
      "billId": "14314844815812356565",
      "bizOrderId": "1431481916612435678",
      "coin": "BGB",
      "groupType": "financial",
      "businessType": "BATCH_INTEREST_USER_IN",
      "size": "0.000012550000",
      "balance": "0.00178210",
      "fees": "0.00000000",
      "cTime": "1777018415280"
    }
  ]
}
```

## Get Transfer Record

`GET /api/v2/spot/account/transferRecords`

Frequency limit: 20 times/1s (User ID)

Get transfer record

Operation ID: `classicSpotAccountGetAccountTransferRecords`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| coin | query | string | 是 | Token name |
| fromType | query | string |  | Account type: spot: Spot account / p2p: P2P/funding account / coin_futures: Coin-M futures account / usdt_futures: USDT-M futures account / usdc_futures: USDC-M futures account / crossed_margin: Cross margin account / isolated_margin: Isolated margin account |
| startTime | query | string |  | The start time of the billing history, i.e., getting the billing history after that timestamp. Unix millisecond timestamp, e.g. 1690196141868 |
| endTime | query | string |  | The end time of the billing history, i.e., getting the billing history before that timestamp. Unix millisecond timestamp, e.g. 1690196141868. The interval between startTime and endTime must not exceed 90 days. |
| clientOid | query | string |  | Order ID customized by user |
| pageNum | query | string |  | (Deprecated) Requests the content on the page. default:1, max:1000 |
| limit | query | string |  | Number of results returned: Default: 100, maximum 500 |
| idLessThan | query | string |  | Requests the content on the page before this ID (older data), the value input should be the transferId of the corresponding interface. |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].coin | string |  | Token name |
| data[].status | string |  | Status of transfer. Successful: Successful / Failed: Failed / Processing: Processing |
| data[].toType | string |  | Recipient account type: spot / p2p / coin_futures / usdt_futures / usdc_futures / crossed_margin / isolated_margin |
| data[].toSymbol | string |  | Trading pair for the recipient account. Returned when the recipient account is isolated_margin |
| data[].fromType | string |  | Sender account type (same enum as toType) |
| data[].fromSymbol | string |  | Trading pair for the sending account. Return when the sending account is isolated_margin |
| data[].size | string |  | Quantity |
| data[].ts | string |  | Transfer time, Unix millisecond timestamp, e.g. 1690196141868 |
| data[].clientOid | string |  | Order ID customized by user |
| data[].transferId | string |  | Transfer order ID |

```json
{
  "code": "00000",
  "data": [
    {
      "coin": "btc",
      "status": "Successful",
      "toType": "usdt_futures",
      "toSymbol": "",
      "fromType": "spot",
      "fromSymbol": "BTC/USD",
      "size": "1000.00000000",
      "ts": "1631070374488",
      "clientOid": "1",
      "transferId": "1"
    }
  ],
  "msg": "success",
  "requestTime": 1631608142260
}
```

## Get MainSub Transfer Record

`GET /api/v2/spot/account/sub-main-trans-record`

Rate limit: 20 req/sec/UID

Get transfer record

Operation ID: `classicSpotAccountGetSubaccountTransferRecords`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| coin | query | string |  | Token name |
| role | query | string |  | Transfer out type(default：initiator). `initiator` initiator / `receiver` receiver |
| subUid | query | string |  | Sub-account UID. `subUid` is not allowed to be passed in when a sub-account makes a call. When a main account makes a call, if `subUid` is not passed in, it will query the transfer records where the main account is the initiator. |
| startTime | query | string |  | The start time of the billing history, i.e., getting the billing history after that timestamp. Unix millisecond timestamp, e.g. 1690196141868 |
| endTime | query | string |  | The end time of the billing history, i.e., getting the billing history before that timestamp. Unix millisecond timestamp, e.g. 1690196141868. The interval between startTime and endTime must not exceed 90 days. |
| clientOid | query | string |  | Order ID customized by user |
| limit | query | string |  | Number of results returned: Default: 100, maximum 100 |
| idLessThan | query | string |  | Requests the content on the page before this ID (older data), the value input should be the transferId of the corresponding interface. |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].coin | string |  | Token name |
| data[].status | string |  | Status of transfer. Successful: Successful / Failed: Failed / Processing: Processing |
| data[].toType | string |  | Recipient account type. spot: Spot account / p2p: P2P account / coin_futures: Coin-M futures account / usdt_futures: USDT-M futures account / usdc_futures: USDC-M futures account / crossed_margin: Cross margin account / isolated_margin: Isolated margin account |
| data[].fromType | string |  | Sender account type (same enum as toType) |
| data[].size | string |  | Quantity |
| data[].ts | string |  | Transfer time, Unix millisecond timestamp, e.g. 1690196141868 |
| data[].clientOid | string |  | Order ID customized by user |
| data[].transferId | string |  | Transfer order ID |
| data[].newTransferId | string |  | Transfer order ID. It is the same as the transferId in the main-sub account transfer response. |
| data[].fromUserId | string |  | the user ID who initiate the transfer ID |
| data[].toUserId | string |  | The user ID who receive the transfer |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1700556280430,
  "data": [
    {
      "coin": "USDT",
      "status": "Successful",
      "toType": "usdt_futures",
      "fromType": "spot",
      "size": "1020.00000000",
      "ts": "1691476360467",
      "clientOid": "xxxx",
      "transferId": "xxxx",
      "newTransferId": "xxxx",
      "fromUserId": "xxxx",
      "toUserId": "xxxx"
    }
  ]
}
```

## Get Sub-accounts Assets

`GET /api/v2/spot/account/subaccount-assets`

Frequency limit: 10 times/1s (User ID)

Get Sub-accounts Assets(only return the sub-accounts which assets > 0). ND Brokers are not allowed to call this endpoint.

Operation ID: `classicSpotAccountGetSubaccountAssets`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| idLessThan | query | string |  | Cursor ID. Pagination cursor. Do not pass it in the first request. For subsequent requests, pass the last ID returned previously. |
| limit | query | string |  | The number of sub-accounts returned per page. The default value is 10, and the maximum value is 50. |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| message | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].id | string |  | Cursor ID |
| data[].userId | string |  | User ID |
| data[].assetsList | object[] |  | List of spot assets |
| data[].assetsList[].coin | string |  | Token name |
| data[].assetsList[].available | string |  | Available assets |
| data[].assetsList[].limitAvailable | string |  | Restricted availability. For spot copy trading |
| data[].assetsList[].frozen | string |  | Assets frozen |
| data[].assetsList[].locked | string |  | Assets locked |
| data[].assetsList[].uTime | string |  | update time, Unix, ms |

```json
{
  "code": "00000",
  "message": "success",
  "requestTime": 1695808949356,
  "data": [
    {
      "id": "1111",
      "userId": "1234567890",
      "assetsList": [
        {
          "coin": "BTC",
          "available": "1.1",
          "limitAvailable": "12.1",
          "frozen": "0",
          "locked": "1.1",
          "uTime": "1337654897651"
        }
      ]
    },
    {
      "id": "2222",
      "userId": "1234567890",
      "assetsList": [
        {
          "coin": "ETH",
          "available": "12.1",
          "limitAvailable": "12.1",
          "frozen": "0",
          "locked": "1.1",
          "uTime": "1337654897651"
        }
      ]
    }
  ]
}
```

## Get Upgrade Status

`GET /api/v2/spot/account/upgrade-status`

Rate Limit: 1 req/sec/UID

No account type restrictions; both parent and sub-accounts are supported.

Operation ID: `classicSpotAccountGetUpgradeStatus`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| subUid | query | string |  | Sub-account User ID |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.status | string |  | Upgrade Status. `process` Processing / `success` Success / `fail` Failed |
| data.reason | string |  | Failure Reason. Only returned when the `status = fail` |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1746687063471,
  "data": {
    "status": "fail",
    "reason": "upgrade_disabled"
  }
}
```

## Upgrade Account

`POST /api/v2/spot/account/upgrade`

Rate Limit: 1 req/sec/UID

1. No account type restrictions; both parent and sub-accounts are supported.

2. This interface is only used for upgrading to the unified account mode.

3. Please note that as the account upgrade process takes approximately 1 minute, the successful response you receive only indicates that the request has been received, and does not mean that the account has been successfully upgraded to a unified account.

4. Please use the query upgrade status interface to confirm whether the account upgrade is successful.

Operation ID: `classicSpotAccountUpgradeAccount`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| subUid | string |  | Sub-account User ID |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data |  |  |  |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1728625799912,
  "data": null
}
```

## Get BGB Deduct Info

`GET /api/v2/spot/account/deduct-info`

Rate limit: 5 req/sec/UID

Operation ID: `classicSpotAccountGetDeductInfo`

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.deduct | string |  | on / off |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695808949356,
  "data": {
    "deduct": "on"
  }
}
```

## Switch BGB Deduct

`POST /api/v2/spot/account/switch-deduct`

Rate Limit: 1 req/sec/UID

Operation ID: `classicSpotAccountSwitchDeduct`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| deduct | string | 是 | on/off |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | boolean |  |  |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1683875302853,
  "data": true
}
```

## Sub Transfer

`POST /api/v2/spot/wallet/subaccount-transfer`

Rate limit: 20 req/sec/UID

The types of transfers supported by this interface include: parent account transfer to sub-accounts, sub-accounts transfer to parent account, sub-accounts transfer to sub-accounts (same parent account), and sub-account inner accounts transfer, e.g. spot to futures (the `fromUserId` & `toUserId` should be same). Only the parent account API Key can use this endpoint, and the API Key must bind IP.

Operation ID: `classicSpotAccountSubTransfer`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| fromType | string | 是 | Account type. `spot`: Spot account / `p2p`: P2P/Funding account / `coin_futures`: Coin-M futures account / `usdt_futures`: USDT-M futures account / `usdc_futures`: USDC-M futures account / `crossed_margin`: Cross margin account / `isolated_margin`: Isolated margin account |
| toType | string | 是 | Account type (same enum as fromType) |
| amount | string | 是 | Amount to transfer |
| coin | string | 是 | Currency of transfer |
| symbol | string |  | Symbol name(Required in Isolated margin (spot) transferring) |
| clientOid | string |  | Custom order ID |
| fromUserId | string | 是 | Outgoing Account UID |
| toUserId | string | 是 | Incoming Account UID |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.transferId | string |  | Transfer ID |
| data.clientOid | string |  | Custom order ID |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1683875302853,
  "data": {
    "transferId": "123456",
    "clientOid": "x123"
  }
}
```

## Transfer

`POST /api/v2/spot/wallet/transfer`

Rate limit: 10 requests/second/UID

Transfer assets between different `productType` accounts

Operation ID: `classicSpotAccountWalletTransfer`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| fromType | string | 是 | Account type. `spot`: Spot account / `p2p`: P2P/funding account / `coin_futures`: Coin-M futures account / `usdt_futures`: USDT-M futures account / `usdc_futures`: USDC-M futures account / `crossed_margin`: Cross margin account / `isolated_margin`: Isolated margin account |
| toType | string | 是 | Account type (same enum as fromType) |
| amount | string | 是 | Amount to transfer |
| coin | string | 是 | Currency of transfer |
| symbol | string |  | Required when transferring to or from an account type that is a leveraged position-by-position account. |
| clientOid | string |  | Custom order ID. It's unique. If you set duplicate clientOid, it will return the result of existing clientOid transfer |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.transferId | string |  | Transfer ID |
| data.clientOid | string |  | Custom order ID |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1683875302853,
  "data": {
    "transferId": "123456",
    "clientOid": "x123"
  }
}
```

## GET Transferable Coin List

`GET /api/v2/spot/wallet/transfer-coin-info`

Frequency limit:10 times/1s (User ID)

Get transferable coin list

Operation ID: `classicSpotAccountGetTransferCoins`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| fromType | query | string | 是 | Account type. `spot`: Spot account / `p2p`: P2P account / `coin_futures`: Coin-M futures account / `usdt_futures`: USDT-M futures account / `usdc_futures`: USDC-M futures account / `crossed_margin`: Cross margin account / `isolated_margin`: Isolated margin account |
| toType | query | string | 是 | Account type (same enum as fromType) |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | string[] |  | transfer_in and transfer_out of accounts supports coins intersection. |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1683875302853,
  "data": [
    "BTC",
    "USDT",
    "ETH"
  ]
}
```

## Modify Deposit Account

`POST /api/v2/spot/wallet/modify-deposit-account`

Frequency limit:10 times/1s (User ID)

Modify the auto-transfer account type of deposit

Operation ID: `classicSpotAccountModifyDepositAccount`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| accountType | string | 是 | Account type. `spot`: Spot account / `funding`: funding account / `coin-futures`: Coin-M futures account / `usdt-futures`: USDT-M futures account / `usdc-futures`: USDC-M futures account |
| coin | string | 是 | Currency of transfer |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | string |  | success/fail |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1683875302853,
  "data": "success"
}
```

## Get Deposit Address

`GET /api/v2/spot/wallet/deposit-address`

Frequency limit: 10 times/1s (User ID)

Get Deposit Address

Operation ID: `classicSpotAccountGetDepositAddress`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| coin | query | string | 是 | Coin name, e.g. USDT. All coin names can be returned from Get Coin Info interface |
| chain | query | string |  | Chain name, e.g. trc20. You can get the chain names via Get Coin Info interface |
| size | query | string |  | Bitcoin Lightning Network withdrawal amount，limit：0.000001 - 0.001 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.address | string |  | Deposit address |
| data.chain | string |  | chain name |
| data.coin | string |  | Token name |
| data.tag | string |  | Tag |
| data.url | string |  | blockchain address |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1683875302853,
  "data": {
    "address": "xxx",
    "chain": "BTC-Bitcoin",
    "coin": "BTC",
    "tag": "",
    "url": "https://btc.com/xxx"
  }
}
```

## Get SubAccount Deposit Address

`GET /api/v2/spot/wallet/subaccount-deposit-address`

Rate limit: 10 req/sec/UID

Get Sub-account Deposit Address(Please ensure that queried sub-account has deposit permission enabled)

Operation ID: `classicSpotAccountGetSubaccountDepositAddress`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| subUid | query | string | 是 | Sub Account Uid. You can get the sub-account list via Get Virtual Subaccounts interface |
| coin | query | string | 是 | Coin name, e.g. USDT. All coin names can be returned from Get Coin Info interface |
| chain | query | string |  | Chain name, e.g. trc20. You can get the chain names via Get Coin Info interface |
| size | query | string |  | Bitcoin Lightning Network withdrawal amount，limit：0.000001 - 0.001 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.address | string |  | Deposit address |
| data.chain | string |  | chain name |
| data.coin | string |  | Token name |
| data.tag | string |  | Tag |
| data.url | string |  | blockchain address |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1683875302853,
  "data": {
    "address": "xxx",
    "chain": "BTC-Bitcoin",
    "coin": "BTC",
    "tag": "",
    "url": "https://btc.com/xxx"
  }
}
```

## Get Deposit Records

`GET /api/v2/spot/wallet/deposit-records`

Frequency limit:10 times/1s (UID)

Get Deposit Records

Operation ID: `classicSpotAccountGetDepositRecord`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| coin | query | string |  | Coin name, e.g. USDT |
| orderId | query | string |  | The response orderId. When orderId is passed, this order is queried directly, ignoring other parameters. |
| startTime | query | string | 是 | The record start time for the query. Unix millisecond timestamp, e.g. 1690196141868 |
| endTime | query | string | 是 | The end time of the record for the query. Unix millisecond timestamp, e.g. 1690196141868 |
| idLessThan | query | string |  | Requests the content on the page before this ID (older data), the value input should be the orderId of the corresponding interface. |
| limit | query | string |  | Number of entries per page. The default value is 20 and the maximum value is 100 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].orderId | string |  | Order ID |
| data[].tradeId | string |  | TX ID. when `dest` is `on_chain`, it's the on chain hash value; if the `dest` is `internal_transfer`, it is the trade ID |
| data[].coin | string |  | Token name |
| data[].type | string |  | Type. Fixed value: `deposit` |
| data[].size | string |  | Quantity |
| data[].status | string |  | Withdrawal status. `pending`: pending confirmation / `fail`: failed / `success`: successed |
| data[].fromAddress | string |  | Deposit Initiators. If `dest` is `on_chain`, it's the on chain address; If `dest` is `internal_transfer`, it would be the UID,email or the mobile |
| data[].toAddress | string |  | Coin Receiver. If `dest` is `on_chain`, it's the on chain address; If `dest` is `internal_transfer`, it would be the UID,email or the mobile |
| data[].chain | string |  | Deposit network. The chain name format is consistent with the `chain` field returned by `/api/v2/spot/public/coins`; if `dest` is `internal_transfer`, please ignore this parameter |
| data[].dest | string |  | Deposit Type. `on_chain`: the on chain deposit / `internal_transfer`: internal deposit |
| data[].cTime | string |  | Creation time, ms |
| data[].uTime | string |  | Edit time, ms |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1654507973411,
  "data": [
    {
      "orderId": "1",
      "tradeId": "1",
      "coin": "USDT",
      "type": "deposit",
      "size": "10.00000000",
      "status": "success",
      "toAddress": "0x51xxx",
      "dest": "on_chain",
      "chain": "erc20",
      "fromAddress": "0x52xxx",
      "cTime": "1653290769222",
      "uTime": "1653290769222"
    }
  ]
}
```

## Get SubAccount Deposit Records

`GET /api/v2/spot/wallet/subaccount-deposit-records`

Frequency limit:10 times/1s (UID)

Operation ID: `classicSpotAccountGetSubaccountDepositRecord`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| subUid | query | string | 是 | Sub Account Uid |
| coin | query | string |  | Coin name, e.g. USDT |
| startTime | query | string |  | The record start time for the query. Unix millisecond timestamp, e.g. 1690196141868 |
| endTime | query | string |  | The end time of the record for the query. Unix millisecond timestamp, e.g. 1690196141868 |
| idLessThan | query | string |  | Requests the content on the page before this ID (older data), the value input should be the orderId of the corresponding interface. |
| limit | query | string |  | Number of entries per page. The default value is 20 and the maximum value is 100 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].orderId | string |  | Order ID |
| data[].tradeId | string |  | TX ID. when `dest` is `on_chain`, it's the on chain hash value; if the `dest` is `internal_transfer`, it is the trade ID |
| data[].coin | string |  | Token name |
| data[].clientOid | string |  | Customized order ID |
| data[].size | string |  | Quantity |
| data[].status | string |  | Deposit status. `pending`：it's still in confirmation / `fail`：fail / `success`：success |
| data[].fromAddress | string |  | Deposit Initiators. If `dest` is `on_chain`, it's the on chain address; If `dest` is `internal_transfer`, it would be the UID,email or the mobile |
| data[].toAddress | string |  | Coin Receiver. If `dest` is `on_chain`, it's the on chain address; If `dest` is `internal_transfer`, it would be the UID,email or the mobile |
| data[].chain | string |  | Deposit network. if `dest` is `internal_transfer`, please ignore this parameter |
| data[].confirm | string |  | The number of confirmed blocks |
| data[].dest | string |  | Deposit Type. `on_chain`: the on chain deposit / `internal_transfer`: internal deposit |
| data[].tag | string |  | Tag |
| data[].fee | string |  | Transaction fee |
| data[].cTime | string |  | Creation time in ms |
| data[].uTime | string |  | Update time in ms |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1654507973411,
  "data": [
    {
      "orderId": "1",
      "tradeId": "1",
      "coin": "USDT",
      "dest": "internal_transfer",
      "clientOid": "123",
      "tag": "",
      "size": "10.00000000",
      "fee": "-1.00000000",
      "status": "success",
      "toAddress": "1",
      "fromAddress": "2",
      "confirm": "100",
      "chain": "erc20",
      "cTime": "1653290769222",
      "uTime": "1653290769222"
    }
  ]
}
```

## Get Withdrawal Records

`GET /api/v2/spot/wallet/withdrawal-records`

Frequency limit:10 times/1s (User ID)

Get Withdrawal Records

Operation ID: `classicSpotAccountGetWithdrawRecord`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| coin | query | string |  | Coin name, e.g. USDT |
| clientOid | query | string |  | Client customized ID. Mutually exclusive with orderId; when passed, queries this order directly and ignores other parameters. |
| startTime | query | string | 是 | The record start time for the query. Unix millisecond timestamp, e.g. 1690196141868 |
| endTime | query | string | 是 | The end time of the record for the query. Unix millisecond timestamp, e.g. 1690196141868 |
| idLessThan | query | string |  | Requests the content on the page before this ID (older data), the value input should be the orderId of the corresponding interface. |
| orderId | query | string |  | The response orderId. Mutually exclusive with clientOid; when passed, queries this order directly and ignores other parameters. |
| limit | query | string |  | Number of entries per page. The default value is 20 and the maximum value is 100 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].orderId | string |  | Order ID |
| data[].tradeId | string |  | TX ID. when `dest` is `on_chain`, it's the on chain hash value; if the `dest` is `internal_transfer`, it is the trade ID |
| data[].coin | string |  | Token name |
| data[].clientOid | string |  | Client customized ID |
| data[].type | string |  | Type. Fixed value: `withdraw` |
| data[].dest | string |  | Type of withdrawal. `on_chain`: withdrawal on chain / `internal_transfer`: internal transfer |
| data[].size | string |  | Quantity |
| data[].fee | string |  | Transaction Fee |
| data[].status | string |  | Withdrawal status. `pending`:Pending preliminary examination / `fail`:Failed / `success`:Successful |
| data[].fromAddress | string |  | Withdrawal Initiators. If `dest` is `on_chain`, it's the on chain address; If `dest` is `internal_transfer`, it would be the UID,email or the mobile |
| data[].toAddress | string |  | Coin receiver address. If `dest` is `on_chain`, it's the on chain address; If `dest` is `internal_transfer`, it would be the UID,email or the mobile |
| data[].chain | string |  | Withdrawal network. The chain name format is consistent with the `chain` field returned by `/api/v2/spot/public/coins`; if `dest` is `internal_transfer`, please ignore this parameter |
| data[].confirm | string |  | Number of confirmed blocks |
| data[].tag | string |  | Tag |
| data[].cTime | string |  | Creation time(ms) |
| data[].uTime | string |  | Update time(ms) |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1654507973411,
  "data": [
    {
      "orderId": "1",
      "tradeId": "1",
      "coin": "USDT",
      "dest": "internal_transfer",
      "clientOid": "123",
      "type": "withdraw",
      "tag": "",
      "size": "10.00000000",
      "fee": "-1.00000000",
      "status": "success",
      "toAddress": "1",
      "fromAddress": "2",
      "confirm": "100",
      "chain": "erc20",
      "cTime": "1653290769222",
      "uTime": "1653290769222"
    }
  ]
}
```

## Withdraw

`POST /api/v2/spot/wallet/withdrawal`

Rate limit:5 req/sec/UID

Coin withdrawals including on-chain withdrawals and internal transfers(the address needs to be added in the address book on web). KYC: For users in Korea, please note that if you withdraw funds to an account address on a Korean exchange and the amount is significant, the following 5 parameters can be referenced for completion: `memberCode`, `identityType`, `companyName`, `firstName`, and `lastName`.

Operation ID: `classicSpotAccountWalletWithdrawal`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| coin | string | 是 | Coin. All coin names can be returned from Get Coin Info interface |
| transferType | string | 是 | The type of withdrawal. `on_chain`: withdrawal on chain / `internal_transfer`: Transfer internally |
| address | string | 是 | Withdrawal address. when `transferType` is `on_chain`, it represents the chain address. When `transferType` is `internal_transfer`, according the `innerToType` parameter, please input the UID, email or the mobile |
| chain | string |  | Chain network e.g. erc20, trc20, etc. This field must be passed when the `transferType` is `on-chain`. You can get the chain names via Get Coin Info interface |
| innerToType | string |  | Type of address for internal withdrawals. `email`: Email address / `mobile`: Mobile phone number / `uid`: UID. The default value is uid |
| areaCode | string |  | This field is required when the value of the collection address type is `mobile` |
| tag | string |  | Address tag. Some special coins need this field, e.g. EOS |
| size | string | 是 | Withdrawal amount. Special instructions for Bitcoin Lightning Network withdrawals apply. The decimal places of withdrawal amount will be returned by the Get Coin Info interface |
| remark | string |  | Note |
| clientOid | string |  | Client Unique Customized Id |
| memberCode | string |  | Support: `bithumb` / `korbit` / `coinone` |
| identityType | string |  | Normal user：`user`  company：`company` |
| companyName | string |  | Company name |
| firstName | string |  | First Name |
| lastName | string |  | Last name |

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
  "requestTime": 1695808949356,
  "data": {
    "orderId": "123",
    "clientOid": "123"
  }
}
```

## Cancel Withdrawal

`POST /api/v2/spot/wallet/cancel-withdrawal`

Frequency limit:10 times/1s (User ID)

1. The user center can set the switch [Cancel Withdrawal], and there is a "regret period" of 1 minute to cancel the withdrawal.

2. There is manual review in the preliminary review status, and the withdrawal can be cancelled. Once the initial review is passed or uploaded to the chain, the withdrawal cannot be revoked.

3. Small-amount automatic currency withdrawals do not require manual review, and the withdrawal cannot be revoked.

Operation ID: `classicSpotAccountCancelWithdrawal`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| orderId | string | 是 | Withdraw orderId |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | string |  | success/fail |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1683875302853,
  "data": "success"
}
```


---

现货账户接口 —— 资产、账单、充值、提币、划转与子账户管理。

版本: 1.0.0

## 服务地址

- `https://api.bitget.com`

## 接口列表

- `GET /api/v2/spot/account/info` — 获取账户信息
- `GET /api/v2/spot/account/assets` — 获取账户现货资产
- `GET /api/v2/spot/account/bills` — 获取账单流水
- `GET /api/v2/spot/account/transferRecords` — 获取划转记录
- `GET /api/v2/spot/account/sub-main-trans-record` — 获取子母账户划转记录
- `GET /api/v2/spot/account/subaccount-assets` — 获取所有子账户现货资产
- `GET /api/v2/spot/account/upgrade-status` — 查询升级状态
- `POST /api/v2/spot/account/upgrade` — 账户升级
- `GET /api/v2/spot/account/deduct-info` — 当前是否开启BGB抵扣
- `POST /api/v2/spot/account/switch-deduct` — 开启BGB抵扣
- `POST /api/v2/spot/wallet/subaccount-transfer` — 子母账户划转
- `POST /api/v2/spot/wallet/transfer` — 划转
- `GET /api/v2/spot/wallet/transfer-coin-info` — 获取账户支持的划转币种
- `POST /api/v2/spot/wallet/modify-deposit-account` — 修改充值自动划转账户类型
- `GET /api/v2/spot/wallet/deposit-address` — 获取充币地址
- `GET /api/v2/spot/wallet/subaccount-deposit-address` — 获取子账户充币地址
- `GET /api/v2/spot/wallet/deposit-records` — 获取充币记录
- `GET /api/v2/spot/wallet/subaccount-deposit-records` — 获取子账户充值记录
- `GET /api/v2/spot/wallet/withdrawal-records` — 获取提币记录
- `POST /api/v2/spot/wallet/withdrawal` — 提币
- `POST /api/v2/spot/wallet/cancel-withdrawal` — 撤销提币

## 获取账户信息

`GET /api/v2/spot/account/info`

限速规则 1次/秒/UID

获取账户信息

Operation ID: `classicSpotAccountGetAccountInfo`

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.userId | string |  | 用户ID |
| data.inviterId | string |  | 邀请人UID |
| data.channelCode | string |  | 渠道邀请码 |
| data.channel | string |  | 渠道 |
| data.ips | string |  | IP白名单 |
| data.authorities | string[] |  | 权限。只读：coor 合约订单 / cpor 合约仓位 / stor 现货 / smor 杠杆 / ttor 跟单 / wtor 划转 / taxr 税务 / chor 子账户 / p2pr P2P。读写：coow 合约订单 / cpow 合约仓位 / stow 现货 / smow 杠杆 / ttow 跟单 / wtow 划转 / wwow 提币 / chow 子账户 / p2pw P2P / pllw 质押借贷写 / pllr 质押借贷读 / taxw 税务读写 |
| data.parentId | integer |  | 母账户UID |
| data.traderType | string |  | trader 是交易员, not_trader 不是交易员 |
| data.regisTime | string |  | 注册时间 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695808949356,
  "data": {
    "userId": "**********",
    "inviterId": "1",
    "ips": "127.0.0.1",
    "authorities": [
      "cpor",
      "coor"
    ],
    "parentId": 2,
    "traderType": "trader",
    "channelCode": "XYZ",
    "channel": "XXX",
    "regisTime": "1246566789345"
  }
}
```

## 获取账户现货资产

`GET /api/v2/spot/account/assets`

限速规则 10次/1s (UID)

获取账户币种资产

Operation ID: `classicSpotAccountGetAccountAssets`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| coin | query | string |  | 币种名称, 如USDT，该字段用于单币种持仓查询 |
| assetType | query | string |  | 资产类型。`hold_only`: 持仓币种 / `all`: 全部币种。该字段用于返回多币种持仓数据。默认值为`hold_only`。当不传coin，只传`assetType`时，则返回全部符合条件的币种。当同时传参coin及`assetType`时，coin优先级更高 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| message | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].coin | string |  | 币种名称 |
| data[].available | string |  | 可用资产 |
| data[].frozen | string |  | 冻结资产数量，通常是下单、参与Launchpad时冻结 |
| data[].locked | string |  | 锁仓资产数量，成为法币商家等的锁仓 |
| data[].limitAvailable | string |  | 受限可用，用于现货跟单场景 |
| data[].uTime | string |  | 更新时间(毫秒) |

```json
{
  "code": "00000",
  "message": "success",
  "requestTime": 1695808949356,
  "data": [
    {
      "coin": "usdt",
      "available": "0",
      "frozen": "0",
      "locked": "0",
      "limitAvailable": "0",
      "uTime": "1622697148"
    }
  ]
}
```

## 获取账单流水

`GET /api/v2/spot/account/bills`

限速规则 10次/1s (UID)

获取账单流水

Operation ID: `classicSpotAccountGetAccountBills`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| coin | query | string |  | 币种名称，如USDT |
| groupType | query | string |  | 账单类型：deposit 充值 / withdraw 提现 / transaction 交易 / transfer 转账 / loan 质押借贷 / financial 理财 / fait 法币 / convert 闪兑 / c2c 币币C2C / pre_c2c 盘前交易 / on_chain 链上交易 / strategy 策略 / other 其它 |
| businessType | query | string |  | 业务类型：DEPOSIT 充值 / WITHDRAW 提现 / BUY 买 / SELL 卖 / DEDUCTION_HANDLING_FEE 币币交易手续费抵扣 / TRANSFER_IN 转入 / TRANSFER_OUT 转出 / REBATE_REWARDS 返佣奖励 / AIRDROP_REWARDS 空投奖励 / USDT_CONTRACT_REWARDS USDT专业合约活动奖励 / MIX_CONTRACT_REWARDS 混合合约活动奖励 / SYSTEM_LOCK系统锁仓 / USER_LOCK 用户锁仓 / STRATEGY_TRANSFER_IN 策略交易平仓 |
| startTime | query | string |  | 账单流水的开始时间，即获取该时间戳以后的账单流水，Unix毫秒时间戳，例如1690196141868 |
| endTime | query | string |  | 账单流水的结束时间，即获取该时间戳以前的账单流水，Unix毫秒时间戳，例如1690196141868，startTime和endTime的时间间隔不超过90天 |
| limit | query | string |  | 返回结果的数量，默认100，最大 500 |
| idLessThan | query | string |  | 上一次查询返回的billId，返回ID小于该入参的数据 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| message | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].billId | string |  | 账单流水ID |
| data[].bizOrderId | string |  | 业务订单ID |
| data[].coin | string |  | 币种名称 |
| data[].groupType | string |  | 账单类型 |
| data[].businessType | string |  | 流水账单业务类型 |
| data[].size | string |  | 数量 |
| data[].balance | string |  | 划转之后的资产 |
| data[].fees | string |  | 手续费 |
| data[].cTime | string |  | 创建时间 |

```json
{
  "code": "00000",
  "message": "success",
  "requestTime": 1695808949356,
  "data": [
    {
      "billId": "14314844815812356565",
      "bizOrderId": "1431481916612435678",
      "coin": "BGB",
      "groupType": "financial",
      "businessType": "BATCH_INTEREST_USER_IN",
      "size": "0.000012550000",
      "balance": "0.00178210",
      "fees": "0.00000000",
      "cTime": "1777018415280"
    }
  ]
}
```

## 获取划转记录

`GET /api/v2/spot/account/transferRecords`

限速规则 20次/1s (UID)

获取划转记录

Operation ID: `classicSpotAccountGetAccountTransferRecords`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| coin | query | string | 是 | 币种名称 |
| fromType | query | string |  | 划转账户类型：`spot` 现货账户 / `p2p` P2P/资金账户 / `coin_futures` 币本位合约账户 / `usdt_futures` U本位合约账户 / `usdc_futures` USDC合约账户 / `crossed_margin` 全仓杠杆账户 / `isolated_margin` 逐仓杠杆账户 |
| startTime | query | string |  | 账单流水的开始时间，即获取该时间戳以后的账单流水，Unix毫秒时间戳，例如1690196141868 |
| endTime | query | string |  | 账单流水的结束时间，即获取该时间戳以前的账单流水，Unix毫秒时间戳，例如1690196141868，startTime和endTime的时间间隔不超过90天 |
| clientOid | query | string |  | 客户自定义订单ID |
| pageNum | query | string |  | (已废弃) 分页第几页，默认1，最大1000 |
| limit | query | string |  | 返回结果的数量，默认100，最大500 |
| idLessThan | query | string |  | 请求此ID之前（更旧的数据）的分页内容，传的值为对应接口的 xxxId。 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].coin | string |  | 币种名称 |
| data[].status | string |  | 划转状态。Successful成功 / Failed 失败 / Processing 处理中 |
| data[].toType | string |  | 转入账户类型：spot 现货账户 / p2p P2P/资金账户 / coin_futures 币本位合约账户 / usdt_futures U本位合约账户 / usdc_futures USDC合约账户 / crossed_margin 全仓杠杆账户 / isolated_margin 逐仓杠杆账户 |
| data[].toSymbol | string |  | 转入账户交易对，当转入账户是isolated_margin时返回 |
| data[].fromType | string |  | 转出账户类型（同上枚举） |
| data[].fromSymbol | string |  | 转出账户交易对，当转出账户是isolated_margin时返回 |
| data[].size | string |  | 数量 |
| data[].ts | string |  | 划转时间，Unix毫秒时间戳，例如1690196141868 |
| data[].clientOid | string |  | 客户自定义订单ID |
| data[].transferId | string |  | 划转订单ID |

```json
{
  "code": "00000",
  "data": [
    {
      "coin": "btc",
      "status": "Successful",
      "toType": "usdt_futures",
      "toSymbol": "",
      "fromType": "spot",
      "fromSymbol": "BTC/USD",
      "size": "1000.00000000",
      "ts": "1631070374488",
      "clientOid": "1",
      "transferId": "1"
    }
  ],
  "msg": "success",
  "requestTime": 1631608142260
}
```

## 获取子母账户划转记录

`GET /api/v2/spot/account/sub-main-trans-record`

限速规则 20次/1s (UID)

获取划转记录

Operation ID: `classicSpotAccountGetSubaccountTransferRecords`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| coin | query | string |  | 币种名称 |
| role | query | string |  | 转出账户类型(默认值：initiator)。`initiator` 发起转账方 / `receiver` 接收方 |
| subUid | query | string |  | 子账户UID，子账户调用时不允许传入`subUid`，母账户调用时，如果不传`subUid`, 则查以母账户为发起方的划转记录 |
| startTime | query | string |  | 账单流水的开始时间，即获取该时间戳以后的账单流水，Unix毫秒时间戳，例如1690196141868 |
| endTime | query | string |  | 账单流水的结束时间，即获取该时间戳以前的账单流水，Unix毫秒时间戳，例如1690196141868，startTime和endTime的时间间隔不超过90天 |
| clientOid | query | string |  | 客户自定义订单ID |
| limit | query | string |  | 返回结果的数量，默认100，最大100 |
| idLessThan | query | string |  | 请求此ID之前（更旧的数据）的分页内容，传的值为对应返回信息中的transferId |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].coin | string |  | 币种名称 |
| data[].status | string |  | 划转状态。Successful成功 / Failed 失败 / Processing 处理中 |
| data[].toType | string |  | 转入账户类型。spot 现货账户 / p2p P2P账户 / coin_futures 币本位合约账户 / usdt_futures U本位合约账户 / usdc_futures USDC合约账户 / crossed_margin 全仓杠杆账户 / isolated_margin 逐仓杠杆账户 |
| data[].fromType | string |  | 转出账户类型（同上枚举） |
| data[].size | string |  | 数量 |
| data[].ts | string |  | 划转时间，Unix毫秒时间戳，例如1690196141868 |
| data[].clientOid | string |  | 客户自定义订单ID |
| data[].transferId | string |  | 划转订单ID |
| data[].newTransferId | string |  | 划转订单ID，与子母账户划转响应中的transferId一样 |
| data[].fromUserId | string |  | 转账发起方 |
| data[].toUserId | string |  | 转账接收方ID |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1700556280430,
  "data": [
    {
      "coin": "USDT",
      "status": "Successful",
      "toType": "usdt_futures",
      "fromType": "spot",
      "size": "1020.00000000",
      "ts": "1691476360467",
      "clientOid": "xxxx",
      "transferId": "xxxx",
      "newTransferId": "xxxx",
      "fromUserId": "xxxx",
      "toUserId": "xxxx"
    }
  ]
}
```

## 获取所有子账户现货资产

`GET /api/v2/spot/account/subaccount-assets`

限速规则 10次/1s (UID)

获取所有子账户现货资产(仅返回有资产账户信息)。仅限非代理商(非ND Broker)用户调用。

Operation ID: `classicSpotAccountGetSubaccountAssets`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| idLessThan | query | string |  | 游标ID，分页游标。首次请求不传，后续传上次返回的最后一个id |
| limit | query | string |  | 每页返回的子账户数量，默认值为10，最大值为50 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| message | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].id | string |  | 游标ID |
| data[].userId | string |  | 用户ID |
| data[].assetsList | object[] |  | 现货资产列表 |
| data[].assetsList[].coin | string |  | 币种名称 |
| data[].assetsList[].available | string |  | 可用资产 |
| data[].assetsList[].limitAvailable | string |  | 受限可用，用于现货跟单场景 |
| data[].assetsList[].frozen | string |  | 冻结资产 |
| data[].assetsList[].locked | string |  | 锁仓资产 |
| data[].assetsList[].uTime | string |  | 更新时间, Unix毫秒时间戳 |

```json
{
  "code": "00000",
  "message": "success",
  "requestTime": 1695808949356,
  "data": [
    {
      "id": "**********",
      "userId": "**********",
      "assetsList": [
        {
          "coin": "BTC",
          "available": "1.1",
          "limitAvailable": "12.1",
          "frozen": "0",
          "locked": "1.1",
          "uTime": "1337654897651"
        }
      ]
    },
    {
      "id": "**********",
      "userId": "**********",
      "assetsList": [
        {
          "coin": "ETH",
          "available": "12.1",
          "limitAvailable": "12.1",
          "frozen": "0",
          "locked": "1.1",
          "uTime": "1337654897651"
        }
      ]
    }
  ]
}
```

## 查询升级状态

`GET /api/v2/spot/account/upgrade-status`

限频规则: 1次/秒/UID

无账户类型限制，母子账户均可调用此接口

Operation ID: `classicSpotAccountGetUpgradeStatus`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| subUid | query | string |  | 子账户用户ID |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.status | string |  | 账户升级状态。`process`处理中 / `success`成功 / `fail`失败 |
| data.reason | string |  | 失败原因，仅`status=fail`时返回，其余情况下为空 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1746687063471,
  "data": {
    "status": "fail",
    "reason": "upgrade_disabled"
  }
}
```

## 账户升级

`POST /api/v2/spot/account/upgrade`

限频规则: 1次/秒/UID

1. 无账户类型限制，母子账户均可调用此接口

2. 接口仅用于升级至统一账户模式

3. 请注意，由于账户升级处理需要约1分钟时间，您收到的成功响应仅表示请求已接收，并不代表账户已成功升级至统一账户

4. 请使用查询升级状态接口，确认账户升级是否成功

Operation ID: `classicSpotAccountUpgradeAccount`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| subUid | string |  | 子账户用户ID |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data |  |  |  |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1728625799912,
  "data": null
}
```

## 当前是否开启BGB抵扣

`GET /api/v2/spot/account/deduct-info`

限速规则: 5次/秒/UID

Operation ID: `classicSpotAccountGetDeductInfo`

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.deduct | string |  | 是否开启 on / off |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695808949356,
  "data": {
    "deduct": "on"
  }
}
```

## 开启BGB抵扣

`POST /api/v2/spot/account/switch-deduct`

限速规则：1次/秒/UID

Operation ID: `classicSpotAccountSwitchDeduct`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| deduct | string | 是 | 是否开启 on/off |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| message | string |  |  |
| requestTime | integer |  |  |
| data | boolean |  |  |

```json
{
  "code": "00000",
  "message": "success",
  "requestTime": 1683875302853,
  "data": true
}
```

## 子母账户划转

`POST /api/v2/spot/wallet/subaccount-transfer`

限速规则 20次/1s (UID)

子母账户资产划转，该接口支持的划转类型包括母账户转子账户、子账户转母账户、子账户转子账户（同一母账户）、子账户内部划转（如现货转合约，要求 fromUserId 与 toUserId 相同）。请求参数中的转入及转出账户UID须为母子/兄弟关系，且所有转账操作均只有母账户才有操作权限。需要母账户API Key绑定IP才能调用此接口。

Operation ID: `classicSpotAccountSubTransfer`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| fromType | string | 是 | 转出账户类型。`spot` 现货账户 / `p2p` P2P/资金账户 / `coin_futures` 币本位合约账户 / `usdt_futures` U本位合约账户 / `usdc_futures` USDC合约账户 / `crossed_margin` 全仓杠杆账户 / `isolated_margin` 逐仓杠杆账户 |
| toType | string | 是 | 转入账户类型（同上枚举） |
| amount | string | 是 | 划转的数量 |
| coin | string | 是 | 币种，如BTC |
| symbol | string |  | 交易对名称，如BTCUSDT (涉及到逐仓杠杆的划转时需要传) |
| clientOid | string |  | 客户自定义ID |
| fromUserId | string | 是 | 转出账户UID |
| toUserId | string | 是 | 转入账户UID |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.transferId | string |  | 划转产生的划转ID |
| data.clientOid | string |  | 自定义clientOid |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1683875302853,
  "data": {
    "transferId": "112321312312312",
    "clientOid": "myclinetOid000001"
  }
}
```

## 划转

`POST /api/v2/spot/wallet/transfer`

限速规则 10次/1s (UID)

资产划转

Operation ID: `classicSpotAccountWalletTransfer`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| fromType | string | 是 | 转出账户类型。`spot` 现货账户 / `p2p` P2P/资金账户 / `coin_futures` 币本位合约账户 / `usdt_futures` U本位合约账户 / `usdc_futures` USDC合约账户 / `crossed_margin` 全仓杠杆账户 / `isolated_margin` 逐仓杠杆账户 |
| toType | string | 是 | 转入账户类型（同上枚举） |
| amount | string | 是 | 划转的数量 |
| coin | string | 是 | 币种，如BTC |
| symbol | string |  | 逐仓杠杆交易对，如BTCUSDT。当转入或转出账户类型是逐仓杠杆账户时必填 |
| clientOid | string |  | 客户自定义ID，幂等，如果传入重复clientOid,则会返回已存在的clientOid划转结果 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.transferId | string |  | 划转产生的划转ID |
| data.clientOid | string |  | 自定义clientOid |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1683875302853,
  "data": {
    "transferId": "112321312312312",
    "clientOid": "myclinetOid000001"
  }
}
```

## 获取账户支持的划转币种

`GET /api/v2/spot/wallet/transfer-coin-info`

限速规则 10 次/1s (UID)

Operation ID: `classicSpotAccountGetTransferCoins`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| fromType | query | string | 是 | 转出账户类型。`spot` 现货账户 / `p2p` P2P账户 / `coin_futures` 币本位合约账户 / `usdt_futures` U本位合约账户 / `usdc_futures` USDC合约账户 / `crossed_margin` 全仓杠杆账户 / `isolated_margin` 逐仓杠杆账户 |
| toType | query | string | 是 | 转入账户类型（同上枚举） |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | string[] |  | 转入转出账户支持币种交集 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1683875302853,
  "data": [
    "BTC",
    "USDT",
    "ETH"
  ]
}
```

## 修改充值自动划转账户类型

`POST /api/v2/spot/wallet/modify-deposit-account`

限速规则 10次/1s (UID)

修改充值自动划转账户类型

Operation ID: `classicSpotAccountModifyDepositAccount`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| accountType | string | 是 | 账户类型。`spot` 现货账户 / `funding` 资金账户 / `coin-futures` 币本位合约账户 / `usdt-futures` U本位合约账户 / `usdc-futures` USDC合约账户 |
| coin | string | 是 | 充值币种 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | string |  | success/fail |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1683875302853,
  "data": "success"
}
```

## 获取充币地址

`GET /api/v2/spot/wallet/deposit-address`

限速规则 10 次/1s (UID)

获取当前账号充币地址

Operation ID: `classicSpotAccountGetDepositAddress`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| coin | query | string | 是 | 币种名称，如USDT，所有币种名称可以通过获取币种信息接口获取 |
| chain | query | string |  | 链名称，如trc20，链名称可以通过获取币种信息接口获取 |
| size | query | string |  | BTC闪电网络提币数量，限制范围：0.000001 - 0.001 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.address | string |  | 充币地址 |
| data.chain | string |  | 链名称 |
| data.coin | string |  | 币种名称 |
| data.tag | string |  | 标签 |
| data.url | string |  | 区块链地址 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1683875302853,
  "data": {
    "address": "xxx",
    "chain": "BTC-Bitcoin",
    "coin": "BTC",
    "tag": "",
    "url": "https://btc.com/xxx"
  }
}
```

## 获取子账户充币地址

`GET /api/v2/spot/wallet/subaccount-deposit-address`

限速规则 10 次/1s (UID)

获取子账号充币地址(查询的子账户需要开启充值权限)

Operation ID: `classicSpotAccountGetSubaccountDepositAddress`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| subUid | query | string | 是 | 子账户uid，子账户列表可以通过查询子账户列表接口获取 |
| coin | query | string | 是 | 币种名称，如USDT，所有币种名称可以通过获取币种信息接口获取 |
| chain | query | string |  | 链名称，如trc20，链名称可以通过获取币种信息接口获取 |
| size | query | string |  | BTC闪电网络提币数量，限制范围：0.000001 - 0.001 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.address | string |  | 充币地址 |
| data.chain | string |  | 链名称 |
| data.coin | string |  | 币种名称 |
| data.tag | string |  | 标签 |
| data.url | string |  | 区块链地址 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1683875302853,
  "data": {
    "address": "xxx",
    "chain": "BTC-Bitcoin",
    "coin": "BTC",
    "tag": "",
    "url": "https://btc.com/xxx"
  }
}
```

## 获取充币记录

`GET /api/v2/spot/wallet/deposit-records`

限速规则 10次/1s (UID)

获取充币记录

Operation ID: `classicSpotAccountGetDepositRecord`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| coin | query | string |  | 币种名称，如USDT |
| orderId | query | string |  | 订单ID。当传入orderId时直接查询此订单，忽略其他入参 |
| startTime | query | string | 是 | 查询的记录起始时间。Unix毫秒时间戳，例如1690196141868 |
| endTime | query | string | 是 | 查询的记录结束时间。Unix毫秒时间戳，例如1690196141868 |
| idLessThan | query | string |  | 游标ID，用于翻页，首次查询不传，查询第二页及后面的数据时，取上一次查询返回的最小orderId，结果会返回小于该值的数据；可以缩短查询响应时间 |
| limit | query | string |  | 每页条目数，默认值为20，最大值为100 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].orderId | string |  | 订单ID |
| data[].tradeId | string |  | 交易ID，如果`dest`为`on_chain`，则为链上交易哈希值；如果`dest`为`internal_transfer`，则为订单ID |
| data[].coin | string |  | 币种名称 |
| data[].type | string |  | 交易类型，固定为`deposit` |
| data[].size | string |  | 数量 |
| data[].status | string |  | 充币状态。`pending`：确认中 / `fail`：失败 / `success`：成功 |
| data[].fromAddress | string |  | 充币发起方，如果`dest`为`on_chain`，则为链上地址；如果`dest`为`internal_transfer`，则为UID,email或者mobile |
| data[].toAddress | string |  | 充币接收方，如果`dest`为`on_chain`，则为链上地址；如果`dest`为`internal_transfer`，则为UID,email或者mobile |
| data[].chain | string |  | 充值网络，链名称格式与 `/api/v2/spot/public/coins` 返回的 `chain` 字段保持一致；如果`dest`为`internal_transfer`时，可忽略此参数 |
| data[].dest | string |  | 充值类型。`on_chain`: 链上充值 / `internal`：内部转账 |
| data[].cTime | string |  | 创建时间，毫秒 |
| data[].uTime | string |  | 修改时间，毫秒 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1654507973411,
  "data": [
    {
      "orderId": "1",
      "tradeId": "1",
      "coin": "USDT",
      "type": "deposit",
      "size": "10.00000000",
      "status": "success",
      "toAddress": "0x51xxx",
      "dest": "on_chain",
      "chain": "erc20",
      "fromAddress": "0x52xxx",
      "cTime": "1653290769222",
      "uTime": "1653290769222"
    }
  ]
}
```

## 获取子账户充值记录

`GET /api/v2/spot/wallet/subaccount-deposit-records`

限速规则 10次/1s (UID)

获取充值记录

Operation ID: `classicSpotAccountGetSubaccountDepositRecord`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| subUid | query | string | 是 | 子账户uid |
| coin | query | string |  | 币种名称，如USDT |
| startTime | query | string |  | 查询的记录起始时间。Unix毫秒时间戳，例如1690196141868 |
| endTime | query | string |  | 查询的记录结束时间。Unix毫秒时间戳，例如1690196141868 |
| idLessThan | query | string |  | 游标ID，用于翻页，首次查询不传，查询第二页及后面的数据时，取上一次查询返回的最小orderId，结果会返回小于该值的数据；可以缩短查询响应时间 |
| limit | query | string |  | 每页条目数，默认值为20，最大值为100 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].orderId | string |  | 订单ID |
| data[].tradeId | string |  | 交易ID，如果`dest`为`on_chain`，则为链上交易哈希值；如果`dest`为`internal_transfer`，则为订单ID |
| data[].coin | string |  | 币种名称 |
| data[].clientOid | string |  | 客户自定义ID |
| data[].size | string |  | 数量 |
| data[].status | string |  | 充值状态。`pending`：确认中 / `fail`：失败 / `success`：成功 |
| data[].fromAddress | string |  | 充值发起方，如果`dest`为`on_chain`，则为链上地址；如果`dest`为`internal_transfer`，则为UID,email或者mobile |
| data[].toAddress | string |  | 充值接收方，如果`dest`为`on_chain`，则为链上地址；如果`dest`为`internal_transfer`，则为UID,email或者mobile |
| data[].chain | string |  | 充值网络，如果`dest`为`internal_transfer`时，可忽略此参数 |
| data[].confirm | string |  | 确认区块数 |
| data[].dest | string |  | 充值方式。`on_chain`：链上充值 / `internal_transfer`：内部转账 |
| data[].tag | string |  | 标签 |
| data[].fee | string |  | 手续费 |
| data[].cTime | string |  | 创建时间 |
| data[].uTime | string |  | 修改时间 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1654507973411,
  "data": [
    {
      "orderId": "1",
      "tradeId": "1",
      "coin": "USDT",
      "dest": "internal_transfer",
      "clientOid": "123",
      "tag": "",
      "size": "10.00000000",
      "fee": "-1.00000000",
      "status": "success",
      "toAddress": "1",
      "fromAddress": "2",
      "confirm": "100",
      "chain": "erc20",
      "cTime": "1653290769222",
      "uTime": "1653290769222"
    }
  ]
}
```

## 获取提币记录

`GET /api/v2/spot/wallet/withdrawal-records`

限速规则 10次/1s (UID)

获取提币记录

Operation ID: `classicSpotAccountGetWithdrawRecord`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| coin | query | string |  | 币种名称，如USDT |
| clientOid | query | string |  | 自定义订单ID。与订单ID二选一，当传入clientOid时直接查询此订单，忽略其他入参 |
| startTime | query | string | 是 | 查询的记录起始时间。Unix毫秒时间戳，例如1690196141868 |
| endTime | query | string | 是 | 查询的记录结束时间。Unix毫秒时间戳，例如1690196141868 |
| idLessThan | query | string |  | 游标ID，用于翻页，首次查询不传，查询第二页及后面的数据时，取上一次查询返回的最小orderId，结果会返回小于该值的数据；可以缩短查询响应时间 |
| orderId | query | string |  | 提币订单ID。与clientOid二选一，当传入订单ID时直接查询此订单，忽略其他入参 |
| limit | query | string |  | 每页条目数，默认值为20，最大值为100 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].orderId | string |  | 提币订单ID |
| data[].tradeId | string |  | 交易ID，如果`dest`为`on_chain`，则为链上交易哈希值；如果`dest`为`internal_transfer`，则为订单ID |
| data[].coin | string |  | 币种名称 |
| data[].clientOid | string |  | 客户自定义ID |
| data[].type | string |  | 类型，固定为`withdraw` |
| data[].dest | string |  | 提币方式。`on_chain`：链上提币 / `internal_transfer`：内部转账 |
| data[].size | string |  | 数量 |
| data[].fee | string |  | 手续费 |
| data[].status | string |  | 提币状态。`pending`：确认中 / `fail`：失败 / `success`：成功 |
| data[].fromAddress | string |  | 提币发起方，如果`dest`为`on_chain`，则为链上地址；如果`dest`为`internal_transfer`，则为UID,email或者mobile |
| data[].toAddress | string |  | 提币接收方，如果`dest`为`on_chain`，则为链上地址；如果`dest`为`internal_transfer`，则为UID,email或者mobile |
| data[].chain | string |  | 提币网络，链名称格式与 `/api/v2/spot/public/coins` 返回的 `chain` 字段保持一致；如果`dest`为`internal_transfer`时，可忽略此参数 |
| data[].confirm | string |  | 确认区块数 |
| data[].tag | string |  | 标签 |
| data[].cTime | string |  | 创建时间，毫秒 |
| data[].uTime | string |  | 修改时间，毫秒 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1654507973411,
  "data": [
    {
      "orderId": "1",
      "tradeId": "1",
      "coin": "USDT",
      "dest": "internal_transfer",
      "clientOid": "123",
      "type": "withdraw",
      "tag": "",
      "size": "10.00000000",
      "fee": "-1.00000000",
      "status": "success",
      "toAddress": "1",
      "fromAddress": "2",
      "confirm": "100",
      "chain": "erc20",
      "cTime": "1653290769222",
      "uTime": "1653290769222"
    }
  ]
}
```

## 提币

`POST /api/v2/spot/wallet/withdrawal`

限速规则 5次/1s (UID)

提币接口 包括链上提币和内部提币。(需要在网页端添加地址到地址簿中)。KYC为韩国的用户请注意，如果您提币至韩国交易所的账户地址内，且数额过大，`memberCode`，`identityType`，`companyName`，`firstName`，`lastName`，这5个参数可以参考填写

Operation ID: `classicSpotAccountWalletWithdrawal`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| coin | string | 是 | 币种，所有币种名称可以通过获取币种信息接口获取 |
| transferType | string | 是 | 提币类型。`on_chain`：链上提币 / `internal_transfer`：内部转账 |
| address | string | 是 | 提币地址，当`transferType`为`on_chain`时，此处填写链地址；当`transferType`为`internal_transfer`时，根据`innerToType`填写UID、email地址或者mobile |
| chain | string |  | 提现币种的区块链网络，例如 erc20, trc20, 等。当`transferType`为`on_chain`时，该参数必须填写；链名称可以通过获取币种信息接口获取 |
| innerToType | string |  | 内部提币地址类型。email 邮件地址 / mobile 移动电话或者手机号 / uid 用户ID。默认值为uid |
| areaCode | string |  | 当提币地址为移动电话时，该参数必须填写 |
| tag | string |  | 地址标签，某些特殊币种提币时使用，例如EOS |
| size | string | 是 | 提币数量。比特币闪电网络提币特别说明：该参数需要填写与比特币闪电网络充值发票金额完全一致的数据；比特币闪电网络的提币数量为到账金额，不包含手续费；数量精度可以通过获取币种信息接口获取 |
| remark | string |  | 备注 |
| clientOid | string |  | 客户端唯一标识 |
| memberCode | string |  | 支持：`bithumb` / `korbit` / `coinone` |
| identityType | string |  | 普通用户：`user`  机构公司：`company` |
| companyName | string |  | 机构，公司名称 |
| firstName | string |  | 名字 |
| lastName | string |  | 姓氏 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.orderId | string |  | 提现产生的提现ID |
| data.clientOid | string |  | 自定义clientOid |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695808949356,
  "data": {
    "orderId": "112321312312312",
    "clientOid": "myclinetOid000001"
  }
}
```

## 撤销提币

`POST /api/v2/spot/wallet/cancel-withdrawal`

限速规则 10次/1s (UID)

1. 用户中心可以设置【撤销提现】开关，有1分钟内"反悔期"可以撤销提币

2. 有人工审核且处于初审状态，可以撤销提币。一旦初审通过或上链，则无法撤销提币

3. 小额自动提币不走人工审核，也无法撤销提币

Operation ID: `classicSpotAccountCancelWithdrawal`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| orderId | string | 是 | 提币订单id |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | string |  | success/fail |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1683875302853,
  "data": "success"
}
```