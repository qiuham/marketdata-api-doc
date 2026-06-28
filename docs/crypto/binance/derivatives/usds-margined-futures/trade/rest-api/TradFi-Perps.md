---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/usds-margined-futures/trade/rest-api/TradFi-Perps
api_type: Trading
updated_at: 2026-01-15T23:47:31.635600
---

# Futures TradFi Perps Contract(USER_DATA)

## API Description[​](/docs/derivatives/usds-margined-futures/trade/rest-api/TradFi-Perps#api-description "Direct link to API Description")

Sign TradFi-Perps agreement contract

## HTTP Request[​](/docs/derivatives/usds-margined-futures/trade/rest-api/TradFi-Perps#http-request "Direct link to HTTP Request")

POST `/fapi/v1/stock/contract`

## Request Weigh[​](/docs/derivatives/usds-margined-futures/trade/rest-api/TradFi-Perps#request-weigh "Direct link to Request Weigh")

**50**

## Request Parameters[​](/docs/derivatives/usds-margined-futures/trade/rest-api/TradFi-Perps#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## Response Example[​](/docs/derivatives/usds-margined-futures/trade/rest-api/TradFi-Perps#response-example "Direct link to Response Example")
    
    
    {     
       "code": 200,  
    	"msg": "success"  
    }

---

# 传统金融合约协议(USER_DATA)

签署传统金融合约协议

## HTTP请求[​](/docs/zh-CN/derivatives/usds-margined-futures/trade/rest-api/TradFi-Perps#http请求 "HTTP请求的直接链接")

POST `/fapi/v1/stock/contract`

## 请求权重[​](/docs/zh-CN/derivatives/usds-margined-futures/trade/rest-api/TradFi-Perps#请求权重 "请求权重的直接链接")

**50**

## 请求参数[​](/docs/zh-CN/derivatives/usds-margined-futures/trade/rest-api/TradFi-Perps#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## 响应示例[​](/docs/zh-CN/derivatives/usds-margined-futures/trade/rest-api/TradFi-Perps#响应示例 "响应示例的直接链接")
    
    
    {     
       	"code": 200,  
    	"msg": "success"  
    }