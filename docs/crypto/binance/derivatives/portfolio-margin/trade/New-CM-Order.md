---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/portfolio-margin/trade/New-CM-Order
api_type: Trading
updated_at: 2026-01-15T23:45:36.746867
---

# New CM Order(TRADE)

## API Description[​](/docs/derivatives/portfolio-margin/trade/New-CM-Order#api-description "Direct link to API Description")

Place new CM order

## HTTP Request[​](/docs/derivatives/portfolio-margin/trade/New-CM-Order#http-request "Direct link to HTTP Request")

POST `/papi/v1/cm/order`

## Request Weight[​](/docs/derivatives/portfolio-margin/trade/New-CM-Order#request-weight "Direct link to Request Weight")

**1**

## Request Parameters[​](/docs/derivatives/portfolio-margin/trade/New-CM-Order#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
symbol| STRING| YES|   
side| ENUM| YES|   
positionSide| ENUM| NO| Default `BOTH` for One-way Mode ; `LONG` or `SHORT` for Hedge Mode. It must be sent in Hedge Mode.  
type| ENUM| YES| "LIMIT", "MARKET"  
timeInForce| ENUM| NO|   
quantity| DECIMAL| NO|   
reduceOnly| STRING| NO| "true" or "false". default "false". Cannot be sent in Hedge Mode.  
price| DECIMAL| NO|   
priceMatch| ENUM| NO| only avaliable for `LIMIT`/`STOP`/`TAKE_PROFIT` order; can be set to `OPPONENT`/ `OPPONENT_5`/ `OPPONENT_10`/ `OPPONENT_20`: /`QUEUE`/ `QUEUE_5`/ `QUEUE_10`/ `QUEUE_20`; Can't be passed together with `price`  
newClientOrderId| STRING| NO| A unique id among open orders. Automatically generated if not sent. Can only be string following the rule: `^[\.A-Z\:/a-z0-9_-]{1,32}$`  
newOrderRespType| ENUM| NO| "ACK", "RESULT", default "ACK"  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
Additional mandatory parameters based on `type`:

Type| Additional mandatory parameters  
---|---  
`LIMIT`| `timeInForce`, `quantity`, `price`  
`MARKET`| `quantity`  
  
  * If `newOrderRespType` is sent as `RESULT` : 
    * `MARKET` order: the final FILLED result of the order will be return directly.
    * `LIMIT` order with special `timeInForce`: the final status result of the order(FILLED or EXPIRED) will be returned directly.



## Response Example[​](/docs/derivatives/portfolio-margin/trade/New-CM-Order#response-example "Direct link to Response Example")
    
    
    {  
        "clientOrderId": "testOrder",  
        "cumQty": "0",  
        "cumBase": "0",  
        "executedQty": "0",  
        "orderId": 22542179,  
        "avgPrice": "0.0",  
        "origQty": "10",  
        "price": "0",  
        "reduceOnly": false,  
        "side": "BUY",  
        "positionSide": "SHORT",   
        "status": "NEW",  
        "symbol": "BTCUSD_200925",  
        "pair": "BTCUSD",  
        "timeInForce": "GTC",  
        "type": "MARKET",  
        "updateTime": 1566818724722  
    }

---

# CM下单(TRADE)

## 接口描述[​](/docs/zh-CN/derivatives/portfolio-margin/trade/New-CM-Order#接口描述 "接口描述的直接链接")

CM下单

## HTTP请求[​](/docs/zh-CN/derivatives/portfolio-margin/trade/New-CM-Order#http请求 "HTTP请求的直接链接")

POST `/papi/v1/cm/order`

## 请求权重[​](/docs/zh-CN/derivatives/portfolio-margin/trade/New-CM-Order#请求权重 "请求权重的直接链接")

**1**

## 请求参数[​](/docs/zh-CN/derivatives/portfolio-margin/trade/New-CM-Order#请求参数 "请求参数的直接链�接")

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
priceMatch| ENUM| NO| `OPPONENT`/ `OPPONENT_5`/ `OPPONENT_10`/ `OPPONENT_20`/`QUEUE`/ `QUEUE_5`/ `QUEUE_10`/ `QUEUE_20`；不能与price同时传  
newClientOrderId| STRING| NO| 用户自定义的订单号，不可以重复出现在挂单中。如空缺系统会自动赋值。必须满足正则规则: `^[\.A-Z\:/a-z0-9_-]{1,32}$`  
newOrderRespType| ENUM| NO| `ACK`， `RESULT`，默认 `ACK`  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
根据 order `type`的不同，某些参数强制要求，具体如下:

类型| 强制要求的参数  
---|---  
`LIMIT`| `timeInForce`, `quantity`, `price`  
`MARKET`| `quantity`  
  
  * `newOrderRespType` 如果传 `RESULT`: 
    * `MARKET` 订单将直接返回成交结果；
    * 配合使用特殊 `timeInForce` 的 `LIMIT` 订单将直接返回成交或过期拒绝结果。



## 响应示例[​](/docs/zh-CN/derivatives/portfolio-margin/trade/New-CM-Order#响应示例 "响应示例的直接链接")
    
    
    {  
        "clientOrderId": "testOrder",  
        "cumQty": "0",  
        "cumBase": "0",  
        "executedQty": "0",  
        "orderId": 22542179,  
        "avgPrice": "0.0",  
        "origQty": "10",  
        "price": "0",  
        "reduceOnly": false,  
        "side": "BUY",  
        "positionSide": "SHORT",   
        "status": "NEW",  
        "symbol": "BTCUSD_200925",  
        "pair": "BTCUSD",  
        "timeInForce": "GTC",  
        "type": "MARKET",  
        "updateTime": 1566818724722  
    }