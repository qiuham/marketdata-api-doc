---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/usds-margined-futures/account/rest-api/Get-Current-Multi-Assets-Mode
api_type: Account
updated_at: 2026-01-15T23:46:18.483716
---

# Get Current Multi-Assets Mode (USER_DATA)

## API Description[​](/docs/derivatives/usds-margined-futures/account/rest-api/Get-Current-Multi-Assets-Mode#api-description "Direct link to API Description")

Get user's Multi-Assets mode (Multi-Assets Mode or Single-Asset Mode) on _**Every symbol**_

## HTTP Request[​](/docs/derivatives/usds-margined-futures/account/rest-api/Get-Current-Multi-Assets-Mode#http-request "Direct link to HTTP Request")

GET `/fapi/v1/multiAssetsMargin`

## Request Weight[​](/docs/derivatives/usds-margined-futures/account/rest-api/Get-Current-Multi-Assets-Mode#request-weight "Direct link to Request Weight")

**30**

## Request Parameters[​](/docs/derivatives/usds-margined-futures/account/rest-api/Get-Current-Multi-Assets-Mode#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## Response Example[​](/docs/derivatives/usds-margined-futures/account/rest-api/Get-Current-Multi-Assets-Mode#response-example "Direct link to Response Example")
    
    
    {  
    	"multiAssetsMargin": true // "true": Multi-Assets Mode; "false": Single-Asset Mode  
    }

---

# 查询联合保证金模式(USER_DATA)

## 接口描述[​](/docs/zh-CN/derivatives/usds-margined-futures/account/rest-api/Get-Current-Multi-Assets-Mode#接口描述 "接口描述的直接链接")

查询用户目前在 _**所有symbol**_ 合约上的联合保证金模式。

## HTTP请求[​](/docs/zh-CN/derivatives/usds-margined-futures/account/rest-api/Get-Current-Multi-Assets-Mode#http请求 "HTTP请求的直接链接")

GET `/fapi/v1/multiAssetsMargin`

## 请求权重[​](/docs/zh-CN/derivatives/usds-margined-futures/account/rest-api/Get-Current-Multi-Assets-Mode#请求权重 "请求权重的直接链接")

30

## 请求参数[​](/docs/zh-CN/derivatives/usds-margined-futures/account/rest-api/Get-Current-Multi-Assets-Mode#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## 响应示例[​](/docs/zh-CN/derivatives/usds-margined-futures/account/rest-api/Get-Current-Multi-Assets-Mode#响应示例 "响应示例的直接链接")
    
    
    {  
    	"multiAssetsMargin": true // "true": 联合保证金模式开启；"false": 联合保证金模式关闭  
    }