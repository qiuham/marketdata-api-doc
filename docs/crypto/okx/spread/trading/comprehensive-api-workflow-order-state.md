---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#spread-trading-comprehensive-api-workflow-order-state
anchor_id: spread-trading-comprehensive-api-workflow-order-state
api_type: API
updated_at: 2026-07-04 19:38:39.516481
---

# Order State

Track the state of an order by subscribing to the `sprd-orders` WebSocket channel.

  1. Upon submitting an order, whether as a Maker or Taker, an order update message is sent via the orders WebSocket channel. The message will indicate the order's `state` == `live`.
  2. Order matching and trade settlement are asynchronous processes. When the order is matched but not settled, system pushes `pendingSettleSz` > 0 and `fillSz` == ""
  3. If the order is partially filled, an order update message is sent with `state` == `partially_filled`.
  4. In the event that the order is completely filled, an order update message is sent with the `state` == `filled`.
  5. If the order is not fully filled but has reached its final state, an order update message is sent with the `state` == `canceled`.
  6. If a certain part of an order is rejected, an order update message is sent with updated `canceledSz` and `pendingFillSz`, and `code` and `msg` corresponding to the error.

---

# 用户的订单状态

通过订阅 `sprd-orders`WebSocket 频道，用户可以跟踪他们的订单状态。

  1. 提交订单后，无论是 _Maker_ 还是 _Taker_ ，用户都会通过订单 WebSocket 频道道收到订单更新消息。该消息将指示订单的`state` == `live`。
  2. 订单成交和结算是异步的。当订单已成交但还没结算，用户将收到`pendingSettleSz`>0，`fillSz` == ""的订单更新消息
  3. 如果订单已部分成交且仍有待处理数量，用户将收到`state` == `partially_filled` 的订单更新消息
  4. 如果订单完全成交，用户将收到`state` == `filled`的订单更新消息
  5. 如果订单未完全消耗，但已达到最终状态，用户将收到`state` == `canceled`的订单更新消息。
  6. 如果订单的某个部分被拒绝，用户会收到更新的订单更新，其中包含更新的 `canceledSz` 和 `pendingFillSz`，以及与错误对应的`code`和`msg`。