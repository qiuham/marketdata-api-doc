---
exchange: binance
source_url: https://developers.binance.com/docs/binance-spot-api-docs/rest-api/general-information-on-endpoints
api_type: REST
updated_at: 2026-06-28 18:49:45.519733
---

# LIMITS

### General Info on Limits[​](/docs/binance-spot-api-docs/rest-api/limits#general-info-on-limits "Direct link to General Info on Limits")

  * The following `intervalLetter` values for headers: 
    * SECOND => S
    * MINUTE => M
    * HOUR => H
    * DAY => D
  * `intervalNum` describes the amount of the interval. For example, `intervalNum` 5 with `intervalLetter` M means "Every 5 minutes".
  * The `/api/v3/exchangeInfo` `rateLimits` array contains objects related to the exchange's `RAW_REQUESTS`, `REQUEST_WEIGHT`, and `ORDERS` rate limits. These are further defined in the `ENUM definitions` section under `Rate limiters (rateLimitType)`.
  * Requests fail with HTTP status code 429 when you exceed the request rate limit.



### IP Limits[​](/docs/binance-spot-api-docs/rest-api/limits#ip-limits "Direct link to IP Limits")

  * Every request will contain `X-MBX-USED-WEIGHT-(intervalNum)(intervalLetter)` in the response headers which has the current used weight for the IP for all request rate limiters defined.
  * Each route has a `weight` which determines for the number of requests each endpoint counts for. Heavier endpoints and endpoints that do operations on multiple symbols will have a heavier `weight`.
  * When a 429 is received, it's your obligation as an API to back off and not spam the API.
  * **Repeatedly violating rate limits and/or failing to back off after receiving 429s will result in an automated IP ban (HTTP status 418).**
  * IP bans are tracked and **scale in duration** for repeat offenders, **from 2 minutes to 3 days**.
  * A `Retry-After` header is sent with a 418 or 429 responses and will give the **number of seconds** required to wait, in the case of a 429, to prevent a ban, or, in the case of a 418, until the ban is over.
  * **The limits on the API are based on the IPs, not the API keys.**



### Unfilled Order Count[​](/docs/binance-spot-api-docs/rest-api/limits#unfilled-order-count "Direct link to Unfilled Order Count")

  * Every successful order response will contain a `X-MBX-ORDER-COUNT-(intervalNum)(intervalLetter)` header indicating how many orders you have placed for that interval.   
  
To monitor this, refer to [`GET api/v3/rateLimit/order`](/docs/binance-spot-api-docs/rest-api/account-endpoints#query-unfilled-order-count).
  * Rejected/unsuccessful orders are not guaranteed to have `X-MBX-ORDER-COUNT-**` headers in the response.
  * If you have exceeded this, you will receive a 429 error with the `Retry-After` header.
  * **Please note that if your orders are consistently filled by trades, you can continuously place orders on the API**. For more information, please see [Spot Unfilled Order Count Rules](/docs/binance-spot-api-docs/faqs/order_count_decrement).
  * **The number of unfilled orders is tracked for each account.**

---

# 访问限制

### 访问限制基本信息[​](/docs/zh-CN/binance-spot-api-docs/rest-api/limits#访问限制基本信息 "访问限制基本信息的直接链接")

  * 以下是 `intervalLetter` 作为头部值: 
    * SECOND => S
    * MINUTE => M
    * HOUR => H
    * DAY => D
  * 在 `/api/v3/exchangeInfo`接口中`rateLimits`数组里包含有REST接口(不限于本篇的REST接口)的访问限制。包括带权重的访问频次限制、下单速率限制。参考 [枚举定义](/docs/zh-CN/binance-spot-api-docs/enums) 中有关有限制类型的进一步说明。
  * 当您超出请求速率限制时，请求会失败并返回 HTTP 状态代码 429。



### IP 访问限制[​](/docs/zh-CN/binance-spot-api-docs/rest-api/limits#ip-访问限制 "IP 访问限制的直接链接")

  * 每个请求将包含一个`X-MBX-USED-WEIGHT-(intervalNum)(intervalLetter)`的头，其中包含当前IP所有请求的已使用权重。
  * 每一个接口均有一个相应的权重(weight)，有的接口根据参数不同可能拥有不同的权重。越消耗资源的接口权重就会越大。
  * 收到429时，您有责任停止发送请求，不得滥用API。
  * **收到429后仍然继续违反访问限制，会被封禁IP，并收到418错误码**
  * 频繁违反限制，封禁时间会逐渐延长，**从最短2分钟到最长3天**.
  * `Retry-After`的头会与带有418或429的响应发送，并且会给出**以秒为单位** 的等待时长(如果是429)以防止禁令，或者如果是418，直到禁令结束。
  * **访问限制是基于IP的，而不是API Key**



### 未成交订单计数[​](/docs/zh-CN/binance-spot-api-docs/rest-api/limits#未成交订单计数 "未成交订单计数的直接链接")

  * 每个成功的订单响应都将包含一个 `X-MBX-ORDER-COUNT-(intervalNum)(intervalLetter)` 报文头，用于标识您在该时间间隔内下了多少订单。  
  
如果您想要对此进行监控，请参阅 [`GET api/v3/rateLimit/order`](/docs/zh-CN/binance-spot-api-docs/rest-api/account-endpoints#query-unfilled-order-count)。
  * 被拒绝/不成功的订单不保证在响应中有 `X-MBX-ORDER-COUNT-**` 报文头。
  * 如果超过此值，您将收到一个 429 错误，而且不带 `Retry-After` 报文头。
  * **请注意，如果您的订单一直顺利完成交易，您可以通过 API 持续下订单** 。更多信息，请参见[现货未成交订单计数规则](/docs/zh-CN/binance-spot-api-docs/faqs/order_count_decrement)。
  * **未成交订单数量是按照每个账户来统计的** 。