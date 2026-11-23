---
exchange: bitget
source_url: https://www.bitget.com/docs/catalog/classic-copytrading-spot-follower
api_type: REST
updated_at: 2026-11-23 19:02:27.920117
---

# Classic Spot Copy Trading Follower API

Classic account — spot copy trading follower endpoints.

版本: 1.0.0

## 服务地址

- `https://api.bitget.com`

## 接口列表

- `POST /api/v2/copy/spot-follower/cancel-trader` — Cancel Follow
- `POST /api/v2/copy/spot-follower/order-close-tracking` — Sell And Sell in Batch
- `GET /api/v2/copy/spot-follower/query-current-orders` — Get Current Copy Trade Orders
- `GET /api/v2/copy/spot-follower/query-history-orders` — Get History Tracking Orders
- `GET /api/v2/copy/spot-follower/query-settings` — Get Follow Configuration
- `GET /api/v2/copy/spot-follower/query-trader-symbols` — Get Trader's Current Trading Pair
- `GET /api/v2/copy/spot-follower/query-traders` — My Trader List
- `POST /api/v2/copy/spot-follower/setting-tpsl` — Set Take Profit And Stop Loss
- `POST /api/v2/copy/spot-follower/settings` — Add or Modify Following Configurations
- `POST /api/v2/copy/spot-follower/stop-order` — Stop The Order

## Cancel Follow

`POST /api/v2/copy/spot-follower/cancel-trader`

Rate Limit: 1 req/sec/UID

Operation ID: `classicCopytradingSpotCopytradeFollowerCancelTrader`

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
| data | string |  | Result<br><br>`success` Success<br><br>others fail |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1656066841304,
  "data": ""
}
```

## Sell And Sell in Batch

`POST /api/v2/copy/spot-follower/order-close-tracking`

Rate Limit: 1 req/sec/UID

Operation ID: `classicCopytradingSpotCopytradeFollowerOrderCloseTracking`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| trackingNoList | string[] | 是 | Tracking numbers of buying orders grouped by trading pair; all successful or all failed; up to 50 order tracking numbers |
| symbol | string | 是 | Trading pair |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | string |  | Result<br><br>`success` Success<br><br>others fail |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1656066841304,
  "data": ""
}
```

## Get Current Copy Trade Orders

`GET /api/v2/copy/spot-follower/query-current-orders`

Rate limit: 5 req/sec/UID

Operation ID: `classicCopytradingSpotCopytradeFollowerQueryCurrentOrders`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string |  | Trading pair |
| traderId | query | string |  | trader id |
| idLessThan | query | string |  | Before requesting this ID |
| idGreaterThan | query | string |  | After requesting this ID |
| startTime | query | string |  | start time |
| endTime | query | string |  | end time ） |
| limit | query | string |  | The default is 20, with a maximum support of 50. More than 20 items will be returned |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.trackingList | object[] |  | tracking list |
| data.trackingList[].trackingNo | string |  | Track order number |
| data.trackingList[].traderId | string |  | trader Id |
| data.trackingList[].buyFillSize | string |  | Filled buy quantity |
| data.trackingList[].buyDelegateSize | string |  | Buy order quantity |
| data.trackingList[].buyPrice | string |  | buy price |
| data.trackingList[].unrealizedPL | string |  | Current unrealized PnL |
| data.trackingList[].buyTime | string |  | Time of buying |
| data.trackingList[].buyFee | string |  | Buying  transaction Fee |
| data.trackingList[].unrealizedPLR | string |  | Current ROI of unrealized PnL <br><br>If the value is 11.11, it represents 11.11% |
| data.trackingList[].symbol | string |  | Trading pair |
| data.trackingList[].stopSurplusPrice | string |  | Stop profit price |
| data.trackingList[].stopLossPrice | string |  | Stop loss price |
| data.endId | string |  | The final data ID. The ID value is the tracking number used for querying based on the ID |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695809370190,
  "data": {
    "endId": "1",
    "trackingList": [
      {
        "trackingNo": "1",
        "traderId": "**********",
        "buyFillSize": "0.0317",
        "buyDelegateSize": "0.0317190800000000",
        "buyPrice": "34870.7",
        "unrealizedPL": "-0.77945295",
        "buyTime": "1695729895491",
        "buyFee": "-0.00001908",
        "unrealizedPLR": "-0.07",
        "symbol": "BTCUSDT",
        "stopSurplusPrice": null,
        "stopLossPrice": null
      }
    ]
  }
}
```

## Get History Tracking Orders

`GET /api/v2/copy/spot-follower/query-history-orders`

Rate Limit: 5 req/sec/UID

Operation ID: `classicCopytradingSpotCopytradeFollowerQueryHistoryOrders`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string |  | Trading pair |
| traderId | query | string |  | trader Id |
| idLessThan | query | string |  | Before requesting this ID |
| idGreaterThan | query | string |  | After requesting this ID |
| startTime | query | string |  | start time |
| endTime | query | string |  | end time |
| limit | query | string |  | The default is 20, with a maximum support of 50. More than 20 items will be returned |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.trackingList | object[] |  | tracking list |
| data.trackingList[].trackingNo | string |  | Track order number |
| data.trackingList[].traderId | string |  | trader Id |
| data.trackingList[].fillSize | string |  | Filled quantity |
| data.trackingList[].buyPrice | string |  | Average buying price |
| data.trackingList[].sellPrice | string |  | Average selling price |
| data.trackingList[].achievedPL | string |  | Realized PnL |
| data.trackingList[].buyTime | string |  | Time of buying |
| data.trackingList[].sellTime | string |  | Time of selling |
| data.trackingList[].buyFee | string |  | Buying  transaction Fee |
| data.trackingList[].sellFee | string |  | Selling transaction fee |
| data.trackingList[].achievedPLR | string |  | ROI of realized PnL. If the value is 11.11, it represents 11.11%. |
| data.trackingList[].symbol | string |  | Trading pair |
| data.endId | string |  | The final data ID. The ID value is the tracking number used for querying based on the ID |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695811537460,
  "data": {
    "endId": "1",
    "trackingList": [
      {
        "trackingNo": "1",
        "traderId": "**********",
        "fillSize": "0.0316",
        "buyPrice": "34870.7",
        "sellPrice": "34865.5",
        "buyFee": "-0.00001902",
        "sellFee": "-0.66104988",
        "achievedPL": "-0.82756",
        "achievedPLR": "-0.07",
        "symbol": "BTCUSDT",
        "buyTime": "1695729617968",
        "sellTime": "1695729886269"
      }
    ]
  }
}
```

## Get Follow Configuration

`GET /api/v2/copy/spot-follower/query-settings`

Rate Limit: 10 req/sec/UID

Operation ID: `classicCopytradingSpotCopytradeFollowerQuerySettings`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| traderId | query | string | 是 | Trader user ID |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.enable | string |  | Am I following |
| data.profitRate | string |  | profit Rate |
| data.settledInDays | string |  | Trader membership period (starting from the registration date) |
| data.traderHeadPic | string |  | trader avatar |
| data.traderName | string |  | trader nick name |
| data.tradeSettingList | object[] |  | My copy trade settings |
| data.tradeSettingList[].maxTraceAmount | string |  | Maximum copy trade buying coin (base currency) |
| data.tradeSettingList[].stopLossRation | string |  | Stop-loss ratio <br><br>If the value is 11.11, it represents 11.11% |
| data.tradeSettingList[].stopSurplusRation | string |  | Take-profit ratio <br><br>If the value is 11.11, it represents 11.11% |
| data.tradeSettingList[].symbol | string |  | Trading pair ID |
| data.tradeSettingList[].traceType | string |  | Copy trade type<br><br>`percent` Set the percentage of the copy trade amount to the trader's elite trade amount. For example, 1 means the follower invests the same amount to open a position as the elite trader, and 2 means the follower invests twice the amount of the elite trader.<br><br>`amount` The fixed volume specified for copy trading<br><br>`count` Number of copy trade orders with fixed volume |
| data.tradeSymbolSettingList | object[] |  | Trading pair copy trading configuration |
| data.tradeSymbolSettingList[].maxStopLossRation | string |  | Maximum stop-loss ratio<br><br>If the value is 11.11, it represents 11.11% |
| data.tradeSymbolSettingList[].maxStopSurplusRation | string |  | Maximum take-profit ratio<br><br>If the value is 11.11, it represents 11.11% |
| data.tradeSymbolSettingList[].maxTraceAmount | string |  | Maximum copy trading volume (single order) |
| data.tradeSymbolSettingList[].maxTraceAmountSystem | string |  | System configuration for the maximum buying amount |
| data.tradeSymbolSettingList[].maxTraceSize | string |  | Maximum amount for copy trading |
| data.tradeSymbolSettingList[].maxTraceRation | string |  | Maximum copy trade ratio <br><br> (2 decimal places, e.g. 0.11 for 11%)<br><br>If the value is 11.11, it represents 11.11% |
| data.tradeSymbolSettingList[].minStopLossRation | string |  | Minimum stop-loss ratio <br><br> (2 decimal places, e.g. 0.11 for 11%)<br><br>If the value is 11.11, it represents 11.11% |
| data.tradeSymbolSettingList[].minStopSurplusRation | string |  | Minimum take-profit ratio <br><br>If the value is 11.11, it represents 11.11% |
| data.tradeSymbolSettingList[].minTraceAmount | string |  | Minimum copy trading volume |
| data.tradeSymbolSettingList[].minTraceSize | string |  | Minimum copy trade volume |
| data.tradeSymbolSettingList[].minTraceRation | string |  | Minimum order ratio |
| data.tradeSymbolSettingList[].sliderMaxStopLossRatio | string |  | Maximum stop loss ratio of slider |
| data.tradeSymbolSettingList[].sliderMaxStopSurplusRatio | string |  | Maximum take-profit ratio of slider |
| data.tradeSymbolSettingList[].symbol | string |  | Trading pair |
| data.endId | string |  | The last data id. The id value is the tracking number, used to query based on id |

```json
{
  "code": "00000",
  "data": {
    "enable": "YES",
    "profitRate": "5",
    "settledInDays": "53",
    "tradeSettingList": [
      {
        "maxTraceAmount": "50000",
        "stopLossRation": "10",
        "stopSurplusRation": "10",
        "symbol": "ETHUSDT",
        "traceType": "FIXED_AMOUNT"
      }
    ],
    "tradeSymbolSettingList": [
      {
        "maxStopLossRation": "90",
        "maxStopSurplusRation": "500",
        "maxTraceAmount": "1200",
        "maxTraceAmountSystem": "50000",
        "maxTraceSize": "500",
        "maxTraceRation": "20",
        "minStopLossRation": "0",
        "minStopSurplusRation": "0",
        "minTraceAmount": "10",
        "minTraceSize": "0.001",
        "minTraceRation": "0.1",
        "sliderMaxStopLossRatio": "90",
        "sliderMaxStopSurplusRatio": "500",
        "symbol": "BTCUSDT"
      }
    ],
    "traderHeadPic": "",
    "traderName": "139****0981"
  },
  "msg": "success",
  "requestTime": 1682401856339
}
```

## Get Trader's Current Trading Pair

`GET /api/v2/copy/spot-follower/query-trader-symbols`

Limit rule 10 times/1s (uid)

Operation ID: `classicCopytradingSpotCopytradeFollowerQueryTraderSymbols`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| traderId | query | string | 是 | trader Id |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.currentTradingList | string[] |  | Current copy trading pairs |

```json
{
  "code": "00000",
  "data": {
    "currentTradingList": [
      "ETHUSDT",
      "BTCUSDT"
    ]
  },
  "msg": "success",
  "requestTime": 1627354109502
}
```

## My Trader List

`GET /api/v2/copy/spot-follower/query-traders`

Rate Limit: 5 req/sec/UID

Operation ID: `classicCopytradingSpotCopytradeFollowerQueryTraders`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| pageNo | query | string |  | pageNo (default 1) |
| pageSize | query | string |  | The default is 20, and the maximum supported is 50. |
| startTime | query | string |  | start Time |
| endTime | query | string |  | end Time |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.resultList | object[] |  | Trader list |
| data.resultList[].certificationType | string |  | Certification type<br><br>uncertified<br><br>certified |
| data.resultList[].traceTotalAmount | string |  | Cumulative position opening value in USDT |
| data.resultList[].traceTotalNetProfit | string |  | Net profit in USDT |
| data.resultList[].traceTotalProfit | string |  | Total profit in USDT |
| data.resultList[].traderName | string |  | trader nick name |
| data.resultList[].traderId | string |  | trader Id |
| data.resultList[].maxFollowLimit | string |  | Maximum number of followers |
| data.resultList[].bgbMaxFollowLimit | string |  | Maximum number of followers granted by BGB holdings |
| data.resultList[].followCount | string |  | Number of current followers |
| data.resultList[].bgbFollowCount | string |  | Number of followers granted by BGB holdings |
| data.resultList[].followerTime | string |  | Following date (take the first following date)<br><br>Milliseconds format of timestamp Unix, e.g. 1597026383085 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695813674738,
  "data": {
    "resultList": [
      {
        "certificationType": "Uncertified",
        "traceTotalAmount": "16027.6543",
        "traceTotalNetProfit": "43.2480",
        "traceTotalProfit": "52.8743",
        "traderName": "BGU***9Z72",
        "traderId": "**********",
        "maxFollowLimit": "300",
        "bgbMaxFollowLimit": "",
        "followCount": "1",
        "bgbFollowCount": "",
        "followerTime": "1693533344295"
      }
    ]
  }
}
```

## Set Take Profit And Stop Loss

`POST /api/v2/copy/spot-follower/setting-tpsl`

Rate Limit: 1 req/sec/UID

Operation ID: `classicCopytradingSpotCopytradeFollowerSettingTpsl`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| trackingNo | string | 是 | tracking Order number |
| stopSurplusPrice | string |  | One of stopSurplusPrice and stopLossPrice must be passed.<br><br>TP price<br><br>When it is empty, it is ignored or not updated, no matter take-profit exists or not,<br><br>When it is 0, it means the original take-profit is canceled if there is a take-profit already.<br><br>When it is greater than or equal to 0, it means take-profit is updated or set. |
| stopLossPrice | string |  | One of stopSurplusPrice and stopLossPrice must be passed.<br><br>SL price<br><br>When it is empty, it is ignored or not updated, no matter stop-loss exists or not,<br><br>When it is 0, it means the original stop-loss is canceled if there is a stop-loss already.<br><br>When it is greater than or equal to 0, it means stop-loss is updated or set. |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | string |  | Result<br><br>`success` Success<br><br>others fail |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1656066841304,
  "data": ""
}
```

## Add or Modify Following Configurations

`POST /api/v2/copy/spot-follower/settings`

Rate Limit: 1 req/sec/UID

Operation ID: `classicCopytradingSpotCopytradeFollowerSettings`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| traderId | string | 是 | Trader user ID |
| autoCopy | string |  | Whether to automatically follow new symbol opened by traders(only take effect when parameter mode is basic)  <br><br> on：auto <br><br> off：no |
| mode | string |  | follow mode    <br><br> basic：basic mode <br><br> advanced（default）：advanced mode |
| settings | object[] | 是 | settings |
| settings[].symbol | string | 是 | Trading pair |
| settings[].traceType | string | 是 | Copy trade type<br><br>`percent` Set the percentage of the copy trade amount to the trader's elite trade amount. For example, 1 means the follower invests the same amount to open a position as the elite trader, and 2 means the follower invests twice the amount of the elite trader.<br><br>`amount` The fixed volume specified for copy trading<br><br>`count` Number of copy trade orders with fixed volume (only take effect when parameter mode is advanced) |
| settings[].maxHoldSize | string | 是 | Maximum following buying quantity |
| settings[].traceValue | string | 是 | Copy trade investment amount <br><br>100 or 0.1 <br><br>TraceType parameter corresponding to the value |
| settings[].stopLossRatio | string |  | The stop-loss ratio can only be a positive integer. 10 means 10%. |
| settings[].stopSurplusRatio | string |  | The take-profit ratio can only be a positive integer. 10 means 10%. |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | string |  | Result<br><br>`success` Success<br><br>others fail |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1656066841304,
  "data": ""
}
```

## Stop The Order

`POST /api/v2/copy/spot-follower/stop-order`

Rate Limit: 1 req/sec/UID

Operation ID: `classicCopytradingSpotCopytradeFollowerStopOrder`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| trackingNoList | string[] | 是 | Order tracking number groups<br><br>Up to 50.<br><br>Atomic execution results, either all successful or all failed. |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | string |  | Result<br><br>`success` Success<br><br>others fail |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1656066841304,
  "data": ""
}
```


---

经典账户 — 现货跟单跟单员相关接口。

版本: 1.0.0

## 服务地址

- `https://api.bitget.com`

## 接口列表

- `GET /api/v2/copy/spot-follower/query-current-orders` — 查询当前跟单信息
- `POST /api/v2/copy/spot-follower/stop-order` — 跟随者终止跟随
- `GET /api/v2/copy/spot-follower/query-history-orders` — 查询历史跟单信息
- `POST /api/v2/copy/spot-follower/setting-tpsl` — 设置止盈止损
- `POST /api/v2/copy/spot-follower/order-close-tracking` — 卖出和批量卖出
- `GET /api/v2/copy/spot-follower/query-settings` — 跟随者查询跟随配置
- `GET /api/v2/copy/spot-follower/query-traders` — 我的交易员列表
- `POST /api/v2/copy/spot-follower/settings` — 跟随者新增或修改跟随配置
- `POST /api/v2/copy/spot-follower/cancel-trader` — 取消跟随
- `GET /api/v2/copy/spot-follower/query-trader-symbols` — 查看交易员当前带单币对

## 查询当前跟单信息

`GET /api/v2/copy/spot-follower/query-current-orders`

限速规则: 5次/秒/UID

Operation ID: `classicCopytradingSpotCopytradeFollowerQueryCurrentOrders`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string |  | 交易对 |
| traderId | query | string |  | 交易员id |
| idLessThan | query | string |  | 请求此ID之前 |
| idGreaterThan | query | string |  | 请求此ID之后 |
| startTime | query | string |  | 开始时间戳 <br><br>Unix时间戳的毫秒数格式，如 1597026383085（时间跨度最大支持三个月，若不传结束时间，则默认结束时间为三个月。） |
| endTime | query | string |  | 结束时间戳 <br><br>Unix时间戳的毫秒数格式，如 1597026383085（时间跨度最大支持三个月，若不传开始时间，则默认开始时间为三个月。） |
| limit | query | string |  | 默认20条，最大支持50条。超过将返回20条 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.trackingList | object[] |  | 跟单集合 |
| data.trackingList[].trackingNo | string |  | 跟踪订单号 |
| data.trackingList[].traderId | string |  | 交易员uid |
| data.trackingList[].buyFillSize | string |  | 买入成交数量 |
| data.trackingList[].buyDelegateSize | string |  | 买入委托数量 |
| data.trackingList[].buyPrice | string |  | 买入价格 |
| data.trackingList[].unrealizedPL | string |  | 当前未实现盈亏 |
| data.trackingList[].buyTime | string |  | 买入时间 |
| data.trackingList[].buyFee | string |  | 买入手续费 |
| data.trackingList[].unrealizedPLR | string |  | 当前未实现盈亏收益率,若值为11.11，则代表11.11% |
| data.trackingList[].symbol | string |  | 交易对 |
| data.trackingList[].stopSurplusPrice | string |  | 止盈价格 |
| data.trackingList[].stopLossPrice | string |  | 止损价格 |
| data.endId | string |  | 最后的数据id。id值为跟踪单号，用于根据id查询 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695809370190,
  "data": {
    "endId": "1",
    "trackingList": [
      {
        "trackingNo": "1",
        "traderId": "**********",
        "buyFillSize": "0.0317",
        "buyDelegateSize": "0.0317190800000000",
        "buyPrice": "34870.7",
        "unrealizedPL": "-0.77945295",
        "buyTime": "1695729895491",
        "buyFee": "-0.00001908",
        "unrealizedPLR": "-0.07",
        "symbol": "BTCUSDT",
        "stopSurplusPrice": null,
        "stopLossPrice": null
      }
    ]
  }
}
```

## 跟随者终止跟随

`POST /api/v2/copy/spot-follower/stop-order`

限速规则: 1次/秒/UID

Operation ID: `classicCopytradingSpotCopytradeFollowerStopOrder`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| trackingNoList | string[] | 是 | 跟单号列表<br><br>最多50个<br><br>要么全部成功，要么全部失败 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | string |  | 执行结果<br><br>`success` 成功<br><br>其它值 失败 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1656066841304,
  "data": ""
}
```

## 查询历史跟单信息

`GET /api/v2/copy/spot-follower/query-history-orders`

限速规则: 5次/秒/UID

Operation ID: `classicCopytradingSpotCopytradeFollowerQueryHistoryOrders`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string |  | 交易对 |
| traderId | query | string |  | 交易员id |
| idLessThan | query | string |  | 请求此ID之前 |
| idGreaterThan | query | string |  | 请求此ID之后 |
| startTime | query | string |  | 开始时间戳 <br><br>Unix时间戳的毫秒数格式，如 1597026383085（时间跨度最大支持三个月，若不传结束时间，则默认结束时间为三个月。） |
| endTime | query | string |  | 结束时间戳 <br><br>Unix时间戳的毫秒数格式，如 1597026383085（时间跨度最大支持三个月，若不传开始时间，则默认开始时间为三个月。） |
| limit | query | string |  | 默认20条，最大支持50条。超过将返回20条 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.trackingList | object[] |  | 跟单集合 |
| data.trackingList[].trackingNo | string |  | 跟踪订单号 |
| data.trackingList[].traderId | string |  | 交易员uid |
| data.trackingList[].fillSize | string |  | 成交数量 |
| data.trackingList[].buyPrice | string |  | 买入价格 |
| data.trackingList[].sellPrice | string |  | 卖出均价 |
| data.trackingList[].achievedPL | string |  | 已实现盈亏收益 |
| data.trackingList[].buyTime | string |  | 买入时间 |
| data.trackingList[].sellTime | string |  | 卖出时间 |
| data.trackingList[].buyFee | string |  | 买入手续费 |
| data.trackingList[].sellFee | string |  | 卖出手续费 |
| data.trackingList[].achievedPLR | string |  | 已实现盈亏收益率若值为11.11，则代表11.11% |
| data.trackingList[].symbol | string |  | 交易对 |
| data.endId | string |  | 最后的数据id。id值为跟踪单号，用于根据id查询 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695811537460,
  "data": {
    "endId": "1",
    "trackingList": [
      {
        "trackingNo": "1",
        "traderId": "**********",
        "fillSize": "0.0316",
        "buyPrice": "34870.7",
        "sellPrice": "34865.5",
        "buyFee": "-0.00001902",
        "sellFee": "-0.66104988",
        "achievedPL": "-0.82756",
        "achievedPLR": "-0.07",
        "symbol": "BTCUSDT",
        "buyTime": "1695729617968",
        "sellTime": "1695729886269"
      }
    ]
  }
}
```

## 设置止盈止损

`POST /api/v2/copy/spot-follower/setting-tpsl`

限速规则: 1次/秒/UID

Operation ID: `classicCopytradingSpotCopytradeFollowerSettingTpsl`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| trackingNo | string | 是 | 跟踪订单号 |
| stopSurplusPrice | string |  | 止盈价（为空时，不管存不存在止盈都忽略或不更新，为0时，若存在止盈则表示取消原有止盈。大于0时，则表示更新或设置止盈。） |
| stopLossPrice | string |  | 止损价(为空时，不管存不存在止损都忽略或不更新，为0时，若存在止损则表示取消原有止损。大于0时，则表示更新或设置止损。) |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | string |  | 执行结果<br><br>`success` 成功<br><br>其它值 失败 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1656066841304,
  "data": ""
}
```

## 卖出和批量卖出

`POST /api/v2/copy/spot-follower/order-close-tracking`

限速规则: 1次/秒/UID

Operation ID: `classicCopytradingSpotCopytradeFollowerOrderCloseTracking`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| trackingNoList | string[] | 是 | 按买入币对分组trackingNo，全部成功或全部失败，跟踪订单号，最大50个 |
| symbol | string | 是 | 交易对 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | string |  | 执行结果<br><br>`success` 成功<br><br>其它值 失败 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1656066841304,
  "data": ""
}
```

## 跟随者查询跟随配置

`GET /api/v2/copy/spot-follower/query-settings`

限速规则: 5次/秒/UID

Operation ID: `classicCopytradingSpotCopytradeFollowerQuerySettings`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| traderId | query | string | 是 | 交易员id |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.enable | string |  | 我是否在跟随, `YES` `NO` |
| data.profitRate | string |  | 分润比例 |
| data.settledInDays | string |  | 交易员入驻天数(从他在平台注册开始) |
| data.traderHeadPic | string |  | 交易员头像 |
| data.traderName | string |  | 交易员昵称 |
| data.tradeSettingList | object[] |  | 我的跟单设置 |
| data.tradeSettingList[].maxTraceAmount | string |  | 最大跟随买入金（右币） |
| data.tradeSettingList[].stopLossRation | string |  | 止损比例 |
| data.tradeSettingList[].stopSurplusRation | string |  | 止盈比例 |
| data.tradeSettingList[].symbol | string |  | 币对ID |
| data.tradeSettingList[].traceType | string |  | 跟单类型<br><br>`percent` 设置跟单金额对交易员开仓金额的比例，例如1，则表示跟交易员开仓金额相同，2表示开仓金额是交易员开仓金额的2倍;<br><br>`amount` 跟单金额指定固定金额;<br><br>`count` 跟单金额固定张数; |
| data.tradeSymbolSettingList | object[] |  | 币对跟单配置 |
| data.tradeSymbolSettingList[].maxStopLossRation | string |  | 最大止损比例 |
| data.tradeSymbolSettingList[].maxStopSurplusRation | string |  | 最大止盈比例 |
| data.tradeSymbolSettingList[].maxTraceAmount | string |  | 最大跟单金额（单次） |
| data.tradeSymbolSettingList[].maxTraceAmountSystem | string |  | 最大买入数量限制系统配置 |
| data.tradeSymbolSettingList[].maxTraceSize | string |  | 最大跟单数量 |
| data.tradeSymbolSettingList[].maxTraceRation | string |  | 最大跟单比例 |
| data.tradeSymbolSettingList[].minStopLossRation | string |  | 最小止损比例 |
| data.tradeSymbolSettingList[].minStopSurplusRation | string |  | 最小止盈比例 |
| data.tradeSymbolSettingList[].minTraceAmount | string |  | 最小跟单金额 |
| data.tradeSymbolSettingList[].minTraceSize | string |  | 最小跟单数量 |
| data.tradeSymbolSettingList[].minTraceRation | string |  | 最小跟单比例 |
| data.tradeSymbolSettingList[].sliderMaxStopLossRatio | string |  | 滑竿最大止损比例 |
| data.tradeSymbolSettingList[].sliderMaxStopSurplusRatio | string |  | 滑竿最大止盈比例 |
| data.tradeSymbolSettingList[].symbol | string |  | 交易对 |
| data.endId | string |  | 最后的数据id。id值为跟踪单号，用于根据id查询 |

```json
{
  "code": "00000",
  "data": {
    "enable": "YES",
    "profitRate": "5",
    "settledInDays": "53",
    "tradeSettingList": [
      {
        "maxTraceAmount": "50000",
        "stopLossRation": "10",
        "stopSurplusRation": "10",
        "symbol": "ETHUSDT",
        "traceType": "FIXED_AMOUNT"
      }
    ],
    "tradeSymbolSettingList": [
      {
        "maxStopLossRation": "90",
        "maxStopSurplusRation": "500",
        "maxTraceAmount": "1200",
        "maxTraceAmountSystem": "50000",
        "maxTraceSize": "500",
        "maxTraceRation": "20",
        "minStopLossRation": "0",
        "minStopSurplusRation": "0",
        "minTraceAmount": "10",
        "minTraceSize": "0.001",
        "minTraceRation": "0.1",
        "sliderMaxStopLossRatio": "90",
        "sliderMaxStopSurplusRatio": "500",
        "symbol": "BTCUSDT"
      }
    ],
    "traderHeadPic": "",
    "traderName": "139****0981"
  },
  "msg": "success",
  "requestTime": 1682401856339
}
```

## 我的交易员列表

`GET /api/v2/copy/spot-follower/query-traders`

限速规则: 5次/秒/UID

Operation ID: `classicCopytradingSpotCopytradeFollowerQueryTraders`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| pageNo | query | string |  | pageNo (default 1) |
| pageSize | query | string |  | 默认为20条，最大支持50条。 |
| startTime | query | string |  | 开始时间 |
| endTime | query | string |  | 结束时间 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.resultList | object[] |  | 交易员列表 |
| data.resultList[].certificationType | string |  | 认证类型 |
| data.resultList[].traceTotalAmount | string |  | 累计开仓价值 , USDT |
| data.resultList[].traceTotalNetProfit | string |  | 净收益 , USDT |
| data.resultList[].traceTotalProfit | string |  | 累计总收益 , USDT |
| data.resultList[].traderName | string |  | 交易员昵称 |
| data.resultList[].traderId | string |  | 交易员ID |
| data.resultList[].maxFollowLimit | string |  | 最大可跟人数 |
| data.resultList[].bgbMaxFollowLimit | string |  | bgb特殊跟随最大可跟人数 |
| data.resultList[].followCount | string |  | 当前已跟人数 |
| data.resultList[].bgbFollowCount | string |  | bgb特殊跟随当前已跟人数 |
| data.resultList[].followerTime | string |  | 跟随日期（以初次跟随日期为准）<br><br>Unix时间戳的毫秒数格式，如 1597026383085 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695813674738,
  "data": {
    "resultList": [
      {
        "certificationType": "Uncertified",
        "traceTotalAmount": "16027.6543",
        "traceTotalNetProfit": "43.2480",
        "traceTotalProfit": "52.8743",
        "traderName": "BGU***9Z72",
        "traderId": "**********",
        "maxFollowLimit": "300",
        "bgbMaxFollowLimit": "",
        "followCount": "1",
        "bgbFollowCount": "",
        "followerTime": "1693533344295"
      }
    ]
  }
}
```

## 跟随者新增或修改跟随配置

`POST /api/v2/copy/spot-follower/settings`

限速规则: 1次/秒/UID

Operation ID: `classicCopytradingSpotCopytradeFollowerSettings`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| traderId | string | 是 | 交易员ID |
| autoCopy | string |  | 是否自动跟随交易员新开的新币对(只在普通模式生效)  <br><br> on：自动跟随 <br><br> off：不自动跟随 |
| mode | string |  | 跟单模式    <br><br> basic：普通模式 <br><br> advanced(默认值)：高级模式 |
| settings | object[] | 是 | 配置 |
| settings[].symbol | string | 是 | 交易币对 |
| settings[].traceType | string | 是 | 跟单类型<br><br>`percent` 设置跟单金额对交易员开仓金额的比例，例如1，则表示跟交易员开仓金额相同，2表示开仓金额是交易员开仓金额的2倍;<br><br>`amount` 跟单金额指定固定金额;<br><br>`count` 跟单金额固定张数(mode参数为advanced高级模式才生效); |
| settings[].maxHoldSize | string | 是 | 最大跟随买入数量 |
| settings[].traceValue | string | 是 | 跟投值 |
| settings[].stopLossRatio | string |  | 止损比例 只能整数 10 代表 10% |
| settings[].stopSurplusRatio | string |  | 止盈比例 只能整数 10 代表 10% |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | string |  | 执行结果<br><br>`success` 成功<br><br>其它值 失败 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1656066841304,
  "data": ""
}
```

## 取消跟随

`POST /api/v2/copy/spot-follower/cancel-trader`

限速规则: 1次/秒/UID

Operation ID: `classicCopytradingSpotCopytradeFollowerCancelTrader`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| traderId | string | 是 | 交易员ID |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | string |  | 执行结果<br><br>`success` 成功<br><br>其它值 失败 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1656066841304,
  "data": ""
}
```

## 查看交易员当前带单币对

`GET /api/v2/copy/spot-follower/query-trader-symbols`

限速规则: 10次/1s (uid)

Operation ID: `classicCopytradingSpotCopytradeFollowerQueryTraderSymbols`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| traderId | query | string | 是 | 交易员ID |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.currentTradingList | string[] |  | 当前带单币对 |

```json
{
  "code": "00000",
  "data": {
    "currentTradingList": [
      "ETHUSDT",
      "BTCUSDT"
    ]
  },
  "msg": "success",
  "requestTime": 1627354109502
}
```