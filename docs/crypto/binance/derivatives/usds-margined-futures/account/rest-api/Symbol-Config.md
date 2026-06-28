---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/usds-margined-futures/account/rest-api/Symbol-Config
api_type: Account
updated_at: 2026-01-15T23:46:29.529726
---

# Symbol Configuration(USER_DATA)

## API Description[​](/docs/derivatives/usds-margined-futures/account/rest-api/Symbol-Config#api-description "Direct link to API Description")

Get current account symbol configuration.

## HTTP Request[​](/docs/derivatives/usds-margined-futures/account/rest-api/Symbol-Config#http-request "Direct link to HTTP Request")

GET `/fapi/v1/symbolConfig`

 

## Request Weight[​](/docs/derivatives/usds-margined-futures/account/rest-api/Symbol-Config#request-weight "Direct link to Request Weight")

**5**

## Request Parameters[​](/docs/derivatives/usds-margined-futures/account/rest-api/Symbol-Config#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
symbol| STRING| NO|   
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## Response Example[​](/docs/derivatives/usds-margined-futures/account/rest-api/Symbol-Config#response-example "Direct link to Response Example")
    
    
    [  
      {  
      "symbol": "BTCUSDT",   
      "marginType": "CROSSED",  
      "isAutoAddMargin": false,  
      "leverage": 21,  
      "maxNotionalValue": "1000000",  
      }  
    ]

---

# 交易对配置 (USER_DATA)

## 接口描述[​](/docs/zh-CN/derivatives/usds-margined-futures/account/rest-api/Symbol-Config#接口描述 "接口描述的直接链接")

查询交易对上的基础配置

## HTTP请求[​](/docs/zh-CN/derivatives/usds-margined-futures/account/rest-api/Symbol-Config#http请求 "HTTP请求的直接链接")

GET `/fapi/v1/symbolConfig`

## 请求权重[​](/docs/zh-CN/derivatives/usds-margined-futures/account/rest-api/Symbol-Config#请求权重 "请求权重的直接链接")

**5**

## 请求参数[​](/docs/zh-CN/derivatives/usds-margined-futures/account/rest-api/Symbol-Config#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
symbol| STRING| NO| 交易对  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## 响应示例[​](/docs/zh-CN/derivatives/usds-margined-futures/account/rest-api/Symbol-Config#响应示例 "响应示例的直接链接")
    
    
    [  
      {  
      "symbol": "BTCUSDT",   
      "marginType": "CROSSED",  
      "isAutoAddMargin": false,  
      "leverage": 21,  
      "maxNotionalValue": "1000000",  
      }  
    ]