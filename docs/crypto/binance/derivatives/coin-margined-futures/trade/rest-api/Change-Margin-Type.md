---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/coin-margined-futures/trade/rest-api/Change-Margin-Type
api_type: Trading
updated_at: 2026-01-15T23:39:38.489665
---

# Change Margin Type (TRADE)

## API Description[​](/docs/derivatives/coin-margined-futures/trade/rest-api/Change-Margin-Type#api-description "Direct link to API Description")

Change user's margin type in the specific symbol market.For Hedge Mode, LONG and SHORT positions of one symbol use the same margin type.  
With ISOLATED margin type, margins of the LONG and SHORT positions are isolated from each other.

## HTTP Request[​](/docs/derivatives/coin-margined-futures/trade/rest-api/Change-Margin-Type#http-request "Direct link to HTTP Request")

POST `/dapi/v1/marginType`

## Request Weight[​](/docs/derivatives/coin-margined-futures/trade/rest-api/Change-Margin-Type#request-weight "Direct link to Request Weight")

**1**

## Request Parameters[​](/docs/derivatives/coin-margined-futures/trade/rest-api/Change-Margin-Type#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
symbol| STRING| YES|   
marginType| ENUM| YES| ISOLATED, CROSSED  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## Response Example[​](/docs/derivatives/coin-margined-futures/trade/rest-api/Change-Margin-Type#response-example "Direct link to Response Example")
    
    
    {  
    	"code": 200,  
    	"msg": "success"  
    }

---

# 变换逐全仓模式 (TRADE)

## 接口描述[​](/docs/zh-CN/derivatives/coin-margined-futures/trade/rest-api/Change-Margin-Type#接口描述 "接口描述的直接链接")

变换用户在指定 symbol 合约上的保证金模式：逐仓或全仓。  
不同持仓方向上使用相同的保证金模式。双向持仓模式下的逐仓,`LONG` 与 `SHORT`使用独立的逐仓仓位。

## HTTP请求[​](/docs/zh-CN/derivatives/coin-margined-futures/trade/rest-api/Change-Margin-Type#http请求 "HTTP请求的直接链接")

POST `/dapi/v1/marginType`

## 请求权重[​](/docs/zh-CN/derivatives/coin-margined-futures/trade/rest-api/Change-Margin-Type#请求权重 "请求权重的直接链接")

**1**

## 请求参数[​](/docs/zh-CN/derivatives/coin-margined-futures/trade/rest-api/Change-Margin-Type#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
symbol| STRING| YES| 交易对  
marginType| ENUM| YES| 保证金模式 ISOLATED(逐仓), CROSSED(全仓)  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## 响应示例[​](/docs/zh-CN/derivatives/coin-margined-futures/trade/rest-api/Change-Margin-Type#响应示例 "响应示例的直接链接")
    
    
    {  
    	"code": 200,  
    	"msg": "success"  
    }