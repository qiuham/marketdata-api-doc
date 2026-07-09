---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#order-book-trading-market-data-ws-tickers-channel
anchor_id: order-book-trading-market-data-ws-tickers-channel
api_type: WebSocket
updated_at: 2026-07-09 19:37:40.592524
---

# WS / Tickers channel

Retrieve the last traded price, bid price, ask price and 24-hour trading volume of instruments. Best ask price may be lower than the best bid price during the pre-open period.   
The fastest rate is 1 update/100ms. There will be no update if the event is not triggered. The events which can trigger update: trade, the change on best ask/bid.

#### URL Path

/ws/v5/public

> Request Example
    
    
    {
      "id": "1512",
      "op": "subscribe",
      "args": [
        {
          "channel": "tickers",
          "instId": "BTC-USDT"
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
            "channel": "tickers",
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
`tickers`  
> instId | String | Yes | Instrument ID  
  
> Successful Response Example
    
    
    {
      "id": "1512",
      "event": "subscribe",
      "arg": {
        "channel": "tickers",
        "instId": "BTC-USDT"
      },
      "connId": "a4d3ae55"
    }
    

> Failure Response Example
    
    
    {
      "id": "1512",
      "event": "error",
      "code": "60012",
      "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{ \"channel\" : \"tickers\", \"instId\" : \"LTC-USD-200327\"}]}",
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
        "channel": "tickers",
        "instId": "BTC-USDT"
      },
      "data": [
        {
          "instType": "SPOT",
          "instId": "BTC-USDT",
          "last": "9999.99",
          "lastSz": "0.1",
          "askPx": "9999.99",
          "askSz": "11",
          "bidPx": "8888.88",
          "bidSz": "5",
          "open24h": "9000",
          "high24h": "10000",
          "low24h": "8888.88",
          "volCcy24h": "2222",
          "vol24h": "2222",
          "sodUtc0": "2222",
          "sodUtc8": "2222",
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
> instType | String | Instrument type  
> instId | String | Instrument ID  
> last | String | Last traded price  
> lastSz | String | Last traded size. 0 represents there is no trading volume  
> askPx | String | Best ask price  
> askSz | String | Best ask size  
> bidPx | String | Best bid price  
> bidSz | String | Best bid size  
> open24h | String | Open price in the past 24 hours  
> high24h | String | Highest price in the past 24 hours  
> low24h | String | Lowest price in the past 24 hours  
> volCcy24h | String | 24h trading volume, with a unit of `currency`.   
If it is a `derivatives` contract, the value is the number of base currency.   
If it is `SPOT`/`MARGIN`, the value is the quantity in quote currency.  
> vol24h | String | 24h trading volume, with a unit of `contract`.   
If it is a `derivatives` contract, the value is the number of contracts.   
If it is `SPOT`/`MARGIN`, the value is the quantity in base currency.  
> sodUtc0 | String | Open price in the UTC 0  
> sodUtc8 | String | Open price in the UTC 8  
> ts | String | Ticker data generation time, Unix timestamp format in milliseconds, e.g. `1597026383085`

---

# WS / 行情频道

获取产品的最新成交价、买一价、卖一价和24小时交易量等信息。在提前挂单阶段，best ask的价格有机会低于best bid。  
最快100ms推送一次，没有触发事件时不推送，触发推送的事件有：成交、买一卖一发生变动。

#### URL Path

/ws/v5/public

> 请求示例
    
    
    {
        "id": "1512",
        "op": "subscribe",
        "args": [{
            "channel": "tickers",
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
            "channel": "tickers",
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
`tickers`  
> instId | String | 是 | 产品ID  
  
> 成功返回示例
    
    
    {
        "id": "1512",
        "event": "subscribe",
        "arg": {
            "channel": "tickers",
            "instId": "BTC-USDT"
        },
        "connId": "a4d3ae55"
    }
    

> 失败返回示例
    
    
    {
        "id": "1512",
        "event": "error",
        "code": "60012",
        "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{ \"channel\" : \"tickers\", \"instId\" : \"LTC-USD-200327\"}]}",
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
            "channel": "tickers",
            "instId": "BTC-USDT"
        },
        "data": [{
            "instType": "SPOT",
            "instId": "BTC-USDT",
            "last": "9999.99",
            "lastSz": "0.1",
            "askPx": "9999.99",
            "askSz": "11",
            "bidPx": "8888.88",
            "bidSz": "5",
            "open24h": "9000",
            "high24h": "10000",
            "low24h": "8888.88",
            "volCcy24h": "2222",
            "vol24h": "2222",
            "sodUtc0": "2222",
            "sodUtc8": "2222",
            "ts": "1597026383085"
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
> instId | String | 产品ID  
> last | String | 最新成交价  
> lastSz | String | 最新成交的数量，0 代表没有成交量  
> askPx | String | 卖一价  
> askSz | String | 卖一价对应的量  
> bidPx | String | 买一价  
> bidSz | String | 买一价对应的数量  
> open24h | String | 24小时开盘价  
> high24h | String | 24小时最高价  
> low24h | String | 24小时最低价  
> volCcy24h | String | 24小时成交量，以`币`为单位  
如果是`衍生品`合约，数值为交易货币的数量。  
如果是`币币/币币杠杆`，数值为计价货币的数量。  
> vol24h | String | 24小时成交量，以`张`为单位  
如果是`衍生品`合约，数值为合约的张数。  
如果是`币币/币币杠杆`，数值为交易货币的数量。  
> sodUtc0 | String | UTC+0 时开盘价  
> sodUtc8 | String | UTC+8 时开盘价  
> ts | String | 数据产生时间，Unix时间戳的毫秒数格式，如 `1597026383085`