---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/portfolio-margin/user-data-streams/Keepalive-User-Data-Stream
api_type: REST
updated_at: 2026-01-15T23:46:10.041098
---

# Keepalive User Data Stream (USER_STREAM)

## API Description[​](/docs/derivatives/portfolio-margin/user-data-streams/Keepalive-User-Data-Stream#api-description "Direct link to API Description")

Keepalive a user data stream to prevent a time out. User data streams will close after 60 minutes. It's recommended to send a ping about every 60 minutes.

## HTTP Request[​](/docs/derivatives/portfolio-margin/user-data-streams/Keepalive-User-Data-Stream#http-request "Direct link to HTTP Request")

PUT `/papi/v1/listenKey`

## Request Weight[​](/docs/derivatives/portfolio-margin/user-data-streams/Keepalive-User-Data-Stream#request-weight "Direct link to Request Weight")

**1**

## Request Parameters[​](/docs/derivatives/portfolio-margin/user-data-streams/Keepalive-User-Data-Stream#request-parameters "Direct link to Request Parameters")

**None**

## Response Example[​](/docs/derivatives/portfolio-margin/user-data-streams/Keepalive-User-Data-Stream#response-example "Direct link to Response Example")
    
    
    {}

---

# 延长listenKey有效期(USER_STREAM)

## 接口描述[​](/docs/zh-CN/derivatives/portfolio-margin/user-data-streams/Keepalive-User-Data-Stream#接口描述 "接口描述的直接链接")

有效期延长至本次调用后60分钟

## HTTP请求[​](/docs/zh-CN/derivatives/portfolio-margin/user-data-streams/Keepalive-User-Data-Stream#http请求 "HTTP请求的直接链接")

PUT `/papi/v1/listenKey`

## 请求权重[​](/docs/zh-CN/derivatives/portfolio-margin/user-data-streams/Keepalive-User-Data-Stream#请求权重 "请求权重的直接链接")

**1**

## 请求参数[​](/docs/zh-CN/derivatives/portfolio-margin/user-data-streams/Keepalive-User-Data-Stream#请求参数 "请求参数的直接链接")

**None**

## 响应示例[​](/docs/zh-CN/derivatives/portfolio-margin/user-data-streams/Keepalive-User-Data-Stream#响应示例 "响应示例的直接链接")
    
    
    {}