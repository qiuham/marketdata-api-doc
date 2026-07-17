---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#public-data-websocket-price-limit-channel
anchor_id: public-data-websocket-price-limit-channel
api_type: WebSocket
updated_at: 2026-07-17 19:17:37.599497
---

# Price limit channel

Retrieve the maximum buy price and minimum sell price of instruments. Data will be pushed every 200ms when there are changes in limits, and will not be pushed when there is no changes on limit.

#### URL Path

/ws/v5/public

> Request Example
    
    
    {
      "id": "1512",
      "op": "subscribe",
      "args": [
        {
          "channel": "price-limit",
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
        args = [
            {
              "channel": "price-limit",
              "instId": "LTC-USD-190628"
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
`price-limit`  
> instId | String | Yes | Instrument ID  
  
> Successful Response Example
    
    
    {
      "id": "1512",
      "event": "subscribe",
      "arg": {
        "channel": "price-limit",
        "instId": "LTC-USD-190628"
      },
      "connId": "a4d3ae55"
    }
    

> Failure Response Example
    
    
    {
      "id": "1512",
      "event": "error",
      "code": "60012",
      "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{ \"channel\" : \"price-limit\", \"instId\" : \"LTC-USD-190628\"}]}",
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
> instId | String | Yes | Instrument ID  
code | String | No | Error code  
msg | String | No | Error message  
connId | String | Yes | WebSocket connection ID  
  
> Push Data Example
    
    
    {
        "arg": {
            "channel": "price-limit",
            "instId": "LTC-USD-190628"
        },
        "data": [{
            "instId": "LTC-USD-190628",
            "buyLmt": "200",
            "sellLmt": "300",
            "ts": "1597026383085",
            "enabled": true
        }]
    }
    

#### Push data parameters

**Parameter** | **Type** | **Description**  
---|---|---  
arg | Object | Successfully subscribed channel  
> channel | String | Channel name  
> instId | String | Instrument ID  
data | Array of objects | Subscribed data  
> instType | String | Instrument type  
> instId | String | Instrument ID, e.g. `BTC-USDT`  
> buyLmt | String | Maximum buy price   
Return "" when enabled is false  
> sellLmt | String | Minimum sell price   
Return "" when enabled is false  
> ts | String | Price update time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
> enabled | Boolean | Whether price limit is effective   
`true`: the price limit is effective   
`false`: the price limit is not effective

---

# 限价频道

获取交易产品的最高买价和最低卖价。限价有变化时，每 200 毫秒推送一次数据，限价没变化时，不推送数据

#### URL Path

/ws/v5/public

> 请求示例
    
    
    {
        "id": "1512",
        "op": "subscribe",
        "args": [{
            "channel": "price-limit",
            "instId": "LTC-USD-190628"
        }]
    }
    
    
    
    import asyncio
    from okx.websocket.WsPublicAsync import WsPublicAsync
    
    def callbackFunc(message):
        print(message)
    
    async def main():
        ws = WsPublicAsync(url="wss://wspap.okx.com:8443/ws/v5/public")
        await ws.start()
        args = [
            {
              "channel": "price-limit",
              "instId": "LTC-USD-190628"
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
`price-limit`  
> instId | String | 是 | 产品ID  
  
> 成功返回示例
    
    
    {
        "id": "1512",
        "event": "subscribe",
        "arg": {
            "channel": "price-limit",
            "instId": "LTC-USD-190628"
        },
        "connId": "a4d3ae55"
    }
    

> 失败返回示例
    
    
    {
        "id": "1512",
        "event": "error",
        "code": "60012",
        "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{ \"channel\" : \"price-limit\", \"instId\" : \"LTC-USD-190628\"}]}",
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
> instId | String | 是 | 产品ID  
code | String | 否 | 错误码  
msg | String | 否 | 错误消息  
connId | String | 是 | WebSocket连接ID  
  
> 推送示例
    
    
    {
        "arg": {
            "channel": "price-limit",
            "instId": "LTC-USD-190628"
        },
        "data": [{
            "instId": "LTC-USD-190628",
            "buyLmt": "200",
            "sellLmt": "300",
            "ts": "1597026383085",
            "enabled": true
        }]
    }
    

#### 推送数据参数

**参数名** | **类型** | **描述**  
---|---|---  
arg | Object | 订阅成功的频道  
> channel | String | 频道名  
> instId | String | 产品ID  
data | Array of objects | 订阅的数据  
> instType | String | 产品类型  
> instId | String | 产品ID，如 `BTC-USD-SWAP`  
> buyLmt | String | 最高买价   
当enabled为false时，返回""  
> sellLmt | String | 最低卖价   
当enabled为false时，返回""  
> ts | String | 限价数据更新时间 ，Unix时间戳的毫秒数格式，如 `1597026383085`  
> enabled | Boolean | 限价是否生效   
`true`：限价生效   
`false`：限价不生效