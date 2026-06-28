---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/options-trading/market-data/Order-Book
api_type: Market Data
updated_at: 2026-01-15T23:41:10.217699
---

# Order Book

## API Description[​](/docs/derivatives/options-trading/market-data/Order-Book#api-description "Direct link to API Description")

Check orderbook depth on specific symbol

## HTTP Request[​](/docs/derivatives/options-trading/market-data/Order-Book#http-request "Direct link to HTTP Request")

GET `/eapi/v1/depth`

## Request Weight[​](/docs/derivatives/options-trading/market-data/Order-Book#request-weight "Direct link to Request Weight")

limit| weight  
---|---  
5, 10, 20, 50| 1  
100| 5  
500| 10  
1000| 20  
  
## Request Parameters[​](/docs/derivatives/options-trading/market-data/Order-Book#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
symbol| STRING| YES| Option trading pair, e.g BTC-200730-9000-C  
limit| INT| NO| Default:100 Max:1000.Optional value:[10, 20, 50, 100, 500, 1000]  
  
## Response Example[​](/docs/derivatives/options-trading/market-data/Order-Book#response-example "Direct link to Response Example")
    
    
    {  
        "bids": [            // Buy order  
            [  
                "1000.000",  // Price  
                "0.1000"     // Quantity  
            ]  
        ],  
        "asks": [            // Sell order  
            [  
                "1900.000",  // Price  
                "0.1000"     // Quantity  
            ]  
        ],  
        "T": 1762780909676,  // transaction time  
        "lastUpdateId": 361  // update id  
    }

---

# 深度信息

## 接口描述[​](/docs/zh-CN/derivatives/options-trading/market-data/Order-Book#接口描述 "接口描述的直接链接")

查询特定交易对深度

## HTTP请求[​](/docs/zh-CN/derivatives/options-trading/market-data/Order-Book#http请求 "HTTP请求的直接链接")

GET `/eapi/v1/depth`

## 请求权重[​](/docs/zh-CN/derivatives/options-trading/market-data/Order-Book#请求权重 "请求权重的直接链接")

limit| 权重  
---|---  
5, 10, 20, 50| 1  
100| 5  
500| 10  
1000| 20  
  
## 请求参数[​](/docs/zh-CN/derivatives/options-trading/market-data/Order-Book#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
symbol| STRING| YES| 交易对  
limit| INT| NO| 默认 100; 可选值:[10, 20, 50, 100, 500, 1000]  
  
## 响应示例[​](/docs/zh-CN/derivatives/options-trading/market-data/Order-Book#响应示例 "响应示例的直接链接")
    
    
    {  
        "bids": [            // 买单  
            [  
                "1000.000",  // 价格  
                "0.1000"     // 数量  
            ]  
        ],  
        "asks": [            // 卖单  
            [  
                "1900.000",  // 价格  
                "0.1000"     // 数量  
            ]  
        ],  
        "T": 1762780909676,  // 撮合引擎时间  
        "lastUpdateId": 361  // 更新id  
    }