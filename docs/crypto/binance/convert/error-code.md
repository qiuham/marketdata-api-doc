---
exchange: binance
source_url: https://developers.binance.com/docs/convert/error-code
api_type: REST
updated_at: 2026-06-28 18:55:32.141833
---

# General Info

## General API Information[​](/docs/convert/general-info#general-api-information "Direct link to General API Information")

  * The following base endpoints are available: 
    * **<https://api.binance.com>**
    * **<https://api-gcp.binance.com>**
    * **<https://api1.binance.com>**
    * **<https://api2.binance.com>**
    * **<https://api3.binance.com>**
    * **<https://api4.binance.com>**
  * The last 4 endpoints in the point above (`api1`-`api4`) might give better performance but have less stability. Please use whichever works best for your setup.
  * All endpoints return either a JSON object or array.
  * Data is returned in **ascending** order. Oldest first, newest last.
  * All time and timestamp related fields are in **milliseconds**.



### HTTP Return Codes[​](/docs/convert/general-info#http-return-codes "Direct link to HTTP Return Codes")

  * HTTP `4XX` return codes are used for malformed requests; the issue is on the sender's side.
  * HTTP `403` return code is used when the WAF Limit (Web Application Firewall) has been violated.
  * HTTP `409` return code is used when a cancelReplace order partially succeeds. (e.g. if the cancellation of the order fails but the new order placement succeeds.)
  * HTTP `429` return code is used when breaking a request rate limit.
  * HTTP `418` return code is used when an IP has been auto-banned for continuing to send requests after receiving `429` codes.
  * HTTP `5XX` return codes are used for internal errors; the issue is on Binance's side. It is important to **NOT** treat this as a failure operation; the execution status is **UNKNOWN** and could have been a success.



### Error Codes and Messages[​](/docs/convert/general-info#error-codes-and-messages "Direct link to Error Codes and Messages")

  * If there is an error, the API will return an error with a message of the reason.



> The error payload on API and SAPI is as follows:
    
    
    {  
      "code": -1121,  
      "msg": "Invalid symbol."  
    }  
    

  * Specific error codes and messages defined in [Error Codes](/docs/convert/general-info#error-codes).



### General Information on Endpoints[​](/docs/convert/general-info#general-information-on-endpoints "Direct link to General Information on Endpoints")

  * For `GET` endpoints, parameters must be sent as a `query string`.
  * For `POST`, `PUT`, and `DELETE` endpoints, the parameters may be sent as a `query string` or in the `request body` with content type `application/x-www-form-urlencoded`. You may mix parameters between both the `query string` and `request body` if you wish to do so.
  * Parameters may be sent in any order.
  * If a parameter sent in both the `query string` and `request body`, the `query string` parameter will be used.



* * *

## LIMITS[​](/docs/convert/general-info#limits "Direct link to LIMITS")

### General Info on Limits[​](/docs/convert/general-info#general-info-on-limits "Direct link to General Info on Limits")

  * The following `intervalLetter` values for headers: 
    * SECOND => S
    * MINUTE => M
    * HOUR => H
    * DAY => D
  * `intervalNum` describes the amount of the interval. For example, `intervalNum` 5 with `intervalLetter` M means "Every 5 minutes".
  * The `/api/v3/exchangeInfo` `rateLimits` array contains objects related to the exchange's `RAW_REQUESTS`, `REQUEST_WEIGHT`, and `ORDERS` rate limits. These are further defined in the `ENUM definitions` section under `Rate limiters (rateLimitType)`.
  * A 429 will be returned when either request rate limit or order rate limit is violated.



### IP Limits[​](/docs/convert/general-info#ip-limits "Direct link to IP Limits")

  * Every request will contain `X-MBX-USED-WEIGHT-(intervalNum)(intervalLetter)` in the response headers which has the current used weight for the IP for all request rate limiters defined.
  * Each route has a `weight` which determines for the number of requests each endpoint counts for. Heavier endpoints and endpoints that do operations on multiple symbols will have a heavier `weight`.
  * When a 429 is received, it's your obligation as an API to back off and not spam the API.
  * **Repeatedly violating rate limits and/or failing to back off after receiving 429s will result in an automated IP ban (HTTP status 418).**
  * IP bans are tracked and **scale in duration** for repeat offenders, **from 2 minutes to 3 days**.
  * A `Retry-After` header is sent with a 418 or 429 responses and will give the **number of seconds** required to wait, in the case of a 429, to prevent a ban, or, in the case of a 418, until the ban is over.
  * **The limits on the API are based on the IPs, not the API keys.**

We recommend using the websocket for getting data as much as possible, as this will not count to the request rate limit. 

### Order Rate Limits[​](/docs/convert/general-info#order-rate-limits "Direct link to Order Rate Limits")

  * Every successful order response will contain a `X-MBX-ORDER-COUNT-(intervalNum)(intervalLetter)` header which has the current order count for the account for all order rate limiters defined.

  * When the order count exceeds the limit, you will receive a 429 error without the `Retry-After` header. Please check the Order Rate Limit rules using `GET api/v3/exchangeInfo` and wait for reactivation accordingly.

  * Rejected/unsuccessful orders are not guaranteed to have `X-MBX-ORDER-COUNT-**` headers in the response.

  * **The order rate limit is counted against each account**.

  * To monitor order count usage, refer to GET `api/v3/rateLimit/order`




### Websocket Limits[​](/docs/convert/general-info#websocket-limits "Direct link to Websocket Limits")

  * WebSocket connections have a limit of 5 incoming messages per second. A message is considered: 
    * A PING frame
    * A PONG frame
    * A JSON controlled message (e.g. subscribe, unsubscribe)
  * A connection that goes beyond the limit will be disconnected; IPs that are repeatedly disconnected may be banned.
  * A single connection can listen to a maximum of 1024 streams.
  * There is a limit of **300 connections per attempt every 5 minutes per IP**.



### /api/ and /sapi/ Limit Introduction[​](/docs/convert/general-info#api-and-sapi-limit-introduction "Direct link to /api/ and /sapi/ Limit Introduction")

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

## Data Sources[​](/docs/convert/general-info#data-sources "Direct link to Data Sources")

  * The API system is asynchronous, so some delay in the response is normal and expected.
  * Each endpoint has a data source indicating where the data is being retrieved, and thus which endpoints have the most up-to-date response.



These are the three sources, ordered by which is has the most up-to-date response to the one with potential delays in updates.

  * **Matching Engine** \- the data is from the matching Engine
  * **Memory** \- the data is from a server's local or external memory
  * **Database** \- the data is taken directly from a database

Some endpoints can have more than 1 data source. (e.g. Memory => Database)   
  
This means that the endpoint will check the first Data Source, and if it cannot find the value it's looking for it will check the next one. 

## Request Security[​](/docs/convert/general-info#request-security "Direct link to Request Security")

  * Each endpoint has a security type indicating required API key permissions, shown next to the endpoint name (e.g., [New order (TRADE)](/docs/convert/general-info#place-new-order-trade)).
  * If unspecified, the security type is `NONE`.
  * Except for `NONE`, all endpoints with a security type are considered `SIGNED` requests (i.e. including a `signature`), except for [listenKey management](/docs/convert/general-info#user-data-stream-requests).
  * Secure endpoints require a valid API key to be specified and authenticated. 
    * API keys can be created on the [API Management](https://www.binance.com/en/support/faq/360002502072) page of your Binance account.
    * **Both API key and secret key are sensitive.** Never share them with anyone. If you notice unusual activity in your account, immediately revoke all the keys and contact Binance support.
  * API keys can be configured to allow access only to certain types of secure endpoints. 
    * For example, you can have an API key with `TRADE` permission for trading, while using a separate API key with `USER_DATA` permission to monitor your order status.
    * By default, an API key cannot `TRADE`. You need to enable trading in API Management first.

Security Type| Description  
---|---  
NONE| Endpoint can be accessed freely.  
TRADE| Endpoint requires sending a valid API-Key and signature.  
MARGIN| Endpoint requires sending a valid API-Key and signature.  
USER_DATA| Endpoint requires sending a valid API-Key and signature.  
USER_STREAM| Endpoint requires sending a valid API-Key.  
MARKET_DATA| Endpoint requires sending a valid API-Key.  
  
  * `TRADE`, `MARGIN` and `USER_DATA` endpoints are `SIGNED` endpoints.



### SIGNED Endpoint security[​](/docs/convert/general-info#signed-endpoint-security "Direct link to SIGNED Endpoint security")

  * `SIGNED` endpoints require an additional parameter, `signature`, to be sent in the `query string` or `request body`.



#### Signature Case Sensitivity[​](/docs/convert/general-info#signature-case-sensitivity "Direct link to Signature Case Sensitivity")

  * **HMAC:** Signatures generated using HMAC are **not case-sensitive**. This means the signature string can be verified regardless of letter casing.
  * **RSA:** Signatures generated using RSA are **case-sensitive**.
  * **Ed25519:** Signatures generated using Ed25519 are also **case-sensitive**



Please consult [SIGNED request example (HMAC)](/docs/convert/general-info#hmac-keys), [SIGNED request example (RSA)](/docs/convert/general-info#rsa-keys), and [SIGNED request example (Ed25519)](/docs/convert/general-info#ed25519-keys) on how to compute signature, depending on which API key type you are using.

### Timing security[​](/docs/convert/general-info#timing-security "Direct link to Timing security")

  * `SIGNED` requests also require a `timestamp` parameter which should be the current timestamp either in milliseconds or microseconds. (See [General API Information](/docs/convert/general-info#general-api-information))
  * An additional optional parameter, `recvWindow`, specifies for how long the request stays valid and may only be specified in milliseconds. 
    * `recvWindow` supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be specified.
    * If `recvWindow` is not sent, **it defaults to 5000 milliseconds**.
    * Maximum `recvWindow` is 60000 milliseconds.
  * Request processing logic is as follows:


    
    
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

### SIGNED Endpoint Examples for POST /api/v3/order[​](/docs/convert/general-info#signed-endpoint-examples-for-post-apiv3order "Direct link to SIGNED Endpoint Examples for POST /api/v3/order")

#### HMAC Keys[​](/docs/convert/general-info#hmac-keys "Direct link to HMAC Keys")

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
    
    
    symbol=LTCBTC&side=BUY&type=LIMIT&timeInForce=GTC&quantity=1&price=0.1&recvWindow=5000&timestamp=1499827319559  
    

After percent-encoding, the signature payload should look like this:
    
    
    symbol=LTCBTC&side=BUY&type=LIMIT&timeInForce=GTC&quantity=1&price=0.1&recvWindow=5000&timestamp=1499827319559  
    

For the second set of example parameters (some non-ASCII characters), the `parameter=value` string should look like this:
    
    
    symbol=１２３４５６&side=BUY&type=LIMIT&timeInForce=GTC&quantity=1&price=0.1&recvWindow=5000&timestamp=1499827319559  
    

After percent-encoding, the signature payload should look like this:
    
    
    symbol=%EF%BC%91%EF%BC%92%EF%BC%93%EF%BC%94%EF%BC%95%EF%BC%96&side=BUY&type=LIMIT&timeInForce=GTC&quantity=1&price=0.1&recvWindow=5000&timestamp=1499827319559  
    

**Step 2: Compute the signature**

  1. Use the `secretKey` of your API key as the signing key for the HMAC-SHA-256 algorithm.
  2. Sign the signature payload constructed in Step 1.
  3. Encode the HMAC-SHA-256 output as a hex string.



Note that `secretKey` and the payload are **case-sensitive** , while the resulting signature value is case-insensitive.

**Example commands**

For the first set of example parameters (ASCII only):
    
    
    $ echo -n "symbol=LTCBTC&side=BUY&type=LIMIT&timeInForce=GTC&quantity=1&price=0.1&recvWindow=5000&timestamp=1499827319559" | openssl dgst -sha256 -hmac "NhqPtmdSJYdKjVHjA7PZj4Mge3R5YNiP1e3UZjInClVN65XAbvqqM6A7H5fATj0j"  
      
    c8db56825ae71d6d79447849e617115f4a920fa2acdcab2b053c4b2838bd6b71  
    

For the second set of example parameters (some non-ASCII characters):
    
    
    $ echo -n "symbol=%EF%BC%91%EF%BC%92%EF%BC%93%EF%BC%94%EF%BC%95%EF%BC%96&side=BUY&type=LIMIT&timeInForce=GTC&quantity=1&price=0.1&recvWindow=5000&timestamp=1499827319559" | openssl dgst -sha256 -hmac "NhqPtmdSJYdKjVHjA7PZj4Mge3R5YNiP1e3UZjInClVN65XAbvqqM6A7H5fATj0j"  
      
    e1353ec6b14d888f1164ae9af8228a3dbd508bc82eb867db8ab6046442f33ef3  
    

**Step 3: Add signature to the request**

Complete the request by adding the `signature` parameter to the query string.

For the first set of example parameters (ASCII only):
    
    
    curl -s -v -H "X-MBX-APIKEY: $apiKey" -X POST "https://api.binance.com/api/v3/order?symbol=LTCBTC&side=BUY&type=LIMIT&timeInForce=GTC&quantity=1&price=0.1&recvWindow=5000&timestamp=1499827319559&signature=c8db56825ae71d6d79447849e617115f4a920fa2acdcab2b053c4b2838bd6b71"  
    

For the second set of example parameters (some non-ASCII characters)
    
    
    curl -s -v -H "X-MBX-APIKEY: $apiKey" -X POST "https://api.binance.com/api/v3/order?symbol=%EF%BC%91%EF%BC%92%EF%BC%93%EF%BC%94%EF%BC%95%EF%BC%96&side=BUY&type=LIMIT&timeInForce=GTC&quantity=1&price=0.1&recvWindow=5000&timestamp=1499827319559&signature=e1353ec6b14d888f1164ae9af8228a3dbd508bc82eb867db8ab6046442f33ef3"  
    

Here is a sample Bash script performing all the steps above:
    
    
    apiKey="vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A"  
    secretKey="NhqPtmdSJYdKjVHjA7PZj4Mge3R5YNiP1e3UZjInClVN65XAbvqqM6A7H5fATj0j"  
      
    payload="symbol=LTCBTC&side=BUY&type=LIMIT&timeInForce=GTC&quantity=1&price=0.1&recvWindow=5000&timestamp=1499827319559"  
      
    # Sign the request  
      
    signature=$(echo -n "$payload" | openssl dgst -sha256 -hmac "$secretKey")  
    signature=${signature#*= }    # Keep only the part after the "= "  
      
    # Send the request  
      
    curl -H "X-MBX-APIKEY: $apiKey" -X POST "https://api.binance.com/api/v3/order?$payload&signature=$signature"  
      
    

#### RSA Keys[​](/docs/convert/general-info#rsa-keys "Direct link to RSA Keys")

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
    
    
    symbol=BTCUSDT&side=SELL&type=LIMIT&timeInForce=GTC&quantity=1&price=0.2&timestamp=1668481559918&recvWindow=5000  
    

After percent-encoding, the signature payload should look like this:
    
    
    symbol=BTCUSDT&side=SELL&type=LIMIT&timeInForce=GTC&quantity=1&price=0.2&timestamp=1668481559918&recvWindow=5000  
    

For the second set of example parameters (some non-ASCII characters), the `parameter=value` string should look like this:
    
    
    symbol=１２３４５６=SELL&type=LIMIT&timeInForce=GTC&quantity=1&price=0.2&timestamp=1668481559918&recvWindow=5000  
    

After percent-encoding, the signature payload should look like this:
    
    
    symbol=%EF%BC%91%EF%BC%92%EF%BC%93%EF%BC%94%EF%BC%95%EF%BC%96&side=SELL&type=LIMIT&timeInForce=GTC&quantity=1&price=0.2&timestamp=1668481559918&recvWindow=5000  
    

**Step 2: Compute the signature**

  1. Sign the signature payload constructed in Step 1 using the RSASSA-PKCS1-v1_5 algorithm with SHA-256 hash function.
  2. Encode the output in base64.



Note that the payload and the resulting `signature` are **case-sensitive**.

For the first set of example parameters (ASCII only):
    
    
    $  echo -n 'symbol=BTCUSDT&side=SELL&type=LIMIT&timeInForce=GTC&quantity=1&price=0.2&timestamp=1668481559918&recvWindow=5000' | openssl dgst -sha256 -sign ./test-prv-key.pem | openssl enc -base64 -A | tr -d '\n'  
    HZ8HOjiJ1s/igS9JA+n7+7Ti/ihtkRF5BIWcPIEluJP6tlbFM/Bf44LfZka/iemtahZAZzcO9TnI5uaXh3++lrqtNonCwp6/245UFWkiW1elpgtVAmJPbogcAv6rSlokztAfWk296ZJXzRDYAtzGH0gq7CgSJKfH+XxaCmR0WcvlKjNQnp12/eKXJYO4tDap8UCBLuyxDnR7oJKLHQHJLP0r0EAVOOSIbrFang/1WOq+Jaq4Efc4XpnTgnwlBbWTmhWDR1pvS9iVEzcSYLHT/fNnMRxFc7u+j3qI//5yuGuu14KR0MuQKKCSpViieD+fIti46sxPTsjSemoUKp0oXA==  
    

For the second set of example parameters (some non-ASCII characters):
    
    
    $  echo -n 'symbol=%EF%BC%91%EF%BC%92%EF%BC%93%EF%BC%94%EF%BC%95%EF%BC%96&side=SELL&type=LIMIT&timeInForce=GTC&quantity=1&price=0.2&timestamp=1668481559918&recvWindow=5000' | openssl dgst -sha256 -sign ./test-prv-key.pem | openssl enc -base64 -A | tr -d '\n'  
      
    qJtv66wyp/1mZE+mIFAAMUoTe8xkmLN7/eAZjuC9x1ocxovItHLl/sNK7Wq8QjgiHqGn0bb8P7yVvGBEd1gFe71NQ8aM0M+JNIMz5UFxfeA53rXjFlvsyH1Sig+OuO9Nz5nhCaJ6bEfj2iuv7w27pB3L8MVqmoCi6D9C/QMiLxtPaR70CxtnvoOlIgPmpv2bQy029A31NEK19ieVLkoyp1EUkXRaX3v0mohx8yMnUG1dhX9nUg3Oy8TYZ03DQy7kHDGkMKisNX7rt/GuGx1HIgjFclDGLsbAFIodvSLjm9FbseasMELoxlAJDlwRnW8zo5sQmL0Fz7ao935QBynrng==  
    

  3. Percent-encode the base64 string.



For the first set of example parameters (ASCII only):
    
    
    HZ8HOjiJ1s%2FigS9JA%2Bn7%2B7Ti%2FihtkRF5BIWcPIEluJP6tlbFM%2FBf44LfZka%2FiemtahZAZzcO9TnI5uaXh3%2B%2BlrqtNonCwp6%2F245UFWkiW1elpgtVAmJPbogcAv6rSlokztAfWk296ZJXzRDYAtzGH0gq7CgSJKfH%2BXxaCmR0WcvlKjNQnp12%2FeKXJYO4tDap8UCBLuyxDnR7oJKLHQHJLP0r0EAVOOSIbrFang%2F1WOq%2BJaq4Efc4XpnTgnwlBbWTmhWDR1pvS9iVEzcSYLHT%2FfNnMRxFc7u%2Bj3qI%2F%2F5yuGuu14KR0MuQKKCSpViieD%2BfIti46sxPTsjSemoUKp0oXA%3D%3D  
    

For the second set of example parameters (some non-ASCII characters):
    
    
    qJtv66wyp%2F1mZE%2BmIFAAMUoTe8xkmLN7%2FeAZjuC9x1ocxovItHLl%2FsNK7Wq8QjgiHqGn0bb8P7yVvGBEd1gFe71NQ8aM0M%2BJNIMz5UFxfeA53rXjFlvsyH1Sig%2BOuO9Nz5nhCaJ6bEfj2iuv7w27pB3L8MVqmoCi6D9C%2FQMiLxtPaR70CxtnvoOlIgPmpv2bQy029A31NEK19ieVLkoyp1EUkXRaX3v0mohx8yMnUG1dhX9nUg3Oy8TYZ03DQy7kHDGkMKisNX7rt%2FGuGx1HIgjFclDGLsbAFIodvSLjm9FbseasMELoxlAJDlwRnW8zo5sQmL0Fz7ao935QBynrng%3D%3D  
    

**Step 3: Add signature to the request**

Complete the request by adding the `signature` parameter to the query string.

For the first set of example parameters (ASCII only):
    
    
    curl -H "X-MBX-APIKEY: CAvIjXy3F44yW6Pou5k8Dy1swsYDWJZLeoK2r8G4cFDnE9nosRppc2eKc1T8TRTQ" -X POST 'https://api.binance.com/api/v3/order?symbol=BTCUSDT&side=SELL&type=LIMIT&timeInForce=GTC&quantity=1&price=0.2&timestamp=1668481559918&recvWindow=5000&signature=HZ8HOjiJ1s%2FigS9JA%2Bn7%2B7Ti%2FihtkRF5BIWcPIEluJP6tlbFM%2FBf44LfZka%2FiemtahZAZzcO9TnI5uaXh3%2B%2BlrqtNonCwp6%2F245UFWkiW1elpgtVAmJPbogcAv6rSlokztAfWk296ZJXzRDYAtzGH0gq7CgSJKfH%2BXxaCmR0WcvlKjNQnp12%2FeKXJYO4tDap8UCBLuyxDnR7oJKLHQHJLP0r0EAVOOSIbrFang%2F1WOq%2BJaq4Efc4XpnTgnwlBbWTmhWDR1pvS9iVEzcSYLHT%2FfNnMRxFc7u%2Bj3qI%2F%2F5yuGuu14KR0MuQKKCSpViieD%2BfIti46sxPTsjSemoUKp0oXA%3D%3D'  
    

For the second set of example parameters (some non-ASCII characters):
    
    
    curl -H "X-MBX-APIKEY: CAvIjXy3F44yW6Pou5k8Dy1swsYDWJZLeoK2r8G4cFDnE9nosRppc2eKc1T8TRTQ" -X POST 'https://api.binance.com/api/v3/order?symbol=%EF%BC%91%EF%BC%92%EF%BC%93%EF%BC%94%EF%BC%95%EF%BC%96&side=SELL&type=LIMIT&timeInForce=GTC&quantity=1&price=0.2&timestamp=1668481559918&recvWindow=5000&signature=qJtv66wyp%2F1mZE%2BmIFAAMUoTe8xkmLN7%2FeAZjuC9x1ocxovItHLl%2FsNK7Wq8QjgiHqGn0bb8P7yVvGBEd1gFe71NQ8aM0M%2BJNIMz5UFxfeA53rXjFlvsyH1Sig%2BOuO9Nz5nhCaJ6bEfj2iuv7w27pB3L8MVqmoCi6D9C%2FQMiLxtPaR70CxtnvoOlIgPmpv2bQy029A31NEK19ieVLkoyp1EUkXRaX3v0mohx8yMnUG1dhX9nUg3Oy8TYZ03DQy7kHDGkMKisNX7rt%2FGuGx1HIgjFclDGLsbAFIodvSLjm9FbseasMELoxlAJDlwRnW8zo5sQmL0Fz7ao935QBynrng%3D%3D'  
    

Here is a sample Bash script performing all the steps above:
    
    
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
    

#### Ed25519 Keys[​](/docs/convert/general-info#ed25519-keys "Direct link to Ed25519 Keys")

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
    
    
    symbol=BTCUSDT&side=SELL&type=LIMIT&timeInForce=GTC&quantity=1&price=0.2&timestamp=1668481559918&recvWindow=5000  
    

After percent-encoding, the signature payload should look like this:
    
    
    symbol=BTCUSDT&side=SELL&type=LIMIT&timeInForce=GTC&quantity=1&price=0.2&timestamp=1668481559918&recvWindow=5000  
    

For the second set of example parameters (some non-ASCII characters), the `parameter=value` string should look like this:
    
    
    symbol=１２３４５６&side=SELL&type=LIMIT&timeInForce=GTC&quantity=1&price=0.2&timestamp=1668481559918&recvWindow=5000  
    

After percent-encoding, the signature payload should look like this:
    
    
    symbol=%EF%BC%91%EF%BC%92%EF%BC%93%EF%BC%94%EF%BC%95%EF%BC%96&side=SELL&type=LIMIT&timeInForce=GTC&quantity=1&price=0.2&timestamp=1668481559918&recvWindow=5000  
    

**Step 2: Compute the signature**

  1. Sign the payload.
  2. Encode the output as a base64 string.



Note that the payload and the resulting `signature` are **case-sensitive**.

For the first set of example parameters (ASCII only):
    
    
    echo -n "symbol=BTCUSDT&side=SELL&type=LIMIT&timeInForce=GTC&quantity=1&price=0.2&timestamp=1668481559918&recvWindow=5000" | openssl dgst -keyform PEM -sha256 -sign ./test-prv-key.pem | openssl enc -base64 | tr -d '\n'  
      
    HaZnek7KOGa/k5+f6Q1nw8lzMUpo36mRVvvLHCMUCXxlmdQQGZge1luAUKnleD/DYeD19YrqzeHbb6xU3MkSIXKhAO1MaYq48uGVYb3vJScEZVOutgMInrZzUcCWNulNkfcbmExSiymCZ5xQBw5QDuzpuDFqRZ1Xt+BZxEHBN9OYQKpoe0+ovjnXyVOaH8VUKhE/ghUWnThrXJr+hmSc5t7ggjiVPQc7pGn3qSNGCQwdpkQC9GHMr/r+8n6qeEKMYB5j/1wC4d8Jae8FQiU8xcXR0NlUgV2LAw61/ZJv5BTJpa+z5Lv1W9v6jHQWRX2O8uaG3KU/lR3spR7+oGlWOw=  
    

For the second set of example parameters (some non-ASCII characters):
    
    
    echo -n "symbol=%EF%BC%91%EF%BC%92%EF%BC%93%EF%BC%94%EF%BC%95%EF%BC%96&side=SELL&type=LIMIT&timeInForce=GTC&quantity=1&price=0.2&timestamp=1668481559918&recvWindow=5000" | openssl dgst -keyform PEM -sha256 -sign ./test-prv-key.pem | openssl enc -base64 | tr -d '\n'  
      
    qJtv66wyp/1mZE+mIFAAMUoTe8xkmLN7/eAZjuC9x1ocxovItHLl/sNK7Wq8QjgiHqGn0bb8P7yVvGBEd1gFe71NQ8aM0M+JNIMz5UFxfeA53rXjFlvsyH1Sig+OuO9Nz5nhCaJ6bEfj2iuv7w27pB3L8MVqmoCi6D9C/QMiLxtPaR70CxtnvoOlIgPmpv2bQy029A31NEK19ieVLkoyp1EUkXRaX3v0mohx8yMnUG1dhX9nUg3Oy8TYZ03DQy7kHDGkMKisNX7rt/GuGx1HIgjFclDGLsbAFIodvSLjm9FbseasMELoxlAJDlwRnW8zo5sQmL0Fz7ao935QBynrng==  
    

  3. Percent-encode the base64 string.



For the first set of example parameters (ASCII only):
    
    
    HaZnek7KOGa%2Fk5%2Bf6Q1nw8lzMUpo36mRVvvLHCMUCXxlmdQQGZge1luAUKnleD%2FDYeD19YrqzeHbb6xU3MkSIXKhAO1MaYq48uGVYb3vJScEZVOutgMInrZzUcCWNulNkfcbmExSiymCZ5xQBw5QDuzpuDFqRZ1Xt%2BBZxEHBN9OYQKpoe0%2BovjnXyVOaH8VUKhE%2FghUWnThrXJr%2BhmSc5t7ggjiVPQc7pGn3qSNGCQwdpkQC9GHMr%2Fr%2B8n6qeEKMYB5j%2F1wC4d8Jae8FQiU8xcXR0NlUgV2LAw61%2FZJv5BTJpa%2Bz5Lv1W9v6jHQWRX2O8uaG3KU%2FlR3spR7%2BoGlWOw%3D  
    

For the second set of example parameters (some non-ASCII characters):
    
    
    qJtv66wyp%2F1mZE%2BmIFAAMUoTe8xkmLN7%2FeAZjuC9x1ocxovItHLl%2FsNK7Wq8QjgiHqGn0bb8P7yVvGBEd1gFe71NQ8aM0M%2BJNIMz5UFxfeA53rXjFlvsyH1Sig%2BOuO9Nz5nhCaJ6bEfj2iuv7w27pB3L8MVqmoCi6D9C%2FQMiLxtPaR70CxtnvoOlIgPmpv2bQy029A31NEK19ieVLkoyp1EUkXRaX3v0mohx8yMnUG1dhX9nUg3Oy8TYZ03DQy7kHDGkMKisNX7rt%2FGuGx1HIgjFclDGLsbAFIodvSLjm9FbseasMELoxlAJDlwRnW8zo5sQmL0Fz7ao935QBynrng%3D%3D  
    

**Step 3: Add signature to the request**

Complete the request by adding the `signature` parameter to the query string.

For the first set of example parameters (ASCII only):
    
    
    curl -H "X-MBX-APIKEY: 4yNzx3yWC5bS6YTwEkSRaC0nRmSQIIStAUOh1b6kqaBrTLIhjCpI5lJH8q8R8WNO" -X POST 'https://api.binance.com/api/v3/order?symbol=BTCUSDT&side=SELL&type=LIMIT&timeInForce=GTC&quantity=1&price=0.2&timestamp=1668481559918&recvWindow=5000&signature=HaZnek7KOGa%2Fk5%2Bf6Q1nw8lzMUpo36mRVvvLHCMUCXxlmdQQGZge1luAUKnleD%2FDYeD19YrqzeHbb6xU3MkSIXKhAO1MaYq48uGVYb3vJScEZVOutgMInrZzUcCWNulNkfcbmExSiymCZ5xQBw5QDuzpuDFqRZ1Xt%2BBZxEHBN9OYQKpoe0%2BovjnXyVOaH8VUKhE%2FghUWnThrXJr%2BhmSc5t7ggjiVPQc7pGn3qSNGCQwdpkQC9GHMr%2Fr%2B8n6qeEKMYB5j%2F1wC4d8Jae8FQiU8xcXR0NlUgV2LAw61%2FZJv5BTJpa%2Bz5Lv1W9v6jHQWRX2O8uaG3KU%2FlR3spR7%2BoGlWOw%3D'  
    

For the second set of example parameters (some non-ASCII characters):
    
    
    curl -H "X-MBX-APIKEY: 4yNzx3yWC5bS6YTwEkSRaC0nRmSQIIStAUOh1b6kqaBrTLIhjCpI5lJH8q8R8WNO" -X POST 'https://api.binance.com/api/v3/order?symbol=%EF%BC%91%EF%BC%92%EF%BC%93%EF%BC%94%EF%BC%95%EF%BC%96&&side=SELL&type=LIMIT&timeInForce=GTC&quantity=1&price=0.2&timestamp=1668481559918&recvWindow=5000&signature=qJtv66wyp%2F1mZE%2BmIFAAMUoTe8xkmLN7%2FeAZjuC9x1ocxovItHLl%2FsNK7Wq8QjgiHqGn0bb8P7yVvGBEd1gFe71NQ8aM0M%2BJNIMz5UFxfeA53rXjFlvsyH1Sig%2BOuO9Nz5nhCaJ6bEfj2iuv7w27pB3L8MVqmoCi6D9C%2FQMiLxtPaR70CxtnvoOlIgPmpv2bQy029A31NEK19ieVLkoyp1EUkXRaX3v0mohx8yMnUG1dhX9nUg3Oy8TYZ03DQy7kHDGkMKisNX7rt%2FGuGx1HIgjFclDGLsbAFIodvSLjm9FbseasMELoxlAJDlwRnW8zo5sQmL0Fz7ao935QBynrng%3D%3D'  
    

Here is a sample Python script performing all the steps above:
    
    
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
    

A sample Bash script containing similar steps is available in the right side.

---

# 基本信息

## API 基本信息[​](/docs/zh-CN/convert/general-info#api-基本信息 "API 基本信息的直接链接")

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



### HTTP 返回代码[​](/docs/zh-CN/convert/general-info#http-返回代码 "HTTP 返回代码的直接链接")

  * HTTP `4XX` 错误码用于指示错误的请求内容、行为、格式。问题在于请求者。
  * HTTP `403` 错误码表示违反WAF限制(Web应用程序防火墙)。
  * HTTP `409` 错误码表示重新下单(cancelReplace)的请求部分成功。(比如取消订单失败，但是下单成功了)
  * HTTP `429` 错误码表示警告访问频次超限，即将被封IP。
  * HTTP `418` 表示收到429后继续访问，于是被封了。
  * HTTP `5XX` 错误码用于指示Binance服务侧的问题。



### 接口错误代码[​](/docs/zh-CN/convert/general-info#接口错误代码 "接口错误代码的直接链接")

  * 使用接口 `/api/v3`, 以及 `/sapi/v1/margin`时, 每个接口都有可能抛出异常;



> API 与 SAPI 的错误代码返回形式如下:
    
    
    {  
      "code": -1121,  
      "msg": "Invalid symbol."  
    }  
    

  * 具体的错误码及其解释在 [错误代码](/docs/zh-CN/convert/general-info#cf68bca02a).



### 接口的基本信息[​](/docs/zh-CN/convert/general-info#接口的基本信息 "接口的基本信息的直接链接")

  * `GET` 方法的接口, 参数必须在 `query string`中发送。
  * `POST`, `PUT`, 和 `DELETE` 方法的接口,参数可以在内容形式为`application/x-www-form-urlencoded`的 `query string` 中发送，也可以在 `request body` 中发送。 如果你喜欢，也可以混合这两种方式发送参数。
  * 对参数的顺序不做要求。
  * 但如果同一个参数名在query string和request body中都有，query string中的会被优先采用。



* * *

## 访问限制[​](/docs/zh-CN/convert/general-info#访问限制 "访问限制的直接链接")

### 访问限制基本信息[​](/docs/zh-CN/convert/general-info#访问限制基本信息 "访问限制基本信息的直接链接")

  * 以下 是`intervalLetter` 作为头部值:

    * SECOND => S
    * MINUTE => M
    * HOUR => H
    * DAY => D
  * 在 `/api/v3/exchangeInfo` `rateLimits` 数组中包含与交易的有关RAW_REQUESTS，REQUEST_WEIGHT和ORDERS速率限制相关的对象。这些在 `限制种类 (rateLimitType)` 下的 `枚举定义` 部分中进一步定义。

  * 违反任何一个速率限制时（访问频次限制或下单速率限制），将返回429。




### IP 访问限制[​](/docs/zh-CN/convert/general-info#ip-访问限制 "IP 访问限制的直接链接")

  * 每个请求将包含一个`X-MBX-USED-WEIGHT-(intervalNum)(intervalLetter)`的头，其中包含当前IP所有请求的已使用权重。
  * 每一个接口均有一个相应的权重(weight)，有的接口根据参数不同可能拥有不同的权重。越消耗资源的接口权重就会越大。
  * 收到429时，您有责任停止发送请求，不得滥用API。
  * **收到429后仍然继续违反访问限制，会被封禁IP，并收到418错误码**
  * 频繁违反限制，封禁时间会逐渐延长，**从最短2分钟到最长3天** 。
  * `Retry-After`的头会与带有418或429的响应发送，并且会给出**以秒为单位** 的等待时长(如果是429)以防止禁令，或者如果是418，直到禁令结束。
  * **访问限制是基于IP的，而不是API Key**

建议您尽可能多地使用websocket消息获取相应数据，以减少请求带来的访问限制压力。 

###下单频率限制

  * 每个成功的下单回报将包含一个`X-MBX-ORDER-COUNT-(intervalNum)(intervalLetter)`的头，其中包含当前账户已用的下单限制数量。
  * 当下单数超过限制时，会收到带有429但不含`Retry-After`头的响应。请检查 `GET api/v3/exchangeInfo` 的下单频率限制 (rateLimitType = ORDERS) 并等待封禁时间结束。
  * 被拒绝或不成功的下单并不保证回报中包含以上头内容。
  * **下单频率限制是基于每个账户计数的。**
  * 用户可以通过接口 `GET api/v3/rateLimit/order` 来查询当前的下单量.



### WEB SOCKET 连接限制[​](/docs/zh-CN/convert/general-info#web-socket-连接限制 "WEB SOCKET 连接限制的直接链接")

  * Websocket服务器每秒最多接受5个消息。消息包括: 
    * PING帧
    * PONG帧
    * JSON格式的消息, 比如订阅, 断开订阅.
  * 如果用户发送的消息超过限制，连接会被断开连接。反复被断开连接的IP有可能被服务器屏蔽。
  * 单个连接最多可以订阅 **1024** 个Streams。
  * 每IP地址、每5分钟最多可以发送300次连接请求。



### /api/ 与 /sapi/ 接口限频说明[​](/docs/zh-CN/convert/general-info#api-与-sapi-接口限频说明 "/api/ 与 /sapi/ 接口限频说明的直接链接")

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

## 数据来源[​](/docs/zh-CN/convert/general-info#数据来源 "数据来源的直接链接")

  * 因为API系统是异步的, 所以返回的数据有延时很正常, 也在预期之中。
  * 在每个接口中，都列出了其数据的来源，可以用于理解数据的时效性。



系统一共有3个数据来源，按照更新速度的先后排序。排在前面的数据最新，在后面就有可能存在延迟。

  * **撮合引擎** \- 表示数据来源于撮合引擎
  * **缓存** \- 表示数据来源于内部或者外部的缓存
  * **数据库** \- 表示数据直接来源于数据库

有些接口有不止一个数据源, 比如 `缓存 => 数据库`, 这表示接口会先从第一个数据源检查，如果没有数据，则检查下一个数据源。 

## 请求鉴权类型[​](/docs/zh-CN/convert/general-info#请求鉴权类型 "请求鉴权类型的直接链接")

  * 每个接口都有一个鉴权类型，指示所需的 API 密钥权限，显示在接口名称旁边（例如，[下新订单 (TRADE)](/docs/zh-CN/convert/general-info#place-new-order-trade)）。
  * 如果未指定，则鉴权类型为 `NONE`。
  * 除了为 `NONE` 外，所有具有鉴权类型的接口均视为 `SIGNED` 请求（即包含 `signature`），[listenKey 管理](/docs/zh-CN/convert/general-info#user-data-stream-requests) 除外。
  * 具有鉴权类型的接口需要提供有效的 API 密钥并验证通过。 
    * API 密钥可在您的 Binance 账户的 [API 管理](https://www.binance.com/en/support/faq/360002502072) 页面创建。
    * **API 密钥和密钥对均为敏感信息，切勿与他人分享。** 如果发现账户有异常活动，请立即撤销所有密钥并联系 Binance 支持。
  * API 密钥可配置为仅允许访问某些鉴权接口。 
    * 例如，您可以拥有具有 `TRADE` 权限的 API 密钥用于交易， 同时使用具有 `USER_DATA` 权限的另一个 API 密钥来监控订单状态。
    * 默认情况下，API 密钥无法进行 `TRADE`，您需要先在 API 管理中启用交易权限。

鉴权类型| 描述  
---|---  
NONE| 不需要鉴权的接口  
TRADE| 需要有效的 API-Key 和签名  
MARGIN| 需要有效的 API-Key 和签名  
USER_DATA| 需要有效的 API-Key 和签名  
USER_STREAM| 需要有效的 API-Key  
MARKET_DATA| 需要有效的 API-Key  
  
### 需要签名的接口[​](/docs/zh-CN/convert/general-info#需要签名的接口 "需要签名的接口的直接链接")

  * 调用`SIGNED` 接口时，除了接口本身所需的参数外，还需要在 `query string` 或 `request body` 中传递 `signature`, 即签名参数。



#### 签名是否是大小写敏感的[​](/docs/zh-CN/convert/general-info#签名是否是大小写敏感的 "签名是否��是大小写敏感的的直接链接")

  * **HMAC：** 使用 HMAC 生成的签名**不区分大小写** 。这意味着无论字母大小写如何，签名字符串都可以被验证。
  * **RSA：** 使用 RSA 生成的签名是**大小写敏感的** 。
  * **Ed25519：** 使用 Ed25519 生成的签名也是**大小写敏感的** 。



请参阅[已签名请求示例 (HMAC)](/docs/zh-CN/convert/general-info#hmac-keys)、[已签名请求示例 (RSA)](/docs/zh-CN/convert/general-info#rsa-keys) 和[已签名请求示例 (Ed25519)](/docs/zh-CN/convert/general-info#ed25519-keys)，了解如何根据您使用的 API 密钥类型计算签名。

### 时间同步安全[​](/docs/zh-CN/convert/general-info#时间同步安全 "时间同步安全的直接链接")

  * `SIGNED` 请求还需要一个 `timestamp` 参数，该参数应为当前时间戳，单位为毫秒或微秒。（参见 [通用 API 信息](/docs/zh-CN/convert/general-info#general-api-information)）
  * 另一个可选参数 `recvWindow`，用以指定请求的有效期，只能以毫秒为单位。 
    * `recvWindow` 扩展为三位小数（例如 6000.346），以便可以指定微秒。
    * 如果未发送 `recvWindow`，则 **默认值为 5000 毫秒** 。
    * `recvWindow` 的最大值为 60000 毫秒。
  * 请求处理逻辑如下：


    
    
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

### POST /api/v3/order 的签名示例[​](/docs/zh-CN/convert/general-info#post-apiv3order-的签名示例 "POST /api/v3/order 的签名示例的直接链接")

#### HMAC Keys[​](/docs/zh-CN/convert/general-info#hmac-keys "HMAC Keys的直接链接")

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
    
    
    symbol=LTCBTC&side=BUY&type=LIMIT&timeInForce=GTC&quantity=1&price=0.1&recvWindow=5000&timestamp=1499827319559  
    

对字符串进行百分比编码（percent-encoded）后，签名 payload 如下所示：
    
    
    symbol=LTCBTC&side=BUY&type=LIMIT&timeInForce=GTC&quantity=1&price=0.1&recvWindow=5000&timestamp=1499827319559  
    

对于第二组示例参数（包含一些 Unicode 字符），`parameter=value` 字符串将如下所示：
    
    
    symbol=１２３４５６&side=BUY&type=LIMIT&timeInForce=GTC&quantity=1&price=0.1&recvWindow=5000&timestamp=1499827319559  
    

对字符串进行百分比编码（percent-encoded）后，签名 payload 如下所示：
    
    
    symbol=%EF%BC%91%EF%BC%92%EF%BC%93%EF%BC%94%EF%BC%95%EF%BC%96&side=BUY&type=LIMIT&timeInForce=GTC&quantity=1&price=0.1&recvWindow=5000&timestamp=1499827319559  
    

**第二步: 计算签名。**

  1. 使用 API 密钥中的 `secretKey` 作为 HMAC-SHA-256 算法的签名密钥。
  2. 对步骤 1 中构建的签名 payload 进行签名。
  3. 将 HMAC-SHA-256 的输出编码为十六进制字符串。



请注意，`secretKey` 和 payload 是**大小写敏感的** ，而生成的签名值是不区分大小写的。

**示例命令**

对于第一组示例参数（仅限 ASCII 字符）：
    
    
    $ echo -n "symbol=LTCBTC&side=BUY&type=LIMIT&timeInForce=GTC&quantity=1&price=0.1&recvWindow=5000&timestamp=1499827319559" | openssl dgst -sha256 -hmac "NhqPtmdSJYdKjVHjA7PZj4Mge3R5YNiP1e3UZjInClVN65XAbvqqM6A7H5fATj0j"  
      
    c8db56825ae71d6d79447849e617115f4a920fa2acdcab2b053c4b2838bd6b71  
    

对于第二组示例参数（包含一些 Unicode 字符）：
    
    
    $ echo -n "symbol=%EF%BC%91%EF%BC%92%EF%BC%93%EF%BC%94%EF%BC%95%EF%BC%96&side=BUY&type=LIMIT&timeInForce=GTC&quantity=1&price=0.1&recvWindow=5000&timestamp=1499827319559" | openssl dgst -sha256 -hmac "NhqPtmdSJYdKjVHjA7PZj4Mge3R5YNiP1e3UZjInClVN65XAbvqqM6A7H5fATj0j"  
      
    e1353ec6b14d888f1164ae9af8228a3dbd508bc82eb867db8ab6046442f33ef3  
    

**第三步: 为请求添加签名**

通过在查询字符串中添加 `signature` 参数来完成请求。

对于第一组示例参数（仅限 ASCII 字符）：
    
    
    curl -s -v -H "X-MBX-APIKEY: $apiKey" -X POST "https://api.binance.com/api/v3/order?symbol=LTCBTC&side=BUY&type=LIMIT&timeInForce=GTC&quantity=1&price=0.1&recvWindow=5000&timestamp=1499827319559&signature=c8db56825ae71d6d79447849e617115f4a920fa2acdcab2b053c4b2838bd6b71"  
    

对于第二组示例参数（包含一些 Unicode 字符）：
    
    
    curl -s -v -H "X-MBX-APIKEY: $apiKey" -X POST "https://api.binance.com/api/v3/order?symbol=%EF%BC%91%EF%BC%92%EF%BC%93%EF%BC%94%EF%BC%95%EF%BC%96&side=BUY&type=LIMIT&timeInForce=GTC&quantity=1&price=0.1&recvWindow=5000&timestamp=1499827319559&signature=e1353ec6b14d888f1164ae9af8228a3dbd508bc82eb867db8ab6046442f33ef3"  
    

以下是一个执行上述所有步骤的 Bash 脚本示例：
    
    
    apiKey="vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A"  
    secretKey="NhqPtmdSJYdKjVHjA7PZj4Mge3R5YNiP1e3UZjInClVN65XAbvqqM6A7H5fATj0j"  
      
    payload="symbol=LTCBTC&side=BUY&type=LIMIT&timeInForce=GTC&quantity=1&price=0.1&recvWindow=5000&timestamp=1499827319559"  
      
    # 对请求进行签名  
      
    signature=$(echo -n "$payload" | openssl dgst -sha256 -hmac "$secretKey")  
    signature=${signature#*= }    # Keep only the part after the "= "  
      
    # 发送请求  
      
    curl -H "X-MBX-APIKEY: $apiKey" -X POST "https://api.binance.com/api/v3/order?$payload&signature=$signature"  
      
    

#### RSA Keys[​](/docs/zh-CN/convert/general-info#rsa-keys "RSA Keys的直接链接")

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
    
    
    symbol=BTCUSDT&side=SELL&type=LIMIT&timeInForce=GTC&quantity=1&price=0.2&timestamp=1668481559918&recvWindow=5000  
    

对字符串进行百分比编码（percent-encoded）后，签名 payload 如下所示：
    
    
    symbol=BTCUSDT&side=SELL&type=LIMIT&timeInForce=GTC&quantity=1&price=0.2&timestamp=1668481559918&recvWindow=5000  
    

对于第二组示例参数（包含一些 Unicode 字符），`parameter=value` 字符串将如下所示：
    
    
    symbol=１２３４５６=SELL&type=LIMIT&timeInForce=GTC&quantity=1&price=0.2&timestamp=1668481559918&recvWindow=5000  
    

对字符串进行百分比编码（percent-encoded）后，签名 payload 如下所示：
    
    
    symbol=%EF%BC%91%EF%BC%92%EF%BC%93%EF%BC%94%EF%BC%95%EF%BC%96&side=SELL&type=LIMIT&timeInForce=GTC&quantity=1&price=0.2&timestamp=1668481559918&recvWindow=5000  
    

**第二步: 计算签名。**

  1. 使用 RSASSA-PKCS1-v1_5 算法和 SHA-256 哈希函数对步骤 1 中构建的签名 payload 进行签名。
  2. 将输出结果编码为 base64 格式。



请注意，payload 和生成的`签名值`是**大小写敏感的** 。

对于第一组示例参数（仅限 ASCII 字符）：
    
    
    $  echo -n 'symbol=BTCUSDT&side=SELL&type=LIMIT&timeInForce=GTC&quantity=1&price=0.2&timestamp=1668481559918&recvWindow=5000' | openssl dgst -sha256 -sign ./test-prv-key.pem | openssl enc -base64 -A | tr -d '\n'  
    HZ8HOjiJ1s/igS9JA+n7+7Ti/ihtkRF5BIWcPIEluJP6tlbFM/Bf44LfZka/iemtahZAZzcO9TnI5uaXh3++lrqtNonCwp6/245UFWkiW1elpgtVAmJPbogcAv6rSlokztAfWk296ZJXzRDYAtzGH0gq7CgSJKfH+XxaCmR0WcvlKjNQnp12/eKXJYO4tDap8UCBLuyxDnR7oJKLHQHJLP0r0EAVOOSIbrFang/1WOq+Jaq4Efc4XpnTgnwlBbWTmhWDR1pvS9iVEzcSYLHT/fNnMRxFc7u+j3qI//5yuGuu14KR0MuQKKCSpViieD+fIti46sxPTsjSemoUKp0oXA==  
    

对于第二组示例参数（包含一些 Unicode 字符）：
    
    
    $  echo -n 'symbol=%EF%BC%91%EF%BC%92%EF%BC%93%EF%BC%94%EF%BC%95%EF%BC%96&side=SELL&type=LIMIT&timeInForce=GTC&quantity=1&price=0.2&timestamp=1668481559918&recvWindow=5000' | openssl dgst -sha256 -sign ./test-prv-key.pem | openssl enc -base64 -A | tr -d '\n'  
      
    qJtv66wyp/1mZE+mIFAAMUoTe8xkmLN7/eAZjuC9x1ocxovItHLl/sNK7Wq8QjgiHqGn0bb8P7yVvGBEd1gFe71NQ8aM0M+JNIMz5UFxfeA53rXjFlvsyH1Sig+OuO9Nz5nhCaJ6bEfj2iuv7w27pB3L8MVqmoCi6D9C/QMiLxtPaR70CxtnvoOlIgPmpv2bQy029A31NEK19ieVLkoyp1EUkXRaX3v0mohx8yMnUG1dhX9nUg3Oy8TYZ03DQy7kHDGkMKisNX7rt/GuGx1HIgjFclDGLsbAFIodvSLjm9FbseasMELoxlAJDlwRnW8zo5sQmL0Fz7ao935QBynrng==  
    

  3. 对 base64 格式的字符串进行百分比编码（percent-encoded）。



对于第一组示例参数（仅限 ASCII 字符）：
    
    
    HZ8HOjiJ1s%2FigS9JA%2Bn7%2B7Ti%2FihtkRF5BIWcPIEluJP6tlbFM%2FBf44LfZka%2FiemtahZAZzcO9TnI5uaXh3%2B%2BlrqtNonCwp6%2F245UFWkiW1elpgtVAmJPbogcAv6rSlokztAfWk296ZJXzRDYAtzGH0gq7CgSJKfH%2BXxaCmR0WcvlKjNQnp12%2FeKXJYO4tDap8UCBLuyxDnR7oJKLHQHJLP0r0EAVOOSIbrFang%2F1WOq%2BJaq4Efc4XpnTgnwlBbWTmhWDR1pvS9iVEzcSYLHT%2FfNnMRxFc7u%2Bj3qI%2F%2F5yuGuu14KR0MuQKKCSpViieD%2BfIti46sxPTsjSemoUKp0oXA%3D%3D  
    

对于第二组示例参数（包含一些 Unicode 字符）：
    
    
    qJtv66wyp%2F1mZE%2BmIFAAMUoTe8xkmLN7%2FeAZjuC9x1ocxovItHLl%2FsNK7Wq8QjgiHqGn0bb8P7yVvGBEd1gFe71NQ8aM0M%2BJNIMz5UFxfeA53rXjFlvsyH1Sig%2BOuO9Nz5nhCaJ6bEfj2iuv7w27pB3L8MVqmoCi6D9C%2FQMiLxtPaR70CxtnvoOlIgPmpv2bQy029A31NEK19ieVLkoyp1EUkXRaX3v0mohx8yMnUG1dhX9nUg3Oy8TYZ03DQy7kHDGkMKisNX7rt%2FGuGx1HIgjFclDGLsbAFIodvSLjm9FbseasMELoxlAJDlwRnW8zo5sQmL0Fz7ao935QBynrng%3D%3D  
    

**第三步: 为请求添加签名**

通过在查询字符串中添加 `signature` 参数来完成请求。

对于第一组示例参数（仅限 ASCII 字符）：
    
    
    curl -H "X-MBX-APIKEY: CAvIjXy3F44yW6Pou5k8Dy1swsYDWJZLeoK2r8G4cFDnE9nosRppc2eKc1T8TRTQ" -X POST 'https://api.binance.com/api/v3/order?symbol=BTCUSDT&side=SELL&type=LIMIT&timeInForce=GTC&quantity=1&price=0.2&timestamp=1668481559918&recvWindow=5000&signature=HZ8HOjiJ1s%2FigS9JA%2Bn7%2B7Ti%2FihtkRF5BIWcPIEluJP6tlbFM%2FBf44LfZka%2FiemtahZAZzcO9TnI5uaXh3%2B%2BlrqtNonCwp6%2F245UFWkiW1elpgtVAmJPbogcAv6rSlokztAfWk296ZJXzRDYAtzGH0gq7CgSJKfH%2BXxaCmR0WcvlKjNQnp12%2FeKXJYO4tDap8UCBLuyxDnR7oJKLHQHJLP0r0EAVOOSIbrFang%2F1WOq%2BJaq4Efc4XpnTgnwlBbWTmhWDR1pvS9iVEzcSYLHT%2FfNnMRxFc7u%2Bj3qI%2F%2F5yuGuu14KR0MuQKKCSpViieD%2BfIti46sxPTsjSemoUKp0oXA%3D%3D'  
    

对于第二组示例参数（包含一些 Unicode 字符）：
    
    
    curl -H "X-MBX-APIKEY: CAvIjXy3F44yW6Pou5k8Dy1swsYDWJZLeoK2r8G4cFDnE9nosRppc2eKc1T8TRTQ" -X POST 'https://api.binance.com/api/v3/order?symbol=%EF%BC%91%EF%BC%92%EF%BC%93%EF%BC%94%EF%BC%95%EF%BC%96&side=SELL&type=LIMIT&timeInForce=GTC&quantity=1&price=0.2&timestamp=1668481559918&recvWindow=5000&signature=qJtv66wyp%2F1mZE%2BmIFAAMUoTe8xkmLN7%2FeAZjuC9x1ocxovItHLl%2FsNK7Wq8QjgiHqGn0bb8P7yVvGBEd1gFe71NQ8aM0M%2BJNIMz5UFxfeA53rXjFlvsyH1Sig%2BOuO9Nz5nhCaJ6bEfj2iuv7w27pB3L8MVqmoCi6D9C%2FQMiLxtPaR70CxtnvoOlIgPmpv2bQy029A31NEK19ieVLkoyp1EUkXRaX3v0mohx8yMnUG1dhX9nUg3Oy8TYZ03DQy7kHDGkMKisNX7rt%2FGuGx1HIgjFclDGLsbAFIodvSLjm9FbseasMELoxlAJDlwRnW8zo5sQmL0Fz7ao935QBynrng%3D%3D'  
    

以下是一个执行上述所有步骤的 Bash 脚本示例：
    
    
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
    

#### Ed25519 Keys[​](/docs/zh-CN/convert/general-info#ed25519-keys "Ed25519 Keys的直接链接")

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
    
    
    symbol=BTCUSDT&side=SELL&type=LIMIT&timeInForce=GTC&quantity=1&price=0.2&timestamp=1668481559918&recvWindow=5000  
    

对字符串进行百分比编码（percent-encoded）后，签名 payload 如下所示：
    
    
    symbol=BTCUSDT&side=SELL&type=LIMIT&timeInForce=GTC&quantity=1&price=0.2&timestamp=1668481559918&recvWindow=5000  
    

对于第二组示例参数（包含一些 Unicode 字符），`parameter=value` 字符串将如下所示：
    
    
    symbol=１２３４５６&side=SELL&type=LIMIT&timeInForce=GTC&quantity=1&price=0.2&timestamp=1668481559918&recvWindow=5000  
    

对字符串进行百分比编码（percent-encoded）后，签名 payload 如下所示：
    
    
    symbol=%EF%BC%91%EF%BC%92%EF%BC%93%EF%BC%94%EF%BC%95%EF%BC%96&side=SELL&type=LIMIT&timeInForce=GTC&quantity=1&price=0.2&timestamp=1668481559918&recvWindow=5000  
    

**第二步: 计算签名。**

  1. 对 payload 进行签名。
  2. 将输出结果编码为 base64 格式。



请注意，payload 和生成的`签名值`是**大小写敏感的** 。

对于第一组示例参数（仅限 ASCII 字符）：
    
    
    echo -n "symbol=BTCUSDT&side=SELL&type=LIMIT&timeInForce=GTC&quantity=1&price=0.2&timestamp=1668481559918&recvWindow=5000" | openssl dgst -keyform PEM -sha256 -sign ./test-prv-key.pem | openssl enc -base64 | tr -d '\n'  
      
    HaZnek7KOGa/k5+f6Q1nw8lzMUpo36mRVvvLHCMUCXxlmdQQGZge1luAUKnleD/DYeD19YrqzeHbb6xU3MkSIXKhAO1MaYq48uGVYb3vJScEZVOutgMInrZzUcCWNulNkfcbmExSiymCZ5xQBw5QDuzpuDFqRZ1Xt+BZxEHBN9OYQKpoe0+ovjnXyVOaH8VUKhE/ghUWnThrXJr+hmSc5t7ggjiVPQc7pGn3qSNGCQwdpkQC9GHMr/r+8n6qeEKMYB5j/1wC4d8Jae8FQiU8xcXR0NlUgV2LAw61/ZJv5BTJpa+z5Lv1W9v6jHQWRX2O8uaG3KU/lR3spR7+oGlWOw=  
    

对于第二组示例参数（包含一些 Unicode 字符）：
    
    
    echo -n "symbol=%EF%BC%91%EF%BC%92%EF%BC%93%EF%BC%94%EF%BC%95%EF%BC%96&side=SELL&type=LIMIT&timeInForce=GTC&quantity=1&price=0.2&timestamp=1668481559918&recvWindow=5000" | openssl dgst -keyform PEM -sha256 -sign ./test-prv-key.pem | openssl enc -base64 | tr -d '\n'  
      
    qJtv66wyp/1mZE+mIFAAMUoTe8xkmLN7/eAZjuC9x1ocxovItHLl/sNK7Wq8QjgiHqGn0bb8P7yVvGBEd1gFe71NQ8aM0M+JNIMz5UFxfeA53rXjFlvsyH1Sig+OuO9Nz5nhCaJ6bEfj2iuv7w27pB3L8MVqmoCi6D9C/QMiLxtPaR70CxtnvoOlIgPmpv2bQy029A31NEK19ieVLkoyp1EUkXRaX3v0mohx8yMnUG1dhX9nUg3Oy8TYZ03DQy7kHDGkMKisNX7rt/GuGx1HIgjFclDGLsbAFIodvSLjm9FbseasMELoxlAJDlwRnW8zo5sQmL0Fz7ao935QBynrng==  
    

  3. 对 base64 格式的字符串进行百分比编码（percent-encoded）。



对于第一组示例参数（仅限 ASCII 字符）：
    
    
    HaZnek7KOGa%2Fk5%2Bf6Q1nw8lzMUpo36mRVvvLHCMUCXxlmdQQGZge1luAUKnleD%2FDYeD19YrqzeHbb6xU3MkSIXKhAO1MaYq48uGVYb3vJScEZVOutgMInrZzUcCWNulNkfcbmExSiymCZ5xQBw5QDuzpuDFqRZ1Xt%2BBZxEHBN9OYQKpoe0%2BovjnXyVOaH8VUKhE%2FghUWnThrXJr%2BhmSc5t7ggjiVPQc7pGn3qSNGCQwdpkQC9GHMr%2Fr%2B8n6qeEKMYB5j%2F1wC4d8Jae8FQiU8xcXR0NlUgV2LAw61%2FZJv5BTJpa%2Bz5Lv1W9v6jHQWRX2O8uaG3KU%2FlR3spR7%2BoGlWOw%3D  
    

对于第二组示例参数（包含一些 Unicode 字符）：
    
    
    qJtv66wyp%2F1mZE%2BmIFAAMUoTe8xkmLN7%2FeAZjuC9x1ocxovItHLl%2FsNK7Wq8QjgiHqGn0bb8P7yVvGBEd1gFe71NQ8aM0M%2BJNIMz5UFxfeA53rXjFlvsyH1Sig%2BOuO9Nz5nhCaJ6bEfj2iuv7w27pB3L8MVqmoCi6D9C%2FQMiLxtPaR70CxtnvoOlIgPmpv2bQy029A31NEK19ieVLkoyp1EUkXRaX3v0mohx8yMnUG1dhX9nUg3Oy8TYZ03DQy7kHDGkMKisNX7rt%2FGuGx1HIgjFclDGLsbAFIodvSLjm9FbseasMELoxlAJDlwRnW8zo5sQmL0Fz7ao935QBynrng%3D%3D  
    

**第三步: 为请求添加签名**

通过在查询字符串中添加 `signature` 参数来完成请求。

对于第一组示例参数（仅限 ASCII 字符）：
    
    
    curl -H "X-MBX-APIKEY: 4yNzx3yWC5bS6YTwEkSRaC0nRmSQIIStAUOh1b6kqaBrTLIhjCpI5lJH8q8R8WNO" -X POST 'hhttps://api.binance.com/api/v3/order?symbol=BTCUSDT&side=SELL&type=LIMIT&timeInForce=GTC&quantity=1&price=0.2&timestamp=1668481559918&recvWindow=5000&signature=HaZnek7KOGa%2Fk5%2Bf6Q1nw8lzMUpo36mRVvvLHCMUCXxlmdQQGZge1luAUKnleD%2FDYeD19YrqzeHbb6xU3MkSIXKhAO1MaYq48uGVYb3vJScEZVOutgMInrZzUcCWNulNkfcbmExSiymCZ5xQBw5QDuzpuDFqRZ1Xt%2BBZxEHBN9OYQKpoe0%2BovjnXyVOaH8VUKhE%2FghUWnThrXJr%2BhmSc5t7ggjiVPQc7pGn3qSNGCQwdpkQC9GHMr%2Fr%2B8n6qeEKMYB5j%2F1wC4d8Jae8FQiU8xcXR0NlUgV2LAw61%2FZJv5BTJpa%2Bz5Lv1W9v6jHQWRX2O8uaG3KU%2FlR3spR7%2BoGlWOw%3D'  
    

对于第二组示例参数（包含一些 Unicode 字符）：
    
    
    curl -H "X-MBX-APIKEY: 4yNzx3yWC5bS6YTwEkSRaC0nRmSQIIStAUOh1b6kqaBrTLIhjCpI5lJH8q8R8WNO" -X POST 'https://api.binance.com/api/v3/order?symbol=%EF%BC%91%EF%BC%92%EF%BC%93%EF%BC%94%EF%BC%95%EF%BC%96&&side=SELL&type=LIMIT&timeInForce=GTC&quantity=1&price=0.2&timestamp=1668481559918&recvWindow=5000&signature=qJtv66wyp%2F1mZE%2BmIFAAMUoTe8xkmLN7%2FeAZjuC9x1ocxovItHLl%2FsNK7Wq8QjgiHqGn0bb8P7yVvGBEd1gFe71NQ8aM0M%2BJNIMz5UFxfeA53rXjFlvsyH1Sig%2BOuO9Nz5nhCaJ6bEfj2iuv7w27pB3L8MVqmoCi6D9C%2FQMiLxtPaR70CxtnvoOlIgPmpv2bQy029A31NEK19ieVLkoyp1EUkXRaX3v0mohx8yMnUG1dhX9nUg3Oy8TYZ03DQy7kHDGkMKisNX7rt%2FGuGx1HIgjFclDGLsbAFIodvSLjm9FbseasMELoxlAJDlwRnW8zo5sQmL0Fz7ao935QBynrng%3D%3D'  
    

以下是一个执行上述所有步骤的 Bash 脚本示例：
    
    
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