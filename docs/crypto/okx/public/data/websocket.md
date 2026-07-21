---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#public-data-websocket
anchor_id: public-data-websocket
api_type: WebSocket
updated_at: 2026-07-21 19:27:05.683492
---

# WebSocket

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
`3`: Spot TRY  
`5`: Spot BRL  
`7`: Spot AED  
`8`: Spot AUD  
`10`: Spot SGD  
`11`: Spot zero  
`12`: Spot group one  
`13`: Spot group two  
`14`: Spot group three  
`15`: Spot special rule  
`17`: Spot stablecoin  
`22`: Spot RWA group two  
  
Expiry futures:  
`5`: Expiry futures group one  
`6`: Expiry futures group two  
`8`: XPERP group two  
`10`: XPERP RWA group two  
  
Perpetual futures:  
`4`: Perpetual futures group one  
`5`: Perpetual futures group two  
`6`: SWAP RWA group one  
`7`: SWAP RWA group two  
  
Options:  
`1`: Options crypto-margined  
  
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
> preMktSwTime | String | The time a pre-market instrument switched to normal trading, Unix timestamp format in milliseconds, e.g. `1597026383085`.   
Only applicable to pre-market `SWAP` and pre-market X-Perp `FUTURES`. Populated when a pre-market X-Perp converts to a normal X-Perp  
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
`pre_market`: pre-market trading, including pre-market X-Perp `FUTURES`  
`rebase_contract`: pre-market rebase contract  
`xperp`: perpetual-style futures, only applicable to certain `FUTURES` contracts. A pre-market X-Perp changes from `pre_market` to `xperp` after it converts to a normal X-Perp  
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

# WebSocket

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
`3`：TRY现货  
`5`：BRL现货  
`7`：AED现货  
`8`：AUD现货  
`10`：SGD现货  
`11`：零手续费现货  
`12`：现货分组一  
`13`：现货分组二  
`14`：现货分组三  
`15`: 现货特别分组  
`17`：现货稳定币分组  
`22`：现货RWA分组二  
  
交割合约：  
`5`：交割合约分组一  
`6`：交割合约分组二  
`8`：XPERP分组二  
`10`：XPERP RWA分组二  
  
永续合约：  
`4`：永续合约分组一  
`5`：永续合约分组二  
`6`：SWAP RWA分组一  
`7`：SWAP RWA分组二  
  
期权：  
`1`：币本位期权  
  
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
> preMktSwTime | String | 盘前交易产品切换为正常交易的时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
仅适用于盘前`SWAP` 与盘前 X-Perp `FUTURES`。当盘前 X-Perp 转换为正常 X-Perp 时填充  
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
`pre_market`：盘前交易，含盘前 X-Perp `FUTURES`  
`rebase_contract`：盘前变基合约  
`xperp`：永续合约风格的交割合约，仅适用于部分 `FUTURES` 合约。盘前 X-Perp 转换为正常 X-Perp 后，由 `pre_market` 变为 `xperp`  
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