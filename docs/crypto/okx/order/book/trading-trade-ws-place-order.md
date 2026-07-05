---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#order-book-trading-trade-ws-place-order
anchor_id: order-book-trading-trade-ws-place-order
api_type: WebSocket
updated_at: 2026-07-05 19:33:38.271545
---

# WS / Place order

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

---

# WS / 下单

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