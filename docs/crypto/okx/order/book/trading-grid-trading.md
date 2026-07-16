---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#order-book-trading-grid-trading
anchor_id: order-book-trading-grid-trading
api_type: API
updated_at: 2026-07-16 19:19:55.166744
---

# Grid Trading

Grid trading works by the simple strategy of buy low and sell high. After you set the parameters, the system automatically places orders at incrementally increasing or decreasing prices. Overall, the grid bot seeks to capitalize on normal price volatility by placing buy and sell orders at certain regular intervals above and below a predefined base price.  
The API endpoints of `Grid Trading` require authentication.  
  
### POST / Place grid algo order

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: User ID + Instrument ID

#### HTTP Request

`POST /api/v5/tradingBot/grid/order-algo`

> Request Example
    
    
    # Place spot grid algo order
    POST /api/v5/tradingBot/grid/order-algo
    body
    {
        "instId": "BTC-USDT",
        "algoOrdType": "grid",
        "maxPx": "5000",
        "minPx": "400",
        "gridNum": "10",
        "runType": "1",
        "quoteSz": "25",
        "triggerParams":[
          {
             "triggerAction":"stop",
             "triggerStrategy":"price",  
             "triggerPx":"1000"
          }
        ]
    }
    
    # Place contract grid algo order
    POST /api/v5/tradingBot/grid/order-algo
    body
    {
        "instId": "BTC-USDT-SWAP",
        "algoOrdType": "contract_grid",
        "maxPx": "5000",
        "minPx": "400",
        "gridNum": "10",
        "runType": "1",
        "sz": "200", 
        "direction": "long",
        "lever": "2",
        "triggerParams":[
          {
             "triggerAction":"start", 
             "triggerStrategy":"rsi", 
             "timeframe":"30m",
             "thold":"10",
             "triggerCond":"cross",
             "timePeriod":"14"
          },
          {
             "triggerAction":"stop",
             "triggerStrategy":"price",
             "triggerPx":"1000",
             "stopType":"2"
          }
       ]
    }
    
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
instId | String | Yes | Instrument ID, e.g. `BTC-USDT-SWAP`  
algoOrdType | String | Yes | Algo order type  
`grid`: Spot grid  
`contract_grid`: Contract grid  
maxPx | String | Yes | Upper price of price range  
minPx | String | Yes | Lower price of price range  
gridNum | String | Yes | Grid quantity  
runType | String | No | Grid type  
`1`: Arithmetic, `2`: Geometric  
Default is Arithmetic  
tpTriggerPx | String | No | TP tigger price  
Applicable to `Spot grid`/`Contract grid`  
slTriggerPx | String | No | SL tigger price  
Applicable to `Spot grid`/`Contract grid`  
algoClOrdId | String | No | Client-supplied Algo ID  
A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters.  
tag | String | No | Order tag  
profitSharingRatio | String | No | Profit sharing ratio, it only supports these values  
`0`,`0.1`,`0.2`,`0.3`  
0.1 represents 10%  
triggerParams | Array of objects | No | Trigger Parameters  
Applicable to `Spot grid`/`Contract grid`  
> triggerAction | String | Yes | Trigger action  
`start`  
`stop`  
> triggerStrategy | String | Yes | Trigger strategy  
`instant`  
`price`  
`rsi`  
Default is `instant`  
> delaySeconds | String | No | Delay seconds after action triggered  
> timeframe | String | No | K-line type  
`3m`, `5m`, `15m`, `30m` (`m`: minute)  
`1H`, `4H` (`H`: hour)  
`1D` (`D`: day)  
This field is only valid when `triggerStrategy` is `rsi`  
> thold | String | No | Threshold  
The value should be an integer between 1 to 100  
This field is only valid when `triggerStrategy` is `rsi`  
> triggerCond | String | No | Trigger condition  
`cross_up`  
`cross_down`  
`above`  
`below`  
`cross`  
This field is only valid when `triggerStrategy` is `rsi`  
> timePeriod | String | No | Time Period  
`14`  
This field is only valid when `triggerStrategy` is `rsi`  
> triggerPx | String | No | Trigger Price  
This field is only valid when `triggerStrategy` is `price`  
> stopType | String | No | Stop type  
Spot grid `1`: Sell base currency `2`: Keep base currency  
Contract grid `1`: Market Close All positions `2`: Keep positions  
This field is only valid when `triggerAction` is `stop`  
  
Spot Grid Order

Parameter | Type | Required | Description  
---|---|---|---  
quoteSz | String | Conditional | Invest amount for quote currency  
Either `quoteSz` or `baseSz` is required  
baseSz | String | Conditional | Invest amount for base currency  
Either `quoteSz` or `baseSz` is required  
tradeQuoteCcy | String | No | The quote currency for trading. Only applicable to SPOT.  
The default value is the quote currency of instId, e.g. USD for BTC-USD.  
  
Contract Grid Order

Parameter | Type | Required | Description  
---|---|---|---  
sz | String | Yes | Used margin based on `USDT`  
direction | String | Yes | Contract grid type  
`long`,`short`,`neutral`  
lever | String | Yes | Leverage  
basePos | Boolean | No | Whether or not open a position when the strategy activates   
Default is `false`  
Neutral contract grid should omit the parameter  
tpRatio | String | No | Take profit ratio, 0.1 represents 10%  
slRatio | String | No | Stop loss ratio, 0.1 represents 10%  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "algoClOrdId": "",
                "algoId": "447053782921515008",
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
algoClOrdId | String | Client-supplied Algo ID  
sCode | String | The code of the event execution result, `0` means success.  
sMsg | String | Rejection message if the request is unsuccessful.  
tag | String | Order tag  
  
### POST / Amend grid algo order basic param

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: User ID

#### HTTP Request

`POST /api/v5/tradingBot/grid/amend-algo-basic-param`

> Request Example
    
    
    POST /api/v5/tradingBot/grid/amend-algo-basic-param
    body
        {
          "algoId": "448965992920907776",
          "maxPx": "100",
          "minPx": "10",
          "gridNum": "5"
          "topupAmount": "123.45"
        }
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
algoId | String | Yes | Algo ID  
minPx | String | Yes | Minimum price range  
maxPx | String | Yes | Maximum price range  
gridNum | String | Yes | Grid quantity  
topupAmount | String | No | Contract grid only. Optional client-supplied top up investment amount. If this is not supplied or explicitly supplied as "0", the required top up investment amount to edit grid parameters is topped up by default  
  
> Response Example
    
    
    {
        "code": "55186",
        "msg": "Due to market fluctuations, your investment amount is too large to apply these modifications.",
        "data": [
            {
                "algoId": "4283223775520665600",
                "maxTopupAmount": "12456.78",
                "requiredTopupAmount": "12.34"
            }
        ]
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
algoId | String | Algo ID  
requiredTopupAmount | String | Required top up investment amount to edit grid parameters.  
maxTopupAmount | String | Contract grid only. Max top up investment amount to edit grid parameters  
  
#### Error Code

**Error Code** | **HTTP Status code** | **Error Message**  
---|---|---  
51000 | 400 | Parameter {param} error. This would also be returned when a grid bot does not support the parameter  
51346 | 400 | Upper limit must be greater than the lower limit price.  
55123 | 400 | There is insufficient balance for transfer.  
55124 | 200 | Due to market fluctuations, your investment amount is insufficient to apply these modifications.  
55186 | 200 | Due to market fluctuations, your investment amount is too large to apply these modifications.  
  
### POST / Amend grid algo order

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: User ID

#### HTTP Request

`POST /api/v5/tradingBot/grid/amend-order-algo`

> Request Example
    
    
    POST /api/v5/tradingBot/grid/amend-order-algo
    body
    {
        "algoId":"448965992920907776",
        "instId":"BTC-USDT-SWAP",
        "slTriggerPx":"1200",
        "tpTriggerPx":""
    }
    
    POST /api/v5/tradingBot/grid/amend-order-algo
    body 
    {
       "algoId":"578963447615062016",
       "instId":"BTC-USDT",
       "triggerParams":[
           {
               "triggerAction":"stop",  
               "triggerStrategy":"price",   
               "triggerPx":"1000"
           }
       ]
    }
    
    POST /api/v5/tradingBot/grid/amend-order-algo
    body 
    {
       "algoId":"578963447615062016",
       "instId":"BTC-USDT-SWAP",
       "triggerParams":[
           {
               "triggerAction":"stop",  
               "triggerStrategy":"instant",   
               "stopType":"1"
           }
       ]
    }
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
algoId | String | Yes | Algo ID  
instId | String | Yes | Instrument ID, e.g. `BTC-USDT-SWAP`  
slTriggerPx | String | No | New stop-loss trigger price  
if slTriggerPx is set "" means stop-loss trigger price is canceled.  
Either `slTriggerPx` or `tpTriggerPx` is required.  
tpTriggerPx | String | No | New take-profit trigger price  
if tpTriggerPx is set "" means take-profit trigger price is canceled.  
tpRatio | String | No | Take profit ratio, 0.1 represents 10%, only applicable to contract grid  
if it is set "" means take-profit ratio is canceled.  
slRatio | String | No | Stop loss ratio, 0.1 represents 10%, only applicable to contract grid`  
if it is set "" means stop-loss ratio is canceled.  
topUpAmt | String | No | Top up amount, only applicable to spot grid  
triggerParams | Array of objects | No | Trigger Parameters  
> triggerAction | String | Yes | Trigger action  
`start`  
`stop`  
> triggerStrategy | String | Yes | Trigger strategy  
`instant`  
`price`  
`rsi`  
> triggerPx | String | No | Trigger Price  
This field is only valid when `triggerStrategy` is `price`  
> stopType | String | No | Stop type  
Spot grid `1`: Sell base currency `2`: Keep base currency  
Contract grid `1`: Market Close All positions `2`: Keep positions  
This field is only valid when `triggerAction` is `stop`  
  
> Response Example
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
            {
                "algoClOrdId": "",
                "algoId":"448965992920907776",
                "sCode":"0",
                "sMsg":"",
                "tag": ""
            }
        ]
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
algoId | String | Algo ID  
algoClOrdId | String | Client-supplied Algo ID  
sCode | String | The code of the event execution result, `0` means success.  
sMsg | String | Rejection message if the request is unsuccessful.  
tag | String | Order tag  
  
### POST / Stop grid algo order

A maximum of 10 orders can be stopped per request.

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: User ID

#### HTTP Request

`POST /api/v5/tradingBot/grid/stop-order-algo`

> Request Example
    
    
    POST /api/v5/tradingBot/grid/stop-order-algo
    body
    [
        {
            "algoId":"448965992920907776",
            "instId":"BTC-USDT",
            "stopType":"1",
            "algoOrdType":"grid"
        }
    ]
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
algoId | String | Yes | Algo ID  
instId | String | Yes | Instrument ID, e.g. `BTC-USDT`  
algoOrdType | String | Yes | Algo order type  
`grid`: Spot grid  
`contract_grid`: Contract grid  
stopType | String | Yes | Stop type  
Spot grid `1`: Sell base currency `2`: Keep base currency  
Contract grid `1`: Market Close All positions `2`: Keep positions  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "algoClOrdId": "",
                "algoId": "448965992920907776",
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
algoClOrdId | String | Client-supplied Algo ID  
sCode | String | The code of the event execution result, `0` means success.  
sMsg | String | Rejection message if the request is unsuccessful.  
tag | String | Order tag  
  
### POST / Close position for contract grid

Close position when the contract grid stop type is 'keep position'.

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: User ID

#### HTTP Request

`POST /api/v5/tradingBot/grid/close-position`

> Request Example
    
    
    POST /api/v5/tradingBot/grid/close-position
    body
    {
        "algoId":"448965992920907776",
        "mktClose":true
    }
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
algoId | String | Yes | Algo ID  
mktClose | Boolean | Yes | Market close all the positions or not  
`true`: Market close all position, `false`: Close part of position  
sz | String | Conditional | Close position amount, with unit of `contract`  
If `mktClose` is `false`, the parameter is required.  
px | String | Conditional | Close position price  
If `mktClose` is `false`, the parameter is required.  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "algoClOrdId": "",
                "algoId": "448965992920907776",
                "ordId": "",
                "tag": ""
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
algoId | String | Algo ID  
ordId | String | Close position order ID  
If `mktClose` is `true`, the parameter will return "".  
algoClOrdId | String | Client-supplied Algo ID  
tag | String | Order tag  
  
### POST / Cancel close position order for contract grid

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: User ID

#### HTTP Request

`POST /api/v5/tradingBot/grid/cancel-close-order`

> Request Example
    
    
    POST /api/v5/tradingBot/grid/cancel-close-order
    body
    {
        "algoId":"448965992920907776",
        "ordId":"570627699870375936"
    }
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
algoId | String | Yes | Algo ID  
ordId | String | Yes | Close position order ID  
  
> Response Example
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
            {
                "algoClOrdId": "",
                "algoId": "448965992920907776",
                "ordId": "570627699870375936",
                "tag": ""
            }
        ]
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
algoId | String | Algo ID  
ordId | String | Close position order ID  
algoClOrdId | String | Client-supplied Algo ID  
tag | String | Order tag  
  
### POST / Instant trigger grid algo order

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: User ID + Instrument ID

#### HTTP Request

`POST /api/v5/tradingBot/grid/order-instant-trigger`

> Request Example
    
    
    POST /api/v5/tradingBot/grid/order-instant-trigger
    body
    {
        "algoId":"561564133246894080"
    }
    
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
algoId | String | Yes | Algo ID  
topUpAmt | String | No | Top up amount, only applicable to spot grid  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "algoClOrdId": "",
                "algoId": "561564133246894080"
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
algoId | String | Algo ID  
algoClOrdId | String | Client-supplied Algo ID  
  
### GET / Grid algo order list

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: User ID

#### HTTP Request

`GET /api/v5/tradingBot/grid/orders-algo-pending`

> Request Example
    
    
    GET /api/v5/tradingBot/grid/orders-algo-pending?algoOrdType=grid
    

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
limit | String | No | Number of results per request. The maximum is 100. The default is 100  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "actualLever": "",
                "algoClOrdId": "",
                "algoId": "56802********64032",
                "algoOrdType": "grid",
                "arbitrageNum": "0",
                "availEq": "",
                "basePos": false,
                "baseSz": "0",
                "cTime": "1681700496249",
                "cancelType": "0",
                "direction": "",
                "floatProfit": "0",
                "gridNum": "10",
                "gridProfit": "0",
                "instFamily": "",
                "instId": "BTC-USDT",
                "instType": "SPOT",
                "investment": "25",
                "lever": "",
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
                "slTriggerPx": "",
                "state": "running",
                "stopType": "",
                "sz": "",
                "tag": "",
                "totalPnl": "0",
                "tpTriggerPx": "",
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
                        "triggerTime": ""
                    }
                ],
                "uTime": "1682062564350",
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
`starting`  
`running`  
`stopping`  
`pending_signal`  
`no_close_position`: stopped algo order but have not closed position yet  
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
Spot `1`: Sell base currency `2`: Keep base currency  
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
tradeQuoteCcy | String | The quote currency for trading.  
  
### GET / Grid algo order history

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
  
### GET / Grid algo order details

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: User ID

#### HTTP Request

`GET /api/v5/tradingBot/grid/orders-algo-details`

> Request Example
    
    
    GET /api/v5/tradingBot/grid/orders-algo-details?algoId=448965992920907776&algoOrdType=grid
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
algoOrdType | String | Yes | Algo order type  
`grid`: Spot grid  
`contract_grid`: Contract grid  
algoId | String | Yes | Algo ID  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "actualLever": "",
                "activeOrdNum": "0",
                "algoClOrdId": "",
                "algoId": "448965992920907776",
                "algoOrdType": "grid",
                "annualizedRate": "0",
                "arbitrageNum": "0",
                "availEq": "",
                "basePos": false,
                "baseSz": "0",
                "cTime": "1681181054927",
                "cancelType": "1",
                "curBaseSz": "0",
                "curQuoteSz": "0",
                "direction": "",
                "eq": "",
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
                "perMaxProfitRate": "1.14570215",
                "perMinProfitRate": "0.0991200440528634356837",
                "pnlRatio": "0",
                "profit": "0.00000000",
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
                "runPx": "30089.7",
                "singleAmt": "0.00101214",
                "slTriggerPx": "0",
                "state": "stopped",
                "stopResult": "0",
                "stopType": "1",
                "sz": "",
                "tag": "",
                "totalAnnualizedRate": "0",
                "totalPnl": "0",
                "tpTriggerPx": "0",
                "tradeNum": "0",
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
                        "triggerType": "manual",
                        "triggerTime": "1681181186484"
                    }
                ],
                "uTime": "1681181186496",
                "uly": "",
                "profitSharingRatio": "",
                "copyType": "0",
                "tpRatio": "",
                "slRatio": "",
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
`starting`  
`running`  
`stopping`  
`no_close_position`: stopped algo order but have not closed position yet  
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
tradeNum | String | The number of trades executed  
arbitrageNum | String | The number of arbitrages executed  
singleAmt | String | Amount per grid  
perMinProfitRate | String | Estimated minimum Profit margin per grid  
perMaxProfitRate | String | Estimated maximum Profit margin per grid  
runPx | String | Price at launch  
totalPnl | String | Total P&L  
pnlRatio | String | P&L ratio  
investment | String | Accumulated investment amount  
Spot grid investment amount calculated on quote currency  
gridProfit | String | Grid profit  
floatProfit | String | Variable P&L  
totalAnnualizedRate | String | Total annualized rate  
annualizedRate | String | Grid annualized rate  
cancelType | String | Algo order stop reason  
`0`: None  
`1`: Manual stop  
`2`: Take profit  
`3`: Stop loss  
`4`: Risk control  
`5`: Delivery  
`6`: Signal  
stopType | String | Stop type  
Spot grid `1`: Sell base currency `2`: Keep base currency  
Contract grid `1`: Market Close All positions `2`: Keep positions  
activeOrdNum | String | Total count of pending sub orders  
quoteSz | String | Quote currency investment amount  
Only applicable to `Spot grid`  
baseSz | String | Base currency investment amount  
Only applicable to `Spot grid`  
curQuoteSz | String | Assets of quote currency currently held  
Only applicable to `Spot grid`  
curBaseSz | String | Assets of base currency currently held  
Only applicable to `Spot grid`  
profit | String | Current available profit based on quote currency  
Only applicable to `Spot grid`  
stopResult | String | Stop result  
`0`: default, `1`: Successful selling of currency at market price, `-1`: Failed to sell currency at market price  
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
eq | String | Total equity of strategy account  
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
tpRatio | String | Take profit ratio, 0.1 represents 10%  
slRatio | String | Stop loss ratio, 0.1 represents 10%  
fee | String | Accumulated fee. Only applicable to contract grid, or it will be ""  
feeCcy | String | Accumulated fee currency. Only applicable to contract grid, or it will be ""  
fundingFee | String | Accumulated funding fee. Only applicable to contract grid, or it will be ""  
tradeQuoteCcy | String | The quote currency for trading.  
  
### GET / Grid algo sub orders

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: User ID

#### HTTP Request

`GET /api/v5/tradingBot/grid/sub-orders`

> Request Example
    
    
    GET /api/v5/tradingBot/grid/sub-orders?algoId=123456&type=live&algoOrdType=grid
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
algoOrdType | String | Yes | Algo order type  
`grid`: Spot grid  
`contract_grid`: Contract grid  
algoId | String | Yes | Algo ID  
type | String | Yes | Sub order state  
`live`  
`filled`  
groupId | String | No | Group ID  
after | String | No | Pagination of data to return records earlier than the requested `ordId`.  
before | String | No | Pagination of data to return records newer than the requested `ordId`.  
limit | String | No | Number of results per request. The maximum is 100. The default is 100  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "accFillSz": "0",
                "algoClOrdId": "",
                "algoId": "448965992920907776",
                "algoOrdType": "grid",
                "avgPx": "0",
                "cTime": "1653347949771",
                "ccy": "",
                "ctVal": "",
                "fee": "0",
                "feeCcy": "USDC",
                "groupId": "3",
                "instId": "BTC-USDC",
                "instType": "SPOT",
                "lever": "0",
                "ordId": "449109084439187456",
                "ordType": "limit",
                "pnl": "0",
                "posSide": "net",
                "px": "30404.3",
                "rebate": "0",
                "rebateCcy": "USDT",
                "side": "sell",
                "state": "live",    
                "sz": "0.00059213",
                "tag": "",
                "tdMode": "cash",
                "uTime": "1653347949831"
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
algoOrdType | String | Algo order type  
`grid`: Spot grid  
`contract_grid`: Contract grid  
groupId | String | Group ID  
ordId | String | Sub order ID  
cTime | String | Sub order created time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
uTime | String | Sub order updated time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
tdMode | String | Sub order trade mode  
Margin mode: `cross`/`isolated`  
Non-Margin mode: `cash`  
ccy | String | Margin currency  
Only applicable to cross MARGIN orders in `Futures mode`.  
ordType | String | Sub order type  
`market`: Market order  
`limit`: Limit order  
`ioc`: Immediate-or-cancel order  
sz | String | Sub order quantity to buy or sell  
state | String | Sub order state  
`canceled`  
`live`  
`partially_filled`  
`filled`  
`cancelling`  
side | String | Sub order side  
`buy` `sell`  
px | String | Sub order price  
fee | String | Sub order fee amount  
feeCcy | String | Sub order fee currency  
rebate | String | Sub order rebate amount  
rebateCcy | String | Sub order rebate currency  
avgPx | String | Sub order average filled price  
accFillSz | String | Sub order accumulated fill quantity  
posSide | String | Sub order position side  
`net`  
pnl | String | Sub order profit and loss  
ctVal | String | Contract value  
Only applicable to `FUTURES`/`SWAP`  
lever | String | Leverage  
tag | String | Order tag  
  
### GET / Grid algo order positions

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: User ID

#### HTTP Request

`GET /api/v5/tradingBot/grid/positions`

> Request Example
    
    
    GET /api/v5/tradingBot/grid/positions?algoId=448965992920907776&algoOrdType=contract_grid
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
algoOrdType | String | Yes | Algo order type  
`contract_grid`: Contract grid  
algoId | String | Yes | Algo ID  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "adl": "1",
                "algoClOrdId": "",
                "algoId": "449327675342323712",
                "avgPx": "29215.0142857142857149",
                "cTime": "1653400065917",
                "ccy": "USDT",
                "imr": "2045.386",
                "instId": "BTC-USDT-SWAP",
                "instType": "SWAP",
                "last": "29206.7",
                "lever": "5",
                "liqPx": "661.1684795867162",
                "markPx": "29213.9",
                "mgnMode": "cross",
                "mgnRatio": "217.19370606167573",
                "mmr": "40.907720000000005",
                "notionalUsd": "10216.70307",
                "pos": "35",
                "posSide": "net",
                "uTime": "1653400066938",
                "upl": "1.674999999999818",
                "uplRatio": "0.0008190504784478"
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
instId | String | Instrument ID, e.g. `BTC-USDT-SWAP`  
cTime | String | Algo order created time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
uTime | String | Algo order updated time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
avgPx | String | Average open price  
ccy | String | Margin currency  
lever | String | Leverage  
liqPx | String | Estimated liquidation price  
posSide | String | Position side  
`net`  
pos | String | Quantity of positions  
mgnMode | String | Margin mode  
`cross`  
`isolated`  
mgnRatio | String | Maintenance margin ratio  
imr | String | Initial margin requirement  
mmr | String | Maintenance margin requirement  
upl | String | Unrealized profit and loss  
uplRatio | String | Unrealized profit and loss ratio  
last | String | Latest traded price  
notionalUsd | String | Notional value of positions in `USD`  
adl | String | Automatic-Deleveraging, signal area  
Divided into 5 levels, from 1 to 5, the smaller the number, the weaker the adl intensity.  
markPx | String | Mark price  
  
### POST / Spot grid withdraw income

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: User ID

#### HTTP Request

`POST /api/v5/tradingBot/grid/withdraw-income`

> Request Example
    
    
    POST /api/v5/tradingBot/grid/withdraw-income
    body
    {
        "algoId":"448965992920907776"
    }
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
algoId | String | Yes | Algo ID  
  
> Response Example
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
            {
                "algoClOrdId": "",
                "algoId":"448965992920907776",
                "profit":"100"
            }
        ]
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
algoId | String | Algo ID  
algoClOrdId | String | Client-supplied Algo ID  
profit | String | Withdraw profit  
  
### POST / Compute margin balance

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: User ID

#### HTTP Request

`POST /api/v5/tradingBot/grid/compute-margin-balance`

> Request Example
    
    
    POST /api/v5/tradingBot/grid/compute-margin-balance
    body {
       "algoId":"123456",
       "type":"add",
       "amt":"10"
    }
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
algoId | String | Yes | Algo ID  
type | String | Yes | Adjust margin balance type  
`add` `reduce`  
amt | String | No | Adjust margin balance amount  
Default is zero.  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "lever": "0.3877200981166066",
                "maxAmt": "1.8309562403342999"
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
maxAmt | String | Maximum adjustable margin balance amount  
lever | String | Leverage after adjustment of margin balance  
  
### POST / Adjust margin balance

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: User ID

#### HTTP Request

`POST /api/v5/tradingBot/grid/margin-balance`

> Request Example
    
    
    POST /api/v5/tradingBot/grid/margin-balance
    body {
       "algoId":"123456",
       "type":"add",
       "amt":"10"
    }
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
algoId | String | Yes | Algo ID  
type | String | Yes | Adjust margin balance type  
`add` `reduce`  
amt | String | Conditional | Adjust margin balance amount  
Either `amt` or `percent` is required.  
percent | String | Conditional | Adjust margin balance percentage  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "algoClOrdId": "",
                "algoId": "123456"
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
algoId | String | Algo ID  
algoClOrdId | String | Client-supplied Algo ID  
  
### POST / Add investment

It is used to add investment and only applicable to contract gird.

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: User ID

#### HTTP Request

`POST /api/v5/tradingBot/grid/adjust-investment`

> Request Example
    
    
    POST /api/v5/tradingBot/grid/adjust-investment
    body
    {
        "algoId":"448965992920907776",
        "amt":"12"
    }
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
algoId | String | Yes | Algo ID  
amt | String | Yes | The amount is going to be added  
allowReinvestProfit | String | No | Whether reinvesting profits, only applicable to spot grid.  
`true` or `false`. The default is true.  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "algoId": "448965992920907776"
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
algoId | String | Algo ID  
  
### GET / Grid AI parameter (public)

Authentication is not required for this public endpoint.

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: IP

#### HTTP Request

`GET /api/v5/tradingBot/grid/ai-param`

> Request Example
    
    
    GET /api/v5/tradingBot/grid/ai-param?instId=BTC-USDT&algoOrdType=grid
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
algoOrdType | String | Yes | Algo order type  
`grid`: Spot grid  
`contract_grid`: Contract grid  
instId | String | Yes | Instrument ID, e.g. `BTC-USDT`  
direction | String | Conditional | Contract grid type  
`long`,`short`,`neutral`  
Required in the case of `contract_grid`  
duration | String | No | Back testing duration in number of days  
Spot grid default is `7D` with available durations of `7D`, `30D` and `180D`  
Contract grid default is `14D` with available durations of `7D`, `14D` and `30D`  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "algoOrdType": "grid",
                "annualizedRate": "1.5849",
                "ccy": "USDT",
                "direction": "",
                "duration": "7D",
                "gridNum": "5",
                "instId": "BTC-USDT",
                "lever": "0",
                "maxPx": "21373.3",
                "minInvestment": "0.89557758",
                "minPx": "15544.2",
                "perGridProfitRatio": "4.566226200302574",
                "perMaxProfitRate": "0.0733865364573281",
                "perMinProfitRate": "0.0561101403446263",
                "runType": "1",
                "sourceCcy": ""
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
instId | String | Instrument ID, e.g. BTC-USDT-SWAP  
algoOrdType | String | Algo order type  
`grid`: Spot grid  
`contract_grid`: Contract grid  
duration | String | Back testing duration  
`7D`: 7 Days, `30D`: 30 Days, `180D`: 180 Days  
gridNum | String | Grid quantity  
maxPx | String | Upper price of price range  
minPx | String | Lower price of price range  
perMaxProfitRate | String | Estimated maximum Profit margin per grid  
perMinProfitRate | String | Estimated minimum Profit margin per grid  
perGridProfitRatio | String | Per grid profit ratio  
annualizedRate | String | Grid annualized rate  
minInvestment | String | The minimum invest amount  
ccy | String | The invest currency  
runType | String | Grid type  
`1`: Arithmetic, `2`: Geometric  
direction | String | Contract grid type  
`long`,`short`,`neutral`  
Only applicable to contract grid  
lever | String | Leverage  
Only applicable to contract grid  
sourceCcy | String | Source currency  
  
### POST / Compute min investment (public)

Authentication is not required for this public endpoint.

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: IP

#### HTTP Request

`POST /api/v5/tradingBot/grid/min-investment`

> Request Example
    
    
    POST /api/v5/tradingBot/grid/min-investment
    body 
    {
        "instId": "ETH-USDT",
        "algoOrdType":"grid",
        "gridNum": "50",
        "maxPx":"5000",
        "minPx":"3000",
        "runType":"1",
        "investmentData":[
            {
                "amt":"0.01",
                "ccy":"ETH"
            },
            {
                "amt":"100",
                "ccy":"USDT"
            }
        ]
    }
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
instId | String | Yes | Instrument ID, e.g. `BTC-USDT-SWAP`  
algoOrdType | String | Yes | Algo order type  
`grid`: Spot grid  
`contract_grid`: Contract grid  
maxPx | String | Yes | Upper price of price range  
minPx | String | Yes | Lower price of price range  
gridNum | String | Yes | Grid quantity  
runType | String | Yes | Grid type  
`1`: Arithmetic, `2`: Geometric  
direction | String | Conditional | Contract grid type  
`long`,`short`,`neutral`  
Only applicable to `contract grid`  
lever | String | Conditional | Leverage  
Only applicable to `contract grid`  
basePos | Boolean | No | Whether or not open a position when the strategy activates  
Default is `false`  
Neutral contract grid should omit the parameter  
Only applicable to `contract grid`  
investmentType | String | No | Investment type, only applicable to `grid`  
`quote`  
`base`  
`dual`  
triggerStrategy | String | No | Trigger stragety,   
`instant`  
`price`  
`rsi`  
topUpAmt | String | No | Top up amount, only applicable to spot grid  
investmentData | Array of objects | No | Invest Data  
> amt | String | Yes | Invest amount  
> ccy | String | Yes | Invest currency  
  
> Response Example
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
            {
               "minInvestmentData": [  
                   {
                       "amt":"0.1",
                       "ccy":"ETH"
                   },
                   {
                       "amt":"100",
                       "ccy":"USDT"
                   }
               ],
               "singleAmt":"10"
           }
        ]
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
minInvestmentData | Array of objects | Minimum invest Data  
> amt | String | Minimum invest amount  
> ccy | String | Minimum Invest currency  
singleAmt | String | Single grid trading amount  
In terms of `spot grid`, the unit is `quote currency`  
In terms of `contract grid`, the unit is `contract`  
  
### GET / RSI back testing (public)

Authentication is not required for this public endpoint.

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: IP

#### HTTP Request

`GET /api/v5/tradingBot/public/rsi-back-testing`

> Request Example
    
    
    GET /api/v5/tradingBot/public/rsi-back-testing?instId=BTC-USDT&thold=30&timeframe=3m&timePeriod=14
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
instId | String | Yes | Instrument ID, e.g. `BTC-USDT`  
Only applicable to `SPOT`  
timeframe | String | Yes | K-line type  
`3m`, `5m`, `15m`, `30m` (`m`: minute)  
`1H`, `4H` (`H`: hour)  
`1D` (`D`: day)  
thold | String | Yes | Threshold  
The value should be an integer between 1 to 100  
timePeriod | String | Yes | Time Period  
`14`  
triggerCond | String | No | Trigger condition  
`cross_up`  
`cross_down`  
`above`  
`below`  
`cross`  
Default is `cross_down`  
duration | String | No | Back testing duration  
`1M` (`M`: month)  
Default is `1M`  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "triggerNum": "164"
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
triggerNum | String | Trigger number  
  
### GET / Max grid quantity (public)

Authentication is not required for this public endpoint.  

Maximum grid quantity can be retrieved from this endpoint. Minimum grid quantity always is 2.

#### Rate Limit: 5 requests per 2 seconds

#### Rate limit rule: IP

#### HTTP Request

`GET /api/v5/tradingBot/grid/grid-quantity`

> Request Example
    
    
    GET /api/v5/tradingBot/grid/grid-quantity?instId=BTC-USDT-SWAP&runType=1&algoOrdType=contract_grid&maxPx=70000&minPx=50000&lever=5
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
instId | String | Yes | Instrument ID, e.g. `BTC-USDT`  
runType | String | Yes | Grid type  
`1`: Arithmetic  
`2`: Geometric  
algoOrdType | String | Yes | Algo order type  
`grid`: Spot grid  
`contract_grid`: Contract grid  
maxPx | String | Yes | Upper price of price range  
minPx | String | Yes | Lower price of price range  
lever | String | Conditional | Leverage, it is required for contract grid  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "maxGridQty": "285"
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
maxGridQty | String | Maximum grid quantity  
  
### POST / Copy grid algo order

#### Rate Limit: 20 requests per 2 seconds

#### Rate Limit Rule: User ID + Instrument ID

#### HTTP Request

`POST /api/v5/tradingBot/grid/copy-order-algo`

> Request Example
    
    
    # Spot grid copy
    POST /api/v5/tradingBot/grid/copy-order-algo
    body
    {
        "instId": "BTC-USDT",
        "algoOrdType": "grid",
        "sourceAlgoId": "580007082221121536",
        "quoteSz": "1000"
    }
    
    
    
    # Contract grid copy
    POST /api/v5/tradingBot/grid/copy-order-algo
    body
    {
        "instId": "BTC-USDT-SWAP",
        "algoOrdType": "contract_grid",
        "sourceAlgoId": "580007082221121536",
        "lever": "3",
        "autoReserve": true,
        "sz": "5000"
    }
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
instId | String | Yes | Instrument ID, e.g. `BTC-USDT`  
algoOrdType | String | Yes | Algo order type  
`grid`: Spot grid  
`contract_grid`: Contract grid  
sourceAlgoId | String | Yes | Lead algo order ID to follow and copy from  
quoteSz | String | No | Quote currency investment amount  
Only applicable to `grid`  
lever | String | No | Leverage  
Only applicable to `contract_grid`  
autoReserve | Boolean | No | Whether to auto-reserve margin. Only applicable to `contract_grid`  
`true`: Actual margin and extra margin are automatically calculated based on `sz`  
`false`: Manually specify `actualMarginSz` and `extraMarginSz`  
sz | String | No | Total investment amount in USDT. Required when `autoReserve` is `true`  
Only applicable to `contract_grid`  
actualMarginSz | String | No | Actual margin. Required when `autoReserve` is `false`  
Only applicable to `contract_grid`  
extraMarginSz | String | No | Extra margin reserved. Defaults to `0` when unspecified  
Only applicable to `contract_grid`  
algoClOrdId | String | No | Client-supplied Algo ID  
tag | String | No | Order tag  
  
> Response Example
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "algoId": "581234567890123456",
                "algoClOrdId": "",
                "sCode": "0",
                "sMsg": "",
                "tag": ""
            }
        ]
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
algoId | String | Algo order ID  
algoClOrdId | String | Client-supplied Algo ID  
sCode | String | Event execution status code, `0` indicates success  
sMsg | String | Error message if the event execution failed  
tag | String | Order tag  
  
### WS / Spot grid algo orders channel

Retrieve spot grid algo orders. Data will be pushed when triggered by events such as placing/canceling order. It will also be pushed in regular interval according to subscription granularity.

#### URL Path

/ws/v5/business (required login)

> Request Example
    
    
    {
        "id": "1512",
        "op": "subscribe",
        "args": [{
            "channel": "grid-orders-spot",
            "instType": "SPOT"
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
            "channel": "grid-orders-spot",
            "instType": "SPOT"
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
`grid-orders-spot`  
> instType | String | Yes | Instrument type  
`SPOT`  
`ANY`  
> instId | String | No | Instrument ID  
> algoId | String | No | Algo Order ID  
  
> Successful Response Example
    
    
    {
        "id": "1512",
        "event": "subscribe",
        "arg": {
            "channel": "grid-orders-spot",
            "instType": "ANY"
        },
        "connId": "a4d3ae55"
    }
    

> Failure Response Example
    
    
    {
      "id": "1512",
      "event": "error",
      "code": "60012",
      "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{ \"channel\" : \"grid-orders-spot\", \"instType\" : \"FUTURES\"}]}",
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
            "channel": "grid-orders-spot",
            "instType": "ANY",
            "uid": "44705892343619584"
        },
        "data": [{
            "algoClOrdId": "",
            "algoId": "568028283477164032",
            "activeOrdNum" : "10",
            "algoOrdType": "grid",
            "annualizedRate": "0",
            "arbitrageNum": "0",
            "baseSz": "0",
            "cTime": "1681700496249",
            "cancelType": "0",
            "curBaseSz": "0",
            "curQuoteSz": "25",
            "floatProfit": "0",
            "gridNum": "10",
            "gridProfit": "0",
            "instId": "BTC-USDT",
            "instType": "SPOT",
            "investment": "25",
            "maxPx": "5000",
            "minPx": "400",
            "pTime": "1682416738467",
            "perMaxProfitRate": "1.14570215",
            "perMinProfitRate": "0.0991200440528634356837",
            "pnlRatio": "0",
            "profit": "0",
            "quoteSz": "25",
            "rebateTrans": [{
                "rebate": "0",
                "rebateCcy": "BTC"
            }, {
                "rebate": "0",
                "rebateCcy": "USDT"
            }],
            "runPx": "30031.7",
            "runType": "1",
            "triggerParams": [{
                "triggerAction": "start",
                "triggerStrategy": "instant",
                "delaySeconds": "0",
                "triggerType": "auto",
                "triggerTime": ""
            }, {
                "triggerAction": "stop",
                "triggerStrategy": "instant",
                "delaySeconds": "0",
                "stopType": "1",
                "triggerType": "manual",
                "triggerTime": ""
            }],
            "singleAmt": "0.00101214",
            "slTriggerPx": "",
            "state": "running",
            "stopResult": "0",
            "stopType": "2",
            "tag": "",
            "totalAnnualizedRate": "0",
            "totalPnl": "0",
            "tpTriggerPx": "",
            "tradeNum": "0",
            "uTime": "1682406665527",
            "profitSharingRatio": "", 
            "copyType": "0",
            "tradeQuoteCcy": "USDT"
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
`grid`: Spot grid  
> state | String | Algo order state  
`starting`  
`running`  
`stopping`  
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
> investment | String | Investment amount  
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
`1`: Sell base currency `2`: Keep base currency  
> quoteSz | String | Quote currency investment amount  
Only applicable to `Spot grid`  
> baseSz | String | Base currency investment amount  
Only applicable to `Spot grid`  
> curQuoteSz | String | Assets of quote currency currently held  
Only applicable to `Spot grid`  
> curBaseSz | String | Assets of base currency currently held  
Only applicable to `Spot grid`  
> profit | String | Current available profit based on quote currency  
Only applicable to `Spot grid`  
> stopResult | String | Stop result  
`0`: default, `1`: Successful selling of currency at market price, `-1`: Failed to sell currency at market price  
Only applicable to `Spot grid`  
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
> pTime | String | Push time of algo grid information, Unix timestamp format in milliseconds, e.g. `1597026383085`  
> tradeQuoteCcy | String | The quote currency for trading.  
  
### WS / Contract grid algo orders channel

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
  
### WS / Grid positions channel

Retrieve contract grid positions. Data will be pushed when triggered by events such as placing/canceling order.  
Please ignore the empty data.

#### URL Path

/ws/v5/business (required login)

> Request Example
    
    
    {
        "id": "1512",
        "op": "subscribe",
        "args": [{
            "channel": "grid-positions",
            "algoId": "449327675342323712"
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
            "channel": "grid-positions",
            "algoId": "449327675342323712"
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
`grid-positions`  
> algoId | String | Yes | Algo Order ID  
  
> Successful Response Example
    
    
    {
        "id": "1512",
        "event": "subscribe",
        "arg": {
            "channel": "grid-positions",
            "algoId": "449327675342323712"
        },
        "connId": "a4d3ae55"
    }
    

> Failure Response Example
    
    
    {
      "id": "1512",
      "event": "error",
      "code": "60012",
      "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{ \"channel\" : \"grid-positions\", \"instType\" : \"FUTURES\"}]}",
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
> algoId | String | Yes | Algo Order ID  
code | String | No | Error code  
msg | String | No | Error message  
connId | String | Yes | WebSocket connection ID  
  
> Push Data Example: 
    
    
    {
        "arg": {
            "channel": "grid-positions",
            "uid": "4470****9584",
            "algoId": "449327675342323712"
        },
        "data": [{
            "adl": "1",
            "algoClOrdId": "",
            "algoId": "449327675342323712",
            "avgPx": "29181.4638888888888895",
            "cTime": "1653400065917",
            "ccy": "USDT",
            "imr": "2089.2690000000002",
            "instId": "BTC-USDT-SWAP",
            "instType": "SWAP",
            "last": "29852.7",
            "lever": "5",
            "liqPx": "604.7617536513744",
            "markPx": "29849.7",
            "mgnMode": "cross",
            "mgnRatio": "217.71740878394456",
            "mmr": "41.78538",
            "notionalUsd": "10435.794191550001",
            "pTime": "1653536068723",
            "pos": "35",
            "posSide": "net",
            "uTime": "1653445498682",
            "upl": "232.83263888888962",
            "uplRatio": "0.1139826489932205"
        }]
    }
    

#### Response parameters when data is pushed.

**Parameter** | **Type** | **Description**  
---|---|---  
arg | Object | Successfully subscribed channel  
> channel | String | Channel name  
> uid | String | User Identifier  
> algoId | String | Algo Order ID  
data | Array of objects | Subscribed data  
> algoId | String | Algo ID  
> algoClOrdId | String | Client-supplied Algo ID  
> instType | String | Instrument type  
> instId | String | Instrument ID  
> cTime | String | Algo order created time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
> uTime | String | Algo order updated time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
> avgPx | String | Average open price  
> ccy | String | Margin currency  
> lever | String | Leverage  
> liqPx | String | Estimated liquidation price  
> posSide | String | Position side  
`net`  
> pos | String | Quantity of positions  
> mgnMode | String | Margin mode  
`cross`  
`isolated`  
> mgnRatio | String | Maintenance margin ratio  
> imr | String | Initial margin requirement  
> mmr | String | Maintenance margin requirement  
> upl | String | Unrealized profit and loss  
> uplRatio | String | Unrealized profit and loss ratio  
> last | String | Latest traded price  
> notionalUsd | String | Notional value of positions in `USD`  
> adl | String | Automatic-Deleveraging, signal area  
Divided into 5 levels, from 1 to 5, the smaller the number, the weaker the adl intensity.  
> markPx | String | Mark price  
> pTime | String | Push time of positions information, Unix timestamp format in milliseconds, e.g. `1597026383085`  
  
### WS / Grid sub orders channel

Retrieve grid sub orders. Data will be pushed when triggered by events such as placing order.  
Please ignore the empty data.

#### URL Path

/ws/v5/business (required login)

> Request Example
    
    
    {
        "id": "1512",
        "op": "subscribe",
        "args": [{
            "channel": "grid-sub-orders",
            "algoId": "449327675342323712"
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
            "channel": "grid-sub-orders",
            "algoId": "449327675342323712"
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
`grid-sub-orders`  
> algoId | String | Yes | Algo Order ID  
  
> Successful Response Example
    
    
    {
        "id": "1512",
        "event": "subscribe",
        "arg": {
            "channel": "grid-sub-orders",
            "algoId": "449327675342323712"
        },
        "connId": "a4d3ae55"
    }
    

> Failure Response Example
    
    
    {
      "id": "1512",
      "event": "error",
      "code": "60012",
      "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{ \"channel\" : \"grid-sub-orders\", \"instType\" : \"FUTURES\"}]}",
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
> algoId | String | Yes | Algo Order ID  
code | String | No | Error code  
msg | String | No | Error message  
connId | String | Yes | WebSocket connection ID  
  
> Push Data Example: 
    
    
    {
        "arg": {
            "channel": "grid-sub-orders",
            "uid": "44705892343619584",
            "algoId": "449327675342323712"
        },
        "data": [{
            "accFillSz": "0",
            "algoClOrdId": "",
            "algoId": "449327675342323712",
            "algoOrdType": "contract_grid",
            "avgPx": "0",
            "cTime": "1653445498664",
            "ctVal": "0.01",
            "fee": "0",
            "feeCcy": "USDT",
            "groupId": "-1",
            "instId": "BTC-USDT-SWAP",
            "instType": "SWAP",
            "lever": "5",
            "ordId": "449518234142904321",
            "ordType": "limit",
            "pTime": "1653486524502",
            "pnl": "",
            "posSide": "net",
            "px": "28007.2",
            "rebate": "0",
            "rebateCcy": "USDT",
            "side": "buy",
            "state": "live",
            "sz": "1",
            "tag":"",
            "tdMode": "cross",
            "uTime": "1653445498674"
        }]
    }
    

#### Response parameters when data is pushed.

**Parameter** | **Type** | **Description**  
---|---|---  
arg | Object | Successfully subscribed channel  
> channel | String | Channel name  
> uid | String | User Identifier  
> algoId | String | Algo Order ID  
data | Array of objects | Subscribed data  
> algoId | String | Algo ID  
> algoClOrdId | String | Client-supplied Algo ID  
> instType | String | Instrument type  
> instId | String | Instrument ID  
> algoOrdType | String | Algo order type  
`grid`: Spot grid  
`contract_grid`: Contract grid  
> groupId | String | Group ID  
> ordId | String | Sub order ID  
> cTime | String | Sub order created time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
> uTime | String | Sub order updated time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
> tdMode | String | Sub order trade mode  
Margin mode `cross` `isolated`  
Non-Margin mode `cash`  
> tag | String | Order tag  
> ordType | String | Sub order type  
`market`: Market order  
`limit`: Limit order  
`ioc`: Immediate-or-cancel order  
> sz | String | Sub order quantity to buy or sell  
> state | String | Sub order state  
`canceled`  
`live`  
`partially_filled`  
`filled`  
`cancelling`  
> side | String | Sub order side  
`buy` `sell`  
> px | String | Sub order price  
> fee | String | Sub order fee amount  
> feeCcy | String | Sub order fee currency  
> rebate | String | Sub order rebate amount  
> rebateCcy | String | Sub order rebate currency  
> avgPx | String | Sub order average filled price  
> accFillSz | String | Sub order accumulated fill quantity  
> posSide | String | Sub order position side  
`net`  
> pnl | String | Sub order profit and loss  
> ctVal | String | Contract value  
Only applicable to `FUTURES`/`SWAP`/`OPTION`  
> lever | String | Leverage  
> pTime | String | Push time of orders information, Unix timestamp format in milliseconds, e.g. `1597026383085`

---

# 网格交易

网格是一种在指定价格区间自动进行低买高卖的交易策略。用户设定参数后，系统分割小网格自动挂单，随着市场波动，策略低买高卖赚取波段收益。  
`网格交易`功能模块下的API接口需要身份验证。  
  
### POST / 网格策略委托下单 

#### 限速：20次/2s

#### 限速规则：User ID + Instrument ID

#### HTTP请求

`POST /api/v5/tradingBot/grid/order-algo`

> 请求示例
    
    
    # 现货网格下单
    POST /api/v5/tradingBot/grid/order-algo
    body
    {
        "instId": "BTC-USDT",
        "algoOrdType": "grid",
        "maxPx": "5000",
        "minPx": "400",
        "gridNum": "10",
        "runType": "1",
        "quoteSz": "25",
        "triggerParams":[
          {
             "triggerAction":"stop",
             "triggerStrategy":"price",  
             "triggerPx":"1000"
          }
        ]
    }
    
    # 合约网格下单
    POST /api/v5/tradingBot/grid/order-algo
    body
    {
        "instId": "BTC-USDT-SWAP",
        "algoOrdType": "contract_grid",
        "maxPx": "5000",
        "minPx": "400",
        "gridNum": "10",
        "runType": "1",
        "sz": "200", 
        "direction": "long",
        "lever": "2",
        "triggerParams":[
          {
             "triggerAction":"start", 
             "triggerStrategy":"rsi", 
             "timeframe":"30m",
             "thold":"10",
             "triggerCond":"cross",
             "timePeriod":"14"
          },
          {
             "triggerAction":"stop",
             "triggerStrategy":"price",
             "triggerPx":"1000",
             "stopType":"2"
          }
       ]
    }
    
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
instId | String | 是 | 产品ID，如`BTC-USDT`  
algoOrdType | String | 是 | 策略订单类型  
`grid`：现货网格委托  
`contract_grid`：合约网格委托  
maxPx | String | 是 | 区间最高价格  
minPx | String | 是 | 区间最低价格  
gridNum | String | 是 | 网格数量  
runType | String | 否 | 网格类型  
`1`：等差，`2`：等比  
默认为等差  
tpTriggerPx | String | 否 | 止盈触发价  
适用于`现货网格`/`合约网格`  
slTriggerPx | String | 否 | 止损触发价  
适用于`现货网格`/`合约网格`  
algoClOrdId | String | 否 | 用户自定义策略ID  
字母（区分大小写）与数字的组合，可以是纯字母、纯数字且长度要在1-32位之间。  
tag | String | 否 | 订单标签  
profitSharingRatio | String | 否 | 带单员分润比例，仅支持固定比例分润  
`0`,`0.1`,`0.2`,`0.3`  
triggerParams | Array of objects | 否 | 信号触发参数  
适用于`现货网格`/`合约网格`  
> triggerAction | String | 是 | 触发行为  
`start`：网格启动  
`stop`：网格停止  
> triggerStrategy | String | 是 | 触发策略  
`instant`：立即触发  
`price`：价格触发  
`rsi`：rsi指标触发  
默认为`instant`  
> delaySeconds | String | 否 | 延迟触发时间，单位为秒，默认为`0`  
> timeframe | String | 否 | K线种类  
`3m`, `5m`, `15m`, `30m` (`m`代表分钟)  
`1H`, `4H` (`H`代表小时)  
`1D` (`D`代表天)  
该字段只在`triggerStrategy`为`rsi`时有效  
> thold | String | 否 | 阈值  
取值[1,100]的整数  
该字段只在`triggerStrategy`为`rsi`时有效  
> triggerCond | String | 否 | 触发条件  
`cross_up`：上穿  
`cross_down`：下穿  
`above`：上方  
`below`：下方  
`cross`：交叉  
该字段只在`triggerStrategy`为`rsi`时有效  
> timePeriod | String | 否 | 周期  
`14`  
该字段只在`triggerStrategy`为`rsi`下有效  
> triggerPx | String | 否 | 触发价格  
该字段只在`triggerStrategy`为`price`下有效  
> stopType | String | 否 | 策略停止类型  
现货 `1`：卖出交易币，`2`：不卖出交易币  
合约网格 `1`：停止平仓，`2`：停止不平仓   
该字段只在`triggerAction`为`stop`时有效  
  
现货网格

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
quoteSz | String | 可选 | 计价币投入数量  
`quoteSz`和`baseSz`至少指定一个  
baseSz | String | 可选 | 交易币投入数量  
`quoteSz`和`baseSz`至少指定一个  
tradeQuoteCcy | String | No | 用于交易的计价币种。仅适用于现货网格。  
默认值为 instId 的计价币种，例如 BTC-USD 的计价币种为 USD。  
  
合约网格

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
sz | String | 是 | 投入保证金,单位为`USDT`  
direction | String | 是 | 合约网格类型  
`long`：做多，`short`：做空，`neutral`：中性  
lever | String | 是 | 杠杆倍数  
basePos | Boolean | 否 | 是否开底仓  
默认为`false`  
中性合约网格忽略该参数  
tpRatio | String | 否 | 止盈比率，0.1 代表 10%  
slRatio | String | 否 | 止损比率，0.1 代表 10%  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "algoClOrdId": "",
                "algoId": "447053782921515008",
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
algoId | String | 策略订单ID  
algoClOrdId | String | 用户自定义策略ID  
sCode | String | 事件执行结果的code，0代表成功  
sMsg | String | 事件执行失败时的msg  
tag | String | 订单标签  
  
### POST / 修改网格策略基本参数

#### 限速：20次/2s

#### 限速规则：User ID

#### HTTP请求

`POST /api/v5/tradingBot/grid/amend-algo-basic-param`

> 请求示例
    
    
    POST /api/v5/tradingBot/grid/amend-algo-basic-param
    body
        {
            "algoId":"448965992920907776",
            "maxPx": "100",
            "minPx": "10",
            "gridNum": "5"
            "topupAmount": "123.45"
        }
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
algoId | String | 是 | 策略订单ID  
minPx | String | 是 | 最小价格  
maxPx | String | 是 | 最大价格  
gridNum | String | 是 | 网格数  
topupAmount | String | 不是 | 仅限合约网格。可选填写用户自行提供的追加投资金额。若未填写，或明确填写为“0”，在编辑网格参数时，所需的追加投资金额将默认自动追加。  
  
> 返回结果
    
    
    {
        "code": "55186",
        "msg": "Due to market fluctuations, your investment amount is too large to apply these modifications.",
        "data": [
            {
                "algoId": "4283223775520665600",
                "maxTopupAmount": "12456.78",
                "requiredTopupAmount": "12.34"
            }
        ]
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
algoId | String | 策略订单ID  
requiredTopupAmount | String | 修改网格参数所需补充金额  
maxTopupAmount | String | 仅限合约网格。编辑网格参数时的最大追加投资金额。  
  
#### 报错码

**报错码** | **HTTP Status 代码** | **报错文案**  
---|---|---  
51000 | 400 | {param} 参数错误。  
51346 | 400 | 最高价格应高于最低价格。  
55123 | 400 | 您的交易账户余额不足，无法使此修改生效。请您向交易账户转入资金后再试。  
55124 | 200 | 由于行情波动，您的投入金额不足，修改后的参数无法生效。  
55186 | 200 | 由于行情波动，您的投入金额过大，修改后的参数无法生效。  
  
### POST / 修改网格策略订单 

#### 限速：20次/2s

#### 限速规则：User ID

#### HTTP请求

`POST /api/v5/tradingBot/grid/amend-order-algo`

> 请求示例
    
    
    POST /api/v5/tradingBot/grid/amend-order-algo
    body
    {
        "algoId":"448965992920907776",
        "instId":"BTC-USDT-SWAP",
        "slTriggerPx":"1200",
        "tpTriggerPx":""
    }
    
    POST /api/v5/tradingBot/grid/amend-order-algo
    body 
    {
       "algoId":"578963447615062016",
       "instId":"BTC-USDT",
       "triggerParams":[
           {
               "triggerAction":"stop",  
               "triggerStrategy":"price",   
               "triggerPx":"1000"
           }
       ]
    }
    
    POST /api/v5/tradingBot/grid/amend-order-algo
    body 
    {
       "algoId":"578963447615062016",
       "instId":"BTC-USDT-SWAP",
       "triggerParams":[
           {
               "triggerAction":"stop",  
               "triggerStrategy":"instant",   
               "stopType":"1"
           }
       ]
    }
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
algoId | String | 是 | 策略订单ID  
instId | String | 是 | 产品ID，如`BTC-USDT-SWAP`  
slTriggerPx | String | 可选 | 新的止损触发价  
当值为""则代表取消止损触发价  
`slTriggerPx`、`tpTriggerPx`至少要传一个值  
tpTriggerPx | String | 可选 | 新的止盈触发价  
当值为""则代表取消止盈触发价  
tpRatio | String | 否 | 止盈比率，0.1 代表 10%，仅适用于合约网格  
当值为""则代表取消止盈比率  
slRatio | String | 否 | 止损比率，0.1 代表 10%，仅适用于合约网格  
当值为""则代表取消止损比率  
topUpAmt | String | 否 | 增加的投资额，仅适用于现货网格  
triggerParams | Array of objects | 否 | 信号触发参数  
> triggerAction | String | 是 | 触发行为  
`start`：网格启动  
`stop`：网格停止  
> triggerStrategy | String | 是 | 触发策略  
`instant`：立即触发  
`price`：价格触发  
`rsi`：rsi指标触发  
> triggerPx | String | 否 | 触发价格  
该字段只在`triggerStrategy`为`price`下有效  
> stopType | String | 否 | 策略停止类型  
现货 `1`：卖出交易币，`2`：不卖出交易币  
合约网格 `1`：停止平仓，`2`：停止不平仓   
该字段只在`triggerAction`为`stop`时有效  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "algoClOrdId": "",
                "algoId": "448965992920907776",
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
algoId | String | 策略订单ID  
algoClOrdId | String | 用户自定义策略ID  
sCode | String | 事件执行结果的code，0代表成功  
sMsg | String | 事件执行失败时的msg  
tag | String | 订单标签  
  
### POST / 网格策略停止 

每次最多可以撤销10个网格策略。

#### 限速：20次/2s

#### 限速规则：User ID

#### HTTP请求

`POST /api/v5/tradingBot/grid/stop-order-algo`

> 请求示例
    
    
    POST /api/v5/tradingBot/grid/stop-order-algo
    body
    [
        {
            "algoId":"448965992920907776",
            "instId":"BTC-USDT",
            "stopType":"1",
            "algoOrdType":"grid"
        }
    ]
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
algoId | String | 是 | 策略订单ID  
instId | String | 是 | 产品ID，如`BTC-USDT`  
algoOrdType | String | 是 | 策略订单类型  
`grid`：现货网格委托  
`contract_grid`：合约网格委托  
stopType | String | 是 | 网格策略停止类型  
现货网格 `1`：卖出交易币，`2`：不卖出交易币  
合约网格 `1`：市价全平 `2`：停止不平仓  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "algoClOrdId": "",
                "algoId": "448965992920907776",
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
algoId | String | 策略订单ID  
algoClOrdId | String | 用户自定义策略ID  
sCode | String | 事件执行结果的code，0代表成功  
sMsg | String | 事件执行失败时的msg  
tag | String | 订单标签  
  
### POST / 合约网格平仓 

只有处于已停止未平仓状态合约网格可使用该接口

#### 限速：20次/2s

#### 限速规则：User ID

#### HTTP请求

`POST /api/v5/tradingBot/grid/close-position`

> 请求示例
    
    
    POST /api/v5/tradingBot/grid/close-position
    body
    {
        "algoId":"448965992920907776",
        "mktClose":true
    }
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
algoId | String | 是 | 策略订单ID  
mktClose | Boolean | 是 | 是否市价全平  
`true`：市价全平，`false`：部分平仓  
sz | String | 可选 | 平仓数量,单位为张  
部分平仓时必传  
px | String | 可选 | 平仓价格   
部分平仓时必传  
  
> 返回结果
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
            {
                "algoClOrdId": "",
                "algoId":"448965992920907776",
                "ordId":"",
                "tag": ""
            }
        ]
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
algoId | String | 策略订单ID  
ordId | String | 平仓单ID  
市价全平时，该字段为""  
algoClOrdId | String | 用户自定义策略ID  
tag | String | 订单标签  
  
### POST / 撤销合约网格平仓单 

#### 限速：20次/2s

#### 限速规则：User ID

#### HTTP请求

`POST /api/v5/tradingBot/grid/cancel-close-order`

> 请求示例
    
    
    POST /api/v5/tradingBot/grid/cancel-close-order
    body
    {
        "algoId":"448965992920907776",
        "ordId":"570627699870375936"
    }
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
algoId | String | 是 | 策略订单ID  
ordId | String | 是 | 平仓单ID  
  
> 返回结果
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
            {
                "algoClOrdId": "",
                "algoId": "448965992920907776",
                "ordId": "570627699870375936",
                "tag": ""
            }
        ]
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
algoId | String | 策略订单ID  
ordId | String | 平仓单ID  
algoClOrdId | String | 用户自定义策略ID  
tag | String | 订单标签  
  
### POST / 网格策略立即触发 

#### 限速：20次/2s

#### 限速规则：User ID + Instrument ID

#### HTTP请求

`POST /api/v5/tradingBot/grid/order-instant-trigger`

> 请求示例
    
    
    POST /api/v5/tradingBot/grid/order-instant-trigger
    body
    {
        "algoId":"561564133246894080"
    }
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
algoId | String | 是 | 策略订单ID  
topUpAmt | String | 否 | 增加的投资额，仅适用于现货网格  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "algoClOrdId": "",
                "algoId": "561564133246894080"
            }
        ],
        "msg": ""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
algoId | String | 策略订单ID  
algoClOrdId | String | 用户自定义策略ID  
  
### GET / 获取未完成网格策略委托单列表 

#### 限速：20次/2s

#### 限速规则：User ID

#### HTTP请求

`GET /api/v5/tradingBot/grid/orders-algo-pending`

> 请求示例
    
    
    GET /api/v5/tradingBot/grid/orders-algo-pending?algoOrdType=grid
    

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
                "algoId": "56802********64032",
                "algoOrdType": "grid",
                "arbitrageNum": "0",
                "availEq": "",
                "basePos": false,
                "baseSz": "0",
                "cTime": "1681700496249",
                "cancelType": "0",
                "direction": "",
                "floatProfit": "0",
                "gridNum": "10",
                "gridProfit": "0",
                "instFamily": "",
                "instId": "BTC-USDT",
                "instType": "SPOT",
                "investment": "25",
                "lever": "",
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
                "slTriggerPx": "",
                "state": "running",
                "stopType": "",
                "sz": "",
                "tag": "",
                "totalPnl": "0",
                "tpTriggerPx": "",
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
                        "triggerTime": ""
                    }
                ],
                "uTime": "1682062564350",
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
`starting`：启动中  
`running`：运行中  
`stopping`：终止中  
`pending_signal`：等待触发  
`no_close_position`：已停止未平仓（仅适用于合约网格）  
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
tradeQuoteCcy | String | 用于交易的计价币种。  
  
### GET / 获取历史网格策略委托单列表 

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
  
### GET / 获取网格策略委托订单详情 

#### 限速：20次/2s

#### 限速规则：User ID

#### HTTP请求

`GET /api/v5/tradingBot/grid/orders-algo-details`

> 请求示例
    
    
    GET /api/v5/tradingBot/grid/orders-algo-details?algoId=448965992920907776&algoOrdType=grid
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
algoOrdType | String | 是 | 策略订单类型  
`grid`：现货网格委托  
`contract_grid`：合约网格委托  
algoId | String | 是 | 策略订单ID  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "actualLever": "",
                "activeOrdNum": "0",
                "algoClOrdId": "",
                "algoId": "448965992920907776",
                "algoOrdType": "grid",
                "annualizedRate": "0",
                "arbitrageNum": "0",
                "availEq": "",
                "basePos": false,
                "baseSz": "0",
                "cTime": "1681181054927",
                "cancelType": "1",
                "curBaseSz": "0",
                "curQuoteSz": "0",
                "direction": "",
                "eq": "",
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
                "perMaxProfitRate": "1.14570215",
                "perMinProfitRate": "0.0991200440528634356837",
                "pnlRatio": "0",
                "profit": "0.00000000",
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
                "runPx": "30089.7",
                "singleAmt": "0.00101214",
                "slTriggerPx": "0",
                "state": "stopped",
                "stopResult": "0",
                "stopType": "1",
                "sz": "",
                "tag": "",
                "totalAnnualizedRate": "0",
                "totalPnl": "0",
                "tpTriggerPx": "0",
                "tradeNum": "0",
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
                        "triggerType": "manual",
                        "triggerTime": "1681181186484"
                    }
                ],
                "uTime": "1681181186496",
                "uly": "",
                "profitSharingRatio": "",
                "copyType": "0",
                "tpRatio": "",
                "slRatio": "",
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
`starting`：启动中  
`running`：运行中  
`stopping`：终止中  
`no_close_position`：已停止未平仓（仅适用于合约网格）  
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
tradeNum | String | 挂单成交次数  
arbitrageNum | String | 网格套利次数  
singleAmt | String | 单网格买卖量  
perMinProfitRate | String | 预期单网格最低利润率  
perMaxProfitRate | String | 预期单网格最高利润率  
runPx | String | 启动时价格  
totalPnl | String | 总收益  
pnlRatio | String | 收益率  
investment | String | 累计投入金额  
现货网格如果投入了交易币则折算为计价币  
gridProfit | String | 网格利润  
floatProfit | String | 浮动盈亏  
totalAnnualizedRate | String | 总年化  
annualizedRate | String | 网格年化  
cancelType | String | 网格策略停止原因  
`0`：无  
`1`：手动停止  
`2`：止盈停止  
`3`：止损停止  
`4`：风控停止  
`5`：交割停止  
`6`: 信号停止  
stopType | String | 网格策略停止类型  
现货网格 `1`：卖出交易币，`2`：不卖出交易币  
合约网格 `1`：市价全平，`2`：停止不平仓  
activeOrdNum | String | 子订单挂单数量  
quoteSz | String | 计价币投入数量  
仅适用于`现货网格`  
baseSz | String | 交易币投入数量  
仅适用于`现货网格`  
curQuoteSz | String | 当前持有的计价币资产  
仅适用于`现货网格`  
curBaseSz | String | 当前持有的交易币资产  
仅适用于`现货网格`  
profit | String | 当前可提取利润,单位是计价币  
仅适用于`现货网格`  
stopResult | String | 策略停止结果  
`0`：默认，`1`：市价卖币成功 `-1`：市价卖币失败  
仅适用于`现货网格`  
direction | String | 合约网格类型  
`long`：做多，`short`：做空，`neutral`：中性  
仅适用于`合约网格`  
basePos | Boolean | 是否开底仓  
仅适用于`合约网格`  
sz | String | 投入保证金，单位为`USDT`  
仅适用于`合约网格`  
lever | String | 杠杆倍数  
仅适用于`合约网格`  
actualLever | String | 实际杠杆倍数  
仅适用于`合约网格`  
liqPx | String | 预估强平价格  
仅适用于`合约网格`  
uly | String | 标的指数  
仅适用于`合约网格`  
instFamily | String | 交易品种  
适用于`交割`/`永续`/`期权`，如 `BTC-USD`  
适用于`合约网格`  
ordFrozen | String | 挂单占用  
适用于`合约网格`  
availEq | String | 可用保证金  
适用于`合约网格`  
eq | String | 策略账户总权益  
仅适用于`合约网格`  
tag | String | 订单标签  
profitSharingRatio | String | 分润比例  
取值范围[0,0.3]  
如果是普通订单（既不是带单也不是跟单），该字段返回""  
copyType | String | 分润订单类型  
`0`：普通订单  
`1`：普通跟单  
`2`：分润跟单  
`3`：带单  
tpRatio | String | 止盈比率，0.1 代表 10%  
slRatio | String | 止损比率，0.1 代表 10%  
fee | String | 累计手续费金额，仅适用于合约网格，其他网格策略为""  
feeCcy | String | 累计手续费货币。仅适用于合约网格，其他网格策略为""  
fundingFee | String | 累计资金费用，仅适用于合约网格，其他网格策略为""  
tradeQuoteCcy | String | 用于交易的计价币种。  
  
### GET / 获取网格策略委托子订单信息 

#### 限速：20次/2s

#### 限速规则：User ID

#### HTTP请求

`GET /api/v5/tradingBot/grid/sub-orders`

> 请求示例
    
    
    GET /api/v5/tradingBot/grid/sub-orders?algoId=123456&type=live&algoOrdType=grid
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
algoId | String | 是 | 策略订单ID  
algoOrdType | String | 是 | 策略订单类型  
`grid`：现货网格委托  
`contract_grid`：合约网格委托  
type | String | 是 | 子订单状态  
`live`：未成交  
`filled`：已成交  
groupId | String | 否 | 组ID  
after | String | 否 | 请求此ID之前（更旧的数据）的分页内容，传的值为对应接口的`ordId`  
before | String | 否 | 请求此ID之后（更新的数据）的分页内容，传的值为对应接口的`ordId`  
limit | String | 否 | 返回结果的数量，最大为100，默认100条  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "accFillSz": "0",
                "algoClOrdId": "",
                "algoId": "448965992920907776",
                "algoOrdType": "grid",
                "avgPx": "0",
                "cTime": "1653347949771",
                "ccy": "",
                "ctVal": "",
                "fee": "0",
                "feeCcy": "USDC",
                "groupId": "3",
                "instId": "BTC-USDC",
                "instType": "SPOT",
                "lever": "0",
                "ordId": "449109084439187456",
                "ordType": "limit",
                "pnl": "0",
                "posSide": "net",
                "px": "30404.3",
                "rebate": "0",
                "rebateCcy": "USDT",
                "side": "sell",
                "state": "live",    
                "sz": "0.00059213",
                "tag": "",
                "tdMode": "cash",
                "uTime": "1653347949831"
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
algoOrdType | String | 策略订单类型  
`grid`：现货网格委托  
`contract_grid`：合约网格委托  
groupId | String | 组ID  
ordId | String | 子订单ID  
cTime | String | 子订单创建时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
uTime | String | 子订单更新时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
tdMode | String | 子订单交易模式  
`cross`：全仓  
`isolated`：逐仓  
`cash`：非保证金  
ccy | String | 保证金币种  
仅适用于`合约模式`模式下的`全仓杠杆`订单  
ordType | String | 子订单类型  
`market`：市价单  
`limit`：限价单  
`ioc`：立即成交并取消剩余  
sz | String | 子订单委托数量  
state | String | 子订单状态  
`canceled`：撤单成功  
`live`：等待成交  
`partially_filled`：部分成交  
`filled`：完全成交  
`cancelling`：撤单中  
side | String | 子订单订单方向  
`buy`：买  
`sell`：卖  
px | String | 子订单委托价格  
fee | String | 子订单手续费数量  
feeCcy | String | 子订单手续费币种  
rebate | String | 子订单返佣数量  
rebateCcy | String | 子订单返佣币种  
avgPx | String | 子订单平均成交价格  
accFillSz | String | 子订单累计成交数量  
posSide | String | 子订单持仓方向  
`net`：买卖模式  
pnl | String | 子订单收益  
ctVal | String | 合约面值  
仅支持`FUTURES/SWAP`  
lever | String | 杠杆倍数  
tag | String | 订单标签  
  
### GET / 获取网格策略委托持仓 

#### 限速：20次/2s

#### 限速规则：User ID

#### HTTP请求

`GET /api/v5/tradingBot/grid/positions`

> 请求示例
    
    
    GET /api/v5/tradingBot/grid/positions?algoId=448965992920907776&algoOrdType=contract_grid
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
algoOrdType | String | 是 | 订单类型  
`contract_grid`：合约网格委托  
algoId | String | 是 | 策略订单ID  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "adl": "1",
                "algoClOrdId": "",
                "algoId": "449327675342323712",
                "avgPx": "29215.0142857142857149",
                "cTime": "1653400065917",
                "ccy": "USDT",
                "imr": "2045.386",
                "instId": "BTC-USDT-SWAP",
                "instType": "SWAP",
                "last": "29206.7",
                "lever": "5",
                "liqPx": "661.1684795867162",
                "markPx": "29213.9",
                "mgnMode": "cross",
                "mgnRatio": "217.19370606167573",
                "mmr": "40.907720000000005",
                "notionalUsd": "10216.70307",
                "pos": "35",
                "posSide": "net",
                "uTime": "1653400066938",
                "upl": "1.674999999999818",
                "uplRatio": "0.0008190504784478"
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
instId | String | 产品ID，如 `BTC-USDT-SWAP`  
cTime | String | 策略订单创建时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
uTime | String | 策略订单更新时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
avgPx | String | 开仓均价  
ccy | String | 保证金币种  
lever | String | 杠杆倍数  
liqPx | String | 预估强平价  
posSide | String | 持仓方向  
`net`：买卖模式  
pos | String | 持仓数量  
mgnMode | String | 保证金模式  
`cross`：全仓  
`isolated`：逐仓  
mgnRatio | String | 维持保证金率  
imr | String | 初始保证金  
mmr | String | 维持保证金  
upl | String | 未实现收益  
uplRatio | String | 未实现收益率  
last | String | 最新成交价  
notionalUsd | String | 仓位美金价值  
adl | String | 自动减仓信号区  
分为5档，从1到5，数字越小代表adl强度越弱  
markPx | String | 标记价格  
  
### POST / 现货网格提取利润 

#### 限速：20次/2s

#### 限速规则：User ID

#### HTTP请求

`POST /api/v5/tradingBot/grid/withdraw-income`

> 请求示例
    
    
    POST /api/v5/tradingBot/grid/withdraw-income
    body
    {
        "algoId":"448965992920907776"
    }
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
algoId | String | 是 | 策略订单ID  
  
> 返回结果
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
            {
                "algoClOrdId": "",
                "algoId":"448965992920907776",
                "profit":"100"
            }
        ]
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
algoId | String | 策略订单ID  
algoClOrdId | String | 用户自定义策略ID  
profit | String | 提取的利润  
  
### POST / 调整保证金计算 

#### 限速：20次/2s

#### 限速规则：User ID

#### HTTP请求

`POST /api/v5/tradingBot/grid/compute-margin-balance`

> 请求示例
    
    
    POST /api/v5/tradingBot/grid/compute-margin-balance
    body {
       "algoId":"123456",
       "type":"add",
       "amt":"10"
    }
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
algoId | String | 是 | 策略订单ID  
type | String | 是 | 调整保证金类型  
`add`：增加，`reduce`：减少  
amt | String | 否 | 调整保证金数量  
  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "lever": "0.3877200981166066",
                "maxAmt": "1.8309562403342999"
            }
        ],
        "msg": ""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
maxAmt | String | 最多可调整的保证金数量  
lever | String | 调整保证金后的杠杠倍数  
  
### POST / 调整保证金 

#### 限速：20次/2s

#### 限速规则：User ID

#### HTTP请求

`POST /api/v5/tradingBot/grid/margin-balance`

> 请求示例
    
    
    POST /api/v5/tradingBot/grid/margin-balance
    body {
       "algoId":"123456",
       "type":"add",
       "amt":"10"
    }
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
algoId | String | 是 | 策略订单ID  
type | String | 是 | 调整保证金类型  
`add`：增加，`reduce`：减少  
amt | String | 可选 | 调整保证金数量  
`amt`和`percent`必须传一个  
percent | String | 可选 | 调整保证金百分比  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "algoClOrdId": "",
                "algoId": "123456"
            }
        ],
        "msg": ""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
algoId | String | 策略订单ID  
algoClOrdId | String | 用户自定义策略ID  
  
### POST / 加仓 

该接口用于加仓，仅适用于合约网格。

#### 限速：20次/2s

#### 限速规则：User ID

#### HTTP请求

`POST /api/v5/tradingBot/grid/adjust-investment`

> 请求示例
    
    
    POST /api/v5/tradingBot/grid/adjust-investment
    body
    {
        "algoId":"448965992920907776",
        "amt":"12"
    }
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
algoId | String | 是 | 策略订单ID  
amt | String | 是 | 加仓数量  
allowReinvestProfit | String | 否 | 是否复投利润，仅适用于现货网格。  
`true` 或者 `false`。默认为 true。  
  
> 返回结果
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
            {
                "algoId":"448965992920907776"
            }
        ]
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
algoId | String | 策略订单ID  
  
### GET / 网格策略智能回测（公共） 

公共接口无须鉴权

#### 限速：20次/2s

#### 限速规则：IP

#### HTTP请求

`GET /api/v5/tradingBot/grid/ai-param`

> 请求示例
    
    
    GET /api/v5/tradingBot/grid/ai-param?instId=BTC-USDT&algoOrdType=grid
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
algoOrdType | String | 是 | 策略订单类型  
`grid`：现货网格委托  
`contract_grid`：合约网格委托  
instId | String | 是 | 产品ID，如`BTC-USDT`  
direction | String | 可选 | 合约网格类型  
`long`：做多，`short`：做空，`neutral`：中性  
合约网格必填  
duration | String | 否 | 回测时长，单位为天  
现货网格默认 `7D`，可选：`7D`、`30D`、`180D`  
合约网格默认 `14D`，可选：`7D`、`14D`、`30D`  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "algoOrdType": "grid",
                "annualizedRate": "1.5849",
                "ccy": "USDT",
                "direction": "",
                "duration": "7D",
                "gridNum": "5",
                "instId": "BTC-USDT",
                "lever": "0",
                "maxPx": "21373.3",
                "minInvestment": "0.89557758",
                "minPx": "15544.2",
                "perGridProfitRatio": "4.566226200302574",
                "perMaxProfitRate": "0.0733865364573281",
                "perMinProfitRate": "0.0561101403446263",
                "runType": "1",
                "sourceCcy": ""
            }
        ],
        "msg": ""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
instId | String | 产品ID  
algoOrdType | String | 策略订单类型  
`grid`：现货网格委托  
`contract_grid`：合约网格委托  
duration | String | 回测周期  
`7D`：7天，`30D`：30天，`180D`：180天  
gridNum | String | 网格数量  
maxPx | String | 区间最高价格  
minPx | String | 区间最低价格  
perMaxProfitRate | String | 单网格最高利润率  
perMinProfitRate | String | 单网格最低利润率  
perGridProfitRatio | String | 单网格利润率  
annualizedRate | String | 网格年化收益率  
minInvestment | String | 最小投资数量  
ccy | String | 投资币种  
runType | String | 网格类型  
`1`：等差，`2`：等比  
direction | String | 合约网格类型  
仅适用于`合约网格`  
lever | String | 杠杆倍数  
仅适用于`合约网格`  
sourceCcy | String | 来源币种  
  
### POST / 计算最小投资数量（公共） 

公共接口无须鉴权

#### 限速：20次/2s

#### 限速规则：IP

#### HTTP请求

`POST /api/v5/tradingBot/grid/min-investment`

> 请求示例
    
    
    POST /api/v5/tradingBot/grid/min-investment
    body
    {
        "instId": "ETH-USDT",
        "algoOrdType":"grid",
        "gridNum": "50",
        "maxPx":"5000",
        "minPx":"3000",
        "runType":"1",
        "investmentData":[
            {
                "amt":"0.01",
                "ccy":"ETH"
            },
            {
                "amt":"100",
                "ccy":"USDT"
            }
        ]
    }
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
instId | String | 是 | 产品ID，如`BTC-USDT`  
algoOrdType | String | 是 | 策略订单类型  
`grid`：现货网格委托  
`contract_grid`：合约网格委托  
gridNum | String | 是 | 网格数量  
maxPx | String | 是 | 区间最高价格  
minPx | String | 是 | 区间最低价格  
runType | String | 是 | 网格类型  
`1`：等差，`2`：等比  
direction | String | 可选 | 合约网格类型  
`long`：做多，`short`：做空，`neutral`：中性  
适用于合约网格  
lever | String | 可选 | 杠杆倍数  
适用于合约网格  
basePos | Boolean | 否 | 是否开底仓  
默认为`false`  
investmentType | String | 否 | 投资类型, 仅适用于现货网格  
`quote`: 计价货币  
`base`: 交易货币  
`dual`: 计价货币和交易货币  
triggerStrategy | String | 否 | 触发策略,   
`instant`: 立即触发   
`price`: 价格触发  
`rsi`: rsi 触发  
topUpAmt | String | 否 | 增加的投资额，仅适用于现货网格  
investmentData | Array of objects | 否 | 投资信息  
> amt | String | 是 | 投资数量  
> ccy | String | 是 | 投资币种  
  
> 返回结果
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
            {
               "minInvestmentData": [  
                   {
                       "amt":"0.1",
                       "ccy":"ETH"
                   },
                   {
                       "amt":"100",
                       "ccy":"USDT"
                   }
               ],
               "singleAmt":"10"
           }
        ]
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
minInvestmentData | Array of objects | 最小投入信息  
> amt | String | 最小投入数量  
> ccy | String | 最小投入币种  
singleAmt | String | 单网格买卖量  
现货网格单位为计价币  
合约网格单位为张  
  
### GET / RSI回测（公共） 

公共接口无须鉴权

#### 限速：20次/2s

#### 限速规则：IP

#### HTTP请求

`GET /api/v5/tradingBot/public/rsi-back-testing`

> 请求示例
    
    
    GET /api/v5/tradingBot/public/rsi-back-testing?instId=BTC-USDT&thold=30&timeframe=3m&timePeriod=14
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
instId | String | 是 | 产品ID，如`BTC-USDT`  
适用于`币币`  
timeframe | String | 是 | K线种类  
`3m`, `5m`, `15m`, `30m` (`m`代表分钟)  
`1H`, `4H` (`H`代表小时)  
`1D` (`D`代表天)  
thold | String | 是 | 阈值  
取值[1,100]的整数  
timePeriod | String | 是 | 周期  
`14`  
triggerCond | String | 否 | 触发条件  
`cross_up`：上穿  
`cross_down`：下穿  
`above`：上方  
`below`：下方  
`cross`：交叉  
默认是`cross_down`  
duration | String | 否 | 回测周期  
`1M`：1个月  
默认`1M`  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "triggerNum": "164"
            }
        ],
        "msg": ""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
triggerNum | String | 触发次数  
  
### GET / 最大网格数量（公共） 

公共接口无须鉴权  

可通过该接口获取最大网格数量，最小网格数量总是 2。

#### 限速：5次/2s

#### 限速规则：IP

#### HTTP请求

`GET /api/v5/tradingBot/grid/grid-quantity`

> 请求示例
    
    
    GET /api/v5/tradingBot/grid/grid-quantity?instId=BTC-USDT-SWAP&runType=1&algoOrdType=contract_grid&maxPx=70000&minPx=50000&lever=5
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
instId | String | 是 | 产品ID，如`BTC-USDT`  
runType | String | 是 | 网格类型  
`1`: 等差  
`2`: 等比  
algoOrdType | String | 是 | 策略订单类型  
`grid`：现货网格委托  
`contract_grid`：合约网格委托  
maxPx | String | 是 | 区间最高价格  
minPx | String | 是 | 区间最低价格  
lever | String | 可选 | 杠杆倍数, 合约网格时必填  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "maxGridQty": "285"
            }
        ],
        "msg": ""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
maxGridQty | String | 最大网格数量  
  
### POST / 网格跟单下单 

#### 限速：20次/2s

#### 限速规则：User ID + Instrument ID

#### HTTP请求

`POST /api/v5/tradingBot/grid/copy-order-algo`

> 请求示例
    
    
    # 现货网格跟单
    POST /api/v5/tradingBot/grid/copy-order-algo
    body
    {
        "instId": "BTC-USDT",
        "algoOrdType": "grid",
        "sourceAlgoId": "580007082221121536",
        "quoteSz": "1000"
    }
    
    
    
    # 合约网格跟单
    POST /api/v5/tradingBot/grid/copy-order-algo
    body
    {
        "instId": "BTC-USDT-SWAP",
        "algoOrdType": "contract_grid",
        "sourceAlgoId": "580007082221121536",
        "lever": "3",
        "autoReserve": true,
        "sz": "5000"
    }
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
instId | String | 是 | 产品ID，如 `BTC-USDT`  
algoOrdType | String | 是 | 策略订单类型  
`grid`：现货网格  
`contract_grid`：合约网格  
sourceAlgoId | String | 是 | 被跟单的策略订单ID  
quoteSz | String | 否 | 计价币投入金额  
仅适用于 `grid`  
lever | String | 否 | 杠杆倍数  
仅适用于 `contract_grid`  
autoReserve | Boolean | 否 | 是否自动预留保证金，仅适用于 `contract_grid`  
`true`：自动计算实际保证金和额外保证金  
`false`：手动指定 `actualMarginSz` 和 `extraMarginSz`  
sz | String | 否 | 合约网格总投入金额（USDT），当 `autoReserve` 为 `true` 时必填  
仅适用于 `contract_grid`  
actualMarginSz | String | 否 | 实际保证金，当 `autoReserve` 为 `false` 时必填  
仅适用于 `contract_grid`  
extraMarginSz | String | 否 | 额外保证金，当 `autoReserve` 为 `false` 时选填，默认为 `0`  
仅适用于 `contract_grid`  
algoClOrdId | String | 否 | 客户自定义策略单ID  
tag | String | 否 | 订单标签  
  
> 返回结果
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "algoId": "581234567890123456",
                "algoClOrdId": "",
                "sCode": "0",
                "sMsg": "",
                "tag": ""
            }
        ]
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
algoId | String | 策略订单ID  
algoClOrdId | String | 客户自定义策略单ID  
sCode | String | 事件执行结果的 code，0 代表成功  
sMsg | String | 事件执行失败时的 msg  
tag | String | 订单标签  
  
### WS / 现货网格策略委托订单频道 

支持现货网格策略订单的定时推送和事件推送

#### 服务地址

/ws/v5/business (需要登录)

> 请求示例
    
    
    {
        "id": "1512",
        "op": "subscribe",
        "args": [{
            "channel": "grid-orders-spot",
            "instType": "SPOT"
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
            "channel": "grid-orders-spot",
            "instType": "SPOT"
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
`grid-orders-spot`  
> instType | String | 是 | 产品类型  
`SPOT`：币币  
`ANY`：全部  
> instId | String | 否 | 产品ID  
> algoId | String | 否 | 策略ID  
  
> 成功返回示例
    
    
    {
        "id": "1512",
        "event": "subscribe",
        "arg": {
            "channel": "grid-orders-spot",
            "instType": "ANY"
        },
        "connId": "a4d3ae55"
    }
    

> 失败返回示例
    
    
    {
        "id": "1512",
        "event": "error",
        "code": "60012",
        "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{ \"channel\" : \"grid-orders-spot\", \"instType\" : \"FUTURES\"}]}",
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
            "channel": "grid-orders-spot",
            "instType": "ANY",
            "uid": "4470****9584"
        },
        "data": [{
            "algoClOrdId": "",
            "algoId": "568028283477164032",
            "activeOrdNum":"10",
            "algoOrdType": "grid",
            "annualizedRate": "0",
            "arbitrageNum": "0",
            "baseSz": "0",
            "cTime": "1681700496249",
            "cancelType": "0",
            "curBaseSz": "0",
            "curQuoteSz": "25",
            "floatProfit": "0",
            "gridNum": "10",
            "gridProfit": "0",
            "instId": "BTC-USDT",
            "instType": "SPOT",
            "investment": "25",
            "maxPx": "5000",
            "minPx": "400",
            "pTime": "1682416738467",
            "perMaxProfitRate": "1.14570215",
            "perMinProfitRate": "0.0991200440528634356837",
            "pnlRatio": "0",
            "profit": "0",
            "quoteSz": "25",
            "rebateTrans": [{
                "rebate": "0",
                "rebateCcy": "BTC"
            }, {
                "rebate": "0",
                "rebateCcy": "USDT"
            }],
            "runPx": "30031.7",
            "runType": "1",
            "triggerParams": [{
                "triggerAction": "start",
                "triggerStrategy": "instant",
                "delaySeconds": "0",
                "triggerType": "auto",
                "triggerTime": ""
            }, {
                "triggerAction": "stop",
                "triggerStrategy": "instant",
                "delaySeconds": "0",
                "stopType": "1",
                "triggerType": "manual",
                "triggerTime": ""
            }],
            "singleAmt": "0.00101214",
            "slTriggerPx": "",
            "state": "running",
            "stopResult": "0",
            "stopType": "2",
            "tag": "",
            "totalAnnualizedRate": "0",
            "totalPnl": "0",
            "tpTriggerPx": "",
            "tradeNum": "0",
            "uTime": "1682406665527",
            "profitSharingRatio": "",
            "copyType": "0",
            "tradeQuoteCcy": "USDT"
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
`grid`：现货网格  
> state | String | 订单状态  
`starting`：启动中  
`running`：运行中  
`stopping`：终止中  
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
`3M`, `5M`, `15M`, `30M` (`M`代表分钟)  
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
现货 `1`：卖出交易币，`2`：不卖出交易币  
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
> investment | String | 投入金额  
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
> quoteSz | String | 计价币投入数量  
仅适用于`现货网格`  
> baseSz | String | 交易币投入数量  
仅适用于`现货网格`  
> curQuoteSz | String | 当前持有的计价币资产  
仅适用于`现货网格`  
> curBaseSz | String | 当前持有的交易币资产  
仅适用于`现货网格`  
> profit | String | 当前可提取利润,单位是计价币  
仅适用于`现货网格`  
> stopResult | String | 现货网格策略停止结果  
`0`：默认，`1`：市价卖币成功 `-1`：市价卖币失败  
仅适用于`现货网格`  
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
> pTime | String | 网格策略的推送时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
> tradeQuoteCcy | String | 用于交易的计价币种。  
  
### WS / 合约网格策略委托订单频道 

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
  
### WS / 合约网格持仓频道 

支持网格策略持仓的首次订阅推送，定时推送和事件推送  
请忽略空数据

#### 服务地址

/ws/v5/business (需要登录)

> 请求示例
    
    
    {
        "id": "1512",
        "op": "subscribe",
        "args": [{
            "channel": "grid-positions",
            "algoId": "449327675342323712"
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
            "channel": "grid-positions",
            "algoId": "449327675342323712"
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
`grid-positions`  
> algoId | String | 是 | 策略ID  
  
> 成功返回示例
    
    
    {
        "id": "1512",
        "event": "subscribe",
        "arg": {
            "channel": "grid-positions",
            "algoId": "449327675342323712"
        },
        "connId": "a4d3ae55"
    }
    

> 失败返回示例
    
    
    {
        "id": "1512",
        "event": "error",
        "code": "60012",
        "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{ \"channel\" : \"grid-positions\", \"instType\" : \"FUTURES\"}]}",
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
> algoId | String | 是 | 策略ID  
code | String | 否 | 错误码  
msg | String | 否 | 错误消息  
connId | String | 是 | WebSocket连接ID  
  
> 推送示例
    
    
    {
        "arg": {
            "channel": "grid-positions",
            "uid": "4470****9584",
            "algoId": "449327675342323712"
        },
        "data": [{
            "adl": "1",
            "algoClOrdId": "",
            "algoId": "449327675342323712",
            "avgPx": "29181.4638888888888895",
            "cTime": "1653400065917",
            "ccy": "USDT",
            "imr": "2089.2690000000002",
            "instId": "BTC-USDT-SWAP",
            "instType": "SWAP",
            "last": "29852.7",
            "lever": "5",
            "liqPx": "604.7617536513744",
            "markPx": "29849.7",
            "mgnMode": "cross",
            "mgnRatio": "217.71740878394456",
            "mmr": "41.78538",
            "notionalUsd": "10435.794191550001",
            "pTime": "1653536068723",
            "pos": "35",
            "posSide": "net",
            "uTime": "1653445498682",
            "upl": "232.83263888888962",
            "uplRatio": "0.1139826489932205"
        }]
    }
    

#### 推送数据参数

**参数名** | **类型** | **描述**  
---|---|---  
arg | Object | 订阅成功的频道  
> channel | String | 频道名  
> uid | String | 用户标识  
> algoId | String | 策略订单ID  
data | Array of objects | 订阅的数据  
> algoId | String | 策略订单ID  
> algoClOrdId | String | 用户自定义策略ID  
> instType | String | 产品类型  
> instId | String | 产品ID  
> cTime | String | 策略订单创建时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
> uTime | String | 策略订单更新时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
> avgPx | String | 开仓均价  
> ccy | String | 保证金币种  
> lever | String | 杠杆倍数  
> liqPx | String | 预估强平价  
> posSide | String | 持仓方向  
`net`：买卖模式  
> pos | String | 持仓数量  
> mgnMode | String | 保证金模式  
`cross`：全仓  
`isolated`：逐仓  
> mgnRatio | String | 维持保证金率  
> imr | String | 初始保证金  
> mmr | String | 维持保证金  
> upl | String | 未实现收益  
> uplRatio | String | 未实现收益率  
> last | String | 最新成交价  
> notionalUsd | String | 仓位美金价值  
> adl | String | 自动减仓信号区  
分为5档，从1到5，数字越小代表adl强度越弱  
> markPx | String | 标记价格  
> pTime | String | 订单信息的推送时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
  
### WS / 网格策略子订单频道 

支持网格策略子订单的事件推送  
请忽略空数据

#### 服务地址

/ws/v5/business (需要登录)

> 请求示例
    
    
    {
        "id": "1512",
        "op": "subscribe",
        "args": [{
            "channel": "grid-sub-orders",
            "algoId": "449327675342323712"
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
            "channel": "grid-sub-orders",
            "algoId": "449327675342323712"
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
`grid-sub-orders`  
> algoId | String | 是 | 策略ID  
  
> 成功返回示例
    
    
    {
        "id": "1512",
        "event": "subscribe",
        "arg": {
            "channel": "grid-sub-orders",
            "algoId": "449327675342323712"
        },
        "connId": "a4d3ae55"
    }
    

> 失败返回示例
    
    
    {
        "id": "1512",
        "event": "error",
        "code": "60012",
        "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{ \"channel\" : \"grid-sub-orders\", \"instType\" : \"FUTURES\"}]}",
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
> algoId | String | 是 | 策略ID  
code | String | 否 | 错误码  
msg | String | 否 | 错误消息  
connId | String | 是 | WebSocket连接ID  
  
> 推送示例
    
    
    {
        "arg": {
            "channel": "grid-sub-orders",
            "uid": "44705892343619584",
            "algoId": "449327675342323712"
        },
        "data": [{
            "accFillSz": "0",
            "algoClOrdId": "",
            "algoId": "449327675342323712",
            "algoOrdType": "contract_grid",
            "avgPx": "0",
            "cTime": "1653445498664",
            "ctVal": "0.01",
            "fee": "0",
            "feeCcy": "USDT",
            "groupId": "-1",
            "instId": "BTC-USDT-SWAP",
            "instType": "SWAP",
            "lever": "5",
            "ordId": "449518234142904321",
            "ordType": "limit",
            "pTime": "1653486524502",
            "pnl": "",
            "posSide": "net",
            "px": "28007.2",
            "rebate": "0",
            "rebateCcy": "USDT",
            "side": "buy",
            "state": "live",
            "sz": "1",
            "tag":"",
            "tdMode": "cross",
            "uTime": "1653445498674"
        }]
    }
    

#### 推送数据参数

**参数名** | **类型** | **描述**  
---|---|---  
arg | Object | 订阅成功的频道  
> channel | String | 频道名  
> uid | String | 用户标识  
> algoId | String | 策略订单ID  
data | Array of objects | 订阅的数据  
> algoId | String | 策略订单ID  
> algoClOrdId | String | 用户自定义策略ID  
> instType | String | 产品类型  
> instId | String | 产品ID  
> algoOrdType | String | 策略订单类型  
`grid`：现货网格委托  
`contract_grid`：合约网格委托  
> groupId | String | 组ID  
> ordId | String | 子订单ID  
> cTime | String | 子订单创建时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
> uTime | String | 子订单更新时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
> tag | String | 订单标签  
> tdMode | String | 子订单交易模式  
`cross`：全仓 `isolated`：逐仓 `cash`：非保证金  
> ordType | String | 子订单类型  
`market`：市价单 `limit`：限价单  
`ioc`：立即成交并取消剩余  
> sz | String | 子订单委托数量  
> state | String | 子订单状态  
`canceled`：撤单成功 `live`：等待成交 `partially_filled`：部分成交 `filled`：完全成交 `cancelling`：撤单中  
> side | String | 子订单订单方向  
`buy`：买 `sell`：卖  
> px | String | 子订单委托价格  
> fee | String | 子订单手续费数量  
> feeCcy | String | 子订单手续费币种  
> rebate | String | 子订单返佣数量  
> rebateCcy | String | 子订单返佣币种  
> avgPx | String | 子订单平均成交价格  
> accFillSz | String | 子订单累计成交数量  
> posSide | String | 子订单持仓方向  
`net`：买卖模式  
> pnl | String | 子订单收益  
> ctVal | String | 合约面值  
> lever | String | 杠杆倍数  
> pTime | String | 订单信息的推送时间，Unix时间戳的毫秒数格式，如 `1597026383085`