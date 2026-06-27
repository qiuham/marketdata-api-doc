---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/usds-margined-futures/trade/rest-api
api_type: Trading
updated_at: 2026-01-15T23:47:06.284439
---

# New Order(TRADE)

## API Description[​](/docs/derivatives/usds-margined-futures/trade/rest-api#api-description "Direct link to API Description")

Send in a new order.

## HTTP Request[​](/docs/derivatives/usds-margined-futures/trade/rest-api#http-request "Direct link to HTTP Request")

POST `/fapi/v1/order`

## Request Weight[​](/docs/derivatives/usds-margined-futures/trade/rest-api#request-weight "Direct link to Request Weight")

1 on 10s order rate limit(X-MBX-ORDER-COUNT-10S); 1 on 1min order rate limit(X-MBX-ORDER-COUNT-1M); 0 on IP rate limit(x-mbx-used-weight-1m)

## Request Parameters[​](/docs/derivatives/usds-margined-futures/trade/rest-api#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
symbol| STRING| YES|   
side| ENUM| YES|   
positionSide| ENUM| NO| Default `BOTH` for One-way Mode ; `LONG` or `SHORT` for Hedge Mode. It must be sent in Hedge Mode.  
type| ENUM| YES|   
timeInForce| ENUM| NO|   
quantity| DECIMAL| NO|   
reduceOnly| STRING| NO| "true" or "false". default "false". Cannot be sent in Hedge Mode  
price| DECIMAL| NO|   
newClientOrderId| STRING| NO| A unique id among open orders. Automatically generated if not sent. Can only be string following the rule: `^[\.A-Z\:/a-z0-9_-]{1,36}$`  
newOrderRespType| ENUM| NO| "ACK", "RESULT", default "ACK"  
priceMatch| ENUM| NO| only avaliable for `LIMIT`/`STOP`/`TAKE_PROFIT` order; can be set to `OPPONENT`/ `OPPONENT_5`/ `OPPONENT_10`/ `OPPONENT_20`: /`QUEUE`/ `QUEUE_5`/ `QUEUE_10`/ `QUEUE_20`; Can't be passed together with `price`  
selfTradePreventionMode| ENUM| NO| `EXPIRE_TAKER`:expire taker order when STP triggers/ `EXPIRE_MAKER`:expire taker order when STP triggers/ `EXPIRE_BOTH`:expire both orders when STP triggers; default `EXPIRE_MAKER`  
goodTillDate| LONG| NO| order cancel time for timeInForce `GTD`, mandatory when `timeInforce` set to `GTD`; order the timestamp only retains second-level precision, ms part will be ignored; The goodTillDate timestamp must be greater than the current time plus 600 seconds and smaller than 253402300799000  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
Additional mandatory parameters based on `type`:

Type| Additional mandatory parameters  
---|---  
`LIMIT`| `timeInForce`, `quantity`, `price`  
`MARKET`| `quantity`  
  
>   * If `newOrderRespType ` is sent as `RESULT` : 
>     * `MARKET` order: the final FILLED result of the order will be return directly.
>     * `LIMIT` order with special `timeInForce`: the final status result of the order(FILLED or EXPIRED) will be returned directly.
>   * `selfTradePreventionMode` is only effective when `timeInForce` set to `IOC` or `GTC` or `GTD`.
>   * In extreme market conditions, timeInForce `GTD` order auto cancel time might be delayed comparing to `goodTillDate`
> 


## Response Example[​](/docs/derivatives/usds-margined-futures/trade/rest-api#response-example "Direct link to Response Example")
    
    
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
      	"stopPrice": "9300",		// please ignore when order type is TRAILING_STOP_MARKET  
      	"closePosition": false,   // if Close-All  
      	"symbol": "BTCUSDT",  
      	"timeInForce": "GTD",  
      	"type": "TRAILING_STOP_MARKET",  
      	"origType": "TRAILING_STOP_MARKET",  
     	"updateTime": 1566818724722,  
     	"workingType": "CONTRACT_PRICE",  
     	"priceProtect": false,      // if conditional order trigger is protected	  
     	"priceMatch": "NONE",              //price match mode  
     	"selfTradePreventionMode": "NONE", //self trading preventation mode  
     	"goodTillDate": 1693207680000      //order pre-set auot cancel time for TIF GTD order  
    }

---

# 下单 (TRADE)

## 接口描述[​](/docs/zh-CN/derivatives/usds-margined-futures/trade/rest-api#接口描述 "接口描述的直接链接")

下单

## HTTP请求[​](/docs/zh-CN/derivatives/usds-margined-futures/trade/rest-api#http请求 "HTTP请求的直接链接")

POST `/fapi/v1/order`

## 请求权重[​](/docs/zh-CN/derivatives/usds-margined-futures/trade/rest-api#请求权重 "请求权重的直接链接")

10s order rate limit(X-MBX-ORDER-COUNT-10S)为1; 1min order rate limit(X-MBX-ORDER-COUNT-1M)为1; IP rate limit(x-mbx-used-weight-1m)为0

## 请求参数[​](/docs/zh-CN/derivatives/usds-margined-futures/trade/rest-api#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
symbol| STRING| YES| 交易对  
side| ENUM| YES| 买卖方向 `SELL`, `BUY`  
positionSide| ENUM| NO| 持仓方向，单向持仓模式下非必填，默认且仅可填`BOTH`;在双向持仓模式下必填,且仅可选择 `LONG` 或 `SHORT`  
type| ENUM| YES| 订单类型 `LIMIT`, `MARKET`, `STOP`, `TAKE_PROFIT`, `STOP_MARKET`, `TAKE_PROFIT_MARKET`, `TRAILING_STOP_MARKET`  
reduceOnly| STRING| NO| `true`, `false`; 非双开模式下默认`false`；双开模式下不接受此参数  
quantity| DECIMAL| NO|   
price| DECIMAL| NO| 委托价格  
newClientOrderId| STRING| NO| 用户自定义的订单号，不可以重复出现在挂单中。如空缺系统会自动赋值。必须满足正则规则 `^[\.A-Z\:/a-z0-9_-]{1,36}$`  
newOrderRespType| ENUM| NO| "ACK", "RESULT", 默认 "ACK"  
priceMatch| ENUM| NO| `OPPONENT`/ `OPPONENT_5`/ `OPPONENT_10`/ `OPPONENT_20`/`QUEUE`/ `QUEUE_5`/ `QUEUE_10`/ `QUEUE_20`；不能与price同时传  
selfTradePreventionMode| ENUM| NO| `EXPIRE_TAKER`/ `EXPIRE_MAKER`/ `EXPIRE_BOTH`； 默认`EXPIRE_MAKER`  
goodTillDate| LONG| NO| TIF为GTD时订单的自动取消时间， 当`timeInforce`为`GTD`时必传；传入的时间戳仅保留秒级精度，毫秒级部分会被自动忽略，时间戳需大于当前时间+600s且小于253402300799000  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
根据 order `type`的不同，某些参数强制要求，具体如下:

Type| 强制要求的参数  
---|---  
`LIMIT`| `timeInForce`, `quantity`, `price`  
`MARKET`| `quantity`  
  
>   * `newOrderRespType` 如果传 `RESULT`: 
>     * `MARKET` 订单将直接返回成交结果；
>     * 配合使用特殊 `timeInForce` 的 `LIMIT` 订单将直接返回成交或过期拒绝结果。
>   * `selfTradePreventionMode` 仅在 `timeInForce`为`IOC`或`GTC`或`GTD`时生效.
>   * 极端行情时，`timeInForce`为`GTD`的订单自动取消可能有一定延迟
> 


## 响应示例[​](/docs/zh-CN/derivatives/usds-margined-futures/trade/rest-api#响应示例 "响应示例的直接链接")
    
    
    {  
     	"clientOrderId": "testOrder", // 用户自定义的订单号  
     	"cumQty": "0",  
     	"cumQuote": "0", // 成交金额  
     	"executedQty": "0", // 成交量  
     	"orderId": 22542179, // 系统订单号  
     	"avgPrice": "0.00000",	// 平均成交价  
     	"origQty": "10", // 原始委托数量  
     	"price": "0", // 委托价格  
     	"reduceOnly": false, // 仅减仓  
     	"side": "SELL", // 买卖方向  
     	"positionSide": "SHORT", // 持仓方向  
     	"status": "NEW", // 订单状态  
     	"stopPrice": "0", // 触发价，对`TRAILING_STOP_MARKET`无效  
     	"closePosition": false,   // 是否条件全平仓  
     	"symbol": "BTCUSDT", // 交易对  
     	"timeInForce": "GTD", // 有效方法  
     	"type": "TRAILING_STOP_MARKET", // 订单类型  
     	"origType": "TRAILING_STOP_MARKET",  // 触发前订单类型  
     	"updateTime": 1566818724722, // 更新时间  
     	"workingType": "CONTRACT_PRICE", // 条件价格触发类型  
     	"priceProtect": false,            // 是否开启条件单触发保护  
     	"priceMatch": "NONE",              //盘口价格下单模式  
     	"selfTradePreventionMode": "NONE", //订单自成交保护模式  
     	"goodTillDate": 1693207680000      //订单TIF为GTD时的自动取消时间  
    }