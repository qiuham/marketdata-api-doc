---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#order-book-trading-grid-trading-ws-grid-positions-channel
anchor_id: order-book-trading-grid-trading-ws-grid-positions-channel
api_type: WebSocket
updated_at: 2026-05-27 19:35:07.020221
---

# WS / Grid positions channel

Retrieve contract grid positions. Data will be pushed when triggered by events such as placing/canceling order.  
Please ignore the empty data.  
  
#### URL Path

/ws/v5/business (required login)

> Request Example
    
    
    {
        "id": "1512",
        "op": "subscribe",
        "args": [{
            "channel": "grid-positions",
            "algoId": "449327675342323712"
        }]
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
        args = [{
            "channel": "grid-positions",
            "algoId": "449327675342323712"
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
`grid-positions`  
> algoId | String | Yes | Algo Order ID  
  
> Successful Response Example
    
    
    {
        "id": "1512",
        "event": "subscribe",
        "arg": {
            "channel": "grid-positions",
            "algoId": "449327675342323712"
        },
        "connId": "a4d3ae55"
    }
    

> Failure Response Example
    
    
    {
      "id": "1512",
      "event": "error",
      "code": "60012",
      "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{ \"channel\" : \"grid-positions\", \"instType\" : \"FUTURES\"}]}",
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
> algoId | String | Yes | Algo Order ID  
code | String | No | Error code  
msg | String | No | Error message  
connId | String | Yes | WebSocket connection ID  
  
> Push Data Example: 
    
    
    {
        "arg": {
            "channel": "grid-positions",
            "uid": "4470****9584",
            "algoId": "449327675342323712"
        },
        "data": [{
            "adl": "1",
            "algoClOrdId": "",
            "algoId": "449327675342323712",
            "avgPx": "29181.4638888888888895",
            "cTime": "1653400065917",
            "ccy": "USDT",
            "imr": "2089.2690000000002",
            "instId": "BTC-USDT-SWAP",
            "instType": "SWAP",
            "last": "29852.7",
            "lever": "5",
            "liqPx": "604.7617536513744",
            "markPx": "29849.7",
            "mgnMode": "cross",
            "mgnRatio": "217.71740878394456",
            "mmr": "41.78538",
            "notionalUsd": "10435.794191550001",
            "pTime": "1653536068723",
            "pos": "35",
            "posSide": "net",
            "uTime": "1653445498682",
            "upl": "232.83263888888962",
            "uplRatio": "0.1139826489932205"
        }]
    }
    

#### Response parameters when data is pushed.

**Parameter** | **Type** | **Description**  
---|---|---  
arg | Object | Successfully subscribed channel  
> channel | String | Channel name  
> uid | String | User Identifier  
> algoId | String | Algo Order ID  
data | Array of objects | Subscribed data  
> algoId | String | Algo ID  
> algoClOrdId | String | Client-supplied Algo ID  
> instType | String | Instrument type  
> instId | String | Instrument ID  
> cTime | String | Algo order created time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
> uTime | String | Algo order updated time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
> avgPx | String | Average open price  
> ccy | String | Margin currency  
> lever | String | Leverage  
> liqPx | String | Estimated liquidation price  
> posSide | String | Position side  
`net`  
> pos | String | Quantity of positions  
> mgnMode | String | Margin mode  
`cross`  
`isolated`  
> mgnRatio | String | Maintenance margin ratio  
> imr | String | Initial margin requirement  
> mmr | String | Maintenance margin requirement  
> upl | String | Unrealized profit and loss  
> uplRatio | String | Unrealized profit and loss ratio  
> last | String | Latest traded price  
> notionalUsd | String | Notional value of positions in `USD`  
> adl | String | Automatic-Deleveraging, signal area  
Divided into 5 levels, from 1 to 5, the smaller the number, the weaker the adl intensity.  
> markPx | String | Mark price  
> pTime | String | Push time of positions information, Unix timestamp format in milliseconds, e.g. `1597026383085`

---

# WS / 合约网格持仓频道

支持网格策略持仓的首次订阅推送，定时推送和事件推送  
请忽略空数据  
  
#### 服务地址

/ws/v5/business (需要登录)

> 请求示例
    
    
    {
        "id": "1512",
        "op": "subscribe",
        "args": [{
            "channel": "grid-positions",
            "algoId": "449327675342323712"
        }]
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
        args = [{
            "channel": "grid-positions",
            "algoId": "449327675342323712"
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
`grid-positions`  
> algoId | String | 是 | 策略ID  
  
> 成功返回示例
    
    
    {
        "id": "1512",
        "event": "subscribe",
        "arg": {
            "channel": "grid-positions",
            "algoId": "449327675342323712"
        },
        "connId": "a4d3ae55"
    }
    

> 失败返回示例
    
    
    {
        "id": "1512",
        "event": "error",
        "code": "60012",
        "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{ \"channel\" : \"grid-positions\", \"instType\" : \"FUTURES\"}]}",
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
> algoId | String | 是 | 策略ID  
code | String | 否 | 错误码  
msg | String | 否 | 错误消息  
connId | String | 是 | WebSocket连接ID  
  
> 推送示例
    
    
    {
        "arg": {
            "channel": "grid-positions",
            "uid": "4470****9584",
            "algoId": "449327675342323712"
        },
        "data": [{
            "adl": "1",
            "algoClOrdId": "",
            "algoId": "449327675342323712",
            "avgPx": "29181.4638888888888895",
            "cTime": "1653400065917",
            "ccy": "USDT",
            "imr": "2089.2690000000002",
            "instId": "BTC-USDT-SWAP",
            "instType": "SWAP",
            "last": "29852.7",
            "lever": "5",
            "liqPx": "604.7617536513744",
            "markPx": "29849.7",
            "mgnMode": "cross",
            "mgnRatio": "217.71740878394456",
            "mmr": "41.78538",
            "notionalUsd": "10435.794191550001",
            "pTime": "1653536068723",
            "pos": "35",
            "posSide": "net",
            "uTime": "1653445498682",
            "upl": "232.83263888888962",
            "uplRatio": "0.1139826489932205"
        }]
    }
    

#### 推送数据参数

**参数名** | **类型** | **描述**  
---|---|---  
arg | Object | 订阅成功的频道  
> channel | String | 频道名  
> uid | String | 用户标识  
> algoId | String | 策略订单ID  
data | Array of objects | 订阅的数据  
> algoId | String | 策略订单ID  
> algoClOrdId | String | 用户自定义策略ID  
> instType | String | 产品类型  
> instId | String | 产品ID  
> cTime | String | 策略订单创建时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
> uTime | String | 策略订单更新时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
> avgPx | String | 开仓均价  
> ccy | String | 保证金币种  
> lever | String | 杠杆倍数  
> liqPx | String | 预估强平价  
> posSide | String | 持仓方向  
`net`：买卖模式  
> pos | String | 持仓数量  
> mgnMode | String | 保证金模式  
`cross`：全仓  
`isolated`：逐仓  
> mgnRatio | String | 维持保证金率  
> imr | String | 初始保证金  
> mmr | String | 维持保证金  
> upl | String | 未实现收益  
> uplRatio | String | 未实现收益率  
> last | String | 最新成交价  
> notionalUsd | String | 仓位美金价值  
> adl | String | 自动减仓信号区  
分为5档，从1到5，数字越小代表adl强度越弱  
> markPx | String | 标记价格  
> pTime | String | 订单信息的推送时间，Unix时间戳的毫秒数格式，如 `1597026383085`