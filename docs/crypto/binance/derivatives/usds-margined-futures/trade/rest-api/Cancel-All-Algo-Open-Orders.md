---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/usds-margined-futures/trade/rest-api/Cancel-All-Algo-Open-Orders
api_type: Trading
updated_at: 2026-01-15T23:47:09.987636
---

# Cancel All Algo Open Orders (TRADE)

## API Description[​](/docs/derivatives/usds-margined-futures/trade/rest-api/Cancel-All-Algo-Open-Orders#api-description "Direct link to API Description")

Cancel All Algo Open Orders

## HTTP Request[​](/docs/derivatives/usds-margined-futures/trade/rest-api/Cancel-All-Algo-Open-Orders#http-request "Direct link to HTTP Request")

DELETE `/fapi/v1/algoOpenOrders`

## Request Weight[​](/docs/derivatives/usds-margined-futures/trade/rest-api/Cancel-All-Algo-Open-Orders#request-weight "Direct link to Request Weight")

**1**

## Request Parameters[​](/docs/derivatives/usds-margined-futures/trade/rest-api/Cancel-All-Algo-Open-Orders#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
symbol| STRING| YES|   
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## Response Example[​](/docs/derivatives/usds-margined-futures/trade/rest-api/Cancel-All-Algo-Open-Orders#response-example "Direct link to Response Example")
    
    
    {  
    	"code": 200,   
    	"msg": "The operation of cancel all open order is done."  
    }

---

# 撤销全部订单(TRADE)

## 接口描述[​](/docs/zh-CN/derivatives/usds-margined-futures/trade/rest-api/Cancel-All-Algo-Open-Orders#接口描述 "接口描述的直接链接")

撤销全部订单 (TRADE)

## HTTP请求[​](/docs/zh-CN/derivatives/usds-margined-futures/trade/rest-api/Cancel-All-Algo-Open-Orders#http请求 "HTTP请求的直接链接")

DELETE `/fapi/v1/algoOpenOrders`

## 请求权重[​](/docs/zh-CN/derivatives/usds-margined-futures/trade/rest-api/Cancel-All-Algo-Open-Orders#请求权重 "请求权重的直接链接")

**1**

## 请求参数[​](/docs/zh-CN/derivatives/usds-margined-futures/trade/rest-api/Cancel-All-Algo-Open-Orders#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
symbol| STRING| YES| 交易对  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## 响应示例[​](/docs/zh-CN/derivatives/usds-margined-futures/trade/rest-api/Cancel-All-Algo-Open-Orders#响应示例 "响应示例的直接链接")
    
    
    {  
    	"code": 200,   
    	"msg": "The operation of cancel all open order is done."  
    }