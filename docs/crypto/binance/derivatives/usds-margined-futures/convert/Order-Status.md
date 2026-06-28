---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/usds-margined-futures/convert/Order-Status
api_type: REST
updated_at: 2026-01-15T23:46:36.681239
---

# Order status(USER_DATA)

## API Description[​](/docs/derivatives/usds-margined-futures/convert/Order-Status#api-description "Direct link to API Description")

Query order status by order ID.

## HTTP Request[​](/docs/derivatives/usds-margined-futures/convert/Order-Status#http-request "Direct link to HTTP Request")

GET `/fapi/v1/convert/orderStatus`

## Request Weight[​](/docs/derivatives/usds-margined-futures/convert/Order-Status#request-weight "Direct link to Request Weight")

**50(IP)**

## Request Parameters[​](/docs/derivatives/usds-margined-futures/convert/Order-Status#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
orderId| STRING| NO| Either orderId or quoteId is required  
quoteId| STRING| NO| Either orderId or quoteId is required  
  
## Response Example[​](/docs/derivatives/usds-margined-futures/convert/Order-Status#response-example "Direct link to Response Example")
    
    
    {  
      "orderId":933256278426274426,  
      "orderStatus":"SUCCESS",  
      "fromAsset":"BTC",  
      "fromAmount":"0.00054414",  
      "toAsset":"USDT",  
      "toAmount":"20",  
      "ratio":"36755",  
      "inverseRatio":"0.00002721",  
      "createTime":1623381330472  
    }

---

# 查询订单状态(USER_DATA)

## 接口描述[​](/docs/zh-CN/derivatives/usds-margined-futures/convert/Order-Status#接口描述 "接口描述的直接链接")

通过 order ID 来查询订单状态。

## HTTP请求[​](/docs/zh-CN/derivatives/usds-margined-futures/convert/Order-Status#http请求 "HTTP请求的直接链接")

GET `/fapi/v1/convert/orderStatus`

## 请求权重[​](/docs/zh-CN/derivatives/usds-margined-futures/convert/Order-Status#请求权重 "请求权重的直接链接")

**50(IP)**

## 请求参数[​](/docs/zh-CN/derivatives/usds-margined-futures/convert/Order-Status#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
orderId| STRING| NO| orderId 和quoteId需要填其中一个  
quoteId| STRING| NO| orderId 和quoteId需要填其中一个  
  
## 响应示例[​](/docs/zh-CN/derivatives/usds-margined-futures/convert/Order-Status#响应示例 "响应示例的直接链接")
    
    
    {  
      "orderId":933256278426274426,  
      "orderStatus":"SUCCESS",  
      "fromAsset":"BTC",  
      "fromAmount":"0.00054414",  
      "toAsset":"USDT",  
      "toAmount":"20",  
      "ratio":"36755",  
      "inverseRatio":"0.00002721",  
      "createTime":1623381330472  
    }