---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#trading-account-websocket
anchor_id: trading-account-websocket
api_type: WebSocket
updated_at: 2026-07-03 19:39:00.899826
---

# WebSocket

### Account channel  
  
Retrieve account information. Data will be pushed when triggered by events such as placing order, canceling order, transaction execution, etc. It will also be pushed in regular interval according to subscription granularity.  

Concurrent connection to this channel will be restricted by the following rules: [WebSocket connection count limit](/docs-v5/en/#overview-websocket-connection-count-limit).

#### URL Path

/ws/v5/private (required login)

> Request Example : single
    
    
    {
      "id": "1512",
      "op": "subscribe",
      "args": [
        {
          "channel": "account",
          "ccy": "BTC"
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
            url = "wss://ws.okx.com:8443/ws/v5/private",
            useServerTime=False
        )
        await ws.start()
        args = [
            {
              "channel": "account",
              "ccy": "BTC"
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
          "channel": "account",
          "extraParams": "
            {
              \"updateInterval\": \"0\"
            }
          "
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
            url = "wss://ws.okx.com:8443/ws/v5/private",
            useServerTime=False
        )
        await ws.start()
        args = [
            {
              "channel": "account",
              "extraParams": "{\"updateInterval\": \"0\"}"
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
`account`  
> ccy | String | No | Currency  
> extraParams | String | No | Additional configuration  
>> updateInterval | int | No | `0`: only push due to account events   
The data will be pushed both by events and regularly if this field is omitted or set to other values than 0.   
The following format should be strictly obeyed when using this field.   
"extraParams": "  
{  
\"updateInterval\": \"0\"  
}  
"  
  
> Successful Response Example : single
    
    
    {
      "id": "1512",
      "event": "subscribe",
      "arg": {
        "channel": "account",
        "ccy": "BTC"
      },
      "connId": "a4d3ae55"
    }
    

> Successful Response Example
    
    
    {
      "id": "1512",
      "event": "subscribe",
      "arg": {
        "channel": "account"
      },
      "connId": "a4d3ae55"
    }
    

> Failure Response Example
    
    
    {
      "id": "1512",
      "event": "error",
      "code": "60012",
      "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{ \"channel\" : \"account\", \"ccy\" : \"BTC\"}]}",
      "connId": "a4d3ae55"
    }
    

#### Response parameters

Parameter | Type | Required | Description  
---|---|---|---  
id | String | No | Unique identifier of the message  
event | String | Yes | Operation  
`subscribe`  
`unsubscribe`  
`error`  
arg | Object | No | Subscribed channel  
> channel | String | Yes | Channel name  
`account`  
> ccy | String | No | Currency  
code | String | No | Error code  
msg | String | No | Error message  
connId | String | Yes | WebSocket connection ID  
  
> Push Data Example
    
    
    {
        "arg": {
            "channel": "account",
            "uid": "44*********584"
        },
        "eventType": "snapshot",
        "curPage": 1,
        "lastPage": true,
        "data": [{
            "adjEq": "55444.12216906034",
        "availEq": "55444.12216906034",
            "borrowFroz": "0",
        "delta": "0",
        "deltaLever": "0",
        "deltaNeutralStatus": "0",
            "details": [{
            "availBal": "4734.371190691436",
            "availEq": "4734.371190691435",
            "borrowFroz": "0",
            "cashBal": "4750.426970691436",
            "ccy": "USDT",
            "coinUsdPrice": "0.99927",
            "crossLiab": "0",
            "colRes": "0",
            "collateralEnabled": false,
            "collateralRestrict": false, // Deprecated, use colRes instead
            "colBorrAutoConversion": "0",
            "disEq": "4889.379316336831",
            "eq": "4892.951170691435",
            "eqUsd": "4889.379316336831",
            "smtSyncEq": "0",
            "spotCopyTradingEq": "0",
            "fixedBal": "0",
            "frozenBal": "158.57998",
            "frpType": "0",
            "imr": "",
            "interest": "0",
            "isoEq": "0",
            "isoLiab": "0",
            "isoUpl": "0",
            "liab": "0",
            "maxLoan": "0",
            "mgnRatio": "",
            "mmr": "",
            "notionalLever": "",
            "ordFrozen": "0",
            "rewardBal": "0",
            "spotInUseAmt": "",
            "clSpotInUseAmt": "",
            "maxSpotInUseAmt": "",          
            "spotIsoBal": "0",
            "stgyEq": "150",
            "twap": "0",
            "uTime": "1705564213903",
            "upl": "-7.475800000000003",
            "uplLiab": "0",
            "spotBal": "",
            "openAvgPx": "",
            "accAvgPx": "",
            "spotUpl": "",
            "spotUplRatio": "",
            "totalPnl": "",
            "totalPnlRatio": ""
            }],
            "imr": "0",
            "isoEq": "0",
            "mgnRatio": "",
            "mmr": "0",
            "notionalUsd": "0",
            "notionalUsdForBorrow": "0",
            "notionalUsdForFutures": "0",
            "notionalUsdForOption": "0",
            "notionalUsdForSwap": "0",
            "ordFroz": "0",
            "totalEq": "55868.06403501676",
            "uTime": "1705564223311",
            "upl": "0"
        }]
    }
    

#### Push data parameters

**Parameters** | **Types** | **Description**  
---|---|---  
arg | Object | Successfully subscribed channel  
> channel | String | Channel name  
> uid | String | User Identifier  
eventType | String | Event type:   
`snapshot`: Initial and regular snapshot push   
`event_update`: Event-driven update push  
curPage | Integer | Current page number.   
Only applicable for `snapshot` events. Not included in `event_update` events.  
lastPage | Boolean | Whether this is the last page of pagination:  
`true`  
`false`  
Only applicable for `snapshot` events. Not included in `event_update` events.  
data | Array of objects | Subscribed data  
> uTime | String | The latest time to get account information, millisecond format of Unix timestamp, e.g. `1597026383085`  
> totalEq | String | The total amount of equity in `USD`  
> isoEq | String | Isolated margin equity in `USD`  
Applicable to `Futures mode`/`Multi-currency margin`/`Portfolio margin`  
> adjEq | String | Adjusted / Effective equity in `USD`   
The net fiat value of the assets in the account that can provide margins for spot, expiry futures, perpetual futures and options under the cross-margin mode.   
In multi-ccy or PM mode, the asset and margin requirement will all be converted to USD value to process the order check or liquidation.   
Due to the volatility of each currency market, our platform calculates the actual USD value of each currency based on discount rates to balance market risks.   
Applicable to `Spot mode`/`Multi-currency margin`/`Portfolio margin`  
> availEq | String | Account level available equity, excluding currencies that are restricted due to the collateralized borrowing limit.  
Applicable to `Multi-currency margin`/`Portfolio margin`  
> ordFroz | String | Margin frozen for pending cross orders in `USD`   
Only applicable to `Spot mode`/`Multi-currency margin`/`Portfolio margin`  
> imr | String | Initial margin requirement in `USD`   
The sum of initial margins of all open positions and pending orders under cross-margin mode in `USD`.   
Applicable to `Spot mode`/`Multi-currency margin`/`Portfolio margin`  
> mmr | String | Maintenance margin requirement in `USD`   
The sum of maintenance margins of all open positions and pending orders under cross-margin mode in `USD`.   
Applicable to `Spot mode`/`Multi-currency margin`/`Portfolio margin`  
> borrowFroz | String | Potential borrowing IMR of the account in `USD`   
Only applicable to `Spot mode`/`Multi-currency margin`/`Portfolio margin`. It is "" for other margin modes.  
> mgnRatio | String | Maintenance margin ratio in `USD`.   
Applicable to `Spot mode`/`Multi-currency margin`/`Portfolio margin`  
> notionalUsd | String | Notional value of positions in `USD`   
Applicable to `Spot mode`/`Multi-currency margin`/`Portfolio margin`  
> notionalUsdForBorrow | String | Notional value for `Borrow` in USD  
Applicable to `Spot mode`/`Multi-currency margin`/`Portfolio margin`  
> notionalUsdForSwap | String | Notional value of positions for `Perpetual Futures` in USD  
Applicable to `Multi-currency margin`/`Portfolio margin`  
> notionalUsdForFutures | String | Notional value of positions for `Expiry Futures` in USD  
Applicable to `Multi-currency margin`/`Portfolio margin`  
> notionalUsdForOption | String | Notional value of positions for `Option` in USD  
Applicable to `Spot mode`/`Multi-currency margin`/`Portfolio margin`  
> upl | String | Cross-margin info of unrealized profit and loss at the account level in `USD`  
Applicable to `Multi-currency margin`/`Portfolio margin`  
> delta | String | Delta (USD)  
> deltaLever | String | Delta neutral strategy account level delta leverage  
deltaLever = delta / totalEq  
> deltaNeutralStatus | String | Delta risk status  
`0`: normal  
`1`: transfer restricted  
`2`: delta reducing - cancel all pending orders if delta is greater than 5000 USD, only one delta reducing order allowed per index (spot, futures, swap)  
> details | Array of objects | Detailed asset information in all currencies  
>> ccy | String | Currency  
>> eq | String | Equity of currency  
>> cashBal | String | Cash balance  
>> uTime | String | Update time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
>> isoEq | String | Isolated margin equity of currency  
Applicable to `Futures mode`/`Multi-currency margin`/`Portfolio margin`  
>> availEq | String | Available equity of currency  
Applicable to `Futures mode`/`Multi-currency margin`/`Portfolio margin`  
>> disEq | String | Discount equity of currency in `USD`.  
Applicable to `Spot mode`(enabled spot borrow)/`Multi-currency margin`/`Portfolio margin`  
>> fixedBal | String | Frozen balance for `Dip Sniper` and `Peak Sniper`  
>> availBal | String | Available balance of currency  
>> frozenBal | String | Frozen balance of currency  
>> ordFrozen | String | Margin frozen for open orders   
Applicable to `Spot mode`/`Futures mode`/`Multi-currency margin`  
>> liab | String | Liabilities of currency  
It is a positive value, e.g. `21625.64`.   
Applicable to `Spot mode`/`Multi-currency margin`/`Portfolio margin`  
>> upl | String | The sum of the unrealized profit & loss of all margin and derivatives positions of currency.   
Applicable to `Futures mode`/`Multi-currency margin`/`Portfolio margin`  
>> uplLiab | String | Liabilities due to Unrealized loss of currency  
Applicable to `Multi-currency margin`/`Portfolio margin`  
>> crossLiab | String | Cross liabilities of currency  
Applicable to `Spot mode`/`Multi-currency margin`/`Portfolio margin`  
>> isoLiab | String | Isolated liabilities of currency  
Applicable to `Multi-currency margin`/`Portfolio margin`  
>> rewardBal | String | Trial fund balance  
>> mgnRatio | String | Cross maintenance margin ratio of currency   
The index for measuring the risk of a certain asset in the account.   
Applicable to `Futures mode` and when there is cross position  
>> imr | String | Cross initial margin requirement at the currency level  
Applicable to `Futures mode` and when there is cross position  
>> mmr | String | Cross maintenance margin requirement at the currency level  
Applicable to `Futures mode` and when there is cross position  
>> interest | String | Interest of currency  
It is a positive value, e.g."9.01". Applicable to `Spot mode`/`Multi-currency margin`/`Portfolio margin`  
>> twap | String | Risk indicator of forced repayment  
Divided into multiple levels from 0 to 5, the larger the number, the more likely the forced repayment will be triggered.   
Applicable to `Spot mode`/`Multi-currency margin`/`Portfolio margin`  
>> frpType | String | Forced repayment (FRP) type  
`0`: no FRP  
`1`: user based FRP  
`2`: platform based FRP  
  
Return `1`/`2` when twap is >= 1, applicable to `Spot mode`/`Multi-currency margin`/`Portfolio margin`  
>> maxLoan | String | Maximum borrowable amount for the currency under the current account conditions. Affects the amount available for margin borrowing and transfers.  
Applicable to `cross` of `Spot mode`/`Multi-currency margin`/`Portfolio margin`  
>> eqUsd | String | Equity `USD` of currency  
>> borrowFroz | String | Potential borrowing IMR of currency in `USD`   
Only applicable to `Spot mode`/`Multi-currency margin`/`Portfolio margin`. It is "" for other margin modes.  
>> notionalLever | String | Leverage of currency  
Applicable to `Futures mode`  
>> coinUsdPrice | String | Price index `USD` of currency  
>> stgyEq | String | Total equity allocated to trading bots for the currency. Covers Spot Grid, Futures Grid, Signal Bot, Futures Martingale, Spot Martingale, Infinite Grid, and Recurring Buy strategies.  
>> isoUpl | String | Isolated unrealized profit and loss of currency  
Applicable to `Futures mode`/`Multi-currency margin`/`Portfolio margin`  
>> spotInUseAmt | String | Actual spot hedging amount in use for the currency.  
Applicable to `Portfolio margin`  
>> clSpotInUseAmt | String | User-defined spot hedging amount for the currency.  
Applicable to `Portfolio margin`  
>> maxSpotInUseAmt | String | System-calculated maximum possible spot hedging amount for the currency.  
Applicable to `Portfolio margin`  
>> spotIsoBal | String | Balance acquired through spot copy trading (as a follower or lead trader), including amounts currently frozen by open orders. For example, if 1 BTC was purchased via copy trading and 0.4 BTC is frozen in an open sell order, `spotIsoBal` returns `1`, not `0.6`.  
Applicable to copy trading. Applicable to `Spot mode`/`Futures mode`.  
>> smtSyncEq | String | Smart sync equity  
The default is "0", only applicable to copy trader.  
>> spotCopyTradingEq | String | Spot smart sync equity.   
The default is "0", only applicable to copy trader.  
>> spotBal | String | Spot balance. The unit is currency, e.g. BTC. [More details](https://www.okx.com/help/i-introduction-of-spot)  
>> openAvgPx | String | Spot average cost price. The unit is USD. [More details](https://www.okx.com/help/i-introduction-of-spot)  
>> accAvgPx | String | Spot accumulated cost price. The unit is USD. [More details](https://www.okx.com/help/i-introduction-of-spot)  
>> spotUpl | String | Spot unrealized profit and loss. The unit is USD. [More details](https://www.okx.com/help/i-introduction-of-spot)  
>> spotUplRatio | String | Spot unrealized profit and loss ratio. [More details](https://www.okx.com/help/i-introduction-of-spot)  
>> totalPnl | String | Spot accumulated profit and loss. The unit is USD. [More details](https://www.okx.com/help/i-introduction-of-spot)  
>> totalPnlRatio | String | Spot accumulated profit and loss ratio. [More details](https://www.okx.com/help/i-introduction-of-spot)  
>> colRes | String | Platform level collateral restriction status  
`0`: The restriction is not enabled.  
`1`: The restriction is not enabled. But the crypto is close to the platform's collateral limit.  
`2`: The restriction is enabled. This crypto can't be used as margin for your new orders. This may result in failed orders. But it will still be included in the account's adjusted equity and doesn't impact margin ratio.  
Refer to [Introduction to the platform collateralized borrowing limit](https://www.okx.com/help/introduction-to-the-platforms-collateralized-borrowing-limit-mechanism) for more details.  
>> colBorrAutoConversion | String | Risk indicator of auto conversion. Divided into multiple levels from 1-5, the larger the number, the more likely the repayment will be triggered. The default will be 0, indicating there is no risk currently. 5 means this user is undergoing auto conversion now, 4 means this user will undergo auto conversion soon whereas 1/2/3 indicates there is a risk for auto conversion.  
Applicable to `Spot mode`/`Futures mode`/`Multi-currency margin`/`Portfolio margin`  
When the total liability for each crypto set as collateral exceeds a certain percentage of the platform's total limit, the auto-conversion mechanism may be triggered. This may result in the automatic sale of excess collateral crypto if you've set this crypto as collateral and have large borrowings. To lower this risk, consider reducing your use of the crypto as collateral or reducing your liabilities.  
Refer to [Introduction to the platform collateralized borrowing limit](https://www.okx.com/help/introduction-to-the-platforms-collateralized-borrowing-limit-mechanism) for more details.  
>> collateralRestrict | Boolean | ~~Platform level collateralized borrow restriction  
`true`  
`false`~~(deprecated, use colRes instead)  
>> collateralEnabled | Boolean | `true`: Collateral enabled  
`false`: Collateral disabled  
Applicable to `Multi-currency margin`  
>> autoLendStatus | String | Auto lend status  
`unsupported`: auto lend is not supported by this currency  
`off`: auto lend is supported but turned off  
`pending`: auto lend is turned on but pending matching  
`active`: auto lend is turned on and matched  
>> autoLendMtAmt | String | Auto lend currency matched amount  
Return "0" when autoLendStatus is `unsupported/off/pending`. Return matched amount when autoLendStatus is `active`  
"" will be returned for inapplicable fields under the current account level.    
\- The account data is sent on event basis and regular basis.   
\- The event push is not pushed in real-time. It is aggregated and pushed at a fixed time interval, around 50ms. For example, if multiple events occur within a fixed time interval, the system will aggregate them into a single message and push it at the end of the fixed time interval. If the data volume is too large, it may be split into multiple messages.   
\- The regular push sends updates regardless of whether there are activities in the trading account or not.    
\- Only currencies with non-zero balance will be pushed. Definition of non-zero balance: any value of eq, availEq, availBal parameters is not 0. If the data is too large to be sent in a single push message, it will be split into multiple messages.   
\- For example, when subscribing to account channel without specifying ccy and there are 5 currencies are with non-zero balance, all 5 currencies data will be pushed in initial snapshot and in regular update. Subsequently when there is change in balance or equity of an token, only the incremental data of that currency will be pushed triggered by this change. 

### Positions channel

Retrieve position information. Initial snapshot will be pushed according to subscription granularity. Data will be pushed when triggered by events such as placing/canceling order, and will also be pushed in regular interval according to subscription granularity.  

Concurrent connection to this channel will be restricted by the following rules: [WebSocket connection count limit](/docs-v5/en/#overview-websocket-connection-count-limit).

#### URL Path

/ws/v5/private (required login)

> Request Example : single
    
    
    {
      "id": "1512",
      "op": "subscribe",
      "args": [
        {
          "channel": "positions",
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
            url = "wss://ws.okx.com:8443/ws/v5/private",
            useServerTime=False
        )
        await ws.start()
        args = [
            {
              "channel": "positions",
              "instType": "FUTURES",
              "instFamily": "BTC-USD"
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
          "channel": "positions",
          "instType": "ANY",
          "extraParams": "
            {
              \"updateInterval\": \"0\"
            }
          "
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
            url = "wss://ws.okx.com:8443/ws/v5/private",
            useServerTime=False
        )
        await ws.start()
        args = [
            {
                "channel": "positions",
                "instType": "ANY",
                "extraParams": "{\"updateInterval\": \"0\"}"
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
`positions`  
> instType | String | Yes | Instrument type  
`MARGIN`  
`SWAP`  
`FUTURES`  
`OPTION`   
`EVENTS`  
`ANY`  
> instFamily | String | No | Instrument family  
Applicable to `FUTURES`/`SWAP`/`OPTION`  
> instId | String | No | Instrument ID  
If instId and instFamily are both passed, instId will be used  
> extraParams | String | No | Additional configuration  
>> updateInterval | int | No | `0`: only push due to positions events   
`2000, 3000, 4000`: push by events and regularly according to the time interval setting (ms)   
  
The data will be pushed both by events and around per 5 seconds regularly if this field is omitted or set to other values than the valid values above.   
  
The following format should be strictly followed when using this field.   
"extraParams": "   
{   
\"updateInterval\": \"0\"   
}  
"  
  
> Successful Response Example : single
    
    
    {
      "id": "1512",
      "event": "subscribe",
      "arg": {
        "channel": "positions",
        "instType": "FUTURES",
        "instFamily": "BTC-USD"
      },
      "connId": "a4d3ae55"
    }
    

> Successful Response Example
    
    
    {
      "id": "1512",
      "event": "subscribe",
      "arg": {
        "channel": "positions",
        "instType": "ANY"
      },
      "connId": "a4d3ae55"
    }
    

> Failure Response Example
    
    
    {
      "id": "1512",
      "event": "error",
      "code": "60012",
      "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{ \"channel\" : \"positions\", \"instType\" : \"FUTURES\"}]}",
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
`MARGIN`  
`FUTURES`  
`SWAP`  
`OPTION`  
`EVENTS`  
`ANY`  
> instFamily | String | No | Instrument family  
> instId | String | No | Instrument ID  
code | String | No | Error code  
msg | String | No | Error message  
connId | String | Yes | WebSocket connection ID  
  
> Push Data Example: single
    
    
    {
      "arg":{
          "channel":"positions",
          "uid": "77982378738415879",
          "instType":"FUTURES"
      },
      "eventType": "snapshot",
      "curPage": 1,
      "lastPage": true,
      "data":[
        {
          "adl":"1",
          "availPos":"1",
          "avgPx":"2566.31",
          "cTime":"1619507758793",
          "ccy":"ETH",
          "deltaBS":"",
          "deltaPA":"",
          "gammaBS":"",
          "gammaPA":"",
          "hedgedPos":"",
          "imr":"",
          "instId":"ETH-USD-210430",
          "instType":"FUTURES",
          "interest":"0",
          "idxPx":"2566.13",
          "last":"2566.22",
          "lever":"10",
          "liab":"",
          "liabCcy":"",
          "liqPx":"2352.8496681818233",
          "markPx":"2353.849",
          "margin":"0.0003896645377994",
          "mgnMode":"isolated",
          "mgnRatio":"11.731726509588816",
          "mmr":"0.0000311811092368",
          "notionalUsd":"2276.2546609009605",
          "optVal":"",
          "pTime":"1619507761462",
          "pendingCloseOrdLiabVal":"0.1",
          "pos":"1",
          "baseBorrowed": "",
          "baseInterest": "",
          "quoteBorrowed": "",
          "quoteInterest": "",
          "posCcy":"",
          "posId":"307173036051017730",
          "posSide":"long",
          "spotInUseAmt": "",
          "clSpotInUseAmt": "",
          "maxSpotInUseAmt": "",
          "bizRefId": "",
          "bizRefType": "",
          "spotInUseCcy": "",
          "thetaBS":"",
          "thetaPA":"",
          "tradeId":"109844",
          "uTime":"1619507761462",
          "upl":"-0.0000009932766034",
          "uplLastPx":"-0.0000009932766034",
          "uplRatio":"-0.0025490556801078",
          "uplRatioLastPx":"-0.0025490556801078",
          "vegaBS":"",
          "vegaPA":"",
          "realizedPnl":"0.001",
          "pnl":"0.0011",
          "fee":"-0.0001",
          "fundingFee":"0",
          "liqPenalty":"0",
          "nonSettleAvgPx":"", 
          "settledPnl":"",
          "closeOrderAlgo":[
              {
                  "algoId":"123",
                  "slTriggerPx":"123",
                  "slTriggerPxType":"mark",
                  "tpTriggerPx":"123",
                  "tpTriggerPxType":"mark",
                  "closeFraction":"0.6"
              },
              {
                  "algoId":"123",
                  "slTriggerPx":"123",
                  "slTriggerPxType":"mark",
                  "tpTriggerPx":"123",
                  "tpTriggerPxType":"mark",
                  "closeFraction":"0.4"
              }
          ]
        }
      ]
    }
    

> Push Data Example
    
    
    {
      "arg":{
          "channel":"positions",
          "uid": "77982378738415879",
          "instType":"ANY"
      },
      "eventType": "snapshot",
      "curPage": 1,
      "lastPage": true,
      "data":[
        {
          "adl":"1",
          "availPos":"1",
          "avgPx":"2566.31",
          "cTime":"1619507758793",
          "ccy":"ETH",
          "deltaBS":"",
          "deltaPA":"",
          "gammaBS":"",
          "gammaPA":"",
          "hedgedPos":"",
          "imr":"",
          "instId":"ETH-USD-210430",
          "instType":"FUTURES",
          "interest":"0",
          "idxPx":"2566.13",
          "last":"2566.22",
          "usdPx":"",
          "bePx":"2353.949",
          "lever":"10",
          "liab":"",
          "liabCcy":"",
          "liqPx":"2352.8496681818233",
          "markPx":"2353.849",
          "margin":"0.0003896645377994",
          "mgnMode":"isolated",
          "mgnRatio":"11.731726509588816",
          "mmr":"0.0000311811092368",
          "notionalUsd":"2276.2546609009605",
          "optVal":"",
          "pTime":"1619507761462",
          "pendingCloseOrdLiabVal":"0.1",
          "pos":"1",
          "baseBorrowed": "",
          "baseInterest": "",
          "quoteBorrowed": "",
          "quoteInterest": "",
          "posCcy":"",
          "posId":"307173036051017730",
          "posSide":"long",
          "spotInUseAmt": "",
          "clSpotInUseAmt": "",
          "maxSpotInUseAmt": "",
          "spotInUseCcy": "",
          "bizRefId": "",
          "bizRefType": "",
          "thetaBS":"",
          "thetaPA":"",
          "tradeId":"109844",
          "uTime":"1619507761462",
          "upl":"-0.0000009932766034",
          "uplLastPx":"-0.0000009932766034",
          "uplRatio":"-0.0025490556801078",
          "uplRatioLastPx":"-0.0025490556801078",
          "vegaBS":"",
          "vegaPA":"",
          "realizedPnl":"0.001",
          "pnl":"0.0011",
          "fee":"-0.0001",
          "fundingFee":"0",
          "liqPenalty":"0",
          "nonSettleAvgPx":"", 
          "settledPnl":"",
          "closeOrderAlgo":[
              {
                  "algoId":"123",
                  "slTriggerPx":"123",
                  "slTriggerPxType":"mark",
                  "tpTriggerPx":"123",
                  "tpTriggerPxType":"mark",
                  "closeFraction":"0.6"
              },
              {
                  "algoId":"123",
                  "slTriggerPx":"123",
                  "slTriggerPxType":"mark",
                  "tpTriggerPx":"123",
                  "tpTriggerPxType":"mark",
                  "closeFraction":"0.4"
              }
          ]
        }, {
          "adl":"1",
          "availPos":"1",
          "avgPx":"2566.31",
          "cTime":"1619507758793",
          "ccy":"ETH",
          "deltaBS":"",
          "deltaPA":"",
          "gammaBS":"",
          "gammaPA":"",
          "hedgedPos":"",
          "imr":"",
          "instId":"ETH-USD-SWAP",
          "instType":"SWAP",
          "interest":"0",
          "idxPx":"2566.13",
          "last":"2566.22",
          "usdPx":"",
          "bePx":"2353.949",
          "lever":"10",
          "liab":"",
          "liabCcy":"",
          "liqPx":"2352.8496681818233",
          "markPx":"2353.849",
          "margin":"0.0003896645377994",
          "mgnMode":"isolated",
          "mgnRatio":"11.731726509588816",
          "mmr":"0.0000311811092368",
          "notionalUsd":"2276.2546609009605",
          "optVal":"",
          "pTime":"1619507761462",
          "pendingCloseOrdLiabVal":"0.1",
          "pos":"1",
          "baseBorrowed": "",
          "baseInterest": "",
          "quoteBorrowed": "",
          "quoteInterest": "",
          "posCcy":"",
          "posId":"307173036051017730",
          "posSide":"long",
          "spotInUseAmt": "",
          "clSpotInUseAmt": "",
          "maxSpotInUseAmt": "",
          "spotInUseCcy": "",
          "bizRefId": "",
          "bizRefType": "",
          "thetaBS":"",
          "thetaPA":"",
          "tradeId":"109844",
          "uTime":"1619507761462",
          "upl":"-0.0000009932766034",
          "uplLastPx":"-0.0000009932766034",
          "uplRatio":"-0.0025490556801078",
          "uplRatioLastPx":"-0.0025490556801078",
          "vegaBS":"",
          "vegaPA":"",
          "realizedPnl":"0.001",
          "pnl":"0.0011",
          "fee":"-0.0001",
          "fundingFee":"0",
          "liqPenalty":"0",
          "nonSettleAvgPx":"", 
          "settledPnl":"",
          "closeOrderAlgo":[
              {
                  "algoId":"123",
                  "slTriggerPx":"123",
                  "slTriggerPxType":"mark",
                  "tpTriggerPx":"123",
                  "tpTriggerPxType":"mark",
                  "closeFraction":"0.6"
              },
              {
                  "algoId":"123",
                  "slTriggerPx":"123",
                  "slTriggerPxType":"mark",
                  "tpTriggerPx":"123",
                  "tpTriggerPxType":"mark",
                  "closeFraction":"0.4"
              }
          ]
        }
      ]
    }
    

#### Push data parameters

Parameter | Type | Description  
---|---|---  
arg | Object | Successfully subscribed channel  
> channel | String | Channel name  
> uid | String | User Identifier  
> instType | String | Instrument type  
`MARGIN`  
`SWAP`  
`FUTURES`  
`OPTION`  
`EVENTS`  
> instFamily | String | Instrument family  
> instId | String | Instrument ID  
eventType | String | Event type:   
`snapshot`: Initial and regular snapshot push   
`event_update`: Event-driven update push  
curPage | Integer | Current page number.   
Only applicable for `snapshot` events. Not included in `event_update` events.  
lastPage | Boolean | Whether this is the last page of pagination:  
`true`  
`false`  
Only applicable for `snapshot` events. Not included in `event_update` events.  
data | Array of objects | Subscribed data  
> instType | String | Instrument type  
`MARGIN`  
`SWAP`  
`FUTURES`  
`OPTION`  
`EVENTS`  
> mgnMode | String | Margin mode, `cross` `isolated`  
> posId | String | Position ID  
> posSide | String | Position side  
`long`   
`short`   
`net` (`FUTURES`/`SWAP`/`OPTION`: positive `pos` means long position and negative `pos` means short position. `MARGIN`: `posCcy` being base currency means long position, `posCcy` being quote currency means short position.)  
> pos | String | Quantity of positions. In the isolated margin mode, when doing manual transfers, a position with pos of `0` will be generated after the deposit is transferred  
> hedgedPos | String | Hedged position size  
Only return for accounts in delta neutral strategy, stgyType:1. Return "" for accounts in general strategy.  
> baseBal | String | ~~Base currency balance, only applicable to`MARGIN`（Quick Margin Mode）~~(Deprecated)  
> quoteBal | String | ~~Quote currency balance, only applicable to`MARGIN`（Quick Margin Mode）~~(Deprecated)  
> baseBorrowed | String | ~~Base currency amount already borrowed, only applicable to MARGIN(Quick Margin Mode）~~(Deprecated)  
> baseInterest | String | ~~Base Interest, undeducted interest that has been incurred, only applicable to MARGIN(Quick Margin Mode）~~(Deprecated)  
> quoteBorrowed | String | ~~Quote currency amount already borrowed, only applicable to MARGIN(Quick Margin Mode）~~(Deprecated)  
> quoteInterest | String | ~~Quote Interest, undeducted interest that has been incurred, only applicable to MARGIN(Quick Margin Mode）~~(Deprecated)  
> posCcy | String | Position currency, only applicable to `MARGIN` positions  
> availPos | String | Position that can be closed   
Only applicable to `MARGIN` and `OPTION`.   
For `Margin` position, the rest of sz will be `SPOT` trading after the liability is repaid while closing the position. Please get the available reduce-only amount from "Get maximum available tradable amount" if you want to reduce the amount of `SPOT` trading as much as possible.  
> avgPx | String | Average open price  
> upl | String | Unrealized profit and loss calculated by mark price.  
> uplRatio | String | Unrealized profit and loss ratio calculated by mark price.  
> uplLastPx | String | Unrealized profit and loss calculated by last price. Main usage is showing, actual value is upl.  
> uplRatioLastPx | String | Unrealized profit and loss ratio calculated by last price.  
> instId | String | Instrument ID, e.g. `BTC-USDT-SWAP`  
> lever | String | Leverage, not applicable to `OPTION` seller  
> liqPx | String | Estimated liquidation price   
Not applicable to `OPTION`  
> markPx | String | Latest Mark price  
> imr | String | Initial margin requirement, only applicable to `cross`  
> margin | String | Margin, can be added or reduced. Only applicable to `isolated` `Margin`.  
> mgnRatio | String | Maintenance margin ratio  
> mmr | String | Maintenance margin requirement  
> liab | String | Liabilities, only applicable to `MARGIN`.  
> liabCcy | String | Liabilities currency, only applicable to `MARGIN`.  
> interest | String | Interest accrued that has not been settled.  
> tradeId | String | Last trade ID  
> notionalUsd | String | Notional value of positions in `USD`  
> optVal | String | Option Value, only applicable to `OPTION`.  
> pendingCloseOrdLiabVal | String | The amount of close orders of isolated margin liability.  
> adl | String | Automatic-Deleveraging, signal area  
Divided into 6 levels, from 0 to 5, the smaller the number, the weaker the adl intensity.   
Only applicable to `FUTURES/SWAP/OPTION`  
> bizRefId | String | External business id, e.g. experience coupon id  
> bizRefType | String | External business type  
> ccy | String | Currency used for margin  
> last | String | Latest traded price  
> idxPx | String | Latest underlying index price  
> usdPx | String | Latest USD price of the `ccy` on the market, only applicable to `FUTURES`/`SWAP`/`OPTION`  
> bePx | String | Breakeven price  
> deltaBS | String | delta: Black-Scholes Greeks in dollars, only applicable to `OPTION`  
> deltaPA | String | delta: Greeks in coins, only applicable to `OPTION`  
> gammaBS | String | gamma: Black-Scholes Greeks in dollars, only applicable to `OPTION`  
> gammaPA | String | gamma: Greeks in coins, only applicable to `OPTION`  
> thetaBS | String | theta: Black-Scholes Greeks in dollars, only applicable to `OPTION`  
> thetaPA | String | theta: Greeks in coins, only applicable to `OPTION`  
> vegaBS | String | vega: Black-Scholes Greeks in dollars, only applicable to `OPTION`  
> vegaPA | String | vega: Greeks in coins, only applicable to `OPTION`  
> spotInUseAmt | String | Spot in use amount  
Applicable to `Portfolio margin`  
> spotInUseCcy | String | Spot in use unit, e.g. `BTC`  
Applicable to `Portfolio margin`  
> clSpotInUseAmt | String | User-defined spot risk offset amount  
Applicable to `Portfolio margin`  
> maxSpotInUseAmt | String | Max possible spot risk offset amount  
Applicable to `Portfolio margin`  
> realizedPnl | String | Realized profit and loss  
Only applicable to `FUTURES`/`SWAP`/`OPTION`  
realizedPnl=pnl+fee+fundingFee+liqPenalty+settledPnl  
> pnl | String | Accumulated pnl of closing order(s) (excluding the fee).  
> fee | String | Accumulated fee  
Negative number represents the user transaction fee charged by the platform.Positive number represents rebate.  
> fundingFee | String | Accumulated funding fee  
> liqPenalty | String | Accumulated liquidation penalty. It is negative when there is a value.  
> closeOrderAlgo | Array of objects | Close position algo orders attached to the position. This array will have values only after you request "Place algo order" with `closeFraction`=1.  
>> algoId | String | Algo ID  
>> slTriggerPx | String | Stop-loss trigger price.  
>> slTriggerPxType | String | Stop-loss trigger price type.   
`last`: last price  
`index`: index price  
`mark`: mark price  
>> tpTriggerPx | String | Take-profit trigger price.  
>> tpTriggerPxType | String | Take-profit trigger price type.   
`last`: last price  
`index`: index price  
`mark`: mark price  
>> closeFraction | String | Fraction of position to be closed when the algo order is triggered.  
> cTime | String | Creation time, Unix timestamp format in milliseconds, e.g. `1597026383085`.  
> uTime | String | Latest time position was adjusted, Unix timestamp format in milliseconds, e.g. `1597026383085`.  
> pTime | String | Push time of positions information, Unix timestamp format in milliseconds, e.g. `1597026383085`.  
> nonSettleAvgPx | String | Non-Settlement entry price  
The non-settlement entry price only reflects the average price at which the position is opened or increased.  
Applicable to `FUTURES` `cross`  
> settledPnl | String | Accumulated settled P&L (calculated by settlement price)  
Applicable to `FUTURES` `cross`  
  
\- The position data is sent on event basis and regular basis   
\- The event push is not pushed in real-time. It is aggregated and pushed at a fixed time interval, around 50ms. For example, if multiple events occur within a fixed time interval, the system will aggregate them into a single message and push it at the end of the fixed time interval. If the data volume is too large, it may be split into multiple messages.   
\- The regular push sends updates regardless of whether there are position activities or not.   
\- If an event push and a regular push happen at the same time, the system will send the event push first, followed by the regular push.  As for portfolio margin account, the IMR and MMR of the position are calculated in risk unit granularity, thus their values of the same risk unit cross positions are the same.  In the position-by-position trading setting, it is an autonomous transfer mode. After the margin is transferred, positions with a position of 0 will be pushed    
\- Only position with non-zero position quantity will be pushed. Definition of non-zero quantity: value of pos parameter is not 0. If the data is too large to be sent in a single push message, it will be split into multiple messages.   
\- For example, when subscribing to positions channel specifying an underlying and there are 20 positions are with non-zero quantity, all 20 positions data will be pushed in initial snapshot and in regular push. Subsequently when there is change in pos of a position, only the data of that position will be pushed triggered by this change.  Unlike futures contracts, option positions are automatically exercised or expire at maturity. The rights then terminate and no closing orders are generated. Therefore, this channel will not push any updates for expired option positions. 

### Balance and position channel

Retrieve account balance and position information. Data will be pushed when triggered by events such as filled order, funding transfer.  
This channel applies to getting the account cash balance and the change of position asset ASAP.   
Concurrent connection to this channel will be restricted by the following rules: [WebSocket connection count limit](/docs-v5/en/#overview-websocket-connection-count-limit).

#### URL Path

/ws/v5/private (required login)

> Request Example 
    
    
    {
        "id": "1512",
        "op": "subscribe",
        "args": [{
            "channel": "balance_and_position"
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
            url = "wss://ws.okx.com:8443/ws/v5/private",
            useServerTime=False
        )
        await ws.start()
        args = [{
            "channel": "balance_and_position"
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
`balance_and_position`  
  
> Response Example 
    
    
    {
        "id": "1512",
        "event": "subscribe",
        "arg": {
            "channel": "balance_and_position"
        },
        "connId": "a4d3ae55"
    }
    

> Failure Response Example
    
    
    {
        "id": "1512",
        "event": "error",
        "code": "60012",
        "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{ \"channel\" : \"balance_and_position\"}]}",
        "connId": "a4d3ae55"
    }
    

#### Response parameters

Parameter | Type | Required | Description  
---|---|---|---  
id | String | No | Unique identifier of the message  
event | String | Yes | Operation  
`subscribe`  
`unsubscribe`  
`error`  
arg | Object | No | List of subscribed channels  
> channel | String | Yes | Channel name  
`balance_and_position`  
code | String | No | Error code  
msg | String | No | Error message  
connId | String | Yes | WebSocket connection ID  
  
> Push Data Example
    
    
    {
        "arg": {
            "channel": "balance_and_position",
            "uid": "77982378738415879"
        },
        "data": [{
            "pTime": "1597026383085",
            "eventType": "snapshot",
            "balData": [{
                "ccy": "BTC",
                "cashBal": "1",
                "uTime": "1597026383085"
            }],
            "posData": [{
                "posId": "1111111111",
                "tradeId": "2",
                "instId": "BTC-USD-191018",
                "instType": "FUTURES",
                "mgnMode": "cross",
                "posSide": "long",
                "pos": "10",
                "ccy": "BTC",
                "posCcy": "",
                "avgPx": "3320",
                "nonSettleAvgPx": "",
                "settledPnl": "",
                "uTime": "1597026383085"
            }],
            "trades": [{
                "instId": "BTC-USD-191018",
                "tradeId": "2",
            }]
        }]
    }
    

#### Push data parameters

**Parameter** | **Type** | **Description**  
---|---|---  
arg | Object | Channel to subscribe to  
> channel | String | Channel name  
> uid | String | User Identifier  
data | Array of objects | Subscribed data  
> pTime | String | Push time of both balance and position information, millisecond format of Unix timestamp, e.g. `1597026383085`  
> eventType | String | Event Type  
`snapshot`  
`delivered`  
`exercised`  
`transferred`  
`filled`  
`liquidation`  
`claw_back`  
`adl`  
`funding_fee`  
`adjust_margin`  
`set_leverage`  
`interest_deduction`  
`settlement`  
> balData | Array of objects | Balance data  
>> ccy | String | Currency  
>> cashBal | String | Cash Balance  
>> uTime | String | Update time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
> posData | Array of objects | Position data  
>> posId | String | Position ID  
>> tradeId | String | Last trade ID  
>> instId | String | Instrument ID, e.g `BTC-USD-180213`  
>> instType | String | Instrument type  
>> mgnMode | String | Margin mode  
`isolated`, `cross`  
>> avgPx | String | Average open price  
>> ccy | String | Currency used for margin  
>> posSide | String | Position side  
`long`, `short`, `net`  
>> pos | String | Quantity of positions. In the isolated margin mode, when doing manual transfers, a position with pos of `0` will be generated after the deposit is transferred  
>> baseBal | String | ~~Base currency balance, only applicable to`MARGIN`（Quick Margin Mode）~~(Deprecated)  
>> quoteBal | String | ~~Quote currency balance, only applicable to`MARGIN`（Quick Margin Mode）~~(Deprecated)  
>> posCcy | String | Position currency, only applicable to MARGIN positions.  
>> nonSettleAvgPx | String | Non-Settlement entry price  
The non-settlement entry price only reflects the average price at which the position is opened or increased.  
Applicable to `FUTURES` `cross`  
>> settledPnl | String | Accumulated settled P&L (calculated by settlement price)  
Applicable to `FUTURES` `cross`  
>> uTime | String | Update time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
> trades | Array of objects | Details of trade  
>> instId | String | Instrument ID, e.g. `BTC-USDT`  
>> tradeId | String | Trade ID  
Only balData will be pushed if only the account balance changes; only posData will be pushed if only the position changes.    
\- Initial snapshot: Only either position with non-zero position quantity or cash balance with non-zero quantity will be pushed. If the data is too large to be sent in a single push message, it will be split into multiple messages.   
\- For example, if you subscribe according to all currencies and the user has 5 currency balances that are not 0 and 20 positions, all 20 positions data and 5 currency balances data will be pushed in initial snapshot; Subsequently when there is change in pos of a position, only the data of that position will be pushed triggered by this change. 

### Position risk warning

This push channel is only used as a risk warning, and is not recommended as a risk judgment for strategic trading   
In the case that the market is volatile, there may be the possibility that the position has been liquidated at the same time that this message is pushed.  
The warning is sent when a position is at risk of liquidation for isolated margin positions. The warning is sent when all the positions are at risk of liquidation for cross-margin positions.  
Concurrent connection to this channel will be restricted by the following rules: [WebSocket connection count limit](/docs-v5/en/#overview-websocket-connection-count-limit).

#### URL Path

/ws/v5/private (required login)

> Request Example
    
    
    {
      "id": "1512",
      "op": "subscribe",
      "args": [
        {
          "channel": "liquidation-warning",
          "instType": "ANY"
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
            url = "wss://ws.okx.com:8443/ws/v5/private",
            useServerTime=False
        )
        await ws.start()
        args = [
            {
              "channel": "liquidation-warning",
              "instType": "ANY"
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
`liquidation-warning`  
> instType | String | Yes | Instrument type  
`MARGIN`  
`SWAP`  
`FUTURES`  
`OPTION`   
`ANY`  
> instFamily | String | No | Instrument family  
Applicable to `FUTURES`/`SWAP`/`OPTION`  
> instId | String | No | Instrument ID  
  
> Successful Response Example
    
    
    {
      "id": "1512",
      "event": "subscribe",
      "arg": {
        "channel": "liquidation-warning",
        "instType": "ANY"
      },
      "connId": "a4d3ae55"
    }
    

> Failure Response Example
    
    
    {
      "id": "1512",
      "event": "error",
      "code": "60012",
      "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{ \"channel\" : \"liquidation-warning\", \"instType\" : \"FUTURES\"}]}",
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
`liquidation-warning`  
> instType | String | Yes | Instrument type  
`OPTION`  
`FUTURES`  
`SWAP`  
`MARGIN`   
`ANY`  
> instFamily | String | No | Instrument family  
> instId | String | No | Instrument ID  
code | String | No | Error code  
msg | String | No | Error message  
connId | String | Yes | WebSocket connection ID  
  
> Push Data Example
    
    
    {
        "arg":{
            "channel":"liquidation-warning",
            "uid": "77982378738415879",
            "instType":"FUTURES"
        },
        "data":[
            {
                "cTime":"1619507758793",
                "ccy":"ETH",
                "instId":"ETH-USD-210430",
                "instType":"FUTURES",
                "lever":"10",
                "markPx":"2353.849",
                "mgnMode":"isolated",
                "mgnRatio":"11.731726509588816",
                "pTime":"1619507761462",
                "pos":"1",
                "posCcy":"",
                "posId":"307173036051017730",
                "posSide":"long",
                "uTime":"1619507761462",
            }
        ]
    }
    

#### Push data parameters

Parameter | Type | Description  
---|---|---  
arg | Object | Successfully subscribed channel  
> channel | String | Channel name  
> uid | String | User Identifier  
> instType | String | Instrument type  
> instFamily | String | Instrument family  
> instId | String | Instrument ID  
data | Array of objects | Subscribed data  
> instType | String | Instrument type  
> mgnMode | String | Margin mode, `cross` `isolated`  
> posId | String | Position ID  
> posSide | String | Position side  
`long`   
`short`   
`net` (`FUTURES`/`SWAP`/`OPTION`: positive `pos` means long position and negative `pos` means short position. `MARGIN`: `posCcy` being base currency means long position, `posCcy` being quote currency means short position.)  
> pos | String | Quantity of positions  
> posCcy | String | Position currency, only applicable to `MARGIN` positions  
> instId | String | Instrument ID, e.g. `BTC-USDT-SWAP`  
> lever | String | Leverage, not applicable to `OPTION` seller  
> markPx | String | Mark price  
> mgnRatio | String | Maintenance margin ratio  
> ccy | String | Currency used for margin  
> cTime | String | Creation time, Unix timestamp format in milliseconds, e.g. `1597026383085`.  
> uTime | String | Latest time position was adjusted, Unix timestamp format in milliseconds, e.g. `1597026383085`.  
> pTime | String | Push time of positions information, Unix timestamp format in milliseconds, e.g. `1597026383085`.  
Trigger push logic: the trigger logic of the liquidation warning and the liquidation message is the same 

### Account greeks channel

Retrieve account greeks information. Data will be pushed when triggered by events such as increase/decrease positions or cash balance in account, and will also be pushed in regular interval according to subscription granularity.  
Concurrent connection to this channel will be restricted by the following rules: [WebSocket connection count limit](/docs-v5/en/#overview-websocket-connection-count-limit).

#### URL Path

/ws/v5/private (required login)

> Request Example
    
    
    {
        "id": "1512",
        "op": "subscribe",
        "args": [{
            "channel": "account-greeks"
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
            url = "wss://ws.okx.com:8443/ws/v5/private",
            useServerTime=False
        )
        await ws.start()
        args = [{
            "channel": "account-greeks"
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
`subscribe` `unsubscribe`  
args | Array of objects | Yes | List of subscribed channels  
> channel | String | Yes | Channel name  
`account-greeks`  
> ccy | String | No | Settlement currency  
When the user specifies a settlement currency, event push will only be triggered when the position of the same settlement currency changes. For example, when ccy=BTC, if the position of `BTC-USDT-SWAP` changes, no event push will be triggered.  
  
> Successful Response Example
    
    
    {
        "id": "1512",
        "event": "subscribe",
        "arg": {
            "channel": "account-greeks"
        },
      "connId": "a4d3ae55"
    }
    

> Failure Response Example
    
    
    {
        "id": "1512",
        "event": "error",
        "code": "60012",
        "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{ \"channel\" : \"account-greeks\", \"ccy\" : \"BTC\"}]}",
      "connId": "a4d3ae55"
    }
    

#### Response parameters

Parameter | Type | Required | Description  
---|---|---|---  
id | String | No | Unique identifier of the message  
event | String | Yes | Operation  
`subscribe`  
`unsubscribe`  
`error`  
arg | Object | No | Subscribed channel  
> channel | String | Yes | Channel name,`account-greeks`  
> ccy | String | No | Settlement currency  
code | String | No | Error code  
msg | String | No | Error message  
connId | String | Yes | WebSocket connection ID  
  
> Push Data Example: single
    
    
    {
        "arg": {
            "channel": "account-greeks",
            "ccy": "BTC",
            "uid": "614488474791936"
        },
        "data": [
            {
                "ccy": "BTC",
                "deltaBS": "1.1246665401944310",
                "deltaPA": "-0.0074076183688949",
                "gammaBS": "0.0000000000000000",
                "gammaPA": "0.0148152367377899",
                "thetaBS": "2.0356991946421226",
                "thetaPA": "-0.0000000200174309",
                "ts": "1729179082006",
                "vegaBS": "0.0000000000000000",
                "vegaPA": "0.0000000000000000"
            }
        ]
    }
    

> Push Data Example
    
    
    {
        "arg": {
            "channel": "account-greeks",
            "uid": "614488474791936"
        },
        "data": [
            {
                "ccy": "BTC",
                "deltaBS": "1.1246665403011684",
                "deltaPA": "-0.0074021163991037",
                "gammaBS": "0.0000000000000000",
                "gammaPA": "0.0148042327982075",
                "thetaBS": "2.1342098201092528",
                "thetaPA": "-0.0000000200876441",
                "ts": "1729179001692",
                "vegaBS": "0.0000000000000000",
                "vegaPA": "0.0000000000000000"
            },
            {
                "ccy": "ETH",
                "deltaBS": "0.3810670161698570",
                "deltaPA": "-0.0688347042402955",
                "gammaBS": "-0.0000000000230396",
                "gammaPA": "0.1376693483440320",
                "thetaBS": "0.3314776517141782",
                "thetaPA": "0.0000000001316008",
                "ts": "1729179001692",
                "vegaBS": "-0.0000000045069794",
                "vegaPA": "-0.0000000000017267"
            }
        ]
    }
    

#### Push data parameters

**Parameters** | **Types** | **Description**  
---|---|---  
arg | Object | Successfully subscribed channel  
> channel | String | Channel name  
> uid | String | User Identifier  
data | Array of objects | Subscribed data  
> deltaBS | String | delta: Black-Scholes Greeks in dollars  
> deltaPA | String | delta: Greeks in coins  
> gammaBS | String | gamma: Black-Scholes Greeks in dollars, only applicable to OPTION cross  
> gammaPA | String | gamma: Greeks in coins, only applicable to OPTION cross  
> thetaBS | String | theta: Black-Scholes Greeks in dollars, only applicable to OPTION cross  
> thetaPA | String | theta: Greeks in coins, only applicable to OPTION cross  
> vegaBS | String | vega: Black-Scholes Greeks in dollars, only applicable to OPTION cross  
> vegaPA | String | vega: Greeks in coins, only applicable to OPTION cross  
> ccy | String | Currency  
> ts | String | Push time of account greeks, Unix timestamp format in milliseconds, e.g. 1597026383085  
The account greeks data is sent on event basis and regular basis   
\- The event push is not pushed in real-time. It is aggregated and pushed at a fixed time interval, around 50ms. For example, if multiple events occur within a fixed time interval, the system will aggregate them into a single message and push it at the end of the fixed time interval. If the data volume is too large, it may be split into multiple messages.   
\- When the user specifies a settlement currency in the subscribe request, event push will only be triggered when the position of the same settlement currency changes. For example, when subscribe `ccy`=BTC, if the position of `BTC-USDT-SWAP` changes, no event push will be triggered.   
\- The regular push sends updates regardless of whether there are activities or not.    
\- Only currencies in the account will be pushed. If the data is too large to be sent in a single push message, it will be split into multiple messages.   
\- For example, when subscribing to account-greeks channel without specifying ccy and there are 5 currencies are with non-zero balance, all 5 currencies data will be pushed in initial snapshot and in regular interval. Subsequently when there is change in balance or equity of an token, only the incremental data of that currency will be pushed triggered by this change.

---

# WebSocket

### 账户频道   
  
获取账户信息，首次订阅按照订阅维度推送数据，此外，当下单、撤单、成交等事件触发时，推送数据以及按照订阅维度定时推送数据  

该频道的并发连接受到如下规则限制：[WebSocket 连接限制](/docs-v5/zh/#overview-websocket-connection-count-limit)

#### 服务地址

/ws/v5/private (需要登录)

> 请求示例：单个
    
    
    {
        "id": "1512",
        "op": "subscribe",
        "args": [{
            "channel": "account",
            "ccy": "BTC"
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
            url = "wss://ws.okx.com:8443/ws/v5/private",
            useServerTime=False
        )
        await ws.start()
        args = [{
            "channel": "account",
            "ccy": "BTC"
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
        "args": [
        {
          "channel": "account",
          "extraParams": "
            {
              \"updateInterval\": \"0\"
            }
          "
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
            url = "wss://ws.okx.com:8443/ws/v5/private",
            useServerTime=False
        )
        await ws.start()
        args = [
            {
              "channel": "account",
              "extraParams": "{\"updateInterval\": \"0\"}"
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
`account`  
> ccy | String | 否 | 币种  
> extraParams | String | 否 | 额外配置  
>> updateInterval | int | 否 | `0`: 仅根据账户事件推送数据   
若不添加该字段或将其设置为除0外的其他值，数据将根据事件推送并定时推送。   
使用该字段需严格遵守以下格式。   
"extraParams": "  
{  
\"updateInterval\": \"0\"  
}  
"  
  
> 成功返回示例：单个
    
    
    {
        "id": "1512",
        "event": "subscribe",
        "arg": {
            "channel": "account",
            "ccy": "BTC"
        },
      "connId": "a4d3ae55"
    }
    
    
    
    import asyncio
    
    from okx.websocket.WsPrivateAsync import WsPrivateAsync
    
    
    def privateCallback(message):
        print(message)
    
    async def main():
        ws = WsPrivateAsync(
            apiKey = "YOUR_API_KEY",
            passphrase = "YOUR_PASSPHRASE",
            secretKey = "YOUR_SECRET_KEY",
            url = "wss://ws.okx.com:8443/ws/v5/private",
            useServerTime=False
        )
        await ws.start()
        args = [{"channel": "account"}]
    
        await ws.subscribe(args, callback=privateCallback)
        await asyncio.sleep(10)
    
        await ws.unsubscribe(args, callback=privateCallback)
        await asyncio.sleep(10)
    
    asyncio.run(main())
    
    

> 成功返回示例
    
    
    {
        "id": "1512",
        "event": "subscribe",
        "arg": {
            "channel": "account"
        },
      "connId": "a4d3ae55"
    }
    

> 失败返回示例
    
    
    {
        "id": "1512",
        "event": "error",
        "code": "60012",
        "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{ \"channel\" : \"account\", \"ccy\" : \"BTC\"}]}",
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
`account`  
> ccy | String | 否 | 币种  
code | String | 否 | 错误码  
msg | String | 否 | 错误消息  
connId | String | 是 | WebSocket连接ID  
  
> 推送示例
    
    
    {
        "arg": {
            "channel": "account",
            "uid": "44*********584"
        },
        "eventType": "snapshot",
        "curPage": 1,
        "lastPage": true,
        "data": [{
            "adjEq": "55444.12216906034",
            "availEq": "55444.12216906034",
            "borrowFroz": "0",
            "delta": "0",
            "deltaLever": "0",
            "deltaNeutralStatus": "0",
            "details": [{
                "availBal": "4734.371190691436",
                "availEq": "4734.371190691435",
                "borrowFroz": "0",
                "cashBal": "4750.426970691436",
                "ccy": "USDT",
                "coinUsdPrice": "0.99927",
                "crossLiab": "0",
                "colRes": "0",
                "collateralEnabled": false,
                "collateralRestrict": false, // 已弃用，请使用colRes
                "colBorrAutoConversion": "0",
                "disEq": "4889.379316336831",
                "eq": "4892.951170691435",
                "eqUsd": "4889.379316336831",
                "smtSyncEq": "0",
                "spotCopyTradingEq": "0",
                "fixedBal": "0",
                "frozenBal": "158.57998",
                "imr": "",
                "interest": "0",
                "isoEq": "0",
                "isoLiab": "0",
                "isoUpl": "0",
                "liab": "0",
                "maxLoan": "0",
                "mgnRatio": "",
                "mmr": "",
                "notionalLever": "",
                "ordFrozen": "0",
                "rewardBal": "0",
                "spotInUseAmt": "",
                "clSpotInUseAmt": "",
                "maxSpotInUseAmt": "",          
                "spotIsoBal": "0",
                "stgyEq": "150",
                "twap": "0",
                "uTime": "1705564213903",
                "upl": "-7.475800000000003",
                "uplLiab": "0",
                "spotBal": "",
                "openAvgPx": "",
                "accAvgPx": "",
                "spotUpl": "",
                "spotUplRatio": "",
                "totalPnl": "",
                "totalPnlRatio": ""
            }],
            "imr": "0",
            "isoEq": "0",
            "mgnRatio": "",
            "mmr": "0",
            "notionalUsd": "0",
            "notionalUsdForBorrow": "0",
            "notionalUsdForFutures": "0",
            "notionalUsdForOption": "0",
            "notionalUsdForSwap": "0",
            "ordFroz": "0",
            "totalEq": "55868.06403501676",
            "uTime": "1705564223311",
            "upl": "0"
        }]
    }
    

#### 推送数据参数

**参数名** | **类型** | **描述**  
---|---|---  
arg | Object | 请求订阅的频道  
> channel | String | 频道名  
> uid | String | 用户标识  
eventType | String | 事件类型：  
`snapshot`: 首推及定时快照推送   
`event_update`：事件推送  
curPage | Integer | 当前消息分页页数   
仅适用于`snapshot`事件类型，`event_update`时不返回。  
lastPage | Boolean | 当前消息是否为最后一页：  
`true`  
`false`  
仅适用于`snapshot`事件类型，`event_update`时不返回.  
data | Array of objects | 订阅的数据  
> uTime | String | 获取账户信息的最新时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
> totalEq | String | 美金层面权益  
> isoEq | String | 美金层面逐仓仓位权益  
适用于`合约模式`/`跨币种保证金模式`/`组合保证金模式`  
> adjEq | String | 美金层面有效保证金  
适用于`现货模式`/`跨币种保证金模式`/`组合保证金模式`  
> availEq | String | 账户美金层面可用保证金，排除因总质押借币上限而被限制的币种  
适用于`跨币种保证金模式/组合保证金模式`  
> ordFroz | String | 美金层面全仓挂单占用保证金  
仅适用于`现货模式`/`跨币种保证金模式`  
> imr | String | 美金层面占用保证金  
适用于`现货模式`/`跨币种保证金模式`/`组合保证金模式`  
> mmr | String | 美金层面维持保证金  
适用于`现货模式`/`跨币种保证金模式`/`组合保证金模式`  
> borrowFroz | String | 账户美金层面潜在借币占用保证金  
仅适用于`现货模式`/`跨币种保证金模式`/`组合保证金模式`。在其他账户模式下为""。  
> mgnRatio | String | 美金层面维持保证金率  
适用于`现货模式`/`跨币种保证金模式`/`组合保证金模式`  
> notionalUsd | String | 以美金价值为单位的持仓数量，即仓位美金价值  
适用于`现货模式`/`跨币种保证金模式`/`组合保证金模式`  
> notionalUsdForBorrow | String | 借币金额（美元价值）  
适用于`现货模式`/`跨币种保证金模式`/`组合保证金模式`  
> notionalUsdForSwap | String | 永续合约持仓美元价值  
适用于`跨币种保证金模式`/`组合保证金模式`  
> notionalUsdForFutures | String | 交割合约持仓美元价值  
适用于`跨币种保证金模式`/`组合保证金模式`  
> notionalUsdForOption | String | 期权持仓美元价值  
适用于`现货模式`/`跨币种保证金模式`/`组合保证金模式`  
> upl | String | 账户层面全仓未实现盈亏（美元单位）  
适用于`跨币种保证金模式`/`组合保证金模式`  
> delta | String | Delta (USD)  
> deltaLever | String | Delta权益比率  
deltaLever = delta/totalEq  
> deltaNeutralStatus | String | Delta 风险状态  
`0`: 普通  
`1`: 限制划转  
`2`: 仅支持降低 Delta - 相同基础货币的现货、交割和永续合约视为同一标的资产。同一标的资产内，仅能新下一笔降低 Delta 值的订单，且下单时不应存在其他挂单。如果触发此限制，且您的账户 Delta 大于 500,000 USD，您的所有限价、市价、高级限价单挂单将被撤销。  
> details | Array | 各币种资产详细信息  
>> ccy | String | 币种  
>> eq | String | 币种总权益  
>> cashBal | String | 币种余额  
>> uTime | String | 币种余额信息的更新时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
>> isoEq | String | 币种逐仓仓位权益  
适用于`合约模式`/`跨币种保证金模式`/`组合保证金模式`  
>> availEq | String | 可用保证金  
适用于`合约模式`/`跨币种保证金模式`/`组合保证金模式`  
>> disEq | String | 美金层面币种折算权益  
>> fixedBal | String | 抄底宝、逃顶宝功能的币种冻结金额  
>> availBal | String | 可用余额  
>> frozenBal | String | 币种占用金额  
>> ordFrozen | String | 挂单冻结数量  
适用于`现货模式`/`合约模式`/`跨币种保证金模式`  
>> liab | String | 币种负债额  
值为正数，如 `21625.64`  
适用于`现货模式`/`跨币种保证金模式`/`组合保证金模式`  
>> upl | String | 未实现盈亏  
适用于`合约模式`/`跨币种保证金模式`/`组合保证金模式`  
>> uplLiab | String | 由于仓位未实现亏损导致的负债  
适用于`跨币种保证金模式`/`组合保证金模式`  
>> crossLiab | String | 币种全仓负债额  
适用于`现货模式`/`跨币种保证金模式`/`组合保证金模式`  
>> isoLiab | String | 币种逐仓负债额  
适用于`跨币种保证金模式`/`组合保证金模式`  
>> rewardBal | String | 体验金余额  
>> mgnRatio | String | 币种全仓维持保证金率，衡量账户内某项资产风险的指标  
适用于`合约模式`且有全仓仓位时  
>> imr | String | 币种维度全仓占用保证金  
适用于`合约模式`且有全仓仓位时  
>> mmr | String | 币种维度全仓维持保证金  
适用于`合约模式`且有全仓仓位时  
>> interest | String | 计息  
值为正数，如 `9.01`  
适用于`现货模式`/`跨币种保证金模式`/`组合保证金模式`  
>> twap | String | 当前负债币种触发自动换币的风险  
0、1、2、3、4、5其中之一，数字越大代表您的负债币种触发自动换币概率越高  
适用于`现货模式`/`跨币种保证金模式`/`组合保证金模式`  
>> frpType | String | 自动换币类型  
`0`：未发生自动换币  
`1`：基于用户的自动换币  
`2`：基于平台借币限额的自动换币  
  
当twap>=1时返回1或2代表自动换币风险类型，适用于`现货模式`/`跨币种保证金模式`/`组合保证金模式`  
>> maxLoan | String | 币种最大可借  
适用于`现货模式`/`跨币种保证金模式`/`组合保证金模式` 的全仓  
>> eqUsd | String | 币种权益美金价值  
>> notionalLever | String | 币种杠杆倍数  
适用于`合约模式`  
>> coinUsdPrice | String | 币种美元指数  
>> stgyEq | String | 策略权益  
>> isoUpl | String | 逐仓未实现盈亏  
适用于`合约模式`/`跨币种保证金模式`/`组合保证金模式`  
>> borrowFroz | String | 币种美金层面潜在借币占用保证金  
仅适用于`现货模式`/`跨币种保证金模式`/`组合保证金模式`。在其他账户模式下为""。  
>> spotInUseAmt | String | 现货对冲占用数量  
适用于`组合保证金模式`  
>> clSpotInUseAmt | String | 用户自定义现货占用数量  
适用于`组合保证金模式`  
>> maxSpotInUseAmt | String | 系统计算得到的最大可能现货占用数量  
适用于`组合保证金模式`  
>> spotIsoBal | String | 现货逐仓余额  
仅适用于现货带单/跟单  
适用于`现货模式`/`合约模式`  
>> smtSyncEq | String | 合约智能跟单权益  
默认为0，仅适用于跟单人。  
>> spotCopyTradingEq | String | 现货智能跟单权益  
默认为0，仅适用于跟单人。  
>> spotBal | String | 现货余额 ，单位为 币种，比如 BTC。[详情](https://www.okx.com/zh-hans/help/i-introduction-of-spot)  
>> openAvgPx | String | 现货开仓成本价 单位 USD。 [详情](https://www.okx.com/zh-hans/help/i-introduction-of-spot)  
>> accAvgPx | String | 现货累计成本价 单位 USD。 [详情](https://www.okx.com/zh-hans/help/i-introduction-of-spot)  
>> spotUpl | String | 现货未实现收益，单位 USD。 [详情](https://www.okx.com/zh-hans/help/i-introduction-of-spot)  
>> spotUplRatio | String | 现货未实现收益率。[详情](https://www.okx.com/zh-hans/help/i-introduction-of-spot)  
>> totalPnl | String | 现货累计收益，单位 USD。 [详情](https://www.okx.com/zh-hans/help/i-introduction-of-spot)  
>> totalPnlRatio | String | 现货累计收益率。[详情](https://www.okx.com/zh-hans/help/i-introduction-of-spot)  
>> colRes | String | 平台维度质押限制状态  
`0`：限制未触发  
`1`：限制未触发，但该币种接近平台质押上限  
`2`：限制已触发。该币种不可用作新订单的保证金，这可能会导致下单失败。但它仍会被计入账户有效保证金，保证金率不会收到影响。  
更多详情，请参阅[平台总质押借币上限说明](https://www.okx.com/zh-hans/help/introduction-to-the-platforms-collateralized-borrowing-limit-mechanism)。  
>> colBorrAutoConversion | String | 基于平台质押借币限额的自动换币风险指标。分为1-5多个等级，数字越大，触发自动换币的可能性越大。默认值为0，表示当前无风险。5表示该用户正在进行自动换币，4代表该用户即将被进行自动换币，1/2/3表示存在自动换币风险。  
适用于`现货模式`/`合约模式`/`跨币种保证金模式`/`组合保证金模式`  
当某币种的全平台质押借币量超出平台总上限一定比例时，对于质押该币种且借币量较大的用户，平台将通过自动换币降低质押借币风险。请减少该币种的质押数量或偿还负债，以降低风险。  
更多详情，请参阅[平台总质押借币上限说明](https://www.okx.com/zh-hans/help/introduction-to-the-platforms-collateralized-borrowing-limit-mechanism)。  
>> collateralRestrict | Boolean | ~~平台维度的质押借币限制  
`true`  
`false`~~（已弃用，请使用colRes）  
>> collateralEnabled | Boolean | `true`：质押币  
`false`：非质押币  
适用于`跨币种保证金模式  
  
\- 账户频道基于事件推送，并进行定时推送   
\- 账户频道的事件推送并非在事件发生时实时进行，而是按照大约50毫秒的固定时间窗口进行聚合推送。例如，在固定时间窗口内发生多个事件，系统将尽量聚合为一条消息并在固定时间窗口结束时进行推送。在数据量过大的情况下可能拆分为多条消息。   
\- 无论是否有账户维度的变化，定时推送都会发送更新    
\- 只推用户币种层面资产不为0的账户信息。币种层面资产不为0的定义：eq、availEq、availBal 中任意一个字段不为0，即币种层面资产不为0。如果数据太大无法在单个推送消息中发送，它将被分成多个消息发送。   
\- 例：按照所有币种订阅且有5个币种的余额或者权益都不为0，首次和定时推全部5个；账户下有一个币种余额或者权益改变，那么账户变更的触发只推这一个。 

### 持仓频道 

获取持仓信息，首次订阅按照订阅维度推送数据，此外，当下单、撤单等事件触发时，推送数据以及按照订阅维度定时推送数据  
该频道的并发连接受到如下规则限制：[WebSocket 连接限制](/docs-v5/zh/#overview-websocket-connection-count-limit)

#### 服务地址

/ws/v5/private (需要登录)

> 请求示例：单个
    
    
    {
        "id": "1512",
        "op": "subscribe",
        "args": [{
            "channel": "positions",
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
            url = "wss://ws.okx.com:8443/ws/v5/private",
            useServerTime=False
        )
        await ws.start()
        args = [
            {
              "channel": "positions",
              "instType": "FUTURES",
              "instFamily": "BTC-USD"
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
        "args": [
            {
                "channel": "positions",
                "instType": "ANY",
                "extraParams": "
                    {
                        \"updateInterval\": \"0\"
                    }
                "
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
            url = "wss://ws.okx.com:8443/ws/v5/private",
            useServerTime=False
        )
        await ws.start()
        args = [
            {
                "channel": "positions",
                "instType": "ANY",
                "extraParams": "{\"updateInterval\": \"0\"}"
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
`positions`  
> instType | String | 是 | 产品类型  
`MARGIN`：币币杠杆  
`SWAP`：永续合约  
`FUTURES`：交割合约  
`OPTION`：期权  
`EVENTS`：事件合约  
`ANY`：全部  
> instFamily | String | 否 | 交易品种  
适用于`交割`/`永续`/`期权`  
> instId | String | 否 | 产品ID  
如果同时传了 instId 和 instFamily，instId 将被使用  
> extraParams | String | 否 | 额外配置  
>> updateInterval | int | 否 | `0`: 仅根据持仓事件推送数据  
`2000, 3000, 4000`: 根据持仓事件推送，且根据设置的时间间隔定时推送（ms）  
  
若不添加该字段或将其设置为上述合法值以外的其他值，数据将根据事件推送并大约每 5 秒定期推送一次。  
  
使用该字段需严格遵守以下格式。  
"extraParams": "  
{  
\"updateInterval\": \"0\"  
}  
"  
  
> 成功返回示例：单个
    
    
    {
        "id": "1512",
        "event": "subscribe",
        "arg": {
            "channel": "positions",
            "instType": "FUTURES",
            "instFamily": "BTC-USD"
        },
        "connId": "a4d3ae55"
    }
    

> 成功返回示例
    
    
    {
        "id": "1512",
        "event": "subscribe",
        "arg": {
            "channel": "positions",
            "instType": "ANY"
        },
        "connId": "a4d3ae55"
    }
    

> 失败返回示例
    
    
    {
        "id": "1512",
        "event": "error",
        "code": "60012",
        "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{ \"channel\" : \"positions\", \"instType\" : \"FUTURES\"}]}",
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
`MARGIN`：币币杠杆  
`SWAP`：永续合约  
`FUTURES`：交割合约  
`OPTION`：期权  
`EVENTS`：事件合约  
`ANY`：全部  
> instFamily | String | 否 | 交易品种  
适用于`交割`/`永续`/`期权`  
> instId | String | 否 | 产品ID  
code | String | 否 | 错误码  
msg | String | 否 | 错误消息  
connId | String | 是 | WebSocket连接ID  
  
> 推送示例：单个
    
    
    {
        "arg":{
            "channel":"positions",
            "uid": "77982378738415879",
            "instType":"FUTURES"
        },
        "eventType": "snapshot",
        "curPage": 1,
        "lastPage": true,
        "data":[
            {
                "adl":"1",
                "availPos":"1",
                "avgPx":"2566.31",
                "cTime":"1619507758793",
                "ccy":"ETH",
                "deltaBS":"",
                "deltaPA":"",
                "gammaBS":"",
                "gammaPA":"",
                "hedgedPos": "",
                "imr":"",
                "instId":"ETH-USD-210430",
                "instType":"FUTURES",
                "interest":"0",
                "idxPx":"2566.13",
                "last":"2566.22",
                "lever":"10",
                "liab":"",
                "liabCcy":"",
                "liqPx":"2352.8496681818233",
                "markPx":"2353.849",
                "margin":"0.0003896645377994",
                "mgnMode":"isolated",
                "mgnRatio":"11.731726509588816",
                "mmr":"0.0000311811092368",
                "notionalUsd":"2276.2546609009605",
                "optVal":"",
                "pTime":"1619507761462",
                "pendingCloseOrdLiabVal":"0.1",
                "pos":"1",
                "baseBorrowed": "",
                "baseInterest": "",
                "quoteBorrowed": "",
                "quoteInterest": "",
                "posCcy":"",
                "posId":"307173036051017730",
                "posSide":"long",
                "spotInUseAmt": "",
                "clSpotInUseAmt": "",
                "maxSpotInUseAmt": "",
                "spotInUseCcy": "",
                "bizRefId": "",
                "bizRefType": "",
                "thetaBS":"",
                "thetaPA":"",
                "tradeId":"109844",
                "uTime":"1619507761462",
                "upl":"-0.0000009932766034",
                "uplLastPx":"-0.0000009932766034",
                "uplRatio":"-0.0025490556801078",
                "uplRatioLastPx":"-0.0025490556801078",
                "vegaBS":"",
                "vegaPA":"",
                "realizedPnl":"0.001",
                "pnl":"0.0011",
                "fee":"-0.0001",
                "fundingFee":"0",
                "liqPenalty":"0",
                "nonSettleAvgPx":"",
                "settledPnl":"",
                "closeOrderAlgo":[
                    {
                        "algoId":"123",
                        "slTriggerPx":"123",
                        "slTriggerPxType":"mark",
                        "tpTriggerPx":"123",
                        "tpTriggerPxType":"mark",
                        "closeFraction":"0.6"
                    },
                    {
                        "algoId":"123",
                        "slTriggerPx":"123",
                        "slTriggerPxType":"mark",
                        "tpTriggerPx":"123",
                        "tpTriggerPxType":"mark",
                        "closeFraction":"0.4"
                    }
                ]
            }
        ]
    }
    

> 推送示例
    
    
    {
        "arg": {
            "channel": "positions",
            "uid": "77982378738415879",
            "instType": "ANY"
        },
        "eventType": "snapshot",
        "curPage": 1,
        "lastPage": true,
        "data": [{
            "adl": "1",
            "availPos": "1",
            "avgPx": "2566.31",
            "cTime": "1619507758793",
            "ccy": "ETH",
            "deltaBS": "",
            "deltaPA": "",
            "gammaBS": "",
            "gammaPA": "",
            "hedgedPos": "",
            "imr": "",
            "instId": "ETH-USD-210430",
            "instType": "FUTURES",
            "interest": "0",
            "idxPx": "2566.13",
            "last": "2566.22",
            "usdPx": "",
            "bePx": "2353.949",
            "lever": "10",
            "liab": "",
            "liabCcy": "",
            "liqPx": "2352.8496681818233",
            "markPx": "2353.849",
            "margin": "0.0003896645377994",
            "mgnMode": "isolated",
            "mgnRatio": "11.731726509588816",
            "mmr": "0.0000311811092368",
            "notionalUsd": "2276.2546609009605",
            "optVal": "",
            "pendingCloseOrdLiabVal": "0.1",
            "pTime": "1619507761462",
            "pos": "1",
            "baseBorrowed": "",
            "baseInterest": "",
            "quoteBorrowed": "",
            "quoteInterest": "",
            "posCcy": "",
            "posId": "307173036051017730",
            "posSide": "long",
            "spotInUseAmt": "",
            "clSpotInUseAmt": "",
            "maxSpotInUseAmt": "",
            "spotInUseCcy": "",
            "bizRefId": "",
            "bizRefType": "",
            "thetaBS": "",
            "thetaPA": "",
            "tradeId": "109844",
            "uTime": "1619507761462",
            "upl": "-0.0000009932766034",
            "uplLastPx": "-0.0000009932766034",
            "uplRatio": "-0.0025490556801078",
            "uplRatioLastPx": "-0.0025490556801078",
            "vegaBS": "",
            "vegaPA": "",
            "realizedPnl": "0.001",
            "pnl": "0.0011",
            "fee": "-0.0001",
            "fundingFee": "0",
            "liqPenalty": "0",
            "nonSettleAvgPx": "",
            "settledPnl": "",
            "closeOrderAlgo": [{
                    "algoId": "123",
                    "slTriggerPx": "123",
                    "slTriggerPxType": "mark",
                    "tpTriggerPx": "123",
                    "tpTriggerPxType": "mark",
                    "closeFraction": "0.6"
                },
                {
                    "algoId": "123",
                    "slTriggerPx": "123",
                    "slTriggerPxType": "mark",
                    "tpTriggerPx": "123",
                    "tpTriggerPxType": "mark",
                    "closeFraction": "0.4"
                }
            ]
        }, {
            "adl": "1",
            "availPos": "1",
            "avgPx": "2566.31",
            "cTime": "1619507758793",
            "ccy": "ETH",
            "deltaBS": "",
            "deltaPA": "",
            "gammaBS": "",
            "gammaPA": "",
            "imr": "",
            "hedgedPos": "",
            "instId": "ETH-USD-SWAP",
            "instType": "SWAP",
            "interest": "0",
            "idxPx": "2566.13",
            "last": "2566.22",
            "usdPx": "",
            "bePx": "2353.949",
            "lever": "10",
            "liab": "",
            "liabCcy": "",
            "liqPx": "2352.8496681818233",
            "markPx": "2353.849",
            "margin": "0.0003896645377994",
            "mgnMode": "isolated",
            "mgnRatio": "11.731726509588816",
            "mmr": "0.0000311811092368",
            "notionalUsd": "2276.2546609009605",
            "optVal": "",
            "pendingCloseOrdLiabVal": "0.1",
            "pTime": "1619507761462",
            "pos": "1",
            "baseBorrowed": "",
            "baseInterest": "",
            "quoteBorrowed": "",
            "quoteInterest": "",
            "posCcy": "",
            "posId": "307173036051017730",
            "posSide": "long",
            "spotInUseAmt": "",
            "clSpotInUseAmt": "",
            "maxSpotInUseAmt": "",
            "spotInUseCcy": "",
            "bizRefId": "",
            "bizRefType": "",
            "thetaBS": "",
            "thetaPA": "",
            "tradeId": "109844",
            "uTime": "1619507761462",
            "upl": "-0.0000009932766034",
            "uplLastPx": "-0.0000009932766034",
            "uplRatio": "-0.0025490556801078",
            "uplRatioLastPx": "-0.0025490556801078",
            "vegaBS": "",
            "vegaPA": "",
            "realizedPnl": "0.001",
            "pnl": "0.0011",
            "fee": "-0.0001",
            "fundingFee": "0",
            "liqPenalty": "0",
            "nonSettleAvgPx": "",
            "settledPnl": "",
            "closeOrderAlgo": [{
                    "algoId": "123",
                    "slTriggerPx": "123",
                    "slTriggerPxType": "mark",
                    "tpTriggerPx": "123",
                    "tpTriggerPxType": "mark",
                    "closeFraction": "0.6"
                },
                {
                    "algoId": "123",
                    "slTriggerPx": "123",
                    "slTriggerPxType": "mark",
                    "tpTriggerPx": "123",
                    "tpTriggerPxType": "mark",
                    "closeFraction": "0.4"
                }
            ]
        }]
    }
    

#### 推送数据参数

参数名 | 类型 | 描述  
---|---|---  
arg | Object | 订阅成功的频道  
> channel | String | 频道名  
> uid | String | 用户标识  
> instType | String | 产品类型  
`MARGIN`：币币杠杆  
`SWAP`：永续合约  
`FUTURES`：交割合约  
`OPTION`：期权  
`EVENTS`：事件合约  
> instFamily | String | 交易品种  
> instId | String | 产品ID  
eventType | String | 事件类型：  
`snapshot`: 首推及定时快照推送   
`event_update`：事件推送  
curPage | Integer | 当前消息分页页数   
仅适用于`snapshot`事件类型，`event_update`时不返回。  
lastPage | Boolean | 当前消息是否为最后一页：  
`true`  
`false`  
仅适用于`snapshot`事件类型，`event_update`时不返回.  
data | Array of objects | 订阅的数据  
> instType | String | 产品类型  
`MARGIN`：币币杠杆  
`SWAP`：永续合约  
`FUTURES`：交割合约  
`OPTION`：期权  
`EVENTS`：事件合约  
> mgnMode | String | 保证金模式， `cross`：全仓 `isolated`：逐仓  
> posId | String | 持仓ID  
> posSide | String | 持仓方向  
`long`：开平仓模式开多  
`short`：开平仓模式开空  
`net`：买卖模式（`交割`/`永续`/`期权`：`pos`为正代表开多，`pos`为负代表开空。`币币杠杆`：`posCcy`为交易货币时，代表开多；`posCcy`为计价货币时，代表开空。）  
> pos | String | 持仓数量，逐仓自主划转模式下，转入保证金后会产生pos为`0`的仓位  
> hedgedPos | String | 对冲持仓数量  
仅在delta 中性策略模式的账户返回stgyType:1，对普通策略模式的账户返回""  
> baseBal | String | ~~交易币余额，适用于`币币杠杆`（逐仓一键借币模式）~~（已弃用）  
> quoteBal | String | ~~计价币余额 ，适用于`币币杠杆`（逐仓一键借币模式）~~（已弃用）  
> baseBorrowed | String | ~~交易币已借，适用于`币币杠杆`（逐仓一键借币模式）~~（已弃用）  
> baseInterest | String | ~~交易币计息，适用于`币币杠杆`（逐仓一键借币模式）~~（已弃用）  
> quoteBorrowed | String | ~~计价币已借，适用于`币币杠杆`（逐仓一键借币模式）~~（已弃用）  
> quoteInterest | String | ~~计价币计息，适用于`币币杠杆`（逐仓一键借币模式）~~（已弃用）  
> posCcy | String | 持仓数量币种，仅适用于`币币杠杆`  
> availPos | String | 可平仓数量，适用于 `币币杠杆`,`期权`  
对于杠杆仓位，平仓时，杠杆还清负债后，余下的部分会视为币币交易，如果想要减少币币交易的数量，可通过"获取最大可用数量"接口获取只减仓的可用数量。  
> avgPx | String | 开仓平均价  
> upl | String | 未实现收益（以标记价格计算）  
> uplRatio | String | 未实现收益率（以标记价格计算  
> uplLastPx | String | 以最新成交价格计算的未实现收益，主要做展示使用，实际值还是 upl  
> uplRatioLastPx | String | 以最新成交价格计算的未实现收益率  
> instId | String | 产品ID，如 `BTC-USDT-SWAP`  
> lever | String | 杠杆倍数，不适用于`期权卖方`  
> liqPx | String | 预估强平价  
不适用于`期权`  
> markPx | String | 最新标记价格  
> imr | String | 初始保证金，仅适用于`全仓`  
> margin | String | 保证金余额，仅适用于`逐仓`，可增减  
> mgnRatio | String | 维持保证金率  
> mmr | String | 维持保证金  
> liab | String | 负债额，仅适用于`币币杠杆`  
> liabCcy | String | 负债币种，仅适用于`币币杠杆`  
> interest | String | 利息，已经生成未扣利息  
> tradeId | String | 最新成交ID  
> notionalUsd | String | 以美金价值为单位的持仓数量  
> optVal | String | 期权价值，仅适用于`期权`  
> pendingCloseOrdLiabVal | String | 逐仓杠杆负债对应平仓挂单的数量  
> adl | String | 自动减仓信号区，分为6档，从0到5，数字越小代表adl强度越弱  
仅适用于`交割/永续/期权`  
> bizRefId | String | 外部业务id，如 体验券id  
> bizRefType | String | 外部业务类型  
> ccy | String | 占用保证金的币种  
> last | String | 最新成交价  
> idxPx | String | 最新指数价格  
> usdPx | String | 保证金币种的市场最新美金价格 仅适用于`交割`/`永续`/`期权`  
> bePx | String | 盈亏平衡价  
> deltaBS | String | 美金本位持仓仓位delta，仅适用于`期权`  
> deltaPA | String | 币本位持仓仓位delta，仅适用于`期权`  
> gammaBS | String | 美金本位持仓仓位gamma，仅适用于`期权`  
> gammaPA | String | 币本位持仓仓位gamma，仅适用于`期权`  
> thetaBS | String | 美金本位持仓仓位theta，仅适用于`期权`  
> thetaPA | String | 币本位持仓仓位theta，仅适用于`期权`  
> vegaBS | String | 美金本位持仓仓位vega，仅适用于`期权`  
> vegaPA | String | 币本位持仓仓位vega，仅适用于`期权`  
> spotInUseAmt | String | 现货对冲占用数量  
适用于`组合保证金模式`  
> clSpotInUseAmt | String | 用户自定义现货占用数量  
适用于`组合保证金模式`  
> maxSpotInUseAmt | String | 系统计算得到的最大可能现货占用数量  
适用于`组合保证金模式`  
> spotInUseCcy | String | 现货对冲占用币种，如 `BTC`  
适用于`组合保证金模式`  
> realizedPnl | String | 已实现收益  
仅适用于`交割`/`永续`/`期权`  
realizedPnl=pnl+fee+fundingFee+liqPenalty+settledPnl  
> pnl | String | 平仓订单累计收益额(不包括手续费)  
> fee | String | 累计手续费金额，正数代表平台返佣 ，负数代表平台扣除  
> fundingFee | String | 累计资金费用  
> liqPenalty | String | 累计爆仓罚金，有值时为负数。  
> closeOrderAlgo | Array of objects | 平仓策略委托订单。调用策略委托下单，且`closeFraction`=1 时，该数组才会有值。  
>> algoId | String | 策略委托单ID  
>> slTriggerPx | String | 止损触发价  
>> slTriggerPxType | String | 止损触发价类型  
`last`：最新价格  
`index`：指数价格  
`mark`：标记价格  
>> tpTriggerPx | String | 止盈委托价  
>> tpTriggerPxType | String | 止盈触发价类型  
`last`：最新价格  
`index`：指数价格  
`mark`：标记价格  
>> closeFraction | String | 策略委托触发时，平仓的百分比。1 代表100%  
> cTime | String | 持仓创建时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
> uTime | String | 最近一次持仓更新时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
> pTime | String | 持仓信息的推送时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
> nonSettleAvgPx | String | 未结算均价  
不受结算影响的加权开仓价格，仅在新增头寸时更新，和开仓均价的主要区别在于是否受到结算影响。  
适用于`全仓``交割`  
> settledPnl | String | 累计已结算收益（以结算价格计算）  
适用于`全仓``交割`  
  
\- 持仓频道基于事件推送，并进行定时推送。   
\- 持仓频道的事件推送并非在事件发生时实时进行，而是按照大约50毫秒的固定时间窗口进行聚合推送。例如，在固定时间窗口内发生多个事件，系统将尽量聚合为一条消息并在固定时间窗口结束时进行推送。在数据量过大的情况下可能拆分为多条消息。   
\- 无论是否有仓位的变化，定时推送都会发送更新。   
\- 若事件推送和定时推送同时发生，系统将在发送一次事件推送消息后再发送一次定时推送消息。  Portfolio Margin 账户下，持仓的 IMR MMR的数据是后端服务以ristUnit为最小粒度重新计算，相同riskUnit全仓仓位的imr和mmr返回值相同。  逐仓交易设置里是自主划转模式，转入保证金后会推送持仓量为0的仓位。    
\- 只推用户持有的仓位。用户持仓仓位定义：持逐仓自主划转模式下的逐仓仓位pos=0，pos>0或者pos<0都认为持有仓位。如果数据太大无法在单个推送消息中发送，它将被分成多个消息发送。   
\- 例：按underlying订阅且该underlying下有20个持仓，首次和定时推全部20个；持仓下有一个成交改变其中的一个持仓，那么持仓变更只推这一个。  与交割合约不同，期权持仓到期之后，期权持仓在到期后会自动行权或作废，持仓本身随即消失，因此，该频道不会推送期权到期的信息。 

### 账户余额和持仓频道 

获取账户余额和持仓信息，首次订阅按照订阅维度推送数据，此外，当成交、资金划转等事件触发时，推送数据。  

该频道适用于尽快获取账户现金余额和仓位资产变化的信息。  
该频道的并发连接受到如下规则限制：[WebSocket 连接限制](/docs-v5/zh/#overview-websocket-connection-count-limit)

#### 服务地址

/ws/v5/private (需要登录)

> 请求示例
    
    
    {
        "id": "1512",
        "op": "subscribe",
        "args": [{
            "channel": "balance_and_position"
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
            url = "wss://ws.okx.com:8443/ws/v5/private",
            useServerTime=False
        )
        await ws.start()
        args = [{
            "channel": "balance_and_position"
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
`balance_and_position`  
  
> 成功返回示例
    
    
    {
        "id": "1512",
        "event": "subscribe",
        "arg": {
            "channel": "balance_and_position"
        },
        "connId": "a4d3ae55"
    }
    

> 失败返回示例
    
    
    {
        "id": "1512",
        "event": "error",
        "code": "60012",
        "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{ \"channel\" : \"balance_and_position\"}]}",
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
`balance_and_position`  
code | String | 否 | 错误码  
msg | String | 否 | 错误消息  
connId | String | 是 | WebSocket连接ID  
  
> 推送示例
    
    
    {
        "arg": {
            "channel": "balance_and_position",
            "uid": "77982378738415879"
        },
        "data": [{
            "pTime": "1597026383085",
            "eventType": "snapshot",
            "balData": [{
                "ccy": "BTC",
                "cashBal": "1",
                "uTime": "1597026383085"
            }],
            "posData": [{
                "posId": "1111111111",
                "tradeId": "2",
                "instId": "BTC-USD-191018",
                "instType": "FUTURES",
                "mgnMode": "cross",
                "posSide": "long",
                "pos": "10",
                "ccy": "BTC",
                "posCcy": "",
                "avgPx": "3320",
                "nonSettleAvgPx": "",
                "settledPnl": "",
                "uTime": "1597026383085"
            }],
            "trades": [{
                "instId": "BTC-USD-191018",
                "tradeId": "2",
            }]
        }]
    }
    

#### 推送数据参数

**参数名** | **类型** | **描述**  
---|---|---  
arg | Object | 请求订阅的频道  
> channel | String | 频道名  
> uid | String | 用户标识  
data | Array of objects | 订阅的数据  
> pTime | String | 推送时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
> eventType | String | 事件类型  
`snapshot`：首推快照  
`delivered`：交割  
`exercised`：行权  
`transferred`：划转  
`filled`：成交  
`liquidation`：强平  
`claw_back`：穿仓补偿  
`adl`：ADL自动减仓  
`funding_fee`：资金费  
`adjust_margin`：调整保证金  
`set_leverage`：设置杠杆  
`interest_deduction`：扣息  
`settlement`：交割结算  
> balData | String | 余额数据  
>> ccy | String | 币种  
>> cashBal | String | 币种余额  
>> uTime | String | 币种余额信息的更新时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
> posData | String | 持仓数据  
>> posId | String | 持仓ID  
>> tradeId | String | 最新成交ID  
>> instId | String | 交易产品ID，如 `BTC-USD-180213`  
>> instType | String | 交易产品类型  
`MARGIN`：币币杠杆  
`SWAP`：永续合约  
`FUTURES`：交割合约  
`OPTION`：期权  
>> mgnMode | String | 保证金模式  
`isolated`, `cross`  
>> avgPx | String | 开仓平均价  
>> ccy | String | 占用保证金的币种  
>> posSide | String | 持仓方向  
`long`，`short`，`net`  
>> pos | String | 持仓数量，逐仓自主划转模式下，转入保证金后会产生pos为`0`的仓位  
>> baseBal | String | ~~交易币余额  
适用于 `币币杠杆`（逐仓一键借币模式）~~（已弃用）  
>> quoteBal | String | ~~计价币余额  
适用于 `币币杠杆`（逐仓一键借币模式）~~（已弃用）  
>> posCcy | String | 持仓数量币种  
只适用于币币杠杆仓位。当是交割、永续、期权持仓时，该字段返回“”  
>> nonSettleAvgPx | String | 未结算均价  
不受结算影响的加权开仓价格，仅在新增头寸时更新，和开仓均价的主要区别在于是否受到结算影响。  
适用于`全仓``交割`  
>> settledPnl | String | 累计已结算收益（以结算价格计算）  
适用于`全仓``交割`  
>> uTime | String | 仓位信息的更新时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
> trades | Array of objects | 成交数据  
>> instId | String | 产品ID，如 `BTC-USDT`  
>> tradeId | String | 最新成交ID  
只有账户余额变化，只推balData；只有持仓余额发生变化，只推posData。    
\- 首次推送，只推用户持有的仓位和币种余额不为0的信息。如果数据太大无法在单个推送消息中发送，它将被分成多个消息发送。   
\- 例：比如按照所有币种订阅且用户有5个币种余额不为0 和20个仓位，那么首推全部5个币种余额列表和20个持仓信息列表；某个订单成交后，那么只推一个币种余额和对应的持仓信息。 

### 爆仓风险预警推送频道 

此推送频道仅作为风险提示，不建议作为策略交易的风险判断。  
在行情剧烈波动的情况下，可能会出现此消息推送的同时仓位已经被强平的可能性。  
预警会在某一个逐仓仓位有风险时推送。预警会在所有全仓仓位有风险时推送。  
该频道的并发连接受到如下规则限制：[WebSocket 连接限制](/docs-v5/zh/#overview-websocket-connection-count-limit)

#### 服务地址

/ws/v5/private (需要登录)

> 请求示例
    
    
    {
        "id": "1512",
        "op": "subscribe",
        "args": [{
            "channel": "liquidation-warning",
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
            url = "wss://ws.okx.com:8443/ws/v5/private",
            useServerTime=False
        )
        await ws.start()
        args = [
            {
              "channel": "liquidation-warning",
              "instType": "ANY"
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
`liquidation-warning`  
> instType | String | 是 | 产品类型  
`MARGIN`：币币杠杆  
`SWAP`：永续合约  
`FUTURES`：交割合约  
`OPTION`：期权  
`ANY`：全部  
> instFamily | String | 否 | 交易品种  
适用于`交割`/`永续`/`期权`  
> instId | String | 否 | 产品ID  
  
> 成功返回示例
    
    
    {
      "id": "1512",
      "event": "subscribe",
      "arg": {
        "channel": "liquidation-warning",
        "instType": "ANY"
      },
      "connId": "a4d3ae55"
    }
    

> 失败返回示例
    
    
    {
        "id": "1512",
        "event": "error",
        "code": "60012",
        "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{ \"channel\" : \"liquidation-warning\", \"instType\" : \"FUTURES\"}]}",
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
> channel | String | 是 | 频道名 ，`liquidation-warning`  
> instType | String | 是 | 产品类型  
`MARGIN`：币币杠杆  
`SWAP`：永续合约  
`FUTURES`：交割合约  
`OPTION`：期权   
`ANY`：全部  
> instFamily | String | 否 | 交易品种  
适用于`交割`/`永续`/`期权`  
> instId | String | 否 | 产品ID  
code | String | 否 | 错误码  
msg | String | 否 | 错误消息  
connId | String | 是 | WebSocket连接ID  
  
> 推送示例：单个
    
    
    {
        "arg":{
            "channel":"liquidation-warning",
            "uid": "77982378738415879",
            "instType":"FUTURES"
        },
        "data":[
            {
                "cTime":"1619507758793",
                "ccy":"ETH",
                "instId":"ETH-USD-210430",
                "instType":"FUTURES",
                "lever":"10",
                "markPx":"2353.849",
                "mgnMode":"isolated",
                "mgnRatio":"11.731726509588816",
                "pTime":"1619507761462",
                "pos":"1",
                "posCcy":"",
                "posId":"307173036051017730",
                "posSide":"long",
                "uTime":"1619507761462",
            }
        ]
    }
    

#### 推送数据参数

参数名 | 类型 | 描述  
---|---|---  
arg | Object | 订阅成功的频道  
> channel | String | 频道名  
> uid | String | 用户标识  
> instType | String | 产品类型  
> instFamily | String | 交易品种  
> instId | String | 产品ID  
data | Array of objects | 订阅的数据  
> instType | String | 产品类型  
> mgnMode | String | 保证金模式， `cross`：全仓 `isolated`：逐仓  
> posId | String | 持仓ID  
> posSide | String | 持仓方向  
`long`：开平仓模式开多  
`short`：开平仓模式开空  
`net`：买卖模式（`交割`/`永续`/`期权`：`pos`为正代表开多，`pos`为负代表开空。`币币杠杆`：`posCcy`为交易货币时，代表开多；`posCcy`为计价货币时，代表开空。）  
> pos | String | 持仓数量  
> posCcy | String | 持仓数量币种，仅适用于`币币杠杆`  
> instId | String | 产品ID，如 `BTC-USDT-SWAP`  
> lever | String | 杠杆倍数，不适用于`期权卖方`  
> markPx | String | 标记价格  
> mgnRatio | String | 维持保证金率  
> ccy | String | 占用保证金的币种  
> cTime | String | 持仓创建时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
> uTime | String | 最近一次持仓更新时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
> pTime | String | 持仓信息的推送时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
触发推送逻辑：爆仓预警和爆仓短信的触发逻辑一致 

### 账户greeks频道 

获取账户资产的greeks信息。当增加或者减少币种余额、持仓数量等会触发事件推送，周期性的也会有定时推送。  
该频道的并发连接受到如下规则限制：[WebSocket 连接限制](/docs-v5/zh/#overview-websocket-connection-count-limit)

#### 服务地址

/ws/v5/private (需要登录)

> 请求示例
    
    
    {
        "id": "1512",
        "op": "subscribe",
        "args": [{
            "channel": "account-greeks"
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
            url = "wss://ws.okx.com:8443/ws/v5/private",
            useServerTime=False
        )
        await ws.start()
        args = [{
            "channel": "account-greeks"
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
`account-greeks`  
> ccy | String | 否 | 保证金币种  
当用户指定了保证金，只有作为保证金的仓位发生变化的时候，才会触发事件推送。例如当指定了ccy = `BTC`，如果 `BTC-USDT-SWAP` 仓位发生变化，不会触发事件推送。  
  
> 成功返回示例
    
    
    {
        "id": "1512",
        "event": "subscribe",
        "arg": {
            "channel": "account-greeks"
        },
      "connId": "a4d3ae55"
    }
    

> 失败返回示例
    
    
    {
        "id": "1512",
        "event": "error",
        "code": "60012",
        "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{ \"channel\" : \"account-greeks\", \"ccy\" : \"BTC\"}]}",
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
`account-greeks`  
> ccy | String | 否 | 保证金币种  
code | String | 否 | 错误码  
msg | String | 否 | 错误消息  
connId | String | 是 | WebSocket连接ID  
  
> 推送示例：单个
    
    
    {
        "arg": {
            "channel": "account-greeks",
            "ccy": "BTC",
            "uid": "614488474791936"
        },
        "data": [
            {
                "ccy": "BTC",
                "deltaBS": "1.1246665401944310",
                "deltaPA": "-0.0074076183688949",
                "gammaBS": "0.0000000000000000",
                "gammaPA": "0.0148152367377899",
                "thetaBS": "2.0356991946421226",
                "thetaPA": "-0.0000000200174309",
                "ts": "1729179082006",
                "vegaBS": "0.0000000000000000",
                "vegaPA": "0.0000000000000000"
            }
        ]
    }
    

> 推送示例
    
    
    {
        "arg": {
            "channel": "account-greeks",
            "uid": "614488474791936"
        },
        "data": [
            {
                "ccy": "BTC",
                "deltaBS": "1.1246665403011684",
                "deltaPA": "-0.0074021163991037",
                "gammaBS": "0.0000000000000000",
                "gammaPA": "0.0148042327982075",
                "thetaBS": "2.1342098201092528",
                "thetaPA": "-0.0000000200876441",
                "ts": "1729179001692",
                "vegaBS": "0.0000000000000000",
                "vegaPA": "0.0000000000000000"
            },
            {
                "ccy": "ETH",
                "deltaBS": "0.3810670161698570",
                "deltaPA": "-0.0688347042402955",
                "gammaBS": "-0.0000000000230396",
                "gammaPA": "0.1376693483440320",
                "thetaBS": "0.3314776517141782",
                "thetaPA": "0.0000000001316008",
                "ts": "1729179001692",
                "vegaBS": "-0.0000000045069794",
                "vegaPA": "-0.0000000000017267"
            }
        ]
    }
    

#### 推送数据参数

**参数名** | **类型** | **描述**  
---|---|---  
arg | Object | 请求订阅的频道  
> channel | String | 频道名  
> uid | String | 用户标识  
data | Array of objects | 订阅的数据  
> deltaBS | String | 美金本位账户资产delta  
> deltaPA | String | 币本位账户资产delta  
> gammaBS | String | 美金本位账户资产gamma，仅适用于期权全仓  
> gammaPA | String | 币本位账户资产gamma，仅适用于期权全仓  
> thetaBS | String | 美金本位账户资产theta，仅适用于期权全仓  
> thetaPA | String | 币本位账户资产theta，仅适用于期权全仓  
> vegaBS | String | 美金本位账户资产vega，仅适用于期权全仓  
> vegaPA | String | 币本位账户资产vega，仅适用于期权全仓  
> ccy | String | 币种  
> ts | String | 获取greeks的时间，Unix时间戳的毫秒数格式，如 1597026383085  
账户greeks频道基于事件推送，并进行定时推送  
\- greeks频道的事件推送并非在事件发生时实时进行，而是按照大约50毫秒的固定时间窗口进行聚合推送。例如，在固定时间窗口内发生多个事件，系统将尽量聚合为一条消息并在固定时间窗口结束时进行推送。在数据量过大的情况下可能拆分为多条消息。   
\- 当用户订阅时指定了保证金币种(ccy)，只有作为保证金的仓位发生变化的时候，才会触发事件推送。例如订阅时指定了ccy=`BTC`，如果`BTC-USDT-SWAP`仓位发生变化，不会触发事件推送。   
\- 无论是否有greeks数据的变化，定时推送都会发送更新。    
\- 只推账户资产不为0的greeks数据。如果数据太大无法在单个推送消息中发送，它将被分成多个消息发送。   
\- 例：按照所有币种订阅且有5个币种资产都不为0，首次和定时推全部5个；账户的某个币种资产改变，那么账户greeks变更的触发只推这一个。