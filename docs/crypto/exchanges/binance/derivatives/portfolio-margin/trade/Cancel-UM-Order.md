---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/portfolio-margin/trade/Cancel-UM-Order
api_type: Trading
updated_at: 2026-01-15T23:45:28.948688
---

# Cancel UM Order(TRADE)

## API Description[​](/docs/derivatives/portfolio-margin/trade/Cancel-UM-Order#api-description "Direct link to API Description")

Cancel an active UM LIMIT order

## HTTP Request[​](/docs/derivatives/portfolio-margin/trade/Cancel-UM-Order#http-request "Direct link to HTTP Request")

DELETE `/papi/v1/um/order`

## Request Weight[​](/docs/derivatives/portfolio-margin/trade/Cancel-UM-Order#request-weight "Direct link to Request Weight")

**1**

## Request Parameters[​](/docs/derivatives/portfolio-margin/trade/Cancel-UM-Order#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
symbol| STRING| YES|   
orderId| LONG| NO|   
origClientOrderId| STRING| NO|   
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
>   * Either `orderId` or `origClientOrderId` must be sent.
> 


## Response Example[​](/docs/derivatives/portfolio-margin/trade/Cancel-UM-Order#response-example "Direct link to Response Example")
    
    
    {  
        "avgPrice": "0.00000",  
        "clientOrderId": "myOrder1",  
        "cumQty": "0",  
        "cumQuote": "0",  
        "executedQty": "0",  
        "orderId": 4611875134427365377,  
        "origQty": "0.40",  
        "price": "0",  
        "reduceOnly": false,  
        "side": "BUY",  
        "positionSide": "SHORT",  
        "status": "CANCELED",  
        "symbol": "BTCUSDT",  
        "timeInForce": "GTC",  
        "type": "LIMIT",  
        "updateTime": 1571110484038,  
        "selfTradePreventionMode": "NONE",   
        "goodTillDate": 0,  
        "priceMatch": "NONE"    
    }

---

# 撤销UM订单 (TRADE)

## 接口描述[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Cancel-UM-Order#接口描述 "接口描述的直接链接")

撤销UM订单

## HTTP请求[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Cancel-UM-Order#http请求 "HTTP请求的直接链接")

DELETE `/papi/v1/um/order`

## 请求权重[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Cancel-UM-Order#请求权重 "请求权重的直接链接")

**1**

## 请求参数[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Cancel-UM-Order#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
symbol| STRING| YES|   
orderId| LONG| NO|   
origClientOrderId| STRING| NO|   
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
>   * `orderId` 或 `origClientOrderId` 必须至少发送一个
> 


## 响应示例[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Cancel-UM-Order#响应示例 "响应示例的直接链接")
    
    
    {  
        "avgPrice": "0.00000",  
        "clientOrderId": "myOrder1",  
        "cumQty": "0",  
        "cumQuote": "0",  
        "executedQty": "0",  
        "orderId": 4611875134427365377,  
        "origQty": "0.40",  
        "price": "0",  
        "reduceOnly": false,  
        "side": "BUY",  
        "positionSide": "SHORT",  
        "status": "CANCELED",  
        "symbol": "BTCUSDT",  
        "timeInForce": "GTC",  
        "type": "LIMIT",  
        "updateTime": 1571110484038,  
        "selfTradePreventionMode": "NONE",   
        "goodTillDate": 0,  
        "priceMatch": "NONE"    
    }