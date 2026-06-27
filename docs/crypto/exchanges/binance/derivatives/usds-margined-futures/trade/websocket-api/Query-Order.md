---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/usds-margined-futures/trade/websocket-api/Query-Order
api_type: WebSocket
updated_at: 2026-01-15T23:47:37.736135
---

# Query Order (USER_DATA)

## API Description[​](/docs/derivatives/usds-margined-futures/trade/websocket-api/Query-Order#api-description "Direct link to API Description")

Check an order's status.

  * These orders will not be found: 
    * order status is `CANCELED` or `EXPIRED` **AND** order has NO filled trade **AND** created time + 3 days < current time
    * order create time + 90 days < current time



## Method[​](/docs/derivatives/usds-margined-futures/trade/websocket-api/Query-Order#method "Direct link to Method")

`order.status`

## Request[​](/docs/derivatives/usds-margined-futures/trade/websocket-api/Query-Order#request "Direct link to Request")
    
    
    {  
        "id": "0ce5d070-a5e5-4ff2-b57f-1556741a4204",  
        "method": "order.status",  
        "params": {  
            "apiKey": "HMOchcfii9ZRZnhjp2XjGXhsOBd6msAhKz9joQaWwZ7arcJTlD2hGPHQj1lGdTjR",  
            "orderId": 328999071,  
            "symbol": "BTCUSDT",  
            "timestamp": 1703441060152,  
            "signature": "ba48184fc38a71d03d2b5435bd67c1206e3191e989fe99bda1bc643a880dfdbf"  
        }  
    }  
    

## Request Weight[​](/docs/derivatives/usds-margined-futures/trade/websocket-api/Query-Order#request-weight "Direct link to Request Weight")

**1**

## Request Parameters[​](/docs/derivatives/usds-margined-futures/trade/websocket-api/Query-Order#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
symbol| STRING| YES|   
orderId| LONG| NO|   
origClientOrderId| STRING| NO|   
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
Notes:

>   * Either `orderId` or `origClientOrderId` must be sent.
>   * `orderId` is self-increment for each specific `symbol`
> 


## Response Example[​](/docs/derivatives/usds-margined-futures/trade/websocket-api/Query-Order#response-example "Direct link to Response Example")
    
    
    {  
     "id": "605a6d20-6588-4cb9-afa0-b0ab087507ba",  
     "status": 200,  
     "result": {  
      "avgPrice": "0.00000",  
      "clientOrderId": "abc",  
      "cumQuote": "0",  
      "executedQty": "0",  
      "orderId": 1917641,  
      "origQty": "0.40",  
      "origType": "TRAILING_STOP_MARKET",  
      "price": "0",  
      "reduceOnly": false,  
      "side": "BUY",  
      "positionSide": "SHORT",  
      "status": "NEW",  
      "stopPrice": "9300",    // please ignore when order type is TRAILING_STOP_MARKET  
      "closePosition": false,   // if Close-All  
      "symbol": "BTCUSDT",  
      "time": 1579276756075,    // order time  
      "timeInForce": "GTC",  
      "type": "TRAILING_STOP_MARKET",  
      "activatePrice": "9020",   // activation price, only return with TRAILING_STOP_MARKET order  
      "priceRate": "0.3",     // callback rate, only return with TRAILING_STOP_MARKET order  
      "updateTime": 1579276756075,  // update time  
      "workingType": "CONTRACT_PRICE",  
      "priceProtect": false            // if conditional order trigger is protected  
     }  
    }

---

# 查询订单 (USER_DATA)

## 接口描述[​](/docs/zh-CN/derivatives/usds-margined-futures/trade/websocket-api/Query-Order#接口描述 "接口描述的直接链接")

查询订单状态

  * 请注意，如果订单满足如下条件，不会被查询到： 
    * 订单的最终状态为 `CANCELED` 或者 `EXPIRED` **并且** 订单没有任何的成交记录 **并且** 订单生成时间 + 3天 < 当前时间
    * 订单创建时间 + 90天 < 当前时间



## 方式[​](/docs/zh-CN/derivatives/usds-margined-futures/trade/websocket-api/Query-Order#方式 "方式的直接链接")

`order.status`

## 请求[​](/docs/zh-CN/derivatives/usds-margined-futures/trade/websocket-api/Query-Order#请求 "请求的直接链接")
    
    
    {  
        "id": "0ce5d070-a5e5-4ff2-b57f-1556741a4204",  
        "method": "order.status",  
        "params": {  
            "apiKey": "HMOchcfii9ZRZnhjp2XjGXhsOBd6msAhKz9joQaWwZ7arcJTlD2hGPHQj1lGdTjR",  
            "orderId": 328999071,  
            "symbol": "BTCUSDT",  
            "timestamp": 1703441060152,  
            "signature": "ba48184fc38a71d03d2b5435bd67c1206e3191e989fe99bda1bc643a880dfdbf"  
        }  
    }  
    

## 请求权重[​](/docs/zh-CN/derivatives/usds-margined-futures/trade/websocket-api/Query-Order#请求权重 "请求权重的直接链接")

**1**

## 请求参数[​](/docs/zh-CN/derivatives/usds-margined-futures/trade/websocket-api/Query-Order#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
symbol| STRING| YES| 交易对  
orderId| LONG| NO| 系统订单号  
origClientOrderId| STRING| NO| 用户自定义的订单号  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
注意:

>   * 至少需要发送 `orderId` 与 `origClientOrderId`中的一个
>   * `orderId`在`symbol`维度是自增的
> 


## 响应示例[​](/docs/zh-CN/derivatives/usds-margined-futures/trade/websocket-api/Query-Order#响应示例 "响应示例的直接链接")
    
    
    {  
      	"avgPrice": "0.00000",				// 平均成交价  
      	"clientOrderId": "abc",				// 用户自定义的订单号  
      	"cumQuote": "0",					// 成交金额  
      	"executedQty": "0",					// 成交量  
      	"orderId": 1573346959,				// 系统订单号  
      	"origQty": "0.40",					// 原始委托数量  
      	"origType": "TRAILING_STOP_MARKET",	// 触发前订单类型  
      	"price": "0",						// 委托价格  
      	"reduceOnly": false,				// 是否仅减仓  
      	"side": "BUY",						// 买卖方向  
      	"positionSide": "SHORT", 			// 持仓方向  
      	"status": "NEW",					// 订单状态  
      	"stopPrice": "9300",			    // 触发价，对`TRAILING_STOP_MARKET`无效  
      	"closePosition": false,             // 是否条件全平仓  
      	"symbol": "BTCUSDT",				// 交易对  
      	"time": 1579276756075,				// 订单时间  
      	"timeInForce": "GTC",				// 有效方法  
      	"type": "TRAILING_STOP_MARKET",		// 订单类型  
      	"activatePrice": "9020",			// 跟踪止损激活价格, 仅`TRAILING_STOP_MARKET` 订单返回此字段  
      	"priceRate": "0.3",					// 跟踪止损回调比例, 仅`TRAILING_STOP_MARKET` 订单返回此字段  
      	"updateTime": 1579276756075,		// 更新时间  
      	"workingType": "CONTRACT_PRICE",    // 条件价格触发类型  
     	"priceProtect": false               // 是否开启条件单触发保护  
    }