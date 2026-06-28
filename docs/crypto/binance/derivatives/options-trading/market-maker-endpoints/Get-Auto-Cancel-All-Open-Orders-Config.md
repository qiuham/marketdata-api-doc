---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/options-trading/market-maker-endpoints/Get-Auto-Cancel-All-Open-Orders-Config
api_type: Market Data
updated_at: 2026-01-15T23:42:11.178084
---

# Get Auto-Cancel All Open Orders (Kill-Switch) Config (TRADE)

## API Description[​](/docs/derivatives/options-trading/market-maker-endpoints/Get-Auto-Cancel-All-Open-Orders-Config#api-description "Direct link to API Description")

This endpoint returns the auto-cancel parameters for each underlying symbol. Note only active auto-cancel parameters will be returned, if countdownTime is set to 0 (ie. countdownTime has been turned off), the underlying symbol and corresponding countdownTime parameter will not be returned in the response.

## HTTP Request[​](/docs/derivatives/options-trading/market-maker-endpoints/Get-Auto-Cancel-All-Open-Orders-Config#http-request "Direct link to HTTP Request")

GET `/eapi/v1/countdownCancelAll` 

## Request Weight[​](/docs/derivatives/options-trading/market-maker-endpoints/Get-Auto-Cancel-All-Open-Orders-Config#request-weight "Direct link to Request Weight")

1

## Request Parameters[​](/docs/derivatives/options-trading/market-maker-endpoints/Get-Auto-Cancel-All-Open-Orders-Config#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
underlying| STRING| NO| Option underlying, e.g BTCUSDT  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
>   * countdownTime = 0 means the function is disabled.
> 


## Response Example[​](/docs/derivatives/options-trading/market-maker-endpoints/Get-Auto-Cancel-All-Open-Orders-Config#response-example "Direct link to Response Example")
    
    
    {  
      "underlying": "ETHUSDT",  
      "countdownTime": 100000  
    }

---

# 获得倒计时自动取消所有订单配置 (TRADE)

## 接口描述[​](/docs/zh-CN/derivatives/options-trading/market-maker-endpoints/Get-Auto-Cancel-All-Open-Orders-Config#接口描述 "接口描述的直接链接")

本接口用于获得倒计时自动取消所有订单配置。接口仅返回有效的自动取消参数，如果标的资产的`countdownTime`设置为0，该标的资产对应的参数不会被返回。

## HTTP请求[​](/docs/zh-CN/derivatives/options-trading/market-maker-endpoints/Get-Auto-Cancel-All-Open-Orders-Config#http请求 "HTTP请求的直接链接")

GET `/eapi/v1/countdownCancelAll`

## 请求权重[​](/docs/zh-CN/derivatives/options-trading/market-maker-endpoints/Get-Auto-Cancel-All-Open-Orders-Config#请求权重 "请求权重的直接链接")

**1**

## 请求参数[​](/docs/zh-CN/derivatives/options-trading/market-maker-endpoints/Get-Auto-Cancel-All-Open-Orders-Config#请求参数 "请求参数的直接链接")

名称| 类型| 是否必须| 描述  
---|---|---|---  
underlying| STRING| YES| 期权标的资产， 如BTCUSDT  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
>   * 当countdownTime = 0时倒计时取消所有订单功能关闭
> 


## 响应示例[​](/docs/zh-CN/derivatives/options-trading/market-maker-endpoints/Get-Auto-Cancel-All-Open-Orders-Config#响应示例 "响应示例的直接链接")
    
    
    {  
      "underlying": "ETHUSDT",  
      "countdownTime": 100000  
    }