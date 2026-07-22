---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#order-book-trading-market-data-ws-trades-channel
anchor_id: order-book-trading-market-data-ws-trades-channel
api_type: WebSocket
updated_at: 2026-07-22 19:19:54.033553
---

# WS / Trades channel

Retrieve the recent trades data. Data will be pushed whenever there is a trade. Every update may aggregate multiple trades.   
  
  
  
The message is sent only once per taker order, filled price, source. The count field is used to represent the number of aggregated matches.

#### URL Path

/ws/v5/public

> Request Example
    
    
    {
      "id": "1512",
      "op": "subscribe",
      "args": [
        {
          "channel": "trades",
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
        args = [
            {
              "channel": "trades",
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
`trades`  
> instId | String | Yes | Instrument ID  
  
> Successful Response Example
    
    
    {
      "id": "1512",
      "event": "subscribe",
      "arg": {
          "channel": "trades",
          "instId": "BTC-USDT"
      },
      "connId": "a4d3ae55"
    }
    

> Failure Response Example
    
    
    {
      "id": "1512",
      "event": "error",
      "code": "60012",
      "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{ \"channel\" : \"trades\", \"instId\" : \"BTC-USD-191227\"}]}",
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
        "channel": "trades",
        "instId": "BTC-USDT"
      },
      "data": [
        {
          "instId": "BTC-USDT",
          "tradeId": "130639474",
          "px": "42219.9",
          "sz": "0.12060306",
          "side": "buy",
          "ts": "1630048897897",
          "count": "3",
          "source": "0",
          "seqId": 1234
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
> tradeId | String | The last trade ID in the trades aggregation  
> px | String | Trade price  
> sz | String | Trade quantity   
For spot trading, the unit is base currency  
For `FUTURES`/`SWAP`/`OPTION`, the unit is contract.  
> side | String | Trade side of taker  
`buy`  
`sell`  
> ts | String | Filled time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
> count | String | The count of trades aggregated  
> source | String | Order source  
`0`: normal orders  
`1`: Enhanced Liquidity Program order  
> seqId | Integer | Sequence ID of the current message.  
Aggregation function description:  
1\. The system will send only one message per taker order, filled price, source. The `count` field will be used to represent the number of aggregated matches.  
2\. The `tradeId` field in the message becomes the last trade ID in the aggregation.  
3\. When the `count` = 1, it means the taker order matches only one maker order with the specific price.  
4\. When the `count` > 1, it means the taker order matches multiple maker orders with the same price. For example, if `tradeId` = 123 and `count` = 3, it means the message aggregates the trades of `tradeId` = 123, 122, and 121. Maker side has filled multiple orders.  
5\. Users can use this information to compare with data from the `trades-all` channel.  
6\. Order book and the aggregated trades data are still published sequentially.  
The seqId may be the same for different trade updates that occur at the same time.

---

# WS / 交易频道

获取最近的成交数据，有成交数据就推送，每次推送可能聚合多条成交数据。  
根据每个taker订单的不同成交价格，不同成交来源推送消息，并使用count字段表示聚合的订单匹配数量。  
  
#### URL Path

/ws/v5/public

> 请求示例
    
    
    {
      "id": "1512",
        "op": "subscribe",
        "args": [{
            "channel": "trades",
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
        args = [
            {
              "channel": "trades",
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
`trades`  
> instId | String | 是 | 产品ID  
  
> 成功返回示例
    
    
    {
      "id": "1512",
        "event": "subscribe",
        "arg": {
            "channel": "trades",
            "instId": "BTC-USDT"
        },
      "connId": "a4d3ae55"
    }
    

> 失败返回示例
    
    
    {
      "id": "1512",
        "event": "error",
        "code": "60012",
        "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{ \"channel\" : \"trades\", \"instId\" : \"BTC-USD-191227\"}]}",
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
        "channel": "trades",
        "instId": "BTC-USDT"
      },
      "data": [
        {
          "instId": "BTC-USDT",
          "tradeId": "130639474",
          "px": "42219.9",
          "sz": "0.12060306",
          "side": "buy",
          "ts": "1630048897897",
          "count": "3",
          "source": "0",
          "seqId": 1234
        }
      ]
    }
    

#### 推送数据参数

**参数名** | **类型** | **描述**  
---|---|---  
arg | Object | 订阅成功的频道  
> channel | String | 频道名  
> instId | String | 产品ID  
data | Array of objects | 订阅的数据  
> instId | String | 产品ID，如 `BTC-USDT`  
> tradeId | String | 聚合的多笔交易中最新一笔交易的成交ID  
> px | String | 成交价格  
> sz | String | 成交数量  
对于币币交易，成交数量的单位为交易货币  
对于交割、永续以及期权，单位为张。  
> side | String | 吃单方向  
`buy`  
`sell`  
> ts | String | 成交时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
> count | String | 聚合的订单匹配数量  
> source | String | 订单来源  
`0`：普通订单  
`1`：流动性增强计划订单  
> seqId | Integer | 推送的序列号  
聚合功能说明：  
1\. 系统将根据每个taker订单的不同成交价格，不同成交来源推送消息，并使用count字段表示聚合的订单匹配数量。  
2\. tradeId是聚合的多笔交易中最新一笔交易的 ID。  
3\. 当count = 1时，表示taker订单部分或完全成交时仅匹配了一个maker订单。  
4\. 当count > 1时，表示taker订单以相同价格匹配了多个maker订单。例如，如果tradeId = 123，且count = 3，表示该消息聚合了tradeId = 123, 122, 121的成交。maker侧有多笔价格相同的订单被成交。  
5\. 用户可以使用此数据与“全部交易”频道的数据进行对比。  
6\. 深度及聚合交易数据仍按顺序发布。  
同时发生的不同交易推送数据的`seqId`可能相同。