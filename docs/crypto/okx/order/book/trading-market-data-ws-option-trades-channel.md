---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#order-book-trading-market-data-ws-option-trades-channel
anchor_id: order-book-trading-market-data-ws-option-trades-channel
api_type: WebSocket
updated_at: 2026-07-18 20:04:03.987352
---

# WS / Option trades channel

Retrieve the recent trades data. Data will be pushed whenever there is a trade. Every update contain only one trade.

#### URL Path

/ws/v5/public

> Request Example
    
    
    {
      "id": "1512",
        "op": "subscribe",
        "args": [{
            "channel": "option-trades",
            "instType": "OPTION",
            "instFamily": "BTC-USD"
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
            "channel": "option-trades",
            "instType": "OPTION",
            "instFamily": "BTC-USD"
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
op | String | Yes | `subscribe` `unsubscribe`  
args | Array of objects | Yes | List of subscribed channels  
> channel | String | Yes | Channel name  
`option-trades`  
> instType | String | Yes | Instrument type, `OPTION`  
> instId | String | Conditional | Instrument ID, e.g. BTC-USD-221230-4000-C, Either `instId` or `instFamily` is required. If both are passed, `instId` will be used.  
> instFamily | String | Conditional | Instrument family, e.g. BTC-USD  
  
> Successful Response Example
    
    
    {
      "id": "1512",
        "event": "subscribe",
        "arg": {
            "channel": "option-trades",
            "instType": "OPTION",
            "instFamily": "BTC-USD"
        },
        "connId": "a4d3ae55"
    }
    

> Failure Response Example
    
    
    {
      "id": "1512",
      "event": "error",
      "code": "60012",
      "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{ \"channel\" : \"option-trades\"}]}",
      "connId": "a4d3ae55"
    }
    

#### Response parameters

Parameter | Type | Required | Description  
---|---|---|---  
id | String | No | Unique identifier of the message  
event | String | Yes | `subscribe` `unsubscribe` `error`  
arg | Object | No | Subscribed channel  
> channel | String | Yes | Channel name  
`status`  
code | String | No | Error code  
msg | String | No | Error message  
connId | String | Yes | WebSocket connection ID  
  
> Push Data Example
    
    
    {
        "arg": {
            "channel": "option-trades",
            "instType": "OPTION",
            "instFamily": "BTC-USD"
        },
        "data": [
            {
                "fillVol": "0.5066007836914062",
                "fwdPx": "16469.69928595038",
                "idxPx": "16537.2",
                "instFamily": "BTC-USD",
                "instId": "BTC-USD-230224-18000-C",
                "markPx": "0.04690107010619562",
                "optType": "C",
                "px": "0.045",
                "side": "sell",
                "sz": "2",
                "tradeId": "38",
                "ts": "1672286551080"
            }
        ]
    }
    

#### Push data parameters

Parameter | Type | Description  
---|---|---  
arg | Object | Successfully subscribed channel  
> channel | String | Channel name  
data | Array of objects | Subscribed data  
> instId | String | Instrument ID  
> instFamily | String | Instrument family  
> tradeId | String | Trade ID  
> px | String | Trade price  
> sz | String | Trade quantity. The unit is contract.  
> side | String | Trade side   
`buy`   
`sell`  
> optType | String | Option type, C: Call P: Put  
> fillVol | String | Implied volatility while trading (Correspond to trade price)  
> fwdPx | String | Forward price while trading  
> idxPx | String | Index price while trading  
> markPx | String | Mark price while trading  
> ts | String | Trade time, Unix timestamp format in milliseconds, e.g. `1597026383085`.  
The first data you receive after subscribing may be cached from the previous trade, so please ignore it.

---

# WS / 期权公共成交频道

获取最近的期权成交数据，有成交数据就推送，每次推送仅包含一条成交数据。

#### URL Path

/ws/v5/public

> 请求示例
    
    
    {
        "id": "1512",
        "op": "subscribe",
        "args": [{
            "channel": "option-trades",
            "instType": "OPTION",
            "instFamily": "BTC-USD"
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
            "channel": "option-trades",
            "instType": "OPTION",
            "instFamily": "BTC-USD"
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
`option-trades`  
> instType | String | 是 | 产品类型，`OPTION`：期权  
> instId | String | 可选 | 产品ID，如 BTC-USD-221230-4000-C，`instId` 和 `instFamily` 必须传一个，若传两个，以 `instId` 为主  
> instFamily | String | 可选 | 交易品种，如 BTC-USD  
  
> 成功返回示例
    
    
    {
        "id": "1512",
        "event": "subscribe",
        "arg": {
            "channel": "option-trades",
            "instType": "OPTION",
            "instFamily": "BTC-USD"
        },
        "connId": "a4d3ae55"
    }
    
    

> 失败返回示例
    
    
    {
        "id": "1512",
        "event": "error",
        "code": "60012",
        "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{ \"channel\" : \"option-trades\"}]}",
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
code | String | 否 | 错误码  
msg | String | 否 | 错误消息  
connId | String | 是 | WebSocket连接ID  
  
> 推送示例
    
    
    {
        "arg": {
            "channel": "option-trades",
            "instType": "OPTION",
            "instFamily": "BTC-USD"
        },
        "data": [
            {
                "fillVol": "0.5066007836914062",
                "fwdPx": "16469.69928595038",
                "idxPx": "16537.2",
                "instFamily": "BTC-USD",
                "instId": "BTC-USD-230224-18000-C",
                "markPx": "0.04690107010619562",
                "optType": "C",
                "px": "0.045",
                "side": "sell",
                "sz": "2",
                "tradeId": "38",
                "ts": "1672286551080"
            }
        ]
    }
    

#### 推送数据参数

参数名 | 类型 | 描述  
---|---|---  
arg | Object | 订阅成功的频道  
> channel | String | 频道名  
data | Array of objects | 订阅的数据  
> instId | String | 产品ID  
> instFamily | String | 交易品种  
> tradeId | String | 成交ID  
> px | String | 成交价格  
> sz | String | 成交数量，单位为张。  
> side | String | 成交方向   
`buy`：买   
`sell`：卖  
> optType | String | 期权类型，C：看涨期权 P：看跌期权 ，仅适用于期权  
> fillVol | String | 成交时的隐含波动率（对应成交价格）  
> fwdPx | String | 成交时的远期价格  
> idxPx | String | 成交时的指数价格  
> markPx | String | 成交时的标记价格  
> ts | String | 成交时间，Unix时间戳的毫秒数格式， 如`1597026383085`  
该频道订阅成功后的首条数据可能为最近一笔成交的缓存数据，请忽略。