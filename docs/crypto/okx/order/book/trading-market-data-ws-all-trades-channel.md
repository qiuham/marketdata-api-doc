---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#order-book-trading-market-data-ws-all-trades-channel
anchor_id: order-book-trading-market-data-ws-all-trades-channel
api_type: WebSocket
updated_at: 2026-06-30 19:55:14.033494
---

# WS / All trades channel

Retrieve the recent trades data. Data will be pushed whenever there is a trade. Every update contain only one trade. 

#### URL Path

/ws/v5/business

> Request Example
    
    
    {
      "id": "1512",
      "op": "subscribe",
      "args": [
        {
          "channel": "trades-all",
          "instId": "BTC-USDT"
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
              "channel": "trades-all",
              "instId": "BTC-USDT"
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
`trades-all`  
> instId | String | Yes | Instrument ID  
  
> Successful Response Example
    
    
    {
      "id": "1512",
      "event": "subscribe",
      "arg": {
          "channel": "trades-all",
          "instId": "BTC-USDT"
        },
      "connId": "a4d3ae55"
    }
    

> Failure Response Example
    
    
    {
      "id": "1512",
      "event": "error",
      "code": "60012",
      "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{ \"channel\" : \"trades-all\", \"instId\" : \"BTC-USD-191227\"}]}",
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
        "channel": "trades-all",
        "instId": "BTC-USDT"
      },
      "data": [
        {
          "instId": "BTC-USDT",
          "tradeId": "130639474",
          "px": "42219.9",
          "sz": "0.12060306",
          "side": "buy",
          "source": "0",
          "ts": "1630048897897"
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
> instId | String | Instrument ID, e.g. `BTC-USDT`  
> tradeId | String | Trade ID  
> px | String | Trade price  
> sz | String | Trade quantity   
For spot trading, the unit is base currency  
For `FUTURES`/`SWAP`/`OPTION`, the unit is contract.  
> side | String | Trade direction  
`buy`  
`sell`  
> source | String | Order source  
`0`: normal  
`1`: Enhanced Liquidity Program order  
> ts | String | Filled time, Unix timestamp format in milliseconds, e.g. `1597026383085`

---

# WS / 全部交易频道

获取最近的成交数据，有成交数据就推送，每次推送仅包含一条成交数据。

#### URL Path

/ws/v5/business

> 请求示例
    
    
    {
      "id": "1512",
        "op": "subscribe",
        "args": [{
            "channel": "trades-all",
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
        args = [
            {
              "channel": "trades-all",
              "instId": "BTC-USDT"
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
`trades-all`  
> instId | String | 是 | 产品ID  
  
> 成功返回示例
    
    
    {
      "id": "1512",
        "event": "subscribe",
        "arg": {
            "channel": "trades-all",
            "instId": "BTC-USDT"
        },
      "connId": "a4d3ae55"
    }
    

> 失败返回示例
    
    
    {
      "id": "1512",
        "event": "error",
        "code": "60012",
        "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{ \"channel\" : \"trades-all\", \"instId\" : \"BTC-USD-191227\"}]}",
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
        "channel": "trades-all",
        "instId": "BTC-USDT"
      },
      "data": [
        {
          "instId": "BTC-USDT",
          "tradeId": "130639474",
          "px": "42219.9",
          "sz": "0.12060306",
          "side": "buy",
          "source": "0",
          "ts": "1630048897897"
        }
      ]
    }
    

#### 推送数据参数

**参数名** | **类型** | **描述**  
---|---|---  
arg | Array of objects | 订阅成功的频道  
> channel | String | 频道名  
> instId | String | 产品ID  
data | Array of objects | 订阅的数据  
> instId | String | 产品ID，如 `BTC-USDT`  
> tradeId | String | 成交ID  
> px | String | 成交价格  
> sz | String | 成交数量  
对于币币交易，成交数量的单位为交易货币  
对于交割、永续以及期权，单位为张。  
> side | String | 成交方向  
`buy`  
`sell`  
> source | String | 订单来源  
`0`：普通订单   
`1`：流动性增强计划订单  
> ts | String | 成交时间，Unix时间戳的毫秒数格式，如 `1597026383085`