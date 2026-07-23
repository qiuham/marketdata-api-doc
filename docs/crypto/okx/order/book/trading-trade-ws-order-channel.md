---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#order-book-trading-trade-ws-order-channel
anchor_id: order-book-trading-trade-ws-order-channel
api_type: WebSocket
updated_at: 2026-07-23 19:21:17.954825
---

# WS / Order channel

Retrieve order information. Data will not be pushed when first subscribed. Data will only be pushed when there are new orders or order updates.  
  
  
Concurrent connection to this channel will be restricted by the following rules: [WebSocket connection count limit](/docs-v5/en/#overview-websocket-connection-count-limit).

#### URL Path

/ws/v5/private (required login)

> Request Example : single
    
    
    {
      "id": "1512",
      "op": "subscribe",
      "args": [
        {
          "channel": "orders",
          "instType": "FUTURES",
          "instId": "BTC-USD-200329"
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
              "channel": "orders",
              "instType": "FUTURES",
              "instId": "BTC-USD-200329"
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
          "channel": "orders",
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
        args =[
            {
              "channel": "orders",
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
`orders`  
> instType | String | Yes | Instrument type  
`SPOT`  
`MARGIN`  
`SWAP`  
`FUTURES`  
`OPTION`  
`EVENTS`  
`ANY`  
> instFamily | String | No | Instrument family  
Applicable to `FUTURES`/`SWAP`/`OPTION`  
> instId | String | No | Instrument ID  
  
> Successful Response Example : single
    
    
    {
      "id": "1512",
        "event": "subscribe",
        "arg": {
            "channel": "orders",
            "instType": "FUTURES",
            "instId": "BTC-USD-200329"
        },
        "connId": "a4d3ae55"
    }
    

> Successful Response Example
    
    
    {
      "id": "1512",
      "event": "subscribe",
      "arg": {
        "channel": "orders",
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
      "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{ \"channel\" : \"orders\", \"instType\" : \"FUTURES\"}]}",
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
`ANY`  
> instFamily | String | No | Instrument family  
> instId | String | No | Instrument ID  
code | String | No | Error code  
msg | String | No | Error message  
connId | String | Yes | WebSocket connection ID  
  
> Push Data Example
    
    
    {
        "arg": {
            "channel": "orders",
            "instType": "SPOT",
            "instId": "BTC-USDT",
            "uid": "614488474791936"
        },
        "data": [
            {
                "accFillSz": "0.001",
                "algoClOrdId": "",
                "algoId": "",
                "amendResult": "",
                "amendSource": "",
                "avgPx": "31527.1",
                "cancelSource": "",
                "category": "normal",
                "ccy": "",
                "clOrdId": "",
                "code": "0",
                "cTime": "1654084334977",
                "execType": "M",
                "fee": "-0.02522168",
                "feeCcy": "USDT",
                "fillFee": "-0.02522168",
                "fillFeeCcy": "USDT",
                "fillNotionalUsd": "31.50818374",
                "fillPx": "31527.1",
                "fillSz": "0.001",
                "fillPnl": "0.01",
                "fillTime": "1654084353263",
                "fillPxVol": "",
                "fillPxUsd": "",
                "fillMarkVol": "",
                "fillFwdPx": "",
                "fillMarkPx": "",
                "fillIdxPx": "",
                "instId": "BTC-USDT",
                "instType": "SPOT",
                "lever": "0",
                "msg": "",
                "notionalUsd": "31.50818374",
                "ordId": "452197707845865472",
                "ordType": "limit",
                "pnl": "0",
                "posSide": "",
                "px": "31527.1",
                "pxUsd":"",
                "pxVol":"",
                "pxType":"",
                "quickMgnType": "",
                "rebate": "0",
                "rebateCcy": "BTC",
                "reduceOnly": "false",
                "reqId": "",
                "side": "sell",
                "attachAlgoClOrdId": "",
                "slOrdPx": "",
                "slTriggerPx": "",
                "slTriggerPxType": "last",
                "source": "",
                "state": "filled",
                "stpId": "",
                "stpMode": "",
                "sz": "0.001",
                "tag": "",
                "tdMode": "cash",
                "tgtCcy": "",
                "tpOrdPx": "",
                "tpTriggerPx": "",
                "tpTriggerPxType": "last",
                "attachAlgoOrds": [],
                "tradeId": "242589207",
                "tradeQuoteCcy": "USDT",
                "lastPx": "38892.2",
                "uTime": "1654084353264",
                "isTpLimit": "false",
                "linkedAlgoOrd": {
                    "algoId": ""
                }
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
`SPOT`  
`MARGIN`  
`SWAP`  
`FUTURES`  
`OPTION`  
`EVENTS`  
> instFamily | String | Instrument family  
> instId | String | Instrument ID  
data | Array of objects | Subscribed data  
> instType | String | Instrument type  
`SPOT`  
`MARGIN`  
`SWAP`  
`FUTURES`  
`OPTION`  
`EVENTS`  
> instId | String | Instrument ID  
> tgtCcy | String | Order quantity unit setting for `sz`  
`base_ccy`: Base currency ,`quote_ccy`: Quote currency   
Only applicable to `SPOT` Market orders.   
Default is `quote_ccy` for buy, `base_ccy` for sell  
> ccy | String | Margin currency   
Applicable to all `isolated` `MARGIN` orders and `cross` `MARGIN` orders in `Futures mode`, `FUTURES` and `SWAP` contracts.  
> ordId | String | Order ID  
> clOrdId | String | Client Order ID as assigned by the client  
> tag | String | Order tag  
> px | String | Price   
For options, use coin as unit (e.g. BTC, ETH)  
> pxUsd | String | Options price in USDOnly applicable to options; return "" for other instrument types  
> pxVol | String | Implied volatility of the options orderOnly applicable to options; return "" for other instrument types  
> pxType | String | Price type of options   
`px`: Place an order based on price, in the unit of coin (the unit for the request parameter px is BTC or ETH)   
`pxVol`: Place an order based on pxVol   
`pxUsd`: Place an order based on pxUsd, in the unit of USD (the unit for the request parameter px is USD)  
> sz | String | Quantity to buy or sell  
> notionalUsd | String | Estimated national value in `USD` of order  
> ordType | String | Order type   
`market`: market order   
`limit`: limit order   
`post_only`: Post-only order   
`fok`: Fill-or-kill order   
`ioc`: Immediate-or-cancel order   
`optimal_limit_ioc`: Market order with immediate-or-cancel order (applicable only to Expiry Futures and Perpetual Futures)  
`mmp`: Market Maker Protection (only applicable to Option in Portfolio Margin mode)  
`mmp_and_post_only`: Market Maker Protection and Post-only order(only applicable to Option in Portfolio Margin mode).   
`op_fok`: Simple options (fok)   
`elp`: Enhanced Liquidity Program order  
> side | String | Order side, `buy` `sell`  
> posSide | String | Position side   
`net`   
`long` or `short` Only applicable to `FUTURES`/`SWAP`  
> tdMode | String | Trade mode, `cross`: cross `isolated`: isolated `cash`: cash  
> fillPx | String | Filled price for the current update.  
> tradeId | String | Trade ID for the current update.  
> fillSz | String | Filled quantity for the current udpate.   
The unit is `base_ccy` for SPOT and MARGIN, e.g. BTC-USDT, the unit is BTC; For market orders, the unit both is `base_ccy` when the tgtCcy is `base_ccy` or `quote_ccy`;  
The unit is contract for `FUTURES`/`SWAP`/`OPTION`  
> fillPnl | String | Filled profit and loss for the current udpate, applicable to orders which have a trade and aim to close position. It always is 0 in other conditions  
> fillTime | String | Filled time for the current udpate.  
> fillFee | String | Filled fee amount or rebate amount for the current udpate. :   
Negative number represents the user transaction fee charged by the platform;   
Positive number represents rebate  
> fillFeeCcy | String | Filled fee currency or rebate currency for the current udpate..  
It is fee currency when fillFee is less than 0; It is rebate currency when fillFee>=0.  
> fillPxVol | String | Implied volatility when filled   
Only applicable to options; return "" for other instrument types  
> fillPxUsd | String | Options price when filled, in the unit of USD   
Only applicable to options; return "" for other instrument types  
> fillMarkVol | String | Mark volatility when filled   
Only applicable to options; return "" for other instrument types  
> fillFwdPx | String | Forward price when filled   
Only applicable to options; return "" for other instrument types  
> fillMarkPx | String | Mark price when filled   
Applicable to `FUTURES`, `SWAP`, `OPTION`  
> fillIdxPx | String | Index price at the moment of trade execution   
For cross currency spot pairs, it returns baseCcy-USDT index price. For example, for LTC-ETH, this field returns the index price of LTC-USDT.  
> execType | String | Liquidity taker or maker for the current update, T: taker M: maker  
> accFillSz | String | Accumulated fill quantity  
The unit is `base_ccy` for SPOT and MARGIN, e.g. BTC-USDT, the unit is BTC; For market orders, the unit both is `base_ccy` when the tgtCcy is `base_ccy` or `quote_ccy`;  
The unit is contract for `FUTURES`/`SWAP`/`OPTION`  
> fillNotionalUsd | String | Filled notional value in `USD` of order  
> avgPx | String | Average filled price. If none is filled, it will return `0`.  
> state | String | Order state   
`canceled`  
`live`   
`partially_filled`   
`filled`  
`mmp_canceled`  
> lever | String | Leverage, from `0.01` to `125`.   
Only applicable to `MARGIN/FUTURES/SWAP`  
> attachAlgoClOrdId | String | Client-supplied Algo ID when placing order with attached TP/SL or trailing stop.  
> tpTriggerPx | String | Take-profit trigger price, it  
> tpTriggerPxType | String | Take-profit trigger price type.   
`last`: last price  
`index`: index price  
`mark`: mark price  
> tpOrdPx | String | Take-profit order price, it  
> slTriggerPx | String | Stop-loss trigger price, it  
> slTriggerPxType | String | Stop-loss trigger price type.   
`last`: last price  
`index`: index price  
`mark`: mark price  
> slOrdPx | String | Stop-loss order price, it  
> attachAlgoOrds | Array of objects | Attached TP/SL or trailing stop order information  
>> attachAlgoId | String | The order ID of the attached TP/SL or trailing stop order. It can be used to identify the attached order when amending. It will not be posted to algoId when placing the attached algo order after the general order is filled completely.  
>> attachAlgoClOrdId | String | Client-supplied Algo ID when placing order with attached TP/SL or trailing stop  
A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters.  
It will be posted to `algoClOrdId` when placing the attached algo order once the general order is filled completely.  
>> tpOrdKind | String | TP order kind  
`condition`  
`limit`  
>> tpTriggerPx | String | Take-profit trigger price.  
>> tpTriggerRatio | String | Take-profit trigger ratio, 0.3 represents 30%. Only applicable to `FUTURES`/`SWAP` contracts.  
>> tpTriggerPxType | String | Take-profit trigger price type.   
`last`: last price  
`index`: index price  
`mark`: mark price  
>> tpOrdPx | String | Take-profit order price.  
>> slTriggerPx | String | Stop-loss trigger price.  
>> slTriggerRatio | String | Stop-loss trigger ratio, 0.3 represents 30%. Only applicable to `FUTURES`/`SWAP` contracts.  
>> slTriggerPxType | String | Stop-loss trigger price type.   
`last`: last price  
`index`: index price  
`mark`: mark price  
>> slOrdPx | String | Stop-loss order price.  
>> sz | String | Size. Only applicable to TP order of split TPs  
>> amendPxOnTriggerType | String | Whether to enable Cost-price SL. Only applicable to SL order of split TPs.   
`0`: disable, the default value   
`1`: Enable  
>> callbackRatio | String | Callback ratio, e.g. `0.05` represents 5%  
>> callbackSpread | String | Callback spread (price distance)  
>> activePx | String | Activation price  
> linkedAlgoOrd | Object | Linked SL order detail, only applicable to TP limit order of one-cancels-the-other order(oco)  
>> algoId | Object | Algo ID  
> stpId | String | ~~Self trade prevention ID  
Return "" if self trade prevention is not applicable~~ (Deprecated)  
> stpMode | String | Self trade prevention mode  
> feeCcy | String | Fee currency  
For maker sell orders of Spot and Margin, this represents the quote currency. For all other cases, it represents the currency in which fees are charged.  
> fee | String | Fee amount  
For Spot and Margin (excluding maker sell orders): accumulated fee charged by the platform, always negative  
For maker sell orders in Spot and Margin, Expiry Futures, Perpetual Futures and Options: accumulated fee and rebate (always in quote currency for maker sell orders in Spot and Margin)  
> rebateCcy | String | Rebate currency  
For maker sell orders of Spot and Margin, this represents the base currency. For all other cases, it represents the currency in which rebates are paid.  
> rebate | String | Rebate amount, only applicable to Spot and Margin  
For maker sell orders: ~~Accumulated fee and~~ rebate amount in the unit of base currency.  
For all other cases, it represents the maker rebate amount, always positive, return "" if no rebate.  
> pnl | String | Profit and loss (excluding the fee).  
applicable to orders which have a trade and aim to close position. It always is 0 in other conditions.   
For liquidation under cross margin mode, it will include liquidation penalties.  
> source | String | Order source  
`6`: The normal order triggered by the `trigger order`  
`7`:The normal order triggered by the `TP/SL order`   
`13`: The normal order triggered by the algo order  
`25`:The normal order triggered by the `trailing stop order`  
`34`: The normal order triggered by the chase order  
> cancelSource | String | Source of the order cancellation.  
Valid values and the corresponding meanings are:  
`0`: Order canceled by system  
`1`: Order canceled by user  
`2`: Order canceled: Pre reduce-only order canceled, due to insufficient margin in user position  
`3`: Order canceled: Risk cancellation was triggered. Pending order was canceled due to insufficient maintenance margin ratio and forced-liquidation risk.  
`4`: Order canceled: Borrowings of crypto reached hard cap, order was canceled by system.  
`6`: Order canceled: ADL order cancellation was triggered. Pending order was canceled due to a low margin ratio and forced-liquidation risk.   
`7`: Order canceled: Futures contract delivery.   
`9`: Order canceled: Insufficient balance after funding fees deducted.   
`10`: Order canceled: Option contract expiration.  
`13`: Order canceled: FOK order was canceled due to incompletely filled.  
`14`: Order canceled: IOC order was partially canceled due to incompletely filled.  
`15`: Order canceled: The order price is beyond the limit  
`17`: Order canceled: Close order was canceled, due to the position was already closed at market price.  
`20`: Cancel all after triggered  
`21`: Order canceled: The TP/SL order was canceled because the position had been closed  
`22` Order canceled: Due to a better price was available for the order in the same direction, the current operation reduce-only order was automatically canceled  
`23` Order canceled: Due to a better price was available for the order in the same direction, the existing reduce-only order was automatically canceled  
`27`: Order canceled: Price limit verification failed because the price difference between counterparties exceeds 5%   
`31`: The post-only order will take liquidity in taker orders   
`32`: Self trade prevention   
`33`: The order exceeds the maximum number of order matches per taker order  
`36`: Your TP limit order was canceled because the corresponding SL order was triggered.   
`37`: Your TP limit order was canceled because the corresponding SL order was canceled.  
`38`: You have canceled market maker protection (MMP) orders.  
`39`: Your order was canceled because market maker protection (MMP) was triggered.   
`42`: Your order was canceled because the difference between the initial and current best bid or ask prices reached the maximum chase difference.  
`43`: Order cancelled because the buy order price is higher than the index price or the sell order price is lower than the index price.  
`44`: Your order was canceled because your available balance of this crypto was insufficient for auto conversion. Auto conversion was triggered when the total collateralized liabilities for this crypto reached the platform’s risk control limit.   
`45`: Order cancelled because ELP order price verification failed  
`46`: delta reducing cancel orders  
> amendSource | String | Source of the order amendation.   
`1`: Order amended by user  
`2`: Order amended by user, but the order quantity is overriden by system due to reduce-only  
`4`: Order quantity amended by system due to reduce-only, including a new order placed by the user whose quantity is overriden by the system, and an existing pending order amended by the system due to other pending orders  
`5`: Order modification due to changes in options px, pxVol, or pxUsd as a result of following variations. For example, when iv = 60, USD and px are anchored at iv = 60, the changes in USD or px lead to modification.  
> category | String | Category   
`normal`   
`twap`   
`adl`   
`full_liquidation`   
`partial_liquidation`  
`delivery`   
`ddh`: Delta dynamic hedge  
`auto_conversion`  
> isTpLimit | String | Whether it is TP limit order. true or false  
> uTime | String | Update time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
> cTime | String | Creation time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
> reqId | String | Client Request ID as assigned by the client for order amendment. "" will be returned if there is no order amendment.  
> amendResult | String | The result of amending the order   
`-1`: failure   
`0`: success   
`1`: Automatic cancel (amendment request returned success but amendment subsequently failed then automatically canceled by the system)   
`2`: Automatic amendation successfully, only applicable to pxVol and pxUsd orders of Option.  
When amending the order through API and `cxlOnFail` is set to `true` in the order amendment request but the amendment is rejected, "" is returned.   
When amending the order through API, the order amendment acknowledgement returns success and the amendment subsequently failed, `-1` will be returned if `cxlOnFail` is set to `false`, `1` will be returned if `cxlOnFail` is set to `true`.   
When amending the order through Web/APP and the amendment failed, `-1` will be returned.  
> reduceOnly | String | Whether the order can only reduce the position size. Valid options: `true` or `false`.  
> quickMgnType | String | ~~Quick Margin type, Only applicable to Quick Margin Mode of isolated margin  
`manual`, `auto_borrow`, `auto_repay`~~ (Deprecated)  
> algoClOrdId | String | Client-supplied Algo ID. There will be a value when algo order attaching `algoClOrdId` is triggered, or it will be "".  
> algoId | String | Algo ID. There will be a value when algo order is triggered, or it will be "".  
> lastPx | String | Last price  
> code | String | Error Code, the default is 0  
> msg | String | Error Message, The default is ""  
> tradeQuoteCcy | String | The quote currency used for trading.  
> outcome | String | The market outcome the user traded on.  
`yes`  
`no`  
Only applicable to `EVENTS`  
For market orders, it's likely the orders channel will show order state as "filled" while showing the "last filled quantity (fillSz)" as 0.  In exceptional cases, the same message may be sent multiple times (perhaps with the different uTime) . The following guidelines are advised:  
  
1\. If a `tradeId` is present, it means a fill. Each `tradeId` should only be returned once per instrument ID, and the later messages that have the same `tradeId` should be discarded.  
2\. If `tradeId` is absent and the `state` is "filled," it means that the `SPOT`/`MARGIN` market order is fully filled. For messages with the same `ordId`, process only the first filled message and discard any subsequent messages. State = filled is the terminal state of an order.  
3\. If the state is `canceled` or `mmp_canceled`, it indicates that the order has been canceled. For cancellation messages with the same `ordId`, process the first one and discard later messages. State = canceled / mmp_canceled is the terminal state of an order.  
4\. If `reqId` is present, it indicates a response to a user-requested order modification. It is recommended to use a unique `reqId` for each modification request. For modification messages with the same `reqId`, process only the first message received and discard subsequent messages.  The definitions for fillPx, tradeId, fillSz, fillPnl, fillTime, fillFee, fillFeeCcy, and execType differ between the REST order information endpoints and the orders channel.  The definitions for fillPx, tradeId, fillSz, fillPnl, fillTime, fillFee, fillFeeCcy, and execType differ between the REST order information endpoints and the orders channel.  Unlike futures contracts, option positions are automatically exercised or expire at maturity. The rights then terminate and no closing orders are generated. Therefore, this channel will not push any closing-order updates for expired options.

---

# WS / 订单频道

获取订单信息，首次订阅不推送，只有当下单、订单变更时，推送数据  
该频道的并发连接受到如下规则限制：[WebSocket 连接限制](/docs-v5/zh/#overview-websocket-connection-count-limit)  
  
#### 服务地址

/ws/v5/private (需要登录)

> 请求示例：单个
    
    
    {
        "id": "1512",
        "op": "subscribe",
        "args": [{
            "channel": "orders",
            "instType": "FUTURES",
            "instId": "BTC-USD-200329"
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
            "channel": "orders",
            "instType": "FUTURES",
            "instId": "BTC-USD-200329"
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
        "args": [{
            "channel": "orders",
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
        args = [{
            "channel": "orders",
            "instType": "FUTURES",
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
`orders`  
> instType | String | 是 | 产品类型  
`SPOT`：币币  
`MARGIN`：币币杠杆  
`SWAP`：永续合约  
`FUTURES`：交割合约  
`OPTION`：期权  
`EVENTS`：事件合约  
`ANY`：全部  
> instFamily | String | 否 | 交易品种  
适用于`交割`/`永续`/`期权`  
> instId | String | 否 | 产品ID  
  
> 成功返回示例：单个
    
    
    {
        "id": "1512",
        "event": "subscribe",
        "arg": {
            "channel": "orders",
            "instType": "FUTURES",
            "instId": "BTC-USD-200329"
        },
        "connId": "a4d3ae55"
    }
    

> 成功返回示例
    
    
    {
        "id": "1512",
        "event": "subscribe",
        "arg": {
            "channel": "orders",
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
        "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{ \"channel\" : \"orders\", \"instType\" : \"FUTURES\"}]}",
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
`ANY`：全部  
> instFamily | String | 否 | 交易品种  
适用于`交割`/`永续`/`期权`  
> instId | String | 否 | 产品ID  
code | String | 否 | 错误码  
msg | String | 否 | 错误消息  
connId | String | 是 | WebSocket连接ID  
  
> 推送示例
    
    
    {
        "arg": {
            "channel": "orders",
            "instType": "SPOT",
            "instId": "BTC-USDT",
            "uid": "614488474791936"
        },
        "data": [
            {
                "accFillSz": "0.001",
                "amendResult": "",
                "avgPx": "31527.1",
                "cTime": "1654084334977",
                "category": "normal",
                "ccy": "",
                "clOrdId": "",
                "code": "0",
                "execType": "M",
                "fee": "-0.02522168",
                "feeCcy": "USDT",
                "fillFee": "-0.02522168",
                "fillFeeCcy": "USDT",
                "fillNotionalUsd": "31.50818374",
                "fillPx": "31527.1",
                "fillSz": "0.001",
                "fillPnl": "0.01",
                "fillTime": "1654084353263",
                "fillPxVol": "",
                "fillPxUsd": "",
                "fillMarkVol": "",
                "fillFwdPx": "",
                "fillMarkPx": "",
                "fillIdxPx": "",
                "instId": "BTC-USDT",
                "instType": "SPOT",
                "lever": "0",
                "msg": "",
                "notionalUsd": "31.50818374",
                "ordId": "452197707845865472",
                "ordType": "limit",
                "pnl": "0",
                "posSide": "",
                "px": "31527.1",
                "pxUsd":"",
                "pxVol":"",
                "pxType":"",
                "rebate": "0",
                "rebateCcy": "BTC",
                "reduceOnly": "false",
                "reqId": "",
                "side": "sell",
                "attachAlgoClOrdId": "",
                "slOrdPx": "",
                "slTriggerPx": "",
                "slTriggerPxType": "last",
                "source": "",
                "state": "filled",
                "stpId": "",
                "stpMode": "",
                "sz": "0.001",
                "tag": "",
                "tdMode": "cash",
                "tgtCcy": "",
                "tpOrdPx": "",
                "tpTriggerPx": "",
                "tpTriggerPxType": "last",
                "tradeId": "242589207",
                "tradeQuoteCcy": "USDT",
                "lastPx": "38892.2",
                "quickMgnType": "",
                "algoClOrdId": "",
                "attachAlgoOrds": [],
                "algoId": "",
                "amendSource": "",
                "cancelSource": "",
                "isTpLimit": "false",
                "uTime": "1654084353264",
                "linkedAlgoOrd": {
                    "algoId": ""
                }
            }
        ]
    }
    

#### 推送数据参数

**参数名** | **类型** | **描述**  
---|---|---  
arg | Object | 订阅成功的频道  
> channel | String | 频道名  
> uid | String | 用户标识  
> instType | String | 产品类型  
`SPOT`：币币  
`MARGIN`：币币杠杆  
`SWAP`：永续合约  
`FUTURES`：交割合约  
`OPTION`：期权  
`EVENTS`：事件合约  
> instFamily | String | 交易品种  
> instId | String | 产品ID  
data | Array of objects | 订阅的数据  
> instType | String | 产品类型  
`SPOT`：币币  
`MARGIN`：币币杠杆  
`SWAP`：永续合约  
`FUTURES`：交割合约  
`OPTION`：期权  
`EVENTS`：事件合约  
> instId | String | 产品ID  
> ccy | String | 保证金币种，适用于`逐仓杠杆`及`合约模式`下的`全仓杠杆`订单以及交割、永续和期权合约订单。  
> ordId | String | 订单ID  
> clOrdId | String | 由用户设置的订单ID来识别您的订单  
> tag | String | 订单标签  
> px | String | 委托价格，对于期权，以币(如BTC, ETH)为单位  
> pxUsd | String | 期权价格，以USD为单位   
仅适用于期权，其他业务线返回空字符串""  
> pxVol | String | 期权订单的隐含波动率   
仅适用于期权，其他业务线返回空字符串""  
> pxType | String | 期权的价格类型   
`px`：代表按价格下单，单位为币 (请求参数 px 的数值单位是BTC或ETH)   
`pxVol`：代表按pxVol下单   
`pxUsd`：代表按照pxUsd下单，单位为USD (请求参数px 的数值单位是USD)  
> sz | String | 委托数量  
> notionalUsd | String | 委托单预估美元价值  
> fillNotionalUsd | String | 委托单已成交的美元价值  
> ordType | String | 订单类型   
`market`：市价单   
`limit`：限价单   
`post_only`：只做maker单   
`fok`：全部成交或立即取消单  
`ioc`：立即成交并取消剩余单   
`optimal_limit_ioc`：市价委托立即成交并取消剩余（仅适用交割、永续）  
`mmp`：做市商保护(仅适用于组合保证金账户模式下的期权订单)  
`mmp_and_post_only`：做市商保护且只做maker单(仅适用于组合保证金账户模式下的期权订单)   
`op_fok`：期权简选（全部成交或立即取消）  
`elp`：流动性增强计划订单  
> side | String | 订单方向，`buy` `sell`  
> posSide | String | 持仓方向  
`long`：开平仓模式开多  
`short`：开平仓模式开空  
`net`：买卖模式  
> tdMode | String | 交易模式  
保证金模式 `isolated`：逐仓 `cross`：全仓   
非保证金模式 `cash`：现金  
> tgtCcy | String | 市价单委托数量`sz`的单位  
`base_ccy`: 交易货币 `quote_ccy`：计价货币  
> fillPx | String | 当前推送消息的成交价格  
> tradeId | String | 当前推送消息的成交ID  
> fillSz | String | 当前推送消息的成交数量  
对于`币币`和`杠杆`，单位为交易货币，如 BTC-USDT, 单位为 BTC；对于市价单，无论`tgtCcy`是`base_ccy`，还是`quote_ccy`，单位均为交易货币；  
对于交割、永续以及期权，单位为张。  
> fillPnl | String | 当前推送消息的成交收益，适用于有成交的平仓订单。其他情况均为0。  
> fillTime | String | 当前推送消息的成交时间  
> fillFee | String | 当前推送消息的成交手续费金额或者返佣金额：  
手续费扣除 为 ‘负数’，如 -0.01 ；   
手续费返佣 为 ‘正数’，如 0.01  
> fillFeeCcy | String | 当前推送消息的成交手续费币种或者返佣币种。  
如果fillFee小于0，为手续费币种；如果fillFee大于等于0，为返佣币种  
> fillPxVol | String | 成交时的隐含波动率仅适用于期权，其他业务线返回空字符串""  
> fillPxUsd | String | 成交时的期权价格，以USD为单位仅适用于期权，其他业务线返回空字符串""  
> fillMarkVol | String | 成交时的标记波动率，仅适用于期权，其他业务线返回空字符串""  
> fillFwdPx | String | 成交时的远期价格，仅适用于期权，其他业务线返回空字符串""  
> fillMarkPx | String | 成交时的标记价格，仅适用于 `交割`/`永续`/`期权`  
> fillIdxPx | String | 交易执行时的指数价格   
对于交叉现货币对，返回 baseCcy-USDT 的指数价格。 例如LTC-ETH，该字段返回LTC-USDT的指数价格。  
> execType | String | 当前推送消息成交的流动性方向 T：taker M：maker  
> accFillSz | String | 累计成交数量  
对于`币币`和`杠杆`，单位为交易货币，如 BTC-USDT, 单位为 BTC；对于市价单，无论`tgtCcy`是`base_ccy`，还是`quote_ccy`，单位均为交易货币；  
对于交割、永续以及期权，单位为张。  
> avgPx | String | 成交均价，如果成交数量为0，该字段也为0  
> state | String | 订单状态   
`canceled`：撤单成功  
`live`：等待成交  
`partially_filled`：部分成交   
`filled`：完全成交  
`mmp_canceled`：做市商保护机制导致的自动撤单  
> lever | String | 杠杆倍数，0.01到125之间的数值，仅适用于 `币币杠杆/交割/永续`  
> attachAlgoClOrdId | String | 下单附带止盈止损或移动止盈止损时，客户自定义的策略订单ID  
> tpTriggerPx | String | 止盈触发价  
> tpTriggerPxType | String | 止盈触发价类型  
`last`：最新价格  
`index`：指数价格  
`mark`：标记价格  
> tpOrdPx | String | 止盈委托价，止盈委托价格为`-1`时，执行市价止盈  
> slTriggerPx | String | 止损触发价  
> slTriggerPxType | String | 止损触发价类型  
`last`：最新价格  
`index`：指数价格  
`mark`：标记价格  
> slOrdPx | String | 止损委托价，止损委托价格为`-1`时，执行市价止损  
> attachAlgoOrds | Array of objects | 附带止盈止损或移动止盈止损订单信息  
>> attachAlgoId | String | 附带止盈止损或移动止盈止损的订单ID，改单时，可用来标识该笔附带止盈止损订单。下附带策略委托单时，该值不会传给 algoId  
>> attachAlgoClOrdId | String | 下单附带止盈止损或移动止盈止损时，客户自定义的策略订单ID  
>> tpOrdKind | String | 止盈订单类型  
`condition`: 条件单  
`limit`: 限价单  
>> tpTriggerPx | String | 止盈触发价  
>> tpTriggerRatio | String | 止盈触发比例，0.3 代表 30%   
仅适用于`交割`/`永续`合约  
>> tpTriggerPxType | String | 止盈触发价类型  
`last`：最新价格  
`index`：指数价格  
`mark`：标记价格  
>> tpOrdPx | String | 止盈委托价  
>> slTriggerPx | String | 止损触发价  
>> slTriggerRatio | String | 止损触发比例，0.3 代表 30%   
仅适用于`交割`/`永续`合约  
>> slTriggerPxType | String | 止损触发价类型  
`last`：最新价格  
`index`：指数价格  
`mark`：标记价格  
>> slOrdPx | String | 止损委托价  
>> sz | String | 张数。仅适用于“多笔止盈”的止盈订单  
>> amendPxOnTriggerType | String | 是否启用开仓价止损，仅适用于分批止盈的止损订单  
`0`：不开启，默认值   
`1`：开启  
>> callbackRatio | String | 回调幅度的比例，如 `0.05` 代表 5%  
>> callbackSpread | String | 回调幅度的价距  
>> activePx | String | 激活价格  
> linkedAlgoOrd | Object | 止损订单信息，仅适用于包含限价止盈单的双向止盈止损订单，触发后生成的普通订单  
>> algoId | Object | 策略订单唯一标识  
> stpId | String | ~~自成交保护ID  
如果自成交保护不适用则返回""~~（已弃用）  
> stpMode | String | 自成交保护模式  
> feeCcy | String | 手续费币种  
对于币币和杠杆的挂单卖单，表示计价币种；其他情况下，表示收取手续费的币种  
> fee | String | 手续费金额  
对于币币和杠杆（除挂单卖单外）：平台收取的累计手续费，始终为负数。  
对于币币和杠杆的挂单卖单、交割、永续和期权：累计手续费和返佣（币币和杠杆挂单卖单始终以计价币种计算）  
> rebateCcy | String | 返佣币种  
对于币币和杠杆的挂单卖单，表示交易币种；其他情况下，表示支付返佣的币种  
> rebate | String | 返佣金额，仅适用于币币和杠杆  
对于挂单卖单：以交易币种为单位的~~累计手续费和~~ 返佣金额。  
其他情况下，表示挂单返佣金额，始终为正数，如无返佣时返回""。  
> pnl | String | 收益(不包括手续费)  
适用于有成交的平仓订单，其他情况均为0   
对于合约全仓爆仓，将包含相应强平惩罚金  
> source | String | 订单来源  
`6`：计划委托策略触发后的生成的普通单  
`7`：止盈止损策略触发后的生成的普通单  
`13`：策略委托单触发后的生成的普通单  
`25`：移动止盈止损策略触发后的生成的普通单  
`34`: 追逐限价委托生成的普通单  
> cancelSource | String | 订单取消的来源  
有效值及对应的含义是：  
`0`: 已撤单：系统撤单  
`1`: 用户主动撤单  
`2`: 已撤单：预减仓撤单，用户保证金不足导致挂单被撤回  
`3`: 已撤单：风控撤单，用户保证金不足有爆仓风险，导致挂单被撤回  
`4`: 已撤单：币种借币量达到平台硬顶，系统已撤回该订单  
`6`: 已撤单：触发 ADL 撤单，用户维持保证金率较低且有爆仓风险，导致挂单被撤回  
`7`: 已撤单：交割合约到期  
`9`: 已撤单：扣除资金费用后可用余额不足，系统已撤回该订单   
`10`: 已撤单：期权合约到期  
`13`: 已撤单：FOK 委托订单未完全成交，导致挂单被完全撤回  
`14`: 已撤单：IOC 委托订单未完全成交，仅部分成交，导致部分挂单被撤回  
`15`: 已撤单：该订单委托价不在限价范围内  
`17`: 已撤单：平仓单被撤单，由于仓位已被市价全平  
`20`: 系统倒计时撤单  
`21`: 已撤单：相关仓位被完全平仓，系统已撤销该止盈止损订单  
`22` 已撤单：存在更优价格的同方向订单，系统自动撤销当前操作的只减仓订单  
`23` 已撤单：存在更优价格的同方向订单，系统自动撤销已存在的只减仓订单  
`27`: 成交滑点超过5%，触发成交差价保护导致系统撤单   
`31`: 当前只挂单订单 (Post only) 将会吃掉挂单深度   
`32`: 自成交保护   
`33`: 当前 taker 订单匹配的订单数量超过最大限制  
`36`: 关联止损被触发，撤销限价止盈   
`37`: 关联止损被撤销，撤销限价止盈   
`38`: 您已撤销做市商保护 (MMP) 类型订单  
`39`: 因做市商保护 (MMP) 被触发，该类型订单已被撤销  
`42`: 初始下单价格与最新的买一或卖一价已达到最大追逐距离，您的订单已被自动取消  
`43`: 由于买单价格高于指数价格或卖单价格低于指数价格，导致系统撤单  
`44`：由于该币种的可用余额不足，无法在触发自动换币后进行兑换，您的订单已撤销，撤销订单后恢复的余额将用于自动换币。当该币种的总抵押借贷量达到平台抵押借贷风控上限时，则会触发自动换币。  
`45`：ELP订单价格校验失败  
`46`：由于降低Delta而导致的撤单  
> amendSource | String | 订单修改的来源  
`1`: 用户主动改单，改单成功  
`2`: 用户主动改单，并且当前这笔订单被只减仓修改，改单成功  
`4`: 订单数量被系统按只减仓修改，改单成功，包括：用户主动下单后当前这笔订单被只减仓修改，以及用户当前已存在的挂单（非当前操作的订单）被只减仓修改  
`5`：期权 px, pxVol 或 pxUsd 的跟随变动导致的改单，比如 iv=60，USD，px 锚定iv=60 时，USD, px 产生变动时的改单  
> category | String | 订单种类分类  
`normal`：普通委托订单种类   
`twap`：TWAP订单种类  
`adl`：ADL订单种类  
`full_liquidation`：爆仓订单种类  
`partial_liquidation`：减仓订单种类  
`delivery`：交割  
`ddh`：对冲减仓类型订单  
`auto_conversion`：抵押借币自动还币订单  
> isTpLimit | String | 是否为限价止盈，true 或 false.  
> uTime | String | 订单更新时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
> cTime | String | 订单创建时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
> reqId | String | 修改订单时使用的request ID，如果没有修改，该字段为""  
> amendResult | String | 修改订单的结果  
`-1`：失败  
`0`：成功  
`1`：自动撤单（修改请求返回成功但最终改单失败导致自动撤销）  
`2`: 自动改单成功，仅适用于期权pxUsd和pxVol订单的自动改单   
通过API修改订单时，如果`cxlOnFail`设置为`true`且修改返回结果为失败时，则返回 ""  
通过API修改订单时，如果修改返回结果为成功但修改最终失败后，当`cxlOnFail`设置为`false`时返回 `-1`;当`cxlOnFail`设置为`true`时则返回`1`  
通过Web/APP修改订单时，如果修改失败后，则返回`-1`  
> reduceOnly | String | 是否只减仓，`true` 或 `false`  
> quickMgnType | String | ~~一键借币类型，仅适用于杠杆逐仓的一键借币模式  
`manual`：手动，`auto_borrow`：自动借币，`auto_repay`：自动还币~~（已弃用）  
> algoClOrdId | String | 客户自定义策略订单ID。策略订单触发，且策略单有`algoClOrdId`时有值，否则为"",  
> algoId | String | 策略委托单ID，策略订单触发时有值，否则为""  
> lastPx | String | 最新成交价  
> code | String | 错误码，默认为0  
> msg | String | 错误消息，默认为""  
> tradeQuoteCcy | String | 用于交易的计价币种。  
> outcome | String | 用户交易的市场结果方向。  
`yes`  
`no`  
仅适用于 `EVENTS`  
对于市价委托，订单频道推送消息会出现状态为“完全成交”，但最新成交数量 (fillSz) 为 0 的情况。  极端情况下，会出现同一条消息重复推送的情况（`uTime` 可能会不一样），建议做如下处理：  
  
* 当`tradeId`有值时，代表成交，对于同一`tradeId`，请以第一条推送消息为准，忽略后续的推送消息；  
* 当`tradeId`没有值且 `state` 为`filled`时，代表币币/杠杆市价单关闭，对于同一`ordId`的完全成交（state:filled）推送消息，请以第一条成交推送消息为准，忽略后续的推送消息；  
* 当`state`为`canceled`或者`mmp_canceled`时，代表订单撤销，对于同一`ordId`的撤单推送消息，请以第一条推送消息为准，忽略后续的推送消息；  
* 当`reqId`有值时，代表用户改单，改单时建议使用唯一的`reqId`，对于同一`reqId`的改单推送消息，请以第一条推送消息为准，忽略后续的推送消息。  REST 订单信息接口和订单频道在 fillPx、tradeId、fillSz、fillPnl、fillTime、fillFee、fillFeeCcy 和 execType 的定义上存在差异。  与交割合约不同，期权持仓到期之后，期权持仓在到期后会自动行权或作废，持仓本身随即消失，不会产生任何平仓订单，因此，该频道不会推送期权到期的平仓订单信息。