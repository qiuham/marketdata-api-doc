---
exchange: binance
source_url: https://developers.binance.com/docs/margin_trading/risk-data-stream/Event-Liability-Update
api_type: REST
updated_at: 2026-06-28 18:52:10.485715
---

# Keepalive User Data Stream (USER_STREAM)

## API Description[​](/docs/margin_trading/risk-data-stream/Keepalive-User-Data-Stream#api-description "Direct link to API Description")

Keepalive a user data stream to prevent a time out.

## HTTP Request[​](/docs/margin_trading/risk-data-stream/Keepalive-User-Data-Stream#http-request "Direct link to HTTP Request")

PUT `/sapi/v1/margin/listen-key`

## Request Weight(UID)[​](/docs/margin_trading/risk-data-stream/Keepalive-User-Data-Stream#request-weightuid "Direct link to Request Weight\(UID\)")

**1**

## Request Parameters[​](/docs/margin_trading/risk-data-stream/Keepalive-User-Data-Stream#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
listenKey| STRING| YES|   
  
## Response Example[​](/docs/margin_trading/risk-data-stream/Keepalive-User-Data-Stream#response-example "Direct link to Response Example")
    
    
    {}

---

# 延长listenKey有效期(USER_STREAM)

## 接口描述[​](/docs/zh-CN/margin_trading/risk-data-stream/Keepalive-User-Data-Stream#接口描述 "接口描述的直接链接")

有效期延长至本次调用后24小时。

## HTTP请求[​](/docs/zh-CN/margin_trading/risk-data-stream/Keepalive-User-Data-Stream#http请求 "HTTP请求的直接链接")

PUT `/sapi/v1/margin/listen-key`

## 请求权重(UID)[​](/docs/zh-CN/margin_trading/risk-data-stream/Keepalive-User-Data-Stream#请求权重uid "请求权重\(UID\)的直接链接")

**1**

## 请求参数[​](/docs/zh-CN/margin_trading/risk-data-stream/Keepalive-User-Data-Stream#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
listenKey| STRING| YES|   
      
    
    {}