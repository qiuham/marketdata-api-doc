---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#order-book-trading-market-data
anchor_id: order-book-trading-market-data
api_type: API
updated_at: 2026-07-11 19:13:12.710066
---

# Market Data

The API endpoints of `Market Data` do not require authentication.  
  
There are multiple services for market data, and each service has an independent cache. A random service will be requested for every request. So for two requests, it’s expected that the data obtained in the second request is earlier than the first request.

For event contracts, market data module will only return data of the YES side. Users can derive NO side data on their own.

### GET / Tickers

Retrieve the latest price snapshot, best bid/ask price, and trading volume in the last 24 hours. Best ask price may be lower than the best bid price during the pre-open period.

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: IP

#### HTTP Request

`GET /api/v5/market/tickers`

> Request Example
    
    
    GET /api/v5/market/tickers?instType=SWAP
    
    
    
    
    import okx.MarketData as MarketData
    
    flag = "0"  # Production trading:0 , demo trading:1
    
    marketDataAPI =  MarketData.MarketAPI(flag=flag)
    
    # Retrieve the latest price snapshot, best bid/ask price, and trading volume in the last 24 hours
    result = marketDataAPI.get_tickers(
        instType="SWAP"
    )
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
instType | String | Yes | Instrument type  
`SPOT`  
`SWAP`  
`FUTURES`  
`OPTION`  
`EVENTS`  
instFamily | String | No | Instrument family  
Applicable to `FUTURES`/`SWAP`/`OPTION`  
  
> Response Example
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
         {
            "instType":"SWAP",
            "instId":"LTC-USD-SWAP",
            "last":"9999.99",
            "lastSz":"1",
            "askPx":"9999.99",
            "askSz":"11",
            "bidPx":"8888.88",
            "bidSz":"5",
            "open24h":"9000",
            "high24h":"10000",
            "low24h":"8888.88",
            "volCcy24h":"2222",
            "vol24h":"2222",
            "sodUtc0":"0.1",
            "sodUtc8":"0.1",
            "ts":"1597026383085"
         },
         {
            "instType":"SWAP",
            "instId":"BTC-USD-SWAP",
            "last":"9999.99",
            "lastSz":"1",
            "askPx":"9999.99",
            "askSz":"11",
            "bidPx":"8888.88",
            "bidSz":"5",
            "open24h":"9000",
            "high24h":"10000",
            "low24h":"8888.88",
            "volCcy24h":"2222",
            "vol24h":"2222",
            "sodUtc0":"0.1",
            "sodUtc8":"0.1",
            "ts":"1597026383085"
        }
      ]
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
instType | String | Instrument type  
instId | String | Instrument ID  
last | String | Last traded price  
lastSz | String | Last traded size. 0 represents there is no trading volume  
askPx | String | Best ask price  
askSz | String | Best ask size  
bidPx | String | Best bid price  
bidSz | String | Best bid size  
open24h | String | Open price in the past 24 hours  
high24h | String | Highest price in the past 24 hours  
low24h | String | Lowest price in the past 24 hours  
volCcy24h | String | 24h trading volume, with a unit of `currency`.   
If it is a `derivatives` contract, the value is the number of base currency. e.g. the unit is BTC for BTC-USD-SWAP and BTC-USDT-SWAP   
If it is `SPOT`/`MARGIN`, the value is the quantity in quote currency.  
vol24h | String | 24h trading volume, with a unit of `contract`.   
If it is a `derivatives` contract, the value is the number of contracts.   
If it is `SPOT`/`MARGIN`, the value is the quantity in base currency.  
sodUtc0 | String | Open price in the UTC 0  
sodUtc8 | String | Open price in the UTC 8  
ts | String | Ticker data generation time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
  
### GET / Ticker

Retrieve the latest price snapshot, best bid/ask price, and trading volume in the last 24 hours. Best ask price may be lower than the best bid price during the pre-open period.

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: IP

#### HTTP Request

`GET /api/v5/market/ticker`

> Request Example
    
    
    GET /api/v5/market/ticker?instId=BTC-USD-SWAP
    
    
    
    
    import okx.MarketData as MarketData
    
    flag = "0"  # Production trading:0 , demo trading:1
    
    marketDataAPI =  MarketData.MarketAPI(flag=flag)
    
    # Retrieve the latest price snapshot, best bid/ask price, and trading volume in the last 24 hours
    result = marketDataAPI.get_ticker(
        instId="BTC-USD-SWAP"
    )
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
instId | String | Yes | Instrument ID, e.g. `BTC-USD-SWAP`  
  
> Response Example
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
         {
            "instType":"SWAP",
            "instId":"BTC-USD-SWAP",
            "last":"9999.99",
            "lastSz":"0.1",
            "askPx":"9999.99",
            "askSz":"11",
            "bidPx":"8888.88",
            "bidSz":"5",
            "open24h":"9000",
            "high24h":"10000",
            "low24h":"8888.88",
            "volCcy24h":"2222",
            "vol24h":"2222",
            "sodUtc0":"2222",
            "sodUtc8":"2222",
            "ts":"1597026383085"
        }
      ]
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
instType | String | Instrument type  
instId | String | Instrument ID  
last | String | Last traded price  
lastSz | String | Last traded size. 0 represents there is no trading volume  
askPx | String | Best ask price  
askSz | String | Best ask size  
bidPx | String | Best bid price  
bidSz | String | Best bid size  
open24h | String | Open price in the past 24 hours  
high24h | String | Highest price in the past 24 hours  
low24h | String | Lowest price in the past 24 hours  
volCcy24h | String | 24h trading volume, with a unit of `currency`.   
If it is a `derivatives` contract, the value is the number of base currency.   
If it is `SPOT`/`MARGIN`, the value is the quantity in quote currency.  
vol24h | String | 24h trading volume, with a unit of `contract`.   
If it is a `derivatives` contract, the value is the number of contracts.   
If it is `SPOT`/`MARGIN`, the value is the quantity in base currency.  
sodUtc0 | String | Open price in the UTC 0  
sodUtc8 | String | Open price in the UTC 8  
ts | String | Ticker data generation time, Unix timestamp format in milliseconds, e.g. `1597026383085`.  
  
### GET / Order book

Retrieve order book of the instrument. The data will be updated once every 50 milliseconds. Best ask price may be lower than the best bid price during the pre-open period.  
This endpoint does not return data immediately. Instead, it returns the latest data once the server-side cache has been updated.

#### Rate Limit: 40 requests per 2 seconds

#### Rate limit rule: IP

#### HTTP Request

`GET /api/v5/market/books`

> Request Example
    
    
    GET /api/v5/market/books?instId=BTC-USDT
    
    
    
    
    import okx.MarketData as MarketData
    
    flag = "0"  # Production trading:0 , demo trading:1
    
    marketDataAPI =  MarketData.MarketAPI(flag=flag)
    
    # Retrieve order book of the instrument
    result = marketDataAPI.get_orderbook(
        instId="BTC-USDT"
    )
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
instId | String | Yes | Instrument ID, e.g. `BTC-USDT`  
sz | String | No | Order book depth per side. Maximum 400, e.g. 400 bids + 400 asks   
Default returns to `1` depth data  
  
> Response Example
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "asks": [
                    [
                        "41006.8",
                        "0.60038921",
                        "0",
                        "1"
                    ]
                ],
                "bids": [
                    [
                        "41006.3",
                        "0.30178218",
                        "0",
                        "2"
                    ]
                ],
                "ts": "1629966436396",
                "seqId": 3235851742
            }
        ]
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
asks | Array of Arrays | Order book on sell side  
bids | Array of Arrays | Order book on buy side  
ts | String | Order book generation time  
seqId | Integer | Sequence ID of the current message  
An example of the array of asks and bids values: ["411.8", "10", "0", "4"]  
\- "411.8" is the depth price  
\- "10" is the quantity at the price (number of contracts for derivatives, quantity in base currency for Spot and Spot Margin)  
\- "0" is part of a deprecated feature and it is always "0"  
\- "4" is the number of orders at the price.  
The order book data will be updated around once a second during the call auction. 

### GET / Full order book

Retrieve order book of the instrument. The data will be updated once a second. Best ask price may be lower than the best bid price during the pre-open period.  
This endpoint does not return data immediately. Instead, it returns the latest data once the server-side cache has been updated.

#### Rate Limit: 10 requests per 2 seconds

#### Rate limit rule: IP

#### HTTP Request

`GET /api/v5/market/books-full`

> Request Example
    
    
    GET /api/v5/market/books-full?instId=BTC-USDT&sz=1
    
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
instId | String | Yes | Instrument ID, e.g. `BTC-USDT`  
sz | String | No | Order book depth per side. Maximum 5000, e.g. 5000 bids + 5000 asks   
Default returns to `1` depth data.  
  
> Response Example
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "asks": [
                    [
                        "41006.8",
                        "0.60038921",
                        "1"
                    ]
                ],
                "bids": [
                    [
                        "41006.3",
                        "0.30178218",
                        "2"
                    ]
                ],
                "ts": "1629966436396"
            }
        ]
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
asks | Array of Arrays | Order book on sell side  
bids | Array of Arrays | Order book on buy side  
ts | String | Order book generation time  
An example of the array of asks and bids values: ["411.8", "10", "4"]  
\- "411.8" is the depth price  
\- "10" is the quantity at the price (number of contracts for derivatives, quantity in base currency for Spot and Spot Margin)  
\- "4" is the number of orders at the price.  
The order book data will be updated around once a second during the call auction. 

### GET / Candlesticks

Retrieve the candlestick charts. This endpoint can retrieve the latest 1,440 data entries. Charts are returned in groups based on the requested bar. 

#### Rate Limit: 40 requests per 2 seconds

#### Rate limit rule: IP

#### HTTP Request

`GET /api/v5/market/candles`

> Request Example
    
    
    GET /api/v5/market/candles?instId=BTC-USDT
    
    
    
    import okx.MarketData as MarketData
    
    flag = "0"  # Production trading:0 , demo trading:1
    
    marketDataAPI =  MarketData.MarketAPI(flag=flag)
    
    # Retrieve the candlestick charts
    result = marketDataAPI.get_candlesticks(
        instId="BTC-USDT"
    )
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
instId | String | Yes | Instrument ID, e.g. `BTC-USDT`  
bar | String | No | Bar size, the default is `1m`  
e.g. [1m/3m/5m/15m/30m/1H/2H/4H]   
UTC+8 opening price k-line: [6H/12H/1D/2D/3D/1W/1M/3M]  
UTC+0 opening price k-line: [6Hutc/12Hutc/1Dutc/2Dutc/3Dutc/1Wutc/1Mutc/3Mutc]  
after | String | No | Pagination of data to return records earlier than the requested `ts`  
before | String | No | Pagination of data to return records newer than the requested `ts`. The latest data will be returned when using `before` individually  
limit | String | No | Number of results per request. The maximum is `300`. The default is `100`.  
adjust | String | No | Price adjustment type for equity perpetual contracts.  
`forward`: Forward adjustment.  
If this field is omitted, unadjusted data is returned by default.  
Only applicable to equity perpetual contracts.  
  
> Response Example
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
         [
            "1597026383085",
            "3.721",
            "3.743",
            "3.677",
            "3.708",
            "8422410",
            "22698348.04828491",
            "12698348.04828491",
            "0"
        ],
        [
            "1597026383085",
            "3.731",
            "3.799",
            "3.494",
            "3.72",
            "24912403",
            "67632347.24399722",
            "37632347.24399722",
            "1"
        ]
        ]
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
ts | String | Opening time of the candlestick, Unix timestamp format in milliseconds, e.g. `1597026383085`  
o | String | Open price  
h | String | highest price  
l | String | Lowest price  
c | String | Close price  
vol | String | Trading volume, with a unit of `contract`.   
If it is a `derivatives` contract, the value is the number of contracts.   
If it is `SPOT`/`MARGIN`, the value is the quantity in base currency.  
volCcy | String | Trading volume, with a unit of `currency`.   
If it is a `derivatives` contract, the value is the number of base currency.   
If it is `SPOT`/`MARGIN`, the value is the quantity in quote currency.  
volCcyQuote | String | Trading volume, the value is the quantity in quote currency   
e.g. The unit is USDT for BTC-USDT and BTC-USDT-SWAP;  
The unit is USD for BTC-USD-SWAP  
confirm | String | The state of candlesticks.  
`0`: K line is uncompleted  
`1`: K line is completed  
  
The first candlestick data may be incomplete, and should not be polled repeatedly. 

The data returned will be arranged in an array like this: [ts,o,h,l,c,vol,volCcy,volCcyQuote,confirm]. 

For the current cycle of k-line data, when there is no transaction, the opening high and closing low default take the closing price of the previous cycle.  When `adjust=forward`, the historical OHLC prices are multiplied by the adjustment factor for the relevant period. For stock splits, `vol` and `volCcy` are also adjusted proportionally. `volCcyQuote` is not adjusted. This parameter is only effective for equity perpetual contracts. 

### GET / Candlesticks history

Retrieve history candlestick charts from recent years(It is last 3 months supported for 1s candlestick).

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: IP

#### HTTP Request

`GET /api/v5/market/history-candles`

> Request Example
    
    
    GET /api/v5/market/history-candles?instId=BTC-USDT
    
    
    
    import okx.MarketData as MarketData
    
    flag = "0"  # Production trading:0 , demo trading:1
    
    marketDataAPI =  MarketData.MarketAPI(flag=flag)
    
    # Retrieve history candlestick charts from recent years
    result = marketDataAPI.get_history_candlesticks(
        instId="BTC-USDT"
    )
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
instId | String | Yes | Instrument ID, e.g. `BTC-USDT`  
after | String | No | Pagination of data to return records earlier than the requested `ts`  
before | String | No | Pagination of data to return records newer than the requested `ts`. The latest data will be returned when using `before` individually  
bar | String | No | Bar size, the default is `1m`  
e.g. [1s/1m/3m/5m/15m/30m/1H/2H/4H]   
UTC+8 opening price k-line: [6H/12H/1D/2D/3D/1W/1M/3M]  
UTC+0 opening price k-line: [6Hutc/12Hutc/1Dutc/2Dutc/3Dutc/1Wutc/1Mutc/3Mutc]  
limit | String | No | Number of results per request. The maximum is `300`. The default is `100`.  
adjust | String | No | Price adjustment type for equity perpetual contracts.  
`forward`: Forward adjustment.  
If this field is omitted, unadjusted data is returned by default.  
Only applicable to equity perpetual contracts.  
  
> Response Example
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
         [
            "1597026383085",
            "3.721",
            "3.743",
            "3.677",
            "3.708",
            "8422410",
            "22698348.04828491",
            "12698348.04828491",
            "1"
        ],
        [
            "1597026383085",
            "3.731",
            "3.799",
            "3.494",
            "3.72",
            "24912403",
            "67632347.24399722",
            "37632347.24399722",
            "1"
        ]
        ]
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
ts | String | Opening time of the candlestick, Unix timestamp format in milliseconds, e.g. `1597026383085`  
o | String | Open price  
h | String | Highest price  
l | String | Lowest price  
c | String | Close price  
vol | String | Trading volume, with a unit of `contract`.   
If it is a `derivatives` contract, the value is the number of contracts.   
If it is `SPOT`/`MARGIN`, the value is the quantity in base currency.  
volCcy | String | Trading volume, with a unit of `currency`.   
If it is a `derivatives` contract, the value is the number of base currency.   
If it is `SPOT`/`MARGIN`, the value is the quantity in quote currency.  
volCcyQuote | String | Trading volume, the value is the quantity in quote currency  
e.g. The unit is USDT for BTC-USDT and BTC-USDT-SWAP;  
The unit is USD for BTC-USD-SWAP  
confirm | String | The state of candlesticks  
`0`: K line is uncompleted  
`1`: K line is completed  
  
The data returned will be arranged in an array like this: [ts,o,h,l,c,vol,volCcy,volCcyQuote,confirm] 

1s candle is not supported by OPTION, but it is supported by other business lines (SPOT, MARGIN, FUTURES and SWAP)  When `adjust=forward`, the historical OHLC prices are multiplied by the adjustment factor for the relevant period. For stock splits, `vol` and `volCcy` are also adjusted proportionally. `volCcyQuote` is not adjusted. This parameter is only effective for equity perpetual contracts. 

### GET / Trades

Retrieve the recent transactions of an instrument.

#### Rate Limit: 100 requests per 2 seconds

#### Rate limit rule: IP

#### HTTP Request

`GET /api/v5/market/trades`

> Request Example
    
    
    GET /api/v5/market/trades?instId=BTC-USDT
    
    
    
    import okx.MarketData as MarketData
    
    flag = "0"  # Production trading:0 , demo trading:1
    
    marketDataAPI =  MarketData.MarketAPI(flag=flag)
    
    # Retrieve the recent transactions of an instrument
    result = marketDataAPI.get_trades(
        instId="BTC-USDT"
    )
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
instId | String | Yes | Instrument ID, e.g. `BTC-USDT`  
limit | String | No | Number of results per request. The maximum is `500`; The default is `100`  
  
> Response Example
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "instId": "BTC-USDT",
                "side": "sell",
                "sz": "0.00001",
                "source": "0",
                "px": "29963.2",
                "tradeId": "242720720",
                "ts": "1654161646974"
            },
            {
                "instId": "BTC-USDT",
                "side": "sell",
                "sz": "0.00001",
                "source": "0",
                "px": "29964.1",
                "tradeId": "242720719",
                "ts": "1654161641568"
            }
        ]
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
instId | String | Instrument ID  
tradeId | String | Trade ID  
px | String | Trade price  
sz | String | Trade quantity   
For spot trading, the unit is base currency  
For `FUTURES`/`SWAP`/`OPTION`, the unit is contract.  
side | String | Trade side of taker   
`buy`   
`sell`  
source | String | Order source  
`0`: normal order  
`1`: Enhanced Liquidity Program order  
ts | String | Trade time, Unix timestamp format in milliseconds, e.g. `1597026383085`.  
Up to 500 most recent historical public transaction data can be retrieved. 

### GET / Trades history

Retrieve the recent transactions of an instrument from the last 3 months with pagination.

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: IP

#### HTTP Request

`GET /api/v5/market/history-trades`

> Request Example
    
    
    GET /api/v5/market/history-trades?instId=BTC-USDT
    
    
    
    import okx.MarketData as MarketData
    
    flag = "0"  # Production trading:0 , demo trading:1
    
    marketDataAPI =  MarketData.MarketAPI(flag=flag)
    
    # Retrieve the recent transactions of an instrument from the last 3 months with pagination
    result = marketDataAPI.get_history_trades(
        instId="BTC-USD-SWAP"
    )
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
instId | String | Yes | Instrument ID, e.g. `BTC-USDT`  
type | String | No | Pagination Type   
`1`: tradeId `2`: timestamp  
The default is `1`  
after | String | No | Pagination of data to return records earlier than the requested tradeId or ts.  
before | String | No | Pagination of data to return records newer than the requested tradeId.   
Do not support timestamp for pagination. The latest data will be returned when using `before` individually  
limit | String | No | Number of results per request. The maximum and default both are `100`  
  
> Response Example
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "instId": "BTC-USDT",
                "side": "sell",
                "sz": "0.00001",
                "source": "0",
                "px": "29963.2",
                "tradeId": "242720720",
                "ts": "1654161646974"
            },
            {
                "instId": "BTC-USDT",
                "side": "sell",
                "sz": "0.00001",
                "source": "0",
                "px": "29964.1",
                "tradeId": "242720719",
                "ts": "1654161641568"
            }
        ]
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
instId | String | Instrument ID  
tradeId | String | Trade ID  
px | String | Trade price  
sz | String | Trade quantity   
For spot trading, the unit is base currency  
For `FUTURES`/`SWAP`/`OPTION`, the unit is contract.  
side | String | Trade side of taker   
`buy`   
`sell`  
source | String | Order source  
`0`: normal order  
`1`: Enhanced Liquidity Program order  
ts | String | Trade time, Unix timestamp format in milliseconds, e.g. `1597026383085`.  
  
### GET / Option trades by instrument family

Retrieve the recent transactions of an instrument under same instFamily. The maximum is 100.

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: IP

#### HTTP Request

`GET /api/v5/market/option/instrument-family-trades`

> Request Example
    
    
    GET /api/v5/market/option/instrument-family-trades?instFamily=BTC-USD
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
instFamily | String | Yes | Instrument family, e.g. BTC-USD  
Applicable to `OPTION`  
  
> Response Example
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "vol24h": "103381",
                "tradeInfo": [
                    {
                        "instId": "BTC-USD-221111-17750-C",
                        "side": "sell",
                        "sz": "1",
                        "px": "0.0075",
                        "tradeId": "20",
                        "ts": "1668090715058"
                    },
                    {
                        "instId": "BTC-USD-221111-17750-C",
                        "side": "sell",
                        "sz": "91",
                        "px": "0.01",
                        "tradeId": "19",
                        "ts": "1668090421062"
                    }
                ],
                "optType": "C"
            },
            {
                "vol24h": "144499",
                "tradeInfo": [
                    {
                        "instId": "BTC-USD-230127-10000-P",
                        "side": "sell",
                        "sz": "82",
                        "px": "0.019",
                        "tradeId": "23",
                        "ts": "1668090967057"
                    },
                    {
                        "instId": "BTC-USD-221111-16250-P",
                        "side": "sell",
                        "sz": "102",
                        "px": "0.0045",
                        "tradeId": "24",
                        "ts": "1668090885050"
                    }
                ],
                "optType": "P"
            }
        ]
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
vol24h | String | 24h trading volume, with a unit of contract.  
optType | String | Option type, C: Call P: Put  
tradeInfo | Array of objects | The list trade data  
> instId | String | The Instrument ID  
> tradeId | String | Trade ID  
> px | String | Trade price  
> sz | String | Trade quantity. The unit is contract.  
> side | String | Trade side  
`buy`  
`sell`  
> ts | String | Trade time, Unix timestamp format in milliseconds, e.g. 1597026383085.  
  
### GET / Option trades

The maximum is 100.

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: IP

#### HTTP Request

`GET /api/v5/public/option-trades`

> Request Example
    
    
    GET /api/v5/public/option-trades?instFamily=BTC-USD
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
instId | String | Conditional | Instrument ID, e.g. BTC-USD-221230-4000-C, Either `instId` or `instFamily` is required. If both are passed, `instId` will be used.  
instFamily | String | Conditional | Instrument family, e.g. BTC-USD  
optType | String | No | Option type, `C`: Call `P`: put  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "fillVol": "0.24415013671875",
                "fwdPx": "16676.907614127158",
                "idxPx": "16667",
                "instFamily": "BTC-USD",
                "instId": "BTC-USD-221230-16600-P",
                "markPx": "0.006308943261227884",
                "optType": "P",
                "px": "0.005",
                "side": "sell",
                "sz": "30",
                "tradeId": "65",
                "ts": "1672225112048"
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
instId | String | Instrument ID  
instFamily | String | Instrument family  
tradeId | String | Trade ID  
px | String | Trade price  
sz | String | Trade quantity. The unit is contract.  
side | String | Trade side   
`buy`   
`sell`  
optType | String | Option type, C: Call P: Put  
fillVol | String | Implied volatility while trading (Correspond to trade price)  
fwdPx | String | Forward price while trading  
idxPx | String | Index price while trading  
markPx | String | Mark price while trading  
ts | String | Trade time, Unix timestamp format in milliseconds, e.g. `1597026383085`.  
  
### GET / 24H total volume

The 24-hour trading volume is calculated on a rolling basis.

#### Rate Limit: 2 requests per 2 seconds

#### Rate limit rule: IP

#### HTTP Request

`GET /api/v5/market/platform-24-volume`

> Request Example
    
    
    GET /api/v5/market/platform-24-volume
    
    
    
    
    import okx.MarketData as MarketData
    
    flag = "0"  # Production trading:0 , demo trading:1
    
    marketDataAPI =  MarketData.MarketAPI(flag=flag)
    
    # Retrieve 24 total volume
    result = marketDataAPI.get_volume()
    print(result)
    

> Response Example
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
         {
             "volCny": "230900886396766",
             "volUsd": "34462818865189",
             "ts": "1657856040389"
         }
      ]
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
volUsd | String | 24-hour total trading volume from the order book trading in "USD"  
volCny | String | 24-hour total trading volume from the order book trading in "CNY"  
ts | String | Data return time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
  
### GET / Call auction details

Retrieve call auction details.

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: IP

#### HTTP Request

`GET /api/v5/market/call-auction-details`

> Request Example
    
    
    GET /api/v5/market/call-auction-details?instId=ONDO-USDC
    
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
instId | String | Yes | Instrument ID, e.g. `BTC-USDT`  
  
> Response Example
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "instId": "ONDO-USDC",
                "unmatchedSz": "9988764",
                "eqPx": "0.6",
                "matchedSz": "44978",
                "state": "continuous_trading",
                "auctionEndTime": "1726542000000",
                "ts": "1726542000007"
            }
        ]
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
instId | String | Instrument ID  
eqPx | String | Equilibrium price  
matchedSz | String | Matched size for both buy and sell  
The unit is in base currency  
unmatchedSz | String | Unmatched size  
auctionEndTime | String | Call auction end time. Unix timestamp in milliseconds.  
state | String | Trading state of the symbol  
`call_auction`  
`continuous_trading`  
ts | String | Data generation time. Unix timestamp in millieseconds.  
During call auction, users can get the updates of equilibrium price, matched size, unmatched size, and auction end time. The data will be updated around once a second. The endpoint returns the actual open price, matched size, and unmatched size when the call auction ends.   
For symbols that never go through call auction, the endpoint will also return results but with state always as `continuous_trading` and other fields as 0 or empty. 

### WS / Tickers channel

Retrieve the last traded price, bid price, ask price and 24-hour trading volume of instruments. Best ask price may be lower than the best bid price during the pre-open period.   
The fastest rate is 1 update/100ms. There will be no update if the event is not triggered. The events which can trigger update: trade, the change on best ask/bid.

#### URL Path

/ws/v5/public

> Request Example
    
    
    {
      "id": "1512",
      "op": "subscribe",
      "args": [
        {
          "channel": "tickers",
          "instId": "BTC-USDT"
        }
      ]
    }
    
    
    
    import asyncio
    
    from okx.websocket.WsPublicAsync import WsPublicAsync
    
    
    def callbackFunc(message):
        print(message)
    
    
    async def main():
        ws = WsPublicAsync(url="wss://wspap.okx.com:8443/ws/v5/public")
        await ws.start()
        args = [{
            "channel": "tickers",
            "instId": "BTC-USDT"
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
`tickers`  
> instId | String | Yes | Instrument ID  
  
> Successful Response Example
    
    
    {
      "id": "1512",
      "event": "subscribe",
      "arg": {
        "channel": "tickers",
        "instId": "BTC-USDT"
      },
      "connId": "a4d3ae55"
    }
    

> Failure Response Example
    
    
    {
      "id": "1512",
      "event": "error",
      "code": "60012",
      "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{ \"channel\" : \"tickers\", \"instId\" : \"LTC-USD-200327\"}]}",
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
> instId | String | Yes | Instrument ID  
code | String | No | Error code  
msg | String | No | Error message  
connId | String | Yes | WebSocket connection ID  
  
> Push Data Example
    
    
    {
      "arg": {
        "channel": "tickers",
        "instId": "BTC-USDT"
      },
      "data": [
        {
          "instType": "SPOT",
          "instId": "BTC-USDT",
          "last": "9999.99",
          "lastSz": "0.1",
          "askPx": "9999.99",
          "askSz": "11",
          "bidPx": "8888.88",
          "bidSz": "5",
          "open24h": "9000",
          "high24h": "10000",
          "low24h": "8888.88",
          "volCcy24h": "2222",
          "vol24h": "2222",
          "sodUtc0": "2222",
          "sodUtc8": "2222",
          "ts": "1597026383085"
        }
      ]
    }
    

#### Push data parameters

**Parameter** | **Type** | **Description**  
---|---|---  
arg | Object | Successfully subscribed channel  
> channel | String | Channel name  
> instId | String | Instrument ID  
data | Array of objects | Subscribed data  
> instType | String | Instrument type  
> instId | String | Instrument ID  
> last | String | Last traded price  
> lastSz | String | Last traded size. 0 represents there is no trading volume  
> askPx | String | Best ask price  
> askSz | String | Best ask size  
> bidPx | String | Best bid price  
> bidSz | String | Best bid size  
> open24h | String | Open price in the past 24 hours  
> high24h | String | Highest price in the past 24 hours  
> low24h | String | Lowest price in the past 24 hours  
> volCcy24h | String | 24h trading volume, with a unit of `currency`.   
If it is a `derivatives` contract, the value is the number of base currency.   
If it is `SPOT`/`MARGIN`, the value is the quantity in quote currency.  
> vol24h | String | 24h trading volume, with a unit of `contract`.   
If it is a `derivatives` contract, the value is the number of contracts.   
If it is `SPOT`/`MARGIN`, the value is the quantity in base currency.  
> sodUtc0 | String | Open price in the UTC 0  
> sodUtc8 | String | Open price in the UTC 8  
> ts | String | Ticker data generation time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
  
### WS / Candlesticks channel

Retrieve the candlesticks data of an instrument. the push frequency is the fastest interval 1 second push the data.

#### URL Path

/ws/v5/business

> Request Example
    
    
    {
      "id": "1512",
      "op": "subscribe",
      "args": [
        {
          "channel": "candle1D",
          "instId": "BTC-USDT"
        }
      ]
    }
    
    
    
    import asyncio
    
    from okx.websocket.WsPublicAsync import WsPublicAsync
    
    
    def callbackFunc(message):
        print(message)
    
    
    async def main():
        ws = WsPublicAsync(url="wss://wspap.okx.com:8443/ws/v5/business")
        await ws.start()
        args = [
            {
              "channel": "candle1D",
              "instId": "BTC-USDT"
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
`candle3M`  
`candle1M`  
`candle1W`   
`candle1D`  
`candle2D`  
`candle3D`  
`candle5D`  
`candle12H`  
`candle6H`  
`candle4H`  
`candle2H`  
`candle1H`  
`candle30m`  
`candle15m`  
`candle5m`  
`candle3m`  
`candle1m`  
`candle1s`  
`candle3Mutc`  
`candle1Mutc`  
`candle1Wutc`  
`candle1Dutc`  
`candle2Dutc`  
`candle3Dutc`  
`candle5Dutc`  
`candle12Hutc`  
`candle6Hutc`  
> instId | String | Yes | Instrument ID  
  
> Successful Response Example
    
    
    {
      "id": "1512",
      "event": "subscribe",
      "arg": {
        "channel": "candle1D",
        "instId": "BTC-USDT"
      },
      "connId": "a4d3ae55"
    }
    

> Failure Response Example
    
    
    {
      "id": "1512",
      "event": "error",
      "code": "60012",
      "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{ \"channel\" : \"candle1D\", \"instId\" : \"BTC-USD-191227\"}]}",
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
> channel | String | yes | channel name  
> instId | String | Yes | Instrument ID  
code | String | No | Error code  
msg | String | No | Error message  
connId | String | Yes | WebSocket connection ID  
  
> Push Data Example
    
    
    {
      "arg": {
        "channel": "candle1D",
        "instId": "BTC-USDT"
      },
      "data": [
        [
          "1597026383085",
          "8533.02",
          "8553.74",
          "8527.17",
          "8548.26",
          "45247",
          "529.5858061",
          "5529.5858061",
          "0"
        ]
      ]
    }
    

#### Push data parameters

**Parameter** | **Type** | **Description**  
---|---|---  
arg | Object | Successfully subscribed channel  
> channel | String | Channel name  
> instId | String | Instrument ID  
data | Array of Arrays | Subscribed data  
> ts | String | Opening time of the candlestick, Unix timestamp format in milliseconds, e.g. `1597026383085`  
> o | String | Open price  
> h | String | highest price  
> l | String | Lowest price  
> c | String | Close price  
> vol | String | Trading volume, with a unit of `contract`.   
If it is a `derivatives` contract, the value is the number of contracts.   
If it is `SPOT`/`MARGIN`, the value is the quantity in base currency.  
> volCcy | String | Trading volume, with a unit of `currency`.   
If it is a `derivatives` contract, the value is the number of base currency.   
If it is `SPOT`/`MARGIN`, the value is the quantity in quote currency.  
> volCcyQuote | String | Trading volume, the value is the quantity in quote currency   
e.g. The unit is `USDT` for `BTC-USDT` and `BTC-USDT-SWAP`  
The unit is `USD` for `BTC-USD-SWAP`  
> confirm | String | The state of candlesticks  
`0`: K line is uncompleted  
`1`: K line is completed  
  
### WS / Trades channel

Retrieve the recent trades data. Data will be pushed whenever there is a trade. Every update may aggregate multiple trades.   
  

The message is sent only once per taker order, filled price, source. The count field is used to represent the number of aggregated matches.

#### URL Path

/ws/v5/public

> Request Example
    
    
    {
      "id": "1512",
      "op": "subscribe",
      "args": [
        {
          "channel": "trades",
          "instId": "BTC-USDT"
        }
      ]
    }
    
    
    
    import asyncio
    
    from okx.websocket.WsPublicAsync import WsPublicAsync
    
    
    def callbackFunc(message):
        print(message)
    
    
    async def main():
        ws = WsPublicAsync(url="wss://wspap.okx.com:8443/ws/v5/public")
        await ws.start()
        args = [
            {
              "channel": "trades",
              "instId": "BTC-USDT"
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
`trades`  
> instId | String | Yes | Instrument ID  
  
> Successful Response Example
    
    
    {
      "id": "1512",
      "event": "subscribe",
      "arg": {
          "channel": "trades",
          "instId": "BTC-USDT"
      },
      "connId": "a4d3ae55"
    }
    

> Failure Response Example
    
    
    {
      "id": "1512",
      "event": "error",
      "code": "60012",
      "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{ \"channel\" : \"trades\", \"instId\" : \"BTC-USD-191227\"}]}",
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
> instId | String | Yes | Instrument ID  
code | String | No | Error code  
msg | String | No | Error message  
connId | String | Yes | WebSocket connection ID  
  
> Push Data Example
    
    
    {
      "arg": {
        "channel": "trades",
        "instId": "BTC-USDT"
      },
      "data": [
        {
          "instId": "BTC-USDT",
          "tradeId": "130639474",
          "px": "42219.9",
          "sz": "0.12060306",
          "side": "buy",
          "ts": "1630048897897",
          "count": "3",
          "source": "0",
          "seqId": 1234
        }
      ]
    }
    

#### Push data parameters

**Parameter** | **Type** | **Description**  
---|---|---  
arg | Object | Successfully subscribed channel  
> channel | String | Channel name  
> instId | String | Instrument ID  
data | Array of objects | Subscribed data  
> instId | String | Instrument ID, e.g. `BTC-USDT`  
> tradeId | String | The last trade ID in the trades aggregation  
> px | String | Trade price  
> sz | String | Trade quantity   
For spot trading, the unit is base currency  
For `FUTURES`/`SWAP`/`OPTION`, the unit is contract.  
> side | String | Trade side of taker  
`buy`  
`sell`  
> ts | String | Filled time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
> count | String | The count of trades aggregated  
> source | String | Order source  
`0`: normal orders  
`1`: Enhanced Liquidity Program order  
> seqId | Integer | Sequence ID of the current message.  
Aggregation function description:  
1\. The system will send only one message per taker order, filled price, source. The `count` field will be used to represent the number of aggregated matches.  
2\. The `tradeId` field in the message becomes the last trade ID in the aggregation.  
3\. When the `count` = 1, it means the taker order matches only one maker order with the specific price.  
4\. When the `count` > 1, it means the taker order matches multiple maker orders with the same price. For example, if `tradeId` = 123 and `count` = 3, it means the message aggregates the trades of `tradeId` = 123, 122, and 121. Maker side has filled multiple orders.  
5\. Users can use this information to compare with data from the `trades-all` channel.  
6\. Order book and the aggregated trades data are still published sequentially.  
The seqId may be the same for different trade updates that occur at the same time. 

### WS / All trades channel

Retrieve the recent trades data. Data will be pushed whenever there is a trade. Every update contain only one trade. 

#### URL Path

/ws/v5/business

> Request Example
    
    
    {
      "id": "1512",
      "op": "subscribe",
      "args": [
        {
          "channel": "trades-all",
          "instId": "BTC-USDT"
        }
      ]
    }
    
    
    
    import asyncio
    
    from okx.websocket.WsPublicAsync import WsPublicAsync
    
    
    def callbackFunc(message):
        print(message)
    
    
    async def main():
        ws = WsPublicAsync(url="wss://wspap.okx.com:8443/ws/v5/business")
        await ws.start()
        args = [
            {
              "channel": "trades-all",
              "instId": "BTC-USDT"
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
`trades-all`  
> instId | String | Yes | Instrument ID  
  
> Successful Response Example
    
    
    {
      "id": "1512",
      "event": "subscribe",
      "arg": {
          "channel": "trades-all",
          "instId": "BTC-USDT"
        },
      "connId": "a4d3ae55"
    }
    

> Failure Response Example
    
    
    {
      "id": "1512",
      "event": "error",
      "code": "60012",
      "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{ \"channel\" : \"trades-all\", \"instId\" : \"BTC-USD-191227\"}]}",
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
> instId | String | Yes | Instrument ID  
code | String | No | Error code  
msg | String | No | Error message  
connId | String | Yes | WebSocket connection ID  
  
> Push Data Example
    
    
    {
      "arg": {
        "channel": "trades-all",
        "instId": "BTC-USDT"
      },
      "data": [
        {
          "instId": "BTC-USDT",
          "tradeId": "130639474",
          "px": "42219.9",
          "sz": "0.12060306",
          "side": "buy",
          "source": "0",
          "ts": "1630048897897"
        }
      ]
    }
    

#### Push data parameters

**Parameter** | **Type** | **Description**  
---|---|---  
arg | Object | Successfully subscribed channel  
> channel | String | Channel name  
> instId | String | Instrument ID  
data | Array of objects | Subscribed data  
> instId | String | Instrument ID, e.g. `BTC-USDT`  
> tradeId | String | Trade ID  
> px | String | Trade price  
> sz | String | Trade quantity   
For spot trading, the unit is base currency  
For `FUTURES`/`SWAP`/`OPTION`, the unit is contract.  
> side | String | Trade direction  
`buy`  
`sell`  
> source | String | Order source  
`0`: normal  
`1`: Enhanced Liquidity Program order  
> ts | String | Filled time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
  
### WS / Order book channel

Retrieve order book data. Best ask price may be lower than the best bid price during the pre-open period.  

Use `books` for 400 depth levels, `books5` for 5 depth levels, `bbo-tbt` tick-by-tick 1 depth level, `books50-l2-tbt` tick-by-tick 50 depth levels, and `books-l2-tbt` for tick-by-tick 400 depth levels.   

  * `books`: 400 depth levels will be pushed in the initial full snapshot. Incremental data will be pushed every 100 ms for the changes in the order book during that period of time.   

  * `books-elp`: only push ELP orders. 400 depth levels will be pushed in the initial full snapshot. Incremental data will be pushed every 100 ms for the changes in the order book during that period of time.   

  * `books5`: 5 depth levels snapshot will be pushed in the initial push. Snapshot data will be pushed every 100 ms when there are changes in the 5 depth levels snapshot.  

  * `bbo-tbt`: 1 depth level snapshot will be pushed in the initial push. Snapshot data will be pushed every 10 ms when there are changes in the 1 depth level snapshot.   

  * `books-l2-tbt`: 400 depth levels will be pushed in the initial full snapshot. Incremental data will be pushed every 10 ms for the changes in the order book during that period of time.   

  * `books50-l2-tbt`: 50 depth levels will be pushed in the initial full snapshot. Incremental data will be pushed every 10 ms for the changes in the order book during that period of time.
  * The push sequence for order book channels within the same connection and trading symbols is fixed as: bbo-tbt -> books-l2-tbt -> books50-l2-tbt -> books -> books-elp -> books5.
  * Users can not simultaneously subscribe to `books-l2-tbt` and `books50-l2-tbt/books` channels for the same trading symbol. 
    * For more details, please refer to the changelog [2024-07-17](/docs-v5/log_en/#2024-07-17)

Only API users who are VIP4 and above in trading fee tier are allowed to subscribe to "books-l2-tbt" 400 depth channels. Other users will receive error code 64003.  
Only API users who are VIP4 and above in trading fee tier are allowed to subscribe to "books50-l2-tbt" 50 depth channels. Other users will receive error code 64003.  

Identity verification refers to [Login](/docs-v5/en/#overview-websocket-login)

#### URL Path

/ws/v5/public

> Request Example
    
    
    {
      "id": "1512",
      "op": "subscribe",
      "args": [
        {
          "channel": "books",
          "instId": "BTC-USDT"
        }
      ]
    }
    
    
    
    import asyncio
    
    from okx.websocket.WsPublicAsync import WsPublicAsync
    
    
    def callbackFunc(message):
        print(message)
    
    
    async def main():
        ws = WsPublicAsync(url="wss://wspap.okx.com:8443/ws/v5/public")
        await ws.start()
        args = [
          {
            "channel": "books",
            "instId": "BTC-USDT"
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
`books`  
`books5`  
`bbo-tbt`  
`books50-l2-tbt`  
`books-l2-tbt`  
> instId | String | Yes | Instrument ID  
  
> Response Example
    
    
    {
      "id": "1512",
      "event": "subscribe",
      "arg": {
        "channel": "books",
        "instId": "BTC-USDT"
      },
      "connId": "a4d3ae55"
    }
    

> Failure example
    
    
    {
      "id": "1512",
      "event": "error",
      "code": "60012",
      "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{ \"channel\" : \"books\", \"instId\" : \"BTC-USD-191227\"}]}",
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
> instId | String | Yes | Instrument ID  
msg | String | No | Error message  
code | String | No | Error code  
connId | String | Yes | WebSocket connection ID  
  
> Push Data Example: Full Snapshot
    
    
    {
      "arg": {
        "channel": "books",
        "instId": "BTC-USDT"
      },
      "action": "snapshot",
      "data": [
        {
          "asks": [
            ["8476.98", "415", "0", "13"],
            ["8477", "7", "0", "2"],
            ["8477.34", "85", "0", "1"],
            ["8477.56", "1", "0", "1"],
            ["8505.84", "8", "0", "1"],
            ["8506.37", "85", "0", "1"],
            ["8506.49", "2", "0", "1"],
            ["8506.96", "100", "0", "2"]
          ],
          "bids": [
            ["8476.97", "256", "0", "12"],
            ["8475.55", "101", "0", "1"],
            ["8475.54", "100", "0", "1"],
            ["8475.3", "1", "0", "1"],
            ["8447.32", "6", "0", "1"],
            ["8447.02", "246", "0", "1"],
            ["8446.83", "24", "0", "1"],
            ["8446", "95", "0", "3"]
          ],
          "ts": "1597026383085",
          "checksum": 0,
          "prevSeqId": -1,
          "seqId": 123456
        }
      ]
    }
    

> Push Data Example: Incremental Data
    
    
    {
      "arg": {
        "channel": "books",
        "instId": "BTC-USDT"
      },
      "action": "update",
      "data": [
        {
          "asks": [
            ["8476.98", "415", "0", "13"],
            ["8477", "7", "0", "2"],
            ["8477.34", "85", "0", "1"],
            ["8477.56", "1", "0", "1"],
            ["8505.84", "8", "0", "1"],
            ["8506.37", "85", "0", "1"],
            ["8506.49", "2", "0", "1"],
            ["8506.96", "100", "0", "2"]
          ],
          "bids": [
            ["8476.97", "256", "0", "12"],
            ["8475.55", "101", "0", "1"],
            ["8475.54", "100", "0", "1"],
            ["8475.3", "1", "0", "1"],
            ["8447.32", "6", "0", "1"],
            ["8447.02", "246", "0", "1"],
            ["8446.83", "24", "0", "1"],
            ["8446", "95", "0", "3"]
          ],
          "ts": "1597026383085",
          "checksum": 0,
          "prevSeqId": 123456,
          "seqId": 123457
        }
      ]
    }
    

#### Push data parameters

**Parameter** | **Type** | **Description**  
---|---|---  
arg | Object | Successfully subscribed channel  
> channel | String | Channel name  
> instId | String | Instrument ID  
action | String | Push data action, incremental data or full snapshot.   
`snapshot`: full   
`update`: incremental  
data | Array of objects | Subscribed data  
> asks | Array of Arrays | Order book on sell side  
> bids | Array of Arrays | Order book on buy side  
> ts | String | Order book generation time, Unix timestamp format in milliseconds, e.g. `1597026383085`   
Exception: For the `bbo-tbt` channel, `ts` is the timestamp when the book is generated by matching engine.  
> checksum | Integer | ~~Checksum~~ (Deprecated). The field remains in the push for `books`, `books-l2-tbt`, and `books50-l2-tbt`, but its value is fixed to `0` and must no longer be used for integrity verification. Please use `seqId/prevSeqId` to verify data continuity and accuracy.  
> prevSeqId | Integer | Sequence ID of the last sent message. Only applicable to `books`, `books-l2-tbt`, `books50-l2-tbt`  
> seqId | Integer | Sequence ID of the current message, implementation details below  
An example of the array of asks and bids values: ["411.8", "10", "0", "4"]  
\- "411.8" is the depth price  
\- "10" is the quantity at the price (number of contracts for derivatives, quantity in base currency for Spot and Spot Margin)  
\- "0" is part of a deprecated feature and it is always "0"  
\- "4" is the number of orders at the price.  If you need to subscribe to many 50 or 400 depth level channels, it is recommended to subscribe through multiple websocket connections, with each of less than 30 channels.  The order book data will be updated around once a second during the call auction.  `books/books5/bbo-tbt/books-l2-tbt/books50-l2-tbt` don't return ELP orders  
`books-elp` only return ELP orders, including both valid and invalid parts (invalid parts means ELP buy orders with a price higher than best bid of non-ELP orders; or ELP sell orders with a price lower than best ask of non-ELP orders). Users should distinguish valid and invalid parts using the best bid/ask price of non-ELP orders. 

#### Sequence ID

`seqId` is the sequence ID of the market data published. The set of sequence ID received by users is the same if users are connecting to the same channel through multiple websocket connections. Each `instId` has an unique set of sequence ID. Users can use `prevSeqId` and `seqId` to build the message sequencing for incremental order book updates. Generally the value of seqId is larger than prevSeqId. The `prevSeqId` in the new message matches with `seqId` of the previous message. The smallest possible sequence ID value is 0, except in snapshot messages where the prevSeqId is always -1.  

Exceptions:  
1\. If there are no updates to the depth for an extended period(Around 60 seconds), for the channel that always updates snapshot data, OKX will send the latest snapshot, for the channel that has incremental data, OKX will send a message with `'asks': [], 'bids': []` to inform users that the connection is still active. `seqId` is the same as the last sent message and `prevSeqId` equals to `seqId`. 2\. The sequence number may be reset due to maintenance, and in this case, users will receive an incremental message with `seqId` smaller than `prevSeqId`. However, subsequent messages will follow the regular sequencing rule.

##### Example

  1. Snapshot message: prevSeqId = -1, seqId = 10
  2. Incremental message 1 (normal update): prevSeqId = 10, seqId = 15
  3. Incremental message 2 (no update): prevSeqId = 15, seqId = 15
  4. Incremental message 3 (sequence reset): prevSeqId = 15, seqId = 3
  5. Incremental message 4 (normal update): prevSeqId = 3, seqId = 5

> Push Data Example of bbo-tbt channel
    
    
    {
      "arg": {
        "channel": "bbo-tbt",
        "instId": "BCH-USDT-SWAP"
      },
      "data": [
        {
          "asks": [
            [
              "111.06","55154","0","2"
            ]
          ],
          "bids": [
            [
              "111.05","57745","0","2"
            ]
          ],
          "ts": "1670324386802",
          "seqId": 363996337
        }
      ]
    }
    

> Push Data Example of books5 channel
    
    
    {
      "arg": {
        "channel": "books5",
        "instId": "BCH-USDT-SWAP"
      },
      "data": [
        {
          "asks": [
            ["111.06","55154","0","2"],
            ["111.07","53276","0","2"],
            ["111.08","72435","0","2"],
            ["111.09","70312","0","2"],
            ["111.1","67272","0","2"]],
          "bids": [
            ["111.05","57745","0","2"],
            ["111.04","57109","0","2"],
            ["111.03","69563","0","2"],
            ["111.02","71248","0","2"],
            ["111.01","65090","0","2"]],
          "instId": "BCH-USDT-SWAP",
          "ts": "1670324386802",
          "seqId": 363996337
        }
      ]
    }
    

### WS / Option trades channel

Retrieve the recent trades data. Data will be pushed whenever there is a trade. Every update contain only one trade.

#### URL Path

/ws/v5/public

> Request Example
    
    
    {
      "id": "1512",
        "op": "subscribe",
        "args": [{
            "channel": "option-trades",
            "instType": "OPTION",
            "instFamily": "BTC-USD"
        }]
    }
    
    
    
    import asyncio
    
    from okx.websocket.WsPublicAsync import WsPublicAsync
    
    
    def callbackFunc(message):
        print(message)
    
    
    async def main():
        ws = WsPublicAsync(url="wss://wspap.okx.com:8443/ws/v5/public")
        await ws.start()
        args = [{
            "channel": "option-trades",
            "instType": "OPTION",
            "instFamily": "BTC-USD"
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
op | String | Yes | `subscribe` `unsubscribe`  
args | Array of objects | Yes | List of subscribed channels  
> channel | String | Yes | Channel name  
`option-trades`  
> instType | String | Yes | Instrument type, `OPTION`  
> instId | String | Conditional | Instrument ID, e.g. BTC-USD-221230-4000-C, Either `instId` or `instFamily` is required. If both are passed, `instId` will be used.  
> instFamily | String | Conditional | Instrument family, e.g. BTC-USD  
  
> Successful Response Example
    
    
    {
      "id": "1512",
        "event": "subscribe",
        "arg": {
            "channel": "option-trades",
            "instType": "OPTION",
            "instFamily": "BTC-USD"
        },
        "connId": "a4d3ae55"
    }
    

> Failure Response Example
    
    
    {
      "id": "1512",
      "event": "error",
      "code": "60012",
      "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{ \"channel\" : \"option-trades\"}]}",
      "connId": "a4d3ae55"
    }
    

#### Response parameters

Parameter | Type | Required | Description  
---|---|---|---  
id | String | No | Unique identifier of the message  
event | String | Yes | `subscribe` `unsubscribe` `error`  
arg | Object | No | Subscribed channel  
> channel | String | Yes | Channel name  
`status`  
code | String | No | Error code  
msg | String | No | Error message  
connId | String | Yes | WebSocket connection ID  
  
> Push Data Example
    
    
    {
        "arg": {
            "channel": "option-trades",
            "instType": "OPTION",
            "instFamily": "BTC-USD"
        },
        "data": [
            {
                "fillVol": "0.5066007836914062",
                "fwdPx": "16469.69928595038",
                "idxPx": "16537.2",
                "instFamily": "BTC-USD",
                "instId": "BTC-USD-230224-18000-C",
                "markPx": "0.04690107010619562",
                "optType": "C",
                "px": "0.045",
                "side": "sell",
                "sz": "2",
                "tradeId": "38",
                "ts": "1672286551080"
            }
        ]
    }
    

#### Push data parameters

Parameter | Type | Description  
---|---|---  
arg | Object | Successfully subscribed channel  
> channel | String | Channel name  
data | Array of objects | Subscribed data  
> instId | String | Instrument ID  
> instFamily | String | Instrument family  
> tradeId | String | Trade ID  
> px | String | Trade price  
> sz | String | Trade quantity. The unit is contract.  
> side | String | Trade side   
`buy`   
`sell`  
> optType | String | Option type, C: Call P: Put  
> fillVol | String | Implied volatility while trading (Correspond to trade price)  
> fwdPx | String | Forward price while trading  
> idxPx | String | Index price while trading  
> markPx | String | Mark price while trading  
> ts | String | Trade time, Unix timestamp format in milliseconds, e.g. `1597026383085`.  
The first data you receive after subscribing may be cached from the previous trade, so please ignore it. 

### WS / Call auction details channel

Retrieve call auction details.

#### URL Path

/ws/v5/public

> Request Example
    
    
    {
        "id": "1512",
        "op": "subscribe",
        "args": [{
            "channel": "call-auction-details",
            "instId": "ONDO-USDC"
        }]
    }
    
    
    
    
    import asyncio
    
    from okx.websocket.WsPublicAsync import WsPublicAsync
    
    
    def callbackFunc(message):
        print(message)
    
    
    async def main():
        ws = WsPublicAsync(url="wss://wspap.okx.com:8443/ws/v5/public")
        await ws.start()
        args = [{
            "channel": "call-auction-details",
            "instId": "ONDO-USDC"
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
`call-auction-details`  
> instId | String | Yes | Instrument ID  
  
> Successful Response Example
    
    
    {
      "id": "1512",
      "event": "subscribe",
      "arg": {
          "channel": "call-auction-details",
          "instId": "ONDO-USDC"
        },
      "connId": "a4d3ae55"
    }
    
    

> Failure Response Example
    
    
    {
      "id": "1512",
      "event": "error",
      "code": "60012",
      "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{ \"channel\" : \"call-auction-details\", \"instId\" : \"BTC-USD-191227\"}]}",
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
> channel | String | yes | channel name  
> instId | String | Yes | Instrument ID  
code | String | No | Error code  
msg | String | No | Error message  
connId | String | Yes | WebSocket connection ID  
  
> Push Data Example
    
    
    {
      "arg": {
        "channel": "call-auction-details",
        "instId": "ONDO-USDC"
      },
      "data": [
            {
                "instId": "ONDO-USDC",
                "unmatchedSz": "9988764",
                "eqPx": "0.6",
                "matchedSz": "44978",
                "state": "continuous_trading",
                "auctionEndTime": "1726542000000",
                "ts": "1726542000007"
            }
      ]
    }
    
    

#### Push data parameters

**Parameter** | **Type** | **Description**  
---|---|---  
arg | Object | Successfully subscribed channel  
> channel | String | Channel name  
> instId | String | Instrument ID  
data | Array of objects | Subscribed data  
> instId | String | Instrument ID  
> eqPx | String | Equilibrium price  
> matchedSz | String | Matched size for both buy and sell  
The unit is in base currency  
> unmatchedSz | String | Unmatched size  
> auctionEndTime | String | Call auction end time. Unix timestamp in milliseconds.  
> state | String | Trading state of the symbol  
`call_auction`  
`continuous_trading`  
> ts | String | Data generation time. Unix timestamp in millieseconds.  
During call auction, users can get the updates of equilibrium price, matched size, unmatched size, and auction end time. The data will be updated around once a second. When call auction ends, this channel will push the last message, returning the actual open price, matched size, and unmatched size, with trading state as `continuous_trading`.

---

# 行情数据

`行情数据`功能模块下的API接口不需要身份验证。  
  
行情数据存在多个服务且每个服务有独立的缓存，每次会随机请求到某一个服务，所以会存在两次请求，第二次获取到的数据早于第一次的情况。

针对事件合约，行情数据模块只返回YES侧的数据，用户可自行推导出NO侧数据。

### GET / 获取所有产品行情信息 

获取产品行情信息。在提前挂单阶段，best ask的价格有机会低于best bid。

#### 限速：20次/2s

#### 限速规则：IP

#### HTTP请求

`GET /api/v5/market/tickers`

> 请求示例
    
    
    GET /api/v5/market/tickers?instType=SWAP
    
    
    
    
    import okx.MarketData as MarketData
    
    flag = "0"  # 实盘:0 , 模拟盘：1
    
    marketDataAPI =  MarketData.MarketAPI(flag=flag)
    
    # 获取所有产品行情信息
    result = marketDataAPI.get_tickers(
        instType="SWAP"
    )
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
instType | String | 是 | 产品类型  
`SPOT`：币币  
`SWAP`：永续合约  
`FUTURES`：交割合约  
`OPTION`：期权  
`EVENTS`：事件合约  
instFamily | String | 否 | 交易品种  
适用于`交割`/`永续`/`期权`，如 `BTC-USD`  
  
> 返回结果
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
         {
            "instType":"SWAP",
            "instId":"LTC-USD-SWAP",
            "last":"9999.99",
            "lastSz":"1",
            "askPx":"9999.99",
            "askSz":"11",
            "bidPx":"8888.88",
            "bidSz":"5",
            "open24h":"9000",
            "high24h":"10000",
            "low24h":"8888.88",
            "volCcy24h":"2222",
            "vol24h":"2222",
            "sodUtc0":"0.1",
            "sodUtc8":"0.1",
            "ts":"1597026383085"
         },
         {
            "instType":"SWAP",
            "instId":"BTC-USD-SWAP",
            "last":"9999.99",
            "lastSz":"1",
            "askPx":"9999.99",
            "askSz":"11",
            "bidPx":"8888.88",
            "bidSz":"5",
            "open24h":"9000",
            "high24h":"10000",
            "low24h":"8888.88",
            "volCcy24h":"2222",
            "vol24h":"2222",
            "sodUtc0":"0.1",
            "sodUtc8":"0.1",
            "ts":"1597026383085"
        }
      ]
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
instType | String | 产品类型  
instId | String | 产品ID  
last | String | 最新成交价  
lastSz | String | 最新成交的数量，0 代表没有成交量  
askPx | String | 卖一价  
askSz | String | 卖一价的挂单数数量  
bidPx | String | 买一价  
bidSz | String | 买一价的挂单数量  
open24h | String | 24小时开盘价  
high24h | String | 24小时最高价  
low24h | String | 24小时最低价  
volCcy24h | String | 24小时成交量，以`币`为单位  
如果是`衍生品`合约，数值为交易货币的数量。比如，对于 BTC-USD-SWAP 和 BTC-USDT-SWAP，单位均为 BTC  
如果是`币币/币币杠杆`，数值为计价货币的数量。  
vol24h | String | 24小时成交量，以`张`为单位  
如果是`衍生品`合约，数值为合约的张数。  
如果是`币币/币币杠杆`，数值为交易货币的数量。  
sodUtc0 | String | UTC 0 时开盘价  
sodUtc8 | String | UTC+8 时开盘价  
ts | String | ticker数据产生时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
  
### GET / 获取单个产品行情信息 

获取产品行情信息。在提前挂单阶段，best ask的价格有机会低于best bid。

#### 限速：20次/2s

#### 限速规则：IP

#### HTTP请求

`GET /api/v5/market/ticker`

> 请求示例
    
    
    GET /api/v5/market/ticker?instId=BTC-USD-SWAP
    
    
    
    
    import okx.MarketData as MarketData
    
    flag = "0"  # 实盘:0 , 模拟盘：1
    
    marketDataAPI =  MarketData.MarketAPI(flag=flag)
    
    # 获取单个产品行情信息
    result = marketDataAPI.get_ticker(
        instId="BTC-USD-SWAP"
    )
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
instId | String | 是 | 产品ID，如 `BTC-USD-SWAP`  
  
> 返回结果
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "instType": "SWAP",
                "instId": "BTC-USD-SWAP",
                "last": "56956.1",
                "lastSz": "3",
                "askPx": "56959.1",
                "askSz": "10582",
                "bidPx": "56959",
                "bidSz": "4552",
                "open24h": "55926",
                "high24h": "57641.1",
                "low24h": "54570.1",
                "volCcy24h": "81137.755",
                "vol24h": "46258703",
                "ts": "1620289117764",
                "sodUtc0": "55926",
                "sodUtc8": "55926"
            }
        ]
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
instType | String | 产品类型  
instId | String | 产品ID  
last | String | 最新成交价  
lastSz | String | 最新成交的数量，0 代表没有成交量  
askPx | String | 卖一价  
askSz | String | 卖一价对应的数量  
bidPx | String | 买一价  
bidSz | String | 买一价对应的数量  
open24h | String | 24小时开盘价  
high24h | String | 24小时最高价  
low24h | String | 24小时最低价  
volCcy24h | String | 24小时成交量，以`币`为单位  
如果是`衍生品`合约，数值为交易货币的数量。  
如果是`币币/币币杠杆`，数值为计价货币的数量。  
vol24h | String | 24小时成交量，以`张`为单位  
如果是`衍生品`合约，数值为合约的张数。  
如果是`币币/币币杠杆`，数值为交易货币的数量。  
sodUtc0 | String | UTC+0 时开盘价  
sodUtc8 | String | UTC+8 时开盘价  
ts | String | ticker数据产生时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
  
### GET / 获取产品深度 

获取产品深度列表，数据每 50 毫秒更新一次。在提前挂单阶段，best ask的价格有机会低于best bid。  
该接口收到请求后不会立刻返回，而是会待服务端缓存数据更新后立即返回最新数据。

#### 限速：40次/2s

#### 限速规则：IP

#### HTTP请求

`GET /api/v5/market/books`

> 请求示例
    
    
    GET /api/v5/market/books?instId=BTC-USDT
    
    
    
    import okx.MarketData as MarketData
    
    flag = "0"  # 实盘:0 , 模拟盘：1
    
    marketDataAPI =  MarketData.MarketAPI(flag=flag)
    
    # 获取产品深度
    result = marketDataAPI.get_orderbook(
        instId="BTC-USDT"
    )
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
instId | String | 是 | 产品ID，如 `BTC-USDT`  
sz | String | 否 | 深度档位数量，最大值可传400，即买卖深度共800条   
不填写此参数，默认返回`1`档深度数据  
  
> 返回结果
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "asks": [
                    [
                        "41006.8",
                        "0.60038921",
                        "0",
                        "1"
                    ]
                ],
                "bids": [
                    [
                        "41006.3",
                        "0.30178218",
                        "0",
                        "2"
                    ]
                ],
                "ts": "1629966436396",
                "seqId": 3235851742
            }
        ]
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
asks | Array of Arrays | 卖方深度  
bids | Array of Arrays | 买方深度  
ts | String | 深度产生的时间  
seqId | Integer | 当前消息的序列号  
合约的asks和bids值数组举例说明： ["411.8","10", "0","4"] 411.8为深度价格，10为此价格的合约张数，0该字段已弃用(始终为0)，4为此价格的订单数量  
现货/币币杠杆的asks和bids值数组举例说明： ["411.8","10", "0","4"] 411.8为深度价格，10为此价格的交易币的数量，0该字段已弃用(始终为0)，4为此价格的订单数量 asks和bids值数组举例说明： ["411.8", "10", "0", "4"]  
\- 411.8为深度价格  
\- 10为此价格的数量 （合约交易为张数，现货/币币杠杆为交易币的数量）  
\- 0该字段已弃用(始终为0)  
\- 4为此价格的订单数量  集合竞价期间，深度数据大约每秒更新一次 

### GET / 获取产品完整深度 

获取产品深度列表。数据每秒更新一次。在提前挂单阶段，best ask的价格有机会低于best bid。  
该接口收到请求后不会立刻返回，而是会待服务端缓存数据更新后立即返回最新数据。

#### 限速：10次/2s

#### 限速规则：IP

#### HTTP请求

`GET /api/v5/market/books-full`

> 请求示例
    
    
    GET /api/v5/market/books-full?instId=BTC-USDT&sz=20
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
instId | String | 是 | 产品ID，如 `BTC-USDT`  
sz | String | 否 | 深度档位数量，最大值可传5000，即买卖深度共10000条   
不填写此参数，默认返回`1`档深度数据  
  
> 返回结果
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "asks": [
                    [
                        "41006.8",
                        "0.60038921",
                        "1"
                    ]
                ],
                "bids": [
                    [
                        "41006.3",
                        "0.30178218",
                        "2"
                    ]
                ],
                "ts": "1629966436396"
            }
        ]
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
asks | Array of Arrays | 卖方深度  
bids | Array of Arrays | 买方深度  
ts | String | 深度产生的时间  
合约的asks和bids值数组举例说明： ["411.8", "10", "4"] 411.8为深度价格，10为此价格的合约张数，4为此价格的订单数量  
现货/币币杠杆的asks和bids值数组举例说明： ["411.8", "10", "4"] 411.8为深度价格，10为此价格的交易币的数量，4为此价格的订单数量  
asks和bids值数组举例说明： ["411.8", "10", "4"]  
\- 411.8为深度价格  
\- 10为此价格的数量 （合约交易为张数，现货/币币杠杆为交易币的数量）  
\- 4为此价格的订单数量  集合竞价期间，深度数据大约每秒更新一次 

### GET / 获取交易产品K线数据 

获取K线数据。K线数据按请求的粒度分组返回，K线数据每个粒度最多可获取最近1,440条。

#### 限速：40次/2s

#### 限速规则：IP

#### HTTP请求

`GET /api/v5/market/candles`

> 请求示例
    
    
    GET /api/v5/market/candles?instId=BTC-USDT
    
    
    
    import okx.MarketData as MarketData
    
    flag = "0"  # 实盘:0 , 模拟盘：1
    
    marketDataAPI =  MarketData.MarketAPI(flag=flag)
    
    # 获取交易产品K线数据
    result = marketDataAPI.get_candlesticks(
        instId="BTC-USDT"
    )
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
instId | String | 是 | 产品ID，如 `BTC-USDT`  
bar | String | 否 | 时间粒度，默认值`1m`  
如 [1m/3m/5m/15m/30m/1H/2H/4H]   
UTC+8开盘价k线：[6H/12H/1D/2D/3D/1W/1M/3M]  
UTC+0开盘价k线：[/6Hutc/12Hutc/1Dutc/2Dutc/3Dutc/1Wutc/1Mutc/3Mutc]  
after | String | 否 | 请求此时间戳之前（更旧的数据）的分页内容，传的值为对应接口的`ts`  
before | String | 否 | 请求此时间戳之后（更新的数据）的分页内容，传的值为对应接口的`ts`, 单独使用时，会返回最新的数据。  
limit | String | 否 | 分页返回的结果集数量，最大为300，不填默认返回100条  
adjust | String | 否 | 复权类型，仅适用于股票永续合约。  
`forward`：前复权。  
不填时默认返回不复权数据。  
  
> 返回结果
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
         [
            "1597026383085",
            "3.721",
            "3.743",
            "3.677",
            "3.708",
            "8422410",
            "22698348.04828491",
            "12698348.04828491",
            "0"
        ],
        [
            "1597026383085",
            "3.731",
            "3.799",
            "3.494",
            "3.72",
            "24912403",
            "67632347.24399722",
            "37632347.24399722",
            "1"
        ]
        ]
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
ts | String | 开始时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
o | String | 开盘价格  
h | String | 最高价格  
l | String | 最低价格  
c | String | 收盘价格  
vol | String | 交易量，以`张`为单位  
如果是`衍生品`合约，数值为合约的张数。  
如果是`币币/币币杠杆`，数值为交易货币的数量。  
volCcy | String | 交易量，以`币`为单位  
如果是`衍生品`合约，数值为交易货币的数量。  
如果是`币币/币币杠杆`，数值为计价货币的数量。  
volCcyQuote | String | 交易量，以计价货币为单位  
如 `BTC-USDT`和`BTC-USDT-SWAP`，单位均是`USDT`。  
`BTC-USD-SWAP`单位是`USD`。  
confirm | String | K线状态  
`0`：K线未完结  
`1`：K线已完结  
返回的第一条K线数据可能不是完整周期k线，返回值数组顺序分别为是：[ts,o,h,l,c,vol,volCcy,volCcyQuote,confirm]   
对于当前周期的K线数据，没有成交时，开高收低默认都取上一周期的收盘价格。  当传入 `adjust=forward` 时，历史K线的开高低收（OHLC）价格将乘以对应时期的复权因子。对于拆股，成交量（`vol`、`volCcy`）也会按相同比例调整。成交金额（`volCcyQuote`）不做调整。该参数仅对股票永续合约有效。 

### GET / 获取交易产品历史K线数据

获取最近几年的历史k线数据(1s k线支持查询最近3个月的数据)

#### 限速：20次/2s

#### 限速规则：IP

#### HTTP请求

`GET /api/v5/market/history-candles`

> 请求示例
    
    
    GET /api/v5/market/history-candles?instId=BTC-USDT
    
    
    
    import okx.MarketData as MarketData
    
    flag = "0"  # 实盘:0 , 模拟盘：1
    
    marketDataAPI =  MarketData.MarketAPI(flag=flag)
    
    # 获取交易产品历史K线数据
    result = marketDataAPI.get_history_candlesticks(
        instId="BTC-USDT"
    )
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
instId | String | 是 | 产品ID，如 `BTC-USDT`  
after | String | 否 | 请求此时间戳之前（更旧的数据）的分页内容，传的值为对应接口的`ts`  
before | String | 否 | 请求此时间戳之后（更新的数据）的分页内容，传的值为对应接口的`ts`, 单独使用时，会返回最新的数据。  
bar | String | 否 | 时间粒度，默认值`1m`  
如 [1s/1m/3m/5m/15m/30m/1H/2H/4H]   
UTC+8开盘价k线：[6H/12H/1D/2D/3D/1W/1M/3M]  
UTC+0开盘价k线：[6Hutc/12Hutc/1Dutc/2Dutc/3Dutc/1Wutc/1Mutc/3Mutc]  
limit | String | 否 | 分页返回的结果集数量，最大为300，不填默认返回100条  
adjust | String | 否 | 复权类型，仅适用于股票永续合约。  
`forward`：前复权。  
不填时默认返回不复权数据。  
  
> 返回结果
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
         [
            "1597026383085",
            "3.721",
            "3.743",
            "3.677",
            "3.708",
            "8422410",
            "22698348.04828491",
            "12698348.04828491",
            "1"
        ],
        [
            "1597026383085",
            "3.731",
            "3.799",
            "3.494",
            "3.72",
            "24912403",
            "67632347.24399722",
            "37632347.24399722",
            "1"
        ]
        ]
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
ts | String | 开始时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
o | String | 开盘价格  
h | String | 最高价格  
l | String | 最低价格  
c | String | 收盘价格  
vol | String | 交易量，以`张`为单位  
如果是`衍生品`合约，数值为合约的张数。  
如果是`币币/币币杠杆`，数值为交易货币的数量。  
volCcy | String | 交易量，以`币`为单位  
如果是`衍生品`合约，数值为交易货币的数量。  
如果是`币币/币币杠杆`，数值为计价货币的数量。  
volCcyQuote | String | 交易量，以计价货币为单位  
如 `BTC-USDT`和`BTC-USDT-SWAP`，单位均是`USDT`  
`BTC-USD-SWAP`单位是`USD`  
confirm | String | K线状态  
`0`：K线未完结  
`1`：K线已完结  
返回值数组顺序分别为是：[ts,o,h,l,c,vol,volCcy,volCcyQuote,confirm]  期权不支持 1s K线， 其他业务线 (币币, 杠杆, 交割和永续)支持  当传入 `adjust=forward` 时，历史K线的开高低收（OHLC）价格将乘以对应时期的复权因子。对于拆股，成交量（`vol`、`volCcy`）也会按相同比例调整。成交金额（`volCcyQuote`）不做调整。该参数仅对股票永续合约有效。 

### GET / 获取交易产品公共成交数据 

查询市场上的成交信息数据

#### 限速：100次/2s

#### 限速规则：IP

#### HTTP请求

`GET /api/v5/market/trades`

> 请求示例
    
    
    GET /api/v5/market/trades?instId=BTC-USDT
    
    
    
    import okx.MarketData as MarketData
    
    flag = "0"  # 实盘:0 , 模拟盘：1
    
    marketDataAPI =  MarketData.MarketAPI(flag=flag)
    
    # 获取交易产品公共成交数据
    result = marketDataAPI.get_trades(
        instId="BTC-USDT"
    )
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
instId | String | 是 | 产品ID，如 `BTC-USDT`  
limit | String | 否 | 分页返回的结果集数量，最大为500，不填默认返回100条  
  
> 返回结果
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "instId": "BTC-USDT",
                "side": "sell",
                "sz": "0.00001",
                "source": "0",
                "px": "29963.2",
                "tradeId": "242720720",
                "ts": "1654161646974"
            },
            {
                "instId": "BTC-USDT",
                "side": "sell",
                "sz": "0.00001",
                "source": "0",
                "px": "29964.1",
                "tradeId": "242720719",
                "ts": "1654161641568"
            }
        ]
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
instId | String | 产品ID  
tradeId | String | 成交ID  
px | String | 成交价格  
sz | String | 成交数量  
对于币币交易，成交数量的单位为交易货币  
对于交割、永续以及期权，单位为张。  
side | String | 吃单方向  
`buy`：买  
`sell`：卖  
source | String | 订单来源  
`0`：普通订单  
`1`：流动性增强计划订单  
ts | String | 成交时间，Unix时间戳的毫秒数格式， 如`1597026383085`  
最多获取最近500条历史公共成交数据 

### GET / 获取交易产品公共历史成交数据 

查询市场上的成交信息数据，可以分页获取最近3个月的数据。

#### 限速：20次/2s

#### 限速规则：IP

#### HTTP请求

`GET /api/v5/market/history-trades`

> 请求示例
    
    
    GET /api/v5/market/history-trades?instId=BTC-USDT
    
    
    
    import okx.MarketData as MarketData
    
    flag = "0"  # 实盘:0 , 模拟盘：1
    
    marketDataAPI =  MarketData.MarketAPI(flag=flag)
    
    # 获取交易产品公共历史成交数据
    result = marketDataAPI.get_history_trades(
        instId="BTC-USDT"
    )
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
instId | String | 是 | 产品ID，如 `BTC-USDT`  
type | String | 否 | 分页类型  
`1`：tradeId 分页 `2`：时间戳分页  
默认为`1`：tradeId 分页  
after | String | 否 | 请求此 ID 或 ts 之前的分页内容，传的值为对应接口的 tradeId 或 ts  
before | String | 否 | 请求此ID之后（更新的数据）的分页内容，传的值为对应接口的 tradeId。  
不支持时间戳分页。单独使用时，会返回最新的数据。  
limit | String | 否 | 分页返回的结果集数量，最大为100，不填默认返回100条  
  
> 返回结果
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "instId": "BTC-USDT",
                "side": "sell",
                "sz": "0.00001",
                "source": "0",
                "px": "29963.2",
                "tradeId": "242720720",
                "ts": "1654161646974"
            },
            {
                "instId": "BTC-USDT",
                "side": "sell",
                "sz": "0.00001",
                "source": "0",
                "px": "29964.1",
                "tradeId": "242720719",
                "ts": "1654161641568"
            }
        ]
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
instId | String | 产品ID  
tradeId | String | 成交ID  
px | String | 成交价格  
sz | String | 成交数量  
对于币币交易，成交数量的单位为交易货币  
对于交割、永续以及期权，单位为张。  
side | String | 吃单方向   
`buy`：买   
`sell`：卖  
source | String | 订单来源  
`0`：普通订单  
`1`：流动性增强计划订单  
ts | String | 成交时间，Unix时间戳的毫秒数格式， 如`1597026383085`  
  
### GET / 获取期权品种公共成交数据 

查询期权同一个交易品种下的成交信息数据，最多返回100条。

#### 限速：20次/2s

#### 限速规则：IP

#### HTTP请求

`GET /api/v5/market/option/instrument-family-trades`

> 请求示例
    
    
    GET /api/v5/market/option/instrument-family-trades?instFamily=BTC-USD
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
instFamily | String | 是 | 交易品种，如 BTC-USD，适用于期权  
  
> 返回结果
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "vol24h": "103381",
                "tradeInfo": [
                    {
                        "instId": "BTC-USD-221111-17750-C",
                        "side": "sell",
                        "sz": "1",
                        "px": "0.0075",
                        "tradeId": "20",
                        "ts": "1668090715058"
                    },
                    {
                        "instId": "BTC-USD-221111-17750-C",
                        "side": "sell",
                        "sz": "91",
                        "px": "0.01",
                        "tradeId": "19",
                        "ts": "1668090421062"
                    }
                ],
                "optType": "C"
            },
            {
                "vol24h": "144499",
                "tradeInfo": [
                    {
                        "instId": "BTC-USD-230127-10000-P",
                        "side": "sell",
                        "sz": "82",
                        "px": "0.019",
                        "tradeId": "23",
                        "ts": "1668090967057"
                    },
                    {
                        "instId": "BTC-USD-221111-16250-P",
                        "side": "sell",
                        "sz": "102",
                        "px": "0.0045",
                        "tradeId": "24",
                        "ts": "1668090885050"
                    }
                ],
                "optType": "P"
            }
        ]
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
vol24h | String | 24小时成交量，以张为单位  
optType | String | 期权类型，`C`：看涨期权 `P`：看跌期权  
tradeInfo | Array of objects | 成交数据列表  
> instId | String | 产品ID  
> tradeId | String | 成交ID  
> px | String | 成交价格  
> sz | String | 成交数量，单位为张。  
> side | String | 成交方向  
`buy`：买  
`sell`：卖  
> ts | String | 成交时间，Unix时间戳的毫秒数格式， 如1597026383085  
  
### GET / 获取期权公共成交数据

最多返回最近的100条成交数据

#### 限速：20次/2s

#### 限速规则：IP

#### HTTP请求

`GET /api/v5/public/option-trades`

> 请求示例
    
    
    GET /api/v5/public/option-trades?instFamily=BTC-USD
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
instId | String | 可选 | 产品ID，如 BTC-USD-221230-4000-C，`instId` 和 `instFamily` 必须传一个，若传两个，以 `instId` 为主  
instFamily | String | 可选 | 交易品种，如 BTC-USD  
optType | String | 否 | 期权类型，`C`：看涨期权 `P`：看跌期权  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "fillVol": "0.24415013671875",
                "fwdPx": "16676.907614127158",
                "idxPx": "16667",
                "instFamily": "BTC-USD",
                "instId": "BTC-USD-221230-16600-P",
                "markPx": "0.006308943261227884",
                "optType": "P",
                "px": "0.005",
                "side": "sell",
                "sz": "30",
                "tradeId": "65",
                "ts": "1672225112048"
            }
        ],
        "msg": ""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
instId | String | 产品ID  
instFamily | String | 交易品种  
tradeId | String | 成交ID  
px | String | 成交价格  
sz | String | 成交数量。单位为张。  
side | String | 成交方向   
`buy`：买   
`sell`：卖  
optType | String | 期权类型，C：看涨期权 P：看跌期权 ，仅适用于期权  
fillVol | String | 成交时的隐含波动率（对应成交价格）  
fwdPx | String | 成交时的远期价格  
idxPx | String | 成交时的指数价格  
markPx | String | 成交时的标记价格  
ts | String | 成交时间，Unix时间戳的毫秒数格式， 如`1597026383085`  
  
### GET / 获取平台24小时总成交量 

24小时成交量滚动计算

#### 限速：2次/2s

#### 限速规则：IP

#### HTTP请求

`GET /api/v5/market/platform-24-volume`

> 请求示例
    
    
    GET /api/v5/market/platform-24-volume
    
    
    
    
    import okx.MarketData as MarketData
    
    flag = "0"  # 实盘:0 , 模拟盘：1
    
    marketDataAPI =  MarketData.MarketAPI(flag=flag)
    
    # 获取平台24小时总成交量
    result = marketDataAPI.get_volume()
    print(result)
    

> 返回结果
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
         {
             "volCny": "230900886396766",
             "volUsd": "34462818865189",
             "ts": "1657856040389"
         }
      ]
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
volUsd | String | 订单簿交易近24小时总成交量，以美元为单位  
volCny | String | 订单簿交易近24小时总成交量，以人民币为单位  
ts | String | 接口返回数据时间  
  
### GET / 集合竞价信息 

获取集合竞价相关信息

#### 限速：20次/2s

#### 限速规则：IP

#### HTTP请求

`GET /api/v5/market/call-auction-details`

> 请求示例
    
    
    GET /api/v5/market/call-auction-details?instId=ONDO-USDC
    
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
instId | String | 是 | 产品ID，如 BTC-USDT  
  
> 返回结果
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "instId": "ONDO-USDC",
                "unmatchedSz": "9988764",
                "eqPx": "0.6",
                "matchedSz": "44978",
                "state": "continuous_trading",
                "auctionEndTime": "1726542000000",
                "ts": "1726542000007"
            }
        ]
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
instId | String | 产品ID  
eqPx | String | 均衡价格  
matchedSz | String | 买卖双边的匹配数量，单位为交易货币  
unmatchedSz | String | 未匹配数量  
auctionEndTime | String | 集合竞价结束时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
state | String | 交易状态  
`call_auction`：集合竞价  
`continuous_trading`：连续交易  
ts | String | 数据产生时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
在集合竞价期间，用户可以获取均衡价格、匹配数量、未匹配数量和集合竞价结束时间的更新。数据大约每秒更新一次。当集合竞价结束时，该接口将返回实际开盘价、匹配数量和未匹配数量。   
对于从未进入集合竞价的交易产品，该接口也会返回结果，但交易状态字段state始终为`continuous_trading`，其他字段为0或空。 

### WS / 行情频道 

获取产品的最新成交价、买一价、卖一价和24小时交易量等信息。在提前挂单阶段，best ask的价格有机会低于best bid。  
最快100ms推送一次，没有触发事件时不推送，触发推送的事件有：成交、买一卖一发生变动。

#### URL Path

/ws/v5/public

> 请求示例
    
    
    {
        "id": "1512",
        "op": "subscribe",
        "args": [{
            "channel": "tickers",
            "instId": "BTC-USDT"
        }]
    }
    
    
    
    import asyncio
    
    from okx.websocket.WsPublicAsync import WsPublicAsync
    
    
    def callbackFunc(message):
        print(message)
    
    
    async def main():
        ws = WsPublicAsync(url="wss://wspap.okx.com:8443/ws/v5/public")
        await ws.start()
        args = [{
            "channel": "tickers",
            "instId": "BTC-USDT"
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
`tickers`  
> instId | String | 是 | 产品ID  
  
> 成功返回示例
    
    
    {
        "id": "1512",
        "event": "subscribe",
        "arg": {
            "channel": "tickers",
            "instId": "BTC-USDT"
        },
        "connId": "a4d3ae55"
    }
    

> 失败返回示例
    
    
    {
        "id": "1512",
        "event": "error",
        "code": "60012",
        "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{ \"channel\" : \"tickers\", \"instId\" : \"LTC-USD-200327\"}]}",
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
> instId | String | 是 | 产品ID  
code | String | 否 | 错误码  
msg | String | 否 | 错误消息  
connId | String | 是 | WebSocket连接ID  
  
> 推送示例
    
    
    {
        "arg": {
            "channel": "tickers",
            "instId": "BTC-USDT"
        },
        "data": [{
            "instType": "SPOT",
            "instId": "BTC-USDT",
            "last": "9999.99",
            "lastSz": "0.1",
            "askPx": "9999.99",
            "askSz": "11",
            "bidPx": "8888.88",
            "bidSz": "5",
            "open24h": "9000",
            "high24h": "10000",
            "low24h": "8888.88",
            "volCcy24h": "2222",
            "vol24h": "2222",
            "sodUtc0": "2222",
            "sodUtc8": "2222",
            "ts": "1597026383085"
        }]
    }
    

#### 推送数据参数

**参数名** | **类型** | **描述**  
---|---|---  
arg | Object | 订阅成功的频道  
> channel | String | 频道名  
> instId | String | 产品ID  
data | Array of objects | 订阅的数据  
> instType | String | 产品类型  
> instId | String | 产品ID  
> last | String | 最新成交价  
> lastSz | String | 最新成交的数量，0 代表没有成交量  
> askPx | String | 卖一价  
> askSz | String | 卖一价对应的量  
> bidPx | String | 买一价  
> bidSz | String | 买一价对应的数量  
> open24h | String | 24小时开盘价  
> high24h | String | 24小时最高价  
> low24h | String | 24小时最低价  
> volCcy24h | String | 24小时成交量，以`币`为单位  
如果是`衍生品`合约，数值为交易货币的数量。  
如果是`币币/币币杠杆`，数值为计价货币的数量。  
> vol24h | String | 24小时成交量，以`张`为单位  
如果是`衍生品`合约，数值为合约的张数。  
如果是`币币/币币杠杆`，数值为交易货币的数量。  
> sodUtc0 | String | UTC+0 时开盘价  
> sodUtc8 | String | UTC+8 时开盘价  
> ts | String | 数据产生时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
  
### WS / K线频道 

获取K线数据，推送频率最快是间隔1秒推送一次数据。

#### URL Path

/ws/v5/business

> 请求示例
    
    
    {
      "id": "1512",
        "op": "subscribe",
        "args": [{
            "channel": "candle1D",
            "instId": "BTC-USDT"
        }]
    }
    
    
    
    import asyncio
    
    from okx.websocket.WsPublicAsync import WsPublicAsync
    
    
    def callbackFunc(message):
        print(message)
    
    
    async def main():
        ws = WsPublicAsync(url="wss://wspap.okx.com:8443/ws/v5/business")
        await ws.start()
        args = [
            {
              "channel": "candle1D",
              "instId": "BTC-USDT"
            }
        ]
    
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
`candle3M`  
`candle1M`  
`candle1W`  
`candle1D`  
`candle2D`  
`candle3D`  
`candle5D`  
`candle12H`  
`candle6H`  
`candle4H`  
`candle2H`  
`candle1H`  
`candle30m`  
`candle15m`  
`candle5m`  
`candle3m`  
`candle1m`  
`candle1s`  
`candle3Mutc`  
`candle1Mutc`  
`candle1Wutc`  
`candle1Dutc`  
`candle2Dutc`  
`candle3Dutc`  
`candle5Dutc`  
`candle12Hutc`  
`candle6Hutc`  
> instId | String | 是 | 产品ID  
  
> 成功返回示例
    
    
    {
      "id": "1512",
        "event": "subscribe",
        "arg": {
            "channel": "candle1D",
            "instId": "BTC-USDT"
        },
      "connId": "a4d3ae55"
    }
    

> 失败返回示例
    
    
    {
      "id": "1512",
        "event": "error",
        "code": "60012",
        "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{ \"channel\" : \"candle1D\", \"instId\" : \"BTC-USD-191227\"}]}",
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
> instId | String | 是 | 产品ID  
code | String | 否 | 错误码  
msg | String | 否 | 错误消息  
connId | String | 是 | WebSocket连接ID  
  
> 推送示例
    
    
    {
      "arg": {
        "channel": "candle1D",
        "instId": "BTC-USDT"
      },
      "data": [
        [
          "1629993600000",
          "42500",
          "48199.9",
          "41006.1",
          "41006.1",
          "3587.41204591",
          "166741046.22583129",
          "166741046.22583129",
          "0"
        ]
      ]
    }
    

#### 推送数据参数

**参数名** | **类型** | **描述**  
---|---|---  
arg | Object | 订阅成功的频道  
> channel | String | 频道名  
> instId | String | 产品ID  
data | Array of Arrays | 订阅的数据  
> ts | String | 开始时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
> o | String | 开盘价格  
> h | String | 最高价格  
> l | String | 最低价格  
> c | String | 收盘价格  
> vol | String | 交易量，以`张`为单位  
如果是`衍生品`合约，数值为合约的张数。  
如果是`币币/币币杠杆`，数值为交易货币的数量。  
> volCcy | String | 交易量，以`币`为单位  
如果是`衍生品`合约，数值为交易货币的数量。  
如果是`币币/币币杠杆`，数值为计价货币的数量。  
> volCcyQuote | String | 交易量，以计价货币为单位  
如 `BTC-USDT`和`BTC-USDT-SWAP`单位均是`USDT`。  
`BTC-USD-SWAP`单位是`USD`。  
> confirm | String | K线状态  
`0`：K线未完结  
`1`：K线已完结  
  
### WS / 交易频道 

获取最近的成交数据，有成交数据就推送，每次推送可能聚合多条成交数据。  
根据每个taker订单的不同成交价格，不同成交来源推送消息，并使用count字段表示聚合的订单匹配数量。

#### URL Path

/ws/v5/public

> 请求示例
    
    
    {
      "id": "1512",
        "op": "subscribe",
        "args": [{
            "channel": "trades",
            "instId": "BTC-USDT"
        }]
    }
    
    
    
    import asyncio
    from okx.websocket.WsPublicAsync import WsPublicAsync
    
    def callbackFunc(message):
        print(message)
    
    async def main():
        ws = WsPublicAsync(url="wss://wspap.okx.com:8443/ws/v5/public")
        await ws.start()
        args = [
            {
              "channel": "trades",
              "instId": "BTC-USDT"
            }
        ]
    
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
`trades`  
> instId | String | 是 | 产品ID  
  
> 成功返回示例
    
    
    {
      "id": "1512",
        "event": "subscribe",
        "arg": {
            "channel": "trades",
            "instId": "BTC-USDT"
        },
      "connId": "a4d3ae55"
    }
    

> 失败返回示例
    
    
    {
      "id": "1512",
        "event": "error",
        "code": "60012",
        "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{ \"channel\" : \"trades\", \"instId\" : \"BTC-USD-191227\"}]}",
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
> instId | String | 是 | 产品ID  
code | String | 否 | 错误码  
msg | String | 否 | 错误消息  
connId | String | 是 | WebSocket连接ID  
  
> 推送示例
    
    
    {
      "arg": {
        "channel": "trades",
        "instId": "BTC-USDT"
      },
      "data": [
        {
          "instId": "BTC-USDT",
          "tradeId": "130639474",
          "px": "42219.9",
          "sz": "0.12060306",
          "side": "buy",
          "ts": "1630048897897",
          "count": "3",
          "source": "0",
          "seqId": 1234
        }
      ]
    }
    

#### 推送数据参数

**参数名** | **类型** | **描述**  
---|---|---  
arg | Object | 订阅成功的频道  
> channel | String | 频道名  
> instId | String | 产品ID  
data | Array of objects | 订阅的数据  
> instId | String | 产品ID，如 `BTC-USDT`  
> tradeId | String | 聚合的多笔交易中最新一笔交易的成交ID  
> px | String | 成交价格  
> sz | String | 成交数量  
对于币币交易，成交数量的单位为交易货币  
对于交割、永续以及期权，单位为张。  
> side | String | 吃单方向  
`buy`  
`sell`  
> ts | String | 成交时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
> count | String | 聚合的订单匹配数量  
> source | String | 订单来源  
`0`：普通订单  
`1`：流动性增强计划订单  
> seqId | Integer | 推送的序列号  
聚合功能说明：  
1\. 系统将根据每个taker订单的不同成交价格，不同成交来源推送消息，并使用count字段表示聚合的订单匹配数量。  
2\. tradeId是聚合的多笔交易中最新一笔交易的 ID。  
3\. 当count = 1时，表示taker订单部分或完全成交时仅匹配了一个maker订单。  
4\. 当count > 1时，表示taker订单以相同价格匹配了多个maker订单。例如，如果tradeId = 123，且count = 3，表示该消息聚合了tradeId = 123, 122, 121的成交。maker侧有多笔价格相同的订单被成交。  
5\. 用户可以使用此数据与“全部交易”频道的数据进行对比。  
6\. 深度及聚合交易数据仍按顺序发布。  
同时发生的不同交易推送数据的`seqId`可能相同。 

### WS / 全部交易频道 

获取最近的成交数据，有成交数据就推送，每次推送仅包含一条成交数据。

#### URL Path

/ws/v5/business

> 请求示例
    
    
    {
      "id": "1512",
        "op": "subscribe",
        "args": [{
            "channel": "trades-all",
            "instId": "BTC-USDT"
        }]
    }
    
    
    
    import asyncio
    
    from okx.websocket.WsPublicAsync import WsPublicAsync
    
    
    def callbackFunc(message):
        print(message)
    
    
    async def main():
        ws = WsPublicAsync(url="wss://wspap.okx.com:8443/ws/v5/business")
        await ws.start()
        args = [
            {
              "channel": "trades-all",
              "instId": "BTC-USDT"
            }
        ]
    
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
`trades-all`  
> instId | String | 是 | 产品ID  
  
> 成功返回示例
    
    
    {
      "id": "1512",
        "event": "subscribe",
        "arg": {
            "channel": "trades-all",
            "instId": "BTC-USDT"
        },
      "connId": "a4d3ae55"
    }
    

> 失败返回示例
    
    
    {
      "id": "1512",
        "event": "error",
        "code": "60012",
        "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{ \"channel\" : \"trades-all\", \"instId\" : \"BTC-USD-191227\"}]}",
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
> instId | String | 是 | 产品ID  
code | String | 否 | 错误码  
msg | String | 否 | 错误消息  
connId | String | 是 | WebSocket连接ID  
  
> 推送示例
    
    
    {
      "arg": {
        "channel": "trades-all",
        "instId": "BTC-USDT"
      },
      "data": [
        {
          "instId": "BTC-USDT",
          "tradeId": "130639474",
          "px": "42219.9",
          "sz": "0.12060306",
          "side": "buy",
          "source": "0",
          "ts": "1630048897897"
        }
      ]
    }
    

#### 推送数据参数

**参数名** | **类型** | **描述**  
---|---|---  
arg | Array of objects | 订阅成功的频道  
> channel | String | 频道名  
> instId | String | 产品ID  
data | Array of objects | 订阅的数据  
> instId | String | 产品ID，如 `BTC-USDT`  
> tradeId | String | 成交ID  
> px | String | 成交价格  
> sz | String | 成交数量  
对于币币交易，成交数量的单位为交易货币  
对于交割、永续以及期权，单位为张。  
> side | String | 成交方向  
`buy`  
`sell`  
> source | String | 订单来源  
`0`：普通订单   
`1`：流动性增强计划订单  
> ts | String | 成交时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
  
### WS / 深度频道 

获取深度数据。在提前挂单阶段，best ask的价格有机会低于best bid。`books`是400档频道，`books5`是5档频道， `bbo-tbt`是先1档后实时推送的频道，`books-l2-tbt`是先400档后实时推送的频道，`books50-l2-tbt`是先50档后实时推的频道；

  * `books` 首次推400档快照数据，以后增量推送，每100毫秒推送一次变化的数据  

  * `books-elp` 仅推送ELP订单，首次推400档快照数据，以后增量推送，每100毫秒推送一次变化的数据  

  * `books5` 首次推5档快照数据，以后定量推送，每100毫秒当5档快照数据有变化推送一次5档数据  

  * `bbo-tbt` 首次推1档快照数据，以后定量推送，每10毫秒当1档快照数据有变化推送一次1档数据  

  * `books-l2-tbt` 首次推400档快照数据，以后增量推送，每10毫秒推送一次变化的数据  

  * `books50-l2-tbt` 首次推50档快照数据，以后增量推送，每10毫秒推送一次变化的数据
  * 单个连接、交易产品维度，深度频道的推送顺序固定为：bbo-tbt -> books-l2-tbt -> books50-l2-tbt -> books -> books-elp -> books5。
  * 在相同连接下，用户将无法为相同交易产品同时订阅 `books-l2-tbt` 以及 `books50-l2-tbt/books`频道 
    * 更多细节，请参阅更新日志 [2024-07-17](/docs-v5/log_zh/#2024-07-17)

books-l2-tbt400档深度频道，只允许交易手续费等级VIP4及以上的API用户订阅，其他用户接入将收到错误码64003。  
books50-l2-tbt50档深度频道，只允许交易手续费等级VIP4及以上的API用户订阅，其他用户接入将收到错误码64003。  

身份认证参考[登录](/docs-v5/zh/#overview-websocket-login)功能 

#### 服务地址

/ws/v5/public

> 请求示例
    
    
    {
        "id": "1512",
        "op": "subscribe",
        "args": [{
            "channel": "books",
            "instId": "BTC-USDT"
        }]
    }
    
    
    
    import asyncio
    
    from okx.websocket.WsPublicAsync import WsPublicAsync
    
    
    def callbackFunc(message):
        print(message)
    
    
    async def main():
        ws = WsPublicAsync(url="wss://wspap.okx.com:8443/ws/v5/public")
        await ws.start()
        args = [
          {
            "channel": "books",
            "instId": "BTC-USDT"
          }
        ]
    
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
`books`  
`books5`  
`bbo-tbt`  
`books-l2-tbt`  
`books50-l2-tbt`  
> instId | String | 是 | 产品ID  
  
> 返回示例
    
    
    {
        "id": "1512",
        "event": "subscribe",
        "arg": {
            "channel": "books",
            "instId": "BTC-USDT"
        },
        "connId": "a4d3ae55"
    }
    

> 失败示例
    
    
    {
        "id": "1512",
        "event": "error",
        "code": "60012",
        "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{ \"channel\" : \"books\", \"instId\" : \"BTC-USD-191227\"}]}",
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
> instId | String | 是 | 产品ID  
msg | String | 否 | 错误消息  
code | String | 否 | 错误码  
connId | String | 是 | WebSocket连接ID  
  
> 推送示例 ：全量
    
    
    {
        "arg": {
            "channel": "books",
            "instId": "BTC-USDT"
        },
        "action": "snapshot",
        "data": [{
            "asks": [
                ["8476.98", "415", "0", "13"],
                ["8477", "7", "0", "2"],
                ["8477.34", "85", "0", "1"],
                ["8477.56", "1", "0", "1"],
                ["8505.84", "8", "0", "1"],
                ["8506.37", "85", "0", "1"],
                ["8506.49", "2", "0", "1"],
                ["8506.96", "100", "0", "2"]
            ],
            "bids": [
                ["8476.97", "256", "0", "12"],
                ["8475.55", "101", "0", "1"],
                ["8475.54", "100", "0", "1"],
                ["8475.3", "1", "0", "1"],
                ["8447.32", "6", "0", "1"],
                ["8447.02", "246", "0", "1"],
                ["8446.83", "24", "0", "1"],
                ["8446", "95", "0", "3"]
            ],
            "ts": "1597026383085",
            "checksum": 0,
            "prevSeqId": -1,
            "seqId": 123456
        }]
    }
    

> 推送示例：增量
    
    
    {
        "arg": {
            "channel": "books",
            "instId": "BTC-USDT"
        },
        "action": "update",
        "data": [{
            "asks": [
                ["8476.98", "415", "0", "13"],
                ["8477", "7", "0", "2"],
                ["8477.34", "85", "0", "1"],
                ["8477.56", "1", "0", "1"],
                ["8505.84", "8", "0", "1"],
                ["8506.37", "85", "0", "1"],
                ["8506.49", "2", "0", "1"],
                ["8506.96", "100", "0", "2"]
            ],
            "bids": [
                ["8476.97", "256", "0", "12"],
                ["8475.55", "101", "0", "1"],
                ["8475.54", "100", "0", "1"],
                ["8475.3", "1", "0", "1"],
                ["8447.32", "6", "0", "1"],
                ["8447.02", "246", "0", "1"],
                ["8446.83", "24", "0", "1"],
                ["8446", "95", "0", "3"]
            ],
            "ts": "1597026383085",
            "checksum": 0,
            "prevSeqId": 123456,
            "seqId": 123457
        }]
    }
    

#### 推送数据参数

**参数名** | **类型** | **描述**  
---|---|---  
arg | Object | 订阅成功的频道  
> channel | String | 频道名  
> instId | String | 产品ID  
action | String | 推送数据动作，增量推送数据还是全量推送数据  
`snapshot`：全量   
`update`：增量  
data | Array of objects | 订阅的数据  
> asks | Array of Arrays | 卖方深度  
> bids | Array of Arrays | 买方深度  
> ts | String | 数据更新时间戳，Unix时间戳的毫秒数格式，如 `1597026383085`   
例外： 对于`bbo-tbt` 频道，`ts` 为撮合引擎触发时的时间戳  
> checksum | Integer | ~~检验和~~ （已弃用）。该字段仍会在 `books`、`books-l2-tbt`、`books50-l2-tbt` 推送中保留，但其值固定为 `0`，不应再用于数据完整性校验。请改用 `seqId/prevSeqId` 校验数据的连续性和准确性。  
> prevSeqId | Integer | 上一个推送的序列号。仅适用 `books`，`books-l2-tbt`，`books50-l2-tbt`  
> seqId | Integer | 推送的序列号 （下方注解）  
asks和bids值数组举例说明： ["411.8", "10", "0", "4"]  
\- 411.8为深度价格  
\- 10为此价格的数量 （合约交易为张数，现货/币币杠杆为交易币的数量  
\- 0该字段已弃用(始终为0)  
\- 4为此价格的订单数量  如果需要订阅多个50或400档频道，建议通过多个链接进行订阅，每个链接低于30条频道。  集合竞价期间，深度数据大约每秒更新一次  `books/books5/bbo-tbt/books-l2-tbt/books50-l2-tbt`不包含ELP订单  
`books-elp`仅返回 ELP 订单，包含有效部分及无效部分（无效部分指 ELP 买单价格高于非 ELP 订单最佳买单价；或 ELP 卖单价格低于非 ELP 订单最佳卖单价）。用户需根据非 ELP 订单的最佳买/卖价区分有效部分和无效部分。 

#### 序列号

`seqId`是交易所行情的一个序号。如果用户通过多个websocket连接同一频道，收到的序列号会是相同的。每个`instId`对应一套。用户可以使用在增量推送频道的`prevSeqId`和`seqId`来构建消息序列。这将允许用户检测数据包丢失和消息的排序。正常场景下`seqId`的值大于`prevSeqId`。新消息中的`prevSeqId`与上一条消息的`seqId`匹配。最小序列号值为0，除了快照消息的`prevSeqId`为-1。  

异常情况：  
1\. 如果一段时间内（约 60 秒）没有深度更新，对于定量推送频道，OKX 会推送最近的一条更新，对于增量推送频道，OKX将发一条消息`'asks': [], 'bids': []`以通知用户连接是正常的。推送的`seqId`跟上一条信息的一样，`prevSeqId`等于`seqId`。 2\. 序列号可能由于维护而重置，在这种情况下，用户将收到一条`seqId`小于`prevSeqId`的增量消息。随后的消息将遵循常规的排序规则。

##### 示例

  1. 快照推送：`prevSeqId = -1`，`seqId = 10`
  2. 增量推送1（正常更新）：`prevSeqId = 10`，`seqId = 15`
  3. 增量推送2（无更新）：`prevSeqId = 15`，`seqId = 15`
  4. 增量推送3（序列重置）：`prevSeqId = 15`，`seqId = 3`
  5. 增量推送4（正常更新）：`prevSeqId = 3`，`seqId = 5`

> bbo-tbt 频道推送示例
    
    
    {
      "arg": {
        "channel": "bbo-tbt",
        "instId": "BCH-USDT-SWAP"
      },
      "data": [
        {
          "asks": [
            [
              "111.06","55154","0","2"
            ]
          ],
          "bids": [
            [
              "111.05","57745","0","2"
            ]
          ],
          "ts": "1670324386802",
          "seqId": 363996337
        }
      ]
    }
    

> books5 频道推送示例
    
    
    {
      "arg": {
        "channel": "books5",
        "instId": "BCH-USDT-SWAP"
      },
      "data": [
        {
          "asks": [
            ["111.06","55154","0","2"],
            ["111.07","53276","0","2"],
            ["111.08","72435","0","2"],
            ["111.09","70312","0","2"],
            ["111.1","67272","0","2"]],
          "bids": [
            ["111.05","57745","0","2"],
            ["111.04","57109","0","2"],
            ["111.03","69563","0","2"],
            ["111.02","71248","0","2"],
            ["111.01","65090","0","2"]],
          "instId": "BCH-USDT-SWAP",
          "ts": "1670324386802",
          "seqId": 363996337
        }
      ]
    }
    

### WS / 期权公共成交频道 

获取最近的期权成交数据，有成交数据就推送，每次推送仅包含一条成交数据。

#### URL Path

/ws/v5/public

> 请求示例
    
    
    {
        "id": "1512",
        "op": "subscribe",
        "args": [{
            "channel": "option-trades",
            "instType": "OPTION",
            "instFamily": "BTC-USD"
        }]
    }
    
    
    
    import asyncio
    
    from okx.websocket.WsPublicAsync import WsPublicAsync
    
    
    def callbackFunc(message):
        print(message)
    
    
    async def main():
        ws = WsPublicAsync(url="wss://wspap.okx.com:8443/ws/v5/public")
        await ws.start()
        args = [{
            "channel": "option-trades",
            "instType": "OPTION",
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
`option-trades`  
> instType | String | 是 | 产品类型，`OPTION`：期权  
> instId | String | 可选 | 产品ID，如 BTC-USD-221230-4000-C，`instId` 和 `instFamily` 必须传一个，若传两个，以 `instId` 为主  
> instFamily | String | 可选 | 交易品种，如 BTC-USD  
  
> 成功返回示例
    
    
    {
        "id": "1512",
        "event": "subscribe",
        "arg": {
            "channel": "option-trades",
            "instType": "OPTION",
            "instFamily": "BTC-USD"
        },
        "connId": "a4d3ae55"
    }
    
    

> 失败返回示例
    
    
    {
        "id": "1512",
        "event": "error",
        "code": "60012",
        "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{ \"channel\" : \"option-trades\"}]}",
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
code | String | 否 | 错误码  
msg | String | 否 | 错误消息  
connId | String | 是 | WebSocket连接ID  
  
> 推送示例
    
    
    {
        "arg": {
            "channel": "option-trades",
            "instType": "OPTION",
            "instFamily": "BTC-USD"
        },
        "data": [
            {
                "fillVol": "0.5066007836914062",
                "fwdPx": "16469.69928595038",
                "idxPx": "16537.2",
                "instFamily": "BTC-USD",
                "instId": "BTC-USD-230224-18000-C",
                "markPx": "0.04690107010619562",
                "optType": "C",
                "px": "0.045",
                "side": "sell",
                "sz": "2",
                "tradeId": "38",
                "ts": "1672286551080"
            }
        ]
    }
    

#### 推送数据参数

参数名 | 类型 | 描述  
---|---|---  
arg | Object | 订阅成功的频道  
> channel | String | 频道名  
data | Array of objects | 订阅的数据  
> instId | String | 产品ID  
> instFamily | String | 交易品种  
> tradeId | String | 成交ID  
> px | String | 成交价格  
> sz | String | 成交数量，单位为张。  
> side | String | 成交方向   
`buy`：买   
`sell`：卖  
> optType | String | 期权类型，C：看涨期权 P：看跌期权 ，仅适用于期权  
> fillVol | String | 成交时的隐含波动率（对应成交价格）  
> fwdPx | String | 成交时的远期价格  
> idxPx | String | 成交时的指数价格  
> markPx | String | 成交时的标记价格  
> ts | String | 成交时间，Unix时间戳的毫秒数格式， 如`1597026383085`  
该频道订阅成功后的首条数据可能为最近一笔成交的缓存数据，请忽略。 

### WS / 集合竞价信息频道 

获取集合竞价相关信息

#### URL Path

/ws/v5/public

> 请求示例
    
    
    {
        "id": "1512",
        "op": "subscribe",
        "args": [{
            "channel": "call-auction-details",
            "instId": "ONDO-USDC"
        }]
    }
    
    
    
    
    import asyncio
    
    from okx.websocket.WsPublicAsync import WsPublicAsync
    
    
    def callbackFunc(message):
        print(message)
    
    
    async def main():
        ws = WsPublicAsync(url="wss://wspap.okx.com:8443/ws/v5/public")
        await ws.start()
        args = [{
            "channel": "call-auction-details",
            "instId": "ONDO-USDC"
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
`call-auction-details`  
> instId | String | 是 | 产品ID  
  
> 成功返回示例
    
    
    {
      "id": "1512",
      "event": "subscribe",
      "arg": {
          "channel": "call-auction-details",
          "instId": "ONDO-USDC"
        },
      "connId": "a4d3ae55"
    }
    
    

> 失败返回示例
    
    
    {
      "id": "1512",
      "event": "error",
      "code": "60012",
      "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{ \"channel\" : \"call-auction-details\", \"instId\" : \"BTC-USD-191227\"}]}",
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
> instId | String | 是 | 产品ID  
code | String | 否 | 错误码  
msg | String | 否 | 错误消息  
connId | String | 是 | WebSocket连接ID  
  
> 推送示例
    
    
    {
      "arg": {
        "channel": "call-auction-details",
        "instId": "ONDO-USDC"
      },
      "data": [
            {
                "instId": "ONDO-USDC",
                "unmatchedSz": "9988764",
                "eqPx": "0.6",
                "matchedSz": "44978",
                "state": "continuous_trading",
                "auctionEndTime": "1726542000000",
                "ts": "1726542000007"
            }
      ]
    }
    
    

#### 推送数据参数

参数名 | 类型 | 描述  
---|---|---  
arg | Object | 订阅成功的频道  
> channel | String | 频道名  
> instId | String | 产品ID  
data | Array of objects | 订阅的数据  
> instId | String | 产品ID  
> eqPx | String | 均衡价格  
> matchedSz | String | 买卖双边的匹配数量，单位为交易货币  
> unmatchedSz | String | 未匹配数量  
> auctionEndTime | String | 集合竞价结束时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
> state | String | 交易状态  
`call_auction`：集合竞价  
`continuous_trading`：连续交易  
> ts | String | 数据产生时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
在集合竞价期间，用户可以获取均衡价格、匹配数量、未匹配数量和集合竞价结束时间的更新。数据大约每秒更新一次。当集合竞价结束时，该频道将推送最后一条消息，返回实际开盘价、匹配数量和未匹配数量，交易状态state为`continuous_trading`。