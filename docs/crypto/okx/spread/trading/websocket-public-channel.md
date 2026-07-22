---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#spread-trading-websocket-public-channel
anchor_id: spread-trading-websocket-public-channel
api_type: WebSocket
updated_at: 2026-07-22 19:20:21.782712
---

# WebSocket Public Channel

* Production Trading URL: `wss://ws.okx.com:8443/ws/v5/business`  
  * Demo Trading URL: `wss://wspap.okx.com:8443/ws/v5/business`

### Order book channel

Retrieve order book data. Available channels:

  * `sprd-bbo-tbt`: 1 depth level snapshot will be pushed in the initial push. Snapshot data will be pushed every 10 ms when there are changes in the 1 depth level snapshot.
  * `sprd-books5`: 5 depth levels snapshot will be pushed in the initial push. Snapshot data will be pushed every 100 ms when there are changes in the 5 depth levels snapshot.
  * `sprd-books-l2-tbt`: 400 depth levels will be pushed in the initial full snapshot. Incremental data will be pushed every 10 ms for the changes in the order book during that period of time. 
  * The push sequence for order book channels within the same connection and trading symbols is fixed as: sprd-bbo-tbt -> sprd-books-l2-tbt -> sprd-books5.

#### URL Path

/ws/v5/business

> Request Example: sprd-books5
    
    
    {
      "id": "1512",
      "op": "subscribe",
      "args": [
        {
          "channel": "sprd-books5",
          "sprdId": "BTC-USDT_BTC-USDT-SWAP"
        }
      ]
    }
    
    
    
    import asyncio
    from okx.websocket.WsPublicAsync import WsPublicAsync
    
    def callbackFunc(message):
        print(message)
    
    async def main():
        ws = WsPublicAsync(url="wss://wspap.okx.com:8443/ws/v5/business")
        await ws.start()
        args = [
            {
              "channel": "sprd-books5",
              "sprdId": "BTC-USDT_BTC-USDT-SWAP"
            }
        ]
    
        await ws.subscribe(args, callback=callbackFunc)
        await asyncio.sleep(10)
    
        await ws.unsubscribe(args, callback=callbackFunc)
        await asyncio.sleep(10)
    
    asyncio.run(main())
    
    

> Request Example: sprd-books-l2-tbt
    
    
    {
      "id": "1512",
      "op": "subscribe",
      "args": [
        {
          "channel": "sprd-books-l2-tbt",
          "sprdId": "BTC-USDT_BTC-USDT-SWAP"
        }
      ]
    }
    
    
    
    import asyncio
    from okx.websocket.WsPublicAsync import WsPublicAsync
    
    def callbackFunc(message):
        print(message)
    
    async def main():
        ws = WsPublicAsync(url="wss://wspap.okx.com:8443/ws/v5/business")
        await ws.start()
        args = [
            {
              "channel": "sprd-books-l2-tbt",
              "sprdId": "BTC-USDT_BTC-USDT-SWAP"
            }
        ]
    
        await ws.subscribe(args, callback=callbackFunc)
        await asyncio.sleep(10)
    
        await ws.unsubscribe(args, callback=callbackFunc)
        await asyncio.sleep(10)
    
    asyncio.run(main())
    
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
id | String | No | Unique identifier of the message   
Provided by client. It will be returned in response message for identifying the corresponding request.   
A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters.  
op | String | Yes | Operation  
`subscribe`  
`unsubscribe`  
  
args | Array of objects | Yes | List of subscribed channels  
`sprd-bbo-tbt`  
`sprd-books5`  
`sprd-books-l2-tbt`  
> channel | String | Yes | Channel name  
> sprdId | String | Yes | spread ID  
  
> Successful Response Example: sprd-books5
    
    
    {
      "id": "1512",
      "event": "subscribe",
      "arg": {
        "channel": "sprd-books5",
        "sprdId": "BTC-USDT_BTC-USDT-SWAP"
      },
      "connId": "a4d3ae55"
    }
    

> Successful Response Example: sprd-books-l2-tbt
    
    
    {
      "id": "1512",
       "event":"subscribe",
       "arg":{
          "channel":"sprd-books-l2-tbt",
          "sprdId":"BTC-USDT_BTC-USDT-SWAP"
       },
       "connId":"214fdd24"
    }
    

> Failure Response Example
    
    
    {
      "id": "1512",
      "event": "error",
      "code": "60012",
      "msg": "Invalid request: {\"op\": \"subscribe\", \"args\":[{ \"channel\" : \"sprd-books5\", \"sprdId\" : \"BTC-USD_BTC-USD-191227\"}]}",
      "connId": "a4d3ae55"
    }
    

#### Response parameters

Parameter | Type | Required | Description  
---|---|---|---  
id | String | No | Unique identifier of the message  
event | String | Yes | Event  
`subscribe`  
`unsubscribe`  
`error`  
arg | Object | No | Subscribed channels  
`sprd-bbo-tbt`  
`sprd-books5`  
`sprd-books-l2-tbt`  
> channel | String | Yes | Channel name  
> sprdId | String | Yes | spread ID  
msg | String | No | Error message  
code | String | No | Error code  
connId | String | Yes | WebSocket connection ID  
  
> Push Data Example: sprd-books5
    
    
    {
      "arg": {
        "channel": "sprd-books5",
        "sprdId": "BTC-USDT_BTC-USDT-SWAP"
      },
      "data": [
        {
          "asks": [
            ["111.06","55154","2"],
            ["111.07","53276","2"],
            ["111.08","72435","2"],
            ["111.09","70312","2"],
            ["111.1","67272","2"]],
          "bids": [
            ["111.05","57745","2"],
            ["111.04","57109","2"],
            ["111.03","69563","2"],
            ["111.02","71248","2"],
            ["111.01","65090","2"]],
          "ts": "1670324386802",
          "seqId":1724294007352168320
        }
      ]
    }
    

> Push Data Example: sprd-books-l2-tbt
    
    
    {
       "arg":{
          "channel":"sprd-books-l2-tbt",
          "sprdId":"BTC-USDT_BTC-USDT-SWAP"
       },
       "action":"snapshot",
       "data":[
          {
             "asks":[
                ["1.9","1.1","3"],
                ["2.5","0.9","1"],
                ["3.2","4.921","1"],
                ["4.8","0.165","1"],
                ["5.2","4.921","1"]
              ......
             ],
             "bids":[
                ["1.8","0.165","1"],
                ["0.6","0.2","2"],
                ["0","23.49","1"],
                ["-0.1","1","1"],
                ["-0.6","1","1"],
                ["-3.9","4.921","1"]
                ......
             ],
             "ts":"1724391380926",
             "checksum":-1285595583,
             "prevSeqId":-1,
             "seqId":1724294007352168320
          }
       ]
    }
    

#### Push data parameters

Parameter | Type | Description  
---|---|---  
arg | Object | Successfully subscribed channel  
> channel | String | Channel name  
> sprdId | String | spread ID  
action | String | Push data action, incremental data or full snapshot.  
`snapshot`: full  
`update`: incremental  
data | Array of objects | Subscribed data  
> asks | Array of strings | Order book on sell side  
> bids | Array of strings | Order book on buy side  
> ts | String | Order book generation time, Unix timestamp format in milliseconds, e.g. 1597026383085  
> checksum | Integer | Checksum, implementation details below. Only applicable to `sprd-books-l2-tbt`.  
> prevSeqId | Integer | Sequence ID of the last sent message. Only applicable to `sprd-books-l2-tbt`.  
> seqId | Integer | Sequence ID of the current message, implementation details below.  
An example of the array of asks and bids values: ["411.8", "10", "4"]  
\- "411.8" is the depth price  
\- "10" is the quantity at the price (Unit: szCcy)  
\- "4" is the number of orders at the price.  

#### Sequence ID

`seqId` is the sequence ID of the market data published. The set of sequence ID received by users is the same if users are connecting to the same channel through multiple websocket connections. Each `sprdId` has an unique set of sequence ID. Users can use `prevSeqId` and `seqId` to build the message sequencing for incremental order book updates. Generally the value of seqId is larger than prevSeqId. The `prevSeqId` in the new message matches with `seqId` of the previous message. The smallest possible sequence ID value is 0, except in snapshot messages where the prevSeqId is always -1.  

Exceptions:  
1\. If there are no updates to the depth for an extended period, OKX will send a message with `'asks': [], 'bids': []` to inform users that the connection is still active. `seqId` is the same as the last sent message and `prevSeqId` equals to `seqId`. 2\. The sequence number may be reset due to maintenance, and in this case, users will receive an incremental message with `seqId` smaller than `prevSeqId`. However, subsequent messages will follow the regular sequencing rule.

##### Example

  1. Snapshot message: prevSeqId = -1, seqId = 10
  2. Incremental message 1 (normal update): prevSeqId = 10, seqId = 15
  3. Incremental message 2 (no update): prevSeqId = 15, seqId = 15
  4. Incremental message 3 (sequence reset): prevSeqId = 15, seqId = 3
  5. Incremental message 4 (normal update): prevSeqId = 3, seqId = 5

#### Checksum

This mechanism can assist users in checking the accuracy of depth data.

##### Merging incremental data into full data

After subscribing to the incremental load push (such as `books` 400 levels) of Order Book Channel, users first receive the initial full load of market depth. After the incremental load is subsequently received, update the local full load.

  1. If there is the same price, compare the size. If the size is 0, delete this depth data. If the size changes, replace the original data.
  2. If there is no same price, sort by price (bid in descending order, ask in ascending order), and insert the depth information into the full load.

##### Calculate Checksum

Use the first 25 bids and asks in the full load to form a string (where a colon connects the price and size in an ask or a bid), and then calculate the CRC32 value (32-bit signed integer).

### Public Trades channel

Retrieve the recent trades data from `sprd-public-trades`. Data will be pushed whenever there is a trade. Every update contains only one trade.

#### URL Path

/ws/v5/business

> Request Example 
    
    
    {
      "id": "1512",
      "op": "subscribe",
      "args": [
        {
          "channel": "sprd-public-trades",
          "sprdId": "BTC-USDT_BTC-USDT-SWAP"
        }
      ]
    }
    
    
    
    import asyncio
    from okx.websocket.WsPublicAsync import WsPublicAsync
    
    def callbackFunc(message):
        print(message)
    
    async def main():
        ws = WsPublicAsync(url="wss://wspap.okx.com:8443/ws/v5/business")
        await ws.start()
        args = [
            {
              "channel": "sprd-public-trades",
              "sprdId": "BTC-USDT_BTC-USDT-SWAP"
            }
        ]
    
        await ws.subscribe(args, callback=callbackFunc)
        await asyncio.sleep(10)
    
        await ws.unsubscribe(args, callback=callbackFunc)
        await asyncio.sleep(10)
    
    asyncio.run(main())
    
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
id | String | No | Unique identifier of the message   
Provided by client. It will be returned in response message for identifying the corresponding request.   
A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters.  
op | String | Yes | Operation  
`subscribe`  
`unsubscribe`  
  
args | Array of objects | Yes | List of subscribed channels  
> channel | String | Yes | Channel name  
`sprd-public-trades`  
> sprdId | String | Yes | spread ID  
  
> Successful Response Example
    
    
    {
      "id": "1512",
      "event": "subscribe",
      "arg": {
          "channel": "sprd-public-trades",
          "sprdId": "BTC-USDT_BTC-USDT-SWAP"
        },
      "connId": "a4d3ae55"
    }
    

> Failure Response Example
    
    
    {
      "id": "1512",
      "event": "error",
      "code": "60012",
      "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{ \"channel\" : \"sprd-public-trades\", \"instId\" : \"BTC-USD-191227\"}]}",
      "connId": "a4d3ae55"
    }
    

#### Response parameters

Parameter | Type | Required | Description  
---|---|---|---  
id | String | No | Unique identifier of the message  
event | String | Yes | Event  
`subscribe`  
`unsubscribe`  
`error`  
arg | Object | No | Subscribed channel  
> channel | String | Yes | Channel name  
> sprdId | String | Yes | spread ID  
code | String | No | Error code  
msg | String | No | Error message  
connId | String | Yes | WebSocket connection ID  
  
> Push Data Example
    
    
    {
        "arg": {
            "channel": "sprd-public-trades",
            "sprdId": "BTC-USDT_BTC-USDT-SWAP"
        },
        "data": [
            {
                "sprdId": "BTC-USDT_BTC-USDT-SWAP",
                "tradeId": "2499206329160695808",
                "px": "-10",
                "sz": "0.001",
                "side": "sell",
                "ts": "1726801105519"
            }
        ]
    }
    

#### Push data parameters

**Parameter** | **Type** | **Description**  
---|---|---  
arg | Object | Successfully subscribed channel  
> channel | String | Channel name  
> sprdId | String | spread ID  
data | Array of objects | Subscribed data  
> sprdId | String | spread ID, e.g.  
> tradeId | String | Trade ID  
> px | String | Trade price  
sz | String | Trade quantity   
For spot trading, the unit is base currency  
For `FUTURES`/`SWAP`/`OPTION`, the unit is contract.  
> side | String | Trade direction, buy, sell  
> ts | String | Filled time, Unix timestamp format in milliseconds, e.g. 1597026383085  
  
### Tickers channel

Retrieve the last traded price, bid price, ask price. The fastest rate is 1 update/100ms. There will be no update if the event is not triggered. The events which can trigger update: trade, the change on best ask/bid price

#### URL Path

/ws/v5/business

> Request Example
    
    
    {
      "id": "1512",
      "op": "subscribe",
      "args": [
        {
          "channel": "sprd-tickers",
          "sprdId": "BTC-USDT_BTC-USDT-SWAP"
        }
      ]
    }
    
    
    
    import asyncio
    from okx.websocket.WsPublicAsync import WsPublicAsync
    
    def callbackFunc(message):
        print(message)
    
    async def main():
        ws = WsPublicAsync(url="wss://wspap.okx.com:8443/ws/v5/business")
        await ws.start()
        args = [
            {
              "channel": "sprd-tickers",
              "sprdId": "BTC-USDT_BTC-USDT-SWAP"
            }
        ]
    
        await ws.subscribe(args, callback=callbackFunc)
        await asyncio.sleep(10)
    
        await ws.unsubscribe(args, callback=callbackFunc)
        await asyncio.sleep(10)
    
    asyncio.run(main())
    
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
id | String | No | Unique identifier of the message   
Provided by client. It will be returned in response message for identifying the corresponding request.   
A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters.  
op | String | Yes | Operation  
`subscribe`  
`unsubscribe`  
  
args | Array of objects | Yes | List of subscribed channels  
> channel | String | Yes | Channel name  
`sprd-tickers`  
> sprdId | String | Yes | spread ID  
  
> Successful Response Example
    
    
    {
      "id": "1512",
      "event": "subscribe",
      "arg": {
        "channel": "sprd-tickers",
        "sprdId": "BTC-USDT_BTC-USDT-SWAP"
      },
      "connId": "a4d3ae55"
    }
    

> Failure Response Example
    
    
    {
      "id": "1512",
      "event": "error",
      "code": "60012",
      "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{ \"channel\" : \"sprd-tickers\", \"instId\" : \"LTC-USD-200327\"}]}",
      "connId": "a4d3ae55"
    }
    

#### Response parameters

Parameter | Type | Required | Description  
---|---|---|---  
id | String | No | Unique identifier of the message  
event | String | Yes | Event  
`subscribe`  
`unsubscribe`  
`error`  
arg | Object | No | Subscribed channel  
> channel | String | Yes | Channel name  
> sprdId | String | Yes | spread ID  
code | String | No | Error code  
msg | String | No | Error message  
connId | String | Yes | WebSocket connection ID  
  
> Push Data Example
    
    
    {
        "arg": {
            "channel": "sprd-tickers",
            "sprdId": "BTC-USDT_BTC-USDT-SWAP"
        },
        "data": [
            {
                "sprdId": "BTC-USDT_BTC-USDT-SWAP",
                "last": "4",
                "lastSz": "0.01",
                "askPx": "19.7",
                "askSz": "5.79",
                "bidPx": "5.9",
                "bidSz": "5.79",
                "open24h": "-7",
                "high24h": "19.6",
                "low24h": "-7",
                "vol24h": "9.87",
                "ts": "1715247061026"
            }
        ]
    }
    

#### Push data parameters

**Parameter** | **Type** | **Description**  
---|---|---  
arg | Object | Successfully subscribed channel  
> channel | String | Channel name  
> sprdId | String | spread ID  
data | Array of objects | Subscribed data  
> sprdId | String | spread ID  
> last | String | Last traded price  
> lastSz | String | Last traded size  
> askPx | String | Best ask price  
> askSz | String | Best ask size  
> bidPx | String | Best bid price  
> bidSz | String | Best bid size  
> open24h | String | Open price in the past 24 hours  
> high24h | String | Highest price in the past 24 hours  
> low24h | String | Lowest price in the past 24 hours  
> vol24h | String | 24h trading volume, with a unit of base currency or USD  
> ts | String | Ticker data generation time, Unix timestamp format in milliseconds, e.g. 1597026383085  
vol24h  
For Spot vs USDT-margined contracts spread and USDT-margined contracts spread, the volume is with the unit of base currency; for Crypto-margined contracts spread, the volume is with the unit of USD. 

### Candlesticks channel

Retrieve the candlesticks data of an instrument. The push frequency is the fastest interval 1 second push the data.

#### URL Path

/ws/v5/business

> Request Example
    
    
    {
      "id": "1512",
       "op":"subscribe",
       "args":[
          {
             "channel":"sprd-candle1D",
             "sprdId":"BTC-USDT_BTC-USDT-SWAP"
          }
       ]
    }
    
    
    
    
    import asyncio
    from okx.websocket.WsPublicAsync import WsPublicAsync
    
    def callbackFunc(message):
        print(message)
    
    async def main():
        ws = WsPublicAsync(url="wss://wspap.okx.com:8443/ws/v5/business")
        await ws.start()
        args = [
          {
             "channel":"sprd-candle1D",
             "sprdId":"BTC-USDT_BTC-USDT-SWAP"
          }
        ]
    
        await ws.subscribe(args, callback=callbackFunc)
        await asyncio.sleep(10)
    
        await ws.unsubscribe(args, callback=callbackFunc)
        await asyncio.sleep(10)
    
    asyncio.run(main())
    
    

#### Request parameters

Parameter | Type | Required | Description  
---|---|---|---  
id | String | No | Unique identifier of the message   
Provided by client. It will be returned in response message for identifying the corresponding request.   
A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters.  
op | String | Yes | Operation, subscribe unsubscribe  
args | Array of objects | Yes | List of subscribed channels  
> channel | String | Yes | Channel name   
`sprd-candle3M` `sprd-candle1M`   
`sprd-candle1W`   
`sprd-candle1D` `sprd-candle2D` `sprd-candle3D` `sprd-candle5D`   
`sprd-candle12H` `sprd-candle6H` `sprd-candle4H` `sprd-candle2H` `sprd-candle1H`   
`sprd-candle30m` `sprd-candle15m` `sprd-candle5m` `sprd-candle3m` `sprd-candle1m`   
`sprd-candle3Mutc` `sprd-candle1Mutc` `sprd-candle1Wutc` `sprd-candle1Dutc` `sprd-candle2Dutc` `sprd-candle3Dutc` `sprd-candle5Dutc` `sprd-candle12Hutc` `sprd-candle6Hutc`  
> sprdId | String | Yes | Spread ID  
  
> Successful Response Example
    
    
    {
      "id": "1512",
      "event": "subscribe",
      "arg": {
        "channel": "sprd-candle1D",
        "sprdId": "BTC-USDT_BTC-USDT-SWAP"
      },
      "connId": "a4d3ae55"
    }
    
    

> Failure Response Example
    
    
    {
      "id": "1512",
      "event": "error",
      "code": "60012",
      "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{ \"channel\" : \"sprd-candle1D\", \"instId\" : \"BTC-USD-191227\"}]}",
      "connId": "a4d3ae55"
    }
    
    

#### Response parameters

Parameter | Type | Required | Description  
---|---|---|---  
id | String | No | Unique identifier of the message  
event | String | Yes | Event, subscribe unsubscribe error  
arg | Object | No | Subscribed channel  
channel | String | yes | channel name  
sprdId | String | Yes | Spread ID  
code | String | No | Error code  
msg | String | No | Error message  
  
> Push Data Example
    
    
    {
      "arg": {
        "channel": "sprd-candle1D",
        "sprdId": "BTC-USDT_BTC-USD-SWAP"
      },
      "data": [
        [
          "1597026383085",
          "8533.02",
          "8553.74",
          "8527.17",
          "8548.26",
          "45247",
          "0"
        ]
      ]
    }
    
    

#### Push data parameters

Parameter | Type | Description  
---|---|---  
arg | Object | Successfully subscribed channel  
> channel | String | Channel name  
> sprdId | String | Spread ID  
data | Array of Arrays | Subscribed data  
> ts | String | Opening time of the candlestick, Unix timestamp format in milliseconds, e.g. 1597026383085  
> o | String | Open price  
> h | String | highest price  
> l | String | Lowest price  
> c | String | Close price  
> vol | String | Trading volume, in szCcy  
> confirm | String | The state of candlesticks.0 represents that it is uncompleted, 1 represents that it is completed.  
The data returned will be arranged in an array like this: [ts,o,h,l,c,vol,confirm]

---

# WebSocket公共频道

* 实盘地址: `wss://ws.okx.com:8443/ws/v5/business`  
  * 模拟盘地址: `wss://wspap.okx.com:8443/ws/v5/business`

### 深度频道 

获取Spread深度数据。可用频道有：

  * `sprd-bbo-tbt`: 首次推1档快照数据，以后定量推送，每10毫秒当1档快照数据有变化推送一次1档数据
  * `sprd-books5`: 首次推5档快照数据，以后定量推送，每100毫秒当5档快照数据有变化推送一次5档数据
  * `sprd-books-l2-tbt`: 首次推400档快照数据，以后增量推送，每10毫秒推送一次变化的数据
  * 单个连接、交易产品维度，深度频道的推送顺序固定为：sprd-bbo-tbt -> sprd-books-l2-tbt -> sprd-books5

#### URL Path

/ws/v5/business

> 请求示例：sprd-books5
    
    
    {
      "id": "1512",
      "op": "subscribe",
      "args": [
        {
          "channel": "sprd-books5",
          "sprdId": "BTC-USDT_BTC-USDT-SWAP"
        }
      ]
    }
    
    
    
    
    import asyncio
    from okx.websocket.WsPublicAsync import WsPublicAsync
    
    def callbackFunc(message):
        print(message)
    
    async def main():
        ws = WsPublicAsync(url="wss://wspap.okx.com:8443/ws/v5/business")
        await ws.start()
        args = [
            {
              "channel": "sprd-books5",
              "sprdId": "BTC-USDT_BTC-USDT-SWAP"
            }
        ]
    
        await ws.subscribe(args, callback=callbackFunc)
        await asyncio.sleep(10)
    
        await ws.unsubscribe(args, callback=callbackFunc)
        await asyncio.sleep(10)
    
    asyncio.run(main())
    
    

> 请求示例：sprd-books-l2-tbt
    
    
    {
      "id": "1512",
      "op": "subscribe",
      "args": [
        {
          "channel": "sprd-books-l2-tbt",
          "sprdId": "BTC-USDT_BTC-USDT-SWAP"
        }
      ]
    }
    
    
    
    import asyncio
    from okx.websocket.WsPublicAsync import WsPublicAsync
    
    def callbackFunc(message):
        print(message)
    
    async def main():
        ws = WsPublicAsync(url="wss://wspap.okx.com:8443/ws/v5/business")
        await ws.start()
        args = [
            {
              "channel": "sprd-books-l2-tbt",
              "sprdId": "BTC-USDT_BTC-USDT-SWAP"
            }
        ]
    
        await ws.subscribe(args, callback=callbackFunc)
        await asyncio.sleep(10)
    
        await ws.unsubscribe(args, callback=callbackFunc)
        await asyncio.sleep(10)
    
    asyncio.run(main())
    
    

#### 请求参数

参数 | 类型 | 是否必须 | 描述  
---|---|---|---  
id | String | 否 | 消息的唯一标识。  
用户提供，返回参数中会返回以便于找到相应的请求。  
字母（区分大小写）与数字的组合，可以是纯字母、纯数字且长度必须要在1-32位之间。  
op | String | 是 | 操作  
`subscribe`  
`unsubscribe`  
args | Array of objects | 是 | 请求订阅的频道列表  
`sprd-bbo-tbt`  
`sprd-books5`  
`sprd-books-l2-tbt`  
> channel | String | 是 | 频道名  
> sprdId | String | 是 | spread ID  
  
> 返回示例：sprd-books5
    
    
    {
      "id": "1512",
      "event": "subscribe",
      "arg": {
        "channel": "sprd-books5",
        "sprdId": "BTC-USDT_BTC-USDT-SWAP"
      },
      "connId": "a4d3ae55"
    }
    
    

> 返回示例：sprd-books-l2-tbt
    
    
    {
      "id": "1512",
       "event":"subscribe",
       "arg":{
          "channel":"sprd-books-l2-tbt",
          "sprdId":"BTC-USDT_BTC-USDT-SWAP"
       },
       "connId":"214fdd24"
    }
    

> 失败示例
    
    
    {
      "id": "1512",
      "event": "error",
      "code": "60012",
      "msg": "Invalid request: {\"op\": \"subscribe\", \"args\":[{ \"channel\" : \"sprd-books5\", \"sprdId\" : \"BTC-USD_BTC-USD-191227\"}]}",
      "connId": "a4d3ae55"
    }
    
    

#### 返回参数

参数 | 类型 | 是否必须 | 描述  
---|---|---|---  
id | String | 否 | 消息的唯一标识  
event | String | 是 | 事件  
`subscribe`  
`unsubscribe`  
`error`  
arg | Object | 否 | 订阅的频道  
`sprd-bbo-tbt`  
`sprd-books5`  
`sprd-books-l2-tbt`  
> channel | String | 是 | 频道名  
> sprdId | String | 是 | spread ID  
msg | String | 否 | 错误消息  
code | String | 否 | 错误码  
connId | String | 是 | WebSocket连接ID  
  
> 推送示例：sprd-books5
    
    
    {
      "arg": {
        "channel": "sprd-books5",
        "sprdId": "BTC-USDT_BTC-USDT-SWAP"
      },
      "data": [
        {
          "asks": [
            ["111.06","55154","2"],
            ["111.07","53276","2"],
            ["111.08","72435","2"],
            ["111.09","70312","2"],
            ["111.1","67272","2"]],
          "bids": [
            ["111.05","57745","2"],
            ["111.04","57109","2"],
            ["111.03","69563","2"],
            ["111.02","71248","2"],
            ["111.01","65090","2"]],
          "ts": "1670324386802",
          "seqId":1724294007352168320
        }
      ]
    }
    
    

> 推送示例：sprd-books-l2-tbt
    
    
    {
       "arg":{
          "channel":"sprd-books-l2-tbt",
          "sprdId":"BTC-USDT_BTC-USDT-SWAP"
       },
       "action":"snapshot",
       "data":[
          {
             "asks":[
                ["1.9","1.1","3"],
                ["2.5","0.9","1"],
                ["3.2","4.921","1"],
                ["4.8","0.165","1"],
                ["5.2","4.921","1"]
              ......
             ],
             "bids":[
                ["1.8","0.165","1"],
                ["0.6","0.2","2"],
                ["0","23.49","1"],
                ["-0.1","1","1"],
                ["-0.6","1","1"],
                ["-3.9","4.921","1"]
                ......
             ],
             "ts":"1724391380926",
             "checksum":-1285595583,
             "prevSeqId":-1,
             "seqId":1724294007352168320
          }
       ]
    }
    

#### 推送数据参数

参数名 | 类型 | 描述  
---|---|---  
arg | Object | 订阅成功的频道  
> channel | String | 频道名  
> sprdId | String | Spread ID  
action | String | 推送数据动作，增量推送数据还是全量推送数据  
`snapshot`：全量  
`update`：增量  
data | Array of objects | 订阅的数据  
> asks | Array of strings | 卖方深度  
> bids | Array of strings | 买方深度  
> ts | String | 数据更新时间戳，Unix时间戳的毫秒数格式，如 1597026383085  
> checksum | Integer | 检验和 （下方注解）。仅适用 `sprd-books-l2-tbt`  
> prevSeqId | Integer | 上一个推送的序列号。仅适用 `sprd-books-l2-tbt`  
> seqId | Integer | 推送的序列号 （下方注解）  
asks和bids值数组举例说明： ["411.8", "10", "4"]   
\- 411.8为深度价格   
\- 10为此价格的数量 （单位为szCcy)   
\- 4为此价格的订单数量   

#### 序列号

`seqId`是交易所行情的一个序号。如果用户通过多个websocket连接同一频道，收到的序列号会是相同的。每个`sprdId`对应一套。用户可以使用在增量推送频道的`prevSeqId`和`seqId`来构建消息序列。这将允许用户检测数据包丢失和消息的排序。正常场景下`seqId`的值大于`prevSeqId`。新消息中的`prevSeqId`与上一条消息的`seqId`匹配。最小序列号值为0，除了快照消息的`prevSeqId`为-1。  

异常情况：  
1\. 如果一段时间内没有深度更新，OKX将发一条消息`'asks': [], 'bids': []`以通知用户连接是正常的。推送的`seqId`跟上一条信息的一样，`prevSeqId`等于`seqId`。 2\. 序列号可能由于维护而重置，在这种情况下，用户将收到一条`seqId`小于`prevSeqId`的增量消息。随后的消息将遵循常规的排序规则。

##### 示例

  1. 快照推送：`prevSeqId = -1`，`seqId = 10`
  2. 增量推送1（正常更新）：`prevSeqId = 10`，`seqId = 15`
  3. 增量推送2（无更新）：`prevSeqId = 15`，`seqId = 15`
  4. 增量推送3（序列重置）：`prevSeqId = 15`，`seqId = 3`
  5. 增量推送4（正常更新）：`prevSeqId = 3`，`seqId = 5`

#### Checksum机制

此机制可以帮助用户校验深度数据的准确性。

##### 深度合并

用户订阅增量推送深度频道成功后，首先获取初始全量深度数据，当获取到增量推送数据后，更新本地全量深度数据。 

  1. 如果有相同价格，则比较数量；数量为0删除此深度，数量有变化则替换此数据。
  2. 如果没有相同价格，则按照价格优劣排序（bid为价格降序，ask为价格升序），将深度信息插入到全量数据中

##### 计算校验和

先用深度合并后前25档bids和asks组成一个字符串（其中ask和bid中的价格和数量以冒号连接），再计算其crc32值（32位有符号整型）。 

### 公共成交数据频道 

订阅`sprd-public-trades`获取最近的成交数据，有成交数据就推送，每次推送仅包含一条成交数据。

#### URL Path

/ws/v5/business

> 请求示例
    
    
    {
      "id": "1512",
      "op": "subscribe",
      "args": [
        {
          "channel": "sprd-public-trades",
          "sprdId": "BTC-USDT_BTC-USDT-SWAP"
        }
      ]
    }
    
    
    
    
    import asyncio
    from okx.websocket.WsPublicAsync import WsPublicAsync
    
    def callbackFunc(message):
        print(message)
    
    async def main():
        ws = WsPublicAsync(url="wss://wspap.okx.com:8443/ws/v5/business")
        await ws.start()
        args = [
            {
              "channel": "sprd-public-trades",
              "sprdId": "BTC-USDT_BTC-USDT-SWAP"
            }
        ]
    
        await ws.subscribe(args, callback=callbackFunc)
        await asyncio.sleep(10)
    
        await ws.unsubscribe(args, callback=callbackFunc)
        await asyncio.sleep(10)
    
    asyncio.run(main())
    
    

#### 请求参数

参数 | 类型 | 是否必须 | 描述  
---|---|---|---  
id | String | 否 | 消息的唯一标识。  
用户提供，返回参数中会返回以便于找到相应的请求。  
字母（区分大小写）与数字的组合，可以是纯字母、纯数字且长度必须要在1-32位之间。  
op | String | 是 | 操作  
`subscribe`  
`unsubscribe`  
args | Array of objects | 是 | 请求订阅的频道列表  
> channel | String | 是 | 频道名  
`sprd-public-trades`  
> sprdId | String | 是 | Spread ID  
  
> 成功返回示例
    
    
    {
      "id": "1512",
      "event": "subscribe",
      "arg": {
          "channel": "sprd-public-trades",
          "sprdId": "BTC-USDT_BTC-USDT-SWAP"
      },
      "connId": "a4d3ae55"
    }
    
    

> 失败返回示例
    
    
    {
      "id": "1512",
      "event": "error",
      "code": "60012",
      "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{ \"channel\" : \"sprd-public-trades\", \"instId\" : \"BTC-USD-191227\"}]}",
      "connId": "a4d3ae55"
    }
    
    

#### 返回参数

参数 | 类型 | 是否必须 | 描述  
---|---|---|---  
id | String | 否 | 消息的唯一标识  
event | String | 是 | 事件  
`subscribe`  
`unsubscribe`  
`error`  
arg | Object | 否 | 订阅的频道  
> channel | String | 是 | 频道名  
> sprdId | String | 是 | Spread ID  
code | String | 否 | 错误码  
msg | String | 否 | 错误消息  
connId | String | 是 | WebSocket连接ID  
  
> 推送示例
    
    
    {
        "arg": {
            "channel": "sprd-public-trades",
            "sprdId": "BTC-USDT_BTC-USDT-SWAP"
        },
        "data": [
            {
                "sprdId": "BTC-USDT_BTC-USDT-SWAP",
                "tradeId": "2499206329160695808",
                "px": "-10",
                "sz": "0.001",
                "side": "sell",
                "ts": "1726801105519"
            }
        ]
    }
    
    

#### 推送数据参数

参数名 | 类型 | 描述  
---|---|---  
arg | Object | 订阅成功的频道  
> channel | String | 频道名  
> sprdId | String | spread ID  
data | Array of objects | 订阅的数据  
> sprdId | String | spread ID  
> tradeId | String | 交易 ID  
> px | String | 成交价格  
sz | String | 成交数量  
对于币币交易，成交数量的单位为交易货币  
对于交割、永续以及期权，单位为张。  
> side | String | 成交方向   
`buy`   
`sell`  
> ts | String | 成交时间，Unix时间戳的毫秒数格式，如 1597026383085  
  
### 行情频道 

订阅`sprd-tickers`获取产品的最新成交价、买一价、卖一价及数量等信息。 最快100ms推送一次，没有触发事件时最慢1s推送一次，触发推送的事件有：成交、买一卖一发生变动。

#### URL Path

/ws/v5/business

> 请求示例
    
    
    {
      "id": "1512",
      "op": "subscribe",
      "args": [
        {
          "channel": "sprd-tickers",
          "sprdId": "BTC-USDT_BTC-USDT-SWAP"
        }
      ]
    }
    
    
    
    
    import asyncio
    from okx.websocket.WsPublicAsync import WsPublicAsync
    
    def callbackFunc(message):
        print(message)
    
    async def main():
        ws = WsPublicAsync(url="wss://wspap.okx.com:8443/ws/v5/business")
        await ws.start()
        args = [
            {
              "channel": "sprd-tickers",
              "sprdId": "BTC-USDT_BTC-USDT-SWAP"
            }
        ]
    
        await ws.subscribe(args, callback=callbackFunc)
        await asyncio.sleep(10)
    
        await ws.unsubscribe(args, callback=callbackFunc)
        await asyncio.sleep(10)
    
    asyncio.run(main())
    
    

#### 请求参数

参数 | 类型 | 是否必须 | 描述  
---|---|---|---  
id | String | 否 | 消息的唯一标识。  
用户提供，返回参数中会返回以便于找到相应的请求。  
字母（区分大小写）与数字的组合，可以是纯字母、纯数字且长度必须要在1-32位之间。  
op | String | 是 | 操作  
`subscribe`  
`unsubscribe`  
args | Array of objects | 是 | 请求订阅的频道列表  
> channel | String | 是 | 频道名  
`sprd-tickers`  
> sprdId | String | 是 | spread ID  
  
> 成功返回示例
    
    
    {
      "id": "1512",
      "event": "subscribe",
      "arg": {
        "channel": "sprd-tickers",
        "sprdId": "BTC-USDT_BTC-USDT-SWAP"
      },
      "connId": "a4d3ae55"
    }
    
    

> 失败返回示例
    
    
    {
      "id": "1512",
      "event": "error",
      "code": "60012",
      "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{ \"channel\" : \"sprd-tickers\", \"instId\" : \"LTC-USD-200327\"}]}",
      "connId": "a4d3ae55"
    }
    
    

#### 返回参数

参数 | 类型 | 是否必须 | 描述  
---|---|---|---  
id | String | 否 | 消息的唯一标识  
event | String | 是 | 事件  
`subscribe`  
`unsubscribe`  
`error`  
arg | Object | 否 | 订阅的频道  
> channel | String | 是 | 频道名  
> sprdId | String | 是 | Spread ID  
code | String | 否 | 错误码  
msg | String | 否 | 错误消息  
connId | String | 是 | WebSocket连接ID  
  
> 推送示例
    
    
    {
        "arg": {
            "channel": "sprd-tickers",
            "sprdId": "BTC-USDT_BTC-USDT-SWAP"
        },
        "data": [
            {
                "sprdId": "BTC-USDT_BTC-USDT-SWAP",
                "last": "4",
                "lastSz": "0.01",
                "askPx": "19.7",
                "askSz": "5.79",
                "bidPx": "5.9",
                "bidSz": "5.79",
                "open24h": "-7",
                "high24h": "19.6",
                "low24h": "-7",
                "vol24h": "9.87",
                "ts": "1715247061026"
            }
        ]
    }
    
    

#### 推送数据参数

参数名 | 类型 | 描述  
---|---|---  
arg | Object | 订阅成功的频道  
> channel | String | 频道名  
> sprdId | String | spread ID  
data | Array of objects | 订阅的数据  
> sprdId | String | spread ID  
> last | String | 最新成交价  
> lastSz | String | 最新成交的数量  
> askPx | String | 卖一价  
> askSz | String | 卖一价对应的量  
> bidPx | String | 买一价  
> bidSz | String | 买一价对应的数量  
> open24h | String | 24小时开盘价  
> high24h | String | 24小时最高价  
> low24h | String | 24小时最低价  
> vol24h | String | 24小时交易量，单元为交易货币或美元  
> ts | String | 数据产生时间，Unix时间戳的毫秒数格式，如 1597026383085  
vol24h  
对于现货/U本位合约价差交易产品，以及U本位合约价差交易产品，交易量以交易货币为单位；对于币本位合约价差交易产品，交易量以USD为单位。 

### K线频道 

该频道使用业务WebSocket，不需鉴权。

获取K线数据，推送频率最快是间隔1秒推送一次数据。

#### URL Path

/ws/v5/business

> 请求示例
    
    
    {
       "id": "1512",
       "op":"subscribe",
       "args":[
          {
             "channel":"sprd-candle1D",
             "sprdId":"BTC-USDT_BTC-USDT-SWAP"
          }
       ]
    }
    
    
    
    
    import asyncio
    from okx.websocket.WsPublicAsync import WsPublicAsync
    
    def callbackFunc(message):
        print(message)
    
    async def main():
        ws = WsPublicAsync(url="wss://wspap.okx.com:8443/ws/v5/business")
        await ws.start()
        args = [
          {
             "channel":"sprd-candle1D",
             "sprdId":"BTC-USDT_BTC-USDT-SWAP"
          }
        ]
    
        await ws.subscribe(args, callback=callbackFunc)
        await asyncio.sleep(10)
    
        await ws.unsubscribe(args, callback=callbackFunc)
        await asyncio.sleep(10)
    
    asyncio.run(main())
    
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
id | String | 否 | 消息的唯一标识。  
用户提供，返回参数中会返回以便于找到相应的请求。  
字母（区分大小写）与数字的组合，可以是纯字母、纯数字且长度必须要在1-32位之间。  
op | String | 是 | 操作  
`subscribe`   
`unsubscribe`  
args | Array of objects | 是 | 请求订阅的频道列表  
> channel | String | 是 | 频道名  
`sprd-candle3M` `sprd-candle1M`   
`sprd-candle1W`   
`sprd-candle1D` `sprd-candle2D` `sprd-candle3D` `sprd-candle5D`   
`sprd-candle12H` `sprd-candle6H` `sprd-candle4H` `sprd-candle2H` `sprd-candle1H`   
`sprd-candle30m` `sprd-candle15m` `sprd-candle5m` `sprd-candle3m` `sprd-candle1m`   
`sprd-candle3Mutc` `sprd-candle1Mutc` `sprd-candle1Wutc` `sprd-candle1Dutc` `sprd-candle2Dutc` `sprd-candle3Dutc` `sprd-candle5Dutc` `sprd-candle12Hutc` `sprd-candle6Hutc`  
> sprdId | String | 是 | Spread ID  
  
> 成功返回示例
    
    
    {
      "id": "1512",
      "event": "subscribe",
      "arg": {
        "channel": "sprd-candle1D",
        "sprdId": "BTC-USDT_BTC-USDT-SWAP"
      },
      "connId": "a4d3ae55"
    }
    
    

> 失败返回示例
    
    
    {
      "id": "1512",
      "event": "error",
      "code": "60012",
      "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{ \"channel\" : \"sprd-candle1D\", \"instId\" : \"BTC-USD-191227\"}]}",
      "connId": "a4d3ae55"
    }
    
    

#### 返回参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
id | String | 否 | 消息的唯一标识  
event | String | 是 | 事件   
`subscribe`   
`unsubscribe`   
`error`  
arg | Object | 否 | 订阅的频道  
channel | String | 是 | 频道名  
sprdId | String | 是 | Spread ID  
code | String | 否 | 错误码  
msg | String | 否 | 错误消息  
  
> 推送示例
    
    
    {
      "arg": {
        "channel": "sprd-candle1D",
        "sprdId": "BTC-USDT_BTC-USD-SWAP"
      },
      "data": [
        [
          "1597026383085",
          "8533.02",
          "8553.74",
          "8527.17",
          "8548.26",
          "45247",
          "0"
        ]
      ]
    }
    
    

#### 推送数据参数

参数名 | 类型 | 描述  
---|---|---  
arg | Object | 订阅成功的频道  
> channel | String | 频道名  
> sprdId | String | Spread ID  
data | Array of Arrays | 订阅的数据  
> ts | String | 开始时间，Unix时间戳的毫秒数格式，如 1597026383085  
> o | String | 开盘价格  
> h | String | 最高价格  
> l | String | 最低价格  
> c | String | 收盘价格  
> vol | String | 交易量  
> confirm | String | K线状态   
`0`：K线未完结   
`1`：K线已完结  
返回值数组顺序分别为是： [ts,o,h,l,c,vol,confirm]