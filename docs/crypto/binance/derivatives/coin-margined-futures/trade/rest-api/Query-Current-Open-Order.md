---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/coin-margined-futures/trade/rest-api/Query-Current-Open-Order
api_type: Trading
updated_at: 2026-01-15T23:39:50.334777
---

# Query Current Open Order(USER_DATA)

## API Description[​](/docs/derivatives/coin-margined-futures/trade/rest-api/Query-Current-Open-Order#api-description "Direct link to API Description")

Query Current Open Order

## HTTP Request[​](/docs/derivatives/coin-margined-futures/trade/rest-api/Query-Current-Open-Order#http-request "Direct link to HTTP Request")

GET `/dapi/v1/openOrder`

## Request Weight[​](/docs/derivatives/coin-margined-futures/trade/rest-api/Query-Current-Open-Order#request-weight "Direct link to Request Weight")

**1**

## Request Parameters[​](/docs/derivatives/coin-margined-futures/trade/rest-api/Query-Current-Open-Order#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
symbol| STRING| YES|   
orderId| LONG| NO|   
origClientOrderId| STRING| NO|   
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
>   * Either`orderId` or `origClientOrderId` must be sent
>   * If the queried order has been filled or cancelled, the error message "Order does not exist" will be returned.
> 


## Response Example[​](/docs/derivatives/coin-margined-futures/trade/rest-api/Query-Current-Open-Order#response-example "Direct link to Response Example")
    
    
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
      	"pair": "BTCUSD"  
      	"time": 1579276756075,				// order time  
      	"timeInForce": "GTC",  
      	"type": "TRAILING_STOP_MARKET",  
      	"activatePrice": "9020",			// activation price, only return with TRAILING_STOP_MARKET order  
      	"priceRate": "0.3",					// callback rate, only return with TRAILING_STOP_MARKET order						  
      	"updateTime": 1579276756075,		  
      	"workingType": "CONTRACT_PRICE",  
      	"priceProtect": false               // if conditional order trigger is protected	  
      	"priceMatch": "NONE",               // price match mode  
      	"selfTradePreventionMode": "NONE"   // self trading preventation mode	  
    }

---

# 查询当前挂单(USER_DATA)

## 接口描述[​](/docs/zh-CN/derivatives/coin-margined-futures/trade/rest-api/Query-Current-Open-Order#接口描述 "接口描述的直接链接")

查询当前挂单

## HTTP请求[​](/docs/zh-CN/derivatives/coin-margined-futures/trade/rest-api/Query-Current-Open-Order#http请求 "HTTP请求的直接链接")

GET `/dapi/v1/openOrder`

## 请求权重[​](/docs/zh-CN/derivatives/coin-margined-futures/trade/rest-api/Query-Current-Open-Order#请求权重 "请求权重的直接链接")

**1**

## 请求参数[​](/docs/zh-CN/derivatives/coin-margined-futures/trade/rest-api/Query-Current-Open-Order#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
symbol| STRING| YES| 交易对  
orderId| LONG| NO| 系统订单号  
origClientOrderId| STRING| NO| 用户自定义的订单号  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
>   * `orderId` 与 `origClientOrderId` 中的一个为必填参数
>   * 查询的订单如果已经成交或取消,将返回报错"Order does not exist."
> 


## 响应示例[​](/docs/zh-CN/derivatives/coin-margined-futures/trade/rest-api/Query-Current-Open-Order#响应示例 "响应示例的直接链接")
    
    
      
    {  
      	"avgPrice": "0.0",			       	// 平均成交价  
      	"clientOrderId": "abc",				// 用户自定义的订单号  
      	"cumBase": "0", 					// 成交金额(标的数量)  
      	"executedQty": "0",					// 成交量(张数)  
      	"orderId": 1917641,					// 系统订单号  
      	"origQty": "0.40",					// 原始委托数量  
      	"origType": "TRAILING_STOP_MARKET",	// 触发前订单类型  
      	"price": "0",					    // 委托价格  
      	"reduceOnly": false,				// 是否仅减仓  
      	"side": "BUY",						// 买卖方向  
      	"status": "NEW",					// 订单状态  
      	"stopPrice": "9300",				// 触发价,对`TRAILING_STOP_MARKET`无效  
      	"closePosition": false,             // 是否条件全平仓  
      	"symbol": "BTCUSD_200925",			// 交易对  
      	"pair": "BTCUSD",	                // 标的交易对  
      	"time": 1579276756075,				// 订单时间  
      	"timeInForce": "GTC",				// 有效方法  
      	"type": "TRAILING_STOP_MARKET",		// 订单类型  
      	"activatePrice": "9020",            // 跟踪止损激活价格, 仅`TRAILING_STOP_MARKET` 订单返回此字段  
      	"priceRate": "0.3",              	// 跟踪止损回调比例, 仅`TRAILING_STOP_MARKET` 订单返回此字段  
      	"updateTime": 1579276756075,		// 更新时间  
      	"workingType": "CONTRACT_PRICE",	// 条件价格触发类型  
      	"priceProtect": false,              // 是否开启条件单触发保护  
      	"priceMatch": "NONE",               // 盘口价格下单模式  
      	"selfTradePreventionMode": "NONE"   // 订单自成交保护模式  
    	  	  
    }