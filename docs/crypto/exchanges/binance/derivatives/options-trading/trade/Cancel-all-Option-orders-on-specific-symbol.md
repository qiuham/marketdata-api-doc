---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/options-trading/trade/Cancel-all-Option-orders-on-specific-symbol
api_type: Trading
updated_at: 2026-01-15T23:42:46.245750
---

# Cancel all Option orders on specific symbol (TRADE)

## API Description[​](/docs/derivatives/options-trading/trade/Cancel-all-Option-orders-on-specific-symbol#api-description "Direct link to API Description")

Cancel all active order on a symbol.

## HTTP Request[​](/docs/derivatives/options-trading/trade/Cancel-all-Option-orders-on-specific-symbol#http-request "Direct link to HTTP Request")

DELETE `/eapi/v1/allOpenOrders`

## Request Weight[​](/docs/derivatives/options-trading/trade/Cancel-all-Option-orders-on-specific-symbol#request-weight "Direct link to Request Weight")

**5**

## Request Parameters[​](/docs/derivatives/options-trading/trade/Cancel-all-Option-orders-on-specific-symbol#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
symbol| STRING| YES| Option trading pair, e.g BTC-200730-9000-C  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## Response Example[​](/docs/derivatives/options-trading/trade/Cancel-all-Option-orders-on-specific-symbol#response-example "Direct link to Response Example")
    
    
    {  
      "code": 0,  
      "msg": "success"  
    }

---

# 撤销单交易对全部订单 (TRADE)

## 接口描述[​](/docs/zh-CN/derivatives/options-trading/trade/Cancel-all-Option-orders-on-specific-symbol#接口描述 "接口描述的直接链接")

撤销单交易对全部订单

## HTTP请求[​](/docs/zh-CN/derivatives/options-trading/trade/Cancel-all-Option-orders-on-specific-symbol#http请求 "HTTP请求的直接链接")

DELETE `/eapi/v1/allOpenOrders`

## 请求权重[​](/docs/zh-CN/derivatives/options-trading/trade/Cancel-all-Option-orders-on-specific-symbol#请求权重 "请求权重的直接链接")

**5**

## 请求参数[​](/docs/zh-CN/derivatives/options-trading/trade/Cancel-all-Option-orders-on-specific-symbol#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
symbol| STRING| YES| 交易对  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## 响应示例[​](/docs/zh-CN/derivatives/options-trading/trade/Cancel-all-Option-orders-on-specific-symbol#响应示例 "响应示例的直接链接")
    
    
    {  
      "code": 0,  
      "msg": "success"  
    }