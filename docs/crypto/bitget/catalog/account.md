---
exchange: bitget
source_url: https://www.bitget.com/docs/catalog/account
api_type: REST
updated_at: 2026-11-28 19:00:13.194353
---

# Account

Unified account assets, settings, margin & borrow, trading risk config, sub-accounts, deposit/withdrawal/transfer, small assets, and institutional rate limit APIs.

版本: 1.0.0

## 服务地址

- `https://api.bitget.com`

## 接口列表

- `GET /api/v3/account/assets` — Get Account Assets
- `GET /api/v3/account/funding-assets` — Get Account Funding Assets
- `GET /api/v3/account/financial-records` — Get Financial Records
- `GET /api/v3/account/funding-financial-records` — Get Funding Financial Records
- `GET /api/v3/account/fee-rate` — Get Account Fee Rate
- `GET /api/v3/account/max-transferable` — Get Max Transferable
- `GET /api/v3/account/max-withdrawal` — Get Max Withdrawal
- `POST /api/v3/account/set-collateral-type` — Set Collateral Type
- `GET /api/v3/account/collateral-type` — Get Collateral Type
- `GET /api/v3/account/custom-collateral-coins` — Get Custom Collateral Coins
- `GET /api/v3/account/info` — Get Account Info
- `GET /api/v3/account/settings` — Get Account Setting
- `GET /api/v3/account/pre-set-leverage` — Pre Set Leverage
- `POST /api/v3/account/set-leverage` — Set Leverage
- `POST /api/v3/account/set-hold-mode` — Set Holding Mode
- `POST /api/v3/account/switch-deduct` — Switch Deduct
- `GET /api/v3/account/deduct-info` — Get Deduct Info
- `POST /api/v3/account/switch` — Switch Account
- `GET /api/v3/account/switch-status` — Get Switch Status
- `POST /api/v3/account/set-margin` — Set Margin
- `GET /api/v3/account/delta-info` — Get Delta Info
- `POST /api/v3/account/adjust-account-mode` — Adjust Account Mode
- `GET /api/v3/account/repayable-coins` — Get Repayable Coins
- `GET /api/v3/account/payment-coins` — Get Payment Coins
- `POST /api/v3/account/repay` — Repay
- `GET /api/v3/account/convert-records` — Get Convert Records
- `POST /api/v3/account/borrow` — Borrow
- `GET /api/v3/account/max-borrowable` — Get Max Borrowable
- `POST /api/v3/account/set-repay-mode` — Set Repay Mode
- `GET /api/v3/account/open-interest-limit` — Get OI Limit
- `GET /api/v3/account/all-fee-rate` — Get All Symbol Fee Rates
- `GET /api/v3/account/eligible-symbols` — Get Eligible Symbols
- `GET /api/v3/account/eligible-margin-tier` — Get Eligible Margin Tier
- `GET /api/v3/account/eligible-loan-info` — Get Eligible Loan Info
- `GET /api/v3/account/eligible-discount-rate` — Get Eligible Discount Rate
- `POST /api/v3/user/create-sub` — Create Sub-account
- `POST /api/v3/user/delete-sub` — Delete Sub-account
- `POST /api/v3/user/freeze-sub` — Freeze/Unfreeze Sub-account
- `GET /api/v3/user/sub-list` — Get Sub-account List
- `GET /api/v3/account/sub-unified-assets` — Get Sub-account Unified Assets
- `POST /api/v3/user/create-sub-api` — Create Sub-account API Key
- `POST /api/v3/user/update-sub-api` — Modify Sub-account API Key
- `POST /api/v3/user/delete-sub-api` — Delete Sub-account API Key
- `GET /api/v3/user/sub-api-list` — Get Sub-account API Keys
- `POST /api/v3/user/sub-account/agent-create` — Create Agent Sub-account
- `POST /api/v3/account/deposit-account` — Set Up Deposit Account
- `GET /api/v3/account/deposit-address` — Get Deposit Address
- `GET /api/v3/account/sub-deposit-address` — Get Sub Deposit Address
- `GET /api/v3/account/deposit-records` — Get Deposit Records
- `GET /api/v3/account/sub-deposit-records` — Get Sub Deposit Records
- `POST /api/v3/account/withdrawal` — Withdrawal
- `POST /api/v3/account/cancel-withdrawal` — Cancel Withdrawal
- `GET /api/v3/account/withdrawal-records` — Get Withdrawal Records
- `GET /api/v3/account/withdraw-address` — Get Withdraw Address Book
- `GET /api/v3/account/transferable-coins` — Get Transferable Coins
- `POST /api/v3/account/transfer` — Transfer
- `POST /api/v3/account/sub-transfer` — Main-Sub Account Transfer
- `GET /api/v3/account/sub-transfer-record` — Get Main-Sub Account Transfer Records
- `POST /api/v3/account/sub-master-transfer` — Sub-Main Account Transfer
- `GET /api/v3/convert/small-assets-history` — Get Small Assets History
- `GET /api/v3/convert/small-assets` — Get Small Assets
- `POST /api/v3/convert/small-assets-trade` — Small Assets Trade
- `GET /api/v3/user/rate-limit-quota` — Get RateLimit Quota
- `POST /api/v3/user/set-rate-limit-quota` — Set RateLimit Quota

## Get Account Assets

`GET /api/v3/account/assets`

Rate limit: 20/sec/UID

Permission: UTA mgt. (read)

Query account information and assets, with only non-zero balances being returned.

Operation ID: `assetsBalanceGetAccountAssets`

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.accountEquity | string |  | Account equity (USD) |
| data.usdtEquity | string |  | Account equity (USDT) |
| data.btcEquity | string |  | Account equity (BTC) |
| data.unrealisedPnl | string |  | Unrealised profit and loss (USD) |
| data.usdtUnrealisedPnl | string |  | Unrealised profit and loss (USDT) |
| data.btcUnrealizedPnl | string |  | Unrealised profit and loss (BTC) |
| data.effEquity | string |  | Effective equity (USD)<br><br>The net value available for margin in spot and perpetual trades under cross-margin mode, converted to fiat |
| data.mmr | string |  | Maintenance margin (USD)<br><br>The minimum margin required to maintain the position, converted to fiat |
| data.imr | string |  | Initial margin (USD)<br><br>Total initial margin of assets in base coin, converted to fiat |
| data.mgnRatio | string |  | Margin ratio |
| data.positionMgnRatio | string |  | Position MMR |
| data.positionValue | string |  | Position value (USD) |
| data.leverage | string |  | Account leverage<br><br>Non-negative number |
| data.assets | object[] |  | Asset list |
| data.assets[].coin | string |  | Coin name |
| data.assets[].equity | string |  | Coin equity |
| data.assets[].usdValue | string |  | Coin equity (USD) |
| data.assets[].balance | string |  | Coin balance (net of borrowed amount) |
| data.assets[].balanceOriginal | string |  | Coin balance (excluding borrowed amount deduction) |
| data.assets[].debt | string |  | Debt<br><br>_Applicable when placing margin orders_ |
| data.assets[].available | string |  | Available |
| data.assets[].locked | string |  | Locked<br><br>_Applicable when placing spot orders_ |
| data.assets[].bonus | string |  | USDT bonus amount |
| data.assets[].interestBase | string |  | Interest calculation base<br><br>Formula: debt + abs(min(0, balance + unrealized PnL)) |
| data.assets[].collateralLimitStatus | string |  | Platform collateral limit status<br><br>`normal` Normal<br><br>`user_warning` User limit warning: the limit has not been triggered, but this coin is approaching the user's collateral limit<br><br>`platform_warning` Platform limit warning: the limit has not been triggered, but this coin is approaching the platform's collateral limit<br><br>`user_limited` User limit triggered<br><br>`platform_limited` Platform limit triggered<br><br>Returns `normal` for coins not under collateral limit management |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1746687063471,
  "data": {
    "accountEquity": "11.13919278",
    "usdtEquity": "11.13921165",
    "btcEquity": "0.00011256",
    "unrealisedPnl": "0",
    "usdtUnrealisedPnl": "0",
    "btcUnrealizedPnl": "0",
    "effEquity": "6.19299777",
    "mmr": "0",
    "imr": "0",
    "mgnRatio": "0",
    "positionMgnRatio": "0",
    "positionValue": "0",
    "leverage": "1",
    "assets": [
      {
        "coin": "USDT",
        "equity": "6.19300826",
        "usdValue": "6.19299777",
        "balance": "6.19300826",
        "balanceOriginal": "6.19300826",
        "available": "6.19300826",
        "debt": "0",
        "locked": "0",
        "bonus": "10",
        "interestBase": "0",
        "collateralLimitStatus": "normal"
      },
      {
        "coin": "BGB",
        "equity": "1.15582129",
        "usdValue": "4.94618029",
        "balance": "1.15582129",
        "balanceOriginal": "1.15582129",
        "available": "1.15582129",
        "debt": "0",
        "locked": "0",
        "bonus": "0",
        "interestBase": "0",
        "collateralLimitStatus": "normal"
      }
    ]
  }
}
```

## Get Account Funding Assets

`GET /api/v3/account/funding-assets`

Rate limit: 20/sec/UID

Permission: UTA mgt. (read)

Obtain fund account information and only return the coins with assets.

Note: For Pre-IPO tokens, the `coin` field uses mixed case, e.g., `preSPAX`. Please be mindful of case sensitivity. The exact `coin` value is subject to what is returned by the Get Coin Info API.

Operation ID: `assetsBalanceGetAccountFundingAssets`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| coin | query | string |  | Coin name |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].coin | string |  | Coin name |
| data[].balance | string |  | Balance<br><br>Unit: the current asset coin |
| data[].available | string |  | Available<br><br>Unit: the current asset coin |
| data[].frozen | string |  | Frozen<br><br>Unit: the current asset coin |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1750396239013,
  "data": [
    {
      "coin": "BGB",
      "available": "0.01",
      "frozen": "0",
      "balance": "0.01"
    },
    {
      "coin": "USDT",
      "available": "0.04",
      "frozen": "0",
      "balance": "0.04"
    }
  ]
}
```

## Get Financial Records

`GET /api/v3/account/financial-records`

Rate limit: 20/sec/UID

Permission: UTA mgt. (read)

Query financial records within the last 90 days.

Operation ID: `assetsBalanceGetFinancialRecords`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| category | query | string | 是 | Product type<br><br>`SPOT` Spot trading<br><br>`MARGIN` Margin trading<br><br>`USDT-FUTURES` USDT futures<br><br>`COIN-FUTURES` Coin-M futures<br><br>`USDC-FUTURES` USDC futures<br><br>`OTHER` Other |
| coin | query | string |  | Coin name<br><br>e.g.,`BTC` |
| type | query | string |  | Type<br><br>`TRANSFER_IN`/`TRANSFER_OUT`......<br><br>All enumeration values can be viewed under the [Enumeration](/docs/uta/enum#type-financial-records) category. |
| startTime | query | string |  | Start timestamp<br><br>A Unix timestamp in milliseconds e.g.,`1597026383085`<br><br>The access window is 90 days |
| endTime | query | string |  | End timestamp<br><br>A Unix timestamp in milliseconds e.g.,`1597026383185`<br><br>The time range between `startTime` and `endTime` must not exceed 30 days |
| limit | query | string |  | Limit per page<br><br>Default:`100`. Maximum:`100` |
| cursor | query | string |  | Cursor<br><br>Pagination is implemented by omitting the cursor in the first query and applying the cursor from the previous query for subsequent pages |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.list | object[] |  | List |
| data.list[].category | string |  | Product Type<br><br>`SPOT` Spot trading<br><br>`MARGIN` Margin trading<br><br>`USDT-FUTURES` USDT futures<br><br>`COIN-FUTURES` Coin-M futures<br><br>`USDC-FUTURES` USDC futures<br><br>`OTHER` Other |
| data.list[].id | string |  | Record ID |
| data.list[].symbol | string |  | Symbol name |
| data.list[].coin | string |  | Coin name |
| data.list[].type | string |  | Type<br><br>`TRANSFER_IN`/`TRANSFER_OUT`/......<br><br>All enumeration values can be viewed under the [Enumeration](/docs/uta/enum#type-financial-records) category. |
| data.list[].positionType | string |  | Position type<br><br>`crossed` Cross margin<br><br>`isolated` Isolated margin |
| data.list[].fee | string |  | Fee |
| data.list[].positionAmount | string |  | Position change amount |
| data.list[].positionBalance | string |  | Position balance |
| data.list[].amount | string |  | Amount |
| data.list[].balance | string |  | Balance |
| data.list[].ts | string |  | The timestamp that system generated the data<br><br>A Unix millisecond timestamp. |
| data.cursor | string |  | Cursor |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1750135478641,
  "data": {
    "list": [
      {
        "category": "Margin",
        "id": "13111111111111111",
        "symbol": "BTCUSDT",
        "coin": "BTC",
        "type": "ORDER_DEALT_IN",
        "positionType": "crossed",
        "fee": "-0.00000531",
        "positionAmount": "0.001",
        "positionBalance": "0.001",
        "amount": "0.00531168",
        "balance": "55.10017801",
        "ts": "1745853486185"
      }
    ],
    "cursor": "122222222222222222"
  }
}
```

## Get Funding Financial Records

`GET /api/v3/account/funding-financial-records`

Rate limit: 10/sec/UID

Permission: UTA mgt. (read)

Query funding account financial records within the last 90 days. You can download your <a href="https://www.bitget.com/record/exchange">full funding account financial records</a> (data available as early as January 1, 2018) via our website.

Operation ID: `assetsBalanceGetFundingFinancialRecords`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| coin | query | string |  | Coin name<br/>e.g.,`BTC` |
| type | query | string |  | Type<br/>`TRANSFER_IN`/`TRANSFER_OUT`......<br/>All enumeration values can be viewed under the [Enumeration](/docs/uta/enum#type-funding-financial-records) category. |
| startTime | query | string |  | Start timestamp<br/>A Unix timestamp in milliseconds e.g.,`1597026383085`<br/>The access window is 90 days |
| endTime | query | string |  | End timestamp<br/>A Unix timestamp in milliseconds e.g.,`1597026383085`<br/>The time range between `startTime` and `endTime` must not exceed 30 days |
| limit | query | string |  | Limit per page<br/>Default:`100`. Maximum:`100` |
| cursor | query | string |  | Cursor<br/>Pagination is implemented by omitting the cursor in the first query and applying the cursor from the previous query for subsequent pages |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.list | object[] |  | List |
| data.list[].id | string |  | Record ID |
| data.list[].coin | string |  | Coin name |
| data.list[].groupType | string |  | Account flow type<br/>All enumeration values can be viewed under the [Enumeration](/docs/uta/enum#grouptype-funding-financial-records) category. |
| data.list[].type | string |  | Account flow subtype<br/>All enumeration values can be viewed under the [Enumeration](/docs/uta/enum#type-funding-financial-records) category. |
| data.list[].amount | string |  | Change amount |
| data.list[].balance | string |  | Account balance after the change |
| data.list[].ts | string |  | Creation time<br/>A Unix millisecond timestamp. |
| data.cursor | string |  | Cursor |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1750135478641,
  "data": {
    "list": [
      {
        "id": "13111111111111111",
        "coin": "BTC",
        "groupType": "financial",
        "type": "interest",
        "amount": "0.00531168",
        "balance": "55.10017801",
        "ts": "1745853486185"
      }
    ],
    "cursor": "122222222222222222"
  }
}
```

## Get Account Fee Rate

`GET /api/v3/account/fee-rate`

Rate limit: 3/sec/UID

Unified account management read permissions are required

Get Account Fee Rate

Operation ID: `assetsBalanceGetAccountFeeRate`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | Symbol<br><br>e.g.,`BTCUSDT` |
| category | query | string | 是 | Product type<br><br>`SPOT` Spot trading<br><br>`MARGIN` Margin trading<br><br>`USDT-FUTURES` USDT futures<br><br>`COIN-FUTURES` Coin-M futures<br><br>`USDC-FUTURES` USDC futures |
| rpiFlag | query | string |  | RPI fee rate flag<br><br>`yes` Yes; `no` No<br><br>For market maker users to get fee rates for RPI-enabled trading pairs. Invalid for non-market-maker users. Default: `no` |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.makerFeeRate | string |  | Maker fee rate<br><br>In decimal form, e.g., 0.0002 represents 0.02% |
| data.takerFeeRate | string |  | Taker fee rate<br><br>In decimal form, e.g., 0.0002 represents 0.02% |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1751972326323,
  "data": {
    "makerFeeRate": "0.0008",
    "takerFeeRate": "0.0008"
  }
}
```

## Get Max Transferable

`GET /api/v3/account/max-transferable`

Rate limit: 3/sec/UID

Permission: UTA mgt. (read)

Get the maximum transferable amount for the unified account.

Operation ID: `assetsBalanceGetMaxTransferable`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| coin | query | string | 是 | Coin name |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.coin | string |  | Coin name |
| data.maxTransfer | string |  | Maximum transferable amount<br><br>Unit: coin. |
| data.borrowMaxTransfer | string |  | Maximum transferable amount for borrowed coins<br><br>Unit: coin. |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1730189435812,
  "data": {
    "coin": "USDT",
    "maxTransfer": "1",
    "borrowMaxTransfer": "1"
  }
}
```

## Get Max Withdrawal

`GET /api/v3/account/max-withdrawal`

Rate limit: 10/sec/UID

Permission: UTA mgt. (read)

Get the maximum withdrawable amount for the specified coin in the unified account. The amount is calculated in real time based on the account's available balance, open positions, liabilities, and other factors. This can be used to obtain the safe withdrawal limit before initiating a withdrawal to avoid failures due to exceeding the limit.

Note: The returned result is a real-time calculated value with millisecond-level latency. The platform will perform a secondary validation at the time of actual withdrawal; this interface result is for reference only.

Operation ID: `assetsBalanceGetMaxWithdrawal`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| coin | query | string | 是 | Coin name, e.g. USDT |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.coin | string |  | Coin name |
| data.otcMaxWithdrawal | string |  | Max withdrawable amount for OTC account |
| data.spotMaxWithdrawal | string |  | Max withdrawable amount for spot account |
| data.utaMaxWithdrawal | string |  | Max withdrawable amount for unified trading account |
| data.totalMaxWithdrawal | string |  | Total max withdrawable amount |
| data.frozenValue | string |  | Frozen asset value, in USDT<br><br>E.g. deposits that have not yet reached the required confirmation count; this amount has not been deducted from the max withdrawable amount |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": {
    "coin": "USDT",
    "otcMaxWithdrawal": "100",
    "spotMaxWithdrawal": "500",
    "utaMaxWithdrawal": "1000",
    "totalMaxWithdrawal": "1600",
    "frozenValue": "0"
  }
}
```

## Set Collateral Type

`POST /api/v3/account/set-collateral-type`

Rate limit: 2/sec/UID

Permission: UTA mgt. (read & write)

Set the collateral type for the unified trading account.

Operation ID: `assetsBalanceSetCollateralType`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| collateralType | query | string | 是 | Collateral type<br><br>`mainstream` Mainstream coins<br><br>`all` All coins<br><br>`custom` Custom |
| collateralCoins | query | string |  | Collateral coin names<br><br>Multiple coins are supported, separated by commas<br><br>Required when `collateralType=custom` |
| allowCashPlus | query | string |  | Whether to enable Cash+ as collateral<br><br>`yes` Enable<br><br>`no` Disable |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | string |  | Operation result |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": "success"
}
```

## Get Collateral Type

`GET /api/v3/account/collateral-type`

Rate limit: 10/sec/UID

Permission: UTA mgt. (read)

Query the collateral type configuration of the unified trading account. Three collateral types are supported: `mainstream`, `all`, and `custom`. Under `mainstream`, USDT, USDC, BTC, DOGE, ETH, and SOL are supported as collateral. Under `custom`, users can specify the effective collateral coins themselves.

Operation ID: `assetsBalanceGetCollateralType`

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.collateralType | string |  | Collateral type<br><br>`mainstream` Mainstream coins<br><br>`all` All coins<br><br>`custom` Custom |
| data.collateralCoins | string |  | Collateral coins<br><br>Returned only when `collateralType=custom`. Multiple coins are separated by commas |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": {
    "collateralType": "custom",
    "collateralCoins": "BTC,ETH,USDT"
  }
}
```

## Get Custom Collateral Coins

`GET /api/v3/account/custom-collateral-coins`

Rate limit: 10/sec/IP

Query all coins supported as custom collateral on the platform. This is a public list that returns the full set of coins supported by the platform and is independent of any user-specific configuration.

Operation ID: `assetsBalanceGetCustomCollateralCoins`

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].collateralCoin | string |  | Collateral coin name |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": [
    {
      "collateralCoin": "BTC"
    },
    {
      "collateralCoin": "ETH"
    },
    {
      "collateralCoin": "USDT"
    }
  ]
}
```

## Get Account Info

`GET /api/v3/account/info`

Rate limit: 5/sec/UID

Query account information, including user ID, inviter, parent account, channel, IP whitelist, permission type and permissions list.

Permission: No permission required

Operation ID: `accountSettingsGetAccountInfo`

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.userId | string |  | User ID |
| data.inviterId | string |  | Inviter UID |
| data.parentId | string |  | Parent account UID.<br><br>Only has a value when the calling account is a sub-account. |
| data.channelCode | string |  | Channel invitation code |
| data.channel | string |  | Channel |
| data.ips | string |  | IP whitelist |
| data.permType | string |  | Permission type<br><br>`read-only` Read only<br><br>`read-and-write` Read and write |
| data.permissions | string[] |  | Permissions list<br><br>`uta_mgt` UTA management<br><br>`uta_trade` UTA trading<br><br>`withdraw` Withdrawal<br><br>`copy_futures_position` Futures copy trading position<br><br>`copy_futures_order` Futures copy trading order |
| data.traderType | string |  | Trader type<br/>`trader` Trader<br/>`not_trader` Not a trader |
| data.regisTime | string |  | Account registration time (Unix timestamp in milliseconds) |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1744617600000.0,
  "data": {
    "userId": "123456789",
    "inviterId": "987654321",
    "parentId": "",
    "channelCode": "6258",
    "channel": "official",
    "ips": "192.168.1.1,192.168.1.2",
    "permType": "read-and-write",
    "permissions": [
      "uta_mgt",
      "uta_trade",
      "withdraw",
      "copy_futures_position",
      "copy_futures_order"
    ],
    "traderType": "trader",
    "regisTime": "1704067200000"
  }
}
```

## Get Account Setting

`GET /api/v3/account/settings`

Rate limit: 20/sec/UID

Query account information, including the holding mode, margin mode, leverage multiple, and more.

Permission: UTA mgt. (read)

Operation ID: `accountSettingsGetAccountSetting`

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.uid | string |  | UID |
| data.accountMode | string |  | Account Mode<br><br>`unified` Unified Mode<br><br>`hybrid` Hybrid Mode<br><br>`upgrading` Unified Account Upgrading<br><br>`switching` Classic Account Switching |
| data.accountLevel | string |  | Account level<br><br>`basic` Stablecoin Margin Mode<br><br>`advanced` Multi-Asset Margin Mode<br><br>`isolated` Spot + Isolated Margin Mode<br><br>`delta` Delta-neutral mode |
| data.assetMode | string |  | Asset mode<br><br>`multi_assets` Multi_assets mode |
| data.holdMode | string |  | Holding mode<br><br>`one_way_mode`/`hedge_mode` |
| data.stpMode | string |  | [STP Mode](https://www.bitget.com/support/articles/12560603812732)<br><br>`none` not setting STP<br><br>`cancel_taker` cancel taker order<br><br>`cancel_maker` cancel maker order<br><br>`cancel_both` cancel both of taker and maker orders |
| data.deltaSwitch | string |  | Delta-neutral mode switch<br><br>`no` Delta-neutral mode disabled<br><br>`yes` Delta-neutral mode enabled<br><br>Delta-neutral mode can only be enabled in Multi-Asset Margin Mode |
| data.repayMode | string |  | Repayment mode<br><br>`auto` Automatic repayment<br><br>`manual` Manual repayment |
| data.symbolConfigList | object[] |  | Symbol configuration list |
| data.symbolConfigList[].category | string |  | Product type<br><br>`USDT-FUTURES` USDT futures<br><br>`COIN-FUTURES` Coin-M futures<br><br>`USDC-FUTURES` USDC futures |
| data.symbolConfigList[].symbol | string |  | Symbol name |
| data.symbolConfigList[].marginMode | string |  | Margin mode<br><br>`crossed`/`isolated` |
| data.symbolConfigList[].leverage | string |  | Leverage multiple |
| data.coinConfigList | object[] |  | Coin configuration list |
| data.coinConfigList[].coin | string |  | Coin name |
| data.coinConfigList[].leverage | string |  | Leverage multiple |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1753787749280,
  "data": {
    "uid": "1111111111",
    "accountMode": "hybrid",
    "assetMode": "multi_assets",
    "accountLevel": "advanced",
    "holdMode": "one_way_mode",
    "stpMode": "none",
    "deltaSwitch": "no",
    "repayMode": "manual",
    "symbolConfigList": [
      {
        "category": "USDT-FUTURES",
        "symbol": "BGBUSDT",
        "marginMode": "crossed",
        "leverage": "20"
      },
      {
        "category": "USDT-FUTURES",
        "symbol": "BTCUSDT",
        "marginMode": "crossed",
        "leverage": "1"
      }
    ],
    "coinConfigList": [
      {
        "coin": "USDT",
        "leverage": "6"
      },
      {
        "coin": "BTC",
        "leverage": "3"
      }
    ]
  }
}
```

## Pre Set Leverage

`GET /api/v3/account/pre-set-leverage`

Rate limit: 10/sec/UID

Preview the impact of adjusting the leverage of a specified symbol. This endpoint returns the estimated maximum tradable amount and required margin after the leverage change, without actually applying the change.

Permission: UTA mgt. (read)

Operation ID: `accountSettingsPreSetLeverage`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| category | query | string | 是 | Product type<br><br>`MARGIN` Margin trading<br><br>`USDT-FUTURES` USDT futures<br><br>`COIN-FUTURES` Coin-M futures<br><br>`USDC-FUTURES` USDC futures |
| symbol | query | string |  | Symbol name<br><br>Required when changing the leverage of a futures symbol |
| coin | query | string |  | Coin name<br><br>Required when changing the leverage for margin trading |
| marginMode | query | string | 是 | Position mode<br><br>`isolated` Isolated margin<br><br>`cross` Cross margin |
| leverage | query | string |  | Leverage multiple<br><br>Applicable to cross margin mode<br><br>Applicable to isolated margin one-way position scenario<br><br>Applicable to isolated margin two-way position scenario when the same leverage is set for both directions |
| longLeverage | query | string |  | Long position leverage<br><br>Only applicable when using isolated margin with two-way position mode and different leverage for each direction<br><br>In two-way position mode, if both `leverage` and `longLeverage` are passed, `longLeverage` takes effect and `leverage` is ignored |
| shortLeverage | query | string |  | Short position leverage<br><br>Only applicable when using isolated margin with two-way position mode and different leverage for each direction<br><br>In two-way position mode, if both `leverage` and `shortLeverage` are passed, `shortLeverage` takes effect and `leverage` is ignored |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.estMaxOpen | string |  | Estimated maximum tradable amount after adjustment<br><br>Returned for futures |
| data.estMaxBorrowable | string |  | Estimated maximum borrowable amount after adjustment<br><br>Returned for margin trading; denominated in `coin` |
| data.requiredMargin | string |  | Required margin, denominated in USD |
| data.marginChange | string |  | Margin usage change after adjustment<br><br>A positive value means an increase, a negative value means a decrease |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": {
    "estMaxOpen": "1.2345",
    "estMaxBorrowable": "100",
    "requiredMargin": "200.5",
    "marginChange": "10.5"
  }
}
```

## Set Leverage

`POST /api/v3/account/set-leverage`

Rate limit: 10/sec/UID

This endpoint allows you to set leverage.

Permission: UTA mgt. (read & write)

Operation ID: `accountSettingsChangeLeverage`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| category | string | 是 | Product type<br><br>`MARGIN` Margin trading<br><br>`USDT-FUTURES` USDT futures<br><br>`COIN-FUTURES` Coin-M futures<br><br>`USDC-FUTURES` USDC futures |
| symbol | string |  | Symbol name<br><br>This field is required to set leverage for futures |
| leverage | string |  | Leverage multiple |
| coin | string |  | Coin name<br><br>This field is required to set leverage for margin trading |
| posSide | string |  | Position side<br><br>`long`/`short`<br><br>This field is required to set leverage for isolated margin |
| marginMode | string |  | Margin mode<br><br>`crossed` Cross margin<br><br>`isolated` Isolated margin<br><br>Defaults to cross margin if not specified. Only futures product lines support isolated margin leverage adjustment in this update. |
| longLeverage | string |  | Long position leverage<br><br>Only applicable when using isolated margin with two-way position mode and different leverage for each direction.<br><br>In two-way position mode, if both `leverage` and `longLeverage` are passed, `longLeverage` takes effect and `leverage` is ignored. |
| shortLeverage | string |  | Short position leverage<br><br>Only applicable when using isolated margin with two-way position mode and different leverage for each direction.<br><br>In two-way position mode, if both `leverage` and `shortLeverage` are passed, `shortLeverage` takes effect and `leverage` is ignored. |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | string |  | Operation result |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1728625799912,
  "data": "success"
}
```

## Set Holding Mode

`POST /api/v3/account/set-hold-mode`

Rate limit: 10/sec/UID

This endpoint allows you to set the position holding mode between one-way and hedge mode.

Permission: UTA mgt. (read & write)

Operation ID: `accountSettingsChangePositionMode`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| holdMode | string | 是 | Holding mode<br><br>`one_way_mode` This mode allows holding positions in a single direction, either long or short, but not both at the same time<br><br>`hedge_mode` This mode allows holding both long and short positions simultaneously |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | string |  | Operation result |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1728625799912,
  "data": "success"
}
```

## Switch Deduct

`POST /api/v3/account/switch-deduct`

Rate limit: 1/sec/UID

Set BGB deduction.

Permission: UTA mgt. (read & write)

Operation ID: `accountSettingsSwitchDeduct`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| deduct | string | 是 | Is it enabled<br><br>`on` enabled<br><br>`off` disabled |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | boolean |  | Operation result |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1728625799912,
  "data": true
}
```

## Get Deduct Info

`GET /api/v3/account/deduct-info`

Rate limit: 1/sec/UID

Get BGB deduction status.

Permission: UTA mgt. (read)

Operation ID: `accountSettingsGetDeductInfo`

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.deduct | string |  | Is it enabled<br><br>`on` enabled<br><br>`off` disabled |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1746687063471,
  "data": {
    "deduct": "on"
  }
}
```

## Switch Account

`POST /api/v3/account/switch`

Rate limit: 1/sec/UID

1. Only supports parent accounts.

2. This endpoint is only used for switching to classic account mode.

3. Please note that since the account switching process takes approximately 1 minute, the successful response you receive only indicates that the request has been received, and does not mean that the account has been successfully switched to the classic account.

4. Please use the query switching status interface to confirm whether the account switching is successful.

Operation ID: `accountSettingsSwitchAccount`

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data |  |  | No response data |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1728625799912,
  "data": null
}
```

## Get Switch Status

`GET /api/v3/account/switch-status`

Rate limit: 5/sec/UID

Only supports parent accounts.

Operation ID: `accountSettingsGetSwitchStatus`

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.status | string |  | Switch Status<br><br>`process` Processing<br><br>`success` Success<br><br>`fail` Failed |
| data.reason | string |  | Failure Reason<br><br>Only returned when the `status = fail` |

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

## Set Margin

`POST /api/v3/account/set-margin`

Rate limit: 10/sec/UID

This endpoint allows you to adjust the margin for an isolated margin position.

Permission: UTA mgt. (read & write)

Operation ID: `accountSettingsSetMargin`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| category | string | 是 | Product type<br><br>`USDT-FUTURES` USDT futures<br><br>`COIN-FUTURES` Coin-M futures<br><br>`USDC-FUTURES` USDC futures |
| symbol | string | 是 | Symbol name |
| posSide | string | 是 | Position side<br><br>`long` Long position<br><br>`short` Short position |
| operation | string | 是 | Operation type<br><br>`add` Add margin<br><br>`remove` Remove margin |
| amount | string | 是 | Margin adjustment amount, denominated in the margin currency<br><br>USDT-FUTURES: USDT; USDC-FUTURES: USDC; COIN-FUTURES: base currency |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | string |  | Operation result |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1728625799912,
  "data": "success"
}
```

## Get Delta Info

`GET /api/v3/account/delta-info`

Rate limit: 20/sec/UID

Get delta-neutral mode information for the account, including the delta equity ratio and per-coin contract position ratios. This endpoint is only available when the account has the delta-neutral switch (`deltaSwitch`) enabled. Delta-neutral mode requires the account to be in Multi-Asset Margin Mode first.

Permission: UTA mgt. (read)

Operation ID: `accountSettingsGetDeltaInfo`

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.deltaEquityRatio | string |  | (Deprecated, no longer used as a hedge-eligibility criterion) Delta equity ratio (decimal form, e.g. `0.2` represents 20%).<br><br>≤ 20%: Account is in a neutral state. If positions also meet the hedge criteria, ADL ranking for contract positions is lower, reducing the risk of auto-deleveraging.<br><br>> 20%: Account is not in a neutral state; contract positions follow normal ADL ranking rules. |
| data.deltaThreshold | string |  | (Deprecated, no longer used as a hedge-eligibility criterion) Delta equity ratio threshold. When both `deltaThreshold` and `positionThreshold` are below their respective thresholds, the account is eligible for the ADL priority queue; otherwise it remains in the normal queue. |
| data.positionThreshold | string |  | Coin net position ratio threshold. |
| data.list | object[] |  | Coin position list. |
| data.list[].coin | string |  | Coin name. |
| data.list[].positionRatio | string |  | Coin net position ratio. Has a value as long as the account has the delta-neutral switch (`deltaSwitch`) enabled. |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": {
    "deltaEquityRatio": "0.15",
    "deltaThreshold": "0.2",
    "positionThreshold": "0.05",
    "list": [
      {
        "coin": "BTC",
        "positionRatio": "0.03"
      }
    ]
  }
}
```

## Adjust Account Mode

`POST /api/v3/account/adjust-account-mode`

Rate limit: 1/sec/UID

This endpoint supports the following account-mode switching scenarios. It supports switching between Stablecoin Margin Mode and Multi-Asset Margin Mode under the Unified Account:

1. The master account switches its own mode

2. A sub-account switches its own mode

3. The master account switches the mode for its sub-account(s)

Operation ID: `accountSettingsAdjustAccountMode`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| mode | string | 是 | Account mode<br><br>`basic` Stablecoin Margin Mode<br><br>`advanced` Multi-Asset Margin Mode<br><br>`delta` Delta-neutral mode (deprecated, use `advanced` mode with `deltaSwitch` instead)<br><br>`isolated` Spot + Isolated Margin Mode |
| deltaSwitch | string |  | Delta-neutral switch, only effective when `mode` is `advanced`<br><br>To enable Delta-neutral mode, the account must first be in Multi-Asset Margin Mode<br><br>`yes` Enable<br><br>`no` Disable |
| targetUid | string |  | Target account UID.<br><br>If not provided, it defaults to the currently operated account.<br><br>If a sub-account UID is provided, it indicates the master account is operating on the sub-account. |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data |  |  | No response data |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1728625799912,
  "data": null
}
```

## Get Repayable Coins

`GET /api/v3/account/repayable-coins`

Rate limit: 10/sec/UID

Query repayable coins.

Permission: UTA mgt. (read)

Operation ID: `marginBorrowGetRepayableCoins`

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.repayableCoinList | object[] |  | Repayable coin list |
| data.repayableCoinList[].coin | string |  | Repayable coin |
| data.repayableCoinList[].size | string |  | Repayable coin quantity |
| data.repayableCoinList[].amount | string |  | Repayable coin amount (USD) |
| data.maxSelection | string |  | Maximum number of coins that can be selected for repayment |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1730189435812,
  "data": {
    "repayableCoinList": [
      {
        "coin": "USDT",
        "size": "147214.04781004",
        "amount": "147102.60677584"
      }
    ],
    "maxSelection": "1"
  }
}
```

## Get Payment Coins

`GET /api/v3/account/payment-coins`

Rate limit: 10/sec/UID

Query payment coins.

Permission: UTA mgt. (read)

Operation ID: `marginBorrowGetPaymentCoins`

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.paymentCoinList | object[] |  | Payment coin list |
| data.paymentCoinList[].coin | string |  | Payment coin |
| data.paymentCoinList[].size | string |  | Payment coin quantity |
| data.paymentCoinList[].amount | string |  | Payment coin amount (USD) |
| data.maxSelection | string |  | Maximum number of coins that can be selected for repayment |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1730189435812,
  "data": {
    "paymentCoinList": [
      {
        "coin": "ETH",
        "size": "0.12",
        "amount": "293.5"
      }
    ],
    "maxSelection": "1"
  }
}
```

## Repay

`POST /api/v3/account/repay`

Rate limit: 5/sec/UID

This endpoint enables manual repayment in the Unified Trading Account.

Permission: UTA mgt. (read & write)

Operation ID: `marginBorrowRepay`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| repayableCoinList | string[] | 是 | Repayable coin list |
| paymentCoinList | string[] | 是 | Payment coin list |

```json
{
  "repayableCoinList": [
    "USDT"
  ],
  "paymentCoinList": [
    "ETH"
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
| data.result | string |  | Repayment result<br><br>`YES`/`NO` |
| data.repayAmount | string |  | Repayment amount |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1728625799912,
  "data": {
    "result": "YES",
    "repayAmount": "4345"
  }
}
```

## Get Convert Records

`GET /api/v3/account/convert-records`

Rate limit: 20/sec/UID

Query convert records within the last 90 days.

Permission: UTA mgt. (read)

Operation ID: `marginBorrowGetConvertRecords`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| fromCoin | query | string |  | From coin (source coin)<br><br>It refers to the coin being converted |
| toCoin | query | string |  | To coin (target coin)<br><br>It refers to the coin being converted into (received) |
| startTime | query | string |  | Start timestamp<br><br>A Unix timestamp in milliseconds e.g.,`1597026383085`<br><br>The access window is 90 days |
| endTime | query | string |  | End timestamp<br><br>A Unix timestamp in milliseconds e.g.,`1597026383185`<br><br>The time range between `startTime` and `endTime` must not exceed 30 days |
| limit | query | string |  | Limit per page<br><br>Default:`100`. Maximum:`100` |
| cursor | query | string |  | Cursor<br><br>Pagination is implemented by omitting the cursor in the first query and applying the cursor from the previous query for subsequent pages |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.list | object[] |  | List |
| data.list[].fromCoin | string |  | From coin (source coin)<br><br>It refers to the coin being converted |
| data.list[].fromCoinSize | string |  | From coin quantity |
| data.list[].toCoin | string |  | To coin (target coin)<br><br>It refers to the coin being converted into (received) |
| data.list[].toCoinSize | string |  | To coin quantity |
| data.list[].price | string |  | Conversion price |
| data.list[].ts | string |  | The timestamp of conversion<br><br>A Unix millisecond timestamp |
| data.cursor | string |  | Cursor |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1730369634178,
  "data": {
    "list": [
      {
        "fromCoin": "USDT",
        "fromCoinSize": "281.72276656",
        "toCoin": "ETH",
        "toCoinSize": "0.0986029682",
        "price": "0.0003499",
        "ts": "1730359119358"
      },
      {
        "fromCoin": "USDT",
        "fromCoinSize": "3305.13434913",
        "toCoin": "ETH",
        "toCoinSize": "1.1567970221",
        "price": "0.00035",
        "ts": "1730359063138"
      }
    ],
    "cursor": "1235780967957364737"
  }
}
```

## Borrow

`POST /api/v3/account/borrow`

Rate limit: 1/sec/UID

Manually borrow a specified amount of a specified coin. Only applicable to the Multi-Asset Margin Mode or delta-neutral mode, and only available when the manual repayment mode is enabled.

Permission: UTA trade

Operation ID: `marginBorrowBorrow`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| coin | string | 是 | Coin to borrow<br><br>Must be a coin supported for borrowing under UTA |
| amount | string | 是 | Amount to borrow |
| clientOid | string |  | Custom borrow order ID |

```json
{
  "coin": "USDT",
  "amount": "100"
}
```

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.orderId | string |  | Borrow order ID |
| data.clientOid | string |  | Custom borrow order ID |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1758512000000.0,
  "data": {
    "orderId": "1234567890",
    "clientOid": "myClientOid001"
  }
}
```

## Get Max Borrowable

`GET /api/v3/account/max-borrowable`

Rate limit: 10/sec/UID

Query the maximum borrowable amount for each coin.

Permission: UTA mgt. (read)

Operation ID: `marginBorrowGetMaxBorrowable`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| coin | query | string | 是 | Coin |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.maxBorrowable | string |  | Maximum manual borrowable |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1758512000000.0,
  "data": {
    "maxBorrowable": "10000"
  }
}
```

## Set Repay Mode

`POST /api/v3/account/set-repay-mode`

Rate limit: 1/sec/UID

Set the repayment mode for manual borrowing. Supports both manual and automatic repayment.

Permission: UTA mgt. (read & write)

Operation ID: `marginBorrowSetRepayMode`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| repayMode | string | 是 | Repayment mode<br><br>`auto` Automatic repayment<br><br>`manual` Manual repayment<br><br>Account (UID)-level setting, not coin-specific; the master account and each sub-account maintain this setting independently, with no inheritance or linkage between them |

```json
{
  "repayMode": "manual"
}
```

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  | No response fields |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1758512000000.0,
  "data": {}
}
```

## Get OI Limit

`GET /api/v3/account/open-interest-limit`

Rate limit: 5/sec/UID

Get open interest limit.

Operation ID: `riskPositionGetOiLimit`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | Symbol<br><br>e.g.,`BTCUSDT` |
| category | query | string | 是 | Product type<br><br>`USDT-FUTURES` USDT futures<br><br>`COIN-FUTURES` Coin-M futures<br><br>`USDC-FUTURES` USDC futures |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.symbol | string |  | Symbol name |
| data.singleUserLimit | string |  | Single User Limit Quantity. |
| data.masterSubLimit | string |  | Main/Sub-account Quantity Limit |
| data.marketMakerLimit | string |  | Market Maker Total Quota |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1764170997805,
  "data": {
    "symbol": "BTCUSDT",
    "singleUserLimit": "2766.30748",
    "masterSubLimit": "9173.8782",
    "marketMakerLimit": "0"
  }
}
```

## Get All Symbol Fee Rates

`GET /api/v3/account/all-fee-rate`

Rate limit: 3/sec/UID

Permission: UTA mgt. (read)

Query fee rates for all trading pairs under a specified product type.

- Only `category` provided (no `symbol`): Returns fee rates for all symbols under that product type

- Only `symbol` provided (no `category`): Returns an error

- Both `category` and `symbol` provided: Returns the fee rate for the specified symbol. If `category` and `symbol` do not match, `symbol` takes priority

- Neither provided: Returns an error

Operation ID: `riskPositionGetAllFeeRate`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| category | query | string | 是 | Product type<br><br>`SPOT` Spot trading<br><br>`MARGIN` Margin trading<br><br>`USDT-FUTURES` USDT futures<br><br>`COIN-FUTURES` Coin-M futures<br><br>`USDC-FUTURES` USDC futures |
| symbol | query | string |  | Symbol name<br><br>e.g.,`BTCUSDT` |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].symbol | string |  | Symbol name |
| data[].makerFeeRate | string |  | Maker fee rate<br><br>In decimal form, e.g., 0.0002 represents 0.02% |
| data[].takerFeeRate | string |  | Taker fee rate<br><br>In decimal form, e.g., 0.0002 represents 0.02% |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1751972326323,
  "data": [
    {
      "symbol": "BTCUSDT",
      "makerFeeRate": "0.0008",
      "takerFeeRate": "0.0008"
    }
  ]
}
```

## Get Eligible Symbols

`GET /api/v3/account/eligible-symbols`

Rate limit: 10/sec/UID

Permission: UTA mgt. (read)

Query all margin trading pairs available to the eligible (whitelist) user.

Operation ID: `riskPositionGetEligibleSymbols`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string |  | Symbol name<br><br>e.g., `BTCUSDT` |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].symbol | string |  | Symbol name |
| data[].category | string |  | Product type<br><br>`MARGIN` Margin trading |
| data[].baseCoin | string |  | Base coin<br><br>e.g., `BTC` in `BTCUSDT` |
| data[].quoteCoin | string |  | Quote coin<br><br>e.g., `USDT` in `BTCUSDT` |
| data[].symbolType | string |  | Symbol type<br><br>`crypto` Cryptocurrency<br><br>`metal` Precious metals<br><br>`stock` Stocks<br><br>`commodity` Commodities |
| data[].buyLimitPriceRatio | string |  | Buy price limit ratio<br><br>The ratio of the buy limit price to the market price, determining the maximum price at which a buy order will be placed |
| data[].sellLimitPriceRatio | string |  | Sell price limit ratio<br><br>The ratio of the sell limit price to the market price, determining the minimum price at which a sell order will be placed |
| data[].minOrderQty | string |  | Minimum order quantity<br><br>The smallest allowable quantity for placing an order in terms of the base coin |
| data[].maxOrderQty | string |  | Maximum order quantity for a single limit order<br><br>The largest allowable quantity for placing an order in terms of the base coin<br><br>A value of 0 indicates no limit |
| data[].pricePrecision | string |  | Price precision<br><br>The number of decimal places allowed for the price |
| data[].quantityPrecision | string |  | Quantity precision<br><br>The number of decimal places allowed for the quantity |
| data[].quotePrecision | string |  | Market order precision<br><br>The number of decimal places allowed for the price of the quote coin |
| data[].minOrderAmount | string |  | Minimum order amount<br><br>The smallest allowable amount for placing an order in terms of the quote coin |
| data[].maxSymbolOrderNum | string |  | Maximum order number in terms of the trading pair |
| data[].maxProductOrderNum | string |  | Maximum order number in terms of the product line |
| data[].status | string |  | Trading pair status<br><br>`listed` Listed (not yet open)<br><br>`online` Normal<br><br>`limit_open` Restrict opening positions<br><br>`limit_close` Restrict closing positions<br><br>`offline` Delisted/under maintenance<br><br>`restrictedAPI` API restricted |
| data[].maintainTime | string |  | Maintenance time<br><br>If not configured, it returns: "" |
| data[].areaSymbol | string |  | Area symbol<br><br>`yes` / `no` |
| data[].maxPositionNum | string |  | Maximum position number in terms of the trading pair |
| data[].isReality | string |  | Reality identifier<br><br>`yes` Reality stock token<br><br>`no` Non-Reality stock token |
| data[].launchTime | string |  | Launch time<br><br>Unix millisecond timestamp indicating when the trading pair was launched |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1784618341109,
  "data": [
    {
      "symbol": "RPBRUSDT",
      "category": "MARGIN",
      "baseCoin": "rPBR",
      "quoteCoin": "USDT",
      "symbolType": "stock",
      "buyLimitPriceRatio": "0.1",
      "sellLimitPriceRatio": "0.1",
      "minOrderQty": "0.0001",
      "maxOrderQty": "0",
      "pricePrecision": "2",
      "quantityPrecision": "4",
      "quotePrecision": "6",
      "minOrderAmount": "20",
      "maxSymbolOrderNum": "",
      "maxProductOrderNum": "400",
      "status": "online",
      "maintainTime": "",
      "areaSymbol": "yes",
      "maxPositionNum": "200",
      "isReality": "yes",
      "launchTime": "1781101641926"
    }
  ]
}
```

## Get Eligible Margin Tier

`GET /api/v3/account/eligible-margin-tier`

Rate limit: 10/sec/UID

Permission: UTA mgt. (read)

Query margin leverage tier information based on the user's whitelist eligibility.

Operation ID: `riskPositionGetEligibleMarginTier`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| coin | query | string |  | Coin name<br><br>e.g., `BTC` |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].coin | string |  | Coin name |
| data[].tiers | object[] |  | Tier list |
| data[].tiers[].tier | string |  | Tier level |
| data[].tiers[].minTierValue | string |  | Minimum position value for this tier |
| data[].tiers[].maxTierValue | string |  | Maximum position value for this tier |
| data[].tiers[].leverage | string |  | Effective leverage |
| data[].tiers[].mmr | string |  | Maintenance margin rate |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1784618341109,
  "data": [
    {
      "coin": "BTC",
      "tiers": [
        {
          "tier": "1",
          "minTierValue": "0",
          "maxTierValue": "50000",
          "leverage": "10",
          "mmr": "0.05"
        }
      ]
    }
  ]
}
```

## Get Eligible Loan Info

`GET /api/v3/account/eligible-loan-info`

Rate limit: 10/sec/UID

Permission: UTA mgt. (read)

Query margin loan information based on the user's whitelist eligibility.

Operation ID: `riskPositionGetEligibleLoanInfo`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| coin | query | string |  | Coin name<br><br>e.g., `BTC` |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].limit | string |  | Single UID loan limit |
| data[].masterSubLimit | string |  | Master and sub-account loan limit |
| data[].platformRemaingQuota | string |  | Platform remaining quota |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1784618341109,
  "data": [
    {
      "limit": "100000",
      "masterSubLimit": "500000",
      "platformRemaingQuota": "10000000"
    }
  ]
}
```

## Get Eligible Discount Rate

`GET /api/v3/account/eligible-discount-rate`

Rate limit: 20/sec/UID

Permission: UTA mgt. (read)

Query the coin discount rate gradient based on the user's whitelist eligibility.

Operation ID: `riskPositionGetEligibleDiscountRate`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| coin | query | string |  | Coin name<br><br>e.g., `BTC` |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].coin | string |  | Coin name |
| data[].list | object[] |  | List |
| data[].list[].tierStartValue | string |  | Tier start value<br><br>e.g., [0,10000 U): tierStartValue=0<br><br>[10000 U,20000 U): tierStartValue=10000<br><br>[20000 U,∞): tierStartValue=20000 |
| data[].list[].discountRate | string |  | Discount rate |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1730911874605,
  "data": [
    {
      "coin": "BTC",
      "list": [
        {
          "tierStartValue": "0",
          "discountRate": "0.85"
        },
        {
          "tierStartValue": "10000",
          "discountRate": "0.70"
        },
        {
          "tierStartValue": "20000",
          "discountRate": "0.50"
        }
      ]
    }
  ]
}
```

## Create Sub-account

`POST /api/v3/user/create-sub`

Rate limit: 10/sec/UID

This API is used for the main account to create a sub-account. It only supports creating unified account virtual sub-accounts and does not support creating regular sub-accounts.

Unified account management read and write permissions are required

Only the main account can call this API

Operation ID: `subAccountsCreateSubAccount`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| username | string | 是 | Generate a virtual email address username. It can only contain lowercase letters and cannot exceed 20 characters. |
| accountMode | string |  | Sub-account Mode<br><br>`classic` Classic Account Sub-account<br><br>`unified` Unified Account Sub-account |
| note | string |  | Note, cannot exceed 50 characters. |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.username | string |  | Virtual Email Address |
| data.subUid | string |  | Virtual Sub-account ID |
| data.status | string |  | Account Status<br><br>`normal` Normal |
| data.note | string |  | Note |
| data.createdTime | string |  | Creation Time, Unix Millisecond Timestamp |
| data.updatedTime | string |  | Last Modified Time, Unix Millisecond Timestamp |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740211442920,
  "data": {
    "username": "xxxx@virtual-bitget.com",
    "subUid": "xxxx",
    "status": "normal",
    "note": "xxxx",
    "createdTime": "1740211445041",
    "updatedTime": "1740211445041"
  }
}
```

## Delete Sub-account

`POST /api/v3/user/delete-sub`

Rate limit: 10/sec/UID

Delete a sub-account.

- **Sub-account type**: Currently only supports deleting virtual sub-accounts and normal sub-accounts; other sub-account types are not supported.
- **Asset check**: The sub-account can only be deleted if the total assets across all business lines do not exceed 10 USDT; otherwise deletion is not allowed.
- **Account opening check**: A sub-account that has opened an MT5 account cannot be deleted.
- **Order check**: The sub-account must have no in-progress orders (unified account, spot, futures, margin, earn, strategy).

Unified account management read and write permissions are required

Only the main account can call this API

Operation ID: `subAccountsDeleteSubAccount`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| subUid | string | 是 | Sub-account to delete |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  | No response fields |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1758512000000.0,
  "data": {}
}
```

## Freeze/Unfreeze Sub-account

`POST /api/v3/user/freeze-sub`

Rate limit: 10/sec/UID

Freeze/Unfreeze Sub-account.

Unified account management read and write permissions are required

Only the main account can call this API

Operation ID: `subAccountsFreezeSubAccount`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| subUid | string | 是 | Sub-account ID to be frozen/unfrozen |
| operation | string | 是 | Operation Type<br><br>`freeze` Freeze<br><br>`unfreeze` Unfreeze |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  | No response fields |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740212117457,
  "data": {}
}
```

## Get Sub-account List

`GET /api/v3/user/sub-list`

Rate limit: 10/sec/UID

Query Sub-account List.

Unified account management read permissions are required

Only the main account can call this API

Operation ID: `subAccountsGetSubAccountList`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| limit | query | string |  | Items per page<br><br>The default value is 100, and the maximum value is 100. |
| cursor | query | string |  | Cursor ID<br><br>Used for pagination. Do not pass it for the first query. For subsequent queries (second page and beyond), use the cursor returned from the previous query. |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.list | object[] |  | Sub-account List |
| data.list[].username | string |  | Sub-account name |
| data.list[].subUid | string |  | Sub-account ID |
| data.list[].status | string |  | Account Status<br><br>`normal` Normal<br><br>`frozen` Frozen |
| data.list[].accountMode | string |  | Account Mode<br><br>`CLASSIC` Classic Account Mode<br><br>`UNIFIED` Unified Account Mode |
| data.list[].type | string |  | Account Type<br><br>`normal` Regular Sub-account<br><br>`virtual` Virtual Sub-account<br><br>`custodian` Custodial Trading Sub-Account<br><br>`fund_management` Custodial Sub-Account<br><br>`agent` Agent Sub-account<br><br>`other` Other |
| data.list[].note | string |  | Note |
| data.list[].createdTime | string |  | Creation Time, Unix Millisecond Timestamp |
| data.list[].updatedTime | string |  | Last Modified Time, Unix Millisecond Timestamp |
| data.hasNext | boolean |  | Is there more data on the next page |
| data.cursor | string |  | Cursor ID |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740212430491,
  "data": {
    "list": [
      {
        "subUid": "xxx",
        "username": "llt****@virtual-bitget.com",
        "status": "normal",
        "accountMode": "CLASSIC",
        "type": "virtual",
        "note": "xxxx",
        "createdTime": "1740129303268",
        "updatedTime": "1740129303268"
      },
      {
        "subUid": "xxx",
        "username": "zml****@virtual-bitget.com",
        "status": "normal",
        "accountMode": "UNIFIED",
        "type": "virtual",
        "note": "xxx",
        "createdTime": "1740211445018",
        "updatedTime": "1740211445018"
      },
      {
        "subUid": "xxx",
        "username": "tmr****@virtual-bitget.com",
        "status": "freeze",
        "accountMode": "UNIFIED",
        "type": "virtual",
        "note": "xxx",
        "createdTime": "1740131800692",
        "updatedTime": "1740212129476"
      }
    ],
    "hasNext": false,
    "cursor": "18484"
  }
}
```

## Get Sub-account Unified Assets

`GET /api/v3/account/sub-unified-assets`

Rate limit: 1/sec/UID

Get Sub-account Unified Assets.

Unified account management read permissions are required

Operation ID: `subAccountsGetSubAccountUnifiedAssets`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| subUid | query | string |  | Sub-account UID<br><br>Leave blank to return all sub-account asset lists |
| cursor | query | string |  | Cursor ID<br><br>For pagination. Omit in first request. Pass previous cursor in subsequent requests. |
| limit | query | string |  | Sub-accounts per Page<br><br>Default value is 10, maximum is 50. |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  | Sub-account asset list |
| data[].subUid | string |  | Sub-account UID |
| data[].cursor | string |  | Cursor ID |
| data[].assets | object[] |  | List of account coins |
| data[].assets[].coin | string |  | Asset coin |
| data[].assets[].equity | string |  | Equity of the asset coin<br><br>Unit is the asset coin |
| data[].assets[].usdValue | string |  | USD value of the asset coin<br><br>Unit is USD |
| data[].assets[].balance | string |  | Balance of the asset coin |
| data[].assets[].available | string |  | Available amount of the asset coin |
| data[].assets[].debt | string |  | Debt of the asset coin |
| data[].assets[].locked | string |  | Amount occupied by orders<br><br>Only has value in spot order scenarios |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1751970047603,
  "data": [
    {
      "subUid": "1111111111",
      "cursor": "5832862",
      "assets": [
        {
          "coin": "USDT",
          "equity": "1",
          "usdValue": "0.99996985",
          "balance": "1",
          "available": "1",
          "debt": "0",
          "locked": "0"
        }
      ]
    }
  ]
}
```

## Create Sub-account API Key

`POST /api/v3/user/create-sub-api`

Rate limit: 10/sec/UID

This API is used to create an API Key for a sub-account under a unified account. It is applicable when the main account is in a mix or unified account mode. If the current main account is in the classic account mode, this API cannot be called.

Supported sub-account types: virtual sub-account, Copper custody sub-account, and regular sub-account. A regular sub-account must already be in unified account mode; if the sub-account is in classic account mode, this API returns an error indicating the sub-account does not support key creation.

Unified account management read and write permissions are required

Only the main account can call this API

Operation ID: `subAccountsCreateSubAccountApiKey`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| subUid | string | 是 | Sub-account ID<br><br>Now also supports regular sub-account UIDs, in addition to virtual sub-accounts and Copper custody sub-accounts |
| note | string | 是 | Note Name<br><br>The note needs to start with a letter and supports [0-9], [a-z], [A-Z], as well as [-,_] |
| type | string | 是 | Permission Type<br><br>`read_write` Read/Write<br><br>`read_only` Read-only |
| passphrase | string | 是 | passphrase<br><br>A combination of 8 to 32 characters of letters and numbers |
| permissions | string[] | 是 | Permission values<br><br>Unified Account Permissions:<br><br>`uta_mgt` Unified Account Management<br><br>`uta_trade` Unified Account Trading |
| ips | string[] | 是 | Withdrawal Whitelist IP<br><br>Multiple IP addresses are supported<br><br>A maximum of 30 IPs can be bound to a single key<br><br>Only supports IPv4 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.note | string |  | Note |
| data.apiKey | string |  | Sub-account API Key |
| data.secret | string |  | Sub-account API Secret |
| data.type | string |  | Sub-account API Key Permission Type<br><br>`read_write` Read/Write<br><br>`read_only` Read-only |
| data.permissions | string[] |  | Sub-account API Key Permission Values<br><br>Unified Account Permissions:<br><br>`uta_mgt` Unified Account Management<br><br>`uta_trade` Unified Account Trading |
| data.ips | string[] |  | Withdrawal Whitelist IP |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740213448866,
  "data": {
    "note": "test",
    "apiKey": "***********************************",
    "secret": "*****************************************",
    "type": "read_only",
    "permissions": [
      "uta_trade"
    ],
    "ips": [
      "127.0.0.1"
    ]
  }
}
```

## Modify Sub-account API Key

`POST /api/v3/user/update-sub-api`

Rate limit: 10/sec/UID

This API is used to modify the unified account sub-account API Key permissions and withdrawal whitelist IP addresses. It only supports modifying the API Key of a unified account sub-account and does not support creating an API Key for a classic account sub-account.

Unified account management read and write permissions are required

Only the main account can call this API

Operation ID: `subAccountsUpdateSubAccountApiKey`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| apiKey | string | 是 | Sub-account API Key |
| passphrase | string | 是 | passphrase<br><br>A combination of 8 to 32 characters of letters and numbers |
| type | string |  | Permission Type<br><br>`read_write` Read/Write<br><br>`read_only` Read-only<br><br>This parameter is required when `permissions` has a value. |
| permissions | string[] |  | Permission values<br><br>Unified Account Permissions:<br><br>`uta_mgt` Unified Account Management<br><br>`uta_trade` Unified Account Trading<br><br>This parameter is required when `type` has a value. |
| ips | string[] |  | Whitelist IP<br><br>If not provided, the IP address will not be modified.<br><br>If an empty value is provided, the IP whitelist will be deleted.<br><br>Multiple IP addresses are supported<br><br>A maximum of 30 IPs can be bound to a single key<br><br>Only supports IPv4 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.apiKey | string |  | Sub-account API Key |
| data.note | string |  | Note name |
| data.type | string |  | Sub-account API Key Permission Type<br><br>`read_write` Read/Write<br><br>`read_only` Read-only |
| data.permissions | string[] |  | Sub-account API Key Permission Values<br><br>Unified Account Permissions:<br><br>`uta_mgt` Unified Account Management<br><br>`uta_trade` Unified Account Trading |
| data.ips | string[] |  | Whitelist IP |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740213448866,
  "data": {
    "note": "test",
    "apiKey": "***********************************",
    "type": "read_only",
    "permissions": [
      "uta_trade"
    ],
    "ips": [
      "127.0.0.1"
    ]
  }
}
```

## Delete Sub-account API Key

`POST /api/v3/user/delete-sub-api`

Rate limit: 10/sec/UID

This API is used for the main account to delete a sub-account's API Key. It is not applicable for the main account or sub-account to delete their own API Key.

Please note that once the deletion is completed, the sub-account API Key will be immediately invalid. Before performing the deletion, ensure that this operation will not cause any loss.

This API only supports deleting API Keys of sub-accounts under a unified account, and does not support deleting API Keys of sub-accounts under a classic account.

Unified account management read and write permissions are required

Only the main account can call this API

Operation ID: `subAccountsDeleteSubAccountApiKey`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| apiKey | string | 是 | The sub-account API Key |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  | No response fields |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740213448866,
  "data": {}
}
```

## Get Sub-account API Keys

`GET /api/v3/user/sub-api-list`

Rate limit: 10/sec/UID

Supports querying the full API Key list under a single sub-account.

Unified account management read permissions are required

Only the main account can call this API

Operation ID: `subAccountsGetSubAccountApiKeyList`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| subUid | query | string | 是 | Sub-account UID |
| limit | query | string |  | Items per page<br><br>The default value is 100, and the maximum value is 100. |
| cursor | query | string |  | Cursor ID<br><br>Used for pagination. Do not pass it for the first query. For subsequent queries (second page and beyond), use the cursor returned from the previous query. |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.list | object[] |  | Sub-account API Key List |
| data.list[].apiKey | string |  | Sub-account API Key |
| data.list[].note | string |  | Note name |
| data.list[].type | string |  | Sub-account API Key Permission Type<br><br>`read_write` Read/Write<br><br>`read_only` Read-only |
| data.list[].permissions | string[] |  | Sub-account API Key Permission Values<br><br>`uta_mgt` Unified Account Management<br><br>`uta_trade` Unified Account Trading |
| data.list[].ips | string[] |  | Withdrawal Whitelist IP |
| data.list[].ts | string |  | Creation timestamp (Unix milliseconds) |
| data.hasNext | boolean |  | Is there more data on the next page |
| data.cursor | string |  | Cursor ID |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740212430491,
  "data": {
    "list": [
      {
        "apiKey": "***********************************",
        "note": "xxxx",
        "type": "read_only",
        "permissions": [
          "uta_trade"
        ],
        "ips": [
          "127.0.0.1"
        ],
        "ts": "1740129303268"
      }
    ],
    "hasNext": false,
    "cursor": "18484"
  }
}
```

## Create Agent Sub-account

`POST /api/v3/user/sub-account/agent-create`

Rate limit: 1/sec/UID

Create a dedicated sub-account for an AI Agent instance. Agent sub-accounts are not editable after creation (name, permissions, and other configurations cannot be modified). Each main account shares the total sub-account quota with regular sub-accounts.

Permission: Unified account management (read and write)

Only the main account can call this API

Operation ID: `subAccountsCreateAgentSubAccount`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| username | string | 是 | Username used to generate the virtual email address. Only lowercase letters are allowed; maximum 20 characters |
| passphrase | string | 是 | API key passphrase. Must be 8-32 characters, consisting of letters and numbers |
| note | string |  | Sub-account note |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.username | string |  | Agent sub-account username |
| data.subUid | string |  | Agent sub-account ID |
| data.apiKey | string |  | Agent sub-account API key |
| data.secret | string |  | Agent sub-account secret |
| data.note | string |  | Note |
| data.createdTime | string |  | Creation time, Unix millisecond timestamp |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": {
    "username": "xxxx@virtual-bitget.com",
    "subUid": "xxxx",
    "apiKey": "***********************************",
    "secret": "*********************************************",
    "note": "xxxx",
    "createdTime": "1740211445041"
  }
}
```

## Set Up Deposit Account

`POST /api/v3/account/deposit-account`

Rate limit: 1/sec/UID

This configuration item remains valid for a long time. That is, once a user sets a default deposit account for a certain symbol, it will be retained permanently, and there is no need to reconfigure it.

Permission: UTA mgt. (read & write)

Operation ID: `depositWithdrawalSetDepositAccount`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| coin | string | 是 | Deposit coin<br><br>e.g. `BTC` |
| accountType | string | 是 | Account type<br><br>`funding` Funding account<br><br>`unified` Unified account<br><br>`otc` OTC account<br><br>The current default is the funding account, and it can be modified to a unified account or an OTC account |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | string |  | Operation result |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1753848186558,
  "data": "success"
}
```

## Get Deposit Address

`GET /api/v3/account/deposit-address`

Rate limit: 10/sec/UID

Get deposit address

Permission: UTA mgt. (read)

Operation ID: `depositWithdrawalGetDepositAddress`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| coin | query | string | 是 | Coin name<br><br>- The coin name can be obtained using the Get Coin Info API |
| chain | query | string |  | Chain name<br><br>- The chain name can be obtained using the Get Coin Info API<br><br>- If not filled, the system will automatically match a chain to generate a deposit address |
| size | query | string |  | Deposit quantity<br><br>- Only applies to BTC Lightning Network<br><br>- Limit range: 0.000001 - 0.001 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.address | string |  | Deposit address |
| data.chain | string |  | Chain name |
| data.coin | string |  | Coin name |
| data.tag | string |  | Tag |
| data.url | string |  | Blockchain explorer address |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1730189276579,
  "data": {
    "address": "0x51xxx",
    "chain": "erc20",
    "coin": "USDT",
    "tag": null,
    "url": ""
  }
}
```

## Get Sub Deposit Address

`GET /api/v3/account/sub-deposit-address`

Rate limit: 10/sec/UID

Get sub-account deposit address

Permission: UTA mgt. (read)

Operation ID: `depositWithdrawalGetSubDepositAddress`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| subUid | query | string | 是 | Sub-account UID<br><br>- The sub-account UID can be obtained via the Sub-account List API |
| coin | query | string | 是 | Coin name<br><br>- The coin name can be obtained using the Get Coin Info API |
| chain | query | string |  | Chain name<br><br>- The chain name can be obtained using the Get Coin Info API |
| size | query | string |  | Deposit quantity<br><br>- Only applies to BTC Lightning Network<br><br>- Limit range: 0.000001 - 0.001 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.address | string |  | Deposit address |
| data.chain | string |  | Chain name |
| data.coin | string |  | Coin name |
| data.tag | string |  | Tag |
| data.url | string |  | Blockchain explorer address |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740213448866,
  "data": {
    "address": "0x51xxx",
    "chain": "erc20",
    "coin": "USDT",
    "tag": "",
    "url": ""
  }
}
```

## Get Deposit Records

`GET /api/v3/account/deposit-records`

Rate limit: 10/sec/UID

Get deposit records

Permission: UTA mgt. (read)

Operation ID: `depositWithdrawalGetDepositRecords`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| coin | query | string |  | Coin name<br><br>- If left blank, all coin deposit records will be retrieved |
| orderId | query | string |  | Order ID<br><br>- Used for specifying order queries |
| startTime | query | string | 是 | Query record start time<br><br>- Unix millisecond timestamp, e.g. 1690196141868 |
| endTime | query | string | 是 | Query record end time<br><br>- Unix millisecond timestamp, e.g. 1690196141868 |
| limit | query | string |  | Items per page<br><br>The default value is 20, and the maximum value is 100 |
| cursor | query | string |  | Cursor ID<br><br>- Used for pagination to reduce query response time<br><br>- Do not send for the initial query. When querying the second page and subsequent data, use the smallest orderId returned from the previous query. The results will return data less than that value |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  | Deposit record list |
| data[].orderId | string |  | Order ID |
| data[].recordId | string |  | Deposit record ID<br><br>- If `dest` is `on_chain`, it is the on-chain hash value<br><br>- If `dest` is `internal_transfer`, it is the order ID |
| data[].coin | string |  | Coin name |
| data[].type | string |  | Operation type<br><br>`deposit` Deposit |
| data[].dest | string |  | Deposit type<br><br>`on_chain` On-chain deposit<br><br>`internal_transfer` Internal transfer |
| data[].size | string |  | Deposit quantity |
| data[].status | string |  | Deposit status<br><br>`pending` Pending<br><br>`success` Success<br><br>`fail` Fail |
| data[].fromAddress | string |  | Deposit initiator<br><br>- If `dest` is `on_chain`, it is the on-chain address<br><br>- If `dest` is `internal_transfer`, it is the UID, email, or mobile number |
| data[].toAddress | string |  | Deposit recipient<br><br>- If `dest` is `on_chain`, it is the on-chain address<br><br>- If `dest` is `internal_transfer`, it is the UID, email, or mobile number |
| data[].chain | string |  | Deposit network<br><br>- This parameter can be ignored when `dest` is `internal_transfer` |
| data[].createdTime | string |  | Deposit record creation time, Unix millisecond timestamp |
| data[].updatedTime | string |  | Deposit record update time, Unix millisecond timestamp |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740481864545,
  "data": [
    {
      "orderId": "1278112570963742720",
      "recordId": "1278112570963742720",
      "coin": "usdt",
      "type": "deposit",
      "dest": "internal_transfer",
      "size": "1",
      "status": "success",
      "fromAddress": "0x51xxx",
      "toAddress": "0x51xxx",
      "chain": "erc20",
      "createdTime": "1740451703778",
      "updatedTime": "1740451703778"
    }
  ]
}
```

## Get Sub Deposit Records

`GET /api/v3/account/sub-deposit-records`

Rate limit: 10/sec/UID

Get sub-account deposit records

Permission: UTA mgt. (read)

Operation ID: `depositWithdrawalGetSubDepositRecords`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| coin | query | string |  | Coin name<br><br>- If left blank, all coin deposit records will be retrieved |
| subUid | query | string | 是 | Sub-account UID |
| startTime | query | string | 是 | Query record start time<br><br>- Unix millisecond timestamp, e.g. 1690196141868 |
| endTime | query | string | 是 | Query record end time<br><br>- Unix millisecond timestamp, e.g. 1690196141868 |
| limit | query | string |  | Items per page<br><br>The default value is 20, and the maximum value is 100 |
| cursor | query | string |  | Cursor ID<br><br>- Used for pagination to reduce query response time<br><br>- Do not send for the initial query. When querying the second page and subsequent data, use the smallest orderId returned from the previous query. The results will return data less than that value |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  | Sub-account deposit record list |
| data[].orderId | string |  | Order ID |
| data[].recordId | string |  | Deposit record ID<br><br>- If `dest` is `on_chain`, it is the on-chain hash value<br><br>- If `dest` is `internal_transfer`, it is the order ID |
| data[].coin | string |  | Coin name |
| data[].type | string |  | Operation type<br><br>`deposit` Deposit |
| data[].dest | string |  | Deposit type<br><br>`on_chain` On-chain deposit<br><br>`internal_transfer` Internal transfer |
| data[].size | string |  | Deposit quantity |
| data[].status | string |  | Deposit status<br><br>`pending` Pending<br><br>`success` Success<br><br>`fail` Fail |
| data[].fromAddress | string |  | Deposit initiator<br><br>- If `dest` is `on_chain`, it is the on-chain address<br><br>- If `dest` is `internal_transfer`, it is the UID, email, or mobile number |
| data[].toAddress | string |  | Deposit recipient<br><br>- If `dest` is `on_chain`, it is the on-chain address<br><br>- If `dest` is `internal_transfer`, it is the UID, email, or mobile number |
| data[].chain | string |  | Deposit network<br><br>- This parameter can be ignored when `dest` is `internal_transfer` |
| data[].createdTime | string |  | Deposit record creation time, Unix millisecond timestamp |
| data[].updatedTime | string |  | Deposit record update time, Unix millisecond timestamp |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1730189276579,
  "data": [
    {
      "orderId": "1278112570963742720",
      "recordId": "1278112570963742720",
      "coin": "usdt",
      "type": "deposit",
      "dest": "internal_transfer",
      "size": "1",
      "status": "success",
      "fromAddress": "0x51xxx",
      "toAddress": "0x51xxx",
      "chain": "erc20",
      "createdTime": "1740451703778",
      "updatedTime": "1740451703778"
    }
  ]
}
```

## Withdrawal

`POST /api/v3/account/withdrawal`

Rate limit: 1/sec/UID

Withdrawal API, includes on-chain withdrawals and internal transfers

Permission: UTA withdrawal

Operation ID: `depositWithdrawalWithdrawal`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| coin | string | 是 | Coin name |
| chain | string |  | Blockchain network<br><br>- For example, `erc20`, `trc20`, etc.<br><br>- This parameter is required when `transferType`=`on_chain`<br><br>- The chain name can be obtained using the Get Coin Info API |
| transferType | string | 是 | Withdrawal type<br><br>`on_chain` On-chain withdrawal<br><br>`internal_transfer` Internal transfer |
| address | string | 是 | Withdrawal address<br><br>- When `transferType` is `on_chain`, fill in the chain address<br><br>- When `transferType` is `internal_transfer`, fill in the UID, email, or mobile number based on `innerToType` |
| innerToType | string |  | Internal withdrawal address type<br><br>`uid` User ID<br><br>`email` Email<br><br>`mobile` Mobile phone number<br><br>- If not filled, the default value is `uid` |
| areaCode | string |  | Area code<br><br>This parameter is required when `innerToType` = `mobile` |
| tag | string |  | Address tag<br><br>This is required for withdrawals of certain coins, like EOS |
| size | string | 是 | Withdrawal quantity<br><br>Special notes for Bitcoin Lightning Network withdrawals:<br><br>This parameter must exactly match the amount on the Bitcoin Lightning Network deposit invoice;<br><br>The withdrawal quantity for Bitcoin Lightning Network represents the amount received, excluding fees;<br><br>The quantity precision can be obtained via the Get Coin Info API |
| remark | string |  | Remark |
| clientOid | string |  | Client order ID |
| memberCode | string |  | Member code<br><br>`bithumb`<br><br>`korbit`<br><br>`coinone` |
| identityType | string |  | Identity type<br><br>`company` Institutional company<br><br>`user` Individual user |
| companyName | string |  | Company name<br><br>Fill in this parameter when `identity`=`company` |
| firstName | string |  | First name<br><br>Fill in this parameter when `identity`=`user` |
| lastName | string |  | Last name<br><br>Fill in this parameter when `identity`=`user` |
| accountType | string |  | Account type to deduct from<br><br>`funding` Funding account<br><br>`uta` Unified trading account<br><br>`otc` OTC account<br><br>Multiple values supported, separated by comma `,`. Deduction order: funding → otc → uta |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.orderId | string |  | Withdrawal order ID |
| data.clientOid | string |  | Client withdrawal order ID |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1730189276579,
  "data": {
    "orderId": "111111111111",
    "clientOid": "111111111111"
  }
}
```

## Cancel Withdrawal

`POST /api/v3/account/cancel-withdrawal`

Rate limit: 1/sec/UID

Cancel a withdrawal request that is still within the cooling-off period. Once the cooling-off period ends, cancellation is no longer possible. Each cancellation is limited to a single order; batch cancellation is not supported.

Permission: Withdraw

Operation ID: `depositWithdrawalCancelWithdrawal`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| orderId | string |  | Withdrawal order ID. Either `orderId` or `clientOid` must be provided. If both are provided, `orderId` takes precedence |
| clientOid | string |  | User-defined withdrawal order ID. Either `orderId` or `clientOid` must be provided |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | string |  | Operation result |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": "success"
}
```

## Get Withdrawal Records

`GET /api/v3/account/withdrawal-records`

Rate limit: 10/sec/UID

Get withdrawal records

Permission: UTA mgt. (read)

Operation ID: `depositWithdrawalGetWithdrawalRecords`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| coin | query | string |  | Coin name<br><br>- If not filled in, all coin withdrawal records will be retrieved |
| orderId | query | string |  | Order ID<br><br>- When querying a single order, you may use either `orderId` or `clientOid`<br><br>- If both are provided, `orderId` takes precedence |
| clientOid | query | string |  | Client order ID<br><br>- When querying a single order, you may use either `orderId` or `clientOid`<br><br>- If both are provided, `orderId` takes precedence |
| startTime | query | string | 是 | Query record start time<br><br>- Unix millisecond timestamp, e.g. 1690196141868 |
| endTime | query | string | 是 | Query record end time<br><br>- Unix millisecond timestamp, e.g. 1690196141868 |
| limit | query | string |  | Items per page<br><br>The default value is 20, and the maximum value is 100 |
| cursor | query | string |  | Cursor ID<br><br>- Used for pagination to reduce query response time<br><br>- Do not send for the initial query. When querying the second page and subsequent data, use the smallest orderId returned from the previous query. The results will return data less than that value |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  | Withdrawal record list |
| data[].orderId | string |  | Order ID |
| data[].clientOid | string |  | Client order ID |
| data[].recordId | string |  | Withdrawal record ID<br><br>- If `dest` is `on_chain`, it is the on-chain hash value<br><br>- If `dest` is `internal_transfer`, it is the order ID |
| data[].coin | string |  | Coin name |
| data[].type | string |  | Operation type<br><br>`withdraw` Withdrawal |
| data[].dest | string |  | Withdrawal type<br><br>`on_chain` On-chain withdrawal<br><br>`internal_transfer` Internal transfer |
| data[].size | string |  | Withdrawal quantity |
| data[].status | string |  | Withdrawal status<br><br>`pending` Pending<br><br>`success` Success<br><br>`fail` Fail |
| data[].fromAddress | string |  | Withdrawal initiator<br><br>- If `dest` is `on_chain`, it is the on-chain address<br><br>- If `dest` is `internal_transfer`, it is the UID, email, or mobile number |
| data[].toAddress | string |  | Withdrawal recipient<br><br>- If `dest` is `on_chain`, it is the on-chain address<br><br>- If `dest` is `internal_transfer`, it is the UID, email, or mobile number |
| data[].chain | string |  | Withdrawal network<br><br>- This parameter can be ignored when `dest` is `internal_transfer` |
| data[].fee | string |  | Transaction fee<br><br>- The unit of measurement is the withdrawal coin |
| data[].confirm | string |  | Confirmation block count |
| data[].tag | string |  | Tag |
| data[].createdTime | string |  | Withdrawal record creation time, Unix millisecond timestamp |
| data[].updatedTime | string |  | Withdrawal record update time, Unix millisecond timestamp |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740481864545,
  "data": [
    {
      "orderId": "1278112570963742720",
      "clientOid": "12121212112",
      "recordId": "1278112570963742720",
      "coin": "usdt",
      "type": "deposit",
      "dest": "internal_transfer",
      "size": "100",
      "status": "success",
      "fromAddress": "0x51xxx",
      "toAddress": "0x51xxx",
      "chain": "erc20",
      "fee": "10",
      "confirm": "5",
      "tag": "",
      "createdTime": "1740451703778",
      "updatedTime": "1740451703778"
    }
  ]
}
```

## Get Withdraw Address Book

`GET /api/v3/account/withdraw-address`

Rate limit: 1/sec/UID

Query the withdrawal address book bound to the account, including address label, chain type, address status and other information.

Permission: Wallet (read)

Operation ID: `depositWithdrawalGetWithdrawAddress`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| coin | query | string |  | Coin name (e.g. BTC, ETH). Returns all coins if not provided. Only supports regular address query; does not support EVM, universal, or internal address queries |
| type | query | string |  | Address book type: `EVM` EVM address / `regular` Regular address / `universal` Universal address / `internal` Internal address |
| limit | query | string |  | Number of entries per page. Default: 10, Max: 10 |
| cursor | query | string |  | Cursor ID for pagination |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.addressList | object[] |  | Address book list |
| data.addressList[].coin | string |  | Coin name |
| data.addressList[].chain | string |  | Chain name |
| data.addressList[].address | string |  | Withdrawal address. When `type=internal`, this field returns UID, phone number, or email |
| data.addressList[].countryCode | string |  | Country code. Only returned when `internalType=mobile` |
| data.addressList[].label | string |  | Address label (user-defined) |
| data.addressList[].memo | string |  | Memo. Required for some chains (e.g. XRP, EOS). Empty string if not applicable |
| data.addressList[].type | string |  | Address book type: `regular` Regular address / `EVM` EVM address / `universal` Universal address / `internal` Internal address |
| data.addressList[].internalType | string |  | Internal transfer type: `uid` UID / `mobile` Phone number / `email` Email. Only has a value when `type=internal` |
| data.addressList[].createdTime | string |  | Creation time (Unix timestamp in milliseconds) |
| data.cursor | string |  | Cursor ID for next page pagination |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": {
    "addressList": [
      {
        "coin": "BTC",
        "chain": "BTC",
        "address": "1A1zP1eP5QGefi2DMPTfTL5SLmv7Divf",
        "countryCode": "",
        "label": "My BTC Wallet",
        "memo": "",
        "type": "regular",
        "internalType": "",
        "createdTime": "1740000000000"
      }
    ],
    "cursor": "1740000000000"
  }
}
```

## Get Transferable Coins

`GET /api/v3/account/transferable-coins`

Rate limit: 10/sec/UID

Query transferable coins **between Classic and UTA accounts**.

_Classic accounts include Spot, Isolated Margin, Cross Margin, USDT Futures, USDC Futures, Coin-M Futures, and P2P accounts_

Permission: UTA mgt. (read)

Operation ID: `depositWithdrawalGetTransferableCoins`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| fromType | query | string | 是 | From (source) account type<br><br>`spot` Spot account/Funding account<br><br>`p2p` P2P account/OTC account<br><br>`coin_futures` Coin-M futures account<br><br>`usdt_futures` USDT futures account<br><br>`usdc_futures` USDC futures account<br><br>`crossed_margin` Cross margin account<br><br>`isolated_margin` Isolated margin account<br><br>`uta` Unified trading account |
| toType | query | string | 是 | To (target) account type<br><br>`spot` Spot account/Funding account<br><br>`p2p` P2P account/OTC account<br><br>`coin_futures` Coin-M futures account<br><br>`usdt_futures` USDT futures account<br><br>`usdc_futures` USDC futures account<br><br>`crossed_margin` Cross margin account<br><br>`isolated_margin` Isolated margin account<br><br>`uta` Unified trading account |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | string[] |  | Transferable coin list |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1730189276579,
  "data": [
    "USDT"
  ]
}
```

## Transfer

`POST /api/v3/account/transfer`

Rate limit: 5/sec/UID

Support for fund transfers in and out between unified accounts and classic accounts

Permission: UTA mgt. (read & write)

Operation ID: `depositWithdrawalTransfer`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| fromType | string | 是 | From (source) account type<br><br>`spot` Spot account/Funding account<br><br>`p2p` P2P account/OTC account<br><br>`coin_futures` Coin-M futures account<br><br>`usdt_futures` USDT futures account<br><br>`usdc_futures` USDC futures account<br><br>`crossed_margin` Cross margin account<br><br>`isolated_margin` Isolated margin account<br><br>`uta` Unified trading account |
| toType | string | 是 | To (target) account type<br><br>`spot` Spot account/Funding account<br><br>`p2p` P2P account/OTC account<br><br>`coin_futures` Coin-M futures account<br><br>`usdt_futures` USDT futures account<br><br>`usdc_futures` USDC futures account<br><br>`crossed_margin` Cross margin account<br><br>`isolated_margin` Isolated margin account<br><br>`uta` Unified trading account |
| amount | string | 是 | Transfer amount |
| coin | string | 是 | Transfer coin, e.g. BTC |
| symbol | string |  | Isolated margin symbol, e.g. BTCUSDT |
| allowBorrow | string |  | Allow borrowing for transfer<br><br>`yes` Enable<br><br>`no` Disable<br><br>If set to `yes`, when the account's available balance is insufficient, the system will automatically borrow through margin to complete the transfer |
| clientOid | string |  | Client-defined ID |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.transferId | string |  | Transfer ID |
| data.clientOid | string |  | Client-defined ID |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1730189276579,
  "data": {
    "transferId": "111111111111",
    "clientOid": "my-transfer-001"
  }
}
```

## Main-Sub Account Transfer

`POST /api/v3/account/sub-transfer`

Rate limit: 5/sec/UID

Sub-account to main account asset transfer. The transfer types supported by this API include:

- Main account to sub-account (only the main account API Key has permission)

- Sub-account to main account (only the main account API Key has permission)

- Sub-account to sub-account (only the main account API Key has permission, and the sending and receiving sub-accounts must belong to the same main account)

- Sub-account internal transfer (only the main account API Key has permission, and the sending and receiving sub-accounts must be the same sub-account)

The UID of the transferring and receiving accounts in the request parameters must be in a main-sub or sibling relationship, and the caller must be the main account API Key.

Unified account management read and write permissions are required. Only the main account can call this API.

Operation ID: `depositWithdrawalSubAccountTransfer`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| fromType | string | 是 | Transferring account type<br><br>`spot` Spot account/Funding account<br><br>`p2p` P2P account/OTC account<br><br>`usdt_futures` USDT-Margined Futures Account<br><br>`coin_futures` Coin-Margined Futures Account<br><br>`usdc_futures` USDC Futures Account<br><br>`crossed_margin` Cross Margin Account<br><br>`uta` Unified Account<br><br>**The above enumerations apply to the main account**<br><br>If it is a sub-account:<br><br>Unified account sub-account only supports `uta` and `spot`<br><br>Classic account sub-account does not support `uta` and `p2p` |
| toType | string | 是 | Receiving account type<br><br>`spot` Spot account/Funding account<br><br>`p2p` P2P account/OTC account<br><br>`usdt_futures` USDT-Margined Futures Account<br><br>`coin_futures` Coin-Margined Futures Account<br><br>`usdc_futures` USDC Futures Account<br><br>`crossed_margin` Cross Margin Account<br><br>`uta` Unified Account<br><br>**The above enumerations apply to the main account**<br><br>If it is a sub-account:<br><br>Unified account sub-account only supports `uta` and `spot`<br><br>Classic account sub-account does not support `uta` and `p2p` |
| amount | string | 是 | Amount to transfer in |
| coin | string | 是 | Transfer coin, e.g. BTC |
| fromUserId | string | 是 | Transferring account UID |
| toUserId | string | 是 | Receiving account UID |
| clientOid | string | 是 | Client order ID. Cannot exceed 50 characters |
| allowBorrow | string |  | Allow borrowing for transfer<br><br>`yes` Enable<br><br>`no` Disable<br><br>If set to `yes`, when the account's available balance is insufficient, the system will automatically borrow through margin to complete the transfer |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.transferId | string |  | Transfer ID |
| data.clientOid | string |  | Client order ID |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740213448866,
  "data": {
    "transferId": "172947298237423",
    "clientOid": "test_001"
  }
}
```

## Get Main-Sub Account Transfer Records

`GET /api/v3/account/sub-transfer-record`

Rate limit: 5/sec/UID

This API supports retrieving transfer records between main and sub accounts.

Unified account management read permissions are required.

Operation ID: `depositWithdrawalGetSubAccountTransferRecords`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| subUid | query | string |  | Sub-account UID. If not provided, transfer records of the main account will be retrieved |
| role | query | string |  | Transfer-out account type<br><br>`initiator` Initiator of the transfer<br><br>`receiver` Recipient of the transfer<br><br>Default: `initiator` |
| coin | query | string |  | Coin name |
| startTime | query | string |  | Start time for querying transfer records<br><br>- Unix millisecond timestamp, e.g. 1690196141868<br><br>- The time interval between startTime and endTime should not exceed 90 days |
| endTime | query | string |  | End time for querying transfer records<br><br>- Unix millisecond timestamp, e.g. 1690196141868<br><br>- The time interval between startTime and endTime should not exceed 90 days |
| clientOid | query | string |  | Client order ID. Cannot exceed 64 characters |
| limit | query | string |  | Items per page<br><br>The default value is 100, and the maximum value is 100 |
| cursor | query | string |  | Cursor ID<br><br>Used for pagination. Do not pass it for the first query. For subsequent queries (second page and beyond), use the cursor returned from the previous query |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.cursor | string |  | Cursor ID |
| data.list | object[] |  | Transfer record list |
| data.list[].transferId | string |  | Transfer ID |
| data.list[].fromType | string |  | Transferring account type<br><br>`spot` Spot account/Funding account<br><br>`p2p` P2P account/OTC account<br><br>`usdt_futures` USDT-Margined Futures Account<br><br>`coin_futures` Coin-Margined Futures Account<br><br>`usdc_futures` USDC Futures Account<br><br>`crossed_margin` Cross Margin Account<br><br>`unified` Unified Account |
| data.list[].toType | string |  | Receiving account type<br><br>`spot` Spot account/Funding account<br><br>`p2p` P2P account/OTC account<br><br>`usdt_futures` USDT-Margined Futures Account<br><br>`coin_futures` Coin-Margined Futures Account<br><br>`usdc_futures` USDC Futures Account<br><br>`crossed_margin` Cross Margin Account<br><br>`unified` Unified Account |
| data.list[].amount | string |  | Transfer amount |
| data.list[].coin | string |  | Transfer coin |
| data.list[].fromUserId | string |  | Transferring account UID |
| data.list[].toUserId | string |  | Receiving account UID |
| data.list[].status | string |  | Transfer status<br><br>`Successful` Success<br><br>`Failed` Failure<br><br>`Processing` In progress |
| data.list[].clientOid | string |  | Client order ID |
| data.list[].oldTransferId | string |  | Old transfer ID |
| data.list[].createdTime | string |  | Transfer creation time, Unix millisecond timestamp |
| data.list[].updatedTime | string |  | Transfer update time, Unix millisecond timestamp |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1751453670468,
  "data": {
    "list": [
      {
        "transferId": "1320888751047921664",
        "fromType": "spot",
        "toType": "uta",
        "amount": "20.00000000",
        "coin": "USDT",
        "fromUserId": "6841950428",
        "toUserId": "6841950428",
        "status": "Successful",
        "clientOid": "1320888751047921664",
        "createdTime": "1750650339853",
        "updatedTime": "1750650339853",
        "oldTransferId": "182797214"
      },
      {
        "transferId": "1314821589514407936",
        "fromType": "spot",
        "toType": "isolated_margin",
        "amount": "1.00000000",
        "coin": "USDT",
        "fromUserId": "6841950428",
        "toUserId": "6841950428",
        "status": "Successful",
        "clientOid": "1314821589514407936",
        "createdTime": "1749203815821",
        "updatedTime": "1749203815821",
        "oldTransferId": "175609331"
      }
    ],
    "cursor": "2"
  }
}
```

## Sub-Main Account Transfer

`POST /api/v3/account/sub-master-transfer`

Rate limit: 5/sec/UID

Sub-account initiates transfer to master account, and the caller must be the sub-account API Key.

Unified account management read and write permissions are required.

Operation ID: `depositWithdrawalSubMasterTransfer`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| fromType | string | 是 | Transferring account type<br><br>`spot` Funding account<br><br>`uta` Unified Account |
| toType | string | 是 | Receiving account type<br><br>`spot` Funding account<br><br>`p2p` OTC account<br><br>`uta` Unified Account |
| amount | string | 是 | Amount to transfer in |
| coin | string | 是 | Transfer coin, e.g. BTC |
| clientOid | string |  | Client order ID. Cannot exceed 64 characters |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.transferId | string |  | Transfer ID |
| data.clientOid | string |  | Client order ID |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740213448866,
  "data": {
    "transferId": "172947298237423",
    "clientOid": "test_001"
  }
}
```

## Get Small Assets History

`GET /api/v3/convert/small-assets-history`

Query historical small asset convert orders under the unified account. Supports filtering by time range and cursor-based pagination. Data from the last 90 days is available; the maximum time range per query is 30 days.

- Rate limit: 10/sec/UID

- Permission: UTA mgt. (read)

Operation ID: `utaAccountSmallAssetsGetSmallAssetsHistory`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| accountType | query | string |  | Account type<br><br>`uta` Unified account<br><br>`funding` Funding account<br><br>If not provided, returns records of all account types |
| orderId | query | string |  | Convert order ID |
| startTime | query | string |  | Start time<br><br>Unix millisecond timestamp<br><br>Data from the last 90 days is available; the maximum time range per query is 30 days |
| endTime | query | string |  | End time<br><br>Unix millisecond timestamp<br><br>Data from the last 90 days is available; the maximum time range per query is 30 days |
| limit | query | string |  | Number of results per page<br><br>Default: 20, Maximum: 100 |
| cursor | query | string |  | Cursor<br><br>Used for pagination. Leave empty for the first query. For subsequent pages, use the smallest orderId returned from the previous query; the result will return data smaller than that value. This can shorten query response time |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.list | object[] |  | List |
| data.list[].orderId | string |  | Convert order ID |
| data.list[].accountType | string |  | Account type<br><br>`uta`/`funding` |
| data.list[].fromCoin | string |  | Coin to convert |
| data.list[].fromAmount | string |  | Amount to convert |
| data.list[].fromCoinPrice | string |  | Price of the coin at conversion time |
| data.list[].toCoin | string |  | Target coin |
| data.list[].toAmount | string |  | Target coin amount |
| data.list[].toCoinPrice | string |  | Target coin price at conversion time |
| data.list[].feeDetail | object[] |  | Fee details |
| data.list[].feeDetail[].fee | string |  | Fee amount |
| data.list[].feeDetail[].feeCoin | string |  | Fee coin |
| data.status | string |  | Convert status<br><br>- success |
| data.createdTime | string |  | Convert time |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": {
    "list": [
      {
        "orderId": "1234567890123456789",
        "accountType": "uta",
        "fromCoin": "DOGE",
        "fromAmount": "12.5",
        "fromCoinPrice": "0.064",
        "toCoin": "BGB",
        "toAmount": "0.8",
        "toCoinPrice": "0.8",
        "feeDetail": {
          "fee": "0.0008",
          "feeCoin": "BGB"
        },
        "status": "success",
        "createdTime": "1740000000000"
      }
    ],
    "cursor": "1234567890123456789"
  }
}
```

## Get Small Assets

`GET /api/v3/convert/small-assets`

Query the list of small-value assets currently held in the unified account. A small-value asset is defined as a position worth less than 5 USDT when converted. The target coin supports BGB.

- Rate limit: 10/sec/UID

- Permission: UTA mgt. (read)

Operation ID: `utaAccountSmallAssetsGetSmallAssets`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| accountType | query | string |  | Account type<br><br>`uta` Unified account (default)<br><br>`funding` Funding account |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].coin | string |  | Coin name |
| data[].available | string |  | Available balance of the coin |
| data[].estimatedCoin | string |  | Estimated target coin<br><br>- BGB |
| data[].estimatedAmount | string |  | Estimated convert amount |
| data[].feeDetail | object |  | Fee details |
| data[].feeDetail.feeRate | string |  | Fee rate |
| data[].feeDetail.fee | string |  | Fee amount |
| data[].cTime | string |  | Current time |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": [
    {
      "coin": "DOGE",
      "available": "12.5",
      "estimatedCoin": "BGB",
      "estimatedAmount": "0.8",
      "feeDetail": {
        "feeRate": "0.001",
        "fee": "0.0008"
      },
      "cTime": "1740000000000"
    }
  ]
}
```

## Small Assets Trade

`POST /api/v3/convert/small-assets-trade`

Convert one or more specified small-value assets in the unified account into the target coin with one click.

- Rate limit: 10/sec/UID

- Permission: UTA trade

Operation ID: `utaAccountSmallAssetsSmallAssetsTrade`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| accountType | string |  | Account type<br><br>`uta` Unified account (default)<br><br>`funding` Funding account |
| fromCoinList | string[] | 是 | Coins to convert |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.fromCoin | string[] |  | Coins to convert |
| data.toCoin | string |  | Target coin |
| data.orderId | string |  | Convert order ID |
| data.accountType | string |  | Account type<br><br>`uta`/`funding`<br><br>Echoes the account type used for this convert |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": {
    "fromCoin": [
      "DOGE",
      "XRP"
    ],
    "toCoin": "BGB",
    "orderId": "1234567890123456789",
    "accountType": "funding"
  }
}
```

## Get RateLimit Quota

`GET /api/v3/user/rate-limit-quota`

Query the rate limit quota configuration for accounts. Supports querying the quota allocation for a single account or listing all sub-account quotas under a master account.

This endpoint also supports being called directly by a sub-account using its own API Key, to query its own rate limit quota.

> **Note**: This endpoint is only available to **MM (Market Maker) and PRO** institutional users.

- Rate limit: 10/sec/UID

- Permission: UTA mgt. (read)

Operation ID: `utaUserRateLimitGetRateLimitQuota`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| category | query | string | 是 | Product type<br><br>`spot` Spot <br><br>`futures` Futures |
| uid | query | string |  | Account UID<br><br>Used to query a single account's rate limit quota; omit to list all sub-accounts<br><br>When called by a sub-account itself, this field is not required and is ignored — the sub-account's own quota is returned |
| cursor | query | string |  | Cursor<br><br>Used for pagination in subsequent queries |
| limit | query | string |  | Limit per page<br><br>Default: `100`. Maximum: `100` |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.category | string |  | Product type<br><br>`spot` Spot <br><br>`futures` Futures |
| data.quotaList | object[] |  | Sub-account rate limit quota list |
| data.quotaList[].uid | string |  | Account UID |
| data.quotaList[].quota | string |  | The actual configured single account rate limit value |
| data.masterSubQuota | string |  | The actual configured master-sub account rate limit value |
| data.masterSubCap | string |  | Master-sub account rate limit Cap |
| data.cursor | string |  | Cursor<br><br>Used for pagination in subsequent queries |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1753987234567,
  "data": {
    "category": "futures",
    "quotaList": [
      {
        "uid": "123456",
        "quota": "100"
      }
    ],
    "masterSubQuota": "10000",
    "masterSubCap": "80000",
    "cursor": "1"
  }
}
```

## Set RateLimit Quota

`POST /api/v3/user/set-rate-limit-quota`

1. Set rate limit quotas for sub-accounts. This endpoint allows master accounts to allocate rate limit quotas for spot and futures trading at the sub-account level.

2. Supports single or batch quota allocation for multiple sub-accounts by business line.

3. The single account rate limit Quota must not exceed the single account rate limit Cap.

4. The sum of all sub-account rate limit Quotas (i.e., the Master-Sub Quota) must not exceed the Master-Sub total rate limit Cap.

5. If adjusting a sub-account's Quota causes the total Master-Sub Quota to exceed the Master-Sub Cap, the API call will be rejected.

6. This endpoint also supports being called directly by a sub-account using its own API Key, to set its own rate limit quota. The rules are the same as when called by the master account.

> **Note**: This endpoint is only available to **MM (Market Maker) and PRO** institutional users.

- Rate limit: 5/sec/UID

- Permission: UTA mgt. (read & write)

Operation ID: `utaUserRateLimitSetRateLimitQuota`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| category | string | 是 | Product type<br><br>`spot` Spot <br><br>`futures` Futures |
| uids | string[] | 是 | Sub-account UIDs<br><br>Up to 50 UIDs per request<br><br>Required when called by the master account; when called by a sub-account itself, this field is not required and is ignored |
| quota | string | 是 | Rate limit quota<br><br>Must not exceed the single account rate limit Cap |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data |  |  | Response data |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1753987234567,
  "data": "success"
}
```


---

统一账户资产、账户设置、杠杆与借贷、交易风控、子账户、充值提币划转、小额资产以及机构限频接口。

版本: 1.0.0

## 服务地址

- `https://api.bitget.com`

## 接口列表

- `GET /api/v3/account/assets` — 获取账户资产
- `GET /api/v3/account/funding-assets` — 获取资金账户资产
- `GET /api/v3/account/financial-records` — 获取财务记录
- `GET /api/v3/account/funding-financial-records` — 获取资金账户财务流水
- `GET /api/v3/account/fee-rate` — 获取交易手续费
- `GET /api/v3/account/max-transferable` — 获取最大可转出
- `GET /api/v3/account/max-withdrawal` — 获取最大可提币数量
- `POST /api/v3/account/set-collateral-type` — 设置抵押品模式
- `GET /api/v3/account/collateral-type` — 获取抵押品模式
- `GET /api/v3/account/custom-collateral-coins` — 获取自定义抵押品支持币种
- `GET /api/v3/account/info` — 获取账户信息
- `GET /api/v3/account/settings` — 获取账户设置
- `GET /api/v3/account/pre-set-leverage` — 预设置调整杠杆
- `POST /api/v3/account/set-leverage` — 调整杠杆
- `POST /api/v3/account/set-hold-mode` — 调整持仓模式
- `POST /api/v3/account/switch-deduct` — 设置BGB抵扣
- `GET /api/v3/account/deduct-info` — 获取BGB抵扣状态
- `POST /api/v3/account/switch` — 账户切换
- `GET /api/v3/account/switch-status` — 获取切换状态
- `POST /api/v3/account/set-margin` — 调整保证金
- `GET /api/v3/account/delta-info` — 获取Delta模式信息
- `POST /api/v3/account/adjust-account-mode` — 账户模式切换
- `GET /api/v3/account/repayable-coins` — 获取可还币种
- `GET /api/v3/account/payment-coins` — 获取支付币种
- `POST /api/v3/account/repay` — 还款
- `GET /api/v3/account/convert-records` — 获取兑换记录
- `POST /api/v3/account/borrow` — 手动借币
- `GET /api/v3/account/max-borrowable` — 查询最大可借
- `POST /api/v3/account/set-repay-mode` — 还币模式设置
- `GET /api/v3/account/open-interest-limit` — 获取OI限仓
- `GET /api/v3/account/all-fee-rate` — 获取业务线所有交易对手续费
- `GET /api/v3/account/eligible-symbols` — 获取准入用户杠杆交易对
- `GET /api/v3/account/eligible-margin-tier` — 获取准入用户杠杆梯度档位
- `GET /api/v3/account/eligible-loan-info` — 获取准入用户借币数据
- `GET /api/v3/account/eligible-discount-rate` — 获取准入用户币种折扣率梯度
- `POST /api/v3/user/create-sub` — 新建子账户
- `POST /api/v3/user/delete-sub` — 删除子账户
- `POST /api/v3/user/freeze-sub` — 冻结/解冻子账户
- `GET /api/v3/user/sub-list` — 查询子账户列表
- `GET /api/v3/account/sub-unified-assets` — 查询子账户统一账户资产
- `POST /api/v3/user/create-sub-api` — 新建子账户API Key
- `POST /api/v3/user/update-sub-api` — 修改子账户API Key
- `POST /api/v3/user/delete-sub-api` — 删除子账户API Key
- `GET /api/v3/user/sub-api-list` — 查询子账户API Key列表
- `POST /api/v3/user/sub-account/agent-create` — 创建 Agent 子账户
- `POST /api/v3/account/deposit-account` — 设置充值账户
- `GET /api/v3/account/deposit-address` — 获取充值地址
- `GET /api/v3/account/sub-deposit-address` — 获取子账户充值地址
- `GET /api/v3/account/deposit-records` — 获取充值记录
- `GET /api/v3/account/sub-deposit-records` — 获取子账户充值记录
- `POST /api/v3/account/withdrawal` — 提币
- `POST /api/v3/account/cancel-withdrawal` — 撤销提币
- `GET /api/v3/account/withdrawal-records` — 获取提币记录
- `GET /api/v3/account/withdraw-address` — 查询提币地址簿
- `GET /api/v3/account/transferable-coins` — 获取可划转币种
- `POST /api/v3/account/transfer` — 划转
- `POST /api/v3/account/sub-transfer` — 子母划转
- `GET /api/v3/account/sub-transfer-record` — 获取子母划转记录
- `POST /api/v3/account/sub-master-transfer` — 子账户主动划转至母账户
- `GET /api/v3/convert/small-assets-history` — 获取小额兑换历史记录
- `GET /api/v3/convert/small-assets` — 获取小额兑换可兑换币种
- `POST /api/v3/convert/small-assets-trade` — 执行小额兑换
- `GET /api/v3/user/rate-limit-quota` — 获取限频配额
- `POST /api/v3/user/set-rate-limit-quota` — 设置限频配额

## 获取账户资产

`GET /api/v3/account/assets`

限频规则: 20次/秒/UID

需要统一账户管理只读/读写权限

获取资产账户信息，仅返回有资产的币种

Operation ID: `assetsBalanceGetAccountAssets`

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.accountEquity | string |  | 账户总权益 (USD) |
| data.usdtEquity | string |  | 账户总权益（USDT） |
| data.btcEquity | string |  | 账户总权益（BTC） |
| data.unrealisedPnl | string |  | 账户总的未实现盈亏 (USD) |
| data.usdtUnrealisedPnl | string |  | 账户总的未实现盈亏（USDT） |
| data.btcUnrealizedPnl | string |  | 账户总的未实现盈亏（BTC） |
| data.effEquity | string |  | 有效权益 USD, 账户中可为全仓模式下的现货、永续合约交易提供保证金的资产折合成法币价值的净值 |
| data.mmr | string |  | 维持保证金 USD, 是用户维持当前仓位所需的最低保证金 |
| data.imr | string |  | 初始保证金 USD, 账户中所有全仓持仓及挂单的保证金折合成法币价值的净值 |
| data.mgnRatio | string |  | 维持保证金率 |
| data.positionMgnRatio | string |  | 仓位维持保证金比率 |
| data.positionValue | string |  | 仓位价值<br><br>单位为USD |
| data.leverage | string |  | 账户杠杆<br><br>非负数 |
| data.assets | object[] |  | 账户币种列表 |
| data.assets[].coin | string |  | 资产币种 |
| data.assets[].equity | string |  | 资产币种权益<br><br>单位为资产币种 |
| data.assets[].usdValue | string |  | 当前币种折USD价值<br><br>单位为USD |
| data.assets[].balance | string |  | 币种余额（扣除借币） |
| data.assets[].balanceOriginal | string |  | 币种余额（不扣除借币） |
| data.assets[].debt | string |  | 资产币种负债 |
| data.assets[].available | string |  | 资产币种可用 |
| data.assets[].locked | string |  | 下单占用<br><br>仅现货下单场景有值 |
| data.assets[].bonus | string |  | USDT 体验金金额 |
| data.assets[].interestBase | string |  | 计息基础<br><br>计息 = 借币 + abs(min(0, 余额 + 未实现盈亏)) |
| data.assets[].collateralLimitStatus | string |  | 平台抵押品限额状态<br><br>`normal`正常<br><br>`user_warning`用户限额预警。未触发限额，但该币种已接近用户抵押品限额<br><br>`platform_warning`平台限额预警。未触发限额，但该币种已接近平台抵押品限额<br><br>`user_limited`用户已触发限额<br><br>`platform_limited`平台已触发限额<br><br>未纳入抵押品限额管理的币种返回 `normal` |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1746687063471,
  "data": {
    "accountEquity": "11.13919278",
    "usdtEquity": "11.13921165",
    "btcEquity": "0.00011256",
    "unrealisedPnl": "0",
    "usdtUnrealisedPnl": "0",
    "btcUnrealizedPnl": "0",
    "effEquity": "6.19299777",
    "mmr": "0",
    "imr": "0",
    "mgnRatio": "0",
    "positionMgnRatio": "0",
    "positionValue": "0",
    "leverage": "1",
    "assets": [
      {
        "coin": "USDT",
        "equity": "6.19300826",
        "usdValue": "6.19299777",
        "balance": "6.19300826",
        "balanceOriginal": "6.19300826",
        "available": "6.19300826",
        "debt": "0",
        "locked": "0",
        "bonus": "10",
        "interestBase": "0",
        "collateralLimitStatus": "normal"
      },
      {
        "coin": "BGB",
        "equity": "1.15582129",
        "usdValue": "4.94618029",
        "balance": "1.15582129",
        "balanceOriginal": "1.15582129",
        "available": "1.15582129",
        "debt": "0",
        "locked": "0",
        "bonus": "0",
        "interestBase": "0",
        "collateralLimitStatus": "normal"
      }
    ]
  }
}
```

## 获取资金账户资产

`GET /api/v3/account/funding-assets`

限频规则: 20次/秒/UID

需要统一账户管理只读/读写权限

获取资金账户信息，仅返回有资产的币种。

注：Pre-IPO 类型币种的 `coin` 字段大小写混用，如 `preSPAX`，请注意大小写，以获取币种信息接口里返回的 coin 为准

Operation ID: `assetsBalanceGetAccountFundingAssets`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| coin | query | string |  | 币种名称 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].coin | string |  | 币种名称 |
| data[].balance | string |  | 总余额<br><br>单位为当前资产币种 |
| data[].available | string |  | 可用<br><br>单位为当前资产币种 |
| data[].frozen | string |  | 冻结<br><br>单位为当前资产币种 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1750396239013,
  "data": [
    {
      "coin": "BGB",
      "available": "0.01",
      "frozen": "0",
      "balance": "0.01"
    },
    {
      "coin": "USDT",
      "available": "0.04",
      "frozen": "0",
      "balance": "0.04"
    }
  ]
}
```

## 获取财务记录

`GET /api/v3/account/financial-records`

限频规则: 20次/秒/UID

需要统一账户管理只读/读写权限

获取账户90天内流水信息

Operation ID: `assetsBalanceGetFinancialRecords`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| category | query | string | 是 | 产品类型<br><br>`SPOT` 现货交易<br><br>`MARGIN` 杠杆交易<br><br>`USDT-FUTURES` USDT合约<br><br>`COIN-FUTURES` 币本位合约<br><br>`USDC-FUTURES` USDC合约<br><br>`OTHER` 其它 |
| coin | query | string |  | 币种<br><br>例如，`BTC` |
| type | query | string |  | 账户流水类型<br><br>`TRANSFER_IN`/`TRANSFER_OUT`......<br><br>详细枚举可以在 [枚举](/zh-CN/docs/uta/enum#type-financial-record) 页面获取 |
| startTime | query | string |  | 开始时间戳<br><br>Unix时间戳的毫秒数格式，如 1597026383085<br><br>最大查询范围90天 |
| endTime | query | string |  | 结束时间戳<br><br>Unix时间戳的毫秒数格式，如 1597026383085<br><br>`startTime`和`endTime`间隔不超过30天 |
| limit | query | string |  | 查询条数 最大100，默认100 |
| cursor | query | string |  | 分页游标<br><br>用于翻页，首次查询不传，查询第二页及后面的数据时，取上一次查询返回cursor |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.list | object[] |  | 账务流水列表 |
| data.list[].category | string |  | 产品类型<br><br>`SPOT` 现货交易<br><br>`MARGIN` 杠杆交易<br><br>`USDT-FUTURES` USDT专业合约<br><br>`COIN-FUTURES` 币本位合约<br><br>`USDC-FUTURES` USDC合约<br><br>`OTHER` 其它 |
| data.list[].id | string |  | 记录ID |
| data.list[].symbol | string |  | 交易对 |
| data.list[].coin | string |  | 币种 |
| data.list[].type | string |  | 账户流水类型<br><br>`TRANSFER_IN`/`TRANSFER_OUT`......<br><br>详细枚举可以在 [枚举](/zh-CN/docs/uta/enum#type-financial-record) 页面获取 |
| data.list[].positionType | string |  | 仓位类型<br><br>`crossed` 全仓<br><br>`isolated` 逐仓 |
| data.list[].fee | string |  | 手续费(交易/提币) |
| data.list[].positionAmount | string |  | 仓位变动数量 |
| data.list[].positionBalance | string |  | 仓位余额 |
| data.list[].amount | string |  | 变动金额 |
| data.list[].balance | string |  | 变动后账户剩余资产 |
| data.list[].ts | string |  | 创建时间<br><br>Unix毫秒时间戳 |
| data.cursor | string |  | 分页游标 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1750135478641,
  "data": {
    "list": [
      {
        "category": "Margin",
        "id": "13111111111111111",
        "symbol": "BTCUSDT",
        "coin": "BTC",
        "type": "ORDER_DEALT_IN",
        "positionType": "crossed",
        "fee": "-0.00000531",
        "positionAmount": "0.001",
        "positionBalance": "0.001",
        "amount": "0.00531168",
        "balance": "55.10017801",
        "ts": "1745853486185"
      }
    ],
    "cursor": "122222222222222222"
  }
}
```

## 获取资金账户财务流水

`GET /api/v3/account/funding-financial-records`

限频规则: 10次/秒/UID

需要统一账户管理只读/读写权限

获取资金账户财务流水，最大查询范围90天，用户可以通过网页端下载[全部时间资金账户财务流水](https://www.bitget.com/zh-CN/record/exchange)(最早可导出2018年1月1日的数据)

Operation ID: `assetsBalanceGetFundingFinancialRecords`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| coin | query | string |  | 币种<br/>例如，`BTC` |
| type | query | string |  | 账户流水类型<br/>`TRANSFER_IN`/`TRANSFER_OUT`......<br/>详细枚举可以在 [枚举](/zh-CN/docs/uta/enum#type-funding-financial-records) 页面获取 |
| startTime | query | string |  | 开始时间戳<br/>Unix时间戳的毫秒数格式，如 1597026383085<br/>最大查询范围90天 |
| endTime | query | string |  | 结束时间戳<br/>Unix时间戳的毫秒数格式，如 1597026383085<br/>`startTime`和`endTime`间隔不超过30天 |
| limit | query | string |  | 查询条数 最大100，默认100 |
| cursor | query | string |  | 分页游标<br/>用于翻页，首次查询不传，查询第二页及后面的数据时，取上一次查询返回cursor |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.list | object[] |  | 账务流水列表 |
| data.list[].id | string |  | 记录ID |
| data.list[].coin | string |  | 币种 |
| data.list[].groupType | string |  | 账户流水类型<br/>详细枚举可以在 [枚举](/zh-CN/docs/uta/enum#grouptype-funding-financial-records) 页面获取 |
| data.list[].type | string |  | 账户流水子类型<br/>详细枚举可以在 [枚举](/zh-CN/docs/uta/enum#type-funding-financial-records) 页面获取 |
| data.list[].amount | string |  | 变动金额 |
| data.list[].balance | string |  | 变动后账户剩余资产 |
| data.list[].ts | string |  | 创建时间<br/>Unix毫秒时间戳 |
| data.cursor | string |  | 分页游标 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1750135478641,
  "data": {
    "list": [
      {
        "id": "13111111111111111",
        "coin": "BTC",
        "groupType": "financial",
        "type": "interest",
        "amount": "0.00531168",
        "balance": "55.10017801",
        "ts": "1745853486185"
      }
    ],
    "cursor": "122222222222222222"
  }
}
```

## 获取交易手续费

`GET /api/v3/account/fee-rate`

限频规则: 3次/秒/UID

需要统一账户管理只读权限

获取交易手续费

Operation ID: `assetsBalanceGetAccountFeeRate`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | 交易对名称<br><br>如`BTCUSDT` |
| category | query | string | 是 | 业务线<br><br>`SPOT` 现货交易<br><br>`MARGIN` 杠杆交易<br><br>`USDT-FUTURES` USDT合约<br><br>`COIN-FUTURES` 币本位合约<br><br>`USDC-FUTURES` USDC合约 |
| rpiFlag | query | string |  | RPI费率标识<br><br>`yes` 是；`no` 否<br><br>用于做市商用户获取RPI交易对的费率，非做市商用户填写无效，默认值为`no` |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.makerFeeRate | string |  | 挂单手续费率<br><br>小数形式，即0.0002代表万分之二 |
| data.takerFeeRate | string |  | 吃单手续费率<br><br>小数形式，即0.0002代表万分之二 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1751972326323,
  "data": {
    "makerFeeRate": "0.0008",
    "takerFeeRate": "0.0008"
  }
}
```

## 获取最大可转出

`GET /api/v3/account/max-transferable`

限频规则: 3次/秒/UID

需要统一账户管理只读权限

获取统一账户最大可转出

Operation ID: `assetsBalanceGetMaxTransferable`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| coin | query | string | 是 | 币种名称 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.coin | string |  | 币种名称 |
| data.maxTransfer | string |  | 最大可转出<br><br>单位为coin |
| data.borrowMaxTransfer | string |  | 借币最大可转出<br><br>单位为coin |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1730189435812,
  "data": {
    "coin": "USDT",
    "maxTransfer": "1",
    "borrowMaxTransfer": "1"
  }
}
```

## 获取最大可提币数量

`GET /api/v3/account/max-withdrawal`

限频规则: 10次/秒/UID

需要统一账户管理只读权限

查询当前统一账户指定币种的最大可提币数量。该额度由平台综合账户可用余额、未结清持仓、负债占用等因素实时计算，适用于用户在发起提币前预先获取安全提币上限，避免因超限而导致提币失败。

注意：返回结果为实时计算值，存在毫秒级延迟；实际提币时平台仍会进行二次校验，该接口结果仅供参考。

Operation ID: `assetsBalanceGetMaxWithdrawal`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| coin | query | string | 是 | 币种名称，如 USDT |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.coin | string |  | 币种名称 |
| data.otcMaxWithdrawal | string |  | OTC账户最大可提币数量 |
| data.spotMaxWithdrawal | string |  | 现货账户最大可提币数量 |
| data.utaMaxWithdrawal | string |  | 统一账户最大可提币数量 |
| data.totalMaxWithdrawal | string |  | 全部最大可提币数量 |
| data.frozenValue | string |  | 冻结资产价值，单位为 USDT<br><br>如充值未达确认数的金额；最大可提币数量未扣减该部分 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": {
    "coin": "USDT",
    "otcMaxWithdrawal": "100",
    "spotMaxWithdrawal": "500",
    "utaMaxWithdrawal": "1000",
    "totalMaxWithdrawal": "1600",
    "frozenValue": "0"
  }
}
```

## 设置抵押品模式

`POST /api/v3/account/set-collateral-type`

限频规则: 2次/秒/UID

需要统一账户管理读写权限

设置当前统一账户的抵押品模式。

Operation ID: `assetsBalanceSetCollateralType`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| collateralType | query | string | 是 | 抵押品模式<br><br>`mainstream` 主流币<br><br>`all` 全部币种<br><br>`custom` 自定义 |
| collateralCoins | query | string |  | 抵押品币种名称<br><br>支持多个币种，使用英文逗号分隔<br><br>自定义模式 `collateralType=custom` 必填 |
| allowCashPlus | query | string |  | 是否启用 Cash+ 作为抵押品<br><br>`yes` 启用<br><br>`no` 禁用 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | string |  | 操作结果 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": "success"
}
```

## 获取抵押品模式

`GET /api/v3/account/collateral-type`

限频规则: 10次/秒/UID

需要统一账户管理只读权限

查询当前统一账户的抵押品模式设置。抵押品模式分为主流币、全部币种和自定义。主流币模式下支持 USDT、USDC、BTC、DOGE、ETH、SOL 作为抵押品；自定义模式下用户可自行指定生效的抵押品币种。

Operation ID: `assetsBalanceGetCollateralType`

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.collateralType | string |  | 抵押品模式<br><br>`mainstream` 主流币<br><br>`all` 全部币种<br><br>`custom` 自定义 |
| data.collateralCoins | string |  | 抵押品币种<br><br>仅 `collateralType=custom` 自定义模式返回，多个币种之间使用英文逗号分隔 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": {
    "collateralType": "custom",
    "collateralCoins": "BTC,ETH,USDT"
  }
}
```

## 获取自定义抵押品支持币种

`GET /api/v3/account/custom-collateral-coins`

限频规则: 10次/秒/IP

查询系统支持作为自定义抵押品的所有币种。该接口为公共接口，返回平台层支持的完整列表，与用户个人配置无关。

Operation ID: `assetsBalanceGetCustomCollateralCoins`

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].collateralCoin | string |  | 抵押品币种名称 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": [
    {
      "collateralCoin": "BTC"
    },
    {
      "collateralCoin": "ETH"
    },
    {
      "collateralCoin": "USDT"
    }
  ]
}
```

## 获取账户信息

`GET /api/v3/account/info`

限频规则: 5次/秒/UID

查询账户信息，包含用户ID、邀请人、母账户、渠道、IP白名单、权限类型及权限列表。

无需任何权限

Operation ID: `accountSettingsGetAccountInfo`

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.userId | string |  | 用户ID |
| data.inviterId | string |  | 邀请人UID |
| data.parentId | string |  | 母账户UID<br><br>调用账户为子账户时，该字段有值 |
| data.channelCode | string |  | 渠道邀请码 |
| data.channel | string |  | 渠道 |
| data.ips | string |  | IP白名单 |
| data.permType | string |  | 权限类型<br><br>`read-only` 只读<br><br>`read-and-write` 读写 |
| data.permissions | string[] |  | 权限列表<br><br>`uta_mgt` 统一账户管理<br><br>`uta_trade` 统一账户交易<br><br>`withdraw` 提币<br><br>`copy_futures_position` 合约带单持仓<br><br>`copy_futures_order` 合约带单订单 |
| data.traderType | string |  | 交易员类型<br/>`trader` 交易员<br/>`not_trader` 非交易员 |
| data.regisTime | string |  | 账户注册时间（Unix时间戳，毫秒） |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1744617600000.0,
  "data": {
    "userId": "123456789",
    "inviterId": "987654321",
    "parentId": "",
    "channelCode": "6258",
    "channel": "official",
    "ips": "192.168.1.1,192.168.1.2",
    "permType": "read-and-write",
    "permissions": [
      "uta_mgt",
      "uta_trade",
      "withdraw",
      "copy_futures_position",
      "copy_futures_order"
    ],
    "traderType": "trader",
    "regisTime": "1704067200000"
  }
}
```

## 获取账户设置

`GET /api/v3/account/settings`

限频规则: 20次/秒/UID

获取账户设置信息，包含持仓模式，保证金模式，杠杆倍数等等

需要统一账户管理只读/读写权限

Operation ID: `accountSettingsGetAccountSetting`

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.uid | string |  | 用户ID |
| data.accountMode | string |  | 账户模式<br><br>`unified` 统一模式<br><br>`hybrid` 混合模式<br><br>`upgrading` 统一账户升级中<br><br>`switching` 经典账户切换中 |
| data.accountLevel | string |  | 账户等级<br><br>`basic` 稳定币保证金模式<br><br>`advanced` 多币种保证金模式<br><br>`isolated` 现货+逐仓模式<br><br>`delta` Delta中性模式 |
| data.assetMode | string |  | 资产模式<br><br>`multi_assets` 跨币种保证金模式 |
| data.holdMode | string |  | 持仓模式<br><br>`one_way_mode` 单向持仓<br><br>`hedge_mode` 双向持仓 |
| data.stpMode | string |  | [STP模式（自成交预防）](https://www.bitget.com/zh-CN/support/articles/12560603812732)<br><br>`none` 不设置STP<br><br>`cancel_taker` 取消taker单<br><br>`cancel_maker` 取消maker单<br><br>`cancel_both` 两者都取消 |
| data.deltaSwitch | string |  | Delta中性模式开关<br><br>`no` Delta中性模式关闭<br><br>`yes` Delta中性模式开启<br><br>需在多币种保证金模式下才能开启Delta中性模式 |
| data.repayMode | string |  | 还币模式<br><br>`auto` 自动还币<br><br>`manual` 手动还币 |
| data.symbolConfigList | object[] |  | 合约币对设置列表 |
| data.symbolConfigList[].category | string |  | 产品类型<br><br>`USDT-FUTURES` U本位合约<br><br>`COIN-FUTURES` 币本位合约<br><br>`USDC-FUTURES` USDC合约 |
| data.symbolConfigList[].symbol | string |  | 交易对 `BTCUSDT` |
| data.symbolConfigList[].marginMode | string |  | 保证金模式<br><br>`crossed` 全仓<br><br>`isolated` 逐仓 |
| data.symbolConfigList[].leverage | string |  | 交易对杠杆 |
| data.coinConfigList | object[] |  | 杠杆业务线币种配置信息 |
| data.coinConfigList[].coin | string |  | 币种名称 BTC |
| data.coinConfigList[].leverage | string |  | 币种杠杆 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1753787749280,
  "data": {
    "uid": "1111111111",
    "accountMode": "hybrid",
    "assetMode": "multi_assets",
    "accountLevel": "advanced",
    "holdMode": "one_way_mode",
    "stpMode": "none",
    "deltaSwitch": "no",
    "repayMode": "manual",
    "symbolConfigList": [
      {
        "category": "USDT-FUTURES",
        "symbol": "BGBUSDT",
        "marginMode": "crossed",
        "leverage": "20"
      },
      {
        "category": "USDT-FUTURES",
        "symbol": "BTCUSDT",
        "marginMode": "crossed",
        "leverage": "1"
      }
    ],
    "coinConfigList": [
      {
        "coin": "USDT",
        "leverage": "6"
      },
      {
        "coin": "BTC",
        "leverage": "3"
      }
    ]
  }
}
```

## 预设置调整杠杆

`GET /api/v3/account/pre-set-leverage`

限频规则: 10次/秒/UID

预设置指定交易对的默认杠杆倍数。该接口仅返回调整后的预计最大可开（合约）/ 最大可借（杠杆）及所需保证金等信息，并不会真正修改账户的杠杆配置。

需要统一账户管理只读权限

Operation ID: `accountSettingsPreSetLeverage`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| category | query | string | 是 | 产品类型<br><br>`MARGIN` 现货杠杆<br><br>`USDT-FUTURES` U本位合约<br><br>`COIN-FUTURES` 币本位合约<br><br>`USDC-FUTURES` USDC合约 |
| symbol | query | string |  | 交易对名称<br><br>更改合约时此参数必填 |
| coin | query | string |  | 杠杆币种<br><br>更改杠杆时此参数必填 |
| marginMode | query | string | 是 | 仓位模式<br><br>`isolated` 逐仓<br><br>`cross` 全仓 |
| leverage | query | string |  | 杠杆倍数<br><br>适用于全仓模式<br><br>适用于逐仓模式的单向持仓场景<br><br>适用于逐仓模式的双向持仓下，不同方向设置相同杠杆倍数的场景 |
| longLeverage | query | string |  | 多仓杠杆<br><br>仅适用于逐仓模式的双向持仓下，不同方向设置不同杠杆倍数的场景<br><br>双向持仓场景下，如同时传参 `leverage` 和 `longLeverage`，则 `longLeverage` 生效，`leverage` 将被忽略 |
| shortLeverage | query | string |  | 空仓杠杆<br><br>仅适用于逐仓模式的双向持仓下，不同方向设置不同杠杆倍数的场景<br><br>双向持仓场景下，如同时传参 `leverage` 和 `shortLeverage`，则 `shortLeverage` 生效，`leverage` 将被忽略 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.estMaxOpen | string |  | 调整后最大可开<br><br>合约返回此参数 |
| data.estMaxBorrowable | string |  | 调整后最大可借<br><br>杠杆返回此参数，单位为 `coin` |
| data.requiredMargin | string |  | 所需保证金，单位为 USD |
| data.marginChange | string |  | 占用保证金变化<br><br>正值为增加，负值为减少 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": {
    "estMaxOpen": "1.2345",
    "estMaxBorrowable": "100",
    "requiredMargin": "200.5",
    "marginChange": "10.5"
  }
}
```

## 调整杠杆

`POST /api/v3/account/set-leverage`

限频规则: 10次/秒/UID

调整杠杆倍数

需要统一账户管理读写权限

Operation ID: `accountSettingsChangeLeverage`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| category | string | 是 | 产品类型<br><br>`MARGIN` 现货杠杆<br><br>`USDT-FUTURES` U本位合约<br><br>`COIN-FUTURES` 币本位合约<br><br>`USDC-FUTURES` USDC合约 |
| symbol | string |  | 交易币对（更改合约时 此参数必填） |
| leverage | string |  | 杠杆倍数 |
| coin | string |  | 杠杆币种（更改杠杆时 此参数必填） |
| posSide | string |  | 仓位方向（逐仓时 此参数必填）<br><br>`long` 多仓<br><br>`short` 空仓 |
| marginMode | string |  | 仓位模式<br><br>`crossed` 全仓<br><br>`isolated` 逐仓<br><br>如不填写则默认为全仓模式。本期仅合约业务线支持调整逐仓模式杠杆。 |
| longLeverage | string |  | 多仓杠杆<br><br>仅适用于逐仓模式的双向持仓下，不同方向设置不同杠杆倍数的场景。<br><br>双向持仓场景下，如同时传参 `leverage` 和 `longLeverage`，则 `longLeverage` 生效，`leverage` 将被忽略。 |
| shortLeverage | string |  | 空仓杠杆<br><br>仅适用于逐仓模式的双向持仓下，不同方向设置不同杠杆倍数的场景。<br><br>双向持仓场景下，如同时传参 `leverage` 和 `shortLeverage`，则 `shortLeverage` 生效，`leverage` 将被忽略。 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | string |  | 操作结果 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1728625799912,
  "data": "success"
}
```

## 调整持仓模式

`POST /api/v3/account/set-hold-mode`

限频规则: 10次/秒/UID

调整持仓模式，支持单向持仓与双向持仓之间切换。

需要统一账户管理读写权限

Operation ID: `accountSettingsChangePositionMode`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| holdMode | string | 是 | 持仓模式<br><br>`one_way_mode` 单向持仓，这种模式允许持有单一方向的仓位，要么是多头，要么是空头，但不能同时持有两者。<br><br>`hedge_mode` 双向持仓，这种模式允许同时持有多头和空头仓位 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | string |  | 操作结果 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1728625799912,
  "data": "success"
}
```

## 设置BGB抵扣

`POST /api/v3/account/switch-deduct`

限频规则: 1次/秒/UID

目前仅现货交易支持BGB抵扣，合约交易暂不支持

需要统一账户管理读写权限

Operation ID: `accountSettingsSwitchDeduct`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| deduct | string | 是 | 是否开启<br><br>`on` 开启<br><br>`off` 关闭 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | boolean |  | 操作结果 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1728625799912,
  "data": true
}
```

## 获取BGB抵扣状态

`GET /api/v3/account/deduct-info`

限频规则: 1次/秒/UID

获取BGB抵扣状态

需要统一账户管理只读/读写权限

Operation ID: `accountSettingsGetDeductInfo`

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.deduct | string |  | 是否开启<br><br>`on` 开启<br><br>`off` 关闭 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1746687063471,
  "data": {
    "deduct": "on"
  }
}
```

## 账户切换

`POST /api/v3/account/switch`

限频规则: 1次/秒/UID

1. 仅母账户可调用此接口

2. 接口仅用于切换至经典账户模式

3. 请注意，由于账户切换处理需要约1分钟时间，您收到的成功响应仅表示请求已接收，并不代表账户已成功切换至经典账户

4. 请使用查询切换状态接口，确认账户切换是否成功

Operation ID: `accountSettingsSwitchAccount`

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data |  |  | 无返回数据 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1728625799912,
  "data": null
}
```

## 获取切换状态

`GET /api/v3/account/switch-status`

限频规则: 5次/秒/UID

母账户可调用此接口

Operation ID: `accountSettingsGetSwitchStatus`

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.status | string |  | 账户切换状态<br><br>`process` 处理中<br><br>`success` 成功<br><br>`fail` 失败 |
| data.reason | string |  | 失败原因<br><br>仅 `status=fail` 时返回，其余情况下为空 |

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

## 调整保证金

`POST /api/v3/account/set-margin`

限频规则: 10次/秒/UID

调整逐仓保证金数量

需要统一账户管理读写权限

Operation ID: `accountSettingsSetMargin`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| category | string | 是 | 业务线<br><br>`USDT-FUTURES` U本位合约<br><br>`COIN-FUTURES` 币本位合约<br><br>`USDC-FUTURES` USDC合约 |
| symbol | string | 是 | 交易对名称 |
| posSide | string | 是 | 仓位方向<br><br>`long` 多仓<br><br>`short` 空仓 |
| operation | string | 是 | 调整动作<br><br>`add` 增加<br><br>`remove` 移除 |
| amount | string | 是 | 保证金调整数量，单位为保证金币种<br><br>U本位合约单位为USDT，USDC合约单位为USDC，币本位合约单位为左币 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | string |  | 操作结果 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1728625799912,
  "data": "success"
}
```

## 获取Delta模式信息

`GET /api/v3/account/delta-info`

限频规则: 20次/秒/UID

获取账户Delta中性模式下的信息，包含Delta权益比率和各币种合约净头寸比例。仅在账户开启Delta中性开关（`deltaSwitch`）时可用。开启Delta中性模式前，需先将账户切换至多币种保证金模式。

需要统一账户管理只读/读写权限

Operation ID: `accountSettingsGetDeltaInfo`

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.deltaEquityRatio | string |  | （废弃，不再作为对冲条件判断依据）Delta权益比率（小数形式，如 `0.2` 代表20%）<br><br>≤ 20%：账户处于中性状态，若仓位同时满足对冲条件，该账户合约仓位自动减仓（ADL）排序靠后，被减仓的概率更低<br><br>> 20%：账户非中性状态，该账户合约仓位将按正常规则参与自动减仓（ADL）排序 |
| data.deltaThreshold | string |  | （废弃，不再作为对冲条件判断依据）Delta权益比率阈值。`deltaThreshold` 和 `positionThreshold` 均小于阈值时，允许当前账户进入ADL优先队列，否则仍处于普通队列 |
| data.positionThreshold | string |  | 币种净头寸比例阈值 |
| data.list | object[] |  | 币种持仓列表 |
| data.list[].coin | string |  | 币种名称 |
| data.list[].positionRatio | string |  | 币种净头寸比例。只要账户开启Delta中性开关（`deltaSwitch`）即有值 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": {
    "deltaEquityRatio": "0.15",
    "deltaThreshold": "0.2",
    "positionThreshold": "0.05",
    "list": [
      {
        "coin": "BTC",
        "positionRatio": "0.03"
      }
    ]
  }
}
```

## 账户模式切换

`POST /api/v3/account/adjust-account-mode`

限频规则: 1次/秒/UID

该接口支持如下账户模式切换场景。支持统一账户下的稳定币保证金模式及多币种保证金模式间切换

1. 母账户自身切换模式

2. 子账户自身切换模式

3. 母账户为其子账户切换模式

Operation ID: `accountSettingsAdjustAccountMode`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| mode | string | 是 | 账户模式<br><br>`basic` 稳定币保证金模式<br><br>`advanced` 多币种保证金模式<br><br>`delta` Delta中性模式（废弃，请使用`advanced`模式配合`deltaSwitch`开关）<br><br>`isolated` 现货+逐仓模式 |
| deltaSwitch | string |  | Delta中性开关，仅在`mode`为`advanced`时生效<br><br>开启Delta中性模式前，账户需先处于多币种保证金模式<br><br>`yes` 开启<br><br>`no` 关闭 |
| targetUid | string |  | 目标账户UID<br><br>若不传，默认为当前操作账户<br><br>若传子账户UID，则为母账户操作子账户 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data |  |  | 无返回数据 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1728625799912,
  "data": null
}
```

## 获取可还币种

`GET /api/v3/account/repayable-coins`

限频规则: 10次/秒/UID

获取可还款币种及可还数量信息

需要统一账户管理只读/读写权限

Operation ID: `marginBorrowGetRepayableCoins`

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.repayableCoinList | object[] |  | 可还币种列表 |
| data.repayableCoinList[].coin | string |  | 可还币种 |
| data.repayableCoinList[].size | string |  | 可还币种数量 |
| data.repayableCoinList[].amount | string |  | 可还币种金额（USD） |
| data.maxSelection | string |  | 最大可选取币种数量 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1730189435812,
  "data": {
    "repayableCoinList": [
      {
        "coin": "USDT",
        "size": "147214.04781004",
        "amount": "147102.60677584"
      }
    ],
    "maxSelection": "1"
  }
}
```

## 获取支付币种

`GET /api/v3/account/payment-coins`

限频规则: 10次/秒/UID

获取支付币种及可支付数量信息

需要统一账户管理只读/读写权限

Operation ID: `marginBorrowGetPaymentCoins`

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.paymentCoinList | object[] |  | 支付币种列表 |
| data.paymentCoinList[].coin | string |  | 支付币种 |
| data.paymentCoinList[].size | string |  | 支付数量 |
| data.paymentCoinList[].amount | string |  | 支付金额（USD） |
| data.maxSelection | string |  | 最大可选取币种数量 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1730189435812,
  "data": {
    "paymentCoinList": [
      {
        "coin": "ETH",
        "size": "0.12",
        "amount": "293.5"
      }
    ],
    "maxSelection": "1"
  }
}
```

## 还款

`POST /api/v3/account/repay`

限频规则: 5次/秒/UID

支持通过可还币种兑换待还币种的还款操作

需要统一账户管理读写权限

Operation ID: `marginBorrowRepay`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| repayableCoinList | string[] | 是 | 可还币种列表 |
| paymentCoinList | string[] | 是 | 支付币种列表 |

```json
{
  "repayableCoinList": [
    "USDT"
  ],
  "paymentCoinList": [
    "ETH"
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
| data.result | string |  | 还款结果<br><br>`YES`/`NO` |
| data.repayAmount | string |  | 还款金额 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1728625799912,
  "data": {
    "result": "YES",
    "repayAmount": "4345"
  }
}
```

## 获取兑换记录

`GET /api/v3/account/convert-records`

限频规则: 20次/秒/UID

获取最近90天兑换记录

需要统一账户管理只读/读写权限

Operation ID: `marginBorrowGetConvertRecords`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| fromCoin | query | string |  | 兑换币种 eg: USDT<br><br>它指的是被转换的币种 |
| toCoin | query | string |  | 目标币种 eg: BTC<br><br>它指的是被转换成的（接收的）币种 |
| startTime | query | string |  | 开始时间戳<br><br>Unix时间戳的毫秒数格式，如 1597026383085<br><br>最大查询范围90天 |
| endTime | query | string |  | 结束时间戳<br><br>Unix时间戳的毫秒数格式，如 1597026383085<br><br>`startTime`和`endTime`间隔不超过30天 |
| limit | query | string |  | 每页查询条数<br><br>最大`100`，默认`100` |
| cursor | query | string |  | 分页游标<br><br>用于翻页，首次查询不传，查询第二页及后面的数据时，取上一次查询返回cursor |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.list | object[] |  | 兑换记录列表 |
| data.list[].fromCoin | string |  | 兑换币种<br><br>它指的是被转换的币种 |
| data.list[].fromCoinSize | string |  | 兑换币种数量 |
| data.list[].toCoin | string |  | 目标币种<br><br>它指的是被转换成的（接收的）币种 |
| data.list[].toCoinSize | string |  | 目标币种数量 |
| data.list[].price | string |  | 兑换时价格 |
| data.list[].ts | string |  | 闪兑记录生成时间, ms |
| data.cursor | string |  | 分页游标 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1730369634178,
  "data": {
    "list": [
      {
        "fromCoin": "USDT",
        "fromCoinSize": "281.72276656",
        "toCoin": "ETH",
        "toCoinSize": "0.0986029682",
        "price": "0.0003499",
        "ts": "1730359119358"
      },
      {
        "fromCoin": "USDT",
        "fromCoinSize": "3305.13434913",
        "toCoin": "ETH",
        "toCoinSize": "1.1567970221",
        "price": "0.00035",
        "ts": "1730359063138"
      }
    ],
    "cursor": "1235780967957364737"
  }
}
```

## 手动借币

`POST /api/v3/account/borrow`

限频规则: 1次/秒/UID

主动借入指定币种指定数量。仅支持多币种保证金模式或Delta 中性模式，并且在手动还币模式下可用。

需要统一账户交易权限

Operation ID: `marginBorrowBorrow`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| coin | string | 是 | 借入币种<br><br>需为 UTA 支持的借贷币种 |
| amount | string | 是 | 借入数量 |
| clientOid | string |  | 自定义借币订单 ID |

```json
{
  "coin": "USDT",
  "amount": "100"
}
```

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.orderId | string |  | 借币订单 ID |
| data.clientOid | string |  | 自定义借币订单 ID |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1758512000000.0,
  "data": {
    "orderId": "1234567890",
    "clientOid": "myClientOid001"
  }
}
```

## 查询最大可借

`GET /api/v3/account/max-borrowable`

限频规则: 10次/秒/UID

查询各币种当前最大可借数量。

需要统一账户管理只读权限

Operation ID: `marginBorrowGetMaxBorrowable`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| coin | query | string | 是 | 币种 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.maxBorrowable | string |  | 最大手动可借 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1758512000000.0,
  "data": {
    "maxBorrowable": "10000"
  }
}
```

## 还币模式设置

`POST /api/v3/account/set-repay-mode`

限频规则: 1次/秒/UID

该接口用于设置手动借贷的还币模式，支持手动及自动还币。

需要统一账户管理读写权限

Operation ID: `marginBorrowSetRepayMode`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| repayMode | string | 是 | 还币模式<br><br>`auto` 自动还币<br><br>`manual` 手动还币<br><br>账户（UID）级配置，不按币种区分；主账户与每个子账户各自独立维护，互不继承、互不联动 |

```json
{
  "repayMode": "manual"
}
```

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  | 无返回字段 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1758512000000.0,
  "data": {}
}
```

## 获取OI限仓

`GET /api/v3/account/open-interest-limit`

限频规则: 5次/秒/UID

OI限仓查询

Operation ID: `riskPositionGetOiLimit`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | 交易对名称<br><br>如`BTCUSDT` |
| category | query | string | 是 | 业务线<br><br>`USDT-FUTURES` USDT合约<br><br>`COIN-FUTURES` 币本位合约<br><br>`USDC-FUTURES` USDC合约 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.symbol | string |  | 交易对名称 |
| data.singleUserLimit | string |  | 单用户限制数量 |
| data.masterSubLimit | string |  | 子母账户限制数量 |
| data.marketMakerLimit | string |  | 做市商总额度 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1764170997805,
  "data": {
    "symbol": "BTCUSDT",
    "singleUserLimit": "2766.30748",
    "masterSubLimit": "9173.8782",
    "marketMakerLimit": "0"
  }
}
```

## 获取业务线所有交易对手续费

`GET /api/v3/account/all-fee-rate`

限频规则: 3次/秒/UID

需要统一账户管理只读权限

查询指定业务线下所有交易对的手续费率。

- 仅传业务线 `category`，不传交易对 `symbol`：返回该业务线下所有交易对的手续费

- 仅传交易对 `symbol`，不传业务线 `category`：接口报错

- `category` 和 `symbol` 均传：返回指定业务线下指定交易对的手续费。若 `category` 和 `symbol` 不一致，以 `symbol` 为准

- `category` 和 `symbol` 均不传：接口报错

Operation ID: `riskPositionGetAllFeeRate`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| category | query | string | 是 | 业务线<br><br>`SPOT` 现货交易<br><br>`MARGIN` 杠杆交易<br><br>`USDT-FUTURES` USDT合约<br><br>`COIN-FUTURES` 币本位合约<br><br>`USDC-FUTURES` USDC合约 |
| symbol | query | string |  | 交易对名称<br><br>如`BTCUSDT` |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].symbol | string |  | 交易对名称 |
| data[].makerFeeRate | string |  | 挂单手续费率<br><br>小数形式，即0.0002代表万分之二 |
| data[].takerFeeRate | string |  | 吃单手续费率<br><br>小数形式，即0.0002代表万分之二 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1751972326323,
  "data": [
    {
      "symbol": "BTCUSDT",
      "makerFeeRate": "0.0008",
      "takerFeeRate": "0.0008"
    }
  ]
}
```

## 获取准入用户杠杆交易对

`GET /api/v3/account/eligible-symbols`

限频规则: 10次/秒/UID

需要统一账户管理只读权限

查询准入用户（白名单用户）可交易的全部杠杆交易对。

Operation ID: `riskPositionGetEligibleSymbols`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string |  | 交易对名称<br><br>例如：`BTCUSDT` |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].symbol | string |  | 交易对名称 |
| data[].category | string |  | 产品类型<br><br>`MARGIN` 杠杆交易 |
| data[].baseCoin | string |  | 交易币种<br><br>例如：`BTCUSDT` 中的 `BTC` |
| data[].quoteCoin | string |  | 计价币种<br><br>例如：`BTCUSDT` 中的 `USDT` |
| data[].symbolType | string |  | 交易对类别<br><br>`crypto` 加密货币<br><br>`metal` 贵金属<br><br>`stock` 股票<br><br>`commodity` 大宗 |
| data[].buyLimitPriceRatio | string |  | 买价限价比例<br><br>买入限价与市场价格的比率，决定买单下单时的最高价格 |
| data[].sellLimitPriceRatio | string |  | 卖价限价比例<br><br>卖出限价与市场价格的比率，决定卖单下单时的最低价格 |
| data[].minOrderQty | string |  | 最小开单数量<br><br>以基础币种下单时允许的最小数量 |
| data[].maxOrderQty | string |  | 单笔限价单最大下单数量<br><br>以基础币种下单时允许的最大数量<br><br>为 0 表示不限制 |
| data[].pricePrecision | string |  | 价格精度<br><br>价格允许的小数位数 |
| data[].quantityPrecision | string |  | 数量精度<br><br>数量允许的小数位数 |
| data[].quotePrecision | string |  | 市价下单精度<br><br>计价币价格允许的小数位数 |
| data[].minOrderAmount | string |  | 最小下单额<br><br>以计价币种下单时允许的最小数量 |
| data[].maxSymbolOrderNum | string |  | 交易对维度最大委托数量 |
| data[].maxProductOrderNum | string |  | 业务线维度最大委托数量 |
| data[].status | string |  | 交易对状态<br><br>`listed` 上架（未开盘）<br><br>`online` 正常交易<br><br>`limit_open` 限制开仓<br><br>`limit_close` 限制平仓<br><br>`offline` 下架/维护<br><br>`restrictedAPI` API限制下单 |
| data[].maintainTime | string |  | 币对维护时间<br><br>未配置则返回："" |
| data[].areaSymbol | string |  | 区域限制标识<br><br>`yes` / `no` |
| data[].maxPositionNum | string |  | 交易对维度最大持仓数量 |
| data[].isReality | string |  | Reality 标识<br><br>`yes` Reality 股票代币<br><br>`no` 非 Reality 股票代币 |
| data[].launchTime | string |  | 上线时间<br><br>Unix毫秒时间戳，表示交易对的上线时间 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1784618341109,
  "data": [
    {
      "symbol": "RPBRUSDT",
      "category": "MARGIN",
      "baseCoin": "rPBR",
      "quoteCoin": "USDT",
      "symbolType": "stock",
      "buyLimitPriceRatio": "0.1",
      "sellLimitPriceRatio": "0.1",
      "minOrderQty": "0.0001",
      "maxOrderQty": "0",
      "pricePrecision": "2",
      "quantityPrecision": "4",
      "quotePrecision": "6",
      "minOrderAmount": "20",
      "maxSymbolOrderNum": "",
      "maxProductOrderNum": "400",
      "status": "online",
      "maintainTime": "",
      "areaSymbol": "yes",
      "maxPositionNum": "200",
      "isReality": "yes",
      "launchTime": "1781101641926"
    }
  ]
}
```

## 获取准入用户杠杆梯度档位

`GET /api/v3/account/eligible-margin-tier`

限频规则: 10次/秒/UID

需要统一账户管理只读权限

根据用户的准入情况返回杠杆梯度档位信息。

Operation ID: `riskPositionGetEligibleMarginTier`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| coin | query | string |  | 币种名称<br><br>例如：`BTC` |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].coin | string |  | 币种名称 |
| data[].tiers | object[] |  | 档位列表 |
| data[].tiers[].tier | string |  | 档位 |
| data[].tiers[].minTierValue | string |  | 当前档位最小价值 |
| data[].tiers[].maxTierValue | string |  | 当前档位最大价值 |
| data[].tiers[].leverage | string |  | 有效杠杆倍数 |
| data[].tiers[].mmr | string |  | 维持保证金率 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1784618341109,
  "data": [
    {
      "coin": "BTC",
      "tiers": [
        {
          "tier": "1",
          "minTierValue": "0",
          "maxTierValue": "50000",
          "leverage": "10",
          "mmr": "0.05"
        }
      ]
    }
  ]
}
```

## 获取准入用户借币数据

`GET /api/v3/account/eligible-loan-info`

限频规则: 10次/秒/UID

需要统一账户管理只读权限

根据用户的准入情况返回借币数据信息。

Operation ID: `riskPositionGetEligibleLoanInfo`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| coin | query | string |  | 币种名称<br><br>例如：`BTC` |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].limit | string |  | 单UID借币上限 |
| data[].masterSubLimit | string |  | 母子账户借币上限 |
| data[].platformRemaingQuota | string |  | 平台剩余额度 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1784618341109,
  "data": [
    {
      "limit": "100000",
      "masterSubLimit": "500000",
      "platformRemaingQuota": "10000000"
    }
  ]
}
```

## 获取准入用户币种折扣率梯度

`GET /api/v3/account/eligible-discount-rate`

限频规则: 20次/秒/UID

需要统一账户管理只读权限

根据用户的准入情况返回币种折扣率梯度信息。

Operation ID: `riskPositionGetEligibleDiscountRate`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| coin | query | string |  | 币种名称<br><br>例如：`BTC` |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].coin | string |  | 币种名称 |
| data[].list | object[] |  | 档位列表 |
| data[].list[].tierStartValue | string |  | 档位起始价值<br><br>例如：[0,10000 U): tierStartValue=0<br><br>[10000 U,20000 U): tierStartValue=10000<br><br>[20000 U,∞): tierStartValue=20000 |
| data[].list[].discountRate | string |  | 折扣率 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1730911874605,
  "data": [
    {
      "coin": "BTC",
      "list": [
        {
          "tierStartValue": "0",
          "discountRate": "0.85"
        },
        {
          "tierStartValue": "10000",
          "discountRate": "0.70"
        },
        {
          "tierStartValue": "20000",
          "discountRate": "0.50"
        }
      ]
    }
  ]
}
```

## 新建子账户

`POST /api/v3/user/create-sub`

限频规则: 10次/秒/UID

该接口用于母账户创建子账户，仅支持创建统一账户虚拟子账户，不支持创建普通子账户。

需要统一账户管理读写权限

仅母账户才能调用此接口

Operation ID: `subAccountsCreateSubAccount`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| username | string | 是 | 生成虚拟邮箱地址的用户名。只能是小写字母且不能超过20个字符 |
| accountMode | string |  | 子账户模式<br><br>`classic` 经典账户子账户<br><br>`unified` 统一账户子账户 |
| note | string |  | 备注，不能超过50个字符 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.username | string |  | 虚拟邮箱地址 |
| data.subUid | string |  | 虚拟子账户ID |
| data.status | string |  | 账户状态<br><br>`normal` 正常 |
| data.note | string |  | 备注 |
| data.createdTime | string |  | 创建时间，Unix毫秒时间戳 |
| data.updatedTime | string |  | 最后修改时间，Unix毫秒时间戳 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740211442920,
  "data": {
    "username": "xxxx@virtual-bitget.com",
    "subUid": "xxxx",
    "status": "normal",
    "note": "xxxx",
    "createdTime": "1740211445041",
    "updatedTime": "1740211445041"
  }
}
```

## 删除子账户

`POST /api/v3/user/delete-sub`

限频规则: 10次/秒/UID

删除子账户。

- **子账户类型**：本期仅支持删除虚拟子账户和普通子账户，不支持其他类型子账户。
- **资产校验**：所有业务线账户总资产不超过10U才可以删除，否则不允许删除。
- **开户校验**：MT5开户过的子账户不允许删除。
- **订单校验**：子账户不能有在途订单（统一账户，现货，合约，杠杆，理财，策略）。

需要统一账户管理读写权限

仅母账户才能调用此接口

Operation ID: `subAccountsDeleteSubAccount`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| subUid | string | 是 | 删除子账户 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  | 无返回字段 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1758512000000.0,
  "data": {}
}
```

## 冻结/解冻子账户

`POST /api/v3/user/freeze-sub`

限频规则: 10次/秒/UID

冻结/解冻虚拟子账户。

需要统一账户管理读写权限

仅母账户才能调用此接口

Operation ID: `subAccountsFreezeSubAccount`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| subUid | string | 是 | 要冻结/解冻的子账户ID |
| operation | string | 是 | 操作类型<br><br>`freeze` 冻结<br><br>`unfreeze` 解冻 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  | 无返回字段 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740212117457,
  "data": {}
}
```

## 查询子账户列表

`GET /api/v3/user/sub-list`

限频规则: 10次/秒/UID

查询子账户列表。

需要统一账户管理读取权限

仅母账户才能调用此接口

Operation ID: `subAccountsGetSubAccountList`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| limit | query | string |  | 每页条目数<br><br>默认值为100，最大值为100 |
| cursor | query | string |  | 游标ID<br><br>用于翻页，首次查询不传，查询第二页及后面的数据时，取上一次查询返回的cursor |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.list | object[] |  | 子账户列表 |
| data.list[].username | string |  | 子账户邮箱地址 |
| data.list[].subUid | string |  | 子账户ID |
| data.list[].status | string |  | 账户状态<br><br>`normal` 正常<br><br>`frozen` 冻结 |
| data.list[].accountMode | string |  | 账户模式<br><br>`CLASSIC` 经典账户模式<br><br>`UNIFIED` 统一账户模式 |
| data.list[].type | string |  | 账户类型<br><br>`normal` 普通子账户<br><br>`virtual` 虚拟子账户<br><br>`custodian` 交易托管子账户<br><br>`fund_management` 资金托管子账户<br><br>`agent` Agent子账户<br><br>`other` 其他 |
| data.list[].note | string |  | 备注 |
| data.list[].createdTime | string |  | 子账户创建时间，Unix毫秒时间戳 |
| data.list[].updatedTime | string |  | 子账户修改时间，Unix毫秒时间戳 |
| data.hasNext | boolean |  | 是否还有下一页数据 |
| data.cursor | string |  | 游标ID |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740212430491,
  "data": {
    "list": [
      {
        "subUid": "xxx",
        "username": "llt****@virtual-bitget.com",
        "status": "normal",
        "accountMode": "CLASSIC",
        "type": "virtual",
        "note": "xxxx",
        "createdTime": "1740129303268",
        "updatedTime": "1740129303268"
      },
      {
        "subUid": "xxx",
        "username": "zml****@virtual-bitget.com",
        "status": "normal",
        "accountMode": "UNIFIED",
        "type": "virtual",
        "note": "xxx",
        "createdTime": "1740211445018",
        "updatedTime": "1740211445018"
      },
      {
        "subUid": "xxx",
        "username": "tmr****@virtual-bitget.com",
        "status": "freeze",
        "accountMode": "UNIFIED",
        "type": "virtual",
        "note": "xxx",
        "createdTime": "1740131800692",
        "updatedTime": "1740212129476"
      }
    ],
    "hasNext": false,
    "cursor": "18484"
  }
}
```

## 查询子账户统一账户资产

`GET /api/v3/account/sub-unified-assets`

限频规则: 1次/秒/UID

查询子账户统一账户资产。

需要统一账户管理读取权限

Operation ID: `subAccountsGetSubAccountUnifiedAssets`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| subUid | query | string |  | 子账户UID<br><br>如不填，则返回所有子账户资产列表 |
| cursor | query | string |  | 游标ID<br><br>用于翻页，首次请求不传。后续请求传上次返回的cursor值 |
| limit | query | string |  | 每页子账户数量<br><br>默认值为10，最大值为50 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  | 子账户资产列表 |
| data[].subUid | string |  | 子账户UID |
| data[].cursor | string |  | 游标ID |
| data[].assets | object[] |  | 账户币种列表 |
| data[].assets[].coin | string |  | 资产币种 |
| data[].assets[].equity | string |  | 资产币种权益<br><br>单位为资产币种 |
| data[].assets[].usdValue | string |  | 资产币种折U价值<br><br>单位为USD |
| data[].assets[].balance | string |  | 资产币种余额 |
| data[].assets[].available | string |  | 资产币种可用 |
| data[].assets[].debt | string |  | 资产币种负债 |
| data[].assets[].locked | string |  | 下单占用<br><br>仅现货下单场景有值 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1751970047603,
  "data": [
    {
      "subUid": "1111111111",
      "cursor": "5832862",
      "assets": [
        {
          "coin": "USDT",
          "equity": "1",
          "usdValue": "0.99996985",
          "balance": "1",
          "available": "1",
          "debt": "0",
          "locked": "0"
        }
      ]
    }
  ]
}
```

## 新建子账户API Key

`POST /api/v3/user/create-sub-api`

限频规则: 10次/秒/UID

该接口用于新建统一账户子账户的API Key，即母账户为混合账户模式或统一账户模式。如当前母账户模式为经典账户，则无法调用该接口。

支持的子账户类型：虚拟子账户、Copper 托管子账户、普通子账户。普通子账户需已是统一账户模式；若该子账户为经典账户模式，接口将返回错误，提示该子账户不支持创建 Key。

需要统一账户管理读写权限

仅母账户才能调用此接口

Operation ID: `subAccountsCreateSubAccountApiKey`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| subUid | string | 是 | 子账户ID<br><br>现已支持传入普通子账户 UID，除虚拟子账户和 Copper 托管子账户外 |
| note | string | 是 | 备注名称<br><br>长度限制20字符；需以字母开头，支持[0-9], [a-z], [A-Z]以及[-,_] |
| type | string | 是 | 权限类型<br><br>`read_write` 读写<br><br>`read_only` 只读 |
| passphrase | string | 是 | 密钥<br><br>长度为8至32位的英文字母与数字组合 |
| permissions | string[] | 是 | 权限值<br><br>统一账户权限：<br><br>`uta_mgt` 统一账户管理<br><br>`uta_trade` 统一账户交易 |
| ips | string[] | 是 | 提币白名单IP<br><br>支持传入多个IP地址<br><br>单密钥最多支持绑定30个IP<br><br>只支持IPv4 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.note | string |  | 备注 |
| data.apiKey | string |  | 子账户api key |
| data.secret | string |  | 子账户密钥 |
| data.type | string |  | 子账户API Key权限类型<br><br>`read_write` 读写<br><br>`read_only` 只读 |
| data.permissions | string[] |  | 子账户API Key权限值<br><br>统一账户权限：<br><br>`uta_mgt` 统一账户管理<br><br>`uta_trade` 统一账户交易 |
| data.ips | string[] |  | 子账户提币IP白名单列表 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740213448866,
  "data": {
    "note": "test",
    "apiKey": "***********************************",
    "secret": "*********************************************",
    "type": "read_only",
    "permissions": [
      "uta_trade"
    ],
    "ips": [
      "127.0.0.1"
    ]
  }
}
```

## 修改子账户API Key

`POST /api/v3/user/update-sub-api`

限频规则: 10次/秒/UID

该接口用于修改统一账户子账户API Key权限及提币白名单IP地址。仅支持修改统一账户子账户的API Key，不支持创建经典账户子账户的API Key。

需要统一账户管理读写权限

仅母账户才能调用此接口

Operation ID: `subAccountsUpdateSubAccountApiKey`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| apiKey | string | 是 | 子账户API Key |
| passphrase | string | 是 | 密钥<br><br>长度为8至32位的英文字母与数字组合 |
| type | string |  | 权限类型<br><br>`read_write` 读写<br><br>`read_only` 只读<br><br>`permissions`有值时此参数必传 |
| permissions | string[] |  | 权限值<br><br>统一账户权限：<br><br>`uta_mgt` 统一账户管理<br><br>`uta_trade` 统一账户交易<br><br>`type`有值时此参数必传 |
| ips | string[] |  | 白名单IP<br><br>如不传，则不修改IP地址<br><br>如传空值，则删除IP白名单<br><br>支持传入多个IP地址<br><br>单密钥最多支持绑定30个IP<br><br>只支持IPv4 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.apiKey | string |  | 子账户api密钥 |
| data.note | string |  | 备注 |
| data.type | string |  | 子账户API Key权限类型<br><br>`read_write` 读写<br><br>`read_only` 只读 |
| data.permissions | string[] |  | 子账户API Key权限值<br><br>统一账户权限：<br><br>`uta_mgt` 统一账户管理<br><br>`uta_trade` 统一账户交易 |
| data.ips | string[] |  | 子账户IP白名单列表 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740213448866,
  "data": {
    "note": "test",
    "apiKey": "***********************************",
    "type": "read_only",
    "permissions": [
      "uta_trade"
    ],
    "ips": [
      "127.0.0.1"
    ]
  }
}
```

## 删除子账户API Key

`POST /api/v3/user/delete-sub-api`

限频规则: 10次/秒/UID

该接口用于母账户删除子账户的API Key，不适用于母账户或子账户删除其调用API Key的场景。

请注意，删除操作一旦完成，子账户API Key将立即失效。在执行删除前，请务必确认此操作不会导致任何损失。

该接口仅支持删除统一账户子账户的API Key，不支持删除经典账户子账户的API Key。

需要统一账户管理读写权限

仅母账户才能调用此接口

Operation ID: `subAccountsDeleteSubAccountApiKey`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| apiKey | string | 是 | 子账户API Key |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  | 无返回字段 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740213448866,
  "data": {}
}
```

## 查询子账户API Key列表

`GET /api/v3/user/sub-api-list`

限频规则: 10次/秒/UID

支持查询单个子账户下的全部API Key列表。

需要统一账户管理读取权限

仅母账户才能调用此接口

Operation ID: `subAccountsGetSubAccountApiKeyList`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| subUid | query | string | 是 | 子账户UID |
| limit | query | string |  | 每页条目数<br><br>默认值为100，最大值为100 |
| cursor | query | string |  | 游标ID<br><br>用于翻页，首次查询不传，查询第二页及后面的数据时，取上一次查询返回的cursor |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.list | object[] |  | 子账户API Key列表 |
| data.list[].apiKey | string |  | 子账户api密钥 |
| data.list[].note | string |  | 备注名称 |
| data.list[].type | string |  | 子账户API Key权限类型<br><br>`read_write` 读写<br><br>`read_only` 只读 |
| data.list[].permissions | string[] |  | 子账户API Key权限列表<br><br>`uta_mgt` 统一账户管理<br><br>`uta_trade` 统一账户交易 |
| data.list[].ips | string[] |  | 子账户提币IP白名单列表 |
| data.list[].ts | string |  | 创建时间（Unix毫秒时间戳） |
| data.hasNext | boolean |  | 是否还有下一页数据 |
| data.cursor | string |  | 游标ID |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740212430491,
  "data": {
    "list": [
      {
        "apiKey": "***********************************",
        "note": "xxxx",
        "type": "read_only",
        "permissions": [
          "uta_trade"
        ],
        "ips": [
          "127.0.0.1"
        ],
        "ts": "1740129303268"
      }
    ],
    "hasNext": false,
    "cursor": "18484"
  }
}
```

## 创建 Agent 子账户

`POST /api/v3/user/sub-account/agent-create`

限频规则: 1次/秒/UID

为 AI Agent 实例创建专属子账户。Agent 子账户创建后不支持编辑（名称、权限等配置均不可修改）。每个主账户可创建的 Agent 子账户数量上限与普通子账户共享总配额。

需要统一账户管理读写权限

仅母账户才能调用此接口

Operation ID: `subAccountsCreateAgentSubAccount`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| username | string | 是 | 用于生成虚拟邮箱地址的用户名。只能是小写字母且不能超过20个字符 |
| passphrase | string | 是 | API Key 密钥，长度为8至32位的英文字母与数字组合 |
| note | string |  | 子账户备注 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.username | string |  | Agent 子账户昵称 |
| data.subUid | string |  | Agent 子账户 ID |
| data.apiKey | string |  | Agent 子账户 API Key |
| data.secret | string |  | Agent 子账户密钥 |
| data.note | string |  | 备注 |
| data.createdTime | string |  | 创建时间，Unix毫秒时间戳 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": {
    "username": "xxxx@virtual-bitget.com",
    "subUid": "xxxx",
    "apiKey": "***********************************",
    "secret": "*********************************************",
    "note": "xxxx",
    "createdTime": "1740211445041"
  }
}
```

## 设置充值账户

`POST /api/v3/account/deposit-account`

限频规则: 1次/秒/UID

该配置项长期有效，即用户设置了某一个交易对的默认充值账户后长期保留，无需重复配置

需要统一账户管理读写权限

Operation ID: `depositWithdrawalSetDepositAccount`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| coin | string | 是 | 充值币种<br><br>如`BTC` |
| accountType | string | 是 | 账户类型<br><br>`funding` 资金账户<br><br>`unified` 统一账户<br><br>`otc` OTC账户<br><br>当前默认值为资金账户，支持修改为统一账户及OTC账户 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | string |  | 操作结果 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1753848186558,
  "data": "success"
}
```

## 获取充值地址

`GET /api/v3/account/deposit-address`

限频规则: 10次/秒/UID

获取充值地址

需要统一账户管理只读权限

Operation ID: `depositWithdrawalGetDepositAddress`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| coin | query | string | 是 | 币种名称<br><br>- 币种名称可以通过获取币种信息接口获取 |
| chain | query | string |  | 链名称<br><br>- 链名称可以通过获取币种信息接口获取<br><br>- 如不填，则系统会自动匹配一条链生成充值地址 |
| size | query | string |  | 充值数量<br><br>- 仅适用于BTC闪电网络<br><br>- 限制范围：0.000001 - 0.001 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.address | string |  | 充值地址 |
| data.chain | string |  | 链名称 |
| data.coin | string |  | 币种名称 |
| data.tag | string |  | 标签 |
| data.url | string |  | 区块链浏览器地址 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1730189276579,
  "data": {
    "address": "0x51xxx",
    "chain": "erc20",
    "coin": "USDT",
    "tag": null,
    "url": ""
  }
}
```

## 获取子账户充值地址

`GET /api/v3/account/sub-deposit-address`

限频规则: 10次/秒/UID

获取子账户充值地址

需要统一账户管理只读权限

Operation ID: `depositWithdrawalGetSubDepositAddress`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| subUid | query | string | 是 | 子账户UID<br><br>- 子账户UID可以通过子账户列表接口获取 |
| coin | query | string | 是 | 币种名称<br><br>- 币种名称可以通过获取币种信息接口获取 |
| chain | query | string |  | 链名称<br><br>- 链名称可以通过获取币种信息接口获取 |
| size | query | string |  | 充值数量<br><br>- 仅适用于BTC闪电网络<br><br>- 限制范围：0.000001 - 0.001 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.address | string |  | 充值地址 |
| data.chain | string |  | 链名称 |
| data.coin | string |  | 币种名称 |
| data.tag | string |  | 标签 |
| data.url | string |  | 区块链浏览器地址 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740213448866,
  "data": {
    "address": "0x51xxx",
    "chain": "erc20",
    "coin": "USDT",
    "tag": "",
    "url": ""
  }
}
```

## 获取充值记录

`GET /api/v3/account/deposit-records`

限频规则: 10次/秒/UID

获取充值记录

需要统一账户管理只读权限

Operation ID: `depositWithdrawalGetDepositRecords`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| coin | query | string |  | 币种名称<br><br>- 如不填，则获取所有币种充值记录 |
| orderId | query | string |  | 订单ID<br><br>- 用于指定订单查询 |
| startTime | query | string | 是 | 查询记录起始时间<br><br>- Unix毫秒时间戳，例如1690196141868 |
| endTime | query | string | 是 | 查询记录结束时间<br><br>- Unix毫秒时间戳，例如1690196141868 |
| limit | query | string |  | 每页条目数<br><br>默认值为20，最大值为100 |
| cursor | query | string |  | 游标ID<br><br>- 用于翻页，可缩短查询响应时间<br><br>- 首次查询不传，查询第二页及后续数据时，取上一次查询返回的最小orderId，结果会返回小于该值的数据 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  | 充值记录列表 |
| data[].orderId | string |  | 订单ID |
| data[].recordId | string |  | 充值记录ID<br><br>- 如果`dest`为`on_chain`，则为链上哈希值<br><br>- 如果`dest`为`internal_transfer`，则为订单ID |
| data[].coin | string |  | 币种名称 |
| data[].type | string |  | 操作类型<br><br>`deposit` 充值 |
| data[].dest | string |  | 充值类型<br><br>`on_chain` 链上充值<br><br>`internal_transfer` 内部转账 |
| data[].size | string |  | 充值数量 |
| data[].status | string |  | 充值状态<br><br>`pending` 确认中<br><br>`success` 成功<br><br>`fail` 失败 |
| data[].fromAddress | string |  | 充值发起方<br><br>- 如果`dest`为`on_chain`，则为链上地址<br><br>- 如果`dest`为`internal_transfer`，则为`uid`, `email`或者`mobile` |
| data[].toAddress | string |  | 充值接收方<br><br>- 如果`dest`为`on_chain`，则为链上地址<br><br>- 如果`dest`为`internal_transfer`，则为`uid`, `email`或者`mobile` |
| data[].chain | string |  | 充值网络<br><br>- `dest`为`internal_transfer`时可忽略此参数 |
| data[].createdTime | string |  | 充值记录创建时间，Unix毫秒时间戳 |
| data[].updatedTime | string |  | 充值记录更新时间，Unix毫秒时间戳 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740481864545,
  "data": [
    {
      "orderId": "1278112570963742720",
      "recordId": "1278112570963742720",
      "coin": "usdt",
      "type": "deposit",
      "dest": "internal_transfer",
      "size": "1",
      "status": "success",
      "fromAddress": "0x51xxx",
      "toAddress": "0x51xxx",
      "chain": "erc20",
      "createdTime": "1740451703778",
      "updatedTime": "1740451703778"
    }
  ]
}
```

## 获取子账户充值记录

`GET /api/v3/account/sub-deposit-records`

限频规则: 10次/秒/UID

获取子账户充值记录

需要统一账户管理只读权限

Operation ID: `depositWithdrawalGetSubDepositRecords`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| coin | query | string |  | 币种名称<br><br>- 如不填，则获取所有币种充值记录 |
| subUid | query | string | 是 | 子账户UID |
| startTime | query | string | 是 | 查询记录起始时间<br><br>- Unix毫秒时间戳，例如1690196141868 |
| endTime | query | string | 是 | 查询记录结束时间<br><br>- Unix毫秒时间戳，例如1690196141868 |
| limit | query | string |  | 每页条目数<br><br>默认值为20，最大值为100 |
| cursor | query | string |  | 游标ID<br><br>- 用于翻页，可缩短查询响应时间<br><br>- 首次查询不传，查询第二页及后续数据时，取上一次查询返回的最小orderId，结果会返回小于该值的数据 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  | 子账户充值记录列表 |
| data[].orderId | string |  | 订单ID |
| data[].recordId | string |  | 充值记录ID<br><br>- 如果`dest`为`on_chain`，则为链上哈希值<br><br>- 如果`dest`为`internal_transfer`，则为订单ID |
| data[].coin | string |  | 币种名称 |
| data[].type | string |  | 操作类型<br><br>`deposit` 充值 |
| data[].dest | string |  | 充值类型<br><br>`on_chain` 链上充值<br><br>`internal_transfer` 内部转账 |
| data[].size | string |  | 充值数量 |
| data[].status | string |  | 充值状态<br><br>`pending` 确认中<br><br>`success` 成功<br><br>`fail` 失败 |
| data[].fromAddress | string |  | 充值发起方<br><br>- 如果`dest`为`on_chain`，则为链上地址<br><br>- 如果`dest`为`internal_transfer`，则为`uid`, `email`或者`mobile` |
| data[].toAddress | string |  | 充值接收方<br><br>- 如果`dest`为`on_chain`，则为链上地址<br><br>- 如果`dest`为`internal_transfer`，则为`uid`, `email`或者`mobile` |
| data[].chain | string |  | 充值网络<br><br>- `dest`为`internal_transfer`时可忽略此参数 |
| data[].createdTime | string |  | 充值记录创建时间，Unix毫秒时间戳 |
| data[].updatedTime | string |  | 充值记录更新时间，Unix毫秒时间戳 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1730189276579,
  "data": [
    {
      "orderId": "1278112570963742720",
      "recordId": "1278112570963742720",
      "coin": "usdt",
      "type": "deposit",
      "dest": "internal_transfer",
      "size": "1",
      "status": "success",
      "fromAddress": "0x51xxx",
      "toAddress": "0x51xxx",
      "chain": "erc20",
      "createdTime": "1740451703778",
      "updatedTime": "1740451703778"
    }
  ]
}
```

## 提币

`POST /api/v3/account/withdrawal`

限频规则: 1次/秒/UID

提币接口，包括链上提币和内部提币

需要统一账户提币权限

Operation ID: `depositWithdrawalWithdrawal`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| coin | string | 是 | 币种名称 |
| chain | string |  | 区块链网络<br><br>- 例如 `erc20`, `trc20` 等<br><br>- 当`transferType`=`on_chain`时，该参数必填<br><br>- 链名称可以通过获取币种信息接口获取 |
| transferType | string | 是 | 提币类型<br><br>`on_chain` 链上提币<br><br>`internal_transfer` 内部转账 |
| address | string | 是 | 提币地址<br><br>- 当`transferType`为`on_chain`时，填写链地址<br><br>- 当`transferType`为`internal_transfer`时，根据`innerToType`填写UID，邮箱或手机号 |
| innerToType | string |  | 内部提币地址类型<br><br>`uid` 用户ID<br><br>`email` 邮件地址<br><br>`mobile` 移动电话或者手机号<br><br>- 如不填，默认值为`uid` |
| areaCode | string |  | 地区码<br><br>`innerToType`=`mobile`时，该参数必填 |
| tag | string |  | 地址标签<br><br>部分币种提币必填，例如EOS |
| size | string | 是 | 提币数量<br><br>比特币闪电网络提币特别说明：<br><br>该参数需要填写与比特币闪电网络充值发票金额完全一致的数据；<br><br>比特币闪电网络的提币数量为到账金额，不包含手续费；<br><br>数量精度可以通过获取币种信息接口获取 |
| remark | string |  | 备注 |
| clientOid | string |  | 自定义订单ID |
| memberCode | string |  | 成员代码<br><br>`bithumb`<br><br>`korbit`<br><br>`coinone` |
| identityType | string |  | 身份类型<br><br>`company` 机构公司<br><br>`user` 普通用户 |
| companyName | string |  | 公司名称<br><br>`identity`=`company`时填写此参数 |
| firstName | string |  | 名字<br><br>`identity`=`user`时填写此参数 |
| lastName | string |  | 姓氏<br><br>`identity`=`user`时填写此参数 |
| accountType | string |  | 扣款账户类型<br><br>`funding` 资金账户<br><br>`uta` 统一账户<br><br>`otc` OTC账户<br><br>支持多选，多个账户类型用英文逗号 `,` 分隔。扣款顺序：资金账户 → OTC账户 → 统一账户 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.orderId | string |  | 提币订单ID |
| data.clientOid | string |  | 自定义提币订单ID |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1730189276579,
  "data": {
    "orderId": "111111111111",
    "clientOid": "111111111111"
  }
}
```

## 撤销提币

`POST /api/v3/account/cancel-withdrawal`

限频规则: 1次/秒/UID

对冷静期间的提币申请发起撤销操作。一旦提币冷静期结束，则无法撤销。每次撤销操作仅限单笔，不支持批量。需要具备提币权限的 API Key 方可调用。

需要提币权限（Withdraw）

Operation ID: `depositWithdrawalCancelWithdrawal`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| orderId | string |  | 提币订单 ID，`orderId` 与 `clientOid` 二选一必传，若两者均传以 `orderId` 为准 |
| clientOid | string |  | 用户自定义提币订单 ID，`orderId` 与 `clientOid` 二选一必传 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | string |  | 操作结果 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": "success"
}
```

## 获取提币记录

`GET /api/v3/account/withdrawal-records`

限频规则: 10次/秒/UID

获取提币记录

需要统一账户管理只读权限

Operation ID: `depositWithdrawalGetWithdrawalRecords`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| coin | query | string |  | 币种名称<br><br>- 如不填，则获取所有币种提币记录 |
| orderId | query | string |  | 订单ID<br><br>- 查询单笔订单时，可通过orderId与clientOid二者其一进行查询<br><br>- 若同时传入orderId与clientOid，则orderId优先级更高 |
| clientOid | query | string |  | 客户自定义ID<br><br>- 查询单笔订单时，可通过orderId与clientOid二者其一进行查询<br><br>- 若同时传入orderId与clientOid，则orderId优先级更高 |
| startTime | query | string | 是 | 查询记录起始时间<br><br>- Unix毫秒时间戳，例如1690196141868 |
| endTime | query | string | 是 | 查询记录结束时间<br><br>- Unix毫秒时间戳，例如1690196141868 |
| limit | query | string |  | 每页条目数<br><br>默认值为20，最大值为100 |
| cursor | query | string |  | 游标ID<br><br>- 用于翻页，可缩短查询响应时间<br><br>- 首次查询不传，查询第二页及后续数据时，取上一次查询返回的最小orderId，结果会返回小于该值的数据 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  | 提币记录列表 |
| data[].orderId | string |  | 订单ID |
| data[].clientOid | string |  | 自定义订单ID |
| data[].recordId | string |  | 提币记录ID<br><br>- 如果`dest`为`on_chain`，则为链上哈希值<br><br>- 如果`dest`为`internal_transfer`，则为订单ID |
| data[].coin | string |  | 币种名称 |
| data[].type | string |  | 操作类型<br><br>`withdraw` 提币 |
| data[].dest | string |  | 提币类型<br><br>`on_chain` 链上提币<br><br>`internal_transfer` 内部转账 |
| data[].size | string |  | 提币数量 |
| data[].status | string |  | 提币状态<br><br>`pending` 确认中<br><br>`success` 成功<br><br>`fail` 失败 |
| data[].fromAddress | string |  | 提币发起方<br><br>- 如果`dest`为`on_chain`，则为链上地址<br><br>- 如果`dest`为`internal_transfer`，则为`uid`, `email`或者`mobile` |
| data[].toAddress | string |  | 提币接收方<br><br>- 如果`dest`为`on_chain`，则为链上地址<br><br>- 如果`dest`为`internal_transfer`，则为`uid`, `email`或者`mobile` |
| data[].chain | string |  | 提币网络<br><br>- `dest`为`internal_transfer`时可忽略此参数 |
| data[].fee | string |  | 手续费<br><br>- 计量单位为提币币种 |
| data[].confirm | string |  | 确认区块数 |
| data[].tag | string |  | 标签 |
| data[].createdTime | string |  | 提币记录创建时间，Unix毫秒时间戳 |
| data[].updatedTime | string |  | 提币记录更新时间，Unix毫秒时间戳 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740481864545,
  "data": [
    {
      "orderId": "1278112570963742720",
      "clientOid": "12121212112",
      "recordId": "1278112570963742720",
      "coin": "usdt",
      "type": "deposit",
      "dest": "internal_transfer",
      "size": "100",
      "status": "success",
      "fromAddress": "0x51xxx",
      "toAddress": "0x51xxx",
      "chain": "erc20",
      "fee": "10",
      "confirm": "5",
      "tag": "",
      "createdTime": "1740451703778",
      "updatedTime": "1740451703778"
    }
  ]
}
```

## 查询提币地址簿

`GET /api/v3/account/withdraw-address`

限频规则: 1次/秒/UID

查询账户下已绑定的提现地址簿，获取地址标签、链类型、地址状态等信息。

需要钱包只读权限

Operation ID: `depositWithdrawalGetWithdrawAddress`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| coin | query | string |  | 币种名称，如 BTC、ETH。不传则返回所有币种。仅支持普通地址查询，不支持EVM地址、通用地址及内部地址查询 |
| type | query | string |  | 地址簿类型：`EVM` EVM地址 / `regular` 普通地址 / `universal` 通用地址 / `internal` 内部地址 |
| limit | query | string |  | 每页条目数，默认为10，最大为10 |
| cursor | query | string |  | 游标ID，用于翻页 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.addressList | object[] |  | 地址簿列表 |
| data.addressList[].coin | string |  | 币种名称 |
| data.addressList[].chain | string |  | 链名称 |
| data.addressList[].address | string |  | 提现地址。当 `type=internal` 时，该字段返回UID、手机号或邮箱 |
| data.addressList[].countryCode | string |  | 国家号，仅 `internalType=mobile` 时返回 |
| data.addressList[].label | string |  | 地址标签（用户自定义） |
| data.addressList[].memo | string |  | Memo，部分链需要（如 XRP、EOS），无则为空字符串 |
| data.addressList[].type | string |  | 地址簿类型：`regular` 普通地址 / `EVM` EVM地址 / `universal` 通用地址 / `internal` 内部地址 |
| data.addressList[].internalType | string |  | 内部转账类别：`uid` UID / `mobile` 手机号 / `email` 邮箱，仅 `type=internal` 时有值 |
| data.addressList[].createdTime | string |  | 创建时间（Unix毫秒时间戳） |
| data.cursor | string |  | 下一页游标ID |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": {
    "addressList": [
      {
        "coin": "BTC",
        "chain": "BTC",
        "address": "1A1zP1eP5QGefi2DMPTfTL5SLmv7Divf",
        "countryCode": "",
        "label": "我的BTC钱包",
        "memo": "",
        "type": "regular",
        "internalType": "",
        "createdTime": "1740000000000"
      }
    ],
    "cursor": "1740000000000"
  }
}
```

## 获取可划转币种

`GET /api/v3/account/transferable-coins`

限频规则: 10次/秒/UID

查询**统一账户和经典账户**可划转币种

_经典账户包含：现货，逐仓杠杆，全仓杠杆，U本位合约，币本位合约，USDC合约，和P2P账户_

需要统一账户管理只读/读写权限

Operation ID: `depositWithdrawalGetTransferableCoins`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| fromType | query | string | 是 | 转出(源)账户类型<br><br>`spot` 现货账户/资金账户<br><br>`p2p` P2P账户/OTC账户<br><br>`coin_futures` 币本位合约账户<br><br>`usdt_futures` U本位合约账户<br><br>`usdc_futures` USDC合约账户<br><br>`crossed_margin` 全仓杠杆账户<br><br>`isolated_margin` 逐仓杠杆账户<br><br>`uta` 统一账户 |
| toType | query | string | 是 | 转入(目的)账户类型<br><br>`spot` 现货账户/资金账户<br><br>`p2p` P2P账户/OTC账户<br><br>`coin_futures` 币本位合约账户<br><br>`usdt_futures` U本位合约账户<br><br>`usdc_futures` USDC合约账户<br><br>`crossed_margin` 全仓杠杆账户<br><br>`isolated_margin` 逐仓杠杆账户<br><br>`uta` 统一账户 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | string[] |  | 可划转币种列表 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1730189276579,
  "data": [
    "USDT"
  ]
}
```

## 划转

`POST /api/v3/account/transfer`

限频规则: 5次/秒/UID

支持统一账户与经典账户间的资金转入/转出

需要统一账户管理读写权限

Operation ID: `depositWithdrawalTransfer`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| fromType | string | 是 | 转出(源)账户类型<br><br>`spot` 现货账户/资金账户<br><br>`p2p` P2P账户/OTC账户<br><br>`coin_futures` 币本位合约账户<br><br>`usdt_futures` U本位合约账户<br><br>`usdc_futures` USDC合约账户<br><br>`crossed_margin` 全仓杠杆账户<br><br>`isolated_margin` 逐仓杠杆账户<br><br>`uta` 统一账户 |
| toType | string | 是 | 转入(目的)账户类型<br><br>`spot` 现货账户/资金账户<br><br>`p2p` P2P账户/OTC账户<br><br>`coin_futures` 币本位合约账户<br><br>`usdt_futures` U本位合约账户<br><br>`usdc_futures` USDC合约账户<br><br>`crossed_margin` 全仓杠杆账户<br><br>`isolated_margin` 逐仓杠杆账户<br><br>`uta` 统一账户 |
| amount | string | 是 | 划转数量 |
| coin | string | 是 | 划转币种，如BTC |
| symbol | string |  | 逐仓杠杆交易对，如BTCUSDT |
| allowBorrow | string |  | 允许转出借币<br><br>`yes` 开启<br><br>`no` 不开启<br><br>若为`yes`，当账户可用余额不足时，将自动通过杠杆借币完成划转 |
| clientOid | string |  | 客户自定义ID |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.transferId | string |  | 划转ID |
| data.clientOid | string |  | 客户自定义ID |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1730189276579,
  "data": {
    "transferId": "111111111111",
    "clientOid": "my-transfer-001"
  }
}
```

## 子母划转

`POST /api/v3/account/sub-transfer`

限频规则: 5次/秒/UID

子母账户资产划转，该接口支持的划转类型包括：

- 母账户转子账户（仅母账户APIKey有权限）

- 子账户转母账户（仅母账户APIKey有权限）

- 子账户转子账户（仅母账户APIKey有权限，并要求发起与接收方子账户归属于同一母账户）

- 子账户内部划转（仅母账户APIKey有权限，并要求发起与接收方子账户为同一子账户）

请求参数中的转入及转出账户UID须为母子/兄弟关系，且调用方需为母账户API Key

需要统一账户管理读写权限，仅母账户才能调用此接口

Operation ID: `depositWithdrawalSubAccountTransfer`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| fromType | string | 是 | 转出账户类型<br><br>`spot` 现货账户/资金账户<br><br>`p2p` P2P账户/OTC账户<br><br>`usdt_futures` U本位合约账户<br><br>`coin_futures` 币本位合约账户<br><br>`usdc_futures` USDC合约账户<br><br>`crossed_margin` 全仓杠杆账户<br><br>`uta` 统一账户<br><br>**上述枚举值全部适用于母账户**<br><br>如果是子账户：<br><br>统一账户子账户仅支持`uta`和`spot`<br><br>经典账户子账户不支持`uta`以及`p2p` |
| toType | string | 是 | 转入账户类型<br><br>`spot` 现货账户/资金账户<br><br>`p2p` P2P账户/OTC账户<br><br>`usdt_futures` U本位合约账户<br><br>`coin_futures` 币本位合约账户<br><br>`usdc_futures` USDC合约账户<br><br>`crossed_margin` 全仓杠杆账户<br><br>`uta` 统一账户<br><br>**上述枚举值全部适用于母账户**<br><br>如果是子账户：<br><br>统一账户子账户仅支持`uta`和`spot`<br><br>经典账户子账户不支持`uta`以及`p2p` |
| amount | string | 是 | 划入数量 |
| coin | string | 是 | 划转币种，如: BTC |
| fromUserId | string | 是 | 转出账户UID |
| toUserId | string | 是 | 转入账户UID |
| clientOid | string | 是 | 划转自定义订单ID，不能超过50个字符 |
| allowBorrow | string |  | 允许转出借币<br><br>`yes` 开启<br><br>`no` 不开启<br><br>若为`yes`，当账户可用余额不足时，将自动通过杠杆借币完成划转 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.transferId | string |  | 划转ID |
| data.clientOid | string |  | 划转自定义订单ID |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740213448866,
  "data": {
    "transferId": "172947298237423",
    "clientOid": "test_001"
  }
}
```

## 获取子母划转记录

`GET /api/v3/account/sub-transfer-record`

限频规则: 5次/秒/UID

该接口支持获取子母账户间的划转记录

需要统一账户管理读取权限

Operation ID: `depositWithdrawalGetSubAccountTransferRecords`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| subUid | query | string |  | 子账户UID，如不传，则获取母账户的划转记录 |
| role | query | string |  | 转出账户类型<br><br>`initiator` 发起转账方<br><br>`receiver` 接收转账方<br><br>默认为`initiator` |
| coin | query | string |  | 币种名称 |
| startTime | query | string |  | 划转记录的查询开始时间<br><br>- Unix毫秒时间戳，例如1690196141868<br><br>- startTime和endTime的时间间隔不超过90天 |
| endTime | query | string |  | 划转记录的查询结束时间<br><br>- Unix毫秒时间戳，例如1690196141868<br><br>- startTime和endTime的时间间隔不超过90天 |
| clientOid | query | string |  | 划转自定义订单ID，不能超过64个字符 |
| limit | query | string |  | 每页条目数<br><br>默认值为100，最大值为100 |
| cursor | query | string |  | 游标ID<br><br>用于翻页，首次查询不传，查询第二页及后面的数据时，取上一次查询返回的cursor |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.cursor | string |  | 游标ID |
| data.list | object[] |  | 划转记录列表 |
| data.list[].transferId | string |  | 划转订单ID |
| data.list[].fromType | string |  | 转出账户类型<br><br>`spot` 现货账户/资金账户<br><br>`p2p` P2P账户/OTC账户<br><br>`usdt_futures` U本位合约账户<br><br>`coin_futures` 币本位合约账户<br><br>`usdc_futures` USDC合约账户<br><br>`crossed_margin` 全仓杠杆账户<br><br>`unified` 统一账户 |
| data.list[].toType | string |  | 转入账户类型<br><br>`spot` 现货账户/资金账户<br><br>`p2p` P2P账户/OTC账户<br><br>`usdt_futures` U本位合约账户<br><br>`coin_futures` 币本位合约账户<br><br>`usdc_futures` USDC合约账户<br><br>`crossed_margin` 全仓杠杆账户<br><br>`unified` 统一账户 |
| data.list[].amount | string |  | 划转数量 |
| data.list[].coin | string |  | 划转币种 |
| data.list[].fromUserId | string |  | 转出账户UID |
| data.list[].toUserId | string |  | 转入账户UID |
| data.list[].status | string |  | 划转状态<br><br>`Successful` 成功<br><br>`Failed` 失败<br><br>`Processing` 处理中 |
| data.list[].clientOid | string |  | 划转自定义订单ID |
| data.list[].oldTransferId | string |  | 原划转订单ID |
| data.list[].createdTime | string |  | 划转创建时间，Unix毫秒时间戳 |
| data.list[].updatedTime | string |  | 划转更新时间，Unix毫秒时间戳 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1751453670468,
  "data": {
    "list": [
      {
        "transferId": "1320888751047921664",
        "fromType": "spot",
        "toType": "uta",
        "amount": "20.00000000",
        "coin": "USDT",
        "fromUserId": "6841950428",
        "toUserId": "6841950428",
        "status": "Successful",
        "clientOid": "1320888751047921664",
        "createdTime": "1750650339853",
        "updatedTime": "1750650339853",
        "oldTransferId": "182797214"
      },
      {
        "transferId": "1314821589514407936",
        "fromType": "spot",
        "toType": "isolated_margin",
        "amount": "1.00000000",
        "coin": "USDT",
        "fromUserId": "6841950428",
        "toUserId": "6841950428",
        "status": "Successful",
        "clientOid": "1314821589514407936",
        "createdTime": "1749203815821",
        "updatedTime": "1749203815821",
        "oldTransferId": "175609331"
      }
    ],
    "cursor": "2"
  }
}
```

## 子账户主动划转至母账户

`POST /api/v3/account/sub-master-transfer`

限频规则: 5次/秒/UID

子账户主动划转至母账户，调用方需为子账户API Key

需要统一账户管理读写权限

Operation ID: `depositWithdrawalSubMasterTransfer`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| fromType | string | 是 | 转出账户类型<br><br>`spot` 资金账户<br><br>`uta` 统一账户 |
| toType | string | 是 | 转入账户类型<br><br>`spot` 资金账户<br><br>`p2p` OTC账户<br><br>`uta` 统一账户 |
| amount | string | 是 | 划入数量 |
| coin | string | 是 | 划转币种，如: BTC |
| clientOid | string |  | 划转自定义订单ID，不能超过64个字符 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.transferId | string |  | 划转ID |
| data.clientOid | string |  | 划转自定义订单ID |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740213448866,
  "data": {
    "transferId": "172947298237423",
    "clientOid": "test_001"
  }
}
```

## 获取小额兑换历史记录

`GET /api/v3/convert/small-assets-history`

查询统一账户下的历史小额兑换订单，支持时间范围筛选与游标分页。支持查询近90天数据，单次查询时间范围最大30天。

- 限频规则: 10次/秒/UID

- 需要统一账户管理只读权限

Operation ID: `utaAccountSmallAssetsGetSmallAssetsHistory`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| accountType | query | string |  | 账户类型<br><br>`uta` 统一账户<br><br>`funding` 资金账户<br><br>不传返回全部账户类型 |
| orderId | query | string |  | 兑换订单ID |
| startTime | query | string |  | 开始时间<br><br>Unix毫秒时间戳<br><br>支持查询近90天数据，单次查询时间范围最大30天 |
| endTime | query | string |  | 结束时间<br><br>Unix毫秒时间戳<br><br>支持查询近90天数据，单次查询时间范围最大30天 |
| limit | query | string |  | 每页条目数<br><br>默认值20，最大100 |
| cursor | query | string |  | 游标ID<br><br>用于翻页。首次查询不传，查询第二页及后面的数据时，取上一次查询返回的最小orderId，结果会返回小于该值的数据；可以缩短查询响应时间 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.list | object[] |  | 列表 |
| data.list[].orderId | string |  | 闪兑记录id |
| data.list[].accountType | string |  | 账户类型<br><br>`uta`/`funding` |
| data.list[].fromCoin | string |  | 兑换币种 |
| data.list[].fromAmount | string |  | 兑换数量 |
| data.list[].fromCoinPrice | string |  | 兑换时价格 |
| data.list[].toCoin | string |  | 目标币种 |
| data.list[].toAmount | string |  | 目标币种数量 |
| data.list[].toCoinPrice | string |  | 兑换时目标币种价格 |
| data.list[].feeDetail | object[] |  | 手续费明细 |
| data.list[].feeDetail[].fee | string |  | 手续费数额 |
| data.list[].feeDetail[].feeCoin | string |  | 手续费币种 |
| data.status | string |  | 兑换状态<br><br>- success 成功 |
| data.createdTime | string |  | 兑换时间 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": {
    "list": [
      {
        "orderId": "1234567890123456789",
        "accountType": "uta",
        "fromCoin": "DOGE",
        "fromAmount": "12.5",
        "fromCoinPrice": "0.064",
        "toCoin": "BGB",
        "toAmount": "0.8",
        "toCoinPrice": "0.8",
        "feeDetail": {
          "fee": "0.0008",
          "feeCoin": "BGB"
        },
        "status": "success",
        "createdTime": "1740000000000"
      }
    ],
    "cursor": "1234567890123456789"
  }
}
```

## 获取小额兑换可兑换币种

`GET /api/v3/convert/small-assets`

查询统一账户下当前账户内持有的小额资产列表。小额资产定义为折合 USDT 价值低于5U的持仓。目标币种支持 BGB。

- 限频规则: 10次/秒/UID

- 需要统一账户管理只读权限

Operation ID: `utaAccountSmallAssetsGetSmallAssets`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| accountType | query | string |  | 账户类型<br><br>`uta` 统一账户（默认）<br><br>`funding` 资金账户 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].coin | string |  | 币种名称 |
| data[].available | string |  | 币种账户可用 |
| data[].estimatedCoin | string |  | 预期兑换币种<br><br>- BGB |
| data[].estimatedAmount | string |  | 预期兑换数量 |
| data[].feeDetail | object |  | 手续费明细 |
| data[].feeDetail.feeRate | string |  | 手续费率 |
| data[].feeDetail.fee | string |  | 手续费数额 |
| data[].cTime | string |  | 当前时间 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": [
    {
      "coin": "DOGE",
      "available": "12.5",
      "estimatedCoin": "BGB",
      "estimatedAmount": "0.8",
      "feeDetail": {
        "feeRate": "0.001",
        "fee": "0.0008"
      },
      "cTime": "1740000000000"
    }
  ]
}
```

## 执行小额兑换

`POST /api/v3/convert/small-assets-trade`

将统一账户内指定的一种或多种小额资产一键兑换为目标币种。

- 限频规则: 10次/秒/UID

- 需要统一账户交易权限

Operation ID: `utaAccountSmallAssetsSmallAssetsTrade`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| accountType | string |  | 账户类型<br><br>`uta` 统一账户（默认）<br><br>`funding` 资金账户 |
| fromCoinList | string[] | 是 | 兑换币种 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.fromCoin | string[] |  | 兑换币种 |
| data.toCoin | string |  | 目标币种 |
| data.orderId | string |  | 兑换订单Id |
| data.accountType | string |  | 账户类型<br><br>`uta`/`funding`<br><br>回传本次兑换的账户类型 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": {
    "fromCoin": [
      "DOGE",
      "XRP"
    ],
    "toCoin": "BGB",
    "orderId": "1234567890123456789",
    "accountType": "funding"
  }
}
```

## 获取限频配额

`GET /api/v3/user/rate-limit-quota`

查询账户限频配额配置。支持查询单个账户的额度分配情况，或列出母账户下所有子账户的限频配额。

该接口现已支持子账号使用自身API Key直接调用，查询子账号自身的限频配额。

> **注意**：该接口仅对 **MM（做市商）和 PRO** 机构用户开放。

- 限频规则: 10次/秒/UID

- 权限：统一账户管理 — 只读

Operation ID: `utaUserRateLimitGetRateLimitQuota`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| category | query | string | 是 | 业务线<br><br>`spot` 现货<br><br>`futures` 合约 |
| uid | query | string |  | 账户UID<br><br>用于单个账户限频配额查询；不填则列出所有子账户<br><br>子账号自行调用时该字段非必填，会被忽略，直接返回该子账号自身的限频配额 |
| cursor | query | string |  | 游标<br><br>后续查询的页码游标 |
| limit | query | string |  | 每页条目数<br><br>默认值：`100`，最大值：`100` |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.category | string |  | 业务线<br><br>`spot` 现货<br><br>`futures` 合约 |
| data.quotaList | object[] |  | 子账户限频配额列表 |
| data.quotaList[].uid | string |  | 账户UID |
| data.quotaList[].quota | string |  | 单账户限频实际设置值 |
| data.masterSubQuota | string |  | 母子账户限频实际设置值 |
| data.masterSubCap | string |  | 母子账户限频硬顶 |
| data.cursor | string |  | 游标<br><br>后续查询的页码游标 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1753987234567,
  "data": {
    "category": "futures",
    "quotaList": [
      {
        "uid": "123456",
        "quota": "100"
      }
    ],
    "masterSubQuota": "10000",
    "masterSubCap": "80000",
    "cursor": "1"
  }
}
```

## 设置限频配额

`POST /api/v3/user/set-rate-limit-quota`

1. 设置子账户限频配额。该接口支持母账户为子账户设定现货与合约交易的独立限频额度。

2. 该接口支持按照业务线维度的单个或批量账户额度分配。

3. 单账户限频Quota数值不得超过单账户限频Cap，否则接口报错

4. 所有子账户的单账户限频Quota总和（即母子账户限频Quota）不得超过母子账户总限频硬顶Cap。

5. 如果调整某账户限频Quota后，母子账户限频Quota超出母子账户硬顶Cap，则当次接口调用不会成功

6. 该接口现已支持子账号使用自身API Key直接调用，自行设置机构限频配额，规则与母账号设置相同。

> **注意**：该接口仅对 **MM（做市商）和 PRO** 机构用户开放。

- 限频规则: 5次/秒/UID

- 权限：统一账户管理 — 读写

Operation ID: `utaUserRateLimitSetRateLimitQuota`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| category | string | 是 | 业务线<br><br>`spot` 现货<br><br>`futures` 合约 |
| uids | string[] | 是 | 子账户UID<br><br>单次最多可传 50 个 UID<br><br>母账号调用时必填；子账号调用时该字段非必填，会被忽略 |
| quota | string | 是 | 限频额度<br><br>额度不得超过单账户限频 Cap |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data |  |  | Response data |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1753987234567,
  "data": "success"
}
```