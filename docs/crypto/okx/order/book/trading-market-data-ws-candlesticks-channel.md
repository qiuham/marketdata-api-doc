---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#order-book-trading-market-data-ws-candlesticks-channel
anchor_id: order-book-trading-market-data-ws-candlesticks-channel
api_type: WebSocket
updated_at: 2026-07-10 19:31:22.933081
---

# WS / Candlesticks channel

Retrieve the candlesticks data of an instrument. the push frequency is the fastest interval 1 second push the data.  
  
#### URL Path

/ws/v5/business

> Request Example
    
    
    {
      "id": "1512",
      "op": "subscribe",
      "args": [
        {
          "channel": "candle1D",
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
              "channel": "candle1D",
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
`candle3M`  
`candle1M`  
`candle1W`   
`candle1D`  
`candle2D`  
`candle3D`  
`candle5D`  
`candle12H`  
`candle6H`  
`candle4H`  
`candle2H`  
`candle1H`  
`candle30m`  
`candle15m`  
`candle5m`  
`candle3m`  
`candle1m`  
`candle1s`  
`candle3Mutc`  
`candle1Mutc`  
`candle1Wutc`  
`candle1Dutc`  
`candle2Dutc`  
`candle3Dutc`  
`candle5Dutc`  
`candle12Hutc`  
`candle6Hutc`  
> instId | String | Yes | Instrument ID  
  
> Successful Response Example
    
    
    {
      "id": "1512",
      "event": "subscribe",
      "arg": {
        "channel": "candle1D",
        "instId": "BTC-USDT"
      },
      "connId": "a4d3ae55"
    }
    

> Failure Response Example
    
    
    {
      "id": "1512",
      "event": "error",
      "code": "60012",
      "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{ \"channel\" : \"candle1D\", \"instId\" : \"BTC-USD-191227\"}]}",
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
> channel | String | yes | channel name  
> instId | String | Yes | Instrument ID  
code | String | No | Error code  
msg | String | No | Error message  
connId | String | Yes | WebSocket connection ID  
  
> Push Data Example
    
    
    {
      "arg": {
        "channel": "candle1D",
        "instId": "BTC-USDT"
      },
      "data": [
        [
          "1597026383085",
          "8533.02",
          "8553.74",
          "8527.17",
          "8548.26",
          "45247",
          "529.5858061",
          "5529.5858061",
          "0"
        ]
      ]
    }
    

#### Push data parameters

**Parameter** | **Type** | **Description**  
---|---|---  
arg | Object | Successfully subscribed channel  
> channel | String | Channel name  
> instId | String | Instrument ID  
data | Array of Arrays | Subscribed data  
> ts | String | Opening time of the candlestick, Unix timestamp format in milliseconds, e.g. `1597026383085`  
> o | String | Open price  
> h | String | highest price  
> l | String | Lowest price  
> c | String | Close price  
> vol | String | Trading volume, with a unit of `contract`.   
If it is a `derivatives` contract, the value is the number of contracts.   
If it is `SPOT`/`MARGIN`, the value is the quantity in base currency.  
> volCcy | String | Trading volume, with a unit of `currency`.   
If it is a `derivatives` contract, the value is the number of base currency.   
If it is `SPOT`/`MARGIN`, the value is the quantity in quote currency.  
> volCcyQuote | String | Trading volume, the value is the quantity in quote currency   
e.g. The unit is `USDT` for `BTC-USDT` and `BTC-USDT-SWAP`  
The unit is `USD` for `BTC-USD-SWAP`  
> confirm | String | The state of candlesticks  
`0`: K line is uncompleted  
`1`: K line is completed

---

# WS / K线频道

获取K线数据，推送频率最快是间隔1秒推送一次数据。  
  
#### URL Path

/ws/v5/business

> 请求示例
    
    
    {
      "id": "1512",
        "op": "subscribe",
        "args": [{
            "channel": "candle1D",
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
              "channel": "candle1D",
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
`candle3M`  
`candle1M`  
`candle1W`  
`candle1D`  
`candle2D`  
`candle3D`  
`candle5D`  
`candle12H`  
`candle6H`  
`candle4H`  
`candle2H`  
`candle1H`  
`candle30m`  
`candle15m`  
`candle5m`  
`candle3m`  
`candle1m`  
`candle1s`  
`candle3Mutc`  
`candle1Mutc`  
`candle1Wutc`  
`candle1Dutc`  
`candle2Dutc`  
`candle3Dutc`  
`candle5Dutc`  
`candle12Hutc`  
`candle6Hutc`  
> instId | String | 是 | 产品ID  
  
> 成功返回示例
    
    
    {
      "id": "1512",
        "event": "subscribe",
        "arg": {
            "channel": "candle1D",
            "instId": "BTC-USDT"
        },
      "connId": "a4d3ae55"
    }
    

> 失败返回示例
    
    
    {
      "id": "1512",
        "event": "error",
        "code": "60012",
        "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{ \"channel\" : \"candle1D\", \"instId\" : \"BTC-USD-191227\"}]}",
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
        "channel": "candle1D",
        "instId": "BTC-USDT"
      },
      "data": [
        [
          "1629993600000",
          "42500",
          "48199.9",
          "41006.1",
          "41006.1",
          "3587.41204591",
          "166741046.22583129",
          "166741046.22583129",
          "0"
        ]
      ]
    }
    

#### 推送数据参数

**参数名** | **类型** | **描述**  
---|---|---  
arg | Object | 订阅成功的频道  
> channel | String | 频道名  
> instId | String | 产品ID  
data | Array of Arrays | 订阅的数据  
> ts | String | 开始时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
> o | String | 开盘价格  
> h | String | 最高价格  
> l | String | 最低价格  
> c | String | 收盘价格  
> vol | String | 交易量，以`张`为单位  
如果是`衍生品`合约，数值为合约的张数。  
如果是`币币/币币杠杆`，数值为交易货币的数量。  
> volCcy | String | 交易量，以`币`为单位  
如果是`衍生品`合约，数值为交易货币的数量。  
如果是`币币/币币杠杆`，数值为计价货币的数量。  
> volCcyQuote | String | 交易量，以计价货币为单位  
如 `BTC-USDT`和`BTC-USDT-SWAP`单位均是`USDT`。  
`BTC-USD-SWAP`单位是`USD`。  
> confirm | String | K线状态  
`0`：K线未完结  
`1`：K线已完结