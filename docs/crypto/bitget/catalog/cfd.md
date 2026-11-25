---
exchange: bitget
source_url: https://www.bitget.com/docs/catalog/cfd
api_type: REST
updated_at: 2026-11-25 19:02:25.492700
---

# CFD

CFD APIs: market data, trading, and account management.

版本: 1.0.0

## 服务地址

- `https://api.bitget.com`

## 接口列表

- `GET /api/v3/cfd/account/instruments` — Get Instruments
- `GET /api/v3/cfd/market/tickers` — Get Tickers
- `GET /api/v3/cfd/market/history-candlestick` — Get Kline/Candlestick History
- `POST /api/v3/cfd/trade/place-order` — Place CFD Order
- `POST /api/v3/cfd/trade/modify-order` — Modify CFD Order
- `POST /api/v3/cfd/trade/cancel-order` — Cancel CFD Order
- `POST /api/v3/cfd/trade/cancel-all` — Cancel All CFD Orders
- `POST /api/v3/cfd/trade/close-positions` — Close CFD Positions
- `POST /api/v3/cfd/trade/close-all-positions` — Close All CFD Positions
- `GET /api/v3/cfd/trade/unfilled-order` — Get CFD Unfilled Orders
- `GET /api/v3/cfd/trade/history-order` — Get CFD Order History
- `GET /api/v3/cfd/trade/current-positions` — Get CFD Current Positions
- `GET /api/v3/cfd/account/fund-detail` — Get CFD Fund Detail
- `POST /api/v3/cfd/account/transfer` — CFD Transfer
- `GET /api/v3/cfd/account/transfer-records` — Get CFD Transfer Records
- `GET /api/v3/cfd/account/financial-records` — Get CFD Financial Records

## Get Instruments

`GET /api/v3/cfd/account/instruments`

Rate limit: 10/sec/UID <br/> Permission: UTA trade (read-only)

Query tradable CFD instrument information. Authentication is required to access this endpoint.

Operation ID: `cfdAccountGetInstruments`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string |  | Trading pair name |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].symbol | string |  | Trading symbol |
| data[].onlineTime | string |  | Time the instrument was added |
| data[].currency | string |  | Base currency |
| data[].digits | string |  | Number of price decimal places |
| data[].spread | string |  | Spread |
| data[].contractSize | string |  | Contract size |
| data[].marginCurrency | string |  | Margin currency |
| data[].profitCurrency | string |  | Profit currency |
| data[].stopLevel | string |  | Stop level |
| data[].enable | string |  | Whether trading is enabled<br/>`0`: Trading disabled<br/>`1`: Close-only<br/>`2`: Trading enabled |
| data[].marginPercent | string |  | Margin percentage |
| data[].initialMargin | string |  | Initial margin |
| data[].marginMode | string |  | Margin model<br/>`Forex` / `CFD` |
| data[].maintMargin | string |  | Maintenance margin |
| data[].maintMarginRateBuy | string |  | Maintenance margin rate for the buy side<br/>The reciprocal of leverage; e.g., if leverage is 500, this value is 0.002 |
| data[].maintMarginRateSell | string |  | Maintenance margin rate for the sell side<br/>The reciprocal of leverage; e.g., if leverage is 500, this value is 0.002 |
| data[].initialMarginRateBuy | string |  | Initial margin rate for the buy side |
| data[].initialMarginRateSell | string |  | Initial margin rate for the sell side |
| data[].maxVolume | string |  | Maximum tradable volume |
| data[].minVolume | string |  | Minimum tradable volume |
| data[].stepVolume | string |  | Volume step size |
| data[].priceCurrency | string |  | Quote currency |
| data[].tickSize | string |  | Minimum price increment |
| data[].tickValue | string |  | Value of the minimum price increment |
| data[].leverage | string |  | Leverage |
| data[].tradeTime | string |  | Tradable hours |
| data[].commissionType | string |  | Commission type<br/>`0`: Charged per lot<br/>`1`: Charged as a percentage of trade value |
| data[].commissionRate | string |  | Commission rate<br/>If charged per lot, this is the commission amount per lot<br/>If charged as a percentage of trade value, this is a percentage value<br/>Default `0` |
| data[].symbolCategory | string |  | Instrument category (the symbol name without its suffix)<br/>e.g., for `XAUUSD.s`, symbolCategory = `"XAUUSD"` |
| data[].exchangeRate | string |  | Exchange rate of priceCurrency against USD |
| data[].marginUsdRate | string |  | Exchange rate of marginCurrency against USD |
| data[].currentTimezone | string |  | Instrument's trading timezone, as a UTC offset in hours, e.g. `+2` means UTC+2 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": [
    {
      "symbol": "XAUUSD",
      "onlineTime": "1740000000000",
      "currency": "USD",
      "digits": "2",
      "spread": "3",
      "contractSize": "100",
      "marginCurrency": "USD",
      "profitCurrency": "USD",
      "stopLevel": "0",
      "enable": "2",
      "marginPercent": "1",
      "initialMargin": "200",
      "marginMode": "Forex",
      "maintMargin": "100",
      "maintMarginRateBuy": "0.002",
      "maintMarginRateSell": "0.002",
      "initialMarginRateBuy": "0.004",
      "initialMarginRateSell": "0.004",
      "maxVolume": "100",
      "minVolume": "0.01",
      "stepVolume": "0.01",
      "priceCurrency": "USD",
      "tickSize": "0.01",
      "tickValue": "1",
      "leverage": "500",
      "tradeTime": "24/5",
      "commissionType": "0",
      "commissionRate": "0",
      "symbolCategory": "XAUUSD",
      "exchangeRate": "1",
      "marginUsdRate": "1",
      "currentTimezone": "+2"
    }
  ]
}
```

## Get Tickers

`GET /api/v3/cfd/market/tickers`

Rate limit: 10/sec/UID <br/> Permission: UTA trade (read-only)

Query ticker information for a CFD trading pair.

Operation ID: `cfdMarketGetTickers`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string |  | Trading pair name |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].symbol | string |  | Trading pair name |
| data[].quoteTime | string |  | Quote time |
| data[].askOpenPriceChange | string |  | Change in the ask opening price<br/>Shown as a decimal, e.g. 0.1 represents 10% |
| data[].bidOpenPriceChange | string |  | Change in the bid opening price<br/>Shown as a decimal, e.g. 0.1 represents 10% |
| data[].highPrice | string |  | Today's highest price |
| data[].lowPrice | string |  | Today's lowest price |
| data[].ask1 | string |  | Best ask price |
| data[].bid1 | string |  | Best bid price |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": [
    {
      "symbol": "XAUUSD",
      "quoteTime": "1740000000000",
      "askOpenPriceChange": "0.001",
      "bidOpenPriceChange": "0.001",
      "highPrice": "2650.12",
      "lowPrice": "2610.34",
      "ask1": "2620.60",
      "bid1": "2620.50"
    }
  ]
}
```

## Get Kline/Candlestick History

`GET /api/v3/cfd/market/history-candlestick`

Rate limit: 10/sec/UID <br/> Permission: UTA trade (read-only)

Query historical candlestick data for a CFD trading pair.

Operation ID: `cfdMarketGetHistoryCandlestick`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | Trading pair, e.g. `XAUUSD` |
| interval | query | string | 是 | Granularity<br/>`1m`, `15m`, `1h`, `4h`, `1d` |
| side | query | string | 是 | Trade side<br/>`buy`: Buy side<br/>`sell`: Sell side |
| startTime | query | string |  | Start time; returns candlesticks after this time<br/>A Unix millisecond timestamp, e.g. `1672410780000`<br/>Maximum query range is 90 days |
| endTime | query | string |  | End time; returns candlesticks before this time<br/>A Unix millisecond timestamp, e.g. `1672410780000`<br/>Maximum query range is 90 days |
| limit | query | string |  | Number of entries per page<br/>Default: 100, maximum: 100 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | string[][] |  | Each element is an array: [timestamp, open, high, low, close] |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": [
    [
      "1597026383085",
      "2610.34",
      "2650.12",
      "2605.10",
      "2620.55"
    ]
  ]
}
```

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

## Get CFD Fund Detail

`GET /api/v3/cfd/account/fund-detail`

Rate limit: 1/sec/UID <br/> Permission: UTA account (read-only)

This endpoint is used to query the fund details of a CFD account.

Operation ID: `cfdAccountGetFundDetail`

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.leverage | string |  | Leverage |
| data.balance | string |  | Account balance<br/>Excludes credit |
| data.credit | string |  | Credit line |
| data.marginStopOut | string |  | Margin stop-out level (%) |
| data.marginUsed | string |  | Margin used |
| data.marginCall | string |  | Margin call level (%) |
| data.marginFree | string |  | Free margin |
| data.marginLevel | string |  | Margin level (%) |
| data.equity | string |  | Account equity<br/>Includes credit |
| data.pnl | string |  | Current unrealized profit and loss |
| data.status | string |  | Account status |
| data.swap | string |  | Overnight interest<br/>Also referred to as storage fee, swap fee, or rollover fee |
| data.frozen | string |  | Frozen amount |
| data.currency | string |  | Trading account currency |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": {
    "leverage": "500",
    "balance": "10000",
    "credit": "0",
    "marginStopOut": "50",
    "marginUsed": "200",
    "marginCall": "100",
    "marginFree": "9800",
    "marginLevel": "5000",
    "equity": "10010.5",
    "pnl": "10.5",
    "status": "normal",
    "swap": "0",
    "frozen": "0",
    "currency": "USD"
  }
}
```

## CFD Transfer

`POST /api/v3/cfd/account/transfer`

Rate limit: 1/sec/UID <br/> Permission: UTA account (read & write)

This endpoint is used to deposit or withdraw funds to/from a CFD account.

Operation ID: `cfdAccountTransfer`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| coin | string | 是 | Coin to transfer |
| amount | string | 是 | Amount to transfer |
| accountType | string | 是 | Account type<br/>`funding`: Spot/Funding account<br/>`uta`: Unified Trading Account |
| direction | string | 是 | Transfer direction<br/>`in`: Deposit into the CFD account<br/>`out`: Withdraw from the CFD account |

```json
{
  "coin": "USDT",
  "amount": "100",
  "accountType": "uta",
  "direction": "in"
}
```

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
    "transferId": "111111111111111111"
  }
}
```

## Get CFD Transfer Records

`GET /api/v3/cfd/account/transfer-records`

Rate limit: 1/sec/UID <br/> Permission: UTA account (read-only)

This endpoint is used to query the transfer records of a CFD account.

> The query span per request must not exceed 30 days. The maximum lookback period is 90 days.

Operation ID: `cfdAccountGetTransferRecords`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| transferId | query | string |  | Transfer ID |
| subUid | query | string |  | Sub-account UID<br/>Used by a master account to query a sub-account's transfer records |
| startTime | query | string |  | Start time, Unix millisecond timestamp |
| endTime | query | string |  | End time, Unix millisecond timestamp |
| direction | query | string |  | Transfer direction<br/>`in`: Deposit into the CFD account<br/>`out`: Withdraw from the CFD account<br/>If not provided, records for all directions are returned |
| limit | query | string |  | Number of entries per page<br/>Default: 10, range [1, 50] |
| cursor | query | string |  | Cursor ID |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.list | object[] |  | List |
| data.list[].transferId | string |  | Transfer ID |
| data.list[].coin | string |  | Coin transferred |
| data.list[].amount | string |  | Amount transferred |
| data.list[].direction | string |  | Transfer direction<br/>`in`: Deposit into the CFD account<br/>`out`: Withdraw from the CFD account |
| data.list[].status | string |  | Status<br/>`ongoing`: In progress<br/>`failed`: Failed<br/>`success`: Successful |
| data.list[].accountType | string |  | Account type<br/>`funding`: Spot/Funding account<br/>`uta`: Unified Trading Account |
| data.list[].createdTime | string |  | Creation time, Unix millisecond timestamp |
| data.list[].updatedTime | string |  | Update time, Unix millisecond timestamp |
| data.cursor | string |  | Cursor ID |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": {
    "list": [
      {
        "transferId": "111111111111111111",
        "coin": "USDT",
        "amount": "100",
        "direction": "in",
        "status": "success",
        "accountType": "uta",
        "createdTime": "1740000000000",
        "updatedTime": "1740000000000"
      }
    ],
    "cursor": "111111111111111112"
  }
}
```

## Get CFD Financial Records

`GET /api/v3/cfd/account/financial-records`

Rate limit: 1/sec/UID <br/> Permission: UTA account (read-only)

This endpoint is used to query the financial records of a CFD account.

> The query span per request must not exceed 30 days. The maximum lookback period is 90 days.

Operation ID: `cfdAccountGetFinancialRecords`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| type | query | string |  | Financial record type |
| startTime | query | string |  | Start time, Unix millisecond timestamp |
| endTime | query | string |  | End time, Unix millisecond timestamp |
| limit | query | string |  | Number of entries per page<br/>Default: 10, range [1, 50] |
| cursor | query | string |  | Cursor ID |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].id | integer |  | Record ID |
| data[].symbol | string |  | Trading pair name |
| data[].side | integer |  | Trade side<br/>`buy`: Buy<br/>`sell`: Sell |
| data[].qty | number |  | Trade quantity |
| data[].swap | number |  | Swap fee |
| data[].fee | number |  | Commission fee |
| data[].cashFlow | number |  | Cash flow<br/>(Settled PnL, deposits/withdrawals, compensation amounts, etc.); excludes commission fee and swap fee |
| data[].balanceBefore | number |  | Balance before the change |
| data[].balanceChange | number |  | Balance change<br/>cashFlow + swap + fee |
| data[].balanceAfter | number |  | Balance after the change |
| data[].creditBefore | number |  | Credit before the change |
| data[].creditChange | number |  | Credit change |
| data[].creditAfter | number |  | Credit after the change |
| data[].openPrice | number |  | Opening price |
| data[].closePrice | number |  | Closing price |
| data[].orderId | integer |  | Order ID |
| data[].ts | integer |  | Record time |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": [
    {
      "id": 1,
      "symbol": "XAUUSD",
      "side": 1,
      "qty": 1,
      "swap": 0,
      "fee": 0.5,
      "cashFlow": 10.5,
      "balanceBefore": 9989.5,
      "balanceChange": 10,
      "balanceAfter": 9999.5,
      "creditBefore": 0,
      "creditChange": 0,
      "creditAfter": 0,
      "openPrice": 2610,
      "closePrice": 2620,
      "orderId": 111111111111111104,
      "ts": 1740000000000.0
    }
  ]
}
```


---

CFD API：行情数据、交易及账户管理接口。

版本: 1.0.0

## 服务地址

- `https://api.bitget.com`

## 接口列表

- `GET /api/v3/cfd/account/instruments` — 获取产品信息
- `GET /api/v3/cfd/market/tickers` — 获取行情数据
- `GET /api/v3/cfd/market/history-candlestick` — 获取 K 线数据
- `POST /api/v3/cfd/trade/place-order` — 下单
- `POST /api/v3/cfd/trade/modify-order` — 改单
- `POST /api/v3/cfd/trade/cancel-order` — 撤单
- `POST /api/v3/cfd/trade/cancel-all` — 撤销全部订单
- `POST /api/v3/cfd/trade/close-positions` — 平仓
- `POST /api/v3/cfd/trade/close-all-positions` — 一键平仓
- `GET /api/v3/cfd/trade/unfilled-order` — 查询当前委托
- `GET /api/v3/cfd/trade/history-order` — 查询历史委托
- `GET /api/v3/cfd/trade/current-positions` — 查询持仓
- `GET /api/v3/cfd/account/fund-detail` — 查询账户资金
- `POST /api/v3/cfd/account/transfer` — CFD 划转
- `GET /api/v3/cfd/account/transfer-records` — 查询划转记录
- `GET /api/v3/cfd/account/financial-records` — 查询财务记录

## 获取产品信息

`GET /api/v3/cfd/account/instruments`

限频：10次/秒/UID <br/> 权限：UTA 交易（只读）

查询可交易的 CFD 产品信息。该接口需要鉴权才能访问。

Operation ID: `cfdAccountGetInstruments`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string |  | 交易对名称 |

### 响应 200：成功响应

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].symbol | string |  | 交易品种名称 |
| data[].onlineTime | string |  | 产品上线时间 |
| data[].currency | string |  | 基础货币 |
| data[].digits | string |  | 价格小数位数 |
| data[].spread | string |  | 点差 |
| data[].contractSize | string |  | 合约大小 |
| data[].marginCurrency | string |  | 保证金货币 |
| data[].profitCurrency | string |  | 盈利货币 |
| data[].stopLevel | string |  | 止损水平 |
| data[].enable | string |  | 是否可交易<br/>`0`：禁止交易<br/>`1`：仅可平仓<br/>`2`：可交易 |
| data[].marginPercent | string |  | 保证金比例 |
| data[].initialMargin | string |  | 初始保证金 |
| data[].marginMode | string |  | 保证金模式<br/>`Forex` / `CFD` |
| data[].maintMargin | string |  | 维持保证金 |
| data[].maintMarginRateBuy | string |  | 买方维持保证金率<br/>等于杠杆的倒数，如杠杆 500 则该值为 0.002 |
| data[].maintMarginRateSell | string |  | 卖方维持保证金率<br/>等于杠杆的倒数，如杠杆 500 则该值为 0.002 |
| data[].initialMarginRateBuy | string |  | 买方初始保证金率 |
| data[].initialMarginRateSell | string |  | 卖方初始保证金率 |
| data[].maxVolume | string |  | 最大可交易量 |
| data[].minVolume | string |  | 最小可交易量 |
| data[].stepVolume | string |  | 数量步长 |
| data[].priceCurrency | string |  | 计价货币 |
| data[].tickSize | string |  | 最小价格变动单位 |
| data[].tickValue | string |  | 最小价格变动单位对应的价值 |
| data[].leverage | string |  | 杠杆 |
| data[].tradeTime | string |  | 可交易时段 |
| data[].commissionType | string |  | 佣金类型<br/>`0`：按手数收取<br/>`1`：按交易额百分比收取 |
| data[].commissionRate | string |  | 佣金费率<br/>按手数收取时为每手佣金金额；按交易额百分比收取时为百分比值<br/>默认 `0` |
| data[].symbolCategory | string |  | 产品分类（去掉后缀的品种名称）<br/>如 `XAUUSD.s` 的 symbolCategory 为 `"XAUUSD"` |
| data[].exchangeRate | string |  | priceCurrency 对 USD 的汇率 |
| data[].marginUsdRate | string |  | marginCurrency 对 USD 的汇率 |
| data[].currentTimezone | string |  | 产品交易时区，以 UTC 偏移小时数表示，如 `+2` 表示 UTC+2 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": [
    {
      "symbol": "XAUUSD",
      "onlineTime": "1740000000000",
      "currency": "USD",
      "digits": "2",
      "spread": "3",
      "contractSize": "100",
      "marginCurrency": "USD",
      "profitCurrency": "USD",
      "stopLevel": "0",
      "enable": "2",
      "marginPercent": "1",
      "initialMargin": "200",
      "marginMode": "Forex",
      "maintMargin": "100",
      "maintMarginRateBuy": "0.002",
      "maintMarginRateSell": "0.002",
      "initialMarginRateBuy": "0.004",
      "initialMarginRateSell": "0.004",
      "maxVolume": "100",
      "minVolume": "0.01",
      "stepVolume": "0.01",
      "priceCurrency": "USD",
      "tickSize": "0.01",
      "tickValue": "1",
      "leverage": "500",
      "tradeTime": "24/5",
      "commissionType": "0",
      "commissionRate": "0",
      "symbolCategory": "XAUUSD",
      "exchangeRate": "1",
      "marginUsdRate": "1",
      "currentTimezone": "+2"
    }
  ]
}
```

## 获取行情数据

`GET /api/v3/cfd/market/tickers`

限频：10次/秒/UID <br/> 权限：UTA 交易（只读）

查询 CFD 交易对的行情信息。

Operation ID: `cfdMarketGetTickers`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string |  | 交易对名称 |

### 响应 200：成功响应

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].symbol | string |  | 交易对名称 |
| data[].quoteTime | string |  | 报价时间 |
| data[].askOpenPriceChange | string |  | ask开盘涨跌幅<br/>小数形式展示，如0.1代表10% |
| data[].bidOpenPriceChange | string |  | bid开盘涨跌幅<br/>小数形式展示，如0.1代表10% |
| data[].highPrice | string |  | 今日最高价 |
| data[].lowPrice | string |  | 今日最低价 |
| data[].ask1 | string |  | 最优卖价 |
| data[].bid1 | string |  | 最优买价 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": [
    {
      "symbol": "XAUUSD",
      "quoteTime": "1740000000000",
      "askOpenPriceChange": "0.001",
      "bidOpenPriceChange": "0.001",
      "highPrice": "2650.12",
      "lowPrice": "2610.34",
      "ask1": "2620.60",
      "bid1": "2620.50"
    }
  ]
}
```

## 获取 K 线数据

`GET /api/v3/cfd/market/history-candlestick`

限频：10次/秒/UID <br/> 权限：UTA 交易（只读）

查询 CFD 交易对的历史 K 线数据。

Operation ID: `cfdMarketGetHistoryCandlestick`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | 交易对，如 `XAUUSD` |
| interval | query | string | 是 | 时间粒度<br/>`1m`、`15m`、`1h`、`4h`、`1d` |
| side | query | string | 是 | 交易方向<br/>`buy`：买方<br/>`sell`：卖方 |
| startTime | query | string |  | 开始时间，Unix 毫秒时间戳，如 `1672410780000`<br/>单次查询范围不超过 90 天 |
| endTime | query | string |  | 结束时间，Unix 毫秒时间戳，如 `1672410780000`<br/>单次查询范围不超过 90 天 |
| limit | query | string |  | 每页条数，默认 100，最大 100 |

### 响应 200：成功响应

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | string[][] |  | 每个元素为数组：[时间戳, 开盘价, 最高价, 最低价, 收盘价] |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": [
    [
      "1597026383085",
      "2610.34",
      "2650.12",
      "2605.10",
      "2620.55"
    ]
  ]
}
```

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

## 查询账户资金

`GET /api/v3/cfd/account/fund-detail`

限频：1次/秒/UID <br/> 权限：UTA 账户（只读）

查询 CFD 账户的资金详情。

Operation ID: `cfdAccountGetFundDetail`

### 响应 200：成功响应

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.leverage | string |  | 杠杆 |
| data.balance | string |  | 账户余额<br/>不含信用额度 |
| data.credit | string |  | 信用额度 |
| data.marginStopOut | string |  | 强平保证金水平（%） |
| data.marginUsed | string |  | 已用保证金 |
| data.marginCall | string |  | 预警保证金水平（%） |
| data.marginFree | string |  | 可用保证金 |
| data.marginLevel | string |  | 保证金水平（%） |
| data.equity | string |  | 账户净值<br/>含信用额度 |
| data.pnl | string |  | 当前未实现盈亏 |
| data.status | string |  | 账户状态 |
| data.swap | string |  | 隔夜利息<br/>即库存费、掉期费或过夜费 |
| data.frozen | string |  | 冻结金额 |
| data.currency | string |  | 交易账户货币 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": {
    "leverage": "500",
    "balance": "10000",
    "credit": "0",
    "marginStopOut": "50",
    "marginUsed": "200",
    "marginCall": "100",
    "marginFree": "9800",
    "marginLevel": "5000",
    "equity": "10010.5",
    "pnl": "10.5",
    "status": "normal",
    "swap": "0",
    "frozen": "0",
    "currency": "USD"
  }
}
```

## CFD 划转

`POST /api/v3/cfd/account/transfer`

限频：1次/秒/UID <br/> 权限：UTA 账户（读写）

用于向/从 CFD 账户充值或提取资金。

Operation ID: `cfdAccountTransfer`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| coin | string | 是 | 划转币种 |
| amount | string | 是 | 划转数量 |
| accountType | string | 是 | 账户类型<br/>`funding`：现货/资金账户<br/>`uta`：统一交易账户 |
| direction | string | 是 | 划转方向<br/>`in`：充值到 CFD 账户<br/>`out`：从 CFD 账户提取 |

```json
{
  "coin": "USDT",
  "amount": "100",
  "accountType": "uta",
  "direction": "in"
}
```

### 响应 200：成功响应

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.transferId | string |  | 划转 ID |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": {
    "transferId": "111111111111111111"
  }
}
```

## 查询划转记录

`GET /api/v3/cfd/account/transfer-records`

限频：1次/秒/UID <br/> 权限：UTA 账户（只读）

查询 CFD 账户的划转记录。

> 单次查询时间范围不超过 30 天，最大可回溯 90 天。

Operation ID: `cfdAccountGetTransferRecords`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| transferId | query | string |  | 划转 ID |
| subUid | query | string |  | 子账户 UID<br/>主账户用于查询子账户的划转记录 |
| startTime | query | string |  | 开始时间，Unix 毫秒时间戳 |
| endTime | query | string |  | 结束时间，Unix 毫秒时间戳 |
| direction | query | string |  | 划转方向<br/>`in`：充值到 CFD 账户<br/>`out`：从 CFD 账户提取<br/>不传则返回全部方向记录 |
| limit | query | string |  | 每页条数，默认 10，范围 [1, 50] |
| cursor | query | string |  | 游标 ID |

### 响应 200：成功响应

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.list | object[] |  | 列表 |
| data.list[].transferId | string |  | 划转 ID |
| data.list[].coin | string |  | 划转币种 |
| data.list[].amount | string |  | 划转数量 |
| data.list[].direction | string |  | 划转方向<br/>`in`：充值到 CFD 账户<br/>`out`：从 CFD 账户提取 |
| data.list[].status | string |  | 状态<br/>`ongoing`：处理中<br/>`failed`：失败<br/>`success`：成功 |
| data.list[].accountType | string |  | 账户类型<br/>`funding`：现货/资金账户<br/>`uta`：统一交易账户 |
| data.list[].createdTime | string |  | 创建时间，Unix 毫秒时间戳 |
| data.list[].updatedTime | string |  | 更新时间，Unix 毫秒时间戳 |
| data.cursor | string |  | 游标 ID |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": {
    "list": [
      {
        "transferId": "111111111111111111",
        "coin": "USDT",
        "amount": "100",
        "direction": "in",
        "status": "success",
        "accountType": "uta",
        "createdTime": "1740000000000",
        "updatedTime": "1740000000000"
      }
    ],
    "cursor": "111111111111111112"
  }
}
```

## 查询财务记录

`GET /api/v3/cfd/account/financial-records`

限频：1次/秒/UID <br/> 权限：UTA 账户（只读）

查询 CFD 账户的财务记录。

> 单次查询时间范围不超过 30 天，最大可回溯 90 天。

Operation ID: `cfdAccountGetFinancialRecords`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| type | query | string |  | 财务记录类型 |
| startTime | query | string |  | 开始时间，Unix 毫秒时间戳 |
| endTime | query | string |  | 结束时间，Unix 毫秒时间戳 |
| limit | query | string |  | 每页条数，默认 10，范围 [1, 50] |
| cursor | query | string |  | 游标 ID |

### 响应 200：成功响应

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].id | integer |  | 记录 ID |
| data[].symbol | string |  | 交易对名称 |
| data[].side | integer |  | 交易方向<br/>`buy`：买入<br/>`sell`：卖出 |
| data[].qty | number |  | 成交数量 |
| data[].swap | number |  | 掉期费 |
| data[].fee | number |  | 佣金 |
| data[].cashFlow | number |  | 现金流<br/>（已结算盈亏、充值/提现、补偿金额等），不含佣金和掉期费 |
| data[].balanceBefore | number |  | 变动前余额 |
| data[].balanceChange | number |  | 余额变动量<br/>cashFlow + swap + fee |
| data[].balanceAfter | number |  | 变动后余额 |
| data[].creditBefore | number |  | 变动前信用额度 |
| data[].creditChange | number |  | 信用额度变动量 |
| data[].creditAfter | number |  | 变动后信用额度 |
| data[].openPrice | number |  | 开仓价格 |
| data[].closePrice | number |  | 平仓价格 |
| data[].orderId | integer |  | 订单 ID |
| data[].ts | integer |  | 记录时间 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": [
    {
      "id": 1,
      "symbol": "XAUUSD",
      "side": 1,
      "qty": 1,
      "swap": 0,
      "fee": 0.5,
      "cashFlow": 10.5,
      "balanceBefore": 9989.5,
      "balanceChange": 10,
      "balanceAfter": 9999.5,
      "creditBefore": 0,
      "creditChange": 0,
      "creditAfter": 0,
      "openPrice": 2610,
      "closePrice": 2620,
      "orderId": 111111111111111104,
      "ts": 1740000000000.0
    }
  ]
}
```