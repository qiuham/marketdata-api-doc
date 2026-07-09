---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#public-data
anchor_id: public-data
api_type: API
updated_at: 2026-07-09 19:38:10.476766
---

# Public Data

The API endpoints of `Public Data` do not require authentication. 

## REST API

### Get instruments

Retrieve a list of instruments with open contracts for OKX. Retrieve available instruments info of current account, please refer to [Get instruments](/docs-v5/en/#trading-account-rest-api-get-instruments).

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: IP + Instrument Type

#### HTTP Request

`GET /api/v5/public/instruments`

> Request Example
    
    
    GET /api/v5/public/instruments?instType=SPOT
    
    
    
    import okx.PublicData as PublicData
    
    flag = "0"  # Production trading: 0, Demo trading: 1
    
    publicDataAPI = PublicData.PublicAPI(flag=flag)
    
    # Retrieve a list of instruments with open contracts
    result = publicDataAPI.get_instruments(
        instType="SPOT"
    )
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
instType | String | Yes | Instrument type  
`SPOT`: Spot  
`MARGIN`: Margin  
`SWAP`: Perpetual Futures  
`FUTURES`: Expiry Futures  
`OPTION`: Option  
`EVENTS`: Event Contracts  
seriesId | String | Conditional | Series ID, e.g. `BTC-ABOVE-DAILY`. Required when instType is `EVENTS`  
instFamily | String | Conditional | Instrument family  
Only applicable to `FUTURES`/`SWAP`/`OPTION`. If instType is `OPTION`, `instFamily` is required.  
instId | String | No | Instrument ID  
  
> Response Example
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
          {
                "alias": "",
                "auctionEndTime": "",
                "baseCcy": "BTC",
                "category": "1",
                "ctMult": "",
                "ctType": "",
                "ctVal": "",
                "ctValCcy": "",
                "contTdSwTime": "1704876947000",
                "expTime": "",
                "futureSettlement": false,
                "groupId": "1",
                "instFamily": "",
                "instId": "BTC-USDT",
                "instType": "SPOT",
                "lever": "10",
                "listTime": "1606468572000",
                "lotSz": "0.00000001",
                "maxIcebergSz": "9999999999.0000000000000000",
                "maxLmtAmt": "1000000",
                "maxLmtSz": "9999999999",
                "maxMktAmt": "1000000",
                "maxMktSz": "",
                "maxStopSz": "",
                "maxTriggerSz": "9999999999.0000000000000000",
                "maxTwapSz": "9999999999.0000000000000000",
                "minSz": "0.00001",
                "optType": "",
                "openType": "call_auction",
                "preMktSwTime": "",
                "quoteCcy": "USDT",
                "tradeQuoteCcyList": [
                    "USDT"
                ],
                "settleCcy": "",
                "state": "live",
                "ruleType": "normal",
                "stk": "",
                "tickSz": "0.1",
                "uly": "",
                "instIdCode": 1000000000,
                "instCategory": "1",
                "upcChg": [
                    {
                        "param": "tickSz",
                        "newValue": "0.0001",
                        "effTime": "1704876947000"
                    }
                ]
            }
        ]
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
instType | String | Instrument type  
seriesId | String | Series ID, e.g. `BTC-ABOVE-DAILY`. Only applicable to `EVENTS`  
instId | String | Instrument ID, e.g. `BTC-USD-SWAP`  
uly | String | Underlying, e.g. `BTC-USD`   
Only applicable to `MARGIN/FUTURES`/`SWAP`/`OPTION`  
groupId | String | Instrument trading fee group ID  
Spot:  
`1`: Spot USDT  
`2`: Spot USDC & Crypto  
`3`: Spot TRY  
`4`: Spot EUR  
`5`: Spot BRL  
`7`: Spot AED  
`8`: Spot AUD  
`9`: Spot USD  
`10`: Spot SGD  
`11`: Spot zero  
`12`: Spot group one  
`13`: Spot group two  
`14`: Spot group three  
`15`: Spot special rule  
  
Expiry futures:  
`1`: Expiry futures crypto-margined  
`2`: Expiry futures USDT-margined  
`3`: Expiry futures USDC-margined  
`4`: Expiry futures premarket  
`5`: Expiry futures group one  
`6`: Expiry futures group two  
  
Perpetual futures:  
`1`: Perpetual futures crypto-margined  
`2`: Perpetual futures USDT-margined  
`3`: Perpetual futures USDC-margined  
`4`: Perpetual futures group one  
`5`: Perpetual futures group two   
`6`: Stock perpetual futures   
  
Options:  
`1`: Options crypto-margined  
`2`: Options USDC-margined  
  
**instType and groupId should be used together to determine a trading fee group. Users should use this endpoint together with[fee rates endpoint](/docs-v5/en/#trading-account-rest-api-get-fee-rates) to get the trading fee of a specific symbol.**   
  
**Some enum values may not apply to you; the actual return values shall prevail.**  
instFamily | String | Instrument family, e.g. `BTC-USD`   
Only applicable to `MARGIN/FUTURES`/`SWAP`/`OPTION`  
category | String | Currency category. Note: this parameter is already deprecated  
baseCcy | String | Base currency, e.g. `BTC` in`BTC-USDT`   
Only applicable to `SPOT`/`MARGIN`  
quoteCcy | String | Quote currency, e.g. `USDT` in `BTC-USDT`   
Only applicable to `SPOT`/`MARGIN`  
settleCcy | String | Settlement and margin currency, e.g. `BTC`   
Only applicable to `FUTURES`/`SWAP`/`OPTION`  
ctVal | String | Face value of one contract. Denomination depends on `ctType`: for linear contracts, `ctVal` is in the base currency (e.g., ctVal=0.01 BTC for BTC-USDT-SWAP); for inverse contracts, `ctVal` is in USD (e.g., ctVal=100 USD for BTC-USD-SWAP). Notional: linear = sz × ctVal × markPx (in quote ccy); inverse = sz × ctVal (in USD, fixed).   
Only applicable to `FUTURES`/`SWAP`/`OPTION`  
ctMult | String | Contract multiplier   
Only applicable to `FUTURES`/`SWAP`/`OPTION`  
ctValCcy | String | Contract value currency   
Only applicable to `FUTURES`/`SWAP`/`OPTION`  
optType | String | Option type, `C`: Call `P`: put   
Only applicable to `OPTION`  
stk | String | Strike price   
Only applicable to `OPTION`  
listTime | String | Listing time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
auctionEndTime | String | ~~The end time of call auction, Unix timestamp format in milliseconds, e.g.`1597026383085`   
Only applicable to `SPOT` that are listed through call auctions, return "" in other cases (deprecated, use contTdSwTime)~~  
contTdSwTime | String | Continuous trading switch time. The switch time from call auction, prequote to continuous trading, Unix timestamp format in milliseconds. e.g. `1597026383085`.  
Only applicable to `SPOT`/`MARGIN` that are listed through call auction or prequote, return "" in other cases.  
preMktSwTime | String | The time premarket swap switched to normal swap, Unix timestamp format in milliseconds, e.g. `1597026383085`.   
Only applicable premarket `SWAP`  
openType | String | Open type  
`fix_price`: fix price opening  
`pre_quote`: pre-quote  
`call_auction`: call auction   
Only applicable to `SPOT`/`MARGIN`, return "" for all other business lines  
expTime | String | Expiry time   
Applicable to `SPOT`/`MARGIN`/`FUTURES`/`SWAP`/`OPTION`. For `FUTURES`/`OPTION`, it is natural delivery/exercise time. It is the instrument offline time when there is `SPOT/MARGIN/FUTURES/SWAP/` manual offline. Update once change.  
lever | String | Exchange-defined maximum leverage ceiling for this instrument. The actual leverage available to a specific account may be lower based on VIP tier and position size. Use GET /api/v5/account/leverage-info for the user's current configured leverage.   
Not applicable to `SPOT`, `OPTION`  
tickSz | String | Minimum price increment, e.g. `0.0001`.  
For `OPTION`/`EVENTS`, it is the minimum tickSz among tick band. Use "Get instrument tick bands" endpoint with the corresponding `instType` for accurate tickSz per price range.  
lotSz | String | Lot size — the minimum order size increment. All order quantities (sz) must be a multiple of `lotSz`. Violation returns error 51121.  
If it is a derivatives contract, the value is the number of contracts.  
If it is `SPOT`/`MARGIN`, the value is the quantity in `base currency`.  
minSz | String | Minimum order size. Order size must satisfy both: sz ≥ `minSz` AND sz is a multiple of `lotSz`.  
If it is a derivatives contract, the value is the number of contracts.  
If it is `SPOT`/`MARGIN`, the value is the quantity in `base currency`.  
ctType | String | Contract type  
`linear`: linear contract — margin, P&L, and settlement in the quote currency (e.g., USDT for BTC-USDT-SWAP).  
`inverse`: inverse contract — margin, P&L, and settlement in the base currency (e.g., BTC for BTC-USD-SWAP). For inverse contracts, P&L in USD terms is non-linear: the USD value of a fixed BTC gain changes with the BTC price.   
Only applicable to `FUTURES`/`SWAP`  
alias | String | Contract alias (deprecated — use expTime to obtain the delivery time, will be removed by the end of April 2026)  
`this_week`  
`next_week`  
`this_month`  
`next_month`  
`quarter`  
`next_quarter`  
`third_quarter`  
`this_five_years`: current 5-year contract  
`next_five_years`: next 5-year contract  
Only applicable to `FUTURES`  
state | String | Instrument status  
`live`   
`suspend`  
`rebase`: can’t be traded during rebasing, only applicable to `SWAP`  
`post_only`: only post-only orders are accepted; existing post-only orders can be amended and cancelled. Other order types (market, IOC, FOK, normal limit) are rejected. Only applicable to `SWAP`  
`preopen`. e.g. There will be `preopen` before the Futures and Options new contracts state is live.  
`test`: Test pairs, can’t be traded  
`settling`: Settling, only applicable to `EVENTS`  
ruleType | String | Trading rule types  
`normal`: normal trading  
`pre_market`: pre-market trading  
`rebase_contract`: pre-market rebase contract  
`xperp`: perpetual-style futures, only applicable to certain `FUTURES` contracts  
maxLmtSz | String | The maximum order quantity of a single limit order.  
If it is a derivatives contract, the value is the number of contracts.  
If it is `SPOT`/`MARGIN`, the value is the quantity in `base currency`.  
maxMktSz | String | The maximum order quantity of a single market order.  
If it is a derivatives contract, the value is the number of contracts.  
If it is `SPOT`/`MARGIN`, the value is the quantity in `USDT`.  
maxLmtAmt | String | Max USD amount for a single limit order  
maxMktAmt | String | Max USD amount for a single market order   
Only applicable to `SPOT`/`MARGIN`  
maxTwapSz | String | The maximum order quantity of a single TWAP order.  
If it is a derivatives contract, the value is the number of contracts.  
If it is `SPOT`/`MARGIN`, the value is the quantity in `base currency`.   
The minimum order quantity of a single TWAP order is minSz*2  
maxIcebergSz | String | The maximum order quantity of a single iceBerg order.  
If it is a derivatives contract, the value is the number of contracts.  
If it is `SPOT`/`MARGIN`, the value is the quantity in `base currency`.  
maxTriggerSz | String | The maximum order quantity of a single trigger order.  
If it is a derivatives contract, the value is the number of contracts.  
If it is `SPOT`/`MARGIN`, the value is the quantity in `base currency`.  
maxStopSz | String | The maximum order quantity of a single stop market order.  
If it is a derivatives contract, the value is the number of contracts.  
If it is `SPOT`/`MARGIN`, the value is the quantity in `USDT`.  
futureSettlement | Boolean | Whether daily settlement for expiry feature is enabled  
Applicable to `FUTURES` `cross`  
tradeQuoteCcyList | Array of strings | List of quote currencies available for trading, e.g. ["USD", "USDC”].  
instIdCode | Integer | Instrument ID code.   
For simple binary encoding, you must use `instIdCode` instead of `instId`.  
For the same `instId`, it's value may be different between production and demo trading.   
It is `null` when the value is not generated.  
instCategory | String | The asset category of the instrument’s base asset (the first segment of the instrument ID). For example, for `BTC-USDT-SWAP`, the `instCategory` represents the asset category of `BTC`.   
`1`: Crypto   
`3`: Stocks   
`4`: Commodities   
`5`: Forex   
`6`: Bonds   
`""`: Not available  
initPxLmtPct | String | Initial price-limit band applied during the first 10 minutes after contract listing, e.g. `0.05` represents 5%. Use GET /api/v5/public/price-limit for the computed price limits.  
Only applicable to `SPOT`/`MARGIN`/`SWAP`/`FUTURES`, returns `""` for `OPTION` and `EVENTS`.  
floatPxLmtPct | String | Floating price-limit band during normal trading, e.g. `0.03` represents 3%. Use GET /api/v5/public/price-limit for the computed price limits.  
Only applicable to `SPOT`/`MARGIN`/`SWAP`/`FUTURES`, returns `""` for `OPTION` and `EVENTS`.  
maxPxLmtPct | String | Maximum price-limit cap (hard ceiling on order-price deviation from the index price), e.g. `0.15` represents 15%. Use GET /api/v5/public/price-limit for the computed price limits.  
Only applicable to `SPOT`/`MARGIN`/`SWAP`/`FUTURES`, returns `""` for `OPTION` and `EVENTS`.  
upcChg | Array of objects | Upcoming changes. It is [] when there is no upcoming change.  
> param | String | The parameter name to be updated.   
`tickSz`  
`minSz`: For `FUTURES`/`SWAP`, `lotSz` will be modified synchronously.  
`maxMktSz`  
> newValue | String | The parameter value that will replace the current one.  
> effTime | String | Effective time. Unix timestamp format in milliseconds, e.g. `1597026383085`  
When a new contract is going to be listed, the instrument data of the new contract will be available with status preopen. When a product is going to be delisted (e.g. when a FUTURES contract is settled or OPTION contract is exercised), the instrument will not be available   
listTime and contTdSwTime  
For spot symbols listed through a call auction or pre-open, listTime represents the start time of the auction or pre-open, and contTdSwTime indicates the end of the auction or pre-open and the start of continuous trading. For other scenarios, listTime will mark the beginning of continuous trading, and contTdSwTime will return an empty value "".  state  
For `SPOT`, `MARGIN`, `SWAP`, and `FUTURES`, the state changes from `preopen` to `live` when the `listTime` is reached. For `OPTION` contracts, the state may change to `live` slightly after `listTime` due to internal processing. It is recommended to verify that `state` is `live` before placing orders.  
When a product is going to be delisted (e.g. when a FUTURES contract is settled or OPTION contract is exercised), the instrument will not be available.  Instruments REST endpoints and WebSocket channel will update `expTime` once the delisting announcement is published.  
Instruments REST endpoint and WebSocket channel will update `listTime` once the listing announcement is published:  
1\. For `SPOT/MARGIN/SWAP`, this event is only applicable to `instType`, `instId`, `listTime`, `state`.  
2\. For `FUTURES`, this event is only applicable to `instType`, `instFamily`, `listTime`, `state`.  
3\. Other fields will be "" temporarily, but they will be updated at least 5 minutes in advance of the `listTime`, then the WebSocket subscription using related `instId`/`instFamily` can be available.  

### Get series

Retrieve the list of series for OKX prediction markets.

#### Rate Limit: 10 requests per 2 seconds

#### Rate limit rule: IP

#### Permission: Public

#### HTTP Request

`GET /api/v5/public/event-contract/series`

> Request Example
    
    
    GET /api/v5/public/event-contract/series?seriesId=BTC-ABOVE-DAILY
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
seriesId | String | No | Series ID, e.g. `BTC-ABOVE-DAILY`. If not passed, all series will be returned.  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "seriesId": "BTC-ABOVE-DAILY",
                "freq": "daily",
                "title": "BTC price above 15k",
                "category": "Crypto",
                "settlement": {
                    "method": "price_above",
                    "closeEarly": false,
                    "srcName": "okx_index",
                    "underlying": "BTC-USDT"
                }
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
seriesId | String | Series ID, e.g. `BTC-ABOVE-DAILY`  
freq | String | Frequency of the series  
`five_min`  
`fifteen_min`  
`hourly`  
`daily`  
`monthly`  
title | String | Series title  
category | String | Category which this series belongs to, e.g. `Crypto`  
settlement | Object | Settlement information  
> method | String | Settlement method.  
`price_up_down`: Price up/down  
`price_above`: Price above  
`hit`: Hit (price touches strike level, settles immediately)  
`between`: Between (settle price within [floorStrike, capStrike) range)  
> closeEarly | Boolean | Whether the market can be settled earlier than the expiration time.  
`true`  
`false`  
> srcName | String | Settlement source name, e.g. `okx_index`, `cf_benchmark_index`  
> underlying | String | Price underlying in OKX trading symbol format, e.g. `BTC-USDT`. Only applicable to price-related settlement methods.  
  
### Get events

Get events for a series in OKX prediction markets. Returns all event records, including expired ones. Return data in expTime and eventId descending order.

#### Rate Limit: 10 requests per 2 seconds

#### Rate limit rule: IP

#### Permission: Public

#### HTTP Request

`GET /api/v5/public/event-contract/events`

> Request Example
    
    
    GET /api/v5/public/event-contract/events?seriesId=BTC-ABOVE-DAILY
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
seriesId | String | Yes | Series ID, e.g. `BTC-ABOVE-DAILY`  
eventId | String | No | Event ID, e.g. `BTC-ABOVE-DAILY-260224-1600`  
state | String | No | Event state filter.  
`preopen`  
`live`  
`settling`  
`expired`  
limit | String | No | Number of results per request. Maximum is 100. Default is 100.  
before | String | No | Pagination. Returns records newer than the requested `expTime`, not included.  
after | String | No | Pagination. Returns records earlier than the requested `expTime`, not included.  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "seriesId": "BTC-ABOVE-DAILY",
                "eventId": "BTC-ABOVE-DAILY-260224-1600",
                "expTime": "1769697132335",
                "state": "live"
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
seriesId | String | Series ID, e.g. `BTC-ABOVE-DAILY`  
eventId | String | Event ID, e.g. `BTC-ABOVE-DAILY-260224-1600`  
fixTime | String | Strike price fixing time, Unix timestamp format in milliseconds, e.g. `1597026383085`. Only applicable to `price_up_down` settlement method.  
expTime | String | The specific strike time this event is based on, Unix timestamp format in milliseconds, e.g. `1597026383085`  
state | String | Event state.  
`preopen`  
`live`  
`settling`  
`expired`  
  
### Get markets

Get markets for events in OKX prediction markets. Return data in expTime and floorStrike descending order.

#### Rate Limit: 10 requests per 2 seconds

#### Rate limit rule: IP

#### Permission: Public

#### HTTP Request

`GET /api/v5/public/event-contract/markets`

> Request Example
    
    
    GET /api/v5/public/event-contract/markets?seriesId=BTC-ABOVE-DAILY
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
seriesId | String | Yes | Series ID, e.g. `BTC-ABOVE-DAILY`  
eventId | String | No | Event ID, e.g. `BTC-ABOVE-DAILY-260224-1600`  
instId | String | No | Instrument ID, e.g. `BTC-ABOVE-DAILY-260224-1600-65000`  
state | String | No | Filter by market status.  
`preopen`  
`live`  
`settling`  
`expired`  
limit | String | No | Number of results per request. Maximum is 100. Default is 100.  
before | String | No | Pagination. Returns records newer than the requested `expTime`, not included.  
after | String | No | Pagination. Returns records earlier than the requested `expTime`, not included.  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "seriesId": "BTC-ABOVE-DAILY",
                "eventId": "BTC-ABOVE-DAILY-260224-1600",
                "instId": "BTC-ABOVE-DAILY-260224-1600-65000",
                "listTime": "1769697132335",
                "expTime": "1769697132335",
                "state": "live",
                "fixTime": "",
                "outcome": "0",
                "floorStrike": "120000",
                "capStrike": "",
                "settleValue": "",
                "disputed": false,
                "hitDir": ""
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
seriesId | String | Series ID, e.g. `BTC-ABOVE-DAILY`  
eventId | String | Event ID, e.g. `BTC-ABOVE-DAILY-260224-1600`  
instId | String | Instrument ID, e.g. `BTC-ABOVE-DAILY-260224-1600-65000`  
listTime | String | Listing time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
fixTime | String | Strike price fixing time, Unix timestamp format in milliseconds, e.g. `1597026383085`. Only applicable to `price_up_down` settlement method.  
expTime | String | Strike time for this event, Unix timestamp format in milliseconds, e.g. `1597026383085`. Updated once the market is settled.  
state | String | Market state.  
`preopen`  
`live`  
`settling`  
`expired`  
disputed | Boolean | Whether the market has been disputed.  
`true`  
`false`  
outcome | String | Market outcome.  
`0`: Not available  
`1`: YES  
`2`: NO.  
`1`/`2` only applicable when state is `expired`  
floorStrike | String | Minimum expiration value that leads to a YES outcome  
capStrike | String | Maximum expiration value that leads to a YES outcome for `between` method. `"INF"` indicates no upper bound (the topmost bracket).  
Returns `""` for non-`between` methods.  
settleValue | String | Settlement value  
Only return when the state is `expired`  
hitDir | String | Hit direction. Only applicable when the settlement method is `hit`.  
`up`: price hit from below  
`dn`: price hit from above  
`""`: not applicable (non-`hit` methods)  
  
### Get estimated delivery/exercise price

Retrieve the estimated delivery price which will only have a return value one hour before the delivery/exercise.

#### Rate Limit: 10 requests per 2 seconds

#### Rate limit rule: IP + Instrument ID

#### HTTP Request

`GET /api/v5/public/estimated-price`

> Request Example
    
    
    GET /api/v5/public/estimated-price?instId=BTC-USD-200214
    
    
    
    import okx.PublicData as PublicData
    
    flag = "0"  # Production trading: 0, Demo trading: 1
    
    publicDataAPI = PublicData.PublicAPI(flag=flag)
    
    # Retrieve estimated delivery/exercise price
    result = publicDataAPI.get_estimated_price(
        instId = "BTC-USD-200214",
    )
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
instId | String | Yes | Instrument ID, e.g. `BTC-USD-200214`   
only applicable to `FUTURES`/`OPTION`/`EVENTS`  
  
> Response Example
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
        {
            "instType":"FUTURES",
            "instId":"BTC-USDT-201227",
            "settlePx":"200",
            "ts":"1597026383085"
        }
      ]
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
instType | String | Instrument type  
`FUTURES`  
`OPTION`  
instId | String | Instrument ID, e.g. `BTC-USD-200214`  
settlePx | String | Estimated delivery/exercise price  
ts | String | Data return time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
  
### Get delivery/exercise history

Retrieve delivery records of Futures and exercise records of Options in the last 3 months.

#### Rate Limit: 40 requests per 2 seconds

#### Rate limit rule: IP + (Instrument Type + instFamily)

#### HTTP Request

`GET /api/v5/public/delivery-exercise-history`

> Request Example
    
    
    GET /api/v5/public/delivery-exercise-history?instType=OPTION&instFamily=BTC-USD
    
    
    
    import okx.PublicData as PublicData
    
    flag = "0"  # Production trading: 0, Demo trading: 1
    
    publicDataAPI = PublicData.PublicAPI(flag=flag)
    
    # Retrieve delivery records of Futures and exercise records of Options in the last 3 months
    result = publicDataAPI.get_delivery_exercise_history(
        instType="FUTURES",
        uly="BTC-USD"
    )
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
instType | String | Yes | Instrument type  
`FUTURES`  
`OPTION`  
instFamily | String | Yes | Instrument family, only applicable to `FUTURES`/`OPTION`  
after | String | No | Pagination of data to return records earlier than the requested `ts`  
before | String | No | Pagination of data to return records newer than the requested `ts`  
limit | String | No | Number of results per request. The maximum is `100`; The default is `100`  
  
> Response Example
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
            {
                "ts":"1597026383085",
                "details":[
                    {
                        "type":"delivery",
                        "insId":"BTC-USD-190927",
                        "px":"0.016"
                    }
                ]
            },
            {
                "ts":"1597026383085",
                "details":[
                    {
                        "insId":"BTC-USD-200529-6000-C",
                        "type":"exercised",
                        "px":"0.016"
                    },
                    {
                        "insId":"BTC-USD-200529-8000-C",
                        "type":"exercised",
                        "px":"0.016"
                    }
                ]
            }
        ]
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
ts | String | Delivery/exercise time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
details | Array of objects | Delivery/exercise details  
> insId | String | Delivery/exercise contract ID  
> px | String | Delivery/exercise price  
> type | String | Type   
`delivery`   
`exercised`   
`expired_otm`:Out of the money  
  
### Get estimated future settlement price

Retrieve the estimated settlement price which will only have a return value one hour before the settlement.

#### Rate Limit: 10 requests per 2 seconds

#### Rate limit rule: IP + Instrument ID

#### HTTP Request

`GET /api/v5/public/estimated-settlement-info`

> Request Example
    
    
    GET /api/v5/public/estimated-settlement-info?instId=XRP-USDT-250307
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
instId | String | Yes | Instrument ID, e.g. `XRP-USDT-250307`   
only applicable to `FUTURES`  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "estSettlePx": "2.5666068562369959",
                "instId": "XRP-USDT-250307",
                "nextSettleTime": "1741248000000",
                "ts": "1741246429748"
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
instId | String | Instrument ID, e.g. `XRP-USDT-250307`  
nextSettleTime | String | Next settlement time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
estSettlePx | String | Estimated settlement price  
ts | String | Data return time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
  
### Get futures settlement history

Retrieve settlement records of futures in the last 3 months.

#### Rate Limit: 40 requests per 2 seconds

#### Rate limit rule: IP + (Instrument Family)

#### HTTP Request

`GET /api/v5/public/settlement-history`

> Request Example
    
    
    GET /api/v5/public/settlement-history?instFamily=XRP-USD
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
instFamily | String | Yes | Instrument family  
after | String | No | Pagination of data to return records earlier than (not include) the requested `ts`  
before | String | No | Pagination of data to return records newer than (not include) the requested `ts`  
limit | String | No | Number of results per request. The maximum is `100`. The default is `100`  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "details": [
                    {
                        "instId": "XRP-USDT-250307",
                        "settlePx": "2.5192078615298715"
                    }
                ],
                "ts": "1741161600000"
            },
            {
                "details": [
                    {
                        "instId": "XRP-USDT-250307",
                        "settlePx": "2.5551316341327384"
                    }
                ],
                "ts": "1741075200000"
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
ts | String | Settlement time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
details | Array of objects | Settlement info  
> instId | String | Instrument ID  
> settlePx | String | Settlement price  
  
### Get funding rate

Retrieve funding rate.

#### Rate Limit: 10 requests per 2 seconds

#### Rate limit rule: IP + Instrument ID

#### HTTP Request

`GET /api/v5/public/funding-rate`

> Request Example
    
    
    GET /api/v5/public/funding-rate?instId=BTC-USD-SWAP
    
    
    
    import okx.PublicData as PublicData
    
    flag = "0"  # Production trading: 0, Demo trading: 1
    
    publicDataAPI = PublicData.PublicAPI(flag=flag)
    
    # Retrieve funding rate
    result = publicDataAPI.get_funding_rate(
        instId="BTC-USD-SWAP",
    )
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
instId | String | Yes | Instrument ID, e.g. `BTC-USD-SWAP` or X-Perps futures instId, or `ANY` to return the funding rate info of all perpetual and X-Perps futures contracts  
Applicable to `SWAP` and X-Perps `FUTURES`  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "formulaType": "noRate",
                "fundingRate": "0.0000182221218054",
                "fundingTime": "1743609600000",
                "impactValue": "",
                "instId": "BTC-USDT-SWAP",
                "instType": "SWAP",
                "interestRate": "",
                "maxFundingRate": "0.00375",
                "method": "current_period",
                "minFundingRate": "-0.00375",
                "nextFundingRate": "",
                "nextFundingTime": "1743638400000",
                "premium": "0.0000910113652644",
                "settFundingRate": "0.0000145824401745",
                "settState": "settled",
                "ts": "1743588686291"
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
instType | String | Instrument type  
`SWAP`: Perpetual futures  
`FUTURES`: X-Perps futures  
instId | String | Instrument ID, e.g. `BTC-USD-SWAP` or `ANY`  
method | String | Funding rate mechanism   
`current_period` ~~  
`next_period`~~(no longer supported)  
formulaType | String | Formula type  
`noRate`: old funding rate formula  
`withRate`: new funding rate formula  
fundingRate | String | Predicted funding rate for the upcoming settlement period. Sign: positive = long positions pay short positions at the next `fundingTime`; negative = short positions pay long positions. This is a forecast — the final settled rate may differ. See `settFundingRate` for the last settled rate. Note: the settlement interval is typically 8 hours but may be adjusted; use the difference between `fundingTime` and `nextFundingTime` to determine the actual interval.  
nextFundingRate | String | ~~Forecasted funding rate for the next period  
The nextFundingRate will be "" if the method is `current_period`~~(no longer supported)  
fundingTime | String | Settlement time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
nextFundingTime | String | Forecasted funding time for the next period , Unix timestamp format in milliseconds, e.g. `1597026383085`  
minFundingRate | String | The lower limit of the funding rate  
maxFundingRate | String | The upper limit of the funding rate  
interestRate | String | Interest rate  
impactValue | String | Depth weighted amount (in the unit of quote currency)  
settState | String | Settlement state of funding rate   
`processing`   
`settled`  
settFundingRate | String | If settState = `processing`, it is the funding rate that is being used for current settlement cycle.   
If settState = `settled`, it is the funding rate that is being used for previous settlement cycle  
premium | String | Premium index  
formula: [Max (0, Impact bid price – Index price) – Max (0, Index price – Impact ask price)] / Index price  
ts | String | Data return time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
For some altcoins perpetual swaps with significant fluctuations in funding rates, OKX will closely monitor market changes. When necessary, the funding rate collection frequency, currently set at 8 hours, may be adjusted to higher frequencies such as 6 hours, 4 hours, 2 hours, or 1 hour. Thus, users should focus on the difference between `fundingTime` and `nextFundingTime` fields to determine the funding fee interval of a contract. 

### Get funding rate history

Retrieve funding rate history. This endpoint can return data up to three months.

#### Rate Limit: 10 requests per 2 seconds

#### Rate limit rule: IP + Instrument ID

#### HTTP Request

`GET /api/v5/public/funding-rate-history`

> Request Example
    
    
    GET /api/v5/public/funding-rate-history?instId=BTC-USD-SWAP
    
    
    
    import okx.PublicData as PublicData
    
    flag = "0"  # Production trading: 0, Demo trading: 1
    
    publicDataAPI = PublicData.PublicAPI(flag=flag)
    
    # Retrieve funding rate history
    result = publicDataAPI.funding_rate_history(
        instId="BTC-USD-SWAP",
    )
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
instId | String | Yes | Instrument ID, e.g. `BTC-USD-SWAP` or X-Perps futures instId  
Applicable to `SWAP` and X-Perps `FUTURES`  
before | String | No | Pagination of data to return records newer than the requested `fundingTime`  
after | String | No | Pagination of data to return records earlier than the requested `fundingTime`  
limit | String | No | Number of results per request. The maximum is `400`; The default is `400`  
  
> Response Example
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
            {
                "formulaType": "noRate",
                "fundingRate": "0.0000746604960499",
                "fundingTime": "1703059200000",
                "instId": "BTC-USD-SWAP",
                "instType": "SWAP",
                "method": "next_period",
                "realizedRate": "0.0000746572360545"
            },
            {
                "formulaType": "noRate",
                "fundingRate": "0.000227985782722",
                "fundingTime": "1703030400000",
                "instId": "BTC-USD-SWAP",
                "instType": "SWAP",
                "method": "next_period",
                "realizedRate": "0.0002279755647389"
            }
      ]
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
instType | String | Instrument type  
`SWAP`: Perpetual futures  
`FUTURES`: X-Perps futures  
instId | String | Instrument ID, e.g. `BTC-USD-SWAP`  
formulaType | String | Formula type  
`noRate`: old funding rate formula  
`withRate`: new funding rate formula  
fundingRate | String | Predicted funding rate  
realizedRate | String | Actual funding rate  
fundingTime | String | Settlement time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
method | String | Funding rate mechanism   
`current_period`   
`next_period`  
For some altcoins perpetual swaps with significant fluctuations in funding rates, OKX will closely monitor market changes. When necessary, the funding rate collection frequency, currently set at 8 hours, may be adjusted to higher frequencies such as 6 hours, 4 hours, 2 hours, or 1 hour. Thus, users should focus on the difference between `fundingTime` and `nextFundingTime` fields to determine the funding fee interval of a contract. 

### Get open interest

Retrieve the total open interest for contracts on OKX.

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: IP + Instrument ID

#### HTTP Request

`GET /api/v5/public/open-interest`

> Request Example
    
    
    GET /api/v5/public/open-interest?instType=SWAP
    
    
    
    import okx.PublicData as PublicData
    
    flag = "0"  # Production trading: 0, Demo trading: 1
    
    publicDataAPI = PublicData.PublicAPI(flag=flag)
    
    # Retrieve the total open interest for contracts on OKX
    result = publicDataAPI.get_open_interest(
        instType="SWAP",
    )
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
instType | String | Yes | Instrument type  
`SWAP`  
`FUTURES`  
`OPTION`  
`EVENTS`  
instFamily | String | Conditional | Instrument family  
Applicable to `FUTURES`/`SWAP`/`OPTION`  
If instType is `OPTION`, instFamily is required.  
instId | String | No | Instrument ID, e.g. `BTC-USDT-SWAP`  
Applicable to `FUTURES`/`SWAP`/`OPTION`/`EVENTS`  
  
> Response Example
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
        {
            "instType":"SWAP",
            "instId":"BTC-USDT-SWAP",
            "oi":"5000",
            "oiCcy":"555.55",
            "oiUsd": "50000",
            "ts":"1597026383085"
        }
      ]
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
instType | String | Instrument type  
instId | String | Instrument ID  
oi | String | Open interest in number of contracts  
oiCcy | String | Open interest in number of coin  
oiUsd | String | Open interest in number of USD  
ts | String | Data return time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
  
### Get limit price

Retrieve the highest buy limit and lowest sell limit of the instrument.

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: IP

#### HTTP Request

`GET /api/v5/public/price-limit`

> Request Example
    
    
    GET /api/v5/public/price-limit?instId=BTC-USDT-SWAP
    
    
    
    import okx.PublicData as PublicData
    
    flag = "0"  # Production trading: 0, Demo trading: 1
    
    publicDataAPI = PublicData.PublicAPI(flag=flag)
    
    # Retrieve the highest buy limit and lowest sell limit of the instrument
    result = publicDataAPI.get_price_limit(
        instId="BTC-USD-SWAP",
    )
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
instId | String | Yes | Instrument ID, e.g. `BTC-USDT-SWAP`  
  
> Response Example
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
        {
            "instType":"SWAP",
            "instId":"BTC-USDT-SWAP",
            "buyLmt":"17057.9",
            "sellLmt":"16388.9",
            "ts":"1597026383085",
            "enabled": true
        }
      ]
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
instType | String | Instrument type  
instId | String | Instrument ID, e.g. `BTC-USDT-SWAP`  
buyLmt | String | Highest buy limit   
Return "" when enabled is false  
sellLmt | String | Lowest sell limit   
Return "" when enabled is false  
ts | String | Data return time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
enabled | Boolean | Whether price limit is effective   
`true`: the price limit is effective   
`false`: the price limit is not effective  
  
### Get option market data

Retrieve option market data.

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: IP + instFamily

#### HTTP Request

`GET /api/v5/public/opt-summary`

> Request Example
    
    
    GET /api/v5/public/opt-summary?uly=BTC-USD
    
    
    
    import okx.PublicData as PublicData
    
    flag = "0"  # Production trading: 0, Demo trading: 1
    
    publicDataAPI = PublicData.PublicAPI(flag=flag)
    
    # Retrieve option market data
    result = publicDataAPI.get_opt_summary(
        uly="BTC-USD",
    )
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
instFamily | String | Yes | Instrument family, only applicable to `OPTION`  
  
expTime | String | No | Contract expiry date, the format is "YYMMDD", e.g. "200527"  
  
**Note** : This endpoint may not return data for every option listed in `/api/v5/public/instruments`. Data can be absent in two cases: 1\. The option is listed but not yet tradeable (e.g. supplemental options may not become tradeable until a scheduled time; data will not be available before trading opens). 2\. Implied volatility surface fitting fails due to insufficient market quotes. This is more likely to occur in demo trading; in live trading, market maker quotes are generally available to ensure fitting succeeds.

> Response Example
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
            {
                "askVol": "3.7207056835937498",
                "bidVol": "0",
                "delta": "0.8310206676289528",
                "deltaBS": "0.9857332101544538",
                "fwdPx": "39016.8143629068452065",
                "gamma": "-1.1965483553276135",
                "gammaBS": "0.000011933182397798109",
                "instId": "BTC-USD-220309-33000-C",
                "instType": "OPTION",
                "lever": "0",
                "markVol": "1.5551965233045728",
                "realVol": "0",
                "volLv": "0",
                "theta": "-0.0014131955002093717",
                "thetaBS": "-66.03526900575946",
                "ts": "1646733631242",
                "uly": "BTC-USD",
                "vega": "0.000018173851073258973",
                "vegaBS": "0.7089307622132419"
            },
            {
                "askVol": "1.7968814062499998",
                "bidVol": "0",
                "delta": "-0.014668822072611904",
                "deltaBS": "-0.01426678984554619",
                "fwdPx": "39016.8143629068452065",
                "gamma": "0.49483062407551576",
                "gammaBS": "0.000011933182397798109",
                "instId": "BTC-USD-220309-33000-P",
                "instType": "OPTION",
                "lever": "0",
                "markVol": "1.5551965233045728",
                "realVol": "0",
                "volLv": "0",
                "theta": "-0.0014131955002093717",
                "thetaBS": "-54.93377294845015",
                "ts": "1646733631242",
                "uly": "BTC-USD",
                "vega": "0.000018173851073258973",
                "vegaBS": "0.7089307622132419"
            }
      ]
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
instType | String | Instrument type  
`OPTION`  
instId | String | Instrument ID, e.g. `BTC-USD-200103-5500-C`  
uly | String | Underlying  
delta | String | Sensitivity of option price to `uly` price  
gamma | String | The delta is sensitivity to `uly` price  
vega | String | Sensitivity of option price to implied volatility  
theta | String | Sensitivity of option price to remaining maturity  
deltaBS | String | Sensitivity of option price to `uly` price in BS mode  
gammaBS | String | The delta is sensitivity to `uly` price in BS mode  
vegaBS | String | Sensitivity of option price to implied volatility in BS mode  
thetaBS | String | Sensitivity of option price to remaining maturity in BS mode  
lever | String | Leverage  
markVol | String | Mark volatility  
bidVol | String | Bid volatility  
askVol | String | Ask volatility  
realVol | String | Realized volatility (not currently used)  
volLv | String | Implied volatility of at-the-money options  
fwdPx | String | Forward price  
ts | String | Data update time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
  
### Get discount rate and interest-free quota

Retrieve discount rate level and interest-free quota.

#### Rate Limit: 2 requests per 2 seconds

#### Rate limit rule: IP

#### HTTP Request

`GET /api/v5/public/discount-rate-interest-free-quota`

> Request Example
    
    
    GET /api/v5/public/discount-rate-interest-free-quota?ccy=BTC
    
    
    
    import okx.PublicData as PublicData
    
    flag = "0"  # Production trading: 0, Demo trading: 1
    
    publicDataAPI = PublicData.PublicAPI(flag=flag)
    
    # Retrieve discount rate level and interest-free quota
    result = publicDataAPI.discount_interest_free_quota()
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
ccy | String | No | Currency  
discountLv | String | No | ~~Discount level (Deprecated)~~~~~~  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "amt": "0",
                "ccy": "BTC",
                "collateralRestrict": false,
                "details": [
                    {
                        "discountRate": "0.98",
                        "liqPenaltyRate": "0.02",
                        "maxAmt": "20",
                        "minAmt": "0",
                        "tier": "1",
                        "disCcyEq": "1000"
                    },
                    {
                        "discountRate": "0.9775",
                        "liqPenaltyRate": "0.0225",
                        "maxAmt": "25",
                        "minAmt": "20",
                        "tier": "2",
                        "disCcyEq": "2000"
                    }
                ],
                "discountLv": "1",
                "minDiscountRate": "0"
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
ccy | String | Currency  
colRes | String | Platform level collateral restriction status  
`0`: The restriction is not enabled.  
`1`: The restriction is not enabled. But the crypto is close to the platform's collateral limit.  
`2`: The restriction is enabled. This crypto can't be used as margin for your new orders. This may result in failed orders. But it will still be included in the account's adjusted equity and doesn't impact margin ratio.  
Refer to [Introduction to the platform collateralized borrowing limit](https://www.okx.com/help/introduction-to-the-platforms-collateralized-borrowing-limit-mechanism) for more details.  
collateralRestrict | Boolean | ~~Platform level collateralized borrow restriction  
`true`  
`false`~~(deprecated, use colRes instead)  
amt | String | Interest-free quota  
discountLv | String | ~~Discount rate level.(Deprecated)~~~~~~  
minDiscountRate | String | Minimum discount rate when it exceeds the maximum amount of the last tier.  
details | Array of objects | New discount details.  
> discountRate | String | Discount rate  
> maxAmt | String | Tier - upper bound.   
The unit is the currency like BTC. "" means positive infinity  
> minAmt | String | Tier - lower bound.   
The unit is the currency like BTC. The minimum is 0  
> tier | String | Tiers  
> liqPenaltyRate | String | Liquidation penalty rate  
> disCcyEq | String | Discount equity in currency for quick calculation if your equity is the`maxAmt`  
  
### Get system time

Retrieve API server time.

#### Rate Limit: 10 requests per 2 seconds

#### Rate limit rule: IP

#### HTTP Request

`GET /api/v5/public/time`

> Request Example
    
    
    GET /api/v5/public/time
    
    
    
    import okx.PublicData as PublicData
    
    flag = "0"  # Production trading: 0, Demo trading: 1
    
    publicDataAPI = PublicData.PublicAPI(flag=flag)
    
    # Retrieve API server time
    result = publicDataAPI.get_system_time()
    print(result)
    

> Response Example
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
        {
            "ts":"1597026383085"
        }
      ]
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
ts | String | System time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
  
### Get mark price

Retrieve mark price.

We set the mark price based on the SPOT index and at a reasonable basis to prevent individual users from manipulating the market and causing the contract price to fluctuate.

#### Rate Limit: 10 requests per 2 seconds

#### Rate limit rule: IP + Instrument ID

#### HTTP Request

`GET /api/v5/public/mark-price`

> Request Example
    
    
    GET /api/v5/public/mark-price?instType=SWAP
    
    
    
    import okx.PublicData as PublicData
    
    flag = "0"  # Production trading: 0, Demo trading: 1
    
    publicDataAPI = PublicData.PublicAPI(flag=flag)
    
    # Retrieve mark price
    result = publicDataAPI.get_mark_price(
        instType="SWAP",
    )
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
instType | String | Yes | Instrument type  
`MARGIN`  
`SWAP`  
`FUTURES`  
`OPTION`  
`EVENTS`  
instFamily | String | No | Instrument family  
Applicable to `FUTURES`/`SWAP`/`OPTION`  
instId | String | No | Instrument ID, e.g. `BTC-USD-SWAP`  
  
> Response Example
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
        {
            "instType":"SWAP",
            "instId":"BTC-USDT-SWAP",
            "markPx":"200",
            "ts":"1597026383085"
        }
      ]
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
instType | String | Instrument type  
`MARGIN`  
`SWAP`  
`FUTURES`  
`OPTION`  
`EVENTS`  
instId | String | Instrument ID, e.g. `BTC-USD-200214`  
markPx | String | Mark price  
ts | String | Data return time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
  
### Get position tiers

Retrieve position tiers information, maximum leverage depends on your borrowings and Maintenance margin ratio.

#### Rate Limit: 10 requests per 2 seconds

#### Rate limit rule: IP

#### HTTP Request

`GET /api/v5/public/position-tiers`

> Request Example
    
    
    GET /api/v5/public/position-tiers?tdMode=cross&instType=SWAP&instFamily=BTC-USDT
    
    
    
    import okx.PublicData as PublicData
    
    flag = "0"  # Production trading: 0, Demo trading: 1
    
    publicDataAPI = PublicData.PublicAPI(flag=flag)
    
    # Retrieve position tiers information
    result = publicDataAPI.get_position_tiers(
        instType="SWAP",
        tdMode="cross",
        uly="BTC-USD"
    )
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
instType | String | Yes | Instrument type  
`MARGIN`  
`SWAP`  
`FUTURES`  
`OPTION`  
tdMode | String | Yes | Trade mode  
Margin mode `cross` `isolated`  
instFamily | String | Conditional | Single instrument familiy or multiple instrument families (no more than 5) separated with comma.  
If instType is `SWAP/FUTURES/OPTION`, `instFamily` is required.  
instId | String | Conditional | Single instrument or multiple instruments (no more than 5) separated with comma.  
Either instId or ccy is required, if both are passed, instId will be used, ignore when instType is one of `SWAP`,`FUTURES`,`OPTION`  
ccy | String | Conditional | Margin currency  
Only applicable to cross MARGIN. It will return borrowing amount for `Multi-currency margin` and `Portfolio margin` when `ccy` takes effect.  
tier | String | No | Tiers  
  
> Response Example
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
        {
                "baseMaxLoan": "50",
                "imr": "0.1",
                "instId": "BTC-USDT",
                "maxLever": "10",
                "maxSz": "50",
                "minSz": "0",
                "mmr": "0.03",
                "optMgnFactor": "0",
                "quoteMaxLoan": "500000",
                "tier": "1",
                "uly": "",
                "instFamily": ""
            }
      ]
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
uly | String | Underlying  
Applicable to `FUTURES`/`SWAP`/`OPTION`  
instFamily | String | Instrument family  
Applicable to `FUTURES`/`SWAP`/`OPTION`  
instId | String | Instrument ID  
tier | String | Tiers  
minSz | String | The minimum borrowing amount or position of this gear is only applicable to margin/options/perpetual/delivery, the minimum position is 0 by default  
It will return the minimum borrowing amount when `ccy` takes effect.  
maxSz | String | The maximum borrowing amount or number of positions held in this position is only applicable to margin/options/perpetual/delivery  
It will return the maximum borrowing amount when `ccy` takes effect.  
mmr | String | Position maintenance margin requirement rate  
imr | String | Initial margin requirement rate  
maxLever | String | Maximum available leverage  
optMgnFactor | String | Option Margin Coefficient (only applicable to options)  
quoteMaxLoan | String | Quote currency borrowing amount (only applicable to leverage and the case when `instId` takes effect)  
baseMaxLoan | String | Base currency borrowing amount (only applicable to leverage and the case when `instId` takes effect)  
  
### Get interest rate and loan quota

Retrieve interest rate

#### Rate Limit: 2 requests per 2 seconds

#### Rate limit rule: IP

#### HTTP Request

`GET /api/v5/public/interest-rate-loan-quota`

> Request Example
    
    
    GET /api/v5/public/interest-rate-loan-quota
    
    
    
    import okx.PublicData as PublicData
    
    flag = "0"  # Production trading: 0, Demo trading: 1
    
    publicDataAPI = PublicData.PublicAPI(flag=flag)
    
    # Retrieve interest rate and loan quota
    result = publicDataAPI.get_interest_rate_loan_quota()
    print(result)
    

> Response Example
    
    
    {
        "code": "0",
        "data": [
            {   
                "configCcyList": [
                    {
                        "ccy": "USDT",
                        "rate": "0.00043728",
                    }
                ],
                "basic": [
                    {
                        "ccy": "USDT",
                        "quota": "500000",
                        "rate": "0.00043728"
                    },
                    {
                        "ccy": "BTC",
                        "quota": "10",
                        "rate": "0.00019992"
                    }
                ],
                "vip": [
                    {
                        "irDiscount": "",
                        "loanQuotaCoef": "6",
                        "level": "VIP1"
                    },
                    {
                        "irDiscount": "",
                        "loanQuotaCoef": "7",
                        "level": "VIP2"
                    }
                ],
                "config": [
                    {
                        "ccy": "USDT",
                        "stgyType": "0",    // normal
                        "quota": "xxxxxx",
                        "level": "VIP 8"
                    },
                    ......
                    {
                        "ccy": "USDT",
                        "stgyType": "1",    // delta neutral
                        "quota": "xxxxx",
                        "level": "VIP 1"
                    },
                    ......
                ],
                "regular": [
                    {
                        "irDiscount": "",
                        "loanQuotaCoef": "1",
                        "level": "Lv1"
                    },
                    {
                        "irDiscount": "",
                        "loanQuotaCoef": "2",
                        "level": "Lv1"
                    }
                ]
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
basic | Array of objects | Basic interest rate  
> ccy | String | Currency  
> rate | String | Daily borrowing rate  
> quota | String | Max borrow  
vip | Array of objects | Interest info for vip users  
> level | String | VIP Level, e.g. `VIP1`  
> loanQuotaCoef | String | Loan quota coefficient. Loan quota = `quota` * `level`  
> irDiscount | String | ~~Interest rate discount~~(Deprecated)  
regular | Array of objects | Interest info for regular users  
> level | String | Regular user Level, e.g. `Lv1`  
> loanQuotaCoef | String | Loan quota coefficient. Loan quota = `quota` * `level`  
> irDiscount | String | ~~Interest rate discount~~(Deprecated)  
configCcyList | Array of strings | Currencies that have loan quota configured using customized absolute value.  
Users should refer to config to get the loan quota of a currency which is listed in configCcyList, instead of getting it from basic/vip/regular.  
> ccy | String | Currency  
> rate | String | Daily rate  
config | Array of objects | The currency details of loan quota configured using customized absolute value  
> ccy | String | Currency  
> stgyType | String | Strategy type  
`0`: general strategy  
`1`: delta neutral strategy  
If only `0` is returned for a currency, it means the loan quota is shared between accounts in general strategy and accounts in delta neutral strategy; if both `0/1` are returned for a currency, it means accounts in delta neutral strategy have separate loan quotas.  
> quota | String | Loan quota in absolute value  
> level | String | VIP level  
  
### Get underlying

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: IP

#### HTTP Request

`GET /api/v5/public/underlying`

> Request Example
    
    
    GET /api/v5/public/underlying?instType=FUTURES
    
    
    
    import okx.PublicData as PublicData
    
    flag = "0"  # Production trading: 0, Demo trading: 1
    
    publicDataAPI = PublicData.PublicAPI(flag=flag)
    
    # Get underlying
    result = publicDataAPI.get_underlying(
        instType="FUTURES"
    )
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
instType | String | Yes | Instrument type  
`SWAP`  
`FUTURES`  
`OPTION`  
  
> Response Example
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
            [
                "LTC-USDT",
                "BTC-USDT",
                "ETC-USDT"
            ]
        ]
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
uly | Array | Underlying  
  
### Get security fund

Get security fund balance information

#### Rate Limit: 10 requests per 2 seconds

#### Rate limit rule: IP

#### HTTP Request

`GET /api/v5/public/insurance-fund`

> Request Example
    
    
    GET /api/v5/public/insurance-fund?instType=SWAP&uly=BTC-USD
    
    
    
    import okx.PublicData as PublicData
    
    flag = "0"  # Production trading: 0, Demo trading: 1
    
    publicDataAPI = PublicData.PublicAPI(flag=flag)
    
    
    # Get security fund balance information
    result = publicDataAPI.get_insurance_fund(
        instType="SWAP",
        uly="BTC-USD"
    )
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
instType | String | Yes | Instrument type  
`MARGIN`  
`SWAP`  
`FUTURES`  
`OPTION`  
type | String | No | Type  
`liquidation_balance_deposit`  
`bankruptcy_loss`  
~~`platform_revenue`~~(Deprecated, returns empty values. To be removed in a future update)   
~~`adl`~~(Deprecated, returns empty values. To be removed in a future update)   
The default is `all type`  
instFamily | String | Conditional | Instrument family  
Required for `FUTURES`/`SWAP`/`OPTION`  
ccy | String | Conditional | Currency, only applicable to `MARGIN`  
before | String | No | Pagination of data to return records newer than the requested `ts`  
after | String | No | Pagination of data to return records earlier than the requested `ts`  
limit | String | No | Number of results per request. The maximum is `100`; The default is `100`  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "details": [
                    {
                        "adlType": "",
                        "amt": "1343.1308",
                        "balance": "1369179138.7489",
                        "ccy": "ETH",
                        "maxBal": "",
                        "maxBalTs": "",
                        "ts": "1704883083000",
                        "type": "liquidation_balance_deposit"
                    }
                ],
                "instFamily": "ETH-USD",
                "instType": "OPTION",
                "total": "1369179138.7489"
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
total | String | The total balance of security fund, in `USD`  
instFamily | String | Instrument family  
Applicable to `FUTURES`/`SWAP`/`OPTION`  
instType | String | Instrument type  
details | Array of objects | security fund data  
> balance | String | The balance of security fund  
> amt | String | The change in the balance of security fund   
Applicable when type is `liquidation_balance_deposit` or `bankruptcy_loss`  
> ccy | String | The currency of security fund  
> type | String | The type of security fund  
`liquidation_balance_deposit`  
`bankruptcy_loss`  
~~`platform_revenue`~~(Deprecated, returns empty values)  
~~`adl`~~(Deprecated, returns empty values)  
> maxBal | String | ~~Maximum security fund balance in the past eight hours  
Only applicable when type is `adl`~~(Deprecated, returns empty values)  
> maxBalTs | String | ~~Timestamp when security fund balance reached maximum in the past eight hours, Unix timestamp format in milliseconds, e.g.`1597026383085`   
Only applicable when type is `adl`~~(Deprecated, returns empty values)  
> decRate | String | ~~Real-time security fund decline rate (compare balance and maxBal)  
Only applicable when type is `adl`~~(Deprecated)  
> adlType | String | ~~ADL related events  
`rate_adl_start`: ADL begins due to high security fund decline rate   
`bal_adl_start`: ADL begins due to security fund balance falling   
`pos_adl_start`：ADL begins due to the volume of liquidation orders falls to a certain level (only applicable to premarket symbols)   
`adl_end`: ADL ends   
Only applicable when type is `adl`~~(Deprecated, returns empty values)  
> ts | String | The update timestamp of security fund. Unix timestamp format in milliseconds, e.g. `1597026383085`  
The `regular_update` type has been removed. The `adl` and `platform_revenue` types are deprecated and currently return empty values; they will be removed in a future update. The `amt` field presents the difference in security fund balance when the `type` is `liquidation_balance_deposit` or `bankruptcy_loss`, which is generated once per day around 08:00 am (UTC). 

### Unit convert

Convert the crypto value to the number of contracts, or vice versa

#### Rate Limit: 10 requests per 2 seconds

#### Rate limit rule: IP

#### HTTP Request

`GET /api/v5/public/convert-contract-coin`

> Request Example
    
    
    GET /api/v5/public/convert-contract-coin?instId=BTC-USD-SWAP&px=35000&sz=0.888
    
    
    
    import okx.PublicData as PublicData
    
    flag = "0"  # Production trading: 0, Demo trading: 1
    
    publicDataAPI = PublicData.PublicAPI(flag=flag)
    
    
    # Convert the crypto value to the number of contracts, or vice versa
    result = publicDataAPI.get_convert_contract_coin(
        instId="BTC-USD-SWAP",
        px="35000",
        sz="0.888"
    )
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
type | String | No | Convert type  
`1`: Convert currency to contract  
`2`: Convert contract to currency  
The default is `1`  
instId | String | Yes | Instrument ID  
only applicable to `FUTURES`/`SWAP`/`OPTION`  
sz | String | Yes | Quantity to buy or sell  
It is quantity of currency while converting currency to contract;   
It is quantity of contract while converting contract to currency.  
px | String | Conditional | Order price  
For crypto-margined contracts, it is necessary while converting.  
For USDT-margined contracts, it is necessary while converting between usdt and contract.  
It is optional while converting between coin and contract.   
For OPTION, it is optional.  
unit | String | No | The unit of currency  
`coin`  
`usds`: USDT/USDC  
The default is `coin`, only applicable to USDⓈ-margined contracts from `FUTURES`/`SWAP`  
opType | String | No | Order type  
`open`: round down sz when opening positions   
`close`: round sz to the nearest when closing positions   
The default is `close`   
Applicable to `FUTURES` `SWAP`  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "instId": "BTC-USD-SWAP",
                "px": "35000",
                "sz": "311",
                "type": "1",
                "unit": "coin"
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
type | String | Convert type   
`1`: Convert currency to contract  
`2`: Convert contract to currency  
instId | String | Instrument ID  
px | String | Order price  
sz | String | Quantity to buy or sell  
It is quantity of contract while converting currency to contract  
It is quantity of currency while contract to currency.  
unit | String | The unit of currency  
`coin`  
`usds`: USDT/USDC  
  
### Get instrument tick bands

Get instrument tick bands information

#### Rate Limit: 5 requests per 2 seconds

#### Rate limit rule: IP

#### HTTP Request

`GET /api/v5/public/instrument-tick-bands`

> Request Example
    
    
    GET /api/v5/public/instrument-tick-bands?instType=OPTION
    
    
    
    GET /api/v5/public/instrument-tick-bands?instType=EVENTS
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
instType | String | Yes | Instrument type  
`OPTION`  
`EVENTS`  
instFamily | String | No | Instrument family  
Only applicable to `OPTION`  
  
> Response Example
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "instType": "OPTION",
                "instFamily": "BTC-USD",
                "tickBand": [
                    {
                        "minPx": "0",
                        "maxPx": "100",
                        "tickSz": "0.1"
                    },
                    {
                        "minPx": "100",
                        "maxPx": "10000",
                        "tickSz": "1"
                    }
                ]
            },
            {
                "instType": "OPTION",
                "instFamily": "ETH-USD",
                "tickBand": [
                    {
                        "minPx": "0",
                        "maxPx": "100",
                        "tickSz": "0.1"
                    },
                    {
                        "minPx": "100",
                        "maxPx": "10000",
                        "tickSz": "1"
                    }
                ]
            }
        ]
    }
    
    

> Response Example: EVENTS
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "instType": "EVENTS",
                "instFamily": "",
                "tickBand": [
                    {
                        "minPx": "0.001",
                        "maxPx": "0.04",
                        "tickSz": "0.001"
                    },
                    {
                        "minPx": "0.04",
                        "maxPx": "0.96",
                        "tickSz": "0.01"
                    },
                    {
                        "minPx": "0.96",
                        "maxPx": "0.999",
                        "tickSz": "0.001"
                    }
                ]
            }
        ]
    }
    
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
instType | String | Instrument type  
instFamily | String | Instrument family. Only applicable to `OPTION`  
tickBand | Array of objects | Tick size band. For `EVENTS`, returns unified tick bands applicable to all event contracts.  
> minPx | String | Minimum price while placing an order  
> maxPx | String | Maximum price while placing an order  
> tickSz | String | Tick size, e.g. `0.0001`  
  
### Get premium history

It will return premium data in the past 6 months.

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: IP

#### HTTP Request

`GET /api/v5/public/premium-history`

> Request Example
    
    
    GET /api/v5/public/premium-history?instId=BTC-USDT-SWAP
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
instId | String | Yes | Instrument ID, e.g. `BTC-USDT-SWAP`  
Applicable to `SWAP`  
after | String | No | Pagination of data to return records earlier than the requested ts(not included)  
before | String | No | Pagination of data to return records newer than the requested ts(not included)  
limit | String | No | Number of results per request. The maximum is `100`. The default is `100`.  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "instId": "BTC-USDT-SWAP",
                "premium": "0.0000578896878167",
                "ts": "1713925924000"
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
instId | String | Instrument ID, e.g. `BTC-USDT-SWAP`  
premium | String | Premium index  
formula: [Max (0, Impact bid price – Index price) – Max (0, Index price – Impact ask price)] / Index price  
ts | String | Data generation time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
  
### Get index tickers

Retrieve index tickers.

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: IP

#### HTTP Request

`GET /api/v5/market/index-tickers`

> Request Example
    
    
    GET /api/v5/market/index-tickers?instId=BTC-USDT
    
    
    
    import okx.MarketData as MarketData
    
    flag = "0"  # Production trading:0 , demo trading:1
    
    marketDataAPI =  MarketData.MarketAPI(flag=flag)
    
    # Retrieve index tickers
    result = marketDataAPI.get_index_tickers(
        instId="BTC-USDT"
    )
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
quoteCcy | String | Conditional | Quote currency   
Currently there is only an index with `USD/USDT/BTC/USDC` as the quote currency.  
instId | String | Conditional | Index, e.g. `BTC-USD`  
Either `quoteCcy` or `instId` is required.   
Same as `uly`.  
  
> Response Example
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "instId": "BTC-USDT",
                "idxPx": "43350",
                "high24h": "43649.7",
                "sodUtc0": "43444.1",
                "open24h": "43640.8",
                "low24h": "43261.9",
                "sodUtc8": "43328.7",
                "ts": "1649419644492"
            }
        ]
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
instId | String | Index  
idxPx | String | Latest index price  
high24h | String | Highest price in the past 24 hours  
low24h | String | Lowest price in the past 24 hours  
open24h | String | Open price in the past 24 hours  
sodUtc0 | String | Open price in the UTC 0  
sodUtc8 | String | Open price in the UTC 8  
ts | String | Index price update time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
  
### Get index candlesticks

Retrieve the candlestick charts of the index. This endpoint can retrieve the latest 1,440 data entries. Charts are returned in groups based on the requested bar. 

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: IP

#### HTTP Request

`GET /api/v5/market/index-candles`

> Request Example
    
    
    GET /api/v5/market/index-candles?instId=BTC-USD
    
    
    
    import okx.MarketData as MarketData
    
    flag = "0"  # Production trading:0 , demo trading:1
    
    marketDataAPI =  MarketData.MarketAPI(flag=flag)
    
    # Retrieve the candlestick charts of the index
    result = marketDataAPI.get_index_candlesticks(
        instId="BTC-USD"
    )
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
instId | String | Yes | Index, e.g. `BTC-USD`  
Same as `uly`.  
after | String | No | Pagination of data to return records earlier than the requested `ts`  
before | String | No | Pagination of data to return records newer than the requested `ts`. The latest data will be returned when using `before` individually  
bar | String | No | Bar size, the default is `1m`  
e.g. [`1m`/`3m`/`5m`/`15m`/`30m`/`1H`/`2H`/`4H`]   
UTC+8 opening price k-line: [`6H`/`12H`/`1D`/`1W`/`1M`/`3M`]  
UTC+0 opening price k-line: [`6Hutc`/`12Hutc`/`1Dutc`/`1Wutc`/`1Mutc`/`3Mutc`]  
limit | String | No | Number of results per request. The maximum is `100`. The default is `100`  
  
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
            "0"
        ],
        [
            "1597026383085",
            "3.731",
            "3.799",
            "3.494",
            "3.72",
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
confirm | String | The state of candlesticks.  
`0` represents that it is uncompleted, `1` represents that it is completed.  
  
The candlestick data may be incomplete, and should not be polled repeatedly. 

The data returned will be arranged in an array like this: [ts,o,h,l,c,confirm]. 

### Get index candlesticks history

Retrieve the candlestick charts of the index from recent years.

#### Rate Limit: 10 requests per 2 seconds

#### Rate limit rule: IP

#### HTTP Request

`GET /api/v5/market/history-index-candles`

> Request Example
    
    
    GET /api/v5/market/history-index-candles?instId=BTC-USD
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
instId | String | Yes | Index, e.g. `BTC-USD`  
Same as `uly`.  
after | String | No | Pagination of data to return records earlier than the requested `ts`  
before | String | No | Pagination of data to return records newer than the requested `ts`. The latest data will be returned when using `before` individually  
bar | String | No | Bar size, the default is `1m`  
e.g. [1m/3m/5m/15m/30m/1H/2H/4H]   
UTC+8 opening price k-line: [6H/12H/1D/1W/1M]  
UTC+0 opening price k-line: [/6Hutc/12Hutc/1Dutc/1Wutc/1Mutc]  
limit | String | No | Number of results per request. The maximum is `100`; The default is `100`  
  
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
            "1"
        ],
        [
            "1597026383085",
            "3.731",
            "3.799",
            "3.494",
            "3.72",
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
confirm | String | The state of candlesticks.  
`0` represents that it is uncompleted, `1` represents that it is completed.  
  
The data returned will be arranged in an array like this: [ts,o,h,l,c,confirm]. 

### Get mark price candlesticks

Retrieve the candlestick charts of mark price. This endpoint can retrieve the latest 1,440 data entries. Charts are returned in groups based on the requested bar.

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: IP

#### HTTP Request

`GET /api/v5/market/mark-price-candles`

> Request Example
    
    
    GET /api/v5/market/mark-price-candles?instId=BTC-USD-SWAP
    
    
    
    import okx.MarketData as MarketData
    
    flag = "0"  # Production trading:0 , demo trading:1
    
    marketDataAPI =  MarketData.MarketAPI(flag=flag)
    
    # Retrieve the candlestick charts of mark price
    result = marketDataAPI.get_mark_price_candlesticks(
        instId="BTC-USD-SWAP"
    )
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
instId | String | Yes | Instrument ID, e.g. `BTC-USD-SWAP`  
after | String | No | Pagination of data to return records earlier than the requested `ts`  
before | String | No | Pagination of data to return records newer than the requested `ts`. The latest data will be returned when using `before` individually  
bar | String | No | Bar size, the default is `1m`  
e.g. [1m/3m/5m/15m/30m/1H/2H/4H]   
UTC+8 opening price k-line: [6H/12H/1D/1W/1M/3M]  
UTC+0 opening price k-line: [6Hutc/12Hutc/1Dutc/1Wutc/1Mutc/3Mutc]  
limit | String | No | Number of results per request. The maximum is `100`; The default is `100`  
  
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
            "0"
        ],
        [
            "1597026383085",
            "3.731",
            "3.799",
            "3.494",
            "3.72",
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
confirm | String | The state of candlesticks.  
`0` represents that it is uncompleted, `1` represents that it is completed.  
  
The candlestick data may be incomplete, and should not be polled repeatedly. 

The data returned will be arranged in an array like this: [ts,o,h,l,c,confirm] 

### Get mark price candlesticks history

Retrieve the candlestick charts of mark price from recent years.

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: IP

#### HTTP Request

`GET /api/v5/market/history-mark-price-candles`

> Request Example
    
    
    GET /api/v5/market/history-mark-price-candles?instId=BTC-USD-SWAP
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
instId | String | Yes | Instrument ID, e.g. `BTC-USD-SWAP`  
after | String | No | Pagination of data to return records earlier than the requested `ts`  
before | String | No | Pagination of data to return records newer than the requested `ts`. The latest data will be returned when using `before` individually  
bar | String | No | Bar size, the default is `1m`  
e.g. [1m/3m/5m/15m/30m/1H/2H/4H]   
UTC+8 opening price k-line: [6H/12H/1D/1W/1M]  
UTC+0 opening price k-line: [6Hutc/12Hutc/1Dutc/1Wutc/1Mutc]  
limit | String | No | Number of results per request. The maximum is `100`; The default is `100`  
  
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
            "1"
        ],
        [
            "1597026383085",
            "3.731",
            "3.799",
            "3.494",
            "3.72",
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
confirm | String | The state of candlesticks.  
`0` represents that it is uncompleted, `1` represents that it is completed.  
  
The data returned will be arranged in an array like this: [ts,o,h,l,c,confirm] 

### Get exchange rate

This interface provides the average exchange rate data for 2 weeks

#### Rate Limit: 1 request per 2 seconds

#### Rate limit rule: IP

#### HTTP Request

`GET /api/v5/market/exchange-rate`

> Request Example
    
    
    GET /api/v5/market/exchange-rate
    
    
    
    import okx.MarketData as MarketData
    
    flag = "0"  # Production trading:0 , demo trading:1
    
    marketDataAPI =  MarketData.MarketAPI(flag=flag)
    
    # Retrieve average exchange rate data for 2 weeks
    result = marketDataAPI.get_exchange_rate()
    print(result)
    

> Response Example
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "usdCny": "7.162"
            }
        ]
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
usdCny | String | Exchange rate  
  
### Get index components

Get the index component information data on the market

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: IP

#### HTTP Request

`GET /api/v5/market/index-components`

> Request Example
    
    
    GET /api/v5/market/index-components?index=BTC-USD
    
    
    
    import okx.MarketData as MarketData
    
    flag = "0"  # Production trading:0 , demo trading:1
    
    marketDataAPI =  MarketData.MarketAPI(flag=flag)
    
    # Get the index component information data on the market
    result = marketDataAPI.get_index_components(
        index="BTC-USD"
    )
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
index | String | Yes | index, e.g `BTC-USDT`  
Same as `uly`.  
  
> Response Example
    
    
    {
        "code": "0",
        "msg": "",
        "data": {
            "components": [
                {
                    "symbol": "BTC/USDT",
                    "symPx": "52733.2",
                    "wgt": "0.25",
                    "cnvPx": "52733.2",
                    "exch": "OKX"
                },
                {
                    "symbol": "BTC/USDT",
                    "symPx": "52739.87000000",
                    "wgt": "0.25",
                    "cnvPx": "52739.87000000",
                    "exch": "Binance"
                },
                {
                    "symbol": "BTC/USDT",
                    "symPx": "52729.1",
                    "wgt": "0.25",
                    "cnvPx": "52729.1",
                    "exch": "Huobi"
                },
                {
                    "symbol": "BTC/USDT",
                    "symPx": "52739.47929397",
                    "wgt": "0.25",
                    "cnvPx": "52739.47929397",
                    "exch": "Poloniex"
                }
            ],
            "last": "52735.4123234925",
            "index": "BTC-USDT",
            "ts": "1630985335599"
        }
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
index | String | Index  
last | String | Latest Index Price  
ts | String | Data generation time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
components | Array of objects | Components  
> exch | String | Name of Exchange  
> symbol | String | Name of Exchange Trading Pairs  
> symPx | String | Price of Exchange Trading Pairs  
> wgt | String | Weights  
> cnvPx | String | Price converted to index  
  
### Get economic calendar data

Authentication is required for this endpoint. This endpoint is only supported in production environment. 

Get the macro-economic calendar data within 3 months. Historical data from 3 months ago is only available to users with trading fee tier VIP1 and above.

#### Rate Limit: 1 request per 5 seconds

#### Rate limit rule: IP

#### HTTP Request

`GET /api/v5/public/economic-calendar`

> Request Example
    
    
    GET /api/v5/public/economic-calendar
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
region | string | No | Country, region or entity   
`afghanistan`, `albania`, `algeria`, `andorra`, `angola`, `antigua_and_barbuda`, `argentina`, `armenia`, `aruba`, `australia`, `austria`, `azerbaijan`, `bahamas`, `bahrain`, `bangladesh`, `barbados`, `belarus`, `belgium`, `belize`, `benin`, `bermuda`, `bhutan`, `bolivia`, `bosnia_and_herzegovina`, `botswana`, `brazil`, `brunei`, `bulgaria`, `burkina_faso`, `burundi`, `cambodia`, `cameroon`, `canada`, `cape_verde`, `cayman_islands`, `central_african_republic`, `chad`, `chile`, `china`, `colombia`, `comoros`, `congo`, `costa_rica`, `croatia`, `cuba`, `cyprus`, `czech_republic`, `denmark`, `djibouti`, `dominica`, `dominican_republic`, `east_timor`, `ecuador`, `egypt`, `el_salvador`, `equatorial_guinea`, `eritrea`, `estonia`, `ethiopia`, `euro_area`, `european_union`, `faroe_islands`, `fiji`, `finland`, `france`, `g20`, `g7`, `gabon`, `gambia`, `georgia`, `germany`, `ghana`, `greece`, `greenland`, `grenada`, `guatemala`, `guinea`, `guinea_bissau`, `guyana`, `hungary`, `haiti`, `honduras`, `hong_kong`, `hungary`, `imf`, `indonesia`, `iceland`, `india`, `indonesia`, `iran`, `iraq`, `ireland`, `isle_of_man`, `israel`, `italy`, `ivory_coast`, `jamaica`, `japan`, `jordan`, `kazakhstan`, `kenya`, `kiribati`, `kosovo`, `kuwait`, `kyrgyzstan`, `laos`, `latvia`, `lebanon`, `lesotho`, `liberia`, `libya`, `liechtenstein`, `lithuania`, `luxembourg`, `macau`, `macedonia`, `madagascar`, `malawi`, `malaysia`, `maldives`, `mali`, `malta`, `mauritania`, `mauritius`, `mexico`, `micronesia`, `moldova`, `monaco`, `mongolia`, `montenegro`, `morocco`, `mozambique`, `myanmar`, `namibia`, `nepal`, `netherlands`, `new_caledonia`, `new_zealand`, `nicaragua`, `niger`, `nigeria`, `north_korea`, `northern_mariana_islands`, `norway`, `opec`, `oman`, `pakistan`, `palau`, `palestine`, `panama`, `papua_new_guinea`, `paraguay`, `peru`, `philippines`, `poland`, `portugal`, `puerto_rico`, `qatar`, `russia`, `republic_of_the_congo`, `romania`, `russia`, `rwanda`, `slovakia`, `samoa`, `san_marino`, `sao_tome_and_principe`, `saudi_arabia`, `senegal`, `serbia`, `seychelles`, `sierra_leone`, `singapore`, `slovakia`, `slovenia`, `solomon_islands`, `somalia`, `south_africa`, `south_korea`, `south_sudan`, `spain`, `sri_lanka`, `st_kitts_and_nevis`, `st_lucia`, `sudan`, `suriname`, `swaziland`, `sweden`, `switzerland`, `syria`, `taiwan`, `tajikistan`, `tanzania`, `thailand`, `togo`, `tonga`, `trinidad_and_tobago`, `tunisia`, `turkey`, `turkmenistan`, `uganda`, `ukraine`, `united_arab_emirates`, `united_kingdom`, `united_states`, `uruguay`, `uzbekistan`, `vanuatu`, `venezuela`, `vietnam`, `world`, `yemen`, `zambia`, `zimbabwe`  
importance | string | No | Level of importance   
`1`: low   
`2`: medium   
`3`: high  
before | String | No | Pagination of data to return records newer than the requested ts based on the date parameter. Unix timestamp format in milliseconds.  
after | String | No | Pagination of data to return records earlier than the requested ts based on the date parameter. Unix timestamp format in milliseconds. The default is the timestamp of the request moment.  
limit | String | No | Number of results per request. The maximum is 100. The default is 100.  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "actual": "7.8%",
                "calendarId": "330631",
                "category": "Harmonised Inflation Rate YoY",
                "ccy": "",
                "date": "1700121600000",
                "dateSpan": "0",
                "event": "Harmonised Inflation Rate YoY",
                "forecast": "7.8%",
                "importance": "1",
                "prevInitial": "",
                "previous": "9%",
                "refDate": "1698710400000",
                "region": "Slovakia",
                "uTime": "1700121605007",
                "unit": "%"
            }
        ],
        "msg": ""
    }
    
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
calendarId | string | Calendar ID  
date | string | Estimated release time of the value of actual field, millisecond format of Unix timestamp, e.g. `1597026383085`  
region | string | Country, region or entity  
category | string | Category name  
event | string | Event name  
refDate | string | Date for which the datapoint refers to  
actual | string | The actual value of this event  
previous | string | Latest actual value of the previous period   
The value will be revised if revision is applicable  
forecast | string | Average forecast among a representative group of economists  
dateSpan | string | `0`: The time of the event is known  
`1`: we only know the date of the event, the exact time of the event is unknown.  
importance | string | Level of importance   
`1`: low   
`2`: medium   
`3`: high  
uTime | string | Update time of this record, millisecond format of Unix timestamp, e.g. `1597026383085`  
prevInitial | string | The initial value of the previous period   
Only applicable when revision happens  
ccy | string | Currency of the data  
unit | string | Unit of the data  
  
### Get historical market data

**Data availability**  
Historical data backfill is currently in progress. Data availability may vary by module, instrument, and time period. The dataset will be continuously expanded to provide more comprehensive historical coverage.  **Legacy data format notice**  
For module 1 (trade history), some old historical files may contain column headers with both Chinese characters along with English column names. All the Chinese characters will be removed once the data backfill is done. Please account for this when parsing the data.  **Data release schedule**  
Most data for modules 1, 2, 3, 11 is typically available on T+2; order book data is typically available on T+3. 

Retrieve historical market data for OKX.

#### Rate Limit: 5 requests per 2 seconds

#### Rate limit rule: IP

#### HTTP Request

`GET /api/v5/public/market-data-history`

> Request Example
    
    
    GET /api/v5/public/market-data-history?module=1&instType=SWAP&instFamilyList=BTC-USDT&dateAggrType=daily&begin=1756604295000&end=1756777095000
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
module | String | Yes | Data module type  
`1`: Tick-by-tick trade history  
`2`: 1-minute candlestick  
`3`: Funding rate  
`4`: 400-level orderbook  
`5`: 5000-level orderbook (from Nov 1, 2025)  
`6`: 50-level orderbook (will gradually be deprecated, please use module = `4`,`5` instead)  
`11`: Borrowing rate  
instType | String | Yes | Instrument type  
`SPOT`  
`FUTURES`  
`SWAP`  
`OPTION`  
instIdList | String | Conditional | List of instrument IDs, e.g. `BTC-USDT`, or `ANY` for all instruments (`ANY` is only supported for module = `1`, `2`, `3`, `11` & dateAggrType = `daily`)  
Multiple instrument IDs should be separated by commas, e.g. `BTC-USDT,ETH-USDT`  
Maximum length = 10  
Only applicable when instType = `SPOT`  
instFamilyList | String | Conditional | List of instrument families, e.g. `BTC-USDT`, or `ANY` for all instruments (`ANY` is only supported for module = `1`, `2`, `3`, `11` & dateAggrType = `daily`)  
Multiple instrument families should be separated by commas, e.g. `BTC-USDT,ETH-USDT`  
Maximum length = 10 (= 1when module = `6` & instType = `OPTION`)  
Only applicable when instType ≠ `SPOT`  
dateAggrType | String | Yes | Date aggregation type  
`daily` (not supported for module = `3` & instFamilyList ≠ `ANY`)  
`monthly` (not supported for module = `6`)  
begin | String | Yes | Begin timestamp. Unix timestamp format in milliseconds (inclusive)  
Maximum range: 20 days for daily, 20 months for monthly  
end | String | Yes | End timestamp. Unix timestamp format in milliseconds (inclusive)  
When module = `6` & instType = `OPTION`, only returns data for the day specified by `end`  
  
> Response Example
    
    
    {
      "code": "0",
      "data": [{
        "dateAggrType": "daily",
        "details": [{
          "dateRangeEnd": "1756656000000",
          "dateRangeStart": "1756569600000",
          "groupDetails": [{
            "dateTs": "1756656000000",
            "filename": "BTC-USDT-SWAP-trades-2025-09-01.zip",
            "sizeMB": "10.82",
            "url": "https://static.okx.com/cdn/okex/traderecords/trades/daily/20250901/BTC-USDT-SWAP-trades-2025-09-01.zip"
          },
          {
            "dateTs": "1756569600000",
            "filename": "BTC-USDT-SWAP-trades-2025-08-31.zip",
            "sizeMB": "4.82",
            "url": "https://static.okx.com/cdn/okex/traderecords/trades/daily/20250831/BTC-USDT-SWAP-trades-2025-08-31.zip"
          }],
          "groupSizeMB": "15.64",
          "instFamily": "BTC-USDT",
          "instId": "",
          "instType": "SWAP"
        }],
        "totalSizeMB": "15.64",
        "ts": "1756882260390"
      }],
      "msg": ""
    }
    

> Response Example when no data files are available
    
    
    {
        "code": "0",
        "data": [
            {
                "dateAggrType": "monthly",
                "details": [],
                "totalSizeMB": "0",
                "ts": "1756889595507"
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
ts | String | Response timestamp, Unix timestamp format in milliseconds  
totalSizeMB | String | Total size of all data files in MB  
dateAggrType | String | Date aggregation type  
`daily`  
`monthly`  
details | Array |   
> instId | String | Instrument ID  
> instFamily | String | Instrument family  
> dateRangeStart | String | Data range start date, Unix timestamp format in milliseconds (inclusive)  
> dateRangeEnd | String | Data range end date, Unix timestamp format in milliseconds (inclusive)  
> groupSizeMB | String | Data group size in MB  
> groupDetails | Array |   
>> filename | String | Data file name, e.g. `BTC-USDT-SWAP-trades-2025-05-15.zip`  
>> dataTs | String | Data date timestamp, Unix timestamp format in milliseconds  
>> sizeMB | String | File size in MB  
>> url | String | Download URL  
**Data query rules**  
• Only the date portion (yyyy-mm-dd) of timestamps is used; time components are ignored  
• Both begin and end timestamps are inclusive  
• Data is returned in reverse chronological order (closer to end first)  
• If the query exceeds record limits, data closest to the end timestamp is returned  
• **Exception:** When module = 6 & instType = OPTION, only data for the day specified by the end is returned  **Timezone specifications for timestamp parsing**  
When converting Unix timestamps to dates, the following timezone conventions are applied to all timestamp fields (begin, end, dateRangeStart, dateRangeEnd, dataTs):  
• **Orderbook data** (modules 4, 5, 6): UTC+0  
• **All other data modules** (modules 1, 2, 3, 11): UTC+8 

### Get MM instrument types

Retrieve the list of MM Program instrument type classifications for SPOT and SWAP instruments.

#### Rate Limit: 5 requests per 2 seconds

#### Rate limit rule: IP

#### HTTP Request

`GET /api/v5/public/mm-instrument-types`

> Request Example
    
    
    GET /api/v5/public/mm-instrument-types?instType=SWAP
    
    
    
    import okx.PublicData as PublicData
    
    flag = "0"  # Production trading: 0, Demo trading: 1
    
    publicDataAPI = PublicData.PublicAPI(flag=flag)
    
    # Retrieve the list of MM Program instrument type classifications
    result = publicDataAPI.get_mm_instrument_types(
        instType="SWAP"
    )
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
instType | String | No | Instrument type.  
`SPOT`  
`SWAP`  
When not specified, returns all types.  
instId | String | No | Instrument ID, e.g. `BTC-USDT`, `BTC-USDT-SWAP`.  
When specified, returns at most one record.  
  
> Response Example
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "instId": "BTC-USDT-SWAP",
                "instType": "SWAP",
                "pairType": "A"
            },
            {
                "instId": "ETH-USDT-SWAP",
                "instType": "SWAP",
                "pairType": "A"
            },
            {
                "instId": "XAU-USDT-SWAP",
                "instType": "SWAP",
                "pairType": "B-TradFi"
            }
        ]
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
instId | String | Instrument ID, e.g. `BTC-USDT-SWAP`  
instType | String | Instrument type.  
`SPOT`  
`SWAP`  
pairType | String | MM Program classification type.  
`A`: High liquidity tier  
`B-Crypto`: Medium/low liquidity crypto assets  
`B-TradFi`: Traditional finance instruments (SWAP only)  
  
## WebSocket

### Instruments channel

The triggering scenarios for incremental data are:  
1\. When there is any change to the instrument’s state (such as delivery of FUTURES, exercise of OPTION, listing of new contracts / trading pairs, trading suspension, etc.)  
2\. When the trading parameters change (tickSz,minSz,maxMktSz)  
3\. When the expTime or listTime changes  

#### URL Path

/ws/v5/public

> Request Example
    
    
    {
      "id": "1512",
      "op": "subscribe",
      "args": [
        {
          "channel": "instruments",
          "instType": "SPOT"
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
              "channel": "instruments",
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
`instruments`  
> instType | String | Yes | Instrument type  
`SPOT`  
`MARGIN`  
`SWAP`  
`FUTURES`  
`OPTION`  
`EVENTS`  
  
> Successful Response Example
    
    
    {
      "id": "1512",
      "event": "subscribe",
      "arg": {
        "channel": "instruments",
        "instType": "SPOT"
      },
      "connId": "a4d3ae55"
    }
    

> Failure Response Example
    
    
    {
      "id": "1512",
      "event": "error",
      "code": "60012",
      "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{ \"channel\" : \"instruments\", \"instType\" : \"FUTURES\"}]}",
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
`OPTION`  
`EVENTS`  
code | String | No | Error code  
msg | String | No | Error message  
connId | String | Yes | WebSocket connection ID  
  
> Push Data Example
    
    
    {
      "arg": {
        "channel": "instruments",
        "instType": "SPOT"
      },
      "data": [
        {
            "alias": "",
            "auctionEndTime": "",
            "baseCcy": "BTC",
            "category": "1",
            "ctMult": "",
            "ctType": "",
            "ctVal": "",
            "ctValCcy": "",
            "contTdSwTime": "1704876947000",
            "expTime": "",
            "futureSettlement": false,
            "groupId": "1",
            "instFamily": "",
            "instId": "BTC-USDT",
            "instType": "SPOT",
            "lever": "10",
            "listTime": "1606468572000",
            "lotSz": "0.00000001",
            "maxIcebergSz": "9999999999.0000000000000000",
            "maxLmtAmt": "1000000",
            "maxLmtSz": "9999999999",
            "maxMktAmt": "1000000",
            "maxMktSz": "",
            "maxStopSz": "",
            "maxTriggerSz": "9999999999.0000000000000000",
            "maxTwapSz": "9999999999.0000000000000000",
            "minSz": "0.00001",
            "optType": "",
            "openType": "call_auction",
            "preMktSwTime": "",
            "quoteCcy": "USDT",
            "settleCcy": "",
            "state": "live",
            "ruleType": "normal",
            "stk": "",
            "tickSz": "0.1",
            "uly": "",
            "instIdCode": 1000000000,
            "instCategory": "1",
            "upcChg": [
                {
                    "param": "tickSz",
                    "newValue": "0.0001",
                    "effTime": "1704876947000"
                }
            ]
        }
      ]
    }
    

#### Push data parameters

Parameter | Type | Description  
---|---|---  
arg | Object | Subscribed channel  
> channel | String | Channel name  
> instType | String | Instrument type  
data | Array of objects | Subscribed data  
> instType | String | Instrument type  
> seriesId | String | Series ID, e.g. `BTC-ABOVE-DAILY`. Only applicable to `EVENTS`  
> instId | String | Instrument ID, e.g. `BTC-UST`  
> uly | String | Underlying, e.g. `BTC-USD`   
Only applicable to `FUTURES`/`SWAP`/`OPTION`  
> groupId | String | Instrument trading fee group ID  
Spot:  
`1`: Spot USDT  
`2`: Spot USDC & Crypto  
`3`: Spot TRY  
`4`: Spot EUR  
`5`: Spot BRL  
`7`: Spot AED  
`8`: Spot AUD  
`9`: Spot USD  
`10`: Spot SGD  
`11`: Spot zero  
`12`: Spot group one  
`13`: Spot group two  
`14`: Spot group three  
`15`: Spot special rule  
  
Expiry futures:  
`1`: Expiry futures crypto-margined  
`2`: Expiry futures USDT-margined  
`3`: Expiry futures USDC-margined  
`4`: Expiry futures premarket  
`5`: Expiry futures group one  
`6`: Expiry futures group two  
  
Perpetual futures:  
`1`: Perpetual futures crypto-margined  
`2`: Perpetual futures USDT-margined  
`3`: Perpetual futures USDC-margined  
`4`: Perpetual futures group one  
`5`: Perpetual futures group two  
`6`: Stock perpetual futures   
  
Options:  
`1`: Options crypto-margined  
`2`: Options USDC-margined  
  
**instType and groupId should be used together to determine a trading fee group. Users should use this endpoint together with[fee rates endpoint](/docs-v5/en/#trading-account-rest-api-get-fee-rates) to get the trading fee of a specific symbol.**   
  
**Some enum values may not apply to you; the actual return values shall prevail.**  
> instFamily | String | Instrument family, e.g. `BTC-USD`   
Only applicable to `FUTURES`/`SWAP`/`OPTION`  
> category | String | Currency category. Note: this parameter is already deprecated  
> baseCcy | String | Base currency, e.g. `BTC` in `BTC-USDT`   
Only applicable to `SPOT`/`MARGIN`  
> quoteCcy | String | Quote currency, e.g. `USDT` in `BTC-USDT`   
Only applicable to `SPOT`/`MARGIN`  
> settleCcy | String | Settlement and margin currency, e.g. `BTC`   
Only applicable to `FUTURES`/`SWAP`/`OPTION`  
> ctVal | String | Contract value  
> ctMult | String | Contract multiplier  
> ctValCcy | String | Contract value currency  
> optType | String | Option type  
`C`: Call  
`P`: Put  
Only applicable to `OPTION`  
> stk | String | Strike price  
Only applicable to `OPTION`  
> listTime | String | Listing time  
Only applicable to `FUTURES`/`SWAP`/`OPTION`  
> auctionEndTime | String | ~~The end time of call auction, Unix timestamp format in milliseconds, e.g.`1597026383085`   
Only applicable to `SPOT` that are listed through call auctions, return "" in other cases (deprecated, use contTdSwTime)~~  
> contTdSwTime | String | Continuous trading switch time. The switch time from call auction, prequote to continuous trading, Unix timestamp format in milliseconds. e.g. `1597026383085`.  
Only applicable to `SPOT`/`MARGIN` that are listed through call auction or prequote, return "" in other cases.  
> preMktSwTime | String | The time premarket swap switched to normal swap, Unix timestamp format in milliseconds, e.g. `1597026383085`.   
Only applicable premarket `SWAP`  
> openType | String | Open type  
`fix_price`: fix price opening  
`pre_quote`: pre-quote  
`call_auction`: call auction   
Only applicable to `SPOT`/`MARGIN`, return "" for all other business lines  
> expTime | String | Expiry time  
Applicable to `SPOT`/`MARGIN`/`FUTURES`/`SWAP`/`OPTION`. For `FUTURES`/`OPTION`, it is the delivery/exercise time. It can also be the delisting time of the trading instrument. Update once change.  
> lever | String | Max Leverage  
Not applicable to `SPOT`/`OPTION`, used to distinguish between `MARGIN` and `SPOT`.  
> tickSz | String | Tick size, e.g. `0.0001`.  
For `OPTION`/`EVENTS`, it is the minimum tickSz among tick band.  
> lotSz | String | Lot size  
If it is a derivatives contract, the value is the number of contracts.  
If it is `SPOT`/`MARGIN`, the value is the quantity in `base currency`  
> minSz | String | Minimum order size  
If it is a derivatives contract, the value is the number of contracts.  
If it is `SPOT`/`MARGIN`, the value is the quantity in `base currency`  
> ctType | String | Contract type  
`linear`: linear contract  
`inverse`: inverse contract  
Only applicable to `FUTURES`/`SWAP`  
> alias | String | Contract alias (deprecated — use expTime to obtain the delivery time, will be removed by the end of April 2026)  
`this_week`  
`next_week`  
`this_month`  
`next_month`  
`quarter`  
`next_quarter`  
`this_five_years`: current 5-year contract  
`next_five_years`: next 5-year contract  
Only applicable to `FUTURES`  
> state | String | Instrument status  
`live`  
`suspend`  
`expired`  
`rebase`: can't be traded during rebasing, only applicable to `SWAP`  
`post_only`: only post-only orders are accepted; existing post-only orders can be amended and cancelled. Other order types (market, IOC, FOK, normal limit) are rejected. Only applicable to `SWAP`  
`preopen`. e.g. There will be `preopen` before the Futures and Options new contracts state is live.  
`test`: Test pairs, can't be traded  
`settling`: Settling, only applicable to `EVENTS`  
> ruleType | String | Trading rule types  
`normal`: normal trading  
`pre_market`: pre-market trading  
`rebase_contract`: pre-market rebase contract  
`xperp`: perpetual-style futures, only applicable to certain `FUTURES` contracts  
> maxLmtSz | String | The maximum order quantity of a single limit order.  
If it is a derivatives contract, the value is the number of contracts.  
If it is `SPOT`/`MARGIN`, the value is the quantity in `base currency`.  
> maxMktSz | String | The maximum order quantity of a single market order.  
If it is a derivatives contract, the value is the number of contracts.  
If it is `SPOT`/`MARGIN`, the value is the quantity in `USDT`.  
> maxTwapSz | String | The maximum order quantity of a single TWAP order.  
If it is a derivatives contract, the value is the number of contracts.  
If it is `SPOT`/`MARGIN`, the value is the quantity in `base currency`.  
> maxIcebergSz | String | The maximum order quantity of a single iceBerg order.  
If it is a derivatives contract, the value is the number of contracts.  
If it is `SPOT`/`MARGIN`, the value is the quantity in `base currency`.  
> maxTriggerSz | String | The maximum order quantity of a single trigger order.  
If it is a derivatives contract, the value is the number of contracts.  
If it is `SPOT`/`MARGIN`, the value is the quantity in `base currency`.  
> maxStopSz | String | The maximum order quantity of a single stop market order.  
If it is a derivatives contract, the value is the number of contracts.  
If it is `SPOT`/`MARGIN`, the value is the quantity in `USDT`.  
> futureSettlement | Boolean | Whether daily settlement for expiry feature is enabled  
Applicable to `FUTURES` `cross`  
> instIdCode | Integer | Instrument ID code.   
For simple binary encoding, you must use `instIdCode` instead of `instId`.  
For the same `instId`, it's value may be different between production and demo trading.   
It is `null` when the value is not generated.  
> instCategory | String | The asset category of the instrument’s base asset (the first segment of the instrument ID). For example, for `BTC-USDT-SWAP`, the `instCategory` represents the asset category of `BTC`.   
`1`: Crypto   
`3`: Stocks   
`4`: Commodities   
`5`: Forex   
`6`: Bonds   
`""`: Not available  
> upcChg | Array of objects | Upcoming changes. It is [] when there is no upcoming change.  
>> param | String | The parameter name to be updated.   
`tickSz`  
`minSz`: For `FUTURES`/`SWAP`, `lotSz` will be modified synchronously.  
`maxMktSz`  
>> newValue | String | The parameter value that will replace the current one.  
>> effTime | String | Effective time. Unix timestamp format in milliseconds, e.g. `1597026383085`  
Instrument status will trigger pushing of incremental data from instruments channel. When a new contract is going to be listed, the instrument data of the new contract will be available with status preopen. When a product is going to be delisted (e.g. when a FUTURES contract is settled or OPTION contract is exercised), the instrument status will be changed to expired.  listTime and contTdSwTime  
For spot symbols listed through a call auction or pre-open, listTime represents the start time of the auction or pre-open, and contTdSwTime indicates the end of the auction or pre-open and the start of continuous trading. For other scenarios, listTime will mark the beginning of continuous trading, and contTdSwTime will return an empty value "".  state  
For `SPOT`, `MARGIN`, `SWAP`, and `FUTURES`, the state changes from `preopen` to `live` when the `listTime` is reached. For `OPTION` contracts, the state may change to `live` slightly after `listTime` due to internal processing. It is recommended to verify that `state` is `live` before placing orders. Certain symbols will now have `state:preopen` before they go live. Before going live, the instruments channel will push data for pre-listing symbols with `state:preopen`. If the listing is cancelled, the channel will send full data excluding the cancelled symbol, without additional notification. When the symbol goes live (at or shortly after `listTime` for `OPTION`), the channel will push data with `state:live`. Users can also query the corresponding data via the REST endpoint.  
When a product is going to be delisted (e.g. when a FUTURES contract is settled or OPTION contract is exercised), the instrument will not be available. 

### Event contract markets channel

Pushes event contract market status updates and floorStrike generation. No initial snapshot push.

#### URL Path

/ws/v5/public

> Request Example
    
    
    {
        "op": "subscribe",
        "args": [
            {
                "channel": "event-contract-markets",
                "instType": "EVENTS"
            }
        ]
    }
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
id | String | No | Unique identifier of the message. Provided by client. Returned in response. Alphanumeric, 1-32 characters.  
op | String | Yes | Operation.  
`subscribe`  
`unsubscribe`  
args | Array of objects | Yes | List of subscribed channels  
> channel | String | Yes | Channel name.  
`event-contract-markets`  
> instType | String | Yes | Instrument type.  
`EVENTS`  
  
> Successful Response Example
    
    
    {
        "id": "1512",
        "event": "subscribe",
        "arg": {
            "channel": "event-contract-markets",
            "instType": "EVENTS"
        },
        "connId": "a4d3ae55"
    }
    

> Failure Response Example
    
    
    {
        "id": "1512",
        "event": "error",
        "code": "60012",
        "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{\"channel\": \"event-contract-markets\", \"instType\": \"EVENTS\"}]}",
        "connId": "a4d3ae55"
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
id | String | Unique identifier of the message  
event | String | Event.  
`subscribe`  
`unsubscribe`  
`error`  
arg | Object | Subscribed channel  
> channel | String | Channel name  
> instType | String | Instrument type  
code | String | Error code  
msg | String | Error message  
connId | String | WebSocket connection ID  
  
> Push Data Example
    
    
    {
        "arg": {
            "channel": "event-contract-markets"
        },
        "data": [
            {
                "seriesId": "BTC-ABOVE-DAILY",
                "eventId": "BTC-ABOVE-DAILY-260224-1600",
                "instId": "BTC-ABOVE-DAILY-260224-1600-65000",
                "listTime": "1769697132335",
                "fixTime": "",
                "expTime": "1769697132335",
                "state": "live",
                "outcome": "0",
                "floorStrike": "120000",
                "capStrike": "",
                "settleValue": "",
                "disputed": false,
                "hitDir": ""
            }
        ]
    }
    

#### Push Data Parameters

Parameter | Type | Description  
---|---|---  
arg | Object | Subscribed channel  
> channel | String | Channel name  
data | Array of objects | Subscribed data  
> seriesId | String | Series ID, e.g. `BTC-ABOVE-DAILY`  
> eventId | String | Event ID, e.g. `BTC-ABOVE-DAILY-260224-1600`  
> instId | String | Instrument ID, e.g. `BTC-ABOVE-DAILY-260224-1600-65000`  
> listTime | String | Listing time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
> fixTime | String | Strike price fixing time, Unix timestamp format in milliseconds, e.g. `1597026383085`. Only applicable to `price_up_down` settlement method.  
> expTime | String | Strike time for this event, Unix timestamp format in milliseconds, e.g. `1597026383085`. Updated once the market is settled.  
> state | String | Market state.  
`preopen`  
`live`  
`settling`  
`expired`  
> outcome | String | Market outcome.  
`0`: Not available  
`1`: YES  
`2`: NO.  
`1`/`2` only applicable when state is `expired`  
> floorStrike | String | Minimum expiration value that leads to a YES outcome  
> capStrike | String | Maximum expiration value that leads to a YES outcome for `between` method. `"INF"` indicates no upper bound (the topmost bracket).  
Returns `""` for non-`between` methods.  
> settleValue | String | Settlement value  
Only return when the state is `expired`  
> disputed | Boolean | Whether the market has been disputed.  
`true`  
`false`  
> hitDir | String | Hit direction. Only applicable when the settlement method is `hit`.  
`up`: price hit from below  
`dn`: price hit from above  
`""`: not applicable (non-`hit` methods)  
  
### Open interest channel

Retrieve the open interest. Data will be pushed every 3 seconds when there are updates.

#### URL Path

/ws/v5/public

> Request Example
    
    
    {
      "id": "1512",
      "op": "subscribe",
      "args": [
        {
          "channel": "open-interest",
          "instId": "LTC-USD-SWAP"
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
              "channel": "open-interest",
              "instId": "LTC-USD-SWAP"
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
`open-interest`  
> instId | String | Yes | Instrument ID  
  
> Successful Response Example
    
    
    {
      "id": "1512",
      "event": "subscribe",
      "arg": {
          "channel": "open-interest",
          "instId": "LTC-USD-SWAP"
      },
      "connId": "a4d3ae55"
    }
    

> Failure Response Example
    
    
    {
      "id": "1512",
      "event": "error",
      "code": "60012",
      "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{ \"channel\" : \"open-interest\", \"instId\" : \"LTC-USD-SWAP\"}]}",
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
            "channel": "open-interest",
            "instId": "BTC-USDT-SWAP"
        },
        "data": [
            {
                "instId": "BTC-USDT-SWAP",
                "instType": "SWAP",
                "oi": "2216113.01000000309",
                "oiCcy": "22161.1301000000309",
                "oiUsd": "1939251795.54769270396321",
                "ts": "1743041250440"
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
> instId | String | Instrument ID, e.g. `BTC-USDT-SWAP`  
> oi | String | Open interest, in units of contracts.  
> oiCcy | String | Open interest, in currency units, like BTC.  
> oiUsd | String | Open interest in number of USD  
> ts | String | The time when the data was updated, Unix timestamp format in milliseconds, e.g. `1597026383085`  
  
### Funding rate channel

Retrieve funding rate. Data will be pushed in 30s to 90s.

#### URL Path

/ws/v5/public

> Request Example
    
    
    {
      "id": "1512",
      "op": "subscribe",
      "args": [
        {
          "channel": "funding-rate",
          "instId": "BTC-USD-SWAP"
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
              "channel": "funding-rate",
              "instId": "BTC-USD-SWAP"
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
`funding-rate`  
> instId | String | Yes | Instrument ID  
  
> Successful Response Example
    
    
    {
      "id": "1512",
      "event": "subscribe",
      "arg": {
        "channel": "funding-rate",
        "instId": "BTC-USD-SWAP"
      },
      "connId": "a4d3ae55"
    }
    

> Failure Response Example
    
    
    {
      "id": "1512",
      "event": "error",
      "code": "60012",
      "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{ \"channel\" : \"funding-rate\", \"instId\" : \"BTC-USD-SWAP\"}]}",
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
> channel | String | yes | Channel name  
> instId | String | No | Instrument ID  
code | String | No | Error code  
msg | String | No | Error message  
connId | String | Yes | WebSocket connection ID  
  
> Push Data Example
    
    
    {
       "arg":{
          "channel":"funding-rate",
          "instId":"BTC-USD-SWAP"
       },
       "data":[
          {
             "formulaType": "noRate",
             "fundingRate":"0.0001875391284828",
             "fundingTime":"1700726400000",
             "impactValue": "",
             "instId":"BTC-USD-SWAP",
             "instType":"SWAP",
             "interestRate": "",
             "method": "current_period",
             "maxFundingRate":"0.00375",
             "minFundingRate":"-0.00375",
             "nextFundingRate":"",
             "nextFundingTime":"1700755200000",
             "premium": "0.0001233824646391",
             "settFundingRate":"0.0001699799259033",
             "settState":"settled",
             "ts":"1700724675402"
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
`SWAP`: Perpetual futures  
`FUTURES`: X-Perps futures  
> instId | String | Instrument ID, e.g. `BTC-USD-SWAP`  
> method | String | Funding rate mechanism   
`current_period` ~~  
`next_period`~~(no longer supported)  
> formulaType | String | Formula type  
`noRate`: old funding rate formula  
`withRate`: new funding rate formula  
> fundingRate | String | Current funding rate  
> nextFundingRate | String | ~~Forecasted funding rate for the next period  
The nextFundingRate will be "" if the method is `current_period`~~(no longer supported)  
> fundingTime | String | Settlement time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
> nextFundingTime | String | Forecasted funding time for the next period, Unix timestamp format in milliseconds, e.g. `1597026383085`  
> minFundingRate | String | The lower limit of the predicted funding rate of the next cycle  
> maxFundingRate | String | The upper limit of the predicted funding rate of the next cycle  
> interestRate | String | Interest rate  
> impactValue | String | Depth weighted amount (in the unit of quote currency)  
> settState | String | Settlement state of funding rate   
`processing`   
`settled`  
> settFundingRate | String | If settState = `processing`, it is the funding rate that is being used for current settlement cycle.   
If settState = `settled`, it is the funding rate that is being used for previous settlement cycle  
> premium | String | Premium index  
formula: [Max (0, Impact bid price – Index price) – Max (0, Index price – Impact ask price)] / Index price  
> ts | String | Data return time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
For some altcoins perpetual swaps with significant fluctuations in funding rates, OKX will closely monitor market changes. When necessary, the funding rate collection frequency, currently set at 8 hours, may be adjusted to higher frequencies such as 6 hours, 4 hours, 2 hours, or 1 hour. Thus, users should focus on the difference between `fundingTime` and `nextFundingTime` fields to determine the funding fee interval of a contract. 

### Price limit channel

Retrieve the maximum buy price and minimum sell price of instruments. Data will be pushed every 200ms when there are changes in limits, and will not be pushed when there is no changes on limit.

#### URL Path

/ws/v5/public

> Request Example
    
    
    {
      "id": "1512",
      "op": "subscribe",
      "args": [
        {
          "channel": "price-limit",
          "instId": "LTC-USD-190628"
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
              "channel": "price-limit",
              "instId": "LTC-USD-190628"
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
`price-limit`  
> instId | String | Yes | Instrument ID  
  
> Successful Response Example
    
    
    {
      "id": "1512",
      "event": "subscribe",
      "arg": {
        "channel": "price-limit",
        "instId": "LTC-USD-190628"
      },
      "connId": "a4d3ae55"
    }
    

> Failure Response Example
    
    
    {
      "id": "1512",
      "event": "error",
      "code": "60012",
      "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{ \"channel\" : \"price-limit\", \"instId\" : \"LTC-USD-190628\"}]}",
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
            "channel": "price-limit",
            "instId": "LTC-USD-190628"
        },
        "data": [{
            "instId": "LTC-USD-190628",
            "buyLmt": "200",
            "sellLmt": "300",
            "ts": "1597026383085",
            "enabled": true
        }]
    }
    

#### Push data parameters

**Parameter** | **Type** | **Description**  
---|---|---  
arg | Object | Successfully subscribed channel  
> channel | String | Channel name  
> instId | String | Instrument ID  
data | Array of objects | Subscribed data  
> instType | String | Instrument type  
> instId | String | Instrument ID, e.g. `BTC-USDT`  
> buyLmt | String | Maximum buy price   
Return "" when enabled is false  
> sellLmt | String | Minimum sell price   
Return "" when enabled is false  
> ts | String | Price update time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
> enabled | Boolean | Whether price limit is effective   
`true`: the price limit is effective   
`false`: the price limit is not effective  
  
### Option summary channel

Retrieve detailed pricing information of all OPTION contracts. Data will be pushed at once.

#### URL Path

/ws/v5/public

> Request Example
    
    
    {
      "id": "1512",
      "op": "subscribe",
      "args": [
        {
          "channel": "opt-summary",
          "instFamily": "BTC-USD"
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
              "channel": "opt-summary",
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
`opt-summary`  
> instFamily | String | Yes | Instrument family  
  
> Response Example
    
    
    {
      "id": "1512",
      "event": "subscribe",
      "arg": {
        "channel": "opt-summary",
        "instFamily": "BTC-USD"
      },
      "connId": "a4d3ae55"
    }
    

> Failure example
    
    
    {
      "id": "1512",
      "event": "error",
      "code": "60012",
      "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{ \"channel\" : \"opt-summary\", \"uly\" : \"BTC-USD\"}]}",
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
> instFamily | String | Yes | Instrument family  
code | String | No | Error code  
msg | String | No | Error message  
connId | String | Yes | WebSocket connection ID  
  
> Push Data Example
    
    
    {
        "arg": {
            "channel": "opt-summary",
            "instFamily": "BTC-USD"
        },
        "data": [
            {
                "instType": "OPTION",
                "instId": "BTC-USD-241013-70000-P",
                "uly": "BTC-USD",
                "delta": "-1.1180902625",
                "gamma": "2.2361957091",
                "vega": "0.0000000001",
                "theta": "0.0000032334",
                "lever": "8.465747567",
                "markVol": "0.3675503331",
                "bidVol": "0",
                "askVol": "1.1669998535",
                "realVol": "",
                "deltaBS": "-0.9999672034",
                "gammaBS": "0.0000000002",
                "thetaBS": "28.2649858387",
                "vegaBS": "0.0000114332",
                "ts": "1728703155650",
                "fwdPx": "62604.6993093463",
                "volLv": "0.2044711229"
            }
        ]
    }
    

#### Push data parameters

**Parameter** | **Type** | **Description**  
---|---|---  
arg | Object | Successfully subscribed channel  
> channel | String | Channel name  
> instFamily | String | Instrument family  
data | Array of objects | Subscribed data  
> instType | String | Instrument type, `OPTION`  
> instId | String | Instrument ID  
> uly | String | Underlying  
> delta | String | Sensitivity of option price to `uly` price  
> gamma | String | The delta is sensitivity to `uly` price  
> vega | String | Sensitivity of option price to implied volatility  
> theta | String | Sensitivity of option priceo remaining maturity  
> deltaBS | String | Sensitivity of option price to `uly` price in BS mode  
> gammaBS | String | The delta is sensitivity to `uly` price in BS mode  
> vegaBS | String | Sensitivity of option price to implied volatility in BS mode  
> thetaBS | String | Sensitivity of option price to remaining maturity in BS mode  
> lever | String | Leverage  
> markVol | String | Mark volatility  
> bidVol | String | Bid volatility  
> askVol | String | Ask Volatility  
> realVol | String | Realized volatility (not currently used)  
> volLv | String | Implied volatility of at-the-money options  
> fwdPx | String | Forward price  
> ts | String | Price update time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
  
### Estimated delivery/exercise/settlement price channel

Retrieve the estimated delivery/exercise/settlement price of `FUTURES`, `OPTION` and `SWAP` contracts.

The estimated price, calculated based on index price during the one-hour period prior to delivery, excerise, or settlement, with updates pushed approximately every 200ms.

#### URL Path

/ws/v5/public

> Request Example
    
    
    {
      "id": "1512",
      "op": "subscribe",
      "args": [
        {
          "channel": "estimated-price",
          "instType": "FUTURES",
          "instFamily": "BTC-USD"
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
              "channel": "estimated-price",
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
`estimated-price`  
> instType | String | Yes | Instrument type  
`OPTION`  
`FUTURES`  
`SWAP`  
`EVENTS`  
> instFamily | String | Conditional | Instrument family  
Either `instFamily` or `instId` is required.  
> instId | String | Conditional | Instrument ID  
Either `instFamily` or `instId` is required.  
  
> Successful Response Example
    
    
    {
      "id": "1512",
      "event": "subscribe",
      "arg": {
        "channel": "estimated-price",
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
      "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{ \"channel\" : \"estimated-price\", \"instId\" : \"FUTURES\",\"uly\" :\"BTC-USD\"}]}",
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
`OPTION`  
`FUTURES`  
`SWAP`  
`EVENTS`  
> instFamily | String | Conditional | Instrument family  
> instId | String | Conditional | Instrument ID  
code | String | No | Error code  
msg | String | No | Error message  
connId | String | Yes | WebSocket connection ID  
  
> Push Data Example
    
    
    {
        "arg": {
            "channel": "estimated-price",
            "instType": "FUTURES",
            "instFamily": "XRP-USDT"
        },
        "data": [{
            "instId": "XRP-USDT-250307",
            "instType": "FUTURES",
            "settlePx": "2.4230631578947368",
            "settleType": "settlement",
            "ts": "1741244598708"
        }]
    }
    

#### Push data parameters

**Parameter** | **Type** | **Description**  
---|---|---  
arg | Object | Successfully subscribed channel  
> channel | String | Channel name  
> instType | String | Instrument type  
`FUTURES`  
`OPTION`  
`SWAP`  
`EVENTS`  
> instFamily | String | Instrument family  
> instId | String | Instrument ID  
data | Array of objects | Subscribed data  
> instType | String | Instrument type  
> instId | String | Instrument ID, e.g. `BTC-USD-170310`  
> settleType | String | Type  
`settlement`: Futures settlement  
`delivery`: Futures delivery  
`exercise`: Option exercise  
> settlePx | String | Estimated price  
> ts | String | Data update time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
  
### Mark price channel

Retrieve the mark price. Data will be pushed every 200 ms when the mark price changes, and will be pushed every 10 seconds when the mark price does not change.

#### URL Path

/ws/v5/public

> Request Example
    
    
    {
      "id": "1512",
      "op": "subscribe",
      "args": [
        {
          "channel": "mark-price",
          "instId": "LTC-USD-190628"
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
            "channel": "mark-price",
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
`mark-price`  
> instId | String | Yes | Instrument ID  
  
> Successful Response Example
    
    
    {
      "id": "1512",
      "event": "subscribe",
      "arg": {
        "channel": "mark-price",
        "instId": "LTC-USD-190628"
      },
      "connId": "a4d3ae55"
    }
    

> Failure Response Example
    
    
    {
      "id": "1512",
      "event": "error",
      "code": "60012",
      "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{ \"channel\" : \"mark-price\", \"instId\" : \"LTC-USD-190628\"}]}",
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
> instId | String | No | Instrument ID  
code | String | No | Error code  
msg | String | No | Error message  
connId | String | Yes | WebSocket connection ID  
  
> Push Data Example
    
    
    {
      "arg": {
        "channel": "mark-price",
        "instId": "LTC-USD-190628"
      },
      "data": [
        {
          "instType": "FUTURES",
          "instId": "LTC-USD-190628",
          "markPx": "0.1",
          "ts": "1597026383085"
        }
      ]
    }
    

#### Push data parameters

Parameter | Type | Description  
---|---|---  
arg | Object | Successfully subscribed channel  
> channel | String | Channel name  
> instId | String | Instrument ID  
data | Array of objects | Subscribed data  
> instType | String | Instrument type  
> instId | String | Instrument ID  
> markPx | String | Mark price  
> ts | String | Price update time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
In rare cases, two mark price messages with the same timestamp may be received within a short window. This can occur during scheduled system maintenance or deployments and is not persistent. When this happens, clients should use the later-received message as the authoritative value. The difference between the two values will be negligible and will not materially affect trading strategies. 

### Index tickers channel

Retrieve index tickers data. Push data every 100ms if there are any changes, otherwise push once a minute.

#### URL Path

/ws/v5/public

> Request Example
    
    
    {
      "id": "1512",
      "op": "subscribe",
      "args": [
        {
          "channel": "index-tickers",
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
              "channel": "index-tickers",
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
op | String | Yes | `subscribe` `unsubscribe`  
args | Array of objects | Yes | List of subscribed channels  
> channel | String | Yes | Channel name  
`index-tickers`  
> instId | String | Yes | Index with USD, USDT, BTC, USDC as the quote currency, e.g. `BTC-USDT`  
Same as `uly`.  
  
> Successful Response Example
    
    
    {
      "id": "1512",
      "event": "subscribe",
      "arg": {
        "channel": "index-tickers",
        "instId": "BTC-USDT"
      },
      "connId": "a4d3ae55"
    }
    

> Failure Response Example
    
    
    {
      "id": "1512",
      "event": "error",
      "code": "60012",
      "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{ \"channel\" : \"index-tickers\", \"instId\" : \"BTC-USDT\"}]}",
      "connId": "a4d3ae55"
    }
    

#### Response parameters

Parameter | Type | Required | Description  
---|---|---|---  
id | String | No | Unique identifier of the message  
event | String | Yes | `subscribe` `unsubscribe` `error`  
arg | Object | No | Subscribed channel  
> channel | String | Yes | Channel name  
`index-tickers`  
> instId | String | Yes | Index with USD, USDT, BTC, USDC as the quote currency, e.g. `BTC-USDT`  
code | String | No | Error code  
msg | String | No | Error message  
connId | String | Yes | WebSocket connection ID  
  
> Push Data Example
    
    
    {
      "arg": {
        "channel": "index-tickers",
        "instId": "BTC-USDT"
      },
      "data": [
        {
          "instId": "BTC-USDT",
          "idxPx": "0.1",
          "high24h": "0.5",
          "low24h": "0.1",
          "open24h": "0.1",
          "sodUtc0": "0.1",
          "sodUtc8": "0.1",
          "ts": "1597026383085"
        }
      ]
    }
    

#### Push data parameters

Parameter | Type | Description  
---|---|---  
arg | Object | Successfully subscribed channel  
> channel | String | Channel name  
> instId | String | Index with USD, USDT, or BTC as quote currency, e.g. `BTC-USDT`.  
data | Array of objects | Subscribed data  
> instId | String | Index  
> idxPx | String | Latest Index Price  
> open24h | String | Open price in the past 24 hours  
> high24h | String | Highest price in the past 24 hours  
> low24h | String | Lowest price in the past 24 hours  
> sodUtc0 | String | Open price in the UTC 0  
> sodUtc8 | String | Open price in the UTC 8  
> ts | String | Update time of the index ticker, Unix timestamp format in milliseconds, e.g. `1597026383085`  
  
### Mark price candlesticks channel

Retrieve the candlesticks data of the mark price. The push frequency is the fastest interval 1 second push the data.

#### URL Path

/ws/v5/business

> Request Example
    
    
    {
      "id": "1512",
      "op": "subscribe",
      "args": [
        {
          "channel": "mark-price-candle1D",
          "instId": "BTC-USD-190628"
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
              "channel": "mark-price-candle1D",
              "instId": "BTC-USD-190628"
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
`subscribe` `unsubscribe`  
args | Array of objects | Yes | List of subscribed channels  
> channel | String | Yes | Channel name   
`mark-price-candle3M`   
`mark-price-candle1M`   
`mark-price-candle1W`   
`mark-price-candle1D`   
`mark-price-candle2D`   
`mark-price-candle3D`   
`mark-price-candle5D`   
`mark-price-candle12H`   
`mark-price-candle6H`   
`mark-price-candle4H`   
`mark-price-candle2H`   
`mark-price-candle1H`   
`mark-price-candle30m`   
`mark-price-candle15m`   
`mark-price-candle5m`   
`mark-price-candle3m`   
`mark-price-candle1m`   
`mark-price-candle1Yutc`   
`mark-price-candle3Mutc`   
`mark-price-candle1Mutc`   
`mark-price-candle1Wutc`   
`mark-price-candle1Dutc`   
`mark-price-candle2Dutc`   
`mark-price-candle3Dutc`   
`mark-price-candle5Dutc`   
`mark-price-candle12Hutc`   
`mark-price-candle6Hutc`  
> instId | String | Yes | Instrument ID  
  
> Successful Response Example
    
    
    {
      "id": "1512",
      "event": "subscribe",
      "arg": {
        "channel": "mark-price-candle1D",
        "instId": "BTC-USD-190628"
      },
      "connId": "a4d3ae55"
    }
    

> Failure Response Example
    
    
    {
      "id": "1512",
      "event": "error",
      "code": "60012",
      "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{ \"channel\" : \"mark-price-candle1D\", \"instId\" : \"BTC-USD-190628\"}]}",
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
        "channel": "mark-price-candle1D",
        "instId": "BTC-USD-190628"
      },
      "data": [
        ["1597026383085", "3.721", "3.743", "3.677", "3.708","0"],
        ["1597026383085", "3.731", "3.799", "3.494", "3.72","1"]
      ]
    }
    

#### Push data parameters

Parameter | Type | Description  
---|---|---  
arg | Object | Successfully subscribed channel  
> channel | String | Channel name  
> instId | String | Instrument ID  
data | Array of Arrays | Subscribed data  
> ts | String | Opening time of the candlestick, Unix timestamp format in milliseconds, e.g. `1597026383085`  
> o | String | Open price  
> h | String | Highest price  
> l | String | Lowest price  
> c | String | Close price  
> confirm | String | The state of candlesticks.  
`0` represents that it is uncompleted, `1` represents that it is completed.  
  
### Index candlesticks channel

Retrieve the candlesticks data of the index. The push frequency is the fastest interval 1 second push the data. .

#### URL Path

/ws/v5/business

> Request Example
    
    
    {
      "id": "1512",
      "op": "subscribe",
      "args": [
        {
          "channel": "index-candle30m",
          "instId": "BTC-USD"
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
              "channel": "index-candle30m",
              "instId": "BTC-USD"
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
`index-candle3M`   
`index-candle1M`   
`index-candle1W`   
`index-candle1D`   
`index-candle2D`   
`index-candle3D`   
`index-candle5D`   
`index-candle12H`   
`index-candle6H`   
`index-candle4H`   
`index -candle2H`   
`index-candle1H`   
`index-candle30m`   
`index-candle15m`   
`index-candle5m`   
`index-candle3m`   
`index-candle1m`   
`index-candle3Mutc`   
`index-candle1Mutc`   
`index-candle1Wutc`   
`index-candle1Dutc`   
`index-candle2Dutc`   
`index-candle3Dutc`   
`index-candle5Dutc`   
`index-candle12Hutc`   
`index-candle6Hutc`  
> instId | String | Yes | Index, e.g. `BTC-USD`  
Same as `uly`.  
  
> Successful Response Example
    
    
    {
      "id": "1512",
      "event": "subscribe",
      "arg": {
        "channel": "index-candle30m",
        "instId": "BTC-USD"
      },
      "connId": "a4d3ae55"
    }
    

> Failure Response Example
    
    
    {
      "id": "1512",
      "event": "error",
      "code": "60012",
      "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{ \"channel\" : \"index-candle30m\", \"instId\" : \"BTC-USD\"}]}",
      "connId": "a4d3ae55"
    }
    

#### Response parameters

Parameter | Type | Required | Description  
---|---|---|---  
id | String | No | Unique identifier of the message  
event | String | Yes | `subscribe` `unsubscribe`  
arg | Object | No | Subscribed channel  
> channel | String | Yes | Channel name  
> instId | String | No | Index, e.g. `BTC-USD`  
code | String | No | Error code  
msg | String | No | Error message  
connId | String | Yes | WebSocket connection ID  
  
> Push Data Example
    
    
    {
      "arg": {
        "channel": "index-candle30m",
        "instId": "BTC-USD"
      },
      "data": [["1597026383085", "3811.31", "3811.31", "3811.31", "3811.31", "0"]]
    }
    

#### Push data parameters

Parameter | Type | Description  
---|---|---  
arg | Object | Successfully subscribed channel  
> channel | String | Channel name  
> instId | String | Index  
data | Array of Arrays | Subscribed data  
> ts | String | Opening time of the candlestick, Unix timestamp format in milliseconds, e.g. `1597026383085`  
> o | String | Open price  
> h | String | Highest price  
> l | String | Lowest price  
> c | String | Close price  
> confirm | String | The state of candlesticks.  
`0` represents that it is uncompleted, `1` represents that it is completed.  
The order of the returned values is: [ts,o,h,l,c,confirm] 

### Liquidation orders channel

Retrieve the recent liquidation orders. This data doesn’t represent the total number of liquidations on OKX.

#### URL Path

/ws/v5/public

> Request Example
    
    
    {
      "id": "1512",
      "op": "subscribe",
      "args": [
        {
          "channel": "liquidation-orders",
          "instType": "SWAP"
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
              "channel": "liquidation-orders",
              "instType": "SWAP"
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
`liquidation-orders`  
> instType | String | Yes | Instrument type  
`SWAP`  
`FUTURES`  
`MARGIN`  
`OPTION`  
  
> Response Example
    
    
    {
        "id": "1512",
        "arg": {
            "channel": "liquidation-orders",
            "instType": "SWAP"
        },
        "data": [
            {
                "details": [
                    {
                        "bkLoss": "0",
                        "bkPx": "0.007831",
                        "ccy": "",
                        "posSide": "short",
                        "side": "buy",
                        "sz": "13",
                        "ts": "1692266434010"
                    }
                ],
                "instFamily": "IOST-USDT",
                "instId": "IOST-USDT-SWAP",
                "instType": "SWAP",
                "uly": "IOST-USDT"
            }
        ]
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
id | String | Unique identifier of the message  
arg | Object | Successfully subscribed channel  
> channel | String | Channel name  
> instId | String | Instrument ID  
data | Array of objects | Subscribed data  
> instType | String | Instrument type  
> instId | String | Instrument ID, e.g. `BTC-USD-SWAP`  
> uly | String | Underlying  
Applicable to `FUTURES`/`SWAP`/`OPTION`  
> details | Array of objects | Liquidation details  
>> side | String | Order side  
`buy`  
`sell`  
Applicable to `FUTURES`/`SWAP`  
>> posSide | String | Position mode side  
`long`: Hedge mode long  
`short`: Hedge mode short  
`net`: Net mode  
>> bkPx | String | Liquidation mark price. The price of the transaction with the system's liquidation account, only applicable to `FUTURES`/`SWAP`  
>> sz | String | Quantity of liquidation, only applicable to `MARGIN`/`FUTURES`/`SWAP`.  
For `MARGIN`, the unit is base currency.   
For `FUTURES/SWAP`, the unit is contract.  
>> bkLoss | String | Bankruptcy loss  
>> ccy | String | Liquidation currency, only applicable to `MARGIN`  
>> ts | String | Liquidation time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
Liquidation data comes from different data sources, so the updated data is not necessarily in chronological order. 

### ADL warning channel

Auto-deleveraging warning channel.

Data is only pushed in the `warning` or `adl` state, once every second, displaying the security fund balance and related risk information. No data is pushed in the `normal` state.

For more ADL details, please refer to [Introduction to Auto-deleveraging](https://www.okx.com/help/iv-introduction-to-auto-deleveraging-adl)

#### URL Path

/ws/v5/public

> Request Example
    
    
    {
        "id": "1512",
        "op": "subscribe",
        "args": [{
            "channel": "adl-warning",
            "instType": "FUTURES",
            "instFamily": "BTC-USDT"
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
            "channel": "adl-warning",
            "instType": "FUTURES",
            "instFamily": "BTC-USDT"
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
`adl-warning`  
> instType | String | Yes | Instrument type  
`SWAP`  
`FUTURES`  
`OPTION`  
> instFamily | String | No | Instrument family  
  
> Successful Response Example
    
    
    {
       "id": "1512",
       "event":"subscribe",
       "arg":{
          "channel":"adl-warning",
          "instType":"FUTURES",
          "instFamily":"BTC-USDT"
       },
       "connId":"48d8960a"
    }
    
    

> Failure Response Example
    
    
    {
       "id": "1512",
       "event":"error",
       "msg":"Illegal request: { \"event\": \"subscribe\", \"arg\": { \"channel\": \"adl-warning\", \"instType\": \"FUTURES\", \"instFamily\": \"BTC-USDT\" } }",
       "code":"60012",
       "connId":"48d8960a"
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
`adl-warning`  
> instType | String | Yes | Instrument type  
> instFamily | String | No | Instrument family  
code | String | No | Error code  
msg | String | No | Error message  
connId | String | Yes | WebSocket connection ID  
  
> Push Data Example
    
    
    {
       "arg":{
          "channel":"adl-warning",
          "instType":"FUTURES",
          "instFamily":"BTC-USDT"
       },
       "data":[
          {
             "instType":"FUTURES",
             "instFamily":"BTC-USDT",
             "state":"warning",
             "bal":"280784384.9564228289548144",
             "ccy":"",
             "maxBal":"",
             "maxBalTs":"",
             "adlType":"",
             "adlBal":"",
             "adlRecBal":"",
             "ts":"1700210763001",
             "decRate":"",
             "adlRate":"",
             "adlRecRate":""
          }
       ]
    }
    
    

#### Push data parameters

Parameter | Type | Description  
---|---|---  
arg | Object | Subscribed channel  
> channel | String | Channel name  
`adl-warning`  
> instType | String | Instrument type  
> instFamily | String | Instrument family  
data | Array of objects | Subscribed data  
> instType | String | Instrument type  
> instFamily | String | Instrument family  
> state | String | state   
`warning`   
`adl`  
> bal | String | Real-time security fund balance  
> ccy | String | ~~The corresponding currency of security fund balance~~(Deprecated, returns `""`. To be removed in a future update)  
> maxBal | String | ~~Maximum security fund balance in the past eight hours  
  
Applicable when state is `warning` or `adl`~~(Deprecated, returns `""`. To be removed in a future update)  
> maxBalTs | String | ~~Timestamp when security fund balance reached maximum in the past eight hours, Unix timestamp format in milliseconds, e.g.`1597026383085`~~(Deprecated, returns `""`. To be removed in a future update)  
> adlType | String | ~~ADL related events  
`rate_adl_start`: ADL begins due to high security fund decline rate   
`bal_adl_start`: ADL begins due to security fund balance falling   
`pos_adl_start`：ADL begins due to the volume of liquidation orders falls to a certain level (only applicable to premarket symbols)   
`adl_end`: ADL ends~~(Deprecated, returns `""`. To be removed in a future update)  
> adlBal | String | ~~security fund balance that triggers ADL~~(Deprecated, returns `""`. To be removed in a future update)  
> adlRecBal | String | ~~security fund balance that turns off ADL~~(Deprecated, returns `""`. To be removed in a future update)  
> ts | String | Data push time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
> decRate | String | ~~Real-time security fund decline rate (compare bal and maxBal)  
  
Applicable when state is `warning` or `adl`~~(Deprecated)  
> adlRate | String | ~~security fund decline rate that triggers ADL~~(Deprecated)  
> adlRecRate | String | ~~security fund decline rate that turns off ADL~~(Deprecated)  
  
### Economic calendar channel

This endpoint is only supported in production environment. 

Retrieve the most up-to-date economic calendar data. This endpoint is only applicable to VIP 1 and above users in the trading fee tier.

#### URL Path

/ws/v5/business (required login)

> Request Example
    
    
    {
        "id": "1512",
        "op": "subscribe",
        "args": [
          {
              "channel": "economic-calendar"
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
              "channel": "economic-calendar"
          }
        ]
    
        await ws.subscribe(args, callback=callbackFunc)
        await asyncio.sleep(10)
    
        await ws.unsubscribe(args, callback=callbackFunc)
        await asyncio.sleep(10)
    
    
    asyncio.run(main())
    
    

#### Request parameters

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
`economic-calendar`  
  
> Successful Response Example
    
    
    {
        "id": "1512",
        "event": "subscribe",
        "arg": {
            "channel": "economic-calendar"
        },
        "connId": "a4d3ae55"
    }
    
    

> Failure Response Example
    
    
    {
      "id": "1512",
      "event": "error",
      "code": "60012",
      "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{ \"channel\" : \"economic-calendar\", \"instId\" : \"LTC-USD-190628\"}]}",
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
code | String | No | Error code  
msg | String | No | Error message  
connId | String | Yes | WebSocket connection ID  
  
> Push Data Example
    
    
    {
        "arg": {
            "channel": "economic-calendar"
        },
        "data": [
            {
                "calendarId": "319275",
                "date": "1597026383085",
                "region": "United States",
                "category": "Manufacturing PMI",
                "event": "S&P Global Manufacturing PMI Final",
                "refDate": "1597026383085",
                "actual": "49.2",
                "previous": "47.3",
                "forecast": "49.3",
                "importance": "2",
                "prevInitial": "",
                "ccy": "",
                "unit": "",
                "ts": "1698648096590"
            }
        ]
    }
    

#### Push data parameters

Parameter | Type | Description  
---|---|---  
arg | Object | Successfully subscribed channel  
> channel | String | Channel name  
`economic-calendar`  
data | Array of objects | Subscribed data  
> event | string | Event name  
> region | string | Country, region or entity  
> category | string | Category name  
> actual | string | The actual value of this event  
> previous | string | Latest actual value of the previous period   
The value will be revised if revision is applicable  
> forecast | string | Average forecast among a representative group of economists  
> prevInitial | string | The initial value of the previous period   
Only applicable when revision happens  
> date | string | Estimated release time of the value of actual field, millisecond format of Unix timestamp, e.g. `1597026383085`  
> refDate | string | Date for which the datapoint refers to  
> calendarId | string | Calendar ID  
> unit | string | Unit of the data  
> ccy | string | Currency of the data  
> importance | string | Level of importance  
`1`: low   
`2`: medium   
`3`: high  
> ts | string | The time of the latest update

---

# 公共数据

`公共数据`功能模块下的API接口不需要身份验证。

## REST API 

### 获取交易产品基础信息 

获取所有可交易产品的信息列表。

#### 限速：20次/2s

#### 限速规则：IP + Instrument Type

#### HTTP请求

`GET /api/v5/public/instruments`

> 请求示例
    
    
    GET /api/v5/public/instruments?instType=SPOT
    
    
    
    import okx.PublicData as PublicData
    
    flag = "0"  # 实盘:0 , 模拟盘：1
    
    publicDataAPI = PublicData.PublicAPI(flag=flag)
    
    # 获取交易产品基础信息
    result = publicDataAPI.get_instruments(
        instType="SPOT"
    )
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
instType | String | 是 | 产品类型  
`SPOT`：币币  
`MARGIN`：币币杠杆  
`SWAP`：永续合约  
`FUTURES`：交割合约  
`OPTION`：期权  
`EVENTS`：事件合约  
seriesId | String | 可选 | 系列 ID，如 `BTC-ABOVE-DAILY`。当 `instType` 为 `EVENTS` 时必填  
instFamily | String | 否 | 交易品种，仅适用于`交割`/`永续`/`期权`  
instId | String | 否 | 产品ID  
  
> 返回结果
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
          {
                "alias": "",
                "auctionEndTime": "",
                "baseCcy": "BTC",
                "category": "1",
                "ctMult": "",
                "ctType": "",
                "ctVal": "",
                "ctValCcy": "",
                "contTdSwTime": "1704876947000",
                "expTime": "",
                "futureSettlement": false,
                "groupId": "1",
                "instFamily": "",
                "instId": "BTC-USDT",
                "instType": "SPOT",
                "lever": "10",
                "listTime": "1606468572000",
                "lotSz": "0.00000001",
                "maxIcebergSz": "9999999999.0000000000000000",
                "maxLmtAmt": "1000000",
                "maxLmtSz": "9999999999",
                "maxMktAmt": "1000000",
                "maxMktSz": "",
                "maxStopSz": "",
                "maxTriggerSz": "9999999999.0000000000000000",
                "maxTwapSz": "9999999999.0000000000000000",
                "minSz": "0.00001",
                "optType": "",
                "openType": "call_auction",
                "preMktSwTime": "",
                "quoteCcy": "USDT",
                "tradeQuoteCcyList": [
                    "USDT"
                ],
                "settleCcy": "",
                "state": "live",
                "ruleType": "normal",
                "stk": "",
                "tickSz": "0.1",
                "uly": "",
                "instIdCode": 1000000000,
                "instCategory": "1",
                "upcChg": [
                    {
                        "param": "tickSz",
                        "newValue": "0.0001",
                        "effTime": "1704876947000"
                    }
                ]
            }
        ]
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
instType | String | 产品类型  
seriesId | String | 系列 ID，如 `BTC-ABOVE-DAILY`。仅适用于 `EVENTS`  
instId | String | 产品id， 如 `BTC-USDT`  
uly | String | 标的指数，如 `BTC-USD`，仅适用于`杠杆/交割/永续/期权`  
groupId | String | 交易产品手续费分组ID  
现货：  
`1`：USDT现货  
`2`：USDC及Crypto现货  
`3`：TRY现货  
`4`：EUR现货  
`5`：BRL现货  
`7`：AED现货  
`8`：AUD现货  
`9`：USD现货  
`10`：SGD现货  
`11`：零手续费现货  
`12`：现货分组一  
`13`：现货分组二  
`14`：现货分组三  
`15`: 现货特别分组  
  
交割合约：  
`1`：币本位交割合约  
`2`：USDT本位交割合约  
`3`：USDC本位交割合约  
`4`：盘前交易交割合约  
`5`：交割合约分组一  
`6`：交割合约分组二  
  
永续合约：  
`1`：币本位永续合约  
`2`：USDT本位永续合约  
`3`：USDC本位永续合约  
`4`：永续合约分组一  
`5`：永续合约分组二  
`6`：股票永续合约  
  
期权：  
`1`：币本位期权  
`2`：USDC本位期权  
  
**用户需要同时使用instType和groupId来确定一个交易产品的交易手续费分组；用户应该将此接口和[获取当前账户交易手续费费率](/docs-v5/zh/#trading-account-rest-api-get-fee-rates)一起使用，以获取特定交易产品的手续费率**   
  
**部分枚举值可能不适用于您，以实际返回为准**  
instFamily | String | 交易品种，如 `BTC-USD`，仅适用于`杠杆/交割/永续/期权`  
category | String | ~~币种类别~~ （已废弃）  
baseCcy | String | 交易货币币种，如 `BTC-USDT` 中的 `BTC` ，仅适用于`币币/币币杠杆`  
quoteCcy | String | 计价货币币种，如 `BTC-USDT` 中的`USDT` ，仅适用于`币币/币币杠杆`  
settleCcy | String | 盈亏结算和保证金币种，如 `BTC` 仅适用于`交割`/`永续`/`期权`  
ctVal | String | 每张合约的面值。计价货币取决于 `ctType`：线性合约以标的货币计（如BTC-USDT-SWAP，ctVal=0.01 BTC）；反向合约以USD计（如BTC-USD-SWAP，ctVal=100 USD）。名义价值：线性 = 张数 × ctVal × 标记价格（计价货币）；反向 = 张数 × ctVal（USD固定）。  
仅适用于 `FUTURES`/`SWAP`/`OPTION`  
ctMult | String | 合约乘数，仅适用于`交割`/`永续`/`期权`  
ctValCcy | String | 合约面值计价币种，仅适用于`交割`/`永续`/`期权`  
optType | String | 期权类型，`C`或`P` 仅适用于`期权`  
stk | String | 行权价格，仅适用于`期权`  
listTime | String | 上线时间   
Unix时间戳的毫秒数格式，如 `1597026383085`  
auctionEndTime | String | ~~集合竞价结束时间，Unix时间戳的毫秒数格式，如`1597026383085`   
仅适用于通过集合竞价方式上线的`币币`，其余情况返回""（已废弃，请使用contTdSwTime）~~  
contTdSwTime | String | 连续交易开始时间，从集合竞价、提前挂单切换到连续交易的时间，Unix时间戳格式，单位为毫秒。e.g. `1597026383085`。  
仅适用于通过集合竞价或提前挂单上线的`SPOT`/`MARGIN`，在其他情况下返回""。  
preMktSwTime | String | 盘前永续合约转为普通永续合约的时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
仅适用于盘前`SWAP`  
openType | String | 开盘类型  
`fix_price`: 定价开盘  
`pre_quote`: 提前挂单  
`call_auction`: 集合竞价   
只适用于`SPOT`/`MARGIN`，其他业务线返回""  
expTime | String | 产品下线时间  
适用于`币币/杠杆/交割/永续/期权`，对于 `交割/期权`，为交割/行权日期；亦可以为产品下线时间，有变动就会推送。  
lever | String | 交易所对该合约设定的最大杠杆上限。账户实际可用杠杆可能因VIP等级和仓位大小而更低。用户当前配置的杠杆请使用 GET /api/v5/account/leverage-info 查询。  
不适用于 `SPOT`、`OPTION`  
tickSz | String | 最小价格变动单位，如 `0.0001`。  
对于 `OPTION`/`EVENTS`，该值为 tick band 中的最小 tickSz。如需获取各价格区间的精确 tickSz，请使用"获取期权价格梯度"接口并传入对应的 `instType` 参数。  
lotSz | String | 合约面值最小变动单位（委托量步长），所有委托量（sz）必须为 `lotSz` 的整数倍，违反则返回错误51121。下单数量精度  
合约的数量单位是`张`，现货的数量单位是`交易货币`  
minSz | String | 最小委托量。委托量必须同时满足：sz ≥ `minSz` 且 sz 为 `lotSz` 的整数倍。最小下单数量  
合约的数量单位是`张`，现货的数量单位是`交易货币`  
ctType | String | 合约类型  
`linear`：正向合约，保证金、盈亏及结算均以计价货币计（如BTC-USDT-SWAP以USDT计）。  
`inverse`：反向合约，保证金、盈亏及结算均以标的货币计（如BTC-USD-SWAP以BTC计）。反向合约的USD盈亏为非线性：固定BTC盈亏的USD价值随BTC价格变化。  
仅适用于 `FUTURES`/`SWAP`  
alias | String | 合约日期别名（已废弃，将于 2026 年 4 月底下线，请使用 expTime 字段获取交割时间）  
`this_week`：本周  
`next_week`：次周  
`this_month`：本月  
`next_month`：次月  
`quarter`：季度  
`next_quarter`：次季度  
`third_quarter`：第三季度  
`this_five_years`：当期五年合约  
`next_five_years`：次期五年合约  
仅适用于`交割`  
state | String | 产品状态  
`live`：交易中   
`suspend`：暂停中  
`rebase`：合约在变基中，不可交易，仅适用于`SWAP`  
`post_only`：仅接受 post-only 订单；已有 post-only 订单可改单和撤单。其他订单类型（市价单、IOC、FOK、普通限价单）将被拒绝。仅适用于 `SWAP`  
`preopen`：预上线，交割和期权合约轮转生成到开始交易；部分交易产品上线前  
`test`：测试中（测试产品，不可交易）  
`settling`：结算中，仅适用于 `EVENTS`  
ruleType | String | 交易规则类型  
`normal`：普通交易  
`pre_market`：盘前交易  
`rebase_contract`：盘前变基合约  
`xperp`：永续合约风格的交割合约，仅适用于部分 `FUTURES` 合约  
maxLmtSz | String | 限价单的单笔最大委托数量  
合约的数量单位是`张`，现货的数量单位是`交易货币`  
maxMktSz | String | 市价单的单笔最大委托数量  
合约的数量单位是`张`，现货的数量单位是`USDT`  
maxLmtAmt | String | 限价单的单笔最大美元价值  
maxMktAmt | String | 市价单的单笔最大美元价值  
仅适用于`币币/币币杠杆`  
maxTwapSz | String | 时间加权单的单笔最大委托数量  
合约的数量单位是`张`，现货的数量单位是`交易货币`。  
单笔最小委托数量为 minSz*2  
maxIcebergSz | String | 冰山委托的单笔最大委托数量  
合约的数量单位是`张`，现货的数量单位是`交易货币`  
maxTriggerSz | String | 计划委托委托的单笔最大委托数量  
合约的数量单位是`张`，现货的数量单位是`交易货币`  
maxStopSz | String | 止盈止损市价委托的单笔最大委托数量  
合约的数量单位是`张`，现货的数量单位是`USDT`  
futureSettlement | Boolean | 交割合约是否支持每日结算  
适用于`全仓``交割`  
tradeQuoteCcyList | Array of strings | 可用于交易的计价币种列表，如 ["USD", "USDC”].  
instIdCode | Integer | 产品唯一标识代码。  
对于简单二进制编码，您必须使用 `instIdCode` 而不是 `instId`。  
对于同一`instId`，实盘和模拟盘的值可能会不一样。   
当值还未生成时，返回 `null`。  
instCategory | String | 标的资产类别（产品ID的第一部分）。例如：对于 `BTC-USDT-SWAP`，instCategory 表示 `BTC` 所属的资产类别。  
`1`: 加密货币   
`3`: 股票类资产   
`4`: 大宗商品   
`5`: 外汇   
`6`: 债券   
`""` 当值不可用时返回空字符串  
initPxLmtPct | String | 合约上线后前 10 分钟内的初始价格限制区间，小数百分比，例如 `0.05` 代表 5%。通过 GET /api/v5/public/price-limit 可获取对应价格限制。  
适用于 `SPOT`/`MARGIN`/`SWAP`/`FUTURES`；`OPTION` 和 `EVENTS` 返回 `""`。  
floatPxLmtPct | String | 常规交易期间的浮动价格限制区间，小数百分比，例如 `0.03` 代表 3%。通过 GET /api/v5/public/price-limit 可获取对应价格限制。  
适用于 `SPOT`/`MARGIN`/`SWAP`/`FUTURES`；`OPTION` 和 `EVENTS` 返回 `""`。  
maxPxLmtPct | String | 最大价格限制上限（下单价格相对指数价格偏离的硬性上限），小数百分比，例如 `0.15` 代表 15%。通过 GET /api/v5/public/price-limit 可获取对应价格限制。  
适用于 `SPOT`/`MARGIN`/`SWAP`/`FUTURES`；`OPTION` 和 `EVENTS` 返回 `""`。  
upcChg | Array of objects | 即将变更的参数列表。当没有即将变更的参数时，返回空数组 []  
> param | String | 即将变更的参数名称。  
`tickSz`  
`minSz`：若为交割/永续合约（`FUTURES`/`SWAP`），`lotSz` 会同步变更。  
`maxMktSz`  
> newValue | String | 即将变更的参数值。  
> effTime | String | 生效时间。Unix 时间戳格式，例如 `1597026383085`  
当合约预上线时，状态变更为预上线（即新生成一个合约，新合约会处于预上线状态）；  listTime以及contTdSwTime  
对于通过集合竞价/提前挂单方式上线的币币，listTime为集合竞价/提前挂单的开始时间，contTdSwTime为集合竞价/提前挂单的结束时间、连续交易的开始时间；对于其他情况及业务线，listTime即为连续交易开始时间，contTdSwTime将返回""  state  
对于`币币`、`杠杆`、`永续`和`交割`，状态state在时间到达listTime时由`preopen`转变为`live`。对于`期权`合约，由于内部处理原因，状态可能在`listTime`之后短暂延迟变为`live`。建议在下单前确认`state`为`live`。  
当产品下线的时候（如交割合约被交割的时候，期权合约被行权的时候），查询不到该产品  产品下线公告一经发出，接口及频道会更新下线时间(expTime)。  
产品上线公告一经发出，接口及频道会更新上线时间：  
1\. 对于币币/杠杆/永续， 该事件仅适用于产品类型(instType), 交易产品ID(instId), 上线时间(listTime), 产品状态(state)字段；  
2\. 对于交割，该事件仅适用于产品类型(instType), 交易品种(instFamily), 上线时间(listTime), 产品状态(state)字段；  
3\. 其他字段暂时为空，会比上线时间至少提前 5 分钟更新完整，然后 WebSocket 才会支持通过对应的交易产品ID/交易品种进行订阅。  

### 获取系列 

获取 OKX 预测市场的系列列表。

#### 限速：10次/2s

#### 限速规则：IP

#### 权限：公共

#### HTTP请求

`GET /api/v5/public/event-contract/series`

> 请求示例
    
    
    GET /api/v5/public/event-contract/series?seriesId=BTC-ABOVE-DAILY
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
seriesId | String | 否 | 系列 ID，如 `BTC-ABOVE-DAILY`。不传则返回所有系列。  
  
> 返回示例
    
    
    {
        "code": "0",
        "data": [
            {
                "seriesId": "BTC-ABOVE-DAILY",
                "freq": "daily",
                "title": "BTC price above 15k",
                "category": "Crypto",
                "settlement": {
                    "method": "price_above",
                    "closeEarly": false,
                    "srcName": "okx_index",
                    "underlying": "BTC-USDT"
                }
            }
        ],
        "msg": ""
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
seriesId | String | 系列 ID，如 `BTC-ABOVE-DAILY`  
freq | String | 系列频率  
`five_min`  
`fifteen_min`  
`hourly`  
`daily`  
`monthly`  
title | String | 系列标题  
category | String | 所属分类，如 `Crypto`  
settlement | Object | 结算信息  
> method | String | 结算方式。  
`price_up_down`：价格涨跌  
`price_above`：价格高于  
`hit`：触及（价格触达行权价格，立即结算）  
`between`：区间（结算价格在 [floorStrike, capStrike) 范围内）  
> closeEarly | Boolean | 是否可以在到期时间前提前结算。  
`true`  
`false`  
> srcName | String | 结算数据来源名称，如 `okx_index`、`cf_benchmark_index`  
> underlying | String | OKX 交易对格式的标的价格，如 `BTC-USDT`。仅适用于价格相关结算方式。  
  
### 获取事件 

获取 OKX 预测市场某系列下的事件列表，包含已到期事件。返回数据按 expTime 和 eventId 降序排列。

#### 限速：10次/2s

#### 限速规则：IP

#### 权限：公共

#### HTTP请求

`GET /api/v5/public/event-contract/events`

> 请求示例
    
    
    GET /api/v5/public/event-contract/events?seriesId=BTC-ABOVE-DAILY
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
seriesId | String | 是 | 系列 ID，如 `BTC-ABOVE-DAILY`  
eventId | String | 否 | 事件 ID，如 `BTC-ABOVE-DAILY-260224-1600`  
state | String | 否 | 事件状态过滤。  
`preopen`  
`live`  
`settling`  
`expired`  
limit | String | 否 | 返回结果数量，最大 100，默认 100  
before | String | 否 | 分页，返回早于请求 `expTime` 的更新记录，不包含该时间戳  
after | String | 否 | 分页，返回晚于请求 `expTime` 的更旧记录，不包含该时间戳  
  
> 返回示例
    
    
    {
        "code": "0",
        "data": [
            {
                "seriesId": "BTC-ABOVE-DAILY",
                "eventId": "BTC-ABOVE-DAILY-260224-1600",
                "expTime": "1769697132335",
                "state": "live"
            }
        ],
        "msg": ""
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
seriesId | String | 系列 ID，如 `BTC-ABOVE-DAILY`  
eventId | String | 事件 ID，如 `BTC-ABOVE-DAILY-260224-1600`  
fixTime | String | 执行价格确定时间。Unix时间戳的毫秒数格式，如 `1597026383085`。仅适用于 `price_up_down` 结算方式。  
expTime | String | 该事件的行权时间。Unix时间戳的毫秒数格式，如 `1597026383085`  
state | String | 事件状态。  
`preopen`  
`live`  
`settling`  
`expired`  
  
### 获取市场 

获取 OKX 预测市场某事件下的市场列表。返回数据按 expTime 和 floorStrike 降序排列。

#### 限速：10次/2s

#### 限速规则：IP

#### 权限：公共

#### HTTP请求

`GET /api/v5/public/event-contract/markets`

> 请求示例
    
    
    GET /api/v5/public/event-contract/markets?seriesId=BTC-ABOVE-DAILY
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
seriesId | String | 是 | 系列 ID，如 `BTC-ABOVE-DAILY`  
eventId | String | 否 | 事件 ID，如 `BTC-ABOVE-DAILY-260224-1600`  
instId | String | 否 | 产品 ID，如 `BTC-ABOVE-DAILY-260224-1600-65000`  
state | String | 否 | 市场状态过滤。  
`preopen`  
`live`  
`settling`  
`expired`  
limit | String | 否 | 返回结果数量，最大 100，默认 100  
before | String | 否 | 分页，返回早于请求 `expTime` 的更新记录，不包含该时间戳  
after | String | 否 | 分页，返回晚于请求 `expTime` 的更旧记录，不包含该时间戳  
  
> 返回示例
    
    
    {
        "code": "0",
        "data": [
            {
                "seriesId": "BTC-ABOVE-DAILY",
                "eventId": "BTC-ABOVE-DAILY-260224-1600",
                "instId": "BTC-ABOVE-DAILY-260224-1600-65000",
                "listTime": "1769697132335",
                "expTime": "1769697132335",
                "state": "live",
                "fixTime": "",
                "outcome": "0",
                "floorStrike": "120000",
                "capStrike": "",
                "settleValue": "",
                "disputed": false,
                "hitDir": ""
            }
        ],
        "msg": ""
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
seriesId | String | 系列 ID，如 `BTC-ABOVE-DAILY`  
eventId | String | 事件 ID，如 `BTC-ABOVE-DAILY-260224-1600`  
instId | String | 产品 ID，如 `BTC-ABOVE-DAILY-260224-1600-65000`  
listTime | String | 上线时间。Unix时间戳的毫秒数格式，如 `1597026383085`  
fixTime | String | 行权价格确定时间。Unix时间戳的毫秒数格式，如 `1597026383085`。仅适用于 `price_up_down` 结算方式。  
expTime | String | 该事件的行权时间。Unix时间戳的毫秒数格式，如 `1597026383085`。结算后更新。  
state | String | 市场状态。  
`preopen`  
`live`  
`settling`  
`expired`  
disputed | Boolean | 是否存在争议。  
`true`  
`false`  
outcome | String | 市场结果。  
`0`：未确定  
`1`：YES  
`2`：NO。  
`1`/`2` 仅在 state 为 `expired` 时适用  
floorStrike | String | 导致 YES 结果的最低到期价格  
capStrike | String | `between` 结算方式中导致 YES 结果的最大到期值。`"INF"` 表示无上限（最高区间）。  
非 `between` 方式返回 `""`。  
settleValue | String | 结算价格。  
仅在 state 为 `expired` 时返回  
hitDir | String | 触及方向。仅在结算方式为 `hit` 时适用。  
`up`：价格从下方触及  
`dn`：价格从上方触及  
`""`：不适用（非 `hit` 方式）  
  
### 获取预估交割/行权价格 

获取交割合约和期权预估交割/行权价。交割/行权预估价只有交割/行权前一小时才有返回值

#### 限速：10次/2s

#### 限速规则：IP + Instrument ID

#### HTTP请求

`GET /api/v5/public/estimated-price`

> 请求示例
    
    
    GET /api/v5/public/estimated-price?instId=BTC-USD-200214
    
    
    
    import okx.PublicData as PublicData
    
    flag = "0"  # 实盘:0 , 模拟盘：1
    
    publicDataAPI = PublicData.PublicAPI(flag=flag)
    
    # 获取预估交割/行权价格
    result = publicDataAPI.get_estimated_price(
        instId="BTC-USD-200214",
    )
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
instId | String | 是 | 产品ID，如 `BTC-USD-200214`  
仅适用于`交割`/`期权`/`事件合约`  
  
> 返回结果
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
        {
            "instType":"FUTURES",
            "instId":"BTC-USDT-201227",
            "settlePx":"200",
            "ts":"1597026383085"
        }
      ]
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
instType | String | 产品类型  
`FUTURES`：交割合约  
`OPTION`：期权  
instId | String | 产品ID， 如 `BTC-USD-200214`  
settlePx | String | 预估交割/行权价格  
ts | String | 数据返回时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
  
### 获取交割和行权记录 

获取3个月内的交割合约的交割记录和期权的行权记录

#### 限速：40次/2s

#### 限速规则：IP + (Instrument Type + instFamily)

#### HTTP请求

`GET /api/v5/public/delivery-exercise-history`

> 请求示例
    
    
    GET /api/v5/public/delivery-exercise-history?instType=OPTION&uly=BTC-USD
    
    
    
    import okx.PublicData as PublicData
    
    flag = "0"  # 实盘:0 , 模拟盘：1
    
    publicDataAPI = PublicData.PublicAPI(flag=flag)
    
    # 获取交割和行权记录
    result = publicDataAPI.get_delivery_exercise_history(
        instType="FUTURES",
        uly="BTC-USD"
    )
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
instType | String | 是 | 产品类型  
`FUTURES`：交割合约  
`OPTION`：期权  
instFamily | String | 是 | 交易品种  
after | String | 否 | 请求此时间戳之前（更旧的数据）的分页内容，传的值为对应接口的`ts`  
before | String | 否 | 请求此时间戳之后（更新的数据）的分页内容，传的值为对应接口的`ts`  
limit | String | 否 | 分页返回的结果集数量，最大为100，不填默认返回100条  
  
> 返回结果
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
            {
                "ts":"1597026383085",
                "details":[
                    {
                        "type":"delivery",
                        "insId":"BTC-USD-190927",
                        "px":"0.016"
                    }
                ]
            },
            {
                "ts":"1597026383085",
                "details":[
                    {
                        "insId":"BTC-USD-200529-6000-C",
                        "type":"exercised",
                        "px":"0.016"
                    },
                    {
                        "insId":"BTC-USD-200529-8000-C",
                        "type":"exercised",
                        "px":"0.016"
                    }
                ]
            }
        ]
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
ts | String | 交割/行权日期，Unix时间戳的毫秒数格式，如 `1597026383085`  
details | Array of objects | 详细数据  
> insId | String | 交割/行权的合约ID  
> px | String | 交割/行权的价格  
> type | String | 类型   
`delivery`：交割   
`exercised`：实值已行权   
`expired_otm`：虚值已过期  
  
### 获取交割预估结算价格 

获取交割合约预估结算价。只有结算前一小时才有返回值。

#### 限速：10次/2s

#### 限速规则：IP + Instrument ID

#### HTTP请求

`GET /api/v5/public/estimated-settlement-info`

> 请求示例
    
    
    GET /api/v5/public/estimated-settlement-info?instId=XRP-USDT-250307
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
instId | String | 是 | 产品ID，如 `XRP-USDT-250307`  
仅适用于`交割`  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "estSettlePx": "2.5666068562369959",
                "instId": "XRP-USDT-250307",
                "nextSettleTime": "1741248000000",
                "ts": "1741246429748"
            }
        ],
        "msg": ""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
instId | String | 产品ID， 如 `XRP-USDT-250307`  
nextSettleTime | String | 下一次结算时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
estSettlePx | String | 预估结算价格  
ts | String | 数据返回时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
  
### 获取交割结算记录 

获取3个月内的交割合约的结算记录

#### 限速：40次/2s

#### 限速规则：IP + (Instrument Family)

#### HTTP请求

`GET /api/v5/public/settlement-history`

> 请求示例
    
    
    GET /api/v5/public/settlement-history?instFamily=XRP-USDT
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
instFamily | String | 是 | 交易品种  
after | String | 否 | 请求此时间戳之前（不包含）的分页内容，传的值为对应接口的`ts`  
before | String | 否 | 请求此时间戳之后（不包含）的分页内容，传的值为对应接口的`ts`  
limit | String | 否 | 分页返回的结果集数量，最大为`100`，不填默认返回`100`条  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "details": [
                    {
                        "instId": "XRP-USDT-250307",
                        "settlePx": "2.5192078615298715"
                    }
                ],
                "ts": "1741161600000"
            },
            {
                "details": [
                    {
                        "instId": "XRP-USDT-250307",
                        "settlePx": "2.5551316341327384"
                    }
                ],
                "ts": "1741075200000"
            }
        ],
        "msg": ""
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
ts | String | 结算日期，Unix时间戳的毫秒数格式，如 `1597026383085`  
details | Array of objects | 详细数据  
> instId | String | 产品ID  
> settlePx | String | 结算价格  
  
### 获取合约当前资金费率 

获取合约当前资金费率

#### 限速：10次/2s

#### 限速规则：IP + Instrument ID

#### HTTP请求

`GET /api/v5/public/funding-rate`

> 请求示例
    
    
    GET /api/v5/public/funding-rate?instId=BTC-USD-SWAP
    
    
    
    import okx.PublicData as PublicData
    
    flag = "0"  # 实盘:0 , 模拟盘：1
    
    publicDataAPI = PublicData.PublicAPI(flag=flag)
    
    # 获取合约当前资金费率
    result = publicDataAPI.get_funding_rate(
        instId="BTC-USD-SWAP",
    )
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
instId | String | 是 | 产品ID，如 `BTC-USD-SWAP` 或 X-Perps 交割合约 instId，传入 `ANY` 时返回所有 X-Perps 交割合约及永续合约的资金费率信息  
适用于`永续`及 X-Perps `交割`  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "formulaType": "noRate",
                "fundingRate": "0.0000182221218054",
                "fundingTime": "1743609600000",
                "impactValue": "",
                "instId": "BTC-USDT-SWAP",
                "instType": "SWAP",
                "interestRate": "",
                "maxFundingRate": "0.00375",
                "method": "current_period",
                "minFundingRate": "-0.00375",
                "nextFundingRate": "",
                "nextFundingTime": "1743638400000",
                "premium": "0.0000910113652644",
                "settFundingRate": "0.0000145824401745",
                "settState": "settled",
                "ts": "1743588686291"
            }
        ],
        "msg": ""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
instType | String | 产品类型  
`SWAP`：永续合约  
`FUTURES`：X-Perps 交割合约  
instId | String | 产品ID，如`BTC-USD-SWAP` 或 `ANY`  
method | String | 资金费收取逻辑   
`current_period`：当期收 ~~  
`next_period`：跨期收~~（不再支持跨期收合约）  
formulaType | String | 公式类型  
`noRate`：旧资金费率计算公式  
`withRate`：新资金费率计算公式  
fundingRate | String | 下一结算周期的预测资金费率。正数表示多头向空头支付资金费；负数表示空头向多头支付资金费。此为预测值，最终结算费率可能有所不同，请参阅 `settFundingRate` 查看上次实际结算费率。注意：结算周期通常为8小时，但可能调整；实际周期请通过 `fundingTime` 与 `nextFundingTime` 之差确定。  
nextFundingRate | String | ~~下一期预测资金费率  
当收取逻辑为`current_period`时，nextFundingRate字段将返回""~~（不再支持跨期收合约）  
fundingTime | String | 资金费时间 ，Unix时间戳的毫秒数格式，如 `1597026383085`  
nextFundingTime | String | 下一期资金费时间 ，Unix时间戳的毫秒数格式，如 `1622851200000`  
minFundingRate | String | 资金费率下限  
maxFundingRate | String | 资金费率上限  
interestRate | String | 利率  
impactValue | String | 深度加权金额（计价币数量）  
settState | String | 资金费率结算状态   
`processing`：结算中   
`settled`：已结算  
settFundingRate | String | 若 settState = `processing`，该字段代表用于本轮结算的资金费率；若 settState = `settled`，该字段代表用于上轮结算的资金费率  
premium | String | 溢价指数  
公式：[max (0，深度加权买价 - 指数价格) – max (0，指数价格 – 深度加权卖价)] / 指数价格  
ts | String | 数据更新时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
针对一些资金费率波动较大的小币种，OKX也将实时关注行情变化，在必要时候，将资金费率收取频率从8小时收付，改成频率较高的6小时/4小时/2小时/1小时收付。因此，用户应关注`fundingTime`及`nextFundingTime`字段以确定合约的资金费收取频率。 

### 获取合约历史资金费率 

获取合约历史资金费率，最多返回近三个月数据

#### 限速：10次/2s

#### 限速规则：IP + Instrument ID

#### HTTP请求

`GET /api/v5/public/funding-rate-history`

> 请求示例
    
    
    GET /api/v5/public/funding-rate-history?instId=BTC-USD-SWAP
    
    
    
    import okx.PublicData as PublicData
    
    flag = "0"  # 实盘:0 , 模拟盘：1
    
    publicDataAPI = PublicData.PublicAPI(flag=flag)
    
    # 获取合约历史资金费率
    result = publicDataAPI.funding_rate_history(
        instId="BTC-USD-SWAP",
    )
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
instId | String | 是 | 产品ID，如 `BTC-USD-SWAP` 或 X-Perps 交割合约 instId  
适用于`永续`及 X-Perps `交割`  
before | String | 否 | 请求此时间戳之后（更新的数据）的分页内容，传的值为对应接口的`fundingTime`  
after | String | 否 | 请求此时间戳之前（更旧的数据）的分页内容，传的值为对应接口的`fundingTime`  
limit | String | 否 | 分页返回的结果集数量，最大为400，不填默认返回400条  
  
> 返回结果
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
            {
                "formulaType": "noRate",
                "fundingRate": "0.0000746604960499",
                "fundingTime": "1703059200000",
                "instId": "BTC-USD-SWAP",
                "instType": "SWAP",
                "method": "next_period",
                "realizedRate": "0.0000746572360545"
            },
            {
                "formulaType": "noRate",
                "fundingRate": "0.000227985782722",
                "fundingTime": "1703030400000",
                "instId": "BTC-USD-SWAP",
                "instType": "SWAP",
                "method": "next_period",
                "realizedRate": "0.0002279755647389"
            }
      ]
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
instType | String | 产品类型  
`SWAP`：永续合约  
`FUTURES`：X-Perps 交割合约  
instId | String | 产品ID，如 `BTC-USD-SWAP`  
formulaType | String | 公式类型  
`noRate`：旧资金费率计算公式  
`withRate`：新资金费率计算公式  
fundingRate | String | 预计资金费率  
realizedRate | String | 实际资金费率  
fundingTime | String | 资金费时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
method | String | 资金费收取逻辑   
`current_period`：当期收   
`next_period`：跨期收  
针对一些资金费率波动较大的小币种，OKX也将实时关注行情变化，在必要时候，将资金费率收取频率从8小时收付，改成频率较高的6小时/4小时/2小时/1小时收付。因此，用户应关注`fundingTime`及`nextFundingTime`字段以确定合约的资金费收取频率。 

### 获取持仓总量 

查询单个交易产品的市场的持仓总量

#### 限速：20次/2s

#### 限速规则：IP + Instrument ID

#### HTTP请求

`GET /api/v5/public/open-interest`

> 请求示例
    
    
    GET /api/v5/public/open-interest?instType=SWAP
    
    
    
    import okx.PublicData as PublicData
    
    flag = "0"  # 实盘:0 , 模拟盘：1
    
    publicDataAPI = PublicData.PublicAPI(flag=flag)
    
    # 获取持仓总量
    result = publicDataAPI.get_open_interest(
        instType="FUTURES",
    )
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
instType | String | 是 | 产品类型  
`SWAP`：永续合约  
`FUTURES`：交割合约  
`OPTION`：期权  
`EVENTS`：事件合约  
instFamily | String | 可选 | 交易品种  
适用于`交割`/`永续`/`期权`  
`期权`下必传  
instId | String | 否 | 产品ID，如 `BTC-USDT-SWAP`   
仅适用于`交割`/`永续`/`期权`/`事件合约`  
  
> 返回结果
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
        {
            "instType":"SWAP",
            "instId":"BTC-USDT-SWAP",
            "oi":"5000",
            "oiCcy":"555.55",
            "oiUsd": "50000",
            "ts":"1597026383085"
        }
      ]
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
instType | String | 产品类型  
instId | String | 产品ID  
oi | String | 持仓量（按`张`折算）  
oiCcy | String | 持仓量（按`币`折算）  
oiUsd | String | 持仓量（按`USD`折算）  
ts | String | 数据返回时间，Unix时间戳的毫秒数格式 ，如 `1597026383085`  
  
### 获取限价 

查询单个交易产品的最高买价和最低卖价

#### 限速：20次/2s

#### 限速规则：IP

#### HTTP请求

`GET /api/v5/public/price-limit`

> 请求示例
    
    
    GET /api/v5/public/price-limit?instId=BTC-USDT-SWAP
    
    
    
    import okx.PublicData as PublicData
    
    flag = "0"  # 实盘:0 , 模拟盘：1
    
    publicDataAPI = PublicData.PublicAPI(flag=flag)
    
    # 获取限价
    result = publicDataAPI.get_price_limit(
        instId="BTC-USD-SWAP",
    )
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
instId | String | 是 | 产品ID，如 `BTC-USDT-SWAP`  
  
> 返回结果
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
        {
            "instType":"SWAP",
            "instId":"BTC-USDT-SWAP",
            "buyLmt":"17057.9",
            "sellLmt":"16388.9",
            "ts":"1597026383085",
            "enabled": true
        }
      ]
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
instType | String | 产品类型  
`SPOT`：币币  
`MARGIN`：杠杆  
`SWAP`：永续合约  
`FUTURES`：交割合约  
`OPTION`：期权   
若产品ID支持杠杆交易，则返回`MARGIN`；否则，返回`SPOT`。  
instId | String | 产品ID ，如 `BTC-USDT-SWAP`  
buyLmt | String | 最高买价   
当enabled为false时，返回""  
sellLmt | String | 最低卖价   
当enabled为false时，返回""  
ts | String | 限价数据更新时间 ，Unix时间戳的毫秒数格式，如 `1597026383085`  
enabled | Boolean | 限价是否生效   
`true`：限价生效   
`false`：限价不生效  
  
### 获取期权定价 

查询期权详细信息

#### 限速：20次/2s

#### 限速规则：IP + instFamily

#### HTTP请求

`GET /api/v5/public/opt-summary`

> 请求示例
    
    
    GET /api/v5/public/opt-summary?uly=BTC-USD
    
    
    
    import okx.PublicData as PublicData
    
    flag = "0"  # 实盘:0 , 模拟盘：1
    
    publicDataAPI = PublicData.PublicAPI(flag=flag)
    
    # 获取期权定价
    result = publicDataAPI.get_opt_summary(
        uly="BTC-USD",
    )
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
instFamily | String | 是 | 交易品种，仅适用于期权  
expTime | String | 否 | 合约到期日，格式为"YYMMDD"，如 "200527"  
  
**注意** ：本接口返回的数据可能不包含 `/api/v5/public/instruments` 中所有的期权合约。以下两种情况可能导致数据缺失： 1\. 期权已上架但尚未开始交易（例如，补充期权默认在特定时间开始交易，在开始交易之前可能无法获取对应数据）。 2\. 因市场报价不足导致隐含波动率曲面拟合失败。此情况在模拟盘中较易发生；实盘中由于做市商会提供报价，通常可保证拟合成功。

> 返回结果
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
          {
                "askVol": "3.7207056835937498",
                "bidVol": "0",
                "delta": "0.8310206676289528",
                "deltaBS": "0.9857332101544538",
                "fwdPx": "39016.8143629068452065",
                "gamma": "-1.1965483553276135",
                "gammaBS": "0.000011933182397798109",
                "instId": "BTC-USD-220309-33000-C",
                "instType": "OPTION",
                "lever": "0",
                "markVol": "1.5551965233045728",
                "realVol": "0",
                "volLv": "0",
                "theta": "-0.0014131955002093717",
                "thetaBS": "-66.03526900575946",
                "ts": "1646733631242",
                "uly": "BTC-USD",
                "vega": "0.000018173851073258973",
                "vegaBS": "0.7089307622132419"
            },
            {
                "askVol": "1.7968814062499998",
                "bidVol": "0",
                "delta": "-0.014668822072611904",
                "deltaBS": "-0.01426678984554619",
                "fwdPx": "39016.8143629068452065",
                "gamma": "0.49483062407551576",
                "gammaBS": "0.000011933182397798109",
                "instId": "BTC-USD-220309-33000-P",
                "instType": "OPTION",
                "lever": "0",
                "markVol": "1.5551965233045728",
                "realVol": "0",
                "volLv": "0",
                "theta": "-0.0014131955002093717",
                "thetaBS": "-54.93377294845015",
                "ts": "1646733631242",
                "uly": "BTC-USD",
                "vega": "0.000018173851073258973",
                "vegaBS": "0.7089307622132419"
            }
      ]
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
instType | String | 产品类型  
`OPTION`：期权  
instId | String | 产品ID，如 `BTC-USD-200103-5500-C`  
uly | String | 标的指数  
delta | String | 期权价格对`uly`价格的敏感度  
gamma | String | delta对`uly`价格的敏感度  
vega | String | 期权价格对隐含波动率的敏感度  
theta | String | 期权价格对剩余期限的敏感度  
deltaBS | String | BS模式下期权价格对`uly`价格的敏感度  
gammaBS | String | BS模式下delta对`uly`价格的敏感度  
vegaBS | String | BS模式下期权价格对隐含波动率的敏感度  
thetaBS | String | BS模式下期权价格对剩余期限的敏感度  
lever | String | 杠杆倍数  
markVol | String | 标记波动率  
bidVol | String | bid波动率  
askVol | String | ask波动率  
realVol | String | 已实现波动率（目前该字段暂未启用）  
volLv | String | 平价期权的隐含波动率  
fwdPx | String | 远期价格  
ts | String | 数据更新时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
  
### 获取免息额度和币种折算率等级 

获取免息额度和币种折算率等级

#### 限速：2 次/2s

#### 限速规则：IP

#### HTTP 请求

`GET /api/v5/public/discount-rate-interest-free-quota`

> 请求示例
    
    
    GET /api/v5/public/discount-rate-interest-free-quota?ccy=BTC
    
    
    
    import okx.PublicData as PublicData
    
    flag = "0"  # 实盘:0 , 模拟盘：1
    
    publicDataAPI = PublicData.PublicAPI(flag=flag)
    
    # 获取免息额度和币种折算率等级
    result = publicDataAPI.discount_interest_free_quota()
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
ccy | String | 否 | 币种  
discountLv | String | 否 | ~~折算率等级（已废弃）~~~~~~  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "amt": "0",
                "ccy": "BTC",
                "collateralRestrict": false,
                "details": [
                    {
                        "discountRate": "0.98",
                        "liqPenaltyRate": "0.02",
                        "maxAmt": "20",
                        "minAmt": "0",
                        "tier": "1",
                        "disCcyEq": "1000"
                    },
                    {
                        "discountRate": "0.9775",
                        "liqPenaltyRate": "0.0225",
                        "maxAmt": "25",
                        "minAmt": "20",
                        "tier": "2",
                        "disCcyEq": "2000"
                    }
                ],
                "discountLv": "1",
                "minDiscountRate": "0"
            }
        ],
        "msg": ""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
ccy | String | 币种  
colRes | String | 平台维度质押限制状态  
`0`：限制未触发  
`1`：限制未触发，但该币种接近平台质押上限  
`2`：限制已触发。该币种不可用作新订单的保证金，这可能会导致下单失败。但它仍会被计入账户有效保证金，保证金率不会收到影响。  
更多详情，请参阅[平台总质押借币上限说明](https://www.okx.com/zh-hans/help/introduction-to-the-platforms-collateralized-borrowing-limit-mechanism)。  
collateralRestrict | Boolean | ~~平台维度的质押借币限制  
`true`  
`false`~~（已弃用，请使用colRes）  
amt | String | 免息金额  
discountLv | String | ~~折算率等级~~（已废弃）~~~~  
minDiscountRate | String | 最小折算率，针对数量超过最后一档的最大值时  
details | Array of objects | 新的币种折算率详情  
> discountRate | String | 折算率  
> maxAmt | String | 梯度区间上限，单位为币种，如 BTC，"" 表示正无穷  
> minAmt | String | 梯度区间下限，单位为币种，如 BTC，最小值是0  
> tier | String | 档位  
> liqPenaltyRate | String | 强平罚金费率  
> disCcyEq | String | 折扣后的币种权益（取当前梯度区间上限），便于快速计算  
  
### 获取系统时间 

获取系统时间

#### 限速：10次/2s

#### 限速规则：IP

#### HTTP请求

`GET /api/v5/public/time`

> 请求示例
    
    
    GET /api/v5/public/time
    
    
    
    import okx.PublicData as PublicData
    
    flag = "0"  # 实盘:0 , 模拟盘：1
    
    publicDataAPI = PublicData.PublicAPI(flag=flag)
    
    # 获取系统时间
    result = publicDataAPI.get_system_time()
    print(result)
    

> 返回结果
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
        {
            "ts":"1597026383085"
        }
      ]
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
ts | String | 系统时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
  
### 获取标记价格 

为了防止个别用户恶意操控市场导致合约价格波动剧烈，我们根据现货指数和合理基差设定标记价格。

#### 限速：10次/2s

#### 限速规则：IP + Instrument ID

#### HTTP请求

`GET /api/v5/public/mark-price`

> 请求示例
    
    
    GET /api/v5/public/mark-price?instType=SWAP
    
    
    
    import okx.PublicData as PublicData
    
    flag = "0"  # 实盘:0 , 模拟盘：1
    
    publicDataAPI = PublicData.PublicAPI(flag=flag)
    
    # 获取标记价格
    result = publicDataAPI.get_mark_price(
        instType="SWAP",
    )
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
instType | String | 是 | 产品类型  
`MARGIN`：币币杠杆  
`SWAP`：永续合约  
`FUTURES`：交割合约  
`OPTION`：期权  
`EVENTS`：事件合约  
instFamily | String | 否 | 交易品种  
适用于`交割`/`永续`/`期权`  
instId | String | 否 | 产品ID，如 `BTC-USD-SWAP`  
  
> 返回结果
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
        {
            "instType":"SWAP",
            "instId":"BTC-USDT-SWAP",
            "markPx":"200",
            "ts":"1597026383085"
        }
      ]
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
instType | String | 产品类型  
`MARGIN`：币币杠杆  
`SWAP`：永续合约  
`FUTURES`：交割合约  
`OPTION`：期权  
`EVENTS`：事件合约  
instId | String | 产品ID，如 `BTC-USD-200214`  
markPx | String | 标记价格  
ts | String | 接口数据返回时间，Unix时间戳的毫秒数格式，如`1597026383085`  
  
### 获取衍生品仓位档位 

全部仓位档位对应信息，当前最高可开杠杆倍数由您的借币持仓和维持保证金率决定。

#### 限速：10次/2s

#### 限速规则：IP

#### HTTP请求

`GET /api/v5/public/position-tiers`

> 请求示例
    
    
    GET /api/v5/public/position-tiers?tdMode=cross&instType=SWAP&instFamily=BTC-USDT
    
    
    
    import okx.PublicData as PublicData
    
    flag = "0"  # 实盘:0 , 模拟盘：1
    
    publicDataAPI = PublicData.PublicAPI(flag=flag)
    
    # 获取衍生品仓位档位
    result = publicDataAPI.get_position_tiers(
        instType="SWAP",
        tdMode="cross",
        uly="BTC-USD"
    )
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
instType | String | 是 | 产品类型  
`MARGIN`：币币杠杆  
`SWAP`：永续合约  
`FUTURES`：交割合约  
`OPTION`：期权  
tdMode | String | 是 | 保证金模式  
`isolated`：逐仓 ；`cross`：全仓  
instFamily | String | 可选 | 交易品种，支持多instFamily，半角逗号分隔，最大不超过5个  
当产品类型是`永续`/`交割`/`期权` 之一时，`instFamily` 必填  
instId | String | 可选 | 产品ID，支持多instId，半角逗号分隔，最大不超过5个  
仅适用`币币杠杆`，`instId`和`ccy`必须传一个，若传两个，以`instId`为主  
ccy | String | 可选 | 保证金币种  
仅适用杠杆全仓，该值生效时，返回的是`跨币种保证金模式`和`组合保证金模式`下的借币量  
tier | String | 否 | 查指定档位  
  
> 返回结果
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
        {
                "baseMaxLoan": "50",
                "imr": "0.1",
                "instId": "BTC-USDT",
                "instFamily": "",
                "maxLever": "10",
                "maxSz": "50",
                "minSz": "0",
                "mmr": "0.03",
                "optMgnFactor": "0",
                "quoteMaxLoan": "500000",
                "tier": "1",
                "uly": ""
            }
      ]
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
uly | String | 标的指数  
适用于`交割`/`永续`/`期权`  
instFamily | String | 交易品种  
适用于`交割`/`永续`/`期权`  
instId | String | 币对  
tier | String | 仓位档位  
minSz | String | 该档位最少借币量或者持仓数量 `杠杆`/`期权`/`永续`/`交割` 最小持仓量 默认0   
当 `ccy` 参数生效时，返回 `ccy` 的最小借币量  
maxSz | String | 该档位最多借币量或者持仓数量 `杠杆`/`期权`/`永续`/`交割`   
当 `ccy` 参数生效时，返回 `ccy` 的最大借币量  
mmr | String | 仓位维持保证金率  
imr | String | 最低初始维持保证金率  
maxLever | String | 最高可用杠杆倍数  
optMgnFactor | String | 期权保证金系数 （仅适用于期权）  
quoteMaxLoan | String | 计价货币 最大借币量（仅适用于杠杆，且`instId`参数生效时），如 BTC-USDT 里的 USDT最大借币量  
baseMaxLoan | String | 交易货币 最大借币量（仅适用于杠杆，且`instId`参数生效时），如 BTC-USDT 里的 BTC最大借币量  
  
### 获取市场借币杠杆利率和借币限额 

#### 限速：2次/2s

#### 限速规则：IP

#### HTTP请求

`GET /api/v5/public/interest-rate-loan-quota`

> 请求示例
    
    
    GET /api/v5/public/interest-rate-loan-quota
    
    
    
    import okx.PublicData as PublicData
    
    flag = "0"  # 实盘:0 , 模拟盘：1
    
    publicDataAPI = PublicData.PublicAPI(flag=flag)
    
    # 获取市场借币杠杆利率和借币限额
    result = publicDataAPI.get_interest_rate_loan_quota()
    print(result)
    

> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "configCcyList": [
                    {
                        "ccy": "USDT",
                        "rate": "0.00043728",
                    }
                ],
                "basic": [
                    {
                        "ccy": "USDT",
                        "quota": "500000",
                        "rate": "0.00043728"
                    },
                    {
                        "ccy": "BTC",
                        "quota": "10",
                        "rate": "0.00019992"
                    }
                ],
                "vip": [
                    {
                        "irDiscount": "",
                        "loanQuotaCoef": "6",
                        "level": "VIP1"
                    },
                    {
                        "irDiscount": "",
                        "loanQuotaCoef": "7",
                        "level": "VIP2"
                    }
                ],
                "config": [
                    {
                        "ccy": "USDT",
                        "stgyType": "0",    // normal
                        "quota": "xxxxxx",
                        "level": "VIP 8"
                    },
                    ......
                    {
                        "ccy": "USDT",
                        "stgyType": "1",    // delta neutral
                        "quota": "xxxxx",
                        "level": "VIP 1"
                    },
                    ......
                ],
                "regular": [
                    {
                        "irDiscount": "",
                        "loanQuotaCoef": "1",
                        "level": "Lv1"
                    }
                ]
            }
        ],
        "msg": ""
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
basic | Array of objects | 基础利率和借币限额  
> ccy | String | 币种  
> rate | String | 日借币利率  
> quota | String | 基础借币限额  
vip | Array of objects | 专业用户  
> level | String | 账户交易手续费等级，如 `VIP1`  
> loanQuotaCoef | String | 借币限额系数，借币限额 = 基础借币限额 * 该系数  
> irDiscount | String | ~~利率的折扣率~~(已废弃)  
regular | Array of objects | 普通用户  
> level | String | 账户交易手续费等级，如 `Lv1`  
> loanQuotaCoef | String | 借币限额系数，借币限额 = 基础借币限额 * 该系数  
> irDiscount | String | ~~利率的折扣率~~(已废弃)  
configCcyList | Array of strings | 由自定义绝对值方式配置借币限额的币种  
当币种在configCcyList中时，用户应该参考config以获取相应限额，而非使用basic/vip/regular  
> ccy | String | 币种  
> rate | String | 基础杠杆日利率  
config | Array of objects | 由自定义绝对值方式配置借币限额的币种详情  
> ccy | String | 币种  
> stgyType | String | 策略类型  
`0`：普通策略模式  
`1`：delta 中性策略模式  
如果某个币种仅返回0，则表示该借贷额度由普通策略模式的账户和 delta 中性策略模式的账户共享；如果某个币种同时返回0/1，则表示 delta 中性策略模式的账户拥有单独的借贷额度。  
> quota | String | 借币限额  
> level | String | 账户交易手续费等级，如 `VIP1`  
  
### 获取衍生品标的指数 

#### 限速：20次/2s

#### 限速规则：IP

#### HTTP请求

`GET /api/v5/public/underlying`

> 请求示例
    
    
    GET /api/v5/public/underlying?instType=FUTURES
    
    
    
    import okx.PublicData as PublicData
    
    flag = "0"  # 实盘:0 , 模拟盘：1
    
    publicDataAPI = PublicData.PublicAPI(flag=flag)
    
    # 获取衍生品标的指数
    result = publicDataAPI.get_underlying(
        instType="FUTURES"
    )
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
instType | String | 是 | 产品类型  
`SWAP`：永续合约  
`FUTURES`：交割合约  
`OPTION`：期权  
  
> 返回结果
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
            [
                "LTC-USDT",
                "BTC-USDT",
                "ETC-USDT"
            ]
        ]
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
uly | Array of strings | 标的指数 如：BTC-USDT  
  
### 获取风险保证金余额 

通过该接口获取系统风险保证金余额信息

#### 限速：10次/2s

#### 限速规则：IP

#### HTTP请求

`GET /api/v5/public/insurance-fund`

> 请求示例
    
    
    GET /api/v5/public/insurance-fund?instType=SWAP&uly=BTC-USD
    
    
    
    import okx.PublicData as PublicData
    
    flag = "0"  # 实盘:0 , 模拟盘：1
    
    publicDataAPI = PublicData.PublicAPI(flag=flag)
    
    
    # 获取风险保证金余额
    result = publicDataAPI.get_insurance_fund(
        instType="SWAP",
        uly="BTC-USD"
    )
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
instType | String | 是 | 产品类型  
`MARGIN`：币币杠杆  
`SWAP`：永续合约  
`FUTURES`：交割合约  
`OPTION`：期权  
type | String | 否 | 风险保证金类型  
`liquidation_balance_deposit`：强平注入   
`bankruptcy_loss`：穿仓亏损   
~~`platform_revenue`：平台收入注入~~（已弃用，返回空值。将在后续更新中删除）   
~~`adl`：自动减仓历史数据~~（已弃用，返回空值。将在后续更新中删除）   
默认返回全部类型  
instFamily | String | 可选 | 交易品种  
`交割`/`永续`/`期权`情况下，`instFamily`必传  
ccy | String | 可选 | 币种， 仅适用`币币杠杆`，且必填写  
before | String | 否 | 请求此时间戳之后（更新的数据）的分页内容，传的值为对应接口的`ts`  
after | String | 否 | 请求此时间戳之前（更旧的数据）的分页内容，传的值为对应接口的`ts`  
limit | String | 否 | 分页返回的结果集数量，最大为100，不填默认返回100条  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "details": [
                    {
                        "adlType": "",
                        "amt": "1343.1308",
                        "balance": "1369179138.7489",
                        "ccy": "ETH",
                        "maxBal": "",
                        "maxBalTs": "",
                        "ts": "1704883083000",
                        "type": "liquidation_balance_deposit"
                    }
                ],
                "instFamily": "ETH-USD",
                "instType": "OPTION",
                "total": "1369179138.7489"
            }
        ],
        "msg": ""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
total | String | 平台风险保证金总计，单位为USD  
instFamily | String | 交易品种  
适用于`交割`/`永续`/`期权`  
instType | String | 产品类型  
details | Array of objects | 风险保证金详情  
> balance | String | 风险保证金总量  
> amt | String | 风险保证金更新数量   
在type为`liquidation_balance_deposit`或`bankruptcy_loss`时适用  
> ccy | String | 风险保证金总量对应的币种  
> type | String | 风险保证金类型  
`liquidation_balance_deposit`：强平注入  
`bankruptcy_loss`：穿仓亏损  
~~`platform_revenue`：平台收入注入~~（已弃用，返回空值）  
~~`adl`：自动减仓历史数据~~（已弃用，返回空值）  
> maxBal | String | ~~过去八小时内的风险保证金余额最大值  
仅在type为`adl`时适用~~（已弃用，返回空值）  
> maxBalTs | String | ~~过去八小时内风险保证金余额最大值对应的时间戳，Unix时间戳的毫秒数格式，如`1597026383085`   
仅在type为`adl`时适用~~（已弃用，返回空值）  
> decRate | String | ~~风险保证金实时下降率（balance与maxBal相比较）  
仅在type为`adl`时适用~~（已弃用）  
> adlType | String | ~~关于自动减仓的事件  
`rate_adl_start`：由于风险保证金下降率过高造成的自动减仓开始   
`bal_adl_start`：由于风险保证金余额下降过高造成的自动减仓开始   
`pos_adl_start`：由于强平单的规模积累到一定程度的自动减仓开始（仅适用于盘前交易市场）  
`adl_end`：自动减仓结束   
仅在type为`adl`时适用~~（已弃用，返回空值）  
> ts | String | 风险保证金更新时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
`regular_update` 类型已被删除。`adl` 和 `platform_revenue` 类型已弃用，当前返回空值；将在后续更新中删除。`amt` 字段用于展示 type 为 `liquidation_balance_deposit` 或 `bankruptcy_loss` 时的风险保证金余额差值，数据一天产生一次，每天下午4点左右（UTC 8）更新。 

### 张币转换 

由币转换为张，或者张转换为币。

#### 限速：10次/2s

#### 限速规则：IP

#### HTTP请求

`GET /api/v5/public/convert-contract-coin`

> 请求示例
    
    
    GET /api/v5/public/convert-contract-coin?instId=BTC-USD-SWAP&px=35000&sz=0.888
    
    
    
    import okx.PublicData as PublicData
    
    flag = "0"  # 实盘:0 , 模拟盘：1
    
    publicDataAPI = PublicData.PublicAPI(flag=flag)
    
    
    # 张币转换
    result = publicDataAPI.get_convert_contract_coin(
        instId="BTC-USD-SWAP",
        px="35000",
        sz="0.888"
    )
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
type | String | 否 | 转换类型  
`1`：币转张   
`2`：张转币  
默认为`1`  
instId | String | 是 | 产品ID，仅适用于`交割`/`永续`/`期权`  
sz | String | 是 | 数量，币转张时，为币的数量，张转币时，为张的数量。  
px | String | 可选 | 委托价格  
币本位合约的张币转换时必填  
U本位合约，usdt 与张的转换时，必填；coin 与张的转换时，可不填  
期权的张币转换时，可不填。  
unit | String | 否 | 币的单位  
`coin`：币  
`usds`：usdt/usdc  
默认为 `coin`，仅适用于`交割`/`永续`的U本位合约  
opType | String | 否 | 将要下单的类型  
`open`：开仓时将sz舍位  
`close`：平仓时将sz四舍五入  
默认值为`close`  
适用于`交割`/`永续`  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "instId": "BTC-USD-SWAP",
                "px": "35000",
                "sz": "311",
                "type": "1",
                "unit": "coin"
            }
        ],
        "msg": ""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
type | String | 转换类型   
`1`：币转张   
`2`：张转币  
instId | String | 产品ID  
px | String | 委托价格  
sz | String | 数量  
张转币时，为币的数量；币转张时，为张的数量。  
unit | String | 币的单位  
`coin`：币  
`usds`：usdt/usdc  
  
### 获取期权价格梯度

获取产品价格梯度信息

#### 限速：5次/2s

#### 限速规则：IP

#### HTTP请求

`GET /api/v5/public/instrument-tick-bands`

> 请求示例
    
    
    GET /api/v5/public/instrument-tick-bands?instType=OPTION
    
    
    
    GET /api/v5/public/instrument-tick-bands?instType=EVENTS
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
instType | String | 是 | 产品类型  
`OPTION`：期权  
`EVENTS`：事件合约  
instFamily | String | 否 | 交易品种，仅适用于 `OPTION`  
  
> 返回结果
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "instType": "OPTION",
                "instFamily": "BTC-USD",
                "tickBand": [
                    {
                        "minPx": "0",
                        "maxPx": "100",
                        "tickSz": "0.1"
                    },
                    {
                        "minPx": "100",
                        "maxPx": "10000",
                        "tickSz": "1"
                    }
                ]
            },
            {
                "instType": "OPTION",
                "instFamily": "ETH-USD",
                "tickBand": [
                    {
                        "minPx": "0",
                        "maxPx": "100",
                        "tickSz": "0.1"
                    },
                    {
                        "minPx": "100",
                        "maxPx": "10000",
                        "tickSz": "1"
                    }
                ]
            }
        ]
    }
    

> 返回结果：EVENTS
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "instType": "EVENTS",
                "instFamily": "",
                "tickBand": [
                    {
                        "minPx": "0.001",
                        "maxPx": "0.04",
                        "tickSz": "0.001"
                    },
                    {
                        "minPx": "0.04",
                        "maxPx": "0.96",
                        "tickSz": "0.01"
                    },
                    {
                        "minPx": "0.96",
                        "maxPx": "0.999",
                        "tickSz": "0.001"
                    }
                ]
            }
        ]
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
instType | String | 产品类型  
instFamily | String | 交易品种。仅适用于 `OPTION`  
tickBand | Array of objects | 价格梯度。对于 `EVENTS`，返回适用于所有事件合约的统一价格梯度配置。  
> minPx | String | 下单最低价格  
> maxPx | String | 下单最高价格  
> tickSz | String | 下单价格精度，如 `0.0001`  
  
### 获取溢价历史数据 

获取最近6个月的溢价历史数据

#### 限速：20次/2s

#### 限速规则：IP

#### HTTP请求

`GET /api/v5/public/premium-history`

> 请求示例
    
    
    GET /api/v5/public/premium-history?instId=BTC-USDT-SWAP
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
instId | String | 是 | 产品ID，如 `BTC-USDT-SWAP`  
适用于`永续`  
after | String | 否 | 请求此时间戳（不包含）之前的分页内容，传的值为对应接口的`ts`  
before | String | 否 | 请求此时间戳（不包含）之后的分页内容，传的值为对应接口的`ts`  
limit | String | 否 | 分页返回的结果集数量，最大为`100`。默认返回`100`条。  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "instId": "BTC-USDT-SWAP",
                "premium": "0.0000578896878167",
                "ts": "1713925924000"
            }
        ],
        "msg": ""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
instId | String | 产品ID ，如 `BTC-USDT-SWAP`  
premium | String | 溢价指数  
公式：[max (0，深度加权买价 - 指数价格) – max (0，指数价格 – 深度加权卖价)] / 指数价格  
ts | String | 数据产生的时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
  
### 获取指数行情 

获取指数行情数据

#### 限速：20次/2s

#### 限速规则：IP

#### HTTP请求

`GET /api/v5/market/index-tickers`

> 请求示例
    
    
    GET /api/v5/market/index-tickers?instId=BTC-USDT
    
    
    
    import okx.MarketData as MarketData
    
    flag = "0"  # 实盘:0 , 模拟盘：1
    
    marketDataAPI =  MarketData.MarketAPI(flag=flag)
    
    # 获取指数行情
    result = marketDataAPI.get_index_tickers(
        instId="BTC-USD"
    )
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
quoteCcy | String | 可选 | 指数计价单位， 目前只有 `USD/USDT/BTC/USDC`为计价单位的指数，`quoteCcy`和`instId`必须填写一个  
instId | String | 可选 | 指数，如 `BTC-USD`  
与 `uly` 含义相同。  
  
> 返回结果
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "instId": "BTC-USDT",
                "idxPx": "43350",
                "high24h": "43649.7",
                "sodUtc0": "43444.1",
                "open24h": "43640.8",
                "low24h": "43261.9",
                "sodUtc8": "43328.7",
                "ts": "1649419644492"
            }
        ]
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
instId | String | 指数  
idxPx | String | 最新指数价格  
high24h | String | 24小时指数最高价格  
low24h | String | 24小时指数最低价格  
open24h | String | 24小时指数开盘价格  
sodUtc0 | String | UTC 0 时开盘价  
sodUtc8 | String | UTC+8 时开盘价  
ts | String | 指数价格更新时间，Unix时间戳的毫秒数格式，如`1597026383085`  
  
### 获取指数K线数据 

指数K线数据每个粒度最多可获取最近1,440条。

#### 限速：20次/2s

#### 限速规则：IP

#### HTTP请求

`GET /api/v5/market/index-candles`

> 请求示例
    
    
    GET /api/v5/market/index-candles?instId=BTC-USD
    
    
    
    import okx.MarketData as MarketData
    
    flag = "0"  # 实盘:0 , 模拟盘：1
    
    marketDataAPI =  MarketData.MarketAPI(flag=flag)
    
    # 获取指数K线数据
    result = marketDataAPI.get_index_candlesticks(
        instId="BTC-USD"
    )
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
instId | String | 是 | 现货指数，如 `BTC-USD`  
与 `uly` 含义相同。  
after | String | 否 | 请求此时间戳之前（更旧的数据）的分页内容，传的值为对应接口的`ts`  
before | String | 否 | 请求此时间戳之后（更新的数据）的分页内容，传的值为对应接口的`ts`, 单独使用时，会返回最新的数据。  
bar | String | 否 | 时间粒度，默认值`1m`  
如 [`1m`/`3m`/`5m`/`15m`/`30m`/`1H`/`2H`/`4H`]   
UTC+8开盘价k线：[`6H`/`12H`/`1D`/`1W`/`1M`/`3M`]  
UTC+0开盘价k线：[`6Hutc`/`12Hutc`/`1Dutc`/`1Wutc`/`1Mutc`/`3Mutc`]  
limit | String | 否 | 分页返回的结果集数量，最大为`100`，不填默认返回`100`条  
  
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
            "0"
        ],
        [
            "1597026383085",
            "3.731",
            "3.799",
            "3.494",
            "3.72",
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
confirm | String | K线状态   
`0` 代表 K 线未完结，`1` 代表 K 线已完结。  
返回的第一条K线数据可能不是完整周期k线，返回值数组顺序分别为是：[ts,o,h,l,c,confirm] 

### 获取指数历史K线数据 

获取最近几年的指数K线数据

#### 限速：10次/2s

#### 限速规则：IP

#### HTTP请求

`GET /api/v5/market/history-index-candles`

> 请求示例
    
    
    GET /api/v5/market/history-index-candles?instId=BTC-USD
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
instId | String | 是 | 现货指数，如`BTC-USD`  
与 `uly` 含义相同。  
after | String | 否 | 请求此时间戳之前（更旧的数据）的分页内容，传的值为对应接口的`ts`  
before | String | 否 | 请求此时间戳之后（更新的数据）的分页内容，传的值为对应接口的`ts`, 单独使用时，会返回最新的数据。  
bar | String | 否 | 时间粒度，默认值`1m`  
如 [1m/3m/5m/15m/30m/1H/2H/4H]   
UTC+8开盘价k线：[6H/12H/1D/1W/1M]  
UTC+0开盘价k线：[/6Hutc/12Hutc/1Dutc/1Wutc/1Mutc]  
limit | String | 否 | 分页返回的结果集数量，最大为100，不填默认返回100条  
  
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
            "1"
        ],
        [
            "1597026383085",
            "3.731",
            "3.799",
            "3.494",
            "3.72",
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
confirm | String | K线状态   
`0` 代表 K 线未完结，`1` 代表 K 线已完结。  
返回值数组顺序分别为是：[ts,o,h,l,c,confirm] 

### 获取标记价格K线数据 

标记价格K线数据每个粒度最多可获取最近1,440条。

#### 限速：20次/2s

#### 限速规则：IP

#### HTTP请求

`GET /api/v5/market/mark-price-candles`

> 请求示例
    
    
    GET /api/v5/market/mark-price-candles?instId=BTC-USD-SWAP
    
    
    
    import okx.MarketData as MarketData
    
    flag = "0"  # 实盘:0 , 模拟盘：1
    
    marketDataAPI =  MarketData.MarketAPI(flag=flag)
    
    # 获取标记价格K线数据
    result = marketDataAPI.get_mark_price_candlesticks(
        instId="BTC-USD-SWAP"
    )
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
instId | String | 是 | 产品ID，如`BTC-USD-SWAP`  
after | String | 否 | 请求此时间戳之前（更旧的数据）的分页内容，传的值为对应接口的`ts`  
before | String | 否 | 请求此时间戳之后（更新的数据）的分页内容，传的值为对应接口的`ts`, 单独使用时，会返回最新的数据。  
bar | String | 否 | 时间粒度，默认值`1m`  
如 [1m/3m/5m/15m/30m/1H/2H/4H]   
UTC+8开盘价k线：[6H/12H/1D/1W/1M/3M]  
UTC+0开盘价k线：[6Hutc/12Hutc/1Dutc/1Wutc/1Mutc/3Mutc]  
limit | String | 否 | 分页返回的结果集数量，最大为100，不填默认返回100条  
  
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
            "0"
        ],
        [
            "1597026383085",
            "3.731",
            "3.799",
            "3.494",
            "3.72",
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
confirm | String | K线状态   
`0` 代表 K 线未完结，`1` 代表 K 线已完结。  
返回的第一条K线数据可能不是完整周期k线，返回值数组顺序分别为是：[ts,o,h,l,c,confirm] 

### 获取标记价格历史K线数据 

获取最近几年的标记价格K线数据

#### 限速：20次/2s

#### 限速规则：IP

#### HTTP请求

`GET /api/v5/market/history-mark-price-candles`

> 请求示例
    
    
    GET /api/v5/market/history-mark-price-candles?instId=BTC-USD-SWAP
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
instId | String | 是 | 产品ID，如`BTC-USD-SWAP`  
after | String | 否 | 请求此时间戳之前（更旧的数据）的分页内容，传的值为对应接口的`ts`  
before | String | 否 | 请求此时间戳之后（更新的数据）的分页内容，传的值为对应接口的`ts`, 单独使用时，会返回最新的数据。  
bar | String | 否 | 时间粒度，默认值`1m`  
如 [1m/3m/5m/15m/30m/1H/2H/4H]   
UTC+8开盘价k线：[6H/12H/1D/1W/1M]  
UTC+0开盘价k线：[6Hutc/12Hutc/1Dutc/1Wutc/1Mutc]  
limit | String | 否 | 分页返回的结果集数量，最大为100，不填默认返回100条  
  
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
            "1"
        ],
        [
            "1597026383085",
            "3.731",
            "3.799",
            "3.494",
            "3.72",
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
confirm | String | K线状态   
`0` 代表 K 线未完结，`1` 代表 K 线已完结。  
返回值数组顺序分别为是：[ts,o,h,l,c,confirm] 

### 获取法币汇率 

该接口提供的是2周的平均汇率数据

#### 限速：1次/2s

#### 限速规则：IP

#### HTTP请求

`GET /api/v5/market/exchange-rate`

> 请求示例
    
    
    GET /api/v5/market/exchange-rate
    
    
    
    import okx.MarketData as MarketData
    
    flag = "0"  # 实盘:0 , 模拟盘：1
    
    marketDataAPI =  MarketData.MarketAPI(flag=flag)
    
    # 获取法币汇率
    result = marketDataAPI.get_exchange_rate(
    )
    print(result)
    

> 返回结果
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "usdCny": "7.162"
            }
        ]
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
usdCny | String | 人民币兑美元汇率  
  
### 获取指数成分数据 

查询市场上的指数成分信息数据

#### 限速：20次/2s

#### 限速规则：IP

#### HTTP请求

`GET /api/v5/market/index-components`

> 请求示例
    
    
    GET /api/v5/market/index-components?index=BTC-USD
    
    
    
    import okx.MarketData as MarketData
    
    flag = "0"  # 实盘:0 , 模拟盘：1
    
    marketDataAPI =  MarketData.MarketAPI(flag=flag)
    
    # 获取指数成分数据
    result = marketDataAPI.get_index_components(
        index="BTC-USD"
    )
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
index | String | 是 | 指数，如 `BTC-USDT`  
与 `uly` 含义相同。  
  
> 返回结果
    
    
    {
        "code": "0",
        "msg": "",
        "data": {
            "components": [
                {
                    "symbol": "BTC/USDT",
                    "symPx": "52733.2",
                    "wgt": "0.25",
                    "cnvPx": "52733.2",
                    "exch": "OKEx"
                },
                {
                    "symbol": "BTC/USDT",
                    "symPx": "52739.87000000",
                    "wgt": "0.25",
                    "cnvPx": "52739.87000000",
                    "exch": "Binance"
                },
                {
                    "symbol": "BTC/USDT",
                    "symPx": "52729.1",
                    "wgt": "0.25",
                    "cnvPx": "52729.1",
                    "exch": "Huobi"
                },
                {
                    "symbol": "BTC/USDT",
                    "symPx": "52739.47929397",
                    "wgt": "0.25",
                    "cnvPx": "52739.47929397",
                    "exch": "Poloniex"
                }
            ],
            "last": "52735.4123234925",
            "index": "BTC-USDT",
            "ts": "1630985335599"
        }
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
index | String | 指数名称  
last | String | 最新指数价格  
ts | String | 数据产生时间，Unix时间戳的毫秒数格式， 如`1597026383085`  
components | String | 成分  
> exch | String | 交易所名称  
> symbol | String | 采集的币对名称  
> symPx | String | 采集的币对价格  
> wgt | String | 权重  
> cnvPx | String | 换算成指数后的价格  
  
### 获取经济日历数据 

该接口需验证后使用。仅支持实盘服务。 

获取过去三个月的宏观经济日历数据。三个月前的历史数据仅开放给交易费等级VIP1及以上的用户。

#### 限速：1次/5s

#### 限速规则：IP

#### HTTP请求

`GET /api/v5/public/economic-calendar`

> 请求示例
    
    
    GET /api/v5/public/economic-calendar
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
region | string | 否 | 国家，地区或实体   
`afghanistan`, `albania`, `algeria`, `andorra`, `angola`, `antigua_and_barbuda`, `argentina`, `armenia`, `aruba`, `australia`, `austria`, `azerbaijan`, `bahamas`, `bahrain`, `bangladesh`, `barbados`, `belarus`, `belgium`, `belize`, `benin`, `bermuda`, `bhutan`, `bolivia`, `bosnia_and_herzegovina`, `botswana`, `brazil`, `brunei`, `bulgaria`, `burkina_faso`, `burundi`, `cambodia`, `cameroon`, `canada`, `cape_verde`, `cayman_islands`, `central_african_republic`, `chad`, `chile`, `china`, `colombia`, `comoros`, `congo`, `costa_rica`, `croatia`, `cuba`, `cyprus`, `czech_republic`, `denmark`, `djibouti`, `dominica`, `dominican_republic`, `east_timor`, `ecuador`, `egypt`, `el_salvador`, `equatorial_guinea`, `eritrea`, `estonia`, `ethiopia`, `euro_area`, `european_union`, `faroe_islands`, `fiji`, `finland`, `france`, `g20`, `g7`, `gabon`, `gambia`, `georgia`, `germany`, `ghana`, `greece`, `greenland`, `grenada`, `guatemala`, `guinea`, `guinea_bissau`, `guyana`, `hungary`, `haiti`, `honduras`, `hong_kong`, `hungary`, `imf`, `indonesia`, `iceland`, `india`, `indonesia`, `iran`, `iraq`, `ireland`, `isle_of_man`, `israel`, `italy`, `ivory_coast`, `jamaica`, `japan`, `jordan`, `kazakhstan`, `kenya`, `kiribati`, `kosovo`, `kuwait`, `kyrgyzstan`, `laos`, `latvia`, `lebanon`, `lesotho`, `liberia`, `libya`, `liechtenstein`, `lithuania`, `luxembourg`, `macau`, `macedonia`, `madagascar`, `malawi`, `malaysia`, `maldives`, `mali`, `malta`, `mauritania`, `mauritius`, `mexico`, `micronesia`, `moldova`, `monaco`, `mongolia`, `montenegro`, `morocco`, `mozambique`, `myanmar`, `namibia`, `nepal`, `netherlands`, `new_caledonia`, `new_zealand`, `nicaragua`, `niger`, `nigeria`, `north_korea`, `northern_mariana_islands`, `norway`, `opec`, `oman`, `pakistan`, `palau`, `palestine`, `panama`, `papua_new_guinea`, `paraguay`, `peru`, `philippines`, `poland`, `portugal`, `puerto_rico`, `qatar`, `russia`, `republic_of_the_congo`, `romania`, `russia`, `rwanda`, `slovakia`, `samoa`, `san_marino`, `sao_tome_and_principe`, `saudi_arabia`, `senegal`, `serbia`, `seychelles`, `sierra_leone`, `singapore`, `slovakia`, `slovenia`, `solomon_islands`, `somalia`, `south_africa`, `south_korea`, `south_sudan`, `spain`, `sri_lanka`, `st_kitts_and_nevis`, `st_lucia`, `sudan`, `suriname`, `swaziland`, `sweden`, `switzerland`, `syria`, `taiwan`, `tajikistan`, `tanzania`, `thailand`, `togo`, `tonga`, `trinidad_and_tobago`, `tunisia`, `turkey`, `turkmenistan`, `uganda`, `ukraine`, `united_arab_emirates`, `united_kingdom`, `united_states`, `uruguay`, `uzbekistan`, `vanuatu`, `venezuela`, `vietnam`, `world`, `yemen`, `zambia`, `zimbabwe`  
importance | string | 否 | 重要性   
`1`: 低   
`2`: 中等   
`3`: 高  
before | String | 否 | 查询发布日期(date)之后的内容，值为时间戳，Unix 时间戳为毫秒数格式，如 `1597026383085`  
after | String | 否 | 查询发布日期(date)之前的内容，值为时间戳，Unix 时间戳为毫秒数格式，如 `1597026383085`   
默认值为请求时刻的时间戳  
limit | String | 否 | 分页返回结果的数量，最大为100，默认100条  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "actual": "7.8%",
                "calendarId": "330631",
                "category": "Harmonised Inflation Rate YoY",
                "ccy": "",
                "date": "1700121600000",
                "dateSpan": "0",
                "event": "Harmonised Inflation Rate YoY",
                "forecast": "7.8%",
                "importance": "1",
                "prevInitial": "",
                "previous": "9%",
                "refDate": "1698710400000",
                "region": "Slovakia",
                "uTime": "1700121605007",
                "unit": "%"
            }
        ],
        "msg": ""
    }
    
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
calendarId | string | 经济日历ID  
date | string | actual字段值的预期发布时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
region | string | 国家，地区或实体  
category | string | 类别名  
event | string | 事件名  
refDate | string | 当前事件指向的日期  
actual | string | 事件实际值  
previous | string | 当前事件上个周期的最新实际值。  
若发生数据修正，该字段存储上个周期修正后的实际值。  
forecast | string | 由权威经济学家共同得出的预测值  
dateSpan | string | `0`：事件的具体发生时间已知  
`1`：事件的具体发生日期已知，但时间未知  
importance | string | 重要性   
`1`: 低   
`2`: 中等   
`3`: 高  
uTime | string | 当前事件的最新更新时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
prevInitial | string | 该事件上一周期的初始值  
仅在修正发生时有值  
ccy | string | 事件实际值对应的货币  
unit | string | 事件实际值对应的单位  
  
### 获取历史市场数据

**数据覆盖范围**  
历史数据回填正在进行中，不同模块、产品和时间段的数据覆盖范围可能有所差异。数据集将持续扩展，以提供更全面的历史数据覆盖。  **旧数据格式注意**  
对于模块1（交易历史），一些旧的历史文件可能包含同时带有中文字符和英文列名的列标题。数据回填完成后，所有中文字符将被移除。请在解析数据时考虑到这一点。  **数据发布安排**  
模块 1、2、3、11 的数据通常在 T+2 可用；订单簿数据通常在 T+3 可用。 

获取OKX历史市场数据。

#### 限速：2次/5s

#### 限速规则：IP

#### HTTP请求

`GET /api/v5/public/market-data-history`

> 请求示例
    
    
    GET /api/v5/public/market-data-history?module=1&instType=SWAP&instFamilyList=BTC-USDT&dateAggrType=daily&begin=1756604295000&end=1756777095000
    

#### 请求参数

参数名称 | 类型 | 是否必须 | 描述  
---|---|---|---  
module | String | 是 | 数据模块类型  
`1`: 逐笔成交历史  
`2`: 1分钟K线  
`3`: 资金费率  
`4`: 400档位深度   
`5`: 5000档位深度（自2025年11月1日起支持）  
`6`: 50档位深度 (将逐步弃用，请使用 module = `4`,`5` 代替)  
`11`: 借币利率  
instType | String | 是 | 产品类型  
`SPOT`  
`FUTURES`  
`SWAP`  
`OPTION`  
instIdList | String | 可选 | 产品ID列表，例如 `BTC-USDT` 或 `ANY` 表示所有产品（`ANY` 仅支持 module = `1`, `2`, `3`, `11` & dateAggrType = `daily`）  
多个产品请用英文逗号分隔，如 `BTC-USDT,ETH-USDT`  
最大长度 = 10   
仅适用于instType = `SPOT`  
instFamilyList | String | 可选 | 交易品种列表，例如 `BTC-USDT` 或 `ANY` 表示所有产品（`ANY` 仅支持 module = `1`, `2`, `3`, `11` & dateAggrType = `daily`）  
多个品种请用英文逗号分隔，如 `BTC-USDT,ETH-USDT`  
最大长度 = 10 (当module = `6` & instType = `OPTION`时为1)   
仅适用于instType ≠ `SPOT`  
dateAggrType | String | 是 | 日期聚合类型  
`daily` (不支持 module = `3` & instFamilyList ≠ `ANY`)  
`monthly` （不支持module = `6`）  
begin | String | 是 | 开始时间戳，Unix时间戳格式为毫秒数（包含该时间）  
日度最大范围：20天，月度最大范围：20个月  
end | String | 是 | 结束时间戳，Unix时间戳格式为毫秒数（包含该时间）  
当module = `6` & instType = `OPTION`时，仅返回`end`指定日期的数据  
  
> 返回示例
    
    
    {
      "code": "0",
      "data": [{
        "dateAggrType": "daily",
        "details": [{
          "dateRangeEnd": "1756656000000",
          "dateRangeStart": "1756569600000",
          "groupDetails": [{
            "dateTs": "1756656000000",
            "filename": "BTC-USDT-SWAP-trades-2025-09-01.zip",
            "sizeMB": "10.82",
            "url": "https://static.okx.com/cdn/okex/traderecords/trades/daily/20250901/BTC-USDT-SWAP-trades-2025-09-01.zip"
          },
          {
            "dateTs": "1756569600000",
            "filename": "BTC-USDT-SWAP-trades-2025-08-31.zip",
            "sizeMB": "4.82",
            "url": "https://static.okx.com/cdn/okex/traderecords/trades/daily/20250831/BTC-USDT-SWAP-trades-2025-08-31.zip"
          }],
          "groupSizeMB": "15.64",
          "instFamily": "BTC-USDT",
          "instId": "",
          "instType": "SWAP"
        }],
        "totalSizeMB": "15.64",
        "ts": "1756882260390"
      }],
      "msg": ""
    }
    

> 返回示例，当没有数据文件时
    
    
    {
        "code": "0",
        "data": [
            {
                "dateAggrType": "monthly",
                "details": [],
                "totalSizeMB": "0",
                "ts": "1756889595507"
            }
        ],
        "msg": ""
    }
    

#### 返回参数

**参数名称** | **类型** | **描述**  
---|---|---  
ts | String | 响应时间戳，Unix时间戳格式为毫秒数  
totalSizeMB | String | 所有数据文件总大小，单位MB  
dateAggrType | String | 日期聚合类型  
`daily`  
`monthly`  
details | Array |   
> instId | String | 产品ID  
> instFamily | String | 交易品种  
> dateRangeStart | String | 数据范围开始日期，Unix时间戳格式为毫秒数（包含该时间）  
> dateRangeEnd | String | 数据范围结束日期，Unix时间戳格式为毫秒数（包含该时间）  
> groupSizeMB | String | 数据组大小，单位MB  
> groupDetails | Array |   
>> filename | String | 数据文件名，例如 `BTC-USDT-SWAP-trades-2025-05-15.zip`  
>> dataTs | String | 数据日期时间戳，Unix时间戳格式为毫秒数  
>> sizeMB | String | 文件大小，单位MB  
>> url | String | 下载链接  
**数据查询规则**  
• 仅使用时间戳的日期部分（yyyy-mm-dd），忽略时间部分  
• begin和end时间戳均为包含该时间  
• 数据按倒序时间顺序返回（越接近end的数据越靠前）  
• 如果查询超出记录限制，返回最接近end时间戳的数据  
• **例外：** 当 module = 6 且 instType = OPTION 时，仅返回 end 指定日期的数据  **时间戳解析的时区规范**  
将Unix时间戳转换为日期时，以下时区约定适用于所有时间戳字段（begin, end, dateRangeStart, dateRangeEnd, dataTs）：  
• **深度数据** （模块4、5、6）：UTC+0  
• **其他数据模块** （模块1、2、3、11）：UTC+8 

### 获取 MM 币对分类类型 

获取当前做市商（MM）计划 SPOT 和 SWAP 产品的币对分类类型列表。

#### 限速：每2秒5次请求

#### 限速规则：IP

#### HTTP请求

`GET /api/v5/public/mm-instrument-types`

> 请求示例
    
    
    GET /api/v5/public/mm-instrument-types?instType=SWAP
    
    
    
    import okx.PublicData as PublicData
    
    flag = "0"  # 实盘:0 , 模拟盘：1
    
    publicDataAPI = PublicData.PublicAPI(flag=flag)
    
    # 获取 MM 币对分类类型
    result = publicDataAPI.get_mm_instrument_types(
        instType="SWAP"
    )
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
instType | String | 否 | 产品类型  
`SPOT`  
`SWAP`  
未指定时返回全部类型  
instId | String | 否 | 产品ID，如 `BTC-USDT`、`BTC-USDT-SWAP`  
指定时返回至多一条记录  
  
> 返回结果
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "instId": "BTC-USDT-SWAP",
                "instType": "SWAP",
                "pairType": "A"
            },
            {
                "instId": "ETH-USDT-SWAP",
                "instType": "SWAP",
                "pairType": "A"
            },
            {
                "instId": "XAU-USDT-SWAP",
                "instType": "SWAP",
                "pairType": "B-TradFi"
            }
        ]
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
instId | String | 产品ID，如 `BTC-USDT-SWAP`  
instType | String | 产品类型  
`SPOT`  
`SWAP`  
pairType | String | MM 计划分类类型  
`A`：高流动性品种  
`B-Crypto`：中低流动性加密资产  
`B-TradFi`：传统金融品种（仅 SWAP）  
  
## WebSocket 

### 产品频道 

增量数据的触发场景有：  
1\. 当有产品状态 state 变化时（如期货交割、期权行权、新合约/币对上线、人工暂停/恢复交易等）  
2\. 当交易参数变更（tickSz,minSz,maxMktSz）时  
3\. 当上线时间或者下线时间（expTime， listTime）变更时  

#### URL Path

/ws/v5/public

> 请求示例
    
    
    { 
      "id": "1512",
      "op": "subscribe",  
      "args":   [    
        {     
          "channel": "instruments",
          "instType": "SPOT"
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
              "channel": "instruments",
              "instType": "SPOT"
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
`instruments`  
> instType | String | 是 | 产品类型  
`SPOT`：币币  
`MARGIN`：币币杠杆  
`SWAP`：永续合约  
`FUTURES`：交割合约  
`OPTION`：期权  
`EVENTS`：事件合约  
  
> 成功返回示例
    
    
    {
      "id": "1512",
        "event": "subscribe",
        "arg": {
            "channel": "instruments",
            "instType": "SPOT"
        },
        "connId": "a4d3ae55"
    }
    

> 失败返回示例
    
    
    {
      "id": "1512",
        "event": "error",
        "code": "60012",
        "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{ \"channel\" : \"instruments\", \"instType\" : \"FUTURES\"}]}",
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
`OPTION`：期权  
`EVENTS`：事件合约  
code | String | 否 | 错误码  
msg | String | 否 | 错误消息  
connId | String | 是 | WebSocket连接ID  
  
> 推送示例
    
    
    {
      "arg": {
        "channel": "instruments",
        "instType": "SPOT"
      },
      "data": [
        {
            "alias": "",
            "auctionEndTime": "",
            "baseCcy": "BTC",
            "category": "1",
            "ctMult": "",
            "ctType": "",
            "ctVal": "",
            "ctValCcy": "",
            "contTdSwTime": "1704876947000",
            "expTime": "",
            "futureSettlement": false,
            "groupId": "1",
            "instFamily": "",
            "instId": "BTC-USDT",
            "instType": "SPOT",
            "lever": "10",
            "listTime": "1606468572000",
            "lotSz": "0.00000001",
            "maxIcebergSz": "9999999999.0000000000000000",
            "maxLmtAmt": "1000000",
            "maxLmtSz": "9999999999",
            "maxMktAmt": "1000000",
            "maxMktSz": "",
            "maxStopSz": "",
            "maxTriggerSz": "9999999999.0000000000000000",
            "maxTwapSz": "9999999999.0000000000000000",
            "minSz": "0.00001",
            "optType": "",
            "openType": "call_auction",
            "preMktSwTime": "",
            "quoteCcy": "USDT",
            "settleCcy": "",
            "state": "live",
            "ruleType": "normal",
            "stk": "",
            "tickSz": "0.1",
            "uly": "",
            "instIdCode": 1000000000，
            "instCategory": "1",
            "upcChg": [
                {
                    "param": "tickSz",
                    "newValue": "0.0001",
                    "effTime": "1704876947000"
                }
            ]
        }
      ]
    }
    

#### 推送数据参数

参数名 | 类型 | 描述  
---|---|---  
arg | Object | 订阅的频道  
> channel | String | 频道名  
> instType | String | 产品类型  
data | Array of objects | 订阅的数据  
> instType | String | 产品类型  
> seriesId | String | 系列 ID，如 `BTC-ABOVE-DAILY`。仅适用于 `EVENTS`  
> instId | String | 产品ID，如 `BTC-USDT`  
> category | String | ~~币种类别~~ （已废弃）  
> uly | String | 标的指数，如 `BTC-USD`，仅适用于`交割`/`永续`/`期权`  
> groupId | String | 交易产品手续费分组ID  
现货：  
`1`：USDT现货  
`2`：USDC及Crypto现货  
`3`：TRY现货  
`4`：EUR现货  
`5`：BRL现货  
`7`：AED现货  
`8`：AUD现货  
`9`：USD现货  
`10`：SGD现货  
`11`：零手续费现货  
`12`：现货分组一  
`13`：现货分组二  
`14`：现货分组三  
`15`: 现货特别分组  
  
交割合约：  
`1`：币本位交割合约  
`2`：USDT本位交割合约  
`3`：USDC本位交割合约  
`4`：盘前交易交割合约  
`5`：交割合约分组一  
`6`：交割合约分组二  
  
永续合约：  
`1`：币本位永续合约  
`2`：USDT本位永续合约  
`3`：USDC本位永续合约  
`4`：永续合约分组一  
`5`：永续合约分组二  
`6`：股票永续合约  
  
期权：  
`1`：币本位期权  
`2`：USDC本位期权  
  
**用户需要同时使用instType和groupId来确定一个交易产品的交易手续费分组；用户应该将此接口和[获取当前账户交易手续费费率](/docs-v5/zh/#trading-account-rest-api-get-fee-rates)一起使用，以获取特定交易产品的手续费率**   
  
**部分枚举值可能不适用于您，以实际返回为准**  
> instFamily | String | 交易品种，如 `BTC-USD`，仅适用于`交割`/`永续`/`期权`  
> baseCcy | String | 交易货币币种，如 `BTC-USDT`中`BTC`，仅适用于`币币/币币杠杆`  
> quoteCcy | String | 计价货币币种，如 `BTC-USDT`中`USDT`，仅适用于`币币/币币杠杆`  
> settleCcy | String | 盈亏结算和保证金币种，如 `BTC`，仅适用于 `交割`/`永续`/`期权`  
> ctVal | String | 合约面值  
> ctMult | String | 合约乘数  
> ctValCcy | String | 合约面值计价币种  
> optType | String | 期权类型  
`C`：看涨期权  
`P`：看跌期权  
仅适用于`期权`  
> stk | String | 行权价格，仅适用于 `期权`  
> listTime | String | 上线时间  
> auctionEndTime | String | ~~集合竞价结束时间，Unix时间戳的毫秒数格式，如`1597026383085`   
仅适用于通过集合竞价方式上线的`币币`，其余情况返回""（已废弃，请使用contTdSwTime）~~  
> contTdSwTime | String | 连续交易开始时间，从集合竞价、提前挂单切换到连续交易的时间，Unix时间戳格式，单位为毫秒。e.g. `1597026383085`。  
仅适用于通过集合竞价或提前挂单上线的`SPOT`/`MARGIN`，在其他情况下返回""。  
> preMktSwTime | String | 盘前永续合约转为普通永续合约的时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
仅适用于盘前`SWAP`  
> openType | String | 开盘类型  
`fix_price`: 定价开盘  
`pre_quote`: 提前挂单  
`call_auction`: 集合竞价   
只适用于`SPOT`/`MARGIN`，其他业务线返回""  
> expTime | String | 产品下线时间  
适用于`币币/杠杆/交割/永续/期权`，对于 `交割/期权`，为自然的交割/行权时间；如果`币币/杠杆/交割/永续`产品人工下线，为产品下线时间，有变动就会推送。  
> lever | String | 该产品支持的最大杠杆倍数  
不适用于`币币`/`期权`。可用来区分`币币杠杆`和`币币`  
> tickSz | String | 下单价格精度，如 `0.0001`。  
对于 `OPTION`/`EVENTS`，该值为 tick band 中的最小下单价格精度。  
> lotSz | String | 下单数量精度  
合约的数量单位是`张`，现货的数量单位是`交易货币`  
> minSz | String | 最小下单数  
合约的数量单位是`张`，现货的数量单位是`交易货币`  
> ctType | String | 合约类型  
`linear`：正向合约  
`inverse`：反向合约  
仅适用于`交割/永续`  
> alias | String | 合约日期别名（已废弃，将于 2026 年 4 月底下线，请使用 expTime 字段获取交割时间）  
`this_week`：本周  
`next_week`：次周  
`this_month`：本月  
`next_month`：次月  
`quarter`：季度  
`next_quarter`：次季度  
`this_five_years`：当期五年合约  
`next_five_years`：次期五年合约  
仅适用于`交割`  
> state | String | 产品状态  
`live`：交易中   
`suspend`：暂停中  
`expired`：已过期  
`rebase`：合约在变基中，不可交易，仅适用于`SWAP`  
`post_only`：仅接受 post-only 订单；已有 post-only 订单可改单和撤单。其他订单类型（市价单、IOC、FOK、普通限价单）将被拒绝。仅适用于 `SWAP`  
`preopen`：预上线，交割和期权合约轮转生成到开始交易；部分交易产品上线前  
`test`：测试中（测试产品，不可交易）  
`settling`：结算中，仅适用于 `EVENTS`  
> ruleType | String | 交易规则类型  
`normal`：普通交易  
`pre_market`：盘前交易  
`rebase_contract`：盘前变基合约  
`xperp`：永续合约风格的交割合约，仅适用于部分 `FUTURES` 合约  
> maxLmtSz | String | 限价单的单笔最大委托数量  
合约的数量单位是`张`，现货的数量单位是`交易货币`  
> maxMktSz | String | 市价单的单笔最大委托数量  
合约的数量单位是`张`，现货的数量单位是`USDT`  
> maxTwapSz | String | 时间加权单的单笔最大委托数量  
合约的数量单位是`张`，现货的数量单位是`交易货币`  
> maxIcebergSz | String | 冰山委托的单笔最大委托数量  
合约的数量单位是`张`，现货的数量单位是`交易货币`  
> maxTriggerSz | String | 计划委托委托的单笔最大委托数量  
合约的数量单位是`张`，现货的数量单位是`交易货币`  
> maxStopSz | String | 止盈止损市价委托的单笔最大委托数量  
合约的数量单位是`张`，现货的数量单位是`USDT`  
> futureSettlement | Boolean | 交割合约是否支持每日结算  
适用于`全仓``交割`  
> instIdCode | Integer | 产品唯一标识代码。  
对于简单二进制编码，您必须使用 `instIdCode` 而不是 `instId`。  
对于同一`instId`，实盘和模拟盘的值可能会不一样。   
当值还未生成时，返回 `null`。  
> instCategory | String | 标的资产类别（产品ID的第一部分）。例如：对于 `BTC-USDT-SWAP`，instCategory 表示 `BTC` 所属的资产类别。  
`1`: 加密货币   
`3`: 股票类资产   
`4`: 大宗商品   
`5`: 外汇   
`6`: 债券   
`""` 当值不可用时返回空字符串  
> upcChg | Array of objects | 即将变更的参数列表。当没有即将变更的参数时，返回空数组 []  
>> param | String | 即将变更的参数名称。  
`tickSz`  
`minSz`：若为交割/永续合约（`FUTURES`/`SWAP`），`lotSz` 会同步变更。  
`maxMktSz`  
>> newValue | String | 即将变更的参数值。  
>> effTime | String | 生效时间。Unix 时间戳格式，例如 `1597026383085`  
产品状态变更，是触发instrument接口推送条件： 当合约预上线时，状态变更为预上线（即新生成一个合约，新合约会处于预上线状态）； 当产品下线的时候（如交割合约被交割的时候，期权合约被行权的时候），状态变更为已过期  listTime以及contTdSwTime  
对于通过集合竞价/提前挂单方式上线的币币，listTime为集合竞价/提前挂单的开始时间，contTdSwTime为集合竞价/提前挂单的结束时间、连续交易的开始时间；对于其他情况及业务线，listTime即为连续交易开始时间，contTdSwTime将返回""  state  
对于`币币`、`杠杆`、`永续`和`交割`，状态state在时间到达listTime时由`preopen`转变为`live`。对于`期权`合约，由于内部处理原因，状态可能在`listTime`之后短暂延迟变为`live`。建议在下单前确认`state`为`live`。上线前，交易产品频道将推送预上线产品，状态为`state:preopen`；若上线被取消，频道将全量推送数据，其中不包括被取消的预上线产品，不做额外通知。交易产品上线时（`期权`合约可能在listTime之后短暂时间内），频道将推送状态为交易中`state:live`。用户亦可以通过REST接口查询到相应数据。  
当产品下线的时候（如交割合约被交割的时候，期权合约被行权的时候），查询不到该产品 

### 事件合约市场频道 

推送事件合约市场状态更新及 floorStrike 生成。不推送初始快照。

#### URL Path

/ws/v5/public

> 请求示例
    
    
    {
        "op": "subscribe",
        "args": [
            {
                "channel": "event-contract-markets",
                "instType": "EVENTS"
            }
        ]
    }
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
id | String | 否 | 消息的唯一标识。用户提供，返回参数中会返回以便于找到相应的请求。字母（区分大小写）与数字的组合，可以是纯字母、纯数字且长度必须要在1-32位之间。  
op | String | 是 | 操作。  
`subscribe`  
`unsubscribe`  
args | Array of objects | 是 | 订阅频道列表  
> channel | String | 是 | 频道名。  
`event-contract-markets`  
> instType | String | 是 | 产品类型。  
`EVENTS`  
  
> 成功返回示例
    
    
    {
        "id": "1512",
        "event": "subscribe",
        "arg": {
            "channel": "event-contract-markets",
            "instType": "EVENTS"
        },
        "connId": "a4d3ae55"
    }
    

> 失败返回示例
    
    
    {
        "id": "1512",
        "event": "error",
        "code": "60012",
        "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{\"channel\": \"event-contract-markets\", \"instType\": \"EVENTS\"}]}",
        "connId": "a4d3ae55"
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
id | String | 消息的唯一标识  
event | String | 事件。  
`subscribe`  
`unsubscribe`  
`error`  
arg | Object | 订阅的频道  
> channel | String | 频道名  
> instType | String | 产品类型  
code | String | 错误码  
msg | String | 错误消息  
connId | String | WebSocket 连接 ID  
  
> 推送数据示例
    
    
    {
        "arg": {
            "channel": "event-contract-markets"
        },
        "data": [
            {
                "seriesId": "BTC-ABOVE-DAILY",
                "eventId": "BTC-ABOVE-DAILY-260224-1600",
                "instId": "BTC-ABOVE-DAILY-260224-1600-65000",
                "listTime": "1769697132335",
                "fixTime": "",
                "expTime": "1769697132335",
                "state": "live",
                "outcome": "0",
                "floorStrike": "120000",
                "capStrike": "",
                "settleValue": "",
                "disputed": false,
                "hitDir": ""
            }
        ]
    }
    

#### 推送数据参数

参数名 | 类型 | 描述  
---|---|---  
arg | Object | 订阅的频道  
> channel | String | 频道名  
data | Array of objects | 订阅数据  
> seriesId | String | 系列 ID，如 `BTC-ABOVE-DAILY`  
> eventId | String | 事件 ID，如 `BTC-ABOVE-DAILY-260224-1600`  
> instId | String | 产品 ID，如 `BTC-ABOVE-DAILY-260224-1600-65000`  
> listTime | String | 上线时间。Unix时间戳的毫秒数格式，如 `1597026383085`  
> fixTime | String | 行权价格确定时间。Unix时间戳的毫秒数格式，如 `1597026383085`。仅适用于 `price_up_down` 结算方式。  
> expTime | String | 行权时间。Unix时间戳的毫秒数格式，如 `1597026383085`。结算后更新。  
> state | String | 市场状态。  
`preopen`  
`live`  
`settling`  
`expired`  
> outcome | String | 市场结果。  
`0`：未确定  
`1`：YES  
`2`：NO。  
`1`/`2` 仅在 state 为 `expired` 时适用  
> floorStrike | String | 导致 YES 结果的最低到期价格  
> capStrike | String | `between` 结算方式中导致 YES 结果的最大到期值。`"INF"` 表示无上限（最高区间）。  
非 `between` 方式返回 `""`。  
> settleValue | String | 结算价格。  
仅在 state 为 `expired` 时返回  
> disputed | Boolean | 是否存在争议。  
`true`  
`false`  
> hitDir | String | 触及方向。仅在结算方式为 `hit` 时适用。  
`up`：价格从下方触及  
`dn`：价格从上方触及  
`""`：不适用（非 `hit` 方式）  
  
### 持仓总量频道 

获取持仓总量，每3s有数据更新推送一次数据

#### URL Path

/ws/v5/public

> 请求示例
    
    
    {
        "id": "1512",
        "op": "subscribe",
        "args": [{
            "channel": "open-interest",
            "instId": "LTC-USD-SWAP"
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
              "channel": "open-interest",
              "instId": "LTC-USD-SWAP"
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
`open-interest`  
> instId | String | 是 | 产品ID  
  
> 成功返回示例
    
    
    {
        "id": "1512",
        "event": "subscribe",
        "arg": {
            "channel": "open-interest",
            "instId": "LTC-USD-SWAP"
        },
        "connId": "a4d3ae55"
    }
    

> 失败返回示例
    
    
    {
        "id": "1512",
        "event": "error",
        "code": "60012",
        "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{ \"channel\" : \"open-interest\", \"instId\" : \"LTC-USD-SWAP\"}]}",
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
            "channel": "open-interest",
            "instId": "BTC-USDT-SWAP"
        },
        "data": [
            {
                "instId": "BTC-USDT-SWAP",
                "instType": "SWAP",
                "oi": "2216113.01000000309",
                "oiCcy": "22161.1301000000309",
                "oiUsd": "1939251795.54769270396321",
                "ts": "1743041250440"
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
> instType | String | 产品类型  
> instId | String | 产品ID，如 `BTC-USDT-SWAP`  
> oi | String | 持仓量，按张为单位  
> oiCcy | String | 持仓量，按币为单位，如 BTC  
> oiUsd | String | 持仓量（按`USD`折算）  
> ts | String | 数据更新的时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
  
### 资金费率频道 

获取合约资金费率，30秒到90秒内推送一次数据

#### URL Path

/ws/v5/public

> 请求示例
    
    
    {
       "id": "1512",
        "op": "subscribe",
        "args": [{
            "channel": "funding-rate",
            "instId": "BTC-USD-SWAP"
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
              "channel": "funding-rate",
              "instId": "BTC-USD-SWAP"
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
`funding-rate`  
> instId | String | 是 | 产品ID  
  
> 成功返回示例
    
    
    {
       "id": "1512",
        "event": "subscribe",
        "arg": {
            "channel": "funding-rate",
            "instId": "BTC-USD-SWAP"
        },
        "connId": "a4d3ae55"
    }
    

> 失败返回示例
    
    
    {
       "id": "1512",
        "event": "error",
        "code": "60012",
        "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{ \"channel\" : \"funding-rate\", \"instId\" : \"BTC-USD-SWAP\"}]}",
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
> instId | String | 否 | 产品ID  
code | String | 否 | 错误码  
msg | String | 否 | 错误消息  
connId | String | 是 | WebSocket连接ID  
  
> 推送示例
    
    
    {
       "arg":{
          "channel":"funding-rate",
          "instId":"BTC-USD-SWAP"
       },
       "data":[
          {
             "fundingRate":"0.0001875391284828",
             "fundingTime":"1700726400000",
             "instId":"BTC-USD-SWAP",
             "instType":"SWAP",
             "method": "current_period",
             "maxFundingRate":"0.00375",
             "minFundingRate":"-0.00375",
             "nextFundingRate":"",
             "nextFundingTime":"1700755200000",
             "premium": "0.0001233824646391",
             "settFundingRate":"0.0001699799259033",
             "settState":"settled",
             "ts":"1700724675402"
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
> instType | String | 产品类型  
`SWAP`：永续合约  
`FUTURES`：X-Perps 交割合约  
> instId | String | 产品ID，如 `BTC-USD-SWAP`  
> method | String | 资金费收取逻辑   
`current_period`：当期收 ~~  
`next_period`：跨期收~~（不再支持跨期收合约）  
> formulaType | String | 公式类型  
`noRate`：旧资金费率计算公式  
`withRate`：新资金费率计算公式  
> fundingRate | String | 资金费率  
> fundingTime | String | 最新的到期结算的资金费时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
> nextFundingRate | String | ~~下一期预测资金费率~~ （不再支持跨期收合约）  
> nextFundingTime | String | 下一期资金费时间，Unix时间戳的毫秒数格式，如 `1622851200000`  
> minFundingRate | String | 下一期的预测资金费率下限  
> maxFundingRate | String | 下一期的预测资金费率上限  
> interestRate | String | 利率  
> impactValue | String | 深度加权金额（计价币数量）  
> settState | String | 资金费率结算状态   
`processing`：结算中   
`settled`：已结算  
> settFundingRate | String | 若 settState = `processing`，该字段代表用于本轮结算的资金费率；若 settState = `settled`，该字段代表用于上轮结算的资金费率  
> premium | String | 溢价指数  
公式：[max (0，深度加权买价 - 指数价格) – max (0，指数价格 – 深度加权卖价)] / 指数价格  
> ts | String | 数据更新时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
针对一些资金费率波动较大的小币种，OKX也将实时关注行情变化，在必要时候，将资金费率收取频率从8小时收付，改成频率较高的6小时/4小时/2小时/1小时收付。因此，用户应关注`fundingTime`及`nextFundingTime`字段以确定合约的资金费收取频率。 

### 限价频道 

获取交易产品的最高买价和最低卖价。限价有变化时，每 200 毫秒推送一次数据，限价没变化时，不推送数据

#### URL Path

/ws/v5/public

> 请求示例
    
    
    {
        "id": "1512",
        "op": "subscribe",
        "args": [{
            "channel": "price-limit",
            "instId": "LTC-USD-190628"
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
              "channel": "price-limit",
              "instId": "LTC-USD-190628"
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
`price-limit`  
> instId | String | 是 | 产品ID  
  
> 成功返回示例
    
    
    {
        "id": "1512",
        "event": "subscribe",
        "arg": {
            "channel": "price-limit",
            "instId": "LTC-USD-190628"
        },
        "connId": "a4d3ae55"
    }
    

> 失败返回示例
    
    
    {
        "id": "1512",
        "event": "error",
        "code": "60012",
        "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{ \"channel\" : \"price-limit\", \"instId\" : \"LTC-USD-190628\"}]}",
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
            "channel": "price-limit",
            "instId": "LTC-USD-190628"
        },
        "data": [{
            "instId": "LTC-USD-190628",
            "buyLmt": "200",
            "sellLmt": "300",
            "ts": "1597026383085",
            "enabled": true
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
> instId | String | 产品ID，如 `BTC-USD-SWAP`  
> buyLmt | String | 最高买价   
当enabled为false时，返回""  
> sellLmt | String | 最低卖价   
当enabled为false时，返回""  
> ts | String | 限价数据更新时间 ，Unix时间戳的毫秒数格式，如 `1597026383085`  
> enabled | Boolean | 限价是否生效   
`true`：限价生效   
`false`：限价不生效  
  
### 期权定价频道 

获取所有期权合约详细定价信息，一次性推送所有

#### URL Path

/ws/v5/public

> 请求示例
    
    
    {
        "id": "1512",
        "op": "subscribe",
        "args": [{
            "channel": "opt-summary",
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
        args = [
            {
              "channel": "opt-summary",
              "instFamily": "BTC-USD"
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
`opt-summary`  
> instFamily | String | 是 | 交易品种  
  
> 返回示例
    
    
    {
        "id": "1512",
        "event": "subscribe",
        "arg": {
            "channel": "opt-summary",
            "instFamily": "BTC-USD"
        },
        "connId": "a4d3ae55"
    }
    

> 失败示例
    
    
    {
        "id": "1512",
        "event": "error",
        "code": "60012",
        "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{ \"channel\" : \"opt-summary\", \"instFamily\" : \"BTC-USD\"}]}",
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
> instFamily | String | 是 | 交易品种  
code | String | 否 | 错误码  
msg | String | 否 | 错误消息  
connId | String | 是 | WebSocket连接ID  
  
> 推送示例
    
    
    {
        "arg": {
            "channel": "opt-summary",
            "instFamily": "BTC-USD"
        },
        "data": [
            {
                "instType": "OPTION",
                "instId": "BTC-USD-241013-70000-P",
                "uly": "BTC-USD",
                "delta": "-1.1180902625",
                "gamma": "2.2361957091",
                "vega": "0.0000000001",
                "theta": "0.0000032334",
                "lever": "8.465747567",
                "markVol": "0.3675503331",
                "bidVol": "0",
                "askVol": "1.1669998535",
                "realVol": "",
                "deltaBS": "-0.9999672034",
                "gammaBS": "0.0000000002",
                "thetaBS": "28.2649858387",
                "vegaBS": "0.0000114332",
                "ts": "1728703155650",
                "fwdPx": "62604.6993093463",
                "volLv": "0.2044711229"
            }
        ]
    }
    

#### 推送数据参数

**参数名** | **类型** | **描述**  
---|---|---  
arg | Object | 订阅成功的频道  
> channel | String | 频道名  
> instFamily | String | 交易品种  
data | Array of objects | 订阅的数据  
> instType | String | 产品类型， `OPTION`  
> instId | String | 产品ID  
> uly | String | 标的指数  
> delta | String | 期权价格对`uly`价格的敏感度  
> gamma | String | delta对`uly`价格的敏感度  
> vega | String | 期权价格对隐含波动率的敏感度  
> theta | String | 期权价格对剩余期限的敏感度  
> deltaBS | String | BS模式下期权价格对`uly`价格的敏感度  
> gammaBS | String | BS模式下delta对`uly`价格的敏感度  
> vegaBS | String | BS模式下期权价格对隐含波动率的敏感度  
> thetaBS | String | BS模式下期权价格对剩余期限的敏感度  
> lever | String | 杠杆倍数  
> markVol | String | 标记波动率  
> bidVol | String | bid波动率  
> askVol | String | ask波动率  
> realVol | String | 已实现波动率，目前该字段暂未启用  
> volLv | String | 平价期权的隐含波动率  
> fwdPx | String | 远期价格  
> ts | String | 数据更新时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
  
### 预估永续/交割/行权/结算价格频道 

在永续/交割/行权/结算前一小时内，将基于指数价格计算并推送预估价，更新频率约为每 200 毫秒一次。

#### URL Path

/ws/v5/public

> 请求示例
    
    
    {
        "id": "1512",
        "op": "subscribe",
        "args": [{
            "channel": "estimated-price",
            "instType": "FUTURES",
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
        args = [
            {
              "channel": "estimated-price",
              "instType": "FUTURES",
              "instFamily": "BTC-USD"
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
`estimated-price`  
> instType | String | 是 | 产品类型  
`FUTURES`：交割  
`OPTION`：期权  
`SWAP`：永续  
`EVENTS`：事件合约  
> instFamily | String | 可选 | 交易品种  
`instFamily`和`instId`必须指定一个  
> instId | String | 可选 | 产品ID  
`instFamily`和`instId`必须指定一个  
  
> 成功返回示例
    
    
    {
        "id": "1512",
        "event": "subscribe",
        "arg": {
            "channel": "estimated-price",
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
        "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{ \"channel\" : \"estimated-price\", \"instId\" : \"FUTURES\",\"instFamily\" :\"BTC-USD\"}]}",
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
`FUTURES`：交割  
`OPTION`：期权  
`SWAP`：永续  
`EVENTS`：事件合约  
> instFamily | String | 否 | 交易品种  
> instId | String | 否 | 产品ID  
code | String | 否 | 错误码  
msg | String | 否 | 错误消息  
connId | String | 是 | WebSocket连接ID  
  
> 推送示例
    
    
    {
        "arg": {
            "channel": "estimated-price",
            "instType": "FUTURES",
            "instFamily": "XRP-USDT"
        },
        "data": [{
            "instId": "XRP-USDT-250307",
            "instType": "FUTURES",
            "settlePx": "2.4230631578947368",
            "settleType": "settlement",
            "ts": "1741244598708"
        }]
    }
    

#### 推送数据参数

**参数名** | **类型** | **描述**  
---|---|---  
arg | Object | 订阅成功的频道  
> channel | String | 频道名  
> instType | String | 产品类型  
`FUTURES`：交割  
`OPTION`：期权  
`SWAP`：永续  
`EVENTS`：事件合约  
> instFamily | String | 交易品种  
> instId | String | 产品ID  
data | Array of objects | 订阅的数据  
> instType | String | 产品类型  
> instId | String | 产品ID，如 `BTC-USD-170310`  
> settleType | String | 类型  
`settlement`：结算  
`delivery`：交割  
`exercise`：行权  
> settlePx | String | 预估价  
> ts | String | 数据更新时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
  
### 标记价格频道 

获取标记价格，标记价格有变化时，每200ms推送一次数据，标记价格没变化时，每10s推送一次数据

#### URL Path

/ws/v5/public

> 请求示例
    
    
    {
      "id": "1512",
        "op": "subscribe",
        "args": [{
            "channel": "mark-price",
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
            "channel": "mark-price",
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
`mark-price`  
> instId | String | 是 | 产品ID  
  
> 成功返回示例
    
    
    {
      "id": "1512",
        "event": "subscribe",
        "arg": {
            "channel": "mark-price",
            "instId": "BTC-USDT"
        },
        "connId": "a4d3ae55"
    }
    

> 失败返回示例
    
    
    {
      "id": "1512",
        "event": "error",
        "code": "60012",
        "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{ \"channel\" : \"mark-price\", \"instId\" : \"LTC-USD-190628\"}]}",
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
> instId | String | 否 | 产品ID  
code | String | 否 | 错误码  
msg | String | 否 | 错误消息  
connId | String | 是 | WebSocket连接ID  
  
> 推送示例
    
    
    {
      "arg": {
        "channel": "mark-price",
        "instId": "BTC-USDT"
      },
      "data": [
        {
          "instType": "MARGIN",
          "instId": "BTC-USDT",
          "markPx": "42310.6",
          "ts": "1630049139746"
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
> instType | String | 交易品种  
> instId | String | 产品ID  
> markPx | String | 标记价格  
> ts | String | 标记价格数据更新时间 ，Unix时间戳的毫秒数格式，如 `1597026383085`  
在极少数情况下，客户端可能在短时间内收到两条时间戳相同的标记价格消息。这可能发生在系统维护或服务发布期间，且不会持续出现。当出现此情况时，客户端应以后收到的消息作为权威值。两条消息的差值可忽略不计，不会对交易策略产生实质性影响。 

### 指数行情频道 

获取指数的行情数据。每100ms有变化就推送一次数据，否则一分钟推一次。

#### URL Path

/ws/v5/public

> 请求示例
    
    
    {
        "id": "1512",
        "op": "subscribe",
        "args": [{
            "channel": "index-tickers",
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
              "channel": "index-tickers",
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
op | String | 是 | `subscribe` `unsubscribe`  
args | Array of objects | 是 | 请求订阅的频道列表  
> channel | String | 是 | 频道名  
`index-tickers`  
> instId | String | 是 | 指数，以USD、USDT、BTC、USDC 为计价货币的指数，如 `BTC-USDT`  
与 `uly` 含义相同。  
  
> 成功返回示例
    
    
    {
        "id": "1512",
        "event": "subscribe",
        "arg": {
            "channel": "index-tickers",
            "instId": "BTC-USDT"
        },
        "connId": "a4d3ae55"
    }
    

> 失败返回示例
    
    
    {
        "id": "1512",
        "event": "error",
        "code": "60012",
        "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{ \"channel\" : \"index-tickers\", \"instId\" : \"BTC-USDT\"}]}",
        "connId": "a4d3ae55"
    }
    

#### 返回参数

参数 | 类型 | 是否必须 | 描述  
---|---|---|---  
id | String | 否 | 消息的唯一标识  
event | String | 是 | `subscribe` `unsubscribe` `error`  
arg | Object | 否 | 订阅的频道  
> channel | String | 是 | 频道名  
`index-tickers`  
> instId | String | 是 | 指数，以USD、USDT、BTC、USDC 为计价货币的指数，如 `BTC-USDT`  
code | String | 否 | 错误码  
msg | String | 否 | 错误消息  
connId | String | 是 | WebSocket连接ID  
  
> 推送示例
    
    
    {
        "arg": {
            "channel": "index-tickers",
            "instId": "BTC-USDT"
        },
        "data": [{
            "instId": "BTC-USDT",
            "idxPx": "0.1",
            "high24h": "0.5",
            "low24h": "0.1",
            "open24h": "0.1",
            "sodUtc0": "0.1",
            "sodUtc8": "0.1",
            "ts": "1597026383085"
        }]
    }
    

#### 推送数据参数

参数名 | 类型 | 描述  
---|---|---  
arg | Object | 订阅成功的频道  
> channel | String | 频道名  
> instId | String | 指数  
data | Array of objects | 订阅的数据  
> instId | String | 指数，以USD、USDT、BTC 为计价货币的指数，如 `BTC-USDT`  
> idxPx | String | 最新指数价格  
> open24h | String | 24小时开盘价  
> high24h | String | 24小时指数最高价格  
> low24h | String | 24小时指数最低价格  
> sodUtc0 | String | UTC 0 时开盘价  
> sodUtc8 | String | UTC+8 时开盘价  
> ts | String | 指数价格更新时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
  
### 标记价格K线频道 

获取标记价格的K线数据，推送频率最快是间隔1秒推送一次数据。

#### URL Path

/ws/v5/business

> 请求示例
    
    
    {
        "id": "1512",
        "op": "subscribe",
        "args": [{
            "channel": "mark-price-candle1D",
            "instId": "BTC-USD-190628"
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
              "channel": "mark-price-candle1D",
              "instId": "BTC-USD-190628"
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
`mark-price-candle3M`   
`mark-price-candle1M`   
`mark-price-candle1W`   
`mark-price-candle1D`  
`mark-price-candle2D`  
`mark-price-candle3D`   
`mark-price-candle5D`  
`mark-price-candle12H`   
`mark-price-candle6H`   
`mark-price-candle4H`  
`mark-price-candle2H`  
`mark-price-candle1H`   
`mark-price-candle30m`  
`mark-price-candle15m`   
`mark-price-candle5m`   
`mark-price-candle3m`   
`mark-price-candle1m`   
`mark-price-candle3Mutc`  
`mark-price-candle1Mutc`   
`mark-price-candle1Wutc`  
`mark-price-candle1Dutc`  
`mark-price-candle2Dutc`  
`mark-price-candle3Dutc`  
`mark-price-candle5Dutc`   
`mark-price-candle12Hutc`  
`mark-price-candle6Hutc`  
> instId | String | 是 | 产品ID  
  
> 成功返回示例
    
    
    {
        "id": "1512",
        "event": "subscribe",
        "arg": {
            "channel": "mark-price-candle1D",
            "instId": "BTC-USD-190628"
        },
        "connId": "a4d3ae55"
    }
    
    

> 失败返回示例
    
    
    {
        "id": "1512",
        "event": "error",
        "code": "60012",
        "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{ \"channel\" : \"mark-price-candle1D\", \"instId\" : \"BTC-USD-190628\"}]}",
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
            "channel": "mark-price-candle1D",
            "instId": "BTC-USD-190628"
        },
        "data": [
            ["1597026383085", "3.721", "3.743", "3.677", "3.708", "0"],
            ["1597026383085", "3.731", "3.799", "3.494", "3.72", "1"]
        ]
    }
    

#### 推送数据参数

参数名 | 类型 | 描述  
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
> confirm | String | K线状态   
`0` 代表 K 线未完结，`1` 代表 K 线已完结。  
  
### 指数K线频道 

获取指数的K线数据，推送频率最快是间隔1秒推送一次数据。

#### URL Path

/ws/v5/business

> 请求示例
    
    
    {
        "id": "1512",
        "op": "subscribe",
        "args": [{
            "channel": "index-candle30m",
            "instId": "BTC-USD"
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
              "channel": "index-candle30m",
              "instId": "BTC-USD"
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
`index-candle3M`  
`index-candle1M`  
`index-candle1W`  
`index-candle1D`  
`index-candle2D`  
`index-candle3D`  
`index-candle5D`  
`index-candle12H`  
`index-candle6H`  
`index-candle4H`  
`index -candle2H`  
`index-candle1H`  
`index-candle30m`  
`index-candle15m`  
`index-candle5m`  
`index-candle3m`  
`index-candle1m`  
`index-candle3Mutc`   
`index-candle1Mutc`  
`index-candle1Wutc`  
`index-candle1Dutc`  
`index-candle2Dutc`  
`index-candle3Dutc`  
`index-candle5Dutc`  
`index-candle12Hutc`  
`index-candle6Hutc`  
> instId | String | 是 | 现货指数，如 `BTC-USD`  
与 `uly` 含义相同。  
  
> 成功返回示例
    
    
    {
        "id": "1512",
        "event": "subscribe",
        "arg": {
            "channel": "index-candle30m",
            "instId": "BTC-USD"
        },
        "connId": "a4d3ae55"
    }
    

> 失败返回示例
    
    
    {
        "id": "1512",
        "event": "error",
        "code": "60012",
        "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{ \"channel\" : \"index-candle30m\", \"instId\" : \"BTC-USD\"}]}",
        "connId": "a4d3ae55"
    }
    

#### 返回参数

参数 | 类型 | 是否必须 | 描述  
---|---|---|---  
id | String | 否 | 消息的唯一标识  
event | String | 是 | `subscribe` `unsubscribe`  
arg | Object | 否 | 订阅的频道  
> channel | String | 是 | 频道名  
> instId | String | 否 | 现货指数  
code | String | 否 | 错误码  
msg | String | 否 | 错误消息  
connId | String | 是 | WebSocket连接ID  
  
> 推送示例
    
    
    {
        "arg": {
            "channel": "index-candle30m",
            "instId": "BTC-USD"
        },
        "data": [
            ["1597026383085", "3811.31", "3811.31", "3811.31", "3811.31","0"]
        ]
    }
    

#### 推送数据参数

参数名 | 类型 | 描述  
---|---|---  
arg | Object | 订阅成功的频道  
> channel | String | 频道名  
> instId | String | 现货指数  
data | Array of Arrays | 订阅的数据  
> ts | String | 开始时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
> o | String | 开盘价格  
> h | String | 最高价格  
> l | String | 最低价格  
> c | String | 收盘价格  
> confirm | String | K线状态   
`0` 代表 K 线未完结，`1` 代表 K 线已完结。  
返回值数组顺分别为是：[ts,o,h,l,c,confirm] 

### 平台公共爆仓单频道

获取爆仓单信息。显示的强平数据并不准确代表欧易的总强平量，亦不应被当做总强平量使用。

#### URL Path

/ws/v5/public

> 请求示例
    
    
    {
      "id": "1512",
      "op": "subscribe",
      "args": [
        {
          "channel": "liquidation-orders",
          "instType": "SWAP"
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
              "channel": "liquidation-orders",
              "instType": "SWAP"
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
args | Array of objects | 是 | 请求订阅的频道  
> channel | String | 是 | 频道名  
`liquidation-orders`  
> instType | String | 是 | 产品类型  
`MARGIN`：币币杠杆  
`SWAP`：永续合约  
`FUTURES`：交割合约  
`OPTION`：期权  
  
> 返回结果
    
    
    {
      "id": "1512",
        "arg": {
            "channel": "liquidation-orders",
            "instType": "SWAP"
        },
        "data": [
            {
                "details": [
                    {
                        "bkLoss": "0",
                        "bkPx": "0.007831",
                        "ccy": "",
                        "posSide": "short",
                        "side": "buy",
                        "sz": "13",
                        "ts": "1692266434010"
                    }
                ],
                "instFamily": "IOST-USDT",
                "instId": "IOST-USDT-SWAP",
                "instType": "SWAP",
                "uly": "IOST-USDT"
            }
        ]
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
id | String | 消息的唯一标识  
arg | Object | 订阅成功的频道  
> channel | String | 频道名  
> instType | String | 产品类型  
data | Array of objects | 订阅的数据  
> instType | String | 产品类型  
> instId | String | 产品ID，如 `BTC-USD-SWAP`  
> uly | String | 标的指数  
适用于`交割`/`永续`/`期权`  
> details | Array of objects | 详细内容  
>> side | String | 订单方向  
`buy`：买  
`sell`：卖  
仅适用于`交割`/`永续`  
>> posSide | String | 持仓模式方向  
`long`：开平仓模式开多  
`short`：开平仓模式开空  
`net`：买卖模式  
>> bkPx | String | 强平标记价格，与系统爆仓账号委托成交的价格，仅适用于`交割/永续`  
>> sz | String | 强平数量  
适用于`杠杆`/`交割`/`永续`  
对于`杠杆`，单位为交易货币。  
对于`交割/永续`，单位为张。  
>> bkLoss | String | 穿仓亏损数量  
>> ccy | String | 强平币种  
适用于`币币杠杆`  
>> ts | String | 强平发生的时间，Unix时间戳的毫秒数格式，如 `1597026383085` /  
爆仓数据来自不同的数据源，因此推送的数据在时间上不一定是顺序的。 

### 自动减仓预警频道 

自动减仓预警。

仅在 `warning` 或 `adl` 状态下推送数据，每1秒推送一次，展示风险保证金余额及相关风险信息。`normal` 状态下不再推送数据。

更多自动减仓细节，请见[自动减仓机制介绍](https://www.okx.com/cn/help/iv-introduction-to-auto-deleveraging-adl)

#### 服务地址

/ws/v5/public

> 请求示例
    
    
    {
       "id": "1512",
        "op": "subscribe",
        "args": [{
            "channel": "adl-warning",
            "instType": "FUTURES",
            "instFamily": "BTC-USDT"
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
            "channel": "adl-warning",
            "instType": "FUTURES",
            "instFamily": "BTC-USDT"
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
`adl-warning`  
> instType | String | 是 | 产品类型  
`FUTURES`：交割合约  
`SWAP`：永续合约  
`OPTION`：期权  
> instFamily | String | 否 | 交易品种  
  
> 成功返回示例
    
    
    {
       "id": "1512",
       "event":"subscribe",
       "arg":{
          "channel":"adl-warning",
          "instType":"FUTURES",
          "instFamily":"BTC-USDT"
       },
       "connId":"48d8960a"
    }
    
    

> 失败返回示例
    
    
    {
       "id": "1512",
       "event":"error",
       "msg":"Illegal request: { \"event\": \"subscribe\", \"arg\": { \"channel\": \"adl-warning\", \"instType\": \"FUTURES\", \"instFamily\": \"BTC-USDT\" } }",
       "code":"60012",
       "connId":"48d8960a"
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
`adl-warning`  
> instType | String | 是 | 产品类型  
> instFamily | String | 否 | 交易品种  
code | String | 否 | 错误码  
msg | String | 否 | 错误消息  
connId | String | 是 | WebSocket连接ID  
  
> 推送示例
    
    
    {
       "arg":{
          "channel":"adl-warning",
          "instType":"FUTURES",
          "instFamily":"BTC-USDT"
       },
       "data":[
          {
             "instType":"FUTURES",
             "instFamily":"BTC-USDT",
             "state":"warning",
             "bal":"280784384.9564228289548144",
             "ccy":"",
             "maxBal":"",
             "maxBalTs":"",
             "adlType":"",
             "adlBal":"",
             "adlRecBal":"",
             "ts":"1700210763001",
             "decRate":"",
             "adlRate":"",
             "adlRecRate":""
          }
       ]
    }
    
    

#### 推送数据参数

参数名 | 类型 | 描述  
---|---|---  
arg | Object | 请求订阅的频道  
> channel | String | 频道名  
`adl-warning`  
> instType | String | 产品类型  
> instFamily | String | 交易品种  
data | Array of objects | 订阅的数据  
> instType | String | 产品类型  
> instFamily | String | 交易品种  
> state | String | 状态   
`warning`：预警状态   
`adl`：已开启自动减仓  
> bal | String | 实时风险保证金余额  
> ccy | String | ~~风险保证金余额对应币种~~ （已弃用，返回 `""`。将在后续更新中删除）  
> maxBal | String | ~~过去八小时内的风险保证金余额最大值  
仅在状态为`warning`及`adl`时推送，状态为`normal`时推送空字符串""~~（已弃用，返回 `""`。将在后续更新中删除）  
> maxBalTs | String | ~~过去八小时内风险保证金余额最大值对应的时间戳，Unix时间戳的毫秒数格式，如`1597026383085`~~（已弃用，返回 `""`。将在后续更新中删除）  
> adlType | String | ~~关于自动减仓的事件  
`rate_adl_start`：由于风险保证金下降率过高造成的自动减仓开始   
`bal_adl_start`：由于风险保证金余额下降过高造成的自动减仓开始   
`pos_adl_start`：由于强平单的规模积累到一定程度的自动减仓开始（仅适用于盘前交易市场）   
`adl_end`：自动减仓结束~~（已弃用，返回 `""`。将在后续更新中删除）  
> adlBal | String | ~~触发自动减仓的风险保证金余额~~ （已弃用，返回 `""`。将在后续更新中删除）  
> adlRecBal | String | ~~自动减仓结束的风险保证金余额~~ （已弃用，返回 `""`。将在后续更新中删除）  
> ts | String | 数据更新时间，Unix时间戳的毫秒数格式，如 1597026383085  
> decRate | String | ~~风险保证金实时下降率（bal与maxBal相比较）  
仅在状态为`warning`及`adl`时推送，状态为`normal`时推送空字符串""~~（已弃用）  
> adlRate | String | ~~触发自动减仓的风险保证金下降率~~ （已弃用）  
> adlRecRate | String | ~~自动减仓结束的风险保证金下降率~~ （已弃用）  
  
### 经济日历频道 

仅支持实盘服务 

获取最新经济日历数据。 该频道仅开放给交易费等级VIP1及以上的用户。

#### 服务地址

/ws/v5/business (需要登录)

> 请求示例
    
    
    {
        "id": "1512"  
        "op": "subscribe",
        "args": [
          {
              "channel": "economic-calendar"
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
              "channel": "economic-calendar"
          }
        ]
    
        await ws.subscribe(args, callback=callbackFunc)
        await asyncio.sleep(10)
    
        await ws.unsubscribe(args, callback=callbackFunc)
        await asyncio.sleep(10)
    
    
    asyncio.run(main())
    
    

#### 请求参数

参数名 | 类型 | 是否必填 | 描述  
---|---|---|---  
id | String | 否 | 消息的唯一标识。  
用户提供，返回参数中会返回以便于找到相应的请求。  
字母（区分大小写）与数字的组合，可以是纯字母、纯数字且长度必须要在1-32位之间。  
op | String | 是 | 操作  
`subscribe`  
`unsubscribe`  
  
args | Array of objects | 是 | 请求订阅的频道列表  
> channel | String | 是 | 频道名  
`economic-calendar`  
  
> 成功返回示例
    
    
    {
        "id": "1512",
        "event": "subscribe",
        "arg": {
            "channel": "economic-calendar"
        },
        "connId": "a4d3ae55"
    }
    
    

> 失败返回示例
    
    
    {
      "id": "1512",
      "event": "error",
      "code": "60012",
      "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{ \"channel\" : \"economic-calendar\", \"instId\" : \"LTC-USD-190628\"}]}",
      "connId": "a4d3ae55"
    }
    
    

#### 返回参数

参数名 | 类型 | 是否必填 | 描述  
---|---|---|---  
id | String | 否 | 消息的唯一标识  
event | String | 是 | 操作  
`subscribe`  
`unsubscribe`  
`error`  
arg | Object | 否 | 订阅的频道  
> channel | String | 是 | 频道名  
`economic-calendar`  
code | String | 否 | 错误码  
msg | String | 否 | 错误消息  
connId | String | 是 | WebSocket连接ID  
  
> 推送示例
    
    
    {
        "arg": {
            "channel": "economic-calendar"
        },
        "data": [
            {
                "calendarId": "319275",
                "date": "1597026383085",
                "region": "United States",
                "category": "Manufacturing PMI",
                "event": "S&P Global Manufacturing PMI Final",
                "refDate": "1597026383085",
                "actual": "49.2",
                "previous": "47.3",
                "forecast": "49.3",
                "importance": "2",
                "prevInitial": "",
                "ccy": "",
                "unit": "",
                "ts": "1698648096590"
            }
        ]
    }
    

#### 推送数据参数

**参数名** | **类型** | **描述**  
---|---|---  
arg | Object | 订阅成功的频道  
> channel | String | 频道名  
data | Array of objects | 订阅的数据  
> event | string | 事件名  
> region | string | 国家，地区或实体  
> category | string | 类别名  
> actual | string | 事件实际值  
> previous | string | 当前事件上个周期的最新实际值   
若发生数据修正，该字段存储上个周期修正后的实际值  
> forecast | string | 由权威经济学家共同得出的预测值  
> prevInitial | string | 该事件上一周期的初始值   
仅在修正发生时有值  
> date | string | actual字段值的预期发布时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
> refDate | string | 当前事件指向的日期  
> calendarId | string | 经济日历ID  
> unit | string | 事件实际值对应的单位  
> ccy | string | 事件实际值对应的货币  
> importance | string | 重要性   
`1`: 低   
`2`: 中等   
`3`: 高  
> ts | string | 推送时间