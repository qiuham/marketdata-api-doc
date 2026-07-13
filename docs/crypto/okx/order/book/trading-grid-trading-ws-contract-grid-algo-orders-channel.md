---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#order-book-trading-grid-trading-ws-contract-grid-algo-orders-channel
anchor_id: order-book-trading-grid-trading-ws-contract-grid-algo-orders-channel
api_type: WebSocket
updated_at: 2026-07-13 19:27:43.350338
---

# WS / Contract grid algo orders channel

Retrieve contract grid algo orders. Data will be pushed when triggered by events such as placing/canceling order. It will also be pushed in regular interval according to subscription granularity.  
  
#### URL Path

/ws/v5/business (required login)

> Request Example
    
    
    {
      "id": "1512",
        "op": "subscribe",
        "args": [{
            "channel": "grid-orders-contract",
            "instType": "SWAP"
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
            "channel": "grid-orders-contract",
            "instType": "SWAP"
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
`grid-orders-contract`  
> instType | String | Yes | Instrument type  
`SWAP`  
`FUTURES`  
`ANY`  
> instId | String | No | Instrument ID  
> algoId | String | No | Algo Order ID  
  
> Successful Response Example
    
    
    {
        "id": "1512",
        "event": "subscribe",
        "arg": {
            "channel": "grid-orders-contract",
            "instType": "ANY"
        },
        "connId": "a4d3ae55"
    }
    

> Failure Response Example
    
    
    {
      "id": "1512",
      "event": "error",
      "code": "60012",
      "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{ \"channel\" : \"grid-orders-contract\", \"instType\" : \"FUTURES\"}]}",
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
> instId | String | No | Instrument ID  
> algoId | String | No | Algo Order ID  
code | String | No | Error code  
msg | String | No | Error message  
connId | String | Yes | WebSocket connection ID  
  
> Push Data Example: 
    
    
    {
        "arg": {
            "channel": "grid-orders-contract",
            "instType": "ANY",
            "uid": "4470****9584"
        },
        "data": [{
            "actualLever": "2.3481494635276649",
            "activeOrdNum": "10",
            "algoClOrdId": "",
            "algoId": "571039869070475264",
            "algoOrdType": "contract_grid",
            "annualizedRate": "0",
            "arbitrageNum": "0",
            "availEq": "52.3015392887089673",
            "basePos": true,
            "cTime": "1682418514204",
            "cancelType": "0",
            "direction": "long",
            "eq": "108.7945652387089673",
            "floatProfit": "8.7945652387089673",
            "gridNum": "10",
            "gridProfit": "0",
            "instId": "BTC-USDT-SWAP",
            "instType": "SWAP",
            "investment": "100",
            "lever": "5",
            "liqPx": "16370.482143120824",
            "maxPx": "36437.3",
            "minPx": "26931.9",
            "ordFrozen": "5.38638",
            "pTime": "1682492574068",
            "perMaxProfitRate": "0.1687494513302446",
            "perMinProfitRate": "0.1263869357706788",
            "pnlRatio": "0.0879456523870897",
            "rebateTrans": [{
                "rebate": "0",
                "rebateCcy": "USDT"
            }],
            "runPx": "27306.9",
            "runType": "1",
            "singleAmt": "1",
            "slTriggerPx": "",
            "state": "running",
            "stopType": "0",
            "sz": "100",
            "tag": "",
            "totalAnnualizedRate": "38.52019574554529",
            "totalPnl": "8.7945652387089673",
            "tpTriggerPx": "",
            "tradeNum": "9",
            "triggerParams": [{
                "triggerAction": "start",
                "delaySeconds": "0",
                "triggerStrategy": "price",
                "triggerPx": "1",
                "triggerType": "manual",
                "triggerTime": "1682418561497"
            }, {
                "triggerAction": "stop",
                "delaySeconds": "0",
                "triggerStrategy": "instant",
                "stopType": "1",
                "triggerType": "manual",
                "triggerTime": "0"
            }],
            "uTime": "1682492552257",
            "profitSharingRatio": "",
            "copyType": "0",
            "tpRatio": "",
            "slRatio": "",
            "fee": "",
            "fundingFee": ""
        }]
    }
    

#### Response parameters when data is pushed.

**Parameter** | **Type** | **Description**  
---|---|---  
arg | Object | Successfully subscribed channel  
> channel | String | Channel name  
> instType | String | Instrument type  
> uid | String | User ID  
data | Array of objects | Subscribed data  
> algoId | String | Algo ID  
> algoClOrdId | String | Client-supplied Algo ID  
> instType | String | Instrument type  
> instId | String | Instrument ID  
> cTime | String | Algo order created time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
> uTime | String | Algo order updated time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
> algoOrdType | String | Algo order type  
`contract_grid`: Contract grid  
> state | String | Algo order state  
`starting`  
`running`  
`stopping`  
`no_close_position`: stopped algo order but hadn't close position yet  
`stopped`  
> rebateTrans | Array of objects | Rebate transfer info  
>> rebate | String | Rebate amount  
>> rebateCcy | String | Rebate currency  
> triggerParams | Array of objects | Trigger Parameters  
>> triggerAction | String | Trigger action  
`start`  
`stop`  
>> triggerStrategy | String | Trigger strategy  
`instant`  
`price`  
`rsi`  
>> delaySeconds | String | Delay seconds after action triggered  
>> triggerTime | String | Actual action triggered time, unix timestamp format in milliseconds, e.g. `1597026383085`  
>> triggerType | String | Actual action triggered type  
`manual`  
`auto`  
>> timeframe | String | K-line type  
`3m`, `5m`, `15m`, `30m` (`m`: minute)  
`1H`, `4H` (`H`: hour)  
`1D` (`D`: day)  
This field is only valid when `triggerStrategy` is `rsi`  
>> thold | String | Threshold  
The value should be an integer between 1 to 100  
This field is only valid when `triggerStrategy` is `rsi`  
>> triggerCond | String | Trigger condition  
`cross_up`  
`cross_down`  
`above`  
`below`  
`cross`  
This field is only valid when `triggerStrategy` is `rsi`  
>> timePeriod | String | Time Period  
`14`  
This field is only valid when `triggerStrategy` is `rsi`  
>> triggerPx | String | Trigger Price  
This field is only valid when `triggerStrategy` is `price`  
>> stopType | String | Stop type  
Spot grid `1`: Sell base currency `2`: Keep base currency  
Contract grid `1`: Market Close All positions `2`: Keep positions  
This field is only valid when `triggerAction` is `stop`  
> maxPx | String | Upper price of price range  
> minPx | String | Lower price of price range  
> gridNum | String | Grid quantity  
> runType | String | Grid type  
`1`: Arithmetic, `2`: Geometric  
> tpTriggerPx | String | Take-profit trigger price  
> slTriggerPx | String | Stop-loss trigger price  
> tradeNum | String | The number of trades executed  
> arbitrageNum | String | The number of arbitrages executed  
> singleAmt | String | Amount per grid  
> perMinProfitRate | String | Estimated minimum Profit margin per grid  
> perMaxProfitRate | String | Estimated maximum Profit margin per grid  
> runPx | String | Price at launch  
> totalPnl | String | Total P&L  
> pnlRatio | String | P&L ratio  
> investment | String | Accumulated investment amount  
Spot grid investment amount calculated on quote currency  
> gridProfit | String | Grid profit  
> floatProfit | String | Variable P&L  
> totalAnnualizedRate | String | Total annualized rate  
> annualizedRate | String | Grid annualized rate  
> cancelType | String | Algo order stop reason  
`0`: None  
`1`: Manual stop  
`2`: Take profit  
`3`: Stop loss  
`4`: Risk control  
`5`: Delivery  
`6`: Signal  
> stopType | String | Stop type  
Spot grid `1`: Sell base currency `2`: Keep base currency  
Contract grid `1`: Market Close All positions `2`: Keep positions  
> direction | String | Contract grid type  
`long`,`short`,`neutral`  
Only applicable to `contract grid`  
> basePos | Boolean | Whether or not to open a position when the strategy is activated  
Only applicable to `contract grid`  
> sz | String | Used margin based on `USDT`  
Only applicable to `contract grid`  
> lever | String | Leverage  
Only applicable to `contract grid`  
> actualLever | String | Actual Leverage  
Only applicable to `contract grid`  
> liqPx | String | Estimated liquidation price  
Only applicable to `contract grid`  
> ordFrozen | String | Margin used by pending orders  
Only applicable to `contract grid`  
> availEq | String | Available margin  
Only applicable to `contract grid`  
> eq | String | Total equity of strategy account  
Only applicable to `contract grid`  
> activeOrdNum | String | Total count of pending sub orders  
> tag | String | Order tag  
> profitSharingRatio | String | Profit sharing ratio  
Value range [0, 0.3]  
If it is a normal order (neither copy order nor lead order), this field returns ""  
> copyType | String | Profit sharing order type  
`0`: Normal order  
`1`: Copy order without profit sharing  
`2`: Copy order with profit sharing  
`3`: Lead order  
> tpRatio | String | Take profit ratio, 0.1 represents 10%  
> slRatio | String | Stop loss ratio, 0.1 represents 10%  
> fee | String | Accumulated fee. Only applicable to contract grid, or it will be ""  
> fundingFee | String | Accumulated funding fee. Only applicable to contract grid, or it will be ""  
> pTime | String | Push time of algo grid information, Unix timestamp format in milliseconds, e.g. `1597026383085`

---

# WS / 合约网格策略委托订单频道

支持合约网格策略订单的定时推送和事件推送  
  
#### 服务地址

/ws/v5/business (需要登录)

> 请求示例
    
    
    {
        "id": "1512",
        "op": "subscribe",
        "args": [{
            "channel": "grid-orders-contract",
            "instType": "ANY"
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
            "channel": "grid-orders-contract",
            "instType": "SWAP"
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
`grid-orders-contract`  
> instType | String | 是 | 产品类型  
`SWAP`：永续  
`FUTURE`：交割  
`ANY`：全部  
> instId | String | 否 | 产品ID  
> algoId | String | 否 | 策略ID  
  
> 成功返回示例
    
    
    {
        "id": "1512",
        "event": "subscribe",
        "arg": {
            "channel": "grid-orders-contract",
            "instType": "ANY"
        },
        "connId": "a4d3ae55"
    }
    

> 失败返回示例
    
    
    {
        "id": "1512",
        "event": "error",
        "code": "60012",
        "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{ \"channel\" : \"grid-orders-contract\", \"instType\" : \"FUTURES\"}]}",
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
> instId | String | 否 | 产品ID  
> algoId | String | 否 | 策略ID  
code | String | 否 | 错误码  
msg | String | 否 | 错误消息  
connId | String | 是 | WebSocket连接ID  
  
> 推送示例
    
    
    {
        "arg": {
            "channel": "grid-orders-contract",
            "instType": "ANY",
            "uid": "4470****9584"
        },
        "data": [{
            "actualLever": "2.3481494635276649",
            "activeOrdNum": "10",
            "algoClOrdId": "",
            "algoId": "571039869070475264",
            "algoOrdType": "contract_grid",
            "annualizedRate": "0",
            "arbitrageNum": "0",
            "availEq": "52.3015392887089673",
            "basePos": true,
            "cTime": "1682418514204",
            "cancelType": "0",
            "direction": "long",
            "eq": "108.7945652387089673",
            "floatProfit": "8.7945652387089673",
            "gridNum": "10",
            "gridProfit": "0",
            "instId": "BTC-USDT-SWAP",
            "instType": "SWAP",
            "investment": "100",
            "lever": "5",
            "liqPx": "16370.482143120824",
            "maxPx": "36437.3",
            "minPx": "26931.9",
            "ordFrozen": "5.38638",
            "pTime": "1682492574068",
            "perMaxProfitRate": "0.1687494513302446",
            "perMinProfitRate": "0.1263869357706788",
            "pnlRatio": "0.0879456523870897",
            "rebateTrans": [{
                "rebate": "0",
                "rebateCcy": "USDT"
            }],
            "runPx": "27306.9",
            "runType": "1",
            "singleAmt": "1",
            "slTriggerPx": "",
            "state": "running",
            "stopType": "0",
            "sz": "100",
            "tag": "",
            "totalAnnualizedRate": "38.52019574554529",
            "totalPnl": "8.7945652387089673",
            "tpTriggerPx": "",
            "tradeNum": "9",
            "triggerParams": [{
                "triggerAction": "start",
                "delaySeconds": "0",
                "triggerStrategy": "price",
                "triggerPx": "1",
                "triggerType": "manual",
                "triggerTime": "1682418561497"
            }, {
                "triggerAction": "stop",
                "delaySeconds": "0",
                "triggerStrategy": "instant",
                "stopType": "1",
                "triggerType": "manual",
                "triggerTime": "0"
            }],
            "uTime": "1682492552257",
            "profitSharingRatio": "",
            "copyType": "0",
            "tpRatio": "",
            "slRatio": "",
            "fee": "",
            "fundingFee": ""
        }]
    }
    

#### 推送数据参数

**参数名** | **类型** | **描述**  
---|---|---  
arg | Object | 订阅成功的频道  
> channel | String | 频道名  
> instType | String | 产品类型  
> uid | String | 用户ID  
data | Array of objects | 订阅的数据  
> algoId | String | 策略订单ID  
> algoClOrdId | String | 用户自定义策略ID  
> instType | String | 产品类型  
> instId | String | 产品ID  
> cTime | String | 策略订单创建时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
> uTime | String | 策略订单更新时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
> algoOrdType | String | 策略订单类型  
`contract_grid`：合约网格  
> state | String | 订单状态  
`starting`：启动中  
`running`：运行中  
`stopping`：终止中  
`no_close_position`：已停止未平仓（仅适用于合约网格）  
`stopped`：已停止  
> rebateTrans | Array of objects | 返佣划转信息  
>> rebate | String | 返佣数量  
>> rebateCcy | String | 返佣币种  
> triggerParams | Array of objects | 信号触发参数  
>> triggerAction | String | 触发行为  
`start`：网格启动  
`stop`：网格停止  
>> triggerStrategy | String | 触发策略  
`instant`：立即触发  
`price`：价格触发  
`rsi`：rsi指标触发  
>> delaySeconds | String | 延迟触发时间，单位为秒  
>> triggerTime | String | triggerAction实际触发时间，Unix时间戳的毫秒数格式, 如 `1597026383085`  
>> triggerType | String | triggerAction的实际触发类型  
`manual`：手动触发  
`auto`: 自动触发  
>> timeframe | String | K线种类  
`3m`, `5m`, `15m`, `30m` (`m`代表分钟)  
`1H`, `4H` (`H`代表小时)  
`1D` (`D`代表天)  
该字段只在`triggerStrategy`为`rsi`时有效  
>> thold | String | 阈值  
取值[1,100]的整数  
该字段只在`triggerStrategy`为`rsi`时有效  
>> triggerCond | String | 触发条件  
`cross_up`：上穿  
`cross_down`：下穿  
`above`：上方  
`below`：下方  
`cross`：交叉  
该字段只在`triggerStrategy`为`rsi`时有效  
>> timePeriod | String | 周期  
`14`  
该字段只在`triggerStrategy`为`rsi`下有效  
>> triggerPx | String | 触发价格  
该字段只在`triggerStrategy`为`price`下有效  
>> stopType | String | 策略停止类型  
现货网格 `1`：卖出交易币，`2`：不卖出交易币  
合约网格 `1`：停止平仓，`2`：停止不平仓   
该字段只在`triggerAction`为`stop`时有效  
> maxPx | String | 区间最高价格  
> minPx | String | 区间最低价格  
> gridNum | String | 网格数量  
> runType | String | 网格类型  
`1`：等差，`2`：等比  
> tpTriggerPx | String | 止盈触发价  
> slTriggerPx | String | 止损触发价  
> tradeNum | String | 挂单成交次数  
> arbitrageNum | String | 网格套利次数  
> singleAmt | String | 单网格买卖量  
> perMinProfitRate | String | 预期单网格最低利润率  
> perMaxProfitRate | String | 预期单网格最高利润率  
> runPx | String | 启动时价格  
> totalPnl | String | 总收益  
> pnlRatio | String | 收益率  
> investment | String | 累计投入金额  
现货网格如果投入了交易币则折算为计价币  
> gridProfit | String | 网格利润  
> floatProfit | String | 浮动盈亏  
> totalAnnualizedRate | String | 总年化  
> annualizedRate | String | 网格年化  
> cancelType | String | 网格策略停止原因  
`0`：无  
`1`：手动停止  
`2`：止盈停止  
`3`：止损停止  
`4`：风控停止  
`5`：交割停止  
`6`: 信号停止  
> stopType | String | 网格策略停止类型  
现货网格 `1`：卖出交易币，`2`：不卖出交易币  
合约网格 `1`：市价全平，`2`：停止不平仓  
> direction | String | 合约网格类型  
`long`：做多，`short`：做空，`neutral`：中性  
仅适用于`合约网格`  
> basePos | Boolean | 是否开底仓  
仅适用于`合约网格`  
> sz | String | 投入保证金，单位为`USDT`  
仅适用于`合约网格`  
> lever | String | 杠杆倍数  
仅适用于`合约网格`  
> actualLever | String | 实际杠杆倍数  
仅适用于`合约网格`  
> liqPx | String | 预估强平价格  
仅适用于`合约网格`  
> eq | String | 策略账户总权益  
仅适用于`合约网格`  
> ordFrozen | String | 挂单占用  
适用于`合约网格`  
> availEq | String | 可用保证金  
适用于`合约网格`  
> activeOrdNum | String | 子订单挂单数量  
> tag | String | 订单标签  
> profitSharingRatio | String | 分润比例  
取值范围[0,0.3]  
如果是普通订单（既不是带单也不是跟单），该字段返回""  
> copyType | String | 分润订单类型  
`0`：普通订单  
`1`：普通跟单  
`2`：分润跟单  
`3`：带单  
> tpRatio | String | 止盈比率，0.1 代表 10%  
> slRatio | String | 止损比率，0.1 代表 10%  
> fee | String | 累计手续费金额，仅适用于合约网格，其他网格策略为""  
> fundingFee | String | 累计资金费用，仅适用于合约网格，其他网格策略为""  
> pTime | String | 网格策略的推送时间，Unix时间戳的毫秒数格式，如 `1597026383085`