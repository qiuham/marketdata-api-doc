---
exchange: bitget
source_url: https://www.bitget.com/docs/catalog/cfd-trade
api_type: REST
updated_at: 2026-11-25 19:02:26.942796
---

# CFD Trade

CFD trading APIs: place, modify, cancel orders; close positions; query orders and positions.

版本: 1.0.0

## 服务地址

- `https://api.bitget.com`

## 接口列表

- `POST /api/v3/cfd/trade/place-order` — Place CFD Order
- `POST /api/v3/cfd/trade/modify-order` — Modify CFD Order
- `POST /api/v3/cfd/trade/cancel-order` — Cancel CFD Order
- `POST /api/v3/cfd/trade/cancel-all` — Cancel All CFD Orders
- `POST /api/v3/cfd/trade/close-positions` — Close CFD Positions
- `POST /api/v3/cfd/trade/close-all-positions` — Close All CFD Positions
- `GET /api/v3/cfd/trade/unfilled-order` — Get CFD Unfilled Orders
- `GET /api/v3/cfd/trade/history-order` — Get CFD Order History
- `GET /api/v3/cfd/trade/current-positions` — Get CFD Current Positions

## Place CFD Order

`POST /api/v3/cfd/trade/place-order`

Rate limit: 1/sec/UID <br/> Permission: UTA trade (read & write)

This endpoint is used to place an order on a CFD account.

Operation ID: `cfdTradePlaceOrder`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| symbol | string | 是 | Trading pair name |
| orderType | string | 是 | Order type<br/>`limit`: Limit order<br/>`market`: Market order |
| side | string | 是 | Trade side<br/>`buy`: Buy<br/>`sell`: Sell |
| price | string |  | Order price<br/>Required when `orderType=limit`<br/>The price must be an integer multiple of the trading pair's precision |
| qty | string | 是 | Order quantity |
| takeProfit | string |  | Take-profit price<br/>The price must be an integer multiple of the trading pair's precision |
| stopLoss | string |  | Stop-loss price<br/>The price must be an integer multiple of the trading pair's precision |

```json
{
  "symbol": "XAUUSD",
  "orderType": "market",
  "side": "buy",
  "qty": "1"
}
```

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.trxId | string |  | Request ID |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": {
    "trxId": "111111111111111111"
  }
}
```

## Modify CFD Order

`POST /api/v3/cfd/trade/modify-order`

Rate limit: 1/sec/UID <br/> Permission: UTA trade (read & write)

This endpoint is used to modify an order on a CFD account.

Operation ID: `cfdTradeModifyOrder`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| orderId | string | 是 | Order ID |
| price | string |  | Order price<br/>Required when `orderType=limit` |
| takeProfit | string |  | Take-profit price |
| stopLoss | string |  | Stop-loss price |

```json
{
  "orderId": "111111111111111111",
  "price": "2620.00"
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

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": {
    "orderId": "111111111111111111"
  }
}
```

## Cancel CFD Order

`POST /api/v3/cfd/trade/cancel-order`

Rate limit: 1/sec/UID <br/> Permission: UTA trade (read & write)

This endpoint is used to cancel an order on a CFD account.

Operation ID: `cfdTradeCancelOrder`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| orderId | string | 是 | Order ID |

```json
{
  "orderId": "111111111111111111"
}
```

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data |  |  | null |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": null
}
```

## Cancel All CFD Orders

`POST /api/v3/cfd/trade/cancel-all`

Rate limit: 1/sec/UID <br/> Permission: UTA trade (read & write)

This endpoint is used to cancel all orders on a CFD account.

Operation ID: `cfdTradeCancelAllOrders`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| symbol | string |  | Trading pair name<br/>If not provided, all orders are canceled<br/>If `symbol` is provided, only orders for the specified trading pair are canceled |

```json
{
  "symbol": "XAUUSD"
}
```

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data |  |  | null |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": null
}
```

## Close CFD Positions

`POST /api/v3/cfd/trade/close-positions`

Rate limit: 10/sec/UID <br/> Permission: UTA trade (read & write)

This endpoint is used to close positions on a CFD account. Only market-price closing is currently supported.

Operation ID: `cfdTradeClosePositions`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| positionId | string | 是 | Position ID<br/>Can be obtained via the position list endpoint |
| qty | string | 是 | Order quantity |

```json
{
  "positionId": "111111111111111111",
  "qty": "1"
}
```

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data |  |  | null |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": null
}
```

## Close All CFD Positions

`POST /api/v3/cfd/trade/close-all-positions`

Rate limit: 1/sec/UID <br/> Permission: UTA trade (read & write)

This endpoint is used to close all positions on a CFD account.

Operation ID: `cfdTradeCloseAllPositions`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| symbol | string |  | Trading pair name<br/>If not provided, all positions are closed<br/>If `symbol` is provided, only positions for the specified trading pair are closed |

```json
{
  "symbol": "XAUUSD"
}
```

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data |  |  | null |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": null
}
```

## Get CFD Unfilled Orders

`GET /api/v3/cfd/trade/unfilled-order`

Rate limit: 10/sec/UID <br/> Permission: UTA trade (read-only)

This endpoint is used to query unfilled orders on a CFD account.

Operation ID: `cfdTradeGetUnfilledOrders`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | Trading pair name |
| subUid | query | string |  | Sub-account UID<br/>Used to query a sub-account's unfilled orders |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].symbol | string |  | Trading pair name |
| data[].orderType | string |  | Order type<br/>`limit`: Limit order<br/>`market`: Market order |
| data[].side | string |  | Trade side<br/>`buy`: Buy<br/>`sell`: Sell |
| data[].price | string |  | Order price |
| data[].qty | string |  | Order quantity |
| data[].takeProfit | string |  | Take-profit price |
| data[].stopLoss | string |  | Stop-loss price |
| data[].trxId | string |  | Request ID |
| data[].orderId | string |  | Order ID |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": [
    {
      "symbol": "XAUUSD",
      "orderType": "limit",
      "side": "buy",
      "price": "2620.00",
      "qty": "1",
      "takeProfit": "2650.00",
      "stopLoss": "2600.00",
      "trxId": "111111111111111111",
      "orderId": "111111111111111112"
    }
  ]
}
```

## Get CFD Order History

`GET /api/v3/cfd/trade/history-order`

Rate limit: 10/sec/UID <br/> Permission: UTA trade (read-only)

This endpoint is used to query historical orders on a CFD account.

> The query span per request must not exceed 30 days. The maximum lookback period is 90 days.

Operation ID: `cfdTradeGetOrderHistory`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | Trading pair name |
| subUid | query | string |  | Sub-account UID<br/>Used to query a sub-account's historical orders |
| startTime | query | string |  | Start time, Unix millisecond timestamp |
| endTime | query | string |  | End time, Unix millisecond timestamp |
| limit | query | string |  | Number of entries per page<br/>Default: 10, range [1, 50]<br/>For the first page, the number of entries returned may be greater than the specified `limit` |
| pageNo | query | string |  | Page number |
| cursor | query | string |  | Cursor<br/>Not required for the first page<br/>Required from the second page onward: pass the `orderId` of the last record from the previous page's response |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.list | object[] |  | List |
| data.list[].symbol | string |  | Trading pair name |
| data.list[].orderType | string |  | Order type<br/>`limit`: Limit order<br/>`market`: Market order |
| data.list[].side | string |  | Trade side<br/>`buy`: Buy<br/>`sell`: Sell |
| data.list[].price | string |  | Order price |
| data.list[].qty | string |  | Order quantity |
| data.list[].cumExecQty | string |  | Cumulative filled quantity |
| data.list[].takeProfit | string |  | Take-profit price |
| data.list[].stopLoss | string |  | Stop-loss price |
| data.list[].status | string |  | Order status<br/>`partially_filled`: Partially filled<br/>`filled`: Fully filled<br/>`cancelled`: Canceled |
| data.list[].trxId | string |  | Request ID |
| data.list[].orderId | string |  | Order ID |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": {
    "list": [
      {
        "symbol": "XAUUSD",
        "orderType": "limit",
        "side": "buy",
        "price": "2620.00",
        "qty": "1",
        "cumExecQty": "1",
        "takeProfit": "2650.00",
        "stopLoss": "2600.00",
        "status": "filled",
        "trxId": "111111111111111111",
        "orderId": "111111111111111112"
      }
    ]
  }
}
```

## Get CFD Current Positions

`GET /api/v3/cfd/trade/current-positions`

Rate limit: 10/sec/UID <br/> Permission: UTA trade (read-only)

This endpoint is used to query real-time position information on a CFD account.

Operation ID: `cfdTradeGetCurrentPositions`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string |  | Trading pair name<br/>If not provided, current positions for all trading pairs are returned |
| subUid | query | string |  | Sub-account UID<br/>Used by a master account to query a sub-account's position list |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].positionId | string |  | Position ID |
| data[].symbol | string |  | Trading pair name |
| data[].orderType | string |  | Order type<br/>`limit`: Limit order<br/>`market`: Market order |
| data[].side | string |  | Trade side<br/>`buy`: Buy<br/>`sell`: Sell |
| data[].qty | string |  | Order quantity |
| data[].openPrice | string |  | Opening price |
| data[].takeProfit | string |  | Take-profit price |
| data[].stopLoss | string |  | Stop-loss price |
| data[].interest | string |  | Overnight interest |
| data[].unrealizedPnl | string |  | Unrealized profit and loss |
| data[].totalProfit | string |  | Total profit<br/>Total profit = Overnight interest + Unrealized profit and loss |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": [
    {
      "positionId": "111111111111111111",
      "symbol": "XAUUSD",
      "orderType": "limit",
      "side": "buy",
      "qty": "1",
      "openPrice": "2610.00",
      "takeProfit": "2650.00",
      "stopLoss": "2600.00",
      "interest": "0",
      "unrealizedPnl": "10.5",
      "totalProfit": "10.5"
    }
  ]
}
```


---

CFD 交易 API：下单、改单、撤单、平仓、查询委托与持仓。

版本: 1.0.0

## 服务地址

- `https://api.bitget.com`

## 接口列表

- `POST /api/v3/cfd/trade/place-order` — 下单
- `POST /api/v3/cfd/trade/modify-order` — 改单
- `POST /api/v3/cfd/trade/cancel-order` — 撤单
- `POST /api/v3/cfd/trade/cancel-all` — 撤销全部订单
- `POST /api/v3/cfd/trade/close-positions` — 平仓
- `POST /api/v3/cfd/trade/close-all-positions` — 一键平仓
- `GET /api/v3/cfd/trade/unfilled-order` — 查询当前委托
- `GET /api/v3/cfd/trade/history-order` — 查询历史委托
- `GET /api/v3/cfd/trade/current-positions` — 查询持仓

## 下单

`POST /api/v3/cfd/trade/place-order`

限频：1次/秒/UID <br/> 权限：UTA 交易（读写）

用于在 CFD 账户下单。

Operation ID: `cfdTradePlaceOrder`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| symbol | string | 是 | 交易对名称 |
| orderType | string | 是 | 订单类型<br/>`limit`：限价单<br/>`market`：市价单 |
| side | string | 是 | 交易方向<br/>`buy`：买入<br/>`sell`：卖出 |
| price | string |  | 委托价格<br/>`orderType=limit` 时必填<br/>价格须为交易对精度的整数倍 |
| qty | string | 是 | 委托数量 |
| takeProfit | string |  | 止盈价格<br/>价格须为交易对精度的整数倍 |
| stopLoss | string |  | 止损价格<br/>价格须为交易对精度的整数倍 |

```json
{
  "symbol": "XAUUSD",
  "orderType": "market",
  "side": "buy",
  "qty": "1"
}
```

### 响应 200：成功响应

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.trxId | string |  | 请求 ID |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": {
    "trxId": "111111111111111111"
  }
}
```

## 改单

`POST /api/v3/cfd/trade/modify-order`

限频：1次/秒/UID <br/> 权限：UTA 交易（读写）

用于修改 CFD 账户的订单。

Operation ID: `cfdTradeModifyOrder`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| orderId | string | 是 | 订单 ID |
| price | string |  | 委托价格<br/>`orderType=limit` 时必填 |
| takeProfit | string |  | 止盈价格 |
| stopLoss | string |  | 止损价格 |

```json
{
  "orderId": "111111111111111111",
  "price": "2620.00"
}
```

### 响应 200：成功响应

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.orderId | string |  | 订单 ID |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": {
    "orderId": "111111111111111111"
  }
}
```

## 撤单

`POST /api/v3/cfd/trade/cancel-order`

限频：1次/秒/UID <br/> 权限：UTA 交易（读写）

用于撤销 CFD 账户的订单。

Operation ID: `cfdTradeCancelOrder`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| orderId | string | 是 | 订单 ID |

```json
{
  "orderId": "111111111111111111"
}
```

### 响应 200：成功响应

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data |  |  | null |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": null
}
```

## 撤销全部订单

`POST /api/v3/cfd/trade/cancel-all`

限频：1次/秒/UID <br/> 权限：UTA 交易（读写）

用于撤销 CFD 账户的全部订单。

Operation ID: `cfdTradeCancelAllOrders`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| symbol | string |  | 交易对名称<br/>不传则撤销全部订单<br/>传入则仅撤销指定交易对的订单 |

```json
{
  "symbol": "XAUUSD"
}
```

### 响应 200：成功响应

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data |  |  | null |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": null
}
```

## 平仓

`POST /api/v3/cfd/trade/close-positions`

限频：10次/秒/UID <br/> 权限：UTA 交易（读写）

用于平仓 CFD 账户的持仓，目前仅支持市价平仓。

Operation ID: `cfdTradeClosePositions`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| positionId | string | 是 | 持仓 ID<br/>可通过持仓列表接口获取 |
| qty | string | 是 | 委托数量 |

```json
{
  "positionId": "111111111111111111",
  "qty": "1"
}
```

### 响应 200：成功响应

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data |  |  | null |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": null
}
```

## 一键平仓

`POST /api/v3/cfd/trade/close-all-positions`

限频：1次/秒/UID <br/> 权限：UTA 交易（读写）

用于平仓 CFD 账户的全部持仓。

Operation ID: `cfdTradeCloseAllPositions`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| symbol | string |  | 交易对名称<br/>不传则平仓全部持仓<br/>传入则仅平仓指定交易对的持仓 |

```json
{
  "symbol": "XAUUSD"
}
```

### 响应 200：成功响应

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data |  |  | null |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": null
}
```

## 查询当前委托

`GET /api/v3/cfd/trade/unfilled-order`

限频：10次/秒/UID <br/> 权限：UTA 交易（只读）

查询 CFD 账户的未成交订单。

Operation ID: `cfdTradeGetUnfilledOrders`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | 交易对名称 |
| subUid | query | string |  | 子账户 UID<br/>用于查询子账户的未成交订单 |

### 响应 200：成功响应

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].symbol | string |  | 交易对名称 |
| data[].orderType | string |  | 订单类型<br/>`limit`：限价单<br/>`market`：市价单 |
| data[].side | string |  | 交易方向<br/>`buy`：买入<br/>`sell`：卖出 |
| data[].price | string |  | 委托价格 |
| data[].qty | string |  | 委托数量 |
| data[].takeProfit | string |  | 止盈价格 |
| data[].stopLoss | string |  | 止损价格 |
| data[].trxId | string |  | 请求 ID |
| data[].orderId | string |  | 订单 ID |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": [
    {
      "symbol": "XAUUSD",
      "orderType": "limit",
      "side": "buy",
      "price": "2620.00",
      "qty": "1",
      "takeProfit": "2650.00",
      "stopLoss": "2600.00",
      "trxId": "111111111111111111",
      "orderId": "111111111111111112"
    }
  ]
}
```

## 查询历史委托

`GET /api/v3/cfd/trade/history-order`

限频：10次/秒/UID <br/> 权限：UTA 交易（只读）

查询 CFD 账户的历史订单。

> 单次查询时间范围不超过 30 天，最大可回溯 90 天。

Operation ID: `cfdTradeGetOrderHistory`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | 交易对名称 |
| subUid | query | string |  | 子账户 UID<br/>用于查询子账户的历史订单 |
| startTime | query | string |  | 开始时间，Unix 毫秒时间戳 |
| endTime | query | string |  | 结束时间，Unix 毫秒时间戳 |
| limit | query | string |  | 每页条数，默认 10，范围 [1, 50]<br/>首页返回的条数可能大于传入的`limit`值 |
| pageNo | query | string |  | 页码 |
| cursor | query | string |  | 游标<br/>首页不需要传入<br/>第二页起必填，传入上一页返回结果中最后一条记录的`orderId` |

### 响应 200：成功响应

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.list | object[] |  | 列表 |
| data.list[].symbol | string |  | 交易对名称 |
| data.list[].orderType | string |  | 订单类型<br/>`limit`：限价单<br/>`market`：市价单 |
| data.list[].side | string |  | 交易方向<br/>`buy`：买入<br/>`sell`：卖出 |
| data.list[].price | string |  | 委托价格 |
| data.list[].qty | string |  | 委托数量 |
| data.list[].cumExecQty | string |  | 累计成交量 |
| data.list[].takeProfit | string |  | 止盈价格 |
| data.list[].stopLoss | string |  | 止损价格 |
| data.list[].status | string |  | 订单状态<br/>`partially_filled`：部分成交<br/>`filled`：完全成交<br/>`cancelled`：已撤销 |
| data.list[].trxId | string |  | 请求 ID |
| data.list[].orderId | string |  | 订单 ID |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": {
    "list": [
      {
        "symbol": "XAUUSD",
        "orderType": "limit",
        "side": "buy",
        "price": "2620.00",
        "qty": "1",
        "cumExecQty": "1",
        "takeProfit": "2650.00",
        "stopLoss": "2600.00",
        "status": "filled",
        "trxId": "111111111111111111",
        "orderId": "111111111111111112"
      }
    ]
  }
}
```

## 查询持仓

`GET /api/v3/cfd/trade/current-positions`

限频：10次/秒/UID <br/> 权限：UTA 交易（只读）

查询 CFD 账户的实时持仓信息。

Operation ID: `cfdTradeGetCurrentPositions`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string |  | 交易对名称<br/>不传则返回全部交易对的当前持仓 |
| subUid | query | string |  | 子账户 UID<br/>主账户用于查询子账户持仓列表 |

### 响应 200：成功响应

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].positionId | string |  | 持仓 ID |
| data[].symbol | string |  | 交易对名称 |
| data[].orderType | string |  | 订单类型<br/>`limit`：限价单<br/>`market`：市价单 |
| data[].side | string |  | 交易方向<br/>`buy`：买入<br/>`sell`：卖出 |
| data[].qty | string |  | 委托数量 |
| data[].openPrice | string |  | 开仓价格 |
| data[].takeProfit | string |  | 止盈价格 |
| data[].stopLoss | string |  | 止损价格 |
| data[].interest | string |  | 隔夜利息 |
| data[].unrealizedPnl | string |  | 未实现盈亏 |
| data[].totalProfit | string |  | 总收益<br/>总收益 = 隔夜利息 + 未实现盈亏 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": [
    {
      "positionId": "111111111111111111",
      "symbol": "XAUUSD",
      "orderType": "limit",
      "side": "buy",
      "qty": "1",
      "openPrice": "2610.00",
      "takeProfit": "2650.00",
      "stopLoss": "2600.00",
      "interest": "0",
      "unrealizedPnl": "10.5",
      "totalProfit": "10.5"
    }
  ]
}
```