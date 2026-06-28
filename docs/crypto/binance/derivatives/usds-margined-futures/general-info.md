---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/usds-margined-futures/general-info
api_type: REST
updated_at: 2026-05-27 18:55:56.918323
---

# General Info

## General API Information[​](/docs/derivatives/usds-margined-futures/general-info#general-api-information "Direct link to General API Information")

  * Some endpoints will require an API Key. Please refer to [this page](https://www.binance.com/en/support/articles/360002502072)
  * The base endpoint is: **<https://fapi.binance.com>**
  * All endpoints return either a JSON object or array.
  * Data is returned in **ascending** order. Oldest first, newest last.
  * All time and timestamp related fields are in milliseconds.
  * All data types adopt definition in JAVA.



### Testnet API Information[​](/docs/derivatives/usds-margined-futures/general-info#testnet-api-information "Direct link to Testnet API Information")

  * Most of the endpoints can be used in the testnet platform.
  * The REST base url for **testnet** is "<https://demo-fapi.binance.com>"
  * The Websocket base url for **testnet** is "wss://fstream.binancefuture.com"



* * *

## General Information on Endpoints[​](/docs/derivatives/usds-margined-futures/general-info#general-information-on-endpoints "Direct link to General Information on Endpoints")

  * For `GET` endpoints, parameters must be sent as a `query string`.
  * For `POST`, `PUT`, and `DELETE` endpoints, the parameters may be sent as a `query string` or in the `request body` with content type `application/x-www-form-urlencoded`. You may mix parameters between both the `query string` and `request body` if you wish to do so.
  * Parameters may be sent in any order.
  * If a parameter sent in both the `query string` and `request body`, the `query string` parameter will be used.



### HTTP Return Codes[​](/docs/derivatives/usds-margined-futures/general-info#http-return-codes "Direct link to HTTP Return Codes")

  * HTTP `4XX` return codes are used for for malformed requests; the issue is on the sender's side.
  * HTTP `403` return code is used when the WAF Limit (Web Application Firewall) has been violated.
  * HTTP `408` return code is used when a timeout has occurred while waiting for a response from the backend server.
  * HTTP `429` return code is used when breaking a request rate limit.
  * HTTP `418` return code is used when an IP has been auto-banned for continuing to send requests after receiving `429` codes.
  * HTTP `5XX` return codes are used for internal errors; the issue is on Binance's side. 
    1. If there is an error message **"Request occur unknown error."** , please retry later.
  * HTTP `503` return code is used when: 
    1. If there is an error message **"Unknown error, please check your request or try again later."** returned in the response, the API successfully sent the request but not get a response within the timeout period.  
It is important to **NOT** treat this as a failure operation; the execution status is **UNKNOWN** and could have been a success;
    2. If there is an error message **"Service Unavailable."** returned in the response, it means this is a failure API operation and the service might be unavailable at the moment, you need to retry later.
    3. If there is an error message **"Internal error; unable to process your request. Please try again."** returned in the response, it means this is a failure API operation and you can resend your request if you need.
    4. If the response contains the error message **"Request throttled by system-level protection. Reduce-only/close-position orders are exempt. Please try again." (-1008)** , This indicates the node has exceeded its maximum concurrency and is temporarily throttled. Close-position, reduce-only, and cancel orders are exempt and will not receive this error.



### HTTP 503 Status: Message Variants & Handling[​](/docs/derivatives/usds-margined-futures/general-info#http-503-status-message-variants--handling "Direct link to HTTP 503 Status: Message Variants & Handling")

#### A. “Unknown error, please check your request or try again later.” (Execution status **unknown**)[​](/docs/derivatives/usds-margined-futures/general-info#a-unknown-error-please-check-your-request-or-try-again-later-execution-status-unknown "Direct link to a-unknown-error-please-check-your-request-or-try-again-later-execution-status-unknown")

  * **Meaning** : Request accepted but no response before timeout; **execution may have succeeded**.
  * **Handling** : 
    * **Do not treat as immediate failure** ; first verify via **WebSocket updates** or **orderId queries** to avoid duplicates.
    * During peaks, prefer **single orders** over batch to reduce uncertainty.
  * **Rate-limit counting** : **May or may not** count, check header to verify rate limit info



#### B. “Service Unavailable.” (Failure)[​](/docs/derivatives/usds-margined-futures/general-info#b-service-unavailable-failure "Direct link to B. “Service Unavailable.” \(Failure\)")

  * **Meaning** : Service temporarily unavailable; **100% failure**.
  * **Handling** : **Retry with exponential backoff** (e.g., 200ms → 400ms → 800ms, max 3–5 attempts).
  * **Rate-limit counting** : **not counted**



#### C. “Request throttled by system-level protection. Reduce-only/close-position orders are exempt. Please try again.” (**-1008** , Failure)[​](/docs/derivatives/usds-margined-futures/general-info#c-request-throttled-by-system-level-protection-reduce-onlyclose-position-orders-are-exempt-please-try-again--1008-failure "Direct link to c-request-throttled-by-system-level-protection-reduce-onlyclose-position-orders-are-exempt-please-try-again--1008-failure")

  * **Meaning** : System overload; **100% failure**.
  * **Handling** : **Retry with backoff** and **reduce concurrency** ;
  * **Applicable endpoints** : 
    * `POST /fapi/v1/order`
    * `POST /fapi/v1/batchOrders`
    * `POST /fapi/v1/order/test`
  * **Rate-limit counting** : **Not counted** (overload protection).
  * **Exception integrated here** : When a request **reduces exposure** (Reduce-only / Close-position: `closePosition = true`, or `positionSide = BOTH` with `reduceOnly = true`, or `LONG+SELL`, or `SHORT+BUY`), it is **not affected or prioritized under -1008** to ensure risk reduction. 
    * Covered endpoints: `POST /fapi/v1/order`、`POST /fapi/v1/batchOrders` (when parameters satisfy the condition)



### Error Codes and Messages[​](/docs/derivatives/usds-margined-futures/general-info#error-codes-and-messages "Direct link to Error Codes and Messages")

  * Any endpoint can return an ERROR



> **_The error payload is as follows:_**
    
    
    {  
      "code": -1121,  
      "msg": "Invalid symbol."  
    }  
    

  * Specific error codes and messages defined in [Error Codes](/docs/derivatives/usds-margined-futures/general-info#error-codes).



* * *

## SDK and Code Demonstration[​](/docs/derivatives/usds-margined-futures/general-info#sdk-and-code-demonstration "Direct link to SDK and Code Demonstration")

**Disclaimer:**

  * The following SDKs are provided by partners and users, and are **not officially** produced. They are only used to help users become familiar with the API endpoint. Please use it with caution and expand R&D according to your own situation.
  * Binance does not make any commitment to the safety and performance of the SDKs, nor will be liable for the risks or even losses caused by using the SDKs.



### Python3[​](/docs/derivatives/usds-margined-futures/general-info#python3 "Direct link to Python3")

**SDK:** To get the provided SDK for Binance Futures Connector, please visit <https://github.com/binance/binance-connector-python>, or use the command below: `pip install binance-sdk-derivatives-trading-usds-futures`

### Java[​](/docs/derivatives/usds-margined-futures/general-info#java "Direct link to Java")

To get the provided SDK for Binance Futures, please visit <https://github.com/binance/binance-connector-java>, or use the command below: `git clone https://github.com/binance/binance-connector-java.git`

* * *

## LIMITS[​](/docs/derivatives/usds-margined-futures/general-info#limits "Direct link to LIMITS")

  * The `/fapi/v1/exchangeInfo` `rateLimits` array contains objects related to the exchange's `RAW_REQUEST`, `REQUEST_WEIGHT`, and `ORDER` rate limits. These are further defined in the `ENUM definitions` section under `Rate limiters (rateLimitType)`.
  * A `429` will be returned when either rate limit is violated.

Binance has the right to further tighten the rate limits on users with intent to attack. 

### IP Limits[​](/docs/derivatives/usds-margined-futures/general-info#ip-limits "Direct link to IP Limits")

  * Every request will contain `X-MBX-USED-WEIGHT-(intervalNum)(intervalLetter)` in the response headers which has the current used weight for the IP for all request rate limiters defined.
  * Each route has a `weight` which determines for the number of requests each endpoint counts for. Heavier endpoints and endpoints that do operations on multiple symbols will have a heavier `weight`.
  * When a 429 is received, it's your obligation as an API to back off and not spam the API.
  * **Repeatedly violating rate limits and/or failing to back off after receiving 429s will result in an automated IP ban (HTTP status 418).**
  * IP bans are tracked and **scale in duration** for repeat offenders, **from 2 minutes to 3 days**.
  * **The limits on the API are based on the IPs, not the API keys.**

It is strongly recommended to use websocket stream for getting data as much as possible, which can not only ensure the timeliness of the message, but also reduce the access restriction pressure caused by the request. 

### Order Rate Limits[​](/docs/derivatives/usds-margined-futures/general-info#order-rate-limits "Direct link to Order Rate Limits")

  * Every order response will contain a `X-MBX-ORDER-COUNT-(intervalNum)(intervalLetter)` header which has the current order count for the account for all order rate limiters defined.
  * Rejected/unsuccessful orders are not guaranteed to have `X-MBX-ORDER-COUNT-**` headers in the response.
  * **The order rate limit is counted against each account**.



* * *

## Endpoint Security Type[​](/docs/derivatives/usds-margined-futures/general-info#endpoint-security-type "Direct link to Endpoint Security Type")

  * Each endpoint has a security type that determines the how you will interact with it.
  * API-keys are passed into the Rest API via the `X-MBX-APIKEY` header.
  * API-keys and secret-keys **are case sensitive**.
  * API-keys can be configured to only access certain types of secure endpoints. For example, one API-key could be used for TRADE only, while another API-key can access everything except for TRADE routes.
  * By default, API-keys can access all secure routes.

Security Type| Description  
---|---  
NONE| Endpoint can be accessed freely.  
TRADE| Endpoint requires sending a valid API-Key and signature.  
USER_DATA| Endpoint requires sending a valid API-Key and signature.  
USER_STREAM| Endpoint requires sending a valid API-Key.  
MARKET_DATA| Endpoint requires sending a valid API-Key.  
  
  * `TRADE` and `USER_DATA` endpoints are `SIGNED` endpoints.



### SIGNED (TRADE and USER_DATA) Endpoint Security[​](/docs/derivatives/usds-margined-futures/general-info#signed-trade-and-user_data-endpoint-security "Direct link to SIGNED \(TRADE and USER_DATA\) Endpoint Security")

  * `SIGNED` endpoints require an additional parameter, `signature`, to be sent in the `query string` or `request body`.
  * Endpoints use `HMAC SHA256` signatures. The `HMAC SHA256 signature` is a keyed `HMAC SHA256` operation. Use your `secretKey` as the key and `totalParams` as the value for the HMAC operation.
  * The `signature` is **not case sensitive**.
  * Please make sure the `signature` is the end part of your `query string` or `request body`.
  * `totalParams` is defined as the `query string` concatenated with the `request body`.



### Timing Security[​](/docs/derivatives/usds-margined-futures/general-info#timing-security "Direct link to Timing Security")

  * A `SIGNED` endpoint also requires a parameter, `timestamp`, to be sent which should be the millisecond timestamp of when the request was created and sent.
  * An additional parameter, `recvWindow`, may be sent to specify the number of milliseconds after `timestamp` the request is valid for. If `recvWindow` is not sent, **it defaults to 5000**.



> The logic is as follows:
    
    
    if (timestamp < serverTime + 1000 && serverTime - timestamp <= recvWindow) {  
      // process request  
    } else {  
      // reject request  
    }  
    

**Serious trading is about timing.** Networks can be unstable and unreliable, which can lead to requests taking varying amounts of time to reach the servers. With `recvWindow`, you can specify that the request must be processed within a certain number of milliseconds or be rejected by the server.

It is recommended to use a small recvWindow of 5000 or less! 

### SIGNED Endpoint Examples for POST /fapi/v1/order - HMAC Keys[​](/docs/derivatives/usds-margined-futures/general-info#signed-endpoint-examples-for-post-fapiv1order---hmac-keys "Direct link to SIGNED Endpoint Examples for POST /fapi/v1/order - HMAC Keys")

Here is a step-by-step example of how to send a vaild signed payload from the Linux command line using `echo`, `openssl`, and `curl`.

Key| Value  
---|---  
apiKey| dbefbc809e3e83c283a984c3a1459732ea7db1360ca80c5c2c8867408d28cc83  
secretKey| 2b5eb11e18796d12d88f13dc27dbbd02c2cc51ff7059765ed9821957d82bb4d9  
Parameter| Value  
---|---  
symbol| BTCUSDT  
side| BUY  
type| LIMIT  
timeInForce| GTC  
quantity| 1  
price| 9000  
recvWindow| 5000  
timestamp| 1591702613943  
  
#### Example 1: As a query string[​](/docs/derivatives/usds-margined-futures/general-info#example-1-as-a-query-string "Direct link to Example 1: As a query string")

> **Example 1**

> **HMAC SHA256 signature:**
    
    
        $ echo -n "symbol=BTCUSDT&side=BUY&type=LIMIT&quantity=1&price=9000&timeInForce=GTC&recvWindow=5000&timestamp=1591702613943" | openssl dgst -sha256 -hmac "2b5eb11e18796d12d88f13dc27dbbd02c2cc51ff7059765ed9821957d82bb4d9"  
        (stdin)= 3c661234138461fcc7a7d8746c6558c9842d4e10870d2ecbedf7777cad694af9  
    

> **curl command:**
    
    
        (HMAC SHA256)  
        $ curl -H "X-MBX-APIKEY: dbefbc809e3e83c283a984c3a1459732ea7db1360ca80c5c2c8867408d28cc83" -X POST 'https://fapi/binance.com/fapi/v1/order?symbol=BTCUSDT&side=BUY&type=LIMIT&quantity=1&price=9000&timeInForce=GTC&recvWindow=5000&timestamp=1591702613943&signature= 3c661234138461fcc7a7d8746c6558c9842d4e10870d2ecbedf7777cad694af9'  
    

  * **queryString:**

symbol=BTCUSDT  
&side=BUY  
&type=LIMIT  
&timeInForce=GTC  
&quantity=1  
&price=9000  
&recvWindow=5000  
&timestamp=1591702613943




#### Example 2: As a request body[​](/docs/derivatives/usds-margined-futures/general-info#example-2-as-a-request-body "Direct link to Example 2: As a request body")

> **Example 2**

> **HMAC SHA256 signature:**
    
    
        $ echo -n "symbol=BTCUSDT&side=BUY&type=LIMIT&quantity=1&price=9000&timeInForce=GTC&recvWindow=5000&timestamp=1591702613943" | openssl dgst -sha256 -hmac "2b5eb11e18796d12d88f13dc27dbbd02c2cc51ff7059765ed9821957d82bb4d9"  
        (stdin)= 3c661234138461fcc7a7d8746c6558c9842d4e10870d2ecbedf7777cad694af9  
    

> **curl command:**
    
    
        (HMAC SHA256)  
        $ curl -H "X-MBX-APIKEY: dbefbc809e3e83c283a984c3a1459732ea7db1360ca80c5c2c8867408d28cc83" -X POST 'https://fapi/binance.com/fapi/v1/order' -d 'symbol=BTCUSDT&side=BUY&type=LIMIT&quantity=1&price=9000&timeInForce=GTC&recvWindow=5000&timestamp=1591702613943&signature= 3c661234138461fcc7a7d8746c6558c9842d4e10870d2ecbedf7777cad694af9'  
    

  * **requestBody:**

symbol=BTCUSDT  
&side=BUY  
&type=LIMIT  
&timeInForce=GTC  
&quantity=1  
&price=9000  
&recvWindow=5000  
&timestamp=1591702613943




#### Example 3: Mixed query string and request body[​](/docs/derivatives/usds-margined-futures/general-info#example-3-mixed-query-string-and-request-body "Direct link to Example 3: Mixed query string and request body")

> **Example 3**

> **HMAC SHA256 signature:**
    
    
        $ echo -n "symbol=BTCUSDT&side=BUY&type=LIMIT&timeInForce=GTCquantity=1&price=9000&recvWindow=5000&timestamp= 1591702613943" | openssl dgst -sha256 -hmac "2b5eb11e18796d12d88f13dc27dbbd02c2cc51ff7059765ed9821957d82bb4d9"  
        (stdin)= f9d0ae5e813ef6ccf15c2b5a434047a0181cb5a342b903b367ca6d27a66e36f2  
    

> **curl command:**
    
    
        (HMAC SHA256)  
        $ curl -H "X-MBX-APIKEY: dbefbc809e3e83c283a984c3a1459732ea7db1360ca80c5c2c8867408d28cc83" -X POST 'https://fapi.binance.com/fapi/v1/order?symbol=BTCUSDT&side=BUY&type=LIMIT&timeInForce=GTC' -d 'quantity=1&price=9000&recvWindow=5000&timestamp=1591702613943&signature=f9d0ae5e813ef6ccf15c2b5a434047a0181cb5a342b903b367ca6d27a66e36f2'  
    

  * **queryString:** symbol=BTCUSDT&side=BUY&type=LIMIT&timeInForce=GTC
  * **requestBody:** quantity=1&price=9000&recvWindow=5000&timestamp= 1591702613943



Note that the signature is different in example 3.  
There is no & between "GTC" and "quantity=1".

### SIGNED Endpoint Examples for POST /fapi/v1/order - RSA Keys[​](/docs/derivatives/usds-margined-futures/general-info#signed-endpoint-examples-for-post-fapiv1order---rsa-keys "Direct link to SIGNED Endpoint Examples for POST /fapi/v1/order - RSA Keys")

  * This will be a step by step process how to create the signature payload to send a valid signed payload.
  * We support `PKCS#8` currently.
  * To get your API key, you need to upload your RSA Public Key to your account and a corresponding API key will be provided for you.



For this example, the private key will be referenced as `test-prv-key.pem`

Key| Value  
---|---  
apiKey| vE3BDAL1gP1UaexugRLtteaAHg3UO8Nza20uexEuW1Kh3tVwQfFHdAiyjjY428o2  
Parameter| Value  
---|---  
symbol| BTCUSDT  
side| SELL  
type| MARKET  
quantity| 1.23  
recvWindow| 9999999  
timestamp| 1671090801999  
  
> **Signature payload (with the listed parameters):**
    
    
    timestamp=1671090801999&recvWindow=9999999&symbol=BTCUSDT&side=SELL&type=MARKET&quantity=1.23  
    

**Step 1: Construct the payload**

Arrange the list of parameters into a string. Separate each parameter with a `&`.

**Step 2: Compute the signature:**

2.1 - Encode signature payload as ASCII data.

> **Step 2.2**
    
    
     $ echo -n 'timestamp=1671090801999&recvWindow=9999999&symbol=BTCUSDT&side=SELL&type=MARKET&quantity=1.23' | openssl dgst -keyform PEM -sha256 -sign ./test-prv-key.pem  
    

2.2 - Sign payload using RSASSA-PKCS1-v1_5 algorithm with SHA-256 hash function.

> **Step 2.3**
    
    
    $ echo -n 'timestamp=1671090801999&recvWindow=9999999&symbol=BTCUSDT&side=SELL&type=MARKET&quantity=1.23' | openssl dgst -keyform PEM -sha256 -sign ./test-prv-key.pem | openssl enc -base64  
    aap36wD5loVXizxvvPI3wz9Cjqwmb3KVbxoym0XeWG1jZq8umqrnSk8H8dkLQeySjgVY91Ufs%2BBGCW%2B4sZjQEpgAfjM76riNxjlD3coGGEsPsT2lG39R%2F1q72zpDs8pYcQ4A692NgHO1zXcgScTGgdkjp%2Brp2bcddKjyz5XBrBM%3D  
    

2.3 - Encode output as base64 string.

> **Step 2.4**
    
    
    $  echo -n 'timestamp=1671090801999&recvWindow=9999999&symbol=BTCUSDT&side=SELL&type=MARKET&quantity=1.23' | openssl dgst -keyform PEM -sha256 -sign ./test-prv-key.pem | openssl enc -base64 | tr -d '\n'  
    aap36wD5loVXizxvvPI3wz9Cjqwmb3KVbxoym0XeWG1jZq8umqrnSk8H8dkLQeySjgVY91Ufs%2BBGCW%2B4sZjQEpgAfjM76riNxjlD3coGGEsPsT2lG39R%2F1q72zpDs8pYcQ4A692NgHO1zXcgScTGgdkjp%2Brp2bcddKjyz5XBrBM%3D  
    

2.4 - Delete any newlines in the signature.

> **Step 2.5**
    
    
    aap36wD5loVXizxvvPI3wz9Cjqwmb3KVbxoym0XeWG1jZq8umqrnSk8H8dkLQeySjgVY91Ufs%2BBGCW%2B4sZjQEpgAfjM76riNxjlD3coGGEsPsT2lG39R%2F1q72zpDs8pYcQ4A692NgHO1zXcgScTGgdkjp%2Brp2bcddKjyz5XBrBM%3D  
    

2.5 - Since the signature may contain `/` and `=`, this could cause issues with sending the request. So the signature has to be URL encoded.

> **Step 2.6**
    
    
     curl -H "X-MBX-APIKEY: vE3BDAL1gP1UaexugRLtteaAHg3UO8Nza20uexEuW1Kh3tVwQfFHdAiyjjY428o2" -X POST 'https://fapi.binance.com/fapi/v1/order?timestamp=1671090801999&recvWindow=9999999&symbol=BTCUSDT&side=SELL&type=MARKET&quantity=1.23&signature=aap36wD5loVXizxvvPI3wz9Cjqwmb3KVbxoym0XeWG1jZq8umqrnSk8H8dkLQeySjgVY91Ufs%2BBGCW%2B4sZjQEpgAfjM76riNxjlD3coGGEsPsT2lG39R%2F1q72zpDs8pYcQ4A692NgHO1zXcgScTGgdkjp%2Brp2bcddKjyz5XBrBM%3D'  
    

2.6 - curl command

> **Bash script**
    
    
    #!/usr/bin/env bash  
      
    # Set up authentication:  
    apiKey="vE3BDAL1gP1UaexugRLtteaAHg3UO8Nza20uexEuW1Kh3tVwQfFHdAiyjjY428o2"   ### REPLACE THIS WITH YOUR API KEY  
      
    # Set up the request:  
    apiMethod="POST"  
    apiCall="v1/order"  
    apiParams="timestamp=1671090801999&recvWindow=9999999&symbol=BTCUSDT&side=SELL&type=MARKET&quantity=1.23"  
    function rawurlencode {  
        local value="$1"  
        local len=${#value}  
        local encoded=""  
        local pos c o  
        for (( pos=0 ; pos<len ; pos++ ))  
        do  
            c=${value:$pos:1}  
            case "$c" in  
                [-_.~a-zA-Z0-9] ) o="${c}" ;;  
                * )   printf -v o '%%%02x' "'$c"  
            esac  
            encoded+="$o"  
        done  
        echo "$encoded"  
    }  
    ts=$(date +%s000)  
    paramsWithTs="$apiParams&timestamp=$ts"  
    rawSignature=$(echo -n "$paramsWithTs" \  
                   | openssl dgst -keyform PEM -sha256 -sign ./test-prv-key.pem \  ### THIS IS YOUR PRIVATE KEY. DO NOT SHARE THIS FILE WITH ANYONE.  
                   | openssl enc -base64 \  
                   | tr -d '\n')  
    signature=$(rawurlencode "$rawSignature")  
    curl -H "X-MBX-APIKEY: $apiKey" -X $apiMethod \  
        "https://fapi.binance.com/fapi/$apiCall?$paramsWithTs&signature=$signature"  
    

A sample Bash script containing similar steps is available in the right side.

* * *

## Postman Collections[​](/docs/derivatives/usds-margined-futures/general-info#postman-collections "Direct link to Postman Collections")

There is now a Postman collection containing the API endpoints for quick and easy use.

For more information please refer to this page: [Binance API Postman](https://github.com/binance-exchange/binance-api-postman)

---

# 基本信息

## Rest 基本信息[​](/docs/zh-CN/derivatives/usds-margined-futures/general-info#rest-基本信息 "Rest 基本信息的直接链接")

  * 接口可能需要用户的 API Key，如何创建API-KEY请参考[这里](https://www.binance.com/cn/support/articles/360002502072)
  * 本篇列出REST接口的baseurl **<https://fapi.binance.com>**
  * 所有接口的响应都是JSON格式
  * 响应中如有数组，数组元素以时间升序排列，越早的数据越提前。
  * 所有时间、时间戳均为UNIX时间，单位为毫秒
  * 所有数据类型采用JAVA的数据类型定义



### Testnet API 信息[​](/docs/zh-CN/derivatives/usds-margined-futures/general-info#testnet-api-信息 "Testnet API 信息的直接链接")

  * 本篇接口亦可接入testnet测试平台使用
  * **testnet** 的 REST baseurl 为 "<https://demo-fapi.binance.com>"
  * **testnet** 的 Websocket baseurl 为 "wss://fstream.binancefuture.com"



* * *

## 接口的基本信息[​](/docs/zh-CN/derivatives/usds-margined-futures/general-info#接口的基本信息 "接口的基本信息的直接链接")

  * `GET`方法的接口, 参数必须在`query string`中发送.
  * `POST`, `PUT`, 和 `DELETE` 方法的接口, 参数可以在 `query string`中发送，也可以在 `request body`中发送(content type `application/x-www-form-urlencoded`)。允许混合这两种方式发送参数。但如果同一个参数名在query string和request body中都有，query string中的会被优先采用。
  * 对参数的顺序不做要求。



### HTTP 返回代码[​](/docs/zh-CN/derivatives/usds-margined-futures/general-info#http-返回代码 "HTTP 返回代码的直接链接")

  * HTTP `4XX` 错误码用于指示错误的请求内容、行为、格式。
  * HTTP `403` 错误码表示违反WAF限制(Web应用程序防火墙)。
  * HTTP `408` 返回代码表示在等待后端服务器响应时发生了超时。
  * HTTP `429` 错误码表示警告访问频次超限，即将被封IP
  * HTTP `418` 表示收到429后继续访问，于是被封了。
  * HTTP `5XX` 错误码用于指示Binance服务侧的问题。 
    1. 如果返回内容里包含了报错信息 **"Request occur unknown error."** ，请稍后重试请求。
  * HTTP `503` 表示三种可能： 
    1. 如果返回内容里包含了报错信息 **"Unknown error, please check your request or try again later."** ，则表示API服务端已经向业务核心提交了请求但未能获取响应，特别需要注意的是其不代表请求失败，而是未知。很可能已经得到了执行，也有可能执行失败，需要做进一步确认。
    2. 如果返回内容里包含了报错信息 **"Service Unavailable."** ，则表示本次API请求失败。这种情况下可能是服务暂不可用，您需要稍后重试。
    3. 如果返回内容里包含了报错信息 **"Internal error; unable to process your request. Please try again."** ，则表示本次API请求失败。这种情况下您如果需要的话可以选择立即重试。
    4. 如果返回内容里包含了报错信息 **"Request throttled by system-level protection. Reduce-only/close-position orders are exempt. Please try again.(-1008)"** 。这表示节点已超出最大并发限制，正在临时限流。平仓、仅减仓与取消订单均予以豁免，不会触发该错误。



### HTTP 503 状态码：错误类型与处理[​](/docs/zh-CN/derivatives/usds-margined-futures/general-info#http-503-状态码错误类型与处理 "HTTP 503 状态码：错误类型与处理的直接链接")

#### A. “Unknown error, please check your request or try again later.”（执行状态未知）[​](/docs/zh-CN/derivatives/usds-margined-futures/general-info#a-unknown-error-please-check-your-request-or-try-again-later执行状态未知 "A. “Unknown error, please check your request or try again later.”（执行状态未知）的直接链接")

  * **语义** ：API 成功接收请求，但在超时前未返回结果；**执行状态未知（可能已成功）** 。
  * **处理** ： 
    * **不要直接当失败重试** ；先通过 **WebSocket 回报** 或 **orderId 查询** 确认是否已执行，避免重复下单。
    * 高峰期尽量使用**单笔下单** 替代批量下单以降低不确定性。
  * **是否计入限速** ：**可能计入，也可能不计入** , 请参考header中的rate计数信息



#### B. “Service Unavailable.”（失败）[​](/docs/zh-CN/derivatives/usds-margined-futures/general-info#b-service-unavailable失败 "B. “Service Unavailable.”（失败）的直接链接")

  * **语义** ：服务暂不可用；**100% 失败** 。
  * **处理** ：**退避重试** （如 200ms → 400ms → 800ms，上限 3–5 次）。
  * **是否计入限速** ：**不计入**



#### C. "Request throttled by system-level protection. Reduce-only/close-position orders are exempt. Please try again."（**-1008** ，失败）[​](/docs/zh-CN/derivatives/usds-margined-futures/general-info#c-request-throttled-by-system-level-protection-reduce-onlyclose-position-orders-are-exempt-please-try-again-1008失败 "c-request-throttled-by-system-level-protection-reduce-onlyclose-position-orders-are-exempt-please-try-again-1008失败的直接链接")

  * **语义** ：系统过载；**100% 失败** 。
  * **处理** ：**退避重试** 并**降低并发** ；
  * **适用接口** ： 
    * `POST /fapi/v1/order`
    * `POST /fapi/v1/batchOrders`
    * `POST /fapi/v1/order/test`
  * **仅适用于 C 的豁免说明** ：当请求满足**只减仓/平仓** 条件时（`closePosition = true`，或 `positionSide = BOTH` 且 `reduceOnly = true`，或 `LONG+SELL`，或 `SHORT+BUY`），**不会受 -1008 过载的影响或享有优先处理** ，以保障风险收敛。 
    * 覆盖接口：`POST /fapi/v1/order`、`POST /fapi/v1/batchOrders`（当参数满足只减仓/平仓判定）



### 接口错误代码[​](/docs/zh-CN/derivatives/usds-margined-futures/general-info#接口错误代码 "接口错误代码的直接链接")

  * 每个接口都有可能抛出异常



> 异常响应格式如下：
    
    
    {  
      "code": -1121,  
      "msg": "Invalid symbol."  
    }  
    

  * 具体的错误码及其解释在[错误代码](/docs/zh-CN/derivatives/usds-margined-futures/general-info#cf68bca02a)



* * *

## SDK和代码示例[​](/docs/zh-CN/derivatives/usds-margined-futures/general-info#sdk和代码示例 "SDK和代码示例的直接链接")

**免责声明:**

  * 以下SDK由合作方和用户提供，**非官方制作** 行为。仅做熟悉api接口和学习使用，请广大用户谨慎使用并根据自身情况自行拓展研发。
  * Binance 官方不对SDK的安全和性能做任何承诺，亦不会对使用SDK引起的风险甚至损失承担责任。



### Python3[​](/docs/zh-CN/derivatives/usds-margined-futures/general-info#python3 "Python3的直接链接")

**SDK:** 可以通过以下方式获取Binance Futures Connector SDK：

  * 访问 <https://github.com/binance/binance-connector-python>

  * 执行以下命令： `pip install binance-sdk-derivatives-trading-usds-futures`




### Java[​](/docs/zh-CN/derivatives/usds-margined-futures/general-info#java "Java的直接链接")

可以通过以下方式获取SDK：

  * 访问 <https://github.com/binance/binance-connector-java>,

  * 执行以下命令： `git clone https://github.com/binance/binance-connector-java.git`




* * *

## 访问限制[​](/docs/zh-CN/derivatives/usds-margined-futures/general-info#访问限制 "访问限制的直接链接")

  * 在 `/fapi/v1/exchangeInfo`接口中`rateLimits`数组里包含有REST接口(不限于本篇的REST接口)的访问限制。包括带权重的访问频次限制、下单速率限制。本篇`枚举定义`章节有限制类型的进一步说明。
  * 违反上述任何一个访问限制都会收到HTTP 429，这是一个警告.

请注意，若用户被认定利用频繁挂撤单且故意低效交易意图发起攻击行为，Binance有权视具体情况进一步加强对其访问限制。 

### IP 访问限制[​](/docs/zh-CN/derivatives/usds-margined-futures/general-info#ip-访问限制 "IP 访问限制的直接链接")

  * 每个请求将包含一个`X-MBX-USED-WEIGHT-(intervalNum)(intervalLetter)`的头，其中包含当前IP所有请求的已使用权重。
  * 每个路由都有一个"权重"，该权重确定每个接口计数的请求数。较重的接口和对多个交易对进行操作的接口将具有较重的"权重"。
  * 收到429时，您有责任作为API退回而不向其发送更多的请求。
  * **如果屡次违反速率限制和/或在收到429后未能退回，将导致API的IP被禁(http状态418)。**
  * 频繁违反限制，封禁时间会逐渐延长 ，**对于重复违反者，将会被封从2分钟到3天** 。
  * **访问限制是基于IP的，而不是API Key**

强烈建议您尽可能多地使用websocket消息获取相应数据,既可以保障消息的及时性，也可以减少请求带来的访问限制压力。 

### 下单频率限制[​](/docs/zh-CN/derivatives/usds-margined-futures/general-info#下单频率限制 "下单频率限制的直接链接")

  * 每个下单请求回报将包含一个`X-MBX-ORDER-COUNT-(intervalNum)(intervalLetter)`的头，其中包含当前账户已用的下单限制数量。
  * 被拒绝或不成功的下单并不保证回报中包含以上头内容。
  * **下单频率限制是基于每个账户计数的。**



## 接口鉴权类型[​](/docs/zh-CN/derivatives/usds-margined-futures/general-info#接口鉴权类型 "接口鉴权类型的直接链接")

  * 每个接口都有自己的鉴权类型，鉴权类型决定了访问时应当进行何种鉴权
  * 如果需要 API-key，应当在HTTP头中以`X-MBX-APIKEY`字段传递
  * API-key 与 API-secret 是大小写敏感的
  * 可以在网页用户中心修改API-key 所具有的权限，例如读取账户信息、发送交易指令、发送提现指令

鉴权类型| 描述  
---|---  
NONE| 不需要鉴权的接口  
TRADE| 需要有效的API-KEY和签名  
USER_DATA| 需要有效的API-KEY和签名  
USER_STREAM| 需要有效的API-KEY  
MARKET_DATA| 需要有效的API-KEY  
  
### 需要签名的接口 (TRADE 与 USER_DATA)[​](/docs/zh-CN/derivatives/usds-margined-futures/general-info#需要签名的接口-trade-与-user_data "��需要签名的接口 \(TRADE 与 USER_DATA\)的直接链接")

  * 调用这些接口时，除了接口本身所需的参数外，还需要传递`signature`即签名参数。
  * 签名使用`HMAC SHA256`算法. API-KEY所对应的API-Secret作为 `HMAC SHA256` 的密钥，其他所有参数作为`HMAC SHA256`的操作对象，得到的输出即为签名。
  * 签名大小写不敏感。
  * 请确保`signature`在`query string`或`request body`的最后
  * 当同时使用query string和request body时，`HMAC SHA256`的输入query string在前，request body在后



### 时间同步安全[​](/docs/zh-CN/derivatives/usds-margined-futures/general-info#时间同步安全 "时间同步安全的直接链接")

  * 签名接口均需要传递`timestamp`参数, 其值应当是请求发送时刻的unix时间戳(毫秒)
  * 服务器收到请求时会判断请求中的时间戳，如果是5000毫秒之前发出的，则请求会被认为无效。这个时间窗口值可以通过发送可选参数`recvWindow`来自定义。
  * 另外，如果服务器计算得出客户端时间戳在服务器时间的‘未来’一秒以上，也会拒绝请求。



> 逻辑伪代码：
    
    
    if (timestamp < (serverTime + 1000) && (serverTime - timestamp) <= recvWindow) {  
      // process request  
    } else {  
      // reject request  
    }  
    

**关于交易时效性** 互联网状况并不100%可靠，不可完全依赖,因此你的程序本地到币安服务器的时延会有抖动. 这是我们设置`recvWindow`的目的所在，如果你从事高频交易，对交易时效性有较高的要求，可以灵活设置recvWindow以达到你的要求。

不推荐使用5秒以上的recvWindow 

### POST /fapi/v1/order 的示例 - HMAC Keys[​](/docs/zh-CN/derivatives/usds-margined-futures/general-info#post-fapiv1order-的示例---hmac-keys "POST /fapi/v1/order 的示例 - HMAC Keys的直接链接")

以下是在linux bash环境下使用 echo openssl 和curl工具实现的一个调用接口下单的示例 apikey、secret仅供示范

Key| Value  
---|---  
apiKey| dbefbc809e3e83c283a984c3a1459732ea7db1360ca80c5c2c8867408d28cc83  
secretKey| 2b5eb11e18796d12d88f13dc27dbbd02c2cc51ff7059765ed9821957d82bb4d9  
参数| 取值  
---|---  
symbol| BTCUSDT  
side| BUY  
type| LIMIT  
timeInForce| GTC  
quantity| 1  
price| 9000  
recvWindow| 5000  
timestamp| 1591702613943  
  
#### 示例 1: 所有参数通过 query string 发送[​](/docs/zh-CN/derivatives/usds-margined-futures/general-info#示例-1-所有参数通过-query-string-发送 "示例 1: 所有参数通过 query string 发送的直接链接")

> **示例1:**

> **HMAC SHA256 签名:**
    
    
        $ echo -n "symbol=BTCUSDT&side=BUY&type=LIMIT&quantity=1&price=9000&timeInForce=GTC&recvWindow=5000&timestamp=1591702613943" | openssl dgst -sha256 -hmac "2b5eb11e18796d12d88f13dc27dbbd02c2cc51ff7059765ed9821957d82bb4d9"  
        (stdin)= 3c661234138461fcc7a7d8746c6558c9842d4e10870d2ecbedf7777cad694af9  
    

> **curl 调用:**
    
    
        (HMAC SHA256)  
        $ curl -H "X-MBX-APIKEY: dbefbc809e3e83c283a984c3a1459732ea7db1360ca80c5c2c8867408d28cc83" -X POST 'https://fapi.binance.com/fapi/v1/order?symbol=BTCUSDT&side=BUY&type=LIMIT&quantity=1&price=9000&timeInForce=GTC&recvWindow=5000&timestamp=1591702613943&signature= 3c661234138461fcc7a7d8746c6558c9842d4e10870d2ecbedf7777cad694af9'  
    

  * **queryString:**

symbol=BTCUSDT  
&side=BUY  
&type=LIMIT  
&timeInForce=GTC  
&quantity=1  
&price=0.1  
&recvWindow=5000  
&timestamp=1499827319559




#### 示例 2: 所有参数通过 request body 发送[​](/docs/zh-CN/derivatives/usds-margined-futures/general-info#示例-2-所有参数通过-request-body-发送 "示例 2: 所有参数通过 request body 发送的直接链接")

> **示例2:**

> **HMAC SHA256 签名:**
    
    
        $ echo -n "symbol=BTCUSDT&side=BUY&type=LIMIT&quantity=1&price=9000&timeInForce=GTC&recvWindow=5000&timestamp=1591702613943" | openssl dgst -sha256 -hmac "2b5eb11e18796d12d88f13dc27dbbd02c2cc51ff7059765ed9821957d82bb4d9"  
        (stdin)= 3c661234138461fcc7a7d8746c6558c9842d4e10870d2ecbedf7777cad694af9  
    

> **curl 调用:**
    
    
        (HMAC SHA256)  
        $ curl -H "X-MBX-APIKEY: dbefbc809e3e83c283a984c3a1459732ea7db1360ca80c5c2c8867408d28cc83" -X POST 'https://fapi.binance.com/fapi/v1/order' -d 'symbol=BTCUSDT&side=BUY&type=LIMIT&quantity=1&price=9000&timeInForce=GTC&recvWindow=5000&timestamp=1591702613943&signature= 3c661234138461fcc7a7d8746c6558c9842d4e10870d2ecbedf7777cad694af9'  
    

  * **requestBody:**

symbol=BTCUSDT  
&side=BUY  
&type=LIMIT  
&timeInForce=GTC  
&quantity=1  
&price=9000  
&recvWindow=5000  
&timestamp=1591702613943




#### 示例 3: 混合使用 query string 与 request body[​](/docs/zh-CN/derivatives/usds-margined-futures/general-info#示例-3-混合使用-query-string-与-request-body "示例 3: 混合使用 query string 与 request body的直接链接")

> **示例3:**

> **HMAC SHA256 签名:**
    
    
        $ echo -n "symbol=BTCUSDT&side=BUY&type=LIMIT&timeInForce=GTCquantity=1&price=9000&recvWindow=5000&timestamp= 1591702613943" | openssl dgst -sha256 -hmac "2b5eb11e18796d12d88f13dc27dbbd02c2cc51ff7059765ed9821957d82bb4d9"  
        (stdin)= f9d0ae5e813ef6ccf15c2b5a434047a0181cb5a342b903b367ca6d27a66e36f2  
    

> **curl 调用:**
    
    
        (HMAC SHA256)  
        $ curl -H "X-MBX-APIKEY: dbefbc809e3e83c283a984c3a1459732ea7db1360ca80c5c2c8867408d28cc83" -X POST 'https://fapi.binance.com/fapi/v1/order?symbol=BTCUSDT&side=BUY&type=LIMIT&timeInForce=GTC' -d 'quantity=1&price=9000&recvWindow=5000&timestamp=1591702613943&signature=f9d0ae5e813ef6ccf15c2b5a434047a0181cb5a342b903b367ca6d27a66e36f2'  
    

  * **queryString:** symbol=BTCUSDT&side=BUY&type=LIMIT&timeInForce=GTC
  * **requestBody:** quantity=1&price=9000&recvWindow=5000&timestamp= 1591702613943



请注意，示例3中的签名有些许不同，在"GTC"和"quantity=1"之间**没有** "&"字符。

### POST /fapi/v1/order 的示例 - RSA Keys[​](/docs/zh-CN/derivatives/usds-margined-futures/general-info#post-fapiv1order-的示例---rsa-keys "POST /fapi/v1/order 的示例 - RSA Keys的直接链接")

  * 这将逐步介绍如何通过有效的签名发送 payload。
  * 我们接受 `PKCS#8` 格式的 RSA Key。
  * 要获取 API Key，您需要在您的账户上上传您的 RSA Public Key。



对于这个例子，Private Key 将被引用为`test-prv-key.pem`。

Key| Value  
---|---  
apiKey| vE3BDAL1gP1UaexugRLtteaAHg3UO8Nza20uexEuW1Kh3tVwQfFHdAiyjjY428o2  
参数| 取值  
---|---  
symbol| BTCUSDT  
side| SELL  
type| MARKET  
quantity| 1.23  
recvWindow| 9999999  
timestamp| 1671090801999  
  
> **有列出参数的签名 payload：**
    
    
    timestamp=1671090801999&recvWindow=9999999&symbol=BTCUSDT&side=SELL&type=MARKET&quantity=1.23  
    

**第1步: Payload**

将参数列表排列成一个 string。 用 `&` 分隔每个参数。对于上述参数，签名 payload 如右所示。

**第2步: 计算签名**

2.1 - 将签名有效负载编码为 ASCII 数据。

> **第2.2步**
    
    
     $ echo -n 'timestamp=1671090801999&recvWindow=9999999&symbol=BTCUSDT&side=SELL&type=MARKET&quantity=1.23' | openssl dgst -keyform PEM -sha256 -sign ./test-prv-key.pem  
    

2.2 - 使用带有 SHA-256 hash 函数的 RSASSA-PKCS1-v1_5 算法对 payload 进行签名。

> **第2.3步**
    
    
    $ echo -n 'timestamp=1671090801999&recvWindow=9999999&symbol=BTCUSDT&side=SELL&type=MARKET&quantity=1.23' | openssl dgst -keyform PEM -sha256 -sign ./test-prv-key.pem | openssl enc -base64  
    aap36wD5loVXizxvvPI3wz9Cjqwmb3KVbxoym0XeWG1jZq8umqrnSk8H8dkLQeySjgVY91Ufs%2BBGCW%2B4sZjQEpgAfjM76riNxjlD3coGGEsPsT2lG39R%2F1q72zpDs8pYcQ4A692NgHO1zXcgScTGgdkjp%2Brp2bcddKjyz5XBrBM%3D  
    

2.3 - 将输出编码为 base64 string。

> **第2.4步**
    
    
    $  echo -n 'timestamp=1671090801999&recvWindow=9999999&symbol=BTCUSDT&side=SELL&type=MARKET&quantity=1.23' | openssl dgst -keyform PEM -sha256 -sign ./test-prv-key.pem | openssl enc -base64 | tr -d '\n'  
    aap36wD5loVXizxvvPI3wz9Cjqwmb3KVbxoym0XeWG1jZq8umqrnSk8H8dkLQeySjgVY91Ufs%2BBGCW%2B4sZjQEpgAfjM76riNxjlD3coGGEsPsT2lG39R%2F1q72zpDs8pYcQ4A692NgHO1zXcgScTGgdkjp%2Brp2bcddKjyz5XBrBM%3D  
    

2.4 - 删除签名中的所有 `\n`。

> **第2.5步**
    
    
    aap36wD5loVXizxvvPI3wz9Cjqwmb3KVbxoym0XeWG1jZq8umqrnSk8H8dkLQeySjgVY91Ufs%2BBGCW%2B4sZjQEpgAfjM76riNxjlD3coGGEsPsT2lG39R%2F1q72zpDs8pYcQ4A692NgHO1zXcgScTGgdkjp%2Brp2bcddKjyz5XBrBM%3D  
    

2.5 - 由于签名可能包含 `/` 和 `=`，这可能会导致发送请求时出现问题。 所以签名必须是 URL 编码的。

> **第2.6步**
    
    
     curl -H "X-MBX-APIKEY: vE3BDAL1gP1UaexugRLtteaAHg3UO8Nza20uexEuW1Kh3tVwQfFHdAiyjjY428o2" -X POST 'https://fapi.binance.com/fapi/v1/order?timestamp=1671090801999&recvWindow=9999999&symbol=BTCUSDT&side=SELL&type=MARKET&quantity=1.23&signature=aap36wD5loVXizxvvPI3wz9Cjqwmb3KVbxoym0XeWG1jZq8umqrnSk8H8dkLQeySjgVY91Ufs%2BBGCW%2B4sZjQEpgAfjM76riNxjlD3coGGEsPsT2lG39R%2F1q72zpDs8pYcQ4A692NgHO1zXcgScTGgdkjp%2Brp2bcddKjyz5XBrBM%3D'  
    

2.6 - curl 命令

> **Bash 脚本**
    
    
    #!/usr/bin/env bash  
    # 设置身份验证：  
    apiKey="vE3BDAL1gP1UaexugRLtteaAHg3UO8Nza20uexEuW1Kh3tVwQfFHdAiyjjY428o2"   ### 替换成您的 API Key  
    # 设置您的请求:  
    apiMethod="POST"  
    apiCall="v1/order"  
    apiParams="timestamp=1671090801999&recvWindow=9999999&symbol=BTCUSDT&side=SELL&type=MARKET&quantity=1.23"  
    function rawurlencode {  
        local value="$1"  
        local len=${#value}  
        local encoded=""  
        local pos c o  
        for (( pos=0 ; pos<len ; pos++ ))  
        do  
            c=${value:$pos:1}  
            case "$c" in  
                [-_.~a-zA-Z0-9] ) o="${c}" ;;  
                * )   printf -v o '%%%02x' "'$c"  
            esac  
            encoded+="$o"  
        done  
        echo "$encoded"  
    }  
    ts=$(date +%s000)  
    paramsWithTs="$apiParams&timestamp=$ts"  
    rawSignature=$(echo -n "$paramsWithTs" \  
                   | openssl dgst -keyform PEM -sha256 -sign ./test-prv-key.pem \  ### 替换成您的 Private Key。不要与任何人共享此文件。  
                   | openssl enc -base64 \  
                   | tr -d '\n')  
    signature=$(rawurlencode "$rawSignature")  
    curl -H "X-MBX-APIKEY: $apiKey" -X $apiMethod \  
        "https://fapi.binance.com/fapi/$apiCall?$paramsWithTs&signature=$signature"  
    

右边有示例 Bash 脚本执行上述类似的步骤.

## Postman 收藏[​](/docs/zh-CN/derivatives/usds-margined-futures/general-info#postman-收藏 "Postman 收藏的直接链接")

现在有一个包含 API 端点的 Postman 集合，方便快速使用。

更多信息请参阅此页面: [Binance API Postman](https://github.com/binance-exchange/binance-api-postman)