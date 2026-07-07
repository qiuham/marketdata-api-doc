---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#order-book-trading-dca-trading-get-dca-algo-order-history
anchor_id: order-book-trading-dca-trading-get-dca-algo-order-history
api_type: API
updated_at: 2026-07-07 19:42:04.020789
---

# GET / DCA algo order history

#### Rate Limit: 20 requests per 2 seconds  
  
#### Rate Limit Rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/tradingBot/dca/history-list`

> Request Example
    
    
    GET /api/v5/tradingBot/dca/history-list?algoOrdType=contract_dca
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
algoOrdType | String | Yes | Algo order type  
`contract_dca`: Contract DCA order  
`spot_dca`: Spot DCA order  
algoId | String | No | Algo ID  
after | String | No | Pagination of data to return records earlier than the requested `algoId`  
before | String | No | Pagination of data to return records newer than the requested `algoId`  
limit | String | No | Number of results per request. The maximum is 100. The default is 100  
  
> Response Example
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "algoId": "12345689",
                "algoOrdType": "contract_dca",
                "instId": "BTC-USDT-SWAP",
                "copyType": "0",
                "state": "stopped",
                "cancelType": "1",
                "direction": "long",
                "lever": "3",
                "initOrdAmt": "100",
                "safetyOrdAmt": "200",
                "maxSafetyOrds": "5",
                "pxSteps": "0.02",
                "pxStepsMult": "1",
                "volMult": "1",
                "slPct": "",
                "slMode": "",
                "allowReinvest": true,
                "totalPnl": "12.5",
                "pnlRatio": "0.05",
                "fundingFee": "-0.5",
                "investmentAmt": "500",
                "investmentCcy": "USDT",
                "arbitragePnL": "2.1",
                "transferInMargin": "500",
                "profitSharingRatio": "",
                "trackingMode": "",
                "triggerParams": [
                    {
                        "triggerAction": "start",
                        "triggerStrategy": "instant"
                    }
                ],
                "ctVal": "0.01",
                "cTime": "1597026383085",
                "uTime": "1597026383085"
            }
        ]
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
algoId | String | Algo ID  
algoOrdType | String | Algo order type  
`contract_dca`: Contract DCA order  
`spot_dca`: Spot DCA order  
instId | String | Instrument ID, e.g. `BTC-USDT-SWAP`  
copyType | String | Profit sharing order type  
`0`: Normal order  
`1`: Copy order without profit sharing  
`2`: Copy order with profit sharing  
`3`: Lead order  
state | String | Algo order state  
`starting`  
`running`  
`stopping`  
`pending_signal`  
`no_close_position`: Stopped algo order but have not closed position yet  
cancelType | String | Algo order stop reason  
`0`: None  
`1`: Manual stop  
`2`: Take profit  
`3`: Stop loss  
`4`: Risk control  
`5`: Delivery  
direction | String | Contract DCA: `long`: Long position, `short`: Short position  
Spot DCA: `long`: Long position  
lever | String | Leverage  
Only applicable to `contract_dca`  
initOrdAmt | String | Initial order amount  
safetyOrdAmt | String | Safety order amount  
maxSafetyOrds | String | Max number of safety orders  
pxSteps | String | Safety order price step  
pxStepsMult | String | Price step multiplier  
volMult | String | Safety order amount multiplier  
slPct | String | Stop-loss target, e.g. `0.05` represents 5%  
slMode | String | Stop-loss mode  
`limit`: Limit order  
`market`: Market order  
allowReinvest | Boolean | Whether to reinvest profit  
`true` or `false`  
totalPnl | String | Total PnL  
pnlRatio | String | PnL ratio  
fundingFee | String | Total funding fee  
Only applicable to `contract_dca`  
investmentAmt | String | Total investment amount  
investmentCcy | String | The invested quantity unit, can only be `USDT`/`USDC`  
arbitragePnL | String | Arbitrage PnL  
transferInMargin | String | Net transfer in margin, including margin and manually added investment  
Only applicable to `contract_dca`  
profitSharingRatio | String | Profit sharing ratio, range [0, 0.3]  
Returns `""` for normal orders  
Only applicable to `contract_dca`  
trackingMode | String | Tracking mode  
`sync`: Synchronous  
`async`: Asynchronous  
Only applicable to `contract_dca`  
triggerParams | Array of objects | Trigger parameters  
> triggerAction | String | Trigger action  
`start`: Start bot  
`stop`: Stop bot  
> triggerStrategy | String | Trigger strategy  
Contract DCA: `instant`: Instant trigger, `price`: Price trigger, `rsi`: RSI indicator trigger, `webhook`: WebSocket signal trigger  
Spot DCA: `instant`: Instant trigger, `rsi`: RSI indicator trigger  
> triggerPx | String | Trigger price  
This field is only valid when `triggerStrategy` is `price`  
Only applicable to `contract_dca`  
> triggerCond | String | Trigger condition  
`cross_up`: Cross up  
`cross_down`: Cross down  
`above`: Above  
`below`: Below  
`cross`: Cross  
This field is only valid when `triggerStrategy` is `rsi`  
> timePeriod | String | Time period, e.g. `14`  
This field is only valid when `triggerStrategy` is `rsi`  
> thold | String | Threshold  
Integer between [1, 100]  
This field is only valid when `triggerStrategy` is `rsi`  
> timeframe | String | K-line type  
`3m`, `5m`, `15m`, `30m` (m: minute)  
`1H`, `4H` (H: hour)  
`1D` (D: day)  
This field is only valid when `triggerStrategy` is `rsi`  
ctVal | String | Contract value  
Only applicable to `contract_dca`  
cTime | String | Algo order created time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
uTime | String | Algo order updated time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
tradeQuoteCcy | String | Quote currency for trading  
Only applicable to `spot_dca`

---

# GET / 获取历史马丁策略委托单列表

#### 限速：20次/2s  
  
#### 限速规则：User ID

#### 权限：读取

#### HTTP请求

`GET /api/v5/tradingBot/dca/history-list`

> 请求示例
    
    
    GET /api/v5/tradingBot/dca/history-list?algoOrdType=contract_dca
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
algoOrdType | String | 是 | 策略订单类型  
`contract_dca`：合约马丁委托  
`spot_dca`：现货马丁委托  
algoId | String | 否 | 策略订单 ID  
after | String | 否 | 请求此ID之前（更旧的数据）的分页内容，传的值为对应接口的 `algoId`  
before | String | 否 | 请求此ID之后（更新的数据）的分页内容，传的值为对应接口的 `algoId`  
limit | String | 否 | 返回结果的数量，最大为100，默认100条  
  
> 返回结果
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "algoId": "12345689",
                "algoOrdType": "contract_dca",
                "instId": "BTC-USDT-SWAP",
                "copyType": "0",
                "state": "stopped",
                "cancelType": "1",
                "direction": "long",
                "lever": "3",
                "initOrdAmt": "100",
                "safetyOrdAmt": "200",
                "maxSafetyOrds": "5",
                "pxSteps": "0.02",
                "pxStepsMult": "1",
                "volMult": "1",
                "slPct": "",
                "slMode": "",
                "allowReinvest": true,
                "totalPnl": "12.5",
                "pnlRatio": "0.05",
                "fundingFee": "-0.5",
                "investmentAmt": "500",
                "investmentCcy": "USDT",
                "arbitragePnL": "2.1",
                "transferInMargin": "500",
                "profitSharingRatio": "",
                "trackingMode": "",
                "triggerParams": [
                    {
                        "triggerAction": "start",
                        "triggerStrategy": "instant"
                    }
                ],
                "ctVal": "0.01",
                "cTime": "1597026383085",
                "uTime": "1597026383085"
            }
        ]
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
algoId | String | 策略订单 ID  
algoOrdType | String | 策略订单类型  
`contract_dca`：合约马丁委托  
`spot_dca`：现货马丁委托  
instId | String | 产品 ID，如 `BTC-USDT-SWAP`  
copyType | String | 分润订单类型  
`0`：普通订单  
`1`：普通跟单  
`2`：分润跟单  
`3`：带单  
state | String | 订单状态  
`starting`：启动中  
`running`：运行中  
`stopping`：终止中  
`pending_signal`：等待触发  
`no_close_position`：已停止未平仓  
cancelType | String | 马丁策略停止原因  
`0`：无  
`1`：手动停止  
`2`：止盈停止  
`3`：止损停止  
`4`：风控停止  
`5`：交割停止  
direction | String | 合约马丁类型：`long`：多仓，`short`：空仓  
现货马丁类型：`long`：做多  
lever | String | 杠杆倍数  
仅适用于 `contract_dca`  
initOrdAmt | String | 初始订单金额  
safetyOrdAmt | String | 加仓单金额  
maxSafetyOrds | String | 最大自动加仓次数  
pxSteps | String | 跌多少加仓  
pxStepsMult | String | 加仓价差倍数  
volMult | String | 加仓金额倍数  
slPct | String | 止损目标，如 `0.05` 表示 5%  
slMode | String | 止损模式  
`limit`：限价  
`market`：市价  
allowReinvest | Boolean | 是否复投利润  
`true` 或 `false`  
totalPnl | String | 总收益  
pnlRatio | String | 收益率  
fundingFee | String | 累计资金费用  
仅适用于 `contract_dca`  
investmentAmt | String | 累计投入金额  
investmentCcy | String | 投入数量单位，仅支持 `USDT`/`USDC`  
arbitragePnL | String | 周期套利收益  
transferInMargin | String | 净转入金额，包括保证金和手动加仓金额  
仅适用于 `contract_dca`  
profitSharingRatio | String | 分润比例，取值范围 [0, 0.3]  
普通订单返回 `""`  
仅适用于 `contract_dca`  
trackingMode | String | 分润设置  
`sync`：同步  
`async`：异步  
仅适用于 `contract_dca`  
triggerParams | Array of objects | 信号触发参数  
> triggerAction | String | 触发行为  
`start`：马丁启动  
`stop`：马丁停止  
> triggerStrategy | String | 触发策略  
合约马丁类型：`instant`：立即触发，`price`：价格触发，`rsi`：RSI 指标触发，`webhook`：WS 信号触发  
现货马丁类型：`instant`：立即触发，`rsi`：RSI 指标触发  
> triggerPx | String | 触发价格  
仅在 `triggerStrategy` 为 `price` 时有效  
仅适用于 `contract_dca`  
> triggerCond | String | 触发条件  
`cross_up`：上穿  
`cross_down`：下穿  
`above`：上方  
`below`：下方  
`cross`：交叉  
仅在 `triggerStrategy` 为 `rsi` 时有效  
> timePeriod | String | 周期，如 `14`  
仅在 `triggerStrategy` 为 `rsi` 时有效  
> thold | String | 阈值，取值 [1, 100] 的整数  
仅在 `triggerStrategy` 为 `rsi` 时有效  
> timeframe | String | K 线种类  
`3m`、`5m`、`15m`、`30m`（m 代表分钟）  
`1H`、`4H`（H 代表小时）  
`1D`（D 代表天）  
仅在 `triggerStrategy` 为 `rsi` 时有效  
ctVal | String | 合约面值  
仅适用于 `contract_dca`  
cTime | String | 订单创建时间，Unix 时间戳毫秒数，如 `1597026383085`  
uTime | String | 订单更新时间，Unix 时间戳毫秒数，如 `1597026383085`  
tradeQuoteCcy | String | 指定交易计价货币  
仅适用于 `spot_dca`