---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/options-trading/market-data/Historical-Exercise-Records
api_type: Market Data
updated_at: 2026-01-15T23:41:03.169908
---

# Historical Exercise Records

## API Description[​](/docs/derivatives/options-trading/market-data/Historical-Exercise-Records#api-description "Direct link to API Description")

Get historical exercise records.

  * REALISTIC_VALUE_STRICKEN -> Exercised
  * EXTRINSIC_VALUE_EXPIRED -> Expired OTM



## HTTP Request[​](/docs/derivatives/options-trading/market-data/Historical-Exercise-Records#http-request "Direct link to HTTP Request")

GET `/eapi/v1/exerciseHistory`

## Request Weight[​](/docs/derivatives/options-trading/market-data/Historical-Exercise-Records#request-weight "Direct link to Request Weight")

**3**

## Request Parameters[​](/docs/derivatives/options-trading/market-data/Historical-Exercise-Records#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
underlying| STRING| NO| Underlying index like BTCUSDT  
startTime| LONG| NO| Start Time  
endTime| LONG| NO| End Time  
limit| INT| NO| Number of records Default:100 Max:100  
  
## Response Example[​](/docs/derivatives/options-trading/market-data/Historical-Exercise-Records#response-example "Direct link to Response Example")
    
    
    [  
      {   
        "symbol": "BTC-220121-60000-P",            // symbol    
        "strikePrice": "60000",                    // strike price  
        "realStrikePrice": "38844.69652571",       // real strike price  
        "expiryDate": 1642752000000,               // Exercise time  
        "strikeResult": "REALISTIC_VALUE_STRICKEN" // strike result  
      }  
    ]

---

# 历史行权记录

## 接口描述[​](/docs/zh-CN/derivatives/options-trading/market-data/Historical-Exercise-Records#接口描述 "接口描述的直接链接")

查询行权记录

  * REALISTIC_VALUE_STRICKEN 行权
  * EXTRINSIC_VALUE_EXPIRED 未行权



## HTTP请求[​](/docs/zh-CN/derivatives/options-trading/market-data/Historical-Exercise-Records#http请求 "HTTP请求的直接链接")

GET `/eapi/v1/exerciseHistory`

## 请求权重[​](/docs/zh-CN/derivatives/options-trading/market-data/Historical-Exercise-Records#请求权重 "请求权重的直接链��接")

**3**

## 请求参数[​](/docs/zh-CN/derivatives/options-trading/market-data/Historical-Exercise-Records#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
underlying| STRING| NO| 标的资产如BTCUSDT  
startTime| LONG| NO| 开始时间  
endTime| LONG| NO| 结束时间  
limit| INT| NO| 默认值:100 最大值:100.  
  
## 响应示例[​](/docs/zh-CN/derivatives/options-trading/market-data/Historical-Exercise-Records#响应示例 "响应示例的直接链接")
    
    
    [  
      {   
        "symbol": "BTC-220121-60000-P",            // 交易对    
        "strikePrice": "60000",                    // 行权价  
        "realStrikePrice": "38844.69652571",       // 行权结算价格  
        "expiryDate": 1642752000000,               // 行权时间  
        "strikeResult": "REALISTIC_VALUE_STRICKEN" // 行权结果  
      }  
    ]