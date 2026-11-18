---
exchange: bitget
source_url: https://www.bitget.com/docs/catalog/copy-trading
api_type: REST
updated_at: 2026-11-18 19:01:26.097649
---

# Copy Trading

Futures copy-trading APIs: lead trader (public/private) and follower (public) endpoints.

版本: 1.0.0

## 服务地址

- `https://api.bitget.com`

## 接口列表

- `GET /api/v3/copy/futures/position-summary` — Get Position Summary
- `GET /api/v3/copy/futures/trading-pairs` — Get Trading Pairs
- `GET /api/v3/copy/futures/max-transferable` — Get Max Transferable
- `POST /api/v3/copy/futures/transfer` — Transfer
- `GET /api/v3/copy/futures/transfer-record` — Get Transfer Record
- `GET /api/v3/copy/futures/current-follower` — Get Current Followers
- `GET /api/v3/copy/futures/history-follower` — Get History Followers
- `GET /api/v3/copy/futures/profit-summary` — Get Profit Summary
- `GET /api/v3/copy/futures/profit-details` — Get Profit Details
- `GET /api/v3/copy/futures/portfolio-overview` — Get Portfolio Overview
- `POST /api/v3/copy/futures/follower-settings` — Create Copy
- `POST /api/v3/copy/futures/modify-follower-settings` — Modify Follower Settings
- `POST /api/v3/copy/futures/unfollow` — Unfollow
- `GET /api/v3/copy/futures/copy-settings` — Get Copy Settings
- `GET /api/v3/copy/futures/copy-max-transferable` — Get Copy Max Transferable
- `POST /api/v3/copy/futures/copy-transfer` — Copy Transfer
- `GET /api/v3/copy/futures/copy-transfer-record` — Get Copy Transfer Record
- `GET /api/v3/copy/futures/current-copy` — Get Current Copy
- `GET /api/v3/copy/futures/copy-profit-details` — Get Copy Profit Details
- `POST /api/v3/copy/futures/close-positions` — Close Positions
- `POST /api/v3/copy/futures/close-all` — Close All
- `GET /api/v3/copy/futures/current-positions` — Get Current Positions
- `POST /api/v3/copy/futures/place-tpsl` — Place TPSL
- `POST /api/v3/copy/futures/modify-tpsl` — Modify TPSL
- `POST /api/v3/copy/futures/cancel-tpsl` — Cancel TPSL
- `GET /api/v3/copy/futures/current-tpsl-orders` — Get Current TPSL Orders
- `GET /api/v3/copy/futures/tpsl-order-history` — Get TPSL Order History

## Get Position Summary

`GET /api/v3/copy/futures/position-summary`

Rate limit: 5/sec/UID

Permission: Unified Account — Futures Copy-Trading Positions — Read-only

Get position summary

Operation ID: `copyTradingPublicPrivateGetPositionSummary`

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].unrealizedPnl | string |  | Unrealized PnL<br><br>unit: USDT |
| data[].realizedPnl | string |  | Realized PnL<br><br>unit: USDT |
| data[].holdSize | string |  | Position size |
| data[].avgPrice | string |  | Average entry price |
| data[].symbol | string |  | Symbol name |
| data[].leverage | string |  | Leverage multiplier<br><br>positive integer |
| data[].marginMode | string |  | Margin mode:<br><br>`isolated` isolated<br><br>`cross` cross |
| data[].liqPrice | string |  | Liquidation price |
| data[].margin | string |  | Margin |
| data[].holdSide | string |  | Position side:<br><br>`long` long<br><br>`short` short |
| data[].roi | string |  | Return on investment (ROI) |
| data[].markPrice | string |  | Mark price |
| data[].positionValue | string |  | Position value<br><br>unit: USDT |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1774957537393,
  "data": [
    {
      "unrealizedPnl": "0.0095",
      "realizedPnl": "-0.0085658580000000",
      "holdSize": "0.01",
      "avgPrice": "2039.49",
      "symbol": "ETHUSDT",
      "leverage": "10",
      "marginMode": "crossed",
      "liqPrice": "0",
      "margin": "2.04900984",
      "holdSide": "long",
      "roi": "0.0046363857202896",
      "markPrice": "2040.44",
      "positionValue": "20.4044"
    }
  ]
}
```

## Get Trading Pairs

`GET /api/v3/copy/futures/trading-pairs`

Rate limit: 5/sec/UID

Permission: Unified Account — Futures Copy-Trading Orders — Read-only

Get copy-trading symbol

Operation ID: `copyTradingPublicPrivateGetTradingPairs`

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].symbol | string |  | Symbol name |
| data[].leverage | string |  | Leverage multiplier |
| data[].marginDetails | object[] |  | Margin details list |
| data[].marginDetails[].marginCoin | string |  | Margin currency<br><br>e.g., `USDT` |
| data[].marginDetails[].maxLongCount | string |  | Maximum long position size |
| data[].marginDetails[].remainingLongCount | string |  | Remaining long position size |
| data[].marginDetails[].maxShortCount | string |  | Maximum short position size |
| data[].marginDetails[].remainingShortCount | string |  | Remaining short position size |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1774957070136,
  "data": [
    {
      "symbol": "ADAUSDT",
      "leverage": "50",
      "marginDetails": [
        {
          "marginCoin": "USDT",
          "maxLongCount": "9600000",
          "remainingLongCount": "9600000",
          "maxShortCount": "9600000",
          "remainingShortCount": "9600000"
        }
      ]
    }
  ]
}
```

## Get Max Transferable

`GET /api/v3/copy/futures/max-transferable`

Rate limit: 1/sec/UID

Permission: Unified Account — Futures Copy-Trading Orders — Read-only

Get the maximum transferable amount and available balance for a copy-trading lead account.

Operation ID: `copyTradingPublicPrivateGetMaxTransferable`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| coin | query | string | 是 | Coin name, e.g. `USDT` |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.maxTransferable | string |  | Maximum transferable amount |
| data.available | string |  | Available balance |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": {
    "maxTransferable": "1000.00",
    "available": "1200.00"
  }
}
```

## Transfer

`POST /api/v3/copy/futures/transfer`

Rate limit: 1/sec/UID

Permission: Unified Account — Futures Copy-Trading Orders — Read-write

Transfer funds into or out of a copy-trading lead account. Only transfers between the spot/funding account and the lead account are supported.

Operation ID: `copyTradingPublicPrivateTransfer`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| type | string | 是 | Transfer direction<br><br>`in` Transfer in (spot/funding account -> lead account)<br><br>`out` Transfer out (lead account -> spot/funding account) |
| inAccountType | string |  | Source account type for transfer-in. Multiple types supported, separated by commas (`,`).<br><br>`funding` Spot/funding account<br><br>`uta` Unified account<br><br>`otc` OTC account<br><br>If not specified, all account types are selected by default.<br><br>Deduction order: funding account -> OTC account -> unified account.<br><br>Classic account mode only supports `funding` (spot account) as the source. |
| coin | string | 是 | Transfer coin |
| amount | string | 是 | Transfer amount |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.transferId | string |  | Transfer ID |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": {
    "transferId": "1234567890"
  }
}
```

## Get Transfer Record

`GET /api/v3/copy/futures/transfer-record`

Rate limit: 1/sec/UID

Permission: Unified Account — Futures Copy-Trading Orders — Read-only

Query transfer history for a copy-trading lead account.

Operation ID: `copyTradingPublicPrivateGetTransferRecord`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| startTime | query | string |  | Start timestamp (Unix ms, e.g. `1597026383085`) |
| endTime | query | string |  | End timestamp (Unix ms, e.g. `1597026383085`) |
| limit | query | string |  | Number of results. Default: `20`, max: `100` |
| cursor | query | string |  | Cursor ID. Pass the `nextCursor` returned from the previous call to paginate forward (newer records). |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.list | object[] |  | Transfer record list |
| data.list[].transferId | string |  | Transfer order ID |
| data.list[].fromType | string |  | Source account type. Multiple values may be returned, separated by commas.<br><br>`spot` Spot/funding account<br><br>`uta` Unified account<br><br>`otc` OTC account<br><br>`lead` Lead account |
| data.list[].toType | string |  | Destination account type. Multiple values may be returned, separated by commas.<br><br>`spot` Spot/funding account<br><br>`uta` Unified account<br><br>`otc` OTC account<br><br>`lead` Lead account |
| data.list[].amount | string |  | Transfer amount |
| data.list[].coin | string |  | Transfer coin |
| data.list[].status | string |  | Transfer status<br><br>`Successful` Success<br><br>`Failed` Failed<br><br>`Processing` Processing |
| data.list[].createdTime | string |  | Transfer creation time (Unix ms) |
| data.nextCursor | string |  | Next page cursor |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": {
    "list": [
      {
        "transferId": "1234567890",
        "fromType": "spot,uta",
        "toType": "lead",
        "amount": "100.00",
        "coin": "USDT",
        "status": "Successful",
        "createdTime": "1740000000000"
      }
    ],
    "nextCursor": "1234567890"
  }
}
```

## Get Current Followers

`GET /api/v3/copy/futures/current-follower`

Rate limit: 1/sec/UID

Permission: Unified Account — Futures Copy-Trading Orders — Read-only

Get the list of current active followers for a copy-trading lead account.

Operation ID: `copyTradingPublicPrivateGetCurrentFollowers`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| limit | query | string |  | Number of results. Default: `20`, max: `100` |
| cursor | query | string |  | Cursor ID. Pass the `nextCursor` returned from the previous call to paginate forward (newer records). |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.list | object[] |  | Follower list |
| data.list[].followerName | string |  | Follower nickname |
| data.list[].estimateAssets | string |  | Estimated asset value (USDT) |
| data.list[].totalProfit | string |  | Total profit (USDT) |
| data.list[].totalShareProfit | string |  | Total profit share (USDT) |
| data.list[].totalInvestment | string |  | Total investment (USDT) |
| data.list[].canRemove | string |  | Whether the follower can be removed<br><br>`yes` Yes<br><br>`no` No |
| data.list[].followDays | string |  | Number of days following (positive integer) |
| data.list[].totalAssets | string |  | Account equity (USDT) |
| data.list[].startTime | string |  | Follow start time (Unix ms) |
| data.nextCursor | string |  | Next page cursor |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": {
    "list": [
      {
        "followerName": "Alice",
        "estimateAssets": "10000.00",
        "totalProfit": "500.00",
        "totalShareProfit": "50.00",
        "totalInvestment": "9500.00",
        "canRemove": "no",
        "followDays": "30",
        "totalAssets": "10500.00",
        "startTime": "1740000000000"
      }
    ],
    "nextCursor": "1234567890"
  }
}
```

## Get History Followers

`GET /api/v3/copy/futures/history-follower`

Rate limit: 1/sec/UID

Permission: Unified Account — Futures Copy-Trading Orders — Read-only

Get the list of historical followers for a copy-trading lead account.

Operation ID: `copyTradingPublicPrivateGetHistoryFollowers`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| limit | query | string |  | Number of results. Default: `20`, max: `100` |
| cursor | query | string |  | Cursor ID. Pass the `nextCursor` returned from the previous call to paginate forward (newer records). |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.list | object[] |  | Historical follower list |
| data.list[].followerName | string |  | Follower nickname |
| data.list[].totalProfit | string |  | Total profit (USDT) |
| data.list[].totalShareProfit | string |  | Total profit share (USDT) |
| data.list[].totalInvestment | string |  | Total investment (USDT) |
| data.list[].startTime | string |  | Follow start time (Unix ms) |
| data.list[].endTime | string |  | Follow end time (Unix ms) |
| data.nextCursor | string |  | Next page cursor |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": {
    "list": [
      {
        "followerName": "Bob",
        "totalProfit": "200.00",
        "totalShareProfit": "20.00",
        "totalInvestment": "5000.00",
        "startTime": "1730000000000",
        "endTime": "1740000000000"
      }
    ],
    "nextCursor": "1234567890"
  }
}
```

## Get Profit Summary

`GET /api/v3/copy/futures/profit-summary`

Rate limit: 1/sec/UID

Permission: Unified Account — Futures Copy-Trading Orders — Read-only

Get the profit-sharing summary for a copy-trading lead account.

Operation ID: `copyTradingPublicPrivateGetProfitSummary`

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.totalProfit | string |  | Cumulative profit (USDT) |
| data.totalAllocatedProfit | string |  | Cumulative allocated profit share (USDT) |
| data.totalPendingProfit | string |  | Cumulative pending profit share (USDT) |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": {
    "totalProfit": "10000.00",
    "totalAllocatedProfit": "8000.00",
    "totalPendingProfit": "2000.00"
  }
}
```

## Get Profit Details

`GET /api/v3/copy/futures/profit-details`

Rate limit: 1/sec/UID

Permission: Unified Account — Futures Copy-Trading Orders — Read-only

Get the profit-sharing detail records for a copy-trading lead account.

Operation ID: `copyTradingPublicPrivateGetProfitDetails`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| startTime | query | string |  | Start timestamp (Unix ms, e.g. `1597026383085`) |
| endTime | query | string |  | End timestamp (Unix ms, e.g. `1597026383085`) |
| limit | query | string |  | Number of results. Default: `20`, max: `100` |
| cursor | query | string |  | Cursor ID. Pass the `nextCursor` returned from the previous call to paginate forward (newer records). |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.list | object[] |  | Profit detail list |
| data.list[].followerName | string |  | Follower name |
| data.list[].profit | string |  | Follower's profit and loss |
| data.list[].allocatedPnl | string |  | Allocated profit and loss |
| data.list[].pendingPnl | string |  | Pending profit and loss |
| data.list[].shareRatio | string |  | Profit-sharing ratio (decimal form) |
| data.list[].shareProfit | string |  | Profit-sharing amount |
| data.list[].reason | string |  | Reason<br><br>`period` Periodic settlement<br><br>`unfollow` Settlement upon unfollow |
| data.list[].settleTime | string |  | Settlement time (Unix ms) |
| data.nextCursor | string |  | Cursor ID |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": {
    "list": [
      {
        "followerName": "Alice",
        "profit": "500.00",
        "allocatedPnl": "400.00",
        "pendingPnl": "100.00",
        "shareRatio": "0.1",
        "shareProfit": "50.00",
        "reason": "period",
        "settleTime": "1740000000000"
      }
    ],
    "nextCursor": "1234567890"
  }
}
```

## Get Portfolio Overview

`GET /api/v3/copy/futures/portfolio-overview`

Rate limit: 1/sec/UID

Permission: Unified Account — Futures Copy-Trading Orders — Read-only

Get a portfolio overview of the lead trading project.

Operation ID: `copyTradingPublicPrivateGetPortfolioOverview`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| period | query | string | 是 | 7D/30D/90D/180D |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.projectId | string |  | Project ID |
| data.asset | string |  | Assets under management |
| data.roi | string |  | Return on investment |
| data.totalProfit | string |  | Total profit |
| data.followerProfit | string |  | Follower profit |
| data.maxDrawdown | string |  | Maximum drawdown |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": {
    "projectId": "1234567890",
    "asset": "10000.00",
    "roi": "0.15",
    "totalProfit": "1500.00",
    "followerProfit": "1200.00",
    "maxDrawdown": "0.05"
  }
}
```

## Create Copy

`POST /api/v3/copy/futures/follower-settings`

Rate limit: 1/sec/UID

Permission: Unified Account — Trade — Read-write

Create a copy trading subscription for a lead trading project.

Operation ID: `copyTradingFollowerCreateCopy`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| projectId | string | 是 | Project ID |
| accountType | string |  | Account type for auto fund transfer. Multiple values separated by commas (`,`).<br><br>`funding` Spot/funding account<br><br>`uta` Unified account<br><br>`otc` OTC account<br><br>If not specified, all account types are selected by default.<br><br>Deduction order: funding account → OTC account → unified account. |
| type | string | 是 | Copy type<br><br>`fixed_ratio` Fixed ratio: each order is placed proportionally based on the ratio of the lead trader's order margin to their account equity.<br><br>`fixed_margin` Fixed margin: each order uses a fixed margin amount. |
| amount | string | 是 | Copy amount in USDT. Minimum: 50. |
| tradingPairList | string |  | List of trading pairs to copy. If not specified, all pairs are copied. If the lead trader trades a pair outside your selected list, no order will be placed. |
| marginPerOrder | string |  | Margin per order in USDT. Required when `type` is `fixed_margin`. |
| autoCopy | string |  | Auto-follow new trading pairs.<br><br>`on` Auto-follow (default)<br><br>`off` Do not auto-follow |
| leverage | string |  | Leverage multiplier. If not specified, follows the lead trader's leverage. Range: [1, 10]. |
| maxEntrySlippage | string |  | Maximum entry slippage. If not specified, the system default applies. Range: [0.1, 3]. For example, 0.1 represents 0.1%. |
| maxMarginRatio | string |  | Maximum single-order margin ratio. Range: [5, 95]. For example, 5 represents 5%. When the margin for a single futures order exceeds this percentage of total assets, the order is placed using the maximum ratio. |
| maxPostionValue | string |  | Maximum total position value in USDT. Default and maximum: 2,000,000. When the total position value reaches this limit, no new copy orders will be placed. |

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
  "requestTime": 1740000000000.0,
  "data": "success"
}
```

## Modify Follower Settings

`POST /api/v3/copy/futures/modify-follower-settings`

Rate limit: 1/sec/UID

Permission: Unified Account — Trade — Read-write

Modify the settings for an existing copy trading subscription.

Operation ID: `copyTradingFollowerModifySettings`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| projectId | string | 是 | Project ID |
| tradingPairList | string |  | List of trading pairs. Pass `all` to follow all pairs. |
| marginPerOrder | string |  | Margin per order in USDT. |
| autoCopy | string |  | Auto-follow new trading pairs.<br><br>`on` Auto-follow<br><br>`off` Do not auto-follow |
| leverage | string |  | Leverage multiplier. Range: [1, 10]. Can only be modified when there are no open positions. |
| maxEntrySlippage | string |  | Maximum entry slippage. Range: [0.1, 3]. 0.1 represents 0.1%. |
| maxMarginRatio | string |  | Maximum single-order margin ratio. Range: [5, 95]. |
| maxPostionValue | string |  | Maximum total position value in USDT. Maximum: 2,000,000. |

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
  "requestTime": 1740000000000.0,
  "data": "success"
}
```

## Unfollow

`POST /api/v3/copy/futures/unfollow`

Rate limit: 1/sec/UID

Permission: Unified Account — Trade — Read-write

Cancel a copy trading subscription.

Operation ID: `copyTradingFollowerUnfollow`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| projectId | string | 是 | Project ID |
| closeType | string |  | Close type when unfollowing.<br><br>`follow_close` Follow the lead trader to close positions<br><br>`instant_close` Close positions immediately |

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
  "requestTime": 1740000000000.0,
  "data": "success"
}
```

## Get Copy Settings

`GET /api/v3/copy/futures/copy-settings`

Rate limit: 5/sec/UID

Permission: Unified Account — Trade — Read-only

Query the copy trading settings for a project.

Operation ID: `copyTradingFollowerGetCopySettings`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| projectId | query | string | 是 | Project ID |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.type | string |  | Copy type<br><br>`fixed_ratio` Fixed ratio<br><br>`fixed_margin` Fixed margin |
| data.amount | string |  | Copy amount in USDT |
| data.tradingPairList | string[] |  | List of copy trading pairs |
| data.marginPerOrder | string |  | Margin per order in USDT |
| data.autoCopy | string |  | Auto-follow setting<br><br>`on` Auto-follow<br><br>`off` Do not auto-follow |
| data.leverage | string |  | Leverage multiplier. Returns empty if following the lead trader's leverage. |
| data.maxEntrySlippage | string |  | Maximum entry slippage. Returned as a percentage, e.g. 1 represents 1%. |
| data.maxMarginRatio | string |  | Maximum single-order margin ratio. Returned as a percentage, e.g. 90 represents 90%. |
| data.maxPostionValue | string |  | Maximum total position value |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": {
    "type": "fixed_ratio",
    "amount": "1000.00",
    "tradingPairList": [
      "BTCUSDT",
      "ETHUSDT"
    ],
    "marginPerOrder": "",
    "autoCopy": "on",
    "leverage": "",
    "maxEntrySlippage": "1",
    "maxMarginRatio": "90",
    "maxPostionValue": "2000000"
  }
}
```

## Get Copy Max Transferable

`GET /api/v3/copy/futures/copy-max-transferable`

Rate limit: 1/sec/UID

Permission: Unified Account — Management — Read-only

Get the maximum transferable amount of the copy trading account for a specified coin.

Operation ID: `copyTradingFollowerGetCopyMaxTransferable`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| projectId | query | string | 是 | Project ID |
| coin | query | string | 是 | Coin name, e.g. `USDT` |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.maxTransferable | string |  | Maximum transferable amount |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": {
    "maxTransferable": "1000.00"
  }
}
```

## Copy Transfer

`POST /api/v3/copy/futures/copy-transfer`

Rate limit: 1/sec/UID

Permission: Unified Account — Management — Read-write

Transfer funds into or out of the copy trading account.

Operation ID: `copyTradingFollowerCopyTransfer`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| projectId | string | 是 | Project ID |
| type | string | 是 | Transfer direction<br><br>`in` Transfer in<br><br>`out` Transfer out. Only transfers to the spot/funding account are supported. |
| inAccountType | string |  | Source account type for transfer-in. Multiple values separated by commas.<br><br>`funding` Spot/funding account<br><br>`uta` Unified account<br><br>`otc` OTC account<br><br>If not specified, all account types are selected. Deduction order: funding account → OTC account → unified account. |
| coin | string | 是 | Transfer coin |
| amount | string | 是 | Transfer amount |

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
  "requestTime": 1740000000000.0,
  "data": "success"
}
```

## Get Copy Transfer Record

`GET /api/v3/copy/futures/copy-transfer-record`

Rate limit: 1/sec/UID

Permission: Unified Account — Management — Read-only

Query the transfer history for the copy trading account.

Operation ID: `copyTradingFollowerGetCopyTransferRecord`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| projectId | query | string | 是 | Project ID |
| limit | query | string |  | Number of results. Default: 20, max: 100. |
| cursor | query | string |  | Cursor ID. Pass the `nextCursor` from the previous response to paginate. |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.list | object[] |  | Transfer records |
| data.list[].fromType | string |  | Source account type<br><br>`funding` Spot/funding account<br><br>`uta` Unified account<br><br>`otc` OTC account<br><br>`copy` Copy trading account |
| data.list[].toType | string |  | Destination account type<br><br>`funding` Spot/funding account<br><br>`uta` Unified account<br><br>`otc` OTC account<br><br>`copy` Copy trading account |
| data.list[].amount | string |  | Transfer amount |
| data.list[].coin | string |  | Transfer coin |
| data.list[].status | string |  | Transfer status<br><br>`successful` Success<br><br>`failed` Failed<br><br>`processing` Processing |
| data.list[].createdTime | string |  | Transfer creation time (Unix ms) |
| data.nextCursor | string |  | Cursor ID for next page |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": {
    "list": [
      {
        "fromType": "funding",
        "toType": "copy",
        "amount": "500.00",
        "coin": "USDT",
        "status": "successful",
        "createdTime": "1740000000000"
      }
    ],
    "nextCursor": "1234567890"
  }
}
```

## Get Current Copy

`GET /api/v3/copy/futures/current-copy`

Rate limit: 10/sec/UID

Permission: Unified Account — Trade — Read-only

Get current copy trading information for a project.

Operation ID: `copyTradingFollowerGetCurrentCopy`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| projectId | query | string | 是 | Project ID |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.eliteTrader | string |  | Lead trader name |
| data.estNetProfit | string |  | Estimated net profit in USDT |
| data.profitShare | string |  | Profit sharing amount in USDT |
| data.estValue | string |  | Estimated total asset value in USDT, including unrealized P&L |
| data.available | string |  | Available balance in USDT |
| data.currentInvestment | string |  | Cumulative investment amount in USDT |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": {
    "eliteTrader": "TraderAlpha",
    "estNetProfit": "200.00",
    "profitShare": "20.00",
    "estValue": "1200.00",
    "available": "500.00",
    "currentInvestment": "1000.00"
  }
}
```

## Get Copy Profit Details

`GET /api/v3/copy/futures/copy-profit-details`

Rate limit: 1/sec/UID

Permission: Unified Account — Trade — Read-only

Get the profit sharing detail records for the copy trading account.

Operation ID: `copyTradingFollowerGetCopyProfitDetails`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| projectId | query | string | 是 | Project ID |
| startTime | query | string |  | Start timestamp (Unix ms, e.g. `1597026383085`) |
| endTime | query | string |  | End timestamp (Unix ms, e.g. `1597026383085`) |
| limit | query | string |  | Number of results. Default: 20, max: 100. |
| cursor | query | string |  | Cursor ID for pagination. Pass the `nextCursor` returned from the previous response. |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.list | object[] |  | Profit sharing records |
| data.list[].settleTime | string |  | Settlement time (Unix ms) |
| data.list[].profit | string |  | Follower profit or loss |
| data.list[].allocatedPnl | string |  | Allocated profit sharing P&L |
| data.list[].pendingPnl | string |  | Pending profit sharing P&L |
| data.list[].shareRatio | string |  | Profit sharing ratio in decimal form |
| data.list[].shareProfit | string |  | Profit sharing amount |
| data.nextCursor | string |  | Cursor ID for next page |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": {
    "list": [
      {
        "settleTime": "1740000000000",
        "profit": "100.00",
        "allocatedPnl": "80.00",
        "pendingPnl": "20.00",
        "shareRatio": "0.1",
        "shareProfit": "10.00"
      }
    ],
    "nextCursor": "1234567890"
  }
}
```

## Close Positions

`POST /api/v3/copy/futures/close-positions`

Rate limit: 1/sec/UID

Permission: Unified Account — Trade — Read-write

Manually close a position in the copy trading account.

Operation ID: `copyTradingFollowerClosePositions`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| projectId | string | 是 | Project ID |
| symbol | string | 是 | Trading pair name |
| qty | string | 是 | Quantity to close |
| holdSide | string | 是 | Position side<br><br>`long` Long position<br><br>`short` Short position<br><br>Required in hedge mode. |

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
  "requestTime": 1740000000000.0,
  "data": "success"
}
```

## Close All

`POST /api/v3/copy/futures/close-all`

Rate limit: 1/sec/UID

Permission: Unified Account — Trade — Read-write

Close all positions in the copy trading account with one click.

Operation ID: `copyTradingFollowerCloseAll`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| projectId | string | 是 | Project ID |

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
  "requestTime": 1740000000000.0,
  "data": "success"
}
```

## Get Current Positions

`GET /api/v3/copy/futures/current-positions`

Rate limit: 1/sec/UID

Permission: Unified Account — Trade — Read-only

Get the current open positions for the copy trading account.

Operation ID: `copyTradingFollowerGetCurrentPositions`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| projectId | query | string | 是 | Project ID |
| symbol | query | string |  | Trading pair, e.g. `BTCUSDT`. If not specified, all positions are returned. |
| posSide | query | string |  | Position side. If specified, only positions in the given direction are returned.<br><br>`long` Long<br><br>`short` Short |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.list | object[] |  | Current positions |
| data.list[].symbol | string |  | Trading pair name |
| data.list[].marginCoin | string |  | Margin coin |
| data.list[].posSide | string |  | Position side<br><br>`long` Long<br><br>`short` Short |
| data.list[].total | string |  | Position quantity |
| data.list[].leverage | string |  | Leverage multiplier |
| data.list[].avgPrice | string |  | Average entry price |
| data.list[].marginMode | string |  | Margin mode<br><br>`crossed` Cross margin<br><br>`isolated` Isolated margin |
| data.list[].holdMode | string |  | Position mode<br><br>`one_way_mode` One-way mode<br><br>`hedge_mode` Hedge mode |
| data.list[].createdTime | string |  | Position creation time (Unix ms) |
| data.list[].positionId | string |  | Position ID |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": {
    "list": [
      {
        "symbol": "BTCUSDT",
        "marginCoin": "USDT",
        "posSide": "long",
        "total": "0.01",
        "leverage": "10",
        "avgPrice": "50000.00",
        "marginMode": "crossed",
        "holdMode": "hedge_mode",
        "createdTime": "1740000000000",
        "positionId": "9876543210"
      }
    ]
  }
}
```

## Place TPSL

`POST /api/v3/copy/futures/place-tpsl`

Rate limit: 1/sec/UID

Permission: Unified Account — Trade — Read-write

Set take-profit and stop-loss for a position in the copy trading account.

Operation ID: `copyTradingFollowerPlaceTpsl`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| projectId | string | 是 | Project ID |
| positionId | string | 是 | Position ID |
| tpTriggerBy | string | 是 | Take-profit trigger type<br><br>`market` Market price (default)<br><br>`mark` Mark price |
| slTriggerBy | string | 是 | Stop-loss trigger type<br><br>`market` Market price (default)<br><br>`mark` Mark price |
| takeProfit | string | 是 | Take-profit trigger price |
| stopLoss | string | 是 | Stop-loss trigger price |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.strategyId | string |  | Strategy ID |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": {
    "strategyId": "1234567890"
  }
}
```

## Modify TPSL

`POST /api/v3/copy/futures/modify-tpsl`

Rate limit: 1/sec/UID

Permission: Unified Account — Trade — Read-write

Modify the take-profit and stop-loss for a copy trading position.

Operation ID: `copyTradingFollowerModifyTpsl`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| projectId | string | 是 | Project ID |
| strategyId | string | 是 | Strategy ID |
| tpTriggerBy | string | 是 | Take-profit trigger type<br><br>`market` Market price<br><br>`mark` Mark price |
| slTriggerBy | string | 是 | Stop-loss trigger type<br><br>`market` Market price<br><br>`mark` Mark price |
| takeProfit | string | 是 | Take-profit trigger price |
| stopLoss | string | 是 | Stop-loss trigger price |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.strategyId | string |  | Strategy ID |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": {
    "strategyId": "1234567890"
  }
}
```

## Cancel TPSL

`POST /api/v3/copy/futures/cancel-tpsl`

Rate limit: 1/sec/UID

Permission: Unified Account — Trade — Read-write

Cancel a take-profit/stop-loss strategy for a copy trading position.

Operation ID: `copyTradingFollowerCancelTpsl`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| projectId | string | 是 | Project ID |
| strategyId | string | 是 | Strategy ID |

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
  "requestTime": 1740000000000.0,
  "data": "success"
}
```

## Get Current TPSL Orders

`GET /api/v3/copy/futures/current-tpsl-orders`

Rate limit: 1/sec/UID

Permission: Unified Account — Trade — Read-only

Get the current take-profit/stop-loss orders for the copy trading account.

Operation ID: `copyTradingFollowerGetCurrentTpslOrders`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| projectId | query | string | 是 | Project ID |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.list | object[] |  | Current TPSL orders |
| data.list[].strategyId | string |  | Strategy ID |
| data.list[].category | string |  | Product type<br><br>`USDT-FUTURES` USDT-M futures<br><br>`COIN-FUTURES` Coin-M futures<br><br>`USDC-FUTURES` USDC futures |
| data.list[].symbol | string |  | Trading pair name, e.g. `BTCUSDT` |
| data.list[].qty | string |  | Order quantity |
| data.list[].posSide | string |  | Position side<br><br>`long` Long<br><br>`short` Short |
| data.list[].status | string |  | Strategy order status<br><br>`pending` Pending execution<br><br>`success` Executed<br><br>`failed` Failed<br><br>`cancelled` Cancelled<br><br>`submitting` Submitting |
| data.list[].tpTriggerBy | string |  | Take-profit trigger type<br><br>`market` Market price<br><br>`mark` Mark price |
| data.list[].slTriggerBy | string |  | Stop-loss trigger type<br><br>`market` Market price<br><br>`mark` Mark price |
| data.list[].takeProfit | string |  | Take-profit trigger price |
| data.list[].stopLoss | string |  | Stop-loss trigger price |
| data.list[].tpOrderType | string |  | Take-profit order type<br><br>`market` Market order |
| data.list[].slOrderType | string |  | Stop-loss order type<br><br>`market` Market order |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": {
    "list": [
      {
        "strategyId": "1234567890",
        "category": "USDT-FUTURES",
        "symbol": "BTCUSDT",
        "qty": "0.01",
        "posSide": "long",
        "status": "pending",
        "tpTriggerBy": "market",
        "slTriggerBy": "market",
        "takeProfit": "60000.00",
        "stopLoss": "45000.00",
        "tpOrderType": "market",
        "slOrderType": "market"
      }
    ]
  }
}
```

## Get TPSL Order History

`GET /api/v3/copy/futures/tpsl-order-history`

Rate limit: 1/sec/UID

Permission: Unified Account — Trade — Read-only

Get historical take-profit/stop-loss orders for the copy trading account.

Operation ID: `copyTradingFollowerGetTpslOrderHistory`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| projectId | query | string | 是 | Project ID |
| startTime | query | string |  | Start timestamp (Unix ms). Defaults to the last 30 days. Maximum query range: 90 days. |
| endTime | query | string |  | End timestamp (Unix ms). Defaults to the last 30 days. Maximum query range: 90 days. |
| limit | query | string |  | Number of results. Default and max: 100. |
| cursor | query | string |  | Cursor ID for pagination. |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.list | object[] |  | Historical TPSL orders |
| data.list[].strategyId | string |  | Strategy ID |
| data.list[].category | string |  | Product type<br><br>`USDT-FUTURES` USDT-M futures<br><br>`COIN-FUTURES` Coin-M futures<br><br>`USDC-FUTURES` USDC futures |
| data.list[].symbol | string |  | Trading pair name, e.g. `BTCUSDT` |
| data.list[].qty | string |  | Order quantity |
| data.list[].posSide | string |  | Position side<br><br>`long` Long<br><br>`short` Short |
| data.list[].status | string |  | Strategy order status<br><br>`success` Executed<br><br>`failed` Failed<br><br>`cancelled` Cancelled |
| data.list[].tpTriggerBy | string |  | Take-profit trigger type<br><br>`market` Market price<br><br>`mark` Mark price |
| data.list[].slTriggerBy | string |  | Stop-loss trigger type<br><br>`market` Market price<br><br>`mark` Mark price |
| data.list[].takeProfit | string |  | Take-profit trigger price |
| data.list[].stopLoss | string |  | Stop-loss trigger price |
| data.list[].tpOrderType | string |  | Take-profit order type<br><br>`market` Market order |
| data.list[].slOrderType | string |  | Stop-loss order type<br><br>`market` Market order |
| data.cursor | string |  | Cursor ID for next page |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": {
    "list": [
      {
        "strategyId": "1234567890",
        "category": "USDT-FUTURES",
        "symbol": "BTCUSDT",
        "qty": "0.01",
        "posSide": "long",
        "status": "success",
        "tpTriggerBy": "market",
        "slTriggerBy": "market",
        "takeProfit": "60000.00",
        "stopLoss": "45000.00",
        "tpOrderType": "market",
        "slOrderType": "market"
      }
    ],
    "cursor": "1234567890"
  }
}
```


---

合约跟单接口：合约带单（公域&私域）与合约跟单（公域）。

版本: 1.0.0

## 服务地址

- `https://api.bitget.com`

## 接口列表

- `GET /api/v3/copy/futures/position-summary` — 获取仓位汇总
- `GET /api/v3/copy/futures/trading-pairs` — 获取带单币对信息
- `GET /api/v3/copy/futures/max-transferable` — 带单账户最大可转出
- `POST /api/v3/copy/futures/transfer` — 带单账户划转
- `GET /api/v3/copy/futures/transfer-record` — 查询带单账户划转记录
- `GET /api/v3/copy/futures/current-follower` — 获取当前跟随者
- `GET /api/v3/copy/futures/history-follower` — 获取历史跟随者
- `GET /api/v3/copy/futures/profit-summary` — 获取分润汇总
- `GET /api/v3/copy/futures/profit-details` — 获取分润详情
- `GET /api/v3/copy/futures/portfolio-overview` — 获取项目总览
- `POST /api/v3/copy/futures/follower-settings` — 创建跟单
- `POST /api/v3/copy/futures/modify-follower-settings` — 调整跟单设置
- `POST /api/v3/copy/futures/unfollow` — 取消跟单
- `GET /api/v3/copy/futures/copy-settings` — 查询跟单设置
- `GET /api/v3/copy/futures/copy-max-transferable` — 跟单账户最大可转出
- `POST /api/v3/copy/futures/copy-transfer` — 跟单账户划转
- `GET /api/v3/copy/futures/copy-transfer-record` — 查询跟单账户划转记录
- `GET /api/v3/copy/futures/current-copy` — 获取当前跟单信息
- `GET /api/v3/copy/futures/copy-profit-details` — 获取分润记录
- `POST /api/v3/copy/futures/close-positions` — 手动平仓
- `POST /api/v3/copy/futures/close-all` — 一键平仓
- `GET /api/v3/copy/futures/current-positions` — 获取当前仓位
- `POST /api/v3/copy/futures/place-tpsl` — 设置止盈止损
- `POST /api/v3/copy/futures/modify-tpsl` — 修改止盈止损
- `POST /api/v3/copy/futures/cancel-tpsl` — 撤销止盈止损
- `GET /api/v3/copy/futures/current-tpsl-orders` — 获取当前止盈止损单
- `GET /api/v3/copy/futures/tpsl-order-history` — 获取历史止盈止损单

## 获取仓位汇总

`GET /api/v3/copy/futures/position-summary`

限频规则: 5次/秒/UID

权限: 统一账户 — 合约带单持仓 — 只读

获取仓位汇总

Operation ID: `copyTradingPublicPrivateGetPositionSummary`

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].unrealizedPnl | string |  | 未实现盈亏<br><br>单位：USDT |
| data[].realizedPnl | string |  | 已实现盈亏<br><br>单位：USDT |
| data[].holdSize | string |  | 持仓数量 |
| data[].avgPrice | string |  | 持仓均价 |
| data[].symbol | string |  | 交易对名称 |
| data[].leverage | string |  | 杠杆倍数<br><br>正整数 |
| data[].marginMode | string |  | 保证金模式：<br><br>`isolated` 逐仓<br><br>`cross` 全仓 |
| data[].liqPrice | string |  | 强平价格 |
| data[].margin | string |  | 保证金 |
| data[].holdSide | string |  | 持仓方向：<br><br>`long` 多仓<br><br>`short` 空仓 |
| data[].roi | string |  | 回报率 |
| data[].markPrice | string |  | 标记价格 |
| data[].positionValue | string |  | 仓位价值<br><br>单位：USDT |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1774957537393,
  "data": [
    {
      "unrealizedPnl": "0.0095",
      "realizedPnl": "-0.0085658580000000",
      "holdSize": "0.01",
      "avgPrice": "2039.49",
      "symbol": "ETHUSDT",
      "leverage": "10",
      "marginMode": "crossed",
      "liqPrice": "0",
      "margin": "2.04900984",
      "holdSide": "long",
      "roi": "0.0046363857202896",
      "markPrice": "2040.44",
      "positionValue": "20.4044"
    }
  ]
}
```

## 获取带单币对信息

`GET /api/v3/copy/futures/trading-pairs`

限频规则: 5次/秒/UID

权限: 统一账户 — 合约带单订单 — 只读

获取带单币对信息

Operation ID: `copyTradingPublicPrivateGetTradingPairs`

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].symbol | string |  | 交易对名称 |
| data[].leverage | string |  | 杠杆倍数 |
| data[].marginDetails | object[] |  | 保证金明细列表 |
| data[].marginDetails[].marginCoin | string |  | 保证金币种<br><br>如 `USDT` |
| data[].marginDetails[].maxLongCount | string |  | 多单最大张数 |
| data[].marginDetails[].remainingLongCount | string |  | 多单剩余张数 |
| data[].marginDetails[].maxShortCount | string |  | 空单最大张数 |
| data[].marginDetails[].remainingShortCount | string |  | 空单剩余张数 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1774957070136,
  "data": [
    {
      "symbol": "ADAUSDT",
      "leverage": "50",
      "marginDetails": [
        {
          "marginCoin": "USDT",
          "maxLongCount": "9600000",
          "remainingLongCount": "9600000",
          "maxShortCount": "9600000",
          "remainingShortCount": "9600000"
        }
      ]
    }
  ]
}
```

## 带单账户最大可转出

`GET /api/v3/copy/futures/max-transferable`

限频规则: 1次/秒/UID

权限: 需要统一账户合约带单订单只读权限

获取带单账户的最大可转出金额及可用余额。

Operation ID: `copyTradingPublicPrivateGetMaxTransferable`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| coin | query | string | 是 | 币种名称，例如 `USDT` |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.maxTransferable | string |  | 最大可转出金额 |
| data.available | string |  | 可用余额 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": {
    "maxTransferable": "1000.00",
    "available": "1200.00"
  }
}
```

## 带单账户划转

`POST /api/v3/copy/futures/transfer`

限频规则: 1次/秒/UID

权限: 需要统一账户合约带单订单读写权限

将资金转入或转出带单账户。仅支持现货账户（经典）/资金账户（统一）与带单账户之间的划转。

Operation ID: `copyTradingPublicPrivateTransfer`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| type | string | 是 | 划转类型<br><br>`in` 转入（现货/资金账户 → 带单账户）<br><br>`out` 转出（带单账户 → 现货/资金账户） |
| inAccountType | string |  | 转入账户类型，支持多选，多个账户类型用英文逗号 `,` 分隔<br><br>`funding` 现货/资金账户<br><br>`uta` 统一账户<br><br>`otc` OTC账户<br><br>如不选，默认选择全部账户<br><br>扣款顺序：资金账户 → OTC账户 → 统一账户<br><br>经典账户模式仅支持 `funding` 现货账户转入 |
| coin | string | 是 | 划转币种 |
| amount | string | 是 | 划转数量 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.transferId | string |  | 划转订单ID |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": {
    "transferId": "1234567890"
  }
}
```

## 查询带单账户划转记录

`GET /api/v3/copy/futures/transfer-record`

限频规则: 1次/秒/UID

权限: 需要统一账户合约带单订单只读权限

查询带单账户的划转历史记录。

Operation ID: `copyTradingPublicPrivateGetTransferRecord`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| startTime | query | string |  | 开始时间戳，Unix毫秒时间戳，如 `1597026383085` |
| endTime | query | string |  | 结束时间戳，Unix毫秒时间戳，如 `1597026383085` |
| limit | query | string |  | 查询条数，默认 `20`，最大 `100` |
| cursor | query | string |  | 游标ID。传入上次调用返回的 `nextCursor` 以分页获取更新的数据 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.list | object[] |  | 划转记录列表 |
| data.list[].transferId | string |  | 划转订单ID |
| data.list[].fromType | string |  | 转出账户类型，可能返回多个值，以英文逗号分隔<br><br>`spot` 现货/资金账户<br><br>`uta` 统一账户<br><br>`otc` OTC账户<br><br>`lead` 带单账户 |
| data.list[].toType | string |  | 转入账户类型，可能返回多个值，以英文逗号分隔<br><br>`spot` 现货/资金账户<br><br>`uta` 统一账户<br><br>`otc` OTC账户<br><br>`lead` 带单账户 |
| data.list[].amount | string |  | 划转数量 |
| data.list[].coin | string |  | 划转币种 |
| data.list[].status | string |  | 划转状态<br><br>`Successful` 成功<br><br>`Failed` 失败<br><br>`Processing` 处理中 |
| data.list[].createdTime | string |  | 划转创建时间，Unix毫秒时间戳 |
| data.nextCursor | string |  | 下页游标 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": {
    "list": [
      {
        "transferId": "1234567890",
        "fromType": "spot,uta",
        "toType": "lead",
        "amount": "100.00",
        "coin": "USDT",
        "status": "Successful",
        "createdTime": "1740000000000"
      }
    ],
    "nextCursor": "1234567890"
  }
}
```

## 获取当前跟随者

`GET /api/v3/copy/futures/current-follower`

限频规则: 1次/秒/UID

权限: 需要统一账户合约带单订单只读权限

获取带单账户当前活跃的跟随者列表。

Operation ID: `copyTradingPublicPrivateGetCurrentFollowers`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| limit | query | string |  | 查询条数，默认 `20`，最大 `100` |
| cursor | query | string |  | 游标ID。传入上次调用返回的 `nextCursor` 以分页获取更新的数据 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.list | object[] |  | 跟随者列表 |
| data.list[].followerName | string |  | 跟随者用户昵称 |
| data.list[].estimateAssets | string |  | 资产估值，单位为USDT |
| data.list[].totalProfit | string |  | 总收益，单位为USDT |
| data.list[].totalShareProfit | string |  | 总分润，单位为USDT |
| data.list[].totalInvestment | string |  | 总投资额，单位为USDT |
| data.list[].canRemove | string |  | 能否移除<br><br>`yes` 是<br><br>`no` 否 |
| data.list[].followDays | string |  | 跟随天数，正整数 |
| data.list[].totalAssets | string |  | 账户权益，单位为USDT |
| data.list[].startTime | string |  | 开始跟随时间，Unix毫秒时间戳 |
| data.nextCursor | string |  | 下页游标 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": {
    "list": [
      {
        "followerName": "Alice",
        "estimateAssets": "10000.00",
        "totalProfit": "500.00",
        "totalShareProfit": "50.00",
        "totalInvestment": "9500.00",
        "canRemove": "no",
        "followDays": "30",
        "totalAssets": "10500.00",
        "startTime": "1740000000000"
      }
    ],
    "nextCursor": "1234567890"
  }
}
```

## 获取历史跟随者

`GET /api/v3/copy/futures/history-follower`

限频规则: 1次/秒/UID

权限: 需要统一账户合约带单订单只读权限

获取带单账户的历史跟随者列表。

Operation ID: `copyTradingPublicPrivateGetHistoryFollowers`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| limit | query | string |  | 查询条数，默认 `20`，最大 `100` |
| cursor | query | string |  | 游标ID。传入上次调用返回的 `nextCursor` 以分页获取更新的数据 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.list | object[] |  | 历史跟随者列表 |
| data.list[].followerName | string |  | 跟随者昵称 |
| data.list[].totalProfit | string |  | 总收益，单位为USDT |
| data.list[].totalShareProfit | string |  | 总分润，单位为USDT |
| data.list[].totalInvestment | string |  | 总投资额，单位为USDT |
| data.list[].startTime | string |  | 跟随开始时间，Unix毫秒时间戳 |
| data.list[].endTime | string |  | 跟随结束时间，Unix毫秒时间戳 |
| data.nextCursor | string |  | 下页游标 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": {
    "list": [
      {
        "followerName": "Bob",
        "totalProfit": "200.00",
        "totalShareProfit": "20.00",
        "totalInvestment": "5000.00",
        "startTime": "1730000000000",
        "endTime": "1740000000000"
      }
    ],
    "nextCursor": "1234567890"
  }
}
```

## 获取分润汇总

`GET /api/v3/copy/futures/profit-summary`

限频规则: 1次/秒/UID

权限: 需要统一账户合约带单订单只读权限

获取带单账户的分润汇总信息。

Operation ID: `copyTradingPublicPrivateGetProfitSummary`

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.totalProfit | string |  | 累计收益，单位为USDT |
| data.totalAllocatedProfit | string |  | 累计已分润，单位为USDT |
| data.totalPendingProfit | string |  | 累计待分润，单位为USDT |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": {
    "totalProfit": "10000.00",
    "totalAllocatedProfit": "8000.00",
    "totalPendingProfit": "2000.00"
  }
}
```

## 获取分润详情

`GET /api/v3/copy/futures/profit-details`

限频规则: 1次/秒/UID

权限: 需要统一账户合约带单订单只读权限

获取带单账户的分润明细记录。

Operation ID: `copyTradingPublicPrivateGetProfitDetails`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| startTime | query | string |  | 开始时间戳，Unix毫秒时间戳，如 `1597026383085` |
| endTime | query | string |  | 结束时间戳，Unix毫秒时间戳，如 `1597026383085` |
| limit | query | string |  | 查询条数，默认 `20`，最大 `100` |
| cursor | query | string |  | 游标ID。传入上次调用返回的 `nextCursor` 以分页获取更新的数据 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.list | object[] |  | 分润明细列表 |
| data.list[].followerName | string |  | 跟随者名称 |
| data.list[].profit | string |  | 跟单者盈亏 |
| data.list[].allocatedPnl | string |  | 已分润盈亏 |
| data.list[].pendingPnl | string |  | 待分润盈亏 |
| data.list[].shareRatio | string |  | 分润比例，小数形式 |
| data.list[].shareProfit | string |  | 分润金额 |
| data.list[].reason | string |  | 原因<br><br>`period` 周期结算<br><br>`unfollow` 取消跟随结算 |
| data.list[].settleTime | string |  | 结算时间，Unix毫秒时间戳 |
| data.nextCursor | string |  | 游标ID |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": {
    "list": [
      {
        "followerName": "Alice",
        "profit": "500.00",
        "allocatedPnl": "400.00",
        "pendingPnl": "100.00",
        "shareRatio": "0.1",
        "shareProfit": "50.00",
        "reason": "period",
        "settleTime": "1740000000000"
      }
    ],
    "nextCursor": "1234567890"
  }
}
```

## 获取项目总览

`GET /api/v3/copy/futures/portfolio-overview`

限频规则: 1次/秒/UID

权限: 统一账户 — 合约带单订单 — 只读

获取带单项目总览。

Operation ID: `copyTradingPublicPrivateGetPortfolioOverview`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| period | query | string | 是 | 7D/30D/90D/180D |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.projectId | string |  | 项目ID |
| data.asset | string |  | 管理资产 |
| data.roi | string |  | 投资回报率 |
| data.totalProfit | string |  | 总利润 |
| data.followerProfit | string |  | 跟单者利润 |
| data.maxDrawdown | string |  | 最大回撤 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": {
    "projectId": "1234567890",
    "asset": "10000.00",
    "roi": "0.15",
    "totalProfit": "1500.00",
    "followerProfit": "1200.00",
    "maxDrawdown": "0.05"
  }
}
```

## 创建跟单

`POST /api/v3/copy/futures/follower-settings`

限频规则: 1次/秒/UID

权限: 统一账户 — 交易 — 读写

为带单项目创建跟单订阅。

Operation ID: `copyTradingFollowerCreateCopy`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| projectId | string | 是 | 项目ID |
| accountType | string |  | 自动划转的账户类型，多个账户类型用英文逗号`,`分隔。<br><br>`funding` 资金账户<br><br>`uta` 统一账户<br><br>`otc` OTC账户<br><br>如不选，默认选择全部账户。<br><br>扣款顺序：资金账户 → OTC账户 → 统一账户。 |
| type | string | 是 | 跟单类型<br><br>`fixed_ratio` 固定比例：每笔订单将根据交易专家的下单保证金与其账户净值的比例进行等比例下单。<br><br>`fixed_margin` 固定保证金：每笔订单均使用固定保证金开仓。 |
| amount | string | 是 | 跟单金额，单位USDT，最小值为50。 |
| tradingPairList | string |  | 跟单币对列表。如不传，则默认跟随全部币对。如果交易专家交易的币对超出您选择的范围，系统将不会为您执行任何交易。 |
| marginPerOrder | string |  | 每笔保证金，单位USDT。`type=fixed_margin`时必填。 |
| autoCopy | string |  | 自动跟随新带单币对。<br><br>`on` 自动跟随（默认）<br><br>`off` 不自动跟随 |
| leverage | string |  | 杠杆倍数。如不填，则默认跟随带单专家的杠杆倍数。范围为[1, 10]。 |
| maxEntrySlippage | string |  | 最大开仓滑点。如不填，则为系统默认值。范围为[0.1, 3]，0.1代表0.1%。 |
| maxMarginRatio | string |  | 单笔最大保证金比例，范围为[5, 95]，5代表5%。当合约单笔开仓保证金占总资产比例达到设置值时，系统会以最大比例计算的开仓保证金下单。 |
| maxPostionValue | string |  | 最大持仓价值，单位USDT，默认值和最大值均为2000000。当持有的全部仓位价值超过设置值时，系统将不再进行跟单开仓。 |

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
  "requestTime": 1740000000000.0,
  "data": "success"
}
```

## 调整跟单设置

`POST /api/v3/copy/futures/modify-follower-settings`

限频规则: 1次/秒/UID

权限: 统一账户 — 交易 — 读写

调整已有跟单订阅的设置。

Operation ID: `copyTradingFollowerModifySettings`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| projectId | string | 是 | 项目ID |
| tradingPairList | string |  | 跟单币对列表。如传`all`，则代表全部币对。 |
| marginPerOrder | string |  | 每笔保证金，单位USDT。 |
| autoCopy | string |  | 自动跟随新带单币对。<br><br>`on` 自动跟随<br><br>`off` 不自动跟随 |
| leverage | string |  | 杠杆倍数，范围为[1, 10]。在无仓位情况下可修改该字段。 |
| maxEntrySlippage | string |  | 最大开仓滑点，范围为[0.1, 3]，0.1代表0.1%。 |
| maxMarginRatio | string |  | 单笔最大保证金比例，范围为[5, 95]。 |
| maxPostionValue | string |  | 最大持仓价值，单位USDT，最大值为2000000。 |

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
  "requestTime": 1740000000000.0,
  "data": "success"
}
```

## 取消跟单

`POST /api/v3/copy/futures/unfollow`

限频规则: 1次/秒/UID

权限: 统一账户 — 交易 — 读写

取消跟单订阅。

Operation ID: `copyTradingFollowerUnfollow`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| projectId | string | 是 | 项目ID |
| closeType | string |  | 取消跟单时的平仓类型。<br><br>`follow_close` 跟随交易专家平仓<br><br>`instant_close` 立即平仓 |

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
  "requestTime": 1740000000000.0,
  "data": "success"
}
```

## 查询跟单设置

`GET /api/v3/copy/futures/copy-settings`

限频规则: 5次/秒/UID

权限: 统一账户 — 交易 — 只读

查询跟单设置。

Operation ID: `copyTradingFollowerGetCopySettings`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| projectId | query | string | 是 | 项目ID |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.type | string |  | 跟单类型<br><br>`fixed_ratio` 固定比例<br><br>`fixed_margin` 固定保证金 |
| data.amount | string |  | 跟单金额 |
| data.tradingPairList | string[] |  | 跟单币对列表 |
| data.marginPerOrder | string |  | 每笔保证金 |
| data.autoCopy | string |  | 自动跟随设置<br><br>`on` 自动跟随<br><br>`off` 不自动跟随 |
| data.leverage | string |  | 杠杆倍数。跟随带单专家的杠杆倍数时，该字段返回空。 |
| data.maxEntrySlippage | string |  | 最大开仓滑点，百分比数值返回，如1代表1%。 |
| data.maxMarginRatio | string |  | 单笔最大保证金比例，百分比数值返回，如90代表90%。 |
| data.maxPostionValue | string |  | 最大持仓价值 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": {
    "type": "fixed_ratio",
    "amount": "1000.00",
    "tradingPairList": [
      "BTCUSDT",
      "ETHUSDT"
    ],
    "marginPerOrder": "",
    "autoCopy": "on",
    "leverage": "",
    "maxEntrySlippage": "1",
    "maxMarginRatio": "90",
    "maxPostionValue": "2000000"
  }
}
```

## 跟单账户最大可转出

`GET /api/v3/copy/futures/copy-max-transferable`

限频规则: 1次/秒/UID

权限: 统一账户 — 管理 — 只读

根据指定币种查询跟单账户的最大可转出数量。

Operation ID: `copyTradingFollowerGetCopyMaxTransferable`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| projectId | query | string | 是 | 项目ID |
| coin | query | string | 是 | 币种名称，例如 `USDT` |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.maxTransferable | string |  | 最大可转出数量 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": {
    "maxTransferable": "1000.00"
  }
}
```

## 跟单账户划转

`POST /api/v3/copy/futures/copy-transfer`

限频规则: 1次/秒/UID

权限: 统一账户 — 管理 — 读写

向跟单账户转入或转出资金。

Operation ID: `copyTradingFollowerCopyTransfer`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| projectId | string | 是 | 项目ID |
| type | string | 是 | 划转类型<br><br>`in` 转入<br><br>`out` 转出，仅支持转出至现货/资金账户 |
| inAccountType | string |  | 转入账户类型，多个账户类型用英文逗号分隔。<br><br>`funding` 资金账户<br><br>`uta` 统一账户<br><br>`otc` OTC账户<br><br>如不选，默认选择全部账户。扣款顺序：资金账户 → OTC账户 → 统一账户。 |
| coin | string | 是 | 划转币种 |
| amount | string | 是 | 划转数量 |

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
  "requestTime": 1740000000000.0,
  "data": "success"
}
```

## 查询跟单账户划转记录

`GET /api/v3/copy/futures/copy-transfer-record`

限频规则: 1次/秒/UID

权限: 统一账户 — 管理 — 只读

查询跟单账户的划转历史记录。

Operation ID: `copyTradingFollowerGetCopyTransferRecord`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| projectId | query | string | 是 | 项目ID |
| limit | query | string |  | 查询条数，默认20，最大100。 |
| cursor | query | string |  | 游标ID。传上次调用返回的`nextCursor`进行翻页。 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.list | object[] |  | 划转记录 |
| data.list[].fromType | string |  | 转出账户类型<br><br>`funding` 资金账户<br><br>`uta` 统一账户<br><br>`otc` OTC账户<br><br>`copy` 跟单账户 |
| data.list[].toType | string |  | 转入账户类型<br><br>`funding` 资金账户<br><br>`uta` 统一账户<br><br>`otc` OTC账户<br><br>`copy` 跟单账户 |
| data.list[].amount | string |  | 划转数量 |
| data.list[].coin | string |  | 划转币种 |
| data.list[].status | string |  | 划转状态<br><br>`successful` 成功<br><br>`failed` 失败<br><br>`processing` 处理中 |
| data.list[].createdTime | string |  | 划转创建时间（Unix毫秒时间戳） |
| data.nextCursor | string |  | 下一页游标ID |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": {
    "list": [
      {
        "fromType": "funding",
        "toType": "copy",
        "amount": "500.00",
        "coin": "USDT",
        "status": "successful",
        "createdTime": "1740000000000"
      }
    ],
    "nextCursor": "1234567890"
  }
}
```

## 获取当前跟单信息

`GET /api/v3/copy/futures/current-copy`

限频规则: 10次/秒/UID

权限: 统一账户 — 交易 — 只读

获取当前跟单信息。

Operation ID: `copyTradingFollowerGetCurrentCopy`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| projectId | query | string | 是 | 项目ID |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.eliteTrader | string |  | 交易专家名称 |
| data.estNetProfit | string |  | 预计净利润，单位USDT |
| data.profitShare | string |  | 分润金额，单位USDT |
| data.estValue | string |  | 资产估值，单位USDT，包含未实现盈亏 |
| data.available | string |  | 可用余额，单位USDT |
| data.currentInvestment | string |  | 累计投资额，单位USDT |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": {
    "eliteTrader": "TraderAlpha",
    "estNetProfit": "200.00",
    "profitShare": "20.00",
    "estValue": "1200.00",
    "available": "500.00",
    "currentInvestment": "1000.00"
  }
}
```

## 获取分润记录

`GET /api/v3/copy/futures/copy-profit-details`

限频规则: 1次/秒/UID

权限: 统一账户 — 交易 — 只读

获取跟单账户的分润详情记录。

Operation ID: `copyTradingFollowerGetCopyProfitDetails`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| projectId | query | string | 是 | 项目ID |
| startTime | query | string |  | 开始时间戳（Unix毫秒，如`1597026383085`） |
| endTime | query | string |  | 结束时间戳（Unix毫秒，如`1597026383085`） |
| limit | query | string |  | 查询条数，默认20，最大100。 |
| cursor | query | string |  | 游标ID，传上次调用返回的`nextCursor`进行翻页。 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.list | object[] |  | 分润记录 |
| data.list[].settleTime | string |  | 结算时间（Unix毫秒时间戳） |
| data.list[].profit | string |  | 跟单者盈亏 |
| data.list[].allocatedPnl | string |  | 已分润盈亏 |
| data.list[].pendingPnl | string |  | 待分润盈亏 |
| data.list[].shareRatio | string |  | 分润比例，小数形式 |
| data.list[].shareProfit | string |  | 分润金额 |
| data.nextCursor | string |  | 下一页游标ID |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": {
    "list": [
      {
        "settleTime": "1740000000000",
        "profit": "100.00",
        "allocatedPnl": "80.00",
        "pendingPnl": "20.00",
        "shareRatio": "0.1",
        "shareProfit": "10.00"
      }
    ],
    "nextCursor": "1234567890"
  }
}
```

## 手动平仓

`POST /api/v3/copy/futures/close-positions`

限频规则: 1次/秒/UID

权限: 统一账户 — 交易 — 读写

手动平仓。

Operation ID: `copyTradingFollowerClosePositions`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| projectId | string | 是 | 项目ID |
| symbol | string | 是 | 交易对名称 |
| qty | string | 是 | 平仓数量 |
| holdSide | string | 是 | 持仓方向<br><br>`long` 多仓<br><br>`short` 空仓<br><br>双向持仓模式，该字段必填。 |

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
  "requestTime": 1740000000000.0,
  "data": "success"
}
```

## 一键平仓

`POST /api/v3/copy/futures/close-all`

限频规则: 1次/秒/UID

权限: 统一账户 — 交易 — 读写

一键平仓，关闭跟单账户下的全部仓位。

Operation ID: `copyTradingFollowerCloseAll`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| projectId | string | 是 | 项目ID |

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
  "requestTime": 1740000000000.0,
  "data": "success"
}
```

## 获取当前仓位

`GET /api/v3/copy/futures/current-positions`

限频规则: 1次/秒/UID

权限: 统一账户 — 交易 — 只读

获取跟单账户当前仓位。

Operation ID: `copyTradingFollowerGetCurrentPositions`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| projectId | query | string | 是 | 项目ID |
| symbol | query | string |  | 交易对，如`BTCUSDT`。如不传，则返回全部仓位。 |
| posSide | query | string |  | 仓位方向。如传入此参数，则仅返回对应方向仓位。<br><br>`long` 多<br><br>`short` 空 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.list | object[] |  | 当前仓位 |
| data.list[].symbol | string |  | 交易对名称 |
| data.list[].marginCoin | string |  | 保证金币种 |
| data.list[].posSide | string |  | 仓位方向<br><br>`long` 多<br><br>`short` 空 |
| data.list[].total | string |  | 仓位数量 |
| data.list[].leverage | string |  | 杠杆倍数 |
| data.list[].avgPrice | string |  | 平均开仓价 |
| data.list[].marginMode | string |  | 保证金模式<br><br>`crossed` 全仓<br><br>`isolated` 逐仓 |
| data.list[].holdMode | string |  | 持仓模式<br><br>`one_way_mode` 单向持仓<br><br>`hedge_mode` 双向持仓 |
| data.list[].createdTime | string |  | 仓位创建时间（Unix毫秒时间戳） |
| data.list[].positionId | string |  | 仓位ID |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": {
    "list": [
      {
        "symbol": "BTCUSDT",
        "marginCoin": "USDT",
        "posSide": "long",
        "total": "0.01",
        "leverage": "10",
        "avgPrice": "50000.00",
        "marginMode": "crossed",
        "holdMode": "hedge_mode",
        "createdTime": "1740000000000",
        "positionId": "9876543210"
      }
    ]
  }
}
```

## 设置止盈止损

`POST /api/v3/copy/futures/place-tpsl`

限频规则: 1次/秒/UID

权限: 统一账户 — 交易 — 读写

为跟单账户仓位设置止盈止损。

Operation ID: `copyTradingFollowerPlaceTpsl`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| projectId | string | 是 | 项目ID |
| positionId | string | 是 | 仓位ID |
| tpTriggerBy | string | 是 | 止盈触发类型<br><br>`market` 市场价格（默认）<br><br>`mark` 标记价格 |
| slTriggerBy | string | 是 | 止损触发类型<br><br>`market` 市场价格（默认）<br><br>`mark` 标记价格 |
| takeProfit | string | 是 | 止盈触发价格 |
| stopLoss | string | 是 | 止损触发价格 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.strategyId | string |  | 策略ID |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": {
    "strategyId": "1234567890"
  }
}
```

## 修改止盈止损

`POST /api/v3/copy/futures/modify-tpsl`

限频规则: 1次/秒/UID

权限: 统一账户 — 交易 — 读写

修改跟单账户仓位的止盈止损。

Operation ID: `copyTradingFollowerModifyTpsl`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| projectId | string | 是 | 项目ID |
| strategyId | string | 是 | 策略ID |
| tpTriggerBy | string | 是 | 止盈触发类型<br><br>`market` 市场价格<br><br>`mark` 标记价格 |
| slTriggerBy | string | 是 | 止损触发类型<br><br>`market` 市场价格<br><br>`mark` 标记价格 |
| takeProfit | string | 是 | 止盈触发价格 |
| stopLoss | string | 是 | 止损触发价格 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.strategyId | string |  | 策略ID |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": {
    "strategyId": "1234567890"
  }
}
```

## 撤销止盈止损

`POST /api/v3/copy/futures/cancel-tpsl`

限频规则: 1次/秒/UID

权限: 统一账户 — 交易 — 读写

撤销跟单账户仓位的止盈止损策略。

Operation ID: `copyTradingFollowerCancelTpsl`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| projectId | string | 是 | 项目ID |
| strategyId | string | 是 | 策略ID |

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
  "requestTime": 1740000000000.0,
  "data": "success"
}
```

## 获取当前止盈止损单

`GET /api/v3/copy/futures/current-tpsl-orders`

限频规则: 1次/秒/UID

权限: 统一账户 — 交易 — 只读

获取跟单账户当前止盈止损单。

Operation ID: `copyTradingFollowerGetCurrentTpslOrders`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| projectId | query | string | 是 | 项目ID |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.list | object[] |  | 当前止盈止损单 |
| data.list[].strategyId | string |  | 策略ID |
| data.list[].category | string |  | 产品类型<br><br>`USDT-FUTURES` U本位合约<br><br>`COIN-FUTURES` 币本位合约<br><br>`USDC-FUTURES` USDC合约 |
| data.list[].symbol | string |  | 交易对名称，如`BTCUSDT` |
| data.list[].qty | string |  | 委托数量 |
| data.list[].posSide | string |  | 仓位方向<br><br>`long` 多仓<br><br>`short` 空仓 |
| data.list[].status | string |  | 策略订单状态<br><br>`pending` 等待执行<br><br>`success` 已执行<br><br>`failed` 执行失败<br><br>`cancelled` 已撤销<br><br>`submitting` 下单中 |
| data.list[].tpTriggerBy | string |  | 止盈触发类型<br><br>`market` 市场价格<br><br>`mark` 标记价格 |
| data.list[].slTriggerBy | string |  | 止损触发类型<br><br>`market` 市场价格<br><br>`mark` 标记价格 |
| data.list[].takeProfit | string |  | 止盈触发价格 |
| data.list[].stopLoss | string |  | 止损触发价格 |
| data.list[].tpOrderType | string |  | 止盈触发的策略单类型<br><br>`market` 市价单 |
| data.list[].slOrderType | string |  | 止损触发的策略单类型<br><br>`market` 市价单 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": {
    "list": [
      {
        "strategyId": "1234567890",
        "category": "USDT-FUTURES",
        "symbol": "BTCUSDT",
        "qty": "0.01",
        "posSide": "long",
        "status": "pending",
        "tpTriggerBy": "market",
        "slTriggerBy": "market",
        "takeProfit": "60000.00",
        "stopLoss": "45000.00",
        "tpOrderType": "market",
        "slOrderType": "market"
      }
    ]
  }
}
```

## 获取历史止盈止损单

`GET /api/v3/copy/futures/tpsl-order-history`

限频规则: 1次/秒/UID

权限: 统一账户 — 交易 — 只读

获取跟单账户历史止盈止损单。

Operation ID: `copyTradingFollowerGetTpslOrderHistory`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| projectId | query | string | 是 | 项目ID |
| startTime | query | string |  | 开始时间戳（Unix毫秒）。默认查询时间为近30天，最大时间间隔为90天。 |
| endTime | query | string |  | 结束时间戳（Unix毫秒）。默认查询时间为近30天，最大时间间隔为90天。 |
| limit | query | string |  | 每页条目数，最大和默认均为100。 |
| cursor | query | string |  | 分页游标，用于翻页。 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.list | object[] |  | 历史止盈止损单 |
| data.list[].strategyId | string |  | 策略ID |
| data.list[].category | string |  | 产品类型<br><br>`USDT-FUTURES` U本位合约<br><br>`COIN-FUTURES` 币本位合约<br><br>`USDC-FUTURES` USDC合约 |
| data.list[].symbol | string |  | 交易对名称，如`BTCUSDT` |
| data.list[].qty | string |  | 委托数量 |
| data.list[].posSide | string |  | 仓位方向<br><br>`long` 多仓<br><br>`short` 空仓 |
| data.list[].status | string |  | 策略订单状态<br><br>`success` 已执行<br><br>`failed` 执行失败<br><br>`cancelled` 已撤销 |
| data.list[].tpTriggerBy | string |  | 止盈触发类型<br><br>`market` 市场价格<br><br>`mark` 标记价格 |
| data.list[].slTriggerBy | string |  | 止损触发类型<br><br>`market` 市场价格<br><br>`mark` 标记价格 |
| data.list[].takeProfit | string |  | 止盈触发价格 |
| data.list[].stopLoss | string |  | 止损触发价格 |
| data.list[].tpOrderType | string |  | 止盈触发的策略单类型<br><br>`market` 市价单 |
| data.list[].slOrderType | string |  | 止损触发的策略单类型<br><br>`market` 市价单 |
| data.cursor | string |  | 游标ID，用于翻页 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": {
    "list": [
      {
        "strategyId": "1234567890",
        "category": "USDT-FUTURES",
        "symbol": "BTCUSDT",
        "qty": "0.01",
        "posSide": "long",
        "status": "success",
        "tpTriggerBy": "market",
        "slTriggerBy": "market",
        "takeProfit": "60000.00",
        "stopLoss": "45000.00",
        "tpOrderType": "market",
        "slOrderType": "market"
      }
    ],
    "cursor": "1234567890"
  }
}
```