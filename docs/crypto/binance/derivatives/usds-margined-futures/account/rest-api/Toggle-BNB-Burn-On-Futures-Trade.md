---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/usds-margined-futures/account/rest-api/Toggle-BNB-Burn-On-Futures-Trade
api_type: Trading
updated_at: 2026-01-15T23:46:33.012333
---

# Toggle BNB Burn On Futures Trade (TRADE)

## API Description[​](/docs/derivatives/usds-margined-futures/account/rest-api/Toggle-BNB-Burn-On-Futures-Trade#api-description "Direct link to API Description")

Change user's BNB Fee Discount (Fee Discount On or Fee Discount Off ) on _**EVERY symbol**_

## HTTP Request[​](/docs/derivatives/usds-margined-futures/account/rest-api/Toggle-BNB-Burn-On-Futures-Trade#http-request "Direct link to HTTP Request")

POST `/fapi/v1/feeBurn`

## Request Weight[​](/docs/derivatives/usds-margined-futures/account/rest-api/Toggle-BNB-Burn-On-Futures-Trade#request-weight "Direct link to Request Weight")

**1**

## Request Parameters[​](/docs/derivatives/usds-margined-futures/account/rest-api/Toggle-BNB-Burn-On-Futures-Trade#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
feeBurn| STRING| YES| "true": Fee Discount On; "false": Fee Discount Off  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## Response Example[​](/docs/derivatives/usds-margined-futures/account/rest-api/Toggle-BNB-Burn-On-Futures-Trade#response-example "Direct link to Response Example")
    
    
    {  
    	"code": 200,  
    	"msg": "success"  
    }

---

# 合约交易BNB抵扣开关(TRADE)

## 接口描述[​](/docs/zh-CN/derivatives/usds-margined-futures/account/rest-api/Toggle-BNB-Burn-On-Futures-Trade#接口描述 "接口描述的直接链接")

改变用户 _**所有 symbol**_ 合约交易BNB抵扣开关(手续费抵扣开或关)

## HTTP请求[​](/docs/zh-CN/derivatives/usds-margined-futures/account/rest-api/Toggle-BNB-Burn-On-Futures-Trade#http请求 "HTTP请求的直接链接")

POST `/fapi/v1/feeBurn`

## 请求权重[​](/docs/zh-CN/derivatives/usds-margined-futures/account/rest-api/Toggle-BNB-Burn-On-Futures-Trade#请求权重 "请求权重的直接链接")

**1**

## 请求参数[​](/docs/zh-CN/derivatives/usds-margined-futures/account/rest-api/Toggle-BNB-Burn-On-Futures-Trade#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
feeBurn| STRING| YES| "true": 手续费抵扣开; "false": 手续费抵扣关  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## 响应示例[​](/docs/zh-CN/derivatives/usds-margined-futures/account/rest-api/Toggle-BNB-Burn-On-Futures-Trade#响应示例 "�响应示例的直接链接")
    
    
    {  
    	"code": 200,  
    	"msg": "success"  
    }