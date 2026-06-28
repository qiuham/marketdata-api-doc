---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/usds-margined-futures/trade/rest-api/Modify-Isolated-Position-Margin
api_type: Trading
updated_at: 2026-01-15T23:47:22.397539
---

# Modify Isolated Position Margin(TRADE)

## API Description[​](/docs/derivatives/usds-margined-futures/trade/rest-api/Modify-Isolated-Position-Margin#api-description "Direct link to API Description")

Modify Isolated Position Margin

## HTTP Request[​](/docs/derivatives/usds-margined-futures/trade/rest-api/Modify-Isolated-Position-Margin#http-request "Direct link to HTTP Request")

POST `/fapi/v1/positionMargin`

## Request Weight[​](/docs/derivatives/usds-margined-futures/trade/rest-api/Modify-Isolated-Position-Margin#request-weight "Direct link to Request Weight")

**1**

## Request Parameters[​](/docs/derivatives/usds-margined-futures/trade/rest-api/Modify-Isolated-Position-Margin#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
symbol| STRING| YES|   
positionSide| ENUM| NO| Default `BOTH` for One-way Mode ; `LONG` or `SHORT` for Hedge Mode. It must be sent with Hedge Mode.  
amount| DECIMAL| YES|   
type| INT| YES| 1: Add position margin，2: Reduce position margin  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
>   * Only for isolated symbol
> 


## Response Example[​](/docs/derivatives/usds-margined-futures/trade/rest-api/Modify-Isolated-Position-Margin#response-example "Direct link to Response Example")
    
    
    {  
    	"amount": 100.0,  
      	"code": 200,  
      	"msg": "Successfully modify position margin.",  
      	"type": 1  
    }

---

# 调整逐仓保证金 (TRADE)

## 接口描述[​](/docs/zh-CN/derivatives/usds-margined-futures/trade/rest-api/Modify-Isolated-Position-Margin#接口描述 "接口描述的直接链接")

针对逐仓模式下的仓位，调整其逐仓保证金资金。

## HTTP请求[​](/docs/zh-CN/derivatives/usds-margined-futures/trade/rest-api/Modify-Isolated-Position-Margin#http请求 "HTTP请求的直接链接")

POST `/fapi/v1/positionMargin`

## 请求权重[​](/docs/zh-CN/derivatives/usds-margined-futures/trade/rest-api/Modify-Isolated-Position-Margin#请求权重 "请求权重的直接链接")

**1**

## 请求参数[​](/docs/zh-CN/derivatives/usds-margined-futures/trade/rest-api/Modify-Isolated-Position-Margin#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
symbol| STRING| YES| 交易对  
positionSide| ENUM| NO| 持仓方向，单向持仓模式下非必填，默认且仅可填`BOTH`;在双向持仓模式下必填,且仅可选择 `LONG` 或 `SHORT`  
amount| DECIMAL| YES| 保证金资金  
type| INT| YES| 调整方向 1: 增加逐仓保证金，2: 减少逐仓保证金  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
>   * 只针对逐仓symbol 与 positionSide(如有)
> 


## 响应示例[​](/docs/zh-CN/derivatives/usds-margined-futures/trade/rest-api/Modify-Isolated-Position-Margin#响应示例 "响应示例的直接链接")
    
    
    {  
    	"amount": 100.0,  
      	"code": 200,  
      	"msg": "Successfully modify position margin.",  
      	"type": 1  
    }