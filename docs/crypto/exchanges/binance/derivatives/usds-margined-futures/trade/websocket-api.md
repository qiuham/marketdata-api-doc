---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/usds-margined-futures/trade/websocket-api
api_type: WebSocket
updated_at: 2026-01-15T23:47:34.811238
---

# New Order(TRADE)

## API Description[​](/docs/derivatives/usds-margined-futures/trade/websocket-api#api-description "Direct link to API Description")

Send in a new order.

## Method[​](/docs/derivatives/usds-margined-futures/trade/websocket-api#method "Direct link to Method")

`order.place`

## Request[​](/docs/derivatives/usds-margined-futures/trade/websocket-api#request "Direct link to Request")
    
    
    {  
        "id": "3f7df6e3-2df4-44b9-9919-d2f38f90a99a",  
        "method": "order.place",  
        "params": {  
            "apiKey": "HMOchcfii9ZRZnhjp2XjGXhsOBd6msAhKz9joQaWwZ7arcJTlD2hGPHQj1lGdTjR",  
            "positionSide": "BOTH",  
            "price": 43187.00,  
            "quantity": 0.1,  
            "side": "BUY",  
            "symbol": "BTCUSDT",  
            "timeInForce": "GTC",  
            "timestamp": 1702555533821,  
            "type": "LIMIT",  
            "signature": "0f04368b2d22aafd0ggc8809ea34297eff602272917b5f01267db4efbc1c9422"  
        }  
    }  
    

## Request Weight[​](/docs/derivatives/usds-margined-futures/trade/websocket-api#request-weight "Direct link to Request Weight")

**0**

## Request Parameters[​](/docs/derivatives/usds-margined-futures/trade/websocket-api#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
symbol| STRING| YES|   
side| ENUM| YES|   
positionSide| ENUM| NO| Default `BOTH` for One-way Mode ; `LONG` or `SHORT` for Hedge Mode. It must be sent in Hedge Mode.  
type| ENUM| YES|   
timeInForce| ENUM| NO|   
quantity| DECIMAL| NO| Cannot be sent with `closePosition`=`true`(Close-All)  
reduceOnly| STRING| NO| "true" or "false". default "false". Cannot be sent in Hedge Mode; cannot be sent with `closePosition`=`true`  
price| DECIMAL| NO|   
newClientOrderId| STRING| NO| A unique id among open orders. Automatically generated if not sent. Can only be string following the rule: `^[\.A-Z\:/a-z0-9_-]{1,36}$`  
stopPrice| DECIMAL| NO| Used with `STOP/STOP_MARKET` or `TAKE_PROFIT/TAKE_PROFIT_MARKET` orders.  
closePosition| STRING| NO| `true`, `false`；Close-All，used with `STOP_MARKET` or `TAKE_PROFIT_MARKET`.  
activationPrice| DECIMAL| NO| Used with `TRAILING_STOP_MARKET` orders, default as the latest price(supporting different `workingType`)  
callbackRate| DECIMAL| NO| Used with `TRAILING_STOP_MARKET` orders, min 0.1, max 10 where 1 for 1%  
workingType| ENUM| NO| stopPrice triggered by: "MARK_PRICE", "CONTRACT_PRICE". Default "CONTRACT_PRICE"  
priceProtect| STRING| NO| "TRUE" or "FALSE", default "FALSE". Used with `STOP/STOP_MARKET` or `TAKE_PROFIT/TAKE_PROFIT_MARKET` orders.  
newOrderRespType| ENUM| NO| "ACK", "RESULT", default "ACK"  
priceMatch| ENUM| NO| only avaliable for `LIMIT`/`STOP`/`TAKE_PROFIT` order; can be set to `OPPONENT`/ `OPPONENT_5`/ `OPPONENT_10`/ `OPPONENT_20`: /`QUEUE`/ `QUEUE_5`/ `QUEUE_10`/ `QUEUE_20`; Can't be passed together with `price`  
selfTradePreventionMode| ENUM| NO| `NONE`:No STP / `EXPIRE_TAKER`:expire taker order when STP triggers/ `EXPIRE_MAKER`:expire taker order when STP triggers/ `EXPIRE_BOTH`:expire both orders when STP triggers; default `NONE`  
goodTillDate| LONG| NO| order cancel time for timeInForce `GTD`, mandatory when `timeInforce` set to `GTD`; order the timestamp only retains second-level precision, ms part will be ignored; The goodTillDate timestamp must be greater than the current time plus 600 seconds and smaller than 253402300799000  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
Additional mandatory parameters based on `type`:

Type| Additional mandatory parameters  
---|---  
`LIMIT`| `timeInForce`, `quantity`, `price` or `priceMatch`  
`MARKET`| `quantity`  
`STOP/TAKE_PROFIT`| `quantity`, `stopPrice`, `price` or `priceMatch`  
`STOP_MARKET/TAKE_PROFIT_MARKET`| `stopPrice`  
`TRAILING_STOP_MARKET`| `callbackRate`  
  
>   * Order with type `STOP`, parameter `timeInForce` can be sent ( default `GTC`).
> 
>   * Order with type `TAKE_PROFIT`, parameter `timeInForce` can be sent ( default `GTC`).
> 
>   * Condition orders will be triggered when:
> 
>     * If parameter`priceProtect`is sent as true: 
>       * when price reaches the `stopPrice` ，the difference rate between "MARK_PRICE" and "CONTRACT_PRICE" cannot be larger than the "triggerProtect" of the symbol
>       * "triggerProtect" of a symbol can be got from `GET /fapi/v1/exchangeInfo`
>     * `STOP`, `STOP_MARKET`: 
>       * BUY: latest price ("MARK_PRICE" or "CONTRACT_PRICE") >= `stopPrice`
>       * SELL: latest price ("MARK_PRICE" or "CONTRACT_PRICE") <= `stopPrice`
>     * `TAKE_PROFIT`, `TAKE_PROFIT_MARKET`: 
>       * BUY: latest price ("MARK_PRICE" or "CONTRACT_PRICE") <= `stopPrice`
>       * SELL: latest price ("MARK_PRICE" or "CONTRACT_PRICE") >= `stopPrice`
>     * `TRAILING_STOP_MARKET`: 
>       * BUY: the lowest price after order placed `<= `activationPrice`, and the latest price >`= the lowest price * (1 + `callbackRate`)
>       * SELL: the highest price after order placed >= `activationPrice`, and the latest price <= the highest price * (1 - `callbackRate`)
>   * For `TRAILING_STOP_MARKET`, if you got such error code.  
>  `{"code": -2021, "msg": "Order would immediately trigger."}`  
>  means that the parameters you send do not meet the following requirements:
> 
>     * BUY: `activationPrice` should be smaller than latest price.
>     * SELL: `activationPrice` should be larger than latest price.
>   * If `newOrderRespType ` is sent as `RESULT` :
> 
>     * `MARKET` order: the final FILLED result of the order will be return directly.
>     * `LIMIT` order with special `timeInForce`: the final status result of the order(FILLED or EXPIRED) will be returned directly.
>   * `STOP_MARKET`, `TAKE_PROFIT_MARKET` with `closePosition`=`true`:
> 
>     * Follow the same rules for condition orders.
>     * If triggered，**close all** current long position( if `SELL`) or current short position( if `BUY`).
>     * Cannot be used with `quantity` paremeter
>     * Cannot be used with `reduceOnly` parameter
>     * In Hedge Mode,cannot be used with `BUY` orders in `LONG` position side. and cannot be used with `SELL` orders in `SHORT` position side
> 


## Response Example[​](/docs/derivatives/usds-margined-futures/trade/websocket-api#response-example "Direct link to Response Example")
    
    
    {  
        "id": "3f7df6e3-2df4-44b9-9919-d2f38f90a99a",  
        "status": 200,  
        "result": {  
            "orderId": 325078477,  
            "symbol": "BTCUSDT",  
            "status": "NEW",  
            "clientOrderId": "iCXL1BywlBaf2sesNUrVl3",  
            "price": "43187.00",  
            "avgPrice": "0.00",  
            "origQty": "0.100",  
            "executedQty": "0.000",  
            "cumQty": "0.000",  
            "cumQuote": "0.00000",  
            "timeInForce": "GTC",  
            "type": "LIMIT",  
            "reduceOnly": false,  
            "closePosition": false,  
            "side": "BUY",  
            "positionSide": "BOTH",  
            "stopPrice": "0.00",  
            "workingType": "CONTRACT_PRICE",  
            "priceProtect": false,  
            "origType": "LIMIT",  
            "priceMatch": "NONE",  
            "selfTradePreventionMode": "NONE",  
            "goodTillDate": 0,  
            "updateTime": 1702555534435  
        },  
        "rateLimits": [  
            {  
                "rateLimitType": "ORDERS",  
                "interval": "SECOND",  
                "intervalNum": 10,  
                "limit": 300,  
                "count": 1  
            },  
            {  
                "rateLimitType": "ORDERS",  
                "interval": "MINUTE",  
                "intervalNum": 1,  
                "limit": 1200,  
                "count": 1  
            },  
            {  
                "rateLimitType": "REQUEST_WEIGHT",  
                "interval": "MINUTE",  
                "intervalNum": 1,  
                "limit": 2400,  
                "count": 1  
            }  
        ]  
    }

---

# 下单 (TRADE)

## 接口描述[​](/docs/zh-CN/derivatives/usds-margined-futures/trade/websocket-api#接口描述 "接口描述的直接链接")

下单

## 方式[​](/docs/zh-CN/derivatives/usds-margined-futures/trade/websocket-api#方式 "方式的直接链接")

`order.place`

## 请求[​](/docs/zh-CN/derivatives/usds-margined-futures/trade/websocket-api#请求 "请求的直接链接")

`order.place`
    
    
    {  
        "id": "3f7df6e3-2df4-44b9-9919-d2f38f90a99a",  
        "method": "order.place",  
        "params": {  
            "apiKey": "HMOchcfii9ZRZnhjp2XjGXhsOBd6msAhKz9joQaWwZ7arcJTlD2hGPHQj1lGdTjR",  
            "positionSide": "BOTH",  
            "price": 43187.00,  
            "quantity": 0.1,  
            "side": "BUY",  
            "symbol": "BTCUSDT",  
            "timeInForce": "GTC",  
            "timestamp": 1702555533821,  
            "type": "LIMIT",  
            "signature": "0f04368b2d22aafd0ggc8809ea34297eff602272917b5f01267db4efbc1c9422"  
        }  
    }  
    

## 请求权重[​](/docs/zh-CN/derivatives/usds-margined-futures/trade/websocket-api#请求权重 "请求权重的直接链接")

**0**

## 请求参数[​](/docs/zh-CN/derivatives/usds-margined-futures/trade/websocket-api#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
symbol| STRING| YES| 交易对  
side| ENUM| YES| 买卖方向 `SELL`, `BUY`  
positionSide| ENUM| NO| 持仓方向，单向持仓模式下非必填，默认且仅可填`BOTH`;在双向持仓模式下必填,且仅可选择 `LONG` 或 `SHORT`  
type| ENUM| YES| 订单类型 `LIMIT`, `MARKET`, `STOP`, `TAKE_PROFIT`, `STOP_MARKET`, `TAKE_PROFIT_MARKET`, `TRAILING_STOP_MARKET`  
reduceOnly| STRING| NO| `true`, `false`; 非双开模式下默认`false`；双开模式下不接受此参数； 使用`closePosition`不支持此参数。  
quantity| DECIMAL| NO| 下单数量,使用`closePosition`不支持此参数。  
price| DECIMAL| NO| 委托价格  
newClientOrderId| STRING| NO| 用户自定义的订单号，不可以重复出现在挂单中。如空缺系统会自动赋值。必须满足正则规则 `^[\.A-Z\:/a-z0-9_-]{1,36}$`  
stopPrice| DECIMAL| NO| 触发价, 仅 `STOP`, `STOP_MARKET`, `TAKE_PROFIT`, `TAKE_PROFIT_MARKET` 需要此参数  
closePosition| STRING| NO| `true`, `false`；触发后全部平仓，仅支持`STOP_MARKET`和`TAKE_PROFIT_MARKET`；不与`quantity`合用；自带只平仓效果，不与`reduceOnly` 合用  
activationPrice| DECIMAL| NO| 追踪止损激活价格，仅`TRAILING_STOP_MARKET` 需要此参数, 默认为下单当前市场价格(支持不同`workingType`)  
callbackRate| DECIMAL| NO| 追踪止损回调比例，可取值范围[0.1, 10],其中 1代表1% ,仅`TRAILING_STOP_MARKET` 需要此参数  
timeInForce| ENUM| NO| 有效方法  
workingType| ENUM| NO| stopPrice 触发类型: `MARK_PRICE`(标记价格), `CONTRACT_PRICE`(合约最新价). 默认 `CONTRACT_PRICE`  
priceProtect| STRING| NO| 条件单触发保护："TRUE","FALSE", 默认"FALSE". 仅 `STOP`, `STOP_MARKET`, `TAKE_PROFIT`, `TAKE_PROFIT_MARKET` 需要此参数  
newOrderRespType| ENUM| NO| "ACK", "RESULT", 默认 "ACK"  
priceMatch| ENUM| NO| `OPPONENT`/ `OPPONENT_5`/ `OPPONENT_10`/ `OPPONENT_20`/`QUEUE`/ `QUEUE_5`/ `QUEUE_10`/ `QUEUE_20`；不能与price同时传  
selfTradePreventionMode| ENUM| NO| `NONE` / `EXPIRE_TAKER`/ `EXPIRE_MAKER`/ `EXPIRE_BOTH`； 默认`NONE`  
goodTillDate| LONG| NO| TIF为GTD时订单的自动取消时间， 当`timeInforce`为`GTD`时必传；传入的时间戳仅保留秒级精度，毫秒级部分会被自动忽略，时间戳需大于当前时间+600s且小于253402300799000  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
根据 order `type`的不同，某些参数强制要求，具体如下:

Type| 强制要求的参数  
---|---  
`LIMIT`| `timeInForce`, `quantity`, `price`或`priceMatch`  
`MARKET`| `quantity`  
`STOP`, `TAKE_PROFIT`| `quantity`, `stopPrice`  
`STOP_MARKET`, `TAKE_PROFIT_MARKET`| `stopPrice`, `price`或`priceMatch`  
`TRAILING_STOP_MARKET`| `callbackRate`  
  
>   * 条件单的触发必须:
> 
>     * 如果订单参数`priceProtect`为true: 
>       * 达到触发价时，`MARK_PRICE`(标记价格)与`CONTRACT_PRICE`(合约最新价)之间的价差不能超过改symbol触发保护阈值
>       * 触发保护阈值请参考接口`GET /fapi/v1/exchangeInfo` 返回内容相应symbol中"triggerProtect"字段
>     * `STOP`, `STOP_MARKET` 止损单: 
>       * 买入: 最新合约价格/标记价格高于等于触发价`stopPrice`
>       * 卖出: 最新合约价格/标记价格低于等于触发价`stopPrice`
>     * `TAKE_PROFIT`, `TAKE_PROFIT_MARKET` 止盈单: 
>       * 买入: 最新合约价格/标记价格低于等于触发价`stopPrice`
>       * 卖出: 最新合约价格/标记价格高于等于触发价`stopPrice`
>     * `TRAILING_STOP_MARKET` 跟踪止损单: 
>       * 买入: 当合约价格/标记价格区间最低价格低于激活价格`activationPrice`,且最新合约价格/标记价高于等于最低价设定回调幅度。
>       * 卖出: 当合约价格/标记价格区间最高价格高于激活价格`activationPrice`,且最新合约价格/标记价低于等于最高价设定回调幅度。
>   * `TRAILING_STOP_MARKET` 跟踪止损单如果遇到报错 `{"code": -2021, "msg": "Order would immediately trigger."}`  
>  表示订单不满足以下条件:
> 
>     * 买入: 指定的`activationPrice` 必须小于 latest price
>     * 卖出: 指定的`activationPrice` 必须大于 latest price
>   * `newOrderRespType` 如果传 `RESULT`:
> 
>     * `MARKET` 订单将直接返回成交结果；
>     * 配合使用特殊 `timeInForce` 的 `LIMIT` 订单将直接返回成交或过期拒绝结果。
>   * `STOP_MARKET`, `TAKE_PROFIT_MARKET` 配合 `closePosition`=`true`:
> 
>     * 条件单触发依照上述条件单触发逻辑
>     * 条件触发后，平掉当时持有所有多头仓位(若为卖单)或当时持有所有空头仓位(若为买单)
>     * 不支持 `quantity` 参数
>     * 自带只平仓属性，不支持`reduceOnly`参数
>     * 双开模式下,`LONG`方向上不支持`BUY`; `SHORT` 方向上不支持`SELL`
> 


## 响应示例[​](/docs/zh-CN/derivatives/usds-margined-futures/trade/websocket-api#响应示例 "响应示例的直接链接")
    
    
    {  
        "id": "3f7df6e3-2df4-44b9-9919-d2f38f90a99a",  
        "status": 200,  
        "result": {  
            "orderId": 325078477,  
            "symbol": "BTCUSDT",  
            "status": "NEW",  
            "clientOrderId": "iCXL1BywlBaf2sesNUrVl3",  
            "price": "43187.00",  
            "avgPrice": "0.00",  
            "origQty": "0.100",  
            "executedQty": "0.000",  
            "cumQty": "0.000",  
            "cumQuote": "0.00000",  
            "timeInForce": "GTC",  
            "type": "LIMIT",  
            "reduceOnly": false,  
            "closePosition": false,  
            "side": "BUY",  
            "positionSide": "BOTH",  
            "stopPrice": "0.00",  
            "workingType": "CONTRACT_PRICE",  
            "priceProtect": false,  
            "origType": "LIMIT",  
            "priceMatch": "NONE",  
            "selfTradePreventionMode": "NONE",  
            "goodTillDate": 0,  
            "updateTime": 1702555534435  
        },  
        "rateLimits": [  
            {  
                "rateLimitType": "ORDERS",  
                "interval": "SECOND",  
                "intervalNum": 10,  
                "limit": 300,  
                "count": 1  
            },  
            {  
                "rateLimitType": "ORDERS",  
                "interval": "MINUTE",  
                "intervalNum": 1,  
                "limit": 1200,  
                "count": 1  
            },  
            {  
                "rateLimitType": "REQUEST_WEIGHT",  
                "interval": "MINUTE",  
                "intervalNum": 1,  
                "limit": 2400,  
                "count": 1  
            }  
        ]  
    }