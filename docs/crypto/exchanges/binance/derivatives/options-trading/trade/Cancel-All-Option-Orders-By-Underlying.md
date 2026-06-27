---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/options-trading/trade/Cancel-All-Option-Orders-By-Underlying
api_type: Trading
updated_at: 2026-01-15T23:42:29.399919
---

# Cancel All Option Orders By Underlying (TRADE)

## API Description[​](/docs/derivatives/options-trading/trade/Cancel-All-Option-Orders-By-Underlying#api-description "Direct link to API Description")

Cancel all active orders on specified underlying.

## HTTP Request[​](/docs/derivatives/options-trading/trade/Cancel-All-Option-Orders-By-Underlying#http-request "Direct link to HTTP Request")

DELETE `/eapi/v1/allOpenOrdersByUnderlying`

## Request Weight[​](/docs/derivatives/options-trading/trade/Cancel-All-Option-Orders-By-Underlying#request-weight "Direct link to Request Weight")

**1**

## Request Parameters[​](/docs/derivatives/options-trading/trade/Cancel-All-Option-Orders-By-Underlying#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
underlying| STRING| YES| Option underlying, e.g BTCUSDT  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## Response Example[​](/docs/derivatives/options-trading/trade/Cancel-All-Option-Orders-By-Underlying#response-example "Direct link to Response Example")
    
    
    {  
        "code": 0,  
        "msg": "success",  
    }

---

# 撤销特定标的全部订单(TRADE)

## 接口描述[​](/docs/zh-CN/derivatives/options-trading/trade/Cancel-All-Option-Orders-By-Underlying#接口描述 "接口描述的直接链接")

撤销特定标的全部订单

## HTTP请求[​](/docs/zh-CN/derivatives/options-trading/trade/Cancel-All-Option-Orders-By-Underlying#http请求 "HTTP请求的直接链接")

DELETE `/eapi/v1/allOpenOrdersByUnderlying`

## 请求权重[​](/docs/zh-CN/derivatives/options-trading/trade/Cancel-All-Option-Orders-By-Underlying#请求权重 "请求权重的直接链接")

**1**

## 请求参数[​](/docs/zh-CN/derivatives/options-trading/trade/Cancel-All-Option-Orders-By-Underlying#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
underlying| STRING| YES| 标的资产如BTCUSDT  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## 响应示例[​](/docs/zh-CN/derivatives/options-trading/trade/Cancel-All-Option-Orders-By-Underlying#响应示例 "响应示例的直接链接")
    
    
    {  
        "code": 0,  
        "msg": "success",  
    }