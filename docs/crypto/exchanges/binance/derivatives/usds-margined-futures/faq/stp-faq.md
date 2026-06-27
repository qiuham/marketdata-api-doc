---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/usds-margined-futures/faq/stp-faq
api_type: REST
updated_at: 2026-01-15T23:46:40.202849
---

# Self Trade Prevention (STP) FAQ

## What is Self Trade Prevention?[​](/docs/derivatives/usds-margined-futures/faq/stp-faq#what-is-self-trade-prevention "Direct link to What is Self Trade Prevention?")

Self Trade Prevention (or STP) prevents orders of users, or the user's `tradeGroupId` to match against their own.

## What defines a self-trade?[​](/docs/derivatives/usds-margined-futures/faq/stp-faq#what-defines-a-self-trade "Direct link to What defines a self-trade?")

A self-trade can occur in either scenario:

  * The order traded against the same account.
  * The order traded against an account with the same `tradeGroupId`.



## What happens when STP is triggered?[​](/docs/derivatives/usds-margined-futures/faq/stp-faq#what-happens-when-stp-is-triggered "Direct link to What happens when STP is triggered?")

There are three possible modes for what the system will do if an order could create a self-trade.

`EXPIRE_TAKER` \- This mode prevents a trade by immediately expiring the taker order's remaining quantity.

`EXPIRE_MAKER` \- This mode prevents a trade by immediately expiring the potential maker order's remaining quantity.

`EXPIRE_BOTH` \- This mode prevents a trade by immediately expiring both the taker and the potential maker orders' remaining quantities.

The STP event will occur depending on the STP mode of the **taker order**.   
Thus, the STP mode of an order that goes on the book is no longer relevant and will be ignored for all future order processing.

## Where do I set STP mode for an order?[​](/docs/derivatives/usds-margined-futures/faq/stp-faq#where-do-i-set-stp-mode-for-an-order "Direct link to Where do I set STP mode for an order?")

STP can only be set using field `selfTradePreventionMode` through API endpoints below:

  * POST `/fapi/v1/order`
  * POST `/fapi/v1/batchOrders`



## What is a Trade Group Id?[​](/docs/derivatives/usds-margined-futures/faq/stp-faq#what-is-a-trade-group-id "Direct link to What is a Trade Group Id?")

Different accounts with the same `tradeGroupId` are considered part of the same "trade group". Orders submitted by members of a trade group are eligible for STP according to the taker-order's STP mode.

A user can confirm if their accounts are under the same `tradeGroupId` from the API either from `GET /fapi/v1/accountConfig` (REST API).

If the value is `-1`, then the `tradeGroupId` has not been set for that account, so the STP may only take place between orders of the same account.

We will release feature for user to group subaccounts to same `tradeGroupId` on website in future updates.

## How do I know which symbol uses STP?[​](/docs/derivatives/usds-margined-futures/faq/stp-faq#how-do-i-know-which-symbol-uses-stp "Direct link to How do I know which symbol uses STP?")

Placing orders on all symbols in `GET fapi/v1/exchangeInfo` can set `selfTradePreventionMode`.

## What order types support STP?[​](/docs/derivatives/usds-margined-futures/faq/stp-faq#what-order-types-support-stp "Direct link to What order types support STP?")

`LIMIT`/`MARKET`/`STOP`/`TAKE_PROFIT`/`STOP_MARKET`/`TAKE_PROFIT_MARKET`/`TRAILING_STOP_MARKET` all supports STP when Time in force(timeInForce) set to `GTC`/ `IOC`/ `GTD`. STP won't take effect for Time in force(timeInForce) `FOK` or `GTX`

## Does Modify order support STP?[​](/docs/derivatives/usds-margined-futures/faq/stp-faq#does-modify-order-support-stp "Direct link to Does Modify order support STP?")

No. Modify order that has reset `selfTradePreventionMode` to `NONE`

## How do I know if an order expired due to STP?[​](/docs/derivatives/usds-margined-futures/faq/stp-faq#how-do-i-know-if-an-order-expired-due-to-stp "Direct link to How do I know if an order expired due to STP?")

The order will have the status `EXPIRED_IN_MATCH`.

In user data stream event `ORDER_TRADE_UPDATE`, field `X` would be `EXPIRED_IN_MATCH` if order is expired due to STP
    
    
    {  
      "e":"ORDER_TRADE_UPDATE",      // Event Type  
      "E":1568879465651,             // Event Time  
      "T":1568879465650,             // Transaction Time  
      "o":{                               
        "s":"BTCUSDT",               // Symbol  
        "c":"TEST",                  // Client Order Id  
          // special client order id:  
          // starts with "autoclose-": liquidation order  
          // "adl_autoclose": ADL auto close order  
          // "settlement_autoclose-": settlement order for delisting or delivery  
        "S":"SELL",                  // Side  
        "o":"TRAILING_STOP_MARKET",  // Order Type  
        "f":"GTC",                   // Time in Force  
        "q":"0.001",                 // Original Quantity  
        "p":"0",                     // Original Price  
        "ap":"0",                    // Average Price  
        "sp":"7103.04",              // Stop Price. Please ignore with TRAILING_STOP_MARKET order  
        "x":"EXPIRED",               // Execution Type  
        "X":"EXPIRED_IN_MATCH",      // Order Status  
        "i":8886774,                 // Order Id  
        "l":"0",                     // Order Last Filled Quantity  
        "z":"0",                     // Order Filled Accumulated Quantity  
        "L":"0",                     // Last Filled Price  
        "N":"USDT",                  // Commission Asset, will not push if no commission  
        "n":"0",                     // Commission, will not push if no commission  
        "T":1568879465650,           // Order Trade Time  
        "t":0,                       // Trade Id  
        "b":"0",                     // Bids Notional  
        "a":"9.91",                  // Ask Notional  
        "m":false,                   // Is this trade the maker side?  
        "R":false,                   // Is this reduce only  
        "wt":"CONTRACT_PRICE",       // Stop Price Working Type  
        "ot":"TRAILING_STOP_MARKET", // Original Order Type  
        "ps":"LONG",                 // Position Side  
        "cp":false,                  // If Close-All, pushed with conditional order  
        "AP":"7476.89",              // Activation Price, only puhed with TRAILING_STOP_MARKET order  
        "cr":"5.0",                  // Callback Rate, only puhed with TRAILING_STOP_MARKET order  
        "pP": false,                 // ignore  
        "si": 0,                     // ignore  
        "ss": 0,                     // ignore  
        "rp":"0",                    // Realized Profit of the trade  
        "V": "EXPIRE_MAKER",         // selfTradePreventionMode  
        "pm":"QUEUE",                // price match type  
        "gtd":1768879465650          // good till date  
       }  
    }  
    

## STP Examples:[​](/docs/derivatives/usds-margined-futures/faq/stp-faq#stp-examples "Direct link to STP Examples:")

For all these cases, assume that all orders for these examples are made on the same account.

**Scenario A- A user sends an order with`EXPIRE_MAKER` that would match with their orders that are already on the book.**
    
    
    Maker Order 1: symbol=BTCUSDT side=BUY  type=LIMIT quantity=1 price=20002 selfTradePreventionMode=EXPIRE_MAKER  
    Maker Order 2: symbol=BTCUSDT side=BUY  type=LIMIT quantity=1 price=20001 selfTradePreventionMode=EXPIRE_MAKER  
    Taker Order 1: symbol=BTCUSDT side=SELL type=LIMIT quantity=1 price=20000 selfTradePreventionMode=EXPIRE_MAKER  
    

**Result** : The orders that were on the book will expire due to STP, and the taker order will go on the book.

Maker Order 1
    
    
    {  
        "orderId": 292864710,  
        "symbol": "BTCUSDT",  
        "status": "FILLED",  
        "clientOrderId": "testMaker1",  
        "price": "20002",  
        "avgPrice": "20002",  
        "origQty": "1",  
        "executedQty": "1",  
        "cumQuote": "20002",  
        "timeInForce": "GTC",  
        "type": "LIMIT",  
        "reduceOnly": false,  
        "closePosition": false,  
        "side": "BUY",  
        "positionSide": "BOTH",  
        "stopPrice": "0",  
        "workingType": "CONTRACT_PRICE",  
        "priceMatch": "NONE",  
        "selfTradePreventionMode": "EXPIRE_MAKER",  
        "goodTillDate": "null",  
        "priceProtect": false,  
        "origType": "LIMIT",  
        "time": 1692849639460,  
        "updateTime": 1692849639460  
    }  
    

Maker Order 2
    
    
    {  
        "orderId": 292864711,  
        "symbol": "BTCUSDT",  
        "status": "EXPIRED_IN_MATCH",  
        "clientOrderId": "testMaker2",  
        "price": "20001",  
        "avgPrice": "0.0000",  
        "origQty": "1",  
        "executedQty": "0",  
        "cumQuote": "0",  
        "timeInForce": "GTC",  
        "type": "LIMIT",  
        "reduceOnly": false,  
        "closePosition": false,  
        "side": "BUY",  
        "positionSide": "BOTH",  
        "stopPrice": "0",  
        "workingType": "CONTRACT_PRICE",  
        "priceMatch": "NONE",  
        "selfTradePreventionMode": "EXPIRE_MAKER",  
        "goodTillDate": "null",  
        "priceProtect": false,  
        "origType": "LIMIT",  
        "time": 1692849639460,  
        "updateTime": 1692849639460  
    }  
    

Output of the Taker Order
    
    
    {  
        "orderId": 292864712,  
        "symbol": "BTCUSDT",  
        "status": "PARTIALLY_FILLED",  
        "clientOrderId": "testTaker1",  
        "price": "20000",  
        "avgPrice": "20002",  
        "origQty": "2",  
        "executedQty": "1",  
        "cumQuote": "20002",  
        "timeInForce": "GTC",  
        "type": "LIMIT",  
        "reduceOnly": false,  
        "closePosition": false,  
        "side": "SELL",  
        "positionSide": "BOTH",  
        "stopPrice": "0",  
        "workingType": "CONTRACT_PRICE",  
        "priceMatch": "NONE",  
        "selfTradePreventionMode": "EXPIRE_MAKER",  
        "goodTillDate": "null",  
        "priceProtect": false,  
        "origType": "LIMIT",  
        "time": 1692849639460,  
        "updateTime": 1692849639460  
    }  
    

**Scenario B - A user sends an order with`EXPIRE_TAKER` that would match with their orders already on the book.**
    
    
    Maker Order 1: symbol=BTCUSDT side=BUY  type=LIMIT quantity=1 price=20002  selfTradePreventionMode=EXPIRE_MAKER  
    Maker Order 2: symbol=BTCUSDT side=BUY  type=LIMIT quantity=1 price=20001  selfTradePreventionMode=EXPIRE_MAKER  
    Taker Order 1: symbol=BTCUSDT side=SELL type=LIMIT quantity=2 price=3      selfTradePreventionMode=EXPIRE_TAKER  
    

**Result** : The orders already on the book will remain, while the taker order will expire.

Maker Order 1
    
    
    {  
        "orderId": 292864710,  
        "symbol": "BTCUSDT",  
        "status": "FILLED",  
        "clientOrderId": "testMaker1",  
        "price": "20002",  
        "avgPrice": "0.0000",  
        "origQty": "1",  
        "executedQty": "0",  
        "cumQuote": "0",  
        "timeInForce": "GTC",  
        "type": "LIMIT",  
        "reduceOnly": false,  
        "closePosition": false,  
        "side": "BUY",  
        "positionSide": "BOTH",  
        "stopPrice": "0",  
        "workingType": "CONTRACT_PRICE",  
        "priceMatch": "NONE",  
        "selfTradePreventionMode": "EXPIRE_MAKER",  
        "goodTillDate": "null",  
        "priceProtect": false,  
        "origType": "LIMIT",  
        "time": 1692849639460,  
        "updateTime": 1692849639460  
    }  
    

Maker Order 2
    
    
    {  
        "orderId": 292864711,  
        "symbol": "BTCUSDT",  
        "status": "EXPIRED_IN_MATCH",  
        "clientOrderId": "testMaker2",  
        "price": "20001",  
        "avgPrice": "0.0000",  
        "origQty": "1",  
        "executedQty": "0",  
        "cumQuote": "0",  
        "timeInForce": "GTC",  
        "type": "LIMIT",  
        "reduceOnly": false,  
        "closePosition": false,  
        "side": "BUY",  
        "positionSide": "BOTH",  
        "stopPrice": "0",  
        "workingType": "CONTRACT_PRICE",  
        "priceMatch": "NONE",  
        "selfTradePreventionMode": "EXPIRE_MAKER",  
        "goodTillDate": "null",  
        "priceProtect": false,  
        "origType": "LIMIT",  
        "time": 1692849639460,  
        "updateTime": 1692849639460  
    }  
    

Output of the Taker order
    
    
    {  
        "orderId": 292864712,  
        "symbol": "BTCUSDT",  
        "status": "EXPIRED_IN_MATCH",  
        "clientOrderId": "testTaker1",  
        "price": "20000",  
        "avgPrice": "0.0000",  
        "origQty": "3",  
        "executedQty": "0",  
        "cumQuote": "0",  
        "timeInForce": "GTC",  
        "type": "LIMIT",  
        "reduceOnly": false,  
        "closePosition": false,  
        "side": "SELL",  
        "positionSide": "BOTH",  
        "stopPrice": "0",  
        "workingType": "CONTRACT_PRICE",  
        "priceMatch": "NONE",  
        "selfTradePreventionMode": "EXPIRE_TAKER",  
        "goodTillDate": "null",  
        "priceProtect": false,  
        "origType": "LIMIT",  
        "time": 1692849639460,  
        "updateTime": 1692849639460  
    }  
    

**Scenario C- A user has an order on the book, and then sends an order with`EXPIRE_BOTH` that would match with the existing order.**
    
    
    Maker Order: symbol=BTCUSDT side=BUY  type=LIMIT quantity=1 price=20002 selfTradePreventionMode=EXPIRE_MAKER  
    Taker Order: symbol=BTCUSDT side=SELL type=LIMIT quantity=3 price=20000 selfTradePreventionMode=EXPIRE_BOTH  
    

**Result:** Both orders will expire.

Maker Order
    
    
    {  
        "orderId": 292864710,  
        "symbol": "BTCUSDT",  
        "status": "EXPIRED_IN_MATCH",  
        "clientOrderId": "testMaker1",  
        "price": "20002",  
        "avgPrice": "0.0000",  
        "origQty": "1",  
        "executedQty": "0",  
        "cumQuote": "0",  
        "timeInForce": "GTC",  
        "type": "LIMIT",  
        "reduceOnly": false,  
        "closePosition": false,  
        "side": "BUY",  
        "positionSide": "BOTH",  
        "stopPrice": "0",  
        "workingType": "CONTRACT_PRICE",  
        "priceMatch": "NONE",  
        "selfTradePreventionMode": "EXPIRE_MAKER",  
        "goodTillDate": "null",  
        "priceProtect": false,  
        "origType": "LIMIT",  
        "time": 1692849639460,  
        "updateTime": 1692849639460  
    }  
    

Taker Order
    
    
    {  
        "orderId": 292864712,  
        "symbol": "BTCUSDT",  
        "status": "EXPIRED_IN_MATCH",  
        "clientOrderId": "testTaker1",  
        "price": "20000",  
        "avgPrice": "0.0000",  
        "origQty": "3",  
        "executedQty": "0",  
        "cumQuote": "0",  
        "timeInForce": "GTC",  
        "type": "LIMIT",  
        "reduceOnly": false,  
        "closePosition": false,  
        "side": "SELL",  
        "positionSide": "BOTH",  
        "stopPrice": "0",  
        "workingType": "CONTRACT_PRICE",  
        "priceMatch": "NONE",  
        "selfTradePreventionMode": "EXPIRE_BOTH",  
        "goodTillDate": "null",  
        "priceProtect": false,  
        "origType": "LIMIT",  
        "time": 1692849639460,  
        "updateTime": 1692849639460  
    }  
    

**Scenario D - A user has an order on the book with`EXPIRE_MAKER`, and then sends a new order with `EXPIRE_TAKER` which would match with the existing order.**
    
    
    Maker Order: symbol=BTCUSDT side=BUY  type=LIMIT quantity=1 price=1 selfTradePreventionMode=EXPIRE_MAKER  
    Taker Order: symbol=BTCUSDT side=SELL type=LIMIT quantity=1 price=1 selfTradePreventionMode=EXPIRE_TAKER  
    

**Result** : The taker order's STP mode will be used, so the taker order will be expired.

Maker Order
    
    
    {  
        "orderId": 292864710,  
        "symbol": "BTCUSDT",  
        "status": "NEW",  
        "clientOrderId": "testMaker1",  
        "price": "20002",  
        "avgPrice": "0.0000",  
        "origQty": "1",  
        "executedQty": "0",  
        "cumQuote": "0",  
        "timeInForce": "GTC",  
        "type": "LIMIT",  
        "reduceOnly": false,  
        "closePosition": false,  
        "side": "BUY",  
        "positionSide": "BOTH",  
        "stopPrice": "0",  
        "workingType": "CONTRACT_PRICE",  
        "priceMatch": "NONE",  
        "selfTradePreventionMode": "EXPIRE_MAKER",  
        "goodTillDate": "null",  
        "priceProtect": false,  
        "origType": "LIMIT",  
        "time": 1692849639460,  
        "updateTime": 1692849639460  
    }  
    

Taker Order
    
    
    {  
        "orderId": 292864712,  
        "symbol": "BTCUSDT",  
        "status": "EXPIRED_IN_MATCH",  
        "clientOrderId": "testTaker1",  
        "price": "20000",  
        "avgPrice": "0.0000",  
        "origQty": "3",  
        "executedQty": "0",  
        "cumQuote": "0",  
        "timeInForce": "GTC",  
        "type": "LIMIT",  
        "reduceOnly": false,  
        "closePosition": false,  
        "side": "SELL",  
        "positionSide": "BOTH",  
        "stopPrice": "0",  
        "workingType": "CONTRACT_PRICE",  
        "priceMatch": "NONE",  
        "selfTradePreventionMode": "EXPIRE_TAKER",  
        "goodTillDate": "null",  
        "priceProtect": false,  
        "origType": "LIMIT",  
        "time": 1692849639460,  
        "updateTime": 1692849639460  
    }  
    

**Scenario E - A user sends a market order with`EXPIRE_MAKER` which would match with an existing order.**
    
    
    Maker Order: symbol=ABCDEF side=BUY  type=LIMIT  quantity=1 price=1  selfTradePreventionMode=EXPIRE_MAKER  
    Taker Order: symbol=ABCDEF side=SELL type=MARKET quantity=3          selfTradePreventionMode=EXPIRE_MAKER  
    

**Result** : The existing order expires with the status `EXPIRED_IN_MATCH`, due to STP. The new order also expires but with status `EXPIRED`, due to low liquidity on the order book.

Maker Order
    
    
    {  
        "orderId": 292864710,  
        "symbol": "BTCUSDT",  
        "status": "EXPIRED_IN_MATCH",  
        "clientOrderId": "testMaker1",  
        "price": "20002",  
        "avgPrice": "0.0000",  
        "origQty": "1",  
        "executedQty": "0",  
        "cumQuote": "0",  
        "timeInForce": "GTC",  
        "type": "LIMIT",  
        "reduceOnly": false,  
        "closePosition": false,  
        "side": "BUY",  
        "positionSide": "BOTH",  
        "stopPrice": "0",  
        "workingType": "CONTRACT_PRICE",  
        "priceMatch": "NONE",  
        "selfTradePreventionMode": "EXPIRE_MAKER",  
        "goodTillDate": "null",  
        "priceProtect": false,  
        "origType": "LIMIT",  
        "time": 1692849639460,  
        "updateTime": 1692849639460  
    }  
    

Taker Order
    
    
    {  
        "orderId": 292864712,  
        "symbol": "BTCUSDT",  
        "status": "EXPIRED",  
        "clientOrderId": "testTaker1",  
        "price": "20000",  
        "avgPrice": "0.0000",  
        "origQty": "3",  
        "executedQty": "0",  
        "cumQuote": "0",  
        "timeInForce": "GTC",  
        "type": "LIMIT",  
        "reduceOnly": false,  
        "closePosition": false,  
        "side": "SELL",  
        "positionSide": "BOTH",  
        "stopPrice": "0",  
        "workingType": "CONTRACT_PRICE",  
        "priceMatch": "NONE",  
        "selfTradePreventionMode": "EXPIRE_MAKER",  
        "goodTillDate": "null",  
        "priceProtect": false,  
        "origType": "LIMIT",  
        "time": 1692849639460,  
        "updateTime": 1692849639460  
    }

---

# 自我交易预防 (Self Trade Prevention - STP) 常见问题

## 什么是 Self Trade Prevention - STP?[​](/docs/zh-CN/derivatives/usds-margined-futures/faq/stp-faq#什么是-self-trade-prevention---stp "什么是 Self Trade Prevention - STP?的直接链接")

自我交易预防是指阻止订单与来自同一账户或者同一 `tradeGroupId` 账户的订单交易。

## 什么是自我交易（self-trade）?[​](/docs/zh-CN/derivatives/usds-margined-futures/faq/stp-faq#什么是自我交易self-trade "什么是自我交易（self-trade）?的直接链接")

在以下任一情况下都可能发生自我交易：

  * 属于同一账户的订单之间交易。
  * 属于相同 `tradeGroupId` 的账户的订单之间交易。



## STP 触发时会发生什么？[​](/docs/zh-CN/derivatives/usds-margined-futures/faq/stp-faq#stp-触发时会发生什么 "STP 触发时会发生什么？的直接链接")

如果订单会触发自我交易，系统将执行三种可能的模式：

`EXPIRE_TAKER` \- 此模式通过立即使吃单者(taker)的剩余数量过期来预防交易。

`EXPIRE_MAKER` \- 此模式通过立即使潜在挂单者(maker)的剩余数量过期来预防交易。

`EXPIRE_BOTH` \- 此模式通过立即同时使吃单和挂单者的剩余数量过期来预防交易。

STP 的发生取决于 **Taker 订单** 的 STP 模式。   
因此，订单薄上的订单的 STP 模式不再有效果，并且将在所有未来的订单处理中被忽略。

## 如何在订单上设置自我交易预防 ？[​](/docs/zh-CN/derivatives/usds-margined-futures/faq/stp-faq#如何在订单上设置自我交易预防- "如何在订单上设置自我交易预防 ？的直接链接")

自我交易预防可以通过下单接口的参数`selfTradePreventionMode`设置，相关接口如下：

  * POST `/fapi/v1/order`
  * POST `/fapi/v1/batchOrders`



## 什么是交易组 Id（Trade Group Id）?[​](/docs/zh-CN/derivatives/usds-margined-futures/faq/stp-faq#什么是交易组-idtrade-group-id "什么是交易组 Id（Trade Group Id）?的直接链接")

属于同一 `tradeGroupId` 的账户被视为同一交易组。相同交易组成员提交的订单有 STP 资格。

每个账户可以从 `GET /fapi/v1/accountConfig`（REST API）确认账户是否属于同一个 `tradeGroupId`。

`tradeGroupId` 也存在 `GET /api/v3/preventedMatches`（Rest API）或 `myPreventedMatches`（Websocket API）的响应中。

如果该值为 `-1`，这表示账户未设置 `tradeGroupId`，因此 STP 只能发生在同一账户的订单之间。

我们将在之后的更新提供将子账户设置为同一`tradeGroupId`的功能

## 如何知道有那些交易对支持 STP?[​](/docs/zh-CN/derivatives/usds-margined-futures/faq/stp-faq#如何知道有那些交易对支持-stp "如何知道有那些交易对支持 STP?的直接链接")

所有`GET fapi/v1/exchangeInfo`中的交易对都支持`selfTradePreventionMode`。

## 哪些订单类型支持 STP？[​](/docs/zh-CN/derivatives/usds-margined-futures/faq/stp-faq#哪些订单类型支持-stp "哪些订单类型支持 STP？的直接链接")

`LIMIT`/`MARKET`/`STOP`/`TAKE_PROFIT`/`STOP_MARKET`/`TAKE_PROFIT_MARKET`/`TRAILING_STOP_MARKET` 在Time in force(timeInForce)设置为`GTC`/ `IOC`/ `GTD`时支持STP。 当Time in force(timeInForce)为`FOK` 或 `GTX`时订单STP设置不生效

## 改单是否支持 STP?[​](/docs/zh-CN/derivatives/usds-margined-futures/faq/stp-faq#改单是否支持-stp "改单是否支持 STP?的直接链接")

目前不支持。改单会将订单的`selfTradePreventionMode` 重制为 `NONE`

## 如何知道订单因为 STP 而过期？[​](/docs/zh-CN/derivatives/usds-margined-futures/faq/stp-faq#如何知道订单因为-stp-而过期 "如何知道订单因为 STP 而过期？的直接链接")

订单的状态会是 `EXPIRED_IN_MATCH`.

在用户信息流推送 `ORDER_TRADE_UPDATE`，如果订单因为STP过期字段`X`会显示`EXPIRED_IN_MATCH`
    
    
    {  
      "e":"ORDER_TRADE_UPDATE",      // Event Type  
      "E":1568879465651,             // Event Time  
      "T":1568879465650,             // Transaction Time  
      "o":{                               
        "s":"BTCUSDT",               // Symbol  
        "c":"TEST",                  // Client Order Id  
          // special client order id:  
          // starts with "autoclose-": liquidation order  
          // "adl_autoclose": ADL auto close order  
          // "settlement_autoclose-": settlement order for delisting or delivery  
        "S":"SELL",                  // Side  
        "o":"TRAILING_STOP_MARKET",  // Order Type  
        "f":"GTC",                   // Time in Force  
        "q":"0.001",                 // Original Quantity  
        "p":"0",                     // Original Price  
        "ap":"0",                    // Average Price  
        "sp":"7103.04",              // Stop Price. Please ignore with TRAILING_STOP_MARKET order  
        "x":"EXPIRED",               // Execution Type  
        "X":"EXPIRED_IN_MATCH",      // Order Status  
        "i":8886774,                 // Order Id  
        "l":"0",                     // Order Last Filled Quantity  
        "z":"0",                     // Order Filled Accumulated Quantity  
        "L":"0",                     // Last Filled Price  
        "N":"USDT",                  // Commission Asset, will not push if no commission  
        "n":"0",                     // Commission, will not push if no commission  
        "T":1568879465650,           // Order Trade Time  
        "t":0,                       // Trade Id  
        "b":"0",                     // Bids Notional  
        "a":"9.91",                  // Ask Notional  
        "m":false,                   // Is this trade the maker side?  
        "R":false,                   // Is this reduce only  
        "wt":"CONTRACT_PRICE",       // Stop Price Working Type  
        "ot":"TRAILING_STOP_MARKET", // Original Order Type  
        "ps":"LONG",                 // Position Side  
        "cp":false,                  // If Close-All, pushed with conditional order  
        "AP":"7476.89",              // Activation Price, only puhed with TRAILING_STOP_MARKET order  
        "cr":"5.0",                  // Callback Rate, only puhed with TRAILING_STOP_MARKET order  
        "pP": false,                 // ignore  
        "si": 0,                     // ignore  
        "ss": 0,                     // ignore  
        "rp":"0",                    // Realized Profit of the trade  
        "V": "EXPIRE_MAKER",         // selfTradePreventionMode  
        "pm":"QUEUE",                // price match type  
        "gtd":1768879465650          // good till date  
       }  
    }  
    

## STP 的一些示例:[​](/docs/zh-CN/derivatives/usds-margined-futures/faq/stp-faq#stp-的一些示例 "STP 的一些示例:的直接链接")

假设以下示例的所有订单都是在同一个账户下发送。

**情况 A - 用户发送带有`EXPIRE_MAKER` 的订单，该订单将与订单薄上已有的订单撮合。**
    
    
    Maker 订单 1: symbol=BTCUSDT side=BUY  type=LIMIT quantity=1 price=20002 selfTradePreventionMode=EXPIRE_MAKER  
    Maker 订单 2: symbol=BTCUSDT side=BUY  type=LIMIT quantity=1 price=20001 selfTradePreventionMode=EXPIRE_MAKER  
    Taker 订单 1: symbol=BTCUSDT side=SELL type=LIMIT quantity=1 price=20000 selfTradePreventionMode=EXPIRE_MAKER  
    

**结果:** : 由于 STP，订单薄上的订单将会过期，taker 订单将继续在订单薄。

Maker 订单 1
    
    
    {  
        "orderId": 292864710,  
        "symbol": "BTCUSDT",  
        "status": "FILLED",  
        "clientOrderId": "testMaker1",  
        "price": "20002",  
        "avgPrice": "20002",  
        "origQty": "1",  
        "executedQty": "1",  
        "cumQuote": "20002",  
        "timeInForce": "GTC",  
        "type": "LIMIT",  
        "reduceOnly": false,  
        "closePosition": false,  
        "side": "BUY",  
        "positionSide": "BOTH",  
        "stopPrice": "0",  
        "workingType": "CONTRACT_PRICE",  
        "priceMatch": "NONE",  
        "selfTradePreventionMode": "EXPIRE_MAKER",  
        "goodTillDate": "null",  
        "priceProtect": false,  
        "origType": "LIMIT",  
        "time": 1692849639460,  
        "updateTime": 1692849639460  
    }  
    

Maker 订单 2
    
    
    {  
        "orderId": 292864711,  
        "symbol": "BTCUSDT",  
        "status": "EXPIRED_IN_MATCH",  
        "clientOrderId": "testMaker2",  
        "price": "20001",  
        "avgPrice": "0.0000",  
        "origQty": "1",  
        "executedQty": "0",  
        "cumQuote": "0",  
        "timeInForce": "GTC",  
        "type": "LIMIT",  
        "reduceOnly": false,  
        "closePosition": false,  
        "side": "BUY",  
        "positionSide": "BOTH",  
        "stopPrice": "0",  
        "workingType": "CONTRACT_PRICE",  
        "priceMatch": "NONE",  
        "selfTradePreventionMode": "EXPIRE_MAKER",  
        "goodTillDate": "null",  
        "priceProtect": false,  
        "origType": "LIMIT",  
        "time": 1692849639460,  
        "updateTime": 1692849639460  
    }  
    

Taker 订单的响应
    
    
    {  
        "orderId": 292864712,  
        "symbol": "BTCUSDT",  
        "status": "PARTIALLY_FILLED",  
        "clientOrderId": "testTaker1",  
        "price": "20000",  
        "avgPrice": "20002",  
        "origQty": "2",  
        "executedQty": "1",  
        "cumQuote": "20002",  
        "timeInForce": "GTC",  
        "type": "LIMIT",  
        "reduceOnly": false,  
        "closePosition": false,  
        "side": "SELL",  
        "positionSide": "BOTH",  
        "stopPrice": "0",  
        "workingType": "CONTRACT_PRICE",  
        "priceMatch": "NONE",  
        "selfTradePreventionMode": "EXPIRE_MAKER",  
        "goodTillDate": "null",  
        "priceProtect": false,  
        "origType": "LIMIT",  
        "time": 1692849639460,  
        "updateTime": 1692849639460  
    }  
    

**情况 B - 用户发送带有`EXPIRE_TAKER` 的订单，该订单将与订单薄上已有的订单撮合。**
    
    
    Maker 订单 1: symbol=BTCUSDT side=BUY  type=LIMIT quantity=1 price=20002  selfTradePreventionMode=EXPIRE_MAKER  
    Maker 订单 2: symbol=BTCUSDT side=BUY  type=LIMIT quantity=1 price=20001  selfTradePreventionMode=EXPIRE_MAKER  
    Taker 订单 1: symbol=BTCUSDT side=SELL type=LIMIT quantity=2 price=3      selfTradePreventionMode=EXPIRE_TAKER  
    

**结果:** : 已经在订单薄上的订单将保留，而taker订单将过期。

Maker 订单 1
    
    
    {  
        "orderId": 292864710,  
        "symbol": "BTCUSDT",  
        "status": "FILLED",  
        "clientOrderId": "testMaker1",  
        "price": "20002",  
        "avgPrice": "0.0000",  
        "origQty": "1",  
        "executedQty": "0",  
        "cumQuote": "0",  
        "timeInForce": "GTC",  
        "type": "LIMIT",  
        "reduceOnly": false,  
        "closePosition": false,  
        "side": "BUY",  
        "positionSide": "BOTH",  
        "stopPrice": "0",  
        "workingType": "CONTRACT_PRICE",  
        "priceMatch": "NONE",  
        "selfTradePreventionMode": "EXPIRE_MAKER",  
        "goodTillDate": "null",  
        "priceProtect": false,  
        "origType": "LIMIT",  
        "time": 1692849639460,  
        "updateTime": 1692849639460  
    }  
    

Maker 订单 2
    
    
    {  
        "orderId": 292864711,  
        "symbol": "BTCUSDT",  
        "status": "EXPIRED_IN_MATCH",  
        "clientOrderId": "testMaker2",  
        "price": "20001",  
        "avgPrice": "0.0000",  
        "origQty": "1",  
        "executedQty": "0",  
        "cumQuote": "0",  
        "timeInForce": "GTC",  
        "type": "LIMIT",  
        "reduceOnly": false,  
        "closePosition": false,  
        "side": "BUY",  
        "positionSide": "BOTH",  
        "stopPrice": "0",  
        "workingType": "CONTRACT_PRICE",  
        "priceMatch": "NONE",  
        "selfTradePreventionMode": "EXPIRE_MAKER",  
        "goodTillDate": "null",  
        "priceProtect": false,  
        "origType": "LIMIT",  
        "time": 1692849639460,  
        "updateTime": 1692849639460  
    }  
    

Taker 订单的状态
    
    
    {  
        "orderId": 292864712,  
        "symbol": "BTCUSDT",  
        "status": "EXPIRED_IN_MATCH",  
        "clientOrderId": "testTaker1",  
        "price": "20000",  
        "avgPrice": "0.0000",  
        "origQty": "3",  
        "executedQty": "0",  
        "cumQuote": "0",  
        "timeInForce": "GTC",  
        "type": "LIMIT",  
        "reduceOnly": false,  
        "closePosition": false,  
        "side": "SELL",  
        "positionSide": "BOTH",  
        "stopPrice": "0",  
        "workingType": "CONTRACT_PRICE",  
        "priceMatch": "NONE",  
        "selfTradePreventionMode": "EXPIRE_TAKER",  
        "goodTillDate": "null",  
        "priceProtect": false,  
        "origType": "LIMIT",  
        "time": 1692849639460,  
        "updateTime": 1692849639460  
    }  
    

**情况 C - 用户发送带有`EXPIRE_BOTH` 的订单，该订单将与订单薄上已有的订单撮合。**
    
    
    Maker 订单: symbol=BTCUSDT side=BUY  type=LIMIT quantity=1 price=20002 selfTradePreventionMode=EXPIRE_MAKER  
    Taker 订单: symbol=BTCUSDT side=SELL type=LIMIT quantity=3 price=20000 selfTradePreventionMode=EXPIRE_BOTH  
    

**结果:** 两个订单都将过期。

Maker 订单
    
    
    {  
        "orderId": 292864710,  
        "symbol": "BTCUSDT",  
        "status": "EXPIRED_IN_MATCH",  
        "clientOrderId": "testMaker1",  
        "price": "20002",  
        "avgPrice": "0.0000",  
        "origQty": "1",  
        "executedQty": "0",  
        "cumQuote": "0",  
        "timeInForce": "GTC",  
        "type": "LIMIT",  
        "reduceOnly": false,  
        "closePosition": false,  
        "side": "BUY",  
        "positionSide": "BOTH",  
        "stopPrice": "0",  
        "workingType": "CONTRACT_PRICE",  
        "priceMatch": "NONE",  
        "selfTradePreventionMode": "EXPIRE_MAKER",  
        "goodTillDate": "null",  
        "priceProtect": false,  
        "origType": "LIMIT",  
        "time": 1692849639460,  
        "updateTime": 1692849639460  
    }  
    

Taker 订单
    
    
    {  
        "orderId": 292864712,  
        "symbol": "BTCUSDT",  
        "status": "EXPIRED_IN_MATCH",  
        "clientOrderId": "testTaker1",  
        "price": "20000",  
        "avgPrice": "0.0000",  
        "origQty": "3",  
        "executedQty": "0",  
        "cumQuote": "0",  
        "timeInForce": "GTC",  
        "type": "LIMIT",  
        "reduceOnly": false,  
        "closePosition": false,  
        "side": "SELL",  
        "positionSide": "BOTH",  
        "stopPrice": "0",  
        "workingType": "CONTRACT_PRICE",  
        "priceMatch": "NONE",  
        "selfTradePreventionMode": "EXPIRE_BOTH",  
        "goodTillDate": "null",  
        "priceProtect": false,  
        "origType": "LIMIT",  
        "time": 1692849639460,  
        "updateTime": 1692849639460  
    }  
    

**情况 D - 用户在订单薄上有一个带有`EXPIRE_MAKER` 的订单，然后发送一个带有 `EXPIRE_TAKER` 的新订单，该订单将与订单薄上的订单撮合。**
    
    
    Maker Order: symbol=BTCUSDT side=BUY  type=LIMIT quantity=1 price=1 selfTradePreventionMode=EXPIRE_MAKER  
    Taker Order: symbol=BTCUSDT side=SELL type=LIMIT quantity=1 price=1 selfTradePreventionMode=EXPIRE_TAKER  
    

**结果:** 将使用 taker 订单的 STP 模式，因此 taker 订单将过期。

Maker 订单
    
    
    {  
        "orderId": 292864710,  
        "symbol": "BTCUSDT",  
        "status": "NEW",  
        "clientOrderId": "testMaker1",  
        "price": "20002",  
        "avgPrice": "0.0000",  
        "origQty": "1",  
        "executedQty": "0",  
        "cumQuote": "0",  
        "timeInForce": "GTC",  
        "type": "LIMIT",  
        "reduceOnly": false,  
        "closePosition": false,  
        "side": "BUY",  
        "positionSide": "BOTH",  
        "stopPrice": "0",  
        "workingType": "CONTRACT_PRICE",  
        "priceMatch": "NONE",  
        "selfTradePreventionMode": "EXPIRE_MAKER",  
        "goodTillDate": "null",  
        "priceProtect": false,  
        "origType": "LIMIT",  
        "time": 1692849639460,  
        "updateTime": 1692849639460  
    }  
    

Taker 订单
    
    
    {  
        "orderId": 292864712,  
        "symbol": "BTCUSDT",  
        "status": "EXPIRED_IN_MATCH",  
        "clientOrderId": "testTaker1",  
        "price": "20000",  
        "avgPrice": "0.0000",  
        "origQty": "3",  
        "executedQty": "0",  
        "cumQuote": "0",  
        "timeInForce": "GTC",  
        "type": "LIMIT",  
        "reduceOnly": false,  
        "closePosition": false,  
        "side": "SELL",  
        "positionSide": "BOTH",  
        "stopPrice": "0",  
        "workingType": "CONTRACT_PRICE",  
        "priceMatch": "NONE",  
        "selfTradePreventionMode": "EXPIRE_TAKER",  
        "goodTillDate": "null",  
        "priceProtect": false,  
        "origType": "LIMIT",  
        "time": 1692849639460,  
        "updateTime": 1692849639460  
    }  
    

**情况 E - 用户发送带有`EXPIRE_MAKER` 的市价订单，该订单将与订单薄上已有的订单撮合。**
    
    
    Maker 订单: symbol=ABCDEF side=BUY  type=LIMIT  quantity=1 price=1  selfTradePreventionMode=EXPIRE_MAKER  
    Taker 订单: symbol=ABCDEF side=SELL type=MARKET quantity=3          selfTradePreventionMode=EXPIRE_MAKER  
    

**结果:** 由于 STP，订单薄上的订单会过期，状态为 `EXPIRED_IN_MATCH`。 由于订单薄上的流动性低，新订单也已过期但状态为 `EXPIRED`。

Maker 订单
    
    
    {  
        "orderId": 292864710,  
        "symbol": "BTCUSDT",  
        "status": "EXPIRED_IN_MATCH",  
        "clientOrderId": "testMaker1",  
        "price": "20002",  
        "avgPrice": "0.0000",  
        "origQty": "1",  
        "executedQty": "0",  
        "cumQuote": "0",  
        "timeInForce": "GTC",  
        "type": "LIMIT",  
        "reduceOnly": false,  
        "closePosition": false,  
        "side": "BUY",  
        "positionSide": "BOTH",  
        "stopPrice": "0",  
        "workingType": "CONTRACT_PRICE",  
        "priceMatch": "NONE",  
        "selfTradePreventionMode": "EXPIRE_MAKER",  
        "goodTillDate": "null",  
        "priceProtect": false,  
        "origType": "LIMIT",  
        "time": 1692849639460,  
        "updateTime": 1692849639460  
    }  
    

Taker 订单
    
    
    {  
        "orderId": 292864712,  
        "symbol": "BTCUSDT",  
        "status": "EXPIRED",  
        "clientOrderId": "testTaker1",  
        "price": "20000",  
        "avgPrice": "0.0000",  
        "origQty": "3",  
        "executedQty": "0",  
        "cumQuote": "0",  
        "timeInForce": "GTC",  
        "type": "LIMIT",  
        "reduceOnly": false,  
        "closePosition": false,  
        "side": "SELL",  
        "positionSide": "BOTH",  
        "stopPrice": "0",  
        "workingType": "CONTRACT_PRICE",  
        "priceMatch": "NONE",  
        "selfTradePreventionMode": "EXPIRE_MAKER",  
        "goodTillDate": "null",  
        "priceProtect": false,  
        "origType": "LIMIT",  
        "time": 1692849639460,  
        "updateTime": 1692849639460  
    }