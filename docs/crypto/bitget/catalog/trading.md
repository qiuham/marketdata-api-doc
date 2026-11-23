---
exchange: bitget
source_url: https://www.bitget.com/docs/catalog/trading
api_type: REST
updated_at: 2026-11-23 19:02:48.240036
---

# Trading

Place, amend, cancel and query UTA orders, positions, strategy / trigger orders, and grid trading.

版本: 1.0.0

## 服务地址

- `https://api.bitget.com`

## 接口列表

- `POST /api/v3/trade/place-order` — Place Order
- `POST /api/v3/trade/modify-order` — Modify Order
- `POST /api/v3/trade/cancel-order` — Cancel Order
- `POST /api/v3/trade/place-batch` — Batch Order
- `POST /api/v3/trade/batch-modify-order` — Batch Modify Orders
- `POST /api/v3/trade/cancel-batch` — Batch Cancel
- `POST /api/v3/trade/cancel-symbol-order` — Cancel All Orders
- `GET /api/v3/trade/order-info` — Get Order Details
- `GET /api/v3/trade/unfilled-orders` — Get Open Orders
- `GET /api/v3/trade/history-orders` — Get Order History
- `GET /api/v3/trade/fills` — Get Fill History
- `POST /api/v3/trade/countdown-cancel-all` — CountDown Cancel All
- `POST /api/v3/trade/place-reality-order` — Place Reality Order
- `POST /api/v3/trade/cancel-reality-order` — Cancel Reality Order
- `POST /api/v3/trade/close-positions` — Close All Positions
- `POST /api/v3/account/move-positions` — Move Positions
- `GET /api/v3/account/move-position-history` — Get Move Position History
- `GET /api/v3/position/current-position` — Get Position Info
- `GET /api/v3/position/history-position` — Get Positions History
- `POST /api/v3/account/max-open-available` — Get Max Open Available
- `GET /api/v3/position/adlRank` — Get Position ADL Rank
- `GET /api/v3/trade/loan-data` — Get Loan Data
- `POST /api/v3/trade/place-strategy-order` — Place Strategy Order
- `POST /api/v3/trade/modify-strategy-order` — Modify Strategy Order
- `POST /api/v3/trade/cancel-strategy-order` — Cancel Strategy Order
- `GET /api/v3/trade/unfilled-strategy-orders` — Unfilled Strategy Orders
- `GET /api/v3/trade/history-strategy-orders` — History Strategy Orders
- `GET /api/v3/trade/strategy-sub-orders` — Get Strategy Sub-orders
- `POST /api/v3/trade/grid/add-investment` — Add Investment Amount
- `GET /api/v3/trade/grid/bot-detail` — Get Grid Bot Detail
- `POST /api/v3/trade/grid/close-bot` — Close Grid Bot
- `POST /api/v3/trade/grid/create-bot` — Create Grid Bot
- `POST /api/v3/trade/grid/create-neutral-bot` — Create Neutral Grid Bot
- `GET /api/v3/trade/grid/list-details` — Get Grid Bot Order Details
- `POST /api/v3/trade/grid/modify-bot` — Modify Grid Bot Parameters
- `POST /api/v3/trade/grid/modify-grid-interval` — Modify Grid Interval and Grid Number
- `POST /api/v3/trade/grid/modify-neutral-bot` — Modify Neutral Grid Bot Parameters
- `POST /api/v3/trade/grid/modify-neutral-grid-interval` — Modify Neutral Grid Interval and Grid Number
- `GET /api/v3/trade/grid/neutral-bot-detail` — Get Neutral Grid Bot Detail
- `GET /api/v3/trade/grid/neutral-list-details` — Get Neutral Grid Bot Order Details
- `POST /api/v3/trade/grid/validate-neutral` — Validate Neutral Grid Parameters
- `POST /api/v3/trade/grid/validate` — Validate Grid Parameters

## Place Order

`POST /api/v3/trade/place-order`

- Rate limit: 10/sec/UID
- Permission: UTA trade (read & write)

> This endpoint now supports Reality stock trading pairs (rToken, e.g., `rAAPLUSDT`). Reality orders are subject to a separate rate limit: 5/sec/UID by default, 30/sec/UID for whitelisted users.

This endpoint allows the order placement across spot, margin, or futures markets with customizable parameters, including price, quantity, and order type, etc.

- **Futures** 

  For one-way mode, reduce-only orders are allowed to place. If a reduce only order already exists and the order quantity equals the position size, or if a new reduce only order exceeds the remaining position size, the previous reduction order will be automatically canceled and replaced. In this case, the returned orderId will be null. <br/>**It is recommended to always provide a `clientOid`.**


- **Margin** <br/>Margin orders will automatically trigger fund borrowing.


- **Order Check**
  - **Futures**:`price` must meet the price multiplier and be a multiple of `priceMultiplier`, and conform to the `pricePrecision` decimal places. `qty` must be greater than or equal to `minOrderAmount` and be a multiple of `sizeMultiplier`.

  - **Spot**:`price` must meet the decimal place requirement. `qty` must be greater than or equal to `minOrderAmount`.


- **Open Position Logic**
  - **Hedge-mode**

    Open long: `side=buy` & `posSide=long`

    Open Short:  `side=sell` & `posSide=short`

    Close long: `side=sell` & `posSide=long`

    Close short: `side=buy` & `posSide=short`


  - **One-way-mode**

    Open long: `side=buy`

    Open short: `side=sell`

    Close long: `side=sell` & `reduceOnly=yes`

    Close short: `side=buy` & `reduceOnly=yes`



- **Order Limit**
  - **Futures**: 400 orders across all USDT, Coin-M, and USDC futures trading pairs.
  - **Spot**: 400 orders across all spot and margin trading pairs.


- **ClientOid Constraints**

  Please ensure your clientOid matches the regular expression `^[\.A-Z\:/a-z0-9_-]{1,32}$`, consisting of 1 to 32 characters, including periods (.), uppercase letters, colons (:), lowercase letters, numbers, underscores (_), and hyphens (-).


- **Request Monitor**

  The API requests will be monitored. If the total number of orders for a single account (including master and sub-accounts) exceeds a set daily limit (UTC 00:00 - UTC 24:00), the platform reserves the right to issue reminders, warnings, and enforce necessary restrictions. By using the API, clients acknowledge and agree to comply with these terms.


- **API Broker rebate identifier**:

  The following code block needs to be added to the HTTP Header of the request.
  > "X-CHANNEL-API-CODE":"your-channel-api-code"

- **COIN-M Futures Symbol Format Description:**

  - **The symbol format for the new COIN-M business line is "XXXUSD_CM". For example, the BTCUSD trading pair in COIN-M futures is formatted as BTCUSD_CM.**
  - The new COIN-M business line does not support modifying orders, ADL, strategy orders, or preset take-profit/stop-loss orders.

Note: If the following errors occur when placing an order, please use `clientOid` to query the order details to confirm the final result of the operation.

  > { "code": "40010", "msg": "Request timed out", "requestTime": 1666268894074, "data": null } <br/> { "code": "40725", "msg": "service return an error", "requestTime": 1666268894071, "data": null } <br/> { "code": "45001", "msg": "Unknown error", "requestTime": 1666268894071, "data": null }

Operation ID: `utaTradeOrderPlaceOrder`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| category | string | 是 | Product type <br/>`SPOT` Spot trading <br/>`MARGIN` Margin trading <br/>`USDT-FUTURES` USDT futures <br/>`COIN-FUTURES` Coin-M futures <br/>`USDC-FUTURES` USDC futures |
| symbol | string | 是 | Symbol name <br/>e.g.,`BTCUSDT` |
| qty | string | 是 | Order quantity <br/>`Spot/Margin`<br/>For market buy orders,the unit is **quote coin**<br/>For limit and market sell orders, the unit is **base coin**<br/>`USDT/USDC-Futures` <br/>The unit is **base coin** <br/>`COIN-Futures` <br/>The unit is **quote coin** |
| price | string |  | Order price <br/>This field is required when the order type is a `limit` order .<br/>This field is not applicable  when the order type is a `market` order. |
| side | string | 是 | Order side<br/>`buy`/`sell` |
| orderType | string | 是 | Order type<br/>`limit`/`market` |
| timeInForce | string |  | Time in force<br/>`ioc` Immediate or cancel. It must be executed immediately, with any unfilled portion canceled. <br/>`fok` Fill or kill. It must be fully executed immediately, or it is canceled entirely. <br/>`gtc` Good 'til canceled. It remains active until it is either filled or manually canceled.<br/>`post_only` Post only. It will only be added to the order book as a maker.<br/>`rpi` Retail Price Improvement order. A non-displayed limit order that provides price improvement for retail order flow. Only available for accounts with RPI market maker permissions.<br/> When orderType is `limit`, it defaults to `gtc`; <br/>when orderType is `market`, the system will execute it as `ioc` |
| posSide | string |  | Position side<br/>`long`/`short`<br/>This field is required in hedge-mode position.<br/>Available only for futures |
| clientOid | string |  | Client order ID |
| reduceOnly | string |  | Reduce-only identifier<br/>`yes`/`no`, default `no`; <br/>`yes` indicates that your position may only be reduced in size upon the activation of this order |
| stpMode | string |  | STP Mode(Self Trade Prevention)<br/>`none`: not setting STP(default)<br/>`cancel_taker`: cancel taker order <br/>`cancel_maker`: cancel maker order <br/>`cancel_both`: cancel both of taker and maker orders |
| tpTriggerBy | string |  | Preset Take-Profit Trigger Type<br/>`market`: Market Price<br/>`mark`: Mark Price<br/>If not specified, the default value is market price<br/>Note: This field is only valid for the contract business lines: USDT-Futures, COIN-Futures, and USDC-Futures. |
| slTriggerBy | string |  | Preset Stop-Loss Trigger Type<br/>`market`: Market Price<br/>`mark`: Mark Price<br/>If not filled in, the default value is market price<br/>Note: This field is only valid for the contract business lines: USDT-Futures, COIN-Futures, and USDC-Futures |
| takeProfit | string |  | Preset Take-Profit Trigger Price |
| stopLoss | string |  | Preset Stop-Loss Trigger Price |
| tpOrderType | string |  | Take-Profit Trigger Strategy Order Type<br/>`limit`: Limit Order<br/>`market`: Market Order<br/>For Reality (rtoken) trading pairs, only `market` is currently supported. |
| slOrderType | string |  | Stop-Loss Trigger Strategy Order Type<br/>`limit`: Limit Order<br/>`market`: Market Order<br/>For Reality (rtoken) trading pairs, only `market` is currently supported. |
| tpLimitPrice | string |  | Take-Profit Strategy Order Execution Price<br/>This field is only valid for limit orders (when `tpOrderType=limit`); it is ignored for market orders. |
| slLimitPrice | string |  | Stop-Loss Strategy Order Execution Price<br/>This field is only valid for limit orders (when `slOrderType=limit`); it is ignored for market orders. |
| marginMode | string |  | Margin mode<br/>`crossed` Cross margin<br/>`isolated` Isolated margin<br/>If not provided, defaults to cross margin<br/>Available only for futures |
| autoBorrow | string |  | Auto borrow switch<br/>`yes` Enable<br/>`no` Disable (default)<br/>Only applicable to spot orders. When enabled, if the obtained coin does not support borrowing while the consumed coin does, and the available balance of the consumed coin is insufficient, the system automatically borrows the consumed coin to make up the shortfall. |
| pxAmendType | string |  | Order price amendment type<br/>`no` When the order price exceeds the price limit range, the system is not allowed to adjust the order price; the order will be rejected (default)<br/>`yes` When the order price exceeds the price limit range, the system is allowed to adjust the price to the best value within the limit range and place the order<br/>Only applicable to limit orders (`orderType`=`limit`) |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.orderId | string |  | Order ID |
| data.clientOid | string |  | Client order ID |

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

## Modify Order

`POST /api/v3/trade/modify-order`

Support modifying orders using either the order ID (orderId) or a custom order ID (clientOid).

Only orders that have not been fully filled can be modified. If an order has been completely filled, it cannot be<br/>  modified through this interface.<br/>After submitting a modification request and before receiving the result, repeated modification requests cannot be<br/>  submitted.
- Rate limit: 10/sec/UID
- Permission: UTA trade

Operation ID: `utaTradeOrderModifyOrder`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| orderId | string |  | Order ID<br/>Either orderId or clientOid must be provided<br/>If both orderId and clientOid are provided simultaneously, orderId takes higher priority |
| clientOid | string |  | Client order ID<br/>Either orderId or clientOid must be provided<br/>If both orderId and clientOid are provided simultaneously, orderId takes higher priority |
| qty | string |  | Order quantity<br/>Base coin<br/>Either qty or price must be provided |
| price | string |  | Order price<br/>Either qty or price must be provided |
| requestId | number |  | Custom request ID used to identify this order modification request<br/>Only supports numbers within 18 digits<br/>Returned when autoCancel=yes and the modify order request is rejected |
| autoCancel | string |  | Will the original order be canceled if the order modification fails<br/>`yes`: Cancel<br/>`no`: Not cancel (default)<br/>When set to `yes`: if the matching engine fails to modify the order, the order is cancelled immediately; after cancellation, the counter will reject any further modification requests for that order (including in-flight and new requests). |
| symbol | string |  | Symbol name<br/>e.g.,`BTCUSDT` |
| category | string |  | Product type<br/>`SPOT` Spot trading<br/>`MARGIN` Margin trading<br/>`USDT-FUTURES` USDT futures<br/>`COIN-FUTURES` Coin-M futures<br/>`USDC-FUTURES` USDC futures |
| tpTriggerBy | string |  | Preset Take-Profit Trigger Type<br/>`market` Market price<br/>`mark` Mark price<br/>Defaults to market price if not specified<br/>Only valid for futures: USDT-FUTURES, COIN-FUTURES, USDC-FUTURES<br/>If not provided or empty, the existing value remains unchanged |
| slTriggerBy | string |  | Preset Stop-Loss Trigger Type<br/>`market` Market price<br/>`mark` Mark price<br/>Defaults to market price if not specified<br/>Only valid for futures: USDT-FUTURES, COIN-FUTURES, USDC-FUTURES<br/>If not provided or empty, the existing value remains unchanged |
| takeProfit | string |  | Preset Take-Profit Trigger Price<br/>If not provided or empty, the existing value remains unchanged<br/>Pass "0" to cancel take-profit |
| stopLoss | string |  | Preset Stop-Loss Trigger Price<br/>If not provided or empty, the existing value remains unchanged<br/>Pass "0" to cancel stop-loss |
| tpOrderType | string |  | Take-Profit Strategy Order Type<br/>`limit` Limit order<br/>`market` Market order |
| slOrderType | string |  | Stop-Loss Strategy Order Type<br/>`limit` Limit order<br/>`market` Market order |
| tpLimitPrice | string |  | Take-Profit Strategy Order Execution Price<br/>Only valid for limit orders (`tpOrderType=limit`); ignored for market orders<br/>If not provided or empty, the existing value remains unchanged |
| slLimitPrice | string |  | Stop-Loss Strategy Order Execution Price<br/>Only valid for limit orders (`slOrderType=limit`); ignored for market orders<br/>If not provided or empty, the existing value remains unchanged |
| pxAmendType | string |  | Order price amendment type<br/>`no` When the order price exceeds the price limit range, the system is not allowed to adjust the order price; the order will be rejected (default)<br/>`yes` When the order price exceeds the price limit range, the system is allowed to adjust the price to the best value within the limit range and place the order<br/>Only applicable to limit orders (`orderType`=`limit`) |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.orderId | string |  | Order ID |
| data.clientOid | string |  | Client order ID |

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

## Cancel Order

`POST /api/v3/trade/cancel-order`

> This endpoint now supports Reality stock trading pairs (rToken, e.g., `rAAPLUSDT`). Reality orders are subject to a separate rate limit: 5/sec/UID by default, 30/sec/UID for whitelisted users.

This endpoint allows you to cancel a single unfilled or partially filled order across spot, margin, and futures markets.
- Rate limit: 10/sec/UID
- Permission: UTA trade (read & write)

Operation ID: `utaTradeOrderCancelOrder`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| orderId | string |  | Order ID<br/>Either `clientOid` or `orderId` must be provided. If both are present or do not match, `orderId` will take priority |
| clientOid | string |  | Client order ID<br/>Either `clientOid` or `orderId` must be provided. If both are present or do not match, `orderId` will take priority |
| category | string |  | Product type <br/>`SPOT` Spot trading <br/>`MARGIN` Margin trading <br/>`USDT-FUTURES` USDT futures <br/>`COIN-FUTURES` Coin-M futures <br/>`USDC-FUTURES` USDC futures |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.orderId | string |  | Order ID |
| data.clientOid | string |  | Client order ID |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695806875837,
  "data": {
    "clientOid": "121211212122",
    "orderId": "111111111111111111"
  }
}
```

## Batch Order

`POST /api/v3/trade/place-batch`

This endpoint allows the order placement across spot, margin, or futures markets with customizable parameters, including<br/>price, quantity, and order type, etc.

**Upcoming Features** (currently not supported)
    - Isolated spot margin will be available soon.
    - Copy trading order placement will be available soon.
    - Take profit and stop loss will be available soon.


**Futures** 

  For one-way mode, reduce-only orders are allowed to place. If a reduce only order already exists and the order<br/>  quantity equals the position size, or if a new reduce only order exceeds the remaining position size, the previous<br/>  reduction order will be automatically canceled and replaced. In this case, the returned orderId will be null. <br/>*<br/>  *It is recommended to always provide a `clientOid`.（currently,`reduce-only` orders are not supported）**


**Margin** <br/>Margin orders will automatically trigger fund borrowing.


**Order Check**
    - **Futures**:`price` must meet the price multiplier and be a multiple of `priceMultiplier`, and conform to the<br/>      `pricePrecision` decimal places. `qty` must be greater than or equal to `minOrderAmount` and be a multiple of<br/>      `sizeMultiplier`.

    - **Spot**:`price` must meet the decimal place requirement. `qty` must be greater than or equal to `minOrderAmount`.


**Open Position Logic**
    - **Hedge-mode**

      Open long: `side=buy` & `posSide=long`

      Open Short:  `side=sell` & `posSide=short`

      Close long: `side=sell` & `posSide=long`

      Close short: `side=buy` & `posSide=short`


    - **One-way-mode**

      Open long: `side=buy`

      Open short: `side=sell`

      Close long: `side=sell` & `reduceOnly=yes`

      Close short: `side=buy` & `reduceOnly=yes`



**Order Limit**
    - **Futures**: 400 orders across all USDT, Coin-M, and USDC futures trading pairs.
    - **Spot**: 400 orders across all spot and margin trading pairs.


**ClientOid Constraints**

  Please ensure your clientOid matches the regular expression `^[\.A-Z\:/a-z0-9_-]{1,32}$`, consisting of 1 to 32<br/>  characters, including periods (.), uppercase letters, colons (:), lowercase letters, numbers, underscores (_), and<br/>  hyphens (-).


**Request Monitor**

  The API requests will be monitored. If the total number of orders for a single account (including master and<br/>  sub-accounts) exceeds a set daily limit (UTC 00:00 - UTC 24:00), the platform reserves the right to issue reminders,<br/>  warnings, and enforce necessary restrictions. By using the API, clients acknowledge and agree to comply with these<br/>  terms.


**API Broker rebate identifier**:

  The following code block needs to be added to the HTTP Header of the request.
  > "X-CHANNEL-API-CODE":"your-channel-api-code"

**Error Sample**

  > { "code":"40762", "msg":"The order size is greater than the max open size", "requestTime":1627293504612 }

  ><br/>  This error code may occur in the following scenarios.
    - Insufficient account balance.

    - The position tier for this symbol has reached its limit. For details on specific tiers, please<br/>      refer <br/>      here .


Note: If the following errors occur when placing an order, please use `clientOid` to query the order details to confirm<br/>the final result of the operation.

> { "code": "40010", "msg": "Request timed out", "requestTime": 1666268894074, "data": null }

> { "code": "40725", "msg": "service return an error", "requestTime": 1666268894071, "data": null }

> { "code": "45001", "msg": "Unknown error", "requestTime": 1666268894071, "data": null }
- Rate limit: 5/sec/UID
- Batch limit: No more than 20 orders per batch
- Permission: UTA trade (read & write)

Operation ID: `utaTradeOrderPlaceBatch`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| category | string | 是 | Product type <br/>`SPOT` Spot trading <br/>`MARGIN` Margin trading <br/>`USDT-FUTURES` USDT futures <br/>`COIN-FUTURES` Coin-M futures <br/>`USDC-FUTURES` USDC futures <br/>All orders must have the same category |
| symbol | string | 是 | Symbol name <br/>e.g.,`BTCUSDT` |
| qty | string | 是 | Order quantity <br/>`Spot/Margin`<br/>For market buy orders,the unit is **quote coin**<br/>For limit and market sell orders, the unit is **base coin**<br/>`USDT/USDC-Futures` <br/>The unit is **base coin** <br/>`COIN-Futures` <br/>The unit is **quote coin** |
| price | string |  | Order price <br/>This field is required when orderType is `limit` |
| side | string | 是 | Order side<br/>`buy`/`sell` |
| orderType | string | 是 | Order type<br/>`limit`/`market` |
| timeInForce | string |  | Time in force<br/>`ioc` Immediate or cancel. It must be executed immediately, with any unfilled portion canceled. <br/>`fok` Fill or kill. It must be fully executed immediately, or it is canceled entirely. <br/>`gtc` Good 'til canceled. It remains active until it is either filled or manually canceled.<br/>`post_only` Post only. It will only be added to the order book as a maker.<br/>`rpi` Retail Price Improvement order. A non-displayed limit order that provides price improvement for retail order flow. Only available for accounts with RPI market maker permissions.<br/>When orderType is `limit`, it defaults to `gtc`; <br/>when orderType is `market`, the system will execute it as `ioc` |
| posSide | string |  | Position side<br/>`long`/`short`<br/>This field is required in hedge-mode position.<br/>Available only for futures |
| clientOid | string |  | Client order ID |
| stpMode | string |  | STP Mode, default `none` <br/>`none` not setting STP <br/>`cancel_taker` cancel taker order <br/>`cancel_maker` cancel maker order <br/>`cancel_both` cancel both of taker and maker orders |
| pxAmendType | string |  | Order price amendment type<br/>`no` When the order price exceeds the price limit range, the system is not allowed to adjust the order price; the order will be rejected (default)<br/>`yes` When the order price exceeds the price limit range, the system is allowed to adjust the price to the best value within the limit range and place the order<br/>Only applicable to limit orders (`orderType`=`limit`) |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.orderId | string |  | Order ID |
| data.clientOid | string |  | Client order ID |
| data.code | string |  | Error code for this order |
| data.msg | string |  | Error message for this order |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695806875837,
  "data": [
    {
      "clientOid": "121211212122",
      "orderId": "121211212122"
    }
  ]
}
```

## Batch Modify Orders

`POST /api/v3/trade/batch-modify-order`

Supports batch order modification via API, allowing simultaneous submission of multiple orders across different<br/>  trading pairs (limited to orders within the same business line).<br/>Each request supports modification of up to 20 orders.<br/>Supports continuous order modification, meaning additional modification requests can be submitted before the previous<br/>  modification request is completed. A maximum of 5 consecutive modification requests for in-progress orders can be<br/>  submitted, and the matching engine will process the modification requests in sequence.<br/>Within the same batch of modification requests, each order can only appear once.<br/>Only fully unfilled orders can have their price and quantity modified.<br/>Partially filled orders can have their price and quantity modified (the modified quantity cannot be less than the<br/>  already filled quantity).<br/>Modification of reduce-only orders is not supported.
- Rate limit: 10/sec/UID
- Permission: UTA trade

Operation ID: `utaTradeOrderBatchModifyOrders`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| orderId | string |  | Order ID<br/>Either orderId or clientOid must be provided<br/>If both orderId and clientOid are provided simultaneously, orderId takes higher priority |
| clientOid | string |  | Client order ID<br/>Either orderId or clientOid must be provided<br/>If both orderId and clientOid are provided simultaneously, orderId takes higher priority |
| qty | string |  | Order quantity<br/>Base coin |
| price | string |  | Order price |
| requestId | number |  | Custom request ID used to identify this order modification request<br/>Only supports numbers within 18 digits<br/>Returned when autoCancel=yes and the modify order request is rejected |
| autoCancel | string |  | Will the original order be canceled if the order modification fails<br/>`yes`: Cancel<br/>`no`: Not cancel (default)<br/>When set to `yes`: if the matching engine fails to modify the order, the order is cancelled immediately; after cancellation, the counter will reject any further modification requests for that order (including in-flight and new requests). |
| symbol | string |  | Symbol name<br/>e.g.,`BTCUSDT` |
| category | string |  | Product type<br/>`SPOT` Spot trading<br/>`MARGIN` Margin trading<br/>`USDT-FUTURES` USDT futures<br/>`COIN-FUTURES` Coin-M futures<br/>`USDC-FUTURES` USDC futures |
| pxAmendType | string |  | Order price amendment type<br/>`no` When the order price exceeds the price limit range, the system is not allowed to adjust the order price; the order will be rejected (default)<br/>`yes` When the order price exceeds the price limit range, the system is allowed to adjust the price to the best value within the limit range and place the order<br/>Only applicable to limit orders (`orderType`=`limit`) |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.orderId | string |  | Order ID |
| data.clientOid | string |  | Client order ID |

```json
{
  "code": "00000",
  "data": [
    {
      "orderId": "1",
      "clientOid": "12312"
    },
    {
      "orderId": "2",
      "clientOid": "2321"
    }
  ],
  "msg": "success",
  "requestTime": 1627293504612
}
```

## Batch Cancel

`POST /api/v3/trade/cancel-batch`

This endpoint allows you to cancel a multiple unfilled or partially filled order across spot, margin, and futures<br/>markets.<br/>When making a batch order cancellation, ensure that each request uses either orderId or clientOid for identification — never both. If both orderId and clientOid are provided in a single request, the clientOid will be ignored.<br/>Batch order cancellation allows partial success.
- Rate limit: 5/sec/UID
- Batch limit: No more than 20 orders per batch
- Permission: UTA trade (read & write)

Operation ID: `utaTradeOrderCancelBatch`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| orderId | string |  | Order ID<br/>Either `clientOid` or `orderId` must be provided. If both are present or do not match, `orderId` will take priority |
| clientOid | string |  | Client order ID<br/>Either `clientOid` or `orderId` must be provided. If both are present or do not match, `orderId` will take priority |
| category | string | 是 | Product type <br/>`SPOT` Spot trading <br/>`MARGIN` Margin trading <br/>`USDT-FUTURES` USDT futures <br/>`COIN-FUTURES` Coin-M futures <br/>`USDC-FUTURES` USDC futures <br/>All orders must have the same category |
| symbol | string | 是 | Symbol name <br/>e.g.,`BTCUSDT` |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.orderId | string |  | Order ID |
| data.clientOid | string |  | Client order ID |
| data.code | string |  | Error code for this order |
| data.msg | string |  | Error message for this order |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695806875837,
  "data": [
    {
      "clientOid": "121211212122",
      "orderId": "111111111111111111"
    },
    {
      "clientOid": "121211212123",
      "orderId": "111111111111111114"
    }
  ]
}
```

## Cancel All Orders

`POST /api/v3/trade/cancel-symbol-order`

Cancel unfilled or partially filled orders by symbol or category.
- Rate limit: 5/sec/UID
- Permission: UTA trade (read & write)

Operation ID: `utaTradeOrderCancelAllOrder`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| category | string | 是 | Product type <br/>`SPOT` Spot trading <br/>`MARGIN` Margin trading <br/>`USDT-FUTURES` USDT futures <br/>`COIN-FUTURES` Coin-M futures <br/>`USDC-FUTURES` USDC futures |
| symbol | string |  | Symbol name <br/>e.g.,`BTCUSDT`<br/>If no symbol is provided, all pending orders in the corresponding category will be closed. |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.list | object[] |  | List |
| data.list[].orderId | string |  | Order ID |
| data.list[].clientOid | string |  | Client order ID |
| data.list[].msg | string |  | Message |
| data.list[].code | string |  | Code |

```json
{
  "code": "00000",
  "data": {
    "list": [
      {
        "orderId": "111111111111111111",
        "clientOid": "111111111111111111",
        "code": "24056",
        "msg": "notExisted"
      }
    ]
  },
  "msg": "success",
  "requestTime": 1627293504612
}
```

## Get Order Details

`GET /api/v3/trade/order-info`

Query order details using either orderId or clientOid.
- Rate limit: 20/sec/UID
- Permission: UTA trade (read)

Operation ID: `utaTradeOrderGetOrderDetails`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| orderId | query | string |  | Order ID<br/>Either `clientOid` or `orderId` must be provided. If both are present or do not match, `orderId` will take priority |
| clientOid | query | string |  | Client order ID<br/>Either `clientOid` or `orderId` must be provided. If both are present or do not match, `orderId` will take priority |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.orderId | string |  | Order ID |
| data.clientOid | string |  | Client order ID |
| data.category | string |  | Product type<br/>`SPOT` Spot trading <br/>`MARGIN` Margin trading <br/>`USDT-FUTURES` USDT futures <br/>`COIN-FUTURES` Coin-M futures <br/>`USDC-FUTURES` USDC futures |
| data.symbol | string |  | Symbol name |
| data.price | string |  | Order price |
| data.qty | string |  | Order quantity<br/>_The unit is base coin_ |
| data.amount | string |  | Order amount<br/>_The unit is quote coin_ |
| data.orderType | string |  | Order type<br/>`limit`/`market` |
| data.cumExecQty | string |  | Cumulative executed quantity<br/>_The unit is base coin_ |
| data.cumExecValue | string |  | Cumulative executed value<br/>_The unit is quote coin_ |
| data.avgPrice | string |  | Average executed price |
| data.orderStatus | string |  | Order status<br/>`live` Order created. <br/>`new` Order matching. <br/>`partially_filled` Partially filled<br/>`filled` Fully filled<br/>`cancelled` Cancelled |
| data.side | string |  | Order side<br/>`buy`/`sell` |
| data.timeInForce | string |  | Time in force<br/>`ioc` Immediate or cancel<br/>`fok`: Fill or kill<br/>`gtc`: Good 'til canceled<br/>`post_only`: Post (Maker) only<br/>`rpi`: Retail Price Improvement order |
| data.posSide | string |  | Position side<br/>`long`/`short` |
| data.tradeSide | string |  | Trade side<br/>`open`/`close` |
| data.holdMode | string |  | Position mode<br/>`one_way_mode`/`hedge_mode` |
| data.marginMode | string |  | Margin mode<br/>`crossed`: Cross margin<br/>`isolated`: Isolated margin<br/>Available only for futures |
| data.stpMode | string |  | STP Mode(Self Trade Prevention)<br/>`none`: not setting STP(default)<br/>`cancel_taker`: cancel taker order <br/>`cancel_maker`: cancel maker order <br/>`cancel_both`: cancel both of taker and maker orders |
| data.takeProfit | string |  | Take-Profit Trigger Price |
| data.stopLoss | string |  | Stop-Loss Trigger Price |
| data.tpTriggerBy | string |  | Take-Profit Trigger Type<br/>`market`: Market Price<br/>`mark`: Mark Price |
| data.slTriggerBy | string |  | Stop-Loss Trigger Type<br/>`market`: Market Price<br/>`mark`: Mark Price |
| data.tpOrderType | string |  | Take-Profit Order Type<br/>`limit`: Limit Order<br/>`market`: Market Order |
| data.slOrderType | string |  | Stop-Loss Order Type<br/>`limit`: Limit Order<br/>`market`: Market Order |
| data.tpLimitPrice | string |  | Take-Profit Limit Order Execution Price |
| data.slLimitPrice | string |  | Stop-Loss Limit Order Execution Price |
| data.reduceOnly | string |  | Reduce-only identifier<br/>`YES`/`NO`<br/>Available only for futures |
| data.feeDetail | object[] |  | Fee detail |
| data.feeDetail[].feeCoin | string |  | Fee coin |
| data.feeDetail[].fee | string |  | Total fee |
| data.delegateType | string |  | Delegate type<br/>`normal` Normal limit<br/>`stop_profit_market` Best-price take-profit<br/>`stop_loss_market` Best-price stop-loss<br/>`stop_profit_chase` Take-profit chase<br/>`stop_loss_chase` Stop-loss chase<br/>`trader_delegate` Copy trade order<br/>`trader_stop_profit` Copy trade take-profit<br/>`trader_stop_loss` Copy trade stop-loss<br/>`follower_delegate` Follow trade order<br/>`reduce_offset_delegate` Position reduction netting<br/>`market` Best-price normal<br/>`market_risk` Best-price risk handling<br/>`plan_limit` Limit conditional order<br/>`plan_market` Market conditional order<br/>`back_contract` Reverse position<br/>`trader_back_contract` Copy trade reverse<br/>`strategy_grid_positive` Strategy - positive grid<br/>`strategy_grid_reverse` Strategy - reverse grid<br/>`strategy_unlimited` Unlimited strategy<br/>`stop_profit_limit` Limit take-profit<br/>`stop_loss_limit` Limit stop-loss<br/>`move_stop_limit` Limit trailing stop<br/>`move_stop_market` Best-price trailing stop<br/>`position_stop_profit_limit` Limit position take-profit<br/>`position_stop_profit_market` Best-price position take-profit<br/>`position_stop_loss_limit` Limit position stop-loss<br/>`position_stop_loss_market` Best-price position stop-loss<br/>`tracking_plan_limit` Limit tracking order<br/>`tracking_plan_market` Best-price tracking order<br/>`delivery_close_long` Long delivery<br/>`delivery_close_short` Short delivery<br/>`liquidation` Liquidation<br/>`strategy_dca_positive` DCA strategy - positive<br/>`strategy_dca_reverse` DCA strategy - reverse<br/>`spot_trace_trader_buy` Spot copy trade buy<br/>`spot_trace_follower_buy` Spot follow trade buy<br/>`spot_trace_trader_sell` Spot copy trade sell<br/>`spot_trace_follower_sell` Spot follow trade sell<br/>`strategy_oco_limit` Strategy - OCO limit<br/>`strategy_oco_trigger` Strategy - OCO trigger<br/>`modify_limit_order` Limit modify<br/>`strategy_regular_buy` Strategy - DCA buy<br/>`strategy_grid_middle` Strategy - neutral grid<br/>`strategy_cta_positive` CTA strategy - positive<br/>`strategy_cta_reverse` CTA strategy - reverse<br/>`strategy_tpsl_limit` Spot TPSL limit<br/>`strategy_tpsl_market` Spot TPSL market<br/>`strategy_contract_ai` Contract AI investment<br/>`strategy_trace_market` Trailing market order<br/>`strategy_trace_limit` Trailing limit order<br/>`strategy_portfolio_buy` Strategy - portfolio buy<br/>`strategy_portfolio_sell` Strategy - portfolio sell<br/>`strategy_tradingview` TradingView signal strategy<br/>`sigan_trace` Signal copy trade<br/>`mmr_stop_loss_market` Best-price MMR stop-loss<br/>`bbo_opponent1` BBO - opponent price 1<br/>`bbo_opponent5` BBO - opponent price 5<br/>`bbo_companion1` BBO - companion price 1<br/>`bbo_companion5` BBO - companion price 5<br/>`bbo_opponent1_profit` BBO - opponent price 1 take-profit<br/>`bbo_opponent5_profit` BBO - opponent price 5 take-profit<br/>`bbo_companion1_profit` BBO - companion price 1 take-profit<br/>`bbo_companion5_profit` BBO - companion price 5 take-profit<br/>`bbo_opponent1_loss` BBO - opponent price 1 stop-loss<br/>`bbo_opponent5_loss` BBO - opponent price 5 stop-loss<br/>`bbo_companion1_loss` BBO - companion price 1 stop-loss<br/>`bbo_companion5_loss` BBO - companion price 5 stop-loss<br/>`spot_bbo_opponent1_tpsl` BBO - opponent price 1 TP/SL<br/>`spot_bbo_opponent5_tpsl` BBO - opponent price 5 TP/SL<br/>`spot_bbo_companion1_tpsl` BBO - companion price 1 TP/SL<br/>`spot_bbo_companion5_tpsl` BBO - companion price 5 TP/SL<br/>`dummy_bbo_profit` BBO - take-profit<br/>`dummy_bbo_loss` BBO - stop-loss<br/>`strategy_pre_tpsl_limit` Spot preset TP/SL limit order<br/>`strategy_pre_tpsl_market` Spot preset TP/SL market order<br/>`future_signal_delegate` Contract signal copy trade limit order<br/>`grant_market` Experience coupon open position<br/>`tg_signal_limit` TG signal order<br/>`tg_signal_tp_market` TG signal order take-profit<br/>`tg_signal_sl_market` TG signal order stop-loss<br/>`strategy_preset_tpsl_limit` Spot preset plan order TP/SL limit order<br/>`strategy_preset_tpsl_market` Spot preset plan order TP/SL market order<br/>`trader_iceberg_limit` Iceberg order<br/>`trader_time_share_market` TWAP order<br/>`strategy_arbitrage_positive` Funding rate arbitrage strategy - positive<br/>`strategy_arbitrage_reverse` Funding rate arbitrage strategy - reverse<br/>`convert_hedging` Flash swap hedging<br/>`off_close` Delisted close position |
| data.cancelReason | string |  | Cancel reason<br/>`normal_cancel` |
| data.execType | string |  | Execution type<br/>`normal` Normal<br/>`offset` Netting of hedged positions<br/>`reduce` Forced reduction<br/>`liquidation` Liquidation<br/>`delivery` Delivery |
| data.createdTime | string |  | Created timestamp<br/>A Unix millisecond timestamp |
| data.updatedTime | string |  | Updated timestamp<br/>A Unix millisecond timestamp |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1730369201783,
  "data": {
    "orderId": "111111111111111111",
    "clientOid": "111111111111111111",
    "category": "SPOT",
    "symbol": "ETHUSDT",
    "orderType": "market",
    "side": "buy",
    "price": "0",
    "qty": "0",
    "amount": "100",
    "cumExecQty": "0.0372",
    "cumExecValue": "99.853356",
    "avgPrice": "2684.23",
    "timeInForce": "gtc",
    "orderStatus": "filled",
    "posSide": "",
    "holdMode": "",
    "tradeSide": "open",
    "reduceOnly": "NO",
    "marginMode": "crossed",
    "stpMode": "none",
    "takeProfit": "",
    "stopLoss": "",
    "tpTriggerBy": "",
    "slTriggerBy": "",
    "tpOrderType": "",
    "slOrderType": "",
    "tpLimitPrice": "",
    "slLimitPrice": "",
    "feeDetail": [
      {
        "feeCoin": "ETH",
        "fee": "0.00000744"
      }
    ],
    "delegateType": "normal",
    "cancelReason": "",
    "execType": "",
    "createdTime": "1730295766596",
    "updatedTime": "1730295766691"
  }
}
```

## Get Open Orders

`GET /api/v3/trade/unfilled-orders`

Query unfilled or partially filled orders. To query closed orders, please use the order history endpoint.

**Order Limit**
    - **Futures**: 400 orders across all USDT, Coin-M, and USDC futures trading pairs.
    - **Spot**: 400 orders across all spot and margin trading pairs.
- Rate limit: 20/sec/UID
- Permission: UTA trade (read)

Operation ID: `utaTradeOrderGetOrderPending`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| category | query | string |  | Product type<br/>`SPOT` Spot trading<br/>`MARGIN` Margin trading<br/>`USDT-FUTURES` USDT futures<br/>`COIN-FUTURES` Coin-M futures<br/>`USDC-FUTURES` USDC futures |
| symbol | query | string |  | Symbol name<br/>e.g.,`BTCUSDT` |
| startTime | query | string |  | Start timestamp<br/>A Unix timestamp in milliseconds e.g.,`1597026383085` |
| endTime | query | string |  | End timestamp<br/>A Unix timestamp in milliseconds e.g.,`1597026383085` |
| limit | query | string |  | Limit per page<br/>Default:`100`. Maximum:`100` |
| cursor | query | string |  | Cursor<br/>Pagination is implemented by omitting the cursor in the first query and applying the cursor from the previous query for subsequent pages |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.list | object[] |  | Order list |
| data.list[].orderId | string |  | Order ID |
| data.list[].clientOid | string |  | Client order ID |
| data.list[].category | string |  | Business Line<br/>`SPOT`: Spot trading<br/>`MARGIN`: Margin trading<br/>`USDT-FUTURES`: USDT futures<br/>`COIN-FUTURES`: Coin-M futures <br/>`USDC-FUTURES`: USDC futures |
| data.list[].symbol | string |  | Symbol name<br/>e.g.,`BTCUSDT` |
| data.list[].price | string |  | Order price |
| data.list[].qty | string |  | Order quantity<br/>_The unit is base coin_ |
| data.list[].amount | string |  | Order amount<br/>_The unit is quote coin_<br/>Applicable to Spot and Margin. |
| data.list[].orderType | string |  | Order type<br/>`limit`/`market` |
| data.list[].cumExecQty | string |  | Cumulative executed order quantity<br/>_The unit is base coin_ |
| data.list[].cumExecValue | string |  | Cumulative executed order value<br/>_The unit is quote coin_ |
| data.list[].avgPrice | string |  | Average price |
| data.list[].orderStatus | string |  | Order status<br/>`live` Order created. <br/>`new` Order matching. <br/>`partially_filled` Partially filled |
| data.list[].side | string |  | Order side<br/>`buy`/`sell` |
| data.list[].timeInForce | string |  | Time in force<br/>`ioc` Immediate or cancel. It must be executed immediately, with any unfilled portion canceled. <br/>`fok` Fill or kill. It must be fully executed immediately, or it is canceled entirely. <br/>`gtc` Good 'til canceled. It remains active until it is either filled or manually canceled.<br/>`post_only` Post only. It will only be added to the order book as a maker.<br/>`rpi` Retail Price Improvement order |
| data.list[].posSide | string |  | Position side<br/>`long`/`short` |
| data.list[].holdMode | string |  | Holding mode<br/>`one_way_mode`/`hedge_mode` |
| data.list[].delegateType | string |  | Delegate type<br/>`normal`: Limit Order<br/>`stop_profit_market`: Take Profit Market<br/>`stop_loss_market`: Stop Loss Market<br/>`stop_profit_chase`: Take Profit Chase Order<br/>`stop_loss_chase`: Stop Loss Chase Order<br/>`trader_delegate`: Lead Trader Order<br/>`trader_stop_profit`: Lead Trader Take Profit<br/>`trader_stop_loss`: Lead Trader Stop Loss<br/>`follower_delegate`: Follower Order<br/>`reduce_offset_delegate`: Reduce-Only Offset Order<br/>`market`: Market Order<br/>`market_risk`: Market Order (Risk Handling)<br/>`plan_limit`: Limit Conditional Order<br/>`plan_market`: Market Conditional Order<br/>`back_contract`: Reverse Position<br/>`trader_back_contract`: Lead Trader Reverse Position<br/>`strategy_grid_positive`: Strategy - Long Grid<br/>`strategy_grid_reverse`: Strategy - Short Grid<br/>`strategy_unlimited`: Unlimited Strategy<br/>`stop_profit_limit`: Take Profit Limit<br/>`stop_loss_limit`: Stop Loss Limit<br/>`move_stop_limit`: Trailing Stop Limit<br/>`move_stop_market`: Trailing Stop Market<br/>`position_stop_profit_limit`: Position Take Profit Limit<br/>`position_stop_profit_market`: Position Take Profit Market<br/>`position_stop_loss_limit`: Position Stop Loss Limit<br/>`position_stop_loss_market`: Position Stop Loss Market<br/>`tracking_plan_limit`: Trailing Limit Order<br/>`tracking_plan_market`: Trailing Market Order<br/>`delivery_close_long`: Long Delivery Close<br/>`delivery_close_short`: Short Delivery Close<br/>`liquidation`: Liquidation<br/>`strategy_dca_positive`: DCA Strategy - Long<br/>`strategy_dca_reverse`: DCA Strategy - Short<br/>`spot_trace_trader_buy`: Spot Lead Trader Buy<br/>`spot_trace_follower_buy`: Spot Follower Buy<br/>`spot_trace_trader_sell`: Spot Lead Trader Sell<br/>`spot_trace_follower_sell`: Spot Follower Sell<br/>`strategy_oco_limit`: Strategy - OCO Limit Order<br/>`strategy_oco_trigger`: Strategy - OCO Trigger Order<br/>`modify_limit_order`: Modify Limit Order<br/>`strategy_regular_buy`: Strategy - Auto-Invest Buy<br/>`strategy_grid_middle`: Strategy - Neutral Grid<br/>`strategy_cta_positive`: CTA Strategy - Long<br/>`strategy_cta_reverse`: CTA Strategy - Short<br/>`strategy_tpsl_limit`: Spot TP/SL Limit Order<br/>`strategy_tpsl_market`: Spot TP/SL Market Order<br/>`strategy_contract_ai`: Futures AI Investment Strategy<br/>`strategy_trace_market`: Trailing Stop Market Order<br/>`strategy_trace_limit`: Trailing Stop Limit Order<br/>`strategy_portfolio_buy`: Strategy - Smart Portfolio Buy<br/>`strategy_portfolio_sell`: Strategy - Smart Portfolio Sell<br/>`strategy_tradingview`: TradingView Signal Strategy<br/>`sigan_trace`: Signal Follower<br/>`mmr_stop_loss_market`: MMR Stop Loss Market<br/>`bbo_opponent1`: BBO - Opponent Best Price 1<br/>`bbo_opponent5`: BBO - Opponent Best Price 5<br/>`bbo_companion1`: BBO - Companion Best Price 1<br/>`bbo_companion5`: BBO - Companion Best Price 5<br/>`bbo_opponent1_profit`: BBO - Opponent 1 Take Profit<br/>`bbo_opponent5_profit`: BBO - Opponent 5 Take Profit<br/>`bbo_companion1_profit`: BBO - Companion 1 Take Profit<br/>`bbo_companion5_profit`: BBO - Companion 5 Take Profit<br/>`bbo_opponent1_loss`: BBO - Opponent 1 Stop Loss<br/>`bbo_opponent5_loss`: BBO - Opponent 5 Stop Loss<br/>`bbo_companion1_loss`: BBO - Companion 1 Stop Loss<br/>`bbo_companion5_loss`: BBO - Companion 5 Stop Loss<br/>`spot_bbo_opponent1_tpsl`: Spot BBO - Opponent 1 TP/SL<br/>`spot_bbo_opponent5_tpsl`: Spot BBO - Opponent 5 TP/SL<br/>`spot_bbo_companion1_tpsl`: Spot BBO - Companion 1 TP/SL<br/>`spot_bbo_companion5_tpsl`: Spot BBO - Companion 5 TP/SL<br/>`dummy_bbo_profit`: BBO - Take Profit<br/>`dummy_bbo_loss`: BBO - Stop Loss<br/>`strategy_pre_tpsl_limit`: Spot Preset TP/SL Limit Order<br/>`strategy_pre_tpsl_market`: Spot Preset TP/SL Market Order<br/>`future_signal_delegate`: Futures Copy Trading Limit Order<br/>`grant_market`: Voucher Opening Order<br/>`tg_signal_limit`: TG Signal Limit Order<br/>`tg_signal_tp_market`: TG Signal Take Profit Market<br/>`tg_signal_sl_market`: TG Signal Stop Loss Market<br/>`strategy_preset_tpsl_limit`: Spot Preset Trigger TP/SL Limit Order<br/>`strategy_preset_tpsl_market`: Spot Preset Trigger TP/SL Market Order<br/>`trader_iceberg_limit`: Iceberg Order<br/>`trader_time_share_market`: TWAP Market Order<br/>`strategy_arbitrage_positive`: Funding Rate Arbitrage Strategy - Long<br/>`strategy_arbitrage_reverse`: Funding Rate Arbitrage Strategy - Short<br/>`liquidation_take_over_long`: Liquidation Takeover Long<br/>`liquidation_take_over_short`: Liquidation Takeover Short<br/>`convert_hedging`: Convert Hedging<br/>`off_close`: Delisting Close |
| data.list[].marginMode | string |  | Margin mode<br/>`crossed`: Cross margin<br/>`isolated`: Isolated margin<br/>Available only for futures |
| data.list[].stpMode | string |  | [STP Mode(Self Trade Prevention)](https://www.bitget.com/support/articles/12560603812732)<br/>`none`: not setting STP(default)<br/>`cancel_taker`: cancel taker order <br/>`cancel_maker`: cancel maker order <br/>`cancel_both`: cancel both of taker and maker orders |
| data.list[].takeProfit | string |  | Take-Profit Trigger Price |
| data.list[].stopLoss | string |  | Stop-Loss Trigger Price |
| data.list[].tpTriggerBy | string |  | Take-Profit Trigger Type<br/>`market`: Market Price<br/>`mark`: Mark Price |
| data.list[].slTriggerBy | string |  | Stop-Loss Trigger Type<br/>`market`: Market Price<br/>`mark`: Mark Price |
| data.list[].tpOrderType | string |  | Take-Profit Order Type<br/>`limit`: Limit Order<br/>`market`: Market Order |
| data.list[].slOrderType | string |  | Stop-Loss Order Type<br/>`limit`: Limit Order<br/>`market`: Market Order |
| data.list[].tpLimitPrice | string |  | Take-Profit Limit Order Execution Price |
| data.list[].slLimitPrice | string |  | Stop-Loss Limit Order Execution Price |
| data.list[].reduceOnly | string |  | Reduce-only identifier<br/>`YES`/`NO` |
| data.list[].feeDetail | object[] |  | Fee detail list |
| data.list[].feeDetail[].feeCoin | string |  | Fee coin |
| data.list[].feeDetail[].fee | string |  | Total fee |
| data.list[].channelCode | string |  | Channel identifier<br/>Used for broker users to reconcile commission rebates |
| data.list[].createdTime | string |  | Order created timestamp<br/>A Unix millisecond timestamp |
| data.list[].updatedTime | string |  | Order update timestamp<br/>A Unix millisecond timestamp |
| data.cursor | string |  | Cursor for the next page (the smallest orderId in current page; pass it to query older orders) |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1730186730084,
  "data": {
    "list": [
      {
        "orderId": "111111111111111111",
        "clientOid": "111111111111111111",
        "category": "USDT-FUTURES",
        "symbol": "BTCUSDT",
        "orderType": "limit",
        "side": "buy",
        "price": "45000",
        "qty": "0.01",
        "amount": "0",
        "cumExecQty": "0",
        "cumExecValue": "0",
        "avgPrice": "0",
        "timeInForce": "gtc",
        "orderStatus": "live",
        "posSide": "long",
        "holdMode": "hedge_mode",
        "delegateType": "normal",
        "reduceOnly": "NO",
        "marginMode": "crossed",
        "stpMode": "none",
        "takeProfit": "",
        "stopLoss": "",
        "tpTriggerBy": "",
        "slTriggerBy": "",
        "tpOrderType": "",
        "slOrderType": "",
        "tpLimitPrice": "",
        "slLimitPrice": "",
        "feeDetail": [
          {
            "feeCoin": null,
            "fee": null
          }
        ],
        "channelCode": "",
        "createdTime": "1730186725663",
        "updatedTime": "1730186725691"
      }
    ],
    "cursor": "1235058132196622336"
  }
}
```

## Get Order History

`GET /api/v3/trade/history-orders`

- [In historical order records placed via API, orders in 'cancelled' status are retained for only 2 hours; orders not placed via API are not affected](https://www.bitget.com/support/articles/12560603823188);

- You can download your <a href="https://www.bitget.com/trade-asset-order/uta-order-history">full UTA order history</a> and <a href="https://www.bitget.com/transac?tab=1">full Classic order history</a> (data available as early as January 1, 2018) via our website

- **Query Range Constraint**<br/> Each individual query can only cover any 30 days within the 90-day window.
- Rate limit: 20/sec/UID
- Permission: UTA trade (read)

Operation ID: `utaTradeOrderGetOrderHistory`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| category | query | string | 是 | Product type <br/>`SPOT` Spot trading <br/>`MARGIN` Margin trading <br/>`USDT-FUTURES` USDT futures <br/>`COIN-FUTURES` Coin-M futures <br/>`USDC-FUTURES` USDC futures |
| symbol | query | string |  | Symbol name <br/>e.g.,`BTCUSDT` |
| startTime | query | string |  | Start timestamp <br/>A Unix timestamp in milliseconds e.g.,`1597026383085`<br/>The access window is 90 days |
| endTime | query | string |  | End timestamp <br/>A Unix timestamp in milliseconds e.g.,`1597026383185`<br/>The time range between `startTime` and `endTime` must not exceed 30 days |
| limit | query | string |  | Limit per page <br/>Default:`100`. Maximum:`100` |
| cursor | query | string |  | Cursor <br/>Pagination is implemented by omitting the cursor in the first query and applying the cursor from the previous query for subsequent pages |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.list | object[] |  | Order list |
| data.list[].orderId | string |  | Order ID |
| data.list[].clientOid | string |  | Client order id |
| data.list[].category | string |  | Product Type <br/>`SPOT` Spot trading <br/>`MARGIN` Margin trading <br/>`USDT-FUTURES` USDT futures <br/>`COIN-FUTURES` Coin-M futures <br/>`USDC-FUTURES` USDC futures |
| data.list[].symbol | string |  | Symbol name <br/>e.g.,`BTCUSDT` |
| data.list[].price | string |  | Order price |
| data.list[].qty | string |  | Order quantity <br/>_The unit is base coin_ |
| data.list[].amount | string |  | Order amount <br/>_The unit is quote coin_ <br/>Applicable to Spot and Margin. |
| data.list[].orderType | string |  | Order type <br/>`limit`/`market` |
| data.list[].cumExecQty | string |  | Cumulative executed order quantity<br/>_The unit is base coin_ |
| data.list[].cumExecValue | string |  | Cumulative executed order value<br/>_The unit is quote coin_ |
| data.list[].avgPrice | string |  | Average price |
| data.list[].orderStatus | string |  | Order status<br/>`live` Order created. <br/>`new` Order matching. <br/>`partially_filled` Partially filled<br/>`filled` Fully filled<br/>`cancelled` Cancelled |
| data.list[].side | string |  | Order side<br/>`buy`/`sell` |
| data.list[].timeInForce | string |  | Time in force<br/>`ioc` Immediate or cancel. It must be executed immediately, with any unfilled portion canceled. <br/>`fok` Fill or kill. It must be fully executed immediately, or it is canceled entirely. <br/>`gtc` Good 'til canceled. It remains active until it is either filled or manually canceled.<br/>`post_only` Post only. It will only be added to the order book as a maker.<br/>`rpi` Retail Price Improvement order |
| data.list[].posSide | string |  | Position side<br/>`long`/`short` |
| data.list[].holdMode | string |  | Holding mode<br/>`one_way_mode`/`hedge_mode` |
| data.list[].delegateType | string |  | Delegate type<br/>`normal`: Limit Order<br/>`stop_profit_market`: Take Profit Market<br/>`stop_loss_market`: Stop Loss Market<br/>`stop_profit_chase`: Take Profit Chase Order<br/>`stop_loss_chase`: Stop Loss Chase Order<br/>`trader_delegate`: Lead Trader Order<br/>`trader_stop_profit`: Lead Trader Take Profit<br/>`trader_stop_loss`: Lead Trader Stop Loss<br/>`follower_delegate`: Follower Order<br/>`reduce_offset_delegate`: Reduce-Only Offset Order<br/>`market`: Market Order<br/>`market_risk`: Market Order (Risk Handling)<br/>`plan_limit`: Limit Conditional Order<br/>`plan_market`: Market Conditional Order<br/>`back_contract`: Reverse Position<br/>`trader_back_contract`: Lead Trader Reverse Position<br/>`strategy_grid_positive`: Strategy - Long Grid<br/>`strategy_grid_reverse`: Strategy - Short Grid<br/>`strategy_unlimited`: Unlimited Strategy<br/>`stop_profit_limit`: Take Profit Limit<br/>`stop_loss_limit`: Stop Loss Limit<br/>`move_stop_limit`: Trailing Stop Limit<br/>`move_stop_market`: Trailing Stop Market<br/>`position_stop_profit_limit`: Position Take Profit Limit<br/>`position_stop_profit_market`: Position Take Profit Market<br/>`position_stop_loss_limit`: Position Stop Loss Limit<br/>`position_stop_loss_market`: Position Stop Loss Market<br/>`tracking_plan_limit`: Trailing Limit Order<br/>`tracking_plan_market`: Trailing Market Order<br/>`delivery_close_long`: Long Delivery Close<br/>`delivery_close_short`: Short Delivery Close<br/>`liquidation`: Liquidation<br/>`strategy_dca_positive`: DCA Strategy - Long<br/>`strategy_dca_reverse`: DCA Strategy - Short<br/>`spot_trace_trader_buy`: Spot Lead Trader Buy<br/>`spot_trace_follower_buy`: Spot Follower Buy<br/>`spot_trace_trader_sell`: Spot Lead Trader Sell<br/>`spot_trace_follower_sell`: Spot Follower Sell<br/>`strategy_oco_limit`: Strategy - OCO Limit Order<br/>`strategy_oco_trigger`: Strategy - OCO Trigger Order<br/>`modify_limit_order`: Modify Limit Order<br/>`strategy_regular_buy`: Strategy - Auto-Invest Buy<br/>`strategy_grid_middle`: Strategy - Neutral Grid<br/>`strategy_cta_positive`: CTA Strategy - Long<br/>`strategy_cta_reverse`: CTA Strategy - Short<br/>`strategy_tpsl_limit`: Spot TP/SL Limit Order<br/>`strategy_tpsl_market`: Spot TP/SL Market Order<br/>`strategy_contract_ai`: Futures AI Investment Strategy<br/>`strategy_trace_market`: Trailing Stop Market Order<br/>`strategy_trace_limit`: Trailing Stop Limit Order<br/>`strategy_portfolio_buy`: Strategy - Smart Portfolio Buy<br/>`strategy_portfolio_sell`: Strategy - Smart Portfolio Sell<br/>`strategy_tradingview`: TradingView Signal Strategy<br/>`sigan_trace`: Signal Follower<br/>`mmr_stop_loss_market`: MMR Stop Loss Market<br/>`bbo_opponent1`: BBO - Opponent Best Price 1<br/>`bbo_opponent5`: BBO - Opponent Best Price 5<br/>`bbo_companion1`: BBO - Companion Best Price 1<br/>`bbo_companion5`: BBO - Companion Best Price 5<br/>`bbo_opponent1_profit`: BBO - Opponent 1 Take Profit<br/>`bbo_opponent5_profit`: BBO - Opponent 5 Take Profit<br/>`bbo_companion1_profit`: BBO - Companion 1 Take Profit<br/>`bbo_companion5_profit`: BBO - Companion 5 Take Profit<br/>`bbo_opponent1_loss`: BBO - Opponent 1 Stop Loss<br/>`bbo_opponent5_loss`: BBO - Opponent 5 Stop Loss<br/>`bbo_companion1_loss`: BBO - Companion 1 Stop Loss<br/>`bbo_companion5_loss`: BBO - Companion 5 Stop Loss<br/>`spot_bbo_opponent1_tpsl`: Spot BBO - Opponent 1 TP/SL<br/>`spot_bbo_opponent5_tpsl`: Spot BBO - Opponent 5 TP/SL<br/>`spot_bbo_companion1_tpsl`: Spot BBO - Companion 1 TP/SL<br/>`spot_bbo_companion5_tpsl`: Spot BBO - Companion 5 TP/SL<br/>`dummy_bbo_profit`: BBO - Take Profit<br/>`dummy_bbo_loss`: BBO - Stop Loss<br/>`strategy_pre_tpsl_limit`: Spot Preset TP/SL Limit Order<br/>`strategy_pre_tpsl_market`: Spot Preset TP/SL Market Order<br/>`future_signal_delegate`: Futures Copy Trading Limit Order<br/>`grant_market`: Voucher Opening Order<br/>`tg_signal_limit`: TG Signal Limit Order<br/>`tg_signal_tp_market`: TG Signal Take Profit Market<br/>`tg_signal_sl_market`: TG Signal Stop Loss Market<br/>`strategy_preset_tpsl_limit`: Spot Preset Trigger TP/SL Limit Order<br/>`strategy_preset_tpsl_market`: Spot Preset Trigger TP/SL Market Order<br/>`trader_iceberg_limit`: Iceberg Order<br/>`trader_time_share_market`: TWAP Market Order<br/>`strategy_arbitrage_positive`: Funding Rate Arbitrage Strategy - Long<br/>`strategy_arbitrage_reverse`: Funding Rate Arbitrage Strategy - Short<br/>`liquidation_take_over_long`: Liquidation Takeover Long<br/>`liquidation_take_over_short`: Liquidation Takeover Short<br/>`convert_hedging`: Convert Hedging<br/>`off_close`: Delisting Close |
| data.list[].reduceOnly | string |  | Reduce-only identifier<br/>`yes`/`no` <br/>`yes` indicates that your position may only be reduced in size upon the activation of this order |
| data.list[].feeDetail | object[] |  | Fee detail |
| data.list[].feeDetail[].feeCoin | string |  | Fee coin |
| data.list[].feeDetail[].fee | string |  | Fee |
| data.list[].cancelReason | string |  | Cancel reason<br/>`normal_cancel` |
| data.list[].execType | string |  | Execution type<br/>`normal` Normal<br/>`offset` Offset<br/>`reduce` Forced reduction <br/>`liquidation` Liquidation<br/>`delivery` Delivery |
| data.list[].marginMode | string |  | Margin mode<br/>`crossed`: Cross margin<br/>`isolated`: Isolated margin<br/>Available only for futures |
| data.list[].stpMode | string |  | [STP Mode(Self Trade Prevention)](https://www.bitget.com/support/articles/12560603812732)<br/>`none`: not setting STP(default)<br/>`cancel_taker`: cancel taker order <br/>`cancel_maker`: cancel maker order <br/>`cancel_both`: cancel both of taker and maker orders |
| data.list[].takeProfit | string |  | Take-Profit Trigger Price |
| data.list[].stopLoss | string |  | Stop-Loss Trigger Price |
| data.list[].tpTriggerBy | string |  | Take-Profit Trigger Type<br/>`market`: Market Price<br/>`mark`: Mark Price |
| data.list[].slTriggerBy | string |  | Stop-Loss Trigger Type<br/>`market`: Market Price<br/>`mark`: Mark Price |
| data.list[].tpOrderType | string |  | Take-Profit Order Type<br/>`limit`: Limit Order<br/>`market`: Market Order |
| data.list[].slOrderType | string |  | Stop-Loss Order Type<br/>`limit`: Limit Order<br/>`market`: Market Order |
| data.list[].tpLimitPrice | string |  | Take-Profit Limit Order Execution Price |
| data.list[].slLimitPrice | string |  | Stop-Loss Limit Order Execution Price |
| data.list[].channelCode | string |  | Channel identifier<br/>Used for broker users to reconcile commission rebates |
| data.list[].createdTime | string |  | Created timestamp<br/>A Unix millisecond timestamp. e.g.,`1736388000` |
| data.list[].updatedTime | string |  | Updated timestamp<br/>A Unix millisecond timestamp. e.g.,`1736388000` |
| data.cursor | string |  | Cursor |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1730186348272,
  "data": {
    "list": [
      {
        "orderId": "111111111111111111",
        "clientOid": "111111111111111111",
        "category": "USDT-FUTURES",
        "symbol": "BTCUSDT",
        "orderType": "limit",
        "side": "sell",
        "price": "49534.4",
        "qty": "0.429",
        "amount": "0",
        "cumExecQty": "0.429",
        "cumExecValue": "21250.2929",
        "avgPrice": "49534.4",
        "timeInForce": "gtc",
        "orderStatus": "filled",
        "posSide": "long",
        "holdMode": "hedge_mode",
        "delegateType": "normal",
        "reduceOnly": "NO",
        "marginMode": "crossed",
        "stpMode": "none",
        "takeProfit": "",
        "stopLoss": "",
        "tpTriggerBy": "",
        "slTriggerBy": "",
        "tpOrderType": "",
        "slOrderType": "",
        "tpLimitPrice": "",
        "slLimitPrice": "",
        "feeDetail": [
          {
            "feeCoin": "USDT",
            "fee": "4.2500586"
          }
        ],
        "cancelReason": "normal_cancel",
        "execType": "liquidation",
        "channelCode": "",
        "createdTime": "1730181468493",
        "updatedTime": "1730181468493"
      }
    ],
    "cursor": "1233319323918499840"
  }
}
```

## Get Fill History

`GET /api/v3/trade/fills`

Query historical fills within the last 90 days.

**Query Range Constraint**<br/> Each individual query can only cover a maximum of 30 days within the 90-day window.
- Rate limit: 20/sec/UID
- Permission: UTA trade (read)

Operation ID: `utaTradeOrderGetOrderFills`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| category | query | string |  | Product type <br/>`SPOT` Spot trading <br/>`MARGIN` Margin trading <br/>`USDT-FUTURES` USDT futures <br/>`COIN-FUTURES` Coin-M futures <br/>`USDC-FUTURES` USDC futures |
| orderId | query | string |  | Order ID |
| startTime | query | string |  | Start timestamp <br/>A Unix timestamp in milliseconds e.g.,`1597026383085`<br/>The access window is 90 days. |
| endTime | query | string |  | End timestamp <br/>A Unix timestamp in milliseconds e.g.,`1597026383185`<br/>The time range between `startTime` and `endTime` must not exceed 30 days. |
| limit | query | string |  | Limit per page <br/>Default:`100`. Maximum:`100` |
| cursor | query | string |  | Cursor <br/>Pagination is implemented by omitting the cursor in the first query and applying the cursor from the previous query for subsequent pages |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.list | object[] |  | Fill list |
| data.list[].execId | string |  | Fill ID |
| data.list[].execLinkId | string |  | Execution correlation ID |
| data.list[].orderId | string |  | Order ID |
| data.list[].clientOid | string |  | Client order ID |
| data.list[].category | string |  | Product type <br/>`SPOT` Spot trading <br/>`MARGIN` Margin trading <br/>`USDT-FUTURES` USDT futures <br/>`COIN-FUTURES` Coin-M futures <br/>`USDC-FUTURES` USDC futures |
| data.list[].symbol | string |  | Symbol name |
| data.list[].orderType | string |  | Order type <br/>`limit`/`market` |
| data.list[].execPrice | string |  | Fill price |
| data.list[].execQty | string |  | Fill quantity<br/>_The unit is base coin_ |
| data.list[].execValue | string |  | Fill value<br/>_The unit is quote coin_ |
| data.list[].feeDetail | object[] |  | Fee detail |
| data.list[].feeDetail[].feeCoin | string |  | Fee coin |
| data.list[].feeDetail[].fee | string |  | Fee |
| data.list[].side | string |  | Fill side<br/>`buy`/`sell` |
| data.list[].tradeScope | string |  | Trade scope<br/>`taker`/`maker` |
| data.list[].tradeSide | string |  | Trade side <br/>`open`/`close`    <br/>Detailed enumerations can be obtained on the Enumeration page. |
| data.list[].createdTime | string |  | Created timestamp<br/>A Unix millisecond timestamp. e.g.,`1736388000` |
| data.list[].updatedTime | string |  | Updated timestamp<br/>A Unix millisecond timestamp. e.g.,`1736388000` |
| data.list[].execPnl | string |  | Closed Position Profit and Loss |
| data.list[].isRPI | string |  | Whether it is an RPI fill<br/>`yes` Yes<br/>`no` No |
| data.cursor | string |  | Cursor |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1750142995229,
  "data": {
    "list": [
      {
        "execId": "131111111111111111",
        "execLinkId": "131111111111111111",
        "orderId": "131111111111111111",
        "clientOid": "131111111111111111",
        "category": "USDT-FUTURES",
        "symbol": "BTCUSDT",
        "orderType": "market",
        "side": "sell",
        "execPrice": "106950.1",
        "execQty": "0.01",
        "execValue": "1069.501",
        "tradeScope": "taker",
        "tradeSide": "open",
        "feeDetail": [
          {
            "feeCoin": "USDT",
            "fee": "0.6417006"
          }
        ],
        "createdTime": "1750141421721",
        "updatedTime": "1750141421728",
        "execPnl": "-0.002",
        "isRPI": "no"
      }
    ],
    "cursor": "131111111111111111"
  }
}
```

## CountDown Cancel All

`POST /api/v3/trade/countdown-cancel-all`

In practical use, clients need to periodically send heartbeat requests to prevent uncontrolled open orders due to<br/>abnormal disconnections or system crashes.

For example, if your expected heartbeat interval is 10 seconds, meaning if no heartbeat request is sent for over 10<br/>seconds, all orders must be canceled:


Under normal circumstances, you can call this interface every 3-5 seconds, set the countdown to 10, and repeatedly<br/>  call it to reset the countdown.

Under abnormal circumstances, if no heartbeat request is sent for over 10 seconds, all orders under the account will<br/>  be automatically canceled; after automatic cancellation, the Deadman Switch mechanism will automatically close.

To manually close the Deadman Switch mechanism, simply set the countdown to 0.

  P.S. This interface only supports canceling orders under UTA accounts, not classic accounts.


Please contact your dedicated Business Development representative to apply for access to this interface.
- Rate limit: 1/sec/UID
- Permission: UTA trade (read & write)

Operation ID: `utaTradeOrderCountDownCancelAll`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| countdown | string | 是 | Reconnect Window<br/>- Unit: seconds<br/>- Positive integer, range: [5, 60]. The minimum countdown is 5 second, and the maximum is 60 seconds.<br/>Filling in 0 cancels the countdown order cancellation function. |

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
  "requestTime": 1728625799912,
  "data": "success"
}
```

## Place Reality Order

`POST /api/v3/trade/place-reality-order`

Place a limit or market order for Reality stock trading pairs.<br/>This endpoint is only available for whitelisted UIDs, please contact BD if needed.
- Rate limit: 10/sec/UID
- Permission: UTA trade (read & write)

Operation ID: `utaTradeOrderPlaceRealityOrder`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| category | string |  | Category<br/>`SPOT` Spot trading<br/>`MARGIN` Margin trading<br/>Default: `SPOT` |
| symbol | string | 是 | Symbol name<br/>e.g., `rAAPLUSDT` <br/>This endpoint only supports Reality stock trading pairs |
| side | string | 是 | Order side<br/>`buy` Buy<br/>`sell` Sell |
| orderType | string | 是 | Order type<br/>`limit` Limit order<br/>`market` Market order |
| qty | string | 是 | Order quantity<br/>For market buy orders, the unit is **quote coin**<br/>For limit and market sell orders, the unit is **base coin** |
| price | string |  | Order price<br/>Required when `orderType=limit` |
| clientOid | string |  | Client order ID |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.orderId | string |  | Order ID |
| data.clientOid | string |  | Client order ID. Returns an empty string if not provided |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695806875837,
  "data": {
    "orderId": "121211212122",
    "clientOid": "myOrder001"
  }
}
```

## Cancel Reality Order

`POST /api/v3/trade/cancel-reality-order`

Cancel an unfilled or partially filled Reality stock order.<br/>This endpoint is only available for whitelisted UIDs, please contact BD if needed.
- Rate limit: 10/sec/UID
- Permission: UTA trade (read & write)

Operation ID: `utaTradeOrderCancelRealityOrder`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| category | string |  | Category<br/>`SPOT` Spot trading<br/>`MARGIN` Margin trading<br/>Default: `SPOT` |
| symbol | string | 是 | Symbol name<br/>e.g., `rAAPLUSDT` |
| orderId | string |  | Order ID<br/>Either `orderId` or `clientOid` must be provided. If both are provided, `orderId` takes priority |
| clientOid | string |  | Client order ID<br/>Either `orderId` or `clientOid` must be provided. If both are provided, `orderId` takes priority |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.orderId | string |  | Order ID |
| data.clientOid | string |  | Client order ID. Returns an empty string if not provided |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695806875837,
  "data": {
    "orderId": "121211212122",
    "clientOid": "myOrder001"
  }
}
```

## Close All Positions

`POST /api/v3/trade/close-positions`

Rate limit: 5/sec/UID

Close positions by position side or category. All positions will be closed at market price, subject to slippage.


**API Broker rebate identifier**:

  The following code block needs to be added to the HTTP Header of the request.

  > "X-CHANNEL-API-CODE":"your-channel-api-code"

- Rate limit: 5/sec/UID

- Permission: UTA trade (read & write)

Operation ID: `utaTradePositionCloseAllPositions`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| category | string | 是 | Product type <br><br> `USDT-FUTURES` USDT futures <br><br> `COIN-FUTURES` Coin-M futures <br><br> `USDC-FUTURES` USDC futures |
| symbol | string |  | Symbol name <br><br>e.g.,`BTCUSDT`<br><br>If no symbol is provided, all positions in the corresponding category will be closed. |
| posSide | string |  | Position side <br><br>`long`/`short`  <br><br> If this field is provided, only the position in the corresponding side will be closed. |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.list | string[] |  | List |
| data.>orderId | string |  | Order ID |
| data.>clientOid | string |  | Client order ID |
| data.>msg | string |  | Message |
| data.>code | string |  | Code |

```json
{
  "code": "00000",
  "data": {
    "list": [
      {
        "orderId": "111111111111111111",
        "clientOid": "111111111111111111",
        "code": "24056",
        "msg": "notExisted"
      }
    ]
  },
  "msg": "success",
  "requestTime": 1627293504612
}
```

## Move Positions

`POST /api/v3/account/move-positions`

Rate limit: 1/sec/UID

Supports position moves between master and sub-accounts, as well as between sub-accounts:

1. Master account → Sub-account

2. Sub-account → Master account

3. Sub-account → Sub-account (must belong to the same master account)

This feature is only available to whitelisted users and can only be called using the master account's API Key. The

  `fromUid` and `toUid` must belong to the same master-sub account system. Currently only supports USDT futures and USDC

  futures. Only cross-margin mode is supported.

The trades generated by position moves will **not** appear in the public market trades and **no trading fees** will be

  charged.

Position moves are **not supported** within 5 minutes before or after each hour (funding fee settlement period).

  Position moves are **not supported** when the source account's MMR ≥ 80%. Before the position move, the system will

  cancel all pending orders for the corresponding symbol in both the source and target accounts. The move price defaults

  to and only supports the **mark price**.

Users can trigger up to **100** position move requests per day per UID (counting from a successful call). Each

  request must be at least **30 seconds** apart. A maximum of **10** positions can be moved per request.

After the position move, the position mode and leverage are based on the target account's original settings.

- Rate limit: 1/sec/UID

- **Business limit: 100 times/day/UID, minimum interval 30 seconds between requests**

- Permission: UTA trade (read & write)

Operation ID: `utaTradePositionMovePositions`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| fromUid | string | 是 | Source account UID <br><br>The account from which positions are transferred <br><br>`fromUid` and `toUid` must belong to the same master-sub account system |
| toUid | string | 是 | Target account UID <br><br>The account to which positions are transferred <br><br>`fromUid` and `toUid` must belong to the same master-sub account system |
| category | string | 是 | Product type <br><br>`USDT-FUTURES` USDT futures <br><br>`COIN-FUTURES` Coin-M futures <br><br>`USDC-FUTURES` USDC futures |
| positionList | string[] | 是 | Position list <br><br>Maximum of 10 positions per request |
| >symbol | string | 是 | Symbol name <br><br>e.g., `BTCUSDT` |
| >side | string | 是 | Order side (from the source account's perspective) <br><br>`buy`/`sell` <br><br>The logic is consistent for both one-way mode and hedge mode. <br><br>When the source holds a long position, pass `side=sell` to reduce the position. <br><br>When the source holds a short position, pass `side=buy` to reduce the position. |
| >qty | string | 是 | Transfer quantity <br><br>Must meet the minimum quantity precision requirement |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.closePosition | string[] |  | Source account position result list |
| data.>orderId | string |  | Target order ID |
| data.>clientOid | string |  | Target client order ID |
| data.>code | string |  | Error code <br><br>Returned when an error occurs during the open position operation |
| data.>msg | string |  | Error message <br><br>Returned when an error occurs during the open position operation |
| data.openPosition | string[] |  | Target account position result list |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695806875837,
  "data": {
    "closePosition": [
      {
        "orderId": "121211212122",
        "clientOid": "131311313133",
        "code": "",
        "msg": ""
      }
    ],
    "openPosition": [
      {
        "orderId": "121211212123",
        "clientOid": "131311313134",
        "code": "",
        "msg": ""
      }
    ]
  }
}
```

## Get Move Position History

`GET /api/v3/account/move-position-history`

Rate limit: 5/sec/UID

Query the history of position moves. Only callable by the master account. You can query the move position history for a

specified source account (master account or sub-account).

**Query Range Constraint**

 If `endTime` is not provided, the default query range is the last 30 days. The maximum

  supported time span is 90 days.

- Rate limit: 5/sec/UID

- Permission: UTA trade (read)

Operation ID: `utaTradePositionGetMovePositionHistory`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| category | query | string | 是 | Product type <br><br>`USDT-FUTURES` USDT futures <br><br>`COIN-FUTURES` Coin-M futures <br><br>`USDC-FUTURES` USDC futures |
| symbol | query | string |  | Symbol name <br><br>e.g., `BTCUSDT` |
| startTime | query | string |  | Start timestamp <br><br>A Unix timestamp in milliseconds e.g., `1597026383085` |
| endTime | query | string |  | End timestamp <br><br>A Unix timestamp in milliseconds e.g., `1597026383185` <br><br>If not provided, defaults to querying the last 30 days. <br><br>Maximum supported time span is 90 days |
| cursor | query | string |  | Cursor <br><br>Pagination is implemented by omitting the cursor in the first query and applying the cursor from the previous query for subsequent pages |
| limit | query | string |  | Limit per page <br><br>Default: `100`. Maximum: `100` |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.list | string[] |  | Move position history list |
| data.>category | string |  | Product type <br><br>`USDT-FUTURES` USDT futures <br><br>`COIN-FUTURES` Coin-M futures <br><br>`USDC-FUTURES` USDC futures |
| data.>fromUid | string |  | Source account UID |
| data.>toUid | string |  | Target account UID |
| data.>orderId | string |  | Order ID |
| data.>openExecId | string |  | Open Position Execution ID |
| data.>closeExecId | string |  | Close Position Execution ID |
| data.>symbol | string |  | Symbol name <br><br>e.g., `BTCUSDT` |
| data.>posSide | string |  | Position side <br><br>`long` Long position <br><br>`short` Short position |
| data.>qty | string |  | Transfer quantity |
| data.>price | string |  | Transfer price |
| data.>status | string |  | Transfer status <br><br>`processing` In progress <br><br>`completed` Completed <br><br>`failed` Failed |
| data.>createdTime | string |  | Created timestamp <br><br>A Unix millisecond timestamp |
| data.>updatedTime | string |  | Updated timestamp <br><br>A Unix millisecond timestamp |
| data.cursor | string |  | Cursor |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1730186348272,
  "data": {
    "list": [
      {
        "category": "USDT-FUTURES",
        "fromUid": "111111111",
        "toUid": "222222222",
        "orderId": "121211212122",
        "openExecId": "343434343434",
        "closeExecId": "343434343435",
        "symbol": "BTCUSDT",
        "posSide": "long",
        "qty": "0.5",
        "price": "61000",
        "status": "completed",
        "createdTime": "1730181468493",
        "updatedTime": "1730181468593"
      }
    ],
    "cursor": "1233319323918499840"
  }
}
```

## Get Position Info

`GET /api/v3/position/current-position`

Rate limit: 20/sec/UID

Query real-time position data by symbol, side, or category.

- Rate limit: 20/sec/UID

- Permission: UTA trade (read)

Operation ID: `utaTradePositionGetPosition`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| category | query | string | 是 | Product type <br><br> `USDT-FUTURES` USDT futures <br><br> `COIN-FUTURES` Coin-M futures <br><br> `USDC-FUTURES` USDC futures |
| symbol | query | string |  | Symbol name<br><br>e.g.`BTCUSDT`<br><br>If no symbol is provided, all positions in the corresponding category will be returned. |
| posSide | query | string |  | Position side <br><br>`long`/`short`<br><br> If this field is provided, only the position in the corresponding side will be returned. |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.list | string[] |  | Position list |
| data.>category | string |  | Product Type <br><br>`USDT-FUTURES` USDT futures <br><br> `COIN-FUTURES` Coin-M futures <br><br> `USDC-FUTURES` USDC futures |
| data.>symbol | string |  | Symbol name |
| data.>marginCoin | string |  | Margin coin |
| data.>posSide | string |  | Position side <br><br>`long`/`short` |
| data.>positionBalance | string |  | Position balance (margin amount)<br><br>_The unit is margin coin_<br><br>In isolated margin mode, reflects the isolated margin amount for this position |
| data.>available | string |  | Available position |
| data.>frozen | string |  | Frozen position |
| data.>total | string |  | Total position (available + frozen) |
| data.>leverage | string |  | Leverage multiple |
| data.>curRealisedPnl | string |  | Current realised profit and loss |
| data.>avgPrice | string |  | Average entry price |
| data.>marginMode | string |  | Margin mode<br><br>`crossed` crossed margin<br><br>`isolated` isolated margin |
| data.>positionStatus | string |  | Position status<br><br>`normal` |
| data.>holdMode | string |  | Holding mode<br><br>`one_way_mode`/`hedge_mode` |
| data.>unrealisedPnl | string |  | Unrealised profit and loss<br><br>In isolated margin mode, reflects the unrealised PnL for this isolated position |
| data.>liquidationPrice | string |  | Estimated liquidation price<br><br>Less than or equal to 0 means liquidation will not occur |
| data.>mmr | string |  | Maintenance margin rate |
| data.>profitRate | string |  | Profit rate |
| data.>markPrice | string |  | Mark price |
| data.>breakEvenPrice | string |  | Break-even price |
| data.>totalFunding | string |  | Total funding<br><br>The accumulated fund fee during the position's duration. If the value is zero, it indicates no fees have been charged |
| data.>openFeeTotal | string |  | Fees deducted on position opening <br><br>Opening fees deducted during the position's lifetime |
| data.>closeFeeTotal | string |  | Fees deducted on position closing <br><br>Closing fees deducted during the position's lifetime |
| data.>cashDividend | string |  | Cash dividend<br><br>The unit is USDT |
| data.>createdTime | string |  | Created timestamp<br><br> A Unix millisecond timestamp |
| data.>updatedTime | string |  | Updated timestamp<br><br> A Unix millisecond timestamp |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1753103840140,
  "data": {
    "list": [
      {
        "category": "USDT-FUTURES",
        "symbol": "BTCUSDT",
        "marginCoin": "USDT",
        "holdMode": "hedge_mode",
        "posSide": "long",
        "marginMode": "crossed",
        "positionBalance": "4701531.84941582",
        "available": "119.2068",
        "frozen": "0",
        "total": "119.2068",
        "leverage": "3",
        "curRealisedPnl": "0",
        "avgPrice": "108674",
        "positionStatus": "normal",
        "unrealisedPnl": "1124573.04243999",
        "liquidationPrice": "43099.9",
        "mmr": "0.015",
        "profitRate": "0.2391929010498401",
        "markPrice": "118097",
        "breakEvenPrice": "109208.6",
        "totalFunding": "-53076.32433032",
        "openFeeTotal": "-2842.86603479",
        "closeFeeTotal": "0",
        "cashDividend": "0",
        "createdTime": "1736378720620",
        "updatedTime": "1753102803148"
      }
    ]
  }
}
```

## Get Positions History

`GET /api/v3/position/history-position`

Rate limit: 20/sec/UID

Query historical positions within the last 90 days. You can download your <a href="https://www.bitget.com/trade-asset-order/uta-order-history-order">full historical positions</a> (data available as early as January 1, 2018) via our website.

- Rate limit: 20/sec/UID

- Permission: UTA trade (read & write)

Operation ID: `utaTradePositionGetPositionHistory`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| category | query | string | 是 | Product type<br><br> `USDT-FUTURES` USDT futures <br><br> `COIN-FUTURES` Coin-M futures <br><br> `USDC-FUTURES` USDC futures |
| symbol | query | string |  | Symbol name<br><br>e.g.,`BTCUSDT` |
| startTime | query | string |  | Start timestamp <br><br>A Unix timestamp in milliseconds e.g.,`1597026383085`<br><br>The access window is 90 days |
| endTime | query | string |  | End timestamp <br><br>A Unix timestamp in milliseconds e.g.,`1597026383185`<br><br> The time range between `startTime` and `endTime` must not exceed 30 days |
| limit | query | string |  | Limit per page<br><br>Default:`100`. Maximum:`100` |
| cursor | query | string |  | Cursor <br><br>Pagination is implemented by omitting the cursor in the first query and applying the cursor from the previous query for subsequent pages |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.list | string[] |  | List |
| data.>positionId | string |  | Position ID |
| data.>category | string |  | Product Type <br><br> `USDT-FUTURES` USDT futures <br><br> `COIN-FUTURES` Coin-M futures <br><br> `USDC-FUTURES` USDC futures |
| data.>symbol | string |  | Symbol name |
| data.>marginCoin | string |  | Margin coin |
| data.>posSide | string |  | Position side<br><br>`long`/`short` |
| data.>openPriceAvg | string |  | Average opening price |
| data.>closePriceAvg | string |  | Average closing price |
| data.>openTotalPos | string |  | Total open position |
| data.>closeTotalPos | string |  | Total closed position |
| data.>marginMode | string |  | Margin mode<br><br>`crossed`/`isolated` |
| data.>holdMode | string |  | Holding mode<br><br>`one_way_mode` /`hedge_mode` |
| data.>cumRealisedPnl | string |  | Cumulative realised profit and loss<br><br>Excluding fees and funding costs |
| data.>netProfit | string |  | Net profit and loss<br><br>Including fees and funding costs |
| data.>totalFunding | string |  | Total funding<br><br>The accumulated fund fee during the position's duration. If the value is zero, it indicates no fees have been charged |
| data.>openFeeTotal | string |  | Fees deducted on position opening <br><br>Opening fees deducted during the position's lifetime |
| data.>closeFeeTotal | string |  | Fees deducted on position closing <br><br>Closing fees deducted during the position's lifetime |
| data.>cashDividend | string |  | Cash dividend<br><br>The unit is USDT |
| data.>createdTime | string |  | Position created timestamp <br><br> A Unix millisecond timestamp |
| data.>updatedTime | string |  | Position updated timestamp <br><br> A Unix millisecond timestamp |
| data.cursor | string |  | Cursor |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1730186957802,
  "data": {
    "list": [
      {
        "positionId": "1111111111111111111",
        "category": "USDT-FUTURES",
        "symbol": "EOSUSDT",
        "marginCoin": "USDT",
        "holdMode": "one_way_mode",
        "posSide": "long",
        "marginMode": "crossed",
        "openPriceAvg": "1960.001",
        "closePriceAvg": "1959.999",
        "openTotalPos": "58",
        "closeTotalPos": "58",
        "cumRealisedPnl": "-0.116",
        "netProfit": "-45.588",
        "totalFunding": "0",
        "openFeeTotal": "-22.7360116",
        "closeFeeTotal": "-22.7359884",
        "cashDividend": "0",
        "createdTime": "1729928018076",
        "updatedTime": "1729929656321"
      }
    ],
    "cursor": "1111111111111111111"
  }
}
```

## Get Max Open Available

`POST /api/v3/account/max-open-available`

Rate limit: 5/sec/UID

Get max open available

- Rate limit: 5/sec/UID

- Permission: UTA trade (read)

Operation ID: `utaTradePositionGetMaxOpenAvailable`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| category | string | 是 | Product type <br><br> `SPOT` Spot trading <br><br> `MARGIN` Margin trading <br><br> `USDT-FUTURES` USDT futures <br><br> `COIN-FUTURES` Coin-M futures <br><br> `USDC-FUTURES` USDC futures |
| symbol | string | 是 | Symbol name <br><br>e.g.,`BTCUSDT` |
| orderType | string | 是 | Order type<br><br>`limit`/`market` |
| side | string | 是 | Transaction direction `buy`/`sell` |
| price | string |  | Order price <br><br>This field is required when orderType is `limit` |
| size | string |  | Order quantity, base coin |
| autoBorrow | string |  | Auto borrow switch<br/>`yes` Enable<br/>`no` Disable (default)<br/>Only applicable to spot orders. When enabled, if the obtained coin does not support borrowing while the consumed coin does, and the available balance of the consumed coin is insufficient, the system automatically borrows the consumed coin to make up the shortfall. |
| marginMode | string |  | Margin mode<br/>`crossed` Cross margin<br/>`isolated` Isolated margin<br/>If not provided, defaults to `crossed`<br/>Under isolated margin mode, the `available` calculation excludes futures trial funds |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.available | string |  | Available <br><br> For spot/margin When `side=buy`, it represents the number of quote coins; when `side=sell`, it represents the number of base coins. <br><br> The futures represents the quantity of the quote coins |
| data.maxOpen | string |  | Maximum openable size <br><br> When `side=buy`, it represents the number of quote coins; when `side=sell`, it represents the number of base coins. <br><br>  Has a value for margin, and for spot when auto borrow (`autoBorrow`) is enabled. |
| data.buyOpenCost | string |  | When buying, the quantity of the quote coin required to open a position is calculated based on the input `size`. <br><br>Only the futures has a value. |
| data.sellOpenCost | string |  | When selling, the quantity of the quote coin required to open a position is calculated based on the input `size`.<br><br>Only the futures has a value. |
| data.maxBuyOpen | string |  | The maximum position that can be opened for purchase. <br><br> Base coin quantity calculated based on account balance.<br><br> Only the futures has a value. |
| data.maxSellOpen | string |  | The maximum position that can be opened for sale. <br><br>  Base coin quantity calculated based on account balance. <br><br>  Only the futures has a value. |
| data.maxBuyAvailable | string |  | Maximum buy available |
| data.maxSellAvailable | string |  | Maximum sell available |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1741851607871,
  "data": {
    "available": "52.008255",
    "maxOpen": "",
    "buyOpenCost": "",
    "sellOpenCost": "",
    "maxBuyOpen": "",
    "maxSellOpen": "",
    "maxBuyAvailable": "",
    "maxSellAvailable": ""
  }
}
```

## Get Position ADL Rank

`GET /api/v3/position/adlRank`

Rate limit: 1/sec/UID

Get Position ADL Rank

- Rate limit: 1/sec/UID

- Permission: UTA trade (read & write)

Operation ID: `utaTradePositionGetPositionADLRank`

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.symbol | string |  | Symbol |
| data.marginCoin | string |  | Margin Coin |
| data.adlRank | string |  | ADL Ranking<br><br>The ranking of your current position in the auto-deleveraging sequence. When an auto-deleveraging event occurs in the market, the closer the value is to 1, the higher the probability that your position will be reduced |
| data.holdSide | string |  | Position Direction <br><br>`long` long position <br><br>`short` short position |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1754035547922,
  "data": [
    {
      "symbol": "MOVEUSDT",
      "marginCoin": "USDT",
      "adlRank": "0.4872",
      "holdSide": "long"
    }
  ]
}
```

## Get Loan Data

`GET /api/v3/trade/loan-data`

Rate limit: 10/sec/UID

Query the current loan data for the unified trading account, including total borrowed amount, next interest payment time, and debt details by coin.

- Rate limit: 10/sec/UID

- Permission: UTA trade (read)

Operation ID: `utaTradePositionGetLoanData`

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.currentLoans | string |  | Total current borrowed amount (USD) |
| data.interestPaymentTime | string |  | Next interest deduction time<br><br>A Unix timestamp in milliseconds |
| data.debtCoinList | object[] |  | Debt coin list |
| data.debtCoinList[].coin | string |  | Debt coin |
| data.debtCoinList[].debt | string |  | Debt amount<br><br>Unit is the debt coin |
| data.debtCoinList[].interestFreeAmount | string |  | Interest-free quota<br><br>Unit is the debt coin |
| data.debtCoinList[].interestRateNextHour | string |  | Next hour borrow rate (annualized)<br><br>In decimal form, e.g., 0.1 means 10% |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1751972326323,
  "data": {
    "currentLoans": "1000.5",
    "interestPaymentTime": "1751976000000",
    "debtCoinList": [
      {
        "coin": "USDT",
        "debt": "1000.5",
        "interestFreeAmount": "200",
        "interestRateNextHour": "0.0001"
      }
    ]
  }
}
```

## Place Strategy Order

`POST /api/v3/trade/place-strategy-order`

Place a strategy order

**API Broker rebate identifier**:

  The following code block needs to be added to the HTTP Header of the request.

  > "X-CHANNEL-API-CODE":"your-channel-api-code"

  This header is now effective for every strategy `type` (`tpsl`/`trigger`/`oco`/`trailing_stop`/`iceberg`/`twap`).

- Speed limit is 10 times/s (UID)

- Permission: UTA trade (read & write)

### Common Request Parameters

These fields apply to every strategy `type`. The parameters specific to each strategy type are listed separately in the sections below.

Operation ID: `utaStrategyPlaceStrategyOrder`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| category | string | 是 | Product type <br><br> `SPOT` Spot <br><br> `MARGIN` Margin <br><br> `USDT-FUTURES` USDT futures <br><br> `COIN-FUTURES` Coin-M futures <br><br> `USDC-FUTURES` USDC futures |
| symbol | string | 是 | Symbol name <br><br>e.g.,`BTCUSDT` |
| type | string |  | Strategy Type<br><br>`tpsl` Take-Profit and Stop-Loss<br><br>`trigger` Trigger Order<br><br>`oco` One-Cancels-the-Other Order<br><br>`trailing_stop` Trailing Stop Order<br><br>`iceberg` Iceberg Order<br><br>`twap` TWAP Order<br><br>Default:`tpsl` |
| side | string |  | Trade side<br><br>`buy`/`sell`<br><br>Hedge-mode:<br><br>Open long: `side=buy` & `posSide=long`<br><br>Open short: `side=sell` & `posSide=short`<br><br>Close long: `side=sell` & `posSide=long`<br><br>Close short: `side=buy` & `posSide=short`<br><br>One-way mode:<br><br>Open long: `side=buy`<br><br>Open short: `side=sell`<br><br>Close long: `side=sell` & `reduceOnly=yes`<br><br>Close short: `side=buy` & `reduceOnly=yes` |
| posSide | string |  | Position side<br><br>`long`/`short` |
| qty | string |  | Order Quantity |
| marginMode | string |  | Margin mode<br/>`crossed` Cross margin<br/>`isolated` Isolated margin<br/>If not provided, defaults to cross margin<br/>Available only for futures |
| clientOid | string |  | Client order ID<br><br>Format: `^[\.A-Z\:/a-z0-9_-]{1,32}$`<br><br>The idempotent validity period is six hours<br><br>Now supported for every strategy `type` (`tpsl`/`trigger`/`oco`/`trailing_stop`/`iceberg`/`twap`). |

```json
{
  "category": "USDT-FUTURES",
  "symbol": "BTCUSDT",
  "posSide": "long",
  "stopLoss": "99000",
  "takeProfit": "100800",
  "clientOid": "121211212122"
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
| data.clientOid | string |  | Client order ID |

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

## Modify Strategy Order

`POST /api/v3/trade/modify-strategy-order`

Modify strategy order

- Speed limit is 10 times/s (UID)

- Permission: UTA trade (read & write)

Operation ID: `utaStrategyModifyStrategyOrder`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| orderId | string | 是 | Order ID<br><br>Either orderId or clientOid must be provided<br><br>If both orderId and clientOid are provided simultaneously, orderId takes higher priority |
| clientOid | string |  | Client order ID <br><br>Either orderId or clientOid must be provided<br><br>If both orderId and clientOid are provided simultaneously, orderId takes higher priority |
| qty | string | 是 | Order Quantity<br><br>Can be modified under partial take-profit/stop-loss mode, and the unit is in the `base coin` |
| tpTriggerBy | string |  | Take-Profit Trigger Type<br><br>`market`: Market Price<br><br>`mark`: Mark Price |
| slTriggerBy | string |  | Stop-Loss Trigger Type<br><br>`market`: Market Price<br><br>`mark`: Mark Price |
| takeProfit | string |  | Take-Profit Trigger Price |
| stopLoss | string |  | Stop-Loss Trigger Price |
| tpOrderType | string |  | Take-Profit Trigger Strategy Order Type<br><br>`limit`: Limit Order<br><br>`market`: Market Order |
| slOrderType | string |  | Stop-Loss Trigger Strategy Order Type<br><br>`limit`: Limit Order<br><br>`market`: Market Order |
| tpLimitPrice | string |  | Take-Profit Strategy Order Execution Price<br><br>This field is only valid for limit orders (when `tpOrderType=limit`); it is ignored for market orders. |
| slLimitPrice | string |  | Stop-Loss Strategy Order Execution Price<br><br>This field is only valid for limit orders (when `slOrderType=limit`); it is ignored for market orders |
| triggerBy | string |  | Trigger order trigger price type<br><br>`market`: Market Price<br><br>`mark`: Mark Price |
| triggerPrice | string |  | Trigger order trigger price<br><br>Only valid for limit orders (when `triggerOrderType=limit`) |
| triggerOrderType | string |  | Trigger order type<br><br>`limit`: Limit Order<br><br>`market`: Market Order |
| triggerOrderPrice | string |  | Trigger order execution price<br><br>Only valid for limit orders (when `triggerOrderType=limit`) |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.orderId | string |  | Order ID |
| data.clientOid | string |  | Client order ID |

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

## Cancel Strategy Order

`POST /api/v3/trade/cancel-strategy-order`

Cancel strategy order

For `iceberg`/`twap` orders, cancelling the parent order also cancels all of its unfilled child orders. For `oco` orders, cancelling either leg of the pair also cancels the other leg.

- Speed limit is 10 times/s (UID)

- Permission: UTA trade (read & write)

Operation ID: `utaStrategyCancelStrategyOrder`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| orderId | string | 是 | Order ID<br><br>Either orderId or clientOid must be provided<br><br>If both orderId and clientOid are provided simultaneously, orderId takes higher priority |
| clientOid | string |  | Client order ID <br><br>Either orderId or clientOid must be provided<br><br>If both orderId and clientOid are provided simultaneously, orderId takes higher priority |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.code | string |  | Code |
| data.msg | string |  | Msg |
| data.requestTime | string |  | Timestamp |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695806875837,
  "data": null
}
```

## Unfilled Strategy Orders

`GET /api/v3/trade/unfilled-strategy-orders`

Get unfilled strategy orders

- Speed limit is 20 times/s (UID)

- Permission: UTA trade (read)

Operation ID: `utaStrategyGetUnfilledStrategyOrders`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| category | query | string | 是 | Product type <br><br> `SPOT` Spot <br><br> `MARGIN` Margin <br><br> `USDT-FUTURES` USDT futures <br><br> `COIN-FUTURES` Coin-M futures <br><br> `USDC-FUTURES` USDC futures |
| type | query | string |  | Strategy Type<br><br>`tpsl` Take-Profit and Stop-Loss<br><br>`trigger` Trigger Order<br><br>`oco` OCO<br><br>`trailing_stop` Trailing Stop<br><br>`iceberg` Iceberg<br><br>`twap` TWAP |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  | Order list |
| data[].orderId | string |  | Order ID |
| data[].clientOid | string |  | Client order ID |
| data[].category | string |  | Product type <br><br> `USDT-FUTURES` USDT futures <br><br> `COIN-FUTURES` Coin-M futures <br><br> `USDC-FUTURES` USDC futures |
| data[].symbol | string |  | Symbol name <br><br>e.g.,`BTCUSDT` |
| data[].qty | string |  | Order Quantity |
| data[].side | string |  | Order side<br><br>`buy`/`sell` |
| data[].posSide | string |  | Position side<br><br>`long`/`short` |
| data[].status | string |  | Strategy order status<br><br>`pending` Waiting to be executed<br><br>`success` Executed<br><br>`failed` Execution failed<br><br>`cancelled` Cancelled<br><br>`submitting` Submitting |
| data[].marginMode | string |  | Margin mode<br/>`crossed` Cross margin<br/>`isolated` Isolated margin<br/>If not provided, defaults to cross margin<br/>Available only for futures |
| data[].type | string |  | Strategy Type<br><br>`tpsl` Take-Profit and Stop-Loss<br><br>`trigger` Trigger Order<br><br>`oco` OCO<br><br>`trailing_stop` Trailing Stop<br><br>`iceberg` Iceberg<br><br>`twap` TWAP |
| data[].createdTime | string |  | Order created timestamp<br><br>A Unix millisecond timestamp |
| data[].updatedTime | string |  | Order update timestamp<br><br>A Unix millisecond timestamp |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1730186730084,
  "data": [
    {
      "orderId": "111111111111111111",
      "clientOid": "111111111111111111",
      "category": "USDT-FUTURES",
      "symbol": "BTCUSDT",
      "qty": "0.01",
      "side": "sell",
      "posSide": "long",
      "status": "pending",
      "tpTriggerBy": "market",
      "slTriggerBy": "market",
      "takeProfit": "110000",
      "stopLoss": "90000",
      "tpOrderType": "market",
      "slOrderType": "market",
      "tpLimitPrice": "91000",
      "slLimitPrice": "111000",
      "triggerBy": "market",
      "triggerPrice": "100000",
      "triggerOrderType": "limit",
      "triggerOrderPrice": "100500",
      "marginMode": "crossed",
      "createdTime": "1730186725663",
      "updatedTime": "1730186725691"
    }
  ]
}
```

## History Strategy Orders

`GET /api/v3/trade/history-strategy-orders`

Get historical strategy orders

- Speed limit is 20 times/s (UID)

- Permission: UTA trade (read)

Operation ID: `utaStrategyGetHistoryStrategyOrders`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| category | query | string | 是 | Product type <br><br> `SPOT` Spot <br><br> `MARGIN` Margin <br><br> `USDT-FUTURES` USDT futures <br><br> `COIN-FUTURES` Coin-M futures <br><br> `USDC-FUTURES` USDC futures |
| type | query | string |  | Strategy Type<br><br>`tpsl` Take-Profit and Stop-Loss<br><br>`trigger` Trigger Order<br><br>`oco` OCO<br><br>`trailing_stop` Trailing Stop<br><br>`iceberg` Iceberg<br><br>`twap` TWAP<br><br>Defaults to `tpsl` |
| startTime | query | string |  | Start timestamp <br><br>A Unix timestamp in milliseconds e.g.,`1597026383085` |
| endTime | query | string |  | End timestamp <br><br>A Unix timestamp in milliseconds e.g.,`1597026383085` |
| limit | query | string |  | Limit per page<br><br>Default:`100`. Maximum:`100` |
| cursor | query | string |  | Cursor <br><br>Pagination is implemented by omitting the cursor in the first query and applying the cursor from the previous query for subsequent pages |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.list | object[] |  | Order list |
| data.list[].orderId | string |  | Order ID |
| data.list[].clientOid | string |  | Client order ID |
| data.list[].category | string |  | Product type <br><br> `USDT-FUTURES` USDT futures <br><br> `COIN-FUTURES` Coin-M futures <br><br> `USDC-FUTURES` USDC futures |
| data.list[].symbol | string |  | Symbol name <br><br>e.g.,`BTCUSDT` |
| data.list[].qty | string |  | Order Quantity |
| data.list[].posSide | string |  | Position side<br><br>`long`/`short` |
| data.list[].status | string |  | Strategy order status<br><br>`success` Executed<br><br>`failed` Execution failed<br><br>`cancelled` Cancelled |
| data.list[].marginMode | string |  | Margin mode<br/>`crossed` Cross margin<br/>`isolated` Isolated margin<br/>If not provided, defaults to cross margin<br/>Available only for futures |
| data.list[].type | string |  | Strategy Type<br><br>`tpsl` Take-Profit and Stop-Loss<br><br>`trigger` Trigger Order<br><br>`oco` OCO<br><br>`trailing_stop` Trailing Stop<br><br>`iceberg` Iceberg<br><br>`twap` TWAP |
| data.list[].tpslMode | string |  | Take-Profit/Stop-Loss mode<br><br>`full`: Take-Profit/Stop-Loss for the entire position<br><br>`partial`: Take-Profit/Stop-Loss for part of the position<br><br>Only has a value for orders with `type=tpsl`; returns an empty string `""` for other strategy types |
| data.list[].createdTime | string |  | Order created timestamp<br><br>A Unix millisecond timestamp |
| data.list[].updatedTime | string |  | Order update timestamp<br><br>A Unix millisecond timestamp |
| data.cursor | string |  | Cursor for next page<br><br>Pass this value as the `cursor` parameter in the next request to get the next page of data |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1730186730084,
  "data": {
    "list": [
      {
        "orderId": "111111111111111111",
        "clientOid": "111111111111111111",
        "category": "USDT-FUTURES",
        "symbol": "BTCUSDT",
        "qty": "0.01",
        "posSide": "long",
        "status": "success",
        "tpTriggerBy": "market",
        "slTriggerBy": "market",
        "takeProfit": "110000",
        "stopLoss": "90000",
        "tpOrderType": "market",
        "slOrderType": "market",
        "tpLimitPrice": "91000",
        "slLimitPrice": "111000",
        "triggerBy": "market",
        "triggerPrice": "100000",
        "triggerOrderType": "limit",
        "triggerOrderPrice": "100500",
        "marginMode": "crossed",
        "tpslMode": "full",
        "createdTime": "1730186725663",
        "updatedTime": "1730186725691"
      }
    ],
    "cursor": "1233319323918499840"
  }
}
```

## Get Strategy Sub-orders

`GET /api/v3/trade/strategy-sub-orders`

Get historical sub-orders generated by a strategy order

Only sub-orders created within 7 days after the strategy order was created can be queried

- Rate limit: 10 times/s (UID)

- Permission: UTA trade (read)

Operation ID: `utaStrategyGetStrategySubOrders`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| orderId | query | string | 是 | Strategy order ID |
| limit | query | string |  | Limit per page<br><br>Default:`100`. Maximum:`100` |
| cursor | query | string |  | Cursor<br><br>Pagination is implemented by omitting the cursor in the first query and applying the cursor from the previous query for subsequent pages |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.list | object[] |  | Sub-order list |
| data.list[].subOrderId | string |  | Sub-order ID |
| data.list[].subClientOid | string |  | Client order ID |
| data.list[].category | string |  | Product type<br><br>`SPOT` Spot<br><br>`MARGIN` Margin<br><br>`USDT-FUTURES` USDT futures<br><br>`COIN-FUTURES` Coin-M futures<br><br>`USDC-FUTURES` USDC futures |
| data.list[].symbol | string |  | Symbol name |
| data.list[].price | string |  | Order price |
| data.list[].qty | string |  | Order quantity<br><br>Unit: base coin |
| data.list[].cumExecQty | string |  | Cumulative executed quantity<br><br>Unit: base coin |
| data.list[].avgPrice | string |  | Average execution price |
| data.list[].side | string |  | Trade side<br><br>`buy`/`sell` |
| data.list[].posSide | string |  | Position side<br><br>`long`/`short`<br><br>Applies to futures orders only |
| data.list[].status | string |  | Order status<br><br>`filled` Filled<br><br>`cancelled` Cancelled<br><br>`failed` Failed |
| data.list[].createdTime | string |  | Order created timestamp<br><br>Unix millisecond timestamp |
| data.list[].updatedTime | string |  | Order updated timestamp<br><br>Unix millisecond timestamp |
| data.cursor | integer |  | Cursor for next page<br><br>Pass this value as the `cursor` parameter in the next request to get the next page of data |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1724486400000.0,
  "data": {
    "list": [
      {
        "subOrderId": "1234567890123456789",
        "subClientOid": "myOrder001",
        "category": "USDT-FUTURES",
        "symbol": "BTCUSDT",
        "price": "60000",
        "qty": "0.01",
        "cumExecQty": "0.01",
        "avgPrice": "60001",
        "side": "buy",
        "posSide": "long",
        "status": "filled",
        "createdTime": "1724486400000",
        "updatedTime": "1724486401000"
      }
    ],
    "cursor": 1234567890123456768
  }
}
```

## Add Investment Amount

`POST /api/v3/trade/grid/add-investment`

Add investment amount to a grid trading bot. Supports adding spot investment amount and adjusting futures margin.

- Rate limit: 1/sec/UID

- Permission: UTA trade (read & write)

Operation ID: `utaGridAddInvestment`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| category | string | 是 | Business line<br/>`SPOT`: Spot trading<br/>`USDT-FUTURES`: USDT-margined futures<br/>`USDC-FUTURES`: USDC-margined futures |
| botId | string | 是 | Grid bot ID. The business line must match the grid bot ID, otherwise an error will be returned |
| coin | string | 是 | Coin to add |
| size | string | 是 | Amount |
| fundsSource | string[] | 是 | Source of funds<br><br>`funding`: Funding account<br><br>`uta`: Unified account<br><br>`otc`: OTC account |
| adjustType | string |  | Adjustment type. Only applicable to futures grid, required for futures<br><br>`increase`<br><br>`decrease` |
| reinvestProfit | string |  | Whether to reinvest profit, default `yes`. Only applicable to spot grid<br><br>`yes`<br><br>`no` |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.botId | string |  | Grid bot ID |

## Get Grid Bot Detail

`GET /api/v3/trade/grid/bot-detail`

Query the detailed information of a specified strategy, including parameter configuration, current status, accumulated profit, etc.

- Rate limit: 10/sec/UID

- Permission: UTA trade (read-only)

Operation ID: `utaGridBotDetail`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| botId | query | string | 是 | Grid bot ID |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.botId | string |  | Grid bot ID |
| data.symbol | string |  | Trading pair |
| data.status | string |  | Status<br><br>`init`: Initializing<br><br>`waiting`: Waiting to start<br><br>`running`: Running<br><br>`terminating`: Terminating<br><br>`terminated`: Terminated |
| data.totalProfit | string |  | Total profit, in USDT |
| data.roi | string |  | ROI, in decimal form |
| data.gridProfit | string |  | Grid profit, in USDT |
| data.gridProfitRate | string |  | Grid profit rate |
| data.unpairedProfit | string |  | Unpaired profit, in USDT |
| data.unpairedProfitRate | string |  | Unpaired profit rate |
| data.margin | string |  | Margin, only for futures |
| data.arbitrageAPR | string |  | Arbitrage APR |
| data.totalAPR | string |  | Total APR |
| data.createdTime | string |  | Creation time |
| data.runningTime | string |  | Running duration, in ms |
| data.currentBaseBalance | string |  | Current base coin balance |
| data.currentQuoteBalance | string |  | Current quote coin balance |
| data.initialBaseHoldings | string |  | Initial base coin holdings |
| data.initialQuoteHoldings | string |  | Initial quote coin holdings |
| data.reservedBaseTradingFee | string |  | Reserved base coin trading fee |
| data.reservedQuoteTradingFee | string |  | Reserved quote coin trading fee |
| data.gridStartPrice | string |  | Grid start price |
| data.gridType | string |  | Grid type<br><br>`long`<br><br>`short`<br><br>`netural` |
| data.maxPrice | string |  | Grid upper limit price |
| data.minPrice | string |  | Grid lower limit price |
| data.gridNum | string |  | Number of grids |
| data.gridOrderMode | string |  | Grid order mode<br><br>`arithmetic`<br><br>`geometric` |
| data.baseInvestmentCoin | string |  | Base coin of investment |
| data.baseInvestmentAmount | string |  | Base coin investment amount |
| data.quoteInvestmentCoin | string |  | Quote coin of investment |
| data.quoteInvestmentAmount | string |  | Quote coin investment amount |
| data.slippage | string |  | Slippage<br><br>`1%`<br><br>`2%`<br><br>`none` |
| data.triggerCondition | string |  | Trigger condition<br><br>`instant`<br><br>`price`<br><br>`rsi`<br><br>`boll` |
| data.triggerParams | object[] |  | Trigger parameters |
| data.triggerParams[].indicatorLength | string |  | Indicator period |
| data.triggerParams[].threshold | string |  | Threshold |
| data.triggerParams[].multiplier | string |  | Multiplier |
| data.triggerParams[].interval | string |  | Interval |
| data.triggerPrice | string |  | Trigger price |
| data.terminationCondition | string |  | Termination condition<br><br>`rsi`<br><br>`boll` |
| data.terminationParams | object[] |  | Termination parameters |
| data.terminationParams[].indicatorLength | string |  | Indicator period |
| data.terminationParams[].threshold | string |  | Threshold |
| data.terminationParams[].multiplier | string |  | Multiplier |
| data.terminationParams[].interval | string |  | Interval |
| data.terminationSell | string |  | Whether to sell on termination<br><br>`yes`<br><br>`no` |
| data.stopLoss | string |  | Stop-loss price |
| data.takeProfit | string |  | Take-profit price |
| data.hodlMode | string |  | HODL mode<br><br>`yes`<br><br>`no` |
| data.autoTransferProfits | string |  | Auto transfer profit<br><br>`yes`<br><br>`no` |
| data.arbitrageCount | string |  | Arbitrage count |
| data.terminationReason | string |  | Termination reason<br><br>`MANUAL_END`: Manually terminated<br><br>`NEW_WAIT`: Waiting to start<br><br>`ACCOUNT_BALANCE_LACKING_END`: Terminated due to insufficient available funds<br><br>`STOP_PROFIT_END`: Terminated by take-profit<br><br>`STOP_LOSS_END`: Terminated by stop-loss<br><br>`CANCEL_END`: Terminated by cancellation<br><br>`SYSTEM_END`: Cancelled due to order placement failure<br><br>`FOLLOW_END`: Terminated by follow<br><br>`SUBSCRIBE_STOP_PROFIT_END`: Terminated by subscription take-profit<br><br>`SUBSCRIBE_STOP_LOSS_END`: Terminated by subscription stop-loss<br><br>`PLACE_ORDER_FAIL_END`: Terminated by consecutive order placement failures<br><br>`SYMBOL_DOWN_END`: Terminated due to trading pair delisting<br><br>`SUB_ACCOUNT_TRANSFER_FAIL`: Terminated due to fund transfer failure<br><br>`HIGHEST_PRICE_END`: Terminated at highest price<br><br>`BOTTOM_PRICE_END`: Terminated at lowest price<br><br>`BURST_END`: Terminated by liquidation<br><br>`MOVE_GRID_FAIL`: Terminated due to grid move failure<br><br>`EXPIRE_TIME_END`: Terminated by scheduled expiration<br><br>`HANDLE_SUB_POSITION_END`: Terminated by manual position reduction<br><br>`STOP_PRICE_ACHIEVE`: Terminated upon reaching stop price<br><br>`ADL_END`: Terminated by ADL<br><br>`AUTO_CONVERT_END`: Terminated by auto-conversion<br><br>`CONDITION_TRIGGER_END`: Terminated by condition trigger<br><br>`ADL_CONVERT_END`: Terminated by ADL reduction<br><br>`CANCEL_DELIVERY_ORDER`: Cancelled due to delivery<br><br>`BASIS_RATE_TRIGGER`: Terminated by basis rate trigger<br><br>`EARN_REDEEM_FAIL`: Terminated due to earn redemption failure<br><br>`SYSTEM_CANCEL`: Cancelled by system<br><br>`SYMBOL_RSTOCK_SPLIT`: Cancelled due to stock split/reverse split |

## Close Grid Bot

`POST /api/v3/trade/grid/close-bot`

Terminate a specified bot, stopping order placement and handling unfilled orders/positions according to the strategy configuration.

- Rate limit: 1/sec/UID

- Permission: UTA trade (read & write)

Operation ID: `utaGridCloseBot`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| botId | string | 是 | Grid bot ID |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data |  |  | Response data |

## Create Grid Bot

`POST /api/v3/trade/grid/create-bot`

Submit a request to create a spot or futures grid trading bot.

- Rate limit: 1/sec/UID

- Permission: UTA trade (read & write)

Operation ID: `utaGridCreateBot`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| category | string | 是 | Business line<br><br>`SPOT`: Spot trading<br><br>`USDT-FUTURES`: USDT-margined futures<br><br>`USDC-FUTURES`: USDC-margined futures |
| symbol | string | 是 | Trading pair name |
| gridType | string |  | Grid direction<br>`long`<br>`short`<br>`neutral`<br>**Required when category is futures (`USDT-FUTURES` / `USDC-FUTURES`); optional for `SPOT`** |
| maxPrice | string | 是 | Grid upper limit price |
| minPrice | string | 是 | Grid lower limit price |
| gridNum | string | 是 | Number of grids |
| gridOrderMode | string | 是 | Grid order mode<br><br>`arithmetic`: Arithmetic<br><br>`geometric`: Geometric |
| leverage | string |  | Leverage, default 1. Only effective for futures |
| investmentAmount | object[] | 是 | Investment amount |
| investmentAmount[].coin | string | 是 | Coin |
| investmentAmount[].amount | string | 是 | Amount |
| fundsSource | string[] | 是 | Source of funds<br><br>`funding`: Funding account<br><br>`uta`: Unified account<br><br>`otc`: OTC account |
| autoReserveMargin | string |  | Auto reserve margin |
| reservedMargin | string |  | Reserved margin. Only effective for futures |
| triggerCondition | string |  | Trigger condition, default `instant`<br><br>`instant`<br><br>`price`<br><br>`rsi`<br><br>`boll` |
| triggerParams | object[] |  | Trigger parameters |
| triggerParams[].indicatorLength | string |  | Indicator length |
| triggerParams[].threshold | string |  | Threshold |
| triggerParams[].multiplier | string |  | Multiplier |
| triggerParams[].interval | string |  | Interval |
| triggerPrice | string |  | Trigger price |
| terminationCondition | string |  | Termination condition<br><br>`rsi`<br><br>`boll` |
| terminationParams | object[] |  | Termination parameters |
| terminationParams[].indicatorLength | string |  | Indicator length |
| terminationParams[].threshold | string |  | Threshold |
| terminationParams[].multiplier | string |  | Multiplier |
| terminationParams[].interval | string |  | Interval |
| terminationSell | string |  | Whether to sell on termination. Only for spot grid<br><br>`yes`<br><br>`no` |
| stopLoss | string |  | Stop-loss price |
| takeProfit | string |  | Take-profit price |
| slippage | string | 是 | Slippage |
| trailingGrid | string |  | Trailing grid, default `no`<br><br>`yes`<br><br>`no` |
| movingAverageGains | string |  | Moving average gains |
| stopUpwardPrice | string |  | Stop upward price |
| hodlMode | string |  | HODL mode, default `no`. Only effective for spot<br><br>`yes`<br><br>`no` |
| marketOpen | string |  | Market open, default enabled. Only effective for futures<br><br>`yes`<br><br>`no` |
| lossReserve | string |  | Loss reserve, default enabled. Only effective for futures<br><br>`yes`<br><br>`no` |
| autoTransferProfits | string | 是 | Auto transfer profits, default `no`<br><br>`yes`<br><br>`no` |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.botId | string |  | Grid bot ID |

## Create Neutral Grid Bot

`POST /api/v3/trade/grid/create-neutral-bot`

Submit a request to create a neutral futures grid trading bot.

- Rate limit: 1/sec/UID

- Permission: UTA trade (read & write)

Operation ID: `utaGridCreateNeutralBot`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| category | string | 是 | Business line<br><br>`USDT-FUTURES`: USDT-margined futures<br><br>`USDC-FUTURES`: USDC-margined futures |
| symbol | string | 是 | Trading pair |
| maxPrice | string | 是 | Upper limit price |
| minPrice | string | 是 | Lower limit price |
| gridNum | string | 是 | Number of grids |
| gridOrderMode | string | 是 | Grid order mode<br><br>`arithmetic`: Arithmetic<br><br>`geometric`: Geometric |
| leverage | string |  | Leverage |
| investmentAmount | object[] |  | List of investment coins and amounts. For futures, only quote coin USDT/USDC is supported |
| investmentAmount[].coin | string | 是 | Investment coin |
| investmentAmount[].amount | string | 是 | Investment amount |
| triggerPrice | string |  | Trigger price |
| stopLoss | string |  | Stop-loss price |
| takeProfit | string |  | Take-profit price |
| autoTransferProfits | string |  | Auto transfer profit |
| fundsSource | string[] | 是 | Source of funds<br><br>`funding`: Funding account<br><br>`uta`: UTA account<br><br>`otc`: OTC account |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.botId | string |  | Grid bot ID |

## Get Grid Bot Order Details

`GET /api/v3/trade/grid/list-details`

Query the order details associated with a specified strategy.

- Rate limit: 1/sec/UID

- Permission: UTA trade (read-only)

Operation ID: `utaGridListDetails`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| category | query | string | 是 | Business line<br/>`SPOT`: Spot trading<br/>`USDT-FUTURES`: USDT-margined futures<br/>`USDC-FUTURES`: USDC-margined futures |
| botId | query | string | 是 | Grid bot ID |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.botId | string |  | Grid bot ID |
| data.symbol | string |  | Trading pair |
| data.buyOrderList | object[] |  | Buy order list |
| data.buyOrderList[].orderId | string |  | Order ID |
| data.buyOrderList[].delegateCount | string |  | Delegated quantity |
| data.buyOrderList[].delegatePrice | string |  | Delegated price |
| data.buyOrderList[].changeRequired | integer |  | Price change required to trigger a fill. Returned with the percentage sign removed, e.g. `1` means `1%` |
| data.sellOrderList | object[] |  | Sell order list |
| data.sellOrderList[].orderId | string |  | Order ID |
| data.sellOrderList[].delegateCount | string |  | Delegated quantity |
| data.sellOrderList[].delegatePrice | string |  | Delegated price |
| data.sellOrderList[].changeRequired | integer |  | Price change required to trigger a fill. Returned with the percentage sign removed, e.g. `1` means `1%` |

## Modify Grid Bot Parameters

`POST /api/v3/trade/grid/modify-bot`

Modify the basic parameters (price range, investment amount, etc.) of a running grid trading bot.

- Rate limit: 1/sec/UID

- Permission: UTA trade (read & write)

Operation ID: `utaGridModifyBot`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| category | string |  | Business line<br/>`SPOT`: Spot trading<br/>`USDT-FUTURES`: USDT-margined futures<br/>`USDC-FUTURES`: USDC-margined futures |
| botId | string | 是 | Grid bot ID |
| takeProfit | string |  | Take-profit price. **If not passed, the take-profit price will be cleared.** If you do not want to modify the current take-profit price, pass in the current value |
| stopLoss | string |  | Stop-loss price. **If not passed, the stop-loss price will be cleared.** If you do not want to modify the current stop-loss price, pass in the current value |
| terminationCondition | string |  | Termination condition<br><br>`rsi`<br><br>`boll` |
| terminationParams | object[] |  | Termination parameters |
| terminationParams[].indicatorLength | string |  | Indicator length |
| terminationParams[].threshold | string |  | Threshold |
| terminationParams[].multiplier | string |  | Multiplier |
| terminationParams[].interval | string |  | Interval |
| hodlMode | string |  | HODL mode<br><br>`yes`<br><br>`no` |
| autoTransferProfits | string |  | Auto transfer profits<br><br>`yes`: transfer out<br><br>`no`: do not transfer out |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.botId | string |  | Grid bot ID |

## Modify Grid Interval and Grid Number

`POST /api/v3/trade/grid/modify-grid-interval`

Modify the grid price range and grid number.

- Rate limit: 1/sec/UID

- Permission: UTA trade (read & write)

Operation ID: `utaGridModifyGridInterval`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| category | string | 是 | Business line<br><br>`SPOT`: Spot trading<br><br>`USDT-FUTURES`: USDT-margined futures<br><br>`USDC-FUTURES`: USDC-margined futures |
| botId | string | 是 | Grid bot ID |
| maxPrice | string | 是 | Grid upper limit price |
| minPrice | string | 是 | Grid lower limit price |
| gridNum | string | 是 | Number of grids |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.botId | string |  | Grid bot ID |

## Modify Neutral Grid Bot Parameters

`POST /api/v3/trade/grid/modify-neutral-bot`

Modify the basic parameters of a running neutral grid trading bot.

- Rate limit: 1/sec/UID

- Permission: UTA trade (read & write)

Operation ID: `utaGridModifyNeutralBot`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| botId | string | 是 | Grid bot ID |
| category | string | 是 | Business line<br><br>`USDT-FUTURES`: USDT-margined futures<br><br>`USDC-FUTURES`: USDC-margined futures |
| takeProfit | string |  | Take-profit price. **If not passed, the take-profit price will be cleared.** Pass the current value if no change is intended |
| stopLoss | string |  | Stop-loss price. **If not passed, the stop-loss price will be cleared.** Pass the current value if no change is intended |
| autoTransferProfits | string |  | Auto transfer profit<br><br>`yes`: Transfer out<br><br>`no`: Do not transfer out |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.botId | string |  | Grid bot ID |

## Modify Neutral Grid Interval and Grid Number

`POST /api/v3/trade/grid/modify-neutral-grid-interval`

Modify the grid price range and number of grids.

- Rate limit: 1/sec/UID

- Permission: UTA trade (read & write)

Operation ID: `utaGridModifyNeutralGridInterval`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| category | string | 是 | Business line<br><br>`USDT-FUTURES`: USDT-margined futures<br><br>`USDC-FUTURES`: USDC-margined futures |
| botId | string | 是 | Grid bot ID |
| maxPrice | string | 是 | Upper limit price |
| minPrice | string | 是 | Lower limit price |
| gridNum | string | 是 | Number of grids |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.botId | string |  | Grid bot ID |

## Get Neutral Grid Bot Detail

`GET /api/v3/trade/grid/neutral-bot-detail`

Query the detailed information of a specified neutral futures grid strategy, including parameter configuration, current status, and cumulative profit.

- Rate limit: 10/sec/UID

- Permission: UTA trade (read-only)

Operation ID: `utaGridNeutralBotDetail`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| botId | query | string | 是 | Grid bot ID |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.botId | string |  | Grid bot ID |
| data.symbol | string |  | Trading pair |
| data.status | string |  | Status<br><br>`init`: Initializing<br><br>`waiting`: Waiting<br><br>`running`: Running<br><br>`terminating`: Terminating<br><br>`terminated`: Terminated |
| data.totalProfit | string |  | Total profit, in USDT |
| data.roi | string |  | ROI, in decimal form |
| data.gridProfit | string |  | Grid profit, in USDT, equal to realized arbitrage profit minus fees |
| data.gridProfitRate | string |  | Grid profit rate, in decimal form |
| data.unpairedProfit | string |  | Unpaired profit, in USDT |
| data.unpairedProfitRate | string |  | Unpaired profit rate, in decimal form |
| data.margin | string |  | Margin (futures only) |
| data.arbitrageAPR | string |  | Arbitrage APR, in decimal form. If running for less than 1 day, calculated as 1 day |
| data.totalAPR | string |  | Total APR, in decimal form. If running for less than 1 day, calculated as 1 day |
| data.createdTime | string |  | Creation time |
| data.runningTime | string |  | Running time, in milliseconds |
| data.gridStartPrice | string |  | Grid start price |
| data.maxPrice | string |  | Upper limit price |
| data.minPrice | string |  | Lower limit price |
| data.gridNum | string |  | Number of grids |
| data.gridOrderMode | string |  | Grid order mode<br><br>`arithmetic`: Arithmetic<br><br>`geometric`: Geometric |
| data.triggerPrice | string |  | Trigger price |
| data.leverage | string |  | Leverage |
| data.stopLoss | string |  | Stop-loss price |
| data.takeProfit | string |  | Take-profit price |
| data.holdPosition | string |  | Holding position |
| data.oneGridMinProfit | string |  | Minimum profit per grid |
| data.oneGridMaxProfit | string |  | Maximum profit per grid |
| data.autoTransferProfits | string |  | Auto transfer profit<br><br>`yes`: Transfer out<br><br>`no`: Do not transfer out |

## Get Neutral Grid Bot Order Details

`GET /api/v3/trade/grid/neutral-list-details`

Query the order details associated with a specified neutral futures grid strategy.

- Rate limit: 1/sec/UID

- Permission: UTA trade (read-only)

Operation ID: `utaGridNeutralListDetails`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| category | query | string | 是 | Business line<br/>`SPOT`: Spot trading<br/>`USDT-FUTURES`: USDT-margined futures<br/>`USDC-FUTURES`: USDC-margined futures |
| botId | query | string | 是 | Grid bot ID |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.botId | string |  | Grid bot ID |
| data.symbol | string |  | Trading pair |
| data.buyOrderList | object[] |  | Buy order list |
| data.buyOrderList[].orderId | string |  | Order ID |
| data.buyOrderList[].delegateCount | string |  | Delegated quantity |
| data.buyOrderList[].delegatePrice | string |  | Delegated price |
| data.buyOrderList[].changeRequired | integer |  | Price change required to trigger a fill. Returned with the percentage sign removed, e.g. `1` means `1%` |
| data.sellOrderList | object[] |  | Sell order list |
| data.sellOrderList[].orderId | string |  | Order ID |
| data.sellOrderList[].delegateCount | string |  | Delegated quantity |
| data.sellOrderList[].delegatePrice | string |  | Delegated price |
| data.sellOrderList[].changeRequired | integer |  | Price change required to trigger a fill. Returned with the percentage sign removed, e.g. `1` means `1%` |

## Validate Neutral Grid Parameters

`POST /api/v3/trade/grid/validate-neutral`

Before creating a neutral grid strategy, validate whether the grid parameters (price range, number of grids, investment amount, etc.) are legal, without actually creating the strategy.

- Rate limit: 1/sec/UID

- Permission: UTA trade (read & write)

Operation ID: `utaGridValidateNeutral`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| category | string | 是 | Business line<br><br>`USDT-FUTURES`: USDT-margined futures<br><br>`USDC-FUTURES`: USDC-margined futures |
| symbol | string | 是 | Trading pair |
| maxPrice | string | 是 | Upper limit price |
| minPrice | string | 是 | Lower limit price |
| gridNum | string | 是 | Number of grids |
| gridOrderMode | string | 是 | Grid order mode<br><br>`arithmetic`: Arithmetic<br><br>`geometric`: Geometric |
| leverage | string |  | Leverage |
| investmentAmount | object[] |  | List of investment coins and amounts. For futures, only quote coin USDT/USDC is supported |
| investmentAmount[].coin | string | 是 | Investment coin |
| investmentAmount[].amount | string | 是 | Investment amount |
| triggerPrice | string |  | Trigger price |
| stopLoss | string |  | Stop-loss price |
| takeProfit | string |  | Take-profit price |
| autoTransferProfits | string |  | Auto transfer profit |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.valid | string |  | Whether validation passed |
| data.reason | string |  | Reason for validation failure |
| data.minInvestment | string |  | Minimum investment amount |

## Validate Grid Parameters

`POST /api/v3/trade/grid/validate`

Before creating a grid strategy, validate whether the grid parameters (price range, grid number, investment amount, etc.) are legal. This does not actually create a strategy.

- Rate limit: 1/sec/UID

- Permission: UTA trade (read & write)

Operation ID: `utaGridValidate`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| category | string | 是 | Business line<br><br>`SPOT`: Spot trading<br><br>`USDT-FUTURES`: USDT-margined futures<br><br>`USDC-FUTURES`: USDC-margined futures |
| symbol | string | 是 | Trading pair name |
| gridType | string |  | Grid direction<br>`long`<br>`short`<br>`neutral`<br>**Required when category is futures (`USDT-FUTURES` / `USDC-FUTURES`); optional for `SPOT`** |
| maxPrice | string | 是 | Grid upper limit price |
| minPrice | string | 是 | Grid lower limit price |
| gridNum | string | 是 | Number of grids |
| gridOrderMode | string | 是 | Grid order mode<br><br>`arithmetic`: Arithmetic<br><br>`geometric`: Geometric |
| leverage | string |  | Leverage, default 1. Only effective for futures |
| investmentAmount | object[] | 是 | Investment amount |
| investmentAmount[].coin | string | 是 | Coin |
| investmentAmount[].amount | string | 是 | Amount |
| reservedMargin | string |  | Reserved margin. Only effective for futures |
| triggerCondition | string |  | Trigger condition, default `instant`<br><br>`instant`<br><br>`price`<br><br>`rsi`<br><br>`boll` |
| triggerParams | object[] |  | Trigger parameters |
| triggerParams[].indicatorLength | string |  | Indicator length |
| triggerParams[].threshold | string |  | Threshold |
| triggerParams[].multiplier | string |  | Multiplier |
| triggerParams[].interval | string |  | Interval |
| triggerPrice | string |  | Trigger price |
| terminationCondition | string |  | Termination condition<br><br>`rsi`<br><br>`boll` |
| terminationParams | object[] |  | Termination parameters |
| terminationParams[].indicatorLength | string |  | Indicator length |
| terminationParams[].threshold | string |  | Threshold |
| terminationParams[].multiplier | string |  | Multiplier |
| terminationParams[].interval | string |  | Interval |
| stopLoss | string |  | Stop-loss price |
| takeProfit | string |  | Take-profit price |
| trailingGrid | string |  | Trailing grid, default `no`<br><br>`yes`<br><br>`no` |
| movingAverageGains | string |  | Moving average gains |
| stopUpwardPrice | string |  | Stop upward price |
| hodlMode | string |  | HODL mode, default `no`. Only effective for spot<br><br>`yes`<br><br>`no` |
| marketOpen | string |  | Market open, default enabled. Only effective for futures<br><br>`yes`<br><br>`no` |
| lossReserve | string |  | Loss reserve, default enabled. Only effective for futures<br><br>`yes`<br><br>`no` |
| autoTransferProfits | string | 是 | Auto transfer profits, default `no`<br><br>`yes`<br><br>`no` |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.valid | string |  | Whether the validation passed |
| data.reason | string |  | Reason for validation failure |
| data.minInvestment | string |  | Minimum investment amount |


---

统一账户下单、改单、撤单与订单/仓位查询，以及策略交易（计划委托）和网格交易。

版本: 1.0.0

## 服务地址

- `https://api.bitget.com`

## 接口列表

- `POST /api/v3/trade/place-order` — 下单
- `POST /api/v3/trade/modify-order` — 修改订单
- `POST /api/v3/trade/cancel-order` — 撤单
- `POST /api/v3/trade/countdown-cancel-all` — 倒计时全部撤单
- `POST /api/v3/trade/place-batch` — 批量下单
- `POST /api/v3/trade/batch-modify-order` — 批量修改订单
- `POST /api/v3/trade/cancel-batch` — 批量撤单
- `POST /api/v3/trade/cancel-symbol-order` — 一键撤单
- `GET /api/v3/trade/order-info` — 获取订单信息
- `GET /api/v3/trade/unfilled-orders` — 获取当前委托
- `GET /api/v3/trade/history-orders` — 获取历史委托
- `GET /api/v3/trade/fills` — 获取成交明细
- `POST /api/v3/trade/place-reality-order` — 创建Reality股票订单
- `POST /api/v3/trade/cancel-reality-order` — 撤销Reality股票订单
- `POST /api/v3/account/max-open-available` — 获取最大可开可用
- `POST /api/v3/trade/close-positions` — 一键平仓
- `POST /api/v3/account/move-positions` — 仓位转移
- `GET /api/v3/account/move-position-history` — 获取移仓历史
- `GET /api/v3/position/current-position` — 获取当前仓位
- `GET /api/v3/position/history-position` — 获取历史仓位
- `GET /api/v3/position/adlRank` — 获取仓位ADL排名
- `GET /api/v3/trade/loan-data` — 获取借币数据
- `POST /api/v3/trade/place-strategy-order` — 创建策略单
- `POST /api/v3/trade/modify-strategy-order` — 修改策略单
- `POST /api/v3/trade/cancel-strategy-order` — 撤销策略单
- `GET /api/v3/trade/unfilled-strategy-orders` — 获取当前策略单
- `GET /api/v3/trade/history-strategy-orders` — 获取历史策略单
- `GET /api/v3/trade/strategy-sub-orders` — 获取历史策略子订单
- `POST /api/v3/trade/grid/add-investment` — 追加投资额
- `GET /api/v3/trade/grid/bot-detail` — 查询网格交易机器人详情
- `POST /api/v3/trade/grid/close-bot` — 终止网格交易机器人
- `POST /api/v3/trade/grid/create-bot` — 创建网格交易机器人
- `POST /api/v3/trade/grid/create-neutral-bot` — 创建中性网格交易机器人
- `GET /api/v3/trade/grid/list-details` — 查询网格交易机器人挂单详情
- `POST /api/v3/trade/grid/modify-bot` — 修改网格交易机器人参数
- `POST /api/v3/trade/grid/modify-grid-interval` — 修改网格区间和网格数
- `POST /api/v3/trade/grid/modify-neutral-bot` — 修改中性网格交易机器人参数
- `POST /api/v3/trade/grid/modify-neutral-grid-interval` — 修改中性网格区间和网格数
- `GET /api/v3/trade/grid/neutral-bot-detail` — 查询中性网格交易机器人详情
- `GET /api/v3/trade/grid/neutral-list-details` — 查询中性网格机器人挂单详情
- `POST /api/v3/trade/grid/validate-neutral` — 验证中性网格参数
- `POST /api/v3/trade/grid/validate` — 验证网格输入

## 下单

`POST /api/v3/trade/place-order`

- 限频规则: 10次/秒/UID
- 需要统一账户交易读写权限

> 该接口现支持 Reality 股票交易对（rtoken，如 `rAAPLUSDT`）下单。Reality 订单适用独立限频规则：默认 `5次/秒/UID`，白名单用户 `30次/秒/UID`。

该接口支持现货、杠杆及合约下单，并可以自定义包括价格、数量和订单类型等参数。

- **合约交易**<br/>合约单向持仓下只减仓订单，如果已经存在减仓单并且减仓单数量已经等于仓位数量，或者你新下的减仓单大于仓位剩余数量，会自动把之前减仓单取消，重新下新的减仓单，此时返回的信息 orderId会为 null，**建议一定要传`cliendOid`**


- **杠杆交易**<br/>杠杆下单会自动借贷


- **订单检查**
    - **合约**：`Price`下单价格要满足价格乘数`priceMultiplier`的倍数，并且符合`pricePrecision`小数位。`qty`要满足大于`minOrderAmount`并且满足`sizeMultiplier`的倍数

    - **现货**：`price`要满足小数位。`qty`下单数量必须要大于`minOrderAmount`


- **开仓逻辑**
    - **双向持仓**

      开多： `side=buy` & `posSide=long`

      开空：`side=sell` & `posSide=short`

      平多：`side=sell` & `posSide=long`

      平空：`side=buy` & `posSide=short`


    - **单向持仓**

      开多 `side`:buy

      开空 `side`:sell

      平多 `side`:sell   `reduceOnly`:yes

      平空 `side`:buy    `reduceOnly`:yes



- **订单持有上限:**
    - **合约**: USDT合约/币本位合约/USDC合约所有交易对加起来一共最多支持400个订单
    - **现货**: 现货/杠杆所有交易对最多支持400订单


- **请求监控**:

  将针对您的 API 请求进行统计监控，当单日 (UTC 0点 - UTC 24点) 单账号（母账号和子账号整体运算）订单总数超过一定上限，平台将保留提醒、警告，以及进行必要性限制的权利。使用API的客户预设接收本条款并负有配合调整的义务。


- **API Broker返佣标识**:

  需在HTTP Header请求头中添加如下代码块
  > "X-CHANNEL-API-CODE":"your-channel-api-code"


- **币本位合约说明**:

    - **新币本位业务线symbol格式为"XXXUSD_CM"，例如BTCUSD交易对在币本位合约的格式为BTCUSD_CM**
    - 新币本位暂时不支持修改订单，ADL，策略单，预设止盈止损

注意：操作订单时出现以下错误，请用`clientOid`查询订单详情，以确认操作的最终结果

 > { "code": "40010", "msg": "Request timed out", "requestTime": 1666268894074, "data": null } <br/> { "code": "40725", "msg": "service return an error", "requestTime": 1666268894071, "data": null } <br/> { "code": "45001", "msg": "Unknown error", "requestTime": 1666268894071, "data": null }

Operation ID: `utaTradeOrderPlaceOrder`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| category | string | 是 | 产品类型<br/>`SPOT` 现货交易<br/>`MARGIN` 杠杆交易<br/>`USDT-FUTURES` USDT合约<br/>`COIN-FUTURES` 币本位合约<br/>`USDC-FUTURES` USDC合约 |
| symbol | string | 是 | 交易对名称<br/>例如：`BTCUSDT` |
| qty | string | 是 | 下单数量<br/>现货/杠杆：<br/>市价买单，单位为 **quote coin**<br/>限价及市价卖单，单位为 **base coin**  <br/>USDT/USDC合约： <br/>单位为 **base coin**  <br/>币本位合约： <br/>单位为 **quote coin** |
| price | string |  | 下单价格<br/>订单类型为限价单`limit`时，该字段必填<br/>订单类型为市价单`market`时，该字段失效 |
| side | string | 是 | 下单方向<br/>`buy`: 买<br/>`sell`: 卖 |
| orderType | string | 是 | 订单类型<br/>`limit`: 限价单<br/>`market`: 市价单 |
| timeInForce | string |  | 订单执行策略<br/>`ioc`: 无法立即成交的部分就撤销<br/>`fok`: 无法全部立即成交就撤销<br/>`gtc`: 普通订单, 订单会一直有效，直到被成交或者取消<br/>`post_only`: 只做maker<br/>`rpi`: 零售价格优化订单，为零售订单流提供价格优化的非显示限价单。仅限拥有RPI做市商权限的账户使用。<br/>订单类型为限价单`limit`时，默认值为`gtc`；<br/>订单类型为市价单`market`时，系统会按照`ioc`执行 |
| posSide | string |  | 仓位方向 <br/>双向持仓模式下必填，单向持仓时不要填，否则会报错<br/>`long`: 多头<br/>`short`: 空头   <br/>只适用于合约交易 |
| clientOid | string |  | 自定义订单ID, `^[0-9A-Za-z_:#\\-+\\s]{1,32}$` |
| reduceOnly | string |  | 是否只减仓:`yes`,`no`，默认`no`;<br/>`yes`表示确保委托的执行只以平仓为目的，减少仓位<br/>仅适用于**单向持仓**模式下 |
| stpMode | string |  | STP模式（自成交预防）<br/>`none`：不设置STP（默认值）<br/>`cancel_taker`：取消taker单 <br/>`cancel_maker`：取消maker单 <br/>`cancel_both`：两者都取消 |
| tpTriggerBy | string |  | 预设止盈触发类型<br/>`market`：市场价格<br/>`mark`：标记价格<br/>如不填写，默认值为market市场价格<br/>该字段仅针对合约业务线usdt-futures，coin-futures及usdc-futures生效 |
| slTriggerBy | string |  | 预设止损触发类型<br/>`market`市场价格<br/>`mark`标记价格<br/>如不填写，默认值为market市场价格<br/>该字段仅针对合约业务线usdt-futures，coin-futures及usdc-futures生效 |
| takeProfit | string |  | 预设止盈触发价格 |
| stopLoss | string |  | 预设止损触发价格 |
| tpOrderType | string |  | 止盈触发的策略单类型<br/>`limit` 限价单<br/>`market` 市价单<br/>Reality（rtoken）交易对暂时仅支持`market`市价单 |
| slOrderType | string |  | 止损触发的策略单类型<br/>`limit` 限价单<br/>`market` 市价单<br/>Reality（rtoken）交易对暂时仅支持`market`市价单 |
| tpLimitPrice | string |  | 止盈策略单执行价格<br/>仅限价单`tpOrderType=limit`时有效，市价单忽略该参数 |
| slLimitPrice | string |  | 止损策略单执行价格<br/>仅限价单`slOrderType=limit`时有效，市价单忽略该参数 |
| marginMode | string |  | 保证金模式<br/>`crossed` 全仓<br/>`isolated` 逐仓<br/>不传默认为全仓<br/>仅适用于合约 |
| autoBorrow | string |  | 自动借币开关<br/>`yes` 开启<br/>`no` 关闭（默认）<br/>仅用于现货下单。开启后，若得到币不支持借贷、消耗币支持借贷，则在消耗币可用余额不足时，系统将自动借入消耗币，补足委托所需金额。 |
| pxAmendType | string |  | 订单价格修正类型<br/>`no` 当委托价格超出价格限制时，不允许系统修改订单价格，委托单会被拒绝（默认）<br/>`yes` 当委托价格超出价格限制时，允许系统将价格修改为限制范围内的最优值进行下单<br/>仅对限价单（`orderType`=`limit`）生效 |

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

## 修改订单

`POST /api/v3/trade/modify-order`

支持通过订单号orderId或者自定义订单号clientOid来修改订单

仅支持修改未完全成交的订单。如订单已完全成交，您将无法通过该接口修改<br/>修改提交后到返回结果前，无法重复提交修改请求
- 限频规则: 10次/秒/UID
- 需要统一账户交易读写权限

Operation ID: `utaTradeOrderModifyOrder`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| orderId | string |  | 订单ID<br/>orderId和clientOid二者必填其一<br/>如同时传入orderId及clientOid，则orderId优先级更高 |
| clientOid | string |  | 自定义订单ID <br/>orderId和clientOid二者必填其一<br/>如同时传入orderId及clientOid，则orderId优先级更高 |
| qty | string |  | 下单数量<br/>单位为基础币 <br/>qty和price二者必填其一 |
| price | string |  | 下单价格 <br/>qty和price二者必填其一 |
| requestId | number |  | 自定义requestId，用于标识本次改单请求<br/>只支持18位以内的数字<br/>当 autoCancel=yes 且改单请求被拒绝时会返回 |
| autoCancel | string |  | **修改订单失败是否撤销原订单**<br/>`yes`: 撤销 <br/>`no`: 不撤销（默认值）<br/>若设置为 `yes`：撮合改单失败后，直接执行撤单；撤单后，柜台将拒绝该订单的后续改单请求（含在途及新请求）。 |
| symbol | string |  | 交易对名称<br/>例如：`BTCUSDT` |
| category | string |  | 产品类型<br/>`SPOT` 现货交易<br/>`MARGIN` 杠杆交易<br/>`USDT-FUTURES` USDT合约<br/>`COIN-FUTURES` 币本位合约<br/>`USDC-FUTURES` USDC合约 |
| tpTriggerBy | string |  | 预设止盈触发类型<br/>`market` 市场价格<br/>`mark` 标记价格<br/>如不填写，默认值为market市场价格<br/>该字段仅针对合约业务线USDT-FUTURES、COIN-FUTURES及USDC-FUTURES生效<br/>若不传或传空，则代表不修改现有值 |
| slTriggerBy | string |  | 预设止损触发类型<br/>`market` 市场价格<br/>`mark` 标记价格<br/>如不填写，默认值为market市场价格<br/>该字段仅针对合约业务线USDT-FUTURES、COIN-FUTURES及USDC-FUTURES生效<br/>若不传或传空，则代表不修改现有值 |
| takeProfit | string |  | 预设止盈触发价格<br/>若不传或传空，则代表不修改现有值<br/>若传"0"，则代表取消止盈 |
| stopLoss | string |  | 预设止损触发价格<br/>若不传或传空，则代表不修改现有值<br/>若传"0"，则代表取消止损 |
| tpOrderType | string |  | 止盈触发的策略单类型<br/>`limit` 限价单<br/>`market` 市价单 |
| slOrderType | string |  | 止损触发的策略单类型<br/>`limit` 限价单<br/>`market` 市价单 |
| tpLimitPrice | string |  | 止盈策略单执行价格<br/>仅限价单`tpOrderType=limit`时有效，市价单忽略该参数<br/>若不传或传空，则代表不修改现有值 |
| slLimitPrice | string |  | 止损策略单执行价格<br/>仅限价单`slOrderType=limit`时有效，市价单忽略该参数<br/>若不传或传空，则代表不修改现有值 |
| pxAmendType | string |  | 订单价格修正类型<br/>`no` 当委托价格超出价格限制时，不允许系统修改订单价格，委托单会被拒绝（默认）<br/>`yes` 当委托价格超出价格限制时，允许系统将价格修改为限制范围内的最优值进行下单<br/>仅对限价单（`orderType`=`limit`）生效 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.orderId | string |  | 订单号 |
| data.clientOid | string |  | 自定义订单号 |

```json
{
  "code": "00000",
  "data": {
    "orderId": "1",
    "clientOid": "12313"
  },
  "msg": "success",
  "requestTime": 1627293504612
}
```

## 撤单

`POST /api/v3/trade/cancel-order`

> 该接口现支持 Reality 股票交易对（rtoken，如 `rAAPLUSDT`）撤单。Reality 订单适用独立限频规则：默认 `5次/秒/UID`，白名单用户 `30次/秒/UID`。

该接口支持取消单独的现货、合约、杠杆的未成交以及部分成交订单
- 限频规则: 10次/秒/UID
- 需要统一账户交易读写权限

Operation ID: `utaTradeOrderCancelOrder`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| orderId | string |  | 订单号<br/>clientOid和orderId二者必填其一<br/>如用户同时传入orderId及clientOid,则orderId优先级更高 |
| clientOid | string |  | 自定义订单号d<br/>clientOid和orderId二者必填其一<br/>如用户同时传入orderId及clientOid,则orderId优先级更高 |
| category | string |  | 产品类型<br/>`SPOT` 现货交易<br/>`MARGIN` 杠杆交易<br/>`USDT-FUTURES` USDT合约<br/>`COIN-FUTURES` 币本位合约<br/>`USDC-FUTURES` USDC合约 |

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
    "orderId": "111111111111111111"
  }
}
```

## 倒计时全部撤单

`POST /api/v3/trade/countdown-cancel-all`

实际使用时，客户端需要定期重复发送心跳请求，以防止异常断连或系统崩溃导致的挂单失控情况

举例说明，假设您预期的心跳周期为10s，即如果超过10s未发送心跳请求，则需要撤销全部订单


正常情况下，可以选择每3-5s调用一次该接口，将countdown设置为10，并以此反复调用来重置倒计时

异常情况下，超过10s未发送心跳请求，则账户下的全部订单将被自动撤销；自动撤销后，Deadman switch机制将自动关闭

如需手动关闭Deadman Switch机制，则将countdown设置为0即可

  p.s 该接口仅支持撤销UTA账户下的订单，不支持撤销经典账户下的订单


该接口请联系对接BD申请接入权限
- 限频规则: 1次/秒/UID
- 需要统一账户交易读写权限

Operation ID: `utaTradeOrderCountDownCancelAll`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| countdown | string | 是 | 重连窗口期<br/>- 单位为秒 <br/>- 正整数，范围为[5,60]，倒计时最小为5s，最大为60s <br/>- 如填写0，则表示取消倒计时撤单功能 |

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
  "requestTime": 1728625799912,
  "data": "success"
}
```

## 批量下单

`POST /api/v3/trade/place-batch`

该接口支持现货、杠杆及合约的批量下单，并可以自定义包括价格、数量和订单类型等参数。

**新功能预告** (当前暂不支持)
    - 逐仓杠杆交易即将上线
    - 跟单交易即将上线
    - 即将支持止盈止损功能


**合约交易**<br/>合约单向持仓下只减仓订单，如果已经存在减仓单并且减仓单数量已经等于仓位数量，或者你新下的减仓单大于仓位剩余数量，会自动把之前减仓单取消，重新下新的减仓单，此时返回的信息<br/>  orderId会为 null，**建议一定要传`cliendOid`（暂不支持`reduce-only`订单）**


**杠杆交易**<br/>杠杆下单会自动借贷


**订单检查**
    - **合约**：`Price`下单价格要满足价格乘数`priceMultiplier`的倍数，并且符合`pricePrecision`小数位。`qty`要满足大于<br/>      `minTradeUSDT`并且满足`sizeMultiplier`的倍数

    - **现货**：`price`要满足小数位。`qty`下单数量必须要大于`minTradeUSDT`


**开仓逻辑**
    - **双向持仓**

      开多： `side=buy` & `posSide=long`

      开空：`side=sell` & `posSide=short`

      平多：`side=sell` & `posSide=long`

      平空：`side=buy` & `posSide=short`


    - **单向持仓**

      开多 `side`:buy

      开空 `side`:sell

      平多 `side`:sell   `reduceOnly`:yes

      平空 `side`:buy    `reduceOnly`:yes



**订单持有上限:**
    - **合约**: USDT合约/币本位合约/USDC合约所有交易对加起来一共最多支持400个订单
    - **现货**: 现货/杠杆所有交易对最多支持400订单


**请求监控**:

  将针对您的 API 请求进行统计监控，当单日 (UTC 0点 - UTC 24点) 单账号（母账号和子账号整体运算）订单总数超过一定上限，平台将保留提醒、警告，以及进行必要性限制的权利。<br/>  使用API的客户预设接收本条款并负有配合调整的义务。


**API Broker返佣标识**:

  需在HTTP Header请求头中添加如下代码块
  > "X-CHANNEL-API-CODE":"your-channel-api-code"

下单出现错误

  > { "code":"40762", "msg":"The order size is greater than the max open size", "requestTime":1627293504612 }

  ><br/>  两种原因
    - 账户余额不足

    -<br/>  当前交易对当前杠杆仓位梯度已满，具体仓位梯度请参考 <br/>  这里


注意：操作订单时出现以下错误，请用`clientOid`查询订单详情，以确认操作的最终结果

> { "code": "40010", "msg": "Request timed out", "requestTime": 1666268894074, "data": null }

> { "code": "40725", "msg": "service return an error", "requestTime": 1666268894071, "data": null }

> { "code": "45001", "msg": "Unknown error", "requestTime": 1666268894071, "data": null }
- 限频规则: 5次/秒/UID
- 批量限制：每批不能超过20笔委托单
- 需要统一账户交易读写权限

Operation ID: `utaTradeOrderPlaceBatch`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| category | string | 是 | 产品类型<br/>`SPOT` 现货交易<br/>`MARGIN` 杠杆交易<br/>`USDT-FUTURES` USDT合约<br/>`COIN-FUTURES` 币本位合约<br/>`USDC-FUTURES` USDC合约 <br/>所有委托单的产品类型必须相同 |
| symbol | string | 是 | 交易对名称<br/>例如：`BTCUSDT` |
| qty | string | 是 | 下单数量<br/>现货/杠杆：<br/>市价买单，单位为**quote coin**<br/>限价及市价卖单，单位为**base coin**<br/>USDT/USDC合约： <br/>单位为**base coin**  <br/>币本位合约： <br/>单位为 **quote coin** |
| price | string |  | 下单价格<br/>订单类型为限价单`limit`时，该字段必填<br/>订单类型为市价单`market`时，该字段失效 |
| side | string | 是 | 下单方向<br/>`buy`: 买<br/>`sell`: 卖 |
| orderType | string | 是 | 订单类型<br/>`limit`: 限价单<br/>`market`: 市价单 |
| timeInForce | string |  | 订单执行策略<br/>`ioc`: 无法立即成交的部分就撤销<br/>`fok`: 无法全部立即成交就撤销<br/>`gtc`: 普通订单, 订单会一直有效，直到被成交或者取消<br/>`post_only`: 只做maker<br/>`rpi`: 零售价格优化订单，为零售订单流提供价格优化的非显示限价单。仅限拥有RPI做市商权限的账户使用。<br/>订单类型为限价单`limit`时，默认值为`gtc`；<br/>订单类型为市价单`market`时，系统会按照`ioc`执行 |
| posSide | string |  | 仓位方向 <br/>双向持仓模式下必填，单向持仓时不要填，否则会报错<br/>`long`: 多头<br/>`short`: 空头   <br/>只适用于合约交易 |
| clientOid | string |  | 自定义订单ID,  `[0-9A-Za-z_:#\\-+\\s]{1,32}$` |
| stpMode | string |  | STP模式<br/>`none` 不设置STP（默认） <br/>`cancel_taker` 取消taker单 <br/>`cancel_maker` 取消maker单 <br/>`cancel_both` 两者都取消 |
| pxAmendType | string |  | 订单价格修正类型<br/>`no` 当委托价格超出价格限制时，不允许系统修改订单价格，委托单会被拒绝（默认）<br/>`yes` 当委托价格超出价格限制时，允许系统将价格修改为限制范围内的最优值进行下单<br/>仅对限价单（`orderType`=`limit`）生效 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.orderId | string |  | 订单id |
| data.clientOid | string |  | 自定义订单id |
| data.code | string |  | 这笔委托单的Error code |
| data.msg | string |  | 这笔委托单的Error message |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695806875837,
  "data": [
    {
      "clientOid": "121211212122",
      "orderId": "121211212122"
    }
  ]
}
```

## 批量修改订单

`POST /api/v3/trade/batch-modify-order`

支持API批量改单，可以同时提交多笔跨交易对订单（限同一个业务线订单）<br/>每次请求最多支持修改20笔<br/>支持连续改单，即在前一个改单申请完成前可以再提交多个改单申请，在途修改订单最多连续提交5笔改单申请，撮合将依序处理改单请求<br/>同一批改单申请中，每个委托订单只能存在一个<br/>仅支持完全未成交订单修改价格、数量<br/>支持部分成交订单修改价格、数量 (不可低于已成交数量)<br/>不支持改只减仓(reduceOnly)委托
- 限频规则: 10次/秒/UID
- 需要统一账户交易读写权限

Operation ID: `utaTradeOrderBatchModifyOrders`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| orderId | string |  | 订单ID<br/>orderId和clientOid二者必填其一<br/>如同时传入orderId及clientOid，则orderId优先级更高 |
| clientOid | string |  | 自定义订单ID <br/>orderId和clientOid二者必填其一<br/>如同时传入orderId及clientOid，则orderId优先级更高 |
| qty | string |  | 下单数量<br/>`base coin` |
| price | string |  | 下单价格 |
| requestId | number |  | 自定义requestId，用于标识本次改单请求<br/>只支持18位以内的数字<br/>当 autoCancel=yes 且改单请求被拒绝时会返回 |
| autoCancel | string |  | **修改订单失败是否撤销原订单**<br/>`yes`: 撤销 <br/>`no`: 不撤销（默认值）<br/>若设置为 `yes`：撮合改单失败后，直接执行撤单；撤单后，柜台将拒绝该订单的后续改单请求（含在途及新请求）。 |
| category | string |  | 产品类型<br/>`SPOT` 现货交易<br/>`MARGIN` 杠杆交易<br/>`USDT-FUTURES` USDT合约<br/>`COIN-FUTURES` 币本位合约<br/>`USDC-FUTURES` USDC合约 |
| symbol | string |  | 交易对名称<br/>例如：`BTCUSDT` |
| pxAmendType | string |  | 订单价格修正类型<br/>`no` 当委托价格超出价格限制时，不允许系统修改订单价格，委托单会被拒绝（默认）<br/>`yes` 当委托价格超出价格限制时，允许系统将价格修改为限制范围内的最优值进行下单<br/>仅对限价单（`orderType`=`limit`）生效 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.orderId | string |  | 订单号 |
| data.clientOid | string |  | 自定义订单号 |

```json
{
  "code": "00000",
  "data": [
    {
      "orderId": "1",
      "clientOid": "12312"
    },
    {
      "orderId": "2",
      "clientOid": "2321"
    }
  ],
  "msg": "success",
  "requestTime": 1627293504612
}
```

## 批量撤单

`POST /api/v3/trade/cancel-batch`

该接口支持批量取消现货、合约、杠杆的未成交以及部分成交订单<br/>在批量撤单操作中，请确保每次调用仅使用orderId或clientOid进行标识，避免混用。如果在一次调用中混合使用orderId和clientOid，则clientOid将失效<br/>批量撤单允许部分成功
- 限频规则: 5次/秒/UID
- 批量限制：每批不能超过20笔委托单
- 需要统一账户交易读写权限

Operation ID: `utaTradeOrderCancelBatch`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| orderId | string |  | 订单号<br/>clientOid和orderId二者必填其一<br/>如用户同时传入orderId及clientOid,则orderId优先级更高 |
| clientOid | string |  | 自定义订单号d<br/>clientOid和orderId二者必填其一<br/>如用户同时传入orderId及clientOid,则orderId优先级更高 |
| category | string | 是 | 产品类型<br/>`SPOT` 现货交易<br/>`MARGIN` 杠杆交易<br/>`USDT-FUTURES` USDT合约<br/>`COIN-FUTURES` 币本位合约<br/>`USDC-FUTURES` USDC合约 <br/>所有委托单的产品类型必须相同 |
| symbol | string | 是 | 交易对名称<br/>例如：`BTCUSDT` |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.orderId | string |  | 订单id |
| data.clientOid | string |  | 自定义订单id |
| data.code | string |  | 这笔委托单的Error code |
| data.msg | string |  | 这笔委托单的Error message |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1751970947623,
  "data": [
    {
      "orderId": "1311111111111111111",
      "clientOid": null,
      "code": "25204",
      "msg": "订单不存在"
    },
    {
      "orderId": "1311111111111111111",
      "clientOid": "1311111111111111111"
    }
  ]
}
```

## 一键撤单

`POST /api/v3/trade/cancel-symbol-order`

按交易对或者业务线撤销未成交以及部分成交的挂单
- 限频规则: 5次/秒/UID
- 需要统一账户交易读写权限

Operation ID: `utaTradeOrderCancelAllOrder`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| category | string | 是 | 产品类型<br/>`SPOT` 现货交易<br/>`MARGIN` 杠杆<br/>`USDT-FUTURES` U本位合约<br/>`COIN-FUTURES` 币本位合约<br/>`USDC-FUTURES` USDC合约 |
| symbol | string |  | 交易对名称<br/>例如：`BTCUSDT` 如不填，则取消 `category` 下所有symbol挂单 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.list | object[] |  | 列表 |
| data.list[].orderId | string |  | 订单ID |
| data.list[].clientOid | string |  | 自定义订单ID |
| data.list[].msg | string |  | 失败原因 |
| data.list[].code | string |  | 错误码 |

```json
{
  "code": "00000",
  "data": {
    "list": [
      {
        "orderId": "111111111111111111",
        "clientOid": "111111111111111111",
        "code": "24056",
        "msg": "notExisted"
      }
    ]
  },
  "msg": "success",
  "requestTime": 1627293504612
}
```

## 获取订单信息

`GET /api/v3/trade/order-info`

通过orderId或者clientOid获取订单详情
- 限频规则: 20次/秒/UID
- 需要统一账户交易只读/读写权限

Operation ID: `utaTradeOrderGetOrderDetails`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| orderId | query | string |  | 订单号<br/>`clientOid`和`orderId`必传其一。如同时传参，则`orderId`优先级更高 |
| clientOid | query | string |  | 自定义订单号<br/>`clientOid`和`orderId`必传其一。如同时传参，则`orderId`优先级更高 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.orderId | string |  | 订单ID |
| data.clientOid | string |  | 自定义订单ID |
| data.category | string |  | 产品类型<br/>`SPOT` 现货交易<br/>`MARGIN` 杠杆交易<br/>`USDT-FUTURES` U本位合约<br/>`COIN-FUTURES` 币本位合约<br/>`USDC-FUTURES` USDC合约 |
| data.symbol | string |  | 交易对名称 |
| data.price | string |  | 委托价格 |
| data.qty | string |  | 委托数量<br/>_单位为base coin_ |
| data.amount | string |  | 委托金额<br/>_单位为quote coin_ |
| data.orderType | string |  | 订单类型 <br/>`limit`: 限价 <br/>`market`: 市价 |
| data.cumExecQty | string |  | 累计成交数量<br/>_单位为base coin_ |
| data.cumExecValue | string |  | 累计成交价值<br/>_单位为quote coin_ |
| data.avgPrice | string |  | 平均成交价 |
| data.orderStatus | string |  | 订单状态<br/>`live`: 订单已创建<br/>`new`: 订单已进入撮合<br/>`partially_filled`: 部分成交<br/>`filled`: 全部成交<br/>`cancelled`: 已撤销 |
| data.side | string |  | 开单方向<br/>`buy`: 买<br/>`sell`: 卖 |
| data.timeInForce | string |  | 订单执行策略<br/>`ioc`: 无法立即成交的部分就撤销<br/>`fok`: 无法全部立即成交就撤<br/>`gtc`: 普通订单, 订单会一直有效，直到被成交或者取消<br/>`post_only`: 只做maker<br/>`rpi`: 零售价格优化订单 |
| data.posSide | string |  | 仓位方向<br/>`long`: 开<br/>`short`: 平<br/>只适用合约订单 |
| data.tradeSide | string |  | 交易方向 <br/>`open`: 开 <br/>`close` : 平     <br/>详细枚举可以在 枚举 页面获取 |
| data.holdMode | string |  | 持仓模式<br/>`one_way_mode`: 单向持仓<br/>`hedge_mode`: 双向持仓<br/>只适用合约订单 |
| data.marginMode | string |  | 保证金模式<br/>`crossed`: 全仓<br/>`isolated`: 逐仓<br/>只适用合约订单 |
| data.stpMode | string |  | STP模式（自成交预防）<br/>`none`：不设置STP（默认值）<br/>`cancel_taker`：取消taker单 <br/>`cancel_maker`：取消maker单 <br/>`cancel_both`：两者都取消 |
| data.takeProfit | string |  | 止盈触发价格 |
| data.stopLoss | string |  | 止损触发价格 |
| data.tpTriggerBy | string |  | 止盈触发类型<br/>`market`: 市场价格<br/>`mark`: 标记价格 |
| data.slTriggerBy | string |  | 止损触发类型<br/>`market`: 市场价格<br/>`mark`: 标记价格 |
| data.tpOrderType | string |  | 止盈订单类型<br/>`limit`: 限价单<br/>`market`: 市价单 |
| data.slOrderType | string |  | 止损订单类型<br/>`limit`: 限价单<br/>`market`: 市价单 |
| data.tpLimitPrice | string |  | 止盈限价单执行价格 |
| data.slLimitPrice | string |  | 止损限价单执行价格 |
| data.reduceOnly | string |  | 是否减仓单<br/>`YES`: 是<br/>`NO`: 否<br/>只适用合约订单 |
| data.feeDetail | string[] |  | 手续费明细 |
| data.> feeCoin | string |  | 手续费币种 |
| data.> fee | string |  | 总计手续费 |
| data.delegateType | string |  | 委托类型<br/>`normal` 限价普通<br/>`stop_profit_market` 最优价止盈<br/>`stop_loss_market` 最优价止损<br/>`stop_profit_chase` 止盈追价委托<br/>`stop_loss_chase` 止损追价委托<br/>`trader_delegate` 带单委托<br/>`trader_stop_profit` 带单止盈<br/>`trader_stop_loss` 带单止损<br/>`follower_delegate` 跟单委托<br/>`reduce_offset_delegate` 减仓扎差委托<br/>`market` 最优价普通<br/>`market_risk` 最优价风险处理<br/>`plan_limit` 限价计划委托<br/>`plan_market` 最优价计划委托<br/>`back_contract` 反手<br/>`trader_back_contract` 带单反手<br/>`strategy_grid_positive` 策略-正向网格<br/>`strategy_grid_reverse` 策略-反向网格<br/>`strategy_unlimited` 无限策略<br/>`stop_profit_limit` 限价止盈<br/>`stop_loss_limit` 限价止损<br/>`move_stop_limit` 限价移动止盈止损<br/>`move_stop_market` 最优价移动止盈止损<br/>`position_stop_profit_limit` 限价仓位止盈<br/>`position_stop_profit_market` 最优价仓位止盈<br/>`position_stop_loss_limit` 限价仓位止损<br/>`position_stop_loss_market` 最优价仓位止损<br/>`tracking_plan_limit` 限价追踪委托<br/>`tracking_plan_market` 最优价追踪委托<br/>`delivery_close_long` 多头交割<br/>`delivery_close_short` 空头交割<br/>`liquidation` 爆仓清算<br/>`strategy_dca_positive` DCA策略-正向<br/>`strategy_dca_reverse` DCA策略-反向<br/>`spot_trace_trader_buy` 现货带单买<br/>`spot_trace_follower_buy` 现货跟单买<br/>`spot_trace_trader_sell` 现货带单卖<br/>`spot_trace_follower_sell` 现货跟单卖<br/>`strategy_oco_limit` 策略-OCO限价单<br/>`strategy_oco_trigger` 策略-OCO触发单<br/>`modify_limit_order` 限价修改<br/>`strategy_regular_buy` 策略-定投策略买<br/>`strategy_grid_middle` 策略-中性网格<br/>`strategy_cta_positive` CTA策略-正向<br/>`strategy_cta_reverse` CTA策略-反向<br/>`strategy_tpsl_limit` 现货止盈止损限价单<br/>`strategy_tpsl_market` 现货止盈止损市价单<br/>`strategy_contract_ai` 合约AI智投<br/>`strategy_trace_market` 追踪委托市价单<br/>`strategy_trace_limit` 追踪委托限价单<br/>`strategy_portfolio_buy` 策略-囤币宝买<br/>`strategy_portfolio_sell` 策略-囤币宝卖<br/>`strategy_tradingview` TRADINGVIEW信号接入策略<br/>`sigan_trace` 信号跟单<br/>`mmr_stop_loss_market` 最优价MMR止损<br/>`bbo_opponent1` BBO-对手价1<br/>`bbo_opponent5` BBO-对手价5<br/>`bbo_companion1` BBO-同向价1<br/>`bbo_companion5` BBO-同向价5<br/>`bbo_opponent1_profit` BBO-对手价1止盈<br/>`bbo_opponent5_profit` BBO-对手价5止盈<br/>`bbo_companion1_profit` BBO-同向价1止盈<br/>`bbo_companion5_profit` BBO-同向价5止盈<br/>`bbo_opponent1_loss` BBO-对手价1止损<br/>`bbo_opponent5_loss` BBO-对手价5止损<br/>`bbo_companion1_loss` BBO-同向价1止损<br/>`bbo_companion5_loss` BBO-同向价5止损<br/>`spot_bbo_opponent1_tpsl` BBO-对手价1止盈止损<br/>`spot_bbo_opponent5_tpsl` BBO-对手价5止盈止损<br/>`spot_bbo_companion1_tpsl` BBO-同向价1止盈止损<br/>`spot_bbo_companion5_tpsl` BBO-同向价5止盈止损<br/>`dummy_bbo_profit` BBO-止盈<br/>`dummy_bbo_loss` BBO-止损<br/>`strategy_pre_tpsl_limit` 现货预设止盈止损限价单<br/>`strategy_pre_tpsl_market` 现货预设止盈止损市价单<br/>`future_signal_delegate` 合约喊单跟单限价单<br/>`grant_market` 体验券开仓<br/>`tg_signal_limit` TG信号单<br/>`tg_signal_tp_market` TG信号单止盈<br/>`tg_signal_sl_market` TG信号单止损<br/>`strategy_preset_tpsl_limit` 现货预设计划委托止盈止损限价单<br/>`strategy_preset_tpsl_market` 现货预设计划委托止盈止损市价单<br/>`trader_iceberg_limit` 冰山委托<br/>`trader_time_share_market` 分时委托<br/>`strategy_arbitrage_positive` 资金费套利策略正向<br/>`strategy_arbitrage_reverse` 资金费套利策略反向<br/>`convert_hedging` 闪兑操盘<br/>`off_close` 下架平仓 |
| data.cancelReason | string |  | 撤销原因<br/>`normal_cancel`: 常规取消 <br/>详细枚举可以在 枚举 页面获取 |
| data.execType | string |  | 执行类型<br/>`normal`: 常规成交<br/>`offset`: 轧差订单<br/>`reduce`: 强制减仓单<br/>`liquidation`: 爆仓单<br/>`delivery`: 交割订单 |
| data.createdTime | string |  | 订单创建时间<br/>Unix时间戳，毫秒 |
| data.updatedTime | string |  | 订单更新时间<br/>Unix时间戳，毫秒 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1730369201783,
  "data": {
    "orderId": "111111111111111111",
    "clientOid": "111111111111111111",
    "category": "SPOT",
    "symbol": "ETHUSDT",
    "orderType": "market",
    "side": "buy",
    "price": "0",
    "qty": "0",
    "amount": "100",
    "cumExecQty": "0.0372",
    "cumExecValue": "99.853356",
    "avgPrice": "2684.23",
    "timeInForce": "gtc",
    "orderStatus": "filled",
    "posSide": "",
    "tradeSide": "open",
    "holdMode": "",
    "reduceOnly": "NO",
    "marginMode": "crossed",
    "stpMode": "none",
    "takeProfit": "",
    "stopLoss": "",
    "tpTriggerBy": "",
    "slTriggerBy": "",
    "tpOrderType": "",
    "slOrderType": "",
    "tpLimitPrice": "",
    "slLimitPrice": "",
    "feeDetail": [
      {
        "feeCoin": "ETH",
        "fee": "0.00000744"
      }
    ],
    "delegateType": "normal",
    "cancelReason": "",
    "execType": "",
    "createdTime": "1730295766596",
    "updatedTime": "1730295766691"
  }
}
```

## 获取当前委托

`GET /api/v3/trade/unfilled-orders`

查询未成交及部分成交订单。查询已成交订单，请使用【获取历史委托单】接口

**订单持有上限:**
    - **合约:** USDT合约/币本位合约/USDC合约所有交易对加起来一共最多支持400个订单
    - **现货:** 现货/杠杆所有交易对最多支持400订单
- 限频规则: 20次/秒/UID
- 需要统一账户交易只读/读写权限

Operation ID: `utaTradeOrderGetOrderPending`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| category | query | string |  | 产品类型<br/>`SPOT` 现货交易<br/>`MARGIN` 杠杆交易<br/>`USDT-FUTURES` U本位合约<br/>`COIN-FUTURES` 币本位合约<br/>`USDC-FUTURES` USDC合约 |
| symbol | query | string |  | 交易对名称<br/>例如：`BTCUSDT` |
| startTime | query | string |  | 开始时间戳 <br/>Unix时间戳的毫秒数格式，如 1597026383085 |
| endTime | query | string |  | 结束时间戳 <br/>Unix时间戳的毫秒数格式，如 1597026383085 |
| limit | query | string |  | 每页条目数<br/>最大`100`，默认`100` |
| cursor | query | string |  | 分页游标<br/>用于翻页，首次查询不传，查询第二页及后面的数据时，取上一次查询返回的最小orderId，结果会返回小于该值的数据 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.list | string[] |  | 订单列表 |
| data.>orderId | string |  | 订单ID |
| data.>clientOid | string |  | 自定义订单ID |
| data.>category | string |  | 产品类型<br/>`SPOT` 现货交易<br/>`MARGIN` 杠杆交易<br/>`USDT-FUTURES` U本位合约<br/>`COIN-FUTURES` 币本位合约<br/>`USDC-FUTURES` USDC合约 |
| data.>symbol | string |  | 交易对名称 <br/>例如：`BTCUSDT` |
| data.>price | string |  | 委托价格 |
| data.>qty | string |  | 委托数量 <br/>_单位为base coin_ |
| data.>amount | string |  | 委托金额 <br/>_单位为quote coin_ <br/>适用于现货和杠杆 |
| data.>orderType | string |  | 订单类型 <br/>`limit`: 限价 <br/>`market`: 市价 |
| data.>cumExecQty | string |  | 累计成交量<br/>_单位为base coin_ |
| data.>cumExecValue | string |  | 累计成交额<br/>_单位为quote coin_ |
| data.>avgPrice | string |  | 成交均价 |
| data.>orderStatus | string |  | 订单状态<br/>`live`: 订单已创建<br/>`new`: 订单已进入撮合<br/>`partially_filled`: 部分成交 |
| data.>side | string |  | 订单方向<br/>`buy`: 买<br/>`sell`: 卖 |
| data.>timeInForce | string |  | 订单有效期<br/>`ioc`: 无法立即成交的部分就撤销<br/>`fok`: 无法全部立即成交就撤<br/>`gtc`: 普通订单, 订单会一直有效，直到被成交或者取消<br/>`post_only`: 只做maker<br/>`rpi`: 零售价格优化订单 |
| data.>posSide | string |  | 交易方向<br/>`long`: 开<br/>`short`: 平 |
| data.>holdMode | string |  | 持仓模式<br/>`one_way_mode`: 单向持仓<br/>`hedge_mode`: 双向持仓 |
| data.>delegateType | string |  | 委托类型<br/>`normal`: 限价普通<br/>`stop_profit_market`: 最优价止盈<br/>`stop_loss_market`: 最优价止损<br/>`stop_profit_chase`: 止盈追价委托<br/>`stop_loss_chase`: 止损追价委托<br/>`trader_delegate`: 带单委托<br/>`trader_stop_profit`: 带单止盈<br/>`trader_stop_loss`: 带单止损<br/>`follower_delegate`: 跟单委托<br/>`reduce_offset_delegate`: 减仓扎差委托<br/>`market`: 最优价普通<br/>`market_risk`: 最优价风险处理<br/>`plan_limit`: 限价计划委托<br/>`plan_market`: 最优价计划委托<br/>`back_contract`: 反手<br/>`trader_back_contract`: 带单反手<br/>`strategy_grid_positive`: 策略-正向网格<br/>`strategy_grid_reverse`: 策略-反向网格<br/>`strategy_unlimited`: 无限策略<br/>`stop_profit_limit`: 限价止盈<br/>`stop_loss_limit`: 限价止损<br/>`move_stop_limit`: 限价移动止盈止损<br/>`move_stop_market`: 最优价移动止盈止损<br/>`position_stop_profit_limit`: 限价仓位止盈<br/>`position_stop_profit_market`: 最优价仓位止盈<br/>`position_stop_loss_limit`: 限价仓位止损<br/>`position_stop_loss_market`: 最优价仓位止损<br/>`tracking_plan_limit`: 限价追踪委托<br/>`tracking_plan_market`: 最优价追踪委托<br/>`delivery_close_long`: 多头交割<br/>`delivery_close_short`: 空头交割<br/>`liquidation`: 爆仓清算<br/>`strategy_dca_positive`: DCA策略-正向<br/>`strategy_dca_reverse`: DCA策略-反向<br/>`spot_trace_trader_buy`: 现货带单买<br/>`spot_trace_follower_buy`: 现货跟单买<br/>`spot_trace_trader_sell`: 现货带单卖<br/>`spot_trace_follower_sell`: 现货跟单卖<br/>`strategy_oco_limit`: 策略-OCO限价单<br/>`strategy_oco_trigger`: 策略-OCO触发单<br/>`modify_limit_order`: 限价修改<br/>`strategy_regular_buy`: 策略-定投策略买<br/>`strategy_grid_middle`: 策略-中性网格<br/>`strategy_cta_positive`: CTA策略-正向<br/>`strategy_cta_reverse`: CTA策略-反向<br/>`strategy_tpsl_limit`: 现货止盈止损限价单<br/>`strategy_tpsl_market`: 现货止盈止损市价单<br/>`strategy_contract_ai`: 合约AI智投<br/>`strategy_trace_market`: 追踪委托市价单<br/>`strategy_trace_limit`: 追踪委托限价单<br/>`strategy_portfolio_buy`: 策略-囤币宝买<br/>`strategy_portfolio_sell`: 策略-囤币宝卖<br/>`strategy_tradingview`: TRADINGVIEW信号接入策略<br/>`sigan_trace`: 信号跟单<br/>`mmr_stop_loss_market`: 最优价MMR止损<br/>`bbo_opponent1`: BBO-对手价1<br/>`bbo_opponent5`: BBO-对手价5<br/>`bbo_companion1`: BBO-同向价1<br/>`bbo_companion5`: BBO-同向价5<br/>`bbo_opponent1_profit`: BBO-对手价1止盈<br/>`bbo_opponent5_profit`: BBO-对手价5止盈<br/>`bbo_companion1_profit`: BBO-同向价1止盈<br/>`bbo_companion5_profit`: BBO-同向价5止盈<br/>`bbo_opponent1_loss`: BBO-对手价1止损<br/>`bbo_opponent5_loss`: BBO-对手价5止损<br/>`bbo_companion1_loss`: BBO-同向价1止损<br/>`bbo_companion5_loss`: BBO-同向价5止损<br/>`spot_bbo_opponent1_tpsl`: BBO-对手价1止盈止损<br/>`spot_bbo_opponent5_tpsl`: BBO-对手价5止盈止损<br/>`spot_bbo_companion1_tpsl`: BBO-同向价1止盈止损<br/>`spot_bbo_companion5_tpsl`: BBO-同向价5止盈止损<br/>`dummy_bbo_profit`: BBO-止盈<br/>`dummy_bbo_loss`: BBO-止损<br/>`strategy_pre_tpsl_limit`: 现货预设止盈止损限价单<br/>`strategy_pre_tpsl_market`: 现货预设止盈止损市价单<br/>`future_signal_delegate`: 合约喊单跟单限价单<br/>`grant_market`: 体验券开仓<br/>`tg_signal_limit`: TG信号单<br/>`tg_signal_tp_market`: TG信号单止盈<br/>`tg_signal_sl_market`: TG信号单止损<br/>`strategy_preset_tpsl_limit`: 现货预设计划委托止盈止损限价单<br/>`strategy_preset_tpsl_market`: 现货预设计划委托止盈止损市价单<br/>`trader_iceberg_limit`: 冰山委托<br/>`trader_time_share_market`: 分时委托<br/>`strategy_arbitrage_positive`: 资金费套利策略正向<br/>`strategy_arbitrage_reverse`: 资金费套利策略反向<br/>`liquidation_take_over_long`: 爆仓接管多仓<br/>`liquidation_take_over_short`: 爆仓接管空仓<br/>`convert_hedging`: 闪兑操盘<br/>`off_close`: 下架平仓 |
| data.>marginMode | string |  | 保证金模式<br/>`crossed`: 全仓<br/>`isolated`: 逐仓<br/>只适用合约订单 |
| data.>stpMode | string |  | [STP模式（自成交预防）](https://www.bitget.com/zh-CN/support/articles/12560603812732)<br/>`none`：不设置STP（默认值）<br/>`cancel_taker`：取消taker单 <br/>`cancel_maker`：取消maker单 <br/>`cancel_both`：两者都取消 |
| data.>takeProfit | string |  | 止盈触发价格 |
| data.>stopLoss | string |  | 止损触发价格 |
| data.>tpTriggerBy | string |  | 止盈触发类型<br/>`market`: 市场价格<br/>`mark`: 标记价格 |
| data.>slTriggerBy | string |  | 止损触发类型<br/>`market`: 市场价格<br/>`mark`: 标记价格 |
| data.>tpOrderType | string |  | 止盈订单类型<br/>`limit`: 限价单<br/>`market`: 市价单 |
| data.>slOrderType | string |  | 止损订单类型<br/>`limit`: 限价单<br/>`market`: 市价单 |
| data.>tpLimitPrice | string |  | 止盈限价单执行价格 |
| data.>slLimitPrice | string |  | 止损限价单执行价格 |
| data.>reduceOnly | string |  | 是否减仓单<br/>`YES`: 是<br/>`NO`: 否 |
| data.>feeDetail | string[] |  | 手续费明细 |
| data.>> feeCoin | string |  | 手续费币种 |
| data.>> fee | string |  | 总计手续费 |
| data.>channelCode | string |  | 渠道标识<br/>用于经纪商用户返佣核对 |
| data.>createdTime | string |  | 订单创建时间<br/>Unix毫秒时间戳，例如1690196141868 |
| data.>updatedTime | string |  | 订单更新时间<br/>Unix毫秒时间戳，例如1690196141868 |
| data.cursor | string |  | 翻页游标（取当前页最小 orderId，传入查询更早的订单） |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1730186730084,
  "data": {
    "list": [
      {
        "orderId": "111111111111111111",
        "clientOid": "111111111111111111",
        "category": "USDT-FUTURES",
        "symbol": "BTCUSDT",
        "orderType": "limit",
        "side": "buy",
        "price": "45000",
        "qty": "0.01",
        "amount": "0",
        "cumExecQty": "0",
        "cumExecValue": "0",
        "avgPrice": "0",
        "timeInForce": "gtc",
        "orderStatus": "live",
        "posSide": "long",
        "holdMode": "hedge_mode",
        "delegateType": "normal",
        "reduceOnly": "NO",
        "marginMode": "crossed",
        "stpMode": "none",
        "takeProfit": "",
        "stopLoss": "",
        "tpTriggerBy": "",
        "slTriggerBy": "",
        "tpOrderType": "",
        "slOrderType": "",
        "tpLimitPrice": "",
        "slLimitPrice": "",
        "feeDetail": [
          {
            "feeCoin": null,
            "fee": null
          }
        ],
        "channelCode": "",
        "createdTime": "1730186725663",
        "updatedTime": "1730186725691"
      }
    ],
    "cursor": "1235058132196622336"
  }
}
```

## 获取历史委托

`GET /api/v3/trade/history-orders`

- [通过API下单的历史订单记录中，委托订单为cancelled状态的记录，仅支持保留2小时，非API下单的委托订单数据不受影响](https://www.bitget.com/zh-CN/support/articles/12560603823188)；

- 可以通过网页端下载[统一账户全部时间历史委托](https://www.bitget.com/zh-CN/trade-asset-order/uta-order-history)以及[经典账户全部时间历史委托](https://www.bitget.com/zh-CN/transac?tab=1)(最早可导出2018年1月1日的数据)

- **接口查询时间范围**

  每次查询只支持查询90天内的任意30天数据
- 限频规则: 20次/秒/UID
- 需要统一账户交易只读/读写权限

Operation ID: `utaTradeOrderGetOrderHistory`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| category | query | string | 是 | 产品类型<br/>`SPOT` 现货交易<br/>`MARGIN` 杠杆交易<br/>`USDT-FUTURES` USDT合约<br/>`COIN-FUTURES` 币本位合约<br/>`USDC-FUTURES` USDC合约 |
| symbol | query | string |  | 交易对名称<br/>例如：`BTCUSDT` |
| startTime | query | string |  | 开始时间戳 <br/>Unix时间戳的毫秒数格式，如 1597026383085<br/>最大查询范围90天 |
| endTime | query | string |  | 结束时间戳 <br/>Unix时间戳的毫秒数格式，如 1597026383085<br/>`startTime`和`endTime`间隔不超过30天 |
| limit | query | string |  | 每页条目数<br/>最大`100`，默认`100` |
| cursor | query | string |  | 游标ID<br/>用于翻页，首次查询不传，查询第二页及后面的数据时，取上一次查询返回的最小orderId，结果会返回小于该值的数据 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.list | object[] |  | 订单列表 |
| data.list[].orderId | string |  | 订单ID |
| data.list[].clientOid | string |  | 自定义订单ID |
| data.list[].category | string |  | 产品类型<br/>`SPOT` 现货交易<br/>`MARGIN` 杠杆交易<br/>`USDT-FUTURES` U本位合约<br/>`COIN-FUTURES` 币本位合约<br/>`USDC-FUTURES` USDC合约 |
| data.list[].symbol | string |  | 交易对名称<br/>例如：`BTCUSDT` |
| data.list[].price | string |  | 委托价格 |
| data.list[].qty | string |  | 委托数量 <br/>_单位为base coin_ |
| data.list[].amount | string |  | 委托金额<br/>_单位为quote coin_ <br/>适用于现货和杠杆 |
| data.list[].orderType | string |  | 交易类型 <br/>`limit`: 限价 <br/>`market`: 市价 |
| data.list[].cumExecQty | string |  | 累计成交数量 <br/>_单位为base coin_ |
| data.list[].cumExecValue | string |  | 累计成交额<br/>_单位为quote coin_ |
| data.list[].avgPrice | string |  | 成交均价 |
| data.list[].orderStatus | string |  | 订单状态<br/>`live`: 订单已创建<br/>`new`: 订单已进入撮合<br/>`partially_filled`: 部分成交<br/>`filled`: 全部成交<br/>`cancelled`: 已撤销 |
| data.list[].side | string |  | 开单方向<br/>`buy`: 买<br/>`sell`: 卖 |
| data.list[].timeInForce | string |  | 订单有效期<br/>`ioc`: 无法立即成交的部分就撤销<br/>`fok`: 无法全部立即成交就撤<br/>`gtc`: 普通订单, 订单会一直有效，直到被成交或者取消<br/>`post_only`: 只做maker<br/>`rpi`: 零售价格优化订单 |
| data.list[].posSide | string |  | 仓位方向<br/>`long`: 双向持仓多头<br/>`short`: 双向持仓空头 |
| data.list[].holdMode | string |  | 持仓模式<br/>`one_way_mode`: 单向持仓<br/>`hedge_mode`: 双向持仓 |
| data.list[].delegateType | string |  | 委托类型<br/>`normal`: 限价普通<br/>`stop_profit_market`: 最优价止盈<br/>`stop_loss_market`: 最优价止损<br/>`stop_profit_chase`: 止盈追价委托<br/>`stop_loss_chase`: 止损追价委托<br/>`trader_delegate`: 带单委托<br/>`trader_stop_profit`: 带单止盈<br/>`trader_stop_loss`: 带单止损<br/>`follower_delegate`: 跟单委托<br/>`reduce_offset_delegate`: 减仓扎差委托<br/>`market`: 最优价普通<br/>`market_risk`: 最优价风险处理<br/>`plan_limit`: 限价计划委托<br/>`plan_market`: 最优价计划委托<br/>`back_contract`: 反手<br/>`trader_back_contract`: 带单反手<br/>`strategy_grid_positive`: 策略-正向网格<br/>`strategy_grid_reverse`: 策略-反向网格<br/>`strategy_unlimited`: 无限策略<br/>`stop_profit_limit`: 限价止盈<br/>`stop_loss_limit`: 限价止损<br/>`move_stop_limit`: 限价移动止盈止损<br/>`move_stop_market`: 最优价移动止盈止损<br/>`position_stop_profit_limit`: 限价仓位止盈<br/>`position_stop_profit_market`: 最优价仓位止盈<br/>`position_stop_loss_limit`: 限价仓位止损<br/>`position_stop_loss_market`: 最优价仓位止损<br/>`tracking_plan_limit`: 限价追踪委托<br/>`tracking_plan_market`: 最优价追踪委托<br/>`delivery_close_long`: 多头交割<br/>`delivery_close_short`: 空头交割<br/>`liquidation`: 爆仓清算<br/>`strategy_dca_positive`: DCA策略-正向<br/>`strategy_dca_reverse`: DCA策略-反向<br/>`spot_trace_trader_buy`: 现货带单买<br/>`spot_trace_follower_buy`: 现货跟单买<br/>`spot_trace_trader_sell`: 现货带单卖<br/>`spot_trace_follower_sell`: 现货跟单卖<br/>`strategy_oco_limit`: 策略-OCO限价单<br/>`strategy_oco_trigger`: 策略-OCO触发单<br/>`modify_limit_order`: 限价修改<br/>`strategy_regular_buy`: 策略-定投策略买<br/>`strategy_grid_middle`: 策略-中性网格<br/>`strategy_cta_positive`: CTA策略-正向<br/>`strategy_cta_reverse`: CTA策略-反向<br/>`strategy_tpsl_limit`: 现货止盈止损限价单<br/>`strategy_tpsl_market`: 现货止盈止损市价单<br/>`strategy_contract_ai`: 合约AI智投<br/>`strategy_trace_market`: 追踪委托市价单<br/>`strategy_trace_limit`: 追踪委托限价单<br/>`strategy_portfolio_buy`: 策略-囤币宝买<br/>`strategy_portfolio_sell`: 策略-囤币宝卖<br/>`strategy_tradingview`: TRADINGVIEW信号接入策略<br/>`sigan_trace`: 信号跟单<br/>`mmr_stop_loss_market`: 最优价MMR止损<br/>`bbo_opponent1`: BBO-对手价1<br/>`bbo_opponent5`: BBO-对手价5<br/>`bbo_companion1`: BBO-同向价1<br/>`bbo_companion5`: BBO-同向价5<br/>`bbo_opponent1_profit`: BBO-对手价1止盈<br/>`bbo_opponent5_profit`: BBO-对手价5止盈<br/>`bbo_companion1_profit`: BBO-同向价1止盈<br/>`bbo_companion5_profit`: BBO-同向价5止盈<br/>`bbo_opponent1_loss`: BBO-对手价1止损<br/>`bbo_opponent5_loss`: BBO-对手价5止损<br/>`bbo_companion1_loss`: BBO-同向价1止损<br/>`bbo_companion5_loss`: BBO-同向价5止损<br/>`spot_bbo_opponent1_tpsl`: BBO-对手价1止盈止损<br/>`spot_bbo_opponent5_tpsl`: BBO-对手价5止盈止损<br/>`spot_bbo_companion1_tpsl`: BBO-同向价1止盈止损<br/>`spot_bbo_companion5_tpsl`: BBO-同向价5止盈止损<br/>`dummy_bbo_profit`: BBO-止盈<br/>`dummy_bbo_loss`: BBO-止损<br/>`strategy_pre_tpsl_limit`: 现货预设止盈止损限价单<br/>`strategy_pre_tpsl_market`: 现货预设止盈止损市价单<br/>`future_signal_delegate`: 合约喊单跟单限价单<br/>`grant_market`: 体验券开仓<br/>`tg_signal_limit`: TG信号单<br/>`tg_signal_tp_market`: TG信号单止盈<br/>`tg_signal_sl_market`: TG信号单止损<br/>`strategy_preset_tpsl_limit`: 现货预设计划委托止盈止损限价单<br/>`strategy_preset_tpsl_market`: 现货预设计划委托止盈止损市价单<br/>`trader_iceberg_limit`: 冰山委托<br/>`trader_time_share_market`: 分时委托<br/>`strategy_arbitrage_positive`: 资金费套利策略正向<br/>`strategy_arbitrage_reverse`: 资金费套利策略反向<br/>`liquidation_take_over_long`: 爆仓接管多仓<br/>`liquidation_take_over_short`: 爆仓接管空仓<br/>`convert_hedging`: 闪兑操盘<br/>`off_close`: 下架平仓 |
| data.list[].reduceOnly | string |  | 是否减仓单<br/>`YES`: 是<br/>`NO`: 否 |
| data.list[].feeDetail | object[] |  | 手续费明细 |
| data.list[].feeDetail[].feeCoin | string |  | 手续费币种 |
| data.list[].feeDetail[].fee | string |  | 手续费 |
| data.list[].cancelReason | string |  | 撤销原因<br/>`normal_cancel`: 常规撤销 |
| data.list[].execType | string |  | 执行类型<br/>`normal`: 正常订单<br/>`offset`: 轧差订单<br/>`reduce`: 强制减仓单<br/>`liquidation`: 爆仓单<br/>`delivery`: 交割订单 |
| data.list[].marginMode | string |  | 保证金模式<br/>`crossed`: 全仓<br/>`isolated`: 逐仓<br/>只适用合约订单 |
| data.list[].stpMode | string |  | [STP模式（自成交预防）](https://www.bitget.com/zh-CN/support/articles/12560603812732)<br/>`none`：不设置STP（默认值）<br/>`cancel_taker`：取消taker单 <br/>`cancel_maker`：取消maker单 <br/>`cancel_both`：两者都取消 |
| data.list[].takeProfit | string |  | 止盈触发价格 |
| data.list[].stopLoss | string |  | 止损触发价格 |
| data.list[].tpTriggerBy | string |  | 止盈触发类型<br/>`market`: 市场价格<br/>`mark`: 标记价格 |
| data.list[].slTriggerBy | string |  | 止损触发类型<br/>`market`: 市场价格<br/>`mark`: 标记价格 |
| data.list[].tpOrderType | string |  | 止盈订单类型<br/>`limit`: 限价单<br/>`market`: 市价单 |
| data.list[].slOrderType | string |  | 止损订单类型<br/>`limit`: 限价单<br/>`market`: 市价单 |
| data.list[].tpLimitPrice | string |  | 止盈限价单执行价格 |
| data.list[].slLimitPrice | string |  | 止损限价单执行价格 |
| data.list[].channelCode | string |  | 渠道标识<br/>用于经纪商用户返佣核对 |
| data.list[].createdTime | string |  | 创建时间<br/>Unix毫秒时间戳 |
| data.list[].updatedTime | string |  | 更新时间<br/>Unix毫秒时间戳 |
| data.cursor | string |  | 分页游标 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1730186348272,
  "data": {
    "list": [
      {
        "orderId": "111111111111111111",
        "clientOid": "111111111111111111",
        "category": "USDT-FUTURES",
        "symbol": "BTCUSDT",
        "orderType": "limit",
        "side": "sell",
        "price": "49534.4",
        "qty": "0.429",
        "amount": "0",
        "cumExecQty": "0.429",
        "cumExecValue": "21250.2929",
        "avgPrice": "49534.4",
        "timeInForce": "gtc",
        "orderStatus": "filled",
        "posSide": "long",
        "holdMode": "hedge_mode",
        "delegateType": "normal",
        "reduceOnly": "NO",
        "marginMode": "crossed",
        "stpMode": "none",
        "takeProfit": "",
        "stopLoss": "",
        "tpTriggerBy": "",
        "slTriggerBy": "",
        "tpOrderType": "",
        "slOrderType": "",
        "tpLimitPrice": "",
        "slLimitPrice": "",
        "feeDetail": [
          {
            "feeCoin": "USDT",
            "fee": "4.2500586"
          }
        ],
        "cancelReason": "normal_cancel",
        "execType": "liquidation",
        "channelCode": "",
        "createdTime": "1730181468493",
        "updatedTime": "1730181468493"
      }
    ],
    "cursor": "1233319323918499840"
  }
}
```

## 获取成交明细

`GET /api/v3/trade/fills`

获取用户最近90天内委托单成交明细

**查询时间范围**

  每次查询只支持查询90天内的30天数据
- 限频规则: 20次/秒/UID
- 需要统一账户交易只读/读写权限

Operation ID: `utaTradeOrderGetOrderFills`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| category | query | string |  | 产品类型<br/>`SPOT` 现货交易<br/>`MARGIN` 杠杆交易<br/>`USDT-FUTURES` USDT合约<br/>`COIN-FUTURES` 币本位合约<br/>`USDC-FUTURES` USDC合约 |
| orderId | query | string |  | 订单ID |
| startTime | query | string |  | 开始时间戳 <br/>Unix时间戳的毫秒数格式，如 1597026383085<br/>最大查询范围90天 |
| endTime | query | string |  | 结束时间戳 <br/>Unix时间戳的毫秒数格式，如 1597026383085<br/>`startTime`和`endTime`间隔不超过30天 |
| limit | query | string |  | 查询条数<br/>最大`100`，默认`100` |
| cursor | query | string |  | 分页游标<br/>用于翻页，首次查询不传，查询第二页及后面的数据时，取上一次查询返回cursor |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.list | object[] |  | 成交明细集合 |
| data.list[].execId | string |  | 成交ID |
| data.list[].execLinkId | string |  | 成交关联ID |
| data.list[].orderId | string |  | 订单ID |
| data.list[].clientOid | string |  | 自定义订单ID |
| data.list[].category | string |  | 产品类型<br/>`SPOT` 现货交易<br/>`MARGIN` 杠杆交易<br/>`USDT-FUTURES` U本位合约<br/>`COIN-FUTURES` 币本位合约<br/>`USDC-FUTURES` USDC合约 |
| data.list[].symbol | string |  | 交易对名称 |
| data.list[].orderType | string |  | 订单类型 <br/>`limit` 限价单 <br/>`market` 市价单 |
| data.list[].execPrice | string |  | 成交价格 |
| data.list[].execQty | string |  | 交易币成交数量<br/>_单位为base coin_ |
| data.list[].execValue | string |  | 计价币交易额<br/>_单位为quote coin_ |
| data.list[].feeDetail | object[] |  | 手续费明细 |
| data.list[].feeDetail[].feeCoin | string |  | 手续费币种 |
| data.list[].feeDetail[].fee | string |  | 手续费 |
| data.list[].side | string |  | 成交类型<br/>`buy` 买<br/>`sell` 卖 |
| data.list[].tradeScope | string |  | 交易方标识<br/>`taker`: Taker<br/>`maker`: Maker |
| data.list[].tradeSide | string |  | 交易方向 <br/>`open`: 开 <br/>`close` : 平     <br/>详细枚举可以在 枚举 页面获取 |
| data.list[].createdTime | string |  | 订单创建时间<br/>Unix毫秒时间戳，例如1690196141868 |
| data.list[].updatedTime | string |  | 订单更新时间<br/>Unix毫秒时间戳，例如1690196141868 |
| data.list[].execPnl | string |  | 成交盈亏 |
| data.list[].isRPI | string |  | 是否为RPI类型成交<br/>`yes` 是<br/>`no` 否 |
| data.cursor | string |  | 分页游标 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1750142995229,
  "data": {
    "list": [
      {
        "execId": "131111111111111111",
        "execLinkId": "131111111111111111",
        "orderId": "131111111111111111",
        "clientOid": "131111111111111111",
        "category": "USDT-FUTURES",
        "symbol": "BTCUSDT",
        "orderType": "market",
        "side": "sell",
        "tradeSide": "open",
        "execPrice": "106950.1",
        "execQty": "0.01",
        "execValue": "1069.501",
        "tradeScope": "taker",
        "feeDetail": [
          {
            "feeCoin": "USDT",
            "fee": "0.6417006"
          }
        ],
        "createdTime": "1750141421721",
        "updatedTime": "1750141421728",
        "execPnl": "-0.002",
        "isRPI": "no"
      }
    ],
    "cursor": "131111111111111111"
  }
}
```

## 创建Reality股票订单

`POST /api/v3/trade/place-reality-order`

对 Reality 股票交易对进行限价或市价下单。<br/>该接口仅对白名单 UID 开放，如有需要请联系BD。
- 限频规则: 10次/秒/UID
- 需要统一账户交易权限

Operation ID: `utaTradeOrderPlaceRealityOrder`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| category | string |  | 交易类型<br/>`SPOT` 现货交易<br/>`MARGIN` 杠杆交易<br/>默认值：`SPOT` |
| symbol | string | 是 | 交易对名称<br/>如 `rAAPLUSDT`<br/>该接口仅支持 Reality 股票交易对 |
| side | string | 是 | 方向<br/>`buy` 买<br/>`sell` 卖 |
| orderType | string | 是 | 订单类型<br/>`limit` 限价单<br/>`market` 市价单 |
| qty | string | 是 | 下单数量<br/>市价买单，单位为 **quote coin**<br/>限价及市价卖单，单位为 **base coin** |
| price | string |  | 委托价格<br/>`orderType=limit` 时必传 |
| clientOid | string |  | 自定义订单 ID |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.orderId | string |  | 系统订单 ID |
| data.clientOid | string |  | 客户端自定义订单 ID，未传则返回空字符串 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695806875837,
  "data": {
    "orderId": "121211212122",
    "clientOid": "myOrder001"
  }
}
```

## 撤销Reality股票订单

`POST /api/v3/trade/cancel-reality-order`

撤销未成交或部分成交的 Reality 股票订单。<br/>该接口仅对白名单 UID 开放，如有需要请联系BD。
- 限频规则: 10次/秒/UID
- 需要统一账户交易权限

Operation ID: `utaTradeOrderCancelRealityOrder`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| category | string |  | 交易类型<br/>`SPOT` 现货交易<br/>`MARGIN` 杠杆交易<br/>默认值：`SPOT` |
| symbol | string | 是 | 交易对名称<br/>如 `rAAPLUSDT` |
| orderId | string |  | 系统订单 ID<br/>`orderId` 与 `clientOid` 至少传其一；同时传入时 `orderId` 优先 |
| clientOid | string |  | 自定义订单 ID<br/>`orderId` 与 `clientOid` 至少传其一；同时传入时 `orderId` 优先 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.orderId | string |  | 系统订单 ID |
| data.clientOid | string |  | 客户端自定义订单 ID，未传则返回空字符串 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695806875837,
  "data": {
    "orderId": "121211212122",
    "clientOid": "myOrder001"
  }
}
```

## 获取最大可开可用

`POST /api/v3/account/max-open-available`

限频规则: 5次/秒/UID

获取最大可开可用

- 限频规则: 5次/秒/UID

- 需要统一账户交易只读权限

Operation ID: `utaTradePositionGetMaxOpenAvailable`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| category | string | 是 | 产品类型<br><br>`SPOT` 现货交易<br><br>`MARGIN` 杠杆交易<br><br>`USDT-FUTURES` USDT合约<br><br>`COIN-FUTURES` 币本位合约<br><br>`USDC-FUTURES` USDC合约 |
| symbol | string | 是 | 交易对名称<br><br>例如：`BTCUSDT` |
| orderType | string | 是 | 订单类型<br><br>`limit`: 限价单<br><br>`market`: 市价单 |
| side | string | 是 | 交易方向 `buy` 买 `sell` 卖 |
| price | string |  | 下单价格<br><br>订单类型为限价单`limit`时，该字段必填 |
| size | string |  | 下单数量 基础币 |
| autoBorrow | string |  | 自动借币开关<br/>`yes` 开启<br/>`no` 关闭（默认）<br/>仅用于现货下单。开启后，若得到币不支持借贷、消耗币支持借贷，则在消耗币可用余额不足时，系统将自动借入消耗币，补足委托所需金额。 |
| marginMode | string |  | 保证金模式<br/>`crossed` 全仓<br/>`isolated` 逐仓<br/>不传默认为`crossed`<br/>逐仓模式下，`available`计算会剔除合约体验金 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.available | string |  | 可用 <br><br> 现货/杠杆 `side=buy` 时代表计价币数量 `side=sell`时代表基础币数量 <br><br> 合约代表计价币数量 |
| data.maxOpen | string |  | 最大可开  <br><br>`side=buy` 时代表计价币数量 `side=sell`时代表基础币数量  <br><br>杠杆有值；现货在开启自动借币（`autoBorrow`）时也有值 |
| data.buyOpenCost | string |  | 买入时以输入的`size`计算开仓所需的计价币数量 <br><br>只有合约有值 |
| data.sellOpenCost | string |  | 卖出时以输入的`size`计算开仓所需的计价币数量 <br><br>只有合约有值 |
| data.maxBuyOpen | string |  | 买入最大可开 以账户余额计算的基础币数量<br><br> 只有合约有值 |
| data.maxSellOpen | string |  | 卖出最大可开 以账户余额计算的基础币数量<br><br> 只有合约有值 |
| data.maxBuyAvailable | string |  | 最大可买 |
| data.maxSellAvailable | string |  | 最大可卖 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1741851607871,
  "data": {
    "available": "52.008255",
    "maxOpen": "",
    "buyOpenCost": "",
    "sellOpenCost": "",
    "maxBuyOpen": "",
    "maxSellOpen": "",
    "maxBuyAvailable": "",
    "maxSellAvailable": ""
  }
}
```

## 一键平仓

`POST /api/v3/trade/close-positions`

限频规则: 5次/秒/UID

支持把当前仓位按产品类型或者持仓方向以市价进行平仓，可能会有滑点


**API Broker返佣标识**:

  需在HTTP Header请求头中添加如下代码块

  > "X-CHANNEL-API-CODE":"your-channel-api-code"

- 限频规则: 5次/秒/UID

- 需要统一账户交易读写权限

Operation ID: `utaTradePositionCloseAllPositions`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| category | string | 是 | 产品类型<br><br>`USDT-FUTURES` U本位合约<br><br>`COIN-FUTURES` 币本位合约<br><br>`USDC-FUTURES` USDC合约 |
| symbol | string |  | 交易对名称<br><br>例如：`BTCUSDT`<br><br>如果不填此参数，会平掉对应的产品类型下的所有仓位 |
| posSide | string |  | 持仓方向 <br><br>`long` 多仓<br><br>`short` 空仓<br><br> 如填此参数 则只会平对应方向下仓位 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.list | string[] |  | 列表 |
| data.>orderId | string |  | 订单ID |
| data.>clientOid | string |  | 自定义订单ID |
| data.>msg | string |  | 失败原因 |
| data.>code | string |  | 错误码 |

```json
{
  "code": "00000",
  "data": {
    "list": [
      {
        "orderId": "111111111111111111",
        "clientOid": "111111111111111111",
        "code": "24056",
        "msg": "notExisted"
      }
    ]
  },
  "msg": "success",
  "requestTime": 1627293504612
}
```

## 仓位转移

`POST /api/v3/account/move-positions`

限频规则: 1次/秒/UID

支持母子账户互转及子账户间移仓：

1. 母账户向子账户移仓

2. 子账户向母账户移仓

3. 子账户向子账户移仓（需隶属于相同母账户）

该功能仅对白名单用户开放，仅能通过母账户的API Key调用，必须是同一母账户体系，当前仅支持USDT和USDC合约，仅支持全仓模式。

移仓生成的交易不会出现在公有行情的成交中，不产生手续费。

整点前后5分钟不支持移仓，源账户mmr>=80%不支持移仓。移仓前会撤销源账户和目标账户对应合约的订单，移仓价格默认且仅支持标记价格。

用户每日最多可触发**100**次移仓请求，调用成功算1次，每次移仓请求需间隔**30秒**，每个移仓请求最多支持10个仓位。

移仓之后的持仓模式和杠杆倍数以目标账户原先的设置为准。

- 限频规则: 1次/秒/UID

- **业务限制: 100次/天/UID，请求间隔最少30秒**

- 需要统一账户交易读写权限

Operation ID: `utaTradePositionMovePositions`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| fromUid | string | 是 | 移仓发起账户UID <br><br>转出仓位的账户 <br><br>`fromUid`及`toUid`需隶属于同一母子账户体系 |
| toUid | string | 是 | 移仓目标账户UID <br><br>接收仓位的账户 <br><br>`fromUid`及`toUid`需隶属于同一母子账户体系 |
| category | string | 是 | 产品类型 <br><br>`USDT-FUTURES` USDT合约 <br><br>`COIN-FUTURES` 币本位合约 <br><br>`USDC-FUTURES` USDC合约 |
| positionList | string[] | 是 | 仓位列表 <br><br>单次请求最多10个仓位 |
| >symbol | string | 是 | 交易对名称 <br><br>例如：`BTCUSDT` |
| >side | string | 是 | 下单方向<br><br>`buy`/`sell` <br><br>单向模式/双向模式处理逻辑一致 <br><br>持有多仓时，需传入`side=sell`进行减仓 <br><br>持有空仓时，需传入`side=buy`进行减仓 |
| >qty | string | 是 | 转移数量 <br><br>需满足最小数量精度要求 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.closePosition | string[] |  | 发起账户仓位列表 |
| data.>orderId | string |  | 目标订单ID |
| data.>clientOid | string |  | 目标订单自定义ID |
| data.>code | string |  | 错误码 <br><br>开仓产生错误时返回 |
| data.>msg | string |  | 错误信息 <br><br>开仓产生错误时返回 |
| data.openPosition | string[] |  | 目标账户仓位结果列表 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695806875837,
  "data": {
    "closePosition": [
      {
        "orderId": "121211212122",
        "clientOid": "131311313133",
        "code": "",
        "msg": ""
      }
    ],
    "openPosition": [
      {
        "orderId": "121211212123",
        "clientOid": "131311313134",
        "code": "",
        "msg": ""
      }
    ]
  }
}
```

## 获取移仓历史

`GET /api/v3/account/move-position-history`

限频规则: 5次/秒/UID

查询移仓历史记录。仅支持母账户调用。

**查询时间范围**

  如不传`endTime`，默认查询最近30天数据。最大支持的时间跨度为90天。

- 限频规则: 5次/秒/UID

- 需要统一账户交易只读/读写权限

Operation ID: `utaTradePositionGetMovePositionHistory`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| category | query | string | 是 | 产品类型 <br><br>`USDT-FUTURES` USDT合约 <br><br>`COIN-FUTURES` 币本位合约 <br><br>`USDC-FUTURES` USDC合约 |
| symbol | query | string |  | 交易对名称 <br><br>例如：`BTCUSDT` |
| startTime | query | string |  | 开始时间戳 <br><br>Unix时间戳的毫秒数格式，如 `1597026383085` |
| endTime | query | string |  | 结束时间戳 <br><br>Unix时间戳的毫秒数格式，如 `1597026383185` <br><br>如不传，默认查询最近30天数据 <br><br>最大支持的时间跨度为90天 |
| cursor | query | string |  | 游标ID <br><br>用于分页。首次不传，后续传上次响应结果 |
| limit | query | string |  | 每页条目数 <br><br>默认值为`100`，最大值为`100` |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.list | string[] |  | 移仓历史列表 |
| data.>category | string |  | 产品类型 <br><br>`USDT-FUTURES` USDT合约 <br><br>`COIN-FUTURES` 币本位合约 <br><br>`USDC-FUTURES` USDC合约 |
| data.>fromUid | string |  | 发起账户UID |
| data.>toUid | string |  | 目标账户UID |
| data.>orderId | string |  | 订单ID |
| data.>openExecId | string |  | 开仓成交ID |
| data.>closeExecId | string |  | 平仓成交ID |
| data.>symbol | string |  | 交易对名称 <br><br>例如：`BTCUSDT` |
| data.>posSide | string |  | 仓位方向 <br><br>`long` 多仓 <br><br>`short` 空仓 |
| data.>qty | string |  | 转移数量 |
| data.>price | string |  | 转移价格 |
| data.>status | string |  | 转移状态 <br><br>`processing` 处理中 <br><br>`completed` 已完成 <br><br>`failed` 失败 |
| data.>createdTime | string |  | 订单创建时间 <br><br>Unix毫秒时间戳 |
| data.>updatedTime | string |  | 订单更新时间 <br><br>Unix毫秒时间戳 |
| data.cursor | string |  | 分页游标 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1730186348272,
  "data": {
    "list": [
      {
        "category": "USDT-FUTURES",
        "fromUid": "111111111",
        "toUid": "222222222",
        "orderId": "121211212122",
        "openExecId": "343434343434",
        "closeExecId": "343434343435",
        "symbol": "BTCUSDT",
        "posSide": "long",
        "qty": "0.5",
        "price": "61000",
        "status": "completed",
        "createdTime": "1730181468493",
        "updatedTime": "1730181468593"
      }
    ],
    "cursor": "1233319323918499840"
  }
}
```

## 获取当前仓位

`GET /api/v3/position/current-position`

限频规则: 20次/秒/UID

以交易对、仓位方向，或者产品类型维度获取实时仓位信息

- 限频规则: 20次/秒/UID

- 需要统一账户管理只读/读写权限

Operation ID: `utaTradePositionGetPosition`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| category | query | string | 是 | 产品类型<br><br>`USDT-FUTURES` USDT合约<br><br>`COIN-FUTURES` 币本位合约<br><br>`USDC-FUTURES` USDC合约 |
| symbol | query | string |  | 交易币对<br><br>例如:`BTCUSDT`<br><br>如果不传symbol，那么将返回对应产品类型的所有仓位 |
| posSide | query | string |  | 仓位方向 <br><br>`long`: 多仓<br><br>`short`: 空仓<br><br>如果传入此参数，那么仅返回对应仓位方向的仓位信息 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.list | string[] |  | 列表 |
| data.>category | string |  | 产品类型 <br><br>`USDT-FUTURES` USDT合约<br><br>`COIN-FUTURES` 币本位合约<br><br>`USDC-FUTURES` USDC合约 |
| data.>symbol | string |  | 币对名称 |
| data.>marginCoin | string |  | 保证金币种 |
| data.>posSide | string |  | 持仓方向 持仓方向<br><br>`long`: 多仓<br><br>`short`:空仓 |
| data.>positionBalance | string |  | 仓位保证金数量 (保证金币种)<br><br>逐仓模式下反映该仓位的逐仓保证金数量 |
| data.>available | string |  | 仓位可用(基础币) |
| data.>frozen | string |  | 仓位冻结(基础币)<br><br>平仓单占用 |
| data.>total | string |  | 仓位总数量(available + frozen) |
| data.>leverage | string |  | 杠杆倍数 |
| data.>curRealisedPnl | string |  | 已实现盈亏<br><br>不包含手续费和资金费率 |
| data.>avgPrice | string |  | 平均开仓价 |
| data.>marginMode | string |  | 保证金模式<br><br>`crossed` 全仓<br><br>`isolated` 逐仓 |
| data.>positionStatus | string |  | 仓位执行状态<br><br>`normal` 正常 |
| data.>holdMode | string |  | 持仓模式<br><br>`one_way_mode` 单向持仓<br><br>`hedge_mode` 双向持仓 |
| data.>unrealisedPnl | string |  | 未实现盈亏<br><br>逐仓模式下反映该逐仓仓位的未实现盈亏 |
| data.>liquidationPrice | string |  | 预估强平价<br><br>小于等于0，代表永不爆仓 |
| data.>mmr | string |  | 维持保证金率 |
| data.>profitRate | string |  | 收益率 |
| data.>markPrice | string |  | 标记价格 |
| data.>breakEvenPrice | string |  | 仓位盈亏平衡价 |
| data.>totalFunding | string |  | 资金总费用，仓位存续期间，资金费用的累加值,初始值为空，表示还没收取过资金费 |
| data.>openFeeTotal | string |  | 开仓已扣除手续费<br><br>仓位存续期间扣除的开仓交易手续费 |
| data.>closeFeeTotal | string |  | 平仓已扣手续费<br><br>仓位存续期间扣除的平仓交易手续费 |
| data.>cashDividend | string |  | 现金派息<br><br>单位为USDT |
| data.>createdTime | string |  | 仓位创建时间 时间戳 毫秒 |
| data.>updatedTime | string |  | 最近更新时间 时间戳 毫秒 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1753103840140,
  "data": {
    "list": [
      {
        "category": "USDT-FUTURES",
        "symbol": "BTCUSDT",
        "marginCoin": "USDT",
        "holdMode": "hedge_mode",
        "posSide": "long",
        "marginMode": "crossed",
        "positionBalance": "4701531.84941582",
        "available": "119.2068",
        "frozen": "0",
        "total": "119.2068",
        "leverage": "3",
        "curRealisedPnl": "0",
        "avgPrice": "108674",
        "positionStatus": "normal",
        "unrealisedPnl": "1124573.04243999",
        "liquidationPrice": "43099.9",
        "mmr": "0.015",
        "profitRate": "0.2391929010498401",
        "markPrice": "118097",
        "breakEvenPrice": "109208.6",
        "totalFunding": "-53076.32433032",
        "openFeeTotal": "-2842.86603479",
        "closeFeeTotal": "0",
        "cashDividend": "0",
        "createdTime": "1736378720620",
        "updatedTime": "1753102803148"
      }
    ]
  }
}
```

## 获取历史仓位

`GET /api/v3/position/history-position`

限频规则: 20次/秒/UID

查询历史90天内持仓列表；用户可以通过网页端下载[全部时间历史仓位信息](https://www.bitget.com/zh-CN/trade-asset-order/uta-order-history-order)(最早可导出2018年1月1日的数据)

- 限频规则: 20次/秒/UID

- 需要统一账户管理只读/读写权限

Operation ID: `utaTradePositionGetPositionHistory`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| category | query | string | 是 | 产品类型<br><br>`USDT-FUTURES` USDT合约<br><br>`COIN-FUTURES` 币本位合约<br><br>`USDC-FUTURES` USDC合约 |
| symbol | query | string |  | 交易对 如:`BTCUSDT` |
| startTime | query | string |  | 开始时间戳 <br><br>Unix时间戳的毫秒数格式，如 1597026383085<br><br> 最大查询范围90天天 |
| endTime | query | string |  | 结束时间戳 <br><br>Unix时间戳的毫秒数格式，如 1597026383085<br><br> `startTime`和`endTime`间隔不超过30天 |
| limit | query | string |  | 每页查询条数<br><br>最大`100`，默认`100` |
| cursor | query | string |  | 分页游标<br><br>用于翻页，首次查询不传，查询第二页及后面的数据时，取上一次查询返回cursor |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.list | string[] |  | 列表 |
| data.>positionId | string |  | 仓位id |
| data.>category | string |  | 产品类型 <br><br>`USDT-FUTURES` USDT合约<br><br>`COIN-FUTURES` 币本位合约<br><br>`USDC-FUTURES` USDC合约 |
| data.>symbol | string |  | 币对名称 BTCUSDT |
| data.>marginCoin | string |  | 保证金币种 |
| data.>posSide | string |  | 仓位方向<br><br>`long`/`short` |
| data.>openPriceAvg | string |  | 开仓平均价 |
| data.>closePriceAvg | string |  | 平仓平均价 |
| data.>openTotalPos | string |  | 累计开仓数量 |
| data.>closeTotalPos | string |  | 累计平仓数量 |
| data.>marginMode | string |  | 保证金模式<br><br>`crossed` 全仓<br><br>`isolated` 逐仓 |
| data.>holdMode | string |  | 持仓模式<br><br>`one_way_mode` 单向持仓<br><br>`hedge_mode` 双向持仓 |
| data.>cumRealisedPnl | string |  | 已实现盈亏(不包含手续费和资金费用) |
| data.>netProfit | string |  | 净盈亏 (包含扣除手续费和资金费用) |
| data.>totalFunding | string |  | 资金总费用<br><br>仓位存续期间，资金费用的累加值,初始值为空，表示还没收取过资金费 |
| data.>openFeeTotal | string |  | 开仓已扣除手续费<br><br>仓位存续期间扣除的开仓交易手续费 |
| data.>closeFeeTotal | string |  | 平仓已扣手续费<br><br>仓位存续期间扣除的平仓交易手续费 |
| data.>cashDividend | string |  | 现金派息<br><br>单位为USDT |
| data.>createdTime | string |  | 仓位创建时间<br><br>时间戳 毫秒 |
| data.>updatedTime | string |  | 仓位更新时间<br><br>时间戳 毫秒 |
| data.cursor | string |  | 分页游标 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1730186957802,
  "data": {
    "list": [
      {
        "positionId": "1111111111111111111",
        "category": "USDT-FUTURES",
        "symbol": "EOSUSDT",
        "marginCoin": "USDT",
        "holdMode": "one_way_mode",
        "posSide": "long",
        "marginMode": "crossed",
        "openPriceAvg": "1960.001",
        "closePriceAvg": "1959.999",
        "openTotalPos": "58",
        "closeTotalPos": "58",
        "cumRealisedPnl": "-0.116",
        "netProfit": "-45.588",
        "totalFunding": "0",
        "openFeeTotal": "-22.7360116",
        "closeFeeTotal": "-22.7359884",
        "cashDividend": "0",
        "createdTime": "1729928018076",
        "updatedTime": "1729929656321"
      }
    ],
    "cursor": "1111111111111111111"
  }
}
```

## 获取仓位ADL排名

`GET /api/v3/position/adlRank`

限频规则: 1次/秒/UID

获取合约仓位ADL排名

- 限频规则: 1次/秒/UID

- 需要统一账户交易只读/读写权限

Operation ID: `utaTradePositionGetPositionADLRank`

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.symbol | string |  | 交易对名称 |
| data.marginCoin | string |  | 保证金币种 |
| data.adlRank | string |  | ADL排序<br><br>当前仓位在自动减仓序列中的排序。当市场发生自动减仓事件时，值越接近1，您的持仓被减少的概率越大 |
| data.holdSide | string |  | 持仓方向<br><br>`long` 多仓<br><br>`short`空仓 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1754035547922,
  "data": [
    {
      "symbol": "MOVEUSDT",
      "marginCoin": "USDT",
      "adlRank": "0.4872",
      "holdSide": "long"
    }
  ]
}
```

## 获取借币数据

`GET /api/v3/trade/loan-data`

限频规则: 10次/秒/UID

查询统一账户当前的借币数据，包含借币总额、下次扣息时间及各币种负债明细。

- 限频规则: 10次/秒/UID

- 需要统一账户交易只读/读写权限

Operation ID: `utaTradePositionGetLoanData`

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.currentLoans | string |  | 当前借币总额<br><br>单位为USD |
| data.interestPaymentTime | string |  | 下次扣息时间<br><br>Unix毫秒时间戳 |
| data.debtCoinList | object[] |  | 负债币种列表 |
| data.debtCoinList[].coin | string |  | 负债币种 |
| data.debtCoinList[].debt | string |  | 负债数量<br><br>单位为负债币种 |
| data.debtCoinList[].interestFreeAmount | string |  | 免息额度<br><br>单位为coin |
| data.debtCoinList[].interestRateNextHour | string |  | 下小时借贷利率（年化）<br><br>小数形式，如0.1代表10% |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1751972326323,
  "data": {
    "currentLoans": "1000.5",
    "interestPaymentTime": "1751976000000",
    "debtCoinList": [
      {
        "coin": "USDT",
        "debt": "1000.5",
        "interestFreeAmount": "200",
        "interestRateNextHour": "0.0001"
      }
    ]
  }
}
```

## 创建策略单

`POST /api/v3/trade/place-strategy-order`

限频规则: 10次/秒/UID

创建策略单

**API Broker返佣标识**:

  需在HTTP Header请求头中添加如下代码块

  > "X-CHANNEL-API-CODE":"your-channel-api-code"

  该返佣标识 header 现已对全部策略 `type`（`tpsl`/`trigger`/`oco`/`trailing_stop`/`iceberg`/`twap`）生效。

- 限频规则: 10次/秒/UID

- 需要统一账户交易读写权限

### 公共请求参数

以下字段适用于所有策略 `type`。各策略类型专属的参数详见下方各自的独立小节。

Operation ID: `utaStrategyPlaceStrategyOrder`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| category | string | 是 | 产品类型<br><br>`SPOT` 现货<br><br>`MARGIN` 杠杆<br><br>`USDT-FUTURES` USDT合约<br><br>`COIN-FUTURES` 币本位合约<br><br>`USDC-FUTURES` USDC合约 |
| symbol | string | 是 | 交易对名称<br><br>例如：`BTCUSDT` |
| type | string |  | 策略类型<br><br>`tpsl`止盈止损<br><br>`trigger`计划委托<br><br>`oco`OCO委托<br><br>`trailing_stop`追踪委托<br><br>`iceberg`冰山委托<br><br>`twap`TWAP委托<br><br>默认为`tpsl`止盈止损 |
| side | string |  | 交易方向<br><br>`buy`买<br><br>`sell`卖<br><br>双向持仓：<br><br>开多：`side=buy` & `posSide=long`<br><br>开空：`side=sell` & `posSide=short`<br><br>平多：`side=sell` & `posSide=long`<br><br>平空：`side=buy` & `posSide=short`<br><br>单向持仓：<br><br>开多 `side=buy`<br><br>开空 `side=sell`<br><br>平多 `side=sell` & `reduceOnly=yes`<br><br>平空 `side=buy` & `reduceOnly=yes` |
| posSide | string |  | 持仓方向<br><br>`long` 多<br><br>`short` 空 |
| qty | string |  | 委托数量 |
| marginMode | string |  | 保证金模式<br/>`crossed` 全仓<br/>`isolated` 逐仓<br/>不传默认为全仓<br/>仅适用于合约 |
| clientOid | string |  | 自定义策略单 ID<br><br>格式：`^[\.A-Z\:/a-z0-9_-]{1,32}$`<br><br>幂等有效期六小时<br><br>现已支持全部策略 `type`（`tpsl`/`trigger`/`oco`/`trailing_stop`/`iceberg`/`twap`）。 |

```json
{
  "category": "USDT-FUTURES",
  "symbol": "BTCUSDT",
  "posSide": "long",
  "stopLoss": "99000",
  "takeProfit": "100800",
  "clientOid": "121211212122"
}
```

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.orderId | string |  | 策略订单id |
| data.clientOid | string |  | 自定义策略订单id |

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

## 修改策略单

`POST /api/v3/trade/modify-strategy-order`

限频规则: 10次/秒/UID

修改策略单

- 限频规则: 10次/秒/UID

- 需要统一账户交易读写权限

Operation ID: `utaStrategyModifyStrategyOrder`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| orderId | string | 是 | 策略订单id<br><br>`orderId`和`clientOid`二者必填其一<br><br>如同时传入`orderId`及`clientOid`，则`orderId`先级更高，忽略`clientOid`入参 |
| clientOid | string |  | 自定义策略订单id<br><br>`orderId`和`clientOid`二者必填其一<br><br>如同时传入`orderId`及`clientOid`，则`orderId`先级更高，忽略`clientOid`入参 |
| qty | string | 是 | 委托数量<br><br>部分止盈止损模式下可修改，单位为`base coin` |
| tpTriggerBy | string |  | 止盈触发类型<br><br>`market`市场价格<br><br>`mark`标记价格 |
| slTriggerBy | string |  | 止损触发类型<br><br>`market`市场价格<br><br>`mark`标记价格 |
| takeProfit | string |  | 止盈触发价格 |
| stopLoss | string |  | 止损触发价格 |
| tpOrderType | string |  | 止盈触发的策略单类型<br><br>`limit` 限价单<br><br>`market` 市价单 |
| slOrderType | string |  | 止损触发的策略单类型<br><br>`limit` 限价单<br><br>`market` 市价单 |
| tpLimitPrice | string |  | 止盈策略单执行价格<br><br>仅限价单`tpOrderType=limit`时可修改 |
| slLimitPrice | string |  | 止损策略单执行价格<br><br>仅限价单`slOrderType=limit`时可修改 |
| triggerBy | string |  | 计划委托触发价格类型<br><br>`market`市场价格<br><br>`mark`标记价格 |
| triggerPrice | string |  | 计划委托触发价格<br><br>仅限价单`triggerOrderType=limit`时可修改 |
| triggerOrderType | string |  | 计划委托订单类型<br><br>`limit`限价单<br><br>`market`市价单 |
| triggerOrderPrice | string |  | 计划委托执行价格<br><br>仅限价单`triggerOrderType=limit`时可修改 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.orderId | string |  | 策略订单id |
| data.clientOid | string |  | 自定义策略订单id |

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

## 撤销策略单

`POST /api/v3/trade/cancel-strategy-order`

限频规则: 10次/秒/UID

撤销策略单

对于`iceberg`/`twap`委托，撤销母订单会同时撤销其所有未成交子订单；对于`oco`委托，撤销其中一笔委托会同时撤销另一笔委托。

- 限频规则: 10次/秒/UID

- 需要统一账户交易读写权限

Operation ID: `utaStrategyCancelStrategyOrder`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| orderId | string | 是 | 策略订单id<br><br>`orderId`和`clientOid`二者必填其一<br><br>如同时传入`orderId`及`clientOid`，则`orderId`先级更高，忽略`clientOid`入参 |
| clientOid | string |  | 自定义策略订单id<br><br>`orderId`和`clientOid`二者必填其一<br><br>如同时传入`orderId`及`clientOid`，则`orderId`先级更高，忽略`clientOid`入参 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.code | string |  | 状态码 |
| data.msg | string |  | 状态消息 |
| data.requestTime | string |  | 时间戳 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695806875837,
  "data": null
}
```

## 获取当前策略单

`GET /api/v3/trade/unfilled-strategy-orders`

限频规则: 20次/秒/UID

获取当前策略单

- 限频规则: 20次/秒/UID

- 需要统一账户交易只读/读写权限

Operation ID: `utaStrategyGetUnfilledStrategyOrders`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| category | query | string | 是 | 产品类型<br><br>`spot` 现货<br><br>`margin` 杠杆<br><br>`usdt-futures` U本位合约<br><br>`coin-futures` 币本位合约<br><br>`usdc-futures` USDC合约 |
| type | query | string |  | 策略类型<br><br>`tpsl`止盈止损<br><br>`trigger`计划委托<br><br>`oco` OCO<br><br>`trailing_stop`追踪委托<br><br>`iceberg`冰山委托<br><br>`twap`分时委托 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  | 订单列表 |
| data[].orderId | string |  | 策略订单id |
| data[].clientOid | string |  | 自定义策略订单id |
| data[].category | string |  | 产品类型<br><br>`USDT-FUTURES` U本位合约<br><br>`COIN-FUTURES` 币本位合约<br><br>`USDC-FUTURES` USDC合约 |
| data[].symbol | string |  | 交易对名称 <br><br>例如：`BTCUSDT` |
| data[].qty | string |  | 委托数量 |
| data[].side | string |  | 订单方向<br><br>`buy`: 买<br><br>`sell`: 卖 |
| data[].posSide | string |  | 交易方向<br><br>`long` 多仓<br><br>`short` 空仓 |
| data[].status | string |  | 策略订单状态<br><br>`pending` 等待执行<br><br>`success` 已执行<br><br>`failed` 执行失败<br><br>`cancelled` 已撤销<br><br>`submitting` 下单中 |
| data[].marginMode | string |  | 保证金模式<br/>`crossed` 全仓<br/>`isolated` 逐仓<br/>不传默认为全仓<br/>仅适用于合约 |
| data[].type | string |  | 策略类型<br><br>`tpsl`止盈止损<br><br>`trigger`计划委托<br><br>`oco` OCO<br><br>`trailing_stop`追踪委托<br><br>`iceberg`冰山委托<br><br>`twap`分时委托 |
| data[].createdTime | string |  | 订单创建时间<br><br>Unix毫秒时间戳，例如1690196141868 |
| data[].updatedTime | string |  | 订单更新时间<br><br>Unix毫秒时间戳，例如1690196141868 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1730186730084,
  "data": [
    {
      "orderId": "111111111111111111",
      "clientOid": "111111111111111111",
      "category": "USDT-FUTURES",
      "symbol": "BTCUSDT",
      "qty": "0.01",
      "side": "sell",
      "posSide": "long",
      "status": "pending",
      "tpTriggerBy": "market",
      "slTriggerBy": "market",
      "takeProfit": "110000",
      "stopLoss": "90000",
      "tpOrderType": "market",
      "slOrderType": "market",
      "tpLimitPrice": "91000",
      "slLimitPrice": "111000",
      "triggerBy": "market",
      "triggerPrice": "100000",
      "triggerOrderType": "limit",
      "triggerOrderPrice": "100500",
      "marginMode": "crossed",
      "createdTime": "1730186725663",
      "updatedTime": "1730186725691"
    }
  ]
}
```

## 获取历史策略单

`GET /api/v3/trade/history-strategy-orders`

限频规则: 20次/秒/UID

查询历史策略单

- 限频规则: 20次/秒/UID

- 需要统一账户交易只读/读写权限

Operation ID: `utaStrategyGetHistoryStrategyOrders`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| category | query | string | 是 | 产品类型<br><br>`spot` 现货<br><br>`margin` 杠杆<br><br>`usdt-futures` U本位合约<br><br>`coin-futures` 币本位合约<br><br>`usdc-futures` USDC合约 |
| type | query | string |  | 策略类型<br><br>`tpsl`止盈止损<br><br>`trigger`计划委托<br><br>`oco` OCO<br><br>`trailing_stop`追踪委托<br><br>`iceberg`冰山委托<br><br>`twap`分时委托<br><br>默认值为`tpsl` |
| startTime | query | string |  | 开始时间戳 <br><br>Unix时间戳的毫秒数格式，如 1597026383085<br><br> - 默认查询时间为近30天<br><br>- 开始和结束的最大时间间隔为90天 |
| endTime | query | string |  | 结束时间戳 <br><br>Unix时间戳的毫秒数格式，如 1597026383085<br><br> - 默认查询时间为近30天<br><br>- 开始和结束的最大时间间隔为90天 |
| limit | query | string |  | 每页条目数<br><br> 最大`100`，默认`100` |
| cursor | query | string |  | 分页游标<br><br>用于翻页，首次查询不传，查询第二页及后面的数据时，取上一次查询返回的最小orderId，结果会返回小于该值的数据 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.list | object[] |  | 订单列表 |
| data.list[].orderId | string |  | 策略订单id |
| data.list[].clientOid | string |  | 自定义策略订单id |
| data.list[].category | string |  | 产品类型<br><br>`usdt-futures` U本位合约<br><br>`coin-futures` 币本位合约<br><br>`usdc-futures` USDC合约 |
| data.list[].symbol | string |  | 交易对名称 <br><br>例如：`BTCUSDT` |
| data.list[].qty | string |  | 委托数量 |
| data.list[].posSide | string |  | 交易方向<br><br>`long` 多仓<br><br>`short` 空仓 |
| data.list[].status | string |  | 策略订单状态<br><br>`success` 已执行<br><br>`failed` 执行失败<br><br>`cancelled` 已撤销 |
| data.list[].marginMode | string |  | 保证金模式<br/>`crossed` 全仓<br/>`isolated` 逐仓<br/>不传默认为全仓<br/>仅适用于合约 |
| data.list[].type | string |  | 策略类型<br><br>`tpsl`止盈止损<br><br>`trigger`计划委托<br><br>`oco` OCO<br><br>`trailing_stop`追踪委托<br><br>`iceberg`冰山委托<br><br>`twap`分时委托 |
| data.list[].tpslMode | string |  | 止盈止损模式<br><br>`full` 全部止盈止损<br><br>`partial` 部分止盈止损<br><br>仅 `type=tpsl` 的订单有值，其他策略类型返回空字符串 `""` |
| data.list[].createdTime | string |  | 订单创建时间<br><br>Unix毫秒时间戳，例如1690196141868 |
| data.list[].updatedTime | string |  | 订单更新时间<br><br>Unix毫秒时间戳，例如1690196141868 |
| data.cursor | string |  | 下一页游标<br><br>把该值作为下次请求的`cursor`参数，可获取下一页数据 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1730186730084,
  "data": {
    "list": [
      {
        "orderId": "111111111111111111",
        "clientOid": "111111111111111111",
        "category": "USDT-FUTURES",
        "symbol": "BTCUSDT",
        "qty": "0.01",
        "posSide": "long",
        "status": "success",
        "tpTriggerBy": "market",
        "slTriggerBy": "market",
        "takeProfit": "110000",
        "stopLoss": "90000",
        "tpOrderType": "market",
        "slOrderType": "market",
        "tpLimitPrice": "91000",
        "slLimitPrice": "111000",
        "triggerBy": "market",
        "triggerPrice": "100000",
        "triggerOrderType": "limit",
        "triggerOrderPrice": "100500",
        "marginMode": "crossed",
        "tpslMode": "full",
        "createdTime": "1730186725663",
        "updatedTime": "1730186725691"
      }
    ],
    "cursor": "1233319323918499840"
  }
}
```

## 获取历史策略子订单

`GET /api/v3/trade/strategy-sub-orders`

查询策略生成的终态历史子订单

仅支持查询策略订单创建后 7 天内的子订单

- 限频规则: 10次/秒/UID

- 需要统一账户交易只读/读写权限

Operation ID: `utaStrategyGetStrategySubOrders`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| orderId | query | string | 是 | 策略订单ID |
| limit | query | string |  | 每页条目数<br><br>最大`100`，默认`100` |
| cursor | query | string |  | 分页游标<br><br>用于翻页，首次查询不传，查询第二页及后面的数据时，取上一次查询返回的最小orderId，结果会返回小于该值的数据 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.list | object[] |  | 子订单列表 |
| data.list[].subOrderId | string |  | 子订单ID |
| data.list[].subClientOid | string |  | 自定义订单ID |
| data.list[].category | string |  | 业务线<br><br>`SPOT` 现货交易<br><br>`MARGIN` 杠杆交易<br><br>`USDT-FUTURES` U本位合约<br><br>`COIN-FUTURES` 币本位合约<br><br>`USDC-FUTURES` USDC合约 |
| data.list[].symbol | string |  | 交易对名称 |
| data.list[].price | string |  | 委托价格 |
| data.list[].qty | string |  | 委托数量<br><br>单位为base coin |
| data.list[].cumExecQty | string |  | 累计成交数量<br><br>单位为base coin |
| data.list[].avgPrice | string |  | 平均成交价 |
| data.list[].side | string |  | 开单方向<br><br>`buy` 买<br><br>`sell` 卖 |
| data.list[].posSide | string |  | 仓位方向<br><br>`long` 多<br><br>`short` 空<br><br>只适用合约订单 |
| data.list[].status | string |  | 订单状态<br><br>`filled` 已成交<br><br>`cancelled` 已撤销<br><br>`failed` 失败 |
| data.list[].createdTime | string |  | 订单创建时间<br><br>Unix毫秒时间戳 |
| data.list[].updatedTime | string |  | 订单更新时间<br><br>Unix毫秒时间戳 |
| data.cursor | integer |  | 下一页游标<br><br>把该值作为下次请求的`cursor`参数，可获取下一页数据 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1724486400000.0,
  "data": {
    "list": [
      {
        "subOrderId": "1234567890123456789",
        "subClientOid": "myOrder001",
        "category": "USDT-FUTURES",
        "symbol": "BTCUSDT",
        "price": "60000",
        "qty": "0.01",
        "cumExecQty": "0.01",
        "avgPrice": "60001",
        "side": "buy",
        "posSide": "long",
        "status": "filled",
        "createdTime": "1724486400000",
        "updatedTime": "1724486401000"
      }
    ],
    "cursor": 1234567890123456768
  }
}
```

## 追加投资额

`POST /api/v3/trade/grid/add-investment`

交易机器人投资追加金额，支持追加现货金额及合约调整保证金。

- 限频规则: 1次/秒/UID

- 需要统一账户交易权限

Operation ID: `utaGridAddInvestment`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| category | string | 是 | 业务线<br/>`SPOT`：现货交易<br/>`USDT-FUTURES`：USDT保证金合约<br/>`USDC-FUTURES`：USDC保证金合约 |
| botId | string | 是 | 网格机器人ID，需保证业务线与网格机器人ID匹配，否则报错 |
| coin | string | 是 | 追加币种 |
| size | string | 是 | 金额 |
| fundsSource | string[] | 是 | 资金来源<br><br>`funding`：资金账户<br><br>`uta`：统一账户<br><br>`otc`：OTC账户 |
| adjustType | string |  | 调整类型，仅适用于合约网格，合约必填<br><br>`increase`<br><br>`decrease` |
| reinvestProfit | string |  | 是否复投利润，默认`yes`，仅适用于现货网格<br><br>`yes`<br><br>`no` |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.botId | string |  | 网格机器人ID |

## 查询网格交易机器人详情

`GET /api/v3/trade/grid/bot-detail`

查询指定策略的详细信息，含参数配置、当前状态、累计收益等。

- 限频规则: 10次/秒/UID

- 需要统一账户交易只读权限

Operation ID: `utaGridBotDetail`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| botId | query | string | 是 | 网格机器人ID |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.botId | string |  | 网格机器人ID |
| data.symbol | string |  | 交易对 |
| data.status | string |  | 状态<br><br>`init`：初始化<br><br>`waiting`：待启动<br><br>`running`：运行中<br><br>`terminating`：终止中<br><br>`terminated`：已终止 |
| data.totalProfit | string |  | 总收益，单位USDT |
| data.roi | string |  | 收益率，小数形式 |
| data.gridProfit | string |  | 网格利润，单位USDT |
| data.gridProfitRate | string |  | 网格利润比例 |
| data.unpairedProfit | string |  | 未配对收益，单位USDT |
| data.unpairedProfitRate | string |  | 未配对收益比例 |
| data.margin | string |  | 保证金，仅合约有 |
| data.arbitrageAPR | string |  | 套利APR |
| data.totalAPR | string |  | 总APR |
| data.createdTime | string |  | 创建时间 |
| data.runningTime | string |  | 运行时长，单位ms |
| data.currentBaseBalance | string |  | 当前基础币余额 |
| data.currentQuoteBalance | string |  | 当前计价币余额 |
| data.initialBaseHoldings | string |  | 初始基础币持仓 |
| data.initialQuoteHoldings | string |  | 初始计价币持仓 |
| data.reservedBaseTradingFee | string |  | 预留基础币交易手续费 |
| data.reservedQuoteTradingFee | string |  | 预留计价币交易手续费 |
| data.gridStartPrice | string |  | 网格起始价 |
| data.gridType | string |  | 网格类型<br><br>`long`：做多<br><br>`short`：做空<br><br>`netural`：中性 |
| data.maxPrice | string |  | 网格上限价格 |
| data.minPrice | string |  | 网格下限价格 |
| data.gridNum | string |  | 网格格数 |
| data.gridOrderMode | string |  | 网格模式<br><br>`arithmetic`：等差<br><br>`geometric`：等比 |
| data.baseInvestmentCoin | string |  | 基础币投入币种 |
| data.baseInvestmentAmount | string |  | 基础币投入金额 |
| data.quoteInvestmentCoin | string |  | 计价币投入币种 |
| data.quoteInvestmentAmount | string |  | 计价币投入金额 |
| data.slippage | string |  | 滑点<br><br>`1%`<br><br>`2%`<br><br>`none` |
| data.triggerCondition | string |  | 触发条件<br><br>`instant`：立即<br><br>`price`：价格<br><br>`rsi`<br><br>`boll` |
| data.triggerParams | object[] |  | 触发参数 |
| data.triggerParams[].indicatorLength | string |  | 指标周期 |
| data.triggerParams[].threshold | string |  | 阈值 |
| data.triggerParams[].multiplier | string |  | 倍数 |
| data.triggerParams[].interval | string |  | 周期 |
| data.triggerPrice | string |  | 触发价格 |
| data.terminationCondition | string |  | 终止条件<br><br>`rsi`<br><br>`boll` |
| data.terminationParams | object[] |  | 终止参数 |
| data.terminationParams[].indicatorLength | string |  | 指标周期 |
| data.terminationParams[].threshold | string |  | 阈值 |
| data.terminationParams[].multiplier | string |  | 倍数 |
| data.terminationParams[].interval | string |  | 周期 |
| data.terminationSell | string |  | 终止时是否卖出<br><br>`yes`<br><br>`no` |
| data.stopLoss | string |  | 止损价格 |
| data.takeProfit | string |  | 止盈价格 |
| data.hodlMode | string |  | 屯币模式<br><br>`yes`<br><br>`no` |
| data.autoTransferProfits | string |  | 自动转出利润<br><br>`yes`<br><br>`no` |
| data.arbitrageCount | string |  | 套利次数 |
| data.terminationReason | string |  | 终止原因<br><br>`MANUAL_END`：手动终止<br><br>`NEW_WAIT`：待启动<br><br>`ACCOUNT_BALANCE_LACKING_END`：可用资金不足<br><br>`STOP_PROFIT_END`：止盈终止<br><br>`STOP_LOSS_END`：止损终止<br><br>`CANCEL_END`：撤单终止<br><br>`SYSTEM_END`：下单失败导致撤单<br><br>`FOLLOW_END`：跟随终止<br><br>`SUBSCRIBE_STOP_PROFIT_END`：订阅止盈终止<br><br>`SUBSCRIBE_STOP_LOSS_END`：订阅止损终止<br><br>`PLACE_ORDER_FAIL_END`：下单连续失败终止<br><br>`SYMBOL_DOWN_END`：币对下架终止<br><br>`SUB_ACCOUNT_TRANSFER_FAIL`：资金划转失败<br><br>`HIGHEST_PRICE_END`：最高价终止<br><br>`BOTTOM_PRICE_END`：最低价终止<br><br>`BURST_END`：爆仓终止<br><br>`MOVE_GRID_FAIL`：网格移动失败终止<br><br>`EXPIRE_TIME_END`：系统定时终止<br><br>`HANDLE_SUB_POSITION_END`：手动减仓终止<br><br>`STOP_PRICE_ACHIEVE`：达到终止价格<br><br>`ADL_END`：ADL终止<br><br>`AUTO_CONVERT_END`：自动兑换终止<br><br>`CONDITION_TRIGGER_END`：条件触发终止<br><br>`ADL_CONVERT_END`：ADL减仓终止<br><br>`CANCEL_DELIVERY_ORDER`：交割撤单<br><br>`BASIS_RATE_TRIGGER`：基差率触发终止<br><br>`EARN_REDEEM_FAIL`：理财资金赎回失败<br><br>`SYSTEM_CANCEL`：系统取消<br><br>`SYMBOL_RSTOCK_SPLIT`：拆合股撤单 |

## 终止网格交易机器人

`POST /api/v3/trade/grid/close-bot`

终止指定机器人，停止挂单并按策略配置处理未成交订单/持仓。

- 限频规则: 1次/秒/UID

- 需要统一账户交易权限

Operation ID: `utaGridCloseBot`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| botId | string | 是 | 网格机器人ID |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data |  |  | Response data |

## 创建网格交易机器人

`POST /api/v3/trade/grid/create-bot`

提交现货及合约网格交易机器人创建请求。

- 限频规则: 1次/秒/UID

- 需要统一账户交易权限

Operation ID: `utaGridCreateBot`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| category | string | 是 | 业务线<br><br>`SPOT`：现货交易<br><br>`USDT-FUTURES`：U本位合约<br><br>`USDC-FUTURES`：USDC合约 |
| symbol | string | 是 | 交易对名称 |
| gridType | string |  | 网格方向<br>`long`<br>`short`<br>`neutral`<br>**合约（`USDT-FUTURES` / `USDC-FUTURES`）必填；现货（`SPOT`）可选** |
| maxPrice | string | 是 | 网格上限价格 |
| minPrice | string | 是 | 网格下限价格 |
| gridNum | string | 是 | 网格格数 |
| gridOrderMode | string | 是 | 网格挂单模式<br><br>`arithmetic`：等差<br><br>`geometric`：等比 |
| leverage | string |  | 杠杆倍数，默认1，仅合约生效 |
| investmentAmount | object[] | 是 | 投入金额 |
| investmentAmount[].coin | string | 是 | 币种 |
| investmentAmount[].amount | string | 是 | 金额 |
| fundsSource | string[] | 是 | 资金来源<br><br>`funding`：资金账户<br><br>`uta`：统一账户<br><br>`otc`：OTC账户 |
| autoReserveMargin | string |  | 自动预留保证金 |
| reservedMargin | string |  | 预留保证金，仅合约生效 |
| triggerCondition | string |  | 触发条件，默认`instant`<br><br>`instant`<br><br>`price`<br><br>`rsi`<br><br>`boll` |
| triggerParams | object[] |  | 触发参数 |
| triggerParams[].indicatorLength | string |  | 指标周期 |
| triggerParams[].threshold | string |  | 阈值 |
| triggerParams[].multiplier | string |  | 倍数 |
| triggerParams[].interval | string |  | 周期 |
| triggerPrice | string |  | 触发价格 |
| terminationCondition | string |  | 终止条件<br><br>`rsi`<br><br>`boll` |
| terminationParams | object[] |  | 终止参数 |
| terminationParams[].indicatorLength | string |  | 指标周期 |
| terminationParams[].threshold | string |  | 阈值 |
| terminationParams[].multiplier | string |  | 倍数 |
| terminationParams[].interval | string |  | 周期 |
| terminationSell | string |  | 终止时是否卖出，仅现货网格有<br><br>`yes`<br><br>`no` |
| stopLoss | string |  | 止损价格 |
| takeProfit | string |  | 止盈价格 |
| slippage | string | 是 | 滑点 |
| trailingGrid | string |  | 移动网格，默认`no`<br><br>`yes`<br><br>`no` |
| movingAverageGains | string |  | 移动平均收益 |
| stopUpwardPrice | string |  | 上移止损价格 |
| hodlMode | string |  | 屯币模式，默认`no`，仅现货生效<br><br>`yes`<br><br>`no` |
| marketOpen | string |  | 市价开仓，默认开启，仅合约生效<br><br>`yes`<br><br>`no` |
| lossReserve | string |  | 亏损预留，默认开启，仅合约生效<br><br>`yes`<br><br>`no` |
| autoTransferProfits | string | 是 | 自动转出利润，默认`no`<br><br>`yes`<br><br>`no` |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.botId | string |  | 网格机器人ID |

## 创建中性网格交易机器人

`POST /api/v3/trade/grid/create-neutral-bot`

提交合约中性交易机器人创建请求。

- 限频规则: 1次/秒/UID

- 需要统一账户交易权限

Operation ID: `utaGridCreateNeutralBot`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| category | string | 是 | 业务线<br><br>`USDT-FUTURES`：USDT保证金合约<br><br>`USDC-FUTURES`：USDC保证金合约 |
| symbol | string | 是 | 交易对 |
| maxPrice | string | 是 | 上限价格 |
| minPrice | string | 是 | 下限价格 |
| gridNum | string | 是 | 网格格数 |
| gridOrderMode | string | 是 | 网格模式<br><br>`arithmetic`：等差<br><br>`geometric`：等比 |
| leverage | string |  | 杠杆 |
| investmentAmount | object[] |  | 投入币种及金额列表，合约仅支持计价币USDT/USDC |
| investmentAmount[].coin | string | 是 | 投入币种 |
| investmentAmount[].amount | string | 是 | 投入金额 |
| triggerPrice | string |  | 触发价格 |
| stopLoss | string |  | 止损价格 |
| takeProfit | string |  | 止盈价格 |
| autoTransferProfits | string |  | 是否自动转出利润 |
| fundsSource | string[] | 是 | 资金来源<br><br>`funding`：资金账户<br><br>`uta`：统一账户<br><br>`otc`：OTC账户 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.botId | string |  | 网格机器人ID |

## 查询网格交易机器人挂单详情

`GET /api/v3/trade/grid/list-details`

查询指定策略关联的挂单详情。

- 限频规则: 1次/秒/UID

- 需要统一账户交易只读权限

Operation ID: `utaGridListDetails`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| category | query | string | 是 | 业务线<br/>`SPOT`：现货交易<br/>`USDT-FUTURES`：USDT保证金合约<br/>`USDC-FUTURES`：USDC保证金合约 |
| botId | query | string | 是 | 网格机器人ID |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.botId | string |  | 网格机器人ID |
| data.symbol | string |  | 交易对名称 |
| data.buyOrderList | object[] |  | 买单列表 |
| data.buyOrderList[].orderId | string |  | 订单ID |
| data.buyOrderList[].delegateCount | string |  | 委托数量 |
| data.buyOrderList[].delegatePrice | string |  | 委托价格 |
| data.buyOrderList[].changeRequired | integer |  | 成交所需涨跌，返回去除百分比的数值，如返回`1`代表`1%` |
| data.sellOrderList | object[] |  | 卖单列表 |
| data.sellOrderList[].orderId | string |  | 订单ID |
| data.sellOrderList[].delegateCount | string |  | 委托数量 |
| data.sellOrderList[].delegatePrice | string |  | 委托价格 |
| data.sellOrderList[].changeRequired | integer |  | 成交所需涨跌，返回去除百分比的数值，如返回`1`代表`1%` |

## 修改网格交易机器人参数

`POST /api/v3/trade/grid/modify-bot`

运行中修改网格交易机器人的基本参数（价格区间、投入金额等）。

- 限频规则: 1次/秒/UID

- 需要统一账户交易权限

Operation ID: `utaGridModifyBot`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| category | string |  | 业务线<br/>`SPOT`：现货交易<br/>`USDT-FUTURES`：USDT保证金合约<br/>`USDC-FUTURES`：USDC保证金合约 |
| botId | string | 是 | 网格机器人ID |
| takeProfit | string |  | 止盈价格。**如不传，会清空止盈价格。**如不修改止盈价格，需要传入当前值 |
| stopLoss | string |  | 止损价格。**如不传，会清空止损价格。**如不修改止损价格，需要传入当前值 |
| terminationCondition | string |  | 终止条件<br><br>`rsi`<br><br>`boll` |
| terminationParams | object[] |  | 终止参数 |
| terminationParams[].indicatorLength | string |  | 指标周期 |
| terminationParams[].threshold | string |  | 阈值 |
| terminationParams[].multiplier | string |  | 倍数 |
| terminationParams[].interval | string |  | 周期 |
| hodlMode | string |  | 屯币模式<br><br>`yes`<br><br>`no` |
| autoTransferProfits | string |  | 自动转出利润<br><br>`yes`：转出<br><br>`no`：不转出 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.botId | string |  | 网格机器人ID |

## 修改网格区间和网格数

`POST /api/v3/trade/grid/modify-grid-interval`

修改网格区间及网格数接口。

- 限频规则: 1次/秒/UID

- 需要统一账户交易权限

Operation ID: `utaGridModifyGridInterval`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| category | string | 是 | 业务线<br><br>`SPOT`：现货交易<br><br>`USDT-FUTURES`：U本位合约<br><br>`USDC-FUTURES`：USDC合约 |
| botId | string | 是 | 网格机器人ID |
| maxPrice | string | 是 | 网格上限价格 |
| minPrice | string | 是 | 网格下限价格 |
| gridNum | string | 是 | 网格格数 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.botId | string |  | 网格机器人ID |

## 修改中性网格交易机器人参数

`POST /api/v3/trade/grid/modify-neutral-bot`

修改运行中的中性网格交易机器人基本参数。

- 限频规则: 1次/秒/UID

- 需要统一账户交易权限

Operation ID: `utaGridModifyNeutralBot`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| botId | string | 是 | 网格机器人ID |
| category | string | 是 | 业务线<br><br>`USDT-FUTURES`：USDT保证金合约<br><br>`USDC-FUTURES`：USDC保证金合约 |
| takeProfit | string |  | 止盈价格。**如不传，会清空止盈价格**，如不修改需传入当前值 |
| stopLoss | string |  | 止损价格。**如不传，会清空止损价格**，如不修改需传入当前值 |
| autoTransferProfits | string |  | 是否自动转出利润<br><br>`yes`：转出<br><br>`no`：不转出 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.botId | string |  | 网格机器人ID |

## 修改中性网格区间和网格数

`POST /api/v3/trade/grid/modify-neutral-grid-interval`

修改网格区间及网格数接口。

- 限频规则: 1次/秒/UID

- 需要统一账户交易权限

Operation ID: `utaGridModifyNeutralGridInterval`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| category | string | 是 | 业务线<br><br>`USDT-FUTURES`：USDT保证金合约<br><br>`USDC-FUTURES`：USDC保证金合约 |
| botId | string | 是 | 网格机器人ID |
| maxPrice | string | 是 | 网格上限价格 |
| minPrice | string | 是 | 网格下限价格 |
| gridNum | string | 是 | 网格格数 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.botId | string |  | 网格机器人ID |

## 查询中性网格交易机器人详情

`GET /api/v3/trade/grid/neutral-bot-detail`

查询指定合约中性策略的详细信息，含参数配置、当前状态、累计收益等。

- 限频规则: 10次/秒/UID

- 需要统一账户交易只读权限

Operation ID: `utaGridNeutralBotDetail`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| botId | query | string | 是 | 网格机器人ID |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.botId | string |  | 网格机器人ID |
| data.symbol | string |  | 交易对 |
| data.status | string |  | 状态<br><br>`init`：初始化中<br><br>`waiting`：等待中<br><br>`running`：运行中<br><br>`terminating`：终止中<br><br>`terminated`：已终止 |
| data.totalProfit | string |  | 总收益，单位USDT |
| data.roi | string |  | 收益率，小数形式 |
| data.gridProfit | string |  | 网格收益，单位USDT，等于已套利利润减去手续费 |
| data.gridProfitRate | string |  | 网格利润比例，小数形式 |
| data.unpairedProfit | string |  | 未配对收益，单位USDT |
| data.unpairedProfitRate | string |  | 未配对收益率，小数形式 |
| data.margin | string |  | 保证金（仅合约有） |
| data.arbitrageAPR | string |  | 套利年化收益率，小数形式，运行不足1天按1天计算 |
| data.totalAPR | string |  | 总年化收益率，小数形式，运行不足1天按1天计算 |
| data.createdTime | string |  | 创建时间 |
| data.runningTime | string |  | 运行时长，单位毫秒 |
| data.gridStartPrice | string |  | 网格起始价格 |
| data.maxPrice | string |  | 网格上限价格 |
| data.minPrice | string |  | 网格下限价格 |
| data.gridNum | string |  | 网格格数 |
| data.gridOrderMode | string |  | 网格模式<br><br>`arithmetic`：等差<br><br>`geometric`：等比 |
| data.triggerPrice | string |  | 触发价格 |
| data.leverage | string |  | 杠杆 |
| data.stopLoss | string |  | 止损价格 |
| data.takeProfit | string |  | 止盈价格 |
| data.holdPosition | string |  | 持仓量 |
| data.oneGridMinProfit | string |  | 单格最小利润 |
| data.oneGridMaxProfit | string |  | 单格最大利润 |
| data.autoTransferProfits | string |  | 是否自动转出利润<br><br>`yes`：转出<br><br>`no`：不转出 |

## 查询中性网格机器人挂单详情

`GET /api/v3/trade/grid/neutral-list-details`

查询指定合约中性策略关联的挂单详情。

- 限频规则: 1次/秒/UID

- 需要统一账户交易只读权限

Operation ID: `utaGridNeutralListDetails`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| category | query | string | 是 | 业务线<br/>`SPOT`：现货交易<br/>`USDT-FUTURES`：USDT保证金合约<br/>`USDC-FUTURES`：USDC保证金合约 |
| botId | query | string | 是 | 网格机器人ID |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.botId | string |  | 网格机器人ID |
| data.symbol | string |  | 交易对 |
| data.buyOrderList | object[] |  | 买单列表 |
| data.buyOrderList[].orderId | string |  | 订单ID |
| data.buyOrderList[].delegateCount | string |  | 委托数量 |
| data.buyOrderList[].delegatePrice | string |  | 委托价格 |
| data.buyOrderList[].changeRequired | integer |  | 成交所需涨跌，返回去除百分比的数值，如返回`1`代表`1%` |
| data.sellOrderList | object[] |  | 卖单列表 |
| data.sellOrderList[].orderId | string |  | 订单ID |
| data.sellOrderList[].delegateCount | string |  | 委托数量 |
| data.sellOrderList[].delegatePrice | string |  | 委托价格 |
| data.sellOrderList[].changeRequired | integer |  | 成交所需涨跌，返回去除百分比的数值，如返回`1`代表`1%` |

## 验证中性网格参数

`POST /api/v3/trade/grid/validate-neutral`

创建网格中性策略前，校验网格参数（价格区间、格数、投入金额等）是否合法，不实际创建策略。

- 限频规则: 1次/秒/UID

- 需要统一账户交易权限

Operation ID: `utaGridValidateNeutral`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| category | string | 是 | 业务线<br><br>`USDT-FUTURES`：USDT保证金合约<br><br>`USDC-FUTURES`：USDC保证金合约 |
| symbol | string | 是 | 交易对 |
| maxPrice | string | 是 | 上限价格 |
| minPrice | string | 是 | 下限价格 |
| gridNum | string | 是 | 网格格数 |
| gridOrderMode | string | 是 | 网格模式<br><br>`arithmetic`：等差<br><br>`geometric`：等比 |
| leverage | string |  | 杠杆 |
| investmentAmount | object[] |  | 投入币种及金额列表，合约仅支持计价币USDT/USDC |
| investmentAmount[].coin | string | 是 | 投入币种 |
| investmentAmount[].amount | string | 是 | 投入金额 |
| triggerPrice | string |  | 触发价格 |
| stopLoss | string |  | 止损价格 |
| takeProfit | string |  | 止盈价格 |
| autoTransferProfits | string |  | 是否自动转出利润 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.valid | string |  | 是否校验通过 |
| data.reason | string |  | 校验失败原因 |
| data.minInvestment | string |  | 最小投入金额 |

## 验证网格输入

`POST /api/v3/trade/grid/validate`

创建网格策略前，校验网格参数（价格区间、格数、投入金额等）是否合法，不实际创建策略。

- 限频规则: 1次/秒/UID

- 需要统一账户交易权限

Operation ID: `utaGridValidate`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| category | string | 是 | 业务线<br><br>`SPOT`：现货交易<br><br>`USDT-FUTURES`：U本位合约<br><br>`USDC-FUTURES`：USDC合约 |
| symbol | string | 是 | 交易对名称 |
| gridType | string |  | 网格方向<br>`long`<br>`short`<br>`neutral`<br>**合约（`USDT-FUTURES` / `USDC-FUTURES`）必填；现货（`SPOT`）可选** |
| maxPrice | string | 是 | 网格上限价格 |
| minPrice | string | 是 | 网格下限价格 |
| gridNum | string | 是 | 网格格数 |
| gridOrderMode | string | 是 | 网格挂单模式<br><br>`arithmetic`：等差<br><br>`geometric`：等比 |
| leverage | string |  | 杠杆倍数，默认1，仅合约生效 |
| investmentAmount | object[] | 是 | 投入金额 |
| investmentAmount[].coin | string | 是 | 币种 |
| investmentAmount[].amount | string | 是 | 金额 |
| reservedMargin | string |  | 预留保证金，仅合约生效 |
| triggerCondition | string |  | 触发条件，默认`instant`<br><br>`instant`<br><br>`price`<br><br>`rsi`<br><br>`boll` |
| triggerParams | object[] |  | 触发参数 |
| triggerParams[].indicatorLength | string |  | 指标周期 |
| triggerParams[].threshold | string |  | 阈值 |
| triggerParams[].multiplier | string |  | 倍数 |
| triggerParams[].interval | string |  | 周期 |
| triggerPrice | string |  | 触发价格 |
| terminationCondition | string |  | 终止条件<br><br>`rsi`<br><br>`boll` |
| terminationParams | object[] |  | 终止参数 |
| terminationParams[].indicatorLength | string |  | 指标周期 |
| terminationParams[].threshold | string |  | 阈值 |
| terminationParams[].multiplier | string |  | 倍数 |
| terminationParams[].interval | string |  | 周期 |
| stopLoss | string |  | 止损价格 |
| takeProfit | string |  | 止盈价格 |
| trailingGrid | string |  | 移动网格，默认`no`<br><br>`yes`<br><br>`no` |
| movingAverageGains | string |  | 移动平均收益 |
| stopUpwardPrice | string |  | 上移止损价格 |
| hodlMode | string |  | 屯币模式，默认`no`，仅现货生效<br><br>`yes`<br><br>`no` |
| marketOpen | string |  | 市价开仓，默认开启，仅合约生效<br><br>`yes`<br><br>`no` |
| lossReserve | string |  | 亏损预留，默认开启，仅合约生效<br><br>`yes`<br><br>`no` |
| autoTransferProfits | string | 是 | 自动转出利润，默认`no`<br><br>`yes`<br><br>`no` |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.valid | string |  | 是否校验通过 |
| data.reason | string |  | 校验失败原因 |
| data.minInvestment | string |  | 最小投入金额 |