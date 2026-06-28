---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/options-trading/market-maker-endpoints/Auto-Cancel-All-Open-Orders-Heartbeat
api_type: Market Data
updated_at: 2026-01-15T23:42:11.098218
---

# Auto-Cancel All Open Orders (Kill-Switch) Heartbeat (TRADE)

## API Description[​](/docs/derivatives/options-trading/market-maker-endpoints/Auto-Cancel-All-Open-Orders-Heartbeat#api-description "Direct link to API Description")

This endpoint resets the time from which the countdown will begin to the time this messaged is received. It should be called repeatedly as heartbeats. Multiple heartbeats can be updated at once by specifying the underlying symbols as a list (ex. BTCUSDT,ETHUSDT) in the underlyings parameter.

## HTTP Request[​](/docs/derivatives/options-trading/market-maker-endpoints/Auto-Cancel-All-Open-Orders-Heartbeat#http-request "Direct link to HTTP Request")

POST `/eapi/v1/countdownCancelAllHeartBeat`

## Request Weight[​](/docs/derivatives/options-trading/market-maker-endpoints/Auto-Cancel-All-Open-Orders-Heartbeat#request-weight "Direct link to Request Weight")

10

## Request Parameters[​](/docs/derivatives/options-trading/market-maker-endpoints/Auto-Cancel-All-Open-Orders-Heartbeat#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
underlyings| STRING| YES| Option Underlying Symbols, e.g BTCUSDT,ETHUSDT  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
>   * The response will only include underlying symbols where the heartbeat has been successfully updated.
> 


## Response Example[​](/docs/derivatives/options-trading/market-maker-endpoints/Auto-Cancel-All-Open-Orders-Heartbeat#response-example "Direct link to Response Example")
    
    
    {  
     "underlyings":["BTCUSDT","ETHUSDT"]  
    }

---

# 重置倒计时取消所有订单心跳 (TRADE)

## 接口描述[​](/docs/zh-CN/derivatives/options-trading/market-maker-endpoints/Auto-Cancel-All-Open-Orders-Heartbeat#接口描述 "接口描述的直接链接")

本接口用户更新倒计时取消所有订单心跳。本接口需要作为心跳更新被频繁调用。将多个标的资产以list形式传入`underlyings`可以同时更新多个标的资产的心跳。

## HTTP请求[​](/docs/zh-CN/derivatives/options-trading/market-maker-endpoints/Auto-Cancel-All-Open-Orders-Heartbeat#http请求 "HTTP请求的直接链接")

POST `/eapi/v1/countdownCancelAllHeartBeat`

## 请求权重[​](/docs/zh-CN/derivatives/options-trading/market-maker-endpoints/Auto-Cancel-All-Open-Orders-Heartbeat#请求权重 "请求权重的直接链接")

**10**

## 请求参数[​](/docs/zh-CN/derivatives/options-trading/market-maker-endpoints/Auto-Cancel-All-Open-Orders-Heartbeat#请求参数 "请求参数的直接链接")

名称| 类型| 是否必须| 描述  
---|---|---|---  
underlyings| STRING| YES| 期权标的资产， 如BTCUSDT  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
>   * 响应仅包含心跳已被更新的标的资产
> 


## 响应示例[​](/docs/zh-CN/derivatives/options-trading/market-maker-endpoints/Auto-Cancel-All-Open-Orders-Heartbeat#响应示例 "响应示例的直接链接")
    
    
    {  
     "underlyings":["BTCUSDT","ETHUSDT"]  
    }