---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/options-trading/market-maker-endpoints/Set-Auto-Cancel-All-Open-Orders-Config
api_type: Market Data
updated_at: 2026-01-15T23:42:11.340353
---

# Set Auto-Cancel All Open Orders (Kill-Switch) Config (TRADE)

## API Description[​](/docs/derivatives/options-trading/market-maker-endpoints/Set-Auto-Cancel-All-Open-Orders-Config#api-description "Direct link to API Description")

This endpoint sets the parameters of the auto-cancel feature which cancels all open orders (both market maker protection and non market maker protection order types) of the underlying symbol at the end of the specified countdown time period if no heartbeat message is sent. After the countdown time period, all open orders will be cancelled and new orders will be rejected with error code -2010 until either a heartbeat message is sent or the auto-cancel feature is turned off by setting countdownTime to 0.

## HTTP Request[​](/docs/derivatives/options-trading/market-maker-endpoints/Set-Auto-Cancel-All-Open-Orders-Config#http-request "Direct link to HTTP Request")

POST `/eapi/v1/countdownCancelAll`

## Request Weight[​](/docs/derivatives/options-trading/market-maker-endpoints/Set-Auto-Cancel-All-Open-Orders-Config#request-weight "Direct link to Request Weight")

**1**

## Request Parameters[​](/docs/derivatives/options-trading/market-maker-endpoints/Set-Auto-Cancel-All-Open-Orders-Config#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
underlying| STRING| YES| Option underlying, e.g BTCUSDT  
countdownTime| LONG| YES| Countdown time in milliseconds (ex. 1,000 for 1 second). 0 to disable the timer. Negative values (ex. -10000) are not accepted. Minimum acceptable value is 5,000   
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
>   * This rest endpoint sets up the parameters to cancel your open orders in case of an outage or disconnection.
>   * Example usage: Call this endpoint with a countdownTime value of 10000 (10 seconds) to turn on the auto-cancel feature. If the corresponding countdownCancelAllHeartBeat endpoint is not called within 10 seconds with the specified underlying symbol, all open orders of the specified symbol will be automatically canceled. If this endpoint is called with an countdownTime of 0, the countdown timer will be stopped.
>   * The system will check all countdowns approximately every 1000 milliseconds, **please note that sufficient redundancy should be considered when using this function**. We do not recommend setting the countdown time to be too precise or too small.
> 


## Response Example[​](/docs/derivatives/options-trading/market-maker-endpoints/Set-Auto-Cancel-All-Open-Orders-Config#response-example "Direct link to Response Example")
    
    
    {  
      "underlying": "ETHUSDT",  
      "countdownTime": 30000  
    }

---

# 设置倒计时取消所有订单配置 (TRADE)

## 接口描述[​](/docs/zh-CN/derivatives/options-trading/market-maker-endpoints/Set-Auto-Cancel-All-Open-Orders-Config#接口描述 "接口描述的直接链接")

此接口用于设置倒计时取消所有订单（包括做市商保护订单与普通订单）配置，即在倒计时结束前心跳没有更新，特定标的资产的所有订单会被取消。若倒计时结束前心跳没有更新，所有的订单将会被取消，同时新订单会返回错误代码-2010。可以通过设置`countdownTime`为0取消此功能。

## HTTP请求[​](/docs/zh-CN/derivatives/options-trading/market-maker-endpoints/Set-Auto-Cancel-All-Open-Orders-Config#http请求 "HTTP请求的直接链接")

POST `/eapi/v1/countdownCancelAll`

 

## 请求权重[​](/docs/zh-CN/derivatives/options-trading/market-maker-endpoints/Set-Auto-Cancel-All-Open-Orders-Config#请求权重 "请求权重的直接链接")

**1**

## 请求参数[​](/docs/zh-CN/derivatives/options-trading/market-maker-endpoints/Set-Auto-Cancel-All-Open-Orders-Config#请求参数 "请求参数的直接链接")

名称| 类型| 是否必须| 描述  
---|---|---|---  
underlying| STRING| YES| 期权标的资产， 如 BTCUSDT  
countdownTime| LONG| YES| 以毫秒计量倒计时长 (1000代表1秒)。 设为0时关闭倒计时。最小设为5000（负值无效）   
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
>   * 本接口用于配置网络中断情况下自动取消已有订单。
>   * 使用样例：对特定的标的资产调用本接口（使用参数countdownTime = 10000，10秒）打开自动取消所有订单功能。如果功能开启后任意10秒内没有对该标的资产调用`countdownCancelAllHeartBeat`接口，则该标的资产上所有订单被去取消。如果调用接口时传参countdownTime = 0，倒计时自动取消订单功能关闭。
>   * 请注意，系统每隔1000ms（1s）倒计时是否结束，**使用此功能时应考虑足够的时间冗余** 。 我们不建议将倒计时时间设置得太精确或太小。  
> 


## 响应示例[​](/docs/zh-CN/derivatives/options-trading/market-maker-endpoints/Set-Auto-Cancel-All-Open-Orders-Config#响应示例 "响应示例的直接链接")
    
    
    {  
      "underlying": "ETHUSDT",  
      "countdownTime": 100000  
    }