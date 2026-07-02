---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#order-book-trading-algo-trading-ws-advance-algo-orders-channel
anchor_id: order-book-trading-algo-trading-ws-advance-algo-orders-channel
api_type: WebSocket
updated_at: 2026-07-02 19:43:22.119299
---

# WS / Advance algo orders channel

Retrieve advance algo orders (including Iceberg order, TWAP order, Trailing order). Data will be pushed when first subscribed. Data will be pushed when triggered by events such as placing/canceling order.  
  
#### URL Path

/ws/v5/business (required login)

> Request Example : single
    
    
    {
      "id": "1512",
      "op": "subscribe",
      "args": [
        {
          "channel": "algo-advance",
          "instType": "SPOT",
          "instId": "BTC-USDT"
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
              "channel": "algo-advance",
              "instType": "SPOT",
              "instId": "BTC-USDT"
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
          "channel": "algo-advance",
          "instType": "SPOT"
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
              "channel": "algo-advance",
              "instType": "SPOT"
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
`algo-advance`  
> instType | String | Yes | Instrument type   
`SPOT`  
`MARGIN`  
`SWAP`  
`FUTURES`   
`ANY`  
> instId | String | No | Instrument ID  
> algoId | String | No | Algo Order ID  
  
> Successful Response Example : single
    
    
    {
      "id": "1512",
      "event": "subscribe",
      "arg": {
        "channel": "algo-advance",
        "instType": "SPOT",
        "instId": "BTC-USDT"
      },
      "connId": "a4d3ae55"
    }
    

> Successful Response Example
    
    
    {
      "id": "1512",
      "event": "subscribe",
      "arg": {
        "channel": "algo-advance",
        "instType": "SPOT"
      },
      "connId": "a4d3ae55"
    }
    

> Failure Response Example
    
    
    {
      "id": "1512",
      "event": "error",
      "code": "60012",
      "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{ \"channel\" : \"algo-advance\", \"instType\" : \"FUTURES\"}]}",
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
> instId | String | No | Instrument ID  
> algoId | String | No | Algo Order ID  
code | String | No | Error code  
msg | String | No | Error message  
connId | String | Yes | WebSocket connection ID  
  
> Push Data Example: single
    
    
    {
        "arg":{
            "channel":"algo-advance",
            "uid": "77982378738415879",
            "instType":"SPOT",
            "instId":"BTC-USDT"
        },
        "data":[
            {
                "actualPx":"",
                "actualSide":"",
                "actualSz":"0",
                "algoId":"355056228680335360",
                "cTime":"1630924001545",
                "ccy":"",
                "clOrdId": "",
                "count":"1",
                "instId":"BTC-USDT",
                "instType":"SPOT",
                "lever":"0",
                "notionalUsd":"",
                "ordPx":"",
                "ordType":"iceberg",
                "pTime":"1630924295204",
                "posSide":"net",
                "pxLimit":"10",
                "pxSpread":"1",
                "pxVar":"",
                "side":"buy",
                "slOrdPx":"",
                "slTriggerPx":"",
                "state":"pause",
                "sz":"0.1",
                "szLimit":"0.1",
                "tdMode":"cash",
                "timeInterval":"",
                "tpOrdPx":"",
                "tpTriggerPx":"",
                "tag": "adadadadad",
                "triggerPx":"",
                "triggerTime":"",
                "tradeQuoteCcy": "USDT",
                "callbackRatio":"",
                "callbackSpread":"",
                "activePx":"",
                "moveTriggerPx":"",
                "failCode": "",
                    "algoClOrdId": "",
                "reduceOnly": "",
                "isTradeBorrowMode": true
            }
        ]
    }
    

#### Response parameters when data is pushed.

**Parameter** | **Type** | **Description**  
---|---|---  
arg | Object | Successfully subscribed channel  
> channel | String | Channel name  
> uid | String | User Identifier  
> instType | String | Instrument type  
> instId | String | Instrument ID  
> algoId | String | Algo Order ID  
data | Array of objects | Subscribed data  
> instType | String | Instrument type  
> instId | String | Instrument ID  
> ccy | String | Margin currency   
Applicable to all `isolated` `MARGIN` orders and `cross` `MARGIN` orders in `Futures mode`, `FUTURES` and `SWAP` contracts.  
> ordId | String | Order ID, the order ID associated with the algo order.  
> algoId | String | Algo ID  
> clOrdId | String | Client Order ID as assigned by the client  
> sz | String | Quantity to buy or sell. `SPOT`/`MARGIN`: in the unit of currency. `FUTURES`/`SWAP`/`OPTION`: in the unit of contract.  
> side | String | Order side, `buy` `sell`  
> posSide | String | Position side   
`net`   
`long` or `short` Only applicable to `FUTURES`/`SWAP`  
> tdMode | String | Trade mode, `cross`: cross `isolated`: isolated `cash`: cash  
> tgtCcy | String | Order quantity unit setting for `sz`  
`base_ccy`: Base currency ,`quote_ccy`: Quote currency   
Only applicable to `SPOT` Market Orders  
Default is `quote_ccy` for buy, `base_ccy` for sell  
> lever | String | Leverage, from `0.01` to `125`.   
Only applicable to `MARGIN/FUTURES/SWAP`  
> state | String | Order status   
`live`: to be effective   
`effective`: effective  
`partially_effective`: partially effective  
`canceled`: canceled   
`order_failed`: order failed   
`pause`: pause  
> tpTriggerPx | String | Take-profit trigger price.  
> tpOrdPx | String | Take-profit order price.  
> slTriggerPx | String | Stop-loss trigger price.  
> slOrdPx | String | Stop-loss order price.  
> triggerPx | String | Trigger price  
> ordPx | String | Order price  
> actualSz | String | Actual order quantity  
> actualPx | String | Actual order price  
> notionalUsd | String | Estimated national value in `USD` of order  
> tag | String | Order tag  
> actualSide | String | Actual trigger side  
> triggerTime | String | Trigger time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
> cTime | String | Creation time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
> pxVar | String | Price ratio   
Only applicable to `iceberg` order or `twap` order  
> pxSpread | String | Price variance   
Only applicable to `iceberg` order or `twap` order  
> szLimit | String | Average amount   
Only applicable to `iceberg` order or `twap` order  
> pxLimit | String | Price limit   
Only applicable to `iceberg` order or `twap` order  
> timeInterval | String | Time interval   
Only applicable to `twap` order  
> count | String | Algo Order count   
Only applicable to `iceberg` order or `twap` order  
> callbackRatio | String | Callback price ratio  
Only applicable to `move_order_stop` order  
> callbackSpread | String | Callback price variance  
Only applicable to `move_order_stop` order  
> activePx | String | Active price  
Only applicable to `move_order_stop` order  
> moveTriggerPx | String | Trigger price  
Only applicable to `move_order_stop` order  
> failCode | String | It represents that the reason that algo order fails to trigger. It is "" when the state is `effective`/`canceled`. There will be value when the state is `order_failed`, e.g. 51008;  
Only applicable to Stop Order, Trailing Stop Order, Trigger order.  
> algoClOrdId | String | Client Algo Order ID as assigned by the client.  
> reduceOnly | String | Whether the order can only reduce the position size. Valid options: `true` or `false`.  
> pTime | String | Push time of algo order information, millisecond format of Unix timestamp, e.g. `1597026383085`  
> isTradeBorrowMode | Boolean | Whether borrowing currency automatically  
true  
false  
Only applicable to `trigger order`, `trailing order` and `twap order`  
> tradeQuoteCcy | String | The quote currency used for trading.

---

# WS / 高级策略委托订单频道

获取高级策略委托订单（冰山、时间加权、移动止盈止损），首次订阅推送，当下单、撤单等事件触发时，推送数据  
  
#### 服务地址

/ws/v5/business (需要登录)

> 请求示例：单个
    
    
    {
        "id": "1512",
        "op": "subscribe",
        "args": [{
            "channel": "algo-advance",
            "instType": "SPOT",
            "instId": "BTC-USDT"
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
        args = [
            {
              "channel": "algo-advance",
              "instType": "SPOT",
              "instId": "BTC-USDT"
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
        "args": [{
            "channel": "algo-advance",
            "instType": "SPOT",
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
            "channel": "algo-advance",
            "instType": "SPOT",
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
`algo-advance`  
> instType | String | 是 | 产品类型  
`SPOT`：币币  
`MARGIN`：币币杠杆  
`SWAP`：永续合约  
`FUTURES`：交割合约  
`ANY`：全部  
> instId | String | 否 | 产品ID  
> algoId | String | 否 | 策略ID  
  
> 成功返回示例：单个
    
    
    {
        "event": "subscribe",
        "arg": {
            "channel": "algo-advance",
            "instType": "SPOT",
            "instId": "BTC-USDT"
        },
        "connId": "a4d3ae55"
    }
    

> 成功返回示例
    
    
    {
        "event": "subscribe",
        "arg": {
            "channel": "algo-advance",
            "instType": "SPOT"
        },
        "connId": "a4d3ae55"
    }
    

> 失败返回示例
    
    
    {
        "event": "error",
        "code": "60012",
        "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{ \"channel\" : \"algo-advance\", \"instType\" : \"FUTURES\"}]}",
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
> instId | String | 否 | 产品ID  
> algoId | String | 否 | 策略ID  
code | String | 否 | 错误码  
msg | String | 否 | 错误消息  
connId | String | 是 | WebSocket连接ID  
  
> 推送示例：单个
    
    
    {
        "arg":{
            "channel":"algo-advance",
            "uid": "77982378738415879",
            "instType":"SPOT",
            "instId":"BTC-USDT"
        },
        "data":[
            {
                "actualPx":"",
                "actualSide":"",
                "actualSz":"0",
                "algoId":"355056228680335360",
                "cTime":"1630924001545",
                "ccy":"",
                "clOrdId": "",
                "count":"1",
                "instId":"BTC-USDT",
                "instType":"SPOT",
                "lever":"0",
                "notionalUsd":"",
                "ordPx":"",
                "ordType":"iceberg",
                "pTime":"1630924295204",
                "posSide":"net",
                "pxLimit":"10",
                "pxSpread":"1",
                "pxVar":"",
                "side":"buy",
                "slOrdPx":"",
                "slTriggerPx":"",
                "state":"pause",
                "sz":"0.1",
                "szLimit":"0.1",
                "tag": "adadadadad",
                "tdMode":"cash",
                "timeInterval":"",
                "tpOrdPx":"",
                "tpTriggerPx":"",
                "triggerPx":"",
                "triggerTime":"",
                "tradeQuoteCcy": "USDT",
                "callbackRatio":"",
                "callbackSpread":"",
                "activePx":"",
                "moveTriggerPx":"",
                "failCode": "",
                "algoClOrdId": "",
                "reduceOnly": "",
                "isTradeBorrowMode": true
            }
        ]
    }
    

#### 推送数据参数

**参数名** | **类型** | **描述**  
---|---|---  
arg | Object | 订阅成功的频道  
> channel | String | 频道名  
> uid | String | 用户标识  
> instType | String | 产品类型  
> instId | String | 产品ID  
> algoId | String | 策略ID  
data | Array of objects | 订阅的数据  
> instType | String | 产品类型  
> instId | String | 产品ID  
> ccy | String | 保证金币种，适用于`逐仓杠杆`及`合约模式`下的`全仓杠杆`订单  
> ordId | String | 订单ID，与策略委托订单关联的订单ID  
> algoId | String | 策略委托单ID  
> clOrdId | String | 客户自定义订单ID  
> sz | String | 委托数量，`币币/币币杠杆` 以币为单位；`交割`/`永续`/`期权` 以张为单位  
> side | String | 订单方向，`buy` `sell`  
> posSide | String | 持仓方向   
`long`：开平仓模式开多  
`short`：开平仓模式开空  
`net`：买卖模式  
> tdMode | String | 交易模式  
保证金模式 `cross`：全仓 `isolated`：逐仓   
非保证金模式 `cash`：现金  
> tgtCcy | String | 币币市价单委托数量`sz`的单位  
`base_ccy`: 交易货币 ；`quote_ccy`：计价货币  
仅适用于`币币`市价订单  
默认买单为`quote_ccy`，卖单为`base_ccy`  
> lever | String | 杠杆倍数，0.01到125之间的数值，仅适用于 `币币杠杆/交割/永续`  
> state | String | 订单状态  
`live`：待生效  
`effective`：已生效  
`partially_effective`：部分生效  
`canceled`：已撤销  
`order_failed`：委托失败  
`pause`: 暂停生效  
> tpTriggerPx | String | 止盈触发价  
> tpOrdPx | String | 止盈委托价，委托价格为`-1`时，执行市价止盈  
> slTriggerPx | String | 止损触发价  
> slOrdPx | String | 止损委托价委托价格为`-1`时，执行市价止损  
> triggerPx | String | 计划委托单的触发价格  
> ordPx | String | 计划委托单的委托价格  
> actualSz | String | 实际委托量  
> actualPx | String | 实际委价  
> tag | String | 订单标签  
字母（区分大小写）与数字的组合，可以是纯字母、纯数字，且长度在1-16位之间。  
> notionalUsd | String | 委托单预估美元价值  
> actualSide | String | 实际触发方向，`sl`：止损 `tp`：止盈  
> triggerTime | String | 策略委托触发时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
> cTime | String | 订单创建时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
> pxVar | String | 价格比例  
仅适用于`冰山委托`和`时间加权委托`  
> pxSpread | String | 价距  
仅适用于`冰山委托`和`时间加权委托`  
> szLimit | String | 单笔数量  
仅适用于`冰山委托`和`时间加权委托`  
> pxLimit | String | 挂单限制价  
仅适用于`冰山委托`和`时间加权委托`  
> timeInterval | String | 下单间隔  
仅适用于`时间加权委托`  
> count | String | 策略订单计数  
仅适用于`冰山委托`和`时间加权委托`  
> callbackRatio | String | 回调幅度的比例  
仅适用于`移动止盈止损`  
> callbackSpread | String | 回调幅度的价距  
仅适用于`移动止盈止损`  
> activePx | String | 移动止盈止损激活价格  
仅适用于`移动止盈止损`  
> failCode | String | 代表策略触发失败的原因，已撤销和已生效时为""，委托失败时有值，如 51008；  
仅适用于单向止盈止损委托、双向止盈止损委托、移动止盈止损委托、计划委托。  
> algoClOrdId | String | 客户自定义策略订单ID  
> moveTriggerPx | String | 移动止盈止损触发价格  
仅适用于`移动止盈止损`  
> reduceOnly | String | 是否只减仓，`true` 或 `false`  
> pTime | String | 订单信息的推送时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
> isTradeBorrowMode | Boolean | 是否自动借币  
true：自动借币  
false：不自动借币  
仅适用于计划委托、移动止盈止损和 时间加权策略  
> tradeQuoteCcy | String | 用于交易的计价币种。