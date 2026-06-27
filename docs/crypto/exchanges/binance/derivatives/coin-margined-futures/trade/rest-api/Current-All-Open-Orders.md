---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/coin-margined-futures/trade/rest-api/Current-All-Open-Orders
api_type: Trading
updated_at: 2026-01-15T23:39:44.350383
---

# Current All Open Orders (USER_DATA)

## API Description[​](/docs/derivatives/coin-margined-futures/trade/rest-api/Current-All-Open-Orders#api-description "Direct link to API Description")

Get all open orders on a symbol. **Careful** when accessing this with no symbol.

## HTTP Request[​](/docs/derivatives/coin-margined-futures/trade/rest-api/Current-All-Open-Orders#http-request "Direct link to HTTP Request")

GET `/dapi/v1/openOrders`

## Request Weight[​](/docs/derivatives/coin-margined-futures/trade/rest-api/Current-All-Open-Orders#request-weight "Direct link to Request Weight")

**1** for a single symbol, **40** for mutltiple symbols

## Request Parameters[​](/docs/derivatives/coin-margined-futures/trade/rest-api/Current-All-Open-Orders#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
symbol| STRING| NO|   
pair| STRING| NO|   
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## Response Example[​](/docs/derivatives/coin-margined-futures/trade/rest-api/Current-All-Open-Orders#response-example "Direct link to Response Example")
    
    
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
      	"time": 1579276756075,				// order time  
      	"timeInForce": "GTC",  
      	"type": "TRAILING_STOP_MARKET",  
      	"activatePrice": "9020",			// activation price, only return with TRAILING_STOP_MARKET order  
      	"priceRate": "0.3",					// callback rate, only return with TRAILING_STOP_MARKET order  
      	"updateTime": 1579276756075,		// update time  
      	"workingType": "CONTRACT_PRICE",  
      	"priceProtect": false,              // if conditional order trigger is protected  
      	"priceMatch": "NONE",               //price match mode  
      	"selfTradePreventionMode": "NONE"   //self trading preventation mode  
      }  
    ]

---

# 查看当前全部挂单(USER_DATA)

## 接口描述[​](/docs/zh-CN/derivatives/coin-margined-futures/trade/rest-api/Current-All-Open-Orders#接口描述 "接口描述的直接链接")

查看当前全部挂单

## HTTP请求[​](/docs/zh-CN/derivatives/coin-margined-futures/trade/rest-api/Current-All-Open-Orders#http请求 "HTTP请求的直接链接")

GET `/dapi/v1/openOrders`

## 请求权重[​](/docs/zh-CN/derivatives/coin-margined-futures/trade/rest-api/Current-All-Open-Orders#请求权重 "请求权重的直接链接")

请小心使用不带symbol参数的调用

带symbol **1** ，不带symbol **40**

## 请求参数[​](/docs/zh-CN/derivatives/coin-margined-futures/trade/rest-api/Current-All-Open-Orders#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
symbol| STRING| NO| 交易对  
pair| STRING| NO| 标的交易对  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## 响应示例[​](/docs/zh-CN/derivatives/coin-margined-futures/trade/rest-api/Current-All-Open-Orders#响应示例 "响应示例的直接链接")
    
    
    [  
      {  
      	"avgPrice": "0.0",				// 平均成交价  
      	"clientOrderId": "abc",				// 用户自定义的订单号  
      	"cumBase": "0", 						// 成交金额(标的数量)  
      	"executedQty": "0",					// 成交量(张数)  
      	"orderId": 1917641,					// 系统订单号  
      	"origQty": "0.40",					// 原始委托数量  
      	"origType": "TRAILING_STOP_MARKET",	// 触发前订单类型  
      	"price": "0",					// 委托价格  
      	"reduceOnly": false,				// 是否仅减仓  
      	"side": "BUY",						// 买卖方向  
      	"positionSide": "SHORT", // 持仓方向  
      	"status": "NEW",					// 订单状态  
      	"stopPrice": "9300",					// 触发价,对`TRAILING_STOP_MARKET`无效  
      	"closePosition": false,   // 是否条件全平仓  
      	"symbol": "BTCUSD_200925",				// 交易对  
      	"pair": "BTCUSD",	// 标的交易对  
      	"time": 1579276756075,				// 订单时间  
      	"timeInForce": "GTC",				// 有效方法  
      	"type": "TRAILING_STOP_MARKET",		// 订单类型  
      	"activatePrice": "9020", // 跟踪止损激活价格, 仅`TRAILING_STOP_MARKET` 订单返回此字段  
      	"priceRate": "0.3",	// 跟踪止损回调比例, 仅`TRAILING_STOP_MARKET` 订单返回此字段  
      	"updateTime": 1579276756075,		// 更新时间  
      	"workingType": "CONTRACT_PRICE",		// 条件价格触发类型  
      	"priceProtect": false,            // 是否开启条件单触发保护  
      	"priceMatch": "NONE",               //盘口价格下单模式  
      	"selfTradePreventionMode": "NONE",  //订单自成交保护模式   
      }  
    ]