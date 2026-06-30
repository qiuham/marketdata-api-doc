---
exchange: binance
source_url: https://developers.binance.com/docs/margin_trading/market-data/Query-Margin-PriceIndex
api_type: Market Data
updated_at: 2026-06-30 19:07:15.290337
---

# Query Margin Available Inventory(USER_DATA)

## API Description[​](/docs/margin_trading/market-data/Query-margin-avaliable-inventory#api-description "Direct link to API Description")

Margin available Inventory query

## HTTP Request[​](/docs/margin_trading/market-data/Query-margin-avaliable-inventory#http-request "Direct link to HTTP Request")

GET `/sapi/v1/margin/available-inventory`

## Request Weight(UID)[​](/docs/margin_trading/market-data/Query-margin-avaliable-inventory#request-weightuid "Direct link to Request Weight\(UID\)")

**50**

## Request Parameters[​](/docs/margin_trading/market-data/Query-margin-avaliable-inventory#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
type| STRING| YES| MARGIN,ISOLATED  
  
## Response Example[​](/docs/margin_trading/market-data/Query-margin-avaliable-inventory#response-example "Direct link to Response Example")
    
    
    {  
        "assets": {  
            "MATIC": "100000000",  
            "STPT": "100000000",  
            "TVK": "100000000",  
            "SHIB": "97409653"  
        }  
       "updateTime": 1699272487  
    }

---

# 杠杆可用放贷库存查询(USER_DATA)

## 接口描述[​](/docs/zh-CN/margin_trading/market-data/Query-margin-avaliable-inventory#接口描述 "接口描述的直接链接")

杠杆可用放贷库存查询

## HTTP请求[​](/docs/zh-CN/margin_trading/market-data/Query-margin-avaliable-inventory#http请求 "HTTP请求的直接链接")

GET `/sapi/v1/margin/available-inventory`

## 请求权重(UID)[​](/docs/zh-CN/margin_trading/market-data/Query-margin-avaliable-inventory#请求权重uid "请求权重\(UID\)的直接链接")

**50**

## 请求参数[​](/docs/zh-CN/margin_trading/market-data/Query-margin-avaliable-inventory#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
type| STRING| YES| MARGIN,ISOLATED  
  
## 响应示例[​](/docs/zh-CN/margin_trading/market-data/Query-margin-avaliable-inventory#响应示例 "响应示例的直接链接")
    
    
    {  
        "assets": {  
            "MATIC": "100000000",  
            "STPT": "100000000",  
            "TVK": "100000000",  
            "SHIB": "97409653"  
        }  
      	"updateTime": 1699272487  
    }