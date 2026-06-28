---
exchange: binance
source_url: https://developers.binance.com/docs/binance-spot-api-docs/websocket-api/market-data-requests
api_type: WebSocket
updated_at: 2026-06-28 18:50:22.444811
---

# Rate limits

### Connection limits[​](/docs/binance-spot-api-docs/websocket-api/rate-limits#connection-limits "Direct link to Connection limits")

There is a limit of **300 connections per attempt every 5 minutes**.

The connection is per **IP address**.

### General information on rate limits[​](/docs/binance-spot-api-docs/websocket-api/rate-limits#general-information-on-rate-limits "Direct link to General information on rate limits")

  * Current API rate limits can be queried using the [`exchangeInfo`](/docs/binance-spot-api-docs/websocket-api/rate-limits#exchange-information) request.
  * There are multiple rate limit types across multiple intervals.
  * Responses can indicate current rate limit status in the optional `rateLimits` field.
  * Requests fail with status `429` when unfilled order count or request rate limits are violated.



#### How to interpret rate limits[​](/docs/binance-spot-api-docs/websocket-api/rate-limits#how-to-interpret-rate-limits "Direct link to How to interpret rate limits")

A response with rate limit status may look like this:
    
    
    {  
        "id": "7069b743-f477-4ae3-81db-db9b8df085d2",  
        "status": 200,  
        "result": {  
            "serverTime": 1656400526260  
        },  
        "rateLimits": [  
            {  
                "rateLimitType": "REQUEST_WEIGHT",  
                "interval": "MINUTE",  
                "intervalNum": 1,  
                "limit": 6000,  
                "count": 70  
            }  
        ]  
    }  
    

The `rateLimits` array describes all currently active rate limits affected by the request.

Name| Type| Mandatory| Description  
---|---|---|---  
`rateLimitType`| ENUM| YES| Rate limit type: `REQUEST_WEIGHT`, `ORDERS`  
`interval`| ENUM| YES| Rate limit interval: `SECOND`, `MINUTE`, `HOUR`, `DAY`  
`intervalNum`| INT| YES| Rate limit interval multiplier  
`limit`| INT| YES| Request limit per interval  
`count`| INT| YES| Current usage per interval  
  
Rate limits are accounted by intervals.

For example, a `1 MINUTE` interval starts every minute. Request submitted at 00:01:23.456 counts towards the 00:01:00 minute's limit. Once the 00:02:00 minute starts, the count will reset to zero again.

Other intervals behave in a similar manner. For example, `1 DAY` rate limit resets at 00:00 UTC every day, and `10 SECOND` interval resets at 00, 10, 20... seconds of each minute.

APIs have multiple rate-limiting intervals. If you exhaust a shorter interval but the longer interval still allows requests, you will have to wait for the shorter interval to expire and reset. If you exhaust a longer interval, you will have to wait for that interval to reset, even if shorter rate limit count is zero.

#### How to show/hide rate limit information[​](/docs/binance-spot-api-docs/websocket-api/rate-limits#how-to-showhide-rate-limit-information "Direct link to How to show/hide rate limit information")

`rateLimits` field is included with every response by default.

However, rate limit information can be quite bulky. If you are not interested in detailed rate limit status of every request, the `rateLimits` field can be omitted from responses to reduce their size.

  * Optional `returnRateLimits` boolean parameter in request.

Use `returnRateLimits` parameter to control whether to include `rateLimits` fields in response to individual requests.

Default request and response:
        
        { "id": 1, "method": "time" }  
        
        
        {  
            "id": 1,  
            "status": 200,  
            "result": { "serverTime": 1656400526260 },  
            "rateLimits": [  
                {  
                    "rateLimitType": "REQUEST_WEIGHT",  
                    "interval": "MINUTE",  
                    "intervalNum": 1,  
                    "limit": 6000,  
                    "count": 70  
                }  
            ]  
        }  
        

Request and response without rate limit status:
        
        { "id": 2, "method": "time", "params": { "returnRateLimits": false } }  
        
        
        { "id": 2, "status": 200, "result": { "serverTime": 1656400527891 } }  
        

  * Optional `returnRateLimits` boolean parameter in connection URL.

If you wish to omit `rateLimits` from all responses by default, use `returnRateLimits` parameter in the query string instead:
        
        wss://ws-api.binance.com:443/ws-api/v3?returnRateLimits=false  
        

This will make all requests made through this connection behave as if you have passed `"returnRateLimits": false`.

If you _want_ to see rate limits for a particular request, you need to explicitly pass the `"returnRateLimits": true` parameter.




**Note:** Your requests are still rate limited if you hide the `rateLimits` field in responses.

### IP limits[​](/docs/binance-spot-api-docs/websocket-api/rate-limits#ip-limits "Direct link to IP limits")

  * Every request has a certain **weight** , added to your limit as you perform requests. 
    * The heavier the request (e.g. querying data from multiple symbols), the more weight the request will cost.
    * Connecting to WebSocket API costs 2 weight.
  * Current weight usage is indicated by the `REQUEST_WEIGHT` rate limit type.
  * Use the [`exchangeInfo`](/docs/binance-spot-api-docs/websocket-api/rate-limits#exchange-information) request to keep track of the current weight limits.
  * Weight is accumulated **per IP address** and is shared by all connections from that address.
  * If you go over the weight limit, requests fail with status `429`. 
    * This status code indicates you should back off and stop spamming the API.
    * Rate-limited responses include a `retryAfter` field, indicating when you can retry the request.
  * **Repeatedly violating rate limits and/or failing to back off after receiving 429s will result in an automated IP ban and you will be disconnected.**
    * Requests from a banned IP address fail with status `418`.
    * `retryAfter` field indicates the timestamp when the ban will be lifted.
  * IP bans are tracked and **scale in duration** for repeat offenders, **from 2 minutes to 3 days**.



Successful response indicating that in 1 minute you have used 70 weight out of your 6000 limit:
    
    
    {  
        "id": "7069b743-f477-4ae3-81db-db9b8df085d2",  
        "status": 200,  
        "result": [],  
        "rateLimits": [  
            {  
                "rateLimitType": "REQUEST_WEIGHT",  
                "interval": "MINUTE",  
                "intervalNum": 1,  
                "limit": 6000,  
                "count": 70  
            }  
        ]  
    }  
    

Failed response indicating that you are banned and the ban will last until epoch `1659146400000`:
    
    
    {  
        "id": "fc93a61a-a192-4cf4-bb2a-a8f0f0c51e06",  
        "status": 418,  
        "error": {  
            "code": -1003,  
            "msg": "Way too much request weight used; IP banned until 1659146400000. Please use WebSocket Streams for live updates to avoid bans.",  
            "data": {  
                "serverTime": 1659142907531,  
                "retryAfter": 1659146400000  
            }  
        },  
        "rateLimits": [  
            {  
                "rateLimitType": "REQUEST_WEIGHT",  
                "interval": "MINUTE",  
                "intervalNum": 1,  
                "limit": 6000,  
                "count": 2411  
            }  
        ]  
    }  
    

### Unfilled Order Count[​](/docs/binance-spot-api-docs/websocket-api/rate-limits#unfilled-order-count "Direct link to Unfilled Order Count")

  * Successfully placed orders update the `ORDERS` rate limit type.
  * Rejected or unsuccessful orders might or might not update the `ORDERS` rate limit type.
  * **Please note that if your orders are consistently filled by trades, you can continuously place orders on the API**. For more information, please see [Spot Unfilled Order Count Rules](/docs/binance-spot-api-docs/faqs/order_count_decrement).
  * Use the [`account.rateLimits.orders`](/docs/binance-spot-api-docs/websocket-api/account-requests#query-unfilled-order-count) request to keep track of how many orders you have placed within this interval.
  * If you exceed this, requests fail with status `429`. 
    * This status code indicates you should back off and stop spamming the API.
    * Responses that have a status `429` include a `retryAfter` field, indicating when you can retry the request.
  * This is maintained **per account** and is shared by all API keys of the account.



Successful response indicating that you have placed 12 orders in 10 seconds, and 4043 orders in the past 24 hours:
    
    
    {  
        "id": "e2a85d9f-07a5-4f94-8d5f-789dc3deb097",  
        "status": 200,  
        "result": {  
            "symbol": "BTCUSDT",  
            "orderId": 12510053279,  
            "orderListId": -1,  
            "clientOrderId": "a097fe6304b20a7e4fc436",  
            "transactTime": 1655716096505,  
            "price": "0.10000000",  
            "origQty": "10.00000000",  
            "executedQty": "0.00000000",  
            "origQuoteOrderQty": "0.000000",  
            "cummulativeQuoteQty": "0.00000000",  
            "status": "NEW",  
            "timeInForce": "GTC",  
            "type": "LIMIT",  
            "side": "BUY",  
            "workingTime": 1655716096505,  
            "selfTradePreventionMode": "NONE"  
        },  
        "rateLimits": [  
            {  
                "rateLimitType": "ORDERS",  
                "interval": "SECOND",  
                "intervalNum": 10,  
                "limit": 50,  
                "count": 12  
            },  
            {  
                "rateLimitType": "ORDERS",  
                "interval": "DAY",  
                "intervalNum": 1,  
                "limit": 160000,  
                "count": 4043  
            },  
            {  
                "rateLimitType": "REQUEST_WEIGHT",  
                "interval": "MINUTE",  
                "intervalNum": 1,  
                "limit": 6000,  
                "count": 321  
            }  
        ]  
    }

---

# 速率限制

### 连接数量限制[​](/docs/zh-CN/binance-spot-api-docs/websocket-api/rate-limits#连接数量限制 "连接数量限制的直接链接")

每IP地址、每5分钟最多可以发送300次连接请求。

### 速率限制基本信息[​](/docs/zh-CN/binance-spot-api-docs/websocket-api/rate-limits#速率限制基本信息 "速率限制基本信息的直接链接")

  * [`exchangeInfo`](/docs/zh-CN/binance-spot-api-docs/websocket-api/general-requests#exchangeInfo) 有包含与速率限制相关的信息。
  * 根据不同的间隔，有多种频率限制类型。
  * 从响应中的可选 `rateLimits` 字段，能看到当前的频率限制状态。
  * 当您超出未成交订单计数或者请求速率限制时，请求会失败并返回 HTTP 状态代码 429。



#### 如何咨询频率限制[​](/docs/zh-CN/binance-spot-api-docs/websocket-api/rate-limits#如何咨询频率限制 "如何咨询频率限制的直接链接")

频率限制状态的响应可能如下所示：
    
    
    {  
        "id": "7069b743-f477-4ae3-81db-db9b8df085d2",  
        "status": 200,  
        "result": {  
            "serverTime": 1656400526260  
        },  
        "rateLimits": [  
            {  
                "rateLimitType": "REQUEST_WEIGHT",  
                "interval": "MINUTE",  
                "intervalNum": 1,  
                "limit": 6000,  
                "count": 70  
            }  
        ]  
    }  
    

`rate Limits` 数组描述了受请求影响的所有当前的速率限制。

名称| 类型| 是否必须| 描述  
---|---|---|---  
`rateLimitType`| ENUM| YES| 频率限制类型: `REQUEST_WEIGHT`, `ORDERS`  
`interval`| ENUM| YES| 频率限制间隔: `SECOND`, `MINUTE`, `HOUR`, `DAY`  
`intervalNum`| INT| YES| 频率限制间隔乘数  
`limit`| INT| YES| 每个间隔的请求限制  
`count`| INT| YES| 每个间隔的当前使用情况  
  
频率限制按间隔计算。

例如，`1 MINUTE` 间隔表示每分钟开始。 在 00:01:23.456 提交的请求计入 00:01:00 分钟的限制。 一旦 00:02:00 分钟开始，计数将再次重置为零。

其他间隔的行为方式类似。 例如，`1 DAY` 频率限制是在每天 00:00 UTC 重置，并且 `10 SECOND` 间隔重置为每分钟的 00、10、20...秒。

API 有多种频率限制间隔。 如果您用完了较短的间隔但较长的间隔仍然允许请求，您将不得不等待较短的间隔到期并重置。 如果你用完了更长的间隔，你将不得不等待那个间隔重置，即使较短的频率限制计数为零。

#### 如何显示/隐藏频率限制信息[​](/docs/zh-CN/binance-spot-api-docs/websocket-api/rate-limits#如何显示隐藏频率限制信息 "如何显示/隐藏频率限制信息的直接链接")

默认情况下，每个响应都包含 `rateLimits` 字段。

但是，频率限制信息可能非常大。 如果您对每个请求的详细频率限制状态不感兴趣，可以从响应中省略 `rateLimits` 字段。

  * 请求中的可选 `returnRateLimits` boolean 参数。

使用 `returnRateLimits` 参数控制是否包含 `rateLimits` 字段以响应单个请求。

默认请求和响应：
        
        { "id": 1, "method": "time" }  
        
        
        {  
            "id": 1,  
            "status": 200,  
            "result": { "serverTime": 1656400526260 },  
            "rateLimits": [  
                {  
                    "rateLimitType": "REQUEST_WEIGHT",  
                    "interval": "MINUTE",  
                    "intervalNum": 1,  
                    "limit": 6000,  
                    "count": 70  
                }  
            ]  
        }  
        

没有频率限制状态的请求和响应：
        
        { "id": 2, "method": "time", "params": { "returnRateLimits": false } }  
        
        
        { "id": 2, "status": 200, "result": { "serverTime": 1656400527891 } }  
        

  * 连接 URL 中可选的 `returnRateLimits` boolean 参数。

如果您希望在默认情况下从所有响应中省略 `rateLimits`，可以在 query string 中使用 `returnRateLimits` 参数：
        
        wss://ws-api.binance.com:443/ws-api/v3?returnRateLimits=false  
        

这将使通过此连接发出的所有请求的行为就像您已传了 `"returnRateLimits"：false` 一样。

如果您_想_查看特定请求的频率限制，您需要特定传 `"returnRateLimits"：true` 参数。




**注意:** 如果您在响应中隐藏 `rateLimits` 字段，您的请求仍然还是会受到频率限制的。

### IP 访问限制[​](/docs/zh-CN/binance-spot-api-docs/websocket-api/rate-limits#ip-访问限制 "IP 访问限制的直接链接")

  * 每个请求都有一个特定的 **权重** ，它会添加到您的访问限制中。 
    * 越消耗资源的接口, 比如查询多个交易对, 权重就会越大。
    * 连接到 WebSocket API 会用到2个权重。
  * 当前权重使用由 `REQUEST_WEIGHT` 频率限制类型指示。
  * 请使用[`exchangeInfo`](/docs/zh-CN/binance-spot-api-docs/websocket-api/general-requests#exchangeInfo)请求来跟踪当前的重量限制。
  * 权重是基于**每个 IP 地址** 累积的，并由来自该地址的所有连接共享。
  * 如果超多限制，客服端会收到 `429`。 
    * 这错误代码表示您有责任停止发送请求，不得滥用API。
    * 响应会包含一个 `retryAfter` 字段，指示在什么时候您能重试。
  * **屡次违反速率限制或者在收到429后未能退缩将导致自动 IP 封禁和断开连接。**
    * 被禁止 IP 地址的请求失败，状态为 `418`。
    * `retryAfter` 字段表示解除禁令的timestamp。
  * 频繁违反限制的封禁时间会**逐渐延长** ，**从最短2分钟到最长3天** 。



表示在1分钟内使用了（1200权重限制中的）70权重的成功响应：
    
    
    {  
        "id": "7069b743-f477-4ae3-81db-db9b8df085d2",  
        "status": 200,  
        "result": [],  
        "rateLimits": [  
            {  
                "rateLimitType": "REQUEST_WEIGHT",  
                "interval": "MINUTE",  
                "intervalNum": 1,  
                "limit": 6000,  
                "count": 70  
            }  
        ]  
    }  
    

表示已被封禁且封禁将在 epoch `1659146400000` 解锁的失败响应：
    
    
    {  
        "id": "fc93a61a-a192-4cf4-bb2a-a8f0f0c51e06",  
        "status": 418,  
        "error": {  
            "code": -1003,  
            "msg": "Way too much request weight used; IP banned until 1659146400000. Please use WebSocket Streams for live updates to avoid bans.",  
            "data": {  
                "serverTime": 1659142907531,  
                "retryAfter": 1659146400000  
            }  
        },  
        "rateLimits": [  
            {  
                "rateLimitType": "REQUEST_WEIGHT",  
                "interval": "MINUTE",  
                "intervalNum": 1,  
                "limit": 6000,  
                "count": 2411  
            }  
        ]  
    }  
    

### 未成交订单计数[​](/docs/zh-CN/binance-spot-api-docs/websocket-api/rate-limits#未成交订单计数 "未成交订单计数��的直接链接")

  * 成功下单将更新 `订单` 速率限制类型。
  * 被拒绝或不成功的订单可能会也可能不会更新 `订单` 速率限制类型。
  * **请注意，如果您的订单一直顺利完成交易，您可以通过 API 持续下订单** 。更多信息，请参见 [现货未成交订单计数规则](/docs/zh-CN/binance-spot-api-docs/faqs/order_count_decrement)。
  * 使用 [`account.rateLimits.orders`](/docs/zh-CN/binance-spot-api-docs/websocket-api/account-requests#query-unfilled-order-count) 请求来跟踪您在此时间间隔内下了多少订单。
  * 如果超过此值，请求将失败，状态为 `429`。 
    * 此状态代码表示您应退出并停止向 API 滥发信息。
    * 状态为 `429` 的响应会包含 `retryAfter` 字段，用以指示何时可以重试请求。
  * 这是按 **每一个账户** 维护的，并由该账户的所有 API 密钥共享。



表示在10秒内下了12个订单和在24小时内下了4043个订单的成功响应：
    
    
    {  
        "id": "e2a85d9f-07a5-4f94-8d5f-789dc3deb097",  
        "status": 200,  
        "result": {  
            "symbol": "BTCUSDT",  
            "orderId": 12510053279,  
            "orderListId": -1,  
            "clientOrderId": "a097fe6304b20a7e4fc436",  
            "transactTime": 1655716096505,  
            "price": "0.10000000",  
            "origQty": "10.00000000",  
            "executedQty": "0.00000000",  
            "origQuoteOrderQty": "0.000000",  
            "cummulativeQuoteQty": "0.00000000",  
            "status": "NEW",  
            "timeInForce": "GTC",  
            "type": "LIMIT",  
            "side": "BUY",  
            "workingTime": 1655716096505,  
            "selfTradePreventionMode": "NONE"  
        },  
        "rateLimits": [  
            {  
                "rateLimitType": "ORDERS",  
                "interval": "SECOND",  
                "intervalNum": 10,  
                "limit": 50,  
                "count": 12  
            },  
            {  
                "rateLimitType": "ORDERS",  
                "interval": "DAY",  
                "intervalNum": 1,  
                "limit": 160000,  
                "count": 4043  
            },  
            {  
                "rateLimitType": "REQUEST_WEIGHT",  
                "interval": "MINUTE",  
                "intervalNum": 1,  
                "limit": 6000,  
                "count": 321  
            }  
        ]  
    }