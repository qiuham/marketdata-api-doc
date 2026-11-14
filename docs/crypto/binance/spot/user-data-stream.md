---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/spot/user-data-stream
api_type: REST
updated_at: 2026-11-13 20:27:24.287908
---

# User Data Streams for Binance

## General information

  * Subscribe via the [WebSocket API](/en/docs/catalog/core-trading-spot-trading/api/ws-api/user-data-stream#user-data-stream-subscribe) using an API Key.
  * Both [SBE](/en/docs/products/spot/faqs/sbe_faq) and JSON output are supported.
  * Account events are pushed in **real-time**.
  * All timestamps in JSON payloads are in **milliseconds by default**.
  * Events may contain non-ASCII characters encoded in UTF-8 if you own or trade any assets or symbols whose names contain non-ASCII characters.
  * You can also filter specific events. Please see [User Data Stream Subscription Filters](/en/docs/catalog/core-trading-spot-trading/api/ws-api/user-data-stream#user-data-stream-subscription-filters) for more information.



## User Data Stream Events

### Account Update

`outboundAccountPosition` is sent any time an account balance has changed and contains the assets that were possibly changed by the event that generated the balance change.

> **Schema:** [`outboundAccountPosition`](/en/docs/catalog/core-trading-spot-trading/api/ws-streams/~schemas#outboundaccountposition)

`{ "e": "outboundAccountPosition", // Event type "E": 1564034571105, // Event Time "u": 1564034571073, // Time of last account update "B": [ // Balances Array { "a": "ETH", // Asset "f": "10000.000000", // Free "l": "0.000000" // Locked } ] }`

### Balance Update

Balance Update occurs during the following:

  * Deposits or withdrawals from the account
  * Transfer of funds between accounts (e.g. Spot to Margin)



**Payload**

> **Schema:** [`balanceUpdate`](/en/docs/catalog/core-trading-spot-trading/api/ws-streams/~schemas#balanceupdate)

`{ "e": "balanceUpdate", // Event Type "E": 1573200697110, // Event Time "a": "BTC", // Asset "d": "100.00000000", // Balance Delta "T": 1573200697068 // Clear Time }`

### Order Update

Orders are updated with the `executionReport` event.

**Payload:**

> **Schema:** [`executionReport`](/en/docs/catalog/core-trading-spot-trading/api/ws-streams/~schemas#executionreport)

`{ "e": "executionReport", // Event type "E": 1499405658658, // Event time "s": "ETHBTC", // Symbol "c": "mUvoqJxFIILMdfAW5iGSOW", // Client order ID "S": "BUY", // Side "o": "LIMIT", // Order type "f": "GTC", // Time in force "q": "1.00000000", // Order quantity "p": "0.10264410", // Order price "P": "0.00000000", // Stop price "F": "0.00000000", // Iceberg quantity "g": -1, // OrderListId "C": "", // Original client order ID; This is the ID of the order being canceled "x": "NEW", // Current execution type "X": "NEW", // Current order status "r": "NONE", // Order reject reason; Please see Order Reject Reason for more information. "i": 4293153, // Order ID "l": "0.00000000", // Last executed quantity "z": "0.00000000", // Cumulative filled quantity "L": "0.00000000", // Last executed price "n": "0", // Commission amount "N": null, // Commission asset "T": 1499405658657, // Transaction time "t": -1, // Trade ID "v": 3, // Prevented Match Id; This is only visible if the order expired due to STP "I": 8641984, // Execution Id "w": true, // Is the order on the book? "m": false, // Is this trade the maker side? "M": false, // Ignore "O": 1499405658657, // Order creation time "Z": "0.00000000", // Cumulative quote asset transacted quantity "Y": "0.00000000", // Last quote asset transacted quantity (i.e. lastPrice * lastQty) "Q": "0.00000000", // Quote Order Quantity "W": 1499405658657, // Working Time; This is only visible if the order has been placed on the book. "V": "NONE", // SelfTradePreventionMode "d": 4, // Trailing Delta "D": 1668680518494, // Trailing Time "j": 1, // Strategy Id "J": 1000000, // Strategy Type "A": "3.000000", // Prevented Quantity "B": "3.000000", // Last Prevented Quantity "u": 1, // Trade Group Id "U": 37, // Counter Order Id "Cs": "BTCUSDT", // Counter Symbol "pl": "2.123456", // Prevented Execution Quantity "pL": "0.10000001", // Prevented Execution Price "pY": "0.21234562", // Prevented Execution Quote Qty "Qq": "90.00000000", // Quote Notional Limit. Appears only if the order was placed with a quote notional limit. "eV": "DECREMENT", // Effective Self Trade Prevention Mode. Appears on prevented-match reports when the applied STP mode differs from the order's `selfTradePreventionMode`. Values: `EXPIRE_MAKER`, `EXPIRE_BOTH`, `DECREMENT`. "b": "ONE_PARTY_TRADE_REPORT", // Match Type "a": 1234, // Allocation ID "k": "SOR", // Working Floor "uS": true, // UsedSor "gP": "PRIMARY_PEG", // Pegged Price Type "gOT": "PRICE_LEVEL", // Pegged Offset Type "gOV": 5, // Pegged Offset Value "gp": "1.00000000", // Pegged Price "eR": "INSUFFICIENT_LIQUIDITY" // Expiry Reason. Appears when the order has expired. }`

**Note:** Average price can be found by doing `Z` divided by `z`.

#### Conditional Fields in Execution Report

These are fields that appear in the payload only if certain conditions are met.

For additional information on these parameters, please refer to the [Spot Glossary](/en/docs/products/spot/faqs/spot_glossary).

Field| Name| Description| Examples  
---|---|---|---  
`d`| Trailing Delta| Appears only for trailing stop orders.| `"d": 4`  
`D`| Trailing Time| Appears only for trailing stop orders.| `"D": 1668680518494`  
`j`| Strategy Id| Appears only if the `strategyId` parameter was provided upon order placement.| `"j": 1`  
`J`| Strategy Type| Appears only if the `strategyType` parameter was provided upon order placement.| `"J": 1000000`  
`v`| Prevented Match Id| Appears only for orders that expired due to STP.| `"v": 3`  
`A`| Prevented Quantity| Appears only for orders that expired due to STP.| `"A": "3.000000"`  
`B`| Last Prevented Quantity| Appears only for orders that expired due to STP.| `"B": "3.000000"`  
`u`| Trade Group Id| Appears only for orders that expired due to STP.| `"u": 1`  
`U`| Counter Order Id| Appears only for orders that expired due to STP.| `"U": 37`  
`Cs`| Counter Symbol| Appears only for orders that expired due to STP.| `"Cs": "BTCUSDT"`  
`pl`| Prevented Execution Quantity| Appears only for orders that expired due to STP.| `"pl": "2.123456"`  
`pL`| Prevented Execution Price| Appears only for orders that expired due to STP.| `"pL": "0.10000001"`  
`pY`| Prevented Execution Quote Qty| Appears only for orders that expired due to STP.| `"pY": "0.21234562"`  
`Qq`| Quote Notional Limit| Appears only if the order was placed with a quote notional limit.| `"Qq": "90.00000000"`  
`eV`| Effective Self Trade Prevention Mode| Appears on prevented-match reports when the applied STP mode differs from the order's `selfTradePreventionMode`. Values: `EXPIRE_MAKER`, `EXPIRE_BOTH`, `DECREMENT`.| `"eV": "DECREMENT"`  
`W`| Working Time| Appears when the order is working on the book| `"W": 1668683798379`  
`b`| Match Type| Appears for orders that have allocations| `"b": "ONE_PARTY_TRADE_REPORT"`  
`a`| Allocation ID| Appears for orders that have allocations| `"a": 1234`  
`k`| Working Floor| Appears for orders that potentially have allocations| `"k": "SOR"`  
`uS`| UsedSor| Appears for orders that used SOR| `"uS": true`  
`gP`| Pegged Price Type| Appears only for Pegged Orders| `"gP": "PRIMARY_PEG"`  
`gOT`| Pegged Offset Type| Appears only for Pegged Orders| `"gOT": "PRICE_LEVEL"`  
`gOV`| Pegged Offset Value| Appears only for Pegged Orders| `"gOV": 5`  
`gp`| Pegged Price| Appears only for Pegged Orders| `"gp": "1.00000000"`  
`eR`| Expiry Reason| Appears when the order has expired.| `"eR": "INSUFFICIENT_LIQUIDITY"`  
  
#### Order Reject Reason

For additional details, look up the Error Message in the [Errors](/en/docs/products/spot/errors#messages-for--1010-error_msg_received--2010-new_order_rejected--2011-cancel_rejected-and--2038-order_amend_rejected) documentation.

Rejection Reason (`r`)| Error Message  
---|---  
`NONE`| N/A (i.e. The order was not rejected.)  
`INSUFFICIENT_BALANCES`| "Account has insufficient balance for requested action."  
`STOP_PRICE_WOULD_TRIGGER_IMMEDIATELY`| "Order would trigger immediately."  
`WOULD_MATCH_IMMEDIATELY`| "Order would immediately match and take."  
`OCO_BAD_PRICES`| "The relationship of the prices for the orders is not correct."  
  
If the order is an order list, an event named `ListStatus` will be sent in addition to the `executionReport` event.

**Payload**

> **Schema:** [`listStatus`](/en/docs/catalog/core-trading-spot-trading/api/ws-streams/~schemas#liststatus)

`{ "e": "listStatus", // Event Type "E": 1564035303637, // Event Time "s": "ETHBTC", // Symbol "g": 2, // OrderListId "c": "OCO", // Contingency Type "l": "EXEC_STARTED", // List Status Type "L": "EXECUTING", // List Order Status "r": "NONE", // List Reject Reason "C": "F4QN4G8DlFATFlIUQ0cjdD", // List Client Order ID "T": 1564035303625, // Transaction Time "O": [ // An array of objects { "s": "ETHBTC", // Symbol "i": 17, // OrderId "c": "AJYsMjErWJesZvqlJCTUgL" // ClientOrderId } ] }`

**Execution types:**

See [Execution types](/en/docs/products/spot/enums#execution-types) on the Enums page for what each `x` / `X` value means.

#### Order Expiry Reason

See [Expiry Reasons](/en/docs/products/spot/enums#expiry-reasons) on the Enums page for what each `eR` value means.

Check the [Enums page](/en/docs/products/spot/enums) for more relevant enum definitions.

## Event Stream Terminated

`eventStreamTerminated` is sent when:

  * [A listen token subscription](/en/docs/products/margin-trading/listen-token-data-stream#websocket-api-method--userdatastreamsubscribelistentoken) expires due to token expiration.
  * A [logon subscription](/en/docs/catalog/core-trading-spot-trading/api/ws-api/auth#session-logon) ends after sending [`session.logout`](/en/docs/catalog/core-trading-spot-trading/api/ws-api/auth#session-logout) method.
  * The subscription is stopped via the [`userDataStream.unsubscribe`](/en/docs/catalog/core-trading-spot-trading/api/ws-api/user-data-stream#user-data-stream-unsubscribe) method.



**Payload:**

> **Schema:** [`eventStreamTerminated`](/en/docs/catalog/core-trading-spot-trading/api/ws-streams/~schemas#eventstreamterminated)

`{ "e": "eventStreamTerminated", // Event Type "E": 1728973001334 // Event Time }`

## External Lock Update

`externalLockUpdate` is sent when part of your spot wallet balance is locked/unlocked by an external system, for example when used as margin collateral.

**Payload:**

> **Schema:** [`externalLockUpdate`](/en/docs/catalog/core-trading-spot-trading/api/ws-streams/~schemas#externallockupdate)

`{ "e": "externalLockUpdate", // Event Type "E": 1581557507324, // Event Time "a": "NEO", // Asset "d": "10.00000000", // Delta "T": 1581557507268 // Transaction Time }`

Was this page helpful?

Last modified on November 12, 2026

[FIX Schemas](/en/docs/products/spot/fix/schemas/introduction)[Terms of Use](/en/docs/products/spot/PROD-TERMS-OF-USE)

---

# WebSocket 账户接口

## 一般信息

  * 通过使用 API Key 订阅 [WebSocket API](/zh-CN/docs/catalog/core-trading-spot-trading/api/ws-api/user-data-stream#user-data-stream-subscribe)。
  * 支持 [SBE](/zh-CN/docs/products/spot/faqs/sbe_faq) 和 JSON 输出格式。
  * 账户事件以 **实时** 方式推送。
  * JSON 数据中的所有时间戳默认均为 **毫秒** 。
  * 如果您持有或交易任何名称包含非 ASCII 字符的资产或交易对，那么事件中可能包含以 UTF-8 编码的非 ASCII 字符。
  * 您也可以只订阅特定的事件。详情请参阅 [用户数据流订阅过滤器](/zh-CN/docs/catalog/core-trading-spot-trading/api/ws-api/user-data-stream#user-data-stream-subscription-filters)。



## 用户数据流事件

### 账户更新

每当帐户余额发生更改时，都会发送一个事件`outboundAccountPosition`，其中包含可能由生成余额变动的事件而变动的资产。

> **Schema:** [`outboundAccountPosition`](/zh-CN/docs/catalog/core-trading-spot-trading/api/ws-streams/~schemas#outboundaccountposition)

`{ "e": "outboundAccountPosition", // Event type "E": 1564034571105, // Event Time "u": 1564034571073, // Time of last account update "B": [ // Balances Array { "a": "ETH", // Asset "f": "10000.000000", // Free "l": "0.000000" // Locked } ] }`

### 余额更新

当下列情形发生时更新:

  * 账户发生充值或提取
  * 交易账户之间发生划转(例如 现货向杠杆账户划转)



**Payload**

> **Schema:** [`balanceUpdate`](/zh-CN/docs/catalog/core-trading-spot-trading/api/ws-streams/~schemas#balanceupdate)

`{ "e": "balanceUpdate", // Event Type "E": 1573200697110, // Event Time "a": "BTC", // Asset "d": "100.00000000", // Balance Delta "T": 1573200697068 // Clear Time }`

### 订单更新

订单通过`executionReport`事件进行更新。

**Payload:**

> **Schema:** [`executionReport`](/zh-CN/docs/catalog/core-trading-spot-trading/api/ws-streams/~schemas#executionreport)

`{ "e": "executionReport", // Event type "E": 1499405658658, // Event time "s": "ETHBTC", // Symbol "c": "mUvoqJxFIILMdfAW5iGSOW", // Client order ID "S": "BUY", // Side "o": "LIMIT", // Order type "f": "GTC", // Time in force "q": "1.00000000", // Order quantity "p": "0.10264410", // Order price "P": "0.00000000", // Stop price "F": "0.00000000", // Iceberg quantity "g": -1, // OrderListId "C": "", // Original client order ID; This is the ID of the order being canceled "x": "NEW", // Current execution type "X": "NEW", // Current order status "r": "NONE", // Order reject reason; Please see Order Reject Reason for more information. "i": 4293153, // Order ID "l": "0.00000000", // Last executed quantity "z": "0.00000000", // Cumulative filled quantity "L": "0.00000000", // Last executed price "n": "0", // Commission amount "N": null, // Commission asset "T": 1499405658657, // Transaction time "t": -1, // Trade ID "v": 3, // Prevented Match Id; This is only visible if the order expired due to STP "I": 8641984, // Execution Id "w": true, // Is the order on the book? "m": false, // Is this trade the maker side? "M": false, // Ignore "O": 1499405658657, // Order creation time "Z": "0.00000000", // Cumulative quote asset transacted quantity "Y": "0.00000000", // Last quote asset transacted quantity (i.e. lastPrice * lastQty) "Q": "0.00000000", // Quote Order Quantity "W": 1499405658657, // Working Time; This is only visible if the order has been placed on the book. "V": "NONE", // SelfTradePreventionMode "d": 4, // Trailing Delta "D": 1668680518494, // Trailing Time "j": 1, // Strategy Id "J": 1000000, // Strategy Type "A": "3.000000", // Prevented Quantity "B": "3.000000", // Last Prevented Quantity "u": 1, // Trade Group Id "U": 37, // Counter Order Id "Cs": "BTCUSDT", // Counter Symbol "pl": "2.123456", // Prevented Execution Quantity "pL": "0.10000001", // Prevented Execution Price "pY": "0.21234562", // Prevented Execution Quote Qty "Qq": "90.00000000", // Quote Notional Limit. Appears only if the order was placed with a quote notional limit. "eV": "DECREMENT", // Effective Self Trade Prevention Mode. Appears on prevented-match reports when the applied STP mode differs from the order's `selfTradePreventionMode`. Values: `EXPIRE_MAKER`, `EXPIRE_BOTH`, `DECREMENT`. "b": "ONE_PARTY_TRADE_REPORT", // Match Type "a": 1234, // Allocation ID "k": "SOR", // Working Floor "uS": true, // UsedSor "gP": "PRIMARY_PEG", // Pegged Price Type "gOT": "PRICE_LEVEL", // Pegged Offset Type "gOV": 5, // Pegged Offset Value "gp": "1.00000000", // Pegged Price "eR": "INSUFFICIENT_LIQUIDITY" // Expiry Reason. Appears when the order has expired. }`

**备注:** 通过将`Z`除以`z`可以找到平均价格。

#### `executionReport` 中的特定条件时才会出现的字段

这些字段仅在满足特定条件时才会出现。有关这些参数的更多信息，请参阅 [现货交易API术语表](/zh-CN/docs/products/spot/faqs/spot_glossary)。

字段| 名称| 描述| 示例  
---|---|---|---  
`d`| Trailing Delta| 出现在追踪止损订单中。| `"d": 4`  
`D`| Trailing Time| 出现在追踪止损订单中。| `"D": 1668680518494`  
`j`| Strategy Id| 如果在请求中添加了`strategyId`参数，则会出现。| `"j": 1`  
`J`| Strategy Type| 如果在请求中添加了`strategyType`参数，则会出现。| `"J": 1000000`  
`v`| Prevented Match Id| 只有在因为 STP 导致订单失效时可见。| `"v": 3`  
`A`| Prevented Quantity| 只有在因为 STP 导致订单失效时可见。| `"A": "3.000000"`  
`B`| Last Prevented Quantity| 只有在因为 STP 导致订单失效时可见。| `"B": "3.000000"`  
`u`| Trade Group Id| 只有在因为 STP 导致订单失效时可见。| `"u": 1`  
`U`| Counter Order Id| 只有在因为 STP 导致订单失效时可见。| `"U": 37`  
`Cs`| Counter Symbol| 只有在因为 STP 导致订单失效时可见。| `"Cs": "BTCUSDT"`  
`pl`| Prevented Execution Quantity| 只有在因为 STP 导致订单失效时可见。| `"pl": "2.123456"`  
`pL`| Prevented Execution Price| 只有在因为 STP 导致订单失效时可见。| `"pL": "0.10000001"`  
`pY`| Prevented Execution Quote Qty| 只有在因为 STP 导致订单失效时可见。| `"pY": "0.21234562"`  
`Qq`| Quote Notional Limit| 只有在下单时设置了报价资产名义价值上限时可见。| `"Qq": "90.00000000"`  
`eV`| Effective Self Trade Prevention Mode| 在预防撮合的回报中，实际生效的 STP 模式与订单的 `selfTradePreventionMode` 不同时可见。可能的值：`EXPIRE_MAKER`、`EXPIRE_BOTH`、`DECREMENT`。| `"eV": "DECREMENT"`  
`W`| Working Time| 只有在订单在订单簿上时可见| `"W": 1668683798379`  
`b`| Match Type| 只有在订单有分配时可见| `"b": "ONE_PARTY_TRADE_REPORT"`  
`a`| Allocation ID| 只有在订单有分配时可见| `"a": 1234`  
`k`| Working Floor| 只有在订单可能有分配时可见| `"k": "SOR"`  
`uS`| UsedSor| 只有在订单使用 SOR 时可见| `"uS": true`  
`gP`| Pegged Price Type| 仅出现在挂钩订单中| `"gP": "PRIMARY_PEG"`  
`gOT`| Pegged Offset Type| 仅出现在挂钩订单中| `"gOT": "PRICE_LEVEL"`  
`gOV`| Pegged Offset Value| 仅出现在挂钩订单中| `"gOV": 5`  
`gp`| Pegged Price| 仅出现在挂钩订单中| `"gp": "1.00000000"`  
`eR`| Expiry Reason| 出现在订单已过期时。| `"eR": "INSUFFICIENT_LIQUIDITY"`  
  
#### 订单拒绝原因

有关更多详细信息，请查阅 [错误代码汇总](/zh-CN/docs/products/spot/errors#messages-for--1010-error_msg_received--2010-new_order_rejected--2011-cancel_rejected-and--2038-order_amend_rejected) 文档中的错误消息。

拒绝原因 (`r`)| 错误信息  
---|---  
`NONE`| N/A (i.e. The order was not rejected.)  
`INSUFFICIENT_BALANCES`| "Account has insufficient balance for requested action."  
`STOP_PRICE_WOULD_TRIGGER_IMMEDIATELY`| "Order would trigger immediately."  
`WOULD_MATCH_IMMEDIATELY`| "Order would immediately match and take."  
`OCO_BAD_PRICES`| "The relationship of the prices for the orders is not correct."  
  
如果是一个订单组，则除了显示 `executionReport` 事件外，还将显示一个名为 `ListStatus` 的事件。

**Payload**

> **Schema:** [`listStatus`](/zh-CN/docs/catalog/core-trading-spot-trading/api/ws-streams/~schemas#liststatus)

`{ "e": "listStatus", // Event Type "E": 1564035303637, // Event Time "s": "ETHBTC", // Symbol "g": 2, // OrderListId "c": "OCO", // Contingency Type "l": "EXEC_STARTED", // List Status Type "L": "EXECUTING", // List Order Status "r": "NONE", // List Reject Reason "C": "F4QN4G8DlFATFlIUQ0cjdD", // List Client Order ID "T": 1564035303625, // Transaction Time "O": [ // An array of objects { "s": "ETHBTC", // Symbol "i": 17, // OrderId "c": "AJYsMjErWJesZvqlJCTUgL" // ClientOrderId } ] }`

**可能的执行类型:**

每个 `x` / `X` 值的含义请参阅枚举定义页面的 [可能的执行类型](/zh-CN/docs/products/spot/enums#execution-types)。

#### 订单过期原因

每个 `eR` 值的含义请参阅枚举定义页面的 [订单过期原因](/zh-CN/docs/products/spot/enums#expiry-reasons)。

请查阅 [枚举定义](/zh-CN/docs/products/spot/enums) 文档获取更多枚举定义。

## 事件流已终止

`eventStreamTerminated` 会在以下情况下发送：

  * 当 [Listen Token 订阅](/zh-CN/docs/products/margin-trading/listen-token-data-stream) 因 Token 过期而失效时。
  * 在发送 [`session.logout`](/zh-CN/docs/catalog/core-trading-spot-trading/api/ws-api/auth#session-logout) 方法后，[登录订阅](/zh-CN/docs/catalog/core-trading-spot-trading/api/ws-api/auth#session-logon) 结束时。
  * 通过 [`userDataStream.unsubscribe`](/zh-CN/docs/catalog/core-trading-spot-trading/api/ws-api/user-data-stream#user-data-stream-unsubscribe) 方法终止订阅时。



**Payload:**

> **Schema:** [`eventStreamTerminated`](/zh-CN/docs/catalog/core-trading-spot-trading/api/ws-streams/~schemas#eventstreamterminated)

`{ "e": "eventStreamTerminated", // Event Type "E": 1728973001334 // Event Time }`

## 外部锁定更新

当您的现货钱包余额被外部系统锁定/解锁时 （例如，当用作保证金抵押品时），新事件 `externalLockUpdate` 将会被发送。

**Payload:**

> **Schema:** [`externalLockUpdate`](/zh-CN/docs/catalog/core-trading-spot-trading/api/ws-streams/~schemas#externallockupdate)

`{ "e": "externalLockUpdate", // Event Type "E": 1581557507324, // Event Time "a": "NEO", // Asset "d": "10.00000000", // Delta "T": 1581557507268 // Transaction Time }`

此页面是否有帮助？

Last modified on November 12, 2026

[FIX Schemas](/zh-CN/docs/products/spot/fix/schemas/introduction)[使用条款](/zh-CN/docs/products/spot/PROD-TERMS-OF-USE)