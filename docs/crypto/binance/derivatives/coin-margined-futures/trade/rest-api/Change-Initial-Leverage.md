---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/coin-margined-futures/trade/rest-api/Change-Initial-Leverage
api_type: Trading
updated_at: 2026-01-15T23:39:38.424015
---

# Change Initial Leverage (TRADE)

## API Description[​](/docs/derivatives/coin-margined-futures/trade/rest-api/Change-Initial-Leverage#api-description "Direct link to API Description")

Change user's initial leverage in the specific symbol market.  
For Hedge Mode, LONG and SHORT positions of one symbol use the same initial leverage and share a total notional value.

## HTTP Request[​](/docs/derivatives/coin-margined-futures/trade/rest-api/Change-Initial-Leverage#http-request "Direct link to HTTP Request")

POST `/dapi/v1/leverage`

## Request Weight[​](/docs/derivatives/coin-margined-futures/trade/rest-api/Change-Initial-Leverage#request-weight "Direct link to Request Weight")

**1**

## Request Parameters[​](/docs/derivatives/coin-margined-futures/trade/rest-api/Change-Initial-Leverage#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
symbol| STRING| YES|   
leverage| INT| YES| target initial leverage: int from 1 to 125  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## Response Example[​](/docs/derivatives/coin-margined-futures/trade/rest-api/Change-Initial-Leverage#response-example "Direct link to Response Example")
    
    
    {  
     	"leverage": 21,  
     	"maxQty": "1000",  // maximum quantity of base asset  
     	"symbol": "BTCUSD_200925"  
    }

---

# 调整开仓杠杆(TRADE)

## 接口描述[​](/docs/zh-CN/derivatives/coin-margined-futures/trade/rest-api/Change-Initial-Leverage#接口描述 "接口描述的直接链接")

调整用户在指定symbol合约的开仓杠杆。不同持仓方向上使用相同杠杆倍数,共享允许的最大交易标的资产数量。

## HTTP请求[​](/docs/zh-CN/derivatives/coin-margined-futures/trade/rest-api/Change-Initial-Leverage#http请求 "HTTP请求的直接链接")

POST `/dapi/v1/leverage`

## 请求权重[​](/docs/zh-CN/derivatives/coin-margined-futures/trade/rest-api/Change-Initial-Leverage#请求权重 "请求权重的直接链接")

**1**

## 请求参数[​](/docs/zh-CN/derivatives/coin-margined-futures/trade/rest-api/Change-Initial-Leverage#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
symbol| STRING| YES| 交易对  
leverage| INT| YES| 目标杠杆倍数  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## 响应示例[​](/docs/zh-CN/derivatives/coin-margined-futures/trade/rest-api/Change-Initial-Leverage#响应示例 "响应示例的直接链接")
    
    
    {  
     	"leverage": 21,	// 杠杆倍数  
     	"maxQty": "1000", // 当前杠杆倍数下允许的最大base asset数量  
     	"symbol": "BTCUSD_200925"	// 交易对  
    }