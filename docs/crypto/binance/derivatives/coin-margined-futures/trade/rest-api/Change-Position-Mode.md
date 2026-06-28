---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/coin-margined-futures/trade/rest-api/Change-Position-Mode
api_type: Trading
updated_at: 2026-01-15T23:39:38.566841
---

# Change Position Mode(TRADE)

## API Description[​](/docs/derivatives/coin-margined-futures/trade/rest-api/Change-Position-Mode#api-description "Direct link to API Description")

Change user's position mode (Hedge Mode or One-way Mode ) on _**EVERY symbol**_

## HTTP Request[​](/docs/derivatives/coin-margined-futures/trade/rest-api/Change-Position-Mode#http-request "Direct link to HTTP Request")

POST `/dapi/v1/positionSide/dual`

## Request Weight[​](/docs/derivatives/coin-margined-futures/trade/rest-api/Change-Position-Mode#request-weight "Direct link to Request Weight")

**1**

## Request Parameters[​](/docs/derivatives/coin-margined-futures/trade/rest-api/Change-Position-Mode#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
dualSidePosition| STRING| YES| "true": Hedge Mode; "false": One-way Mode  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## Response Example[​](/docs/derivatives/coin-margined-futures/trade/rest-api/Change-Position-Mode#response-example "Direct link to Response Example")
    
    
    {  
    	"code": 200,  
    	"msg": "success"  
    }

---

# 更改持仓模式(TRADE)

## 接口描述[​](/docs/zh-CN/derivatives/coin-margined-futures/trade/rest-api/Change-Position-Mode#接口描述 "接口描述的直接链接")

变换用户在 _**所有symbol**_ 合约上的持仓模式：双向持仓或单向持仓。

## HTTP请求[​](/docs/zh-CN/derivatives/coin-margined-futures/trade/rest-api/Change-Position-Mode#http请求 "HTTP请求的直接链接")

POST `/dapi/v1/positionSide/dual`

## 请求权重[​](/docs/zh-CN/derivatives/coin-margined-futures/trade/rest-api/Change-Position-Mode#请求权重 "请求权重的直接链接")

**1**

## 请求参数[​](/docs/zh-CN/derivatives/coin-margined-futures/trade/rest-api/Change-Position-Mode#��请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
dualSidePosition| STRING| YES| "true": 双向持仓模式；"false": 单向持仓模式  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## 响应示例[​](/docs/zh-CN/derivatives/coin-margined-futures/trade/rest-api/Change-Position-Mode#响应示例 "响应示例的直接链接")
    
    
    {  
    	"code": 200,  
    	"msg": "success"  
    }