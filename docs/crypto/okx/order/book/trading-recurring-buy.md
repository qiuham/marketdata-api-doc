---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#order-book-trading-recurring-buy
anchor_id: order-book-trading-recurring-buy
api_type: API
updated_at: 2026-07-18 20:03:44.615246
---

# Recurring Buy

Recurring buy is a strategy for investing a fixed amount in crypto at fixed intervals. An appropriate recurring approach in volatile markets allows you to buy crypto at lower costs. [Learn more](/help/vii-recurring-buy)  
The API endpoints of `Recurring buy` require authentication.  
  
### POST / Place recurring buy order

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: User ID

#### HTTP Request

`POST /api/v5/tradingBot/recurring/order-algo`

> Request Example
    
    
    POST /api/v5/tradingBot/recurring/order-algo
    body
    {
      "stgyName": "BTC|ETH recurring buy monthly",     
      "amt":"100",
      "recurringList":[    
        {
             "ccy":"BTC",
             "ratio":"0.2"
        },
        {
             "ccy":"ETH",
             "ratio":"0.8"
        }
      ],
      "period":"monthly",
      "recurringDay":"1",
      "recurringTime":"0",
      "timeZone":"8",   // UTC +8
      "tdMode":"cross",
      "investmentCcy":"USDT"
    }
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
stgyName | String | Yes | Custom name for trading bot, no more than 40 characters  
recurringList | Array of objects | Yes | Recurring buy info  
> ccy | String | Yes | Recurring currency, e.g. `BTC`  
> ratio | String | Yes | Proportion of recurring currency assets, e.g. "0.2" representing 20%  
> minPx | String | No | Minimum price of recurring currency. `""` means no limit  
> maxPx | String | No | Maximum price of recurring currency. `""` means no limit  
period | String | Yes | Period  
`monthly`  
`weekly`  
`daily`  
`hourly`  
recurringDay | String | Conditional | Recurring buy date  
When the period is `monthly`, the value range is an integer of [1,28]  
When the period is `weekly`, the value range is an integer of [1,7]  
When the period is `daily`/`hourly`, the parameter is not required.  
recurringHour | String | Conditional | Recurring buy by hourly  
`1`/`4`/`8`/`12`, e.g. `4` represents "recurring buy every 4 hour"  
When the period is `hourly`, the parameter is required.  
recurringTime | String | Yes | Recurring buy time, the value range is an integer of [0,23]  
When the period is `hourly`, the parameter is the time of the first investment occurs.  
timeZone | String | Yes | UTC time zone, the value range is an integer of [-12,14]  
e.g. "8" representing UTC+8 (East 8 District), Beijing Time  
amt | String | Yes | Quantity invested per cycle  
investmentCcy | String | Yes | The invested quantity unit, can only be `USDT`/`USDC`  
tdMode | String | Yes | Trading mode  
Margin mode: `cross`  
Non-Margin mode: `cash`  
algoClOrdId | String | No | Client-supplied Algo ID  
There will be a value when algo order attaching algoClOrdId is triggered, or it will be "".  
A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters.  
tag | String | No | Order tag  
A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 16 characters.  
tradeQuoteCcy | String | No | The quote currency for trading.  
source | Array | No | Funding source  
`1`: Trading account  
`2`: Funding account  
`3`: Simple earn account  
Default is `1`  
recurringTimeType | String | No | Recurring buy time type  
`1`: Custom time  
`2`: Immediate trigger  
Default is `1`  
  
> Response Example
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
            {
                "algoId":"560472804207104000",
                "algoClOrdId":"",
                "sCode":"0",
                "sMsg":"",
                "tag":""
            }
        ]
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
algoId | String | Algo ID  
algoClOrdId | String | Client-supplied Algo ID  
sCode | String | The code of the event execution result, 0 means success  
sMsg | String | Rejection message if the request is unsuccessful  
tag | String | Order tag  
  
### POST / Amend recurring buy order

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: User ID

#### HTTP Request

`POST /api/v5/tradingBot/recurring/amend-order-algo`

> Request Example
    
    
    POST /api/v5/tradingBot/recurring/amend-order-algo
    body
    {
        "algoId":"448965992920907776",
        "stgyName":"stg1"
    }
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
algoId | String | Yes | Algo ID  
stgyName | String | Yes | New custom name for trading bot after adjustment, no more than 40 characters  
  
> Response Example
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
            {
                "algoId":"448965992920907776",
                "algoClOrdId":"",
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
sCode | String | The code of the event execution result, 0 means success  
sMsg | String | Rejection message if the request is unsuccessful  
  
### POST / Stop recurring buy order

A maximum of 10 orders can be stopped per request.

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: User ID

#### HTTP Request

`POST /api/v5/tradingBot/recurring/stop-order-algo`

> Request Example
    
    
    POST /api/v5/tradingBot/recurring/stop-order-algo
    body
    [
        {
            "algoId":"560472804207104000"
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
                "algoClOrdId": "",
                "algoId": "1839309556514557952",
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
sCode | String | The code of the event execution result, 0 means success  
sMsg | String | Rejection message if the request is unsuccessful  
tag | String | ~~Order tag~~(Deprecated)  
  
### GET / Recurring buy order list

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: User ID

#### HTTP Request

`GET /api/v5/tradingBot/recurring/orders-algo-pending`

> Request Example
    
    
    GET /api/v5/tradingBot/recurring/orders-algo-pending
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
algoId | String | No | Algo ID  
after | String | No | Pagination of data to return records earlier than the requested `algoId`.  
before | String | No | Pagination of data to return records newer than the requested `algoId`.  
limit | String | No | Number of results per request. The maximum is 100. The default is 100  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "algoClOrdId": "",
                "algoId": "644497312047435776",
                "algoOrdType": "recurring",
                "amt": "100",
                "cTime": "1699932133373",
                "cycles": "6",
                "instType": "SPOT",
                "investmentAmt": "0",
                "investmentCcy": "USDC",
                "mktCap": "0",
                "period": "hourly",
                "pnlRatio": "0",
                "recurringDay": "",
                "recurringHour": "1",
                "recurringList": [
                    {
                        "ccy": "BTC",
                        "ratio": "0.2",
                        "minPx": "",
                        "maxPx": ""
                    },
                    {
                        "ccy": "ETH",
                        "ratio": "0.8",
                        "minPx": "",
                        "maxPx": ""
                    }
                ],
                "recurringTime": "12",
                "state": "running",
                "stgyName": "stg1",
                "tag": "",
                "timeZone": "8",
                "totalAnnRate": "0",
                "totalPnl": "0",
                "uTime": "1699952473152",
                "tradeQuoteCcy": "USDT",
                "source": ["1"],
                "recurringTimeType": "1",
                "recurringTimeMinutes": "0"
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
cTime | String | Algo order created time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
uTime | String | Algo order updated time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
algoOrdType | String | Algo order type  
`recurring`: recurring buy  
state | String | Algo order state  
`running`  
`stopping`  
`pause`  
stgyName | String | Custom name for trading bot, no more than 40 characters  
recurringList | Array of objects | Recurring buy info  
> ccy | String | Recurring currency, e.g. `BTC`  
> ratio | String | Proportion of recurring currency assets, e.g. "0.2" representing 20%  
> minPx | String | Minimum price of recurring currency. `""` means no limit  
> maxPx | String | Maximum price of recurring currency. `""` means no limit  
period | String | Period  
`monthly`  
`weekly`  
`daily`  
`hourly`  
recurringDay | String | Recurring buy date  
When the period is `monthly`, the value range is an integer of [1,28]  
When the period is `weekly`, the value range is an integer of [1,7]  
recurringHour | String | Recurring buy by hourly  
`1`/`4`/`8`/`12`, e.g. `4` represents "recurring buy every 4 hour"  
recurringTime | String | Recurring buy time, the value range is an integer of [0,23]  
timeZone | String | UTC time zone, the value range is an integer of [-12,14]  
e.g. "8" representing UTC+8 (East 8 District), Beijing Time  
amt | String | Quantity invested per cycle  
investmentAmt | String | Accumulate quantity invested  
investmentCcy | String | The invested quantity unit, can only be `USDT`/`USDC`  
totalPnl | String | Total P&L  
totalAnnRate | String | Total annualized rate of yield  
pnlRatio | String | Rate of yield  
mktCap | String | Market value in unit of `USDT`  
cycles | String | Accumulate recurring buy cycles  
tag | String | Order tag  
tradeQuoteCcy | String | The quote currency for trading.  
source | Array | Funding source  
`1`: Trading account  
`2`: Funding account  
`3`: Simple earn account  
recurringTimeType | String | Recurring buy time type  
`1`: Custom time  
`2`: Immediate trigger  
recurringTimeMinutes | String | Recurring buy time in minutes, integer of [0,59]  
  
### GET / Recurring buy order history

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: User ID

#### HTTP Request

`GET /api/v5/tradingBot/recurring/orders-algo-history`

> Request Example
    
    
    GET /api/v5/tradingBot/recurring/orders-algo-history
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
algoId | String | No | Algo ID  
after | String | No | Pagination of data to return records earlier than the requested `algoId`.  
before | String | No | Pagination of data to return records newer than the requested `algoId`.  
limit | String | No | Number of results per request. The maximum is 100. The default is 100  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "algoClOrdId": "",
                "algoId": "644496098429767680",
                "algoOrdType": "recurring",
                "amt": "100",
                "cTime": "1699931844050",
                "cycles": "0",
                "instType": "SPOT",
                "investmentAmt": "0",
                "investmentCcy": "USDC",
                "mktCap": "0",
                "period": "hourly",
                "pnlRatio": "0",
                "recurringDay": "",
                "recurringHour": "1",
                "recurringList": [
                    {
                        "ccy": "BTC",
                        "ratio": "0.2",
                        "minPx": "",
                        "maxPx": ""
                    },
                    {
                        "ccy": "ETH",
                        "ratio": "0.8",
                        "minPx": "",
                        "maxPx": ""
                    }
                ],
                "recurringTime": "0",
                "state": "stopped",
                "stgyName": "stg1",
                "tag": "",
                "timeZone": "8",
                "totalAnnRate": "0",
                "totalPnl": "0",
                "uTime": "1699932177659",
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
cTime | String | Algo order created time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
uTime | String | Algo order updated time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
algoOrdType | String | Algo order type  
`recurring`: recurring buy  
state | String | Algo order state  
`stopped`  
stgyName | String | Custom name for trading bot, no more than 40 characters  
recurringList | Array of objects | Recurring buy info  
> ccy | String | Recurring currency, e.g. `BTC`  
> ratio | String | Proportion of recurring currency assets, e.g. "0.2" representing 20%  
> minPx | String | Minimum price of recurring currency. `""` means no limit  
> maxPx | String | Maximum price of recurring currency. `""` means no limit  
period | String | Period  
`monthly`  
`weekly`  
`daily`  
`hourly`  
recurringDay | String | Recurring buy date  
When the period is `monthly`, the value range is an integer of [1,28]  
When the period is `weekly`, the value range is an integer of [1,7]  
recurringHour | String | Recurring buy by hourly  
`1`/`4`/`8`/`12`, e.g. `4` represents "recurring buy every 4 hour"  
recurringTime | String | Recurring buy time, the value range is an integer of [0,23]  
timeZone | String | UTC time zone, the value range is an integer of [-12,14]  
e.g. "8" representing UTC+8 (East 8 District), Beijing Time  
amt | String | Quantity invested per cycle  
investmentAmt | String | Accumulate quantity invested  
investmentCcy | String | The invested quantity unit, can only be `USDT`/`USDC`  
totalPnl | String | Total P&L  
totalAnnRate | String | Total annualized rate of yield  
pnlRatio | String | Rate of yield  
mktCap | String | Market value in unit of `USDT`  
cycles | String | Accumulate recurring buy cycles  
tag | String | Order tag  
tradeQuoteCcy | String | The quote currency for trading.  
source | Array | Funding source  
`1`: Trading account  
`2`: Funding account  
`3`: Simple earn account  
recurringTimeType | String | Recurring buy time type  
`1`: Custom time  
`2`: Immediate trigger  
recurringTimeMinutes | String | Recurring buy time in minutes, integer of [0,59]  
  
### GET / Recurring buy order details

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: User ID

#### HTTP Request

`GET /api/v5/tradingBot/recurring/orders-algo-details`

> Request Example
    
    
    GET /api/v5/tradingBot/recurring/orders-algo-details?algoId=644497312047435776
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
algoId | String | Yes | Algo ID  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "algoClOrdId": "",
                "algoId": "644497312047435776",
                "algoOrdType": "recurring",
                "amt": "100",
                "cTime": "1699932133373",
                "cycles": "6",
                "instType": "SPOT",
                "investmentAmt": "0",
                "investmentCcy": "USDC",
                "mktCap": "0",
                "nextInvestTime": "1699956005500",
                "period": "hourly",
                "pnlRatio": "0",
                "recurringDay": "",
                "recurringHour": "1",
                "recurringList": [
                    {
                        "avgPx": "0",
                        "ccy": "BTC",
                        "profit": "0",
                        "px": "36683.2",
                        "ratio": "0.2",
                        "minPx": "",
                        "maxPx": "",
                        "totalAmt": "0"
                    },
                    {
                        "avgPx": "0",
                        "ccy": "ETH",
                        "profit": "0",
                        "px": "2058.36",
                        "ratio": "0.8",
                        "minPx": "",
                        "maxPx": "",
                        "totalAmt": "0"
                    }
                ],
                "recurringTime": "12",
                "state": "running",
                "stgyName": "stg1",
                "tag": "",
                "timeZone": "8",
                "totalAnnRate": "0",
                "totalPnl": "0",
                "uTime": "1699952485451",
                "tradeQuoteCcy": "USDT"，
                "source": ["1"],
                "recurringTimeType": "1",
                "recurringTimeMinutes": "0"
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
cTime | String | Algo order created time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
uTime | String | Algo order updated time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
algoOrdType | String | Algo order type  
`recurring`: recurring buy  
state | String | Algo order state  
`running`  
`stopping`  
`stopped`  
`pause`  
stgyName | String | Custom name for trading bot, no more than 40 characters  
recurringList | Array of objects | Recurring buy info  
> ccy | String | Recurring buy currency, e.g. `BTC`  
> ratio | String | Proportion of recurring currency assets, e.g. "0.2" representing 20%  
> minPx | String | Minimum price of recurring currency. `""` means no limit  
> maxPx | String | Maximum price of recurring currency. `""` means no limit  
> totalAmt | String | Accumulated quantity in unit of recurring buy currency  
> profit | String | Profit in unit of `investmentCcy`  
> avgPx | String | Average price of recurring buy, quote currency is `investmentCcy`  
> px | String | Current market price, quote currency is `investmentCcy`  
period | String | Period  
`monthly`  
`weekly`  
`daily`  
`hourly`  
recurringDay | String | Recurring buy date  
When the period is `monthly`, the value range is an integer of [1,28]  
When the period is `weekly`, the value range is an integer of [1,7]  
recurringHour | String | Recurring buy by hourly  
`1`/`4`/`8`/`12`, e.g. `4` represents "recurring buy every 4 hour"  
recurringTime | String | Recurring buy time, the value range is an integer of [0,23]  
timeZone | String | UTC time zone, the value range is an integer of [-12,14]  
e.g. "8" representing UTC+8 (East 8 District), Beijing Time  
amt | String | Quantity invested per cycle  
investmentAmt | String | Accumulate quantity invested  
investmentCcy | String | The invested quantity unit, can only be `USDT`/`USDC`  
nextInvestTime | String | Next invest time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
totalPnl | String | Total P&L  
totalAnnRate | String | Total annualized rate of yield  
pnlRatio | String | Rate of yield  
mktCap | String | Market value in unit of `USDT`  
cycles | String | Accumulate recurring buy cycles  
tag | String | Order tag  
tradeQuoteCcy | String | The quote currency for trading.  
source | Array | Funding source  
`1`: Trading account  
`2`: Funding account  
`3`: Simple earn account  
recurringTimeType | String | Recurring buy time type  
`1`: Custom time  
`2`: Immediate trigger  
recurringTimeMinutes | String | Recurring buy time in minutes, integer of [0,59]  
  
### GET / Recurring buy sub orders

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: User ID

#### HTTP Request

`GET /api/v5/tradingBot/recurring/sub-orders`

> Request Example
    
    
    GET /api/v5/tradingBot/recurring/sub-orders?algoId=560516615079727104
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
algoId | String | Yes | Algo ID  
ordId | String | No | Sub order ID  
after | String | No | Pagination of data to return records earlier than the requested `algoId`.  
before | String | No | Pagination of data to return records newer than the requested `algoId`.  
limit | String | No | Number of results per request. The maximum is 100. The default is 100  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "accFillSz": "0.045315",
                "algoClOrdId": "",
                "algoId": "560516615079727104",
                "algoOrdType": "recurring",
                "avgPx": "1765.4",
                "cTime": "1679911222200",
                "fee": "-0.0000317205",
                "feeCcy": "ETH",
                "instId": "ETH-USDC",
                "instType": "SPOT",
                "ordId": "560523524230717440",
                "ordType": "market",
                "px": "-1",
                "side": "buy",
                "state": "filled",
                "sz": "80",
                "tag": "",
                "tdMode": "",
                "uTime": "1679911222207"
            },
            {
                "accFillSz": "0.00071526",
                "algoClOrdId": "",
                "algoId": "560516615079727104",
                "algoOrdType": "recurring",
                "avgPx": "27961.6",
                "cTime": "1679911222189",
                "fee": "-0.000000500682",
                "feeCcy": "BTC",
                "instId": "BTC-USDC",
                "instType": "SPOT",
                "ordId": "560523524184580096",
                "ordType": "market",
                "px": "-1",
                "side": "buy",
                "state": "filled",
                "sz": "20",
                "tag": "",
                "tdMode": "",
                "uTime": "1679911222194"
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
algoId | String | Algo ID  
instType | String | Instrument type  
instId | String | Instrument ID  
algoOrdType | String | Algo order type  
`recurring`: recurring buy  
ordId | String | Sub order ID  
cTime | String | Sub order created time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
uTime | String | Sub order updated time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
tdMode | String | Sub order trade mode  
Margin mode : `cross`  
Non-Margin mode : `cash`  
ordType | String | Sub order type  
`market`: Market order  
`manual_add_order`: Manual add investment order  
sz | String | Sub order quantity to buy or sell  
state | String | Sub order state  
`canceled`  
`live`  
`partially_filled`  
`filled`  
`cancelling`  
side | String | Sub order side  
`buy` `sell`  
px | String | Sub order limit price  
If it is a market order, "-1" will be return  
fee | String | Sub order fee  
feeCcy | String | Sub order fee currency  
avgPx | String | Sub order average filled price  
accFillSz | String | Sub order accumulated fill quantity  
tag | String | Order tag  
algoClOrdId | String | Client-supplied Algo ID  
  
### WS / Recurring buy orders channel

Retrieve recurring buy orders. Data will be pushed when triggered by events. It will also be pushed in regular interval according to subscription granularity.

#### URL Path

/ws/v5/business (required login)

> Request Example
    
    
    {
        "id": "1512",
        "op": "subscribe",
        "args": [{
            "channel": "algo-recurring-buy",
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
            "channel": "algo-recurring-buy",
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
`algo-recurring-buy`  
> instType | String | Yes | Instrument type  
`SPOT`  
`ANY`  
> algoId | String | No | Algo Order ID  
  
> Successful Response Example
    
    
    {
        "id": "1512",
        "event": "subscribe",
        "arg": {
            "channel": "algo-recurring-buy",
            "instType": "SPOT"
        },
            "connId": "a4d3ae55"
    }
    

> Failure Response Example
    
    
    {
      "id": "1512",
      "event": "error",
      "code": "60012",
      "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{ \"channel\" : \"algo-recurring-buy\", \"instType\" : \"FUTURES\"}]}",
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
> algoId | String | No | Algo Order ID  
code | String | No | Error code  
msg | String | No | Error message  
connId | String | Yes | WebSocket connection ID  
  
> Push Data Example: 
    
    
    {
        "arg": {
            "channel": "algo-recurring-buy",
            "instType": "SPOT",
            "uid": "447*******584"
        },
        "data": [{
            "algoClOrdId": "",
            "algoId": "644497312047435776",
            "algoOrdType": "recurring",
            "amt": "100",
            "cTime": "1699932133373",
            "cycles": "0",
            "instType": "SPOT",
            "investmentAmt": "0",
            "investmentCcy": "USDC",
            "mktCap": "0",
            "nextInvestTime": "1699934415300",
            "pTime": "1699933314691",
            "period": "hourly",
            "pnlRatio": "0",
            "recurringDay": "",
            "recurringHour": "1",
            "recurringList": [{
                "avgPx": "0",
                "ccy": "BTC",
                "profit": "0",
                "px": "36482",
                "ratio": "0.2",
                "minPx": "30000",
                "maxPx": "50000"
                "totalAmt": "0"
            }, {
                "avgPx": "0",
                "ccy": "ETH",
                "profit": "0",
                "px": "2057.54",
                "ratio": "0.8",
                "minPx": "",
                "maxPx": "",
                "totalAmt": "0"
            }],
            "recurringTime": "12",
            "state": "running",
            "stgyName": "stg1",
            "tag": "",
            "timeZone": "8",
            "totalAnnRate": "0",
            "totalPnl": "0",
            "uTime": "1699932136249",
            "tradeQuoteCcy": "USDT"
        }]
    }
    

#### Response parameters when data is pushed.

**Parameter** | **Type** | **Description**  
---|---|---  
arg | Object | Successfully subscribed channel  
> channel | String | Channel name  
> instType | String | Instrument type  
> algoId | String | Algo Order ID  
> uid | String | User ID  
data | Array of objects | Subscribed data  
> algoId | String | Algo ID  
> algoClOrdId | String | Client-supplied Algo ID  
> instType | String | Instrument type  
> cTime | String | Algo order created time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
> uTime | String | Algo order updated time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
> algoOrdType | String | Algo order type  
`recurring`: recurring buy  
> state | String | Algo order state  
`running`  
`stopping`  
`stopped`  
`pause`  
> stgyName | String | Custom name for trading bot, no more than 40 characters  
> recurringList | Array of objects | Recurring buy info  
>> ccy | String | Recurring buy currency, e.g. `BTC`  
>> ratio | String | Proportion of recurring currency assets, e.g. "0.2" representing 20%  
>> minPx | String | Minimum price of price range. `""` means no limit  
>> maxPx | String | Maximum price of price range. `""` means no limit  
>> totalAmt | String | Accumulated quantity in unit of recurring buy currency  
>> profit | String | Profit in unit of `investmentCcy`  
>> avgPx | String | Average price of recurring buy, quote currency is `investmentCcy`  
>> px | String | Current market price, quote currency is `investmentCcy`  
> period | String | Period  
`monthly`  
`weekly`  
`daily`  
`hourly`  
> recurringDay | String | Recurring buy date  
When the period is `monthly`, the value range is an integer of [1,28]  
When the period is `weekly`, the value range is an integer of [1,7]  
> recurringHour | String | Recurring buy by hourly  
`1`/`4`/`8`/`12`, e.g. `4` represents "recurring buy every 4 hour"  
> recurringTime | String | Recurring buy time, the value range is an integer of [0,23]  
> timeZone | String | UTC time zone, the value range is an integer of [-12,14]  
e.g. "8" representing UTC+8 (East 8 District), Beijing Time  
> amt | String | Quantity invested per cycle  
> investmentAmt | String | Accumulate quantity invested  
> investmentCcy | String | The invested quantity unit, can only be `USDT`/`USDC`  
> nextInvestTime | String | Next invest time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
> totalPnl | String | Total P&L  
> totalAnnRate | String | Total annualized rate of yield  
> pnlRatio | String | Rate of yield  
> mktCap | String | Market value in unit of `USDT`  
> cycles | String | Accumulate recurring buy cycles  
> tag | String | Order tag  
> pTime | String | Push time of algo order information, Unix timestamp format in milliseconds, e.g. `1597026383085`  
> tradeQuoteCcy | String | The quote currency for trading.  
> recurringTimeType | String | Recurring buy time type  
> recurringTimeMinutes | String | Custom recurring buy minutes  
> source | Array | Source of recurring buy  
  
### POST / Amend recurring buy time

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: User ID

#### HTTP Request

`POST /api/v5/tradingBot/recurring/amend-recurring-time`

> Request Example
    
    
    POST /api/v5/tradingBot/recurring/amend-recurring-time
    body
    {
        "algoId": "2837428373700509696",
        "recurringTimeType": "1",
        "period": "hourly",
        "recurringHour": "8",
        "recurringDay": "1",
        "recurringTime": "11",
        "timeZone": "8"
    }
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
algoId | String | Yes | Algo ID  
recurringTimeType | String | Yes | Recurring buy time type  
`1`: Custom time  
`2`: Immediate trigger  
timeZone | String | Yes | UTC time zone, the value range is an integer of [-12,14]  
e.g. `8` representing UTC+8 (East 8 District), Beijing Time  
period | String | Yes | Period  
`monthly`  
`weekly`  
`daily`  
`hourly`  
recurringHour | String | Conditional | Recurring buy by hourly  
`1`/`4`/`8`/`12`, e.g. `1` represents "recurring buy every 1 hour"  
Required when `period` is `hourly`  
recurringDay | String | Conditional | Recurring buy date  
When the period is `monthly`, the value range is an integer of [1,28]  
When the period is `weekly`, the value range is an integer of [1,7]  
When the period is `daily`/`hourly`, the parameter is not required  
Only required when `recurringTimeType` is `1`  
recurringTime | String | Conditional | Recurring buy time, the value range is an integer of [0,23]  
Only required when `recurringTimeType` is `1`  
  
> Response Example
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "sCode": "0",
                "sMsg": ""
            }
        ]
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
algoId | String | Algo order ID  
sCode | String | Event execution status code, `0` indicates success  
sMsg | String | Error message if the event execution failed  
  
### POST / Amend recurring buy amount

#### Rate Limit: 20 requests per 2 seconds

#### Rate Limit Rule: User ID

#### HTTP Request

`POST /api/v5/tradingBot/recurring/amend-recurring-amount`

> Request Example
    
    
    POST /api/v5/tradingBot/recurring/amend-recurring-amount
    body
    {
        "algoId": "2837428373700509696",
        "amount": "20"
    }
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
algoId | String | Yes | Algo order ID  
amount | String | Yes | Amended recurring buy amount. Only the investment currency used when the strategy was created is supported  
  
> Response Example
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "algoId": "2837428373700509696",
                "sCode": "0",
                "sMsg": ""
            }
        ]
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
algoId | String | Algo order ID  
sCode | String | Event execution status code, `0` indicates success  
sMsg | String | Error message if the event execution failed  
  
### POST / Add investment

#### Rate Limit: 20 requests per 2 seconds

#### Rate Limit Rule: User ID

#### HTTP Request

`POST /api/v5/tradingBot/recurring/add-investment`

> Request Example
    
    
    POST /api/v5/tradingBot/recurring/add-investment
    body
    {
        "algoId": "2837428373700509696",
        "amount": "20"
    }
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
algoId | String | Yes | Algo order ID  
amount | String | Yes | Additional investment amount. Only the investment currency used when the strategy was created is supported  
  
> Response Example
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "algoId": "2837428373700509696",
                "sCode": "0",
                "sMsg": ""
            }
        ]
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
algoId | String | Algo order ID  
sCode | String | Event execution status code, `0` indicates success  
sMsg | String | Error message if the event execution failed  
  
### POST / Pause recurring buy

#### Rate Limit: 20 requests per 2 seconds

#### Rate Limit Rule: User ID

#### HTTP Request

`POST /api/v5/tradingBot/recurring/pause`

> Request Example
    
    
    POST /api/v5/tradingBot/recurring/pause
    body
    {
        "algoId": "2837428373700509696"
    }
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
algoId | String | Yes | Algo order ID  
  
> Response Example
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "algoId": "2837428373700509696",
                "sCode": "0",
                "sMsg": ""
            }
        ]
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
algoId | String | Algo order ID  
sCode | String | Event execution status code, `0` indicates success  
sMsg | String | Error message if the event execution failed  
  
### POST / Restart recurring buy

#### Rate Limit: 20 requests per 2 seconds

#### Rate Limit Rule: User ID

#### HTTP Request

`POST /api/v5/tradingBot/recurring/restart`

> Request Example
    
    
    POST /api/v5/tradingBot/recurring/restart
    body
    {
        "algoId": "2837428373700509696"
    }
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
algoId | String | Yes | Algo order ID  
  
> Response Example
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "algoId": "2837428373700509696",
                "sCode": "0",
                "sMsg": ""
            }
        ]
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
algoId | String | Algo order ID  
sCode | String | Event execution status code, `0` indicates success  
sMsg | String | Error message if the event execution failed  
  
### POST / Amend price range

#### Rate Limit: 20 requests per 2 seconds

#### Rate Limit Rule: User ID

#### HTTP Request

`POST /api/v5/tradingBot/recurring/amend-price-range`

> Request Example
    
    
    POST /api/v5/tradingBot/recurring/amend-price-range
    body
    {
        "algoId": "2837428373700509696",
        "recurringList": [
            {
                "ccy": "BTC",
                "minPx": "80000",
                "maxPx": "120000"
            }
        ]
    }
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
algoId | String | Yes | Algo order ID  
recurringList | Array | Yes | Price range settings. The currency must be within the scope of the recurring buy currencies  
>ccy | String | Yes | Recurring buy currency  
>minPx | String | Yes | Minimum price of price range. `""` means no limit  
>maxPx | String | Yes | Maximum price of price range. `""` means no limit  
  
> Response Example
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "algoId": "2837428373700509696",
                "sCode": "0",
                "sMsg": ""
            }
        ]
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
algoId | String | Algo order ID  
sCode | String | Event execution status code, `0` indicates success  
sMsg | String | Error message if the event execution failed

---

# 定投

定投是以固定的时间周期，投入固定的金额买入选定币种的策略。在市场波动较为剧烈时，运用适当的定投策略，以同样的投资额度可以在低点购入更多的筹码，可以使用户获得更加可观的收益。[了解更多](/cn/help/vii-recurring-buy)  
`定投`功能模块下的API接口需要身份验证。  
  
### POST / 定投策略委托下单 

#### 限速：20次/2s

#### 限速规则 ：User ID

#### HTTP请求

`POST /api/v5/tradingBot/recurring/order-algo`

> 请求示例
    
    
    POST /api/v5/tradingBot/recurring/order-algo
    body
    {
      "stgyName": "BTC|ETH recurring buy monthly",     
      "amt":"100",
      "recurringList":[    
        {
             "ccy":"BTC",
             "ratio":"0.2"
        },
        {
             "ccy":"ETH",
             "ratio":"0.8"
        }
      ],
      "period":"monthly",
      "recurringDay":"1",
      "recurringTime":"0",
      "timeZone":"8",   // 东8区
      "tdMode":"cross",
      "investmentCcy":"USDT"
    }
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
stgyName | String | 是 | 策略自定义名称，不超过40个字符  
recurringList | Array of objects | 是 | 定投信息  
> ccy | String | 是 | 定投币种，如 `BTC`  
> ratio | String | 是 | 定投币种资产占比，如 "0.2"代表占比20%  
> minPx | String | 否 | 定投币种价格下限，`""`代表没有限制  
> maxPx | String | 否 | 定投币种价格上限，`""`代表没有限制  
period | String | 是 | 周期类型  
`monthly`：月  
`weekly`：周  
`daily`：日  
`hourly`：小时  
recurringDay | String | 可选 | 投资日  
当周期类型为`monthly`，则取值范围是 [1,28] 的整数  
当周期类型为`weekly`，则取值范围是 [1,7] 的整数  
当周期类型为`daily`/`hourly`，该参数可不填。  
recurringHour | String | 可选 | 小时级别定投的间隔  
`1`/`4`/`8`/`12`  
如：`1`代表每隔`1`个小时定投  
当周期类型选择`hourly`，该字段必填。  
recurringTime | String | 是 | 投资时间，取值范围是 [0,23] 的整数  
当周期类型选择`hourly`代表首次定投发生的时间  
timeZone | String | 是 | 时区（UTC），取值范围是 [-12,14] 的整数  
如 `8`表示UTC+8（东8区），北京时间  
amt | String | 是 | 每期投入数量  
investmentCcy | String | 是 | 投入数量单位，只能是`USDT`/`USDC`  
tdMode | String | 是 | 交易模式  
`跨币种保证金模式`/`组合保证金模式`下选择 `cross`：全仓  
`现货模式`/`合约模式`下选择 `cash`：非保证金  
algoClOrdId | String | 否 | 客户自定义订单ID  
字母（区分大小写）与数字的组合，可以是纯字母、纯数字且长度要在1-32位之间。  
tag | String | 否 | 订单标签  
字母（区分大小写）与数字的组合，可以是纯字母、纯数字，且长度在1-16位之间。  
tradeQuoteCcy | String | 否 | 用于交易的计价币种。  
source | Array | 否 | 资金来源  
`1`：交易账户  
`2`：资金账户  
`3`：简单赚币账户  
默认为`1`  
recurringTimeType | String | 否 | 定投周期类型  
`1`：自定义时间  
`2`：立即触发  
默认为`1`  
  
> 返回结果
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
            {
                "algoId":"560472804207104000",
                "algoClOrdId":"",
                "sCode":"0",
                "sMsg":"",
                "tag":""
            }
        ]
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
algoId | String | 策略订单ID  
algoClOrdId | String | 客户自定义订单ID  
sCode | String | 事件执行结果的code，0代表成功  
sMsg | String | 事件执行失败时的msg  
tag | String | 订单标签  
  
### POST / 修改定投策略订单 

#### 限速：20次/2s

#### 限速规则：User ID

#### HTTP请求

`POST /api/v5/tradingBot/recurring/amend-order-algo`

> 请求示例
    
    
    POST /api/v5/tradingBot/recurring/amend-order-algo
    body
    {
        "algoId":"448965992920907776",
        "stgyName":"stg1"
    }
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
algoId | String | 是 | 策略订单ID  
stgyName | String | 是 | 调整后的策略自定义名称  
  
> 返回结果
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
            {
                "algoId":"448965992920907776",
                "algoClOrdId":"",
                "sCode":"0",
                "sMsg":""
            }
        ]
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
algoId | String | 策略订单ID  
algoClOrdId | String | 客户自定义订单ID  
sCode | String | 事件执行结果的code，0代表成功  
sMsg | String | 事件执行失败时的msg  
  
### POST / 定投策略停止 

每次最多可以撤销10个定投策略订单。

#### 限速：20次/2s

#### 限速规则：User ID

#### HTTP请求

`POST /api/v5/tradingBot/recurring/stop-order-algo`

> 请求示例
    
    
    POST /api/v5/tradingBot/recurring/stop-order-algo
    body
    [
        {
            "algoId":"560472804207104000"
        }
    ]
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
algoId | String | 是 | 策略订单ID  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "algoClOrdId": "",
                "algoId": "1839309556514557952",
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
algoClOrdId | String | 客户自定义订单ID  
sCode | String | 事件执行结果的code，0代表成功  
sMsg | String | 事件执行失败时的msg  
tag | String | ~~订单标签~~ （已废弃）  
  
### GET / 获取未完成定投策略委托单列表 

#### 限速：20次/2s

#### 限速规则：User ID

#### HTTP请求

`GET /api/v5/tradingBot/recurring/orders-algo-pending`

> 请求示例
    
    
    GET /api/v5/tradingBot/recurring/orders-algo-pending
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
algoId | String | 否 | 策略订单ID  
after | String | 否 | 请求此ID之前（更旧的数据）的分页内容，传的值为对应接口的`algoId`  
before | String | 否 | 请求此ID之后（更新的数据）的分页内容，传的值为对应接口的`algoId`  
limit | String | 否 | 返回结果的数量，最大为100，默认100条  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "algoClOrdId": "",
                "algoId": "644497312047435776",
                "algoOrdType": "recurring",
                "amt": "100",
                "cTime": "1699932133373",
                "cycles": "6",
                "instType": "SPOT",
                "investmentAmt": "0",
                "investmentCcy": "USDC",
                "mktCap": "0",
                "period": "hourly",
                "pnlRatio": "0",
                "recurringDay": "",
                "recurringHour": "1",
                "recurringList": [
                    {
                        "ccy": "BTC",
                        "ratio": "0.2",
                        "minPx": "",
                        "maxPx": ""
                    },
                    {
                        "ccy": "ETH",
                        "ratio": "0.8",
                        "minPx": "",
                        "maxPx": ""
                    }
                ],
                "recurringTime": "12",
                "state": "running",
                "stgyName": "stg1",
                "tag": "",
                "timeZone": "8",
                "totalAnnRate": "0",
                "totalPnl": "0",
                "uTime": "1699952473152",
                "tradeQuoteCcy": "USDT",
                "source": ["1"],
                "recurringTimeType": "1",
                "recurringTimeMinutes": "0"
            }
        ],
        "msg": ""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
algoId | String | 策略订单ID  
algoClOrdId | String | 客户自定义订单ID  
instType | String | 产品类型  
`SPOT`：现货  
cTime | String | 策略订单创建时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
uTime | String | 策略订单更新时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
algoOrdType | String | 策略订单类型  
`recurring`：定投  
state | String | 订单状态  
`running`：运行中  
`stopping`：终止中  
`pause`: 已暂停  
stgyName | String | 策略自定义名称，不超过40个字符  
recurringList | Array of objects | 定投信息  
> ccy | String | 定投币种，如 `BTC`  
> ratio | String | 定投币种资产占比，如 "0.2"代表占比20%  
> minPx | String | 定投币种价格下限，`""`代表没有限制  
> maxPx | String | 定投币种价格上限，`""`代表没有限制  
period | String | 周期类型  
`monthly`：月  
`weekly`：周  
`daily`：日  
`hourly`：小时  
recurringDay | String | 投资日  
当周期类型为`monthly`，则取值范围是 [1,28] 的整数  
当周期类型为`weekly`，则取值范围是 [1,7] 的整数  
recurringHour | String | 小时级别定投的间隔  
`1`/`4`/`8`/`12`  
如：`1`代表每隔`1`个小时定投  
recurringTime | String | 投资时间，取值范围是 [0,23] 的整数  
timeZone | String | 时区（UTC），取值范围是 [-12,14] 的整数  
如 `8`表示UTC+8（东8区），北京时间  
amt | String | 每期投入数量  
investmentAmt | String | 累计投入数量  
investmentCcy | String | 投入数量单位，只能是`USDT`/`USDC`  
totalPnl | String | 总收益  
totalAnnRate | String | 总年化  
pnlRatio | String | 收益率  
mktCap | String | 当前总市值，单位为`USDT`  
cycles | String | 定投累计轮数  
tag | String | 订单标签  
tradeQuoteCcy | String | 用于交易的计价币种。  
source | Array | 资金来源  
`1`：交易账户  
`2`：资金账户  
`3`：简单赚币账户  
recurringTimeType | String | 定投周期类型  
`1`：自定义时间  
`2`：立即触发  
recurringTimeMinutes | String | 定投时间（分钟），取值范围是 [0,59] 的整数  
  
### GET / 获取历史定投策略委托单列表 

#### 限速：20次/2s

#### 限速规则：User ID

#### HTTP请求

`GET /api/v5/tradingBot/recurring/orders-algo-history`

> 请求示例
    
    
    GET /api/v5/tradingBot/recurring/orders-algo-history
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
algoId | String | 否 | 策略订单ID  
after | String | 否 | 请求此ID之前（更旧的数据）的分页内容，传的值为对应接口的`algoId`  
before | String | 否 | 请求此ID之后（更新的数据）的分页内容，传的值为对应接口的`algoId`  
limit | String | 否 | 返回结果的数量，最大为100，默认100条  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "algoClOrdId": "",
                "algoId": "644496098429767680",
                "algoOrdType": "recurring",
                "amt": "100",
                "cTime": "1699931844050",
                "cycles": "0",
                "instType": "SPOT",
                "investmentAmt": "0",
                "investmentCcy": "USDC",
                "mktCap": "0",
                "period": "hourly",
                "pnlRatio": "0",
                "recurringDay": "",
                "recurringHour": "1",
                "recurringList": [
                    {
                        "ccy": "BTC",
                        "ratio": "0.2",
                        "minPx": "",
                        "maxPx": ""
                    },
                    {
                        "ccy": "ETH",
                        "ratio": "0.8",
                        "minPx": "",
                        "maxPx": ""
                    }
                ],
                "recurringTime": "0",
                "state": "stopped",
                "stgyName": "stg1",
                "tag": "",
                "timeZone": "8",
                "totalAnnRate": "0",
                "totalPnl": "0",
                "uTime": "1699932177659",
                "tradeQuoteCcy": "USDT"
            }
        ],
        "msg": ""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
algoId | String | 策略订单ID  
algoClOrdId | String | 客户自定义订单ID  
instType | String | 产品类型  
`SPOT`：现货  
cTime | String | 策略订单创建时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
uTime | String | 策略订单更新时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
algoOrdType | String | 策略订单类型  
`recurring`：定投  
state | String | 订单状态  
`stopped`：已停止  
stgyName | String | 策略自定义名称，不超过40个字符  
recurringList | Array of objects | 定投信息  
> ccy | String | 定投币种，如 `BTC`  
> ratio | String | 定投币种资产占比，如 "0.2"代表占比20%  
> minPx | String | 定投币种价格下限，`""`代表没有限制  
> maxPx | String | 定投币种价格上限，`""`代表没有限制  
period | String | 周期类型  
`monthly`：月  
`weekly`：周  
`daily`：日  
`hourly`：小时  
recurringDay | String | 投资日  
当周期类型为`monthly`，则取值范围是 [1,28] 的整数  
当周期类型为`weekly`，则取值范围是 [1,7] 的整数  
recurringHour | String | 小时级别定投的间隔  
`1`/`4`/`8`/`12`  
如：`1`代表每隔`1`个小时定投  
recurringTime | String | 投资时间，取值范围是 [0,23] 的整数  
timeZone | String | 时区（UTC），取值范围是 [-12,14] 的整数  
如 `8`表示UTC+8（东8区），北京时间  
amt | String | 每期投入数量  
investmentAmt | String | 累计投入数量  
investmentCcy | String | 投入数量单位，只能是`USDT`/`USDC`  
totalPnl | String | 总收益  
totalAnnRate | String | 总年化  
pnlRatio | String | 收益率  
mktCap | String | 当前总市值，单位为`USDT`  
cycles | String | 定投累计轮数  
tag | String | 订单标签  
tradeQuoteCcy | String | 用于交易的计价币种。  
source | Array | 资金来源  
`1`：交易账户  
`2`：资金账户  
`3`：简单赚币账户  
recurringTimeType | String | 定投周期类型  
`1`：自定义时间  
`2`：立即触发  
recurringTimeMinutes | String | 定投时间（分钟），取值范围是 [0,59] 的整数  
  
### GET / 获取定投策略委托订单详情 

#### 限速：20次/2s

#### 限速规则：User ID

#### HTTP请求

`GET /api/v5/tradingBot/recurring/orders-algo-details`

> 请求示例
    
    
    GET /api/v5/tradingBot/recurring/orders-algo-details?algoId=644497312047435776
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
algoId | String | 是 | 策略订单ID  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "algoClOrdId": "",
                "algoId": "644497312047435776",
                "algoOrdType": "recurring",
                "amt": "100",
                "cTime": "1699932133373",
                "cycles": "6",
                "instType": "SPOT",
                "investmentAmt": "0",
                "investmentCcy": "USDC",
                "mktCap": "0",
                "nextInvestTime": "1699956005500",
                "period": "hourly",
                "pnlRatio": "0",
                "recurringDay": "",
                "recurringHour": "1",
                "recurringList": [
                    {
                        "avgPx": "0",
                        "ccy": "BTC",
                        "profit": "0",
                        "px": "36683.2",
                        "ratio": "0.2",
                        "minPx": "",
                        "maxPx": "",
                        "totalAmt": "0"
                    },
                    {
                        "avgPx": "0",
                        "ccy": "ETH",
                        "profit": "0",
                        "px": "2058.36",
                        "ratio": "0.8",
                        "minPx": "",
                        "maxPx": "",
                        "totalAmt": "0"
                    }
                ],
                "recurringTime": "12",
                "state": "running",
                "stgyName": "stg1",
                "tag": "",
                "timeZone": "8",
                "totalAnnRate": "0",
                "totalPnl": "0",
                "uTime": "1699952485451",
                "tradeQuoteCcy": "USDT"，
                "source": ["1"],
                "recurringTimeType": "1",
                "recurringTimeMinutes": "0"
            }
        ],
        "msg": ""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
algoId | String | 策略订单ID  
algoClOrdId | String | 客户自定义订单ID  
instType | String | 产品类型  
`SPOT`：现货  
cTime | String | 策略订单创建时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
uTime | String | 策略订单更新时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
algoOrdType | String | 策略订单类型  
`recurring`：定投  
state | String | 订单状态  
`running`：运行中  
`stopping`：终止中  
`stopped`：已停止  
`pause`: 已暂停  
stgyName | String | 策略自定义名称，不超过40个字符  
recurringList | Array of objects | 定投信息  
> ccy | String | 定投币种，如 `BTC`  
> ratio | String | 定投币种资产占比，如 "0.2"代表占比20%  
> minPx | String | 定投币种价格下限，`""`代表没有限制  
> maxPx | String | 定投币种价格上限，`""`代表没有限制  
> totalAmt | String | 累计购入定投币种的数量  
> profit | String | 定投收益，单位为`investmentCcy`  
> avgPx | String | 定投均价，计价单位为`investmentCcy`  
> px | String | 当前价格，计价单位为`investmentCcy`  
period | String | 周期类型  
`monthly`：月  
`weekly`：周  
`daily`：日  
`hourly`：小时  
recurringDay | String | 投资日  
当周期类型为`monthly`，则取值范围是 [1,28] 的整数  
当周期类型为`weekly`，则取值范围是 [1,7] 的整数  
recurringHour | String | 小时级别定投的间隔  
`1`/`4`/`8`/`12`  
如：`1`代表每隔`1`个小时定投  
recurringTime | String | 投资时间，取值范围是 [0,23] 的整数  
timeZone | String | 时区（UTC），取值范围是 [-12,14] 的整数  
如 `8`表示UTC+8（东8区），北京时间  
amt | String | 每期投入数量  
investmentAmt | String | 累计投入数量  
investmentCcy | String | 投入数量单位，只能是`USDT`/`USDC`  
nextInvestTime | String | 下一次定投发生的时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
totalPnl | String | 总收益  
totalAnnRate | String | 总年化  
pnlRatio | String | 收益率  
mktCap | String | 当前总市值，单位为`USDT`  
cycles | String | 定投累计轮数  
tag | String | 订单标签  
tradeQuoteCcy | String | 用于交易的计价币种。  
source | Array | 资金来源  
`1`：交易账户  
`2`：资金账户  
`3`：简单赚币账户  
recurringTimeType | String | 定投周期类型  
`1`：自定义时间  
`2`：立即触发  
recurringTimeMinutes | String | 定投时间（分钟），取值范围是 [0,59] 的整数  
  
### GET / 获取定投策略子订单信息 

#### 限速：20次/2s

#### 限速规则：User ID

#### HTTP请求

`GET /api/v5/tradingBot/recurring/sub-orders`

> 请求示例
    
    
    GET /api/v5/tradingBot/recurring/sub-orders?algoId=560516615079727104
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
algoId | String | 是 | 策略订单ID  
ordId | String | 否 | 子订单ID  
after | String | 否 | 请求此ID之前（更旧的数据）的分页内容，传的值为对应接口的`ordId`  
before | String | 否 | 请求此ID之后（更新的数据）的分页内容，传的值为对应接口的`ordId`  
limit | String | 否 | 返回结果的数量，最大为300，默认300条  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "accFillSz": "0.045315",
                "algoClOrdId": "",
                "algoId": "560516615079727104",
                "algoOrdType": "recurring",
                "avgPx": "1765.4",
                "cTime": "1679911222200",
                "fee": "-0.0000317205",
                "feeCcy": "ETH",
                "instId": "ETH-USDC",
                "instType": "SPOT",
                "ordId": "560523524230717440",
                "ordType": "market",
                "px": "-1",
                "side": "buy",
                "state": "filled",
                "sz": "80",
                "tag": "",
                "tdMode": "",
                "uTime": "1679911222207"
            },
            {
                "accFillSz": "0.00071526",
                "algoClOrdId": "",
                "algoId": "560516615079727104",
                "algoOrdType": "recurring",
                "avgPx": "27961.6",
                "cTime": "1679911222189",
                "fee": "-0.000000500682",
                "feeCcy": "BTC",
                "instId": "BTC-USDC",
                "instType": "SPOT",
                "ordId": "560523524184580096",
                "ordType": "market",
                "px": "-1",
                "side": "buy",
                "state": "filled",
                "sz": "20",
                "tag": "",
                "tdMode": "",
                "uTime": "1679911222194"
            }
        ],
        "msg": ""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
algoId | String | 策略订单ID  
instType | String | 产品类型  
instId | String | 产品ID  
algoOrdType | String | 策略订单类型  
`recurring`：定投  
ordId | String | 子订单ID  
cTime | String | 子订单创建时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
uTime | String | 子订单更新时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
tdMode | String | 子订单交易模式  
`cross`：全仓 `cash`：非保证金  
ordType | String | 子订单类型  
`market`：市价单  
`manual_add_order`：手动加仓单  
sz | String | 子订单委托数量  
state | String | 子订单状态  
`canceled`：撤单成功  
`live`：等待成交  
`partially_filled`：部分成交  
`filled`：完全成交  
`cancelling`：撤单中  
side | String | 子订单订单方向  
`buy`：买 `sell`：卖  
px | String | 子订单委托价格  
市价委托时为"-1"  
fee | String | 子订单手续费数量  
feeCcy | String | 子订单手续费币种  
avgPx | String | 子订单平均成交价格  
accFillSz | String | 子订单累计成交数量  
tag | String | 订单标签  
algoClOrdId | String | 用户自定义策略ID  
  
### WS / 定投策略委托订单频道 

支持定投策略订单的定时推送和事件推送

#### 服务地址

/ws/v5/business (需要登录)

> 请求示例
    
    
    {
        "id": "1512",
        "op": "subscribe",
        "args": [{
            "channel": "algo-recurring-buy",
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
            "channel": "algo-recurring-buy",
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
`algo-recurring-buy`  
> instType | String | 是 | 产品类型  
`SPOT`：币币  
`ANY`：全部  
> algoId | String | 否 | 策略ID  
  
> 成功返回示例
    
    
    {
        "id": "1512",
        "event": "subscribe",
        "arg": {
                "channel": "algo-recurring-buy",
                "instType": "SPOT"
        },
        "connId": "a4d3ae55"
    }
    

> 失败返回示例
    
    
    {
        "id": "1512",
        "event": "error",
        "code": "60012",
        "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{ \"channel\" : \"algo-recurring-buy\", \"instType\" : \"FUTURES\"}]}",
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
> algoId | String | 否 | 策略ID  
code | String | 否 | 错误码  
msg | String | 否 | 错误消息  
connId | String | 是 | WebSocket连接ID  
  
> 推送示例
    
    
    {
        "arg": {
            "channel": "algo-recurring-buy",
            "instType": "SPOT",
            "uid": "447*******584"
        },
        "data": [{
            "algoClOrdId": "",
            "algoId": "644497312047435776",
            "algoOrdType": "recurring",
            "amt": "100",
            "cTime": "1699932133373",
            "cycles": "0",
            "instType": "SPOT",
            "investmentAmt": "0",
            "investmentCcy": "USDC",
            "mktCap": "0",
            "nextInvestTime": "1699934415300",
            "pTime": "1699933314691",
            "period": "hourly",
            "pnlRatio": "0",
            "recurringDay": "",
            "recurringHour": "1",
            "recurringList": [{
                "avgPx": "0",
                "ccy": "BTC",
                "profit": "0",
                "px": "36482",
                "ratio": "0.2",
                "minPx": "30000",
                "maxPx": "50000",
                "totalAmt": "0"
            }, {
                "avgPx": "0",
                "ccy": "ETH",
                "profit": "0",
                "px": "2057.54",
                "ratio": "0.8",
                "minPx": "",
                "maxPx": "",
                "totalAmt": "0"
            }],
            "recurringTime": "12",
            "recurringTimeType": "1",
            "recurringTimeMinutes": "",
            "source": ["1"],
            "state": "running",
            "stgyName": "stg1",
            "tag": "",
            "timeZone": "8",
            "totalAnnRate": "0",
            "totalPnl": "0",
            "uTime": "1699932136249",
            "tradeQuoteCcy": "USDT"
        }]
    }
    

#### 推送数据参数

**参数名** | **类型** | **描述**  
---|---|---  
arg | Object | 订阅成功的频道  
> channel | String | 频道名  
> instType | String | 产品类型  
> algoId | String | 策略ID  
> uid | String | 用户ID  
data | Array of objects | 订阅的数据  
> algoId | String | 策略订单ID  
> algoClOrdId | String | 客户自定义订单ID  
> instType | String | 产品类型  
`SPOT`：现货  
> cTime | String | 策略订单创建时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
> uTime | String | 策略订单更新时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
> algoOrdType | String | 策略订单类型  
`recurring`：定投  
> state | String | 订单状态  
`running`：运行中  
`stopping`：终止中  
`stopped`：已停止  
`pause`: 已暂停  
> stgyName | String | 策略自定义名称，不超过40个字符  
> recurringList | Array of objects | 定投信息  
>> ccy | String | 定投币种，如 `BTC`  
>> ratio | String | 定投币种资产占比，如 "0.2"代表占比20%  
>> minPx | String | 价格区间最低价，`""` 代表没有限制  
>> maxPx | String | 价格区间最高价，`""` 代表没有限制  
>> totalAmt | String | 累计购入定投币种的数量  
>> profit | String | 定投收益，单位为`investmentCcy`  
>> avgPx | String | 定投均价，计价单位为`investmentCcy`  
>> px | String | 当前价格，计价单位为`investmentCcy`  
> period | String | 周期类型  
  
`monthly`：月  
`weekly`：周  
`daily`：日  
`hourly`：小时  
> recurringDay | String | 投资日  
当周期类型为`monthly`，则取值范围是 [1,28] 的整数  
当周期类型为`weekly`，则取值范围是 [1,7] 的整数  
> recurringHour | String | 小时级别定投的间隔  
`1`/`4`/`8`/`12`  
如：`1`代表每隔`1`个小时定投  
> recurringTime | String | 投资时间，取值范围是 [0,23] 的整数  
> timeZone | String | 时区（UTC），取值范围是 [-12,14] 的整数  
如 `8`表示UTC+8（东8区），北京时间  
> amt | String | 每期投入数量  
> investmentAmt | String | 累计投入数量  
> investmentCcy | String | 投入数量单位，只能是`USDT`/`USDC`  
> nextInvestTime | String | 下一次定投发生的时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
> totalPnl | String | 总收益  
> totalAnnRate | String | 总年化  
> pnlRatio | String | 收益率  
> mktCap | String | 当前总市值，单位为`USDT`  
> cycles | String | 定投累计轮数  
> tag | String | 订单标签  
> pTime | String | 策略订单的推送时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
> tradeQuoteCcy | String | 用于交易的计价币种。  
> recurringTimeType | String | 定投时间类型  
> recurringTimeMinutes | String | 自定义定投分钟数  
> source | Array | 定投来源  
  
### POST / 编辑定投周期 

#### 限速：20次/2s

#### 限速规则：User ID

#### HTTP请求

`POST /api/v5/tradingBot/recurring/amend-recurring-time`

> 请求示例
    
    
    POST /api/v5/tradingBot/recurring/amend-recurring-time
    body
    {
        "algoId": "2837428373700509696",
        "recurringTimeType": "1",
        "period": "hourly",
        "recurringHour": "8",
        "recurringDay": "1",
        "recurringTime": "11",
        "timeZone": "8"
    }
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
algoId | String | 是 | 策略订单ID  
recurringTimeType | String | 是 | 定投周期类型  
`1`：自定义时间  
`2`：立即触发  
timeZone | String | 是 | 时区（UTC），取值范围是 [-12,14] 的整数  
如 `8` 表示UTC+8（东8区），北京时间  
period | String | 是 | 周期类型  
`monthly`：月  
`weekly`：周  
`daily`：日  
`hourly`：小时  
recurringHour | String | 可选 | 小时级别定投的间隔  
`1`/`4`/`8`/`12`  
如：`1` 代表每隔 `1` 个小时定投  
当 `period` 为 `hourly` 时必填  
recurringDay | String | 可选 | 投资日  
当周期类型为 `monthly`，则取值范围是 [1,28] 的整数  
当周期类型为 `weekly`，则取值范围是 [1,7] 的整数  
当周期类型为 `daily`/`hourly`，该参数可不填  
仅在 `recurringTimeType` 为 `1` 时需要传  
recurringTime | String | 可选 | 投资时间，取值范围是 [0,23] 的整数  
仅在 `recurringTimeType` 为 `1` 时需要传  
  
> 返回结果
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "sCode": "0",
                "sMsg": ""
            }
        ]
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
algoId | String | 策略订单ID  
sCode | String | 事件执行结果的 code，0 代表成功  
sMsg | String | 事件执行失败时的 msg  
  
### POST / 编辑定投金额 

#### 限速：20次/2s

#### 限速规则：User ID

#### HTTP请求

`POST /api/v5/tradingBot/recurring/amend-recurring-amount`

> 请求示例
    
    
    POST /api/v5/tradingBot/recurring/amend-recurring-amount
    body
    {
        "algoId": "2837428373700509696",
        "amount": "20"
    }
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
algoId | String | 是 | 策略订单ID  
amount | String | 是 | 编辑后的定投金额，仅支持创建策略时的投资币种  
  
> 返回结果
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "algoId": "2837428373700509696",
                "sCode": "0",
                "sMsg": ""
            }
        ]
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
algoId | String | 策略订单ID  
sCode | String | 事件执行结果的 code，0 代表成功  
sMsg | String | 事件执行失败时的 msg  
  
### POST / 手动加仓 

#### 限速：20次/2s

#### 限速规则：User ID

#### HTTP请求

`POST /api/v5/tradingBot/recurring/add-investment`

> 请求示例
    
    
    POST /api/v5/tradingBot/recurring/add-investment
    body
    {
        "algoId": "2837428373700509696",
        "amount": "20"
    }
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
algoId | String | 是 | 策略订单ID  
amount | String | 是 | 加仓投入金额，仅支持创建策略时的投资币种  
  
> 返回结果
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "algoId": "2837428373700509696",
                "sCode": "0",
                "sMsg": ""
            }
        ]
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
algoId | String | 策略订单ID  
sCode | String | 事件执行结果的 code，0 代表成功  
sMsg | String | 事件执行失败时的 msg  
  
### POST / 暂停定投策略 

#### 限速：20次/2s

#### 限速规则：User ID

#### HTTP请求

`POST /api/v5/tradingBot/recurring/pause`

> 请求示例
    
    
    POST /api/v5/tradingBot/recurring/pause
    body
    {
        "algoId": "2837428373700509696"
    }
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
algoId | String | 是 | 策略订单ID  
  
> 返回结果
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "algoId": "2837428373700509696",
                "sCode": "0",
                "sMsg": ""
            }
        ]
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
algoId | String | 策略订单ID  
sCode | String | 事件执行结果的 code，0 代表成功  
sMsg | String | 事件执行失败时的 msg  
  
### POST / 重启定投策略 

#### 限速：20次/2s

#### 限速规则：User ID

#### HTTP请求

`POST /api/v5/tradingBot/recurring/restart`

> 请求示例
    
    
    POST /api/v5/tradingBot/recurring/restart
    body
    {
        "algoId": "2837428373700509696"
    }
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
algoId | String | 是 | 策略订单ID  
  
> 返回结果
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "algoId": "2837428373700509696",
                "sCode": "0",
                "sMsg": ""
            }
        ]
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
algoId | String | 策略订单ID  
sCode | String | 事件执行结果的 code，0 代表成功  
sMsg | String | 事件执行失败时的 msg  
  
### POST / 编辑价格区间 

#### 限速：20次/2s

#### 限速规则：User ID

#### HTTP请求

`POST /api/v5/tradingBot/recurring/amend-price-range`

> 请求示例
    
    
    POST /api/v5/tradingBot/recurring/amend-price-range
    body
    {
        "algoId": "2837428373700509696",
        "recurringList": [
            {
                "ccy": "BTC",
                "minPx": "80000",
                "maxPx": "120000"
            }
        ]
    }
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
algoId | String | 是 | 策略订单ID  
recurringList | Array | 是 | 价格区间设置，币种必须在策略定投币种范围内  
>ccy | String | 是 | 定投币种  
>minPx | String | 是 | 价格区间最低价，`""` 代表没有限制  
>maxPx | String | 是 | 价格区间最高价，`""` 代表没有限制  
  
> 返回结果
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "algoId": "2837428373700509696",
                "sCode": "0",
                "sMsg": ""
            }
        ]
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
algoId | String | 策略订单ID  
sCode | String | 事件执行结果的 code，0 代表成功  
sMsg | String | 事件执行失败时的 msg