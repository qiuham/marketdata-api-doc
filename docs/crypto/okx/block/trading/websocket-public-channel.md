---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#block-trading-websocket-public-channel
anchor_id: block-trading-websocket-public-channel
api_type: WebSocket
updated_at: 2026-07-16 19:20:46.228762
---

# WebSocket Public Channel

### Public structure block trades channel

Retrieve the recent block trades data in OKX. All the legs in the same block trade are included in the same update. The data will be pushed 15 minutes after the block trade execution.

#### URL Path

/ws/v5/business

> Request Example
    
    
    {
      "id": "1512",
      "op": "subscribe",
      "args": [
        {
          "channel": "public-struc-block-trades"
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
              "channel": "public-struc-block-trades"
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
`public-struc-block-trades`  
  
> Successful Response Example
    
    
    {
      "id": "1512",
      "event": "subscribe",
      "arg": {
        "channel": "public-struc-block-trades"
      },
      "connId": "a4d3ae55"
    }
    

> Failure Response Example
    
    
    {
      "id": "1512",
      "event": "error",
      "code": "60012",
      "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{ \"channel\" : \"public-struc-block-trades\""}]}",
      "connId": "a4d3ae55"
    }
    

#### Response parameters

Parameter | Type | Required | Description  
---|---|---|---  
id | String | No | Unique identifier of the message  
event | String | Yes | Operation  
`subscribe`  
`unsubscribe`  
`error`  
arg | Object | No | Subscribed channel  
> channel | String | Yes | Channel name  
`public-struc-block-trades`  
code | String | No | Error code  
msg | String | No | Error message  
connId | String | Yes | WebSocket connection ID  
  
> Push Data Example
    
    
    {
        "arg":{
            "channel":"public-struc-block-trades"
        },
        "data":[
            {
    
                "cTime":"1608267227834",
                "blockTdId":"1802896",
                "groupId":"",
                "legs":[
                    {
                        "px":"0.323",
                        "sz":"25.0",
                        "instId":"BTC-USD-20220114-13250-C",
                        "side":"sell",
                        "tradeId":"15102"
                    },
                    {
                        "px":"0.666",
                        "sz":"25",
                        "instId":"BTC-USD-20220114-21125-C",
                        "side":"buy",
                        "tradeId":"15103"
                    }
                ]
            }
        ]
    }
    

#### Push data parameters

**Parameters** | **Types** | **Description**  
---|---|---  
arg | Object | Successfully subscribed channel  
> channel | String | Channel name  
data | Array of objects | Subscribed data  
> cTime | String | The time the trade was executed. Unix timestamp in milliseconds.  
> blockTdId | String | Block trade ID.  
> groupId | String | Group RFQ ID  
Only applicable to group RFQ, return "" for normal RFQ  
> legs | Array of objects | Legs of trade  
>> instId | String | Instrument ID, e.g. BTC-USDT-SWAP  
>> px | String | The price the leg executed  
>> sz | String | Trade quantity   
For spot trading, the unit is base currency  
For `FUTURES`/`SWAP`/`OPTION`, the unit is contract.  
>> side | String | The direction of the leg from the Takers perspective. Valid value can be `buy` or `sell`.  
>> tradeId | String | Last traded ID.  
Group RFQ introduction  
  
1\. Add new response parameter groupId, facilitating clients to map subaccount execution to group RFQ. Only applicable to group RFQ, return "" for normal RFQ.  
2\. Data return by this endpoint should be at **parent RFQ level** regardless of the subaccounts allocation. blockTdId and tradeId will be empty.  Mapping blockTdId to rfqId  
  
For normal RFQs, each `blockTdId` has a 1:1 relationship with an `rfqId`. For Group RFQs, one `rfqId` may correspond to multiple `blockTdId`s.  
  
This channel does not include `rfqId` directly. Users who are counterparties to the trade (taker and executing maker) can subscribe to the private [Structure block trades channel](/docs-v5/en/#block-trading-websocket-private-channel-structure-block-trades-channel), which provides both `rfqId` and `blockTdId`, enabling cross-referencing between the two channels. 

### Public block trades channel

Retrieve the recent block trades data by individual legs. Each leg in a block trade is pushed in a separate update. The data will be pushed 15 minutes after the block trade execution.

#### URL Path

/ws/v5/business

> Request Example
    
    
    {
      "id": "1512",
      "op": "subscribe",
      "args": [
        {
          "channel": "public-block-trades",
          "instId": "BTC-USDT-SWAP"
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
              "channel": "public-block-trades",
              "instId": "BTC-USDT-SWAP"
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
`public-block-trades`  
> instId | String | Yes | Instrument ID, e.g. BTC-USDT-SWAP.  
  
> Successful Response Example
    
    
    {
      "id": "1512",
      "event": "subscribe",
      "arg": {
        "channel": "public-block-trades",
        "instId": "BTC-USDT-SWAP",
        "connId": "a4d3ae55"
      }
    }
    

> Failure Response Example
    
    
    {
      "id": "1512",
      "event": "error",
      "code": "60012",
      "msg": "Invalid request: {\"op\": \"subscribe\", \"args\":[{ \"channel\" : \"public-block-trades\""}]}",
      "connId": "a4d3ae55"
    }
    

#### Response parameters

Parameter | Type | Required | Description  
---|---|---|---  
id | String | No | Unique identifier of the message  
event | String | Yes | Operation  
`subscribe`  
`unsubscribe`  
`error`  
arg | Object | No | Subscribed channel  
> channel | String | Yes | Channel name  
`public-block-trades`  
> instId | String | Yes | Instrument ID, e.g. BTC-USDT-SWAP.  
code | String | No | Error code  
msg | String | No | Error message  
connId | String | Yes | WebSocket connection ID  
  
> Push Data Example
    
    
    {
       "arg":{
          "channel":"public-block-trades",
          "instId":"BTC-USD-231020-5000-P"
       },
       "data":[
          {
             "fillVol":"5",
             "fwdPx":"26808.16",
             "groupId":"",
             "idxPx":"27222.5",
             "instId":"BTC-USD-231020-5000-P",
             "markPx":"0.0022406326071111",
             "px":"0.0048",
             "side":"buy",
             "sz":"1",
             "tradeId":"633971452580106242",
             "ts":"1697422572972"
          }
       ]
    }
    

#### Push data parameters

**Parameters** | **Types** | **Description**  
---|---|---  
arg | Object | Successfully subscribed channel  
> channel | String | Channel name  
> instId | String | Instrument ID, e.g. BTC-USDT-SWAP.  
data | Array of objects | Information of the public trade object.  
> instId | String | Instrument ID, e.g. BTC-USDT-SWAP.  
> tradeId | String | Trade ID, generated by counter.  
> px | String | The price the leg executed.  
> sz | String | Trade quantity   
For spot trading, the unit is base currency  
For `FUTURES`/`SWAP`/`OPTION`, the unit is contract.  
> side | String | Trade direction, buy, sell, from taker perspective.  
> fillVol | String | Implied volatility   
Only applicable to `OPTION`  
> fwdPx | String | Forward price   
Only applicable to options  
> idxPx | String | Index price   
Applicable to `FUTURES`, `SWAP`, `OPTION`  
> markPx | String | Mark price   
Applicable to `FUTURES`, `SWAP`, `OPTION`  
> groupId | String | Group RFQ ID  
Only applicable to group RFQ, return "" for normal RFQ  
> ts | String | Filled time, Unix timestamp format in milliseconds, e.g. 1597026383085.  
Group RFQ introduction  
  
1\. Add new response parameter groupId, facilitating clients to map subaccount execution to group RFQ. Only applicable to group RFQ, return "" for normal RFQ.  
2\. Data return by this endpoint should be at **child RFQ execution level** but split into a single leg. tradeId will be populated.  

### Block tickers channel

Retrieve the latest block trading volume in the last 24 hours.

The data will be pushed when triggered by transaction execution event. In addition, it will also be pushed in 5 minutes interval according to subscription granularity.

#### URL Path

/ws/v5/business

> Request Example
    
    
    {
        "id": "1512",
        "op": "subscribe",
        "args": [{
            "channel": "block-tickers",
            "instId": "BTC-USDT"
        }]
    }
    
    
    
    import asyncio
    from okx.websocket.WsPublicAsync import WsPublicAsync
    
    def callbackFunc(message):
        print(message)
    
    async def main():
        ws = WsPublicAsync(url="wss://wspap.okx.com:8443/ws/v5/business")
        await ws.start()
        args = [{
            "channel": "block-tickers",
            "instId": "BTC-USDT"
        }]
    
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
`block-tickers`  
> instId | String | Yes | Instrument ID e.g. BTC-USDT-SWAP  
  
> Successful Response Example
    
    
    {
      "id": "1512",
      "event": "subscribe",
      "arg": {
        "channel": "block-tickers",
        "instId": "LTC-USD-200327"
      },
      "connId": "a4d3ae55"
    }
    

> Failure Response Example
    
    
    {
      "id": "1512",
      "event": "error",
      "code": "60012",
      "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{ \"channel\" : \"block-tickers\", \"instId\" : \"LTC-USD-200327\"}]}",
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
`block-tickers`  
> instId | String | Yes | Instrument ID  
code | String | No | Error code  
msg | String | No | Error message  
connId | String | Yes | WebSocket connection ID  
  
> Push Data Example
    
    
    {
        "arg": {
            "channel": "block-tickers"
        },
        "data": [
            {
                "instType": "SWAP",
                "instId": "LTC-USD-SWAP",
                "volCcy24h": "0",
                "vol24h": "0",
                "ts": "1597026383085"
            }
        ]
    }
    

#### Push data parameters

**Parameter** | **Type** | **Description**  
---|---|---  
arg | Object | Successfully subscribed channel  
> channel | String | Channel name  
> instId | String | Instrument ID  
data | Array of objects | Subscribed data  
> instId | String | Instrument ID  
> instType | String | Instrument type  
> volCcy24h | String | 24h trading volume, with a unit of `currency`.   
If it is a `derivatives` contract, the value is the number of base currency.   
If it is `SPOT`/`MARGIN`, the value is the quantity in quote currency.  
> vol24h | String | 24h trading volume, with a unit of `contract`.   
If it is a `derivatives` contract, the value is the number of contracts.   
If it is `SPOT`/`MARGIN`, the value is the quantity in base currency.  
> ts | String | Block ticker data generation time, Unix timestamp format in milliseconds, e.g. `1597026383085`

---

# WebSocket 公共频道

### 公共大宗交易频道 

获取欧易的最新大宗交易信息。同一大宗交易中的所有腿都包含在同一更新中。数据将在大宗交易执行15分钟后被推送。

#### URL Path

/ws/v5/business

> 请求示例
    
    
    {
      "id": "1512",
      "op": "subscribe",
      "args": [
        {
          "channel": "public-struc-block-trades"
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
              "channel": "public-struc-block-trades"
            }
        ]
    
        await ws.subscribe(args, callback=callbackFunc)
        await asyncio.sleep(10)
    
        await ws.unsubscribe(args, callback=callbackFunc)
        await asyncio.sleep(10)
    
    asyncio.run(main())
    

#### 请求参数

参数名 | 类型 | 是否必填 | 描述  
---|---|---|---  
id | String | 否 | 消息的唯一标识。  
用户提供，返回参数中会返回以便于找到相应的请求。  
字母（区分大小写）与数字的组合，可以是纯字母、纯数字且长度必须要在1-32位之间。  
op | String | 是 | 操作  
`subscribe`  
`unsubscribe`  
  
args | Array of objects | 是 | 请求订阅的频道列表  
> channel | String | 是 | 频道名  
`public-struc-block-trades`  
  
> 成功返回示例
    
    
    {
      "id": "1512",
      "event": "subscribe",
      "arg": {
        "channel": "public-struc-block-trades"
      },
      "connId": "a4d3ae55"
    }
    

> 失败返回示例
    
    
    {
      "id": "1512",
      "event": "error",
      "code": "60012",
      "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{ \"channel\" : \"public-struc-block-trades\""}]}",
      "connId": "a4d3ae55"
    }
    

#### 返回参数

参数名 | 类型 | 是否必填 | 描述  
---|---|---|---  
id | String | 否 | 消息的唯一标识  
event | String | 是 | 操作  
`subscribe`  
`unsubscribe`  
`error`  
arg | Object | 否 | 订阅的频道  
> channel | String | 是 | 频道名  
`public-struc-block-trades`  
code | String | 否 | 错误码  
msg | String | 否 | 错误消息  
connId | String | 是 | WebSocket连接ID  
  
> 推送示例
    
    
    {
        "arg":{
            "channel":"public-struc-block-trades"
        },
        "data":[
            {
    
                "cTime":"1608267227834",
                "blockTdId":"1802896",
                "groupId":"",
                "legs":[
                    {
                        "px":"0.323",
                        "sz":"25.0",
                        "instId":"BTC-USD-20220114-13250-C",
                        "side":"sell",
                        "tradeId":"15102"
                    },
                    {
                        "px":"0.666",
                        "sz":"25",
                        "instId":"BTC-USD-20220114-21125-C",
                        "side":"buy",
                        "tradeId":"15103"
                    }
                ]
            }
        ]
    }
    

#### 推送数据参数

**参数名** | **类型** | **描述**  
---|---|---  
arg | Object | 订阅成功的频道  
> channel | String | 频道名  
data | Array of objects | 订阅的数据  
> cTime | String | 执行创建的时间戳，Unix 时间戳格式，以毫秒为单位。  
> blockTdId | String | 大宗交易ID  
> groupId | String | 组合询价单ID  
只适用于组合询价单，普通询价单返回 ""  
> legs | Array of objects | 组合交易  
>> instId | String | 产品名Id  
>> px | String | 成交价格  
>> sz | String | 成交数量  
对于币币交易，成交数量的单位为交易货币  
对于交割、永续以及期权，单位为张。  
>> side | String | 询价单方向，从 Taker的视角看  
>> tradeId | String | 最新成交Id  
组合询价单介绍  
  
1\. 新增返回参数 groupId，协助用户将子账户执行映射到组合询价单。仅适用于组合询价单，对普通询价单返回 ""。  
2\. 该接口返回的交易数据应为父级询价单，而不是子级询价单，与子账户分配无关，blockTdId 及 tradeId 为空  blockTdId 与 rfqId 的对应关系  
  
对于普通询价单，每个 `blockTdId` 与一个 `rfqId` 一一对应。对于组合询价单，一个 `rfqId` 可能对应多个 `blockTdId`。  
  
本频道不直接返回 `rfqId`。作为交易对手方（询价方或成交的报价方）的用户，可订阅私有[大宗交易频道](/docs-v5/zh/#block-trading-websocket-private-channel-structure-block-trades-channel)，该频道同时包含 `rfqId` 和 `blockTdId`，可用于两个频道之间的关联查询。 

### 公共大宗交易单腿交易频道 

获取欧易的最新大宗交易单腿交易信息。大宗交易中的每条腿都在单独的更新中推送。数据将在大宗交易执行15分钟后被推送。

#### URL Path

/ws/v5/business

> 请求示例
    
    
    {
      "id": "1512",
      "op": "subscribe",
      "args": [
        {
          "channel": "public-block-trades",
          "instId": "BTC-USDT-SWAP"
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
              "channel": "public-block-trades",
              "instId": "BTC-USDT-SWAP"
            }
        ]
    
        await ws.subscribe(args, callback=callbackFunc)
        await asyncio.sleep(10)
    
        await ws.unsubscribe(args, callback=callbackFunc)
        await asyncio.sleep(10)
    
    asyncio.run(main())
    

#### 请求参数

参数名 | 类型 | 是否必填 | 描述  
---|---|---|---  
id | String | 否 | 消息的唯一标识。  
用户提供，返回参数中会返回以便于找到相应的请求。  
字母（区分大小写）与数字的组合，可以是纯字母、纯数字且长度必须要在1-32位之间。  
op | String | 是 | 操作  
`subscribe`  
`unsubscribe`  
  
args | Array of objects | 是 | 请求订阅的频道列表  
> channel | String | 是 | 频道名  
`public-block-trades`  
> instId | String | 是 | 产品 ID, 如 `BTC-USDT-SWAP`  
  
> 成功返回示例
    
    
    {
      "id": "1512",
      "event": "subscribe",
      "arg": {
        "channel": "public-block-trades",
        "instId": "BTC-USDT-SWAP"
      },
      "connId": "a4d3ae55"
    }
    

> 失败返回示例
    
    
    {
      "id": "1512",
      "event": "error",
      "code": "60012",
      "msg": "Invalid request: {\"op\": \"subscribe\", \"args\":[{ \"channel\" : \"public-block-trades\""}]}",
      "connId": "a4d3ae55"
    }
    

#### 返回参数

参数名 | 类型 | 是否必需 | 描述  
---|---|---|---  
id | String | 否 | 消息的唯一标识  
event | String | 是 | 操作  
`subscribe`  
`unsubscribe`  
`error`  
arg | Object | 否 | 订阅的频道  
> channel | String | 是 | 频道名  
`public-block-trades`  
> instId | String | 是 | 产品 ID, 如 `BTC-USDT-SWAP`  
code | String | 否 | 错误码  
msg | String | 否 | 错误消息  
connId | String | 是 | WebSocket连接ID  
  
> 推送示例
    
    
    {
       "arg":{
          "channel":"public-block-trades",
          "instId":"BTC-USD-231020-5000-P"
       },
       "data":[
          {
             "fillVol":"5",
             "fwdPx":"26808.16",
             "groupId":"",
             "idxPx":"27222.5",
             "instId":"BTC-USD-231020-5000-P",
             "markPx":"0.0022406326071111",
             "px":"0.0048",
             "side":"buy",
             "sz":"1",
             "tradeId":"633971452580106242",
             "ts":"1697422572972"
          }
       ]
    }
    

#### 推送数据参数

**参数名** | **类型** | **描述**  
---|---|---  
arg | Object | 订阅成功的频道  
> channel | String | 频道名  
> instId | String | 产品 ID, 如 `BTC-USDT-SWAP`  
data | Array of objects | 公共大宗交易单腿交易信息  
> instId | String | 产品 ID, 如 `BTC-USDT-SWAP`  
> tradeId | String | 交易 ID, 由柜台提供.  
> px | String | 该单腿交易价格.  
> sz | String | 成交数量  
对于币币交易，成交数量的单位为交易货币  
对于交割、永续以及期权，单位为张。  
> side | String | 交易方向, buy, sell, 从taker角度看.  
> fillVol | String | 成交时的隐含波动率   
仅适用于 `期权`  
> fwdPx | String | 成交时的远期价格   
仅适用于 `期权`  
> idxPx | String | 成交时的指数价格   
适用于 `交割`, `永续`, `期权`  
> markPx | String | 成交时的标记价格   
适用于 `交割`, `永续`, `期权`  
> groupId | String | 组合询价单ID  
只适用于组合询价单，普通询价单返回 ""  
> ts | String | 成交时间, 时间戳格式，以毫秒为单位. 如 1597026383085.  
组合询价单介绍  
  
1\. 新增返回参数 groupId，协助用户将子账户执行映射到组合询价单。仅适用于组合询价单，对普通询价单返回 ""。  
2\. 该接口返回的交易数据应为子级询价单，但拆分为单腿，tradeId 有值。  

### 大宗交易行情频道 

获取最近24小时大宗交易量  

当发生成交事件时触发推送，此外，也会根据订阅维度每隔5分钟推送一次

#### 服务地址

/ws/v5/business

> 请求示例
    
    
    {
        "id": "1512",
        "op": "subscribe",
        "args": [{
            "channel": "block-tickers",
            "instId": "BTC-USDT"
        }]
    }
    
    
    
    import asyncio
    from okx.websocket.WsPublicAsync import WsPublicAsync
    
    def callbackFunc(message):
        print(message)
    
    async def main():
        ws = WsPublicAsync(url="wss://wspap.okx.com:8443/ws/v5/business")
        await ws.start()
        args = [{
            "channel": "block-tickers",
            "instId": "BTC-USDT"
        }]
    
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
`block-tickers`  
> instId | String | 是 | 产品ID  
  
> 成功返回示例
    
    
    {
        "id": "1512",
        "event": "subscribe",
        "arg": {
            "channel": "block-tickers",
            "instId": "LTC-USD-200327"
        },
        "connId": "a4d3ae55"
    }
    

> 失败返回示例
    
    
    {
        "id": "1512",
        "event": "error",
        "code": "60012",
        "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{ \"channel\" : \"block-tickers\", \"instId\" : \"LTC-USD-200327\"}]}",
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
> channel | String | 是 | 频道名 `block-tickers`  
> instId | String | 是 | 产品ID  
code | String | 否 | 错误码  
msg | String | 否 | 错误消息  
connId | String | 是 | WebSocket连接ID  
  
> 推送示例
    
    
    {
        "arg": {
            "channel": "block-tickers"
        },
        "data": [
            {
                "instType": "SWAP",
                "instId": "LTC-USD-SWAP",
                "volCcy24h": "0",
                "vol24h": "0",
                "ts": "1597026383085"
            }
        ]
    }
    

#### 推送数据参数

**参数名** | **类型** | **描述**  
---|---|---  
arg | Object | 订阅成功的频道  
> channel | String | 频道名  
> instId | String | 产品ID  
data | Array of objects | 订阅的数据  
> instId | String | 产品ID  
> instType | String | 产品类型  
> volCcy24h | String | 24小时成交量，以`币`为单位  
如果是`衍生品`合约，数值为交易货币的数量。  
如果是`币币/币币杠杆`，数值为计价货币的数量。  
> vol24h | String | 24小时成交量，以`张`为单位  
如果是`衍生品`合约，数值为合约的张数。  
如果是`币币/币币杠杆`，数值为交易货币的数量。  
> ts | String | 数据产生时间，Unix时间戳的毫秒数格式，如 `1597026383085`