---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/derivatives-trading-options/user-data-streams
api_type: WebSocket
updated_at: 2026-11-26 18:32:48.395409
---

# User Data Streams

## Connect

- The base API endpoint is: **https://eapi.binance.com**
- A User Data Stream `listenKey` is valid for 60 minutes after creation.
- Doing a `PUT` on a `listenKey` will extend its validity for 60 minutes.
- Doing a `DELETE` on a `listenKey` will close the stream and invalidate the `listenKey`.
- Doing a `POST` on an account with an active `listenKey` will return the currently active
  `listenKey` and extend its validity for 60 minutes.
- Connection method for Websocket:
  - Base Url: **wss://fstream.binance.com/private/**
  - User Data Streams are accessed at **/ws/\<listenKey\>**
  - Example:
    `wss://fstream.binance.com/private/ws/XaEAKTsQSRLZAGH9tuIu37plSRsdjmlAVBoNYPUITlTAko1WI22PgmBMpI1rS8Yh`
- A single connection is only valid for 24 hours; expect to be disconnected at the 24 hour mark

---

## Event: Account Data

### Description

- Update under the following conditions:
  - Account deposit or withdrawal
  - Position info change
  - Periodic update every 10s when having position

### URL Path

`/private`

### Event Name

`ACCOUNT_UPDATE`

### Update Speed

**50ms**

### Payload

> **Schema:**
> [`accountUpdate`](/catalog/core-trading-derivatives-trading-options/api/ws-streams/~schemas#accountupdate)

> **Note:** The event payload is wrapped in a `stream`/`data` envelope on the WebSocket connection.

<SchemaEmbed
  spec="derivatives-trading-options-ws-streams"
  schema="accountUpdate"
/>

---

## Event: Balance and Position Update

### Description

Event type is `BALANCE_POSITION_UPDATE`.

- When balance or position get updated, this event will be pushed.
  - `BALANCE_POSITION_UPDATE` will be pushed only when update happens on user's account, including
    changes on balances, positions.
  - Unfilled orders or cancelled orders will not make the event pushed, since there's no change on
    positions.
  - "position" in `BALANCE_POSITION_UPDATE`: Only symbols of changed positions will be pushed.

- The field "m" represents the reason type for the event and may shows the following possible types:
  - DEPOSIT
  - WITHDRAW
  - ORDER

- The field "bc" represents the balance change except for PnL and commission.

### Event Name

`BALANCE_POSITION_UPDATE`

### Payload

> **Schema:**
> [`balancePositionUpdate`](/catalog/core-trading-derivatives-trading-options/api/ws-streams/~schemas#balancepositionupdate)

<SchemaEmbed
  spec="derivatives-trading-options-ws-streams"
  schema="balancePositionUpdate"
/>

---

## Event: Order Update

### Description

When new order created, order status changed will push such event. Event type is
`ORDER_TRADE_UPDATE`.

**Side**

- BUY
- SELL

**Order Type**

- LIMIT

**Execution Type**

- NEW
- CANCELED
- EXPIRED
- TRADE

**Order Status**

- NEW
- PARTIALLY_FILLED
- FILLED
- CANCELED
- EXPIRED

**Time in force**

- GTC
- IOC
- FOK
- GTX

### URL Path

`/private`

### Event Name

`ORDER_TRADE_UPDATE`

### Update Speed

**50ms**

### Payload

> **Schema:**
> [`orderTradeUpdate`](/catalog/core-trading-derivatives-trading-options/api/ws-streams/~schemas#ordertradeupdate)

<SchemaEmbed
  spec="derivatives-trading-options-ws-streams"
  schema="orderTradeUpdate"
/>

---

## Event: Greek Update

### Description

`GREEK_UPDATE` will be triggered when a position changes or periodically every 10 seconds when
having position.

### URL Path

`/private`

### Event Name

`GREEK_UPDATE`

### Payload

> **Schema:**
> [`greekUpdate`](/catalog/core-trading-derivatives-trading-options/api/ws-streams/~schemas#greekupdate)

<SchemaEmbed
  spec="derivatives-trading-options-ws-streams"
  schema="greekUpdate"
/>

---

## Event: Risk Level Change

### Description

- Updates whenever there is an account risk level change. The following are possibly values:
  - NORMAL
  - REDUCE_ONLY
- Note: Risk level changes are only applicable to VIP and Market Makers user accounts. VIP and
  certain Market Maker accounts will be automatically placed into REDUCE_ONLY mode if their margin
  balance is insufficient to meet their maintenance margin obligations. Once in REDUCE_ONLY mode,
  the system will re-evaluate the risk level only upon the following events:
  - Funds transfer
  - Trade fill
  - Option expiry

### URL Path

`/private`

### Event Name

`RISK_LEVEL_CHANGE`

### Update Speed

**50ms**

### Payload

> **Schema:**
> [`riskLevelChange`](/catalog/core-trading-derivatives-trading-options/api/ws-streams/~schemas#risklevelchange)

<SchemaEmbed
  spec="derivatives-trading-options-ws-streams"
  schema="riskLevelChange"
/>

---

## Event: User Data Stream Expired

### Description

When the `listenKey` used for the user data stream turns expired, this event will be pushed.

**Notice:**

- This event is not related to the websocket disconnection.
- This event will be received only when a valid `listenKey` in connection got expired.
- No more user data event will be updated after this event received until a new valid `listenKey`
  used.

### Event Name

`listenKeyExpired`

### Payload

> **Schema:**
> [`listenKeyExpired`](/catalog/core-trading-derivatives-trading-options/api/ws-streams/~schemas#listenkeyexpired)

<SchemaEmbed
  spec="derivatives-trading-options-ws-streams"
  schema="listenKeyExpired"
/>

---

# 账户信息流

## 连接

- 本篇所列出REST接口的baseurl **https://eapi.binance.com**
- 用于订阅账户数据的 `listenKey` 从创建时刻起有效期为60分钟
- 可以通过`PUT`一个`listenKey`延长60分钟有效期
- 可以通过`DELETE`一个 `listenKey` 立即关闭当前数据流，并使该`listenKey` 无效
- 在具有有效`listenKey`的帐户上执行`POST`将返回当前有效的`listenKey`并将其有效期延长60分钟
- websocket接口的连接方式如下：
  - Base Url: **wss://fstream.binance.com/private/**
  - 订阅账户数据流的stream名称为 **/ws/\<listenKey\>**
  - 连接样例：`wss://fstream.binance.com/private/ws/XaEAKTsQSRLZAGH9tuIu37plSRsdjmlAVBoNYPUITlTAko1WI22PgmBMpI1rS8Yh`
- 每个链接有效期不超过24小时，请妥善处理断线重连。
- 考虑到剧烈行情下, RESTful接口可能存在查询延迟，我们强烈建议您优先从Websocket user data
  stream推送的消息来获取订单，仓位等信息。

---

## Account 数据更新推送

### 事件描述

账户更新事件的event type 固定为 `ACCOUNT_UPDATE`

- 当账户信息有变动时，会推送此事件：
  - 仅当账户信息有变动时(包括资金、仓位发生变化)，才会推送此事件；
  - 有仓位情况下每10s定期更新

### URL Path

`/private`

### 事件类型

`ACCOUNT_UPDATE`

### 更新速度

**50ms**

### Payload

> **Schema:**
> [`accountUpdate`](/catalog/core-trading-derivatives-trading-options/api/ws-streams/~schemas#accountupdate)

> **注意:** 事件推送数据包含在 WebSocket 连接的 `stream`/`data` 信封中。

<SchemaEmbed
  spec="derivatives-trading-options-ws-streams"
  schema="accountUpdate"
/>

---

## Balance 和 Position 更新推送

### 事件描述

账户更新事件的 event type 固定为 `BALANCE_POSITION_UPDATE`

- 当账户信息有变动时，会推送此事件：
  - 仅当账户信息有变动时(包括资金、仓位等发生变化)，才会推送此事件；
  - 订单状态变化没有引起账户和持仓变化的，不会推送此事件；
  - position 信息：仅当 symbol 仓位有变动时推送。

- 字段"m"代表了事件推出的原因，包含了以下可能类型:
  - DEPOSIT
  - WITHDRAW
  - ORDER

- 字段"bc"代表了钱包余额的改变量，即 balance change，但注意其不包含仓位盈亏及交易手续费。

### 事件类型

`BALANCE_POSITION_UPDATE`

### Payload

> **Schema:**
> [`balancePositionUpdate`](/catalog/core-trading-derivatives-trading-options/api/ws-streams/~schemas#balancepositionupdate)

<SchemaEmbed
  spec="derivatives-trading-options-ws-streams"
  schema="balancePositionUpdate"
/>

---

## 订单/交易更新推送

### 事件描述

当有新订单创建、订单有新成交或者新的状态变化时会推送此类事件，事件类型统一为 `ORDER_TRADE_UPDATE`

**订单方向**

- BUY 买入
- SELL 卖出

**订单类型**

- LIMIT 限价单

**本次事件的具体执行类型**

- NEW
- CANCELED 已撤
- EXPIRED 订单失效
- TRADE 交易

**订单状态**

- NEW
- PARTIALLY_FILLED
- FILLED
- CANCELED
- EXPIRED

**有效方式**

- GTC
- IOC
- FOK
- GTX

**强平和ADL:**

- 若用户因保证金不足发生强平：
  - `c`为"autoclose-XXX"，`X`为"NEW"
- 若用户保证金充足但被 ADL:
  - `c`为"adl_autoclose"，`X`为"NEW"

### URL Path

`/private`

### 事件类型

`ORDER_TRADE_UPDATE`

### 更新速度

**50ms**

### Payload

> **Schema:**
> [`orderTradeUpdate`](/catalog/core-trading-derivatives-trading-options/api/ws-streams/~schemas#ordertradeupdate)

<SchemaEmbed
  spec="derivatives-trading-options-ws-streams"
  schema="orderTradeUpdate"
/>

---

## Greek更新推送

### 事件描述

`GREEK_UPDATE`在仓位变动时或有仓位情况下每10s定期更新

### URL Path

`/private`

### 事件类型

`GREEK_UPDATE`

### Payload

> **Schema:**
> [`greekUpdate`](/catalog/core-trading-derivatives-trading-options/api/ws-streams/~schemas#greekupdate)

<SchemaEmbed
  spec="derivatives-trading-options-ws-streams"
  schema="greekUpdate"
/>

---

## 风险等级变更通知

### 事件描述

- 每当账户风险等级发生变化时进行更新。以下是可能的状态：
  - NORMAL
  - REDUCE_ONLY

- 需要注意的是，风险等级变化仅适用于VIP和市场做市商用户帐户。如果VIP和某些市场做市商账户的保证金余额不足以满足其维持保证金义务，系统将自动将其风险等级更改为仅减少模式（REDUCE_ONLY）。一旦风险等级被设置为仅减少模式（REDUCE_ONLY），系统将在以下事件发生时重新评估风险等级：
  - 资金转账
  - 成交填充
  - 期权到期

### URL Path

`/private`

### 事件类型

`RISK_LEVEL_CHANGE`

### 更新速度

**50ms**

### Payload

> **Schema:**
> [`riskLevelChange`](/catalog/core-trading-derivatives-trading-options/api/ws-streams/~schemas#risklevelchange)

<SchemaEmbed
  spec="derivatives-trading-options-ws-streams"
  schema="riskLevelChange"
/>

---

## listenKey过期推送

### 事件描述

当前连接使用的有效listenKey过期时，user data stream 将会推送此事件。

**注意:**

- 此事件与 websocket 连接中断没有必然联系
- 只有正在连接中的有效`listenKey`过期时才会收到此消息
- 收到此消息后 user data stream 将不再更新，直到用户使用新的有效的`listenKey`

### 事件类型

`listenKeyExpired`

### Payload

> **Schema:**
> [`listenKeyExpired`](/catalog/core-trading-derivatives-trading-options/api/ws-streams/~schemas#listenkeyexpired)

<SchemaEmbed
  spec="derivatives-trading-options-ws-streams"
  schema="listenKeyExpired"
/>