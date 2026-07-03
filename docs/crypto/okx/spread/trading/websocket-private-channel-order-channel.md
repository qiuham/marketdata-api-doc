---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#spread-trading-websocket-private-channel-order-channel
anchor_id: spread-trading-websocket-private-channel-order-channel
api_type: WebSocket
updated_at: 2026-07-03 19:40:23.818140
---

# Order channel

Retrieve order information from the `sprd-order` Websocket channel. Data will not be pushed when first subscribed. Data will only be pushed when triggered by events such as placing/canceling order.  
  
#### URL Path

/ws/v5/business (required login)

> Request Example : single
    
    
    {
      "id": "1512",
      "op": "subscribe",
      "args": [
        {
          "channel": "sprd-orders",
          "sprdId": "BTC-USDT_BTC-USDT-SWAP"
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
            url = "wss://ws.okx.com:8443/ws/v5/business",
            useServerTime=False
        )
        await ws.start()
        args = [
            {
              "channel": "sprd-orders",
              "sprdId": "BTC-USDT_BTC-USDT-SWAP"
            }
        ]
    
        await ws.subscribe(args, callback=callbackFunc)
        await asyncio.sleep(10)
    
        await ws.unsubscribe(args, callback=callbackFunc)
        await asyncio.sleep(10)
    
    
    asyncio.run(main())
    

> Request Example:
    
    
    {
      "id": "1512",
      "op": "subscribe",
      "args": [
        {
          "channel": "sprd-orders",
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
            url = "wss://ws.okx.com:8443/ws/v5/business",
            useServerTime=False
        )
        await ws.start()
        args = [
            {
              "channel": "sprd-orders",
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
`sprd-orders`  
> sprdId | String | No | Spread ID  
  
> Successful Response Example : single
    
    
    {
      "id": "1512",
      "event": "subscribe",
      "arg": {
        "channel": "sprd-orders",
        "sprdId": "BTC-USDT_BTC-UST-SWAP"
      },
      "connId": "a4d3ae55"
    }
    

> Successful Response Example
    
    
    {
      "id": "1512",
      "event": "subscribe",
      "arg": {
        "channel": "sprd-orders"
      },
      "connId": "a4d3ae55"
    }
    

> Failure Response Example 
    
    
    {
      "id": "1512",
      "event": "error",
      "code": "60012",
      "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{ \"channel\" : \"sprd-orders\", \"instType\" : \"FUTURES\"}]}",
      "connId": "a4d3ae55"
    }
    
    

#### Response parameters

Parameter | Required | Type | Description  
---|---|---|---  
id | String | No | Unique identifier of the message  
event | Yes | String | Event  
`subscribe`  
`unsubscribe`  
`error`  
arg | No | Object | Subscribed channel  
> channel | Yes | String | Channel name  
> sprdId | No | String | Spread ID  
code | No | String | Error code  
msg | No | String | Error message  
connId | String | Yes | WebSocket connection ID  
  
> Push Data Example: single
    
    
    {
      "arg": {
            "channel": "sprd-orders",
            "sprdId": "BTC-USDT_BTC-USDT-SWAP",
            "uid": "614488474791936"
        },
      "data": [
         {
          "sprdId": "BTC-USDT_BTC-UST-SWAP",
          "ordId": "312269865356374016",
          "clOrdId": "b1",
          "tag": "",
          "px": "999",
          "sz": "3",
          "ordType": "limit",
          "side": "buy",
          "fillSz": "0",
          "fillPx": "",
          "tradeId": "",
          "accFillSz": "0",
          "pendingFillSz": "2",
          "pendingSettleSz": "1",
          "canceledSz": "1",
          "state": "live",
          "avgPx": "0",
          "cancelSource": "",
          "uTime": "1597026383085",
          "cTime": "1597026383085",
          "code": "0",
          "msg": "",
          "reqId": "",
          "amendResult": ""
        }
      ]
    }
    

#### Push data parameters

**Parameter** | **Type** | **Description**  
---|---|---  
arg | Object | Successfully subscribed channel  
> channel | String | Channel name  
> uid | String | User Identifier  
> sprdId | String | spread ID  
data | Array of objects | Subscribed data  
> sprdId | String | spread ID, e.g.  
> ordId | String | Order ID  
> clOrdId | String | Client Order ID as assigned by the client  
> tag | String | Order tag  
> px | String | Order price  
> sz | String | The original order quantity, in the unit of szCcy  
> ordType | String | Order type  
`market`: Market order   
`limit`: limit order   
`post_only`: Post-only order   
`ioc`: Immediate-or-cancel order  
> side | String | Order side, buy sell  
> fillSz | String | Last trade quantity, only applicable to order updates representing successful settlement  
> fillPx | String | Last trade price, only applicable to order updates representing successful settlement  
> tradeId | String | Last trade ID  
> accFillSz | String | Accumulated fill quantity  
> pendingFillSz | String | Quantity still remaining to be filled  
> pendingSettleSz | String | Quantity that's pending settlement  
> canceledSz | String | Quantity canceled due order cancellations or trade rejections  
> avgPx | String | Average filled price. If none is filled, it will return "0".  
> state | String | Order state:   
`canceled`   
`live`   
`partially_filled`   
`filled`  
> cancelSource | String | Source of the order cancellation.Valid values and the corresponding meanings are:   
`0`: Order canceled by system   
`1`: Order canceled by user   
`14`: Order canceled: IOC order was partially canceled due to incompletely filled  
`15`: Order canceled: The order price is beyond the limit  
`20`: Cancel all after triggered   
`31`: The post-only order will take liquidity in maker orders  
`32`: Self trade prevention   
`34`: Order failed to settle due to insufficient margin   
`35`: Order cancellation due to insufficient margin from another order  
`44`: Your order was canceled because your available balance of this crypto was insufficient for auto conversion. Auto conversion was triggered when the total collateralized liabilities for this crypto reached the platform’s risk control limit.  
> uTime | String | Update time, Unix timestamp format in milliseconds, e.g. 1597026383085  
> cTime | String | Creation time, Unix timestamp format in milliseconds, e.g. 1597026383085  
> code | String | Error Code, the default is 0  
> msg | String | Error Message, the default is ""  
> reqId | String | Client Request ID as assigned by the client for order amendment. "" will be returned if there is no order amendment.  
> amendResult | String | The result of amending the order   
`-1`: failure   
`0`: success  
"" will be returned if there is no order amendment.

---

# 订单频道

通过订阅`sprd-orders`频道获取Spread订单信息，首次订阅不推送，只有当下单、撤单等事件触发时，推送数据。  
  
#### 服务地址

/ws/v5/business (需要登录)

> 请求示例：单个
    
    
    {
      "id": "1512",
      "op": "subscribe",
      "args": [
        {
          "channel": "sprd-orders",
          "sprdId": "BTC-USDT_BTC-USDT-SWAP"
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
            url = "wss://ws.okx.com:8443/ws/v5/business",
            useServerTime=False
        )
        await ws.start()
        args = [
            {
              "channel": "sprd-orders",
              "sprdId": "BTC-USDT_BTC-USDT-SWAP"
            }
        ]
    
        await ws.subscribe(args, callback=callbackFunc)
        await asyncio.sleep(10)
    
        await ws.unsubscribe(args, callback=callbackFunc)
        await asyncio.sleep(10)
    
    
    asyncio.run(main())
    

> 请求示例：
    
    
    {
      "id": "1512",
      "op": "subscribe",
      "args": [
        {
          "channel": "sprd-orders",
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
            url = "wss://ws.okx.com:8443/ws/v5/business",
            useServerTime=False
        )
        await ws.start()
        args = [
            {
              "channel": "sprd-orders",
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
`sprd-orders`  
> sprdId | String | 是 | Spread ID  
  
> 成功返回示例：单个
    
    
    {
      "id": "1512",
      "event": "subscribe",
      "arg": {
        "channel": "sprd-orders",
        "sprdId": "BTC-USDT_BTC-UST-SWAP"
      },
      "connId": "a4d3ae55"
    }
    
    

> 成功返回示例
    
    
    {
      "id": "1512",
      "event": "subscribe",
      "arg": {
        "channel": "sprd-orders"
      },
      "connId": "a4d3ae55"
    }
    
    

> 失败返回示例
    
    
    {
      "id": "1512",
      "event": "error",
      "code": "60012",
      "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{ \"channel\" : \"sprd-orders\", \"instType\" : \"FUTURES\"}]}",
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
> sprdId | String | 否 | Spread ID  
code | String | 否 | 错误码  
msg | String | 否 | 错误消息  
connId | String | 是 | WebSocket连接ID  
  
> 推送示例：单个
    
    
    {
      "arg": {
            "channel": "sprd-orders",
            "sprdId": "BTC-USDT_BTC-USDT-SWAP",
            "uid": "614488474791936"
        },
      "data": [
         {
          "sprdId": "BTC-USDT_BTC-UST-SWAP",
          "ordId": "312269865356374016",
          "clOrdId": "b1",
          "tag": "",
          "px": "999",
          "sz": "3",
          "ordType": "limit",
          "side": "buy",
          "fillSz": "0",
          "fillPx": "",
          "tradeId": "",
          "accFillSz": "0",
          "pendingFillSz": "2",
          "pendingSettleSz": "1",
          "canceledSz": "1",
          "state": "live",
          "avgPx": "0",
          "cancelSource": "",
          "uTime": "1597026383085",
          "cTime": "1597026383085",
          "code": "0",
          "msg": "",
          "reqId": "",
          "amendResult": ""
        }
      ]
    
    }
    
    

#### 推送数据参数

参数名 | 类型 | 描述  
---|---|---  
arg | Object | 订阅成功的频道  
> channel | String | 频道名  
> uid | String | 用户标识  
> sprdId | String | spread ID  
data | Array of objects | 订阅的数据  
> sprdId | String | spread ID  
> ordId | String | 订单ID  
> clOrdId | String | 由用户设置的订单ID来识别您的订单  
> tag | String | 订单标签  
> px | String | 委托价格  
> sz | String | 原始委托数量，单位szCcy  
> ordType | String | 订单类型  
`market`：市价单   
`limit`：限价单   
`post_only`：只做maker单   
`ioc`：立即成交并取消剩余  
> side | String | 订单方向   
`buy`   
`sell`  
> fillSz | String | 最新成交数量，适用于结算成功的订单更新  
> fillPx | String | 最新成交价格，适用于结算成功的订单更新  
> tradeId | String | 最近成交ID  
> accFillSz | String | 累计成交数量  
> pendingFillSz | String | 待成交数量，包括待结算数量  
> pendingSettleSz | String | 待结算数量  
> canceledSz | String | 撤单数量  
> avgPx | String | 成交均价，如果成交数量为0，该字段为"0"  
> state | String | 订单状态  
`canceled`：撤单成功  
`live`：等待成交  
`partially_filled`：部分成交  
`filled`：完全成交  
> cancelSource | String | 撤单原因  
`0`: 系统撤单  
`1`: 用户撤单   
`14`: 已撤单：IOC 委托订单未完全成交，仅部分成交，导致部分挂单被撤回  
`15`: 已撤单：该订单委托价不在限价范围内  
`20`: 系统倒计时撤单  
`31`: 当前只挂单订单 (Post only) 将会吃掉挂单深度  
`32`: 自成交保护  
`34`: 订单结算失败因为保证金不足   
`35`: 撤单因为其他订单保证金不足  
`44`：由于该币种的可用余额不足，无法在触发自动换币后进行兑换，您的订单已撤销，撤销订单后恢复的余额将用于自动换币。当该币种的总抵押借贷量达到平台抵押借贷风控上限时，则会触发自动换币。  
> uTime | String | 订单更新时间，Unix时间戳的毫秒数格式，如 1597026383085  
> cTime | String | 订单创建时间，Unix时间戳的毫秒数格式，如 1597026383085  
> code | String | 错误码，默认为0  
> msg | String | 错误消息，默认为""  
> reqId | String | 修改订单时使用的request ID，如果没有修改，该字段为""  
> amendResult | String | 修改订单的结果  
`-1`：失败  
`0`：成功  
如果没有修改，该字段为""