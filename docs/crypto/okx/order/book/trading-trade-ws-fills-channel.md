---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#order-book-trading-trade-ws-fills-channel
anchor_id: order-book-trading-trade-ws-fills-channel
api_type: WebSocket
updated_at: 2026-07-03 19:39:13.813476
---

# WS / Fills channel

Retrieve transaction information. Data will not be pushed when first subscribed. Data will only be pushed when there are order book fill events, where tradeId > 0.  

The channel is exclusively available to users with trading fee tier VIP4 or above. Other users will receive error code 64003. For other users, please use [WS / Order channel](/docs-v5/en/#order-book-trading-trade-ws-order-channel). 

For `EVENTS`, only data for the YES side is returned regardless of whether the actual order was placed on YES or NO.

#### URL Path

/ws/v5/private (required login)

> Request Example: single
    
    
    {
        "id": "1512",
        "op": "subscribe",
        "args": [
            {
                "channel": "fills",
                "instId": "BTC-USDT-SWAP"
            }
        ]
    }
    
    
    
    import asyncio
    
    from okx.websocket.WsPrivateAsync import WsPrivateAsync
    
    
    def callbackFunc(message):
        print(message)
    
    async def main():
    
        ws = WsPrivateAsync(
            apiKey = "YOUR_API_KEY",
            passphrase = "YOUR_PASSPHRASE",
            secretKey = "YOUR_SECRET_KEY",
            url = "wss://ws.okx.com:8443/ws/v5/private",
            useServerTime=False
        )
        await ws.start()
        args = [
            {
                "channel": "fills",
                "instId": "BTC-USDT-SWAP"
            }
        ]
    
        await ws.subscribe(args, callback=callbackFunc)
        await asyncio.sleep(10)
    
        await ws.unsubscribe(args, callback=callbackFunc)
        await asyncio.sleep(10)
    
    
    asyncio.run(main())
    

> Request Example
    
    
    {
        "id": "1512",
        "op": "subscribe",
        "args": [
            {
                "channel": "fills"
            }
        ]
    }
    
    
    
    import asyncio
    
    from okx.websocket.WsPrivateAsync import WsPrivateAsync
    
    
    def callbackFunc(message):
        print(message)
    
    async def main():
    
        ws = WsPrivateAsync(
            apiKey = "YOUR_API_KEY",
            passphrase = "YOUR_PASSPHRASE",
            secretKey = "YOUR_SECRET_KEY",
            url = "wss://ws.okx.com:8443/ws/v5/private",
            useServerTime=False
        )
        await ws.start()
        args = [
            {
                "channel": "fills"
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
`subscribe` `unsubscribe`  
args | Array of objects | Yes | List of subscribed channels  
> channel | String | Yes | Channel name `fills`  
> instId | String | No | Instrument ID  
  
> Successful Response Example: single
    
    
    {
      "id": "1512",
      "event": "subscribe",
      "arg": {
        "channel": "fills",
        "instId": "BTC-USDT-SWAP"
      },
      "connId": "a4d3ae55"
    }
    
    

> Successful Response Example
    
    
    {
      "id": "1512",
      "event": "subscribe",
      "arg": {
        "channel": "fills"
      },
      "connId": "a4d3ae55"
    }
    
    

#### Response parameters

Parameter | Type | Required | Description  
---|---|---|---  
id | String | No | Unique identifier of the message  
event | String | Yes | Event  
`subscribe` `unsubscribe` `error`  
arg | Object | No | Subscribed channel  
> channel | String | Yes | Channel name  
> instId | String | No | Instrument ID  
code | String | No | Error code  
msg | String | No | Error message  
connId | String | Yes | WebSocket connection ID  
  
> Push Data Example: single
    
    
    {
        "arg": {
            "channel": "fills",
            "instId": "BTC-USDT-SWAP",
            "uid": "614488474791111"
        },
        "data":[
            {
                "instId": "BTC-USDT-SWAP",
                "fillSz": "100",
                "fillPx": "70000",
                "side": "buy",
                "ts": "1705449605015",
                "ordId": "680800019749904384",
                "clOrdId": "1234567890",
                "tradeId": "12345",
                "execType": "T",
                "count": "10"
            }
        ]
    }
    
    

#### Push data parameters

Parameter | Type | Description  
---|---|---  
arg | Object | Successfully subscribed channel  
> channel | String | Channel name  
> uid | String | User Identifier  
> instId | String | Instrument ID  
data | Array of objects | Subscribed data  
> instId | String | Instrument ID  
> fillSz | String | Filled quantity. If the trade is aggregated, the filled quantity will also be aggregated.  
> fillPx | String | Last filled price  
> side | String | Trade direction  
`buy` `sell`  
> ts | String | Filled time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
> ordId | String | Order ID  
> clOrdId | String | Client Order ID as assigned by the client  
> tradeId | String | The last trade ID in the trades aggregation  
> execType | String | Liquidity taker or maker, `T`: taker `M`: maker  
> count | String | The count of trades aggregated  
\- The channel is exclusively available to users with trading fee tier VIP4 or above. Others will receive error code 64003 when subscribing to it.   
\- The channel only pushes partial information of the orders channel. Fill events of block trading, nitro spread, liquidation, ADL, and some other non order book events will not be pushed through this channel. Users should also subscribe to the orders channel for order confirmation.   
\- When a fill event is received by this channel, the account balance, margin, and position information might not have changed yet.   
\- Taker orders will be aggregated based on different fill prices. When aggregation occurs, the count field indicates the number of orders matched, and the tradeId represents the tradeId of the last trade in the aggregation. Maker orders will not be aggregated.   
\- The channel returns clOrdId. The field will be returned upon trade execution. Note that the fills channel will only return this field if the user-provided clOrdId conforms to the signed int64 positive integer format (1-9223372036854775807, 2^63-1); if the user does not provide this field or if clOrdId does not meet the format requirements, the field will return "0". The order endpoints and channel will continue to return the user-provided clOrdId as usual. All request and response parameters are of string type.  
\- In the future, connection limits will be imposed on this channel. The maximum number of connections subscribing to this channel per subaccount will be 20. We recommend users always use this channel within this limit to avoid any impact on their strategies when the limit is enforced.

---

# WS / 成交频道

获取成交信息。该频道无首推，仅在订单簿成交相关事件触发时推送数据，tradeId > 0。

该频道仅适用于交易等级VIP4及以上的用户，其他用户接入将收到错误码64003。其他用户请使用[WS / 订单频道](/docs-v5/zh/#order-book-trading-trade-ws-order-channel)。

对于 `EVENTS`，无论实际订单是否为 YES 或 NO 方向，仅推送 YES 侧成交数据。

#### 服务地址

/ws/v5/private (需要登录)

> 请求示例：单个
    
    
    {
        "id": "1512",
        "op": "subscribe",
        "args": [
            {
                "channel": "fills",
                "instId": "BTC-USDT-SWAP"
            }
        ]
    }
    
    
    
    import asyncio
    
    from okx.websocket.WsPrivateAsync import WsPrivateAsync
    
    
    def callbackFunc(message):
        print(message)
    
    async def main():
    
        ws = WsPrivateAsync(
            apiKey = "YOUR_API_KEY",
            passphrase = "YOUR_PASSPHRASE",
            secretKey = "YOUR_SECRET_KEY",
            url = "wss://ws.okx.com:8443/ws/v5/private",
            useServerTime=False
        )
        await ws.start()
        args = [
            {
                "channel": "fills",
                "instId": "BTC-USDT-SWAP"
            }
        ]
    
        await ws.subscribe(args, callback=callbackFunc)
        await asyncio.sleep(10)
    
        await ws.unsubscribe(args, callback=callbackFunc)
        await asyncio.sleep(10)
    
    
    asyncio.run(main())
    

> 请求示例
    
    
    {
        "id": "1512",
        "op": "subscribe",
        "args": [
            {
                "channel": "fills"
            }
        ]
    }
    
    
    
    import asyncio
    
    from okx.websocket.WsPrivateAsync import WsPrivateAsync
    
    
    def callbackFunc(message):
        print(message)
    
    async def main():
    
        ws = WsPrivateAsync(
            apiKey = "YOUR_API_KEY",
            passphrase = "YOUR_PASSPHRASE",
            secretKey = "YOUR_SECRET_KEY",
            url = "wss://ws.okx.com:8443/ws/v5/private",
            useServerTime=False
        )
        await ws.start()
        args = [
            {
                "channel": "fills"
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
args | Array of objects | 是 | 订阅的频道  
> channel | String | 是 | 频道名  
`fills`  
> instId | String | 否 | 产品ID  
  
> 成功返回示例：单个
    
    
    {
      "id": "1512",
      "event": "subscribe",
      "arg": {
        "channel": "fills",
        "instId": "BTC-USDT-SWAP"
      },
      "connId": "a4d3ae55"
    }
    
    

> 成功返回示例
    
    
    {
      "id": "1512",
      "event": "subscribe",
      "arg": {
        "channel": "fills"
      },
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
> channel | String | 是 | 频道名  
`fills`  
> instId | String | 否 | 产品ID  
code | String | 否 | 错误码  
msg | String | 否 | 错误消息  
connId | String | 是 | WebSocket连接ID  
  
> 推送示例：单个
    
    
    {
        "arg": {
            "channel": "fills",
            "instId": "BTC-USDT-SWAP",
            "uid": "614488474791111"
        },
        "data":[
            {
                "instId": "BTC-USDT-SWAP",
                "fillSz": "100",
                "fillPx": "70000",
                "side": "buy",
                "ts": "1705449605015",
                "ordId": "680800019749904384",
                "clOrdId": "1234567890",
                "tradeId": "12345",
                "execType": "T",
                "count": "10"
            }
        ]
    }
    
    

#### 推送数据参数

参数名 | 类型 | 描述  
---|---|---  
arg | Object | 订阅成功的频道  
> channel | String | 频道名  
> uid | String | 用户标识  
> instId | String | 产品ID  
data | Array of objects | 订阅的数据  
> instId | String | 产品ID  
> fillSz | String | 成交数量，若这笔成交有聚合，则成交数量为聚合后的数量  
> fillPx | String | 成交价格  
> side | String | 订单方向  
`buy`  
`sell`  
> ts | String | 成交时间  
> ordId | String | 订单ID  
> clOrdId | String | 由用户设置的订单ID  
> tradeId | String | 成交ID  
若为taker订单且有聚合，则为聚合的多笔交易中最新一笔交易的成交ID  
> execType | String | 流动性方向  
`T`：taker  
`M`：maker  
> count | String | 聚合的订单匹配数量  
\- 该频道仅适用于交易等级VIP4及以上的用户，其他用户接入将收到错误码64003  
\- 该频道只推送部分订单频道的信息，与大宗交易、价差速递相关的成交，强平、自动减仓等非订单簿事件不会通过该频道推送。用户应同时关注订单频道，对订单做最终确认  
\- 该频道接收到成交推送时，账户余额、保证金、持仓等信息可能仍未发生变化  
\- taker订单将根据不同成交价格进行聚合，有聚合时，count字段表示聚合的订单匹配数量，tradeId代表聚合的多笔交易中最新一笔交易的ID；maker订单不会聚合  
\- 用户可以在下单时指定clOrdId，成交时会返回该字段。请注意，成交频道仅在用户输入的clOrdId符合带符号int64正整数格式（1-9223372036854775807, 2^63-1）时返回该字段；若用户未输入该字段，或clOrdId不符合格式要求，该字段将返回"0"。订单接口及频道将照常返回用户传入的clOrdId。所有请求及返回参数均为字符串类型。  
\- 未来，该频道将施加连接数量限制，子账户维度，订阅成交频道的最大连接数为20个。我们建议用户始终低于限制使用该频道，以免限制上线后对策略造成影响