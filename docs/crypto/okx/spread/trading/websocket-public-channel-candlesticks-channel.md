---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#spread-trading-websocket-public-channel-candlesticks-channel
anchor_id: spread-trading-websocket-public-channel-candlesticks-channel
api_type: WebSocket
updated_at: 2026-07-01 19:55:04.805408
---

# Candlesticks channel

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

# K线频道

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