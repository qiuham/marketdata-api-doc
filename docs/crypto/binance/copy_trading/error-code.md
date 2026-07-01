---
exchange: binance
source_url: https://developers.binance.com/docs/copy_trading/error-code
api_type: REST
updated_at: 2026-07-01 19:12:08.187681
---

# Get Futures Lead Trader Status(TRADE)

## API Description[​](/docs/copy_trading/future-copy-trading#api-description "Direct link to API Description")

Get Futures Lead Trader Status

## HTTP Request[​](/docs/copy_trading/future-copy-trading#http-request "Direct link to HTTP Request")

GET `/sapi/v1/copyTrading/futures/userStatus`

## Request Weight(IP)[​](/docs/copy_trading/future-copy-trading#request-weightip "Direct link to Request Weight\(IP\)")

**1**

## Request Parameters[​](/docs/copy_trading/future-copy-trading#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
recvWindow| LONG| NO| The value cannot be greater than 60000  
timestamp| LONG| YES|   
  
## Response Example[​](/docs/copy_trading/future-copy-trading#response-example "Direct link to Response Example")
    
    
    {  
      "code": "000000",  
      "message": "success",  
      "data": {  
         "isLeadTrader": true,  
         "time": 1717382310843  
       },  
      "success": true  
    }

---

# 查询是否为带单员身份(TRADE)

## 接口描述[​](/docs/zh-CN/copy_trading/future-copy-trading#接口描述 "接口描述的直接链接")

查询是否为带单员身份

## HTTP请求[​](/docs/zh-CN/copy_trading/future-copy-trading#http请求 "HTTP请求的直接链接")

GET `/sapi/v1/copyTrading/futures/userStatus`

## 请求权重(IP)[​](/docs/zh-CN/copy_trading/future-copy-trading#请求权重ip "请求权重\(IP\)的直接链接")

**1**

## 请求参数[​](/docs/zh-CN/copy_trading/future-copy-trading#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
recvWindow| LONG| NO| 此值不能大于 60000  
timestamp| LONG| YES|   
  
## 响应示例[​](/docs/zh-CN/copy_trading/future-copy-trading#响应示例 "响应示例的直接链接")
    
    
    {  
      "code": "000000",  
      "message": "success",  
      "data": {  
         "isLeadTrader": true,  
         "time": 1717382310843  
       },  
      "success": true  
    }