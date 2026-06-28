---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/usds-margined-futures/trade/rest-api/Cancel-Algo-Order
api_type: Trading
updated_at: 2026-01-15T23:47:09.927054
---

# Cancel Algo Order (TRADE)

## API Description[​](/docs/derivatives/usds-margined-futures/trade/rest-api/Cancel-Algo-Order#api-description "Direct link to API Description")

Cancel an active algo order.

## HTTP Request[​](/docs/derivatives/usds-margined-futures/trade/rest-api/Cancel-Algo-Order#http-request "Direct link to HTTP Request")

DELETE `/fapi/v1/algoOrder`

## Request Weight[​](/docs/derivatives/usds-margined-futures/trade/rest-api/Cancel-Algo-Order#request-weight "Direct link to Request Weight")

**1**

## Request Parameters[​](/docs/derivatives/usds-margined-futures/trade/rest-api/Cancel-Algo-Order#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
algoId| LONG| NO|   
clientAlgoId| STRING| NO|   
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
>   * Either `algoId` or `clientAlgoId` must be sent.
> 


## Response Example[​](/docs/derivatives/usds-margined-futures/trade/rest-api/Cancel-Algo-Order#response-example "Direct link to Response Example")
    
    
    {  
       "algoId": 2146760,  
       "clientAlgoId": "6B2I9XVcJpCjqPAJ4YoFX7",  
       "code": "200",  
       "msg": "success"  
    }

---

# 撤销条件订单 (TRADE)

## 接口描述[​](/docs/zh-CN/derivatives/usds-margined-futures/trade/rest-api/Cancel-Algo-Order#接口描述 "接口描述的直接链接")

撤销条件订单

## HTTP请求[​](/docs/zh-CN/derivatives/usds-margined-futures/trade/rest-api/Cancel-Algo-Order#http请求 "HTTP请求的直接链接")

DELETE `/fapi/v1/algoOrder`

## 请求权重[​](/docs/zh-CN/derivatives/usds-margined-futures/trade/rest-api/Cancel-Algo-Order#请求权重 "请求权重的直接链接")

**1**

## 请求参数[​](/docs/zh-CN/derivatives/usds-margined-futures/trade/rest-api/Cancel-Algo-Order#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
algoId| LONG| NO| 系统订单号  
clientAlgoId| STRING| NO| 用户自定义的订单号  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
>   * `algoId` 与 `clientAlgoId` 必须至少发送一个
> 


## 响应示例[​](/docs/zh-CN/derivatives/usds-margined-futures/trade/rest-api/Cancel-Algo-Order#响应示例 "响应示例的直接链接")
    
    
    {  
       "algoId": 2146760,  
       "clientAlgoId": "6B2I9XVcJpCjqPAJ4YoFX7",  
       "code": "200",  
       "msg": "success"  
    }