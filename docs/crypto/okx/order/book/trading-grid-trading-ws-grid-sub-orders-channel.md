---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#order-book-trading-grid-trading-ws-grid-sub-orders-channel
anchor_id: order-book-trading-grid-trading-ws-grid-sub-orders-channel
api_type: WebSocket
updated_at: 2026-07-11 19:12:48.295809
---

# WS / Grid sub orders channel

Retrieve grid sub orders. Data will be pushed when triggered by events such as placing order.  
Please ignore the empty data.  
  
#### URL Path

/ws/v5/business (required login)

> Request Example
    
    
    {
        "id": "1512",
        "op": "subscribe",
        "args": [{
            "channel": "grid-sub-orders",
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
            "channel": "grid-sub-orders",
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
`grid-sub-orders`  
> algoId | String | Yes | Algo Order ID  
  
> Successful Response Example
    
    
    {
        "id": "1512",
        "event": "subscribe",
        "arg": {
            "channel": "grid-sub-orders",
            "algoId": "449327675342323712"
        },
        "connId": "a4d3ae55"
    }
    

> Failure Response Example
    
    
    {
      "id": "1512",
      "event": "error",
      "code": "60012",
      "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{ \"channel\" : \"grid-sub-orders\", \"instType\" : \"FUTURES\"}]}",
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
            "channel": "grid-sub-orders",
            "uid": "44705892343619584",
            "algoId": "449327675342323712"
        },
        "data": [{
            "accFillSz": "0",
            "algoClOrdId": "",
            "algoId": "449327675342323712",
            "algoOrdType": "contract_grid",
            "avgPx": "0",
            "cTime": "1653445498664",
            "ctVal": "0.01",
            "fee": "0",
            "feeCcy": "USDT",
            "groupId": "-1",
            "instId": "BTC-USDT-SWAP",
            "instType": "SWAP",
            "lever": "5",
            "ordId": "449518234142904321",
            "ordType": "limit",
            "pTime": "1653486524502",
            "pnl": "",
            "posSide": "net",
            "px": "28007.2",
            "rebate": "0",
            "rebateCcy": "USDT",
            "side": "buy",
            "state": "live",
            "sz": "1",
            "tag":"",
            "tdMode": "cross",
            "uTime": "1653445498674"
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
> algoOrdType | String | Algo order type  
`grid`: Spot grid  
`contract_grid`: Contract grid  
> groupId | String | Group ID  
> ordId | String | Sub order ID  
> cTime | String | Sub order created time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
> uTime | String | Sub order updated time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
> tdMode | String | Sub order trade mode  
Margin mode `cross` `isolated`  
Non-Margin mode `cash`  
> tag | String | Order tag  
> ordType | String | Sub order type  
`market`: Market order  
`limit`: Limit order  
`ioc`: Immediate-or-cancel order  
> sz | String | Sub order quantity to buy or sell  
> state | String | Sub order state  
`canceled`  
`live`  
`partially_filled`  
`filled`  
`cancelling`  
> side | String | Sub order side  
`buy` `sell`  
> px | String | Sub order price  
> fee | String | Sub order fee amount  
> feeCcy | String | Sub order fee currency  
> rebate | String | Sub order rebate amount  
> rebateCcy | String | Sub order rebate currency  
> avgPx | String | Sub order average filled price  
> accFillSz | String | Sub order accumulated fill quantity  
> posSide | String | Sub order position side  
`net`  
> pnl | String | Sub order profit and loss  
> ctVal | String | Contract value  
Only applicable to `FUTURES`/`SWAP`/`OPTION`  
> lever | String | Leverage  
> pTime | String | Push time of orders information, Unix timestamp format in milliseconds, e.g. `1597026383085`

---

# WS / 网格策略子订单频道

支持网格策略子订单的事件推送  
请忽略空数据  
  
#### 服务地址

/ws/v5/business (需要登录)

> 请求示例
    
    
    {
        "id": "1512",
        "op": "subscribe",
        "args": [{
            "channel": "grid-sub-orders",
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
            "channel": "grid-sub-orders",
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
`grid-sub-orders`  
> algoId | String | 是 | 策略ID  
  
> 成功返回示例
    
    
    {
        "id": "1512",
        "event": "subscribe",
        "arg": {
            "channel": "grid-sub-orders",
            "algoId": "449327675342323712"
        },
        "connId": "a4d3ae55"
    }
    

> 失败返回示例
    
    
    {
        "id": "1512",
        "event": "error",
        "code": "60012",
        "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{ \"channel\" : \"grid-sub-orders\", \"instType\" : \"FUTURES\"}]}",
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
            "channel": "grid-sub-orders",
            "uid": "44705892343619584",
            "algoId": "449327675342323712"
        },
        "data": [{
            "accFillSz": "0",
            "algoClOrdId": "",
            "algoId": "449327675342323712",
            "algoOrdType": "contract_grid",
            "avgPx": "0",
            "cTime": "1653445498664",
            "ctVal": "0.01",
            "fee": "0",
            "feeCcy": "USDT",
            "groupId": "-1",
            "instId": "BTC-USDT-SWAP",
            "instType": "SWAP",
            "lever": "5",
            "ordId": "449518234142904321",
            "ordType": "limit",
            "pTime": "1653486524502",
            "pnl": "",
            "posSide": "net",
            "px": "28007.2",
            "rebate": "0",
            "rebateCcy": "USDT",
            "side": "buy",
            "state": "live",
            "sz": "1",
            "tag":"",
            "tdMode": "cross",
            "uTime": "1653445498674"
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
> algoOrdType | String | 策略订单类型  
`grid`：现货网格委托  
`contract_grid`：合约网格委托  
> groupId | String | 组ID  
> ordId | String | 子订单ID  
> cTime | String | 子订单创建时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
> uTime | String | 子订单更新时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
> tag | String | 订单标签  
> tdMode | String | 子订单交易模式  
`cross`：全仓 `isolated`：逐仓 `cash`：非保证金  
> ordType | String | 子订单类型  
`market`：市价单 `limit`：限价单  
`ioc`：立即成交并取消剩余  
> sz | String | 子订单委托数量  
> state | String | 子订单状态  
`canceled`：撤单成功 `live`：等待成交 `partially_filled`：部分成交 `filled`：完全成交 `cancelling`：撤单中  
> side | String | 子订单订单方向  
`buy`：买 `sell`：卖  
> px | String | 子订单委托价格  
> fee | String | 子订单手续费数量  
> feeCcy | String | 子订单手续费币种  
> rebate | String | 子订单返佣数量  
> rebateCcy | String | 子订单返佣币种  
> avgPx | String | 子订单平均成交价格  
> accFillSz | String | 子订单累计成交数量  
> posSide | String | 子订单持仓方向  
`net`：买卖模式  
> pnl | String | 子订单收益  
> ctVal | String | 合约面值  
> lever | String | 杠杆倍数  
> pTime | String | 订单信息的推送时间，Unix时间戳的毫秒数格式，如 `1597026383085`