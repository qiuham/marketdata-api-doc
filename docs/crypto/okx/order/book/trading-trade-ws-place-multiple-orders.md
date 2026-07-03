---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#order-book-trading-trade-ws-place-multiple-orders
anchor_id: order-book-trading-trade-ws-place-multiple-orders
api_type: WebSocket
updated_at: 2026-07-03 19:39:14.463471
---

# WS / Place multiple orders

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

---

# WS / 批量下单

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