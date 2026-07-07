---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#public-data-websocket-estimated-delivery-exercise-settlement-price-channel
anchor_id: public-data-websocket-estimated-delivery-exercise-settlement-price-channel
api_type: WebSocket
updated_at: 2026-07-07 19:43:14.564435
---

# Estimated delivery/exercise/settlement price channel

Retrieve the estimated delivery/exercise/settlement price of `FUTURES`, `OPTION` and `SWAP` contracts.  
  
The estimated price, calculated based on index price during the one-hour period prior to delivery, excerise, or settlement, with updates pushed approximately every 200ms.

#### URL Path

/ws/v5/public

> Request Example
    
    
    {
      "id": "1512",
      "op": "subscribe",
      "args": [
        {
          "channel": "estimated-price",
          "instType": "FUTURES",
          "instFamily": "BTC-USD"
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
              "channel": "estimated-price",
              "instType": "FUTURES",
              "instFamily": "BTC-USD"
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
`estimated-price`  
> instType | String | Yes | Instrument type  
`OPTION`  
`FUTURES`  
`SWAP`  
`EVENTS`  
> instFamily | String | Conditional | Instrument family  
Either `instFamily` or `instId` is required.  
> instId | String | Conditional | Instrument ID  
Either `instFamily` or `instId` is required.  
  
> Successful Response Example
    
    
    {
      "id": "1512",
      "event": "subscribe",
      "arg": {
        "channel": "estimated-price",
        "instType": "FUTURES",
        "instFamily": "BTC-USD"
      },
      "connId": "a4d3ae55"
    }
    

> Failure Response Example
    
    
    {
      "id": "1512",
      "event": "error",
      "code": "60012",
      "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{ \"channel\" : \"estimated-price\", \"instId\" : \"FUTURES\",\"uly\" :\"BTC-USD\"}]}",
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
> instType | String | Yes | Instrument type  
`OPTION`  
`FUTURES`  
`SWAP`  
`EVENTS`  
> instFamily | String | Conditional | Instrument family  
> instId | String | Conditional | Instrument ID  
code | String | No | Error code  
msg | String | No | Error message  
connId | String | Yes | WebSocket connection ID  
  
> Push Data Example
    
    
    {
        "arg": {
            "channel": "estimated-price",
            "instType": "FUTURES",
            "instFamily": "XRP-USDT"
        },
        "data": [{
            "instId": "XRP-USDT-250307",
            "instType": "FUTURES",
            "settlePx": "2.4230631578947368",
            "settleType": "settlement",
            "ts": "1741244598708"
        }]
    }
    

#### Push data parameters

**Parameter** | **Type** | **Description**  
---|---|---  
arg | Object | Successfully subscribed channel  
> channel | String | Channel name  
> instType | String | Instrument type  
`FUTURES`  
`OPTION`  
`SWAP`  
`EVENTS`  
> instFamily | String | Instrument family  
> instId | String | Instrument ID  
data | Array of objects | Subscribed data  
> instType | String | Instrument type  
> instId | String | Instrument ID, e.g. `BTC-USD-170310`  
> settleType | String | Type  
`settlement`: Futures settlement  
`delivery`: Futures delivery  
`exercise`: Option exercise  
> settlePx | String | Estimated price  
> ts | String | Data update time, Unix timestamp format in milliseconds, e.g. `1597026383085`

---

# 预估永续/交割/行权/结算价格频道

在永续/交割/行权/结算前一小时内，将基于指数价格计算并推送预估价，更新频率约为每 200 毫秒一次。  
  
#### URL Path

/ws/v5/public

> 请求示例
    
    
    {
        "id": "1512",
        "op": "subscribe",
        "args": [{
            "channel": "estimated-price",
            "instType": "FUTURES",
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
        args = [
            {
              "channel": "estimated-price",
              "instType": "FUTURES",
              "instFamily": "BTC-USD"
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
`estimated-price`  
> instType | String | 是 | 产品类型  
`FUTURES`：交割  
`OPTION`：期权  
`SWAP`：永续  
`EVENTS`：事件合约  
> instFamily | String | 可选 | 交易品种  
`instFamily`和`instId`必须指定一个  
> instId | String | 可选 | 产品ID  
`instFamily`和`instId`必须指定一个  
  
> 成功返回示例
    
    
    {
        "id": "1512",
        "event": "subscribe",
        "arg": {
            "channel": "estimated-price",
            "instType": "FUTURES",
            "instFamily": "BTC-USD"
        },
        "connId": "a4d3ae55"
    }
    

> 失败返回示例
    
    
    {
        "id": "1512",
        "event": "error",
        "code": "60012",
        "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{ \"channel\" : \"estimated-price\", \"instId\" : \"FUTURES\",\"instFamily\" :\"BTC-USD\"}]}",
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
> instType | String | 是 | 产品类型  
`FUTURES`：交割  
`OPTION`：期权  
`SWAP`：永续  
`EVENTS`：事件合约  
> instFamily | String | 否 | 交易品种  
> instId | String | 否 | 产品ID  
code | String | 否 | 错误码  
msg | String | 否 | 错误消息  
connId | String | 是 | WebSocket连接ID  
  
> 推送示例
    
    
    {
        "arg": {
            "channel": "estimated-price",
            "instType": "FUTURES",
            "instFamily": "XRP-USDT"
        },
        "data": [{
            "instId": "XRP-USDT-250307",
            "instType": "FUTURES",
            "settlePx": "2.4230631578947368",
            "settleType": "settlement",
            "ts": "1741244598708"
        }]
    }
    

#### 推送数据参数

**参数名** | **类型** | **描述**  
---|---|---  
arg | Object | 订阅成功的频道  
> channel | String | 频道名  
> instType | String | 产品类型  
`FUTURES`：交割  
`OPTION`：期权  
`SWAP`：永续  
`EVENTS`：事件合约  
> instFamily | String | 交易品种  
> instId | String | 产品ID  
data | Array of objects | 订阅的数据  
> instType | String | 产品类型  
> instId | String | 产品ID，如 `BTC-USD-170310`  
> settleType | String | 类型  
`settlement`：结算  
`delivery`：交割  
`exercise`：行权  
> settlePx | String | 预估价  
> ts | String | 数据更新时间，Unix时间戳的毫秒数格式，如 `1597026383085`