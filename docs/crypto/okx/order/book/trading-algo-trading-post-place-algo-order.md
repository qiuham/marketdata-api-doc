---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#order-book-trading-algo-trading-post-place-algo-order
anchor_id: order-book-trading-algo-trading-post-place-algo-order
api_type: API
updated_at: 2026-06-30 19:54:33.719712
---

# POST / Place algo order

The algo order includes `trigger` order, `oco` order, `chase` order, `conditional` order, `twap` order and trailing order.  
  
#### Rate Limit: 20 requests per 2 seconds

#### Rate Limit of lead trader lead instruments for Copy Trading: 1 request per 2 seconds

#### Rate limit rule (except Options): User ID + Instrument ID

#### Rate limit rule (Options only): User ID + Instrument Family

#### Permission: Trade

#### HTTP Request

`POST /api/v5/trade/order-algo`

> Request Example
    
    
    # Place Take Profit / Stop Loss Order
    POST /api/v5/trade/order-algo
    body
    {
        "instId":"BTC-USDT",
        "tdMode":"cross",
        "side":"buy",
        "ordType":"conditional",
        "sz":"2",
        "tpTriggerPx":"15",
        "tpOrdPx":"18"
    }
    
    # Place Trigger Order
    POST /api/v5/trade/order-algo
    body
    {
        "instId": "BTC-USDT-SWAP",
        "side": "buy",
        "tdMode": "cross",
        "posSide": "net",
        "sz": "1",
        "ordType": "trigger",
        "triggerPx": "25920",
        "triggerPxType": "last",
        "orderPx": "-1",
        "attachAlgoOrds": [{
            "attachAlgoClOrdId": "",
            "slTriggerPx": "100",
            "slOrdPx": "600",
            "tpTriggerPx": "25921",
            "tpOrdPx": "2001"
        }]
    }
    
    # Place Trailing Stop Order
    POST /api/v5/trade/order-algo
    body
    {
        "instId": "BTC-USDT-SWAP",
        "tdMode": "cross",
        "side": "buy",
        "ordType": "move_order_stop",
        "sz": "10",
        "posSide": "net",
        "callbackRatio": "0.05",
        "reduceOnly": true
    }
    
    # Place TWAP Order
    POST /api/v5/trade/order-algo
    body
    {
        "instId": "BTC-USDT-SWAP",
        "tdMode": "cross",
        "side": "buy",
        "ordType": "twap",
        "sz": "10",
        "posSide": "net",
        "szLimit": "10",
        "pxLimit": "100",
        "timeInterval": "10",
        "pxSpread": "10"
    }
    
    # Iceberg order
    POST /api/v5/trade/order-algo
    body
    {
        "instId": "BTC-USDT",
        "tdMode": "cash",
        "side": "buy",
        "ordType": "smart_iceberg",
        "sz": "100",
        "szLimit": "10",
        "lmtOrderNumber": "5",
        "aggressiveness": "conservative",
        "pxLimit": "95000",
        "triggerParams": [
            {
                "triggerAction": "start",
                "triggerStrategy": "price",
                "triggerPx": "90000",
                "triggerCond": "cross_down"
            }
        ]
    }
    
    
    
    
    import okx.Trade as Trade
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # Production trading: 0, Demo trading: 1
    
    tradeAPI = Trade.TradeAPI(apikey, secretkey, passphrase, False, flag)
    
    # One-way stop order
    result = tradeAPI.place_algo_order(
        instId="BTC-USDT",
        tdMode="cross",
        side="buy",
        ordType="conditional",
        sz="2",
        tpTriggerPx="15",
        tpOrdPx="18"
    )
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
instId | String | Yes | Instrument ID, e.g. `BTC-USDT`  
tdMode | String | Yes | Trade mode  
Margin mode `cross` `isolated`  
Non-Margin mode `cash`  
`spot_isolated` (only applicable to SPOT lead trading)  
Note: `isolated` is not available in multi-currency margin mode and portfolio margin mode.  
ccy | String | No | Margin currency   
Applicable to all `isolated` `MARGIN` orders and `cross` `MARGIN` orders in `Futures mode`.  
side | String | Yes | Order side, `buy` `sell`  
posSide | String | Conditional | Position side   
Required in `long/short` mode and only be `long` or `short`  
ordType | String | Yes | Order type   
`conditional`: One-way stop order  
`oco`: One-cancels-the-other order  
`chase`: chase order, only applicable to FUTURES and SWAP  
`trigger`: Trigger order  
`move_order_stop`: Trailing order  
`twap`: TWAP order  
`smart_iceberg`: Iceberg order  
sz | String | Conditional | Quantity to buy or sell  
Either `sz` or `closeFraction` is required.  
tag | String | No | Order tag   
A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 16 characters.  
tgtCcy | String | No | Order quantity unit setting for `sz`  
`base_ccy`: Base currency ,`quote_ccy`: Quote currency   
Only applicable to `SPOT` traded with Market buy `conditional` order  
Default is `quote_ccy` for buy, `base_ccy` for sell  
algoClOrdId | String | No | Client-supplied Algo ID  
A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters.  
closeFraction | String | Conditional | Fraction of position to be closed when the algo order is triggered.   
Currently the system supports fully closing the position only so the only accepted value is `1`. For the same position, only one TPSL pending order for fully closing the position is supported.   
This is only applicable to `FUTURES` or `SWAP` instruments.  
If `posSide` is `net`, `reduceOnly` must be `true`.  
This is only applicable if `ordType` is `conditional` or `oco`.  
This is only applicable if the stop loss and take profit order is executed as market order.  
This is not supported in Portfolio Margin mode.  
Either `sz` or `closeFraction` is required.  
tradeQuoteCcy | String | No | The quote currency used for trading. Only applicable to `SPOT`.   
The default value is the quote currency of the `instId`, for example: for `BTC-USD`, the default is `USD`.  
  
**Take Profit / Stop Loss Order**

Predefine the price you want the order to trigger a market order to execute immediately or it will place a limit order.   
This type of order will not freeze your free margin in advance. 

learn more about [Take Profit / Stop Loss Order](/help/11015447687437)

Parameter | Type | Required | Description  
---|---|---|---  
tpTriggerPx | String | No | Take-profit trigger price  
If you fill in this parameter, you should fill in the take-profit order price as well.  
tpTriggerPxType | String | No | Take-profit trigger price type  
`last`: last price  
`index`: index price  
`mark`: mark price   
The default is `last`  
tpOrdPx | String | No | Take-profit order price   
For condition TP order, if you fill in this parameter, you should fill in the take-profit trigger price as well.  
For limit TP order, you need to fill in this parameter, but the take-profit trigger price doesn’t need to be filled.   
If the price is `-1`, take-profit will be executed at the market price.  
tpOrdKind | String | No | TP order kind  
`condition`  
`limit`  
The default is `condition`  
slTriggerPx | String | No | Stop-loss trigger price   
If you fill in this parameter, you should fill in the stop-loss order price.  
slTriggerPxType | String | No | Stop-loss trigger price type  
`last`: last price  
`index`: index price  
`mark`: mark price   
The default is `last`  
slOrdPx | String | No | Stop-loss order price   
If you fill in this parameter, you should fill in the stop-loss trigger price.   
If the price is `-1`, stop-loss will be executed at the market price.  
cxlOnClosePos | Boolean | No | Whether the TP/SL order placed by the user is associated with the corresponding position of the instrument. If it is associated, the TP/SL order will be canceled when the position is fully closed; if it is not, the TP/SL order will not be affected when the position is fully closed.   
Valid values:   
`true`: Place a TP/SL order associated with the position   
`false`: Place a TP/SL order that is not associated with the position   
The default value is `false`. If `true` is passed in, users must pass reduceOnly = true as well, indicating that when placing a TP/SL order associated with a position, it must be a reduceOnly order.   
Only applicable to `Futures mode` and `Multi-currency margin`.  
reduceOnly | Boolean | No | Whether the order can only reduce the position size.   
Valid options: `true` or `false`. The default value is `false`.  
Take Profit / Stop Loss Order  
When placing net TP/SL order (ordType=conditional) and both take-profit and stop-loss parameters are sent, only stop-loss logic will be performed and take-profit logic will be ignored. 

**Chase order**

It will place a Post Only order immediately and amend it continuously  
Chase order and corresponding Post Only order can't be amended. 

Parameter | Type | Required | Description  
---|---|---|---  
chaseType | String | No | Chase type.  
`distance`: distance from best bid/ask price, the default value.  
`ratio`: ratio.  
chaseVal | String | No | Chase value.  
It represents distance from best bid/ask price when `chaseType` is distance.   
For USDT-margined contract, the unit is USDT.   
For USDC-margined contract, the unit is USDC.   
For Crypto-margined contract, the unit is USD.   
It represents ratio when `chaseType` is ratio. 0.1 represents 10%.  
The default value is 0.  
maxChaseType | String | Conditional | Maximum chase type.  
`distance`: maximum distance from best bid/ask price  
`ratio`: the ratio.   
  
maxChaseTyep and maxChaseVal need to be used together or none of them.  
maxChaseVal | String | Conditional | Maximum chase value.  
It represents maximum distance when `maxChaseType` is distance.  
It represents ratio when `maxChaseType` is ratio. 0.1 represents 10%.  
reduceOnly | Boolean | No | Whether the order can only reduce the position size.   
Valid options: `true` or `false`. The default value is `false`.  
  
**Trigger Order**

Use a trigger order to place a market or limit order when a specific price level is crossed.   
When a Trigger Order is triggered, if your account balance is lower than the order amount, the system will automatically place the order based on your current balance.   
Trigger orders do not freeze assets when placed.  
Only applicable to SPOT/FUTURES/SWAP 

learn more about [Trigger Order](/help/11015447687437)

Parameter | Type | Required | Description  
---|---|---|---  
triggerPx | String | Yes | The price level that activates this algo order. Unit: same as `px` for the instrument. Which price feed is compared depends on `triggerPxType` (default: last trade price). Direction: for a sell stop-loss, trigger must be below orderPx; for a buy stop, above orderPx. Error codes 51046–51049 are returned for direction violations.  
orderPx | String | Yes | Price of the order submitted when `triggerPx` is reached. This is separate from `triggerPx` (which determines when the algo activates). Set to `-1` to submit a market order when triggered; set to a specific price to submit a limit order.  
advanceOrdType | String | No | Trigger order type  
`fok`: Fill-or-kill order  
`ioc`: Immediate-or-cancel order  
Default is "", limit or market (controlled by orderPx)  
triggerPxType | String | No | Trigger price type:  
`last`: triggers when any trade occurs at or beyond `triggerPx` — most responsive but vulnerable to brief price wicks in thin markets.  
`index`: triggers on the underlying multi-exchange composite index — stable, not affected by OKX-specific wicks.  
`mark`: triggers on OKX mark price — smoothed and wick-resistant; recommended for derivatives.  
`last` is the only option available for SPOT instruments. The default is `last`.  
attachAlgoOrds | Array of objects | No | Attached SL/TP orders info  
Applicable to `Futures mode/Multi-currency margin/Portfolio margin`  
> attachAlgoClOrdId | String | No | Client-supplied Algo ID when placing order attaching TP/SL.  
A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters.  
It will be posted to algoClOrdId when placing TP/SL order once the general order is filled completely.  
> tpTriggerPx | String | No | Take-profit trigger price  
If you fill in this parameter, you should fill in the take-profit order price as well.  
> tpTriggerRatio | String | No | Take profit trigger ratio, 0.3 represents 30%   
Only applicable to FUTURES and SWAP.   
Only one of `tpTriggerPx` and `tpTriggerRatio` can be passed   
If the main order is a buy order, it must be greater than 0, and if the main order is a sell order, it must be between -1 and 0.  
> tpTriggerPxType | String | No | Take-profit trigger price type  
`last`: last price  
`index`: index price  
`mark`: mark price  
The default is `last`  
> tpOrdPx | String | No | Take-profit order price  
If you fill in this parameter, you should fill in the take-profit trigger price as well.   
If the price is `-1`, take-profit will be executed at the market price.  
> slTriggerPx | String | No | Stop-loss trigger price  
If you fill in this parameter, you should fill in the stop-loss order price.  
> slTriggerRatio | String | No | Stop-loss trigger ratio, 0.3 represents 30%   
Only applicable to FUTURES and SWAP.   
Only one of `slTriggerPx` and `slTriggerRatio` can be passed   
If the main order is a buy order, it must be between 0 and 1, and if the main order is a sell order, it must be greater than 0.  
> slTriggerPxType | String | No | Stop-loss trigger price type  
`last`: last price  
`index`: index price  
`mark`: mark price   
The default is `last`  
> slOrdPx | String | No | Stop-loss order price   
If you fill in this parameter, you should fill in the stop-loss trigger price.   
If the price is `-1`, stop-loss will be executed at the market price.  
> callbackRatio | String | Conditional | Callback ratio, e.g. `0.05` represents 5%.  
Either `callbackRatio` or `callbackSpread` is required. Only one can be passed.  
Only applicable when `ordType` = `move_order_stop`  
> callbackSpread | String | Conditional | Callback spread (price distance).  
Either `callbackRatio` or `callbackSpread` is required. Only one can be passed.  
Only applicable when `ordType` = `move_order_stop`  
> activePx | String | No | Activation price.  
The trailing stop is activated when the market price reaches the activation price. After activation, the system starts calculating the actual trigger price. If not provided, the trailing stop is activated immediately upon order placement.  
Only applicable when `ordType` = `move_order_stop`  
  
**Trailing Stop Order**

A trailing stop order is a stop order that tracks the market price. Its trigger price changes with the market price. Once the trigger price is reached, a market order is placed.  
Actual trigger price for sell orders and short positions = Highest price after order placement – Trail variance (Var.), or Highest price after placement × (1 – Trail variance) (Ratio).  
Actual trigger price for buy orders and long positions = Lowest price after order placement + Trail variance, or Lowest price after order placement × (1 + Trail variance).  
You can use the activation price to set the activation condition for a trailing stop order. 

learn more about [Trailing Stop Order](/help/11015447687437)

Parameter | Type | Required | Description  
---|---|---|---  
callbackRatio | String | Conditional | Callback price ratio, e.g. `0.01` represents `1%`  
Either `callbackRatio` or `callbackSpread` is allowed to be passed.  
callbackSpread | String | Conditional | Callback price variance  
activePx | String | No | Active price  
The system will only start tracking the market and calculating your trigger price after the activation price is reached. If you don’t set a price, your order will be activated as soon as it’s placed.  
reduceOnly | Boolean | No | Whether the order can only reduce the position size.   
Valid options: `true` or `false`. The default value is `false`.  
This parameter is only valid in the `FUTRUES`/`SWAP` net mode, and is ignored in the long/short mode.  
  
**TWAP Order**

Time-weighted average price (TWAP) strategy splits your order and places smaller orders at regular time intervals.  
It is a strategy that will attempt to execute an order which trades in slices of order quantity at regular intervals of time as specified by users.  

learn more about [TWAP Order](/help/xiii-time-weighted-average-price-twap)

Parameter | Type | Required | Description  
---|---|---|---  
pxVar | String | Conditional | Price variance by percentage, range between [0.0001 ~ 0.01], e.g. `0.01` represents `1%`  
Take buy orders as an example. When the market price is lower than the limit price, small buy orders will be placed above the best bid price within a certain range. This parameter determines the range by percentage.  
Either `pxVar` or `pxSpread` is allowed to be passed.  
pxSpread | String | Conditional | Price variance by constant, should be no less then 0 (no upper limit)  
Take buy orders as an example. When the market price is lower than the limit price, small buy orders will be placed above the best bid price within a certain range. This parameter determines the range by constant.  
szLimit | String | Yes | Average amount  
Take buy orders as an example. When the market price is lower than the limit price, a certain amount of buy orders will be placed above the best bid price within a certain range. This parameter determines the amount.  
pxLimit | String | Yes | Price Limit, should be no less then 0 (no upper limit)  
Take buy orders as an example. When the market price is lower than the limit price, small buy orders will be placed above the best bid price within a certain range. This parameter represents the limit price.  
timeInterval | String | Yes | Time interval in unit of `second`  
ake buy orders as an example. When the market price is lower than the limit price, small buy orders will be placed above the best bid price within a certain range based on the time cycle. This parameter represents the time cycle.  
  
**Iceberg Order**

Parameter | Type | Required | Description  
---|---|---|---  
szLimit | String | Yes | Minimum order size per execution. Only applicable to `smart_iceberg`  
lmtOrderNumber | String | Yes | Number of limit order splits. Only applicable to `smart_iceberg`  
aggressiveness | String | Yes | Aggressiveness level. Only applicable to `smart_iceberg`  
`radical`: Faster fill  
`mid`: Faster fill with better price  
`conservative`: Queue at best bid/ask  
pxLimit | String | No | Price limit. Only applicable to `smart_iceberg`  
triggerParams | Array of objects | No | Trigger parameters. If the list is empty, the order is triggered immediately by default. Only applicable to `smart_iceberg`  
> triggerAction | String | Yes | Trigger action  
`start`: Start iceberg order  
> triggerStrategy | String | Yes | Trigger strategy  
`instant`: Trigger immediately  
`price`: Trigger by price  
`rsi`: Trigger by RSI indicator  
Default is `instant`  
> triggerPx | String | No | Trigger price  
Only valid when `triggerStrategy` is `price`  
> triggerCond | String | No | Trigger condition  
`cross_up` / `cross_down` / `above` / `below` / `cross`  
Only valid when `triggerStrategy` is `rsi`  
> timeframe | String | No | K-line type: 3m / 5m / 15m / 30m / 1H / 4H / 1D  
Only valid when `triggerStrategy` is `rsi`  
> thold | String | No | Threshold, range [1, 100]  
Only valid when `triggerStrategy` is `rsi`  
> timePeriod | String | No | RSI calculation period. Default and fixed value is `14`. Only valid when `triggerStrategy` is `rsi`  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "algoClOrdId": "order1234",
                "algoId": "1836487817828872192",
                "clOrdId": "",
                "sCode": "0",
                "sMsg": "",
                "tag": ""
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
algoId | String | Algo ID  
clOrdId | String | ~~Client Order ID as assigned by the client~~(Deprecated)  
algoClOrdId | String | Client-supplied Algo ID  
sCode | String | The code of the event execution result, `0` means success.  
sMsg | String | Rejection message if the request is unsuccessful.  
tag | String | Order tag

---

# POST / 策略委托下单

提供单向止盈止损委托、双向止盈止损委托、追逐限价委托、计划委托、时间加权委托、移动止盈止损委托  
  
#### 限速：20次/2s

#### 跟单交易带单员带单产品的限速：1次/2s

#### 限速规则（期权以外）：User ID + Instrument ID

#### 限速规则（只限期权）：User ID + Instrument Family

#### 权限：交易

#### HTTP请求

`POST /api/v5/trade/order-algo`

> 请求示例
    
    
    # 止盈止损策略下单
    POST /api/v5/trade/order-algo
    body
    {
        "instId":"BTC-USDT",
        "tdMode":"cross",
        "side":"buy",
        "ordType":"conditional",
        "sz":"2",
        "tpTriggerPx":"15",
        "tpOrdPx":"18"
    }
    
    # 计划委托策略下单
    POST /api/v5/trade/order-algo
    body
    {
        "instId": "BTC-USDT-SWAP",
        "side": "buy",
        "tdMode": "cross",
        "posSide": "net",
        "sz": "1",
        "ordType": "trigger",
        "triggerPx": "25920",
        "triggerPxType": "last",
        "orderPx": "-1",
        "attachAlgoOrds": [{
            "attachAlgoClOrdId": "",
            "slTriggerPx": "100",
            "slOrdPx": "600",
            "tpTriggerPx": "25921",
            "tpOrdPx": "2001"
        }]
    }
    
    # 移动止盈止损策略下单
    POST /api/v5/trade/order-algo
    body
    {
        "instId": "BTC-USDT-SWAP",
        "tdMode": "cross",
        "side": "buy",
        "ordType": "move_order_stop",
        "sz": "10",
        "posSide": "net",
        "callbackRatio": "0.05",
        "reduceOnly": true
    }
    
    # 时间加权策略下单
    POST /api/v5/trade/order-algo
    body
    {
        "instId": "BTC-USDT-SWAP",
        "tdMode": "cross",
        "side": "buy",
        "ordType": "twap",
        "sz": "10",
        "posSide": "net",
        "szLimit": "10",
        "pxLimit": "100",
        "timeInterval": "10",
        "pxSpread": "10"
    }
    
    # 冰山委托策略下单
    POST /api/v5/trade/order-algo
    body
    {
        "instId": "BTC-USDT",
        "tdMode": "cash",
        "side": "buy",
        "ordType": "smart_iceberg",
        "sz": "1000",
        "szLimit": "50",
        "lmtOrderNumber": "5",
        "aggressiveness": "conservative",
        "pxLimit": "95000",
        "side": "buy",
        "posSide": "",
        "ordType": "smart_iceberg",
        "triggerParams": [
          {
              "triggerAction":"start",
              "triggerStrategy":"rsi",
              "timeframe":"30m",
              "thold":"10",
              "triggerCond":"cross",
              "timePeriod":"14"
    }
    
    
    
    import okx.Trade as Trade
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # 实盘: 0, 模拟盘: 1
    
    tradeAPI = Trade.TradeAPI(apikey, secretkey, passphrase, False, flag)
    
    # 单向止盈止损
    result = tradeAPI.place_algo_order(
        instId="BTC-USDT",
        tdMode="cross",
        side="buy",
        ordType="conditional",
        sz="2",
        tpTriggerPx="15",
        tpOrdPx="18"
    )
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
instId | String | 是 | 产品ID，如 `BTC-USDT`  
tdMode | String | 是 | 交易模式  
保证金模式 `isolated`：逐仓，`cross：`全仓  
非保证金模式 `cash`：非保证金  
`spot_isolated`：现货逐仓(仅适用于现货带单)  
注意：`isolated` 在跨币种保证金模式和组合保证金模式下不可用。  
ccy | String | 否 | 保证金币种  
适用于`逐仓杠杆`及`合约模式`下的`全仓杠杆`订单  
side | String | 是 | 订单方向  
`buy`：买  
`sell`：卖  
posSide | String | 可选 | 持仓方向  
在开平仓模式下必填，且仅可选择 `long` 或 `short`  
ordType | String | 是 | 订单类型  
`conditional`：单向止盈止损  
`oco`：双向止盈止损  
  
`chase`: 追逐限价委托，仅适用于交割和永续  
`trigger`：计划委托  
`move_order_stop`：移动止盈止损  
`twap`：时间加权委托  
`smart_iceberg`：冰山委托  
sz | String | 可选 | 委托数量  
`sz`和`closeFraction`必填且只能填其一  
tag | String | 否 | 订单标签  
字母（区分大小写）与数字的组合，可以是纯字母、纯数字，且长度在1-16位之间  
tgtCcy | String | 否 | 委托数量的类型  
`base_ccy`: 交易货币 ；`quote_ccy`：计价货币  
仅适用于`币币`单向止盈止损市价买单  
默认买为`计价货币`，卖为`交易货币`  
algoClOrdId | String | 否 | 客户自定义策略订单ID  
字母（区分大小写）与数字的组合，可以是纯字母、纯数字且长度要在1-32位之间。  
closeFraction | String | 可选 | 策略委托触发时，平仓的百分比。1 代表100%  
现在系统只支持全部平仓，唯一接受参数为`1`  
对于同一个仓位，仅支持一笔全部平仓的止盈止损挂单  
  
仅适用于`交割`或`永续`  
当`posSide` = `net`时，`reduceOnly`必须为`true`  
仅适用于止盈止损 `ordType` = `conditional` 或 `oco`  
仅适用于止盈止损市价订单  
不支持组合保证金模式  
`sz`和`closeFraction`必填且只能填其一  
tradeQuoteCcy | String | 否 | 用于交易的计价币种。仅适用于`币币`。  
默认值为 `instId` 的计价币种，比如：对于 `BTC-USD`，默认取 `USD`。  
  
**止盈止损**

用户可预先设置触发价和委托价，等市场价到达触发价时，系统会按委托价自动下单。  
单向止盈止损可设置单边的止盈或止损；双向止盈止损可设置双边，一边触发后另一边失效。  
该委托不会预先占用仓位或保证金。 

了解更多 [止盈止损](/cn/help/11015447687437)

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
tpTriggerPx | String | 否 | 止盈触发价，如果填写此参数，必须填写`止盈委托价`  
tpTriggerPxType | String | 否 | 止盈触发价类型  
`last`：最新价格  
`index`：指数价格  
`mark`：标记价格  
默认为`last`  
tpOrdPx | String | 否 | 止盈委托价  
对于条件止盈单，如果填写此参数，必须填写`止盈触发价`  
对于限价止盈单，需填写此参数，不需要填写`止盈触发价`   
委托价格为-1时，执行市价止盈  
tpOrdKind | String | 否 | 止盈订单类型  
`condition`: 条件单  
`limit`: 限价单  
默认为`condition`  
slTriggerPx | String | 否 | 止损触发价，如果填写此参数，必须填写`止损委托价`  
slTriggerPxType | String | 否 | 止损触发价类型  
`last`：最新价格  
`index`：指数价格  
`mark`：标记价格  
默认为`last`  
slOrdPx | String | 否 | 止损委托价，如果填写此参数，必须填写`止损触发价`   
委托价格为`-1`时，执行市价止损  
cxlOnClosePos | Boolean | 否 | 决定用户所下的止盈止损订单是否与该交易产品对应的仓位关联。若关联，仓位被全平时，该止盈止损订单会被同时撤销；若不关联，仓位被撤销时，该止盈止损订单不受影响。   
  
有效值：   
`true`：下单与仓位关联的止盈止损订单   
`false`：下单与仓位不关联的止盈止损订单   
  
默认值为`false`。若传入`true`，用户必须同时传入 reduceOnly = true，说明当下单与仓位关联的止盈止损订单时，必须为只减仓。  
适用于`合约模式`/`跨币种保证金模式`。  
reduceOnly | Boolean | 否 | 是否只减仓，`true` 或 `false`，默认`false`  
仅适用于`币币杠杆`，以及买卖模式下的`交割/永续`  
仅适用于`合约模式`和`跨币种保证金模式`  
止盈止损  
当用户进行单向止盈止损委托（ordType=conditional）时，如果用户同时传了止盈止损四个参数，只进行止损的功能校验，忽略止盈的业务逻辑校验。 

**追逐限价委托**

追逐限价委托会立即下 Post Only 订单（只做maker单）并跟随深度变动进行改单。  
追逐限价委托和对应的 Post Only 订单不支持改单。  参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
chaseType | String | 否 | 追逐类型。  
`distance`: 买一/卖一价的距离，默认值。  
`ratio`: 比例。  
chaseVal | String | 否 | 追逐值。  
当`chaseType`为`distance`时，是到买一/卖一价的距离。  
对于 USDT 本位合约，单位为 USDT；  
对于 USDC 合约，单位为 USDC；  
对于币本位合约，单位为 USD 。  
当`chaseType`为`ratio`时，为比率，0.1 代表 10%。  
默认值为 0。  
maxChaseType | String | 可选 | 最大追逐值的类型。  
`distance`: 买一/卖一价的距离  
`ratio`: 比例。0.1 代表 10%。  
  
maxChaseTyep 和 maxChaseVal 需要同时填写或者不填写。  
maxChaseVal | String | 可选 | 最大追逐值。  
当`chaseType`为`distance`时，是到买一/卖一价的的最大距离  
当`chaseType`为`ratio`时，指的比率，0.1 代表 10%。  
reduceOnly | Boolean | 否 | 是否只减仓，`true` 或 `false`，默认`false`  
仅适用于`币币杠杆`，以及买卖模式下的`交割/永续`  
仅适用于`合约模式`和`跨币种保证金模式`  
  
**计划委托**

当市场价格到达触发价格时，系统将按预先设置的委托价格和数量自动下单。  
该委托不会预先占用仓位或保证金。  
仅适用于币币、交割和永续。 

了解更多 [计划委托](/cn/help/11015447687437)

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
triggerPx | String | 是 | 触发该策略订单的价格阈值，单位与该产品的 `px` 相同。具体使用哪种价格源取决于 `triggerPxType`（默认为最新成交价）。方向：做空止损单的触发价须低于 orderPx；做多止损单的触发价须高于 orderPx。方向违规将返回错误码 51046–51049。  
orderPx | String | 是 | 触发后提交的委托价格，与 `triggerPx`（决定何时激活）相互独立。设为 `-1` 表示触发后以市价委托；设置具体价格表示触发后以限价委托。  
advanceOrdType | String | 否 | 计划委托订单类型  
`fok`：全部成交或立即取消  
`ioc`：立即成交并取消剩余  
默认为 ""，限价或者市价（由 orderPx 控制）  
triggerPxType | String | 否 | 触发价格类型：  
`last`：任意成交价达到或超过 `triggerPx` 时触发——响应最快，但在流动性较差市场中易受短暂插针影响。  
`index`：基于多交易所合成指数触发——稳定，不受OKX自身插针影响。  
`mark`：基于OKX标记价格触发——经过平滑处理，抗插针能力强；衍生品推荐使用。  
现货产品仅支持 `last`。默认为 `last`。  
attachAlgoOrds | Array of objects | 否 | 附带止盈止损信息  
适用于`合约模式/跨币种保证金模式/组合保证金模式`  
> attachAlgoClOrdId | String | 否 | 下单附带止盈止损时，客户自定义的策略订单ID，字母（区分大小写）与数字的组合，可以是纯字母、纯数字且长度要在1-32位之间。  
订单完全成交，下止盈止损委托单时，该值会传给algoClOrdId。  
> tpTriggerPx | String | 否 | 止盈触发价，如果填写此参数，必须填写`止盈委托价`  
> tpTriggerRatio | String | 否 | 止盈触发比例，0.3 代表 30%   
仅适用于`交割`/`永续`合约   
`tpTriggerPx` 和 `tpTriggerRatio` 只能传入其中一个  
如果主单为买入订单，必须大于 0，如果主单为卖出订单，必须处于 -1 和 0 之间。  
> tpTriggerPxType | String | 否 | 止盈触发价类型  
`last`：最新价格  
`index`：指数价格  
`mark`：标记价格  
默认为`last`  
> tpOrdPx | String | 否 | 止盈委托价，如果填写此参数，必须填写`止盈触发价`  
委托价格为`-1`时，执行市价止盈  
> slTriggerPx | String | 否 | 止损触发价，如果填写此参数，必须填写`止损委托价`  
> slTriggerRatio | String | 否 | 止损触发比例，0.3 代表 30%   
仅适用于`交割`/`永续`合约   
`slTriggerPx` 和 `slTriggerRatio` 只能传入其中一个  
如果主单为买入订单，必须处于 0 和 1 之间，如果主单为卖出订单，必须大于 0。0 代表删除止损。  
> slTriggerPxType | String | 否 | 止损触发价类型  
`last`：最新价格  
`index`：指数价格  
`mark`：标记价格  
默认为`last`  
> slOrdPx | String | 否 | 止损委托价，如果填写此参数，必须填写`止损触发价`  
委托价格为`-1`时，执行市价止损  
> callbackRatio | String | 可选 | 回调幅度的比例，如 `0.05` 代表 5%。  
`callbackRatio` 和 `callbackSpread` 必须传入其中一个，且只能传入一个。  
仅适用于 `ordType` = `move_order_stop`  
> callbackSpread | String | 可选 | 回调幅度的价距。  
`callbackRatio` 和 `callbackSpread` 必须传入其中一个，且只能传入一个。  
仅适用于 `ordType` = `move_order_stop`  
> activePx | String | 否 | 激活价格。  
激活价格是移动止盈止损的激活条件，当市场最新成交价达到或超过激活价格，委托被激活。激活后系统开始计算止盈止损的实际触发价格。如果不填写激活价格，即下单后就被激活。  
仅适用于 `ordType` = `move_order_stop`  
  
**移动止盈止损**

移动止盈止损是一种跟踪市场价格的止盈止损，它的触发价格会跟随市场波动而变化，触发成功后会下市价单。  
实际触发价格的计算：卖出或开空时，实际触发价格 = 下单成功后最高价-回调幅度 (价距)，或下单成功后最高价 *(1-回调幅度 %) (比例)；买入或开多，实际触发价格 = 下单成功后最低价 + 回调幅度，或下单成功后最低价 *(1+ 回调幅度 %)。同时，您可以利用激活价格来设置委托被激活的价格。 

了解更多 [移动止盈止损](/cn/help/11015447687437)

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
callbackRatio | String | 可选 | 回调幅度的比例，如 "0.05"代表"5%"  
`callbackRatio`和`callbackSpread`只能传入一个  
callbackSpread | String | 可选 | 回调幅度的价距  
activePx | String | 否 | 激活价格  
激活价格是移动止盈止损的激活条件，当市场最新成交价达到或超过激活价格，委托被激活。激活后系统开始计算止盈止损的实际触发价格。如果不填写激活价格，即下单后就被激活。  
reduceOnly | Boolean | 否 | 是否只减仓，`true` 或 `false`，默认`false`  
该参数仅在 `交割/永续` 的买卖模式下有效，开平模式忽略此参数  
  
**时间加权**

时间加权是一种大额订单拆分后分时吃单的策略。  
用户在进行大额交易时，为避免对市场造成过大冲击，需要将大单委托自动拆为多笔委托。 

了解更多 [时间加权委托](/cn/help/xiii-time-weighted-average-price-twap)

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
pxVar | String | 可选 | 吃单价优于盘口的比例，取值范围在 [0.0001,0.01] 之间，如 "0.01"代表"1%"  
以买入为例，市价低于限制价时，策略开始用买一价向上取一定比例的委托价来委托小额买单。当前这个参数就用来确定向上的比例。  
`pxVar`和`pxSpread`只能传入一个  
pxSpread | String | 可选 | 吃单单价优于盘口的价距，取值范围不小于0（无上限）  
以买入为例，市价低于限制价时，策略开始用买一价向上取一定价距的委托价来委托小额买单。当前这个参数就用来确定向上的价距。  
szLimit | String | 是 | 单笔数量  
以买入为例，市价低于 “限制价” 时，策略开始用买一价向上取一定价距 / 比例的委托价来委托 “一定数量” 的买单。当前这个参数用来确定其中的 “一定数量”。  
pxLimit | String | 是 | 吃单限制价，取值范围不小于0（无上限）  
以买入为例，市价低于 “限制价” 时，策略开始用买一价向上取一定价距 / 比例的委托价来委托小额买单。当前这个参数就是其中的 “限制价”。  
timeInterval | String | 是 | 下单间隔，单位为秒。  
以买入为例，市价低于 “限制价” 时，策略开始按 “时间周期” 用买一价向上取一定价距 / 比例的委托价来委托小额买单。当前这个参数就是其中的 “时间周期”。  
  
**冰山委托**

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
szLimit | String | 是 | 单笔最小数量限制，仅适用于 `smart_iceberg`  
lmtOrderNumber | String | 是 | 限价拆单数量，仅适用于 `smart_iceberg`  
aggressiveness | String | 是 | 激进度，仅适用于 `smart_iceberg`  
`radical`：更快成交  
`mid`：较快成交，较优价格  
`conservative`：盘口排队  
pxLimit | String | 否 | 价格上限，仅适用于 `smart_iceberg`  
triggerParams | Array of objects | 否 | 触发参数，列表为空时默认立即触发，仅适用于 `smart_iceberg`  
> triggerAction | String | 是 | 触发行为  
`start`：启动冰山委托  
> triggerStrategy | String | 是 | 触发策略  
`instant`：立即触发  
`price`：价格触发  
`rsi`：RSI指标触发  
默认为 `instant`  
> triggerPx | String | 否 | 触发价格  
仅在 `triggerStrategy` 为 `price` 时有效  
> triggerCond | String | 否 | 触发条件  
`cross_up`：上穿  
`cross_down`：下穿  
`above`：上方  
`below`：下方  
`cross`：交叉  
仅在 `triggerStrategy` 为 `rsi` 时有效  
> timeframe | String | 否 | K线种类  
`3m`、`5m`、`15m`、`30m`（m代表分钟）  
`1H`、`4H`（H代表小时）  
`1D`（D代表天）  
仅在 `triggerStrategy` 为 `rsi` 时有效  
> thold | String | 否 | 阈值，取值 [1,100] 的整数  
仅在 `triggerStrategy` 为 `rsi` 时有效  
> timePeriod | String | 否 | RSI 计算周期，默认值为 `14`  
仅在 `triggerStrategy` 为 `rsi` 时有效  
  
> 返回结果
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
            {
                "algoId":"12345689",
                "clOrdId": "",
                "algoClOrdId": "",
                "sCode":"0",
                "sMsg":"",
                "tag":""
            }
        ]
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
algoId | String | 策略委托单ID  
clOrdId | String | ~~客户自定义订单ID~~ （已废弃）  
algoClOrdId | String | 客户自定义策略订单ID  
sCode | String | 事件执行结果的code，0代表成功  
sMsg | String | 事件执行失败时的msg  
tag | String | 订单标签