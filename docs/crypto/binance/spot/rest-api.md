---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/spot/rest-api
api_type: REST
updated_at: 2026-11-13 20:24:41.694557
---

# General REST API Information

## General API Information

  * The following base endpoints are available. Please use whichever works best for your setup:
    * **<https://api.binance.com>**
    * **<https://api-gcp.binance.com>**
    * **<https://api1.binance.com>**
    * **<https://api2.binance.com>**
    * **<https://api3.binance.com>**
    * **<https://api4.binance.com>**
  * The last 4 endpoints in the point above (`api1`-`api4`) should give better performance but have less stability.
  * Responses are in JSON by default. To receive responses in SBE, refer to the [SBE FAQ](/en/docs/products/spot/faqs/sbe_faq) page.
  * Data is returned in **chronological order** , unless noted otherwise.
    * Without `startTime` or `endTime`, returns the most recent items up to the limit.
    * With `startTime`, returns oldest items from `startTime` up to the limit.
    * With `endTime`, returns most recent items up to `endTime` and the limit.
    * With both, behaves like `startTime` but does not exceed `endTime`.
  * All time and timestamp related fields in the JSON responses are in **milliseconds by default.** To receive the information in microseconds, please add the header `X-MBX-TIME-UNIT:MICROSECOND` or `X-MBX-TIME-UNIT:microsecond`.
  * We support HMAC, RSA, and Ed25519 keys. For more information, please see [API Key types](/en/docs/products/spot/faqs/api_key_types).
  * Timestamp parameters (e.g. `startTime`, `endTime`, `timestamp`) can be passed in milliseconds or microseconds.
  * For APIs that only send public market data, please use the base endpoint **<https://data-api.binance.vision>**. Please refer to [Market Data Only](/en/docs/products/spot/faqs/market_data_only) page.
  * If there are enums or terms you want clarification on, please see the [SPOT Glossary](/en/docs/products/spot/faqs/spot_glossary) for more information.
  * APIs have a timeout of 10 seconds when processing a request. If a response from the Matching Engine takes longer than this, the API responds with "Timeout waiting for response from backend server. Send status unknown; execution status unknown." [(-1007 TIMEOUT)](/en/docs/products/spot/errors#-1007-timeout)
    * This does not always mean that the request failed in the Matching Engine.
    * If the status of the request has not appeared in [User Data Stream](/en/docs/products/spot/user-data-stream), please perform an API query for its status.
  * **Please avoid SQL keywords in requests** as they may trigger a security block by a WAF (Web Application Firewall) rule. See <https://www.binance.com/en/support/faq/detail/360004492232> for more details.
  * If your request contains a symbol name containing non-ASCII characters, then the response may contain non-ASCII characters encoded in UTF-8.
  * Some endpoints may return asset and/or symbol names containing non-ASCII characters encoded in UTF-8 even if the request did not contain non-ASCII characters.



## HTTP Return Codes

  * HTTP `4XX` return codes are used for malformed requests; the issue is on the sender's side.
  * HTTP `403` return code is used when a WAF (Web Application Firewall) rule has been violated. This can indicate a rate limit violation or a security block. See <https://www.binance.com/en/support/faq/detail/360004492232> for more details.
  * HTTP `409` return code is used when a cancelReplace order partially succeeds. (i.e. if the cancellation of the order fails but the new order placement succeeds.)
  * HTTP `429` return code is used when breaking a request rate limit.
  * HTTP `418` return code is used when an IP has been auto-banned for continuing to send requests after receiving `429` codes.
  * HTTP `5XX` return codes are used for internal errors; the issue is on Binance's side. It is important to **NOT** treat this as a failure operation; the execution status is **UNKNOWN** and could have been a success.



## Error Codes

  * Any endpoint can return an ERROR



Sample Payload below:
    
    
    Code
    
    {
        "code": -1121,
        "msg": "Invalid symbol."
    }

  * Specific error codes and messages are defined in [Errors Codes](/en/docs/products/spot/errors).



## General Information on Endpoints

  * For `GET` endpoints, parameters must be sent as a `query string`.
  * For `POST`, `PUT`, and `DELETE` endpoints, the parameters may be sent as a `query string` or in the `request body` with content type `application/x-www-form-urlencoded`. You may mix parameters between both the `query string` and `request body` if you wish to do so.
  * Parameters may be sent in any order.
  * If a parameter sent in both the `query string` and `request body`, the `query string` parameter will be used.



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
  
## LIMITS

### General Info on Limits

  * The following `intervalLetter` values for headers:
    * SECOND => S
    * MINUTE => M
    * HOUR => H
    * DAY => D
  * `intervalNum` describes the amount of the interval. For example, `intervalNum` 5 with `intervalLetter` M means "Every 5 minutes".
  * The `/api/v3/exchangeInfo` `rateLimits` array contains objects related to the exchange's `RAW_REQUESTS`, `REQUEST_WEIGHT`, and `ORDERS` rate limits. These are further defined in the `ENUM definitions` section under `Rate limiters (rateLimitType)`.
  * Requests fail with HTTP status code 429 when you exceed the request rate limit.



### IP Limits

  * Every request will contain `X-MBX-USED-WEIGHT-(intervalNum)(intervalLetter)` in the response headers which has the current used weight for the IP for all request rate limiters defined.
  * Each route has a `weight` which determines for the number of requests each endpoint counts for. Heavier endpoints and endpoints that do operations on multiple symbols will have a heavier `weight`.
  * When a 429 is received, it's your obligation as an API to back off and not spam the API.
  * **Repeatedly violating rate limits and/or failing to back off after receiving 429s will result in an automated IP ban (HTTP status 418).**
  * IP bans are tracked and **scale in duration** for repeat offenders, **from 2 minutes to 3 days**.
  * A `Retry-After` header is sent with a 418 or 429 responses and will give the **number of seconds** required to wait, in the case of a 429, to prevent a ban, or, in the case of a 418, until the ban is over.
  * **The limits on the API are based on the IPs, not the API keys.**



### Unfilled Order Count

  * Every successful order response will contain a `X-MBX-ORDER-COUNT-(intervalNum)(intervalLetter)` header indicating how many orders you have placed for that interval.  To monitor this, refer to [`GET api/v3/rateLimit/order`](/en/docs/catalog/core-trading-spot-trading/api/rest-api/account#rate-limit-order).
  * Rejected/unsuccessful orders are not guaranteed to have `X-MBX-ORDER-COUNT-**` headers in the response.
  * If you have exceeded this, you will receive a 429 error with the `Retry-After` header.
  * **Please note that if your orders are consistently filled by trades, you can continuously place orders on the API**. For more information, please see [Spot Unfilled Order Count Rules](/en/docs/products/spot/faqs/order_count_decrement).
  * **The number of unfilled orders is tracked for each account.**



## Data Sources

  * The API system is asynchronous, so some delay in the response is normal and expected.
  * Each endpoint has a data source indicating where the data is being retrieved, and thus which endpoints have the most up-to-date response.



These are the three sources, ordered by least to most potential for delays in data updates.

  * **Matching Engine** \- the data is from the Matching Engine
  * **Memory** \- the data is from a server's local or external memory
  * **Database** \- the data is taken directly from a database



Some endpoints can have more than 1 data source. (e.g. Memory => Database) This means that the endpoint will check the first Data Source, and if it cannot find the value it's looking for it will check the next one.

## Request Security

  * Each endpoint has a security type indicating required API key permissions, shown next to the endpoint name (e.g., [New order (TRADE)](/en/docs/catalog/core-trading-spot-trading/api/rest-api/trade#new-order)).
  * If unspecified, the security type is `NONE`.
  * Except for `NONE`, all endpoints with a security type are considered `SIGNED` requests (i.e. including a `signature`).
  * Secure endpoints require a valid API key to be specified and authenticated.
    * API keys can be created on the [API Management](https://www.binance.com/en/support/faq/360002502072) page of your Binance account.
    * **Both API key and secret key are sensitive.** Never share them with anyone. If you notice unusual activity in your account, immediately revoke all the keys and contact Binance support.
  * API keys can be configured to allow access only to certain types of secure endpoints.
    * For example, you can have an API key with `TRADE` permission for trading, while using a separate API key with `USER_DATA` permission to monitor your order status.
    * By default, an API key cannot `TRADE`. You need to enable trading in API Management first.

Security type| Description  
---|---  
`NONE`| Public market data  
`TRADE`| Trading on the exchange, placing and canceling orders  
`USER_DATA`| Private account information, such as order status and your trading history  
`USER_STREAM`| Managing User Data Stream subscriptions  
  
### SIGNED Endpoint security

  * `SIGNED` endpoints require an additional parameter, `signature`, to be sent in the `query string` or `request body`.



#### Signature Case Sensitivity

  * **HMAC:** Signatures generated using HMAC are **not case-sensitive**. This means the signature string can be verified regardless of letter casing.
  * **RSA:** Signatures generated using RSA are **case-sensitive**.
  * **Ed25519:** Signatures generated using Ed25519 are also **case-sensitive**



Please consult [SIGNED request example (HMAC)](/en/docs/products/spot/rest-api#hmac-keys), [SIGNED request example (RSA)](/en/docs/products/spot/rest-api#rsa-keys), and [SIGNED request example (Ed25519)](/en/docs/products/spot/rest-api#ed25519-keys) on how to compute signature, depending on which API key type you are using.

### Timing security

  * `SIGNED` requests also require a `timestamp` parameter which should be the current timestamp either in milliseconds or microseconds. (See [General API Information](/en/docs/products/spot/rest-api#general-api-information))
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

**It is recommended to use a small recvWindow of 5000 or less! The max cannot go beyond 60,000!**

### SIGNED Endpoint Examples for POST /api/v3/order

#### HMAC Keys

The signature payload of your request is the query string concatenated without separator to the HTTP body. Any non-ASCII character must be percent-encoded before signing.

Here is a step-by-step example of how to send a valid signed payload from the Linux command line using `echo`, `openssl`, and `curl`. There is one example with a symbol name comprised entirely of ASCII characters and one example with a symbol name containing non-ASCII characters.

Example API key and secret key:

Key| Value  
---|---  
`apiKey`| vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A  
`secretKey`| NhqPtmdSJYdKjVHjA7PZj4Mge3R5YNiP1e3UZjInClVN65XAbvqqM6A7H5fATj0j  
  
**WARNING: DO NOT SHARE YOUR API KEY AND SECRET KEY WITH ANYONE.**

The example keys are provided here only for illustrative purposes.

Example of request with a symbol name comprised entirely of ASCII characters:

Parameter| Value  
---|---  
`symbol`| LTCBTC  
`side`| BUY  
`type`| LIMIT  
`timeInForce`| GTC  
`quantity`| 1  
`price`| 0.1  
`recvWindow`| 5000  
`timestamp`| 1499827319559  
  
Example of a request with a symbol name containing non-ASCII characters:

Parameter| Value  
---|---  
`symbol`| １２３４５６  
`side`| BUY  
`type`| LIMIT  
`timeInForce`| GTC  
`quantity`| 1  
`price`| 0.1  
`recvWindow`| 5000  
`timestamp`| 1499827319559  
  
**Step 1: Construct the signature payload**

  1. Format parameters as `parameter=value` pairs separated by `&`.
  2. Percent-encode the string.



For the first set of example parameters (ASCII only), the `parameter=value` string should look like this:
    
    
    Code
    
    symbol=LTCBTC&side=BUY&type=LIMIT&timeInForce=GTC&quantity=1&price=0.1&recvWindow=5000&timestamp=1499827319559

After percent-encoding, the signature payload should look like this:
    
    
    Code
    
    symbol=LTCBTC&side=BUY&type=LIMIT&timeInForce=GTC&quantity=1&price=0.1&recvWindow=5000&timestamp=1499827319559

For the second set of example parameters (some non-ASCII characters), the `parameter=value` string should look like this:
    
    
    Code
    
    symbol=１２３４５６&side=BUY&type=LIMIT&timeInForce=GTC&quantity=1&price=0.1&recvWindow=5000&timestamp=1499827319559

After percent-encoding, the signature payload should look like this:
    
    
    Code
    
    symbol=%EF%BC%91%EF%BC%92%EF%BC%93%EF%BC%94%EF%BC%95%EF%BC%96&side=BUY&type=LIMIT&timeInForce=GTC&quantity=1&price=0.1&recvWindow=5000&timestamp=1499827319559

**Step 2: Compute the signature**

  1. Use the `secretKey` of your API key as the signing key for the HMAC-SHA-256 algorithm.
  2. Sign the signature payload constructed in Step 1.
  3. Encode the HMAC-SHA-256 output as a hex string.



Note that `secretKey` and the payload are **case-sensitive** , while the resulting signature value is case-insensitive.

**Example commands**

For the first set of example parameters (ASCII only):
    
    
    Code
    
    $ echo -n "symbol=LTCBTC&side=BUY&type=LIMIT&timeInForce=GTC&quantity=1&price=0.1&recvWindow=5000&timestamp=1499827319559" | openssl dgst -sha256 -hmac "NhqPtmdSJYdKjVHjA7PZj4Mge3R5YNiP1e3UZjInClVN65XAbvqqM6A7H5fATj0j"
    
    c8db56825ae71d6d79447849e617115f4a920fa2acdcab2b053c4b2838bd6b71

For the second set of example parameters (some non-ASCII characters):
    
    
    Code
    
    $ echo -n "symbol=%EF%BC%91%EF%BC%92%EF%BC%93%EF%BC%94%EF%BC%95%EF%BC%96&side=BUY&type=LIMIT&timeInForce=GTC&quantity=1&price=0.1&recvWindow=5000&timestamp=1499827319559" | openssl dgst -sha256 -hmac "NhqPtmdSJYdKjVHjA7PZj4Mge3R5YNiP1e3UZjInClVN65XAbvqqM6A7H5fATj0j"
    
    e1353ec6b14d888f1164ae9af8228a3dbd508bc82eb867db8ab6046442f33ef3

**Step 3: Add signature to the request**

Complete the request by adding the `signature` parameter to the query string.

For the first set of example parameters (ASCII only):
    
    
    Code
    
    curl -s -v -H "X-MBX-APIKEY: $apiKey" -X POST "https://api.binance.com/api/v3/order?symbol=LTCBTC&side=BUY&type=LIMIT&timeInForce=GTC&quantity=1&price=0.1&recvWindow=5000&timestamp=1499827319559&signature=c8db56825ae71d6d79447849e617115f4a920fa2acdcab2b053c4b2838bd6b71"

For the second set of example parameters (some non-ASCII characters)
    
    
    Code
    
    curl -s -v -H "X-MBX-APIKEY: $apiKey" -X POST "https://api.binance.com/api/v3/order?symbol=%EF%BC%91%EF%BC%92%EF%BC%93%EF%BC%94%EF%BC%95%EF%BC%96&side=BUY&type=LIMIT&timeInForce=GTC&quantity=1&price=0.1&recvWindow=5000&timestamp=1499827319559&signature=e1353ec6b14d888f1164ae9af8228a3dbd508bc82eb867db8ab6046442f33ef3"

Here is a sample Bash script performing all the steps above:
    
    
    Code
    
    apiKey="vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A"
    secretKey="NhqPtmdSJYdKjVHjA7PZj4Mge3R5YNiP1e3UZjInClVN65XAbvqqM6A7H5fATj0j"
    
    payload="symbol=LTCBTC&side=BUY&type=LIMIT&timeInForce=GTC&quantity=1&price=0.1&recvWindow=5000&timestamp=1499827319559"
    
    # Sign the request
    
    signature=$(echo -n "$payload" | openssl dgst -sha256 -hmac "$secretKey")
    signature=${signature#*= }    # Keep only the part after the "= "
    
    # Send the request
    
    curl -H "X-MBX-APIKEY: $apiKey" -X POST "https://api.binance.com/api/v3/order?$payload&signature=$signature"
    

#### RSA Keys

The signature payload of your request is the query string concatenated without separator to the HTTP body. Any non-ASCII character must be percent-encoded before signing.

To get your API key, you need to upload your RSA Public Key to your account and a corresponding API key will be provided for you.

Only `PKCS#8` keys are supported.

There is one example with a symbol name comprised entirely of ASCII characters and one example with a symbol name containing non-ASCII characters.

These examples assume the private key is stored in the file `./test-prv-key.pem`.

Key| Value  
---|---  
`apiKey`| CAvIjXy3F44yW6Pou5k8Dy1swsYDWJZLeoK2r8G4cFDnE9nosRppc2eKc1T8TRTQ  
  
Example of request with a symbol name comprised entirely of ASCII characters:

Parameter| Value  
---|---  
`symbol`| BTCUSDT  
`side`| SELL  
`type`| LIMIT  
`timeInForce`| GTC  
`quantity`| 1  
`price`| 0.2  
`timestamp`| 1668481559918  
`recvWindow`| 5000  
  
Example of a request with a symbol name containing non-ASCII characters:

Parameter| Value  
---|---  
`symbol`| １２３４５６  
`side`| SELL  
`type`| LIMIT  
`timeInForce`| GTC  
`quantity`| 1  
`price`| 0.2  
`timestamp`| 1668481559918  
`recvWindow`| 5000  
  
**Step 1: Construct the signature payload**

  1. Format parameters as `parameter=value` pairs separated by `&`.
  2. Percent-encode the string.



For the first set of example parameters (ASCII only), the `parameter=value` string should look like this:
    
    
    Code
    
    symbol=BTCUSDT&side=SELL&type=LIMIT&timeInForce=GTC&quantity=1&price=0.2&timestamp=1668481559918&recvWindow=5000

After percent-encoding, the signature payload should look like this:
    
    
    Code
    
    symbol=BTCUSDT&side=SELL&type=LIMIT&timeInForce=GTC&quantity=1&price=0.2&timestamp=1668481559918&recvWindow=5000

For the second set of example parameters (some non-ASCII characters), the `parameter=value` string should look like this:
    
    
    Code
    
    symbol=１２３４５６=SELL&type=LIMIT&timeInForce=GTC&quantity=1&price=0.2&timestamp=1668481559918&recvWindow=5000

After percent-encoding, the signature payload should look like this:
    
    
    Code
    
    symbol=%EF%BC%91%EF%BC%92%EF%BC%93%EF%BC%94%EF%BC%95%EF%BC%96&side=SELL&type=LIMIT&timeInForce=GTC&quantity=1&price=0.2&timestamp=1668481559918&recvWindow=5000

**Step 2: Compute the signature**

  1. Sign the signature payload constructed in Step 1 using the RSASSA-PKCS1-v1_5 algorithm with SHA-256 hash function.
  2. Encode the output in base64.



Note that the payload and the resulting `signature` are **case-sensitive**.

For the first set of example parameters (ASCII only):
    
    
    Code
    
    $  echo -n 'symbol=BTCUSDT&side=SELL&type=LIMIT&timeInForce=GTC&quantity=1&price=0.2&timestamp=1668481559918&recvWindow=5000' | openssl dgst -sha256 -sign ./test-prv-key.pem | openssl enc -base64 -A | tr -d '\n'
    HZ8HOjiJ1s/igS9JA+n7+7Ti/ihtkRF5BIWcPIEluJP6tlbFM/Bf44LfZka/iemtahZAZzcO9TnI5uaXh3++lrqtNonCwp6/245UFWkiW1elpgtVAmJPbogcAv6rSlokztAfWk296ZJXzRDYAtzGH0gq7CgSJKfH+XxaCmR0WcvlKjNQnp12/eKXJYO4tDap8UCBLuyxDnR7oJKLHQHJLP0r0EAVOOSIbrFang/1WOq+Jaq4Efc4XpnTgnwlBbWTmhWDR1pvS9iVEzcSYLHT/fNnMRxFc7u+j3qI//5yuGuu14KR0MuQKKCSpViieD+fIti46sxPTsjSemoUKp0oXA==

For the second set of example parameters (some non-ASCII characters):
    
    
    Code
    
    $  echo -n 'symbol=%EF%BC%91%EF%BC%92%EF%BC%93%EF%BC%94%EF%BC%95%EF%BC%96&side=SELL&type=LIMIT&timeInForce=GTC&quantity=1&price=0.2&timestamp=1668481559918&recvWindow=5000' | openssl dgst -sha256 -sign ./test-prv-key.pem | openssl enc -base64 -A | tr -d '\n'
    
    qJtv66wyp/1mZE+mIFAAMUoTe8xkmLN7/eAZjuC9x1ocxovItHLl/sNK7Wq8QjgiHqGn0bb8P7yVvGBEd1gFe71NQ8aM0M+JNIMz5UFxfeA53rXjFlvsyH1Sig+OuO9Nz5nhCaJ6bEfj2iuv7w27pB3L8MVqmoCi6D9C/QMiLxtPaR70CxtnvoOlIgPmpv2bQy029A31NEK19ieVLkoyp1EUkXRaX3v0mohx8yMnUG1dhX9nUg3Oy8TYZ03DQy7kHDGkMKisNX7rt/GuGx1HIgjFclDGLsbAFIodvSLjm9FbseasMELoxlAJDlwRnW8zo5sQmL0Fz7ao935QBynrng==

  3. Percent-encode the base64 string.



For the first set of example parameters (ASCII only):
    
    
    Code
    
    HZ8HOjiJ1s%2FigS9JA%2Bn7%2B7Ti%2FihtkRF5BIWcPIEluJP6tlbFM%2FBf44LfZka%2FiemtahZAZzcO9TnI5uaXh3%2B%2BlrqtNonCwp6%2F245UFWkiW1elpgtVAmJPbogcAv6rSlokztAfWk296ZJXzRDYAtzGH0gq7CgSJKfH%2BXxaCmR0WcvlKjNQnp12%2FeKXJYO4tDap8UCBLuyxDnR7oJKLHQHJLP0r0EAVOOSIbrFang%2F1WOq%2BJaq4Efc4XpnTgnwlBbWTmhWDR1pvS9iVEzcSYLHT%2FfNnMRxFc7u%2Bj3qI%2F%2F5yuGuu14KR0MuQKKCSpViieD%2BfIti46sxPTsjSemoUKp0oXA%3D%3D

For the second set of example parameters (some non-ASCII characters):
    
    
    Code
    
    qJtv66wyp%2F1mZE%2BmIFAAMUoTe8xkmLN7%2FeAZjuC9x1ocxovItHLl%2FsNK7Wq8QjgiHqGn0bb8P7yVvGBEd1gFe71NQ8aM0M%2BJNIMz5UFxfeA53rXjFlvsyH1Sig%2BOuO9Nz5nhCaJ6bEfj2iuv7w27pB3L8MVqmoCi6D9C%2FQMiLxtPaR70CxtnvoOlIgPmpv2bQy029A31NEK19ieVLkoyp1EUkXRaX3v0mohx8yMnUG1dhX9nUg3Oy8TYZ03DQy7kHDGkMKisNX7rt%2FGuGx1HIgjFclDGLsbAFIodvSLjm9FbseasMELoxlAJDlwRnW8zo5sQmL0Fz7ao935QBynrng%3D%3D

**Step 3: Add signature to the request**

Complete the request by adding the `signature` parameter to the query string.

For the first set of example parameters (ASCII only):
    
    
    Code
    
    curl -H "X-MBX-APIKEY: CAvIjXy3F44yW6Pou5k8Dy1swsYDWJZLeoK2r8G4cFDnE9nosRppc2eKc1T8TRTQ" -X POST 'https://api.binance.com/api/v3/order?symbol=BTCUSDT&side=SELL&type=LIMIT&timeInForce=GTC&quantity=1&price=0.2&timestamp=1668481559918&recvWindow=5000&signature=HZ8HOjiJ1s%2FigS9JA%2Bn7%2B7Ti%2FihtkRF5BIWcPIEluJP6tlbFM%2FBf44LfZka%2FiemtahZAZzcO9TnI5uaXh3%2B%2BlrqtNonCwp6%2F245UFWkiW1elpgtVAmJPbogcAv6rSlokztAfWk296ZJXzRDYAtzGH0gq7CgSJKfH%2BXxaCmR0WcvlKjNQnp12%2FeKXJYO4tDap8UCBLuyxDnR7oJKLHQHJLP0r0EAVOOSIbrFang%2F1WOq%2BJaq4Efc4XpnTgnwlBbWTmhWDR1pvS9iVEzcSYLHT%2FfNnMRxFc7u%2Bj3qI%2F%2F5yuGuu14KR0MuQKKCSpViieD%2BfIti46sxPTsjSemoUKp0oXA%3D%3D'

For the second set of example parameters (some non-ASCII characters):
    
    
    Code
    
    curl -H "X-MBX-APIKEY: CAvIjXy3F44yW6Pou5k8Dy1swsYDWJZLeoK2r8G4cFDnE9nosRppc2eKc1T8TRTQ" -X POST 'https://api.binance.com/api/v3/order?symbol=%EF%BC%91%EF%BC%92%EF%BC%93%EF%BC%94%EF%BC%95%EF%BC%96&side=SELL&type=LIMIT&timeInForce=GTC&quantity=1&price=0.2&timestamp=1668481559918&recvWindow=5000&signature=qJtv66wyp%2F1mZE%2BmIFAAMUoTe8xkmLN7%2FeAZjuC9x1ocxovItHLl%2FsNK7Wq8QjgiHqGn0bb8P7yVvGBEd1gFe71NQ8aM0M%2BJNIMz5UFxfeA53rXjFlvsyH1Sig%2BOuO9Nz5nhCaJ6bEfj2iuv7w27pB3L8MVqmoCi6D9C%2FQMiLxtPaR70CxtnvoOlIgPmpv2bQy029A31NEK19ieVLkoyp1EUkXRaX3v0mohx8yMnUG1dhX9nUg3Oy8TYZ03DQy7kHDGkMKisNX7rt%2FGuGx1HIgjFclDGLsbAFIodvSLjm9FbseasMELoxlAJDlwRnW8zo5sQmL0Fz7ao935QBynrng%3D%3D'

Here is a sample Bash script performing all the steps above:
    
    
    Code
    
    function rawurlencode {
      local string="${1}"
      local strlen=${#string}
      local encoded=""
      local pos c o
    
      for (( pos=0 ; pos<strlen ; pos++ )); do
         c=${string:$pos:1}
         case "$c" in
            [-_.~a-zA-Z0-9] ) o="${c}" ;;
            * )               printf -v o '%%%02x' "'$c"
         esac
         encoded+="${o}"
      done
      echo "${encoded}"
    }
    
    API_KEY="put your own API Key here"
    PRIVATE_KEY_PATH="test-prv-key.pem"
    # Set up the request:
    API_METHOD="POST"
    API_CALL="api/v3/order"
    API_PARAMS="symbol=BTCUSDT&side=SELL&type=LIMIT&timeInForce=GTC&quantity=1&price=0.2"
    # Sign the request:
    timestamp=$(date +%s000)
    api_params_with_timestamp="$API_PARAMS&timestamp=$timestamp"
    
    rawSignature=$(echo -n $api_params_with_timestamp | openssl dgst -keyform PEM -sha256 -sign $PRIVATE_KEY_PATH | openssl enc -base64 | tr -d '\n')
    
    # Percent-encode the signature
    signature=$(rawurlencode "$rawSignature")
    
    # Send the request:
    curl -H "X-MBX-APIKEY: $API_KEY" -X "$API_METHOD" \
        "https://api.binance.com/$API_CALL?$api_params_with_timestamp" \
        --data-urlencode "signature=$signature"

#### Ed25519 Keys

**Note: It is highly recommended to use Ed25519 API keys as it should provide the best performance and security out of all supported key types.**

The signature payload of your request is the query string concatenated without separator to the HTTP body. Any non-ASCII character must be percent-encoded before signing.

There is one example with a symbol name comprised entirely of ASCII characters and one example with a symbol name containing non-ASCII characters.

These examples assume the private key is stored in the file `./test-prv-key.pem`.

Key| Value  
---|---  
`apiKey`| 4yNzx3yWC5bS6YTwEkSRaC0nRmSQIIStAUOh1b6kqaBrTLIhjCpI5lJH8q8R8WNO  
  
Example of request with a symbol name comprised entirely of ASCII characters.

Parameter| Value  
---|---  
`symbol`| BTCUSDT  
`side`| SELL  
`type`| LIMIT  
`timeInForce`| GTC  
`quantity`| 1  
`price`| 0.2  
`timestamp`| 1668481559918  
`recvWindow`| 5000  
  
Example of a request with a symbol name containing non-ASCII characters.

Parameter| Value  
---|---  
`symbol`| １２３４５６  
`side`| SELL  
`type`| LIMIT  
`timeInForce`| GTC  
`quantity`| 1  
`price`| 0.2  
`timestamp`| 1668481559918  
`recvWindow`| 5000  
  
**Step 1: Construct the signature payload**

  1. Format parameters as `parameter=value` pairs separated by `&`.
  2. Percent-encode the string.



For the first set of example parameters (ASCII only), the `parameter=value` string should look like this:
    
    
    Code
    
    symbol=BTCUSDT&side=SELL&type=LIMIT&timeInForce=GTC&quantity=1&price=0.2&timestamp=1668481559918&recvWindow=5000

After percent-encoding, the signature payload should look like this:
    
    
    Code
    
    symbol=BTCUSDT&side=SELL&type=LIMIT&timeInForce=GTC&quantity=1&price=0.2&timestamp=1668481559918&recvWindow=5000

For the second set of example parameters (some non-ASCII characters), the `parameter=value` string should look like this:
    
    
    Code
    
    symbol=１２３４５６&side=SELL&type=LIMIT&timeInForce=GTC&quantity=1&price=0.2&timestamp=1668481559918&recvWindow=5000

After percent-encoding, the signature payload should look like this:
    
    
    Code
    
    symbol=%EF%BC%91%EF%BC%92%EF%BC%93%EF%BC%94%EF%BC%95%EF%BC%96&side=SELL&type=LIMIT&timeInForce=GTC&quantity=1&price=0.2&timestamp=1668481559918&recvWindow=5000

**Step 2: Compute the signature**

  1. Sign the payload.
  2. Encode the output as a base64 string.



Note that the payload and the resulting `signature` are **case-sensitive**.

For the first set of example parameters (ASCII only):
    
    
    Code
    
    echo -n "symbol=BTCUSDT&side=SELL&type=LIMIT&timeInForce=GTC&quantity=1&price=0.2&timestamp=1668481559918&recvWindow=5000" | openssl dgst -keyform PEM -sha256 -sign ./test-prv-key.pem | openssl enc -base64 | tr -d '\n'
    
    HaZnek7KOGa/k5+f6Q1nw8lzMUpo36mRVvvLHCMUCXxlmdQQGZge1luAUKnleD/DYeD19YrqzeHbb6xU3MkSIXKhAO1MaYq48uGVYb3vJScEZVOutgMInrZzUcCWNulNkfcbmExSiymCZ5xQBw5QDuzpuDFqRZ1Xt+BZxEHBN9OYQKpoe0+ovjnXyVOaH8VUKhE/ghUWnThrXJr+hmSc5t7ggjiVPQc7pGn3qSNGCQwdpkQC9GHMr/r+8n6qeEKMYB5j/1wC4d8Jae8FQiU8xcXR0NlUgV2LAw61/ZJv5BTJpa+z5Lv1W9v6jHQWRX2O8uaG3KU/lR3spR7+oGlWOw=

For the second set of example parameters (some non-ASCII characters):
    
    
    Code
    
    echo -n "symbol=%EF%BC%91%EF%BC%92%EF%BC%93%EF%BC%94%EF%BC%95%EF%BC%96&side=SELL&type=LIMIT&timeInForce=GTC&quantity=1&price=0.2&timestamp=1668481559918&recvWindow=5000" | openssl dgst -keyform PEM -sha256 -sign ./test-prv-key.pem | openssl enc -base64 | tr -d '\n'
    
    qJtv66wyp/1mZE+mIFAAMUoTe8xkmLN7/eAZjuC9x1ocxovItHLl/sNK7Wq8QjgiHqGn0bb8P7yVvGBEd1gFe71NQ8aM0M+JNIMz5UFxfeA53rXjFlvsyH1Sig+OuO9Nz5nhCaJ6bEfj2iuv7w27pB3L8MVqmoCi6D9C/QMiLxtPaR70CxtnvoOlIgPmpv2bQy029A31NEK19ieVLkoyp1EUkXRaX3v0mohx8yMnUG1dhX9nUg3Oy8TYZ03DQy7kHDGkMKisNX7rt/GuGx1HIgjFclDGLsbAFIodvSLjm9FbseasMELoxlAJDlwRnW8zo5sQmL0Fz7ao935QBynrng==

  3. Percent-encode the base64 string.



For the first set of example parameters (ASCII only):
    
    
    Code
    
    HaZnek7KOGa%2Fk5%2Bf6Q1nw8lzMUpo36mRVvvLHCMUCXxlmdQQGZge1luAUKnleD%2FDYeD19YrqzeHbb6xU3MkSIXKhAO1MaYq48uGVYb3vJScEZVOutgMInrZzUcCWNulNkfcbmExSiymCZ5xQBw5QDuzpuDFqRZ1Xt%2BBZxEHBN9OYQKpoe0%2BovjnXyVOaH8VUKhE%2FghUWnThrXJr%2BhmSc5t7ggjiVPQc7pGn3qSNGCQwdpkQC9GHMr%2Fr%2B8n6qeEKMYB5j%2F1wC4d8Jae8FQiU8xcXR0NlUgV2LAw61%2FZJv5BTJpa%2Bz5Lv1W9v6jHQWRX2O8uaG3KU%2FlR3spR7%2BoGlWOw%3D

For the second set of example parameters (some non-ASCII characters):
    
    
    Code
    
    qJtv66wyp%2F1mZE%2BmIFAAMUoTe8xkmLN7%2FeAZjuC9x1ocxovItHLl%2FsNK7Wq8QjgiHqGn0bb8P7yVvGBEd1gFe71NQ8aM0M%2BJNIMz5UFxfeA53rXjFlvsyH1Sig%2BOuO9Nz5nhCaJ6bEfj2iuv7w27pB3L8MVqmoCi6D9C%2FQMiLxtPaR70CxtnvoOlIgPmpv2bQy029A31NEK19ieVLkoyp1EUkXRaX3v0mohx8yMnUG1dhX9nUg3Oy8TYZ03DQy7kHDGkMKisNX7rt%2FGuGx1HIgjFclDGLsbAFIodvSLjm9FbseasMELoxlAJDlwRnW8zo5sQmL0Fz7ao935QBynrng%3D%3D

**Step 3: Add signature to the request**

Complete the request by adding the `signature` parameter to the query string.

For the first set of example parameters (ASCII only):
    
    
    Code
    
    curl -H "X-MBX-APIKEY: 4yNzx3yWC5bS6YTwEkSRaC0nRmSQIIStAUOh1b6kqaBrTLIhjCpI5lJH8q8R8WNO" -X POST 'https://api.binance.com/api/v3/order?symbol=BTCUSDT&side=SELL&type=LIMIT&timeInForce=GTC&quantity=1&price=0.2&timestamp=1668481559918&recvWindow=5000&signature=HaZnek7KOGa%2Fk5%2Bf6Q1nw8lzMUpo36mRVvvLHCMUCXxlmdQQGZge1luAUKnleD%2FDYeD19YrqzeHbb6xU3MkSIXKhAO1MaYq48uGVYb3vJScEZVOutgMInrZzUcCWNulNkfcbmExSiymCZ5xQBw5QDuzpuDFqRZ1Xt%2BBZxEHBN9OYQKpoe0%2BovjnXyVOaH8VUKhE%2FghUWnThrXJr%2BhmSc5t7ggjiVPQc7pGn3qSNGCQwdpkQC9GHMr%2Fr%2B8n6qeEKMYB5j%2F1wC4d8Jae8FQiU8xcXR0NlUgV2LAw61%2FZJv5BTJpa%2Bz5Lv1W9v6jHQWRX2O8uaG3KU%2FlR3spR7%2BoGlWOw%3D'

For the second set of example parameters (some non-ASCII characters):
    
    
    Code
    
    curl -H "X-MBX-APIKEY: 4yNzx3yWC5bS6YTwEkSRaC0nRmSQIIStAUOh1b6kqaBrTLIhjCpI5lJH8q8R8WNO" -X POST 'https://api.binance.com/api/v3/order?symbol=%EF%BC%91%EF%BC%92%EF%BC%93%EF%BC%94%EF%BC%95%EF%BC%96&side=SELL&type=LIMIT&timeInForce=GTC&quantity=1&price=0.2&timestamp=1668481559918&recvWindow=5000&signature=qJtv66wyp%2F1mZE%2BmIFAAMUoTe8xkmLN7%2FeAZjuC9x1ocxovItHLl%2FsNK7Wq8QjgiHqGn0bb8P7yVvGBEd1gFe71NQ8aM0M%2BJNIMz5UFxfeA53rXjFlvsyH1Sig%2BOuO9Nz5nhCaJ6bEfj2iuv7w27pB3L8MVqmoCi6D9C%2FQMiLxtPaR70CxtnvoOlIgPmpv2bQy029A31NEK19ieVLkoyp1EUkXRaX3v0mohx8yMnUG1dhX9nUg3Oy8TYZ03DQy7kHDGkMKisNX7rt%2FGuGx1HIgjFclDGLsbAFIodvSLjm9FbseasMELoxlAJDlwRnW8zo5sQmL0Fz7ao935QBynrng%3D%3D'

Here is a sample Python script performing all the steps above:
    
    
    Code
    
    #!/usr/bin/env python3
    
    import base64
    import requests
    import time
    import urllib.parse
    from cryptography.hazmat.primitives.serialization import load_pem_private_key
    
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
        'symbol':       'BTCUSDT',
        'side':         'SELL',
        'type':         'LIMIT',
        'timeInForce':  'GTC',
        'quantity':     '1.0000000',
        'price':        '0.20',
    }
    
    # Timestamp the request
    timestamp = int(time.time() * 1000) # UNIX timestamp in milliseconds
    params['timestamp'] = timestamp
    
    # Sign the request
    payload = urllib.parse.urlencode(params, encoding='UTF-8')
    signature = base64.b64encode(private_key.sign(payload.encode('ASCII')))
    params['signature'] = signature
    
    # Send the request
    headers = {
        'X-MBX-APIKEY': API_KEY,
    }
    response = requests.post(
        'https://api.binance.com/api/v3/order',
        headers=headers,
        data=params,
    )
    print(response.json())

Was this page helpful?

Last modified on November 12, 2026

[Errors](/en/docs/products/spot/errors)[WebSocket API](/en/docs/products/spot/web-socket-api)

---

# REST API 基本信息

## API 基本信息

  * 本篇列出接口的 base URL 有:
    * **<https://api.binance.com>**
    * **<https://api-gcp.binance.com>**
    * **<https://api1.binance.com>**
    * **<https://api2.binance.com>**
    * **<https://api3.binance.com>**
    * **<https://api4.binance.com>**
  * 上述列表的最后4个接口 (`api1`-`api4`) 会提供更好的性能，但其稳定性略为逊色。因此，请务必使用最适合的URL。
  * 响应默认为 JSON 格式。如果您想接收 SBE 格式的响应，请参考 [简单二进制编码 （SBE） 常见问题](/zh-CN/docs/products/spot/faqs/sbe_faq)。
  * 除非另有说明，否则数据将按**时间顺序** 返回。
    * 如果未指定 `startTime` 或 `endTime`，则返回最近的条目，直至达到限制值。
    * 如果指定 `startTime`，则返回从 `startTime` 到限制值为止最老的条目。
    * 如果指定 `endTime`，则返回截至 `endTime` 和限制值为止最近的条目。
    * 如果同时指定 `startTime` 和 `endTime`，则行为类似于 `startTime`，但不超过 `endTime`。
  * JSON 响应中的所有时间和时间戳相关字段均以**毫秒为默认单位** 。要以微秒为单位接收信息，请添加报文头 `X-MBX-TIME-UNIT:MICROSECOND` 或 `X-MBX-TIME-UNIT:microsecond`。
  * 我们支持 HMAC，RSA 以及 Ed25519 Key 类型。 如需进一步了解，请参考 [API Key 类型](/zh-CN/docs/products/spot/faqs/api_key_types)。
  * 时间戳参数（例如 `startTime`、`endTime`、`timestamp`）可以以毫秒或微秒为单位传递。
  * 对于仅发送公开市场数据的 API，您可以使用接口的 base URL <https://data-api.binance.vision> 。请参考 [Market Data Only](/zh-CN/docs/products/spot/faqs/market_data_only) 页面。
  * 如需进一步了解枚举或术语，请参考 [现货交易API术语表](/zh-CN/docs/products/spot/faqs/spot_glossary) 页面。
  * API 处理请求的超时时间为 10 秒。如果撮合引擎的响应时间超过此时间，API 将返回 “Timeout waiting for response from backend server. Send status unknown; execution status unknown.”。[(-1007 超时)](/zh-CN/docs/products/spot/errors#-1007-%E8%B6%85%E6%97%B6)
    * 这并不总是意味着该请求在撮合引擎中失败。
    * 如果请求状态未显示在 [用户数据流](/zh-CN/docs/products/spot/user-data-stream) 中，请执行 API 查询以获取其状态。
  * **请避免在请求中使用 SQL 关键字** ，因为这可能会触发 Web 应用防火墙（WAF）规则导致安全拦截。详情请参见 <https://www.binance.com/zh-CN/support/faq/detail/360004492232>
  * 如果您的请求包含非 ASCII 字符的交易对名称，那么响应中可能会包含以 UTF-8 编码的非 ASCII 字符。
  * 即使请求中不包含非 ASCII 字符，某些接口也可能返回包含以 UTF-8 编码的非 ASCII 字符的资产和/或交易对名称。



## HTTP 返回代码

  * HTTP `4XX` 错误码用于指示错误的请求内容、行为、格式。问题在于请求者。
  * HTTP `403` 错误码表示违反WAF限制(Web应用程序防火墙)。详情请参见 <https://www.binance.com/zh-CN/support/faq/detail/360004492232> 。
  * HTTP `409` 错误码表示重新下单(cancelReplace)的请求部分成功。(比如取消订单失败，但是下单成功了)
  * HTTP `429` 错误码表示警告访问频次超限，即将被封IP。
  * HTTP `418` 表示收到429后继续访问，于是被封了。
  * HTTP `5XX` 错误码用于指示Binance服务侧的问题。



## 接口错误代码

  * 每个接口都有可能抛出异常，异常响应格式如下：


    
    
    Code
    
    {
        "code": -1121,
        "msg": "Invalid symbol."
    }

  * 具体的错误码及其解释在[错误代码汇总](/zh-CN/docs/products/spot/errors)



## 接口的基本信息

  * `GET` 方法的接口, 参数必须在 `query string`中发送。
  * `POST`, `PUT`, 和 `DELETE` 方法的接口,参数可以在内容形式为`application/x-www-form-urlencoded`的 `query string` 中发送，也可以在 `request body` 中发送。 如果你喜欢，也可以混合这两种方式发送参数。
  * 对参数的顺序不做要求。
  * 但如果同一个参数名在`query string`和`request body`中都有，`query string`中的会被优先采用。



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
  
## 访问限制

### 访问限制基本信息

  * 以下是 `intervalLetter` 作为头部值:
    * SECOND => S
    * MINUTE => M
    * HOUR => H
    * DAY => D
  * 在 `/api/v3/exchangeInfo`接口中`rateLimits`数组里包含有REST接口(不限于本篇的REST接口)的访问限制。包括带权重的访问频次限制、下单速率限制。参考 [枚举定义](/zh-CN/docs/products/spot/enums) 中有关有限制类型的进一步说明。
  * 当您超出请求速率限制时，请求会失败并返回 HTTP 状态代码 429。



### IP 访问限制

  * 每个请求将包含一个`X-MBX-USED-WEIGHT-(intervalNum)(intervalLetter)`的头，其中包含当前IP所有请求的已使用权重。
  * 每一个接口均有一个相应的权重(weight)，有的接口根据参数不同可能拥有不同的权重。越消耗资源的接口权重就会越大。
  * 收到429时，您有责任停止发送请求，不得滥用API。
  * **收到429后仍然继续违反访问限制，会被封禁IP，并收到418错误码**
  * 频繁违反限制，封禁时间会逐渐延长，**从最短2分钟到最长3天**.
  * `Retry-After`的头会与带有418或429的响应发送，并且会给出**以秒为单位** 的等待时长(如果是429)以防止禁令，或者如果是418，直到禁令结束。
  * **访问限制是基于IP的，而不是API Key**



### 未成交订单计数

  * 每个成功的订单响应都将包含一个 `X-MBX-ORDER-COUNT-(intervalNum)(intervalLetter)` 报文头，用于标识您在该时间间隔内下了多少订单。如果您想要对此进行监控，请参阅 [`GET api/v3/rateLimit/order`](/zh-CN/docs/catalog/core-trading-spot-trading/api/rest-api/account#rate-limit-order)。
  * 被拒绝/不成功的订单不保证在响应中有 `X-MBX-ORDER-COUNT-**` 报文头。
  * 如果超过此值，您将收到一个 429 错误，而且不带 `Retry-After` 报文头。
  * **请注意，如果您的订单一直顺利完成交易，您可以通过 API 持续下订单** 。更多信息，请参见[现货未成交订单计数规则](/zh-CN/docs/products/spot/faqs/order_count_decrement)。
  * **未成交订单数量是按照每个账户来统计的** 。



## 数据来源

  * 因为API系统是异步的, 所以返回的数据有延时很正常, 也在预期之中。
  * 在每个接口中，都列出了其数据的来源，可以用于理解数据的时效性。



系统一共有3个数据来源，按照更新速度的先后排序。排在前面的数据最新，在后面就有可能存在延迟。

  * **撮合引擎** \- 表示数据来源于撮合引擎
  * **缓存** \- 表示数据来源于内部或者外部的缓存
  * **数据库** \- 表示数据直接来源于数据库



有些接口有不止一个数据源, 比如 `缓存 => 数据库`, 这表示接口会先从第一个数据源检查，如果没有数据，则检查下一个数据源。

## 请求鉴权类型

  * 每个接口都有一个鉴权类型，指示所需的 API 密钥权限，显示在接口名称旁边（例如，[下新订单 (TRADE)](/zh-CN/docs/catalog/core-trading-spot-trading/api/rest-api/trade#new-order)）。
  * 如果未指定，则鉴权类型为 `NONE`。
  * 除了为 `NONE` 外，所有具有鉴权类型的接口均视为 `SIGNED` 请求（即包含 `signature`）。
  * 具有鉴权类型的接口需要提供有效的 API 密钥并验证通过。
    * API 密钥可在您的 Binance 账户的 [API 管理](https://www.binance.com/en/support/faq/360002502072) 页面创建。
    * **API 密钥和密钥对均为敏感信息，切勿与他人分享。** 如果发现账户有异常活动，请立即撤销所有密钥并联系 Binance 支持。
  * API 密钥可配置为仅允许访问某些鉴权接口。
    * 例如，您可以拥有具有 `TRADE` 权限的 API 密钥用于交易，同时使用具有 `USER_DATA` 权限的另一个 API 密钥来监控订单状态。
    * 默认情况下，API 密钥无法进行 `TRADE`，您需要先在 API 管理中启用交易权限。

鉴权类型| 描述  
---|---  
`NONE`| 公开市场数据  
`TRADE`| 在交易所交易，下单和取消订单  
`USER_DATA`| 私人账户信息，例如订单状态和交易历史  
`USER_STREAM`| 管理用户数据流订阅  
  
### 需要签名的接口

  * 调用`SIGNED` 接口时，除了接口本身所需的参数外，还需要在 `query string` 或 `request body` 中传递 `signature`, 即签名参数。



#### 签名是否是大小写敏感的

  * **HMAC：** 使用 HMAC 生成的签名**不区分大小写** 。这意味着无论字母大小写如何，签名字符串都可以被验证。
  * **RSA：** 使用 RSA 生成的签名是**大小写敏感的** 。
  * **Ed25519：** 使用 Ed25519 生成的签名也是**大小写敏感的** 。



请参阅[已签名请求示例 (HMAC)](/zh-CN/docs/products/spot/rest-api#hmac-keys)、[已签名请求示例 (RSA)](/zh-CN/docs/products/spot/rest-api#rsa-keys) 和[已签名请求示例 (Ed25519)](/zh-CN/docs/products/spot/rest-api#ed25519-keys)，了解如何根据您使用的 API 密钥类型计算签名。

### 时间同步安全

  * `SIGNED` 请求还需要一个 `timestamp` 参数，该参数应为当前时间戳，单位为毫秒或微秒。（参见 [通用 API 信息](/zh-CN/docs/products/spot/rest-api#rest-api-%E5%9F%BA%E6%9C%AC%E4%BF%A1%E6%81%AF)）
  * 另一个可选参数 `recvWindow`，用以指定请求的有效期，只能以毫秒为单位。
    * `recvWindow` 扩展为三位小数（例如 6000.346），以便可以指定微秒。
    * 如果未发送 `recvWindow`，则 **默认值为 5000 毫秒** 。
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

**关于交易时效性** 互联网状况并不100%可靠，不可完全依赖,因此你的程序本地到币安服务器的时延会有抖动. 这是我们设置`recvWindow`的目的所在，如果你从事高频交易，对交易时效性有较高的要求，可以灵活设置`recvWindow`以达到你的要求。 **不推荐使用5秒以上的recvWindow。最大值不能超过60秒！**

### POST /api/v3/order 的签名示例

#### HMAC Keys

不使用分隔符，把查询字符串与 `HTTP body` 连接在一起将生成请求的签名 payload。任何非 ASCII 字符在签名前都必须进行百分比编码（percent-encoded）。

以下示例分步演示如何使用 `echo`、`openssl` 和 `curl` 从 Linux 命令行发送有效的签名 payload。其中一个例子中的交易对名称完全由 ASCII 字符组成，另一个例子中的交易对名称则包含非 ASCII 字符。

API 密钥和密钥示例：

Key| Value  
---|---  
`apiKey`| vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A  
`secretKey`| NhqPtmdSJYdKjVHjA7PZj4Mge3R5YNiP1e3UZjInClVN65XAbvqqM6A7H5fATj0j  
  
**警告：请勿与任何人分享您的 API 密钥和秘钥。**

此处提供的示例密钥仅用于示范说明目的。

交易对名称完全由 ASCII 字符组成的请求示例：

参数| 取值  
---|---  
`symbol`| LTCBTC  
`side`| BUY  
`type`| LIMIT  
`timeInForce`| GTC  
`quantity`| 1  
`price`| 0.1  
`recvWindow`| 5000  
`timestamp`| 1499827319559  
  
交易对名称包含非 ASCII 字符的请求示例：

参数| 取值  
---|---  
`symbol`| １２３４５６  
`side`| BUY  
`type`| LIMIT  
`timeInForce`| GTC  
`quantity`| 1  
`price`| 0.1  
`recvWindow`| 5000  
`timestamp`| 1499827319559  
  
**第一步: 构建签名 payload。**

  1. 将参数格式化为 `参数=取值` 对并用 `&` 分隔每个参数对。
  2. 对字符串进行百分比编码（percent-encoded）。



对于第一组示例参数（仅限 ASCII 字符）， `parameter=value` 字符串将如下所示：
    
    
    Code
    
    symbol=LTCBTC&side=BUY&type=LIMIT&timeInForce=GTC&quantity=1&price=0.1&recvWindow=5000&timestamp=1499827319559

对字符串进行百分比编码（percent-encoded）后，签名 payload 如下所示：
    
    
    Code
    
    symbol=LTCBTC&side=BUY&type=LIMIT&timeInForce=GTC&quantity=1&price=0.1&recvWindow=5000&timestamp=1499827319559

对于第二组示例参数（包含一些 Unicode 字符），`parameter=value` 字符串将如下所示：
    
    
    Code
    
    symbol=１２３４５６&side=BUY&type=LIMIT&timeInForce=GTC&quantity=1&price=0.1&recvWindow=5000&timestamp=1499827319559

对字符串进行百分比编码（percent-encoded）后，签名 payload 如下所示：
    
    
    Code
    
    symbol=%EF%BC%91%EF%BC%92%EF%BC%93%EF%BC%94%EF%BC%95%EF%BC%96&side=BUY&type=LIMIT&timeInForce=GTC&quantity=1&price=0.1&recvWindow=5000&timestamp=1499827319559

**第二步: 计算签名。**

  1. 使用 API 密钥中的 `secretKey` 作为 HMAC-SHA-256 算法的签名密钥。
  2. 对步骤 1 中构建的签名 payload 进行签名。
  3. 将 HMAC-SHA-256 的输出编码为十六进制字符串。



请注意，`secretKey` 和 payload 是**大小写敏感的** ，而生成的签名值是不区分大小写的。

**示例命令**

对于第一组示例参数（仅限 ASCII 字符）：
    
    
    Code
    
    $ echo -n "symbol=LTCBTC&side=BUY&type=LIMIT&timeInForce=GTC&quantity=1&price=0.1&recvWindow=5000&timestamp=1499827319559" | openssl dgst -sha256 -hmac "NhqPtmdSJYdKjVHjA7PZj4Mge3R5YNiP1e3UZjInClVN65XAbvqqM6A7H5fATj0j"
    
    c8db56825ae71d6d79447849e617115f4a920fa2acdcab2b053c4b2838bd6b71

对于第二组示例参数（包含一些 Unicode 字符）：
    
    
    Code
    
    $ echo -n "symbol=%EF%BC%91%EF%BC%92%EF%BC%93%EF%BC%94%EF%BC%95%EF%BC%96&side=BUY&type=LIMIT&timeInForce=GTC&quantity=1&price=0.1&recvWindow=5000&timestamp=1499827319559" | openssl dgst -sha256 -hmac "NhqPtmdSJYdKjVHjA7PZj4Mge3R5YNiP1e3UZjInClVN65XAbvqqM6A7H5fATj0j"
    
    e1353ec6b14d888f1164ae9af8228a3dbd508bc82eb867db8ab6046442f33ef3

**第三步: 为请求添加签名**

通过在查询字符串中添加 `signature` 参数来完成请求。

对于第一组示例参数（仅限 ASCII 字符）：
    
    
    Code
    
    curl -s -v -H "X-MBX-APIKEY: $apiKey" -X POST "https://api.binance.com/api/v3/order?symbol=LTCBTC&side=BUY&type=LIMIT&timeInForce=GTC&quantity=1&price=0.1&recvWindow=5000&timestamp=1499827319559&signature=c8db56825ae71d6d79447849e617115f4a920fa2acdcab2b053c4b2838bd6b71"

对于第二组示例参数（包含一些 Unicode 字符）：
    
    
    Code
    
    curl -s -v -H "X-MBX-APIKEY: $apiKey" -X POST "https://api.binance.com/api/v3/order?symbol=%EF%BC%91%EF%BC%92%EF%BC%93%EF%BC%94%EF%BC%95%EF%BC%96&side=BUY&type=LIMIT&timeInForce=GTC&quantity=1&price=0.1&recvWindow=5000&timestamp=1499827319559&signature=e1353ec6b14d888f1164ae9af8228a3dbd508bc82eb867db8ab6046442f33ef3"

以下是一个执行上述所有步骤的 Bash 脚本示例：
    
    
    Code
    
    apiKey="vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A"
    secretKey="NhqPtmdSJYdKjVHjA7PZj4Mge3R5YNiP1e3UZjInClVN65XAbvqqM6A7H5fATj0j"
    
    payload="symbol=LTCBTC&side=BUY&type=LIMIT&timeInForce=GTC&quantity=1&price=0.1&recvWindow=5000&timestamp=1499827319559"
    
    # 对请求进行签名
    
    signature=$(echo -n "$payload" | openssl dgst -sha256 -hmac "$secretKey")
    signature=${signature#*= }    # Keep only the part after the "= "
    
    # 发送请求
    
    curl -H "X-MBX-APIKEY: $apiKey" -X POST "https://api.binance.com/api/v3/order?$payload&signature=$signature"
    

#### RSA Keys

不使用分隔符，把查询字符串与 `HTTP body` 连接在一起将生成请求的签名 payload。任何非 ASCII 字符在签名前都必须进行百分比编码（percent-encoded）。

要获取 API 密钥，您需要将 RSA 公钥上传到您的帐户中，系统将为您提供相应的 API 密钥。

仅支持 `PKCS#8` 密钥。

在以下示例中，其中一个例子中的交易对名称完全由 ASCII 字符组成，另一个例子中的交易对名称则包含非 ASCII 字符。

这些示例假设私钥存储在文件 `./test-prv-key.pem` 中。

Key| Value  
---|---  
`apiKey`| CAvIjXy3F44yW6Pou5k8Dy1swsYDWJZLeoK2r8G4cFDnE9nosRppc2eKc1T8TRTQ  
  
交易对名称完全由 ASCII 字符组成的请求示例：

参数| 取值  
---|---  
`symbol`| BTCUSDT  
`side`| SELL  
`type`| LIMIT  
`timeInForce`| GTC  
`quantity`| 1  
`price`| 0.2  
`timestamp`| 1668481559918  
`recvWindow`| 5000  
  
交易对名称包含非 ASCII 字符的请求示例：

参数| 取值  
---|---  
`symbol`| １２３４５６  
`side`| SELL  
`type`| LIMIT  
`timeInForce`| GTC  
`quantity`| 1  
`price`| 0.2  
`timestamp`| 1668481559918  
`recvWindow`| 5000  
  
**第一步: 构建签名 payload。**

  1. 将参数格式化为 `参数=取值` 对并用 `&` 分隔每个参数对。
  2. 对字符串进行百分比编码（percent-encoded）。



对于第一组示例参数（仅限 ASCII 字符）， `parameter=value` 字符串将如下所示：
    
    
    Code
    
    symbol=BTCUSDT&side=SELL&type=LIMIT&timeInForce=GTC&quantity=1&price=0.2&timestamp=1668481559918&recvWindow=5000

对字符串进行百分比编码（percent-encoded）后，签名 payload 如下所示：
    
    
    Code
    
    symbol=BTCUSDT&side=SELL&type=LIMIT&timeInForce=GTC&quantity=1&price=0.2&timestamp=1668481559918&recvWindow=5000

对于第二组示例参数（包含一些 Unicode 字符），`parameter=value` 字符串将如下所示：
    
    
    Code
    
    symbol=１２３４５６=SELL&type=LIMIT&timeInForce=GTC&quantity=1&price=0.2&timestamp=1668481559918&recvWindow=5000

对字符串进行百分比编码（percent-encoded）后，签名 payload 如下所示：
    
    
    Code
    
    symbol=%EF%BC%91%EF%BC%92%EF%BC%93%EF%BC%94%EF%BC%95%EF%BC%96&side=SELL&type=LIMIT&timeInForce=GTC&quantity=1&price=0.2&timestamp=1668481559918&recvWindow=5000

**第二步: 计算签名。**

  1. 使用 RSASSA-PKCS1-v1_5 算法和 SHA-256 哈希函数对步骤 1 中构建的签名 payload 进行签名。
  2. 将输出结果编码为 base64 格式。



请注意，payload 和生成的`签名值`是**大小写敏感的** 。

对于第一组示例参数（仅限 ASCII 字符）：
    
    
    Code
    
    $  echo -n 'symbol=BTCUSDT&side=SELL&type=LIMIT&timeInForce=GTC&quantity=1&price=0.2&timestamp=1668481559918&recvWindow=5000' | openssl dgst -sha256 -sign ./test-prv-key.pem | openssl enc -base64 -A | tr -d '\n'
    HZ8HOjiJ1s/igS9JA+n7+7Ti/ihtkRF5BIWcPIEluJP6tlbFM/Bf44LfZka/iemtahZAZzcO9TnI5uaXh3++lrqtNonCwp6/245UFWkiW1elpgtVAmJPbogcAv6rSlokztAfWk296ZJXzRDYAtzGH0gq7CgSJKfH+XxaCmR0WcvlKjNQnp12/eKXJYO4tDap8UCBLuyxDnR7oJKLHQHJLP0r0EAVOOSIbrFang/1WOq+Jaq4Efc4XpnTgnwlBbWTmhWDR1pvS9iVEzcSYLHT/fNnMRxFc7u+j3qI//5yuGuu14KR0MuQKKCSpViieD+fIti46sxPTsjSemoUKp0oXA==

对于第二组示例参数（包含一些 Unicode 字符）：
    
    
    Code
    
    $  echo -n 'symbol=%EF%BC%91%EF%BC%92%EF%BC%93%EF%BC%94%EF%BC%95%EF%BC%96&side=SELL&type=LIMIT&timeInForce=GTC&quantity=1&price=0.2&timestamp=1668481559918&recvWindow=5000' | openssl dgst -sha256 -sign ./test-prv-key.pem | openssl enc -base64 -A | tr -d '\n'
    
    qJtv66wyp/1mZE+mIFAAMUoTe8xkmLN7/eAZjuC9x1ocxovItHLl/sNK7Wq8QjgiHqGn0bb8P7yVvGBEd1gFe71NQ8aM0M+JNIMz5UFxfeA53rXjFlvsyH1Sig+OuO9Nz5nhCaJ6bEfj2iuv7w27pB3L8MVqmoCi6D9C/QMiLxtPaR70CxtnvoOlIgPmpv2bQy029A31NEK19ieVLkoyp1EUkXRaX3v0mohx8yMnUG1dhX9nUg3Oy8TYZ03DQy7kHDGkMKisNX7rt/GuGx1HIgjFclDGLsbAFIodvSLjm9FbseasMELoxlAJDlwRnW8zo5sQmL0Fz7ao935QBynrng==

  3. 对 base64 格式的字符串进行百分比编码（percent-encoded）。



对于第一组示例参数（仅限 ASCII 字符）：
    
    
    Code
    
    HZ8HOjiJ1s%2FigS9JA%2Bn7%2B7Ti%2FihtkRF5BIWcPIEluJP6tlbFM%2FBf44LfZka%2FiemtahZAZzcO9TnI5uaXh3%2B%2BlrqtNonCwp6%2F245UFWkiW1elpgtVAmJPbogcAv6rSlokztAfWk296ZJXzRDYAtzGH0gq7CgSJKfH%2BXxaCmR0WcvlKjNQnp12%2FeKXJYO4tDap8UCBLuyxDnR7oJKLHQHJLP0r0EAVOOSIbrFang%2F1WOq%2BJaq4Efc4XpnTgnwlBbWTmhWDR1pvS9iVEzcSYLHT%2FfNnMRxFc7u%2Bj3qI%2F%2F5yuGuu14KR0MuQKKCSpViieD%2BfIti46sxPTsjSemoUKp0oXA%3D%3D

对于第二组示例参数（包含一些 Unicode 字符）：
    
    
    Code
    
    qJtv66wyp%2F1mZE%2BmIFAAMUoTe8xkmLN7%2FeAZjuC9x1ocxovItHLl%2FsNK7Wq8QjgiHqGn0bb8P7yVvGBEd1gFe71NQ8aM0M%2BJNIMz5UFxfeA53rXjFlvsyH1Sig%2BOuO9Nz5nhCaJ6bEfj2iuv7w27pB3L8MVqmoCi6D9C%2FQMiLxtPaR70CxtnvoOlIgPmpv2bQy029A31NEK19ieVLkoyp1EUkXRaX3v0mohx8yMnUG1dhX9nUg3Oy8TYZ03DQy7kHDGkMKisNX7rt%2FGuGx1HIgjFclDGLsbAFIodvSLjm9FbseasMELoxlAJDlwRnW8zo5sQmL0Fz7ao935QBynrng%3D%3D

**第三步: 为请求添加签名**

通过在查询字符串中添加 `signature` 参数来完成请求。

对于第一组示例参数（仅限 ASCII 字符）：
    
    
    Code
    
    curl -H "X-MBX-APIKEY: CAvIjXy3F44yW6Pou5k8Dy1swsYDWJZLeoK2r8G4cFDnE9nosRppc2eKc1T8TRTQ" -X POST 'https://api.binance.com/api/v3/order?symbol=BTCUSDT&side=SELL&type=LIMIT&timeInForce=GTC&quantity=1&price=0.2&timestamp=1668481559918&recvWindow=5000&signature=HZ8HOjiJ1s%2FigS9JA%2Bn7%2B7Ti%2FihtkRF5BIWcPIEluJP6tlbFM%2FBf44LfZka%2FiemtahZAZzcO9TnI5uaXh3%2B%2BlrqtNonCwp6%2F245UFWkiW1elpgtVAmJPbogcAv6rSlokztAfWk296ZJXzRDYAtzGH0gq7CgSJKfH%2BXxaCmR0WcvlKjNQnp12%2FeKXJYO4tDap8UCBLuyxDnR7oJKLHQHJLP0r0EAVOOSIbrFang%2F1WOq%2BJaq4Efc4XpnTgnwlBbWTmhWDR1pvS9iVEzcSYLHT%2FfNnMRxFc7u%2Bj3qI%2F%2F5yuGuu14KR0MuQKKCSpViieD%2BfIti46sxPTsjSemoUKp0oXA%3D%3D'

对于第二组示例参数（包含一些 Unicode 字符）：
    
    
    Code
    
    curl -H "X-MBX-APIKEY: CAvIjXy3F44yW6Pou5k8Dy1swsYDWJZLeoK2r8G4cFDnE9nosRppc2eKc1T8TRTQ" -X POST 'https://api.binance.com/api/v3/order?symbol=%EF%BC%91%EF%BC%92%EF%BC%93%EF%BC%94%EF%BC%95%EF%BC%96&side=SELL&type=LIMIT&timeInForce=GTC&quantity=1&price=0.2&timestamp=1668481559918&recvWindow=5000&signature=qJtv66wyp%2F1mZE%2BmIFAAMUoTe8xkmLN7%2FeAZjuC9x1ocxovItHLl%2FsNK7Wq8QjgiHqGn0bb8P7yVvGBEd1gFe71NQ8aM0M%2BJNIMz5UFxfeA53rXjFlvsyH1Sig%2BOuO9Nz5nhCaJ6bEfj2iuv7w27pB3L8MVqmoCi6D9C%2FQMiLxtPaR70CxtnvoOlIgPmpv2bQy029A31NEK19ieVLkoyp1EUkXRaX3v0mohx8yMnUG1dhX9nUg3Oy8TYZ03DQy7kHDGkMKisNX7rt%2FGuGx1HIgjFclDGLsbAFIodvSLjm9FbseasMELoxlAJDlwRnW8zo5sQmL0Fz7ao935QBynrng%3D%3D'

以下是一个执行上述所有步骤的 Bash 脚本示例：
    
    
    Code
    
    function rawurlencode {
      local string="${1}"
      local strlen=${#string}
      local encoded=""
      local pos c o
    
      for (( pos=0 ; pos<strlen ; pos++ )); do
         c=${string:$pos:1}
         case "$c" in
            [-_.~a-zA-Z0-9] ) o="${c}" ;;
            * )               printf -v o '%%%02x' "'$c"
         esac
         encoded+="${o}"
      done
      echo "${encoded}"
    }
    
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
    
    rawSignature=$(echo -n $api_params_with_timestamp | openssl dgst -keyform PEM -sha256 -sign $PRIVATE_KEY_PATH | openssl enc -base64 | tr -d '\n')
    
    # 对签名编码进行百分号编码（percent-encoding）
    signature=$(rawurlencode "$rawSignature")
    
    # 发送请求：
    curl -H "X-MBX-APIKEY: $API_KEY" -X "$API_METHOD" \
        "https://api.binance.com/$API_CALL?$api_params_with_timestamp" \
        --data-urlencode "signature=$signature"

#### Ed25519 Keys

**我们强烈建议使用 Ed25519 API keys** ，因为它在所有受支持的 API key 类型中提供最佳性能和安全性。

不使用分隔符，把查询字符串与 `HTTP body` 连接在一起将生成请求的签名 payload。任何非 ASCII 字符在签名前都必须进行百分比编码（percent-encoded）。

在以下示例中，其中一个例子中的交易对名称完全由 ASCII 字符组成，另一个例子中的交易对名称则包含非 ASCII 字符。

这些示例假设私钥存储在文件 `./test-prv-key.pem` 中。

Key| Value  
---|---  
`apiKey`| 4yNzx3yWC5bS6YTwEkSRaC0nRmSQIIStAUOh1b6kqaBrTLIhjCpI5lJH8q8R8WNO  
  
交易对名称完全由 ASCII 字符组成的请求示例：

参数| 取值  
---|---  
`symbol`| BTCUSDT  
`side`| SELL  
`type`| LIMIT  
`timeInForce`| GTC  
`quantity`| 1  
`price`| 0.2  
`timestamp`| 1668481559918  
`recvWindow`| 5000  
  
交易对名称包含非 ASCII 字符的请求示例：

参数| 取值  
---|---  
`symbol`| １２３４５６  
`side`| SELL  
`type`| LIMIT  
`timeInForce`| GTC  
`quantity`| 1  
`price`| 0.2  
`timestamp`| 1668481559918  
`recvWindow`| 5000  
  
**第一步: 构建签名 payload。**

  1. 将参数格式化为 `参数=取值` 对并用 `&` 分隔每个参数对。
  2. 对字符串进行百分比编码（percent-encoded）。



对于第一组示例参数（仅限 ASCII 字符）， `parameter=value` 字符串将如下所示：
    
    
    Code
    
    symbol=BTCUSDT&side=SELL&type=LIMIT&timeInForce=GTC&quantity=1&price=0.2&timestamp=1668481559918&recvWindow=5000

对字符串进行百分比编码（percent-encoded）后，签名 payload 如下所示：
    
    
    Code
    
    symbol=BTCUSDT&side=SELL&type=LIMIT&timeInForce=GTC&quantity=1&price=0.2&timestamp=1668481559918&recvWindow=5000

对于第二组示例参数（包含一些 Unicode 字符），`parameter=value` 字符串将如下所示：
    
    
    Code
    
    symbol=１２３４５６&side=SELL&type=LIMIT&timeInForce=GTC&quantity=1&price=0.2&timestamp=1668481559918&recvWindow=5000

对字符串进行百分比编码（percent-encoded）后，签名 payload 如下所示：
    
    
    Code
    
    symbol=%EF%BC%91%EF%BC%92%EF%BC%93%EF%BC%94%EF%BC%95%EF%BC%96&side=SELL&type=LIMIT&timeInForce=GTC&quantity=1&price=0.2&timestamp=1668481559918&recvWindow=5000

**第二步: 计算签名。**

  1. 对 payload 进行签名。
  2. 将输出结果编码为 base64 格式。



请注意，payload 和生成的`签名值`是**大小写敏感的** 。

对于第一组示例参数（仅限 ASCII 字符）：
    
    
    Code
    
    echo -n "symbol=BTCUSDT&side=SELL&type=LIMIT&timeInForce=GTC&quantity=1&price=0.2&timestamp=1668481559918&recvWindow=5000" | openssl dgst -keyform PEM -sha256 -sign ./test-prv-key.pem | openssl enc -base64 | tr -d '\n'
    
    HaZnek7KOGa/k5+f6Q1nw8lzMUpo36mRVvvLHCMUCXxlmdQQGZge1luAUKnleD/DYeD19YrqzeHbb6xU3MkSIXKhAO1MaYq48uGVYb3vJScEZVOutgMInrZzUcCWNulNkfcbmExSiymCZ5xQBw5QDuzpuDFqRZ1Xt+BZxEHBN9OYQKpoe0+ovjnXyVOaH8VUKhE/ghUWnThrXJr+hmSc5t7ggjiVPQc7pGn3qSNGCQwdpkQC9GHMr/r+8n6qeEKMYB5j/1wC4d8Jae8FQiU8xcXR0NlUgV2LAw61/ZJv5BTJpa+z5Lv1W9v6jHQWRX2O8uaG3KU/lR3spR7+oGlWOw=

对于第二组示例参数（包含一些 Unicode 字符）：
    
    
    Code
    
    echo -n "symbol=%EF%BC%91%EF%BC%92%EF%BC%93%EF%BC%94%EF%BC%95%EF%BC%96&side=SELL&type=LIMIT&timeInForce=GTC&quantity=1&price=0.2&timestamp=1668481559918&recvWindow=5000" | openssl dgst -keyform PEM -sha256 -sign ./test-prv-key.pem | openssl enc -base64 | tr -d '\n'
    
    qJtv66wyp/1mZE+mIFAAMUoTe8xkmLN7/eAZjuC9x1ocxovItHLl/sNK7Wq8QjgiHqGn0bb8P7yVvGBEd1gFe71NQ8aM0M+JNIMz5UFxfeA53rXjFlvsyH1Sig+OuO9Nz5nhCaJ6bEfj2iuv7w27pB3L8MVqmoCi6D9C/QMiLxtPaR70CxtnvoOlIgPmpv2bQy029A31NEK19ieVLkoyp1EUkXRaX3v0mohx8yMnUG1dhX9nUg3Oy8TYZ03DQy7kHDGkMKisNX7rt/GuGx1HIgjFclDGLsbAFIodvSLjm9FbseasMELoxlAJDlwRnW8zo5sQmL0Fz7ao935QBynrng==

  3. 对 base64 格式的字符串进行百分比编码（percent-encoded）。



对于第一组示例参数（仅限 ASCII 字符）：
    
    
    Code
    
    HaZnek7KOGa%2Fk5%2Bf6Q1nw8lzMUpo36mRVvvLHCMUCXxlmdQQGZge1luAUKnleD%2FDYeD19YrqzeHbb6xU3MkSIXKhAO1MaYq48uGVYb3vJScEZVOutgMInrZzUcCWNulNkfcbmExSiymCZ5xQBw5QDuzpuDFqRZ1Xt%2BBZxEHBN9OYQKpoe0%2BovjnXyVOaH8VUKhE%2FghUWnThrXJr%2BhmSc5t7ggjiVPQc7pGn3qSNGCQwdpkQC9GHMr%2Fr%2B8n6qeEKMYB5j%2F1wC4d8Jae8FQiU8xcXR0NlUgV2LAw61%2FZJv5BTJpa%2Bz5Lv1W9v6jHQWRX2O8uaG3KU%2FlR3spR7%2BoGlWOw%3D

对于第二组示例参数（包含一些 Unicode 字符）：
    
    
    Code
    
    qJtv66wyp%2F1mZE%2BmIFAAMUoTe8xkmLN7%2FeAZjuC9x1ocxovItHLl%2FsNK7Wq8QjgiHqGn0bb8P7yVvGBEd1gFe71NQ8aM0M%2BJNIMz5UFxfeA53rXjFlvsyH1Sig%2BOuO9Nz5nhCaJ6bEfj2iuv7w27pB3L8MVqmoCi6D9C%2FQMiLxtPaR70CxtnvoOlIgPmpv2bQy029A31NEK19ieVLkoyp1EUkXRaX3v0mohx8yMnUG1dhX9nUg3Oy8TYZ03DQy7kHDGkMKisNX7rt%2FGuGx1HIgjFclDGLsbAFIodvSLjm9FbseasMELoxlAJDlwRnW8zo5sQmL0Fz7ao935QBynrng%3D%3D

**第三步: 为请求添加签名**

通过在查询字符串中添加 `signature` 参数来完成请求。

对于第一组示例参数（仅限 ASCII 字符）：
    
    
    Code
    
    curl -H "X-MBX-APIKEY: 4yNzx3yWC5bS6YTwEkSRaC0nRmSQIIStAUOh1b6kqaBrTLIhjCpI5lJH8q8R8WNO" -X POST 'hhttps://api.binance.com/api/v3/order?symbol=BTCUSDT&side=SELL&type=LIMIT&timeInForce=GTC&quantity=1&price=0.2&timestamp=1668481559918&recvWindow=5000&signature=HaZnek7KOGa%2Fk5%2Bf6Q1nw8lzMUpo36mRVvvLHCMUCXxlmdQQGZge1luAUKnleD%2FDYeD19YrqzeHbb6xU3MkSIXKhAO1MaYq48uGVYb3vJScEZVOutgMInrZzUcCWNulNkfcbmExSiymCZ5xQBw5QDuzpuDFqRZ1Xt%2BBZxEHBN9OYQKpoe0%2BovjnXyVOaH8VUKhE%2FghUWnThrXJr%2BhmSc5t7ggjiVPQc7pGn3qSNGCQwdpkQC9GHMr%2Fr%2B8n6qeEKMYB5j%2F1wC4d8Jae8FQiU8xcXR0NlUgV2LAw61%2FZJv5BTJpa%2Bz5Lv1W9v6jHQWRX2O8uaG3KU%2FlR3spR7%2BoGlWOw%3D'

对于第二组示例参数（包含一些 Unicode 字符）：
    
    
    Code
    
    curl -H "X-MBX-APIKEY: 4yNzx3yWC5bS6YTwEkSRaC0nRmSQIIStAUOh1b6kqaBrTLIhjCpI5lJH8q8R8WNO" -X POST 'https://api.binance.com/api/v3/order?symbol=%EF%BC%91%EF%BC%92%EF%BC%93%EF%BC%94%EF%BC%95%EF%BC%96&side=SELL&type=LIMIT&timeInForce=GTC&quantity=1&price=0.2&timestamp=1668481559918&recvWindow=5000&signature=qJtv66wyp%2F1mZE%2BmIFAAMUoTe8xkmLN7%2FeAZjuC9x1ocxovItHLl%2FsNK7Wq8QjgiHqGn0bb8P7yVvGBEd1gFe71NQ8aM0M%2BJNIMz5UFxfeA53rXjFlvsyH1Sig%2BOuO9Nz5nhCaJ6bEfj2iuv7w27pB3L8MVqmoCi6D9C%2FQMiLxtPaR70CxtnvoOlIgPmpv2bQy029A31NEK19ieVLkoyp1EUkXRaX3v0mohx8yMnUG1dhX9nUg3Oy8TYZ03DQy7kHDGkMKisNX7rt%2FGuGx1HIgjFclDGLsbAFIodvSLjm9FbseasMELoxlAJDlwRnW8zo5sQmL0Fz7ao935QBynrng%3D%3D'

以下是一个执行上述所有步骤的 Bash 脚本示例：
    
    
    Code
    
    #!/usr/bin/env python3
    
    import base64
    import requests
    import time
    import urllib.parse
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
    payload = urllib.parse.urlencode(params, encoding='UTF-8')
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

此页面是否有帮助？

Last modified on November 12, 2026

[错误代码](/zh-CN/docs/products/spot/errors)[WebSocket API](/zh-CN/docs/products/spot/web-socket-api)