---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/portfolio-margin/account/Change-UM-Initial-Leverage
api_type: Account
updated_at: 2026-01-15T23:44:39.958783
---

# Change UM Initial Leverage(TRADE)

## API Description[​](/docs/derivatives/portfolio-margin/account/Change-UM-Initial-Leverage#api-description "Direct link to API Description")

Change user's initial leverage of specific symbol in UM.

## HTTP Request[​](/docs/derivatives/portfolio-margin/account/Change-UM-Initial-Leverage#http-request "Direct link to HTTP Request")

POST `/papi/v1/um/leverage`

## Request Weight[​](/docs/derivatives/portfolio-margin/account/Change-UM-Initial-Leverage#request-weight "Direct link to Request Weight")

**1**

## Request Parameters[​](/docs/derivatives/portfolio-margin/account/Change-UM-Initial-Leverage#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
symbol| STRING| YES|   
leverage| INT| YES| target initial leverage: int from 1 to 125  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## Response Example[​](/docs/derivatives/portfolio-margin/account/Change-UM-Initial-Leverage#response-example "Direct link to Response Example")
    
    
    {  
        "leverage": 21,  
        "maxNotionalValue": "1000000",  
        "symbol": "BTCUSDT"  
    }

---

# 调整UM开仓杠杆(TRADE)

## 接口描述[​](/docs/zh-CN/derivatives/portfolio-margin/account/Change-UM-Initial-Leverage#接口描述 "接口描述的直接链接")

调整用户在指定UM symbol合约的开仓杠杆。不同持仓方向上使用相同杠杆倍数，共享允许的最大交易标的资产数量

## HTTP请求[​](/docs/zh-CN/derivatives/portfolio-margin/account/Change-UM-Initial-Leverage#http请求 "HTTP请求的直接链接")

`POST /papi/v1/um/leverage`

## 请求权重[​](/docs/zh-CN/derivatives/portfolio-margin/account/Change-UM-Initial-Leverage#请求权重 "请求权重的直接链接")

**1**

## 请求参数[​](/docs/zh-CN/derivatives/portfolio-margin/account/Change-UM-Initial-Leverage#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
symbol| STRING| YES|   
leverage| INT| YES| target initial leverage: int from 1 to 125  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## 响应示例[​](/docs/zh-CN/derivatives/portfolio-margin/account/Change-UM-Initial-Leverage#响应示例 "响应示例的直接链接")
    
    
    {  
        "leverage": 21,  
        "maxNotionalValue": "1000000",  
        "symbol": "BTCUSDT"  
    }