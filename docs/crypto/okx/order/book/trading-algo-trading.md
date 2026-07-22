---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#order-book-trading-algo-trading
anchor_id: order-book-trading-algo-trading
api_type: API
updated_at: 2026-07-22 19:19:14.033207
---

# Algo Trading

### POST / Place algo order  
  
The algo order includes `trigger` order, `oco` order, `chase` order, `conditional` order, `twap` order and trailing order.

#### Rate Limit: 20 requests per 2 seconds

#### Rate Limit of lead trader lead instruments for Copy Trading: 1 request per 2 seconds

#### Rate limit rule (except Options): User ID + Instrument ID

#### Rate limit rule (Options only): User ID + Instrument Family

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
  
### POST / Cancel algo order

Cancel unfilled algo orders. A maximum of 10 orders can be canceled per request. Request parameters should be passed in the form of an array.

#### Rate Limit: 20 orders per 2 seconds

#### Rate limit rule (except Options): User ID + Instrument ID

#### Rate limit rule (Options only): User ID + Instrument Family

#### HTTP Request

`POST /api/v5/trade/cancel-algos`

> Request Example
    
    
    POST /api/v5/trade/cancel-algos
    body
    [
        {
            "algoId":"590919993110396111",
            "instId":"BTC-USDT"
        },
        {
            "algoId":"590920138287841222",
            "instId":"BTC-USDT"
        }
    ]
    
    
    
    import okx.Trade as Trade
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # Production trading: 0, Demo trading: 1
    
    tradeAPI = Trade.TradeAPI(apikey, secretkey, passphrase, False, flag)
    
    # Cancel unfilled algo orders (not including Iceberg order, TWAP order, Trailing Stop order)
    algo_orders = [
        {"instId": "BTC-USDT", "algoId": "590919993110396111"},
        {"instId": "BTC-USDT", "algoId": "590920138287841222"}
    ]
    
    result = tradeAPI.cancel_algo_order(algo_orders)
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
instId | String | Yes | Instrument ID, e.g. `BTC-USDT`  
algoId | String | Conditional | Algo ID  
Either `algoId` or `algoClOrdId` is required. If both are passed, `algoId` will be used.  
algoClOrdId | String | Conditional | Client-supplied Algo ID  
Either `algoId` or `algoClOrdId` is required. If both are passed, `algoId` will be used.  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "algoClOrdId": "",
                "algoId": "1836489397437468672",
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
sCode | String | The code of the event execution result, `0` means success.  
sMsg | String | Rejection message if the request is unsuccessful.  
clOrdId | String | ~~Client Order ID as assigned by the client~~(Deprecated)  
algoClOrdId | String | ~~Client-supplied Algo ID~~(Deprecated)  
tag | String | ~~Order tag~~(Deprecated)  
  
### POST / Amend algo order

Amend unfilled algo orders (Support Stop order and Trigger order only, not including Move_order_stop order, Iceberg order, TWAP order, Trailing Stop order).  

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: User ID + Instrument ID

#### HTTP Request

`POST /api/v5/trade/amend-algos`

> Request Example
    
    
    POST /api/v5/trade/amend-algos
    body
    {
        "algoId":"2510789768709120",
        "newSz":"2",
        "instId":"BTC-USDT"
    }
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
instId | String | Yes | Instrument ID  
algoId | String | Conditional | Algo ID  
Either `algoId` or `algoClOrdId` is required. If both are passed, `algoId` will be used.  
algoClOrdId | String | Conditional | Client-supplied Algo ID  
Either `algoId` or `algoClOrdId` is required. If both are passed, `algoId` will be used.  
cxlOnFail | Boolean | No | Whether the order needs to be automatically canceled when the order amendment fails   
Valid options: `false` or `true`, the default is `false`.  
reqId | String | Conditional | Client Request ID as assigned by the client for order amendment   
A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters.   
The response will include the corresponding `reqId` to help you identify the request if you provide it in the request.  
newSz | String | Conditional | New quantity after amendment and it has to be larger than 0.  
  
**Take Profit / Stop Loss Order**

Parameter | Type | Required | Description  
---|---|---|---  
newTpTriggerPx | String | Conditional | Take-profit trigger price.   
Either the take-profit trigger price or order price is 0, it means that the take-profit is deleted  
newTpOrdPx | String | Conditional | Take-profit order price   
If the price is -1, take-profit will be executed at the market price.  
newSlTriggerPx | String | Conditional | Stop-loss trigger price.  
Either the stop-loss trigger price or order price is 0, it means that the stop-loss is deleted  
newSlOrdPx | String | Conditional | Stop-loss order price   
If the price is -1, stop-loss will be executed at the market price.  
newTpTriggerPxType | String | Conditional | Take-profit trigger price type  
`last`: last price   
`index`: index price   
`mark`: mark price  
newSlTriggerPxType | String | Conditional | Stop-loss trigger price type  
`last`: last price   
`index`: index price   
`mark`: mark price  
  
**Trigger Order**

Parameter | Type | Required | Description  
---|---|---|---  
newTriggerPx | String | Yes | New trigger price after amendment  
newOrdPx | String | Yes | New order price after amendment  
If the price is `-1`, the order will be executed at the market price.  
newTriggerPxType | String | No | New trigger price type after amendment   
`last`: last price  
`index`: index price  
`mark`: mark price   
The default is `last`  
attachAlgoOrds | Array of objects | No | Attached TP/SL or trailing stop order info  
Applicable to `Futures mode/Multi-currency margin/Portfolio margin`  
> newTpTriggerPx | String | No | Take-profit trigger price  
If you fill in this parameter, you should fill in the take-profit order price as well.  
> newTpTriggerRatio | String | No | Take profit trigger ratio, 0.3 represents 30%   
Only applicable to FUTURES and SWAP.   
Only one of `newTpTriggerPx` and `newTpTriggerRatio` can be passed   
If the main order is a buy order, it must be greater than 0, and if the main order is a sell order, it must be between -1 and 0.   
0 means to delete the take-profit.  
> newTpTriggerPxType | String | No | Take-profit trigger price type  
`last`: last price  
`index`: index price  
`mark`: mark price  
The default is `last`  
> newTpOrdPx | String | No | Take-profit order price  
If you fill in this parameter, you should fill in the take-profit trigger price as well.   
If the price is `-1`, take-profit will be executed at the market price.  
> newSlTriggerPx | String | No | Stop-loss trigger price  
If you fill in this parameter, you should fill in the stop-loss order price.  
> newSlTriggerRatio | String | No | Stop-loss trigger ratio, 0.3 represents 30%   
Only applicable to FUTURES and SWAP.   
Only one of `newSlTriggerPx` and `newSlTriggerRatio` can be passed   
If the main order is a buy order, it must be between 0 and 1, and if the main order is a sell order, it must be greater than 0.   
0 means to delete the stop-loss.  
> newSlTriggerPxType | String | No | Stop-loss trigger price type  
`last`: last price  
`index`: index price  
`mark`: mark price   
The default is `last`  
> newSlOrdPx | String | No | Stop-loss order price   
If you fill in this parameter, you should fill in the stop-loss trigger price.   
If the price is `-1`, stop-loss will be executed at the market price.  
> newCallbackRatio | String | Conditional | New callback ratio, e.g. `0.05` represents 5%.  
Either `newCallbackRatio` or `newCallbackSpread` can be passed. Only one can be passed.  
Only applicable when `ordType` = `move_order_stop`  
> newCallbackSpread | String | Conditional | New callback spread (price distance).  
Either `newCallbackRatio` or `newCallbackSpread` can be passed. Only one can be passed.  
Only applicable when `ordType` = `move_order_stop`  
> newActivePx | String | No | New activation price.  
Only applicable when `ordType` = `move_order_stop`  
  
> Response Example
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
            {
                "algoClOrdId":"algo_01",
                "algoId":"2510789768709120",
                "reqId":"po103ux",
                "sCode":"0",
                "sMsg":""
            }
        ]
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
algoId | String | Algo ID  
algoClOrdId | String | Client-supplied Algo ID  
reqId | String | Client Request ID as assigned by the client for order amendment.  
sCode | String | The code of the event execution result, `0` means success.  
sMsg | String | Rejection message if the request is unsuccessful.  
  
### GET / Algo order details

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: User ID

#### HTTP Request

`GET /api/v5/trade/order-algo`

> Request Example
    
    
    GET /api/v5/trade/order-algo?algoId=1753184812254216192
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
algoId | String | Conditional | Algo ID  
Either `algoId` or `algoClOrdId` is required.If both are passed, `algoId` will be used.  
algoClOrdId | String | Conditional | Client-supplied Algo ID  
A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters.  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "activePx": "",
                "actualPx": "",
                "actualSide": "",
                "actualSz": "0",
                "algoClOrdId": "",
                "algoId": "1753184812254216192",
                "amendPxOnTriggerType": "0",
                "attachAlgoOrds": [],
                "cTime": "1724751378980",
                "callbackRatio": "",
                "callbackSpread": "",
                "ccy": "",
                "chaseType": "",
                "chaseVal": "",
                "clOrdId": "",
                "closeFraction": "",
                "failCode": "0",
                "instId": "BTC-USDT",
                "instType": "SPOT",
                "isTradeBorrowMode": "",
                "last": "62916.5",
                "lever": "",
                "linkedOrd": {
                    "ordId": ""
                },
                "maxChaseType": "",
                "maxChaseVal": "",
                "moveTriggerPx": "",
                "ordId": "",
                "ordIdList": [],
                "ordPx": "",
                "ordType": "conditional",
                "posSide": "net",
                "pxLimit": "",
                "pxSpread": "",
                "pxVar": "",
                "quickMgnType": "",
                "reduceOnly": "false",
                "side": "buy",
                "slOrdPx": "",
                "slTriggerPx": "",
                "slTriggerPxType": "",
                "state": "live",
                "sz": "10",
                "szLimit": "",
                "tag": "",
                "tdMode": "cash",
                "tgtCcy": "quote_ccy",
                "timeInterval": "",
                "tpOrdPx": "-1",
                "tpTriggerPx": "10000",
                "tpTriggerPxType": "last",
                "triggerPx": "",
                "triggerPxType": "",
                "triggerTime": "",
                "tradeQuoteCcy": "USDT",
                "uTime": "1724751378980"
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
ordIdList | Array of strings | Order ID list. There will be multiple order IDs when there is TP/SL splitting order.  
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
`live`   
`pause`   
`partially_effective`  
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
advanceOrdType | String | Trigger order type  
`fok`: Fill-or-kill order  
`ioc`: Immediate-or-cancel order  
Default is "", limit or market (controlled by orderPx)  
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
algoClOrdId | String | Client-supplied Algo ID  
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
  
### GET / Algo order list

Retrieve a list of untriggered Algo orders under the current account.

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: User ID

#### HTTP Request

`GET /api/v5/trade/orders-algo-pending`

> Request Example
    
    
    GET /api/v5/trade/orders-algo-pending?ordType=conditional
    
    
    
    
    import okx.Trade as Trade
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # Production trading: 0, Demo trading: 1
    
    tradeAPI = Trade.TradeAPI(apikey, secretkey, passphrase, False, flag)
    
    # Retrieve a list of untriggered one-way stop orders
    result = tradeAPI.order_algos_list(
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
algoId | String | No | Algo ID  
instType | String | No | Instrument type  
`SPOT`  
`SWAP`  
`FUTURES`  
`MARGIN`  
instId | String | No | Instrument ID, e.g. `BTC-USDT`  
after | String | No | Pagination of data to return records earlier than the requested `algoId`.  
before | String | No | Pagination of data to return records newer than the requested `algoId`.  
limit | String | No | Number of results per request. The maximum is `100`. The default is `100`  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "activePx": "",
                "actualPx": "",
                "actualSide": "",
                "actualSz": "0",
                "algoClOrdId": "",
                "algoId": "1753184812254216192",
                "amendPxOnTriggerType": "0",
                "attachAlgoOrds": [],
                "cTime": "1724751378980",
                "callbackRatio": "",
                "callbackSpread": "",
                "ccy": "",
                "chaseType": "",
                "chaseVal": "",
                "clOrdId": "",
                "closeFraction": "",
                "failCode": "0",
                "instId": "BTC-USDT",
                "instType": "SPOT",
                "isTradeBorrowMode": "",
                "last": "62916.5",
                "lever": "",
                "linkedOrd": {
                    "ordId": ""
                },
                "maxChaseType": "",
                "maxChaseVal": "",
                "moveTriggerPx": "",
                "ordId": "",
                "ordIdList": [],
                "ordPx": "",
                "ordType": "conditional",
                "posSide": "net",
                "pxLimit": "",
                "pxSpread": "",
                "pxVar": "",
                "quickMgnType": "",
                "reduceOnly": "false",
                "side": "buy",
                "slOrdPx": "",
                "slTriggerPx": "",
                "slTriggerPxType": "",
                "state": "live",
                "sz": "10",
                "szLimit": "",
                "tag": "",
                "tdMode": "cash",
                "tgtCcy": "quote_ccy",
                "timeInterval": "",
                "tpOrdPx": "-1",
                "tpTriggerPx": "10000",
                "tpTriggerPxType": "last",
                "triggerPx": "",
                "triggerPxType": "",
                "triggerTime": "",
                "tradeQuoteCcy": "USDT",
                "uTime": "1724751378980"
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
ordIdList | Array of strings | Order ID list. There will be multiple order IDs when there is TP/SL splitting order.  
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
Only applicable to `SPOT` traded with Market order  
state | String | State  
`live`  
`pause`  
lever | String | Leverage, from `0.01` to `125`.   
Only applicable to `MARGIN/FUTURES/SWAP`  
tpTriggerPx | String | Take-profit trigger price  
tpTriggerPxType | String | Take-profit trigger price type.   
`last`: last price  
`index`: index price  
`mark`: mark price  
tpOrdPx | String | Take-profit order price  
slTriggerPx | String | Stop-loss trigger price  
slTriggerPxType | String | Stop-loss trigger price type.   
`last`: last price  
`index`: index price  
`mark`: mark price  
slOrdPx | String | Stop-loss order price  
triggerPx | String | Trigger price  
triggerPxType | String | Trigger price type.   
`last`: last price  
`index`: index price  
`mark`: mark price  
ordPx | String | Order price for the trigger order  
advanceOrdType | String | Trigger order type  
actualSz | String | Actual order quantity  
tag | String | Order tag  
actualPx | String | Actual order price  
actualSide | String | Actual trigger side  
`tp`: take profit `sl`: stop loss  
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
failCode | String | It represents that the reason that algo order fails to trigger. There will be value when the state is `order_failed`, e.g. 51008;  
For this endpoint, it always is "".  
algoClOrdId | String | Client-supplied Algo ID  
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
  
### GET / Algo order history

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
ordIdList | Array of strings | Order ID list. There will be multiple order IDs when there is TP/SL splitting order.  
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
advanceOrdType | String | Trigger order type  
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
  
### WS / Algo orders channel

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
  
### WS / Advance algo orders channel

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

# 策略交易

### POST / 策略委托下单   
  
提供单向止盈止损委托、双向止盈止损委托、追逐限价委托、计划委托、时间加权委托、移动止盈止损委托

#### 限速：20次/2s

#### 跟单交易带单员带单产品的限速：1次/2s

#### 限速规则（期权以外）：User ID + Instrument ID

#### 限速规则（只限期权）：User ID + Instrument Family

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
  
### POST / 撤销策略委托订单 

撤销策略委托订单，每次最多可以撤销10个策略委托单

#### 限速：20个/2s

#### 限速规则（期权以外）：User ID + Instrument ID

#### 限速规则（只限期权）：User ID + Instrument Family

#### HTTP请求

`POST /api/v5/trade/cancel-algos`

> 请求示例
    
    
    POST /api/v5/trade/cancel-algos
    body
    [
        {
            "algoId":"590919993110396111",
            "instId":"BTC-USDT"
        },
        {
            "algoId":"590920138287841222",
            "instId":"BTC-USDT"
        }
    ]
    
    
    
    
    import okx.Trade as Trade
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # 实盘: 0, 模拟盘: 1
    
    tradeAPI = Trade.TradeAPI(apikey, secretkey, passphrase, False, flag)
    
    # 支持止盈止损，计划委托 类型的策略撤单
    algo_orders = [
        {"instId": "BTC-USDT", "algoId": "590919993110396111"},
        {"instId": "BTC-USDT", "algoId": "590920138287841222"}
    ]
    
    result = tradeAPI.cancel_algo_order(algo_orders)
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
instId | String | 是 | 产品ID 如 `BTC-USDT`  
algoId | String | 可选 | 策略委托单ID  
`algoId`和`algoClOrdId`必须传一个，若传两个，以`algoId`为主  
algoClOrdId | String | 可选 | 客户自定义策略订单ID  
`algoId`和`algoClOrdId`必须传一个，若传两个，以`algoId`为主  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "algoClOrdId": "",
                "algoId": "1836489397437468672",
                "clOrdId": "",
                "sCode": "0",
                "sMsg": "",
                "tag": ""
            }
        ],
        "msg": ""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
algoId | String | 策略委托单ID  
sCode | String | 事件执行结果的code，0代表成功  
sMsg | String | 事件执行失败时的msg  
clOrdId | String | ~~客户自定义订单ID~~ （已废弃）  
algoClOrdId | String | ~~客户自定义策略订单ID~~ （已废弃）  
tag | String | ~~订单标签~~ （已废弃）  
  
### POST / 修改策略委托订单 

修改策略委托订单（仅支持止盈止损和计划委托订单，不包含、冰山委托、时间加权、移动止盈止损等订单）  

#### 限速：20次/2s

#### 限速规则：User ID + Instrument ID

#### HTTP请求

`POST /api/v5/trade/amend-algos`

> 请求示例
    
    
    POST /api/v5/trade/amend-algos
    body
    {
        "algoId":"2510789768709120",
        "newSz":"2",
        "instId":"BTC-USDT"
    }
    
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
instId | String | 是 | 产品ID  
algoId | String | 可选 | 策略委托单ID  
`algoId`和`algoClOrdId`必须传一个，若传两个，以`algoId`为主  
algoClOrdId | String | 可选 | 客户自定义策略订单ID  
`algoId`和`algoClOrdId`必须传一个，若传两个，以`algoId`为主  
cxlOnFail | Boolean | 否 | 当订单修改失败时，该订单是否需要自动撤销。默认为`false`  
`false`：不自动撤单  
`true`：自动撤单  
reqId | String | 否 | 用户自定义修改事件ID，字母（区分大小写）与数字的组合，可以是纯字母、纯数字且长度要在1-32位之间  
newSz | String | 可选 | 修改的新数量，必须大于0。  
  
**止盈止损**

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
newTpTriggerPx | String | 可选 | 止盈触发价  
如果止盈触发价或者委托价为0，那代表删除止盈  
newTpOrdPx | String | 可选 | 止盈委托价  
委托价格为-1时，执行市价止盈  
newSlTriggerPx | String | 可选 | 止损触发价  
如果止损触发价或者委托价为0，那代表删除止损  
newSlOrdPx | String | 可选 | 止损委托价  
委托价格为-1时，执行市价止损  
newTpTriggerPxType | String | 可选 | 止盈触发价类型  
`last`：最新价格  
`index`：指数价格  
`mark`：标记价格  
newSlTriggerPxType | String | 可选 | 止损触发价类型  
`last`：最新价格  
`index`：指数价格  
`mark`：标记价格  
  
**计划委托**

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
newTriggerPx | String | 是 | 修改后的触发价格  
newOrdPx | String | 是 | 修改后的委托价格   
委托价格为`-1`时，执行市价委托  
newTriggerPxType | String | 否 | 修改后的计划委托触发价格类型  
`last`：最新价格  
`index`：指数价格  
`mark`：标记价格  
默认为`last`  
attachAlgoOrds | Array of objects | 否 | 修改附带止盈止损或移动止盈止损订单信息  
适用于`合约模式/跨币种保证金模式/组合保证金模式`  
> newTpTriggerPx | String | 否 | 止盈触发价，如果填写此参数，必须填写`止盈委托价`  
> newTpTriggerRatio | String | 否 | 止盈触发比例，0.3 代表 30%   
仅适用于`交割`/`永续`合约  
`newTpTriggerPx` 和 `newTpTriggerRatio` 只能传入其中一个  
如果主单为买入订单，必须大于 0，如果主单为卖出订单，必须处于 -1 和 0 之间。0 代表删除止盈。  
> newTpTriggerPxType | String | 否 | 修改后的止盈触发价类型  
`last`：最新价格  
`index`：指数价格  
`mark`：标记价格  
默认为`last`  
> newTpOrdPx | String | 否 | 止盈委托价，如果填写此参数，必须填写`止盈触发价`  
委托价格为`-1`时，执行市价止盈  
> newSlTriggerPx | String | 否 | 止损触发价，如果填写此参数，必须填写`止损委托价`  
> newSlTriggerRatio | String | 否 | 止损触发比例，0.3 代表 30%   
仅适用于`交割`/`永续`合约  
`newSlTriggerPx` 和 `newSlTriggerRatio` 只能传入其中一个  
如果主单为买入订单，必须处于 0 和 1 之间，如果主单为卖出订单，必须大于 0。0 代表删除止损。  
> newSlTriggerPxType | String | 否 | 止损触发价类型  
`last`：最新价格  
`index`：指数价格  
`mark`：标记价格  
默认为`last`  
> newSlOrdPx | String | 否 | 止损委托价，如果填写此参数，必须填写`止损触发价`  
委托价格为`-1`时，执行市价止损  
> newCallbackRatio | String | 可选 | 新的回调幅度比例，如 `0.05` 代表 5%。  
`newCallbackRatio` 和 `newCallbackSpread` 只能传入其中一个。  
仅适用于 `ordType` = `move_order_stop`  
> newCallbackSpread | String | 可选 | 新的回调幅度价距。  
`newCallbackRatio` 和 `newCallbackSpread` 只能传入其中一个。  
仅适用于 `ordType` = `move_order_stop`  
> newActivePx | String | 否 | 新的激活价格。  
仅适用于 `ordType` = `move_order_stop`  
  
> 返回结果
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
            {
                "algoClOrdId":"algo_01",
                "algoId":"2510789768709120",
                "reqId":"po103ux",
                "sCode":"0",
                "sMsg":""
            }
        ]
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
algoId | String | 订单ID  
algoClOrdId | String | 客户自定义策略订单ID  
reqId | String | 用户自定义修改事件ID，字母（区分大小写）与数字的组合，可以是纯字母、纯数字且长度要在1-32位之间  
sCode | String | 事件执行结果的code，0代表成功  
sMsg | String | 事件执行失败时的msg  
  
### GET / 获取策略委托单信息 

#### 限速：20次/2s

#### 限速规则：User ID

#### HTTP请求

`GET /api/v5/trade/order-algo`

> 请求示例
    
    
    GET /api/v5/trade/order-algo?algoId=1753184812254216192
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
algoId | String | 可选 | 策略委托单ID  
`algoId`和`algoClOrdId`必须传一个，若传两个，以`algoId`为主  
algoClOrdId | String | 可选 | 客户自定义策略订单ID  
字母（区分大小写）与数字的组合，可以是纯字母、纯数字且长度要在1-32位之间。  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "activePx": "",
                "actualPx": "",
                "actualSide": "",
                "actualSz": "0",
                "algoClOrdId": "",
                "algoId": "1753184812254216192",
                "amendPxOnTriggerType": "0",
                "attachAlgoOrds": [],
                "cTime": "1724751378980",
                "callbackRatio": "",
                "callbackSpread": "",
                "ccy": "",
                "chaseType": "",
                "chaseVal": "",
                "clOrdId": "",
                "closeFraction": "",
                "failCode": "0",
                "instId": "BTC-USDT",
                "instType": "SPOT",
                "isTradeBorrowMode": "",
                "last": "62916.5",
                "lever": "",
                "linkedOrd": {
                    "ordId": ""
                },
                "maxChaseType": "",
                "maxChaseVal": "",
                "moveTriggerPx": "",
                "ordId": "",
                "ordIdList": [],
                "ordPx": "",
                "ordType": "conditional",
                "posSide": "net",
                "pxLimit": "",
                "pxSpread": "",
                "pxVar": "",
                "quickMgnType": "",
                "reduceOnly": "false",
                "side": "buy",
                "slOrdPx": "",
                "slTriggerPx": "",
                "slTriggerPxType": "",
                "state": "live",
                "sz": "10",
                "szLimit": "",
                "tag": "",
                "tdMode": "cash",
                "tgtCcy": "quote_ccy",
                "timeInterval": "",
                "tpOrdPx": "-1",
                "tpTriggerPx": "10000",
                "tpTriggerPxType": "last",
                "triggerPx": "",
                "triggerPxType": "",
                "triggerTime": "",
                "tradeQuoteCcy": "USDT",
                "uTime": "1724751378980"
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
ordIdList | Array of strings | 订单ID列表，当止盈止损存在市价拆单时，会有多个。  
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
`live`：待生效  
`pause`：暂停生效   
`partially_effective`:部分生效  
`effective`：已生效  
`canceled`：已撤销   
`order_failed`：委托失败   
`partially_failed`：部分委托失败  
lever | String | 杠杆倍数，0.01到125之间的数值，仅适用于 `币币杠杆/交割/永续`  
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
triggerPxType | String | 计划委托触发价格类型  
`last`：最新价格  
`index`：指数价格  
`mark`：标记价格  
ordPx | String | 计划委托单的委托价格  
advanceOrdType | String | 计划委托订单类型  
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
amendPxOnTriggerType | String | 是否启用开仓价止损  
仅适用于分批止盈的止损订单  
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
  
### GET / 获取未完成策略委托单列表 

获取当前账户下未触发的策略委托单列表

#### 限速：20次/2s

#### 限速规则：User ID

#### HTTP请求

`GET /api/v5/trade/orders-algo-pending`

> 请求示例
    
    
    GET /api/v5/trade/orders-algo-pending?ordType=conditional
    
    
    
    
    import okx.Trade as Trade
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # 实盘: 0, 模拟盘: 1
    
    tradeAPI = Trade.TradeAPI(apikey, secretkey, passphrase, False, flag)
    
    # 查询所有未触发的单向止盈止损策略订单
    result = tradeAPI.order_algos_list(
        ordType="conditional"
    )
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
algoId | String | 否 | 策略委托单ID  
instType | String | 否 | 产品类型  
`SPOT`：币币  
`SWAP`：永续合约  
`FUTURES`：交割合约  
`MARGIN`：杠杆  
instId | String | 否 | 产品ID，如 `BTC-USDT`  
ordType | String | 是 | 订单类型  
`conditional`：单向止盈止损  
`oco`：双向止盈止损   
`chase`: 追逐限价委托，仅适用于交割和永续  
`trigger`：计划委托  
`move_order_stop`：移动止盈止损  
`twap`：时间加权委托  
`smart_iceberg`：冰山委托  
支持 `conditional` 和 `oco` 同时查询，半角逗号分隔，对于其他类型，一次请求仅支持查询一个  
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
                "actualSide": "",
                "actualSz": "0",
                "algoClOrdId": "",
                "algoId": "1753184812254216192",
                "amendPxOnTriggerType": "0",
                "attachAlgoOrds": [],
                "cTime": "1724751378980",
                "callbackRatio": "",
                "callbackSpread": "",
                "ccy": "",
                "chaseType": "",
                "chaseVal": "",
                "clOrdId": "",
                "closeFraction": "",
                "failCode": "0",
                "instId": "BTC-USDT",
                "instType": "SPOT",
                "isTradeBorrowMode": "",
                "last": "62916.5",
                "lever": "",
                "linkedOrd": {
                    "ordId": ""
                },
                "maxChaseType": "",
                "maxChaseVal": "",
                "moveTriggerPx": "",
                "ordId": "",
                "ordIdList": [],
                "ordPx": "",
                "ordType": "conditional",
                "posSide": "net",
                "pxLimit": "",
                "pxSpread": "",
                "pxVar": "",
                "quickMgnType": "",
                "reduceOnly": "false",
                "side": "buy",
                "slOrdPx": "",
                "slTriggerPx": "",
                "slTriggerPxType": "",
                "state": "live",
                "sz": "10",
                "szLimit": "",
                "tag": "",
                "tdMode": "cash",
                "tgtCcy": "quote_ccy",
                "timeInterval": "",
                "tpOrdPx": "-1",
                "tpTriggerPx": "10000",
                "tpTriggerPxType": "last",
                "triggerPx": "",
                "triggerPxType": "",
                "triggerTime": "",
                ”tradeQuoteCcy“: "USDT",
                "uTime": "1724751378980"
            }
        ],
        "msg": ""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
instType | String | 产品类型  
instId | String | 产品ID  
ccy | String | 保证金币种，适用于`逐仓杠杆`及`合约模式`下的`全仓杠杆`订单  
ordId | String | 最新一笔订单ID，即将废弃。  
ordIdList | Array of strings | 订单ID列表，当止盈止损存在市价拆单时，会有多个。  
algoId | String | 策略委托单ID  
clOrdId | String | 客户自定义订单ID  
sz | String | 委托数量  
closeFraction | String | 策略委托触发时，平仓的百分比。1 代表100%  
ordType | String | 订单类型  
side | String | 订单方向  
posSide | String | 持仓方向  
tdMode | String | 交易模式  
tgtCcy | String | 币币市价单委托数量`sz`的单位  
`base_ccy`：交易货币  
`quote_ccy`：计价货币  
仅适用于`币币`市价订单  
默认买单为`quote_ccy`，卖单为`base_ccy`  
state | String | 订单状态  
`live`：待生效  
`pause`：暂停生效  
lever | String | 杠杆倍数，0.01到125之间的数值  
仅适用于 `币币杠杆`/`交割`/`永续`  
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
triggerPxType | String | 计划委托触发价类型  
`last`：最新价格  
`index`：指数价格  
`mark`：标记价格  
ordPx | String | 计划委托单的委托价格  
advanceOrdType | String | 计划委托订单类型  
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
tag | String | 订单标签  
pxLimit | String | 挂单限制价，仅适用于`时间加权委托`  
价格上限，仅适用于`冰山委托`  
lmtOrderNumber | String | 限价拆单数量  
仅适用于 `冰山委托`  
aggressiveness | String | 激进度  
`radical`：更快成交  
`mid`：较快成交，较优价格  
`conservative`：盘口排队  
仅适用于 `冰山委托`  
triggerParams | Array of objects | 触发参数  
仅适用于 `冰山委托`  
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
`true` 或 `false`  
quickMgnType | String | ~~一键借币类型，仅适用于杠杆逐仓的一键借币模式  
`manual`：手动，`auto_borrow`：自动借币，`auto_repay`：自动还币~~（已弃用）  
last | String | 下单时的最新成交价  
failCode | String | 代表策略触发失败的原因，委托失败时有值，如 51008，对于该接口一直为""。  
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
  
### GET / 获取历史策略委托单列表 

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
ordIdList | Array of strings | 订单ID列表，当止盈止损存在市价拆单时，会有多个。  
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
advanceOrdType | String | 计划委托订单类型  
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
  
### WS / 策略委托订单频道 

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
  
### WS / 高级策略委托订单频道 

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