---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#order-book-trading-algo-trading-ws-algo-orders-channel
anchor_id: order-book-trading-algo-trading-ws-algo-orders-channel
api_type: WebSocket
updated_at: 2026-07-15 19:18:47.529025
---

# WS / Algo orders channel

Retrieve algo orders (includes `trigger` order, `oco` order, `conditional` order). Data will not be pushed when first subscribed. Data will only be pushed when there are order updates.  
  
#### URL Path

/ws/v5/business (required login)

> Request Example : single
    
    
    {
      "id": "1512",
      "op": "subscribe",
      "args": [
        {
          "channel": "orders-algo",
          "instType": "FUTURES",
          "instFamily": "BTC-USD",
          "instId": "BTC-USD-200329"
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
              "channel": "orders-algo",
              "instType": "FUTURES",
              "instFamily": "BTC-USD",
              "instId": "BTC-USD-200329"
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
          "channel": "orders-algo",
          "instType": "FUTURES",
          "instFamily": "BTC-USD"
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
              "channel": "orders-algo",
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
`orders-algo`  
> instType | String | Yes | Instrument type   
`SPOT`  
`MARGIN`  
`SWAP`  
`FUTURES`   
`ANY`  
> instFamily | String | No | Instrument family  
Applicable to `FUTURES`/`SWAP`/`OPTION`  
> instId | String | No | Instrument ID  
  
> Successful Response Example : single
    
    
    {
      "id": "1512",
      "event": "subscribe",
      "arg": {
        "channel": "orders-algo",
        "instType": "FUTURES",
        "instFamily": "BTC-USD",
        "instId": "BTC-USD-200329"
      },
      "connId": "a4d3ae55"
    }
    

> Successful Response Example
    
    
    {
      "id": "1512",
      "event": "subscribe",
      "arg": {
        "channel": "orders-algo",
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
      "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{ \"channel\" : \"orders-algo\", \"instType\" : \"FUTURES\"}]}",
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
`SPOT`  
`MARGIN`  
`SWAP`  
`FUTURES`   
`ANY`  
> instFamily | String | No | Instrument family  
Applicable to `FUTURES`/`SWAP`/`OPTION`  
> instId | String | No | Instrument ID  
code | String | No | Error code  
msg | String | No | Error message  
connId | String | Yes | WebSocket connection ID  
  
> Push Data Example: single
    
    
    {
        "arg": {
            "channel": "orders-algo",
            "uid": "77982378738415879",
            "instType": "FUTURES",
            "instId": "BTC-USD-200329"
        },
        "data": [{
            "actualPx": "0",
            "actualSide": "",
            "actualSz": "0",
            "algoClOrdId": "",
            "algoId": "581878926302093312",
            "attachAlgoOrds": [],
            "amendResult": "",
            "cTime": "1685002746818",
            "uTime": "1708679675245",
            "ccy": "",
            "clOrdId": "",
            "closeFraction": "",
            "failCode": "",
            "instId": "BTC-USDC",
            "instType": "SPOT",
            "last": "26174.8",
            "lever": "0",
            "notionalUsd": "11.0",
            "ordId": "",
            "ordIdList": [],
            "ordPx": "",
            "ordType": "conditional",
            "posSide": "",
            "quickMgnType": "",
            "reduceOnly": "false",
            "reqId": "",
            "side": "buy",
            "slOrdPx": "",
            "slTriggerPx": "",
            "slTriggerPxType": "",
            "state": "live",
            "sz": "11",
            "tag": "",
            "tdMode": "cross",
            "tgtCcy": "quote_ccy",
            "tpOrdPx": "-1",
            "tpTriggerPx": "1",
            "tpTriggerPxType": "last",
            "triggerPx": "",
            "triggerTime": "",
            "tradeQuoteCcy": "USDT",
            "amendPxOnTriggerType": "0",
            "linkedOrd":{
                    "ordId":"98192973880283"
            },
            "isTradeBorrowMode": ""
        }]
    }
    

#### Response parameters when data is pushed.

**Parameter** | **Type** | **Description**  
---|---|---  
arg | Object | Successfully subscribed channel  
> channel | String | Channel name  
> uid | String | User Identifier  
> instType | String | Instrument type  
> instFamily | String | Instrument family  
> instId | String | Instrument ID  
data | Array of objects | Subscribed data  
> instType | String | Instrument type  
> instId | String | Instrument ID  
> ccy | String | Margin currency   
Applicable to all `isolated` `MARGIN` orders and `cross` `MARGIN` orders in `Futures mode`, `FUTURES` and `SWAP` contracts.  
> ordId | String | Latest order ID, the order ID associated with the algo order. It will be deprecated soon  
> ordIdList | Array of strings | Order ID list. There will be multiple order IDs when there is TP/SL splitting order.  
> algoId | String | Algo ID  
> clOrdId | String | Client Order ID as assigned by the client  
> sz | String | Quantity to buy or sell.  
`SPOT`/`MARGIN`: in the unit of currency.  
`FUTURES`/`SWAP`/`OPTION`: in the unit of contract.  
> ordType | String | Order type  
`conditional`: One-way stop order   
`oco`: One-cancels-the-other order   
`trigger`: Trigger order   
`chase`: Chase order  
> side | String | Order side  
`buy`  
`sell`  
> posSide | String | Position side   
`net`  
`long` or `short`  
Only applicable to `FUTURES`/`SWAP`  
> tdMode | String | Trade mode  
`cross`: cross  
`isolated`: isolated  
`cash`: cash  
> tgtCcy | String | Order quantity unit setting for `sz`  
`base_ccy`: Base currency  
`quote_ccy`: Quote currency  
Only applicable to `SPOT` Market Orders  
Default is `quote_ccy` for buy, `base_ccy` for sell  
> lever | String | Leverage, from `0.01` to `125`.   
Only applicable to `MARGIN/FUTURES/SWAP`  
> state | String | Order status   
`live`: to be effective   
`effective`: effective   
`canceled`: canceled   
`order_failed`: order failed  
`partially_failed`: partially failed  
`partially_effective`: partially effective  
> tpTriggerPx | String | Take-profit trigger price.  
> tpTriggerPxType | String | Take-profit trigger price type.   
`last`: last price  
`index`: index price  
`mark`: mark price  
> tpOrdPx | String | Take-profit order price.  
> slTriggerPx | String | Stop-loss trigger price.  
> slTriggerPxType | String | Stop-loss trigger price type.   
`last`: last price  
`index`: index price  
`mark`: mark price  
> slOrdPx | String | Stop-loss order price.  
> triggerPx | String | Trigger price  
> triggerPxType | String | Trigger price type.   
`last`: last price  
`index`: index price  
`mark`: mark price  
> ordPx | String | Order price for the trigger order  
> advanceOrdType | String | Trigger order type  
> last | String | Last filled price while placing  
> actualSz | String | Actual order quantity  
> actualPx | String | Actual order price  
> notionalUsd | String | Estimated national value in `USD` of order  
> tag | String | Order tag  
> actualSide | String | Actual trigger side  
Only applicable to oco order and conditional order  
> triggerTime | String | Trigger time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
> reduceOnly | String | Whether the order can only reduce the position size. Valid options: `true` or `false`.  
> failCode | String | It represents that the reason that algo order fails to trigger. It is "" when the state is `effective`/`canceled`. There will be value when the state is `order_failed`, e.g. 51008;  
Only applicable to Stop Order, Trailing Stop Order, Trigger order.  
> algoClOrdId | String | Client Algo Order ID as assigned by the client.  
> reqId | String | Client Request ID as assigned by the client for order amendment. "" will be returned if there is no order amendment.  
> amendResult | String | The result of amending the order  
`-1`: failure   
`0`: success  
> amendPxOnTriggerType | String | Whether to enable Cost-price SL. Only applicable to SL order of split TPs.   
`0`: disable, the default value   
`1`: Enable  
> attachAlgoOrds | Array of objects | Attached TP/SL or trailing stop order info  
Applicable to `Futures mode/Multi-currency margin/Portfolio margin`  
>> attachAlgoClOrdId | String | Client-supplied Algo ID when placing order with attached TP/SL or trailing stop.  
A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters.  
It will be posted to algoClOrdId when placing the attached algo order once the general order is filled completely.  
>> tpTriggerPx | String | Take-profit trigger price  
If you fill in this parameter, you should fill in the take-profit order price as well.  
>> tpTriggerRatio | String | Take-profit trigger ratio, 0.3 represents 30%. Only applicable to `FUTURES`/`SWAP` contracts.  
>> tpTriggerPxType | String | Take-profit trigger price type  
`last`: last price  
`index`: index price  
`mark`: mark price  
>> tpOrdPx | String | Take-profit order price  
If you fill in this parameter, you should fill in the take-profit trigger price as well.   
If the price is `-1`, take-profit will be executed at the market price.  
>> slTriggerPx | String | Stop-loss trigger price  
If you fill in this parameter, you should fill in the stop-loss order price.  
>> slTriggerRatio | String | Stop-loss trigger ratio, 0.3 represents 30%. Only applicable to `FUTURES`/`SWAP` contracts.  
>> slTriggerPxType | String | Stop-loss trigger price type  
`last`: last price  
`index`: index price  
`mark`: mark price  
>> slOrdPx | String | Stop-loss order price   
If you fill in this parameter, you should fill in the stop-loss trigger price.   
If the price is `-1`, stop-loss will be executed at the market price.  
>> callbackRatio | String | Callback ratio, e.g. `0.05` represents 5%  
>> callbackSpread | String | Callback spread (price distance)  
>> activePx | String | Activation price  
> linkedOrd | Object | Linked TP order detail, only applicable to SL order that comes from the one-cancels-the-other (OCO) order that contains the TP limit order.  
>> ordId | String | Order ID  
> cTime | String | Creation time Unix timestamp format in milliseconds, e.g. `1597026383085`  
> uTime | String | Order updated time, Unix timestamp format in milliseconds, e.g. 1597026383085  
> isTradeBorrowMode | String | Whether borrowing currency automatically  
true  
false  
Only applicable to `trigger order`, `trailing order` and `twap order`  
> chaseType | String | Chase type. Only applicable to `chase` order.  
> chaseVal | String | Chase value. Only applicable to `chase` order.  
> maxChaseType | String | Maximum chase type. Only applicable to `chase` order.  
> maxChaseVal | String | Maximum chase value. Only applicable to `chase` order.  
> tradeQuoteCcy | String | The quote currency used for trading.

---

# WS / 策略委托订单频道

获取策略委托订单，首次订阅不推送，只有当下单、撤单等事件触发时，推送数据  
  
#### 服务地址

/ws/v5/business (需要登录)

> 请求示例：单个
    
    
    {
        "id": "1512",
        "op": "subscribe",
        "args": [{
            "channel": "orders-algo",
            "instType": "FUTURES",
            "instFamily": "BTC-USD",
            "instId": "BTC-USD-200329"
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
            "channel": "orders-algo",
            "instType": "FUTURES",
            "instFamily": "BTC-USD",
            "instId": "BTC-USD-200329"
        }]
    
        await ws.subscribe(args, callback=callbackFunc)
        await asyncio.sleep(10)
    
        await ws.unsubscribe(args, callback=callbackFunc)
        await asyncio.sleep(10)
    
    
    asyncio.run(main())
    
    

> 请求示例
    
    
    {
        "id": "1512",
        "op": "subscribe",
        "args": [{
            "channel": "orders-algo",
            "instType": "FUTURES",
            "instFamily": "BTC-USD"
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
            "channel": "orders-algo",
            "instType": "FUTURES",
            "instFamily": "BTC-USD"
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
`orders-algo`  
> instType | String | 是 | 产品类型  
`SPOT`：币币  
`MARGIN`：币币杠杆  
`SWAP`：永续合约  
`FUTURES`：交割合约  
`ANY`：全部  
> instFamily | String | 否 | 交易品种  
适用于`交割`/`永续`/`期权`  
> instId | String | 否 | 产品ID  
  
> 成功返回示例：单个
    
    
    {
        "id": "1512",
        "event": "subscribe",
        "arg": {
            "channel": "orders-algo",
            "instType": "FUTURES",
            "instFamily": "BTC-USD",
            "instId": "BTC-USD-200329"
        },
        "connId": "a4d3ae55"
    }
    

> 成功返回示例
    
    
    {
        "id": "1512",
        "event": "subscribe",
        "arg": {
            "channel": "orders-algo",
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
        "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{ \"channel\" : \"orders-algo\", \"instType\" : \"FUTURES\"}]}",
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
`SPOT`：币币  
`MARGIN`：币币杠杆  
`SWAP`：永续合约  
`FUTURES`：交割合约  
`ANY`：全部  
> instFamily | String | 否 | 交易品种  
适用于`交割`/`永续`/`期权`  
> instId | String | 否 | 产品ID  
code | String | 否 | 错误码  
msg | String | 否 | 错误消息  
connId | String | 是 | WebSocket连接ID  
  
> 推送示例：单个
    
    
    {
        "arg": {
            "channel": "orders-algo",
            "uid": "77982378738415879",
            "instType": "FUTURES",
            "instId": "BTC-USD-200329"
        },
        "data": [{
            "actualPx": "0",
            "actualSide": "",
            "actualSz": "0",
            "algoClOrdId": "",
            "algoId": "581878926302093312",
            "attachAlgoOrds": [],
            "amendResult": "",
            "cTime": "1685002746818",
            "uTime": "1708679675245",
            "ccy": "",
            "clOrdId": "",
            "closeFraction": "",
            "failCode": "",
            "instId": "BTC-USDC",
            "instType": "SPOT",
            "last": "26174.8",
            "lever": "0",
            "notionalUsd": "11.0",
            "ordId": "",
            "ordIdList": [],
            "ordPx": "",
            "ordType": "conditional",
            "posSide": "",
            "quickMgnType": "",
            "reduceOnly": "false",
            "reqId": "",
            "side": "buy",
            "slOrdPx": "",
            "slTriggerPx": "",
            "slTriggerPxType": "",
            "state": "live",
            "sz": "11",
            "tag": "",
            "tdMode": "cross",
            "tgtCcy": "quote_ccy",
            "tpOrdPx": "-1",
            "tpTriggerPx": "1",
            "tpTriggerPxType": "last",
            "triggerPx": "",
            "triggerTime": "",
            "tradeQuoteCcy": "USDC",
            "amendPxOnTriggerType": "0",
            "linkedOrd":{
                "ordId":"98192973880283"
            },
            "isTradeBorrowMode": ""
        }]
    }
    

#### 推送数据参数

**参数名** | **类型** | **描述**  
---|---|---  
arg | Object | 订阅成功的频道  
> channel | String | 频道名  
> uid | String | 用户标识  
> instType | String | 产品类型  
> instFamily | String | 交易品种  
适用于`交割`/`永续`/`期权`  
> instId | String | 产品ID  
data | Array of objects | 订阅的数据  
> instType | String | 产品类型  
> instId | String | 产品ID  
> ccy | String | 保证金币种，适用于`逐仓杠杆`及`合约模式`下的`全仓杠杆`订单以及交割、永续和期权合约订单。  
> ordId | String | 最新一笔订单ID，与策略委托订单关联的订单ID，即将废弃。  
> ordIdList | Array of strings | 订单ID列表，当止盈止损存在市价拆单时，会有多个。  
> algoId | String | 策略委托单ID  
> clOrdId | String | 客户自定义订单ID  
> sz | String | 委托数量，`币币/币币杠杆` 以币为单位；`交割`/`永续`/`期权` 以张为单位  
> ordType | String | 订单类型  
`conditional`：单向止盈止损   
`oco`：双向止盈止损  
`trigger`：计划委托   
`chase`：追逐限价委托  
> side | String | 订单方向，`buy` `sell`  
> posSide | String | 持仓方向   
`long`：开平仓模式开多  
`short`：开平仓模式开空  
`net`：买卖模式  
> tdMode | String | 交易模式  
保证金模式 `cross`：全仓 `isolated`：逐仓   
非保证金模式 `cash`：现金  
> tgtCcy | String | 币币市价单委托数量`sz`的单位  
`base_ccy`：交易货币  
`quote_ccy`：计价货币  
仅适用于`币币`市价订单  
默认买单为`quote_ccy`，卖单为`base_ccy`  
> lever | String | 杠杆倍数，0.01到125之间的数值，仅适用于 `币币杠杆/交割/永续`  
> state | String | 订单状态   
`live`：待生效  
`effective`：已生效  
`canceled`：已撤销  
`order_failed`：委托失败  
`partially_failed`：部分委托失败  
`partially_effective`: 部分生效  
> tpTriggerPx | String | 止盈触发价  
> tpTriggerPxType | String | 止盈触发价类型  
`last`：最新价格  
`index`：指数价格  
`mark`：标记价格  
> tpOrdPx | String | 止盈委托价，委托价格为`-1`时，执行市价止盈  
> slTriggerPx | String | 止损触发价  
> slTriggerPxType | String | 止损触发价类型  
`last`：最新价格  
`index`：指数价格  
`mark`：标记价格  
> slOrdPx | String | 止损委托价委托价格为`-1`时，执行市价止损  
> triggerPx | String | 计划委托单的触发价格  
> triggerPxType | String | 计划委托单的触发价类型  
`last`：最新价格  
`index`：指数价格  
`mark`：标记价格  
> ordPx | String | 计划委托单的委托价格  
> advanceOrdType | String | 计划委托订单类型  
> last | String | 下单时的最新成交价  
> actualSz | String | 实际委托量  
> actualPx | String | 实际委价  
> tag | String | 订单标签  
> notionalUsd | String | 委托单预估美元价值  
> actualSide | String | 实际触发方向  
`sl`：止损  
`tp`：止盈  
仅适用于`单向止盈止损委托`和`双向止盈止损委托`  
> triggerTime | String | 策略委托触发时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
> reduceOnly | String | 是否只减仓，`true` 或 `false`  
> failCode | String | 代表策略触发失败的原因，已撤销和已生效时为""，委托失败时有值，如 51008；  
仅适用于单向止盈止损委托、双向止盈止损委托、移动止盈止损委托、计划委托。  
> algoClOrdId | String | 客户自定义策略订单ID  
> reqId | String | 修改订单时使用的request ID，如果没有修改，该字段为""  
> amendResult | String | 修改订单的结果  
`-1`：失败  
`0`：成功  
> amendPxOnTriggerType | String | 是否启用开仓价止损，仅适用于分批止盈的止损订单  
`0`：不开启，默认值   
`1`：开启  
> attachAlgoOrds | Array of objects | 附带止盈止损或移动止盈止损订单信息  
适用于`合约模式/跨币种保证金模式/组合保证金模式`  
>> attachAlgoClOrdId | String | 下单附带止盈止损或移动止盈止损时，客户自定义的策略订单ID，字母（区分大小写）与数字的组合，可以是纯字母、纯数字且长度要在1-32位之间。  
订单完全成交，下附带策略委托单时，该值会传给algoClOrdId。  
>> tpTriggerPx | String | 止盈触发价，如果填写此参数，必须填写`止盈委托价`  
>> tpTriggerRatio | String | 止盈触发比例，0.3 代表 30%   
仅适用于`交割`/`永续`合约  
>> tpTriggerPxType | String | 止盈触发价类型  
`last`：最新价格  
`index`：指数价格  
`mark`：标记价格  
>> tpOrdPx | String | 止盈委托价，如果填写此参数，必须填写`止盈触发价`  
委托价格为`-1`时，执行市价止盈  
>> slTriggerPx | String | 止损触发价，如果填写此参数，必须填写`止损委托价`  
>> slTriggerRatio | String | 止损触发比例，0.3 代表 30%   
仅适用于`交割`/`永续`合约  
>> slTriggerPxType | String | 止损触发价类型  
`last`：最新价格  
`index`：指数价格  
`mark`：标记价格  
>> slOrdPx | String | 止损委托价，如果填写此参数，必须填写`止损触发价`  
委托价格为`-1`时，执行市价止损  
>> callbackRatio | String | 回调幅度的比例，如 `0.05` 代表 5%  
>> callbackSpread | String | 回调幅度的价距  
>> activePx | String | 激活价格  
> linkedOrd | Object | 止盈订单信息，仅适用于止损单，且该止损订单来自包含限价止盈单的双向止盈止损订单  
>> ordId | String | 订单 ID  
> cTime | String | 订单创建时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
> uTime | String | 订单更新时间，Unix时间戳的毫秒数格式，如 1597026383085  
> isTradeBorrowMode | String | 是否自动借币  
true：自动借币  
false：不自动借币  
仅适用于计划委托、移动止盈止损和 时间加权策略  
> chaseType | String | 追逐类型。仅适用于`追逐限价委托`。  
> chaseVal | String | 追逐值。仅适用于`追逐限价委托`。  
> maxChaseType | String | 最大追逐值的类型。仅适用于`追逐限价委托`。  
> maxChaseVal | String | 最大追逐值。仅适用于`追逐限价委托`。  
> tradeQuoteCcy | String | 用于交易的计价币种。