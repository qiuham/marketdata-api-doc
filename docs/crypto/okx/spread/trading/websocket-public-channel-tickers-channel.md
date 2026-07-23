---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#spread-trading-websocket-public-channel-tickers-channel
anchor_id: spread-trading-websocket-public-channel-tickers-channel
api_type: WebSocket
updated_at: 2026-07-23 19:22:28.450479
---

# Tickers channel

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

---

# 行情频道

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