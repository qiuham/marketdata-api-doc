---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#spread-trading-comprehensive-api-workflow-trade-lifecycle
anchor_id: spread-trading-comprehensive-api-workflow-trade-lifecycle
api_type: API
updated_at: 2026-07-08 19:28:29.690381
---

# Trade Lifecycle

In order for a trade to take place, two orders must be crossed within a Spread's Order Book.  
  
Obtain information about the state of an Order and determine if it has reached its final state by monitoring the `sprd-orders`WebSocket channel. The `state` key in the channel indicates the current state of the Order. If the state is `live` or `partially_filled`, it means that the Order still has available size (`sz`) that the creator or another user can take action on. On the other hand, if the state is `canceled` or `filled`, the Order no longer has any available actions that the creator or any other user can take action on.

It is important to closely track the values of the following attributes: `sz`(size),`pendingFillSz` (pending fill size), `canceledSz` (canceled size), and `accFillSz`(accumulated fill size). These attributes provide crucial information regarding the status and progression of the Order.

---

# 交易生命周期

为了进行交易，需要在价差撮合交易中匹配两个订单。 通过订阅 `sprd-orders`WebSocket 通道，您可以获得有关订单状态的信息并确定它是否已达到最终状态。通道中的`state`值表示订单的当前状态。  
  
  1. 如果状态为`live` 或 `partially_filled`，则意味着订单仍有未达最终状态（`filled`或`canceled`）数量，创建者或其他用户仍可能可以对其执行操作。
  2. 另一方面，如果状态为`canceled`或`filled`，创建者或任何其他用户将无法对此订单执行任何操作。

请密切跟踪以下属性：`sz`（数量）、`pendingFillSz`（待完成数量）、`canceledSz`（被取消数量）和 `accFillSz`（累积完成数量）。这些属性提供了有关订单状态和进展的重要信息。