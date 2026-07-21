---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#order-book-trading-trade-post-place-multiple-orders
anchor_id: order-book-trading-trade-post-place-multiple-orders
api_type: API
updated_at: 2026-07-21 19:25:33.750048
---

# POST / Place multiple orders

Place orders in batches. Maximum 20 orders can be placed per request.   
Request parameters should be passed in the form of an array. Orders will be placed in turn  

#### Rate Limit: 300 orders per 2 seconds

#### Rate Limit of lead trader lead instruments for Copy Trading: 4 orders per 2 seconds

#### Rate limit rule (except Options): User ID + Instrument ID

#### Rate limit rule (Options only): User ID + Instrument Family

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
> ts | String | Order creation time. Unix timestamp format in milliseconds, e.g. `1597026383085`. Equivalent to `cTime` in the order channel.  
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

---

# POST / 批量下单

每次最多可以批量提交20个新订单。请求参数应该按数组格式传递，会依次委托订单。  
  

#### 限速：300个/2s

#### 跟单交易带单员带单产品的限速：4个/2s

#### 限速规则（期权以外）：User ID + Instrument ID

#### 限速规则（只限期权）：User ID + Instrument Family

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
> ts | String | 订单创建时间，Unix时间戳的毫秒数格式，如 `1597026383085`。与订单频道中的 `cTime` 相同。  
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