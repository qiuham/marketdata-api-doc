---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/spot/faqs/order_count_decrement
api_type: REST
updated_at: 2026-11-13 20:24:34.800480
---

# Spot Unfilled Order Count Rules

To ensure a fair and orderly Spot market, we limit the rate at which new orders may be placed.

The rate limit applies to the number of new, _unfilled_ orders placed within a time interval. That is, orders which are partially or fully filled do not count against the rate limit.

Unfilled order rate limit rewards efficient traders.

**So long as your orders trade, you can keep trading.**

More information: [How do filled orders affect the rate limit?](/en/docs/products/spot/faqs/order_count_decrement#how-do-filled-orders-affect-the-unfilled-order-count)

### What are the current rate limits?

You can query current rate limits using the "exchange information" request.

The `"rateLimitType": "ORDERS"` indicates the current unfilled order rate limit.

Please refer to the API documentation:

API| Request  
---|---  
FIX API| [LimitQuery`<XLQ>`](/en/docs/products/spot/fix-api#limitquery-xlq)  
REST API| [`GET /api/v3/exchangeInfo`](/en/docs/catalog/core-trading-spot-trading/api/rest-api/general#exchange-info)  
WebSocket API| [`exchangeInfo`](/en/docs/catalog/core-trading-spot-trading/api/ws-api/general#exchange-info)  
  
Order placement requests are also affected by the general request rate limits on REST and WebSocket API and the message limits on FIX API.

If you send too many requests at a high rate, you will be blocked by the API.

### How does the unfilled `ORDERS` rate limit work?

Every successful request to place an order adds to the unfilled order count for the current time interval. If too many unfilled orders accumulate during the interval, subsequent requests will be rejected.

For example, if the unfilled order rate limit is 100 per 10 seconds:
    
    
    Code
    
    {
        "rateLimitType": "ORDERS",
        "interval": "SECOND",
        "intervalNum": 10,
        "limit": 100
    }

then you can place at most 100 new orders between 12:34:00 and 12:34:10, then 100 more from 12:34:10 to 12:34:20, and so on.

If the newly placed orders receive fills, your unfilled order count decreases and you may place more orders during the time interval.

More information: [How do filled orders affect the rate limit?](/en/docs/products/spot/faqs/order_count_decrement#how-do-filled-orders-affect-the-unfilled-order-count)

When an order is rejected by the system due to the unfilled order rate limit, the HTTP status code is set to `429 Too Many Requests` and the error code is `-1015 "Too many new orders"`.

If you encounter these errors, please stop sending orders until the affected rate limit interval expires.

Please refer to the API documentation:

API| Documentation  
---|---  
FIX API| [Unfilled Order Count](/en/docs/products/spot/fix-api#unfilled-order-count)  
REST API| [Unfilled Order Count](/en/docs/products/spot/rest-api#unfilled-order-count)  
WebSocket API| [Unfilled Order Count](/en/docs/products/spot/web-socket-api#unfilled-order-count)  
  
### Is the unfilled order count tracked by IP address?

Unfilled order count is tracked **by (sub)account**.

Unfilled order count is shared across all IP addresses, all API keys, and all APIs.

### How do filled orders affect the unfilled order count?

When an order is filled for the first time (partially or fully), your unfilled order count is decremented by one order for all intervals of the `ORDERS` rate limit. Effectively, orders that trade do not count towards the rate limit, allowing efficient traders to keep placing new orders.

Certain orders provide additional incentive:

  * **Orders that do not fill immediately (that is, first fill in the maker phase).**
  * Orders that fill large quantities.



In these cases the unfilled order count may be decremented by more than one order for each order that starts trading.

**Notes:**

  * **The examples only give a general idea of the behavior.** The 10-second interval is used for simplicity. The actual configuration on the live exchange may be different.
  * There is a short delay between the order being filled and the unfilled order count update. Please be careful when your unfilled order count is close to the limit.
  * Please refer to [How does unfilled `ORDERS` rate limit work?](/en/docs/products/spot/faqs/order_count_decrement#how-does-the-unfilled-orders-rate-limit-work) to see how you can monitor the unfilled order count depending on the API.



**Example 1** — taker:

Time| Action| Unfilled order count  
---|---|---  
00:00:00| | 0  
00:00:01| Place LIMIT order A| 1 — new order (+1)  
00:00:02| Place LIMIT order B| 2 — new order (+1)  
| (order B partially filled)| 1 — first fill as taker (−1)  
00:00:03| Place LIMIT order C| 2 — new order (+1)  
00:00:04| (order B partially filled)| 2  
00:00:04| (order B filled)| 2  
00:00:05| Place MARKET order D| 3 — new order (+1)  
| (order D fully filled)| 2 — first fill as taker (−1)  
  
Note how for every taker order that immediately trades, the unfilled order count is decremented later, allowing you to keep placing orders.

**Example 2** — maker:

Time| Action| Unfilled order count  
---|---|---  
00:00:00| | 0  
00:00:01| Place LIMIT order A| 1 — new order (+1)  
00:00:01| Place LIMIT order B| 2 — new order (+1)  
00:00:02| Place LIMIT order C| 3 — new order (+1)  
00:00:02| Place LIMIT order D| 4 — new order (+1)  
00:00:02| Place LIMIT order E| 5 — new order (+1)  
00:00:03| (order A partially filled)| 0 — first fill as maker (−5)  
00:00:04| Place LIMIT order F| 1 — new order (+1)  
00:00:04| Place LIMIT order G| 2 — new order (+1)  
00:00:05| (order A partially filled)| 2  
00:00:05| (order A filled)| 2  
00:00:05| (order B partially filled)| 0 — first fill as maker (−5)  
00:00:06| Place LIMIT order H| 1 — new order (+1)  
  
Note how for every maker order that is filled later, the unfilled order count is decremented by a higher amount, allowing you to place more orders.

### How do canceled or expired orders affect the unfilled order count?

Canceling an order does not change the unfilled order count.

Expired orders also do not change the unfilled order count.

**Example:**

Time| Action| Unfilled order count  
---|---|---  
00:00:00| | 0  
00:00:01| Place LIMIT order A| 1 — new order (+1)  
00:00:02| Cancel order A| 1  
00:00:02| Place LIMIT order B| 2 — new order (+1)  
00:00:03| Place LIMIT FOK order C| 3 — new order (+1)  
| (order C is fully filled)| 2 — fill (−1)  
00:00:05| Place LIMIT order D| 3 — new order (+1)  
00:00:06| Place LIMIT FOK order E| 4 — new order (+1)  
| (order E expires with no fill)| 4  
00:00:07| Cancel order D| 4  
00:00:07| Place LIMIT order F| 5 — new order (+1)  
  
### Which time zone does `"interval":"DAY"` use?

UTC

### What happens if I placed an order yesterday but it is filled the next day?

New order fills decrease your _current_ unfilled order count regardless of when the orders were placed.

**Example:**

Time| Action| Unfilled order count  
---|---|---  
2024-01-01 09:00| Place 5 orders: 1..5| 5  
2024-01-02 00:00| (rate limit interval reset)| 0  
2024-01-02 09:00| Place 10 orders: 6..15| 10  
2024-01-02 12:00| (orders 1..5 are filled)| 5  
2024-01-02 13:00| (orders 6..10 are filled)| 0  
2024-01-02 14:00| Place 2 orders: 16, 17| 2  
2024-01-02 15:00| (orders 11..15 are filled)| 0  
  
**Note:** You do not get credit for order fills. That is, once the unfilled order count is down to zero, additional fills will not decrease it further. New orders will increase the count as usual.

Was this page helpful?

Last modified on November 12, 2026

[Order Amend Keep Priority](/en/docs/products/spot/faqs/order_amend_keep_priority)[Pegged orders](/en/docs/products/spot/faqs/pegged_orders)

---

# 现货未成交订单计数规则

为确保公平有序的现货市场，我们限制了新订单的下达率。

速率限制适用于在时间间隔内下达的新的、 _未成交_ 的订单数量。也就是说，部分或全部成交的订单不计入速率限制。

未成交的订单速率限制奖励高效的交易者。只要您的订单成交，您就可以继续交易。详细信息：[已成交订单如何影响速率限制?](/zh-CN/docs/products/spot/faqs/order_count_decrement#%E5%B7%B2%E6%88%90%E4%BA%A4%E7%9A%84%E8%AE%A2%E5%8D%95%E5%A6%82%E4%BD%95%E5%BD%B1%E5%93%8D%E6%9C%AA%E6%88%90%E4%BA%A4%E7%9A%84%E8%AE%A2%E5%8D%95%E6%95%B0%E9%87%8F)

### 当前的速率限制是多少？

您可以使用 "exchange information" 请求查询当前的速率限制。

`"rateLimitType": "ORDERS"` 表示当前未成交的订单速率限制。

请参考 API 文档:

API| 请求  
---|---  
FIX API| [LimitQuery`<XLQ>`](/zh-CN/docs/products/spot/fix-api#limitquery-xlq)  
REST API| [`GET /api/v3/exchangeInfo`](/zh-CN/docs/catalog/core-trading-spot-trading/api/rest-api/general#exchange-info)  
WebSocket API| [`exchangeInfo`](/zh-CN/docs/catalog/core-trading-spot-trading/api/ws-api/general#exchange-info)  
  
下单请求还受到 REST 和 WebSocket API 上的常规请求速率限制以及 FIX API 上的消息限制的影响。如果您以高速率发送过多的请求，您将会被 API 阻止。

### 如何运作未成交的 `ORDERS` 速率限制？

每次成功下单的请求都会增加当前时间间隔内的未成交订单计数。如果在时间间隔内累积了太多未成交的订单，后续的请求将被拒绝。

例如，如果未成交的订单速率限制为每 10 秒 100 个：
    
    
    Code
    
    {
        "rateLimitType": "ORDERS",
        "interval": "SECOND",
        "intervalNum": 10,
        "limit": 100
    }

那么，您在 12：34：00 到 12：34：10 之间最多可以下 100 个新订单，然后在 12：34：10 到 12：34：20 之间再下 100 个新订单，依此类推。

如果新下的订单成交，那么您的未成交订单数量会减少，您可能会在该时间间隔内下更多的订单。详细信息：[已成交订单如何影响速率限制？](/zh-CN/docs/products/spot/faqs/order_count_decrement#%E5%B7%B2%E6%88%90%E4%BA%A4%E7%9A%84%E8%AE%A2%E5%8D%95%E5%A6%82%E4%BD%95%E5%BD%B1%E5%93%8D%E6%9C%AA%E6%88%90%E4%BA%A4%E7%9A%84%E8%AE%A2%E5%8D%95%E6%95%B0%E9%87%8F)

当订单因未成交订单速率限制而被系统拒绝时，HTTP 状态代码会被设置为`429 Too Many Requests`，错误代码为`-1015 "Too many new orders"`。

如果您遇到这些错误，请停止发送订单，直到受影响的速率限制间隔到期。

请参考 API 文档:

API| 文档  
---|---  
FIX API| [未成交订单计数](/zh-CN/docs/products/spot/fix-api#%E8%BF%9E%E6%8E%A5%E9%99%90%E5%88%B6)  
REST API| [未成交订单计数](/zh-CN/docs/products/spot/rest-api#%E6%9C%AA%E6%88%90%E4%BA%A4%E8%AE%A2%E5%8D%95%E8%AE%A1%E6%95%B0)  
WebSocket API| [未成交订单计数](/zh-CN/docs/products/spot/web-socket-api#%E6%9C%AA%E6%88%90%E4%BA%A4%E8%AE%A2%E5%8D%95%E8%AE%A1%E6%95%B0)  
  
### 是否按 IP 地址来统计未成交的订单计数？

未成交订单计数是根据 **（子）账户** 来统计的。

未成交订单计数在所有 IP 地址、所有 API 密钥和所有 API 之间共享。

### 已成交的订单如何影响未成交的订单数量？

当订单首次（部分或全部）成交时，在 `ORDERS` 速率限制的所有时间间隔内，您的未成交订单数量将会减少一个订单。实际上，已成交的订单不计入速率限制，这将允许高效的交易者继续下新订单。

某些订单会提供额外的激励：

  * **未立即成交的订单（即，在 maker 阶段首次成交）。**
  * 大批量成交的订单。



在这些情况下，对于每个开始交易的订单，未成交的订单数量可能会减少多个订单。

**注意：**

  * **这些示例仅给出了相关行为的通用概念。** 为了简单起见，请使用 10 秒间隔。实时交易平台上的实际配置可能会有所不同。
  * 在正在执行的订单和未成交订单计数更新之间有短暂的延迟。当您的未成交订单数量接近限制时，请务必小心。
  * 请参考 [如何运作未成交的 `ORDERS` 速率限制？](/zh-CN/docs/products/spot/faqs/order_count_decrement#%E5%A6%82%E4%BD%95%E8%BF%90%E4%BD%9C%E6%9C%AA%E6%88%90%E4%BA%A4%E7%9A%84-orders-%E9%80%9F%E7%8E%87%E9%99%90%E5%88%B6) 以了解如何根据 API 来监控未成交订单计数。



**例 1** — taker:

时间| 操作| 未成交订单数量  
---|---|---  
00:00:00| | 0  
00:00:01| 下订单 A (限价单)| 1 — 新订单 (+1)  
00:00:02| 下订单 B (限价单)| 2 — 新订单 (+1)  
| (订单 B 部分成交)| 1 — 作为 taker 首次成交 (−1)  
00:00:03| 下订单 C (限价单)| 2 — 新订单 (+1)  
00:00:04| (订单 B 部分成交)| 2  
00:00:04| (订单 B 已成交)| 2  
00:00:05| 下订单 D (市价单)| 3 — 新订单 (+1)  
| (订单 D 全部成交)| 2 — 作为 taker 首次成交 (−1)  
  
请注意，对于每个立即交易的 taker 订单，未成交的订单数量稍后会减少，从而允许您继续下单。

**例 2** — maker:

时间| 操作| 未成交订单数量  
---|---|---  
00:00:00| | 0  
00:00:01| 下订单 A (限价单)| 1 — 新订单 (+1)  
00:00:01| 下订单 B (限价单)| 2 — 新订单 (+1)  
00:00:02| 下订单 C (限价单)| 3 — 新订单 (+1)  
00:00:02| 下订单 D (限价单)| 4 — 新订单 (+1)  
00:00:02| 下订单 E (限价单)| 5 — 新订单 (+1)  
00:00:03| (订单 A 部分成交)| 0 — 作为 maker 首次成交 (−5)  
00:00:04| 下订单 F (限价单)| 1 — 新订单 (+1)  
00:00:04| 下订单 G (限价单)| 2 — 新订单 (+1)  
00:00:05| (订单 A 部分成交)| 2  
00:00:05| (订单 A 已成交)| 2  
00:00:05| (订单 B 部分成交)| 0 — 作为 maker 首次成交 (−5)  
00:00:06| 下订单 H (限价单)| 1 — 新订单 (+1)  
  
请注意，对于稍后执行的每个 maker 单，未执行的订单数量会减去更高的数量，从而允许您下更多订单。

### 取消或过期的订单如何影响未成交的订单数量？

取消订单不会更改未成交的订单计数。

过期的订单也不会改变未成交的订单计数。

**例:**

时间| 操作| 未成交订单数量  
---|---|---  
00:00:00| | 0  
00:00:01| 下订单 A (限价单)| 1 — 新订单 (+1)  
00:00:02| 取消订单 A| 1  
00:00:02| 下订单 B (限价单)| 2 — 新订单(+1)  
00:00:03| 下订单 C (限价 FOK 单)| 3 — 新订单 (+1)  
| (订单 C 已成交)| 2 — fill (−1)  
00:00:05| 下订单 D (限价单)| 3 — 新订单 (+1)  
00:00:06| 下订单 E (限价 FOK 单)| 4 — 新订单 (+1)  
| (订单 E 过期且没有成交)| 4  
00:00:07| 取消订单 D| 4  
00:00:07| 下订单 F (限价单)| 5 — 新订单 (+1)  
  
### `interval：DAY` 使用哪个时区？

UTC。

### 如果我昨天下了订单，但第二天才成交，会发生什么情况？

无论订单是何时成交的，新成交的订单都会减少您当前未成交的订单数量。

**例:**

时间| 操作| 未成交订单数量  
---|---|---  
2024-01-01 09:00| 下 5 个订单: 1..5| 5  
2024-01-02 00:00| (速率间隔重置)| 0  
2024-01-02 09:00| 下 10 个订单: 6..15| 10  
2024-01-02 12:00| (订单 1...5 已成交)| 5  
2024-01-02 13:00| (订单 6...10 已成交)| 0  
2024-01-02 14:00| 下 2 个订单: 16, 17| 2  
2024-01-02 15:00| (订单 11...15 已成交)| 0  
  
**注意：** 您不会因订单的成交而获得信用。也就是说，一旦未成交的订单数量减少到零，额外的成交将不会进一步影响未成交订单计数。新订单将像依旧增加计数。

此页面是否有帮助？

Last modified on November 12, 2026

[保留优先级的修改订单请求（Order Amend Keep Priority）](/zh-CN/docs/products/spot/faqs/order_amend_keep_priority)[挂钩订单（Pegged orders）](/zh-CN/docs/products/spot/faqs/pegged_orders)