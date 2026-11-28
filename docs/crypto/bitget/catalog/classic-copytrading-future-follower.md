---
exchange: bitget
source_url: https://www.bitget.com/docs/catalog/classic-copytrading-future-follower
api_type: REST
updated_at: 2026-11-28 19:00:20.489370
---

# Classic Futures Copy Trading Follower API

Classic account — futures copy trading follower endpoints.

版本: 1.0.0

## 服务地址

- `https://api.bitget.com`

## 接口列表

- `POST /api/v2/copy/mix-follower/copy-settings` — Copy settings
- `GET /api/v2/copy/mix-follower/query-current-orders` — Get Current Tracking Orders
- `GET /api/v2/copy/mix-follower/query-history-orders` — Get History Tracking Orders
- `POST /api/v2/copy/mix-follower/setting-tpsl` — Set TPSL
- `POST /api/v2/copy/mix-follower/close-positions` — Close Positions
- `GET /api/v2/copy/mix-follower/query-settings` — Get Copy Trade Settings
- `POST /api/v2/copy/mix-follower/settings` — Set Copy Trade Settings
- `POST /api/v2/copy/mix-follower/cancel-trader` — Unfollow the Trader
- `GET /api/v2/copy/mix-follower/query-traders` — Get My Traders
- `GET /api/v2/copy/mix-follower/query-quantity-limit` — Get Follow Limit

## Copy settings

`POST /api/v2/copy/mix-follower/copy-settings`

Rate Limit: 1 req/sec/UID

This interface is designed for setting up order following for the new version of followers. Currently, the interface only supports intelligent proportion and does not support multivariate exploration.

Criteria for the new version of followers: Users who registered after January 26, 2024, or users who registered before January 26, 2024 and have manually upgraded.

Operation ID: `classicCopytradingFutureCopytradeFollowerCopySettings`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| traderId | string | 是 | ID of the elite trader that you followed |
| copyAmount | string | 是 | Copy trading amount, must be a positive integer not less than 50, denominated in USDT.. |
| copyAllPostions | string |  | Whether to follow all positions of the trader. <br><br>`yes`Follow all positions. `no` Do not follow all positions <br><br> If not provided, the default value is`no` |
| autoCopy | string |  | Whether to automatically follow new symbol opened by traders(only takes effect when mode is basic).<br><br> `on`Automatic following. `off`Not automatically following <br><br> If not provided, the default value is`on` |
| equityGuardian | string |  | Equity protection switch.<br><br> `on`Enabled <br><br> `off`Disabled <br><br>  If not provided,the default value is`off` |
| equityGuardianMode | string |  | Equity protection mode, triggered when equityGuardian=on. <br><br> `amount`Fixed amount protection <br><br> `percentage`Percentage-based protection <br><br>  If not provided, the default value is`amount` |
| equity | string |  | Equity protection trigger value. Required when equityGuardian=on. Must be a positive integer. If equityGuardian Mode=percentage, range is [1-100], representing 1%-100%. If equityGuardianMode=amount, it represents a fixeed loss amount. |
| marginMode | string |  | Margin mode.<br><br> `follow_trader`Follow the trader's leverage.<br><br>`crossed_margin`Cross margin <br><br>`isolated_margin`Isolated margin.<br><br> If not provided, the default value is`follow_trader` |
| leverage | string |  | Leverage mode, effective when marginMode=follow_trader.<br><br> `follow_trader`Follow trader.<br><br> `fixed_leverage`Use fixed leverage. <br><br> Default: follow_trader. |
| multiple | string |  | Leverage multiple, ranging from [1,125]. Default: 10. |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | string |  | `success` Success <br><br> `failure` Failure |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695872676719,
  "data": "success"
}
```

## Get Current Tracking Orders

`GET /api/v2/copy/mix-follower/query-current-orders`

Rate Limit: 5 req/sec/UID

Operation ID: `classicCopytradingFutureCopytradeFollowerQueryCurrentOrders`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| idLessThan | query | string |  | Separate page content before this ID is requested (older data), and the value input should be the end ID of the corresponding interface. |
| idGreaterThan | query | string |  | Separate page content after this ID is requested (newer data), and the value input should be the end ID of the corresponding interface. |
| startTime | query | string |  | Start timestamp <br><br>(Copy trade creation time)<br><br>Milliseconds format of timestamp Unix, e.g. 1597026383085<br><br>(The maximum time span supported is three months. The default end time is three months if no value is set for the end time. ) |
| endTime | query | string |  | End timestamp <br><br>(Copy trade creation time)<br><br>Milliseconds format of timestamp Unix, e.g. 1597026383085<br><br>(The maximum time span supported is three months. The default start time is three months ago if no value is set for the start time. ) |
| limit | query | string |  | Number of queries: Default: 20, maximum: 100. |
| symbol | query | string |  | Trading pairs, case sensitive |
| productType | query | string | 是 | Product type<br><br>`USDT-FUTURES` USDT-M Futures<br><br>`COIN-FUTURES` Coin-M Futures<br><br>`USDC-FUTURES` USDC-M Futures |
| traderId | query | string |  | Trader ID |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.trackingList | object[] |  | Overview of current tracking records |
| data.trackingList[].trackingNo | string |  | Track order number |
| data.trackingList[].traderId | string |  | Trader user ID |
| data.trackingList[].traderName | string |  | Trader alias |
| data.trackingList[].openOrderId | string |  | Opening order ID |
| data.trackingList[].closeOrderId | string |  | Closing order ID |
| data.trackingList[].symbol | string |  | Trading pair |
| data.trackingList[].posSide | string |  | Position direction<br><br>`long`: long position in hedging mode<br><br>`short`: short position in hedging mode |
| data.trackingList[].openLeverage | string |  | Leverage for opening position |
| data.trackingList[].openPriceAvg | string |  | Average entry price |
| data.trackingList[].openTime | string |  | Position opening time (millisecond timestamp) |
| data.trackingList[].openFee | string |  | Opening fee (excluding discounts) |
| data.trackingList[].openSize | string |  | Opening volume |
| data.trackingList[].openMarginSz | string |  | Margin amount |
| data.trackingList[].closePriceAvg | string |  | Average closing price |
| data.trackingList[].closeSize | string |  | Closing volume |
| data.trackingList[].closeTime | string |  | Position closing time (millisecond timestamp) |
| data.endId | string |  | Last tracking order ID.<br><br>This is used when idLessThan/idGreaterThan is set as the querying scope |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1634107646972,
  "data": {
    "trackingList": [
      {
        "trackingNo": "1",
        "traderName": "xxxxxx",
        "openOrderId": "1",
        "closeOrderId": "",
        "traderId": "**********",
        "symbol": "BTCUSDT",
        "posSide": "short",
        "openLeverage": "47",
        "openPriceAvg": "39827",
        "openTime": "1627567376984",
        "openSize": "0.0010000000000000",
        "closePriceAvg": "0",
        "closeSize": "0.0000000000000000",
        "openMarginSz": "21",
        "closeTime": "0"
      }
    ],
    "endId": ""
  }
}
```

## Get History Tracking Orders

`GET /api/v2/copy/mix-follower/query-history-orders`

Rate Limit: 5 req/sec/UID

Operation ID: `classicCopytradingFutureCopytradeFollowerQueryHistoryOrders`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| idLessThan | query | string |  | Separate page content before this ID is requested (older data), and the value input should be the end ID of the corresponding interface. |
| idGreaterThan | query | string |  | Separate page content after this ID is requested (newer data), and the value input should be the end ID of the corresponding interface. |
| startTime | query | string |  | Start timestamp <br><br>(Copy trade creation time)<br><br>Milliseconds format of timestamp Unix, e.g. 1597026383085<br><br>(The maximum time span supported is three months. The default end time is three months if no value is set for the end time. ) |
| endTime | query | string |  | End timestamp <br><br>(Copy trade creation time)<br><br>Milliseconds format of timestamp Unix, e.g. 1597026383085<br><br>(The maximum time span supported is three months. The default start time is three months ago if no value is set for the start time. ) |
| limit | query | string |  | Number of queries: Default: 20, maximum: 100. |
| symbol | query | string |  | Trading pairs, case sensitive |
| productType | query | string | 是 | Product type<br><br>`USDT-FUTURES` USDT-M Futures<br><br>`COIN-FUTURES` Coin-M Futures<br><br>`USDC-FUTURES` USDC-M Futures |
| traderId | query | string |  | Trader ID |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.trackingList | object[] |  | Overview of elite trade records |
| data.trackingList[].trackingNo | string |  | Order number tracking |
| data.trackingList[].traderId | string |  | Trader user ID |
| data.trackingList[].openOrderId | string |  | Opening order ID |
| data.trackingList[].closeOrderId | string |  | Closing order ID |
| data.trackingList[].productType | string |  | Product type default `USDT-FUTURES`<br><br>`USDT-FUTURES` USDT-M Futures<br><br>`COIN-FUTURES` Coin-M Futures<br><br>`USDC-FUTURES` USDC-M Futures |
| data.trackingList[].symbol | string |  | Trading pair |
| data.trackingList[].posSide | string |  | Position direction<br><br>`long`: long position in hedging mode<br><br>`short`: short position in hedging mode |
| data.trackingList[].openLeverage | string |  | Leverage for opening position |
| data.trackingList[].openPriceAvg | string |  | Average entry price |
| data.trackingList[].openTime | string |  | Position opening time (millisecond timestamp) |
| data.trackingList[].openSize | string |  | Opening volume |
| data.trackingList[].closePriceAvg | string |  | Average closing price |
| data.trackingList[].closeFee | string |  | close fee (excluding discounts) |
| data.trackingList[].openFee | string |  | Opening fee (excluding discounts) |
| data.trackingList[].closeSize | string |  | Closing volume |
| data.trackingList[].closeTime | string |  | Closing volume |
| data.trackingList[].profitRate | string |  | rate of return |
| data.trackingList[].netProfit | string |  | follower net income |
| data.trackingList[].achievedPL | string |  | Realized profit and loss |
| data.endId | string |  | Last tracking order ID.<br><br>This is used when idLessThan/idGreaterThan is set as the querying scope |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695808417159,
  "data": {
    "trackingList": [
      {
        "trackingNo": "123123123123",
        "posSide": "long",
        "openLeverage": "20",
        "openSize": "0.1852",
        "closeSize": "0.1852",
        "openPriceAvg": "32000.5",
        "closePriceAvg": "28233.0",
        "achievedPL": "-697.74100000",
        "openFee": "-5.92649260",
        "closeFee": "-5.22875160",
        "symbol": "BTCUSDT",
        "profitRate": "-235.47",
        "netProfit": "-697.74100000",
        "openOrderId": "1",
        "closeOrderId": "1",
        "openTime": "1695176941362",
        "closeTime": "1695353868557",
        "traderId": "**********",
        "productType": "usdt-futures"
      }
    ],
    "endId": ""
  }
}
```

## Set TPSL

`POST /api/v2/copy/mix-follower/setting-tpsl`

Rate Limit: 5 req/sec/UID

Operation ID: `classicCopytradingFutureCopytradeFollowerSettingTpsl`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| trackingNo | string | 是 | Order tracking number |
| symbol | string |  | Trading pair |
| productType | string | 是 | Product type<br><br>`USDT-FUTURES` USDT-M Futures<br><br>`COIN-FUTURES` Coin-M Futures<br><br>`USDC-FUTURES` USDC-M Futures |
| stopSurplusPrice | string |  | Take profit price<br><br>When it is empty, it is ignored or not updated, no matter take-profit exists or not,<br><br>When it is 0, it means the original take-profit is canceled if there is a take-profit already.<br><br>When it is greater than or equal to 0, it means take-profit is updated or set. |
| stopLossPrice | string |  | Stop loss price<br><br>When it is empty, it is ignored or not updated, no matter stop-loss exists or not,<br><br>When it is 0, it means the original stop-loss is canceled if there is a stop-loss already.<br><br>When it is greater than or equal to 0, it means stop-loss is updated or set. |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | string |  | Result<br><br>`success`: success,`fail`: fail |

```json
{
  "code": "00000",
  "data": "success",
  "msg": "success",
  "requestTime": 1627354109502
}
```

## Close Positions

`POST /api/v2/copy/mix-follower/close-positions`

Rate Limit: 5 req/sec/UID



Interface for followers to close positions. Can close positions based on order ID, trading pair, direction, position mode, and margin

Operation ID: `classicCopytradingFutureCopytradeFollowerClosePositions`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| productType | string | 是 | Product type<br><br>`USDT-FUTURES` USDT-M Futures<br><br>`COIN-FUTURES` Coin-M Futures<br><br>`USDC-FUTURES` USDC-M Futures |
| trackingNo | string |  | Tracking numbers of buying orders grouped by trading pair<br><br>（If you pass the trackingNo and ensure that the symbol, marginCoin, marginMode, and holdSide are not empty, you need to ensure that the trackingNo corresponds to them.） |
| symbol | string |  | Trading pair |
| marginCoin | string |  | margin coin |
| marginMode | string |  | Position mode<br><br>`isolated`: isolated margin <br><br>`cross`: cross margin |
| holdSide | string |  | Position direction <br><br>1. In the buying and selling (one-way position) mode: you don’t have to fill it in, if you fill it in, it will be ignored. <br><br>2. In the opening and closing position (hedge mode): This parameter must be filled in.  <br><br>`long`: long position in hedging mode<br><br>`short`: short position in hedging mode |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.orderIdList | string[] |  | Order ID |

```json
{
  "code": "00000",
  "data": {
    "orderIdList": [
      "123",
      "321"
    ]
  },
  "msg": "success",
  "requestTime": 1627293504612
}
```

## Get Copy Trade Settings

`GET /api/v2/copy/mix-follower/query-settings`

Rate Limit: 5 req/sec/UID

Operation ID: `classicCopytradingFutureCopytradeFollowerQuerySettings`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| traderId | query | string | 是 | ID of the elite trader that you followed |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.followerEnable | string |  | Am I following<br><br>YES<br><br>NO |
| data.detailList | object[] |  | Copy trade details |
| data.detailList[].symbol | string |  | Trading pair |
| data.detailList[].productType | string |  | Product type<br><br>`USDT-FUTURES` USDT-M Futures<br><br>`COIN-FUTURES` Coin-M Futures<br><br>`USDC-FUTURES` USDC-M Futures |
| data.detailList[].marginType | string |  | Margin type<br><br>`trader` margin type of the elite trader that you followed;<br><br>`specify` your own margin type. |
| data.detailList[].marginCoin | string |  | Margin currency |
| data.detailList[].leverType | string |  | Leverage type<br><br>`position` use position leverage;<br><br>`specify` use the specified leverage;<br><br>`trader` use the leverage of the elite trader; |
| data.detailList[].longLeverage | string |  | Leverage of long positions |
| data.detailList[].shortLeverage | string |  | Leverage of short positions |
| data.detailList[].traceType | string |  | Copy trade position type<br><br>`percent` Set the percentage of the copy trade amount to the trader's elite trade amount. For example, 1 means the follower invests the same amount to open a position as the elite trader, and 2 means the follower invests twice the amount of the elite trader.<br><br>`amount` the fixed volume specified for copy trading<br><br>`count` number of copy trade orders with fixed volume |
| data.detailList[].traceValue | string |  | Copy trade position value |
| data.detailList[].maxHoldSize | string |  | Maximum number of orders |
| data.detailList[].stopSurplusRatio | string |  | Take-profit ratio<br><br>positive integers within 1-400,<br><br>Value exceeding this number is invalid. |
| data.detailList[].stopLossRatio | string |  | Stop-loss ratio<br><br>positive integers within 1-400,<br><br>Value exceeding this number is invalid. |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1679465100798,
  "data": {
    "followerEnable": "YES",
    "detailList": [
      {
        "symbol": "ETHUSDT",
        "productType": "USDT-FUTURES",
        "marginType": "specify",
        "marginCoin": "USDT",
        "leverType": "trader",
        "longLeverage": "20",
        "shortLeverage": "20",
        "traceType": "percent",
        "traceValue": "1",
        "maxHoldSize": "50000",
        "stopSurplusRatio": "200",
        "stopLossRatio": ""
      }
    ]
  }
}
```

## Set Copy Trade Settings

`POST /api/v2/copy/mix-follower/settings`

Rate Limit:  5 req/sec/UID

Operation ID: `classicCopytradingFutureCopytradeFollowerSettings`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| traderId | string | 是 | ID of the elite trader that you followed |
| autoCopy | string |  | Whether to automatically follow new symbol opened by traders(only take effect when parameter mode is basic)  <br><br> on：auto <br><br> off：no |
| mode | string |  | follow mode    <br><br> basic：basic mode <br><br> advanced（default）：advanced mode |
| settings | object[] | 是 | Settings of copy trading (based on trading pair)<br><br>Maximum: 10 |
| settings[].symbol | string | 是 | Trading pair |
| settings[].productType | string | 是 | Product type<br><br>`USDT-FUTURES` USDT-M Futures<br><br>`COIN-FUTURES` Coin-M Futures<br><br>`USDC-FUTURES` USDC-M Futures |
| settings[].marginType | string | 是 | Margin type(only take effect when parameter mode is advanced)<br><br>`trader` margin type of the elite trader that you followed;<br><br>`specify` your own margin type. |
| settings[].marginCoin | string |  | Margin currency |
| settings[].leverType | string | 是 | Leverage type(only take effect when parameter mode is advanced)<br><br>`position` use position leverage;<br><br>`specify` use the specified leverage;<br><br>`trader` use the leverage of the elite trader; |
| settings[].longLeverage | string |  | Leverage of long positions  (only take effect when parameter mode is advanced) |
| settings[].shortLeverage | string |  | Leverage of short positions    (only take effect when parameter mode is advanced) |
| settings[].traceType | string | 是 | Copy trade position type<br><br>`percent` Set the percentage of the copy trade amount to the trader's elite trade amount. For example, 1 means the follower invests the same amount to open a position as the elite trader, and 2 means the follower invests twice the amount of the elite trader.<br><br>`amount` the fixed volume specified for copy trading<br><br>`count` number of copy trade orders with fixed volume (only take effect when parameter mode is advanced) |
| settings[].traceValue | string | 是 | Copy trade position value |
| settings[].maxHoldSize | string |  | Maximum number of orders |
| settings[].stopSurplusRatio | string |  | Take-profit ratio<br><br> Positive integers within 1-400,<br><br>Value exceeding this number is invalid. |
| settings[].stopLossRatio | string |  | Stop-loss ratio <br><br> Positive integers within 1-400,<br><br>Value exceeding this number is invalid.<br><br>Stop-loss ratio |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | string |  | Result<br><br>`success` `fail` |

```json
{
  "code": "00000",
  "data": "success",
  "msg": "success",
  "requestTime": 1627354109502
}
```

## Unfollow the Trader

`POST /api/v2/copy/mix-follower/cancel-trader`

Rate Limit: 5 req/sec/UID

Operation ID: `classicCopytradingFutureCopytradeFollowerCancelTrader`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| traderId | string | 是 | Trader user ID |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | string |  | Result<br><br>`success` `fail` |

```json
{
  "code": "00000",
  "data": "success",
  "msg": "success",
  "requestTime": 1627354109502
}
```

## Get My Traders

`GET /api/v2/copy/mix-follower/query-traders`

Rate Limit: 5 req/sec/UID

Operation ID: `classicCopytradingFutureCopytradeFollowerQueryTraders`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| startTime | query | string |  | Start timestamp <br><br>Milliseconds format of timestamp Unix, e.g. 1597026383085<br><br>(The maximum time span supported is three months. The default end time is three months if no value is set for the end time. ) |
| endTime | query | string |  | End timestamp <br><br>Milliseconds format of timestamp Unix, e.g. 1597026383085<br><br>(The maximum time span supported is three months. The default start time is three months ago if no value is set for the start time. ) |
| pageNo | query | string |  | Current page number<br><br>Default to 1. |
| pageSize | query | string |  | Number of quiries<br><br>Default to 20 entries and supports a maximum of 50 entries. |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].certificationType | string |  | Certification type<br><br>`Uncertified`<br><br>`Certified` |
| data[].traderId | string |  | Trader ID |
| data[].traderName | string |  | Alias |
| data[].maxFollowLimit | string |  | Maximum number of elite traders to follow |
| data[].bgbMaxFollowLimit | string |  | Maximum number of elite traders to follow granted by BGB holdings |
| data[].followCount | string |  | Number of elite traders that you have followed |
| data[].bgbFollowCount | string |  | Number of elite traders that you have followed granted by BGB holdings |
| data[].traceTotalMarginAmount | string |  | Total opening margin |
| data[].traceTotalNetProfit | string |  | Total net profit |
| data[].traceTotalProfit | string |  | Total profit |
| data[].currentTradingPairs | string[] |  | Current underlying assets for copy trading |
| data[].followerTime | string |  | Following date (take the first following date)<br><br>Milliseconds format of timestamp Unix, e.g. 1597026383085 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695812788826,
  "data": [
    {
      "certificationType": "Uncertified",
      "traderId": "**********",
      "traderName": "x-1111111",
      "maxFollowLimit": "1000",
      "followCount": "0",
      "traceTotalMarginAmount": "1185.3286",
      "traceTotalNetProfit": "-744.7362",
      "traceTotalProfit": "-698.0210",
      "currentTradingPairs": [
        "BTCUSDT",
        "BTCUSD",
        "EOSUSDT",
        "ETHUSDT",
        "ETHUSD"
      ],
      "followerTime": "1693381832000",
      "bgbMaxFollowLimit": "100",
      "bgbFollowCount": "0"
    }
  ]
}
```

## Get Follow Limit

`GET /api/v2/copy/mix-follower/query-quantity-limit`

Frequency limit: 10 times/1s (IP)

Operation ID: `classicCopytradingFutureCopytradeFollowerQueryQuantityLimit`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string |  | Trading pair |
| productType | query | string | 是 | Product type<br><br>`USDT-FUTURES` USDT-M Futures<br><br>`COIN-FUTURES` Coin-M Futures<br><br>`USDC-FUTURES` USDC-M Futures |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].maxFollowSize | string |  | Maximum order size to place (trading currency) |
| data[].minFollowSize | string |  | Minimum order size to place (trading currency) |
| data[].symbol | string |  | Trading pair |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695812926981,
  "data": [
    {
      "maxFollowSize": "20000",
      "minFollowSize": "0.005",
      "symbol": "BTCUSDT"
    }
  ]
}
```


---

经典账户 — 合约跟单跟单员相关接口。

版本: 1.0.0

## 服务地址

- `https://api.bitget.com`

## 接口列表

- `POST /api/v2/copy/mix-follower/copy-settings` — 新版跟随者跟单设置接口
- `GET /api/v2/copy/mix-follower/query-current-orders` — 跟随者查询当前跟单信息
- `GET /api/v2/copy/mix-follower/query-history-orders` — 跟随者查询历史跟单信息
- `POST /api/v2/copy/mix-follower/setting-tpsl` — 跟随者设置仓位止盈止损
- `POST /api/v2/copy/mix-follower/close-positions` — 跟单员平仓
- `GET /api/v2/copy/mix-follower/query-settings` — 跟随者查看跟单设置
- `POST /api/v2/copy/mix-follower/settings` — 跟单设置
- `POST /api/v2/copy/mix-follower/cancel-trader` — 跟随者取消跟随交易员
- `GET /api/v2/copy/mix-follower/query-traders` — 获取我的交易员列表
- `GET /api/v2/copy/mix-follower/query-quantity-limit` — 查询最大/最小跟随下单数量

## 新版跟随者跟单设置接口

`POST /api/v2/copy/mix-follower/copy-settings`

限频规则: 1次/秒/UID

该接口用于新版跟随者进行跟单设置，本期接口仅支持智能比例，暂不支持多元探索

新版跟随者条件 2024-01-26之后注册的用户，或2024-01-26之前注册且手动升级过的用户

Operation ID: `classicCopytradingFutureCopytradeFollowerCopySettings`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| traderId | string | 是 | 交易员ID |
| copyAmount | string | 是 | 跟单金额<br><br>正整数，不小于50，单位为USDT |
| copyAllPostions | string |  | 是否自动跟随交易员仓位 <br><br>`yes`自动跟随 `no`不自动跟随  如不传，默认值为`no`，不自动跟随。 <br><br> 一次性行为。如选择`yes`自动跟随，则会根据交易员已有仓位，以市价开仓进行跟单 |
| autoCopy | string |  | 是否自动跟随交易员新开的新币对<br><br> `on`自动跟随 `off`不自动跟随 - 如不传，默认值为`on`，自动跟随 |
| equityGuardian | string |  | 净值守护者开关<br><br> `on`开启 `off`关闭 - 如不传，默认值为`off`关闭 |
| equityGuardianMode | string |  | 净值守护者模式<br><br> `amount`数额 `percentage`百分比 - 当`equityGuardian=on`时，该字段生效 - 如不传，默认值为`amount` |
| equity | string |  | 守护触发净值<br><br> 即达到该净值亏损时，跟单关系自动取消。所有订单将会以市价平仓，剩余资产将划转至合约账户<br><br>  当净值守护者开关开启，即`equityGuardian=on`时，该字段必填 <br><br>  `equityGuardianMode=amount`时，该字段表示净值亏损数额 <br><br>  `equityGuardianMode=percentage`时，该字段表示净值亏损百分比 |
| marginMode | string |  | 保证金模式<br><br> `follow_trader`跟随交易员 <br><br>`crossed_margin`全仓杠杆模式 <br><br>`isolated_margin`逐仓杠杆模式 <br><br> 如不传，默认值为`follow_trader` |
| leverage | string |  | 杠杆模式<br><br> `follow_trader`跟随交易员<br><br> `fixed_leverage`固定杠杆 <br><br> `marginMode=follow_trader`时，该参数生效，用户可自行选择杠杆模式。如不传，默认值为`follow_trader` <br><br> `marginMode=cross_margin`或`marginMode=isolated_margin`时，接口会忽略入参，一律按照`fixed_leverage`处理 |
| multiple | string |  | 杠杆倍数<br><br>正整，范围为[1, 125] <br><br> 如不传，默认值为10 <br><br> 当`leverage=fixed_leverage`时，该参数生效 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | string |  | `success`设置成功 <br><br> `failure`设置失败 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695872676719,
  "data": "success"
}
```

## 跟随者查询当前跟单信息

`GET /api/v2/copy/mix-follower/query-current-orders`

限频规则：5次/秒/UID

Operation ID: `classicCopytradingFutureCopytradeFollowerQueryCurrentOrders`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| idLessThan | query | string |  | 请求此ID之前（更旧的数据）的分页内容，传的值为对应接口的 endId。 |
| idGreaterThan | query | string |  | 请求此ID之后（更新的数据）的分页内容，传的值为对应接口的 endId |
| startTime | query | string |  | 开始时间戳 <br><br>Unix时间戳的毫秒数格式，如 1597026383085<br><br>（时间跨度最大支持三个月，若不传结束时间，则默认结束时间为三个月。） |
| endTime | query | string |  | 结束时间戳 <br><br>Unix时间戳的毫秒数格式，如 1597026383085<br><br>（时间跨度最大支持三个月，若不传开始时间，则默认开始时间为三个月。） |
| limit | query | string |  | 查询条数 默认20，最大100 |
| symbol | query | string |  | 交易币对,支持大小写 |
| productType | query | string | 是 | 产品类型<br><br>`USDT-FUTURES` U本位合约<br><br>`COIN-FUTURES` 币本位合约<br><br>`USDC-FUTURES` USDC合约 |
| traderId | query | string |  | 交易员id |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.trackingList | object[] |  | 当前跟单记录列表 |
| data.trackingList[].trackingNo | string |  | 跟踪订单号 |
| data.trackingList[].traderId | string |  | 交易员UID |
| data.trackingList[].traderName | string |  | 交易员昵称 |
| data.trackingList[].openOrderId | string |  | 跟单开仓单号 |
| data.trackingList[].closeOrderId | string |  | 跟单平仓单号 |
| data.trackingList[].symbol | string |  | 交易对名称 |
| data.trackingList[].posSide | string |  | 持仓方向<br><br>`long` 双向持仓多头<br><br>`short` 双向持仓空头 |
| data.trackingList[].openLeverage | string |  | 开仓杠杆 |
| data.trackingList[].openPriceAvg | string |  | 开仓均价 |
| data.trackingList[].openTime | string |  | 开仓时间 |
| data.trackingList[].openFee | string |  | 开仓手续费<br><br>(只展示usdt，不展示抵扣) |
| data.trackingList[].openSize | string |  | 开仓数量 |
| data.trackingList[].openMarginSz | string |  | 开仓保证金数量 |
| data.trackingList[].closePriceAvg | string |  | 平仓均价 |
| data.trackingList[].closeSize | string |  | 平仓数量 |
| data.trackingList[].closeTime | string |  | 平仓时间 |
| data.endId | string |  | 最后一条跟单订单ID<br><br>用于 idLessThan/idGreaterThan 分页查询 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695807474823,
  "data": {
    "trackingList": [
      {
        "trackingNo": "1",
        "traderId": "**********",
        "openOrderId": "1",
        "closeOrderId": "",
        "symbol": "BTCUSDT",
        "posSide": "long",
        "openLeverage": "20",
        "openPriceAvg": "26248.9",
        "openTime": "1695801596651",
        "openSize": "0.2258000000000000",
        "openFee": "-5.92700162",
        "openMarginSz": "296.350081",
        "closePriceAvg": "",
        "closeSize": "0",
        "closeTime": "0",
        "traderName": "XXX"
      }
    ],
    "endId": "1"
  }
}
```

## 跟随者查询历史跟单信息

`GET /api/v2/copy/mix-follower/query-history-orders`

限频规则：5次/秒/UID

Operation ID: `classicCopytradingFutureCopytradeFollowerQueryHistoryOrders`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| idLessThan | query | string |  | 请求此ID之前（更旧的数据）的分页内容，传的值为对应接口的 endId。 |
| idGreaterThan | query | string |  | 请求此ID之后（更新的数据）的分页内容，传的值为对应接口的 endId |
| startTime | query | string |  | 开始时间戳 <br><br>Unix时间戳的毫秒数格式，如 1597026383085<br><br>（时间跨度最大支持三个月，若不传结束时间，则默认结束时间为三个月。） |
| endTime | query | string |  | 结束时间戳 <br><br>Unix时间戳的毫秒数格式，如 1597026383085<br><br>（时间跨度最大支持三个月，若不传开始时间，则默认开始时间为三个月。） |
| limit | query | string |  | 查询条数 默认100，最大100 |
| symbol | query | string |  | 交易币对,支持大小写 |
| productType | query | string | 是 | 产品类型<br><br>`USDT-FUTURES` U本位合约<br><br>`COIN-FUTURES` 币本位合约<br><br>`USDC-FUTURES` USDC合约 |
| traderId | query | string |  | 交易员id |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.trackingList | object[] |  | 跟单记录集合 |
| data.trackingList[].trackingNo | string |  | 跟踪订单号 |
| data.trackingList[].traderId | string |  | 交易员UID |
| data.trackingList[].openOrderId | string |  | 跟随者开仓单号 |
| data.trackingList[].closeOrderId | string |  | 跟随者平仓单号 |
| data.trackingList[].productType | string |  | 产品类型<br><br>`USDT-FUTURES` U本位合约<br><br>`COIN-FUTURES` 币本位合约<br><br>`USDC-FUTURES` USDC合约 |
| data.trackingList[].symbol | string |  | 交易对名称 |
| data.trackingList[].posSide | string |  | 持仓方向<br><br>`long` 双向持仓多头<br><br>`short` 双向持仓空头 |
| data.trackingList[].openLeverage | string |  | 开仓杠杆 |
| data.trackingList[].openPriceAvg | string |  | 开仓均价 |
| data.trackingList[].openTime | string |  | 开仓时间 |
| data.trackingList[].openSize | string |  | 开仓数量 |
| data.trackingList[].closePriceAvg | string |  | 平仓均价 |
| data.trackingList[].closeFee | string |  | 平仓手续费<br><br>(只展示usdt，不展示抵扣) |
| data.trackingList[].openFee | string |  | 开仓手续费<br><br>(只展示usdt，不展示抵扣) |
| data.trackingList[].closeSize | string |  | 平仓数量 |
| data.trackingList[].closeTime | string |  | 平仓时间 |
| data.trackingList[].profitRate | string |  | 收益率 |
| data.trackingList[].netProfit | string |  | 跟随净收益 |
| data.trackingList[].achievedPL | string |  | 已实现盈亏 |
| data.endId | string |  | 最后的跟踪订单id。指定idLessThan/idGreaterThan作为范围查询时以此为准。 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695808417159,
  "data": {
    "trackingList": [
      {
        "trackingNo": "123123123123",
        "posSide": "long",
        "openLeverage": "20",
        "openSize": "0.1852",
        "closeSize": "0.1852",
        "openPriceAvg": "32000.5",
        "closePriceAvg": "28233.0",
        "achievedPL": "-697.74100000",
        "openFee": "-5.92649260",
        "closeFee": "-5.22875160",
        "symbol": "BTCUSDT",
        "profitRate": "-235.47",
        "netProfit": "-697.74100000",
        "openOrderId": "1",
        "closeOrderId": "1",
        "openTime": "1695176941362",
        "closeTime": "1695353868557",
        "traderId": "**********",
        "productType": "usdt-futures"
      }
    ],
    "endId": ""
  }
}
```

## 跟随者设置仓位止盈止损

`POST /api/v2/copy/mix-follower/setting-tpsl`

限频规则：5次/秒/UID

Operation ID: `classicCopytradingFutureCopytradeFollowerSettingTpsl`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| trackingNo | string | 是 | 跟单号 |
| symbol | string |  | 交易对 |
| productType | string | 是 | 产品类型<br><br>`USDT-FUTURES` U本位合约<br><br>`COIN-FUTURES` 币本位合约<br><br>`USDC-FUTURES` USDC合约 |
| stopSurplusPrice | string |  | 止盈价<br><br>为空时，不管存不存在止盈都忽略或不更新，<br><br>为0时，若存在止盈则表示取消原有止盈。<br><br>大于等于0时，则表示更新或设置止盈。 |
| stopLossPrice | string |  | 止损价<br><br>为空时，不管存不存在止损都忽略或不更新，<br><br>为0时，若存在止损则表示取消原有止损。<br><br>大于等于0时，则表示更新或设置止损。 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | string |  | 结果<br><br>success 成功;fail 失败 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695812312921,
  "data": "success"
}
```

## 跟单员平仓

`POST /api/v2/copy/mix-follower/close-positions`

限频规则: 5次/秒/UID



跟单员平仓接口。可根据单号、币对、方向、仓位模式、保证金平仓

Operation ID: `classicCopytradingFutureCopytradeFollowerClosePositions`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| productType | string | 是 | 产品类型<br><br>`USDT-FUTURES` U本位合约<br><br>`COIN-FUTURES` 币本位合约<br><br>`USDC-FUTURES` USDC合约 |
| trackingNo | string |  | 跟单号<br><br>（如若传递单号，且保证交易对、保证金币种、仓位模式、持仓方向四者其中不为空时，需保证单号和其相呼应。） |
| symbol | string |  | 交易对 |
| marginCoin | string |  | 保证金币种 |
| marginMode | string |  | 仓位模式<br><br>isolated 逐仓 <br><br>cross 全仓 |
| holdSide | string |  | 持仓方向<br><br>1.买卖（单向持仓）模式下：可不填，若填则忽略。<br><br>2.开平仓模式（双向持仓）下： 必须填写此参数。<br><br>`long`：多仓 <br><br>`short`：空仓 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.orderIdList | string[] |  | 订单Id |

```json
{
  "code": "00000",
  "data": {
    "orderIdList": [
      "123",
      "321"
    ]
  },
  "msg": "success",
  "requestTime": 1627293504612
}
```

## 跟随者查看跟单设置

`GET /api/v2/copy/mix-follower/query-settings`

限频规则: 5次/秒/UID

Operation ID: `classicCopytradingFutureCopytradeFollowerQuerySettings`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| traderId | query | string | 是 | 跟单的交易员ID |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.followerEnable | string |  | 我是否在跟随<br><br>YES 是<br><br>NO 否 |
| data.detailList | object[] |  | 跟单详情 |
| data.detailList[].symbol | string |  | 交易对 |
| data.detailList[].productType | string |  | 产品类型<br><br>`USDT-FUTURES` U本位合约<br><br>`COIN-FUTURES` 币本位合约<br><br>`USDC-FUTURES` USDC合约 |
| data.detailList[].marginType | string |  | 保证金类型<br><br>`trader` 保证金类型跟随交易员;<br><br>`specify` 自己指定保证金类型; |
| data.detailList[].marginCoin | string |  | 保证金币种 |
| data.detailList[].leverType | string |  | 杠杆类型<br><br>`position` 使用仓位杠杆;<br><br>`specify` 使用指定杠杆;<br><br>`trader` 使用交易员杠杆; |
| data.detailList[].longLeverage | string |  | 多仓杠杆 |
| data.detailList[].shortLeverage | string |  | 空仓杠杆 |
| data.detailList[].traceType | string |  | 跟单仓位类型<br><br>`percent` 设置跟单金额对交易员开仓金额的比例，例如1，则表示跟交易员开仓金额相同，2表示开仓金额是交易员开仓金额的2倍;<br><br>`amount` 跟单金额指定固定金额;<br><br>`count` 跟单金额固定张数; |
| data.detailList[].traceValue | string |  | 跟单仓位值 |
| data.detailList[].maxHoldSize | string |  | 最大跟单张数 |
| data.detailList[].stopSurplusRatio | string |  | 止盈比例<br><br>1-400之内的正整数，<br><br>超过这个值为非法。 |
| data.detailList[].stopLossRatio | string |  | 止损比例<br><br>1-400之内的正整数，<br><br>超过这个值为非法。 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1679465100798,
  "data": {
    "followerEnable": "Yes",
    "detailList": [
      {
        "symbol": "ETHUSDT",
        "productType": "USDT-FUTURES",
        "marginType": "specify",
        "marginCoin": "USDT",
        "leverType": "trader",
        "longLeverage": "20",
        "shortLeverage": "20",
        "traceType": "percent",
        "traceValue": "1",
        "maxHoldSize": "50000",
        "stopSurplusRatio": "200",
        "stopLossRatio": ""
      }
    ]
  }
}
```

## 跟单设置

`POST /api/v2/copy/mix-follower/settings`

限频规则: 5次/秒/UID

Operation ID: `classicCopytradingFutureCopytradeFollowerSettings`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| traderId | string | 是 | 跟单的交易员ID |
| autoCopy | string |  | 是否自动跟随交易员新开的新币对(只在普通模式生效)  <br><br> on：自动跟随 <br><br> off：不自动跟随 |
| mode | string |  | 跟单模式    <br><br> basic：普通模式 <br><br> advanced(默认值)：高级模式 |
| settings | object[] | 是 | 跟单的设置(按照交易对)<br><br>最大为10 |
| settings[].symbol | string | 是 | 交易对 |
| settings[].productType | string | 是 | 产品类型<br><br>`USDT-FUTURES` U本位合约<br><br>`COIN-FUTURES` 币本位合约<br><br>`USDC-FUTURES` USDC合约 |
| settings[].marginType | string | 是 | 保证金类型(mode参数为advanced高级模式才生效)<br><br>`trader` 保证金类型跟随交易员;<br><br>`specify` 自己指定保证金类型; |
| settings[].marginCoin | string |  | 保证金币种 |
| settings[].leverType | string | 是 | 杠杆类型(mode参数为advanced高级模式才生效)<br><br>`position` 使用仓位杠杆;<br><br>`specify` 使用指定杠杆;<br><br>`trader` 使用交易员杠杆; |
| settings[].longLeverage | string |  | 多仓杠杆(mode参数为advanced高级模式才生效) |
| settings[].shortLeverage | string |  | 空仓杠杆(mode参数为advanced高级模式才生效) |
| settings[].traceType | string | 是 | 跟单仓位类型<br><br>`percent` 设置跟单金额对交易员开仓金额的比例，例如1，则表示跟交易员开仓金额相同，2表示开仓金额是交易员开仓金额的2倍;<br><br>`amount` 跟单金额指定固定金额;<br><br>`count` 跟单金额固定张数;(mode参数为advanced高级模式才生效) |
| settings[].traceValue | string | 是 | 跟单仓位值 |
| settings[].maxHoldSize | string |  | 最大跟单数量 |
| settings[].stopSurplusRatio | string |  | 止盈比例<br><br>1-400之内的正整数，<br><br>超过这个值为非法 |
| settings[].stopLossRatio | string |  | 止损比例<br><br>1-400之内的正整数，<br><br>超过这个值为非法 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | string |  | 结果<br><br>success 成功<br><br>fail 失败 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695809764463,
  "data": "success"
}
```

## 跟随者取消跟随交易员

`POST /api/v2/copy/mix-follower/cancel-trader`

限频规则: 5次/秒/UID

Operation ID: `classicCopytradingFutureCopytradeFollowerCancelTrader`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| traderId | string | 是 | 交易员uid |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | string |  | 结果<br><br>`success` 成功<br><br>`fail` 失败 |

```json
{
  "code": "00000",
  "data": "success",
  "msg": "success",
  "requestTime": 1627354109502
}
```

## 获取我的交易员列表

`GET /api/v2/copy/mix-follower/query-traders`

限频规则: 5次/秒/UID

Operation ID: `classicCopytradingFutureCopytradeFollowerQueryTraders`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| startTime | query | string |  | 开始时间戳 <br><br>Unix时间戳的毫秒数格式，如 1597026383085<br><br>（时间跨度最大支持三个月，若不传结束时间，则默认结束时间为三个月。） |
| endTime | query | string |  | 结束时间戳 <br><br>Unix时间戳的毫秒数格式，如 1597026383085<br><br>（时间跨度最大支持三个月，若不传开始时间，则默认开始时间为三个月。） |
| pageNo | query | string |  | 当前页号<br><br>默认为1. |
| pageSize | query | string |  | 查询数量<br><br>默认为20条，最大支持50条。 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].certificationType | string |  | 认证类型<br><br>`uncertified` 未认证<br><br>`certified` 已认证 |
| data[].traderId | string |  | 交易员ID |
| data[].traderName | string |  | 昵称 |
| data[].maxFollowLimit | string |  | 最大可跟人数 |
| data[].bgbMaxFollowLimit | string |  | bgb特殊跟随最大可跟人数 |
| data[].followCount | string |  | 当前已跟人数 |
| data[].bgbFollowCount | string |  | bgb特殊跟随当前已跟人数 |
| data[].traceTotalMarginAmount | string |  | 累计开仓保证金 |
| data[].traceTotalNetProfit | string |  | 累计净收益 |
| data[].traceTotalProfit | string |  | 累计总收益 |
| data[].currentTradingPairs | string[] |  | 当前带单 交易对 |
| data[].followerTime | string |  | 跟随日期（以初次跟随日期为准）<br><br>Unix时间戳的毫秒数格式，如 1597026383085 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695812788826,
  "data": [
    {
      "certificationType": "Uncertified",
      "traderId": "**********",
      "traderName": "x-1111111",
      "maxFollowLimit": "1000",
      "followCount": "0",
      "traceTotalMarginAmount": "1185.3286",
      "traceTotalNetProfit": "-744.7362",
      "traceTotalProfit": "-698.0210",
      "currentTradingPairs": [
        "BTCUSDT",
        "BTCUSD",
        "EOSUSDT",
        "ETHUSDT",
        "ETHUSD"
      ],
      "followerTime": "1693381832000",
      "bgbMaxFollowLimit": "100",
      "bgbFollowCount": "0"
    }
  ]
}
```

## 查询最大/最小跟随下单数量

`GET /api/v2/copy/mix-follower/query-quantity-limit`

限速规则: 10次/1s (ip)

Operation ID: `classicCopytradingFutureCopytradeFollowerQueryQuantityLimit`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string |  | 交易对 |
| productType | query | string | 是 | 产品类型<br><br>`USDT-FUTURES` U本位合约<br><br>`COIN-FUTURES` 币本位合约<br><br>`USDC-FUTURES` USDC合约 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].maxFollowSize | string |  | 最大下单量(交易币) |
| data[].minFollowSize | string |  | 最小下单量(交易币) |
| data[].symbol | string |  | 交易对名称 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695812926981,
  "data": [
    {
      "maxFollowSize": "20000",
      "minFollowSize": "0.005",
      "symbol": "BTCUSDT"
    }
  ]
}
```