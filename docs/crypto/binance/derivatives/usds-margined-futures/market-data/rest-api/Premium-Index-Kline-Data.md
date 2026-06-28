---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/usds-margined-futures/market-data/rest-api/Premium-Index-Kline-Data
api_type: Market Data
updated_at: 2026-01-15T23:47:00.157523
---

# Premium index Kline Data

## API Description[​](/docs/derivatives/usds-margined-futures/market-data/rest-api/Premium-Index-Kline-Data#api-description "Direct link to API Description")

Premium index kline bars of a symbol. Klines are uniquely identified by their open time.

## HTTP Request[​](/docs/derivatives/usds-margined-futures/market-data/rest-api/Premium-Index-Kline-Data#http-request "Direct link to HTTP Request")

GET `/fapi/v1/premiumIndexKlines`

## Request Weight[​](/docs/derivatives/usds-margined-futures/market-data/rest-api/Premium-Index-Kline-Data#request-weight "Direct link to Request Weight")

based on parameter `LIMIT`

LIMIT| weight  
---|---  
[1,100)| 1  
[100, 500)| 2  
[500, 1000]| 5  
> 1000| 10  
  
## Request Parameters[​](/docs/derivatives/usds-margined-futures/market-data/rest-api/Premium-Index-Kline-Data#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
symbol| STRING| YES|   
interval| ENUM| YES|   
startTime| LONG| NO|   
endTime| LONG| NO|   
limit| INT| NO| Default 500; max 1500.  
  
>   * If startTime and endTime are not sent, the most recent klines are returned.
> 


## Response Example[​](/docs/derivatives/usds-margined-futures/market-data/rest-api/Premium-Index-Kline-Data#response-example "Direct link to Response Example")
    
    
    [  
      [  
        1691603820000,          // Open time  
        "-0.00042931",          // Open  
        "-0.00023641",          // High  
        "-0.00059406",          // Low  
        "-0.00043659",          // Close  
        "0",                    // Ignore  
        1691603879999,          // Close time  
        "0",                    // Ignore  
        12,                     // Ignore  
        "0",                    // Ignore  
        "0",                    // Ignore  
        "0"                     // Ignore  
      ]  
    ]

---

# 溢价指数K线数据

## 接口描述[​](/docs/zh-CN/derivatives/usds-margined-futures/market-data/rest-api/Premium-Index-Kline-Data#接口描述 "接口描述的直接链接")

合约溢价指数K线。每根K线的开盘时间可视为唯一ID。

## HTTP请求[​](/docs/zh-CN/derivatives/usds-margined-futures/market-data/rest-api/Premium-Index-Kline-Data#http请求 "HTTP请求的直接链接")

GET `/fapi/v1/premiumIndexKlines`

## 请求权重[​](/docs/zh-CN/derivatives/usds-margined-futures/market-data/rest-api/Premium-Index-Kline-Data#请求权重 "请求权重的直接链接")

取决于请求中的LIMIT参数

LIMIT参数| 权重  
---|---  
[1,100)| 1  
[100, 500)| 2  
[500, 1000]| 5  
> 1000| 10  
  
## 请求参数[​](/docs/zh-CN/derivatives/usds-margined-futures/market-data/rest-api/Premium-Index-Kline-Data#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
symbol| STRING| YES| 交易对  
interval| ENUM| YES| 时间间隔  
startTime| LONG| NO| 起始时间  
endTime| LONG| NO| 结束时间  
limit| INT| NO| 默认值:500 最大值:1500  
  
>   * 缺省返回最近的数据
> 


## 响应示例[​](/docs/zh-CN/derivatives/usds-margined-futures/market-data/rest-api/Premium-Index-Kline-Data#响应示例 "响应示例的直接链接")
    
    
    [  
      [  
        1691603820000,          // 开盘时间  
        "-0.00042931",          // 开盘价  
        "-0.00023641",          // 最高价  
        "-0.00059406",          // 最低价  
        "-0.00043659",          // 收盘价  
        "0",                    // 请忽略  
        1691603879999,          // 收盘时间  
        "0",                    // 请忽略  
        12,                     // 请忽略  
        "0",                    // 请忽略  
        "0",                    // 请忽略  
        "0"                     // 请忽略  
      ]  
    ]