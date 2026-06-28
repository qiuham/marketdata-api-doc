---
exchange: binance
source_url: https://developers.binance.com/docs/algo/error-code
api_type: REST
updated_at: 2026-05-27 18:58:18.314164
---

# Cancel Algo Order(TRADE)

## API Description[​](/docs/algo/future-algo/Cancel-Algo-Order#api-description "Direct link to API Description")

Cancel an active order.

## HTTP Request[​](/docs/algo/future-algo/Cancel-Algo-Order#http-request "Direct link to HTTP Request")

DELETE `/sapi/v1/algo/futures/order `

## Request Weight(IP)[​](/docs/algo/future-algo/Cancel-Algo-Order#request-weightip "Direct link to Request Weight\(IP\)")

**1**

## Request Parameters[​](/docs/algo/future-algo/Cancel-Algo-Order#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
algoId| LONG| YES| eg. 14511  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
>   * You need to enable `Futures Trading Permission` for the api key which requests this endpoint.
>   * Base URL: <https://api.binance.com>
> 


## Response Example[​](/docs/algo/future-algo/Cancel-Algo-Order#response-example "Direct link to Response Example")
    
    
    {  
        "algoId": 14511,  
        "success": true,  
        "code": 0,  
        "msg": "OK"  
    }

---

# 取消策略订单 (TRADE)

## 接口描述[​](/docs/zh-CN/algo/future-algo/Cancel-Algo-Order#接口描述 "接口描述的直接链接")

撤销订单

## HTTP请求[​](/docs/zh-CN/algo/future-algo/Cancel-Algo-Order#http请求 "HTTP请求的直接链接")

DELETE `/sapi/v1/algo/futures/order`

## 请求权重(IP)[​](/docs/zh-CN/algo/future-algo/Cancel-Algo-Order#请求权重ip "请求权重\(IP\)的直接链接")

**1**

## 请求参数[​](/docs/zh-CN/algo/future-algo/Cancel-Algo-Order#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
algoId| LONG| YES| eg. 14511  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
>   * 您的 API Key 需要开通 `允许合约交易` 权限
>   * 请使用Base URL: <https://api.binance.com>
> 


## 响应示例[​](/docs/zh-CN/algo/future-algo/Cancel-Algo-Order#响应示例 "响应示例的直接链接")
    
    
    {  
        "algoId": 14511,  //策略订单ID  
        "success": true,  
        "code": 0,  
        "msg": "OK"  
    }