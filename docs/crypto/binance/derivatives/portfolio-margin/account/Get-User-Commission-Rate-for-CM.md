---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/portfolio-margin/account/Get-User-Commission-Rate-for-CM
api_type: Account
updated_at: 2026-01-15T23:45:03.221673
---

# Get User Commission Rate for CM(USER_DATA)

## API Description[​](/docs/derivatives/portfolio-margin/account/Get-User-Commission-Rate-for-CM#api-description "Direct link to API Description")

Get User Commission Rate for CM

## HTTP Request[​](/docs/derivatives/portfolio-margin/account/Get-User-Commission-Rate-for-CM#http-request "Direct link to HTTP Request")

GET `/papi/v1/cm/commissionRate`

## Request Weight[​](/docs/derivatives/portfolio-margin/account/Get-User-Commission-Rate-for-CM#request-weight "Direct link to Request Weight")

**20**

## Request Parameters[​](/docs/derivatives/portfolio-margin/account/Get-User-Commission-Rate-for-CM#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
symbol| STRING| YES|   
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## Response Example[​](/docs/derivatives/portfolio-margin/account/Get-User-Commission-Rate-for-CM#response-example "Direct link to Response Example")
    
    
    {  
        "symbol": "BTCUSD_PERP",  
        "makerCommissionRate": "0.00015",  // 0.015%  
        "takerCommissionRate": "0.00040"   // 0.040%  
    }

---

# 查询用户CM手续费率(USER_DATA)

## 接口描述[​](/docs/zh-CN/derivatives/portfolio-margin/account/Get-User-Commission-Rate-for-CM#接口描述 "接口描述的直接链接")

查询用户CM手续费率

## HTTP请求[​](/docs/zh-CN/derivatives/portfolio-margin/account/Get-User-Commission-Rate-for-CM#http请求 "HTTP请求的直接链接")

GET /`papi/v1/cm/commissionRate`

## 请求权重[​](/docs/zh-CN/derivatives/portfolio-margin/account/Get-User-Commission-Rate-for-CM#请求权重 "请求权重的直接链接")

**20**

## 请求参数[​](/docs/zh-CN/derivatives/portfolio-margin/account/Get-User-Commission-Rate-for-CM#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
symbol| STRING| YES|   
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## 响应示例[​](/docs/zh-CN/derivatives/portfolio-margin/account/Get-User-Commission-Rate-for-CM#响应示例 "响应示例的直接链接")
    
    
    {  
        "symbol": "BTCUSD_PERP",  
        "makerCommissionRate": "0.00015",  // 0.015%  
        "takerCommissionRate": "0.00040"   // 0.040%  
    }