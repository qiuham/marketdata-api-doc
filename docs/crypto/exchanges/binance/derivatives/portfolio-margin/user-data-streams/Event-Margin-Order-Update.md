---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/portfolio-margin/user-data-streams/Event-Margin-Order-Update
api_type: REST
updated_at: 2026-01-15T23:46:07.542455
---

# Event: Margin Order Update

## Event Description[​](/docs/derivatives/portfolio-margin/user-data-streams/Event-Margin-Order-Update#event-description "Direct link to Event Description")

Margin orders are updated with the `executionReport` event.

**Execution types:**

  * NEW - The order has been accepted into the engine.
  * CANCELED - The order has been canceled by the user.
  * REJECTED - The order has been rejected and was not processed (This message appears only with Cancel Replace Orders wherein the new order placement is rejected but the request to cancel request succeeds.)
  * TRADE - Part of the order or all of the order's quantity has filled.
  * EXPIRED - The order was canceled according to the order type's rules (e.g. LIMIT FOK orders with no fill, LIMIT IOC or MARKET orders that partially fill) or by the exchange, (e.g. orders canceled during liquidation, orders canceled during maintenance).
  * TRADE_PREVENTION - The order has expired due to STP trigger. Check the Public API Definitions for more relevant enum definitions.



## Event Name[​](/docs/derivatives/portfolio-margin/user-data-streams/Event-Margin-Order-Update#event-name "Direct link to Event Name")

`executionReport`

## Response Example[​](/docs/derivatives/portfolio-margin/user-data-streams/Event-Margin-Order-Update#response-example "Direct link to Response Example")
    
    
    {  
      "e": "executionReport",        // Event type  
      "E": 1499405658658,            // Event time  
      "s": "ETHBTC",                 // Symbol  
      "c": "mUvoqJxFIILMdfAW5iGSOW", // Client order ID  
      "S": "BUY",                    // Side  
      "o": "LIMIT",                  // Order type  
      "f": "GTC",                    // Time in force  
      "q": "1.00000000",             // Order quantity  
      "p": "0.10264410",             // Order price  
      "P": "0.00000000",             // Stop price  
      "d": 4,                        // Trailing Delta; This is only visible if the order was a trailing stop order.  
      "F": "0.00000000",             // Iceberg quantity; Will not be visible if not iceberg order  
      "g": -1,                       // OrderListId  
      "C": "",                       // Original client order ID; Only visible on cancellation of order, the ID of the order being canceled.  
      "x": "NEW",                    // Current execution type  
      "X": "NEW",                    // Current order status  
      "r": "NONE",                   // Order reject reason; Only visible if there is a rejection, will be an error code.  
      "i": 4293153,                  // Order ID  
      "l": "0.00000000",             // Last executed quantity  
      "z": "0.00000000",             // Cumulative filled quantity  
      "L": "0.00000000",             // Last executed price  
      "n": "0",                      // Commission amount  
      "N": null,                     // Commission asset; Only visible when there is a commission amount.  
      "T": 1499405658657,            // Transaction time  
      "t": -1,                       // Trade ID  
      "v": 3,                        // Prevented Match Id; This is only visible if the order expire due to STP trigger.  
      "I": 8641984,                  // updateId  
      "w": true,                     // Is the order on the book?  
      "m": false,                    // Is this trade the maker side?  
      "O": 1499405658657,            // Order creation time  
      "Z": "0.00000000",             // Cumulative quote asset transacted quantity  
      "Y": "0.00000000",             // Last quote asset transacted quantity (i.e. lastPrice * lastQty)  
      "Q": "0.00000000",             // Quote Order Quantity; This is only visible if indicated in the order  
      "D": 1668680518494,            // Trailing Time; This is only visible if the trailing stop order has been activated.  
      "j": 1,                        // Strategy ID; This is only visible if the strategyId parameter was provided upon order placement  
      "J": 1000000,                  // Strategy Type; This is only visible if the strategyType parameter was provided upon order placement  
      "W": 1499405658657,            // Working Time; This is only visible if the order has been placed on the book.  
      "V": "NONE",                   // selfTradePreventionMode  
      "u":1,                         // TradeGroupId; This is only visible if the account is part of a trade group and the order expired due to STP trigger.  
      "U":37,                        // CounterOrderId; This is only visible if the order expired due to STP trigger.  
      "A":"3.000000",                // Prevented Quantity; This is only visible if the order expired due to STP trigger.  
      "B":"3.000000"                 // Last Prevented Quantity; This is only visible if the order expired due to STP trigger.  
    }

---

# 杠杆账户订单事件

## 事件描述[​](/docs/zh-CN/derivatives/portfolio-margin/user-data-streams/Event-Margin-Order-Update#事件描述 "事件描述的直接链接")

杠杆账户订单由`executionReport`事件推出

**执行类型:**

  * NEW - 新订单已被引擎接受。
  * CANCELED - 订单被用户取消。
  * REPLACED - (保留字段，当前未使用)
  * REJECTED - 新订单被拒绝 （这信息只会在撤消挂单再下单中发生，下新订单被拒绝但撤消挂单请求成功）。
  * TRADE - 订单有新成交。
  * EXPIRED - 订单已根据 Time In Force 参数的规则取消（e.g. 没有成交的 LIMIT FOK 订单或部分成交的 LIMIT IOC 订单）或者被交易所取消（e.g. 强平或维护期间取消的订单）。
  * TRADE_PREVENTION - 订单因 STP 触发而过期。



## 事件类型[​](/docs/zh-CN/derivatives/portfolio-margin/user-data-streams/Event-Margin-Order-Update#事件类型 "事件类型的直接链接")

`executionReport`

## 响应示例[​](/docs/zh-CN/derivatives/portfolio-margin/user-data-streams/Event-Margin-Order-Update#响应示例 "响应示例的直接链接")
    
    
    {  
      "e": "executionReport",        // 事件类型  
      "E": 1499405658658,            // 事件时间  
      "s": "ETHBTC",                 // 交易对  
      "c": "mUvoqJxFIILMdfAW5iGSOW", // clientOrderId  
      "S": "BUY",                    // 订单方向  
      "o": "LIMIT",                  // 订单类型  
      "f": "GTC",                    // 有效方式  
      "q": "1.00000000",             // 订单原始数量  
      "p": "0.10264410",             // 订单原始价格  
      "P": "0.00000000",             // 止盈止损单触发价格  
      "F": "0.00000000",             // 冰山订单数量; 这仅在冰山订单可见  
      "g": -1,                       // OCO订单 OrderListId  
      "C": "",                       // 原始订单自定义ID(原始订单，指撤单操作的对象。撤单本身被视为另一个订单); 这仅在撤单可见  
      "x": "NEW",                    // 本次事件的具体执行类型  
      "X": "NEW",                    // 订单的当前状态  
      "r": "NONE",                   // 订单被拒绝的原因  
      "i": 4293153,                  // orderId  
      "l": "0.00000000",             // 订单末次成交量  
      "z": "0.00000000",             // 订单累计已成交量  
      "L": "0.00000000",             // 订单末次成交价格  
      "n": "0",                      // 手续费数量  
      "N": null,                     // 手续费资产类别; 这仅在非零的手续费可见  
      "T": 1499405658657,            // 成交时间  
      "t": -1,                       // 成交ID  
      "v": 3,                        // 被阻止撮合交易的ID; 这仅在订单因 STP 触发而过期时可见  
      "I": 8641984,                  // updateId  
      "w": true,                     // 订单是否在订单簿上？  
      "m": false,                    // 该成交是作为挂单成交吗？  
      "O": 1499405658657,            // 订单创建时间  
      "Z": "0.00000000",             // 订单累计已成交金额  
      "Y": "0.00000000",             // 订单末次成交金额  
      "Q": "0.00000000",             // Quote Order Quantity; 这仅在订单中明确标明可见  
      "W": 1499405658657,            // Working Time; 订单被添加到 order book 的时间  
      "V": "NONE"                    // SelfTradePreventionMode  
    }