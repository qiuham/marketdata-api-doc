---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#order-book-trading-signal-bot-trading
anchor_id: order-book-trading-signal-bot-trading
api_type: API
updated_at: 2026-07-05 19:33:56.498448
---

# Signal bot trading

Create and customize your own signals while gaining access to a diverse selection of signals from top providers. Empower your trading strategies and stay ahead of the game with our comprehensive signal trading platform. [Learn more](/learn/signal-trading)  
  
### POST / Create signal

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Trade

#### HTTP Request

`POST /api/v5/tradingBot/signal/create-signal`

> Request Example
    
    
    POST /api/v5/tradingBot/signal/create-signal
    body
    {
      "signalChanName": "long short",
      "signalDesc": "this is the first version"
    }
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
signalChanName | String | Yes | Signal channel name  
signalChanDesc | String | No | Signal channel description  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
           {
               "signalChanId" :"572112109",
               "signalChanToken":"dojuckew331lkx"
           }
    
        ],
        "msg": ""
    }
    
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
signalChanId | String | Signal channel Id  
signalChanToken | String | User identify when placing orders via signal  
  
### GET / Signals

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/tradingBot/signal/signals`

> Request Example
    
    
    GET /api/v5/tradingBot/signal/signals?signalSourceType=1
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
signalSourceType | String | Yes | Signal source type  
`1`: Created by yourself  
`2`: Subscribe  
`3`: Free signal  
signalChanId | String | No | Signal channel id  
after | String | No | Pagination of data to return records `signalChanId` earlier than the requested timestamp, Unix timestamp format in milliseconds, e.g. `1597026383085`  
before | String | No | Pagination of data to return records `signalChanId` newer than the requested timestamp, Unix timestamp format in milliseconds, e.g. `1597026383085`  
limit | String | No | Number of results per request. The maximum is 100. The default is 100.  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "signalChanId": "623833708424069120",
                "signalChanName": "test",
                "signalChanDesc": "test",
                "signalChanToken": "test",
                "signalSourceType": "1"
            }
        ],
        "msg": ""
    }
    
    
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
signalChanId | String | Signal channel id  
signalChanName | String | Signal channel name  
signalChanDesc | String | Signal channel description  
signalChanToken | String | User identify when placing orders via signal  
signalSourceType | String | Signal source type  
`1`: Created by yourself  
`2`: Subscribe  
`3`: Free signal  
  
### POST / Create signal bot

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Trade

#### HTTP Request

`POST /api/v5/tradingBot/signal/order-algo`

> Request Example
    
    
    # Create signal bot
    POST /api/v5/tradingBot/signal/order-algo
    body
    {
      "signalChanId": "627921182788161536",
      "instIds": [
        "BTC-USDT-SWAP",
        "ETH-USDT-SWAP",
        "LTC-USDT-SWAP"
      ],
      "lever": "10",
      "investAmt": "100",
      "subOrdType": "9",
      "entrySettingParam": {
        "allowMultipleEntry": true,
        "entryType": "1",
        "amt": "",
        "ratio": ""
      },
      "exitSettingParam": {
        "tpSlType": "2",
        "tpPct": "",
        "slPct": ""
      }
    }
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
signalChanId | String | Yes | Signal channel Id  
lever | String | Yes | Leverage  
Only applicable to `contract signal`  
investAmt | String | Yes | Investment amount  
subOrdType | String | Yes | Sub order type `1`：limit order `2`：market order `9`：tradingView signal  
includeAll | Boolean | No | Whether to include all USDT-margined contract.The default value is `false`. `true`: include `false` : exclude  
instIds | String | No | Instrument IDs. Single currency or multiple currencies separated with comma. When `includeAll` is `true`, it is ignored  
ratio | String | No | Price offset ratio, calculate the limit price as a percentage offset from the best bid/ask price.  
Only applicable to `subOrdType` is `limit` order  
entrySettingParam | String | No | Entry setting  
> allowMultipleEntry | String | No | Whether or not allow multiple entries in the same direction for the same trading pairs.The default value is `true`。 `true`：Allow `false`：Prohibit  
> entryType | String | No | Entry type  
`1`: TradingView signal  
`2`: Fixed margin  
`3`: Contracts  
`4`: Percentage of free margin  
`5`: Percentage of the initial invested margin  
> amt | String | No | Amount per order   
Only applicable to entryType in `2`/`3`  
> ratio | Array of objects | No | Amount ratio per order  
Only applicable to entryType in `4`/`5`  
exitSettingParam | String | No | Exit setting  
> tpSlType | String | 是 | Type of set the take-profit and stop-loss trigger price   
`pnl`: Based on the estimated profit and loss percentage from the entry point   
`price`: Based on price increase or decrease from the crypto’s entry price  
> tpPct | String | No | Take-profit percentage  
> slPct | String | No | Stop-loss percentage  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "algoClOrdId": "",
                "algoId": "447053782921515008",
                "sCode": "0",
                "sMsg": ""
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
algoId | String | Algo ID  
algoClOrdId | String | Client-supplied Algo ID  
sCode | String | The code of the event execution result, 0 means success.  
sMsg | String | The code of the event execution result, 0 means success.  
  
### POST / Cancel signal bots

A maximum of 10 orders can be stopped per request.

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Trade

#### HTTP Request

`POST /api/v5/tradingBot/signal/stop-order-algo`

> Request Example
    
    
    POST /api/v5/tradingBot/signal/stop-order-algo
    body
    [
        {
            "algoId":"448965992920907776"
        }
    ]
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
algoId | String | Yes | Algo ID  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "algoId": "448965992920907776",
                "sCode": "0",
                "sMsg": "",
                "algoClOrdId": ""
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
algoId | String | Algo ID  
sCode | String | The code of the event execution result, `0` means success.  
sMsg | String | Rejection or success message of event execution.  
algoClOrdId | String | Client-supplied Algo ID  
  
### POST / Adjust margin balance

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Trade

#### HTTP Request

`POST /api/v5/tradingBot/signal/margin-balance`

> Request Example
    
    
    POST /api/v5/tradingBot/signal/margin-balance
    body
    {
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
amt | String | Yes | Adjust margin balance amount  
Either `amt` or `percent` is required.  
allowReinvest | Boolean | No | Whether to reinvest with newly added margin. The default value is `false`.   
`false`:it will be used as passive margin to prevent liquidation and will not be used as active investment  
`true`:the margin added here will furthermore be accounted for in calculations of your total investment amount, and furthermore your order size。  
Only applicable to your signal comes in with an “investmentType” of “percentage_investment”  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "algoId": "123456"
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
algoId | String | Algo ID  
  
### POST / Amend TPSL

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Trade

#### HTTP Request

`POST /api/v5/tradingBot/signal/amendTPSL`

> Request Example
    
    
    POST /api/v5/tradingBot/signal/amendTPSL
    body
    {
        "algoId": "637039348240277504",
        "exitSettingParam": {
            "tpSlType": "pnl",
            "tpPct": "0.01",
            "slPct": "0.01"
        }
    }
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
algoId | String | Yes | Algo ID  
exitSettingParam | String | Yes | Exit setting  
> tpSlType | String | Yes | Type of set the take-profit and stop-loss trigger price  
`pnl`: Based on the estimated profit and loss percentage from the entry point  
`price`: Based on price increase or decrease from the crypto’s entry price  
> tpPct | String | No | Take-profit percentage  
> slPct | String | No | Stop-loss percentage  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "algoId": "637039348240277504"
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
algoId | String | Algo ID  
  
### POST / Set instruments

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Trade

#### HTTP Request

`POST /api/v5/tradingBot/signal/set-instruments`

> Request Example
    
    
    POST /api/v5/tradingBot/signal/set-instruments
    body
    {
        "algoId": "637039348240277504",
        "instIds": [
            "SHIB-USDT-SWAP",
            "ETH-USDT-SWAP"
        ]
    }
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
algoId | String | Yes | Algo ID  
instIds | Array of strings | Yes | Instrument IDs. When `includeAll` is `true`, it is ignored  
includeAll | Boolean | Yes | Whether to include all USDT-margined contract.The default value is `false`. `true`: include `false` : exclude  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "algoId": "637039348240277504"
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
algoId | String | Algo ID  
  
### GET / Signal bot order details

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Read

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
  
### GET / Active signal bot

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/tradingBot/signal/orders-algo-pending`

> Request Example
    
    
    GET /api/v5/tradingBot/signal/orders-algo-pending?algoOrdType=contract
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
algoOrdType | String | Yes | Algo order type  
`contract`: Contract signal  
algoId | String | No | Algo ID  
after | String | Yes | Pagination of data to return records `algoId` earlier than the requested timestamp, Unix timestamp format in milliseconds, e.g. `1597026383085`  
before | String | No | Pagination of data to return records `algoId` newer than the requested timestamp, Unix timestamp format in milliseconds, e.g. `1597026383085`  
limit | String | No | Number of results per request. The maximum is 100. The default is 100.  
  
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
                "signalChanName": "my signal",
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
cancelType | String | Algo order stop reason  
`0`: None  
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
  
### GET / Signal bot history

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/tradingBot/signal/orders-algo-history`

> Request Example
    
    
    GET /api/v5/tradingBot/signal/orders-algo-history?algoId=623833708424069120&algoOrdType=contract
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
algoOrdType | String | Yes | Algo order type  
`contract`: Contract signal  
algoId | String | Yes | Algo ID  
after | String | Yes | Pagination of data to return records `algoId` earlier than the requested timestamp, Unix timestamp format in milliseconds, e.g. `1597026383085`  
before | String | No | Pagination of data to return records `algoId` newer than the requested timestamp, Unix timestamp format in milliseconds, e.g. `1597026383085`  
limit | String | No | Number of results per request. The maximum is 100. The default is 100.  
  
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
                "cancelType": "1",
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
                "signalChanName": "my signal",
                "signalSourceType": "1",
                "state": "stopped",
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
`stopped`  
cancelType | String | Algo order stop reason  
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
  
### GET / Signal bot order positions

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/tradingBot/signal/positions`

> Request Example
    
    
    GET /api/v5/tradingBot/signal/positions?algoId=623833708424069120&algoOrdType=contract
    

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
                "adl": "1",
                "algoClOrdId": "",
                "algoId": "623833708424069120",
                "avgPx": "1597.74",
                "cTime": "1697502301460",
                "ccy": "USDT",
                "imr": "23.76495",
                "instId": "ETH-USDT-SWAP",
                "instType": "SWAP",
                "last": "1584.34",
                "lever": "10",
                "liqPx": "1438.7380360728976",
                "markPx": "1584.33",
                "mgnMode": "cross",
                "mgnRatio": "11.719278420807477",
                "mmr": "1.9011959999999997",
                "notionalUsd": "237.75168928499997",
                "pos": "15",
                "posSide": "net",
                "uTime": "1697502301460",
                "upl": "-2.0115000000000123",
                "uplRatio": "-0.0839310526118142"
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
algoId | String | Algo ID  
algoClOrdId | String | Client-supplied Algo ID. Used to be extended in the future.  
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
  
### GET / Position history

Retrieve the updated position data for the last 3 months. Return in reverse chronological order using utime.

#### Rate Limit: 10 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/tradingBot/signal/positions-history`

> Request Example
    
    
    GET /api/v5/tradingBot/signal/positions-history?algoId=1234
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
algoId | String | Yes | Algo ID  
instId | String | No | Instrument ID, e.g.：`BTC-USD-SWAP`  
after | String | No | Pagination of data to return records earlier than the requested `uTime`, Unix timestamp format in milliseconds, e.g.`1597026383085`  
before | String | No | Pagination of data to return records newer than the requested `uTime`, Unix timestamp format in milliseconds, e.g `1597026383085`  
limit | String | No | Number of results per request. The maximum is 100. The default is 100.  
  
> Response Example
    
    
    {
      "code": "0",
      "data": [
        {
          "cTime": "1704724451471",
          "closeAvgPx": "200",
          "direction": "net",
          "instId": "ETH-USDT-SWAP",
          "lever": "5.0",
          "mgnMode": "cross",
          "openAvgPx": "220",
          "pnl": "-2.021",
          "pnlRatio": "-0.4593181818181818",
          "uTime": "1704724456322",
          "uly": "ETH-USDT"
        }
      ],
      "msg": ""
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
instId | String | Instrument ID  
mgnMode | String | Margin mode `cross` `isolated`  
cTime | String | Created time of position  
uTime | String | Updated time of position  
openAvgPx | String | Average price of opening position  
closeAvgPx | String | Average price of closing position  
pnl | String | Profit and loss  
pnlRatio | String | P&L ratio  
lever | String | Leverage  
direction | String | Direction: `long` `short`  
uly | String | Underlying  
  
### POST / Close position

Close the position of an instrument via a market order.

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Trade

#### HTTP Request

`POST /api/v5/tradingBot/signal/close-position`

> Request Example
    
    
    POST /api/v5/tradingBot/signal/close-position
    body
    {
        "instId":"BTC-USDT-SWAP",
        "algoId":"448965992920907776"
    }
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
algoId | String | Yes | Algo ID  
instId | String | Yes | Instrument ID  
  
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
  
### POST / Place sub order

You can place an order only if you have sufficient funds.  
  

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Trade

#### HTTP Request

`POST /api/v5/tradingBot/signal/sub-order`

> Request Example
    
    
    POST /api/v5/tradingBot/signal/sub-order
    body
    {
        "algoId":"1222",
        "instId":"BTC-USDT-SWAP",
        "side":"buy",
        "ordType":"limit",
        "px":"2.15",
        "sz":"2"
    }
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
instId | String | Yes | Instrument ID, e.g. `BTC-USDT-SWAP`  
algoId | String | Yes | Algo ID  
side | String | Yes | Order side, `buy` `sell`  
ordType | String | Yes | Order type   
`market`: Market order   
`limit`: Limit order  
sz | String | Yes | Quantity to buy or sell  
px | String | Conditional | Order price. Only applicable to `limit` order.  
reduceOnly | Boolean | No | Whether orders can only reduce in position size.   
Valid options: `true` or `false`. The default value is `false`.   
Only applicable to `Futures mode`/`Multi-currency margin`  
  
> Response Example
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
        ]
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
code | String | The result code, `0` means success  
msg | String | The error message, empty if the code is 0  
data | Array of objects | Array of objects contains the response results  
ordType  
Order type. When creating a new order, you must specify the order type. The order type you specify will affect: 1) what order parameters are required, and 2) how the matching system executes your order. The following are valid order types:  
`limit`: Limit order, which requires specified sz and px.  
`market`: Market order. It will be filled with market price (by swiping opposite order book). Market order will be placed to order book with most aggressive price allowed by Price Limit Mechanism.  sz refers to the number of contracts。  reduceOnly  
When placing an order with this parameter set to true, it means that the order will reduce the size of the position only The sum of the current order size and all reverse direction reduce-only pending orders which's price-time priority is higher than the current order, cannot exceed the contract quantity of position. Only applicable to `Futures mode` and `Multi-currency margin` 

### POST / Cancel sub order

Cancel an incomplete order.

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Trade

#### HTTP Request

`POST /api/v5/tradingBot/signal/cancel-sub-order`

> Request Example
    
    
    POST /api/v5/tradingBot/signal/cancel-sub-order
    body
    {
        "algoId":"91664",
        "signalOrdId":"590908157585625111",
        "instId":"BTC-USDT-SWAP"
    }
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
algoId | String | Yes | Algo ID  
instId | String | Yes | Instrument ID, e.g. BTC-USDT-SWAP  
signalOrdId | String | Yes | Order ID  
  
> Response Example
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
            {
                "signalOrdId":"590908157585625111",
                "sCode":"0",
                "sMsg":""
            }
        ]
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
code | String | The result code, `0` means success  
msg | String | The error message, empty if the code is 0  
data | Array of objects | Array of objects contains the response results  
> signalOrdId | String | Order ID  
> sCode | String | The code of the event execution result, `0` means success.  
> sMsg | String | Rejection or success message of event execution.  
Cancel order returns with sCode equal to 0. It is not strictly considered that the order has been canceled. It only means that your cancellation request has been accepted by the system server. The result of the cancellation is subject to the state by get sub orders endpoint.  

### GET / Signal bot sub orders

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/tradingBot/signal/sub-orders`

> Request Example
    
    
    # Get historical filled sub orders
    GET /api/v5/tradingBot/signal/sub-orders?algoId=623833708424069120&algoOrdType=contract&state=filled
    
    # Get designated sub order
    GET /api/v5/tradingBot/signal/sub-orders?algoId=623833708424069120&algoOrdType=contract&signalOrdId=O632302662327996418
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
algoId | String | Yes | Algo ID  
algoOrdType | String | Yes | Algo order type  
`contract`: Contract signal  
state | String | Conditional | Sub order state  
`live`  
`partially_filled`  
`filled`  
`cancelled`  
Either `state` or `signalOrdId` is required, if both are passed in, only `state` is valid.  
signalOrdId | String | Conditional | Sub order ID  
after | String | No | Pagination of data to return records earlier than the requested `ordId`  
before | String | No | Pagination of data to return records newer than the requested `ordId`.  
begin | String | No | Return records of `ctime` after than the requested timestamp (include), Unix timestamp format in milliseconds, e.g. `1597026383085`  
end | String | No | Return records of `ctime` before than the requested timestamp (include), Unix timestamp format in milliseconds, e.g. `1597026383085`  
limit | String | No | Number of results per request. The maximum is 100. The default is 100.  
type | String | No | Sub order type   
`live`  
`filled`  
Either `type` or `clOrdId` is required, if both are passed in, only `clOrdId` is valid.  
clOrdId | String | No | Sub order client-supplied ID.   
`It will be deprecated soon`  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "accFillSz": "18",
                "algoClOrdId": "",
                "algoId": "623833708424069120",
                "algoOrdType": "contract",
                "avgPx": "1572.81",
                "cTime": "1697024702320",
                "ccy": "",
                "clOrdId": "O632302662327996418",
                "ctVal": "0.01",
                "fee": "-0.1415529",
                "feeCcy": "USDT",
                "instId": "ETH-USDT-SWAP",
                "instType": "SWAP",
                "lever": "10",
                "ordId": "632302662351958016",
                "ordType": "market",
                "pnl": "-2.6784",
                "posSide": "net",
                "px": "",
                "side": "buy",
                "state": "filled",
                "sz": "18",
                "tag": "",
                "tdMode": "cross",
                "uTime": "1697024702322"
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
algoId | String | Algo ID  
algoClOrdId | String | Client-supplied Algo ID. Used to be extended in the future  
instType | String | Instrument type  
instId | String | Instrument ID  
algoOrdType | String | Algo order type  
`contract`: Contract signal  
ordId | String | Sub order ID  
clOrdId | String | Sub order client-supplied ID.   
It is equal to `signalOrdId`  
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
`buy`,`sell`  
px | String | Sub order price  
fee | String | Sub order fee amount  
feeCcy | String | Sub order fee currency  
avgPx | String | Sub order average filled price  
accFillSz | String | Sub order accumulated fill quantity  
posSide | String | Sub order position side  
`net`  
pnl | String | Sub order profit and loss  
ctVal | String | Contract value  
Only applicable to `FUTURES`/`SWAP`  
lever | String | Leverage  
tag | String | Order tag  
  
### GET / Signal bot event history

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/tradingBot/signal/event-history`

> Request Example
    
    
    GET /api/v5/tradingBot/signal/event-history?algoId=623833708424069120
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
algoId | String | Yes | Algo ID  
after | String | No | Pagination of data to return records `eventCtime` earlier than the requested timestamp, Unix timestamp format in milliseconds, e.g. `1597026383085`  
before | String | No | Pagination of data to return records `eventCtime` newer than the requested timestamp, Unix timestamp format in milliseconds, e.g. `1597026383085`  
limit | String | No | Number of results per request. The maximum is 100. The default is 100.  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "alertMsg": "{\"marketPosition\":\"short\",\"prevMarketPosition\":\"long\",\"action\":\"sell\",\"instrument\":\"ETHUSDT.P\",\"timestamp\":\"2023-10-16T10:50:00.000Z\",\"maxLag\":\"60\",\"investmentType\":\"base\",\"amount\":\"2\"}",
                "algoId": "623833708424069120",
                "eventCtime": "1697453400959",
                "eventProcessMsg": "Processed reverse entry signal and placed ETH-USDT-SWAP order with all available balance",
                "eventStatus": "success",
                "eventType": "signal_processing",
                "eventUtime": "",
                "triggeredOrdData": [
                    {
                        "clOrdId": "O634100754731765763"
                    },
                    {
                        "clOrdId": "O634100754752737282"
                    }
                ]
            }
         ],
         "msg": ""
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
alertMsg | String | Alert message  
algoId | String | Algo ID  
eventType | String | Event type  
`system_action`  
`user_action`  
`signal_processing`  
eventCtime | String | Event timestamp of creation. Unix timestamp format in milliseconds, e.g. `1597026383085`  
eventUtime | String | Event timestamp of update. Unix timestamp format in milliseconds, e.g. `1597026383085`  
eventProcessMsg | String | Event process message  
eventStatus | String | Event status  
`success`  
`failure`  
triggeredOrdData | Array of objects | Triggered sub order data  
> clOrdId | String | Sub order client-supplied id

---

# 信号交易

信号策略允许您将定制的数字货币交易策略展示在欧易平台。您可以完全控制自己设计的算法，而策略将会以高性能、高可靠性实时执行您的交易。[了解更多](/cn/learn/signal-trading)  
  
### POST / 创建信号 

#### 限速：20次/2s

#### 限速规则：User ID

#### 权限：交易

#### HTTP请求

`POST /api/v5/tradingBot/signal/create-signal`

> 请求示例
    
    
    POST /api/v5/tradingBot/signal/create-signal
    body
    {
      "signalChanName": "long short",
      "signalDesc": "this is the first version"
    }
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
signalChanName | String | 是 | 信号名称  
signalChanDesc | String | 否 | 信号描述  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
           {
               "signalChanId" :"572112109",
               "signalChanToken":"dojuckew331lkx"
           }
    
        ],
        "msg": ""
    }
    
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
signalChanId | String | 信号ID  
signalChanToken | String | 信号单的用户身份标识  
  
### GET / 查询所有信号 

#### 限速：20次/2s

#### 限速规则：User ID

#### 权限：读取

#### HTTP请求

`GET /api/v5/tradingBot/signal/signals`

> 请求示例
    
    
    GET /api/v5/tradingBot/signal/signals
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
signalSourceType | String | 是 | 信号来源类型  
`1`：自己创建的  
`2`：订阅他人  
`3`：免费信号  
signalChanId | String | 否 | 信号ID  
after | String | 否 | 请求此ID之前（更旧的数据）的分页内容，传的值为对应接口的signalChanId  
before | String | 否 | 请求此ID之后（更新的数据）的分页内容，传的值为对应接口的signalChanId  
limit | String | 否 | 返回结果的数量，最大为100，默认100条  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "signalChanId": "623833708424069120",
                "signalChanName": "test",
                "signalChanDesc": "test",
                "signalChanToken": "test",
                "signalSourceType": "1"
            }
        ],
        "msg": ""
    }
    
    
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
signalChanId | String | 信号ID  
signalChanName | String | 信号名称  
signalChanDesc | String | 信号描述  
signalChanToken | String | 信号单的用户身份标识  
signalSourceType | String | 信号来源类型  
`1`：自己创建的  
`2`：订阅他人  
`3`：免费信号  
  
### POST / 创建信号策略 

#### 限速：20次/2s

#### 限速规则：User ID

#### 权限：交易

#### HTTP请求

`POST /api/v5/tradingBot/signal/order-algo`

> 请求示例
    
    
    # 创建信号策略
    POST /api/v5/tradingBot/signal/order-algo
    body
    {
      "signalChanId": "627921182788161536",
      "instIds": [
        "BTC-USDT-SWAP",
        "ETH-USDT-SWAP",
        "LTC-USDT-SWAP"
      ],
      "lever": "10",
      "investAmt": "100",
      "subOrdType": "9",
      "entrySettingParam": {
        "allowMultipleEntry": true,
        "entryType": "1",
        "amt": "",
        "ratio": ""
      },
      "exitSettingParam": {
        "tpSlType": "2",
        "tpPct": "",
        "slPct": ""
      }
    }
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
signalChanId | String | 是 | 信号ID  
includeAll | Boolean | 否 | 是否包含所有USDT 本位永续合约，默认false。 `true`: 包含 `false` : 不包含  
instIds | String | 否 | 该信号支持的产品ID列表， 多个instId 用逗号分隔。当 includeAll 为true 时， 忽略此参数  
lever | String | 是 | 杠杆倍数仅适用于合约信号  
investAmt | String | 是 | 投入金额  
subOrdType | String | 是 | 1：限价 2：市价 9：由tradingView信号指定  
ratio | String | 否 | 限价单的委托价格距离买一/卖一价的百分比。当委托类型为限价时，该字段有效。  
entrySettingParam | String | 否 | 进场参数设定  
> allowMultipleEntry | String | 否 | 是否允许多次进场，默认允许。 `true`：允许 `false`：不允许  
> entryType | String | 否 | 单次委托类型  
`1`：单次委托量具体数值将从 TradingView 信号中传入  
`2`：单次委托量为固定数量的保证金  
`3`：单次委托量为固定的合约张数  
`4`：单次委托量基于在收到触发信号时策略中可用保证金的百分比  
`5`：单次委托量基于在创建策略时设置的初始投入保证金的百分比  
> amt | String | 否 | 单笔委托量  
在单次委托类型是 固定保证金 / 合约张数 下该字段有效  
> ratio | Array of objects | 否 | 单笔委托数量百分比  
在单次委托类型是 占用保证金比例 / 初始投资比例 下该字段有效  
exitSettingParam | String | 否 | 离场参数设定  
> tpSlType | String | 是 | 止盈止损类型，该参数用户确定设置止盈止损的触发价格计算的方式  
`pnl`：基于平均持仓成本和预期收益率  
`price`：基于相对于平均持仓成本的涨跌幅  
> tpPct | String | 否 | 止盈百分比  
> slPct | String | 否 | 止损百分比  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "algoClOrdId": "",
                "algoId": "447053782921515008",
                "sCode": "0",
                "sMsg": ""
            }
        ],
        "msg": ""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
algoId | String | 策略ID  
algoClOrdId | String | 用户自定义策略ID  
sCode | String | 事件执行结果的code，0代表成功  
sMsg | String | 事件执行失败时的msg  
  
### POST / 停止信号策略 

每次最多可以撤销10个信号策略。

#### 限速：20次/2s

#### 限速规则：User ID

#### 权限：交易

#### HTTP请求

`POST /api/v5/tradingBot/signal/stop-order-algo`

> 请求示例
    
    
    POST /api/v5/tradingBot/signal/stop-order-algo
    body
    [
        {
            "algoId":"448965992920907776"
        }
    ]
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
algoId | String | 是 | 策略ID  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "algoId": "448965992920907776",
                "sCode": "0",
                "sMsg": "",
                "algoClOrdId": ""
    
            }
        ],
        "msg": ""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
algoId | String | 策略ID  
sCode | String | 事件执行结果的code，0代表成功  
sMsg | String | 事件执行失败时的msg  
algoClOrdId | String | 客户自定义订单ID  
  
### POST / 调整保证金 

#### 限速：20次/2s

#### 限速规则：User ID

#### 权限：交易

#### HTTP请求

`POST /api/v5/tradingBot/signal/margin-balance`

> 请求示例
    
    
    POST /api/v5/tradingBot/signal/margin-balance
    body
    {
       "algoId":"123456",
       "type":"add",
       "amt":"10"
    }
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
algoId | String | 是 | 策略ID  
type | String | 是 | 调整保证金类型  
`add`：增加，`reduce`：减少  
amt | String | 是 | 调整保证金数量  
allowReinvest | Boolean | 否 | 是否允许复投调整后的保证金，默认false。true 或者 false `false`:新投入的资金仅作为保证金用于避免爆仓  
`true`:新投入的资金将可用于进行复投。  
仅适用于进场设定为“TradingView 信号”或“初始投资比例”的策略  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "algoId": "123456"
            }
        ],
        "msg": ""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
algoId | String | 策略ID  
  
### POST / 修改止盈止损 

#### 限速：20次/2s

#### 限速规则：User ID

#### 权限：交易

#### HTTP请求

`POST /api/v5/tradingBot/signal/amendTPSL`

> 请求示例
    
    
    POST /api/v5/tradingBot/signal/amendTPSL
    body
    {
        "algoId": "637039348240277504",
        "exitSettingParam": {
            "tpSlType": "pnl",
            "tpPct": "0.01",
            "slPct": "0.01"
        }
    }
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
algoId | String | 是 | 策略ID  
exitSettingParam | String | 是 | 离场参数设定  
> tpSlType | String | 是 | 止盈止损类型  
> tpPct | String | 否 | 止盈百分比  
> slPct | String | 否 | 止损百分比  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "algoId": "637039348240277504"
            }
        ],
        "msg": ""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
algoId | String | 策略ID  
  
### POST / 设置币对 

#### 限速：20次/2s

#### 限速规则：User ID

#### 权限：交易

#### HTTP请求

`POST /api/v5/tradingBot/signal/set-instruments`

> 请求示例
    
    
    POST /api/v5/tradingBot/signal/set-instruments
    body
    {
        "algoId": "637039348240277504",
        "instIds": [
            "SHIB-USDT-SWAP",
            "ETH-USDT-SWAP"
        ]
    }
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
algoId | String | 是 | 策略ID  
instIds | Array of strings | 是 | 产品Id 列表，当 includeAll 为 true 时，忽略此参数。  
includeAll | Boolean | 是 | 是否包含所有USDT 本位永续合约，默认false `true`: 包含 `false` : 不包含  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "algoId": "637039348240277504"
            }
        ],
        "msg": ""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
algoId | String | 策略ID  
  
### GET / 获取信号策略详情 

#### 限速：20次/2s

#### 限速规则：User ID

#### 权限：读取

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
  
### GET / 获取活跃信号策略 

#### 限速：20次/2s

#### 限速规则：User ID

#### 权限：读取

#### HTTP请求

`GET /api/v5/tradingBot/signal/orders-algo-pending`

> 请求示例
    
    
    GET /api/v5/tradingBot/signal/orders-algo-pending?algoOrdType=contract
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
algoOrdType | String | 是 | 策略类型  
`contract`：合约信号  
algoId | String | 否 | 策略ID  
after | String | 否 | 请求此ID之前（更旧的数据）的分页内容，传的值为对应接口的algoId  
before | String | 否 | 请求此ID之后（更新的数据）的分页内容，传的值为对应接口的algoId  
limit | String | 否 | 返回结果的数量，最大为100，默认100条  
  
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
  
### GET / 获取历史信号策略 

#### 限速：20次/2s

#### 限速规则：User ID

#### 权限：读取

#### HTTP请求

`GET /api/v5/tradingBot/signal/orders-algo-history`

> 请求示例
    
    
    GET /api/v5/tradingBot/signal/orders-algo-history?algoId=623833708424069120&algoOrdType=contract
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
algoOrdType | String | 是 | 策略类型  
`contract`：合约信号  
algoId | String | 是 | 策略ID  
after | String | 否 | 请求此ID之前（更旧的数据）的分页内容，传的值为对应接口的algoId  
before | String | 否 | 请求此ID之后（更新的数据）的分页内容，传的值为对应接口的algoId  
limit | String | 否 | 返回结果的数量，最大为100，默认100条  
  
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
                "cancelType": "1",
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
                "state": "stopped",
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
`stopped`：已停止  
cancelType | String | 策略停止原因  
1`：手动停止  
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
  
### GET / 获取信号策略持仓 

#### 限速：20次/2s

#### 限速规则：User ID

#### 权限：读取

#### HTTP请求

`GET /api/v5/tradingBot/signal/positions`

> 请求示例
    
    
    GET /api/v5/tradingBot/signal/positions?algoId=623833708424069120&algoOrdType=contract
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
algoOrdType | String | 是 | 订单类型  
`contract`：合约信号  
algoId | String | 是 | 策略ID  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "adl": "1",
                "algoClOrdId": "",
                "algoId": "623833708424069120",
                "avgPx": "1597.74",
                "cTime": "1697502301460",
                "ccy": "USDT",
                "imr": "23.76495",
                "instId": "ETH-USDT-SWAP",
                "instType": "SWAP",
                "last": "1584.34",
                "lever": "10",
                "liqPx": "1438.7380360728976",
                "markPx": "1584.33",
                "mgnMode": "cross",
                "mgnRatio": "11.719278420807477",
                "mmr": "1.9011959999999997",
                "notionalUsd": "237.75168928499997",
                "pos": "15",
                "posSide": "net",
                "uTime": "1697502301460",
                "upl": "-2.0115000000000123",
                "uplRatio": "-0.0839310526118142"
            }
        ],
        "msg": ""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
algoId | String | 策略ID  
algoClOrdId | String | 用户自定义策略ID，将来扩展使用。  
instType | String | 产品类型  
instId | String | 产品ID，如 `BTC-USDT-SWAP`  
cTime | String | 策略创建时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
uTime | String | 策略更新时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
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
  
### GET /查看历史持仓信息 

获取最近3个月有更新的仓位信息，按照仓位更新时间倒序排列。组合保证金账户模式不支持查询历史持仓。

#### 限速：10次/2s

#### 限速规则：User ID

#### 权限：读取

#### HTTP请求

`GET /api/v5/tradingBot/signal/positions-history`

> 请求示例
    
    
    GET /api/v5/tradingBot/signal/positions-history?algoId=1234
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
algoId | String | 是 | 策略ID  
instId | String | 否 | 交易产品ID，如：`BTC-USD-SWAP`  
after | String | 否 | 查询仓位更新 (uTime) 之前的内容，值为时间戳，Unix 时间戳为毫秒数格式，如 `1597026383085`  
before | String | 否 | 查询仓位更新 (uTime) 之后的内容，值为时间戳，Unix 时间戳为毫秒数格式，如 `1597026383085`  
limit | String | 否 | 分页返回结果的数量，最大为100，默认100条  
  
> 返回结果
    
    
    {
      "code": "0",
      "data": [
        {
          "cTime": "1704724451471",
          "closeAvgPx": "200",
          "direction": "net",
          "instId": "ETH-USDT-SWAP",
          "lever": "5.0",
          "mgnMode": "cross",
          "openAvgPx": "220",
          "pnl": "-2.021",
          "pnlRatio": "-0.4593181818181818",
          "uTime": "1704724456322",
          "uly": "ETH-USDT"
        }
      ],
      "msg": ""
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
instId | String | 交易产品ID  
mgnMode | String | 保证金模式 `cross`：全仓，`isolated`：逐仓"  
cTime | String | 仓位创建时间  
uTime | String | 仓位更新时间  
openAvgPx | String | 开仓均价  
closeAvgPx | String | 平仓均价  
pnl | String | 平仓收益额  
pnlRatio | String | 平仓收益率  
lever | String | 杠杆倍数  
direction | String | 持仓方向 `long`：多 `short`：空  
uly | String | 标的指数  
  
### POST / 市价仓位全平 

市价平掉指定交易产品的持仓

#### 限速：20次/2s

#### 限速规则：User ID

#### 权限：交易

#### HTTP请求

`POST /api/v5/tradingBot/signal/close-position`

> 请求示例
    
    
    POST /api/v5/tradingBot/signal/close-position
    body
    {
        "instId":"BTC-USDT-SWAP",
        "algoId":"448965992920907776"
    }
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
algoId | String | 是 | 策略ID  
instId | String | 是 | 产品ID  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "algoId": "448965992920907776"
            }
        ],
        "msg": ""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
algoId | String | 策略ID  
  
### POST / 下单 

只有当您的账户有足够的资金才能下单。  
  

#### 限速：20次/2s

#### 权限：交易

#### HTTP请求

`POST /api/v5/tradingBot/signal/sub-order`

> 请求示例
    
    
    POST /api/v5/tradingBot/signal/sub-order
    body
    {
        "algoId":"1222",
        "instId":"BTC-USDT-SWAP",
        "side":"buy",
        "ordType":"limit",
        "px":"2.15",
        "sz":"2"
    }
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
instId | String | 是 | 产品ID，如 `BTC-USDT-SWAP`  
algoId | String | 是 | 策略订单ID  
side | String | 是 | 订单方向  
`buy`：买， `sell`：卖  
ordType | String | 是 | 订单类型   
`market`：市价单  
`limit`：限价单  
sz | String | 是 | 委托数量  
px | String | 可选 | 委托价格，仅适用于`limit`  
reduceOnly | Boolean | 否 | 是否只减仓，`true` 或 `false`，默认`false`  
仅适用于`合约模式`和`跨币种保证金模式`  
  
> 返回结果
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
        ]
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
code | String | 结果代码，`0`表示成功  
msg | String | 错误信息，代码为0时，该字段为空  
data | Array of objects | 包含结果的对象数组  
ordType  
订单类型，创建新订单时必须指定，您指定的订单类型将影响需要哪些订单参数和撮合系统如何执行您的订单，以下是有效的ordType：  
普通委托：  
limit：限价单，要求指定sz 和 px  
market：自动以最高买/最低卖价格委托，遵循限价机制  
sz 指合约张数。  reduceOnly  
只减仓，下单时，此参数设置为 true 时，表示此笔订单具有减仓属性，只会减少持仓数量，不会增加新的持仓仓位  
当前只减仓下单张数，加上价格时间优先于当前只减仓下单的只减仓挂单张数总和，不能超过持仓数量  
仅适用于`合约模式`和`跨币种保证金模式`  

### POST / 撤单 

撤销之前下的未完成订单。

#### 限速：20次/2s

#### 限速规则：User ID

#### 权限：交易

#### HTTP请求

`POST /api/v5/tradingBot/signal/cancel-sub-order`

> 请求示例
    
    
    POST /api/v5/tradingBot/signal/cancel-sub-order
    body
    {
        "algoId":"91664",
        "signalOrdId":"590908157585625111",
        "instId":"BTC-USDT-SWAP"
    }
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
algoId | String | 是 | 策略ID  
instId | String | 是 | 产品ID，如 BTC-USDT-SWAP  
signalOrdId | String | 是 | 订单ID  
  
> 返回结果
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
            {
                "signalOrdId":"590908157585625111",
                "sCode":"0",
                "sMsg":""
            }
        ]
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
code | String | 结果代码，`0`表示成功  
msg | String | 错误信息，代码为0时，该字段为空  
data | Array of objects | 包含结果的对象数组  
> signalOrdId | String | 订单ID  
> sCode | String | 事件执行结果的code，0代表成功  
> sMsg | String | 事件执行失败时的msg  
撤单返回sCode等于0不能严格认为该订单已经被撤销，只表示您的撤单请求被系统服务器所接受，撤单结果以者查询订单状态为准  

### GET / 获取信号策略子订单信息 

#### 限速：20次/2s

#### 限速规则：User ID

#### 权限：读取

#### HTTP请求

`GET /api/v5/tradingBot/signal/sub-orders`

> 请求示例
    
    
    # 查询已成交历史子订单
    GET /api/v5/tradingBot/signal/sub-orders?algoId=623833708424069120&algoOrdType=contract&state=filled
    
    # 查询指定子订单
    GET /api/v5/tradingBot/signal/sub-orders?algoId=623833708424069120&algoOrdType=contract&signalOrdId=O632302662327996418
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
algoId | String | 是 | 策略ID  
algoOrdType | String | 是 | 策略类型  
`contract`：合约信号  
state | String | 可选 | 子订单状态  
`live`：未成交  
`partially_filled`：部分成交  
`filled`：已成交  
`canceled`：已取消  
state 和 signalOrdId 必须传一个，若传两个，以 state 为主  
signalOrdId | String | 可选 | 子订单ID  
after | String | 否 | 请求此ID之前（更旧的数据）的分页内容，传的值为对应接口的`ordId`  
before | String | 否 | 请求此ID之后（更新的数据）的分页内容，传的值为对应接口的`ordId`  
begin | String | 否 | 请求`cTime`在此时间戳之后(包含)的数据，值为时间戳，Unix 时间戳为毫秒数格式，如 `1597026383085`  
end | String | 否 | 请求`cTime`在此时间戳之前(包含)的数据，值为时间戳，Unix 时间戳为毫秒数格式，如 `1597026383085`  
limit | String | 否 | 返回结果的数量，最大为100，默认100条  
type | String | 否 | 子订单类型  
`live`：未成交  
`filled`：已成交  
`即将废弃`  
clOrdId | String | 否 | 子订单自定义订单ID   
`即将废弃`  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "accFillSz": "18",
                "algoClOrdId": "",
                "algoId": "623833708424069120",
                "algoOrdType": "contract",
                "avgPx": "1572.81",
                "cTime": "1697024702320",
                "ccy": "",
                "clOrdId": "O632302662327996418",
                "ctVal": "0.01",
                "fee": "-0.1415529",
                "feeCcy": "USDT",
                "instId": "ETH-USDT-SWAP",
                "instType": "SWAP",
                "lever": "10",
                "ordId": "632302662351958016",
                "ordType": "market",
                "pnl": "-2.6784",
                "posSide": "net",
                "px": "",
                "side": "buy",
                "state": "filled",
                "sz": "18",
                "tag": "",
                "tdMode": "cross",
                "uTime": "1697024702322"
            }
        ],
        "msg": ""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
algoId | String | 策略ID  
algoClOrdId | String | 用户自定义策略ID，将来扩展使用。  
instType | String | 产品类型  
instId | String | 交易产品ID  
algoOrdType | String | 策略类型  
`contract`：合约信号  
ordId | String | 子订单ID  
clOrdId | String | 子订单自定义ID，等同于`signalOrdId`  
cTime | String | 子订单创建时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
uTime | String | 子订单更新时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
tdMode | String | 子订单交易模式  
`cross`：全仓  
`isolated`：逐仓  
`cash`：非保证金  
ccy | String | 保证金币种  
仅适用于`合约模式`下的`全仓杠杆`订单  
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
avgPx | String | 子订单平均成交价格  
accFillSz | String | 子订单累计成交数量  
posSide | String | 子订单持仓方向  
`net`：买卖模式  
pnl | String | 子订单收益  
ctVal | String | 合约面值  
仅支持`FUTURES/SWAP`  
lever | String | 杠杆倍数  
tag | String | 订单标签  
  
### GET / 获取信号策略历史事件 

#### 限速：20次/2s

#### 限速规则：User ID

#### 权限：读取

#### HTTP请求

`GET /api/v5/tradingBot/signal/event-history`

> 请求示例
    
    
    GET /api/v5/tradingBot/signal/event-history?algoId=623833708424069120
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
algoId | String | 是 | 策略ID  
after | String | 否 | 请求`eventCtime`在此时间之前（更旧的数据）的分页内容，值为时间戳，Unix 时间戳为毫秒数格式，如 `1597026383085`  
before | String | 否 | 请求`eventCtime`此时间之后（更新的数据）的分页内容，值为时间戳，Unix 时间戳为毫秒数格式，如 `1597026383085`  
limit | String | 否 | 返回结果的数量，最大为100，默认100条  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "alertMsg": "{\"marketPosition\":\"short\",\"prevMarketPosition\":\"long\",\"action\":\"sell\",\"instrument\":\"ETHUSDT.P\",\"timestamp\":\"2023-10-16T10:50:00.000Z\",\"maxLag\":\"60\",\"investmentType\":\"base\",\"amount\":\"2\"}",
                "algoId": "623833708424069120",
                "eventCtime": "1697453400959",
                "eventProcessMsg": "Processed reverse entry signal and placed ETH-USDT-SWAP order with all available balance",
                "eventStatus": "success",
                "eventType": "signal_processing",
                "eventUtime": "",
                "triggeredOrdData": [
                    {
                        "clOrdId": "O634100754731765763"
                    },
                    {
                        "clOrdId": "O634100754752737282"
                    }
                ]
            }
         ],
         "msg": ""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
alertMsg | String | 提示信息  
algoId | String | 策略ID  
eventType | String | 事件类型  
`system_action`：系统行为  
`user_action`：用户行为  
`signal_processing`：信号下单  
eventCtime | String | 事件发生时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
eventUtime | String | 事件更新时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
eventProcessMsg | String | 事件处理信息  
eventStatus | String | 事件处理状态  
`success`：成功  
`failure`：失败  
triggeredOrdData | Array of objects | 信号触发的子订单的信息  
> clOrdId | String | 子订单自定义ID