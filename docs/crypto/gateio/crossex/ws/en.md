---
exchange: gateio
source_url: https://www.gate.com/docs/developers/crossex/ws/en
api_type: WebSocket
updated_at: 2026-05-27 20:18:22.354879
---

# CrossEx WebSocket v1.0.0

* Python 
  * Shell 

v1.0.0 · Stable


CrossEx provides a simple and powerful Websocket API to integrate trading status into your business or application.

##  Server URL

  * Production: 
    * Public Market: wss://api.gateio.ws/ws/crossex/public
    * Private Push: wss://api.gateio.ws/ws/crossex
  * Heartbeat: Clients must send a **protocol-level** Ping frame to the WebSocket server every 30 seconds to maintain the connection. If the server does not receive this frame for more than 30 seconds, it will automatically disconnect.
  * Connection limit: Maximum 20 connections per uid+channel

##  Changelog

**Mar 24 2026**

  1. Added Ticker subscription channel (ticker) for spot/futures ticker updates from major exchanges
  2. Added Public Trade subscription channel (trade) for tick-by-tick trade updates from major exchanges
  3. Added Kline subscription channel (kline_x) supporting multiple intervals: 1m/5m/15m/30m/1h/4h/1d
  4. Added Futures Funding Rate subscription channel (funding_rate) for futures funding rate updates
  5. Added Futures Open Interest subscription channel (open_interest) for futures open interest updates (excluding BINANCE)

**Mar 12 2026**

  1. CrossEx adds support for BYBIT exchange

**Feb 27 2026**

  1. Added public market data push, including last trade price, index price, mark price
  2. Added incremental order book depth and full order book depth subscriptions

**Jan 21 2026**

  1. Added channel for complete position closing
  2. Added connection limit description
  3. Added rate limit descriptions for all APIs

**Jan 19 2026**

  1. Added margin position subscription/unsubscription
  2. Added margin interest subscription/unsubscription
  3. Added modify spot margin leverage

##  Websocket API Overview

###  Events

Each common channel (e.g., order, asset, etc.) supports 2 different event messages:

  1. **`subscribe`** (**Recommended**)

Subscribe to receive new data pushes from the server.

  2. **`unsubscribe`**

If unsubscribed, the server will not send new data pushes.

###  Request Parameters

Each request follows a common format containing `time`, `channel`, `event` and `payload`.

Request ParametersName | Type | Required | Description  
---|---|---|---  
`time` | Integer | Optional | Request time  
`channel` | String | Optional | Request subscribe/unsubscribe channel  
`auth` | Object | Optional | Request authentication information, see Authentication section for details  
`event` | String | Optional | Request event (subscribe/unsubscribe/api/login)  
`payload` | Array/Object | Optional | Request detailed parameters  
  
###  Push Parameters

Similar to requests, push parameters follow the following common format containing: `time`, `channel`, `event`, `error` and `result`.

Push ParametersName | Type | Required | Description  
---|---|---|---  
`time` | Integer | Optional | Push time  
`channel` | String | Optional | Push channel  
`event` | String | Optional | Push channel event (subscribe/update)  
`error` | Object | Optional | Push error  
`result` | Any | Optional | Returns new data notification from the server or response to client request. If there is an error, `error` is not empty, otherwise this field is empty.  
  
Note: If it is a data update notification initiated by the server, then the type of `result` is based on the channel, and the `result` type varies for different channels.

But if it is a response to a client subscription request, then `result` is fixed as `{"code": "100000", "message": "success"}`. To verify whether the subscription request is successful, you only need to check whether the `error` field is empty, and you don't need to parse the `result` field.

For simplicity, the channel descriptions below only give the payload format for the corresponding channel.

###  Errors

If an error occurs, you will receive an error field containing the error code and error type.

ErrorsCode | Message  
---|---  
`100001` | `Parameter missing or invalid`  
`100002` | `Not logged in`  
`100003` | `Connection limit reached`  
`100004` | `Timeout`  
`100005` | `Operation failed`  
`100006` | `Login failed`  
`100007` | `Network error, please try again later`  
  
##  Authentication

WARNING

Note: The GateAPIv4 key pair you use must have at least CrossEx read permissions enabled. If IP whitelisting is enabled for the key, your outbound IP address must be in the key's IP whitelist.

If the channel is private, for example, the client request needs to carry authentication information. For example: the `order` channel to retrieve user order updates.

Authentication is sent through the `payload` field in the request body, formatted as follows:

Name | Type | Description  
---|---|---  
`method` | String | Authentication method: `api_key`  
`api_key` | String | apiKey value  
`sign` | String | Signature result  
  
WebSocket authentication uses the same signature calculation method as Gate APIv4 API, i.e. `HexEncode(HMAC_SHA512(secret, signature_string))`, but with the following differences:

  1. Signature string concatenation method: `channel=<channel>&event=<event>&time=<time>`, where `<channel>`, `<event>`, `<time>` correspond to the request information
  2. Authentication information is sent in the `payload` field of the request body.

You can log in to your account to obtain the api_key and secret for your CrossEx account.
    
    
    # example WebSocket signature calculation implementation in Python
    import hmac, hashlib, json, time
    
    
    def gen_sign(channel, event, timestamp):
        # GateAPIv4 key pair
        api_key = 'YOUR_API_KEY'
        api_secret = 'YOUR_API_SECRET'
    
        s = 'channel=%s&event=%s&time=%d' % (channel, event, timestamp)
        sign = hmac.new(api_secret.encode('utf-8'), s.encode('utf-8'), hashlib.sha512).hexdigest()
        return {'method': 'api_key', 'api_key': api_key, 'sign': sign}
    
    
    request = {
        'time': int(time.time()),
        'event': 'login',
        'payload': {
            'method': 'api_key',
            'api_key': 'YOUR_API_KEY',
            'sign': gen_sign('', 'login', int(time.time()))['sign']
        }
    }
    print(json.dumps(request))
    

#  Authentication

**» event** : login

**» method** : api_key

##  Request Parameters

Request ParametersName | Location | Type | Required | Description  
---|---|---|---|---  
↳ time | body | integer | Optional | Timestamp (seconds)  
↳ event | body | string | Optional | Event login  
↳ payload | body | object | Optional | none  
↳ method | body | string | Optional | Authentication method  
↳ api_key | body | string | Optional | api key  
↳ sign | body | string | Optional | Signature  
  
##  Response Data Structure

Response Data StructureName | Type | Required | Constraint | Description  
---|---|---|---|---  
↳ event | string | Required | none | Event  
api  
↳ payload | object | Required | none | none  
↳ conn_id | string | Required | none | Connection ID  
↳ result | object | Required | none | Login result  
↳ code | string | Required | none | Response code  
↳ message | string | Required | none | Response message  
↳ time | integer | Required | none | Timestamp (seconds)  
↳ time_ms | integer | Required | none | Timestamp (milliseconds)  
  
Request example
    
    
    {
    	"time": 1754272114,
    	"event": "login",
    	"payload": {
    		"method": "api_key",
    		"api_key": "0d5245a5d8be8ac0e96ed8aaa47386cf",
    		"sign": "568e694ebf998fc0e9a26ab26c8cb962d8649fd61fbfc61f068251ae8169f00066b3205bb2491c1625e111f18c4bf1e6bcf8d3fd519eaea8b7335edea960eee2"
    	}
    }
    

Response example
    
    
    {
      "event": "login",
      "payload": {
        "conn_id": "644ff57f-add4-407a-97aa-b654c4ede839"
      },
      "result": {
        "code": "100000",
        "message": "success"
      },
      "time": 1756434168,
      "time_ms": 1756434168928
    }
    

#  Last Price Subscription

`last_price`

The last price channel provides real-time last trade price updates from major exchanges for spot/margin and futures trading pairs.

**Push Type** : `continuous`

**Update Frequency** : `real-time`

##  Client Subscription

##  Request Parameters

Request ParametersName | Location | Type | Required | Description  
---|---|---|---|---  
↳ time | body | integer | Optional | Timestamp (seconds)  
↳ event | body | string | Optional | Event  
↳ channel | body | string | Optional | Channel name  
↳ payload | body | [string] | Optional | Subscribe/Unsubscribe trading pairs, subscribe all not supported  
  
###  Details

**» event** : subscribe、unsubscribe

**» channel** : last_price

Payload format:

DetailsName | Type | Required | Description  
---|---|---|---  
`payload` | `Array[String]` | Optional | Trading pair list  
  
You can subscribe/unsubscribe multiple times. Trading pairs subscribed earlier will not be overridden unless explicitly unsubscribed to.

WARNING

No authentication required

Request example
    
    
    {
       "time": 1754272114,
       "event": "subscribe",
       "channel": "last_price",
       "payload": [
          "BINANCE_SPOT_BTC_USDT",
          "OKX_FUTURE_BTC_USDT",
          "GATE_FUTURE_ETH_USDT"
       ]
    }
    

##  Server Push

Push parameters:

Name | Type | Required | Constraint | Description | Note  
---|---|---|---|---|---  
↳ channel | string | Required | none | Channel name | none  
↳ event | string | Required | none | Event | none  
↳ result | object | Required | none | Result | none  
↳ s | string | Required | none | Trading pair | Symbol  
↳ lp | string | Required | none | Last price | LastPrice  
  
Push example
    
    
    {
       "time": 1771988975,
       "channel": "last_price",
       "event": "update",
       "result": {
          "s": "BINANCE_SPOT_BTC_USDT",
          "lp": "65873.49000000"
       },
       "time_ms": 1771988975033
    }
    
    
    
    {
       "time": 1771988975,
       "channel": "last_price",
       "event": "update",
       "result": {
          "s": "OKX_FUTURE_BTC_USDT",
          "lp": "65843.3"
       },
       "time_ms": 1771988975120
    }
    
    
    
    {
       "time": 1771988978,
       "channel": "last_price",
       "event": "update",
       "result": {
          "s": "GATE_FUTURE_ETH_USDT",
          "lp": "1918.01"
       },
       "time_ms": 1771988978067
    }
    

#  Index Price Subscription

`index_price`

The index price channel provides real-time index price updates from major exchanges for spot margin trading pairs.

**Push Type** : `continuous`

**Update Frequency** : `real-time`

##  Client Subscription

##  Request Parameters

Request ParametersName | Location | Type | Required | Description  
---|---|---|---|---  
↳ time | body | integer | Optional | Timestamp (seconds)  
↳ event | body | string | Optional | Event  
↳ channel | body | string | Optional | Channel name  
↳ payload | body | [string] | Optional | Subscribe/Unsubscribe trading pairs, subscribe all not supported  
  
###  Details

**» event** : subscribe、unsubscribe

**» channel** : index_price

Payload format:

DetailsName | Type | Required | Description  
---|---|---|---  
`payload` | `Array[String]` | Optional | Trading pair list  
  
You can subscribe/unsubscribe multiple times. Trading pairs subscribed earlier will not be overridden unless explicitly unsubscribed to.

WARNING

No authentication required

Request example
    
    
    {
       "time": 1754272114,
       "event": "subscribe",
       "channel": "index_price",
       "payload": [
          "BINANCE_MARGIN_BTC_USDT",
          "OKX_MARGIN_BTC_USDT",
          "GATE_MARGIN_ETH_USDT"
       ]
    }
    

##  Server Push

Push parameters:

Name | Type | Required | Constraint | Description | Note  
---|---|---|---|---|---  
↳ channel | string | Required | none | Channel name | none  
↳ event | string | Required | none | Event | none  
↳ result | object | Required | none | Result | none  
↳ s | string | Required | none | Trading pair | Symbol  
↳ ip | string | Required | none | Index price | IndexPrice  
  
Push example
    
    
    {
       "time": 1771990104,
       "channel": "index_price",
       "event": "update",
       "result": {
          "s": "BINANCE_MARGIN_BTC_USDT",
          "ip": "65590.40739130"
       },
       "time_ms": 1771990104116
    }
    
    
    
    {
       "time": 1771990103,
       "channel": "index_price",
       "event": "update",
       "result": {
          "s": "OKX_MARGIN_BTC_USDT",
          "ip": "65591.5"
       },
       "time_ms": 1771990103520
    }
    
    
    
    {
       "time": 1771990106,
       "channel": "index_price",
       "event": "update",
       "result": {
          "s": "GATE_MARGIN_BTC_USDT",
          "ip": "65589.9"
       },
       "time_ms": 1771990106074
    }
    

#  Mark Price Subscription

`mark_price`

The mark price channel provides real-time mark price updates from major exchanges for spot margin trading pairs.

**Push Type** : `continuous`

**Update Frequency** : `real-time`

##  Client Subscription

##  Request Parameters

Request ParametersName | Location | Type | Required | Description  
---|---|---|---|---  
↳ time | body | integer | Optional | Timestamp (seconds)  
↳ event | body | string | Optional | Event  
↳ channel | body | string | Optional | Channel name  
↳ payload | body | [string] | Optional | Subscribe/Unsubscribe trading pairs, subscribe all not supported  
  
###  Details

**» event** : subscribe、unsubscribe

**» channel** : mark_price

Payload format:

DetailsName | Type | Required | Description  
---|---|---|---  
`payload` | `Array[String]` | Optional | Trading pair list  
  
You can subscribe/unsubscribe multiple times. Trading pairs subscribed earlier will not be overridden unless explicitly unsubscribed to.

WARNING

No authentication required

Request example
    
    
    {
       "time": 1754272114,
       "event": "subscribe",
       "channel": "mark_price",
       "payload": [
          "BINANCE_FUTURE_BTC_USDT",
          "OKX_FUTURE_BTC_USDT",
          "GATE_FUTURE_ETH_USDT"
       ]
    }
    

##  Server Push

Push parameters:

Name | Type | Required | Constraint | Description | Note  
---|---|---|---|---|---  
↳ channel | string | Required | none | Channel name | none  
↳ event | string | Required | none | Event | none  
↳ result | object | Required | none | Result | none  
↳ s | string | Required | none | Trading pair | Symbol  
↳ mp | string | Required | none | Mark price | MarkPrice  
  
Push example
    
    
    {
       "time": 1771990349,
       "channel": "mark_price",
       "event": "update",
       "result": {
          "s": "BINANCE_FUTURE_BTC_USDT",
          "mp": "65566.30000000"
       },
       "time_ms": 1771990349113
    }
    
    
    
    {
       "time": 1771990348,
       "channel": "mark_price",
       "event": "update",
       "result": {
          "s": "OKX_FUTURE_BTC_USDT",
          "mp": "65562.8"
       },
       "time_ms": 1771990348142
    }
    
    
    
    {
       "time": 1771990349,
       "channel": "mark_price",
       "event": "update",
       "result": {
          "s": "GATE_FUTURE_ETH_USDT",
          "mp": "1908.90"
       },
       "time_ms": 1771990349066
    }
    

#  Full Limited-Level Order Book Subscription

`order_book_x`

  * BINANCE: [5, 10, 20]
  * OKX: [1, 5]
  * GATE: 
    * SPOT: [5, 10, 20, 30, 50, 100]
    * FUTURE: [1, 5, 10, 20, 50, 100]

The order book channel provides full limited-level order book depth push from major exchanges for spot/futures trading pairs.

**Push Type** : `continuous`

**Update Frequency** : `real-time`

##  Client Subscription

##  Request Parameters

Request ParametersName | Location | Type | Required | Description  
---|---|---|---|---  
↳ time | body | integer | Optional | Timestamp (seconds)  
↳ event | body | string | Optional | Event  
↳ channel | body | string | Optional | Channel name  
↳ payload | body | [string] | Optional | Subscribe/Unsubscribe trading pairs, subscribe all not supported  
  
###  Details

**» event** : subscribe、unsubscribe

**» channel** : order_book_x

Payload format:

DetailsName | Type | Required | Description  
---|---|---|---  
`payload` | `Array[String]` | Optional | Trading pair list  
  
You can subscribe/unsubscribe multiple times. Trading pairs subscribed earlier will not be overridden unless explicitly unsubscribed to.

WARNING

No authentication required

Request example
    
    
    {
       "time": 1754272114,
       "event": "subscribe",
       "channel": "order_book_5",
       "payload": [
          "BINANCE_SPOT_BTC_USDT",
          "OKX_FUTURE_BTC_USDT",
          "GATE_FUTURE_ETH_USDT"
       ]
    }
    

##  Server Push

Push parameters:

Name | Type | Required | Constraint | Description | Note  
---|---|---|---|---|---  
↳ channel | string | Required | none | Channel name | none  
↳ event | string | Required | none | Event | none  
↳ result | object | Required | none | Result | none  
↳ ts | long | Required | none | Millisecond timestamp | Timestamp  
↳ s | string | Required | none | Trading pair | Symbol  
↳ a | array | Required | none | Ask depth | [Price,Qty]  
↳ b | array | Required | none | Bid depth | [Price,Qty]  
  
Push example
    
    
    {
       "time": 1771990690,
       "channel": "order_book_5",
       "event": "update",
       "result": {
          "ts": 1771990690844,
          "s": "BINANCE_SPOT_BTC_USDT",
          "a": [
             [
                "65485.33000000",
                "2.25708000"
             ],
             [
                "65485.34000000",
                "0.00025000"
             ],
             [
                "65485.38000000",
                "0.15432000"
             ],
             [
                "65485.39000000",
                "0.50423000"
             ],
             [
                "65486.26000000",
                "0.00208000"
             ]
          ],
          "b": [
             [
                "65485.32000000",
                "0.04107000"
             ],
             [
                "65485.31000000",
                "0.00097000"
             ],
             [
                "65485.20000000",
                "0.00008000"
             ],
             [
                "65485.10000000",
                "0.00018000"
             ],
             [
                "65484.99000000",
                "0.00045000"
             ]
          ]
       },
       "time_ms": 1771990690844
    }
    
    
    
    {
       "time": 1771990690,
       "channel": "order_book_5",
       "event": "update",
       "result": {
          "ts": 1771990690900,
          "s": "OKX_FUTURE_BTC_USDT",
          "a": [
             [
                "65457.1",
                "997.61"
             ],
             [
                "65457.2",
                "0.01"
             ],
             [
                "65458",
                "0.01"
             ],
             [
                "65458.1",
                "106.34"
             ],
             [
                "65458.4",
                "0.01"
             ]
          ],
          "b": [
             [
                "65457",
                "121.04"
             ],
             [
                "65456.9",
                "0.03"
             ],
             [
                "65456.8",
                "0.01"
             ],
             [
                "65456",
                "0.01"
             ],
             [
                "65455.9",
                "0.01"
             ]
          ]
       },
       "time_ms": 1771990690905
    }
    
    
    
    {
       "time": 1771990690,
       "channel": "order_book_5",
       "event": "update",
       "result": {
          "ts": 1771990690848,
          "s": "GATE_FUTURE_ETH_USDT",
          "a": [
             [
                "1906.86",
                "3638"
             ],
             [
                "1907.01",
                "99"
             ],
             [
                "1907.05",
                "194"
             ],
             [
                "1907.1",
                "1686"
             ],
             [
                "1907.11",
                "5098"
             ]
          ],
          "b": [
             [
                "1906.85",
                "7139"
             ],
             [
                "1906.8",
                "1"
             ],
             [
                "1906.79",
                "3382"
             ],
             [
                "1906.7",
                "43"
             ],
             [
                "1906.65",
                "74"
             ]
          ]
       },
       "time_ms": 1771990690887
    }
    

#  Incremental Order Book Subscription

`order_book_update`

The incremental order book channel provides real-time order book depth updates from major exchanges for spot/futures trading pairs.

**Push Type** : `continuous`

**Update Frequency** : `real-time`

##  Client Subscription

##  Request Parameters

Request ParametersName | Location | Type | Required | Description  
---|---|---|---|---  
↳ time | body | integer | Optional | Timestamp (seconds)  
↳ event | body | string | Optional | Event  
↳ channel | body | string | Optional | Channel name  
↳ payload | body | [string] | Optional | Subscribe/Unsubscribe trading pairs, subscribe all not supported  
  
###  Details

**» event** : subscribe、unsubscribe

**» channel** : order_book_update

Payload format:

DetailsName | Type | Required | Description  
---|---|---|---  
`payload` | `Array[String]` | Optional | Trading pair list  
  
You can subscribe/unsubscribe multiple times. Trading pairs subscribed earlier will not be overridden unless explicitly unsubscribed to.

WARNING

No authentication required

Request example
    
    
    {
       "time": 1754272114,
       "event": "subscribe",
       "channel": "order_book_update",
       "payload": [
          "BINANCE_FUTURE_BTC_USDT",
          "OKX_FUTURE_BTC_USDT",
          "GATE_FUTURE_ETH_USDT"
       ]
    }
    

##  Server Push

Push parameters:

Name | Type | Required | Constraint | Description | Note  
---|---|---|---|---|---  
↳ channel | string | Required | none | Channel name | none  
↳ event | string | Required | none | Event | none  
↳ result | object | Required | none | Result | none  
↳ snapshot | boolean | Required | none | Whether it is a snapshot (yes for full override, otherwise incremental update) | Snapshot  
↳ ts | long | Required | none | Millisecond timestamp | Timestamp  
↳ s | string | Required | none | Trading pair | Symbol  
↳ U | string | Required | none | Start sequence number | StartIndex  
↳ u | string | Required | none | End sequence number | EndIndex  
↳ a | array | Required | none | Ask depth | [Price,Qty]  
↳ b | array | Required | none | Bid depth | [Price,Qty]  
  
Push example
    
    
    {
       "time": 1771991193,
       "channel": "order_book_update",
       "event": "update",
       "result": {
          "snapshot": false,
          "ts": 1771991193314,
          "s": "BINANCE_FUTURE_BTC_USDT",
          "U": 88686516370,
          "u": 88686516769,
          "a": [
             [
                "65475.36000000",
                "0.00000000"
             ],
             [
                "65475.37000000",
                "0.00000000"
             ]
          ],
          "b": [
             [
                "65479.75000000",
                "0.96961000"
             ],
             [
                "65478.71000000",
                "0.03395000"
             ]
          ]
       },
       "time_ms": 1771991193344
    }
    
    
    
    {
       "time": 1771991192,
       "channel": "order_book_update",
       "event": "update",
       "result": {
          "snapshot": false,
          "ts": 1771991192200,
          "s": "OKX_FUTURE_BTC_USDT",
          "U": 298872114996,
          "u": 298872115067,
          "a": [
             [
                "65458.8",
                "692.41"
             ],
             [
                "65463.4",
                "0.3"
             ],
             [
                "65464.9",
                "28.64"
             ],
             [
                "65465",
                "0"
             ],
             [
                "65466.4",
                "0"
             ],
             [
                "65466.9",
                "29.57"
             ],
             [
                "65468",
                "4.98"
             ],
             [
                "65471.5",
                "0.37"
             ],
             [
                "65479.2",
                "0.29"
             ],
             [
                "65483.8",
                "0.05"
             ],
             [
                "65492.6",
                "0.02"
             ],
             [
                "65503.8",
                "0.02"
             ],
             [
                "65510.1",
                "0"
             ]
          ],
          "b": [
             [
                "65458.7",
                "174.61"
             ],
             [
                "65449.5",
                "2.3"
             ],
             [
                "65448.6",
                "99.61"
             ],
             [
                "65444.9",
                "0.33"
             ],
             [
                "65432.6",
                "29.59"
             ],
             [
                "65432.3",
                "15.6"
             ],
             [
                "65431.4",
                "0"
             ],
             [
                "65431.3",
                "2.62"
             ],
             [
                "65429.9",
                "91.78"
             ],
             [
                "65427.3",
                "1.34"
             ],
             [
                "65426.7",
                "0.01"
             ],
             [
                "65417.8",
                "0"
             ],
             [
                "65417.1",
                "14.87"
             ],
             [
                "65411.8",
                "0.01"
             ],
             [
                "65403",
                "0"
             ],
             [
                "65402.9",
                "0.04"
             ],
             [
                "65402.4",
                "23.4"
             ],
             [
                "65402.2",
                "2"
             ],
             [
                "65398.8",
                "0"
             ],
             [
                "65398.7",
                "28.46"
             ],
             [
                "65398.5",
                "36.71"
             ]
          ]
       },
       "time_ms": 1771991192205
    }
    
    
    
    {
       "time": 1771991192,
       "channel": "order_book_update",
       "event": "update",
       "result": {
          "snapshot": false,
          "ts": 1771991192182,
          "s": "GATE_FUTURE_ETH_USDT",
          "U": 89944768993,
          "u": 89944768950,
          "a": [
             [
                "1907.56",
                "10757"
             ],
             [
                "1907.61",
                "2"
             ],
             [
                "1907.66",
                "74"
             ],
             [
                "1907.91",
                "522"
             ],
             [
                "1908",
                "194"
             ],
             [
                "1911.35",
                "5174"
             ],
             [
                "1911.36",
                "2"
             ],
             [
                "1915.34",
                "1"
             ],
             [
                "1915.35",
                "18"
             ],
             [
                "1907.78",
                "0"
             ],
             [
                "1907.93",
                "0"
             ],
             [
                "1907.97",
                "0"
             ],
             [
                "1911.37",
                "0"
             ]
          ],
          "b": [
             [
                "1906.95",
                "393"
             ],
             [
                "1906.6",
                "160"
             ],
             [
                "1898.01",
                "12"
             ],
             [
                "1906.67",
                "0"
             ]
          ]
       },
       "time_ms": 1771991192213
    }
    

#  Ticker Subscription

`ticker`

The ticker channel provides ticker updates for spot/futures markets from major exchanges

**Push Type** : `continuous`

**Update Frequency** : `real-time`

##  Client Subscription

##  Request Parameters

Request ParametersName | Location | Type | Required | Description  
---|---|---|---|---  
↳ time | body | integer | Optional | Timestamp (seconds)  
↳ event | body | string | Optional | Event  
↳ channel | body | string | Optional | Channel name  
↳ payload | body | [string] | Optional | Subscribe/Unsubscribe trading pairs, subscription to all is not supported yet  
  
###  Details

**» event** : subscribe, unsubscribe

**» channel** : ticker

Format:

DetailsName | Type | Required | Description  
---|---|---|---  
`payload` | `Array[String]` | Optional | Trading pair list  
  
You can subscribe/unsubscribe multiple times. Trading pairs subscribed earlier will not be overridden unless explicitly unsubscribed to.

WARNING

No authentication required

Request example
    
    
    {
      "event": "subscribe",
      "channel": "ticker",
      "payload": [
        "BINANCE_FUTURE_BTC_USDT"
      ]
    }
    

##  Server Push

Push parameters:

Name | Type | Required | Constraint | Description | Remarks  
---|---|---|---|---|---  
↳ channel | string | Required | none | Channel name | none  
↳ event | string | Required | none | Event | none  
↳ result | object | Required | none | Result | none  
↳ s | string | Required | none | Trading pair | Symbol  
↳ lp | string | Required | none | Latest trade price | LastPrice  
↳ bp | string | Required | none | Best bid price | BidPrice  
↳ bs | string | Required | none | Best bid size | BidSize  
↳ ap | string | Required | none | Best ask price | AskPrice  
↳ as | string | Required | none | Best ask size | AskSize  
↳ o | string | Required | none | 24h open price | Open24h  
↳ h | string | Required | none | 24h high price | High24h  
↳ l | string | Required | none | 24h low price | Low24h  
↳ v | string | Required | none | 24h volume (base) | Volume24h  
↳ q | string | Optional | none | 24h volume (quote) | QuoteVolume24h  
↳ ts | long | Required | none | Exchange timestamp (milliseconds) | Timestamp  
  
Push example
    
    
    {
      "time": 1770709567,
      "channel": "ticker",
      "event": "update",
      "result": {
        "s": "BINANCE_FUTURE_BTC_USDT",
        "lp": "67280.50",
        "bp": "67280.20",
        "bs": "35",
        "ap": "67280.70",
        "as": "28",
        "o": "69100.00",
        "h": "69100.00",
        "l": "66000.00",
        "v": "825432",
        "q": "5523487123.55",
        "ts": 1710001234567
      },
      "time_ms": 1770709567032
    }
    

#  Public Trade Subscription

`trade`

The trade channel provides tick-by-tick public trade updates for spot/futures markets from major exchanges

**Push Type** : `continuous`

**Update Frequency** : `real-time`

##  Client Subscription

##  Request Parameters

Request ParametersName | Location | Type | Required | Description  
---|---|---|---|---  
↳ time | body | integer | Optional | Timestamp (seconds)  
↳ event | body | string | Optional | Event  
↳ channel | body | string | Optional | Channel name  
↳ payload | body | [string] | Optional | Subscribe/Unsubscribe trading pairs, subscription to all is not supported yet  
  
###  Details

**» event** : subscribe, unsubscribe

**» channel** : trade

Format:

DetailsName | Type | Required | Description  
---|---|---|---  
`payload` | `Array[String]` | Optional | Trading pair list  
  
You can subscribe/unsubscribe multiple times. Trading pairs subscribed earlier will not be overridden unless explicitly unsubscribed to.

WARNING

No authentication required

Request example
    
    
    {
      "event": "subscribe",
      "channel": "trade",
      "payload": [
        "BINANCE_FUTURE_BTC_USDT"
      ]
    }
    

##  Server Push

Push parameters:

Name | Type | Required | Constraint | Description | Remarks  
---|---|---|---|---|---  
↳ channel | string | Required | none | Channel name | none  
↳ event | string | Required | none | Event | none  
↳ result | object | Required | none | Result | none  
↳ s | string | Required | none | Trading pair | Symbol  
↳ i | string | Required | none | Trade ID (exchange raw format) | TradeId  
↳ p | string | Required | none | Trade price | Price  
↳ q | string | Required | none | Trade quantity (base) | Quantity  
↳ S | string | Required | none | Side | BUY/SELL  
↳ ts | long | Required | none | Exchange timestamp (milliseconds) | Timestamp  
  
Push example
    
    
    {
      "time": 1770709567,
      "channel": "trade",
      "event": "update",
      "result": {
        "s": "BTCUSDT",
        "i": "18473628192",
        "p": "67250.12",
        "q": "0.015",
        "S": "BUY",
        "ts": 1710001234567,
        "m": false
      },
      "time_ms": 1770709567032
    }
    

#  Kline Subscription

`kline_x`

  * kline_1m,kline_5m,kline_15m,kline_30m,kline_1h,kline_4h,kline_1d;

The kline channel provides kline updates for spot/futures markets from major exchanges

**Push Type** : `continuous`

**Update Frequency** : `real-time`

##  Client Subscription

##  Request Parameters

Request ParametersName | Location | Type | Required | Description  
---|---|---|---|---  
↳ time | body | integer | Optional | Timestamp (seconds)  
↳ event | body | string | Optional | Event  
↳ channel | body | string | Optional | Channel name  
↳ payload | body | [string] | Optional | Subscribe/Unsubscribe trading pairs, subscription to all is not supported yet  
  
###  Details

**» event** : subscribe, unsubscribe

**» channel** : kline

Format:

DetailsName | Type | Required | Description  
---|---|---|---  
`payload` | `Array[String]` | Optional | Trading pair list  
  
You can subscribe/unsubscribe multiple times. Trading pairs subscribed earlier will not be overridden unless explicitly unsubscribed to.

WARNING

No authentication required

Request example
    
    
    {
      "channel": "kline_1m",
      "event": "subscribe",
      "payload": ["BYBIT_FUTURE_BTC_USDT", "BINANCE_FUTURE_ETH_USDT"]
    }
    

##  Server Push

Push parameters:

Name | Type | Required | Constraint | Description | Remarks  
---|---|---|---|---|---  
↳ channel | string | Required | none | Channel name | none  
↳ event | string | Required | none | Event | none  
↳ result | object | Required | none | Result | none  
↳ s | string | Required | none | Trading pair | Symbol  
↳ o | string | Required | none | Open price | OpenPrice  
↳ h | string | Required | none | High price | HighPrice  
↳ l | string | Required | none | Low price | LowPrice  
↳ c | string | Required | none | Close price | ClosePrice  
↳ v | string | Required | none | Volume | Volume  
↳ t | long | Required | none | Kline start time (milliseconds) | StartTime  
↳ T | long | Required | none | Kline end time (milliseconds) | EndTime  
↳ x | boolean | Required | none | Is kline closed (0: in progress, 1: closed) | Confirm  
  
Push example
    
    
    {
      "channel": "kline_1m",
      "event": "update",
      "result": {
        "s": "BYBIT_FUTURE_BTC_USDT",
        "o": "95000",
        "h": "95100",
        "l": "94900",
        "c": "95050",
        "v": "1234.5",
        "t": 1710000000000,
        "T": 1710000059999,
        "x": true
      }
    }
    

#  Futures Funding Rate Subscription

`funding_rate`

The funding_rate channel provides funding rate updates for futures markets from major exchanges

**Push Type** : `continuous`

**Update Frequency** : `real-time`

##  Client Subscription

##  Request Parameters

Request ParametersName | Location | Type | Required | Description  
---|---|---|---|---  
↳ time | body | integer | Optional | Timestamp (seconds)  
↳ event | body | string | Optional | Event  
↳ channel | body | string | Optional | Channel name  
↳ payload | body | [string] | Optional | Subscribe/Unsubscribe trading pairs, subscription to all is not supported yet  
  
###  Details

**» event** : subscribe, unsubscribe

**» channel** : funding_rate

Format:

DetailsName | Type | Required | Description  
---|---|---|---  
`payload` | `Array[String]` | Optional | Trading pair list  
  
You can subscribe/unsubscribe multiple times. Trading pairs subscribed earlier will not be overridden unless explicitly unsubscribed to.

WARNING

No authentication required

Request example
    
    
    {
      "event": "subscribe",
      "channel": "funding_rate",
      "payload": [
        "BINANCE_FUTURE_BTC_USDT"
      ]
    }
    

##  Server Push

Push parameters:

Name | Type | Required | Constraint | Description | Remarks  
---|---|---|---|---|---  
↳ channel | string | Required | none | Channel name | none  
↳ event | string | Required | none | Event | none  
↳ result | object | Required | none | Result | none  
↳ s | string | Required | none | Trading pair | Symbol  
↳ r | string | Required | none | Current funding rate | FundingRate  
↳ T | long | Required | none | Next funding time (milliseconds) | NextFundingTime  
  
Push example
    
    
    {
      "time": 1773382659,
      "channel": "funding_rate",
      "event": "update",
      "result": {
        "s": "BINANCE_FUTURE_BTC_USDT",
        "r": "0.00002534",
        "T": 1773388800000
      },
      "time_ms": 1773382659999
    }
    

#  Futures Open Interest Subscription

`open_interest`

The open_interest channel provides open interest updates for futures markets from major exchanges (excluding BINANCE)

**Push Type** : `continuous`

**Update Frequency** : `real-time`

##  Client Subscription

##  Request Parameters

Request ParametersName | Location | Type | Required | Description  
---|---|---|---|---  
↳ time | body | integer | Optional | Timestamp (seconds)  
↳ event | body | string | Optional | Event  
↳ channel | body | string | Optional | Channel name  
↳ payload | body | [string] | Optional | Subscribe/Unsubscribe trading pairs, subscription to all is not supported yet  
  
###  Details

**» event** : subscribe, unsubscribe

**» channel** : open_interest

Format:

DetailsName | Type | Required | Description  
---|---|---|---  
`payload` | `Array[String]` | Optional | Trading pair list  
  
You can subscribe/unsubscribe multiple times. Trading pairs subscribed earlier will not be overridden unless explicitly unsubscribed to.

WARNING

No authentication required

Request example
    
    
    {
      "event": "subscribe",
      "channel": "open_interest",
      "payload": [
        "OKX_FUTURE_BTC_USDT"
      ]
    }
    

##  Server Push

Push parameters:

Name | Type | Required | Constraint | Description | Remarks  
---|---|---|---|---|---  
↳ channel | string | Required | none | Channel name | none  
↳ event | string | Required | none | Event | none  
↳ result | object | Required | none | Result | none  
↳ s | string | Required | none | Trading pair | Symbol  
↳ oi | string | Required | none | Open interest | OpenInterest  
↳ oiV | string | Optional | none | Open interest value | OpenInterestValue  
  
Push example
    
    
    {
      "time": 1773384822,
      "channel": "open_interest",
      "event": "update",
      "result": {
        "s": "OKX_FUTURE_BTC_USDT",
        "oi": "2929823.88000001813",
        "oiV": "29298.2388000001813"
      },
      "time_ms": 1773384822164
    }
    

#  Order Subscription/Unsubscription

`order`

The order channel provides a way to receive user order updates.

**Push Type** : `continuous`

**Update Frequency** : `real-time`

##  Client Subscription

##  Request Parameters

Request ParametersName | Location | Type | Required | Description  
---|---|---|---|---  
↳ time | body | integer | Optional | Timestamp (seconds)  
↳ event | body | string | Optional | Event  
↳ channel | body | string | Optional | Channel name  
↳ payload | body | [string] | Optional | Subscribe/Unsubscribe trading pairs !all means all  
  
###  Details

**» event** : subscribe、unsubscribe

**» channel** : order

Payload format:

DetailsName | Type | Required | Description  
---|---|---|---  
`payload` | `Array[String]` | Optional | Trading pair list  
  
You can subscribe/unsubscribe multiple times. Trading pairs subscribed earlier will not be overridden unless explicitly unsubscribed to.

WARNING

Authentication required

Request example
    
    
    {
      "time": 1754272114,
      "event": "subscribe",
      "channel": "order",
      "payload": [
        "GATE_FUTURE_ETH_USDT"
      ]
    }
    

##  Server Push

Push parameters:

Name | Type | Required | Constraint | Description  
---|---|---|---|---  
↳ channel | string | Required | none | Channel name  
↳ event | string | Required | none | Event  
↳ payload | object | Required | none | Data set  
↳ user_id | string | Required | none | User ID  
↳ order_id | string | Required | none | Order ID  
↳ text | string | Required | none | Customer order ID  
↳ state | string | Required | none | Order state  
↳ symbol | string | Required | none | Trading pair  
↳ side | string | Required | none | Direction  
↳ type | string | Required | none | Type  
↳ attribute | string | Required | none | Attribute  
↳ exchange_type | string | Required | none | Exchange type  
↳ business_type | string | Required | none | Business type  
↳ qty | string | Required | none | Base currency quantity  
↳ quote_qty | string | Required | none | Quote currency quantity  
↳ price | string | Required | none | Price  
↳ time_in_force | string | Required | none | Time in force strategy  
↳ executed_qty | string | Required | none | Executed quantity  
↳ executed_amount | string | Required | none | Executed amount  
↳ executed_avg_price | string | Required | none | Executed average price  
↳ fee_coin | string | Required | none | Fee coin  
↳ fee | string | Required | none | Fee  
↳ reduce_only | string | Required | none | Reduce only  
↳ leverage | string | Required | none | Leverage  
↳ reason | string | Required | none | Reason  
↳ last_executed_qty | string | Required | none | Last executed quantity  
↳ last_executed_price | string | Required | none | Last executed price  
↳ last_executed_amount | string | Required | none | Last executed amount  
↳ position_side | string | Required | none | Position side  
↳ create_time | string | Required | none | Create time  
↳ update_time | string | Required | none | Update time  
↳ result | object | Required | none | Update time  
↳ code | string | Required | none | Return code  
↳ time | integer | Required | none | Timestamp (seconds)  
↳ time_ms | integer | Required | none | Timestamp (milliseconds)  
  
Push example
    
    
    {
      "channel": "order",
      "event": "update",
      "payload": {
        "attribute": "COMMON",
        "business_type": "FUTURE",
        "create_time": "1756434169096",
        "exchange_type": "OKX",
        "executed_amount": "0",
        "executed_avg_price": "0",
        "executed_qty": "0",
        "fee": "0",
        "fee_coin": "",
        "last_executed_amount": "0",
        "last_executed_price": "0",
        "last_executed_qty": "0",
        "leverage": "3",
        "order_id": "2072652940337152",
        "position_side": "NONE",
        "price": "0.8499",
        "qty": "10",
        "quote_qty": "0",
        "reason": "{\"label\":\"TRADE_INSUFFICIENT_AVAILABLE_MARGIN_ERROR\",\"message\":\"Insufficient availableMargin\"}",
        "reduce_only": "false",
        "side": "BUY",
        "state": "FAIL",
        "symbol": "OKX_FUTURE_ADA_USDT",
        "text": "2072652940337152",
        "time_in_force": "GTC",
        "type": "MARKET",
        "update_time": "1756434169098",
        "user_id": "2124485957"
      },
      "result": {
        "code": "100000",
        "message": "success"
      },
      "time": 1756434168,
      "time_ms": 1756434168968
    }
    

#  Asset Subscription/Unsubscription

`asset`

The asset channel provides a way to receive user asset updates.

**Push Type** : `continuous`

**Update Frequency** : `real-time`

##  Client Subscription

##  Request Parameters

Request ParametersName | Location | Type | Required | Description  
---|---|---|---|---  
↳ time | body | integer | Optional | Timestamp (seconds)  
↳ event | body | string | Optional | Event  
↳ channel | body | string | Optional | Channel name  
↳ payload | body | [string] | Optional | Subscribe/Unsubscribe coin set !all means all  
  
###  Details

**» event** : subscribe、unsubscribe

**» channel** : asset

Payload format:

DetailsName | Type | Required | Description  
---|---|---|---  
`payload` | `Array[String]` | Optional | Coin list  
  
You can subscribe/unsubscribe multiple times. Coins subscribed earlier will not be overridden unless explicitly unsubscribed to.

WARNING

Authentication required

Request example
    
    
    {
      "time": 1754272114,
      "event": "subscribe",
      "channel": "asset",
      "payload": [
        "USDT"
      ]
    }
    

##  Server Push

Push parameters:

Name | Type | Required | Constraint | Description  
---|---|---|---|---  
↳ channel | string | Required | none | Channel name  
↳ event | string | Required | none | Event  
↳ payload | object | Required | none | Data set  
↳ user_id | string | Optional | none | User ID  
↳ coin | string | Optional | none | Coin  
↳ exchange_type | string | Optional | none | Exchange type  
↳ balance | string | Optional | none | Balance  
↳ upnl | string | Optional | none | Unrealized P&L  
↳ equity | string | Optional | none | Equity  
↳ futures_initial_margin | string | Optional | none | Futures initial margin  
↳ futures_maintenance_margin | string | Optional | none | Futures maintenance margin  
↳ borrowing_initial_margin | string | Optional | none | Borrowing initial margin for the coin  
↳ borrowing_maintenance_margin | string | Optional | none | Borrowing maintenance margin for the coin  
↳ available_balance | string | Optional | none | Available balance  
↳ result | object | Required | none | Update time  
↳ code | string | Required | none | Return code  
↳ time | integer | Required | none | Timestamp (seconds)  
↳ time_ms | integer | Required | none | Timestamp (milliseconds)  
  
Push example
    
    
    {
      "channel": "asset",
      "event": "update",
      "payload": {
        "available_balance": "9940.013209",
        "balance": "9967.013209",
        "coin": "USDT",
        "equity": "9967.013209",
        "exchange_type": "CROSSEX",
        "futures_initial_margin": "1.236",
        "futures_maintenance_margin": "0",
        "borrowing_initial_margin": "0",
        "borrowing_maintenance_margin": "0",
        "price": "1",
        "upnl": "0",
        "user_id": "2124492766"
      },
      "result": {
        "code": "100000",
        "message": "success"
      },
      "time": 1756465636,
      "time_ms": 1756465636463
    }
    

#  Trade Subscription/Unsubscription

`usertrades`

The trade channel provides a way to receive user trade updates.

**Push Type** : `continuous`

**Update Frequency** : `real-time`

##  Client Subscription

##  Request Parameters

Request ParametersName | Location | Type | Required | Description  
---|---|---|---|---  
↳ time | body | integer | Optional | Timestamp (seconds)  
↳ event | body | string | Optional | Event  
↳ channel | body | string | Optional | Channel name  
↳ payload | body | [string] | Optional | Subscribe/Unsubscribe coin set !all means all  
  
###  Details

**» event** : subscribe、unsubscribe

**» channel** : usertrades

##  Response Result

Response ResultName | Type | Required | Constraint | Description  
---|---|---|---|---  
↳ channel | string | Required | none | Channel name   
usertrades  
↳ event | string | Required | none | Event  
subscribe  
unsubscribe  
↳ payload | [string] | Required | none | Subscribe/Unsubscribe trading pair set  
↳ result | object | Required | none | Subscription/Unsubscription result  
↳ code | string | Required | none | Response code  
↳ message | string | Required | none | Response message  
↳ time | integer | Required | none | Timestamp (seconds)  
↳ time_ms | integer | Required | none | Timestamp (milliseconds)  
  
Payload format:

Response ResultName | Type | Required | Description  
---|---|---|---  
`payload` | `Array[String]` | Optional | Trading pair list  
  
You can subscribe/unsubscribe multiple times. Trading pairs subscribed earlier will not be overridden unless explicitly unsubscribed to.

WARNING

Authentication required

Request example
    
    
    {
      "time": 1754272114,
      "event": "subscribe",
      "channel": "usertrades",
      "payload": [
        "GATE_FUTURE_ETH_USDT"
      ]
    }
    

Response example
    
    
    {
      "channel": "usertrades",
      "event": "subscribe",
      "payload": [
        "OKX_FUTURE_ADA_USDT"
      ],
      "result": {
        "code": "100000",
        "message": "success"
      },
      "time": 1756434168,
      "time_ms": 1756434168928
    }
    

##  Server Push

Push parameters:

Name | Type | Required | Constraint | Description  
---|---|---|---|---  
↳ channel | string | Required | none | Channel name  
↳ event | string | Required | none | Event  
↳ payload | object | Required | none | Data set  
↳ user_id | string | Optional | none | User ID  
↳ transaction_id | string | Optional | none | Trade record ID  
↳ order_id | string | Optional | none | Order ID  
↳ text | string | Optional | none | User order ID  
↳ symbol | string | Optional | none | Trading pair  
↳ exchange_type | string | Optional | none | Exchange type  
↳ business_type | string | Optional | none | Business type  
↳ side | string | Optional | none | Buy/Sell direction  
↳ qty | string | Optional | none | Trade quantity  
↳ price | string | Optional | none | Trade price  
↳ fee | string | Optional | none | Fee  
↳ fee_coin | string | Optional | none | Fee coin  
↳ fee_rate | string | Optional | none | Fee rate  
↳ match_role | string | Optional | none | Trade role  
↳ rpnl | string | Optional | none | Realized P&L  
↳ position_mode | string | Optional | none | Position mode  
↳ position_side | string | Optional | none | Position side  
↳ create_time | string | Optional | none | Create time  
↳ result | object | Required | none | Update time  
↳ code | string | Required | none | Return code  
↳ time | integer | Required | none | Timestamp (seconds)  
↳ time_ms | integer | Required | none | Timestamp (milliseconds)  
  
Push example
    
    
    {
      "channel": "usertrades",
      "event": "update",
      "payload": {
        "user_id": "2124492766",
        "transaction_id": "2072784922594048",
        "order_id": "2072784922592768",
        "text": "2072784922592768",
        "symbol": "GATE_SPOT_ADA_USDT",
        "exchange_type": "GATE",
        "business_type": "SPOT",
        "side": "BUY",
        "qty": "13.36",
        "price": "0.8228",
        "fee": "0.004008000000000000",
        "fee_coin": "ADA",
        "fee_rate": "0.0003",
        "match_role": "TAKER",
        "rpnl": "0",
        "position_mode": "SINGLE",
        "position_side": "",
        "create_time": "1756465636528"
      },
      "result": {
        "code": "100000",
        "message": "success"
      },
      "time": 1756434168,
      "time_ms": 1756434168984
    }
    

#  Position Subscription/Unsubscription

`position`

The position channel provides a way to receive user position updates.

**Push Type** : `continuous`

**Update Frequency** : `real-time`

##  Client Subscription

##  Request Parameters

Request ParametersName | Location | Type | Required | Description  
---|---|---|---|---  
↳ time | body | integer | Optional | Timestamp (seconds)  
↳ event | body | string | Optional | Event  
↳ channel | body | string | Optional | Channel name  
↳ payload | body | [string] | Optional | !all means all  
  
###  Details

**» event** : subscribe、unsubscribe

**» channel** : position

##  Response Result

Response ResultName | Type | Required | Constraint | Description  
---|---|---|---|---  
↳ channel | string | Required | none | Channel name  
position  
↳ event | string | Required | none | Event  
subscribe  
unsubscribe  
↳ payload | [string] | Required | none | Subscribe/Unsubscribe trading pair set  
↳ result | object | Required | none | Subscription/Unsubscription result  
↳ code | string | Required | none | Response code  
↳ message | string | Required | none | Response message  
↳ time | integer | Required | none | Timestamp (seconds)  
↳ time_ms | integer | Required | none | Timestamp (milliseconds)  
  
Payload format:

Response ResultName | Type | Required | Description  
---|---|---|---  
`payload` | `Array[String]` | Optional | Trading pair list, `!all` means subscribe to all trading pairs  
  
You can subscribe/unsubscribe multiple times. Trading pairs subscribed earlier will not be overridden unless explicitly unsubscribed to.

WARNING

Authentication required

Request example
    
    
    {
      "time": 1754272114,
      "event": "subscribe",
      "channel": "position",
      "payload": [
        "GATE_FUTURE_ETH_USDT"
      ]
    }
    

Response example
    
    
    {
      "channel": "position",
      "event": "subscribe",
      "payload": [
        "OKX_FUTURE_ADA_USDT"
      ],
      "result": {
        "code": "100000",
        "message": "success"
      },
      "time": 1756434168,
      "time_ms": 1756434168929
    }
    

##  Server Push

Push parameters:

Name | Type | Required | Constraint | Description  
---|---|---|---|---  
↳ channel | string | Required | none | Channel name  
↳ event | string | Required | none | Event  
↳ payload | object | Required | none | Data set  
↳ user_id | string | Optional | none | User ID  
↳ position_id | string | Optional | none | Position ID  
↳ symbol | string | Optional | none | Trading pair  
↳ position_side | string | Optional | none | Position side  
↳ initial_margin | string | Optional | none | Initial margin  
↳ maintenance_margin | string | Optional | none | Maintenance margin  
↳ position_qty | string | Optional | none | Position quantity  
↳ position_value | string | Optional | none | Position value  
↳ upnl | string | Optional | none | Unrealized P&L  
↳ upnl_rate | string | Optional | none | Unrealized P&L rate  
↳ entry_price | string | Optional | none | Position entry average price  
↳ mark_price | string | Optional | none | Mark price  
↳ leverage | string | Optional | none | Position leverage  
↳ max_leverage | string | Optional | none | Maximum leverage  
↳ risk_limit | string | Optional | none | Risk limit  
↳ fee | string | Optional | none | Position fee  
↳ funding_fee | string | Optional | none | Position funding fee  
↳ funding_time | string | Optional | none | Position funding fee collection time  
↳ create_time | string | Optional | none | Position create time  
↳ update_time | string | Optional | none | Position update time  
↳ closed_pnl | string | Optional | none | Realized P&L  
↳ result | object | Required | none | Update time  
↳ code | string | Required | none | Return code  
↳ time | integer | Required | none | Timestamp (seconds)  
↳ time_ms | integer | Required | none | Timestamp (milliseconds)  
  
Push example
    
    
    {
    	"channel": "position",
    	"event": "update",
    	"payload": {
    		"create_time": "1756434169096",
    		"entry_price": "0",
    		"fee": "0",
    		"funding_fee": "0",
    		"funding_time": "0",
    		"initial_margin": "0",
    		"leverage": "3",
    		"maintenance_margin": "0",
    		"mark_price": "0.8499",
    		"max_leverage": "20",
    		"position_id": "20087051449819136",
    		"position_qty": "0",
    		"position_side": "NONE",
    		"position_value": "0",
    		"risk_limit": "1",
    		"symbol": "OKX_FUTURE_ADA_USDT",
    		"update_time": "1756434169098",
    		"upnl": "0",
    		"upnl_rate": "0",
    		"user_id": "2124485957",
    		"closed_pnl": "12"
    	},
    	"result": {
    		"code": "100000",
    		"message": "success"
    	},
    	"time": 1756434168,
    	"time_ms": 1756434168984
    }
    

#  Margin Position Subscription/Unsubscription

`margin_position`

The margin position channel provides a way to receive user margin position updates.

**Push Type** : `continuous`

**Update Frequency** : `real-time`

##  Client Subscription

##  Request Parameters

Request ParametersName | Location | Type | Required | Description  
---|---|---|---|---  
↳ time | body | integer | Optional | Timestamp (seconds)  
↳ event | body | string | Optional | Event  
↳ channel | body | string | Optional | Channel name  
↳ payload | body | [string] | Optional | !all means all  
  
###  Details

**» event** : subscribe、unsubscribe

**» channel** : margin_position

##  Response Result

Response ResultName | Type | Required | Constraint | Description  
---|---|---|---|---  
↳ channel | string | Required | none | Channel name  
position  
↳ event | string | Required | none | Event  
subscribe  
unsubscribe  
↳ payload | [string] | Required | none | Subscribe/Unsubscribe trading pair set  
↳ result | object | Required | none | Subscription/Unsubscription result  
↳ code | string | Required | none | Response code  
↳ message | string | Required | none | Response message  
↳ time | integer | Required | none | Timestamp (seconds)  
↳ time_ms | integer | Required | none | Timestamp (milliseconds)  
  
##  Push Message Response

Push Message ResponseName | Type | Required | Constraint | Description  
---|---|---|---|---  
↳ channel | string | Required | none | Channel name  
↳ event | string | Required | none | Event  
↳ payload | object | Required | none | Data set  
↳ user_id | string | Optional | none | User ID  
↳ position_id | string | Optional | none | Position ID  
↳ symbol | string | Optional | none | Trading pair EXCHANGE_MARGIN_BASE_COUNTER  
↳ position_side | string | Optional | none | Position side  
↳ initial_margin | string | Optional | none | Position initial margin  
↳ maintenance_margin | string | Optional | none | Position maintenance margin  
↳ asset_qty | string | Optional | none | Position asset quantity  
↳ asset_coin | string | Optional | none | Position asset coin  
↳ position_value | string | Optional | none | Position value  
↳ liability | string | Optional | none | Liability quantity  
↳ liability_coin | string | Optional | none | Liability coin  
↳ interest | string | Optional | none | Deducted interest  
↳ max_position_qty | string | Optional | none | Maximum position quantity  
↳ entry_price | string | Optional | none | Position cost price (entry average price)  
↳ index_price | string | Optional | none | Index price  
↳ upnl | string | Optional | none | Unrealized P&L  
↳ upnl_rate | string | Optional | none | Unrealized P&L rate  
↳ leverage | string | Optional | none | Entry leverage  
↳ max_leverage | string | Optional | none | Maximum leverage  
↳ create_time | string | Optional | none | Create time  
↳ update_time | string | Optional | none | Update time  
↳ result | object | Required | none | Update time  
↳ code | string | Required | none | Return code  
↳ time | integer | Required | none | Timestamp (seconds)  
↳ time_ms | integer | Required | none | Timestamp (milliseconds)  
  
Request example
    
    
    {
      "time": 1754272114,
      "event": "subscribe",
      "channel": "margin_position",
      "payload": [
        "GATE_MARGIN_ETH_USDT"
      ]
    }
    

Response example
    
    
    {
      "channel": "margin_position",
      "event": "subscribe",
      "payload": [
        "GATE_MARGIN_ETH_USDT"
      ],
      "result": {
        "code": "100000",
        "message": "success"
      },
      "time": 1756434168,
      "time_ms": 1756434168929
    }
    

Push message response example
    
    
    {
      "channel": "margin_position",
      "event": "subscribe",
      "payload":{
            "user_id": "20251115",
            "position_id": "20116122196200192",
            "symbol": "OKX_MARGIN_DOGE_USDT",
            "position_side": "LONG",
            "initial_margin": "3.339831063595188875",
            "maintenance_margin": "0.20743774877",
            "asset_qty": "61.72130605",
            "asset_coin": "DOGE",
            "position_value": "9.9969999409185",
            "liability": "10.00003424116",
            "liability_coin": "USDT",
            "interest": "0.0000343",
            "max_position_qty": "61.72130605",
            "entry_price": "0.162018605585874506",
            "index_price": "0.16197",
            "upnl": "-0.0030343002415",
            "upnl_rate": "-0.000909",
            "leverage": "3",
            "max_leverage": "8",
            "create_time": "1763365175843",
            "update_time": "1763365689548"
      },
      "result": {
        "code": "100000",
        "message": "success"
      },
      "time": 1756434168,
      "time_ms": 1756434168984
    }
    

#  Margin Interest Subscription/Unsubscription

`margin_interest`

The margin interest channel provides a way to receive user margin interest updates.

**Push Type** : `continuous`

**Update Frequency** : `real-time`

##  Client Subscription

##  Request Parameters

Request ParametersName | Location | Type | Required | Description  
---|---|---|---|---  
↳ time | body | integer | Optional | Timestamp (seconds)  
↳ event | body | string | Optional | Event  
↳ channel | body | string | Optional | Channel name  
↳ payload | body | [string] | Optional | !all means all  
  
###  Details

**» event** : subscribe、unsubscribe

**» channel** : margin_interest

##  Response Result

Response ResultName | Type | Required | Constraint | Description  
---|---|---|---|---  
↳ channel | string | Required | none | Channel name  
position  
↳ event | string | Required | none | Event  
subscribe  
unsubscribe  
↳ payload | [string] | Required | none | Subscribe/Unsubscribe trading pair set  
↳ result | object | Required | none | Subscription/Unsubscription result  
↳ code | string | Required | none | Response code  
↳ message | string | Required | none | Response message  
↳ time | integer | Required | none | Timestamp (seconds)  
↳ time_ms | integer | Required | none | Timestamp (milliseconds)  
  
##  Push Message Response

Push Message ResponseName | Type | Required | Constraint | Description  
---|---|---|---|---  
↳ channel | string | Required | none | Channel name  
↳ event | string | Required | none | Event  
↳ payload | object | Required | none | Data set  
↳ user_id | string | Optional | none | User ID  
↳ symbol | string | Optional | none | Trading pair  
↳ interest_id | string | Optional | none | Interest deduction ID  
↳ liability_id | string | Optional | none | Liability source ID, can be order ID/position ID  
↳ liability | string | Optional | none | Liability  
↳ liability_coin | string | Optional | none | Coin  
↳ interest | string | Optional | none | Interest  
↳ interest_rate | string | Optional | none | Interest rate  
↳ interest_type | string | Optional | none | Interest deduction type  
↳ create_time | string | Optional | none | Position create time  
↳ result | object | Required | none | Update time  
↳ code | string | Required | none | Return code  
↳ time | integer | Required | none | Timestamp (seconds)  
↳ time_ms | integer | Required | none | Timestamp (milliseconds)  
  
###  Details

**» interest_type** : Interest deduction type PERIODIC_POSITION hourly position interest, PERIODIC_OPEN_ORDER hourly order interest, IMMEDIATE_OPEN_ORDER order interest

Request example
    
    
    {
      "time": 1754272114,
      "event": "subscribe",
      "channel": "margin_interest",
      "payload": [
        "GATE_MARGIN_ETH_USDT"
      ]
    }
    

Response example
    
    
    {
      "channel": "margin_interest",
      "event": "subscribe",
      "payload": [
        "GATE_MARGIN_ETH_USDT"
      ],
      "result": {
        "code": "100000",
        "message": "success"
      },
      "time": 1756434168,
      "time_ms": 1756434168929
    }
    

Push message response example
    
    
    {
      "channel": "margin_interest",
      "event": "subscribe",
      "payload": {
        "user_id": "20251115",
        "symbol": "OKX_MARGIN_DOGE_USDT",
        "interest_id": "2101724189861376",
        "liability_id": "2101724189861120",
        "liability": "10",
        "liability_coin": "USDT",
        "interest": "0.0000343",
        "interest_rate": "0.00000343",
        "interest_type": "IMMEDIATE_OPEN_ORDER",
        "create_time": "1763365295219"
      },
      "result": {
        "code": "100000",
        "message": "success"
      },
      "time": 1756434168,
      "time_ms": 1756434168984
    }
    

#  Place Order

`place_order`

Provides a way to place orders via WebSocket.

Rate Limit: 100 requests per 10 seconds (shared with REST order placement)

##  Client Request

##  Request Parameters

Request ParametersName | Location | Type | Required | Description  
---|---|---|---|---  
↳ time | body | integer | Optional | none  
↳ event | body | string | Optional | Event  
↳ channel | body | string | Optional | Channel name  
↳ payload | body | object | Optional | none  
↳ header | body | object | Optional | Request header information  
↳ X-Gate-Channel-Id | body | string | Optional | Broker rebate channel ID  
↳ text | body | string¦null | Optional | User-defined ID  
↳ symbol | body | string | Optional | Unique identifier: Exchange_Business_Base_Counter  
↳ side | body | string | Optional | Trading direction  
↳ qty | body | string¦null | Optional | Base currency quantity  
↳ price | body | string¦null | Optional | Price  
↳ type | body | string¦null | Optional | Order type (default LIMIT, supported types: LIMIT, MARKET)  
↳ time_in_force | body | string¦null | Optional | Execution method  
↳ quote_qty | body | string¦null | Optional | Quote currency quantity  
↳ reduce_only | body | boolean¦null | Optional | Reduce only  
↳ position_side | body | string¦null | Optional | Position side  
  
###  Details

**» event** : api

**» channel** : place_order

**»» text** : User-defined ID Customer-defined order ID, only supports letters (a-z), numbers (0-9), symbols (-, _)

**»» symbol** : Unique identifier: Exchange_Business_Base_Counter Examples:

  * If you want to place a SPOT order for ADA/USDT on BINANCE exchange, you can use this unique identifier: `BINANCE_SPOT_ADA_USDT`;
  * If you want to place a USDT-M perpetual FUTURE order for ADA/USDT on OKX exchange, you can use this unique identifier: `OKX_FUTURE_ADA_USDT`;
  * If you want to place a spot MARGIN order for ADA/USDT on GATE exchange, you can use this unique identifier: `GATE_MARGIN_ADA_USDT`;
  * If you want to place a SPOT order for ADA/USDT on BYBIT exchange, you can use this unique identifier: `BYBIT_SPOT_ADA_USDT`;
  * Currently three order types are supported: SPOT orders, USDT-M perpetual FUTURE orders, and spot MARGIN orders. BYBIT does not support spot MARGIN orders yet

**»» side** : Buy BUY Sell SELL

**»» qty** : Base currency quantity Order quantity (mandatory, except for spot market buy)

**»» price** : Price Limit order price (required for limit orders)

**»» time_in_force** : Execution method Default GTC, supported types: GTC, IOC, FOK, POC

**»» quote_qty** : Quote currency quantity Order quote quantity, only used for spot market buy orders

**»» reduce_only** : Reduce only true、false

**»» position_side** : Position side Not passed for single position. LONG, SHORT Enum values: LONG SHORT NONE

##  Response Result

Response ResultName | Type | Required | Constraint | Description  
---|---|---|---|---  
↳ channel | string | Required | none | Channel name  
place_order  
↳ event | string | Required | none | Event  
api  
↳ payload | object | Required | none | Place order request parameters  
↳ order_id | string | Required | none | Order ID  
↳ text | string | Required | none | Client ID  
↳ result | object | Required | none | Place order result  
↳ code | string | Required | none | none  
↳ message | string | Required | none | none  
↳ time | integer | Required | none | Timestamp (seconds)  
↳ time_ms | integer | Required | none | Timestamp (milliseconds)  
  
Request example
    
    
    {
      "time": 1754272114,
      "event": "api",
      "channel": "place_order",
      "payload": {
        "header":{
          "X-Gate-Channel-Id":"broker-api"
        },
        "text": "test1",
        "symbol": "GATE_FUTURE_ETH_USDT",
        "side": "BUY",
        "qty": "0.01",
        "price": "2800",
        "type": "LIMIT"
      }
    }
    

Response example
    
    
    {
      "channel": "place_order",
      "event": "api",
      "payload": {
        "order_id": "2072652940337152",
        "text": "2072652940337152"
      },
      "result": {
        "code": "100000",
        "message": "success"
      },
      "time": 1756434168,
      "time_ms": 1756434168948
    }
    

#  Cancel Order

`cancel_order`

Provides a way to cancel orders via WebSocket.

Rate Limit: 100 requests per 10 seconds (shared with REST order placement)

##  Client Request

##  Request Parameters

Request ParametersName | Location | Type | Required | Description  
---|---|---|---|---  
↳ time | body | integer | Optional | Timestamp (seconds)  
↳ event | body | string | Optional | Event  
↳ channel | body | string | Optional | Channel name  
↳ payload | body | string | Optional | Order ID  
  
###  Details

**» event** : api

**» channel** : cancel_order

##  Response Result

Response ResultName | Type | Required | Constraint | Description  
---|---|---|---|---  
↳ channel | string | Required | none | Channel name  
cancel_order  
↳ event | string | Required | none | Event  
api  
↳ result | object | Required | none | Cancel order result  
↳ code | string | Required | none | Response code  
↳ message | string | Required | none | Response message  
↳ time | integer | Required | none | Timestamp (seconds)  
↳ time_ms | integer | Required | none | Timestamp (milliseconds)  
  
Request example
    
    
    {
      "time": 1754272114,
      "event": "api",
      "channel": "cancel_order",
      "payload": "2065058175870464"
    }
    

Response example
    
    
    {
      "channel": "cancel_order",
      "event": "api",
      "result": {
        "code": "100000",
        "message": "success"
      },
      "time": 1756434168,
      "time_ms": 1756434168948
    }
    

#  Update Order

`update_order`

Provides a way to update orders via WebSocket.

Rate Limit: 100 requests per 10 seconds (shared with REST order placement)

##  Client Request

##  Request Parameters

Request ParametersName | Location | Type | Required | Description  
---|---|---|---|---  
↳ time | body | integer | Optional | Timestamp (seconds)  
↳ event | body | string | Optional | Event  
↳ channel | body | string | Optional | Channel name  
↳ payload | body | object | Optional | none  
↳ order_id | body | string | Optional | Order ID  
↳ qty | body | string | Optional | Quantity  
↳ price | body | string | Optional | none  
↳ symbol | body | string | Optional | none  
  
###  Details

**» event** : api

**» channel** : update_order

##  Response Result

Response ResultName | Type | Required | Constraint | Description  
---|---|---|---|---  
↳ channel | string | Required | none | Channel name  
update_order  
↳ event | string | Required | none | Event  
api  
↳ payload | object | Required | none | none  
↳ order_id | string | Required | none | Order ID  
↳ text | string | Required | none | Client ID  
↳ result | object | Required | none | Update result  
↳ code | string | Required | none | Response code  
↳ message | string | Required | none | Response message  
↳ time | integer | Required | none | Timestamp (seconds)  
↳ time_ms | integer | Required | none | Timestamp (milliseconds)  
  
Request example
    
    
    {
      "time": 1754272114,
      "event": "api",
      "channel": "update_order",
      "payload": {
        "order_id": "2065057827622656",
        "qty": "0.01",
        "symbol": "GATE_SPOT_BTC_USDT",
        "price": "2801"
      }
    }
    

Response example
    
    
    {
      "channel": "update_order",
      "event": "api",
      "payload": {
        "order_id": "2072652940337152",
        "text": "2072652940337152"
      },
      "result": {
        "code": "100000",
        "message": "success"
      },
      "time": 1756434168,
      "time_ms": 1756434168948
    }
    

#  Set Leverage

`set_leverage`

Provides a way to modify contract leverage via WebSocket.

Rate Limit: 100 requests per 10 seconds (shared with REST order placement)

##  Client Request

##  Request Parameters

Request ParametersName | Location | Type | Required | Description  
---|---|---|---|---  
↳ time | body | integer | Optional | Timestamp (seconds)  
↳ event | body | string | Optional | Event  
↳ channel | body | string | Optional | Channel name  
↳ payload | body | object | Optional | none  
↳ symbol | body | string | Optional | Trading pair  
↳ leverage | body | string | Optional | Leverage  
  
##  Details

**» event** : api

**» channel** : set_leverage

##  Response Result

Response ResultName | Type | Required | Constraint | Description  
---|---|---|---|---  
↳ channel | string | Required | none | Channel name  
set_leverage  
↳ event | string | Required | none | Event  
api  
↳ payload | object | Required | none | none  
↳ symbol | string | Required | none | Trading pair  
↳ leverage | string | Required | none | Leverage  
↳ result | object | Required | none | Update result  
↳ code | string | Required | none | Response code  
↳ message | string | Required | none | Response message  
↳ time | integer | Required | none | Timestamp (seconds)  
↳ time_ms | integer | Required | none | Timestamp (milliseconds)  
  
Request example
    
    
    {
      "time": 1754272114,
      "event": "api",
      "channel": "set_leverage",
      "payload": {
        "symbol": "GATE_FUTURE_ETH_USDT",
        "leverage": "5"
      }
    }
    

Response example
    
    
    {
      "channel": "set_leverage",
      "event": "api",
      "payload": {
        "symbol": "GATE_FUTURE_ETH_USDT",
        "leverage": "10"
      },
      "result": {
        "code": "100000",
        "message": "success"
      },
      "time": 1756434168,
      "time_ms": 1756434168948
    }
    

#  Set Margin Leverage

`set_margin_leverage`

Provides a way to modify spot margin leverage via WebSocket.

Rate Limit: 100 requests per 10 seconds (shared with REST order placement)

##  Client Request

##  Request Parameters

Request ParametersName | Location | Type | Required | Description  
---|---|---|---|---  
↳ time | body | integer | Optional | Timestamp (seconds)  
↳ event | body | string | Optional | Event  
↳ channel | body | string | Optional | Channel name  
↳ payload | body | object | Optional | none  
↳ symbol | body | string | Optional | Trading pair  
↳ leverage | body | string | Optional | Leverage  
  
##  Details

**» event** : api

**» channel** : set_margin_leverage

##  Response Result

Response ResultName | Type | Required | Constraint | Description  
---|---|---|---|---  
↳ channel | string | Required | none | Channel name  
set_leverage  
↳ event | string | Required | none | Event  
api  
↳ payload | object | Required | none | none  
↳ symbol | string | Required | none | Trading pair  
↳ leverage | string | Required | none | Leverage  
↳ result | object | Required | none | Update result  
↳ code | string | Required | none | Response code  
↳ message | string | Required | none | Response message  
↳ time | integer | Required | none | Timestamp (seconds)  
↳ time_ms | integer | Required | none | Timestamp (milliseconds)  
  
Request example
    
    
    {
      "time": 1754272114,
      "event": "api",
      "channel": "set_margin_leverage",
      "payload": {
        "symbol": "OKX_MARGIN_ADA_USDT",
        "leverage": "5"
      }
    }
    

Response example
    
    
    {
      "channel": "set_margin_leverage",
      "event": "api",
      "payload": {
        "symbol": "OKX_MARGIN_ADA_USDT",
        "leverage": "10"
      },
      "result": {
        "code": "100000",
        "message": "success"
      },
      "time": 1756434168,
      "time_ms": 1756434168948
    }
    

#  Update Accounts

`update_accounts`

Provides a way to change account contract position mode and account mode via WebSocket.

Rate Limit: 100 requests per 60 seconds

##  Client Request

##  Request Parameters

Request ParametersName | Location | Type | Required | Description  
---|---|---|---|---  
↳ time | body | integer | Optional | Timestamp (seconds)  
↳ event | body | string | Optional | Event  
↳ channel | body | string | Optional | Channel name  
↳ payload | body | object | Optional | none  
↳ position_mode | body | string | Optional | Position mode  
↳ account_mode | body | string | Optional | Account mode  
↳ exchange_type | body | string | Optional | Exchange, default is cross-exchange  
  
###  Details

**» event** : api

**» channel** : update_accounts

**»» position_mode** : SINGLE/DUAL

**»» account_mode** : CROSS_EXCHANGE/ISOLATED_EXCHANGE

**»» exchange_type** : BINANCE/OKX/GATE/BYBIT/CROSSEX, when account mode is ISOLATED_EXCHANGE, exchange must be specified when modifying contract position mode

##  Response Result

Response ResultName | Type | Required | Constraint | Description  
---|---|---|---|---  
↳ channel | string | Required | none | Channel name  
update_accounts  
↳ event | string | Required | none | Event  
api  
↳ payload | object | Required | none | none  
↳ position_mode | string | Optional | none | Position mode  
↳ account_mode | string | Optional | none | Account mode  
↳ exchange_type | string | Optional | none | Exchange  
↳ result | object | Required | none | Update result  
↳ code | string | Required | none | Response code  
↳ message | string | Required | none | Response message  
↳ time | integer | Required | none | Timestamp (seconds)  
↳ time_ms | integer | Required | none | Timestamp (milliseconds)  
  
Request example
    
    
    {
      "time": 1754272114,
      "event": "api",
      "channel": "update_accounts",
      "payload": {
        "account_mode":"ISOLATED_EXCHANGE",
        "position_mode": "DUAL",
        "exchange_type": "BINANCE"
      }
    }
    

Response example
    
    
    {
      "channel": "update_accounts",
      "event": "api",
      "payload": {
        "account_mode":"ISOLATED_EXCHANGE",
        "position_mode": "DUAL",
        "exchange_type": "BINANCE"
      },
      "result": {
        "code": "100000",
        "message": "success"
      },
      "time": 1756434168,
      "time_ms": 1756434168948
    }
    

#  Close Position

`close_position`

Provides a way to close positions completely via WebSocket.

Rate Limit: 100 requests per day

##  Client Request

##  Request Parameters

Request ParametersName | Location | Type | Required | Description  
---|---|---|---|---  
↳ time | body | integer | Optional | Timestamp (seconds)  
↳ event | body | string | Optional | Event  
↳ channel | body | string | Optional | Channel name  
↳ payload | body | object | Optional | none  
↳ symbol | body | string | Optional | Trading pair  
↳ position_side | body | string | Optional | Position side  
  
##  Details

**» event** : api

**» channel** : close_position

##  Response Result

Response ResultName | Type | Required | Constraint | Description  
---|---|---|---|---  
↳ channel | string | Required | none | Channel name  
close_position  
↳ event | string | Required | none | Event  
api  
↳ payload | object | Required | none | none  
↳ order_id | string | Required | none | Order ID  
↳ text | string | Required | none | Client ID  
  
Request example
    
    
    {
      "time": 1754272114,
      "event": "api",
      "channel": "close_position",
      "payload": {
        "symbol": "GATE_MARGIN_ETH_USDT",
        "position_side": "LONG"
      }
    }
    

Response example
    
    
    {
      "channel": "close_position",
      "event": "api",
      "payload": {
        "order_id": "2072652940337152",
        "text": "2072652940337152"
      },
      "result": {
        "code": "100000",
        "message": "success"
      },
      "time": 1756434168,
      "time_ms": 1756434168948
    }
    

#  Response Codes

Response Code | Description  
---|---  
100000 | Success  
100001 | Parameter missing or invalid  
100002 | Not logged in  
100003 | Connection limit reached  
100004 | Timeout  
100005 | Operation failed  
100006 | Login failed  
100007 | Network error, please try again later  
  
Last Updated: 4/27/2026, 10:15:14 AM