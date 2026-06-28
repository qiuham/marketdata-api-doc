---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/usds-margined-futures/account/rest-api/Get-Download-Id-For-Futures-Order-History
api_type: Account
updated_at: 2026-01-15T23:46:18.730921
---

# Get Download Id For Futures Order History (USER_DATA)

## API Description[​](/docs/derivatives/usds-margined-futures/account/rest-api/Get-Download-Id-For-Futures-Order-History#api-description "Direct link to API Description")

Get Download Id For Futures Order History

## HTTP Request[​](/docs/derivatives/usds-margined-futures/account/rest-api/Get-Download-Id-For-Futures-Order-History#http-request "Direct link to HTTP Request")

GET `/fapi/v1/order/asyn`

## Request Weight[​](/docs/derivatives/usds-margined-futures/account/rest-api/Get-Download-Id-For-Futures-Order-History#request-weight "Direct link to Request Weight")

**1000**

## Request Parameters[​](/docs/derivatives/usds-margined-futures/account/rest-api/Get-Download-Id-For-Futures-Order-History#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
startTime| LONG| YES| Timestamp in ms  
endTime| LONG| YES| Timestamp in ms  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
>   * Request Limitation is 10 times per month, shared by front end download page and rest api
>   * The time between `startTime` and `endTime` can not be longer than 1 year
> 


## Response Example[​](/docs/derivatives/usds-margined-futures/account/rest-api/Get-Download-Id-For-Futures-Order-History#response-example "Direct link to Response Example")
    
    
    {  
    	"avgCostTimestampOfLast30d":7241837, // Average time taken for data download in the past 30 days  
      	"downloadId":"546975389218332672",  
    }

---

# 获取合约订单历史下载Id (USER_DATA)

## 接口描述[​](/docs/zh-CN/derivatives/usds-margined-futures/account/rest-api/Get-Download-Id-For-Futures-Order-History#接口描述 "接口描述的直接链接")

获取合约订单历史下载Id

## HTTP请求[​](/docs/zh-CN/derivatives/usds-margined-futures/account/rest-api/Get-Download-Id-For-Futures-Order-History#http请求 "HTTP请求的直接链接")

GET `/fapi/v1/order/asyn`

## 请求权重[​](/docs/zh-CN/derivatives/usds-margined-futures/account/rest-api/Get-Download-Id-For-Futures-Order-History#请求权重 "请求权重的直接链接")

**1000**

## 请求参数[​](/docs/zh-CN/derivatives/usds-margined-futures/account/rest-api/Get-Download-Id-For-Futures-Order-History#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
startTime| LONG| YES| 起始时间，ms格式时间戳  
endTime| LONG| YES| 结束时间，ms格式时间戳  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
>   * 存在每月10次的请求限制，网页端和Rest接口下载次数共用。
>   * `startTime`与`endTime`间隔不能超过1年
> 


## 响应示例[​](/docs/zh-CN/derivatives/usds-margined-futures/account/rest-api/Get-Download-Id-For-Futures-Order-History#响应示例 "响应示例的直接链接")
    
    
    {  
    	"avgCostTimestampOfLast30d":7241837, //过去30天平均数据下载时间  
      	"downloadId":"546975389218332672",   //下载Id  
    }