---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#trading-account-websocket-account-channel
anchor_id: trading-account-websocket-account-channel
api_type: WebSocket
updated_at: 2026-07-11 19:12:21.617388
---

# Account channel

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

---

# 账户频道

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