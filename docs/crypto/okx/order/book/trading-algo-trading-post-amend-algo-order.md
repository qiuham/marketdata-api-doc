---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#order-book-trading-algo-trading-post-amend-algo-order
anchor_id: order-book-trading-algo-trading-post-amend-algo-order
api_type: API
updated_at: 2026-07-01 19:53:56.305317
---

# POST / Amend algo order

Amend unfilled algo orders (Support Stop order and Trigger order only, not including Move_order_stop order, Iceberg order, TWAP order, Trailing Stop order).  
  
  
#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: User ID + Instrument ID

#### Permission: Trade

#### HTTP Request

`POST /api/v5/trade/amend-algos`

> Request Example
    
    
    POST /api/v5/trade/amend-algos
    body
    {
        "algoId":"2510789768709120",
        "newSz":"2",
        "instId":"BTC-USDT"
    }
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
instId | String | Yes | Instrument ID  
algoId | String | Conditional | Algo ID  
Either `algoId` or `algoClOrdId` is required. If both are passed, `algoId` will be used.  
algoClOrdId | String | Conditional | Client-supplied Algo ID  
Either `algoId` or `algoClOrdId` is required. If both are passed, `algoId` will be used.  
cxlOnFail | Boolean | No | Whether the order needs to be automatically canceled when the order amendment fails   
Valid options: `false` or `true`, the default is `false`.  
reqId | String | Conditional | Client Request ID as assigned by the client for order amendment   
A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters.   
The response will include the corresponding `reqId` to help you identify the request if you provide it in the request.  
newSz | String | Conditional | New quantity after amendment and it has to be larger than 0.  
  
**Take Profit / Stop Loss Order**

Parameter | Type | Required | Description  
---|---|---|---  
newTpTriggerPx | String | Conditional | Take-profit trigger price.   
Either the take-profit trigger price or order price is 0, it means that the take-profit is deleted  
newTpOrdPx | String | Conditional | Take-profit order price   
If the price is -1, take-profit will be executed at the market price.  
newSlTriggerPx | String | Conditional | Stop-loss trigger price.  
Either the stop-loss trigger price or order price is 0, it means that the stop-loss is deleted  
newSlOrdPx | String | Conditional | Stop-loss order price   
If the price is -1, stop-loss will be executed at the market price.  
newTpTriggerPxType | String | Conditional | Take-profit trigger price type  
`last`: last price   
`index`: index price   
`mark`: mark price  
newSlTriggerPxType | String | Conditional | Stop-loss trigger price type  
`last`: last price   
`index`: index price   
`mark`: mark price  
  
**Trigger Order**

Parameter | Type | Required | Description  
---|---|---|---  
newTriggerPx | String | Yes | New trigger price after amendment  
newOrdPx | String | Yes | New order price after amendment  
If the price is `-1`, the order will be executed at the market price.  
newTriggerPxType | String | No | New trigger price type after amendment   
`last`: last price  
`index`: index price  
`mark`: mark price   
The default is `last`  
attachAlgoOrds | Array of objects | No | Attached TP/SL or trailing stop order info  
Applicable to `Futures mode/Multi-currency margin/Portfolio margin`  
> newTpTriggerPx | String | No | Take-profit trigger price  
If you fill in this parameter, you should fill in the take-profit order price as well.  
> newTpTriggerRatio | String | No | Take profit trigger ratio, 0.3 represents 30%   
Only applicable to FUTURES and SWAP.   
Only one of `newTpTriggerPx` and `newTpTriggerRatio` can be passed   
If the main order is a buy order, it must be greater than 0, and if the main order is a sell order, it must be between -1 and 0.   
0 means to delete the take-profit.  
> newTpTriggerPxType | String | No | Take-profit trigger price type  
`last`: last price  
`index`: index price  
`mark`: mark price  
The default is `last`  
> newTpOrdPx | String | No | Take-profit order price  
If you fill in this parameter, you should fill in the take-profit trigger price as well.   
If the price is `-1`, take-profit will be executed at the market price.  
> newSlTriggerPx | String | No | Stop-loss trigger price  
If you fill in this parameter, you should fill in the stop-loss order price.  
> newSlTriggerRatio | String | No | Stop-loss trigger ratio, 0.3 represents 30%   
Only applicable to FUTURES and SWAP.   
Only one of `newSlTriggerPx` and `newSlTriggerRatio` can be passed   
If the main order is a buy order, it must be between 0 and 1, and if the main order is a sell order, it must be greater than 0.   
0 means to delete the stop-loss.  
> newSlTriggerPxType | String | No | Stop-loss trigger price type  
`last`: last price  
`index`: index price  
`mark`: mark price   
The default is `last`  
> newSlOrdPx | String | No | Stop-loss order price   
If you fill in this parameter, you should fill in the stop-loss trigger price.   
If the price is `-1`, stop-loss will be executed at the market price.  
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
                "algoClOrdId":"algo_01",
                "algoId":"2510789768709120",
                "reqId":"po103ux",
                "sCode":"0",
                "sMsg":""
            }
        ]
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
algoId | String | Algo ID  
algoClOrdId | String | Client-supplied Algo ID  
reqId | String | Client Request ID as assigned by the client for order amendment.  
sCode | String | The code of the event execution result, `0` means success.  
sMsg | String | Rejection message if the request is unsuccessful.

---

# POST / 修改策略委托订单

修改策略委托订单（仅支持止盈止损和计划委托订单，不包含、冰山委托、时间加权、移动止盈止损等订单）  
  
  
#### 限速：20次/2s

#### 限速规则：User ID + Instrument ID

#### 权限：交易

#### HTTP请求

`POST /api/v5/trade/amend-algos`

> 请求示例
    
    
    POST /api/v5/trade/amend-algos
    body
    {
        "algoId":"2510789768709120",
        "newSz":"2",
        "instId":"BTC-USDT"
    }
    
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
instId | String | 是 | 产品ID  
algoId | String | 可选 | 策略委托单ID  
`algoId`和`algoClOrdId`必须传一个，若传两个，以`algoId`为主  
algoClOrdId | String | 可选 | 客户自定义策略订单ID  
`algoId`和`algoClOrdId`必须传一个，若传两个，以`algoId`为主  
cxlOnFail | Boolean | 否 | 当订单修改失败时，该订单是否需要自动撤销。默认为`false`  
`false`：不自动撤单  
`true`：自动撤单  
reqId | String | 否 | 用户自定义修改事件ID，字母（区分大小写）与数字的组合，可以是纯字母、纯数字且长度要在1-32位之间  
newSz | String | 可选 | 修改的新数量，必须大于0。  
  
**止盈止损**

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
newTpTriggerPx | String | 可选 | 止盈触发价  
如果止盈触发价或者委托价为0，那代表删除止盈  
newTpOrdPx | String | 可选 | 止盈委托价  
委托价格为-1时，执行市价止盈  
newSlTriggerPx | String | 可选 | 止损触发价  
如果止损触发价或者委托价为0，那代表删除止损  
newSlOrdPx | String | 可选 | 止损委托价  
委托价格为-1时，执行市价止损  
newTpTriggerPxType | String | 可选 | 止盈触发价类型  
`last`：最新价格  
`index`：指数价格  
`mark`：标记价格  
newSlTriggerPxType | String | 可选 | 止损触发价类型  
`last`：最新价格  
`index`：指数价格  
`mark`：标记价格  
  
**计划委托**

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
newTriggerPx | String | 是 | 修改后的触发价格  
newOrdPx | String | 是 | 修改后的委托价格   
委托价格为`-1`时，执行市价委托  
newTriggerPxType | String | 否 | 修改后的计划委托触发价格类型  
`last`：最新价格  
`index`：指数价格  
`mark`：标记价格  
默认为`last`  
attachAlgoOrds | Array of objects | 否 | 修改附带止盈止损或移动止盈止损订单信息  
适用于`合约模式/跨币种保证金模式/组合保证金模式`  
> newTpTriggerPx | String | 否 | 止盈触发价，如果填写此参数，必须填写`止盈委托价`  
> newTpTriggerRatio | String | 否 | 止盈触发比例，0.3 代表 30%   
仅适用于`交割`/`永续`合约  
`newTpTriggerPx` 和 `newTpTriggerRatio` 只能传入其中一个  
如果主单为买入订单，必须大于 0，如果主单为卖出订单，必须处于 -1 和 0 之间。0 代表删除止盈。  
> newTpTriggerPxType | String | 否 | 修改后的止盈触发价类型  
`last`：最新价格  
`index`：指数价格  
`mark`：标记价格  
默认为`last`  
> newTpOrdPx | String | 否 | 止盈委托价，如果填写此参数，必须填写`止盈触发价`  
委托价格为`-1`时，执行市价止盈  
> newSlTriggerPx | String | 否 | 止损触发价，如果填写此参数，必须填写`止损委托价`  
> newSlTriggerRatio | String | 否 | 止损触发比例，0.3 代表 30%   
仅适用于`交割`/`永续`合约  
`newSlTriggerPx` 和 `newSlTriggerRatio` 只能传入其中一个  
如果主单为买入订单，必须处于 0 和 1 之间，如果主单为卖出订单，必须大于 0。0 代表删除止损。  
> newSlTriggerPxType | String | 否 | 止损触发价类型  
`last`：最新价格  
`index`：指数价格  
`mark`：标记价格  
默认为`last`  
> newSlOrdPx | String | 否 | 止损委托价，如果填写此参数，必须填写`止损触发价`  
委托价格为`-1`时，执行市价止损  
> newCallbackRatio | String | 可选 | 新的回调幅度比例，如 `0.05` 代表 5%。  
`newCallbackRatio` 和 `newCallbackSpread` 只能传入其中一个。  
仅适用于 `ordType` = `move_order_stop`  
> newCallbackSpread | String | 可选 | 新的回调幅度价距。  
`newCallbackRatio` 和 `newCallbackSpread` 只能传入其中一个。  
仅适用于 `ordType` = `move_order_stop`  
> newActivePx | String | 否 | 新的激活价格。  
仅适用于 `ordType` = `move_order_stop`  
  
> 返回结果
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
            {
                "algoClOrdId":"algo_01",
                "algoId":"2510789768709120",
                "reqId":"po103ux",
                "sCode":"0",
                "sMsg":""
            }
        ]
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
algoId | String | 订单ID  
algoClOrdId | String | 客户自定义策略订单ID  
reqId | String | 用户自定义修改事件ID，字母（区分大小写）与数字的组合，可以是纯字母、纯数字且长度要在1-32位之间  
sCode | String | 事件执行结果的code，0代表成功  
sMsg | String | 事件执行失败时的msg