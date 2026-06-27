---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/options-trading/market-data/Recent-Trades-List
api_type: Market Data
updated_at: 2026-01-15T23:41:10.340713
---

# Recent Trades List

## API Description[​](/docs/derivatives/options-trading/market-data/Recent-Trades-List#api-description "Direct link to API Description")

Get recent market trades

## HTTP Request[​](/docs/derivatives/options-trading/market-data/Recent-Trades-List#http-request "Direct link to HTTP Request")

GET `/eapi/v1/trades`

## Request Weight[​](/docs/derivatives/options-trading/market-data/Recent-Trades-List#request-weight "Direct link to Request Weight")

**5**

## Request Parameters[​](/docs/derivatives/options-trading/market-data/Recent-Trades-List#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
symbol| STRING| YES| Option trading pair, e.g BTC-200730-9000-C  
limit| INT| NO| Number of records Default:100 Max:500  
  
## Response Example[​](/docs/derivatives/options-trading/market-data/Recent-Trades-List#response-example "Direct link to Response Example")
    
    
    [  
        {  
            "id": 2323857420768529130,  
            "tradeId": 1,                    // TradeId  
            "symbol": "BTC-251123-126000-C", // Completed trade price  
            "price": "1300",                 // Completed trade quantity  
            "qty": "0.1",                    // Completed trade quantity  
            "quoteQty": "130",               // Completed trade amount  
            "side": -1,                      // Completed trade direction（-1 Sell，1 Buy）  
            "time": 1762780453623            // Time   
        }  
    ]

---

# 近期成交

## 接口描述[​](/docs/zh-CN/derivatives/options-trading/market-data/Recent-Trades-List#接口描述 "接口描述的直接链接")

获取近期订单簿成交

## HTTP请求[​](/docs/zh-CN/derivatives/options-trading/market-data/Recent-Trades-List#http请求 "HTTP请求的直接链接")

GET `/eapi/v1/trades`

## 请求权重[​](/docs/zh-CN/derivatives/options-trading/market-data/Recent-Trades-List#请求权重 "请求权重的直接链接")

**5**

## 请求参数[​](/docs/zh-CN/derivatives/options-trading/market-data/Recent-Trades-List#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
symbol| STRING| YES| 交易对  
limit| INT| NO| 默认:100，最大500  
  
## 响应示例[​](/docs/zh-CN/derivatives/options-trading/market-data/Recent-Trades-List#响应示例 "响应示例的直接链接")
    
    
    [  
        {  
            "id": 2323857420768529130,  
            "tradeId": 1,                    // TradeId  
            "symbol": "BTC-251123-126000-C", // 交易对  
            "price": "1300",                 // 成交价格  
            "qty": "0.1",                    // 成交量  
            "quoteQty": "130",               // 成交额  
            "side": -1,                      // 主动成交方方向（-1 Sell，1 Buy）  
            "time": 1762780453623            // 时间   
        }  
    ]