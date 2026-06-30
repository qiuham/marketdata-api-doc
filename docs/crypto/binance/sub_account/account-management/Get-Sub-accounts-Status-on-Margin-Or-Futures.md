---
exchange: binance
source_url: https://developers.binance.com/docs/sub_account/account-management/Get-Sub-accounts-Status-on-Margin-Or-Futures
api_type: Account
updated_at: 2026-06-30 19:11:47.404270
---

# Get IP Restriction for a Sub-account API Key (For Master Account) (USER_DATA)

## API Description[​](/docs/sub_account/api-management#api-description "Direct link to API Description")

Get IP Restriction for a Sub-account API Key

## HTTP Request[​](/docs/sub_account/api-management#http-request "Direct link to HTTP Request")

GET `/sapi/v1/sub-account/subAccountApi/ipRestriction`

## Request Weight(UID)[​](/docs/sub_account/api-management#request-weightuid "Direct link to Request Weight\(UID\)")

**3000**

## Request Parameters[​](/docs/sub_account/api-management#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
email| STRING| YES| [Sub-account email](/docs/sub_account/api-management#email-address)  
subAccountApiKey| STRING| YES|   
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## Response Example[​](/docs/sub_account/api-management#response-example "Direct link to Response Example")
    
    
    {  
        "ipRestrict": "true",  
        "ipList": [  
            "69.210.67.14",  
            "8.34.21.10"  
        ],  
        "updateTime": 1636371437000,  
        "apiKey": "k5V49ldtn4tszj6W3hystegdfvmGbqDzjmkCtpTvC0G74WhK7yd4rfCTo4lShf"  
    }

---

# 查询子账户API Key IP白名单 (适用母账户) (USER_DATA)

## 接口描述[​](/docs/zh-CN/sub_account/api-management#接口描述 "接口描述的直接链接")

查询子账户API Key IP白名单

## HTTP请求[​](/docs/zh-CN/sub_account/api-management#http请求 "HTTP请求的直接链接")

GET `/sapi/v1/sub-account/subAccountApi/ipRestriction`

## 请求权重(UID)[​](/docs/zh-CN/sub_account/api-management#请求权重uid "请求权重\(UID\)的直接链接")

**3000**

## 请求参数[​](/docs/zh-CN/sub_account/api-management#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
email| STRING| YES| [Sub-account email](/docs/zh-CN/sub_account/api-management#email-address)  
subAccountApiKey| STRING| YES|   
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## 响应示例[​](/docs/zh-CN/sub_account/api-management#响应示例 "响应示例的直接链接")
    
    
    {  
        "ipRestrict": "true",  
        "ipList": [  
            "69.210.67.14",  
            "8.34.21.10"  
        ],  
        "updateTime": 1636371437000,  
        "apiKey": "k5V49ldtn4tszj6W3hystegdfvmGbqDzjmkCtpTvC0G74WhK7yd4rfCTo4lShf"  
    }