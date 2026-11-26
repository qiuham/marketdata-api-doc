---
exchange: bitget
source_url: https://www.bitget.com/docs/catalog/classic-spot-trade
api_type: REST
updated_at: 2026-11-26 19:03:59.791556
---

# Classic Spot Trade API

Spot trade endpoints — place, cancel, and query orders and fills.

版本: 1.0.0

## 服务地址

- `https://api.bitget.com`

## 接口列表

- `POST /api/v2/spot/trade/place-order` — Place Order
- `POST /api/v2/spot/trade/batch-orders` — Batch Place Orders
- `POST /api/v2/spot/trade/cancel-order` — Cancel Order
- `POST /api/v2/spot/trade/batch-cancel-order` — Batch Cancel Orders
- `POST /api/v2/spot/trade/cancel-symbol-order` — Cancel Order by Symbol
- `POST /api/v2/spot/trade/cancel-replace-order` — Cancel an Existing Order and Send a New Order
- `POST /api/v2/spot/trade/batch-cancel-replace-order` — Batch Cancel Existing Order and Send New Orders
- `GET /api/v2/spot/trade/orderInfo` — Get Order Info
- `GET /api/v2/spot/trade/unfilled-orders` — Get Current Orders
- `GET /api/v2/spot/trade/history-orders` — Get History Orders
- `GET /api/v2/spot/trade/fills` — Get Fills

## Place Order

`POST /api/v2/spot/trade/place-order`

Rate limit: 10 requests/second/UID

Rate limit: 1 request/second/UID for copy trading traders

Place Order

- **API Broker rebate identifier**: The following code block needs to be added to the HTTP Header of the request.

  > "X-CHANNEL-API-CODE":"your-channel-api-code"

Operation ID: `classicSpotTradePlaceOrder`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| symbol | string | 是 | Trading pair name, e.g. BTCUSDT |
| side | string | 是 | Order Direction<br><br>`buy`: Buy<br><br>`sell`: Sell |
| orderType | string | 是 | Order type<br><br>`limit`: Limit order<br><br>`market`: Market order |
| force | string | 是 | Execution strategy(It is invalid when `orderType` is `market`)<br><br>`gtc`: Normal limit order, good till cancelled<br><br>`post_only`: Post only<br><br>`fok`: Fill or kill<br><br>`ioc`: Immediate or cancel |
| price | string |  | Limit price |
| size | string | 是 | Amount. For Limit and Market-Sell orders, it represents the number of base coins. For Market-Buy orders, it represents the number of quote coins. |
| clientOid | string |  | Customed order ID. It's invalid when `tpslType` is `tpsl` |
| triggerPrice | string |  | SPOT TP/SL trigger price, only required in SPOT TP/SL order |
| tpslType | string |  | Order type<br><br>`normal`: SPOT order(default)<br><br>`tpsl`: SPOT TP/SL order |
| requestTime | string |  | Request Time, Unix millisecond timestamp |
| receiveWindow | string |  | Valid time window, Unix millisecond timestamp |
| stpMode | string |  | STP Mode(Self Trade Prevention)<br><br>`none`: not setting STP(default)<br><br>`cancel_taker`: cancel taker order<br><br>`cancel_maker`: cancel maker order<br><br>`cancel_both`: cancel both of taker and maker orders |
| presetTakeProfitPrice | string |  | Take profit price. It's invalid when `tpslType` is `tpsl` |
| executeTakeProfitPrice | string |  | Take profit execute price. It's invalid when `tpslType` is `tpsl` |
| presetStopLossPrice | string |  | Stop loss price. It's invalid when `tpslType` is `tpsl` |
| executeStopLossPrice | string |  | Stop loss execute price. It's invalid when `tpslType` is `tpsl` |

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
    "orderId": "1001",
    "clientOid": "121211212122"
  }
}
```

## Batch Place Orders

`POST /api/v2/spot/trade/batch-orders`

Frequency limit: 5 times/1s (UID)

Trader frequency limit: 1 times/1s (UID)

Place Orders in Batch

- **API Broker rebate identifier**: The following code block needs to be added to the HTTP Header of the request.

  > "X-CHANNEL-API-CODE":"your-channel-api-code"

Operation ID: `classicSpotTradeBatchPlaceOrders`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| batchMode | string |  | Batch order mode<br><br>`single` single currency mode, default single currency mode<br><br>`multiple` cross-currency mode.<br><br>If single mode, the symbol in orderList will be ignored.<br><br>If multiple mode, the symbol in orderList is not allowed to be null, and the symbol in orderList is required. The symbol outside orderList will be ignored. |
| orderList | object[] | 是 | Collection of placing orders，maximum length: 50 |
| orderList[].symbol | string |  | Trading pair name, e.g. BTCUSDT. Required when batchMode is multiple. |
| orderList[].side | string |  | Order Direction<br><br>`buy`: Buy<br><br>`sell`: Sell |
| orderList[].orderType | string |  | Order type<br><br>`limit`: Limit order<br><br>`market`: Market order |
| orderList[].force | string |  | Execution strategy(It will be invalid when `orderType` is `market`)<br><br>`gtc`: Normal limit order, good till cancelled<br><br>`post_only`: Post only<br><br>`fok`: Fill or kill<br><br>`ioc`: Immediate or cancel |
| orderList[].price | string |  | Limit price |
| orderList[].size | string |  | Amount. For Limit and Market-Sell orders, it represents the number of base coins. For Market-Buy orders, it represents the number of quote coins. |
| orderList[].clientOid | string |  | Customed order ID |
| orderList[].stpMode | string |  | STP Mode, default `none`<br><br>`none` not setting STP<br><br>`cancel_taker` cancel taker order<br><br>`cancel_maker` cancel maker order<br><br>`cancel_both` cancel both of taker and maker orders |
| orderList[].presetTakeProfitPrice | string |  | Take profit price |
| orderList[].executeTakeProfitPrice | string |  | Take profit execute price |
| orderList[].presetStopLossPrice | string |  | Stop loss price |
| orderList[].executeStopLossPrice | string |  | Stop loss execute price |
| symbol | string |  | Trading pair name, e.g. BTCUSDT. Used when batchMode is single. |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.successList | object[] |  | Successful order number |
| data.successList[].orderId | string |  | Order ID |
| data.successList[].clientOid | string |  | Client Order ID |
| data.failureList | object[] |  | Failed order number |
| data.failureList[].orderId | string |  | Order ID |
| data.failureList[].clientOid | string |  | Client Order ID |
| data.failureList[].errorMsg | string |  | Error information |
| data.failureList[].errorCode | string |  | Error code |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1666336231317,
  "data": {
    "successList": [
      {
        "orderId": "121211212122",
        "clientOid": "1"
      }
    ],
    "failureList": [
      {
        "orderId": "121211212122",
        "clientOid": "1",
        "errorMsg": "clientOrderId duplicate",
        "errorCode": "43118"
      }
    ]
  }
}
```

## Cancel Order

`POST /api/v2/spot/trade/cancel-order`

Frequency limit:10 times/1s (UID)

Cancel Order

Operation ID: `classicSpotTradeCancelOrder`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| symbol | string |  | Trading pair name, e.g. BTCUSDT. It is not required when tpslType is `tpsl` |
| tpslType | string |  | order type, deafult:`normal`<br><br>`normal` spot order<br><br>`tpsl` spot tpsl order |
| orderId | string |  | Order ID. Either orderId or clientOid is required. It's required when tpslType is `tpsl` |
| clientOid | string |  | Client Order ID. Either orderId or clientOid is required |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.orderId | string |  | Order ID |
| data.clientOid | string |  | Client Order ID |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1234567891234,
  "data": {
    "orderId": "121211212122",
    "clientOid": "xx001"
  }
}
```

## Batch Cancel Orders

`POST /api/v2/spot/trade/batch-cancel-order`

Frequency limit:10 times/1s (UID)

Cancel Orders in Batch

- For batch cancellation (simultaneously revoking multiple orders for the same symbol), it is not permitted to mix the use of orderId and clientOid. The identifiers used must be consistent across all orders in the batch. Otherwise, orders that only submit a clientOid will fail to be cancelled.

Operation ID: `classicSpotTradeBatchCancelOrders`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| symbol | string |  | Trading pair name, e.g. BTCUSDT |
| batchMode | string |  | Batch order mode<br><br>`single` single currency mode, default single currency mode<br><br>`multiple` cross-currency mode.<br><br>If single mode, the symbol in orderList will be ignored.<br><br>If multiple mode, the symbol in orderList is not allowed to be null, and the symbol in orderList is required. The symbol outside orderList will be ignored. |
| orderList | object[] | 是 | Order ID List, maximum length: 50 |
| orderList[].symbol | string |  | Trading pair name, e.g. BTCUSDT |
| orderList[].orderId | string |  | Order ID. Either orderId or clientOid is required. |
| orderList[].clientOid | string |  | Client Order ID. Either clientOid or orderId is required. |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.successList | object[] |  | Successful order number |
| data.successList[].orderId | string |  | Order ID |
| data.successList[].clientOid | string |  | Client Order ID |
| data.failureList | object[] |  | Failed order number |
| data.failureList[].orderId | string |  | Order ID |
| data.failureList[].clientOid | string |  | Client Order ID |
| data.failureList[].errorMsg | string |  | Error information |
| data.failureList[].errorCode | string |  | Error code |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695808949356,
  "data": {
    "successList": [
      {
        "orderId": "121211212122",
        "clientOid": "121211212122"
      }
    ],
    "failureList": [
      {
        "orderId": "121211212122",
        "clientOid": "xxx001",
        "errorMsg": "duplicate clientOrderId",
        "errorCode": "43118"
      }
    ]
  }
}
```

## Cancel Order by Symbol

`POST /api/v2/spot/trade/cancel-symbol-order`

Frequency limit: 5 times/1s (UID)

Cancel order by symbol

Operation ID: `classicSpotTradeCancelSymbolOrders`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| symbol | string | 是 | Trading pair name, e.g. BTCUSDT |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.symbol | string |  | Cancelled symbol (This request is executed asynchronously. If you need to know the result, please query the Get History Orders endpoint.) |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1698313139948,
  "data": {
    "symbol": "BGBUSDT"
  }
}
```

## Cancel an Existing Order and Send a New Order

`POST /api/v2/spot/trade/cancel-replace-order`

Rate limit: 5 requests/second/UID

Cancel an Existing Order and Send a New Order

- **API Broker rebate identifier**: The following code block needs to be added to the HTTP Header of the request.

  > "X-CHANNEL-API-CODE":"your-channel-api-code"

Operation ID: `classicSpotTradeCancelReplaceOrder`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| symbol | string | 是 | Trading pair name, e.g. BTCUSDT |
| price | string | 是 | Limit price |
| size | string | 是 | Amount，it represents the number of base coins. |
| clientOid | string |  | Client Order ID. Either orderId or clientOid is required |
| orderId | string |  | Order ID. Either orderId or clientOid is required |
| newClientOid | string |  | New customed order ID.<br><br>If newClientOid results in idempotency duplication, it may cause the old order to be successfully canceled but the new order placement to fail. |
| presetTakeProfitPrice | string |  | Take profit price |
| executeTakeProfitPrice | string |  | Take profit execute price |
| presetStopLossPrice | string |  | Stop loss price |
| executeStopLossPrice | string |  | Stop loss execute price |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.orderId | string |  | Order ID |
| data.clientOid | ['string', 'null'] |  | Client Order ID |
| data.success | string |  | operate success<br><br>`success`: success<br><br>`failure`: failure |
| data.msg | ['string', 'null'] |  | Failure reason |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1725345009763,
  "data": {
    "orderId": "xxxxxxxxxxxxxxx",
    "clientOid": null,
    "success": "success",
    "msg": null
  }
}
```

## Batch Cancel Existing Order and Send New Orders

`POST /api/v2/spot/trade/batch-cancel-replace-order`

Rate limit: 5 requests/second/UID

Cancel an Existing Order and Send a New Order

- **API Broker rebate identifier**: The following code block needs to be added to the HTTP Header of the request.

  > "X-CHANNEL-API-CODE":"your-channel-api-code"

Operation ID: `classicSpotTradeBatchCancelReplaceOrder`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| orderList | object[] | 是 | Collection of placing orders，maximum length: 50 |
| orderList[].symbol | string |  | Trading pair name, e.g. BTCUSDT |
| orderList[].price | string |  | Limit price |
| orderList[].size | string |  | Amount，it represents the number of base coins. |
| orderList[].clientOid | string |  | Client Order ID. Either orderId or clientOid is required |
| orderList[].orderId | string |  | Order ID. Either orderId or clientOid is required |
| orderList[].newClientOid | string |  | New customed order ID.<br><br>If newClientOid results in idempotency duplication, it may cause the old order to be successfully canceled but the new order placement to fail. |
| orderList[].presetTakeProfitPrice | string |  | Take profit price |
| orderList[].executeTakeProfitPrice | string |  | Take profit execute price |
| orderList[].presetStopLossPrice | string |  | Stop loss price |
| orderList[].executeStopLossPrice | string |  | Stop loss execute price |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].orderId | string |  | Order ID |
| data[].clientOid | ['string', 'null'] |  | Client Order ID |
| data[].success | string |  | operate success<br><br>`success`: success<br><br>`failure`: failure |
| data[].msg | string |  | Failure reason |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1725341809524,
  "data": [
    {
      "orderId": "xxxxxxxxxxxxxxxxxxxxxx",
      "clientOid": null,
      "success": "failure",
      "msg": "xxxxxx"
    }
  ]
}
```

## Get Order Info

`GET /api/v2/spot/trade/orderInfo`

Frequency limit: 20 times/1s (UID)

Get Order Info

Operation ID: `classicSpotTradeGetOrderInfo`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| orderId | query | string |  | Either Order ID or clientOids is required. |
| clientOid | query | string |  | Either Client customized ID or orderId is required. |
| requestTime | query | string |  | request Time Unix millisecond timestamp |
| receiveWindow | query | string |  | valid window period Unix millisecond timestamp |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].userId | string |  | Account id |
| data[].symbol | string |  | Trading pair name |
| data[].orderId | string |  | Order ID |
| data[].clientOid | string |  | Customized ID |
| data[].price | string |  | Order price |
| data[].size | string |  | Amount. Limit represents the number of base coins. market-buy represents the number of quote coins. market-sell represents the number of base coins. |
| data[].orderType | string |  | Order type<br><br>limit Limit price<br><br>market Market price |
| data[].side | string |  | Direction |
| data[].status | string |  | Order status<br><br>`live`: pending match<br><br>`partially_filled`: Partially filled<br><br>`filled`: All filled<br><br>`cancelled`: The order is cancelled |
| data[].priceAvg | string |  | Filled price |
| data[].baseVolume | string |  | Filled quantity (base coin) |
| data[].quoteVolume | string |  | Total trading amount (quote coin) |
| data[].enterPointSource | string |  | Client<br><br>WEB WEB Client<br><br>API API Client<br><br>SYS SYS Client<br><br>ANDROID ANDROID Client<br><br>IOS IOS Client |
| data[].cTime | string |  | Creation time, Unix millisecond timestamp, e.g. 1690196141868 |
| data[].uTime | string |  | Update time, Unix millisecond timestamp, e.g. 1690196141868 |
| data[].orderSource | string |  | Order source<br><br>normal Normal order<br><br>market Market order<br><br>spot_trader_buy Elite spot trade to buy (elite traders)<br><br>spot_follower_buy Copy trade to buy (followers)<br><br>spot_trader_sell Elite spot trade to sell (elite traders)<br><br>spot_follower_sell Copy trade to sell (followers) |
| data[].feeDetail | string |  | Transaction fee breakdown<br><br>> newFees: Fee details for "newFees".<br><br>>> c: Amount deducted by coupons, unit: currency obtained from the transaction.<br><br>>> d: Amount deducted in BGB (Bitget Coin), unit: BGB<br><br>>> r: If the BGB balance is insufficient to cover the fees, the remaining amount is deducted from the currency obtained from the transaction.<br><br>>> t: The total fee amount to be paid, unit: currency obtained from the transaction.<br><br>>> deduction: Ignore.<br><br>>> totalDeductionFee: Ignore.<br><br>> BGB: (Ignore) If there is no "newFees" field, this data represents earlier historical data. This key represents the currency used for fee deduction (it is not fixed; if BGB deduction is enabled, it's BGB, otherwise, it's the currency obtained from the transaction).<br><br>>> deduction: Whether there is a fee deduction.<br><br>>> feeCoinCode: Transaction fee coin code<br><br>>> totalDeductionFee: Deduction amount unit: BGB<br><br>>> totalFee: The total fee amount to be paid, unit: currency obtained from the transaction. |
| data[].tpslType | string |  | `normal`: spot order<br><br>`tpsl`: spot tpsl order |
| data[].triggerPrice | ['string', 'null'] |  | Spot tpsl trigger price (Only valid when `tpslType` is `tpsl`) |
| data[].quoteCoin | string |  | Quote coin |
| data[].baseCoin | string |  | Base coin |
| data[].cancelReason | string |  | Cancel reason<br><br>`normal_cancel`: Normal cancel<br><br>`stp_cancel`: Cancelled by STP |
| data[].executionType | string |  | Execution type<br><br>`exchange`: exchange |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695865476577,
  "data": [
    {
      "userId": "**********",
      "symbol": "BTCUSDT",
      "orderId": "121211212122",
      "clientOid": "121211212122",
      "price": "0",
      "size": "10.0000000000000000",
      "orderType": "market",
      "side": "buy",
      "status": "filled",
      "priceAvg": "13000.0000000000000000",
      "baseVolume": "0.0007000000000000",
      "quoteVolume": "9.1000000000000000",
      "enterPointSource": "API",
      "feeDetail": "{\"BGB\":{\"deduction\":true,\"feeCoinCode\":\"BGB\",\"totalDeductionFee\":-0.0041,\"totalFee\":-0.0041},\"newFees\":{\"c\":0,\"d\":0,\"deduction\":false,\"r\":-0.112079256,\"t\":-0.112079256,\"totalDeductionFee\":0}}",
      "orderSource": "market",
      "tpslType": "normal",
      "triggerPrice": null,
      "quoteCoin": "USDT",
      "baseCoin": "BTC",
      "cancelReason": "",
      "executionType": "exchange",
      "cTime": "1695865232127",
      "uTime": "1695865233051"
    }
  ]
}
```

## Get Current Orders

`GET /api/v2/spot/trade/unfilled-orders`

Frequency limit: 20 times/1s (UID)

Get Unfilled Orders

Operation ID: `classicSpotTradeGetUnfilledOrders`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string |  | Trading pair |
| startTime | query | string |  | The record start time for the query. Unix millisecond timestamp, e.g. 1690196141868 (Only queries for data from the past 90 days are allowed.) |
| endTime | query | string |  | The end time of the record for the query. Unix millisecond timestamp, e.g. 1690196141868 (The startTime and endTime should be within 90 days.) |
| idLessThan | query | string |  | Requests the content on the page before this ID (older data), the value input should be the orderId of the corresponding interface. |
| limit | query | string |  | Limit number default 100 max 100 |
| orderId | query | string |  | OrderId |
| tpslType | query | string |  | order type deafult `normal`<br><br>`normal` spot order<br><br>`tpsl` spot tpsl order |
| requestTime | query | string |  | request Time Unix millisecond timestamp |
| receiveWindow | query | string |  | valid window period Unix millisecond timestamp |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].userId | string |  | User id |
| data[].symbol | string |  | Trading pair name |
| data[].orderId | string |  | Order ID |
| data[].clientOid | string |  | Client order ID |
| data[].priceAvg | string |  | Order price |
| data[].size | string |  | Amount. (orderType = limit means base coin; orderType = market means quote coin) |
| data[].orderType | string |  | Order type<br><br>limit Limit price<br><br>market Market price |
| data[].side | string |  | Direction |
| data[].status | string |  | Order status<br><br>`live`:unfilled;<br><br>`partially_filled`:partially filled;<br><br>`filled`:filled;<br><br>`cancelled`:cancelled; |
| data[].basePrice | string |  | Filled price |
| data[].baseVolume | string |  | Filled volume in base coin |
| data[].quoteVolume | string |  | Filled volume in quote coin |
| data[].enterPointSource | string |  | Client type<br><br>WEB WEB Client<br><br>APP APP Client<br><br>API API Client<br><br>SYS SYS Client<br><br>ANDROID ANDROID Client<br><br>IOS IOS Client |
| data[].orderSource | string |  | Order source<br><br>normal: Normal order<br><br>market: Market order<br><br>spot_trader_buy: Elite spot trade to buy (elite traders)<br><br>spot_follower_buy: Copy trade to buy (followers)<br><br>spot_trader_sell: Elite spot trade to sell (elite traders)<br><br>spot_follower_sell: Copy trade to sell (followers)<br><br>strategy_oco_limit: OCO orders |
| data[].triggerPrice | ['string', 'null'] |  | spot tpsl trigger price(Only valid when `tpslType` is `tpsl`) |
| data[].tpslType | string |  | `normal` spot order<br><br>`tpsl` spot tpsl order |
| data[].presetTakeProfitPrice | string |  | Take profit trigger price |
| data[].executeTakeProfitPrice | string |  | Take profit execute price(If the value is empty, it means take profit in market price) |
| data[].presetStopLossPrice | string |  | Stop loss trigger price |
| data[].executeStopLossPrice | string |  | Stop loss execute price(If the value is empty, it means stop loss in market price) |
| data[].cTime | string |  | Creation time, Unix millisecond timestamp, e.g. 1690196141868 |
| data[].uTime | string |  | Update time, Unix millisecond timestamp, e.g. 1690196141868 |
| data[].force | string |  | Execution strategy<br><br>`gtc`: Normal limit order, good till cancelled<br><br>`post_only`: Post only<br><br>`fok`: Fill or kill<br><br>`ioc`: Immediate or cancel |
| data[].executionType | string |  | Execution type<br><br>`exchange`: exchange |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695808949356,
  "data": [
    {
      "userId": "**********",
      "symbol": "btcusdt",
      "orderId": "2222222",
      "clientOid": "xxxxxxx",
      "priceAvg": "34829.12",
      "size": "1",
      "orderType": "limit",
      "side": "buy",
      "status": "new",
      "basePrice": "0",
      "baseVolume": "0",
      "quoteVolume": "0",
      "enterPointSource": "WEB",
      "orderSource": "normal",
      "triggerPrice": null,
      "tpslType": "normal",
      "presetTakeProfitPrice": "70000",
      "executeTakeProfitPrice": "",
      "presetStopLossPrice": "10000",
      "executeStopLossPrice": "",
      "force": "gtc",
      "executionType": "exchange",
      "cTime": "1622697148",
      "uTime": "1622697148"
    }
  ]
}
```

## Get History Orders

`GET /api/v2/spot/trade/history-orders`

Frequency limit: 20 times/1s (UID)

Get History Orders(It only supports to get the data within 90days. The older data can be downloaded from web)<br/>You can export your historical orders on our <a href="https://www.bitget.com/asset/export/downOrders">web</a>.

Operation ID: `classicSpotTradeGetHistoryOrders`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string |  | Trading pair |
| startTime | query | string |  | The record start time for the query. Unix millisecond timestamp, e.g. 1690196141868. (For Managed Sub-Account, the StartTime cannot be earlier than the binding time) |
| endTime | query | string |  | The end time of the record for the query. Unix millisecond timestamp, e.g. 1690196141868 |
| idLessThan | query | string |  | Requests the content on the page before this ID (older data), the value input should be the orderId of the corresponding interface. |
| limit | query | string |  | Limit number default 100 max 100 |
| orderId | query | string |  | OrderId |
| tpslType | query | string |  | order type deafult `normal`<br><br>`normal` spot order<br><br>`tpsl` spot tpsl order |
| requestTime | query | string |  | request Time Unix millisecond timestamp |
| receiveWindow | query | string |  | valid window period Unix millisecond timestamp |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].userId | string |  | User id |
| data[].symbol | string |  | Trading pair name |
| data[].orderId | string |  | Order ID |
| data[].clientOid | string |  | Client Order ID |
| data[].price | string |  | Order price |
| data[].size | string |  | Amount (orderType = limit means base coin; orderType = market means quote coin) |
| data[].orderType | string |  | Order type<br><br>limit Limit price<br><br>market Market price |
| data[].side | string |  | Direction |
| data[].status | string |  | Order status<br><br>`live`:unfilled;<br><br>`partially_filled`:partially filled;<br><br>`filled`:filled;<br><br>`cancelled`:cancelled; |
| data[].priceAvg | string |  | Average fill price |
| data[].baseVolume | string |  | Filled volume (base coin) |
| data[].quoteVolume | string |  | Filled volume (quote coin) |
| data[].enterPointSource | string |  | Client<br><br>WEB WEB Client<br><br>APP APP Client<br><br>API API Client<br><br>SYS SYS Client<br><br>ANDROID ANDROID Client<br><br>IOS IOS Client |
| data[].orderSource | string |  | Order source<br><br>normal Normal order<br><br>market Market order<br><br>spot_trader_buy Elite spot trade to buy (elite traders)<br><br>spot_follower_buy Copy trade to buy (followers)<br><br>spot_trader_sell Elite spot trade to sell (elite traders)<br><br>spot_follower_sell Copy trade to sell (followers) |
| data[].cTime | string |  | Creation time, Unix millisecond timestamp, e.g. 1690196141868 |
| data[].uTime | string |  | Update time, Unix millisecond timestamp, e.g. 1690196141868 |
| data[].feeDetail | string |  | Fee details. If there is a "newFees" field, then "newFees" represents the fee details. If not, the remaining information is the fee details.<br><br>> newFees: Fee details for "newFees".<br><br>>> c: Amount deducted by coupons, unit: currency obtained from the transaction.<br><br>>> d: Amount deducted in BGB (Bitget Coin), unit: BGB<br><br>>> r: If the BGB balance is insufficient to cover the fees, the remaining amount is deducted from the currency obtained from the transaction.<br><br>>> t: The total fee amount to be paid, unit: currency obtained from the transaction.<br><br>>> deduction: Ignore.<br><br>>> totalDeductionFee: Ignore.<br><br>> BGB: If there is no "newFees" field, this data represents earlier historical data. This key represents the currency used for fee deduction (it is not fixed; if BGB deduction is enabled, it's BGB, otherwise, it's the currency obtained from the transaction).<br><br>>> deduction: Whether there is a fee deduction.<br><br>>> feeCoinCode: Transaction fee coin code<br><br>>> totalDeductionFee: Deduction amount unit: BGB<br><br>>> totalFee: The total fee amount to be paid, unit: currency obtained from the transaction. |
| data[].triggerPrice | ['string', 'null'] |  | spot tpsl trigger price |
| data[].tpslType | string |  | `normal` spot order<br><br>`tpsl` spot tpsl order |
| data[].cancelReason | string |  | Cancel reason<br><br>`normal_cancel`: Normal cancel<br><br>`stp_cancel`: Cancelled by STP |
| data[].quoteCoin | string |  | Quote coin |
| data[].baseCoin | string |  | Base coin |
| data[].executionType | string |  | Execution type<br><br>`exchange`: exchange |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695808949356,
  "data": [
    {
      "userId": "*********",
      "symbol": "ETHUSDT",
      "orderId": "*****************************",
      "clientOid": "*****************************",
      "price": "0",
      "size": "20.0000000000000000",
      "orderType": "market",
      "side": "buy",
      "status": "filled",
      "priceAvg": "1598.1000000000000000",
      "baseVolume": "0.0125000000000000",
      "quoteVolume": "19.9762500000000000",
      "enterPointSource": "WEB",
      "feeDetail": "{\"newFees\":{\"c\":0,\"d\":0,\"deduction\":false,\"r\":-0.112079256,\"t\":-0.112079256,\"totalDeductionFee\":0}}",
      "orderSource": "market",
      "quoteCoin": "USDT",
      "baseCoin": "ETH",
      "executionType": "exchange",
      "cTime": "1698736299656",
      "uTime": "1698736300363",
      "tpslType": "normal",
      "cancelReason": "",
      "triggerPrice": null
    }
  ]
}
```

## Get Fills

`GET /api/v2/spot/trade/fills`

Frequency limit:10 times/1s (UID)

Trader frequency limit: 1 times/1s (UID)

Get Fills(It only supports to get the data within 90days.The older data can be downloaded from web)<br/>You can export your historical orders on our <a href="https://www.bitget.com/asset/export/downOrders">web</a>.

Operation ID: `classicSpotTradeGetFills`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string |  | Trading pair name |
| orderId | query | string |  | Order ID |
| startTime | query | string |  | The start time of the orders, i.e. to get orders after that timestamp. Unix millisecond timestamp, e.g. 1690196141868. (For Managed Sub-Account, the StartTime cannot be earlier than the binding time) |
| endTime | query | string |  | The end time of a fulfilled order, i.e., get orders prior to that timestamp. Unix millisecond timestamp, e.g. 1690196141868. The interval between startTime and endTime must not exceed 90 days. |
| limit | query | string |  | Number of results returned: Default: 100, max 100 |
| idLessThan | query | string |  | Requests the content on the page before this ID (older data), the value input should be the tradeId of the corresponding interface. |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].userId | string |  | Account ID |
| data[].symbol | string |  | Trading pair name |
| data[].orderId | string |  | Order ID |
| data[].tradeId | string |  | Transaction id |
| data[].orderType | string |  | Order type |
| data[].side | string |  | Order direction |
| data[].priceAvg | string |  | Filled price |
| data[].size | string |  | Filled quantity |
| data[].amount | string |  | Total trading amount |
| data[].cTime | string |  | Creation time, Unix second timestamp, e.g. 1622697148 |
| data[].uTime | string |  | Update time, Unix second timestamp, e.g. 1622697148 |
| data[].tradeScope | string |  | Trader tag<br><br>taker Taker<br><br>maker Maker |
| data[].feeDetail | object |  | Transaction fee breakdown |
| data[].feeDetail.deduction | string |  | Discount or not |
| data[].feeDetail.feeCoin | string |  | Transaction fee coin |
| data[].feeDetail.totalDeductionFee | string |  | Total transaction fee discount |
| data[].feeDetail.totalFee | string |  | Total transaction fee |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695865274510,
  "data": [
    {
      "userId": "**********",
      "symbol": "BTCUSDT",
      "orderId": "12345678910",
      "tradeId": "12345678910",
      "orderType": "market",
      "side": "buy",
      "priceAvg": "13000",
      "size": "0.0007",
      "amount": "9.1",
      "feeDetail": {
        "deduction": "no",
        "feeCoin": "BTC",
        "totalDeductionFee": "",
        "totalFee": "-0.0000007"
      },
      "tradeScope": "taker",
      "cTime": "1695865232579",
      "uTime": "1695865233027"
    }
  ]
}
```


---

现货交易接口 —— 下单、撤单及订单与成交查询。

版本: 1.0.0

## 服务地址

- `https://api.bitget.com`

## 接口列表

- `POST /api/v2/spot/trade/place-order` — 下单
- `POST /api/v2/spot/trade/batch-orders` — 批量下单
- `POST /api/v2/spot/trade/cancel-order` — 撤单
- `POST /api/v2/spot/trade/batch-cancel-order` — 批量撤单
- `POST /api/v2/spot/trade/cancel-symbol-order` — 按币对撤单
- `POST /api/v2/spot/trade/cancel-replace-order` — 撤单再下单
- `POST /api/v2/spot/trade/batch-cancel-replace-order` — 批量撤单再下单
- `GET /api/v2/spot/trade/orderInfo` — 获取订单详情
- `GET /api/v2/spot/trade/unfilled-orders` — 获取当前委托列表
- `GET /api/v2/spot/trade/history-orders` — 获取历史委托列表
- `GET /api/v2/spot/trade/fills` — 获取成交明细

## 下单

`POST /api/v2/spot/trade/place-order`

限速规则: 10次/秒/UID

跟单交易员限速规则：1次/秒/UID

现货下单

- **API Broker返佣标识**: 需在HTTP Header请求头中添加如下代码块

  > "X-CHANNEL-API-CODE":"your-channel-api-code"

Operation ID: `classicSpotTradePlaceOrder`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| symbol | string | 是 | 交易对名称，如BTCUSDT |
| side | string | 是 | 交易方向<br><br>`buy`：买入<br><br>`sell`：卖出 |
| orderType | string | 是 | 订单类型<br><br>`limit`：限价<br><br>`market`：市价 |
| force | string | 是 | 执行策略（orderType为market时无效）<br><br>`gtc`：普通限价单，一直有效直至取消<br><br>`post_only`：只做 maker 订单<br><br>`fok`：全部成交或立即取消<br><br>`ioc`：立即成交并取消剩余 |
| price | string |  | 限价价格 |
| size | string | 是 | 委托数量。对于Limit和Market-Sell订单，此参数表示base coin数量；对于Market-Buy订单，此参数表示quote coin数量 |
| clientOid | string |  | 自定义订单ID。当 `tpslType`为`tpsl` 时不生效 |
| triggerPrice | string |  | 现货止盈止损触发价格，仅限于下止盈止损订单时使用 |
| tpslType | string |  | 订单类型<br><br>`normal`：普通单（默认值）<br><br>`tpsl`：止盈止损单 |
| requestTime | string |  | 请求时间, Unix毫秒时间戳格式 |
| receiveWindow | string |  | 有效窗口期，单位毫秒，最大不超过60000 |
| stpMode | string |  | STP（自成交预防）模式<br><br>`none`：不设置STP（默认值）<br><br>`cancel_taker`：取消taker单<br><br>`cancel_maker`：取消maker单<br><br>`cancel_both`：两者都取消 |
| presetTakeProfitPrice | string |  | 止盈价格。当 `tpslType`为`tpsl` 时不生效 |
| executeTakeProfitPrice | string |  | 止盈执行价格。当 `tpslType`为`tpsl` 时不生效 |
| presetStopLossPrice | string |  | 止损价格。当 `tpslType`为`tpsl` 时不生效 |
| executeStopLossPrice | string |  | 止损执行价格。当 `tpslType`为`tpsl` 时不生效 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.orderId | string |  | 订单ID |
| data.clientOid | string |  | 自定义订单ID |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695808949356,
  "data": {
    "orderId": "121211212122",
    "clientOid": "121211212122"
  }
}
```

## 批量下单

`POST /api/v2/spot/trade/batch-orders`

限速规则 5次/1s (UID)

跟单交易员限速规则：1次/s（UID）

批量下单

- **API Broker返佣标识**: 需在HTTP Header请求头中添加如下代码块

  > "X-CHANNEL-API-CODE":"your-channel-api-code"

Operation ID: `classicSpotTradeBatchPlaceOrders`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| batchMode | string |  | 批量下单模式<br><br>`single` 单币种模式, 默认单币种模式<br><br>`multiple` 跨币种模式<br><br>如选择单币种模式，则orderList中的symbol不生效<br><br>如选择跨币种模式，则orderList中的symbol生效，且orderList中的symbol必填。orderList外的symbol不生效 |
| orderList | object[] | 是 | 下单订单集合，最大长度：50 |
| orderList[].symbol | string |  | 交易对名称，如BTCUSDT。跨币种模式下必填 |
| orderList[].side | string |  | 交易方向<br><br>`buy` 买入<br><br>`sell` 卖出 |
| orderList[].orderType | string |  | 订单类型 <br><br>`limit`限价<br><br>`market`市价 |
| orderList[].force | string |  | 执行策略（orderType为market时无效）<br><br>`gtc`普通限价单，一直有效直至取消<br><br>`post_only` 只做 maker 订单<br><br>`fok`全部成交或立即取消<br><br>`ioc`立即成交并取消剩余 |
| orderList[].price | string |  | 限价价格 |
| orderList[].size | string |  | 委托数量。对于Limit和Market-Sell订单，表示base coin数量；对于Market-Buy订单，表示quote coin数量 |
| orderList[].clientOid | string |  | 自定义订单ID |
| orderList[].stpMode | string |  | STP模式， default `none`<br><br>`none` 不设置STP<br><br>`cancel_taker` 取消taker单<br><br>`cancel_maker` 取消maker单<br><br>`cancel_both` 两者都取消 |
| orderList[].presetTakeProfitPrice | string |  | 止盈价格 |
| orderList[].executeTakeProfitPrice | string |  | 止盈执行价格 |
| orderList[].presetStopLossPrice | string |  | 止损价格 |
| orderList[].executeStopLossPrice | string |  | 止损执行价格 |
| symbol | string |  | 交易对名称，如BTCUSDT。单币种模式下使用 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.successList | object[] |  | 成功订单数组 |
| data.successList[].orderId | string |  | 订单ID |
| data.successList[].clientOid | string |  | 客户端订单ID |
| data.failureList | object[] |  | 失败订单数组 |
| data.failureList[].orderId | string |  | 订单ID |
| data.failureList[].clientOid | string |  | 客户端订单ID |
| data.failureList[].errorMsg | string |  | 错误信息 |
| data.failureList[].errorCode | string |  | 错误码 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1666336231317,
  "data": {
    "successList": [
      {
        "orderId": "121211212122",
        "clientOid": "1"
      }
    ],
    "failureList": [
      {
        "orderId": "121211212122",
        "clientOid": "1",
        "errorMsg": "clientOrderId duplicate",
        "errorCode": "43118"
      }
    ]
  }
}
```

## 撤单

`POST /api/v2/spot/trade/cancel-order`

限速规则 10次/1s (UID)

撤单

Operation ID: `classicSpotTradeCancelOrder`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| symbol | string |  | 交易对名称，如BTCUSDT。当 tpslType 为`tpsl`时，此项为非必填 |
| tpslType | string |  | 订单类型 默认：`normal`<br><br>`normal`：普通单<br><br>`tpsl`：止盈止损单 |
| orderId | string |  | 订单ID。orderId与clientOid二选一。当 tpslType 为`tpsl`时，此项为必填 |
| clientOid | string |  | 客户自定义ID。orderId与clientOid二选一 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.orderId | string |  | 订单ID |
| data.clientOid | string |  | 自定义订单ID |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1234567891234,
  "data": {
    "orderId": "121211212122",
    "clientOid": "xx001"
  }
}
```

## 批量撤单

`POST /api/v2/spot/trade/batch-cancel-order`

限速规则 10次/1s (UID)

批量撤单

- 批量撤单，同时撤销同一个币对的多笔订单时，不允许部分订单传orderId，另一部分订单传clientOid，不允许混用 orderId 和 clientOid，必须保持一致，否则只传入 clientOid 的订单将无法被取消。

Operation ID: `classicSpotTradeBatchCancelOrders`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| symbol | string |  | 交易对名称，如BTCUSDT |
| batchMode | string |  | 批量下单模式<br><br>`single` 单币种模式, 默认单币种模式<br><br>`multiple` 跨币种模式<br><br>如选择单币种模式，则orderList中的symbol不生效<br><br>如选择跨币种模式，则orderList中的symbol生效，且orderList中的symbol必填。orderList外的symbol不生效 |
| orderList | object[] | 是 | 订单id数组，最大长度：50 |
| orderList[].symbol | string |  | 交易对名称，如BTCUSDT |
| orderList[].orderId | string |  | orderId，与clientOid必填一个 |
| orderList[].clientOid | string |  | clientOid，与orderId必填一个 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.successList | object[] |  | 成功订单数组 |
| data.successList[].orderId | string |  | 订单ID |
| data.successList[].clientOid | string |  | 客户端订单ID |
| data.failureList | object[] |  | 失败订单数组 |
| data.failureList[].orderId | string |  | 订单ID |
| data.failureList[].clientOid | string |  | 客户端订单ID |
| data.failureList[].errorMsg | string |  | 错误信息 |
| data.failureList[].errorCode | string |  | 错误码 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695808949356,
  "data": {
    "successList": [
      {
        "orderId": "121211212122",
        "clientOid": "121211212122"
      }
    ],
    "failureList": [
      {
        "orderId": "121211212122",
        "clientOid": "xxx001",
        "errorMsg": "duplicate clientOrderId",
        "errorCode": "43118"
      }
    ]
  }
}
```

## 按币对撤单

`POST /api/v2/spot/trade/cancel-symbol-order`

限速规则 5次/1s (UID)

按币对撤单

Operation ID: `classicSpotTradeCancelSymbolOrders`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| symbol | string | 是 | 交易对名称，如BTCUSDT |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.symbol | string |  | 撤销的symbol (此请求是异步执行的，如果需要知道结果，请查询历史订单接口) |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1698313139948,
  "data": {
    "symbol": "BGBUSDT"
  }
}
```

## 撤单再下单

`POST /api/v2/spot/trade/cancel-replace-order`

限速规则: 5次/秒/UID

撤销原订单再下新的订单

- **API Broker返佣标识**: 需在HTTP Header请求头中添加如下代码块

  > "X-CHANNEL-API-CODE":"your-channel-api-code"

Operation ID: `classicSpotTradeCancelReplaceOrder`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| symbol | string | 是 | 交易对名称，如BTCUSDT |
| price | string | 是 | 限价价格 |
| size | string | 是 | 委托数量，限价单base coin数量 |
| clientOid | string |  | 待撤销自定义订单ID。orderId与clientOid二选一 |
| orderId | string |  | 待撤销订单号。orderId与clientOid二选一 |
| newClientOid | string |  | 新订单的自定义订单ID<br><br>注：newClientOid如果因为幂等被限制住，会导致旧单撤销成功，但是新单下单失败 |
| presetTakeProfitPrice | string |  | 止盈价格 |
| executeTakeProfitPrice | string |  | 止盈执行价格 |
| presetStopLossPrice | string |  | 止损价格 |
| executeStopLossPrice | string |  | 止损执行价格 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.orderId | string |  | 订单ID |
| data.clientOid | ['string', 'null'] |  | 自定义订单ID |
| data.success | string |  | 是否成功<br><br>`success`: 成功<br><br>`failure`: 失败 |
| data.msg | ['string', 'null'] |  | 如果失败，则是失败的原因 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1725345009763,
  "data": {
    "orderId": "xxxxxxxxxxxxxxx",
    "clientOid": null,
    "success": "success",
    "msg": null
  }
}
```

## 批量撤单再下单

`POST /api/v2/spot/trade/batch-cancel-replace-order`

限速规则: 5次/秒/UID

批量撤销原订单再下新的订单

- **API Broker返佣标识**: 需在HTTP Header请求头中添加如下代码块

  > "X-CHANNEL-API-CODE":"your-channel-api-code"

Operation ID: `classicSpotTradeBatchCancelReplaceOrder`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| orderList | object[] | 是 | 下单订单集合，最大长度：50 |
| orderList[].symbol | string |  | 交易对名称，如BTCUSDT |
| orderList[].price | string |  | 限价价格 |
| orderList[].size | string |  | 委托数量，限价单base coin数量 |
| orderList[].clientOid | string |  | 待撤销自定义订单ID。orderId与clientOid二选一 |
| orderList[].orderId | string |  | 待撤销订单号。orderId与clientOid二选一 |
| orderList[].newClientOid | string |  | 新订单的自定义订单ID<br><br>注：newClientOid如果因为幂等被限制住，会导致旧单撤销成功，但是新单下单失败 |
| orderList[].presetTakeProfitPrice | string |  | 止盈价格 |
| orderList[].executeTakeProfitPrice | string |  | 止盈执行价格 |
| orderList[].presetStopLossPrice | string |  | 止损价格 |
| orderList[].executeStopLossPrice | string |  | 止损执行价格 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].orderId | string |  | 订单ID |
| data[].clientOid | ['string', 'null'] |  | 自定义订单ID |
| data[].success | string |  | 是否成功<br><br>`success`: 成功<br><br>`failure`: 失败 |
| data[].msg | string |  | 如果失败，则是失败的原因 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1725341809524,
  "data": [
    {
      "orderId": "xxxxxxxxxxxxxxxxxxxxxx",
      "clientOid": null,
      "success": "failure",
      "msg": "xxxxxxxxxx"
    }
  ]
}
```

## 获取订单详情

`GET /api/v2/spot/trade/orderInfo`

限速规则 20次/1s (UID)

获取订单详情

Operation ID: `classicSpotTradeGetOrderInfo`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| orderId | query | string |  | 订单ID，和clientOid必填其中一个 |
| clientOid | query | string |  | 客户自定义ID，和orderId必填其中一个 |
| requestTime | query | string |  | 请求时间 Unix毫秒时间戳格式 |
| receiveWindow | query | string |  | 有效窗口期 单位毫秒 窗口期不超过60s |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].userId | string |  | 账户id |
| data[].symbol | string |  | 交易对名称 |
| data[].orderId | string |  | 订单ID |
| data[].clientOid | string |  | 自定义ID |
| data[].price | string |  | 委托价格 |
| data[].size | string |  | 委托数量。limit时表示base coin数量; market-buy表示quote coin数量；market-sell表示base coin数量 |
| data[].orderType | string |  | 订单类型<br><br>limit限价<br><br>market市价 |
| data[].side | string |  | 交易方向 |
| data[].status | string |  | 订单状态<br><br>`live` 未成交<br><br>`partially_filled` 部分成交<br><br>`filled` 全部成交<br><br>`cancelled` 已撤销 |
| data[].priceAvg | string |  | 成交价格 |
| data[].baseVolume | string |  | 成交数量，左币 |
| data[].quoteVolume | string |  | 成交总额，右币 |
| data[].enterPointSource | string |  | 订单来源<br><br>WEB    WEB客户端<br><br>IOS    IOS客户端<br><br>ANDROID    Andriod客户端<br><br>API    API客户端<br><br>SYS    系统订单 |
| data[].cTime | string |  | 创建时间，Unix毫秒时间戳，例如1690196141868 |
| data[].uTime | string |  | 更新时间，Unix毫秒时间戳，例如1690196141868 |
| data[].orderSource | string |  | 订单来源<br><br>normal 正常下单<br><br>market 市价单<br><br>spot_trader_buy 现货带单买 (交易员)<br><br>spot_follower_buy现货跟单买 (跟随者)<br><br>spot_trader_sell 现货带单卖(交易员)<br><br>spot_follower_sell 现货跟单卖(跟随者) |
| data[].feeDetail | string |  | 手续费明细<br><br>> newFees：手续费明细newFees<br><br>>> c：优惠券抵扣的金额，单位：交易所得币种<br><br>>> d：BGB抵扣的金额，单位：BGB<br><br>>> r：如BGB余额不够抵扣手续费，则剩下的用所得币抵扣<br><br>>> t：手续费应付金额，单位：所得币种<br><br>>> deduction：忽略<br><br>>> totalDeductionFee：忽略<br><br>> BGB：（忽略）如果没有newFees字段，则代表此数据是较早的历史数据，此key是抵扣手续费的币种（不是固定的，如果开启了BGB抵扣，则是BGB，如果没有开启BGB抵扣，则是交易获得币种）<br><br>>> deduction：是否有手续费抵扣<br><br>>> feeCoinCode：手续费币种<br><br>>> totalDeductionFee：抵扣金额 单位：BGB<br><br>>> totalFee：手续费应付金额，单位：所得币种 |
| data[].tpslType | string |  | `normal` 现货普通订单<br><br>`tpsl` 现货止盈止损订单 |
| data[].triggerPrice | ['string', 'null'] |  | 现货止盈止损触发价（仅当 `tpslType` 为 `tpsl` 时有效） |
| data[].quoteCoin | string |  | 计价币 |
| data[].baseCoin | string |  | 交易币 |
| data[].cancelReason | string |  | 取消原因<br><br>`normal_cancel`：普通取消<br><br>`stp_cancel`：因STP规则取消 |
| data[].executionType | string |  | 执行类型<br><br>`exchange`：交易所撮合 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695865476577,
  "data": [
    {
      "userId": "**********",
      "symbol": "BTCUSDT",
      "orderId": "121211212122",
      "clientOid": "121211212122",
      "price": "0",
      "size": "10.0000000000000000",
      "orderType": "market",
      "side": "buy",
      "status": "filled",
      "priceAvg": "13000.0000000000000000",
      "baseVolume": "0.0007000000000000",
      "quoteVolume": "9.1000000000000000",
      "enterPointSource": "API",
      "feeDetail": "{\"BGB\":{\"deduction\":true,\"feeCoinCode\":\"BGB\",\"totalDeductionFee\":-0.0041,\"totalFee\":-0.0041},\"newFees\":{\"c\":0,\"d\":0,\"deduction\":false,\"r\":-0.112079256,\"t\":-0.112079256,\"totalDeductionFee\":0}}",
      "orderSource": "market",
      "tpslType": "normal",
      "triggerPrice": null,
      "quoteCoin": "USDT",
      "baseCoin": "BTC",
      "cancelReason": "",
      "executionType": "exchange",
      "cTime": "1695865232127",
      "uTime": "1695865233051"
    }
  ]
}
```

## 获取当前委托列表

`GET /api/v2/spot/trade/unfilled-orders`

限速规则 20次/1s (UID)

获取未成交列表

Operation ID: `classicSpotTradeGetUnfilledOrders`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string |  | 交易对名称 如 BTCUSDT |
| startTime | query | string |  | 查询开始时间，Unix毫秒时间戳，例如1690196141868 (只允许查询近90天数据) |
| endTime | query | string |  | 查询结束时间，Unix毫秒时间戳，例如1690196141868 (startTime和endTime间隔不允许超过90天) |
| idLessThan | query | string |  | 上一次查询的最后一条数据的orderId |
| limit | query | string |  | 查询条数 默认100，最大100 |
| orderId | query | string |  | 订单ID |
| tpslType | query | string |  | 订单类型 deafult `normal`<br><br>`normal` 普通单<br><br>`tpsl` 止盈止损单 |
| requestTime | query | string |  | 请求时间 Unix毫秒时间戳格式 |
| receiveWindow | query | string |  | 有效窗口期 单位毫秒 窗口期不超过60s |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].userId | string |  | 账户id |
| data[].symbol | string |  | 交易对名称 |
| data[].orderId | string |  | 订单ID |
| data[].clientOid | string |  | 自定义ID |
| data[].priceAvg | string |  | 委托价格 |
| data[].size | string |  | 委托数量(orderType=`limit`时表示base coin; orderType=`market`时表示quote coin) |
| data[].orderType | string |  | 订单类型<br><br>limit限价<br><br>market市价 |
| data[].side | string |  | 交易方向 |
| data[].status | string |  | 订单状态<br><br>`live`:未成交;<br><br>`partially_filled`:部分成交;<br><br>`filled`:已成交;<br><br>`cancelled`:已取消; |
| data[].basePrice | string |  | 成交价格 |
| data[].baseVolume | string |  | 成交数量 |
| data[].quoteVolume | string |  | 成交总额 |
| data[].enterPointSource | string |  | 订单来源<br><br>WEB    WEB客户端<br><br>IOS    IOS客户端<br><br>ANDROID    Andriod客户端<br><br>API    API客户端<br><br>SYS    系统, 通常为爆仓 |
| data[].orderSource | string |  | 订单来源<br><br>normal: 正常下单<br><br>market: 市价单<br><br>spot_trader_buy: 现货带单买 (交易员)<br><br>spot_follower_buy: 现货跟单买 (跟随者)<br><br>spot_trader_sell: 现货带单卖(交易员)<br><br>spot_follower_sell: 现货跟单卖(跟随者)<br><br>strategy_oco_limit：OCO订单 |
| data[].triggerPrice | ['string', 'null'] |  | 触发价格 只有 tpsl 订单返回 |
| data[].tpslType | string |  | 订单类型 deafult `normal`<br><br>`normal` 普通单<br><br>`tpsl` 止盈止损单 |
| data[].presetTakeProfitPrice | string |  | 止盈触发价格 |
| data[].executeTakeProfitPrice | string |  | 止盈执行价格(为空时代表市价止盈) |
| data[].presetStopLossPrice | string |  | 止损触发价格 |
| data[].executeStopLossPrice | string |  | 止损执行价格(为空时代表市价止损) |
| data[].cTime | string |  | 创建时间，Unix毫秒时间戳，例如1690196141868 |
| data[].uTime | string |  | 更新时间，Unix毫秒时间戳，例如1690196141868 |
| data[].force | string |  | 执行策略<br><br>`gtc`: 普通限价单，永久有效<br><br>`post_only`: 只做maker<br><br>`fok`: 全部成交或全部撤销<br><br>`ioc`: 立即成交剩余撤销 |
| data[].executionType | string |  | 执行类型<br><br>`exchange`：交易所撮合 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695808949356,
  "data": [
    {
      "userId": "**********",
      "symbol": "btcusdt",
      "orderId": "2222222",
      "clientOid": "xxxxxxx",
      "priceAvg": "34829.12",
      "size": "1",
      "orderType": "limit",
      "side": "buy",
      "status": "new",
      "basePrice": "0",
      "baseVolume": "0",
      "quoteVolume": "0",
      "enterPointSource": "WEB",
      "orderSource": "normal",
      "triggerPrice": null,
      "tpslType": "normal",
      "presetTakeProfitPrice": "70000",
      "executeTakeProfitPrice": "",
      "presetStopLossPrice": "10000",
      "executeStopLossPrice": "",
      "force": "gtc",
      "executionType": "exchange",
      "cTime": "1622697148",
      "uTime": "1622697148"
    }
  ]
}
```

## 获取历史委托列表

`GET /api/v2/spot/trade/history-orders`

限速规则 20次/1s (UID)

获取历史订单列表(仅支持查询90天内数据，超过90天数据可以在网页端导出)<br/>您可以在网页端<a href="https://www.bitget.com/zh-CN/asset/export/downOrders">导出</a>历史订单。

Operation ID: `classicSpotTradeGetHistoryOrders`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string |  | 交易对名称BTCUSDT |
| startTime | query | string |  | 查询开始时间 (只允许查询近90天数据) 。（托管子账户访问时，StartTime 时间不能早于 绑定开始的时间） |
| endTime | query | string |  | 查询结束时间 (startTime和endTime间隔不允许超过90天) |
| idLessThan | query | string |  | 上一次查询的最后一条数据的orderId |
| limit | query | string |  | 查询条数 默认100，最大100 |
| orderId | query | string |  | 订单ID |
| tpslType | query | string |  | 订单类型 deafult `normal`<br><br>`normal` 普通单<br><br>`tpsl` 止盈止损单 |
| requestTime | query | string |  | 请求时间 Unix毫秒时间戳格式 |
| receiveWindow | query | string |  | 有效窗口期 单位毫秒 窗口期不超过60s |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].userId | string |  | 账户id |
| data[].symbol | string |  | 交易对名称 |
| data[].orderId | string |  | 订单ID |
| data[].clientOid | string |  | 自定义ID |
| data[].price | string |  | 委托价格 |
| data[].size | string |  | 委托数量(orderType=`limit`时表示base coin; orderType=`market`时表示quote coin) |
| data[].orderType | string |  | 订单类型<br><br>limit限价<br><br>market市价 |
| data[].side | string |  | 交易方向 |
| data[].status | string |  | 订单状态<br><br>`live`:未成交;<br><br>`partially_filled`:部分成交;<br><br>`filled`:已成交;<br><br>`cancelled`:已取消; |
| data[].priceAvg | string |  | 成交价格 |
| data[].baseVolume | string |  | 成交数量 |
| data[].quoteVolume | string |  | 成交总额 |
| data[].enterPointSource | string |  | 订单来源<br><br>WEB    WEB客户端<br><br>IOS    IOS客户端<br><br>ANDROID    Andriod客户端<br><br>API    API客户端<br><br>SYS    系统, 通常为爆仓 |
| data[].orderSource | string |  | 订单来源<br><br>normal 正常下单<br><br>market 市价单<br><br>spot_trader_buy 现货带单买 (交易员)<br><br>spot_follower_buy现货跟单买 (跟随者)<br><br>spot_trader_sell 现货带单卖(交易员)<br><br>spot_follower_sell 现货跟单卖(跟随者) |
| data[].cTime | string |  | 创建时间，Unix毫秒时间戳，例如1690196141868 |
| data[].uTime | string |  | 更新时间，Unix毫秒时间戳，例如1690196141868 |
| data[].feeDetail | string |  | 手续费明细, 如果有newFees字段，则newFees是手续费明细，如果没有，则剩下的信息是手续费明细<br><br>> newFees：手续费明细newFees<br><br>>> c：优惠券抵扣的金额，单位：交易所得币种<br><br>>> d：BGB抵扣的金额，单位：BGB<br><br>>> r：如BGB余额不够抵扣手续费，则剩下的用所得币抵扣<br><br>>> t：手续费应付金额，单位：所得币种<br><br>>> deduction：忽略<br><br>>> totalDeductionFee：忽略<br><br>> BGB：如果没有newFees字段，则代表此数据是较早的历史数据，此key是抵扣手续费的币种（不是固定的，如果开启了BGB抵扣，则是BGB，如果没有开启BGB抵扣，则是交易获得币种）<br><br>>> deduction：是否有手续费抵扣<br><br>>> feeCoinCode：手续费币种<br><br>>> totalDeductionFee：抵扣金额 单位：BGB<br><br>>> totalFee：手续费应付金额，单位：所得币种 |
| data[].triggerPrice | ['string', 'null'] |  | 触发价格 只有 tpsl 订单返回 |
| data[].tpslType | string |  | `normal` 普通单 <br><br>`tpsl` 止盈止损单 |
| data[].cancelReason | string |  | 取消原因<br><br>`normal_cancel`：普通取消<br><br>`stp_cancel`：因STP规则取消 |
| data[].quoteCoin | string |  | 计价币 |
| data[].baseCoin | string |  | 交易币 |
| data[].executionType | string |  | 执行类型<br><br>`exchange`：交易所撮合 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695808949356,
  "data": [
    {
      "userId": "*********",
      "symbol": "ETHUSDT",
      "orderId": "*****************************",
      "clientOid": "*****************************",
      "price": "0",
      "size": "20.0000000000000000",
      "orderType": "market",
      "side": "buy",
      "status": "filled",
      "priceAvg": "1598.1000000000000000",
      "baseVolume": "0.0125000000000000",
      "quoteVolume": "19.9762500000000000",
      "enterPointSource": "WEB",
      "feeDetail": "{\"newFees\":{\"c\":0,\"d\":0,\"deduction\":false,\"r\":-0.112079256,\"t\":-0.112079256,\"totalDeductionFee\":0}}",
      "orderSource": "market",
      "quoteCoin": "USDT",
      "baseCoin": "ETH",
      "executionType": "exchange",
      "cTime": "1698736299656",
      "uTime": "1698736300363",
      "cancelReason": "",
      "tpslType": "normal",
      "triggerPrice": null
    }
  ]
}
```

## 获取成交明细

`GET /api/v2/spot/trade/fills`

限速规则 10次/1s (UID)

交易员限速规则：1次/s（uid）

获取成交明细(仅支持查询90天内数据，超过90天数据可以在网页端导出)<br/>您可以在网页端<a href="https://www.bitget.com/zh-CN/asset/export/downOrders">导出</a>历史订单。

Operation ID: `classicSpotTradeGetFills`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string |  | 交易对名称 |
| orderId | query | string |  | 订单ID |
| startTime | query | string |  | 成交订单的开始时间，即获取该时间戳以后的订单。Unix毫秒时间戳，例如1690196141868。（托管子账户访问时，StartTime 时间不能早于 绑定开始的时间） |
| endTime | query | string |  | 成交订单的结束时间，即获取该时间戳以前的订单。Unix毫秒时间戳，例如1690196141868。startTime和endTime的时间间隔不超过90天 |
| limit | query | string |  | 返回结果的数量，默认100，最大100 |
| idLessThan | query | string |  | 请求此ID之前（更旧的数据）的分页内容，传的值为对应接口的 tradeId。 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].userId | string |  | 账户ID |
| data[].symbol | string |  | 交易对名称 |
| data[].orderId | string |  | 订单ID |
| data[].tradeId | string |  | 成交ID |
| data[].orderType | string |  | 订单类型 |
| data[].side | string |  | 委托方向 |
| data[].priceAvg | string |  | 成交价格 |
| data[].size | string |  | 成交数量 |
| data[].amount | string |  | 成交总额 |
| data[].cTime | string |  | 创建时间，Unix毫秒时间戳，例如1622697148123 |
| data[].uTime | string |  | 更新时间，Unix毫秒时间戳，例如1622697148123 |
| data[].tradeScope | string |  | 交易者标识<br><br>taker 吃单方<br><br>maker 挂单方 |
| data[].feeDetail | object |  | 手续费明细 |
| data[].feeDetail.deduction | string |  | 是否折扣 |
| data[].feeDetail.feeCoin | string |  | 手续费币种 |
| data[].feeDetail.totalDeductionFee | string |  | 总计折扣手续费 |
| data[].feeDetail.totalFee | string |  | 总计手续费 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695865274510,
  "data": [
    {
      "userId": "**********",
      "symbol": "BTCUSDT",
      "orderId": "12345678910",
      "tradeId": "12345678910",
      "orderType": "market",
      "side": "buy",
      "priceAvg": "13000",
      "size": "0.0007",
      "amount": "9.1",
      "feeDetail": {
        "deduction": "no",
        "feeCoin": "BTC",
        "totalDeductionFee": "",
        "totalFee": "-0.0000007"
      },
      "tradeScope": "taker",
      "cTime": "1695865232579",
      "uTime": "1695865233027"
    }
  ]
}
```