---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#order-book-trading-trade
anchor_id: order-book-trading-trade
api_type: API
updated_at: 2026-06-30 19:54:21.721736
---

# Trade

All `Trade` API endpoints require authentication.

### POST / Place order

You can place an order only if you have sufficient funds.

#### Rate Limit: 60 requests per 2 seconds

#### Rate Limit of lead trader lead instruments for Copy Trading: 4 requests per 2 seconds

#### Rate limit rule (except Options): User ID + Instrument ID

#### Rate limit rule (Options only): User ID + Instrument Family

#### Permission: Trade

Rate limit of this endpoint will also be affected by the rules [Sub-account rate limit](/docs-v5/en/#overview-rate-limits-sub-account-rate-limit) and [Fill ratio based sub-account rate limit](/docs-v5/en/#overview-rate-limits-fill-ratio-based-sub-account-rate-limit).

#### HTTP Request

`POST /api/v5/trade/order`

> Request Example
    
    
     place order for SPOT
     POST /api/v5/trade/order
     body
     {
        "instId":"BTC-USDT",
        "tdMode":"cash",
        "clOrdId":"b15",
        "side":"buy",
        "ordType":"limit",
        "px":"2.15",
        "sz":"2"
    }
    
    
    
    import okx.Trade as Trade
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # Production trading: 0, Demo trading: 1
    
    tradeAPI = Trade.TradeAPI(apikey, secretkey, passphrase, False, flag)
    
    # Spot mode, limit order
    result = tradeAPI.place_order(
        instId="BTC-USDT",
        tdMode="cash",
        clOrdId="b15",
        side="buy",
        ordType="limit",
        px="2.15",
        sz="2"
    )
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
instId | String | Yes | Instrument ID, e.g. `BTC-USDT`  
tdMode | String | Yes | Trade mode  
Margin mode `cross` `isolated` (`isolated` is only applicable to spot margin isolated)  
Non-Margin mode `cash`  
`spot_isolated` (only applicable to SPOT lead trading, `tdMode` should be `spot_isolated` for `SPOT` lead trading.)  
Note: `isolated` (spot margin isolated) is not available in multi-currency margin mode and portfolio margin mode.   
  
Event contracts symbols only support `isolated`  
ccy | String | No | Margin currency   
Applicable to all `isolated` `MARGIN` orders and `cross` `MARGIN` orders in `Futures mode`.  
clOrdId | String | No | Client Order ID as assigned by the client   
A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters.  
Only applicable to general order. It will not be posted to algoId when placing TP/SL order after the general order is filled completely.  
tag | String | No | Order tag   
A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 16 characters.  
side | String | Yes | Order side, `buy` `sell`  
posSide | String | Conditional | Position side   
The default is `net` in the `net` mode   
It is required in the `long/short` mode, and can only be `long` or `short`.   
Only applicable to `FUTURES`/`SWAP`. Do not send this field for `SPOT` or `MARGIN` orders. Omitting it for `FUTURES`/`SWAP` in long/short mode returns error 51000.  
ordType | String | Yes | Order type   
`market`: Market order, only applicable to `SPOT/MARGIN/FUTURES/SWAP`   
`limit`: Limit order   
`post_only`: Post-only order   
`fok`: Fill-or-kill order   
`ioc`: Immediate-or-cancel order   
`optimal_limit_ioc`: Places a limit order at the maximum buy price (upper price limit) for buy orders, or the minimum sell price (lower price limit) for sell orders, as defined by the exchange's price limit bands. Any unfilled portion is immediately cancelled (IOC). Applicable only to Expiry Futures and Perpetual Futures.  
`mmp`: Market Maker Protection (only applicable to Option in Portfolio Margin mode)   
`mmp_and_post_only`: Market Maker Protection and Post-only order(only applicable to Option in Portfolio Margin mode)  
`elp`: Enhanced Liquidity Program order  
sz | String | Yes | Quantity to buy or sell  
px | String | Conditional | Order price. Only applicable to `limit`,`post_only`,`fok`,`ioc`,`mmp`,`mmp_and_post_only` order.  
When placing an option order, one of px/pxUsd/pxVol must be filled in, and only one can be filled in  
speedBump | String | Conditional | Speed bump  
`1`: Event contract speed bumps (the delay duration will be changed subject to adjustment without prior notice). Required for non-post-only orders of `EVENTS` symbols.  
outcome | String | Conditional | The market outcome users trade on.  
`yes`  
`no`  
Only applicable and required for `EVENTS`  
pxUsd | String | Conditional | Place options orders in `USD`   
Only applicable to options   
When placing an option order, one of px/pxUsd/pxVol must be filled in, and only one can be filled in  
pxVol | String | Conditional | Place options orders based on implied volatility, where 1 represents 100%   
Only applicable to options   
When placing an option order, one of px/pxUsd/pxVol must be filled in, and only one can be filled in  
reduceOnly | Boolean | No | Whether orders can only reduce in position size.   
Valid options: `true` or `false`. The default value is `false`.  
Only applicable to `MARGIN` orders, and `FUTURES`/`SWAP` orders in `net` mode   
Only applicable to `Futures mode` and `Multi-currency margin`  
tgtCcy | String | No | Whether the target currency uses the quote or base currency.  
`base_ccy`: Base currency ,`quote_ccy`: Quote currency   
Only applicable to `SPOT` Market Orders  
Default is `quote_ccy` for buy, `base_ccy` for sell  
banAmend | Boolean | No | Whether to disallow the system from automatically reducing the order size when account balance is insufficient for the full SPOT Market Order.  
Valid options: `true` or `false`. The default value is `false`.  
If `true`: the entire order is rejected when balance is insufficient. If `false` (default): the system reduces sz to fit the available balance and executes the smaller order.  
Only applicable to SPOT Market Orders  
pxAmendType | String | No | The price amendment type for orders  
`0`: Do not allow the system to amend to order price if `px` exceeds the price limit   
`1`: Allow the system to amend the price to the best available value within the price limit if `px` exceeds the price limit  
The default value is `0`  
tradeQuoteCcy | String | No | The quote currency used for trading. Only applicable to `SPOT`.   
The default value is the quote currency of the `instId`, for example: for `BTC-USD`, the default is `USD`.  
slippagePct | String | No | Maximum acceptable slippage for spot and spot margin market-side orders, where `tgtCcy` is the received currency (`base_ccy` for buy, `quote_ccy` for sell).  
Range: `0` to `0.05` (0% to 5%, inclusive). Up to 2 decimal places of the percentage, e.g., `0.01` (1%) and `0.0123` (1.23%) are accepted; `0.01234` (1.234%) is rejected.  
If not specified or empty, defaults to `0.00%`.  
Slippage cannot be modified on an existing order. Cancel and resubmit to change the slippage setting.  
Only applicable to `SPOT` and `SPOT margin` `market` orders.  
stpMode | String | No | Self trade prevention mode.   
`cancel_maker`,`cancel_taker`, `cancel_both`  
Cancel both does not support FOK   
  
The account-level acctStpMode will be used to place orders by default. The default value of this field is `cancel_maker`. Users can log in to the webpage through the master account to modify this configuration. Users can also utilize the stpMode request parameter of the placing order endpoint to determine the stpMode of a certain order.  
isElpTakerAccess | Boolean | No | ELP taker access  
`true`: the request can trade with ELP orders but a speed bump will be applied  
`false`: the request cannot trade with ELP orders and no speed bump  
  
The default value is `false` while `true` is only applicable to ioc orders.  
attachAlgoOrds | Array of objects | No | Attached TP/SL or trailing stop order information  
> attachAlgoClOrdId | String | No | Client-supplied Algo ID when placing order with attached TP/SL or trailing stop  
A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters.  
It will be posted to `algoClOrdId` when placing the attached algo order once the general order is filled completely.  
> tpTriggerPx | String | Conditional | Take-profit trigger price  
For condition TP order, if you fill in this parameter, you should fill in the take-profit order price as well.  
> tpTriggerRatio | String | Conditional | Take profit trigger ratio, 0.3 represents 30%   
Only one of `tpTriggerPx` and `tpTriggerRatio` can be passed   
Only applicable to FUTURES and SWAP.   
If the main order is a buy order, it must be greater than 0, and if the main order is a sell order, it must be between -1 and 0.  
> tpOrdPx | String | Conditional | Take-profit order price   
  
For condition TP order, if you fill in this parameter, you should fill in the take-profit trigger price as well.   
For limit TP order, you need to fill in this parameter, but the take-profit trigger price doesn’t need to be filled.   
If the price is -1, take-profit will be executed at the market price.  
> tpOrdKind | String | No | TP order kind  
`condition`  
`limit`  
The default is `condition`  
> slTriggerPx | String | Conditional | Stop-loss trigger price  
If you fill in this parameter, you should fill in the stop-loss order price.  
> slTriggerRatio | String | Conditional | Stop-loss trigger ratio, 0.3 represents 30%   
Only one of `slTriggerPx` and `slTriggerRatio` can be passed   
Only applicable to FUTURES and SWAP.   
If the main order is a buy order, it should be between 0 and 1, and if the main order is a sell order, it must be greater than 0.  
> slOrdPx | String | Conditional | Stop-loss order price  
If you fill in this parameter, you should fill in the stop-loss trigger price.  
If the price is -1, stop-loss will be executed at the market price.  
> tpTriggerPxType | String | No | Take-profit trigger price type  
`last`: last price   
`index`: index price   
`mark`: mark price   
The default is last  
> slTriggerPxType | String | No | Stop-loss trigger price type  
`last`: last price   
`index`: index price   
`mark`: mark price   
The default is last  
> sz | String | Conditional | Size. Only applicable to TP order of split TPs, and it is required for TP order of split TPs  
> amendPxOnTriggerType | String | No | Whether to enable Cost-price SL. Only applicable to SL order of split TPs. Whether `slTriggerPx` will move to `avgPx` when the first TP order is triggered  
`0`: disable, the default value   
`1`: Enable  
> callbackRatio | String | Conditional | Callback ratio, e.g. `0.05` represents 5%.  
Either `callbackRatio` or `callbackSpread` is required. Only one can be passed.  
Only applicable when `ordType` = `move_order_stop`  
> callbackSpread | String | Conditional | Callback spread (price distance).  
Either `callbackRatio` or `callbackSpread` is required. Only one can be passed.  
Only applicable when `ordType` = `move_order_stop`  
> activePx | String | No | Activation price.  
The trailing stop is activated when the market price reaches the activation price. After activation, the system starts calculating the actual trigger price. If not provided, the trailing stop is activated immediately upon order placement.  
Only applicable when `ordType` = `move_order_stop`  
  
> Response Example
    
    
    {
      "code": "0",
      "msg": "",
      "data": [
        {
          "clOrdId": "oktswap6",
          "ordId": "312269865356374016",
          "tag": "",
          "ts":"1695190491421",
          "sCode": "0",
          "sMsg": "",
          "subCode": ""
        }
      ],
      "inTime": "1695190491421339",
      "outTime": "1695190491423240"
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
code | String | The result code, `0` means success  
msg | String | The error message, empty if the code is 0  
data | Array of objects | Array of objects contains the response results  
> ordId | String | Order ID  
> clOrdId | String | Client Order ID as assigned by the client  
> tag | String | Order tag  
> ts | String | Timestamp when the order request processing is finished by our system, Unix timestamp format in milliseconds, e.g. `1597026383085`  
> sCode | String | The code of the event execution result, `0` means success.  
> sMsg | String | Rejection or success message of event execution.  
> subCode | String | Sub-code of sCode.  
Returns `""` when sCode is 0 (request successful).  
When sCode is not 0 (request failed), returns the sub-code if available; otherwise returns `""`.  
inTime | String | Timestamp at REST gateway when the request is received, Unix timestamp format in microseconds, e.g. `1597026383085123`   
The time is recorded after authentication.  
outTime | String | Timestamp at REST gateway when the response is sent, Unix timestamp format in microseconds, e.g. `1597026383085123`  
tdMode  
Trade Mode, when placing an order, you need to specify the trade mode.  
**Spot mode:**  
\- SPOT and OPTION buyer: cash  
**Futures mode:**  
\- Isolated MARGIN (spot margin isolated only): isolated  
\- Cross MARGIN: cross  
\- SPOT: cash  
\- Cross FUTURES/SWAP/OPTION: cross  
**Multi-currency margin mode:**  
\- Cross SPOT: cross  
\- Cross FUTURES/SWAP/OPTION: cross  
**Portfolio margin:**  
\- Cross SPOT: cross  
\- Cross FUTURES/SWAP/OPTION: cross  
clOrdId  
clOrdId is a user-defined unique order identifier at the User ID level. If provided in the request parameters, it will be included in the response and can be used as a request parameter to query, cancel, and amend orders.   
clOrdId must be unique among all currently pending (live or partially_filled) orders in the account. Once an order reaches a terminal state (filled, canceled, mmp_canceled), the same clOrdId may be reused for a new order. Uniqueness is not enforced historically — GET /api/v5/trade/order returns only the latest match when multiple orders share a clOrdId. "General order" means a standard order placed via this endpoint; clOrdId is not forwarded to attached TP/SL algo orders.  posSide  
Position side, this parameter is not mandatory in **net** mode. If you pass it through, the only valid value is **net**.  
In **long/short** mode, it is mandatory. Valid values are **long** or **short**.  
In **long/short** mode, **side** and **posSide** need to be specified in the combinations below:  
Open long: buy and open long (side: fill in buy; posSide: fill in long)  
Open short: sell and open short (side: fill in sell; posSide: fill in short)  
Close long: sell and close long (side: fill in sell; posSide: fill in long)  
Close short: buy and close short (side: fill in buy; posSide: fill in short)  
Portfolio margin mode: Expiry Futures and Perpetual Futures only support net mode  
Do not send this field for SPOT or MARGIN orders. For FUTURES/SWAP in net mode, omit or explicitly pass `net`.  ordType   
Order type. When creating a new order, you must specify the order type. The order type you specify will affect: 1) what order parameters are required, and 2) how the matching system executes your order. The following are valid order types:   
limit: Limit order, which requires specified sz and px.   
market: Market order. For SPOT and MARGIN, market order will be filled with market price (by swiping opposite order book). For Expiry Futures and Perpetual Futures, market order will be placed to order book with most aggressive price allowed by Price Limit Mechanism. For OPTION, market order is not supported yet. As the filled price for market orders cannot be determined in advance, OKX reserves/freezes your quote currency by an additional 5% for risk check.   
post_only: Post-only order, which the order can only provide liquidity to the market and be a maker. If the order would have executed on placement, it will be canceled instead.   
fok: Fill or kill order. If the order cannot be fully filled, the order will be canceled. The order would not be partially filled.   
ioc: Immediate or cancel order. Immediately execute the transaction at the order price, cancel the remaining unfilled quantity of the order, and the order quantity will not be displayed in the order book.   
optimal_limit_ioc: Places a limit order at the maximum buy price (upper price limit) for buy orders, or the minimum sell price (lower price limit) for sell orders, as defined by the exchange's price limit bands at the time of submission. Any unfilled portion is immediately cancelled (IOC). Applicable only to Expiry Futures and Perpetual Futures. The order will not execute at a price worse than the current price limit boundary.  sz  
Quantity to buy or sell.   
For SPOT/MARGIN Buy and Sell Limit Orders, it refers to the quantity in base currency.   
For MARGIN Buy Market Orders, it refers to the quantity in quote currency.   
For MARGIN Sell Market Orders, it refers to the quantity in base currency.   
For SPOT Market Orders, it is set by tgtCcy.   
For FUTURES/SWAP/OPTION orders, it refers to the number of contracts. Notional value = sz × ctVal × markPx (linear contracts) or sz × ctVal (inverse contracts, USD-denominated). Retrieve ctVal and ctType from GET /api/v5/public/instruments.  reduceOnly  
When placing an order with this parameter set to true, it means that the order will reduce the size of the position only  
For the same MARGIN instrument, the coin quantity of all reverse direction pending orders adds `sz` of new `reduceOnly` order cannot exceed the position assets. After the debt is paid off, if there is a remaining size of orders, the position will not be opened in reverse, but will be traded in SPOT.  
For the same FUTURES/SWAP instrument, the sum of the current order size and all reverse direction reduce-only pending orders which’s price-time priority is higher than the current order, cannot exceed the contract quantity of position.  
Only applicable to `Futures mode` and `Multi-currency margin`  
Only applicable to `MARGIN` orders, and `FUTURES`/`SWAP` orders in `net` mode  
Notice: Under long/short mode of Expiry Futures and Perpetual Futures, all closing orders apply the reduce-only feature which is not affected by this parameter.  
If sz exceeds the current position size, the entire order is rejected — the system does not auto-trim to the position size.  tgtCcy  
This parameter is used to specify the order quantity in the order request is denominated in the quantity of base or quote currency. This is applicable to SPOT Market Orders only.  
Quick reference for BTC-USDT:  
\- tgtCcy=`quote_ccy`, sz=100 (buy): spend 100 USDT on BTC.  
\- tgtCcy=`base_ccy`, sz=0.001 (buy): buy 0.001 BTC at market price.  
\- tgtCcy=`base_ccy`, sz=0.001 (sell, default): sell 0.001 BTC.  
\- tgtCcy=`quote_ccy`, sz=100 (sell): sell BTC until you receive 100 USDT.  
Base currency: base_ccy  
Quote currency: quote_ccy   
If you use the Base Currency quantity for buy market orders or the Quote Currency for sell market orders, please note:   
1\. If the quantity you enter is greater than what you can buy or sell, the system will execute the order according to your maximum buyable or sellable quantity. If you want to trade according to the specified quantity, you should use Limit orders.   
2\. When the market price is too volatile, the locked balance may not be sufficient to buy the Base Currency quantity or sell to receive the Quote Currency that you specified. We will change the quantity of the order to execute the order based on best effort principle based on your account balance. In addition, we will try to over lock a fraction of your balance to avoid changing the order quantity.   
2.1 Example of base currency buy market order:   
Taking the market order to buy 10 LTCs as an example, and the user can buy 11 LTC. At this time, if 10 < 11, the order is accepted. When the LTC-USDT market price is 200, and the locked balance of the user is 3,000 USDT, as 200*10 < 3,000, the market order of 10 LTC is fully executed; If the market is too volatile and the LTC-USDT market price becomes 400, 400*10 > 3,000, the user's locked balance is not sufficient to buy using the specified amount of base currency, the user's maximum locked balance of 3,000 USDT will be used to settle the trade. Final transaction quantity becomes 3,000/400 = 7.5 LTC.   
2.2 Example of quote currency sell market order:   
Taking the market order to sell 1,000 USDT as an example, and the user can sell 1,200 USDT, 1,000 < 1,200, the order is accepted. When the LTC-USDT market price is 200, and the locked balance of the user is 6 LTC, as 1,000/200 < 6, the market order of 1,000 USDT is fully executed; If the market is too volatile and the LTC-USDT market price becomes 100, 100*6 < 1,000, the user's locked balance is not sufficient to sell using the specified amount of quote currency, the user's maximum locked balance of 6 LTC will be used to settle the trade. Final transaction quantity becomes 6 * 100 = 600 USDT.  px  
The value for px must be a multiple of tickSz for OPTION orders.  
If not, the system will apply the rounding rules below. Using tickSz 0.0005 as an example:  
The px will be rounded up to the nearest 0.0005 when the remainder of px to 0.0005 is more than 0.00025 or `px` is less than 0.0005.  
The px will be rounded down to the nearest 0.0005 when the remainder of px to 0.0005 is less than 0.00025 and `px` is more than 0.0005.  For placing order with TP/SL:  
Attached TP/SL orders become active only after the parent order is filled. If the parent is cancelled before any fill, the attached TP/SL is also discarded. For TP/SL orders independent of a parent order, use POST /api/v5/trade/order-algo.  
1\. TP/SL algo order will be generated only when this order is filled; if the parent order is cancelled before any fill, no TP/SL algo order will be generated.  
2\. Attaching TP/SL is neither supported for market buy with tgtCcy is base_ccy or market sell with tgtCcy is quote_ccy  
3\. If tpOrdKind is limit, and there is only one conditional TP order, attachAlgoClOrdId can be used as clOrdId for retrieving on "GET / Order details" endpoint.  
4\. For “split TPs”, including condition TP order and limit TP order.  
* TP/SL orders in Split TPs only support one-way TP/SL. You can't use slTriggerPx&slOrdPx and tpTriggerPx&tpOrdPx at the same time, or error code 51076 will be thrown.  
* Take-profit trigger price types (tpTriggerPxType) must be the same in an order with Split TPs attached, or error code 51080 will be thrown.  
* Take-profit trigger prices (tpTriggerPx) cannot be the same in an order with Split TPs attached, or error code 51081 will be thrown.  
* The size of the TP order among split TPs attached cannot be empty, or error code 51089 will be thrown.  
* The total size of TP orders with Split TPs attached in a same order should equal the size of this order, or error code 51083 will be thrown.  
* The number of TP orders with Split TPs attached in a same order cannot exceed 10, or error code 51079 will be thrown.  
* Setting multiple TP and cost-price SL orders isn’t supported for spot and margin trading, or error code 51077 will be thrown.  
* The number of SL orders with Split TPs attached in a same order cannot exceed 1, or error code 51084 will be thrown.  
* The number of TP orders cannot be less than 2 when cost-price SL is enabled (amendPxOnTriggerType set as 1) for Split TPs, or error code 51085 will be thrown.  
* All TP orders in one order must be of the same type, or error code 51091 will be thrown.  
* TP order prices (tpOrdPx) in one order must be different, or error code 51092 will be thrown.  
* TP limit order prices (tpOrdPx) in one order can't be –1 (market price), or error code 51093 will be thrown.  
* You can't place TP limit orders in spot, margin, or options trading. Otherwise, error code 51094 will be thrown.  
Mandatory self trade prevention (STP)  
The trading platform imposes mandatory self trade prevention at master account level, which means the accounts under the same master account, including master account itself and all its affiliated sub-accounts, will be prevented from self trade. The account-level acctStpMode will be used to place orders by default. The default value of this field is `cancel_maker`. Users can log in to the webpage through the master account to modify this configuration. Users can also utilize the stpMode request parameter of the placing order endpoint to determine the stpMode of a certain order.  
Mandatory self trade prevention will not lead to latency.   
There are three STP modes. The STP mode is always taken based on the configuration in the taker order.  
1\. Cancel Maker: This is the default STP mode, which cancels the maker order to prevent self-trading. Then, the taker order continues to match with the next order based on the order book priority.  
2\. Cancel Taker: The taker order is canceled to prevent self-trading. If the user's own maker order is lower in the order book priority, the taker order is partially filled and then canceled. FOK orders are always honored and canceled if they would result in self-trading.  
3\. Cancel Both: Both taker and maker orders are canceled to prevent self-trading. If the user's own maker order is lower in the order book priority, the taker order is partially filled. Then, the remaining quantity of the taker order and the first maker order are canceled. FOK orders are not supported in this mode. Combining stpMode=cancel_both with ordType=`fok` returns error 50016.  tradeQuoteCcy  
For users in specific countries and regions, this parameter must be filled out for a successful order. Otherwise, the system will use the quote currency of instId as the default value, then error code 51000 will occur.  
The value provided must be one of the enumerated values from tradeQuoteCcyList, which can be obtained from the endpoint Get instruments (GET /api/v5/account/instruments).  Rate limit of orders tagged as isElpTakerAccess:true  
\- 50 orders per 2 seconds per User ID per instrument ID.  
\- This rate limit is shared in Place order/Place multiple orders endpoints in REST/WebSocket  

### POST / Place multiple orders

Place orders in batches. Maximum 20 orders can be placed per request.   
Request parameters should be passed in the form of an array. Orders will be placed in turn  

#### Rate Limit: 300 orders per 2 seconds

#### Rate Limit of lead trader lead instruments for Copy Trading: 4 orders per 2 seconds

#### Rate limit rule (except Options): User ID + Instrument ID

#### Rate limit rule (Options only): User ID + Instrument Family

#### Permission: Trade

Rate limit of this endpoint will also be affected by the rules [Sub-account rate limit](/docs-v5/en/#overview-rate-limits-sub-account-rate-limit) and [Fill ratio based sub-account rate limit](/docs-v5/en/#overview-rate-limits-fill-ratio-based-sub-account-rate-limit).

Unlike other endpoints, the rate limit of this endpoint is determined by the number of orders. If there is only one order in the request, it will consume the rate limit of `Place order`. 

#### HTTP Request

`POST /api/v5/trade/batch-orders`

> Request Example
    
    
     batch place order for SPOT
     POST /api/v5/trade/batch-orders
     body
     [
        {
            "instId":"BTC-USDT",
            "tdMode":"cash",
            "clOrdId":"b15",
            "side":"buy",
            "ordType":"limit",
            "px":"2.15",
            "sz":"2"
        },
        {
            "instId":"BTC-USDT",
            "tdMode":"cash",
            "clOrdId":"b16",
            "side":"buy",
            "ordType":"limit",
            "px":"2.15",
            "sz":"2"
        }
    ]
    
    
    
    
    import okx.Trade as Trade
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # Production trading: 0, Demo trading: 1
    
    tradeAPI = Trade.TradeAPI(apikey, secretkey, passphrase, False, flag)
    
    # Place multiple orders 
    place_orders_without_clOrdId = [
        {"instId": "BTC-USDT", "tdMode": "cash", "clOrdId": "b15", "side": "buy", "ordType": "limit", "px": "2.15", "sz": "2"},
        {"instId": "BTC-USDT", "tdMode": "cash", "clOrdId": "b16", "side": "buy", "ordType": "limit", "px": "2.15", "sz": "2"}
    ]
    
    result = tradeAPI.place_multiple_orders(place_orders_without_clOrdId)
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
instId | String | Yes | Instrument ID, e.g. `BTC-USDT`  
tdMode | String | Yes | Trade mode  
Margin mode `cross` `isolated`  
Non-Margin mode `cash`  
`spot_isolated` (only applicable to SPOT lead trading, `tdMode` should be `spot_isolated` for `SPOT` lead trading.)  
Note: `isolated` is not available in multi-currency margin mode and portfolio margin mode.   
  
Event contracts symbols only support `isolated`  
ccy | String | No | Margin currency   
Applicable to all `isolated` `MARGIN` orders and `cross` `MARGIN` orders in `Futures mode`.  
clOrdId | String | No | Client Order ID as assigned by the client   
A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters.  
tag | String | No | Order tag   
A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 16 characters.  
side | String | Yes | Order side `buy` `sell`  
posSide | String | Conditional | Position side   
The default is `net` in the `net` mode   
It is required in the `long/short` mode, and can only be `long` or `short`.   
Only applicable to `FUTURES`/`SWAP`.  
ordType | String | Yes | Order type   
`market`: Market order, only applicable to `SPOT/MARGIN/FUTURES/SWAP`   
`limit`: Limit order   
`post_only`: Post-only order   
`fok`: Fill-or-kill order   
`ioc`: Immediate-or-cancel order   
`optimal_limit_ioc`: Market order with immediate-or-cancel order (applicable only to Expiry Futures and Perpetual Futures).  
`mmp`: Market Maker Protection (only applicable to Option in Portfolio Margin mode)  
`mmp_and_post_only`: Market Maker Protection and Post-only order(only applicable to Option in Portfolio Margin mode)   
`elp`: Enhanced Liquidity Program order  
sz | String | Yes | Quantity to buy or sell  
px | String | Conditional | Order price. Only applicable to `limit`,`post_only`,`fok`,`ioc`,`mmp`,`mmp_and_post_only` order.  
When placing an option order, one of px/pxUsd/pxVol must be filled in, and only one can be filled in  
speedBump | String | Conditional | Speed bump  
`1`: Event contract speed bumps (the delay duration will be changed subject to adjustment without prior notice). Required for non-post-only orders of `EVENTS` symbols.  
outcome | String | Conditional | The market outcome users trade on.  
`yes`  
`no`  
Only applicable and required for `EVENTS`  
pxUsd | String | Conditional | Place options orders in `USD`   
Only applicable to options   
When placing an option order, one of px/pxUsd/pxVol must be filled in, and only one can be filled in  
pxVol | String | Conditional | Place options orders based on implied volatility, where 1 represents 100%   
Only applicable to options   
When placing an option order, one of px/pxUsd/pxVol must be filled in, and only one can be filled in  
reduceOnly | Boolean | No | Whether the order can only reduce position size.   
Valid options: `true` or `false`. The default value is `false`.  
Only applicable to `MARGIN` orders, and `FUTURES`/`SWAP` orders in `net` mode   
Only applicable to `Futures mode` and `Multi-currency margin`  
tgtCcy | String | No | Order quantity unit setting for `sz`  
`base_ccy`: Base currency ,`quote_ccy`: Quote currency   
Only applicable to `SPOT` Market Orders  
Default is `quote_ccy` for buy, `base_ccy` for sell  
banAmend | Boolean | No | Whether to disallow the system from amending the size of the SPOT Market Order.  
Valid options: `true` or `false`. The default value is `false`.  
If `true`, system will not amend and reject the market order if user does not have sufficient funds.   
Only applicable to SPOT Market Orders  
pxAmendType | String | No | The price amendment type for orders  
`0`: Do not allow the system to amend to order price if `px` exceeds the price limit   
`1`: Allow the system to amend the price to the best available value within the price limit if `px` exceeds the price limit  
The default value is `0`  
tradeQuoteCcy | String | No | The quote currency used for trading. Only applicable to `SPOT`.   
The default value is the quote currency of the `instId`, for example: for `BTC-USD`, the default is `USD`.  
slippagePct | String | No | Maximum acceptable slippage for spot and spot margin market-side orders, where `tgtCcy` is the received currency (`base_ccy` for buy, `quote_ccy` for sell).  
Range: `0` to `0.05` (0% to 5%, inclusive). Up to 2 decimal places of the percentage, e.g., `0.01` (1%) and `0.0123` (1.23%) are accepted; `0.01234` (1.234%) is rejected.  
If not specified or empty, defaults to `0.00%`.  
Slippage cannot be modified on an existing order. Cancel and resubmit to change the slippage setting.  
Only applicable to `SPOT` and `SPOT margin` `market` orders.  
stpMode | String | No | Self trade prevention mode.   
`cancel_maker`,`cancel_taker`, `cancel_both`  
Cancel both does not support FOK.   
  
The account-level acctStpMode will be used to place orders by default. The default value of this field is `cancel_maker`. Users can log in to the webpage through the master account to modify this configuration. Users can also utilize the stpMode request parameter of the placing order endpoint to determine the stpMode of a certain order.  
isElpTakerAccess | Boolean | No | ELP taker access  
`true`: the request can trade with ELP orders but a speed bump will be applied  
`false`: the request cannot trade with ELP orders and no speed bump  
  
The default value is `false` while `true` is only applicable to ioc orders.  
attachAlgoOrds | Array of objects | No | Attached TP/SL or trailing stop order information  
> attachAlgoClOrdId | String | No | Client-supplied Algo ID when placing order with attached TP/SL or trailing stop  
A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters.  
It will be posted to `algoClOrdId` when placing the attached algo order once the general order is filled completely.  
> tpTriggerPx | String | Conditional | Take-profit trigger price  
For condition TP order, if you fill in this parameter, you should fill in the take-profit order price as well.  
> tpTriggerRatio | String | Conditional | Take profit trigger ratio, 0.3 represents 30%   
Only one of `tpTriggerPx` and `tpTriggerRatio` can be passed   
Only applicable to FUTURES and SWAP.  
If the main order is a buy order, it must be greater than 0, and if the main order is a sell order, it must be between -1 and 0.  
> tpOrdPx | String | Conditional | Take-profit order price   
For condition TP order, if you fill in this parameter, you should fill in the take-profit trigger price as well.   
For limit TP order, you need to fill in this parameter, take-profit trigger needn't to be filled.  
If the price is -1, take-profit will be executed at the market price.  
> tpOrdKind | String | No | TP order kind  
`condition`  
`limit`  
The default is `condition`  
> slTriggerPx | String | Conditional | Stop-loss trigger price  
If you fill in this parameter, you should fill in the stop-loss order price.  
> slTriggerRatio | String | Conditional | Stop-loss trigger ratio, 0.3 represents 30%   
Only one of `slTriggerPx` and `slTriggerRatio` can be passed   
Only applicable to FUTURES and SWAP.  
If the main order is a buy order, it should be between 0 and 1, and if the main order is a sell order, it must be greater than 0.  
> slOrdPx | String | Conditional | Stop-loss order price  
If you fill in this parameter, you should fill in the stop-loss trigger price.  
If the price is -1, stop-loss will be executed at the market price.  
> tpTriggerPxType | String | No | Take-profit trigger price type  
`last`: last price   
`index`: index price   
`mark`: mark price   
The default is last  
> slTriggerPxType | String | No | Stop-loss trigger price type  
`last`: last price   
`index`: index price   
`mark`: mark price   
The default is last  
> sz | String | Conditional | Size. Only applicable to TP order of split TPs, and it is required for TP order of split TPs  
> amendPxOnTriggerType | String | No | Whether to enable Cost-price SL. Only applicable to SL order of split TPs. Whether `slTriggerPx` will move to `avgPx` when the first TP order is triggered  
`0`: disable, the default value   
`1`: Enable  
> callbackRatio | String | Conditional | Callback ratio, e.g. `0.05` represents 5%.  
Either `callbackRatio` or `callbackSpread` is required. Only one can be passed.  
Only applicable when `ordType` = `move_order_stop`  
> callbackSpread | String | Conditional | Callback spread (price distance).  
Either `callbackRatio` or `callbackSpread` is required. Only one can be passed.  
Only applicable when `ordType` = `move_order_stop`  
> activePx | String | No | Activation price.  
The trailing stop is activated when the market price reaches the activation price. After activation, the system starts calculating the actual trigger price. If not provided, the trailing stop is activated immediately upon order placement.  
Only applicable when `ordType` = `move_order_stop`  
  
> Response Example
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
            {
                "clOrdId":"oktswap6",
                "ordId":"12345689",
                "tag":"",
                "ts":"1695190491421",
                "sCode":"0",
                "sMsg":"",
                "subCode": ""
            },
            {
                "clOrdId":"oktswap7",
                "ordId":"12344",
                "tag":"",
                "ts":"1695190491421",
                "sCode":"0",
                "sMsg":"",
                "subCode": ""
            }
        ],
        "inTime": "1695190491421339",
        "outTime": "1695190491423240"
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
code | String | The result code, `0` means success  
msg | String | The error message, empty if the code is 0  
data | Array of objects | Array of objects contains the response results  
> ordId | String | Order ID  
> clOrdId | String | Client Order ID as assigned by the client  
> tag | String | Order tag  
> ts | String | Timestamp when the order request processing is finished by our system, Unix timestamp format in milliseconds, e.g. `1597026383085`  
> sCode | String | The code of the event execution result, `0` means success.  
> sMsg | String | Rejection or success message of event execution.  
> subCode | String | Sub-code of sCode.  
Returns `""` when sCode is 0 (request successful).  
When sCode is not 0 (request failed), returns the sub-code if available; otherwise returns `""`.  
inTime | String | Timestamp at REST gateway when the request is received, Unix timestamp format in microseconds, e.g. `1597026383085123`   
The time is recorded after authentication.  
outTime | String | Timestamp at REST gateway when the response is sent, Unix timestamp format in microseconds, e.g. `1597026383085123`  
In the `Portfolio Margin` account mode, either all orders are accepted by the system successfully, or all orders are rejected by the system.  clOrdId  
clOrdId is a user-defined unique ID used to identify the order. It will be included in the response parameters if you have specified during order submission, and can be used as a request parameter to the endpoints to query, cancel and amend orders.   
clOrdId must be unique among all pending orders and the current request.  Rate limit of orders tagged as isElpTakerAccess:true  
\- 50 orders per 2 seconds per User ID per instrument ID.  
\- This rate limit is shared in Place order/Place multiple orders endpoints in REST/WebSocket  

### POST / Cancel order

Cancel an incomplete order.

#### Rate Limit: 60 requests per 2 seconds

#### Rate limit rule (except Options): User ID + Instrument ID

#### Rate limit rule (Options only): User ID + Instrument Family

#### Permission: Trade

#### HTTP Request

`POST /api/v5/trade/cancel-order`

> Request Example
    
    
    POST /api/v5/trade/cancel-order
    body
    {
        "ordId":"590908157585625111",
        "instId":"BTC-USD-190927"
    }
    
    
    
    
    import okx.Trade as Trade
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # Production trading: 0, Demo trading: 1
    
    tradeAPI = Trade.TradeAPI(apikey, secretkey, passphrase, False, flag)
    
    # Cancel order
    result = tradeAPI.cancel_order(instId="BTC-USDT", ordId="590908157585625111")
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
instId | String | Yes | Instrument ID, e.g. `BTC-USDT`  
ordId | String | Conditional | Order ID   
Either `ordId` or `clOrdId` is required. If both are passed, ordId will be used.  
clOrdId | String | Conditional | Client Order ID as assigned by the client  
  
> Response Example
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
            {
                "clOrdId":"oktswap6",
                "ordId":"12345689",
                "ts":"1695190491421",
                "sCode":"0",
                "sMsg":""
            }
        ],
        "inTime": "1695190491421339",
        "outTime": "1695190491423240"
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
code | String | The result code, `0` means success  
msg | String | The error message, empty if the code is 0  
data | Array of objects | Array of objects contains the response results  
> ordId | String | Order ID  
> clOrdId | String | Client Order ID as assigned by the client  
> ts | String | Timestamp when the order request processing is finished by our system, Unix timestamp format in milliseconds, e.g. `1597026383085`  
> sCode | String | The code of the event execution result, `0` means success.  
> sMsg | String | Rejection message if the request is unsuccessful.  
inTime | String | Timestamp at REST gateway when the request is received, Unix timestamp format in microseconds, e.g. `1597026383085123`   
The time is recorded after authentication.  
outTime | String | Timestamp at REST gateway when the response is sent, Unix timestamp format in microseconds, e.g. `1597026383085123`  
Cancel order returns with sCode equal to 0. It is not strictly considered that the order has been canceled. It only means that your cancellation request has been accepted by the system server. The result of the cancellation is subject to the state pushed by the order channel or the get order state.  

### POST / Cancel multiple orders

Cancel incomplete orders in batches. Maximum 20 orders can be canceled per request. Request parameters should be passed in the form of an array.

#### Rate Limit: 300 orders per 2 seconds

#### Rate limit rule (except Options): User ID + Instrument ID

#### Rate limit rule (Options only): User ID + Instrument Family

#### Permission: Trade

Unlike other endpoints, the rate limit of this endpoint is determined by the number of orders. If there is only one order in the request, it will consume the rate limit of `Cancel order`. 

#### HTTP Request

`POST /api/v5/trade/cancel-batch-orders`

> Request Example
    
    
    POST /api/v5/trade/cancel-batch-orders
    body
    [
        {
            "instId":"BTC-USDT",
            "ordId":"590908157585625111"
        },
        {
            "instId":"BTC-USDT",
            "ordId":"590908544950571222"
        }
    ]
    
    
    
    import okx.Trade as Trade
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # Production trading: 0, Demo trading: 1
    
    tradeAPI = Trade.TradeAPI(apikey, secretkey, passphrase, False, flag)
    
    # Cancel multiple orders by ordId
    cancel_orders_with_orderId = [
        {"instId": "BTC-USDT", "ordId": "590908157585625111"},
        {"instId": "BTC-USDT", "ordId": "590908544950571222"}
    ]
    
    result = tradeAPI.cancel_multiple_orders(cancel_orders_with_orderId)
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
instId | String | Yes | Instrument ID, e.g. `BTC-USDT`  
ordId | String | Conditional | Order ID  
Either `ordId` or `clOrdId` is required. If both are passed, `ordId` will be used.  
clOrdId | String | Conditional | Client Order ID as assigned by the client  
  
> Response Example
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
            {
                "clOrdId":"oktswap6",
                "ordId":"12345689",
                "ts":"1695190491421",
                "sCode":"0",
                "sMsg":""
            },
            {
                "clOrdId":"oktswap7",
                "ordId":"12344",
                "ts":"1695190491421",
                "sCode":"0",
                "sMsg":""
            }
        ],
        "inTime": "1695190491421339",
        "outTime": "1695190491423240"
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
code | String | The result code, `0` means success  
msg | String | The error message, empty if the code is 0  
data | Array of objects | Array of objects contains the response results  
> ordId | String | Order ID  
> clOrdId | String | Client Order ID as assigned by the client  
> ts | String | Timestamp when the order request processing is finished by our system, Unix timestamp format in milliseconds, e.g. `1597026383085`  
> sCode | String | The code of the event execution result, `0` means success.  
> sMsg | String | Rejection message if the request is unsuccessful.  
inTime | String | Timestamp at REST gateway when the request is received, Unix timestamp format in microseconds, e.g. `1597026383085123`   
The time is recorded after authentication.  
outTime | String | Timestamp at REST gateway when the response is sent, Unix timestamp format in microseconds, e.g. `1597026383085123`  
  
### POST / Amend order

Amend an incomplete order.

#### Rate Limit: 60 requests per 2 seconds

#### Rate Limit of lead trader lead instruments for Copy Trading: 4 requests per 2 seconds

#### Rate limit rule (except Options): User ID + Instrument ID

#### Rate limit rule (Options only): User ID + Instrument Family

#### Permission: Trade

Rate limit of this endpoint will also be affected by the rules [Sub-account rate limit](/docs-v5/en/#overview-rate-limits-sub-account-rate-limit) and [Fill ratio based sub-account rate limit](/docs-v5/en/#overview-rate-limits-fill-ratio-based-sub-account-rate-limit).

#### HTTP Request

`POST /api/v5/trade/amend-order`

> Request Example
    
    
    POST /api/v5/trade/amend-order
    body
    {
        "ordId":"590909145319051111",
        "newSz":"2",
        "instId":"BTC-USDT"
    }
    
    
    
    import okx.Trade as Trade
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # Production trading: 0, Demo trading: 1
    
    tradeAPI = Trade.TradeAPI(apikey, secretkey, passphrase, False, flag)
    
    # Amend order
    result = tradeAPI.amend_order(
        instId="BTC-USDT",
        ordId="590909145319051111",
        newSz="2"
    )
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
instId | String | Yes | Instrument ID  
cxlOnFail | Boolean | No | Whether the order needs to be automatically canceled when the order amendment fails   
Valid options: `false` or `true`, the default is `false`.   
Amendment failure scenarios include: `newSz` not a multiple of `lotSz`, position or risk limit breach, etc. When `false` (default): the original order continues unchanged after a failed amendment. When `true`: the original order is auto-cancelled on any amendment failure.  
ordId | String | Conditional | Order ID   
Either `ordId` or `clOrdId` is required. If both are passed, `ordId` will be used.  
clOrdId | String | Conditional | Client Order ID as assigned by the client  
reqId | String | No | Client Request ID as assigned by the client for order amendment   
A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters.   
The response will include the corresponding `reqId` to help you identify the request if you provide it in the request.  
newSz | String | Conditional | New **total** target quantity after amendment, must be > 0\. This is the desired total order size, not the remaining unfilled portion. For a partially-filled order: if 3 contracts are already filled and you want a total of 8, pass `newSz=8` (not 5). The system will attempt to fill the remaining 5. At least one of `newSz` or `newPx` (or `newPxUsd`/`newPxVol` for options) must be provided.  
newPx | String | Conditional | New price after amendment.   
When modifying options orders, users can only fill in one of the following: newPx, newPxUsd, or newPxVol. It must be consistent with parameters when placing orders. For example, if users placed the order using px, they should use newPx when modifying the order. At least one of `newSz` or `newPx` must be provided.  
speedBump | String | Conditional | Speed bump  
`1`: Event contract speed bumps (the delay duration will be changed subject to adjustment without prior notice). Required for non-post-only orders of `EVENTS` symbols.  
newPxUsd | String | Conditional | Modify options orders using USD prices   
Only applicable to options.   
When modifying options orders, users can only fill in one of the following: newPx, newPxUsd, or newPxVol.  
newPxVol | String | Conditional | Modify options orders based on implied volatility, where 1 represents 100%   
Only applicable to options.   
When modifying options orders, users can only fill in one of the following: newPx, newPxUsd, or newPxVol.  
pxAmendType | String | No | The price amendment type for orders  
`0`: Do not allow the system to amend to order price if `newPx` exceeds the price limit   
`1`: Allow the system to amend the price to the best available value within the price limit if `newPx` exceeds the price limit  
The default value is `0`  
attachAlgoOrds | Array of objects | No | Attached TP/SL or trailing stop order information  
> attachAlgoId | String | Conditional | The order ID of the attached TP/SL or trailing stop order. It is required to identify the attached order when amending. It will not be posted to algoId when placing the attached algo order after the general order is filled completely.  
> attachAlgoClOrdId | String | Conditional | Client-supplied Algo ID when placing order with attached TP/SL or trailing stop  
A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters.  
It will be posted to `algoClOrdId` when placing the attached algo order once the general order is filled completely.  
> newTpTriggerPx | String | Conditional | Take-profit trigger price.   
Either the take profit trigger price or order price is 0, it means that the take profit is deleted.  
> newTpTriggerRatio | String | Conditional | Take profit trigger ratio, 0.3 represents 30%   
Only applicable to FUTURES and SWAP.   
Only one of `newTpTriggerPx` and `newTpTriggerRatio` can be passed.   
If the main order is a buy order, it must be greater than 0, and if the main order is a sell order, it must be between -1 and 0. 0 means to delete the take-profit.  
> newTpOrdPx | String | Conditional | Take-profit order price  
If the price is -1, take-profit will be executed at the market price.  
> newTpOrdKind | String | No | TP order kind  
`condition`  
`limit`  
> newSlTriggerPx | String | Conditional | Stop-loss trigger price  
Either the stop loss trigger price or order price is 0, it means that the stop loss is deleted.  
> newSlTriggerRatio | String | Conditional | Stop-loss trigger ratio, 0.3 represents 30%   
Only applicable to FUTURES and SWAP.  
Only one of `newSlTriggerPx` and `newSlTriggerRatio` can be passed.   
If the main order is a buy order, it should be between 0 and 1, and if the main order is a sell order, it must be greater than 0.   
Only one of `newSlTriggerPx` and `newSlTriggerRatio` can be passed, 0 means to delete the stop-loss.  
> newSlOrdPx | String | Conditional | Stop-loss order price  
If the price is -1, stop-loss will be executed at the market price.  
> newTpTriggerPxType | String | Conditional | Take-profit trigger price type  
`last`: last price   
`index`: index price   
`mark`: mark price  
Only applicable to `FUTURES`/`SWAP`  
If you want to add the take-profit, this parameter is required  
> newSlTriggerPxType | String | Conditional | Stop-loss trigger price type  
`last`: last price   
`index`: index price   
`mark`: mark price  
Only applicable to `FUTURES`/`SWAP`  
If you want to add the stop-loss, this parameter is required  
> sz | String | Conditional | New size. Only applicable to TP order of split TPs, and it is required for TP order of split TPs  
> amendPxOnTriggerType | String | No | Whether to enable Cost-price SL. Only applicable to SL order of split TPs.   
`0`: disable, the default value   
`1`: Enable  
> newCallbackRatio | String | Conditional | New callback ratio, e.g. `0.05` represents 5%.  
Either `newCallbackRatio` or `newCallbackSpread` can be passed. Only one can be passed.  
Only applicable when `ordType` = `move_order_stop`  
> newCallbackSpread | String | Conditional | New callback spread (price distance).  
Either `newCallbackRatio` or `newCallbackSpread` can be passed. Only one can be passed.  
Only applicable when `ordType` = `move_order_stop`  
> newActivePx | String | No | New activation price.  
Only applicable when `ordType` = `move_order_stop`  
  
> Response Example
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
            {
             "clOrdId":"",
             "ordId":"12344",
             "ts":"1695190491421",
             "reqId":"b12344",
             "sCode":"0",
             "sMsg":""
             "subCode": ""
            }
        ],
        "inTime": "1695190491421339",
        "outTime": "1695190491423240"
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
code | String | The result code, `0` means success  
msg | String | The error message, empty if the code is 0  
data | Array of objects | Array of objects contains the response results  
> ordId | String | Order ID  
> clOrdId | String | Client Order ID as assigned by the client  
> ts | String | Timestamp when the order request processing is finished by our system, Unix timestamp format in milliseconds, e.g. `1597026383085`  
> reqId | String | Client Request ID as assigned by the client for order amendment.  
> sCode | String | The code of the event execution result, `0` means success.  
> sMsg | String | Rejection message if the request is unsuccessful.  
> subCode | String | Sub-code of sCode.  
Returns `""` when sCode is 0 (request successful).  
When sCode is not 0 (request failed), returns the sub-code if available; otherwise returns `""`.  
inTime | String | Timestamp at REST gateway when the request is received, Unix timestamp format in microseconds, e.g. `1597026383085123`   
The time is recorded after authentication.  
outTime | String | Timestamp at REST gateway when the response is sent, Unix timestamp format in microseconds, e.g. `1597026383085123`  
newSz   
If the new quantity of the order is less than or equal to the filled quantity when you are amending a partially-filled order, the order status will be changed to filled.  The amend order returns sCode equal to 0. It is not strictly considered that the order has been amended. It only means that your amend order request has been accepted by the system server. The result of the amend is subject to the status pushed by the order channel or the order status query 

### POST / Amend multiple orders

Amend incomplete orders in batches. Maximum 20 orders can be amended per request. Request parameters should be passed in the form of an array.

#### Rate Limit: 300 orders per 2 seconds

#### Rate Limit of lead trader lead instruments for Copy Trading: 4 orders per 2 seconds

#### Rate limit rule (except Options): User ID + Instrument ID

#### Rate limit rule (Options only): User ID + Instrument Family

#### Permission: Trade

Rate limit of this endpoint will also be affected by the rules [Sub-account rate limit](/docs-v5/en/#overview-rate-limits-sub-account-rate-limit) and [Fill ratio based sub-account rate limit](/docs-v5/en/#overview-rate-limits-fill-ratio-based-sub-account-rate-limit).

Unlike other endpoints, the rate limit of this endpoint is determined by the number of orders. If there is only one order in the request, it will consume the rate limit of `Amend order`. 

#### HTTP Request

`POST /api/v5/trade/amend-batch-orders`

> Request Example
    
    
    POST /api/v5/trade/amend-batch-orders
    body
    [
        {
            "ordId":"590909308792049444",
            "newSz":"2",
            "instId":"BTC-USDT"
        },
        {
            "ordId":"590909308792049555",
            "newSz":"2",
            "instId":"BTC-USDT"
        }
    ]
    
    
    
    import okx.Trade as Trade
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # Production trading: 0, Demo trading: 1
    
    tradeAPI = Trade.TradeAPI(apikey, secretkey, passphrase, False, flag)
    
    # Amend incomplete orders in batches by ordId
    amend_orders_with_orderId = [
        {"instId": "BTC-USDT", "ordId": "590909308792049444","newSz":"2"},
        {"instId": "BTC-USDT", "ordId": "590909308792049555","newSz":"2"}
    ]
    
    result = tradeAPI.amend_multiple_orders(amend_orders_with_orderId)
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
instId | String | Yes | Instrument ID  
cxlOnFail | Boolean | No | Whether the order needs to be automatically canceled when the order amendment fails  
Valid options: `false` or `true`, the default is `false`.   
Amendment failure scenarios include: `newSz` not a multiple of `lotSz`, position or risk limit breach, etc. When `false` (default): the original order continues unchanged after a failed amendment. When `true`: the original order is auto-cancelled on any amendment failure.  
ordId | String | Conditional | Order ID   
Either `ordId` or `clOrdId`is required, if both are passed, `ordId` will be used.  
clOrdId | String | Conditional | Client Order ID as assigned by the client  
reqId | String | No | Client Request ID as assigned by the client for order amendment   
A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters.   
The response will include the corresponding `reqId` to help you identify the request if you provide it in the request.  
newSz | String | Conditional | New **total** target quantity after amendment, must be > 0\. This is the desired total order size, not the remaining unfilled portion. For a partially-filled order: if 3 contracts are already filled and you want a total of 8, pass `newSz=8` (not 5). The system will attempt to fill the remaining 5. At least one of `newSz` or `newPx` (or `newPxUsd`/`newPxVol` for options) must be provided.  
newPx | String | Conditional | New price after amendment.   
When modifying options orders, users can only fill in one of the following: newPx, newPxUsd, or newPxVol. It must be consistent with parameters when placing orders. For example, if users placed the order using px, they should use newPx when modifying the order. At least one of `newSz` or `newPx` must be provided.  
speedBump | String | Conditional | Speed bump  
`1`: Event contract speed bumps (the delay duration will be changed subject to adjustment without prior notice). Required for non-post-only orders of `EVENTS` symbols.  
newPxUsd | String | Conditional | Modify options orders using USD prices   
Only applicable to options.   
When modifying options orders, users can only fill in one of the following: newPx, newPxUsd, or newPxVol.  
newPxVol | String | Conditional | Modify options orders based on implied volatility, where 1 represents 100%   
Only applicable to options.   
When modifying options orders, users can only fill in one of the following: newPx, newPxUsd, or newPxVol.  
pxAmendType | String | No | The price amendment type for orders  
`0`: Do not allow the system to amend to order price if `newPx` exceeds the price limit   
`1`: Allow the system to amend the price to the best available value within the price limit if `newPx` exceeds the price limit  
The default value is `0`  
attachAlgoOrds | Array of objects | No | Attached TP/SL or trailing stop order information  
> attachAlgoId | String | Conditional | The order ID of the attached TP/SL or trailing stop order. It is required to identify the attached order when amending. It will not be posted to algoId when placing the attached algo order after the general order is filled completely.  
> attachAlgoClOrdId | String | Conditional | Client-supplied Algo ID when placing order with attached TP/SL or trailing stop  
A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters.  
It will be posted to `algoClOrdId` when placing the attached algo order once the general order is filled completely.  
> newTpTriggerPx | String | Conditional | Take-profit trigger price.   
Either the take profit trigger price or order price is 0, it means that the take profit is deleted.  
> newTpTriggerRatio | String | Conditional | Take profit trigger ratio, 0.3 represents 30%   
Only applicable to FUTURES and SWAP.   
Only one of `newTpTriggerPx` and `newTpTriggerRatio` can be passed   
If the main order is a buy order, it must be greater than 0, and if the main order is a sell order, it must be between -1 and 0.   
0 means to delete the take-profit.  
> newTpOrdPx | String | Conditional | Take-profit order price  
If the price is -1, take-profit will be executed at the market price.  
> newTpOrdKind | String | No | TP order kind  
`condition`  
`limit`  
> newSlTriggerPx | String | Conditional | Stop-loss trigger price  
Either the stop loss trigger price or order price is 0, it means that the stop loss is deleted.  
> newSlTriggerRatio | String | Conditional | Stop-loss trigger ratio, 0.3 represents 30%   
Only applicable to FUTURES and SWAP.   
Only one of `newSlTriggerPx` and `newSlTriggerRatio` can be passed   
If the main order is a buy order, it must be between 0 and 1, and if the main order is a sell order, it must be greater than 0.   
0 means to delete the stop-loss.  
> newSlOrdPx | String | Conditional | Stop-loss order price  
If the price is -1, stop-loss will be executed at the market price.  
> newTpTriggerPxType | String | Conditional | Take-profit trigger price type  
`last`: last price   
`index`: index price   
`mark`: mark price  
Only applicable to `FUTURES`/`SWAP`  
If you want to add the take-profit, this parameter is required  
> newSlTriggerPxType | String | Conditional | Stop-loss trigger price type  
`last`: last price   
`index`: index price   
`mark`: mark price  
Only applicable to `FUTURES`/`SWAP`  
If you want to add the stop-loss, this parameter is required  
> sz | String | Conditional | New size. Only applicable to TP order of split TPs, and it is required for TP order of split TPs  
> amendPxOnTriggerType | String | No | Whether to enable Cost-price SL. Only applicable to SL order of split TPs.   
`0`: disable, the default value   
`1`: Enable  
> newCallbackRatio | String | Conditional | New callback ratio, e.g. `0.05` represents 5%.  
Either `newCallbackRatio` or `newCallbackSpread` can be passed. Only one can be passed.  
Only applicable when `ordType` = `move_order_stop`  
> newCallbackSpread | String | Conditional | New callback spread (price distance).  
Either `newCallbackRatio` or `newCallbackSpread` can be passed. Only one can be passed.  
Only applicable when `ordType` = `move_order_stop`  
> newActivePx | String | No | New activation price.  
Only applicable when `ordType` = `move_order_stop`  
  
> Response Example
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
            {
                "clOrdId":"oktswap6",
                "ordId":"12345689",
                "ts":"1695190491421",
                "reqId":"b12344",
                "sCode":"0",
                "sMsg":"",
                "subCode": ""
            },
            {
                "clOrdId":"oktswap7",
                "ordId":"12344",
                "ts":"1695190491421",
                "reqId":"b12344",
                "sCode":"0",
                "sMsg":"",
                "subCode": ""
            }
        ],
        "inTime": "1695190491421339",
        "outTime": "1695190491423240"
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
code | String | The result code, `0` means success  
msg | String | The error message, empty if the code is 0  
data | Array of objects | Array of objects contains the response results  
> ordId | String | Order ID  
> clOrdId | String | Client Order ID as assigned by the client  
> ts | String | Timestamp when the order request processing is finished by our system, Unix timestamp format in milliseconds, e.g. `1597026383085`  
> reqId | String | Client Request ID as assigned by the client for order amendment.  
> sCode | String | The code of the event execution result, `0` means success.  
> sMsg | String | Rejection message if the request is unsuccessful.  
> subCode | String | Sub-code of sCode.  
Returns `""` when sCode is 0 (request successful).  
When sCode is not 0 (request failed), returns the sub-code if available; otherwise returns `""`.  
inTime | String | Timestamp at REST gateway when the request is received, Unix timestamp format in microseconds, e.g. `1597026383085123`   
The time is recorded after authentication.  
outTime | String | Timestamp at REST gateway when the response is sent, Unix timestamp format in microseconds, e.g. `1597026383085123`  
newSz   
If the new quantity of the order is less than or equal to the filled quantity when you are amending a partially-filled order, the order status will be changed to filled. 

### POST / Close positions

Close the position of an instrument via a market order.

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule (except Options): User ID + Instrument ID

#### Rate limit rule (Options only): User ID + Instrument Family

#### Permission: Trade

#### HTTP Request

`POST /api/v5/trade/close-position`

> Request Example
    
    
    POST /api/v5/trade/close-position
    body
    {
        "instId":"BTC-USDT-SWAP",
        "mgnMode":"cross"
    }
    
    
    
    import okx.Trade as Trade
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # Production trading: 0, Demo trading: 1
    
    tradeAPI = Trade.TradeAPI(apikey, secretkey, passphrase, False, flag)
    
    # Close the position of an instrument via a market order
    result = tradeAPI.close_positions(
        instId="BTC-USDT-SWAP",
        mgnMode="cross"
    )
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
instId | String | Yes | Instrument ID  
posSide | String | Conditional | Position side   
This parameter can be omitted in `net` mode, and the default value is `net`. You can only fill with `net`.  
This parameter must be filled in under the `long/short` mode. Fill in `long` for close-long and `short` for close-short.  
mgnMode | String | Yes | Margin mode  
`cross` `isolated`  
ccy | String | Conditional | Margin currency, required in the case of closing `cross` `MARGIN` position for `Futures mode`.  
autoCxl | Boolean | No | Whether any pending orders for closing out needs to be automatically canceled when close position via a market order.  
`false` or `true`, the default is `false`.  
clOrdId | String | No | Client-supplied ID  
A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters.  
tag | String | No | Order tag  
A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 16 characters.  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "clOrdId": "",
                "instId": "BTC-USDT-SWAP",
                "posSide": "long",
                "tag": ""
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
instId | String | Instrument ID  
posSide | String | Position side  
clOrdId | String | Client-supplied ID  
A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters.  
tag | String | Order tag  
A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 16 characters.  
if there are any pending orders for closing out and the orders do not need to be automatically canceled, it will return an error code and message to prompt users to cancel pending orders before closing the positions.   

### GET / Order details

Retrieve order details.

#### Rate Limit: 60 requests per 2 seconds

#### Rate limit rule (except Options): User ID + Instrument ID

#### Rate limit rule (Options only): User ID + Instrument Family

#### Permission: Read

#### HTTP Request

`GET /api/v5/trade/order`

> Request Example
    
    
    GET /api/v5/trade/order?ordId=1753197687182819328&instId=BTC-USDT
    
    
    
    
    import okx.Trade as Trade
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # Production trading: 0, Demo trading: 1
    
    tradeAPI = Trade.TradeAPI(apikey, secretkey, passphrase, False, flag)
    
    # Retrieve order details by ordId
    result = tradeAPI.get_order(
        instId="BTC-USDT",
        ordId="680800019749904384"
    )
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
instId | String | Yes | Instrument ID, e.g. `BTC-USDT`  
Only applicable to live instruments  
ordId | String | Conditional | Order ID   
Either `ordId` or `clOrdId` is required, if both are passed, `ordId` will be used  
clOrdId | String | Conditional | Client Order ID as assigned by the client  
If the `clOrdId` is associated with multiple orders, only the latest one will be returned.  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "accFillSz": "0.00192834",
                "algoClOrdId": "",
                "algoId": "",
                "attachAlgoClOrdId": "",
                "attachAlgoOrds": [],
                "avgPx": "51858",
                "cTime": "1708587373361",
                "cancelSource": "",
                "cancelSourceReason": "",
                "category": "normal",
                "ccy": "",
                "clOrdId": "",
                "fee": "-0.00000192834",
                "feeCcy": "BTC",
                "fillPx": "51858",
                "fillSz": "0.00192834",
                "fillTime": "1708587373361",
                "instId": "BTC-USDT",
                "instType": "SPOT",
                "isTpLimit": "false",
                "lever": "",
                "linkedAlgoOrd": {
                    "algoId": ""
                },
                "ordId": "680800019749904384",
                "ordType": "market",
                "pnl": "0",
                "posSide": "net",
                "px": "",
                "pxType": "",
                "pxUsd": "",
                "pxVol": "",
                "quickMgnType": "",
                "rebate": "0",
                "rebateCcy": "USDT",
                "reduceOnly": "false",
                "side": "buy",
                "slOrdPx": "",
                "slTriggerPx": "",
                "slTriggerPxType": "",
                "source": "",
                "state": "filled",
                "stpId": "",
                "stpMode": "",
                "sz": "100",
                "tag": "",
                "tdMode": "cash",
                "tgtCcy": "quote_ccy",
                "tpOrdPx": "",
                "tpTriggerPx": "",
                "tpTriggerPxType": "",
                "tradeId": "744876980",
                "tradeQuoteCcy": "USDT",
                "uTime": "1708587373362"
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
instType | String | Instrument type  
`SPOT`  
`MARGIN`  
`SWAP`  
`FUTURES`  
`OPTION`  
`EVENTS`  
instId | String | Instrument ID  
tgtCcy | String | Order quantity unit setting for `sz`  
`base_ccy`: Base currency ,`quote_ccy`: Quote currency   
Only applicable to `SPOT` Market Orders  
Default is `quote_ccy` for buy, `base_ccy` for sell  
ccy | String | Margin currency   
Applicable to all `isolated` `MARGIN` orders and `cross` `MARGIN` orders in `Futures mode`, `FUTURES` and `SWAP` contracts.  
ordId | String | Order ID  
clOrdId | String | Client Order ID as assigned by the client  
tag | String | Order tag  
px | String | Price  
For options, use coin as unit (e.g. BTC, ETH)  
pxUsd | String | Options price in USDOnly applicable to options; return "" for other instrument types  
pxVol | String | Implied volatility of the options orderOnly applicable to options; return "" for other instrument types  
pxType | String | Price type of options   
`px`: Place an order based on price, in the unit of coin (the unit for the request parameter px is BTC or ETH)   
`pxVol`: Place an order based on pxVol   
`pxUsd`: Place an order based on pxUsd, in the unit of USD (the unit for the request parameter px is USD)  
sz | String | Quantity to buy or sell  
pnl | String | Profit and loss (excluding the fee).  
Applicable to orders which have a trade and aim to close position. It always is 0 in other conditions  
ordType | String | Order type   
`market`: Market order   
`limit`: Limit order   
`post_only`: Post-only order   
`fok`: Fill-or-kill order   
`ioc`: Immediate-or-cancel order   
`optimal_limit_ioc`: Market order with immediate-or-cancel order  
`mmp`: Market Maker Protection (only applicable to Option in Portfolio Margin mode)  
`mmp_and_post_only`: Market Maker Protection and Post-only order(only applicable to Option in Portfolio Margin mode)   
`op_fok`: Simple options (fok)  
`elp`: Enhanced Liquidity Program order  
side | String | Order side  
posSide | String | Position side  
tdMode | String | Trade mode  
accFillSz | String | Running total of filled quantity since order creation. In WebSocket order channel push events, `accFillSz` always represents the cumulative total, not the increment since the last push.  
The unit is `base_ccy` for SPOT and MARGIN, e.g. BTC-USDT, the unit is BTC;  
The unit is contract for `FUTURES`/`SWAP`/`OPTION`  
fillPx | String | Last filled price. If none is filled, it will return "".  
tradeId | String | Last traded ID  
fillSz | String | Quantity of the most recent individual fill event (not cumulative). For the running total of all fills, use `accFillSz`.  
The unit is `base_ccy` for SPOT and MARGIN, e.g. BTC-USDT, the unit is BTC;  
The unit is contract for `FUTURES`/`SWAP`/`OPTION`  
fillTime | String | Last filled time  
avgPx | String | Average filled price. If none is filled, it will return "".  
state | String | Order state:  
`live`: on the order book, no fills yet.  
`partially_filled`: partially executed, still active on book.  
`filled`: fully executed, terminal state.  
`canceled`: cancelled, terminal state. For IOC orders partially filled before cancellation, `accFillSz` may be non-zero.  
`mmp_canceled`: automatically cancelled by Market Maker Protection, terminal state.  
Note: GET /api/v5/trade/orders-pending only returns `live` and `partially_filled`; GET /api/v5/trade/orders-history returns `filled`, `canceled`, and `mmp_canceled`.  
stpId | String | ~~Self trade prevention ID  
Return "" if self trade prevention is not applicable~~ (Deprecated)  
stpMode | String | Self trade prevention mode  
lever | String | Leverage, from `0.01` to `125`.   
Only applicable to `MARGIN/FUTURES/SWAP`  
attachAlgoClOrdId | String | Client-supplied Algo ID when placing order with attached TP/SL or trailing stop.  
tpTriggerPx | String | Take-profit trigger price.  
tpTriggerPxType | String | Take-profit trigger price type.   
`last`: last price  
`index`: index price  
`mark`: mark price  
tpOrdPx | String | Take-profit order price.  
slTriggerPx | String | Stop-loss trigger price.  
slTriggerPxType | String | Stop-loss trigger price type.   
`last`: last price  
`index`: index price  
`mark`: mark price  
slOrdPx | String | Stop-loss order price.  
attachAlgoOrds | Array of objects | Attached TP/SL or trailing stop order information  
> attachAlgoId | String | The order ID of the attached TP/SL or trailing stop order. It can be used to identify the attached order when amending. It will not be posted to algoId when placing the attached algo order after the general order is filled completely.  
> attachAlgoClOrdId | String | Client-supplied Algo ID when placing order with attached TP/SL or trailing stop  
A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters.  
It will be posted to `algoClOrdId` when placing the attached algo order once the general order is filled completely.  
> tpOrdKind | String | TP order kind  
`condition`  
`limit`  
> tpTriggerPx | String | Take-profit trigger price.  
> tpTriggerRatio | String | Take profit trigger ratio, 0.3 represents 30%   
Only applicable to FUTURES and SWAP.  
> tpTriggerPxType | String | Take-profit trigger price type.   
`last`: last price  
`index`: index price  
`mark`: mark price  
> tpOrdPx | String | Take-profit order price.  
> slTriggerPx | String | Stop-loss trigger price.  
> slTriggerRatio | String | Stop-loss trigger ratio, 0.3 represents 30%   
Only applicable to FUTURES and SWAP.  
> slTriggerPxType | String | Stop-loss trigger price type.   
`last`: last price  
`index`: index price  
`mark`: mark price  
> slOrdPx | String | Stop-loss order price.  
> sz | String | Size. Only applicable to TP order of split TPs  
> amendPxOnTriggerType | String | Whether to enable Cost-price SL. Only applicable to SL order of split TPs.   
`0`: disable, the default value   
`1`: Enable  
> callbackRatio | String | Callback ratio, e.g. `0.05` represents 5%  
> callbackSpread | String | Callback spread (price distance)  
> activePx | String | Activation price  
> failCode | String | The error code when failing to place TP/SL order, e.g. 51020   
The default is ""  
> failReason | String | The error reason when failing to place TP/SL order.   
The default is ""  
linkedAlgoOrd | Object | Linked SL order detail, only applicable to the order that is placed by one-cancels-the-other (OCO) order that contains the TP limit order.  
> algoId | String | Algo ID  
feeCcy | String | Fee currency  
For maker sell orders of Spot and Margin, this represents the quote currency. For all other cases, it represents the currency in which fees are charged.  
fee | String | Fee amount. Sign convention: negative = net fee paid to platform; positive = net rebate received from platform. The net amount reflects fee minus rebate.  
For Spot and Margin (excluding maker sell orders): accumulated fee charged by the platform, always negative.  
For maker sell orders in Spot and Margin, Expiry Futures, Perpetual Futures and Options: accumulated fee and rebate (always in quote currency for maker sell orders in Spot and Margin).  
For split accounting, use `feeCcy` \+ `fee` together with `rebateCcy` \+ `rebate`. `feeCcy` and `rebateCcy` may differ.  
rebateCcy | String | Rebate currency  
For maker sell orders of Spot and Margin, this represents the base currency. For all other cases, it represents the currency in which rebates are paid.  
rebate | String | Rebate amount, only applicable to Spot and Margin  
For maker sell orders: ~~Accumulated fee and~~ rebate amount in the unit of base currency.  
For all other cases, it represents the maker rebate amount, always positive, return "" if no rebate.  
source | String | Order source (non-exhaustive — handle unknown values gracefully as new types may be added):  
`6`: The normal order triggered by the `trigger order`  
`7`: The normal order triggered by the `TP/SL order`   
`13`: The normal order triggered by the algo order  
`25`: The normal order triggered by the `trailing stop order`  
`34`: The normal order triggered by the chase order.  
All values represent system-generated child orders triggered by parent algo or strategy orders.  
category | String | Category:  
`normal`: standard user-placed order.  
`twap`: forced repayment order generated by the system (not a TWAP algorithmic strategy).  
`adl`: auto-deleveraging, system-triggered position reduction.  
`full_liquidation`: forced full position close due to margin breach.  
`partial_liquidation`: forced partial position close.  
`delivery`: futures/options expiry settlement execution.  
`ddh`: delta dynamic hedge order placed by the options market-maker system.  
`auto_conversion`: system-triggered asset conversion.  
reduceOnly | String | Whether the order can only reduce the position size. Valid options: true or false.  
isTpLimit | String | Whether it is TP limit order. true or false  
cancelSource | String | Code of the cancellation source.  
cancelSourceReason | String | Reason for the cancellation.  
quickMgnType | String | ~~Quick Margin type, Only applicable to Quick Margin Mode of isolated margin  
`manual`, `auto_borrow`, `auto_repay`~~ (Deprecated)  
algoClOrdId | String | Client-supplied Algo ID. There will be a value when algo order attaching `algoClOrdId` is triggered, or it will be "".  
algoId | String | Algo ID. There will be a value when algo order is triggered, or it will be "".  
uTime | String | Update time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
cTime | String | Creation time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
tradeQuoteCcy | String | The quote currency used for trading.  
outcome | String | The market outcome the user traded on.  
`yes`  
`no`  
Only applicable to `EVENTS`  
  
### GET / Order List

Retrieve all incomplete orders under the current account.

#### Rate Limit: 60 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/trade/orders-pending`

> Request Example
    
    
    GET /api/v5/trade/orders-pending?ordType=post_only,fok,ioc&instType=SPOT
    
    
    
    
    import okx.Trade as Trade
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # Production trading: 0, Demo trading: 1
    
    tradeAPI = Trade.TradeAPI(apikey, secretkey, passphrase, False, flag)
    
    # Retrieve all incomplete orders
    result = tradeAPI.get_order_list(
        instType="SPOT",
        ordType="post_only,fok,ioc"
    )
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
instType | String | No | Instrument type  
`SPOT`  
`MARGIN`  
`SWAP`  
`FUTURES`  
`OPTION`  
`EVENTS`  
instFamily | String | No | Instrument family  
Applicable to `FUTURES`/`SWAP`/`OPTION`  
instId | String | No | Instrument ID, e.g. `BTC-USD-200927`  
ordType | String | No | Order type   
`market`: Market order   
`limit`: Limit order   
`post_only`: Post-only order   
`fok`: Fill-or-kill order   
`ioc`: Immediate-or-cancel order   
`optimal_limit_ioc`: Market order with immediate-or-cancel order   
`mmp`: Market Maker Protection (only applicable to Option in Portfolio Margin mode)  
`mmp_and_post_only`: Market Maker Protection and Post-only order(only applicable to Option in Portfolio Margin mode)   
`op_fok`: Simple options (fok)  
`elp`: Enhanced Liquidity Program order  
state | String | No | State  
`live`   
`partially_filled`  
after | String | No | Pagination of data to return records earlier than the requested `ordId`  
before | String | No | Pagination of data to return records newer than the requested `ordId`  
limit | String | No | Number of results per request. The maximum is `100`; The default is `100`  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "accFillSz": "0",
                "algoClOrdId": "",
                "algoId": "",
                "attachAlgoClOrdId": "",
                "attachAlgoOrds": [],
                "avgPx": "",
                "cTime": "1724733617998",
                "cancelSource": "",
                "cancelSourceReason": "",
                "category": "normal",
                "ccy": "",
                "clOrdId": "",
                "fee": "0",
                "feeCcy": "BTC",
                "fillPx": "",
                "fillSz": "0",
                "fillTime": "",
                "instId": "BTC-USDT",
                "instType": "SPOT",
                "isTpLimit": "false",
                "lever": "",
                "linkedAlgoOrd": {
                    "algoId": ""
                },
                "ordId": "1752588852617379840",
                "ordType": "post_only",
                "pnl": "0",
                "posSide": "net",
                "px": "13013.5",
                "pxType": "",
                "pxUsd": "",
                "pxVol": "",
                "quickMgnType": "",
                "rebate": "0",
                "rebateCcy": "USDT",
                "reduceOnly": "false",
                "side": "buy",
                "slOrdPx": "",
                "slTriggerPx": "",
                "slTriggerPxType": "",
                "source": "",
                "state": "live",
                "stpId": "",
                "stpMode": "cancel_maker",
                "sz": "0.001",
                "tag": "",
                "tdMode": "cash",
                "tgtCcy": "",
                "tpOrdPx": "",
                "tpTriggerPx": "",
                "tpTriggerPxType": "",
                "tradeId": "",
                "tradeQuoteCcy": "USDT",
                "uTime": "1724733617998"
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
instType | String | Instrument type  
`SPOT`  
`MARGIN`  
`SWAP`  
`FUTURES`  
`OPTION`  
`EVENTS`  
instId | String | Instrument ID  
tgtCcy | String | Order quantity unit setting for `sz`  
`base_ccy`: Base currency ,`quote_ccy`: Quote currency   
Only applicable to `SPOT` Market Orders  
Default is `quote_ccy` for buy, `base_ccy` for sell  
ccy | String | Margin currency   
Applicable to all `isolated` `MARGIN` orders and `cross` `MARGIN` orders in `Futures mode`, `FUTURES` and `SWAP` contracts.  
ordId | String | Order ID  
clOrdId | String | Client Order ID as assigned by the client  
tag | String | Order tag  
px | String | Price   
For options, use coin as unit (e.g. BTC, ETH)  
pxUsd | String | Options price in USD  
Only applicable to options; return "" for other instrument types  
pxVol | String | Implied volatility of the options order  
Only applicable to options; return "" for other instrument types  
pxType | String | Price type of options   
`px`: Place an order based on price, in the unit of coin (the unit for the request parameter px is BTC or ETH)   
`pxVol`: Place an order based on pxVol   
`pxUsd`: Place an order based on pxUsd, in the unit of USD (the unit for the request parameter px is USD)  
sz | String | Quantity to buy or sell  
pnl | String | Profit and loss (excluding the fee).  
Applicable to orders which have a trade and aim to close position. It always is 0 in other conditions  
ordType | String | Order type   
`market`: Market order   
`limit`: Limit order   
`post_only`: Post-only order   
`fok`: Fill-or-kill order   
`ioc`: Immediate-or-cancel order   
`optimal_limit_ioc`: Market order with immediate-or-cancel order  
`mmp`: Market Maker Protection (only applicable to Option in Portfolio Margin mode)  
`mmp_and_post_only`: Market Maker Protection and Post-only order(only applicable to Option in Portfolio Margin mode)   
`op_fok`: Simple options (fok)  
`elp`: Enhanced Liquidity Program order  
side | String | Order side  
posSide | String | Position side  
tdMode | String | Trade mode  
accFillSz | String | Accumulated fill quantity  
fillPx | String | Last filled price  
tradeId | String | Last trade ID  
fillSz | String | Last filled quantity  
fillTime | String | Last filled time  
avgPx | String | Average filled price. If none is filled, it will return "".  
state | String | State  
`live`   
`partially_filled`  
lever | String | Leverage, from `0.01` to `125`.   
Only applicable to `MARGIN/FUTURES/SWAP`  
attachAlgoClOrdId | String | Client-supplied Algo ID when placing order with attached TP/SL or trailing stop.  
tpTriggerPx | String | Take-profit trigger price.  
tpTriggerPxType | String | Take-profit trigger price type.   
`last`: last price  
`index`: index price  
`mark`: mark price  
tpOrdPx | String | Take-profit order price.  
slTriggerPx | String | Stop-loss trigger price.  
slTriggerPxType | String | Stop-loss trigger price type.   
`last`: last price  
`index`: index price  
`mark`: mark price  
slOrdPx | String | Stop-loss order price.  
attachAlgoOrds | Array of objects | Attached TP/SL or trailing stop order information  
> attachAlgoId | String | The order ID of the attached TP/SL or trailing stop order. It can be used to identify the attached order when amending. It will not be posted to algoId when placing the attached algo order after the general order is filled completely.  
> attachAlgoClOrdId | String | Client-supplied Algo ID when placing order with attached TP/SL or trailing stop  
A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters.  
It will be posted to `algoClOrdId` when placing the attached algo order once the general order is filled completely.  
> tpOrdKind | String | TP order kind  
`condition`  
`limit`  
> tpTriggerPx | String | Take-profit trigger price.  
> tpTriggerRatio | String | Take profit trigger ratio, 0.3 represents 30%   
Only applicable to FUTURES and SWAP.  
> tpTriggerPxType | String | Take-profit trigger price type.   
`last`: last price  
`index`: index price  
`mark`: mark price  
> tpOrdPx | String | Take-profit order price.  
> slTriggerPx | String | Stop-loss trigger price.  
> slTriggerRatio | String | Stop-loss trigger ratio, 0.3 represents 30%   
Only applicable to FUTURES and SWAP.  
> slTriggerPxType | String | Stop-loss trigger price type.   
`last`: last price  
`index`: index price  
`mark`: mark price  
> slOrdPx | String | Stop-loss order price.  
> sz | String | Size. Only applicable to TP order of split TPs  
> amendPxOnTriggerType | String | Whether to enable Cost-price SL. Only applicable to SL order of split TPs.   
`0`: disable, the default value   
`1`: Enable  
> callbackRatio | String | Callback ratio, e.g. `0.05` represents 5%  
> callbackSpread | String | Callback spread (price distance)  
> activePx | String | Activation price  
> failCode | String | The error code when failing to place TP/SL order, e.g. 51020   
The default is ""  
> failReason | String | The error reason when failing to place TP/SL order.   
The default is ""  
linkedAlgoOrd | Object | Linked SL order detail, only applicable to the order that is placed by one-cancels-the-other (OCO) order that contains the TP limit order.  
> algoId | String | Algo ID  
stpId | String | ~~Self trade prevention ID  
Return "" if self trade prevention is not applicable~~ (Deprecated)  
stpMode | String | Self trade prevention mode  
feeCcy | String | Fee currency  
For maker sell orders of Spot and Margin, this represents the quote currency. For all other cases, it represents the currency in which fees are charged.  
fee | String | Fee amount  
For Spot and Margin (excluding maker sell orders): accumulated fee charged by the platform, always negative  
For maker sell orders in Spot and Margin, Expiry Futures, Perpetual Futures and Options: accumulated fee and rebate (always in quote currency for maker sell orders in Spot and Margin)  
rebateCcy | String | Rebate currency  
For maker sell orders of Spot and Margin, this represents the base currency. For all other cases, it represents the currency in which rebates are paid.  
rebate | String | Rebate amount, only applicable to Spot and Margin  
For maker sell orders: ~~Accumulated fee and~~ rebate amount in the unit of base currency.  
For all other cases, it represents the maker rebate amount, always positive, return "" if no rebate.  
source | String | Order source  
`6`: The normal order triggered by the `trigger order`  
`7`: The normal order triggered by the `TP/SL order`   
`13`: The normal order triggered by the algo order  
`25`: The normal order triggered by the `trailing stop order`  
`34`: The normal order triggered by the chase order  
category | String | Category   
`normal`  
reduceOnly | String | Whether the order can only reduce the position size. Valid options: true or false.  
quickMgnType | String | ~~Quick Margin type, Only applicable to Quick Margin Mode of isolated margin  
`manual`, `auto_borrow`, `auto_repay`~~ (Deprecated)  
algoClOrdId | String | Client-supplied Algo ID. There will be a value when algo order attaching `algoClOrdId` is triggered, or it will be "".  
algoId | String | Algo ID. There will be a value when algo order is triggered, or it will be "".  
isTpLimit | String | Whether it is TP limit order. true or false  
uTime | String | Update time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
cTime | String | Creation time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
cancelSource | String | Code of the cancellation source.  
cancelSourceReason | String | Reason for the cancellation.  
tradeQuoteCcy | String | The quote currency used for trading.  
outcome | String | The market outcome the user traded on.  
`yes`  
`no`  
Only applicable to `EVENTS`  
  
### GET / Order history (last 7 days)

Get completed orders which are placed in the last 7 days, including those placed 7 days ago but completed in the last 7 days.   

The incomplete orders that have been canceled are only reserved for 2 hours.

#### Rate Limit: 40 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/trade/orders-history`

> Request Example
    
    
    GET /api/v5/trade/orders-history?ordType=post_only,fok,ioc&instType=SPOT
    
    
    
    
    import okx.Trade as Trade
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # Production trading: 0, Demo trading: 1
    
    tradeAPI = Trade.TradeAPI(apikey, secretkey, passphrase, False, flag)
    
    # Get completed SPOT orders which are placed in the last 7 days
    # The incomplete orders that have been canceled are only reserved for 2 hours
    result = tradeAPI.get_orders_history(
        instType="SPOT",
        ordType="post_only,fok,ioc"
    )
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
instType | String | yes | Instrument type  
`SPOT`  
`MARGIN`  
`SWAP`  
`FUTURES`  
`OPTION`  
`EVENTS`  
instFamily | String | No | Instrument family  
Applicable to `FUTURES`/`SWAP`/`OPTION`  
instId | String | No | Instrument ID, e.g. `BTC-USDT`  
ordType | String | No | Order type  
`market`: market order   
`limit`: limit order   
`post_only`: Post-only order   
`fok`: Fill-or-kill order   
`ioc`: Immediate-or-cancel order   
`optimal_limit_ioc`: Market order with immediate-or-cancel order  
`mmp`: Market Maker Protection (only applicable to Option in Portfolio Margin mode)  
`mmp_and_post_only`: Market Maker Protection and Post-only order(only applicable to Option in Portfolio Margin mode)   
`op_fok`: Simple options (fok)   
`elp`: Enhanced Liquidity Program order  
state | String | No | State  
`canceled`  
`filled`  
`mmp_canceled`: Order canceled automatically due to Market Maker Protection  
category | String | No | Category   
`twap`   
`adl`  
`full_liquidation`  
`partial_liquidation`   
`delivery`   
`ddh`: Delta dynamic hedge  
after | String | No | Pagination of data to return records earlier than the requested `ordId`  
before | String | No | Pagination of data to return records newer than the requested `ordId`  
begin | String | No | Filter with a begin timestamp `cTime`. Unix timestamp format in milliseconds, e.g. 1597026383085  
end | String | No | Filter with an end timestamp `cTime`. Unix timestamp format in milliseconds, e.g. 1597026383085  
limit | String | No | Number of results per request. The maximum is `100`; The default is `100`  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "accFillSz": "0.00192834",
                "algoClOrdId": "",
                "algoId": "",
                "attachAlgoClOrdId": "",
                "attachAlgoOrds": [],
                "avgPx": "51858",
                "cTime": "1708587373361",
                "cancelSource": "",
                "cancelSourceReason": "",
                "category": "normal",
                "ccy": "",
                "clOrdId": "",
                "fee": "-0.00000192834",
                "feeCcy": "BTC",
                "fillPx": "51858",
                "fillSz": "0.00192834",
                "fillTime": "1708587373361",
                "instId": "BTC-USDT",
                "instType": "SPOT",
                "lever": "",
                "linkedAlgoOrd": {
                    "algoId": ""
                },
                "ordId": "680800019749904384",
                "ordType": "market",
                "pnl": "0",
                "posSide": "",
                "px": "",
                "pxType": "",
                "pxUsd": "",
                "pxVol": "",
                "quickMgnType": "",
                "rebate": "0",
                "rebateCcy": "USDT",
                "reduceOnly": "false",
                "side": "buy",
                "slOrdPx": "",
                "slTriggerPx": "",
                "slTriggerPxType": "",
                "source": "",
                "state": "filled",
                "stpId": "",
                "stpMode": "",
                "sz": "100",
                "tag": "",
                "tdMode": "cash",
                "tgtCcy": "quote_ccy",
                "tpOrdPx": "",
                "tpTriggerPx": "",
                "tpTriggerPxType": "",
                "tradeId": "744876980",
                "tradeQuoteCcy": "USDT",
                "uTime": "1708587373362",
                "isTpLimit": "false"
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
instType | String | Instrument type  
`SPOT`  
`MARGIN`  
`SWAP`  
`FUTURES`  
`OPTION`  
`EVENTS`  
instId | String | Instrument ID  
tgtCcy | String | Order quantity unit setting for `sz`  
`base_ccy`: Base currency ,`quote_ccy`: Quote currency   
Only applicable to `SPOT` Market Orders  
Default is `quote_ccy` for buy, `base_ccy` for sell  
ccy | String | Margin currency   
Applicable to all `isolated` `MARGIN` orders and `cross` `MARGIN` orders in `Futures mode`, `FUTURES` and `SWAP` contracts.  
ordId | String | Order ID  
clOrdId | String | Client Order ID as assigned by the client  
tag | String | Order tag  
px | String | Price   
For options, use coin as unit (e.g. BTC, ETH)  
pxUsd | String | Options price in USD  
Only applicable to options; return "" for other instrument types  
pxVol | String | Implied volatility of the options order  
Only applicable to options; return "" for other instrument types  
pxType | String | Price type of options   
`px`: Place an order based on price, in the unit of coin (the unit for the request parameter px is BTC or ETH)   
`pxVol`: Place an order based on pxVol   
`pxUsd`: Place an order based on pxUsd, in the unit of USD (the unit for the request parameter px is USD)  
sz | String | Quantity to buy or sell  
ordType | String | Order type   
`market`: market order   
`limit`: limit order   
`post_only`: Post-only order   
`fok`: Fill-or-kill order   
`ioc`: Immediate-or-cancel order   
`optimal_limit_ioc`: Market order with immediate-or-cancel order  
`mmp`: Market Maker Protection (only applicable to Option in Portfolio Margin mode)  
`mmp_and_post_only`: Market Maker Protection and Post-only order(only applicable to Option in Portfolio Margin mode)   
`op_fok`: Simple options (fok)  
`elp`: Enhanced Liquidity Program order  
side | String | Order side  
posSide | String | Position side  
tdMode | String | Trade mode  
accFillSz | String | Accumulated fill quantity  
fillPx | String | Last filled price. If none is filled, it will return "".  
tradeId | String | Last trade ID  
fillSz | String | Last filled quantity  
fillTime | String | Last filled time  
avgPx | String | Average filled price. If none is filled, it will return "".  
state | String | State   
`canceled`   
`filled`   
`mmp_canceled`  
lever | String | Leverage, from `0.01` to `125`.   
Only applicable to `MARGIN/FUTURES/SWAP`  
attachAlgoClOrdId | String | Client-supplied Algo ID when placing order with attached TP/SL or trailing stop.  
tpTriggerPx | String | Take-profit trigger price.  
tpTriggerPxType | String | Take-profit trigger price type.   
`last`: last price  
`index`: index price  
`mark`: mark price  
tpOrdPx | String | Take-profit order price.  
slTriggerPx | String | Stop-loss trigger price.  
slTriggerPxType | String | Stop-loss trigger price type.   
`last`: last price  
`index`: index price  
`mark`: mark price  
slOrdPx | String | Stop-loss order price.  
attachAlgoOrds | Array of objects | Attached TP/SL or trailing stop order information  
> attachAlgoId | String | The order ID of the attached TP/SL or trailing stop order. It can be used to identify the attached order when amending. It will not be posted to algoId when placing the attached algo order after the general order is filled completely.  
> attachAlgoClOrdId | String | Client-supplied Algo ID when placing order with attached TP/SL or trailing stop  
A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters.  
It will be posted to `algoClOrdId` when placing the attached algo order once the general order is filled completely.  
> tpOrdKind | String | TP order kind  
`condition`  
`limit`  
> tpTriggerPx | String | Take-profit trigger price.  
> tpTriggerRatio | String | Take profit trigger ratio, 0.3 represents 30%   
Only applicable to FUTURES and SWAP.  
> tpTriggerPxType | String | Take-profit trigger price type.   
`last`: last price  
`index`: index price  
`mark`: mark price  
> tpOrdPx | String | Take-profit order price.  
> slTriggerPx | String | Stop-loss trigger price.  
> slTriggerRatio | String | Stop-loss trigger ratio, 0.3 represents 30%   
Only applicable to FUTURES and SWAP.  
> slTriggerPxType | String | Stop-loss trigger price type.   
`last`: last price  
`index`: index price  
`mark`: mark price  
> slOrdPx | String | Stop-loss order price.  
> sz | String | Size. Only applicable to TP order of split TPs  
> amendPxOnTriggerType | String | Whether to enable Cost-price SL. Only applicable to SL order of split TPs.   
`0`: disable, the default value   
`1`: Enable  
> callbackRatio | String | Callback ratio, e.g. `0.05` represents 5%  
> callbackSpread | String | Callback spread (price distance)  
> activePx | String | Activation price  
> failCode | String | The error code when failing to place TP/SL order, e.g. 51020   
The default is ""  
> failReason | String | The error reason when failing to place TP/SL order.   
The default is ""  
linkedAlgoOrd | Object | Linked SL order detail, only applicable to the order that is placed by one-cancels-the-other (OCO) order that contains the TP limit order.  
> algoId | String | Algo ID  
stpId | String | ~~Self trade prevention ID  
Return "" if self trade prevention is not applicable~~ (Deprecated)  
stpMode | String | Self trade prevention mode  
feeCcy | String | Fee currency  
For maker sell orders of Spot and Margin, this represents the quote currency. For all other cases, it represents the currency in which fees are charged.  
fee | String | Fee amount  
For Spot and Margin (excluding maker sell orders): accumulated fee charged by the platform, always negative  
For maker sell orders in Spot and Margin, Expiry Futures, Perpetual Futures and Options: accumulated fee and rebate (always in quote currency for maker sell orders in Spot and Margin)  
rebateCcy | String | Rebate currency  
For maker sell orders of Spot and Margin, this represents the base currency. For all other cases, it represents the currency in which rebates are paid.  
rebate | String | Rebate amount, only applicable to Spot and Margin  
For maker sell orders: ~~Accumulated fee and~~ rebate amount in the unit of base currency.  
For all other cases, it represents the maker rebate amount, always positive, return "" if no rebate.  
source | String | Order source  
`6`: The normal order triggered by the `trigger order`  
`7`: The normal order triggered by the `TP/SL order`   
`13`: The normal order triggered by the algo order  
`25`: The normal order triggered by the `trailing stop order`  
`34`: The normal order triggered by the chase order  
pnl | String | Profit and loss (excluding the fee).  
Applicable to orders which have a trade and aim to close position. It always is 0 in other conditions  
category | String | Category   
`normal`  
`twap`   
`adl`  
`full_liquidation`  
`partial_liquidation`   
`delivery`   
`ddh`: Delta dynamic hedge  
`auto_conversion`  
reduceOnly | String | Whether the order can only reduce the position size. Valid options: true or false.  
cancelSource | String | Code of the cancellation source.  
cancelSourceReason | String | Reason for the cancellation.  
algoClOrdId | String | Client-supplied Algo ID. There will be a value when algo order attaching `algoClOrdId` is triggered, or it will be "".  
algoId | String | Algo ID. There will be a value when algo order is triggered, or it will be "".  
isTpLimit | String | Whether it is TP limit order. true or false  
uTime | String | Update time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
cTime | String | Creation time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
quickMgnType | String | ~~Quick Margin type, Only applicable to Quick Margin Mode of isolated margin  
`manual`, `auto_borrow`, `auto_repay`~~ (Deprecated)  
tradeQuoteCcy | String | The quote currency used for trading.  
outcome | String | The market outcome the user traded on.  
`yes`  
`no`  
Only applicable to `EVENTS`  
  
### GET / Order history (last 3 months)

Get completed orders which are placed in the last 3 months, including those placed 3 months ago but completed in the last 3 months.   

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/trade/orders-history-archive`

> Request Example
    
    
    GET /api/v5/trade/orders-history-archive?ordType=post_only,fok,ioc&instType=SPOT
    
    
    
    
    import okx.Trade as Trade
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # Production trading: 0, Demo trading: 1
    
    tradeAPI = Trade.TradeAPI(apikey, secretkey, passphrase, False, flag)
    
    # Get completed SPOT orders which are placed in the last 3 months
    result = tradeAPI.get_orders_history_archive(
        instType="SPOT",
        ordType="post_only,fok,ioc"
    )
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
instType | String | yes | Instrument type  
`SPOT`  
`MARGIN`  
`SWAP`  
`FUTURES`  
`OPTION`  
`EVENTS`  
instFamily | String | No | Instrument family  
Applicable to `FUTURES`/`SWAP`/`OPTION`  
instId | String | No | Instrument ID, e.g. `BTC-USD-200927`  
ordType | String | No | Order type   
`market`: Market order   
`limit`: Limit order   
`post_only`: Post-only order   
`fok`: Fill-or-kill order   
`ioc`: Immediate-or-cancel order   
`optimal_limit_ioc`: Market order with immediate-or-cancel order  
`mmp`: Market Maker Protection (only applicable to Option in Portfolio Margin mode)  
`mmp_and_post_only`: Market Maker Protection and Post-only order(only applicable to Option in Portfolio Margin mode)   
`op_fok`: Simple options (fok)   
`elp`: Enhanced Liquidity Program order  
state | String | No | State  
`canceled`   
`filled`  
`mmp_canceled`: Order canceled automatically due to Market Maker Protection  
category | String | No | Category   
`twap`   
`adl`  
`full_liquidation`  
`partial_liquidation`  
`delivery`   
`ddh`: Delta dynamic hedge  
after | String | No | Pagination of data to return records earlier than the requested `ordId`  
before | String | No | Pagination of data to return records newer than the requested `ordId`  
begin | String | No | Filter with a begin timestamp `cTime`. Unix timestamp format in milliseconds, e.g. 1597026383085  
end | String | No | Filter with an end timestamp `cTime`. Unix timestamp format in milliseconds, e.g. 1597026383085  
limit | String | No | Number of results per request. The maximum is `100`; The default is `100`  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "accFillSz": "0.00192834",
                "algoClOrdId": "",
                "algoId": "",
                "attachAlgoClOrdId": "",
                "attachAlgoOrds": [],
                "avgPx": "51858",
                "cTime": "1708587373361",
                "cancelSource": "",
                "cancelSourceReason": "",
                "category": "normal",
                "ccy": "",
                "clOrdId": "",
                "fee": "-0.00000192834",
                "feeCcy": "BTC",
                "fillPx": "51858",
                "fillSz": "0.00192834",
                "fillTime": "1708587373361",
                "instId": "BTC-USDT",
                "instType": "SPOT",
                "lever": "",
                "ordId": "680800019749904384",
                "ordType": "market",
                "pnl": "0",
                "posSide": "",
                "px": "",
                "pxType": "",
                "pxUsd": "",
                "pxVol": "",
                "quickMgnType": "",
                "rebate": "0",
                "rebateCcy": "USDT",
                "reduceOnly": "false",
                "side": "buy",
                "slOrdPx": "",
                "slTriggerPx": "",
                "slTriggerPxType": "",
                "source": "",
                "state": "filled",
                "stpId": "",
                "stpMode": "",
                "sz": "100",
                "tag": "",
                "tdMode": "cash",
                "tgtCcy": "quote_ccy",
                "tpOrdPx": "",
                "tpTriggerPx": "",
                "tpTriggerPxType": "",
                "tradeId": "744876980",
                "tradeQuoteCcy": "USDT",
                "uTime": "1708587373362",
                "isTpLimit": "false",
                "linkedAlgoOrd": {
                    "algoId": ""
                }
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
instType | String | Instrument type  
`SPOT`  
`MARGIN`  
`SWAP`  
`FUTURES`  
`OPTION`  
`EVENTS`  
instId | String | Instrument ID  
tgtCcy | String | Order quantity unit setting for `sz`  
`base_ccy`: Base currency ,`quote_ccy`: Quote currency   
Only applicable to `SPOT` Market Orders  
Default is `quote_ccy` for buy, `base_ccy` for sell  
ccy | String | Margin currency   
Applicable to all `isolated` `MARGIN` orders and `cross` `MARGIN` orders in `Futures mode`, `FUTURES` and `SWAP` contracts.  
ordId | String | Order ID  
clOrdId | String | Client Order ID as assigned by the client  
tag | String | Order tag  
px | String | Price   
For options, use coin as unit (e.g. BTC, ETH)  
pxUsd | String | Options price in USDOnly applicable to options; return "" for other instrument types  
pxVol | String | Implied volatility of the options orderOnly applicable to options; return "" for other instrument types  
pxType | String | Price type of options   
`px`: Place an order based on price, in the unit of coin (the unit for the request parameter px is BTC or ETH)   
`pxVol`: Place an order based on pxVol   
`pxUsd`: Place an order based on pxUsd, in the unit of USD (the unit for the request parameter px is USD)  
sz | String | Quantity to buy or sell  
ordType | String | Order type   
`market`: Market order   
`limit`: Limit order   
`post_only`: Post-only order   
`fok`: Fill-or-kill order   
`ioc`: Immediate-or-cancel order   
`optimal_limit_ioc`: Market order with immediate-or-cancel order  
`mmp`: Market Maker Protection (only applicable to Option in Portfolio Margin mode)  
`mmp_and_post_only`: Market Maker Protection and Post-only order(only applicable to Option in Portfolio Margin mode)   
`op_fok`: Simple options (fok)   
`elp`: Enhanced Liquidity Program order  
side | String | Order side  
posSide | String | Position side  
tdMode | String | Trade mode  
accFillSz | String | Accumulated fill quantity  
fillPx | String | Last filled price. If none is filled, it will return "".  
tradeId | String | Last trade ID  
fillSz | String | Last filled quantity  
fillTime | String | Last filled time  
avgPx | String | Average filled price. If none is filled, it will return "".  
state | String | State   
`canceled`   
`filled`   
`mmp_canceled`  
lever | String | Leverage, from `0.01` to `125`.   
Only applicable to `MARGIN/FUTURES/SWAP`  
attachAlgoClOrdId | String | Client-supplied Algo ID when placing order with attached TP/SL or trailing stop.  
tpTriggerPx | String | Take-profit trigger price.  
tpTriggerPxType | String | Take-profit trigger price type.   
`last`: last price  
`index`: index price  
`mark`: mark price  
tpOrdPx | String | Take-profit order price.  
slTriggerPx | String | Stop-loss trigger price.  
slTriggerPxType | String | Stop-loss trigger price type.   
`last`: last price  
`index`: index price  
`mark`: mark price  
slOrdPx | String | Stop-loss order price.  
attachAlgoOrds | Array of objects | Attached TP/SL or trailing stop order information  
> attachAlgoId | String | The order ID of the attached TP/SL or trailing stop order. It can be used to identify the attached order when amending. It will not be posted to algoId when placing the attached algo order after the general order is filled completely.  
> attachAlgoClOrdId | String | Client-supplied Algo ID when placing order with attached TP/SL or trailing stop  
A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters.  
It will be posted to `algoClOrdId` when placing the attached algo order once the general order is filled completely.  
> tpOrdKind | String | TP order kind  
`condition`  
`limit`  
> tpTriggerPx | String | Take-profit trigger price.  
> tpTriggerRatio | String | Take profit trigger ratio, 0.3 represents 30%   
Only applicable to FUTURES and SWAP.  
> tpTriggerPxType | String | Take-profit trigger price type.   
`last`: last price  
`index`: index price  
`mark`: mark price  
> tpOrdPx | String | Take-profit order price.  
> slTriggerPx | String | Stop-loss trigger price.  
> slTriggerRatio | String | Stop-loss trigger ratio, 0.3 represents 30%   
Only applicable to FUTURES and SWAP.  
> slTriggerPxType | String | Stop-loss trigger price type.   
`last`: last price  
`index`: index price  
`mark`: mark price  
> slOrdPx | String | Stop-loss order price.  
> sz | String | Size. Only applicable to TP order of split TPs  
> amendPxOnTriggerType | String | Whether to enable Cost-price SL. Only applicable to SL order of split TPs.   
`0`: disable, the default value   
`1`: Enable  
> callbackRatio | String | Callback ratio, e.g. `0.05` represents 5%  
> callbackSpread | String | Callback spread (price distance)  
> activePx | String | Activation price  
> failCode | String | The error code when failing to place TP/SL order, e.g. 51020   
The default is ""  
> failReason | String | The error reason when failing to place TP/SL order.   
The default is ""  
linkedAlgoOrd | Object | Linked SL order detail, only applicable to the order that is placed by one-cancels-the-other (OCO) order that contains the TP limit order.  
> algoId | String | Algo ID  
stpId | String | ~~Self trade prevention ID  
Return "" if self trade prevention is not applicable~~ (Deprecated)  
stpMode | String | Self trade prevention mode  
feeCcy | String | Fee currency  
For maker sell orders of Spot and Margin, this represents the quote currency. For all other cases, it represents the currency in which fees are charged.  
fee | String | Fee amount  
For Spot and Margin (excluding maker sell orders): accumulated fee charged by the platform, always negative  
For maker sell orders in Spot and Margin, Expiry Futures, Perpetual Futures and Options: accumulated fee and rebate (always in quote currency for maker sell orders in Spot and Margin)  
rebateCcy | String | Rebate currency  
For maker sell orders of Spot and Margin, this represents the base currency. For all other cases, it represents the currency in which rebates are paid.  
rebate | String | Rebate amount, only applicable to Spot and Margin  
For maker sell orders: ~~Accumulated fee and~~ rebate amount in the unit of base currency.  
For all other cases, it represents the maker rebate amount, always positive, return "" if no rebate.  
source | String | Order source  
`6`: The normal order triggered by the `trigger order`  
`7`:The normal order triggered by the `TP/SL order`   
`13`: The normal order triggered by the algo order  
`25`:The normal order triggered by the `trailing stop order`  
`34`: The normal order triggered by the `chase order`  
pnl | String | Profit and loss (excluding the fee).  
Applicable to orders which have a trade and aim to close position. It always is 0 in other conditions  
category | String | Category   
`normal`  
`twap`   
`adl`  
`full_liquidation`  
`partial_liquidation`   
`delivery`   
`ddh`: Delta dynamic hedge  
`auto_conversion`  
reduceOnly | String | Whether the order can only reduce the position size. Valid options: true or false.  
cancelSource | String | Code of the cancellation source.  
cancelSourceReason | String | Reason for the cancellation.  
algoClOrdId | String | Client-supplied Algo ID. There will be a value when algo order attaching `algoClOrdId` is triggered, or it will be "".  
algoId | String | Algo ID. There will be a value when algo order is triggered, or it will be "".  
isTpLimit | String | Whether it is TP limit order. true or false  
uTime | String | Update time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
cTime | String | Creation time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
quickMgnType | String | ~~Quick Margin type, Only applicable to Quick Margin Mode of isolated margin  
`manual`, `auto_borrow`, `auto_repay`~~ (Deprecated)  
tradeQuoteCcy | String | The quote currency used for trading.  
outcome | String | The market outcome the user traded on.  
`yes`  
`no`  
Only applicable to `EVENTS`  
This interface does not contain the order data of the `Canceled orders without any fills` type, which can be obtained through the `Get Order History (last 7 days)` interface.   
As far as OPTION orders that are complete, pxVol and pxUsd will update in time for px order, pxVol will update in time for pxUsd order, pxUsd will update in time for pxVol order.   

### GET / Transaction details (last 3 days)

Retrieve recently-filled transaction details in the last 3 day.

#### Rate Limit: 60 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/trade/fills`

> Request Example
    
    
    GET /api/v5/trade/fills
    
    
    
    
    import okx.Trade as Trade
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # Production trading: 0, Demo trading: 1
    
    tradeAPI = Trade.TradeAPI(apikey, secretkey, passphrase, False, flag)
    
    # Retrieve recently-filled transaction details
    result = tradeAPI.get_fills()
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
instType | String | No | Instrument type  
`SPOT`  
`MARGIN`  
`SWAP`  
`FUTURES`  
`OPTION`  
`EVENTS`  
instFamily | String | No | Instrument family  
Applicable to `FUTURES`/`SWAP`/`OPTION`  
instId | String | No | Instrument ID, e.g. `BTC-USDT`  
ordId | String | No | Order ID  
subType | String | No | Transaction type   
`1`: Buy  
`2`: Sell  
`3`: Open long  
`4`: Open short  
`5`: Close long  
`6`: Close short   
`100`: Partial liquidation close long  
`101`: Partial liquidation close short  
`102`: Partial liquidation buy  
`103`: Partial liquidation sell  
`104`: Liquidation long  
`105`: Liquidation short  
`106`: Liquidation buy   
`107`: Liquidation sell   
`110`: Liquidation transfer in  
`111`: Liquidation transfer out   
`118`: System token conversion transfer in  
`119`: System token conversion transfer out  
`112`: Delivery long  
`113`: Delivery short   
`125`: ADL close long  
`126`: ADL close short  
`127`: ADL buy  
`128`: ADL sell   
`212`: Auto borrow of quick margin  
`213`: Auto repay of quick margin   
`204`: block trade buy  
`205`: block trade sell  
`206`: block trade open long  
`207`: block trade open short  
`208`: block trade close long  
`209`: block trade close short  
`236`: Easy convert in  
`237`: Easy convert out  
`270`: Spread trading buy  
`271`: Spread trading sell  
`272`: Spread trading open long  
`273`: Spread trading open short  
`274`: Spread trading close long  
`275`: Spread trading close short  
`324`: Move position buy  
`325`: Move position sell  
`326`: Move position open long  
`327`: Move position open short  
`328`: Move position close long  
`329`: Move position close short   
`376`: Collateralized borrowing auto conversion buy  
`377`: Collateralized borrowing auto conversion sell  
`410`: Buy yes  
`411`: Buy no  
`412`: Sell yes  
`413`: Sell no  
`414`: Yes expiry  
`415`: No expiry  
after | String | No | Pagination of data to return records earlier than the requested `billId`  
before | String | No | Pagination of data to return records newer than the requested `billId`  
begin | String | No | Filter with a begin timestamp `ts`. Unix timestamp format in milliseconds, e.g. `1597026383085`  
end | String | No | Filter with an end timestamp `ts`. Unix timestamp format in milliseconds, e.g. `1597026383085`  
limit | String | No | Number of results per request. The maximum is `100`; The default is `100`  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "side": "buy",
                "fillSz": "0.00192834",
                "fillPx": "51858",
                "fillPxVol": "",
                "fillFwdPx": "",
                "fee": "-0.00000192834",
                "fillPnl": "0",
                "ordId": "680800019749904384",
                "feeRate": "-0.001",
                "instType": "SPOT",
                "fillPxUsd": "",
                "instId": "BTC-USDT",
                "clOrdId": "",
                "posSide": "net",
                "billId": "680800019754098688",
                "subType": "1",
                "fillMarkVol": "",
                "tag": "",
                "fillTime": "1708587373361",
                "execType": "T",
                "fillIdxPx": "",
                "tradeId": "744876980",
                "fillMarkPx": "",
                "feeCcy": "BTC",
                "ts": "1708587373362",
                "tradeQuoteCcy": "USDT"
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
instType | String | Instrument type  
instId | String | Instrument ID  
tradeId | String | Last trade ID  
ordId | String | Order ID  
clOrdId | String | Client Order ID as assigned by the client  
billId | String | Bill ID  
subType | String | Transaction type  
tag | String | Order tag  
fillPx | String | Last filled price. It is the same as the px from "Get bills details".  
fillSz | String | Last filled quantity  
fillIdxPx | String | Index price at the moment of trade execution   
For cross currency spot pairs, it returns baseCcy-USDT index price. For example, for LTC-ETH, this field returns the index price of LTC-USDT.  
fillPnl | String | Realised P&L from this fill for close-position trades, denominated in the settlement currency (see `feeCcy`). Positive = realised gain; negative = realised loss. Formula: (fillPx − avgPx) × fillSz × ctVal (linear) or (1/avgPx − 1/fillPx) × fillSz × ctVal (inverse). Returns 0 for opening trades.  
fillPxVol | String | Implied volatility when filled   
Only applicable to options; return "" for other instrument types  
fillPxUsd | String | Options price when filled, in the unit of USD   
Only applicable to options; return "" for other instrument types  
fillMarkVol | String | Mark volatility when filled   
Only applicable to options; return "" for other instrument types  
fillFwdPx | String | Forward price when filled   
Only applicable to options; return "" for other instrument types  
fillMarkPx | String | Mark price when filled   
Applicable to `FUTURES`, `SWAP`, `OPTION`  
side | String | Order side, `buy` `sell`  
posSide | String | Position side   
`long` `short`   
it returns `net` in`net` mode.  
execType | String | Liquidity taker or maker  
`T`: taker  
`M`: maker  
Not applicable to system orders such as ADL and liquidation  
feeCcy | String | Trading fee or rebate currency  
fee | String | The amount of trading fee or rebate. The trading fee deduction is negative, such as '-0.01'; the rebate is positive, such as '0.01'.  
ts | String | Timestamp when this fill record was generated by the system, in Unix milliseconds (UTC). Note: this differs from `fillTime`, which is the actual trade execution time. For chronological ordering of trades, sort by `fillTime`, not `ts`.  
fillTime | String | Trade time which is the same as `fillTime` for the order channel.  
feeRate | String | Fee rate. This field is returned for `SPOT` and `MARGIN` only  
tradeQuoteCcy | String | The quote currency for trading.  
tradeId  
For partial_liquidation, full_liquidation, or adl, when it comes to fill information, this field will be assigned a negative value to distinguish it from other matching transaction scenarios, when it comes to order information, this field will be 0.  ordId  
Order ID, always "" for block trading.  
clOrdId  
Client-supplied order ID, always "" for block trading. 

### GET / Transaction details (last 3 months)

This endpoint can retrieve data from the last 3 months.

#### Rate Limit: 10 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/trade/fills-history`

> Request Example
    
    
    GET /api/v5/trade/fills-history?instType=SPOT
    
    
    
    
    import okx.Trade as Trade
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # Production trading: 0, Demo trading: 1
    
    tradeAPI = Trade.TradeAPI(apikey, secretkey, passphrase, False, flag)
    
    # Retrieve SPOT transaction details in the last 3 months.
    result = tradeAPI.get_fills_history(
        instType="SPOT"
    )
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
instType | String | YES | Instrument type  
`SPOT`  
`MARGIN`  
`SWAP`  
`FUTURES`  
`OPTION`  
`EVENTS`  
instFamily | String | No | Instrument family  
Applicable to `FUTURES`/`SWAP`/`OPTION`  
instId | String | No | Instrument ID, e.g. `BTC-USDT`  
ordId | String | No | Order ID  
subType | String | No | Transaction type   
`1`: Buy  
`2`: Sell  
`3`: Open long  
`4`: Open short  
`5`: Close long  
`6`: Close short   
`100`: Partial liquidation close long  
`101`: Partial liquidation close short  
`102`: Partial liquidation buy  
`103`: Partial liquidation sell  
`104`: Liquidation long  
`105`: Liquidation short  
`106`: Liquidation buy   
`107`: Liquidation sell   
`110`: Liquidation transfer in  
`111`: Liquidation transfer out   
`118`: System token conversion transfer in  
`119`: System token conversion transfer out  
`112`: Delivery long  
`113`: Delivery short   
`125`: ADL close long  
`126`: ADL close short  
`127`: ADL buy  
`128`: ADL sell   
`212`: Auto borrow of quick margin  
`213`: Auto repay of quick margin   
`204`: block trade buy  
`205`: block trade sell  
`206`: block trade open long  
`207`: block trade open short  
`208`: block trade close long  
`209`: block trade close short  
`236`: Easy convert in  
`237`: Easy convert out  
`270`: Spread trading buy  
`271`: Spread trading sell  
`272`: Spread trading open long  
`273`: Spread trading open short  
`274`: Spread trading close long  
`275`: Spread trading close short  
`324`: Move position buy  
`325`: Move position sell  
`326`: Move position open long  
`327`: Move position open short  
`328`: Move position close long  
`329`: Move position close short   
`376`: Collateralized borrowing auto conversion buy  
`377`: Collateralized borrowing auto conversion sell  
`410`: Buy yes  
`411`: Buy no  
`412`: Sell yes  
`413`: Sell no  
`414`: Yes expiry  
`415`: No expiry  
after | String | No | Pagination of data to return records earlier than the requested `billId`  
before | String | No | Pagination of data to return records newer than the requested `billId`  
begin | String | No | Filter with a begin timestamp `ts`. Unix timestamp format in milliseconds, e.g. `1597026383085`  
end | String | No | Filter with an end timestamp `ts`. Unix timestamp format in milliseconds, e.g. `1597026383085`  
limit | String | No | Number of results per request. The maximum is `100`; The default is `100`  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "side": "buy",
                "fillSz": "0.00192834",
                "fillPx": "51858",
                "fillPxVol": "",
                "fillFwdPx": "",
                "fee": "-0.00000192834",
                "fillPnl": "0",
                "ordId": "680800019749904384",
                "feeRate": "-0.001",
                "instType": "SPOT",
                "fillPxUsd": "",
                "instId": "BTC-USDT",
                "clOrdId": "",
                "posSide": "net",
                "billId": "680800019754098688",
                "subType": "1",
                "fillMarkVol": "",
                "tag": "",
                "fillTime": "1708587373361",
                "execType": "T",
                "fillIdxPx": "",
                "tradeId": "744876980",
                "fillMarkPx": "",
                "feeCcy": "BTC",
                "ts": "1708587373362",
                "tradeQuoteCcy": "USDT"
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
instType | String | Instrument type  
instId | String | Instrument ID  
tradeId | String | Last trade ID  
ordId | String | Order ID  
clOrdId | String | Client Order ID as assigned by the client  
billId | String | Bill ID  
subType | String | Transaction type  
tag | String | Order tag  
fillPx | String | Last filled price  
fillSz | String | Last filled quantity  
fillIdxPx | String | Index price at the moment of trade execution   
For cross currency spot pairs, it returns baseCcy-USDT index price. For example, for LTC-ETH, this field returns the index price of LTC-USDT.  
fillPnl | String | Last filled profit and loss, applicable to orders which have a trade and aim to close position. It always is 0 in other conditions  
fillPxVol | String | Implied volatility when filled   
Only applicable to options; return "" for other instrument types  
fillPxUsd | String | Options price when filled, in the unit of USD   
Only applicable to options; return "" for other instrument types  
fillMarkVol | String | Mark volatility when filled   
Only applicable to options; return "" for other instrument types  
fillFwdPx | String | Forward price when filled   
Only applicable to options; return "" for other instrument types  
fillMarkPx | String | Mark price when filled   
Applicable to `FUTURES`, `SWAP`, `OPTION`  
side | String | Order side  
`buy`  
`sell`  
posSide | String | Position side  
`long`  
`short`  
it returns `net` in`net` mode.  
execType | String | Liquidity taker or maker  
`T`: taker  
`M`: maker  
Not applicable to system orders such as ADL and liquidation  
feeCcy | String | Trading fee or rebate currency  
fee | String | The amount of trading fee or rebate. The trading fee deduction is negative, such as '-0.01'; the rebate is positive, such as '0.01'.  
ts | String | Data generation time, Unix timestamp format in milliseconds, e.g. `1597026383085`.  
fillTime | String | Trade time which is the same as `fillTime` for the order channel.  
feeRate | String | Fee rate. This field is returned for `SPOT` and `MARGIN` only  
tradeQuoteCcy | String | The quote currency for trading.  
tradeId  
When the order category to which the transaction details belong is partial_liquidation, full_liquidation, or adl, this field will be assigned a negative value to distinguish it from other matching transaction scenarios.  
ordId  
Order ID, always "" for block trading.  
clOrdId  
Client-supplied order ID, always "" for block trading.  We advise you to use Get Transaction details (last 3 days)when you request data for recent 3 days. 

### GET / Easy convert currency list

Get list of small convertibles and mainstream currencies. Only applicable to the crypto balance less than $10.

#### Rate Limit: 1 request per 2 seconds

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/trade/easy-convert-currency-list`

> Request Example
    
    
    GET /api/v5/trade/easy-convert-currency-list
    
    
    
    import okx.Trade as Trade
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # Production trading: 0, Demo trading: 1
    
    tradeAPI = Trade.TradeAPI(apikey, secretkey, passphrase, False, flag)
    
    # Get list of small convertibles and mainstream currencies
    result = tradeAPI.get_easy_convert_currency_list()
    print(result)
    

#### Request Parameters

Parameters | Type | Required | Description  
---|---|---|---  
source | String | No | Funding source  
`1`: Trading account  
`2`: Funding account  
The default is `1`.  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "fromData": [
                    {
                        "fromAmt": "6.580712708344864",
                        "fromCcy": "ADA"
                    },
                    {
                        "fromAmt": "2.9970000013055097",
                        "fromCcy": "USDC"
                    }
                ],
                "toCcy": [
                    "USDT",
                    "BTC",
                    "ETH",
                    "OKB"
                ]
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
fromData | Array of objects | Currently owned and convertible small currency list  
> fromCcy | String | Type of small payment currency convert from, e.g. `BTC`  
> fromAmt | String | Amount of small payment currency convert from  
toCcy | Array of strings | Type of mainstream currency convert to, e.g. `USDT`  
  
### POST / Place easy convert

Convert small currencies to mainstream currencies. 

#### Rate Limit: 1 request per 2 seconds

#### Rate limit rule: User ID

#### Permission: Trade

#### HTTP Request

`POST /api/v5/trade/easy-convert`

> Request Example
    
    
    POST /api/v5/trade/easy-convert
    body
    {
        "fromCcy": ["ADA","USDC"], //Seperated by commas
        "toCcy": "OKB" 
    }
    
    
    
    import okx.Trade as Trade
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # Production trading: 0, Demo trading: 1
    
    tradeAPI = Trade.TradeAPI(apikey, secretkey, passphrase, False, flag)
    
    # Convert small currencies to mainstream currencies
    result = tradeAPI.easy_convert(
        fromCcy=["ADA", "USDC"],
        toCcy="OKB"
    )
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
fromCcy | Array of strings | Yes | Type of small payment currency convert from   
Maximum 5 currencies can be selected in one order. If there are multiple currencies, separate them with commas.  
toCcy | String | Yes | Type of mainstream currency convert to   
Only one receiving currency type can be selected in one order and cannot be the same as the small payment currencies.  
source | String | No | Funding source  
`1`: Trading account  
`2`: Funding account  
The default is `1`.  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "fillFromSz": "6.5807127",
                "fillToSz": "0.17171580105126",
                "fromCcy": "ADA",
                "status": "running",
                "toCcy": "OKB",
                "uTime": "1661419684687"
            },
            {
                "fillFromSz": "2.997",
                "fillToSz": "0.1683755161661844",
                "fromCcy": "USDC",
                "status": "running",
                "toCcy": "OKB",
                "uTime": "1661419684687"
            }
        ],
        "msg": ""
    }
    
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
status | String | Current status of easy convert   
`running`: Running   
`filled`: Filled   
`failed`: Failed  
fromCcy | String | Type of small payment currency convert from  
toCcy | String | Type of mainstream currency convert to  
fillFromSz | String | Filled amount of small payment currency convert from  
fillToSz | String | Filled amount of mainstream currency convert to  
uTime | String | Trade time, Unix timestamp format in milliseconds, e.g. 1597026383085  
  
### GET / Easy convert history

Get the history and status of easy convert trades in the past 7 days.

#### Rate Limit: 1 request per 2 seconds

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/trade/easy-convert-history`

> Request Example
    
    
    GET /api/v5/trade/easy-convert-history
    
    
    
    import okx.Trade as Trade
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # Production trading: 0, Demo trading: 1
    
    tradeAPI = Trade.TradeAPI(apikey, secretkey, passphrase, False, flag)
    
    # Get the history of easy convert trades
    result = tradeAPI.get_easy_convert_history()
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
after | String | No | Pagination of data to return records earlier than the requested time (exclude), Unix timestamp format in milliseconds, e.g. `1597026383085`  
before | String | No | Pagination of data to return records newer than the requested time (exclude), Unix timestamp format in milliseconds, e.g. `1597026383085`  
limit | String | No | Number of results per request. The maximum is 100. The default is 100.  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "fillFromSz": "0.1761712511667539",
                "fillToSz": "6.7342205900000000",
                "fromCcy": "OKB",
                "status": "filled",
                "toCcy": "ADA",
                "acct": "18",
                "uTime": "1661313307979"
            },
            {
                "fillFromSz": "0.1722106121112177",
                "fillToSz": "2.9971018300000000",
                "fromCcy": "OKB",
                "status": "filled",
                "toCcy": "USDC",
                "acct": "18",
                "uTime": "1661313307979"
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
fromCcy | String | Type of small payment currency convert from  
fillFromSz | String | Amount of small payment currency convert from  
toCcy | String | Type of mainstream currency convert to  
fillToSz | String | Amount of mainstream currency convert to  
acct | String | The account where the mainstream currency is located  
`6`: Funding account   
`18`: Trading account  
status | String | Current status of easy convert   
`running`: Running   
`filled`: Filled   
`failed`: Failed  
uTime | String | Trade time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
  
### GET / One-click repay currency list

Get list of debt currency data and repay currencies. Debt currencies include both cross and isolated debts. Only applicable to `Multi-currency margin`/`Portfolio margin`.

#### Rate Limit: 1 request per 2 seconds

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/trade/one-click-repay-currency-list`

> Request Example
    
    
    GET /api/v5/trade/one-click-repay-currency-list
    
    
    
    import okx.Trade as Trade
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # Production trading: 0, Demo trading: 1
    
    tradeAPI = Trade.TradeAPI(apikey, secretkey, passphrase, False, flag)
    
    # Get list of debt currency data and repay currencies
    result = tradeAPI.get_oneclick_repay_list()
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
debtType | String | No | Debt type   
`cross`: cross   
`isolated`: isolated  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "debtData": [
                    {
                        "debtAmt": "29.653478",
                        "debtCcy": "LTC"
                    },
                    {
                        "debtAmt": "237803.6828295906051002",
                        "debtCcy": "USDT"
                    }
                ],
                "debtType": "cross",
                "repayData": [
                    {
                        "repayAmt": "0.4978335419825104",
                        "repayCcy": "ETH"
                    }
                ]
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
debtData | Array of objects | Debt currency data list  
> debtCcy | String | Debt currency  
> debtAmt | String | Debt currency amount   
Including principal and interest  
debtType | String | Debt type   
`cross`: cross   
`isolated`: isolated  
repayData | Array of objects | Repay currency data list  
> repayCcy | String | Repay currency  
> repayAmt | String | Repay currency's available balance amount  
  
### POST / Trade one-click repay

Trade one-click repay to repay cross debts. Isolated debts are not applicable. The maximum repayment amount is based on the remaining available balance of funding and trading accounts. Only applicable to `Multi-currency margin`/`Portfolio margin`.

#### Rate Limit: 1 request per 2 seconds

#### Rate limit rule: User ID

#### Permission: Trade

#### HTTP Request

`POST /api/v5/trade/one-click-repay`

> Request Example
    
    
    POST /api/v5/trade/one-click-repay
    body
    {
        "debtCcy": ["ETH","BTC"], 
        "repayCcy": "USDT" 
    }
    
    
    
    import okx.Trade as Trade
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # Production trading: 0, Demo trading: 1
    
    tradeAPI = Trade.TradeAPI(apikey, secretkey, passphrase, False, flag)
    
    # Trade one-click repay to repay cross debts
    result = tradeAPI.oneclick_repay(
        debtCcy=["ETH", "BTC"],
        repayCcy="USDT"
    )
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
debtCcy | Array of strings | Yes | Debt currency type   
Maximum 5 currencies can be selected in one order. If there are multiple currencies, separate them with commas.  
repayCcy | String | Yes | Repay currency type   
Only one receiving currency type can be selected in one order and cannot be the same as the small payment currencies.  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "debtCcy": "ETH", 
                "fillDebtSz": "0.01023052",
                "fillRepaySz": "30", 
                "repayCcy": "USDT", 
                "status": "filled",
                "uTime": "1646188520338"
            },
            {
                "debtCcy": "BTC", 
                "fillFromSz": "3",
                "fillToSz": "60,221.15910001",
                "repayCcy": "USDT",
                "status": "filled",
                "uTime": "1646188520338"
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
status | String | Current status of one-click repay   
`running`: Running   
`filled`: Filled   
`failed`: Failed  
debtCcy | String | Debt currency type  
repayCcy | String | Repay currency type  
fillDebtSz | String | Filled amount of debt currency  
fillRepaySz | String | Filled amount of repay currency  
uTime | String | Trade time, Unix timestamp format in milliseconds, e.g. 1597026383085  
  
### GET / One-click repay history

Get the history and status of one-click repay trades in the past 7 days. Only applicable to `Multi-currency margin`/`Portfolio margin`.

#### Rate Limit: 1 request per 2 seconds

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/trade/one-click-repay-history`

> Request Example
    
    
    GET /api/v5/trade/one-click-repay-history
    
    
    
    import okx.Trade as Trade
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # Production trading: 0, Demo trading: 1
    
    tradeAPI = Trade.TradeAPI(apikey, secretkey, passphrase, False, flag)
    
    # Get the history of one-click repay trades
    result = tradeAPI.oneclick_repay_history()
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
after | String | No | Pagination of data to return records earlier than the requested time, Unix timestamp format in milliseconds, e.g. 1597026383085  
before | String | No | Pagination of data to return records newer than the requested time, Unix timestamp format in milliseconds, e.g. 1597026383085  
limit | String | No | Number of results per request. The maximum is 100. The default is 100.  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "debtCcy": "USDC",
                "fillDebtSz": "6950.4865447900000000",
                "fillRepaySz": "4.3067975995094930",
                "repayCcy": "ETH",
                "status": "filled",
                "uTime": "1661256148746"
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
debtCcy | String | Debt currency type  
fillDebtSz | String | Amount of debt currency transacted  
repayCcy | String | Repay currency type  
fillRepaySz | String | Amount of repay currency transacted  
status | String | Current status of one-click repay   
`running`: Running   
`filled`: Filled   
`failed`: Failed  
uTime | String | Trade time, Unix timestamp format in milliseconds, e.g. 1597026383085  
  
### GET / One-click repay currency list (New)

Get list of debt currency data and repay currencies. Only applicable to `SPOT mode`/`Multi-currency margin mode`/`Portfolio margin mode`.

#### Rate Limit: 1 request per 2 seconds

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/trade/one-click-repay-currency-list-v2`

> Request Example
    
    
    GET /api/v5/trade/one-click-repay-currency-list-v2
    
    
    
    import okx.Trade as Trade
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    flag = "1"  # Production trading: 0, Demo trading: 1
    
    tradeAPI = Trade.TradeAPI(apikey, secretkey, passphrase, False, flag,debug=True) 
    result = tradeAPI.get_oneclick_repay_list_v2()
    print(result)
    

> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "debtData": [
                    {
                        "debtAmt": "100",
                        "debtCcy": "USDC"
                    }
                ],
                "repayData": [
                    {
                        "repayAmt": "1.000022977",
                        "repayCcy": "BTC"
                    },
                    {
                        "repayAmt": "4998.0002397",
                        "repayCcy": "USDT"
                    },
                    {
                        "repayAmt": "100",
                        "repayCcy": "OKB"
                    },
                    {
                        "repayAmt": "1",
                        "repayCcy": "ETH"
                    },
                    {
                        "repayAmt": "100",
                        "repayCcy": "USDC"
                    }
                ]
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
debtData | Array of objects | Debt currency data list  
> debtCcy | String | Debt currency  
> debtAmt | String | Debt currency amount  
Including principal and interest  
repayData | Array of objects | Repay currency data list  
> repayCcy | String | Repay currency  
> repayAmt | String | Repay currency's available balance amount  
  
### POST / Trade one-click repay (New)

Trade one-click repay to repay debts. Only applicable to `SPOT mode`/`Multi-currency margin mode`/`Portfolio margin mode`.

#### Rate Limit: 1 request per 2 seconds

#### Rate limit rule: User ID

#### Permission: Trade

#### HTTP Request

`POST /api/v5/trade/one-click-repay-v2`

> Request Example
    
    
    POST /api/v5/trade/one-click-repay-v2
    body
    {
        "debtCcy": "USDC", 
        "repayCcyList": ["USDC","BTC"] 
    }
    
    
    
    import okx.Trade as Trade
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    flag = "1"  # Production trading: 0, Demo trading: 1
    
    tradeAPI = Trade.TradeAPI(apikey, secretkey, passphrase, False, flag,debug=True)
    result = tradeAPI.oneclick_repay_v2("USDC",["USDC","BTC"])
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
debtCcy | String | Yes | Debt currency  
repayCcyList | Array of strings | Yes | Repay currency list, e.g. ["USDC","BTC"]  
The priority of currency to repay is consistent with the order in the array. (The first item has the highest priority)  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "debtCcy": "USDC",
                "repayCcyList": [
                    "USDC",
                    "BTC"
                ],
                "ts": "1742192217514"
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
debtCcy | String | Debt currency  
repayCcyList | Array of strings | Repay currency list, e.g. ["USDC","BTC"]  
ts | String | Request time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
  
### GET / One-click repay history (New)

Get the history and status of one-click repay trades in the past 7 days. Only applicable to `SPOT mode`.

#### Rate Limit: 1 request per 2 seconds

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/trade/one-click-repay-history-v2`

> Request Example
    
    
    GET /api/v5/trade/one-click-repay-history-v2
    
    
    
    import okx.Trade as Trade
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    flag = "1"  # Production trading: 0, Demo trading: 1
    
    tradeAPI = Trade.TradeAPI(apikey, secretkey, passphrase, False, flag)
    result = tradeAPI.oneclick_repay_history_v2()
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
after | String | No | Pagination of data to return records earlier than (included) the requested time `ts` , Unix timestamp format in milliseconds, e.g. `1597026383085`  
before | String | No | Pagination of data to return records newer than (included) the requested time `ts`, Unix timestamp format in milliseconds, e.g. `1597026383085`  
limit | String | No | Number of results per request. The maximum is 100. The default is 100.  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "debtCcy": "USDC",
                "fillDebtSz": "9.079631989",
                "ordIdInfo": [
                    {
                        "cTime": "1742194485439",
                        "fillPx": "1",
                        "fillSz": "9.088651",
                        "instId": "USDC-USDT",
                        "ordId": "2338478342062235648",
                        "ordType": "ioc",
                        "px": "1.0049",
                        "side": "buy",
                        "state": "filled",
                        "sz": "9.0886514537313433"
                    },
                    {
                        "cTime": "1742194482326",
                        "fillPx": "83271.9",
                        "fillSz": "0.00010969",
                        "instId": "BTC-USDT",
                        "ordId": "2338478237607288832",
                        "ordType": "ioc",
                        "px": "82856.7",
                        "side": "sell",
                        "state": "filled",
                        "sz": "0.000109696512171"
                    }
                ],
                "repayCcyList": [
                    "USDC",
                    "BTC"
                ],
                "status": "filled",
                "ts": "1742194481852"
            },
            {
                "debtCcy": "USDC",
                "fillDebtSz": "100",
                "ordIdInfo": [],
                "repayCcyList": [
                    "USDC",
                    "BTC"
                ],
                "status": "filled",
                "ts": "1742192217511"
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
debtCcy | String | Debt currency  
repayCcyList | Array of strings | Repay currency list, e.g. ["USDC","BTC"]  
fillDebtSz | String | Amount of debt currency transacted  
status | String | Current status of one-click repay   
`running`: Running   
`filled`: Filled   
`failed`: Failed  
ordIdInfo | Array of objects | Order info  
> ordId | String | Order ID  
> instId | String | Instrument ID, e.g. `BTC-USDT`  
> ordType | String | Order type  
`ioc`: Immediate-or-cancel order  
> side | String | Side  
`buy`  
`sell`  
> px | String | Price  
> sz | String | Quantity to buy or sell  
> fillPx | String | Last filled price.  
If none is filled, it will return "".  
> fillSz | String | Last filled quantity  
> state | String | State  
`filled`  
`canceled`  
> cTime | String | Creation time for order, Unix timestamp format in milliseconds, e.g. `1597026383085`  
ts | String | Request time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
  
### POST / Mass cancel order

Cancel all the MMP pending orders of an instrument family.  

Only applicable to Option in Portfolio Margin mode, and MMP privilege is required.

#### Rate Limit: 5 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Trade

#### HTTP Request

`POST /api/v5/trade/mass-cancel`

> Request Example
    
    
    POST /api/v5/trade/mass-cancel
    body
    {
        "instType":"OPTION",
        "instFamily":"BTC-USD"
    }
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
instType | String | Yes | Instrument type  
`OPTION`  
instFamily | String | Yes | Instrument family  
lockInterval | String | No | Lock interval(ms)  
The range should be [0, 10 000]  
The default is 0. You can set it as "0" if you want to unlock it immediately.  
Error 54008 will be returned when placing order during lock interval, it is different from 51034 which is thrown when MMP is triggered  
  
> Response Example
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
            {
                "result":true
            }
        ]
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
result | Boolean | Result of the request `true`, `false`  
  
### POST / Cancel All After

Cancel all pending orders after the countdown timeout. Applicable to all trading symbols through order book (except Spread trading)  

#### Rate Limit: 1 request per second

#### Rate limit rule: User ID + tag

#### Permission: Trade

#### HTTP Request

`POST /api/v5/trade/cancel-all-after`

> Request Example
    
    
    POST /api/v5/trade/cancel-all-after
    {
       "timeOut":"60"
    }
    
    
    
    import okx.Trade as Trade
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # Production trading: 0, Demo trading: 1
    
    tradeAPI = Trade.TradeAPI(apikey, secretkey, passphrase, False, flag)
    
    # Set cancel all after
    result = tradeAPI.cancel_all_after(
        timeOut="10"
    )
    
    print(result)
    
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
timeOut | String | Yes | The countdown for order cancellation, with second as the unit.  
Range of value can be 0, [10, 120].   
Setting timeOut to 0 disables Cancel All After.  
tag | String | No | CAA order tag   
A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 16 characters.  
  
> Response Example
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
            {
                "triggerTime":"1587971460",
                "tag":"",
                "ts":"1587971400"
            }
        ]
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
triggerTime | String | The time the cancellation is triggered.  
triggerTime=0 means Cancel All After is disabled.  
tag | String | CAA order tag  
ts | String | The time the request is received.  
Users are recommended to send heartbeat to the exchange every second. When the cancel all after is triggered, the trading engine will cancel orders on behalf of the client one by one and this operation may take up to a few seconds. This feature is intended as a protection mechanism for clients only and clients should not use this feature as part of their trading strategies.    
To use tag level CAA, first, users need to set tags for their orders using the `tag` request parameter in the placing orders endpoint. When calling the CAA endpoint, if the `tag` request parameter is not provided, the default will be to set CAA at the account level. In this case, all pending orders for all order book trading symbols under that sub-account will be cancelled when CAA triggers, consistent with the existing logic. If the `tag` request parameter is provided, CAA will be set at the order tag level. When triggered, only pending orders of order book trading symbols with the specified tag will be canceled, while orders with other tags or no tags will remain unaffected.   
  
Users can run a maximum of 20 tag level CAAs simultaneously under the same sub-account. The system will only count live tag level CAAs. CAAs that have been triggered or revoked by the user will not be counted. The user will receive error code 51071 when exceeding the limit. 

### GET / Account rate limit

Get account rate limit related information.   

Only new order requests and amendment order requests will be counted towards this limit. For batch order requests consisting of multiple orders, each order will be counted individually.   

For details, please refer to [Fill ratio based sub-account rate limit](/docs-v5/en/#overview-rate-limits-fill-ratio-based-sub-account-rate-limit)

#### Rate Limit: 1 request per second

#### Rate limit rule: User ID

#### HTTP Request

`GET /api/v5/trade/account-rate-limit`

> Request Example
    
    
    # Get the account rate limit
    GET /api/v5/trade/account-rate-limit
    
    

#### Request Parameters

None

> Response Example
    
    
    {
       "code":"0",
       "data":[
          {
             "accRateLimit":"2000",
             "fillRatio":"0.1234",
             "mainFillRatio":"0.1234",
             "nextAccRateLimit":"2000",
             "ts":"123456789000"
          }
       ],
       "msg":""
    }
    
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
fillRatio | String | Sub account fill ratio during the monitoring period.   
Applicable to users with trading fee tier >= VIP 5; other users will receive `""`.  
If there has been no trading activity on the account in the past 7 days, `""` will be returned.  
If there is no executed volume during the monitoring period, `"0"` will be returned.  
If there is executed volume but no order operation count during the monitoring period, `"9999"` will be returned.  
mainFillRatio | String | Master account aggregated fill ratio during the monitoring period.   
Applicable to users with trading fee tier >= VIP 5; other users will receive `""`.  
If there has been no trading activity on the account in the past 7 days, `""` will be returned.  
If there is no executed volume during the monitoring period, `"0"` will be returned.  
accRateLimit | String | Current sub-account rate limit per 2 seconds  
nextAccRateLimit | String | Expected sub-account rate limit (per 2 seconds) in the next monitoring period.   
Applicable to users with trading fee tier >= VIP 5; other users will receive `""`.  
ts | String | Data update timestamp   
For users with trading fee tier >= VIP 5, the data will be generated daily at 08:00 am (UTC)   
For users with trading fee tier < VIP 5, the current timestamp will be returned.  
  
### POST / Order precheck

This endpoint is used to precheck the account information before and after placing the order.   
Only applicable to `Multi-currency margin mode`, and `Portfolio margin mode`.

#### Rate Limit: 5 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Trade

#### HTTP Request

`POST /api/v5/trade/order-precheck`

> Request Example
    
    
    # place order for SPOT
    POST /api/v5/trade/order-precheck
     body
     {
        "instId":"BTC-USDT",
        "tdMode":"cash",
        "clOrdId":"b15",
        "side":"buy",
        "ordType":"limit",
        "px":"2.15",
        "sz":"2"
    }
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
instId | String | Yes | Instrument ID, e.g. `BTC-USDT`  
tdMode | String | Yes | Trade mode  
Margin mode `cross` `isolated`  
Non-Margin mode `cash`  
`spot_isolated` (only applicable to SPOT lead trading, `tdMode` should be `spot_isolated` for `SPOT` lead trading.)  
side | String | Yes | Order side, `buy` `sell`  
posSide | String | Conditional | Position side   
The default is `net` in the `net` mode   
It is required in the `long/short` mode, and can only be `long` or `short`.   
Only applicable to `FUTURES`/`SWAP`.  
ordType | String | Yes | Order type   
`market`: Market order   
`limit`: Limit order   
`post_only`: Post-only order   
`fok`: Fill-or-kill order   
`ioc`: Immediate-or-cancel order   
`optimal_limit_ioc`: Market order with immediate-or-cancel order (applicable only to Expiry Futures and Perpetual Futures).   
`elp`: Enhanced Liquidity Program order  
sz | String | Yes | Quantity to buy or sell  
px | String | Conditional | Order price. Only applicable to `limit`,`post_only`,`fok`,`ioc`,`mmp`,`mmp_and_post_only` order.  
outcome | String | Conditional | The market outcome users trade on.  
`yes`  
`no`  
Only applicable and required for `EVENTS`  
reduceOnly | Boolean | No | Whether orders can only reduce in position size.   
Valid options: `true` or `false`. The default value is `false`.  
Only applicable to `MARGIN` orders, and `FUTURES`/`SWAP` orders in `net` mode   
Only applicable to `Futures mode` and `Multi-currency margin`  
tgtCcy | String | No | Whether the target currency uses the quote or base currency.  
`base_ccy`: Base currency ,`quote_ccy`: Quote currency   
Only applicable to `SPOT` Market Orders  
Default is `quote_ccy` for buy, `base_ccy` for sell  
attachAlgoOrds | Array of objects | No | Attached TP/SL or trailing stop order information  
> attachAlgoClOrdId | String | No | Client-supplied Algo ID when placing order with attached TP/SL or trailing stop  
A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters.  
It will be posted to `algoClOrdId` when placing the attached algo order once the general order is filled completely.  
> tpTriggerPx | String | Conditional | Take-profit trigger price  
For condition TP order, if you fill in this parameter, you should fill in the take-profit order price as well.  
> tpOrdPx | String | Conditional | Take-profit order price   
  
For condition TP order, if you fill in this parameter, you should fill in the take-profit trigger price as well.   
For limit TP order, you need to fill in this parameter, take-profit trigger needn‘t to be filled.   
If the price is -1, take-profit will be executed at the market price.  
> tpOrdKind | String | No | TP order kind  
`condition`  
`limit`  
The default is `condition`  
> slTriggerPx | String | Conditional | Stop-loss trigger price  
If you fill in this parameter, you should fill in the stop-loss order price.  
> slOrdPx | String | Conditional | Stop-loss order price  
If you fill in this parameter, you should fill in the stop-loss trigger price.  
If the price is -1, stop-loss will be executed at the market price.  
> tpTriggerPxType | String | No | Take-profit trigger price type  
`last`: last price   
`index`: index price   
`mark`: mark price   
The default is last  
> slTriggerPxType | String | No | Stop-loss trigger price type  
`last`: last price   
`index`: index price   
`mark`: mark price   
The default is last  
> sz | String | Conditional | Size. Only applicable to TP order of split TPs, and it is required for TP order of split TPs  
> callbackRatio | String | Conditional | Callback ratio, e.g. `0.05` represents 5%.  
Either `callbackRatio` or `callbackSpread` is required. Only one can be passed.  
Only applicable when `ordType` = `move_order_stop`  
> callbackSpread | String | Conditional | Callback spread (price distance).  
Either `callbackRatio` or `callbackSpread` is required. Only one can be passed.  
Only applicable when `ordType` = `move_order_stop`  
> activePx | String | No | Activation price.  
The trailing stop is activated when the market price reaches the activation price. After activation, the system starts calculating the actual trigger price. If not provided, the trailing stop is activated immediately upon order placement.  
Only applicable when `ordType` = `move_order_stop`  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "adjEq": "41.94347460746277",
                "adjEqChg": "-226.05616481626",
                "availBal": "0",
                "availBalChg": "0",
                "imr": "0",
                "imrChg": "57.74709688430927",
                "liab": "0",
                "liabChg": "0",
                "liabChgCcy": "",
                "liqPx": "6764.8556232031115",
                "liqPxDiff": "-57693.044376796888536773622035980224609375",
                "liqPxDiffRatio": "-0.8950500152315991",
                "mgnRatio": "0",
                "mgnRatioChg": "0",
                "mmr": "0",
                "mmrChg": "0",
                "posBal": "",
                "posBalChg": "",
                "type": ""
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
adjEq | String | Current adjusted / Effective equity in `USD`  
adjEqChg | String | After placing order, changed quantity of adjusted / Effective equity in `USD`  
imr | String | Current initial margin requirement in `USD`  
imrChg | String | After placing order, changed quantity of initial margin requirement in `USD`  
mmr | String | Current Maintenance margin requirement in `USD`  
mmrChg | String | After placing order, changed quantity of maintenance margin requirement in `USD`  
mgnRatio | String | Current Maintenance margin ratio in `USD`  
mgnRatioChg | String | After placing order, changed quantity of Maintenance margin ratio in `USD`  
availBal | String | Current available balance in margin coin currency, only applicable to turn auto borrow off  
availBalChg | String | After placing order, changed quantity of available balance after placing order, only applicable to turn auto borrow off  
liqPx | String | Current estimated liquidation price  
liqPxDiff | String | After placing order, the distance between estimated liquidation price and mark price  
liqPxDiffRatio | String | After placing order, the distance rate between estimated liquidation price and mark price  
posBal | String | Current positive asset, only applicable to margin isolated position  
posBalChg | String | After placing order, positive asset of margin isolated, only applicable to margin isolated position  
liab | String | Current liabilities of currency  
For cross, it is cross liabilities  
For isolated position, it is isolated liabilities  
liabChg | String | After placing order, changed quantity of liabilities  
For cross, it is cross liabilities  
For isolated position, it is isolated liabilities  
liabChgCcy | String | After placing order, the unit of changed liabilities quantity  
only applicable cross and in auto borrow  
type | String | Unit type of positive asset, only applicable to margin isolated position  
`1`: it is both base currency before and after placing order   
`2`: before plaing order, it is base currency. after placing order, it is quota currency.  
`3`: before plaing order, it is quota currency. after placing order, it is base currency  
`4`: it is both quota currency before and after placing order  
  
### WS / Order channel

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
`3`: New order placed by user, but the order quantity is overriden by system due to reduce-only  
`4`: Order amended by system due to other pending orders  
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

### WS / Fills channel

Retrieve transaction information. Data will not be pushed when first subscribed. Data will only be pushed when there are order book fill events, where tradeId > 0.  

The channel is exclusively available to users with trading fee tier VIP4 or above. Other users will receive error code 64003. For other users, please use [WS / Order channel](/docs-v5/en/#order-book-trading-trade-ws-order-channel). 

For `EVENTS`, only data for the YES side is returned regardless of whether the actual order was placed on YES or NO.

#### URL Path

/ws/v5/private (required login)

> Request Example: single
    
    
    {
        "id": "1512",
        "op": "subscribe",
        "args": [
            {
                "channel": "fills",
                "instId": "BTC-USDT-SWAP"
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
                "channel": "fills",
                "instId": "BTC-USDT-SWAP"
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
                "channel": "fills"
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
                "channel": "fills"
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
> channel | String | Yes | Channel name `fills`  
> instId | String | No | Instrument ID  
  
> Successful Response Example: single
    
    
    {
      "id": "1512",
      "event": "subscribe",
      "arg": {
        "channel": "fills",
        "instId": "BTC-USDT-SWAP"
      },
      "connId": "a4d3ae55"
    }
    
    

> Successful Response Example
    
    
    {
      "id": "1512",
      "event": "subscribe",
      "arg": {
        "channel": "fills"
      },
      "connId": "a4d3ae55"
    }
    
    

#### Response parameters

Parameter | Type | Required | Description  
---|---|---|---  
id | String | No | Unique identifier of the message  
event | String | Yes | Event  
`subscribe` `unsubscribe` `error`  
arg | Object | No | Subscribed channel  
> channel | String | Yes | Channel name  
> instId | String | No | Instrument ID  
code | String | No | Error code  
msg | String | No | Error message  
connId | String | Yes | WebSocket connection ID  
  
> Push Data Example: single
    
    
    {
        "arg": {
            "channel": "fills",
            "instId": "BTC-USDT-SWAP",
            "uid": "614488474791111"
        },
        "data":[
            {
                "instId": "BTC-USDT-SWAP",
                "fillSz": "100",
                "fillPx": "70000",
                "side": "buy",
                "ts": "1705449605015",
                "ordId": "680800019749904384",
                "clOrdId": "1234567890",
                "tradeId": "12345",
                "execType": "T",
                "count": "10"
            }
        ]
    }
    
    

#### Push data parameters

Parameter | Type | Description  
---|---|---  
arg | Object | Successfully subscribed channel  
> channel | String | Channel name  
> uid | String | User Identifier  
> instId | String | Instrument ID  
data | Array of objects | Subscribed data  
> instId | String | Instrument ID  
> fillSz | String | Filled quantity. If the trade is aggregated, the filled quantity will also be aggregated.  
> fillPx | String | Last filled price  
> side | String | Trade direction  
`buy` `sell`  
> ts | String | Filled time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
> ordId | String | Order ID  
> clOrdId | String | Client Order ID as assigned by the client  
> tradeId | String | The last trade ID in the trades aggregation  
> execType | String | Liquidity taker or maker, `T`: taker `M`: maker  
> count | String | The count of trades aggregated  
\- The channel is exclusively available to users with trading fee tier VIP4 or above. Others will receive error code 64003 when subscribing to it.   
\- The channel only pushes partial information of the orders channel. Fill events of block trading, nitro spread, liquidation, ADL, and some other non order book events will not be pushed through this channel. Users should also subscribe to the orders channel for order confirmation.   
\- When a fill event is received by this channel, the account balance, margin, and position information might not have changed yet.   
\- Taker orders will be aggregated based on different fill prices. When aggregation occurs, the count field indicates the number of orders matched, and the tradeId represents the tradeId of the last trade in the aggregation. Maker orders will not be aggregated.   
\- The channel returns clOrdId. The field will be returned upon trade execution. Note that the fills channel will only return this field if the user-provided clOrdId conforms to the signed int64 positive integer format (1-9223372036854775807, 2^63-1); if the user does not provide this field or if clOrdId does not meet the format requirements, the field will return "0". The order endpoints and channel will continue to return the user-provided clOrdId as usual. All request and response parameters are of string type.  
\- In the future, connection limits will be imposed on this channel. The maximum number of connections subscribing to this channel per subaccount will be 20. We recommend users always use this channel within this limit to avoid any impact on their strategies when the limit is enforced.   

### WS / Place order

You can place an order only if you have sufficient funds.  
  

#### URL Path

/ws/v5/private (required login)

#### Rate Limit: 60 requests per 2 seconds

#### Rate Limit of lead trader lead instruments for Copy Trading: 4 requests per 2 seconds

#### Rate limit rule (except Options): User ID + Instrument ID

#### Rate limit rule (Options only): User ID + Instrument Family

Rate limit of this endpoint will also be affected by the rules [Sub-account rate limit](/docs-v5/en/#overview-rate-limits-sub-account-rate-limit) and [Fill ratio based sub-account rate limit](/docs-v5/en/#overview-rate-limits-fill-ratio-based-sub-account-rate-limit).

Rate limit is shared with the `Place order` REST API endpoints 

> Request Example
    
    
    {
      "id": "1512",
      "op": "order",
      "args": [
        {
          "side": "buy",
          "instIdCode": 123456,
          "tdMode": "isolated",
          "ordType": "market",
          "sz": "100"
        }
      ]
    }
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
id | String | Yes | Unique identifier of the message   
Provided by client. It will be returned in response message for identifying the corresponding request.   
A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters.  
op | String | Yes | Operation  
`order`  
args | Array of objects | Yes | Request parameters  
> instIdCode | Integer | 是 | Instrument ID code.  
> tdMode | String | Yes | Trade mode   
Margin mode `isolated` `cross`   
Non-Margin mode `cash`  
`spot_isolated` (only applicable to SPOT lead trading, `tdMode` should be `spot_isolated` for `SPOT` lead trading.)   
  
Event contracts symbols only support `isolated`  
> ccy | String | No | Margin currency   
Applicable to all `isolated` `MARGIN` orders and `cross` `MARGIN` orders in `Futures mode`.  
> clOrdId | String | No | Client Order ID as assigned by the client   
A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters.  
> tag | String | No | Order tag   
A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 16 characters.  
> side | String | Yes | Order side, `buy` `sell`  
> posSide | String | Conditional | Position side   
The default is `net` in the `net` mode   
It is required in the `long/short` mode, and can only be `long` or `short`.   
Only applicable to `FUTURES`/`SWAP`.  
> ordType | String | Yes | Order type   
`market`: Market order, only applicable to `SPOT/MARGIN/FUTURES/SWAP`   
`limit`: limit order   
`post_only`: Post-only order   
`fok`: Fill-or-kill order   
`ioc`: Immediate-or-cancel order   
`optimal_limit_ioc`: Market order with immediate-or-cancel order  
`mmp`: Market Maker Protection (only applicable to Option in Portfolio Margin mode)  
`mmp_and_post_only`: Market Maker Protection and Post-only order(only applicable to Option in Portfolio Margin mode)  
`elp`: Enhanced Liquidity Program order  
> sz | String | Yes | Quantity to buy or sell.  
> px | String | Conditional | Order price. Only applicable to `limit`,`post_only`,`fok`,`ioc`,`mmp`,`mmp_and_post_only` order.  
When placing an option order, one of px/pxUsd/pxVol must be filled in, and only one can be filled in  
> speedBump | String | Conditional | Speed bump  
`1`: Event contract speed bumps (the delay duration will be changed subject to adjustment without prior notice). Required for non-post-only orders of `EVENTS` symbols.  
> outcome | String | Conditional | The market outcome users trade on.  
`yes`  
`no`  
Only applicable and required for `EVENTS`  
> pxUsd | String | Conditional | Place options orders in `USD`   
Only applicable to options   
When placing an option order, one of px/pxUsd/pxVol must be filled in, and only one can be filled in  
> pxVol | String | Conditional | Place options orders based on implied volatility, where 1 represents 100%   
Only applicable to options   
When placing an option order, one of px/pxUsd/pxVol must be filled in, and only one can be filled in  
> reduceOnly | Boolean | No | Whether the order can only reduce the position size.   
Valid options: `true` or `false`. The default value is `false`.  
Only applicable to `MARGIN` orders, and `FUTURES`/`SWAP` orders in `net` mode   
Only applicable to `Futures mode` and `Multi-currency margin`  
> tgtCcy | String | No | Order quantity unit setting for `sz`  
`base_ccy`: Base currency ,`quote_ccy`: Quote currency   
Only applicable to `SPOT` Market Orders  
Default is `quote_ccy` for buy, `base_ccy` for sell  
> banAmend | Boolean | No | Whether to disallow the system from amending the size of the SPOT Market Order.  
Valid options: `true` or `false`. The default value is `false`.  
If `true`, system will not amend and reject the market order if user does not have sufficient funds.   
Only applicable to SPOT Market Orders  
> pxAmendType | String | No | The price amendment type for orders  
`0`: Do not allow the system to amend to order price if `px` exceeds the price limit   
`1`: Allow the system to amend the price to the best available value within the price limit if `px` exceeds the price limit  
The default value is `0`  
> tradeQuoteCcy | String | No | The quote currency used for trading. Only applicable to `SPOT`.   
The default value is the quote currency of the `instId`, for example: for `BTC-USD`, the default is `USD`.  
> slippagePct | String | No | Maximum acceptable slippage for spot and spot margin market-side orders, where `tgtCcy` is the received currency (`base_ccy` for buy, `quote_ccy` for sell).  
Range: `0` to `0.05` (0% to 5%, inclusive). Up to 2 decimal places of the percentage, e.g., `0.01` (1%) and `0.0123` (1.23%) are accepted; `0.01234` (1.234%) is rejected.  
If not specified or empty, defaults to `0.00%`.  
Slippage cannot be modified on an existing order. Cancel and resubmit to change the slippage setting.  
Only applicable to `SPOT` and `SPOT margin` `market` orders.  
> stpMode | String | No | Self trade prevention mode.   
`cancel_maker`,`cancel_taker`, `cancel_both`.  
Cancel both does not support FOK   
  
The account-level acctStpMode will be used to place orders. The default value of this field is `cancel_maker`. Users can log in to the webpage through the master account to modify this configuration. Users can also utilize the stpMode request parameter of the placing order endpoint to determine the stpMode of a certain order.  
> isElpTakerAccess | Boolean | No | ELP taker access  
`true`: the request can trade with ELP orders but a speed bump will be applied  
`false`: the request cannot trade with ELP orders and no speed bump  
  
The default value is `false` while `true` is only applicable to ioc orders.  
expTime | String | No | Request effective deadline. Unix timestamp format in milliseconds, e.g. `1597026383085`  
  
> Successful Response Example
    
    
    {
      "id": "1512",
      "op": "order",
      "data": [
        {
          "clOrdId": "",
          "ordId": "12345689",
          "tag": "",
          "ts":"1695190491421",
          "sCode": "0",
          "sMsg": ""
        }
      ],
      "code": "0",
      "msg": "",
      "inTime": "1695190491421339",
      "outTime": "1695190491423240"
    }
    

> Failure Response Example
    
    
    {
      "id": "1512",
      "op": "order",
      "data": [
        {
          "clOrdId": "",
          "ordId": "",
          "tag": "",
          "ts":"1695190491421",
          "sCode": "5XXXX",
          "sMsg": "not exist"
        }
      ],
      "code": "1",
      "msg": "",
      "inTime": "1695190491421339",
      "outTime": "1695190491423240"
    }
    

> Response Example When Format Error
    
    
    {
      "id": "1512",
      "op": "order",
      "data": [],
      "code": "60013",
      "msg": "Invalid args",
      "inTime": "1695190491421339",
      "outTime": "1695190491423240"
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
id | String | Unique identifier of the message  
op | String | Operation  
code | String | Error Code  
msg | String | Error message  
data | Array of objects | Data  
> ordId | String | Order ID  
> clOrdId | String | Client Order ID as assigned by the client  
> tag | String | Order tag  
> ts | String | Timestamp when the order request processing is finished by our system, Unix timestamp format in milliseconds, e.g. `1597026383085`  
> sCode | String | Order status code, `0` means success  
> sMsg | String | Rejection or success message of event execution.  
> subCode | String | Sub-code of sCode.  
Returns `""` when sCode is 0 (request successful).  
When sCode is not 0 (request failed), returns the sub-code if available; otherwise returns `""`.  
inTime | String | Timestamp at Websocket gateway when the request is received, Unix timestamp format in microseconds, e.g. `1597026383085123`  
outTime | String | Timestamp at Websocket gateway when the response is sent, Unix timestamp format in microseconds, e.g. `1597026383085123`  
tdMode  
Trade Mode, when placing an order, you need to specify the trade mode.  
**Spot mode:**  
\- SPOT and OPTION buyer: cash  
**Futures mode:**  
\- Isolated MARGIN: isolated  
\- Cross MARGIN: cross  
\- SPOT: cash  
\- Cross FUTURES/SWAP/OPTION: cross  
\- Isolated FUTURES/SWAP/OPTION: isolated  
**Multi-currency margin:**  
\- Isolated MARGIN: isolated  
\- Cross SPOT: cross  
\- Cross FUTURES/SWAP/OPTION: cross  
\- Isolated FUTURES/SWAP/OPTION: isolated  
**Portfolio margin:**  
\- Isolated MARGIN: isolated  
\- Cross SPOT: cross  
\- Cross FUTURES/SWAP/OPTION: cross  
\- Isolated FUTURES/SWAP/OPTION: isolated  clOrdId  
clOrdId is a user-defined unique order identifier at the User ID level. If provided in the request parameters, it will be included in the response and can be used as a request parameter to query, cancel, and amend orders.   
clOrdId cannot duplicate any existing clOrdId of all current pending orders.  posSide  
Position side, this parameter is not mandatory in **net** mode. If you pass it through, the only valid value is **net**.  
In **long/short** mode, it is mandatory. Valid values are **long** or **short**.  
In **long/short** mode, **side** and **posSide** need to be specified in the combinations below:  
Open long: buy and open long (side: fill in buy; posSide: fill in long)  
Open short: sell and open short (side: fill in sell; posSide: fill in short)  
Close long: sell and close long (side: fill in sell; posSide: fill in long)  
Close short: buy and close short (side: fill in buy; posSide: fill in short)  
Portfolio margin mode: Expiry Futures and Perpetual Futures only support net mode  ordType   
Order type. When creating a new order, you must specify the order type. The order type you specify will affect: 1) what order parameters are required, and 2) how the matching system executes your order. The following are valid order types:   
limit: Limit order, which requires specified sz and px.   
market: Market order. For SPOT and MARGIN, market order will be filled with market price (by swiping opposite order book). For Expiry Futures and Perpetual Futures, market order will be placed to order book with most aggressive price allowed by Price Limit Mechanism. For OPTION, market order is not supported yet. As the filled price for market orders cannot be determined in advance, OKX reserves/freezes your quote currency by an additional 5% for risk check.   
post_only: Post-only order, which the order can only provide liquidity to the market and be a maker. If the order would have executed on placement, it will be canceled instead.   
fok: Fill or kill order. If the order cannot be fully filled, the order will be canceled. The order would not be partially filled.   
ioc: Immediate or cancel order. Immediately execute the transaction at the order price, cancel the remaining unfilled quantity of the order, and the order quantity will not be displayed in the order book.   
optimal_limit_ioc: Market order with ioc (immediate or cancel). Immediately execute the transaction of this market order, cancel the remaining unfilled quantity of the order, and the order quantity will not be displayed in the order book. Only applicable to Expiry Futures and Perpetual Futures.  sz  
Quantity to buy or sell.   
For SPOT/MARGIN Buy and Sell Limit Orders, it refers to the quantity in base currency.   
For MARGIN Buy Market Orders, it refers to the quantity in quote currency.   
For MARGIN Sell Market Orders, it refers to the quantity in base currency.   
For SPOT Market Orders, it is set by tgtCcy.   
For FUTURES/SWAP/OPTION orders, it refers to the number of contracts.  reduceOnly  
When placing an order with this parameter set to true, it means that the order will reduce the size of the position only  
For the same MARGIN instrument, the coin quantity of all reverse direction pending orders adds `sz` of new `reduceOnly` order cannot exceed the position assets. After the debt is paid off, if there is a remaining size of orders, the position will not be opened in reverse, but will be traded in SPOT.  
For the same FUTURES/SWAP instrument, the sum of the current order size and all reverse direction reduce-only pending orders which's price-time priority is higher than the current order, cannot exceed the contract quantity of position.  
Only applicable to `Futures mode` and `Multi-currency margin`  
Only applicable to `MARGIN` orders, and `FUTURES`/`SWAP` orders in `net` mode  
Notice: Under long/short mode of Expiry Futures and Perpetual Futures, all closing orders apply the reduce-only feature which is not affected by this parameter.  tgtCcy  
This parameter is used to specify the order quantity in the order request is denominated in the quantity of base or quote currency. This is applicable to SPOT Market Orders only.  
Base currency: base_ccy  
Quote currency: quote_ccy   
If you use the Base Currency quantity for buy market orders or the Quote Currency for sell market orders, please note:   
1\. If the quantity you enter is greater than what you can buy or sell, the system will execute the order according to your maximum buyable or sellable quantity. If you want to trade according to the specified quantity, you should use Limit orders.   
2\. When the market price is too volatile, the locked balance may not be sufficient to buy the Base Currency quantity or sell to receive the Quote Currency that you specified. We will change the quantity of the order to execute the order based on best effort principle based on your account balance. In addition, we will try to over lock a fraction of your balance to avoid changing the order quantity.   
2.1 Example of base currency buy market order:   
Taking the market order to buy 10 LTCs as an example, and the user can buy 11 LTC. At this time, if 10 < 11, the order is accepted. When the LTC-USDT market price is 200, and the locked balance of the user is 3,000 USDT, as 200*10 < 3,000, the market order of 10 LTC is fully executed; If the market is too volatile and the LTC-USDT market price becomes 400, 400*10 > 3,000, the user's locked balance is not sufficient to buy using the specified amount of base currency, the user's maximum locked balance of 3,000 USDT will be used to settle the trade. Final transaction quantity becomes 3,000/400 = 7.5 LTC.   
2.2 Example of quote currency sell market order:   
Taking the market order to sell 1,000 USDT as an example, and the user can sell 1,200 USDT, 1,000 < 1,200, the order is accepted. When the LTC-USDT market price is 200, and the locked balance of the user is 6 LTC, as 1,000/200 < 6, the market order of 1,000 USDT is fully executed; If the market is too volatile and the LTC-USDT market price becomes 100, 100*6 < 1,000, the user's locked balance is not sufficient to sell using the specified amount of quote currency, the user's maximum locked balance of 6 LTC will be used to settle the trade. Final transaction quantity becomes 6 * 100 = 600 USDT.  px  
The value for px must be a multiple of tickSz for OPTION orders.  
If not, the system will apply the rounding rules below. Using tickSz 0.0005 as an example:  
The px will be rounded up to the nearest 0.0005 when the remainder of px to 0.0005 is more than 0.00025 or `px` is less than 0.0005.  
The px will be rounded down to the nearest 0.0005 when the remainder of px to 0.0005 is less than 0.00025 and `px` is more than 0.0005.  Mandatory self trade prevention (STP)  
The trading platform imposes mandatory self trade prevention at master account level, which means the accounts under the same master account, including master account itself and all its affiliated sub-accounts, will be prevented from self trade. The account-level acctStpMode will be used to place orders by default. The default value of this field is `cancel_maker`. Users can log in to the webpage through the master account to modify this configuration. Users can also utilize the stpMode request parameter of the placing order endpoint to determine the stpMode of a certain order.  
Mandatory self trade prevention will not lead to latency.   
There are three STP modes. The STP mode is always taken based on the configuration in the taker order.  
1\. Cancel Maker: This is the default STP mode, which cancels the maker order to prevent self-trading. Then, the taker order continues to match with the next order based on the order book priority.  
2\. Cancel Taker: The taker order is canceled to prevent self-trading. If the user's own maker order is lower in the order book priority, the taker order is partially filled and then canceled. FOK orders are always honored and canceled if they would result in self-trading.  
3\. Cancel Both: Both taker and maker orders are canceled to prevent self-trading. If the user's own maker order is lower in the order book priority, the taker order is partially filled. Then, the remaining quantity of the taker order and the first maker order are canceled. FOK orders are not supported in this mode.  Rate limit of orders tagged as isElpTakerAccess:true  
\- 50 orders per 2 seconds per User ID per instrument ID.  
\- This rate limit is shared in Place order/Place multiple orders endpoints in REST/WebSocket  

### WS / Place multiple orders

Place orders in a batch. Maximum 20 orders can be placed per request  
  

#### URL Path

/ws/v5/private (required login)

#### Rate Limit: 300 orders per 2 seconds

#### Rate Limit of lead trader lead instruments for Copy Trading: 4 orders per 2 seconds

#### Rate limit rule (except Options): User ID + Instrument ID

#### Rate limit rule (Options only): User ID + Instrument Family

Rate limit of this endpoint will also be affected by the rules [Sub-account rate limit](/docs-v5/en/#overview-rate-limits-sub-account-rate-limit) and [Fill ratio based sub-account rate limit](/docs-v5/en/#overview-rate-limits-fill-ratio-based-sub-account-rate-limit).

Unlike other endpoints, the rate limit of this endpoint is determined by the number of orders. If there is only one order in the request, it will consume the rate limit of `Place order`.  Rate limit is shared with the `Place multiple orders` REST API endpoints 

> Request Example
    
    
    {
      "id": "1513",
      "op": "batch-orders",
      "args": [
        {
          "side": "buy",
          "instIdCode": 123456,
          "tdMode": "cash",
          "ordType": "market",
          "sz": "100"
        },
        {
          "side": "buy",
          "instIdCode": 654321,
          "tdMode": "cash",
          "ordType": "market",
          "sz": "1"
        }
      ]
    }
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
id | String | Yes | Unique identifier of the message   
Provided by client. It will be returned in response message for identifying the corresponding request.   
A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters.  
op | String | Yes | Operation  
`batch-orders`  
args | Array of objects | Yes | Request Parameters  
> instIdCode | Integer | Yes | Instrument ID code.  
> tdMode | String | Yes | Trade mode   
Margin mode `isolated` `cross`   
Non-Margin mode `cash`  
`spot_isolated` (only applicable to SPOT lead trading, `tdMode` should be `spot_isolated` for `SPOT` lead trading.)  
Note: `isolated` is not available in multi-currency margin mode and portfolio margin mode.   
  
Event contracts symbols only support `isolated`  
> ccy | String | No | Margin currency   
Applicable to all `isolated` `MARGIN` orders and `cross` `MARGIN` orders in `Futures mode`.  
> clOrdId | String | No | Client Order ID as assigned by the client   
A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters.  
> tag | String | No | Order tag   
A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 16 characters.  
> side | String | Yes | Order side, `buy` `sell`  
> posSide | String | Conditional | Position side   
The default `net` in the `net` mode   
It is required in the `long/short` mode, and only be `long` or `short`.   
Only applicable to `FUTURES`/`SWAP`.  
> ordType | String | Yes | Order type   
`market`: Market order, only applicable to `SPOT/MARGIN/FUTURES/SWAP`   
`limit`: limit order   
`post_only`: Post-only order   
`fok`: Fill-or-kill order   
`ioc`: Immediate-or-cancel order   
`optimal_limit_ioc`: Market order with immediate-or-cancel order (applicable only to Expiry Futures and Perpetual Futures)  
`mmp`: Market Maker Protection (only applicable to Option in Portfolio Margin mode)  
`mmp_and_post_only`: Market Maker Protection and Post-only order(only applicable to Option in Portfolio Margin mode).   
`elp`: Enhanced Liquidity Program order  
> sz | String | Yes | Quantity to buy or sell.  
> px | String | Conditional | Order price. Only applicable to `limit`,`post_only`,`fok`,`ioc`,`mmp`,`mmp_and_post_only` order.  
When placing an option order, one of px/pxUsd/pxVol must be filled in, and only one can be filled in  
> speedBump | String | Conditional | Speed bump  
`1`: Event contract speed bumps (the delay duration will be changed subject to adjustment without prior notice). Required for non-post-only orders of `EVENTS` symbols.  
> outcome | String | Conditional | The market outcome users trade on.  
`yes`  
`no`  
Only applicable and required for `EVENTS`  
> pxUsd | String | Conditional | Place options orders in `USD`   
Only applicable to options   
When placing an option order, one of px/pxUsd/pxVol must be filled in, and only one can be filled in  
> pxVol | String | Conditional | Place options orders based on implied volatility, where 1 represents 100%   
Only applicable to options   
When placing an option order, one of px/pxUsd/pxVol must be filled in, and only one can be filled in  
> reduceOnly | Boolean | No | Whether the order can only reduce the position size.   
Valid options: `true` or `false`. The default value is `false`.  
Only applicable to `MARGIN` orders, and `FUTURES`/`SWAP` orders in `net` mode   
Only applicable to `Futures mode` and `Multi-currency margin`  
> tgtCcy | String | No | Order quantity unit setting for `sz`  
`base_ccy`: Base currency ,`quote_ccy`: Quote currency   
Only applicable to `SPOT` Market Orders  
Default is `quote_ccy` for buy, `base_ccy` for sell  
> banAmend | Boolean | No | Whether to disallow the system from amending the size of the SPOT Market Order.  
Valid options: `true` or `false`. The default value is `false`.  
If `true`, system will not amend and reject the market order if user does not have sufficient funds.   
Only applicable to SPOT Market Orders  
> pxAmendType | String | No | The price amendment type for orders  
`0`: Do not allow the system to amend to order price if `px` exceeds the price limit   
`1`: Allow the system to amend the price to the best available value within the price limit if `px` exceeds the price limit  
The default value is `0`  
> tradeQuoteCcy | String | No | The quote currency used for trading. Only applicable to `SPOT`.   
The default value is the quote currency of the `instId`, for example: for `BTC-USD`, the default is `USD`.  
> slippagePct | String | No | Maximum acceptable slippage for spot and spot margin market-side orders, where `tgtCcy` is the received currency (`base_ccy` for buy, `quote_ccy` for sell).  
Range: `0` to `0.05` (0% to 5%, inclusive). Up to 2 decimal places of the percentage, e.g., `0.01` (1%) and `0.0123` (1.23%) are accepted; `0.01234` (1.234%) is rejected.  
If not specified or empty, defaults to `0.00%`.  
Slippage cannot be modified on an existing order. Cancel and resubmit to change the slippage setting.  
Only applicable to `SPOT` and `SPOT margin` `market` orders.  
> isElpTakerAccess | Boolean | No | ELP taker access  
`true`: the request can trade with ELP orders but a speed bump will be applied  
`false`: the request cannot trade with ELP orders and no speed bump  
  
The default value is `false` while `true` is only applicable to ioc orders.  
> stpMode | String | No | Self trade prevention mode.   
`cancel_maker`,`cancel_taker`, `cancel_both`  
Cancel both does not support FOK.   
  
The account-level acctStpMode will be used to place orders by default. The default value of this field is `cancel_maker`. Users can log in to the webpage through the master account to modify this configuration. Users can also utilize the stpMode request parameter of the placing order endpoint to determine the stpMode of a certain order.  
expTime | String | No | Request effective deadline. Unix timestamp format in milliseconds, e.g. `1597026383085`  
  
> Response Example When All Succeed
    
    
    {
      "id": "1513",
      "op": "batch-orders",
      "data": [
        {
          "clOrdId": "",
          "ordId": "12345689",
          "tag": "",
          "ts": "1695190491421",
          "sCode": "0",
          "sMsg": "",
          "subCode": ""
        },
        {
          "clOrdId": "",
          "ordId": "12344",
          "tag": "",
          "ts": "1695190491421",
          "sCode": "0",
          "sMsg": "",
          "subCode": ""
        }
      ],
      "code": "0",
      "msg": "",
      "inTime": "1695190491421339",
      "outTime": "1695190491423240"
    }
    

> Response Example When Partially Successful
    
    
    {
      "id": "1513",
      "op": "batch-orders",
      "data": [
        {
          "clOrdId": "",
          "ordId": "12345689",
          "tag": "",
          "ts": "1695190491421",
          "sCode": "0",
          "sMsg": "",
          "subCode": ""
        },
        {
          "clOrdId": "",
          "ordId": "",
          "tag": "",
          "ts": "1695190491421",
          "sCode": "51008",
          "sMsg": "Order failed. Insufficient USDT balance in account",
          "subCode": "1000"
        }
      ],
      "code": "2",
      "msg": "",
      "inTime": "1695190491421339",
      "outTime": "1695190491423240"
    }
    

> Response Example When All Failed
    
    
    {
      "id": "1513",
      "op": "batch-orders",
      "data": [
        {
          "clOrdId": "oktswap6",
          "ordId": "",
          "tag": "",
          "ts": "1695190491421",
          "sCode": "51008",
          "sMsg": "Order failed. Insufficient USDT balance in account",
          "subCode": "1000"
        },
        {
          "clOrdId": "oktswap7",
          "ordId": "",
          "tag": "",
          "ts": "1695190491421",
          "sCode": "51008",
          "sMsg": "Order failed. Insufficient USDT balance in account",
          "subCode": "1000"
        }
      ],
      "code": "1",
      "msg": "",
      "subCode": "",
      "inTime": "1695190491421339",
      "outTime": "1695190491423240"
    }
    

> Response Example When Format Error
    
    
    {
      "id": "1513",
      "op": "batch-orders",
      "data": [],
      "code": "60013",
      "msg": "Invalid args",
      "inTime": "1695190491421339",
      "outTime": "1695190491423240"
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
id | String | Unique identifier of the message  
op | String | Operation  
code | String | Error Code  
msg | String | Error message  
data | Array of objects | Data  
> ordId | String | Order ID  
> clOrdId | String | Client Order ID as assigned by the client  
> tag | String | Order tag  
> ts | String | Timestamp when the order request processing is finished by our system, Unix timestamp format in milliseconds, e.g. `1597026383085`  
> sCode | String | Order status code, `0` means success  
> sMsg | String | Rejection or success message of event execution.  
> subCode | String | Sub-code of sCode.  
Returns `""` when sCode is 0 (request successful).  
When sCode is not 0 (request failed), returns the sub-code if available; otherwise returns `""`.  
inTime | String | Timestamp at Websocket gateway when the request is received, Unix timestamp format in microseconds, e.g. `1597026383085123`  
outTime | String | Timestamp at Websocket gateway when the response is sent, Unix timestamp format in microseconds, e.g. `1597026383085123`  
In the `Portfolio Margin` account mode, either all orders are accepted by the system successfully, or all orders are rejected by the system.  clOrdId  
clOrdId is a user-defined unique ID used to identify the order. It will be included in the response parameters if you have specified during order submission, and can be used as a request parameter to the endpoints to query, cancel and amend orders.   
clOrdId must be unique among all pending orders and the current request.  Rate limit of orders tagged as isElpTakerAccess:true  
\- 50 orders per 2 seconds per User ID per instrument ID.  
\- This rate limit is shared in Place order/Place multiple orders endpoints in REST/WebSocket  

### WS / Cancel order

Cancel an incomplete order

#### URL Path

/ws/v5/private (required login)

#### Rate Limit: 60 requests per 2 seconds

#### Rate limit rule (except Options): User ID + Instrument ID

#### Rate limit rule (Options only): User ID + Instrument Family

Rate limit is shared with the `Cancel order` REST API endpoints 

> Request Example
    
    
    {
      "id": "1514",
      "op": "cancel-order",
      "args": [
        {
          "instIdCode": 123456,
          "ordId": "2510789768709120"
        }
      ]
    }
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
id | String | Yes | Unique identifier of the message   
Provided by client. It will be returned in response message for identifying the corresponding request.   
A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters.  
op | String | Yes | Operation  
`cancel-order`  
args | Array of objects | Yes | Request Parameters  
> instIdCode | Integer | Yes | Instrument ID code  
> ordId | String | Conditional | Order ID   
Either `ordId` or `clOrdId` is required, if both are passed, ordId will be used  
> clOrdId | String | Conditional | Client Order ID as assigned by the client   
A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters.  
  
> Successful Response Example
    
    
    {
      "id": "1514",
      "op": "cancel-order",
      "data": [
        {
          "clOrdId": "",
          "ordId": "2510789768709120",
          "ts": "1695190491421",
          "sCode": "0",
          "sMsg": ""
        }
      ],
      "code": "0",
      "msg": "",
      "inTime": "1695190491421339",
      "outTime": "1695190491423240"
    }
    

> Failure Response Example
    
    
    {
      "id": "1514",
      "op": "cancel-order",
      "data": [
        {
          "clOrdId": "",
          "ordId": "2510789768709120",
          "ts": "1695190491421",
          "sCode": "5XXXX",
          "sMsg": "Order not exist"
        }
      ],
      "code": "1",
      "msg": "",
      "inTime": "1695190491421339",
      "outTime": "1695190491423240"
    }
    

> Response Example When Format Error
    
    
    {
      "id": "1514",
      "op": "cancel-order",
      "data": [],
      "code": "60013",
      "msg": "Invalid args",
      "inTime": "1695190491421339",
      "outTime": "1695190491423240"
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
id | String | Unique identifier of the message  
op | String | Operation  
code | String | Error Code  
msg | String | Error message  
data | Array of objects | Data  
> ordId | String | Order ID  
> clOrdId | String | Client Order ID as assigned by the client  
> ts | String | Timestamp when the order request processing is finished by our system, Unix timestamp format in milliseconds, e.g. `1597026383085`  
> sCode | String | Order status code, `0` means success  
> sMsg | String | Order status message  
inTime | String | Timestamp at Websocket gateway when the request is received, Unix timestamp format in microseconds, e.g. `1597026383085123`  
outTime | String | Timestamp at Websocket gateway when the response is sent, Unix timestamp format in microseconds, e.g. `1597026383085123`  
Cancel order returns with sCode equal to 0. It is not strictly considered that the order has been canceled. It only means that your cancellation request has been accepted by the system server. The result of the cancellation is subject to the state pushed by the order channel or the get order state.  

### WS / Cancel multiple orders

Cancel incomplete orders in batches. Maximum 20 orders can be canceled per request.

#### URL Path

/ws/v5/private (required login)

#### Rate Limit: 300 orders per 2 seconds

#### Rate limit rule (except Options): User ID + Instrument ID

#### Rate limit rule (Options only): User ID + Instrument Family

Unlike other endpoints, the rate limit of this endpoint is determined by the number of orders. If there is only one order in the request, it will consume the rate limit of `Cancel order`.  Rate limit is shared with the `Cancel multiple orders` REST API endpoints 

> Request Example
    
    
    {
      "id": "1515",
      "op": "batch-cancel-orders",
      "args": [
        {
          "instIdCode": 123456,
          "ordId": "2517748157541376"
        },
        {
          "instIdCode": 654321,
          "ordId": "2517748155771904"
        }
      ]
    }
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
id | String | Yes | Unique identifier of the message   
Provided by client. It will be returned in response message for identifying the corresponding request.   
A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters.  
op | String | Yes | Operation  
`batch-cancel-orders`  
args | Array of objects | Yes | Request Parameters  
> instIdCode | Integer | Yes | Instrument ID code  
> ordId | String | Conditional | Order ID   
Either `ordId` or `clOrdId` is required, if both are passed, ordId will be used  
> clOrdId | String | Conditional | Client Order ID as assigned by the client   
A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters.  
  
> Response Example When All Succeed
    
    
    {
      "id": "1515",
      "op": "batch-cancel-orders",
      "data": [
        {
          "clOrdId": "oktswap6",
          "ordId": "2517748157541376",
          "ts": "1695190491421",
          "sCode": "0",
          "sMsg": ""
        },
        {
          "clOrdId": "oktswap7",
          "ordId": "2517748155771904",
          "ts": "1695190491421",
          "sCode": "0",
          "sMsg": ""
        }
      ],
      "code": "0",
      "msg": "",
      "inTime": "1695190491421339",
      "outTime": "1695190491423240"
    }
    

> Response Example When partially successfully
    
    
    {
      "id": "1515",
      "op": "batch-cancel-orders",
      "data": [
        {
          "clOrdId": "oktswap6",
          "ordId": "2517748157541376",
          "ts": "1695190491421",
          "sCode": "0",
          "sMsg": ""
        },
        {
          "clOrdId": "oktswap7",
          "ordId": "2517748155771904",
          "ts": "1695190491421",
          "sCode": "5XXXX",
          "sMsg": "order not exist"
        }
      ],
      "code": "2",
      "msg": "",
      "inTime": "1695190491421339",
      "outTime": "1695190491423240"
    }
    

> Response Example When All Failed
    
    
    {
      "id": "1515",
      "op": "batch-cancel-orders",
      "data": [
        {
          "clOrdId": "oktswap6",
          "ordId": "2517748157541376",
          "ts": "1695190491421",
          "sCode": "5XXXX",
          "sMsg": "order not exist"
        },
        {
          "clOrdId": "oktswap7",
          "ordId": "2517748155771904",
          "ts": "1695190491421",
          "sCode": "5XXXX",
          "sMsg": "order not exist"
        }
      ],
      "code": "1",
      "msg": "",
      "inTime": "1695190491421339",
      "outTime": "1695190491423240"
    }
    

> Response Example When Format Error
    
    
    {
      "id": "1515",
      "op": "batch-cancel-orders",
      "data": [],
      "code": "60013",
      "msg": "Invalid args",
      "inTime": "1695190491421339",
      "outTime": "1695190491423240"
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
id | String | Unique identifier of the message  
op | String | Operation  
code | String | Error Code  
msg | String | Error message  
data | Array of objects | Data  
> ordId | String | Order ID  
> clOrdId | String | Client Order ID as assigned by the client  
> ts | String | Timestamp when the order request processing is finished by our system, Unix timestamp format in milliseconds, e.g. `1597026383085`  
> sCode | String | Order status code, `0` means success  
> sMsg | String | Order status message  
inTime | String | Timestamp at Websocket gateway when the request is received, Unix timestamp format in microseconds, e.g. `1597026383085123`  
outTime | String | Timestamp at Websocket gateway when the response is sent, Unix timestamp format in microseconds, e.g. `1597026383085123`  
  
### WS / Amend order

Amend an incomplete order.

#### URL Path

/ws/v5/private (required login)

#### Rate Limit: 60 requests per 2 seconds

#### Rate Limit of lead trader lead instruments for Copy Trading: 4 requests per 2 seconds

#### Rate limit rule (except Options): User ID + Instrument ID

#### Rate limit rule (Options only): User ID + Instrument Family

Rate limit of this endpoint will also be affected by the rules [Sub-account rate limit](/docs-v5/en/#overview-rate-limits-sub-account-rate-limit) and [Fill ratio based sub-account rate limit](/docs-v5/en/#overview-rate-limits-fill-ratio-based-sub-account-rate-limit).

Rate limit is shared with the `Amend order` REST API endpoints 

> Request Example
    
    
    {
      "id": "1512",
      "op": "amend-order",
      "args": [
        {
          "instIdCode": 123456,
          "ordId": "2510789768709120",
          "newSz": "2"
        }
      ]
    }
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
id | String | Yes | Unique identifier of the message   
Provided by client. It will be returned in response message for identifying the corresponding request.   
A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters.  
op | String | Yes | Operation  
`amend-order`  
args | Array of objects | Yes | Request Parameters  
> instIdCode | Integer | Yes | Instrument ID code  
> cxlOnFail | Boolean | No | Whether the order needs to be automatically canceled when the order amendment fails   
Valid options: `false` or `true`, the default is `false`.  
> ordId | String | Conditional | Order ID   
Either `ordId` or `clOrdId` is required, if both are passed, `ordId` will be used.  
> clOrdId | String | Conditional | Client Order ID as assigned by the client  
> reqId | String | No | Client Request ID as assigned by the client for order amendment   
A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters.  
> newSz | String | Conditional | New quantity after amendment and it has to be larger than 0. Either `newSz` or `newPx` is required. When amending a partially-filled order, the `newSz` should include the amount that has been filled.  
> newPx | String | Conditional | New price after amendment.   
When modifying options orders, users can only fill in one of the following: newPx, newPxUsd, or newPxVol. It must be consistent with parameters when placing orders. For example, if users placed the order using px, they should use newPx when modifying the order.  
> speedBump | String | Conditional | Speed bump  
`1`: Event contract speed bumps (the delay duration will be changed subject to adjustment without prior notice). Required for non-post-only orders of `EVENTS` symbols.  
> newPxUsd | String | Conditional | Modify options orders using USD prices   
Only applicable to options.   
When modifying options orders, users can only fill in one of the following: newPx, newPxUsd, or newPxVol.  
> newPxVol | String | Conditional | Modify options orders based on implied volatility, where 1 represents 100%   
Only applicable to options.   
When modifying options orders, users can only fill in one of the following: newPx, newPxUsd, or newPxVol.  
> pxAmendType | String | No | The price amendment type for orders  
`0`: Do not allow the system to amend to order price if `newPx` exceeds the price limit   
`1`: Allow the system to amend the price to the best available value within the price limit if `newPx` exceeds the price limit  
The default value is `0`  
expTime | String | No | Request effective deadline. Unix timestamp format in milliseconds, e.g. `1597026383085`  
  
> Successful Response Example
    
    
    {
      "id": "1512",
      "op": "amend-order",
      "data": [
        {
          "clOrdId": "",
          "ordId": "2510789768709120",
          "ts": "1695190491421",
          "reqId": "b12344",
          "sCode": "0",
          "sMsg": "",
          "subCode": ""
        }
      ],
      "code": "0",
      "msg": "",
      "inTime": "1695190491421339",
      "outTime": "1695190491423240"
    }
    

> Failure Response Example
    
    
    {
      "id": "1512",
      "op": "amend-order",
      "data": [
        {
          "clOrdId": "",
          "ordId": "2510789768709120",
          "ts": "1695190491421",
          "reqId": "b12344",
          "sCode": "51008",
          "sMsg": "Order failed. Insufficient USDT balance in account",
          "subCode": "10000"
        }
      ],
      "code": "1",
      "msg": "",
      "inTime": "1695190491421339",
      "outTime": "1695190491423240"
    }
    

> Response Example When Format Error
    
    
    {
      "id": "1512",
      "op": "amend-order",
      "data": [],
      "code": "60013",
      "msg": "Invalid args",
      "inTime": "1695190491421339",
      "outTime": "1695190491423240"
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
id | String | Unique identifier of the message  
op | String | Operation  
code | String | Error Code  
msg | String | Error message  
data | Array of objects | Data  
> ordId | String | Order ID  
> clOrdId | String | Client Order ID as assigned by the client  
> ts | String | Timestamp when the order request processing is finished by our system, Unix timestamp format in milliseconds, e.g. `1597026383085`  
> reqId | String | Client Request ID as assigned by the client for order amendment  
> sCode | String | Order status code, `0` means success  
> sMsg | String | Order status message  
> subCode | String | Sub-code of sCode.  
Returns `""` when sCode is 0 (request successful).  
When sCode is not 0 (request failed), returns the sub-code if available; otherwise returns `""`.  
inTime | String | Timestamp at Websocket gateway when the request is received, Unix timestamp format in microseconds, e.g. `1597026383085123`  
outTime | String | Timestamp at Websocket gateway when the response is sent, Unix timestamp format in microseconds, e.g. `1597026383085123`  
newSz   
If the new quantity of the order is less than or equal to the filled quantity when you are amending a partially-filled order, the order status will be changed to filled.  The amend order returns sCode equal to 0. It is not strictly considered that the order has been amended. It only means that your amend order request has been accepted by the system server. The result of the amend is subject to the status pushed by the order channel or the order status query 

### WS / Amend multiple orders

Amend incomplete orders in batches. Maximum 20 orders can be amended per request.

#### URL Path

/ws/v5/private (required login)

#### Rate Limit: 300 orders per 2 seconds

#### Rate Limit of lead trader lead instruments for Copy Trading: 4 orders per 2 seconds

#### Rate limit rule (except Options): User ID + Instrument ID

#### Rate limit rule (Options only): User ID + Instrument Family

Rate limit of this endpoint will also be affected by the rules [Sub-account rate limit](/docs-v5/en/#overview-rate-limits-sub-account-rate-limit) and [Fill ratio based sub-account rate limit](/docs-v5/en/#overview-rate-limits-fill-ratio-based-sub-account-rate-limit).

Unlike other endpoints, the rate limit of this endpoint is determined by the number of orders. If there is only one order in the request, it will consume the rate limit of `Amend order`.  Rate limit is shared with the `Amend multiple orders` REST API endpoints 

> Request Example
    
    
    {
      "id": "1513",
      "op": "batch-amend-orders",
      "args": [
        {
          "instIdCode": 123456,
          "ordId": "12345689",
          "newSz": "2"
        },
        {
          "instIdCode": 123456,
          "ordId": "12344",
          "newSz": "2"
        }
      ]
    }
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
id | String | Yes | Unique identifier of the message   
Provided by client. It will be returned in response message for identifying the corresponding request.   
A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters.  
op | String | Yes | Operation  
`batch-amend-orders`  
args | Array of objects | Yes | Request Parameters  
> instIdCode | Integer | Yes | Instrument ID code  
> cxlOnFail | Boolean | No | Whether the order needs to be automatically canceled when the order amendment fails   
Valid options: `false` or `true`, the default is `false`.  
> ordId | String | Conditional | Order ID   
Either `ordId` or `clOrdId` is required, if both are passed, `ordId` will be used.  
> clOrdId | String | Conditional | Client Order ID as assigned by the client  
> reqId | String | No | Client Request ID as assigned by the client for order amendment   
A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters.  
> newSz | String | Conditional | New quantity after amendment and it has to be larger than 0. Either `newSz` or `newPx` is required. When amending a partially-filled order, the `newSz` should include the amount that has been filled.  
> newPx | String | Conditional | New price after amendment.   
When modifying options orders, users can only fill in one of the following: newPx, newPxUsd, or newPxVol. It must be consistent with parameters when placing orders. For example, if users placed the order using px, they should use newPx when modifying the order.  
> speedBump | String | Conditional | Speed bump  
`1`: Event contract speed bumps (the delay duration will be changed subject to adjustment without prior notice). Required for non-post-only orders of `EVENTS` symbols.  
> newPxUsd | String | Conditional | Modify options orders using USD prices   
Only applicable to options.   
When modifying options orders, users can only fill in one of the following: newPx, newPxUsd, or newPxVol.  
> newPxVol | String | Conditional | Modify options orders based on implied volatility, where 1 represents 100%   
Only applicable to options.   
When modifying options orders, users can only fill in one of the following: newPx, newPxUsd, or newPxVol.  
> pxAmendType | String | No | The price amendment type for orders  
`0`: Do not allow the system to amend to order price if `newPx` exceeds the price limit   
`1`: Allow the system to amend the price to the best available value within the price limit if `newPx` exceeds the price limit  
The default value is `0`  
expTime | String | No | Request effective deadline. Unix timestamp format in milliseconds, e.g. `1597026383085`  
  
> Response Example When All Succeed
    
    
    {
      "id": "1513",
      "op": "batch-amend-orders",
      "data": [
        {
          "clOrdId": "oktswap6",
          "ordId": "12345689",
          "ts": "1695190491421",
          "reqId": "b12344",
          "sCode": "0",
          "sMsg": "",
          "subCode": ""
        },
        {
          "clOrdId": "oktswap7",
          "ordId": "12344",
          "ts": "1695190491421",
          "reqId": "b12344",
          "sCode": "0",
          "sMsg": "",
          "subCode": ""
        }
      ],
      "code": "0",
      "msg": "",
      "inTime": "1695190491421339",
      "outTime": "1695190491423240"
    }
    

> Response Example When All Failed
    
    
    {
      "id": "1513",
      "op": "batch-amend-orders",
      "data": [
        {
          "clOrdId": "",
          "ordId": "12345689",
          "ts": "1695190491421",
          "reqId": "b12344",
          "sCode": "5XXXX",
          "sMsg": "order not exist"
        },
        {
          "clOrdId": "oktswap7",
          "ordId": "",
          "ts": "1695190491421",
          "reqId": "b12344",
              "sCode": "51008",
          "sMsg": "Order failed. Insufficient USDT balance in account",
          "subCode": "1000"
        }
      ],
      "code": "1",
      "msg": "",
      "inTime": "1695190491421339",
      "outTime": "1695190491423240"
    }
    

> Response Example When Partially Successful
    
    
    {
      "id": "1513",
      "op": "batch-amend-orders",
      "data": [
        {
          "clOrdId": "",
          "ordId": "12345689",
          "ts": "1695190491421",
          "reqId": "b12344",
          "sCode": "0",
          "sMsg": ""
        },
        {
          "clOrdId": "",
          "ordId": "oktswap7",
          "ts": "1695190491421",
          "reqId": "b12344",
          "sCode": "51063",
          "sMsg": "OrdId does not exist"
          "subCode": ""
        }
      ],
      "code": "2",
      "msg": "",
      "inTime": "1695190491421339",
      "outTime": "1695190491423240"
    }
    

> Response Example When Format Error
    
    
    {
      "id": "1513",
      "op": "batch-amend-orders",
      "data": [],
      "code": "60013",
      "msg": "Invalid args",
      "inTime": "1695190491421339",
      "outTime": "1695190491423240"
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
id | String | Unique identifier of the message  
op | String | Operation  
code | String | Error Code  
msg | String | Error message  
data | Array of objects | Data  
> ordId | String | Order ID  
> clOrdId | String | Client Order ID as assigned by the client  
> ts | String | Timestamp when the order request processing is finished by our system, Unix timestamp format in milliseconds, e.g. `1597026383085`  
> reqId | String | Client Request ID as assigned by the client for order amendment   
If the user provides reqId in the request, the corresponding reqId will be returned  
> sCode | String | Order status code, `0` means success  
> sMsg | String | Order status message  
> subCode | String | Sub-code of sCode.  
Returns `""` when sCode is 0 (request successful).  
When sCode is not 0 (request failed), returns the sub-code if available; otherwise returns `""`.  
inTime | String | Timestamp at Websocket gateway when the request is received, Unix timestamp format in microseconds, e.g. `1597026383085123`  
outTime | String | Timestamp at Websocket gateway when the response is sent, Unix timestamp format in microseconds, e.g. `1597026383085123`  
newSz   
If the new quantity of the order is less than or equal to the filled quantity when you are amending a partially-filled order, the order status will be changed to filled. 

### WS / Mass cancel order

Cancel all the MMP pending orders of an instrument family.  

Only applicable to Option in Portfolio Margin mode, and MMP privilege is required.

#### URL Path

/ws/v5/private (required login)

#### Rate Limit: 5 requests per 2 seconds

#### Rate limit rule: User ID

Rate limit is shared with the `Mass Cancel Order` REST API endpoints 

> Request Example
    
    
    {
        "id": "1512",
        "op": "mass-cancel",
        "args": [{
            "instType":"OPTION",
            "instFamily":"BTC-USD"
        }]
    }
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
id | String | Yes | Unique identifier of the message   
Provided by client. It will be returned in response message for identifying the corresponding request.   
A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters.  
op | String | Yes | Operation  
`mass-cancel`  
args | Array of objects | Yes | Request parameters  
> instType | String | Yes | Instrument type  
`OPTION`  
> instFamily | String | Yes | Instrument family  
> lockInterval | String | No | Lock interval(ms)  
The range should be [0, 10 000]  
The default is 0. You can set it as "0" if you want to unlock it immediately.  
Error 54008 will be returned when placing order during lock interval, it is different from 51034 which is thrown when MMP is triggered  
  
> ##### Successful Response Example
    
    
    {
        "id": "1512",
        "op": "mass-cancel",
        "data": [
            {
                "result": true
            }
        ],
        "code": "0",
        "msg": ""
    } 
    

> Response Example When Format Error
    
    
    {
      "id": "1512",
      "op": "mass-cancel",
      "data": [],
      "code": "60013",
      "msg": "Invalid args"
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
id | String | Unique identifier of the message  
op | String | Operation  
code | String | Error Code  
msg | String | Error message  
data | Array of objects | Data  
> result | Boolean | Result of the request `true`, `false`

---

# 交易

`交易`功能模块下的API接口需要身份验证。

### POST / 下单 

只有当您的账户有足够的资金才能下单。  
  

#### 限速：60次/2s

#### 跟单交易带单员带单产品的限速：4次/2s

#### 限速规则（期权以外）：User ID + Instrument ID

#### 限速规则（只限期权）：User ID + Instrument Family

#### 权限：交易

该接口限速同时受到 [子账户限速](/docs-v5/log_zh/#upcoming-changes-sub-account-rate-limit) 及 [基于成交比率的子账户限速](/docs-v5/log_zh/#upcoming-changes-fill-ratio-based-sub-account-rate-limit) 限速规则的影响。

#### HTTP请求

`POST /api/v5/trade/order`

> 请求示例
    
    
    # 币币下单
    POST /api/v5/trade/order
    body
    {
        "instId":"BTC-USDT",
        "tdMode":"cash",
        "clOrdId":"b15",
        "side":"buy",
        "ordType":"limit",
        "px":"2.15",
        "sz":"2"
    }
    
    
    
    import okx.Trade as Trade
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # 实盘: 0, 模拟盘: 1
    
    tradeAPI = Trade.TradeAPI(apikey, secretkey, passphrase, False, flag)
    
    # 现货模式限价单
    result = tradeAPI.place_order(
        instId="BTC-USDT",
        tdMode="cash",
        clOrdId="b15",
        side="buy",
        ordType="limit",
        px="2.15",
        sz="2"
    )
    
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
instId | String | 是 | 产品ID，如 `BTC-USDT`  
tdMode | String | 是 | 交易模式  
保证金模式：`isolated`：逐仓（仅限于现货杠杆逐仓）；`cross`：全仓   
非保证金模式：`cash`：非保证金  
`spot_isolated`：现货逐仓(仅适用于现货带单) ，现货带单时，`tdMode` 的值需要指定为`spot_isolated`  
注意：`isolated`（现货杠杆逐仓）在跨币种保证金模式和组合保证金模式下不可用。  
  
事件合约对应交易产品仅支持`isolated`逐仓下单  
ccy | String | 否 | 保证金币种，适用于`逐仓杠杆`及`合约模式`下的`全仓杠杆`订单  
clOrdId | String | 否 | 客户自定义订单ID   
字母（区分大小写）与数字的组合，可以是纯字母、纯数字且长度要在1-32位之间。  
tag | String | 否 | 订单标签  
字母（区分大小写）与数字的组合，可以是纯字母、纯数字，且长度在1-16位之间。  
side | String | 是 | 订单方向  
`buy`：买， `sell`：卖  
posSide | String | 可选 | 持仓方向  
在开平仓模式下必填，且仅可选择 `long` 或 `short`。 仅适用交割、永续。`SPOT` 或 `MARGIN` 订单请勿传此字段。交割/永续在开平仓模式下如未填写，返回错误码 51000。  
ordType | String | 是 | 订单类型   
`market`：市价单，仅适用于`币币/杠杆/交割/永续`  
`limit`：限价单   
`post_only`：只做maker单   
`fok`：全部成交或立即取消   
`ioc`：立即成交并取消剩余   
`optimal_limit_ioc`：以价格限制区间的最高买价（买单）或最低卖价（卖单）挂限价单，未成交部分立即取消（IOC）。仅适用交割、永续合约，订单不会以超出当前价格限制边界的价格成交  
`mmp`：做市商保护(仅适用于组合保证金账户模式下的期权订单)  
`mmp_and_post_only`：做市商保护且只做maker单(仅适用于组合保证金账户模式下的期权订单)  
`elp`：流动性增强计划订单  
sz | String | 是 | 委托数量  
px | String | 可选 | 委托价格，仅适用于`limit`、`post_only`、`fok`、`ioc`、`mmp`、`mmp_and_post_only`类型的订单  
期权下单时，px/pxUsd/pxVol 只能填一个  
speedBump | String | 可选 | 减速带  
`1`：事件合约速度限制（延迟可能因市场情况调整，不提前通知）。对 `EVENTS` 产品的非只挂单操作为必填。  
outcome | String | 可选 | 用户交易的市场结果方向。  
`yes`  
`no`  
仅适用于 `EVENTS`，且为必填  
pxUsd | String | 可选 | 以USD价格进行期权下单   
仅适用于期权   
期权下单时 px/pxUsd/pxVol 必填一个，且只能填一个  
pxVol | String | 可选 | 以隐含波动率进行期权下单，例如 1 代表 100%   
仅适用于期权   
期权下单时 px/pxUsd/pxVol 必填一个，且只能填一个  
reduceOnly | Boolean | 否 | 是否只减仓，`true` 或 `false`，默认`false`  
仅适用于`币币杠杆`，以及买卖模式下的`交割/永续`  
适用于`合约模式`/`跨币种保证金模式`  
tgtCcy | String | 否 | 市价单委托数量`sz`的单位，仅适用于`币币`市价订单  
`base_ccy`: 交易货币 ；`quote_ccy`：计价货币  
买单默认`quote_ccy`， 卖单默认`base_ccy`  
banAmend | Boolean | 否 | 是否禁止系统在余额不足时自动缩减币币市价单数量。true 或 false，默认false。  
为true时：余额不足时，整笔订单将被拒绝。为false（默认）时：系统将缩减 sz 至可用余额所能支持的数量后执行。仅适用于币币市价单  
pxAmendType | String | 否 | 订单价格修正类型  
`0`：当`px`超出价格限制时，不允许系统修改订单价格   
`1`：当`px`超出价格限制时，允许系统将价格修改为限制范围内的最优值  
默认值为`0`  
tradeQuoteCcy | String | 否 | 用于交易的计价币种。仅适用于`币币`。  
默认值为 `instId` 的计价币种，比如：对于 `BTC-USD`，默认取 `USD`。  
slippagePct | String | 否 | 币币、币币杠杆市价单（`tgtCcy` 为到手币种：买单为 `base_ccy`，卖单为 `quote_ccy`）的最大可接受滑点。  
取值范围：`0` 至 `0.05`（即 0% 至 5%，含边界），以百分比形式表示时最多保留 2 位小数，例如 `0.01`（1%）和 `0.0123`（1.23%）合法；`0.01234`（1.234%）将被拒绝。  
不填或为空时，默认为 `0.00%`。  
不支持改单修改滑点，如需调整请撤单重新提交。  
仅适用于币币和币币杠杆的市价单。  
stpMode | String | 否 | 自成交保护模式   
`cancel_maker`,`cancel_taker`, `cancel_both`  
Cancel both不支持FOK   
  
默认使用账户层面的acctStpMode进行下单，该字段的默认值为`cancel_maker`，用户可通过母账户登录网页修改该配置；用户亦可以通过下单接口的stpMode参数指定订单的STP模式。  
isElpTakerAccess | Boolean | 否 | 是否作为 taker 吃单 ELP  
`true`：该请求能吃单 ELP，但会被施加延迟  
`false`：该请求不能吃单 ELP，并且没有延迟  
  
默认值为`false`，`true`仅适用于ioc订单  
attachAlgoOrds | Array of objects | 否 | 附带止盈止损或移动止盈止损订单信息  
> attachAlgoClOrdId | String | 否 | 下单附带止盈止损或移动止盈止损时，客户自定义的策略订单ID   
字母（区分大小写）与数字的组合，可以是纯字母、纯数字且长度要在1-32位之间。  
订单完全成交，下附带策略委托单时，该值会传给`algoClOrdId`  
> tpTriggerPx | String | 可选 | 止盈触发价  
对于条件止盈单，如果填写此参数，必须填写 止盈委托价  
> tpTriggerRatio | String | 可选 | 止盈触发比例，0.3 代表 30%   
仅适用于`交割`/`永续`合约  
`tpTriggerPx` 和 `tpTriggerRatio` 只能传入其中一个  
如果主单为买入订单，必须大于 0，如果主单为卖出订单，必须处于 -1 和 0 之间。  
> tpOrdPx | String | 可选 | 止盈委托价  
对于条件止盈单，如果填写此参数，必须填写 止盈触发价  
对于限价止盈单，需填写此参数，不需要填写止盈触发价  
委托价格为-1时，执行市价止盈  
> tpOrdKind | String | 否 | 止盈订单类型  
`condition`: 条件单  
`limit`: 限价单  
默认为`condition`  
> slTriggerPx | String | 可选 | 止损触发价，如果填写此参数，必须填写 止损委托价  
> slTriggerRatio | String | 可选 | 止损触发比例，0.3 代表 30%   
仅适用于`交割`/`永续`合约  
`slTriggerPx` 和 `slTriggerRatio` 只能传入其中一个  
如果主单为买入订单，必须处于 0 和 1 之间，如果主单为卖出订单，必须大于 0。  
> slOrdPx | String | 可选 | 止损委托价，如果填写此参数，必须填写 止损触发价  
委托价格为-1时，执行市价止损  
> tpTriggerPxType | String | 否 | 止盈触发价类型  
`last`：最新价格  
`index`：指数价格  
`mark`：标记价格  
默认为`last`  
> slTriggerPxType | String | 否 | 止损触发价类型  
`last`：最新价格  
`index`：指数价格  
`mark`：标记价格  
默认为`last`  
> sz | String | 可选 | 数量。仅适用于“多笔止盈”的止盈订单，且对于“多笔止盈”的止盈订单必填  
> amendPxOnTriggerType | String | 否 | 是否启用开仓价止损，仅适用于分批止盈的止损订单，第一笔止盈触发时，止损触发价格是否移动到开仓均价止损  
`0`：不开启，默认值   
`1`：开启，且止损触发价不能为空  
> callbackRatio | String | 可选 | 回调幅度的比例，如 `0.05` 代表 5%。  
`callbackRatio` 和 `callbackSpread` 必须传入其中一个，且只能传入一个。  
仅适用于 `ordType` = `move_order_stop`  
> callbackSpread | String | 可选 | 回调幅度的价距。  
`callbackRatio` 和 `callbackSpread` 必须传入其中一个，且只能传入一个。  
仅适用于 `ordType` = `move_order_stop`  
> activePx | String | 否 | 激活价格。  
激活价格是移动止盈止损的激活条件，当市场最新成交价达到或超过激活价格，委托被激活。激活后系统开始计算止盈止损的实际触发价格。如果不填写激活价格，即下单后就被激活。  
仅适用于 `ordType` = `move_order_stop`  
  
> 返回结果
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
            {
                "clOrdId":"oktswap6",
                "ordId":"12345689",
                "tag":"",
                "ts":"1695190491421",
                "sCode":"0",
                "sMsg":"",
                "subCode": ""
            }
        ],
        "inTime": "1695190491421339",
        "outTime": "1695190491423240"
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
code | String | 结果代码，`0`表示成功  
msg | String | 错误信息，代码为0时，该字段为空  
data | Array of objects | 包含结果的对象数组  
> ordId | String | 订单ID  
> clOrdId | String | 客户自定义订单ID  
> tag | String | 订单标签  
> ts | String | 系统完成订单请求处理的时间戳，Unix时间戳的毫秒数格式，如 `1597026383085`  
> sCode | String | 事件执行结果的code，0代表成功  
> sMsg | String | 事件执行失败或成功时的msg  
> subCode | String | sCode 的子码。  
当 sCode 为 0（请求成功）时，返回 `""`。  
当 sCode 不为 0（事件执行失败）且存在子码时，返回对应的子码；若无子码，则返回 `""`。  
inTime | String | REST网关接收请求时的时间戳，Unix时间戳的微秒数格式，如 `1597026383085123`   
返回的时间是请求验证后的时间。  
outTime | String | REST网关发送响应时的时间戳，Unix时间戳的微秒数格式，如 `1597026383085123`  
tdMode  
交易模式，下单时需要指定  
**现货模式：**  
\- 币币和期权买方：cash  
**合约模式：**  
\- 逐仓杠杆（仅限于现货杠杆逐仓）：isolated  
\- 全仓杠杆：cross  
\- 币币：cash  
\- 全仓交割/永续/期权：cross  
**跨币种保证金模式：**  
\- 全仓币币：cross  
\- 全仓交割/永续/期权：cross  
**组合保证金模式：**  
\- 全仓币币：cross  
\- 全仓交割/永续/期权：cross  
clOrdId  
clOrdId 是用户在 User ID 维度自定义的订单唯一标识符。如果在请求参数中传入了，那它一定会在返回参数内，并且可以用于查询订单，撤销订单，修改订单等接口。  
clOrdId 不能与当前所有挂单（live 或 partially_filled 状态）的 clOrdId 重复。订单达到终态（filled、canceled、mmp_canceled）后，相同的 clOrdId 可重新用于新订单。系统不强制历史唯一性——当多笔订单共享同一 clOrdId 时，GET /api/v5/trade/order 仅返回最新一笔。"普通委托单"指通过本接口下的标准订单；clOrdId 不会传递至附带的止盈止损策略订单。  posSide  
持仓方向，买卖模式下此参数非必填，如果填写仅可以选择net；在开平仓模式下必填，且仅可选择 long 或 short。  
开平仓模式下，side和posSide需要进行组合  
开多：买入开多（side 填写 buy； posSide 填写 long ）  
开空：卖出开空（side 填写 sell； posSide 填写 short ）  
平多：卖出平多（side 填写 sell；posSide 填写 long ）  
平空：买入平空（side 填写 buy； posSide 填写 short ）  
组合保证金模式：交割和永续仅支持买卖模式  
SPOT 或 MARGIN 订单请勿传此字段。交割/永续在买卖模式下可不传或传 `net`。  ordType  
订单类型，创建新订单时必须指定，您指定的订单类型将影响需要哪些订单参数和撮合系统如何执行您的订单，以下是有效的ordType：  
普通委托：  
limit：限价单，要求指定sz 和 px  
market：市价单，币币和币币杠杆，是市价委托吃单；交割合约和永续合约，是自动以最高买/最低卖价格委托，遵循限价机制；期权合约不支持市价委托；由于市价委托无法确定成交价格，为确保有足够的资产买入设定数量的交易币种，会多冻结5%的计价币资产  
高级委托：  
post_only：限价委托，在下单那一刻只做maker，如果该笔订单的任何部分会吃掉当前挂单深度，则该订单将被全部撤销。  
fok：限价委托，全部成交或立即取消，如果无法全部成交该笔订单，则该订单将被全部撤销。  
ioc：限价委托，立即成交并取消剩余，立即按照委托价格撮合成交，并取消该订单剩余未完成数量，不会在深度列表上展示委托数量。  
optimal_limit_ioc：以价格限制区间的最高买价（买单）或最低卖价（卖单）挂限价单，未成交部分立即取消（IOC），仅适用于交割合约和永续合约。订单不会以超出当前价格限制边界的价格成交。  sz  
交易数量，表示要购买或者出售的数量。  
当币币/币币杠杆以限价买入和卖出时，指交易货币数量。  
当币币杠杆以市价买入时，指计价货币的数量。  
当币币杠杆以市价卖出时，指交易货币的数量。  
对于币币市价单，单位由 tgtCcy 决定  
当交割、永续、期权买入和卖出时，指合约张数。合约面值 = sz × ctVal × markPx（正向合约）或 sz × ctVal（反向合约，USD 计价）。ctVal 和 ctType 可通过 GET /api/v5/public/instruments 获取。  reduceOnly  
只减仓，下单时，此参数设置为 true 时，表示此笔订单具有减仓属性，只会减少持仓数量，不会增加新的持仓仓位  
对于同一杠杆产品，所有反方向挂单的币数加上当前只减仓下单数量，不能超过仓位资产；负债还完后，如果还有剩余的委托数量，不会反向开仓，而是会进行币币交易。  
对于同一交割/永续产品，当前只减仓下单张数，加上价格时间优先于当前只减仓下单的只减仓挂单张数总和，不能超过持仓数量  
仅适用于`合约模式`和`跨币种保证金模式`  
仅适用于`币币杠杆`，以及买卖模式下的`交割/永续`  
注意：交割和永续合约在开平仓模式下，所有的平仓单都有只减仓逻辑，不受该字段传值的影响。  
如果 sz 超过当前持仓数量，整笔订单同样会被拒绝——系统不会自动截取至持仓数量。  tgtCcy  
市价单委托数量`sz`的单位：仅适用于币币市价下单交易。  
快速参考（以 BTC-USDT 为例）：  
\- tgtCcy=`quote_ccy`，sz=100（买入）：花费 100 USDT 购买 BTC。  
\- tgtCcy=`base_ccy`，sz=0.001（买入）：以市价买入 0.001 BTC。  
\- tgtCcy=`base_ccy`，sz=0.001（卖出，默认）：卖出 0.001 BTC。  
\- tgtCcy=`quote_ccy`，sz=100（卖出）：卖出 BTC 直至收到 100 USDT。  
交易货币：base_ccy  
计价货币：quote_ccy   
您在使用交易货币买入或者计价货币卖出时，请知晓：   
1.如果您输入的数量大于当前可买或者可卖的数量，系统将按照您的最大可买或者可卖数量帮您完成交易，如果您希望按照指定数量成交，那您可以尝试使用限价单，等待市场价格波动到锁定的余额可以买入或卖出您指定的数量。   
2.如果您输入的数量不大于当前可买或者可卖的数量，那当市场价格波动过大时，锁定的余额可能没办法买入您输入的交易货币数量或卖出您输入的计价货币数量，为保证您的交易体验，我们基于【能买多少买多少】或者【能卖多少卖多少】的原则，更改下单的数量帮您完成交易。此外，我们将尽量多锁定一点余额来规避更改下单数量的情况。   
2.1 交易币买入例子：   
以市价下单 买入 10个LTC为例，用户可买为11个，此时 10 < 11，挂单成功。当LTC-USDT的市价为200，用户被锁定余额为3,000 USDT，200*10 < 3,000，最终成交10个LTC； 若市场波动过大，LTC-USDT的市价为400，此时400*10 > 3,000，当用户被锁定的余额不够买入下单指定的交易货币数量时，系統使用用户被锁定的最大余额3,000 USDT下单买入，最终成交 3,000/400 = 7.5个 LTC。   
2.2 计价币卖出例子：   
以市价下单 卖出 1,000USDT为例，用户可卖为1,200USDT，1,000 < 1,200，挂单成功。LTC-USDT的市价为200，用户被锁定的余额为6个LTC，最终成交5个LTC； 若市场波动过大，LTC-USDT的市价为100，100*6 < 1,000，当用户被锁定的余额不够卖出下单指定的计价货币数量时，系統使用用户被锁定的最大余额6个LTC下单，最终成交 6 * 100 = 600 USDT。  px  
期权下单时，委托价格需为 tickSz 的整数倍。  
当不为整数倍时，取值规则以tickSz取 0.0005 为例：  
当委托价格对0.0005的余数大于0.00025或者委托价格小于0.0005时，向上取；  
当委托价格对0.0005的余数小于等于0.00025，且委托价格大于0.0005时，向下取。  对于下单附带止盈止损：  
附带的止盈止损订单仅在母单成交后才会激活。若母单在任何成交前被撤销，附带的止盈止损也将一并丢弃。如需独立于母单的止盈止损，请使用 POST /api/v5/trade/order-algo。  
1\. 只有当该订单成交时，才会生成止盈止损策略订单；若母单在成交前被撤销，则不会生成止盈止损策略订单。  
  
2\. tgtCcy 为 base_ccy 时的市价买单和 tgtCcy 为 quote_ccy 时的市价卖单，均不支持附带止盈止损  
3\. tpOrdKind 为 limit，且只有一笔单边止盈时，attachAlgoClOrdId 可以作为 clOrdId 在获取订单信息接口查询。  
4\. 对于“分批止盈”，包含限价止盈和触发止盈：  
* 分批止盈的每笔止盈止损订单仅支持单向止盈止损，slTriggerPx&slOrdPx 与 tpTriggerPx&tpOrdPx 只能填写一组，否则 报错 51076  
* 同一笔订单上附带分批止盈的止盈触发价类型 (tpTriggerPxType) 必须保持一致，否则报错 51080  
* 同一笔订单上附带分批止盈的止盈触发价 (tpTriggerPx) 不能相等，否则报错 51081  
* 在附带分批止盈时，止盈订单的数量不能为空，否则报错 51089  
* 同一笔订单上分批止盈的止盈数量之和，需要等于订单的委托数量，否则报错 51083  
* 同一笔订单上分批止盈的止盈委托不能超过 10 笔，否则报错 51079  
* 币币/杠杆不支持开启'开仓价止损'，否则报错 51077  
* 同一笔订单上附带分批止盈的止损委托单不能超过 1 笔，否则报错 51084  
* 附带止盈止损开启'开仓价止损'时 (amendPxOnTriggerType 设置为 1)，该笔订单上的止盈委托单必须大于等于 2 笔，否则报错 51085  
* 同一笔订单上附带分批止盈的止盈类型必须保持一致，否则报错 51091  
* 同一笔订单上附带分批止盈的止盈委托价不能相等，否则报错 51092  
* 同一笔订单上附带分批止盈，其中限价止盈的止盈委托价 (tpOrdPx) 不能为 -1 (市价)，否则报错 51093  
* 币币、杠杆和期权交易不支持限价止盈，否则报错 51094  
强制自成交保护  
交易系统会以母账户维度实施强制自成交保护，同一母账户下所有账户，包括母账户本身和所有子账户，都无法进行自成交。默认使用账户层面的acctStpMode进行下单，该字段的默认值为`cancel_maker`，用户可通过母账户登录网页修改该配置；用户亦可以通过下单接口的stpMode参数指定订单的STP模式。  
强制自成交保护不会导致延迟。  
有三种STP模式。STP模式始终基于taker订单中的配置。  
1.Cancel Maker：这是默认的STP模式，系统撤Maker订单以防止自成交。然后，taker订单会基于深度继续和下一个订单成交。  
2.Cancel Taker：撤Taker订单以防止自成交。如果用户的Maker订单不是深度里第一个订单，Taker订单会被部分成交，然后撤单。FOK订单会确保完全成交和自成交保护。  
3.Cancel Both：撤Taker和Maker订单以防止自成交。如果用户的Maker订单不是深度里第一个订单，Taker订单会被部分成交，然后Taker订单的剩余数量和第一个自我Maker订单被取消。此模式不支持FOK订单。将 stpMode=cancel_both 与 ordType=`fok` 组合使用将返回错误码 50016。  
tradeQuoteCcy  
对于特定国家和地区的用户，下单成功需要填写该参数，否则会取 `instId` 的计价币种为默认值，报错 51000。  
传值必须取 tradeQuoteCcyList 的枚举值，tradeQuoteCcyList 来自获取交易产品基础信息(GET /api/v5/account/instruments) 接口。  
isElpTakerAccess:true订单限速  
\- 50个/2s，限制维度为 User ID + Instrument ID  
\- 该限速会在 REST 和 WebSocket 的下单及批量下单接口中共享 

### POST / 批量下单 

每次最多可以批量提交20个新订单。请求参数应该按数组格式传递，会依次委托订单。  
  

#### 限速：300个/2s

#### 跟单交易带单员带单产品的限速：4个/2s

#### 限速规则（期权以外）：User ID + Instrument ID

#### 限速规则（只限期权）：User ID + Instrument Family

#### 权限：交易

该接口限速同时受到 [子账户限速](/docs-v5/log_zh/#upcoming-changes-sub-account-rate-limit) 及 [基于成交比率的子账户限速](/docs-v5/log_zh/#upcoming-changes-fill-ratio-based-sub-account-rate-limit) 限速规则的影响。

与其他限速按接口调用次数不同，该接口限速按订单的总个数限速。如果单次批量请求中只有一个元素，则算在单个`下单`限速中。 

#### HTTP请求

`POST /api/v5/trade/batch-orders`

> 请求示例
    
    
    # 币币批量下单
     POST /api/v5/trade/batch-orders
     body
     [
        {
            "instId":"BTC-USDT",
            "tdMode":"cash",
            "clOrdId":"b15",
            "side":"buy",
            "ordType":"limit",
            "px":"2.15",
            "sz":"2"
        },
        {
            "instId":"BTC-USDT",
            "tdMode":"cash",
            "clOrdId":"b16",
            "side":"buy",
            "ordType":"limit",
            "px":"2.15",
            "sz":"2"
        }
    ]
    
    
    
    import okx.Trade as Trade
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # 实盘: 0, 模拟盘: 1
    
    tradeAPI = Trade.TradeAPI(apikey, secretkey, passphrase, False, flag)
    
    # 批量下单
    place_orders_without_clOrdId = [
        {"instId": "BTC-USDT", "tdMode": "cash", "clOrdId": "b15", "side": "buy", "ordType": "limit", "px": "2.15", "sz": "2"},
        {"instId": "BTC-USDT", "tdMode": "cash", "clOrdId": "b16", "side": "buy", "ordType": "limit", "px": "2.15", "sz": "2"}
    ]
    
    result = tradeAPI.place_multiple_orders(place_orders_without_clOrdId)
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
instId | String | 是 | 产品ID，如 `BTC-USDT`  
tdMode | String | 是 | 交易模式  
保证金模式：`isolated`：逐仓 ；`cross`：全仓   
非保证金模式：`cash`：非保证金  
`spot_isolated`：现货逐仓(仅适用于现货带单) ，现货带单时，`tdMode` 的值需要指定为`spot_isolated`  
注意：`isolated` 在跨币种保证金模式和组合保证金模式下不可用。  
  
事件合约对应交易产品仅支持`isolated`逐仓下单  
ccy | String | 否 | 保证金币种，适用于`逐仓杠杆`及`合约模式`下的`全仓杠杆`订单  
clOrdId | String | 否 | 客户自定义订单ID  
字母（区分大小写）与数字的组合，可以是纯字母、纯数字且长度要在1-32位之间。  
tag | String | 否 | 订单标签  
字母（区分大小写）与数字的组合，可以是纯字母、纯数字且长度要在1-16位之间。  
side | String | 是 | 订单方向 `buy`：买， `sell`：卖  
posSide | String | 可选 | 持仓方向  
在开平仓模式下必填，且仅可选择 `long` 或 `short`。 仅适用交割、永续。  
ordType | String | 是 | 订单类型   
`market`：市价单，仅适用于`币币/杠杆/交割/永续`  
`limit`：限价单   
`post_only`：只做maker单   
`fok`：全部成交或立即取消   
`ioc`：立即成交并取消剩余   
`optimal_limit_ioc`：市价委托立即成交并取消剩余（仅适用交割、永续）  
`mmp`：做市商保护(仅适用于组合保证金账户模式下的期权订单)  
`mmp_and_post_only`：做市商保护且只做maker单(仅适用于组合保证金账户模式下的期权订单)  
`elp`：流动性增强计划订单  
sz | String | 是 | 委托数量  
px | String | 可选 | 委托价格，仅适用于`limit`、`post_only`、`fok`、`ioc`、`mmp`、`mmp_and_post_only`类型的订单  
期权下单时，px/pxUsd/pxVol 只能填一个  
speedBump | String | 可选 | 减速带  
`1`：事件合约速度限制（延迟可能因市场情况调整，不提前通知）。对 `EVENTS` 产品的非只挂单操作为必填。  
outcome | String | 可选 | 用户交易的市场结果方向。  
`yes`  
`no`  
仅适用于 `EVENTS`，且为必填  
pxUsd | String | 可选 | 以USD价格进行期权下单   
仅适用于期权   
期权下单时 px/pxUsd/pxVol 必填一个，且只能填一个  
pxVol | String | 可选 | 以隐含波动率进行期权下单，例如 1 代表 100%   
仅适用于期权   
期权下单时 px/pxUsd/pxVol 必填一个，且只能填一个  
reduceOnly | Boolean | 否 | 是否只减仓，`true` 或 `false`，默认`false`  
仅适用于`币币杠杆`，以及买卖模式下的`交割/永续`  
仅适用于`合约模式`和`跨币种保证金模式`  
tgtCcy | String | 否 | 市价单委托数量`sz`的单位，仅适用于`币币`市价订单  
`base_ccy`: 交易货币 ；`quote_ccy`：计价货币  
买单默认`quote_ccy`， 卖单默认`base_ccy`  
banAmend | Boolean | 否 | 是否禁止币币市价改单，true 或 false，默认false   
为true时，余额不足时，系统不会改单，下单会失败，仅适用于币币市价单  
pxAmendType | String | 否 | 订单价格修正类型  
`0`：当`px`超出价格限制时，不允许系统修改订单价格   
`1`：当`px`超出价格限制时，允许系统将价格修改为限制范围内的最优值  
默认值为`0`  
stpMode | String | 否 | 自成交保护模式   
`cancel_maker`,`cancel_taker`, `cancel_both`  
Cancel both不支持FOK  
  
默认使用账户层面的acctStpMode进行下单，该字段的默认值为`cancel_maker`，用户可通过母账户登录网页修改该配置；用户亦可以通过下单接口的stpMode参数指定订单的STP模式。  
tradeQuoteCcy | String | 否 | 用于交易的计价币种。仅适用于`币币`。  
默认值为 `instId` 的计价币种，比如：对于 `BTC-USD`，默认取 `USD`。  
slippagePct | String | 否 | 币币、币币杠杆市价单（`tgtCcy` 为到手币种：买单为 `base_ccy`，卖单为 `quote_ccy`）的最大可接受滑点。  
取值范围：`0` 至 `0.05`（即 0% 至 5%，含边界），以百分比形式表示时最多保留 2 位小数，例如 `0.01`（1%）和 `0.0123`（1.23%）合法；`0.01234`（1.234%）将被拒绝。  
不填或为空时，默认为 `0.00%`。  
不支持改单修改滑点，如需调整请撤单重新提交。  
仅适用于币币和币币杠杆的市价单。  
isElpTakerAccess | Boolean | 否 | 是否作为 taker 吃单 ELP  
`true`：该请求能吃单 ELP，但会被施加延迟  
`false`：该请求不能吃单 ELP，并且没有延迟  
  
默认值为`false`，`true`仅适用于ioc订单  
attachAlgoOrds | Array of objects | 否 | 附带止盈止损或移动止盈止损订单信息  
> attachAlgoClOrdId | String | 否 | 下单附带止盈止损或移动止盈止损时，客户自定义的策略订单ID   
字母（区分大小写）与数字的组合，可以是纯字母、纯数字且长度要在1-32位之间。  
订单完全成交，下附带策略委托单时，该值会传给`algoClOrdId`  
> tpTriggerPx | String | 可选 | 止盈触发价  
对于条件止盈单，如果填写此参数，必须填写 止盈委托价  
> tpTriggerRatio | String | 可选 | 止盈触发比例，0.3 代表 30%   
仅适用于`交割`/`永续`合约   
`tpTriggerPx` 和 `tpTriggerRatio` 只能传入其中一个  
如果主单为买入订单，必须大于 0，如果主单为卖出订单，必须处于 -1 和 0 之间。  
> tpOrdPx | String | 可选 | 止盈委托价  
对于条件止盈单，如果填写此参数，必须填写 止盈触发价  
对于限价止盈单，需填写此参数，不需要填写止盈触发价  
委托价格为-1时，执行市价止盈  
> tpOrdKind | String | 否 | 止盈订单类型  
`condition`: 条件单  
`limit`: 限价单  
默认为`condition`  
> slTriggerPx | String | 可选 | 止损触发价，如果填写此参数，必须填写 止损委托价  
> slTriggerRatio | String | 可选 | 止损触发比例，0.3 代表 30%   
仅适用于`交割`/`永续`合约   
`slTriggerPx` 和 `slTriggerRatio` 只能传入其中一个  
如果主单为买入订单，必须处于 0 和 1 之间，如果主单为卖出订单，必须大于 0。0 代表删除止损。  
> slOrdPx | String | 可选 | 止损委托价，如果填写此参数，必须填写 止损触发价  
委托价格为-1时，执行市价止损  
> tpTriggerPxType | String | 否 | 止盈触发价类型  
`last`：最新价格  
`index`：指数价格  
`mark`：标记价格  
默认为`last`  
> slTriggerPxType | String | 否 | 止损触发价类型  
`last`：最新价格  
`index`：指数价格  
`mark`：标记价格  
默认为`last`  
> sz | String | 可选 | 数量。仅适用于"多笔止盈"的止盈订单，且对于"多笔止盈"的止盈订单必填  
> amendPxOnTriggerType | String | 否 | 是否启用开仓价止损，仅适用于分批止盈的止损订单，第一笔止盈触发时，止损触发价格是否移动到开仓均价止损  
`0`：不开启，默认值   
`1`：开启，且止损触发价不能为空  
> callbackRatio | String | 可选 | 回调幅度的比例，如 `0.05` 代表 5%。  
`callbackRatio` 和 `callbackSpread` 必须传入其中一个，且只能传入一个。  
仅适用于 `ordType` = `move_order_stop`  
> callbackSpread | String | 可选 | 回调幅度的价距。  
`callbackRatio` 和 `callbackSpread` 必须传入其中一个，且只能传入一个。  
仅适用于 `ordType` = `move_order_stop`  
> activePx | String | 否 | 激活价格。  
激活价格是移动止盈止损的激活条件，当市场最新成交价达到或超过激活价格，委托被激活。激活后系统开始计算止盈止损的实际触发价格。如果不填写激活价格，即下单后就被激活。  
仅适用于 `ordType` = `move_order_stop`  
  
> 返回结果
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
            {
                "clOrdId":"oktswap6",
                "ordId":"12345689",
                "tag":"",
                "ts":"1695190491421",
                "sCode":"0",
                "sMsg":"",
                "subCode":""
            },
            {
                "clOrdId":"oktswap7",
                "ordId":"12344",
                "tag":"",
                "ts":"1695190491421",
                "sCode":"0",
                "sMsg":"",
                "subCode":""
            }
        ],
        "inTime": "1695190491421339",
        "outTime": "1695190491423240"
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
code | String | 结果代码，`0`表示成功  
msg | String | 错误信息，代码为0时，该字段为空  
data | Array of objects | 包含结果的对象数组  
> ordId | String | 订单ID  
> clOrdId | String | 客户自定义订单ID  
> tag | String | 订单标签  
> ts | String | 系统完成订单请求处理的时间戳，Unix时间戳的毫秒数格式，如 `1597026383085`  
> sCode | String | 事件执行结果的code，0代表成功  
> sMsg | String | 事件执行失败或成功时的msg  
> subCode | String | sCode 的子码。  
当 sCode 为 0（请求成功）时，返回 `""`。  
当 sCode 不为 0（请求失败）且存在子码时，返回对应的子码；若无子码，则返回 `""`。  
inTime | String | REST网关接收请求时的时间戳，Unix时间戳的微秒数格式，如 `1597026383085123`   
返回的时间是请求验证后的时间。  
outTime | String | REST网关发送响应时的时间戳，Unix时间戳的微秒数格式，如 `1597026383085123`  
在组合保证金账户模式下，或者全部成功，或者全部失败。  clOrdId  
clOrdId是用户自定义的唯一ID用来识别订单。如果在请求参数中传入了，那它一定会在返回参数内，并且可以用于查询订单，撤销订单，修改订单等接口。 clOrdId不能与当前所有挂单和当前请求中的clOrdId重复。  isElpTakerAccess:true订单限速  
\- 50个/2s，限制维度为 User ID + Instrument ID  
\- 该限速会在 REST 和 WebSocket 的下单及批量下单接口中共享 

### POST / 撤单 

撤销之前下的未完成订单。

#### 限速：60次/2s

#### 限速规则（期权以外）：User ID + Instrument ID

#### 限速规则（只限期权）：User ID + Instrument Family

#### 权限：交易

#### HTTP请求

`POST /api/v5/trade/cancel-order`

> 请求示例
    
    
    POST /api/v5/trade/cancel-order
    body
    {
        "ordId":"590908157585625111",
        "instId":"BTC-USDT"
    }
    
    
    
    
    import okx.Trade as Trade
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # 实盘: 0, 模拟盘: 1
    
    tradeAPI = Trade.TradeAPI(apikey, secretkey, passphrase, False, flag)
    
    # 撤单
    result = tradeAPI.cancel_order(instId="BTC-USDT", ordId = "590908157585625111")
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
instId | String | 是 | 产品ID，如 `BTC-USDT`  
ordId | String | 可选 | 订单ID， `ordId`和`clOrdId`必须传一个，若传两个，以`ordId`为主  
clOrdId | String | 可选 | 用户自定义ID  
  
> 返回结果
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
            {
                "clOrdId":"oktswap6",
                "ordId":"12345689",
                "ts":"1695190491421",
                "sCode":"0",
                "sMsg":""
            }
        ],
        "inTime": "1695190491421339",
        "outTime": "1695190491423240"
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
code | String | 结果代码，`0`表示成功  
msg | String | 错误信息，代码为0时，该字段为空  
data | Array of objects | 包含结果的对象数组  
> ordId | String | 订单ID  
> clOrdId | String | 客户自定义订单ID  
> ts | String | 系统完成订单请求处理的时间戳，Unix时间戳的毫秒数格式，如 `1597026383085`  
> sCode | String | 事件执行结果的code，0代表成功  
> sMsg | String | 事件执行失败时的msg  
inTime | String | REST网关接收请求时的时间戳，Unix时间戳的微秒数格式，如 `1597026383085123`   
返回的时间是请求验证后的时间。  
outTime | String | REST网关发送响应时的时间戳，Unix时间戳的微秒数格式，如 `1597026383085123`  
撤单返回sCode等于0不能严格认为该订单已经被撤销，只表示您的撤单请求被系统服务器所接受，撤单结果以订单频道推送的状态或者查询订单状态为准  

### POST / 批量撤单 

撤销未完成的订单，每次最多可以撤销20个订单。请求参数应该按数组格式传递。

#### 限速：300个/2s

#### 限速规则（期权以外）：User ID + Instrument ID

#### 限速规则（只限期权）：User ID + Instrument Family

#### 权限：交易

与其他限速按接口调用次数不同，该接口限速按订单的总个数限速。如果单次批量请求中只有一个元素，则算在单个`撤单`限速中。 

#### HTTP请求

`POST /api/v5/trade/cancel-batch-orders`

> 请求示例
    
    
    POST /api/v5/trade/cancel-batch-orders
    body
    [
        {
            "instId":"BTC-USDT",
            "ordId":"590908157585625111"
        },
        {
            "instId":"BTC-USDT",
            "ordId":"590908544950571222"
        }
    ]
    
    
    
    
    import okx.Trade as Trade
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # 实盘: 0, 模拟盘: 1
    
    tradeAPI = Trade.TradeAPI(apikey, secretkey, passphrase, False, flag)
    
    # 按ordId撤单
    cancel_orders_with_orderId = [
        {"instId": "BTC-USDT", "ordId": "590908157585625111"},
        {"instId": "BTC-USDT", "ordId": "590908544950571222"}
    ]
    
    result = tradeAPI.cancel_multiple_orders(cancel_orders_with_orderId)
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
instId | String | 是 | 产品ID，如 `BTC-USD-190927`  
ordId | String | 可选 | 订单ID， `ordId`和`clOrdId`必须传一个，若传两个，以`ordId`为主  
clOrdId | String | 可选 | 用户自定义ID  
  
> 返回结果
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
            {
                "clOrdId":"oktswap6",
                "ordId":"12345689",
                "ts":"1695190491421",
                "sCode":"0",
                "sMsg":""
            },
            {
                "clOrdId":"oktswap7",
                "ordId":"12344",
                "ts":"1695190491421",
                "sCode":"0",
                "sMsg":""
            }
        ],
        "inTime": "1695190491421339",
        "outTime": "1695190491423240"
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
code | String | 结果代码，`0`表示成功  
msg | String | 错误信息，代码为0时，该字段为空  
data | Array of objects | 包含结果的对象数组  
> ordId | String | 订单ID  
> clOrdId | String | 客户自定义订单ID  
> ts | String | 系统完成订单请求处理的时间戳，Unix时间戳的毫秒数格式，如 `1597026383085`  
> sCode | String | 事件执行结果的code，0代表成功  
> sMsg | String | 事件执行失败时的msg  
inTime | String | REST网关接收请求时的时间戳，Unix时间戳的微秒数格式，如 `1597026383085123`   
返回的时间是请求验证后的时间。  
outTime | String | REST网关发送响应时的时间戳，Unix时间戳的微秒数格式，如 `1597026383085123`  
  
### POST / 修改订单 

修改当前未成交的挂单  

#### 限速：60次/2s

#### 跟单交易带单员带单产品的限速：4个/2s

#### 限速规则：User ID + Instrument ID

#### 权限：交易

该接口限速同时受到 [子账户限速](/docs-v5/log_zh/#upcoming-changes-sub-account-rate-limit) 及 [基于成交比率的子账户限速](/docs-v5/log_zh/#upcoming-changes-fill-ratio-based-sub-account-rate-limit) 限速规则的影响。

#### HTTP请求

`POST /api/v5/trade/amend-order`

> 请求示例
    
    
    POST /api/v5/trade/amend-order
    body
    {
        "ordId":"590909145319051111",
        "newSz":"2",
        "instId":"BTC-USDT"
    }
    
    
    
    import okx.Trade as Trade
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # 实盘: 0, 模拟盘: 1
    
    tradeAPI = Trade.TradeAPI(apikey, secretkey, passphrase, False, flag)
    
    # 修改订单
    result = tradeAPI.amend_order(
        instId="BTC-USDT",
        ordId="590909145319051111",
        newSz="2"
    )
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
instId | String | 是 | 产品ID  
cxlOnFail | Boolean | 否 | 订单修改失败时是否自动撤单  
有效值：`false` 或 `true`，默认值为 `false`。  
修改失败的场景包括：`newSz` 不是 `lotSz` 的整数倍、超出仓位或风险限额等。`false`（默认）：修改失败时原订单继续保持不变。`true`：修改失败时原订单将自动撤销。  
ordId | String | 可选 | 订单ID  
`ordId`和`clOrdId`必须传一个，若传两个，以`ordId`为主  
clOrdId | String | 可选 | 用户自定义订单ID  
reqId | String | 否 | 用户自定义修改事件ID  
字母（区分大小写）与数字的组合，可以是纯字母、纯数字且长度要在1-32位之间。  
newSz | String | 可选 | 修改后的总目标委托量，必须大于0。这是期望的总委托量，而非剩余未成交量。对于部分成交的订单：如果已成交3张合约，您希望总量为8张，则填写 `newSz=8`（而非5）。系统将尝试成交剩余的5张。`newSz`、`newPx`（或期权的 `newPxUsd`/`newPxVol`）至少需要填写一个。  
newPx | String | 可选 | 修改后的新价格  
修改的新价格期权改单时，newPx/newPxUsd/newPxVol 只能填一个，且必须与下单参数保持一致，如下单用px，改单时需使用newPx  
`newSz` 或 `newPx` 至少需要填写一个。  
speedBump | String | 可选 | 减速带  
`1`：事件合约速度限制（延迟可能因市场情况调整，不提前通知）。对 `EVENTS` 产品的非只挂单操作为必填。  
newPxUsd | String | 可选 | 以USD价格进行期权改单   
仅适用于期权，期权改单时，newPx/newPxUsd/newPxVol 只能填一个  
newPxVol | String | 可选 | 以隐含波动率进行期权改单，如 1 代表 100%   
仅适用于期权，期权改单时，newPx/newPxUsd/newPxVol 只能填一个  
pxAmendType | String | 否 | 订单价格修正类型  
`0`：当`newPx`超出价格限制时，不允许系统修改订单价格  
`1`：当`newPx`超出价格限制时，允许系统将价格修改为限制范围内的最优值  
默认值为`0`  
attachAlgoOrds | Array of objects | 否 | 修改附带止盈止损或移动止盈止损订单信息  
> attachAlgoId | String | 可选 | 附带止盈止损或移动止盈止损的订单ID，由系统生成，改单时必填，用来标识该笔附带止盈止损订单。下附带策略委托单时，该值不会传给 algoId  
> attachAlgoClOrdId | String | 可选 | 下单附带止盈止损或移动止盈止损时，客户自定义的策略订单ID  
> newTpTriggerPx | String | 可选 | 止盈触发价  
如果止盈触发价或者委托价为0，那代表删除止盈。  
> newTpTriggerRatio | String | 可选 | 止盈触发比例，0.3 代表 30%   
仅适用于`交割`/`永续`合约  
`newTpTriggerPx` 和 `newTpTriggerRatio` 只能传入其中一个  
如果主单为买入订单，必须大于 0，如果主单为卖出订单，必须处于 -1 和 0 之间。0 代表删除止盈。  
> newTpOrdPx | String | 可选 | 止盈委托价  
委托价格为-1时，执行市价止盈。  
> newTpOrdKind | String | 否 | 止盈订单类型  
`condition`: 条件单  
`limit`: 限价单  
> newSlTriggerPx | String | 可选 | 止损触发价  
如果止损触发价或者委托价为0，那代表删除止损。  
> newSlTriggerRatio | String | 可选 | 止损触发比例，0.3 代表 30%   
仅适用于`交割`/`永续`合约  
`newSlTriggerPx` 和 `newSlTriggerRatio` 只能传入其中一个  
如果主单为买入订单，必须处于 0 和 1 之间，如果主单为卖出订单，必须大于 0。0 代表删除止损。  
> newSlOrdPx | String | 可选 | 止损委托价  
委托价格为-1时，执行市价止损。  
> newTpTriggerPxType | String | 可选 | 止盈触发价类型  
`last`：最新价格  
`index`：指数价格  
`mark`：标记价格  
只适用于`交割`/`永续`  
如果要新增止盈，该参数必填  
> newSlTriggerPxType | String | 可选 | 止损触发价类型  
`last`：最新价格  
`index`：指数价格  
`mark`：标记价格  
只适用于`交割`/`永续`  
如果要新增止损，该参数必填  
> sz | String | 可选 | 新的张数。仅适用于“多笔止盈”的止盈订单且必填  
> amendPxOnTriggerType | String | 否 | 是否启用开仓价止损，仅适用于分批止盈的止损订单  
`0`：不开启，默认值  
`1`：开启  
> newCallbackRatio | String | 可选 | 新的回调幅度比例，如 `0.05` 代表 5%。  
`newCallbackRatio` 和 `newCallbackSpread` 只能传入其中一个。  
仅适用于 `ordType` = `move_order_stop`  
> newCallbackSpread | String | 可选 | 新的回调幅度价距。  
`newCallbackRatio` 和 `newCallbackSpread` 只能传入其中一个。  
仅适用于 `ordType` = `move_order_stop`  
> newActivePx | String | 否 | 新的激活价格。  
仅适用于 `ordType` = `move_order_stop`  
newSz  
修改的数量<=该笔订单已成交数量时，该订单的状态会修改为完全成交状态。  

> 返回结果
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
            {
             "clOrdId":"",
             "ordId":"12344",
             "ts":"1695190491421",
             "reqId":"b12344",
             "sCode":"0",
             "sMsg":"",
             "subCode": ""
            }
        ],
        "inTime": "1695190491421339",
        "outTime": "1695190491423240"
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
code | String | 结果代码，`0`表示成功  
msg | String | 错误信息，代码为0时，该字段为空  
data | Array of objects | 包含结果的对象数组  
> ordId | String | 订单ID  
> clOrdId | String | 用户自定义ID  
> ts | String | 系统完成订单请求处理的时间戳，Unix时间戳的毫秒数格式，如 `1597026383085`  
> reqId | String | 用户自定义修改事件ID  
> sCode | String | 事件执行结果的code，0代表成功  
> sMsg | String | 事件执行失败时的msg  
> subCode | String | sCode 的子码。  
当 sCode 为 0（请求成功）时，返回 `""`。  
当 sCode 不为 0（请求失败）且存在子码时，返回对应的子码；若无子码，则返回 `""`。  
inTime | String | REST网关接收请求时的时间戳，Unix时间戳的微秒数格式，如 `1597026383085123`   
返回的时间是请求验证后的时间。  
outTime | String | REST网关发送响应时的时间戳，Unix时间戳的微秒数格式，如 `1597026383085123`  
修改订单返回sCode等于0不能严格认为该订单已经被修改，只表示您的修改订单请求被系统服务器所接受，改单结果以订单频道推送的状态或者查询订单状态为准  

### POST / 批量修改订单 

修改未完成的订单，一次最多可批量修改20个订单。请求参数应该按数组格式传递。

#### 限速：300个/2s

#### 跟单交易带单员带单产品的限速：4个/2s

#### 限速规则：User ID + Instrument ID

#### 权限：交易

该接口限速同时受到 [子账户限速](/docs-v5/log_zh/#upcoming-changes-sub-account-rate-limit) 及 [基于成交比率的子账户限速](/docs-v5/log_zh/#upcoming-changes-fill-ratio-based-sub-account-rate-limit) 限速规则的影响。

与其他限速按接口调用次数不同，该接口限速按订单的总个数限速。如果单次批量请求中只有一个元素，则算在单个`修改订单`限速中。 

#### HTTP请求

`POST /api/v5/trade/amend-batch-orders`

> 请求示例
    
    
    POST /api/v5/trade/amend-batch-orders
    body
    [
        {
            "ordId":"590909308792049444",
            "newSz":"2",
            "instId":"BTC-USDT"
        },
        {
            "ordId":"590909308792049555",
            "newSz":"2",
            "instId":"BTC-USDT"
        }
    ]
    
    
    
    import okx.Trade as Trade
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # 实盘: 0, 模拟盘: 1
    
    tradeAPI = Trade.TradeAPI(apikey, secretkey, passphrase, False, flag)
    
    # 按ordId修改未完成的订单
    amend_orders_with_orderId = [
        {"instId": "BTC-USDT", "ordId": "590909308792049444","newSz":"2"},
        {"instId": "BTC-USDT", "ordId": "590909308792049555","newSz":"2"}
    ]
    
    result = tradeAPI.amend_multiple_orders(amend_orders_with_orderId)
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
instId | String | 是 | 产品ID  
cxlOnFail | Boolean | 否 | 订单修改失败时是否自动撤单  
有效值：`false` 或 `true`，默认值为 `false`。  
修改失败的场景包括：`newSz` 不是 `lotSz` 的整数倍、超出仓位或风险限额等。`false`（默认）：修改失败时原订单继续保持不变。`true`：修改失败时原订单将自动撤销。  
ordId | String | 可选 | 订单ID， `ordId`和`clOrdId`必须传一个，若传两个，以`ordId`为主  
clOrdId | String | 可选 | 用户自定义order ID  
reqId | String | 否 | 用户自定义修改事件ID  
字母（区分大小写）与数字的组合，可以是纯字母、纯数字且长度要在1-32位之间。  
newSz | String | 可选 | 修改的新数量，必须大于0，对于部分成交订单，该数量应包含已成交数量。  
newPx | String | 可选 | 修改后的新价格  
修改的新价格期权改单时，newPx/newPxUsd/newPxVol 只能填一个，且必须与下单参数保持一致，如下单用px，改单时需使用newPx  
speedBump | String | 可选 | 减速带  
`1`：事件合约速度限制（延迟可能因市场情况调整，不提前通知）。对 `EVENTS` 产品的非只挂单操作为必填。  
newPxUsd | String | 可选 | 以USD价格进行期权改单   
仅适用于期权，期权改单时，newPx/newPxUsd/newPxVol 只能填一个  
newPxVol | String | 可选 | 以隐含波动率进行期权改单，如 1 代表 100%   
仅适用于期权，期权改单时，newPx/newPxUsd/newPxVol 只能填一个  
pxAmendType | String | 否 | 订单价格修正类型  
`0`：当`newPx`超出价格限制时，不允许系统修改订单价格  
`1`：当`newPx`超出价格限制时，允许系统将价格修改为限制范围内的最优值  
默认值为`0`  
attachAlgoOrds | Array of objects | 否 | 附带止盈止损或移动止盈止损订单信息  
> attachAlgoId | String | 可选 | 附带止盈止损或移动止盈止损的订单ID，由系统生成，改单时必填，用来标识该笔附带止盈止损订单。下附带策略委托单时，该值不会传给 algoId  
> attachAlgoClOrdId | String | 可选 | 下单附带止盈止损或移动止盈止损时，客户自定义的策略订单ID  
> newTpTriggerPx | String | 可选 | 止盈触发价  
如果止盈触发价或者委托价为0，那代表删除止盈。  
> newTpTriggerRatio | String | 可选 | 止盈触发比例，0.3 代表 30%   
仅适用于`交割`/`永续`合约   
`newTpTriggerPx` 和 `newTpTriggerRatio` 只能传入其中一个  
如果主单为买入订单，必须大于 0，如果主单为卖出订单，必须处于 -1 和 0 之间。 0 means to delete the take-profit.  
> newTpOrdPx | String | 可选 | 止盈委托价  
委托价格为-1时，执行市价止盈。  
> newTpOrdKind | String | 否 | 止盈订单类型  
`condition`: 条件单  
`limit`: 限价单  
> newSlTriggerPx | String | 可选 | 止损触发价  
如果止损触发价或者委托价为0，那代表删除止损。  
> newSlTriggerRatio | String | 可选 | 止损触发比例，0.3 代表 30%   
仅适用于`交割`/`永续`合约   
`newSlTriggerPx` 和 `newSlTriggerRatio` 只能传入其中一个  
如果主单为买入订单，必须处于 0 和 1 之间，如果主单为卖出订单，必须大于 0。0 means to delete the stop-loss.  
> newSlOrdPx | String | 可选 | 止损委托价  
委托价格为-1时，执行市价止损。  
> newTpTriggerPxType | String | 可选 | 止盈触发价类型  
`last`：最新价格  
`index`：指数价格  
`mark`：标记价格  
只适用于`交割`/`永续`  
如果要新增止盈，该参数必填  
> newSlTriggerPxType | String | 可选 | 止损触发价类型  
`last`：最新价格  
`index`：指数价格  
`mark`：标记价格  
只适用于`交割`/`永续`  
如果要新增止损，该参数必填  
> sz | String | 可选 | 新的张数。仅适用于“多笔止盈”的止盈订单且必填  
> amendPxOnTriggerType | String | 否 | 是否启用开仓价止损，仅适用于分批止盈的止损订单  
`0`：不开启，默认值   
`1`：开启  
> newCallbackRatio | String | 可选 | 新的回调幅度比例，如 `0.05` 代表 5%。  
`newCallbackRatio` 和 `newCallbackSpread` 只能传入其中一个。  
仅适用于 `ordType` = `move_order_stop`  
> newCallbackSpread | String | 可选 | 新的回调幅度价距。  
`newCallbackRatio` 和 `newCallbackSpread` 只能传入其中一个。  
仅适用于 `ordType` = `move_order_stop`  
> newActivePx | String | 否 | 新的激活价格。  
仅适用于 `ordType` = `move_order_stop`  
newSz  
修改的数量<=该笔订单已成交数量时，该订单的状态会修改为完全成交状态。  

> 返回结果
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
            {
                "clOrdId":"oktswap6",
                "ordId":"12345689",
                "ts":"1695190491421",
                "reqId":"b12344",
                "sCode":"0",
                "sMsg":"",
                "subCode": ""
            },
            {
                "clOrdId":"oktswap7",
                "ordId":"12344",
                "ts":"1695190491421",
                "reqId":"b12344",
                "sCode":"0",
                "sMsg":"",
                "subCode": ""
            }
        ],
        "inTime": "1695190491421339",
        "outTime": "1695190491423240"
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
code | String | 结果代码，`0`表示成功  
msg | String | 错误信息，代码为0时，该字段为空  
data | Array of objects | 包含结果的对象数组  
> ordId | String | 订单ID  
> clOrdId | String | 用户自定义ID  
> ts | String | 系统完成订单请求处理的时间戳，Unix时间戳的毫秒数格式，如 `1597026383085`  
> reqId | String | 用户自定义修改事件ID  
> sCode | String | 事件执行结果的code，0代表成功  
> sMsg | String | 事件执行失败时的msg  
> subCode | String | sCode 的子码。  
当 sCode 为 0（请求成功）时，返回 `""`。  
当 sCode 不为 0（请求失败）且存在子码时，返回对应的子码；若无子码，则返回 `""`。  
inTime | String | REST网关接收请求时的时间戳，Unix时间戳的微秒数格式，如 `1597026383085123`   
返回的时间是请求验证后的时间。  
outTime | String | REST网关发送响应时的时间戳，Unix时间戳的微秒数格式，如 `1597026383085123`  
  
### POST / 市价仓位全平 

市价平掉指定交易产品的持仓

#### 限速：20次/2s

#### 限速规则（期权以外）：User ID + Instrument ID

#### 限速规则（只限期权）：User ID + Instrument Family

#### 权限：交易

#### HTTP请求

`POST /api/v5/trade/close-position`

> 请求示例
    
    
    POST /api/v5/trade/close-position
    body
    {
        "instId":"BTC-USDT-SWAP",
        "mgnMode":"cross"
    }
    
    
    
    import okx.Trade as Trade
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # 实盘: 0, 模拟盘: 1
    
    tradeAPI = Trade.TradeAPI(apikey, secretkey, passphrase, False, flag)
    
    # 市价全平
    result = tradeAPI.close_positions(
        instId="BTC-USDT-SWAP",
        mgnMode="cross"
    )
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
instId | String | 是 | 产品ID  
posSide | String | 可选 | 持仓方向   
买卖模式下：可不填写此参数，默认值net，如果填写，仅可以填写net  
开平仓模式下： 必须填写此参数，且仅可以填写 `long`：平多 ，`short`：平空  
mgnMode | String | 是 | 保证金模式  
`cross`：全仓 ； `isolated`：逐仓  
ccy | String | 可选 | 保证金币种，`合约模式`下的全仓币币杠杆平仓必填  
autoCxl | Boolean | 否 | 当市价全平时，平仓单是否需要自动撤销,默认为false.  
`false`：不自动撤单 `true`：自动撤单  
clOrdId | String | 否 | 客户自定义ID  
字母（区分大小写）与数字的组合，可以是纯字母、纯数字且长度要在1-32位之间。  
tag | String | 否 | 订单标签  
字母（区分大小写）与数字的组合，可以是纯字母、纯数字，且长度在1-16位之间。  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "clOrdId": "",
                "instId": "BTC-USDT-SWAP",
                "posSide": "long",
                "tag": ""
            }
        ],
        "msg": ""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
instId | String | 产品ID  
posSide | String | 持仓方向  
clOrdId | String | 客户自定义ID  
字母（区分大小写）与数字的组合，可以是纯字母、纯数字且长度要在1-32位之间。  
tag | String | 订单标签  
字母（区分大小写）与数字的组合，可以是纯字母、纯数字，且长度在1-16位之间。  
如果不自动撤单，那有任何平仓挂单的情况下，市价全平会返回错误码信息，提示用户先撤销平仓挂单  

### GET / 获取订单信息 

查订单信息

#### 限速：60次/2s

#### 限速规则（期权以外）：User ID + Instrument ID

#### 限速规则（只限期权）：User ID + Instrument Family

#### 权限：读取

#### HTTP请求

`GET /api/v5/trade/order`

> 请求示例
    
    
    GET /api/v5/trade/order?ordId=1753197687182819328&instId=BTC-USDT
    
    
    
    
    import okx.Trade as Trade
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # 实盘: 0, 模拟盘: 1
    
    tradeAPI = Trade.TradeAPI(apikey, secretkey, passphrase, False, flag)
    
    # 通过 ordId 查询订单
    result = tradeAPI.get_order(
        instId="BTC-USDT",
        ordId="680800019749904384"
    )
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
instId | String | 是 | 产品ID，如 `BTC-USDT`  
只适用于交易中的产品  
ordId | String | 可选 | 订单ID，`ordId`和`clOrdId`必须传一个，若传两个，以`ordId`为主  
clOrdId | String | 可选 | 用户自定义ID  
如果`clOrdId`关联了多个订单，只会返回最近的那笔订单  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "accFillSz": "0.00192834",
                "algoClOrdId": "",
                "algoId": "",
                "attachAlgoClOrdId": "",
                "attachAlgoOrds": [],
                "avgPx": "51858",
                "cTime": "1708587373361",
                "cancelSource": "",
                "cancelSourceReason": "",
                "category": "normal",
                "ccy": "",
                "clOrdId": "",
                "fee": "-0.00000192834",
                "feeCcy": "BTC",
                "fillPx": "51858",
                "fillSz": "0.00192834",
                "fillTime": "1708587373361",
                "instId": "BTC-USDT",
                "instType": "SPOT",
                "isTpLimit": "false",
                "lever": "",
                "linkedAlgoOrd": {
                    "algoId": ""
                },
                "ordId": "680800019749904384",
                "ordType": "market",
                "pnl": "0",
                "posSide": "net",
                "px": "",
                "pxType": "",
                "pxUsd": "",
                "pxVol": "",
                "quickMgnType": "",
                "rebate": "0",
                "rebateCcy": "USDT",
                "reduceOnly": "false",
                "side": "buy",
                "slOrdPx": "",
                "slTriggerPx": "",
                "slTriggerPxType": "",
                "source": "",
                "state": "filled",
                "stpId": "",
                "stpMode": "",
                "sz": "100",
                "tag": "",
                "tdMode": "cash",
                "tgtCcy": "quote_ccy",
                "tpOrdPx": "",
                "tpTriggerPx": "",
                "tpTriggerPxType": "",
                "tradeId": "744876980",
                "tradeQuoteCcy": "USDT",
                "uTime": "1708587373362"
            }
        ],
        "msg": ""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
instType | String | 产品类型  
`SPOT`：币币  
`MARGIN`：币币杠杆  
`SWAP`：永续合约  
`FUTURES`：交割合约  
`OPTION`：期权  
`EVENTS`：事件合约  
instId | String | 产品ID  
tgtCcy | String | 币币市价单委托数量`sz`的单位  
`base_ccy`: 交易货币 ；`quote_ccy`：计价货币  
仅适用于`币币`市价订单  
默认买单为`quote_ccy`，卖单为`base_ccy`  
ccy | String | 保证金币种，适用于`逐仓杠杆`及`合约模式`下的`全仓杠杆`订单以及交割、永续和期权合约订单。  
ordId | String | 订单ID  
clOrdId | String | 客户自定义订单ID  
tag | String | 订单标签  
px | String | 委托价格，对于期权，以币(如BTC, ETH)为单位  
pxUsd | String | 期权价格，以USD为单位   
仅适用于期权，其他业务线返回空字符串""  
pxVol | String | 期权订单的隐含波动率   
仅适用于期权，其他业务线返回空字符串""  
pxType | String | 期权的价格类型   
`px`：代表按价格下单，单位为币 (请求参数 px 的数值单位是BTC或ETH)   
`pxVol`：代表按pxVol下单   
`pxUsd`：代表按照pxUsd下单，单位为USD (请求参数px 的数值单位是USD)  
sz | String | 委托数量  
pnl | String | 收益(不包括手续费)  
适用于有成交的平仓订单，其他情况均为0  
ordType | String | 订单类型   
`market`：市价单  
`limit`：限价单   
`post_only`：只做maker单   
`fok`：全部成交或立即取消   
`ioc`：立即成交并取消剩余   
`optimal_limit_ioc`：市价委托立即成交并取消剩余（仅适用交割、永续）  
`mmp`：做市商保护(仅适用于组合保证金账户模式下的期权订单)  
`mmp_and_post_only`：做市商保护且只做maker单(仅适用于组合保证金账户模式下的期权订单)   
`op_fok`：期权简选（全部成交或立即取消）  
`elp`：流动性增强计划订单  
side | String | 订单方向  
posSide | String | 持仓方向  
tdMode | String | 交易模式  
accFillSz | String | 自下单以来的累计成交数量。在WebSocket订单频道推送中，`accFillSz` 始终表示累计总量，而非本次推送的增量。  
对于`币币`和`杠杆`，单位为交易货币，如 BTC-USDT, 单位为 BTC；  
对于交割、永续以及期权，单位为张。  
fillPx | String | 最新成交价格，如果成交数量为0，该字段为""  
tradeId | String | 最新成交ID  
fillSz | String | 最近一次单笔成交数量（非累计）。累计成交总量请使用 `accFillSz`。  
对于`币币`和`杠杆`，单位为交易货币，如 BTC-USDT, 单位为 BTC；  
对于交割、永续以及期权，单位为张。  
fillTime | String | 最新成交时间  
avgPx | String | 成交均价，如果成交数量为0，该字段也为""  
state | String | 订单状态：  
`live`：已在订单簿中，尚无成交。  
`partially_filled`：部分成交，仍在订单簿中。  
`filled`：完全成交，终态。  
`canceled`：撤单，终态。IOC 订单被撤销时可能存在部分成交，此时 `accFillSz` 不为零。  
`mmp_canceled`：由做市商保护机制自动撤单，终态。  
注意：GET /api/v5/trade/orders-pending 仅返回 `live` 和 `partially_filled`；GET /api/v5/trade/orders-history 返回 `filled`、`canceled` 和 `mmp_canceled`。  
lever | String | 杠杆倍数，0.01到125之间的数值，仅适用于 `币币杠杆/交割/永续`  
attachAlgoClOrdId | String | 下单附带止盈止损或移动止盈止损时，客户自定义的策略订单ID  
tpTriggerPx | String | 止盈触发价  
tpTriggerPxType | String | 止盈触发价类型  
`last`：最新价格  
`index`：指数价格  
`mark`：标记价格  
tpOrdPx | String | 止盈委托价  
slTriggerPx | String | 止损触发价  
slTriggerPxType | String | 止损触发价类型  
`last`：最新价格  
`index`：指数价格  
`mark`：标记价格  
slOrdPx | String | 止损委托价  
attachAlgoOrds | Array of objects | 附带止盈止损或移动止盈止损订单信息  
> attachAlgoId | String | 附带止盈止损或移动止盈止损的订单ID，改单时，可用来标识该笔附带止盈止损订单。下附带策略委托单时，该值不会传给 algoId  
> attachAlgoClOrdId | String | 下单附带止盈止损或移动止盈止损时，客户自定义的策略订单ID  
> tpOrdKind | String | 止盈订单类型  
`condition`: 条件单  
`limit`: 限价单  
> tpTriggerPx | String | 止盈触发价  
> tpTriggerRatio | String | 止盈触发比例，0.3 代表 30%   
仅适用于`交割`/`永续`合约  
> tpTriggerPxType | String | 止盈触发价类型  
`last`：最新价格  
`index`：指数价格  
`mark`：标记价格  
> tpOrdPx | String | 止盈委托价  
> slTriggerPx | String | 止损触发价  
> slTriggerRatio | String | 止损触发比例，0.3 代表 30%   
仅适用于`交割`/`永续`合约  
> slTriggerPxType | String | 止损触发价类型  
`last`：最新价格  
`index`：指数价格  
`mark`：标记价格  
> slOrdPx | String | 止损委托价  
> sz | String | 张数。仅适用于“多笔止盈”的止盈订单  
> amendPxOnTriggerType | String | 是否启用开仓价止损，仅适用于分批止盈的止损订单  
`0`：不开启，默认值   
`1`：开启  
> callbackRatio | String | 回调幅度的比例，如 `0.05` 代表 5%  
> callbackSpread | String | 回调幅度的价距  
> activePx | String | 激活价格  
> failCode | String | 委托失败的错误码，默认为"",  
委托失败时有值，如 51020  
> failReason | String | 委托失败的原因，默认为""  
委托失败时有值  
linkedAlgoOrd | Object | 止损订单信息，仅适用于包含限价止盈单的双向止盈止损订单，触发后生成的普通订单  
> algoId | String | 策略订单唯一标识  
stpId | String | ~~自成交保护ID  
如果自成交保护不适用则返回""~~（已弃用）  
stpMode | String | 自成交保护模式  
feeCcy | String | 手续费币种  
对于币币和杠杆的挂单卖单，表示计价币种；其他情况下，表示收取手续费的币种。  
fee | String | 手续费金额。符号规则：负数表示向平台净支付手续费；正数表示从平台净获得返佣。该净额已包含手续费与返佣的轧差。  
对于币币和杠杆（除挂单卖单外）：平台收取的累计手续费，始终为负数。  
对于币币和杠杆的挂单卖单、交割、永续和期权：累计手续费和返佣（币币和杠杆挂单卖单始终以计价币种计算）。  
如需分开核算，请结合 `feeCcy`+`fee` 与 `rebateCcy`+`rebate` 使用，两者货币种类可能不同。  
rebateCcy | String | 返佣币种  
对于币币和杠杆的挂单卖单，表示交易币种；其他情况下，表示支付返佣的币种。  
rebate | String | 返佣金额，仅适用于币币和杠杆  
对于挂单卖单：以交易币种为单位的~~累计手续费和~~ 返佣金额。  
其他情况下，表示挂单返佣金额，始终为正数，如无返佣则返回""。  
source | String | 订单来源（列表不完整——如遇未知值请做容错处理，后续可能新增类型）：  
`6`：计划委托策略触发后生成的普通单  
`7`：止盈止损策略触发后生成的普通单  
`13`：策略委托单触发后生成的普通单  
`25`：移动止盈止损策略触发后生成的普通单  
`34`：追逐限价委托生成的普通单  
所有值均表示由母策略或算法订单触发生成的系统子单。  
category | String | 订单种类：  
`normal`：用户正常下单。  
`twap`：系统生成的强制还款单（非TWAP算法策略）。  
`adl`：ADL自动减仓，系统触发的仓位削减。  
`full_liquidation`：因保证金不足触发的全仓强制平仓。  
`partial_liquidation`：因保证金不足触发的部分强制平仓。  
`delivery`：期货/期权到期结算执行。  
`ddh`：期权做市商系统触发的Delta动态对冲单。  
`auto_conversion`：系统触发的资产自动转换单。  
reduceOnly | String | 是否只减仓，`true` 或 `false`  
cancelSource | String | 订单取消来源的原因枚举值代码  
cancelSourceReason | String | 订单取消来源的对应具体原因  
quickMgnType | String | ~~一键借币类型，仅适用于杠杆逐仓的一键借币模式  
`manual`：手动，`auto_borrow`：自动借币，`auto_repay`：自动还币~~（已弃用）  
algoClOrdId | String | 客户自定义策略订单ID。策略订单触发，且策略单有`algoClOrdId`时有值，否则为"",  
algoId | String | 策略委托单ID，策略订单触发时有值，否则为""  
isTpLimit | String | 是否为限价止盈，true 或 false.  
uTime | String | 订单状态更新时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
cTime | String | 订单创建时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
tradeQuoteCcy | String | 用于交易的计价币种。  
outcome | String | 用户交易的市场结果方向。  
`yes`  
`no`  
仅适用于 `EVENTS`  
  
### GET / 获取未成交订单列表 

获取当前账户下所有未成交订单信息

#### 限速：60次/2s

#### 限速规则：User ID

#### 权限：读取

#### HTTP请求

`GET /api/v5/trade/orders-pending`

> 请求示例
    
    
    GET /api/v5/trade/orders-pending?ordType=post_only,fok,ioc&instType=SPOT
    
    
    
    
    import okx.Trade as Trade
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # 实盘: 0, 模拟盘: 1
    
    tradeAPI = Trade.TradeAPI(apikey, secretkey, passphrase, False, flag)
    
    # 查询所有未成交订单
    result = tradeAPI.get_order_list(
        instType="SPOT",
        ordType="post_only,fok,ioc"
    )
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
instType | String | 否 | 产品类型  
`SPOT`：币币  
`MARGIN`：币币杠杆  
`SWAP`：永续合约  
`FUTURES`：交割合约  
`OPTION`：期权  
`EVENTS`：事件合约  
instFamily | String | 否 | 交易品种  
适用于`交割`/`永续`/`期权`  
instId | String | 否 | 产品ID，如 `BTC-USDT`  
ordType | String | 否 | 订单类型  
`market`：市价单  
`limit`：限价单  
`post_only`：只做maker单  
`fok`：全部成交或立即取消  
`ioc`：立即成交并取消剩余  
`optimal_limit_ioc`：市价委托立即成交并取消剩余（仅适用交割、永续）  
`mmp`：做市商保护(仅适用于组合保证金账户模式下的期权订单)  
`mmp_and_post_only`：做市商保护且只做maker单(仅适用于组合保证金账户模式下的期权订单)   
`op_fok`：期权简选（全部成交或立即取消）  
`elp`：流动性增强计划订单  
state | String | 否 | 订单状态  
`live`：等待成交  
`partially_filled`：部分成交  
after | String | 否 | 请求此ID之前（更旧的数据）的分页内容，传的值为对应接口的`ordId`  
before | String | 否 | 请求此ID之后（更新的数据）的分页内容，传的值为对应接口的`ordId`  
limit | String | 否 | 返回结果的数量，最大为100，默认100条  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "accFillSz": "0",
                "algoClOrdId": "",
                "algoId": "",
                "attachAlgoClOrdId": "",
                "attachAlgoOrds": [],
                "avgPx": "",
                "cTime": "1724733617998",
                "cancelSource": "",
                "cancelSourceReason": "",
                "category": "normal",
                "ccy": "",
                "clOrdId": "",
                "fee": "0",
                "feeCcy": "BTC",
                "fillPx": "",
                "fillSz": "0",
                "fillTime": "",
                "instId": "BTC-USDT",
                "instType": "SPOT",
                "isTpLimit": "false",
                "lever": "",
                "linkedAlgoOrd": {
                    "algoId": ""
                },
                "ordId": "1752588852617379840",
                "ordType": "post_only",
                "pnl": "0",
                "posSide": "net",
                "px": "13013.5",
                "pxType": "",
                "pxUsd": "",
                "pxVol": "",
                "quickMgnType": "",
                "rebate": "0",
                "rebateCcy": "USDT",
                "reduceOnly": "false",
                "side": "buy",
                "slOrdPx": "",
                "slTriggerPx": "",
                "slTriggerPxType": "",
                "source": "",
                "state": "live",
                "stpId": "",
                "stpMode": "cancel_maker",
                "sz": "0.001",
                "tag": "",
                "tdMode": "cash",
                "tgtCcy": "",
                "tpOrdPx": "",
                "tpTriggerPx": "",
                "tpTriggerPxType": "",
                "tradeId": "",
                ”tradeQuoteCcy“: "USDT",
                "uTime": "1724733617998"
            }
        ],
        "msg": ""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
instType | String | 产品类型  
`SPOT`：币币  
`MARGIN`：币币杠杆  
`SWAP`：永续合约  
`FUTURES`：交割合约  
`OPTION`：期权  
`EVENTS`：事件合约  
instId | String | 产品ID  
tgtCcy | String | 币币市价单委托数量`sz`的单位  
`base_ccy`: 交易货币 ；`quote_ccy`：计价货币  
仅适用于`币币`市价订单  
默认买单为`quote_ccy`，卖单为`base_ccy`  
ccy | String | 保证金币种，适用于`逐仓杠杆`及`合约模式`下的`全仓杠杆`订单以及交割、永续和期权合约订单。  
ordId | String | 订单ID  
clOrdId | String | 客户自定义订单ID  
tag | String | 订单标签  
px | String | 委托价格，对于期权，以币(如BTC, ETH)为单位  
pxUsd | String | 期权价格，以USD为单位   
仅适用于期权，其他业务线返回空字符串""  
pxVol | String | 期权订单的隐含波动率   
仅适用于期权，其他业务线返回空字符串""  
pxType | String | 期权的价格类型   
`px`：代表按价格下单，单位为币 (请求参数 px 的数值单位是BTC或ETH)   
`pxVol`：代表按pxVol下单   
`pxUsd`：代表按照pxUsd下单，单位为USD (请求参数px 的数值单位是USD)  
sz | String | 委托数量  
pnl | String | 收益(不包括手续费)  
适用于有成交的平仓订单，其他情况均为0  
ordType | String | 订单类型  
`market`：市价单  
`limit`：限价单   
`post_only`：只做maker单   
`fok`：全部成交或立即取消   
`ioc`：立即成交并取消剩余   
`optimal_limit_ioc`：市价委托立即成交并取消剩余（仅适用交割、永续）  
`mmp`：做市商保护(仅适用于组合保证金账户模式下的期权订单)  
`mmp_and_post_only`：做市商保护且只做maker单(仅适用于组合保证金账户模式下的期权订单)   
`op_fok`：期权简选（全部成交或立即取消）  
`elp`：流动性增强计划订单  
side | String | 订单方向  
posSide | String | 持仓方向  
tdMode | String | 交易模式  
accFillSz | String | 累计成交数量  
fillPx | String | 最新成交价格。如果还没成交，系统返回""。  
tradeId | String | 最新成交ID  
fillSz | String | 最新成交数量  
fillTime | String | 最新成交时间  
avgPx | String | 成交均价。如果还没成交，系统返回`0`。  
state | String | 订单状态  
`live`：等待成交   
`partially_filled`：部分成交  
  
lever | String | 杠杆倍数，0.01到125之间的数值，仅适用于 `币币杠杆/交割/永续`  
attachAlgoClOrdId | String | 下单附带止盈止损或移动止盈止损时，客户自定义的策略订单ID  
tpTriggerPx | String | 止盈触发价  
tpTriggerPxType | String | 止盈触发价类型  
`last`：最新价格  
`index`：指数价格  
`mark`：标记价格  
slTriggerPx | String | 止损触发价  
slTriggerPxType | String | 止损触发价类型  
`last`：最新价格  
`index`：指数价格  
`mark`：标记价格  
slOrdPx | String | 止损委托价  
tpOrdPx | String | 止盈委托价  
attachAlgoOrds | Array of objects | 附带止盈止损或移动止盈止损订单信息  
> attachAlgoId | String | 附带止盈止损或移动止盈止损的订单ID，改单时，可用来标识该笔附带止盈止损订单。下附带策略委托单时，该值不会传给 algoId  
> attachAlgoClOrdId | String | 下单附带止盈止损或移动止盈止损时，客户自定义的策略订单ID  
> tpOrdKind | String | 止盈订单类型  
`condition`: 条件单  
`limit`: 限价单  
> tpTriggerPx | String | 止盈触发价  
> tpTriggerRatio | String | 止盈触发比例，0.3 代表 30%   
仅适用于`交割`/`永续`合约  
> tpTriggerPxType | String | 止盈触发价类型  
`last`：最新价格  
`index`：指数价格  
`mark`：标记价格  
> tpOrdPx | String | 止盈委托价  
> slTriggerPx | String | 止损触发价  
> slTriggerRatio | String | 止损触发比例，0.3 代表 30%   
仅适用于`交割`/`永续`合约  
> slTriggerPxType | String | 止损触发价类型  
`last`：最新价格  
`index`：指数价格  
`mark`：标记价格  
> slOrdPx | String | 止损委托价  
> sz | String | 张数。仅适用于”多笔止盈”的止盈订单  
> amendPxOnTriggerType | String | 是否启用开仓价止损，仅适用于分批止盈的止损订单  
`0`：不开启，默认值   
`1`：开启  
> callbackRatio | String | 回调幅度的比例，如 `0.05` 代表 5%  
> callbackSpread | String | 回调幅度的价距  
> activePx | String | 激活价格  
> failCode | String | 委托失败的错误码，默认为””,  
委托失败时有值，如 51020  
> failReason | String | 委托失败的原因，默认为””  
委托失败时有值  
linkedAlgoOrd | Object | 止损订单信息，仅适用于包含限价止盈单的双向止盈止损订单，触发后生成的普通订单  
> algoId | String | 策略订单唯一标识  
stpId | String | ~~自成交保护ID  
如果自成交保护不适用则返回""~~（已弃用）  
stpMode | String | 自成交保护模式  
feeCcy | String | 手续费币种  
对于币币和杠杆的挂单卖单，表示计价币种；其他情况下，表示收取手续费的币种。  
fee | String | 手续费金额  
对于币币和杠杆（除挂单卖单外）：平台收取的累计手续费，始终为负数。  
对于币币和杠杆的挂单卖单、交割、永续和期权：累计手续费和返佣（币币和杠杆挂单卖单始终以计价币种计算）。  
rebateCcy | String | 返佣币种  
对于币币和杠杆的挂单卖单，表示交易币种；其他情况下，表示支付返佣的币种。  
rebate | String | 返佣金额，仅适用于币币和杠杆  
对于挂单卖单：以交易币种为单位的~~累计手续费和~~ 返佣金额。  
其他情况下，表示挂单返佣金额，始终为正数，如无返佣则返回""。  
source | String | 订单来源  
`6`：计划委托策略触发后的生成的普通单  
`7`：止盈止损策略触发后的生成的普通单  
`13`：策略委托单触发后的生成的普通单  
`25`：移动止盈止损策略触发后的生成的普通单  
`34`: 追逐限价委托生成的普通单  
category | String | 订单种类   
`normal`：普通委托  
`twap`：TWAP自动换币  
`adl`：ADL自动减仓  
`full_liquidation`：强制平仓  
`partial_liquidation`：强制减仓  
`delivery`：交割  
`ddh`：对冲减仓类型订单  
`auto_conversion`：抵押借币自动还币订单  
reduceOnly | String | 是否只减仓，`true` 或 `false`  
quickMgnType | String | ~~一键借币类型，仅适用于杠杆逐仓的一键借币模式  
`manual`：手动，`auto_borrow`：自动借币，`auto_repay`：自动还币~~（已弃用）  
algoClOrdId | String | 客户自定义策略订单ID。策略订单触发，且策略单有`algoClOrdId`是有值，否则为"",  
algoId | String | 策略委托单ID，策略订单触发时有值，否则为""  
isTpLimit | String | 是否为限价止盈，true 或 false.  
uTime | String | 订单状态更新时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
cTime | String | 订单创建时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
cancelSource | String | 订单取消来源的原因枚举值代码  
cancelSourceReason | String | 订单取消来源的对应具体原因  
tradeQuoteCcy | String | 用于交易的计价币种。  
outcome | String | 用户交易的市场结果方向。  
`yes`  
`no`  
仅适用于 `EVENTS`  
  
### GET / 获取历史订单记录（近七天）

获取最近7天挂单，且完成的订单数据，包括7天以前挂单，但近7天才成交的订单数据。按照订单创建时间倒序排序。  

已经撤销的未成交单 只保留2小时

#### 限速：40次/2s

#### 限速规则：User ID

#### 权限：读取

#### HTTP请求

`GET /api/v5/trade/orders-history`

> 请求示例
    
    
    GET /api/v5/trade/orders-history?ordType=post_only,fok,ioc&instType=SPOT
    
    
    
    
    import okx.Trade as Trade
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # 实盘: 0, 模拟盘: 1
    
    tradeAPI = Trade.TradeAPI(apikey, secretkey, passphrase, False, flag)
    
    # 查询币币历史订单（7天内）
    # 已经撤销的未成交单 只保留2小时
    result = tradeAPI.get_orders_history(
        instType="SPOT",
        ordType="post_only,fok,ioc"
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
instFamily | String | 否 | 交易品种  
适用于`交割`/`永续`/`期权`  
instId | String | 否 | 产品ID，如`BTC-USD-190927`  
ordType | String | 否 | 订单类型   
`market`：市价单  
`limit`：限价单   
`post_only`：只做maker单   
`fok`：全部成交或立即取消   
`ioc`：立即成交并取消剩余  
`optimal_limit_ioc`：市价委托立即成交并取消剩余（仅适用交割、永续）  
`mmp`：做市商保护(仅适用于组合保证金账户模式下的期权订单)  
`mmp_and_post_only`：做市商保护且只做maker单(仅适用于组合保证金账户模式下的期权订单)   
`op_fok`：期权简选（全部成交或立即取消）  
`elp`：流动性增强计划订单  
state | String | 否 | 订单状态  
`canceled`：撤单成功   
`filled`：完全成交  
`mmp_canceled`：做市商保护机制导致的自动撤单  
category | String | 否 | 订单种类   
`twap`：TWAP自动换币   
`adl`：ADL自动减仓  
`full_liquidation`：强制平仓  
`partial_liquidation`：强制减仓   
`delivery`：交割  
`ddh`：对冲减仓类型订单  
after | String | 否 | 请求此ID之前（更旧的数据）的分页内容，传的值为对应接口的`ordId`  
before | String | 否 | 请求此ID之后（更新的数据）的分页内容，传的值为对应接口的`ordId`  
begin | String | 否 | 筛选的开始时间戳 `cTime`，Unix 时间戳为毫秒数格式，如 1597026383085  
end | String | 否 | 筛选的结束时间戳 `cTime`，Unix 时间戳为毫秒数格式，如 1597027383085  
limit | String | 否 | 返回结果的数量，最大为100，默认100条  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "accFillSz": "0.00192834",
                "algoClOrdId": "",
                "algoId": "",
                "attachAlgoClOrdId": "",
                "attachAlgoOrds": [],
                "avgPx": "51858",
                "cTime": "1708587373361",
                "cancelSource": "",
                "cancelSourceReason": "",
                "category": "normal",
                "ccy": "",
                "clOrdId": "",
                "fee": "-0.00000192834",
                "feeCcy": "BTC",
                "fillPx": "51858",
                "fillSz": "0.00192834",
                "fillTime": "1708587373361",
                "instId": "BTC-USDT",
                "instType": "SPOT",
                "isTpLimit": "false",
                "lever": "",
                "ordId": "680800019749904384",
                "ordType": "market",
                "pnl": "0",
                "posSide": "",
                "px": "",
                "pxType": "",
                "pxUsd": "",
                "pxVol": "",
                "quickMgnType": "",
                "rebate": "0",
                "rebateCcy": "USDT",
                "reduceOnly": "false",
                "side": "buy",
                "slOrdPx": "",
                "slTriggerPx": "",
                "slTriggerPxType": "",
                "source": "",
                "state": "filled",
                "stpId": "",
                "stpMode": "",
                "sz": "100",
                "tag": "",
                "tdMode": "cash",
                "tgtCcy": "quote_ccy",
                "tpOrdPx": "",
                "tpTriggerPx": "",
                "tpTriggerPxType": "",
                "tradeId": "744876980",
                ”tradeQuoteCcy“: "USDT",
                "uTime": "1708587373362",
                "linkedAlgoOrd": {
                    "algoId": ""
                }
            }
        ],
        "msg": ""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
instType | String | 产品类型  
`SPOT`：币币  
`MARGIN`：币币杠杆  
`SWAP`：永续合约  
`FUTURES`：交割合约  
`OPTION`：期权  
`EVENTS`：事件合约  
instId | String | 产品ID  
tgtCcy | String | 币币市价单委托数量`sz`的单位  
`base_ccy`: 交易货币 ；`quote_ccy`：计价货币  
仅适用于`币币`市价订单  
默认买单为`quote_ccy`，卖单为`base_ccy`  
ccy | String | 保证金币种，适用于`逐仓杠杆`及`合约模式`下的`全仓杠杆`订单以及交割、永续和期权合约订单。  
ordId | String | 订单ID  
clOrdId | String | 客户自定义订单ID  
tag | String | 订单标签  
px | String | 委托价格，对于期权，以币(如BTC, ETH)为单位  
pxUsd | String | 期权价格，以USD为单位   
仅适用于期权，其他业务线返回空字符串""  
pxVol | String | 期权订单的隐含波动率   
仅适用于期权，其他业务线返回空字符串""  
pxType | String | 期权的价格类型   
`px`：代表按价格下单，单位为币 (请求参数 px 的数值单位是BTC或ETH)   
`pxVol`：代表按pxVol下单   
`pxUsd`：代表按照pxUsd下单，单位为USD (请求参数px 的数值单位是USD)  
sz | String | 委托数量  
ordType | String | 订单类型  
`market`：市价单  
`limit`：限价单   
`post_only`：只做maker单  
`fok`：全部成交或立即取消  
`ioc`：立即成交并取消剩余  
`optimal_limit_ioc`：市价委托立即成交并取消剩余（仅适用交割、永续）  
`mmp`：做市商保护(仅适用于组合保证金账户模式下的期权订单)  
`mmp_and_post_only`：做市商保护且只做maker单(仅适用于组合保证金账户模式下的期权订单)   
`op_fok`：期权简选（全部成交或立即取消）  
`elp`：流动性增强计划订单  
side | String | 订单方向  
posSide | String | 持仓方向  
tdMode | String | 交易模式  
accFillSz | String | 累计成交数量  
fillPx | String | 最新成交价格，如果成交数量为0，该字段为""  
tradeId | String | 最新成交ID  
fillSz | String | 最新成交数量  
fillTime | String | 最新成交时间  
avgPx | String | 成交均价，如果成交数量为0，该字段也为""  
state | String | 订单状态  
`canceled`：撤单成功   
`filled`：完全成交  
`mmp_canceled`：做市商保护机制导致的自动撤单  
lever | String | 杠杆倍数，0.01到125之间的数值，仅适用于 `币币杠杆/交割/永续`  
attachAlgoClOrdId | String | 下单附带止盈止损或移动止盈止损时，客户自定义的策略订单ID  
tpTriggerPx | String | 止盈触发价  
tpTriggerPxType | String | 止盈触发价类型  
`last`：最新价格  
`index`：指数价格  
`mark`：标记价格  
tpOrdPx | String | 止盈委托价  
slTriggerPx | String | 止损触发价  
slTriggerPxType | String | 止损触发价类型  
`last`：最新价格  
`index`：指数价格  
`mark`：标记价格  
slOrdPx | String | 止损委托价  
attachAlgoOrds | Array of objects | 附带止盈止损或移动止盈止损订单信息  
> attachAlgoId | String | 附带止盈止损或移动止盈止损的订单ID，改单时，可用来标识该笔附带止盈止损订单。下附带策略委托单时，该值不会传给 algoId  
> attachAlgoClOrdId | String | 下单附带止盈止损或移动止盈止损时，客户自定义的策略订单ID  
> tpOrdKind | String | 止盈订单类型  
`condition`: 条件单  
`limit`: 限价单  
> tpTriggerPx | String | 止盈触发价  
> tpTriggerRatio | String | 止盈触发比例，0.3 代表 30%   
仅适用于`交割`/`永续`合约  
> tpTriggerPxType | String | 止盈触发价类型  
`last`：最新价格  
`index`：指数价格  
`mark`：标记价格  
> tpOrdPx | String | 止盈委托价  
> slTriggerPx | String | 止损触发价  
> slTriggerRatio | String | 止损触发比例，0.3 代表 30%   
仅适用于`交割`/`永续`合约  
> slTriggerPxType | String | 止损触发价类型  
`last`：最新价格  
`index`：指数价格  
`mark`：标记价格  
> slOrdPx | String | 止损委托价  
> sz | String | 张数。仅适用于“多笔止盈”的止盈订单  
> amendPxOnTriggerType | String | 是否启用开仓价止损，仅适用于分批止盈的止损订单  
`0`：不开启，默认值   
`1`：开启  
> callbackRatio | String | 回调幅度的比例，如 `0.05` 代表 5%  
> callbackSpread | String | 回调幅度的价距  
> activePx | String | 激活价格  
> failCode | String | 委托失败的错误码，默认为"",  
委托失败时有值，如 51020  
> failReason | String | 委托失败的原因，默认为""  
委托失败时有值  
linkedAlgoOrd | Object | 止损订单信息，仅适用于包含限价止盈单的双向止盈止损订单，触发后生成的普通订单  
> algoId | String | 策略订单唯一标识  
stpId | String | ~~自成交保护ID  
如果自成交保护不适用则返回""~~（已弃用）  
stpMode | String | 自成交保护模式  
feeCcy | String | 手续费币种  
对于币币和杠杆的挂单卖单，表示计价币种；其他情况下，表示收取手续费的币种。  
fee | String | 手续费金额  
对于币币和杠杆（除挂单卖单外）：平台收取的累计手续费，始终为负数。  
对于币币和杠杆的挂单卖单、交割、永续和期权：累计手续费和返佣（币币和杠杆挂单卖单始终以计价币种计算）。  
rebateCcy | String | 返佣币种  
对于币币和杠杆的挂单卖单，表示交易币种；其他情况下，表示支付返佣的币种。  
rebate | String | 返佣金额，仅适用于币币和杠杆  
对于挂单卖单：以交易币种为单位的~~累计手续费和~~ 返佣金额。  
其他情况下，表示挂单返佣金额，始终为正数，如无返佣则返回""。  
source | String | 订单来源  
`6`：计划委托策略触发后的生成的普通单  
`7`：止盈止损策略触发后的生成的普通单  
`13`：策略委托单触发后的生成的普通单  
`25`：移动止盈止损策略触发后的生成的普通单  
`34`: 追逐限价委托生成的普通单  
pnl | String | 收益(不包括手续费)  
适用于有成交的平仓订单，其他情况均为0  
category | String | 订单种类   
`normal`：普通委托  
`twap`：TWAP自动换币  
`adl`：ADL自动减仓  
`full_liquidation`：强制平仓  
`partial_liquidation`：强制减仓  
`delivery`：交割  
`ddh`：对冲减仓类型订单  
`auto_conversion`：抵押借币自动还币订单  
reduceOnly | String | 是否只减仓，`true` 或 `false`  
cancelSource | String | 订单取消来源的原因枚举值代码  
cancelSourceReason | String | 订单取消来源的对应具体原因  
algoClOrdId | String | 客户自定义策略订单ID。策略订单触发，且策略单有`algoClOrdId`时有值，否则为"",  
algoId | String | 策略委托单ID，策略订单触发时有值，否则为""  
isTpLimit | String | 是否为限价止盈，true 或 false.  
uTime | String | 订单状态更新时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
cTime | String | 订单创建时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
quickMgnType | String | ~~一键借币类型，仅适用于杠杆逐仓的一键借币模式  
`manual`：手动，`auto_borrow`：自动借币，`auto_repay`：自动还币~~（已弃用）  
tradeQuoteCcy | String | 用于交易的计价币种。  
outcome | String | 用户交易的市场结果方向。  
`yes`  
`no`  
仅适用于 `EVENTS`  
  
### GET / 获取历史订单记录（近三个月）

获取最近3个月挂单，且完成的订单数据，包括3个月以前挂单，但近3个月才成交的订单数据。按照订单创建时间倒序排序。

#### 限速：20次/2s

#### 限速规则：User ID

#### 权限：读取

#### HTTP请求

`GET /api/v5/trade/orders-history-archive`

> 请求示例
    
    
    GET /api/v5/trade/orders-history-archive?ordType=post_only,fok,ioc&instType=SPOT
    
    
    
    
    import okx.Trade as Trade
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # 实盘: 0, 模拟盘: 1
    
    tradeAPI = Trade.TradeAPI(apikey, secretkey, passphrase, False, flag)
    
    # 查询币币历史订单（3月内）
    result = tradeAPI.get_orders_history_archive(
        instType="SPOT",
        ordType="post_only,fok,ioc"
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
instFamily | String | 否 | 交易品种  
适用于`交割`/`永续`/`期权`  
instId | String | 否 | 产品ID，如 `BTC-USDT`  
ordType | String | 否 | 订单类型  
`market`：市价单  
`limit`：限价单   
`post_only`：只做maker单   
`fok`：全部成交或立即取消  
`ioc`：立即成交并取消剩余  
`optimal_limit_ioc`：市价委托立即成交并取消剩余（仅适用交割、永续）  
`mmp`：做市商保护(仅适用于组合保证金账户模式下的期权订单)  
`mmp_and_post_only`：做市商保护且只做maker单(仅适用于组合保证金账户模式下的期权订单)   
`op_fok`：期权简选（全部成交或立即取消）  
`elp`：流动性增强计划订单  
state | String | 否 | 订单状态  
`canceled`：撤单成功   
`filled`：完全成交  
`mmp_canceled`：做市商保护机制导致的自动撤单  
category | String | 否 | 订单种类  
`twap`：TWAP自动换币   
`adl`：ADL自动减仓  
`full_liquidation`：强制平仓  
`partial_liquidation`：强制减仓  
`delivery`：交割  
`ddh`：对冲减仓类型订单  
after | String | 否 | 请求此ID之前（更旧的数据）的分页内容，传的值为对应接口的`ordId`  
before | String | 否 | 请求此ID之后（更新的数据）的分页内容，传的值为对应接口的`ordId`  
begin | String | 否 | 筛选的开始时间戳 `cTime`，Unix 时间戳为毫秒数格式，如 `1597026383085`  
end | String | 否 | 筛选的结束时间戳 `cTime`，Unix 时间戳为毫秒数格式，如 `1597027383085`  
limit | String | 否 | 返回结果的数量，最大为100，默认100条  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "accFillSz": "0.00192834",
                "algoClOrdId": "",
                "algoId": "",
                "attachAlgoClOrdId": "",
                "attachAlgoOrds": [],
                "avgPx": "51858",
                "cTime": "1708587373361",
                "cancelSource": "",
                "cancelSourceReason": "",
                "category": "normal",
                "ccy": "",
                "clOrdId": "",
                "fee": "-0.00000192834",
                "feeCcy": "BTC",
                "fillPx": "51858",
                "fillSz": "0.00192834",
                "fillTime": "1708587373361",
                "instId": "BTC-USDT",
                "instType": "SPOT",
                "isTpLimit": "false",
                "lever": "",
                "ordId": "680800019749904384",
                "ordType": "market",
                "pnl": "0",
                "posSide": "",
                "px": "",
                "pxType": "",
                "pxUsd": "",
                "pxVol": "",
                "quickMgnType": "",
                "rebate": "0",
                "rebateCcy": "USDT",
                "reduceOnly": "false",
                "side": "buy",
                "slOrdPx": "",
                "slTriggerPx": "",
                "slTriggerPxType": "",
                "source": "",
                "state": "filled",
                "stpId": "",
                "stpMode": "",
                "sz": "100",
                "tag": "",
                "tdMode": "cash",
                "tgtCcy": "quote_ccy",
                "tpOrdPx": "",
                "tpTriggerPx": "",
                "tpTriggerPxType": "",
                "tradeId": "744876980",
                ”tradeQuoteCcy“: "USDT",
                "uTime": "1708587373362",
                "linkedAlgoOrd": {
                    "algoId": ""
                }
            }
        ],
        "msg": ""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
instType | String | 产品类型  
`SPOT`：币币  
`MARGIN`：币币杠杆  
`SWAP`：永续合约  
`FUTURES`：交割合约  
`OPTION`：期权  
`EVENTS`：事件合约  
instId | String | 产品ID  
tgtCcy | String | 币币市价单委托数量`sz`的单位  
`base_ccy`: 交易货币 ；`quote_ccy`：计价货币  
仅适用于`币币`市价订单  
默认买单为`quote_ccy`，卖单为`base_ccy`  
ccy | String | 保证金币种，适用于`逐仓杠杆`及`合约模式`下的`全仓杠杆`订单以及交割、永续和期权合约订单。  
ordId | String | 订单ID  
clOrdId | String | 客户自定义订单ID  
tag | String | 订单标签  
px | String | 委托价格，对于期权，以币(如BTC, ETH)为单位  
pxUsd | String | 期权价格，以USD为单位   
仅适用于期权，其他业务线返回空字符串""  
pxVol | String | 期权订单的隐含波动率   
仅适用于期权，其他业务线返回空字符串""  
pxType | String | 期权的价格类型   
`px`：代表按价格下单，单位为币 (请求参数 px 的数值单位是BTC或ETH)   
`pxVol`：代表按pxVol下单   
`pxUsd`：代表按照pxUsd下单，单位为USD (请求参数px 的数值单位是USD)  
sz | String | 委托数量  
ordType | String | 订单类型   
`market`：市价单  
`limit`：限价单   
`post_only`：只做maker单   
`fok`：全部成交或立即取消   
`ioc`：立即成交并取消剩余   
`optimal_limit_ioc`：市价委托立即成交并取消剩余（仅适用交割、永续）  
`mmp`：做市商保护(仅适用于组合保证金账户模式下的期权订单)  
`mmp_and_post_only`：做市商保护且只做maker单(仅适用于组合保证金账户模式下的期权订单)   
`op_fok`：期权简选（全部成交或立即取消）  
`elp`：流动性增强计划订单  
side | String | 订单方向  
posSide | String | 持仓方向  
tdMode | String | 交易模式  
accFillSz | String | 累计成交数量  
fillPx | String | 最新成交价格，如果成交数量为0，该字段为""  
tradeId | String | 最新成交ID  
fillSz | String | 最新成交数量  
fillTime | String | 最新成交时间  
avgPx | String | 成交均价，如果成交数量为0，该字段也为""  
state | String | 订单状态   
`canceled`：撤单成功   
`filled`：完全成交  
`mmp_canceled`：做市商保护机制导致的自动撤单  
lever | String | 杠杆倍数，0.01到125之间的数值，仅适用于 `币币杠杆/交割/永续`  
attachAlgoClOrdId | String | 下单附带止盈止损或移动止盈止损时，客户自定义的策略订单ID  
tpTriggerPx | String | 止盈触发价  
tpTriggerPxType | String | 止盈触发价类型  
`last`：最新价格  
`index`：指数价格  
`mark`：标记价格  
tpOrdPx | String | 止盈委托价  
slTriggerPx | String | 止损触发价  
slTriggerPxType | String | 止损触发价类型  
`last`：最新价格  
`index`：指数价格  
`mark`：标记价格  
slOrdPx | String | 止损委托价  
stpId | String | ~~自成交保护ID  
如果自成交保护不适用则返回""~~（已弃用）  
attachAlgoOrds | Array of objects | 附带止盈止损或移动止盈止损订单信息  
> attachAlgoId | String | 附带止盈止损或移动止盈止损的订单ID，改单时，可用来标识该笔附带止盈止损订单。下附带策略委托单时，该值不会传给 algoId  
> attachAlgoClOrdId | String | 下单附带止盈止损或移动止盈止损时，客户自定义的策略订单ID  
> tpOrdKind | String | 止盈订单类型  
`condition`: 条件单  
`limit`: 限价单  
> tpTriggerPx | String | 止盈触发价  
> tpTriggerRatio | String | 止盈触发比例，0.3 代表 30%   
仅适用于`交割`/`永续`合约  
> tpTriggerPxType | String | 止盈触发价类型  
`last`：最新价格  
`index`：指数价格  
`mark`：标记价格  
> tpOrdPx | String | 止盈委托价  
> slTriggerPx | String | 止损触发价  
> slTriggerRatio | String | 止损触发比例，0.3 代表 30%   
仅适用于`交割`/`永续`合约  
> slTriggerPxType | String | 止损触发价类型  
`last`：最新价格  
`index`：指数价格  
`mark`：标记价格  
> slOrdPx | String | 止损委托价  
> sz | String | 张数。仅适用于“多笔止盈”的止盈订单  
> amendPxOnTriggerType | String | 是否启用开仓价止损，仅适用于分批止盈的止损订单  
`0`：不开启，默认值   
`1`：开启  
> callbackRatio | String | 回调幅度的比例，如 `0.05` 代表 5%  
> callbackSpread | String | 回调幅度的价距  
> activePx | String | 激活价格  
> failCode | String | 委托失败的错误码，默认为"",  
委托失败时有值，如 51020  
> failReason | String | 委托失败的原因，默认为""  
委托失败时有值  
linkedAlgoOrd | Object | 止损订单信息，仅适用于包含限价止盈单的双向止盈止损订单，触发后生成的普通订单  
> algoId | String | 策略订单唯一标识  
stpMode | String | 自成交保护模式  
feeCcy | String | 手续费币种  
对于币币和杠杆的挂单卖单，表示计价币种；其他情况下，表示收取手续费的币种。  
fee | String | 手续费金额  
对于币币和杠杆（除挂单卖单外）：平台收取的累计手续费，始终为负数。  
对于币币和杠杆的挂单卖单、交割、永续和期权：累计手续费和返佣（币币和杠杆挂单卖单始终以计价币种计算）。  
rebateCcy | String | 返佣币种  
对于币币和杠杆的挂单卖单，表示交易币种；其他情况下，表示支付返佣的币种。  
rebate | String | 返佣金额，仅适用于币币和杠杆  
对于挂单卖单：以交易币种为单位的~~累计手续费和~~ 返佣金额。  
其他情况下，表示挂单返佣金额，始终为正数，如无返佣则返回""。  
pnl | String | 收益(不包括手续费)  
适用于有成交的平仓订单，其他情况均为0  
source | String | 订单来源  
`6`：计划委托策略触发后的生成的普通单  
`7`：止盈止损策略触发后的生成的普通单  
`13`：策略委托单触发后的生成的普通单  
`25`：移动止盈止损策略触发后的生成的普通单  
`34`: 追逐限价委托生成的普通单  
category | String | 订单种类  
`normal`：普通委托  
`twap`：TWAP自动换币   
`adl`：ADL自动减仓  
`full_liquidation`：强制平仓  
`partial_liquidation`：强制减仓   
`delivery`：交割  
`ddh`：对冲减仓类型订单  
`auto_conversion`：抵押借币自动还币订单  
reduceOnly | String | 是否只减仓，`true` 或 `false`  
cancelSource | String | 订单取消来源的原因枚举值代码  
cancelSourceReason | String | 订单取消来源的对应具体原因  
algoClOrdId | String | 客户自定义策略订单ID。策略订单触发，且策略单有`algoClOrdId`是有值，否则为"",  
algoId | String | 策略委托单ID，策略订单触发时有值，否则为""  
isTpLimit | String | 是否为限价止盈，true 或 false.  
uTime | String | 订单状态更新时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
cTime | String | 订单创建时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
quickMgnType | String | ~~一键借币类型，仅适用于杠杆逐仓的一键借币模式  
`manual`：手动，`auto_borrow`：自动借币，`auto_repay`：自动还币~~（已弃用）  
tradeQuoteCcy | String | 用于交易的计价币种。  
outcome | String | 用户交易的市场结果方向。  
`yes`  
`no`  
仅适用于 `EVENTS`  
该接口不包含`已撤销的完全无成交`类型订单数据，可通过`获取历史订单记录（近七天)`接口获取。  
对于已完成的期权订单，如果是px订单，pxVol 和 pxUsd 会实时更新，如果是 pxUsd 订单，pxVol 会实时更新，如果是pxVol 订单，pxUsd 会实时更新。 

### GET / 获取成交明细（近三天） 

获取近3天的订单成交明细信息

#### 限速：60次/2s

#### 限速规则：User ID

#### 权限：读取

#### HTTP 请求

`GET /api/v5/trade/fills`

> 请求示例
    
    
    GET /api/v5/trade/fills
    
    
    
    
    import okx.Trade as Trade
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # 实盘: 0, 模拟盘: 1
    
    tradeAPI = Trade.TradeAPI(apikey, secretkey, passphrase, False, flag)
    
    # 获取成交明细
    result = tradeAPI.get_fills()
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
instType | String | 否 | 产品类型  
`SPOT`：币币  
`MARGIN`：币币杠杆  
`SWAP`：永续合约  
`FUTURES`：交割合约  
`OPTION`：期权  
`EVENTS`：事件合约  
instFamily | String | 否 | 交易品种  
适用于`交割`/`永续`/`期权`  
instId | String | 否 | 产品 ID，如`BTC-USDT`  
ordId | String | 否 | 订单 ID  
subType | String | 否 | 成交类型   
`1`：买入  
`2`：卖出   
`3`：开多   
`4`：开空   
`5`：平多   
`6`：平空   
`100`：强减平多   
`101`：强减平空   
`102`：强减买入   
`103`：强减卖出   
`104`：强平平多   
`105`：强平平空   
`106`：强平买入   
`107`：强平卖出   
`110`：强平换币转入   
`111`：强平换币转出   
`118`：系统换币转入   
`119`：系统换币转出   
`112`：交割平多   
`113`：交割平空   
`125`：自动减仓平多   
`126`：自动减仓平空   
`127`：自动减仓买入   
`128`：自动减仓卖出   
`212`：一键借币的自动借币   
`213`：一键借币的自动还币   
`204`：大宗交易买   
`205`：大宗交易卖   
`206`：大宗交易开多   
`207`：大宗交易开空   
`208`：大宗交易平多   
`209`：大宗交易平空  
`236`：小额兑换买入  
`237`：小额兑换卖出  
`270`：价差交易买  
`271`：价差交易卖  
`272`：价差交易开多  
`273`：价差交易开空  
`274`：价差交易平多  
`275`：价差交易平空  
`324`：移仓买入  
`325`：移仓卖出  
`326`：移仓开多  
`327`：移仓开空  
`328`：移仓平多  
`329`：移仓平空  
`376`：质押借币超限买入  
`377`： 质押借币超限卖出  
`410`：买入yes  
`411`：买入no  
`412`：卖出yes  
`413`：卖出no  
`414`：yes结算  
`415`：no结算  
after | String | 否 | 请求此 ID 之前（更旧的数据）的分页内容，传的值为对应接口的`billId`  
before | String | 否 | 请求此 ID 之后（更新的数据）的分页内容，传的值为对应接口的`billId`  
begin | String | 否 | 筛选的开始时间戳 `ts`，Unix 时间戳为毫秒数格式，如 `1597026383085`  
end | String | 否 | 筛选的结束时间戳 `ts`，Unix 时间戳为毫秒数格式，如 `1597027383085`  
limit | String | 否 | 返回结果的数量，最大为100，默认100条  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "side": "buy",
                "fillSz": "0.00192834",
                "fillPx": "51858",
                "fillPxVol": "",
                "fillFwdPx": "",
                "fee": "-0.00000192834",
                "fillPnl": "0",
                "ordId": "680800019749904384",
                "feeRate": "-0.001",
                "instType": "SPOT",
                "fillPxUsd": "",
                "instId": "BTC-USDT",
                "clOrdId": "",
                "posSide": "net",
                "billId": "680800019754098688",
                "subType": "1",
                "fillMarkVol": "",
                "tag": "",
                "fillTime": "1708587373361",
                "execType": "T",
                "fillIdxPx": "",
                "tradeId": "744876980",
                "fillMarkPx": "",
                "feeCcy": "BTC",
                "ts": "1708587373362",
                "tradeQuoteCcy": "USDT"
            }
        ],
        "msg": ""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
instType | String | 产品类型  
instId | String | 产品 ID  
tradeId | String | 最新成交 ID  
ordId | String | 订单 ID  
clOrdId | String | 用户自定义订单ID  
billId | String | 账单 ID  
subType | String | 成交类型  
tag | String | 订单标签  
fillPx | String | 最新成交价格，同"账单流水查询"的 px  
fillSz | String | 最新成交数量  
fillIdxPx | String | 交易执行时的指数价格   
对于交叉现货币对，返回 baseCcy-USDT 的指数价格。 如 LTC-ETH，该字段返回LTC-USDT的指数价格。  
fillPnl | String | 本次成交的已实现盈亏，以结算货币（见 `feeCcy`）计价，仅适用于平仓交易。正数为盈利，负数为亏损。公式：正向合约 = (fillPx − avgPx) × fillSz × ctVal；反向合约 = (1/avgPx − 1/fillPx) × fillSz × ctVal。开仓交易返回0。  
fillPxVol | String | 成交时的隐含波动率，仅适用于期权，其他业务线返回空字符串""  
fillPxUsd | String | 成交时的期权价格，以USD为单位，仅适用于期权，其他业务线返回空字符串""  
fillMarkVol | String | 成交时的标记波动率，仅适用于期权，其他业务线返回空字符串""  
fillFwdPx | String | 成交时的远期价格，仅适用于期权，其他业务线返回空字符串""  
fillMarkPx | String | 成交时的标记价格，仅适用于 `交割`/`永续`/`期权`  
side | String | 订单方向 `buy`：买 `sell`：卖  
posSide | String | 持仓方向 `long`：多 `short`：空 买卖模式返回 `net`  
execType | String | 流动性方向 `T`：taker `M`：maker  
不适用于系统订单比如强平和ADL  
feeCcy | String | 交易手续费币种或者返佣金币种  
fee | String | 手续费金额或者返佣金额，手续费扣除为‘负数’，如-0.01；手续费返佣为‘正数’，如 0.01  
ts | String | 系统生成该成交记录的时间戳，Unix毫秒数格式（UTC）。注意：此字段与 `fillTime`（实际撮合成交时间）不同。若需按时间顺序排列成交记录，请使用 `fillTime` 而非 `ts` 进行排序。  
fillTime | String | 成交时间，与订单频道的`fillTime`相同  
feeRate | String | 手续费费率。 该字段仅对 `币币`和`杠杆`返回  
tradeQuoteCcy | String | 用于交易的计价币种。  
tradeId  
当订单种类（category）为 partial_liquidation：强制减仓、full_liquidation：强制平仓、adl：ADL自动减仓时，成交明细 tradeId 字段的值为负数，以便和其他撮合成交场景区分，订单信息 tradeId 字段的值为 0  
ordId  
订单ID, 对于大宗交易总是 "" 。  
clOrdId  
用户自定义订单ID, 对于大宗交易总是 "" 。 

### GET / 获取成交明细（近三个月） 

本接口可以查询最近 3 个月的成交明细数据。

#### 限速：10 次/2s

#### 限速规则：User ID

#### 权限：读取

#### HTTP 请求

`GET /api/v5/trade/fills-history`

> 请求示例
    
    
    GET /api/v5/trade/fills-history?instType=SPOT
    
    
    
    
    import okx.Trade as Trade
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # 实盘: 0, 模拟盘: 1
    
    tradeAPI = Trade.TradeAPI(apikey, secretkey, passphrase, False, flag)
    
    # 查询 币币 成交明细（3月内）
    result = tradeAPI.get_fills_history(
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
instFamily | String | 否 | 交易品种  
适用于`交割`/`永续`/`期权`  
instId | String | 否 | 产品 ID，如`BTC-USD-190927`  
ordId | String | 否 | 订单 ID  
subType | String | 否 | 成交类型   
`1`：买入  
`2`：卖出   
`3`：开多   
`4`：开空   
`5`：平多   
`6`：平空   
`100`：强减平多   
`101`：强减平空   
`102`：强减买入   
`103`：强减卖出   
`104`：强平平多   
`105`：强平平空   
`106`：强平买入   
`107`：强平卖出   
`110`：强平换币转入   
`111`：强平换币转出   
`118`：系统换币转入   
`119`：系统换币转出  
`112`：交割平多   
`113`：交割平空   
`125`：自动减仓平多   
`126`：自动减仓平空   
`127`：自动减仓买入   
`128`：自动减仓卖出   
`212`：一键借币的自动借币   
`213`：一键借币的自动还币   
`204`：大宗交易买   
`205`：大宗交易卖   
`206`：大宗交易开多   
`207`：大宗交易开空   
`208`：大宗交易平多   
`209`：大宗交易平空  
`236`：小额兑换买入  
`237`：小额兑换卖出  
`270`：价差交易买  
`271`：价差交易卖  
`272`：价差交易开多  
`273`：价差交易开空  
`274`：价差交易平多  
`275`：价差交易平空  
`324`：移仓买入  
`325`：移仓卖出  
`326`：移仓开多  
`327`：移仓开空  
`328`：移仓平多  
`329`：移仓平空  
`376`：质押借币超限买入  
`377`： 质押借币超限卖出  
`410`：买入yes  
`411`：买入no  
`412`：卖出yes  
`413`：卖出no  
`414`：yes结算  
`415`：no结算  
after | String | 否 | 请求此 ID 之前（更旧的数据）的分页内容，传的值为对应接口的 `billId`  
before | String | 否 | 请求此 ID 之后（更新的数据）的分页内容，传的值为对应接口的 `billId`  
begin | String | 否 | 筛选的开始时间戳 `ts`，Unix 时间戳为毫秒数格式，如 `1597026383085`  
end | String | 否 | 筛选的结束时间戳 `ts`，Unix 时间戳为毫秒数格式，如 `1597027383085`  
limit | String | 否 | 返回结果的数量，最大为100，默认100条  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "side": "buy",
                "fillSz": "0.00192834",
                "fillPx": "51858",
                "fillPxVol": "",
                "fillFwdPx": "",
                "fee": "-0.00000192834",
                "fillPnl": "0",
                "ordId": "680800019749904384",
                "feeRate": "-0.001",
                "instType": "SPOT",
                "fillPxUsd": "",
                "instId": "BTC-USDT",
                "clOrdId": "",
                "posSide": "net",
                "billId": "680800019754098688",
                "subType": "1",
                "fillMarkVol": "",
                "tag": "",
                "fillTime": "1708587373361",
                "execType": "T",
                "fillIdxPx": "",
                "tradeId": "744876980",
                "fillMarkPx": "",
                "feeCcy": "BTC",
                "ts": "1708587373362",
                "tradeQuoteCcy": "USDT"
            }
        ],
        "msg": ""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
instType | String | 产品类型  
instId | String | 产品 ID  
tradeId | String | 最新成交 ID  
ordId | String | 订单 ID  
clOrdId | String | 用户自定义订单ID  
billId | String | 账单 ID  
subType | String | 成交类型  
tag | String | 订单标签  
fillPx | String | 最新成交价格，同"账单流水查询"的 px  
fillSz | String | 最新成交数量  
fillIdxPx | String | 交易执行时的指数价格  
对于交叉现货币对，返回 baseCcy-USDT 的指数价格。 如 LTC-ETH，该字段返回 LTC-USDT 的指数价格。  
fillPnl | String | 最新成交收益，适用于有成交的平仓订单。其他情况均为0。  
fillPxVol | String | 成交时的隐含波动率，仅适用于期权，其他业务线返回空字符串""  
fillPxUsd | String | 成交时的期权价格，以USD为单位，仅适用于期权，其他业务线返回空字符串""  
fillMarkVol | String | 成交时的标记波动率，仅适用于期权，其他业务线返回空字符串""  
fillFwdPx | String | 成交时的远期价格，仅适用于期权，其他业务线返回空字符串""  
fillMarkPx | String | 成交时的标记价格，仅适用于 `交割`/`永续`/`期权`  
side | String | 订单方向  
`buy`：买  
`sell`：卖  
posSide | String | 持仓方向  
`long`：多  
`short`：空  
买卖模式返回 `net`  
execType | String | 流动性方向  
`T`：taker  
`M`：maker  
不适用于系统订单比如强平和ADL  
feeCcy | String | 交易手续费币种或者返佣金币种  
fee | String | 手续费金额或者返佣金额  
手续费扣除为‘负数’，如 -0.01  
手续费返佣为‘正数’，如 0.01  
ts | String | 成交明细产生时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
fillTime | String | 成交时间，与订单频道的`fillTime`相同  
feeRate | String | 手续费费率。 该字段仅对 `币币`和`杠杆`返回  
tradeQuoteCcy | String | 用于交易的计价币种。  
tradeId  
当成交明细所归属的订单种类（category）为 partial_liquidation：强制减仓、full_liquidation：强制平仓、adl：ADL自动减仓时，tradeId字段的值为负数，以便和其他撮合成交场景区分  
ordId  
订单ID, 对于大宗交易总是 "" 。  
clOrdId  
用户自定义订单ID, 对于大宗交易总是 "" 。  获取近3天的成交明细时，建议使用获取成交明细（近三天）接口。 

### GET / 获取一键兑换主流币币种列表 

获取小币一键兑换主流币币种列表。仅可兑换余额在 $10 以下币种。

#### 限速：1次/2s

#### 限速规则：User ID

#### 权限：读取

#### HTTP 请求

`GET /api/v5/trade/easy-convert-currency-list`

> 请求示例
    
    
    GET /api/v5/trade/easy-convert-currency-list
    
    
    
    import okx.Trade as Trade
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # 实盘: 0, 模拟盘: 1
    
    tradeAPI = Trade.TradeAPI(apikey, secretkey, passphrase, False, flag)
    
    # 获取小币一键兑换主流币币种列表
    result = tradeAPI.get_easy_convert_currency_list()
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
source | String | 否 | 资金来源  
`1`：交易账户  
`2`：资金账户  
默认为`1`  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "fromData": [
                    {
                        "fromAmt": "6.580712708344864",
                        "fromCcy": "ADA"
                    },
                    {
                        "fromAmt": "2.9970000013055097",
                        "fromCcy": "USDC"
                    }
                ],
                "toCcy": [
                    "USDT",
                    "BTC",
                    "ETH",
                    "OKB"
                ]
            }
        ],
        "msg": ""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
fromData | Array of objects | 当前拥有并可兑换的小币币种列表信息  
> fromCcy | String | 可兑换币种  
> fromAmt | String | 可兑换币种数量  
toCcy | Array of strings | 可转换成的主流币币种列表  
  
### POST / 一键兑换主流币交易 

进行小币一键兑换主流币交易。

#### 限速：1次/2s

#### 限速规则：User ID

#### 权限：交易

#### HTTP 请求

`POST /api/v5/trade/easy-convert`

> 请求示例
    
    
    POST /api/v5/trade/easy-convert
    body
    {
        "fromCcy": ["ADA","USDC"], //逗号分隔小币
        "toCcy": "OKB" 
    }
    
    
    
    import okx.Trade as Trade
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # 实盘: 0, 模拟盘: 1
    
    tradeAPI = Trade.TradeAPI(apikey, secretkey, passphrase, False, flag)
    
    # 进行小币一键兑换主流币交易
    result = tradeAPI.easy_convert(
        fromCcy=["ADA", "USDC"],
        toCcy="OKB"
    )
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
fromCcy | Array of strings | 是 | 小币支付币种   
单次最多同时选择5个币种，如有多个币种则用逗号隔开  
toCcy | String | 是 | 兑换的主流币   
只选择一个币种，且不能和小币支付币种重复  
source | String | 否 | 资金来源  
`1`：交易账户  
`2`：资金账户  
默认为`1`  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "fillFromSz": "6.5807127",
                "fillToSz": "0.17171580105126",
                "fromCcy": "ADA",
                "status": "running",
                "toCcy": "OKB",
                "uTime": "1661419684687"
            },
            {
                "fillFromSz": "2.997",
                "fillToSz": "0.1683755161661844",
                "fromCcy": "USDC",
                "status": "running",
                "toCcy": "OKB",
                "uTime": "1661419684687"
            }
        ],
        "msg": ""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
status | String | 当前兑换进度/状态   
`running`: 进行中   
`filled`: 已完成   
`failed`: 失败  
fromCcy | String | 小币支付币种  
toCcy | String | 兑换的主流币  
fillFromSz | String | 小币偿还币种支付数量  
fillToSz | String | 兑换的主流币成交数量  
uTime | String | 交易时间戳，Unix时间戳为毫秒数格式，如 1597026383085  
  
### GET / 获取一键兑换主流币历史记录 

查询一键兑换主流币过去7天内的历史记录与进度状态。

#### 限速：1次/2s

#### 限速规则：User ID

#### 权限：读取

#### HTTP 请求

`GET /api/v5/trade/easy-convert-history`

> 请求示例
    
    
    GET /api/v5/trade/easy-convert-history
    
    
    
    import okx.Trade as Trade
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # 实盘: 0, 模拟盘: 1
    
    tradeAPI = Trade.TradeAPI(apikey, secretkey, passphrase, False, flag)
    
    # 获取一键兑换主流币历史记录
    result = tradeAPI.get_easy_convert_history()
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
after | String | 否 | 查询在此之前(不包含)的内容，值为时间戳，Unix时间戳为毫秒数格式，如`1597026383085`  
before | String | 否 | 查询在此之后(不包含)的内容，值为时间戳，Unix时间戳为毫秒数格式，如`1597026383085`  
limit | String | 否 | 返回的结果集数量，默认为100，最大为100  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "fillFromSz": "0.1761712511667539",
                "fillToSz": "6.7342205900000000",
                "fromCcy": "OKB",
                "status": "filled",
                "toCcy": "ADA",
                "acct": "18",
                "uTime": "1661313307979"
            },
            {
                "fillFromSz": "0.1722106121112177",
                "fillToSz": "2.9971018300000000",
                "fromCcy": "OKB",
                "status": "filled",
                "toCcy": "USDC",
                "acct": "18",
                "uTime": "1661313307979"
            }
        ],
        "msg": ""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
fromCcy | String | 小币支付币种  
fillFromSz | String | 对应的小币支付数量  
toCcy | String | 兑换到的主流币  
fillToSz | String | 兑换到的主流币数量  
acct | String | 兑换到的主流币所在的账户  
`6`：资金账户   
`18`：交易账户  
status | String | 当前兑换进度/状态   
`running`: 进行中   
`filled`: 已完成   
`failed`: 失败  
uTime | String | 交易时间戳，Unix时间戳为毫秒数格式，如 1597026383085  
  
### GET / 获取一键还债币种列表 

查询一键还债币种列表。负债币种包括全仓负债和逐仓负债。仅适用于`跨币种保证金模式`/`组合保证金模式`。

#### 限速：1次/2s

#### 限速规则：User ID

#### 权限：读取

#### HTTP 请求

`GET /api/v5/trade/one-click-repay-currency-list`

> 请求示例
    
    
    GET /api/v5/trade/one-click-repay-currency-list
    
    
    
    import okx.Trade as Trade
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # 实盘: 0, 模拟盘: 1
    
    tradeAPI = Trade.TradeAPI(apikey, secretkey, passphrase, False, flag)
    
    # 查询一键还债币种列表
    result = tradeAPI.get_oneclick_repay_list()
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
debtType | String | 否 | 负债类型   
`cross`: 全仓负债   
`isolated`: 逐仓负债  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "debtData": [
                    {
                        "debtAmt": "29.653478",
                        "debtCcy": "LTC"
                    },
                    {
                        "debtAmt": "237803.6828295906051002",
                        "debtCcy": "USDT"
                    }
                ],
                "debtType": "cross",
                "repayData": [
                    {
                        "repayAmt": "0.4978335419825104",
                        "repayCcy": "ETH"
                    }
                ]
            }
        ],
        "msg": ""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
debtData | Array of objects | 负债币种信息  
> debtCcy | String | 负债币种  
> debtAmt | String | 可负债币种数量  
包括本金和利息  
debtType | String | 负债类型   
`cross`: 全仓负债   
`isolated`: 逐仓负债  
repayData | Array of objects | 偿还币种信息  
> repayCcy | String | 可偿还负债的币种  
> repayAmt | String | 可偿还负债的币种可用资产数量  
  
### POST / 一键还债交易 

交易一键偿还全仓债务。不支持逐仓负债的偿还。根据资金和交易账户的剩余可用余额为最大偿还数量。仅适用于`跨币种保证金模式`/`组合保证金模式`。

#### 限速：1次/2s

#### 限速规则：User ID

#### 权限：交易

#### HTTP 请求

`POST /api/v5/trade/one-click-repay`

> 请求示例
    
    
    POST /api/v5/trade/one-click-repay
    body
    {
        "debtCcy": ["ETH","BTC"], //逗号分隔债务币
        "repayCcy": "USDT" //用USDT偿还ETH和BTC
    }
    
    
    
    import okx.Trade as Trade
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # 实盘: 0, 模拟盘: 1
    
    tradeAPI = Trade.TradeAPI(apikey, secretkey, passphrase, False, flag)
    
    # 交易一键偿还小额全仓债务，使用USDT偿还ETH和BTC债务
    result = tradeAPI.oneclick_repay(
        debtCcy=["ETH", "BTC"],
        repayCcy="USDT"
    )
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
debtCcy | Array of strings | 是 | 负债币种   
单次最多同时选择5个币种，如有多个币种则用逗号隔开  
repayCcy | String | 是 | 偿还币种   
只选择一个币种，且不能和负债币种重复  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "debtCcy": "ETH", 
                "fillDebtSz": "0.01023052",
                "fillRepaySz": "30", 
                "repayCcy": "USDT", 
                "status": "filled",
                "uTime": "1646188520338"
            },
            {
                "debtCcy": "BTC", 
                "fillFromSz": "3",
                "fillToSz": "60,221.15910001",
                "repayCcy": "USDT",
                "status": "filled",
                "uTime": "1646188520338"
            }
        ],
        "msg": ""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
status | String | 当前还债进度/状态   
`running`: 进行中   
`filled`: 已完成   
`failed`: 失败  
debtCcy | String | 负债币种  
repayCcy | String | 偿还币种  
fillDebtSz | String | 负债币种成交数量  
fillRepaySz | String | 偿还币种成交数量  
uTime | String | 交易时间戳，Unix时间戳为毫秒数格式，如 1597026383085  
  
### GET / 获取一键还债历史记录 

查询一键还债近7天的历史记录与进度状态。仅适用于`跨币种保证金模式`/`组合保证金模式`。

#### 限速：1次/2s

#### 限速规则：User ID

#### 权限：读取

#### HTTP 请求

`GET /api/v5/trade/one-click-repay-history`

> 请求示例
    
    
    GET /api/v5/trade/one-click-repay-history
    
    
    
    import okx.Trade as Trade
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # 实盘: 0, 模拟盘: 1
    
    tradeAPI = Trade.TradeAPI(apikey, secretkey, passphrase, False, flag)
    
    # 获取一键还债历史记录
    result = tradeAPI.oneclick_repay_history()
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
after | String | 否 | 查询在此之前的内容，值为时间戳，Unix时间戳为毫秒数格式，如`1597026383085`  
before | String | 否 | 查询在此之后的内容，值为时间戳，Unix时间戳为毫秒数格式，如`1597026383085`  
limit | String | 否 | 返回的结果集数量，默认为100，最大为100  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "debtCcy": "USDC",
                "fillDebtSz": "6950.4865447900000000",
                "fillRepaySz": "4.3067975995094930",
                "repayCcy": "ETH",
                "status": "filled",
                "uTime": "1661256148746"
            }
        ],
        "msg": ""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
debtCcy | String | 负债币种  
fillDebtSz | String | 对应的负债币种成交数量  
repayCcy | String | 偿还币种  
fillRepaySz | String | 偿还币种实际支付数量  
status | String | 当前还债进度/状态   
`running`: 进行中   
`filled`: 已完成   
`failed`: 失败  
uTime | String | 交易时间戳，Unix时间戳为毫秒数格式，如 1597026383085  
  
### GET / 获取一键还债币种列表(新) 

查询一键还债币种列表。仅适用于`现货模式`/`跨币种保证金模式`/`组合保证金模式`。

#### 限速：1次/2s

#### 限速规则：User ID

#### 权限：读取

#### HTTP 请求

`GET /api/v5/trade/one-click-repay-currency-list-v2`

> 请求示例
    
    
    GET /api/v5/trade/one-click-repay-currency-list-v2
    
    
    
    import okx.Trade as Trade
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    flag = "1"  # 实盘: 0, 模拟盘: 1
    
    tradeAPI = Trade.TradeAPI(apikey, secretkey, passphrase, False, flag,debug=True) 
    result = tradeAPI.get_oneclick_repay_list_v2()
    print(result)
    

> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "debtData": [
                    {
                        "debtAmt": "100",
                        "debtCcy": "USDC"
                    }
                ],
                "repayData": [
                    {
                        "repayAmt": "1.000022977",
                        "repayCcy": "BTC"
                    },
                    {
                        "repayAmt": "4998.0002397",
                        "repayCcy": "USDT"
                    },
                    {
                        "repayAmt": "100",
                        "repayCcy": "OKB"
                    },
                    {
                        "repayAmt": "1",
                        "repayCcy": "ETH"
                    },
                    {
                        "repayAmt": "100",
                        "repayCcy": "USDC"
                    }
                ]
            }
        ],
        "msg": ""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
debtData | Array of objects | 负债币种信息  
> debtCcy | String | 负债币种  
> debtAmt | String | 可负债币种数量  
包括本金和利息  
repayData | Array of objects | 偿还币种信息  
> repayCcy | String | 可偿还负债的币种  
> repayAmt | String | 可偿还负债的币种可用资产数量  
  
### POST / 一键还债交易(新) 

交易一键偿还债务。仅适用于`现货模式`/`跨币种保证金模式`/`组合保证金模式`。

#### 限速：1次/2s

#### 限速规则：User ID

#### 权限：交易

#### HTTP 请求

`POST /api/v5/trade/one-click-repay-v2`

> 请求示例
    
    
    POST /api/v5/trade/one-click-repay-v2
    body
    {
        "debtCcy": "USDC", 
        "repayCcyList": ["USDC","BTC"] 
    }
    
    
    
    import okx.Trade as Trade
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    flag = "1"  # 实盘: 0, 模拟盘: 1
    
    tradeAPI = Trade.TradeAPI(apikey, secretkey, passphrase, False, flag,debug=True)
    result = tradeAPI.oneclick_repay_v2("USDC",["USDC","BTC"])
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
debtCcy | String | 是 | 负债币种  
repayCcyList | Array of strings | 是 | 偿还币种列表，如 ["USDC","BTC"]  
资产还币优先级和数组中的排序一致（排第一的优先级最高）。  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "debtCcy": "USDC",
                "repayCcyList": [
                    "USDC",
                    "BTC"
                ],
                "ts": "1742192217514"
            }
        ],
        "msg": ""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
debtCcy | String | 负债币种  
repayCcyList | Array of strings | 偿还币种列表，如 ["USDC","BTC"]  
资产还币优先级和数组中的排序一致（排第一的优先级最高）。  
ts | String | 请求时间，Unix时间戳为毫秒数格式，如 `1597026383085`  
  
### GET / 获取一键还债历史记录(新) 

查询一键还债近7天的历史记录与进度状态。仅适用于`现货模式`。

#### 限速：1次/2s

#### 限速规则：User ID

#### 权限：读取

#### HTTP 请求

`GET /api/v5/trade/one-click-repay-history-v2`

> 请求示例
    
    
    GET /api/v5/trade/one-click-repay-history-v2
    
    
    
    import okx.Trade as Trade
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    flag = "1"  # 实盘: 0, 模拟盘: 1
    
    tradeAPI = Trade.TradeAPI(apikey, secretkey, passphrase, False, flag)
    result = tradeAPI.oneclick_repay_history_v2()
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
after | String | 否 | 查询在指定请求时间`ts`之前(包含)的内容，值为时间戳，Unix时间戳为毫秒数格式，如 `1597026383085`  
before | String | 否 | 查询在指定请求时间`ts`之后(包含)的内容，值为时间戳，Unix时间戳为毫秒数格式，如 `1597026383085`  
limit | String | 否 | 返回的结果集数量，默认为`100`，最大为`100`  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "debtCcy": "USDC",
                "fillDebtSz": "9.079631989",
                "ordIdInfo": [
                    {
                        "cTime": "1742194485439",
                        "fillPx": "1",
                        "fillSz": "9.088651",
                        "instId": "USDC-USDT",
                        "ordId": "2338478342062235648",
                        "ordType": "ioc",
                        "px": "1.0049",
                        "side": "buy",
                        "state": "filled",
                        "sz": "9.0886514537313433"
                    },
                    {
                        "cTime": "1742194482326",
                        "fillPx": "83271.9",
                        "fillSz": "0.00010969",
                        "instId": "BTC-USDT",
                        "ordId": "2338478237607288832",
                        "ordType": "ioc",
                        "px": "82856.7",
                        "side": "sell",
                        "state": "filled",
                        "sz": "0.000109696512171"
                    }
                ],
                "repayCcyList": [
                    "USDC",
                    "BTC"
                ],
                "status": "filled",
                "ts": "1742194481852"
            },
            {
                "debtCcy": "USDC",
                "fillDebtSz": "100",
                "ordIdInfo": [],
                "repayCcyList": [
                    "USDC",
                    "BTC"
                ],
                "status": "filled",
                "ts": "1742192217511"
            }
        ],
        "msg": ""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
debtCcy | String | 负债币种  
repayCcyList | Array of strings | 偿还币种列表，如 ["USDC","BTC"]  
fillDebtSz | String | 对应的负债币种成交数量  
status | String | 当前还债进度/状态  
`running`：进行中   
`filled`：已完成   
`failed`：失败  
ordIdInfo | Array of objects | 相关订单信息  
> ordId | String | 订单ID  
> instId | String | 产品ID，如 `BTC-USDT`  
> ordType | String | 订单类型  
`ioc`：立即成交并取消剩余  
> side | String | 订单方向  
`buy`  
`sell`  
> px | String | 委托价格  
> sz | String | 委托数量  
> fillPx | String | 最新成交价格  
如果成交数量为0，该字段为""  
> fillSz | String | 最新成交数量  
> state | String | 订单状态  
`filled`：完全成交  
`canceled`：撤单成功  
> cTime | String | 订单创建时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
ts | String | 请求时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
  
### POST / 撤销 MMP 订单

撤销同一交易品种下用户所有的 MMP 挂单  
仅适用于组合保证金账户模式下的期权订单，且有 MMP 权限。

#### 限速：5次/2s

#### 限速规则：User ID

#### 权限：交易

#### HTTP请求

`POST /api/v5/trade/mass-cancel`

> 请求示例
    
    
    POST /api/v5/trade/mass-cancel
    body
    {
        "instType":"OPTION",
        "instFamily":"BTC-USD"
    }
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
instType | String | 是 | 交易产品类型  
`OPTION`:期权  
instFamily | String | 是 | 交易品种  
lockInterval | String | 否 | 锁定时长(毫秒)  
范围应为[0, 10 000]  
默认为 0. 如果想要立即解锁，您可以设置为 "0"  
下单时，如果在该锁定期间，会报错 54008，如果在 MMP 触发期间，会报错 51034  
  
> 返回结果
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
            {
                "result":true
            }
        ]
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
result | Boolean | 撤单结果  
`true`：全部撤单成功  
`false`：全部撤单失败  
  
### POST / 倒计时全部撤单

在倒计时结束后，取消所有挂单。适用于所有撮合交易产品（不包括价差交易）。

#### 限速：1次/s

#### 限速规则：User ID + tag

#### 权限：交易

#### HTTP请求

`POST /api/v5/trade/cancel-all-after`

> 请求示例
    
    
    POST /api/v5/trade/cancel-all-after
    {
       "timeOut":"60"
    }
    
    
    
    import okx.Trade as Trade
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # 实盘: 0, 模拟盘: 1
    
    tradeAPI = Trade.TradeAPI(apikey, secretkey, passphrase, False, flag)
    
    # 设置倒计时全部撤单
    result = tradeAPI.cancel_all_after(
        timeOut="10"
    )
    
    print(result)
    
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
timeOut | String | 是 | 取消挂单的倒计时，单位为秒  
取值范围为 0, [10, 120]  
0 代表不使用该功能  
tag | String | 否 | CAA订单标签  
字母（区分大小写）与数字的组合，可以是纯字母、纯数字，且长度在1-16位之间  
  
> 返回结果
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
            {
                "triggerTime":"1587971460",
                "tag":"",
                "ts":"1587971400"
            }
        ]
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
triggerTime | String | 触发撤单的时间  
triggerTime=0 代表未使用该功能  
tag | String | CAA订单标签  
ts | String | 请求被接收到的时间  
建议用户每一秒调用接口一次。当倒计时全部撤单被触发时，交易引擎将为用户逐一取消其挂单，该操作可能持续数秒。该功能起到保护用户的作用，不应作为交易策略使用。    
为使用标签维度倒计时全部撤单，首先，用户需使用现有下单接口的tag请求参数，为订单设置标签。调用CAA接口时，若不传入tag请求参数，则默认设置账户维度CAA，CAA触发时，撤销该子账户下的所有撮合交易产品挂单；若传入tag请求参数，则默认设置订单标签维度CAA，CAA触发时，带有此tag的撮合交易产品挂单将被撤销，带有其他tag或没有tag的订单将不受影响。   
  
同一子账户下，用户最多能同时运行20个标签维度的CAA。系统仅计数活跃的标签维度CAA，已被触发或被用户主动撤销的将不被计入。超过限制时，用户将收到错误码51071。 

### GET / 获取账户限速 

获取账户限速相关信息  

仅有新订单及修改订单请求会被计入此限制。对于包含多个订单的批量请求，每个订单将被单独计数。  

更多细节，请见 [基于成交比率的子账户限速](/docs-v5/zh/#overview-rate-limits-fill-ratio-based-sub-account-rate-limit)

#### 限速：1次/s

#### 限速规则：User ID

#### 权限：读取

#### HTTP请求

`GET /api/v5/trade/account-rate-limit`

> 请求示例
    
    
    # 获取账户限速相关信息
    GET /api/v5/trade/account-rate-limit
    
    

#### 请求参数

None

> 返回结果
    
    
    {
       "code":"0",
       "data":[
          {
             "accRateLimit":"2000",
             "fillRatio":"0.1234",
             "mainFillRatio":"0.1234",
             "nextAccRateLimit":"2000",
             "ts":"123456789000"
          }
       ],
       "msg":`""`
    }
    
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
fillRatio | String | 监测期内子账户的成交比率。   
适用于交易费等级 >= VIP 5 的用户，其他用户返回 `""`。  
若账户在过去 7 天内无任何成交数据，则返回 `""`。  
若监测期内无成交量，则返回 `"0"`。  
若监测期内有成交量但无下单操作数，则返回 `"9999"`。  
mainFillRatio | String | 监测期内母账户合计成交比率。  
适用于交易费等级 >= VIP 5 的用户，其他用户返回 `""`。  
若账户在过去 7 天内无任何成交数据，则返回 `""`。  
若监测期内无成交量，则返回 `"0"`。  
accRateLimit | String | 当前子账户交易限速（每两秒）  
nextAccRateLimit | String | 下一评估周期预计的子账户交易限速（每两秒）。  
适用于交易费等级 >= VIP 5的用户，其余用户返回 `""` 。  
ts | String | 数据更新时间   
对于交易费等级>= VIP 5的用户，数据将于每日 08:00（UTC）生成   
对于交易费等级 < VIP 5的用户，返回当前时间戳 。  
  
### POST / 订单预检查 

用来预先查看订单下单前后的账户的对比信息，仅适用于`跨币种保证金模式`和`组合保证金模式`。

#### 限速：5次/2s

#### 限速规则：User ID

#### 权限：交易

#### HTTP请求

`POST /api/v5/trade/order-precheck`

> 请求示例
    
    
    POST /api/v5/trade/order-precheck
    body
    {
        "instId":"BTC-USDT",
        "tdMode":"cash",
        "clOrdId":"b15",
        "side":"buy",
        "ordType":"limit",
        "px":"2.15",
        "sz":"2"
    }
    
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
instId | String | 是 | 产品ID，如 `BTC-USDT`  
tdMode | String | 是 | 交易模式  
保证金模式：`isolated`：逐仓 ；`cross`：全仓   
非保证金模式：`cash`：非保证金  
`spot_isolated`：现货逐仓(仅适用于现货带单) ，现货带单时，`tdMode` 的值需要指定为`spot_isolated`  
side | String | 是 | 订单方向  
`buy`：买， `sell`：卖  
posSide | String | 可选 | 持仓方向  
在开平仓模式下必填，且仅可选择 `long` 或 `short`。 仅适用交割、永续。  
ordType | String | 是 | 订单类型   
`market`：市价单  
`limit`：限价单   
`post_only`：只做maker单   
`fok`：全部成交或立即取消   
`ioc`：立即成交并取消剩余   
`optimal_limit_ioc`：市价委托立即成交并取消剩余（仅适用交割、永续）  
`elp`：流动性增强计划订单  
sz | String | 是 | 委托数量  
px | String | 可选 | 委托价格，仅适用于`limit`、`post_only`、`fok`、`ioc`类型的订单  
outcome | String | 可选 | 用户交易的市场结果方向。  
`yes`  
`no`  
仅适用于 `EVENTS`，且为必填  
reduceOnly | Boolean | 否 | 是否只减仓，`true` 或 `false`，默认`false`  
仅适用于`币币杠杆`，以及买卖模式下的`交割/永续`  
仅适用于`合约模式`和`跨币种保证金模式`  
tgtCcy | String | 否 | 市价单委托数量`sz`的单位，仅适用于`币币`市价订单  
`base_ccy`: 交易货币 ；`quote_ccy`：计价货币  
买单默认`quote_ccy`， 卖单默认`base_ccy`  
attachAlgoOrds | Array of objects | 否 | 附带止盈止损或移动止盈止损订单信息  
> attachAlgoClOrdId | String | 否 | 下单附带止盈止损或移动止盈止损时，客户自定义的策略订单ID   
字母（区分大小写）与数字的组合，可以是纯字母、纯数字且长度要在1-32位之间。  
订单完全成交，下附带策略委托单时，该值会传给`algoClOrdId`  
> tpTriggerPx | String | 可选 | 止盈触发价  
对于条件止盈单，如果填写此参数，必须填写 止盈委托价  
> tpOrdPx | String | 可选 | 止盈委托价  
对于条件止盈单，如果填写此参数，必须填写 止盈触发价  
对于限价止盈单，需填写此参数，不需要填写止盈触发价  
委托价格为-1时，执行市价止盈  
> tpOrdKind | String | 否 | 止盈订单类型  
`condition`: 条件单  
`limit`: 限价单  
默认为`condition`  
> slTriggerPx | String | 可选 | 止损触发价，如果填写此参数，必须填写 止损委托价  
> slOrdPx | String | 可选 | 止损委托价，如果填写此参数，必须填写 止损触发价  
委托价格为-1时，执行市价止损  
> tpTriggerPxType | String | 否 | 止盈触发价类型  
`last`：最新价格  
`index`：指数价格  
`mark`：标记价格  
默认为`last`  
> slTriggerPxType | String | 否 | 止损触发价类型  
`last`：最新价格  
`index`：指数价格  
`mark`：标记价格  
默认为`last`  
> sz | String | 可选 | 数量。仅适用于”多笔止盈”的止盈订单，且对于”多笔止盈”的止盈订单必填  
> callbackRatio | String | 可选 | 回调幅度的比例，如 `0.05` 代表 5%。  
`callbackRatio` 和 `callbackSpread` 必须传入其中一个，且只能传入一个。  
仅适用于 `ordType` = `move_order_stop`  
> callbackSpread | String | 可选 | 回调幅度的价距。  
`callbackRatio` 和 `callbackSpread` 必须传入其中一个，且只能传入一个。  
仅适用于 `ordType` = `move_order_stop`  
> activePx | String | 否 | 激活价格。  
激活价格是移动止盈止损的激活条件，当市场最新成交价达到或超过激活价格，委托被激活。激活后系统开始计算止盈止损的实际触发价格。如果不填写激活价格，即下单后就被激活。  
仅适用于 `ordType` = `move_order_stop`  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "adjEq": "41.94347460746277",
                "adjEqChg": "-226.05616481626",
                "availBal": "0",
                "availBalChg": "0",
                "imr": "0",
                "imrChg": "57.74709688430927",
                "liab": "0",
                "liabChg": "0",
                "liabChgCcy": "",
                "liqPx": "6764.8556232031115",
                "liqPxDiff": "-57693.044376796888536773622035980224609375",
                "liqPxDiffRatio": "-0.8950500152315991",
                "mgnRatio": "0",
                "mgnRatioChg": "0",
                "mmr": "0",
                "mmrChg": "0",
                "posBal": "",
                "posBalChg": "",
                "type": ""
            }
        ],
        "msg": ""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
adjEq | String | 当前美金层面有效保证金  
adjEqChg | String | 下单后，美金层面有效保证金的变动数量  
imr | String | 当前美金层面占用保证金  
imrChg | String | 下单后，美金层面占用保证金的变动数量  
mmr | String | 当前美金层面维持保证金  
mmrChg | String | 下单后，美金层面维持保证金的变动数量  
mgnRatio | String | 当前美金层面维持保证金率  
mgnRatioChg | String | 下单后，美金层面维持保证金率的变动数量  
availBal | String | 当前币种可用余额，仅适用于关闭自动借币时  
availBalChg | String | 下单后，币种可用余额的变动数量，仅适用于关闭自动借币时  
liqPx | String | 当前预估强平价  
liqPxDiff | String | 下单后，预估强平价与标记价格的差距  
liqPxDiffRatio | String | 下单后，预估强平价与标记价格的差距比率  
posBal | String | 当前杠杆逐仓仓位正资产，仅适用于逐仓杠杆  
posBalChg | String | 下单后，杠杆逐仓仓位正资产的变动数量，仅适用于逐仓杠杆  
liab | String | 当前负债  
如果是全仓，对应全仓负债，如果是逐仓，对应逐仓负债  
liabChg | String | 下单后，当前负债的变动数量  
如果是全仓，对应全仓负债，如果是逐仓，对应逐仓负债  
liabChgCcy | String | 下单后，当前负债变动数量的单位  
仅适用于全仓，开启自动借币时  
type | String | 仓位正资产(`posBal`)的单位类型，仅适用于杠杆逐仓，用来确定`posBal`的单位   
`1`:下单前后都是交易货币  
`2`:下单前是交易货币，下单后是计价货币  
`3`:下单前是计价货币，下单后是交易货币  
`4`:下单前后都是计价货币  
  
### WS / 订单频道 

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
`3`: 用户主动下单，并且当前这笔订单被只减仓修改，改单成功  
`4`: 用户当前已存在的挂单（非当前操作的订单），被只减仓修改，改单成功  
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

### WS / 成交频道 

获取成交信息。该频道无首推，仅在订单簿成交相关事件触发时推送数据，tradeId > 0。

该频道仅适用于交易等级VIP4及以上的用户，其他用户接入将收到错误码64003。其他用户请使用[WS / 订单频道](/docs-v5/zh/#order-book-trading-trade-ws-order-channel)。

对于 `EVENTS`，无论实际订单是否为 YES 或 NO 方向，仅推送 YES 侧成交数据。

#### 服务地址

/ws/v5/private (需要登录)

> 请求示例：单个
    
    
    {
        "id": "1512",
        "op": "subscribe",
        "args": [
            {
                "channel": "fills",
                "instId": "BTC-USDT-SWAP"
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
                "channel": "fills",
                "instId": "BTC-USDT-SWAP"
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
                "channel": "fills"
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
                "channel": "fills"
            }
        ]
    
        await ws.subscribe(args, callback=callbackFunc)
        await asyncio.sleep(10)
    
        await ws.unsubscribe(args, callback=callbackFunc)
        await asyncio.sleep(10)
    
    
    asyncio.run(main())
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
id | String | 否 | 消息的唯一标识。  
用户提供，返回参数中会返回以便于找到相应的请求。  
字母（区分大小写）与数字的组合，可以是纯字母、纯数字且长度必须要在1-32位之间。  
op | String | 是 | 操作  
`subscribe`  
`unsubscribe`  
args | Array of objects | 是 | 订阅的频道  
> channel | String | 是 | 频道名  
`fills`  
> instId | String | 否 | 产品ID  
  
> 成功返回示例：单个
    
    
    {
      "id": "1512",
      "event": "subscribe",
      "arg": {
        "channel": "fills",
        "instId": "BTC-USDT-SWAP"
      },
      "connId": "a4d3ae55"
    }
    
    

> 成功返回示例
    
    
    {
      "id": "1512",
      "event": "subscribe",
      "arg": {
        "channel": "fills"
      },
      "connId": "a4d3ae55"
    }
    
    

#### 返回参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
id | String | 否 | 消息的唯一标识  
event | String | 是 | 事件  
`subscribe`  
`unsubscribe`  
`error`  
arg | Object | 否 | 订阅的频道  
> channel | String | 是 | 频道名  
`fills`  
> instId | String | 否 | 产品ID  
code | String | 否 | 错误码  
msg | String | 否 | 错误消息  
connId | String | 是 | WebSocket连接ID  
  
> 推送示例：单个
    
    
    {
        "arg": {
            "channel": "fills",
            "instId": "BTC-USDT-SWAP",
            "uid": "614488474791111"
        },
        "data":[
            {
                "instId": "BTC-USDT-SWAP",
                "fillSz": "100",
                "fillPx": "70000",
                "side": "buy",
                "ts": "1705449605015",
                "ordId": "680800019749904384",
                "clOrdId": "1234567890",
                "tradeId": "12345",
                "execType": "T",
                "count": "10"
            }
        ]
    }
    
    

#### 推送数据参数

参数名 | 类型 | 描述  
---|---|---  
arg | Object | 订阅成功的频道  
> channel | String | 频道名  
> uid | String | 用户标识  
> instId | String | 产品ID  
data | Array of objects | 订阅的数据  
> instId | String | 产品ID  
> fillSz | String | 成交数量，若这笔成交有聚合，则成交数量为聚合后的数量  
> fillPx | String | 成交价格  
> side | String | 订单方向  
`buy`  
`sell`  
> ts | String | 成交时间  
> ordId | String | 订单ID  
> clOrdId | String | 由用户设置的订单ID  
> tradeId | String | 成交ID  
若为taker订单且有聚合，则为聚合的多笔交易中最新一笔交易的成交ID  
> execType | String | 流动性方向  
`T`：taker  
`M`：maker  
> count | String | 聚合的订单匹配数量  
\- 该频道仅适用于交易等级VIP4及以上的用户，其他用户接入将收到错误码64003  
\- 该频道只推送部分订单频道的信息，与大宗交易、价差速递相关的成交，强平、自动减仓等非订单簿事件不会通过该频道推送。用户应同时关注订单频道，对订单做最终确认  
\- 该频道接收到成交推送时，账户余额、保证金、持仓等信息可能仍未发生变化  
\- taker订单将根据不同成交价格进行聚合，有聚合时，count字段表示聚合的订单匹配数量，tradeId代表聚合的多笔交易中最新一笔交易的ID；maker订单不会聚合  
\- 用户可以在下单时指定clOrdId，成交时会返回该字段。请注意，成交频道仅在用户输入的clOrdId符合带符号int64正整数格式（1-9223372036854775807, 2^63-1）时返回该字段；若用户未输入该字段，或clOrdId不符合格式要求，该字段将返回"0"。订单接口及频道将照常返回用户传入的clOrdId。所有请求及返回参数均为字符串类型。  
\- 未来，该频道将施加连接数量限制，子账户维度，订阅成交频道的最大连接数为20个。我们建议用户始终低于限制使用该频道，以免限制上线后对策略造成影响 

### WS / 下单 

只有当您的账户有足够的资金才能下单。一旦下单，您的账户资金将在订单生命周期内被冻结。被冻结的资金以及数量取决于订单指定的类型和参数  
  

#### 服务地址

/ws/v5/private (需要登录)

#### 限速：60次/2s

#### 跟单交易带单员带单产品的限速：4次/2s

#### 限速规则（期权以外）：User ID + Instrument ID

#### 限速规则（只限期权）：User ID + Instrument Family

该接口限速同时受到 [子账户限速](/docs-v5/log_zh/#upcoming-changes-sub-account-rate-limit) 及 [基于成交比率的子账户限速](/docs-v5/log_zh/#upcoming-changes-fill-ratio-based-sub-account-rate-limit) 限速规则的影响。

同`下单` REST API 共享限速 

> 请求示例
    
    
    {
        "id": "1512",
        "op": "order",
        "args": [{
            "side": "buy",
            "instIdCode": 123456,
            "tdMode": "isolated",
            "ordType": "market",
            "sz": "100"
        }]
    }
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
id | String | 是 | 消息的唯一标识  
用户提供，返回参数中会返回以便于找到相应的请求。  
字母（区分大小写）与数字的组合，可以是纯字母、纯数字且长度必须要在1-32位之间。  
op | String | 是 | 操作  
`order`  
args | Array of objects | 是 | 请求参数  
> instIdCode | Integer | 是 | 产品唯一标识代码。  
> tdMode | String | 是 | 交易模式  
保证金模式 `isolated`：逐仓 `cross`：全仓   
非保证金模式 `cash`：现金  
`spot_isolated`：现货逐仓(仅适用于现货带单) ，现货带单时，`tdMode` 的值需要指定为`spot_isolated`   
  
事件合约对应交易产品仅支持`isolated`逐仓下单  
> ccy | String | 否 | 保证金币种，适用于`逐仓杠杆`及`合约模式`下的`全仓杠杆`订单  
> clOrdId | String | 否 | 由用户设置的订单ID  
字母（区分大小写）与数字的组合，可以是纯字母、纯数字且长度要在1-32位之间。  
> tag | String | 否 | 订单标签  
字母（区分大小写）与数字的组合，可以是纯字母、纯数字且长度要在1-16位之间。  
> side | String | 是 | 订单方向，`buy` `sell`  
> posSide | String | 否 | 持仓方向  
在买卖模式下，默认 `net`  
在开平仓模式下必填，且仅可选择 `long` 或 `short`，仅适用于`交割/永续`  
> ordType | String | 是 | 订单类型   
`market`：市价单，仅适用于`币币/杠杆/交割/永续`  
`limit`：限价单   
`post_only`：只做maker单   
`fok`：全部成交或立即取消   
`ioc`：立即成交并取消剩余   
`optimal_limit_ioc`：市价委托立即成交并取消剩余（仅适用交割、永续）  
`mmp`：做市商保护(仅适用于组合保证金账户模式下的期权订单)  
`mmp_and_post_only`：做市商保护且只做maker单(仅适用于组合保证金账户模式下的期权订单)  
`elp`：流动性增强计划订单  
> sz | String | 是 | 委托数量  
> px | String | 可选 | 委托价格，仅适用于`limit`、`post_only`、`fok`、`ioc`、`mmp`、`mmp_and_post_only`类型的订单  
期权下单时，px/pxUsd/pxVol 只能填一个  
> speedBump | String | 可选 | 减速带  
`1`：事件合约速度限制（延迟可能因市场情况调整，不提前通知）。对 `EVENTS` 产品的非只挂单操作为必填。  
> outcome | String | 可选 | 用户交易的市场结果方向。  
`yes`  
`no`  
仅适用于 `EVENTS`，且为必填  
> pxUsd | String | 可选 | 以USD价格进行期权下单   
仅适用于期权   
期权下单时 px/pxUsd/pxVol 必填一个，且只能填一个  
> pxVol | String | 可选 | 以隐含波动率进行期权下单，例如 1 代表 100%   
仅适用于期权   
期权下单时 px/pxUsd/pxVol 必填一个，且只能填一个  
> reduceOnly | Boolean | 否 | 是否只减仓，`true` 或 `false`，默认`false`  
仅适用于`币币杠杆`，以及买卖模式下的`交割/永续`  
仅适用于`合约模式`和`跨币种保证金模式`  
> tgtCcy | String | 否 | 币币市价单委托数量`sz`的单位  
`base_ccy`: 交易货币 ；`quote_ccy`：计价货币  
仅适用于`币币`市价订单  
默认买单为`quote_ccy`，卖单为`base_ccy`  
> banAmend | Boolean | 否 | 是否禁止币币市价改单，true 或 false，默认false   
为true时，余额不足时，系统不会改单，下单会失败，仅适用于币币市价单  
> pxAmendType | String | 否 | 订单价格修正类型  
`0`：当`px`超出价格限制时，不允许系统修改订单价格  
`1`：当`px`超出价格限制时，允许系统将价格修改为限制范围内的最优值  
默认值为`0`  
> tradeQuoteCcy | String | 否 | 用于交易的计价币种。仅适用于`币币`。  
默认值为 `instId` 的计价币种，比如：对于 `BTC-USD`，默认取 `USD`。  
> slippagePct | String | 否 | 币币、币币杠杆市价单（`tgtCcy` 为到手币种：买单为 `base_ccy`，卖单为 `quote_ccy`）的最大可接受滑点。  
取值范围：`0` 至 `0.05`（即 0% 至 5%，含边界），以百分比形式表示时最多保留 2 位小数，例如 `0.01`（1%）和 `0.0123`（1.23%）合法；`0.01234`（1.234%）将被拒绝。  
不填或为空时，默认为 `0.00%`。  
不支持改单修改滑点，如需调整请撤单重新提交。  
仅适用于币币和币币杠杆的市价单。  
> stpMode | String | 否 | 自成交保护模式   
`cancel_maker`,`cancel_taker`, `cancel_both`  
Cancel both不支持FOK   
  
默认使用账户层面的acctStpMode进行下单，该字段的默认值为`cancel_maker`，用户可通过母账户登录网页修改该配置；用户亦可以通过下单接口的stpMode参数指定订单的STP模式。  
> isElpTakerAccess | Boolean | 否 | 是否作为 taker 吃单 ELP  
`true`：该请求能吃单 ELP，但会被施加延迟  
`false`：该请求不能吃单 ELP，并且没有延迟  
  
默认值为`false`，`true`仅适用于ioc订单  
expTime | String | 否 | 请求有效截止时间。Unix时间戳的毫秒数格式，如 `1597026383085`  
  
> 成功返回示例
    
    
    {
        "id": "1512",
        "op": "order",
        "data": [{
            "clOrdId": "",
            "ordId": "12345689",
            "tag": "",
            "ts":"1695190491421",
            "sCode": "0",
            "sMsg": "",
            "subCode": ""
        }],
        "code": "0",
        "msg": "",
        "inTime": "1695190491421339",
        "outTime": "1695190491423240"
    }
    

> 失败返回示例
    
    
    {
        "id": "1512",
        "op": "order",
        "data": [{
            "clOrdId": "",
            "ordId": "",
            "tag": "",
            "ts":"1695190491421",
            "sCode": "51008",
            "sMsg": "Order failed. Insufficient USDT balance in account",
            "subCode": "1000"
        }],
        "code": "1",
        "msg": "",
        "inTime": "1695190491421339",
        "outTime": "1695190491423240"
    }
    

> 格式错误返回示例
    
    
    {
        "id": "1512",
        "op": "order",
        "data": [],
        "code": "60013",
        "msg": "Invalid args",
        "inTime": "1695190491421339",
        "outTime": "1695190491423240"
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
id | String | 消息的唯一标识  
op | String | 操作  
`order`  
code | String | 代码  
msg | String | 消息  
data | Array of objects | 请求成功后返回的数据  
> ordId | String | 订单ID  
> clOrdId | String | 由用户设置的订单ID  
> tag | String | 订单标签  
> ts | String | 系统完成订单请求处理的时间戳，Unix时间戳的毫秒数格式，如 `1597026383085`  
> sCode | String | 订单状态码，0 代表成功  
> sMsg | String | 订单状态消息  
> subCode | String | sCode 的子码。  
当 sCode 为 0（请求成功）时，返回 `""`。  
当 sCode 不为 0（请求失败）且存在子码时，返回对应的子码；若无子码，则返回 `""`。  
inTime | String | WebSocket 网关接收请求时的时间戳，Unix时间戳的微秒数格式，如 `1597026383085123`  
outTime | String | WebSocket 网关发送响应时的时间戳，Unix时间戳的微秒数格式，如 `1597026383085123`  
tdMode  
交易模式，下单时需要指定  
**现货模式：**  
\- 币币和期权买方：cash  
**合约模式：**  
\- 逐仓杠杆：isolated  
\- 全仓杠杆：cross  
\- 币币：cash  
\- 全仓交割/永续/期权：cross  
\- 逐仓交割/永续/期权：isolated  
**跨币种保证金模式：**  
\- 逐仓杠杆：isolated  
\- 全仓币币：cross  
\- 全仓交割/永续/期权：cross  
\- 逐仓交割/永续/期权：isolated  
**组合保证金模式：**  
\- 逐仓杠杆：isolated  
\- 全仓币币：cross  
\- 全仓交割/永续/期权：cross  
\- 逐仓交割/永续/期权：isolated  
clOrdId  
clOrdId 是用户在 User ID 维度自定义的订单唯一标识符。如果在请求参数中传入了，那它一定会在返回参数内，并且可以用于查询订单，撤销订单，修改订单等接口。  
clOrdId不能与当前所有的挂单的clOrdId重复  posSide  
持仓方向，买卖模式下此参数非必填，如果填写仅可以选择net；在开平仓模式下必填，且仅可选择 long 或 short。  
开平仓模式下，side和posSide需要进行组合  
开多：买入开多（side 填写 buy； posSide 填写 long ）  
开空：卖出开空（side 填写 sell； posSide 填写 short ）  
平多：卖出平多（side 填写 sell；posSide 填写 long ）  
平空：买入平空（side 填写 buy； posSide 填写 short ）  
组合保证金模式：交割和永续仅支持买卖模式  ordType  
订单类型，创建新订单时必须指定，您指定的订单类型将影响需要哪些订单参数和撮合系统如何执行您的订单，以下是有效的ordType：  
普通委托：  
limit：限价单，要求指定sz 和 px  
market：市价单，币币和币币杠杆，是市价委托吃单；交割合约和永续合约，是自动以最高买/最低卖价格委托，遵循限价机制；期权合约不支持市价委托；由于市价委托无法确定成交价格，为确保有足够的资产买入设定数量的交易币种，会多冻结5%的计价币资产  
高级委托：  
post_only：限价委托，在下单那一刻只做maker，如果该笔订单的任何部分会吃掉当前挂单深度，则该订单将被全部撤销。  
fok：限价委托，全部成交或立即取消，如果无法全部成交该笔订单，则该订单将被全部撤销。  
ioc：限价委托，立即成交并取消剩余，立即按照委托价格撮合成交，并取消该订单剩余未完成数量，不会在深度列表上展示委托数量。  
optimal_limit_ioc：市价委托，立即成交并取消剩余，仅适用于交割合约和永续合约。  sz  
交易数量，表示要购买或者出售的数量。  
当币币/币币杠杆以限价买入和卖出时，指交易货币数量。  
当币币杠杆以市价买入时，指计价货币的数量。  
当币币杠杆以市价卖出时，指交易货币的数量。  
对于币币市价单，单位由 tgtCcy 决定  
当交割、永续、期权买入和卖出时，指合约张数。  reduceOnly  
只减仓，下单时，此参数设置为 true 时，表示此笔订单具有减仓属性，只会减少持仓数量，不会增加新的持仓仓位  
对于同一杠杆产品，所有反方向挂单的币数加上当前只减仓下单数量，不能超过仓位资产；负债还完后，如果还有剩余的委托数量，不会反向开仓，而是会进行币币交易。  
对于同一交割/永续产品，当前只减仓下单张数，加上价格时间优先于当前只减仓下单的只减仓挂单张数总和，不能超过持仓数量  
仅适用于`合约模式`和`跨币种保证金模式`  
仅适用于`币币杠杆`，以及买卖模式下的`交割/永续`  
注意：交割和永续合约在开平仓模式下，所有的平仓单都有只减仓逻辑，不受该字段传值的影响。  tgtCcy  
市价单委托数量`sz`的单位：仅适用于币币市价下单交易。  
交易货币：base_ccy  
计价货币：quote_ccy   
您在使用交易货币买入或者计价货币卖出时，请知晓：   
1.如果您输入的数量大于当前可买或者可卖的数量，系统将按照您的最大可买或者可卖数量帮您完成交易，如果您希望按照指定数量成交，那您可以尝试使用限价单，等待市场价格波动到锁定的余额可以买入或卖出您指定的数量。   
2.如果您输入的数量不大于当前可买或者可卖的数量，那当市场价格波动过大时，锁定的余额可能没办法买入您输入的交易货币数量或卖出您输入的计价货币数量，为保证您的交易体验，我们基于【能买多少买多少】或者【能卖多少卖多少】的原则，更改下单的数量帮您完成交易。此外，我们将尽量多锁定一点余额来规避更改下单数量的情况。   
2.1 交易币买入例子：   
以市价下单 买入 10个LTC为例，用户可买为11个，此时 10 < 11，挂单成功。当LTC-USDT的市价为200，用户被锁定余额为3,000 USDT，200*10 < 3,000，最终成交10个LTC； 若市场波动过大，LTC-USDT的市价为400，此时400*10 > 3,000，当用户被锁定的余额不够买入下单指定的交易货币数量时，系統使用用户被锁定的最大余额3,000 USDT下单买入，最终成交 3,000/400 = 7.5个 LTC。   
2.2 计价币卖出例子：   
以市价下单 卖出 1,000USDT为例，用户可卖为1,200USDT，1,000 < 1,200，挂单成功。LTC-USDT的市价为200，用户被锁定的余额为6个LTC，最终成交5个LTC； 若市场波动过大，LTC-USDT的市价为100，100*6 < 1,000，当用户被锁定的余额不够卖出下单指定的计价货币数量时，系統使用用户被锁定的最大余额6个LTC下单，最终成交 6 * 100 = 600 USDT。  px  
期权下单时，委托价格需为 tickSz 的整数倍。  
当不为整数倍时，取值规则以tickSz取 0.0005 为例：  
当委托价格对0.0005的余数大于0.00025或者委托价格小于0.0005时，向上取；  
当委托价格对0.0005的余数小于等于0.00025，且委托价格大于0.0005时，向下取。  强制自成交保护  
交易系统会以母账户维度实施强制自成交保护，同一母账户下所有账户，包括母账户本身和所有子账户，都无法进行自成交。默认使用账户层面的acctStpMode进行下单，该字段的默认值为`cancel_maker`，用户可通过母账户登录网页修改该配置；用户亦可以通过下单接口的stpMode参数指定订单的STP模式。用户亦可以通过下单接口的stpMode参数指定订单的STP模式。  
强制自成交保护不会导致延迟。  
有三种STP模式。STP模式始终基于taker订单中的配置。  
1.Cancel Maker：这是默认的STP模式，系统撤Maker订单以防止自成交。然后，taker订单会基于深度继续和下一个订单成交。  
2.Cancel Taker：撤Taker订单以防止自成交。如果用户的Maker订单不是深度里第一个订单，Taker订单会被部分成交，然后撤单。FOK订单会确保完全成交和自成交保护。  
3.Cancel Both：撤Taker和Maker订单以防止自成交。如果用户的Maker订单不是深度里第一个订单，Taker订单会被部分成交，然后Taker订单的剩余数量和第一个自我Maker订单被取消。此模式不支持FOK订单。  
isElpTakerAccess:true订单限速  
\- 50个/2s，限制维度为 User ID + Instrument ID  
\- 该限速会在 REST 和 WebSocket 的下单及批量下单接口中共享 

### WS / 批量下单 

批量进行下单操作，每次可批量交易不同类型的产品，最多可下单20个  
  

#### 服务地址

/ws/v5/private (需要登录)

#### 限速：300个/2s

#### 跟单交易带单员带单产品的限速：4个/2s

#### 限速规则（期权以外）：User ID + Instrument ID

#### 限速规则（只限期权）：User ID + Instrument Family

该接口限速同时受到 [子账户限速](/docs-v5/log_zh/#upcoming-changes-sub-account-rate-limit) 及 [基于成交比率的子账户限速](/docs-v5/log_zh/#upcoming-changes-fill-ratio-based-sub-account-rate-limit) 限速规则的影响。

与其他限速按接口调用次数不同，该接口限速按订单的总个数限速。如果单次批量请求中只有一个元素，则算在单个`下单`限速中。  同`批量下单` REST API 共享限速 

> 请求示例
    
    
    {
        "id": "1513",
        "op": "batch-orders",
        "args": [{
            "side": "buy",
            "instIdCode": 123456,
            "tdMode": "isolated",
            "ordType": "market",
            "sz": "100"
        }, {
            "side": "buy",
            "instIdCode": 654321,
            "tdMode": "isolated",
            "ordType": "limit",
            "sz": "1",
            "px": "20000"
        }]
    }
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
id | String | 是 | 消息的唯一标识   
用户提供，返回参数中会返回以便于找到相应的请求。  
字母（区分大小写）与数字的组合，可以是纯字母、纯数字且长度必须要在1-32位之间。  
op | String | 是 | 支持的业务操作，如 `batch-orders`  
args | Array of objects | 是 | 请求参数  
> instIdCode | Integer | 是 | 产品唯一标识代码。  
> tdMode | String | 否 | 交易模式  
保证金模式 `cross`：全仓 `isolated`：逐仓   
非保证金模式 `cash`：现金  
`spot_isolated`：现货逐仓(仅适用于现货带单) ，现货带单时，`tdMode` 的值需要指定为`spot_isolated`  
注意：`isolated` 在跨币种保证金模式和组合保证金模式下不可用。   
  
事件合约对应交易产品仅支持`isolated`逐仓下单  
> ccy | String | 否 | 保证金币种，适用于`逐仓杠杆`及`合约模式`下的`全仓杠杆`订单  
> clOrdId | String | 否 | 用户提供的订单ID  
字母（区分大小写）与数字的组合，可以是纯字母、纯数字且长度要在1-32位之间。  
> tag | String | 否 | 订单标签  
字母（区分大小写）与数字的组合，可以是纯字母、纯数字且长度要在1-16位之间。  
> side | String | 是 | 订单方向， `buy` `sell`  
> posSide | String | 否 | 持仓方向   
在买卖模式下，默认 `net`  
在开平仓模式下必填，且仅可选择 `long` 或 `short`，仅适用于`交割/永续`  
> ordType | String | 是 | 订单类型   
`market`：市价单，仅适用于`币币/杠杆/交割/永续`   
`limit`：限价单  
`post_only`：只做maker单   
`fok`：全部成交或立即取消单   
`ioc`：立即成交并取消剩余单   
`optimal_limit_ioc`：市价委托立即成交并取消剩余（仅适用交割、永续）  
`mmp`：做市商保护(仅适用于组合保证金账户模式下的期权订单)  
`mmp_and_post_only`：做市商保护且只做maker单(仅适用于组合保证金账户模式下的期权订单)   
`elp`：流动性增强计划订单  
> sz | String | 是 | 委托数量  
> px | String | 可选 | 委托价格，仅适用于`limit`、`post_only`、`fok`、`ioc`、`mmp`、`mmp_and_post_only`类型的订单  
期权下单时，px/pxUsd/pxVol 只能填一个  
> speedBump | String | 可选 | 减速带  
`1`：事件合约速度限制（延迟可能因市场情况调整，不提前通知）。对 `EVENTS` 产品的非只挂单操作为必填。  
> outcome | String | 可选 | 用户交易的市场结果方向。  
`yes`  
`no`  
仅适用于 `EVENTS`，且为必填  
> pxUsd | String | 可选 | 以USD价格进行期权下单   
仅适用于期权   
期权下单时 px/pxUsd/pxVol 必填一个，且只能填一个  
> pxVol | String | 可选 | 以隐含波动率进行期权下单，例如 1 代表 100%   
仅适用于期权   
期权下单时 px/pxUsd/pxVol 必填一个，且只能填一个  
> reduceOnly | Boolean | 否 | 是否只减仓，`true` 或 `false`，默认`false`  
仅适用于`币币杠杆`，以及买卖模式下的`交割/永续`  
仅适用于`合约模式`和`跨币种保证金模式`  
> tgtCcy | String | 否 | 币币市价单委托数量`sz`的单位  
`base_ccy`: 交易货币 ；`quote_ccy`：计价货币  
仅适用于`币币`市价订单  
默认买单为`quote_ccy`，卖单为`base_ccy`  
> banAmend | Boolean | 否 | 是否禁止币币市价改单，true 或 false，默认false   
为true时，余额不足时，系统不会改单，下单会失败，仅适用于币币市价单  
> pxAmendType | String | 否 | 订单价格修正类型  
`0`：当`px`超出价格限制时，不允许系统修改订单价格  
`1`：当`px`超出价格限制时，允许系统将价格修改为限制范围内的最优值  
默认值为`0`  
> tradeQuoteCcy | String | 否 | 用于交易的计价币种。仅适用于`币币`。  
默认值为 `instId` 的计价币种，比如：对于 `BTC-USD`，默认取 `USD`。  
> slippagePct | String | 否 | 币币、币币杠杆市价单（`tgtCcy` 为到手币种：买单为 `base_ccy`，卖单为 `quote_ccy`）的最大可接受滑点。  
取值范围：`0` 至 `0.05`（即 0% 至 5%，含边界），以百分比形式表示时最多保留 2 位小数，例如 `0.01`（1%）和 `0.0123`（1.23%）合法；`0.01234`（1.234%）将被拒绝。  
不填或为空时，默认为 `0.00%`。  
不支持改单修改滑点，如需调整请撤单重新提交。  
仅适用于币币和币币杠杆的市价单。  
> stpMode | String | 否 | 自成交保护模式   
`cancel_maker`,`cancel_taker`, `cancel_both`  
Cancel both不支持FOK   
  
默认使用账户层面的acctStpMode进行下单，该字段的默认值为`cancel_maker`，用户可通过母账户登录网页修改该配置；用户亦可以通过下单接口的stpMode参数指定订单的STP模式。  
> isElpTakerAccess | Boolean | 否 | 是否作为 taker 吃单 ELP  
`true`：该请求能吃单 ELP，但会被施加延迟  
`false`：该请求不能吃单 ELP，并且没有延迟  
  
默认值为`false`，`true`仅适用于ioc订单  
expTime | String | 否 | 请求有效截止时间。Unix时间戳的毫秒数格式，如 `1597026383085`  
  
> 全部成功返回示例
    
    
    {
        "id": "1513",
        "op": "batch-orders",
        "data": [{
            "clOrdId": "",
            "ordId": "12345689",
            "tag": "",
            "ts":"1695190491421",
            "sCode": "0",
            "sMsg": "",
            "subCode": ""
        }, {
            "clOrdId": "",
            "ordId": "12344",
            "tag": "",
            "ts":"1695190491421",
            "sCode": "0",
            "sMsg": "",
            "subCode": ""
        }],
        "code": "0",
        "msg": "",
        "inTime": "1695190491421339",
        "outTime": "1695190491423240"
    }
    

> 部分成功返回示例
    
    
    {
        "id": "1513",
        "op": "batch-orders",
        "data": [{
            "clOrdId": "",
            "ordId": "12345689",
            "tag": "",
            "ts":"1695190491421",
            "sCode": "0",
            "sMsg": "",
            "subCode": ""
        }, {
            "clOrdId": "",
            "ordId": "",
            "tag": "",
            "ts":"1695190491421",
            "sCode": "51008",
            "sMsg": "Order failed. Insufficient USDT balance in account",
            "subCode": "1000"
        }],
        "code": "2",
        "msg": "",
        "inTime": "1695190491421339",
        "outTime": "1695190491423240"
    }
    

> 全部失败返回示例
    
    
    {
        "id": "1513",
        "op": "batch-orders",
        "data": [{
            "clOrdId": "oktswap6",
            "ordId": "",
            "tag": "",
            "ts":"1695190491421",
            "sCode": "51008",
            "sMsg": "Order failed. Insufficient USDT balance in account",
            "subCode": "1000"
        }, {
            "clOrdId": "oktswap7",
            "ordId": "",
            "tag": "",
            "ts":"1695190491421",
            "sCode": "51008",
            "sMsg": "Order failed. Insufficient USDT balance in account",
            "subCode": "1000"
        }],
        "code": "1",
        "msg": "",
        "inTime": "1695190491421339",
        "outTime": "1695190491423240"
    }
    

> 格式错误返回示例
    
    
    {
        "id": "1513",
        "op": "batch-orders",
        "data": [],
        "code": "60013",
        "msg": "Invalid args",
        "inTime": "1695190491421339",
        "outTime": "1695190491423240"
    }
    

#### 返回参数

参数 | 类型 | 描述  
---|---|---  
id | String | 消息的唯一标识  
op | String | 业务操作  
code | String | 代码  
msg | String | 消息  
data | Array of objects | 请求成功后返回的数据  
> ordId | String | 订单ID  
> clOrdId | String | 由用户设置的订单ID  
> tag | String | 订单标签  
> ts | String | 系统完成订单请求处理的时间戳，Unix时间戳的毫秒数格式，如 `1597026383085`  
> sCode | String | 订单状态码，0 代表成功  
> sMsg | String | 事件执行失败或成功时的msg  
> subCode | String | sCode 的子码。  
当 sCode 为 0（请求成功）时，返回 `""`。  
当 sCode 不为 0（请求失败）且存在子码时，返回对应的子码；若无子码，则返回 `""`。  
inTime | String | WebSocket 网关接收请求时的时间戳，Unix时间戳的微秒数格式，如 `1597026383085123`  
outTime | String | WebSocket 网关发送响应时的时间戳，Unix时间戳的微秒数格式，如 `1597026383085123`  
在组合保证金账户模式下，或者全部成功，或者全部失败。  clOrdId  
clOrdId是用户自定义的唯一ID用来识别订单。如果在请求参数中传入了，那它一定会在返回参数内，并且可以用于查询订单，撤销订单，修改订单等接口。 clOrdId不能与当前所有挂单和当前请求中的clOrdId重复。  isElpTakerAccess:true订单限速  
\- 50个/2s，限制维度为 User ID + Instrument ID  
\- 该限速会在 REST 和 WebSocket 的下单及批量下单接口中共享 

### WS / 撤单 

撤销当前未完成订单

#### 服务地址

/ws/v5/private (需要登录)

#### 限速：60次/2s

#### 限速规则（期权以外）：User ID + Instrument ID

#### 限速规则（只限期权）：User ID + Instrument Family

同`撤单` REST API 共享限速 

> 请求示例
    
    
    {
        "id": "1514",
        "op": "cancel-order",
        "args": [{
            "instIdCode": 123456,
            "ordId": "2510789768709120"
        }]
    }
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
id | String | 是 | 消息的唯一标识  
用户提供，返回参数中会返回以便于找到相应的请求。  
字母（区分大小写）与数字的组合，可以是纯字母、纯数字且长度必须要在1-32位之间。  
op | String | 是 | 支持的业务操作，如 `cancel-order`  
args | Array of objects | 是 | 请求参数  
> instIdCode | Integer | 是 | 产品唯一标识代码  
> ordId | String | 可选 | 订单ID  
ordId和clOrdId必须传一个，若传两个，以 ordId 为主  
> clOrdId | String | 可选 | 用户提供的订单ID  
字母（区分大小写）与数字的组合，可以是纯字母、纯数字，且长度要在1-32位之间。  
  
> 成功返回示例
    
    
    {
        "id": "1514",
        "op": "cancel-order",
        "data": [{
            "clOrdId": "",
            "ordId": "2510789768709120",
            "ts": "1695190491421",
            "sCode": "0",
            "sMsg": ""
        }],
        "code": "0",
        "msg": "",
        "inTime": "1695190491421339",
        "outTime": "1695190491423240"
    }
    

> 失败返回示例
    
    
    {
        "id": "1514",
        "op": "cancel-order",
        "data": [{
            "clOrdId": "",
            "ordId": "2510789768709120",
            "ts": "1695190491421",
            "sCode": "5XXXX",
            "sMsg": "Order not exist"
        }],
        "code": "1",
        "msg": "",
        "inTime": "1695190491421339",
        "outTime": "1695190491423240"
    }
    

> 格式错误返回示例
    
    
    {
        "id": "1514",
        "op": "cancel-order",
        "data": [],
        "code": "60013",
        "msg": "Invalid args",
        "inTime": "1695190491421339",
        "outTime": "1695190491423240"
    }
    

#### 返回参数

参数 | 类型 | 描述  
---|---|---  
id | String | 消息的唯一标识  
op | String | 业务操作  
code | String | 代码  
msg | String | 消息  
data | Array of objects | 请求成功后返回的数据  
> ordId | String | 订单ID  
> clOrdId | String | 由用户设置的订单ID  
> ts | String | 系统完成订单请求处理的时间戳，Unix时间戳的毫秒数格式，如 `1597026383085`  
> sCode | String | 订单状态码，0 代表成功  
> sMsg | String | 订单状态消息  
inTime | String | WebSocket 网关接收请求时的时间戳，Unix时间戳的微秒数格式，如 `1597026383085123`  
outTime | String | WebSocket 网关发送响应时的时间戳，Unix时间戳的微秒数格式，如 `1597026383085123`  
撤单返回sCode等于0不能严格认为该订单已经被撤销，只表示您的撤单请求被系统服务器所接受，撤单结果以订单频道推送的状态或者查询订单状态为准  

### WS / 批量撤单 

批量进行撤单操作，每次可批量撤销不同类型的产品，最多撤销20个

#### 服务地址

/ws/v5/private (需要登录)

#### 限速：300个/2s

#### 限速规则（期权以外）：User ID + Instrument ID

#### 限速规则（只限期权）：User ID + Instrument Family

与其他限速按接口调用次数不同，该接口限速按订单的总个数限速。如果单次批量请求中只有一个元素，则算在单个`撤单`限速中。  同`批量撤单` REST API 共享限速 

> 请求示例
    
    
    {
        "id": "1515",
        "op": "batch-cancel-orders",
        "args": [{
            "instIdCode": 123456,
            "ordId": "2517748157541376"
        }, {
            "instIdCode": 654321,
            "ordId": "2517748155771904"
        }]
    }
    

#### 请求参数

参数 | 类型 | 是否必须 | 描述  
---|---|---|---  
id | String | 是 | 消息的唯一标识  
用户提供，返回参数中会返回以便于找到相应的请求。  
字母（区分大小写）与数字的组合，可以是纯字母、纯数字且长度必须要在1-32位之间。  
op | String | 是 | 支持的业务操作，如 `batch-cancel-orders`  
args | Array of objects | 是 | 请求参数  
> instIdCode | Integer | 是 | 产品唯一标识代码  
> ordId | String | 可选 | 订单ID  
ordId和clOrdId必须传一个，若传两个，以ordId 为主  
> clOrdId | String | 可选 | 用户提供的订单ID  
字母（区分大小写）与数字的组合，可以是纯字母、纯数字，且长度要在1-32位之间。  
  
> 全部成功返回示例
    
    
    {
        "id": "1515",
        "op": "batch-cancel-orders",
        "data": [{
            "clOrdId": "oktswap6",
            "ordId": "2517748157541376",
            "ts": "1695190491421",
            "sCode": "0",
            "sMsg": ""
        }, {
            "clOrdId": "oktswap7",
            "ordId": "2517748155771904",
            "ts": "1695190491421",
            "sCode": "0",
            "sMsg": ""
        }],
        "code": "0",
        "msg": "",
        "inTime": "1695190491421339",
        "outTime": "1695190491423240"
    }
    

> 部分成功的返回示例
    
    
    {
        "id": "1515",
        "op": "batch-cancel-orders",
        "data": [{
            "clOrdId": "oktswap6",
            "ordId": "2517748157541376",
            "ts": "1695190491421",
            "sCode": "0",
            "sMsg": ""
        }, {
            "clOrdId": "oktswap7",
            "ordId": "2517748155771904",
            "ts": "1695190491421",
            "sCode": "5XXXX",
            "sMsg": "order not exist"
        }],
        "code": "2",
        "msg": "",
        "inTime": "1695190491421339",
        "outTime": "1695190491423240"
    }
    

> 全部失败的返回示例
    
    
    {
        "id": "1515",
        "op": "batch-cancel-orders",
        "data": [{
            "clOrdId": "oktswap6",
            "ordId": "2517748157541376",
            "ts": "1695190491421",
            "sCode": "5XXXX",
            "sMsg": "order not exist"
        }, {
            "clOrdId": "oktswap7",
            "ordId": "2517748155771904",
            "ts": "1695190491421",
            "sCode": "5XXXX",
            "sMsg": "order not exist"
        }],
        "code": "1",
        "msg": "",
        "inTime": "1695190491421339",
        "outTime": "1695190491423240"
    }
    

> 格式错误示例
    
    
    {
        "id": "1515",
        "op": "batch-cancel-orders",
        "data": [],
        "code": "60013",
        "msg": "Invalid args",
        "inTime": "1695190491421339",
        "outTime": "1695190491423240"
    }
    

#### 返回参数

参数 | 类型 | 描述  
---|---|---  
id | String | 消息的唯一标识  
op | String | 业务操作  
code | String | 代码  
msg | String | 消息  
data | Array of objects | 请求成功后返回的数据  
> ordId | String | 订单ID  
> clOrdId | String | 由用户设置的订单ID  
> ts | String | 系统完成订单请求处理的时间戳，Unix时间戳的毫秒数格式，如 `1597026383085`  
> sCode | String | 订单状态码，0 代表成功  
> sMsg | String | 订单状态消息  
inTime | String | WebSocket 网关接收请求时的时间戳，Unix时间戳的微秒数格式，如 `1597026383085123`  
outTime | String | WebSocket 网关发送响应时的时间戳，Unix时间戳的微秒数格式，如 `1597026383085123`  
  
### WS / 改单 

修改当前未成交的订单

#### 服务地址

/ws/v5/private (需要登录)

#### 限速：60次/2s

#### 跟单交易带单员带单产品的限速：4次/2s

#### 限速规则（期权以外）：User ID + Instrument ID

#### 限速规则（只限期权）：User ID + Instrument Family

该接口限速同时受到 [子账户限速](/docs-v5/log_zh/#upcoming-changes-sub-account-rate-limit) 及 [基于成交比率的子账户限速](/docs-v5/log_zh/#upcoming-changes-fill-ratio-based-sub-account-rate-limit) 限速规则的影响。

同`改单` REST API 共享限速 

> 请求示例
    
    
    {
        "id": "1512",
        "op": "amend-order",
        "args": [{
            "instIdCode": 123456,
            "ordId": "2510789768709120",
            "newSz": "2"
        }]
    }
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
id | String | 是 | 消息的唯一标识   
用户提供，返回参数中会返回以便于找到相应的请求。  
字母（区分大小写）与数字的组合，可以是纯字母、纯数字且长度必须要在1-32位之间。  
op | String | 是 | 支持的业务操作，如 `amend-order`  
args | Array of objects | 是 | 请求参数  
> instIdCode | Integer | 是 | 产品唯一标识代码  
> cxlOnFail | Boolean | 否 | 当订单修改失败时，该订单是否需要自动撤销。默认为`false`  
`false`：不自动撤单  
`true`：自动撤单  
> ordId | String | 可选 | 订单ID  
ordId和clOrdId必须传一个，若传两个，以 ordId 为主  
> clOrdId | String | 可选 | 用户提供的订单ID  
> reqId | String | 否 | 用户提供的reqId  
如果提供，那在返回参数中返回reqId，方便找到相应的修改请求。  
字母（区分大小写）与数字的组合，可以是纯字母、纯数字且长度要在1-32位之间。  
> newSz | String | 可选 | 请求修改的新数量，必须大于0。`newSz`和`newPx`不可同时为空。对于部分成交订单，该数量应包含已成交数量。  
> newPx | String | 可选 | 修改后的新价格  
修改的新价格期权改单时，newPx/newPxUsd/newPxVol 只能填一个，且必须与下单参数保持一致，如下单用px，改单时需使用newPx  
> speedBump | String | 可选 | 减速带  
`1`：事件合约速度限制（延迟可能因市场情况调整，不提前通知）。对 `EVENTS` 产品的非只挂单操作为必填。  
> newPxUsd | String | 可选 | 以USD价格进行期权改单   
仅适用于期权，期权改单时，newPx/newPxUsd/newPxVol 只能填一个  
> newPxVol | String | 可选 | 以隐含波动率进行期权改单，例如 1 代表 100%   
仅适用于期权，期权改单时，newPx/newPxUsd/newPxVol 只能填一个  
> pxAmendType | String | 否 | 订单价格修正类型  
`0`：当`newPx`超出价格限制时，不允许系统修改订单价格  
`1`：当`newPx`超出价格限制时，允许系统将价格修改为限制范围内的最优值  
默认值为`0`  
expTime | String | 否 | 请求有效截止时间。Unix时间戳的毫秒数格式，如 `1597026383085`  
  
> 成功返回示例
    
    
    {
        "id": "1512",
        "op": "amend-order",
        "data": [{
            "clOrdId": "",
            "ordId": "2510789768709120",
            "ts": "1695190491421",
            "reqId": "b12344",
            "sCode": "0",
            "sMsg": "",
            "subCode": ""
        }],
        "code": "0",
        "msg": "",
        "inTime": "1695190491421339",
        "outTime": "1695190491423240"
    } 
    

> 失败返回示例
    
    
    {
        "id": "1512",
        "op": "amend-order",
        "data": [{
            "clOrdId": "",
            "ordId": "2510789768709120",
            "ts": "1695190491421",
            "reqId": "b12344",
            "sCode": "51008",
            "sMsg": "Order failed. Insufficient USDT balance in account",
            "subCode": "1000"
        }],
        "code": "1",
        "msg": "",
        "inTime": "1695190491421339",
        "outTime": "1695190491423240"
    }
    

> 格式错误返回示例
    
    
    {
        "id": "1512",
        "op": "amend-order",
        "data": [],
        "code": "60013",
        "msg": "Invalid args",
        "inTime": "1695190491421339",
        "outTime": "1695190491423240"
    
    }
    

#### 返回参数

参数 | 类型 | 描述  
---|---|---  
id | String | 消息的唯一标识  
op | String | 业务操作  
code | String | 代码  
msg | String | 消息  
data | Array of objects | 请求成功后返回的数据  
> ordId | String | 订单ID  
> clOrdId | String | 用户提供的订单ID  
> ts | String | 系统完成订单请求处理的时间戳，Unix时间戳的毫秒数格式，如 `1597026383085`  
> reqId | String | 用户提供的reqId  
如果用户在请求中提供reqId，则返回相应reqId  
> sCode | String | 订单状态码，0 代表成功  
> sMsg | String | 订单状态消息  
> subCode | String | sCode 的子码。  
当 sCode 为 0（请求成功）时，返回 `""`。  
当 sCode 不为 0（请求失败）且存在子码时，返回对应的子码；若无子码，则返回 `""`。  
inTime | String | WebSocket 网关接收请求时的时间戳，Unix时间戳的微秒数格式，如 `1597026383085123`  
outTime | String | WebSocket 网关发送响应时的时间戳，Unix时间戳的微秒数格式，如 `1597026383085123`  
  
newSz : 当修改已经部分成交的订单时，新的委托数量必须大于等于已成交数量 

修改订单返回sCode等于0不能严格认为该订单已经被修改，只表示您的修改订单请求被系统服务器所接受，改单结果以订单频道推送的状态或者查询订单状态为准  

### WS / 批量改单 

批量进行改单操作，每次可批量修改不同类型的产品，最多改20个

#### 服务地址

/ws/v5/private (需要登录)

#### 限速：300个/2s

#### 跟单交易带单员带单产品的限速：4个/2s

#### 限速规则（期权以外）：User ID + Instrument ID

#### 限速规则（只限期权）：User ID + Instrument Family

该接口限速同时受到 [子账户限速](/docs-v5/log_zh/#upcoming-changes-sub-account-rate-limit) 及 [基于成交比率的子账户限速](/docs-v5/log_zh/#upcoming-changes-fill-ratio-based-sub-account-rate-limit) 限速规则的影响。

与其他限速按接口调用次数不同，该接口限速按订单的总个数限速。如果单次批量请求中只有一个元素，则算在单个`修改订单`限速中。  同`批量改单` REST API 共享限速 

> 请求示例
    
    
    {
        "id": "1513",
        "op": "batch-amend-orders",
        "args": [{
            "instIdCode": 123456,
            "ordId": "12345689",
            "newSz": "2"
        }, {
            "instIdCode": 123456,
            "ordId": "12344",
            "newSz": "2"
        }]
    }
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
id | String | 是 | 消息的唯一标识   
用户提供，返回参数中会返回以便于找到相应的请求。  
字母（区分大小写）与数字的组合，可以是纯字母、纯数字且长度必须要在1-32位之间。  
op | String | 是 | 支持的业务操作，如 `batch-amend-orders`  
args | Array of objects | 是 | 请求参数  
> instIdCode | Integer | 是 | 产品唯一标识代码  
> cxlOnFail | Boolean | 否 | 当订单修改失败时，该订单是否需要自动撤销。默认为`false`  
`false`：不自动撤单  
`true`：自动撤单  
> ordId | String | 可选 | 订单ID  
ordId 和 clOrdId 必须传一个，若传两个，以order id 为主  
> clOrdId | String | 可选 | 用户提供的订单ID  
> reqId | String | 否 | 用户提供的请求ID  
如果提供，那在返回参数中返回reqId，方便找到相应的修改请求。  
字母（区分大小写）与数字的组合，可以是纯字母、纯数字且长度要在1-32位之间。  
> newSz | String | 可选 | 修改后的新数量，必须大于0。`newSz`和`newPx`不可同时为空。对于部分成交订单，该数量应包含已成交数量。  
> newPx | String | 可选 | 修改后的新价格  
修改的新价格期权改单时，newPx/newPxUsd/newPxVol 只能填一个，且必须与下单参数保持一致，如下单用px，改单时需使用newPx  
> speedBump | String | 可选 | 减速带  
`1`：事件合约速度限制（延迟可能因市场情况调整，不提前通知）。对 `EVENTS` 产品的非只挂单操作为必填。  
> newPxUsd | String | 可选 | 以USD价格进行期权改单   
仅适用于期权，期权改单时，newPx/newPxUsd/newPxVol 只能填一个  
> newPxVol | String | 可选 | 以隐含波动率进行期权改单，例如 1 代表 100%   
仅适用于期权，期权改单时，newPx/newPxUsd/newPxVol 只能填一个  
> pxAmendType | String | 否 | 订单价格修正类型  
`0`：当`newPx`超出价格限制时，不允许系统修改订单价格  
`1`：当`newPx`超出价格限制时，允许系统将价格修改为限制范围内的最优值  
默认值为`0`  
expTime | String | 否 | 请求有效截止时间。Unix时间戳的毫秒数格式，如 `1597026383085`  
  
> 全部成功返回示例
    
    
    {
        "id": "1513",
        "op": "batch-amend-orders",
        "data": [{
            "clOrdId": "oktswap6",
            "ordId": "12345689",
            "ts": "1695190491421",
            "reqId": "b12344",
            "sCode": "0",
            "sMsg": "",
            "subCode": ""
        }, {
            "clOrdId": "oktswap7",
            "ordId": "12344",
            "ts": "1695190491421",
            "reqId": "b12344",
            "sCode": "0",
            "sMsg": "",
            "subCode": ""
        }],
        "code": "0",
        "msg": "",
        "inTime": "1695190491421339",
        "outTime": "1695190491423240"
    }
    

> 全部失败返回示例
    
    
    {
        "id": "1513",
        "op": "batch-amend-orders",
        "data": [{
            "clOrdId": "",
            "ordId": "12345689",
            "ts": "1695190491421",
            "reqId": "b12344",
            "sCode": "51008",
            "sMsg": "Order failed. Insufficient USDT balance in account",
            "subCode": "1000"
        }, {
            "clOrdId": "oktswap7",
            "ordId": "",
            "ts": "1695190491421",
            "reqId": "b12344",
            "sCode": "51008",
            "sMsg": "Order failed. Insufficient USDT balance in account",
            "subCode": "1000"
        }],
        "code": "1",
        "msg": "",
        "inTime": "1695190491421339",
        "outTime": "1695190491423240"
    }
    

> 部分成功返回示例
    
    
    {
        "id": "1513",
        "op": "batch-amend-orders",
        "data": [{
            "clOrdId": "",
            "ordId": "12345689",
            "ts": "1695190491421",
            "reqId": "b12344",
            "sCode": "0",
            "sMsg": "",
            "subCode": ""
    
        }, {
            "clOrdId": "oktswap7",
            "ordId": "",
            "ts": "1695190491421",
            "reqId": "b12344",
            "sCode": "51008",
            "sMsg": "Order failed. Insufficient USDT balance in account",
            "subCode": "1000"
        }],
        "code": "2",
        "msg": "",
        "inTime": "1695190491421339",
        "outTime": "1695190491423240"
    }
    

> 格式错误返回示例
    
    
    {
        "id": "1513",
        "op": "batch-amend-orders",
        "data": [],
        "code": "60013",
        "msg": "Invalid args",
        "inTime": "1695190491421339",
        "outTime": "1695190491423240"
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
id | String | 消息的唯一标识  
op | String | 业务操作  
code | String | 代码  
msg | String | 消息  
data | Array of objects | 请求成功后返回的数据  
> ordId | String | 订单ID  
> clOrdId | String | 由用户设置的订单ID  
> ts | String | 系统完成订单请求处理的时间戳，Unix时间戳的毫秒数格式，如 `1597026383085`  
> reqId | String | 用户提供的请求ID  
如果用户在请求中提供reqId，则返回相应reqId  
> sCode | String | 订单状态码，0 代表成功  
> sMsg | String | 订单状态消息  
> subCode | String | sCode 的子码。  
当 sCode 为 0（请求成功）时，返回 `""`。  
当 sCode 不为 0（请求失败）且存在子码时，返回对应的子码；若无子码，则返回 `""`。  
inTime | String | WebSocket 网关接收请求时的时间戳，Unix时间戳的微秒数格式，如 `1597026383085123`  
outTime | String | WebSocket 网关发送响应时的时间戳，Unix时间戳的微秒数格式，如 `1597026383085123`  
  
### WS / 撤销 MMP 订单 

撤销同一交易品种下用户所有的 MMP 挂单  
仅适用于组合保证金账户模式下的期权订单，且有 MMP 权限。

#### 服务地址

/ws/v5/private (需要登录)

#### 限速：5次/2s

#### 限速规则：User ID

同`撤销 MMP 订单` REST API 共享限速 

> 请求示例
    
    
    {
        "id": "1512",
        "op": "mass-cancel",
        "args": [{
            "instType":"OPTION",
            "instFamily":"BTC-USD"
        }]
    }
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
id | String | 是 | 消息的唯一标识   
用户提供，返回参数中会返回以便于找到相应的请求。  
字母（区分大小写）与数字的组合，可以是纯字母、纯数字且长度必须要在1-32位之间。  
op | String | 是 | 支持的业务操作，如 `mass-cancel`  
args | Array of objects | 是 | 请求参数  
> instType | String | 是 | 交易产品类型  
`OPTION`:期权  
> instFamily | String | 是 | 交易品种  
> lockInterval | String | 否 | 锁定时长(毫秒)  
范围应为[0, 10 000]  
默认为 0. 如果想要立即解锁，您可以设置为 "0"  
下单时，如果在该锁定期间，会报错 54008，如果在 MMP 触发期间，会报错 51034  
  
> 成功返回示例
    
    
    {
        "id": "1512",
        "op": "mass-cancel",
        "data": [
            {
                "result": true
            }
        ],
        "code": "0",
        "msg": ""
    } 
    

> 格式错误返回示例
    
    
    {
        "id": "1512",
        "op": "mass-cancel",
        "data": [],
        "code": "60013",
        "msg": "Invalid args"
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
id | String | 消息的唯一标识  
op | String | 业务操作  
code | String | 代码  
msg | String | 消息  
data | Array of objects | 请求成功后返回的数据  
> result | Boolean | 撤单结果  
`true`：全部撤单成功  
`false`：全部撤单失败