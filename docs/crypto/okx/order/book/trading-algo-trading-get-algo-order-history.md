---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#order-book-trading-algo-trading-get-algo-order-history
anchor_id: order-book-trading-algo-trading-get-algo-order-history
api_type: API
updated_at: 2026-07-23 19:21:22.790159
---

# GET / Algo order history

Retrieve a list of all algo orders under the current account in the last 3 months.  
  
#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: User ID

#### HTTP Request

`GET /api/v5/trade/orders-algo-history`

> Request Example
    
    
    GET /api/v5/trade/orders-algo-history?ordType=conditional&state=effective
    
    
    
    import okx.Trade as Trade
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # Production trading: 0, Demo trading: 1
    
    tradeAPI = Trade.TradeAPI(apikey, secretkey, passphrase, False, flag)
    
    # Retrieve a list of all one-way stop algo orders
    result = tradeAPI.order_algos_history(
        state="effective",
        ordType="conditional"
    )
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
ordType | String | Yes | Order type   
`conditional`: One-way stop order   
`oco`: One-cancels-the-other order   
`chase`: chase order, only applicable to FUTURES and SWAP  
`trigger`: Trigger order   
`move_order_stop`: Trailing order   
`iceberg`: Iceberg order   
`twap`: TWAP order  
`smart_iceberg`: Iceberg order  
For every request, unlike other ordType which only can use one type, `conditional` and `oco` both can be used and separated with comma.  
state | String | Conditional | State  
`effective`  
`canceled`  
`order_failed`  
Either `state` or `algoId` is required  
algoId | String | Conditional | Algo ID   
Either `state` or `algoId` is required.  
instType | String | No | Instrument type  
`SPOT`  
`SWAP`  
`FUTURES`  
`MARGIN`  
instId | String | No | Instrument ID, e.g. `BTC-USDT`  
after | String | No | Pagination of data to return records earlier than the requested `algoId`  
before | String | No | Pagination of data to return records new than the requested `algoId`  
limit | String | No | Number of results per request. The maximum is `100`. The default is `100`  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "activePx": "",
                "actualPx": "",
                "actualSide": "tp",
                "actualSz": "100",
                "algoClOrdId": "",
                "algoId": "1880721064716505088",
                "amendPxOnTriggerType": "0",
                "attachAlgoOrds": [],
                "cTime": "1728552255493",
                "callbackRatio": "",
                "callbackSpread": "",
                "ccy": "",
                "chaseType": "",
                "chaseVal": "",
                "clOrdId": "",
                "closeFraction": "1",
                "failCode": "1",
                "instId": "BTC-USDT-SWAP",
                "instType": "SWAP",
                "isTradeBorrowMode": "",
                "last": "60777.5",
                "lever": "10",
                "linkedOrd": {
                    "ordId": ""
                },
                "maxChaseType": "",
                "maxChaseVal": "",
                "moveTriggerPx": "",
                "ordId": "1884789786215137280",
                "ordIdList": [
                    "1884789786215137280"
                ],
                "ordPx": "",
                "ordType": "oco",
                "posSide": "long",
                "pxLimit": "",
                "pxSpread": "",
                "pxVar": "",
                "quickMgnType": "",
                "reduceOnly": "true",
                "side": "sell",
                "slOrdPx": "-1",
                "slTriggerPx": "57000",
                "slTriggerPxType": "mark",
                "state": "effective",
                "sz": "100",
                "szLimit": "",
                "tag": "",
                "tdMode": "isolated",
                "tgtCcy": "",
                "timeInterval": "",
                "tpOrdPx": "-1",
                "tpTriggerPx": "63000",
                "tpTriggerPxType": "last",
                "triggerPx": "",
                "triggerPxType": "",
                "triggerTime": "1728673513447",
                "tradeQuoteCcy": "USDT",
                "uTime": "1728673513447"
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
instType | String | Instrument type  
instId | String | Instrument ID  
ccy | String | Margin currency   
Applicable to all `isolated` `MARGIN` orders and `cross` `MARGIN` orders in `Futures mode`, `FUTURES` and `SWAP` contracts.  
ordId | String | Latest order ID. It will be deprecated soon  
ordIdList | Array of strings | Order ID list. There will be multiple order IDs when there is TP/SL splitting order. Empty for a trigger+chase (the spawned order is an algo — see `subAlgoIdList`).  
subAlgoIdList | Array of strings | `algoId`(s) of the algo order(s) spawned when the trigger fires. For `advanceOrdType` `chase`, holds the spawned chase order's `algoId` after the trigger fires; empty before then. Mirrors `ordIdList`, which records spawned regular orders.  
algoId | String | Algo ID  
clOrdId | String | Client Order ID as assigned by the client  
sz | String | Quantity to buy or sell  
closeFraction | String | Fraction of position to be closed when the algo order is triggered  
ordType | String | Order type  
side | String | Order side  
posSide | String | Position side  
tdMode | String | Trade mode  
tgtCcy | String | Order quantity unit setting for `sz`  
`base_ccy`: Base currency ,`quote_ccy`: Quote currency   
Only applicable to `SPOT` Market Orders  
Default is `quote_ccy` for buy, `base_ccy` for sell  
state | String | State   
`effective`   
`canceled`   
`order_failed`   
`partially_failed`  
lever | String | Leverage, from `0.01` to `125`.   
Only applicable to `MARGIN/FUTURES/SWAP`  
tpTriggerPx | String | Take-profit trigger price.  
tpTriggerPxType | String | Take-profit trigger price type.   
`last`: last price  
`index`: index price  
`mark`: mark price  
tpOrdPx | String | Take-profit order price.  
slTriggerPx | String | Stop-loss trigger price.  
slTriggerPxType | String | Stop-loss trigger price type.   
`last`: last price  
`index`: index price  
`mark`: mark price  
slOrdPx | String | Stop-loss order price.  
triggerPx | String | trigger price.  
triggerPxType | String | trigger price type.   
`last`: last price  
`index`: index price  
`mark`: mark price  
ordPx | String | Order price for the trigger order  
advanceOrdType | String | Sub-order type for trigger orders.  
`fok`: Fill-or-kill order  
`ioc`: Immediate-or-cancel order  
`chase`: Chase limit order  
Default is "".  
advChaseParams | Array of objects | Chase parameters. Present when `advanceOrdType` is `chase`.  
> chaseType | String | Chase distance unit. `distance` or `ratio`.  
> chaseVal | String | Chase value. `0` tracks the best bid/ask directly; `>0` is a distance.  
> maxChaseType | String | Maximum chase distance unit. `distance` or `ratio`.  
> maxChaseVal | String | Maximum chase distance value.  
actualSz | String | Actual order quantity  
actualPx | String | Actual order price  
tag | String | Order tag  
actualSide | String | Actual trigger side, `tp`: take profit `sl`: stop loss  
Only applicable to oco order and conditional order  
triggerTime | String | Trigger time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
pxVar | String | Price ratio   
Only applicable to `iceberg` order or `twap` order  
pxSpread | String | Price variance   
Only applicable to `iceberg` order or `twap` order  
szLimit | String | Average amount   
Only applicable to `iceberg` order or `twap` order  
pxLimit | String | Price Limit   
Only applicable to `iceberg` order or `twap` order  
lmtOrderNumber | String | Number of limit order splits  
Only applicable to `smart_iceberg`  
aggressiveness | String | Aggressiveness level  
`radical`: Faster fill  
`mid`: Faster fill with better price  
`conservative`: Queue at best bid/ask  
Only applicable to `smart_iceberg`  
triggerParams | Array of objects | Trigger parameters  
Only applicable to `smart_iceberg`  
> triggerAction | String | Trigger action  
`start`: Start iceberg order  
> triggerStrategy | String | Trigger strategy  
`instant`: Trigger immediately  
`price`: Trigger by price  
`rsi`: Trigger by RSI indicator  
> triggerPx | String | Trigger price  
Only valid when `triggerStrategy` is `price`  
> triggerCond | String | Trigger condition  
`cross_up` / `cross_down` / `above` / `below` / `cross`  
Only valid when `triggerStrategy` is `rsi`  
> timeframe | String | K-line type: `3m` / `5m` / `15m` / `30m` (m = minute)  
`1H` / `4H` (H = hour)  
`1D` (D = day)  
Only valid when `triggerStrategy` is `rsi`  
> thold | String | Threshold, integer in range [1, 100]  
Only valid when `triggerStrategy` is `rsi`  
> timePeriod | String | RSI calculation period. Default and fixed value is `14`  
Only valid when `triggerStrategy` is `rsi`  
timeInterval | String | Time interval   
Only applicable to `twap` order  
callbackRatio | String | Callback price ratio  
Only applicable to `move_order_stop` order  
callbackSpread | String | Callback price variance  
Only applicable to `move_order_stop` order  
activePx | String | Active price  
Only applicable to `move_order_stop` order  
moveTriggerPx | String | Trigger price  
Only applicable to `move_order_stop` order  
reduceOnly | String | Whether the order can only reduce the position size. Valid options: true or false.  
quickMgnType | String | ~~Quick Margin type, Only applicable to Quick Margin Mode of isolated margin  
`manual`, `auto_borrow`, `auto_repay`~~ (Deprecated)  
last | String | Last filled price while placing  
failCode | String | It represents that the reason that algo order fails to trigger. It is "" when the state is `effective`/`canceled`. There will be value when the state is `order_failed`, e.g. 51008;  
Only applicable to Stop Order, Trailing Stop Order, Trigger order.  
algoClOrdId | String | Client Algo Order ID as assigned by the client.  
amendPxOnTriggerType | String | Whether to enable Cost-price SL. Only applicable to SL order of split TPs.   
`0`: disable, the default value   
`1`: Enable  
attachAlgoOrds | Array of objects | Attached TP/SL or trailing stop order info  
Applicable to `Futures mode/Multi-currency margin/Portfolio margin`  
> attachAlgoClOrdId | String | Client-supplied Algo ID when placing order with attached TP/SL or trailing stop.  
A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters.  
It will be posted to algoClOrdId when placing the attached algo order once the general order is filled completely.  
> tpTriggerPx | String | Take-profit trigger price  
If you fill in this parameter, you should fill in the take-profit order price as well.  
> tpTriggerRatio | String | Take profit trigger ratio, 0.3 represents 30%   
Only applicable to FUTURES and SWAP.  
> tpTriggerPxType | String | Take-profit trigger price type  
`last`: last price  
`index`: index price  
`mark`: mark price  
> tpOrdPx | String | Take-profit order price  
If you fill in this parameter, you should fill in the take-profit trigger price as well.   
If the price is `-1`, take-profit will be executed at the market price.  
> slTriggerPx | String | Stop-loss trigger price  
If you fill in this parameter, you should fill in the stop-loss order price.  
> slTriggerRatio | String | Stop-loss trigger ratio, 0.3 represents 30%   
Only applicable to FUTURES and SWAP.  
> slTriggerPxType | String | Stop-loss trigger price type  
`last`: last price  
`index`: index price  
`mark`: mark price  
> slOrdPx | String | Stop-loss order price   
If you fill in this parameter, you should fill in the stop-loss trigger price.   
If the price is `-1`, stop-loss will be executed at the market price.  
> callbackRatio | String | Callback ratio, e.g. `0.05` represents 5%  
> callbackSpread | String | Callback spread (price distance)  
> activePx | String | Activation price  
linkedOrd | Object | Linked TP order detail, only applicable to SL order that comes from the one-cancels-the-other (OCO) order that contains the TP limit order.  
> ordId | String | Order ID  
cTime | String | Creation time Unix timestamp format in milliseconds, e.g. `1597026383085`  
uTime | String | Order updated time, Unix timestamp format in milliseconds, e.g. 1597026383085  
isTradeBorrowMode | String | Whether borrowing currency automatically  
true  
false  
Only applicable to `trigger order`, `trailing order` and `twap order`  
chaseType | String | Chase type. Only applicable to `chase` order.  
chaseVal | String | Chase value. Only applicable to `chase` order.  
maxChaseType | String | Maximum chase type. Only applicable to `chase` order.  
maxChaseVal | String | Maximum chase value. Only applicable to `chase` order.  
tradeQuoteCcy | String | The quote currency used for trading.

---

# GET / 获取历史策略委托单列表

获取最近3个月当前账户下所有策略委托单列表  
  
#### 限速：20次/2s

#### 限速规则：User ID

#### HTTP请求

`GET /api/v5/trade/orders-algo-history`

> 请求示例
    
    
    GET /api/v5/trade/orders-algo-history?ordType=conditional&state=effective
    
    
    
    import okx.Trade as Trade
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # 实盘: 0, 模拟盘: 1
    
    tradeAPI = Trade.TradeAPI(apikey, secretkey, passphrase, False, flag)
    
    # 查询 单向止盈止损 历史订单
    result = tradeAPI.order_algos_history(
        state="effective",
        ordType="conditional"
    )
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
ordType | String | 是 | 订单类型  
`conditional`：单向止盈止损  
`oco`：双向止盈止损  
`chase`: 追逐限价委托，仅适用于交割和永续  
`trigger`：计划委托  
`move_order_stop`：移动止盈止损  
`twap`：时间加权委托  
`smart_iceberg`：冰山委托  
支持 `conditional` 和 `oco` 同时查询，半角逗号分隔，对于其他类型，一次请求仅支持查询一个  
state | String | 可选 | 订单状态  
`effective`：已生效  
`canceled`：已经撤销  
`order_failed`：委托失败  
`state`和`algoId`必填且只能填其一  
algoId | String | 可选 | 策略委托单ID  
instType | String | 否 | 产品类型  
`SPOT`：币币  
`SWAP`：永续合约  
`FUTURES`：交割合约  
`MARGIN`：杠杆  
instId | String | 否 | 产品ID，`BTC-USDT`  
after | String | 否 | 请求此ID之前（更旧的数据）的分页内容，传的值为对应接口的`algoId`  
before | String | 否 | 请求此ID之后（更新的数据）的分页内容，传的值为对应接口的`algoId`  
limit | String | 否 | 返回结果的数量，最大为100，默认100条  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "activePx": "",
                "actualPx": "",
                "actualSide": "tp",
                "actualSz": "100",
                "algoClOrdId": "",
                "algoId": "1880721064716505088",
                "amendPxOnTriggerType": "0",
                "attachAlgoOrds": [],
                "cTime": "1728552255493",
                "callbackRatio": "",
                "callbackSpread": "",
                "ccy": "",
                "chaseType": "",
                "chaseVal": "",
                "clOrdId": "",
                "closeFraction": "1",
                "failCode": "1",
                "instId": "BTC-USDT-SWAP",
                "instType": "SWAP",
                "isTradeBorrowMode": "",
                "last": "60777.5",
                "lever": "10",
                "linkedOrd": {
                    "ordId": ""
                },
                "maxChaseType": "",
                "maxChaseVal": "",
                "moveTriggerPx": "",
                "ordId": "1884789786215137280",
                "ordIdList": [
                    "1884789786215137280"
                ],
                "ordPx": "",
                "ordType": "oco",
                "posSide": "long",
                "pxLimit": "",
                "pxSpread": "",
                "pxVar": "",
                "quickMgnType": "",
                "reduceOnly": "true",
                "side": "sell",
                "slOrdPx": "-1",
                "slTriggerPx": "57000",
                "slTriggerPxType": "mark",
                "state": "effective",
                "sz": "100",
                "szLimit": "",
                "tag": "",
                "tdMode": "isolated",
                "tgtCcy": "",
                "timeInterval": "",
                "tpOrdPx": "-1",
                "tpTriggerPx": "63000",
                "tpTriggerPxType": "last",
                "triggerPx": "",
                "triggerPxType": "",
                "triggerTime": "1728673513447",
                "tradeQuoteCcy": "",
                "uTime": "1728673513447"
            }
        ],
        "msg": ""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
instType | String | 产品类型  
instId | String | 产品ID  
ccy | String | 保证金币种，适用于`逐仓杠杆`及`合约模式`下的`全仓杠杆`订单以及交割、永续和期权合约订单。  
ordId | String | 最新一笔订单ID，即将废弃。  
ordIdList | Array of strings | 订单ID列表，当止盈止损存在市价拆单时，会有多个。 对于追逐委托（trigger+chase），该字段为空——生成的订单为策略委托，参见 `subAlgoIdList`。  
subAlgoIdList | Array of strings | 计划委托触发时生成的策略委托单 `algoId`。当 `advanceOrdType` 为 `chase` 时，在触发后存放生成的追逐委托 `algoId`，触发前为空。与 `ordIdList` 对应，后者记录生成的普通订单。  
algoId | String | 策略委托单ID  
clOrdId | String | 客户自定义订单ID  
sz | String | 委托数量  
closeFraction | String | 策略委托触发时，平仓的百分比。1 代表100%  
ordType | String | 订单类型  
side | String | 订单方向  
posSide | String | 持仓方向  
tdMode | String | 交易模式  
tgtCcy | String | 币币市价单委托数量`sz`的单位  
`base_ccy`: 交易货币 ；`quote_ccy`：计价货币  
仅适用于`币币`市价订单  
默认买单为`quote_ccy`，卖单为`base_ccy`  
state | String | 订单状态  
`effective`：已生效  
`canceled`：已撤销   
`order_failed`：委托失败   
`partially_failed`：部分委托失败  
lever | String | 杠杆倍数，0.01到125之间的数值  
仅适用于 `币币杠杆`/`交割`/永续`  
tpTriggerPx | String | 止盈触发价  
tpTriggerPxType | String | 止盈触发价类型  
`last`：最新价格  
`index`：指数价格  
`mark`：标记价格  
tpOrdPx | String | 止盈委托价  
slTriggerPx | String | 止损触发价  
slTriggerPxType | String | 止损触发价类型  
`last`：最新价格  
`index`：指数价格  
`mark`：标记价格  
slOrdPx | String | 止损委托价  
triggerPx | String | 计划委托触发价格  
triggerPxType | String | 计划委托委托价格类型  
`last`：最新价格  
`index`：指数价格  
`mark`：标记价格  
ordPx | String | 计划委托委托价格  
advanceOrdType | String | 计划委托的子订单类型。  
`fok`：全部成交或立即取消  
`ioc`：立即成交并取消剩余  
`chase`：追逐限价委托  
默认为空。  
advChaseParams | Array of objects | 追逐参数。当 `advanceOrdType` 为 `chase` 时返回。  
> chaseType | String | 追逐距离单位。`distance` 或 `ratio`。  
> chaseVal | String | 追逐值。`0` 表示直接跟随买一价/卖一价；大于 `0` 表示距离。  
> maxChaseType | String | 最大追逐距离单位。`distance` 或 `ratio`。  
> maxChaseVal | String | 最大追逐距离值。  
actualSz | String | 实际委托量  
actualPx | String | 实际委托价  
actualSide | String | 实际触发方向  
`tp`：止盈  
`sl`：止损  
仅适用于`单向止盈止损委托`和`双向止盈止损委托`  
triggerTime | String | 策略委托触发时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
pxVar | String | 价格比例  
仅适用于`冰山委托`和`时间加权委托`  
pxSpread | String | 价距  
仅适用于`冰山委托`和`时间加权委托`  
szLimit | String | 单笔数量  
仅适用于`冰山委托`和`时间加权委托`  
pxLimit | String | 挂单限制价  
仅适用于`冰山委托`和`时间加权委托`  
lmtOrderNumber | String | 限价拆单数量  
仅适用于`冰山委托`  
aggressiveness | String | 激进度  
`radical`：更快成交  
`mid`：较快成交，较优价格  
`conservative`：盘口排队  
仅适用于`冰山委托`  
triggerParams | Array of objects | 触发参数  
仅适用于`冰山委托`  
> triggerAction | String | 触发行为  
`start`：启动冰山委托  
> triggerStrategy | String | 触发策略  
`instant`：立即触发  
`price`：价格触发  
`rsi`：RSI指标触发  
> triggerPx | String | 触发价格  
仅在 `triggerStrategy` 为 `price` 时有效  
> triggerCond | String | 触发条件  
`cross_up`：上穿  
`cross_down`：下穿  
`above`：上方  
`below`：下方  
`cross`：交叉  
仅在 `triggerStrategy` 为 `rsi` 时有效  
> timeframe | String | K线种类  
`3m`、`5m`、`15m`、`30m`（m代表分钟）  
`1H`、`4H`（H代表小时）  
`1D`（D代表天）  
仅在 `triggerStrategy` 为 `rsi` 时有效  
> thold | String | 阈值，取值 [1,100] 的整数  
仅在 `triggerStrategy` 为 `rsi` 时有效  
> timePeriod | String | RSI 计算周期，默认值为 `14`  
仅在 `triggerStrategy` 为 `rsi` 时有效  
tag | String | 订单标签  
timeInterval | String | 下单间隔  
仅适用于`时间加权委托`  
callbackRatio | String | 回调幅度的比例  
仅适用于`移动止盈止损`  
callbackSpread | String | 回调幅度的价距  
仅适用于`移动止盈止损`  
activePx | String | 移动止盈止损激活价格  
仅适用于`移动止盈止损`  
moveTriggerPx | String | 移动止盈止损触发价格  
仅适用于`移动止盈止损`  
reduceOnly | String | 是否只减仓  
`true`或`false`  
quickMgnType | String | ~~一键借币类型，仅适用于杠杆逐仓的一键借币模式  
`manual`：手动，`auto_borrow`：自动借币，`auto_repay`：自动还币~~（已弃用）  
last | String | 下单时的最新成交价  
failCode | String | 代表策略触发失败的原因，已撤销和已生效时为""，委托失败时有值，如 51008；  
仅适用于单向止盈止损委托、双向止盈止损委托、移动止盈止损委托、计划委托。  
algoClOrdId | String | 客户自定义策略订单ID  
amendPxOnTriggerType | String | 是否启用开仓价止损，仅适用于分批止盈的止损订单  
`0`：不开启，默认值   
`1`：开启  
attachAlgoOrds | Array of objects | 附带止盈止损或移动止盈止损订单信息  
适用于`合约模式/跨币种保证金模式/组合保证金模式`  
> attachAlgoClOrdId | String | 下单附带止盈止损或移动止盈止损时，客户自定义的策略订单ID，字母（区分大小写）与数字的组合，可以是纯字母、纯数字且长度要在1-32位之间。  
订单完全成交，下附带策略委托单时，该值会传给algoClOrdId。  
> tpTriggerPx | String | 止盈触发价，如果填写此参数，必须填写`止盈委托价`  
> tpTriggerRatio | String | 止盈触发比例，0.3 代表 30%   
仅适用于`交割`/`永续`合约  
> tpTriggerPxType | String | 止盈触发价类型  
`last`：最新价格  
`index`：指数价格  
`mark`：标记价格  
> tpOrdPx | String | 止盈委托价，如果填写此参数，必须填写`止盈触发价`  
委托价格为`-1`时，执行市价止盈  
> slTriggerPx | String | 止损触发价，如果填写此参数，必须填写`止损委托价`  
> slTriggerRatio | String | 止损触发比例，0.3 代表 30%   
仅适用于`交割`/`永续`合约  
> slTriggerPxType | String | 止损触发价类型  
`last`：最新价格  
`index`：指数价格  
`mark`：标记价格  
> slOrdPx | String | 止损委托价，如果填写此参数，必须填写`止损触发价`  
委托价格为`-1`时，执行市价止损  
> callbackRatio | String | 回调幅度的比例，如 `0.05` 代表 5%  
> callbackSpread | String | 回调幅度的价距  
> activePx | String | 激活价格  
linkedOrd | Object | 止盈订单信息，仅适用于止损单，且该止损订单来自包含限价止盈单的双向止盈止损订单  
> ordId | String | 订单 ID  
cTime | String | 订单创建时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
uTime | String | 订单更新时间，Unix时间戳的毫秒数格式，如 1597026383085  
isTradeBorrowMode | String | 是否自动借币  
true：自动借币  
false：不自动借币  
仅适用于计划委托、移动止盈止损和 时间加权策略  
chaseType | String | 追逐类型。仅适用于`追逐限价委托`。  
chaseVal | String | 追逐值。仅适用于`追逐限价委托`。  
maxChaseType | String | 最大追逐值的类型。仅适用于`追逐限价委托`。  
maxChaseVal | String | 最大追逐值。仅适用于`追逐限价委托`。  
tradeQuoteCcy | String | 用于交易的计价币种。