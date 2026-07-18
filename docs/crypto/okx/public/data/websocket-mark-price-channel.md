---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#public-data-websocket-mark-price-channel
anchor_id: public-data-websocket-mark-price-channel
api_type: WebSocket
updated_at: 2026-07-18 20:04:46.656763
---

# Mark price channel

Retrieve the mark price. Data will be pushed every 200 ms when the mark price changes, and will be pushed every 10 seconds when the mark price does not change.  
  
#### URL Path

/ws/v5/public

> Request Example
    
    
    {
      "id": "1512",
      "op": "subscribe",
      "args": [
        {
          "channel": "mark-price",
          "instId": "LTC-USD-190628"
        }
      ]
    }
    
    
    
    import asyncio
    from okx.websocket.WsPublicAsync import WsPublicAsync
    
    def callbackFunc(message):
        print(message)
    
    async def main():
        ws = WsPublicAsync(url="wss://wspap.okx.com:8443/ws/v5/public")
        await ws.start()
        args = [{
            "channel": "mark-price",
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
`mark-price`  
> instId | String | Yes | Instrument ID  
  
> Successful Response Example
    
    
    {
      "id": "1512",
      "event": "subscribe",
      "arg": {
        "channel": "mark-price",
        "instId": "LTC-USD-190628"
      },
      "connId": "a4d3ae55"
    }
    

> Failure Response Example
    
    
    {
      "id": "1512",
      "event": "error",
      "code": "60012",
      "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{ \"channel\" : \"mark-price\", \"instId\" : \"LTC-USD-190628\"}]}",
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
> instId | String | No | Instrument ID  
code | String | No | Error code  
msg | String | No | Error message  
connId | String | Yes | WebSocket connection ID  
  
> Push Data Example
    
    
    {
      "arg": {
        "channel": "mark-price",
        "instId": "LTC-USD-190628"
      },
      "data": [
        {
          "instType": "FUTURES",
          "instId": "LTC-USD-190628",
          "markPx": "0.1",
          "ts": "1597026383085"
        }
      ]
    }
    

#### Push data parameters

Parameter | Type | Description  
---|---|---  
arg | Object | Successfully subscribed channel  
> channel | String | Channel name  
> instId | String | Instrument ID  
data | Array of objects | Subscribed data  
> instType | String | Instrument type  
> instId | String | Instrument ID  
> markPx | String | Mark price  
> ts | String | Price update time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
In rare cases, two mark price messages with the same timestamp may be received within a short window. This can occur during scheduled system maintenance or deployments and is not persistent. When this happens, clients should use the later-received message as the authoritative value. The difference between the two values will be negligible and will not materially affect trading strategies.

---

# 标记价格频道

获取标记价格，标记价格有变化时，每200ms推送一次数据，标记价格没变化时，每10s推送一次数据  
  
#### URL Path

/ws/v5/public

> 请求示例
    
    
    {
      "id": "1512",
        "op": "subscribe",
        "args": [{
            "channel": "mark-price",
            "instId": "BTC-USDT"
        }]
    }
    
    
    
    import asyncio
    from okx.websocket.WsPublicAsync import WsPublicAsync
    
    def callbackFunc(message):
        print(message)
    
    async def main():
        ws = WsPublicAsync(url="wss://wspap.okx.com:8443/ws/v5/public")
        await ws.start()
        args = [{
            "channel": "mark-price",
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
`mark-price`  
> instId | String | 是 | 产品ID  
  
> 成功返回示例
    
    
    {
      "id": "1512",
        "event": "subscribe",
        "arg": {
            "channel": "mark-price",
            "instId": "BTC-USDT"
        },
        "connId": "a4d3ae55"
    }
    

> 失败返回示例
    
    
    {
      "id": "1512",
        "event": "error",
        "code": "60012",
        "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{ \"channel\" : \"mark-price\", \"instId\" : \"LTC-USD-190628\"}]}",
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
> instId | String | 否 | 产品ID  
code | String | 否 | 错误码  
msg | String | 否 | 错误消息  
connId | String | 是 | WebSocket连接ID  
  
> 推送示例
    
    
    {
      "arg": {
        "channel": "mark-price",
        "instId": "BTC-USDT"
      },
      "data": [
        {
          "instType": "MARGIN",
          "instId": "BTC-USDT",
          "markPx": "42310.6",
          "ts": "1630049139746"
        }
      ]
    }
    

#### 推送数据参数

参数名 | 类型 | 描述  
---|---|---  
arg | Object | 订阅成功的频道  
> channel | String | 频道名  
> instId | String | 产品ID  
data | Array of objects | 订阅的数据  
> instType | String | 交易品种  
> instId | String | 产品ID  
> markPx | String | 标记价格  
> ts | String | 标记价格数据更新时间 ，Unix时间戳的毫秒数格式，如 `1597026383085`  
在极少数情况下，客户端可能在短时间内收到两条时间戳相同的标记价格消息。这可能发生在系统维护或服务发布期间，且不会持续出现。当出现此情况时，客户端应以后收到的消息作为权威值。两条消息的差值可忽略不计，不会对交易策略产生实质性影响。