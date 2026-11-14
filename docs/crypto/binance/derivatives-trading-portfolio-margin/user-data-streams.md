---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/derivatives-trading-portfolio-margin/user-data-streams
api_type: REST
updated_at: 2026-11-13 20:28:11.648237
---

# User Data Streams

## Connect

  * The base API endpoint is: **<https://papi.binance.com>**
  * A User Data Stream `listenKey` is valid for 60 minutes after creation.
  * Doing a `PUT` on a `listenKey` will extend its validity for 60 minutes, if response `-1125` error "This listenKey does not exist." Please use `POST /papi/v1/listenKey` to recreate `listenKey`.
  * Doing a `DELETE` on a `listenKey` will close the stream and invalidate the `listenKey`.
  * Doing a `POST` on an account with an active `listenKey` will return the currently active `listenKey` and extend its validity for 60 minutes.
  * Connection method for Websocket:
    * Base Url: **wss://fstream.binance.com/pm**
    * User Data Streams are accessed at **/ws/ <listenKey>**
    * Example: `wss://fstream.binance.com/pm/ws/pqia91ma19a5s61cv6a81va65sdf19v8a65a1a5s61cv6a81va65sdf19v8a65a1`
  * **Message Ordering Guarantee** :
    * For the same user on a single Websocket connection, messages of the **same event type** (e.g., `ACCOUNT_UPDATE`, `ORDER_TRADE_UPDATE`) are **strictly ordered** by both `T` (transaction time from Matching Engine) and `E` (event time when the message is generated).
    * **Recommended** : Use the `E` field for ordering updates, especially when:
      * Comparing events across different event types (e.g., `ORDER_TRADE_UPDATE` vs market data streams like `aggTrade`).
      * Events from different services may share the same `T` but have different `E` values due to processing timing.
      * For the same event type on the same connection, both `T` and `E` remain strictly ordered, so either field can be used reliably.
  * A single connection is only valid for 24 hours; expect to be disconnected at the 24 hour mark
  * Considering that RESTful endpoints may experience query delays under volatile market conditions, we strongly recommend prioritizing Websocket user data stream messages for retrieving orders, positions, and other information.



* * *

## Event: Futures Balance and Position Update

### Description

Event type is `ACCOUNT_UPDATE`.

  * When balance or position get updated, this event will be pushed.

    * `ACCOUNT_UPDATE` will be pushed only when update happens on user's account, including changes on balances, positions, or margin type.
    * Unfilled orders or cancelled orders will not make the event `ACCOUNT_UPDATE` pushed, since there's no change on positions.
    * "position" in `ACCOUNT_UPDATE`: Only symbols of changed positions will be pushed.
  * When "FUNDING FEE" changes to the user's balance, the event will be pushed with the brief message:

    * When "FUNDING FEE" occurs in a **crossed position** , `ACCOUNT_UPDATE` will be pushed with the balance `B` (including the "FUNDING FEE" asset only) and symbol, without any position `P` message.
    * When "FUNDING FEE" occurs in an **isolated position** , `ACCOUNT_UPDATE` will be pushed with the balance `B` (including the "FUNDING FEE" asset only), symbol and the relative position message `P` (including the isolated position on which the "FUNDING FEE" occurs only, without any other position message).
  * The field "m" represents the reason type for the event and may shows the following possible types:

    * DEPOSIT
    * WITHDRAW
    * ORDER
    * FUNDING_FEE
    * WITHDRAW_REJECT
    * ADJUSTMENT
    * INSURANCE_CLEAR
    * ADMIN_DEPOSIT
    * ADMIN_WITHDRAW
    * MARGIN_TRANSFER
    * MARGIN_TYPE_CHANGE
    * ASSET_TRANSFER
    * OPTIONS_PREMIUM_FEE
    * OPTIONS_SETTLE_PROFIT
    * AUTO_EXCHANGE
    * COIN_SWAP_DEPOSIT
    * COIN_SWAP_WITHDRAW
  * The field "bc" represents the balance change except for PnL and commission.




### Event Name

`ACCOUNT_UPDATE`

### Update Speed

50ms

### Payload

> **Schema:** [`accountUpdate`](/en/docs/catalog/advanced-trading-derivatives-trading-portfolio-margin/api/ws-streams/~schemas#accountupdate)

Loading schema...

* * *

## Event: Futures Order Update

### Description

When new order created, order status changed will push such event. Event type is `ORDER_TRADE_UPDATE`.

**Side**

  * BUY
  * SELL



**Order Type**

  * MARKET
  * LIMIT
  * LIQUIDATION



**Execution Type**

  * NEW
  * CANCELED
  * CALCULATED - Liquidation Execution
  * EXPIRED
  * TRADE



**Order Status**

  * NEW
  * PARTIALLY_FILLED
  * FILLED
  * CANCELED
  * EXPIRED
  * EXPIRED_IN_MATCH



**Time in force**

  * GTC
  * IOC
  * FOK
  * GTX



**Liquidation and ADL:**

  * If user gets liquidated due to insufficient margin balance:
    * `c` shows as "autoclose-XXX", `X` shows as "NEW"
  * If user has enough margin balance but gets ADL:
    * `c` shows as "adl_autoclose", `X` shows as "NEW"



### Event Name

`ORDER_TRADE_UPDATE`

### Payload

> **Schema:** [`orderTradeUpdate`](/en/docs/catalog/advanced-trading-derivatives-trading-portfolio-margin/api/ws-streams/~schemas#ordertradeupdate)

Loading schema...

* * *

## Event: Futures Account Configuration Update (Leverage Update)

### Description

When the account configuration is changed, the event type will be pushed as `ACCOUNT_CONFIG_UPDATE`. When the leverage of a trade pair changes, the payload will contain the object `ac` to represent the account configuration of the trade pair, where `s` represents the specific trade pair and `l` represents the leverage.

### Event Name

`ACCOUNT_CONFIG_UPDATE`

### Payload

> **Schema:** [`accountConfigUpdate`](/en/docs/catalog/advanced-trading-derivatives-trading-portfolio-margin/api/ws-streams/~schemas#accountconfigupdate)

Loading schema...

* * *

## Event: Conditional Order Trade Update

### Description

When new order created, order status changed will push such event. Event type is `CONDITIONAL_ORDER_TRADE_UPDATE`.

**Side**

  * BUY
  * SELL



**Conditional Order Type**

  * STOP
  * TAKE_PROFIT
  * STOP_MARKET
  * TAKE_PROFIT_MARKET
  * TRAILING_STOP_MARKET



**Execution Type**

  * NEW
  * CANCELED
  * CALCULATED - Liquidation Execution
  * EXPIRED
  * TRADE



**Order Status**

  * NEW
  * CANCELED
  * EXPIRED
  * TRIGGERED
  * FINISHED



**Time in force**

  * GTC
  * IOC
  * FOK
  * GTX



### Event Name

`CONDITIONAL_ORDER_TRADE_UPDATE`

### Payload

> **Schema:** [`conditionalOrderTradeUpdate`](/en/docs/catalog/advanced-trading-derivatives-trading-portfolio-margin/api/ws-streams/~schemas#conditionalordertradeupdate)

Loading schema...

* * *

## Event: Margin Balance Update

### Description

Margin Balance Update

### Event Name

`balanceUpdate`

### Payload

> **Schema:** [`balanceUpdate`](/en/docs/catalog/advanced-trading-derivatives-trading-portfolio-margin/api/ws-streams/~schemas#balanceupdate)

Loading schema...

* * *

## Event: Margin Order Update

### Description

Margin orders are updated with the `executionReport` event.

**Execution types:**

  * NEW - The order has been accepted into the engine.
  * CANCELED - The order has been canceled by the user.
  * REJECTED - The order has been rejected and was not processed (This message appears only with Cancel Replace Orders wherein the new order placement is rejected but the request to cancel request succeeds.)
  * TRADE - Part of the order or all of the order's quantity has filled.
  * EXPIRED - The order was canceled according to the order type's rules (e.g. LIMIT FOK orders with no fill, LIMIT IOC or MARKET orders that partially fill) or by the exchange, (e.g. orders canceled during liquidation, orders canceled during maintenance).
  * TRADE_PREVENTION - The order has expired due to STP trigger.



### Event Name

`executionReport`

### Payload

> **Schema:** [`executionReport`](/en/docs/catalog/advanced-trading-derivatives-trading-portfolio-margin/api/ws-streams/~schemas#executionreport)

Loading schema...

* * *

## Event: Margin Account Update

### Description

`outboundAccountPosition` is sent any time an account balance has changed and contains the assets that were possibly changed by the event that generated the balance change.

### Event Name

`outboundAccountPosition`

### Payload

> **Schema:** [`outboundAccountPosition`](/en/docs/catalog/advanced-trading-derivatives-trading-portfolio-margin/api/ws-streams/~schemas#outboundaccountposition)

Loading schema...

* * *

## Event: Liability Update

### Description

Margin Liability update

### Event Name

`liabilityChange`

### Payload

> **Schema:** [`liabilityChange`](/en/docs/catalog/advanced-trading-derivatives-trading-portfolio-margin/api/ws-streams/~schemas#liabilitychange)

Loading schema...

* * *

## Event: OpenOrderLoss Update

### Description

Cross margin order margin stream

### Event Name

`openOrderLoss`

### Payload

> **Schema:** [`openOrderLoss`](/en/docs/catalog/advanced-trading-derivatives-trading-portfolio-margin/api/ws-streams/~schemas#openorderloss)

Loading schema...

* * *

## Event: Risk Level Change

### Description

  * When the user's position risk ratio is too high, this stream will be pushed.
  * This message is only used as risk guidance information and is not recommended for investment strategies.
  * `RISK_LEVEL_CHANGE` includes following types: `MARGIN_CALL`, `REDUCE_ONLY`, `FORCE_LIQUIDATION`
  * In the case of a highly volatile market, there may be the possibility that the user's position has been liquidated at the same time when this stream is pushed out.



### Event Name

`RISK_LEVEL_CHANGE`

### Payload

> **Schema:** [`riskLevelChange`](/en/docs/catalog/advanced-trading-derivatives-trading-portfolio-margin/api/ws-streams/~schemas#risklevelchange)

Loading schema...

* * *

## Event: Algo Order Update

### Description

When new algo order created, order status changed will push such event. Event type is `ALGO_UPDATE`.

**Algo Status:**

  * `NEW`: Conditional order was successfully placed but has not yet been triggered.
  * `CANCELED`: Conditional order has been canceled.
  * `TRIGGERING`: Order has met the triggering condition and has been forwarded to the matching engine.
  * `TRIGGERED`: Order has been successfully placed into the matching engine.
  * `FINISHED`: Triggered conditional order has been filled or canceled in the matching engine.
  * `REJECTED`: Conditional order has been denied by the matching engine (e.g. margin check failures).
  * `EXPIRED`: Conditional order has been canceled by the system.



### Event Name

`ALGO_UPDATE`

### Payload

> **Schema:** [`algoOrderUpdate`](/en/docs/catalog/advanced-trading-derivatives-trading-portfolio-margin/api/ws-streams/~schemas#algoorderupdate)

Loading schema...

* * *

## Event: User Data Stream Expired

### Description

When the `listenKey` used for the user data stream turns expired, this event will be pushed.

**Notice:**

  * This event is not related to the websocket disconnection.
  * This event will be received only when a valid `listenKey` in connection got expired.
  * No more user data event will be updated after this event received until a new valid `listenKey` used.



### Event Name

`listenKeyExpired`

### Payload

> **Schema:** [`listenKeyExpired`](/en/docs/catalog/advanced-trading-derivatives-trading-portfolio-margin/api/ws-streams/~schemas#listenkeyexpired)

Loading schema...

Was this page helpful?

Last modified on November 12, 2026

[General Info](/en/docs/products/derivatives-trading-portfolio-margin/general-info)[Error Codes](/en/docs/products/derivatives-trading-portfolio-margin/error-code)

---

# 账户信息流

## 连接

  * 本篇所列出REST接口的baseurl **<https://papi.binance.com>**
  * 用于订阅账户数据的 `listenKey` 从创建时刻起有效期为60分钟
  * 可以通过`PUT`一个`listenKey`延长60分钟有效期，如收到`-1125`报错提示此`listenKey`不存在，建议重新使用`POST /papi/v1/listenKey`生成`listenKey`
  * 可以通过`DELETE`一个 `listenKey` 立即关闭当前数据流，并使该`listenKey` 无效
  * 在具有有效`listenKey`的帐户上执行`POST`将返回当前有效的`listenKey`并将其有效期延长60分钟
  * Websocket连接方式：
    * Base Url: **wss://fstream.binance.com/pm**
    * 订阅账户数据流的stream名称为 **/ws/ <listenKey>**
    * 连接样例：`wss://fstream.binance.com/pm/ws/pqia91ma19a5s61cv6a81va65sdf19v8a65a1a5s61cv6a81va65sdf19v8a65a1`
  * 每个链接有效期不超过24小时，请妥善处理断线重连。
  * **消息顺序保证** :
    * 对于同一用户的单一 Websocket 连接，**相同事件类型** 的消息(例如 `ACCOUNT_UPDATE`、`ORDER_TRADE_UPDATE`)在 `T`(来自撮合引擎的成交时间)和 `E`(消息生成时的事件时间)两个字段上都**严格有序** 。
    * **建议** :使用 `E` 字段进行更新排序，特别是在以下情况下:
      * 比较不同事件类型的事件时(例如 `ORDER_TRADE_UPDATE` 与市场数据流如 `aggTrade`)。
      * 来自不同服务的事件可能具有相同的 `T` 但由于处理时间的差异而具有不同的 `E` 值。
      * 对于同一连接上的相同事件类型，`T` 和 `E` 都保持严格有序，因此可以可靠地使用任一字段。
  * 考虑到剧烈行情下, RESTful接口可能存在查询延迟，我们强烈建议您优先从Websocket user data stream推送的消息来获取订单，仓位等信息。



* * *

## 合约Balance和Position更新推送

### 事件描述

账户更新事件的 event type 固定为 `ACCOUNT_UPDATE`

  * 当账户信息有变动时，会推送此事件：

    * 仅当账户信息有变动时(包括资金、仓位、保证金模式等发生变化)，才会推送此事件；
    * 订单状态变化没有引起账户和持仓变化的，不会推送此事件；
    * position 信息：仅当symbol仓位有变动时推送。
  * "FUNDING FEE" 引起的资金余额变化，仅推送简略事件：

    * 当用户某**全仓** 持仓发生"FUNDING FEE"时，事件`ACCOUNT_UPDATE`将推送相关的用户资产余额信息`B`(仅推送FUNDING FEE 发生相关的资产余额信息)和交易对`S`，而不会推送任何持仓信息`P`。
    * 当用户某**逐仓** 仓持仓发生"FUNDING FEE"时，事件`ACCOUNT_UPDATE`将推送相关的用户资产余额信息`B`(仅推送"FUNDING FEE"所使用的资产余额信息)、交易对`S`，和相关的持仓信息`P`(仅推送这笔"FUNDING FEE"发生所在的持仓信息)，其余持仓信息不会被推送。
  * 字段"m"代表了事件推出的原因，包含了以下可能类型:

    * DEPOSIT
    * WITHDRAW
    * ORDER
    * FUNDING_FEE
    * WITHDRAW_REJECT
    * ADJUSTMENT
    * INSURANCE_CLEAR
    * ADMIN_DEPOSIT
    * ADMIN_WITHDRAW
    * MARGIN_TRANSFER
    * MARGIN_TYPE_CHANGE
    * ASSET_TRANSFER
    * OPTIONS_PREMIUM_FEE
    * OPTIONS_SETTLE_PROFIT
    * AUTO_EXCHANGE
    * COIN_SWAP_DEPOSIT
    * COIN_SWAP_WITHDRAW
  * 字段"bc"代表了钱包余额的改变量，即 balance change，但注意其不包含仓位盈亏及交易手续费。




### 事件类型

`ACCOUNT_UPDATE`

### 更新速度

50ms

### Payload

> **Schema:** [`accountUpdate`](/zh-CN/docs/catalog/advanced-trading-derivatives-trading-portfolio-margin/api/ws-streams/~schemas#accountupdate)

Loading schema...

* * *

## 合约订单/交易更新推送

### 事件描述

当有新订单创建、订单有新成交或者新的状态变化时会推送此类事件，事件类型统一为 `ORDER_TRADE_UPDATE`

**订单方向**

  * BUY 买入
  * SELL 卖出



**订单类型**

  * MARKET 市价单
  * LIMIT 限价单
  * LIQUIDATION 强平单



**本次事件的具体执行类型**

  * NEW
  * CANCELED 已撤
  * CALCULATED 订单 ADL 或爆仓
  * EXPIRED 订单失效
  * TRADE 交易



**订单状态**

  * NEW
  * PARTIALLY_FILLED
  * FILLED
  * CANCELED
  * EXPIRED
  * EXPIRED_IN_MATCH



**有效方式**

  * GTC
  * IOC
  * FOK
  * GTX



**强平和 ADL:**

  * 若用户因保证金不足发生强平：
    * `c`为"autoclose-XXX"，`X`为"NEW"
  * 若用户保证金充足但被 ADL:
    * `c`为"adl_autoclose"，`X`为"NEW"



### 事件类型

`ORDER_TRADE_UPDATE`

### Payload

> **Schema:** [`orderTradeUpdate`](/zh-CN/docs/catalog/advanced-trading-derivatives-trading-portfolio-margin/api/ws-streams/~schemas#ordertradeupdate)

Loading schema...

* * *

## 合约杠杆倍数等账户配置更新推送

### 事件描述

当账户配置发生变化时会推送此类事件，类型统一为`ACCOUNT_CONFIG_UPDATE`。当交易对杠杆倍数发生变化时，推送消息体会包含对象`ac`表示交易对账户配置，其中`s`代表具体的交易对，`l`代表杠杆倍数。

### 事件类型

`ACCOUNT_CONFIG_UPDATE`

### Payload

> **Schema:** [`accountConfigUpdate`](/zh-CN/docs/catalog/advanced-trading-derivatives-trading-portfolio-margin/api/ws-streams/~schemas#accountconfigupdate)

Loading schema...

* * *

## 合约条件订单/交易更新推送

### 事件描述

当有新订单创建、订单有新成交或者新的状态变化时会推送此类事件，事件类型统一为 `CONDITIONAL_ORDER_TRADE_UPDATE`

**订单方向**

  * BUY 买入
  * SELL 卖出



**条件订单类型**

  * STOP
  * TAKE_PROFIT
  * STOP_MARKET
  * TAKE_PROFIT_MARKET
  * TRAILING_STOP_MARKET



**本次事件的具体执行类型**

  * NEW
  * CANCELED 已撤
  * CALCULATED 订单 ADL 或爆仓
  * EXPIRED 订单失效
  * TRADE 交易



**订单状态**

  * NEW
  * CANCELED
  * EXPIRED
  * TRIGGERED
  * FINISHED



**有效方式**

  * GTC
  * IOC
  * FOK
  * GTX



### 事件类型

`CONDITIONAL_ORDER_TRADE_UPDATE`

### Payload

> **Schema:** [`conditionalOrderTradeUpdate`](/zh-CN/docs/catalog/advanced-trading-derivatives-trading-portfolio-margin/api/ws-streams/~schemas#conditionalordertradeupdate)

Loading schema...

* * *

## 杠杆账户余额更新事件

### 事件描述

杠杆账户余额更新事件

### 事件类型

`balanceUpdate`

### Payload

> **Schema:** [`balanceUpdate`](/zh-CN/docs/catalog/advanced-trading-derivatives-trading-portfolio-margin/api/ws-streams/~schemas#balanceupdate)

Loading schema...

* * *

## 杠杆账户订单事件

### 事件描述

杠杆账户订单由`executionReport`事件推出

**执行类型:**

  * NEW - 新订单已被引擎接受。
  * CANCELED - 订单被用户取消。
  * REJECTED - 新订单被拒绝 （这信息只会在撤消挂单再下单中发生，下新订单被拒绝但撤消挂单请求成功）。
  * TRADE - 订单有新成交。
  * EXPIRED - 订单已根据 Time In Force 参数的规则取消（e.g. 没有成交的 LIMIT FOK 订单或部分成交的 LIMIT IOC 订单）或者被交易所取消（e.g. 强平或维护期间取消的订单）。
  * TRADE_PREVENTION - 订单因 STP 触发而过期。



### 事件类型

`executionReport`

### Payload

> **Schema:** [`executionReport`](/zh-CN/docs/catalog/advanced-trading-derivatives-trading-portfolio-margin/api/ws-streams/~schemas#executionreport)

Loading schema...

* * *

## 杠杆账户更新事件

### 事件描述

每当帐户余额发生更改时，都会发送一个事件`outboundAccountPosition`，其中包含可能由生成余额变动的事件而变动的资产。

### 事件类型

`outboundAccountPosition`

### Payload

> **Schema:** [`outboundAccountPosition`](/zh-CN/docs/catalog/advanced-trading-derivatives-trading-portfolio-margin/api/ws-streams/~schemas#outboundaccountposition)

Loading schema...

* * *

## 杠杆账户负债更新

### 事件描述

杠杆账户负债更新

### 事件类型

`liabilityChange`

### Payload

> **Schema:** [`liabilityChange`](/zh-CN/docs/catalog/advanced-trading-derivatives-trading-portfolio-margin/api/ws-streams/~schemas#liabilitychange)

Loading schema...

* * *

## 杠杆账户全仓挂单占用事件

### 事件描述

杠杆账户全仓挂单占用事件

### 事件类型

`openOrderLoss`

### Payload

> **Schema:** [`openOrderLoss`](/zh-CN/docs/catalog/advanced-trading-derivatives-trading-portfolio-margin/api/ws-streams/~schemas#openorderloss)

Loading schema...

* * *

## 账户风险状态变动

### 事件描述

  * 当用户持仓风险过高，会推送此消息。
  * 此消息仅作为风险指导信息，不建议用于投资策略。
  * `RISK_LEVEL_CHANGE`包含如下事件：`MARGIN_CALL`, `REDUCE_ONLY`, `FORCE_LIQUIDATION`
  * 在大波动市场行情下，不排除此消息发出的同时用户仓位已被强平的可能。



### 事件类型

`RISK_LEVEL_CHANGE`

### Payload

> **Schema:** [`riskLevelChange`](/zh-CN/docs/catalog/advanced-trading-derivatives-trading-portfolio-margin/api/ws-streams/~schemas#risklevelchange)

Loading schema...

* * *

## 条件订单更新推送

### 事件描述

当有新条件订单创建、订单状态变化时会推送此类事件。事件类型为 `ALGO_UPDATE`。

**条件单状态:**

  * `NEW`: 条件订单已提交，但尚未触发。
  * `CANCELED`: 条件订单已被取消。
  * `TRIGGERING`: 条件订单已满足触发条件，且已被转发至撮合引擎。
  * `TRIGGERED`: 条件订单已成功触发并进入撮合引擎。
  * `FINISHED`: 触发的条件订单已在撮合引擎中被成交或取消。
  * `REJECTED`: 条件订单被撮合引擎拒绝（例如保证金检查失败）。
  * `EXPIRED`: 条件订单被系统取消。



### 事件类型

`ALGO_UPDATE`

### Payload

> **Schema:** [`algoOrderUpdate`](/zh-CN/docs/catalog/advanced-trading-derivatives-trading-portfolio-margin/api/ws-streams/~schemas#algoorderupdate)

Loading schema...

* * *

## listenKey过期推送

### 事件描述

当前连接使用的有效 listenKey 过期时，user data stream 将会推送此事件。

**注意:**

  * 此事件与 websocket 连接中断没有必然联系
  * 只有正在连接中的有效`listenKey`过期时才会收到此消息
  * 收到此消息后 user data stream 将不再更新，直到用户使用新的有效的`listenKey`



### 事件类型

`listenKeyExpired`

### Payload

> **Schema:** [`listenKeyExpired`](/zh-CN/docs/catalog/advanced-trading-derivatives-trading-portfolio-margin/api/ws-streams/~schemas#listenkeyexpired)

Loading schema...

此页面是否有帮助？

Last modified on November 12, 2026

[基本信息](/zh-CN/docs/products/derivatives-trading-portfolio-margin/general-info)[错误代码](/zh-CN/docs/products/derivatives-trading-portfolio-margin/error-code)