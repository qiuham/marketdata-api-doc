---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/usds-margined-futures/account/rest-api/Get-BNB-Burn-Status
api_type: Account
updated_at: 2026-01-15T23:46:18.397584
---

# Get BNB Burn Status (USER_DATA)

## API Description[​](/docs/derivatives/usds-margined-futures/account/rest-api/Get-BNB-Burn-Status#api-description "Direct link to API Description")

Get user's BNB Fee Discount (Fee Discount On or Fee Discount Off )

## HTTP Request[​](/docs/derivatives/usds-margined-futures/account/rest-api/Get-BNB-Burn-Status#http-request "Direct link to HTTP Request")

GET `/fapi/v1/feeBurn`

## Request Weight[​](/docs/derivatives/usds-margined-futures/account/rest-api/Get-BNB-Burn-Status#request-weight "Direct link to Request Weight")

**30**

## Request Parameters[​](/docs/derivatives/usds-margined-futures/account/rest-api/Get-BNB-Burn-Status#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## Response Example[​](/docs/derivatives/usds-margined-futures/account/rest-api/Get-BNB-Burn-Status#response-example "Direct link to Response Example")
    
    
    {  
    	"feeBurn": true // "true": Fee Discount On; "false": Fee Discount Off  
    }

---

# 获取BNB抵扣开关状态(USER_DATA)

## 接口描述[​](/docs/zh-CN/derivatives/usds-margined-futures/account/rest-api/Get-BNB-Burn-Status#接口描述 "接口描述的直接链接")

查询用户 _**所有 symbol**_ 合约交易BNB抵扣开关状态(手续费抵扣开或关)

## HTTP请求[​](/docs/zh-CN/derivatives/usds-margined-futures/account/rest-api/Get-BNB-Burn-Status#http请求 "HTTP请求的直接链接")

GET `/fapi/v1/feeBurn`

## 请求权重[​](/docs/zh-CN/derivatives/usds-margined-futures/account/rest-api/Get-BNB-Burn-Status#请求权重 "请求权重的直接链接")

**30**

## 请求参数[​](/docs/zh-CN/derivatives/usds-margined-futures/account/rest-api/Get-BNB-Burn-Status#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## 响应示例[​](/docs/zh-CN/derivatives/usds-margined-futures/account/rest-api/Get-BNB-Burn-Status#响应示例 "响应示例的直接链接")
    
    
    {  
    	"feeBurn": true // "true": 手续费抵扣开; "false": 手续费抵扣关  
    }