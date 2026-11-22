---
exchange: bitget
source_url: https://www.bitget.com/docs/catalog/classic-contract-plan
api_type: REST
updated_at: 2026-11-22 19:01:01.748129
---

# Classic Contract Trigger API

Classic account — futures trigger/TP-SL orders.

版本: 1.0.0

## 服务地址

- `https://api.bitget.com`

## 接口列表

- `POST /api/v2/mix/order/modify-tpsl-order` — Modify the stop-profit and stop-loss plan order
- `POST /api/v2/mix/order/place-plan-order` — Place Trigger Order
- `POST /api/v2/mix/order/place-pos-tpsl` — Simultaneous Stop-profit and stop-loss plan orders
- `POST /api/v2/mix/order/place-tpsl-order` — Stop-profit and stop-loss plan orders
- `GET /api/v2/mix/order/plan-sub-order` — Trigger Sub Order
- `POST /api/v2/mix/order/modify-plan-order` — Modify Trigger Order
- `POST /api/v2/mix/order/cancel-plan-order` — Cancel Trigger Order
- `GET /api/v2/mix/order/orders-plan-pending` — Get Pending Trigger Order
- `GET /api/v2/mix/order/orders-plan-history` — Get History Trigger Order

## Modify the stop-profit and stop-loss plan order

`POST /api/v2/mix/order/modify-tpsl-order`

Speed limit is 10 times/s (UID)

Modify the stop-profit and stop-loss plan order

Operation ID: `classicContractPlanModifyTpslOrder`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| orderId | string |  | Take profit and stop loss order number, 'orderId' and 'clientOid' must provide one |
| clientOid | string |  | Take profit and stop loss client order number, 'orderId' and 'clientOid' must provide one |
| marginCoin | string | 是 | Margin currency |
| productType | string | 是 | Product type<br><br>`USDT-FUTURES` USDT-M Futures<br><br>`COIN-FUTURES` Coin-M Futures<br><br>`USDC-FUTURES` USDC-M Futures |
| symbol | string | 是 | Trading pair, e.g. ETHUSDT |
| triggerPrice | string | 是 | trigger price |
| triggerType | string |  | Trigger type (fill_price (transaction price) mark_price (mark price) |
| executePrice | string |  | Execution price (if it is 0 or not filled in, it means market price execution. If it is greater than 0, it means limit price execution. When planType (stop-profit and stop-loss type) is moving_plan (moving take-profit and stop-loss), it is not filled in and is fixed to the market price. implement.) |
| size | string | 是 | Order quantity<br><br>For the position take profit and position stop loss orders, the size should be `"size":""` |
| rangeRate | string |  | callback range<br><br>Value range: [0.01, 10]<br><br>Precision: 2 decimal places |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.orderId | string |  | Trigger order ID |
| data.clientOid | string |  | Customized trigger order ID |

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

## Place Trigger Order

`POST /api/v2/mix/order/place-plan-order`

Rate limit: 10 req/sec/UID

The interface for placing an trigger or trailing stop order with TP/SL setting feature.

**API Broker rebate identifier**:

  The following code block needs to be added to the HTTP Header of the request.

  > "X-CHANNEL-API-CODE":"your-channel-api-code"

Operation ID: `classicContractPlanPlacePlanOrder`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| planType | string | 是 | Trigger order type<br><br>`normal_plan`: Trigger order<br><br>`track_plan`: Trailing stop order |
| symbol | string | 是 | Trading pair, e.g. ETHUSDT |
| productType | string | 是 | Product type<br><br>`USDT-FUTURES` USDT-M Futures<br><br>`COIN-FUTURES` Coin-M Futures<br><br>`USDC-FUTURES` USDC-M Futures |
| marginMode | string | 是 | Position mode<br><br>`isolated`: isolated margin <br><br>`crossed`: cross margin |
| marginCoin | string | 是 | Margin coin |
| size | string | 是 | Amount(base coin) |
| price | string |  | Price<br><br>1. For `track_plan`, it must be empty.<br><br>2. For `normal_plan`, it is required when orderType is `limit`;It must be empty when orderType is `market`. |
| callbackRatio | string |  | Callback rate (applies to trailing stop orders only)<br><br>1. Required for trailing stop orders and the rate cannot be greater than 10. |
| triggerPrice | string | 是 | Trigger price |
| triggerType | string | 是 | Trigger type<br><br>1. Required when placing a trigger order or a trailing stop order.<br><br>mark_price: Mark price<br><br>fill_price: Lastest price |
| side | string | 是 | Order direction<br><br>`buy`; `sell` |
| tradeSide | string |  | Direction<br><br>`open`: Open; `close`: Close<br><br>1. Only required in hedge position mode<br><br>Notes:<br><br>For open long, "side" fill in "buy"; tradeSide should be "open" <br><br>For open short, "side" fill in "sell"; tradeSide should be "open" <br><br>For close long, "side" fill in "buy"; "tradeSide" should be "close" <br><br>For close short, "side" fill in "sell"; "tradeSide" should be "close" |
| orderType | string | 是 | Order type<br><br>`limit`: limit order<br><br>`market`: market order<br><br> 1. For `track_plan`, it is required and must be `market` |
| clientOid | string |  | Customize order ID |
| reduceOnly | string |  | Whether or not to just reduce the position.<br><br>`yes`: Yes; `no`: No(default)<br><br>1. Only applicable in buy/sell (one-way position) mode |
| stopSurplusTriggerPrice | string |  | Take-profit trigger price/Take-profit  trigger percentage return rate<br><br>1. For `normal_plan`, it represents the take-profit trigger price<br><br>2. For `track_plan`, it represents the take-profit percentage, with a maximum of 999.99 and a minimum of 0.01<br><br>3. If left empty or set to 0, no take-profit will be set by default |
| stopSurplusExecutePrice | string |  | Take-profit execute price<br><br>1. For `track_plan`, it must be empty.<br><br>2. For a `normal_plan` that has stopSurplusTriggerPrice parameter set, if it is empty or set to 0, it represents a market order execution; if not empty and greater than 0, it represents a limit order execution |
| stopSurplusTriggerType | string |  | Take-profit trigger type<br><br>`fill_price`: Lastest price<br><br>`mark_price`: Mark price<br><br>1. For orders that have stopSurplusTriggerPrice parameter set, it is required<br><br>2. For `track_plan`, it only accepts `fill_price` |
| stopLossTriggerPrice | string |  | Stop-loss trigger price/Stop-loss  trigger percentage return rate<br><br>1. For `normal_plan`, it represents the stop-loss trigger price<br><br>2. For `track_plan`, it represents the stop-loss percentage, with a maximum of 999.99 and a minimum of 0.01<br><br>3. If left empty or set to 0, no stop-loss will be set by default |
| stopLossExecutePrice | string |  | Stop-loss execute price<br><br>1. For `track_plan`, it must be empty.<br><br>2. For a `normal_plan` that has stopLossTriggerPrice parameter set, if it is empty or set to 0, it represents a market order execution; if not empty and greater than 0, it represents a limit order execution |
| stopLossTriggerType | string |  | Stop-loss trigger type<br><br>`fill_price`: Lastest price<br><br>`mark_price`: Mark price<br><br>1. For orders that have stopLossTriggerPrice parameter set, it is required<br><br>2. For `track_plan`, it only accepts `fill_price` |
| stpMode | string |  | STP Mode <br><br> `none` not setting STP(default) <br><br> `cancel_taker` cancel taker order <br><br>  `cancel_maker` cancel maker order <br><br>  `cancel_both` cancel both of taker and maker orders |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.orderId | string |  | Trigger order ID |
| data.clientOid | string |  | Customized trigger order ID |

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

## Simultaneous Stop-profit and stop-loss plan orders

`POST /api/v2/mix/order/place-pos-tpsl`

Speed limit is 10 times/s (UID)

Place a stop-profit and stop-loss plan order

**API Broker rebate identifier**:

  The following code block needs to be added to the HTTP Header of the request.

  > "X-CHANNEL-API-CODE":"your-channel-api-code"

Operation ID: `classicContractPlanPlacePosTpslOrder`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| marginCoin | string | 是 | Margin currency |
| productType | string | 是 | Product type<br><br>`USDT-FUTURES` USDT-M Futures<br><br>`COIN-FUTURES` Coin-M Futures<br><br>`USDC-FUTURES` USDC-M Futures |
| symbol | string | 是 | Trading pair, e.g. ETHUSDT |
| stopSurplusTriggerPrice | string |  | Take Profit Trigger price |
| stopSurplusSize | string |  | Order quantity(base coin)，if filled it's profit_plan，if not filled，it's pos_profit |
| stopSurplusTriggerType | string |  | Take Profit Trigger type<br><br>fill_price: market price;<br><br>mark_price: mark price |
| stopSurplusExecutePrice | string |  | Take Profit Execution price<br><br>If it is 0 or not filled in, it means market price execution.If it is greater than 0, it means limit price execution. |
| stopLossTriggerPrice | string |  | Stop Loss Trigger price |
| stopLossSize | string |  | Order quantity(base coin)，if filled it's loss_plan，if not filled，it's pos_loss |
| stopLossTriggerType | string |  | Stop Loss Trigger type<br><br>fill_price: market price;<br><br>mark_price: mark price |
| stopLossExecutePrice | string |  | Stop Loss Execution price<br><br>If it is 0 or not filled in, it means market price execution.If it is greater than 0, it means limit price execution. |
| holdSide | string | 是 | Two-way position:(long: long position, short: short position)<br><br>one-way position: (buy: long position, sell: short position) |
| stpMode | string |  | STP Mode, default `none` <br><br> `none` not setting STP <br><br> `cancel_taker` cancel taker order <br><br>  `cancel_maker` cancel maker order <br><br>  `cancel_both` cancel both of taker and maker orders |
| stopSurplusClientOid | string |  | Take-profit order custom order ID |
| stopLossClientOid | string |  | Stop-loss order custom order ID |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].orderId | string |  | Trigger order ID |
| data[].stopSurplusClientOid | string |  | Take-profit order custom order ID |
| data[].stopLossClientOid | string |  | Stop-loss order custom order ID |

```json
{
  "code": "00000",
  "data": [
    {
      "orderId": "xxxxxxxx",
      "stopSurplusClientOid": "xxxxxxxx",
      "stopLossClientOid": "xxxxxxxx"
    },
    {
      "orderId": "xxxxxxxx",
      "stopSurplusClientOid": "xxxxxxxx",
      "stopLossClientOid": "xxxxxxxx"
    }
  ],
  "msg": "success",
  "requestTime": 1627293504612
}
```

## Stop-profit and stop-loss plan orders

`POST /api/v2/mix/order/place-tpsl-order`

Speed limit is 10 times/s (UID)

Place a stop-profit and stop-loss plan order

**API Broker rebate identifier**:

  The following code block needs to be added to the HTTP Header of the request.

  > "X-CHANNEL-API-CODE":"your-channel-api-code"

Operation ID: `classicContractPlanPlaceTpslOrder`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| marginCoin | string | 是 | Margin currency (Capitalized) |
| productType | string | 是 | Product type<br><br>`USDT-FUTURES` USDT-M Futures<br><br>`COIN-FUTURES` Coin-M Futures<br><br>`USDC-FUTURES` USDC-M Futures |
| symbol | string | 是 | Trading pair, e.g. ETHUSDT |
| planType | string | 是 | Take profit and stop loss type<br><br>profit_plan: take profit plan;<br><br>loss_plan: stop loss plan;<br><br>moving_plan: trailing stop;<br><br>pos_profit: position take profit;<br><br>pos_loss: position stop loss |
| triggerPrice | string | 是 | Trigger price |
| triggerType | string |  | Trigger type<br><br>fill_price: market price;<br><br>mark_price: mark price |
| executePrice | string |  | Execution price<br><br>If it is 0 or not filled in, it means market price execution.If it is greater than 0, it means limit price execution.<br><br>Do not fill in this parameters when `planType` is moving_plan, it only executs in market price. |
| holdSide | string | 是 | Two-way position:(long: long position, short: short position)<br><br>one-way position: (buy: long position, sell: short position) |
| size | string | 是 | Order quantity(base coin)<br><br>It's required when `planType` is profit_plan, loss_plan or moving_plan,and should be greater than 0;<br><br>It's NOT required when `planType` is pos_profit or pos_loss |
| rangeRate | string |  | Callback range<br><br>It's required only in `planType` is moving_plan<br><br>Value range: [0.01, 10]<br><br>Precision: 2 decimal places |
| clientOid | string |  | Customize order ID |
| stpMode | string |  | STP Mode, default `none` <br><br> `none` not setting STP <br><br> `cancel_taker` cancel taker order <br><br>  `cancel_maker` cancel maker order <br><br>  `cancel_both` cancel both of taker and maker orders |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.orderId | string |  | Trigger order ID |
| data.clientOid | string |  | Customized trigger order ID |

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

## Trigger Sub Order

`GET /api/v2/mix/order/plan-sub-order`

Rate limit: 10 req/sec/UID

Get trigger executed futures orders

Operation ID: `classicContractPlanPlanSubOrders`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| planType | query | string | 是 | Trigger order type<br><br>normal_plan: average trigger order<br><br>track_plan: trailing stop order |
| planOrderId | query | string | 是 | Trigger order ID |
| productType | query | string | 是 | Product type<br><br>`USDT-FUTURES` USDT-M Futures<br><br>`COIN-FUTURES` Coin-M Futures<br><br>`USDC-FUTURES` USDC-M Futures |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].orderId | string |  | Futures order ID |
| data[].price | string |  | Price of the futures order |
| data[].type | string |  | Order type<br><br>limit<br><br>market |
| data[].status | string |  | Plan order trigger status<br><br>success: trigger success<br><br>fail: trigger failed<br><br>cancelled: cancelled<br><br>in_progress: trigger spot placing order<br><br>in_progress_tracking: tracking trigger |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1710813939206,
  "data": [
    {
      "orderId": "xxxxxxxxxxxxx",
      "price": "0.4188",
      "type": "limit",
      "status": "success"
    }
  ]
}
```

## Modify Trigger Order

`POST /api/v2/mix/order/modify-plan-order`

Speed limit is 10 times/s (UID)

Interface for trigger order modification, used to modify an pending order, such as its TP/SL and/or triggerPrice.

Operation ID: `classicContractPlanModifyPlanOrder`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| orderId | string |  | Trigger order ID<br><br>Either orderId or clientOid is required. If both are entered, orderId prevails. |
| clientOid | string |  | Customized trigger order ID<br><br>Either orderId or clientOid is required. If both are entered, orderId prevails. |
| productType | string | 是 | Product type<br><br>`USDT-FUTURES` USDT-M Futures<br><br>`COIN-FUTURES` Coin-M Futures<br><br>`USDC-FUTURES` USDC-M Futures |
| newSize | string |  | Amount of the modified transaction<br><br>If it is empty, the amount remains unchanged. |
| newPrice | string |  | Modified price for executing orders.<br><br>1: When the original order is a trigger order and its type is Limit, the original price remains unchanged when this field is empty.<br><br>Must be empty if the order type is Market.<br><br>2: When the original order is a trailing order, it must be empty. |
| newCallbackRatio | string |  | Modified callback rate (for trailing stop orders only)<br><br>1. When the original order is a trailing stop order, it must be filled in, and the rate must not be greater than 10.<br><br>2: When the original order is a trigger order, it must be empty. |
| newTriggerPrice | string |  | Modified trigger price<br><br>1. When the original order is a trigger order or a trailing stop order, if the field is not set, the price stays unchanged; if it is set, the price updates. |
| newTriggerType | string |  | Modified trigger type<br><br>1. When the original order is a trigger order or a trailing stop order, if the field is not set, the type stays unchanged; if it is set, the type updates.<br><br>Setting this parameter requires the setting of newTriggerPrice.<br><br>fill_price: filled price<br><br>mark_price: mark price |
| newStopSurplusTriggerPrice | string |  | Modified take-profit trigger price<br><br>1. If the field is left empty: when the original order has the TP set, the original value will be maintained.<br><br>2. If it is not empty: when the original order has the TP set, the TP will update; when the original order doesn't have the TP set, the TP will be added. If 0 is filled in, the original TP setting will be removed. |
| newStopSurplusExecutePrice | string |  | Modified take-profit strike price<br><br>1. This parameter must be empty when the original order is a trailing stop order.<br><br>2.For a trigger order, if this field is filled in, the price will update; if not filled in, the price stays unchanged; if 0 is filled in, the price setting will be removed. |
| newStopSurplusTriggerType | string |  | Modified take-profit trigger type<br><br>Default to the transaction price<br><br>1. This parameter must be empty when the original order is a trailing stop order.<br><br>2. For a trigger order that has newStopSurplusTriggerPrice parameter set, it is required.<br><br>fill_price: filled price<br><br>mark_price: mark price |
| newStopLossTriggerPrice | string |  | Modified stop-loss trigger price<br><br>1. If the field is left empty: when the original order has the SL set, the original value will be maintained.<br><br>2. If it is not empty: when the original order has the SL set, the SL will update; when the original order doesn't have the SL set, the SL will be added. If 0 is filled in, the original SL setting will be removed. |
| newStopLossExecutePrice | string |  | Modified stop-loss strike price<br><br>1. This parameter must be empty when the original order is a trailing stop order.<br><br>2.For a trigger order, if this field is filled in, the price will update; if not filled in, the price stays unchanged; if 0 is filled in, the SL setting will be removed. |
| newStopLossTriggerType | string |  | Modified stop-loss trigger type<br><br>Default to the transaction price<br><br>1. This parameter must be empty when the original order is a trailing stop order.<br><br>2. For a trigger order that has newStopLossTriggerPrice parameter set, it is required.<br><br>fill_price: filled price<br><br>mark_price: mark price |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.orderId | string |  | Trigger order ID |
| data.clientOid | string |  | Customized trigger order ID |

```json
{
  "code": "00000",
  "data": {
    "orderId": "21627293504612",
    "clientOid": "BITGET#1627293504612"
  },
  "msg": "success",
  "requestTime": 1627293504612
}
```

## Cancel Trigger Order

`POST /api/v2/mix/order/cancel-plan-order`

Speed limit is 10 times/s (UID)

Interface for cancelling trigger orders, can be used to cancel by 'productType', 'symbol' and/or trigger ID list.

All orders that fall under that'productType' and 'symbol' will be cancelled.

Operation ID: `classicContractPlanCancelPlanOrder`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| orderIdList | object[] |  | Trigger order id list.<br><br>If it is passed, symbol must not be null and must be aligned with symbol/productType/planType. |
| orderIdList[].orderId | string |  | Trigger order ID<br><br>Either orderId or clientOid is required. If both are entered, orderId prevails. |
| orderIdList[].clientOid | string |  | Customized trigger order ID<br><br>Either orderId or clientOid is required. If both are entered, triggerId prevails. |
| symbol | string |  | Trading pair, e.g. ETHUSDT |
| productType | string | 是 | Product type<br><br>`USDT-FUTURES` USDT-M Futures<br><br>`COIN-FUTURES` Coin-M Futures<br><br>`USDC-FUTURES` USDC-M Futures |
| marginCoin | string |  | Margin coin must be capitalized |
| planType | string |  | Trigger order type<br><br>normal_plan plan order(default)<br><br>profit_plan batch profit  order <br><br>loss_plan batch loss order <br><br>pos_profit position profit order <br><br> pos_loss position loss order <br><br> moving_plan trailing order |

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

```json
{
  "code": "00000",
  "data": {
    "successList": [
      {
        "orderId": "121212121212",
        "clientOid": "123"
      },
      {
        "orderId": "123",
        "clientOid": ""
      }
    ],
    "failureList": [
      {
        "orderId": "3",
        "clientOid": "123",
        "errorMsg": "notExistend"
      },
      {
        "orderId": "21221",
        "clientOid": "",
        "errorMsg": "notExistend"
      }
    ]
  },
  "msg": "success",
  "requestTime": 1627293504612
}
```

## Get Pending Trigger Order

`GET /api/v2/mix/order/orders-plan-pending`

Rate limit: 10 req/sec/UID

Can be used to query one or all current trigger orders.

Operation ID: `classicContractPlanGetOrdersPlanPending`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| orderId | query | string |  | Trigger order ID<br><br>Either orderId or clientOid is required. If both are entered, orderId prevails. |
| clientOid | query | string |  | Customized trigger order ID<br><br>Either orderId or clientOid is required. If both are entered, orderId prevails. |
| symbol | query | string |  | Trading pair, e.g. ETHUSDT |
| planType | query | string | 是 | Trigger order type<br><br>normal_plan: average trigger order<br><br>track_plan: trailing stop order <br><br> profit_loss: take profit and stop loss orders(including the profit_plan, loss_plan, moving_plan, pos_profit and pos_loss) |
| productType | query | string | 是 | Product type<br><br>`USDT-FUTURES` USDT-M Futures<br><br>`COIN-FUTURES` Coin-M Futures<br><br>`USDC-FUTURES` USDC-M Futures |
| idLessThan | query | string |  | Requests the content on the page before this ID (older data), the value input should be the endId of the corresponding interface. |
| startTime | query | string |  | Start timestamp <br><br>Unix timestamp in milliseconds format, e.g. 1597026383085<br><br>(The maximum time span supported is three months. The default end time is three months if no value is set for the end time. ) |
| endTime | query | string |  | End timestamp <br><br>Unix timestamp in milliseconds format, e.g. 1597026383085<br><br>(The maximum time span supported is three months. The default start time is three months ago if no value is set for the start time. ) |
| limit | query | string |  | Number of queries: Default: 100, maximum: 100 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.entrustedList | object[] |  | Order list |
| data.entrustedList[].planType | string |  | Trigger order type<br><br>normal_plan: average trigger order<br><br>track_plan: trailing stop order |
| data.entrustedList[].symbol | string |  | Trading pair |
| data.entrustedList[].size | string |  | Amount |
| data.entrustedList[].orderId | string |  | Trigger order ID |
| data.entrustedList[].clientOid | string |  | Customized trigger order ID |
| data.entrustedList[].price | string |  | Order execute price<br><br>For a common trigger order, it represents the order execute price.<br><br>For a trailing stop order, the value doesn't exist. |
| data.entrustedList[].executePrice | string |  | Execute Price |
| data.entrustedList[].callbackRatio | string |  | Implementation of the callback rate. (Range 1-10)<br><br>Only exists when the order is a trailing stop order. |
| data.entrustedList[].triggerPrice | string |  | Trigger price<br><br>It appears for both common trigger orders and trailing stop orders. |
| data.entrustedList[].triggerType | string |  | Trigger type<br><br>It appears for both common trigger orders and trailing stop orders.<br><br>fill_price: filled price<br><br>mark_price: mark price<br><br>index_price: index price |
| data.entrustedList[].planStatus | string |  | Order status<br><br>For a current trigger order, the status will only be `live` |
| data.entrustedList[].side | string |  | Direction<br><br>Buy; Sell |
| data.entrustedList[].posSide | string |  | Position direction<br><br>long: hedge mode long position<br><br>short: hedge mode short position<br><br>net: one-way position |
| data.entrustedList[].marginCoin | string |  | Margin coin |
| data.entrustedList[].marginMode | string |  | Margin mode<br><br>`isolated`: isolated margin mode<br><br>`crossed`: crossed margin |
| data.entrustedList[].enterPointSource | string |  | Order source<br><br>WEB: Orders created on the website<br><br>API: Orders created on API<br><br>SYS: System managed orders, usually generated by forced liquidation logic<br><br>ANDROID: Orders created on the Android app<br><br>IOS: Orders created on the iOS app |
| data.entrustedList[].tradeSide | string |  | Direction<br><br>open: Open (hedge-mode)<br><br>close: Close (hedge-mode) |
| data.entrustedList[].posMode | string |  | Position mode<br><br>one_way_mode: one-way mode<br><br>hedge_mode: hedge mode |
| data.entrustedList[].orderType | string |  | Order type<br><br>`limit`: limit order<br><br>`market`: market order |
| data.entrustedList[].orderSource | string |  | Order sources<br><br>normal: Normal order<br><br>market: Market order<br><br>profit_market: Market TP order<br><br>loss_market: Market SL order<br><br>Trader_delegate: Elite trade order<br><br>trader_profit: Trader takes profit<br><br>trader_loss: Trader stops loss<br><br>trader_reverse: Reversed elite trades<br><br>profit_limit: Take-profit limit order<br><br>loss_limit: Stop-loss limit order<br><br>delivery_close_short: close short positions<br><br>pos_profit_limit: Position take-profit limit order<br><br>pos_profit_market: Position take-profit market order<br><br>pos_loss_limit: Position stop-loss limit order<br><br>pos_loss_market: Position stop-loss market order |
| data.entrustedList[].cTime | string |  | Creation time |
| data.entrustedList[].uTime | string |  | Last updated |
| data.entrustedList[].stopSurplusExecutePrice | string |  | Setting take profit execution price |
| data.entrustedList[].stopSurplusTriggerPrice | string |  | Setting take-profit trigger price |
| data.entrustedList[].stopSurplusTriggerType | string |  | Setting take-profit trigger type<br><br>fill_price: filled price<br><br>mark_price: mark price<br><br>index_price: index price |
| data.entrustedList[].stopLossExecutePrice | string |  | Setting stop loss execution price |
| data.entrustedList[].stopLossTriggerPrice | string |  | Setting stop-loss trigger price |
| data.entrustedList[].stopLossTriggerType | string |  | Setting stop-loss trigger type<br><br>fill_price: filled price<br><br>mark_price: mark price<br><br>index_price: index price |
| data.endId | string |  | This is used when idLessThan/idGreaterThan is set as a range. |

```json
{
  "code": "00000",
  "data": {
    "entrustedList": [
      {
        "planType": "normal_plan",
        "symbol": "ethusdt",
        "size": "1",
        "orderId": "123",
        "clientOid": "121212",
        "price": "1900",
        "executePrice": "1900",
        "callbackRatio": "",
        "triggerPrice": "1901",
        "triggerType": "mark_price",
        "planStatus": "not_trigger",
        "side": "buy",
        "posSide": "long",
        "marginCoin": "usdt",
        "marginMode": "crossed",
        "enterPointSource": "api",
        "tradeSide": "open",
        "posMode": "hedge_mode",
        "orderType": "limit",
        "orderSource": "normal",
        "cTime": "1627293504612",
        "uTime": "",
        "stopSurplusExecutePrice": "2001",
        "stopSurplusTriggerPrice": "2002",
        "stopSurplusTriggerType": "fill_price",
        "stopLossExecutePrice": "1800",
        "stopLossTriggerPrice": "1820",
        "stopLossTriggerType": "fill_price"
      }
    ],
    "endId": "123"
  },
  "msg": "success",
  "requestTime": 1627293504612
}
```

## Get History Trigger Order

`GET /api/v2/mix/order/orders-plan-history`

Speed limit is 10 times/s (UID)

Can be used to query one or all previous common orders and trigger orders.

Operation ID: `classicContractPlanOrdersPlanHistory`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| orderId | query | string |  | Order ID<br><br>Either orderId or clientOid is required. If both are entered, orderId prevails. |
| clientOid | query | string |  | Customize order ID<br><br>Either orderId or clientOid is required. If both are entered, orderId prevails. |
| planType | query | string | 是 | Order type<br><br>`normal_plan`: trigger order<br><br>`track_plan`: trailing stop order<br><br>`profit_loss`: take profit and stop loss orders(including the profit_plan, loss_plan, moving_plan, pos_profit and pos_loss) |
| planStatus | query | string |  | Trigger order status<br><br>If not specified, all states will be queried<br><br>executed: the order triggered<br><br>fail_execute: Failed to trigger<br><br>cancelled: Cancelled |
| symbol | query | string |  | Trading pair, e.g. ETHUSDT |
| productType | query | string | 是 | Product type<br><br>`USDT-FUTURES` USDT-M Futures<br><br>`COIN-FUTURES` Coin-M Futures<br><br>`USDC-FUTURES` USDC-M Futures |
| idLessThan | query | string |  | Requests the content on the page before this ID (older data), the value input should be the endId of the corresponding interface. |
| startTime | query | string |  | Start timestamp <br><br>Unix timestamp in milliseconds format, e.g. 1597026383085<br><br>(The maximum time span supported is three months. The default end time is three months if no value is set for the end time. ) <br><br> (For Managed Sub-Account, the StartTime cannot be earlier than the binding time) |
| endTime | query | string |  | End timestamp <br><br>Unix timestamp in milliseconds format, e.g. 1597026383085<br><br>(The maximum time span supported is three months. The default start time is three months ago if no value is set for the start time. ) |
| limit | query | string |  | Number of queries: Default: 100, maximum: 100 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.entrustedList | object[] |  | Order list |
| data.entrustedList[].planType | string |  | Trigger order type<br><br>normal_plan: average trigger order<br><br>track_plan: trailing stop order |
| data.entrustedList[].symbol | string |  | Trading pair |
| data.entrustedList[].size | string |  | Amount |
| data.entrustedList[].orderId | string |  | Trigger order ID |
| data.entrustedList[].executeOrderId | string |  | the order ID after plan triggered |
| data.entrustedList[].clientOid | string |  | Customized trigger order ID |
| data.entrustedList[].planStatus | string |  | Order status<br><br>`executed`: the order triggered<br><br>`fail_execute`: Failed to trigger<br><br>`cancelled`: Cancelled |
| data.entrustedList[].price | string |  | Order price<br><br>For a common trigger order, it represents the order price.<br><br>For a trailing stop order, this field doesn't exist. |
| data.entrustedList[].executePrice | string |  | Execute Price |
| data.entrustedList[].baseVolume | string |  | Amount of coins traded<br><br>It is only available when the order status is triggered. |
| data.entrustedList[].triggerPrice | string |  | Trigger price<br><br>It appears for both common trigger orders and trailing stop orders. |
| data.entrustedList[].triggerType | string |  | Trigger type<br><br>It appears for both common trigger orders and trailing stop orders.<br><br>fill_price: filled price<br><br>mark_price: mark price |
| data.entrustedList[].side | string |  | Direction<br><br>Buy; Sell |
| data.entrustedList[].posSide | string |  | Position direction<br><br>`long`: hedge mode long position<br><br>`short`: hedge mode short position<br><br>`net`: one-way position |
| data.entrustedList[].marginCoin | string |  | Margin coin |
| data.entrustedList[].marginMode | string |  | Margin mode<br><br>`isolated`: isolated margin<br><br>`crossed`: cross margin |
| data.entrustedList[].enterPointSource | string |  | Order source<br><br>WEB: Orders created on the website<br><br>API: Orders created on API<br><br>SYS: System managed orders, usually generated by forced liquidation logic<br><br>ANDROID: Orders created on the Android app<br><br>IOS: Orders created on the iOS app |
| data.entrustedList[].tradeSide | string |  | Direction<br><br>open (open and close mode)<br><br>close: Close (open and close mode) |
| data.entrustedList[].posMode | string |  | Position mode<br><br>one_way_mode: one-way mode<br><br>hedge_mode: hedge mode |
| data.entrustedList[].orderType | string |  | Order type<br><br>limit: limit order<br><br>market |
| data.entrustedList[].cTime | string |  | Creation time |
| data.entrustedList[].uTime | string |  | Last updated time |
| data.entrustedList[].stopSurplusExecutePrice | string |  | Setting take-profit strike price |
| data.entrustedList[].stopSurplusTriggerPrice | string |  | Setting take-profit trigger price |
| data.entrustedList[].stopSurplusTriggerType | string |  | Setting take-profit trigger type<br><br>fill_price: filled price<br><br>mark_price: mark price |
| data.entrustedList[].stopLossExecutePrice | string |  | Setting stop-loss strike price |
| data.entrustedList[].stopLossTriggerPrice | string |  | Setting stop-loss trigger price |
| data.entrustedList[].stopLossTriggerType | string |  | Setting stop-loss trigger type<br><br>fill_price: filled price<br><br>mark_price: mark price |
| data.callbackRatio | string |  | Implementation of the callback rate. (Maximum 1-10)<br><br>Only exists for trailing stop orders. |
| data.endId | string |  | The last Trigger order  ID.<br><br>This is used when idLessThan/idGreaterThan is set as a range. |

```json
{
  "code": "00000",
  "data": {
    "entrustedList": [
      {
        "planType": "normal_plan",
        "symbol": "ethusdt",
        "size": "1",
        "orderId": "123",
        "executeOrderId": "123456",
        "clientOid": "",
        "planStatus": "executed",
        "price": "1990",
        "executePrice": "1990",
        "priceAvg": "1999.2",
        "baseVolume": "1",
        "callbackRatio": "",
        "triggerPrice": "1989",
        "triggerType": "fill_price",
        "side": "buy",
        "posSide": "long",
        "marginCoin": "usdt",
        "marginMode": "crossed",
        "enterPointSource": "api",
        "tradeSide": "open",
        "posMode": "hedge_mode",
        "orderType": "limit",
        "cTime": "1627293504612",
        "uTime": "",
        "stopSurplusExecutePrice": "2001",
        "stopSurplusTriggerPrice": "2002",
        "stopSurplusTriggerType": "fill_price",
        "stopLossExecutePrice": "1800",
        "stopLossTriggerPrice": "1820",
        "stopLossTriggerType": "fill_price"
      }
    ],
    "endId": "123"
  },
  "msg": "success",
  "requestTime": 1627293504612
}
```


---

经典账户 — 合约计划委托与止盈止损。

版本: 1.0.0

## 服务地址

- `https://api.bitget.com`

## 接口列表

- `POST /api/v2/mix/order/modify-tpsl-order` — 修改止盈止损计划委托
- `POST /api/v2/mix/order/place-plan-order` — 计划委托下单
- `POST /api/v2/mix/order/place-pos-tpsl` — 支持止盈止损计划委托同时下单
- `POST /api/v2/mix/order/place-tpsl-order` — 止盈止损计划委托下单
- `GET /api/v2/mix/order/plan-sub-order` — 获取计划委托触发条件单
- `POST /api/v2/mix/order/modify-plan-order` — 修改计划委托
- `GET /api/v2/mix/order/orders-plan-pending` — 获取当前计划委托
- `POST /api/v2/mix/order/cancel-plan-order` — 计划委托撤单
- `GET /api/v2/mix/order/orders-plan-history` — 查询历史计划委托

## 修改止盈止损计划委托

`POST /api/v2/mix/order/modify-tpsl-order`

普通用户10次/S 根据uid限频

修改止盈止损计划委托

Operation ID: `classicContractPlanModifyTpslOrder`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| orderId | string |  | 止盈止损订单号, 'orderId' 与 'clientOid' 必需提供一个 |
| clientOid | string |  | 止盈止损客户端订单号，'orderId' 与 'clientOid' 必需提供一个 |
| marginCoin | string | 是 | 保证金币种 |
| productType | string | 是 | 产品类型<br><br>`USDT-FUTURES` U本位合约<br><br>`COIN-FUTURES` 币本位合约<br><br>`USDC-FUTURES` USDC合约 |
| symbol | string | 是 | 交易币对 |
| triggerPrice | string | 是 | 触发价格 |
| triggerType | string |  | 触发类型（fill_price （成交价格）  mark_price（标记价格） |
| executePrice | string |  | 执行价格 （若为0或不填则代表市价执行。若填写大于0，为限价执行。当planType（止盈止损类型）为moving_plan（移动止盈止损）时则不填，固定为市价执行。） |
| size | string | 是 | 下单数量<br><br>对于仓位止盈止损订单，size必须为空`"size":""` |
| rangeRate | string |  | 回调幅度<br><br>取值范围：[0.01, 10]<br><br>精度：小数点后2位 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.orderId | string |  | 计划委托订单id |
| data.clientOid | string |  | 自定义计划委托订单id |

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

## 计划委托下单

`POST /api/v2/mix/order/place-plan-order`

限频规则：10次/秒/UID

计划委托/追踪委托下单接口，支持预设止盈止损特性。

**API Broker返佣标识**:

  需在HTTP Header请求头中添加如下代码块

  > "X-CHANNEL-API-CODE":"your-channel-api-code"

Operation ID: `classicContractPlanPlacePlanOrder`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| planType | string | 是 | 计划委托类型<br><br>`normal_plan`: 普通计划委托<br><br>`track_plan`: 追踪委托 |
| symbol | string | 是 | 交易币对 如:ETHUSDT |
| productType | string | 是 | 产品类型<br><br>`USDT-FUTURES` U本位合约<br><br>`COIN-FUTURES` 币本位合约<br><br>`USDC-FUTURES` USDC合约 |
| marginMode | string | 是 | 仓位模式<br><br>`isolated`: 逐仓 <br><br>`crossed`: 全仓 |
| marginCoin | string | 是 | 保证金币种 |
| size | string | 是 | 下单数量 |
| price | string |  | 委托价格<br><br>1.若下追踪委托时，则必须为空。<br><br>2.若下普通计划委托时，订单类型(orderType)为限价单(limit)则必填，为市价单(market)时则为空。 |
| callbackRatio | string |  | 执行回调幅度（只适用追踪委托）<br><br>1.若下追踪委托时必填，且幅度不可大于10。 |
| triggerPrice | string | 是 | 触发价格 |
| triggerType | string | 是 | 触发类型<br><br>1.若下普通计划委托、追踪委托时必填<br><br>`mark_price`: 标记价格<br><br>`fill_price`: 成交价格 |
| side | string | 是 | 下单方向<br><br>`buy` 买，`sell` 卖 |
| tradeSide | string |  | 交易方向<br><br>1.双向持仓模式下必填，单向持仓模式不填<br><br>`open` 开，`close` 平<br><br>补充：<br><br>开多：side 填写 buy； tradeSide 填写 open <br><br>开空：side 填写 sell； tradeSide 填写 open <br><br>平多：side 填写 buy；tradeSide 填写 close <br><br>平空：side 填写 sell； tradeSide 填写 close |
| orderType | string | 是 | 订单类型<br><br>1.若下追踪委托时，只能填market<br><br>`limit` 限价单，<br><br>`market` 市价单 |
| clientOid | string |  | 自定义订单id |
| reduceOnly | string |  | 是否只减仓。<br><br>`yes`：是;`no`：否（默认）<br><br>1.仅适用于买卖（单向持仓）模式下。<br><br>2.开平仓（双向持仓）模式下必须为空或no。 |
| stopSurplusTriggerPrice | string |  | 止盈触发价/止盈触发百分比收益率<br><br>1.为普通委托时，代表止盈触发价；2.为追踪委托时，为止盈触发百分比，且最大比例必须小于等于999.99，最小0.01；3.为空或0则默认不设止盈 |
| stopSurplusExecutePrice | string |  | 止盈执行价格<br><br>1.若下追踪委托时，则必须为空。<br><br>2.若下普通计划委托时，同时携带了stopSurplusTriggerPrice参数，为空或为0，则代表市价订单执行；不为空且大于0则为限价执行 |
| stopSurplusTriggerType | string |  | 止盈触发类型<br><br>`fill_price` 成交价格<br><br>`mark_price` 标记价格<br><br>1.若携带了stopSurplusTriggerPrice参数，则必填<br><br>2. 若为追踪委托，则只支持`fill_price` |
| stopLossTriggerPrice | string |  | 止损触发价/止损触发百分比收益率<br><br>1.为普通委托时，代表止损触发价<br><br>2.为追踪委托时，为止损触发百分比，且最大比例必须小于等于999.99，最小0.01<br><br>3.为空或0则默认不设止损 |
| stopLossExecutePrice | string |  | 止损执行价格<br><br>1.若下追踪委托时，则必须为空。<br><br>2.若下普通计划委托时，同时携带了stopLossTriggerPrice参数，为空或为0，则代表市价订单执行；不为空且大于0则为限价执行 |
| stopLossTriggerType | string |  | 止损触发类型<br><br>`fill_price` 成交价格<br><br>`mark_price` 标记价格<br><br>1.若携带了stopLossTriggerPrice参数，则必填<br><br>2. 若为追踪委托，则只支持`fill_price` |
| stpMode | string |  | STP模式<br><br> `none` 不设置STP（默认） <br><br> `cancel_taker` 取消taker单 <br><br>  `cancel_maker` 取消maker单 <br><br>  `cancel_both` 两者都取消 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.orderId | string |  | 计划委托订单id |
| data.clientOid | string |  | 自定义计划委托订单id |

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

## 支持止盈止损计划委托同时下单

`POST /api/v2/mix/order/place-pos-tpsl`

普通用户10次/S 根据uid限频

下止盈止损计划委托单

**API Broker返佣标识**:

  需在HTTP Header请求头中添加如下代码块

  > "X-CHANNEL-API-CODE":"your-channel-api-code"

Operation ID: `classicContractPlanPlacePosTpslOrder`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| marginCoin | string | 是 | 保证金币种(大写) |
| productType | string | 是 | 产品类型<br><br>`USDT-FUTURES` U本位合约<br><br>`COIN-FUTURES` 币本位合约<br><br>`USDC-FUTURES` USDC合约 |
| symbol | string | 是 | 交易币对 |
| stopSurplusTriggerPrice | string |  | 止盈触发价格 |
| stopSurplusSize | string |  | 止盈数量，如果传，则是部分止盈计划，如果不传，则是仓位止盈 |
| stopSurplusTriggerType | string |  | 触发类型<br><br>fill_price：市场价格<br><br>mark_price：标记价格 |
| stopSurplusExecutePrice | string |  | 止盈执行价格<br><br>不传或者传0则市价执行。大于0为限价执行 |
| stopLossTriggerPrice | string |  | 止损触发价格 |
| stopLossSize | string |  | 止损数量，如果传，则是部分止损计划，如果不传，则是仓位止损 |
| stopLossTriggerType | string |  | 触发类型<br><br>fill_price：市场价格<br><br>mark_price：标记价格 |
| stopLossExecutePrice | string |  | 止损执行价格<br><br>不传或者传0则市价执行。大于0为限价执行 |
| holdSide | string | 是 | 双向持仓：<br><br>long：多仓，short：空仓;<br><br>单向持仓：<br><br>buy：多仓，sell：空仓 |
| stpMode | string |  | STP模式， default `none` <br><br> `none` 不设置STP <br><br> `cancel_taker` 取消taker单 <br><br>  `cancel_maker` 取消maker单 <br><br>  `cancel_both` 两者都取消 |
| stopSurplusClientOid | string |  | 止盈委托自定义订单ID |
| stopLossClientOid | string |  | 止损委托自定义订单ID |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].orderId | string |  | 计划委托订单id |
| data[].stopSurplusClientOid | string |  | 止盈委托自定义订单ID |
| data[].stopLossClientOid | string |  | 止损委托自定义订单ID |

```json
{
  "code": "00000",
  "data": [
    {
      "orderId": "xxxxxxxx",
      "stopSurplusClientOid": "xxxxxxxx",
      "stopLossClientOid": "xxxxxxxx"
    },
    {
      "orderId": "xxxxxxxx",
      "stopSurplusClientOid": "xxxxxxxx",
      "stopLossClientOid": "xxxxxxxx"
    }
  ],
  "msg": "success",
  "requestTime": 1627293504612
}
```

## 止盈止损计划委托下单

`POST /api/v2/mix/order/place-tpsl-order`

普通用户10次/S 根据uid限频

下止盈止损计划委托单

**API Broker返佣标识**:

  需在HTTP Header请求头中添加如下代码块

  > "X-CHANNEL-API-CODE":"your-channel-api-code"

Operation ID: `classicContractPlanPlaceTpslOrder`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| marginCoin | string | 是 | 保证金币种(大写) |
| productType | string | 是 | 产品类型<br><br>`USDT-FUTURES` U本位合约<br><br>`COIN-FUTURES` 币本位合约<br><br>`USDC-FUTURES` USDC合约 |
| symbol | string | 是 | 交易币对 |
| planType | string | 是 | 止盈止损类型<br><br>profit_plan：止盈计划<br><br>loss_plan：止损计划<br><br>moving_plan：移动止盈止损<br><br>pos_profit：仓位止盈<br><br>pos_loss：仓位止损 |
| triggerPrice | string | 是 | 触发价格 |
| triggerType | string |  | 触发类型<br><br>fill_price：市场价格<br><br>mark_price：标记价格 |
| executePrice | string |  | 执行价格<br><br>不传或者传0则市价执行。大于0为限价执行<br><br>`planType`为moving_plan时不允许传此参数，固定为市价执行 |
| holdSide | string | 是 | 双向持仓：<br><br>long：多仓，short：空仓;<br><br>单向持仓：<br><br>buy：多仓，sell：空仓 |
| size | string | 是 | 下单数量(基础币)<br><br>`planType`为profit_plan、loss_plan、moving_plan时必填（大于0）<br><br>`planType`为pos_profit、pos_loss时非必填 |
| rangeRate | string |  | 回调幅度<br><br>`planType`为moving_plan时必填<br><br>取值范围：[0.01, 10]<br><br>精度：小数点后2位 |
| clientOid | string |  | 自定义订单id |
| stpMode | string |  | STP模式， default `none` <br><br> `none` 不设置STP <br><br> `cancel_taker` 取消taker单 <br><br>  `cancel_maker` 取消maker单 <br><br>  `cancel_both` 两者都取消 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.orderId | string |  | 计划委托订单id |
| data.clientOid | string |  | 自定义计划委托订单id |

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

## 获取计划委托触发条件单

`GET /api/v2/mix/order/plan-sub-order`

普通用户10次/S 根据uid限频

获取计划委托触发条件单（计划委托触发后执行的合约订单）

Operation ID: `classicContractPlanPlanSubOrders`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| planOrderId | query | string | 是 | 计划委托订单ID |
| productType | query | string | 是 | 产品类型<br><br>`USDT-FUTURES` U本位合约<br><br>`COIN-FUTURES` 币本位合约<br><br>`USDC-FUTURES` USDC合约 |
| planType | query | string | 是 | 计划委托类型<br><br>normal_plan 普通计划委托<br><br>track_plan 追踪委托 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].orderId | string |  | 合约订单ID |
| data[].price | string |  | 委托价格 |
| data[].type | string |  | 订单类型<br><br>limit限价<br><br>market市价 |
| data[].status | string |  | 计划委托单触发状态<br><br>success: 执行成功<br><br>fail: 执行失败<br><br>cancelled: 取消<br><br>in_progress: 下单中<br><br>in_progress_tracking: 执行追踪中 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1710813939206,
  "data": [
    {
      "orderId": "xxxxxxxxxxxxx",
      "price": "0.4188",
      "type": "limit",
      "status": "success"
    }
  ]
}
```

## 修改计划委托

`POST /api/v2/mix/order/modify-plan-order`

普通用户10次/S 根据uid限频

修改计划委托订单，对于处于委托状态的订单进行修改，支持修改止盈止损及其触发价格

Operation ID: `classicContractPlanModifyPlanOrder`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| orderId | string |  | 计划委托订单id<br><br>与clientOid两者必传其一，如果两个都传 则以orderId 为主 |
| clientOid | string |  | 自定义计划委托订单id<br><br>与orderId两者必传其一，如果两个都传 则以orderId 为主 |
| productType | string | 是 | 产品类型<br><br>`USDT-FUTURES` U本位合约<br><br>`COIN-FUTURES` 币本位合约<br><br>`USDC-FUTURES` USDC合约 |
| newSize | string |  | 修改的新交易数量<br><br>若为空则保持原有不变。 |
| newPrice | string |  | 修改的新执行价格。<br><br>1:原订单为普通计划委托时，若原订单类型为限价单(limit)时，不传则保持原有价格。<br><br>若订单类型为为市价单(market)时则必须为空。<br><br>2:原订单为追踪委托时，必须为空。 |
| newCallbackRatio | string |  | 修改的新执行回调幅度（只适用追踪委托）<br><br>1.原订单为追踪委托时，则必传，且回调幅度不可大于10.<br><br>2.原订单为普通计划委托，必须为空。 |
| newTriggerPrice | string |  | 修改的新触发价格<br><br>原订单为普通计划委托、追踪委托时，不传则保持变，若传则更新触发价格。 |
| newTriggerType | string |  | 修改的新触发类型<br><br>原订单为普通计划委托、追踪委托时，不传则保持变，若传则更新触发类型。<br><br>填写此参数时必须携带newTriggerPrice。<br><br>fill_price 成交价格<br><br>mark_price 标记价格 |
| newStopSurplusTriggerPrice | string |  | 修改的新止盈触发价格/止盈触发百分比<br><br>1.若为空，原有订单已设止盈的话则保持原有值<br><br>2.若不为空且大于0，原有订单已设止盈则更新止盈值；原有订单未设止盈则新增止盈项。若为追踪委托，最大比例必须小于等于999.99，最小0.01<br><br>3.若等于0，则代表删除止盈。 |
| newStopSurplusExecutePrice | string |  | 修改的新止盈执行价格<br><br>1.原有订单为追踪委托时，本参数必须为空。否则将报错。默认为市价执行<br><br>2.原有订单为普通计划委托，若传递本参数则会更新执行价格，若不传则保持原样。若等于0，则为则为市价执行；大于0则为限价执行 |
| newStopSurplusTriggerType | string |  | 修改的新止盈触发类型<br><br>默认为成交价格<br><br>1.原有订单为追踪委托时，本参数必须为空。<br><br>2.若原有订单为普通计划委托，若同时携带了newStopSurplusTriggerPrice参数则必传。<br><br>fill_price 成交价格<br><br>mark_price 标记价格 |
| newStopLossTriggerPrice | string |  | 修改的新止损触发价格/止损触发百分比<br><br>1.若为空，原有订单已设止损的话则保持原有值<br><br>2.若不为空且大于0，原有订单已设止损则更新止损值；原有订单未设止损则新增止损项。若为追踪委托，最大比例必须小于等于999.99，最小0.01<br><br>3.若为0，则代表删除止损。 |
| newStopLossExecutePrice | string |  | 修改的新止损执行价格<br><br>1.原有订单为追踪委托时，本参数必须为空。否则将报错。默认为市价执行<br><br>2.原有订单为普通计划委托，若传递本参数则会更新执行价格，若不传则保持原样。若等于0，则为则为市价执行；大于0则为限价执行。 |
| newStopLossTriggerType | string |  | 修改的新止损触发类型<br><br>默认为成交价格<br><br>1.原有订单为追踪委托时，本参数必须为空。<br><br>2.若原有订单为普通计划委托，若同时携带了newStopLossTriggerPrice参数则必传。<br><br>fill_price 成交价格<br><br>mark_price 标记价格 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.orderId | string |  | 计划委托订单id |
| data.clientOid | string |  | 自定义计划委托订单id |

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

## 获取当前计划委托

`GET /api/v2/mix/order/orders-plan-pending`

普通用户10次/S 根据uid限频

可获取当前普通单和计划委托，支持单个和全量查询。

Operation ID: `classicContractPlanGetOrdersPlanPending`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| orderId | query | string |  | 订单ID<br><br>orderId和clientOid同传时以orderId为准。 |
| clientOid | query | string |  | 自定义订单ID<br><br>orderId和clientOid同传时以orderId为准。 |
| planType | query | string | 是 | 计划委托类型<br><br>`normal_plan`: 普通计划委托<br><br>`track_plan`: 追踪委托 <br><br>`profit_loss`: 止盈止损类委托(包含了：profit_plan：止盈计划, loss_plan：止损计划, moving_plan：移动止盈止损，pos_profit：仓位止盈，pos_loss：仓位止损) |
| symbol | query | string |  | 交易对 如:ethusdt |
| productType | query | string | 是 | 产品类型<br><br>`USDT-FUTURES` U本位合约<br><br>`COIN-FUTURES` 币本位合约<br><br>`USDC-FUTURES` USDC合约 |
| idLessThan | query | string |  | 请求此ID之前（更旧的数据）的分页内容，传的值为对应接口的 endId。 |
| startTime | query | string |  | 开始时间戳 <br><br>Unix时间戳的毫秒数格式，如 1597026383085<br><br>（时间跨度最大支持三个月，若不传结束时间，则默认结束时间为三个月。） |
| endTime | query | string |  | 结束时间戳 <br><br>Unix时间戳的毫秒数格式，如 1597026383085<br><br>（时间跨度最大支持三个月，若不传开始时间，则默认开始时间为三个月。） |
| limit | query | string |  | 查询条数 默认100，最大100 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.entrustedList | object[] |  | 委托集合 |
| data.entrustedList[].planType | string |  | 委托类型<br><br>normal_plan 普通计划委托<br><br>track_plan 追踪委托<br><br>profit_plan 止盈计划（分批止盈止损）<br><br>loss_plan 止损计划（分批止盈止损）<br><br>pos_profit 仓位止盈<br><br>pos_loss 仓位止损<br><br>moving_plan 移动止盈止损 |
| data.entrustedList[].symbol | string |  | 交易对名称 |
| data.entrustedList[].size | string |  | 委托数量 |
| data.entrustedList[].orderId | string |  | 计划委托订单id |
| data.entrustedList[].clientOid | string |  | 自定义计划委托订单id |
| data.entrustedList[].price | string |  | 执行价格<br><br>当计划委托为追踪委托时，则不存在 |
| data.entrustedList[].executePrice | string |  | 执行价格 |
| data.entrustedList[].callbackRatio | string |  | 执行回调幅度。(范围为1-10)<br><br>只有为追踪委托时才会存在。 |
| data.entrustedList[].triggerPrice | string |  | 触发价格<br><br>普通计划委托/追踪委托时会存在。 |
| data.entrustedList[].triggerType | string |  | 触发类型<br><br>普通计划委托/追踪委托时会存在。<br><br>fill_price 成交价格<br><br>mark_price 标记价格<br><br>index_price 指数价格 |
| data.entrustedList[].planStatus | string |  | 订单状态<br><br>当前计划委托中，状态仅会为`live`（未触发） |
| data.entrustedList[].side | string |  | 开单方向<br><br>buy 买，sell 卖 |
| data.entrustedList[].posSide | string |  | 持仓方向<br><br>long 双向持仓多头<br><br>short 双向持仓空头<br><br>net 单向持仓 |
| data.entrustedList[].marginCoin | string |  | 保证金币种 |
| data.entrustedList[].marginMode | string |  | 保证金模式<br><br>`isolated`: 逐仓<br><br>`crossed`: 全仓 |
| data.entrustedList[].enterPointSource | string |  | 订单来源<br><br>WEB        自Web端创建的订单<br><br>API        自API端创建的订单<br><br>SYS        系统托管订单, 通常由强制平仓逻辑生成<br><br>ANDROID        自Android端创建的订单<br><br>IOS        自IOS端创建的订单 |
| data.entrustedList[].tradeSide | string |  | 交易方向<br><br>`open` 开（开平仓模式）<br><br>`close` 平（开平仓模式） |
| data.entrustedList[].posMode | string |  | 持仓模式<br><br>one_way_mode 单向持仓<br><br>hedge_mode 双向持仓 |
| data.entrustedList[].orderType | string |  | 订单类型<br><br>limit 限价单<br><br>market 市价单 |
| data.entrustedList[].orderSource | string |  | 订单资源<br><br>normal        正常下单<br><br>market          市价单<br><br>profit_market        市价止盈单<br><br>loss_market        市价止损单<br><br>Trader_delegate        交易员带单下单<br><br>trader_profit        交易员止盈<br><br>trader_loss        交易员止损<br><br>trader_reverse        交易员带单反手<br><br>profit_limit        止盈限价<br><br>loss_limit        止损限价<br><br>delivery_close_short        空仓交割<br><br>pos_profit_limit        仓位止盈限价<br><br>pos_profit_market        仓位止盈市价<br><br>pos_loss_limit        仓位止损限价<br><br>pos_loss_market        仓位止损市价 |
| data.entrustedList[].cTime | string |  | 创建时间 |
| data.entrustedList[].uTime | string |  | 最近更新时间 |
| data.entrustedList[].stopSurplusExecutePrice | string |  | 预设止盈值 |
| data.entrustedList[].stopSurplusTriggerPrice | string |  | 预设止盈触发价格 |
| data.entrustedList[].stopSurplusTriggerType | string |  | 预设止盈触发类型<br><br>fill_price 成交价格<br><br>mark_price 标记价格<br><br>index_price 指数价格 |
| data.entrustedList[].stopLossExecutePrice | string |  | 预设止损值 |
| data.entrustedList[].stopLossTriggerPrice | string |  | 预设止损触发价格 |
| data.entrustedList[].stopLossTriggerType | string |  | 预设止损触发类型<br><br>fill_price 成交价格<br><br>mark_price 标记价格<br><br>index_price 指数价格 |
| data.endId | string |  | 最后的订单ID<br><br>指定idLessThan/idGreaterThan作为范围查询时以此为准。 |

```json
{
  "code": "00000",
  "data": {
    "entrustedList": [
      {
        "planType": "normal_plan",
        "symbol": "ethusdt",
        "size": "1",
        "orderId": "123",
        "clientOid": "121212",
        "price": "1900",
        "executePrice": "1990",
        "callbackRatio": "",
        "triggerPrice": "1901",
        "triggerType": "mark_price",
        "planStatus": "not_trigger",
        "side": "buy",
        "posSide": "long",
        "marginCoin": "usdt",
        "marginMode": "crossed",
        "enterPointSource": "api",
        "tradeSide": "open",
        "posMode": "hedge_mode",
        "orderType": "limit",
        "orderSource": "normal",
        "cTime": "1627293504612",
        "uTime": "",
        "stopSurplusExecutePrice": "2001",
        "stopSurplusTriggerPrice": "2002",
        "stopSurplusTriggerType": "fill_price",
        "stopLossExecutePrice": "1800",
        "stopLossTriggerPrice": "1820",
        "stopLossTriggerType": "fill_price"
      }
    ],
    "endId": "123"
  },
  "msg": "success",
  "requestTime": 1627293504612
}
```

## 计划委托撤单

`POST /api/v2/mix/order/cancel-plan-order`

普通用户10次/S 根据uid限频

计划委托撤单接口，可按产品类型、交易对名称或计划委托订单ID进行撤单。

Operation ID: `classicContractPlanCancelPlanOrder`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| orderIdList | object[] |  | 计划委托订单id集合。<br><br>若传递，symbol不可为空，且需与symbol/productType/planType对齐 |
| orderIdList[].orderId | string |  | 计划委托订单id<br><br> orderId和clientOid必须两者传一个，同传时以orderId为准。 |
| orderIdList[].clientOid | string |  | 自定义计划委托订单id<br><br> orderId和clientOid必须两者传一个，同传时以orderId为准。 |
| symbol | string |  | 交易对 如:ethusdt |
| productType | string | 是 | 产品类型<br><br>`USDT-FUTURES` U本位合约<br><br>`COIN-FUTURES` 币本位合约<br><br>`USDC-FUTURES` USDC合约 |
| marginCoin | string |  | 保证金币种 必须大写 |
| planType | string |  | 计划委托类型<br><br>normal_plan 普通计划委托(默认)<br><br>profit_plan 分批止盈 <br><br>loss_plan 分批止损 <br><br>pos_profit 仓位止盈 <br><br> pos_loss 仓位止损 <br><br> moving_plan 移动止盈止损 |

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

```json
{
  "code": "00000",
  "data": {
    "successList": [
      {
        "orderId": "121212121212",
        "clientOid": "BITGET#1627293504612"
      },
      {
        "orderId": "21221",
        "clientOid": ""
      }
    ],
    "failureList": [
      {
        "orderId": "232",
        "clientOid": "321342",
        "errorMsg": "notExistend"
      },
      {
        "orderId": "21221",
        "clientOid": "",
        "errorMsg": "notExisted"
      }
    ]
  },
  "msg": "success",
  "requestTime": 1627293504612
}
```

## 查询历史计划委托

`GET /api/v2/mix/order/orders-plan-history`

普通用户10次/S 根据uid限频

可查询历史的个别或所有的历史计划委托。

Operation ID: `classicContractPlanOrdersPlanHistory`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| orderId | query | string |  | 订单ID<br><br> orderId和clientOid同传时以orderId为准。 |
| clientOid | query | string |  | 自定义订单ID<br><br> orderId和clientOid同传时以orderId为准。 |
| planType | query | string | 是 | 委托类型<br><br>`normal_plan`：普通计划委托<br><br>`track_plan`：追踪委托<br><br>`profit_loss`：止盈止损类委托(包含了：profit_plan：止盈计划, loss_plan：止损计划, moving_plan：移动止盈止损，pos_profit：仓位止盈，pos_loss：仓位止损) |
| planStatus | query | string |  | 计划委托状态<br><br>若未指定，将查询所有状态<br><br>executed：已触发<br><br>fail_execute：触发失败<br><br>cancelled：已撤销 |
| symbol | query | string |  | 交易对 如:ethusdt |
| productType | query | string | 是 | 产品类型<br><br>`USDT-FUTURES` U本位合约<br><br>`COIN-FUTURES` 币本位合约<br><br>`USDC-FUTURES` USDC合约 |
| idLessThan | query | string |  | 请求此ID之前（更旧的数据）的分页内容，传的值为对应接口的 endId。 |
| startTime | query | string |  | 开始时间戳 <br><br>Unix时间戳的毫秒数格式，如 1597026383085<br><br>（时间跨度最大支持三个月，若不传结束时间，则默认结束时间为三个月。） <br><br>(托管子账户访问时，StartTime 时间不能早于 绑定开始的时间) |
| endTime | query | string |  | 结束时间戳 <br><br>Unix时间戳的毫秒数格式，如 1597026383085<br><br>（时间跨度最大支持三个月，若不传开始时间，则默认开始时间为三个月。） |
| limit | query | string |  | 查询条数 默认100，最大100 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.entrustedList | object[] |  | 委托集合 |
| data.entrustedList[].planType | string |  | 委托类型<br><br>normal_plan 普通计划委托<br><br>track_plan 追踪委托<br><br>profit_plan 止盈计划（分批止盈止损）<br><br>loss_plan 止损计划（分批止盈止损）<br><br>pos_profit 仓位止盈<br><br>pos_loss 仓位止损<br><br>moving_plan 移动止盈止损 |
| data.entrustedList[].symbol | string |  | 交易对名称 |
| data.entrustedList[].size | string |  | 委托数量 |
| data.entrustedList[].orderId | string |  | 计划委托订单id |
| data.entrustedList[].executeOrderId | string |  | 委托触发后生成的订单ID |
| data.entrustedList[].clientOid | string |  | 自定义计划委托订单id |
| data.entrustedList[].planStatus | string |  | 订单状态<br><br>`live`: 新建订单<br><br>`executed`：已触发<br><br>`fail_execute`：触发失败<br><br>`cancelled`：已撤销 |
| data.entrustedList[].price | string |  | 委托价格<br><br>当计划委托类型为普通计划委托时，代表的是单纯的委托价格。<br><br>当计划委托类型为追踪委托时，则不存在。 |
| data.entrustedList[].executePrice | string |  | 执行价格 |
| data.entrustedList[].baseVolume | string |  | 交易币成交数量<br><br>订单状态为triggered（已触发）时才会有。 |
| data.entrustedList[].triggerPrice | string |  | 触发价格<br><br>普通计划委托/追踪委托时会存在。 |
| data.entrustedList[].triggerType | string |  | 触发类型<br><br>普通计划委托/追踪委托时会存在。<br><br>fill_price 成交价格<br><br>mark_price 标记价格 |
| data.entrustedList[].side | string |  | 开单方向<br><br>buy 买，sell 卖 |
| data.entrustedList[].posSide | string |  | 持仓方向<br><br>long 双向持仓多头<br><br>short 双向持仓空头<br><br>net 单向持仓 |
| data.entrustedList[].marginCoin | string |  | 保证金币种 |
| data.entrustedList[].marginMode | string |  | 保证金模式<br><br>isolated 逐仓<br><br>crossed 全仓 |
| data.entrustedList[].enterPointSource | string |  | 订单来源<br><br>WEB        自Web端创建的订单<br><br>API        自API端创建的订单<br><br>SYS        系统托管订单, 通常由强制平仓逻辑生成<br><br>ANDROID        自Android端创建的订单<br><br>IOS        自IOS端创建的订单 |
| data.entrustedList[].tradeSide | string |  | 交易方向<br><br>open 开（开平仓模式）<br><br>close 平（开平仓模式） |
| data.entrustedList[].posMode | string |  | 持仓模式<br><br>one_way_mode 单向持仓<br><br>hedge_mode 双向持仓 |
| data.entrustedList[].orderType | string |  | 订单类型<br><br>limit 限价单<br><br>market 市价单 |
| data.entrustedList[].cTime | string |  | 创建时间 |
| data.entrustedList[].uTime | string |  | 最近更新时间 |
| data.entrustedList[].stopSurplusExecutePrice | string |  | 预设止盈执行价 |
| data.entrustedList[].stopSurplusTriggerPrice | string |  | 预设止盈触发价格 |
| data.entrustedList[].stopSurplusTriggerType | string |  | 预设止盈触发类型<br><br>fill_price 成交价格<br><br>mark_price 标记价格 |
| data.entrustedList[].stopLossExecutePrice | string |  | 预设止损执行价 |
| data.entrustedList[].stopLossTriggerPrice | string |  | 预设止损触发价格 |
| data.entrustedList[].stopLossTriggerType | string |  | 预设止损触发类型<br><br>fill_price 成交价格<br><br>mark_price 标记价格 |
| data.callbackRatio | string |  | 执行回调幅度。(最大为1-10)<br><br>只有为追踪委托时才会存在 |
| data.endId | string |  | 最后的订单id<br><br>指定idLessThan/idGreaterThan作为范围查询时以此为准。 |

```json
{
  "code": "00000",
  "data": {
    "entrustedList": [
      {
        "planType": "normal_plan",
        "symbol": "ethusdt",
        "size": "1",
        "orderId": "123",
        "executeOrderId": "123456",
        "clientOid": "",
        "planStatus": "executed",
        "price": "1990",
        "executePrice": "1990",
        "priceAvg": "1999.2",
        "baseVolume": "1",
        "callbackRatio": "",
        "triggerPrice": "1989",
        "triggerType": "fill_price",
        "side": "buy",
        "posSide": "long",
        "marginCoin": "usdt",
        "marginMode": "crossed",
        "enterPointSource": "api",
        "tradeSide": "open",
        "posMode": "hedge_mode",
        "orderType": "limit",
        "cTime": "1627293504612",
        "uTime": "",
        "stopSurplusExecutePrice": "2001",
        "stopSurplusTriggerPrice": "2002",
        "stopSurplusTriggerType": "fill_price",
        "stopLossExecutePrice": "1800",
        "stopLossTriggerPrice": "1820",
        "stopLossTriggerType": "fill_price"
      }
    ],
    "endId": "123"
  },
  "msg": "success",
  "requestTime": 1627293504612
}
```