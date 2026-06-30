---
exchange: binance
source_url: https://developers.binance.com/docs/convert/quick-start
api_type: REST
updated_at: 2026-06-30 19:10:38.220382
---

# Accept Quote (TRADE)

## API Description[​](/docs/convert/trade/Accept-Quote#api-description "Direct link to API Description")

Accept the offered quote by quote ID.

## HTTP Request[​](/docs/convert/trade/Accept-Quote#http-request "Direct link to HTTP Request")

POST `/sapi/v1/convert/acceptQuote`

## Request Weight[​](/docs/convert/trade/Accept-Quote#request-weight "Direct link to Request Weight")

**500(UID)**

## Request Parameters[​](/docs/convert/trade/Accept-Quote#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
quoteId| STRING| YES|   
recvWindow| LONG| NO| The value cannot be greater than 60000  
timestamp| LONG| YES|   
  
## Response Example[​](/docs/convert/trade/Accept-Quote#response-example "Direct link to Response Example")
    
    
    {  
      "orderId":"933256278426274426",  
      "createTime":1623381330472,  
      "orderStatus":"PROCESS" //PROCESS/ACCEPT_SUCCESS/SUCCESS/FAIL  
    }

---

# 接受报价(TRADE)

## 接口描述[​](/docs/zh-CN/convert/trade/Accept-Quote#接口描述 "接口描述的直接链接")

通过 quote ID 来接受报价。

## HTTP请求[​](/docs/zh-CN/convert/trade/Accept-Quote#http请求 "HTTP请求的直接链接")

POST `/sapi/v1/convert/acceptQuote`

## 请求权重[​](/docs/zh-CN/convert/trade/Accept-Quote#请求权重 "请求权重的直接链接")

**500(UID)**

## 请求参数[​](/docs/zh-CN/convert/trade/Accept-Quote#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
quoteId| STRING| YES|   
recvWindow| LONG| NO| 此值不能大于 60000  
timestamp| LONG| YES|   
  
## 响应示例[​](/docs/zh-CN/convert/trade/Accept-Quote#响应示例 "响应示例的直接链接")
    
    
    {  
      "orderId":"933256278426274426",  
      "createTime":1623381330472,  
      "orderStatus":"PROCESS" //PROCESS/ACCEPT_SUCCESS/SUCCESS/FAIL  
    }