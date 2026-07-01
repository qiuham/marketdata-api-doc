---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#order-book-trading-dca-trading-post-place-dca-algo-order
anchor_id: order-book-trading-dca-trading-post-place-dca-algo-order
api_type: API
updated_at: 2026-07-01 19:54:07.234774
---

# POST / Place dca algo order

#### Rate Limit: 20 requests per 2 seconds  
  
#### Rate limit rule: User ID + Instrument ID

#### Permission: Trade

#### HTTP Request

`POST /api/v5/tradingBot/dca/create`

> Request Example
    
    
    POST /api/v5/tradingBot/dca/create
    body
    {
        "instId": "BTC-USDT",
        "algoOrdType": "contract_dca",
        "direction": "long",
        "lever": "2",
        "initOrdAmt": "50",
        "maxSafetyOrds": "0",
        "safetyOrdAmt": "10",
        "pxSteps": "0.01",
        "tpPct": "0.05",
        "triggerParams": [
            {
                "triggerAction": "start",
                "triggerStrategy": "rsi",
                "timeframe": "30m",
                "thold": "10",
                "triggerCond": "cross",
                "timePeriod": "14"
            }
        ]
    }
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
instId | String | Yes | Instrument ID, e.g. `BTC-USDT`  
algoOrdType | String | Yes | Algo order type  
`contract_dca`: Contract DCA order  
`spot_dca`: Spot DCA order  
initOrdAmt | String | Yes | Initial order amount  
allowReinvest | String | No | Whether to reinvest profit. Only applicable to Contract DCA  
`true` or `false`, default is `true`  
safetyOrdAmt | String | No | Safety order amount  
When `maxSafetyOrds` >= 1, `safetyOrdAmt` is required  
maxSafetyOrds | String | Yes | Max number of safety orders  
pxSteps | String | No | Safety order price step  
When `maxSafetyOrds` >= 1, `pxSteps` is required  
pxStepsMult | String | No | Price step multiplier  
When `maxSafetyOrds` >= 1, `pxStepsMult` is required  
volMult | String | No | Safety order amount multiplier  
When `maxSafetyOrds` >= 1, `volMult` is required  
tpPct | String | Yes | Take-profit target per cycle  
0.05 represents 5%  
slPct | String | No | Stop-loss target  
0.05 represents 5%  
slMode | String | No | Stop-loss mode  
`limit`: Limit order  
`market`: Market order  
direction | String | No | Contract DCA type. Only applicable to `contract_dca`  
`long`: Long position, `short`: Short position  
lever | String | Yes | Leverage  
Only applicable to `contract_dca`  
triggerParams | Array of objects | Yes | Trigger parameters  
> triggerAction | String | Yes | Trigger action  
Contract DCA: `start`: Start bot  
Spot DCA: `start`: Start bot  
> triggerStrategy | String | Yes | Trigger strategy  
Contract DCA: `instant`: Instant trigger, `price`: Price trigger, `rsi`: RSI indicator trigger, default is `instant`  
Spot DCA: `instant`: Instant trigger, `rsi`: RSI indicator trigger, default is `instant`  
> timeframe | String | No | K-line type  
`3m`, `5m`, `15m`, `30m` (m: minute)  
`1H`, `4H` (H: hour)  
`1D` (D: day)  
This field is only valid when `triggerStrategy` is `rsi`  
> thold | String | No | Threshold  
Integer between [1, 100]  
This field is only valid when `triggerStrategy` is `rsi`  
> triggerCond | String | No | Trigger condition  
`cross_up`: Cross up  
`cross_down`: Cross down  
`above`: Above  
`below`: Below  
`cross`: Cross  
This field is only valid when `triggerStrategy` is `rsi`  
> timePeriod | String | No | Time period  
`14`  
This field is only valid when `triggerStrategy` is `rsi`  
> triggerPx | String | No | Trigger price  
This field is only valid when `triggerStrategy` is `price`  
Only applicable to `contract_dca`  
profitSharingRatio | String | No | Lead trader profit sharing ratio. Only fixed profit sharing is supported. Only applicable to `contract_dca`  
`0`, `0.1`, `0.2`, `0.3`  
trackingMode | String | No | Tracking mode. Only applicable to `contract_dca`  
`sync`: Synchronous, `async`: Asynchronous  
tag | String | No | Order tag  
algoClOrdId | String | No | Client-supplied Algo ID  
tradeQuoteCcy | String | No | Quote currency for trading. Only applicable to `spot_dca`  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "algoId": "447053782921515008",
                "sCode": "0",
                "sMsg": ""
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
algoId | String | Algo ID  
tag | String | Order tag  
algoClOrdId | String | Client-supplied Algo ID  
sCode | String | The code of the event execution result, 0 means success  
sMsg | String | Rejection message if the request is unsuccessful

---

# POST / 马丁策略委托下单

#### 限速：20次/2s  
  
#### 限速规则（期权以外）：User ID + Instrument ID

#### 限速规则（只限期权）：User ID + Instrument Family

#### 权限：交易

#### HTTP请求

`POST /api/v5/tradingBot/dca/create`

> 请求示例
    
    
    # 马丁下单
    POST /api/v5/tradingBot/dca/create
    body
    {
        "instId": "BTC-USDT",
        "algoOrdType": "contract_dca",
        "direction": "long",
        "lever": "2",
        "initOrdAmt"="50",
        "maxSafetyOrds"="0",
        "safetyOrdAmt"="10",
        "pxSteps"="0.01",
        "tpPct"="0.05",
        "triggerParams":[
          {
             "triggerAction":"start",
             "triggerStrategy":"rsi",
             "timeframe":"30m",
             "thold":"10",
             "triggerCond":"cross",
             "timePeriod":"14"
          }
    }
    
    
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
instId | String | 是 | 产品ID，如 `BTC-USDT`  
algoOrdType | String | 是 | 策略订单类型  
`contract_dca`：合约马丁委托  
`spot_dca`：现货马丁委托  
initOrdAmt | String | 是 | 初始订单金额  
allowReinvest | String | 否 | 是否复投利润，仅适用于合约马丁  
`true` 或者 `false`，默认为 `true`  
safetyOrdAmt | String | 否 | 加仓单金额  
当 `maxSafetyOrds` >= 1 时，`safetyOrdAmt` 必传  
maxSafetyOrds | String | 是 | 最大自动加仓次数  
pxSteps | String | 否 | 跌多少加仓  
当 `maxSafetyOrds` >= 1 时，`pxSteps` 必传  
pxStepsMult | String | 否 | 加仓价差倍数  
当 `maxSafetyOrds` >= 1 时，`pxStepsMult` 必传  
volMult | String | 否 | 加仓金额倍数  
当 `maxSafetyOrds` >= 1 时，`volMult` 必传  
tpPct | String | 是 | 单周期止盈目标  
0.05 表示 5%  
slPct | String | 否 | 止损目标  
0.05 表示 5%  
slMode | String | 否 | 止损模式  
`limit`：限价  
`market`：市价  
direction | String | 否 | 合约马丁类型，仅适用于 `contract_dca`  
`long`：多仓，`short`：空仓  
lever | String | 是 | 杠杆倍数  
仅适用于 `contract_dca`  
triggerParams | Array of objects | 是 | 信号触发参数  
> triggerAction | String | 是 | 触发行为  
合约马丁触发行为：`start`：马丁启动  
现货马丁触发行为：`start`：马丁启动  
> triggerStrategy | String | 是 | 触发策略  
合约马丁类型：`instant`：立即触发，`price`：价格触发，`rsi`：RSI 指标触发，默认为 `instant`  
现货马丁类型：`instant`：立即触发，`rsi`：RSI 指标触发，默认为 `instant`  
> timeframe | String | 否 | K线种类  
`3m`, `5m`, `15m`, `30m`（`m` 代表分钟）  
`1H`, `4H`（`H` 代表小时）  
`1D`（`D` 代表天）  
该字段只在 `triggerStrategy` 为 `rsi` 时有效  
> thold | String | 否 | 阈值  
取值 [1,100] 的整数  
该字段只在 `triggerStrategy` 为 `rsi` 时有效  
> triggerCond | String | 否 | 触发条件  
`cross_up`：上穿  
`cross_down`：下穿  
`above`：上方  
`below`：下方  
`cross`：交叉  
该字段只在 `triggerStrategy` 为 `rsi` 时有效  
> timePeriod | String | 否 | 周期  
`14`  
该字段只在 `triggerStrategy` 为 `rsi` 时有效  
> triggerPx | String | 否 | 触发价格  
该字段只在 `triggerStrategy` 为 `price` 时有效  
仅适用于 `contract_dca`  
profitSharingRatio | String | 否 | 带单员分润比例，仅支持固定比例分润，仅适用于 `contract_dca`  
`0`, `0.1`, `0.2`, `0.3`  
trackingMode | String | 否 | 分润设置，仅适用于 `contract_dca`  
`sync` 同步，`async` 异步  
tag | String | 否 | 订单标签  
algoClOrdId | String | 否 | 客户端自定义策略单ID  
tradeQuoteCcy | String | 否 | 指定交易计价货币，仅适用`spot_dca`  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "algoId": "447053782921515008",
                "sCode": "0",
                "sMsg": ""
            }
        ],
        "msg": ""
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
algoId | String | 策略订单ID  
tag | String | 订单标签  
algoClOrdId | String | 客户端自定义策略单ID  
sCode | String | 事件执行结果的code，0代表成功  
sMsg | String | 事件执行失败时的msg