---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/margin-trading/trade-data-stream
api_type: Trading
updated_at: 2026-11-16 18:30:15.257342
---

# (deprecated) Trade Data Stream

## Connect

  * The base API endpoint is: **<https://api.binance.com>**
  * A User Data Stream `listenKey` is valid for 60 minutes after creation.
  * Doing a `PUT` on a `listenKey` will extend its validity for 60 minutes.
  * Doing a `DELETE` on a `listenKey` will close the stream and invalidate the `listenKey`.
  * Doing a `POST` on an account with an active `listenKey` will return the currently active `listenKey` and extend its validity for 60 minutes.
  * A `listenKey` is a stream.
  * Users can listen to multiple streams.
  * The base websocket endpoint is: **wss://stream.binance.com:9443**
  * User Data Streams are accessed at **/ws/ <listenKey>** or **/stream?streams= <listenKey>**
  * A single connection to **stream.binance.com** is only valid for 24 hours; expect to be disconnected at the 24 hour mark



* * *

## Event: Order Update

### Description

Orders are updated with the `executionReport` event.

**Execution types:**

  * NEW - The order has been accepted into the engine.
  * CANCELED - The order has been canceled by the user.
  * REPLACED (currently unused)
  * REJECTED - The order has been rejected and was not processed (This message appears only with Cancel Replace Orders wherein the new order placement is rejected but the request to cancel request succeeds.)
  * TRADE - Part of the order or all of the order's quantity has filled.
  * EXPIRED - The order was canceled according to the order type's rules (e.g. LIMIT FOK orders with no fill, LIMIT IOC or MARKET orders that partially fill) or by the exchange, (e.g. orders canceled during liquidation, orders canceled during maintenance).
  * TRADE_PREVENTION - The order has expired due to STP trigger.



### Event Name

`executionReport`

### Payload

> **Schema:** [`executionReport`](/en/docs/catalog/core-trading-margin-trading/api/ws-streams/~schemas#executionreport)

Loading schema...

If the order is an OCO, an event will be displayed named `listStatus` in addition to the `executionReport` event.

> **Schema:** [`listStatus`](/en/docs/catalog/core-trading-margin-trading/api/ws-streams/~schemas#liststatus)

Loading schema...

* * *

## Event: Account Update

### Description

`outboundAccountPosition` is sent any time an account balance has changed and contains the assets that were possibly changed by the event that generated the balance change.

### Event Name

`outboundAccountPosition`

### Payload

> **Schema:** [`outboundAccountPosition`](/en/docs/catalog/core-trading-margin-trading/api/ws-streams/~schemas#outboundaccountposition)

Loading schema...

* * *

## Event: Balance Update

### Description

Balance Update occurs during the following:

  * Deposits or withdrawals from the account
  * Transfer of funds between accounts (e.g. Spot to Margin)



### Event Name

`balanceUpdate`

### Payload

> **Schema:** [`balanceUpdate`](/en/docs/catalog/core-trading-margin-trading/api/ws-streams/~schemas#balanceupdate)

Loading schema...

* * *

## Event: Listen Key Expire

### Description

This event is sent when the listen key expires. No more events will be sent after this until a new listenKey is created. This event will not be pushed when the stream is closed normally.

### Event Name

`listenKeyExpired`

### Payload

> **Schema:** [`listenKeyExpired`](/en/docs/catalog/core-trading-margin-trading/api/ws-streams/~schemas#listenkeyexpired)

Loading schema...

Was this page helpful?

Last modified on November 16, 2026

[Risk Data Stream](/en/docs/products/margin-trading/risk-data-stream)[Listen Token User Data Stream](/en/docs/products/margin-trading/listen-token-data-stream)

---

# （已弃用）交易数据流

## 连接

  * 本篇所列出 API 接口的 base URL : **<https://api.binance.com>**
  * 用于订阅账户数据的 `listenKey` 从创建时刻起有效期为60分钟。
  * 可以通过 `PUT` 一个 `listenKey` 延长60分钟有效期。
  * 可以通过 `DELETE` 一个 `listenKey` 立即关闭当前数据流，并使该 `listenKey` 无效。
  * 在具有有效 `listenKey` 的帐户上执行`POST`将返回当前有效的 `listenKey` 并将其有效期延长60分钟。
  * 一个`listenKey`就是一个数据流。
  * 用户可以侦听/订阅数个数据流。
  * websocket 接口的 base URL: **wss://stream.binance.com:9443**
  * 订阅账户数据流的 stream 名称为 **/ws/ <listenKey>** 或 **/stream?streams= <listenKey>**
  * 每个链接有效期不超过24小时，请妥善处理断线重连。
  * 账户数据流的消息不保证严格时间序; **请使用 E 字段进行排序**



* * *

## 订单更新

### 事件描述

订单通过`executionReport`事件进行更新。

**执行类型:**

  * NEW - 新订单已被引擎接受。
  * CANCELED - 订单被用户取消。
  * REPLACED - (保留字段，当前未使用)
  * REJECTED - 新订单被拒绝 （这信息只会在撤消挂单再下单中发生，下新订单被拒绝但撤消挂单请求成功）。
  * TRADE - 订单有新成交。
  * EXPIRED - 订单已根据 Time In Force 参数的规则取消（e.g. 没有成交的 LIMIT FOK 订单或部分成交的 LIMIT IOC 订单）或者被交易所取消（e.g. 强平或维护期间取消的订单）。
  * TRADE_PREVENTION - 订单因 STP 触发而过期。



### 事件类型

`executionReport`

### Payload

> **Schema:** [`executionReport`](/zh-CN/docs/catalog/core-trading-margin-trading/api/ws-streams/~schemas#executionreport)

`{ "e": "executionReport", // Event type "E": 1499405658658, // Event time "s": "ETHBTC", // Symbol "c": "mUvoqJxFIILMdfAW5iGSOW", // Client order ID "S": "BUY", // Side "o": "LIMIT", // Order type "f": "GTC", // Time in force "q": "1.00000000", // Order quantity "p": "0.10264410", // Order price "P": "0.00000000", // Stop price "F": "0.00000000", // Iceberg quantity "g": -1, // OrderListId "C": "", // Original client order ID; This is the ID of the order being canceled "x": "NEW", // Current execution type "X": "NEW", // Current order status "r": "NONE", // Order reject reason; will be an error code. "i": 4293153, // Order ID "l": "0.00000000", // Last executed quantity "z": "0.00000000", // Cumulative filled quantity "L": "0.00000000", // Last executed price "n": "0", // Commission amount "N": "null", // Commission asset "T": 1499405658657, // Transaction time "t": -1, // Trade ID "I": 8641984, // Ignore "w": true, // Is the order on the book? "m": false, // Is this trade the maker side? "M": false, // Ignore "O": 1499405658657, // Order creation time "Z": "0.00000000", // Cumulative quote asset transacted quantity "Y": "0.00000000", // Last quote asset transacted quantity (i.e. lastPrice * lastQty) "Q": "0.00000000", // Quote Order Quantity "W": 1499405658657, // Working Time; This is only visible if the order has been placed on the book. "V": "NONE", // selfTradePreventionMode "d": 4, // Trailing Delta; This is only visible if the order was a trailing stop order. "D": 1668680518494, // Trailing Time "j": 1, // Strategy Id "J": 1000000, // Strategy Type "v": 3, // Prevented Match Id "A": "3.000000", // Prevented Quantity "B": "3.000000", // Last Prevented Quantity "u": 1, // Trade Group Id "U": 37, // Counter Order Id "Cs": "BTCUSDT", // Counter Symbol "pl": "2.123456", // Prevented Execution Quantity "pL": "0.10000001", // Prevented Execution Price "pY": "0.21234562", // Prevented Execution Quote Qty "b": "ONE_PARTY_TRADE_REPORT", // Match Type "a": 1234, // Allocation ID "k": "SOR", // Working Floor "uS": true // UsedSor }`

如果订单是OCO，则除了显示`executionReport`事件外，还将显示一个名为`ListStatus`的事件。

> **Schema:** [`listStatus`](/zh-CN/docs/catalog/core-trading-margin-trading/api/ws-streams/~schemas#liststatus)

`{ "e": "listStatus", // Event Type "E": 1564035303637, // Event Time "s": "ETHBTC", // Symbol "g": 2, // OrderListId "c": "OCO", // Contingency Type "l": "EXEC_STARTED", // List Status Type "L": "EXECUTING", // List Order Status "r": "NONE", // List Reject Reason "C": "F4QN4G8DlFATFlIUQ0cjdD", // List Client Order ID "T": 1564035303625, // Transaction Time "O": [ // An array of objects { "s": "ETHBTC", // Symbol "i": 17, // orderId "c": "AJYsMjErWJesZvqlJCTUgL" // ClientOrderId } ] }`

* * *

## 账户更新

### 事件描述

每当帐户余额发生更改时，都会发送一个事件`outboundAccountPosition`，其中包含可能由生成余额变动的事件而变动的资产。

### 事件类型

`outboundAccountPosition`

### Payload

> **Schema:** [`outboundAccountPosition`](/zh-CN/docs/catalog/core-trading-margin-trading/api/ws-streams/~schemas#outboundaccountposition)

`{ "e": "outboundAccountPosition", // Event type "E": 1564034571105, // Event Time "u": 1564034571073, // Time of last account update "B": [ // Balances Array { "a": "ETH", // Asset "f": "10000.000000", // Free "l": "0.000000" // Locked } ] }`

* * *

## 余额更新

### 事件描述

当下列情形发生时更新:

  * 账户发生充值或提取
  * 交易账户之间发生划转(例如 现货向杠杆账户划转)



### 事件类型

`balanceUpdate`

### Payload

> **Schema:** [`balanceUpdate`](/zh-CN/docs/catalog/core-trading-margin-trading/api/ws-streams/~schemas#balanceupdate)

`{ "e": "balanceUpdate", // Event Type "E": 1573200697110, // Event Time "a": "BTC", // Asset "d": "100.00000000", // Balance Delta "T": 1573200697068 // Clear Time }`

* * *

## Listen Key已过期

### 事件描述

当监听 listen key 过期时会发送此事件。此后不会再发送任何事件，直到创建新的 listenKey。正常关闭流时不会推送该事件。

### 事件类型

`listenKeyExpired`

### Payload

> **Schema:** [`listenKeyExpired`](/zh-CN/docs/catalog/core-trading-margin-trading/api/ws-streams/~schemas#listenkeyexpired)

`{ "e": "listenKeyExpired", // Event type "E": "1699596037418", // Event time "listenKey": "OfYGbUzi3PraNagEkdKuFwUHn48brFsItTdsuiIXrucEvD0rhRXZ7I6URWfE8YE8" }`

此页面是否有帮助？

Last modified on November 16, 2026

[风险数据流](/zh-CN/docs/products/margin-trading/risk-data-stream)[Listen Token 用户数据流](/zh-CN/docs/products/margin-trading/listen-token-data-stream)