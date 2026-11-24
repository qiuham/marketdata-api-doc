---
exchange: bitget
source_url: https://www.bitget.com/docs/catalog/classic-contract-account
api_type: REST
updated_at: 2026-11-24 19:01:54.927382
---

# Classic Contract Account API

Classic account — futures account & leverage settings.

版本: 1.0.0

## 服务地址

- `https://api.bitget.com`

## 接口列表

- `GET /api/v2/mix/account/account` — Get Single Account
- `GET /api/v2/mix/account/accounts` — Get Account List
- `GET /api/v2/mix/account/sub-account-assets` — Get Subaccount Assets
- `GET /api/v2/mix/account/open-count` — My Estimated Open Count
- `GET /api/v2/mix/account/liq-price` — Get Liquidation Price
- `GET /api/v2/mix/account/max-open` — Get Max Openable Quantity
- `GET /api/v2/mix/account/interest-history` — Get USDT-M futures Interest history
- `POST /api/v2/mix/account/set-all-leverage` — Change The Product Line Leverage
- `POST /api/v2/mix/account/set-leverage` — Change Leverage
- `POST /api/v2/mix/account/set-margin` — Adjust Position Margin
- `POST /api/v2/mix/account/set-auto-margin` — Set Isolated Position Auto Margin
- `POST /api/v2/mix/account/set-margin-mode` — Change Margin Mode
- `POST /api/v2/mix/account/set-position-mode` — Change Position Mode
- `POST /api/v2/mix/account/set-asset-mode` — Set USDT-M Futures Asset Mode
- `GET /api/v2/mix/account/bill` — Get Account Bills
- `POST /api/v2/mix/account/union-convert` — Union Convert
- `GET /api/v2/mix/account/transfer-limits` — Get Union Transfer Limits
- `GET /api/v2/mix/account/union-config` — Get Union Config
- `GET /api/v2/mix/account/switch-union-usdt` — Get Switch Union USDT
- `GET /api/v2/mix/account/isolated-symbols` — Get Isolated Symbols

## Get Single Account

`GET /api/v2/mix/account/account`

Frequency limit: 10 times/1s (uid)

Get account details with the given 'marginCoin' and 'productType'

Operation ID: `classicContractAccountGetSingleAccount`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | Trading pair |
| productType | query | string | 是 | Product type<br><br>`USDT-FUTURES` USDT-M Futures<br><br>`COIN-FUTURES` Coin-M Futures<br><br>`USDC-FUTURES` USDC-M Futures |
| marginCoin | query | string | 是 | Margin coin |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.marginCoin | string |  | Margin coin |
| data.locked | string |  | Locked quantity (margin coin). Lockup will be triggered when there is a position to be closed. |
| data.available | string |  | Available quantity in the account |
| data.crossedMaxAvailable | string |  | Maximum available balance to open positions under the cross margin mode (margin coin) |
| data.isolatedMaxAvailable | string |  | Maximum available balance to open positions under the isolated margin mode (margin coin) |
| data.maxTransferOut | string |  | Maximum transferable amount |
| data.accountEquity | string |  | Account equity (margin coin), including unrealized PnL (based on mark price) |
| data.usdtEquity | string |  | Account equity in USDT |
| data.btcEquity | string |  | Account equity in BTC |
| data.crossedRiskRate | string |  | Risk ratio in cross margin mode |
| data.crossedMarginLeverage | string |  | Leverage in cross margin mode |
| data.isolatedLongLever | string |  | Leverage of long positions in isolated margin mode |
| data.isolatedShortLever | string |  | Leverage of short positions in isolated margin mode |
| data.marginMode | string |  | Margin mode.<br><br>isolated – isolated margin mode;<br><br>crossed – cross margin mode |
| data.posMode | string |  | Position mode<br><br>one_way_mode: one-way mode<br><br>hedge_mode: hedge mode |
| data.unrealizedPL | string |  | Unrealized PnL |
| data.coupon | string |  | Trading bonus |
| data.crossedUnrealizedPL | string |  | unrealizedPL for croessed |
| data.isolatedUnrealizedPL | string |  | unrealizedPL for isolated |
| data.assetMode | string |  | Assets mode<br><br>`union` Multi-assets mode<br><br>`single` Single-assets mode |
| data.grant | string |  | Futures Airdrop Voucher Amount |
| data.isolatedMargin | string |  | Isolated Margin Occupied |
| data.crossedMargin | string |  | Crossed Margin Occupied |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1766991729861,
  "data": {
    "marginCoin": "USDT",
    "locked": "0",
    "available": "-4500.10469626",
    "crossedMaxAvailable": "82755.86971252",
    "isolatedMaxAvailable": "82755.86971252",
    "maxTransferOut": "0",
    "accountEquity": "-4767.74182959",
    "usdtEquity": "-4767.7418295954693173",
    "btcEquity": "-0.0530992998208352",
    "crossedRiskRate": "0.002850528048353",
    "crossedMarginLeverage": 14,
    "isolatedLongLever": 14,
    "isolatedShortLever": 14,
    "marginMode": "crossed",
    "posMode": "hedge_mode",
    "unrealizedPL": "-267.6371333333333385",
    "coupon": "0",
    "crossedUnrealizedPL": "-19.4814333333333385",
    "isolatedUnrealizedPL": "",
    "grant": "0",
    "assetMode": "union",
    "isolatedMargin": null,
    "crossedMargin": null
  }
}
```

## Get Account List

`GET /api/v2/mix/account/accounts`

Frequency limit: 10 times/1s (uid)

Query all account information under a certain product type

Operation ID: `classicContractAccountGetAccountList`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| productType | query | string | 是 | Product type<br><br>`USDT-FUTURES` USDT-M Futures<br><br>`COIN-FUTURES` Coin-M Futures<br><br>`USDC-FUTURES` USDC-M Futures |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].marginCoin | string |  | Margin coin |
| data[].locked | string |  | Locked quantity (margin coin) |
| data[].available | string |  | Available quantity in the account |
| data[].crossedMaxAvailable | string |  | Maximum available balance to open positions under the cross margin mode (margin coin) |
| data[].isolatedMaxAvailable | string |  | Maximum available balance to open positions under the isolated margin mode (margin coin) |
| data[].maxTransferOut | string |  | Maximum transferable amount |
| data[].accountEquity | string |  | Account equity (margin coin),<br><br>Includes unrealized PnL (based on mark price) |
| data[].usdtEquity | string |  | Account equity in USDT |
| data[].btcEquity | string |  | Account equity in BTC |
| data[].crossedRiskRate | string |  | Risk ratio in cross margin mode |
| data[].unrealizedPL | string |  | Unrealized PnL |
| data[].coupon | string |  | Trading bonus |
| data[].unionTotalMargin | string |  | Multi-assets multi-assets mode |
| data[].unionAvailable | string |  | Available under multi-assets mode |
| data[].unionMm | string |  | Maintenance margin under multi-assets mode |
| data[].assetList | object[] |  | Assets list under multi-assets mode |
| data[].assetList[].coin | string |  | Coin name |
| data[].assetList[].balance | string |  | Balance |
| data[].assetList[].available | string |  | Maximum transferable amount <br><br> Unit: current coin |
| data[].isolatedMargin | string |  | Isolated Margin Occupied |
| data[].crossedMargin | string |  | Crossed Margin Occupied |
| data[].crossedUnrealizedPL | string |  | unrealizedPL for croessed |
| data[].isolatedUnrealizedPL | string |  | unrealizedPL for isolated |
| data[].assetMode | string |  | Assets mode<br><br>`union` Multi-assets mode<br><br>`single` Single-assets mode |
| data[].grant | string |  | Futures Airdrop Voucher Amount |

```json
{
  "code": "00000",
  "data": [
    {
      "marginCoin": "USDT",
      "locked": "0.31876482",
      "available": "10575.26735771",
      "crossedMaxAvailable": "10580.56434289",
      "isolatedMaxAvailable": "10580.56434289",
      "maxTransferOut": "10572.92904289",
      "accountEquity": "10582.90265771",
      "usdtEquity": "10582.902657719473",
      "btcEquity": "0.204885807029",
      "crossedRiskRate": "0",
      "unrealizedPL": "",
      "coupon": "0",
      "unionTotalMargin": "111,1",
      "unionAvailable": "1111.1",
      "unionMm": "111",
      "assetList": [
        {
          "coin": "BTC",
          "balance": "1.2",
          "available": "1.2"
        }
      ],
      "isolatedMargin": "23.43",
      "crossedMargin": "34.34",
      "crossedUnrealizedPL": "23",
      "isolatedUnrealizedPL": "0",
      "grant": "0",
      "assetMode": "union"
    }
  ],
  "msg": "success",
  "requestTime": 1630901215622
}
```

## Get Subaccount Assets

`GET /api/v2/mix/account/sub-account-assets`

Frequency limit: 1 time/10s (uid)

Query the contract asset information of all sub-accounts. **ND Brokers are not allowed to call this endpoint**

Operation ID: `classicContractAccountGetSubAccountContractAssets`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| productType | query | string | 是 | Product type<br><br>`USDT-FUTURES` USDT-M Futures<br><br>`COIN-FUTURES` Coin-M Futures<br><br>`USDC-FUTURES` USDC-M Futures |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].userId | string |  | Sub account userId |
| data[].assetList | object[] |  | Collection of all futures assets under sub-accounts |
| data[].assetList[].marginCoin | string |  | Margin coin |
| data[].assetList[].locked | string |  | Locked quantity (margin coin) |
| data[].assetList[].available | string |  | Available quantity in the account |
| data[].assetList[].crossedMaxAvailable | string |  | Maximum available balance to open positions under the cross margin mode (margin coin) |
| data[].assetList[].isolatedMaxAvailable | string |  | Maximum available balance to open positions under the isolated margin mode (margin coin) |
| data[].assetList[].maxTransferOut | string |  | Maximum transferable amount |
| data[].assetList[].equity | string |  | Account equity (margin coin) |
| data[].assetList[].usdtEquity | string |  | Account equity in USDT |
| data[].assetList[].btcEquity | string |  | Account equity in BTC |
| data[].assetList[].unrealizedPL | string |  | PnL of open positions |
| data[].assetList[].coupon | string |  | Trading bonus |
| data[].assetList[].crossedUnrealizedPL | string |  | unrealizedPL for croessed |
| data[].assetList[].isolatedUnrealizedPL | string |  | unrealizedPL for isolated |
| data[].assetList[].assetMode | string |  | Assets mode<br><br>`union` Multi-assets mode<br><br>`single` Single-assets mode |
| data[].assetList[].grant | string |  | Futures Airdrop Voucher Amount |
| data[].assetList[].isolatedMargin | string |  | Isolated Margin Occupied |
| data[].assetList[].crossedMargin | string |  | Crossed Margin Occupied |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1767781062372,
  "data": [
    {
      "userId": 1234567890,
      "assetList": [
        {
          "marginCoin": "USDT",
          "locked": "0",
          "available": "0",
          "crossedMaxAvailable": "0",
          "isolatedMaxAvailable": "0",
          "maxTransferOut": "0",
          "accountEquity": "0",
          "usdtEquity": "0",
          "btcEquity": "0",
          "unrealizedPL": "0",
          "coupon": null,
          "crossedUnrealizedPL": null,
          "isolatedUnrealizedPL": null,
          "grant": null,
          "assetMode": null,
          "isolatedMargin": null,
          "crossedMargin": null
        }
      ]
    },
    {
      "userId": 1234567890,
      "assetList": [
        {
          "marginCoin": "USDT",
          "locked": "0",
          "available": "0",
          "crossedMaxAvailable": "0",
          "isolatedMaxAvailable": "0",
          "maxTransferOut": "0",
          "accountEquity": "0",
          "usdtEquity": "0",
          "btcEquity": "0",
          "unrealizedPL": "0",
          "coupon": null,
          "crossedUnrealizedPL": null,
          "isolatedUnrealizedPL": null,
          "grant": null,
          "assetMode": null,
          "isolatedMargin": null,
          "crossedMargin": null
        }
      ]
    }
  ]
}
```

## My Estimated Open Count

`GET /api/v2/mix/account/open-count`

Frequency limit: 10 times/1s (uid)

The result for the estimated openable quantity does not include current positions and existing orders.

Operation ID: `classicContractAccountEstOpenCount`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | Trading pair, e.g. ETHUSDT |
| productType | query | string | 是 | Product type<br><br>`USDT-FUTURES` USDT-M Futures<br><br>`COIN-FUTURES` Coin-M Futures<br><br>`USDC-FUTURES` USDC-M Futures |
| marginCoin | query | string | 是 | Margin coin |
| openAmount | query | string | 是 | Margin amount |
| openPrice | query | string | 是 | Price of the order |
| leverage | query | string |  | Leverage<br><br>default 20 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.size | string |  | Estimated open size |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695812285073,
  "data": {
    "size": "0.47"
  }
}
```

## Get Liquidation Price

`GET /api/v2/mix/account/liq-price`

Rate limit: 20 req/sec/UID

Get Liquidation Price

Operation ID: `classicContractAccountGetLiquidationPrice`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | Symbol，e.g.: ETHUSDT |
| productType | query | string | 是 | Product type<br><br>`USDT-FUTURES` USDT Futures<br><br>`COIN-FUTURES` Coin Futures<br><br>`USDC-FUTURES` USDC Futures |
| marginCoin | query | string | 是 | Margin Coin |
| posSide | query | string | 是 | Position side<br><br>`long`Long<br><br>`short`Short |
| orderType | query | string | 是 | orderType<br><br>`limit`Limit order<br><br>`market`Market order |
| openAmount | query | string | 是 | Opening amount |
| openPrice | query | string |  | Opening price<br><br>Required when `orderType=limit` |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.liqPrice | string |  | Liquidation Price |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1762437950669,
  "data": {
    "liqPrice": "-5025939.4855934659933227"
  }
}
```

## Get Max Openable Quantity

`GET /api/v2/mix/account/max-open`

Rate limit: 20 req/sec/UID

The result for the estimated openable quantity includes current positions and existing orders.

Operation ID: `classicContractAccountGetMaxOpen`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | Symbol，e.g.: ETHUSDT |
| productType | query | string | 是 | Product type<br><br>`USDT-FUTURES` USDT Futures<br><br>`COIN-FUTURES` Coin Futures<br><br>`USDC-FUTURES` USDC Futures |
| marginCoin | query | string | 是 | Margin Coin |
| posSide | query | string | 是 | Position side<br><br>`long`Long<br><br>`short`Short |
| orderType | query | string | 是 | orderType<br><br>`limit`Limit order<br><br>`market`Market order |
| openPrice | query | string |  | Opening price<br><br>Required when `orderType=limit` |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.maxOpen | string |  | Max Openable Quantity |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1762438504409,
  "data": {
    "maxOpen": "17563.78"
  }
}
```

## Get USDT-M futures Interest history

`GET /api/v2/mix/account/interest-history`

Frequency limit： 5 times/s (UID)

Get USDT-M futures Interest history

Operation ID: `classicContractAccountInterestHistory`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| coin | query | string |  | coin |
| productType | query | string | 是 | Product type<br><br>`USDT-FUTURES` USDT professional futures |
| idLessThan | query | string |  | Requests the content on the page before this ID (older data), the value input should be the endId of the corresponding interface. |
| startTime | query | string | 是 | Start timestamp <br><br>Unix timestamp in milliseconds format, e.g. 1597026383085 |
| endTime | query | string | 是 | End timestamp <br><br>Unix timestamp in milliseconds format, e.g. 1597026383085 |
| limit | query | string |  | Number of queries: Default: 20, maximum: 100 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.nextSettleTime | string |  | Next interest payment time |
| data.borrowAmount | string |  | Current USDT-M Futures debt |
| data.borrowLimit | string |  | Loan limit |
| data.interestList | object[] |  | interest data |
| data.interestList[].coin | string |  | Coin |
| data.interestList[].liability | string |  | Total debt |
| data.interestList[].interestFreeLimit | string |  | Interest-free amount |
| data.interestList[].interestLimit | string |  | Interest-accruing amount |
| data.interestList[].hourInterestRate | string |  | Hourly interest rate |
| data.interestList[].interest | string |  | interest |
| data.interestList[].cTime | string |  | create time |
| data.endId | string |  | This is used when 'idLessThan' is set as a range. |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1725875190690,
  "data": {
    "nextSettleTime": "1725876300000",
    "borrowAmount": "0",
    "borrowLimit": "600000",
    "interestList": [
      {
        "coin": "USDT",
        "liability": "100",
        "interestFreeLimit": "100",
        "interestLimit": "500",
        "hourInterestRate": "0.12",
        "interest": "0.12",
        "cTime": "1725848567893"
      }
    ],
    "endId": "xxxxxxxxxxxxxxx"
  }
}
```

## Change The Product Line Leverage

`POST /api/v2/mix/account/set-all-leverage`

Frequency limit: 5 times/1s (uid)

Adjust the leverage on the given productType

Operation ID: `classicContractAccountChangeAllLeverage`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| productType | string | 是 | Product type<br><br>`USDT-FUTURES` USDT-M Futures<br><br>`COIN-FUTURES` Coin-M Futures<br><br>`USDC-FUTURES` USDC-M Futures |
| leverage | string | 是 | Leverage (Only effective for symbols that have opened positions) |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | string |  | result<br><br>success: sueexeeful<br><br>failure: failed |

```json
{
  "code": "00000",
  "data": "success",
  "msg": "success",
  "requestTime": 1627293049406
}
```

## Change Leverage

`POST /api/v2/mix/account/set-leverage`

Frequency limit: 5 times/1s (uid)

Adjust the leverage on the given symbol and productType

Note: When adjusting leverage in cross margin mode, please use the leverage parameter instead of `longLeverage` or `shortLeverage`. Currently, there is no mandatory validation for `longLeverage` and `shortLeverage`. If these two parameters are passed in cross margin mode, they will still take effect, with `longLeverage` taking priority.

Operation ID: `classicContractAccountChangeLeverage`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| symbol | string | 是 | Trading pair |
| productType | string | 是 | Product type<br><br>`USDT-FUTURES` USDT-M Futures<br><br>`COIN-FUTURES` Coin-M Futures<br><br>`USDC-FUTURES` USDC-M Futures |
| marginCoin | string | 是 | Margin coin must be capitalized |
| leverage | string |  | Leverage ratio<br><br>- Applicable to cross-margin mode<br><br>- Applicable to one-way position scenarios in isolated margin mode<br><br>- Applicable to scenarios where the same leverage ratio is set for different directions under hedge-mode in isolated margin mode |
| longLeverage | string |  | Long position leverage<br><br>- Only applicable to scenarios where different leverage ratios are set for different directions under hedge-mode in isolated margin mode<br><br>- In two-way position scenarios, if both leverage and longLeverage parameters are passed, longLeverage will take effect and leverage will be ignored |
| shortLeverage | string |  | Short position leverage<br><br>- Only applicable to scenarios where different leverage ratios are set for different directions under hedge-mode in isolated margin mode<br><br>- In two-way position scenarios, if both leverage and shortLeverage parameters are passed, shortLeverage will take effect and leverage will be ignored |
| holdSide | string |  | Position direction <br><br> `long`： Long position；<br><br>`short`：Short position  <br><br>  Cross-margin mode: The holdSide parameter does not need to be filled in <br><br>  Isolated margin mode: For one-way positions, the holdSide parameter does not need to be filled in; for hedge-mode, the holdSide parameter must be filled in. And when long and short leverages are set simultaneously for hedge-mode, holdSide is not required |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.symbol | string |  | Trading pair name |
| data.marginCoin | string |  | Margin coin |
| data.longLeverage | string |  | Leverage of long positions |
| data.shortLeveage | string |  | Leverage of short positions |
| data.crossMarginLeverage | string |  | Leverage of 'crossed' margin mode |
| data.marginMode | string |  | Margin mode.<br><br>isolated – isolated margin mode;<br><br>crossed – cross margin mode |

```json
{
  "code": "00000",
  "data": {
    "symbol": "BTCUSDT",
    "marginCoin": "USDT",
    "longLeverage": "25",
    "shortLeverage": "20",
    "crossMarginLeverage": "20",
    "marginMode": "crossed"
  },
  "msg": "success",
  "requestTime": 1627293049406
}
```

## Adjust Position Margin

`POST /api/v2/mix/account/set-margin`

Rate limit: 5 req/sec/UID

Add or reduce the margin（**only for isolated margin mode**）

Operation ID: `classicContractAccountChangeMargin`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| symbol | string | 是 | Trading pair |
| productType | string | 是 | Product type<br><br>`USDT-FUTURES` USDT-M Futures<br><br>`COIN-FUTURES` Coin-M Futures<br><br>`USDC-FUTURES` USDC-M Futures |
| marginCoin | string | 是 | Margin coin must be capitalized |
| holdSide | string | 是 | Position direction<br><br>long &ndash; long position; short &ndash; short position |
| amount | string | 是 | Margin amount, positive means increase, and negative means decrease |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | string |  | ‘00000’: success; others:  fail |

```json
{
  "code": "00000",
  "data": "",
  "msg": "success",
  "requestTime": 1627293357336
}
```

## Set Isolated Position Auto Margin

`POST /api/v2/mix/account/set-auto-margin`

Frequency limit: 5 times/1s (uid)

Adjust isolated position auto margin

Operation ID: `classicContractAccountSetAutoMargin`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| symbol | string | 是 | Trading pair |
| autoMargin | string | 是 | Auto margin flag<br><br>`on` auto margin on<br><br>`off` auto margin off |
| marginCoin | string | 是 | Margin coin must be capitalized |
| holdSide | string | 是 | Position direction (no need in cross margin mode). <br><br>long &ndash; long position; short &ndash; short position |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | string |  | ‘00000’: success; others:  fail |

```json
{
  "code": "00000",
  "data": "success",
  "msg": "success",
  "requestTime": 1627293357336
}
```

## Change Margin Mode

`POST /api/v2/mix/account/set-margin-mode`

Frequency limit: 5 times/1s (uid)

This interface cannot be used when the users have an open position or an order

Operation ID: `classicContractAccountChangeMarginMode`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| symbol | string | 是 | Trading pair. e.g. BTCUSDT |
| productType | string | 是 | Product type<br><br>`USDT-FUTURES` USDT-M Futures<br><br>`COIN-FUTURES` Coin-M Futures<br><br>`USDC-FUTURES` USDC-M Futures |
| marginCoin | string | 是 | Margin coin, must be capitalized |
| marginMode | string | 是 | Margin mode.<br><br>`isolated`: isolated margin mode<br><br>`crossed`: crossed margin mode |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.symbol | string |  | Trading pair name |
| data.marginCoin | string |  | Margin coin |
| data.longLeverage | string |  | Leverage of long positions |
| data.shortLeveage | string |  | Leverage of short positions |
| data.marginMode | string |  | Margin mode. <br><br>`isolated`: isolated margin mode<br><br>`crossed`: crossed margin mode |

```json
{
  "code": "00000",
  "data": {
    "symbol": "BTCUSDT",
    "marginCoin": "USDT",
    "longLeverage": "25",
    "shortLeverage": "20",
    "marginMode": "isolated"
  },
  "msg": "success",
  "requestTime": 1627293445916
}
```

## Change Position Mode

`POST /api/v2/mix/account/set-position-mode`

Frequency limit: 5 times/1s (uid)

Adjust the position mode between 'one way mode' and 'hedge mode'

If you want to change the user's position mode on all symbol contracts, you need to specify hedge mode positions or one-way positions.

Note: The position mode can't be adjusted when there is an open position order under the product type. Changes the user's position mode for all symbol futures: hedging mode or one-way mode.When users hold positions or orders on any side of any trading pair in the specific product type, the request may fail.

Operation ID: `classicContractAccountChangeHoldMode`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| productType | string | 是 | Product type<br><br>`USDT-FUTURES` USDT-M Futures<br><br>`COIN-FUTURES` Coin-M Futures<br><br>`USDC-FUTURES` USDC-M Futures |
| posMode | string | 是 | Position mode<br><br>one_way_mode: one-way mode<br><br>hedge_mode: hedge mode |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.posMode | string |  | Position mode<br><br>one_way_mode: one-way mode<br><br>hedge_mode: hedge mode |

```json
{
  "code": "00000",
  "msg": "success",
  "data": {
    "posMode": "one_way_mode"
  },
  "requestTime": 1627293445916
}
```

## Set USDT-M Futures Asset Mode

`POST /api/v2/mix/account/set-asset-mode`

Frequency limit: 2 times/1s (uid)

Set USDT-M Futures Asset Mode

Operation ID: `classicContractAccountSetAssetMode`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| productType | string | 是 | Product type<br><br>`USDT-FUTURES` USDT professional futures |
| assetMode | string | 是 | Asset mode<br><br>`single`: Single asset mode<br><br>`union`: Multi-assets mode |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | string |  | 'success' mean set the asset mode success |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1725848356656,
  "data": "success"
}
```

## Get Account Bills

`GET /api/v2/mix/account/bill`

Rate limit: 10 req/sec/UID

Get Account bills(It only supports to get the data within 90days. The older data can be downloaded from web)

Operation ID: `classicContractAccountGetAccountBill`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| productType | query | string | 是 | Product type<br><br>`USDT-FUTURES` USDT-M Futures<br><br>`COIN-FUTURES` Coin-M Futures<br><br>`USDC-FUTURES` USDC-M Futures |
| coin | query | string |  | Currency<br><br>It's valid only when the `businessType` is "trans_from_exchange" or "trans_to_exchange" |
| businessType | query | string |  | Business type |
| onlyFunding | query | string |  | The following four types of non-financial businessType will be excluded.,default：no，<br><br>`yes`：excluded<br><br> `no`: included;<br><br>  The following four businessType ：`append_margin`,`adjust_down_lever_append_margin`, `reduce_margin`, `auto_append_margin` |
| idLessThan | query | string |  | Requests the content on the page before this ID (older data), the value input should be the endId of the corresponding interface. |
| startTime | query | string |  | Start time, ms<br><br>The interval between the `startTime` and the `endTime` should be <= 30 days |
| endTime | query | string |  | End time, ms<br><br>The interval between the `startTime` and the `endTime` should be <= 30 days |
| limit | query | string |  | Page size, max 100, default 20 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.bills | object[] |  | Bill list |
| data.bills[].billId | string |  | Bill ID |
| data.bills[].symbol | string |  | Symbol |
| data.bills[].amount | string |  | Amount |
| data.bills[].fee | string |  | Fee |
| data.bills[].feeByCoupon | string |  | Fee paid by the  coupon |
| data.bills[].businessType | string |  | Business Type<br><br>unknown: unknown <br><br> trans_from_exchange: transfer in from SPOT account <br><br> trans_to_exchange: transfer out to SPOT account <br><br> open_long: open long <br><br> open_short: open short <br><br> close_long: close long <br><br> close_short: close short <br><br> force_close_long: force close long (when burst) <br><br> force_close_short: force close short (when burst) <br><br> contract_settle_fee: funding fee <br><br> append_margin: adjust margin <br><br> adjust_down_lever_append_margin: reduce leverage add margin <br><br> reduce_margin: reduce margin <br><br> auto_append_margin: automatic margin call <br><br> cash_gift_issue: distribute coupon/gift/card <br><br> cash_gift_recycle: recycling coupon/gift/card <br><br> tracking_follow_pay: follower tracking order pay <br><br> tracking_follow_back: follower tracking order cashback <br><br> tracking_trader_income: tracking order income <br><br> burst_long_loss_query: burst close long <br><br> burst_short_loss_query: burst close short <br><br> trans_from_contract: transfer in from FUTURE account <br><br> trans_to_contract: transfer out to FUTURE account <br><br> trans_from_otc: transfer in from OCT account <br><br> trans_to_otc: transfer out to OCT account <br><br> buy: buy in one_way_mode <br><br> sell: sell in one_way_mode <br><br> force_buy: force buy in one_way_mode <br><br> force_sell: force sell in one_way_mode <br><br> burst_buy: burst buy <br><br> burst_sell: burst sell <br><br> bonus_issue: bonus/coupon issue <br><br> bonus_recycle: bonus/coupon recycle <br><br> bonus_expired: bonus/coupon expired <br><br> delivery_long: delivery future settle long <br><br> delivery_short: delivery future settle short <br><br> trans_from_cross: transfer in from CROSS account <br><br> trans_to_cross: transfer out to CROSS account <br><br> trans_from_isolated: transfer in from ISOLATED account <br><br> trans_to_isolated: transfer out to ISOLATED account<br><br>risk_captital_user_transfer：Insurance fund transfer at user end<br><br>user_exchange_buy：Exchange buy(multi-assets mode)<br><br>user_exchange_sell：Exchange sell(multi-assets mode)<br><br>settle_interest：Interest Settlement<br><br>adl_close_long :Auto-Deleveraging closes long positions<br><br>adl_close_short : Auto-Deleveraging closes short positions<br><br>adl_buy_in_single_side_mode :Auto-Deleveraging triggers buy orders<br><br>adl_sell_in_single_side_mode :Auto-Deleveraging triggers sell orders |
| data.bills[].coin | string |  | Coin: USDT |
| data.bills[].balance | string |  | Balance |
| data.bills[].cTime | string |  | Created Time, ms |
| data.endId | string |  | The final transaction order ID.<br><br>This is used when idLessThan/idGreaterThan is set as a range. |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695809161807,
  "data": {
    "bills": [
      {
        "billId": "1",
        "symbol": "BTCUSDT",
        "amount": "-0.004992",
        "fee": "0",
        "feeByCoupon": "",
        "businessType": "contract_settle_fee",
        "coin": "USDT",
        "balance": "232.21",
        "cTime": "1695715200654"
      },
      {
        "billId": "2",
        "symbol": "ETHUSDT",
        "amount": "0",
        "fee": "-0.222012",
        "feeByCoupon": "",
        "businessType": "open_long",
        "coin": "USDT",
        "balance": "232.21",
        "cTime": "1695714563516"
      }
    ],
    "endId": "2"
  }
}
```

## Union Convert

`POST /api/v2/mix/account/union-convert`

Rate limits: 1 time/1s (uid)

Union margin exchange

Operation ID: `classicContractAccountUnionConvert`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| coin | string | 是 | Coin Name<br><br>E.g., BTC |
| amount | string | 是 | Exchange Quantity<br><br>Unit: Exchange Currency |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.usdtAmount | string |  | Exchanged USDT Quantity |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1627293357336,
  "data": {
    "usdtAmount": "1"
  }
}
```

## Get Union Transfer Limits

`GET /api/v2/mix/account/transfer-limits`

Rate limits: 1 time/1s (uid)

Get union margin currency transfer limits

Operation ID: `classicContractAccountGetUnionTransferLimits`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| coin | query | string | 是 | Coin Name<br><br>E.g., BTC |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.coin | string |  | Coin Name |
| data.maxTransferIn | string |  | Maximum Transfer-in Quantity<br><br>Unit: coin |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1627293357336,
  "data": {
    "coin": "BTC",
    "maxTransferIn": "100"
  }
}
```

## Get Union Config

`GET /api/v2/mix/account/union-config`

Rate limits: 1 time/1s (uid)

Get API for union margin configuration parameters (Liability Initial Margin Rate, Liability Maintenance Margin Rate,

Personal Liability Limit, Personal Liability Limit Ratio)

Operation ID: `classicContractAccountGetUnionConfig`

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.imr | string |  | Liability Initial Margin Rate<br><br>Decimal format. Fixed value: 0.1 |
| data.mmr | string |  | Liability Maintenance Margin Rate<br><br>Decimal format. Fixed value: 0.05 |
| data.individualLimit | string |  | Personal Liability Limit<br><br>Unit: USDT |
| data.individualLimitRatio | string |  | Personal Liability Limit Ratio<br><br>Decimal format. E.g., 0.8 represents 80% |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1627293357336,
  "data": {
    "imr": "0.1",
    "mmr": "0.05",
    "individualLimit": "10000",
    "individualLimitRatio": "0.8"
  }
}
```

## Get Switch Union USDT

`GET /api/v2/mix/account/switch-union-usdt`

Rate limits: 1 time/1s (uid)

Get USDT quota for switching from union margin to single margin

Operation ID: `classicContractAccountGetSwitchUnionUSDT`

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.usdtAmount | string |  | USDT quota required for account mode switching<br><br>Unit: USDT |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695809161807,
  "data": {
    "usdtAmount": "1"
  }
}
```

## Get Isolated Symbols

`GET /api/v2/mix/account/isolated-symbols`

Rate limits:  10 time/1s (uid)

Retrieve trading pairs with isolated margin mode under the account.

Operation ID: `classicContractAccountGetIsolatedSymbols`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| productType | query | string | 是 | Product type<br><br>`USDT-FUTURES` USDT-M Futures<br><br>`COIN-FUTURES` Coin-M Futures<br><br>`USDC-FUTURES` USDC-M Futures |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].symbol | string |  | Symbol name |
| data[].marginMode | string |  | The margin mode is fixed as `isolated` |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1761568886493,
  "data": [
    {
      "symbol": "COAIUSDT",
      "marginMode": "isolated"
    },
    {
      "symbol": "EVAAUSDT",
      "marginMode": "isolated"
    }
  ]
}
```


---

经典账户 — 合约账户与杠杆设置。

版本: 1.0.0

## 服务地址

- `https://api.bitget.com`

## 接口列表

- `GET /api/v2/mix/account/account` — 获取单个交易对账户信息
- `GET /api/v2/mix/account/accounts` — 获取账户信息列表
- `GET /api/v2/mix/account/sub-account-assets` — 获取所有子账户合约资产信息
- `GET /api/v2/mix/account/open-count` — 获取可开数量
- `GET /api/v2/mix/account/liq-price` — 获取预估强平价
- `GET /api/v2/mix/account/max-open` — 获取最大可开
- `POST /api/v2/mix/account/set-all-leverage` — 调整业务线所有交易对杠杆
- `POST /api/v2/mix/account/set-leverage` — 调整杠杆
- `POST /api/v2/mix/account/set-margin` — 调整保证金
- `POST /api/v2/mix/account/set-auto-margin` — 设置逐仓仓位自动追加保证金
- `POST /api/v2/mix/account/set-margin-mode` — 调整保证金模式
- `POST /api/v2/mix/account/set-position-mode` — 调整单双向持仓模式
- `POST /api/v2/mix/account/set-asset-mode` — 设置U本位合约联合保证金模式
- `GET /api/v2/mix/account/bill` — 获取账务记录
- `GET /api/v2/mix/account/interest-history` — U本位合约利息记录
- `POST /api/v2/mix/account/union-convert` — 联合保证金兑换
- `GET /api/v2/mix/account/transfer-limits` — 获取联合保证金币种划转限制
- `GET /api/v2/mix/account/union-config` — 获取联合保证金配置参数
- `GET /api/v2/mix/account/switch-union-usdt` — 获取联合保证金切换单币种保证金所需USDT额度
- `GET /api/v2/mix/account/isolated-symbols` — 获取逐仓模式交易对

## 获取单个交易对账户信息

`GET /api/v2/mix/account/account`

限速规则: 10次/1s (uid)

获取资产账户信息

Operation ID: `classicContractAccountGetSingleAccount`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | 交易对名称，例如"BTCUSDT" |
| productType | query | string | 是 | 产品类型<br><br>`USDT-FUTURES` U本位合约<br><br>`COIN-FUTURES` 币本位合约<br><br>`USDC-FUTURES` USDC合约 |
| marginCoin | query | string | 是 | 保证金币种，必须大写 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.marginCoin | string |  | 保证金币种 |
| data.locked | string |  | 锁定数量(保证金币种)，有平仓单时会lock |
| data.available | string |  | 账户可用数量 |
| data.crossedMaxAvailable | string |  | 全仓最大可用来开仓余额(保证金币种) |
| data.isolatedMaxAvailable | string |  | 逐仓最大可用来开仓余额(保证金币种) |
| data.maxTransferOut | string |  | 最大可转出 |
| data.accountEquity | string |  | 账户权益(保证金币种)，包含未实现盈亏（根据mark price计算） |
| data.usdtEquity | string |  | 折算USDT账户权益 |
| data.btcEquity | string |  | 折算BTC账户权益 |
| data.crossedRiskRate | string |  | 全仓时风险率 |
| data.crossedMarginLeverage | string |  | 全仓时杠杆倍数 |
| data.isolatedLongLever | string |  | 逐仓时多头杠杆数 |
| data.isolatedShortLever | string |  | 逐仓时空头杠杆数 |
| data.marginMode | string |  | 保证金模式。<br><br>isolated逐仓模式；<br><br>crossed 全仓模式 |
| data.posMode | string |  | 持仓模式<br><br>one_way_mode 单向持仓<br><br>hedge_mode 双向持仓 |
| data.unrealizedPL | string |  | 未实现盈亏 |
| data.coupon | string |  | 体验金 |
| data.crossedUnrealizedPL | string |  | 全仓未实现盈亏 |
| data.isolatedUnrealizedPL | string |  | 逐仓未实现盈亏 |
| data.assetMode | string |  | 联合保证金<br><br>`union` 联合保证金<br><br>`single` 单币种保证金 |
| data.grant | string |  | 合约空投券金额 |
| data.isolatedMargin | string |  | 逐仓占用保证金 |
| data.crossedMargin | string |  | 全仓占用保证金 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1766991729861,
  "data": {
    "marginCoin": "USDT",
    "locked": "0",
    "available": "-4500.10469626",
    "crossedMaxAvailable": "82755.86971252",
    "isolatedMaxAvailable": "82755.86971252",
    "maxTransferOut": "0",
    "accountEquity": "-4767.74182959",
    "usdtEquity": "-4767.7418295954693173",
    "btcEquity": "-0.0530992998208352",
    "crossedRiskRate": "0.002850528048353",
    "crossedMarginLeverage": 14,
    "isolatedLongLever": 14,
    "isolatedShortLever": 14,
    "marginMode": "crossed",
    "posMode": "hedge_mode",
    "unrealizedPL": "-267.6371333333333385",
    "coupon": "0",
    "crossedUnrealizedPL": "-19.4814333333333385",
    "isolatedUnrealizedPL": "",
    "grant": "0",
    "assetMode": "union",
    "isolatedMargin": null,
    "crossedMargin": null
  }
}
```

## 获取账户信息列表

`GET /api/v2/mix/account/accounts`

限速规则: 10次/1s (uid)

查询某产品类型下所有账户信息

Operation ID: `classicContractAccountGetAccountList`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| productType | query | string | 是 | 产品类型<br><br>`USDT-FUTURES` U本位合约<br><br>`COIN-FUTURES` 币本位合约<br><br>`USDC-FUTURES` USDC合约 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].marginCoin | string |  | 保证金币种 |
| data[].locked | string |  | 锁定数量(保证金币种) |
| data[].available | string |  | 账户可用数量 |
| data[].crossedMaxAvailable | string |  | 全仓最大可用来开仓余额(保证金币种) |
| data[].isolatedMaxAvailable | string |  | 逐仓最大可用来开仓余额(保证金币种) |
| data[].maxTransferOut | string |  | 最大可转出 |
| data[].accountEquity | string |  | 账户权益(保证金币种)，<br><br>包含未实现盈亏（根据mark price计算） |
| data[].usdtEquity | string |  | 折算USDT账户权益 |
| data[].btcEquity | string |  | 折算BTC账户权益 |
| data[].crossedRiskRate | string |  | 全仓时风险率 |
| data[].unrealizedPL | string |  | 未实现盈亏 |
| data[].coupon | string |  | 体验金 |
| data[].unionTotalMargin | string |  | 联合保证金 |
| data[].unionAvailable | string |  | 联合保证金模式下的可用 |
| data[].unionMm | string |  | 联合保证金模式下的维持保证金 |
| data[].assetList | object[] |  | 联合保证金币种数据 |
| data[].assetList[].coin | string |  | 币种 |
| data[].assetList[].balance | string |  | 余额 |
| data[].assetList[].available | string |  | 最大可转出<br><br> 单位为当前币种 |
| data[].isolatedMargin | string |  | 逐仓占用保证金 |
| data[].crossedMargin | string |  | 全仓占用保证金 |
| data[].crossedUnrealizedPL | string |  | 全仓未实现盈亏 |
| data[].isolatedUnrealizedPL | string |  | 逐仓未实现盈亏 |
| data[].assetMode | string |  | 联合保证金<br><br>`union` 联合保证金<br><br>`single` 单币种保证金 |
| data[].grant | string |  | 合约空投券金额 |

```json
{
  "code": "00000",
  "data": [
    {
      "marginCoin": "USDT",
      "locked": "0.31876482",
      "available": "10575.26735771",
      "crossedMaxAvailable": "10580.56434289",
      "isolatedMaxAvailable": "10580.56434289",
      "maxTransferOut": "10572.92904289",
      "accountEquity": "10582.90265771",
      "usdtEquity": "10582.902657719473",
      "btcEquity": "0.204885807029",
      "crossedRiskRate": "0",
      "unrealizedPL": "",
      "coupon": "0",
      "unionTotalMargin": "111,1",
      "unionAvailable": "1111.1",
      "unionMm": "111",
      "assetList": [
        {
          "coin": "BTC",
          "balance": "1.2",
          "available": "1.2"
        }
      ],
      "isolatedMargin": "23.43",
      "crossedMargin": "34.34",
      "crossedUnrealizedPL": "23",
      "isolatedUnrealizedPL": "0",
      "grant": "0",
      "assetMode": "union"
    }
  ],
  "msg": "success",
  "requestTime": 1630901215622
}
```

## 获取所有子账户合约资产信息

`GET /api/v2/mix/account/sub-account-assets`

限速规则: 1次/10s (uid)

查询所有子账户的合约资产信息。**仅限非代理商(非ND Broker)用户调用。**

Operation ID: `classicContractAccountGetSubAccountContractAssets`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| productType | query | string | 是 | 产品类型<br><br>`USDT-FUTURES` U本位合约<br><br>`COIN-FUTURES` 币本位合约<br><br>`USDC-FUTURES` USDC合约 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].userId | string |  | 子账户userId |
| data[].assetList | object[] |  | 子账户下合约资产集合 |
| data[].assetList[].marginCoin | string |  | 保证金币种 |
| data[].assetList[].locked | string |  | 锁定数量(保证金币种) |
| data[].assetList[].available | string |  | 账户可用数量 |
| data[].assetList[].crossedMaxAvailable | string |  | 全仓最大可用来开仓余额(保证金币种) |
| data[].assetList[].isolatedMaxAvailable | string |  | 逐仓最大可用来开仓余额(保证金币种) |
| data[].assetList[].maxTransferOut | string |  | 最大可转出 |
| data[].assetList[].accountEquity | string |  | 账户权益(保证金币种) |
| data[].assetList[].usdtEquity | string |  | 折算USDT账户权益 |
| data[].assetList[].btcEquity | string |  | 折算BTC账户权益 |
| data[].assetList[].unrealizedPL | string |  | 未平仓损益 |
| data[].assetList[].coupon | string |  | 体验金 |
| data[].assetList[].crossedUnrealizedPL | string |  | 全仓未实现盈亏 |
| data[].assetList[].isolatedUnrealizedPL | string |  | 逐仓未实现盈亏 |
| data[].assetList[].assetMode | string |  | 联合保证金<br><br>`union` 联合保证金<br><br>`single` 单币种保证金 |
| data[].assetList[].grant | string |  | 合约空投券金额 |
| data[].assetList[].isolatedMargin | string |  | 逐仓占用保证金 |
| data[].assetList[].crossedMargin | string |  | 全仓占用保证金 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1767781062372,
  "data": [
    {
      "userId": 1234567890,
      "assetList": [
        {
          "marginCoin": "USDT",
          "locked": "0",
          "available": "0",
          "crossedMaxAvailable": "0",
          "isolatedMaxAvailable": "0",
          "maxTransferOut": "0",
          "accountEquity": "0",
          "usdtEquity": "0",
          "btcEquity": "0",
          "unrealizedPL": "0",
          "coupon": null,
          "crossedUnrealizedPL": null,
          "isolatedUnrealizedPL": null,
          "grant": null,
          "assetMode": null,
          "isolatedMargin": null,
          "crossedMargin": null
        }
      ]
    },
    {
      "userId": 1234567890,
      "assetList": [
        {
          "marginCoin": "USDT",
          "locked": "0",
          "available": "0",
          "crossedMaxAvailable": "0",
          "isolatedMaxAvailable": "0",
          "maxTransferOut": "0",
          "accountEquity": "0",
          "usdtEquity": "0",
          "btcEquity": "0",
          "unrealizedPL": "0",
          "coupon": null,
          "crossedUnrealizedPL": null,
          "isolatedUnrealizedPL": null,
          "grant": null,
          "assetMode": null,
          "isolatedMargin": null,
          "crossedMargin": null
        }
      ]
    }
  ]
}
```

## 获取可开数量

`GET /api/v2/mix/account/open-count`

限速规则: 10次/1s (UID)

获取预估可开数量结果，未计入当前仓位及委托。

Operation ID: `classicContractAccountEstOpenCount`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | 币对，如: ETHUSDT |
| productType | query | string | 是 | 产品类型<br><br>`USDT-FUTURES` U本位合约<br><br>`COIN-FUTURES` 币本位合约<br><br>`USDC-FUTURES` USDC合约 |
| marginCoin | query | string | 是 | 保证金币种 |
| openAmount | query | string | 是 | 保证金数量 |
| openPrice | query | string | 是 | 订单价格 |
| leverage | query | string |  | 杠杆倍数（默认20） |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.size | string |  | 预估可开数量 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695812285073,
  "data": {
    "size": "0.47"
  }
}
```

## 获取预估强平价

`GET /api/v2/mix/account/liq-price`

限速规则: 20次/1s (UID)

获取预估强平价

Operation ID: `classicContractAccountGetLiquidationPrice`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | 币对，如: ETHUSDT |
| productType | query | string | 是 | 产品类型<br><br>`USDT-FUTURES` U本位合约<br><br>`COIN-FUTURES` 币本位合约<br><br>`USDC-FUTURES` USDC合约 |
| marginCoin | query | string | 是 | 保证金币种 |
| posSide | query | string | 是 | 持仓方向<br><br>`long`多<br><br>`short`空 |
| orderType | query | string | 是 | 订单类型<br><br>`limit`限价<br><br>`market`市价 |
| openAmount | query | string | 是 | 开仓数量 |
| openPrice | query | string |  | 开仓价格<br><br>`orderType=limit`时必填 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.liqPrice | string |  | 预估强平价 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1762437950669,
  "data": {
    "liqPrice": "-5025939.4855934659933227"
  }
}
```

## 获取最大可开

`GET /api/v2/mix/account/max-open`

限速规则: 20次/1s (UID)

获取预估可开数量结果，计入当前仓位及委托。

Operation ID: `classicContractAccountGetMaxOpen`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | 币对，如: ETHUSDT |
| productType | query | string | 是 | 产品类型<br><br>`USDT-FUTURES` U本位合约<br><br>`COIN-FUTURES` 币本位合约<br><br>`USDC-FUTURES` USDC合约 |
| marginCoin | query | string | 是 | 保证金币种 |
| posSide | query | string | 是 | 持仓方向<br><br>`long`多<br><br>`short`空 |
| orderType | query | string | 是 | 订单类型<br><br>`limit`限价<br><br>`market`市价 |
| openPrice | query | string |  | 开仓价格<br><br>`orderType=limit`时必填 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.maxOpen | string |  | 最大可开数量 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1762438504409,
  "data": {
    "maxOpen": "17563.78"
  }
}
```

## 调整业务线所有交易对杠杆

`POST /api/v2/mix/account/set-all-leverage`

限速规则: 5次/1s (uid)

调整杠杆倍数

Operation ID: `classicContractAccountChangeAllLeverage`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| productType | string | 是 | 产品类型<br><br>`USDT-FUTURES` U本位合约<br><br>`COIN-FUTURES` 币本位合约<br><br>`USDC-FUTURES` USDC合约 |
| leverage | string | 是 | 杠杆倍数 （仅对开过仓位的交易对生效） |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | string |  | 结果<br><br>`success` 成功<br><br>`failure` 失败 |

```json
{
  "code": "00000",
  "data": "success",
  "msg": "success",
  "requestTime": 1627293049406
}
```

## 调整杠杆

`POST /api/v2/mix/account/set-leverage`

限速规则: 5次/1s (uid)

调整杠杆倍数

注意:全仓模式调整杠杆请使用`leverage`不要使用 `longLeverage`,`shortLeverage` 参数，目前`longLeverage`,`shortLeverage`没有强制校验，如果在全仓时传递这两个也会生效，优先以 `longLeverage` 为准

Operation ID: `classicContractAccountChangeLeverage`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| symbol | string | 是 | 交易币对 |
| productType | string | 是 | 产品类型<br><br>`USDT-FUTURES` U本位合约<br><br>`COIN-FUTURES` 币本位合约<br><br>`USDC-FUTURES` USDC合约 |
| marginCoin | string | 是 | 保证金币种 必须大写 |
| leverage | string |  | 杠杆倍数<br><br>- 适用于全仓模式<br><br>- 适用于逐仓模式的单向持仓场景<br><br>- 适用于逐仓模式的双向持仓下，不同方向设置相同杠杆倍数的场景 |
| longLeverage | string |  | 多仓杠杆<br><br>- 仅适用于逐仓模式的双向持仓下，不同方向设置不同杠杆倍数的场景<br><br>- 双向持仓场景下，如同时传参leverage和longLeverage，则longLeverage生效，leverage将被忽略 |
| shortLeverage | string |  | 空仓杠杆<br><br>- 仅适用于逐仓模式的双向持仓下，不同方向设置不同杠杆倍数的场景<br><br>- 双向持仓场景下，如同时传参leverage和shortLeverage，则shortLeverage生效，leverage将被忽略 |
| holdSide | string |  | 持仓方向<br><br> `long`：多仓；<br><br>`short`：空仓  <br><br>  全仓模式：holdSide 参数不用填 <br><br>  逐仓模式：单向持仓，holdSide 参数不用填; 双向持仓，holdSide 参数必填。且双向持仓多空杠杆同时设置时，holdSide非必填 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.symbol | string |  | 币对名称 |
| data.marginCoin | string |  | 保证金币种 |
| data.longLeverage | string |  | 多仓杠杆 |
| data.shortLeveage | string |  | 空仓杠杆 |
| data.crossMarginLeverage | string |  | 全仓杠杆 |
| data.marginMode | string |  | 保证金模式。 isolated逐仓模式；crossed 全仓模式 |

```json
{
  "code": "00000",
  "data": {
    "symbol": "BTCUSDT",
    "marginCoin": "USDT",
    "longLeverage": "25",
    "shortLeverage": "20",
    "crossMarginLeverage": "20",
    "marginMode": "crossed"
  },
  "msg": "success",
  "requestTime": 1627293049406
}
```

## 调整保证金

`POST /api/v2/mix/account/set-margin`

限速规则: 5次/1s (uid)

增加或减少仓位保证金（**仅限逐仓模式下调用**）

Operation ID: `classicContractAccountChangeMargin`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| symbol | string | 是 | 交易对名称，例如"BTCUSDT" |
| productType | string | 是 | 产品类型<br><br>`USDT-FUTURES` U本位合约<br><br>`COIN-FUTURES` 币本位合约<br><br>`USDC-FUTURES` USDC合约 |
| marginCoin | string | 是 | 保证金币种 必须大写 |
| holdSide | string | 是 | 持仓方向<br><br>long 多仓；short 空仓 |
| amount | string | 是 | 保证金金额<br><br>正数代表增加保证金； 负数代表减少保证金 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | string |  | 处理结果'00000':成功   其它:失败 |

```json
{
  "code": "00000",
  "data": "",
  "msg": "success",
  "requestTime": 1627293357336
}
```

## 设置逐仓仓位自动追加保证金

`POST /api/v2/mix/account/set-auto-margin`

限速规则: 5次/1s (uid)

逐仓自动追加保证金

Operation ID: `classicContractAccountSetAutoMargin`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| symbol | string | 是 | 交易对名称，例如"BTCUSDT" |
| autoMargin | string | 是 | 是否自动追加保证金<br><br>`on` 自动追加<br><br>`off` 关闭自动追加 |
| marginCoin | string | 是 | 保证金币种 必须大写 |
| holdSide | string | 是 | 持仓方向（仅逐仓）<br><br>long 多仓；short 空仓 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | string |  | 处理结果'00000':成功   其它:失败 |

```json
{
  "code": "00000",
  "data": "success",
  "msg": "success",
  "requestTime": 1627293357336
}
```

## 调整保证金模式

`POST /api/v2/mix/account/set-margin-mode`

限速规则: 5次/1s (uid)

有持仓或委托时不能调用本接口

Operation ID: `classicContractAccountChangeMarginMode`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| symbol | string | 是 | 交易币对，如BTCUSDT |
| productType | string | 是 | 产品类型<br><br>`USDT-FUTURES` U本位合约<br><br>`COIN-FUTURES` 币本位合约<br><br>`USDC-FUTURES` USDC合约 |
| marginCoin | string | 是 | 保证金币种 必须大写 |
| marginMode | string | 是 | 保证金模式<br><br>`isolated`: 逐仓模式<br><br>`crossed`: 全仓模式 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.symbol | string |  | 交易对名称 |
| data.marginCoin | string |  | 保证金币种 |
| data.longLeverage | string |  | 多仓杠杆 |
| data.shortLeveage | string |  | 空仓杠杆 |
| data.marginMode | string |  | 保证金模式<br><br>`isolated`: 逐仓模式<br><br>`crossed`: 全仓模式 |

```json
{
  "code": "00000",
  "data": {
    "symbol": "BTCUSDT",
    "marginCoin": "USDT",
    "longLeverage": "25",
    "shortLeverage": "20",
    "marginMode": "isolated"
  },
  "msg": "success",
  "requestTime": 1627293445916
}
```

## 调整单双向持仓模式

`POST /api/v2/mix/account/set-position-mode`

限速规则: 5次/1s (uid)

产品类型下有仓位/委托时不能调整持仓模式。

如果想变换用户在 所有symbol 合约上的持仓模式时，则需指定双向持仓或单向持仓。

指定productType任意币对任意side存在仓位/委托的情况下，请求会失败

Operation ID: `classicContractAccountChangeHoldMode`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| productType | string | 是 | 产品类型<br><br>`USDT-FUTURES` U本位合约<br><br>`COIN-FUTURES` 币本位合约<br><br>`USDC-FUTURES` USDC合约 |
| posMode | string | 是 | 持仓模式<br><br>one_way_mode 单向持仓<br><br>hedge_mode 双向持仓 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.posMode | string |  | 持仓模式<br><br>one_way_mode 单向持仓<br><br>hedge_mode 双向持仓 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1696817554949,
  "data": {
    "posMode": "hedge_mode"
  }
}
```

## 设置U本位合约联合保证金模式

`POST /api/v2/mix/account/set-asset-mode`

限速规则: 2次/1s (uid)

调整U本位合约账户联合保证金模式

Operation ID: `classicContractAccountSetAssetMode`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| productType | string | 是 | 产品类型<br><br>`USDT-FUTURES` USDT专业合约 |
| assetMode | string | 是 | 保证金模式<br><br>`single` 单币种保证金模式<br><br>`union` 多币种联合保证金模式 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | string |  | 'success' 成功 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1725848356656,
  "data": "success"
}
```

## 获取账务记录

`GET /api/v2/mix/account/bill`

限速规则: 10次/1s (uid)

获取账务记录(仅支持查询90天内数据，超过90天数据可以在网页端导出)

Operation ID: `classicContractAccountGetAccountBill`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| productType | query | string | 是 | 产品类型<br><br>`USDT-FUTURES` U本位合约<br><br>`COIN-FUTURES` 币本位合约<br><br>`USDC-FUTURES` USDC合约 |
| coin | query | string |  | 币种<br><br>只在`businessType`为trans_from_exchange和trans_to_exchange时有效 |
| businessType | query | string |  | 业务类型 |
| onlyFunding | query | string |  | 是否剔除以下4种非资金类流水数据,默认值：no，<br><br>`yes`：是<br><br> `no`: 否;<br><br>  过滤的4种流水：`append_margin`,`adjust_down_lever_append_margin`, `reduce_margin`, `auto_append_margin` |
| idLessThan | query | string |  | 用于翻页。首次查询不传，查询第二页及后面的数据时，取上一次查询返回的最后一条repayId，结果会返回小于该值的数据；可以缩短查询响应时间 |
| startTime | query | string |  | 开始时间, ms<br><br>`startTime`和`endTime`时间间隔应小于等于30天 |
| endTime | query | string |  | 结束时间, ms<br><br>`startTime`和`endTime`时间间隔应小于等于30天 |
| limit | query | string |  | 查询页大小，最大100，默认20 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.bills | object[] |  | 列表 |
| data.bills[].billId | string |  | 流水ID |
| data.bills[].symbol | string |  | 币对名称 |
| data.bills[].amount | string |  | 数额 |
| data.bills[].fee | string |  | 手续费 |
| data.bills[].feeByCoupon | string |  | 手续费抵扣 |
| data.bills[].businessType | string |  | 业务类型 |
| data.bills[].coin | string |  | 币种: USDT |
| data.bills[].balance | string |  | 余额 |
| data.bills[].cTime | string |  | 创建时间, ms |
| data.endId | string |  | 最后的跟踪订单id。<br><br>指定idLessThan/idGreaterThan作为范围查询时以此为准。 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695809161807,
  "data": {
    "bills": [
      {
        "billId": "1",
        "symbol": "BTCUSDT",
        "amount": "-0.004992",
        "fee": "0",
        "feeByCoupon": "",
        "businessType": "contract_settle_fee",
        "coin": "USDT",
        "balance": "232.21",
        "cTime": "1695715200654"
      },
      {
        "billId": "2",
        "symbol": "ETHUSDT",
        "amount": "0",
        "fee": "-0.222012",
        "feeByCoupon": "",
        "businessType": "open_long",
        "coin": "USDT",
        "balance": "232.21",
        "cTime": "1695714563516"
      }
    ],
    "endId": "2"
  }
}
```

## U本位合约利息记录

`GET /api/v2/mix/account/interest-history`

限速规则: 5次/1s (uid)

获取U本位合约利息记录

Operation ID: `classicContractAccountInterestHistory`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| coin | query | string |  | 币种 只能传 `USDT` |
| productType | query | string | 是 | 产品类型<br><br>`USDT-FUTURES` USDT专业合约 |
| idLessThan | query | string |  | 请求返回数据的`endId`之前（更旧的数据）的分页内容。 |
| startTime | query | string | 是 | 开始时间 （时间戳毫秒） |
| endTime | query | string | 是 | 结束时间 （时间戳毫秒） |
| limit | query | string |  | 查询条数 默认100，最大100 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.nextSettleTime | string |  | 下一次利息结算时间 |
| data.borrowAmount | string |  | U本位合约借款总额 |
| data.borrowLimit | string |  | 借款限额 |
| data.interestList | object[] |  | 利息集合 |
| data.interestList[].coin | string |  | 币种 |
| data.interestList[].liability | string |  | 总负债 |
| data.interestList[].interestFreeLimit | string |  | 免息额度 |
| data.interestList[].interestLimit | string |  | 计息额度 |
| data.interestList[].hourInterestRate | string |  | 每小时借贷利率 |
| data.interestList[].cTime | string |  | 利息收取时间 |
| data.interestList[].interest | string |  | 利息 |
| data.endId | string |  | 最后数据的id。<br><br>指定idLessThan作为范围查询时以此为准。 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1725875190690,
  "data": {
    "nextSettleTime": "1725876300000",
    "borrowAmount": "0",
    "borrowLimit": "600000",
    "interestList": [
      {
        "coin": "USDT",
        "liability": "100",
        "interestFreeLimit": "100",
        "interestLimit": "500",
        "hourInterestRate": "0.12",
        "interest": "0.12",
        "cTime": "1725848567893"
      }
    ],
    "endId": "xxxxxxxxxxxxxxx"
  }
}
```

## 联合保证金兑换

`POST /api/v2/mix/account/union-convert`

限速规则: 1次/1s (uid)

联合保证金兑换

Operation ID: `classicContractAccountUnionConvert`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| coin | string | 是 | 兑换币种<br><br>如BTC |
| amount | string | 是 | 兑换数量<br><br>单位为兑换币种 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.usdtAmount | string |  | 兑换的USDT数量 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1627293357336,
  "data": {
    "usdtAmount": "1"
  }
}
```

## 获取联合保证金币种划转限制

`GET /api/v2/mix/account/transfer-limits`

限速规则: 1次/1s (uid)

获取联合保证金币种划转限制

Operation ID: `classicContractAccountGetUnionTransferLimits`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| coin | query | string | 是 | 币种名称<br><br>如BTC |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.coin | string |  | 币种名称 |
| data.maxTransferIn | string |  | 最大可转入数量<br><br>单位为coin |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1627293357336,
  "data": {
    "coin": "BTC",
    "maxTransferIn": "100"
  }
}
```

## 获取联合保证金配置参数

`GET /api/v2/mix/account/union-config`

限速规则: 1次/1s (uid)

获取联合保证金配置参数接口（负债初始保证金率，负债维持保证金率，个人负债上限，个人负债上限比例）

Operation ID: `classicContractAccountGetUnionConfig`

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.imr | string |  | 负债初始保证金率<br><br>小数格式。固定值0.1 |
| data.mmr | string |  | 负债维持保证金率<br><br>小数格式。固定值0.05 |
| data.individualLimit | string |  | 个人负债上限<br><br>单位为USDT |
| data.individualLimitRatio | string |  | 个人负债上限比例<br><br>小数格式。如0.8代表80% |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1627293357336,
  "data": {
    "imr": "0.1",
    "mmr": "0.05",
    "individualLimit": "10000",
    "individualLimitRatio": "0.8"
  }
}
```

## 获取联合保证金切换单币种保证金所需USDT额度

`GET /api/v2/mix/account/switch-union-usdt`

限速规则: 1次/1s (uid)

获取联合保证金切换单币种保证金所需USDT额度

Operation ID: `classicContractAccountGetSwitchUnionUSDT`

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.usdtAmount | string |  | 账户模式切换所需USDT额度 <br><br> 单位为USDT |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695809161807,
  "data": {
    "usdtAmount": "1"
  }
}
```

## 获取逐仓模式交易对

`GET /api/v2/mix/account/isolated-symbols`

限速规则: 10次/1s (uid)

获取账户下的逐仓模式交易对

Operation ID: `classicContractAccountGetIsolatedSymbols`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| productType | query | string | 是 | 产品类型<br><br>`USDT-FUTURES` U本位合约<br><br>`COIN-FUTURES` 币本位合约<br><br>`USDC-FUTURES` USDC合约 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].symbol | string |  | 交易对名称 |
| data[].marginMode | string |  | 保证金模式<br><br>固定值为`isolated` |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1761568886493,
  "data": [
    {
      "symbol": "COAIUSDT",
      "marginMode": "isolated"
    },
    {
      "symbol": "EVAAUSDT",
      "marginMode": "isolated"
    }
  ]
}
```