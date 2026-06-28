---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/portfolio-margin-pro/account/Fund-Collection-by-Asset
api_type: Account
updated_at: 2026-01-15T23:44:05.145796
---

# Fund Collection by Asset(USER_DATA)

## API Description[​](/docs/derivatives/portfolio-margin-pro/account/Fund-Collection-by-Asset#api-description "Direct link to API Description")

Transfers specific asset from Futures Account to Margin account

## HTTP Request[​](/docs/derivatives/portfolio-margin-pro/account/Fund-Collection-by-Asset#http-request "Direct link to HTTP Request")

POST `/sapi/v1/portfolio/asset-collection`

## Request Weight(IP)[​](/docs/derivatives/portfolio-margin-pro/account/Fund-Collection-by-Asset#request-weightip "Direct link to Request Weight\(IP\)")

**60**

## Request Parameters[​](/docs/derivatives/portfolio-margin-pro/account/Fund-Collection-by-Asset#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
asset| STRING| YES|   
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
>   * The BNB transfer is not be supported
> 


## Response Example[​](/docs/derivatives/portfolio-margin-pro/account/Fund-Collection-by-Asset#response-example "Direct link to Response Example")
    
    
    {  
        "msg": "success"  
    }

---

# 特定资产资金归集(USER_DATA)

## 接口描述[​](/docs/zh-CN/derivatives/portfolio-margin-pro/account/Fund-Collection-by-Asset#接口描述 "接口描述的直接链接")

特定资产账户资金归集，从合约账户划转到杠杆账户

## HTTP请求[​](/docs/zh-CN/derivatives/portfolio-margin-pro/account/Fund-Collection-by-Asset#http请求 "HTTP请求的直接链接")

POST `/sapi/v1/portfolio/asset-collection`

## 请求权重(IP)[​](/docs/zh-CN/derivatives/portfolio-margin-pro/account/Fund-Collection-by-Asset#请求权重ip "请求权重\(IP\)的直接链接")

**60**

## 请求参数[​](/docs/zh-CN/derivatives/portfolio-margin-pro/account/Fund-Collection-by-Asset#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
asset| STRING| YES|   
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
>   * 本接口不支持划转BNB资产
> 


## 响应示例[​](/docs/zh-CN/derivatives/portfolio-margin-pro/account/Fund-Collection-by-Asset#响应示例 "响应示例的直接链接")
    
    
    {  
        "msg": "success"  
    }