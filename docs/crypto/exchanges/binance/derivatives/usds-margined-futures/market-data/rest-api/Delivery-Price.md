---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/usds-margined-futures/market-data/rest-api/Delivery-Price
api_type: Market Data
updated_at: 2026-01-15T23:46:46.068129
---

# Quarterly Contract Settlement Price

## API Description[​](/docs/derivatives/usds-margined-futures/market-data/rest-api/Delivery-Price#api-description "Direct link to API Description")

Latest price for a symbol or symbols.

## HTTP Request[​](/docs/derivatives/usds-margined-futures/market-data/rest-api/Delivery-Price#http-request "Direct link to HTTP Request")

GET `/futures/data/delivery-price`

## Request Weight[​](/docs/derivatives/usds-margined-futures/market-data/rest-api/Delivery-Price#request-weight "Direct link to Request Weight")

**0**

## Request Parameters[​](/docs/derivatives/usds-margined-futures/market-data/rest-api/Delivery-Price#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
pair| STRING| YES| e.g BTCUSDT  
  
## Response Example[​](/docs/derivatives/usds-margined-futures/market-data/rest-api/Delivery-Price#response-example "Direct link to Response Example")
    
    
    [  
        {  
            "deliveryTime": 1695945600000,  
            "deliveryPrice": 27103.00000000  
        },  
        {  
            "deliveryTime": 1688083200000,  
            "deliveryPrice": 30733.60000000  
        },  
        {  
            "deliveryTime": 1680220800000,  
            "deliveryPrice": 27814.20000000  
        },  
        {  
            "deliveryTime": 1648166400000,  
            "deliveryPrice": 44066.30000000  
        }  
    ]

---

# 季度合约历史结算价

## 接口描述[​](/docs/zh-CN/derivatives/usds-margined-futures/market-data/rest-api/Delivery-Price#接口描述 "接口描述的直接链接")

返回季度合约历史结算价

## HTTP请求[​](/docs/zh-CN/derivatives/usds-margined-futures/market-data/rest-api/Delivery-Price#http请求 "HTTP请求的直接链接")

GET `/futures/data/delivery-price`

## 请求权重[​](/docs/zh-CN/derivatives/usds-margined-futures/market-data/rest-api/Delivery-Price#请求权重 "请求权重的直接链接")

**0**

## 请求参数[​](/docs/zh-CN/derivatives/usds-margined-futures/market-data/rest-api/Delivery-Price#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
pair| STRING| YES| 如BTCUSDT  
  
## 响应示例[​](/docs/zh-CN/derivatives/usds-margined-futures/market-data/rest-api/Delivery-Price#响应示例 "响应示例的直接链接")

> **响应:**
    
    
    [  
        {  
            "deliveryTime": 1695945600000,  
            "deliveryPrice": 27103.00000000  
        },  
        {  
            "deliveryTime": 1688083200000,  
            "deliveryPrice": 30733.60000000  
        },  
        {  
            "deliveryTime": 1680220800000,  
            "deliveryPrice": 27814.20000000  
        },  
        {  
            "deliveryTime": 1648166400000,  
            "deliveryPrice": 44066.30000000  
        }  
    ]