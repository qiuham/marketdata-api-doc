---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/margin-trading/general-info
api_type: REST
updated_at: 2026-11-13 20:28:35.118138
---

# General Info

## General API Information

  * The following base endpoints are available:
    * **<https://api.binance.com>**
    * **<https://api1.binance.com>**
    * **<https://api2.binance.com>**
    * **<https://api3.binance.com>**
    * **<https://api4.binance.com>**
  * The last 4 endpoints in the point above (`api1`-`api4`) might give better performance but have less stability. Please use whichever works best for your setup.
  * All endpoints return either a JSON object or array.
  * Data is returned in **ascending** order. Oldest first, newest last.
  * All time and timestamp related fields are in **milliseconds**.
  * The base endpoint **<https://data-api.binance.vision>** can be used to access the following API endpoints that have `NONE` as security type:
    * [GET /api/v3/aggTrades](/en/docs/products/margin-trading/general-info#compressed-aggregate-trades-list)
    * [GET /api/v3/avgPrice](/en/docs/products/margin-trading/general-info#current-average-price)
    * [GET /api/v3/depth](/en/docs/products/margin-trading/general-info#order-book)
    * [GET /api/v3/exchangeInfo](/en/docs/products/margin-trading/general-info#exchange-information)
    * [GET /api/v3/klines](/en/docs/products/margin-trading/general-info#kline-candlestick-data)
    * [GET /api/v3/ping](/en/docs/products/margin-trading/general-info#test-connectivity)
    * [GET /api/v3/ticker](/en/docs/products/margin-trading/general-info#rolling-window-price-change-statistics)
    * [GET /api/v3/ticker/24hr](/en/docs/products/margin-trading/general-info#24hr-ticker-price-change-statistics)
    * [GET /api/v3/ticker/bookTicker](/en/docs/products/margin-trading/general-info#symbol-order-book-ticker)
    * [GET /api/v3/ticker/price](/en/docs/products/margin-trading/general-info#symbol-price-ticker)
    * [GET /api/v3/time](/en/docs/products/margin-trading/general-info#check-server-time)
    * [GET /api/v3/trades](/en/docs/products/margin-trading/general-info#recent-trades-list)
    * [GET /api/v3/uiKlines](/en/docs/products/margin-trading/general-info#uiklines)



### HTTP Return Codes

  * HTTP `4XX` return codes are used for malformed requests; the issue is on the sender's side.

  * HTTP `403` return code is used when the WAF Limit (Web Application Firewall) has been violated.

  * HTTP `409` return code is used when a cancelReplace order partially succeeds. (e.g. if the cancellation of the order fails but the new order placement succeeds.)

  * HTTP `429` return code is used when breaking a request rate limit.

  * HTTP `418` return code is used when an IP has been auto-banned for continuing to send requests after receiving `429` codes.

  * HTTP `5XX` return codes are used for internal errors; the issue is on Binance's side.

If there is an error message "Unknown error, please check your request or try again later." with the error code -1000 returned in the response, the API successfully sent the request but not get a response within the timeout period.




​ It is important to NOT treat this as a failure operation; the execution status is UNKNOWN and could have been a success;

### Error Codes and Messages

  * If there is an error, the API will return an error with a message of the reason.



> The error payload on API and SAPI is as follows:
    
    
    Code
    
    {
      "code": -1121,
      "msg": "Invalid symbol."
    }

  * Specific error codes and messages defined in [Error Codes](/en/docs/products/margin-trading/general-info#error-codes).



### General Information on Endpoints

  * For `GET` endpoints, parameters must be sent as a `query string`.
  * For `POST`, `PUT`, and `DELETE` endpoints, the parameters may be sent as a `query string` or in the `request body` with content type `application/x-www-form-urlencoded`. You may mix parameters between both the `query string` and `request body` if you wish to do so.
  * Parameters may be sent in any order.
  * If a parameter sent in both the `query string` and `request body`, the `query string` parameter will be used.



* * *

## LIMITS

### General Info on Limits

  * The following `intervalLetter` values for headers:
    * SECOND => S
    * MINUTE => M
    * HOUR => H
    * DAY => D
  * `intervalNum` describes the amount of the interval. For example, `intervalNum` 5 with `intervalLetter` M means "Every 5 minutes".
  * The `/api/v3/exchangeInfo` `rateLimits` array contains objects related to the exchange's `RAW_REQUESTS`, `REQUEST_WEIGHT`, and `ORDERS` rate limits. These are further defined in the `ENUM definitions` section under `Rate limiters (rateLimitType)`.
  * A 429 will be returned when either request rate limit or order rate limit is violated.



### IP Limits

  * Every request will contain `X-MBX-USED-WEIGHT-(intervalNum)(intervalLetter)` in the response headers which has the current used weight for the IP for all request rate limiters defined.
  * Each route has a `weight` which determines for the number of requests each endpoint counts for. Heavier endpoints and endpoints that do operations on multiple symbols will have a heavier `weight`.
  * When a 429 is received, it's your obligation as an API to back off and not spam the API.
  * **Repeatedly violating rate limits and/or failing to back off after receiving 429s will result in an automated IP ban (HTTP status 418).**
  * IP bans are tracked and **scale in duration** for repeat offenders, **from 2 minutes to 3 days**.
  * A `Retry-After` header is sent with a 418 or 429 responses and will give the **number of seconds** required to wait, in the case of a 429, to prevent a ban, or, in the case of a 418, until the ban is over.
  * **The limits on the API are based on the IPs, not the API keys.**



### Order Rate Limits

  * Every successful order response will contain a `X-MBX-ORDER-COUNT-(intervalNum)(intervalLetter)` header which has the current order count for the account for all order rate limiters defined.

  * When the order count exceeds the limit, you will receive a 429 error without the `Retry-After` header. Please check the Order Rate Limit rules using `GET api/v3/exchangeInfo` and wait for reactivation accordingly.

  * Rejected/unsuccessful orders are not guaranteed to have `X-MBX-ORDER-COUNT-**` headers in the response.

  * **The order rate limit is counted against each account**.

  * To monitor order count usage, refer to GET `api/v3/rateLimit/order`




### Websocket Limits

  * WebSocket connections have a limit of 5 incoming messages per second. A message is considered:
    * A PING frame
    * A PONG frame
    * A JSON controlled message (e.g. subscribe, unsubscribe)
  * A connection that goes beyond the limit will be disconnected; IPs that are repeatedly disconnected may be banned.
  * A single connection can listen to a maximum of 1024 streams.
  * There is a limit of **300 connections per attempt every 5 minutes per IP**.



### /api/ and /sapi/ Limit Introduction

The `/api/*` and `/sapi/*` endpoints adopt either of two access limiting rules, IP limits or UID (account) limits.

  * Endpoints related to `/api/*`:

    * According to the two modes of IP and UID (account) limit, each are independent.
    * Endpoints share the 6000 per minute limit based on IP.
    * Responses contain the header `X-MBX-USED-WEIGHT-(intervalNum)(intervalLetter)`, defining the weight used by the current IP.
    * Successful order responses contain the header `X-MBX-ORDER-COUNT-(intervalNum)(intervalLetter)`, defining the order limit used by the UID.
  * Endpoints related to `/sapi/*`:

    * Endpoints are marked according to IP or UID limit and their corresponding weight value.
    * Each endpoint with IP limits has an independent 12000 per minute limit.
    * Each endpoint with UID limits has an independent 180000 per minute limit.
    * Responses from endpoints with IP limits contain the header `X-SAPI-USED-IP-WEIGHT-1M`, defining the weight used by the current IP.
    * Responses from endpoints with UID limits contain the header `X-SAPI-USED-UID-WEIGHT-1M`, defining the weight used by the current UID.



* * *

## Data Sources

  * The API system is asynchronous, so some delay in the response is normal and expected.
  * Each endpoint has a data source indicating where the data is being retrieved, and thus which endpoints have the most up-to-date response.



These are the three sources, ordered by which is has the most up-to-date response to the one with potential delays in updates.

  * **Matching Engine** \- the data is from the matching Engine
  * **Memory** \- the data is from a server's local or external memory
  * **Database** \- the data is taken directly from a database



## Endpoint security type

  * Each endpoint has a security type that determines how you will interact with it. This is stated next to the NAME of the endpoint.
    * If no security type is stated, assume the security type is NONE.
  * API-keys are passed into the Rest API via the `X-MBX-APIKEY` header.
  * API-keys and secret-keys **are case sensitive**.
  * API-keys can be configured to only access certain types of secure endpoints. For example, one API-key could be used for TRADE only, while another API-key can access everything except for TRADE routes.
  * By default, API-keys can access all secure routes.

Security Type| Description  
---|---  
NONE| Endpoint can be accessed freely.  
TRADE| Endpoint requires sending a valid API-Key and signature.  
MARGIN| Endpoint requires sending a valid API-Key and signature.  
USER_DATA| Endpoint requires sending a valid API-Key and signature.  
USER_STREAM| Endpoint requires sending a valid API-Key.  
MARKET_DATA| Endpoint requires sending a valid API-Key.  
  
  * `TRADE`, `MARGIN` and `USER_DATA` endpoints are `SIGNED` endpoints.



* * *

## SIGNED (TRADE, USER_DATA, AND MARGIN) Endpoint security

  * `SIGNED` endpoints require an additional parameter, `signature`, to be sent in the `query string` or `request body`.
  * Endpoints use `HMAC SHA256` signatures. The `HMAC SHA256 signature` is a keyed `HMAC SHA256` operation. Use your `secretKey` as the key and `totalParams` as the value for the HMAC operation.
  * The `signature` is **not case sensitive**.
  * `totalParams` is defined as the `query string` concatenated with the `request body`.



### Timing security

  * A `SIGNED` endpoint also requires a parameter, `timestamp`, to be sent which should be the millisecond timestamp of when the request was created and sent.
  * An additional parameter, `recvWindow`, may be sent to specify the number of milliseconds after `timestamp` the request is valid for. If `recvWindow` is not sent, **it defaults to 5000**.



> The logic is as follows:
    
    
    Code
    
    if (timestamp < serverTime + 1000 && serverTime - timestamp <= recvWindow) {
      // process request
    } else {
      // reject request
    }

**Serious trading is about timing.** Networks can be unstable and unreliable, which can lead to requests taking varying amounts of time to reach the servers. With `recvWindow`, you can specify that the request must be processed within a certain number of milliseconds or be rejected by the server.

### SIGNED Endpoint Examples for POST /api/v3/order - HMAC Keys

Here is a step-by-step example of how to send a vaild signed payload from the Linux command line using `echo`, `openssl`, and `curl`.

Key| Value  
---|---  
apiKey| vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A  
secretKey| NhqPtmdSJYdKjVHjA7PZj4Mge3R5YNiP1e3UZjInClVN65XAbvqqM6A7H5fATj0j  
Parameter| Value  
---|---  
symbol| LTCBTC  
side| BUY  
type| LIMIT  
timeInForce| GTC  
quantity| 1  
price| 0.1  
recvWindow| 5000  
timestamp| 1499827319559  
  
**Example 1: As a request body**

> **Example 1**

> **HMAC SHA256 signature:**
    
    
    Code
    
        $ echo -n "symbol=LTCBTC&side=BUY&type=LIMIT&timeInForce=GTC&quantity=1&price=0.1&recvWindow=5000&timestamp=1499827319559" | openssl dgst -sha256 -hmac "NhqPtmdSJYdKjVHjA7PZj4Mge3R5YNiP1e3UZjInClVN65XAbvqqM6A7H5fATj0j"
        (stdin)= c8db56825ae71d6d79447849e617115f4a920fa2acdcab2b053c4b2838bd6b71

> **curl command:**
    
    
    Code
    
        (HMAC SHA256)
        $ curl -H "X-MBX-APIKEY: vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A" -X POST 'https://api.binance.com/api/v3/order' -d 'symbol=LTCBTC&side=BUY&type=LIMIT&timeInForce=GTC&quantity=1&price=0.1&recvWindow=5000&timestamp=1499827319559&signature=c8db56825ae71d6d79447849e617115f4a920fa2acdcab2b053c4b2838bd6b71'
    

  * **requestBody:**



symbol=LTCBTC  
&side=BUY  
&type=LIMIT  
&timeInForce=GTC  
&quantity=1  
&price=0.1  
&recvWindow=5000  
&timestamp=1499827319559

**Example 2: As a query string**

> **Example 2**

> **HMAC SHA256 signature:**
    
    
    Code
    
        $ echo -n "symbol=LTCBTC&side=BUY&type=LIMIT&timeInForce=GTC&quantity=1&price=0.1&recvWindow=5000&timestamp=1499827319559" | openssl dgst -sha256 -hmac "NhqPtmdSJYdKjVHjA7PZj4Mge3R5YNiP1e3UZjInClVN65XAbvqqM6A7H5fATj0j"
        (stdin)= c8db56825ae71d6d79447849e617115f4a920fa2acdcab2b053c4b2838bd6b71
    

> **curl command:**
    
    
    Code
    
        (HMAC SHA256)
       $ curl -H "X-MBX-APIKEY: vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A" -X POST 'https://api.binance.com/api/v3/order?symbol=LTCBTC&side=BUY&type=LIMIT&timeInForce=GTC&quantity=1&price=0.1&recvWindow=5000&timestamp=1499827319559&signature=c8db56825ae71d6d79447849e617115f4a920fa2acdcab2b053c4b2838bd6b71'
    

  * **queryString:**



symbol=LTCBTC  
&side=BUY  
&type=LIMIT  
&timeInForce=GTC  
&quantity=1  
&price=0.1  
&recvWindow=5000  
&timestamp=1499827319559

**Example 3: Mixed query string and request body**

> **Example 3**

> **HMAC SHA256 signature:**
    
    
    Code
    
       $ echo -n "symbol=LTCBTC&side=BUY&type=LIMIT&timeInForce=GTCquantity=1&price=0.1&recvWindow=5000&timestamp=1499827319559" | openssl dgst -sha256 -hmac "NhqPtmdSJYdKjVHjA7PZj4Mge3R5YNiP1e3UZjInClVN65XAbvqqM6A7H5fATj0j"
        (stdin)= 0fd168b8ddb4876a0358a8d14d0c9f3da0e9b20c5d52b2a00fcf7d1c602f9a77
    

> **curl command:**
    
    
    Code
    
        (HMAC SHA256)
        $ curl -H "X-MBX-APIKEY: vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A" -X POST 'https://api.binance.com/api/v3/order?symbol=LTCBTC&side=BUY&type=LIMIT&timeInForce=GTC' -d 'quantity=1&price=0.1&recvWindow=5000&timestamp=1499827319559&signature=0fd168b8ddb4876a0358a8d14d0c9f3da0e9b20c5d52b2a00fcf7d1c602f9a77'

  * **queryString:**



symbol=LTCBTC&side=BUY&type=LIMIT&timeInForce=GTC

  * **requestBody:**



quantity=1&price=0.1&recvWindow=5000&timestamp=1499827319559

Note that the signature is different in example 3. There is no & between "GTC" and "quantity=1".

### SIGNED Endpoint Example for POST /api/v3/order - RSA Keys

  * This will be a step by step process how to create the signature payload to send a valid signed payload.
  * We support `PKCS#8` currently.
  * To get your API key, you need to upload your RSA Public Key to your account and a corresponding API key will be provided for you.



For this example, the private key will be referenced as `test-prv-key.pem`

Key| Value  
---|---  
apiKey| CAvIjXy3F44yW6Pou5k8Dy1swsYDWJZLeoK2r8G4cFDnE9nosRppc2eKc1T8TRTQ  
Parameter| Value  
---|---  
symbol| BTCUSDT  
side| SELL  
type| LIMIT  
timeInForce| GTC  
quantity| 1  
price| 0.2  
recvWindow| 5000  
timestamp| 1668481559918  
  
> **Signature payload (with the listed parameters):**
    
    
    Code
    
    symbol=BTCUSDT&side=SELL&type=LIMIT&timeInForce=GTC&quantity=1&price=0.2&timestamp=1668481559918&recvWindow=5000

**Step 1: Construct the payload**

Arrange the list of parameters into a string. Separate each parameter with a `&`.

**Step 2: Compute the signature:**

2.1 - Encode signature payload as ASCII data.

> **Step 2.2**
    
    
    Code
    
     $ echo -n 'symbol=BTCUSDT&side=SELL&type=LIMIT&timeInForce=GTC&quantity=1&price=0.2&timestamp=1668481559918&recvWindow=5000' | openssl dgst -sha256 -sign ./test-prv-key.pem

2.2 - Sign payload using RSASSA-PKCS1-v1_5 algorithm with SHA-256 hash function.

> **Step 2.3**
    
    
    Code
    
    $  echo -n 'symbol=BTCUSDT&side=SELL&type=LIMIT&timeInForce=GTC&quantity=1&price=0.2&timestamp=1668481559918&recvWindow=5000' | openssl dgst -sha256 -sign ./test-prv-key.pem | openssl enc -base64 -A
    HZ8HOjiJ1s/igS9JA+n7+7Ti/ihtkRF5BIWcPIEluJP6tlbFM/Bf44LfZka/iemtahZAZzcO9TnI5uaXh3++lrqtNonCwp6/245UFWkiW1elpgtVAmJPbogcAv6rSlokztAfWk296ZJXzRDYAtzGH0gq7CgSJKfH+XxaCmR0WcvlKjNQnp12/eKXJYO4tDap8UCBLuyxDnR7oJKLHQHJLP0r0EAVOOSIbrFang/1WOq+Jaq4Efc4XpnTgnwlBbWTmhWDR1pvS9iVEzcSYLHT/fNnMRxFc7u+j3qI//5yuGuu14KR0MuQKKCSpViieD+fIti46sxPTsjSemoUKp0oXA==

2.3 - Encode output as base64 string.

> **Step 2.4**
    
    
    Code
    
    HZ8HOjiJ1s%2FigS9JA%2Bn7%2B7Ti%2FihtkRF5BIWcPIEluJP6tlbFM%2FBf44LfZka%2FiemtahZAZzcO9TnI5uaXh3%2B%2BlrqtNonCwp6%2F245UFWkiW1elpgtVAmJPbogcAv6rSlokztAfWk296ZJXzRDYAtzGH0gq7CgSJKfH%2BXxaCmR0WcvlKjNQnp12%2FeKXJYO4tDap8UCBLuyxDnR7oJKLHQHJLP0r0EAVOOSIbrFang%2F1WOq%2BJaq4Efc4XpnTgnwlBbWTmhWDR1pvS9iVEzcSYLHT%2FfNnMRxFc7u%2Bj3qI%2F%2F5yuGuu14KR0MuQKKCSpViieD%2BfIti46sxPTsjSemoUKp0oXA%3D%3D

2.4 - Since the signature may contain `/` and `=`, this could cause issues with sending the request. So the signature has to be URL encoded.

> **Step 2.5**
    
    
    Code
    
     curl -H "X-MBX-APIKEY: CAvIjXy3F44yW6Pou5k8Dy1swsYDWJZLeoK2r8G4cFDnE9nosRppc2eKc1T8TRTQ" -X POST 'https://api.binance.com/api/v3/order?symbol=BTCUSDT&side=SELL&type=LIMIT&timeInForce=GTC&quantity=1&price=0.2&timestamp=1668481559918recvWindow=5000&signature=HZ8HOjiJ1s%2FigS9JA%2Bn7%2B7Ti%2FihtkRF5BIWcPIEluJP6tlbFM%2FBf44LfZka%2FiemtahZAZzcO9TnI5uaXh3%2B%2BlrqtNonCwp6%2F245UFWkiW1elpgtVAmJPbogcAv6rSlokztAfWk296ZJXzRDYAtzGH0gq7CgSJKfH%2BXxaCmR0WcvlKjNQnp12%2FeKXJYO4tDap8UCBLuyxDnR7oJKLHQHJLP0r0EAVOOSIbrFang%2F1WOq%2BJaq4Efc4XpnTgnwlBbWTmhWDR1pvS9iVEzcSYLHT%2FfNnMRxFc7u%2Bj3qI%2F%2F5yuGuu14KR0MuQKKCSpViieD%2BfIti46sxPTsjSemoUKp0oXA%3D%3D'

2.5 - curl command

> **Bash script**
    
    
    Code
    
    #!/usr/bin/env bash
    
    # Set up authentication:
    API_KEY="put your own API Key here"
    PRIVATE_KEY_PATH="test-prv-key.pem"
    
    # Set up the request:
    API_METHOD="POST"
    API_CALL="api/v3/order"
    API_PARAMS="symbol=BTCUSDT&side=SELL&type=LIMIT&timeInForce=GTC&quantity=1&price=0.2"
    
    # Sign the request:
    timestamp=$(date +%s000)
    api_params_with_timestamp="$API_PARAMS&timestamp=$timestamp"
    signature=$(echo -n "$api_params_with_timestamp" \
                | openssl dgst -sha256 -sign "$PRIVATE_KEY_PATH" \
                | openssl enc -base64 -A)
    
    # Send the request:
    curl -H "X-MBX-APIKEY: $API_KEY" -X "$API_METHOD" \
        "https://api.binance.com/$API_CALL?$api_params_with_timestamp" \
        --data-urlencode "signature=$signature"

A sample Bash script containing similar steps is available in the right side.

Was this page helpful?

Last modified on November 12, 2026

[Introduction](/en/docs/products/margin-trading/Introduction)[Change Log](/en/docs/products/margin-trading/change-log)

---

# 基本信息

## API 基本信息

  * 接口可能需要用户的 API Key，如何创建API-KEY请参考[这里](https://www.binance.com/cn/support/articles/360002502072)
  * 本篇列出接口的 base URL 有:
    * **<https://api.binance.com>**
    * **<https://api-gcp.binance.com>**
    * **<https://api1.binance.com>**
    * **<https://api2.binance.com>**
    * **<https://api3.binance.com>**
    * **<https://api4.binance.com>**
  * 上述列表的最后4个接口 (`api1`-`api4`) 可能会提供更好的性能，但其稳定性略为逊色。因此，请务必使用最适合您现有配置的那款。
  * 所有接口的响应都是 JSON 格式。
  * 响应中如有数组，数组元素以时间**升序** 排列，越早的数据越提前。
  * 所有时间、时间戳均为UNIX时间，单位为**毫秒** 。
  * 对于仅发送公开市场数据的 API，您可以使用 base URL <https://data-api.binance.vision> 。
    * GET /api/v3/aggTrades
    * GET /api/v3/avgPrice
    * GET /api/v3/depth
    * GET /api/v3/exchangeInfo
    * GET /api/v3/klines
    * GET /api/v3/ping
    * GET /api/v3/ticker
    * GET /api/v3/ticker/24hr
    * GET /api/v3/ticker/bookTicker
    * GET /api/v3/ticker/price
    * GET /api/v3/time
    * GET /api/v3/trades
    * GET /api/v3/uiKlines



### HTTP 返回代码

  * HTTP `4XX` 错误码用于指示错误的请求内容、行为、格式。问题在于请求者。

  * HTTP `403` 错误码表示违反WAF限制(Web应用程序防火墙)。

  * HTTP `409` 错误码表示重新下单(cancelReplace)的请求部分成功。(比如取消订单失败，但是下单成功了)

  * HTTP `429` 错误码表示警告访问频次超限，即将被封IP。

  * HTTP `418` 表示收到429后继续访问，于是被封了。

  * HTTP `5XX` 错误码用于指示Binance服务侧的问题。

如果返回内容里包含了报错信息 **"Unknown error, please check your request or try again later."及错误代码 -1000** ，则表示API服务端已经向业务核心提交了请求但未能获取响应，特别需要注意的是其不代表请求失败，而是未知。很可能已经得到了执行，也有可能执行失败，需要做进一步确认。




### 接口错误代码

  * 使用接口 `/api/v3`, 以及 `/sapi/v1/margin`时, 每个接口都有可能抛出异常;



> API 与 SAPI 的错误代码返回形式如下:
    
    
    Code
    
    {
      "code": -1121,
      "msg": "Invalid symbol."
    }

  * 具体的错误码及其解释在 [错误代码](/zh-CN/docs/products/margin-trading/general-info#cf68bca02a).



### 接口的基本信息

  * `GET` 方法的接口, 参数必须在 `query string`中发送。
  * `POST`, `PUT`, 和 `DELETE` 方法的接口,参数可以在内容形式为`application/x-www-form-urlencoded`的 `query string` 中发送，也可以在 `request body` 中发送。 如果你喜欢，也可以混合这两种方式发送参数。
  * 对参数的顺序不做要求。
  * 但如果同一个参数名在query string和request body中都有，query string中的会被优先采用。



* * *

## 访问限制

### 访问限制基本信息

  * 以下 是`intervalLetter` 作为头部值:

    * SECOND => S
    * MINUTE => M
    * HOUR => H
    * DAY => D
  * 在 `/api/v3/exchangeInfo` `rateLimits` 数组中包含与交易的有关RAW_REQUESTS，REQUEST_WEIGHT和ORDERS速率限制相关的对象。这些在 `限制种类 (rateLimitType)` 下的 `枚举定义` 部分中进一步定义。

  * 违反任何一个速率限制时（访问频次限制或下单速率限制），将返回429。




### IP 访问限制

  * 每个请求将包含一个`X-MBX-USED-WEIGHT-(intervalNum)(intervalLetter)`的头，其中包含当前IP所有请求的已使用权重。
  * 每一个接口均有一个相应的权重(weight)，有的接口根据参数不同可能拥有不同的权重。越消耗资源的接口权重就会越大。
  * 收到429时，您有责任停止发送请求，不得滥用API。
  * **收到429后仍然继续违反访问限制，会被封禁IP，并收到418错误码**
  * 频繁违反限制，封禁时间会逐渐延长，**从最短2分钟到最长3天** 。
  * `Retry-After`的头会与带有418或429的响应发送，并且会给出**以秒为单位** 的等待时长(如果是429)以防止禁令，或者如果是418，直到禁令结束。
  * **访问限制是基于IP的，而不是API Key**



###下单频率限制

  * 每个成功的下单回报将包含一个`X-MBX-ORDER-COUNT-(intervalNum)(intervalLetter)`的头，其中包含当前账户已用的下单限制数量。
  * 当下单数超过限制时，会收到带有429但不含`Retry-After`头的响应。请检查 `GET api/v3/exchangeInfo` 的下单频率限制 (rateLimitType = ORDERS) 并等待封禁时间结束。
  * 被拒绝或不成功的下单并不保证回报中包含以上头内容。
  * **下单频率限制是基于每个账户计数的。**
  * 用户可以通过接口 `GET api/v3/rateLimit/order` 来查询当前的下单量.



### WEB SOCKET 连接限制

  * Websocket服务器每秒最多接受5个消息。消息包括:
    * PING帧
    * PONG帧
    * JSON格式的消息, 比如订阅, 断开订阅.
  * 如果用户发送的消息超过限制，连接会被断开连接。反复被断开连接的IP有可能被服务器屏蔽。
  * 单个连接最多可以订阅 **1024** 个Streams。
  * 每IP地址、每5分钟最多可以发送300次连接请求。



### /api/ 与 /sapi/ 接口限频说明

`/api/*`接口和 `/sapi/*`接口采用两套不同的访问限频规则, 两者互相独立。

  * `/api/*`的接口相关：

    * 按IP和按UID(account)两种模式分别统计, 两者互相独立。
    * 以 `/api/*`开头的接口按IP限频，**且所有接口共用每分钟6,000限制** 。
    * 每个请求将包含一个 `X-MBX-USED-WEIGHT-(intervalNum)(intervalLetter)`的头，包含当前IP所有请求的已使用权重。
    * 每个成功的下单回报将包含一个`X-MBX-ORDER-COUNT-(intervalNum)(intervalLetter)`的头，其中包含当前账户已用的下单限制数量。
  * `/sapi/*`的接口相关：

    * 按IP和按UID(account)两种模式分别统计, 两者互相独立。
    * 以`/sapi/*`开头的接口采用**单接口限频模式** 。按IP统计的权重单接口权重总额为每分钟12000；按照UID统计的单接口权重总额是每分钟180000。
    * 每个接口会标明是按照IP或者按照UID统计, 以及相应请求一次的权重值。
    * 按照IP统计的接口, 请求返回头里面会包含`X-SAPI-USED-IP-WEIGHT-1M=<value>`或`X-SAPI-USED-IP-WEIGHT-1S=<value>`, 包含当前IP所有请求已使用权重。
    * 按照UID统计的接口, 请求返回头里面会包含`X-SAPI-USED-UID-WEIGHT-1M=<value>`或`X-SAPI-USED-UID-WEIGHT-1S=<value>`, 包含当前账户所有已用的UID权重。



* * *

## 数据来源

  * 因为API系统是异步的, 所以返回的数据有延时很正常, 也在预期之中。
  * 在每个接口中，列出了其数据的来源，可以用于理解数据的时效性。



系统一共有3个数据来源，按照更新速度的先后排序。排在前面的数据最新，在后面就有可能存在延迟。

  * **撮合引擎** \- 表示数据来源于撮合引擎
  * **缓存** \- 表示数据来源于内部或者外部的缓存
  * **数据库** \- 表示数据直接来源于数据库



* * *

## 接口鉴权类型

  * 每个接口都有自己的鉴权类型，鉴权类型决定了访问时应当进行何种鉴权。
  * 鉴权类型会在本文档中各个接口名称旁声明，如果没有特殊声明即默认为 `NONE`。
  * 如果需要 API-keys，应当在HTTP头中以 `X-MBX-APIKEY`字段传递。
  * API-keys 与 secret-keys **是大小写敏感的** 。
  * API-keys可以被配置为只拥有访问一些接口的权限。例如, 一个 API-key 仅可用于发送交易指令, 而另一个 API-key 则可访问除交易指令外的所有路径。
  * 默认 API-keys 可访问所有鉴权路径.

鉴权类型| 描述  
---|---  
NONE| 不需要鉴权的接口  
TRADE| 需要有效的 API-Key 和签名  
MARGIN| 需要有效的 API-Key 和签名  
USER_DATA| 需要有效的 API-Key 和签名  
USER_STREAM| 需要有效的 API-Key  
MARKET_DATA| 需要有效的 API-Key  
  
  * `TRADE`, `MARGIN` 和`USER_DATA` 接口是 签名(SIGNED)接口.



* * *

## SIGNED (TRADE、USER_DATA AND MARGIN) Endpoint security

  * 调用`SIGNED` 接口时，除了接口本身所需的参数外，还需要在`query string` 或 `request body`中传递 `signature`, 即签名参数。
  * `签名` **大小写不敏感**.
  * 各种签名方式(比如 HMAC, RSA, Ed25519)，请参考下面的签名的示例。



### 时间同步安全

  * 签名接口均需要传递 `timestamp`参数，其值应当是请求发送时刻的unix时间戳(毫秒)。
  * 服务器收到请求时会判断请求中的时间戳，如果是5000毫秒之前发出的，则请求会被认为无效。这个时间空窗值可以通过发送可选参数 `recvWindow`来定义。



> 逻辑伪代码如下:
    
    
    Code
    
    if (timestamp < serverTime + 1000 && serverTime - timestamp <= recvWindow) {
      // process request
    } else {
      // reject request
    }

**关于交易时效性** 互联网状况并不完全稳定可靠,因此你的程序本地到币安服务器的时延会有抖动。这是我们设置`recvWindow`的目的所在，如果你从事高频交易，对交易时效性有较高的要求，可以灵活设置`recvWindow`以达到你的要求。

### POST /api/v3/order 的示例 - HMAC Keys

以下是在 linux bash 环境下使用 echo openssl 和 curl 工具实现的一个调用接口下单的示例 apikey、secret仅供示范

Key| Value  
---|---  
apiKey| vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A  
secretKey| NhqPtmdSJYdKjVHjA7PZj4Mge3R5YNiP1e3UZjInClVN65XAbvqqM6A7H5fATj0j  
参数| 取值  
---|---  
symbol| LTCBTC  
side| BUY  
type| LIMIT  
timeInForce| GTC  
quantity| 1  
price| 0.1  
recvWindow| 5000  
timestamp| 1499827319559  
  
**示例 1: 所有参数通过 request body 发送**

> **示例 1**

> **HMAC SHA256 signature:**
    
    
    Code
    
        $ echo -n "symbol=LTCBTC&side=BUY&type=LIMIT&timeInForce=GTC&quantity=1&price=0.1&recvWindow=5000&timestamp=1499827319559" | openssl dgst -sha256 -hmac "NhqPtmdSJYdKjVHjA7PZj4Mge3R5YNiP1e3UZjInClVN65XAbvqqM6A7H5fATj0j"
        (stdin)= c8db56825ae71d6d79447849e617115f4a920fa2acdcab2b053c4b2838bd6b71

> **curl command:**
    
    
    Code
    
        (HMAC SHA256)
        $ curl -H "X-MBX-APIKEY: vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A" -X POST 'https://api.binance.com/api/v3/order' -d 'symbol=LTCBTC&side=BUY&type=LIMIT&timeInForce=GTC&quantity=1&price=0.1&recvWindow=5000&timestamp=1499827319559&signature=c8db56825ae71d6d79447849e617115f4a920fa2acdcab2b053c4b2838bd6b71'
    

  * **requestBody:**



symbol=LTCBTC  
&side=BUY  
&type=LIMIT  
&timeInForce=GTC  
&quantity=1  
&price=0.1  
&recvWindow=5000  
&timestamp=1499827319559

**示例 2: 所有参数通过 query string 发送**

> **示例 2**

> **HMAC SHA256 signature:**
    
    
    Code
    
        $ echo -n "symbol=LTCBTC&side=BUY&type=LIMIT&timeInForce=GTC&quantity=1&price=0.1&recvWindow=5000&timestamp=1499827319559" | openssl dgst -sha256 -hmac "NhqPtmdSJYdKjVHjA7PZj4Mge3R5YNiP1e3UZjInClVN65XAbvqqM6A7H5fATj0j"
        (stdin)= c8db56825ae71d6d79447849e617115f4a920fa2acdcab2b053c4b2838bd6b71
    

> **curl command:**
    
    
    Code
    
        (HMAC SHA256)
       $ curl -H "X-MBX-APIKEY: vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A" -X POST 'https://api.binance.com/api/v3/order?symbol=LTCBTC&side=BUY&type=LIMIT&timeInForce=GTC&quantity=1&price=0.1&recvWindow=5000&timestamp=1499827319559&signature=c8db56825ae71d6d79447849e617115f4a920fa2acdcab2b053c4b2838bd6b71'
    

  * **queryString:**



symbol=LTCBTC  
&side=BUY  
&type=LIMIT  
&timeInForce=GTC  
&quantity=1  
&price=0.1  
&recvWindow=5000  
&timestamp=1499827319559

**示例 3: 混合使用 query string 和 request body**

> **示例 3**

> **HMAC SHA256 signature:**
    
    
    Code
    
       $ echo -n "symbol=LTCBTC&side=BUY&type=LIMIT&timeInForce=GTCquantity=1&price=0.1&recvWindow=5000&timestamp=1499827319559" | openssl dgst -sha256 -hmac "NhqPtmdSJYdKjVHjA7PZj4Mge3R5YNiP1e3UZjInClVN65XAbvqqM6A7H5fATj0j"
        (stdin)= 0fd168b8ddb4876a0358a8d14d0c9f3da0e9b20c5d52b2a00fcf7d1c602f9a77
    

> **curl command:**
    
    
    Code
    
        (HMAC SHA256)
        $ curl -H "X-MBX-APIKEY: vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A" -X POST 'https://api.binance.com/api/v3/order?symbol=LTCBTC&side=BUY&type=LIMIT&timeInForce=GTC' -d 'quantity=1&price=0.1&recvWindow=5000&timestamp=1499827319559&signature=0fd168b8ddb4876a0358a8d14d0c9f3da0e9b20c5d52b2a00fcf7d1c602f9a77'

  * **queryString:**



symbol=LTCBTC&side=BUY&type=LIMIT&timeInForce=GTC

  * **requestBody:**



quantity=1&price=0.1&recvWindow=5000&timestamp=1499827319559

请注意，签名与示例3不同。"GTC"和"quantity = 1"之间没有＆。

### POST /api/v3/order 的示例 - RSA Keys

  * 这将逐步介绍如何通过有效的签名发送 payload。
  * 我们接受 `PKCS#8` 格式的 RSA Key。
  * 要获取 API Key，您需要在您的账户上上传您的 RSA Public Key。



对于这个例子，Private Key 将被引用为`test-prv-key.pem`。

Key| Value  
---|---  
apiKey| CAvIjXy3F44yW6Pou5k8Dy1swsYDWJZLeoK2r8G4cFDnE9nosRppc2eKc1T8TRTQ  
参数| 取值  
---|---  
symbol| BTCUSDT  
side| SELL  
type| LIMIT  
timeInForce| GTC  
quantity| 1  
price| 0.2  
recvWindow| 5000  
timestamp| 1668481559918  
  
> **有列出参数的签名 payload：**
    
    
    Code
    
    symbol=BTCUSDT&side=SELL&type=LIMIT&timeInForce=GTC&quantity=1&price=0.2&timestamp=1668481559918&recvWindow=5000

**第1步: Payload**

将参数列表排列成一个 string。 用 `&` 分隔每个参数。对于上述参数，签名 payload 如右所示。

**第2步: 计算签名**

2.1 - 将签名有效负载编码为 ASCII 数据。

> **第2.2步**
    
    
    Code
    
     $ echo -n 'symbol=BTCUSDT&side=SELL&type=LIMIT&timeInForce=GTC&quantity=1&price=0.2&timestamp=1668481559918&recvWindow=5000' | openssl dgst -sha256 -sign ./test-prv-key.pem

2.2 - 使用带有 SHA-256 hash 函数的 RSASSA-PKCS1-v1_5 算法对 payload 进行签名。

> **第2.3步**
    
    
    Code
    
    $ echo -n 'symbol=BTCUSDT&side=SELL&type=LIMIT&timeInForce=GTC&quantity=1&price=0.2&timestamp=1668481559918&recvWindow=5000' | openssl dgst -sha256 -sign ./test-prv-key.pem | openssl enc -base64 -A
    HZ8HOjiJ1s/igS9JA+n7+7Ti/ihtkRF5BIWcPIEluJP6tlbFM/Bf44LfZka/iemtahZAZzcO9TnI5uaXh3++lrqtNonCwp6/245UFWkiW1elpgtVAmJPbogcAv6rSlokztAfWk296ZJXzRDYAtzGH0gq7CgSJKfH+XxaCmR0WcvlKjNQnp12/eKXJYO4tDap8UCBLuyxDnR7oJKLHQHJLP0r0EAVOOSIbrFang/1WOq+Jaq4Efc4XpnTgnwlBbWTmhWDR1pvS9iVEzcSYLHT/fNnMRxFc7u+j3qI//5yuGuu14KR0MuQKKCSpViieD+fIti46sxPTsjSemoUKp0oXA==

2.3 - 将输出编码为 base64 string。

> **第2.4步**
    
    
    Code
    
    HZ8HOjiJ1s%2FigS9JA%2Bn7%2B7Ti%2FihtkRF5BIWcPIEluJP6tlbFM%2FBf44LfZka%2FiemtahZAZzcO9TnI5uaXh3%2B%2BlrqtNonCwp6%2F245UFWkiW1elpgtVAmJPbogcAv6rSlokztAfWk296ZJXzRDYAtzGH0gq7CgSJKfH%2BXxaCmR0WcvlKjNQnp12%2FeKXJYO4tDap8UCBLuyxDnR7oJKLHQHJLP0r0EAVOOSIbrFang%2F1WOq%2BJaq4Efc4XpnTgnwlBbWTmhWDR1pvS9iVEzcSYLHT%2FfNnMRxFc7u%2Bj3qI%2F%2F5yuGuu14KR0MuQKKCSpViieD%2BfIti46sxPTsjSemoUKp0oXA%3D%3D

2.4 - 由于签名可能包含 `/` 和 `=`，这可能会导致发送请求时出现问题。 所以签名必须是 URL 编码的。

> **第2.5步**
    
    
    Code
    
     curl -H "X-MBX-APIKEY: CAvIjXy3F44yW6Pou5k8Dy1swsYDWJZLeoK2r8G4cFDnE9nosRppc2eKc1T8TRTQ" -X POST 'https://api.binance.com/api/v3/order?symbol=BTCUSDT&side=SELL&type=LIMIT&timeInForce=GTC&quantity=1&price=0.2&timestamp=1668481559918&recvWindow=5000&signature=HZ8HOjiJ1s%2FigS9JA%2Bn7%2B7Ti%2FihtkRF5BIWcPIEluJP6tlbFM%2FBf44LfZka%2FiemtahZAZzcO9TnI5uaXh3%2B%2BlrqtNonCwp6%2F245UFWkiW1elpgtVAmJPbogcAv6rSlokztAfWk296ZJXzRDYAtzGH0gq7CgSJKfH%2BXxaCmR0WcvlKjNQnp12%2FeKXJYO4tDap8UCBLuyxDnR7oJKLHQHJLP0r0EAVOOSIbrFang%2F1WOq%2BJaq4Efc4XpnTgnwlBbWTmhWDR1pvS9iVEzcSYLHT%2FfNnMRxFc7u%2Bj3qI%2F%2F5yuGuu14KR0MuQKKCSpViieD%2BfIti46sxPTsjSemoUKp0oXA%3D%3D'

2.5 - curl 命令

> **Bash 脚本**
    
    
    Code
    
    #!/usr/bin/env bash
    
    # 设置身份验证：
    API_KEY="替换成您的 API Key"
    PRIVATE_KEY_PATH="test-prv-key.pem"
    
    # 设置您的请求:
    API_METHOD="POST"
    API_CALL="api/v3/order"
    API_PARAMS="symbol=BTCUSDT&side=SELL&type=LIMIT&timeInForce=GTC&quantity=1&price=0.2"
    
    # 计算签名：
    timestamp=$(date +%s000)
    api_params_with_timestamp="$API_PARAMS&timestamp=$timestamp"
    signature=$(echo -n "$api_params_with_timestamp" \
                | openssl dgst -sha256 -sign "$PRIVATE_KEY_PATH" \
                | openssl enc -base64 -A)
    
    # 发送请求：
    curl -H "X-MBX-APIKEY: $API_KEY" -X "$API_METHOD" \
        "https://api.binance.com/$API_CALL?$api_params_with_timestamp" \
        --data-urlencode "signature=$signature"

右边有示例 Bash 脚本执行上述类似的步骤.

### POST /api/v3/order 的示例 - Ed25519 Keys

参数| 取值  
---|---  
symbol| BTCUSDT  
side| SELL  
type| LIMIT  
timeInForce| GTC  
quantity| 1  
price| 0.2  
timestamp| 1668481559918  
  
> **Python 脚本**
    
    
    Code
    
    #!/usr/bin/env python3
    import base64
    import requests
    import time
    from cryptography.hazmat.primitives.serialization import load_pem_private_key
    # 设置身份验证：
    API_KEY='替换成您的 API Key'
    PRIVATE_KEY_PATH='test-prv-key.pem'
    # 加载 private key。
    # 在这个例子中，private key 没有加密，但我们建议使用强密码以提高安全性。
    with open(PRIVATE_KEY_PATH, 'rb') as f:
        private_key = load_pem_private_key(data=f.read(), password=None)
    # 设置请求参数：
    params = {
        'symbol':       'BTCUSDT',
        'side':         'SELL',
        'type':         'LIMIT',
        'timeInForce':  'GTC',
        'quantity':     '1.0000000',
        'price':        '0.20',
    }
    # 参数中加时间戳：
    timestamp = int(time.time() * 1000) # 以毫秒为单位的 UNIX 时间戳
    params['timestamp'] = timestamp
    # 参数中加签名：
    payload = '&'.join([f'{param}={value}' for param, value in params.items()])
    signature = base64.b64encode(private_key.sign(payload.encode('ASCII')))
    params['signature'] = signature
    # 发送请求：
    headers = {
        'X-MBX-APIKEY': API_KEY,
    }
    response = requests.post(
        'https://api.binance.com/api/v3/order',
        headers=headers,
        data=params,
    )
    print(response.json())

右边有 Python 脚本来示例如何使用 Ed25519 key 签名。

此页面是否有帮助？

Last modified on November 12, 2026

[概述](/zh-CN/docs/products/margin-trading/Introduction)[更新日志](/zh-CN/docs/products/margin-trading/change-log)