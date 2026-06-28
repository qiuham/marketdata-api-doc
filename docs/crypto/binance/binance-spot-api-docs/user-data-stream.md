---
exchange: binance
source_url: https://developers.binance.com/docs/binance-spot-api-docs/user-data-stream
api_type: REST
updated_at: 2026-06-28 18:50:09.200415
---

# User Data Streams for Binance

## General information[​](/docs/binance-spot-api-docs/user-data-stream#general-information "Direct link to General information")

  * Subscribe via the [WebSocket API](/docs/binance-spot-api-docs/websocket-api/user-data-stream-requests#user-data-stream-subscribe) using an API Key.
  * Both [SBE](/docs/binance-spot-api-docs/faqs/sbe_faq) and JSON output are supported.
  * Account events are pushed in **real-time**.
  * All timestamps in JSON payloads are in **milliseconds by default**.
  * Events may contain non-ASCII characters encoded in UTF-8 if you own or trade any assets or symbols whose names contain non-ASCII characters.



## User Data Stream Events[​](/docs/binance-spot-api-docs/user-data-stream#user-data-stream-events "Direct link to User Data Stream Events")

### Account Update[​](/docs/binance-spot-api-docs/user-data-stream#account-update "Direct link to Account Update")

`outboundAccountPosition` is sent any time an account balance has changed and contains the assets that were possibly changed by the event that generated the balance change.
    
    
    {  
        "subscriptionId": 0,  
        "event": {  
            "e": "outboundAccountPosition",     // Event type  
            "E": 1564034571105,                 // Event Time  
            "u": 1564034571073,                 // Time of last account update  
            // Balances Array  
            "B": [  
                {  
                    "a": "ETH",                 // Asset  
                    "f": "10000.000000",        // Free  
                    "l": "0.000000"             // Locked  
                }  
            ]  
        }  
    }  
    

### Balance Update[​](/docs/binance-spot-api-docs/user-data-stream#balance-update "Direct link to Balance Update")

Balance Update occurs during the following:

  * Deposits or withdrawals from the account
  * Transfer of funds between accounts (e.g. Spot to Margin)



**Payload**
    
    
    {  
        "subscriptionId": 0,  
        "event": {  
            "e": "balanceUpdate",     // Event Type  
            "E": 1573200697110,       // Event Time  
            "a": "BTC",               // Asset  
            "d": "100.00000000",      // Balance Delta  
            "T": 1573200697068        // Clear Time  
        }  
    }  
    

### Order Update[​](/docs/binance-spot-api-docs/user-data-stream#order-update "Direct link to Order Update")

Orders are updated with the `executionReport` event.

**Payload:**
    
    
    {  
        "subscriptionId": 0,  
        "event": {  
            "e": "executionReport",            // Event type  
            "E": 1499405658658,                // Event time  
            "s": "ETHBTC",                     // Symbol  
            "c": "mUvoqJxFIILMdfAW5iGSOW",     // Client order ID  
            "S": "BUY",                        // Side  
            "o": "LIMIT",                      // Order type  
            "f": "GTC",                        // Time in force  
            "q": "1.00000000",                 // Order quantity  
            "p": "0.10264410",                 // Order price  
            "P": "0.00000000",                 // Stop price  
            "F": "0.00000000",                 // Iceberg quantity  
            "g": -1,                           // OrderListId  
            "C": "",                           // Original client order ID; This is the ID of the order being canceled  
            "x": "NEW",                        // Current execution type  
            "X": "NEW",                        // Current order status  
            "r": "NONE",                       // Order reject reason; Please see Order Reject Reason (below) for more information.  
            "i": 4293153,                      // Order ID  
            "l": "0.00000000",                 // Last executed quantity  
            "z": "0.00000000",                 // Cumulative filled quantity  
            "L": "0.00000000",                 // Last executed price  
            "n": "0",                          // Commission amount  
            "N": null,                         // Commission asset  
            "T": 1499405658657,                // Transaction time  
            "t": -1,                           // Trade ID  
            "v": 3,                            // Prevented Match Id; This is only visible if the order expired due to STP  
            "I": 8641984,                      // Execution Id  
            "w": true,                         // Is the order on the book?  
            "m": false,                        // Is this trade the maker side?  
            "M": false,                        // Ignore  
            "O": 1499405658657,                // Order creation time  
            "Z": "0.00000000",                 // Cumulative quote asset transacted quantity  
            "Y": "0.00000000",                 // Last quote asset transacted quantity (i.e. lastPrice * lastQty)  
            "Q": "0.00000000",                 // Quote Order Quantity  
            "W": 1499405658657,                // Working Time; This is only visible if the order has been placed on the book.  
            "V": "NONE"                        // SelfTradePreventionMode  
        }  
    }  
    

**Note:** Average price can be found by doing `Z` divided by `z`.

#### Conditional Fields in Execution Report[​](/docs/binance-spot-api-docs/user-data-stream#conditional-fields-in-execution-report "Direct link to Conditional Fields in Execution Report")

These are fields that appear in the payload only if certain conditions are met.

For additional information on these parameters, please refer to the [Spot Glossary](/docs/binance-spot-api-docs/faqs/spot_glossary).

Field | Name | Description | Examples  
---|---|---|---  
`d` | Trailing Delta | Appears only for trailing stop orders. | `"d": 4`  
`D` | Trailing Time | `"D": 1668680518494`  
`j` | Strategy Id | Appears only if the `strategyId` parameter was provided upon order placement. | `"j": 1`  
`J` | Strategy Type | Appears only if the `strategyType` parameter was provided upon order placement. | `"J": 1000000`  
`v` | Prevented Match Id | Appears only for orders that expired due to STP. | `"v": 3`  
`A` | Prevented Quantity | `"A":"3.000000"`  
`B` | Last Prevented Quantity | `"B":"3.000000"`  
`u` | Trade Group Id | `"u":1`  
`U` | Counter Order Id | `"U":37`  
`Cs` | Counter Symbol | `"Cs": "BTCUSDT"`  
`pl` | Prevented Execution Quantity | `"pl":"2.123456"`  
`pL` | Prevented Execution Price | `"pL":"0.10000001"`  
`pY` | Prevented Execution Quote Qty | `"pY":"0.21234562"`  
`W` | Working Time | Appears when the order is working on the book | `"W": 1668683798379`  
`b` | Match Type | Appears for orders that have allocations | `"b":"ONE_PARTY_TRADE_REPORT"`  
`a` | Allocation ID | `"a":1234`  
`k` | Working Floor | Appears for orders that potentially have allocations | `"k":"SOR"`  
`uS` | UsedSor | Appears for orders that used SOR | `"uS":true`  
`gP` | Pegged Price Type | Appears only for Pegged Orders | `"gP": "PRIMARY_PEG"`  
`gOT` | Pegged offset Type | `"gOT": "PRICE_LEVEL"`  
`gOV` | Pegged Offset Value | `"gOV": 5`  
`gp` | Pegged Price | `"gp": "1.00000000"`  
`eR` | Expiry Reason | Appears when the order has expired. | `"eR": "INSUFFICIENT_LIQUIDITY"`  
  
#### Order Reject Reason[​](/docs/binance-spot-api-docs/user-data-stream#order-reject-reason "Direct link to Order Reject Reason")

For additional details, look up the Error Message in the [Errors](/docs/binance-spot-api-docs/errors#other-errors) documentation.

Rejection Reason (`r`)| Error Message  
---|---  
`NONE`| N/A (i.e. The order was not rejected.)  
`INSUFFICIENT_BALANCES`| "Account has insufficient balance for requested action."  
`STOP_PRICE_WOULD_TRIGGER_IMMEDIATELY`| "Order would trigger immediately."  
`WOULD_MATCH_IMMEDIATELY`| "Order would immediately match and take."  
`OCO_BAD_PRICES`| "The relationship of the prices for the orders is not correct."  
  
If the order is an order list, an event named `ListStatus` will be sent in addition to the `executionReport` event.

**Payload**
    
    
    {  
        "subscriptionId": 0,  
        "event": {  
            "e": "listStatus",                        // Event Type  
            "E": 1564035303637,                       // Event Time  
            "s": "ETHBTC",                            // Symbol  
            "g": 2,                                   // OrderListId  
            "c": "OCO",                               // Contingency Type  
            "l": "EXEC_STARTED",                      // List Status Type  
            "L": "EXECUTING",                         // List Order Status  
            "r": "NONE",                              // List Reject Reason  
            "C": "F4QN4G8DlFATFlIUQ0cjdD",            // List Client Order ID  
            "T": 1564035303625,                       // Transaction Time  
            // An array of objects  
            "O": [  
                {  
                    "s": "ETHBTC",                    // Symbol  
                    "i": 17,                          // OrderId  
                    "c": "AJYsMjErWJesZvqlJCTUgL"     // ClientOrderId  
                },  
                {  
                    "s": "ETHBTC",  
                    "i": 18,  
                    "c": "bfYPSQdLoqAJeNrOr9adzq"  
                }  
            ]  
        }  
    }  
    

#### Order Expiry Reason[​](/docs/binance-spot-api-docs/user-data-stream#order-expiry-reason "Direct link to Order Expiry Reason")

Expiry Reason (`eR`)| Explanation  
---|---  
`REJECTED`| A contingent order or an order that was part of an OTO was rejected by the matching engine when trying to place it on the order book. Common reasons are lack of funds and rejection by filters.  
`EXCHANGE_CANCELED`| The order was canceled by Binance.  
`OCO_TRIGGER`| An order that was part of an OCO pair was canceled because the other order of the pair started working or the entire OCO expired.  
`OTO_PHASE_ONE_EXPIRED`| The working order of the order list expired, thus expiring the entire order list.  
`UNFILLED_IOC_QUANTITY_EXPIRED`| The IOC order was not fully filled and thus expired.  
`UNFILLED_FOK_ORDER_EXPIRED`| The FOK order was not fully filled and thus expired.  
`INSUFFICIENT_LIQUIDITY`| There were not enough orders in the order book to match with this order.  
`EXECUTION_RULE_PRICE_RANGE_EXCEEDED`| The order attempted to trade at a price that would not meet the Price Range Execution Rule.  
  
Check the [Enums page](/docs/binance-spot-api-docs/enums) for more relevant enum definitions.

## Event Stream Terminated[​](/docs/binance-spot-api-docs/user-data-stream#event-stream-terminated "Direct link to Event Stream Terminated")

`eventStreamTerminated` is sent when:

  * [A listen token subscription](https://developers.binance.com/docs/margin_trading/trade-data-stream/Listen-Token-Websocket-API#subscribe-to-user-data-stream-using-listentoken-user_stream) expires due to token expiration.
  * A [logon subscription](https://developers.binance.com/docs/binance-spot-api-docs/websocket-api/authentication-requests#log-in-with-api-key-signed) ends after sending [`session.logout`](https://developers.binance.com/docs/binance-spot-api-docs/websocket-api/authentication-requests#log-out-of-the-session) method.
  * The subscription is stopped via the [`userDataStream.unsubscribe`](https://developers.binance.com/docs/binance-spot-api-docs/websocket-api/user-data-stream-requests#unsubscribe-from-user-data-stream) method.



**Payload:**
    
    
    {  
        "subscriptionId": 0,  
        "event": {  
            "e": "eventStreamTerminated",     // Event Type  
            "E": 1728973001334                // Event Time  
        }  
    }  
    

## External Lock Update[​](/docs/binance-spot-api-docs/user-data-stream#external-lock-update "Direct link to External Lock Update")

`externalLockUpdate` is sent when part of your spot wallet balance is locked/unlocked by an external system, for example when used as margin collateral.

**Payload:**
    
    
    {  
        "subscriptionId": 0,  
        "event": {  
            "e": "externalLockUpdate",     // Event Type  
            "E": 1581557507324,            // Event Time  
            "a": "NEO",                    // Asset  
            "d": "10.00000000",            // Delta  
            "T": 1581557507268             // Transaction Time  
        }  
    }

---

# 用户数据流

## 一般信息[​](/docs/zh-CN/binance-spot-api-docs/user-data-stream#一般信息 "一般信息的直接链接")

  * 通过使用 API Key 订阅 [WebSocket API](/docs/zh-CN/binance-spot-api-docs/websocket-api/user-data-stream-requests#user-data-stream-subscribe)。
  * 支持 [SBE](/docs/zh-CN/binance-spot-api-docs/faqs/sbe_faq) 和 JSON 输出格式。
  * 账户事件以 **实时** 方式推送。
  * JSON 数据中的所有时间戳默认均为 **毫秒** 。
  * 如果您持有或交易任何名称包含非 ASCII 字符的资产或交易对，那么事件中可能包含以 UTF-8 编码的非 ASCII 字符。



## 用户数据流事件[​](/docs/zh-CN/binance-spot-api-docs/user-data-stream#用户数据流事件 "用户数据流事件的直接链接")

### 账户更新[​](/docs/zh-CN/binance-spot-api-docs/user-data-stream#账户更新 "账户更新的直接链接")

每当帐户余额发生更改时，都会发送一个事件`outboundAccountPosition`，其中包含可能由生成余额变动的事件而变动的资产。

**Payload**
    
    
    {  
        "subscriptionId": 0,  
        "event": {  
            "e": "outboundAccountPosition",     // 事件类型  
            "E": 1564034571105,                 // 事件时间  
            "u": 1564034571073,                 // 账户末次更新时间戳  
            "B": [                              // 余额  
                {  
                    "a": "ETH",                 // 资产名称  
                    "f": "10000.000000",        // 可用余额  
                    "l": "0.000000"             // 冻结余额  
                }  
            ]  
        }  
    }  
    

### 余额更新[​](/docs/zh-CN/binance-spot-api-docs/user-data-stream#余额更新 "余额更新的直接链接")

当下列情形发生时更新:

  * 账户发生充值或提取
  * 交易账户之间发生划转(例如 现货向杠杆账户划转)



**Payload**
    
    
    {  
        "subscriptionId": 0,  
        "event": {  
            "e": "balanceUpdate",     // 事件类型  
            "E": 1573200697110,       // 事件时间  
            "a": "BTC",               // 资产名称  
            "d": "100.00000000",      // 余额增量  
            "T": 1573200697068        // 清算时间  
        }  
    }  
    

### 订单更新[​](/docs/zh-CN/binance-spot-api-docs/user-data-stream#订单更新 "订单更新的直接链接")

订单通过`executionReport`事件进行更新。

**Payload:**
    
    
    {  
        "subscriptionId": 0,  
        "event": {  
            "e": "executionReport",            // 事件类型  
            "E": 1499405658658,                // 事件时间  
            "s": "ETHBTC",                     // 交易对  
            "c": "mUvoqJxFIILMdfAW5iGSOW",     // clientOrderId  
            "S": "BUY",                        // 订单方向  
            "o": "LIMIT",                      // 订单类型  
            "f": "GTC",                        // 有效方式  
            "q": "1.00000000",                 // 订单原始数量  
            "p": "0.10264410",                 // 订单原始价格  
            "P": "0.00000000",                 // 止盈止损单触发价格  
            "F": "0.00000000",                 // 冰山订单数量  
            "g": -1,                           // OCO订单 OrderListId  
            "C": "",                           // 原始订单自定义ID（原始订单，指撤单操作的对象。撤单本身被视为另一个订单）  
            "x": "NEW",                        // 本次事件的具体执行类型  
            "X": "NEW",                        // 订单的当前状态  
            "r": "NONE",                       // 订单被拒绝的原因；请参阅订单被拒绝的原因（下文）了解更多信息  
            "i": 4293153,                      // orderId  
            "l": "0.00000000",                 // 订单末次成交量  
            "z": "0.00000000",                 // 订单累计已成交量  
            "L": "0.00000000",                 // 订单末次成交价格  
            "n": "0",                          // 佣金数量  
            "N": null,                         // 佣金资产类别  
            "T": 1499405658657,                // 成交时间  
            "t": -1,                           // Trade ID  
            "v": 3,                            // 被阻止的交易Id；仅在订单因为STP被阻止时显示  
            "I": 8641984,                      // Execution ID  
            "w": true,                         // 订单是否在订单簿上？  
            "m": false,                        // 该成交是作为挂单成交吗？  
            "M": false,                        // 请忽略  
            "O": 1499405658657,                // 订单创建时间  
            "Z": "0.00000000",                 // 订单累计已成交金额  
            "Y": "0.00000000",                 // 订单末次成交金额  
            "Q": "0.00000000",                 // Quote Order Quantity  
            "W": 1499405658657,                // Working Time; 订单被添加到 order book 的时间  
            "V": "NONE"                        // SelfTradePreventionMode  
        }  
    }  
    

**备注:** 通过将`Z`除以`z`可以找到平均价格。

#### `executionReport` 中的特定条件时才会出现的字段[​](/docs/zh-CN/binance-spot-api-docs/user-data-stream#executionreport-中的特定条件时才会出现的字段 "executionreport-中的特定条件时才会出现的字段的直接链接")

这些字段仅在满足特定条件时才会出现。有关这些参数的更多信息，请参阅 [现货交易API术语表](/docs/zh-CN/binance-spot-api-docs/faqs/spot_glossary)。

字段 | 名称 | 描述 | 示例  
---|---|---|---  
`d` | Trailing Delta | 出现在追踪止损订单中。 | `"d": 4`  
`D` | Trailing Time | `"D": 1668680518494`  
`j` | Strategy Id | 如果在请求中添加了`strategyId`参数，则会出现。 | `"j": 1`  
`J` | Strategy Type | 如果在请求中添加了`strategyType`参数，则会出现。 | `"J": 1000000`  
`v` | Prevented Match Id | 只有在因为 STP 导致订单失效时可见。 | `"v": 3`  
`A` | Prevented Quantity | `"A":"3.000000"`  
`B` | Last Prevented Quantity | `"B":"3.000000"`  
`u` | Trade Group Id | `"u":1`  
`U` | Counter Order Id | `"U":37`  
`Cs` | Counter Symbol | `"Cs": "BTCUSDT"`  
`pl` | Prevented Execution Quantity | `"pl":"2.123456"`  
`pL` | Prevented Execution Price | `"pL":"0.10000001"`  
`pY` | Prevented Execution Quote Qty | `"pY":"0.21234562"`  
`W` | Working Time | 只有在订单在订单簿上时可见 | `"W": 1668683798379`  
`b` | Match Type | 只有在订单有分配时可见 | `"b":"ONE_PARTY_TRADE_REPORT"`  
`a` | Allocation ID | `"a":1234`  
`k` | Working Floor | 只有在订单可能有分配时可见 | `"k":"SOR"`  
`uS` | UsedSor | 只有在订单使用 SOR 时可见 | `"uS":true`  
`gP` | Pegged Price Type | 仅出现在挂钩订单中 | `"gP": "PRIMARY_PEG"`  
`gOT` | Pegged offset Type | `"gOT": "PRICE_LEVEL"`  
`gOV` | Pegged Offset Value | `"gOV": 5`  
`gp` | Pegged Price | `"gp": "1.00000000"`  
`eR` | Expiry Reason | 当订单已过期时出现。 | `"eR": "INSUFFICIENT_LIQUIDITY"`  
  
#### 订单拒绝原因[​](/docs/zh-CN/binance-spot-api-docs/user-data-stream#订单拒绝原因 "订单拒绝原因的直接链接")

有关更多详细信息，请查阅 [错误代码汇总](/docs/zh-CN/binance-spot-api-docs/errors#other-errors) 文档中的错误消息。

拒绝原因 (`r`)| 错误信息  
---|---  
`NONE`| N/A (i.e. The order was not rejected.)  
`INSUFFICIENT_BALANCES`| "Account has insufficient balance for requested action."  
`STOP_PRICE_WOULD_TRIGGER_IMMEDIATELY`| "Order would trigger immediately."  
`WOULD_MATCH_IMMEDIATELY`| "Order would immediately match and take."  
`OCO_BAD_PRICES`| "The relationship of the prices for the orders is not correct."  
  
如果是一个订单列表，则除了显示 `executionReport` 事件外，还将显示一个名为 `ListStatus` 的事件。

**Payload**
    
    
    {  
        "subscriptionId": 0,  
        "event": {  
            "e": "listStatus",                        // 事件类型  
            "E": 1564035303637,                       // 事件时间  
            "s": "ETHBTC",                            // 交易对  
            "g": 2,                                   // OrderListId  
            "c": "OCO",                               // Contingency 类型  
            "l": "EXEC_STARTED",                      // List 状态类型  
            "L": "EXECUTING",                         // List 订单类型  
            "r": "NONE",                              // List 被拒绝的原因  
            "C": "F4QN4G8DlFATFlIUQ0cjdD",            // List Client Order ID  
            "T": 1564035303625,                       // 成交时间  
            "O": [                                    // 对象数组  
                {  
                    "s": "ETHBTC",                    // 交易对  
                    "i": 17,                          // orderId  
                    "c": "AJYsMjErWJesZvqlJCTUgL"     // clientOrderId  
                },  
                {  
                    "s": "ETHBTC",  
                    "i": 18,  
                    "c": "bfYPSQdLoqAJeNrOr9adzq"  
                }  
            ]  
        }  
    }  
    

#### 订单过期原因[​](/docs/zh-CN/binance-spot-api-docs/user-data-stream#订单过期原因 "订单过期原因的直接链接")

过期原因 (`eR`)| 说明  
---|---  
`REJECTED`| 当尝试将条件单或OTO（One-Triggers-the-Other）订单放入订单簿时，被撮合引擎拒绝。常见原因包括资金不足和过滤器拒绝。  
`EXCHANGE_CANCELED`| 订单被币安取消。  
`OCO_TRIGGER`| OCO（One-Cancels-the-Other）订单对中的一个订单被取消，因为其另一个订单开始生效或整个OCO订单对过期。  
`OTO_PHASE_ONE_EXPIRED`| 订单列表中的生效订单过期，导致整个订单列表过期。  
`UNFILLED_IOC_QUANTITY_EXPIRED`| IOC（立即成交或取消）订单未完全成交，因此过期。  
`UNFILLED_FOK_ORDER_EXPIRED`| FOK（全部成交或取消）订单未完全成交，因此过期。  
`INSUFFICIENT_LIQUIDITY`| 订单簿中没有足够的订单与该订单匹配。  
`EXECUTION_RULE_PRICE_RANGE_EXCEEDED`| 订单尝试以不符合价格区间执行规则的价格进行交易。  
  
请查阅 [枚举定义](/docs/zh-CN/binance-spot-api-docs/enums) 文档获取更多枚举定义。

## 事件流已终止[​](/docs/zh-CN/binance-spot-api-docs/user-data-stream#事件流已终止 "事件流已终止的直接链接")

此事件仅在订阅 WebSocket API 时显示。

`eventStreamTerminated` 会在以下情况下发送：

  * 当 [Listen Token 订阅](https://developers.binance.com/docs/zh-CN/margin_trading/trade-data-stream/Listen-Token-Websocket-API) 因 Token 过期而失效时。
  * 在发送 [`session.logout`](https://developers.binance.com/docs/zh-CN/binance-spot-api-docs/websocket-api/authentication-requests#%E9%80%80%E5%87%BA%E4%BC%9A%E8%AF%9D) 方法后，[登录订阅](https://developers.binance.com/docs/zh-CN/binance-spot-api-docs/websocket-api/authentication-requests#%E7%94%A8api-key%E7%99%BB%E5%BD%95-signed) 结束时。
  * 通过 [`userDataStream.unsubscribe`](https://developers.binance.com/docs/zh-CN/binance-spot-api-docs/websocket-api/user-data-stream-requests#%E5%8F%96%E6%B6%88%E8%AE%A2%E9%98%85%E7%94%A8%E6%88%B7%E6%95%B0%E6%8D%AE%E6%B5%81) 方法终止订阅时。



**Payload:**
    
    
    {  
        "subscriptionId": 0,  
        "event": {  
            "e": "eventStreamTerminated",     // 事件类型  
            "E": 1728973001334                // 事件时间  
        }  
    }  
    

## 外部锁定更新[​](/docs/zh-CN/binance-spot-api-docs/user-data-stream#外部锁定更新 "外部锁定更新的直接链接")

当您的现货钱包余额被外部系统锁定/解锁时 （例如，当用作保证金抵押品时），新事件 `externalLockUpdate` 将会被发送。

**Payload:**
    
    
    {  
        "subscriptionId": 0,  
        "event": {  
            "e": "externalLockUpdate",     // 事件类型  
            "E": 1581557507324,            // 事件时间  
            "a": "NEO",                    // 资产  
            "d": "10.00000000",            // 余额变动量  
            "T": 1581557507268             // 交易时间  
        }  
    }