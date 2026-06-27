---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/options-trading/trade/Option-Position-Information
api_type: Trading
updated_at: 2026-01-15T23:42:46.312373
---

# Option Position Information (USER_DATA)

## API Description[​](/docs/derivatives/options-trading/trade/Option-Position-Information#api-description "Direct link to API Description")

Get current position information.

## HTTP Request[​](/docs/derivatives/options-trading/trade/Option-Position-Information#http-request "Direct link to HTTP Request")

GET `/eapi/v1/position`

## Request Weight[​](/docs/derivatives/options-trading/trade/Option-Position-Information#request-weight "Direct link to Request Weight")

**5**

## Request Parameters[​](/docs/derivatives/options-trading/trade/Option-Position-Information#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
symbol| STRING| NO| Option trading pair, e.g BTC-200730-9000-C  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## Response Example[​](/docs/derivatives/options-trading/trade/Option-Position-Information#response-example "Direct link to Response Example")
    
    
    [  
      {  
        "entryPrice": "1000",               // Average entry price  
        "symbol": "BTC-200730-9000-C",      // Option trading pair  
        "side": "SHORT",                    // Position direction  
        "quantity": "-0.1",                 // Number of positions (positive numbers represent long positions, negative number represent short positions)  
        "markValue": "105.00138",           // Current market value  
        "unrealizedPNL": "-5.00138",        // Unrealized profit/loss  
        "markPrice": "1050.0138",           // Mark price  
        "strikePrice": "9000",              // Strike price  
        "expiryDate": 1593511200000,         // Exercise time  
        "priceScale": 2,  
        "quantityScale": 2,  
        "optionSide": "CALL",               // option type  
        "quoteAsset": "USDT",               // quote asset  
        "time": 1762872654561,              // last update time  
        "bidQuantity": "0.0000",            // buy order qty     
        "askQuantity": "0.0000"             // sell order qty  
       }  
    ]

---

# 仓位信息 (USER_DATA)

## 接口描述[​](/docs/zh-CN/derivatives/options-trading/trade/Option-Position-Information#接口描述 "接口描述的直接链接")

获取仓位信息

## HTTP请求[​](/docs/zh-CN/derivatives/options-trading/trade/Option-Position-Information#http请求 "HTTP请求的直接链接")

GET `/eapi/v1/position`

## 请求权重[​](/docs/zh-CN/derivatives/options-trading/trade/Option-Position-Information#请求权重 "请求权重的直接链接")

**5**

## 请求参数[​](/docs/zh-CN/derivatives/options-trading/trade/Option-Position-Information#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
symbol| STRING| NO| 交易对如BTC-200730-9000-C  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## 响应示例[​](/docs/zh-CN/derivatives/options-trading/trade/Option-Position-Information#响应示例 "响应示例的直接链接")
    
    
    [  
      {  
        "entryPrice": "1000",             // 开仓均价  
        "symbol": "BTC-200730-9000-C",    // 交易对  
        "side": "SHORT",                  // 仓位方向  
        "quantity": "-0.1",               // 仓位数量  
        "markValue": "105.00138",         // 期权价值  
        "unrealizedPNL": "-5.00138",      // 未实现盈亏  
        "markPrice": "1050.0138",         // 期权标记价格  
        "strikePrice": "9000",            // 行权价  
        "expiryDate": 1593511200000,       // 行权时间  
        "priceScale": 2,                  // 价格精度   
        "quantityScale": 2,               // 数量精度  
        "optionSide": "CALL",             // 期权方向  
        "quoteAsset": "USDT",             // 报价资产  
        "time": 1762872654561,  
        "bidQuantity": "0.0000",          // 买单数量  
        "askQuantity": "0.0000"           // 卖单数量  
       }  
    ]