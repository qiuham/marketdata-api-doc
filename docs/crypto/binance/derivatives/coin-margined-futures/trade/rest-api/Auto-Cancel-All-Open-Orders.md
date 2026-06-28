---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/coin-margined-futures/trade/rest-api/Auto-Cancel-All-Open-Orders
api_type: Trading
updated_at: 2026-01-15T23:39:31.294292
---

# Auto-Cancel All Open Orders (TRADE)

## API Description[​](/docs/derivatives/coin-margined-futures/trade/rest-api/Auto-Cancel-All-Open-Orders#api-description "Direct link to API Description")

Cancel all open orders of the specified symbol at the end of the specified countdown. This rest endpoint means to ensure your open orders are canceled in case of an outage. The endpoint should be called repeatedly as heartbeats so that the existing countdown time can be canceled and repalced by a new one. The system will check all countdowns **approximately every 10 milliseconds** , so please note that sufficient redundancy should be considered when using this function. We do not recommend setting the countdown time to be too precise or too small.

  * Example usage:



> Call this endpoint at 30s intervals with an countdownTime of 120000 (120s).  
>  If this endpoint is not called within 120 seconds, all your orders of the specified symbol will be automatically canceled.  
>  If this endpoint is called with an countdownTime of 0, the countdown timer will be stopped.

## HTTP Request[​](/docs/derivatives/coin-margined-futures/trade/rest-api/Auto-Cancel-All-Open-Orders#http-request "Direct link to HTTP Request")

POST `/dapi/v1/countdownCancelAll`

## Request Weight[​](/docs/derivatives/coin-margined-futures/trade/rest-api/Auto-Cancel-All-Open-Orders#request-weight "Direct link to Request Weight")

**10**

## Request Parameters[​](/docs/derivatives/coin-margined-futures/trade/rest-api/Auto-Cancel-All-Open-Orders#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
symbol| STRING| YES|   
countdownTime| LONG| YES| countdown time, 1000 for 1 second. 0 to cancel the timer  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## Response Example[​](/docs/derivatives/coin-margined-futures/trade/rest-api/Auto-Cancel-All-Open-Orders#response-example "Direct link to Response Example")
    
    
    {  
    	"symbol": "BTCUSD_200925",   
    	"countdownTime": "100000"  
    }

---

# 倒计时撤销所有订单 (TRADE)

## 接口描述[​](/docs/zh-CN/derivatives/coin-margined-futures/trade/rest-api/Auto-Cancel-All-Open-Orders#接口描述 "接口描述的直接链接")

倒计时撤销所有订单。该接口可以被用于确保在发生故障时撤销指定symbol上的所有挂单。 在使用这个功能时,接口应像心跳一样在倒计时内被反复调用,以便可以取消既有的倒计时并开始新的倒数计时设置。系统会**大约每10毫秒** 检查一次所有倒计时情况,因此请注意,使用此功能时应考虑足够的冗余。  
我们不建议将倒记时设置得太精确或太小。

  * 用法示例：



> 以30s的间隔重复此接口,每次倒计时countdownTime设置为120000(120s)。  
>  如果在120秒内未再次调用此接口,则您指定symbol上的所有挂单都会被自动撤销。  
>  如果在120秒内以将countdownTime设置为0,则倒数计时器将终止,自动撤单功能取消。

## HTTP请求[​](/docs/zh-CN/derivatives/coin-margined-futures/trade/rest-api/Auto-Cancel-All-Open-Orders#http请求 "HTTP请求的��直接链接")

POST `/dapi/v1/countdownCancelAll`

**权重:** **10**

## 请求参数[​](/docs/zh-CN/derivatives/coin-margined-futures/trade/rest-api/Auto-Cancel-All-Open-Orders#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
symbol| STRING| YES|   
countdownTime| LONG| YES| 倒计时。 1000 表示 1 秒； 0 表示取消倒计时撤单功能。  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## 响应示例[​](/docs/zh-CN/derivatives/coin-margined-futures/trade/rest-api/Auto-Cancel-All-Open-Orders#响应示例 "响应示例的直接链接")
    
    
    {  
    	"symbol": "BTCUSD_200925",   
    	"countdownTime": "100000"  
    }