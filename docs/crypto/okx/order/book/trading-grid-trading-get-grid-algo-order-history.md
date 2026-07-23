---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#order-book-trading-grid-trading-get-grid-algo-order-history
anchor_id: order-book-trading-grid-trading-get-grid-algo-order-history
api_type: API
updated_at: 2026-07-23 19:21:26.683827
---

# GET / Grid algo order history

#### Rate Limit: 20 requests per 2 seconds  
  
#### Rate limit rule: User ID

#### HTTP Request

`GET /api/v5/tradingBot/grid/orders-algo-history`

> Request Example
    
    
    GET /api/v5/tradingBot/grid/orders-algo-history?algoOrdType=grid
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
algoOrdType | String | Yes | Algo order type  
`grid`: Spot grid  
`contract_grid`: Contract grid  
algoId | String | No | Algo ID  
instId | String | No | Instrument ID, e.g. `BTC-USDT`  
instType | String | No | Instrument type  
`SPOT`  
`MARGIN`  
`FUTURES`  
`SWAP`  
after | String | No | Pagination of data to return records earlier than the requested `algoId`.  
before | String | No | Pagination of data to return records newer than the requested `algoId`.  
limit | String | No | Number of results per request. The maximum is 100. The default is 100.  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "actualLever": "",
                "algoClOrdId": "",
                "algoId": "565849588675117056",
                "algoOrdType": "grid",
                "arbitrageNum": "0",
                "availEq": "",
                "basePos": false,
                "baseSz": "0",
                "cTime": "1681181054927",
                "cancelType": "1",
                "direction": "",
                "floatProfit": "0",
                "gridNum": "10",
                "gridProfit": "0",
                "instFamily": "",
                "instId": "BTC-USDT",
                "instType": "SPOT",
                "investment": "25",
                "lever": "0",
                "liqPx": "",
                "maxPx": "5000",
                "minPx": "400",
                "ordFrozen": "",
                "pnlRatio": "0",
                "quoteSz": "25",
                "rebateTrans": [
                    {
                        "rebate": "0",
                        "rebateCcy": "BTC"
                    },
                    {
                        "rebate": "0",
                        "rebateCcy": "USDT"
                    }
                ],
                "runType": "1",
                "slTriggerPx": "0",
                "state": "stopped",
                "stopResult": "0",
                "stopType": "1",
                "sz": "",
                "tag": "",
                "totalPnl": "0",
                "tpTriggerPx": "0",
                "triggerParams": [
                    {
                        "triggerAction": "start",
                        "delaySeconds": "0",
                        "triggerStrategy": "instant",
                        "triggerType": "auto",
                        "triggerTime": ""
                    },
                    {
                        "triggerAction": "stop",
                        "delaySeconds": "0",
                        "triggerStrategy": "instant",
                        "stopType": "1",
                        "triggerPx": "1000",
                        "triggerType": "manual",
                        "triggerTime": "1681181186484"
                    }
                ],
                "uTime": "1681181186496",
                "uly": "BTC-USDT", 
                "profitSharingRatio": "",
                "copyType": "0",
                "fee": "",
                "feeCcy": "",
                "fundingFee": "",
                "tradeQuoteCcy": "USDT"
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
algoId | String | Algo ID  
algoClOrdId | String | Client-supplied Algo ID  
instType | String | Instrument type  
instId | String | Instrument ID  
cTime | String | Algo order created time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
uTime | String | Algo order updated time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
algoOrdType | String | Algo order type  
`grid`: Spot grid  
`contract_grid`: Contract grid  
state | String | Algo order state  
`stopped`  
rebateTrans | Array of objects | Rebate transfer info  
> rebate | String | Rebate amount  
> rebateCcy | String | Rebate currency  
triggerParams | Array of objects | Trigger Parameters  
> triggerAction | String | Trigger action  
`start`  
`stop`  
> triggerStrategy | String | Trigger strategy  
`instant`  
`price`  
`rsi`  
> delaySeconds | String | Delay seconds after action triggered  
> triggerTime | String | Actual action triggered time, unix timestamp format in milliseconds, e.g. `1597026383085`  
> triggerType | String | Actual action triggered type  
`manual`  
`auto`  
> timeframe | String | K-line type  
`3m`, `5m`, `15m`, `30m` (`m`: minute)  
`1H`, `4H` (`H`: hour)  
`1D` (`D`: day)  
This field is only valid when `triggerStrategy` is `rsi`  
> thold | String | Threshold  
The value should be an integer between 1 to 100  
This field is only valid when `triggerStrategy` is `rsi`  
> triggerCond | String | Trigger condition  
`cross_up`  
`cross_down`  
`above`  
`below`  
`cross`  
This field is only valid when `triggerStrategy` is `rsi`  
> timePeriod | String | Time Period  
`14`  
This field is only valid when `triggerStrategy` is `rsi`  
> triggerPx | String | Trigger Price  
This field is only valid when `triggerStrategy` is `price`  
> stopType | String | Stop type  
Spot grid `1`: Sell base currency `2`: Keep base currency  
Contract grid `1`: Market Close All positions `2`: Keep positions  
This field is only valid when `triggerAction` is `stop`  
maxPx | String | Upper price of price range  
minPx | String | Lower price of price range  
gridNum | String | Grid quantity  
runType | String | Grid type  
`1`: Arithmetic, `2`: Geometric  
tpTriggerPx | String | Take-profit trigger price  
slTriggerPx | String | Stop-loss trigger price  
arbitrageNum | String | The number of arbitrages executed  
totalPnl | String | Total P&L  
pnlRatio | String | P&L ratio  
investment | String | Accumulated investment amount  
Spot grid investment amount calculated on quote currency  
gridProfit | String | Grid profit  
floatProfit | String | Variable P&L  
cancelType | String | Algo order stop reason  
`0`: None  
`1`: Manual stop  
`2`: Take profit  
`3`: Stop loss  
`4`: Risk control  
`5`: Delivery  
`6`: Signal  
stopType | String | Actual Stop type  
Spot grid `1`: Sell base currency `2`: Keep base currency  
Contract grid `1`: Market Close All positions `2`: Keep positions  
quoteSz | String | Quote currency investment amount  
Only applicable to `Spot grid`  
baseSz | String | Base currency investment amount  
Only applicable to `Spot grid`  
direction | String | Contract grid type  
`long`,`short`,`neutral`  
Only applicable to `contract grid`  
basePos | Boolean | Whether or not to open a position when the strategy is activated  
Only applicable to `contract grid`  
sz | String | Used margin based on `USDT`  
Only applicable to `contract grid`  
lever | String | Leverage  
Only applicable to `contract grid`  
actualLever | String | Actual Leverage  
Only applicable to `contract grid`  
liqPx | String | Estimated liquidation price  
Only applicable to `contract grid`  
uly | String | Underlying  
Only applicable to `contract grid`  
instFamily | String | Instrument family  
Only applicable to `FUTURES`/`SWAP`/`OPTION`  
Only applicable to `contract grid`  
ordFrozen | String | Margin used by pending orders  
Only applicable to `contract grid`  
availEq | String | Available margin  
Only applicable to `contract grid`  
tag | String | Order tag  
profitSharingRatio | String | Profit sharing ratio  
Value range [0, 0.3]  
If it is a normal order (neither copy order nor lead order), this field returns ""  
copyType | String | Profit sharing order type  
`0`: Normal order  
`1`: Copy order without profit sharing  
`2`: Copy order with profit sharing  
`3`: Lead order  
fee | String | Accumulated fee. Only applicable to contract grid, or it will be ""  
feeCcy | String | Accumulated fee currency. Only applicable to contract grid, or it will be ""  
fundingFee | String | Accumulated funding fee. Only applicable to contract grid, or it will be ""  
stopResult | String | Stop result  
`0`: default, `1`: Successful selling of currency at market price, `-1`: Failed to sell currency at market price  
Only applicable to `Spot grid`  
tradeQuoteCcy | String | The quote currency for trading.

---

# GET / 获取历史网格策略委托单列表

#### 限速：20次/2s  
  
#### 限速规则：User ID

#### HTTP请求

`GET /api/v5/tradingBot/grid/orders-algo-history`

> 请求示例
    
    
    GET /api/v5/tradingBot/grid/orders-algo-history?algoOrdType=grid
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
algoOrdType | String | 是 | 策略订单类型  
`grid`：现货网格委托  
`contract_grid`：合约网格委托  
algoId | String | 否 | 策略订单ID  
instId | String | 否 | 产品ID，如`BTC-USDT`  
instType | String | 否 | 产品类型  
`SPOT`：币币  
`MARGIN`：杠杆  
`FUTURES`：交割合约  
`SWAP`：永续合约  
after | String | 否 | 请求此ID之前（更旧的数据）的分页内容，传的值为对应接口的`algoId`  
before | String | 否 | 请求此ID之后（更新的数据）的分页内容，传的值为对应接口的`algoId`  
limit | String | 否 | 返回结果的数量，最大为100，默认100条  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "actualLever": "",
                "algoClOrdId": "",
                "algoId": "565849588675117056",
                "algoOrdType": "grid",
                "arbitrageNum": "0",
                "availEq": "",
                "basePos": false,
                "baseSz": "0",
                "cTime": "1681181054927",
                "cancelType": "1",
                "direction": "",
                "floatProfit": "0",
                "gridNum": "10",
                "gridProfit": "0",
                "instFamily": "",
                "instId": "BTC-USDT",
                "instType": "SPOT",
                "investment": "25",
                "lever": "0",
                "liqPx": "",
                "maxPx": "5000",
                "minPx": "400",
                "ordFrozen": "",
                "pnlRatio": "0",
                "quoteSz": "25",
                "rebateTrans": [
                    {
                        "rebate": "0",
                        "rebateCcy": "BTC"
                    },
                    {
                        "rebate": "0",
                        "rebateCcy": "USDT"
                    }
                ],
                "runType": "1",
                "slTriggerPx": "0",
                "state": "stopped",
                "stopResult": "0",
                "stopType": "1",
                "sz": "",
                "tag": "",
                "totalPnl": "0",
                "tpTriggerPx": "0",
                "triggerParams": [
                    {
                        "triggerAction": "start",
                        "delaySeconds": "0",
                        "triggerStrategy": "instant",
                        "triggerType": "auto",
                        "triggerTime": ""
                    },
                    {
                        "triggerAction": "stop",
                        "delaySeconds": "0",
                        "triggerStrategy": "instant",
                        "stopType": "1",
                        "triggerPx": "1000",
                        "triggerType": "manual",
                        "triggerTime": "1681181186484"
                    }
                ],
                "uTime": "1681181186496",
                "uly": "BTC-USDT",
                "profitSharingRatio": "",
                "copyType": "0",
                "fee": "",
                "feeCcy": "",
                "fundingFee": "",
                "tradeQuoteCcy": "USDT"
            }
        ],
        "msg": ""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
algoId | String | 策略订单ID  
algoClOrdId | String | 用户自定义策略ID  
instType | String | 产品类型  
instId | String | 产品ID  
cTime | String | 策略订单创建时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
uTime | String | 策略订单更新时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
algoOrdType | String | 策略订单类型  
`grid`：现货网格委托  
`contract_grid`：合约网格委托  
state | String | 订单状态  
`stopped`：已停止  
rebateTrans | Array of objects | 返佣划转信息  
> rebate | String | 返佣数量  
> rebateCcy | String | 返佣币种  
triggerParams | Array of objects | 信号触发参数  
> triggerAction | String | 触发行为  
`start`：网格启动  
`stop`：网格停止  
> triggerStrategy | String | 触发策略  
`instant`：立即触发  
`price`：价格触发  
`rsi`：rsi指标触发  
> delaySeconds | String | 延迟触发时间，单位为秒  
> triggerTime | String | triggerAction实际触发时间，Unix时间戳的毫秒数格式, 如 `1597026383085`  
> triggerType | String | triggerAction的实际触发类型  
`manual`：手动触发  
`auto`: 自动触发  
> timeframe | String | K线种类  
`3m`, `5m`, `15m`, `30m` (`m`代表分钟)  
`1H`, `4H` (`H`代表小时)  
`1D` (`D`代表天)  
该字段只在`triggerStrategy`为`rsi`时有效  
> thold | String | 阈值  
取值[1,100]的整数  
该字段只在`triggerStrategy`为`rsi`时有效  
> triggerCond | String | 触发条件  
`cross_up`：上穿  
`cross_down`：下穿  
`above`：上方  
`below`：下方  
`cross`：交叉  
该字段只在`triggerStrategy`为`rsi`时有效  
> timePeriod | String | 周期  
`14`  
该字段只在`triggerStrategy`为`rsi`下有效  
> triggerPx | String | 触发价格  
该字段只在`triggerStrategy`为`price`下有效  
> stopType | String | 策略停止类型  
现货 `1`：卖出交易币，`2`：不卖出交易币  
合约网格 `1`：停止平仓，`2`：停止不平仓   
该字段只在`triggerAction`为`stop`时有效  
maxPx | String | 区间最高价格  
minPx | String | 区间最低价格  
gridNum | String | 网格数量  
runType | String | 网格类型  
`1`：等差，`2`：等比  
tpTriggerPx | String | 止盈触发价  
slTriggerPx | String | 止损触发价  
arbitrageNum | String | 网格套利次数  
totalPnl | String | 总收益  
pnlRatio | String | 收益率  
investment | String | 累计投入金额  
现货网格如果投入了交易币则折算为计价币  
gridProfit | String | 网格利润  
floatProfit | String | 浮动盈亏  
cancelType | String | 网格策略停止原因  
`0`：无  
`1`：手动停止  
`2`：止盈停止  
`3`：止损停止  
`4`：风控停止  
`5`：交割停止  
`6`: 信号停止  
stopType | String | 网格策略实际停止类型  
现货网格 `1`：卖出交易币，`2`：不卖出交易币  
合约网格 `1`：停止平仓，`2`：停止不平仓  
quoteSz | String | 计价币投入数量  
适用于`现货网格`  
baseSz | String | 交易币投入数量  
适用于`现货网格`  
direction | String | 合约网格类型  
`long`：做多，`short`：做空，`neutral`：中性  
仅适用于`合约网格`  
basePos | Boolean | 是否开底仓  
适用于`合约网格`  
sz | String | 投入保证金，单位为`USDT`  
适用于`合约网格`  
lever | String | 杠杆倍数  
适用于`合约网格`  
actualLever | String | 实际杠杆倍数  
适用于`合约网格`  
liqPx | String | 预估强平价格  
适用于`合约网格`  
uly | String | 标的指数  
适用于`合约网格`  
instFamily | String | 交易品种  
适用于`交割`/`永续`/`期权`，如 `BTC-USD`  
适用于`合约网格`  
ordFrozen | String | 挂单占用  
适用于`合约网格`  
availEq | String | 可用保证金  
适用于`合约网格`  
tag | String | 订单标签  
profitSharingRatio | String | 分润比例  
取值范围[0,0.3]  
如果是普通订单（既不是带单也不是跟单），该字段返回""  
copyType | String | 分润订单类型  
`0`：普通订单  
`1`：普通跟单  
`2`：分润跟单  
`3`：带单  
fee | String | 累计手续费金额，仅适用于合约网格，其他网格策略为""  
feeCcy | String | 累计手续费货币。仅适用于合约网格，其他网格策略为""  
fundingFee | String | 累计资金费用，仅适用于合约网格，其他网格策略为""  
stopResult | String | 策略停止结果  
`0`：默认，`1`：市价卖币成功 `-1`：市价卖币失败  
仅适用于`现货网格`  
tradeQuoteCcy | String | 用于交易的计价币种。