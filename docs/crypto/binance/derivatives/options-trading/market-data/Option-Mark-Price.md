---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/options-trading/market-data/Option-Mark-Price
api_type: Market Data
updated_at: 2026-01-15T23:41:10.157213
---

# Option Mark Price

## API Description[​](/docs/derivatives/options-trading/market-data/Option-Mark-Price#api-description "Direct link to API Description")

Option mark price and greek info.

## HTTP Request[​](/docs/derivatives/options-trading/market-data/Option-Mark-Price#http-request "Direct link to HTTP Request")

GET `/eapi/v1/mark`

## Request Weight[​](/docs/derivatives/options-trading/market-data/Option-Mark-Price#request-weight "Direct link to Request Weight")

**5**

## Request Parameters[​](/docs/derivatives/options-trading/market-data/Option-Mark-Price#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
symbol| STRING| NO| Option trading pair, e.g BTC-200730-9000-C  
  
## Response Example[​](/docs/derivatives/options-trading/market-data/Option-Mark-Price#response-example "Direct link to Response Example")
    
    
    [  
      {  
        "symbol": "BTC-200730-9000-C",  
        "markPrice": "1343.2883",       // Mark price  
        "bidIV": "1.40000077",          // Implied volatility Buy  
        "askIV": "1.50000153",          // Implied volatility Sell  
        "markIV": "1.45000000"          // Implied volatility mark    
        "delta": "0.55937056",          // delta  
        "theta": "3739.82509871",       // theta  
        "gamma": "0.00010969",          // gamma  
        "vega": "978.58874732",         // vega  
        "highPriceLimit": "1618.241",   // Current highest buy price  
        "lowPriceLimit": "1068.3356"    // Current lowest sell price  
        "riskFreeInterest": "0.1"       // risk free rate  
      }  
    ]

---

# 查询期权标记价格

## 接口描述[​](/docs/zh-CN/derivatives/options-trading/market-data/Option-Mark-Price#接口描述 "接口描述的直接链接")

查询期权标记价格

## HTTP请求[​](/docs/zh-CN/derivatives/options-trading/market-data/Option-Mark-Price#http请求 "HTTP请求的直接链接")

GET `/eapi/v1/mark`

## 请求权重[​](/docs/zh-CN/derivatives/options-trading/market-data/Option-Mark-Price#请求权重 "请求权重的直接链接")

**5**

## 请求参数[​](/docs/zh-CN/derivatives/options-trading/market-data/Option-Mark-Price#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
symbol| STRING| NO| 交易对  
  
## 响应示例[​](/docs/zh-CN/derivatives/options-trading/market-data/Option-Mark-Price#响应示例 "响应示例的直接链接")
    
    
    [  
      {  
        "symbol": "BTC-200730-9000-C",// 交易对  
        "markPrice": "1343.2883",     // 标记价格  
        "bidIV": "1.40000077",        // 买一隐含波动率  
        "askIV": "1.50000153",        // 卖一隐含波动率  
        "markIV": "1.45000000"        // 标记价格隐含波动率  
        "delta": "0.55937056",        // delta  
        "theta": "3739.82509871",     // theta  
        "gamma": "0.00010969",        // gamma  
        "vega": "978.58874732",       // vega  
        "highPriceLimit": "1618.241", // 买最高限价  
        "lowPriceLimit": "1068.3356"  // 卖最低限价  
        "riskFreeInterest": "0.1"     // 无风险利率  
      }  
    ]