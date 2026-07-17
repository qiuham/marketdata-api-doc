---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#spread-trading-comprehensive-api-workflow
anchor_id: spread-trading-comprehensive-api-workflow
api_type: API
updated_at: 2026-07-17 19:17:11.734611
---

# Comprehensive API Workflow

Notifications regarding Orders and Trades will be received by both the Taker and the Maker through the WebSocket Notification channels. 

A user assumes the role of a _Maker_ when their Order is executed upon by another Order. A user becomes a _Taker_ when they submit an Order that crosses an existing Order in the Order Book.

### Obtaining Available Spreads

To retrieve all available Spreads for trading on OKX, make a request to the `GET /api/v5/sprd/spreads` endpoint.

### Retrieving Your Orders

To retrieve orders on OKX, make a request to the `GET /api/v5/sprd/order` endpoint.

### Retrieving Your Trades

To retrieve trades on OKX, make a request to the `GET /api/v5/sprd/trades` endpoint.

### Submitting an Order

To submit an order to a Spread's Order Book, make a request to the `POST /api/v5/sprd/order` endpoint.

### Spread States

There are three different states during a Spread's life cycle: `live`, `suspend`, and `expired` as detailed below:

  1. `live`: Spreads that are actively traded on Nitro Spreads
  2. `suspend`: Spreads in which at least one of the legs is suspended and the other one is active or suspended on the OKX orderbook exchange; or spreads in which the underlying instruments are still live on the OKX orderbook exchange, but removed from Nitro Spreads
  3. `expired`: Spreads in which at least one of the underlying instruments is expired on the OKX orderbook exchange

Please refer to the following table for all possible scenarios given the state of the underlying instruments and the resulting state of the spread on Nitro Spreads (except for the case that the spread is delisted on Nitro Spreads):

Instrument A | Instrument B | Spread State  
---|---|---  
Live | Live | Live  
Suspend | Live | Suspend  
Live | Suspend | Suspend  
Suspend | Suspend | Suspend  
Expired | Live | Expired  
Live | Expired | Expired  
Suspend | Expired | Expired  
Expired | Suspend | Expired  
Expired | Expired | Expired  
  
### Trade Lifecycle

In order for a trade to take place, two orders must be crossed within a Spread's Order Book.

Obtain information about the state of an Order and determine if it has reached its final state by monitoring the `sprd-orders`WebSocket channel. The `state` key in the channel indicates the current state of the Order. If the state is `live` or `partially_filled`, it means that the Order still has available size (`sz`) that the creator or another user can take action on. On the other hand, if the state is `canceled` or `filled`, the Order no longer has any available actions that the creator or any other user can take action on.

It is important to closely track the values of the following attributes: `sz`(size),`pendingFillSz` (pending fill size), `canceledSz` (canceled size), and `accFillSz`(accumulated fill size). These attributes provide crucial information regarding the status and progression of the Order.

### Order State

Track the state of an order by subscribing to the `sprd-orders` WebSocket channel.

  1. Upon submitting an order, whether as a Maker or Taker, an order update message is sent via the orders WebSocket channel. The message will indicate the order's `state` == `live`.
  2. Order matching and trade settlement are asynchronous processes. When the order is matched but not settled, system pushes `pendingSettleSz` > 0 and `fillSz` == ""
  3. If the order is partially filled, an order update message is sent with `state` == `partially_filled`.
  4. In the event that the order is completely filled, an order update message is sent with the `state` == `filled`.
  5. If the order is not fully filled but has reached its final state, an order update message is sent with the `state` == `canceled`.
  6. If a certain part of an order is rejected, an order update message is sent with updated `canceledSz` and `pendingFillSz`, and `code` and `msg` corresponding to the error.

### Trade State

Track the state of a trade by subscribing to the `sprd-trades`WebSocket channel.

  1. After an executed trade undergoes clearing and settlement on OKX, it reaches finality.
  2. For successfully cleared trades, a WebSocket message is sent with the `state`denoted as `filled`.
  3. In the case of an unsuccessful trade clearing, a trade update message is sent with the `state` reflected as `rejected`.
  4. If the trade state is `rejected`, the trade update message will also include the error `code` and a corresponding error message (`msg`) that explains the reason for the rejection.

### All Trades

All users have the ability to receive updates on all trades that take place through the OKX Nitro Spreads product.

It's important to note that OKX Nitro Spreads does not disclose information about the counterparties involved in the trades or the individual `side` (`buy` or `sell`) of the composite legs that were traded.

  1. By subscribing to the `sprd-public-trades`WebSocket channel, WebSocket messages are sent exclusively for trades that have been successfully cleared and settled.

---

# 全面的 API 工作流程

有关订单和交易的通知将由 *Taker* 和 *Maker* 通过 WebSocket 通知渠道接收。 

当用户的订单被另一个订单执行时，用户将承担 _Maker_ 的角色。当用户提交的订单与订单簿中的现有订单相匹配时，他们就会成为 _Taker_

### 获取可用Spreads 

要检索在 OKX 上交易的所有可用Spreads，您应该向 `GET /api/v5/sprd/spreads` 发出请求

### 检索您的订单

要在 OKX 上检索您的订单，您应该向 `GET /api/v5/sprd/order` 发出请求。

### 检索您的交易

要检索您在 OKX 上的交易，您应该向 `GET /api/v5/sprd/trades` 发出请求。

### 提交订单 

要向 某个Spread 的订单簿提交订单，您应该请求 `POST /api/v5/sprd/order` 。

### Spread状态 

Spread 的生命周期中存在三种不同的状态：`live`，`suspend`，和 `expired`:

  1. `live`: 在 Nitro Spread 上活跃交易的Spreads
  2. `suspend`：其中至少一条腿被暂停，另一条在 OKX 订单簿交易所处于活跃或暂停状态的价差；或标的工具仍在 OKX 订单簿交易所中存在但已从 Nitro Spread 中移除的Spread
  3. `expired`：至少一条腿在 OKX 订单簿交易所到期的Spread

给定每条腿的状态以及 Nitro Spreads 上的Spread状态（除了在 Nitro Spread上退市的情况），所有可能Spread状态的情况请参考下表：

交易产品A | 交易产品B | Spread状态  
---|---|---  
Live | Live | Live  
Suspend | Live | Suspend  
Live | Suspend | Suspend  
Suspend | Suspend | Suspend  
Expired | Live | Expired  
Live | Expired | Expired  
Suspend | Expired | Expired  
Expired | Suspend | Expired  
Expired | Expired | Expired  
  
### 交易生命周期 

为了进行交易，需要在价差撮合交易中匹配两个订单。 通过订阅 `sprd-orders`WebSocket 通道，您可以获得有关订单状态的信息并确定它是否已达到最终状态。通道中的`state`值表示订单的当前状态。

  1. 如果状态为`live` 或 `partially_filled`，则意味着订单仍有未达最终状态（`filled`或`canceled`）数量，创建者或其他用户仍可能可以对其执行操作。
  2. 另一方面，如果状态为`canceled`或`filled`，创建者或任何其他用户将无法对此订单执行任何操作。

请密切跟踪以下属性：`sz`（数量）、`pendingFillSz`（待完成数量）、`canceledSz`（被取消数量）和 `accFillSz`（累积完成数量）。这些属性提供了有关订单状态和进展的重要信息。

### 用户的订单状态 

通过订阅 `sprd-orders`WebSocket 频道，用户可以跟踪他们的订单状态。

  1. 提交订单后，无论是 _Maker_ 还是 _Taker_ ，用户都会通过订单 WebSocket 频道道收到订单更新消息。该消息将指示订单的`state` == `live`。
  2. 订单成交和结算是异步的。当订单已成交但还没结算，用户将收到`pendingSettleSz`>0，`fillSz` == ""的订单更新消息
  3. 如果订单已部分成交且仍有待处理数量，用户将收到`state` == `partially_filled` 的订单更新消息
  4. 如果订单完全成交，用户将收到`state` == `filled`的订单更新消息
  5. 如果订单未完全消耗，但已达到最终状态，用户将收到`state` == `canceled`的订单更新消息。
  6. 如果订单的某个部分被拒绝，用户会收到更新的订单更新，其中包含更新的 `canceledSz` 和 `pendingFillSz`，以及与错误对应的`code`和`msg`。

### 用户的交易状态 

通过订阅 `sprd-trades`WebSocket 频道，用户可以跟踪他们的交易状态。 1\. 一笔已执行的交易在OKX上进行清算结算后，即为最终交易。 2\. 对于成功清算的交易，用户会收到一条 WebSocket 消息，其中的`state`表示`filled`。 3\. 在交易清算不成功的情况下，用户会收到一条交易更新消息，`state`反映为`rejected`。 4\. 如果交易`state`为`rejected`，交易更新消息还将包含错误代码`code`和解释拒绝原因的相应错误消息 `msg`。

### 所有交易 

所有用户都能够接收通过 OKX Nitro Spread 产品发生的所有交易的更新。 请务必注意，OKX Nitro Spreads 不会披露有关交易双方及交易方向（买入或卖出）的信息。

  1. 用户可以订阅`sprd-public-trades`频道来获取所有已成功结算的交易。