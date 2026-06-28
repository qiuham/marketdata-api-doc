---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/usds-margined-futures/trade/rest-api/Change-Initial-Leverage
api_type: Trading
updated_at: 2026-01-15T23:47:13.216622
---

# Change Initial Leverage(TRADE)

## API Description[​](/docs/derivatives/usds-margined-futures/trade/rest-api/Change-Initial-Leverage#api-description "Direct link to API Description")

Change user's initial leverage of specific symbol market.

## HTTP Request[​](/docs/derivatives/usds-margined-futures/trade/rest-api/Change-Initial-Leverage#http-request "Direct link to HTTP Request")

POST `/fapi/v1/leverage`

## Request Weight[​](/docs/derivatives/usds-margined-futures/trade/rest-api/Change-Initial-Leverage#request-weight "Direct link to Request Weight")

**1**

## Request Parameters[​](/docs/derivatives/usds-margined-futures/trade/rest-api/Change-Initial-Leverage#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
symbol| STRING| YES|   
leverage| INT| YES| target initial leverage: int from 1 to 125  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## Response Example[​](/docs/derivatives/usds-margined-futures/trade/rest-api/Change-Initial-Leverage#response-example "Direct link to Response Example")
    
    
    {  
     	"leverage": 21,  
     	"maxNotionalValue": "1000000",  
     	"symbol": "BTCUSDT"  
    }

---

# 调整开仓杠杆 (TRADE)

## 接口描述[​](/docs/zh-CN/derivatives/usds-margined-futures/trade/rest-api/Change-Initial-Leverage#接口描述 "接口描述的直接链接")

调整用户在指定symbol合约的开仓杠杆。

## HTTP请求[​](/docs/zh-CN/derivatives/usds-margined-futures/trade/rest-api/Change-Initial-Leverage#http请求 "HTTP请求的直接链接")

POST `/fapi/v1/leverage`

## 请求权重[​](/docs/zh-CN/derivatives/usds-margined-futures/trade/rest-api/Change-Initial-Leverage#请求权重 "请求权重的直接链接")

**1**

## 请求参数[​](/docs/zh-CN/derivatives/usds-margined-futures/trade/rest-api/Change-Initial-Leverage#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
symbol| STRING| YES| 交易对  
leverage| INT| YES| 目标杠杆倍数：1 到 125 整数  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## 响应示例[​](/docs/zh-CN/derivatives/usds-margined-futures/trade/rest-api/Change-Initial-Leverage#响应示例 "响应示例的直接链接")
    
    
    {  
     	"leverage": 21,	// 杠杆倍数  
     	"maxNotionalValue": "1000000", // 当前杠杆倍数下允许的最大名义价值  
     	"symbol": "BTCUSDT"	// 交易对  
    }