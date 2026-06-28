---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/portfolio-margin/account/Get-UM-Current-Position-Mode
api_type: Account
updated_at: 2026-01-15T23:44:58.671259
---

# Get UM Current Position Mode(USER_DATA)

## API Description[​](/docs/derivatives/portfolio-margin/account/Get-UM-Current-Position-Mode#api-description "Direct link to API Description")

Get user's position mode (Hedge Mode or One-way Mode ) on EVERY symbol in UM

## HTTP Request[​](/docs/derivatives/portfolio-margin/account/Get-UM-Current-Position-Mode#http-request "Direct link to HTTP Request")

GET `/papi/v1/um/positionSide/dual`

## Request Weight[​](/docs/derivatives/portfolio-margin/account/Get-UM-Current-Position-Mode#request-weight "Direct link to Request Weight")

**30**

## Request Parameters[​](/docs/derivatives/portfolio-margin/account/Get-UM-Current-Position-Mode#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## Response Example[​](/docs/derivatives/portfolio-margin/account/Get-UM-Current-Position-Mode#response-example "Direct link to Response Example")
    
    
    {  
        "dualSidePosition": true // "true": Hedge Mode; "false": One-way Mode  
    }

---

# 查询UM持仓模式(USER_DATA)

## 接口描述[​](/docs/zh-CN/derivatives/portfolio-margin/account/Get-UM-Current-Position-Mode#接口描述 "接口描述的直接链接")

查询用户目前在UM所有symbol合约上的持仓模式: 双向持仓或单向持仓。

## HTTP请求[​](/docs/zh-CN/derivatives/portfolio-margin/account/Get-UM-Current-Position-Mode#http请求 "HTTP请求的直接链接")

GET `/papi/v1/um/positionSide/dual`

## 请求权重[​](/docs/zh-CN/derivatives/portfolio-margin/account/Get-UM-Current-Position-Mode#请求权重 "请求权重的直接链接")

**30**

## 请求参数[​](/docs/zh-CN/derivatives/portfolio-margin/account/Get-UM-Current-Position-Mode#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## 响应示例[​](/docs/zh-CN/derivatives/portfolio-margin/account/Get-UM-Current-Position-Mode#响应示例 "响应示例的直接链接")
    
    
    {  
        "dualSidePosition": true // "true": 双向持仓模式；"false": 单向持仓模式  
    }