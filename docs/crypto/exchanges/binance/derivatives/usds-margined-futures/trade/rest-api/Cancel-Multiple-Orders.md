---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/usds-margined-futures/trade/rest-api/Cancel-Multiple-Orders
api_type: Trading
updated_at: 2026-01-15T23:47:13.086838
---

# Cancel Multiple Orders (TRADE)

## API Description[​](/docs/derivatives/usds-margined-futures/trade/rest-api/Cancel-Multiple-Orders#api-description "Direct link to API Description")

Cancel Multiple Orders

## HTTP Request[​](/docs/derivatives/usds-margined-futures/trade/rest-api/Cancel-Multiple-Orders#http-request "Direct link to HTTP Request")

DELETE `/fapi/v1/batchOrders`

## Request Weight[​](/docs/derivatives/usds-margined-futures/trade/rest-api/Cancel-Multiple-Orders#request-weight "Direct link to Request Weight")

**1**

## Request Parameters[​](/docs/derivatives/usds-margined-futures/trade/rest-api/Cancel-Multiple-Orders#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
symbol| STRING| YES|   
orderIdList| LIST<LONG>| NO| max length 10   
e.g. [1234567,2345678]  
origClientOrderIdList| LIST<STRING>| NO| max length 10  
e.g. ["my_id_1","my_id_2"], encode the double quotes. No space after comma.  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
>   * Either `orderIdList` or `origClientOrderIdList ` must be sent.
> 


## Response Example[​](/docs/derivatives/usds-margined-futures/trade/rest-api/Cancel-Multiple-Orders#response-example "Direct link to Response Example")
    
    
    [  
    	{  
    	 	"clientOrderId": "myOrder1",  
    	 	"cumQty": "0",  
    	 	"cumQuote": "0",  
    	 	"executedQty": "0",  
    	 	"orderId": 283194212,  
    	 	"origQty": "11",  
    	 	"origType": "TRAILING_STOP_MARKET",  
      		"price": "0",  
      		"reduceOnly": false,  
      		"side": "BUY",  
      		"positionSide": "SHORT",  
      		"status": "CANCELED",  
      		"stopPrice": "9300",				// please ignore when order type is TRAILING_STOP_MARKET  
      		"closePosition": false,   // if Close-All  
      		"symbol": "BTCUSDT",  
      		"timeInForce": "GTC",  
      		"type": "TRAILING_STOP_MARKET",  
      		"activatePrice": "9020",			// activation price, only return with TRAILING_STOP_MARKET order  
      		"priceRate": "0.3",					// callback rate, only return with TRAILING_STOP_MARKET order  
    	 	"updateTime": 1571110484038,  
    	 	"workingType": "CONTRACT_PRICE",  
    	 	"priceProtect": false,            // if conditional order trigger is protected	  
    	 	"priceMatch": "NONE",              //price match mode  
    	 	"selfTradePreventionMode": "NONE", //self trading preventation mode  
    	 	"goodTillDate": 1693207680000      //order pre-set auot cancel time for TIF GTD order  
    	},  
    	{  
    		"code": -2011,  
    		"msg": "Unknown order sent."  
    	}  
    ]

---

# 批量撤销订单(TRADE)

## 接口描述[​](/docs/zh-CN/derivatives/usds-margined-futures/trade/rest-api/Cancel-Multiple-Orders#接口描述 "接口描述的直接链接")

批量撤销订单 (TRADE)

## HTTP Request[​](/docs/zh-CN/derivatives/usds-margined-futures/trade/rest-api/Cancel-Multiple-Orders#http-request "HTTP Request的直接链接")

DELETE `/fapi/v1/batchOrders`

## 请求权重[​](/docs/zh-CN/derivatives/usds-margined-futures/trade/rest-api/Cancel-Multiple-Orders#请求权重 "请求权重的直接链接")

**1**

## 请求参数[​](/docs/zh-CN/derivatives/usds-margined-futures/trade/rest-api/Cancel-Multiple-Orders#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
symbol| STRING| YES| 交易对  
orderIdList| LIST<LONG>| NO| 系统订单号, 最多支持10个订单   
  
比如`[1234567,2345678]`  
origClientOrderIdList| LIST<STRING>| NO| 用户自定义的订单号, 最多支持10个订单   
  
比如`["my_id_1","my_id_2"]` 需要encode双引号。逗号后面没有空格。  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
>   * `orderIdList` 与 `origClientOrderIdList` 必须至少发送一个，不可同时发送
> 


## Response Example[​](/docs/zh-CN/derivatives/usds-margined-futures/trade/rest-api/Cancel-Multiple-Orders#response-example "Response Example的直接链接")
    
    
    [  
    	{  
    	 	"clientOrderId": "myOrder1", // 用户自定义的订单号  
    	 	"cumQty": "0",  
    	 	"cumQuote": "0", // 成交金额  
    	 	"executedQty": "0", // 成交量  
    	 	"orderId": 283194212, // 系统订单号  
    	 	"origQty": "11", // 原始委托数量  
    	 	"price": "0", // 委托价格  
    		"reduceOnly": false, // 仅减仓  
    		"side": "BUY", // 买卖方向  
    		"positionSide": "SHORT", // 持仓方向  
    	 	"status": "CANCELED", // 订单状态  
    	 	"stopPrice": "9300", // 触发价，对`TRAILING_STOP_MARKET`无效  
    	 	"closePosition": false,   // 是否条件全平仓  
    	 	"symbol": "BTCUSDT", // 交易对  
    	 	"timeInForce": "GTC", // 有效方法  
    	 	"origType": "TRAILING_STOP_MARKET", // 触发前订单类型  
     		"type": "TRAILING_STOP_MARKET", // 订单类型  
    	 	"activatePrice": "9020", // 跟踪止损激活价格, 仅`TRAILING_STOP_MARKET` 订单返回此字段  
      		"priceRate": "0.3",	// 跟踪止损回调比例, 仅`TRAILING_STOP_MARKET` 订单返回此字段  
    	 	"updateTime": 1571110484038, // 更新时间  
    	 	"workingType": "CONTRACT_PRICE", // 条件价格触发类型  
    	 	"priceProtect": false            // 是否开启条件单触发保护  
    	 	"priceMatch": "NONE",              //盘口价格下单模式  
    	 	"selfTradePreventionMode": "NONE", //订单自成交保护模式  
     		"goodTillDate": 0      //订单TIF为GTD时的自动取消时间  
    	},  
    	{  
    		"code": -2011,  
    		"msg": "Unknown order sent."  
    	}  
    ]