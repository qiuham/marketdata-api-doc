---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#trading-statistics
anchor_id: trading-statistics
api_type: API
updated_at: 2026-07-20 19:37:04.293413
---

# Trading Statistics

## REST API  
  
The API endpoints of `Trading Statistics` do not require authentication.

### Get support coin

Retrieve the currencies supported by the trading statistics endpoints.

#### Rate Limit: 5 requests per 2 seconds

#### Rate limit rule: IP

#### HTTP Request

`GET /api/v5/rubik/stat/trading-data/support-coin`

> Request Example
    
    
    GET /api/v5/rubik/stat/trading-data/support-coin
    
    
    
    import okx.TradingData as TradingData_api
    
    flag = "0"  # Production trading:0 , demo trading:1
    
    tradingDataAPI = TradingData_api.TradingDataAPI(flag=flag)
    
    # Retrieve the currencies supported by the trading statistics endpoints
    result = tradingDataAPI.get_support_coin()
    print(result)
    

> Response Example
    
    
    {
        "code": "0",
        "data": {
            "contract": [
                "ADA",
                "BTC"
            ],
            "option": [
                "BTC"
            ],
            "spot": [
                "ADA",
                "BTC"
            ]
        },
        "msg": ""
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
contract | Array of strings | Currency supported by derivatives trading data  
option | Array of strings | Currency supported by option trading data  
spot | Array of strings | Currency supported by spot trading data  
  
### Get contract open interest history

Retrieve the contract open interest statistics of futures and perp. This endpoint can retrieve the latest 1,440 data entries.   

For period=1D, the data time range is up to January 1, 2024; for other periods, the data time range is up to early February 2024.

#### Rate limit: 10 requests per 2 seconds

#### Rate limit rule: IP + Instrument ID

#### HTTP Request

`GET /api/v5/rubik/stat/contracts/open-interest-history`

> Request example
    
    
    GET /api/v5/rubik/stat/contracts/open-interest-history?instId=BTC-USDT-SWAP
    
    
    
    import okx.TradingData as TradingData_api
    
    flag = "0"  # Production trading:0 , demo trading:1
    
    tradingDataAPI = TradingData_api.TradingDataAPI(flag=flag)
    
    # Retrieve the open interest history
    result = tradingDataAPI.get_open_interest_history(
        instId="BTC-USDT-SWAP"
    )
    
    print(result)
    

#### Request parameters

Parameter | Type | Required | Description  
---|---|---|---  
instId | string | Yes | Instrument ID, eg: BTC-USDT-SWAP   
Only applicable to `FUTURES`, `SWAP`  
period | string | No | Bar size, the default is `5m`, e.g. [`5m/15m/30m/1H/2H/4H`]   
UTC+8 opening price k-line: [`6H/12H/1D/2D/3D/5D/1W/1M/3M`]   
UTC+0 opening price k-line: [`6Hutc/12Hutc/1Dutc/2Dutc/3Dutc/5Dutc/1Wutc/1Mutc/3Mutc`]  
end | string | No | Pagination of data to return records earlier than the requested `ts`  
begin | string | No | return records newer than the requested `ts`  
limit | string | No | Number of results per request. The maximum is `100`. The default is `100`.  
  
> Response example
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
            [
                "1701417600000",    // timestamp
                "731377.57500501",   // open interest (oi, contracts)
                "111",              // open interest (oiCcy, coin)
                "8888888"         // open interest (oiUsd, USD)
            ],
            [
                "1701417500000",    // timestamp
                "731377.57500501",   // open interest (oi, contracts)
                "111",              // open interest (oiCcy, coin)
                "8888888"         // open interest (oiUsd, USD)
            ]
        ]
    }
    
    

#### Response parameters

Parameter | Type | Description  
---|---|---  
ts | String | Timestamp, millisecond format of Unix timestamp, e.g. `1597026383085`  
oi | String | Open interest in the unit of contracts  
oiCcy | String | Open interest in the unit of crypto  
oiUsd | String | Open interest in the unit of USD  
  
The data returned will be arranged in an array like this: [ts, oi, oiCcy, oiUsd].

### Get taker volume

Retrieve the taker volume for both buyers and sellers.

#### Rate Limit: 5 requests per 2 seconds

#### Rate limit rule: IP

#### HTTP Request

`GET /api/v5/rubik/stat/taker-volume`

> Request Example
    
    
    GET /api/v5/rubik/stat/taker-volume?ccy=BTC&instType=SPOT
    
    
    
    import okx.TradingData as TradingData_api
    
    flag = "0"  # Production trading:0 , demo trading:1
    
    tradingDataAPI = TradingData_api.TradingDataAPI(flag=flag)
    
    # Retrieve the taker volume for both buyers and sellers
    result = tradingDataAPI.get_taker_volume(
        ccy="BTC",
        instType="SPOT"
    )
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
ccy | String | Yes | Currency  
instType | String | Yes | Instrument type  
`SPOT`  
`CONTRACTS`  
begin | String | No | Begin time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
end | String | No | End time, Unix timestamp format in milliseconds, e.g. `1597026383011`  
period | String | No | Period, the default is `5m`, e.g. [`5m`/`1H`/`1D`]   
`5m` granularity can only query data within two days at most  
`1H` granularity can only query data within 30 days at most   
`1D` granularity can only query data within 180 days at most  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            [
                "1630425600000",
                "7596.2651",
                "7149.4855"
            ],
            [
                "1630339200000",
                "5312.7876",
                "7002.7541"
            ]
        ],
        "msg": ""
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
ts | String | Timestamp  
sellVol | String | Sell volume  
buyVol | String | Buy volume  
The return value array order is: [ts,sellVol,buyVol] 

### Get contract taker volume

Retrieve the contract taker volume for both buyers and sellers. This endpoint can retrieve the latest 1,440 data entries.   

For period=1D, the data time range is up to January 1, 2024; for other periods, the data time range is up to early February 2024.

#### Rate limit: 5 requests per 2 seconds

#### Rate limit rule: IP + Instrument ID

#### HTTP Request

`GET /api/v5/rubik/stat/taker-volume-contract`

> Request example
    
    
    GET /api/v5/rubik/stat/taker-volume-contract?instId=BTC-USDT-SWAP
    
    
    
    import okx.TradingData as TradingData_api
    
    flag = "0"  # Production trading:0 , demo trading:1
    
    tradingDataAPI = TradingData_api.TradingDataAPI(flag=flag)
    
    # Retrieve the contract taker volume for both buyers and sellers
    result = tradingDataAPI.get_contract_taker_volume(
        instId="BTC-USDT-SWAP"
    )
    
    print(result)
    

#### Request parameters

Parameter | Type | Required | Description  
---|---|---|---  
instId | string | Yes | Instrument ID, eg: BTC-USDT-SWAP   
Only applicable to `FUTURES`, `SWAP`  
period | string | No | Bar size, the default is `5m`, e.g. [`5m/15m/30m/1H/2H/4H`]   
UTC+8 opening price k-line:[`6H/12H/1D/2D/3D/5D/1W/1M/3M`]   
UTC+0 opening price k-line: [`6Hutc/12Hutc/1Dutc/2Dutc/3Dutc/5Dutc/1Wutc/1Mutc/3Mutc`]  
unit | string | No | The unit of buy/sell volume, the default is `1`   
`0`: Crypto   
`1`: Contracts   
`2`: U  
end | string | No | return records earlier than the requested `ts`  
begin | string | No | return records newer than the requested `ts`  
limit | string | No | Number of results per request. The maximum is `100`. The default is `100`.  
  
> Response example
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
            [
                "1701417600000",    // timestamp
                "200",              // taker sell volume
                "380"               // taker buy volume
            ],
            [
                "1701417600000",    // timestamp
                "100",              // taker sell volume
                "300"               // taker buy volume
            ]
        ]
    }
    
    

#### Response parameters

Parameter | Type | Description  
---|---|---  
ts | String | Timestamp, millisecond format of Unix timestamp, e.g. `1597026383085`  
sellVol | String | taker sell volume  
buyVol | String | taker buy volume  
  
The data returned will be arranged in an array like this: [ts, sellVol, buyVol].

### Get margin long/short ratio

Retrieve the ratio of cumulative amount of quote currency to base currency.

#### Rate Limit: 5 requests per 2 seconds

#### Rate limit rule: IP

#### HTTP Request

`GET /api/v5/rubik/stat/margin/loan-ratio`

> Request Example
    
    
    GET /api/v5/rubik/stat/margin/loan-ratio?ccy=BTC
    
    
    
    import okx.TradingData as TradingData_api
    
    flag = "0"  # Production trading:0 , demo trading:1
    
    tradingDataAPI = TradingData_api.TradingDataAPI(flag=flag)
    
    # Retrieve the ratio of cumulative amount between currency margin quote currency and base currency
    result = tradingDataAPI.get_margin_lending_ratio(
        ccy="BTC",
    )
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
ccy | String | Yes | Currency  
begin | String | No | Begin time, e.g. `1597026383085`  
end | String | No | End time, e.g. `1597026383085`  
period | String | No | Period  
`m`: Minute, `H`: Hour, `D`: Day  
the default is `5m`, e.g. [`5m`/`1H`/`1D`]   
`5m` granularity can only query data within two days at most  
`1H` granularity can only query data within 30 days at most  
`1D` granularity can only query data within 180 days at most  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            [
                "1630492800000",
                "0.4614"
            ],
            [
                "1630492500000",
                "0.5767"
            ]
        ],
        "msg": ""
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
ts | String | Timestamp  
ratio | String | Margin lending ratio  
The return value array order is: [ts,ratio] 

### Get top traders contract long/short ratio

Retrieve the account net long/short ratio of a contract for top traders. Top traders refer to the top 5% of traders with the largest open position value. This endpoint can retrieve the latest 1,440 data entries. The data time range is up to March 22, 2024.

#### Rate limit: 5 requests per 2 seconds

#### Rate limit rule: IP + Instrument ID

#### HTTP Request

`GET /api/v5/rubik/stat/contracts/long-short-account-ratio-contract-top-trader`

> Request Example
    
    
    GET /api/v5/rubik/stat/contracts/long-short-account-ratio-contract-top-trader?instId=BTC-USDT-SWAP
    
    
    
    import okx.TradingData as TradingData_api
    
    flag = "0"  # Production trading:0 , demo trading:1
    
    tradingDataAPI = TradingData_api.TradingDataAPI(flag=flag)
    
    # Retrieve the top trader long short account ratio
    result = tradingDataAPI.get_top_trader_long_short_account_ratio(
        instId="BTC-USDT-SWAP"
    )
    
    print(result)
    

#### Request parameters

Parameter | Type | Required | Description  
---|---|---|---  
instId | string | Yes | Instrument ID, eg: BTC-USDT-SWAP   
Only applicable to `FUTURES`, `SWAP`  
period | string | No | Bar size, the default is `5m`, e.g. [`5m/15m/30m/1H/2H/4H`]   
UTC+8 opening price k-line: [`6H/12H/1D/2D/3D/5D/1W/1M/3M`]   
UTC+0 opening price k-line: [`6Hutc/12Hutc/1Dutc/2Dutc/3Dutc/5Dutc/1Wutc/1Mutc/3Mutc`]  
end | string | No | return records earlier than the requested `ts`  
begin | string | No | return records newer than the requested `ts`  
limit | string | No | Number of results per request. The maximum is `100`. The default is `100`.  
  
> Response example
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
            [
                "1701417600000",    // timestamp
                "1.1739"            // long/short account num ratio of top traders
            ],
            [
                "1701417600000",    // timestamp
                "0.1236"            // long/short account num ratio of top traders
            ],
        ]
    }
    
    

#### Response parameters

Parameter | Type | Description  
---|---|---  
ts | String | Timestamp, millisecond format of Unix timestamp, e.g. `1597026383085`  
longShortAcctRatio | String | Long/short account num ratio of top traders  
  
The data returned will be arranged in an array like this: [ts, longShortAcctRatio].

### Get top traders contract long/short ratio (by position)

Retrieve the position long/short ratio of a contract for top traders. Top traders refer to the top 5% of traders with the largest open position value. This endpoint can retrieve the latest 1,440 data entries. The data time range is up to March 22, 2024.

#### Rate limit: 5 requests per 2 seconds

#### Rate limit rule: IP + Instrument ID

#### HTTP Request

`GET /api/v5/rubik/stat/contracts/long-short-position-ratio-contract-top-trader`

> Request example
    
    
    GET /api/v5/rubik/stat/contracts/long-short-position-ratio-contract-top-trader?instId=BTC-USDT-SWAP
    
    
    
    import okx.TradingData as TradingData_api
    
    flag = "0"  # Production trading:0 , demo trading:1
    
    tradingDataAPI = TradingData_api.TradingDataAPI(flag=flag)
    
    # Retrieve the top trader long short position ratio
    result = tradingDataAPI.get_top_trader_long_short_position_ratio(
        instId="BTC-USDT-SWAP"
    )
    
    print(result)
    

#### Request parameters

Parameter | Type | Required | Description  
---|---|---|---  
instId | string | Yes | Instrument ID, e.g. `BTC-USDT-SWAP`   
Only applicable to `FUTURES`/`SWAP`  
period | string | No | Bar size, the default is `5m`, e.g. [`5m/15m/30m/1H/2H/4H`]   
UTC+8 opening price k-line: [`6H/12H/1D/2D/3D/5D/1W/1M/3M`]   
UTC+0 opening price k-line: [`6Hutc/12Hutc/1Dutc/2Dutc/3Dutc/5Dutc/1Wutc/1Mutc/3Mutc`]  
end | string | No | return records earlier than the requested `ts`  
begin | string | No | return records newer than the requested `ts`  
limit | string | No | Number of results per request. The maximum is `100`. The default is `100`.  
  
> Response example
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
            [
                "1701417600000",    // timestamp
                "1.1739"            // long/short position num ratio of top traders
            ],
            [
                "1701417600000",    // timestamp
                "0.1236"            // long/short position num ratio of top traders
            ],
        ]
    }
    
    

#### Response parameters

Parameter | Type | Description  
---|---|---  
ts | String | Timestamp, millisecond format of Unix timestamp, e.g. `1597026383085`  
longShortPosRatio | String | Long/short position ratio of top traders  
  
The data returned will be arranged in an array like this: [ts, longShortPosRatio].

### Get contract long/short ratio

Retrieve the account long/short ratio of a contract. This endpoint can retrieve the latest 1,440 data entries.   

For period=1D, the data time range is up to January 1, 2024; for other periods, the data time range is up to early February 2024.

#### Rate limit: 5 requests per 2 seconds

#### Rate limit rule: IP + Instrument ID

#### HTTP Request

`GET /api/v5/rubik/stat/contracts/long-short-account-ratio-contract`

> Request example
    
    
    GET /api/v5/rubik/stat/contracts/long-short-account-ratio-contract?instId=BTC-USDT-SWAP
    
    
    
    import okx.TradingData as TradingData_api
    
    flag = "0"  # Production trading:0 , demo trading:1
    
    tradingDataAPI = TradingData_api.TradingDataAPI(flag=flag)
    
    # Retrieve the account long short ratio of a contract
    result = tradingDataAPI.get_contract_long_short_ratio(
        instId="BTC-USDT-SWAP"
    )
    
    print(result)
    

#### Request parameters

Parameter | Type | Required | Description  
---|---|---|---  
instId | string | Yes | Instrument ID, eg: BTC-USDT-SWAP   
Only applicable to `FUTURES`, `SWAP`  
period | string | No | Bar size, the default is `5m`, e.g. [`5m/15m/30m/1H/2H/4H`]   
UTC+8 opening price k-line:[`6H/12H/1D/2D/3D/5D/1W/1M/3M`]   
UTC+0 opening price k-line: [`6Hutc/12Hutc/1Dutc/2Dutc/3Dutc/5Dutc/1Wutc/1Mutc/3Mutc`]  
end | string | No | return records earlier than the requested `ts`  
begin | string | No | return records newer than the requested `ts`  
limit | string | No | Number of results per request. The maximum is `100`. The default is `100`.  
  
> Response example
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
            [
                "1701417600000",    // timestamp
                "1.1739"            // long/short account num ratio of traders
            ],
            [
                "1701417600000",    // timestamp
                "0.1236"            // long/short account num ratio of traders
            ],
        ]
    }
    
    

#### Response parameters

Parameter | Type | Description  
---|---|---  
ts | String | Timestamp, millisecond format of Unix timestamp, e.g. `1597026383085`  
longShortAcctRatio | String | Long/short position num ratio of all traders  
  
The data returned will be arranged in an array like this: [ts, longAcctPosRatio].

### Get long/short ratio

Retrieve the ratio of users with net long vs net short positions for Expiry Futures and Perpetual Futures.

#### Rate Limit: 5 requests per 2 seconds

#### Rate limit rule: IP

#### HTTP Request

`GET /api/v5/rubik/stat/contracts/long-short-account-ratio`

> Request Example
    
    
    GET /api/v5/rubik/stat/contracts/long-short-account-ratio?ccy=BTC
    
    
    
    import okx.TradingData as TradingData_api
    
    flag = "0"  # Production trading:0 , demo trading:1
    
    tradingDataAPI = TradingData_api.TradingDataAPI(flag=flag)
    
    # Retrieve the ratio of users with net long vs net short positions for Expiry Futures and Perpetual Futures
    result = tradingDataAPI.get_long_short_ratio(
        ccy="BTC",
    )
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
ccy | String | Yes | Currency  
begin | String | No | Begin time, e.g. `1597026383085`  
end | String | No | End time, e.g. `1597026383011`  
period | String | No | Period, the default is `5m`, e.g. [`5m/1H/1D`]   
`5m` granularity can only query data within two days at most  
`1H` granularity can only query data within 30 days at most   
`1D` granularity can only query data within 180 days at most  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            [
                "1630502100000",
                "1.25"
            ]
        ],
        "msg": ""
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
ts | String | Timestamp  
ratio | String | Long/Short ratio  
The return value array order is: [ts,ratio] 

### Get contracts open interest and volume

Retrieve the open interest and trading volume for Expiry Futures and Perpetual Futures.

#### Rate Limit: 5 requests per 2 seconds

#### Rate limit rule: IP

#### HTTP Request

`GET /api/v5/rubik/stat/contracts/open-interest-volume`

> Request Example
    
    
    GET /api/v5/rubik/stat/contracts/open-interest-volume?ccy=BTC
    
    
    
    import okx.TradingData as TradingData_api
    
    flag = "0"  # Production trading:0 , demo trading:1
    
    tradingDataAPI = TradingData_api.TradingDataAPI(flag=flag)
    
    # Retrieve the open interest and trading volume for Expiry Futures and Perpetual Futures
    result = tradingDataAPI.get_contracts_interest_volume(
        ccy="BTC",
    )
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
ccy | String | Yes | Currency  
begin | String | No | Begin time, e.g. `1597026383085`  
end | String | No | End time, e.g. `1597026383011`  
period | String | No | Period, the default is `5m`, e.g. [`5m/1H/1D`]   
`5m` granularity can only query data within two days at most  
`1H` granularity can only query data within 30 days at most   
`1D` granularity can only query data within 180 days at most  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            [
                "1630502400000",
                "1713028741.6898",
                "39800873.554"
            ]
        ],
        "msg": ""
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
ts | String | Timestamp  
oi | String | Total open interest（USD）  
vol | String | Total trading volume（USD）  
The return value array order is: [ts,oi,vol] 

### Get options open interest and volume

Retrieve the open interest and trading volume for options.

#### Rate Limit: 5 requests per 2 seconds

#### Rate limit rule: IP

#### HTTP Request

`GET /api/v5/rubik/stat/option/open-interest-volume`

> Request Example
    
    
    GET /api/v5/rubik/stat/option/open-interest-volume?ccy=BTC
    
    
    
    import okx.TradingData as TradingData_api
    
    flag = "0"  # Production trading:0 , demo trading:1
    
    tradingDataAPI = TradingData_api.TradingDataAPI(flag=flag)
    
    # Retrieve the open interest and trading volume for options
    result = tradingDataAPI.get_options_interest_volume(
        ccy="BTC",
    )
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
ccy | String | Yes | Currency  
period | String | No | Period, the default is `8H`. e.g. [`8H/1D`]   
Each granularity can only query 72 pieces of data at the earliest  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            [
                "1630368000000",
                "3458.1000",
                "78.8000"
            ]
        ],
        "msg": ""
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
ts | String | Timestamp  
oi | String | Total open interest , unit in `ccy` (in request parameter)  
vol | String | Total trading volume , unit in `ccy` (in request parameter)  
The return value array order is: [ts,oi,vol] 

### Get put/call ratio

Retrieve the open interest ratio and trading volume ratio of calls vs puts.

#### Rate Limit: 5 requests per 2 seconds

#### Rate limit rule: IP

#### HTTP Request

`GET /api/v5/rubik/stat/option/open-interest-volume-ratio`

> Request Example
    
    
    GET /api/v5/rubik/stat/option/open-interest-volume-ratio?ccy=BTC
    
    
    
    import okx.TradingData as TradingData_api
    
    flag = "0"  # Production trading:0 , demo trading:1
    
    tradingDataAPI = TradingData_api.TradingDataAPI(flag=flag)
    
    # Retrieve the open interest ratio and trading volume ratio of calls vs puts
    result = tradingDataAPI.get_put_call_ratio(
        ccy="BTC",
    )
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
ccy | String | Yes | Currency  
period | String | No | Period, the default is `8H`. e.g. [`8H/1D`]   
Each granularity can only query 72 pieces of data at the earliest  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            [
                "1630512000000",
                "2.7261",
                "2.3447"
            ],
            [
                "1630425600000",
                "2.8101",
                "2.3438"
            ]
        ],
        "msg": ""
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
ts | String | Timestamp of data generation time  
oiRatio | String | Long/Short open interest ratio  
volRatio | String | Long/Short trading volume ratio  
The return value array order is: [ts,oiRatio,volRatio] 

### Get open interest and volume (expiry)

Retrieve the open interest and trading volume of calls and puts for each upcoming expiration.

#### Rate Limit: 5 requests per 2 seconds

#### Rate limit rule: IP

#### HTTP Request

`GET /api/v5/rubik/stat/option/open-interest-volume-expiry`

> Request Example
    
    
    GET /api/v5/rubik/stat/option/open-interest-volume-expiry?ccy=BTC
    
    
    
    import okx.TradingData as TradingData_api
    
    flag = "0"  # Production trading:0 , demo trading:1
    
    tradingDataAPI = TradingData_api.TradingDataAPI(flag=flag)
    
    # Retrieve the open interest and trading volume of calls and puts for each upcoming expiration
    result = tradingDataAPI.get_interest_volume_expiry(
        ccy="BTC"
    )
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
ccy | String | Yes | Currency  
period | String | No | Period, the default is `8H`. e.g. [`8H/1D`]   
Each granularity can provide only one latest piece of data  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            [
                "1630540800000",
                "20210902",
                "6.4",
                "18.4",
                "0.7",
                "0.4"
            ],
            [
                "1630540800000",
                "20210903",
                "47",
                "36.6",
                "1",
                "10.7"
            ]
        ],
        "msg": ""
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
ts | String | Timestamp  
expTime | String | Contract expiry date, the format is `YYYYMMDD`, e.g. `20210623`  
callOI | String | Total call open interest (`coin` as the unit)  
putOI | String | Total put open interest (`coin` as the unit)  
callVol | String | Total call trading volume (`coin` as the unit)  
putVol | String | Total put trading volume (`coin` as the unit)  
The return value array order is: [ts,expTime,callOI,putOI,callVol,putVol] 

### Get open interest and volume (strike)

Retrieve the taker volume for both buyers and sellers of calls and puts.

#### Rate Limit: 5 requests per 2 seconds

#### Rate limit rule: IP

#### HTTP Request

`GET /api/v5/rubik/stat/option/open-interest-volume-strike`

> Request Example
    
    
    GET /api/v5/rubik/stat/option/open-interest-volume-strike?ccy=BTC&expTime=20210901
    
    
    
    import okx.TradingData as TradingData_api
    
    flag = "0"  # Production trading:0 , demo trading:1
    
    tradingDataAPI = TradingData_api.TradingDataAPI(flag=flag)
    
    # Retrieve the taker volume for both buyers and sellers of calls and puts
    result = tradingDataAPI.get_interest_volume_strike(
        ccy="BTC",
        expTime="20210623"
    )
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
ccy | String | Yes | Currency  
expTime | String | Yes | Contract expiry date, the format is `YYYYMMdd`, e.g. `20210623`  
period | String | No | Period, the default is `8H`. e.g. [`8H/1D`]   
Each granularity can provide only one latest piece of data  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            [
                "1630540800000",
                "10000",
                "0",
                "0.5",
                "0",
                "0"
            ],
            [
                "1630540800000",
                "14000",
                "0",
                "5.2",
                "0",
                "0"
            ]
        ],
        "msg": ""
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
ts | String | Timestamp  
strike | String | Strike price  
callOI | String | Total call open interest (`coin` as the unit)  
putOI | String | Total put open interest (`coin` as the unit)  
callVol | String | Total call trading volume (`coin` as the unit)  
putVol | String | Total put trading volume (`coin` as the unit)  
The return value array order is: [ts,strike,callOI,putOI,callVol,putVol] 

### Get taker flow

This shows the relative buy/sell volume for calls and puts. It shows whether traders are bullish or bearish on price and volatility.

#### Rate Limit: 5 requests per 2 seconds

#### Rate limit rule: IP

#### HTTP Request

`GET /api/v5/rubik/stat/option/taker-block-volume`

> Request Example
    
    
    GET /api/v5/rubik/stat/option/taker-block-volume?ccy=BTC
    
    
    
    import okx.TradingData as TradingData_api
    
    flag = "0"  # Production trading:0 , demo trading:1
    
    tradingDataAPI = TradingData_api.TradingDataAPI(flag=flag)
    
    # This shows the relative buy/sell volume for calls and puts. It shows whether traders are bullish or bearish on price and volatility
    result = tradingDataAPI.get_taker_block_volume(
        ccy="BTC",
    )
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
ccy | String | Yes | currency  
period | String | No | period, the default is `8H`. e.g. [`8H/1D`]   
Each granularity can provide only one latest piece of data  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            "1630512000000",
            "8.55",
            "67.3",
            "16.05",
            "16.3",
            "126.4",
            "40.7"
        ],
        "msg": ""
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
ts | String | Timestamp  
callBuyVol | String | call option buy volume, in settlement currency  
callSellVol | String | call option sell volume, in settlement currency  
putBuyVol | String | put option buy volume, in settlement currency  
putSellVol | String | put option sell volume, in settlement currency  
callBlockVol | String | call block volume  
putBlockVol | String | put block volume  
The return value array order is: [ts,callBuyVol,callSellVol,putBuyVol,putSellVol,callBlockVol,putBlockVol]

---

# 交易大数据

## REST API   
  
### 获取交易大数据支持币种 

获取支持交易大数据的币种

#### 限速：5次/2s

#### 限速规则：IP

#### HTTP请求

`GET /api/v5/rubik/stat/trading-data/support-coin`

> 请求示例
    
    
    GET /api/v5/rubik/stat/trading-data/support-coin
    
    
    
    import okx.TradingData as TradingData_api
    
    flag = "0"  # 实盘: 0, 模拟盘: 1
    
    tradingDataAPI = TradingData_api.TradingDataAPI(flag=flag)
    
    # 获取交易大数据支持币种
    result = tradingDataAPI.get_support_coin()
    print(result)
    

> 返回结果
    
    
    {
        "code": "0",
        "data": {
            "contract": [
                "ADA",
                "BTC",
            ],
            "option": [
                "BTC"
            ],
            "spot": [
                "ADA",
                "BTC",
            ]
        },
        "msg": ""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
contract | Array of strings | 合约交易大数据接口功能支持的币种  
option | Array of strings | 期权交易大数据接口功能支持的币种  
spot | Array of strings | 现货交易大数据接口功能支持的币种  
  
### 获取合约持仓量历史 

获取交割及永续合约的历史持仓量数据。每个粒度最多可获取最近1,440条数据。  

对于时间粒度period=1D，数据时间范围最早至2024年1月1日；对于其他时间粒度period，最早至2024年2月初。

#### 限速：10次/2s

#### 限速规则：IP + Instrument ID

#### HTTP请求

`GET /api/v5/rubik/stat/contracts/open-interest-history`

> 请求示例
    
    
    GET /api/v5/rubik/stat/contracts/open-interest-history?instId=BTC-USDT-SWAP
    
    
    
    
    import okx.TradingData as TradingData_api
    
    flag = "0"  # 实盘: 0, 模拟盘: 1
    
    tradingDataAPI = TradingData_api.TradingDataAPI(flag=flag)
    
    # 获取持仓量历史
    result = tradingDataAPI.get_open_interest_history(
        instId="BTC-USDT-SWAP"
    )
    
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
instId | string | 是 | 产品ID，如 BTC-USDT-SWAP   
仅适用于`交割`/`永续`  
period | string | 否 | 时间粒度，默认值`5m`, 如 [`5m/15m/30m/1H/2H/4H`]   
UTC+8开盘价k线：[`6H/12H/1D/2D/3D/5D/1W/1M/3M`]   
UTC+0开盘价k线： [`6Hutc/12Hutc/1Dutc/2Dutc/3Dutc/5Dutc/1Wutc/1Mutc/3Mutc`]  
end | string | 否 | 筛选的结束时间戳 ts，Unix 时间戳为毫秒数格式，如 `1597027383085`  
begin | string | 否 | 筛选的开始时间戳 ts，Unix 时间戳为毫秒数格式，如 `1597026383085`  
limit | string | 否 | 分页返回的结果集数量，最大为`100`，不填默认返回`100`条  
  
> 返回结果
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
            [
                "1701417600000",    // timestamp
                "731377.57500501",   // open interest (oi, contracts)
                "111",              // open interest (oiCcy, coin)
                "8888888"         // open interest (oiUsd, USD)
            ],
            [
                "1701417500000",    // timestamp
                "731377.57500501",   // open interest (oi, contracts)
                "111",              // open interest (oiCcy, coin)
                "8888888"         // open interest (oiUsd, USD)
            ]
        ]
    }
    
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
ts | String | 时间戳，Unix时间戳的毫秒数格式，如 `1597026383085`  
oi | String | 合约单位的持仓量  
oiCcy | String | 币种单位的持仓量  
oiUsd | String | USD单位的持仓量  
  
返回值数组顺序分别为是：[ts, oi, oiCcy, oiUsd]

### 获取主动买入/卖出情况 

获取taker主动买入和卖出的交易量

#### 限速：5次/2s

#### 限速规则：IP

#### HTTP请求

`GET /api/v5/rubik/stat/taker-volume`

> 请求示例
    
    
    GET /api/v5/rubik/stat/taker-volume?ccy=BTC&instType=SPOT
    
    
    
    import okx.TradingData as TradingData_api
    
    flag = "0"  # 实盘: 0, 模拟盘: 1
    
    tradingDataAPI = TradingData_api.TradingDataAPI(flag=flag)
    
    # 获取主动买入/卖出情况
    result = tradingDataAPI.get_taker_volume(
        ccy="BTC",
        instType="SPOT"
    )
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
ccy | String | 是 | 币种  
instType | String | 是 | 产品类型  
`SPOT`：币币  
`CONTRACTS`：衍生品  
begin | String | 否 | 开始时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
end | String | 否 | 结束时间，Unix时间戳的毫秒数格式，如 `1597026383011`  
period | String | 否 | 时间粒度，默认值`5m`。支持[`5m`/`1H`/`1D`]   
`5m`粒度最多只能查询两天之内的数据  
`1H`粒度最多只能查询30天之内的数据  
`1D`粒度最多只能查询180天之内的数据  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            [
                "1630425600000",
                "7596.2651",
                "7149.4855"
            ],
            [
                "1630339200000",
                "5312.7876",
                "7002.7541"
            ]
        ],
        "msg": ""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
ts | String | 数据产生时间  
sellVol | String | 卖出量  
buyVol | String | 买入量  
返回值数组顺序分别为是：[ts,sellVol,buyVol] 

### 获取合约主动买入/卖出情况 

获取合约维度taker主动买入和卖出的交易量。每个粒度最多可获取最近1,440条数据。  

对于时间粒度period=1D，数据时间范围最早至2024年1月1日；对于其他时间粒度period，最早至2024年2月初。

#### 限速： 5次/2s

#### 限速规则： IP + Instrument ID

#### HTTP请求

`GET /api/v5/rubik/stat/taker-volume-contract`

> 请求示例
    
    
    GET /api/v5/rubik/stat/taker-volume-contract?instId=BTC-USDT-SWAP
    
    
    
    import okx.TradingData as TradingData_api
    
    flag = "0"  # 实盘: 0, 模拟盘: 1
    
    tradingDataAPI = TradingData_api.TradingDataAPI(flag=flag)
    
    # 获取合约taker主动买入和卖出的交易量
    result = tradingDataAPI.get_contract_taker_volume(
        instId="BTC-USDT-SWAP"
    )
    
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
instId | string | 是 | 产品ID，如 BTC-USDT   
仅适用于`交割`/`永续`  
period | string | 否 | 时间粒度，默认值`5m`, 如 [`5m/15m/30m/1H/2H/4H`]   
UTC+8开盘价k线：[`6H/12H/1D/2D/3D/5D/1W/1M/3M`]   
UTC+0开盘价k线： [`6Hutc/12Hutc/1Dutc/2Dutc/3Dutc/5Dutc/1Wutc/1Mutc/3Mutc`]  
unit | string | 否 | 买入、卖出的单位，默认值是`1`   
`0`: 币   
`1`: 合约   
`2`: U  
end | string | 否 | 筛选的结束时间戳 ts，Unix 时间戳为毫秒数格式，如 `1597027383085`  
begin | string | 否 | 筛选的开始时间戳 ts，Unix 时间戳为毫秒数格式，如 `1597026383085`  
limit | string | 否 | 分页返回的结果集数量，最大为100，不填默认返回100条  
  
> 返回结果
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
            [
                "1701417600000",    // timestamp
                "200",              // taker sell volume
                "380"               // taker buy volume
            ],
            [
                "1701417600000",    // timestamp
                "100",              // taker sell volume
                "300"               // taker buy volume
            ]
        ]
    }
    
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
ts | String | 时间戳，Unix时间戳的毫秒数格式，如 `1597026383085`  
sellVol | String | 卖出量  
buyVol | String | 买入量  
  
返回值数组顺序分别为是：[ts, sellVol, buyVol]

### 获取杠杆多空比 

获取借入计价货币与借入交易货币的累计数额比值。

#### 限速：5次/2s

#### 限速规则：IP

#### HTTP请求

`GET /api/v5/rubik/stat/margin/loan-ratio`

> 请求示例
    
    
    GET /api/v5/rubik/stat/margin/loan-ratio?ccy=BTC
    
    
    
    import okx.TradingData as TradingData_api
    
    flag = "0"  # 实盘: 0, 模拟盘: 1
    
    tradingDataAPI = TradingData_api.TradingDataAPI(flag=flag)
    
    # 获取杠杆多空比
    result = tradingDataAPI.get_margin_lending_ratio(
        ccy="BTC",
    )
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
ccy | String | 是 | 币种  
begin | String | 否 | 开始时间，如 `1597026383085`  
end | String | 否 | 结束时间，如 `1597026383011`  
period | String | 否 | 时间粒度  
`m`：分钟，`H`：小时，`D`：天  
默认值`5m`，支持[`5m`/`1H`/`1D`]   
`5m`粒度最多只能查询两天之内的数据  
`1H`粒度最多只能查询30天之内的数据   
`1D`粒度最多只能查询180天之内的数据  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            [
                "1630492800000",
                "0.4614"
            ],
            [
                "1630492500000",
                "0.5767"
            ]
        ],
        "msg": ""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
ts | String | 数据产生时间  
ratio | String | 多空比值  
返回值数组顺序分别为是：[ts,ratio] 

### 获取精英交易员合约多空持仓人数比 

获取精英交易员交割永续净开多持仓用户数与净开空持仓用户数的比值。精英交易员指持仓价值前5%的用户。每个粒度最多可获取最近1,440条数据。数据时间范围最早至2024年3月22日。

#### 限速： 5次/2s

#### 限速规则： IP + Instrument ID

#### HTTP请求

`GET /api/v5/rubik/stat/contracts/long-short-account-ratio-contract-top-trader`

> 请求示例
    
    
    GET /api/v5/rubik/stat/contracts/long-short-account-ratio-contract-top-trader?instId=BTC-USDT-SWAP
    
    
    
    import okx.TradingData as TradingData_api
    
    flag = "0"  # 实盘: 0, 模拟盘: 1
    
    tradingDataAPI = TradingData_api.TradingDataAPI(flag=flag)
    
    # 获取精英交易员合约多空持仓人数比
    result = tradingDataAPI.get_top_trader_long_short_account_ratio(
        instId="BTC-USDT-SWAP"
    )
    
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
instId | string | 是 | 产品ID，如 BTC-USDT-SWAP   
仅适用于`交割`/`永续`  
period | string | 否 | 时间粒度，默认值`5m`, 如 [`5m/15m/30m/1H/2H/4H`]   
UTC+8开盘价k线：[`6H/12H/1D/2D/3D/5D/1W/1M/3M`]   
UTC+0开盘价k线： [`6Hutc/12Hutc/1Dutc/2Dutc/3Dutc/5Dutc/1Wutc/1Mutc/3Mutc`]  
end | string | 否 | 筛选的结束时间戳 ts，Unix 时间戳为毫秒数格式，如 `1597027383085`  
begin | string | 否 | 筛选的开始时间戳 ts，Unix 时间戳为毫秒数格式，如 `1597026383085`  
limit | string | 否 | 分页返回的结果集数量，最大为100，不填默认返回100条  
  
> 返回结果
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
            [
                "1701417600000",    // timestamp
                "1.1739"            // long/short account num ratio of top traders
            ],
            [
                "1701417600000",    // timestamp
                "0.1236"            // long/short account num ratio of top traders
            ],
        ]
    }
    
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
ts | String | 时间戳，Unix时间戳的毫秒数格式，如 `1597026383085`  
longShortAcctRatio | String | 多空人数比  
  
返回值数组顺序分别为是：[ts, longShortAcctRatio]

### 获取精英交易员合约多空持仓仓位比 

获取交割永续开多、开空仓位占总持仓的比值。精英交易员指持仓价值前5%的用户。每个粒度最多可获取最近1,440条数据。数据时间范围最早至2024年3月22日。

#### 限速： 5次/2s

#### 限速规则： IP + Instrument ID

#### HTTP请求

`GET /api/v5/rubik/stat/contracts/long-short-position-ratio-contract-top-trader`

> 请求示例
    
    
    GET /api/v5/rubik/stat/contracts/long-short-position-ratio-contract-top-trader?instId=BTC-USDT-SWAP
    
    
    
    import okx.TradingData as TradingData_api
    
    flag = "0"  # 实盘: 0, 模拟盘: 1
    
    tradingDataAPI = TradingData_api.TradingDataAPI(flag=flag)
    
    # 获取精英交易员合约多空持仓仓位比
    result = tradingDataAPI.get_top_trader_long_short_position_ratio(
        instId="BTC-USDT-SWAP"
    )
    
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
instId | string | 是 | 产品ID，如 `BTC-USDT-SWAP`   
仅适用于`交割`/`永续`  
period | string | 否 | 时间粒度，默认值`5m`, 如 [`5m/15m/30m/1H/2H/4H`]   
UTC+8开盘价k线：[`6H/12H/1D/2D/3D/5D/1W/1M/3M`]   
UTC+0开盘价k线： [`6Hutc/12Hutc/1Dutc/2Dutc/3Dutc/5Dutc/1Wutc/1Mutc/3Mutc`]  
end | string | 否 | 筛选的结束时间戳 ts，Unix 时间戳为毫秒数格式，如 `1597027383085`  
begin | string | 否 | 筛选的开始时间戳 ts，Unix 时间戳为毫秒数格式，如 `1597026383085`  
limit | string | 否 | 分页返回的结果集数量，最大为100，不填默认返回100条  
  
> 返回结果
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
            [
                "1701417600000",    // timestamp
                "1.1739"            // long/short position num ratio of top traders
            ],
            [
                "1701417600000",    // timestamp
                "0.1236"            // long/short position num ratio of top traders
            ],
        ]
    }
    
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
ts | String | 时间戳，Unix时间戳的毫秒数格式，如 `1597026383085`  
longShortPosRatio | String | 多空仓位占总持仓比值  
  
返回值数组顺序分别为是：[ts, longShortPosRatio]

### 获取合约多空持仓人数比 

获取交割永续净开多持仓用户数与净开空持仓用户数的比值。每个粒度最多可获取最近1,440条数据。  

对于时间粒度period=1D，数据时间范围最早至2024年1月1日；对于其他时间粒度period，最早至2024年2月初。

#### 限速： 5次/2s

#### 限速规则： IP + Instrument ID

#### HTTP请求

`GET /api/v5/rubik/stat/contracts/long-short-account-ratio-contract`

> 请求示例
    
    
    GET /api/v5/rubik/stat/contracts/long-short-account-ratio-contract?instId=BTC-USDT-SWAP
    
    
    
    import okx.TradingData as TradingData_api
    
    flag = "0"  # 实盘: 0, 模拟盘: 1
    
    tradingDataAPI = TradingData_api.TradingDataAPI(flag=flag)
    
    # 获取合约净开多持仓用户数与净开空持仓用户数的比值
    result = tradingDataAPI.get_contract_long_short_ratio(
        instId="BTC-USDT-SWAP"
    )
    
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
instId | string | 是 | 产品ID，如 BTC-USDT   
仅适用于`交割`/`永续`  
period | string | 否 | 时间粒度，默认值`5m`, 如 [`5m/15m/30m/1H/2H/4H`]   
UTC+8开盘价k线：[`6H/12H/1D/2D/3D/5D/1W/1M/3M`]   
UTC+0开盘价k线： [`6Hutc/12Hutc/1Dutc/2Dutc/3Dutc/5Dutc/1Wutc/1Mutc/3Mutc`]  
end | string | 否 | 筛选的结束时间戳 ts，Unix 时间戳为毫秒数格式，如 `1597027383085`  
begin | string | 否 | 筛选的开始时间戳 ts，Unix 时间戳为毫秒数格式，如 `1597026383085`  
limit | string | 否 | 分页返回的结果集数量，最大为100，不填默认返回100条  
  
> 返回结果
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
            [
                "1701417600000",    // timestamp
                "1.1739"            // long/short account num ratio of traders
            ],
            [
                "1701417600000",    // timestamp
                "0.1236"            // long/short account num ratio of traders
            ],
        ]
    }
    
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
ts | String | 时间戳，Unix时间戳的毫秒数格式，如 `1597026383085`  
longShortAcctRatio | String | 多空人数比  
  
返回值数组顺序分别为是：[ts, longAcctPosRatio]

### 获取多空持仓人数比 

获取交割永续净开多持仓用户数与净开空持仓用户数的比值。

#### 限速：5次/2s

#### 限速规则：IP

#### HTTP请求

`GET /api/v5/rubik/stat/contracts/long-short-account-ratio`

> 请求示例
    
    
    GET /api/v5/rubik/stat/contracts/long-short-account-ratio?ccy=BTC
    
    
    
    import okx.TradingData as TradingData_api
    
    flag = "0"  # 实盘: 0, 模拟盘: 1
    
    tradingDataAPI = TradingData_api.TradingDataAPI(flag=flag)
    
    # 获取合约多空持仓人数比
    result = tradingDataAPI.get_long_short_ratio(
        ccy="BTC",
    )
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
ccy | String | 是 | 币种  
begin | String | 否 | 开始时间，如 `1597026383085`  
end | String | 否 | 结束时间，如 `1597026383011`  
period | String | 否 | 时间粒度，默认值`5m`。支持[5m/1H/1D]   
`5m`粒度最多只能查询两天之内的数据  
`1H`粒度最多只能查询30天之内的数据   
`1D`粒度最多只能查询180天之内的数据  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            [
                "1630502100000",
                "1.25"
            ]
        ],
        "msg": ""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
ts | String | 数据产生时间  
ratio | String | 多空人数比  
返回值数组顺序分别为是：[ts,ratio] 

### 获取合约持仓量及交易量 

获取交割永续的持仓量和交易量。

#### 限速：5次/2s

#### 限速规则：IP

#### HTTP请求

`GET /api/v5/rubik/stat/contracts/open-interest-volume`

> 请求示例
    
    
    GET /api/v5/rubik/stat/contracts/open-interest-volume?ccy=BTC
    
    
    
    import okx.TradingData as TradingData_api
    
    flag = "0"  # 实盘: 0, 模拟盘: 1
    
    tradingDataAPI = TradingData_api.TradingDataAPI(flag=flag)
    
    # 获取合约持仓量及交易量
    result = tradingDataAPI.get_contracts_interest_volume(
        ccy="BTC",
    )
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
ccy | String | 是 | 币种  
begin | String | 否 | 开始时间，如 `1597026383085`  
end | String | 否 | 结束时间，如 `1597026383011`  
period | String | 否 | 时间粒度，默认值`5m`。支持[5m/1H/1D]   
`5m`粒度最多只能查询两天之内的数据  
`1H`粒度最多只能查询30天之内的数据   
`1D`粒度最多只能查询180天之内的数据  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            [
                "1630502400000",
                "1713028741.6898",
                "39800873.554"
            ]
        ],
        "msg": ""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
ts | String | 数据产生时间  
oi | String | 持仓总量（USD）  
vol | String | 交易总量（USD）  
返回值数组顺序分别为是：[ts,oi,vol] 

### 获取期权持仓量及交易量 

获取期权的持仓量和交易量。

#### 限速：5次/2s

#### 限速规则：IP

#### HTTP请求

`GET /api/v5/rubik/stat/option/open-interest-volume`

> 请求示例
    
    
    GET /api/v5/rubik/stat/option/open-interest-volume?ccy=BTC
    
    
    
    import okx.TradingData as TradingData_api
    
    flag = "0"  # 实盘: 0, 模拟盘: 1
    
    tradingDataAPI = TradingData_api.TradingDataAPI(flag=flag)
    
    # 获取期权持仓量及交易量
    result = tradingDataAPI.get_options_interest_volume(
        ccy="BTC",
    )
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
ccy | String | 是 | 币种  
period | String | 否 | 时间粒度，默认值`8H`。支持[`8H/1D`]   
每个粒度最多只能查询72条数据  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            [
                "1630368000000",
                "3458.1000",
                "78.8000"
            ]
        ],
        "msg": ""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
ts | String | 数据产生时间  
oi | String | 持仓总量，单位为请求参数的`ccy`  
vol | String | 交易总量，单位为请求参数的`ccy`  
返回值数组顺序分别为是：[ts,oi,vol] 

### 看涨/看跌期权合约 持仓总量比/交易总量比 

获取看涨期权和看跌期权的持仓量比值，以及交易量比值。

#### 限速：5次/2s

#### 限速规则：IP

#### HTTP请求

`GET /api/v5/rubik/stat/option/open-interest-volume-ratio`

> 请求示例
    
    
    GET /api/v5/rubik/stat/option/open-interest-volume-ratio?ccy=BTC
    
    
    
    import okx.TradingData as TradingData_api
    
    flag = "0"  # 实盘: 0, 模拟盘: 1
    
    tradingDataAPI = TradingData_api.TradingDataAPI(flag=flag)
    
    # 看涨/看跌期权合约 持仓总量比/交易总量比
    result = tradingDataAPI.get_put_call_ratio(
        ccy="BTC",
    )
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
ccy | String | 是 | 币种  
period | String | 否 | 时间粒度，默认值`8H`。支持[`8H/1D`]   
每个粒度最多只能查询72条数据  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            [
                "1630512000000",
                "2.7261",
                "2.3447"
            ],
            [
                "1630425600000",
                "2.8101",
                "2.3438"
            ]
        ],
        "msg": ""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
ts | String | 数据产生时间  
oiRatio | String | 看涨/看跌 持仓总量比  
volRatio | String | 看涨/看跌 交易总量比  
返回值数组顺序分别为是：[ts,oiRatio,volRatio] 

### 看涨看跌持仓总量及交易总量（按到期日分） 

获取每个到期日上看涨期权和看跌期权的持仓量和交易量。

#### 限速：5次/2s

#### 限速规则：IP

#### HTTP请求

`GET /api/v5/rubik/stat/option/open-interest-volume-expiry`

> 请求示例
    
    
    GET /api/v5/rubik/stat/option/open-interest-volume-expiry?ccy=BTC
    
    
    
    import okx.TradingData as TradingData_api
    
    flag = "0"  # 实盘: 0, 模拟盘: 1
    
    tradingDataAPI = TradingData_api.TradingDataAPI(flag=flag)
    
    # 看涨看跌持仓总量及交易总量（按到期日分）
    result = tradingDataAPI.get_interest_volume_expiry(
        ccy="BTC"
    )
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
ccy | String | 是 | 币种  
period | String | 否 | 时间粒度，默认值`8H`。支持[`8H/1D`]   
每个粒度仅展示最新的一份数据  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            [
                "1630540800000",
                "20210902",
                "6.4",
                "18.4",
                "0.7",
                "0.4"
            ],
            [
                "1630540800000",
                "20210903",
                "47",
                "36.6",
                "1",
                "10.7"
            ]
        ],
        "msg": ""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
ts | String | 数据产生时间  
expTime | String | 到期日（格式: YYYYMMDD，如 "20210623"）  
callOI | String | 看涨持仓总量（以`币`为单位）  
putOI | String | 看跌持仓总量（以`币`为单位）  
callVol | String | 看涨交易总量（以`币`为单位）  
putVol | String | 看跌交易总量（以`币`为单位）  
返回值数组顺序分别为是：[ts,expTime,callOI,putOI,callVol,putVol] 

### 看涨看跌持仓总量及交易总量（按执行价格分） 

获取看涨期权和看跌期权的taker主动买入和卖出的交易量。

#### 限速：5次/2s

#### 限速规则：IP

#### HTTP请求

`GET /api/v5/rubik/stat/option/open-interest-volume-strike`

> 请求示例
    
    
    GET /api/v5/rubik/stat/option/open-interest-volume-strike?ccy=BTC&expTime=20210901
    
    
    
    import okx.TradingData as TradingData_api
    
    flag = "0"  # 实盘: 0, 模拟盘: 1
    
    tradingDataAPI = TradingData_api.TradingDataAPI(flag=flag)
    
    # 看涨看跌持仓总量及交易总量（按执行价格分）
    result = tradingDataAPI.get_interest_volume_strike(
        ccy="BTC",
        expTime="20210623"
    )
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
ccy | String | 是 | 币种  
expTime | String | 是 | 到期日（格式: `YYYYMMdd`，如 "20210623"）  
period | String | 否 | 时间粒度，默认值`8H`。支持[`8H/1D`]   
每个粒度仅展示最新的一份数据  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            [
                "1630540800000",
                "10000",
                "0",
                "0.5",
                "0",
                "0"
            ],
            [
                "1630540800000",
                "14000",
                "0",
                "5.2",
                "0",
                "0"
            ]
        ],
        "msg": ""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
ts | String | 数据产生时间  
strike | String | 执行价格  
callOI | String | 看涨持仓总量（以`币`为单位）  
putOI | String | 看跌持仓总量（以`币`为单位）  
callVol | String | 看涨交易总量（以`币`为单位）  
putVol | String | 看跌交易总量（以`币`为单位）  
返回值数组顺序分别为是：[ts,strike,callOI,putOI,callVol,putVol] 

### 看跌/看涨期权合约 主动买入/卖出量 

该指标展示某一时刻，单位时间内看跌/看涨期权的主动（taker）买入/卖出交易量

#### 限速：5次/2s

#### 限速规则：IP

#### HTTP请求

`GET /api/v5/rubik/stat/option/taker-block-volume`

> 请求示例
    
    
    GET /api/v5/rubik/stat/option/taker-block-volume?ccy=BTC
    
    
    
    import okx.TradingData as TradingData_api
    
    flag = "0"  # 实盘: 0, 模拟盘: 1
    
    tradingDataAPI = TradingData_api.TradingDataAPI(flag=flag)
    
    # 看跌/看涨期权合约 主动买入/卖出量
    result = tradingDataAPI.get_taker_block_volume(
        ccy="BTC",
    )
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
ccy | String | 是 | 币种  
period | String | 否 | 时间粒度，默认值`8H`。支持[`8H/1D`]   
每个粒度仅展示最新的一份数据  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            "1630512000000",
            "8.55",
            "67.3",
            "16.05",
            "16.3",
            "126.4",
            "40.7"
        ],
        "msg": ""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
ts | String | 数据产生时间  
callBuyVol | String | 看涨买入量 以结算货币为单位  
callSellVol | String | 看涨卖出量 以结算货币为单位  
putBuyVol | String | 看跌买入量 以结算货币为单位  
putSellVol | String | 看跌卖出量 以结算货币为单位  
callBlockVol | String | 看涨大单  
putBlockVol | String | 看跌大单  
返回值数组顺序分别为是：[ts,callBuyVol,callSellVol,putBuyVol,putSellVol,callBlockVol,putBlockVol]