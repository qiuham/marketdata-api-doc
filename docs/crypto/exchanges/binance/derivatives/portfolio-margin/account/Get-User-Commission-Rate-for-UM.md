---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/portfolio-margin/account/Get-User-Commission-Rate-for-UM
api_type: Account
updated_at: 2026-01-15T23:45:06.289187
---

# Get User Commission Rate for UM(USER_DATA)

## API Description[​](/docs/derivatives/portfolio-margin/account/Get-User-Commission-Rate-for-UM#api-description "Direct link to API Description")

Get User Commission Rate for UM

## HTTP Request[​](/docs/derivatives/portfolio-margin/account/Get-User-Commission-Rate-for-UM#http-request "Direct link to HTTP Request")

GET `/papi/v1/um/commissionRate`

## Request Weight[​](/docs/derivatives/portfolio-margin/account/Get-User-Commission-Rate-for-UM#request-weight "Direct link to Request Weight")

**20**

## Request Parameters[​](/docs/derivatives/portfolio-margin/account/Get-User-Commission-Rate-for-UM#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
symbol| STRING| YES|   
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## Response Example[​](/docs/derivatives/portfolio-margin/account/Get-User-Commission-Rate-for-UM#response-example "Direct link to Response Example")
    
    
    {  
        "symbol": "BTCUSDT",  
        "makerCommissionRate": "0.0002",  // 0.02%  
        "takerCommissionRate": "0.0004"   // 0.04%  
    }

---

# 查询用户UM手续费率 (USER_DATA)

## 接口描述[​](/docs/zh-CN/derivatives/portfolio-margin/account/Get-User-Commission-Rate-for-UM#接口描述 "接口描述的直接链接")

查询用户UM手续费率

## HTTP请求[​](/docs/zh-CN/derivatives/portfolio-margin/account/Get-User-Commission-Rate-for-UM#http请求 "HTTP请求的直接链接")

GET `/papi/v1/um/commissionRate`

## 请求权重[​](/docs/zh-CN/derivatives/portfolio-margin/account/Get-User-Commission-Rate-for-UM#请求权重 "请求权重的直接链接")

**20**

## 请求参数[​](/docs/zh-CN/derivatives/portfolio-margin/account/Get-User-Commission-Rate-for-UM#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
symbol| STRING| YES|   
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## 响应示例[​](/docs/zh-CN/derivatives/portfolio-margin/account/Get-User-Commission-Rate-for-UM#响应示例 "响应示例的直接链接")
    
    
    {  
        "symbol": "BTCUSDT",  
        "makerCommissionRate": "0.0002",  // 0.02%  
        "takerCommissionRate": "0.0004"   // 0.04%  
    }