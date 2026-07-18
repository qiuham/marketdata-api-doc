---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#public-data-websocket-index-candlesticks-channel
anchor_id: public-data-websocket-index-candlesticks-channel
api_type: WebSocket
updated_at: 2026-07-18 20:04:47.607089
---

# Index candlesticks channel

Retrieve the candlesticks data of the index. The push frequency is the fastest interval 1 second push the data. .  
  
#### URL Path

/ws/v5/business

> Request Example
    
    
    {
      "id": "1512",
      "op": "subscribe",
      "args": [
        {
          "channel": "index-candle30m",
          "instId": "BTC-USD"
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
              "channel": "index-candle30m",
              "instId": "BTC-USD"
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
`index-candle3M`   
`index-candle1M`   
`index-candle1W`   
`index-candle1D`   
`index-candle2D`   
`index-candle3D`   
`index-candle5D`   
`index-candle12H`   
`index-candle6H`   
`index-candle4H`   
`index -candle2H`   
`index-candle1H`   
`index-candle30m`   
`index-candle15m`   
`index-candle5m`   
`index-candle3m`   
`index-candle1m`   
`index-candle3Mutc`   
`index-candle1Mutc`   
`index-candle1Wutc`   
`index-candle1Dutc`   
`index-candle2Dutc`   
`index-candle3Dutc`   
`index-candle5Dutc`   
`index-candle12Hutc`   
`index-candle6Hutc`  
> instId | String | Yes | Index, e.g. `BTC-USD`  
Same as `uly`.  
  
> Successful Response Example
    
    
    {
      "id": "1512",
      "event": "subscribe",
      "arg": {
        "channel": "index-candle30m",
        "instId": "BTC-USD"
      },
      "connId": "a4d3ae55"
    }
    

> Failure Response Example
    
    
    {
      "id": "1512",
      "event": "error",
      "code": "60012",
      "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{ \"channel\" : \"index-candle30m\", \"instId\" : \"BTC-USD\"}]}",
      "connId": "a4d3ae55"
    }
    

#### Response parameters

Parameter | Type | Required | Description  
---|---|---|---  
id | String | No | Unique identifier of the message  
event | String | Yes | `subscribe` `unsubscribe`  
arg | Object | No | Subscribed channel  
> channel | String | Yes | Channel name  
> instId | String | No | Index, e.g. `BTC-USD`  
code | String | No | Error code  
msg | String | No | Error message  
connId | String | Yes | WebSocket connection ID  
  
> Push Data Example
    
    
    {
      "arg": {
        "channel": "index-candle30m",
        "instId": "BTC-USD"
      },
      "data": [["1597026383085", "3811.31", "3811.31", "3811.31", "3811.31", "0"]]
    }
    

#### Push data parameters

Parameter | Type | Description  
---|---|---  
arg | Object | Successfully subscribed channel  
> channel | String | Channel name  
> instId | String | Index  
data | Array of Arrays | Subscribed data  
> ts | String | Opening time of the candlestick, Unix timestamp format in milliseconds, e.g. `1597026383085`  
> o | String | Open price  
> h | String | Highest price  
> l | String | Lowest price  
> c | String | Close price  
> confirm | String | The state of candlesticks.  
`0` represents that it is uncompleted, `1` represents that it is completed.  
The order of the returned values is: [ts,o,h,l,c,confirm]

---

# 指数K线频道

获取指数的K线数据，推送频率最快是间隔1秒推送一次数据。  
  
#### URL Path

/ws/v5/business

> 请求示例
    
    
    {
        "id": "1512",
        "op": "subscribe",
        "args": [{
            "channel": "index-candle30m",
            "instId": "BTC-USD"
        }]
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
              "channel": "index-candle30m",
              "instId": "BTC-USD"
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
`index-candle3M`  
`index-candle1M`  
`index-candle1W`  
`index-candle1D`  
`index-candle2D`  
`index-candle3D`  
`index-candle5D`  
`index-candle12H`  
`index-candle6H`  
`index-candle4H`  
`index -candle2H`  
`index-candle1H`  
`index-candle30m`  
`index-candle15m`  
`index-candle5m`  
`index-candle3m`  
`index-candle1m`  
`index-candle3Mutc`   
`index-candle1Mutc`  
`index-candle1Wutc`  
`index-candle1Dutc`  
`index-candle2Dutc`  
`index-candle3Dutc`  
`index-candle5Dutc`  
`index-candle12Hutc`  
`index-candle6Hutc`  
> instId | String | 是 | 现货指数，如 `BTC-USD`  
与 `uly` 含义相同。  
  
> 成功返回示例
    
    
    {
        "id": "1512",
        "event": "subscribe",
        "arg": {
            "channel": "index-candle30m",
            "instId": "BTC-USD"
        },
        "connId": "a4d3ae55"
    }
    

> 失败返回示例
    
    
    {
        "id": "1512",
        "event": "error",
        "code": "60012",
        "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{ \"channel\" : \"index-candle30m\", \"instId\" : \"BTC-USD\"}]}",
        "connId": "a4d3ae55"
    }
    

#### 返回参数

参数 | 类型 | 是否必须 | 描述  
---|---|---|---  
id | String | 否 | 消息的唯一标识  
event | String | 是 | `subscribe` `unsubscribe`  
arg | Object | 否 | 订阅的频道  
> channel | String | 是 | 频道名  
> instId | String | 否 | 现货指数  
code | String | 否 | 错误码  
msg | String | 否 | 错误消息  
connId | String | 是 | WebSocket连接ID  
  
> 推送示例
    
    
    {
        "arg": {
            "channel": "index-candle30m",
            "instId": "BTC-USD"
        },
        "data": [
            ["1597026383085", "3811.31", "3811.31", "3811.31", "3811.31","0"]
        ]
    }
    

#### 推送数据参数

参数名 | 类型 | 描述  
---|---|---  
arg | Object | 订阅成功的频道  
> channel | String | 频道名  
> instId | String | 现货指数  
data | Array of Arrays | 订阅的数据  
> ts | String | 开始时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
> o | String | 开盘价格  
> h | String | 最高价格  
> l | String | 最低价格  
> c | String | 收盘价格  
> confirm | String | K线状态   
`0` 代表 K 线未完结，`1` 代表 K 线已完结。  
返回值数组顺分别为是：[ts,o,h,l,c,confirm]