---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/portfolio-margin/trade/Cancel-All-UM-Open-Conditional-Orders
api_type: Trading
updated_at: 2026-01-15T23:45:21.649101
---

# Cancel All UM Open Conditional Orders (TRADE)

## API Description[​](/docs/derivatives/portfolio-margin/trade/Cancel-All-UM-Open-Conditional-Orders#api-description "Direct link to API Description")

Cancel All UM Open Conditional Orders

## HTTP Request[​](/docs/derivatives/portfolio-margin/trade/Cancel-All-UM-Open-Conditional-Orders#http-request "Direct link to HTTP Request")

`DELETE /papi/v1/um/conditional/allOpenOrders`

## Request Weight(Order)[​](/docs/derivatives/portfolio-margin/trade/Cancel-All-UM-Open-Conditional-Orders#request-weightorder "Direct link to Request Weight\(Order\)")

**1**

## Request Parameters[​](/docs/derivatives/portfolio-margin/trade/Cancel-All-UM-Open-Conditional-Orders#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
symbol| STRING| YES|   
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## Response Example[​](/docs/derivatives/portfolio-margin/trade/Cancel-All-UM-Open-Conditional-Orders#response-example "Direct link to Response Example")
    
    
    {  
        "code": "200",   
        "msg": "The operation of cancel all conditional open order is done."  
    }

---

# 取消全部UM条件单(TRADE)

## 接口描述[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Cancel-All-UM-Open-Conditional-Orders#接口描述 "接口描述的直接链接")

取消全部UM条件单

## HTTP请求[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Cancel-All-UM-Open-Conditional-Orders#http请求 "HTTP请求的直接链接")

DELETE `/papi/v1/um/conditional/allOpenOrders`

## 请求权重(Order)[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Cancel-All-UM-Open-Conditional-Orders#请求权重order "请求权重\(Order\)的直接链接")

**1**

## 请求参数[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Cancel-All-UM-Open-Conditional-Orders#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
symbol| STRING| YES|   
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## 响应示例[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Cancel-All-UM-Open-Conditional-Orders#响应示例 "响应示例的直接链接")
    
    
    {  
        "code": "200",   
        "msg": "The operation of cancel all conditional open order is done."  
    }