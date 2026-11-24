---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/derivatives-trading-coin-futures/user-data-streams
api_type: WebSocket
updated_at: 2026-11-24 18:32:17.083023
---

# User Data Streams

## Connect

- The base API endpoint is: **https://dapi.binance.com**
- A User Data Stream `listenKey` is valid for 60 minutes after creation.
- Doing a `PUT` on a `listenKey` will extend its validity for 60 minutes, if response `-1125` error
  "This listenKey does not exist." Please use `POST /dapi/v1/listenKey` to recreate `listenKey`.
- Doing a `DELETE` on a `listenKey` will close the stream and invalidate the `listenKey`.
- Doing a `POST` on an account with an active `listenKey` will return the currently active
  `listenKey` and extend its validity for 60 minutes.
- The connection method for Websocket:
  - Base Url: **wss://dstream.binance.com**
  - User Data Streams are accessed at **/ws/\<listenKey\>**
  - Example:
    `wss://dstream.binance.com/ws/XaEAKTsQSRLZAGH9tuIu37plSRsdjmlAVBoNYPUITlTAko1WI22PgmBMpI1rS8Yh`

- **Message Ordering Guarantee**:
  - For the same user on a single Websocket connection, messages of the **same event type** (e.g.,
    `ACCOUNT_UPDATE`, `ORDER_TRADE_UPDATE`) are **strictly ordered** by both `T` (transaction time
    from Matching Engine) and `E` (event time when the message is generated).
  - **Recommended**: Use the `E` field for ordering updates, especially when:
    - Comparing events across different event types (e.g., `ORDER_TRADE_UPDATE` vs market data
      streams like `aggTrade`).
    - Events from different services may share the same `T` but have different `E` values due to
      processing timing.
    - For the same event type on the same connection, both `T` and `E` remain strictly ordered, so
      either field can be used reliably.
- A single connection is only valid for 24 hours; expect to be disconnected at the 24 hour mark
- Considering that RESTful endpoints may experience query delays under volatile market conditions,
  we strongly recommend prioritizing Websocket user data stream messages for retrieving orders,
  positions, and other information.

---

## Event: Margin Call

### Description

- When the user's position risk ratio is too high, this stream will be pushed.
- This message is only used as risk guidance information and is not recommended for investment
  strategies.
- In the case of a highly volatile market, there may be the possibility that the user's position has
  been liquidated at the same time when this stream is pushed out.

### Event Name

`MARGIN_CALL`

### Payload

> **Schema:**
> [`marginCall`](/catalog/core-trading-derivatives-trading-coin-m-futures/api/ws-streams/~schemas#margincall)

<SchemaEmbed
  spec="derivatives-trading-coin-futures-ws-streams"
  schema="marginCall"
/>

---

## Event: Balance and Position Update

### Description

Event type is `ACCOUNT_UPDATE`.

- When balance or position get updated, this event will be pushed.
  - `ACCOUNT_UPDATE` will be pushed only when update happens on user's account, including changes on
    balances, positions, or margin type.
  - Unfilled orders or cancelled orders will not make the event `ACCOUNT_UPDATE` pushed, since
    there's no change on positions.
  - "position" in `ACCOUNT_UPDATE`: All symbols will be pushed.

- The field "m" represents the reason type for the event and may shows the following possible types:
  - DEPOSIT
  - WITHDRAW
  - ORDER
  - FUNDING_FEE
  - ADJUSTMENT
  - INSURANCE_CLEAR
  - ADMIN_DEPOSIT
  - ADMIN_WITHDRAW
  - MARGIN_TRANSFER
  - MARGIN_TYPE_CHANGE
  - ASSET_TRANSFER
  - COIN_SWAP_DEPOSIT
  - COIN_SWAP_WITHDRAW

- The field "bc" represents the balance change except for PnL and commission.

### Event Name

`ACCOUNT_UPDATE`

### Payload

> **Schema:**
> [`accountUpdate`](/catalog/core-trading-derivatives-trading-coin-m-futures/api/ws-streams/~schemas#accountupdate)

<SchemaEmbed
  spec="derivatives-trading-coin-futures-ws-streams"
  schema="accountUpdate"
/>

---

## Event: Order Update

### Description

When new order created, modified, order status changed will push such event. Event type is
`ORDER_TRADE_UPDATE`.

**Side**

- BUY
- SELL

**Position Side**

- BOTH
- LONG
- SHORT

**Order Type**

- MARKET
- LIMIT
- STOP
- TAKE_PROFIT
- LIQUIDATION

**Execution Type**

- NEW
- CANCELED
- CALCULATED - Liquidation Execution
- EXPIRED
- TRADE
- AMENDMENT - Order Modified

**Order Status**

- NEW
- PARTIALLY_FILLED
- FILLED
- CANCELED
- EXPIRED
- EXPIRED_IN_MATCH

**Time in force**

- GTC
- IOC
- FOK
- GTX

**Liquidation and ADL:**

- If user gets liquidated due to insufficient margin balance:
  - `c` shows as "autoclose-XXX", `X` shows as "NEW"
- If user has enough margin balance but gets ADL:
  - `c` shows as "adl_autoclose", `X` shows as "NEW"

**Expiry Reason**

- `0`: None, the default value
- `1`: Order has expired to prevent users from inadvertently trading against themselves
- `2`: IOC order could not be filled completely, remaining quantity is canceled
- `3`: IOC order could not be filled completely to prevent users from inadvertently trading against
  themselves, remaining quantity is canceled
- `4`: Order has been canceled, as it's knocked out by another higher priority RO (market) order or
  reversed positions would be opened
- `5`: Order has expired when the account was liquidated
- `6`: Order has expired as GTE condition unsatisfied
- `7`: Order has been canceled as the symbol is delisted
- `8`: The initial order has expired after the stop order is triggered
- `9`: Market order could not be filled completely, remaining quantity is canceled
- `10`: FOK order could not be filled completely, the order is canceled
- `11`: Order has been canceled, as it's failed Post-only check.

### Event Name

`ORDER_TRADE_UPDATE`

### Payload

> **Schema:**
> [`orderTradeUpdate`](/catalog/core-trading-derivatives-trading-coin-m-futures/api/ws-streams/~schemas#ordertradeupdate)

<SchemaEmbed
  spec="derivatives-trading-coin-futures-ws-streams"
  schema="orderTradeUpdate"
/>

---

## Event: Account Configuration Update (Leverage Update)

### Description

When the account configuration is changed, the event type will be pushed as `ACCOUNT_CONFIG_UPDATE`.

When the leverage of a trade pair changes, the payload will contain the object `ac` to represent the
account configuration of the trade pair, where `s` represents the specific trade pair and `l`
represents the leverage.

### Event Name

`ACCOUNT_CONFIG_UPDATE`

### Payload

> **Schema:**
> [`accountConfigUpdate`](/catalog/core-trading-derivatives-trading-coin-m-futures/api/ws-streams/~schemas#accountconfigupdate)

<SchemaEmbed
  spec="derivatives-trading-coin-futures-ws-streams"
  schema="accountConfigUpdate"
/>

---

## Event: Strategy Update

### Description

`STRATEGY_UPDATE` update when a strategy is created/cancelled/expired, ...etc.

**Strategy Status**

- NEW
- WORKING
- CANCELLED
- EXPIRED

**opCode**

- 8001: The strategy params have been updated
- 8002: User cancelled the strategy
- 8003: User manually placed or cancelled an order
- 8004: The stop limit of this order reached
- 8005: User position liquidated
- 8006: Max open order limit reached
- 8007: New grid order
- 8008: Margin not enough
- 8009: Price out of bounds
- 8010: Market is closed or paused
- 8011: Close position failed, unable to fill
- 8012: Exceeded the maximum allowable notional value at current leverage
- 8013: Grid expired due to incomplete KYC verification or access from a restricted jurisdiction
- 8014: User can only place reduce only order
- 8015: User position empty or liquidated

### Event Name

`STRATEGY_UPDATE`

### Payload

> **Schema:**
> [`strategyUpdate`](/catalog/core-trading-derivatives-trading-coin-m-futures/api/ws-streams/~schemas#strategyupdate)

<SchemaEmbed
  spec="derivatives-trading-coin-futures-ws-streams"
  schema="strategyUpdate"
/>

---

## Event: Grid Update (Deprecated)

### Description

`GRID_UPDATE` update when a sub order of a grid is filled or partially filled.

**Strategy Status**

- NEW
- WORKING
- CANCELLED
- EXPIRED

### Event Name

`GRID_UPDATE`

### Payload

> **Schema:**
> [`gridUpdate`](/catalog/core-trading-derivatives-trading-coin-m-futures/api/ws-streams/~schemas#gridupdate)

<SchemaEmbed
  spec="derivatives-trading-coin-futures-ws-streams"
  schema="gridUpdate"
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
> [`listenKeyExpired`](/catalog/core-trading-derivatives-trading-coin-m-futures/api/ws-streams/~schemas#listenkeyexpired)

<SchemaEmbed
  spec="derivatives-trading-coin-futures-ws-streams"
  schema="listenKeyExpired"
/>

---

# 账户信息流

## 连接

- 本篇所列出REST接口的baseurl **https://dapi.binance.com**
- 用于订阅账户数据的 `listenKey` 从创建时刻起有效期为60分钟
- 可以通过`PUT`一个`listenKey`延长60分钟有效期，如收到`-1125`报错提示此`listenKey`不存在，建议重新使用`POST /dapi/v1/listenKey`生成`listenKey`
- 可以通过`DELETE`一个 `listenKey` 立即关闭当前数据流，并使该`listenKey` 无效
- 在具有有效`listenKey`的帐户上执行`POST`将返回当前有效的`listenKey`并将其有效期延长60分钟
- 本篇所列出的websocket接口，连接方式如下：
  - Base Url: **wss://dstream.binance.com**
  - 订阅账户数据流的stream名称为 **/ws/\<listenKey\>**
  - 连接样例：`wss://dstream.binance.com/ws/XaEAKTsQSRLZAGH9tuIu37plSRsdjmlAVBoNYPUITlTAko1WI22PgmBMpI1rS8Yh`
- 每个链接有效期不超过24小时，请妥善处理断线重连。
- **消息顺序保证**:
  - 对于同一用户的单一 Websocket 连接，**相同事件类型**的消息(例如
    `ACCOUNT_UPDATE`、`ORDER_TRADE_UPDATE`)在 `T`(来自撮合引擎的成交时间)和
    `E`(消息生成时的事件时间)两个字段上都**严格有序**。
  - **建议**:使用 `E` 字段进行更新排序，特别是在以下情况下:
    - 比较不同事件类型的事件时(例如 `ORDER_TRADE_UPDATE` 与市场数据流如 `aggTrade`)。
    - 来自不同服务的事件可能具有相同的 `T` 但由于处理时间的差异而具有不同的 `E` 值。
    - 对于同一连接上的相同事件类型，`T` 和 `E` 都保持严格有序，因此可以可靠地使用任一字段。
- 考虑到剧烈行情下, RESTful接口可能存在查询延迟，我们强烈建议您优先从Websocket user data
  stream推送的消息来获取订单，仓位等信息。

---

## 追加保证金通知

### 事件描述

- 当用户持仓风险过高，会推送此消息。
- 此消息仅作为风险指导信息，不建议用于投资策略。
- 在大波动市场行情下，不排除此消息发出的同时用户仓位已被强平的可能。

### 事件类型

`MARGIN_CALL`

### Payload

> **Schema:**
> [`marginCall`](/catalog/core-trading-derivatives-trading-coin-m-futures/api/ws-streams/~schemas#margincall)

<SchemaEmbed
  spec="derivatives-trading-coin-futures-ws-streams"
  schema="marginCall"
/>

---

## Balance和Position更新推送

### 事件描述

账户更新事件的 event type 固定为 `ACCOUNT_UPDATE`

- 仅当账户信息有变动时，才会推送此事件。
- 订单状态变化没有引起账户和持仓变化的，不会推送此事件。
- position 信息：所有symbol推送。

- 字段"m"代表了事件推出的原因，包含了以下可能类型:
  - DEPOSIT
  - WITHDRAW
  - ORDER
  - FUNDING_FEE
  - ADJUSTMENT
  - INSURANCE_CLEAR
  - ADMIN_DEPOSIT
  - ADMIN_WITHDRAW
  - MARGIN_TRANSFER
  - MARGIN_TYPE_CHANGE
  - ASSET_TRANSFER
  - COIN_SWAP_DEPOSIT
  - COIN_SWAP_WITHDRAW

- 字段"bc"代表了钱包余额的改变量，即 balance change，但注意其不包含仓位盈亏及交易手续费。

### 事件类型

`ACCOUNT_UPDATE`

### Payload

> **Schema:**
> [`accountUpdate`](/catalog/core-trading-derivatives-trading-coin-m-futures/api/ws-streams/~schemas#accountupdate)

<SchemaEmbed
  spec="derivatives-trading-coin-futures-ws-streams"
  schema="accountUpdate"
/>

---

## 订单/交易更新推送

### 事件描述

当有新订单创建、修改、订单有新成交或者新的状态变化时会推送此类事件

**订单方向**

- BUY 买入
- SELL 卖出

**持仓方向**

- BOTH 单一持仓方向
- LONG 多头(双向持仓下)
- SHORT 空头(双向持仓下)

**订单类型**

- MARKET 市价单
- LIMIT 限价单
- STOP 止损单
- TAKE_PROFIT 止盈单

**本次事件的具体执行类型**

- NEW
- CANCELED 已撤
- CALCULATED 强平单
- EXPIRED 订单失效
- TRADE 交易
- AMENDMENT 订单修改

**订单状态**

- NEW
- PARTIALLY_FILLED
- FILLED
- CANCELED
- EXPIRED
- EXPIRED_IN_MATCH

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

**过期原因**

- `0`: 无，默认值
- `1`: 自成交保护，订单被取消
- `2`: IOC订单无法完全成交，订单被取消
- `3`: IOC订单因自成交保护无法完全成交，订单被取消
- `4`: 只减仓竞争过程中，低优先级的只减仓订单被取消
- `5`: 账户强平过程中，订单被取消
- `6`: 不满足GTE条件，订单被取消
- `7`: Symbol下架，订单被取消
- `8`: 止盈止损单触发后，初始订单被取消
- `9`: 市价订单无法完全成交，订单被取消
- `10`: FOK订单无法完全成交，订单被取消
- `11`: 只做Maker订单会以Taker成交，订单被取消

### 事件类型

`ORDER_TRADE_UPDATE`

### Payload

> **Schema:**
> [`orderTradeUpdate`](/catalog/core-trading-derivatives-trading-coin-m-futures/api/ws-streams/~schemas#ordertradeupdate)

<SchemaEmbed
  spec="derivatives-trading-coin-futures-ws-streams"
  schema="orderTradeUpdate"
/>

---

## 杠杆倍数等账户配置更新推送

### 事件描述

当账户配置发生变化时会推送此类事件，类型统一为`ACCOUNT_CONFIG_UPDATE`。

当交易对杠杆倍数发生变化时，推送消息体会包含对象`ac`表示交易对账户配置，其中`s`代表具体的交易对，`l`代表杠杆倍数。

### 事件类型

`ACCOUNT_CONFIG_UPDATE`

### Payload

> **Schema:**
> [`accountConfigUpdate`](/catalog/core-trading-derivatives-trading-coin-m-futures/api/ws-streams/~schemas#accountconfigupdate)

<SchemaEmbed
  spec="derivatives-trading-coin-futures-ws-streams"
  schema="accountConfigUpdate"
/>

---

## 策略交易更新推送

### 事件描述

`STRATEGY_UPDATE` 在策略交易创建、取消、失效等等时候更新。

**策略状态**

- NEW
- WORKING
- CANCELLED
- EXPIRED

**opCode**

- 8001: 策略参数更改
- 8002: 用户取消策略
- 8003: 用户手动新增或取消订单
- 8004: 达到 stop limit
- 8005: 用户仓位爆仓
- 8006: 已达最大可挂单数量
- 8007: 新增网格策略
- 8008: 保证金不足
- 8009: 价格超出范围
- 8010: 市场非交易状态
- 8011: 关仓失败，平仓单无法成交
- 8012: 超过最大可交易名目金额
- 8013: 不符合网格交易身份
- 8014: 仅接受平仓单
- 8015: 无仓位或是仓位已经爆仓

### 事件类型

`STRATEGY_UPDATE`

### Payload

> **Schema:**
> [`strategyUpdate`](/catalog/core-trading-derivatives-trading-coin-m-futures/api/ws-streams/~schemas#strategyupdate)

<SchemaEmbed
  spec="derivatives-trading-coin-futures-ws-streams"
  schema="strategyUpdate"
/>

---

## 网格更新推送 (Deprecated)

### 事件描述

`GRID_UPDATE` 在网格子订单有部份或是完全成交时更新。

**策略状态**

- NEW
- WORKING
- CANCELLED
- EXPIRED

### 事件类型

`GRID_UPDATE`

### Payload

> **Schema:**
> [`gridUpdate`](/catalog/core-trading-derivatives-trading-coin-m-futures/api/ws-streams/~schemas#gridupdate)

<SchemaEmbed
  spec="derivatives-trading-coin-futures-ws-streams"
  schema="gridUpdate"
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
> [`listenKeyExpired`](/catalog/core-trading-derivatives-trading-coin-m-futures/api/ws-streams/~schemas#listenkeyexpired)

<SchemaEmbed
  spec="derivatives-trading-coin-futures-ws-streams"
  schema="listenKeyExpired"
/>