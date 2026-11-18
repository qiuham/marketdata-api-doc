---
exchange: bitget
source_url: https://www.bitget.com/docs/catalog/classic-copytrading-spot-trader
api_type: REST
updated_at: 2026-11-18 19:01:15.253327
---

# Classic Spot Copy Trading Trader API

Classic account — spot copy trading trader endpoints.

版本: 1.0.0

## 服务地址

- `https://api.bitget.com`

## 接口列表

- `GET /api/v2/copy/spot-trader/config-query-followers` — My Follower List
- `GET /api/v2/copy/spot-trader/config-query-settings` — Get Copytrade Configuration
- `POST /api/v2/copy/spot-trader/config-remove-follower` — Remove Followers
- `POST /api/v2/copy/spot-trader/config-setting-symbols` — Set Copytrade Symbols
- `POST /api/v2/copy/spot-trader/order-close-tracking` — Sell And Sell in Batch
- `GET /api/v2/copy/spot-trader/order-current-track` — Get Current Tracking Orders
- `GET /api/v2/copy/spot-trader/order-history-track` — Get History Tracking Orders
- `POST /api/v2/copy/spot-trader/order-modify-tpsl` — Modify Take Profit and Stop Loss
- `GET /api/v2/copy/spot-trader/order-total-detail` — Get Data Indicator Statistics
- `GET /api/v2/copy/spot-trader/profit-details` — Get Unrealized Profit Sharing Details
- `GET /api/v2/copy/spot-trader/profit-history-details` — Get History Profit Sharing Details
- `GET /api/v2/copy/spot-trader/profit-summarys` — Get Profit Summary

## My Follower List

`GET /api/v2/copy/spot-trader/config-query-followers`

Limit rule 10 times/1s (uid)

Operation ID: `classicCopytradingSpotCopytradeTraderConfigQueryFollowers`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| pageNo | query | string |  | pageNo (default 1) |
| pageSize | query | string |  | pageSize(default 30 max 1000) |
| startTime | query | string |  | start time |
| endTime | query | string |  | end time |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].accountEquity | string |  | Account asset value |
| data[].isRemove | string |  | Is it able to remove followers?<br><br>yes: yes; no: no |
| data[].followerHeadPic | string |  | Follower avatar |
| data[].followerName | string |  | Follower Nickname |
| data[].followerUid | string |  | Follower user id |
| data[].followerTime | string |  | Following date (take the first following date)<br><br>Unix timestamp in milliseconds format, e.g. 1597026383085 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695807814833,
  "data": [
    {
      "accountEquity": "1001711.2164",
      "isRemove": "NO",
      "followerHeadPic": null,
      "followerName": "BGU***1QK5",
      "followerUid": "**********",
      "followerTime": "1693533344295"
    }
  ]
}
```

## Get Copytrade Configuration

`GET /api/v2/copy/spot-trader/config-query-settings`

Rate Limit: 5 req/sec/UID

Operation ID: `classicCopytradingSpotCopytradeTraderConfigQuerySettings`

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.removeLimitUsdt | string |  | The maximum limit of follower assets can be removed.<br><br>(followers with the assets less than this value can be removed) |
| data.spotInfoList | object[] |  | Overview of elite trade amount |
| data.spotInfoList[].maxQuoteSize | string |  | Maximum single order amount (price currency) |
| data.spotInfoList[].surplusQuoteSize | string |  | Remaining amount (price currency) |
| data.spotInfoList[].symbol | string |  | symbol |
| data.labelList | object[] |  | Tag overview |
| data.labelList[].id | string |  | tag id |
| data.labelList[].name | string |  | tag name |
| data.enable | string |  | Activate elite trading or not?<br><br>yes: on; no: off |
| data.showAssetsMap | string |  | Display composition of assets or not?<br><br>yes: on; no: off |
| data.showEquity | string |  | Display total funds or not?<br><br>yes: on; no: off |
| data.traceSymbolList | object[] |  | Overview of trading pairs for elite trades |
| data.traceSymbolList[].enable | string |  | Is this trading pair open for elite trades?<br><br>yes: on; no: off |
| data.traceSymbolList[].symbol | string |  | Trading pair |
| data.traceSymbolList[].minOpenCount | string |  | Minimum number of elite trades for elite traders |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695807020372,
  "data": {
    "removeLimitUsdt": "100",
    "spotInfoList": [
      {
        "maxQuoteSize": "5000000",
        "surplusQuoteSize": "4998894.59",
        "symbol": "BTCUSDT"
      },
      {
        "maxQuoteSize": "300000",
        "surplusQuoteSize": "300000",
        "symbol": "ETHBTC"
      },
      {
        "maxQuoteSize": "50000",
        "surplusQuoteSize": "50000",
        "symbol": "ETHUSDT"
      }
    ],
    "labelList": [],
    "enable": "YES",
    "showAssetsMap": "NO",
    "showEquity": "NO",
    "traceSymbolList": [
      {
        "enable": "NO",
        "symbol": "BGBUSDT",
        "minOpenCount": "0.0001"
      },
      {
        "enable": "YES",
        "symbol": "BTCUSDT",
        "minOpenCount": "0.0005"
      },
      {
        "enable": "YES",
        "symbol": "ETHBTC",
        "minOpenCount": "0.0001"
      },
      {
        "enable": "YES",
        "symbol": "ETHUSDT",
        "minOpenCount": "0.0001"
      }
    ]
  }
}
```

## Remove Followers

`POST /api/v2/copy/spot-trader/config-remove-follower`

Rate Limit: 1 req/sec/UID

Operation ID: `classicCopytradingSpotCopytradeTraderConfigRemoveFollower`

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
| data | string |  | Result code<br><br>`00000`success<br><br>others fail |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1656066841304,
  "data": ""
}
```

## Set Copytrade Symbols

`POST /api/v2/copy/spot-trader/config-setting-symbols`

Rate Limit: 1 req/sec/UID

Operation ID: `classicCopytradingSpotCopytradeTraderConfigSettingSymbols`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| symbolList | string[] | 是 | Collection with single currency pairs<br><br>Maximum 50 |
| settingType | string | 是 | Setting type<br><br>add new;<br><br>delete delete; |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | string |  | Result code<br><br>`00000`success<br><br>others fail |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1656066841304,
  "data": ""
}
```

## Sell And Sell in Batch

`POST /api/v2/copy/spot-trader/order-close-tracking`

Rate Limit: 1 req/sec/UID

Operation ID: `classicCopytradingSpotCopytradeTraderOrderCloseTracking`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| trackingNoList | string[] | 是 | Categorizing trackingNo by buying trading pairs<br><br>All success or all fail, track order number, maximum: 50 |
| symbol | string | 是 | Trading pair |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | string |  | Result code<br><br>`00000`success<br><br>others fail |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1656066841304,
  "data": ""
}
```

## Get Current Tracking Orders

`GET /api/v2/copy/spot-trader/order-current-track`

Limit rule 10 times/1s (uid)

Operation ID: `classicCopytradingSpotCopytradeTraderOrderCurrentTrack`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string |  | Trading pair |
| idLessThan | query | string |  | Before requesting this ID |
| idGreaterThan | query | string |  | After requesting this ID |
| startTime | query | string |  | start time |
| endTime | query | string |  | end time |
| limit | query | string |  | The default is 20, and the maximum supported is 50. More than 20 items will be returned |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.trackingList | object[] |  | tracking order collection |
| data.trackingList[].trackingNo | string |  | Track order number |
| data.trackingList[].orderId | string |  | order number |
| data.trackingList[].buyFillSize | string |  | Number of filled buy orders |
| data.trackingList[].buyDelegateSize | string |  | Buy order quantity |
| data.trackingList[].buyPrice | string |  | buy Price |
| data.trackingList[].unrealizedPL | string |  | Current unrealized PnL |
| data.trackingList[].buyTime | string |  | Time of buying |
| data.trackingList[].buyFee | string |  | Buying  transaction fee |
| data.trackingList[].unrealizedPLR | string |  | ROI of unrealized PnL. If the value is 11.11, it represents 11.11%. |
| data.trackingList[].symbol | string |  | Trading pair |
| data.trackingList[].stopLossPrice | string |  | Stop loss price |
| data.trackingList[].stopSurplusPrice | string |  | Take profit price |
| data.trackingList[].followCount | string |  | Number of followers for this order |
| data.endId | string |  | The last data id. The id value is the tracking number, which is used to query based on id. |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695803899870,
  "data": {
    "endId": "1",
    "trackingList": [
      {
        "trackingNo": "1",
        "orderId": "1",
        "buyFillSize": "0.0317",
        "buyDelegateSize": "0.0317190800000000",
        "buyPrice": "34870.7",
        "unrealizedPL": "-0.79530295",
        "buyTime": "1695729894873",
        "buyFee": "-0.00001908",
        "unrealizedPLR": "-0.07",
        "symbol": "BTCUSDT",
        "stopLossPrice": null,
        "stopSurplusPrice": null,
        "followCount": "1"
      }
    ]
  }
}
```

## Get History Tracking Orders

`GET /api/v2/copy/spot-trader/order-history-track`

Rate Limit: 5req/sec/UID

Operation ID: `classicCopytradingSpotCopytradeTraderOrderHistoryTrack`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| idLessThan | query | string |  | Request the paging content before this ID (older data), and the passed value is the endId of the corresponding interface. |
| idGreaterThan | query | string |  | Request the paging content after this ID (updated data). The value passed is the endId of the corresponding interface. |
| startTime | query | string |  | start time |
| endTime | query | string |  | end time |
| limit | query | string |  | Number of queries: Default 20, maximum 100 |
| symbol | query | string |  | symbol |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.trackingList | object[] |  | Overview of elite trade records |
| data.trackingList[].trackingNo | string |  | Track order number |
| data.trackingList[].fillSize | string |  | Filled quantity |
| data.trackingList[].buyPrice | string |  | buy price |
| data.trackingList[].sellPrice | string |  | sell price |
| data.trackingList[].achievedPL | string |  | Realized PnL |
| data.trackingList[].buyTime | string |  | Time of buying |
| data.trackingList[].sellTime | string |  | Time of selling |
| data.trackingList[].buyFee | string |  | Buying transaction fee |
| data.trackingList[].sellFee | string |  | Selling transaction fee |
| data.trackingList[].achievedPLR | string |  | ROI of realized PnL. If the value is 11.11, it represents 11.11%. |
| data.trackingList[].symbol | string |  | Trading pair |
| data.trackingList[].netProfit | string |  | Net profit (negative value presents a loss) |
| data.trackingList[].followCount | string |  | Number of followers for this order |
| data.endId | string |  | The last tracking order id. <br><br>This shall prevail when specifying idLessThan/idGreaterThan as the range query |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695805248324,
  "data": {
    "endId": "1",
    "trackingList": [
      {
        "trackingNo": "1",
        "fillSize": "0.0317",
        "buyPrice": "34869.2",
        "sellPrice": "34865.5",
        "achievedPL": "-0.78259",
        "buyTime": "1695728919902",
        "sellTime": "1695729885589",
        "buyFee": "-0.00001908",
        "sellFee": "-0.66314181",
        "achievedPLR": "-0.07",
        "symbol": "BTCUSDT",
        "netProfit": "-1.44573",
        "followCount": "1"
      }
    ]
  }
}
```

## Modify Take Profit and Stop Loss

`POST /api/v2/copy/spot-trader/order-modify-tpsl`

Rate Limit: 1 req/sec/UID

Operation ID: `classicCopytradingSpotCopytradeTraderOrderModifyTpsl`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| trackingNo | string | 是 | Track order number |
| stopSurplusPrice | string |  | One of stopSurplusPrice and stopLossPrice must be passed.<br><br>TP price<br><br>When it is empty, it is ignored or not updated, no matter take-profit exists or not,<br><br>When it is 0, it means the original take-profit is canceled if there is a take-profit already.<br><br>When it is greater than or equal to 0, it means take-profit is updated or set. |
| stopLossPrice | string |  | One of stopSurplusPrice and stopLossPrice must be passed.<br><br>When it is empty, it is ignored or not updated, no matter stop-loss exists or not,<br><br>When it is 0, it means the original stop-loss is canceled if there is a stop-loss already.<br><br>When it is greater than or equal to 0, it means stop-loss is updated or set. |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | string |  | Result code<br><br>`00000`success<br><br>others fail |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1656066841304,
  "data": ""
}
```

## Get Data Indicator Statistics

`GET /api/v2/copy/spot-trader/order-total-detail`

Rate Limit: 5 req/sec/UID

Operation ID: `classicCopytradingSpotCopytradeTraderOrderTotalDetail`

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.totalFollowerNum | string |  | Total followers |
| data.currentFollowerNum | string |  | Current number of followers |
| data.maxFollowerNum | string |  | Maximum number of followers for the elite trader |
| data.tradingOrderNum | string |  | Total opening orders |
| data.totalpl | string |  | Total profit<br><br>(USDT) |
| data.gainNum | string |  | Ratio of profitable trades |
| data.lossNum | string |  | Ratio of losing trades |
| data.totalEquity | string |  | Total assets |
| data.winRate | string |  | Win rate |
| data.lastWeekRoiList | object[] |  | ROI for the last week |
| data.lastWeekRoiList[].rate | string |  | rate |
| data.lastWeekRoiList[].ctime | string |  | time |
| data.lastMonthRoiList | object[] |  | 30-day ROI |
| data.lastMonthRoiList[].rate | string |  | rate |
| data.lastMonthRoiList[].ctime | string |  | time |
| data.lastWeekProfitList | object[] |  | Profit for the last week |
| data.lastWeekProfitList[].amount | string |  | amount, USDT |
| data.lastWeekProfitList[].ctime | string |  | time |
| data.lastMonthProfitList | object[] |  | 30-day Profit |
| data.lastMonthProfitList[].amount | string |  | amount, USDT |
| data.lastMonthProfitList[].ctime | string |  | time |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695806393920,
  "data": {
    "totalFollowerNum": "1",
    "currentFollowerNum": "1",
    "maxFollowerNum": "300",
    "tradingOrderNum": "20",
    "totalpl": "180.81650415",
    "gainNum": "9",
    "lossNum": "11",
    "totalEquity": "1002283.204381698640000000",
    "winRate": "10.00",
    "lastWeekRoiList": [
      {
        "rate": "14.08",
        "ctime": "1695139200000"
      },
      {
        "rate": "14.08",
        "ctime": "1695225600000"
      },
      {
        "rate": "16.84",
        "ctime": "1695312000000"
      },
      {
        "rate": "16.84",
        "ctime": "1695398400000"
      },
      {
        "rate": "16.84",
        "ctime": "1695484800000"
      },
      {
        "rate": "16.84",
        "ctime": "1695571200000"
      },
      {
        "rate": "16.84",
        "ctime": "1695657600000"
      },
      {
        "rate": "16.84",
        "ctime": "1695744000000"
      }
    ],
    "lastMonthRoiList": [
      {
        "rate": "0",
        "ctime": "1693152000000"
      },
      {
        "rate": "0",
        "ctime": "1693238400000"
      },
      {
        "rate": "0",
        "ctime": "1693324800000"
      },
      {
        "rate": "-0.06",
        "ctime": "1693411200000"
      },
      {
        "rate": "14.14",
        "ctime": "1693497600000"
      },
      {
        "rate": "14.14",
        "ctime": "1693584000000"
      },
      {
        "rate": "14.14",
        "ctime": "1693670400000"
      },
      {
        "rate": "14.08",
        "ctime": "1693756800000"
      },
      {
        "rate": "14.08",
        "ctime": "1693843200000"
      },
      {
        "rate": "14.08",
        "ctime": "1693929600000"
      },
      {
        "rate": "14.08",
        "ctime": "1694016000000"
      },
      {
        "rate": "14.08",
        "ctime": "1694102400000"
      },
      {
        "rate": "14.08",
        "ctime": "1694188800000"
      },
      {
        "rate": "14.08",
        "ctime": "1694275200000"
      },
      {
        "rate": "14.08",
        "ctime": "1694361600000"
      },
      {
        "rate": "14.08",
        "ctime": "1694448000000"
      },
      {
        "rate": "14.08",
        "ctime": "1694534400000"
      },
      {
        "rate": "14.08",
        "ctime": "1694620800000"
      },
      {
        "rate": "14.08",
        "ctime": "1694707200000"
      },
      {
        "rate": "14.08",
        "ctime": "1694793600000"
      },
      {
        "rate": "14.08",
        "ctime": "1694880000000"
      },
      {
        "rate": "14.08",
        "ctime": "1694966400000"
      },
      {
        "rate": "14.08",
        "ctime": "1695052800000"
      },
      {
        "rate": "14.08",
        "ctime": "1695139200000"
      },
      {
        "rate": "14.08",
        "ctime": "1695225600000"
      },
      {
        "rate": "16.84",
        "ctime": "1695312000000"
      },
      {
        "rate": "16.84",
        "ctime": "1695398400000"
      },
      {
        "rate": "16.84",
        "ctime": "1695484800000"
      },
      {
        "rate": "16.84",
        "ctime": "1695571200000"
      },
      {
        "rate": "16.84",
        "ctime": "1695657600000"
      },
      {
        "rate": "16.84",
        "ctime": "1695744000000"
      }
    ],
    "lastWeekProfitList": [
      {
        "amount": "156.403443",
        "ctime": "1695139200000"
      },
      {
        "amount": "156.403443",
        "ctime": "1695225600000"
      },
      {
        "amount": "187.067143",
        "ctime": "1695312000000"
      },
      {
        "amount": "187.067143",
        "ctime": "1695398400000"
      },
      {
        "amount": "187.067143",
        "ctime": "1695484800000"
      },
      {
        "amount": "187.067143",
        "ctime": "1695571200000"
      },
      {
        "amount": "180.816504",
        "ctime": "1695657600000"
      },
      {
        "amount": "180.816504",
        "ctime": "1695744000000"
      }
    ],
    "lastMonthProfitList": [
      {
        "amount": "-0.703906",
        "ctime": "1695139200000"
      },
      {
        "amount": "-0.703906",
        "ctime": "1695225600000"
      },
      {
        "amount": "187.067143",
        "ctime": "1695312000000"
      },
      {
        "amount": "187.067143",
        "ctime": "1695398400000"
      },
      {
        "amount": "187.067143",
        "ctime": "1695484800000"
      },
      {
        "amount": "187.067143",
        "ctime": "1695571200000"
      },
      {
        "amount": "180.816504",
        "ctime": "1695657600000"
      },
      {
        "amount": "180.816504",
        "ctime": "1695744000000"
      }
    ]
  }
}
```

## Get Unrealized Profit Sharing Details

`GET /api/v2/copy/spot-trader/profit-details`

Rate Limit: 5 req/sec/UID

Operation ID: `classicCopytradingSpotCopytradeTraderProfitDetails`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| coin | query | string |  | Settlement currency of profit share |
| pageNo | query | string |  | page no |
| pageSize | query | string |  | The number of queries <br><br>The default is 20, and the maximum supported is 50. |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].distributeRatio | string[] |  | Profit share ratio <br><br>If the value is 11.11, it represents 11.11% |
| data[].profit | string |  | PnL |
| data[].coin | string |  | Settlement currency |
| data[].followerName | string |  | Elite trader alias |

```json
{
  "code": "00000",
  "data": [
    {
      "distributeRatio": "11.11",
      "coin": "usdt",
      "profit": "0",
      "followerName": "bitget"
    }
  ],
  "msg": "success",
  "requestTime": 1627354109502
}
```

## Get History Profit Sharing Details

`GET /api/v2/copy/spot-trader/profit-history-details`

Rate Limit: 5 req/sec/UID

Operation ID: `classicCopytradingSpotCopytradeTraderProfitHistoryDetails`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| idLessThan | query | string |  | Request the paging content before this ID (older data), and the passed value is the endId of the corresponding interface. |
| idGreaterThan | query | string |  | Request the paging content after this ID (updated data). The value passed is the endId of the corresponding interface. |
| startTime | query | string |  | start time |
| endTime | query | string |  | end time |
| limit | query | string |  | Number of queries: Default 100, maximum 100 |
| coin | query | string |  | Profit sharing settlement currency |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.profitList | object[] |  | Profit share overview |
| data.profitList[].profitId | string |  | Profit share ID |
| data.profitList[].coin | string |  | Settlement currency |
| data.profitList[].distributeRatio | string |  | Profit share ratio <br><br>If the value is 11.11, it represents 11.11% |
| data.profitList[].profit | string |  | PnL |
| data.profitList[].followerName | string |  | Elite trader alias |
| data.profitList[].profitTime | string |  | Time to distribute profit share |
| data.endId | string |  | The last profit share ID.<br><br>This is used when idLessThan/idGreaterThan is set as the querying scope. |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695806800430,
  "data": {
    "endId": "4",
    "profitList": [
      {
        "profitId": "1",
        "coin": "USDT",
        "distributeRatio": "8",
        "profit": "2.40377986",
        "followerName": "xx1",
        "profitTime": "1695371100000"
      },
      {
        "profitId": "2",
        "coin": "USDT",
        "distributeRatio": "8",
        "profit": "0.00000000",
        "followerName": "xx2",
        "profitTime": "1693822200000"
      },
      {
        "profitId": "3",
        "coin": "USDT",
        "distributeRatio": "8",
        "profit": "0.01625000",
        "followerName": "xx3",
        "profitTime": "1693556100000"
      },
      {
        "profitId": "4",
        "coin": "USDT",
        "distributeRatio": "8",
        "profit": "2.16373741",
        "followerName": "xx4",
        "profitTime": "1693536000000"
      }
    ]
  }
}
```

## Get Profit Summary

`GET /api/v2/copy/spot-trader/profit-summarys`

Rate Limit: 5 req/sec/UID



Get basic information on traders' profits and a summary of historical profits.

Operation ID: `classicCopytradingSpotCopytradeTraderProfitSummarys`

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.profitSummarys | object |  | Elite trader profit share overview |
| data.profitSummarys.yesterdayProfit | string |  | Yesterday's profit share (elite traders) |
| data.profitSummarys.yesterdayTime | string |  | Yesterday's profit sharing time (milliseconds) |
| data.profitSummarys.sumProfit | string |  | Profit share in total |
| data.profitSummarys.waitProfit | string |  | To be shared |
| data.profitHistoryList | object[] |  | Profit list |
| data.profitHistoryList[].coin | string |  | Settlement currency<br><br>(in cryptocurrency) |
| data.profitHistoryList[].profitCount | string |  | Profit overview<br><br>(in cryptocurrency) |
| data.profitHistoryList[].lastProfitTime | string |  | The last time to distribute profit share (milliseconds)<br><br>(in cryptocurrency) |
| data.profitHistoryList[].historysByDateList | object[] |  | Historical profit share overview<br><br>(in the dimension of the cryptocurrency and the date) |
| data.profitHistoryList[].historysByDateList[].profit | string |  | PnL<br><br>(in the dimension of the cryptocurrency and the date) |
| data.profitHistoryList[].historysByDateList[].profitTime | string |  | Time to distribute profit share (milliseconds)<br><br>(in the dimension of the cryptocurrency and the date) |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695806592362,
  "data": {
    "profitSummarys": {
      "yesterdayProfit": "0",
      "yesterdayTime": "1695720000000",
      "sumProfit": "4.5837",
      "waitProfit": "0"
    },
    "profitHistoryList": [
      {
        "coin": "USDT",
        "profitCount": "4.58376728",
        "lastProfitTime": "1695371160000",
        "historysByDateList": [
          {
            "profit": "2.40377986",
            "profitTime": "1695371100000"
          },
          {
            "profit": "0.01625000",
            "profitTime": "1693556100000"
          },
          {
            "profit": "2.16373741",
            "profitTime": "1693536000000"
          }
        ]
      }
    ]
  }
}
```


---

经典账户 — 现货跟单带单员相关接口。

版本: 1.0.0

## 服务地址

- `https://api.bitget.com`

## 接口列表

- `GET /api/v2/copy/spot-trader/config-query-followers` — 我的跟随者列表
- `POST /api/v2/copy/spot-trader/config-remove-follower` — 移除跟随者
- `GET /api/v2/copy/spot-trader/order-current-track` — 获取当前带单
- `POST /api/v2/copy/spot-trader/order-modify-tpsl` — 修改止盈止损
- `GET /api/v2/copy/spot-trader/order-history-track` — 查询历史带单
- `POST /api/v2/copy/spot-trader/order-close-tracking` — 卖出和批量卖出
- `GET /api/v2/copy/spot-trader/order-total-detail` — 查看数据指标统计
- `GET /api/v2/copy/spot-trader/profit-summarys` — 交易员分润汇总
- `GET /api/v2/copy/spot-trader/profit-history-details` — 查看历史分润明细
- `GET /api/v2/copy/spot-trader/profit-details` — 查看待分润明细
- `GET /api/v2/copy/spot-trader/config-query-settings` — 交易员查询带单设置
- `POST /api/v2/copy/spot-trader/config-setting-symbols` — 带单币对设置

## 我的跟随者列表

`GET /api/v2/copy/spot-trader/config-query-followers`

限速规则: 10次/1s (uid)

Operation ID: `classicCopytradingSpotCopytradeTraderConfigQueryFollowers`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| pageNo | query | string |  | pageNo (default 1) |
| pageSize | query | string |  | pageSize(default 30 max 1000) |
| startTime | query | string |  | 开始时间戳 <br><br>Unix时间戳的毫秒数格式，如 1597026383085（时间跨度最大支持三个月，若不传结束时间，则默认结束时间为三个月。） |
| endTime | query | string |  | 结束时间戳 <br><br>Unix时间戳的毫秒数格式，如 1597026383085（时间跨度最大支持三个月，若不传开始时间，则默认开始时间为三个月。） |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].accountEquity | string |  | 账户权益值 |
| data[].isRemove | string |  | 能否移除跟单用户<br><br>yes 是;no 否 |
| data[].followerHeadPic | string |  | 跟随者头像 |
| data[].followerName | string |  | 跟随者昵称 |
| data[].followerUid | string |  | 跟随者用户id |
| data[].followerTime | string |  | 跟随日期（以初次跟随日期为准）<br><br>Unix时间戳的毫秒数格式，如 1597026383085 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695807814833,
  "data": [
    {
      "accountEquity": "1001711.2164",
      "isRemove": "NO",
      "followerHeadPic": null,
      "followerName": "BGU***1QK5",
      "followerUid": "*********",
      "followerTime": "1693533344295"
    }
  ]
}
```

## 移除跟随者

`POST /api/v2/copy/spot-trader/config-remove-follower`

限速规则: 1次/秒/UID

Operation ID: `classicCopytradingSpotCopytradeTraderConfigRemoveFollower`

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
| data | string |  | 结果<br><br>`00000` 成功<br><br>其它值 失败 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1656066841304,
  "data": ""
}
```

## 获取当前带单

`GET /api/v2/copy/spot-trader/order-current-track`

限速规则: 10次/1s (uid)

Operation ID: `classicCopytradingSpotCopytradeTraderOrderCurrentTrack`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string |  | 交易对 |
| idLessThan | query | string |  | 请求此ID之前 |
| idGreaterThan | query | string |  | 请求此ID之后 |
| startTime | query | string |  | 开始时间戳 |
| endTime | query | string |  | 结束时间戳 |
| limit | query | string |  | 默认20条，最大支持50条。超过将返回20条 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.trackingList | object[] |  | 带单集合 |
| data.trackingList[].trackingNo | string |  | 跟踪订单号 |
| data.trackingList[].orderId | string |  | 当前订单id |
| data.trackingList[].buyFillSize | string |  | 买入成交张数 |
| data.trackingList[].buyDelegateSize | string |  | 买入委托数量 |
| data.trackingList[].buyPrice | string |  | 买入价格 |
| data.trackingList[].unrealizedPL | string |  | 当前未实现盈亏收益 |
| data.trackingList[].buyTime | string |  | 买入时间 |
| data.trackingList[].buyFee | string |  | 买入手续费 |
| data.trackingList[].unrealizedPLR | string |  | 当前未实现盈亏收益率,若值为11.11，则代表11.11% |
| data.trackingList[].symbol | string |  | 交易对 |
| data.trackingList[].stopLossPrice | string |  | 止损价格 |
| data.trackingList[].stopSurplusPrice | string |  | 止盈价格 |
| data.trackingList[].followCount | string |  | 此笔订单跟单人数 |
| data.endId | string |  | 最后的数据id。id值为跟踪单号，用于根据id查询。 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695803899870,
  "data": {
    "endId": "1",
    "trackingList": [
      {
        "trackingNo": "1",
        "orderId": "1",
        "buyFillSize": "0.0317",
        "buyDelegateSize": "0.0317190800000000",
        "buyPrice": "34870.7",
        "unrealizedPL": "-0.79530295",
        "buyTime": "1695729894873",
        "buyFee": "-0.00001908",
        "unrealizedPLR": "-0.07",
        "symbol": "BTCUSDT",
        "stopLossPrice": null,
        "stopSurplusPrice": null,
        "followCount": "1"
      }
    ]
  }
}
```

## 修改止盈止损

`POST /api/v2/copy/spot-trader/order-modify-tpsl`

限速规则: 1次/秒/UID

Operation ID: `classicCopytradingSpotCopytradeTraderOrderModifyTpsl`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| trackingNo | string | 是 | 跟踪订单号 |
| stopSurplusPrice | string |  | 止盈价（为空时，不管存不存在止盈都忽略或不更新，为0时，若存在止盈则表示取消原有止盈。大于等于0时，则表示更新或设置止盈） |
| stopLossPrice | string |  | 止损价（为空时，不管存不存在止损都忽略或不更新，为0时，若存在止损则表示取消原有止损。大于等于0时，则表示更新或设置止损。） |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | string |  | 结果<br><br>`00000` 成功<br><br>其它值 失败 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1656066841304,
  "data": ""
}
```

## 查询历史带单

`GET /api/v2/copy/spot-trader/order-history-track`

限速规则: 5次/秒/UID

Operation ID: `classicCopytradingSpotCopytradeTraderOrderHistoryTrack`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| idLessThan | query | string |  | 请求此ID之前（更旧的数据）的分页内容，传的值为对应接口的 endId。 |
| idGreaterThan | query | string |  | 请求此ID之后（更新的数据）的分页内容，传的值为对应接口的 endId |
| startTime | query | string |  | 开始时间戳 <br><br>(跟单创建时间)<br><br>Unix时间戳的毫秒数格式，如 1597026383085<br><br>（时间跨度最大支持三个月，若不传结束时间，则默认结束时间为三个月。） |
| endTime | query | string |  | 结束时间戳 <br><br>(跟单创建时间)<br><br>Unix时间戳的毫秒数格式，如 1597026383085<br><br>（时间跨度最大支持三个月，若不传开始时间，则默认开始时间为三个月。） |
| limit | query | string |  | 查询条数 默认20，最大100 |
| symbol | query | string |  | 交易币对<br><br>支持大小写 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.trackingList | object[] |  | 带单记录集合 |
| data.trackingList[].trackingNo | string |  | 跟踪订单号 |
| data.trackingList[].fillSize | string |  | 成交数量 |
| data.trackingList[].buyPrice | string |  | 买入价格 |
| data.trackingList[].sellPrice | string |  | 卖出价格 |
| data.trackingList[].achievedPL | string |  | 已实现盈亏收益 |
| data.trackingList[].buyTime | string |  | 买入时间 |
| data.trackingList[].sellTime | string |  | 卖出时间 |
| data.trackingList[].buyFee | string |  | 买入手续费 |
| data.trackingList[].sellFee | string |  | 卖出手续费 |
| data.trackingList[].achievedPLR | string |  | 已实现盈亏收益率,若值为11.11，则代表11.11% |
| data.trackingList[].symbol | string |  | 交易对 |
| data.trackingList[].netProfit | string |  | 净收益（负数为亏损） |
| data.trackingList[].followCount | string |  | 此笔订单跟单人数 |
| data.endId | string |  | 最后的跟踪订单id。<br><br>指定idLessThan/idGreaterThan作为范围查询时以此为准。 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695805248324,
  "data": {
    "endId": "1",
    "trackingList": [
      {
        "trackingNo": "1",
        "fillSize": "0.0317",
        "buyPrice": "34869.2",
        "sellPrice": "34865.5",
        "achievedPL": "-0.78259",
        "buyTime": "1695728919902",
        "sellTime": "1695729885589",
        "buyFee": "-0.00001908",
        "sellFee": "-0.66314181",
        "achievedPLR": "-0.07",
        "symbol": "BTCUSDT",
        "netProfit": "-1.44573",
        "followCount": "1"
      }
    ]
  }
}
```

## 卖出和批量卖出

`POST /api/v2/copy/spot-trader/order-close-tracking`

限速规则: 1次/秒/UID

Operation ID: `classicCopytradingSpotCopytradeTraderOrderCloseTracking`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| trackingNoList | string[] | 是 | 按买入币对分组trackingNo<br><br>全部成功或全部失败，跟踪订单号，最大50个 |
| symbol | string | 是 | 交易对 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | string |  | 结果<br><br>`00000` 成功<br><br>其它值 失败 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1656066841304,
  "data": ""
}
```

## 查看数据指标统计

`GET /api/v2/copy/spot-trader/order-total-detail`

限速规则: 5次/秒/UID

Operation ID: `classicCopytradingSpotCopytradeTraderOrderTotalDetail`

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.totalFollowerNum | string |  | 累计跟随人数 |
| data.currentFollowerNum | string |  | 当前跟随人数 |
| data.maxFollowerNum | string |  | 交易员最大可跟随人数 |
| data.tradingOrderNum | string |  | 总开单数 |
| data.totalpl | string |  | 总收益<br><br>(USDT） |
| data.gainNum | string |  | 盈利比数 |
| data.lossNum | string |  | 亏损比数 |
| data.totalEquity | string |  | 总权益 |
| data.winRate | string |  | 胜率 |
| data.lastWeekRoiList | object[] |  | 近一周收益率 |
| data.lastWeekRoiList[].rate | string |  | 收益率 |
| data.lastWeekRoiList[].ctime | string |  | 时间 |
| data.lastMonthRoiList | object[] |  | 近30天收益率 |
| data.lastMonthRoiList[].rate | string |  | 收益率 |
| data.lastMonthRoiList[].ctime | string |  | 时间 |
| data.lastWeekProfitList | object[] |  | 近一周收益 |
| data.lastWeekProfitList[].amount | string |  | 收益, USDT |
| data.lastWeekProfitList[].ctime | string |  | 时间 |
| data.lastMonthProfitList | object[] |  | 近30天收益 |
| data.lastMonthProfitList[].amount | string |  | 收益, USDT |
| data.lastMonthProfitList[].ctime | string |  | 时间 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695806393920,
  "data": {
    "totalFollowerNum": "1",
    "currentFollowerNum": "1",
    "maxFollowerNum": "300",
    "tradingOrderNum": "20",
    "totalpl": "180.81650415",
    "gainNum": "9",
    "lossNum": "11",
    "totalEquity": "1002283.204381698640000000",
    "winRate": "10.00",
    "lastWeekRoiList": [
      {
        "rate": "14.08",
        "ctime": "1695139200000"
      },
      {
        "rate": "14.08",
        "ctime": "1695225600000"
      },
      {
        "rate": "16.84",
        "ctime": "1695312000000"
      },
      {
        "rate": "16.84",
        "ctime": "1695398400000"
      },
      {
        "rate": "16.84",
        "ctime": "1695484800000"
      },
      {
        "rate": "16.84",
        "ctime": "1695571200000"
      },
      {
        "rate": "16.84",
        "ctime": "1695657600000"
      },
      {
        "rate": "16.84",
        "ctime": "1695744000000"
      }
    ],
    "lastMonthRoiList": [
      {
        "rate": "0",
        "ctime": "1693152000000"
      },
      {
        "rate": "0",
        "ctime": "1693238400000"
      },
      {
        "rate": "0",
        "ctime": "1693324800000"
      },
      {
        "rate": "-0.06",
        "ctime": "1693411200000"
      },
      {
        "rate": "14.14",
        "ctime": "1693497600000"
      },
      {
        "rate": "14.14",
        "ctime": "1693584000000"
      },
      {
        "rate": "14.14",
        "ctime": "1693670400000"
      },
      {
        "rate": "14.08",
        "ctime": "1693756800000"
      },
      {
        "rate": "14.08",
        "ctime": "1693843200000"
      },
      {
        "rate": "14.08",
        "ctime": "1693929600000"
      },
      {
        "rate": "14.08",
        "ctime": "1694016000000"
      },
      {
        "rate": "14.08",
        "ctime": "1694102400000"
      },
      {
        "rate": "14.08",
        "ctime": "1694188800000"
      },
      {
        "rate": "14.08",
        "ctime": "1694275200000"
      },
      {
        "rate": "14.08",
        "ctime": "1694361600000"
      },
      {
        "rate": "14.08",
        "ctime": "1694448000000"
      },
      {
        "rate": "14.08",
        "ctime": "1694534400000"
      },
      {
        "rate": "14.08",
        "ctime": "1694620800000"
      },
      {
        "rate": "14.08",
        "ctime": "1694707200000"
      },
      {
        "rate": "14.08",
        "ctime": "1694793600000"
      },
      {
        "rate": "14.08",
        "ctime": "1694880000000"
      },
      {
        "rate": "14.08",
        "ctime": "1694966400000"
      },
      {
        "rate": "14.08",
        "ctime": "1695052800000"
      },
      {
        "rate": "14.08",
        "ctime": "1695139200000"
      },
      {
        "rate": "14.08",
        "ctime": "1695225600000"
      },
      {
        "rate": "16.84",
        "ctime": "1695312000000"
      },
      {
        "rate": "16.84",
        "ctime": "1695398400000"
      },
      {
        "rate": "16.84",
        "ctime": "1695484800000"
      },
      {
        "rate": "16.84",
        "ctime": "1695571200000"
      },
      {
        "rate": "16.84",
        "ctime": "1695657600000"
      },
      {
        "rate": "16.84",
        "ctime": "1695744000000"
      }
    ],
    "lastWeekProfitList": [
      {
        "amount": "156.403443",
        "ctime": "1695139200000"
      },
      {
        "amount": "156.403443",
        "ctime": "1695225600000"
      },
      {
        "amount": "187.067143",
        "ctime": "1695312000000"
      },
      {
        "amount": "187.067143",
        "ctime": "1695398400000"
      },
      {
        "amount": "187.067143",
        "ctime": "1695484800000"
      },
      {
        "amount": "187.067143",
        "ctime": "1695571200000"
      },
      {
        "amount": "180.816504",
        "ctime": "1695657600000"
      },
      {
        "amount": "180.816504",
        "ctime": "1695744000000"
      }
    ],
    "lastMonthProfitList": [
      {
        "amount": "-0.703906",
        "ctime": "1695139200000"
      },
      {
        "amount": "-0.703906",
        "ctime": "1695225600000"
      },
      {
        "amount": "187.067143",
        "ctime": "1695312000000"
      },
      {
        "amount": "187.067143",
        "ctime": "1695398400000"
      },
      {
        "amount": "187.067143",
        "ctime": "1695484800000"
      },
      {
        "amount": "187.067143",
        "ctime": "1695571200000"
      },
      {
        "amount": "180.816504",
        "ctime": "1695657600000"
      },
      {
        "amount": "180.816504",
        "ctime": "1695744000000"
      }
    ]
  }
}
```

## 交易员分润汇总

`GET /api/v2/copy/spot-trader/profit-summarys`

限速规则: 5次/秒/UID



获取交易员分润基础信息和历史分润概览汇总。

Operation ID: `classicCopytradingSpotCopytradeTraderProfitSummarys`

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.profitSummarys | object |  | 交易员分润汇总信息 |
| data.profitSummarys.yesterdayProfit | string |  | 昨日分润(交易员) |
| data.profitSummarys.yesterdayTime | string |  | 昨日分润时间(毫秒) |
| data.profitSummarys.sumProfit | string |  | 累计分润 |
| data.profitSummarys.waitProfit | string |  | 待分润 |
| data.profitHistoryList | object[] |  | 分润列表 |
| data.profitHistoryList[].coin | string |  | 结算币种<br><br>（以币种为维度） |
| data.profitHistoryList[].profitCount | string |  | 收益汇总<br><br>（以币种为维度） |
| data.profitHistoryList[].lastProfitTime | string |  | 最后分润时间（毫秒）<br><br>（以币种为维度） |
| data.profitHistoryList[].historysByDateList | object[] |  | 历史分润汇总<br><br>（以该币种日期为维度） |
| data.profitHistoryList[].historysByDateList[].profit | string |  | 收益<br><br>（以该币种日期为维度） |
| data.profitHistoryList[].historysByDateList[].profitTime | string |  | 分润时间(毫秒)<br><br>（以该币种日期为维度） |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695806592362,
  "data": {
    "profitSummarys": {
      "yesterdayProfit": "0",
      "yesterdayTime": "1695720000000",
      "sumProfit": "4.5837",
      "waitProfit": "0"
    },
    "profitHistoryList": [
      {
        "coin": "USDT",
        "profitCount": "4.58376728",
        "lastProfitTime": "1695371160000",
        "historysByDateList": [
          {
            "profit": "2.40377986",
            "profitTime": "1695371100000"
          },
          {
            "profit": "0.01625000",
            "profitTime": "1693556100000"
          },
          {
            "profit": "2.16373741",
            "profitTime": "1693536000000"
          }
        ]
      }
    ]
  }
}
```

## 查看历史分润明细

`GET /api/v2/copy/spot-trader/profit-history-details`

限速规则: 5次/秒/UID

Operation ID: `classicCopytradingSpotCopytradeTraderProfitHistoryDetails`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| idLessThan | query | string |  | 请求此ID之前（更旧的数据）的分页内容，传的值为对应接口的 endId。 |
| idGreaterThan | query | string |  | 请求此ID之后（更新的数据）的分页内容，传的值为对应接口的 endId |
| startTime | query | string |  | 开始时间戳 <br><br>Unix时间戳的毫秒数格式，如 1597026383085<br><br>（时间跨度最大支持三个月，若不传结束时间，则默认结束时间为三个月。） |
| endTime | query | string |  | 结束时间戳 <br><br>Unix时间戳的毫秒数格式，如 1597026383085<br><br>（时间跨度最大支持三个月，若不传开始时间，则默认开始时间为三个月。） |
| limit | query | string |  | 查询条数 默认100，最大100 |
| coin | query | string |  | 分润结算币种 |

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
| data.profitList[].distributeRatio | string |  | 分润比例 <br><br>如为11.11 则代表为11.11% |
| data.profitList[].profit | string |  | 收益 |
| data.profitList[].followerName | string |  | 跟单员昵称 |
| data.profitList[].profitTime | string |  | 分润时间 |
| data.endId | string |  | 最后的跟分润id。<br><br>指定idLessThan/idGreaterThan作为范围查询时以此为准。 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695806800430,
  "data": {
    "endId": "2",
    "profitList": [
      {
        "profitId": "1",
        "coin": "USDT",
        "distributeRatio": "8",
        "profit": "2.40377986",
        "followerName": "xx1",
        "profitTime": "1695371100000"
      },
      {
        "profitId": "2",
        "coin": "USDT",
        "distributeRatio": "8",
        "profit": "0.00000000",
        "followerName": "xx2",
        "profitTime": "1693822200000"
      },
      {
        "profitId": "3",
        "coin": "USDT",
        "distributeRatio": "8",
        "profit": "0.01625000",
        "followerName": "xx3",
        "profitTime": "1693556100000"
      },
      {
        "profitId": "4",
        "coin": "USDT",
        "distributeRatio": "8",
        "profit": "2.16373741",
        "followerName": "xx4",
        "profitTime": "1693536000000"
      }
    ]
  }
}
```

## 查看待分润明细

`GET /api/v2/copy/spot-trader/profit-details`

限速规则: 5次/秒/UID

Operation ID: `classicCopytradingSpotCopytradeTraderProfitDetails`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| coin | query | string |  | 分润结算币种 |
| pageNo | query | string |  | 当前页号<br><br>默认为1. |
| pageSize | query | string |  | 查询数量  <br><br>默认为20条，最大支持50条。 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].distributeRatio | string[] |  | 分润比例 <br><br>如为11.11 则代表为11.11% |
| data[].profit | string |  | 收益 |
| data[].coin | string |  | 结算币种 |
| data[].followerName | string |  | 跟单员昵称 |

```json
{
  "code": "00000",
  "data": [
    {
      "distributeRatio": "11.11",
      "coin": "usdt",
      "profit": "0",
      "followerName": "bitget"
    }
  ],
  "msg": "success",
  "requestTime": 1627354109502
}
```

## 交易员查询带单设置

`GET /api/v2/copy/spot-trader/config-query-settings`

限速规则: 5次/秒/UID

Operation ID: `classicCopytradingSpotCopytradeTraderConfigQuerySettings`

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.removeLimitUsdt | string |  | 可以移除跟随者资产上限。<br><br>（小于该值的跟随者能够被移除） |
| data.spotInfoList | object[] |  | 带单额度集合 |
| data.spotInfoList[].maxQuoteSize | string |  | 单次最大带单额度（计价币） |
| data.spotInfoList[].surplusQuoteSize | string |  | 剩余额度（计价币） |
| data.spotInfoList[].symbol | string |  | 币对名称 |
| data.labelList | object[] |  | 标签集合 |
| data.labelList[].id | string |  | 标签id |
| data.labelList[].name | string |  | 标签名称 |
| data.enable | string |  | 是否开启带单<br><br>yes 开启；no 关闭 |
| data.showAssetsMap | string |  | 是否展示构成资产图表<br><br>yes 开启；no 关闭 |
| data.showEquity | string |  | 是否展示总资金<br><br>yes 开启；no 关闭 |
| data.traceSymbolList | object[] |  | 带单币对集合 |
| data.traceSymbolList[].enable | string |  | 这个币对是否开启带单<br><br>yes 开启；no 关闭 |
| data.traceSymbolList[].symbol | string |  | 交易币对 |
| data.traceSymbolList[].minOpenCount | string |  | 交易员最小开单数量 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695807020372,
  "data": {
    "removeLimitUsdt": "100",
    "spotInfoList": [
      {
        "maxQuoteSize": "5000000",
        "surplusQuoteSize": "4998894.59",
        "symbol": "BTCUSDT"
      },
      {
        "maxQuoteSize": "300000",
        "surplusQuoteSize": "300000",
        "symbol": "ETHBTC"
      },
      {
        "maxQuoteSize": "50000",
        "surplusQuoteSize": "50000",
        "symbol": "ETHUSDT"
      }
    ],
    "labelList": [],
    "enable": "YES",
    "showAssetsMap": "NO",
    "showEquity": "NO",
    "traceSymbolList": [
      {
        "enable": "NO",
        "symbol": "BGBUSDT",
        "minOpenCount": "0.0001"
      },
      {
        "enable": "YES",
        "symbol": "BTCUSDT",
        "minOpenCount": "0.0005"
      },
      {
        "enable": "YES",
        "symbol": "ETHBTC",
        "minOpenCount": "0.0001"
      },
      {
        "enable": "YES",
        "symbol": "ETHUSDT",
        "minOpenCount": "0.0001"
      }
    ]
  }
}
```

## 带单币对设置

`POST /api/v2/copy/spot-trader/config-setting-symbols`

限速规则: 1次/秒/UID

Operation ID: `classicCopytradingSpotCopytradeTraderConfigSettingSymbols`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| symbolList | string[] | 是 | 带单币对集合<br><br>最大50个 |
| settingType | string | 是 | 设置类型<br><br>add 新增;<br><br>delete 删除； |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | string |  | 结果<br><br>`00000` 成功<br><br>其它值 失败 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1656066841304,
  "data": ""
}
```