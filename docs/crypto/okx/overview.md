---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#overview
anchor_id: overview
api_type: API
updated_at: 2026-07-06 19:52:03.766208
---

# Overview

Welcome to our API documentation. OKX provides REST and WebSocket APIs to suit your trading needs.  

**Important - OKX API Agreement: continued use constitutes acceptance**  
  
We encourage you to review the [OKX API Agreement](https://www.okx.com/help/okx-api-agreement) in full before continuing to use the API Services. Your continued use of any OKX API Services following the date of this notice constitutes your acceptance of the Agreement in full.   
If you do not agree to the Agreement, you must immediately cease all use of the OKX API Services, including disconnecting any active API integrations, Agent Trade Kit connections, and automated systems that access OKX via APIs.  **Important - Regional API Domain Requirement**  
  
Depending on where you registered, you **must** use the correct domain for both API calls and documentation.   
Using `openapi.okx.com` will not work for the regions below.  
  
**US & AU users** (registered on [app.okx.com](https://app.okx.com)): Use `us.okx.com` as your API domain. See the [US & AU API documentation](https://app.okx.com/docs-v5/en/).  
**EU users** (registered on [my.okx.com](https://my.okx.com)): Use `eea.okx.com` as your API domain. See the [EU API documentation](https://my.okx.com/docs-v5/en/).  

## API Resources and Support

### Tutorials

  * Learn how to trade with API: [Best practice to OKX’s API](/docs-v5/trick_en/#instrument-configuration)
  * Learn python spot trading step by step: [Python Spot Trading Tutorial](/help/how-can-i-do-spot-trading-with-the-jupyter-notebook)
  * Learn python derivatives trading step by step: [Python Derivatives Trading Tutorial](/help/how-can-i-do-derivatives-trading-with-the-jupyter-notebook)

  

### Python libraries

  * Use Python SDK for easier integration: [Python SDK](https://pypi.org/project/python-okx/)
  * Get access to our market maker python sample code [Python market maker sample](https://github.com/okxapi/okx-sample-market-maker)

  

### Customer service

  * Please take 1 minute to help us improve: [API Satisfaction Survey](https://forms.gle/Ehou2xFv5GE1xUGr9)
  * If you have any API-related inquiries, you can reach out to us by scanning the code below via the OKX APP.

![API Technical Support QR Code](images/APISupport-b5a4ebca.jpeg)

## API key Creation

Please refer to [my api page](/account/my-api) regarding API Key creation.

### Generating an API key

Create an API key on the website before signing any requests. After creating an API key, keep the following information safe:

  * API key
  * Secret key
  * Passphrase

The system returns randomly-generated API keys and SecretKeys. You will need to provide the Passphrase to access the API. We store the salted hash of your Passphrase for authentication. We cannot recover the Passphrase if you have lost it. You will need to create a new set of API key.  
  

### API key permissions

There are three permissions below that can be associated with an API key. One or more permission can be assigned to any key.  

  * `Read` : Can request and view account info such as bills and order history which need read permission
  * `Trade` : Can place and cancel orders, funding transfer, make settings which need write permission
  * `Withdraw` : Can make withdrawals

### API key security

To improve security, we strongly recommend clients linked the API key to IP addresses  

  * Each API key can bind up to 20 IP addresses, which support IPv4/IPv6 and network segment formats.   

API keys that are not linked to an IP address and have `trade` or `withdraw` permissions will expire after 14 days of inactivity. (The API key of demo trading will not expire)   

  * Only when the user calls an API that requires API key authentication will it be considered as the API key is used.
  * Calling an API that does not require API key authentication will not be considered used even if API key information is passed in.
  * For websocket, only operation of logging in will be considered to have used the API key. Any operation though the connection after logging in (such as subscribing/placing an order) will not be considered to have used the API key. Please pay attention.

Users can get the usage records of the API key with `trade` or `withdraw` permissions but unlinked to any IP address though [Security Center](/account/security).

## REST Authentication

### Making Requests

All private REST requests must contain the following headers:

  * `OK-ACCESS-KEY` The API key as a String.

  * `OK-ACCESS-SIGN` The Base64-encoded signature (see Signing Messages subsection for details).

  * `OK-ACCESS-TIMESTAMP` Request timestamp in ISO 8601 UTC format with millisecond precision, e.g. `2020-12-08T09:08:57.715Z`. The server rejects requests where this differs from server time by more than 30 seconds (error 50102). Always use UTC — local timezone offset is the most common cause of error 50102. Synchronise with GET /api/v5/public/time before placing orders.

  * `OK-ACCESS-PASSPHRASE` The passphrase you specified when creating the API key.

Request bodies should have content type `application/json` and be in valid JSON format.

### Signature

> Signing Messages

The `OK-ACCESS-SIGN` header is generated as follows:

  * Create a pre-hash string of timestamp + method + requestPath + body (where + represents String concatenation).
  * Prepare the SecretKey.
  * Sign the pre-hash string with the SecretKey using the HMAC SHA256.
  * Encode the signature in the Base64 format.

Example: `sign=CryptoJS.enc.Base64.stringify(CryptoJS.HmacSHA256(timestamp + 'GET' + '/api/v5/account/balance?ccy=BTC', SecretKey))`

The `timestamp` value is the same as the `OK-ACCESS-TIMESTAMP` header with millisecond ISO format, e.g. `2020-12-08T09:08:57.715Z`.

The request method should be in UPPERCASE: e.g. `GET` and `POST`.

The `requestPath` is the path of requesting an endpoint.

Example: `/api/v5/account/balance`

The `body` refers to the String of the request body. It can be omitted if there is no request body (frequently the case for `GET` requests).

Example: `{"instId":"BTC-USDT","lever":"5","mgnMode":"isolated"}`

`GET` request parameters are counted as requestpath, not body 

The SecretKey is generated when you create an API key.

Example: `22582BD0CFF14C41EDBF1AB98506286D`

## WebSocket

### Overview

WebSocket is a new HTML5 protocol that achieves full-duplex data transmission between the client and server, allowing data to be transferred effectively in both directions. A connection between the client and server can be established with just one handshake. The server will then be able to push data to the client according to preset rules. Its advantages include:

  * The WebSocket request header size for data transmission between client and server is only 2 bytes.
  * Either the client or server can initiate data transmission.
  * There's no need to repeatedly create and delete TCP connections, saving resources on bandwidth and server.

We recommend developers use WebSocket API to retrieve market data and order book depth. 

### Connect

**Connection limit** : 3 requests per second (based on IP)

When subscribing to a public channel, use the address of the public service. When subscribing to a private channel, use the address of the private service

**Request limit** : 

The total number of 'subscribe'/'unsubscribe'/'login' requests per connection is limited to 480 times per hour.

If there’s a network problem, the system will automatically disable the connection. 

The connection will break automatically if the subscription is not established or data has not been pushed for more than 30 seconds. 

To keep the connection stable: 

1\. Set a timer of N seconds whenever a response message is received, where N is less than 30. 

2\. If the timer is triggered, which means that no new message is received within N seconds, send the String 'ping'. 

3\. Expect a 'pong' as a response. If the response message is not received within N seconds, please raise an error or reconnect. 

### Connection count limit

The limit will be set at 30 WebSocket connections per specific WebSocket channel per sub-account. Each WebSocket connection is identified by the unique `connId`.

  

The WebSocket channels subject to this limitation are as follows:

  1. [Orders channel](/docs-v5/en/#order-book-trading-trade-ws-order-channel)
  2. [Account channel](/docs-v5/en/#trading-account-websocket-account-channel)
  3. [Positions channel](/docs-v5/en/#trading-account-websocket-positions-channel)
  4. [Balance and positions channel](/docs-v5/en/#trading-account-websocket-balance-and-position-channel)
  5. [Position risk warning channel](/docs-v5/en/#trading-account-websocket-position-risk-warning)
  6. [Account greeks channel](/docs-v5/en/#trading-account-websocket-account-greeks-channel)

If users subscribe to the same channel through the same WebSocket connection through multiple arguments, for example, by using `{"channel": "orders", "instType": "ANY"}` and `{"channel": "orders", "instType": "SWAP"}`, it will be counted once only. If users subscribe to the listed channels (such as orders and accounts) using either the same or different connections, it will not affect the counting, as these are considered as two different channels. The system calculates the number of WebSocket connections per channel.

  

The platform will send the number of active connections to clients through the `channel-conn-count` event message **to new channel subscriptions**.

> Connection count update
    
    
    {
        "event":"channel-conn-count",
        "channel":"orders",
        "connCount": "2",
        "connId":"abcd1234"
    }
    
    

  

When the limit is breached, generally the latest connection that sends the subscription request will be rejected. Client will receive the usual subscription acknowledgement followed by the `channel-conn-count-error` from the connection that the subscription has been terminated. In exceptional circumstances the platform may unsubscribe existing connections.

> Connection limit error
    
    
    {
        "event": "channel-conn-count-error",
        "channel": "orders",
        "connCount": "30",
        "connId":"a4d3ae55"
    }
    
    

  

Order operations through WebSocket, including place, amend and cancel orders, are not impacted through this change.

### Login

> Request Example
    
    
    {
      "op": "login",
      "args": [
        {
          "apiKey": "******",
          "passphrase": "******",
          "timestamp": "1538054050",
          "sign": "7L+zFQ+CEgGu5rzCj4+BdV2/uUHGqddA9pI6ztsRRPs="
        }
      ]
    }
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
op | String | Yes | Operation  
`login`  
args | Array of objects | Yes | List of account to login  
> apiKey | String | Yes | API Key  
> passphrase | String | Yes | API Key password  
> timestamp | String | Yes | Unix Epoch time, the unit is seconds  
> sign | String | Yes | Signature string  
  
> Successful Response Example
    
    
    {
      "event": "login",
      "code": "0",
      "msg": "",
      "connId": "a4d3ae55"
    }
    

> Failure Response Example
    
    
    {
      "event": "error",
      "code": "60009",
      "msg": "Login failed.",
      "connId": "a4d3ae55"
    }
    

#### Response parameters

Parameter | Type | Required | Description  
---|---|---|---  
event | String | Yes | Operation  
`login`  
`error`  
code | String | No | Error code  
msg | String | No | Error message  
connId | String | Yes | WebSocket connection ID  
  
**apiKey** : Unique identification for invoking API. Requires user to apply one manually.

**passphrase** : API Key password

**timestamp** : the Unix Epoch time, the unit is seconds, e.g. 1704876947

**sign** : signature string, the signature algorithm is as follows:

First concatenate `timestamp`, `method`, `requestPath`, strings, then use HMAC SHA256 method to encrypt the concatenated string with SecretKey, and then perform Base64 encoding.

**secretKey** : The security key generated when the user applies for API key, e.g. `22582BD0CFF14C41EDBF1AB98506286D`

**Example of timestamp** : const timestamp = '' + Date.now() / 1,000

**Among sign example** : sign=CryptoJS.enc.Base64.stringify(CryptoJS.HmacSHA256(timestamp +'GET'+'/users/self/verify', secretKey))

**method** : always 'GET'.

**requestPath** : always '/users/self/verify'

The request will expire 30 seconds after the timestamp. If your server time differs from the API server time, we recommended using the REST API to query the API server time and then set the timestamp. 

### Subscribe

**Subscription Instructions**

> Request format description
    
    
    {
      "id": "1512",
      "op": "subscribe",
      "args": ["<SubscriptionTopic>"]
    }
    

WebSocket channels are divided into two categories: `public` and `private` channels.

`Public channels` \-- No authentication is required, include tickers channel, K-Line channel, limit price channel, order book channel, and mark price channel etc.

`Private channels` \-- including account channel, order channel, and position channel, etc -- require log in.

Users can choose to subscribe to one or more channels, and the total length of multiple channels cannot exceed 64 KB.

Below is an example of subscription parameters. The requirement of subscription parameters for each channel is different. For details please refer to the specification of each channels.

> Request Example
    
    
    {
        "id": "1512",
        "op":"subscribe",
        "args":[
            {
                "channel":"tickers",
                "instId":"BTC-USDT"
            }
        ]
    }
    

**Request parameters**

Parameter | Type | Required | Description  
---|---|---|---  
id | String | No | Unique identifier of the message   
Provided by client. It will be returned in response message for identifying the corresponding request.   
A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters.  
op | String | Yes | Operation  
`subscribe`  
args | Array of objects | Yes | List of subscribed channels  
> channel | String | Yes | Channel name  
> instType | String | No | Instrument type  
`SPOT`  
`MARGIN`  
`SWAP`  
`FUTURES`  
`OPTION`  
`ANY`  
> instFamily | String | No | Instrument family  
Applicable to `FUTURES`/`SWAP`/`OPTION`  
> instId | String | No | Instrument ID  
  
> Response Example
    
    
    {
        "id": "1512",
        "event": "subscribe",
        "arg": {
            "channel": "tickers",
            "instId": "BTC-USDT"
        },
        "connId": "accb8e21"
    }
    

**Return parameters**

Parameter | Type | Required | Description  
---|---|---|---  
id | String | No | Unique identifier of the message  
event | String | Yes | Event  
`subscribe`  
`error`  
arg | Object | No | Subscribed channel  
> channel | String | Yes | Channel name  
> instType | String | No | Instrument type  
`SPOT`  
`MARGIN`  
`SWAP`  
`FUTURES`  
`OPTION`  
`ANY`  
> instFamily | String | No | Instrument family  
Applicable to `FUTURES`/`SWAP`/`OPTION`  
> instId | String | No | Instrument ID  
code | String | No | Error code  
msg | String | No | Error message  
connId | String | Yes | WebSocket connection ID  
  
### Unsubscribe

Unsubscribe from one or more channels.

> Request format description
    
    
    {
      "op": "unsubscribe",
      "args": ["< SubscriptionTopic> "]
    }
    

> Request Example
    
    
    {
      "op": "unsubscribe",
      "args": [
        {
          "channel": "tickers",
          "instId": "BTC-USDT"
        }
      ]
    }
    

**Request parameters**

Parameter | Type | Required | Description  
---|---|---|---  
op | String | Yes | Operation  
`unsubscribe`  
args | Array of objects | Yes | List of channels to unsubscribe from  
> channel | String | Yes | Channel name  
> instType | String | No | Instrument type  
`SPOT`  
`MARGIN`  
`SWAP`  
`FUTURES`  
`OPTION`  
`ANY`  
> instFamily | String | No | Instrument family  
Applicable to `FUTURES`/`SWAP`/`OPTION`  
> instId | String | No | Instrument ID  
  
> Response Example
    
    
    {
        "event": "unsubscribe",
        "arg": {
            "channel": "tickers",
            "instId": "BTC-USDT"
        },
        "connId": "d0b44253"
    }
    

**Response parameters**

Parameter | Type | Required | Description  
---|---|---|---  
event | String | Yes | Event  
`unsubscribe`  
`error`  
arg | Object | No | Unsubscribed channel  
> channel | String | Yes | Channel name  
> instType | String | No | Instrument type  
`SPOT`  
`MARGIN`  
`SWAP`  
`FUTURES`  
`OPTION`  
> instFamily | String | No | Instrument family  
Applicable to `FUTURES`/`SWAP`/`OPTION`  
> instId | String | No | Instrument ID  
code | String | No | Error code  
msg | String | No | Error message  
  
### Notification

WebSocket has introduced a new message type (event = `notice`).   
  

Client will receive the information in the following scenarios:

  * Websocket disconnect for service upgrade  

60 seconds prior to the upgrade of the WebSocket service, the notification message will be sent to users indicating that the connection will soon be disconnected. Users are encouraged to establish a new connection to prevent any disruptions caused by disconnection.

> Response Example
    
    
    {
        "event": "notice",
        "code": "64008",
        "msg": "The connection will soon be closed for a service upgrade. Please reconnect.",
        "connId": "a4d3ae55"
    }
    

  
  
The feature is supported by WebSocket Public (/ws/v5/public) and Private (/ws/v5/private) for now.

## Account mode

To facilitate your trading experience, please set the appropriate account mode before starting trading.

In the trading account trading system, 4 account modes are supported: `Spot mode`, `Futures mode`, `Multi-currency margin mode`, and `Portfolio margin mode`.

You need to set on the Web/App for the first set of every account mode.

## Production Trading Services

The Production Trading URL: 

  * REST: `https://openapi.okx.com`  

  * Public WebSocket: `wss://ws.okx.com:8443/ws/v5/public`  

  * Private WebSocket: `wss://ws.okx.com:8443/ws/v5/private`
  * Business WebSocket: `wss://ws.okx.com:8443/ws/v5/business`

## Demo Trading Services

Currently, the API works for Demo Trading, but some functions are not supported, such as `withdraw`,`deposit`,`purchase/redemption`, etc.

The Demo Trading URL: 

  * REST: `https://openapi.okx.com`  

  * Public WebSocket: `wss://wspap.okx.com:8443/ws/v5/public`  

  * Private WebSocket: `wss://wspap.okx.com:8443/ws/v5/private`  

  * Business WebSocket: `wss://wspap.okx.com:8443/ws/v5/business`

OKX account can be used for login on Demo Trading. If you already have an OKX account, you can log in directly.

Start API Demo Trading by the following steps:  
Login OKX —> Trade —> Demo Trading —> Personal Center —> Demo Trading API -> Create Demo Trading API Key —> Start your Demo Trading

Note: `x-simulated-trading: 1` needs to be added to the header of the Demo Trading request. 

> Http Header Example 
    
    
    Content-Type: application/json
    
    OK-ACCESS-KEY: 37c541a1-****-****-****-10fe7a038418
    
    OK-ACCESS-SIGN: leaVRETrtaoEQ3yI9qEtI1CZ82ikZ4xSG5Kj8gnl3uw=
    
    OK-ACCESS-PASSPHRASE: 1****6
    
    OK-ACCESS-TIMESTAMP: 2020-03-28T12:21:41.274Z
    
    x-simulated-trading: 1
    

### Demo Trading Explorer

You need to sign in to your OKX account before accessing the explorer. The interface only allow access to the demo trading environment.

  * Clicking `Try it out` button in Parameters Panel and editing request parameters.

  * Clicking `Execute` button to send your request. You can check response in Responses panel.

Try [demo trading explorer](/demo-trading-explorer/v5/en)

## General Info

**The rules for placing orders at the exchange level are as follows:**

  * The maximum number of pending orders (including post only orders, limit orders and taker orders that are being processed): 4,000 
  * The maximum number of pending orders per trading symbol is 500, the limit of 500 pending orders applies to the following **order types** : 

    * Limit
    * Market
    * Post only
    * Fill or Kill (FOK)
    * Immediate or Cancel (IOC)
    * Market order with Immediate-or-Cancel order (optimal limit IOC)
    * Take Profit / Stop Loss (TP/SL)
    * Limit and market orders triggered under the order types below: 
      * Take Profit / Stop Loss (TP/SL)
      * Trigger
      * Trailing stop
      * Arbitrage
      * Iceberg
      * TWAP
      * Recurring buy
  * The maximum number of pending spread orders: 500 across all spreads

  * The maximum number of pending algo orders: 

    * TP/SL order: 100 per instrument
    * Trigger order: 500
    * Trailing order: 50
    * Iceberg order: 100
    * TWAP order: 20
  * The maximum number of grid trading

    * Spot grid: 100
    * Contract grid: 100

  

**The rules for trading are as follows:**

  * When the number of maker orders matched with a taker order exceeds the maximum number limit of 1000, the taker order will be canceled. 
    * The limit orders will only be executed with a portion corresponding to 1000 maker orders and the remainder will be canceled.
    * Fill or Kill (FOK) orders will be canceled directly.

  

**The rules for the returning data are as follows:**

  * `code` and `msg` represent the request result or error reason when the return data has `code`, and has not `sCode`;

  * It is `sCode` and `sMsg` that represent the request result or error reason when the return data has `sCode` rather than `code` and `msg`.

  

**`instFamily` and `uly` parameter explanation:**

  * The following explanation is based on the `BTC` contract, other contracts are similar.
  * `uly` is the index, like "BTC-USD", and there is a one-to-many relationship with the settlement and margin currency (`settleCcy`).
  * `instFamily` is the trading instrument family, like `BTC-USD_UM`, and there is a one-to-one relationship with the settlement and margin currency (`settleCcy`).
  * The following table shows the corresponding relationship of `uly`, `instFamily`, `settleCcy` and `instId`.

**Contract Type** | **uly** | **instFamily** | **settleCcy** | **Delivery contract instId** | **Swap contract instId**  
---|---|---|---|---|---  
USDT-margined contract | BTC-USDT | BTC-USDT | USDT | BTC-USDT-250808 | BTC-USDT-SWAP  
USDC-margined contract | BTC-USDC | BTC-USDC | USDC | BTC-USDC-250808 | BTC-USDC-SWAP  
USD-margined contract | BTC-USD | **BTC-USD_UM** | **USDⓈ** | **BTC-USD_UM-250808** | **BTC-USD_UM-SWAP**  
Coin-margined contract | BTC-USD | **BTC-USD** | **BTC** | **BTC-USD-250808** | **BTC-USD-SWAP**  
  
Note:  
1\. USDⓈ represents USD and multiple USD stable coins, like USDC, USDG.  
2\. The settlement and margin currency refers to the `settleCcy` field returned by the [Get instruments](/docs-v5/en/#trading-account-rest-api-get-instruments) endpoint.

## Transaction Timeouts

Orders may not be processed in time due to network delay or busy OKX servers. You can configure the expiry time of the request using `expTime` if you want the order request to be discarded after a specific time.

If `expTime` is specified in the requests for Place (multiple) orders or Amend (multiple) orders, the request will not be processed if the current system time of the server is after the `expTime`.

### REST API

Set the following parameters in the request header

Parameter | Type | Required | Description  
---|---|---|---  
expTime | String | No | Request effective deadline. Unix timestamp format in milliseconds, e.g. `1597026383085`  
  
The following endpoints are supported:

  * [Place order](/docs-v5/en/#order-book-trading-trade-post-place-order)
  * [Place multiple orders](/docs-v5/en/#order-book-trading-trade-post-place-multiple-orders)
  * [Amend order](/docs-v5/en/#order-book-trading-trade-post-amend-order)
  * [Amend multiple orders](/docs-v5/en/#order-book-trading-trade-post-amend-multiple-orders)
  * [POST / Place sub order](/docs-v5/en/#order-book-trading-signal-bot-trading-post-place-sub-order) under signal bot trading

> Request Example
    
    
    curl -X 'POST' \
      'https://openapi.okx.com/api/v5/trade/order' \
      -H 'accept: application/json' \
      -H 'Content-Type: application/json' \
      -H 'OK-ACCESS-KEY: *****' \
      -H 'OK-ACCESS-SIGN: *****'' \
      -H 'OK-ACCESS-TIMESTAMP: *****'' \
      -H 'OK-ACCESS-PASSPHRASE: *****'' \
      -H 'expTime: 1597026383085' \   // request effective deadline
      -d '{
      "instId": "BTC-USDT",
      "tdMode": "cash",
      "side": "buy",
      "ordType": "limit",
      "px": "1000",
      "sz": "0.01"
    }'
    

### WebSocket

The following parameters are set in the request

Parameter | Type | Required | Description  
---|---|---|---  
expTime | String | No | Request effective deadline. Unix timestamp format in milliseconds, e.g. `1597026383085`  
  
The following endpoints are supported:

  * [Place order](/docs-v5/en/#order-book-trading-trade-ws-place-order)
  * [Place multiple orders](/docs-v5/en/#order-book-trading-trade-ws-place-multiple-orders)
  * [Amend order](/docs-v5/en/#order-book-trading-trade-ws-amend-order)
  * [Amend multiple orders](/docs-v5/en/#order-book-trading-trade-ws-amend-multiple-orders)

> Request Example
    
    
    {
        "id": "1512",
        "op": "order",
        "expTime":"1597026383085",  // request effective deadline
        "args": [{
            "side": "buy",
            "instId": "BTC-USDT",
            "tdMode": "isolated",
            "ordType": "market",
            "sz": "100"
        }]
    }
    

## Rate Limits

Our REST and WebSocket APIs use rate limits to protect our APIs against malicious usage so our trading platform can operate reliably and fairly.  
When a request is rejected by our system due to rate limits, the system returns error code 50011 (Rate limit reached. Please refer to API documentation and throttle requests accordingly).  
The rate limit is different for each endpoint. You can find the limit for each endpoint from the endpoint details. Rate limit definitions are detailed below:

  * WebSocket login and subscription rate limits are based on connection.

  * Public unauthenticated REST rate limits are based on IP address.

  * Private REST rate limits are based on User ID (sub-accounts have individual User IDs).

  * WebSocket order management rate limits are based on User ID (sub-accounts have individual User IDs).

### Trading-related APIs

For Trading-related APIs (place order, cancel order, and amend order) the following conditions apply:

  * Rate limits are shared across the REST and WebSocket channels. 

  * Rate limits for placing orders, amending orders, and cancelling orders are independent from each other. 

  * Rate limits are defined on the Instrument ID level (except Options)

  * Rate limits for Options are defined based on the Instrument Family level. Refer to the [Get instruments](/docs-v5/en/#public-data-rest-api-get-instruments) endpoint to view Instrument Family information.

  * Rate limits for a multiple order endpoint and a single order endpoint are also independent, with the exception being when there is only one order sent to a multiple order endpoint, the order will be counted as a single order and adopt the single order rate limit. 

### Sub-account rate limit

At the sub-account level, we allow a maximum of 1000 order requests per 2 seconds. Only new order requests and amendment order requests will be counted towards this limit. The limit encompasses all requests from the endpoints below. For batch order requests consisting of multiple orders, each order will be counted individually. Error code 50061 is returned when the sub-account rate limit is exceeded. The existing rate limit rule per instrument ID remains unchanged and the existing rate limit and sub-account rate limit will operate in parallel. If clients require a higher rate limit, clients can trade via multiple sub-accounts.

  * [POST / Place order](/docs-v5/en/#order-book-trading-trade-post-place-order)
  * [POST / Place multiple orders](/docs-v5/en/#order-book-trading-trade-post-place-multiple-orders)
  * [POST / Amend order](/docs-v5/en/#order-book-trading-trade-post-amend-order)
  * [POST / Amend multiple orders](/docs-v5/en/#order-book-trading-trade-post-amend-multiple-orders)

  * [WS / Place order](/docs-v5/en/#order-book-trading-trade-ws-place-order)

  * [WS / Place multiple orders](/docs-v5/en/#order-book-trading-trade-ws-place-multiple-orders)

  * [WS / Amend order](/docs-v5/en/#order-book-trading-trade-ws-amend-order)

  * [WS / Amend multiple orders](/docs-v5/en/#order-book-trading-trade-ws-amend-multiple-orders)   

### Fill ratio based sub-account rate limit

This is only applicable to >= VIP5 customers.   
As an incentive for more efficient trading, the exchange will offer a higher sub-account rate limit to clients with a high trade fill ratio.   
  
The exchange calculates two ratios based on the transaction data from the past 7 days at 00:00 UTC.

  1. Sub-account fill ratio: This ratio is determined by dividing (the trade volume in USDT of the sub-account) by (sum of (new and amendment request count per symbol * symbol multiplier) of the sub-account). Note that the master trading account itself is also considered as a sub-account in this context.
  2. Master account aggregated fill ratio: This ratio is calculated by dividing (the trade volume in USDT on the master account level) by (the sum (new and amendment count per symbol * symbol multiplier] of all sub-accounts).

  

The symbol multiplier allows for fine-tuning the weight of each symbol. A smaller symbol multiplier (<1) is used for smaller pairs that require more updates per trading volume. All instruments have a default symbol multiplier, and some instruments will have overridden symbol multipliers.

InstType | Override rule | Overridden symbol multiplier | Default symbol multiplier  
---|---|---|---  
Perpetual Futures | Per instrument ID | `1`   
Instrument ID:   
BTC-USDT-SWAP   
BTC-USD-SWAP   
ETH-USDT-SWAP   
ETH-USD-SWAP | `0.2`  
Expiry Futures | Per instrument Family | `0.3`   
Instrument Family:   
BTC-USDT   
BTC-USD   
ETH-USDT   
ETH-USD | `0.1`  
Spot | Per instrument ID | `0.5`   
Instrument ID:   
BTC-USDT   
ETH-USDT | `0.1`  
Options | Per instrument Family |  | `0.1`  
  
The fill ratio computation excludes block trading, spread trading, MMP and fiat orders for order count; and excludes block trading, spread trading for trade volume. Only successful order requests (sCode=0) are considered.

  
  

At 08:00 UTC, the system will use the maximum value between the sub-account fill ratio and the master account aggregated fill ratio based on the data snapshot at 00:00 UTC to determine the sub-account rate limit based on the table below. For broker (non-disclosed) clients, the system considers the sub-account fill ratio only.

| Fill ratio[x<=ratio<y) | Sub-account rate limit per 2 seconds(new and amendment)  
---|---|---  
Tier 1 | [0,1) | 1,000  
Tier 2 | [1,2) | 1,250  
Tier 3 | [2,3) | 1,500  
Tier 4 | [3,5) | 1,750  
Tier 5 | [5,10) | 2,000  
Tier 6 | [10,20) | 2,500  
Tier 7 | [20,50) | 3,000  
Tier 8 | >= 50 | 10,000  
  
If there is an improvement in the fill ratio and rate limit to be uplifted, the uplift will take effect immediately at 08:00 UTC. However, if the fill ratio decreases and the rate limit needs to be lowered, a one-day grace period will be granted, and the lowered rate limit will only be implemented on T+1 at 08:00 UTC. On T+1, if the fill ratio improves, the higher rate limit will be applied accordingly. In the event of client demotion to VIP4, their rate limit will be downgraded to Tier 1, accompanied by a one-day grace period.

  

If the 7-day trading volume of a sub-account is less than 1,000,000 USDT, the fill ratio of the master account will be applied to it.

  

For newly created sub-accounts, the Tier 1 rate limit will be applied at creation until T+1 8am UTC, at which the normal rules will be applied.

  

Block trading, spread trading, MMP and spot/margin orders are exempted from the sub-account rate limit.

  

The exchange offers [GET / Account rate limit](/docs-v5/en/#order-book-trading-trade-get-account-rate-limit) endpoint that provides ratio and rate limit data, which will be updated daily at 8am UTC. It will return the sub-account fill ratio, the master account aggregated fill ratio, current sub-account rate limit and sub-account rate limit on T+1 (applicable if the rate limit is going to be demoted).   
  
The fill ratio and rate limit calculation example is shown below. Client has 3 accounts, symbol multiplier for BTC-USDT-SWAP = 1 and XRP-USDT = 0.1.

  1. Account A (master account): 
     1. BTC-USDT-SWAP trade volume = 100 USDT, order count = 10;
     2. XRP-USDT trade volume = 20 USDT, order count = 15;
     3. Sub-account ratio = (100+20) / (10 * 1 + 15 * 0.1) = 10.4
  2. Account B (sub-account): 
     1. BTC-USDT-SWAP trade volume = 200 USDT, order count = 100;
     2. XRP-USDT trade volume = 20 USDT, order count = 30;
     3. Sub-account ratio = (200+20) / (100 * 1 + 30 * 0.1) = 2.13
  3. Account C (sub-account): 
     1. BTC-USDT-SWAP trade volume = 300 USDT, order count = 1000;
     2. XRP-USDT trade volume = 20 USDT, order count = 45;
     3. Sub-account ratio = (300+20) / (100 * 1 + 45 * 0.1) = 3.06
  4. Master account aggregated fill ratio = (100+20+200+20+300+20) / (10 * 1 + 15 * 0.1 + 100 * 1 + 30 * 0.1 + 100 * 1 + 45 * 0.1) = 3.01
  5. Rate limit of accounts 
     1. Account A = max(10.4, 3.01) = 10.4 -> 2500 order requests/2s
     2. Account B = max(2.13, 3.01) = 3.01 -> 1750 order requests/2s
     3. Account C = max(3.06, 3.01) = 3.06 -> 1750 order requests/2s

### Best practices

If you require a higher request rate than our rate limit, you can set up different sub-accounts to batch request rate limits. We recommend this method for throttling or spacing out requests in order to maximize each accounts' rate limit and avoid disconnections or rejections. 

## Market Maker Program

High-caliber trading teams are welcomed to work with OKX as market makers in providing a liquid, fair, and orderly platform to all users. OKX market makers could enjoy favourable fees in return for meeting the market making obligations.  

Prerequisites (Satisfy any condition): 

  * VIP 2 or above on fee schedule  

  * Qualified Market Maker on other exchange  

Interested parties can reach out to us at `Institutional@okx.com`  

Remarks:

Market making obligations and trading fees will be shared to successful parties only.

OKX reserves the right of final decision and interpretation for the content hereinabove.  In fairness to all users, market makers will be ineligible for other VIP-related and volume-related promotions or rebates. 

## Broker Program

If your business platform offers cryptocurrency services, you can apply to join the OKX Broker Program, become our partner broker, enjoy exclusive broker services, and earn high rebates through trading fees generated by OKX users.  
The Broker Program includes, and is not limited to, integrated trading platforms, trading bots, copy trading platforms, trading bot providers, quantitative strategy institutions, asset management platforms etc.  

  * [Click to apply](/broker/home)
  * [Broker rules](/help/introduction-of-rules-on-okx-brokers)
  * If you have any questions, feel free to contact our customer support.

Relevant information for specific Broker Program documentation and product services will be provided following successful applications.

---

# 概览

欢迎查看 API 文档。我们提供完整的REST和WebSocket API以满足您的交易需求。  

**【重要】欧易 API 协议：继续使用即视为接受**  
  
我们建议您在使用 API 服务前完整阅读[《欧易 API 协议》](https://www.okx.com/help/okx-api-agreement)，继续使用任何欧易 API 服务即视为您完全接受本协议。  
若您不同意本协议，您必须立即停止使用所有欧易 API 服务，包括：断开所有活跃的 API 集成；断开 Agent Trade Kit 连接；关闭通过 API 访问欧易的自动化系统。  **【重要】区域 API 域名要求**  
  
根据您的注册地区，进行 API 调用和查阅文档时**必须** 使用对应的域名。  
以下地区用户使用 `openapi.okx.com` 将无法正常访问。  
  
**美国及澳大利亚用户** （在 [app.okx.com](https://app.okx.com) 完成注册）：请使用 `us.okx.com` 作为 API 域名。请参阅 [美国及澳大利亚 API 文档](https://app.okx.com/docs-v5/en/)。  
**欧盟用户** （在 [my.okx.com](https://my.okx.com) 完成注册）：请使用 `eea.okx.com` 作为 API 域名。请参阅 [欧盟 API 文档](https://my.okx.com/docs-v5/en/)。  

## API学习资源与技术支持 

### 教程 

  * 学习使用 API 交易: [API 使用指南](/docs-v5/trick_zh/#instrument-configuration)
  * 学习使用Python交易现货: [Python 现货交易教程](/help/how-can-i-do-spot-trading-with-the-jupyter-notebook)
  * 学习使用Python交易衍生品: [Python 衍生品交易教程](/help/how-can-i-do-derivatives-trading-with-the-jupyter-notebook)

  

### Python包 

  * 使用Python SDK更简单地上手: [Python SDK](https://pypi.org/project/python-okx/)
  * 轻松上手Python做市商代码 [Python 做市商代码示例](https://github.com/okxapi/okx-sample-market-maker)   

### 客户服务 

  * 如有问题,您可以通过欧易 App 扫码进群与技术专员联系。  
打开 App，点击左上角全功能图标，再点击右上角扫码图标，扫描右侧二维码即可。

![API 技术支持二维码](images/APISupport-b5a4ebca.jpeg)

## 创建我的APIKey 

点击跳转至官网创建V5APIKey的页面 [创建我的APIKey](/account/my-api)  

### 生成APIKey 

在对任何请求进行签名之前，您必须通过交易网站创建一个APIKey。创建APIKey后，您将获得3个必须记住的信息：

  * APIKey
  * SecretKey
  * Passphrase

APIKey和SecretKey将由平台随机生成和提供，Passphrase将由您提供以确保API访问的安全性。平台将存储Passphrase加密后的哈希值进行验证，但如果您忘记Passphrase，则无法恢复，请您通过交易网站重新生成新的APIKey。  
  

### APIKey 权限 

APIKey 有如下3种权限，一个 APIKey 可以有一个或多个权限。

  * 读取 ：查询账单和历史记录等 读权限
  * 提现 ：可以进行提币
  * 交易 ：可以下单和撤单，转账，调整配置 等写权限

### APIKey 安全性 

为了提高安全性，我们建议您将 APIKey 绑定 IP  

  * 每个APIKey最多可绑定20个IP地址，IP地址支持IPv4/IPv6和网段的格式。   

未绑定IP且拥有交易或提币权限的APIKey，将在闲置14天之后自动删除。(模拟盘的 API key 不会被删除)  

  * 用户调用了需要 APIKey 鉴权的接口，才会被视为 APIKey 被使用。
  * 调用了不需要 APIKey 鉴权的接口，即使传入了 APIKey的信息，也不会被视为使用过。
  * Websocket 只有在登陆的时候，才会被视为 APIKey 被使用过。在登陆后的连接中做任何操作（如 订阅/下单），也不会被认为 APIKey 被使用，这点需要注意。

用户可以在 [安全中心](/zh-hans/account/security) 中看到未绑定IP且拥有交易/提现权限的 APIKey 最近使用记录。

## REST 请求验证 

### 发起请求 

所有REST私有请求头都必须包含以下内容：

  * `OK-ACCESS-KEY`字符串类型的APIKey。

  * `OK-ACCESS-SIGN`使用HMAC SHA256哈希函数获得哈希值，再使用Base-64编码（请参阅签名）。

  * `OK-ACCESS-TIMESTAMP` 请求时间戳，ISO 8601 UTC格式，精确到毫秒，如：`2020-12-08T09:08:57.715Z`。服务器将拒绝与服务器时间相差超过30秒的请求（错误码50102）。请务必使用UTC时间——时区偏差是导致50102错误最常见的原因。建议在下单前通过 GET /api/v5/public/time 与服务器时间同步。

  * `OK-ACCESS-PASSPHRASE`您在创建API密钥时指定的Passphrase。

所有请求都应该含有application/json类型内容，并且是有效的JSON。

### 签名 

> 生成签名

`OK-ACCESS-SIGN`的请求头是对`timestamp + method + requestPath + body`字符串（+表示字符串连接），以及SecretKey，使用HMAC SHA256方法加密，通过Base-64编码输出而得到的。

如：`sign=CryptoJS.enc.Base64.stringify(CryptoJS.HmacSHA256(timestamp + 'GET' + '/api/v5/account/balance?ccy=BTC', SecretKey))`

其中，`timestamp`的值与`OK-ACCESS-TIMESTAMP`请求头相同，为ISO格式，如`2020-12-08T09:08:57.715Z`。

method是请求方法，字母全部大写：`GET/POST`。

requestPath是请求接口路径。如：`/api/v5/account/balance`

body是指请求主体的字符串，如果请求没有主体（通常为GET请求）则body可省略。如：`{"instId":"BTC-USDT","lever":"5","mgnMode":"isolated"}`

GET请求参数是算作requestPath，不算body 

SecretKey为用户申请APIKey时所生成。如：`22582BD0CFF14C41EDBF1AB98506286D`

## WebSocket 

### 概述 

WebSocket是HTML5一种新的协议（Protocol）。它实现了用户端与服务器全双工通信， 使得数据可以快速地双向传播。通过一次简单的握手就可以建立用户端和服务器连接， 服务器根据业务规则可以主动推送信息给用户端。其优点如下：

  * 用户端和服务器进行数据传输时，请求头信息比较小，大概2个字节。
  * 用户端和服务器皆可以主动地发送数据给对方。
  * 不需要多次创建TCP请求和销毁，节约宽带和服务器的资源。

强烈建议开发者使用WebSocket API获取市场行情和买卖深度等信息。 

### 连接 

**连接限制** ：3 次/秒 (基于IP)

当订阅公有频道时，使用公有服务的地址；当订阅私有频道时，使用私有服务的地址

**请求限制** ：

每个连接 对于 `订阅`/`取消订阅`/`登录` 请求的总次数限制为 480 次/小时

如果出现网络问题，系统会自动断开连接

如果连接成功后30s未订阅或订阅后30s内服务器未向用户推送数据，系统会自动断开连接

为了保持连接有效且稳定，建议您进行以下操作：

1\. 每次接收到消息后，用户设置一个定时器，定时N秒，N 小于30。

2\. 如果定时器被触发（N 秒内没有收到新消息），发送字符串 'ping'。

3\. 期待一个文字字符串'pong'作为回应。如果在 N秒内未收到，请发出错误或重新连接。

### 连接限制 

子账户维度，订阅每个 WebSocket 频道的最大连接数为 30 个。每个 WebSocket 连接都由唯一的 connId 标识。

  

受此限制的 WebSocket 频道如下：

  1. [订单频道](/docs-v5/zh/#order-book-trading-trade-ws-order-channel)
  2. [账户频道](/docs-v5/zh/#trading-account-websocket-account-channel)
  3. [持仓频道](/docs-v5/zh/#trading-account-websocket-positions-channel)
  4. [账户余额和持仓频道](/docs-v5/zh/#trading-account-websocket-balance-and-position-channel)
  5. [爆仓风险预警推送频道](/docs-v5/zh/#trading-account-websocket-position-risk-warning)
  6. [账户greeks频道](/docs-v5/zh/#trading-account-websocket-account-greeks-channel)

若用户通过不同的请求参数在同一个 WebSocket 连接下订阅同一个频道，如使用 `{"channel": "orders", "instType": "ANY"}` 和 `{"channel": "orders", "instType": "SWAP"}`，只算为一次连接。若用户使用相同或不同的 WebSocket 连接订阅上述频道，如订单频道和账户频道。在该两个频道之间，计数不会累计，因为它们被视作不同的频道。简言之，系统计算每个频道对应的 WebSocket 连接数量。

  

新链接订阅频道时，平台将对该订阅返回`channel-conn-count`的消息同步链接数量。

> 链接数量更新
    
    
    {
        "event":"channel-conn-count",
        "channel":"orders",
        "connCount": "2",
        "connId":"abcd1234"
    }
    
    

  

当超出限制时，一般最新订阅的链接会收到拒绝。用户会先收到平时的订阅成功信息然后收到`channel-conn-count-error`消息，代表平台终止了这个链接的订阅。在异常场景下平台会终止已订阅的现有链接。

> 链接数量限制报错
    
    
    {
        "event": "channel-conn-count-error",
        "channel": "orders",
        "connCount": "30",
        "connId":"a4d3ae55"
    }
    
    

  

通过 WebSocket 进行的订单操作，例如下单、修改和取消订单，不会受到此改动影响。

### 登录 

> 请求示例
    
    
    {
     "op": "login",
     "args":
      [
         {
           "apiKey": "******",
           "passphrase": "******",
           "timestamp": "1538054050",
           "sign": "7L+zFQ+CEgGu5rzCj4+BdV2/uUHGqddA9pI6ztsRRPs=" 
          }
       ]
    }
    

#### 请求参数

参数 | 类型 | 是否必须 | 描述  
---|---|---|---  
op | String | 是 | 操作，`login`  
args | Array of objectss | 是 | 账户列表  
> apiKey | String | 是 | APIKey  
> passphrase | String | 是 | APIKey 的密码  
> timestamp | String | 是 | 时间戳，Unix Epoch时间，单位是秒  
> sign | String | 是 | 签名字符串  
  
> 全部成功返回示例
    
    
    {
      "event": "login",
      "code": "0",
      "msg": "",
      "connId": "a4d3ae55"
    }
    

> 全部失败返回示例
    
    
    {
      "event": "error",
      "code": "60009",
      "msg": "Login failed.",
      "connId": "a4d3ae55"
    }
    

#### 返回参数

参数 | 类型 | 是否必须 | 描述  
---|---|---|---  
event | String | 是 | 操作，`login` `error`  
code | String | 否 | 错误码  
msg | String | 否 | 错误消息  
connId | String | 是 | WebSocket连接ID  
  
**apiKey** :调用API的唯一标识。需要用户手动设置一个 **passphrase** :APIKey的密码 **timestamp** :Unix Epoch 时间戳，单位为秒，如 1704876947 **sign** :签名字符串，签名算法如下：

先将`timestamp` 、 `method` 、`requestPath` 进行字符串拼接，再使用HMAC SHA256方法将拼接后的字符串和SecretKey加密，然后进行Base64编码

**SecretKey:** 用户申请APIKey时所生成的安全密钥，如：22582BD0CFF14C41EDBF1AB98506286D

**其中 timestamp 示例** :const timestamp = '' + Date.now() / 1,000

**其中 sign 示例** : sign=CryptoJS.enc.Base64.stringify(CryptoJS.HmacSHA256(timestamp +'GET'+ '/users/self/verify', secret))

**method** 总是 'GET'

**requestPath** 总是 '/users/self/verify'

请求在时间戳之后30秒会失效，如果您的服务器时间和API服务器时间有偏差，推荐使用 REST API查询API服务器的时间，然后设置时间戳 

### 订阅 

**订阅说明**

> 请求格式说明
    
    
    {
        "op": "subscribe",
        "args": ["<SubscriptionTopic>"]
    }
    

WebSocket 频道分成两类： `公共频道` 和 `私有频道`

`公共频道`无需登录，包括行情频道，K线频道，交易数据频道，资金费率频道，限价范围频道，深度数据频道，标记价格频道等。

`私有频道`需登录，包括用户账户频道，用户交易频道，用户持仓频道等。

用户可以选择订阅一个或者多个频道，多个频道总长度不能超过 64 KB。

以下是一个请求参数的例子。每一个频道的请求参数的要求都不一样。请根据每一个频道的需求来订阅频道。

> 请求示例
    
    
    {
        "op":"subscribe",
        "args":[
            {
                "channel":"tickers",
                "instId":"BTC-USDT"
            }
        ]
    }
    
    

**请求参数**

参数 | 类型 | 是否必须 | 描述  
---|---|---|---  
op | String | 是 | 操作，`subscribe`  
args | Array of objects | 是 | 请求订阅的频道列表  
> channel | String | 是 | 频道名  
> instType | String | 否 | 产品类型  
`SPOT`：币币   
`MARGIN`：币币杠杆  
`SWAP`：永续  
`FUTURES`：交割  
`OPTION`：期权  
`ANY`：全部  
> instFamily | String | 否 | 交易品种  
适用于`交割`/`永续`/`期权`  
> instId | String | 否 | 产品ID  
  
> 返回示例 
    
    
    {
        "event": "subscribe",
        "arg": {
            "channel": "tickers",
            "instId": "BTC-USDT"
        },
        "connId": "accb8e21"
    }
    

**返回参数**

参数 | 类型 | 是否必须 | 描述  
---|---|---|---  
event | String | 是 | 事件，`subscribe` `error`  
arg | Object | 否 | 订阅的频道  
> channel | String | 是 | 频道名  
> instType | String | 否 | 产品类型  
`SPOT`：币币  
`MARGIN`：币币杠杆  
`SWAP`：永续  
`FUTURES`：交割  
`OPTION`：期权  
`ANY`：全部  
> instFamily | String | 否 | 交易品种  
适用于`交割`/`永续`/`期权`  
> instId | String | 否 | 产品ID  
code | String | 否 | 错误码  
msg | String | 否 | 错误消息  
connId | String | 是 | WebSocket连接ID  
  
### 取消订阅 

可以取消一个或者多个频道

> 请求格式说明
    
    
    {
        "op": "unsubscribe",
        "args": ["< SubscriptionTopic > "]
    }
    

> 请求示例
    
    
    {
      "op": "unsubscribe",
      "args": [
        {
          "channel": "tickers",
          "instId": "BTC-USDT"
        }
      ]
    }
    

**请求参数**

参数 | 类型 | 是否必须 | 描述  
---|---|---|---  
op | String | 是 | 操作，`unsubscribe`  
args | Array of objects | 是 | 取消订阅的频道列表  
> channel | String | 是 | 频道名  
> instType | String | 否 | 产品类型  
`SPOT`：币币  
`MARGIN`：币币杠杆  
`SWAP`：永续合约  
`FUTURES`：交割合约  
`OPTION`：期权  
`ANY`：全部  
> instFamily | String | 否 | 交易品种  
适用于`交割`/`永续`/`期权`  
> instId | String | 否 | 产品ID  
  
> 返回示例
    
    
    {
        "event": "unsubscribe",
        "arg": {
            "channel": "tickers",
            "instId": "BTC-USDT"
        },
        "connId": "d0b44253"
    }
    

**返回参数**

参数 | 类型 | 是否必须 | 描述  
---|---|---|---  
event | String | 是 | 事件，`unsubscribe` `error`  
arg | Object | 否 | 取消订阅的频道  
> channel | String | 是 | 频道名  
> instType | String | 否 | 产品类型  
`SPOT`：币币  
`MARGIN`：币币杠杆  
`SWAP`：永续合约  
`FUTURES`：交割合约  
`OPTION`：期权  
`ANY`：全部  
> instFamily | String | 否 | 交易品种  
适用于`交割`/`永续`/`期权`  
> instId | String | 否 | 产品ID  
code | String | 否 | 错误码  
msg | String | 否 | 错误消息  
connId | String | 是 | WebSocket连接ID  
  
### 通知 

WebSocket有一种消息类型(event=`notice`)。   
  

用户会在如下场景收到此类信息：

  * Websocket服务升级断线

在推送服务升级前60秒会推送信息，告知用户WebSocket服务即将升级。用户可以重新建立新的连接避免由于断线造成的影响。

> 返回示例
    
    
    {
        "event": "notice",
        "code": "64008",
        "msg": "The connection will soon be closed for a service upgrade. Please reconnect.",
        "connId": "a4d3ae55"
    }
    

  
  
目前支持WebSocket公共频道(/ws/v5/public)和私有频道(/ws/v5/private)。

## 账户模式 

为了方便您的交易体验，请在开始交易前设置适当的账户模式。

交易账户交易系统提供四个账户模式，分别为`现货模式`、`合约模式`、`跨币种保证金模式`以及`组合保证金模式`。

账户模式的首次设置，需要在网页或手机app上进行。

## 实盘交易 

实盘API交易地址如下： 

  * REST：`https://openapi.okx.com`  

  * WebSocket公共频道：`wss://ws.okx.com:8443/ws/v5/public`  

  * WebSocket私有频道：`wss://ws.okx.com:8443/ws/v5/private`
  * WebSocket业务频道：`wss://ws.okx.com:8443/ws/v5/business`

## 模拟盘交易 

目前可以进行 API 的模拟盘交易，部分功能不支持如`提币`、`充值`、`申购赎回`等。

模拟盘API交易地址如下： 

  * REST：`https://openapi.okx.com`
  * WebSocket公共频道：`wss://wspap.okx.com:8443/ws/v5/public`  

  * WebSocket私有频道：`wss://wspap.okx.com:8443/ws/v5/private`
  * WebSocket业务频道：`wss://wspap.okx.com:8443/ws/v5/business`

模拟盘的账户与欧易的账户是互通的，如果您已经有欧易账户，可以直接登录。

模拟盘API交易需要在模拟盘上创建APIKey：

登录欧易账户—>交易—>模拟交易—>个人中心—>创建模拟盘APIKey—>开始模拟交易

注意：模拟盘的请求的header里面需要添加 "x-simulated-trading: 1"。 

> 请求头示例
    
    
    Content-Type: application/json
    
    OK-ACCESS-KEY: 37c541a1-****-****-****-10fe7a038418
    
    OK-ACCESS-SIGN: leaVRETrtaoEQ3yI9qEtI1CZ82ikZ4xSG5Kj8gnl3uw=
    
    OK-ACCESS-PASSPHRASE: 1****6
    
    OK-ACCESS-TIMESTAMP: 2020-03-28T12:21:41.274Z
    
    x-simulated-trading: 1
    

### 模拟盘交互式浏览器 

该功能接口用户需先登录，接口只会请求模拟环境

  * Parameters 面板中点击`Try it out`按钮，编辑请求参数。

  * 点击`Execute`按钮发送请求。Responses 面板中查看请求结果。

立即体验 [交互式浏览器](/demo-trading-explorer/v5/zh)

## 基本信息 

**交易所层面的下单规则如下：**

  * 未成交订单（包括 post only，limit和处理中的taker单）的最大挂单数：4,000个
  * 单个交易产品未成交订单的最大挂单数为500个，被计入到 500 笔挂单数量限制的**订单类型** 包括： 

    * 限价委托 (Limit)
    * 市价委托 (Market)
    * 只挂单 (Post only)
    * 全部成交或立即取消 (FOK)
    * 立即成交并取消剩余 (IOC)
    * 市价委托立即成交并取消剩余 (optimal limit IOC)
    * 止盈止损 (TP/SL)
    * 以下类型的订单触发的限价和市价委托： 
      * 止盈止损 (TP/SL)
      * 计划委托 (Trigger)
      * 移动止盈止损 (Trailing stop)
      * 套利下单 (Arbitrage)
      * 冰山策略 (Iceberg)
      * 时间加权策略 (TWAP)
      * 定投 (Recurring buy)
  * 价差订单最大挂单数：所有价差订单挂单合计500个

  * 策略委托订单最大挂单数： 

    * 止盈止损：100个 每个Instrument ID
    * 计划委托：500个  

    * 移动止盈止损：50个  

    * 冰山委托：100个  

    * 时间加权委托：20个  

  * 网格策略最大个数： 

    * 现货网格：100个
    * 合约网格：100个  

  

**交易限制规则如下：**

  * 当taker订单匹配的maker订单数量超过最大限制1000笔时，taker订单将被取消 
    * 限价单仅成交与1000笔maker订单相对应的部分，并取消剩余；
    * 全部成交或立即取消（FOK）订单将直接被取消。

  

**返回数据规则如下：**

  * 当返回数据中，有`code`，且没有`sCode`字段时，`code`和`msg`代表请求结果或者报错原因；

  * 当返回中有`sCode`字段时，代表请求结果或者报错原因的是`sCode`和`sMsg`，而不是`code`和`msg`。

  

**`instFamily` 和 `uly` 参数说明：** \- 以下说明以 `BTC` 合约为例，其他币种的合约同理。 \- `uly` 是指数，如："BTC-USD"，与盈亏结算和保证金币种 (`settleCcy`) 会存在一对多的关系。 \- `instFamily` 是交易品种，如：`BTC-USD_UM`，与盈亏结算和保证金币种 (`settleCcy`) 一一对应。 \- 以下表格详细展示了 `uly`, `instFamily`，`settleCcy` 和 `instId` 的对应关系。

**合约类型** | **uly** | **instFamily** | **settleCcy** | **交割合约 instId** | **永续合约 instId**  
---|---|---|---|---|---  
USDT 本位合约 | BTC-USDT | BTC-USDT | USDT | BTC-USDT-250808 | BTC-USDT-SWAP  
USDC 本位合约 | BTC-USDC | BTC-USDC | USDC | BTC-USDC-250808 | BTC-USDC-SWAP  
USD 本位合约 | BTC-USD | **BTC-USD_UM** | **USDⓈ** | **BTC-USD_UM-250808** | **BTC-USD_UM-SWAP**  
币本位合约 | BTC-USD | **BTC-USD** | **BTC** | **BTC-USD-250808** | **BTC-USD-SWAP**  
  
注意：  
1\. USDⓈ 代表 USD 以及多种 USD 稳定币，如：USD, USDC, USDG。  
2\. 盈亏结算和保证金币种指的[获取交易产品基础信息（私有）](/docs-v5/zh/#trading-account-rest-api-get-instruments)接口返回的 `settleCcy` 字段。

## 交易时效性 

由于网络延时或者OKX服务器繁忙会导致订单无法及时处理。如果您对交易时效性有较高的要求，可以灵活设置请求有效截止时间`expTime`以达到你的要求。

（批量）下单，（批量）改单接口请求中如果包含`expTime`，如果服务器当前系统时间超过`expTime`，则该请求不会被服务器处理。

### REST API 

请求头中设置如下参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
expTime | String | 否 | 请求有效截止时间。Unix时间戳的毫秒数格式，如 `1597026383085`  
  
目前支持如下接口： 

  * [下单](/docs-v5/zh/#order-book-trading-trade-post-place-order)
  * [批量下单](/docs-v5/zh/#order-book-trading-trade-post-place-multiple-orders)
  * [修改订单](/docs-v5/zh/#order-book-trading-trade-post-amend-order)
  * [批量修改订单](/docs-v5/zh/#order-book-trading-trade-post-amend-multiple-orders)
  * 信号交易的 [POST / 下单](/docs-v5/zh/#order-book-trading-signal-bot-trading-post-place-sub-order)

> 请求示例
    
    
    curl -X 'POST' \
      'https://openapi.okx.com/api/v5/trade/order' \
      -H 'accept: application/json' \
      -H 'Content-Type: application/json' \
      -H 'OK-ACCESS-KEY: *****' \
      -H 'OK-ACCESS-SIGN: *****'' \
      -H 'OK-ACCESS-TIMESTAMP: *****'' \
      -H 'OK-ACCESS-PASSPHRASE: *****'' \
      -H 'expTime: 1597026383085' \   // 有效截止时间
      -d '{
      "instId": "BTC-USDT",
      "tdMode": "cash",
      "side": "buy",
      "ordType": "limit",
      "px": "1000",
      "sz": "0.01"
    }'
    

### WebSocket 

请求中设置如下参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
expTime | String | 否 | 请求有效截止时间。Unix时间戳的毫秒数格式，如 `1597026383085`  
  
目前支持如下接口： 

  * [下单](/docs-v5/zh/#order-book-trading-trade-ws-place-order)
  * [批量下单](/docs-v5/zh/#order-book-trading-trade-ws-place-multiple-orders)
  * [修改订单](/docs-v5/zh/#order-book-trading-trade-ws-amend-order)
  * [批量修改订单](/docs-v5/zh/#order-book-trading-trade-ws-amend-multiple-orders)

> 请求示例
    
    
    {
        "id": "1512",
        "op": "order",
        "expTime":"1597026383085",  // 有效截止时间
        "args": [{
            "side": "buy",
            "instId": "BTC-USDT",
            "tdMode": "isolated",
            "ordType": "market",
            "sz": "100"
        }]
    }
    

## 限速 

我们的 REST 和 WebSocket API 使用限速来保护我们的 API 免受恶意使用，因此我们的交易平台可以可靠和公平地运行。  
当请求因限速而被我们的系统拒绝时，系统会返回错误代码 50011（用户请求频率过快，超过该接口允许的限额。请参考 API 文档并限制请求）。  
每个接口的限速都不同。 您可以从接口详细信息中找到每个接口的限制。 限速定义详述如下：

  * WebSocket 登录和订阅限速基于连接。

  * 公共未经身份验证的 REST 限速基于 IP 地址。

  * 私有 REST 限速基于 User ID（子帐户具有单独的 User ID）。

  * WebSocket 订单管理限速基于 User ID（子账户具有单独的 User ID）。

### 交易相关API 

对于与交易相关的 API（下订单、取消订单和修改订单），以下条件适用：

  * 限速在 REST 和 WebSocket 通道之间共享。

  * 下单、修改订单、取消订单的限速相互独立。

  * 限速在 Instrument ID 级别定义（期权除外）

  * 期权的限速是根据 Instrument Family 级别定义的。 请参阅 [获取交易产品基础信息](/docs-v5/zh/#public-data-rest-api-get-instruments) 接口以查看交易品种信息。

  * 批量订单接口和单订单接口的限速也是独立的，除了只有一个订单发送到批量订单接口时，该订单将被视为一个订单并采用单订单限速。

### 子账户限速 

子账户维度，每2秒最多允许1000个订单相关请求。仅有新订单及修改订单请求会被计入此限制。此限制涵盖以下所列的所有接口。对于包含多个订单的批量请求，每个订单将被单独计数。如果请求频率超过限制，系统会返回50061错误码。产品ID维度的限速规则保持不变，现有的限速规则与新增的子账户维度限速将并行运行。若用户需要更高的速率限制，可以通过多个子账户进行交易。

  * [POST / 下单](/docs-v5/zh/#order-book-trading-trade-post-place-order)
  * [POST / 批量下单](/docs-v5/zh/#order-book-trading-trade-post-place-multiple-orders)
  * [POST / 修改订单](/docs-v5/zh/#order-book-trading-trade-post-amend-order)
  * [POST / 批量修改订单](/docs-v5/zh/#order-book-trading-trade-post-amend-multiple-orders)

  * [WS / 下单](/docs-v5/zh/#order-book-trading-trade-ws-place-order)

  * [WS / 批量下单](/docs-v5/zh/#order-book-trading-trade-ws-place-multiple-orders)

  * [WS / 改单](/docs-v5/zh/#order-book-trading-trade-ws-amend-order)

  * [WS / 批量改单](/docs-v5/zh/#order-book-trading-trade-ws-amend-multiple-orders)

### 基于成交比率的子账户限速 

仅适用于用户等级 >= VIP5的用户。   
为了激励更高效的交易，交易所将为交易成交比率高的用户提供更高的子账户限速。

交易所将在每天 00:00 UTC，根据过去七天的交易数据计算两个比率。

  1. 子账户成交比率：该比率为（子账户的USDT对应交易量）/（每个交易产品的新增和修改请求数 * 交易产品乘数之和）。请注意，在这种情况下，母账户自身也被视为一个“子账户”。
  2. 母账户合计成交比率：该比率为（母账户层面的USDT对应交易量）/（所有子账户各个交易产品的新增和修改请求数 * 交易产品乘数之和）。

交易产品乘数允许我们微调每个交易产品对成交比率的影响权重。较小的交易产品乘数（<1）适用于小币对及合约，在交易这些币对、合约时，为达到相同交易量往往需要更多的订单。所有的交易产品都有默认乘数，部分交易产品有独立的乘数。详情请见下表。

业务线 | 覆盖规则 | 独立乘数 | 默认乘数  
---|---|---|---  
永续 | 产品ID | `1`   
产品ID：   
BTC-USDT-SWAP   
BTC-USD-SWAP   
ETH-USDT-SWAP   
ETH-USD-SWAP | `0.2`  
交割 | 交易品种 | `0.3`   
交易品种：   
BTC-USDT   
BTC-USD   
ETH-USDT   
ETH-USD | `0.1`  
币币 | 产品ID | `0.5`   
产品ID：   
BTC-USDT   
ETH-USDT | `0.1`  
期权 | 交易品种 |  | `0.1`  
  
成交比率计算不包括大宗交易，价差交易，做市商保护（MMP），以及法币类型订单对应的订单数量；并且不包括大宗交易，价差交易对应的交易量。仅考虑 `sCode = 0` 的成功请求。  

每日 08:00 UTC，系统将根据UTC时间 00:00 的数据快照，选取子账户成交比率及母账户合计成交比率中的较大值决定子账户的未来限速。详情请见下表。对于独立经纪商，系统只会取子账户的成交比率。

| 成交比率[x<=比率<y) | 子账户每2秒限速(新订单及修改订单请求)  
---|---|---  
Tier 1 | [0,1) | 1,000  
Tier 2 | [1,2) | 1,250  
Tier 3 | [2,3) | 1,500  
Tier 4 | [3,5) | 1,750  
Tier 5 | [5,10) | 2,000  
Tier 6 | [10,20) | 2,500  
Tier 7 | [20,50) | 3,000  
Tier 8 | >= 50 | 10,000  
  
若成交比率和预期限速有所改善，则提升将于 08:00 (UTC) 立即生效。但若成交比率下降，需要降低未来限速，系统将给予一天的宽限期，降低后的速率限制将在 T+1 08:00 (UTC) 实施。在 T+1 时，若成交比率提高，则将立即授予更高的限速。若用户的交易手续费等级降级为 VIP4，其限速将降低为最低档位，并有一天的宽限期。

  

若子账户7日交易量低于1,000,000 USDT，则按照母账户的合计成交比率实施限速。

  

对于新创建的子账户，创建时将应用最低档位限速，在 T+1 08:00 (UTC)时，将开始应用上述限速规则。

  

大宗交易、价差交易、做市商保护（MMP）以及币币、币币杠杆订单不受子账户限速限制。

  

交易所提供 [GET / 获取账户限速](/docs-v5/zh/#order-book-trading-trade-get-account-rate-limit) 接口以便用户查询成交比率以及限速数据，数据将于每天 08:00 (UTC) 更新。该接口将返回子账户成交比率，母账户合计成交比率，子账户当前限速以及 T+1 时的预期子账户限速（适用于限速降级）。

  

成交比率、限速计算样例如下。用户有三个账户，交易产品 BTC-USDT-SWAP 及 XRP-USDT 的乘数分别为1，0.1。

  1. 账户 A（母账户）： 
     1. BTC-USDT-SWAP 交易量为100 USDT，订单数量为10;
     2. XRP-USDT 交易量为20 USDT，订单数量为15;
     3. 子账户成交比率 = (100+20) / (10 * 1 + 15 * 0.1) = 10.4
  2. 账户 B (子账户)： 
     1. BTC-USDT-SWAP 交易量为200 USDT，订单数量为100;
     2. XRP-USDT 交易量为20 USDT，订单数量为30;
     3. 子账户成交比率 = (200+20) / (100 * 1 + 30 * 0.1) = 2.13
  3. 账户 C (子账户)： 
     1. BTC-USDT-SWAP 交易量为300 USDT，订单数量为100;
     2. XRP-USDT 交易量为20 USDT，订单数量为45;
     3. 子账户成交比率 = (300+20) / (100 * 1 + 45 * 0.1) = 3.06
  4. 母账户合计成交比率 = (100+20+200+20+300+20) / (10 * 1 + 15 * 0.1 + 100 * 1 + 30 * 0.1 + 100 * 1 + 45 * 0.1) = 3.01
  5. 账户限速 
     1. 账户 A = max(10.4, 3.01) = 10.4 -> 2500订单请求/2秒
     2. 账户 B = max(2.13, 3.01) = 3.01 -> 1750订单请求/2秒
     3. 账户 C = max(3.06, 3.01) = 3.06 -> 1750订单请求/2秒

### 最佳实践 

如果您需要的请求速率高于我们的限速，您可以设置不同的子账户来批量请求限速。 我们建议使用此方法来限制或间隔请求，以最大化每个帐户的限速并避免断开连接或拒绝请求。

## 做市商申请 

满足以下任意条件的用户即可申请加入欧易做市商计划：

  * 交易等级VIP2及以上  

  * 其他交易所达标做市商（需审核）  

感兴趣的各方可以通过邮箱联系我们：`Institutional@okx.com`  

为鼓励做市商为平台提供更好的流动性，可以享受更优的交易手续费，同时也承担相应的做市责任。具体做市责任及手续费申请成功后提供相关资料。

欧易保留对做市商项目的最终解释权  做市商项目不支持VIP、交易量相关活动以及任何形式的返佣活动 

## 经纪商申请 

如果您的业务平台提供数字货币服务，您就可以申请加入欧易经纪商项目，成为欧易的经纪商合作伙伴，享受专属的经纪商服务，并通过用户在欧易产生的交易手续费赚取高额返佣。  
经纪商业务包含且不限：聚合交易平台、交易机器人、跟单平台、交易策略提供方、量化策略机构、资管平台等。  

  * [点击申请](/cn/broker/home)
  * [经纪商规则介绍](/cn/help/introduction-of-rules-on-okx-brokers)
  * 如有问题请咨询线上客服

具体经纪商业务文档及产品服务在申请成功后提供相关资料。