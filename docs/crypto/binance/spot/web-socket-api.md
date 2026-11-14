---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/spot/web-socket-api
api_type: WebSocket
updated_at: 2026-11-13 20:27:24.364797
---

# General WebSocket API Information

## General API Information

  * The base endpoint is: **`wss://ws-api.binance.com:443/ws-api/v3`**.
    * If you experience issues with the standard 443 port, alternative port 9443 is also available.
    * The base endpoint for [testnet](https://testnet.binance.vision/) is: `wss://ws-api.testnet.binance.vision/ws-api/v3`
  * A single connection to the API is only valid for 24 hours; expect to be disconnected after the 24-hour mark.
  * A [`serverShutdown`](/en/docs/products/spot/web-socket-api#server-shutdown) event will be sent when the server is about to shutdown, resulting in disconnection. Please establish a new connection as soon as possible to prevent interruption.
  * We support HMAC, RSA, and Ed25519 keys. For more information, please see [API Key types](/en/docs/products/spot/faqs/api_key_types).
  * Responses are in JSON by default. To receive responses in SBE, refer to the [SBE FAQ](/en/docs/products/spot/faqs/sbe_faq) page.
  * If your request contains a symbol name containing non-ASCII characters, then the response may contain non-ASCII characters encoded in UTF-8.
  * Some methods may return asset and/or symbol names containing non-ASCII characters encoded in UTF-8 even if the request did not contain non-ASCII characters.
  * The WebSocket server will send a `ping frame` every 20 seconds.
    * If the WebSocket server does not receive a `pong frame` back from the connection within a minute the connection will be disconnected.
    * When you receive a ping, you must send a pong with a copy of ping's payload as soon as possible.
    * Unsolicited `pong frames` are allowed, but will not prevent disconnection. **It is recommended that the payload for these pong frames are empty.**
  * Data is returned in **chronological order** , unless noted otherwise.
    * Without `startTime` or `endTime`, returns the most recent items up to the limit.
    * With `startTime`, returns oldest items from `startTime` up to the limit.
    * With `endTime`, returns most recent items up to `endTime` and the limit.
    * With both, behaves like `startTime` but does not exceed `endTime`.
  * All timestamps in the JSON responses are in **milliseconds in UTC by default**. To receive the information in microseconds, please add the parameter `timeUnit=MICROSECOND` or `timeUnit=microsecond` in the URL.
  * Timestamp parameters (e.g. `startTime`, `endTime`, `timestamp`) can be passed in milliseconds or microseconds.
  * All field names and values are **case-sensitive** , unless noted otherwise.
  * If there are enums or terms you want clarification on, please see [SPOT Glossary](/en/docs/products/spot/faqs/spot_glossary) for more information.
  * APIs have a timeout of 10 seconds when processing a request. If a response from the Matching Engine takes longer than this, the API responds with "Timeout waiting for response from backend server. Send status unknown; execution status unknown." [(-1007 TIMEOUT)](/en/docs/products/spot/errors#-1007-timeout)
    * This does not always mean that the request failed in the Matching Engine.
    * If the status of the request has not appeared in [User Data Stream](/en/docs/products/spot/user-data-stream), please perform an API query for its status.
  * **Please avoid SQL keywords in requests** as they may trigger a security block by a WAF (Web Application Firewall) rule. See <https://www.binance.com/en/support/faq/detail/360004492232> for more details.



## Request format

Requests must be sent as JSON in **text frames** , one request per frame.

Example of request:
    
    
    Code
    
    {
      "id": "e2a85d9f-07a5-4f94-8d5f-789dc3deb097",
      "method": "order.place",
      "params": {
        "symbol": "BTCUSDT",
        "side": "BUY",
        "type": "LIMIT",
        "price": "0.1",
        "quantity": "10",
        "timeInForce": "GTC",
        "timestamp": 1655716096498,
        "apiKey": "T59MTDLWlpRW16JVeZ2Nju5A5C98WkMm8CSzWC4oqynUlTm1zXOxyauT8LmwXEv9",
        "signature": "5942ad337e6779f2f4c62cd1c26dba71c91514400a24990a3e7f5edec9323f90"
      }
    }

Request fields:

Name| Type| Mandatory| Description  
---|---|---|---  
`id`| INT / STRING / `null`| YES| Arbitrary ID used to match responses to requests  
`method`| STRING| YES| Request method name  
`params`| OBJECT| NO| Request parameters. May be omitted if there are no parameters  
  
  * Request `id` is truly arbitrary. You can use UUIDs, sequential IDs, current timestamp, etc. The server does not interpret `id` in any way, simply echoing it back in the response.

You can freely reuse IDs within a session. However, be careful to not send more than one request at a time with the same ID, since otherwise it might be impossible to tell the responses apart.

  * Request method names may be prefixed with explicit version: e.g., `"v3/order.place"`.

  * The order of `params` is not significant.




## Response format

Responses are returned as JSON in **text frames** , one response per frame.

Example of successful response:
    
    
    Code
    
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

Example of failed response:
    
    
    Code
    
    {
      "id": "e2a85d9f-07a5-4f94-8d5f-789dc3deb097",
      "status": 400,
      "error": {
        "code": -2010,
        "msg": "Account has insufficient balance for requested action."
      },
      "rateLimits": [
        {
          "rateLimitType": "ORDERS",
          "interval": "SECOND",
          "intervalNum": 10,
          "limit": 50,
          "count": 13
        },
        {
          "rateLimitType": "ORDERS",
          "interval": "DAY",
          "intervalNum": 1,
          "limit": 160000,
          "count": 4044
        },
        {
          "rateLimitType": "REQUEST_WEIGHT",
          "interval": "MINUTE",
          "intervalNum": 1,
          "limit": 6000,
          "count": 322
        }
      ]
    }

Response fields:

### Status codes

Status codes in the `status` field are the same as in HTTP.

Here are some common status codes that you might encounter:

  * `200` indicates a successful response.
  * `4XX` status codes indicate invalid requests; the issue is on your side.
    * `400` – your request failed, see `error` for the reason.
    * `403` – you have been blocked by the Web Application Firewall. This can indicate a rate limit violation or a security block. See <https://www.binance.com/en/support/faq/detail/360004492232> for more details.
    * `409` – your request partially failed but also partially succeeded, see `error` for details.
    * `418` – you have been auto-banned for repeated violation of rate limits.
    * `429` – you have exceeded API request rate limit, please slow down.
  * `5XX` status codes indicate internal errors; the issue is on Binance's side.
    * **Important:** If a response contains 5xx status code, it **does not** necessarily mean that your request has failed. Execution status is _unknown_ and the request might have actually succeeded. Please use query methods to confirm the status. You might also want to establish a new WebSocket connection for that.



See [Error codes for Binance](/en/docs/products/spot/errors) for a list of error codes and messages.

## Conditional fields in Order Responses

There are fields in the order responses (e.g. order placement, order query, order cancellation) that appear only if certain conditions are met.

These fields can apply to order lists.

The fields are listed below:

Field| Description| Visibility conditions| Examples  
---|---|---|---  
`icebergQty`| Quantity for the iceberg order| Appears only if the parameter `icebergQty` was sent in the request.| `"icebergQty": "0.00000000"`  
`quoteNotionalLimit`| Maximum quote-asset notional the order may consume| Appears only if the order was placed with a quote notional limit.| `"quoteNotionalLimit": "250.00000000"`  
`preventedMatchId`| When used in combination with `symbol`, can be used to query a prevented match.| Appears only if the order expired due to STP.| `"preventedMatchId": 0`  
`preventedQuantity`| Order quantity that expired due to STP| Appears only if the order expired due to STP.| `"preventedQuantity": "1.200000"`  
`effectiveSelfTradePreventionMode`| Self-trade-prevention mode the engine actually applied. Values: `EXPIRE_MAKER`, `EXPIRE_BOTH`, `DECREMENT`.| Appears only inside `preventedMatches[]` entries of `FULL` order responses, when the applied STP mode differs from the order's `selfTradePreventionMode`.| `"effectiveSelfTradePreventionMode": "DECREMENT"`  
`stopPrice`| Price when the algorithmic order will be triggered| Appears for `STOP_LOSS`. `TAKE_PROFIT`, `STOP_LOSS_LIMIT` and `TAKE_PROFIT_LIMIT` orders.| `"stopPrice": "23500.00000000"`  
`strategyId`| Can be used to label an order that's part of an order strategy.| Appears if the parameter was populated in the request.| `"strategyId": 37463720`  
`strategyType`| Can be used to label an order that is using an order strategy.| Appears if the parameter was populated in the request.| `"strategyType": 1000000`  
`trailingDelta`| Delta price change required before order activation| Appears for Trailing Stop Orders.| `"trailingDelta": 10`  
`trailingTime`| Time when the trailing order is now active and tracking price changes| Appears only for Trailing Stop Orders.| `"trailingTime": -1`  
`usedSor`| Field that determines whether order used SOR| Appears when placing orders using SOR| `"usedSor": true`  
`workingFloor`| Field that determines whether the order is being filled by the SOR or by the order book the order was submitted to.| Appears when placing orders using SOR| `"workingFloor": "SOR"`  
`pegPriceType`| Price peg type| Only for pegged orders| `"pegPriceType": "PRIMARY_PEG"`  
`pegOffsetType`| Price peg offset type| Only for pegged orders, if requested| `"pegOffsetType": "PRICE_LEVEL"`  
`pegOffsetValue`| Price peg offset value| Only for pegged orders, if requested| `"pegOffsetValue": 5`  
`peggedPrice`| Current price order is pegged at| Only for pegged orders, once determined| `"peggedPrice": "87523.83710000"`  
`expiryReason`| Cause of the order’s expiration| When an order has expired| `"expiryReason": "INSUFFICIENT_LIQUIDITY"`  
  
## Event format

[User Data Stream](/en/docs/products/spot/user-data-stream) events for non-SBE sessions are sent as JSON in **text frames** , one event per frame.

Events in [SBE sessions](/en/docs/products/spot/faqs/sbe_faq) will be sent as **binary frames**.

Please refer to [`userDataStream.subscribe`](/en/docs/catalog/core-trading-spot-trading/api/ws-api/user-data-stream#user-data-stream-subscribe) for details on how to subscribe to User Data Stream in WebSocket API.

Example of an event:
    
    
    Code
    
    {
        "subscriptionId": 0,
        "event": {
            "e": "outboundAccountPosition",
            "E": 1728972148778,
            "u": 1728972148778,
            "B": [
                {
                    "a": "BTC",
                    "f": "11818.00000000",
                    "l": "182.00000000"
                },
                {
                    "a": "USDT",
                    "f": "10580.00000000",
                    "l": "70.00000000"
                }
            ]
        }
    }

Event fields:

Name| Type| Mandatory| Description  
---|---|---|---  
`event`| OBJECT| YES| Event payload. See [User Data Streams](/en/docs/products/spot/user-data-stream)  
`subscriptionId`| INT| NO| Identifies which subscription the event is coming from. See [User Data Stream subscriptions](/en/docs/products/spot/user-data-stream#general-information)  
  
## Connection events

### Server Shutdown

`serverShutdown` event is sent when the server is about to shut down.
    
    
    Code
    
    {
      "event": {
        "e": "serverShutdown", // Event Type
        "E": 1770123456789,    // Event Time
        "T": 1770124000000     // Upcoming shutdown time
      }
    }

The `T` field indicates when the WebSocket session will be shut down.

In SBE sessions, the `T` field is only present in [SBE schema 3:6](/en/docs/products/spot/sbe/schemas/) and later.

Please establish a new connection as soon as possible to prevent interruption.

## Rate limits

### Connection limits

There is a limit of **300 connections per attempt every 5 minutes**.

The connection is per **IP address**.

### General information on rate limits

  * Current API rate limits can be queried using the [`exchangeInfo`](/en/docs/catalog/core-trading-spot-trading/api/ws-api/general#exchange-info) request.
  * There are multiple rate limit types across multiple intervals.
  * Responses can indicate current rate limit status in the optional `rateLimits` field.
  * Requests fail with status `429` when unfilled order count or request rate limits are violated.



#### How to interpret rate limits

A response with rate limit status may look like this:
    
    
    Code
    
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

#### How to show/hide rate limit information

`rateLimits` field is included with every response by default.

However, rate limit information can be quite bulky. If you are not interested in detailed rate limit status of every request, the `rateLimits` field can be omitted from responses to reduce their size.

  * Optional `returnRateLimits` boolean parameter in request.

Use `returnRateLimits` parameter to control whether to include `rateLimits` fields in response to individual requests.

Default request and response:
        
        Code
        
        { "id": 1, "method": "time" }
        
        Code
        
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
        
        Code
        
        { "id": 2, "method": "time", "params": { "returnRateLimits": false } }
        
        Code
        
        { "id": 2, "status": 200, "result": { "serverTime": 1656400527891 } }

  * Optional `returnRateLimits` boolean parameter in connection URL.

If you wish to omit `rateLimits` from all responses by default, use `returnRateLimits` parameter in the query string instead:
        
        Code
        
        wss://ws-api.binance.com:443/ws-api/v3?returnRateLimits=false

This will make all requests made through this connection behave as if you have passed `"returnRateLimits": false`.

If you _want_ to see rate limits for a particular request, you need to explicitly pass the `"returnRateLimits": true` parameter.




**Note:** Your requests are still rate limited if you hide the `rateLimits` field in responses.

### IP limits

  * Every request has a certain **weight** , added to your limit as you perform requests.
    * The heavier the request (e.g. querying data from multiple symbols), the more weight the request will cost.
    * Connecting to WebSocket API costs 2 weight.
  * Current weight usage is indicated by the `REQUEST_WEIGHT` rate limit type.
  * Use the [`exchangeInfo`](/en/docs/catalog/core-trading-spot-trading/api/ws-api/general#exchange-info) request to keep track of the current weight limits.
  * Weight is accumulated **per IP address** and is shared by all connections from that address.
  * If you go over the weight limit, requests fail with status `429`.
    * This status code indicates you should back off and stop spamming the API.
    * Rate-limited responses include a `retryAfter` field, indicating when you can retry the request.
  * **Repeatedly violating rate limits and/or failing to back off after receiving 429s will result in an automated IP ban and you will be disconnected.**
    * Requests from a banned IP address fail with status `418`.
    * `retryAfter` field indicates the timestamp when the ban will be lifted.
  * IP bans are tracked and **scale in duration** for repeat offenders, **from 2 minutes to 3 days**.



Successful response indicating that in 1 minute you have used 70 weight out of your 6000 limit:
    
    
    Code
    
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
    
    
    Code
    
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

### Unfilled Order Count

  * Successfully placed orders update the `ORDERS` rate limit type.
  * Rejected or unsuccessful orders might or might not update the `ORDERS` rate limit type.
  * **Please note that if your orders are consistently filled by trades, you can continuously place orders on the API**. For more information, please see [Spot Unfilled Order Count Rules](/en/docs/products/spot/faqs/order_count_decrement).
  * Use the [`account.rateLimits.orders`](/en/docs/catalog/core-trading-spot-trading/api/ws-api/account#account-rate-limits-orders) request to keep track of how many orders you have placed within this interval.
  * If you exceed this, requests fail with status `429`.
    * This status code indicates you should back off and stop spamming the API.
    * Responses that have a status `429` include a `retryAfter` field, indicating when you can retry the request.
  * This is maintained **per account** and is shared by all API keys of the account.



Successful response indicating that you have placed 12 orders in 10 seconds, and 4043 orders in the past 24 hours:
    
    
    Code
    
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

## Request security

  * Each method has a security type indicating required API key permissions, shown next to the method name (e.g., [Place new order (TRADE)](/en/docs/catalog/core-trading-spot-trading/api/ws-api/trade#order-place)).
  * If unspecified, the security type is `NONE`.
  * Except for `NONE`, all methods with a security type are considered `SIGNED` requests (i.e. including a `signature`), except for [listenKey management](/en/docs/products/spot/user-data-stream).
  * Secure methods require a valid API key to be specified and authenticated.
    * API keys can be created on the [API Management](https://www.binance.com/en/support/faq/360002502072) page of your Binance account.
    * **Both API key and secret key are sensitive.** Never share them with anyone. If you notice unusual activity in your account, immediately revoke all the keys and contact Binance support.
  * API keys can be configured to allow access only to certain types of secure methods.
    * For example, you can have an API key with `TRADE` permission for trading, while using a separate API key with `USER_DATA` permission to monitor your order status.
    * By default, an API key cannot `TRADE`. You need to enable trading in API Management first.

Security type| Description  
---|---  
`NONE`| Public market data  
`TRADE`| Trading on the exchange, placing and canceling orders  
`USER_DATA`| Private account information, such as order status and your trading history  
`USER_STREAM`| Managing User Data Stream subscriptions  
  
### SIGNED request security

  * `SIGNED` requests require an additional parameter: `signature`, authorizing the request.



#### Signature Case Sensitivity

  * **HMAC:** Signatures generated using HMAC are **not case-sensitive**. This means the signature string can be verified regardless of letter casing.
  * **RSA:** Signatures generated using RSA are **case-sensitive**.
  * **Ed25519:** Signatures generated using ED25519 are also **case-sensitive**



Please consult [SIGNED request example (HMAC)](/en/docs/products/spot/web-socket-api#signed-request-example-hmac), [SIGNED request example (RSA)](/en/docs/products/spot/web-socket-api#signed-request-example-rsa), and [SIGNED request example (Ed25519)](/en/docs/products/spot/web-socket-api#signed-request-example-ed25519) on how to compute signature, depending on which API key type you are using.

### Timing security

  * `SIGNED` requests also require a `timestamp` parameter which should be the current timestamp either in milliseconds or microseconds. (See [General API Information](/en/docs/products/spot/web-socket-api#general-api-information))
  * An additional optional parameter, `recvWindow`, specifies for how long the request stays valid and may only be specified in milliseconds.
    * `recvWindow` supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be specified.
    * If `recvWindow` is not sent, **it defaults to 5000 milliseconds**.
    * Maximum `recvWindow` is 60000 milliseconds.
  * Request processing logic is as follows:


    
    
    Code
    
    serverTime = getCurrentTime()
    if (timestamp < (serverTime + 1 second) && (serverTime - timestamp) <= recvWindow) {
      // begin processing request
      serverTime = getCurrentTime()
      if (serverTime - timestamp) <= recvWindow {
        // forward request to Matching Engine
      } else {
        // reject request
      }
      // finish processing request
    } else {
      // reject request
    }

**Serious trading is about timing.** Networks can be unstable and unreliable, which can lead to requests taking varying amounts of time to reach the servers. With `recvWindow`, you can specify that the request must be processed within a certain number of milliseconds or be rejected by the server.

**It is recommended to use a small`recvWindow` of 5000 or less!**

### SIGNED request example (HMAC)

Here is a step-by-step guide on how to sign requests using an HMAC secret key.

Example API key and secret key:

Key| Value  
---|---  
`apiKey`| `vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A`  
`secretKey`| `NhqPtmdSJYdKjVHjA7PZj4Mge3R5YNiP1e3UZjInClVN65XAbvqqM6A7H5fATj0j`  
  
**WARNING: DO NOT SHARE YOUR API KEY AND SECRET KEY WITH ANYONE.**

The example keys are provided here only for illustrative purposes.

Example of request with a symbol name comprised entirely of ASCII characters:
    
    
    Code
    
    {
      "id": "4885f793-e5ad-4c3b-8f6c-55d891472b71",
      "method": "order.place",
      "params": {
        "symbol": "BTCUSDT",
        "side": "SELL",
        "type": "LIMIT",
        "timeInForce": "GTC",
        "quantity": "0.01000000",
        "price": "52000.00",
        "recvWindow": 100,
        "timestamp": 1645423376532,
        "apiKey": "vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A",
        "signature": "------ FILL ME ------"
      }
    }

Example of a request with a symbol name containing non-ASCII characters:
    
    
    Code
    
    {
      "id": "4885f793-e5ad-4c3b-8f6c-55d891472b71",
      "method": "order.place",
      "params": {
        "symbol": "１２３４５６",
        "side": "BUY",
        "type": "LIMIT",
        "timeInForce": "GTC",
        "quantity": "0.01000000",
        "price": "0.10000000",
        "recvWindow": 5000,
        "timestamp": 1645423376532,
        "apiKey": "vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A",
        "signature": "------ FILL ME ------"
      }
    }

As you can see, the `signature` parameter is currently missing.

**Step 1: Construct the signature payload**

Take all request `params` except `signature` and **sort them in alphabetical order by parameter name** :

For the first set of example parameters (ASCII only):

Parameter| Value  
---|---  
`apiKey`| vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A  
`price`| 52000.00  
`quantity`| 0.01000000  
`recvWindow`| 100  
`side`| SELL  
`symbol`| BTCUSDT  
`timeInForce`| GTC  
`timestamp`| 1645423376532  
`type`| LIMIT  
  
For the second set of example parameters (some non-ASCII characters):

Parameter| Value  
---|---  
`apiKey`| vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A  
`price`| 0.10000000  
`quantity`| 1.00000000  
`recvWindow`| 5000  
`side`| BUY  
`symbol`| １２３４５６  
`timeInForce`| GTC  
`timestamp`| 1645423376532  
`type`| LIMIT  
  
Format parameters as `parameter=value` pairs separated by `&`. Values need to be encoded in UTF-8.

For the first set of example parameters (ASCII only), the signature payload should look like this:
    
    
    Code
    
    apiKey=vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A&price=52000.00&quantity=0.01000000&recvWindow=100&side=SELL&symbol=BTCUSDT&timeInForce=GTC&timestamp=1645423376532&type=LIMIT

For the second set of example parameters (some non-ASCII characters), the signature payload should look like this:
    
    
    Code
    
    apiKey=vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A&price=0.10000000&quantity=1.00000000&recvWindow=5000&side=BUY&symbol=１２３４５６&timeInForce=GTC&timestamp=1645423376532&type=LIMIT

**Step 2: Compute the signature**

  1. Use the `secretKey` of your API key as the signing key for the HMAC-SHA-256 algorithm.
  2. Sign the UTF-8 bytes of the signature payload constructed in Step 1.
  3. Encode the HMAC-SHA-256 output as a hex string.



Note that `apiKey`, `secretKey`, and the payload are **case-sensitive** , while the resulting signature value is case-insensitive.

You can cross-check your signature algorithm implementation with OpenSSL:

For the first set of example parameters (ASCII only):
    
    
    Code
    
    $ echo -n 'apiKey=vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A&price=52000.00&quantity=0.01000000&recvWindow=100&side=SELL&symbol=BTCUSDT&timeInForce=GTC&timestamp=1645423376532&type=LIMIT' \
      | openssl dgst -hex -sha256 -hmac 'NhqPtmdSJYdKjVHjA7PZj4Mge3R5YNiP1e3UZjInClVN65XAbvqqM6A7H5fATj0j'
    
    aa1b5712c094bc4e57c05a1a5c1fd8d88dcd628338ea863fec7b88e59fe2db24

For the second set of example parameters (some non-ASCII characters):
    
    
    Code
    
    $ echo -n 'apiKey=vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A&price=0.10000000&quantity=1.00000000&recvWindow=5000&side=BUY&symbol=１２３４５６&timeInForce=GTC&timestamp=1645423376532&type=LIMIT' \
      | openssl dgst -hex -sha256 -hmac 'NhqPtmdSJYdKjVHjA7PZj4Mge3R5YNiP1e3UZjInClVN65XAbvqqM6A7H5fATj0j'
    
    b33892ae8e687c939f4468c6268ddd4c40ac1af18ad19a064864c47bae0752cd

**Step 3: Add`signature` to request `params`**

Complete the request by adding the `signature` parameter with the signature string.

For the first set of example parameters (ASCII only):
    
    
    Code
    
    {
      "id": "4885f793-e5ad-4c3b-8f6c-55d891472b71",
      "method": "order.place",
      "params": {
        "symbol": "BTCUSDT",
        "side": "SELL",
        "type": "LIMIT",
        "timeInForce": "GTC",
        "quantity": "0.01000000",
        "price": "52000.00",
        "recvWindow": 100,
        "timestamp": 1645423376532,
        "apiKey": "vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A",
        "signature": "aa1b5712c094bc4e57c05a1a5c1fd8d88dcd628338ea863fec7b88e59fe2db24"
      }
    }

For the second set of example parameters (some non-ASCII characters):
    
    
    Code
    
    {
      "id": "4885f793-e5ad-4c3b-8f6c-55d891472b71",
      "method": "order.place",
      "params": {
        "symbol": "１２３４５６",
        "side": "BUY",
        "type": "LIMIT",
        "timeInForce": "GTC",
        "quantity": "1.00000000",
        "price": "0.10000000",
        "recvWindow": 5000,
        "timestamp": 1645423376532,
        "apiKey": "vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A",
        "signature": "b33892ae8e687c939f4468c6268ddd4c40ac1af18ad19a064864c47bae0752cd"
      }
    }

### SIGNED request example (RSA)

Here is a step-by-step guide on how to sign requests using an RSA private key.

Key| Value  
---|---  
`apiKey`| `CAvIjXy3F44yW6Pou5k8Dy1swsYDWJZLeoK2r8G4cFDnE9nosRppc2eKc1T8TRTQ`  
  
These examples assume the private key is stored in the file `test-rsa-prv.pem`.

**WARNING: DO NOT SHARE YOUR API KEY AND PRIVATE KEY WITH ANYONE.**

The example keys are provided here only for illustrative purposes.

Example of request with a symbol name comprised entirely of ASCII characters:
    
    
    Code
    
    {
      "id": "4885f793-e5ad-4c3b-8f6c-55d891472b71",
      "method": "order.place",
      "params": {
        "symbol": "BTCUSDT",
        "side": "SELL",
        "type": "LIMIT",
        "timeInForce": "GTC",
        "quantity": "0.01000000",
        "price": "52000.00",
        "recvWindow": 100,
        "timestamp": 1645423376532,
        "apiKey": "CAvIjXy3F44yW6Pou5k8Dy1swsYDWJZLeoK2r8G4cFDnE9nosRppc2eKc1T8TRTQ",
        "signature": "------ FILL ME ------"
      }
    }

Example of a request with a symbol name containing non-ASCII characters:
    
    
    Code
    
    {
      "id": "4885f793-e5ad-4c3b-8f6c-55d891472b71",
      "method": "order.place",
      "params": {
        "symbol": "１２３４５６",
        "side": "BUY",
        "type": "LIMIT",
        "timeInForce": "GTC",
        "quantity": "0.01000000",
        "price": "0.10000000",
        "recvWindow": 5000,
        "timestamp": 1645423376532,
        "apiKey": "CAvIjXy3F44yW6Pou5k8Dy1swsYDWJZLeoK2r8G4cFDnE9nosRppc2eKc1T8TRTQ",
        "signature": "------ FILL ME ------"
      }
    }

**Step 1: Construct the signature payload**

Take all request `params` except `signature` and **sort them in alphabetical order by parameter name** :

For the first set of example parameters (ASCII only):

Parameter| Value  
---|---  
`apiKey`| CAvIjXy3F44yW6Pou5k8Dy1swsYDWJZLeoK2r8G4cFDnE9nosRppc2eKc1T8TRTQ  
`price`| 52000.00  
`quantity`| 0.01000000  
`recvWindow`| 100  
`side`| SELL  
`symbol`| BTCUSDT  
`timeInForce`| GTC  
`timestamp`| 1645423376532  
`type`| LIMIT  
  
For the second set of example parameters (some non-ASCII characters):

Parameter| Value  
---|---  
`apiKey`| CAvIjXy3F44yW6Pou5k8Dy1swsYDWJZLeoK2r8G4cFDnE9nosRppc2eKc1T8TRTQ  
`price`| 0.10000000  
`quantity`| 1.00000000  
`recvWindow`| 5000  
`side`| BUY  
`symbol`| １２３４５６  
`timeInForce`| GTC  
`timestamp`| 1645423376532  
`type`| LIMIT  
  
Format parameters as `parameter=value` pairs separated by `&`. Values need to be encoded in UTF-8.

For the first set of example parameters (ASCII only), the signature payload should look like this:
    
    
    Code
    
    apiKey=CAvIjXy3F44yW6Pou5k8Dy1swsYDWJZLeoK2r8G4cFDnE9nosRppc2eKc1T8TRTQ&price=52000.00&quantity=0.01000000&recvWindow=100&side=SELL&symbol=BTCUSDT&timeInForce=GTC&timestamp=1645423376532&type=LIMIT

For the second set of example parameters (some non-ASCII characters), the signature payload should look like this:
    
    
    Code
    
    apiKey=CAvIjXy3F44yW6Pou5k8Dy1swsYDWJZLeoK2r8G4cFDnE9nosRppc2eKc1T8TRTQ&price=0.10000000&quantity=1.00000000&recvWindow=5000&side=BUY&symbol=１２３４５６&timeInForce=GTC&timestamp=1645423376532&type=LIMIT

**Step 2: Compute the signature**

  1. Sign the UTF-8 bytes of the signature payload constructed in Step 1 using the RSASSA-PKCS1-v1_5 algorithm with SHA-256 hash function.
  2. Encode the output in base64.



Note that `apiKey`, the payload, and the resulting `signature` are **case-sensitive**.

You can cross-check your signature algorithm implementation with OpenSSL:

For the first set of example parameters (ASCII only):
    
    
    Code
    
    $ echo -n 'apiKey=CAvIjXy3F44yW6Pou5k8Dy1swsYDWJZLeoK2r8G4cFDnE9nosRppc2eKc1T8TRTQ&price=52000.00&quantity=0.01000000&recvWindow=100&side=SELL&symbol=BTCUSDT&timeInForce=GTC&timestamp=1645423376532&type=LIMIT' \
      | openssl dgst -sha256 -sign test-rsa-prv.pem \
      | openssl enc -base64 -A
    
    OJJaf8C/3VGrU4ATTR4GiUDqL2FboSE1Qw7UnnoYNfXTXHubIl1iaePGuGyfct4NPu5oVEZCH4Q6ZStfB1w4ssgu0uiB/Bg+fBrRFfVgVaLKBdYHMvT+ljUJzqVaeoThG9oXlduiw8PbS9U8DYAbDvWN3jqZLo4Z2YJbyovyDAvDTr/oC0+vssLqP7NmlNb3fF3Bj7StmOwJvQJTbRAtzxK5PP7OQe+0mbW+D7RqVkUiSswR8qJFWTeSe4nXXNIdZdueYhF/Xf25L+KitJS5IHdIHcKfEw3MQzHFb2ZsGWkjDQwxkwr7Noi0Zaa+gFtxCuatGFm9dFIyx217pmSHtA==

For the second set of example parameters (some non-ASCII characters):
    
    
    Code
    
    $ echo -n 'apiKey=CAvIjXy3F44yW6Pou5k8Dy1swsYDWJZLeoK2r8G4cFDnE9nosRppc2eKc1T8TRTQ&price=0.10000000&quantity=1.00000000&recvWindow=5000&side=BUY&symbol=１２３４５６&timeInForce=GTC&timestamp=1645423376532&type=LIMIT' \
      | openssl dgst -sha256 -sign test-rsa-prv.pem \
      | openssl enc -base64 -A
    
    F3o/79Ttvl2cVYGPfBOF3oEOcm5QcYmTYWpdVIrKve5u+8paMNDAdUE+teqMxFM9HcquetGcfuFpLYtsQames5bDx/tskGM76TWW8HaM+6tuSYBSFLrKqChfA9hQGLYGjAiflf1YBnDhY+7vNbJFusUborNOloOj+ufzP5q42PvI3H0uNy3W5V3pyfXpDGCBtfCYYr9NAqA4d+AQfyllL/zkO9h9JSdozN49t0/hWGoD2dWgSO0Je6MytKEvD4DQXGeqNlBTB6tUXcWnRW+FcaKZ4KYqnxCtb1u8rFXUYgFykr2CbcJLSmw6ydEJ3EZ/NaZopRr+cU0W2m0HZ3qucw==

**Step 3: Add`signature` to request `params`**

Complete the request by adding the `signature` parameter with the signature string.

For the first set of example parameters (ASCII only):
    
    
    Code
    
    {
      "id": "4885f793-e5ad-4c3b-8f6c-55d891472b71",
      "method": "order.place",
      "params": {
        "symbol": "BTCUSDT",
        "side": "SELL",
        "type": "LIMIT",
        "timeInForce": "GTC",
        "quantity": "0.01000000",
        "price": "52000.00",
        "newOrderRespType": "ACK",
        "recvWindow": 100,
        "timestamp": 1645423376532,
        "apiKey": "CAvIjXy3F44yW6Pou5k8Dy1swsYDWJZLeoK2r8G4cFDnE9nosRppc2eKc1T8TRTQ",
        "signature": "OJJaf8C/3VGrU4ATTR4GiUDqL2FboSE1Qw7UnnoYNfXTXHubIl1iaePGuGyfct4NPu5oVEZCH4Q6ZStfB1w4ssgu0uiB/Bg+fBrRFfVgVaLKBdYHMvT+ljUJzqVaeoThG9oXlduiw8PbS9U8DYAbDvWN3jqZLo4Z2YJbyovyDAvDTr/oC0+vssLqP7NmlNb3fF3Bj7StmOwJvQJTbRAtzxK5PP7OQe+0mbW+D7RqVkUiSswR8qJFWTeSe4nXXNIdZdueYhF/Xf25L+KitJS5IHdIHcKfEw3MQzHFb2ZsGWkjDQwxkwr7Noi0Zaa+gFtxCuatGFm9dFIyx217pmSHtA=="
      }
    }

For the second set of example parameters (some non-ASCII characters):
    
    
    Code
    
    {
      "id": "4885f793-e5ad-4c3b-8f6c-55d891472b71",
      "method": "order.place",
      "params": {
        "symbol": "１２３４５６",
        "side": "SELL",
        "type": "LIMIT",
        "timeInForce": "GTC",
        "quantity": "1.00000000",
        "price": "0.10000000",
        "recvWindow": 5000,
        "timestamp": 1645423376532,
        "apiKey": "CAvIjXy3F44yW6Pou5k8Dy1swsYDWJZLeoK2r8G4cFDnE9nosRppc2eKc1T8TRTQ",
        "signature": "F3o/79Ttvl2cVYGPfBOF3oEOcm5QcYmTYWpdVIrKve5u+8paMNDAdUE+teqMxFM9HcquetGcfuFpLYtsQames5bDx/tskGM76TWW8HaM+6tuSYBSFLrKqChfA9hQGLYGjAiflf1YBnDhY+7vNbJFusUborNOloOj+ufzP5q42PvI3H0uNy3W5V3pyfXpDGCBtfCYYr9NAqA4d+AQfyllL/zkO9h9JSdozN49t0/hWGoD2dWgSO0Je6MytKEvD4DQXGeqNlBTB6tUXcWnRW+FcaKZ4KYqnxCtb1u8rFXUYgFykr2CbcJLSmw6ydEJ3EZ/NaZopRr+cU0W2m0HZ3qucw=="
      }
    }

### SIGNED Request Example (Ed25519)

**Note: It is highly recommended to use Ed25519 API keys as they will provide the best performance and security out of all supported key types.**

Here is a step-by-step guide on how to sign requests using an Ed25519 private key.

Key| Value  
---|---  
`apiKey`| `4yNzx3yWC5bS6YTwEkSRaC0nRmSQIIStAUOh1b6kqaBrTLIhjCpI5lJH8q8R8WNO`  
  
These examples assume the private key is stored in the file `test-ed25519-prv.pem`.

**WARNING: DO NOT SHARE YOUR API KEY AND PRIVATE KEY WITH ANYONE.**

The example keys are provided here only for illustrative purposes.

Example of request with a symbol name comprised entirely of ASCII characters:
    
    
    Code
    
    {
      "id": "4885f793-e5ad-4c3b-8f6c-55d891472b71",
      "method": "order.place",
      "params": {
        "symbol": "BTCUSDT",
        "side": "SELL",
        "type": "LIMIT",
        "timeInForce": "GTC",
        "quantity": "0.01000000",
        "price": "52000.00",
        "recvWindow": 100,
        "timestamp": 1645423376532,
        "apiKey": "4yNzx3yWC5bS6YTwEkSRaC0nRmSQIIStAUOh1b6kqaBrTLIhjCpI5lJH8q8R8WNO",
        "signature": "------ FILL ME ------"
      }
    }

Example of a request with a symbol name containing non-ASCII characters:
    
    
    Code
    
    {
      "id": "4885f793-e5ad-4c3b-8f6c-55d891472b71",
      "method": "order.place",
      "params": {
        "symbol": "１２３４５６",
        "side": "BUY",
        "type": "LIMIT",
        "timeInForce": "GTC",
        "quantity": "0.01000000",
        "price": "0.10000000",
        "recvWindow": 5000,
        "timestamp": 1645423376532,
        "apiKey": "4yNzx3yWC5bS6YTwEkSRaC0nRmSQIIStAUOh1b6kqaBrTLIhjCpI5lJH8q8R8WNO",
        "signature": "------ FILL ME ------"
      }
    }

**Step 1: Construct the signature payload**

Take all request `params` except `signature` and **sort them in alphabetical order by parameter name** :

For the first set of example parameters (ASCII only):

Parameter| Value  
---|---  
`apiKey`| 4yNzx3yWC5bS6YTwEkSRaC0nRmSQIIStAUOh1b6kqaBrTLIhjCpI5lJH8q8R8WNO  
`price`| 52000.00  
`quantity`| 0.01000000  
`recvWindow`| 100  
`side`| SELL  
`symbol`| BTCUSDT  
`timeInForce`| GTC  
`timestamp`| 1645423376532  
`type`| LIMIT  
  
For the second set of example parameters (some non-ASCII characters):

Parameter| Value  
---|---  
`apiKey`| 4yNzx3yWC5bS6YTwEkSRaC0nRmSQIIStAUOh1b6kqaBrTLIhjCpI5lJH8q8R8WNO  
`price`| 0.20000000  
`quantity`| 1.00000000  
`recvWindow`| 5000  
`side`| SELL  
`symbol`| １２３４５６  
`timeInForce`| GTC  
`timestamp`| 1668481559918  
`type`| LIMIT  
  
Format parameters as `parameter=value` pairs separated by `&`. Values need to be encoded in UTF-8.

For the first set of example parameters (ASCII only), the signature payload should look like this:
    
    
    Code
    
    apiKey=4yNzx3yWC5bS6YTwEkSRaC0nRmSQIIStAUOh1b6kqaBrTLIhjCpI5lJH8q8R8WNO&price=52000.00&quantity=0.01000000&recvWindow=100&side=SELL&symbol=BTCUSDT&timeInForce=GTC&timestamp=1645423376532&type=LIMIT

For the second set of example parameters (some non-ASCII characters), the signature payload should look like this:
    
    
    Code
    
    apiKey=4yNzx3yWC5bS6YTwEkSRaC0nRmSQIIStAUOh1b6kqaBrTLIhjCpI5lJH8q8R8WNO&price=0.10000000&quantity=1.00000000&recvWindow=5000&side=BUY&symbol=１２３４５６&timeInForce=GTC&timestamp=1645423376532&type=LIMIT

**Step 2: Compute the signature**

  1. Sign the UTF-8 bytes of your signature payload constructed in Step 1 using the Ed25519 private key.
  2. Encode the output in base64.



Note that `apiKey`, the payload, and the resulting `signature` are **case-sensitive**.

You can cross-check your signature algorithm implementation with OpenSSL:

For the first set of example parameters (ASCII only):
    
    
    Code
    
    echo -n "apiKey=4yNzx3yWC5bS6YTwEkSRaC0nRmSQIIStAUOh1b6kqaBrTLIhjCpI5lJH8q8R8WNO&price=52000.00&quantity=0.01000000&recvWindow=100&side=SELL&symbol=BTCUSDT&timeInForce=GTC&timestamp=1645423376532&type=LIMIT" \
      | openssl dgst -sign ./test-ed25519-prv.pem \
      | openssl enc -base64 -A
    
    EocljwPl29jDxWYaaRaOo4pJ9wEblFbklJvPugNscLLuKd5vHM2grWjn1z+rY0aJ7r/44enxHL6mOAJuJ1kqCg==

For the second set of example parameters (some non-ASCII characters):
    
    
    Code
    
    echo -n "apiKey=4yNzx3yWC5bS6YTwEkSRaC0nRmSQIIStAUOh1b6kqaBrTLIhjCpI5lJH8q8R8WNO&price=0.10000000&quantity=1.00000000&recvWindow=5000&side=BUY&symbol=１２３４５６&timeInForce=GTC&timestamp=1645423376532&type=LIMIT" \
      | openssl dgst -sign ./test-ed25519-prv.pem \
      | openssl enc -base64 -A
    
    dtNHJeyKry+cNjiGv+sv5kynO9S40tf8k7D5CfAEQAp0s2scunZj+ovJdz2OgW8XhkB9G3/HmASkA9uY9eyFCA==

**Step 3: Add the signature to request`params`**

For the first set of example parameters (ASCII only):
    
    
    Code
    
    {
      "id": "4885f793-e5ad-4c3b-8f6c-55d891472b71",
      "method": "order.place",
      "params": {
        "symbol": "BTCUSDT",
        "side": "SELL",
        "type": "LIMIT",
        "timeInForce": "GTC",
        "quantity": "0.01000000",
        "price": "52000.00",
        "newOrderRespType": "ACK",
        "recvWindow": 100,
        "timestamp": 1645423376532,
        "apiKey": "4yNzx3yWC5bS6YTwEkSRaC0nRmSQIIStAUOh1b6kqaBrTLIhjCpI5lJH8q8R8WNO",
        "signature": "EocljwPl29jDxWYaaRaOo4pJ9wEblFbklJvPugNscLLuKd5vHM2grWjn1z+rY0aJ7r/44enxHL6mOAJuJ1kqCg=="
      }
    }

For the second set of example parameters (some non-ASCII characters):
    
    
    Code
    
    {
      "id": "4885f793-e5ad-4c3b-8f6c-55d891472b71",
      "method": "order.place",
      "params": {
        "symbol": "１２３４５６",
        "side": "SELL",
        "type": "LIMIT",
        "timeInForce": "GTC",
        "quantity": "1.00000000",
        "price": "0.10000000",
        "recvWindow": 5000,
        "timestamp": 1645423376532,
        "apiKey": "4yNzx3yWC5bS6YTwEkSRaC0nRmSQIIStAUOh1b6kqaBrTLIhjCpI5lJH8q8R8WNO",
        "signature": "dtNHJeyKry+cNjiGv+sv5kynO9S40tf8k7D5CfAEQAp0s2scunZj+ovJdz2OgW8XhkB9G3/HmASkA9uY9eyFCA=="
      }
    }

Here is a sample Python script performing all the steps above:
    
    
    Code
    
    #!/usr/bin/env python3
    
    import base64
    import time
    import json
    from cryptography.hazmat.primitives.serialization import load_pem_private_key
    from websocket import create_connection
    
    # Set up authentication
    API_KEY='put your own API Key here'
    PRIVATE_KEY_PATH='test-prv-key.pem'
    
    # Load the private key.
    # In this example the key is expected to be stored without encryption,
    # but we recommend using a strong password for improved security.
    with open(PRIVATE_KEY_PATH, 'rb') as f:
      private_key = load_pem_private_key(data=f.read(), password=None)
    
    # Set up the request parameters
    params = {
        'apiKey':       API_KEY,
        'symbol':       '１２３４５６',
        'side':         'SELL',
        'type':         'LIMIT',
        'timeInForce':  'GTC',
        'quantity':     '1.0000000',
        'price':        '0.10000000',
        'recvWindow':   5000
    }
    
    # Timestamp the request
    timestamp = int(time.time() * 1000) # UNIX timestamp in milliseconds
    params['timestamp'] = timestamp
    
    # Sort parameters alphabetically by name
    params = dict(sorted(params.items()))
    
    # Compute the signature payload
    payload = '&'.join([f"{k}={v}" for k,v in params.items()]) # no percent encoding here!
    
    # Sign the request
    signature = base64.b64encode(private_key.sign(payload.encode('UTF-8')))
    params['signature'] = signature.decode('ASCII')
    
    # Send the request
    request = {
        'id': 'my_new_order',
        'method': 'order.place',
        'params': params
    }
    
    ws = create_connection("wss://ws-api.binance.com:443/ws-api/v3")
    ws.send(json.dumps(request))
    result =  ws.recv()
    ws.close()
    
    print(result)

## Session Authentication

**Note:** Only _Ed25519_ keys are supported for this feature.

If you do not want to specify `apiKey` and `signature` in each individual request, you can authenticate your API key for the active WebSocket session.

Once authenticated, you no longer have to specify `apiKey` and `signature` for those requests that need them. Requests will be performed on behalf of the account owning the authenticated API key.

**Note:** You still have to specify the `timestamp` parameter for `SIGNED` requests.

### Authenticate after connection

You can authenticate an already established connection using session authentication requests:

  * [`session.logon`](/en/docs/catalog/core-trading-spot-trading/api/ws-api/auth#session-logon) – authenticate, or change the API key associated with the connection
  * [`session.status`](/en/docs/catalog/core-trading-spot-trading/api/ws-api/auth#session-status) – check connection status and the current API key
  * [`session.logout`](/en/docs/catalog/core-trading-spot-trading/api/ws-api/auth#session-logout) – forget the API key associated with the connection



**Regarding API key revocation:**

If during an active session the API key becomes invalid for _any reason_ (e.g. IP address is not whitelisted, API key was deleted, API key doesn't have correct permissions, etc), after the next request the session will be revoked with the following error message:
    
    
    Code
    
    {
        "id": null,
        "status": 401,
        "error": {
            "code": -2015,
            "msg": "Invalid API-key, IP, or permissions for action."
        }
    }

### Authorize _ad hoc_ requests

Only one API key can be authenticated with the WebSocket connection. The authenticated API key is used by default for requests that require an `apiKey` parameter. However, you can always specify the `apiKey` and `signature` explicitly for individual requests, overriding the authenticated API key and using a different one to authorize a specific request.

For example, you might want to authenticate your `USER_DATA` key to be used by default, but specify the `TRADE` key with an explicit signature when placing orders.

## Data sources

  * The API system is asynchronous. Some delay in the response is normal and expected.

  * Each method has a data source indicating where the data is coming from, and thus how up-to-date it is.


Data Source| Latency| Description  
---|---|---  
Matching Engine| lowest| The Matching Engine produces the response directly  
Memory| low| Data is fetched from API server's local or external memory cache  
Database| moderate| Data is retrieved from the database  
  
  * Some methods have more than one data source (e.g., Memory => Database).

This means that the API will look for the latest data in that order: first in the cache, then in the database.




Was this page helpful?

Last modified on November 12, 2026

[REST API](/en/docs/products/spot/rest-api)[WebSocket Streams](/en/docs/products/spot/web-socket-streams)

---

# WebSocket API 基本信息

## API 基本信息

  * 本篇所列出的 wss 接口的 base URL：**`wss://ws-api.binance.com:443/ws-api/v3`**
    * 如果使用标准443端口时遇到问题，可以使用替代端口9443。
    * [现货测试网](https://testnet.binance.vision)的 base URL 是 `wss://ws-api.testnet.binance.vision/ws-api/v3`。
  * 每个到 base URL 的链接有效期不超过24小时，请妥善处理断线重连。
  * 当服务器即将关闭时，系统将发送 [`serverShutdown`](/zh-CN/docs/products/spot/web-socket-api#%E6%9C%8D%E5%8A%A1%E5%99%A8%E5%85%B3%E9%97%AD) 事件，并导致连接断开。请尽快建立新连接，以防止中断。
  * 我们支持 HMAC，RSA 以及 Ed25519 Key 类型。 如需进一步了解，请参考 [API Key 类型](/zh-CN/docs/products/spot/faqs/api_key_types)。
  * 响应默认为 JSON 格式。如果您想接收 SBE 格式的响应，请参考 [简单二进制编码 （SBE） 常见问题](/zh-CN/docs/products/spot/faqs/sbe_faq)。
  * 如果您的请求包含非 ASCII 字符的交易对名称，那么响应中可能包含以 UTF-8 编码的非 ASCII 字符。
  * 即使请求本身不包含非 ASCII 字符，某些方法也可能会返回包含以 UTF-8 编码的非 ASCII 字符的资产和/或交易对名称。
  * WebSocket 服务器**每20秒** 发送 PING 消息。
    * 如果websocket 服务器没有在一分钟之内收到PONG 消息应答，连接会被断开。
    * 当客户收到PING消息，必须尽快回复PONG消息，同时payload需要和PING消息一致。
    * 服务器允许未经请求的PONG消息，但这不会保证连接不断开。**对于这些PONG 消息，建议payload为空。**
  * 除非另有说明，否则数据将按**时间顺序** 返回。
    * 如果未指定 `startTime` 或 `endTime`，则返回最近的条目，直至达到限制值。
    * 如果指定 `startTime`，则返回从 `startTime` 到限制值为止最老的条目。
    * 如果指定 `endTime`，则返回截至 `endTime` 和限制值为止最近的条目。
    * 如果同时指定 `startTime` 和 `endTime`，则行为类似于 `startTime`，但不超过 `endTime`。
  * JSON 响应中的所有时间和时间戳相关字段均以**UTC 毫秒为默认单位** 。要以微秒为单位接收信息，请在 URL 中添加参数 `timeUnit=MICROSECOND` 或 `timeUnit=microsecond`。
  * 时间戳参数（例如 `startTime`、`endTime`、`timestamp`）可以以毫秒或微秒为单位传递。
  * 除非另有说明，所有字段名称和值都**大小写敏感** 。
  * 如需进一步了解枚举或术语，请参考 [现货交易API术语表](/zh-CN/docs/products/spot/faqs/spot_glossary) 页面。
  * API 处理请求的超时时间为 10 秒。如果撮合引擎的响应时间超过此时间，API 将返回 “Timeout waiting for response from backend server. Send status unknown; execution status unknown.”。[(-1007 超时)](/zh-CN/docs/products/spot/errors#-1007-timeout)
    * 这并不总是意味着该请求在撮合引擎中失败。
    * 如果请求状态未显示在 [用户数据流](/zh-CN/docs/products/spot/user-data-stream) 中，请执行 API 查询以获取其状态。
  * **请避免在请求中使用 SQL 关键字** ，因为这可能会触发 Web 应用防火墙（WAF）规则导致安全拦截。详情请参见 <https://www.binance.com/zh-CN/support/faq/detail/360004492232>



## 请求格式

请求必须在 **text 帧** 中以 JSON 格式发送，每帧一个请求。

请求示例:
    
    
    Code
    
    {
      "id": "e2a85d9f-07a5-4f94-8d5f-789dc3deb097",
      "method": "order.place",
      "params": {
        "symbol": "BTCUSDT",
        "side": "BUY",
        "type": "LIMIT",
        "price": "0.1",
        "quantity": "10",
        "timeInForce": "GTC",
        "timestamp": 1655716096498,
        "apiKey": "T59MTDLWlpRW16JVeZ2Nju5A5C98WkMm8CSzWC4oqynUlTm1zXOxyauT8LmwXEv9",
        "signature": "5942ad337e6779f2f4c62cd1c26dba71c91514400a24990a3e7f5edec9323f90"
      }
    }

请求字段:

名称| 类型| 是否必需| 描述  
---|---|---|---  
`id`| INT / STRING / `null`| YES| 任意的 ID 用于匹配对请求的响应  
`method`| STRING| YES| 请求函数名称  
`params`| OBJECT| NO| 请求参数。如果没有参数可以省略  
  
  * 请求 `id` 是任意的。可以使用 UUID、顺次 ID、当前时间戳等。服务器不会以任何方式解释 `id`，只是在响应中回显它。

可以在一个会话中自由重复使用 ID，不过请注意不要一次发送多个具有相同 ID 的请求，因为否则可能无法区分响应。

  * 请求函数名称可以以显式版本为前缀，例如：`"v3/order.place"`

  * `params` 的顺序不重要。




## 响应格式

响应在 **text 帧** 中以 JSON 格式返回，每帧一个响应。

成功响应示例:
    
    
    Code
    
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

失败响应示例:
    
    
    Code
    
    {
      "id": "e2a85d9f-07a5-4f94-8d5f-789dc3deb097",
      "status": 400,
      "error": {
        "code": -2010,
        "msg": "Account has insufficient balance for requested action."
      },
      "rateLimits": [
        {
          "rateLimitType": "ORDERS",
          "interval": "SECOND",
          "intervalNum": 10,
          "limit": 50,
          "count": 13
        },
        {
          "rateLimitType": "ORDERS",
          "interval": "DAY",
          "intervalNum": 1,
          "limit": 160000,
          "count": 4044
        },
        {
          "rateLimitType": "REQUEST_WEIGHT",
          "interval": "MINUTE",
          "intervalNum": 1,
          "limit": 6000,
          "count": 322
        }
      ]
    }

响应字段:

### 状态代码

`status` 字段的状态代码与HTTP的状态代码相同。

一些常见状态代码：

  * `200` 代码指示成功响应。
  * `4XX` 错误码用于指示错误的请求内容、行为、格式。问题在于请求者。
    * `400` – 错误码表示请求失败，请参阅 `error` 了解原因。
    * `403` – 错误码表示违反 WAF 限制(Web应用程序防火墙)。这可能表示触发了速率限制或安全拦截。详情请参见 <https://www.binance.com/zh-CN/support/faq/detail/360004492232> 。
    * `409` – 错误码表示请求有一部分成功，一部分失败。请参阅 `error` 了解更多详细
    * `418` – 表示收到 429 后继续访问，于是被封了。
    * `429` – 错误码表示警告访问频次超限，即将被封IP。
  * `5XX` 错误码用于指示Binance服务侧的问题。
    * **重要** ：如果响应包含 5xx 状态码，**并不** 一定意思请求失败。执行状态为 _unknown_ ，请求可能实际成功。请使用 query 函数确认状态。建议建立一个新 WebSocket 连接用于确认状态。



有关错误代码和消息的列表，请参阅 [Binance 的错误代码](/zh-CN/docs/products/spot/errors)。

## 订单响应中的特定条件时才会出现的字段

订单响应中的有一些字段仅在满足特定条件时才会出现。这些订单响应可以来自下订单，查询订单或取消订单，并且可以包括订单列表类型。下面列出了这些字段：

名称| 描述| 显示的条件| 示例  
---|---|---|---  
`icebergQty`| 冰山订单的数量。| 只有在请求中发送 `icebergQty` 参数时才会出现。| `"icebergQty": "0.00000000"`  
`quoteNotionalLimit`| 订单可消耗的报价资产名义价值上限。| 只有在下单时设置了报价资产名义价值上限时才会出现。| `"quoteNotionalLimit": "250.00000000"`  
`preventedMatchId`| 与 `symbol` 结合使用时，可用于查询因为 STP 导致订单失效的过期订单。| 只有在因为 STP 导致订单失效时可见。| `"preventedMatchId": 0`  
`preventedQuantity`| 因为 STP 导致订单失效的数量。| 只有在因为 STP 导致订单失效时可见。| `"preventedQuantity": "1.200000"`  
`effectiveSelfTradePreventionMode`| 撮合引擎实际生效的 STP 模式。可能的值：`EXPIRE_MAKER`、`EXPIRE_BOTH`、`DECREMENT`。| 仅出现在 `FULL` 订单响应的 `preventedMatches[]` 条目中，且实际生效的 STP 模式与订单的 `selfTradePreventionMode` 不同时出现。| `"effectiveSelfTradePreventionMode": "DECREMENT"`  
`stopPrice`| 用于设置逻辑订单中的触发价。| `STOP_LOSS`，`TAKE_PROFIT`，`STOP_LOSS_LIMIT` 和 `TAKE_PROFIT_LIMIT` 订单时可见。| `"stopPrice": "23500.00000000"`  
`strategyId`| 策略单ID; 用以关联此订单对应的交易策略。| 如果在请求中添加了参数，则会出现。| `"strategyId": 37463720`  
`strategyType`| 策略单类型; 用以显示此订单对应的交易策略。| 如果在请求中添加了参数，则会出现。| `"strategyType": 1000000`  
`trailingDelta`| 用以定义追踪止盈止损订单被触发的价格差。| 出现在追踪止损订单中。| `"trailingDelta": 10`  
`trailingTime`| 追踪单被激活和跟踪价格变化的时间。| 出现在追踪止损订单中。| `"trailingTime": -1`  
`usedSor`| 用于确定订单是否使用SOR的字段| 在使用SOR下单时出现| `"usedSor": true`  
`workingFloor`| 用以定义订单是通过 SOR 还是由订单提交到的订单簿（order book）成交的。| 出现在使用了 SOR 的订单中。| `"workingFloor": "SOR"`  
`pegPriceType`| 挂钩价格类型| 仅用于挂钩订单| `"pegPriceType": "PRIMARY_PEG"`  
`pegOffsetType`| 挂钩价格偏移类型| 如若需要，仅用于挂钩订单| `"pegOffsetType": "PRICE_LEVEL"`  
`pegOffsetValue`| 挂钩价格偏移值| 如若需要，仅用于挂钩订单| `"pegOffsetValue": 5`  
`peggedPrice`| 订单对应的当前挂钩价格| 一旦确定，仅用于挂钩订单| `"peggedPrice": "87523.83710000"`  
`expiryReason`| 订单失效原因| 当订单失效时| `"expiryReason": "INSUFFICIENT_LIQUIDITY"`  
  
## 事件格式

[用户数据流](/zh-CN/docs/products/spot/user-data-stream)中的非 SBE 会话事件以 JSON 格式在 **text 帧** 中发送，每帧一个事件。

[SBE 会话](/zh-CN/docs/products/spot/faqs/sbe_faq)中的事件将作为 **二进制帧** 发送。

有关如何在 WebSocket API 中订阅用户数据流的详细信息，请参阅 [`订阅用户数据流`](/zh-CN/docs/catalog/core-trading-spot-trading/api/ws-api/user-data-stream#user-data-stream-subscribe)。

事件示例:
    
    
    Code
    
    {
        "subscriptionId": 0,
        "event": {
            "e": "outboundAccountPosition",
            "E": 1728972148778,
            "u": 1728972148778,
            "B": [
                {
                    "a": "BTC",
                    "f": "11818.00000000",
                    "l": "182.00000000"
                },
                {
                    "a": "USDT",
                    "f": "10580.00000000",
                    "l": "70.00000000"
                }
            ]
        }
    }

事件字段:

名称| 类型| 是否必须| 描述  
---|---|---|---  
`event`| OBJECT| YES| 事件 payload。请看 [用户数据流](/zh-CN/docs/products/spot/user-data-stream)  
`subscriptionId`| INT| NO| 用以标识事件来自于哪个订阅。详见 [用户数据流订阅](/zh-CN/docs/products/spot/user-data-stream#%E4%B8%80%E8%88%AC%E4%BF%A1%E6%81%AF)  
  
## 连接事件

### 服务器关闭

当服务器即将关闭时，会发送 `serverShutdown` 事件。
    
    
    Code
    
    {
      "event": {
        "e": "serverShutdown", // 事件类型
        "E": 1770123456789,    // 事件时间
        "T": 1770124000000     // 即将关闭时间
       }
    }

`T` 字段表示 WebSocket 会话的关闭时间。

在 SBE 会话中，`T` 字段仅在 [SBE 模式 3:6](/zh-CN/docs/products/spot/sbe/schemas/) 及更高版本中提供。

请尽快建立新连接，以防中断

## 速率限制

### 连接数量限制

每IP地址、每5分钟最多可以发送300次连接请求。

### 速率限制基本信息

  * [`exchangeInfo`](/zh-CN/docs/catalog/core-trading-spot-trading/api/ws-api/general#exchange-info) 有包含与速率限制相关的信息。
  * 根据不同的间隔，有多种频率限制类型。
  * 从响应中的可选 `rateLimits` 字段，能看到当前的频率限制状态。
  * 当您超出未成交订单计数或者请求速率限制时，请求会失败并返回 HTTP 状态代码 429。



#### 如何咨询频率限制

频率限制状态的响应可能如下所示：
    
    
    Code
    
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

例如，`1 MINUTE` 间隔表示每分钟开始。在 00:01:23.456 提交的请求计入 00:01:00 分钟的限制。一旦 00:02:00 分钟开始，计数将再次重置为零。

其他间隔的行为方式类似。例如，`1 DAY` 频率限制是在每天 00:00 UTC 重置，并且 `10 SECOND` 间隔重置为每分钟的 00、10、20...秒。

API 有多种频率限制间隔。如果您用完了较短的间隔但较长的间隔仍然允许请求，您将不得不等待较短的间隔到期并重置。如果你用完了更长的间隔，你将不得不等待那个间隔重置，即使较短的频率限制计数为零。

#### 如何显示/隐藏频率限制信息

默认情况下，每个响应都包含 `rateLimits` 字段。

但是，频率限制信息可能非常大。如果您对每个请求的详细频率限制状态不感兴趣，可以从响应中省略 `rateLimits` 字段。

  * 请求中的可选 `returnRateLimits` boolean 参数。

使用 `returnRateLimits` 参数控制是否包含 `rateLimits` 字段以响应单个请求。

默认请求和响应：
        
        Code
        
        { "id": 1, "method": "time" }
        
        Code
        
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
        
        Code
        
        { "id": 2, "method": "time", "params": { "returnRateLimits": false } }
        
        Code
        
        { "id": 2, "status": 200, "result": { "serverTime": 1656400527891 } }

  * 连接 URL 中可选的 `returnRateLimits` boolean 参数。

如果您希望在默认情况下从所有响应中省略 `rateLimits`，可以在 query string 中使用 `returnRateLimits` 参数：
        
        Code
        
        wss://ws-api.binance.com:443/ws-api/v3?returnRateLimits=false

这将使通过此连接发出的所有请求的行为就像您已传了 `"returnRateLimits"：false` 一样。

如果您 _想_ 查看特定请求的频率限制，您需要特定传 `"returnRateLimits"：true` 参数。




**注意:** 如果您在响应中隐藏 `rateLimits` 字段，您的请求仍然还是会受到频率限制的。

### IP 访问限制

  * 每个请求都有一个特定的 **权重** ，它会添加到您的访问限制中。
    * 越消耗资源的接口, 比如查询多个交易对, 权重就会越大。
    * 连接到 WebSocket API 会用到2个权重。
  * 当前权重使用由 `REQUEST_WEIGHT` 频率限制类型指示。
  * 请使用[`exchangeInfo`](/zh-CN/docs/catalog/core-trading-spot-trading/api/ws-api/general#exchange-info)请求来跟踪当前的重量限制。
  * 权重是基于**每个 IP 地址** 累积的，并由来自该地址的所有连接共享。
  * 如果超多限制，客服端会收到 `429`。
    * 这错误代码表示您有责任停止发送请求，不得滥用API。
    * 响应会包含一个 `retryAfter` 字段，指示在什么时候您能重试。
  * **屡次违反速率限制或者在收到429后未能退缩将导致自动 IP 封禁和断开连接。**
    * 被禁止 IP 地址的请求失败，状态为 `418`。
    * `retryAfter` 字段表示解除禁令的timestamp。
  * 频繁违反限制的封禁时间会**逐渐延长** ，**从最短2分钟到最长3天** 。



表示在1分钟内使用了（1200权重限制中的）70权重的成功响应：
    
    
    Code
    
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
    
    
    Code
    
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

### 未成交订单计数

  * 成功下单将更新 `订单` 速率限制类型。
  * 被拒绝或不成功的订单可能会也可能不会更新 `订单` 速率限制类型。
  * **请注意，如果您的订单一直顺利完成交易，您可以通过 API 持续下订单** 。更多信息，请参见 [现货未成交订单计数规则](/zh-CN/docs/products/spot/faqs/order_count_decrement)。
  * 使用 [`account.rateLimits.orders`](/zh-CN/docs/catalog/core-trading-spot-trading/api/ws-api/account#account-rate-limits-orders) 请求来跟踪您在此时间间隔内下了多少订单。
  * 如果超过此值，请求将失败，状态为 `429`。
    * 此状态代码表示您应退出并停止向 API 滥发信息。
    * 状态为 `429` 的响应会包含 `retryAfter` 字段，用以指示何时可以重试请求。
  * 这是按 **每一个账户** 维护的，并由该账户的所有 API 密钥共享。



表示在10秒内下了12个订单和在24小时内下了4043个订单的成功响应：
    
    
    Code
    
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

## 请求鉴权类型

  * 每个方法都有一个鉴权类型，指示所需的 API 密钥权限，显示在方法名称旁边（例如，[下新订单 (TRADE)](/zh-CN/docs/catalog/core-trading-spot-trading/api/ws-api/trade#order-place)）。
  * 如果未指定，则鉴权类型为 `NONE`。
  * 除了为 `NONE` 外，所有具有鉴权类型的方法均视为 `SIGNED` 请求（即包含 `signature`），[listenKey 管理](/zh-CN/docs/products/spot/user-data-stream) 除外。
  * 具有鉴权类型的方法需要提供有效的 API 密钥并验证通过。
    * API 密钥可在您的 Binance 账户的 [API 管理](https://www.binance.com/en/support/faq/360002502072) 页面创建。
    * **API 密钥和密钥对均为敏感信息，切勿与他人分享。** 如果发现账户有异常活动，请立即撤销所有密钥并联系 Binance 支持。
  * API 密钥可配置为仅允许访问某些鉴权类型。
    * 例如，您可以拥有具有 `TRADE` 权限的 API 密钥用于交易，同时使用具有 `USER_DATA` 权限的另一个 API 密钥来监控订单状态。
    * 默认情况下，API 密钥无法进行 `TRADE`，您需要先在 API 管理中启用交易权限。

鉴权类型| 描述  
---|---  
`NONE`| 公开市场数据  
`TRADE`| 在交易所交易，下单和取消订单  
`USER_DATA`| 私人账户信息，例如订单状态和交易历史  
`USER_STREAM`| 管理用户数据流订阅  
  
### 需要签名的请求

  * 为了授权请求，`SIGNED` 请求必须带 `signature` 参数。



#### 签名区分大小写

  * **HMAC：** 使用 HMAC 生成的签名**不区分大小写** 。这意味着无论字母大小写如何，签名字符串都可以被验证。
  * **RSA：** 使用 RSA 生成的签名**区分大小写** 。
  * **Ed25519：** 使用 Ed25519 生成的签名也**区分大小写** 。



### 时间同步安全

  * `SIGNED` 请求还需要一个 `timestamp` 参数，该参数应为当前时间戳，单位为毫秒或微秒。（参见 [通用 API 信息](/zh-CN/docs/products/spot/web-socket-api#general-api-information)）
  * 另一个可选参数 `recvWindow`，用以指定请求的有效期，只能以毫秒为单位。
    * `recvWindow` 扩展为三位小数（例如 6000.346），以便可以指定微秒。
    * 如果未发送 `recvWindow`，则 **默认为 5000 毫秒** 。
    * `recvWindow` 的最大值为 60000 毫秒。
  * 请求处理逻辑如下：


    
    
    Code
    
    serverTime = getCurrentTime()
    if (timestamp < (serverTime + 1 second) && (serverTime - timestamp) <= recvWindow) {
      // 开始处理请求
      serverTime = getCurrentTime()
      if (serverTime - timestamp) <= recvWindow {
        // 将请求转发到撮合引擎
      } else {
        // 拒绝请求
      }
      // 结束处理请求
    } else {
      // 拒绝请求
    }

**关于交易时效性** 互联网状况并不完全稳定可靠，因此你的程序本地到币安服务器的时延会有抖动, 这是我们设置 `recvWindow` 的目所在。如果你从事高频交易，对交易时效性有较高的要求，可以灵活设置 `recvWindow` 以达到你的要求。

**建议使用5000毫秒以下的`recvWindow`！**

### `SIGNED` 请求示例 (HMAC)

这是有关如何用一个 HMAC secret key 签署请求的分步指南。

示例 API key 和 secret key：

Key| Value  
---|---  
`apiKey`| `vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A`  
`secretKey`| `NhqPtmdSJYdKjVHjA7PZj4Mge3R5YNiP1e3UZjInClVN65XAbvqqM6A7H5fATj0j`  
  
**警告：请勿与任何人分享您的 API 密钥和秘钥。**

此处提供的示例密钥仅用于示范说明目的。

交易对名称完全由 ASCII 字符组成的请求示例：

请求示例：
    
    
    Code
    
    {
      "id": "4885f793-e5ad-4c3b-8f6c-55d891472b71",
      "method": "order.place",
      "params": {
        "symbol": "BTCUSDT",
        "side": "SELL",
        "type": "LIMIT",
        "timeInForce": "GTC",
        "quantity": "0.01000000",
        "price": "52000.00",
        "newOrderRespType": "ACK",
        "recvWindow": 100,
        "timestamp": 1645423376532,
        "apiKey": "vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A",
        "signature": "------ 未填写 ------"
      }
    }

交易对名称包含非 ASCII 字符的请求示例：
    
    
    Code
    
    {
      "id": "4885f793-e5ad-4c3b-8f6c-55d891472b71",
      "method": "order.place",
      "params": {
        "symbol": "１２３４５６",
        "side": "BUY",
        "type": "LIMIT",
        "timeInForce": "GTC",
        "quantity": "0.01000000",
        "price": "0.10000000",
        "recvWindow": 5000,
        "timestamp": 1645423376532,
        "apiKey": "4yNzx3yWC5bS6YTwEkSRaC0nRmSQIIStAUOh1b6kqaBrTLIhjCpI5lJH8q8R8WNO",
        "signature": "------ FILL ME ------"
      }
    }

**第一步：创建签名内容**

除了 `signature` 之外，获取所有请求 `params`，然后**按参数名称的字母顺序对它们进行排序** ：

对于第一组示例参数（仅限 ASCII 字符）：

参数| 取值  
---|---  
`apiKey`| vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A  
`price`| 52000.00  
`quantity`| 0.01000000  
`recvWindow`| 100  
`side`| SELL  
`symbol`| BTCUSDT  
`timeInForce`| GTC  
`timestamp`| 1645423376532  
`type`| LIMIT  
  
对于第二组示例参数（包含一些 Unicode 字符）：

参数| 取值  
---|---  
`apiKey`| vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A  
`price`| 0.10000000  
`quantity`| 1.00000000  
`recvWindow`| 5000  
`side`| BUY  
`symbol`| １２３４５６  
`timeInForce`| GTC  
`timestamp`| 1645423376532  
`type`| LIMIT  
  
将参数格式化为 `参数=取值` 对并用 `&` 分隔每个参数对。数值需要采用 UTF-8 编码。

对于第一组示例参数（仅限 ASCII 字符），签名有效负载将如下所示：
    
    
    Code
    
    apiKey=vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A&price=52000.00&quantity=0.01000000&recvWindow=100&side=SELL&symbol=BTCUSDT&timeInForce=GTC&timestamp=1645423376532&type=LIMIT

对于第二组示例参数（包含一些 Unicode 字符），签名有效负载将如下所示：
    
    
    Code
    
    apiKey=vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A&price=0.10000000&quantity=1.00000000&recvWindow=5000&side=BUY&symbol=１２３４５６&timeInForce=GTC&timestamp=1645423376532&type=LIMIT

**第二步：计算签名**

  1. 使用 API 密钥中的 `secretKey` 作为 HMAC-SHA-256 算法的签名密钥。
  2. 对步骤 1 中构建的签名 payload 进行签名。
  3. 将 HMAC-SHA-256 的输出编码为十六进制字符串。



请注意，`apiKey`、`secretKey` 和有效负载是**大小写敏感的** 。而生成的签名值是不区分大小写的。

可以使用 OpenSSL 交叉检查您的签名算法实现：

对于第一组示例参数（仅限 ASCII 字符）：
    
    
    Code
    
    $ echo -n 'apiKey=vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A&price=52000.00&quantity=0.01000000&recvWindow=100&side=SELL&symbol=BTCUSDT&timeInForce=GTC&timestamp=1645423376532&type=LIMIT' \
      | openssl dgst -hex -sha256 -hmac 'NhqPtmdSJYdKjVHjA7PZj4Mge3R5YNiP1e3UZjInClVN65XAbvqqM6A7H5fATj0j'
    
    aa1b5712c094bc4e57c05a1a5c1fd8d88dcd628338ea863fec7b88e59fe2db24

对于第二组示例参数（包含一些 Unicode 字符）：
    
    
    Code
    
    $ echo -n 'apiKey=vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A&price=0.10000000&quantity=1.00000000&recvWindow=5000&side=BUY&symbol=１２３４５６&timeInForce=GTC&timestamp=1645423376532&type=LIMIT' \
      | openssl dgst -hex -sha256 -hmac 'NhqPtmdSJYdKjVHjA7PZj4Mge3R5YNiP1e3UZjInClVN65XAbvqqM6A7H5fATj0j'
    
    b33892ae8e687c939f4468c6268ddd4c40ac1af18ad19a064864c47bae0752cd

**第三步：添加`signature` 到 `params` 中**

通过在对请求中添加 `signature` 参数和签名字串来完成请求。

对于第一组示例参数（仅限 ASCII 字符）：
    
    
    Code
    
    {
      "id": "4885f793-e5ad-4c3b-8f6c-55d891472b71",
      "method": "order.place",
      "params": {
        "symbol": "BTCUSDT",
        "side": "SELL",
        "type": "LIMIT",
        "timeInForce": "GTC",
        "quantity": "0.01000000",
        "price": "52000.00",
        "recvWindow": 100,
        "timestamp": 1645423376532,
        "apiKey": "vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A",
        "signature": "aa1b5712c094bc4e57c05a1a5c1fd8d88dcd628338ea863fec7b88e59fe2db24"
      }
    }

对于第二组示例参数（包含一些 Unicode 字符）：
    
    
    Code
    
    {
      "id": "4885f793-e5ad-4c3b-8f6c-55d891472b71",
      "method": "order.place",
      "params": {
        "symbol": "１２３４５６",
        "side": "BUY",
        "type": "LIMIT",
        "timeInForce": "GTC",
        "quantity": "1.00000000",
        "price": "0.10000000",
        "recvWindow": 5000,
        "timestamp": 1645423376532,
        "apiKey": "vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A",
        "signature": "b33892ae8e687c939f4468c6268ddd4c40ac1af18ad19a064864c47bae0752cd"
      }
    }

### `SIGNED` 请求示例 (RSA)

这是有关如何用一个 RSA private key 签署请求的分步指南。

Key| Value  
---|---  
`apiKey`| `CAvIjXy3F44yW6Pou5k8Dy1swsYDWJZLeoK2r8G4cFDnE9nosRppc2eKc1T8TRTQ`  
  
这些示例假设私钥存储在文件 `test-prv-key.pem` 中。

**警告：请勿与任何人分享您的 API 密钥和私钥。**

此处提供的示例密钥仅用于示范说明目的。

交易对名称完全由 ASCII 字符组成的请求示例：
    
    
    Code
    
    {
      "id": "4885f793-e5ad-4c3b-8f6c-55d891472b71",
      "method": "order.place",
      "params": {
        "symbol": "BTCUSDT",
        "side": "SELL",
        "type": "LIMIT",
        "timeInForce": "GTC",
        "quantity": "0.01000000",
        "price": "52000.00",
        "recvWindow": 100,
        "timestamp": 1645423376532,
        "apiKey": "CAvIjXy3F44yW6Pou5k8Dy1swsYDWJZLeoK2r8G4cFDnE9nosRppc2eKc1T8TRTQ",
        "signature": "------ FILL ME ------"
      }
    }

交易对名称包含非 ASCII 字符的请求示例：
    
    
    Code
    
    {
      "id": "4885f793-e5ad-4c3b-8f6c-55d891472b71",
      "method": "order.place",
      "params": {
        "symbol": "１２３４５６",
        "side": "BUY",
        "type": "LIMIT",
        "timeInForce": "GTC",
        "quantity": "0.01000000",
        "price": "0.10000000",
        "recvWindow": 5000,
        "timestamp": 1645423376532,
        "apiKey": "CAvIjXy3F44yW6Pou5k8Dy1swsYDWJZLeoK2r8G4cFDnE9nosRppc2eKc1T8TRTQ",
        "signature": "------ FILL ME ------"
      }
    }

**第一步：创建签名内容**

除了 `signature`，获取请求的所有其它 `params`，然后**按参数名称的字母顺序对它们进行排序** ：

对于第一组示例参数（仅限 ASCII 字符）：

参数| 取值  
---|---  
`apiKey`| CAvIjXy3F44yW6Pou5k8Dy1swsYDWJZLeoK2r8G4cFDnE9nosRppc2eKc1T8TRTQ  
`price`| 52000.00  
`quantity`| 0.01000000  
`recvWindow`| 100  
`side`| SELL  
`symbol`| BTCUSDT  
`timeInForce`| GTC  
`timestamp`| 1645423376532  
`type`| LIMIT  
  
对于第二组示例参数（包含一些 Unicode 字符）：

参数| 取值  
---|---  
`apiKey`| CAvIjXy3F44yW6Pou5k8Dy1swsYDWJZLeoK2r8G4cFDnE9nosRppc2eKc1T8TRTQ  
`price`| 0.10000000  
`quantity`| 1.00000000  
`recvWindow`| 5000  
`side`| BUY  
`symbol`| １２３４５６  
`timeInForce`| GTC  
`timestamp`| 1645423376532  
`type`| LIMIT  
  
将参数格式化为 `参数=取值` 对并用 `&` 分隔每个参数对。数值需要采用 UTF-8 编码。

对于第一组示例参数（仅限 ASCII 字符），签名有效负载将如下所示：
    
    
    Code
    
    apiKey=CAvIjXy3F44yW6Pou5k8Dy1swsYDWJZLeoK2r8G4cFDnE9nosRppc2eKc1T8TRTQ&price=52000.00&quantity=0.01000000&recvWindow=100&side=SELL&symbol=BTCUSDT&timeInForce=GTC&timestamp=1645423376532&type=LIMIT

对于第二组示例参数（包含一些 Unicode 字符），签名有效负载将如下所示：
    
    
    Code
    
    apiKey=CAvIjXy3F44yW6Pou5k8Dy1swsYDWJZLeoK2r8G4cFDnE9nosRppc2eKc1T8TRTQ&price=0.10000000&quantity=1.00000000&recvWindow=5000&side=BUY&symbol=１２３４５６&timeInForce=GTC&timestamp=1645423376532&type=LIMIT

**第二步：计算签名**

  1. 使用 RSASSA-PKCS1-v1_5 算法和 SHA-256 哈希函数对步骤 1 中构造的签名有效载荷的 UTF-8 字节进行签名。
  2. 将输出编码为 base64。



请注意，`apiKey`, payload 和生成的`签名值`都是**大小写敏感** 的。

您可以使用 OpenSSL 交叉检查您的签名算法：

对于第一组示例参数（仅限 ASCII 字符）：
    
    
    Code
    
    $ echo -n 'apiKey=CAvIjXy3F44yW6Pou5k8Dy1swsYDWJZLeoK2r8G4cFDnE9nosRppc2eKc1T8TRTQ&price=52000.00&quantity=0.01000000&recvWindow=100&side=SELL&symbol=BTCUSDT&timeInForce=GTC&timestamp=1645423376532&type=LIMIT' \
      | openssl dgst -sha256 -sign test-rsa-prv.pem \
      | openssl enc -base64 -A
    
    OJJaf8C/3VGrU4ATTR4GiUDqL2FboSE1Qw7UnnoYNfXTXHubIl1iaePGuGyfct4NPu5oVEZCH4Q6ZStfB1w4ssgu0uiB/Bg+fBrRFfVgVaLKBdYHMvT+ljUJzqVaeoThG9oXlduiw8PbS9U8DYAbDvWN3jqZLo4Z2YJbyovyDAvDTr/oC0+vssLqP7NmlNb3fF3Bj7StmOwJvQJTbRAtzxK5PP7OQe+0mbW+D7RqVkUiSswR8qJFWTeSe4nXXNIdZdueYhF/Xf25L+KitJS5IHdIHcKfEw3MQzHFb2ZsGWkjDQwxkwr7Noi0Zaa+gFtxCuatGFm9dFIyx217pmSHtA==

对于第二组示例参数（包含一些 Unicode 字符）：
    
    
    Code
    
    $ echo -n 'apiKey=CAvIjXy3F44yW6Pou5k8Dy1swsYDWJZLeoK2r8G4cFDnE9nosRppc2eKc1T8TRTQ&price=0.10000000&quantity=1.00000000&recvWindow=5000&side=BUY&symbol=１２３４５６&timeInForce=GTC&timestamp=1645423376532&type=LIMIT' \
      | openssl dgst -sha256 -sign test-rsa-prv.pem \
      | openssl enc -base64 -A
    
    F3o/79Ttvl2cVYGPfBOF3oEOcm5QcYmTYWpdVIrKve5u+8paMNDAdUE+teqMxFM9HcquetGcfuFpLYtsQames5bDx/tskGM76TWW8HaM+6tuSYBSFLrKqChfA9hQGLYGjAiflf1YBnDhY+7vNbJFusUborNOloOj+ufzP5q42PvI3H0uNy3W5V3pyfXpDGCBtfCYYr9NAqA4d+AQfyllL/zkO9h9JSdozN49t0/hWGoD2dWgSO0Je6MytKEvD4DQXGeqNlBTB6tUXcWnRW+FcaKZ4KYqnxCtb1u8rFXUYgFykr2CbcJLSmw6ydEJ3EZ/NaZopRr+cU0W2m0HZ3qucw==

**第三步：在请求的`params` 参数添加签名值**

通过在对请求中添加 `signature` 参数和签名字串来完成请求。

对于第一组示例参数（仅限 ASCII 字符）：
    
    
    Code
    
    {
      "id": "4885f793-e5ad-4c3b-8f6c-55d891472b71",
      "method": "order.place",
      "params": {
        "symbol": "BTCUSDT",
        "side": "SELL",
        "type": "LIMIT",
        "timeInForce": "GTC",
        "quantity": "0.01000000",
        "price": "52000.00",
        "newOrderRespType": "ACK",
        "recvWindow": 100,
        "timestamp": 1645423376532,
        "apiKey": "CAvIjXy3F44yW6Pou5k8Dy1swsYDWJZLeoK2r8G4cFDnE9nosRppc2eKc1T8TRTQ",
        "signature": "OJJaf8C/3VGrU4ATTR4GiUDqL2FboSE1Qw7UnnoYNfXTXHubIl1iaePGuGyfct4NPu5oVEZCH4Q6ZStfB1w4ssgu0uiB/Bg+fBrRFfVgVaLKBdYHMvT+ljUJzqVaeoThG9oXlduiw8PbS9U8DYAbDvWN3jqZLo4Z2YJbyovyDAvDTr/oC0+vssLqP7NmlNb3fF3Bj7StmOwJvQJTbRAtzxK5PP7OQe+0mbW+D7RqVkUiSswR8qJFWTeSe4nXXNIdZdueYhF/Xf25L+KitJS5IHdIHcKfEw3MQzHFb2ZsGWkjDQwxkwr7Noi0Zaa+gFtxCuatGFm9dFIyx217pmSHtA=="
      }
    }

对于第二组示例参数（包含一些 Unicode 字符）：
    
    
    Code
    
    {
      "id": "4885f793-e5ad-4c3b-8f6c-55d891472b71",
      "method": "order.place",
      "params": {
        "symbol": "１２３４５６",
        "side": "SELL",
        "type": "LIMIT",
        "timeInForce": "GTC",
        "quantity": "1.00000000",
        "price": "0.10000000",
        "recvWindow": 5000,
        "timestamp": 1645423376532,
        "apiKey": "CAvIjXy3F44yW6Pou5k8Dy1swsYDWJZLeoK2r8G4cFDnE9nosRppc2eKc1T8TRTQ",
        "signature": "F3o/79Ttvl2cVYGPfBOF3oEOcm5QcYmTYWpdVIrKve5u+8paMNDAdUE+teqMxFM9HcquetGcfuFpLYtsQames5bDx/tskGM76TWW8HaM+6tuSYBSFLrKqChfA9hQGLYGjAiflf1YBnDhY+7vNbJFusUborNOloOj+ufzP5q42PvI3H0uNy3W5V3pyfXpDGCBtfCYYr9NAqA4d+AQfyllL/zkO9h9JSdozN49t0/hWGoD2dWgSO0Je6MytKEvD4DQXGeqNlBTB6tUXcWnRW+FcaKZ4KYqnxCtb1u8rFXUYgFykr2CbcJLSmw6ydEJ3EZ/NaZopRr+cU0W2m0HZ3qucw=="
      }
    }

### `SIGNED` 请求示例 (Ed25519)

**我们强烈建议使用 Ed25519 API keys，因为它在所有受支持的 API key 类型中提供最佳性能和安全性。**

这是有关如何用一个 Ed25519 private key 签署请求的分步指南。

Key| Value  
---|---  
`apiKey`| `4yNzx3yWC5bS6YTwEkSRaC0nRmSQIIStAUOh1b6kqaBrTLIhjCpI5lJH8q8R8WNO`  
  
这些示例假设私钥存储在文件 `test-ed25519-prv.pem` 中。

**警告：请勿与任何人分享您的 API 密钥和私钥。**

此处提供的示例密钥仅用于示范说明目的。

交易对名称完全由 ASCII 字符组成的请求示例：
    
    
    Code
    
    {
      "id": "4885f793-e5ad-4c3b-8f6c-55d891472b71",
      "method": "order.place",
      "params": {
        "symbol": "BTCUSDT",
        "side": "SELL",
        "type": "LIMIT",
        "timeInForce": "GTC",
        "quantity": "0.01000000",
        "price": "52000.00",
        "recvWindow": 100,
        "timestamp": 1645423376532,
        "apiKey": "4yNzx3yWC5bS6YTwEkSRaC0nRmSQIIStAUOh1b6kqaBrTLIhjCpI5lJH8q8R8WNO",
        "signature": "------ FILL ME ------"
      }
    }

交易对名称包含非 ASCII 字符的请求示例：
    
    
    Code
    
    {
      "id": "4885f793-e5ad-4c3b-8f6c-55d891472b71",
      "method": "order.place",
      "params": {
        "symbol": "１２３４５６",
        "side": "BUY",
        "type": "LIMIT",
        "timeInForce": "GTC",
        "quantity": "0.01000000",
        "price": "0.10000000",
        "recvWindow": 5000,
        "timestamp": 1645423376532,
        "apiKey": "4yNzx3yWC5bS6YTwEkSRaC0nRmSQIIStAUOh1b6kqaBrTLIhjCpI5lJH8q8R8WNO",
        "signature": "------ FILL ME ------"
      }
    }

**第一步：创建签名内容**

除了 `signature`，获取请求的所有其它 `params`，然后**按参数名称的字母顺序对它们进行排序** ：

对于第一组示例参数（仅限 ASCII 字符）：

参数| 取值  
---|---  
`apiKey`| 4yNzx3yWC5bS6YTwEkSRaC0nRmSQIIStAUOh1b6kqaBrTLIhjCpI5lJH8q8R8WNO  
`price`| 52000.00  
`quantity`| 0.01000000  
`recvWindow`| 100  
`side`| SELL  
`symbol`| BTCUSDT  
`timeInForce`| GTC  
`timestamp`| 1645423376532  
`type`| LIMIT  
  
对于第二组示例参数（包含一些 Unicode 字符）：

参数| 取值  
---|---  
`apiKey`| 4yNzx3yWC5bS6YTwEkSRaC0nRmSQIIStAUOh1b6kqaBrTLIhjCpI5lJH8q8R8WNO  
`price`| 0.20000000  
`quantity`| 1.00000000  
`recvWindow`| 5000  
`side`| SELL  
`symbol`| １２３４５６  
`timeInForce`| GTC  
`timestamp`| 1668481559918  
`type`| LIMIT  
  
将参数格式化为 `参数=取值` 对并用 `&` 分隔每个参数对。数值需要采用 UTF-8 编码。

对于第一组示例参数（仅限 ASCII 字符），签名有效负载将如下所示：
    
    
    Code
    
    apiKey=4yNzx3yWC5bS6YTwEkSRaC0nRmSQIIStAUOh1b6kqaBrTLIhjCpI5lJH8q8R8WNO&price=52000.00&quantity=0.01000000&recvWindow=100&side=SELL&symbol=BTCUSDT&timeInForce=GTC&timestamp=1645423376532&type=LIMIT

对于第二组示例参数（包含一些 Unicode 字符），签名有效负载将如下所示：
    
    
    Code
    
    apiKey=4yNzx3yWC5bS6YTwEkSRaC0nRmSQIIStAUOh1b6kqaBrTLIhjCpI5lJH8q8R8WNO&price=0.10000000&quantity=1.00000000&recvWindow=5000&side=BUY&symbol=１２３４５６&timeInForce=GTC&timestamp=1645423376532&type=LIMIT

**第二步：计算签名**

  1. 使用 Ed25519 密钥对步骤 1 中构造的签名有效载荷的 UTF-8 字节进行签名。
  2. 将输出编码为 base64。



请注意，`apiKey`, payload 和生成的`签名值`都是**大小写敏感** 的。

您可以使用 OpenSSL 交叉检查您的签名算法：

对于第一组示例参数（仅限 ASCII 字符）：
    
    
    Code
    
    echo -n "apiKey=4yNzx3yWC5bS6YTwEkSRaC0nRmSQIIStAUOh1b6kqaBrTLIhjCpI5lJH8q8R8WNO&price=52000.00&quantity=0.01000000&recvWindow=100&side=SELL&symbol=BTCUSDT&timeInForce=GTC&timestamp=1645423376532&type=LIMIT" \
      | openssl dgst -sign ./test-ed25519-prv.pem \
      | openssl enc -base64 -A
    
    EocljwPl29jDxWYaaRaOo4pJ9wEblFbklJvPugNscLLuKd5vHM2grWjn1z+rY0aJ7r/44enxHL6mOAJuJ1kqCg==

对于第二组示例参数（包含一些 Unicode 字符）：
    
    
    Code
    
    echo -n "apiKey=4yNzx3yWC5bS6YTwEkSRaC0nRmSQIIStAUOh1b6kqaBrTLIhjCpI5lJH8q8R8WNO&price=0.10000000&quantity=1.00000000&recvWindow=5000&side=BUY&symbol=１２３４５６&timeInForce=GTC&timestamp=1645423376532&type=LIMIT" \
      | openssl dgst -sign ./test-ed25519-prv.pem \
      | openssl enc -base64 -A
    
    dtNHJeyKry+cNjiGv+sv5kynO9S40tf8k7D5CfAEQAp0s2scunZj+ovJdz2OgW8XhkB9G3/HmASkA9uY9eyFCA==

**第三步：在请求的`params` 参数添加签名值**

对于第一组示例参数（仅限 ASCII 字符）：
    
    
    Code
    
    {
      "id": "4885f793-e5ad-4c3b-8f6c-55d891472b71",
      "method": "order.place",
      "params": {
        "symbol": "BTCUSDT",
        "side": "SELL",
        "type": "LIMIT",
        "timeInForce": "GTC",
        "quantity": "0.01000000",
        "price": "52000.00",
        "newOrderRespType": "ACK",
        "recvWindow": 100,
        "timestamp": 1645423376532,
        "apiKey": "4yNzx3yWC5bS6YTwEkSRaC0nRmSQIIStAUOh1b6kqaBrTLIhjCpI5lJH8q8R8WNO",
        "signature": "EocljwPl29jDxWYaaRaOo4pJ9wEblFbklJvPugNscLLuKd5vHM2grWjn1z+rY0aJ7r/44enxHL6mOAJuJ1kqCg=="
      }
    }

对于第二组示例参数（包含一些 Unicode 字符）：
    
    
    Code
    
    {
      "id": "4885f793-e5ad-4c3b-8f6c-55d891472b71",
      "method": "order.place",
      "params": {
        "symbol": "１２３４５６",
        "side": "SELL",
        "type": "LIMIT",
        "timeInForce": "GTC",
        "quantity": "1.00000000",
        "price": "0.10000000",
        "recvWindow": 5000,
        "timestamp": 1645423376532,
        "apiKey": "4yNzx3yWC5bS6YTwEkSRaC0nRmSQIIStAUOh1b6kqaBrTLIhjCpI5lJH8q8R8WNO",
        "signature": "dtNHJeyKry+cNjiGv+sv5kynO9S40tf8k7D5CfAEQAp0s2scunZj+ovJdz2OgW8XhkB9G3/HmASkA9uY9eyFCA=="
      }
    }

下面的 Python 示例代码能执行上述所有步骤。
    
    
    Code
    
    #!/usr/bin/env python3
    
    import base64
    import time
    import json
    from cryptography.hazmat.primitives.serialization import load_pem_private_key
    from websocket import create_connection
    
    # 设置身份验证：
    API_KEY='替换成您的 API Key'
    PRIVATE_KEY_PATH='test-prv-key.pem'
    
    # 加载 private key。
    # 在这个例子中，private key 没有加密
    # 但我们建议使用强密码以提高安全性。
    with open(PRIVATE_KEY_PATH, 'rb') as f:
      private_key = load_pem_private_key(data=f.read(), password=None)
    
    # 设置请求参数：
    params = {
        'apiKey':       API_KEY,
        'symbol':       '１２３４５６',
        'side':         'SELL',
        'type':         'LIMIT',
        'timeInForce':  'GTC',
        'quantity':     '1.0000000',
        'price':        '0.10000000',
        'recvWindow':   5000
    }
    
    # 参数中加时间戳：
    timestamp = int(time.time() * 1000) # UNIX timestamp in milliseconds
    params['timestamp'] = timestamp
    
    # 按参数名称的字母顺序进行排序
    params = dict(sorted(params.items()))
    
    # 计算签名有效负载
    payload = '&'.join([f"{k}={v}" for k,v in params.items()]) # no percent encoding here!
    
    # 对请求进行签名
    signature = base64.b64encode(private_key.sign(payload.encode('UTF-8')))
    params['signature'] = signature.decode('ASCII')
    
    # 发送请求：
    request = {
        'id': 'my_new_order',
        'method': 'order.place',
        'params': params
    }
    
    ws = create_connection("wss://ws-api.binance.com:443/ws-api/v3")
    ws.send(json.dumps(request))
    result =  ws.recv()
    ws.close()
    
    print(result)

## 会话身份验证

**注意：** 仅支持 _Ed25519_ 密钥用于此功能。

如果你不想在每个单独的请求中指定`apiKey`和`signature`，你可以为有效的WebSocket会话进行API密钥身份验证。

一旦完成身份验证，你将不需在需要它们的请求中指定`apiKey`和`signature`。这些请求将代表拥有已验证API密钥的帐户执行。

**注意：** 对于`SIGNED`请求，你仍需要指定`timestamp`参数。

### 连接后进行身份验证

你可以使用会话身份验证请求对已经建立的连接进行身份验证：

  * [`session.logon`](/zh-CN/docs/catalog/core-trading-spot-trading/api/ws-api/auth#session-logon) – 进行身份验证，或更改与连接相关联的API密钥。
  * [`session.status`](/zh-CN/docs/catalog/core-trading-spot-trading/api/ws-api/auth#session-status) – 检查连接状态和当前API密钥。
  * [`session.logout`](/zh-CN/docs/catalog/core-trading-spot-trading/api/ws-api/auth#session-logout) – 忘记与连接关联的API密钥。



**关于吊销API密钥:**

如果在活动会话期间，由于 _任何_ 原因（例如IP地址未被加入白名单、API密钥被删除、API密钥没有正确的权限等），在下一个请求后，会话将被吊销，并显示以下错误消息:
    
    
    Code
    
    {
        "id": null,
        "status": 401,
        "error": {
            "code": -2015,
            "msg": "Invalid API-key, IP, or permissions for action."
        }
    }

### 授权 _临时_ 请求

WebSocket连接只能通过一个API密钥进行身份验证。默认情况下，经过身份验证的API密钥将用于需要`apiKey`参数的请求。但是，你始终可以为单个请求明确指定`apiKey`和`signature`，覆盖已认证的API密钥，以使用不同的API密钥授权特定请求。

例如，你可能希望用默认密钥来验证 `USER_DATA`，但在下单时使用`TRADE`密钥来签名。

## 数据源

  * API 系统是异步的。响应中一些延迟是正常和预期的。

  * 每种函数都会有一个数据源, 用来指示数据的来源，以及它的最新程度。


数据源| 延迟| 描述  
---|---|---  
撮合引擎| 最低| 表示撮合引擎直接产生响应  
缓存| 低| 表示数据来源于内部或者外部的缓存  
数据库| 中度| 表示数据直接来源于数据库  
  
  * 某些函数有多个数据源（例如，缓存 => 数据库）。

这代表 API 将按该顺序查找最新数据：首先是缓存，然后是数据库。




此页面是否有帮助？

Last modified on November 12, 2026

[REST API](/zh-CN/docs/products/spot/rest-api)[WebSocket 流信息](/zh-CN/docs/products/spot/web-socket-streams)