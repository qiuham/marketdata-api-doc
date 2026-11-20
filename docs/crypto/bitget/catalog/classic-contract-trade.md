---
exchange: bitget
source_url: https://www.bitget.com/docs/catalog/classic-contract-trade
api_type: REST
updated_at: 2026-11-20 19:01:57.578392
---

# Classic Contract Trade API

Classic account — futures order placement & queries.

版本: 1.0.0

## 服务地址

- `https://api.bitget.com`

## 接口列表

- `POST /api/v2/mix/order/place-order` — Place Order
- `POST /api/v2/mix/order/click-backhand` — Reversal
- `POST /api/v2/mix/order/batch-place-order` — Batch Order
- `POST /api/v2/mix/order/modify-order` — Modify Order
- `POST /api/v2/mix/order/cancel-order` — Cancel Order
- `POST /api/v2/mix/order/batch-cancel-orders` — Batch Cancel
- `POST /api/v2/mix/order/close-positions` — Flash Close Position
- `GET /api/v2/mix/order/detail` — Get Order Detail
- `GET /api/v2/mix/order/fills` — Get Order Fill Details
- `GET /api/v2/mix/order/fill-history` — Get Historical Transaction Details
- `GET /api/v2/mix/order/orders-pending` — Get Pending Orders
- `GET /api/v2/mix/order/orders-history` — Get History Order
- `POST /api/v2/mix/order/cancel-all-orders` — Cancel All Orders

## Place Order

`POST /api/v2/mix/order/place-order`

Rate limit: 10 requests/second/UID

Ignore the `tradeSide` parameter when position mode is in `one-way-mode`

In “hedge-mode”, when there is limit close order occupying the position, if the size of next market close order and limit close orders exceeds the position size, it will return an “insufficient position error” instead of cancelling the current limit order and executing the market order

**hedge position mode**:  **Open long**: "side"=`buy`, "tradeSide"=`open`; **Close long**: "side"=`buy`, "tradeSide"=`close`; **Open short**: "side"=`sell`, "tradeSide"=`open`; **Close short**: "side"=`sell`, "tradeSide"=`close`; **one-way position mode**: "side"=`buy` and `sell`, tradeSide: ignore

In `one-way-mode` position mode, if the total size of the new reduce-only order and the existing reduce-only orders exceeds the position size, the system will cancel the existing reduce-only orders sequentially based on their creation order until the total size of the new and existing reduce-only orders is less than or equal to the position size. Additionally, the response for the latest reduce-only order request will not include an `orderId`. You can use the `clientOid` set in the request to query order details or retrieve the orderId from the current pending orders.

When in `hedge Mode`, if a limit close order is occupying a position, and a subsequent market close order (its quantity plus the limit order's quantity) exceeds the total position size, it will not report an insufficient position error. It also won't cancel the limit order that's occupying the position. Instead, the quantity of the limit close order will be preserved, and the market order will close only the quantity remaining after subtracting the limit order's quantity from the total position size. For example: If you have a position of 100, a limit order occupies 70, and you then place a market close order for 50, it will not report an insufficient position error, nor will it cancel the occupying limit order to execute the market order. Instead, it will directly close a quantity of 30.

When in `hedge Mode`,if the existing quantity is equal to the limit close position order of the held position, a newly added close position order will automatically cancel the limit order that has occupied the position. 

For elite traders, please strictly adhere to the list of trading pairs specified in the Available trading pairs and parameters for elite traders when placing orders using the Copy Trading API Key. Trading pairs outside the announced list are not available for copy trading.

**API Broker rebate identifier**:

  The following code block needs to be added to the HTTP Header of the request.

  > "X-CHANNEL-API-CODE":"your-channel-api-code"

Operation ID: `classicContractTradePlaceOrder`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| symbol | string | 是 | Trading pair, e.g. ETHUSDT |
| productType | string | 是 | Product type<br><br>`USDT-FUTURES` USDT-M Futures<br><br>`COIN-FUTURES` Coin-M Futures<br><br>`USDC-FUTURES` USDC-M Futures |
| marginMode | string | 是 | Position mode<br><br>`isolated`: isolated margin <br><br>`crossed`: crossed margin |
| marginCoin | string | 是 | Margin coin(capitalized) |
| size | string | 是 | Amount (base coin) <br><br>To get the decimal places of size:Get Contract Config |
| price | string |  | Price of the order.<br><br>Required if the "orderType" is `limit` <br><br>To get the decimal places of size:Get Contract Config |
| side | string | 是 | Trade side<br><br>`buy`: Buy(**one-way-mode**); Long position direction(**hedge-mode**)<br><br>`sell`: Sell(**one-way-mode**); Short position direction(**hedge-mode**) |
| tradeSide | string |  | Trade type<br><br>**Only required in hedge-mode** <br><br>`open`: Open position<br><br>`close`: Close position |
| orderType | string | 是 | Order type<br><br>`limit`: limit orders<br><br>`market`: market orders |
| force | string |  | Order expiration date.<br><br>Required if the orderType is `limit`<br><br>`ioc`: Immediate or cancel<br><br>`fok`: Fill or kill<br><br>`gtc`: Good till canceled(**default value**)<br><br>`post_only`: Post only |
| clientOid | string |  | Customize order ID |
| reduceOnly | string |  | Whether or not to just reduce the position: `YES`, `NO`<br><br>Default: `NO`. <br><br>Applicable only in **one-way-position** mode |
| presetStopSurplusPrice | string |  | Take-profit value<br><br>No take-profit is set if the field is empty. |
| presetStopLossPrice | string |  | Stop-loss value<br><br>No stop-loss is set if the field is empty. |
| presetStopSurplusExecutePrice | string |  | Preset stop - profit execution price. |
| presetStopLossExecutePrice | string |  | Preset stop-loss execution price. |
| stpMode | string |  | [STP Mode(Self Trade Prevention)](https://www.bitget.com/support/articles/12560603812732)<br><br> `none`: not setting STP(default value)<br><br>`cancel_taker`: cancel taker order <br><br>`cancel_maker`: cancel maker order <br><br>`cancel_both`: cancel both of taker and maker orders |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.orderId | string |  | Order ID |
| data.clientOid | string |  | Customize order ID |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695806875837,
  "data": {
    "clientOid": "121211212122",
    "orderId": "121211212122"
  }
}
```

## Reversal

`POST /api/v2/mix/order/click-backhand`

Rate limit: 10 req/sec/UID

Rate limit: 1 req/sec/UID for **copy trading traders**

`side` and `tradeSide`：

    - In `one-way-mode`, do NOT add the `tradeSide` parameter in request

    - In `hedge-mode`, `tradeSide` is required

        - Reversal the current long position and open a short position: `side`=buy, `tradeSide`

        - Reversal the current short position and open a long position: `side`=sell, `tradeSide`

`size`: represents the reversal size

    - In `one-way-mode`, the whole position will be reversed if no `size` was set in the request

    - In `hedge-mode`: 

        - If the `size` set is less than the current position size, the `size` of position will be closed and the same size reversal position will be opened

          For example, for a ETHUSDT size 20 long position, if the `size` was set 3 in request, then the current long position size will be reduced to 17, and a new size 3 short position will be opened

        - If the `size` set is equal to or more than the current position size, the whole position will be reversed

          For example, for a ETHUSDT size 10 long position, if the `size` was set 10 or 11 in request, then the current position will be closed and a new 10 size short position will be opened

      

**API Broker rebate identifier**:

  The following code block needs to be added to the HTTP Header of the request.

  > "X-CHANNEL-API-CODE":"your-channel-api-code"

Operation ID: `classicContractTradeReversal`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| symbol | string | 是 | Trading pair, e.g. ETHUSDT |
| marginCoin | string | 是 | marginCoin e.g: USDT |
| productType | string | 是 | Product type<br><br>`USDT-FUTURES` USDT-M Futures<br><br>`COIN-FUTURES` Coin-M Futures<br><br>`USDC-FUTURES` USDC-M Futures |
| size | string |  | Amount |
| side | string | 是 | Order direction<br><br>buy: Buy<br><br>sell: Sell |
| tradeSide | string |  | Direction<br><br>Required in open and close (hedge mode) position .<br><br>For one-way positions, this field will be ignored<br><br>Open and Close<br><br>Notes:<br><br>For open long, fill in"Buy"; tradeSide should be "Open" <br><br>For open short, fill in "Sell"; tradeSide should be "Open" <br><br>For close long, fill in "Buy"; tradeSide should be "Close" <br><br>For close short, fill in "Sell"; tradeSide should be "Close" |
| clientOid | string |  | Customize order ID |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.orderId | string |  | Order ID |
| data.clientOid | string |  | Customize order ID |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695806875837,
  "data": {
    "clientOid": "121211212122",
    "orderId": "1"
  }
}
```

## Batch Order

`POST /api/v2/mix/order/batch-place-order`

Rate limit: 5 requests/second/UID

Rate limit: 1 request/second/UID for **copy trading traders**

Supports TP/SL feature. If the current underlying asset does not exist in the position, it is intended to preset the TP/SL. If the current underlying exists in the position, it is intended to modify the TP/SL

Ignore the `tradeSide` parameter when position mode is in `one-way-mode`

**API Broker rebate identifier**:

  The following code block needs to be added to the HTTP Header of the request.

  > "X-CHANNEL-API-CODE":"your-channel-api-code"

Operation ID: `classicContractTradeBatchOrder`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| symbol | string | 是 | Trading pair |
| productType | string | 是 | Product type<br><br>`USDT-FUTURES` USDT-M Futures<br><br>`COIN-FUTURES` Coin-M Futures<br><br>`USDC-FUTURES` USDC-M Futures |
| marginCoin | string | 是 | Margin coin, must be capitalized |
| marginMode | string | 是 | Position mode<br><br>`isolated`: isolated margin <br><br>`crossed`: crossed margin |
| orderList | object[] | 是 | Order list, maximum length: 50 |
| orderList[].size | string | 是 | Amount |
| orderList[].price | string |  | Price of the order.<br><br>Required if the order type is `limit` |
| orderList[].side | string | 是 | Order direction<br><br>`buy`: Buy<br><br>`sell`: Sell |
| orderList[].tradeSide | string |  | Direction<br><br>**Only required in hedge-mode** <br><br>Open and Close Notes:<br><br>For open long, `side` fill in"buy"; `tradeSide` should be "Open" <br><br>For open short, `side` fill in "sell"; `tradeSide` should be "open" <br><br>For close long, `side` fill in "buy"; `tradeSide` should be "close" <br><br>For close short, `side` fill in "sell";`tradeSide` should be "close" |
| orderList[].orderType | string | 是 | Order type<br><br>`limit`: limit orders<br><br>`market`: market orders |
| orderList[].force | string |  | Order expiration date.<br><br>Required if the orderType is `limit`, default value is `gtc`<br><br>`ioc`: Immediate or cancel<br><br>`fok`: Fill or kill<br><br>`gtc`: Good till canceled<br><br>`post_only`: Post only |
| orderList[].clientOid | string |  | Custom order ID |
| orderList[].reduceOnly | string |  | Whether or not to just reduce the position: `YES`, `NO`<br><br>Default: `NO`<br><br>Applicable only in **one-way-position** mode |
| orderList[].presetStopSurplusPrice | string |  | Take-profit value<br><br>No take-profit is set if the field is empty. |
| orderList[].presetStopLossPrice | string |  | Stop-loss value<br><br>No stop-loss is set if the field is empty. |
| orderList[].stpMode | string |  | STP Mode, default `none` <br><br> `none` not setting STP <br><br> `cancel_taker` cancel taker order <br><br>  `cancel_maker` cancel maker order <br><br>  `cancel_both` cancel both of taker and maker orders |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.successList | object[] |  | Successful order list |
| data.successList[].orderId | string |  | Order ID |
| data.successList[].clientOid | string |  | Customize order ID |
| data.failureList | object[] |  | Failed order list |
| data.failureList[].orderId | string |  | Order ID |
| data.failureList[].clientOid | string |  | Customize order ID |
| data.failureList[].errorMsg | string |  | Failure reason |
| data.failureList[].errorCode | string |  | Failure code |
| data.result | boolean |  | Whether all orders succeeded. `true`: all succeeded; `false`: at least one failed |

```json
{
  "code": "00000",
  "data": {
    "successList": [
      {
        "orderId": "121211212122",
        "clientOid": "BITGET#121211212122"
      }
    ],
    "failureList": [],
    "result": true
  },
  "msg": "success",
  "requestTime": 1627293504612
}
```

## Modify Order

`POST /api/v2/mix/order/modify-order`

Speed limit is 10 times/s for average users. Frequency limit imposed according to user ID

Interface for order modification, used to modify an pending order, such as its TP/SL and/or price/size.

Modifying size and price will cancel the old order; then create a **new order** asynchronously, modify the preset TPSL will not cancel the old order.

Modifying size and price, please pass in both, not just one of them

Modify the order price, size and preset TPSL according to orderId or clientOId

It is only allowed to modify the new status limit order. If the size, price and TPSL all is set in the request, then the TPSL will not work

Modify the limit order price and size, please be sure to provide newClientOid, because the orderId of the new order cannot be returned synchronously, so you need to use newClientOid to help you query order information

Modifying the order size needs to meet the minimum order quantity

If you only modify the TPSL, please do not pass price and size. If you only pass one of TP or SL, the other one will be cancelled

Operation ID: `classicContractTradeModifyOrder`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| orderId | string |  | Order ID<br><br>Either orderId or clientOid is required. If both are entered, orderId prevails. |
| clientOid | string |  | Customize order ID <br><br>Either orderId or clientOid is required. If both are entered, orderId prevails. |
| symbol | string | 是 | Trading pair, e.g. ETHUSDT |
| productType | string | 是 | Product type<br><br>`USDT-FUTURES` USDT-M Futures<br><br>`COIN-FUTURES` Coin-M Futures<br><br>`USDC-FUTURES` USDC-M Futures |
| newClientOid | string | 是 | New customized order ID after order modification |
| newSize | string |  | Amount of the modified transaction<br><br>The amount stays unchanged if the field if left blank. |
| newPrice | string |  | Modified price for placing new orders.<br><br>1. When the existing order type is Limit, the original price will be maintained if the field is left empty.<br><br>2. When the existing order type is Limit market, the field should not be set. |
| newPresetStopSurplusPrice | string |  | Modifying take-profit<br><br>1. If the original order has take-profit set and the field is empty, the original value will be kept.<br><br>2. If the original order has take-profit set and the field is filled in with a value, TP will be updated; if the original order has take-profit set and the field is not set, a new take-profit value will be added.<br><br>If there was a TP value and a 0 is filled in the filled, the existing TP will be deleted. |
| newPresetStopLossPrice | string |  | Modifying stop-loss<br><br>1. If the original order has stop-loss set and the field is empty, the original value will be kept.<br><br>2. If the original order has stop-loss set and the field is filled in with a value, TP will be updated; if the original order has stop-loss set and the field is not set, a new stop-loss value will be added.<br><br>If there was a SL value and a 0 is filled in the filled, the existing SL will be deleted. |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.orderId | string |  | Order ID |
| data.clientOid | string |  | Customize order ID |

```json
{
  "code": "00000",
  "data": {
    "orderId": "121212121212",
    "clientOid": "BITGET#121212121212"
  },
  "msg": "success",
  "requestTime": 1627293504612
}
```

## Cancel Order

`POST /api/v2/mix/order/cancel-order`

Frequency limit: 10 times/1s

Cancel a pending order

Operation ID: `classicContractTradeCancelOrder`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| symbol | string | 是 | Trading pair |
| productType | string | 是 | Product type<br><br>`USDT-FUTURES` USDT-M Futures<br><br>`COIN-FUTURES` Coin-M Futures<br><br>`USDC-FUTURES` USDC-M Futures |
| marginCoin | string |  | Margin coin must be capitalized |
| orderId | string |  | Order ID<br><br>Either orderId or clientOid is required.<br><br>If both are present, orderId prevails. |
| clientOid | string |  | Customize order ID<br><br>Either orderId or clientOid is required.<br><br>If both are present, orderId prevails. |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.orderId | string |  | Order ID |
| data.clientOid | string |  | Client customized ID |

```json
{
  "code": "00000",
  "data": {
    "orderId": "123",
    "clientOid": ""
  },
  "msg": "success",
  "requestTime": 1627293504612
}
```

## Batch Cancel

`POST /api/v2/mix/order/batch-cancel-orders`

Speed limit is 10 times/s for average users. Frequency limit imposed according to user ID

Order cancelling interface, can be used to cancel by product type and trading pair.

Operation ID: `classicContractTradeBatchCancelOrders`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| orderIdList | object[] |  | Order ID list.maximum length: 50<br><br>If filled in, symbol must not be null and must be aligned with symbol/productType. |
| orderIdList[].orderId | string |  | Order ID<br><br>Either orderId or clientOid is required. If both are entered, orderId prevails. |
| orderIdList[].clientOid | string |  | Customize order ID<br><br>Either orderId or clientOid is required. If both are entered, orderId prevails. |
| symbol | string |  | Trading pair, e.g. ETHUSDT<br><br>It's required when `orderIdList` is set |
| productType | string | 是 | Product type<br><br>`USDT-FUTURES` USDT-M Futures<br><br>`COIN-FUTURES` Coin-M Futures<br><br>`USDC-FUTURES` USDC-M Futures |
| marginCoin | string |  | Margin coin must be capitalized |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.successList | object[] |  | The collection of successfully cancelled orders. |
| data.successList[].orderId | string |  | Order ID |
| data.successList[].clientOid | string |  | Customize order ID |
| data.failureList | object[] |  | The collection of unsuccessfully cancelled orders. |
| data.failureList[].orderId | string |  | Order ID |
| data.failureList[].clientOid | string |  | Customize order ID |
| data.failureList[].errorMsg | string |  | Failure reason |
| data.failureList[].errorCode | string |  | Error code |

```json
{
  "code": "00000",
  "data": {
    "successList": [
      {
        "orderId": "121211212122",
        "clientOid": "BITGET#121211212122"
      }
    ],
    "failureList": [
      {
        "orderId": "232",
        "clientOid": "321342",
        "errorMsg": "notExistend",
        "errorCode": "43001"
      }
    ]
  },
  "msg": "success",
  "requestTime": 1627293504612
}
```

## Flash Close Position

`POST /api/v2/mix/order/close-positions`

Frequency limit: 1 time/1s (User ID)

close position at market price


**API Broker rebate identifier**:

  The following code block needs to be added to the HTTP Header of the request.

  > "X-CHANNEL-API-CODE":"your-channel-api-code"

Operation ID: `classicContractTradeFlashClosePosition`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| symbol | string |  | Trading pair |
| holdSide | string |  | Position direction<br><br>1. In one-way position mode(buy or sell): This field should be left blank. Will be ignored if filled in.<br><br>2. In hedge-mode position(open or close): All positions will be closed if the field is left blank; Positions of the specified direction will be closed is the field is filled in.<br><br>`long`: Long position; `short`: Short position |
| productType | string | 是 | Product type<br><br>`USDT-FUTURES` USDT-M Futures<br><br>`COIN-FUTURES` Coin-M Futures<br><br>`USDC-FUTURES` USDC-M Futures |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.successList | object[] |  | The collection of successfully closed orders |
| data.successList[].orderId | string |  | Order ID |
| data.successList[].clientOid | string |  | Customize order ID |
| data.successList[].symbol | string |  | The Symbol |
| data.failureList | object[] |  | The collection of unsuccessfully closed orders<br><br>The close order may fail when the pair is in delivery or in risk control handling |
| data.failureList[].orderId | string |  | Order ID |
| data.failureList[].clientOid | string |  | Customize order ID |
| data.failureList[].symbol | string |  | The Symbol |
| data.failureList[].errorMsg | string |  | Failure reason |
| data.failureList[].errorCode | string |  | Failure code |

```json
{
  "code": "00000",
  "data": {
    "successList": [
      {
        "orderId": "123",
        "clientOid": "xxxxx",
        "symbol": "BTCUSDT"
      }
    ],
    "failureList": [
      {
        "orderId": "1234",
        "clientOid": "321",
        "symbol": "BTCUSDT",
        "errorMsg": "xxx",
        "errorCode": "xxxx"
      }
    ]
  },
  "msg": "success",
  "requestTime": 1627293504612
}
```

## Get Order Detail

`GET /api/v2/mix/order/detail`

Frequency limit: 10 times/1s (uid)

Get order detail

Operation ID: `classicContractTradeGetOrderDetails`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | Product ID must be capitalized |
| productType | query | string | 是 | Product type<br><br>`USDT-FUTURES` USDT-M Futures<br><br>`COIN-FUTURES` Coin-M Futures<br><br>`USDC-FUTURES` USDC-M Futures |
| orderId | query | string |  | Order ID<br><br> Either 'orderId' or 'clientOid' is required. |
| clientOid | query | string |  | Custom order ID<br><br>Either 'orderId' or 'clientOid' is required. |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.symbol | string |  | Trading pair |
| data.size | string |  | Amount |
| data.orderId | string |  | Order ID |
| data.clientOid | string |  | Customize order ID |
| data.baseVolume | string |  | Amount of coins traded |
| data.priceAvg | string |  | Average price |
| data.fee | string |  | Transaction fee |
| data.price | string |  | Order price |
| data.state | string |  | Order status<br><br>`live`: New order, waiting for a match in orderbook<br><br>`partially_filled`: Partially filled<br><br>`filled`: All filled<br><br>`canceled`: the order is cancelled |
| data.side | string |  | Direction<br><br>`buy`<br><br>`sell` |
| data.force | string |  | Order expiration date<br><br>`ioc`: Immediate or cancel<br><br>`fok`: Fill or kill<br><br>`gtc`: Good till canceled<br><br>`post only`: post only orders |
| data.totalProfits | string |  | Total PnL |
| data.posSide | string |  | Position direction<br><br>`long`: hedge mode long position<br><br>`short`: hedge mode short position<br><br>`net`: one-way position |
| data.marginCoin | string |  | Margin coin |
| data.presetStopSurplusPrice | string |  | Set TP |
| data.presetStopSurplusType | string |  | Preset Take Profit Trigger type<br><br>fill_price: market price;<br><br>mark_price: mark price |
| data.presetStopSurplusExecutePrice | string |  | Preset Take Profit Execution price |
| data.presetStopLossPrice | string |  | Set SL |
| data.presetStopLossType | string |  | Preset Stop Loss Trigger type<br><br>fill_price: market price;<br><br>mark_price: mark price |
| data.presetStopLossExecutePrice | string |  | Preset Stop Loss Execution price |
| data.quoteVolume | string |  | Trading amount in quoting coin |
| data.orderType | string |  | Order type <br><br>`limit` <br><br>`market` |
| data.leverage | string |  | Leverage |
| data.marginMode | string |  | Margin mode<br><br>`isolated`: isolated margin<br><br>`crossed`: cross margin |
| data.reduceOnly | string |  | Whether or not to just reduce the position.<br><br>`YES`<br><br>`NO` |
| data.enterPointSource | string |  | Order source<br><br>WEB: Orders created on the website<br><br>API: Orders created on API<br><br>SYS: System managed orders, usually generated by forced liquidation logic<br><br>ANDROID: Orders created on the Android app<br><br>IOS: Orders created on the iOS app |
| data.tradeSide | string |  | Direction<br><br>`close`: Close (open and close mode)<br><br>`open`: Open (open and close mode)<br><br>`reduce_close_long`: Liquidate partial long positions for hedge position mode<br><br>`reduce_close_short`：Liquidate partial short positions for hedge position mode<br><br>`burst_close_long`：Liquidate long positions for hedge position mode<br><br>`burst_close_short`：Liquidate short positions for hedge position mode<br><br>`offset_close_long`：Liquidate partial long positions for netting for hedge position mode<br><br>`offset_close_short`：Liquidate partial short positions for netting for hedge position mode<br><br>`delivery_close_long`：Delivery long positions for hedge position mode<br><br>`delivery_close_short`：Delivery short positions for hedge position mode<br><br>`dte_sys_adl_close_long`：ADL close long position for hedge position mode<br><br>`dte_sys_adl_close_short`：ADL close short position for hedge position mode<br><br>`buy_single`：Buy, one way postion mode<br><br>`sell_single`：Sell, one way postion mode<br><br>`reduce_buy_single`：Liquidate partial positions, buy, one way position mode<br><br>`reduce_sell_single`：Liquidate partial positions, sell, one way position mode<br><br>`burst_buy_single`：Liquidate short positions, buy, one way postion mode<br><br>`burst_sell_single`：Liquidate partial positions, sell, one way position mode<br><br>`delivery_sell_single`：Delivery sell, one way position mode<br><br>`delivery_buy_single`：Delivery buy, one way position mode<br><br>`dte_sys_adl_buy_in_single_side_mode`：ADL close position, buy, one way position mode<br><br>`dte_sys_adl_sell_in_single_side_mode`：ADL close position, sell, one way position mode |
| data.newTradeSide | string |  | Trade direction (new). Returned together with `tradeSide` for upgraded accounts; may be `null` for legacy orders |
| data.posMode | string |  | Position mode<br><br>`one_way_mode`: one-way position<br><br>`hedge_mode`: two-way position |
| data.orderSource | string |  | Order source<br><br>normal: Normal order<br><br>market: market order<br><br>profit_market: Market TP order<br><br>loss_market: Market SL order<br><br>Trader_delegate: Elite trade order<br><br>trader_profit: Trader takes profit<br><br>trader_loss: Trader stops loss<br><br>reverse: Reversed orders<br><br>trader_reverse: Reversed elite trades<br><br>profit_limit: Take-profit limit order<br><br>loss_limit: Stop-loss limit order<br><br>liquidation: Liquidation order<br><br>delivery_close_long: close long positions<br><br>delivery_close_short: close short positions<br><br>pos_profit_limit: Position take-profit limit order<br><br>pos_profit_market: Position take-profit market order<br><br>pos_loss_limit: Position stop-loss limit order<br><br>pos_loss_market: Position stop-loss market order<br><br>profit_chase:        Take Profit Chase Order<br><br>loss_chase:         Stop Loss Chase Order<br><br>follower_delegate:         Follower Delegate Order<br><br>reduce_offset:        Reduce Position Offset Order<br><br>market_risk:         Best Price Risk Handling<br><br>plan_limit:         Limit Plan Order<br><br>plan_market:         Best Price Plan Order<br><br>pos_loss_limit:         Position Stop Loss Limit<br><br>strategy_positive:         Strategy-Positive Grid<br><br>strategy_reverse:         Strategy-Reverse Grid<br><br>strategy_unlimited:         Unlimited Strategy<br><br>move_limit:         Limit Moving Take Profit and Stop Loss<br><br>move_market:         Best Price Moving Take Profit and Stop Loss<br><br>tracking_limit:         Limit Trailing Order<br><br>tracking_market:         Best Price Trailing Order<br><br>strategy_dca_positive:         DCA Strategy-Positive<br><br>strategy_dca_reverse:         DCA Strategy-Reverse<br><br>strategy_oco_limit:         Strategy-OCO Limit Order<br><br>strategy_oco_trigger:         Strategy-OCO Trigger Order<br><br>modify_order_limit:         Limit Modify Order<br><br>strategy_regular_buy:         Strategy-Regular Buy<br><br>strategy_grid_middle:         Strategy-Neutral Grid |
| data.cancelReason | string |  | Cancel reason<br><br>`normal_cancel`: Normal cancel<br><br>`stp_cancel`: Cancelled by STP |
| data.cTime | string |  | Creation time, ms |
| data.uTime | string |  | Update time, ms |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695823012595,
  "data": {
    "symbol": "ethusdt",
    "size": "2",
    "orderId": "123456",
    "clientOid": "77777",
    "baseVolume": "2",
    "priceAvg": "1900",
    "fee": "",
    "price": "1900",
    "state": "filled",
    "side": "buy",
    "force": "gtc",
    "totalProfits": "2112",
    "posSide": "long",
    "marginCoin": "usdt",
    "presetStopSurplusPrice": "1910",
    "presetStopSurplusType": "fill_price",
    "presetStopSurplusExecutePrice": "1911",
    "presetStopLossPrice": "1890",
    "presetStopLossType": "fill_price",
    "presetStopLossExecutePrice": "1989",
    "quoteVolume": "1900",
    "orderType": "limit",
    "leverage": "20",
    "marginMode": "cross",
    "reduceOnly": "yes",
    "enterPointSource": "api",
    "tradeSide": "",
    "newTradeSide": null,
    "posMode": "one_way_mode",
    "orderSource": "normal",
    "cancelReason": "",
    "cTime": "1627300098776",
    "uTime": "1627300098776"
  }
}
```

## Get Order Fill Details

`GET /api/v2/mix/order/fills`

Speed limit is 10 times/s for average users. Frequency limit imposed according to user ID

Get order fill details

You can export your historical orders on our <a href="https://www.bitget.com/asset/export/downOrders">web</a>.

Operation ID: `classicContractTradeGetOrderFills`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| orderId | query | string |  | Order ID |
| symbol | query | string |  | Trading pair, e.g. ETHUSDT |
| productType | query | string | 是 | Product type<br><br>`USDT-FUTURES` USDT-M Futures<br><br>`COIN-FUTURES` Coin-M Futures<br><br>`USDC-FUTURES` USDC-M Futures |
| idLessThan | query | string |  | Requests the content on the page before the `tradeId` (older data). |
| startTime | query | string |  | Start time (time stamp in milliseconds)<br><br>(The maximum time span supported is three months. The default end time is three months if no value is set for the end time. )<br><br> (For Managed Sub-Account, the StartTime cannot be earlier than the binding time) |
| endTime | query | string |  | End time (time stamp in milliseconds)<br><br>(The maximum time span supported is three months. The default start time is three months ago if no value is set for the start time. ) |
| limit | query | string |  | Number of queries: Default: 100, maximum: 100 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.fillList | object[] |  | Transaction details |
| data.fillList[].tradeId | string |  | Transaction id |
| data.fillList[].symbol | string |  | Trading pair |
| data.fillList[].orderId | string |  | Order no. |
| data.fillList[].price | string |  | Order price |
| data.fillList[].baseVolume | string |  | Amount of coins traded |
| data.fillList[].feeDetail | object[] |  | Transaction fee |
| data.fillList[].feeDetail[].deduction | string |  | Whether or not to deduct (vouchers) |
| data.fillList[].feeDetail[].feeCoin | string |  | Crypto ticker |
| data.fillList[].feeDetail[].totalDeductionFee | string |  | Total transaction fee discount |
| data.fillList[].feeDetail[].totalFee | string |  | Total transaction fee |
| data.fillList[].side | string |  | Type of transaction<br><br>buy: Buy<br><br>sell: Sell |
| data.fillList[].quoteVolume | string |  | Trading amount in quote currency |
| data.fillList[].profit | string |  | Profit |
| data.fillList[].enterPointSource | string |  | Order source<br><br>WEB: Orders created on the website<br><br>API: Orders created on API<br><br>SYS: System managed orders, usually generated by forced liquidation logic<br><br>ANDROID: Orders created on the Android app<br><br>IOS: Orders created on the iOS app |
| data.fillList[].tradeSide | string |  | Direction<br><br>`close`: Close (open and close mode)<br><br>`open`: Open (open and close mode)<br><br>`reduce_close_long`: Liquidate partial long positions for hedge position mode<br><br>`reduce_close_short`：Liquidate partial short positions for hedge position mode<br><br>`burst_close_long`：Liquidate long positions for hedge position mode<br><br>`burst_close_short`：Liquidate short positions for hedge position mode<br><br>`offset_close_long`：Liquidate partial long positions for netting for hedge position mode<br><br>`offset_close_short`：Liquidate partial short positions for netting for hedge position mode<br><br>`delivery_close_long`：Delivery long positions for hedge position mode<br><br>`delivery_close_short`：Delivery short positions for hedge position mode<br><br>`dte_sys_adl_close_long`：ADL close long position for hedge position mode<br><br>`dte_sys_adl_close_short`：ADL close short position for hedge position mode<br><br>`buy_single`：Buy, one way postion mode<br><br>`sell_single`：Sell, one way postion mode<br><br>`reduce_buy_single`：Liquidate partial positions, buy, one way position mode<br><br>`reduce_sell_single`：Liquidate partial positions, sell, one way position mode<br><br>`burst_buy_single`：Liquidate short positions, buy, one way postion mode<br><br>`burst_sell_single`：Liquidate partial positions, sell, one way position mode<br><br>`delivery_sell_single`：Delivery sell, one way position mode<br><br>`delivery_buy_single`：Delivery buy, one way position mode<br><br>`dte_sys_adl_buy_in_single_side_mode`：ADL close position, buy, one way position mode<br><br>`dte_sys_adl_sell_in_single_side_mode`：ADL close position, sell, one way position mode |
| data.fillList[].posMode | string |  | Position mode <br><br>`one_way_mode`: one-way position<br><br>`hedge_mode`: two-way position |
| data.fillList[].tradeScope | string |  | Trader tag<br><br>taker: Taker<br><br>maker: Maker |
| data.fillList[].cTime | string |  | Date of transaction<br><br>endId<br><br>String<br><br>The final order ID.<br><br>This is used when idLessThan/idGreaterThan is set as a range. |
| data.endId | string |  | The final Transaction ID.<br><br>This is used when idLessThan/idGreaterThan is set as a range. |

```json
{
  "code": "00000",
  "data": {
    "fillList": [
      {
        "tradeId": "123",
        "symbol": "ethusdt",
        "orderId": "121212",
        "price": "1900",
        "baseVolume": "1",
        "feeDetail": [
          {
            "deduction": "yes",
            "feeCoin": "BGB",
            "totalDeductionFee": "-0.017118519726",
            "totalFee": "-0.017118519726"
          }
        ],
        "side": "buy",
        "quoteVolume": "1902",
        "profit": "102",
        "enterPointSource": "api",
        "tradeSide": "close",
        "posMode": "hedge_mode",
        "tradeScope": "taker",
        "cTime": "1627293509612"
      }
    ],
    "endId": "123"
  },
  "msg": "success",
  "requestTime": 1627293504612
}
```

## Get Historical Transaction Details

`GET /api/v2/mix/order/fill-history`

Frequency limit: 10 times/1s (uid)

Get order fill history

You can export your historical orders on our <a href="https://www.bitget.com/asset/export/downOrders">web</a>.

Operation ID: `classicContractTradeGetFillHistory`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| orderId | query | string |  | Order ID<br><br>Either orderId or clientOid is required. If both are entered, orderId prevails. |
| symbol | query | string |  | Trading pair, e.g. ETHUSDT |
| productType | query | string | 是 | Product type<br><br>`USDT-FUTURES` USDT-M Futures<br><br>`COIN-FUTURES` Coin-M Futures<br><br>`USDC-FUTURES` USDC-M Futures<br><br>It does not support to query the data in demo trading |
| startTime | query | string |  | Start timestamp <br><br>Unix timestamp in milliseconds format, e.g. 1597026383085<br><br>(The maximum time span supported is a week. The default end time is a week if no value is set for the end time. ) <br><br> (For Managed Sub-Account, the StartTime cannot be earlier than the binding time) |
| endTime | query | string |  | End timestamp <br><br>Unix timestamp in milliseconds format, e.g. 1597026383085<br><br>(The maximum time span supported is a week. The default start time is a week ago if no value is set for the start time. ) |
| idLessThan | query | string |  | Requests the content on the page before this ID (older data), the value input should be the endId of the corresponding interface. |
| limit | query | string |  | Number of queries: Maximum: 100, default: 100 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.endId | string |  | Last query ended order ID |
| data.fillList | object[] |  | Order list |
| data.fillList[].symbol | string |  | Trading pair |
| data.fillList[].marginCoin | string |  | Margin Coin |
| data.fillList[].tradeId | string |  | Transaction ID |
| data.fillList[].orderId | string |  | order id |
| data.fillList[].price | string |  | deal price |
| data.fillList[].baseVolume | string |  | Amount of coins traded |
| data.fillList[].feeDetail | object[] |  | Transaction fee |
| data.fillList[].feeDetail[].deduction | string |  | Whether or not to deduct (vouchers) |
| data.fillList[].feeDetail[].feeCoin | string |  | Crypto ticker |
| data.fillList[].feeDetail[].totalDeductionFee | string |  | Total transaction fee discount |
| data.fillList[].feeDetail[].totalFee | string |  | Total transaction fee |
| data.fillList[].side | string |  | Direction<br><br>Buy; Sell |
| data.fillList[].quoteVolume | string |  | Trading amount in quoting coin |
| data.fillList[].profit | string |  | profit |
| data.fillList[].enterPointSource | string |  | Order source<br><br>WEB: Orders created on the website<br><br>API: Orders created on API<br><br>SYS: System managed orders, usually generated by forced liquidation logic<br><br>ANDROID: Orders created on the Android app<br><br>IOS: Orders created on the iOS app |
| data.fillList[].tradeSide | string |  | Direction<br><br>`close`: Close (open and close mode)<br><br>`open`: Open (open and close mode)<br><br>`reduce_close_long`: Liquidate partial long positions for hedge position mode<br><br>`reduce_close_short`：Liquidate partial short positions for hedge position mode<br><br>`burst_close_long`：Liquidate long positions for hedge position mode<br><br>`burst_close_short`：Liquidate short positions for hedge position mode<br><br>`offset_close_long`：Liquidate partial long positions for netting for hedge position mode<br><br>`offset_close_short`：Liquidate partial short positions for netting for hedge position mode<br><br>`delivery_close_long`：Delivery long positions for hedge position mode<br><br>`delivery_close_short`：Delivery short positions for hedge position mode<br><br>`dte_sys_adl_close_long`：ADL close long position for hedge position mode<br><br>`dte_sys_adl_close_short`：ADL close short position for hedge position mode<br><br>`buy_single`：Buy, one way postion mode<br><br>`sell_single`：Sell, one way postion mode<br><br>`reduce_buy_single`：Liquidate partial positions, buy, one way position mode<br><br>`reduce_sell_single`：Liquidate partial positions, sell, one way position mode<br><br>`burst_buy_single`：Liquidate short positions, buy, one way postion mode<br><br>`burst_sell_single`：Liquidate partial positions, sell, one way position mode<br><br>`delivery_sell_single`：Delivery sell, one way position mode<br><br>`delivery_buy_single`：Delivery buy, one way position mode<br><br>`dte_sys_adl_buy_in_single_side_mode`：ADL close position, buy, one way position mode<br><br>`dte_sys_adl_sell_in_single_side_mode`：ADL close position, sell, one way position mode |
| data.fillList[].posMode | string |  | Position mode<br><br>one_way_mode: one-way position<br><br>hedge_mode: two-way position |
| data.fillList[].tradeScope | string |  | Trader tag<br><br>taker: Taker<br><br>maker: Maker |
| data.fillList[].cTime | string |  | Date of transaction<br><br>endId<br><br>String<br><br>The final order ID.<br><br>This is used when idLessThan/idGreaterThan is set as a range. |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1699267238892,
  "data": {
    "fillList": [
      {
        "tradeId": "xxxx",
        "symbol": "ETHUSDT",
        "marginCoin": "USDT",
        "orderId": "xxxx",
        "price": "1801.33",
        "baseVolume": "0.02",
        "feeDetail": [
          {
            "deduction": "no",
            "feeCoin": "USDT",
            "totalDeductionFee": "0",
            "totalFee": "-0.02161596"
          }
        ],
        "side": "sell",
        "quoteVolume": "36.0266",
        "profit": "0.0252",
        "enterPointSource": "ios",
        "tradeSide": "sell_single",
        "posMode": "one_way_mode",
        "tradeScope": "taker",
        "cTime": "1698730804882"
      }
    ],
    "endId": "123456789"
  }
}
```

## Get Pending Orders

`GET /api/v2/mix/order/orders-pending`

Rate limit: 10 req/sec/UID

To query all existing pending orders.

Operation ID: `classicContractTradeGetOrdersPending`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| orderId | query | string |  | Order ID;<br><br>If both orderId and clientOidare entered, orderId prevails. |
| clientOid | query | string |  | Customize order ID;<br><br>If both orderId and clientOid are entered, orderId prevails. |
| symbol | query | string |  | Trading pair, e.g. ETHUSDT |
| productType | query | string | 是 | Product type<br><br>`USDT-FUTURES` USDT-M Futures<br><br>`COIN-FUTURES` Coin-M Futures<br><br>`USDC-FUTURES` USDC-M Futures |
| status | query | string |  | Order status<br><br>If not specified, all ordered with a status of live (not filled yet) will be returned.<br><br>`live`: pending orders<br><br>`partially_filled`: Partially filled |
| idLessThan | query | string |  | Requests the content on the page before this ID (older data), the value input should be the endId of the corresponding interface. |
| startTime | query | string |  | Start timestamp <br><br>Unix timestamp in milliseconds format, e.g. 1597026383085<br><br>(The maximum time span supported is three months. The default end time is three months if no value is set for the end time. ) |
| endTime | query | string |  | End timestamp <br><br>Unix timestamp in milliseconds format, e.g. 1597026383085<br><br>(The maximum time span supported is three months. The default start time is three months ago if no value is set for the start time. ) |
| limit | query | string |  | Number of queries: Maximum: 100, default: 100 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.entrustedList | object[] |  | Order list |
| data.entrustedList[].symbol | string |  | Trading pair |
| data.entrustedList[].size | string |  | Amount |
| data.entrustedList[].orderId | string |  | Order ID |
| data.entrustedList[].clientOid | string |  | Custom id |
| data.entrustedList[].baseVolume | string |  | Amount of coins traded |
| data.entrustedList[].fee | string |  | Transaction fee |
| data.entrustedList[].price | string |  | Order price |
| data.entrustedList[].priceAvg | string |  | Average order price<br><br>Empty when status is `live` |
| data.entrustedList[].status | string |  | Order status<br><br>`live`: Waiting to be filled (not filled yet)<br><br>`partially_filled`: Partially filled |
| data.entrustedList[].side | string |  | Direction<br><br>`buy`: Buy; `sell`: Sell |
| data.entrustedList[].force | string |  | Order expiration date<br><br>`ioc` (Immediate or cancel)<br><br>`fok` (Fill or kill)<br><br>`gtc` (Good till canceled)<br><br>`post_only`: Post only |
| data.entrustedList[].totalProfits | string |  | Total PnL<br><br>Empty when status is live. |
| data.entrustedList[].posSide | string |  | Position direction<br><br>`long`: two-way long position<br><br>`short`: two-way short position<br><br>`net`: one-way position |
| data.entrustedList[].marginCoin | string |  | Margin coin |
| data.entrustedList[].quoteVolume | string |  | Trading amount in quoting coin |
| data.entrustedList[].leverage | string |  | Leverage |
| data.entrustedList[].marginMode | string |  | Margin mode<br><br>`isolated`: isolated margin<br><br>`crossed`: cross margin |
| data.entrustedList[].reduceOnly | string |  | Reduce only<br><br>`YES`: yes, `NO`: no |
| data.entrustedList[].enterPointSource | string |  | Order source<br><br>WEB: Orders created on the website<br><br>API: Orders created on API<br><br>SYS: System managed orders, usually generated by forced liquidation logic<br><br>ANDROID: Orders created on the Android app<br><br>IOS: Orders created on the iOS app |
| data.entrustedList[].tradeSide | string |  | Direction<br><br>`close`: Close (open and close mode)<br><br>`open`: Open (open and close mode)<br><br>`reduce_close_long`: Liquidate partial long positions for hedge position mode<br><br>`reduce_close_short`：Liquidate partial short positions for hedge position mode<br><br>`burst_close_long`：Liquidate long positions for hedge position mode<br><br>`burst_close_short`：Liquidate short positions for hedge position mode<br><br>`offset_close_long`：Liquidate partial long positions for netting for hedge position mode<br><br>`offset_close_short`：Liquidate partial short positions for netting for hedge position mode<br><br>`delivery_close_long`：Delivery long positions for hedge position mode<br><br>`delivery_close_short`：Delivery short positions for hedge position mode<br><br>`dte_sys_adl_close_long`：ADL close long position for hedge position mode<br><br>`dte_sys_adl_close_short`：ADL close short position for hedge position mode<br><br>`buy_single`：Buy, one way postion mode<br><br>`sell_single`：Sell, one way postion mode<br><br>`reduce_buy_single`：Liquidate partial positions, buy, one way position mode<br><br>`reduce_sell_single`：Liquidate partial positions, sell, one way position mode<br><br>`burst_buy_single`：Liquidate short positions, buy, one way postion mode<br><br>`burst_sell_single`：Liquidate partial positions, sell, one way position mode<br><br>`delivery_sell_single`：Delivery sell, one way position mode<br><br>`delivery_buy_single`：Delivery buy, one way position mode<br><br>`dte_sys_adl_buy_in_single_side_mode`：ADL close position, buy, one way position mode<br><br>`dte_sys_adl_sell_in_single_side_mode`：ADL close position, sell, one way position mode |
| data.entrustedList[].posMode | string |  | Position mode<br><br>`one_way_mode`: one-way position<br><br>`hedge_mode`: two-way position |
| data.entrustedList[].orderType | string |  | Order type<br><br>limit: limit order<br><br>market: market order |
| data.entrustedList[].orderSource | string |  | Order sources<br><br>normal: Normal order<br><br>market: market order<br><br>profit_market: Market TP order<br><br>loss_market: Market SL order<br><br>Trader_delegate: Elite trade order<br><br>trader_profit: Trader takes profit<br><br>trader_loss: Trader stops loss<br><br>reverse: Reversed orders<br><br>trader_reverse: Reversed elite trades<br><br>profit_limit: Take-profit limit order<br><br>loss_limit: Stop-loss limit order<br><br>liquidation: Liquidation order<br><br>delivery_close_long: close long positions<br><br>delivery_close_short: close short positions<br><br>pos_profit_limit: Position take-profit limit order<br><br>pos_profit_market: Position take-profit market order<br><br>pos_loss_limit: Position stop-loss limit order<br><br>pos_loss_market: Position stop-loss market order<br><br>profit_chase:        Take Profit Chase Order<br><br>loss_chase:         Stop Loss Chase Order<br><br>follower_delegate:         Follower Delegate Order<br><br>reduce_offset:        Reduce Position Offset Order<br><br>market_risk:         Best Price Risk Handling<br><br>plan_limit:         Limit Plan Order<br><br>plan_market:         Best Price Plan Order<br><br>pos_loss_limit:         Position Stop Loss Limit<br><br>strategy_positive:         Strategy-Positive Grid<br><br>strategy_reverse:         Strategy-Reverse Grid<br><br>strategy_unlimited:         Unlimited Strategy<br><br>move_limit:         Limit Moving Take Profit and Stop Loss<br><br>move_market:         Best Price Moving Take Profit and Stop Loss<br><br>tracking_limit:         Limit Trailing Order<br><br>tracking_market:         Best Price Trailing Order<br><br>strategy_dca_positive:         DCA Strategy-Positive<br><br>strategy_dca_reverse:         DCA Strategy-Reverse<br><br>strategy_oco_limit:         Strategy-OCO Limit Order<br><br>strategy_oco_trigger:         Strategy-OCO Trigger Order<br><br>modify_order_limit:         Limit Modify Order<br><br>strategy_regular_buy:         Strategy-Regular Buy<br><br>strategy_grid_middle:         Strategy-Neutral Grid<br><br>off_close:         Delisting liquidation |
| data.entrustedList[].cTime | string |  | Creation time, ms |
| data.entrustedList[].uTime | string |  | Last updated time, ms |
| data.entrustedList[].presetStopSurplusPrice | string |  | Take Profit Trigger Price |
| data.entrustedList[].presetStopSurplusTriggerType | string |  | Setting take-profit trigger type<br><br>fill_price: filled price<br><br>mark_price: mark price |
| data.entrustedList[].presetStopSurplusExecutePrice | string |  | Take Profit Execution price<br><br>If it is 0 or not filled in, it means market price execution.If it is greater than 0, it means limit price execution. |
| data.entrustedList[].presetStopLossPrice | string |  | Stop Loss Trigger Price |
| data.entrustedList[].presetStopLossTriggerType | string |  | Setting stop-loss trigger type<br><br>fill_price: filled price<br><br>mark_price: mark price |
| data.entrustedList[].presetStopLossExecutePrice | string |  | Stop Loss Execution price<br><br>If it is 0 or not filled in, it means market price execution.If it is greater than 0, it means limit price execution. |
| data.endId | string |  | The final order ID.<br><br>This is used when idLessThan/idGreaterThan is set as a range. |

```json
{
  "code": "00000",
  "data": {
    "entrustedList": [
      {
        "symbol": "ethusdt",
        "size": "100",
        "orderId": "123",
        "clientOid": "12321",
        "baseVolume": "12.1",
        "fee": "",
        "price": "1900",
        "priceAvg": "1903",
        "status": "partially_filled",
        "side": "buy",
        "force": "gtc",
        "totalProfits": "0",
        "posSide": "long",
        "marginCoin": "usdt",
        "quoteVolume": "22001.21",
        "leverage": "20",
        "marginMode": "cross",
        "enterPointSource": "api",
        "tradeSide": "open",
        "posMode": "hedge_mode",
        "orderType": "limit",
        "orderSource": "normal",
        "cTime": "1627293504612",
        "uTime": "1627293505612",
        "presetStopSurplusPrice": "2001",
        "presetStopSurplusTriggerType": "mark_price",
        "presetStopSurplusExecutePrice": "2201",
        "presetStopLossPrice": "1800",
        "presetStopLossTriggerType": "mark_price",
        "presetStopLossExecutePrice": "1900"
      }
    ],
    "endId": "123"
  },
  "msg": "success",
  "requestTime": 1627293504612
}
```

## Get History Order

`GET /api/v2/mix/order/orders-history`

Rate limit: 10 req/sec/UID

Get history order(It only supports to get the data within 90days. The older data can be downloaded from web)

You can export your historical orders on our <a href="https://www.bitget.com/asset/export/downOrders">web</a>.

Operation ID: `classicContractTradeGetOrdersHistory`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| orderId | query | string |  | Order ID<br><br> If both orderId and clientOid are entered, orderId prevails. |
| clientOid | query | string |  | Customize order ID<br><br>If both orderId and clientOid are entered, orderId prevails. |
| symbol | query | string |  | Trading pair, e.g. ETHUSDT |
| productType | query | string | 是 | Product type<br><br>`USDT-FUTURES` USDT-M Futures<br><br>`COIN-FUTURES` Coin-M Futures<br><br>`USDC-FUTURES` USDC-M Futures |
| idLessThan | query | string |  | Requests the content on the page before this ID (older data), the value input should be the endId of the previous request response |
| orderSource | query | string |  | Order sources<br><br>normal: Normal order<br><br>market: market order<br><br>profit_market: Market TP order<br><br>loss_market: Market SL order<br><br>Trader_delegate: Elite trade order<br><br>trader_profit: Trader takes profit<br><br>trader_loss: Trader stops loss<br><br>reverse: Reversed orders<br><br>trader_reverse: Reversed elite trades<br><br>profit_limit: Take-profit limit order<br><br>loss_limit: Stop-loss limit order<br><br>liquidation: Liquidation order<br><br>delivery_close_long: close long positions<br><br>delivery_close_short: close short positions<br><br>pos_profit_limit: Position take-profit limit order<br><br>pos_profit_market: Position take-profit market order<br><br>pos_loss_limit: Position stop-loss limit order<br><br>pos_loss_market: Position stop-loss market order |
| startTime | query | string |  | Start timestamp <br><br>Unix timestamp in milliseconds format, e.g. 1597026383085<br><br> (For Managed Sub-Account, the StartTime cannot be earlier than the binding time) |
| endTime | query | string |  | End timestamp <br><br>Unix timestamp in milliseconds format, e.g. 1597026383085 |
| limit | query | string |  | Number of queries: Maximum: 100, default: 100 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.endId | string |  | Last query ended order ID |
| data.entrustedList | object[] |  | Order list |
| data.entrustedList[].symbol | string |  | Trading pair |
| data.entrustedList[].size | string |  | Amount |
| data.entrustedList[].orderId | string |  | Order ID |
| data.entrustedList[].clientOid | string |  | Custom id |
| data.entrustedList[].baseVolume | string |  | Amount of coins traded |
| data.entrustedList[].fee | string |  | Transaction fee |
| data.entrustedList[].price | string |  | Order price |
| data.entrustedList[].priceAvg | string |  | Average order price |
| data.entrustedList[].status | string |  | Order status<br><br>`filled`: All filled<br><br>`canceled`: the order is cancelled |
| data.entrustedList[].side | string |  | Direction<br><br>`buy`: buy, `sell`: sell |
| data.entrustedList[].force | string |  | Order expiration date<br><br>(Confirm that if maker is supported)<br><br>`ioc`: Immediate or cancel<br><br>`fok`: Fill or kill<br><br>`gtc`: Good till canceled<br><br>`post_only`: Post only |
| data.entrustedList[].totalProfits | string |  | Total PnL |
| data.entrustedList[].posSide | string |  | Position direction<br><br>`long`: two-way long position<br><br>`short`: two-way short position<br><br>`net`: one-way position |
| data.entrustedList[].marginCoin | string |  | Margin coin |
| data.entrustedList[].quoteVolume | string |  | Trading amount in quoting coin |
| data.entrustedList[].leverage | string |  | Leverage |
| data.entrustedList[].marginMode | string |  | Margin mode<br><br>`isolated`: isolated margin<br><br>`crossed`: cross margin |
| data.entrustedList[].reduceOnly | string |  | Reduce only<br><br>`YES`: Yes,`NO`: No |
| data.entrustedList[].enterPointSource | string |  | Order source<br><br>WEB: Orders created on the website<br><br>API: Orders created on API<br><br>SYS: System managed orders, usually generated by forced liquidation logic<br><br>ANDROID: Orders created on the Android app<br><br>IOS: Orders created on the iOS app |
| data.entrustedList[].tradeSide | string |  | Direction<br><br>`close`: Close (open and close mode)<br><br>`open`: Open (open and close mode)<br><br>`reduce_close_long`: Liquidate partial long positions for hedge position mode<br><br>`reduce_close_short`：Liquidate partial short positions for hedge position mode<br><br>`burst_close_long`：Liquidate long positions for hedge position mode<br><br>`burst_close_short`：Liquidate short positions for hedge position mode<br><br>`offset_close_long`：Liquidate partial long positions for netting for hedge position mode<br><br>`offset_close_short`：Liquidate partial short positions for netting for hedge position mode<br><br>`delivery_close_long`：Delivery long positions for hedge position mode<br><br>`delivery_close_short`：Delivery short positions for hedge position mode<br><br>`dte_sys_adl_close_long`：ADL close long position for hedge position mode<br><br>`dte_sys_adl_close_short`：ADL close short position for hedge position mode<br><br>`buy_single`：Buy, one way postion mode<br><br>`sell_single`：Sell, one way postion mode<br><br>`reduce_buy_single`：Liquidate partial positions, buy, one way position mode<br><br>`reduce_sell_single`：Liquidate partial positions, sell, one way position mode<br><br>`burst_buy_single`：Liquidate short positions, buy, one way postion mode<br><br>`burst_sell_single`：Liquidate partial positions, sell, one way position mode<br><br>`delivery_sell_single`：Delivery sell, one way position mode<br><br>`delivery_buy_single`：Delivery buy, one way position mode<br><br>`dte_sys_adl_buy_in_single_side_mode`：ADL close position, buy, one way position mode<br><br>`dte_sys_adl_sell_in_single_side_mode`：ADL close position, sell, one way position mode |
| data.entrustedList[].posMode | string |  | Position mode<br><br>`one_way_mode`: one-way position<br><br>`hedge_mode`: two-way position |
| data.entrustedList[].orderType | string |  | Order type<br><br>limit: limit order<br><br>market: market order |
| data.entrustedList[].orderSource | string |  | Order sources<br><br>normal: Normal order<br><br>market: market order<br><br>profit_market: Market TP order<br><br>loss_market: Market SL order<br><br>Trader_delegate: Elite trade order<br><br>trader_profit: Trader takes profit<br><br>trader_loss: Trader stops loss<br><br>reverse: Reversed orders<br><br>trader_reverse: Reversed elite trades<br><br>profit_limit: Take-profit limit order<br><br>loss_limit: Stop-loss limit order<br><br>liquidation: Liquidation order<br><br>delivery_close_long: close long positions<br><br>delivery_close_short: close short positions<br><br>pos_profit_limit: Position take-profit limit order<br><br>pos_profit_market: Position take-profit market order<br><br>pos_loss_limit: Position stop-loss limit order<br><br>pos_loss_market: Position stop-loss market order<br><br>profit_chase:        Take Profit Chase Order<br><br>loss_chase:         Stop Loss Chase Order<br><br>follower_delegate:         Follower Delegate Order<br><br>reduce_offset:        Reduce Position Offset Order<br><br>market_risk:         Best Price Risk Handling<br><br>plan_limit:         Limit Plan Order<br><br>plan_market:         Best Price Plan Order<br><br>pos_loss_limit:         Position Stop Loss Limit<br><br>strategy_positive:         Strategy-Positive Grid<br><br>strategy_reverse:         Strategy-Reverse Grid<br><br>strategy_unlimited:         Unlimited Strategy<br><br>move_limit:         Limit Moving Take Profit and Stop Loss<br><br>move_market:         Best Price Moving Take Profit and Stop Loss<br><br>tracking_limit:         Limit Trailing Order<br><br>tracking_market:         Best Price Trailing Order<br><br>strategy_dca_positive:         DCA Strategy-Positive<br><br>strategy_dca_reverse:         DCA Strategy-Reverse<br><br>strategy_oco_limit:         Strategy-OCO Limit Order<br><br>strategy_oco_trigger:         Strategy-OCO Trigger Order<br><br>modify_order_limit:         Limit Modify Order<br><br>strategy_regular_buy:         Strategy-Regular Buy<br><br>strategy_grid_middle:         Strategy-Neutral Grid <br><br>off_close:         Delisting liquidation |
| data.entrustedList[].liqPrice | string |  | liquidation price |
| data.entrustedList[].cTime | string |  | Creation time |
| data.entrustedList[].uTime | string |  | Last updated time |
| data.entrustedList[].presetStopSurplusPrice | string |  | Take profit price |
| data.entrustedList[].presetStopLossPrice | string |  | Stop loss price |
| data.entrustedList[].posAvg | string |  | Average position price |

```json
{
  "code": "00000",
  "data": {
    "entrustedList": [
      {
        "symbol": "ethusdt",
        "size": "100",
        "orderId": "123",
        "clientOid": "12321",
        "baseVolume": "12.1",
        "fee": "-0.00854",
        "price": "1900",
        "priceAvg": "1903",
        "status": "filled",
        "side": "buy",
        "force": "gtc",
        "totalProfits": "0",
        "posSide": "long",
        "marginCoin": "usdt",
        "quoteVolume": "22001.21",
        "leverage": "20",
        "marginMode": "crossed",
        "reduceOnly": "NO",
        "enterPointSource": "api",
        "tradeSide": "open",
        "posMode": "hedge_mode",
        "posAvg": "",
        "orderType": "limit",
        "orderSource": "normal",
        "liqPrice": "",
        "cTime": "1627293504612",
        "uTime": "1627293505612",
        "presetStopSurplusPrice": "2001",
        "presetStopLossPrice": "1800"
      }
    ],
    "endId": "123"
  },
  "msg": "success",
  "requestTime": 1627293504612
}
```

## Cancel All Orders

`POST /api/v2/mix/order/cancel-all-orders`

Rate limit: 10 req/sec/UID

Operation ID: `classicContractTradeCancelAllOrders`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| productType | string | 是 | Product type<br><br>`USDT-FUTURES` USDT-M Futures<br><br>`COIN-FUTURES` Coin-M Futures<br><br>`USDC-FUTURES` USDC-M Futures |
| marginCoin | string |  | Margin coin, must be capitalized |
| requestTime | string |  | request Time Unix millisecond timestamp |
| receiveWindow | string |  | valid window period Unix millisecond timestamp  Unix millisecond timestamp |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.successList | object[] |  | The collection of successfully cancelled orders. |
| data.successList[].orderId | string |  | Order ID |
| data.successList[].clientOid | string |  | Customize order ID |
| data.failureList | object[] |  | The collection of unsuccessfully cancelled orders. |
| data.failureList[].orderId | string |  | Order ID |
| data.failureList[].clientOid | string |  | Customize order ID |
| data.failureList[].errorMsg | string |  | Failure reason |
| data.failureList[].errorCode | string |  | Error code |

```json
{
  "code": "00000",
  "data": {
    "successList": [
      {
        "orderId": "121211212122",
        "clientOid": "BITGET#121211212122"
      }
    ],
    "failureList": [
      {
        "orderId": "232",
        "clientOid": "321342",
        "errorMsg": "notExistend"
      }
    ]
  },
  "msg": "success",
  "requestTime": 1627293504612
}
```


---

经典账户 — 合约下单与订单查询。

版本: 1.0.0

## 服务地址

- `https://api.bitget.com`

## 接口列表

- `POST /api/v2/mix/order/place-order` — 下单
- `POST /api/v2/mix/order/click-backhand` — 一键反手
- `POST /api/v2/mix/order/batch-place-order` — 批量下单
- `POST /api/v2/mix/order/modify-order` — 修改订单
- `POST /api/v2/mix/order/cancel-order` — 撤单
- `POST /api/v2/mix/order/batch-cancel-orders` — 批量撤单
- `POST /api/v2/mix/order/close-positions` — 一键市价平仓
- `GET /api/v2/mix/order/detail` — 获取订单详情
- `GET /api/v2/mix/order/fills` — 获取成交明细
- `GET /api/v2/mix/order/fill-history` — 获取历史成交明细
- `GET /api/v2/mix/order/orders-pending` — 查询当前委托
- `GET /api/v2/mix/order/orders-history` — 获取历史委托
- `POST /api/v2/mix/order/cancel-all-orders` — 一键全撤

## 下单

`POST /api/v2/mix/order/place-order`

普通用户:限速10次/秒，根据uid限频

单向持仓时，必须省略tradeSide参数；

单向持仓时，如果新的reduceOnly单size和现存的reduceOnly单size总和大于仓位size的情况下，会按当前reduceOnly单的创建顺序依次取消挂单，直至新的reduceOnly的size和现存的reduceOnly单的size总和小于等于仓位size。并且最新的reduceOnly单的请求响应不会包含`orderId`，可以通过在请求中添加`clientOid`查询订单详情或者获取当前委托接口查看`orderId`。

双向持仓时，开多规则为：side=buy,tradeSide=open；开空规则为：side=sell,tradeSide=open；平多规则为：side=buy,tradeSide=close；平空规则为：side=sell,tradeSide=close

双向持仓时，如果有限价平仓单占用仓位，此时再下的市价平仓单的数量与限价单平仓的数量超过仓位数量时，不会报仓位不足错误，也不会取消已占用仓位的限价单，而是会直接把限价单平仓的数量保留，平掉仓位数量减去限价单平仓的数量后的数量。例如：仓位数量100，限价单占用70，此时再下50数量的市价单平仓时不会报错仓位不足，也不会取消占用仓位的限价单执行市价单，而是会直接平掉30数量。

双向持仓时，若已有数量等于持仓的限价平仓单，新增平仓单会自动取消已占用仓位的限价单。

为确保带单操作顺利进行，使用新版交易专家的带单 API Key 下单时，请严格按照交易专家可以带单的币对及参数中的币对范围执行。超出公告列表的币对不支持带单下单

**API Broker返佣标识**:

  需在HTTP Header请求头中添加如下代码块

  > "X-CHANNEL-API-CODE":"your-channel-api-code"

Operation ID: `classicContractTradePlaceOrder`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| symbol | string | 是 | 交易对名称 如:"ETHUSDT" |
| productType | string | 是 | 产品类型<br><br>`USDT-FUTURES` U本位合约<br><br>`COIN-FUTURES` 币本位合约<br><br>`USDC-FUTURES` USDC合约 |
| marginMode | string | 是 | 仓位模式<br><br>`isolated`: 逐仓 <br><br>`crossed`: 全仓 |
| marginCoin | string | 是 | 保证金币种(大写), 如:USDT |
| size | string | 是 | 下单数量(基础币)<br><br>数量小数位可以通过获取合约信息 接口获取 |
| price | string |  | 下单价格。<br><br>orderType为`limit`时必填<br><br>价格小数位可以通过获取合约信息 接口获取 |
| side | string | 是 | 交易方向<br><br>`buy`: **单向持仓时**代表买入，**双向持仓时**代表多头方向<br><br>`sell`: **单向持仓**时代表卖出，**双向持仓**时代表空头方向 |
| tradeSide | string |  | 交易类型(仅限双向持仓)<br><br>双向持仓模式下必填，单向持仓时不要填，否则会报错<br><br>`open`: 开仓<br><br>`close`: 平仓 |
| orderType | string | 是 | 订单类型<br><br>`limit`: 限价单，<br><br>`market`: 市价单 |
| force | string |  | 订单有效期<br><br>`ioc`: 无法立即成交的部分就撤销<br><br>`fok`: 无法全部立即成交就撤销<br><br>`gtc`: 普通订单, 订单会一直有效，直到被成交或者取消<br><br>`post_only`: 只做maker<br><br>"orderType"为`limit`限价单时必填，若省略则默认为`gtc` |
| clientOid | string |  | 自定义订单id |
| reduceOnly | string |  | 只减仓(仅适用**单向持仓**模式下)<br><br>`YES`<br><br>`NO`(默认) |
| presetStopSurplusPrice | string |  | 预设止盈值<br><br>为空则默认不设止盈。 |
| presetStopLossPrice | string |  | 预设止损值<br><br>为空则默认不设止损。 |
| presetStopSurplusExecutePrice | string |  | 预设止盈执行价格 |
| presetStopLossExecutePrice | string |  | 预设止损执行价格 |
| stpMode | string |  | [STP模式（自成交预防）](https://www.bitget.com/zh-CN/support/articles/12560603812732)<br><br> `none`：不设置STP（默认值）<br><br>`cancel_taker`：取消taker单 <br><br>`cancel_maker`：取消maker单 <br><br>`cancel_both`：两者都取消 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.orderId | string |  | 订单id |
| data.clientOid | string |  | 自定义订单id |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695806875837,
  "data": {
    "clientOid": "121211212122",
    "orderId": "121211212122"
  }
}
```

## 一键反手

`POST /api/v2/mix/order/click-backhand`

普通用户限速10次/S 根据uid限频

交易员限速1次/S 根据uid限频

side和tradeSide：

    - 单向持仓时，不可以传tradeSide参数。

    - 双向持仓时，tradeSide必填。

        - 反手当前的多仓,开空仓：side=buy，tradeSide=open。

        - 反手当前的空仓，开多仓：Side =sell，tradeSide=open。

size:代表反手数量。

    - 单向持仓时：忽略该参数，会将整个仓位数量反向开仓。

    - 双向持仓时：

        - 若传入数量小于当前仓位数量：当前仓位数量会按传入数量减持，并按传入数量反向开仓。

          例如当前存在多仓ETHUSDT仓位，持仓数为20，传入数为3，那么当前多仓会减持3个ETH成为17 个，并反向3个数量的空仓。

        - 若传入数量大于或等于当前仓位数量：会直接按当前仓位持仓数反向持仓。

          例如当前存在多仓ETHUSDT仓位，持仓数为10，传入数为11或10，那么当前仓位会反向开10个数量的空仓。



**API Broker返佣标识**:

  需在HTTP Header请求头中添加如下代码块

  > "X-CHANNEL-API-CODE":"your-channel-api-code"

Operation ID: `classicContractTradeReversal`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| symbol | string | 是 | 交易币对 如:ethusdt |
| marginCoin | string | 是 | 保证金币种 |
| productType | string | 是 | 产品类型<br><br>`USDT-FUTURES` U本位合约<br><br>`COIN-FUTURES` 币本位合约<br><br>`USDC-FUTURES` USDC合约 |
| size | string |  | 下单数量。<br><br>1.若不传，则按当前持仓数量反向开仓；<br><br>2.若传，<br><br>单向持仓时：会先市价平仓掉当前仓位后按仓位数量市价买入。<br><br>双向持仓时：若数量小于当前持仓数量，则会先按当前仓位持仓数减去传入数量，再去按传入数量反向市价开仓；若大于当前持仓数量，则只会按当前持仓数反向开仓。<br><br>3.单向持仓时为空，若传则无效。默认当前持仓数量反向持仓。 |
| side | string | 是 | 下单方向<br><br>buy 买<br><br>sell 卖 |
| tradeSide | string |  | 交易方向 <br><br>开平仓(双向持仓)模式下必填。<br><br>双向持仓：<br><br>反手当前的多仓，开空仓：<br><br>Side 填写buy，tradeSide填写open。<br><br>反手当前的空仓，开多仓：<br><br>Side 填写sell，tradeSide填写open。<br><br>单向持仓：单向持仓不填此参数 |
| clientOid | string |  | 自定义订单id |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.orderId | string |  | 订单id |
| data.clientOid | string |  | 自定义订单id |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695806875837,
  "data": {
    "clientOid": "121211212122",
    "orderId": "123"
  }
}
```

## 批量下单

`POST /api/v2/mix/order/batch-place-order`

普通用户:限速5次/秒，根据uid限频

跟单交易员:限速1次/秒，根据uid限频

用于合约批量下单

单向持仓时，必须省略tradeSide参数；

双向持仓时，开多规则为：side=buy,tradeSide=open；开空规则为：side=sell,tradeSide=open；平多规则为：side=buy,tradeSide=close；平空规则为：side=sell,tradeSide=close

**API Broker返佣标识**:

  需在HTTP Header请求头中添加如下代码块

  > "X-CHANNEL-API-CODE":"your-channel-api-code"

Operation ID: `classicContractTradeBatchOrder`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| symbol | string | 是 | 交易对 |
| productType | string | 是 | 产品类型<br><br>`USDT-FUTURES` U本位合约<br><br>`COIN-FUTURES` 币本位合约<br><br>`USDC-FUTURES` USDC合约 |
| marginCoin | string | 是 | 保证金币种 必须大写 |
| marginMode | string | 是 | 仓位模式<br><br>`isolated`：逐仓 <br><br>`crossed`：全仓 |
| orderList | object[] | 是 | 下单集合。最大订单数(列表长度)：50 |
| orderList[].size | string | 是 | 下单数量 |
| orderList[].price | string |  | 下单价格。<br><br>orderType为`limit`时必填 |
| orderList[].side | string | 是 | 下单方向<br><br>`buy`：买<br><br>`sell`：卖 |
| orderList[].tradeSide | string |  | 交易方向<br><br>开平仓**双向持仓**模式下必填，单向持仓时不要填，否则会报错<br><br>`open`: 开<br><br>`close`: 平 |
| orderList[].orderType | string | 是 | 订单类型<br><br>`limit`: 限价单，<br><br>`market`: 市价单 |
| orderList[].force | string |  | 订单有效期<br><br>orderType为`limit`时必填，若省略则默认为`gtc`<br><br>`ioc`: 无法立即成交的部分就撤销<br><br>`fok`: 无法全部立即成交就撤销<br><br>`gtc`: 普通订单, 订单会一直有效，直到被成交或者取消<br><br>`post_only`: 只做maker |
| orderList[].clientOid | string |  | 自定义订单id |
| orderList[].reduceOnly | string |  | 是否只减仓<br><br>`YES`，`NO`<br><br>默认为`NO`<br><br>仅适用于单向持仓模式。 |
| orderList[].presetStopSurplusPrice | string |  | 止盈值<br><br>为空则默认不设止盈。 |
| orderList[].presetStopLossPrice | string |  | 止损值<br><br>为空则默认不设止损。 |
| orderList[].stpMode | string |  | STP模式， default `none` <br><br> `none` 不设置STP <br><br> `cancel_taker` 取消taker单 <br><br>  `cancel_maker` 取消maker单 <br><br>  `cancel_both` 两者都取消 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.successList | object[] |  | 成功单集合 |
| data.successList[].orderId | string |  | 订单id |
| data.successList[].clientOid | string |  | 自定义订单id |
| data.failureList | object[] |  | 失败单集合 |
| data.failureList[].orderId | string |  | 订单id |
| data.failureList[].clientOid | string |  | 自定义订单id |
| data.failureList[].errorMsg | string |  | 失败原因 |
| data.failureList[].errorCode | string |  | 错误码 |
| data.result | boolean |  | 是否全部成功。`true`：全部成功；`false`：至少有一笔失败 |

```json
{
  "code": "00000",
  "data": {
    "successList": [
      {
        "orderId": "121211212122",
        "clientOid": "BITGET#121211212122"
      }
    ],
    "failureList": [],
    "result": true
  },
  "msg": "success",
  "requestTime": 1627293504612
}
```

## 修改订单

`POST /api/v2/mix/order/modify-order`

普通用户10次/S 根据uid限频

修改订单接口，对于处于委托状态的订单进行修改，支持修改止盈止损及其size/price。

修改 size 和 price 会取消之前的订单，异步生成一个**新订单**, 修改预设止盈止损不会取消之前的订单。

修改 size 和 price 时请**一同传入**，不能只传其中一个

根据 orderId 或者 clientOId 修改订单价格，数量和预设止盈止损

只允许修改未成交的限价单(部分成交亦不可修改)，如果修改订单的价格和数量则会取消之前订单重新生成一笔订单，如果 size 和 price 和 预设止盈止损同时传入，则**预设止盈止损不生效**

修改限价单 price 和 size 请务必传入 newClientOid 因为新订单 orderId 无法同步返回, 因此需要根据 newClientOid 来帮助您查询订单信息

修改订单数量 需要满足最小下单数量

如果只修改预设止盈止损，请不要传入 price 和 size ，只传止损或止盈则 另外一个会被取消

Operation ID: `classicContractTradeModifyOrder`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| orderId | string |  | 订单id<br><br>与clientOid两者必传其一，如果两个都传 则以orderId 为主 |
| clientOid | string |  | 自定义订单id <br><br>与orderId两者必传其一，如果两个都传 则以orderId 为主 |
| symbol | string | 是 | 交易币对 如:ethusdt |
| productType | string | 是 | 产品类型<br><br>`USDT-FUTURES` U本位合约<br><br>`COIN-FUTURES` 币本位合约<br><br>`USDC-FUTURES` USDC合约 |
| newClientOid | string | 是 | 改单后的新自定义订单id |
| newSize | string |  | 修改的新交易数量<br><br>为空不改变。 |
| newPrice | string |  | 修改的新下单价格。<br><br>1.已有订单类型为限价单(limit)时，若不传则保持原有价格。<br><br>2.订单类型为市价单（market)时，则不传。 |
| newPresetStopSurplusPrice | string |  | 修改的新止盈值<br><br>1.若为空，原有订单已设止盈则保持原有值<br><br>2.若不为空，原有订单已设止盈则更新止盈值；原有订单未设止盈则新增止盈项。<br><br>若原先已有，传0则代表删除止盈。 |
| newPresetStopLossPrice | string |  | 修改的新止损值<br><br>1.若为空，原有订单已设止损则保持原有值<br><br>2.若不为空，原有订单已设止损则更新止盈值；原有订单未设止损则新增止损项。<br><br>若原先已有，传0则代表删除止损。 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.orderId | string |  | 订单id |
| data.clientOid | string |  | 自定义订单id |

```json
{
  "code": "00000",
  "data": {
    "orderId": "121212121212",
    "clientOid": "BITGET#1627293504612"
  },
  "msg": "success",
  "requestTime": 1627293504612
}
```

## 撤单

`POST /api/v2/mix/order/cancel-order`

限速规则: 10次/1s

Operation ID: `classicContractTradeCancelOrder`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| symbol | string | 是 | 交易对 |
| productType | string | 是 | 产品类型<br><br>`USDT-FUTURES` U本位合约<br><br>`COIN-FUTURES` 币本位合约<br><br>`USDC-FUTURES` USDC合约 |
| marginCoin | string |  | 保证金币种 必须大写 |
| orderId | string |  | 订单id<br><br>orderId和clientOid必需提供一个。<br><br>若都存在则以orderId为准。 |
| clientOid | string |  | 自定义订单id<br><br>orderId和clientOid必需提供一个。<br><br>若都存在则以orderId为准。 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.orderId | string |  | 订单Id |
| data.clientOid | string |  | 客户端自定义Id |

```json
{
  "code": "00000",
  "data": {
    "orderId": "123",
    "clientOid": ""
  },
  "msg": "success",
  "requestTime": 1627293504612
}
```

## 批量撤单

`POST /api/v2/mix/order/batch-cancel-orders`

普通用户10次/S 根据uid限频

撤单接口，可按产品类型、交易对名称进行撤单。

Operation ID: `classicContractTradeBatchCancelOrders`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| orderIdList | object[] |  | 订单id集合。最大长度：50<br><br>若传递，symbol不可为空，且需与symbol/productType对齐 |
| orderIdList[].orderId | string |  | 订单id<br><br>orderId和clientOid必须两者传一个，同传时以orderId为准。 |
| orderIdList[].clientOid | string |  | 自定义订单id<br><br>orderId和clientOid必须两者传一个，同传时以orderId为准。 |
| symbol | string |  | 交易对 如:ethusdt<br><br>当传入`orderIdList`参数时，此参数为必传 |
| productType | string | 是 | 产品类型<br><br>`USDT-FUTURES` U本位合约<br><br>`COIN-FUTURES` 币本位合约<br><br>`USDC-FUTURES` USDC合约 |
| marginCoin | string |  | 保证金币种 必须大写 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.successList | object[] |  | 所撤成功单集合。 |
| data.successList[].orderId | string |  | 订单id |
| data.successList[].clientOid | string |  | 自定义订单id |
| data.failureList | object[] |  | 所撤失败单集合。 |
| data.failureList[].orderId | string |  | 订单id |
| data.failureList[].clientOid | string |  | 自定义订单id |
| data.failureList[].errorMsg | string |  | 失败原因 |
| data.failureList[].errorCode | string |  | 错误码 |

```json
{
  "code": "00000",
  "data": {
    "successList": [
      {
        "orderId": "121211212122",
        "clientOid": "BITGET#121211212122"
      }
    ],
    "failureList": [
      {
        "orderId": "232",
        "clientOid": "321342",
        "errorMsg": "notExistend",
        "errorCode": "43001"
      }
    ]
  },
  "msg": "success",
  "requestTime": 1627293504612
}
```

## 一键市价平仓

`POST /api/v2/mix/order/close-positions`

限速规则: 1次/1s (uid)

市价平仓


**API Broker返佣标识**:

  需在HTTP Header请求头中添加如下代码块

  > "X-CHANNEL-API-CODE":"your-channel-api-code"

Operation ID: `classicContractTradeFlashClosePosition`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| symbol | string |  | 交易对 |
| holdSide | string |  | 持仓方向<br><br>1.买卖（单向持仓）模式下：可不填，若填则忽略。<br><br>2.开平仓模式（双向持仓）下： 若不传，则平全部方向；若传，则平指定方向。<br><br>`long`：多仓 ，`short`：空仓 |
| productType | string | 是 | 产品类型<br><br>`USDT-FUTURES` U本位合约<br><br>`COIN-FUTURES` 币本位合约<br><br>`USDC-FUTURES` USDC合约 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.successList | object[] |  | 平仓成功单集合。 |
| data.successList[].orderId | string |  | 订单id |
| data.successList[].clientOid | string |  | 自定义订单id |
| data.successList[].symbol | string |  | 交易对 |
| data.failureList | object[] |  | 平仓失败单集合<br><br>交割币对交割中、风控处理中等原因可能会导致平仓失败 |
| data.failureList[].orderId | string |  | 订单id |
| data.failureList[].clientOid | string |  | 自定义订单id |
| data.failureList[].symbol | string |  | 交易对 |
| data.failureList[].errorMsg | string |  | 失败原因 |
| data.failureList[].errorCode | string |  | 错误码 |

```json
{
  "code": "00000",
  "data": {
    "successList": [
      {
        "orderId": "123",
        "clientOid": "xxxxx",
        "symbol": "BTCUSDT"
      }
    ],
    "failureList": [
      {
        "orderId": "1234",
        "clientOid": "321",
        "symbol": "BTCUSDT",
        "errorMsg": "xxxxx",
        "errorCode": "xxxx"
      }
    ]
  },
  "msg": "success",
  "requestTime": 1627293504612
}
```

## 获取订单详情

`GET /api/v2/mix/order/detail`

限速规则: 10次/1s (uid)

获取订单详情

Operation ID: `classicContractTradeGetOrderDetails`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | 产品ID 必须大写 |
| productType | query | string | 是 | 产品类型<br><br>`USDT-FUTURES` U本位合约<br><br>`COIN-FUTURES` 币本位合约<br><br>`USDC-FUTURES` USDC合约 |
| orderId | query | string |  | 订单ID<br><br> 'orderId' or 'clientOid' 必需提供一个 |
| clientOid | query | string |  | 自定义订单ID<br><br>'orderId' or 'clientOid' 必需提供一个 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.symbol | string |  | 交易对名称 |
| data.size | string |  | 委托数量 |
| data.orderId | string |  | 订单ID |
| data.clientOid | string |  | 自定义订单id |
| data.baseVolume | string |  | 交易币成交数量 |
| data.priceAvg | string |  | 成交均价 |
| data.fee | string |  | 手续费 |
| data.price | string |  | 委托价格 |
| data.state | string |  | 订单状态<br><br>`live`: 新建订单，orderbook中等待撮合<br><br>`partially_filled`: 部分成交<br><br>`filled`: 全部成交<br><br>`canceled`: 已撤销 |
| data.side | string |  | 开单方向<br><br>`buy`: 买<br><br>`sell`: 卖 |
| data.force | string |  | 订单有效期<br><br>`ioc`: 无法立即成交的部分就撤销<br><br>`fok`: 无法全部立即成交就撤<br><br>`gtc`: 普通订单, 订单会一直有效，直到被成交或者取消<br><br>`post_only`: 只做maker |
| data.totalProfits | string |  | 总盈亏 |
| data.posSide | string |  | 持仓方向<br><br>`long`: 双向持仓多头<br><br>`short`: 双向持仓空头<br><br>`net`: 单向持仓 |
| data.marginCoin | string |  | 保证金币种 |
| data.presetStopSurplusPrice | string |  | 预设止盈值 |
| data.presetStopLossPrice | string |  | 预设止损值 |
| data.quoteVolume | string |  | 计价币成交数量 |
| data.orderType | string |  | 交易类型 <br><br>`limit`: 限价 <br><br>`market`: 市价 |
| data.leverage | string |  | 杠杆倍数 |
| data.marginMode | string |  | 保证金模式<br><br>`isolated`: 逐仓<br><br>`crossed`: 全仓 |
| data.reduceOnly | string |  | 是否只减仓<br><br>`YES`: 是<br><br>`NO`: 否 |
| data.enterPointSource | string |  | 订单来源<br><br>`WEB`: 自Web端创建的订单<br><br>`API`: 自API端创建的订单<br><br>`SYS`: 系统托管订单, 通常由强制平仓逻辑生成<br><br>`ANDROID`: 自Android端创建的订单<br><br>`IOS`: 自IOS端创建的订单 |
| data.tradeSide | string |  | 交易方向<br><br>`open` 开（开平仓模式）<br><br>`close` 平（开平仓模式）<br><br>`reduce_close_long` 双向持仓强制减多<br><br>`reduce_close_short` 双向持仓强制减空<br><br>`offset_close_long` 双向持仓轧差强制减多<br><br>`offset_close_short` 双向持仓轧差强制减空<br><br>`burst_close_long` 双向持仓爆仓平多<br><br>`burst_close_short` 双向持仓爆仓平空<br><br>`delivery_close_long` 双向持仓多头交割<br><br>`delivery_close_short` 双向持仓空头交割<br><br>`dte_sys_adl_close_long` 双向持仓ADL减多仓<br><br>`dte_sys_adl_close_short` 双向持仓ADL减空仓<br><br>`buy_single` 单向持仓买<br><br>`sell_single` 单向持仓卖<br><br>`reduce_buy_single` 单向持仓强制减仓买<br><br>`reduce_sell_single` 单向持仓强制减仓卖<br><br>`burst_buy_single` 单向持仓爆仓买<br><br>`burst_sell_single` 单向持仓爆仓卖<br><br>`delivery_sell_single` 单向持仓交割卖<br><br>`delivery_buy_single` 单向持仓交割买<br><br>`dte_sys_adl_buy_in_single_side_mode` 单向持仓ADL减仓买<br><br>`dte_sys_adl_sell_in_single_side_mode` 单向持仓ADL减仓卖 |
| data.newTradeSide | string |  | 新版交易方向。账户升级后与 `tradeSide` 一同返回，旧订单可能为 `null` |
| data.posMode | string |  | 持仓模式<br><br>one_way_mode 单向持仓<br><br>hedge_mode 双向持仓 |
| data.orderSource | string |  | 订单来源<br><br>normal        正常下单<br><br>market         市价单<br><br>profit_market        市价止盈单<br><br>loss_market        市价止损单<br><br>Trader_delegate        交易员带单下单<br><br>trader_profit        交易员止盈<br><br>trader_loss        交易员止损<br><br>reverse        反手订单<br><br>trader_reverse        交易员带单反手<br><br>profit_limit        止盈限价<br><br>loss_limit        止损限价<br><br>liquidation        爆仓单<br><br>delivery_close_long        多仓交割<br><br>delivery_close_short        空仓交割<br><br>pos_profit_limit        仓位止盈限价<br><br>pos_profit_market        仓位止盈市价<br><br>pos_loss_limit        仓位止损限价<br><br>pos_loss_market        仓位止损市价<br><br>profit_chase        止盈追价委托<br><br>loss_chase        止损追价委托<br><br>follower_delegate        跟单委托<br><br> reduce_offset        减仓扎差委托<br><br>market_risk        最优价风险处理<br><br>plan_limit        限价计划委托<br><br>plan_market        最优价计划委托<br><br>pos_loss_limit        仓位止损限价<br><br>strategy_positive        策略-正向网格<br><br>strategy_reverse        策略-反向网格<br><br>strategy_unlimited        无限策略<br><br>move_limit        限价移动止盈止损<br><br>move_market        最优价移动止盈止损<br><br>tracking_limit        限价追踪委托<br><br>tracking_market        最优价追踪委托<br><br>strategy_dca_positive        DCA策略-正向<br><br>strategy_dca_reverse        DCA策略-反向<br><br>strategy_oco_limit        策略-OCO限价单<br><br>strategy_oco_trigger        策略-OCO触发单<br><br>modify_order_limit        限价修改订单<br><br>strategy_regular_buy        策略-定投策略买<br><br>strategy_grid_middle        策略-中性网格 |
| data.cancelReason | string |  | 取消原因<br><br>`normal_cancel`：普通取消<br><br>  `stp_cancel`：因STP规则取消 |
| data.cTime | string |  | 创建时间, ms |
| data.uTime | string |  | 更新时间, ms |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695823012595,
  "data": {
    "symbol": "ethusdt",
    "size": "2",
    "orderId": "123456",
    "clientOid": "77777",
    "baseVolume": "2",
    "priceAvg": "1900",
    "fee": "",
    "price": "1900",
    "state": "filled",
    "side": "buy",
    "force": "gtc",
    "totalProfits": "2112",
    "posSide": "long",
    "marginCoin": "usdt",
    "presetStopSurplusPrice": "1910",
    "presetStopLossPrice": "1890",
    "quoteVolume": "1900",
    "orderType": "limit",
    "leverage": "20",
    "marginMode": "cross",
    "reduceOnly": "yes",
    "enterPointSource": "api",
    "tradeSide": "",
    "newTradeSide": null,
    "posMode": "one_way_mode",
    "orderSource": "normal",
    "cancelReason": "",
    "cTime": "1627300098776",
    "uTime": "1627300098776"
  }
}
```

## 获取成交明细

`GET /api/v2/mix/order/fills`

普通用户10次/S 根据uid限频

获取合约成交明细记录

您可以在网页端<a href="https://www.bitget.com/zh-CN/asset/export/downOrders">导出</a>历史订单。

Operation ID: `classicContractTradeGetOrderFills`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| orderId | query | string |  | 订单id |
| symbol | query | string |  | 交易对 如:ethusdt |
| productType | query | string | 是 | 产品类型<br><br>`USDT-FUTURES` U本位合约<br><br>`COIN-FUTURES` 币本位合约<br><br>`USDC-FUTURES` USDC合约 |
| idLessThan | query | string |  | 请求此`tradeId`之前（更旧的数据）的分页内容。 |
| startTime | query | string |  | 开始时间 （时间戳毫秒）<br><br>(托管子账户访问时，StartTime 时间不能早于 绑定开始的时间) |
| endTime | query | string |  | 结束时间 （时间戳毫秒） |
| limit | query | string |  | 查询条数 默认100，最大100 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.fillList | object[] |  | 成交明细集合 |
| data.fillList[].tradeId | string |  | 成交id |
| data.fillList[].symbol | string |  | 交易对名称 |
| data.fillList[].orderId | string |  | 订单号 |
| data.fillList[].price | string |  | 成交价格 |
| data.fillList[].baseVolume | string |  | 交易币成交数量 |
| data.fillList[].feeDetail | object[] |  | 手续费 |
| data.fillList[].feeDetail[].deduction | string |  | 是否扣除(抵扣劵） |
| data.fillList[].feeDetail[].feeCoin | string |  | 币种代码 |
| data.fillList[].feeDetail[].totalDeductionFee | string |  | 手续费折扣总额 |
| data.fillList[].feeDetail[].totalFee | string |  | 总计手续费 |
| data.fillList[].side | string |  | 成交类型<br><br>buy 买<br><br>sell 卖 |
| data.fillList[].quoteVolume | string |  | 计价币交易额 |
| data.fillList[].profit | string |  | 利润 |
| data.fillList[].enterPointSource | string |  | 订单来源<br><br>WEB        自Web端创建的订单<br><br>API        自API端创建的订单<br><br>SYS        系统托管订单, 通常由强制平仓逻辑生成<br><br>ANDROID        自Android端创建的订单<br><br>IOS        自IOS端创建的订单 |
| data.fillList[].tradeSide | string |  | 交易方向<br><br>`open` 开（开平仓模式）<br><br>`close` 平（开平仓模式）<br><br>`reduce_close_long` 双向持仓强制减多<br><br>`reduce_close_short` 双向持仓强制减空<br><br>`offset_close_long` 双向持仓轧差强制减多<br><br>`offset_close_short` 双向持仓轧差强制减空<br><br>`burst_close_long` 双向持仓爆仓平多<br><br>`burst_close_short` 双向持仓爆仓平空<br><br>`delivery_close_long` 双向持仓多头交割<br><br>`delivery_close_short` 双向持仓空头交割<br><br>`dte_sys_adl_close_long` 双向持仓ADL减多仓<br><br>`dte_sys_adl_close_short` 双向持仓ADL减空仓<br><br>`buy_single` 单向持仓买<br><br>`sell_single` 单向持仓卖<br><br>`reduce_buy_single` 单向持仓强制减仓买<br><br>`reduce_sell_single` 单向持仓强制减仓卖<br><br>`burst_buy_single` 单向持仓爆仓买<br><br>`burst_sell_single` 单向持仓爆仓卖<br><br>`delivery_sell_single` 单向持仓交割卖<br><br>`delivery_buy_single` 单向持仓交割买<br><br>`dte_sys_adl_buy_in_single_side_mode` 单向持仓ADL减仓买<br><br>`dte_sys_adl_sell_in_single_side_mode` 单向持仓ADL减仓卖 |
| data.fillList[].posMode | string |  | 持仓模式 <br><br>one_way_mode 单向持仓<br><br>hedge_mode 双向持仓 |
| data.fillList[].tradeScope | string |  | Trader tag<br><br>taker: Taker<br><br>maker: Maker |
| data.fillList[].cTime | string |  | 成交时间 |
| data.endId | string |  | 最后的成交id。<br><br>指定idLessThan/idGreaterThan作为范围查询时以此为准。 |

```json
{
  "code": "00000",
  "data": {
    "fillList": [
      {
        "tradeId": "123",
        "symbol": "ethusdt",
        "orderId": "121212",
        "price": "1900",
        "baseVolume": "1",
        "feeDetail": [
          {
            "deduction": "yes",
            "feeCoin": "BGB",
            "totalDeductionFee": "-0.017118519726",
            "totalFee": "-0.017118519726"
          }
        ],
        "side": "buy",
        "quoteVolume": "1902",
        "profit": "102",
        "enterPointSource": "api",
        "tradeSide": "close",
        "posMode": "hedge_mode",
        "tradeScope": "taker",
        "cTime": "1627293509612"
      }
    ],
    "endId": "123"
  },
  "msg": "success",
  "requestTime": 1627293504612
}
```

## 获取历史成交明细

`GET /api/v2/mix/order/fill-history`

普通用户10次/S 根据uid限频

您可以在网页端<a href="https://www.bitget.com/zh-CN/asset/export/downOrders">导出</a>历史订单。

Operation ID: `classicContractTradeGetFillHistory`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| orderId | query | string |  | 订单id |
| symbol | query | string |  | 交易对 如:ethusdt |
| productType | query | string | 是 | 产品类型<br><br>`USDT-FUTURES` U本位合约<br><br>`COIN-FUTURES` 币本位合约<br><br>`USDC-FUTURES` USDC合约<br><br>不支持模拟盘数据查询 |
| startTime | query | string |  | 开始时间戳 <br><br>Unix时间戳的毫秒数格式，如 1597026383085<br><br> （时间跨度最大支持一周，若不传结束时间，则默认结束时间为一周。）<br><br>(托管子账户访问时，StartTime 时间不能早于 绑定开始的时间) |
| endTime | query | string |  | 结束时间戳 <br><br>Unix时间戳的毫秒数格式，如 1597026383085<br><br> （时间跨度最大支持一周，若不传结束时间，则默认结束时间为一周。） |
| idLessThan | query | string |  | 请求此ID之前（更旧的数据）的分页内容，传的值为对应接口的 endId。 |
| limit | query | string |  | 查询条数 最大100，默认100 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.endId | string |  | 上次查询结束订单ID |
| data.fillList | object[] |  | 成交明细集合 |
| data.fillList[].symbol | string |  | 交易对名称 |
| data.fillList[].marginCoin | string |  | 保证金币种 |
| data.fillList[].tradeId | string |  | 成交ID |
| data.fillList[].orderId | string |  | 订单id |
| data.fillList[].price | string |  | 成交价格 |
| data.fillList[].baseVolume | string |  | 交易币成交数量 |
| data.fillList[].feeDetail | object[] |  | 手续费 |
| data.fillList[].feeDetail[].deduction | string |  | 是否扣除(抵扣劵） |
| data.fillList[].feeDetail[].feeCoin | string |  | 币种代码 |
| data.fillList[].feeDetail[].totalDeductionFee | string |  | 手续费折扣总额 |
| data.fillList[].feeDetail[].totalFee | string |  | 总计手续费 |
| data.fillList[].side | string |  | 开单方向<br><br>buy 买，sell 卖 |
| data.fillList[].quoteVolume | string |  | 计价币成交数量 |
| data.fillList[].profit | string |  | 利润 |
| data.fillList[].enterPointSource | string |  | 订单来源<br><br>WEB        自Web端创建的订单<br><br>API        自API端创建的订单<br><br>SYS        系统托管订单, 通常由强制平仓逻辑生成<br><br>ANDROID        自Android端创建的订单<br><br>IOS        自IOS端创建的订单 |
| data.fillList[].tradeSide | string |  | 交易方向<br><br>`open` 开（开平仓模式）<br><br>`close` 平（开平仓模式）<br><br>`reduce_close_long` 双向持仓强制减多<br><br>`reduce_close_short` 双向持仓强制减空<br><br>`offset_close_long` 双向持仓轧差强制减多<br><br>`offset_close_short` 双向持仓轧差强制减空<br><br>`burst_close_long` 双向持仓爆仓平多<br><br>`burst_close_short` 双向持仓爆仓平空<br><br>`delivery_close_long` 双向持仓多头交割<br><br>`delivery_close_short` 双向持仓空头交割<br><br>`dte_sys_adl_close_long` 双向持仓ADL减多仓<br><br>`dte_sys_adl_close_short` 双向持仓ADL减空仓<br><br>`buy_single` 单向持仓买<br><br>`sell_single` 单向持仓卖<br><br>`reduce_buy_single` 单向持仓强制减仓买<br><br>`reduce_sell_single` 单向持仓强制减仓卖<br><br>`burst_buy_single` 单向持仓爆仓买<br><br>`burst_sell_single` 单向持仓爆仓卖<br><br>`delivery_sell_single` 单向持仓交割卖<br><br>`delivery_buy_single` 单向持仓交割买<br><br>`dte_sys_adl_buy_in_single_side_mode` 单向持仓ADL减仓买<br><br>`dte_sys_adl_sell_in_single_side_mode` 单向持仓ADL减仓卖 |
| data.fillList[].posMode | string |  | 持仓模式<br><br>one_way_mode 单向持仓<br><br>hedge_mode 双向持仓 |
| data.fillList[].tradeScope | string |  | 买卖方标识<br><br>taker 吃单方<br><br>maker 挂单方 |
| data.fillList[].cTime | string |  | 创建时间 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1699267238892,
  "data": {
    "fillList": [
      {
        "tradeId": "xxxx",
        "symbol": "ETHUSDT",
        "marginCoin": "USDT",
        "orderId": "xxxx",
        "price": "1801.33",
        "baseVolume": "0.02",
        "feeDetail": [
          {
            "deduction": "no",
            "feeCoin": "USDT",
            "totalDeductionFee": "0",
            "totalFee": "-0.02161596"
          }
        ],
        "side": "sell",
        "quoteVolume": "36.0266",
        "profit": "0.0252",
        "enterPointSource": "ios",
        "tradeSide": "sell_single",
        "posMode": "one_way_mode",
        "tradeScope": "taker",
        "cTime": "1698730804882"
      }
    ],
    "endId": "123456789"
  }
}
```

## 查询当前委托

`GET /api/v2/mix/order/orders-pending`

普通用户10次/S 根据uid限频

可查询当前的所有委托（普通单）委托信息。

Operation ID: `classicContractTradeGetOrdersPending`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| orderId | query | string |  | 订单id<br><br>orderId和clientOid同传时以orderId为准。 |
| clientOid | query | string |  | 自定义订单id<br><br>orderId和clientOid同传时以orderId为准。 |
| symbol | query | string |  | 交易对 如:ethusdt |
| productType | query | string | 是 | 产品类型<br><br>`USDT-FUTURES` U本位合约<br><br>`COIN-FUTURES` 币本位合约<br><br>`USDC-FUTURES` USDC合约 |
| status | query | string |  | 订单状态<br><br>若未指定，将查询所有状态live 等待成交（尚未有任何成交）<br><br>`live`: 未成交；`partially_filled`：部分成交 |
| idLessThan | query | string |  | 请求此ID之前（更旧的数据）的分页内容，传的值为对应接口的 endId。 |
| startTime | query | string |  | 开始时间戳 <br><br>Unix时间戳的毫秒数格式，如 1597026383085 |
| endTime | query | string |  | 结束时间戳 <br><br>Unix时间戳的毫秒数格式，如 1597026383085 |
| limit | query | string |  | 查询条数 最大100，默认100 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.entrustedList | object[] |  | 委托集合 |
| data.entrustedList[].symbol | string |  | 交易对名称 |
| data.entrustedList[].size | string |  | 委托数量 |
| data.entrustedList[].orderId | string |  | 订单id |
| data.entrustedList[].clientOid | string |  | 自定义id |
| data.entrustedList[].baseVolume | string |  | 交易币成交数量 |
| data.entrustedList[].fee | string |  | 手续费 |
| data.entrustedList[].price | string |  | 委托价格 |
| data.entrustedList[].priceAvg | string |  | 平均成交价格<br><br>status为live时为空 |
| data.entrustedList[].status | string |  | 订单状态<br><br>`live`: 等待成交（尚未有任何成交）<br><br>`partially_filled`: 部分成交 |
| data.entrustedList[].side | string |  | 开单方向<br><br>buy 买，sell 卖 |
| data.entrustedList[].force | string |  | 订单有效期<br><br>ioc 无法立即成交的部分就撤销<br><br>fok 无法全部立即成交就撤销<br><br>gtc 普通订单, 订单会一直有效，直到被成交或者取消<br><br>post_only 只做maker |
| data.entrustedList[].totalProfits | string |  | 总盈亏<br><br>status为live时为空。 |
| data.entrustedList[].posSide | string |  | 持仓方向<br><br>long 双向持仓多头<br><br>short 双向持仓空头<br><br>net 单向持仓 |
| data.entrustedList[].marginCoin | string |  | 保证金币种 |
| data.entrustedList[].quoteVolume | string |  | 计价币成交数量 |
| data.entrustedList[].leverage | string |  | 杠杆倍数 |
| data.entrustedList[].marginMode | string |  | 保证金模式<br><br>isolated 逐仓<br><br>crossed 全仓 |
| data.entrustedList[].reduceOnly | string |  | 是否只减仓 |
| data.entrustedList[].enterPointSource | string |  | 订单来源<br><br>WEB        自Web端创建的订单<br><br>API        自API端创建的订单<br><br>SYS        系统托管订单, 通常由强制平仓逻辑生成<br><br>ANDROID        自Android端创建的订单<br><br>IOS        自IOS端创建的订单 |
| data.entrustedList[].tradeSide | string |  | 交易方向<br><br>`open` 开（开平仓模式）<br><br>`close` 平（开平仓模式）<br><br>`reduce_close_long` 双向持仓强制减多<br><br>`reduce_close_short` 双向持仓强制减空<br><br>`offset_close_long` 双向持仓轧差强制减多<br><br>`offset_close_short` 双向持仓轧差强制减空<br><br>`burst_close_long` 双向持仓爆仓平多<br><br>`burst_close_short` 双向持仓爆仓平空<br><br>`delivery_close_long` 双向持仓多头交割<br><br>`delivery_close_short` 双向持仓空头交割<br><br>`dte_sys_adl_close_long` 双向持仓ADL减多仓<br><br>`dte_sys_adl_close_short` 双向持仓ADL减空仓<br><br>`buy_single` 单向持仓买<br><br>`sell_single` 单向持仓卖<br><br>`reduce_buy_single` 单向持仓强制减仓买<br><br>`reduce_sell_single` 单向持仓强制减仓卖<br><br>`burst_buy_single` 单向持仓爆仓买<br><br>`burst_sell_single` 单向持仓爆仓卖<br><br>`delivery_sell_single` 单向持仓交割卖<br><br>`delivery_buy_single` 单向持仓交割买<br><br>`dte_sys_adl_buy_in_single_side_mode` 单向持仓ADL减仓买<br><br>`dte_sys_adl_sell_in_single_side_mode` 单向持仓ADL减仓卖 |
| data.entrustedList[].posMode | string |  | 持仓模式<br><br>one_way_mode 单向持仓<br><br>hedge_mode 双向持仓 |
| data.entrustedList[].orderType | string |  | 订单类型<br><br>limit 限价单<br><br>market  市价单 |
| data.entrustedList[].orderSource | string |  | 订单资源<br><br>normal        正常下单<br><br>market        市价单<br><br>profit_market        市价止盈单<br><br>loss_market        市价止损单<br><br>Trader_delegate        交易员带单下单<br><br>trader_profit        交易员止盈<br><br>trader_loss        交易员止损<br><br>reverse        反手订单<br><br>trader_reverse        交易员带单反手<br><br>profit_limit        止盈限价<br><br>loss_limit        止损限价<br><br>liquidation        爆仓单<br><br>delivery_close_long        多仓交割<br><br>delivery_close_short        空仓交割<br><br>pos_profit_limit        仓位止盈限价<br><br>pos_profit_market        仓位止盈市价<br><br>pos_loss_limit        仓位止损限价<br><br>pos_loss_market        仓位止损市价<br><br>profit_chase        止盈追价委托<br><br>loss_chase        止损追价委托<br><br>follower_delegate        跟单委托<br><br> reduce_offset        减仓扎差委托<br><br>market_risk        最优价风险处理<br><br>plan_limit        限价计划委托<br><br>plan_market        最优价计划委托<br><br>pos_loss_limit        仓位止损限价<br><br>strategy_positive        策略-正向网格<br><br>strategy_reverse        策略-反向网格<br><br>strategy_unlimited        无限策略<br><br>move_limit        限价移动止盈止损<br><br>move_market        最优价移动止盈止损<br><br>tracking_limit        限价追踪委托<br><br>tracking_market        最优价追踪委托<br><br>strategy_dca_positive        DCA策略-正向<br><br>strategy_dca_reverse        DCA策略-反向<br><br>strategy_oco_limit        策略-OCO限价单<br><br>strategy_oco_trigger        策略-OCO触发单<br><br>modify_order_limit        限价修改订单<br><br>strategy_regular_buy        策略-定投策略买<br><br>strategy_grid_middle        策略-中性网格<br><br>off_close        下架平仓 |
| data.entrustedList[].cTime | string |  | 创建时间 |
| data.entrustedList[].uTime | string |  | 最近更新时间 |
| data.entrustedList[].presetStopSurplusPrice | string |  | 预设止盈值 |
| data.entrustedList[].presetStopSurplusExecutePrice | string |  | 预设止盈执行价格 |
| data.entrustedList[].presetStopSurplusTriggerType | string |  | 预设止盈触发类型<br><br>fill_price 成交价格<br><br>mark_price 标记价格<br><br>index_price 指数价格 |
| data.entrustedList[].presetStopLossPrice | string |  | 预设止损值 |
| data.entrustedList[].presetStopLossExecutePrice | string |  | 预设止损执行价格 |
| data.entrustedList[].presetStopLossTriggerType | string |  | 预设止损触发类型<br><br>fill_price 成交价格<br><br>mark_price 标记价格<br><br>index_price 指数价格 |
| data.endId | string |  | 上次查询结束订单ID |

```json
{
  "code": "00000",
  "data": {
    "entrustedList": [
      {
        "symbol": "ethusdt",
        "size": "100",
        "orderId": "123",
        "clientOid": "12321",
        "baseVolume": "12.1",
        "fee": "",
        "price": "1900",
        "priceAvg": "1903",
        "status": "partially_filled",
        "side": "buy",
        "force": "gtc",
        "totalProfits": "0",
        "posSide": "long",
        "marginCoin": "usdt",
        "quoteVolume": "22001.21",
        "leverage": "20",
        "marginMode": "cross",
        "enterPointSource": "api",
        "tradeSide": "open",
        "posMode": "hedge_mode",
        "orderType": "limit",
        "orderSource": "normal",
        "cTime": "1627293504612",
        "uTime": "1627293505612",
        "presetStopSurplusPrice": "2001",
        "presetStopSurplusTriggerType": "mark_price",
        "presetStopSurplusExecutePrice": "2201",
        "presetStopLossPrice": "1800",
        "presetStopLossTriggerType": "mark_price",
        "presetStopLossExecutePrice": "1900"
      }
    ],
    "endId": "123"
  },
  "msg": "success",
  "requestTime": 1627293504612
}
```

## 获取历史委托

`GET /api/v2/mix/order/orders-history`

普通用户10次/S 根据uid限频

获取合约历史委托单(仅支持查询90天内数据，超过90天数据可以在网页端导出）

您可以在网页端<a href="https://www.bitget.com/zh-CN/asset/export/downOrders">导出</a>历史订单。

Operation ID: `classicContractTradeGetOrdersHistory`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| orderId | query | string |  | 订单id<br><br>orderId和clientOid同传时以orderId为准。 |
| clientOid | query | string |  | 自定义订单id<br><br>orderId和clientOid同传时以orderId为准。 |
| symbol | query | string |  | 交易对 如:ETHUSDT |
| productType | query | string | 是 | 产品类型<br><br>`USDT-FUTURES` U本位合约<br><br>`COIN-FUTURES` 币本位合约<br><br>`USDC-FUTURES` USDC合约 |
| idLessThan | query | string |  | 请求此ID之前（更旧的数据）的分页内容，传的值为首次查询返回的`endId` |
| orderSource | query | string |  | 订单资源<br><br>normal        正常下单<br><br>market        市价单<br><br>profit_market        市价止盈单<br><br>loss_market        市价止损单<br><br>Trader_delegate        交易员带单下单<br><br>trader_profit        交易员止盈<br><br>trader_loss        交易员止损<br><br>reverse        反手订单<br><br>trader_reverse        交易员带单反手<br><br>profit_limit        止盈限价<br><br>loss_limit        止损限价<br><br>liquidation        爆仓单<br><br>delivery_close_long        多仓交割<br><br>delivery_close_short        空仓交割<br><br>pos_profit_limit        仓位止盈限价<br><br>pos_profit_market        仓位止盈市价<br><br>pos_loss_limit        仓位止损限价<br><br>pos_loss_market        仓位止损市价 |
| endTime | query | string |  | 结束时间戳 <br><br>Unix时间戳的毫秒数格式，如 1597026383085 |
| startTime | query | string |  | 结束时间戳 <br><br>Unix时间戳的毫秒数格式，如 1597026383085（对于托管子账户，startTime不能早于绑定时间） |
| limit | query | string |  | 查询条数 最大100，默认100 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.endId | string |  | 上次查询结束订单ID，在使用入参`idLessThan`作为范围查询时使用 |
| data.entrustedList | object[] |  | 委托集合 |
| data.entrustedList[].symbol | string |  | 交易对名称 |
| data.entrustedList[].size | string |  | 委托数量 |
| data.entrustedList[].orderId | string |  | 订单id |
| data.entrustedList[].clientOid | string |  | 自定义id |
| data.entrustedList[].baseVolume | string |  | 交易币成交数量 |
| data.entrustedList[].fee | string |  | 手续费 |
| data.entrustedList[].price | string |  | 委托价格 |
| data.entrustedList[].priceAvg | string |  | 平均成交价格 |
| data.entrustedList[].status | string |  | 订单状态<br><br>`filled` 全部成交<br><br>`canceled` 已撤销 |
| data.entrustedList[].side | string |  | 开单方向<br><br>`buy` 买，`sell` 卖 |
| data.entrustedList[].force | string |  | 订单有效期<br><br>(确认是否支持maker）<br><br>ioc 无法立即成交的部分就撤销<br><br>fok 无法全部立即成交就撤销<br><br>gtc 普通订单, 订单会一直有效，直到被成交或者取消<br><br>post_only 只做maker |
| data.entrustedList[].totalProfits | string |  | 总盈亏 |
| data.entrustedList[].posSide | string |  | 持仓方向<br><br>`long` 双向持仓多头<br><br>`short` 双向持仓空头<br><br>`net` 单向持仓 |
| data.entrustedList[].marginCoin | string |  | 保证金币种 |
| data.entrustedList[].quoteVolume | string |  | 计价币成交数量 |
| data.entrustedList[].leverage | string |  | 杠杆倍数 |
| data.entrustedList[].marginMode | string |  | 保证金模式<br><br>`isolated` 逐仓<br><br>`crossed` 全仓 |
| data.entrustedList[].reduceOnly | string |  | 是否只减仓<br><br>`YES`: 是<br><br>`NO`: 否 |
| data.entrustedList[].enterPointSource | string |  | 订单来源<br><br>WEB        自Web端创建的订单<br><br>API        自API端创建的订单<br><br>SYS        系统托管订单, 通常由强制平仓逻辑生成<br><br>ANDROID        自Android端创建的订单<br><br>IOS        自IOS端创建的订单 |
| data.entrustedList[].tradeSide | string |  | 交易方向<br><br>`open` 开（开平仓模式）<br><br>`close` 平（开平仓模式）<br><br>`reduce_close_long` 双向持仓强制减多<br><br>`reduce_close_short` 双向持仓强制减空<br><br>`offset_close_long` 双向持仓轧差强制减多<br><br>`offset_close_short` 双向持仓轧差强制减空<br><br>`burst_close_long` 双向持仓爆仓平多<br><br>`burst_close_short` 双向持仓爆仓平空<br><br>`delivery_close_long` 双向持仓多头交割<br><br>`delivery_close_short` 双向持仓空头交割<br><br>`dte_sys_adl_close_long` 双向持仓ADL减多仓<br><br>`dte_sys_adl_close_short` 双向持仓ADL减空仓<br><br>`buy_single` 单向持仓买<br><br>`sell_single` 单向持仓卖<br><br>`reduce_buy_single` 单向持仓强制减仓买<br><br>`reduce_sell_single` 单向持仓强制减仓卖<br><br>`burst_buy_single` 单向持仓爆仓买<br><br>`burst_sell_single` 单向持仓爆仓卖<br><br>`delivery_sell_single` 单向持仓交割卖<br><br>`delivery_buy_single` 单向持仓交割买<br><br>`dte_sys_adl_buy_in_single_side_mode` 单向持仓ADL减仓买<br><br>`dte_sys_adl_sell_in_single_side_mode` 单向持仓ADL减仓卖 |
| data.entrustedList[].posMode | string |  | 持仓模式<br><br>`one_way_mode` 单向持仓<br><br>`hedge_mode` 双向持仓 |
| data.entrustedList[].orderType | string |  | 订单类型<br><br>limit 限价单<br><br>market  市价单 |
| data.entrustedList[].orderSource | string |  | 订单资源<br><br>normal        正常下单<br><br>market        市价单<br><br>profit_market        市价止盈单<br><br>loss_market        市价止损单<br><br>Trader_delegate        交易员带单下单<br><br>trader_profit        交易员止盈<br><br>trader_loss        交易员止损<br><br>reverse        反手订单<br><br>trader_reverse        交易员带单反手<br><br>profit_limit        止盈限价<br><br>loss_limit        止损限价<br><br>liquidation        爆仓单<br><br>delivery_close_long        多仓交割<br><br>delivery_close_short        空仓交割<br><br>pos_profit_limit        仓位止盈限价<br><br>pos_profit_market        仓位止盈市价<br><br>pos_loss_limit        仓位止损限价<br><br>pos_loss_market        仓位止损市价<br><br>profit_chase        止盈追价委托<br><br>loss_chase        止损追价委托<br><br>follower_delegate        跟单委托<br><br> reduce_offset        减仓扎差委托<br><br>market_risk        最优价风险处理<br><br>plan_limit        限价计划委托<br><br>plan_market        最优价计划委托<br><br>pos_loss_limit        仓位止损限价<br><br>strategy_positive        策略-正向网格<br><br>strategy_reverse        策略-反向网格<br><br>strategy_unlimited        无限策略<br><br>move_limit        限价移动止盈止损<br><br>move_market        最优价移动止盈止损<br><br>tracking_limit        限价追踪委托<br><br>tracking_market        最优价追踪委托<br><br>strategy_dca_positive        DCA策略-正向<br><br>strategy_dca_reverse        DCA策略-反向<br><br>strategy_oco_limit        策略-OCO限价单<br><br>strategy_oco_trigger        策略-OCO触发单<br><br>modify_order_limit        限价修改订单<br><br>strategy_regular_buy        策略-定投策略买<br><br>strategy_grid_middle        策略-中性网格 <br><br>off_close        下架平仓 |
| data.entrustedList[].liqPrice | string |  | 强平价格 |
| data.entrustedList[].cTime | string |  | 创建时间, 时间戳，毫秒 |
| data.entrustedList[].uTime | string |  | 最近更新时间，时间戳，毫秒 |
| data.entrustedList[].presetStopSurplusPrice | string |  | 预设止盈值 |
| data.entrustedList[].presetStopLossPrice | string |  | 预设止损值 |
| data.entrustedList[].posAvg | string |  | 持仓均价 |

```json
{
  "code": "00000",
  "data": {
    "entrustedList": [
      {
        "symbol": "ethusdt",
        "size": "100",
        "orderId": "123",
        "clientOid": "12321",
        "baseVolume": "12.1",
        "fee": "-0.00854",
        "price": "1900",
        "priceAvg": "1903",
        "status": "filled",
        "side": "buy",
        "force": "gtc",
        "totalProfits": "0",
        "posSide": "long",
        "marginCoin": "usdt",
        "quoteVolume": "22001.21",
        "leverage": "20",
        "marginMode": "crossed",
        "reduceOnly": "NO",
        "enterPointSource": "api",
        "tradeSide": "open",
        "posMode": "hedge_mode",
        "posAvg": "",
        "orderType": "limit",
        "orderSource": "normal",
        "liqPrice": "",
        "cTime": "1627293504612",
        "uTime": "1627293505612",
        "presetStopSurplusPrice": "2001",
        "presetStopLossPrice": "1800"
      }
    ],
    "endId": "123"
  },
  "msg": "success",
  "requestTime": 1627293504612
}
```

## 一键全撤

`POST /api/v2/mix/order/cancel-all-orders`

普通用户1次/S 根据uid限频

Operation ID: `classicContractTradeCancelAllOrders`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| productType | string | 是 | 产品类型<br><br>`USDT-FUTURES` U本位合约<br><br>`COIN-FUTURES` 币本位合约<br><br>`USDC-FUTURES` USDC合约 |
| marginCoin | string |  | 保证金币种, 必须大写 |
| requestTime | string |  | 请求时间 Unix毫秒时间戳格式 |
| receiveWindow | string |  | 有效窗口期 单位毫秒 窗口期不超过60s |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.successList | object[] |  | 所撤成功单集合。 |
| data.successList[].orderId | string |  | 订单id |
| data.successList[].clientOid | string |  | 自定义订单id |
| data.failureList | object[] |  | 所撤失败单集合。 |
| data.failureList[].orderId | string |  | 订单id |
| data.failureList[].clientOid | string |  | 自定义订单id |
| data.failureList[].errorMsg | string |  | 失败原因 |
| data.failureList[].errorCode | string |  | 错误码 |

```json
{
  "code": "00000",
  "data": {
    "successList": [
      {
        "orderId": "121211212122",
        "clientOid": "BITGET#121211212122"
      }
    ],
    "failureList": [
      {
        "orderId": "232",
        "clientOid": "321342",
        "errorMsg": "notExistend"
      }
    ]
  },
  "msg": "success",
  "requestTime": 1627293504612
}
```