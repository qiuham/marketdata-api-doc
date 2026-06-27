---
exchange: binance
source_url: https://developers.binance.com/docs/binance-spot-api-docs/faqs/opo
api_type: REST
updated_at: 2026-05-27 18:53:56.170744
---

# Order Amend Keep Priority

**Disclaimer** :

  * The symbols and values used here are fictional and do not imply anything about the actual setup on the live exchange.
  * For simplicity, the examples in this document do not include commission.



## What is Order Amend Keep Priority?[​](/docs/binance-spot-api-docs/faqs/order_amend_keep_priority#what-is-order-amend-keep-priority "Direct link to What is Order Amend Keep Priority?")

Order Amend Keep Priority request is used to modify (amend) an existing order **without losing order book priority**.

The following order modifications are allowed:

  * reduce the quantity of the order



## How can I amend the quantity of my order?[​](/docs/binance-spot-api-docs/faqs/order_amend_keep_priority#how-can-i-amend-the-quantity-of-my-order "Direct link to How can I amend the quantity of my order?")

Use the following requests:

API| Request  
---|---  
REST API| `PUT /api/v3/order/amend/keepPriority`  
WebSocket API| `order.amend.keepPriority`  
FIX API| OrderAmendKeepPriorityRequest `<XAK>`  
  
## What is the difference between "Cancel an Existing Order and Send a New Order" (cancel-replace) and "Order Amend Keep Priority"?[​](/docs/binance-spot-api-docs/faqs/order_amend_keep_priority#what-is-the-difference-between-cancel-an-existing-order-and-send-a-new-order-cancel-replace-and-order-amend-keep-priority "Direct link to What is the difference between "Cancel an Existing Order and Send a New Order" \(cancel-replace\) and "Order Amend Keep Priority"?")

**Cancel an Existing Order and Send a New Order** request cancels the old order and places a new order.  
Time priority is lost. The new order executes after existing orders at the same price.

**Order Amend Keep Priority** request modifies an existing order in-place.   
The amended order keeps its time priority among existing orders at the same price.

For example, consider the following order book:

User| Order ID| Side| Order price| quantity  
---|---|---|---|---  
User A| 10| BUY| 87,000| 1.00  
⭐️ YOU| 15| BUY| 87,000| 5.50  
User B| 20| BUY| 87,000| 4.00  
User C| 21| BUY| 86,999| 2.00  
  
Your order 15 is the second one in the queue based on price and time.

You want to reduce the quantity from 5.50 down to 5.00.

If you use **cancel-replace** to cancel `orderId=15` and place a new order with `qty=5.00`, the order book will look like this:

User| Order ID| Side| Order price| quantity  
---|---|---|---|---  
User A| 10| BUY| 87,000| 1.00  
~~⭐️ YOU~~| ~~11~~| ~~BUY~~| ~~87,000~~| ~~5.50~~  
User B| 20| BUY| 87,000| 4.00  
⭐️ YOU| (new) 22| BUY| 87,000| 5.00  
User C| 21| BUY| 86,999| 2.00  
  
Note that the new order gets a new order ID and you lose time priority: order 22 will trade after the order 20.

If instead you use **Order Amend Keep Priority** to reduce the quantity of `orderId=15` down to `qty=5.00`, the order book will look like this:

User| Order ID| Side| Order price| quantity  
---|---|---|---|---  
User A| 10| BUY| 87,000| 1.00  
⭐️ YOU| 15| BUY| 87,000| (amended) **5.00**  
User B| 20| BUY| 87,000| 4.00  
User C| 21| BUY| 86,999| 2.00  
  
Note that the order ID stays the same and the order keeps its priority in the queue. Only the quantity of the order changes.

## Does Order Amend Keep Priority affect unfilled order count (rate limits)?[​](/docs/binance-spot-api-docs/faqs/order_amend_keep_priority#does-order-amend-keep-priority-affect-unfilled-order-count-rate-limits "Direct link to Does Order Amend Keep Priority affect unfilled order count \(rate limits\)?")

Currently, Order Amend Keep Priority requests charge 0 for unfilled order count.

## How do I know if my order has been amended?[​](/docs/binance-spot-api-docs/faqs/order_amend_keep_priority#how-do-i-know-if-my-order-has-been-amended "Direct link to How do I know if my order has been amended?")

If the order was amended successfully, the API response contains your order with the updated quantity.

On User Data Stream, you will receive an `"executionReport"` event with execution type `"x": "REPLACED"`.

If the amended order belongs to an order list and the client order ID has changed, you will also receive a "listStatus" event with list status type `"l": "UPDATED"`.

You can also use the following requests to query order modification history:

API| Request  
---|---  
REST API| `GET /api/v3/order/amendments`  
WebSocket API| `order.amendments`  
  
## What happens if my amend request does not succeed?[​](/docs/binance-spot-api-docs/faqs/order_amend_keep_priority#what-happens-if-my-amend-request-does-not-succeed "Direct link to What happens if my amend request does not succeed?")

If the request fails for any reason (e.g. fails the filters, permissions, account restrictions, etc), then the order amend request is rejected and the order remains unchanged.

## Is it possible to reuse the current clientOrderId for my amended order?[​](/docs/binance-spot-api-docs/faqs/order_amend_keep_priority#is-it-possible-to-reuse-the-current-clientorderid-for-my-amended-order "Direct link to Is it possible to reuse the current clientOrderId for my amended order?")

Yes.

By default, amended orders get a random new client order ID, but you can pass the current client order ID in the `newClientOrderId` parameter if you wish to keep it.

## Can Iceberg Orders be amended?[​](/docs/binance-spot-api-docs/faqs/order_amend_keep_priority#can-iceberg-orders-be-amended "Direct link to Can Iceberg Orders be amended?")

Yes.

Note that an iceberg order's visible quantity will only change if `newQty` is below the pre-amended visible quantity.

## Can Order lists be amended?[​](/docs/binance-spot-api-docs/faqs/order_amend_keep_priority#can-order-lists-be-amended "Direct link to Can Order lists be amended?")

Orders in an order list can be amended.

Note that OCO order pairs must have the same quantity, since only one of the orders can ever be executed. This means that amending either order affects both orders.

For OTO orders, the working and pending orders can be amended individually.

## Which symbols allow Order Amend Keep Priority?[​](/docs/binance-spot-api-docs/faqs/order_amend_keep_priority#which-symbols-allow-order-amend-keep-priority "Direct link to Which symbols allow Order Amend Keep Priority?")

This information is available in Exchange Information. Symbols that allow Order Amend Keep Priority requests have `amendAllowed` set to `true`.

---

# 保留优先级的修改订单请求（Order Amend Keep Priority） 常见问题

**免责声明:**

  * 此处使用的交易对和价格是虚构的，并不反映实际交易所的设置。
  * 为了简化过程，本文档中的示例不包括佣金。



## 什么是 Order Amend Keep Priority？[​](/docs/zh-CN/binance-spot-api-docs/faqs/order_amend_keep_priority#什么是--order-amend-keep-priority "什么是  Order Amend Keep Priority？的直接链接")

保留优先级的修改订单请求（Order Amend Keep Priority）用于修改（修正）现有订单并 **不失去在订单簿上的优先级** 。

允许进行以下订单修改：

  * 减少现有订单的原始数量。



## 我该如何修改我的订单数量？[​](/docs/zh-CN/binance-spot-api-docs/faqs/order_amend_keep_priority#我该如何修改我的订单数量 "我该如何修改我的订单数量？的直接链接")

使用以下请求：

API| 请求  
---|---  
REST API| `PUT /api/v3/order/amend/keepPriority`  
WebSocket API| `order.amend.keepPriority`  
FIX API| OrderAmendKeepPriorityRequest `<XAK>`  
  
## “撤消挂单再下单”（cancel-replace）和”保留优先级的修改订单请求“之间的区别？[​](/docs/zh-CN/binance-spot-api-docs/faqs/order_amend_keep_priority#撤消挂单再下单cancel-replace和保留优先级的修改订单请求之间的区别 "“撤消挂单再下单”（cancel-replace）和”保留优先级的修改订单请求“之间的区别？的直接链接")

**撤消挂单再下单请求** 撤消挂单并重新下单。  
在时间上的优先级会被丢失。 新订单在相同价格的现有订单之后执行。

**留优先级的修改订单请求** 就地修改现有订单。   
修改后的订单在相同价格的现有订单中保持其时间优先级。

比如，拿下面的订单簿为例：

用户| 订单 ID| 订单方向| 订单价格| 数量  
---|---|---|---|---  
用户 A| 10| BUY| 87,000| 1.00  
⭐️ 你| 15| BUY| 87,000| 5.50  
用户 B| 20| BUY| 87,000| 4.00  
用户 C| 21| BUY| 86,999| 2.00  
  
您的订单 15 是根据价格和时间排在队列中的第二个订单。

您想将数量从 5.50 减少.50 降至 5.00。

如果您使用 **cancel-replace** 取消 `orderId=15` 并使用 `qty=5.00` 来下新订单， 订单簿将如下所示：

用户| 订单 ID| 订单方向| 订单价格| 数量  
---|---|---|---|---  
用户 A| 10| BUY| 87,000| 1.00  
~~⭐️ 你~~| ~~11~~| ~~BUY~~| ~~87,000~~| ~~5.50~~  
用户 B| 20| BUY| 87,000| 4.00  
⭐️ 你| (new) 22| BUY| 87,000| 5.00  
用户 C| 21| BUY| 86,999| 2.00  
  
请注意：新订单将获得新的订单 ID，并且您会失去时间优先级：订单 22 将在订单 20 之后交易。

如果您改用 **保留优先级的修改订单请求** 将 `orderId=15` 的数量减少到 `qty=5.00`，订单簿将如下所示：

用户| 订单 ID| 订单方向| 订单价格| 数量  
---|---|---|---|---  
用户 A| 10| BUY| 87,000| 1.00  
⭐️ 你| 15| BUY| 87,000| (amended) **5.00**  
用户 B| 20| BUY| 87,000| 4.00  
用户 C| 21| BUY| 86,999| 2.00  
  
请注意：订单 ID 保持不变，订单在队列中保持其优先级。只有订单数量会发生变化。

## 保留优先级的修改订单请求是否会影响未成交订单数量（速率限制)?[​](/docs/zh-CN/binance-spot-api-docs/faqs/order_amend_keep_priority#保留优先级的修改订单请求是否会影响未成交订单数量速率限制 "保留优先级的修改订单请求是否会影响未成交订单数量（速率限制\)?的直接链接")

目前，保留优先级的修改订单请求对未成交订单计数为 0。

## 我如何才能知道我的订单是否已被修改？[​](/docs/zh-CN/binance-spot-api-docs/faqs/order_amend_keep_priority#我如何才能知道我的订单是否已被修改 "我如何才能知道我的订单是否已被修改？的直接链接")

如果订单修改成功，API 响应会包含具有新数量的订单。

在账户信息流上，您将收到执行类型为 `"x": "REPLACED"` 的 `"executionReport"` 事件。

如果修改后的订单隶属于订单列表，并且 client order ID 已被更改，您还将收到一个列表状态类型为 `"l": "UPDATED"` 的 "listStatus" 事件。

您也可以使用以下请求来查询订单修改历史：

API| 请求  
---|---  
REST API| `GET /api/v3/order/amendments`  
WebSocket API| `order.amendments`  
  
## 如果我的修改请求不成功，该怎么办？[​](/docs/zh-CN/binance-spot-api-docs/faqs/order_amend_keep_priority#如果我的修改请求不成功该怎么办 "如果我的修改请求不成功，该怎么办？的直接链接")

如果请求由于任何原因失败（比如，因为过滤器，权限，帐户限制等而失败），那么订单修改请求会被拒绝，而订单将保持不变。

## 我有可能在我的修改订单请求中重用现在的 clientOrderId 么？[​](/docs/zh-CN/binance-spot-api-docs/faqs/order_amend_keep_priority#我有可能在我的修改订单请求中重用现在的-clientorderid-么 "我有可能在我的修改订单请求中重用现在的 clientOrderId 么？的直接链接")

没问题。

默认状态下，被修改的订单会得到一个随即生成的新 client order ID。但是，你可以通过现有的 current client order ID 赋值给 `newClientOrderId` 参数的方式来重用数据。

## 我可以对冰山订单进行修改吗？[​](/docs/zh-CN/binance-spot-api-docs/faqs/order_amend_keep_priority#我可以对冰山订单进行修改吗 "我可以对冰山订单进行修改吗？的直接链接")

可以的。

请注意：只有当 `newQty` 低于未修改前的可见数量时，冰山订单的可见数量才能被改变。

## 我可以对订单列表进行修改吗？[​](/docs/zh-CN/binance-spot-api-docs/faqs/order_amend_keep_priority#我可以对订单列表进行修改吗 "我可以对订单列表进行修改吗？的直接链接")

在订单列表中的订单是可以被修改的。

请注意：OCO 订单对必须具有相同的数量，因为只有一个订单可以执行。这意味着修改任一订单都会影响两个订单。

对于 OTO 订单，您可以对生效订单和待处理订单进行单独修改。

## 哪些交易对允许保留优先级的修改订单请求？[​](/docs/zh-CN/binance-spot-api-docs/faqs/order_amend_keep_priority#哪些交易对允许保留优先级的修改订单请求 "哪些交易对允许保留优先级的修改订单请求？的直接链接")

相关信息可在 Exchange Information 中找到。 允许保留优先级的修改订单请求的交易对将会把 `amendAllowed` 设置为 `true`。