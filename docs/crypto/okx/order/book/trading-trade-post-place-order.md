---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#order-book-trading-trade-post-place-order
anchor_id: order-book-trading-trade-post-place-order
api_type: API
updated_at: 2026-07-03 19:39:05.235034
---

# POST / Place order

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

---

# POST / 下单

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