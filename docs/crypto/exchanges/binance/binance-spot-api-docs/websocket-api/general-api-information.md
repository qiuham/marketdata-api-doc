---
exchange: binance
source_url: https://developers.binance.com/docs/binance-spot-api-docs/websocket-api/general-api-information
api_type: WebSocket
updated_at: 2026-05-27 18:55:07.598371
---

# Market data requests

### Order book[​](/docs/binance-spot-api-docs/websocket-api/market-data-requests#order-book "Direct link to Order book")  
      
    
    {  
        "id": "51e2affb-0aba-4821-ba75-f2625006eb43",  
        "method": "depth",  
        "params": {  
            "symbol": "BNBBTC",  
            "limit": 5  
        }  
    }  
    

Get current order book.

Note that this request returns limited market depth.

If you need to continuously monitor order book updates, please consider using WebSocket Streams:

  * [`<symbol>@depth<levels>`](/docs/binance-spot-api-docs/web-socket-streams#partial-book-depth-streams)
  * [`<symbol>@depth`](/docs/binance-spot-api-docs/web-socket-streams#diff-depth-stream)



You can use `depth` request together with `<symbol>@depth` streams to [maintain a local order book](/docs/binance-spot-api-docs/web-socket-streams#how-to-manage-a-local-order-book-correctly).

**Weight:** Adjusted based on the limit:

Limit| Weight  
---|---  
1–100| 5  
101–500| 25  
501–1000| 50  
1001–5000| 250  
  
**Parameters:**

Name| Type| Mandatory| Description  
---|---|---|---  
`symbol`| STRING| YES|   
`limit`| INT| NO| Default: 100; Maximum: 5000  
`symbolStatus`| ENUM| NO| Filters for symbols that have this `tradingStatus`.  
A status mismatch returns error `-1220 SYMBOL_DOES_NOT_MATCH_STATUS`  
Valid values: `TRADING`, `HALT`, `BREAK`  
  
**Data Source:** Memory

**Response:**
    
    
    {  
        "id": "51e2affb-0aba-4821-ba75-f2625006eb43",  
        "status": 200,  
        "result": {  
            "lastUpdateId": 2731179239,  
            // Bid levels are sorted from highest to lowest price.  
            "bids": [  
                [  
                    "0.01379900",     // Price  
                    "3.43200000"      // Quantity  
                ],  
                ["0.01379800", "3.24300000"],  
                ["0.01379700", "10.45500000"],  
                ["0.01379600", "3.82100000"],  
                ["0.01379500", "10.26200000"]  
            ],  
            // Ask levels are sorted from lowest to highest price.  
            "asks": [  
                ["0.01380000", "5.91700000"],  
                ["0.01380100", "6.01400000"],  
                ["0.01380200", "0.26800000"],  
                ["0.01380300", "0.33800000"],  
                ["0.01380400", "0.26800000"]  
            ]  
        },  
        "rateLimits": [  
            {  
                "rateLimitType": "REQUEST_WEIGHT",  
                "interval": "MINUTE",  
                "intervalNum": 1,  
                "limit": 6000,  
                "count": 2  
            }  
        ]  
    }  
    

### Recent trades[​](/docs/binance-spot-api-docs/websocket-api/market-data-requests#recent-trades "Direct link to Recent trades")
    
    
    {  
        "id": "409a20bd-253d-41db-a6dd-687862a5882f",  
        "method": "trades.recent",  
        "params": {  
            "symbol": "BNBBTC",  
            "limit": 1  
        }  
    }  
    

Get recent trades.

If you need access to real-time trading activity, please consider using WebSocket Streams:

  * [`<symbol>@trade`](/docs/binance-spot-api-docs/web-socket-streams#trade-streams)



**Weight:** 25

**Parameters:**

Name| Type| Mandatory| Description  
---|---|---|---  
`symbol`| STRING| YES|   
`limit`| INT| NO| Default: 500; Maximum: 1000  
  
**Data Source:** Memory

**Response:**
    
    
    {  
        "id": "409a20bd-253d-41db-a6dd-687862a5882f",  
        "status": 200,  
        "result": [  
            {  
                "id": 194686783,  
                "price": "0.01361000",  
                "qty": "0.01400000",  
                "quoteQty": "0.00019054",  
                "time": 1660009530807,  
                "isBuyerMaker": true,  
                "isBestMatch": true  
            }  
        ],  
        "rateLimits": [  
            {  
                "rateLimitType": "REQUEST_WEIGHT",  
                "interval": "MINUTE",  
                "intervalNum": 1,  
                "limit": 6000,  
                "count": 2  
            }  
        ]  
    }  
    

### Historical trades[​](/docs/binance-spot-api-docs/websocket-api/market-data-requests#historical-trades "Direct link to Historical trades")
    
    
    {  
        "id": "cffc9c7d-4efc-4ce0-b587-6b87448f052a",  
        "method": "trades.historical",  
        "params": {  
            "symbol": "BNBBTC",  
            "fromId": 0,  
            "limit": 1  
        }  
    }  
    

Get historical trades.

**Weight:** 25

**Parameters:**

Name| Type| Mandatory| Description  
---|---|---|---  
`symbol`| STRING| YES|   
`fromId`| INT| NO| Trade ID to begin at  
`limit`| INT| NO| Default: 500; Maximum: 1000  
  
Notes:

  * If `fromId` is not specified, the most recent trades are returned.



**Data Source:** Database

**Response:**
    
    
    {  
        "id": "cffc9c7d-4efc-4ce0-b587-6b87448f052a",  
        "status": 200,  
        "result": [  
            {  
                "id": 0,  
                "price": "0.00005000",  
                "qty": "40.00000000",  
                "quoteQty": "0.00200000",  
                "time": 1500004800376,  
                "isBuyerMaker": true,  
                "isBestMatch": true  
            }  
        ],  
        "rateLimits": [  
            {  
                "rateLimitType": "REQUEST_WEIGHT",  
                "interval": "MINUTE",  
                "intervalNum": 1,  
                "limit": 6000,  
                "count": 10  
            }  
        ]  
    }  
    

### Historical Block Trades[​](/docs/binance-spot-api-docs/websocket-api/market-data-requests#historical-block-trades "Direct link to Historical Block Trades")
    
    
    {  
        "id": "189da436-d4bd-48ca-9f95-9f613d621717",  
        "method": "blockTrades.historical",  
        "params": {  
            "symbol": "BNBBTC",  
            "fromId": 582,  
            "limit": 1  
        }  
    }  
    

Get block trades.

**Weight:** 25

**Parameters:**

Name| Type| Mandatory| Description  
---|---|---|---  
`symbol`| STRING| YES|   
`fromId`| LONG| YES| Block trade ID to fetch from  
`limit`| LONG| NO| Default: 500; Maximum: 1000  
  
**Data Source:** Database

**Response:**
    
    
    {  
        "id": "cffc9c7d-4efc-4ce0-b587-6b87448f052a",  
        "status": 200,  
        "result":  
        [  
            {  
                "id": 582,  
                "price": "0.052",  
                "qty": "5838",  
                "quoteQty": "303.576",  
                "time": 1772506983321,  
                "isBuyerMaker": true  
            }  
        ],  
        "rateLimits":  
        [  
            {  
                "rateLimitType": "REQUEST_WEIGHT",  
                "interval": "MINUTE",  
                "intervalNum": 1,  
                "limit": 6000,  
                "count": 10  
            }  
        ]  
    }  
    

### Aggregate trades[​](/docs/binance-spot-api-docs/websocket-api/market-data-requests#aggregate-trades "Direct link to Aggregate trades")
    
    
    {  
        "id": "189da436-d4bd-48ca-9f95-9f613d621717",  
        "method": "trades.aggregate",  
        "params": {  
            "symbol": "BNBBTC",  
            "fromId": 50000000,  
            "limit": 1  
        }  
    }  
    

Get aggregate trades.

An _aggregate trade_ (aggtrade) represents one or more individual trades. Trades that fill at the same time, from the same taker order, with the same price – those trades are collected into an aggregate trade with total quantity of the individual trades.

If you need access to real-time trading activity, please consider using WebSocket Streams:

  * [`<symbol>@aggTrade`](/docs/binance-spot-api-docs/web-socket-streams#aggregate-trade-streams)



If you need historical aggregate trade data, please consider using [data.binance.vision](https://github.com/binance/binance-public-data/#aggtrades).

**Weight:** 4

**Parameters:**

Name| Type| Mandatory| Description  
---|---|---|---  
`symbol`| STRING| YES|   
`fromId`| LONG| NO| Aggregate trade ID to begin at  
`startTime`| LONG| NO|   
`endTime`| LONG| NO|   
`limit`| LONG| NO| Default: 500; Maximum: 1000  
  
Notes:

  * If `fromId` is specified, return aggtrades with aggregate trade ID >= `fromId`.

Use `fromId` and `limit` to page through all aggtrades.

  * If `startTime` and/or `endTime` are specified, aggtrades are filtered by execution time (`T`).

`fromId` cannot be used together with `startTime` and `endTime`.

  * If no condition is specified, the most recent aggregate trades are returned.




**Data Source:** Database

**Response:**
    
    
    {  
        "id": "189da436-d4bd-48ca-9f95-9f613d621717",  
        "status": 200,  
        "result": [  
            {  
                "a": 50000000,          // Aggregate trade ID  
                "p": "0.00274100",      // Price  
                "q": "57.19000000",     // Quantity  
                "f": 59120167,          // First trade ID  
                "l": 59120170,          // Last trade ID  
                "T": 1565877971222,     // Timestamp  
                "m": true,              // Was the buyer the maker?  
                "M": true               // Was the trade the best price match?  
            }  
        ],  
        "rateLimits": [  
            {  
                "rateLimitType": "REQUEST_WEIGHT",  
                "interval": "MINUTE",  
                "intervalNum": 1,  
                "limit": 6000,  
                "count": 2  
            }  
        ]  
    }  
    

### Klines[​](/docs/binance-spot-api-docs/websocket-api/market-data-requests#klines "Direct link to Klines")
    
    
    {  
        "id": "1dbbeb56-8eea-466a-8f6e-86bdcfa2fc0b",  
        "method": "klines",  
        "params": {  
            "symbol": "BNBBTC",  
            "interval": "1h",  
            "startTime": 1655969280000,  
            "limit": 1  
        }  
    }  
    

Get klines (candlestick bars).

Klines are uniquely identified by their open & close time.

If you need access to real-time kline updates, please consider using WebSocket Streams:

  * [`<symbol>@kline_<interval>`](/docs/binance-spot-api-docs/web-socket-streams#klinecandlestick-streams-for-utc)



If you need historical kline data, please consider using [data.binance.vision](https://github.com/binance/binance-public-data/#klines).

**Weight:** 2

**Parameters:**

Name| Type| Mandatory| Description  
---|---|---|---  
`symbol`| STRING| YES|   
`interval`| ENUM| YES|   
`startTime`| LONG| NO|   
`endTime`| LONG| NO|   
`timeZone`| STRING| NO| Default: 0 (UTC)  
`limit`| INT| NO| Default: 500; Maximum: 1000  
  
Supported kline intervals (case-sensitive):

Interval| `interval` value  
---|---  
seconds| `1s`  
minutes| `1m`, `3m`, `5m`, `15m`, `30m`  
hours| `1h`, `2h`, `4h`, `6h`, `8h`, `12h`  
days| `1d`, `3d`  
weeks| `1w`  
months| `1M`  
  
Notes:

  * If `startTime`, `endTime` are not specified, the most recent klines are returned.
  * Supported values for `timeZone`: 
    * Hours and minutes (e.g. `-1:00`, `05:45`)
    * Only hours (e.g. `0`, `8`, `4`)
    * Accepted range is strictly [-12:00 to +14:00] inclusive
  * If `timeZone` provided, kline intervals are interpreted in that timezone instead of UTC.
  * Note that `startTime` and `endTime` are always interpreted in UTC, regardless of timeZone.



**Data Source:** Database

**Response:**
    
    
    {  
        "id": "1dbbeb56-8eea-466a-8f6e-86bdcfa2fc0b",  
        "status": 200,  
        "result": [  
            [  
                1655971200000,       // Kline open time  
                "0.01086000",        // Open price  
                "0.01086600",        // High price  
                "0.01083600",        // Low price  
                "0.01083800",        // Close price  
                "2290.53800000",     // Volume  
                1655974799999,       // Kline close time  
                "24.85074442",       // Quote asset volume  
                2283,                // Number of trades  
                "1171.64000000",     // Taker buy base asset volume  
                "12.71225884",       // Taker buy quote asset volume  
                "0"                  // Unused field, ignore  
            ]  
        ],  
        "rateLimits": [  
            {  
                "rateLimitType": "REQUEST_WEIGHT",  
                "interval": "MINUTE",  
                "intervalNum": 1,  
                "limit": 6000,  
                "count": 2  
            }  
        ]  
    }  
    

### UI Klines[​](/docs/binance-spot-api-docs/websocket-api/market-data-requests#ui-klines "Direct link to UI Klines")
    
    
    {  
        "id": "b137468a-fb20-4c06-bd6b-625148eec958",  
        "method": "uiKlines",  
        "params": {  
            "symbol": "BNBBTC",  
            "interval": "1h",  
            "startTime": 1655969280000,  
            "limit": 1  
        }  
    }  
    

Get klines (candlestick bars) optimized for presentation.

This request is similar to [`klines`](/docs/binance-spot-api-docs/websocket-api/market-data-requests#klines), having the same parameters and response. `uiKlines` return modified kline data, optimized for presentation of candlestick charts.

**Weight:** 2

**Parameters:**

Name| Type| Mandatory| Description  
---|---|---|---  
`symbol`| STRING| YES|   
`interval`| ENUM| YES| See [`klines`](/docs/binance-spot-api-docs/websocket-api/market-data-requests#kline-intervals)  
`startTime`| LONG| NO|   
`endTime`| LONG| NO|   
`timeZone`| STRING| NO| Default: 0 (UTC)  
`limit`| INT| NO| Default: 500; Maximum: 1000  
  
Notes:

  * If `startTime`, `endTime` are not specified, the most recent klines are returned.
  * Supported values for `timeZone`: 
    * Hours and minutes (e.g. `-1:00`, `05:45`)
    * Only hours (e.g. `0`, `8`, `4`)
    * Accepted range is strictly [-12:00 to +14:00] inclusive
  * If `timeZone` provided, kline intervals are interpreted in that timezone instead of UTC.
  * Note that `startTime` and `endTime` are always interpreted in UTC, regardless of timeZone.



**Data Source:** Database

**Response:**
    
    
    {  
        "id": "b137468a-fb20-4c06-bd6b-625148eec958",  
        "status": 200,  
        "result": [  
            [  
                1655971200000,       // Kline open time  
                "0.01086000",        // Open price  
                "0.01086600",        // High price  
                "0.01083600",        // Low price  
                "0.01083800",        // Close price  
                "2290.53800000",     // Volume  
                1655974799999,       // Kline close time  
                "24.85074442",       // Quote asset volume  
                2283,                // Number of trades  
                "1171.64000000",     // Taker buy base asset volume  
                "12.71225884",       // Taker buy quote asset volume  
                "0"                  // Unused field, ignore  
            ]  
        ],  
        "rateLimits": [  
            {  
                "rateLimitType": "REQUEST_WEIGHT",  
                "interval": "MINUTE",  
                "intervalNum": 1,  
                "limit": 6000,  
                "count": 2  
            }  
        ]  
    }  
    

### Current average price[​](/docs/binance-spot-api-docs/websocket-api/market-data-requests#current-average-price "Direct link to Current average price")
    
    
    {  
        "id": "ddbfb65f-9ebf-42ec-8240-8f0f91de0867",  
        "method": "avgPrice",  
        "params": {  
            "symbol": "BNBBTC"  
        }  
    }  
    

Get current average price for a symbol.

**Weight:** 2

**Parameters:**

Name| Type| Mandatory| Description  
---|---|---|---  
`symbol`| STRING| YES|   
  
**Data Source:** Memory

**Response:**
    
    
    {  
        "id": "ddbfb65f-9ebf-42ec-8240-8f0f91de0867",  
        "status": 200,  
        "result": {  
            "mins": 5,                     // Average price interval (in minutes)  
            "price": "9.35751834",         // Average price  
            "closeTime": 1694061154503     // Last trade time  
        },  
        "rateLimits": [  
            {  
                "rateLimitType": "REQUEST_WEIGHT",  
                "interval": "MINUTE",  
                "intervalNum": 1,  
                "limit": 6000,  
                "count": 2  
            }  
        ]  
    }  
    

### 24hr ticker price change statistics[​](/docs/binance-spot-api-docs/websocket-api/market-data-requests#24hr-ticker-price-change-statistics "Direct link to 24hr ticker price change statistics")
    
    
    {  
        "id": "93fb61ef-89f8-4d6e-b022-4f035a3fadad",  
        "method": "ticker.24hr",  
        "params": {  
            "symbol": "BNBBTC"  
        }  
    }  
    

Get 24-hour rolling window price change statistics.

If you need to continuously monitor trading statistics, please consider using WebSocket Streams:

  * [`<symbol>@ticker`](/docs/binance-spot-api-docs/web-socket-streams#individual-symbol-ticker-streams)
  * [`<symbol>@miniTicker`](/docs/binance-spot-api-docs/web-socket-streams#individual-symbol-mini-ticker-stream) or [`!miniTicker@arr`](/docs/binance-spot-api-docs/web-socket-streams#all-market-mini-tickers-stream)



If you need different window sizes, use the [`ticker`](/docs/binance-spot-api-docs/websocket-api/market-data-requests#rolling-window-price-change-statistics) request.

**Weight:** Adjusted based on the number of requested symbols:

Symbols| Weight  
---|---  
1–20| 2  
21–100| 40  
101 or more| 80  
all symbols| 80  
  
**Parameters:**

Name | Type | Mandatory | Description  
---|---|---|---  
`symbol` | STRING | NO | Query ticker for a single symbol  
`symbols` | ARRAY of STRING | Query ticker for multiple symbols  
`type` | ENUM | NO | Ticker type: `FULL` (default) or `MINI`  
symbolStatus | ENUM | NO | Filters for symbols that have this `tradingStatus`.  
For a single symbol, a status mismatch returns error `-1220 SYMBOL_DOES_NOT_MATCH_STATUS`.  
For multiple or all symbols, non-matching ones are simply excluded from the response.  
Valid values: `TRADING`, `HALT`, `BREAK`  
  
Notes:

  * `symbol` and `symbols` cannot be used together.

  * If no symbol is specified, returns information about all symbols currently trading on the exchange.




**Data Source:** Memory

**Response:**

`FULL` type, for a single symbol:
    
    
    {  
        "id": "93fb61ef-89f8-4d6e-b022-4f035a3fadad",  
        "status": 200,  
        "result": {  
            "symbol": "BNBBTC",  
            "priceChange": "0.00013900",  
            "priceChangePercent": "1.020",  
            "weightedAvgPrice": "0.01382453",  
            "prevClosePrice": "0.01362800",  
            "lastPrice": "0.01376700",  
            "lastQty": "1.78800000",  
            "bidPrice": "0.01376700",  
            "bidQty": "4.64600000",  
            "askPrice": "0.01376800",  
            "askQty": "14.31400000",  
            "openPrice": "0.01362800",  
            "highPrice": "0.01414900",  
            "lowPrice": "0.01346600",  
            "volume": "69412.40500000",  
            "quoteVolume": "959.59411487",  
            "openTime": 1660014164909,  
            "closeTime": 1660100564909,  
            "firstId": 194696115,     // First trade ID  
            "lastId": 194968287,      // Last trade ID  
            "count": 272173           // Number of trades  
        },  
        "rateLimits": [  
            {  
                "rateLimitType": "REQUEST_WEIGHT",  
                "interval": "MINUTE",  
                "intervalNum": 1,  
                "limit": 6000,  
                "count": 2  
            }  
        ]  
    }  
    

`MINI` type, for a single symbol:
    
    
    {  
        "id": "9fa2a91b-3fca-4ed7-a9ad-58e3b67483de",  
        "status": 200,  
        "result": {  
            "symbol": "BNBBTC",  
            "openPrice": "0.01362800",  
            "highPrice": "0.01414900",  
            "lowPrice": "0.01346600",  
            "lastPrice": "0.01376700",  
            "volume": "69412.40500000",  
            "quoteVolume": "959.59411487",  
            "openTime": 1660014164909,  
            "closeTime": 1660100564909,  
            "firstId": 194696115,     // First trade ID  
            "lastId": 194968287,      // Last trade ID  
            "count": 272173           // Number of trades  
        },  
        "rateLimits": [  
            {  
                "rateLimitType": "REQUEST_WEIGHT",  
                "interval": "MINUTE",  
                "intervalNum": 1,  
                "limit": 6000,  
                "count": 2  
            }  
        ]  
    }  
    

If more than one symbol is requested, response returns an array:
    
    
    {  
        "id": "901be0d9-fd3b-45e4-acd6-10c580d03430",  
        "status": 200,  
        "result": [  
            {  
                "symbol": "BNBBTC",  
                "priceChange": "0.00016500",  
                "priceChangePercent": "1.213",  
                "weightedAvgPrice": "0.01382508",  
                "prevClosePrice": "0.01360800",  
                "lastPrice": "0.01377200",  
                "lastQty": "1.01400000",  
                "bidPrice": "0.01377100",  
                "bidQty": "7.55700000",  
                "askPrice": "0.01377200",  
                "askQty": "4.37900000",  
                "openPrice": "0.01360700",  
                "highPrice": "0.01414900",  
                "lowPrice": "0.01346600",  
                "volume": "69376.27900000",  
                "quoteVolume": "959.13277091",  
                "openTime": 1660014615517,  
                "closeTime": 1660101015517,  
                "firstId": 194697254,  
                "lastId": 194969483,  
                "count": 272230  
            },  
            {  
                "symbol": "BTCUSDT",  
                "priceChange": "-938.06000000",  
                "priceChangePercent": "-3.938",  
                "weightedAvgPrice": "23265.34432003",  
                "prevClosePrice": "23819.17000000",  
                "lastPrice": "22880.91000000",  
                "lastQty": "0.00536000",  
                "bidPrice": "22880.40000000",  
                "bidQty": "0.00424000",  
                "askPrice": "22880.91000000",  
                "askQty": "0.04276000",  
                "openPrice": "23818.97000000",  
                "highPrice": "23933.25000000",  
                "lowPrice": "22664.69000000",  
                "volume": "153508.37606000",  
                "quoteVolume": "3571425225.04441220",  
                "openTime": 1660014615977,  
                "closeTime": 1660101015977,  
                "firstId": 1592019902,  
                "lastId": 1597301762,  
                "count": 5281861  
            }  
        ],  
        "rateLimits": [  
            {  
                "rateLimitType": "REQUEST_WEIGHT",  
                "interval": "MINUTE",  
                "intervalNum": 1,  
                "limit": 6000,  
                "count": 2  
            }  
        ]  
    }  
    

### Trading Day Ticker[​](/docs/binance-spot-api-docs/websocket-api/market-data-requests#trading-day-ticker "Direct link to Trading Day Ticker")
    
    
    {  
        "id": "f4b3b507-c8f2-442a-81a6-b2f12daa030f",  
        "method": "ticker.tradingDay",  
        "params": {  
            "symbols": ["BNBBTC", "BTCUSDT"],  
            "timeZone": "00:00"  
        }  
    }  
    

Price change statistics for a trading day.

**Weight:**

4 for each requested `symbol`.   
  
The weight for this request will cap at 200 once the number of `symbols` in the request is more than 50.

**Parameters:**

Name | Type | Mandatory | Description  
---|---|---|---  
`symbol` | STRING | YES | Query ticker of a single symbol  
`symbols` | ARRAY of STRING | Query ticker for multiple symbols  
`timeZone` | STRING | NO | Default: 0 (UTC)  
`type` | ENUM | NO | Supported values: `FULL` or `MINI`.   
If none provided, the default is `FULL`  
symbolStatus | ENUM | NO | Filters for symbols that have this `tradingStatus`.  
For a single symbol, a status mismatch returns error `-1220 SYMBOL_DOES_NOT_MATCH_STATUS`.   
For multiple symbols, non-matching ones are simply excluded from the response.  
Valid values: `TRADING`, `HALT`, `BREAK`  
  
**Notes:**

  * Supported values for `timeZone`: 
    * Hours and minutes (e.g. `-1:00`, `05:45`)
    * Only hours (e.g. `0`, `8`, `4`)



**Data Source:** Database

**Response: - FULL**

With `symbol`:
    
    
    {  
        "id": "f4b3b507-c8f2-442a-81a6-b2f12daa030f",  
        "status": 200,  
        "result": {  
            "symbol": "BTCUSDT",  
            "priceChange": "-83.13000000",            // Absolute price change  
            "priceChangePercent": "-0.317",           // Relative price change in percent  
            "weightedAvgPrice": "26234.58803036",     // quoteVolume / volume  
            "openPrice": "26304.80000000",  
            "highPrice": "26397.46000000",  
            "lowPrice": "26088.34000000",  
            "lastPrice": "26221.67000000",  
            "volume": "18495.35066000",               // Volume in base asset  
            "quoteVolume": "485217905.04210480",  
            "openTime": 1695686400000,  
            "closeTime": 1695772799999,  
            "firstId": 3220151555,  
            "lastId": 3220849281,  
            "count": 697727  
        },  
        "rateLimits": [  
            {  
                "rateLimitType": "REQUEST_WEIGHT",  
                "interval": "MINUTE",  
                "intervalNum": 1,  
                "limit": 6000,  
                "count": 4  
            }  
        ]  
    }  
    

With `symbols`:
    
    
    {  
        "id": "f4b3b507-c8f2-442a-81a6-b2f12daa030f",  
        "status": 200,  
        "result": [  
            {  
                "symbol": "BTCUSDT",  
                "priceChange": "-83.13000000",  
                "priceChangePercent": "-0.317",  
                "weightedAvgPrice": "26234.58803036",  
                "openPrice": "26304.80000000",  
                "highPrice": "26397.46000000",  
                "lowPrice": "26088.34000000",  
                "lastPrice": "26221.67000000",  
                "volume": "18495.35066000",  
                "quoteVolume": "485217905.04210480",  
                "openTime": 1695686400000,  
                "closeTime": 1695772799999,  
                "firstId": 3220151555,  
                "lastId": 3220849281,  
                "count": 697727  
            },  
            {  
                "symbol": "BNBUSDT",  
                "priceChange": "2.60000000",  
                "priceChangePercent": "1.238",  
                "weightedAvgPrice": "211.92276958",  
                "openPrice": "210.00000000",  
                "highPrice": "213.70000000",  
                "lowPrice": "209.70000000",  
                "lastPrice": "212.60000000",  
                "volume": "280709.58900000",  
                "quoteVolume": "59488753.54750000",  
                "openTime": 1695686400000,  
                "closeTime": 1695772799999,  
                "firstId": 672397461,  
                "lastId": 672496158,  
                "count": 98698  
            }  
        ],  
        "rateLimits": [  
            {  
                "rateLimitType": "REQUEST_WEIGHT",  
                "interval": "MINUTE",  
                "intervalNum": 1,  
                "limit": 6000,  
                "count": 8  
            }  
        ]  
    }  
    

**Response: - MINI**

With `symbol`:
    
    
    {  
        "id": "f4b3b507-c8f2-442a-81a6-b2f12daa030f",  
        "status": 200,  
        "result": {  
            "symbol": "BTCUSDT",  
            "openPrice": "26304.80000000",  
            "highPrice": "26397.46000000",  
            "lowPrice": "26088.34000000",  
            "lastPrice": "26221.67000000",  
            "volume": "18495.35066000",              // Volume in base asset  
            "quoteVolume": "485217905.04210480",     // Volume in quote asset  
            "openTime": 1695686400000,  
            "closeTime": 1695772799999,  
            "firstId": 3220151555,                   // Trade ID of the first trade in the interval  
            "lastId": 3220849281,                    // Trade ID of the last trade in the interval  
            "count": 697727                          // Number of trades in the interval  
        },  
        "rateLimits": [  
            {  
                "rateLimitType": "REQUEST_WEIGHT",  
                "interval": "MINUTE",  
                "intervalNum": 1,  
                "limit": 6000,  
                "count": 4  
            }  
        ]  
    }  
    

With `symbols`:
    
    
    {  
        "id": "f4b3b507-c8f2-442a-81a6-b2f12daa030f",  
        "status": 200,  
        "result": [  
            {  
                "symbol": "BTCUSDT",  
                "openPrice": "26304.80000000",  
                "highPrice": "26397.46000000",  
                "lowPrice": "26088.34000000",  
                "lastPrice": "26221.67000000",  
                "volume": "18495.35066000",  
                "quoteVolume": "485217905.04210480",  
                "openTime": 1695686400000,  
                "closeTime": 1695772799999,  
                "firstId": 3220151555,  
                "lastId": 3220849281,  
                "count": 697727  
            },  
            {  
                "symbol": "BNBUSDT",  
                "openPrice": "210.00000000",  
                "highPrice": "213.70000000",  
                "lowPrice": "209.70000000",  
                "lastPrice": "212.60000000",  
                "volume": "280709.58900000",  
                "quoteVolume": "59488753.54750000",  
                "openTime": 1695686400000,  
                "closeTime": 1695772799999,  
                "firstId": 672397461,  
                "lastId": 672496158,  
                "count": 98698  
            }  
        ],  
        "rateLimits": [  
            {  
                "rateLimitType": "REQUEST_WEIGHT",  
                "interval": "MINUTE",  
                "intervalNum": 1,  
                "limit": 6000,  
                "count": 8  
            }  
        ]  
    }  
    

### Rolling window price change statistics[​](/docs/binance-spot-api-docs/websocket-api/market-data-requests#rolling-window-price-change-statistics "Direct link to Rolling window price change statistics")
    
    
    {  
        "id": "f4b3b507-c8f2-442a-81a6-b2f12daa030f",  
        "method": "ticker",  
        "params": {  
            "symbols": ["BNBBTC", "BTCUSDT"],  
            "windowSize": "7d"  
        }  
    }  
    

Get rolling window price change statistics with a custom window.

This request is similar to [`ticker.24hr`](/docs/binance-spot-api-docs/websocket-api/market-data-requests#24hr-ticker-price-change-statistics), but statistics are computed on demand using the arbitrary window you specify.

**Note:** Window size precision is limited to 1 minute. While the `closeTime` is the current time of the request, `openTime` always start on a minute boundary. As such, the effective window might be up to 59999 ms wider than the requested `windowSize`.

Window computation example

For example, a request for `"windowSize": "7d"` might result in the following window:
    
    
    {  
        "openTime": 1659580020000,  
        "closeTime": 1660184865291  
    }  
    

Time of the request – `closeTime` – is 1660184865291 (August 11, 2022 02:27:45.291). Requested window size should put the `openTime` 7 days before that – August 4, 02:27:45.291 – but due to limited precision it ends up a bit earlier: 1659580020000 (August 4, 2022 02:27:00), exactly at the start of a minute.

If you need to continuously monitor trading statistics, please consider using WebSocket Streams:

  * [`<symbol>@ticker_<window_size>`](/docs/binance-spot-api-docs/web-socket-streams#individual-symbol-rolling-window-statistics-streams) or [`!ticker_<window-size>@arr`](/docs/binance-spot-api-docs/web-socket-streams#all-market-rolling-window-statistics-streams)



**Weight:** Adjusted based on the number of requested symbols:

Symbols| Weight  
---|---  
1–50| 4 per symbol  
51–100| 200  
  
**Parameters:**

Name | Type | Mandatory | Description  
---|---|---|---  
`symbol` | STRING | YES | Query ticker of a single symbol  
`symbols` | ARRAY of STRING | Query ticker for multiple symbols  
`type` | ENUM | NO | Ticker type: `FULL` (default) or `MINI`  
`windowSize` | ENUM | NO | Default `1d`  
symbolStatus | ENUM | NO | Filters for symbols that have this `tradingStatus`.  
For a single symbol, a status mismatch returns error `-1220 SYMBOL_DOES_NOT_MATCH_STATUS`.   
For multiple symbols, non-matching ones are simply excluded from the response.  
Valid values: `TRADING`, `HALT`, `BREAK`  
  
Supported window sizes:

Unit| `windowSize` value  
---|---  
minutes| `1m`, `2m` ... `59m`  
hours| `1h`, `2h` ... `23h`  
days| `1d`, `2d` ... `7d`  
  
Notes:

  * Either `symbol` or `symbols` must be specified.

  * Maximum number of symbols in one request: 200.

  * Window size units cannot be combined. E.g., `1d 2h` is not supported.




**Data Source:** Database

**Response:**

`FULL` type, for a single symbol:
    
    
    {  
        "id": "f4b3b507-c8f2-442a-81a6-b2f12daa030f",  
        "status": 200,  
        "result": {  
            "symbol": "BNBBTC",  
            "priceChange": "0.00061500",  
            "priceChangePercent": "4.735",  
            "weightedAvgPrice": "0.01368242",  
            "openPrice": "0.01298900",  
            "highPrice": "0.01418800",  
            "lowPrice": "0.01296000",  
            "lastPrice": "0.01360400",  
            "volume": "587179.23900000",  
            "quoteVolume": "8034.03382165",  
            "openTime": 1659580020000,  
            "closeTime": 1660184865291,  
            "firstId": 192977765,     // First trade ID  
            "lastId": 195365758,      // Last trade ID  
            "count": 2387994          // Number of trades  
        },  
        "rateLimits": [  
            {  
                "rateLimitType": "REQUEST_WEIGHT",  
                "interval": "MINUTE",  
                "intervalNum": 1,  
                "limit": 6000,  
                "count": 4  
            }  
        ]  
    }  
    

`MINI` type, for a single symbol:
    
    
    {  
        "id": "bdb7c503-542c-495c-b797-4d2ee2e91173",  
        "status": 200,  
        "result": {  
            "symbol": "BNBBTC",  
            "openPrice": "0.01298900",  
            "highPrice": "0.01418800",  
            "lowPrice": "0.01296000",  
            "lastPrice": "0.01360400",  
            "volume": "587179.23900000",  
            "quoteVolume": "8034.03382165",  
            "openTime": 1659580020000,  
            "closeTime": 1660184865291,  
            "firstId": 192977765,     // First trade ID  
            "lastId": 195365758,      // Last trade ID  
            "count": 2387994          // Number of trades  
        },  
        "rateLimits": [  
            {  
                "rateLimitType": "REQUEST_WEIGHT",  
                "interval": "MINUTE",  
                "intervalNum": 1,  
                "limit": 6000,  
                "count": 4  
            }  
        ]  
    }  
    

If more than one symbol is requested, response returns an array:
    
    
    {  
        "id": "f4b3b507-c8f2-442a-81a6-b2f12daa030f",  
        "status": 200,  
        "result": [  
            {  
                "symbol": "BNBBTC",  
                "priceChange": "0.00061500",  
                "priceChangePercent": "4.735",  
                "weightedAvgPrice": "0.01368242",  
                "openPrice": "0.01298900",  
                "highPrice": "0.01418800",  
                "lowPrice": "0.01296000",  
                "lastPrice": "0.01360400",  
                "volume": "587169.48600000",  
                "quoteVolume": "8033.90114517",  
                "openTime": 1659580020000,  
                "closeTime": 1660184820927,  
                "firstId": 192977765,  
                "lastId": 195365700,  
                "count": 2387936  
            },  
            {  
                "symbol": "BTCUSDT",  
                "priceChange": "1182.92000000",  
                "priceChangePercent": "5.113",  
                "weightedAvgPrice": "23349.27074846",  
                "openPrice": "23135.33000000",  
                "highPrice": "24491.22000000",  
                "lowPrice": "22400.00000000",  
                "lastPrice": "24318.25000000",  
                "volume": "1039498.10978000",  
                "quoteVolume": "24271522807.76838630",  
                "openTime": 1659580020000,  
                "closeTime": 1660184820927,  
                "firstId": 1568787779,  
                "lastId": 1604337406,  
                "count": 35549628  
            }  
        ],  
        "rateLimits": [  
            {  
                "rateLimitType": "REQUEST_WEIGHT",  
                "interval": "MINUTE",  
                "intervalNum": 1,  
                "limit": 6000,  
                "count": 8  
            }  
        ]  
    }  
    

### Symbol price ticker[​](/docs/binance-spot-api-docs/websocket-api/market-data-requests#symbol-price-ticker "Direct link to Symbol price ticker")
    
    
    {  
        "id": "043a7cf2-bde3-4888-9604-c8ac41fcba4d",  
        "method": "ticker.price",  
        "params": {  
            "symbol": "BNBBTC"  
        }  
    }  
    

Get the latest market price for a symbol.

If you need access to real-time price updates, please consider using WebSocket Streams:

  * [`<symbol>@aggTrade`](/docs/binance-spot-api-docs/web-socket-streams#aggregate-trade-streams)
  * [`<symbol>@trade`](/docs/binance-spot-api-docs/web-socket-streams#trade-streams)



**Weight:** Adjusted based on the number of requested symbols:

Parameter| Weight  
---|---  
`symbol`| 2  
`symbols`| 4  
none| 4  
  
**Parameters:**

Name | Type | Mandatory | Description  
---|---|---|---  
`symbol` | STRING | NO | Query price for a single symbol  
`symbols` | ARRAY of STRING | Query price for multiple symbols  
symbolStatus | ENUM | NO | Filters for symbols that have this `tradingStatus`.  
For a single symbol, a status mismatch returns error `-1220 SYMBOL_DOES_NOT_MATCH_STATUS`.  
For multiple or all symbols, non-matching ones are simply excluded from the response.  
Valid values: `TRADING`, `HALT`, `BREAK`  
  
Notes:

  * `symbol` and `symbols` cannot be used together.

  * If no symbol is specified, returns information about all symbols currently trading on the exchange.




**Data Source:** Memory

**Response:**
    
    
    {  
        "id": "043a7cf2-bde3-4888-9604-c8ac41fcba4d",  
        "status": 200,  
        "result": {  
            "symbol": "BNBBTC",  
            "price": "0.01361900"  
        },  
        "rateLimits": [  
            {  
                "rateLimitType": "REQUEST_WEIGHT",  
                "interval": "MINUTE",  
                "intervalNum": 1,  
                "limit": 6000,  
                "count": 2  
            }  
        ]  
    }  
    

If more than one symbol is requested, response returns an array:
    
    
    {  
        "id": "e739e673-24c8-4adf-9cfa-b81f30330b09",  
        "status": 200,  
        "result": [  
            {  
                "symbol": "BNBBTC",  
                "price": "0.01363700"  
            },  
            {  
                "symbol": "BTCUSDT",  
                "price": "24267.15000000"  
            },  
            {  
                "symbol": "BNBBUSD",  
                "price": "331.10000000"  
            }  
        ],  
        "rateLimits": [  
            {  
                "rateLimitType": "REQUEST_WEIGHT",  
                "interval": "MINUTE",  
                "intervalNum": 1,  
                "limit": 6000,  
                "count": 4  
            }  
        ]  
    }  
    

### Symbol order book ticker[​](/docs/binance-spot-api-docs/websocket-api/market-data-requests#symbol-order-book-ticker "Direct link to Symbol order book ticker")
    
    
    {  
        "id": "057deb3a-2990-41d1-b58b-98ea0f09e1b4",  
        "method": "ticker.book",  
        "params": {  
            "symbols": ["BNBBTC", "BTCUSDT"]  
        }  
    }  
    

Get the current best price and quantity on the order book.

If you need access to real-time order book ticker updates, please consider using WebSocket Streams:

  * [`<symbol>@bookTicker`](/docs/binance-spot-api-docs/web-socket-streams#individual-symbol-book-ticker-streams)



**Weight:** Adjusted based on the number of requested symbols:

Parameter| Weight  
---|---  
`symbol`| 2  
`symbols`| 4  
none| 4  
  
**Parameters:**

Name | Type | Mandatory | Description  
---|---|---|---  
`symbol` | STRING | NO | Query ticker for a single symbol  
`symbols` | ARRAY of STRING | Query ticker for multiple symbols  
symbolStatus | ENUM | NO | Filters for symbols that have this `tradingStatus`.  
For a single symbol, a status mismatch returns error `-1220 SYMBOL_DOES_NOT_MATCH_STATUS`.   
For multiple or all symbols, non-matching ones are simply excluded from the response.  
Valid values: `TRADING`, `HALT`, `BREAK`  
  
Notes:

  * `symbol` and `symbols` cannot be used together.

  * If no symbol is specified, returns information about all symbols currently trading on the exchange.




**Data Source:** Memory

**Response:**
    
    
    {  
        "id": "9d32157c-a556-4d27-9866-66760a174b57",  
        "status": 200,  
        "result": {  
            "symbol": "BNBBTC",  
            "bidPrice": "0.01358000",  
            "bidQty": "12.53400000",  
            "askPrice": "0.01358100",  
            "askQty": "17.83700000"  
        },  
        "rateLimits": [  
            {  
                "rateLimitType": "REQUEST_WEIGHT",  
                "interval": "MINUTE",  
                "intervalNum": 1,  
                "limit": 6000,  
                "count": 2  
            }  
        ]  
    }  
    

If more than one symbol is requested, response returns an array:
    
    
    {  
        "id": "057deb3a-2990-41d1-b58b-98ea0f09e1b4",  
        "status": 200,  
        "result": [  
            {  
                "symbol": "BNBBTC",  
                "bidPrice": "0.01358000",  
                "bidQty": "12.53400000",  
                "askPrice": "0.01358100",  
                "askQty": "17.83700000"  
            },  
            {  
                "symbol": "BTCUSDT",  
                "bidPrice": "23980.49000000",  
                "bidQty": "0.01000000",  
                "askPrice": "23981.31000000",  
                "askQty": "0.01512000"  
            }  
        ],  
        "rateLimits": [  
            {  
                "rateLimitType": "REQUEST_WEIGHT",  
                "interval": "MINUTE",  
                "intervalNum": 1,  
                "limit": 6000,  
                "count": 4  
            }  
        ]  
    }  
    

### Query Reference Price[​](/docs/binance-spot-api-docs/websocket-api/market-data-requests#query-reference-price "Direct link to Query Reference Price")
    
    
    {  
      "id": "5132affb-0aba-4821-b475-f262504556b43",  
      "method": "referencePrice",  
      "params": {  
        "symbol": "BAZUSD"  
      }  
    }  
    

**Weight:** 2

**Parameters** :

Name| Type| Mandatory| Description  
---|---|---|---  
`symbol`| STRING| Yes|   
  
**Data Source:** Memory

**Response:**

If a reference price is set:
    
    
    {  
      "id": "5132affb-0aba-4821-b475-f262504556b43",  
      "status": 200,  
      "result": {  
        "symbol": "BAZUSD",  
        "referencePrice": "0.00501900",  
        "timestamp": 1770946889251  // Timestamp when the reference price was valid  
      }  
    }  
    

If no reference price is set:
    
    
    {  
      "id": "5132affb-0aba-4821-b475-f262504556b43",  
      "status": 200,  
      "result": {  
        "symbol": "BAZUSD",  
        "referencePrice": null,  
        "timestamp": 1770946889251  // Timestamp when the reference price was valid  
      }  
    }  
    

If no reference price has ever been set:
    
    
    {  
        "id": "5132affa-0aba-4831-b475-f262504556b41",  
        "status": 200,  
        "result":  
        {  
            "code": -2043,  
            "msg": "This symbol doesn't have a reference price."  
        }  
    }  
    

### Query Reference Price Calculation[​](/docs/binance-spot-api-docs/websocket-api/market-data-requests#query-reference-price-calculation "Direct link to Query Reference Price Calculation")
    
    
    {  
      "id": "5132affa-0aba-4831-b475-f262504556b41",  
      "method": "referencePrice.calculation",  
      "params": {  
        "symbol": "BAZUSD"  
      }  
    }  
    

Describes how reference price is calculated for a given symbol.

**Weight:** 2

**Parameters** :

Name| Type| Mandatory| Description  
---|---|---|---  
`symbol`| STRING| Yes|   
`symbolStatus`| ENUM| No| Supported values: `TRADING`, `HALT`, `BREAK`  
  
**Data Source:** Memory

**Response:**

If reference price is not being calculated:
    
    
    {  
        "id": "5132affa-0aba-4831-b475-f262504556b41",  
        "status": 400,  
        "error":  
        {  
            "code": -2043,  
            "msg": "This symbol doesn't have a reference price."  
        }  
    }  
    

If the reference price is being calculated by the matching engine as an arithmetic mean:
    
    
    {  
        "id": "5132affa-0aba-4831-b475-f262504556b41",  
        "status": 200,  
        "result":  
        {  
            "symbol": "BAZUSD",  
            "calculationType": "ARITHMETIC_MEAN",  
            "bucketCount": 10,  
            "bucketWidthMs": 1000  
        }  
    }  
    

If the reference price is being calculated outside the matching engine:
    
    
    {  
        "id": "5132affa-0aba-4831-b475-f262504556b41",  
        "status": 200,  
        "result":  
        {  
            "symbol": "BAZUSD",  
            "calculationType": "EXTERNAL",  
            "externalCalculationId": 42  
        }  
    }

---

# 行情接口

### 订单薄深度信息[​](/docs/zh-CN/binance-spot-api-docs/websocket-api/market-data-requests#订单薄深度信息 "订单薄深度信息的直接链接")  
      
    
    {  
        "id": "51e2affb-0aba-4821-ba75-f2625006eb43",  
        "method": "depth",  
        "params": {  
            "symbol": "BNBBTC",  
            "limit": 5  
        }  
    }  
    

获取当前深度信息。

请注意，此请求返回有限的市场深度。

如果需要持续监控深度信息更新，请考虑使用 WebSocket Streams：

  * [`<symbol>@depth<levels>`](/docs/zh-CN/binance-spot-api-docs/web-socket-streams#depth)
  * [`<symbol>@depth`](/docs/zh-CN/binance-spot-api-docs/web-socket-streams#diff-depth)



如果需要[维护本地orderbook](/docs/zh-CN/binance-spot-api-docs/web-socket-streams#how-to-maintain-orderbook)，您可以将 `depth` 请求与 `<symbol>@depth` streams 一起使用。

**权重:** 根据限制调整：

限制| 重量  
---|---  
1–100| 5  
101–500| 25  
501–1000| 50  
1001–5000| 250  
  
**参数:**

名称| 类型| 是否必需| 描述  
---|---|---|---  
`symbol`| STRING| YES|   
`limit`| INT| NO| 默认值： 100； 最大值： 5000  
`symbolStatus`| ENUM| NO| 过滤具有此 `tradingStatus` 的交易对。  
如果状态不匹配，将返回错误 `-1220 交易对与状态不匹配`。  
有效值： `TRADING`, `HALT`, `BREAK`  
  
**数据源:** 缓存

**响应:**
    
    
    {  
        "id": "51e2affb-0aba-4821-ba75-f2625006eb43",  
        "status": 200,  
        "result": {  
            "lastUpdateId": 2731179239,  
            // bid 水平从最高价到最低价排序。  
            "bids": [  
                [  
                    "0.01379900",     // 价格  
                    "3.43200000"      // 重量  
                ],  
                ["0.01379800", "3.24300000"],  
                ["0.01379700", "10.45500000"],  
                ["0.01379600", "3.82100000"],  
                ["0.01379500", "10.26200000"]  
            ],  
            // ask 水平从最低价到最高价排序。  
            "asks": [  
                ["0.01380000", "5.91700000"],  
                ["0.01380100", "6.01400000"],  
                ["0.01380200", "0.26800000"],  
                ["0.01380300", "0.33800000"],  
                ["0.01380400", "0.26800000"]  
            ]  
        },  
        "rateLimits": [  
            {  
                "rateLimitType": "REQUEST_WEIGHT",  
                "interval": "MINUTE",  
                "intervalNum": 1,  
                "limit": 6000,  
                "count": 5  
            }  
        ]  
    }  
    

### 最近的交易[​](/docs/zh-CN/binance-spot-api-docs/websocket-api/market-data-requests#最近的交易 "最近的交易的直接链接")
    
    
    {  
        "id": "409a20bd-253d-41db-a6dd-687862a5882f",  
        "method": "trades.recent",  
        "params": {  
            "symbol": "BNBBTC",  
            "limit": 1  
        }  
    }  
    

获取最近的交易

如果您需要访问实时交易活动，请考虑使用 WebSocket Streams：

  * [`<symbol>@trade`](/docs/zh-CN/binance-spot-api-docs/web-socket-streams#trade)



**权重:** 25

**参数:**

名称| 类型| 是否必需| 描述  
---|---|---|---  
`symbol`| STRING| YES|   
`limit`| INT| NO| 默认值： 500； 最大值： 1000  
  
**数据源:** 缓存

**响应:**
    
    
    {  
        "id": "409a20bd-253d-41db-a6dd-687862a5882f",  
        "status": 200,  
        "result": [  
            {  
                "id": 194686783,  
                "price": "0.01361000",  
                "qty": "0.01400000",  
                "quoteQty": "0.00019054",  
                "time": 1660009530807,  
                "isBuyerMaker": true,  
                "isBestMatch": true  
            }  
        ],  
        "rateLimits": [  
            {  
                "rateLimitType": "REQUEST_WEIGHT",  
                "interval": "MINUTE",  
                "intervalNum": 1,  
                "limit": 6000,  
                "count": 10  
            }  
        ]  
    }  
    

### 历史交易[​](/docs/zh-CN/binance-spot-api-docs/websocket-api/market-data-requests#历史交易 "历史交易的直接链接")
    
    
    {  
        "id": "cffc9c7d-4efc-4ce0-b587-6b87448f052a",  
        "method": "trades.historical",  
        "params": {  
            "symbol": "BNBBTC",  
            "fromId": 0,  
            "limit": 1  
        }  
    }  
    

获取历史交易。

**权重:** 25

**参数:**

名称| 类型| 是否必需| 描述  
---|---|---|---  
`symbol`| STRING| YES|   
`fromId`| INT| NO| 起始交易ID  
`limit`| INT| NO| 默认值 500； 最大值 1000  
  
备注：

  * 如果 `fromId` 未指定，则返回最近的交易。



**数据源:** 数据库

**响应:**
    
    
    {  
        "id": "cffc9c7d-4efc-4ce0-b587-6b87448f052a",  
        "status": 200,  
        "result": [  
            {  
                "id": 0,  
                "price": "0.00005000",  
                "qty": "40.00000000",  
                "quoteQty": "0.00200000",  
                "time": 1500004800376,  
                "isBuyerMaker": true,  
                "isBestMatch": true  
            }  
        ],  
        "rateLimits": [  
            {  
                "rateLimitType": "REQUEST_WEIGHT",  
                "interval": "MINUTE",  
                "intervalNum": 1,  
                "limit": 6000,  
                "count": 10  
            }  
        ]  
    }  
    

### 查询历史大宗交易[​](/docs/zh-CN/binance-spot-api-docs/websocket-api/market-data-requests#查询历史大宗交易 "查询历史大宗交易的直接链接")
    
    
    {  
        "id": "189da436-d4bd-48ca-9f95-9f613d621717",  
        "method": "blockTrades.historical",  
        "params": {  
            "symbol": "BNBBTC",  
            "fromId": 582,  
            "limit": 1  
        }  
    }  
    

获取历史大宗交易。

**权重:** 25

**参数:**

名称| 类型| 是否必需| 描述  
---|---|---|---  
`symbol`| STRING| YES|   
`fromId`| LONG| YES| 起始大宗交易ID  
`limit`| LONG| NO| 默认值：500; 最大值：1000  
  
**数据源:** 数据库

**响应:**
    
    
    {  
        "id": "cffc9c7d-4efc-4ce0-b587-6b87448f052a",  
        "status": 200,  
        "result":  
        [  
            {  
                "id": 582,  
                "price": "0.052",  
                "qty": "5838",  
                "quoteQty": "303.576",  
                "time": 1772506983321,  
                "isBuyerMaker": true  
            }  
        ],  
        "rateLimits":  
        [  
            {  
                "rateLimitType": "REQUEST_WEIGHT",  
                "interval": "MINUTE",  
                "intervalNum": 1,  
                "limit": 6000,  
                "count": 10  
            }  
        ]  
    }  
    

### 归集交易[​](/docs/zh-CN/binance-spot-api-docs/websocket-api/market-data-requests#归集交易 "归集交易的直接链接")
    
    
    {  
        "id": "189da436-d4bd-48ca-9f95-9f613d621717",  
        "method": "trades.aggregate",  
        "params": {  
            "symbol": "BNBBTC",  
            "fromId": 50000000,  
            "limit": 1  
        }  
    }  
    

获取归集交易。

一个 _归集交易_ (aggtrade) 代表一个或多个单独的交易。 同时间，同 taker 订单和同价格的执行交易会被聚合为一条归集交易。

如果需要访问实时交易活动，请考虑使用 WebSocket Streams：

  * [`<symbol>@aggTrade`](/docs/zh-CN/binance-spot-api-docs/web-socket-streams#aggtrade)



如果需要历史总交易数据，可以使用 [data.binance.vision](https://github.com/binance/binance-public-data/#aggtrades)。

**权重:** 4

**参数:**

名称| 类型| 是否必需| 描述  
---|---|---|---  
`symbol`| STRING| YES|   
`fromId`| LONG| NO| 起始归集交易ID  
`startTime`| LONG| NO|   
`endTime`| LONG| NO|   
`limit`| LONG| NO| 默认值： 500； 最大值： 1000  
  
备注：

  * 如果指定了 `fromId`，则返回归集交易 ID >= `fromId` 的 aggtrades。

使用 `fromId` 和 `limit` 会对所有 aggtrades 进行分页。

  * 如果指定了 `startTime` 和/或 `endTime`，响应中的 aggtrades 会按照执行时间 (`T`) 过滤。

`fromId` 不能与 `startTime` 和 `endTime` 一起使用。

  * 如果未指定条件，则返回最近的归集交易。




**数据源:** 数据库

**响应:**
    
    
    {  
        "id": "189da436-d4bd-48ca-9f95-9f613d621717",  
        "status": 200,  
        "result": [  
            {  
                "a": 50000000,          // 归集交易ID  
                "p": "0.00274100",      // 价格  
                "q": "57.19000000",     // 重量  
                "f": 59120167,          // 被归集的首个交易ID  
                "l": 59120170,          // 被归集的末次交易ID  
                "T": 1565877971222,     // 时间戳  
                "m": true,              // 买方是否是做市方。如true，则此次成交是一个主动卖出单，否则是一个主动买入单。  
                "M": true               // 交易是否是最好价格匹配。  
            }  
        ],  
        "rateLimits": [  
            {  
                "rateLimitType": "REQUEST_WEIGHT",  
                "interval": "MINUTE",  
                "intervalNum": 1,  
                "limit": 6000,  
                "count": 2  
            }  
        ]  
    }  
    

### K线数据[​](/docs/zh-CN/binance-spot-api-docs/websocket-api/market-data-requests#k线数据 "K线数据的直接链接")
    
    
    {  
        "id": "1dbbeb56-8eea-466a-8f6e-86bdcfa2fc0b",  
        "method": "klines",  
        "params": {  
            "symbol": "BNBBTC",  
            "interval": "1h",  
            "startTime": 1655969280000,  
            "limit": 1  
        }  
    }  
    

获取K线数据。

Klines 由其开盘时间和收盘时间为唯一标识。

如果您需要访问实时 kline 更新，请考虑使用 WebSocket Streams：

  * [`<symbol>@kline_<interval>`](/docs/zh-CN/binance-spot-api-docs/web-socket-streams#kline)



如果需要历史K线数据，可以使用 [data.binance.vision](https://github.com/binance/binance-public-data/./market-data-requests#klines)。

**权重:** 2

**参数:**

名称| 类型| 是否必需| 描述  
---|---|---|---  
`symbol`| STRING| YES|   
`interval`| ENUM| YES|   
`startTime`| LONG| NO|   
`endTime`| LONG| NO|   
`timeZone`| STRING| NO| 默认: 0 (UTC)  
`limit`| INT| NO| 默认值： 500； 最大值： 1000  
  
支持的 kline 间隔（大小写敏感）：

时间间隔| `interval` 值  
---|---  
seconds| `1s`  
minutes| `1m`, `3m`, `5m`, `15m`, `30m`  
hours| `1h`, `2h`, `4h`, `6h`, `8h`, `12h`  
days| `1d`, `3d`  
weeks| `1w`  
months| `1M`  
  
备注:

  * 如果没有指定 `startTime`，`endTime`，则返回最近的klines。
  * `timeZone`支持的值包括： 
    * 小时和分钟（例如 `-1:00`，`05:45`）
    * 仅小时（例如 `0`，`8，`4）
    * 接受的值范围严格为 [-12:00 到 +14:00]（包括边界）
  * 如果提供了`timeZone`，K线间隔将在该时区中解释，而不是在UTC中。
  * 请注意，无论`timeZone`如何，`startTime`和`endTime`始终以UTC时区解释。



**数据源:** 数据库

**响应:**
    
    
    {  
        "id": "1dbbeb56-8eea-466a-8f6e-86bdcfa2fc0b",  
        "status": 200,  
        "result": [  
            [  
                1655971200000,       // 这根K线的起始时间  
                "0.01086000",        // 这根K线期间第一笔成交价  
                "0.01086600",        // 这根K线期间最高成交价  
                "0.01083600",        // 这根K线期间最低成交价  
                "0.01083800",        // 这根K线期间末一笔成交价  
                "2290.53800000",     // 这根K线期间成交量  
                1655974799999,       // 这根K线的结束时间  
                "24.85074442",       // 这根K线期间成交额  
                2283,                // 这根K线期间成交笔数  
                "1171.64000000",     // 主动买入的成交量  
                "12.71225884",       // 主动买入的成交额  
                "0"                  // 忽略此参数  
            ]  
        ],  
        "rateLimits": [  
            {  
                "rateLimitType": "REQUEST_WEIGHT",  
                "interval": "MINUTE",  
                "intervalNum": 1,  
                "limit": 6000,  
                "count": 2  
            }  
        ]  
    }  
    

### UI K线数据[​](/docs/zh-CN/binance-spot-api-docs/websocket-api/market-data-requests#ui-k线数据 "UI K线数据的直接链接")
    
    
    {  
        "id": "b137468a-fb20-4c06-bd6b-625148eec958",  
        "method": "uiKlines",  
        "params": {  
            "symbol": "BNBBTC",  
            "interval": "1h",  
            "startTime": 1655969280000,  
            "limit": 1  
        }  
    }  
    

请求参数和响应字段与[`k线`](/docs/zh-CN/binance-spot-api-docs/websocket-api/market-data-requests#klines)接口相同。 uiKlines 是返回修改后的k线数据，针对k线图的呈现进行了优化。

**权重:** 2

**参数:**

名称| 类型| 是否必需| 描述  
---|---|---|---  
`symbol`| STRING| YES|   
`interval`| ENUM| YES| 请看 [`k线`](/docs/zh-CN/binance-spot-api-docs/websocket-api/market-data-requests#kline-intervals)  
`startTime`| LONG| NO|   
`endTime`| LONG| NO|   
`timeZone`| STRING| NO| 默认: 0 (UTC)  
`limit`| INT| NO| 默认值： 500； 最大值： 1000  
  
备注:

  * 如果没有指定 `startTime`，`endTime`，则返回最近的klines。
  * `timeZone`支持的值包括： 
    * 小时和分钟（例如 `-1:00`，`05:45`）
    * 仅小时（例如 `0`，`8，`4）
    * 接受的值范围严格为 [-12:00 到 +14:00]（包括边界）
  * 如果提供了`timeZone`，K线间隔将在该时区中解释，而不是在UTC中。
  * 请注意，无论`timeZone`如何，`startTime`和`endTime`始终以UTC时区解释。



**数据源:** 数据库

**响应:**
    
    
    {  
        "id": "b137468a-fb20-4c06-bd6b-625148eec958",  
        "status": 200,  
        "result": [  
            [  
                1655971200000,       // 这根K线的起始时间  
                "0.01086000",        // 这根K线期间第一笔成交价  
                "0.01086600",        // 这根K线期间最高成交价  
                "0.01083600",        // 这根K线期间最低成交价  
                "0.01083800",        // 这根K线期间末一笔成交价  
                "2290.53800000",     // 这根K线期间成交量  
                1655974799999,       // 这根K线的结束时间  
                "24.85074442",       // 这根K线期间成交额  
                2283,                // 这根K线期间成交笔数  
                "1171.64000000",     // 主动买入的成交量  
                "12.71225884",       // 主动买入的成交额  
                "0"                  // 忽略此参数  
            ]  
        ],  
        "rateLimits": [  
            {  
                "rateLimitType": "REQUEST_WEIGHT",  
                "interval": "MINUTE",  
                "intervalNum": 1,  
                "limit": 6000,  
                "count": 2  
            }  
        ]  
    }  
    

### 当前平均价格[​](/docs/zh-CN/binance-spot-api-docs/websocket-api/market-data-requests#当前平均价格 "当前平均价格的直接链接")
    
    
    {  
        "id": "ddbfb65f-9ebf-42ec-8240-8f0f91de0867",  
        "method": "avgPrice",  
        "params": {  
            "symbol": "BNBBTC"  
        }  
    }  
    

获取交易对的当前平均价格

**权重:** 2

**参数:**

名称| 类型| 是否必需| 描述  
---|---|---|---  
`symbol`| STRING| YES|   
  
**数据源:** 缓存

**响应:**
    
    
    {  
        "id": "ddbfb65f-9ebf-42ec-8240-8f0f91de0867",  
        "status": 200,  
        "result": {  
            "mins": 5, // 以分钟为单位的价格平均间隔  
            "price": "0.01378135",  
            "closeTime": 1694061154503  
        },  
        "rateLimits": [  
            {  
                "rateLimitType": "REQUEST_WEIGHT",  
                "interval": "MINUTE",  
                "intervalNum": 1,  
                "limit": 6000,  
                "count": 1  
            }  
        ]  
    }  
    

### 24hr 价格变动情况[​](/docs/zh-CN/binance-spot-api-docs/websocket-api/market-data-requests#24hr-价格变动情况 "24hr 价格变动情况的直接链接")
    
    
    {  
        "id": "93fb61ef-89f8-4d6e-b022-4f035a3fadad",  
        "method": "ticker.24hr",  
        "params": {  
            "symbol": "BNBBTC"  
        }  
    }  
    

24 小时滚动窗口价格变动数据。 如果您需要持续监控交易统计，请考虑使用 WebSocket Streams:

  * [`<symbol>@ticker`](/docs/zh-CN/binance-spot-api-docs/web-socket-streams_CN.md./market-data-requests#twentyfourhourticker)
  * [`<symbol>@miniTicker`](/docs/zh-CN/binance-spot-api-docs/web-socket-streams#twentyfourhourminiticker) 或者 [`!miniTicker@arr`](/docs/zh-CN/binance-spot-api-docs/web-socket-streams#all-markets-mini-ticker)



如果你想用不同的窗口数量，可以用 [`ticker`](/docs/zh-CN/binance-spot-api-docs/websocket-api/market-data-requests#ticker) 请求。

**权重:** 根据交易对的数量进行调整：

交易对| 重量  
---|---  
1–20| 2  
21–100| 40  
101 以上| 80  
全部交易对| 80  
  
**参数:**

名称 | 类型 | 是否必需 | 描述  
---|---|---|---  
`symbol` | STRING | NO | 获取单个交易对的 ticker  
`symbols` | ARRAY of STRING | 获取多个交易对的 ticker  
`type` | ENUM | NO | Ticker 类型: `FULL` (默认) 或者 `MINI`  
symbolStatus | ENUM | NO | 过滤具有此 `tradingStatus` 的交易对。  
对于单个交易对，如果状态不匹配，将返回错误 `-1220 交易对与状态不匹配`。  
对于多个或者全部交易对， 响应中不会包括状态不匹配的交易对。  
有效值： `TRADING`, `HALT`, `BREAK`  
  
备注:

  * `symbol` 和 `symbols` 不能同时用。

  * 如果未指定交易对，则返回有关当前在交易所交易的所有交易对的信息。




**数据源:** 缓存

**响应:**

`FULL` 类型，对于单个交易对：
    
    
    {  
        "id": "93fb61ef-89f8-4d6e-b022-4f035a3fadad",  
        "status": 200,  
        "result": {  
            "symbol": "BNBBTC",  
            "priceChange": "0.00013900",  
            "priceChangePercent": "1.020",  
            "weightedAvgPrice": "0.01382453",  
            "prevClosePrice": "0.01362800",  
            "lastPrice": "0.01376700",  
            "lastQty": "1.78800000",  
            "bidPrice": "0.01376700",  
            "bidQty": "4.64600000",  
            "askPrice": "0.01376800",  
            "askQty": "14.31400000",  
            "openPrice": "0.01362800",  
            "highPrice": "0.01414900",  
            "lowPrice": "0.01346600",  
            "volume": "69412.40500000",  
            "quoteVolume": "959.59411487",  
            "openTime": 1660014164909,  
            "closeTime": 1660100564909,  
            "firstId": 194696115,     // 第一个交易 ID  
            "lastId": 194968287,      // 最后一个交易 ID  
            "count": 272173           // 成交笔数  
        },  
        "rateLimits": [  
            {  
                "rateLimitType": "REQUEST_WEIGHT",  
                "interval": "MINUTE",  
                "intervalNum": 1,  
                "limit": 6000,  
                "count": 2  
            }  
        ]  
    }  
    

`MINI` 类型，对于单个交易对：
    
    
    {  
        "id": "9fa2a91b-3fca-4ed7-a9ad-58e3b67483de",  
        "status": 200,  
        "result": {  
            "symbol": "BNBBTC",  
            "openPrice": "0.01362800",  
            "highPrice": "0.01414900",  
            "lowPrice": "0.01346600",  
            "lastPrice": "0.01376700",  
            "volume": "69412.40500000",  
            "quoteVolume": "959.59411487",  
            "openTime": 1660014164909,  
            "closeTime": 1660100564909,  
            "firstId": 194696115,     // 第一个交易 ID  
            "lastId": 194968287,      // 最后一个交易ID  
            "count": 272173           // 成交笔数  
        },  
        "rateLimits": [  
            {  
                "rateLimitType": "REQUEST_WEIGHT",  
                "interval": "MINUTE",  
                "intervalNum": 1,  
                "limit": 6000,  
                "count": 2  
            }  
        ]  
    }  
    

如果请求是有多个交易对，响应会是数组类型:
    
    
    {  
        "id": "901be0d9-fd3b-45e4-acd6-10c580d03430",  
        "status": 200,  
        "result": [  
            {  
                "symbol": "BNBBTC",  
                "priceChange": "0.00016500",  
                "priceChangePercent": "1.213",  
                "weightedAvgPrice": "0.01382508",  
                "prevClosePrice": "0.01360800",  
                "lastPrice": "0.01377200",  
                "lastQty": "1.01400000",  
                "bidPrice": "0.01377100",  
                "bidQty": "7.55700000",  
                "askPrice": "0.01377200",  
                "askQty": "4.37900000",  
                "openPrice": "0.01360700",  
                "highPrice": "0.01414900",  
                "lowPrice": "0.01346600",  
                "volume": "69376.27900000",  
                "quoteVolume": "959.13277091",  
                "openTime": 1660014615517,  
                "closeTime": 1660101015517,  
                "firstId": 194697254,  
                "lastId": 194969483,  
                "count": 272230  
            },  
            {  
                "symbol": "BTCUSDT",  
                "priceChange": "-938.06000000",  
                "priceChangePercent": "-3.938",  
                "weightedAvgPrice": "23265.34432003",  
                "prevClosePrice": "23819.17000000",  
                "lastPrice": "22880.91000000",  
                "lastQty": "0.00536000",  
                "bidPrice": "22880.40000000",  
                "bidQty": "0.00424000",  
                "askPrice": "22880.91000000",  
                "askQty": "0.04276000",  
                "openPrice": "23818.97000000",  
                "highPrice": "23933.25000000",  
                "lowPrice": "22664.69000000",  
                "volume": "153508.37606000",  
                "quoteVolume": "3571425225.04441220",  
                "openTime": 1660014615977,  
                "closeTime": 1660101015977,  
                "firstId": 1592019902,  
                "lastId": 1597301762,  
                "count": 5281861  
            }  
        ],  
        "rateLimits": [  
            {  
                "rateLimitType": "REQUEST_WEIGHT",  
                "interval": "MINUTE",  
                "intervalNum": 1,  
                "limit": 6000,  
                "count": 2  
            }  
        ]  
    }  
    

### 交易日行情(Ticker)[​](/docs/zh-CN/binance-spot-api-docs/websocket-api/market-data-requests#交易日行情ticker "交易日行情\(Ticker\)的直接链接")
    
    
    {  
        "id": "f4b3b507-c8f2-442a-81a6-b2f12daa030f",  
        "method": "ticker.tradingDay",  
        "params": {  
            "symbols": ["BNBBTC", "BTCUSDT"],  
            "timeZone": "00:00"  
        }  
    }  
    

交易日价格变动统计。

**权重:**

每个`交易对`占用4个权重.   
  
当请求中的交易对数量超过50，此请求的权重将限制在200。

**参数:**

名称 | 类型 | 是否必需 | 描述  
---|---|---|---  
`symbol` | STRING | YES | 查询单交易对的行情  
`symbols` | ARRAY of STRING | 查询多交易对行情  
`timeZone` | STRING | NO | 默认: 0 (UTC)  
`type` | ENUM | NO | 可接受值: `FULL` or `MINI`.   
默认值: `FULL`  
symbolStatus | ENUM | NO | 过滤具有此 `tradingStatus` 的交易对。  
对于单个交易对，如果状态不匹配，将返回错误 `-1220 交易对与状态不匹配`。  
对于多个交易对， 响应中不会包括状态不匹配的交易对。  
有效值： `TRADING`, `HALT`, `BREAK`  
  
**注意:**

  * `timeZone`支持的值包括： 
    * 小时和分钟（例如 `-1:00`，`05:45`）
    * 仅小时（例如 `0`，`8`，`4`）



**数据源:** 数据库

**响应 - FULL**

有 `symbol`:
    
    
    {  
        "id": "f4b3b507-c8f2-442a-81a6-b2f12daa030f",  
        "status": 200,  
        "result": {  
            "symbol": "BTCUSDT",  
            "priceChange": "-83.13000000",            // 绝对价格变动  
            "priceChangePercent": "-0.317",           // 相对价格变动百分比  
            "weightedAvgPrice": "26234.58803036",     // 报价成交量 / 成交量  
            "openPrice": "26304.80000000",  
            "highPrice": "26397.46000000",  
            "lowPrice": "26088.34000000",  
            "lastPrice": "26221.67000000",  
            "volume": "18495.35066000",               // 基础资产的成交量  
            "quoteVolume": "485217905.04210480",  
            "openTime": 1695686400000,  
            "closeTime": 1695772799999,  
            "firstId": 3220151555,  
            "lastId": 3220849281,  
            "count": 697727  
        },  
        "rateLimits": [  
            {  
                "rateLimitType": "REQUEST_WEIGHT",  
                "interval": "MINUTE",  
                "intervalNum": 1,  
                "limit": 6000,  
                "count": 4  
            }  
        ]  
    }  
    

有 `symbols`:
    
    
    {  
        "id": "f4b3b507-c8f2-442a-81a6-b2f12daa030f",  
        "status": 200,  
        "result": [  
            {  
                "symbol": "BTCUSDT",  
                "priceChange": "-83.13000000",  
                "priceChangePercent": "-0.317",  
                "weightedAvgPrice": "26234.58803036",  
                "openPrice": "26304.80000000",  
                "highPrice": "26397.46000000",  
                "lowPrice": "26088.34000000",  
                "lastPrice": "26221.67000000",  
                "volume": "18495.35066000",  
                "quoteVolume": "485217905.04210480",  
                "openTime": 1695686400000,  
                "closeTime": 1695772799999,  
                "firstId": 3220151555,  
                "lastId": 3220849281,  
                "count": 697727  
            },  
            {  
                "symbol": "BNBUSDT",  
                "priceChange": "2.60000000",  
                "priceChangePercent": "1.238",  
                "weightedAvgPrice": "211.92276958",  
                "openPrice": "210.00000000",  
                "highPrice": "213.70000000",  
                "lowPrice": "209.70000000",  
                "lastPrice": "212.60000000",  
                "volume": "280709.58900000",  
                "quoteVolume": "59488753.54750000",  
                "openTime": 1695686400000,  
                "closeTime": 1695772799999,  
                "firstId": 672397461,  
                "lastId": 672496158,  
                "count": 98698  
            }  
        ],  
        "rateLimits": [  
            {  
                "rateLimitType": "REQUEST_WEIGHT",  
                "interval": "MINUTE",  
                "intervalNum": 1,  
                "limit": 6000,  
                "count": 8  
            }  
        ]  
    }  
    

**相应: - MINI**

有 `symbol`:
    
    
    {  
        "id": "f4b3b507-c8f2-442a-81a6-b2f12daa030f",  
        "status": 200,  
        "result": {  
            "symbol": "BTCUSDT",  
            "openPrice": "26304.80000000",  
            "highPrice": "26397.46000000",  
            "lowPrice": "26088.34000000",  
            "lastPrice": "26221.67000000",  
            "volume": "18495.35066000",              // 基础资产的成交量  
            "quoteVolume": "485217905.04210480",     // 报价资产的成交量  
            "openTime": 1695686400000,  
            "closeTime": 1695772799999,  
            "firstId": 3220151555,                   // 区间内的第一个交易的交易ID  
            "lastId": 3220849281,                    // 区间内的最后一个交易的交易ID  
            "count": 697727                          // 区间内的交易数量  
        },  
        "rateLimits": [  
            {  
                "rateLimitType": "REQUEST_WEIGHT",  
                "interval": "MINUTE",  
                "intervalNum": 1,  
                "limit": 6000,  
                "count": 4  
            }  
        ]  
    }  
    

With `symbols`:
    
    
    {  
        "id": "f4b3b507-c8f2-442a-81a6-b2f12daa030f",  
        "status": 200,  
        "result": [  
            {  
                "symbol": "BTCUSDT",  
                "openPrice": "26304.80000000",  
                "highPrice": "26397.46000000",  
                "lowPrice": "26088.34000000",  
                "lastPrice": "26221.67000000",  
                "volume": "18495.35066000",  
                "quoteVolume": "485217905.04210480",  
                "openTime": 1695686400000,  
                "closeTime": 1695772799999,  
                "firstId": 3220151555,  
                "lastId": 3220849281,  
                "count": 697727  
            },  
            {  
                "symbol": "BNBUSDT",  
                "openPrice": "210.00000000",  
                "highPrice": "213.70000000",  
                "lowPrice": "209.70000000",  
                "lastPrice": "212.60000000",  
                "volume": "280709.58900000",  
                "quoteVolume": "59488753.54750000",  
                "openTime": 1695686400000,  
                "closeTime": 1695772799999,  
                "firstId": 672397461,  
                "lastId": 672496158,  
                "count": 98698  
            }  
        ],  
        "rateLimits": [  
            {  
                "rateLimitType": "REQUEST_WEIGHT",  
                "interval": "MINUTE",  
                "intervalNum": 1,  
                "limit": 6000,  
                "count": 8  
            }  
        ]  
    }  
    

### 滚动窗口价格变动统计[​](/docs/zh-CN/binance-spot-api-docs/websocket-api/market-data-requests#滚动窗口价格变动统计 "滚动窗口价格变动统计的直接链接")
    
    
    {  
        "id": "f4b3b507-c8f2-442a-81a6-b2f12daa030f",  
        "method": "ticker",  
        "params": {  
            "symbols": ["BNBBTC", "BTCUSDT"],  
            "windowSize": "7d"  
        }  
    }  
    

使用自定义窗口获取滚动窗口价格变化统计信息。

这个请求类似于 [`ticker.24hr`](/docs/zh-CN/binance-spot-api-docs/websocket-api/market-data-requests#twentyfourhourticker)，但统计数据是使用指定的任意窗口按需计算的。

**注意：** 窗口大小精度限制为1分钟。 虽然 `closeTime` 是请求的当前时间，`openTime` 总是从分钟边界开始。 因此，有效窗口可能比请求的 `windowSize` 宽59999毫秒。

窗口计算示例

例如，对 `"windowSize": "7d"` 的请求可能会导致以下窗口：
    
    
    {  
        "openTime": 1659580020000,  
        "closeTime": 1660184865291  
    }  
    

请求的时间 - `closeTime` \- 是 1660184865291（2022年8月11日 02:27:45.291）。 请求的窗口大小应将 `openTime` 设置为7天之前 – 8月4日，02:27:45.291 – 但由于精度有限，它最终会提前一点：1659580020000（2022年8月4日 02:27:00），正好在一分钟开始。

如果您需要持续监控交易统计，请考虑使用 WebSocket Streams:

  * [`<symbol>@ticker_<window_size>`](/docs/zh-CN/binance-spot-api-docs/web-socket-streams#rolling-window-ticker) 或者 [`!ticker_<window-size>@arr`](/docs/zh-CN/binance-spot-api-docs/web-socket-streams#all-market-rolling-window-ticker)



**权重:** 根据交易对的数量进行调整：

交易对| 重量  
---|---  
1–50| 4 per symbol  
51–100| 200  
  
**参数:**

名称 | 类型 | 是否必需 | 描述  
---|---|---|---  
`symbol` | STRING | YES | 获取单个交易对的 ticker  
`symbols` | ARRAY of STRING | 获取多个交易对的 ticker  
`type` | ENUM | NO | Ticker 类型： `FULL` (默认) 或者 `MINI`  
`windowSize` | ENUM | NO | 默认 `1d`  
symbolStatus | ENUM | NO | 过滤具有此 `tradingStatus` 的交易对。  
对于单个交易对，如果状态不匹配，将返回错误 `-1220 交易对与状态不匹配`。  
对于多个交易对， 响应中不会包括状态不匹配的交易对。  
有效值： `TRADING`, `HALT`, `BREAK`  
  
支持的窗口 size:

单位| `windowSize` 值  
---|---  
minutes| `1m`, `2m` ... `59m`  
hours| `1h`, `2h` ... `23h`  
days| `1d`, `2d` ... `7d`  
  
备注：

  * 必须指定 `symbol` 或 `symbols`。

  * 一个请求中的最大交易对数：200。

  * 窗口 size 单位不能合并。 比如不支持 `1d 2h`。




**数据源:** 数据库

**响应:**

`FULL` 类型，对于单个交易对：
    
    
    {  
        "id": "f4b3b507-c8f2-442a-81a6-b2f12daa030f",  
        "status": 200,  
        "result": {  
            "symbol": "BNBBTC",  
            "priceChange": "0.00061500",  
            "priceChangePercent": "4.735",  
            "weightedAvgPrice": "0.01368242",  
            "openPrice": "0.01298900",  
            "highPrice": "0.01418800",  
            "lowPrice": "0.01296000",  
            "lastPrice": "0.01360400",  
            "volume": "587179.23900000",  
            "quoteVolume": "8034.03382165",  
            "openTime": 1659580020000,  
            "closeTime": 1660184865291,  
            "firstId": 192977765,     // 第一个交易 ID  
            "lastId": 195365758,      // 最后交易 ID  
            "count": 2387994          // 成交笔数  
        },  
        "rateLimits": [  
            {  
                "rateLimitType": "REQUEST_WEIGHT",  
                "interval": "MINUTE",  
                "intervalNum": 1,  
                "limit": 6000,  
                "count": 4  
            }  
        ]  
    }  
    

`MINI` 类型，对于单个交易对：
    
    
    {  
        "id": "bdb7c503-542c-495c-b797-4d2ee2e91173",  
        "status": 200,  
        "result": {  
            "symbol": "BNBBTC",  
            "openPrice": "0.01298900",  
            "highPrice": "0.01418800",  
            "lowPrice": "0.01296000",  
            "lastPrice": "0.01360400",  
            "volume": "587179.23900000",  
            "quoteVolume": "8034.03382165",  
            "openTime": 1659580020000,  
            "closeTime": 1660184865291,  
            "firstId": 192977765,     // 第一个交易 ID  
            "lastId": 195365758,      // 最后交易 ID  
            "count": 2387994          // 成交笔数  
        },  
        "rateLimits": [  
            {  
                "rateLimitType": "REQUEST_WEIGHT",  
                "interval": "MINUTE",  
                "intervalNum": 1,  
                "limit": 6000,  
                "count": 4  
            }  
        ]  
    }  
    

如果请求是有多个交易对，响应会是数组类型:
    
    
    {  
        "id": "f4b3b507-c8f2-442a-81a6-b2f12daa030f",  
        "status": 200,  
        "result": [  
            {  
                "symbol": "BNBBTC",  
                "priceChange": "0.00061500",  
                "priceChangePercent": "4.735",  
                "weightedAvgPrice": "0.01368242",  
                "openPrice": "0.01298900",  
                "highPrice": "0.01418800",  
                "lowPrice": "0.01296000",  
                "lastPrice": "0.01360400",  
                "volume": "587169.48600000",  
                "quoteVolume": "8033.90114517",  
                "openTime": 1659580020000,  
                "closeTime": 1660184820927,  
                "firstId": 192977765,  
                "lastId": 195365700,  
                "count": 2387936  
            },  
            {  
                "symbol": "BTCUSDT",  
                "priceChange": "1182.92000000",  
                "priceChangePercent": "5.113",  
                "weightedAvgPrice": "23349.27074846",  
                "openPrice": "23135.33000000",  
                "highPrice": "24491.22000000",  
                "lowPrice": "22400.00000000",  
                "lastPrice": "24318.25000000",  
                "volume": "1039498.10978000",  
                "quoteVolume": "24271522807.76838630",  
                "openTime": 1659580020000,  
                "closeTime": 1660184820927,  
                "firstId": 1568787779,  
                "lastId": 1604337406,  
                "count": 35549628  
            }  
        ],  
        "rateLimits": [  
            {  
                "rateLimitType": "REQUEST_WEIGHT",  
                "interval": "MINUTE",  
                "intervalNum": 1,  
                "limit": 6000,  
                "count": 8  
            }  
        ]  
    }  
    

### 最新价格[​](/docs/zh-CN/binance-spot-api-docs/websocket-api/market-data-requests#最新价格 "最新价格的直接链接")
    
    
    {  
        "id": "043a7cf2-bde3-4888-9604-c8ac41fcba4d",  
        "method": "ticker.price",  
        "params": {  
            "symbol": "BNBBTC"  
        }  
    }  
    

获取交易对最新价格

如果需要访问实时价格更新，请考虑使用 WebSocket Streams:

  * [`<symbol>@aggTrade`](/docs/zh-CN/binance-spot-api-docs/web-socket-streams#aggtrade)
  * [`<symbol>@trade`](/docs/zh-CN/binance-spot-api-docs/web-socket-streams#trade)



**权重:** 根据交易对的数量进行调整：

参数| 重量  
---|---  
`symbol`| 2  
`symbols`| 4  
none| 4  
  
**参数:**

名称 | 类型 | 是否必需 | 描述  
---|---|---|---  
`symbol` | STRING | NO | 获取单个交易对的 price  
`symbols` | ARRAY of STRING | 获取多个交易对的 price   
symbolStatus | ENUM | NO | 过滤具有此 `tradingStatus` 的交易对。  
对于单个交易对，如果状态不匹配，将返回错误 `-1220 交易对与状态不匹配`。  
对于多个或者全部交易对， 响应中不会包括状态不匹配的交易对。  
有效值： `TRADING`, `HALT`, `BREAK`  
  
备注：

  * `symbol` 和 `symbols` 不能一起使用。

  * 如果未指定交易对，则返回有关当前在交易所交易的所有交易对的信息。




**数据源:** 缓存

**响应:**
    
    
    {  
        "id": "043a7cf2-bde3-4888-9604-c8ac41fcba4d",  
        "status": 200,  
        "result": {  
            "symbol": "BNBBTC",  
            "price": "0.01361900"  
        },  
        "rateLimits": [  
            {  
                "rateLimitType": "REQUEST_WEIGHT",  
                "interval": "MINUTE",  
                "intervalNum": 1,  
                "limit": 6000,  
                "count": 2  
            }  
        ]  
    }  
    

如果请求是有多个交易对，响应会是数组类型:
    
    
    {  
        "id": "e739e673-24c8-4adf-9cfa-b81f30330b09",  
        "status": 200,  
        "result": [  
            {  
                "symbol": "BNBBTC",  
                "price": "0.01363700"  
            },  
            {  
                "symbol": "BTCUSDT",  
                "price": "24267.15000000"  
            },  
            {  
                "symbol": "BNBBUSD",  
                "price": "331.10000000"  
            }  
        ],  
        "rateLimits": [  
            {  
                "rateLimitType": "REQUEST_WEIGHT",  
                "interval": "MINUTE",  
                "intervalNum": 1,  
                "limit": 6000,  
                "count": 4  
            }  
        ]  
    }  
    

### 当前最优挂单[​](/docs/zh-CN/binance-spot-api-docs/websocket-api/market-data-requests#当前最优挂单 "当前最优挂单的直接链接")
    
    
    {  
        "id": "057deb3a-2990-41d1-b58b-98ea0f09e1b4",  
        "method": "ticker.book",  
        "params": {  
            "symbols": ["BNBBTC", "BTCUSDT"]  
        }  
    }  
    

在订单薄获取当前最优价格和数量。

如果您需要访问实时订单薄 ticker 更新，请考虑使用 WebSocket Streams:

  * [`<symbol>@bookTicker`](/docs/zh-CN/binance-spot-api-docs/web-socket-streams#bookticker)



**权重:** 根据交易对的数量进行调整：

参数| 重量  
---|---  
`symbol`| 2  
`symbols`| 4  
none| 4  
  
**参数:**

名称 | 类型 | 是否必需 | 描述  
---|---|---|---  
`symbol` | STRING | NO | 获取单个交易对的 ticker  
`symbols` | ARRAY of STRING | 获取多个交易对的 ticker  
symbolStatus | ENUM | NO | 过滤具有此 `tradingStatus` 的交易对。  
对于单个交易对，如果状态不匹配，将返回错误 `-1220 交易对与状态不匹配`。  
对于多个或者全部交易对， 响应中不会包括状态不匹配的交易对。  
有效值： `TRADING`, `HALT`, `BREAK`  
  
备注：

  * `symbol` 和 `symbols` 不能一起使用。

  * 如果未指定交易对，则返回有关当前在交易所交易的所有交易对的信息。




**数据源:** 缓存

**响应:**
    
    
    {  
        "id": "9d32157c-a556-4d27-9866-66760a174b57",  
        "status": 200,  
        "result": {  
            "symbol": "BNBBTC",  
            "bidPrice": "0.01358000",  
            "bidQty": "12.53400000",  
            "askPrice": "0.01358100",  
            "askQty": "17.83700000"  
        },  
        "rateLimits": [  
            {  
                "rateLimitType": "REQUEST_WEIGHT",  
                "interval": "MINUTE",  
                "intervalNum": 1,  
                "limit": 6000,  
                "count": 2  
            }  
        ]  
    }  
    

如果请求是有多个交易对，响应会是数组类型:
    
    
    {  
        "id": "057deb3a-2990-41d1-b58b-98ea0f09e1b4",  
        "status": 200,  
        "result": [  
            {  
                "symbol": "BNBBTC",  
                "bidPrice": "0.01358000",  
                "bidQty": "12.53400000",  
                "askPrice": "0.01358100",  
                "askQty": "17.83700000"  
            },  
            {  
                "symbol": "BTCUSDT",  
                "bidPrice": "23980.49000000",  
                "bidQty": "0.01000000",  
                "askPrice": "23981.31000000",  
                "askQty": "0.01512000"  
            }  
        ],  
        "rateLimits": [  
            {  
                "rateLimitType": "REQUEST_WEIGHT",  
                "interval": "MINUTE",  
                "intervalNum": 1,  
                "limit": 6000,  
                "count": 4  
            }  
        ]  
    }  
    

### 查询参考价格[​](/docs/zh-CN/binance-spot-api-docs/websocket-api/market-data-requests#查询参考价格 "查询参考价格的直接链接")
    
    
    {  
      "id": "5132affb-0aba-4821-b475-f262504556b43",  
      "method": "referencePrice",  
      "params": {  
        "symbol": "BAZUSD"  
      }  
    }  
    

**权重：** 2

**参数：**

名称| 类型| 是否必需| 描述  
---|---|---|---  
`symbol`| STRING| YES|   
  
**数据来源：** 缓存

**响应示例：**

如果设置了参考价格：
    
    
    {  
      "id": "5132affb-0aba-4821-b475-f262504556b43",  
      "status": 200,  
      "result": {  
        "symbol": "BAZUSD",  
        "referencePrice": "0.00501900",  
        "timestamp": 1770946889251     //参考价格生效的时间  
      }  
    }  
    

如果未设置参考价格：
    
    
    {  
      "id": "5132affb-0aba-4821-b475-f262504556b43",  
      "status": 200,  
      "result": {  
        "symbol": "BAZUSD",  
        "referencePrice": null,  
        "timestamp": 1770946889251      //参考价格生效的时间  
      }  
    }  
    

如果从未设置过参考价格：
    
    
    {  
        "id": "5132affa-0aba-4831-b475-f262504556b41",  
        "status": 200,  
        "result":  
        {  
            "code": -2043,  
            "msg": "This symbol doesn't have a reference price."  
        }  
    }  
    

### 查询参考价格计算方式[​](/docs/zh-CN/binance-spot-api-docs/websocket-api/market-data-requests#查询参考价格计算方式 "查询参考价格计算方式的直接链接")
    
    
    {  
      "id": "5132affa-0aba-4831-b475-f262504556b41",  
      "method": "referencePrice.calculation",  
      "params": {  
        "symbol": "BAZUSD"  
      }  
    }  
    

描述指定交易对参考价格的计算方式。

**权重：** 2

**参数：**

名称| 类型| 是否必需| 描述  
---|---|---|---  
`symbol`| STRING| YES|   
`symbolStatus`| ENUM| NO| 支持的值：`TRADING`（正常交易中）、`HALT`（交易终止）、`BREAK`（交易暂停）  
  
**数据来源：** 缓存

**响应示例：**

如果参考价格未被计算：
    
    
    {  
        "id": "5132affa-0aba-4831-b475-f262504556b41",  
        "status": 400,  
        "error":  
        {  
            "code": -2043,  
            "msg": "This symbol doesn't have a reference price."  
        }  
    }  
    

如果参考价格由撮合引擎以算术平均数计算：
    
    
    {  
      "symbol": "BAZUSD",  
      "calculationType": "ARITHMETIC_MEAN",  
      "bucketCount": 10,  
      "bucketWidthMs": 1000  
    }  
    

如果参考价格由撮合引擎外部计算：
    
    
    {  
      "symbol": "BAZUSD",  
      "calculationType": "EXTERNAL",  
      "externalCalculationId": 42  
    }