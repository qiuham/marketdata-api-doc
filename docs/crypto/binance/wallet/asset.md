---
exchange: binance
source_url: https://developers.binance.com/docs/wallet/asset
api_type: REST
updated_at: 2026-07-01 19:10:38.773125
---

# Toggle BNB Burn On Spot Trade And Margin Interest (USER_DATA)

## API Description[​](/docs/wallet/asset/Toggle-BNB-Burn-On-Spot-Trade-And-Margin-Interest#api-description "Direct link to API Description")

Toggle BNB Burn On Spot Trade And Margin Interest

## HTTP Request[​](/docs/wallet/asset/Toggle-BNB-Burn-On-Spot-Trade-And-Margin-Interest#http-request "Direct link to HTTP Request")

POST `/sapi/v1/bnbBurn`

## Request Weight[​](/docs/wallet/asset/Toggle-BNB-Burn-On-Spot-Trade-And-Margin-Interest#request-weight "Direct link to Request Weight")

**1(IP)**

## Request Parameters[​](/docs/wallet/asset/Toggle-BNB-Burn-On-Spot-Trade-And-Margin-Interest#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
spotBNBBurn| STRING| NO| "true" or "false"; Determines whether to use BNB to pay for trading fees on SPOT  
interestBNBBurn| STRING| NO| "true" or "false"; Determines whether to use BNB to pay for margin loan's interest  
recvWindow| LONG| NO| No more than 60000  
timestamp| LONG| YES|   
  
  * "spotBNBBurn" and "interestBNBBurn" should be sent at least one.



## Response Example[​](/docs/wallet/asset/Toggle-BNB-Burn-On-Spot-Trade-And-Margin-Interest#response-example "Direct link to Response Example")
    
    
    {  
        "spotBNBBurn": true,  
        "interestBNBBurn": false  
    }

---

# 现货交易和杠杆利息BNB抵扣开关(USER_DATA)

## 接口描述[​](/docs/zh-CN/wallet/asset/Toggle-BNB-Burn-On-Spot-Trade-And-Margin-Interest#接口描述 "接口描述的直接链接")

现货交易和杠杆利息BNB抵扣开关

## HTTP请求[​](/docs/zh-CN/wallet/asset/Toggle-BNB-Burn-On-Spot-Trade-And-Margin-Interest#http请求 "HTTP请求的直接链接")

POST `/sapi/v1/bnbBurn`

## 请求权重[​](/docs/zh-CN/wallet/asset/Toggle-BNB-Burn-On-Spot-Trade-And-Margin-Interest#请求权重 "请求权重的直接链接")

**1(IP)**

## 请求参数[​](/docs/zh-CN/wallet/asset/Toggle-BNB-Burn-On-Spot-Trade-And-Margin-Interest#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
spotBNBBurn| STRING| NO| "true" or "false", 是否使用BNB支付现货交易的手续费  
interestBNBBurn| STRING| NO| "true" or "false", 是否使用BNB支付杠杆贷款的利息  
recvWindow| LONG| NO| 赋值不能大于 60000  
timestamp| LONG| YES|   
  
  * "spotBNBBurn" 和 "interestBNBBurn" 二者必须传至少一个



## 响应示例[​](/docs/zh-CN/wallet/asset/Toggle-BNB-Burn-On-Spot-Trade-And-Margin-Interest#响应示例 "响应示例的直接链接")
    
    
    {  
        "spotBNBBurn": true,  
        "interestBNBBurn": false  
    }