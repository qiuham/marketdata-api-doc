---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/coin-margined-futures/trade/rest-api/All-Orders
api_type: Trading
updated_at: 2026-01-15T23:39:31.226294
---

# All Orders (USER_DATA)

## API Description[​](/docs/derivatives/coin-margined-futures/trade/rest-api/All-Orders#api-description "Direct link to API Description")

Get all account orders; active, canceled, or filled.

  * These orders will not be found: 
    * order status is CANCELED or EXPIRED AND order has NO filled trade AND created time + 3 days < current time
    * order create time + 90 days < current time



## HTTP Request[​](/docs/derivatives/coin-margined-futures/trade/rest-api/All-Orders#http-request "Direct link to HTTP Request")

GET `/dapi/v1/allOrders`

## Request Weight[​](/docs/derivatives/coin-margined-futures/trade/rest-api/All-Orders#request-weight "Direct link to Request Weight")

**20** with symbol, **40** with pair

## Request Parameters[​](/docs/derivatives/coin-margined-futures/trade/rest-api/All-Orders#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
symbol| STRING| NO|   
pair| STRING| NO|   
orderId| LONG| NO|   
startTime| LONG| NO|   
endTime| LONG| NO|   
limit| INT| NO| Default 50; max 100.  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
**Notes:**

>   * Either `symbol` or `pair` must be sent.
>   * `pair` can't be sent with `orderId`
>   * If `orderId` is set, it will get orders >= that `orderId`. Otherwise most recent orders are returned.
>   * If orderId is set, it will get orders >= that orderId. Otherwise most recent orders are returned.
>   * The query time period must be less then 7 days( default as the recent 7 days).
> 


## Response Example[​](/docs/derivatives/coin-margined-futures/trade/rest-api/All-Orders#response-example "Direct link to Response Example")
    
    
    [  
      {  
       	"avgPrice": "0.0",  
      	"clientOrderId": "abc",  
      	"cumBase": "0",  
      	"executedQty": "0",  
      	"orderId": 1917641,  
      	"origQty": "0.40",  
      	"origType": "TRAILING_STOP_MARKET",  
      	"price": "0",  
      	"reduceOnly": false,  
      	"side": "BUY",  
      	"positionSide": "SHORT",  
      	"status": "NEW",  
      	"stopPrice": "9300",				// please ignore when order type is TRAILING_STOP_MARKET  
      	"closePosition": false,   			// if Close-All  
      	"symbol": "BTCUSD_200925",  
      	"pair": "BTCUSD",  
      	"time": 1579276756075,				// order time  
      	"timeInForce": "GTC",  
      	"type": "TRAILING_STOP_MARKET",  
      	"activatePrice": "9020",			// activation price, only return with TRAILING_STOP_MARKET order  
      	"priceRate": "0.3",					// callback rate, only return with TRAILING_STOP_MARKET order  
      	"updateTime": 1579276756075,		// update time  
      	"workingType": "CONTRACT_PRICE",  
      	"priceProtect": false,              // if conditional order trigger is protected  
      	"priceMatch": "NONE",               //price match mode  
      	"selfTradePreventionMode": "NONE",  //self trading preventation mode  
      }  
    ]

---

# 查询所有订单(包括历史订单) (USER_DATA)

## 接口描述[​](/docs/zh-CN/derivatives/coin-margined-futures/trade/rest-api/All-Orders#接口描述 "接口描述的直接链接")

查询订单

  * 请注意，如果订单满足如下条件，不会被查询到： 
    * 订单的最终状态为 CANCELED 或者 EXPIRED 并且 订单没有任何的成交记录 并且 订单生成时间 + 3天 < 当前时间
    * 订单创建时间 + 90天 < 当前时间



## HTTP请求[​](/docs/zh-CN/derivatives/coin-margined-futures/trade/rest-api/All-Orders#http请求 "HTTP请求的直接链接")

GET `/dapi/v1/allOrders`

## 请求权重[​](/docs/zh-CN/derivatives/coin-margined-futures/trade/rest-api/All-Orders#请求权重 "请求权重的直接链接")

传symbol **20** ，传pairs **40**

## 请求参数[​](/docs/zh-CN/derivatives/coin-margined-futures/trade/rest-api/All-Orders#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
symbol| STRING| NO| 交易对  
pair| STRING| NO| 标的交易对  
orderId| LONG| NO| 只返回此orderID及之后的订单,缺省返回最近的订单, 仅支持配合symbol使用  
startTime| LONG| NO| 起始时间  
endTime| LONG| NO| 结束时间  
limit| INT| NO| 返回的结果集数量 默认值:50 最大值:100  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
>   * `symbol` 或 `pair`必须传一个，不能同时传
>   * `pair`和`orderId`不能一起传
>   * 如果设置了`orderId`，将返回在此`orderId`之后的订单，否则会返回最近的订单
>   * 查询时间范围最大不得超过7天
>   * 默认查询最近7天内的数据
> 


## 响应示例[​](/docs/zh-CN/derivatives/coin-margined-futures/trade/rest-api/All-Orders#响应示例 "响应示例的直接链接")
    
    
    [  
      {  
       	"avgPrice": "0.0",				    // 平均成交价  
      	"clientOrderId": "abc",				// 用户自定义的订单号  
      	"cumBase": "0", 					// 成交金额(标的数量)  
      	"executedQty": "0",					// 成交量(张数)  
      	"orderId": 1917641,					// 系统订单号  
      	"origQty": "0.40",					// 原始委托数量  
      	"origType": "TRAILING_STOP_MARKET",	// 触发前订单类型  
      	"price": "0",				     	// 委托价格  
      	"reduceOnly": false,				// 是否仅减仓  
      	"side": "BUY",						// 买卖方向  
      	"positionSide": "SHORT", 			// 持仓方向  
      	"status": "NEW",					// 订单状态  
      	"stopPrice": "9300",				// 触发价,对`TRAILING_STOP_MARKET`无效  
      	"closePosition": false,             // 是否条件全平仓  
      	"symbol": "BTCUSD_200925",			// 交易对  
      	"pair": "BTCUSD",	                // 标的交易对  
      	"time": 1579276756075,				// 订单时间  
      	"timeInForce": "GTC",				// 有效方法  
      	"type": "TRAILING_STOP_MARKET",		// 订单类型  
      	"activatePrice": "9020",            // 跟踪止损激活价格, 仅`TRAILING_STOP_MARKET` 订单返回此字段  
      	"priceRate": "0.3",             	// 跟踪止损回调比例, 仅`TRAILING_STOP_MARKET` 订单返回此字段  
      	"updateTime": 1579276756075,		// 更新时间  
      	"workingType": "CONTRACT_PRICE",	// 条件价格触发类型  
      	"priceMatch": "NONE",               //盘口价格下单模式  
      	"selfTradePreventionMode": "NONE"   //订单自成交保护模式  
      }  
    ]