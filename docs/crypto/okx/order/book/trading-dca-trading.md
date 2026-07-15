---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#order-book-trading-dca-trading
anchor_id: order-book-trading-dca-trading
api_type: API
updated_at: 2026-07-15 19:18:56.657352
---

# DCA Trading

A Martingale bot is a trading strategy that automatically adds to positions in batches as the market falls, thereby lowering the average holding cost. Users set the initial order amount, maximum number of safety orders, the price drop percentage that triggers each safety order, and the take-profit target. The bot will automatically place a buy order each time the price reaches a safety order condition, and close the position for profit once the price rebounds to the take-profit target.  
The API endpoints of `DCA Trading` require authentication.  
  
### POST / Place dca algo order

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
  
### POST / Amend spot dca basic param

#### Rate Limit: 20 requests per 2 seconds

#### Rate Limit Rule: User ID

#### Permission: Trade

#### HTTP Request

`POST /api/v5/tradingBot/dca/amend-order-algo`

> Request Example
    
    
    POST /api/v5/tradingBot/dca/amend-order-algo
    body
    {
        "algoId": "532177187189760000",
        "pxSteps": "0.02",
        "pxStepsMult": "2.0",
        "volMult": "2.0",
        "tpPct": "0.05",
        "slPct": "0.20",
        "initOrdAmt": "100",
        "safetyOrdAmt": "50",
        "maxSafetyOrds": "5",
        "reserveFunds": true,
        "triggerParams": [
            {
                "triggerAction": "start",
                "triggerStrategy": "instant"
            }
        ]
    }
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
algoId | String | Yes | Algo order ID  
pxSteps | String | Yes | Price step ratio (price gap to trigger the first safety order)  
pxStepsMult | String | Yes | Price step multiplier  
volMult | String | Yes | Amount multiplier  
tpPct | String | Yes | Take-profit target, e.g. `0.05` represents 5%  
slPct | String | Yes | Stop-loss target, e.g. `0.05` represents 5%  
initOrdAmt | String | Yes | Initial order amount (in quote currency)  
safetyOrdAmt | String | Yes | Safety order amount (in quote currency)  
maxSafetyOrds | String | Yes | Maximum number of safety orders  
reserveFunds | Boolean | Yes | Whether to reserve all funds  
`true`: reserve funds  
`false`: do not reserve funds  
triggerParams | Array of objects | Yes | Signal trigger parameters  
> triggerAction | String | No | Trigger action  
`start`: start the DCA bot  
> triggerStrategy | String | No | Trigger strategy  
`instant`: trigger immediately  
`rsi`: RSI indicator trigger  
> timeframe | String | No | Candlestick type  
`3m`, `5m`, `15m`, `30m` (`m` = minutes)  
`1H`, `4H` (`H` = hours)  
`1D` (`D` = days)  
Only valid when `triggerStrategy` is `rsi`  
> thold | String | No | Threshold, integer in range [1, 100]  
Only valid when `triggerStrategy` is `rsi`  
> triggerCond | String | No | Trigger condition  
`cross_up`: cross upward  
`cross_down`: cross downward  
`above`: above  
`below`: below  
`cross`: cross  
Only valid when `triggerStrategy` is `rsi`  
> timePeriod | String | No | Period, e.g. `14`  
Only valid when `triggerStrategy` is `rsi`  
  
> Response Example
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "algoId": "532177187189760000",
                "algoClOrdId": "",
                "sCode": "0",
                "sMsg": ""
            }
        ]
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
algoId | String | Algo order ID  
algoClOrdId | String | Client-supplied algo order ID  
sCode | String | Event execution status code, `0` indicates success  
sMsg | String | Error message if the event execution failed  
  
### POST / Stop dca algo order

#### Rate Limit: 20 requests per 2 seconds

#### Rate Limit Rule: User ID

#### Permission: Trade

#### HTTP Request

`POST /api/v5/tradingBot/dca/stop`

> Request Example
    
    
    POST /api/v5/tradingBot/dca/stop
    body
    {
        "algoOrdType": "contract_dca",
        "algoId": "448965992920907776",
        "stopType": "1"
    }
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
algoId | String | Yes | Algo ID  
algoOrdType | String | Yes | Algo order type  
`contract_dca`: Contract DCA order  
`spot_dca`: Spot DCA order  
stopType | String | Yes | Stop type  
`contract_dca`: `1`: Market close all positions, `2`: Keep positions  
`spot_dca`: `1`: Sell base currency, `2`: Keep base currency  
  
> Response Example
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "algoId": "448965992920907776",
                "sCode": "0",
                "sMsg": ""
            }
        ]
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
algoId | String | Algo ID  
tag | String | Order tag  
algoClOrdId | String | Client-supplied Algo ID  
sCode | String | The code of the event execution result, 0 means success  
sMsg | String | Rejection message if the request is unsuccessful  
  
### GET / DCA algo order details

#### Rate Limit: 20 requests per 2 seconds

#### Rate Limit Rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/tradingBot/dca/ongoing-list`

> Request Example
    
    
    GET /api/v5/tradingBot/dca/ongoing-list?algoOrdType=contract_dca&limit=20
    

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
                "algoId": "565849588675117056",
                "algoOrdType": "contract_dca",
                "instId": "BTC-USDT-SWAP",
                "copyType": "0",
                "state": "running",
                "direction": "long",
                "lever": "3",
                "initOrdAmt": "100",
                "safetyOrdAmt": "200",
                "maxSafetyOrds": "5",
                "pxSteps": "0.02",
                "pxStepsMult": "1",
                "volMult": "1",
                "tpPxRange": "",
                "slPct": "",
                "slMode": "",
                "allowReinvest": true,
                "totalPnl": "12.5",
                "pnlRatio": "0.05",
                "totalFundingFee": "-0.5",
                "investmentAmt": "500",
                "investmentCcy": "USDT",
                "arbitragePnL": "2.1",
                "profitSharingRatio": "",
                "trackingMode": "",
                "triggerParams": [
                    {
                        "triggerAction": "start",
                        "triggerStrategy": "instant"
                    }
                ],
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
tpPxRange | String | Take-profit price limit  
For Long DCA, the take-profit price must not be lower than the minimum threshold; for Short DCA, the take-profit price must not exceed the maximum threshold  
Only applicable to `contract_dca`  
slPct | String | Stop-loss target, e.g. `0.05` represents 5%  
slMode | String | Stop-loss mode  
`limit`: Limit order  
`market`: Market order  
allowReinvest | Boolean | Whether to reinvest profit  
`true` or `false`  
totalPnl | String | Total PnL  
pnlRatio | String | PnL ratio  
totalFundingFee | String | Total funding fee  
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
cTime | String | Algo order created time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
uTime | String | Algo order updated time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
ctVal | String | Contract value  
Only applicable to `contract_dca`  
tradeQuoteCcy | String | Quote currency for trading  
Only applicable to `spot_dca`  
  
### GET / DCA algo order history

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
  
### GET / DCA sub orders

#### Rate Limit: 20 requests per 2 seconds

#### Rate Limit Rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/tradingBot/dca/orders`

> Request Example
    
    
    GET /api/v5/tradingBot/dca/orders?algoId=2833925189933756416&algoOrdType=contract_dca
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
algoId | String | Yes | Algo ID  
algoOrdType | String | Yes | Algo order type  
`contract_dca`: Contract DCA order  
`spot_dca`: Spot DCA order  
cycleId | String | No | Cycle ID  
after | String | No | Pagination of data to return records earlier than the requested `ordId`  
before | String | No | Pagination of data to return records newer than the requested `ordId`  
limit | String | No | Number of results per request. The maximum is 100. The default is 100  
  
> Response Example
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "cycleId": "9876543",
                "ordId": "570627699870375936",
                "avgFillPx": "41500",
                "direction": "long",
                "side": "buy",
                "ordType": "init_order",
                "px": "41000",
                "sz": "10",
                "filledSz": "10",
                "state": "filled",
                "fee": "-0.2",
                "rebate": "0",
                "rebateCcy": "USDT",
                "lever": "3",
                "instId": "BTC-USDT-SWAP",
                "ctVal": "0.01",
                "fillTime": "1597026383085",
                "cTime": "1597026383085",
                "uTime": "1597026383085",
                "tradeQuoteCcy": ""
            }
        ]
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
cycleId | String | Cycle ID  
ordId | String | Sub order ID  
avgFillPx | String | Average filled price  
direction | String | Position direction  
Contract DCA: `long`: Long position, `short`: Short position  
Spot DCA: `long`: Long position  
side | String | Order side  
`buy`  
`sell`  
ordType | String | Sub order type  
`init_order`: Initial order  
`safety_order`: Safety order  
`tp_order`: Take-profit order  
`sl_order`: Stop-loss order  
`manual_add_order`: Manually added order  
`close_position`: Close position order  
`manual_close_position`: Manual close position order  
px | String | Order price  
sz | String | Order size  
filledSz | String | Filled size  
state | String | Order status  
`live`: Pending fill  
`partially_filled`: Partially filled  
`filled`: Fully filled  
`canceled`: Canceled  
`cancelling`: Cancelling  
fee | String | Accumulated fee  
Negative number represents the user transaction fee charged by the platform. Positive number represents rebate.  
rebate | String | Rebate amount  
rebateCcy | String | Rebate currency  
lever | String | Leverage  
Only applicable to `contract_dca`  
instId | String | Instrument ID, e.g. `BTC-USDT-SWAP`  
ctVal | String | Contract value  
Only applicable to `contract_dca`  
fillTime | String | Last filled time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
cTime | String | Order created time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
uTime | String | Order updated time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
tradeQuoteCcy | String | Quote currency for trading  
Only applicable to `spot_dca`  
  
### POST / Add investment

#### Rate Limit: 20 requests per 2 seconds

#### Rate Limit Rule: User ID

#### Permission: Trade

#### HTTP Request

`POST /api/v5/tradingBot/dca/orders/manual-buy`

> Request Example
    
    
    POST /api/v5/tradingBot/dca/orders/manual-buy
    body
    {
        "algoId": "2833925189933756416",
        "algoOrdType": "contract_dca",
        "price": "41000",
        "amt": "100"
    }
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
algoId | String | Yes | Algo ID  
algoOrdType | String | Yes | Algo order type  
`contract_dca`: Contract DCA order  
`spot_dca`: Spot DCA order  
price | String | Yes | Manual added order limit price  
amt | String | Yes | Amount  
ordType | String | No | Order type  
`limit`: Limit order  
`market`: Market order  
Only applicable to `spot_dca`  
tradeQuoteCcy | String | No | Quote currency for trading  
Only applicable to `spot_dca`  
  
> Response Example
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "algoId": "2833925189933756416",
                "algoClOrdId": "",
                "algoOrdType": "contract_dca",
                "tag": "",
                "diffAmount": "100",
                "sCode": "0",
                "sMsg": ""
            }
        ]
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
algoId | String | Algo ID  
algoClOrdId | String | Client-supplied Algo ID  
algoOrdType | String | Algo order type  
`contract_dca`: Contract DCA order  
`spot_dca`: Spot DCA order  
tag | String | Order tag  
diffAmount | String | Extra amount transferred from trading account  
Only applicable to `contract_dca`  
sCode | String | The code of the event execution result, 0 means success  
sMsg | String | Rejection message if the request is unsuccessful  
  
### POST / Amend dca reinvestment

#### Rate Limit: 20 requests per 2 seconds

#### Rate Limit Rule: User ID

#### Permission: Trade

#### HTTP Request

`POST /api/v5/tradingBot/dca/settings/reinvestment`

> Request Example
    
    
    POST /api/v5/tradingBot/dca/settings/reinvestment
    body
    {
        "algoId": "2833925189933756416",
        "algoOrdType": "contract_dca",
        "allowReinvest": true
    }
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
algoId | String | Yes | Algo ID  
algoOrdType | String | Yes | Algo order type  
`contract_dca`: Contract DCA order  
allowReinvest | Boolean | Yes | Whether to reinvest profit  
`true` or `false`  
  
> Response Example
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "algoId": "2833925189933756416",
                "algoOrdType": "contract_dca",
                "sCode": "0",
                "sMsg": ""
            }
        ]
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
algoId | String | Algo ID  
algoOrdType | String | Algo order type  
`contract_dca`: Contract DCA order  
sCode | String | The code of the event execution result, 0 means success  
sMsg | String | Rejection message if the request is unsuccessful  
  
### POST / Amend dca take profit settings

#### Rate Limit: 20 requests per 2 seconds

#### Rate Limit Rule: User ID

#### Permission: Trade

#### HTTP Request

`POST /api/v5/tradingBot/dca/settings/take-profit`

> Request Example
    
    
    POST /api/v5/tradingBot/dca/settings/take-profit
    body
    {
        "algoId": "2833925189933756416",
        "algoOrdType": "contract_dca",
        "tpPrice": "43500"
    }
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
algoId | String | Yes | Algo order ID  
algoOrdType | String | Yes | Algo order type  
`contract_dca`: Contract DCA order  
tpPrice | String | Yes | Take-profit price  
  
> Response Example
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "algoId": "2833925189933756416",
                "algoOrdType": "contract_dca",
                "sCode": "0",
                "sMsg": ""
            }
        ]
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
algoId | String | Algo order ID  
algoOrdType | String | Algo order type  
`contract_dca`: Contract DCA order  
sCode | String | Event execution status code, `0` indicates success  
sMsg | String | Error message if the event execution failed  
  
### Get / DCA algo order position details

#### Rate Limit: 20 requests per 2 seconds

#### Rate Limit Rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/tradingBot/dca/position-details`

> Request Example
    
    
    GET /api/v5/tradingBot/dca/position-details?algoId=2833925189933756416&algoOrdType=contract_dca
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
algoId | String | Yes | Algo order ID  
algoOrdType | String | Yes | Algo order type  
`contract_dca`: Contract DCA order  
`spot_dca`: Spot DCA order  
  
> Response Example
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "algoId": "2833925189933756416",
                "algoClOrdId": "",
                "algoOrdType": "contract_dca",
                "instId": "BTC-USDT-SWAP",
                "curCycleld": "3",
                "startTime": "1597026383085",
                "fillManualOrds": "0",
                "fillSafetyOrds": "2",
                "fundingFee": "-0.05",
                "initPx": "43200",
                "notionalUsd": "5000",
                "avgPx": "43000",
                "upl": "12.5",
                "liqPx": "38000",
                "sz": "2",
                "baseSz": "",
                "quoteSz": "",
                "slPx": "40000",
                "tpPx": "45000",
                "fee": "-0.2",
                "tradeQuoteCcy": ""
            }
        ]
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
algoId | String | Algo order ID  
algoClOrdId | String | Client-supplied algo order ID  
algoOrdType | String | Algo order type  
`contract_dca`: Contract DCA order  
`spot_dca`: Spot DCA order  
instId | String | Instrument ID, e.g. `BTC-USDT-SWAP`  
curCycleld | String | The cycle ID for the current cycle  
startTime | String | Start time of the current cycle, Unix timestamp in milliseconds, e.g. `1597026383085`  
fillManualOrds | String | Number of filled manually added orders in the current cycle  
fillSafetyOrds | String | Number of filled safety orders in the current cycle  
fundingFee | String | Accumulated funding fee for the current cycle  
Only applicable to `contract_dca`  
initPx | String | Initial order average open price  
notionalUsd | String | Notional value of positions in USD  
Only applicable to `contract_dca`  
avgPx | String | Average open price  
upl | String | Unrealized PnL  
liqPx | String | Estimated liquidation price  
Only applicable to `contract_dca`  
sz | String | Position size in number of contracts  
Only applicable to `contract_dca`  
baseSz | String | Amount of base currency held in the current cycle  
Only applicable to `spot_dca`  
quoteSz | String | Amount of quote currency held in the current cycle  
Only applicable to `spot_dca`  
slPx | String | Stop-loss price  
tpPx | String | Take-profit price  
fee | String | Accumulated fee. Negative number represents the transaction fee charged by the platform. Positive number represents rebate.  
tradeQuoteCcy | String | The quote currency for trading  
Only applicable to `spot_dca`  
  
### GET / DCA cycle list

#### Rate Limit: 20 requests per 2 seconds

#### Rate Limit Rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/tradingBot/dca/cycle-list`

> Request Example
    
    
    GET /api/v5/tradingBot/dca/cycle-list?algoId=2833925189933756416&algoOrdType=contract_dca
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
algoId | String | Yes | Algo ID  
algoOrdType | String | Yes | Algo order type  
`contract_dca`: Contract DCA order  
`spot_dca`: Spot DCA order  
instId | String | No | Instrument ID  
after | String | No | Pagination of data to return records earlier than the requested `cycleId`  
before | String | No | Pagination of data to return records newer than the requested `cycleId`  
limit | String | No | Number of results per request. The maximum is 100. The default is 100  
  
> Response Example
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "algoId": "2833925189933756416",
                "algoClOrdId": "",
                "cycleId": "9876543",
                "currentCycle": true,
                "realizedPnl": "12.5",
                "startTime": "1597026383085",
                "endTime": "",
                "fee": "-0.3",
                "avgPx": "41500",
                "tpPx": "43000"
            }
        ]
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
algoId | String | Algo ID  
algoClOrdId | String | Client-supplied Algo ID  
cycleId | String | Cycle ID  
currentCycle | Boolean | Whether it is the current cycle  
`true` or `false`  
realizedPnl | String | Realized PnL  
startTime | String | Cycle start time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
endTime | String | Cycle end time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
fee | String | Accumulated fee in the cycle  
Negative number represents the user transaction fee charged by the platform. Positive number represents rebate.  
avgPx | String | Average open price  
tpPx | String | Take-profit price  
  
### POST / Add dca margin

#### Rate Limit: 20 requests per 2 seconds

#### Rate Limit Rule: User ID

#### Permission: Trade

#### HTTP Request

`POST /api/v5/tradingBot/dca/margin/add`

> Request Example
    
    
    POST /api/v5/tradingBot/dca/margin/add
    body
    {
        "algoId": "2833925189933756416",
        "amt": "50"
    }
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
algoId | String | Yes | Algo order ID  
amt | String | Yes | Margin add amount  
  
> Response Example
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "algoId": "2833925189933756416",
                "algoOrdType": "contract_dca",
                "sCode": "0",
                "sMsg": ""
            }
        ]
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
algoId | String | Algo order ID  
algoOrdType | String | Algo order type  
`contract_dca`: Contract DCA order  
sCode | String | Event execution status code, `0` indicates success  
sMsg | String | Error message if the event execution failed  
  
### POST / Reduce dca margin

#### Rate Limit: 20 requests per 2 seconds

#### Rate Limit Rule: User ID

#### Permission: Trade

#### HTTP Request

`POST /api/v5/tradingBot/dca/margin/reduce`

> Request Example
    
    
    POST /api/v5/tradingBot/dca/margin/reduce
    body
    {
        "algoId": "2833925189933756416",
        "amt": "50"
    }
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
algoId | String | Yes | Algo order ID  
amt | String | Yes | Margin reduction amount  
  
> Response Example
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "algoId": "2833925189933756416",
                "algoOrdType": "contract_dca",
                "sCode": "0",
                "sMsg": ""
            }
        ]
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
algoId | String | Algo order ID  
algoOrdType | String | Algo order type  
`contract_dca`: Contract DCA order  
sCode | String | Event execution status code, `0` indicates success  
sMsg | String | Error message if the event execution failed

---

# 马丁交易

马丁策略是一种通过在市场下跌时自动分批加仓来摊低持仓均价的交易策略。用户设定首单金额、最大加仓次数、每次加仓的触发跌幅及止盈比例后，策略将在价格每次达到加仓条件时自动买入，待价格反弹至止盈目标时自动平仓获利。  
`马丁交易`功能模块下的API接口需要身份验证。  
  
### POST / 马丁策略委托下单 

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
  
### POST / 现货DCA编辑参数

#### 限速：20次/2s

#### 限速规则：User ID

#### 权限：交易

#### HTTP请求

`POST /api/v5/tradingBot/dca/amend-order-algo`

> 请求示例
    
    
    POST /api/v5/tradingBot/dca/amend-order-algo
    body
    {
        "algoId": "532177187189760000",
        "pxSteps": "0.02",
        "pxStepsMult": "2.0",
        "volMult": "2.0",
        "tpPct": "0.05",
        "slPct": "0.20",
        "initOrdAmt": "100",
        "safetyOrdAmt": "50",
        "maxSafetyOrds": "5",
        "reserveFunds": true,
        "triggerParams": [
            {
                "triggerAction": "start",
                "triggerStrategy": "instant"
            }
        ]
    }
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
algoId | String | 是 | 策略ID  
pxSteps | String | 是 | 价差比例（第一次加仓触发价格差）  
pxStepsMult | String | 是 | 价差放大倍数  
volMult | String | 是 | 金额放大倍数  
tpPct | String | 是 | 止盈目标，0.05 表示 5%  
slPct | String | 是 | 止损目标，0.05 表示 5%  
initOrdAmt | String | 是 | 初始订单金额（计价货币）  
safetyOrdAmt | String | 是 | 加仓单金额（计价货币）  
maxSafetyOrds | String | 是 | 最大加仓次数  
reserveFunds | Boolean | 是 | 是否预留全部资金  
`true`：预留资金  
`false`：不预留资金  
triggerParams | Array of objects | 是 | 信号触发参数  
> triggerAction | String | 否 | 触发行为  
`start`：马丁启动  
> triggerStrategy | String | 否 | 触发策略  
`instant`：立即触发  
`rsi`：RSI 指标触发  
> timeframe | String | 否 | K线种类  
`3m`, `5m`, `15m`, `30m`（`m` 代表分钟）  
`1H`, `4H`（`H` 代表小时）  
`1D`（`D` 代表天）  
该字段只在 `triggerStrategy` 为 `rsi` 时有效  
> thold | String | 否 | 阈值，取值 [1, 100] 的整数  
该字段只在 `triggerStrategy` 为 `rsi` 时有效  
> triggerCond | String | 否 | 触发条件  
`cross_up`：上穿  
`cross_down`：下穿  
`above`：上方  
`below`：下方  
`cross`：交叉  
该字段只在 `triggerStrategy` 为 `rsi` 时有效  
> timePeriod | String | 否 | 周期，如 `14`  
该字段只在 `triggerStrategy` 为 `rsi` 时有效  
  
> 返回结果
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "algoId": "532177187189760000",
                "algoClOrdId": "",
                "sCode": "0",
                "sMsg": ""
            }
        ]
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
algoId | String | 策略ID  
algoClOrdId | String | 客户端自定义策略单ID  
sCode | String | 事件执行结果的code，0代表成功  
sMsg | String | 事件执行失败时的msg  
  
### POST / 停止马丁策略委托订单 

#### 限速：20次/2s

#### 限速规则：User ID

#### 权限：交易

#### HTTP请求

`POST /api/v5/tradingBot/dca/stop`

> 请求示例
    
    
    POST /api/v5/tradingBot/dca/stop
    body
    {
        "algoOrdType": "contract_dca",
        "algoId": "448965992920907776",
        "stopType": "1"
    }
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
algoId | String | 是 | 策略ID  
algoOrdType | String | 是 | 策略订单类型  
`contract_dca`：合约马丁委托  
`spot_dca`：现货马丁委托  
stopType | String | 是 | 停止类型  
合约马丁：`1`：市价全平，`2`：停止但不平仓  
现货马丁：`1`：停止并卖出币，`2`：停止但不卖出币  
  
> 返回结果
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "algoId": "448965992920907776",
                "sCode": "0",
                "sMsg": ""
            }
        ]
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
algoId | String | 策略ID  
tag | String | 订单标签  
algoClOrdId | String | 客户端自定义策略单ID  
sCode | String | 事件执行结果的code，0代表成功  
sMsg | String | 事件执行失败时的msg  
  
### GET / 获取进行中马丁策略委托单列表 

#### 限速：20次/2s

#### 限速规则：User ID

#### 权限：读取

#### HTTP请求

`GET /api/v5/tradingBot/dca/ongoing-list`

> 请求示例
    
    
    GET /api/v5/tradingBot/dca/ongoing-list?algoOrdType=contract_dca&limit=20
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
algoOrdType | String | 是 | 策略订单类型  
`contract_dca`：合约马丁委托  
`spot_dca`：现货马丁委托  
algoId | String | 否 | 策略ID  
after | String | 否 | 请求此ID之前（更旧的数据）的分页内容，传的值为对应接口的 `algoId`  
before | String | 否 | 请求此ID之后（更新的数据）的分页内容，传的值为对应接口的 `algoId`  
limit | String | 否 | 返回结果的数量，最大为100，默认100条  
  
> 返回结果
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "algoId": "565849588675117056",
                "algoOrdType": "contract_dca",
                "instId": "BTC-USDT-SWAP",
                "copyType": "0",
                "state": "running",
                "direction": "long",
                "lever": "3",
                "initOrdAmt": "100",
                "safetyOrdAmt": "200",
                "maxSafetyOrds": "5",
                "pxSteps": "0.02",
                "pxStepsMult": "1",
                "volMult": "1",
                "tpPxRange": "",
                "slPct": "",
                "slMode": "",
                "allowReinvest": true,
                "totalPnl": "12.5",
                "pnlRatio": "0.05",
                "totalFundingFee": "-0.5",
                "investmentAmt": "500",
                "investmentCcy": "USDT",
                "arbitragePnL": "2.1",
                "profitSharingRatio": "",
                "trackingMode": "",
                "triggerParams": [
                    {
                        "triggerAction": "start",
                        "triggerStrategy": "instant"
                    }
                ],
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
tpPxRange | String | 止盈价格限制  
做多时止盈价格不得低于系统最小阈值；做空时不得高于最大阈值  
仅适用于 `contract_dca`  
slPct | String | 止损目标，如 `0.05` 表示 5%  
slMode | String | 止损模式  
`limit`：限价  
`market`：市价  
allowReinvest | Boolean | 是否复投利润  
`true` 或 `false`  
totalPnl | String | 总收益  
pnlRatio | String | 收益率  
totalFundingFee | String | 累计资金费用  
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
cTime | String | 订单创建时间，Unix 时间戳毫秒数，如 `1597026383085`  
uTime | String | 订单更新时间，Unix 时间戳毫秒数，如 `1597026383085`  
ctVal | String | 合约面值  
仅适用于 `contract_dca`  
tradeQuoteCcy | String | 指定交易计价货币  
仅适用于 `spot_dca`  
  
### GET / 获取历史马丁策略委托单列表 

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
  
### GET / 获取马丁策略子订单列表 

#### 限速：20次/2s

#### 限速规则：User ID

#### 权限：读取

#### HTTP请求

`GET /api/v5/tradingBot/dca/orders`

> 请求示例
    
    
    GET /api/v5/tradingBot/dca/orders?algoId=2833925189933756416&algoOrdType=contract_dca
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
algoId | String | 是 | 策略订单 ID  
algoOrdType | String | 是 | 策略订单类型  
`contract_dca`：合约马丁委托  
`spot_dca`：现货马丁委托  
cycleId | String | 否 | 策略周期 ID  
after | String | 否 | 请求此ID之前（更旧的数据）的分页内容，传的值为对应接口的 `ordId`  
before | String | 否 | 请求此ID之后（更新的数据）的分页内容，传的值为对应接口的 `ordId`  
limit | String | 否 | 返回结果的数量，最大为100，默认100条  
  
> 返回结果
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "cycleId": "9876543",
                "ordId": "570627699870375936",
                "avgFillPx": "41500",
                "direction": "long",
                "side": "buy",
                "ordType": "init_order",
                "px": "41000",
                "sz": "10",
                "filledSz": "10",
                "state": "filled",
                "fee": "-0.2",
                "rebate": "0",
                "rebateCcy": "USDT",
                "lever": "3",
                "instId": "BTC-USDT-SWAP",
                "ctVal": "0.01",
                "fillTime": "1597026383085",
                "cTime": "1597026383085",
                "uTime": "1597026383085",
                "tradeQuoteCcy": ""
            }
        ]
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
cycleId | String | 策略周期 ID  
ordId | String | 子订单 ID  
avgFillPx | String | 子订单平均成交价格  
direction | String | 持仓方向  
合约马丁类型：`long`：多仓，`short`：空仓  
现货马丁类型：`long`：做多  
side | String | 子订单方向  
`buy`：买  
`sell`：卖  
ordType | String | 子订单类型  
`init_order`：初始订单  
`safety_order`：加仓订单  
`tp_order`：止盈单  
`sl_order`：止损单  
`manual_add_order`：手动加仓单  
`close_position`：平仓单  
`manual_close_position`：手动平仓单  
px | String | 子订单委托价格  
sz | String | 子订单委托数量  
filledSz | String | 子订单成交数量  
state | String | 子订单状态  
`live`：等待成交  
`partially_filled`：部分成交  
`filled`：完全成交  
`canceled`：撤单成功  
`cancelling`：撤单中  
fee | String | 子订单手续费数量  
rebate | String | 子订单返佣数量  
rebateCcy | String | 子订单返佣币种  
lever | String | 杠杆倍数  
仅适用于 `contract_dca`  
instId | String | 产品 ID，如 `BTC-USDT-SWAP`  
ctVal | String | 合约面值  
仅适用于 `contract_dca`  
fillTime | String | 子订单成交时间，Unix 时间戳毫秒数，如 `1597026383085`  
cTime | String | 子订单创建时间，Unix 时间戳毫秒数，如 `1597026383085`  
uTime | String | 子订单更新时间，Unix 时间戳毫秒数，如 `1597026383085`  
tradeQuoteCcy | String | 指定交易计价货币  
仅适用于 `spot_dca`  
  
### POST / 手动加仓 

#### 限速：20次/2s

#### 限速规则：User ID

#### 权限：交易

#### HTTP请求

`POST /api/v5/tradingBot/dca/orders/manual-buy`

> 请求示例
    
    
    POST /api/v5/tradingBot/dca/orders/manual-buy
    body
    {
        "algoId": "2833925189933756416",
        "algoOrdType": "contract_dca",
        "price": "41000",
        "amt": "100"
    }
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
algoId | String | 是 | 策略订单 ID  
algoOrdType | String | 是 | 策略订单类型  
`contract_dca`：合约马丁委托  
`spot_dca`：现货马丁委托  
price | String | 是 | 加仓价格  
amt | String | 是 | 增加的投资额  
ordType | String | 否 | 订单类型  
`limit`：限价单  
`market`：市价单  
仅适用于 `spot_dca`  
tradeQuoteCcy | String | 否 | 指定交易计价货币  
仅适用于 `spot_dca`  
  
> 返回结果
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "algoId": "2833925189933756416",
                "algoClOrdId": "",
                "algoOrdType": "contract_dca",
                "tag": "",
                "diffAmount": "100",
                "sCode": "0",
                "sMsg": ""
            }
        ]
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
algoId | String | 策略订单 ID  
algoClOrdId | String | 客户端自定义策略单ID  
algoOrdType | String | 策略订单类型  
`contract_dca`：合约马丁委托  
`spot_dca`：现货马丁委托  
tag | String | 订单标签  
diffAmount | String | 手动加仓转入虚拟子账户的资金  
仅适用于 `contract_dca`  
sCode | String | 事件执行结果的 code，0 代表成功  
sMsg | String | 事件执行失败时的 msg  
  
### POST / 修改复投设置 

#### 限速：20次/2s

#### 限速规则：User ID

#### 权限：交易

#### HTTP请求

`POST /api/v5/tradingBot/dca/settings/reinvestment`

> 请求示例
    
    
    POST /api/v5/tradingBot/dca/settings/reinvestment
    body
    {
        "algoId": "2833925189933756416",
        "algoOrdType": "contract_dca",
        "allowReinvest": false
    }
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
algoId | String | 是 | 策略订单 ID  
algoOrdType | String | 是 | 策略订单类型  
`contract_dca`：合约马丁委托  
allowReinvest | Boolean | 是 | 是否复投利润  
`true` 或 `false`  
  
> 返回结果
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "algoId": "2833925189933756416",
                "algoOrdType": "contract_dca",
                "sCode": "0",
                "sMsg": ""
            }
        ]
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
algoId | String | 策略订单 ID  
algoOrdType | String | 策略订单类型  
`contract_dca`：合约马丁委托  
sCode | String | 事件执行结果的 code，0 代表成功  
sMsg | String | 事件执行失败时的 msg  
  
### POST / 修改止盈参数 

#### 限速：20次/2s

#### 限速规则：User ID

#### 权限：交易

#### HTTP请求

`POST /api/v5/tradingBot/dca/settings/take-profit`

> 请求示例
    
    
    POST /api/v5/tradingBot/dca/settings/take-profit
    body
    {
        "algoId": "2833925189933756416",
        "algoOrdType": "contract_dca",
        "tpPrice": "43500"
    }
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
algoId | String | 是 | 策略订单 ID  
algoOrdType | String | 是 | 策略订单类型  
`contract_dca`：合约马丁委托  
tpPrice | String | 是 | 止盈价格  
  
> 返回结果
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "algoId": "2833925189933756416",
                "algoOrdType": "contract_dca",
                "sCode": "0",
                "sMsg": ""
            }
        ]
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
algoId | String | 策略订单 ID  
algoOrdType | String | 策略订单类型  
`contract_dca`：合约马丁委托  
sCode | String | 事件执行结果的 code，0 代表成功  
sMsg | String | 事件执行失败时的 msg  
  
### GET / 获取马丁策略委托持仓 

#### 限速：20次/2s

#### 限速规则：User ID

#### 权限：读取

#### HTTP请求

`GET /api/v5/tradingBot/dca/position-details`

> 请求示例
    
    
    GET /api/v5/tradingBot/dca/position-details?algoId=2833925189933756416&algoOrdType=contract_dca
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
algoId | String | 是 | 策略订单 ID  
algoOrdType | String | 是 | 策略订单类型  
`contract_dca`：合约马丁委托  
`spot_dca`：现货马丁委托  
  
> 返回结果
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "algoId": "2833925189933756416",
                "algoClOrdId": "",
                "algoOrdType": "contract_dca",
                "instId": "BTC-USDT-SWAP",
                "curCycleld": "3",
                "startTime": "1597026383085",
                "fillManualOrds": "0",
                "fillSafetyOrds": "2",
                "fundingFee": "-0.05",
                "initPx": "43200",
                "notionalUsd": "5000",
                "avgPx": "43000",
                "upl": "12.5",
                "liqPx": "38000",
                "sz": "2",
                "baseSz": "",
                "quoteSz": "",
                "slPx": "40000",
                "tpPx": "45000",
                "fee": "-0.2",
                "tradeQuoteCcy": ""
            }
        ]
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
algoId | String | 策略订单 ID  
algoClOrdId | String | 客户端自定义策略单ID  
algoOrdType | String | 策略订单类型  
`contract_dca`：合约马丁委托  
`spot_dca`：现货马丁委托  
instId | String | 产品ID，如 `BTC-USDT`  
curCycleld | String | 正在运行中的周期 ID  
startTime | String | 当轮周期开启时间，Unix 时间戳的毫秒数格式，如 `1597026383085`  
fillManualOrds | String | 周期手动加仓次数  
fillSafetyOrds | String | 周期已加仓次数  
fundingFee | String | 当轮周期累计资金费用  
仅适用于 `contract_dca`  
initPx | String | 初始订单开仓均价或初始订单成交价  
notionalUsd | String | 仓位美金价值  
仅适用于 `contract_dca`  
avgPx | String | 开仓均价  
upl | String | 未实现收益  
liqPx | String | 预估强平价  
仅适用于 `contract_dca`  
sz | String | 合约数量  
仅适用于 `contract_dca`  
baseSz | String | 当前周期持有的交易币数量  
仅适用于 `spot_dca`  
quoteSz | String | 当前周期持有的计价币数量  
仅适用于 `spot_dca`  
slPx | String | 止损价格  
tpPx | String | 止盈价格  
fee | String | 累计手续费金额，正数代表平台返佣，负数代表平台扣除  
tradeQuoteCcy | String | 指定交易计价货币  
仅适用于 `spot_dca`  
  
### GET / 获取马丁周期列表 

#### 限速：20次/2s

#### 限速规则：User ID

#### 权限：读取

#### HTTP请求

`GET /api/v5/tradingBot/dca/cycle-list`

> 请求示例
    
    
    GET /api/v5/tradingBot/dca/cycle-list?algoId=2833925189933756416&algoOrdType=contract_dca
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
algoId | String | 是 | 策略订单 ID  
algoOrdType | String | 是 | 策略订单类型  
`contract_dca`：合约马丁委托  
`spot_dca`：现货马丁委托  
instId | String | 否 | 产品 ID  
after | String | 否 | 请求此ID之前（更旧的数据）的分页内容，传的值为对应接口的 `cycleId`  
before | String | 否 | 请求此ID之后（更新的数据）的分页内容，传的值为对应接口的 `cycleId`  
limit | String | 否 | 返回结果的数量，最大为100，默认100条  
  
> 返回结果
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "algoId": "2833925189933756416",
                "algoClOrdId": "",
                "cycleId": "9876543",
                "currentCycle": true,
                "realizedPnl": "12.5",
                "startTime": "1597026383085",
                "endTime": "",
                "fee": "-0.3",
                "avgPx": "41500",
                "tpPx": "43000"
            }
        ]
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
algoId | String | 策略订单 ID  
algoClOrdId | String | 客户端自定义策略单ID  
cycleId | String | 策略周期 ID  
currentCycle | Boolean | 是否是当轮周期  
`true` 或 `false`  
realizedPnl | String | 已实现盈亏  
startTime | String | 周期开启时间，Unix 时间戳毫秒数，如 `1597026383085`  
endTime | String | 周期结束时间，Unix 时间戳毫秒数，如 `1597026383085`  
fee | String | 累计手续费金额，正数代表平台返佣，负数代表平台扣除  
avgPx | String | 开仓均价  
tpPx | String | 止盈价格  
  
### POST / 增加保证金 

#### 限速：20次/2s

#### 限速规则：User ID

#### 权限：交易

#### HTTP请求

`POST /api/v5/tradingBot/dca/margin/add`

> 请求示例
    
    
    POST /api/v5/tradingBot/dca/margin/add
    body
    {
        "algoId": "2833925189933756416",
        "amt": "50"
    }
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
algoId | String | 是 | 策略订单 ID  
amt | String | 是 | 增加的保证金金额  
  
> 返回结果
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "algoId": "2833925189933756416",
                "algoOrdType": "contract_dca",
                "sCode": "0",
                "sMsg": ""
            }
        ]
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
algoId | String | 策略订单 ID  
algoOrdType | String | 策略订单类型  
`contract_dca`：合约马丁委托  
sCode | String | 事件执行结果的 code，0 代表成功  
sMsg | String | 事件执行失败时的 msg  
  
### POST / 减少保证金 

#### 限速：20次/2s

#### 限速规则：User ID

#### 权限：交易

#### HTTP请求

`POST /api/v5/tradingBot/dca/margin/reduce`

> 请求示例
    
    
    POST /api/v5/tradingBot/dca/margin/reduce
    body
    {
        "algoId": "2833925189933756416",
        "amt": "50"
    }
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
algoId | String | 是 | 策略订单 ID  
amt | String | 是 | 减少的保证金金额  
  
> 返回结果
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "algoId": "2833925189933756416",
                "algoOrdType": "contract_dca",
                "sCode": "0",
                "sMsg": ""
            }
        ]
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
algoId | String | 策略订单 ID  
algoOrdType | String | 策略订单类型  
`contract_dca`：合约马丁委托  
sCode | String | 事件执行结果的 code，0 代表成功  
sMsg | String | 事件执行失败时的 msg