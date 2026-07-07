---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#order-book-trading-trade-post-amend-multiple-orders
anchor_id: order-book-trading-trade-post-amend-multiple-orders
api_type: API
updated_at: 2026-07-07 19:41:41.352036
---

# POST / Amend multiple orders

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

---

# POST / 批量修改订单

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