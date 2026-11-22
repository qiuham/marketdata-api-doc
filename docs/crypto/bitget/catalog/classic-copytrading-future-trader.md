---
exchange: bitget
source_url: https://www.bitget.com/docs/catalog/classic-copytrading-future-trader
api_type: REST
updated_at: 2026-11-22 19:01:03.440946
---

# Classic Futures Copy Trading Trader API

Classic account — futures copy trading trader endpoints.

版本: 1.0.0

## 服务地址

- `https://api.bitget.com`

## 接口列表

- `POST /api/v2/copy/mix-trader/create-copy-api` — Create Copy ApiKey
- `GET /api/v2/copy/mix-trader/order-current-track` — Get Current Tracking Orders
- `GET /api/v2/copy/mix-trader/order-history-track` — Get History Tracking Orders
- `POST /api/v2/copy/mix-trader/order-close-positions` — Close Tracking Order
- `POST /api/v2/copy/mix-trader/order-modify-tpsl` — Modify Tracking Order TPSL
- `GET /api/v2/copy/mix-trader/order-total-detail` — Get Tracking Order Summary
- `GET /api/v2/copy/mix-trader/profit-history-summarys` — Get History Profit Summary
- `GET /api/v2/copy/mix-trader/profit-history-details` — Get History Profit Share Detail
- `GET /api/v2/copy/mix-trader/profit-details` — Get Profit Share Detail
- `GET /api/v2/copy/mix-trader/profits-group-coin-date` — Get Profit Share Group by Coin & Date
- `GET /api/v2/copy/mix-trader/config-query-symbols` — Get Copy Trade Symbol Settings
- `POST /api/v2/copy/mix-trader/config-setting-symbols` — Change Copy Trade Symbol Setting
- `POST /api/v2/copy/mix-trader/config-settings-base` — Change Global Copy Trade Setting
- `GET /api/v2/copy/mix-trader/config-query-followers` — Get My Followers
- `POST /api/v2/copy/mix-trader/config-remove-follower` — Remove Follower

## Create Copy ApiKey

`POST /api/v2/copy/mix-trader/create-copy-api`

Rate Limit: 1 req/sec/UID

This interface is used for the new version of Copy Traders to create a Copy API Key, which is of HMAC type. Old version Copy Traders will receive an error message "This interface is only applicable to the new Copy model" when calling the interface.

The new version of Copy Traders have user identifiers on the following side. These traders support selecting both [Futures Trading] and [Copy Trading] when engaging in contract transactions.

The Copy Trading API Key can only be created once. If a user attempts to create another one while already having a Copy API Key, an error will be returned stating "You have already created a Copy API Key."

For elite traders, please strictly adhere to the list of trading pairs specified in the Available trading pairs and parameters for elite traders when placing orders using the Copy Trading API Key. Trading pairs outside the announced list are not available for copy trading.

Operation ID: `classicCopytradingFutureCopytradeTraderCreateCopyApi`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| passphrase | string | 是 | Password length must be 8 to 32 characters, consisting of English letters and numbers. |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].apikey | string |  | API Key. |
| data[].secret | string |  | API Secret. |
| data[].permissions | string[] |  | API Key permissions: <br><br>`contract_trade`Contract trade.<br><br>`copytrading_trade`Copy trade |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695872676719,
  "data": [
    {
      "apikey": "bg_xxxxxxxxxxxxxxxxxxxx",
      "secret": "**********",
      "permissions": [
        "copytrading_trade",
        "contract_trade"
      ]
    }
  ]
}
```

## Get Current Tracking Orders

`GET /api/v2/copy/mix-trader/order-current-track`

Rate Limit: 5 req/sec/UID

Operation ID: `classicCopytradingFutureCopytradeTraderTraderOrderCurrentTrack`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string |  | Trading pair<br><br>Supports capital and lower-case letters |
| productType | query | string | 是 | Product type<br><br>`USDT-FUTURES` USDT-M Futures<br><br>`COIN-FUTURES` Coin-M Futures<br><br>`USDC-FUTURES` USDC-M Futures |
| startTime | query | string |  | Start time (greater than or equal to) Unix timestamp in milliseconds format, e.g. 1597026383085, rounded down according to granularity, i.e. for granularity=1m: 1672410799436 (December 30, 2022, 22:33:19) rounded down to 1672410780000 (December 30, 2022, 22:33:00)<br><br>Request data generated after this start time<br><br>(If end time is not input, then estimates out the start time based on the current time) |
| endTime | query | string |  | Start time (greater than or equal to) Unix timestamp in milliseconds format, e.g. 1597026383085, rounded down according to granularity, i.e. for granularity=1m: 1672410799436 (December 30, 2022, 22:33:19) rounded down to 1672410780000 (December 30, 2022, 22:33:00)<br><br>Request data generated before this start time |
| limit | query | string |  | default 20, max 50 |
| idGreaterThan | query | string |  | Requests the content on the page after this ID (newer data), the value input should be the endId of the corresponding interface. |
| idLessThan | query | string |  | Separate page content before this ID is requested (older data), the value input should be the endId of the corresponding interface. |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.trackingList | object[] |  | Track order list |
| data.trackingList[].trackingNo | string |  | Track order number |
| data.trackingList[].symbol | string |  | Trading pair name |
| data.trackingList[].posSide | string |  | Position direction<br><br>`long`: long position in hedging mode<br><br>`short`: short position in hedging mode |
| data.trackingList[].openOrderId | string |  | Elite trader opening order ID |
| data.trackingList[].openLeverage | string |  | Leverage to open positions |
| data.trackingList[].openPriceAvg | string |  | Average entry price |
| data.trackingList[].openTime | string |  | Opening time |
| data.trackingList[].openSize | string |  | Position size to open |
| data.trackingList[].presetStopSurplusPrice | string |  | Set TP price |
| data.trackingList[].presetStopLossPrice | string |  | Set SL price |
| data.trackingList[].openFee | string |  | Opening fee<br><br>(Shows USDT only, not coupons) |
| data.trackingList[].followCount | string |  | Number of followers for this order |
| data.endId | string |  | This is used when idLessThan/idGreaterThan is set as a range. |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695801601016,
  "data": {
    "trackingList": [
      {
        "trackingNo": "1231231231",
        "openOrderId": "123123123123",
        "symbol": "BTCUSDT",
        "posSide": "long",
        "openLeverage": "20",
        "openPriceAvg": "26248.9",
        "openTime": "1695801595658",
        "openSize": "0.1000000000000000",
        "presetStopSurplusPrice": "27561.34",
        "presetStopLossPrice": "25855.16",
        "openFee": "-2.62489",
        "followCount": "1"
      }
    ],
    "endId": "1"
  }
}
```

## Get History Tracking Orders

`GET /api/v2/copy/mix-trader/order-history-track`

Rate Limit: 5 req/sec/UID

Operation ID: `classicCopytradingFutureCopytradeTraderTraderOrderHistoryTrack`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| idLessThan | query | string |  | Separate page content before this ID is requested (older data), and the value input should be the endid of the corresponding interface. |
| idGreaterThan | query | string |  | Separate page content after this ID is requested (newer data), and the value input should be the endid of the corresponding interface. |
| startTime | query | string |  | Start timestamp <br><br>(order creation time)<br><br>Milliseconds format of timestamp Unix, e.g. 1597026383085<br><br>(The maximum time span supported is three months. The default end time is three months if no value is set for the end time. ) |
| endTime | query | string |  | End timestamp <br><br>(order creation time)<br><br>Milliseconds format of timestamp Unix, e.g. 1597026383085<br><br>(The maximum time span supported is three months. The default start time is three months ago if no value is set for the start time. ) |
| limit | query | string |  | Number of queries: Default: 20, maximum: 100. |
| order | query | string |  | Sorting rules (creation time): Default: desc |
| symbol | query | string |  | Trading pair<br><br>Supports capital and lower-case letters |
| productType | query | string | 是 | Product type<br><br>`USDT-FUTURES` USDT-M Futures<br><br>`COIN-FUTURES` Coin-M Futures<br><br>`USDC-FUTURES` USDC-M Futures |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.trackingList | object[] |  | Overview of elite trade records |
| data.trackingList[].trackingNo | string |  | Track order number |
| data.trackingList[].symbol | string |  | Trading pair name |
| data.trackingList[].openOrderId | string |  | Opening order ID |
| data.trackingList[].closeOrderId | string |  | Closing order ID |
| data.trackingList[].productType | string |  | Product type<br><br>`USDT-FUTURES` USDT-M Futures<br><br>`COIN-FUTURES` Coin-M Futures<br><br>`USDC-FUTURES` USDC-M Futures |
| data.trackingList[].posSide | string |  | Position direction<br><br>`long`: long position in hedging mode<br><br>`short`: short position in hedging mode |
| data.trackingList[].openLeverage | string |  | Leverage to open positions |
| data.trackingList[].openPriceAvg | string |  | Average entry price |
| data.trackingList[].openTime | string |  | Time to open position (milliseconds) |
| data.trackingList[].openSize | string |  | Position size to open |
| data.trackingList[].closeSize | string |  | Closed quantity |
| data.trackingList[].closeTime | string |  | Time to close position (milliseconds) |
| data.trackingList[].closePriceAvg | string |  | Average exit price |
| data.trackingList[].stopType | string |  | Type of position closed<br><br>`profit`<br><br>`loss` |
| data.trackingList[].achievedPL | string |  | Realized PnL |
| data.trackingList[].openFee | string |  | Opening fee<br><br>(Shows USDT only, not coupons) |
| data.trackingList[].closeFee | string |  | Closing fee<br><br>(Shows USDT only, not coupons) |
| data.trackingList[].cTime | string |  | Order creation time |
| data.endId | string |  | Final tracking order ID.<br><br>This is used when idLessThan/idGreaterThan is set as a range. |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695802740184,
  "data": {
    "trackingList": [
      {
        "trackingNo": "123123",
        "symbol": "BTCUSDT",
        "openOrderId": "12312313123",
        "closeOrderId": "12312313123",
        "productType": "usdt-futures",
        "posSide": "long",
        "openLeverage": "20",
        "openPriceAvg": "32000.5",
        "openTime": "1695035398292",
        "openSize": "0.1000",
        "closeSize": "0.1000",
        "closeTime": "1695176679764",
        "closePriceAvg": "32000.0",
        "stopType": "",
        "achievedPL": "-0.05000000",
        "openFee": "-3.20005000",
        "closeFee": "-3.20000000",
        "cTime": "1695035398292"
      }
    ],
    "endId": "1"
  }
}
```

## Close Tracking Order

`POST /api/v2/copy/mix-trader/order-close-positions`

Rate Limit: 5 req/sec/UID

Tracking orders could only be closed by this API

Operation ID: `classicCopytradingFutureCopytradeTraderTraderOrderClosePositions`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| trackingNo | string |  | Track order number <br><br>Tracking ID from the current elite trade interface<br><br>If a symbol is also passed, make sure the order ID pair corresponds to it. |
| symbol | string |  | Trading pair<br><br>Supports capital and lower-case letters |
| productType | string | 是 | Product type<br><br>`USDT-FUTURES` USDT-M Futures<br><br>`COIN-FUTURES` Coin-M Futures<br><br>`USDC-FUTURES` USDC-M Futures<br><br>If only productType is passed, all positions under that line of business will be closed. |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].trackingNo | string |  | Track order number |
| data[].symbol | string |  | Trading pair |
| data[].productType | string |  | Product type |

```json
{
  "code": "00000",
  "data": [
    {
      "trackingNo": "123",
      "symbol": "ETHUSDT",
      "productType": "USDT-FUTURES"
    },
    {
      "trackingNo": "32123",
      "symbol": "BTCUSDT",
      "productType": "USDT-FUTURES"
    }
  ],
  "msg": "success",
  "requestTime": 1627354109502
}
```

## Modify Tracking Order TPSL

`POST /api/v2/copy/mix-trader/order-modify-tpsl`

Rate Limit: 5 req/sec/UID

Operation ID: `classicCopytradingFutureCopytradeTraderTraderOrderModifyTpsl`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| symbol | string |  | Symbol name<br><br>e.g.,`BTCUSDT` |
| trackingNo | string | 是 | Elite trade order ID |
| productType | string | 是 | Product type<br><br>`USDT-FUTURES` USDT-M Futures<br><br>`COIN-FUTURES` Coin-M Futures<br><br>`USDC-FUTURES` USDC-M Futures |
| stopSurplusPrice | string |  | TP price<br><br>One of stopSurplusPrice and stopLossPrice must be passed.<br><br>When it is empty, it is ignored or not updated, no matter take-profit exists or not,<br><br>When it is 0, it means the original take-profit is canceled if there is a take-profit already.<br><br>When it is greater than or equal to 0, it means take-profit is updated or set. |
| stopLossPrice | string |  | SL price<br><br>One of stopSurplusPrice and stopLossPrice must be passed.<br><br>When it is empty, it is ignored or not updated, no matter stop-loss exists or not,<br><br>When it is 0, it means the original stop-loss is canceled if there is a stop-loss already.<br><br>When it is greater than or equal to 0, it means stop-loss is updated or set. |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | string |  | Implementation results<br><br>`success` `fail` |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1656066841304,
  "data": "success"
}
```

## Get Tracking Order Summary

`GET /api/v2/copy/mix-trader/order-total-detail`

Rate Limit: 5 req/sec/UID

Operation ID: `classicCopytradingFutureCopytradeTraderTraderOrderTotalDetail`

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.roi | string |  | ROI |
| data.tradingOrderNum | string |  | Total opening orders |
| data.totalFollowerNum | string |  | Total followers |
| data.currentFollowerNum | string |  | Current number of followers |
| data.totalpl | string |  | Total profit<br><br>(calculated in USD) |
| data.gainNum | string |  | Ratio of profitable trades |
| data.lossNum | string |  | Ratio of losing trades |
| data.totalEquity | string |  | Total assets |
| data.winRate | string |  | Win rate |
| data.tradingPairsAvailableList | string[] |  | Available trading pairs |
| data.lastWeekRoiList | object[] |  | ROI in the last week |
| data.lastWeekRoiList[].rate | string |  | Rate of profit |
| data.lastWeekRoiList[].ctime | string |  | Time(timestamp) |
| data.lastWeekProfitList | object[] |  | Profit in the past week |
| data.lastWeekProfitList[].amount | string |  | Profit, USDT |
| data.lastWeekProfitList[].ctime | string |  | Time(timestamp) |
| data.lastMonthRoiList | object[] |  | ROI in the last month |
| data.lastMonthRoiList[].rate | string |  | Rate of profit |
| data.lastMonthRoiList[].ctime | string |  | Time(timestamp) |
| data.lastMonthProfitList | object[] |  | Profit in the last month |
| data.lastMonthProfitList[].amount | string |  | Profit, USDT |
| data.lastMonthProfitList[].ctime | string |  | Time(timestamp) |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695805917634,
  "data": {
    "roi": "19.38",
    "tradingOrderNum": "105",
    "totalFollowerNum": "134",
    "currentFollowerNum": "4",
    "totalpl": "$46.95",
    "gainNum": "59",
    "lossNum": "46",
    "winRate": "56.123",
    "tradingPairsAvailableList": [
      "BTCUSDT"
    ],
    "lastWeekRoiList": [
      {
        "rate": "-14.130944",
        "ctime": "1695139200000"
      }
    ],
    "lastWeekProfitList": [],
    "lastMonthRoiList": [
      {
        "rate": "-14.130944",
        "ctime": "1693152000000"
      }
    ],
    "totalEquity": "1776.03"
  }
}
```

## Get History Profit Summary

`GET /api/v2/copy/mix-trader/profit-history-summarys`

Rate Limit: 5 req/sec/UID

Operation ID: `classicCopytradingFutureCopytradeTraderTraderProfitHistorySummarys`

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.profitSummary | object |  | Elite trader profit share overview |
| data.profitSummary.yesterdayProfit | string |  | Yesterday's profit share (elite trader) |
| data.profitSummary.yesterdayTime | string |  | Yesterday's profit sharing time (milliseconds) |
| data.profitSummary.sumProfit | string |  | Profit share in total |
| data.profitSummary.waitProfit | string |  | To be shared |
| data.profitHistoryList | object[] |  | Trader profit sharing summary information |
| data.profitHistoryList[].coin | string |  | Settlement currency<br><br>(in cryptocurrency) |
| data.profitHistoryList[].profitCount | string |  | Profit overview<br><br>(in cryptocurrency) |
| data.profitHistoryList[].lastProfitTime | string |  | The last time to distribute profit share (milliseconds)<br><br>(in cryptocurrency) |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1698200382922,
  "data": {
    "profitSummary": {
      "yesterdayProfit": "0",
      "sumProfit": "26.4519",
      "waitProfit": "0",
      "yesterdayTime": "1698076800000"
    },
    "profitHistoryList": [
      {
        "coin": "USDT",
        "profitCount": "24.28410397",
        "lastProfitTime": "1698076800000"
      }
    ]
  }
}
```

## Get History Profit Share Detail

`GET /api/v2/copy/mix-trader/profit-history-details`

Rate Limit: 5 req/sec/UID

Operation ID: `classicCopytradingFutureCopytradeTraderTraderProfitHistoryDetails`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| coin | query | string |  | Settlement currency |
| idLessThan | query | string |  | Separate page content before this ID is requested (older data), and the value input should be the endid of the corresponding interface. |
| idGreaterThan | query | string |  | Separate page content after this ID is requested (newer data), and the value input should be the endid of the corresponding interface. |
| startTime | query | string |  | Start timestamp <br><br>Milliseconds format of timestamp Unix, e.g. 1597026383085<br><br>(The maximum time span supported is three months. The default end time is three months if no value is set for the end time. ) |
| endTime | query | string |  | End timestamp <br><br>Milliseconds format of timestamp Unix, e.g. 1597026383085<br><br>(The maximum time span supported is three months. The default start time is three months ago if no value is set for the start time. ) |
| limit | query | string |  | Number of queries: Default: 100, maximum: 100 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.profitList | object[] |  | profit share overview |
| data.profitList[].profitId | string |  | Profit share ID |
| data.profitList[].coin | string |  | Settlement currency |
| data.profitList[].profit | string |  | Distributed |
| data.profitList[].nickName | string |  | Alias |
| data.profitList[].profitTime | string |  | Time to distribute profit share |
| data.endId | string |  | The last profit share ID.<br><br>This is used when idLessThan/idGreaterThan is set as a range. |

```json
{
  "code": "00000",
  "data": {
    "profitList": [
      {
        "profitId": "1",
        "coin": "usdt",
        "profit": "1",
        "nickName": "nickname",
        "profitTime": "1691446639000"
      }
    ],
    "endId": "3"
  },
  "msg": "success",
  "requestTime": 1627354109502
}
```

## Get Profit Share Detail

`GET /api/v2/copy/mix-trader/profit-details`

Rate Limit: 5 req/sec/UID

Operation ID: `classicCopytradingFutureCopytradeTraderTraderProfitDetails`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| coin | query | string |  | Settlement currency of profit share |
| pageSize | query | string |  | Number of inquiries <br><br>Default: 20, maximum: 100 |
| pageNo | query | string |  | Current page number<br><br>Default to 1. |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].coin | string |  | Settlement currency |
| data[].profit | string |  | Profit share |
| data[].nickName | string |  | Alias |

```json
{
  "code": "00000",
  "data": [
    {
      "coin": "usdt",
      "profit": "0",
      "nickName": "nickname"
    }
  ],
  "msg": "success",
  "requestTime": 1627354109502
}
```

## Get Profit Share Group by Coin & Date

`GET /api/v2/copy/mix-trader/profits-group-coin-date`

Rate Limit: 5 req/sec/UID

Operation ID: `classicCopytradingFutureCopytradeTraderTraderGetProfitsGroupCoinDate`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| pageSize | query | string |  | Number of inquiries <br><br>Defaults to 20 entries and supports a maximum of 50 entries. |
| pageNo | query | string |  | Current page number<br><br>Default to 1. |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].coin | string |  | Cryptocurrency |
| data[].profit | string |  | PnL<br><br>(in the dimension of the cryptocurrency and the date) |
| data[].profitTime | string |  | Time to distribute profit share (milliseconds)<br><br>(in the dimension of the cryptocurrency and the date) |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695807225928,
  "data": [
    {
      "coin": "usdt",
      "profit": "15",
      "profitTime": "1627354109502"
    }
  ]
}
```

## Get Copy Trade Symbol Settings

`GET /api/v2/copy/mix-trader/config-query-symbols`

Rate limit:  5 req/sec/UID

Operation ID: `classicCopytradingFutureCopytradeTraderTraderGetConfigQuerySymbols`

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
| data[].symbol | string |  | Trading pair |
| data[].openTrader | string |  | Activates copy trading or not, `YES`, `NO` |
| data[].minOpenCount | string |  | Minimum opening amount of elite traders |
| data[].maxLeverage | string |  | Maximum leverage |
| data[].stopSurplusRatio | string |  | Value set for take profit (value is a positive integer, 120 means 120%) |
| data[].stopLossRatio | string |  | Value set for stop-loss ratio (the value is a positive integer, 40 means 40%) |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695807225928,
  "data": [
    {
      "symbol": "BTCUSDT",
      "openTrader": "yes",
      "minOpenCount": "0.002",
      "maxLeverage": "50",
      "stopSurplusRatio": "100",
      "stopLossRatio": "30"
    }
  ]
}
```

## Change Copy Trade Symbol Setting

`POST /api/v2/copy/mix-trader/config-setting-symbols`

Rate limit:  5 req/sec/UID

Operation ID: `classicCopytradingFutureCopytradeTraderTraderConfigSettingSymbols`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| settingList | object[] | 是 | Setting overview<br><br>Maximum: 50 |
| settingList[].symbol | string | 是 | Trading pair |
| settingList[].productType | string | 是 | Product type<br><br>`USDT-FUTURES` USDT-M Futures<br><br>`COIN-FUTURES` Coin-M Futures<br><br>`USDC-FUTURES` USDC-M Futures |
| settingList[].settingType | string | 是 | Setting type, `ADD`, `DELETE`, `UPDATE` |
| settingList[].stopSurplusRatio | string |  | Take-profit ratio <br><br>positive integers within 1-400,Value exceeding this number is invalid.<br><br>2. When a type is deleted: this value is invalid.<br><br>3. When a type is added: when the take-profit ratio is empty, then the take-profit ratio is not set by default.<br><br>4. When a type is updated: if the value is empty, it means that no change is made; if it is 0, it means that the previously set take-profit is canceled; if it is greater than 0, it means that the take-profit is added or updated.<br><br>One of stopSurplusRatio and stopLossRatio must be passed when the type is updated. |
| settingList[].stopLossRatio | string |  | Stop-loss ratio<br><br>positive integers within 1-400,Value exceeding this number is invalid.<br><br>2. When a type is deleted: this value is invalid.<br><br>3. When a type is added: when the stop-loss ratio is empty, then the stop-loss ratio is not set by default.<br><br>4. When a type is updated: if the value is empty, it means that no change is made; if it is 0, it means that the previously set take-profit is canceled; if it is greater than 0, it means that the stop-loss is added or updated.`<br><br>One of stopSurplusRatio and stopLossRatio must be passed when the type is updated. |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | string |  | Setting results |

```json
{
  "code": "00000",
  "data": "success",
  "msg": "success",
  "requestTime": 1627354109502
}
```

## Change Global Copy Trade Setting

`POST /api/v2/copy/mix-trader/config-settings-base`

Rate Limit: 5 req/sec/UID

Operation ID: `classicCopytradingFutureCopytradeTraderTraderConfigSettingsBase`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| enable | string |  | One of the three must be passed.<br><br>Activates elite trading or not? <br><br>`YES` <br><br> `NO` |
| showTotalEquity | string |  | One of the three must be passed.<br><br>Displays total assets (USDT) or not? <br><br>`YES` <br><br> `NO` |
| showTpsl | string |  | One of the three must be passed.<br><br>TP/SL price of orders will be displayed publicly. <br><br>`YES` <br><br> `NO` |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | string |  | Success or not |

```json
{
  "code": "00000",
  "data": "success",
  "msg": "success",
  "requestTime": 1627354109502
}
```

## Get My Followers

`GET /api/v2/copy/mix-trader/config-query-followers`

Rate Limit: 5 req/sec/UID

Operation ID: `classicCopytradingFutureCopytradeTraderConfigQueryFollowers`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| pageNo | query | string |  | Page number<br><br>(default: 1) |
| pageSize | query | string |  | Entries per page<br><br>(default: 20, maximum: 100) |
| startTime | query | string |  | Start timestamp <br><br>Milliseconds format of timestamp Unix, e.g. 1597026383085<br><br>(The maximum time span supported is three months. The default end time is three months if no value is set for the end time. ) |
| endTime | query | string |  | End timestamp <br><br>Milliseconds format of timestamp Unix, e.g. 1597026383085<br><br>(The maximum time span supported is three months. The default start time is three months ago if no value is set for the start time. ) |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].accountEquity | string |  | Total account assets |
| data[].isRemove | string |  | Is it able to remove followers?<br><br>`yes`<br><br>`no` |
| data[].followerHeadPic | string |  | Follower avatar |
| data[].followerName | string |  | Follower alias |
| data[].followerUid | string |  | Follower user ID |
| data[].followerTime | string |  | Date of following (based on date of initial following)<br><br>Milliseconds format of timestamp Unix, e.g. 1597026383085 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1684920707124,
  "data": [
    {
      "accountEquity": "3434361.0097",
      "isRemove": "yes",
      "followerHeadPic": "",
      "followerName": "****@***.com",
      "followerUid": "************",
      "followerTime": "1684920707124"
    }
  ]
}
```

## Remove Follower

`POST /api/v2/copy/mix-trader/config-remove-follower`

Rate limit: 5 req/sec/UID

Operation ID: `classicCopytradingFutureCopytradeTraderConfigRemoveFollower`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| followerUid | string | 是 | Follower UID |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | string |  | success |

```json
{
  "code": "00000",
  "data": "success",
  "msg": "success",
  "requestTime": 1627354109502
}
```


---

经典账户 — 合约跟单带单员相关接口。

版本: 1.0.0

## 服务地址

- `https://api.bitget.com`

## 接口列表

- `POST /api/v2/copy/mix-trader/create-copy-api` — 新版带单员创建带单API Key接口
- `GET /api/v2/copy/mix-trader/order-current-track` — 交易员获取当前带单
- `POST /api/v2/copy/mix-trader/order-modify-tpsl` — 交易员修改带单止盈止损
- `GET /api/v2/copy/mix-trader/order-history-track` — 交易员获取历史带单
- `POST /api/v2/copy/mix-trader/order-close-positions` — 交易员平仓接口
- `GET /api/v2/copy/mix-trader/order-total-detail` — 查看交易员数据指标统计
- `GET /api/v2/copy/mix-trader/profit-history-summarys` — 交易员历史分润汇总
- `GET /api/v2/copy/mix-trader/profit-history-details` — 交易员历史分润明细
- `GET /api/v2/copy/mix-trader/profit-details` — 交易员待分润明细
- `GET /api/v2/copy/mix-trader/profits-group-coin-date` — 交易员历史分润汇总(按结算币种和日期)
- `GET /api/v2/copy/mix-trader/config-query-symbols` — 交易员获取带单交易对
- `POST /api/v2/copy/mix-trader/config-setting-symbols` — 交易员设置跟单交易对
- `POST /api/v2/copy/mix-trader/config-settings-base` — 交易员修改带单设置
- `GET /api/v2/copy/mix-trader/config-query-followers` — 获取我的跟随者列表
- `POST /api/v2/copy/mix-trader/config-remove-follower` — 交易员取消跟随者

## 新版带单员创建带单API Key接口

`POST /api/v2/copy/mix-trader/create-copy-api`

限频规则: 1次/秒/UID

该接口用于新版带单员创建带单API Key，为HMAC类型。老版带单员调用接口报错“该接口仅适用于新版带单模式”

新版带单员在跟单侧有用户标识，此类交易员在合约交易时支持选择[合约交易]及[带单交易]

带单交易API Key仅支持创建一个。如果用户在已有带单API Key情况下重复调用，则报错“您已创建带单API Key”

为确保带单操作顺利进行，使用新版交易专家的带单 API Key 下单时，请严格按照交易专家可以带单的币对及参数中的币对范围执行。超出公告列表的币对不支持带单下单

Operation ID: `classicCopytradingFutureCopytradeTraderCreateCopyApi`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| passphrase | string | 是 | 密钥<br><br>长度为8至32位的英文字母与数字组合 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].apikey | string |  | 带单交易api key |
| data[].secret | string |  | 带单交易api 密钥 |
| data[].permissions | string[] |  | 带单交易API Key权限<br><br>`contract_trade`合约交易<br><br>`copytrading_trade`跟单交易 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695872676719,
  "data": [
    {
      "apikey": "bg_xxxxxxxxxxxxxxxxxxxx",
      "secret": "**********",
      "permissions": [
        "copytrading_trade",
        "contract_trade"
      ]
    }
  ]
}
```

## 交易员获取当前带单

`GET /api/v2/copy/mix-trader/order-current-track`

限频规则: 5次/秒/UID

Operation ID: `classicCopytradingFutureCopytradeTraderTraderOrderCurrentTrack`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string |  | 交易对 eg: BTCUSDT |
| productType | query | string | 是 | 产品类型<br><br>`USDT-FUTURES` U本位合约<br><br>`COIN-FUTURES` 币本位合约<br><br>`USDC-FUTURES` USDC合约 |
| startTime | query | string |  | 开始时间戳 <br><br>(跟单创建时间)<br><br>Unix时间戳的毫秒数格式，如 1597026383085<br><br>（时间跨度最大支持三个月，若不传结束时间，则默认结束时间为三个月。） |
| endTime | query | string |  | 结束时间戳 默认当前时间<br><br>(跟单创建时间)<br><br>Unix时间戳的毫秒数格式，如 1597026383085<br><br>（时间跨度最大支持三个月，若不传开始时间，则默认开始时间为三个月。） |
| limit | query | string |  | 查询条数,默认为20条，最大支持50条。 |
| idGreaterThan | query | string |  | 根据 endId 往前分页查询 |
| idLessThan | query | string |  | 根据 endId 往后分页查询 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.trackingList | object[] |  | 跟踪订单列表 |
| data.trackingList[].trackingNo | string |  | 跟踪订单号 |
| data.trackingList[].symbol | string |  | 交易对 |
| data.trackingList[].posSide | string |  | 仓位方向, `long`, `short` |
| data.trackingList[].openOrderId | string |  | 开单订单号 |
| data.trackingList[].openLeverage | string |  | 开单杠杆倍数 |
| data.trackingList[].openPriceAvg | string |  | 开单成交价均价 |
| data.trackingList[].openTime | string |  | 开单时间 |
| data.trackingList[].openSize | string |  | 开单数量 |
| data.trackingList[].presetStopSurplusPrice | string |  | 预设止盈价 |
| data.trackingList[].presetStopLossPrice | string |  | 预设止损价 |
| data.trackingList[].openFee | string |  | 开仓价格 |
| data.trackingList[].followCount | string |  | 当前带单跟单人数 |
| data.endId | string |  | 分页参数 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695801601016,
  "data": {
    "trackingList": [
      {
        "trackingNo": "1231231231",
        "openOrderId": "123123123123",
        "symbol": "BTCUSDT",
        "posSide": "long",
        "openLeverage": "20",
        "openPriceAvg": "26248.9",
        "openTime": "1695801595658",
        "openSize": "0.1000000000000000",
        "presetStopSurplusPrice": "27561.34",
        "presetStopLossPrice": "25855.16",
        "openFee": "-2.62489",
        "followCount": "1"
      }
    ],
    "endId": "1"
  }
}
```

## 交易员修改带单止盈止损

`POST /api/v2/copy/mix-trader/order-modify-tpsl`

限频规则: 5次/秒/UID

Operation ID: `classicCopytradingFutureCopytradeTraderTraderOrderModifyTpsl`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| symbol | string | 是 | 交易对 |
| trackingNo | string | 是 | 带单号 |
| productType | string | 是 | 产品类型<br><br>`USDT-FUTURES` U本位合约<br><br>`COIN-FUTURES` 币本位合约<br><br>`USDC-FUTURES` USDC合约 |
| stopSurplusPrice | string |  | 止盈价格<br><br>stopSurplusPrice和stopLossPrice两者必传其一<br><br>为空时，不管存不存在止盈都忽略或不更新，<br><br>为0时，若存在止盈则表示取消原有止盈。<br><br>大于等于0时，则表示更新或设置止盈。 |
| stopLossPrice | string |  | 止损价格<br><br>stopSurplusPrice和stopLossPrice两者必传其一<br><br>为空时，不管存不存在止损都忽略或不更新，<br><br>为0时，若存在止损则表示取消原有止损。<br><br>大于等于0时，则表示更新或设置止损。 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | string |  | 执行结果<br><br>success 成功;<br><br>fail 失败 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1656066841304,
  "data": "success"
}
```

## 交易员获取历史带单

`GET /api/v2/copy/mix-trader/order-history-track`

限频规则：5次/秒/UID

Operation ID: `classicCopytradingFutureCopytradeTraderTraderOrderHistoryTrack`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| idLessThan | query | string |  | 请求此ID之前（更旧的数据）的分页内容，传的值为对应接口的 endId。 |
| idGreaterThan | query | string |  | 请求此ID之后（更新的数据）的分页内容，传的值为对应接口的 endId |
| startTime | query | string |  | 开始时间戳 <br><br>(跟单创建时间)<br><br>Unix时间戳的毫秒数格式，如 1597026383085<br><br>（时间跨度最大支持三个月，若不传结束时间，则默认结束时间为三个月。） |
| endTime | query | string |  | 结束时间戳 默认当前时间<br><br>(跟单创建时间)<br><br>Unix时间戳的毫秒数格式，如 1597026383085<br><br>（时间跨度最大支持三个月，若不传开始时间，则默认开始时间为三个月。） |
| limit | query | string |  | 查询条数 默认20，最大100 |
| order | query | string |  | 排序规则（创建时间）默认desc |
| symbol | query | string |  | 交易币对,支持大小写 |
| productType | query | string | 是 | 产品类型<br><br>`USDT-FUTURES` U本位合约<br><br>`COIN-FUTURES` 币本位合约<br><br>`USDC-FUTURES` USDC合约 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.trackingList | object[] |  | 带单记录集合 |
| data.trackingList[].trackingNo | string |  | 跟踪订单号 |
| data.trackingList[].symbol | string |  | 交易对 |
| data.trackingList[].openOrderId | string |  | 开单订单号 |
| data.trackingList[].closeOrderId | string |  | 平仓订单号 |
| data.trackingList[].productType | string |  | 产品类型 |
| data.trackingList[].posSide | string |  | 带单方向 |
| data.trackingList[].openLeverage | string |  | 开仓杠杆 |
| data.trackingList[].openPriceAvg | string |  | 开单成交均价 |
| data.trackingList[].openTime | string |  | 开单时间 |
| data.trackingList[].openSize | string |  | 开单数量 |
| data.trackingList[].closeSize | string |  | 平仓数量 |
| data.trackingList[].closeTime | string |  | 平仓时间 |
| data.trackingList[].closePriceAvg | string |  | 平仓单成交均价 |
| data.trackingList[].stopType | string |  | 是否是止盈或止损触发 |
| data.trackingList[].achievedPL | string |  | 已实现盈亏 |
| data.trackingList[].openFee | string |  | 开单手续费 |
| data.trackingList[].closeFee | string |  | 平仓手续费 |
| data.trackingList[].cTime | string |  | 创建时间 |
| data.endId | string |  | 最后的跟踪订单id。<br><br>指定idLessThan/idGreaterThan作为范围查询时以此为准。 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695802740184,
  "data": {
    "trackingList": [
      {
        "trackingNo": "123123",
        "symbol": "BTCUSDT",
        "openOrderId": "12312313123",
        "closeOrderId": "12312313123",
        "productType": "usdt-futures",
        "posSide": "long",
        "openLeverage": "20",
        "openPriceAvg": "32000.5",
        "openTime": "1695035398292",
        "openSize": "0.1000",
        "closeSize": "0.1000",
        "closeTime": "1695176679764",
        "closePriceAvg": "32000.0",
        "stopType": "",
        "achievedPL": "-0.05000000",
        "openFee": "-3.20005000",
        "closeFee": "-3.20000000",
        "cTime": "1695035398292"
      }
    ],
    "endId": "1"
  }
}
```

## 交易员平仓接口

`POST /api/v2/copy/mix-trader/order-close-positions`

限频规则：5次/秒/UID

Operation ID: `classicCopytradingFutureCopytradeTraderTraderOrderClosePositions`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| trackingNo | string |  | 跟踪订单号 <br><br>来自当前带单接口的 trackingNo<br><br>若同时传递了symbol，需确定订单号对与其相呼应。 |
| symbol | string |  | 交易币对<br><br>支持大小写 |
| productType | string | 是 | 产品类型<br><br>`USDT-FUTURES` U本位合约<br><br>`COIN-FUTURES` 币本位合约<br><br>`USDC-FUTURES` USDC合约<br><br>若仅传递productType，则会平仓该业务线下的所有仓位。 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].trackingNo | string |  | 跟踪订单号 |
| data[].symbol | string |  | 交易币对 |
| data[].productType | string |  | 产品类型 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695810053803,
  "data": [
    {
      "trackingNo": "1",
      "symbol": "BTCUSDT",
      "productType": "USDT-FUTURES"
    }
  ]
}
```

## 查看交易员数据指标统计

`GET /api/v2/copy/mix-trader/order-total-detail`

限频规则: 5次/秒/UID

Operation ID: `classicCopytradingFutureCopytradeTraderTraderOrderTotalDetail`

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.roi | string |  | ROI |
| data.tradingOrderNum | string |  | 总开单数 |
| data.totalFollowerNum | string |  | 累计跟随人数 |
| data.currentFollowerNum | string |  | 当前跟随人数 |
| data.totalpl | string |  | 总收益<br><br>(美元计价） |
| data.gainNum | string |  | 盈利比数 |
| data.lossNum | string |  | 亏损比数 |
| data.totalEquity | string |  | 总权益 |
| data.winRate | string |  | 胜率 |
| data.tradingPairsAvailableList | string[] |  | 可跟交易对 |
| data.lastWeekRoiList | object[] |  | 近一周收益率 |
| data.lastWeekRoiList[].rate | string |  | 收益率 |
| data.lastWeekRoiList[].ctime | string |  | 时间 |
| data.lastWeekProfitList | object[] |  | 近一周收益 |
| data.lastWeekProfitList[].amount | string |  | 收益，USDT |
| data.lastWeekProfitList[].ctime | string |  | 时间 |
| data.lastMonthRoiList | object[] |  | 近一月收益率 |
| data.lastMonthRoiList[].rate | string |  | 收益率 |
| data.lastMonthRoiList[].ctime | string |  | 时间 |
| data.lastMonthProfitList | object[] |  | 近一月收益 |
| data.lastMonthProfitList[].amount | string |  | 收益, USDT |
| data.lastMonthProfitList[].ctime | string |  | 时间 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695805917634,
  "data": {
    "roi": "19.38",
    "tradingOrderNum": "105",
    "totalFollowerNum": "134",
    "currentFollowerNum": "4",
    "totalpl": "$46.95",
    "gainNum": "59",
    "lossNum": "46",
    "winRate": "56.123",
    "tradingPairsAvailableList": [
      "BTCUSDT"
    ],
    "lastWeekRoiList": [
      {
        "rate": "-14.130944",
        "ctime": "1695139200000"
      }
    ],
    "lastWeekProfitList": [],
    "lastMonthRoiList": [
      {
        "rate": "-14.130944",
        "ctime": "1693152000000"
      }
    ],
    "totalEquity": "1776.03"
  }
}
```

## 交易员历史分润汇总

`GET /api/v2/copy/mix-trader/profit-history-summarys`

限频规则：5次/秒/UID

Operation ID: `classicCopytradingFutureCopytradeTraderTraderProfitHistorySummarys`

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.profitSummary | object |  | 交易员分润汇总信息 |
| data.profitSummary.yesterdayProfit | string |  | 昨日分润(交易员) |
| data.profitSummary.yesterdayTime | string |  | 昨日分润时间(毫秒) |
| data.profitSummary.sumProfit | string |  | 累计分润 |
| data.profitSummary.waitProfit | string |  | 待分润 |
| data.profitHistoryList | object[] |  | 历史分润汇总集合 |
| data.profitHistoryList[].coin | string |  | 结算币种<br><br>（以币种为维度） |
| data.profitHistoryList[].profitCount | string |  | 收益汇总<br><br>（以币种为维度） |
| data.profitHistoryList[].lastProfitTime | string |  | 最后分润时间（毫秒）<br><br>（以币种为维度） |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1698200382922,
  "data": {
    "profitSummary": {
      "yesterdayProfit": "0",
      "sumProfit": "26.4519",
      "waitProfit": "0",
      "yesterdayTime": "1698076800000"
    },
    "profitHistoryList": [
      {
        "coin": "USDT",
        "profitCount": "24.28410397",
        "lastProfitTime": "1698076800000"
      }
    ]
  }
}
```

## 交易员历史分润明细

`GET /api/v2/copy/mix-trader/profit-history-details`

限频规则：5次/秒/UID

Operation ID: `classicCopytradingFutureCopytradeTraderTraderProfitHistoryDetails`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| coin | query | string |  | 分润结算币种。 |
| limit | query | string |  | 查询条数 默认100，最大100 |
| idLessThan | query | string |  | 请求此ID之前（更旧的数据）的分页内容，传的值为对应接口的 endId。 |
| idGreaterThan | query | string |  | 请求此ID之后（更新的数据）的分页内容，传的值为对应接口的 endId |
| startTime | query | string |  | 开始时间戳 <br><br>Unix时间戳的毫秒数格式，如 1597026383085<br><br>（时间跨度最大支持三个月，若不传结束时间，则默认结束时间为三个月。） |
| endTime | query | string |  | 结束时间戳 <br><br>Unix时间戳的毫秒数格式，如 1597026383085<br><br>（时间跨度最大支持三个月，若不传开始时间，则默认开始时间为三个月。） |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.profitList | object[] |  | 分润集合 |
| data.profitList[].profitId | string |  | 分润id |
| data.profitList[].coin | string |  | 结算币种 |
| data.profitList[].profit | string |  | 已分润 |
| data.profitList[].nickName | string |  | 昵称 |
| data.profitList[].profitTime | string |  | 分润时间 |
| data.endId | string |  | 最后的跟分润id。<br><br>指定idLessThan/idGreaterThan作为范围查询时以此为准。 |

```json
{
  "code": "00000",
  "data": {
    "profitList": [
      {
        "profitId": "1",
        "coin": "usdt",
        "profit": "1",
        "nickName": "nickname",
        "profitTime": "1691446639000"
      }
    ],
    "endId": "3"
  },
  "msg": "success",
  "requestTime": 1627354109502
}
```

## 交易员待分润明细

`GET /api/v2/copy/mix-trader/profit-details`

限频规则：5次/秒/UID

Operation ID: `classicCopytradingFutureCopytradeTraderTraderProfitDetails`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| coin | query | string |  | 分润结算币种 |
| pageSize | query | string |  | 查询数量 <br><br>默认20 最大100 |
| pageNo | query | string |  | 当前页号<br><br>默认为1. |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].coin | string |  | 结算币种 |
| data[].profit | string |  | 分润 |
| data[].nickName | string |  | 昵称 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695805098677,
  "data": [
    {
      "coin": "USDT",
      "profit": "1",
      "nickName": "nickname"
    }
  ]
}
```

## 交易员历史分润汇总(按结算币种和日期)

`GET /api/v2/copy/mix-trader/profits-group-coin-date`

限频规则：5次/秒/UID

Operation ID: `classicCopytradingFutureCopytradeTraderTraderGetProfitsGroupCoinDate`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| pageSize | query | string |  | 查询条数,默认为20条，最大支持50条。 |
| pageNo | query | string |  | 查询页码, 默认 1 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].coin | string |  | 币种 |
| data[].profit | string |  | 收益<br><br>（以该币种日期为维度） |
| data[].profitTime | string |  | 分润时间(毫秒)<br><br>（以该币种日期为维度） |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695804253784,
  "data": [
    {
      "coin": "USDT",
      "profit": "100",
      "profitTime": "1695721038097"
    }
  ]
}
```

## 交易员获取带单交易对

`GET /api/v2/copy/mix-trader/config-query-symbols`

限速规则:  5次/秒/UID

Operation ID: `classicCopytradingFutureCopytradeTraderTraderGetConfigQuerySymbols`

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
| data[].symbol | string |  | 交易对 |
| data[].openTrader | string |  | 是否开启跟单, `YES`, `NO` |
| data[].minOpenCount | string |  | 交易员最小开单数量 |
| data[].maxLeverage | string |  | 交易员最大开单杠杆倍数 |
| data[].stopSurplusRatio | string |  | 止盈比例设置的值 （值是正整数，120表示 120%） |
| data[].stopLossRatio | string |  | 止损比例设置的值 （值是正整数，40表示 40%） |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695807225928,
  "data": [
    {
      "symbol": "BTCUSDT",
      "openTrader": "yes",
      "minOpenCount": "0.002",
      "maxLeverage": "50",
      "stopSurplusRatio": "100",
      "stopLossRatio": "30"
    }
  ]
}
```

## 交易员设置跟单交易对

`POST /api/v2/copy/mix-trader/config-setting-symbols`

限速规则: 5次/秒/UID

Operation ID: `classicCopytradingFutureCopytradeTraderTraderConfigSettingSymbols`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| settingList | object[] | 是 | 设置集合<br><br>最大50个 |
| settingList[].symbol | string | 是 | 交易对 |
| settingList[].productType | string | 是 | 产品类型<br><br>`USDT-FUTURES` U本位合约<br><br>`COIN-FUTURES` 币本位合约<br><br>`USDC-FUTURES` USDC合约 |
| settingList[].settingType | string | 是 | 设置类型, `ADD`, `DELETE`, `UPDATE` |
| settingList[].stopSurplusRatio | string |  | 止盈比例 <br><br>1-400之内的正整数，超过这个值为非法。<br><br>2.删除类型时：此值无效。<br><br>3.增加类型时：止盈为空则默认不设止盈比例。<br><br>4.更新类型时：若值为空则代表不做任何改变；若为0，则代表取消之前设置的止盈；若大于0，则代表新增或更新止盈。<br><br>更新类型时，stopSurplusRatio和stopLossRatio两者必传其一。 |
| settingList[].stopLossRatio | string |  | 止损比例<br><br>1-400之内的正整数，超过这个值为非法。<br><br>2.删除类型时：此值无效。<br><br>3.增加类型时：止损为空则默认不设止损比例。<br><br>4.更新类型时：若值为空则代表不做任何改变；若为0，则代表取消之前设置的止损；若大于0，则代表新增或更新止损。<br><br>更新类型时，stopSurplusRatio和stopLossRatio两者必传其一。 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | string |  | 设置结果, success fail |

```json
{
  "code": "00000",
  "data": "success",
  "msg": "success",
  "requestTime": 1627354109502
}
```

## 交易员修改带单设置

`POST /api/v2/copy/mix-trader/config-settings-base`

限频规则: 5次/秒/UID

Operation ID: `classicCopytradingFutureCopytradeTraderTraderConfigSettingsBase`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| enable | string |  | 三者必传其一<br><br>是否开启带单 <br><br>`YES` 是<br><br> `NO` 否 |
| showTotalEquity | string |  | 三者必传其一<br><br>是否展示总权益(USDT)  <br><br>`YES` 是<br><br> `NO` 否 |
| showTpsl | string |  | 三者必传其一<br><br>订单的止盈止损价将公开展示  <br><br>`YES` 是<br><br> `NO` 否 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | string |  | 是否成功, success fail |

```json
{
  "code": "00000",
  "data": "success",
  "msg": "success",
  "requestTime": 1627354109502
}
```

## 获取我的跟随者列表

`GET /api/v2/copy/mix-trader/config-query-followers`

限频规则: 5次/秒/UID

Operation ID: `classicCopytradingFutureCopytradeTraderConfigQueryFollowers`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| pageNo | query | string |  | 页码<br><br>（默认为1） |
| pageSize | query | string |  | 每页条数<br><br>（默认20 最大100） |
| startTime | query | string |  | 开始时间戳 <br><br>Unix时间戳的毫秒数格式，如 1597026383085<br><br>（时间跨度最大支持三个月，若不传结束时间，则默认结束时间为三个月。） |
| endTime | query | string |  | 结束时间戳 <br><br>Unix时间戳的毫秒数格式，如 1597026383085<br><br>（时间跨度最大支持三个月，若不传开始时间，则默认开始时间为三个月。） |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].accountEquity | string |  | 账户总权益 |
| data[].isRemove | string |  | 能否移除跟单用户<br><br>yes 是<br><br>no 否 |
| data[].followerHeadPic | string |  | 跟随者头像 |
| data[].followerName | string |  | 跟随者昵称 |
| data[].followerUid | string |  | 跟随者用户id |
| data[].followerTime | string |  | 跟随日期（以初次跟随日期为准）<br><br>Unix时间戳的毫秒数格式，如 1597026383085 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695806678625,
  "data": [
    {
      "accountEquity": "975863.9707",
      "isRemove": "No",
      "followerHeadPic": "",
      "followerName": "xxx-*******",
      "followerUid": "*********",
      "followerTime": "1693381832000"
    }
  ]
}
```

## 交易员取消跟随者

`POST /api/v2/copy/mix-trader/config-remove-follower`

限频规则: 5次/秒/UID

Operation ID: `classicCopytradingFutureCopytradeTraderConfigRemoveFollower`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| followerUid | string | 是 | 跟随者 UID |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | string |  | success |

```json
{
  "code": "00000",
  "data": "success",
  "msg": "success",
  "requestTime": 1627354109502
}
```