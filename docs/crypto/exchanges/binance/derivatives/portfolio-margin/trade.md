---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/portfolio-margin/trade
api_type: Trading
updated_at: 2026-01-15T23:45:17.555682
---

# New UM Order (TRADE)

## API Description[​](/docs/derivatives/portfolio-margin/trade#api-description "Direct link to API Description")

Place new UM order

## HTTP Request[​](/docs/derivatives/portfolio-margin/trade#http-request "Direct link to HTTP Request")

POST `/papi/v1/um/order`

## Request Weight(Order)[​](/docs/derivatives/portfolio-margin/trade#request-weightorder "Direct link to Request Weight\(Order\)")

**1**

## Request Parameters[​](/docs/derivatives/portfolio-margin/trade#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
symbol| STRING| YES|   
side| ENUM| YES|   
positionSide| ENUM| NO| Default `BOTH` for One-way Mode ; `LONG` or `SHORT` for Hedge Mode. It must be sent in Hedge Mode.  
type| ENUM| YES| `LIMIT`, `MARKET`  
timeInForce| ENUM| NO|   
quantity| DECIMAL| NO|   
reduceOnly| STRING| NO| "true" or "false". default "false". Cannot be sent in Hedge Mode .  
price| DECIMAL| NO|   
newClientOrderId| STRING| NO| A unique id among open orders. Automatically generated if not sent. Can only be string following the rule: `^[\.A-Z\:/a-z0-9_-]{1,32}$`  
newOrderRespType| ENUM| NO| `ACK`, `RESULT`, default `ACK`  
priceMatch| ENUM| NO| only avaliable for `LIMIT`/`STOP`/`TAKE_PROFIT` order; can be set to `OPPONENT`/ `OPPONENT_5`/ `OPPONENT_10`/ `OPPONENT_20`: /`QUEUE`/ `QUEUE_5`/ `QUEUE_10`/ `QUEUE_20`; Can't be passed together with `price`  
selfTradePreventionMode| ENUM| NO| `NONE`:No STP / `EXPIRE_TAKER`:expire taker order when STP triggers/ `EXPIRE_MAKER`:expire taker order when STP triggers/ `EXPIRE_BOTH`:expire both orders when STP triggers  
goodTillDate| LONG| NO| order cancel time for timeInForce `GTD`, mandatory when `timeInforce` set to `GTD`; order the timestamp only retains second-level precision, ms part will be ignored; The goodTillDate timestamp must be greater than the current time plus 600 seconds and smaller than 253402300799000Mode. It must be sent in Hedge Mode.  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
Additional mandatory parameters based on type:

Type| Additional mandatory parameters  
---|---  
`LIMIT`| `timeInForce`, `quantity`, `price`  
`MARKET`| `quantity`  
  
>   * If `newOrderRespType` is sent as `RESULT` : 
>     * `MARKET` order: the final FILLED result of the order will be return directly.
>     * `LIMIT` order with special `timeInForce`: the final status result of the order(FILLED or EXPIRED) will be returned directly.
>   * `selfTradePreventionMode` is only effective when `timeInForce` set to `IOC` or `GTC` or `GTD`.
>   * In extreme market conditions, timeInForce `GTD` order auto cancel time might be delayed comparing to `goodTillDate`
> 


## Response Example[​](/docs/derivatives/portfolio-margin/trade#response-example "Direct link to Response Example")
    
    
    {  
        "clientOrderId": "testOrder",  
        "cumQty": "0",  
        "cumQuote": "0",  
        "executedQty": "0",  
        "orderId": 22542179,  
        "avgPrice": "0.00000",  
        "origQty": "10",  
        "price": "0",  
        "reduceOnly": false,  
        "side": "BUY",  
        "positionSide": "SHORT",  
        "status": "NEW",  
        "symbol": "BTCUSDT",  
        "timeInForce": "GTD",  
        "type": "MARKET",  
        "selfTradePreventionMode": "NONE", //self trading preventation mode  
        "goodTillDate": 1693207680000,      //order pre-set auot cancel time for TIF GTD order   
        "updateTime": 1566818724722,  
        "priceMatch": "NONE"  
    }

---

# UM下单(TRADE)

## 接口描述[​](/docs/zh-CN/derivatives/portfolio-margin/trade#接口描述 "接口描述的直接链接")

UM下单

## HTTP请求[​](/docs/zh-CN/derivatives/portfolio-margin/trade#http请求 "HTTP请求的直接链接")

POST `/papi/v1/um/order`

## 请求权重(Order)[​](/docs/zh-CN/derivatives/portfolio-margin/trade#请求权重order "请求权重\(Order\)的直接链接")

**1**

## 请求参数[​](/docs/zh-CN/derivatives/portfolio-margin/trade#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
symbol| STRING| YES| 交易对  
side| ENUM| YES| 方向  
positionSide| ENUM| NO| 持仓方向，单向持仓模式下非必填，默认且仅可填`BOTH`;在双向持仓模式下必填,且仅可选择 `LONG` 或 `SHORT`  
type| ENUM| YES| `LIMIT`, `MARKET`  
timeInForce| ENUM| NO| 有效方法  
quantity| DECIMAL| NO| 下单数量  
reduceOnly| STRING| NO| `true`或`false`; 非双开模式下默认false；双开模式下不接受此参数  
price| DECIMAL| NO| 委托价格  
newClientOrderId| STRING| NO| 用户自定义的订单号，不可以重复出现在挂单中。如空缺系统会自动赋值。必须满足正则规则: `^[\.A-Z\:/a-z0-9_-]{1,32}$`  
newOrderRespType| ENUM| NO| `ACK`， `RESULT`，默认 `ACK`  
priceMatch| ENUM| NO| `OPPONENT`/ `OPPONENT_5`/ `OPPONENT_10`/ `OPPONENT_20`/`QUEUE`/ `QUEUE_5`/ `QUEUE_10`/ `QUEUE_20`；不能与price同时传  
selfTradePreventionMode| ENUM| NO| NONE / EXPIRE_TAKER/ EXPIRE_MAKER/ EXPIRE_BOTH； 默认NONE  
goodTillDate| LONG| NO| TIF为GTD时订单的自动取消时间， 当timeInforce为GTD时必传；传入的时间戳仅保留秒级精度，毫秒级部分会被自动忽略，时间戳需大于当前时间+600s且小于253402300799000  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
根据 order `type`的不同，某些参数强制要求，具体如下:

类型| 强制要求的参数  
---|---  
`LIMIT`| `timeInForce`, `quantity`, `price`  
`MARKET`| `quantity`  
  
>   * `newOrderRespType` 如果传 `RESULT`: 
>     * `MARKET` 订单将直接返回成交结果；
>     * 配合使用特殊 `timeInForce` 的 `LIMIT` 订单将直接返回成交或过期拒绝结果。
>   * `selfTradePreventionMode` 仅在 `timeInForce`为`IOC`或`GTC`或`GTD`时生效.
>   * 极端行情时，`timeInForce`为`GTD`的订单自动取消可能有一定延迟
> 


## 响应示例[​](/docs/zh-CN/derivatives/portfolio-margin/trade#响应示例 "响应示例的直接链接")
    
    
    {  
        "clientOrderId": "testOrder",  
        "cumQty": "0",  
        "cumQuote": "0",  
        "executedQty": "0",  
        "orderId": 22542179,  
        "avgPrice": "0.00000",  
        "origQty": "10",  
        "price": "0",  
        "reduceOnly": false,  
        "side": "BUY",  
        "positionSide": "SHORT",  
        "status": "NEW",  
        "symbol": "BTCUSDT",  
        "timeInForce": "GTD",  
        "type": "MARKET",  
        "selfTradePreventionMode": "NONE", ////订单自成交保护模式  
        "goodTillDate": 1693207680000,      //订单TIF为GTD时的自动取消时间   
        "updateTime": 1566818724722,  
        "priceMatch": "NONE"  
    }