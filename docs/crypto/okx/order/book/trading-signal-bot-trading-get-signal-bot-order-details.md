---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#order-book-trading-signal-bot-trading-get-signal-bot-order-details
anchor_id: order-book-trading-signal-bot-trading-get-signal-bot-order-details
api_type: API
updated_at: 2026-07-16 19:20:10.485897
---

# GET / Signal bot order details

#### Rate Limit: 20 requests per 2 seconds  
  
#### Rate limit rule: User ID

#### HTTP Request

`GET /api/v5/tradingBot/signal/orders-algo-details`

> Request Example
    
    
    GET /api/v5/tradingBot/signal/orders-algo-details?algoId=623833708424069120&algoOrdType=contract
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
algoOrdType | String | Yes | Algo order type  
`contract`: Contract signal  
algoId | String | Yes | Algo ID  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "algoId": "623833708424069120",
                "algoClOrdId": "",
                "algoOrdType": "contract",
                "availBal": "1.6561369013122267",
                "cTime": "1695005546360",
                "cancelType": "0",
                "entrySettingParam": {
                    "allowMultipleEntry": true,
                    "amt": "0",
                    "entryType": "1",
                    "ratio": ""
                },
                "exitSettingParam": {
                    "slPct": "",
                    "tpPct": "",
                    "tpSlType": "price"
                },
                "floatPnl": "0.1279999999999927",
                "frozenBal": "25.16816",
                "instIds": [
                    "BTC-USDT-SWAP",
                    "ETH-USDT-SWAP"
                ],
                "instType": "SWAP",
                "investAmt": "100",
                "lever": "10",
                "ratio": "",
                "realizedPnl": "-73.303703098687766",
                "signalChanId": "623827579484770304",
                "signalChanName": "testing",
                "signalSourceType": "1",
                "state": "running",
                "subOrdType": "9",
                "totalEq": "26.824296901312227",
                "totalPnl": "-73.1757030986877733",
                "totalPnlRatio": "-0.7317570309868777",
                "uTime": "1697029422313"
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
instIds | Array of strings | Instrument IDs  
cTime | String | Algo order created time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
uTime | String | Algo order updated time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
algoOrdType | String | Algo order type  
`contract`: Contract signal  
state | String | Algo order state  
`starting`  
`running`  
`stopping`  
`stopped`  
cancelType | String | Algo order stop reason  
`0`: None  
`1`: Manual stop  
totalPnl | String | Total P&L  
totalPnlRatio | String | Total P&L ratio  
totalEq | String | Total equity of strategy account  
floatPnl | String | Float P&L  
realizedPnl | String | Realized P&L  
frozenBal | String | Frozen balance  
availBal | String | Avail balance  
lever | String | Leverage  
Only applicable to `contract signal`  
investAmt | String | Investment amount  
subOrdType | String | Sub order type  
`1`：limit order  
`2`：market order  
`9`：tradingView signal  
ratio | String | Price offset ratio, calculate the limit price as a percentage offset from the best bid/ask price  
Only applicable to `subOrdType` is `limit order`  
entrySettingParam | Object | Entry setting  
> allowMultipleEntry | Boolean | Whether or not allow multiple entries in the same direction for the same trading pairs  
> entryType | String | Entry type  
`1`: TradingView signal  
`2`: Fixed margin  
`3`: Contracts  
`4`: Percentage of free margin  
`5`: Percentage of the initial invested margin  
> amt | String | Amount per order  
Only applicable to `entryType` in `2`/`3`  
> ratio | String | Amount ratio per order  
Only applicable to `entryType` in `4`/`5`  
exitSettingParam | Object | Exit setting  
> tpSlType | String | Type of set the take-profit and stop-loss trigger price  
`pnl`: Based on the estimated profit and loss percentage from the entry point  
`price`: Based on price increase or decrease from the crypto’s entry price  
> tpPct | String | Take-profit percentage  
> slPct | String | Stop-loss percentage  
signalChanId | String | Signal channel Id  
signalChanName | String | Signal channel name  
signalSourceType | String | Signal source type  
`1`: Created by yourself  
`2`: Subscribe  
`3`: Free signal

---

# GET / 获取信号策略详情

#### 限速：20次/2s  
  
#### 限速规则：User ID

#### HTTP请求

`GET /api/v5/tradingBot/signal/orders-algo-details`

> 请求示例
    
    
    GET /api/v5/tradingBot/signal/orders-algo-details?algoId=623833708424069120&algoOrdType=contract
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
algoOrdType | String | 是 | 策略类型  
`contract`：合约信号  
algoId | String | 是 | 策略ID  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "algoId": "623833708424069120",
                "algoClOrdId": "",
                "algoOrdType": "contract",
                "availBal": "1.6561369013122267",
                "cTime": "1695005546360",
                "cancelType": "0",
                "entrySettingParam": {
                    "allowMultipleEntry": true,
                    "amt": "0",
                    "entryType": "1",
                    "ratio": ""
                },
                "exitSettingParam": {
                    "slPct": "",
                    "tpPct": "",
                    "tpSlType": "price"
                },
                "floatPnl": "0.1279999999999927",
                "frozenBal": "25.16816",
                "instIds": [
                    "BTC-USDT-SWAP",
                    "ETH-USDT-SWAP"
                ],
                "instType": "SWAP",
                "investAmt": "100",
                "lever": "10",
                "ratio": "",
                "realizedPnl": "-73.303703098687766",
                "signalChanId": "623827579484770304",
                "signalChanName": "我的信号",
                "signalSourceType": "1",
                "state": "running",
                "subOrdType": "9",
                "totalEq": "26.824296901312227",
                "totalPnl": "-73.1757030986877733",
                "totalPnlRatio": "-0.7317570309868777",
                "uTime": "1697029422313"
            }
        ],
        "msg": ""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
algoId | String | 策略ID  
algoClOrdId | String | 用户自定义策略ID  
instType | String | 产品类型  
instIds | Array of strings | 该信号支持的产品ID列表  
cTime | String | 策略创建时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
uTime | String | 策略更新时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
algoOrdType | String | 策略类型  
`contract`：合约信号  
state | String | 订单状态  
`starting`：启动中  
`running`：运行中  
`stopping`：终止中  
`stopped`：已停止  
cancelType | String | 策略停止原因  
`0`：无  
`1`：手动停止  
totalPnl | String | 总收益  
totalPnlRatio | String | 总收益率  
totalEq | String | 当前策略总权益  
floatPnl | String | 浮动盈亏  
realizedPnl | String | 已实现盈亏  
frozenBal | String | 占用保证金  
availBal | String | 可用保证金  
lever | String | 杠杆倍数  
仅适用于`合约信号`  
investAmt | String | 投入金额  
subOrdType | String | 委托类型  
`1`：限价  
`2`：市价  
`9`：tradingView信号  
ratio | String | 限价单的委托价格距离买一/卖一价的百分比  
当委托类型为限价时，该字段有效，无效则返回""。  
entrySettingParam | Object | 进场参数设定  
> allowMultipleEntry | Boolean | 是否允许多次进场  
`true`：允许  
`false`：不允许  
> entryType | String | 单次委托类型  
`1`：单次委托量具体数值将从 TradingView 信号中传入  
`2`：单次委托量为固定数量的保证金  
`3`：单次委托量为固定的合约张数  
`4`：单次委托量基于在收到触发信号时策略中可用保证金的百分比  
`5`：单次委托量基于在创建策略时设置的初始投入保证金的百分比  
> amt | String | 单笔委托量  
在单次委托类型是 固定保证金 / 合约张数 下该字段有效，无效的时候返回""  
> ratio | String | 单笔委托数量百分比  
在单次委托类型是 占用保证金比例 / 初始投资比例 下该字段有效，无效的时候返回""  
exitSettingParam | Object | 离场参数设定  
> tpSlType | String | 止盈止损类型，该参数用户确定设置止盈止损的触发价格计算的方式  
`pnl`：基于平均持仓成本和预期收益率  
`price`：基于相对于平均持仓成本的涨跌幅  
> tpPct | String | 止盈百分比  
> slPct | String | 止损百分比  
signalChanId | String | 信号ID  
signalChanName | String | 信号名称  
signalSourceType | String | 信号来源类型  
`1`：自己创建的  
`2`：订阅他人  
`3`：免费信号