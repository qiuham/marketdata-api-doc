---
exchange: binance
source_url: https://developers.binance.com/docs/wallet/account/account-api-trading-status
api_type: Account
updated_at: 2026-05-27 18:58:45.911996
---

# Account API Trading Status (USER_DATA)

## API Description[​](/docs/wallet/account/account-api-trading-status#api-description "Direct link to API Description")

Fetch account api trading status detail.

## HTTP Request[​](/docs/wallet/account/account-api-trading-status#http-request "Direct link to HTTP Request")

GET `/sapi/v1/account/apiTradingStatus`

## Request Weight(IP)[​](/docs/wallet/account/account-api-trading-status#request-weightip "Direct link to Request Weight\(IP\)")

**1**

## Request Parameters[​](/docs/wallet/account/account-api-trading-status#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## Response Example[​](/docs/wallet/account/account-api-trading-status#response-example "Direct link to Response Example")
    
    
    {  
        "data": {  
            // API trading status detail  
            "isLocked": false,              // API trading function is locked or not  
            "plannedRecoverTime": 0,        // If API trading function is locked, this is the planned recover time  
            "triggerCondition": {  
                "GCR": 150,                 // Number of GTC orders  
                "IFER": 150,                // Number of FOK/IOC orders  
                "UFR": 300                  // Number of orders  
            },  
            "updateTime": 1547630471725  
        }  
    }

---

# 账户API交易状态(USER_DATA)

## 接口描述[​](/docs/zh-CN/wallet/account/account-api-trading-status#接口描述 "接口描述的直接链接")

获取 api 账户交易状态详情。

## HTTP请求[​](/docs/zh-CN/wallet/account/account-api-trading-status#http请求 "HTTP请求的直接链接")

GET `/sapi/v1/account/apiTradingStatus`

## 请求权重(IP)[​](/docs/zh-CN/wallet/account/account-api-trading-status#请求权重ip "请求权重\(IP\)的直接链接")

**1**

## 请求参数[​](/docs/zh-CN/wallet/account/account-api-trading-status#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## 响应示例[​](/docs/zh-CN/wallet/account/account-api-trading-status#响应示例 "响应示例的直接链接")
    
    
    {  
        "data": {  
            // 账户API交易状态详情  
            "isLocked": false,              // API交易功能是否被锁  
            "plannedRecoverTime": 0,        // API交易功能被锁情况下的预计恢复时间  
            "triggerCondition": {  
                "GCR": 150,                 // Number of GTC orders  
                "IFER": 150,                // Number of FOK/IOC orders  
                "UFR": 300                  // Number of orders  
            },  
            "updateTime": 1547630471725  
        }  
    }