---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/portfolio-margin/trade/Query-Current-CM-Open-Order
api_type: Trading
updated_at: 2026-01-15T23:45:48.679079
---

# Query Current CM Open Order (USER_DATA)

## API Description[​](/docs/derivatives/portfolio-margin/trade/Query-Current-CM-Open-Order#api-description "Direct link to API Description")

Query current CM open order

## HTTP Request[​](/docs/derivatives/portfolio-margin/trade/Query-Current-CM-Open-Order#http-request "Direct link to HTTP Request")

GET `/papi/v1/cm/openOrder`

## Request Weight[​](/docs/derivatives/portfolio-margin/trade/Query-Current-CM-Open-Order#request-weight "Direct link to Request Weight")

**1**

## Request Parameters[​](/docs/derivatives/portfolio-margin/trade/Query-Current-CM-Open-Order#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
symbol| STRING| YES|   
orderId| LONG| NO|   
origClientOrderId| STRING| NO|   
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
Notes:

>   * Either `orderId` or `origClientOrderId` must be sent.
>   * If the queried order has been filled or cancelled, the error message "Order does not exist" will be returned.
> 


## Response Example[​](/docs/derivatives/portfolio-margin/trade/Query-Current-CM-Open-Order#response-example "Direct link to Response Example")
    
    
    {  
        "avgPrice": "0.0",                
        "clientOrderId": "abc",               
        "cumBase": "0",                       
        "executedQty": "0",                   
        "orderId": 1917641,                   
        "origQty": "0.40",                        
        "origType": "LIMIT",  
        "price": "0",  
        "reduceOnly": false,  
        "side": "BUY",  
        "positionSide": "SHORT",  
        "status": "NEW",  
        "symbol": "BTCUSD_200925",  
        "pair": "BTCUSD"  
        "time": 1579276756075,              // order time  
        "timeInForce": "GTC",  
        "type": "LIMIT",  
        "updateTime": 1579276756075        // update time  
    }

---

# 查看当前全部CM挂单(USER_DATA)

## 接口描述[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-Current-CM-Open-Order#接口描述 "接口描述的直接链接")

查看当前全部CM挂单，请小心使用不带symbol参数的调用

## HTTP请求[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-Current-CM-Open-Order#http请求 "HTTP请求的直接链接")

GET `/papi/v1/cm/openOrders`

## 请求权重[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-Current-CM-Open-Order#请求权重 "请求权重的直接链接")

带symbol **1** ; 不带 **40**

## 请求参数[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-Current-CM-Open-Order#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
symbol| STRING| NO|   
pair| STRING| NO|   
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
注意：

  * 不带`symbol`参数，会返回所有交易对的挂单



## 响应示例[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-Current-CM-Open-Order#响应示例 "响应示例的直接链接")
    
    
    [  
      {  
        "avgPrice": "0.0",  
        "clientOrderId": "abc",  
        "cumBase": "0",  
        "executedQty": "0",  
        "orderId": 1917641,  
        "origQty": "0.40",  
        "origType": "LIMIT",  
        "price": "0",  
        "reduceOnly": false,  
        "side": "BUY",  
        "positionSide": "SHORT",  
        "status": "NEW",  
        "symbol": "BTCUSD_200925",  
        "pair":"BTCUSD",  
        "time": 1579276756075,                
        "timeInForce": "GTC",  
        "type": "LIMIT",  
        "updateTime": 1579276756075        
      }  
    ]