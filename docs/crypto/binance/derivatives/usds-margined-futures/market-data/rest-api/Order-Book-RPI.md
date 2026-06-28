---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/usds-margined-futures/market-data/rest-api/Order-Book-RPI
api_type: Market Data
updated_at: 2026-01-15T23:46:56.780504
---

# RPI Order Book

## API Description[​](/docs/derivatives/usds-margined-futures/market-data/rest-api/Order-Book-RPI#api-description "Direct link to API Description")

Query symbol orderbook with RPI orders

## HTTP Request[​](/docs/derivatives/usds-margined-futures/market-data/rest-api/Order-Book-RPI#http-request "Direct link to HTTP Request")

GET `/fapi/v1/rpiDepth`

**Note** :

> RPI(Retail Price Improvement) orders are included and aggreated in the response message. Crossed price levels are hidden and invisible.

## Request Weight[​](/docs/derivatives/usds-margined-futures/market-data/rest-api/Order-Book-RPI#request-weight "Direct link to Request Weight")

Adjusted based on the limit:

Limit| Weight  
---|---  
1000| 20  
  
## Request Parameters[​](/docs/derivatives/usds-margined-futures/market-data/rest-api/Order-Book-RPI#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
symbol| STRING| YES|   
limit| INT| NO| Default 1000; Valid limits:[1000]  
  
## Response Example[​](/docs/derivatives/usds-margined-futures/market-data/rest-api/Order-Book-RPI#response-example "Direct link to Response Example")
    
    
    {  
      "lastUpdateId": 1027024,  
      "E": 1589436922972,   // Message output time  
      "T": 1589436922959,   // Transaction time  
      "bids": [  
        [  
          "4.00000000",     // PRICE  
          "431.00000000"    // QTY  
        ]  
      ],  
      "asks": [  
        [  
          "4.00000200",  
          "12.00000000"  
        ]  
      ]  
    }

---

# RPI深度信息

## 接口描述[​](/docs/zh-CN/derivatives/usds-margined-futures/market-data/rest-api/Order-Book-RPI#接口描述 "接口描述的直接链接")

交易对深度信息，包含非交叉的RPI订单

## HTTP请求[​](/docs/zh-CN/derivatives/usds-margined-futures/market-data/rest-api/Order-Book-RPI#http请求 "HTTP请求的直接链接")

GET `/fapi/v1/rpiDepth`

**注意：** 响应消息包含RPI订单数量。相互交叉的价格档位不可见。

## 请求权重[​](/docs/zh-CN/derivatives/usds-margined-futures/market-data/rest-api/Order-Book-RPI#请求权重 "请求权重的直接链接")

limit| 权重  
---|---  
1000| 20  
  
## 请求参数[​](/docs/zh-CN/derivatives/usds-margined-futures/market-data/rest-api/Order-Book-RPI#请求参数 "请求��参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
symbol| STRING| YES| 交易对  
limit| INT| NO| 默认 1000; 可选值:[1000]  
  
## 响应示例[​](/docs/zh-CN/derivatives/usds-margined-futures/market-data/rest-api/Order-Book-RPI#响应示例 "响应示例的直接链接")
    
    
    {  
      "lastUpdateId": 1027024,  
      "E": 1589436922972,   // 消息时间  
      "T": 1589436922959,   // 撮合引擎时间  
      "bids": [				// 买单  
        [  
          "4.00000000",     // 价格  
          "431.00000000"    // 数量  
        ]  
      ],  
      "asks": [				// 卖单  
        [  
          "4.00000200",		// 价格  
          "12.00000000"		// 数量  
        ]  
      ]  
    }