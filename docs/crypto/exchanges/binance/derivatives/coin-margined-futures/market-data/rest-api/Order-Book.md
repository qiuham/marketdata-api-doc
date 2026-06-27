---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/coin-margined-futures/market-data/rest-api/Order-Book
api_type: Market Data
updated_at: 2026-01-15T23:38:50.402872
---

# Order Book

## API Description[​](/docs/derivatives/coin-margined-futures/market-data/rest-api/Order-Book#api-description "Direct link to API Description")

Query orderbook on specific symbol

## HTTP Request[​](/docs/derivatives/coin-margined-futures/market-data/rest-api/Order-Book#http-request "Direct link to HTTP Request")

GET `/dapi/v1/depth`

## Request Weight[​](/docs/derivatives/coin-margined-futures/market-data/rest-api/Order-Book#request-weight "Direct link to Request Weight")

Adjusted based on the limit:

Limit| Weight  
---|---  
5, 10, 20, 50| 2  
100| 5  
500| 10  
1000| 20  
  
## Request Parameters[​](/docs/derivatives/coin-margined-futures/market-data/rest-api/Order-Book#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
symbol| STRING| YES|   
limit| INT| NO| Default 500; Valid limits:[5, 10, 20, 50, 100, 500, 1000]  
  
## Response Example[​](/docs/derivatives/coin-margined-futures/market-data/rest-api/Order-Book#response-example "Direct link to Response Example")
    
    
    {  
      "lastUpdateId": 16769853,  
      "symbol": "BTCUSD_PERP", // Symbol  
      "pair": "BTCUSD",		 // Pair  
      "E": 1591250106370,   // Message output time  
      "T": 1591250106368,   // Transaction time  
      "bids": [  
        [  
          "9638.0",     	// PRICE  
          "431"    			// QTY  
        ]  
      ],  
      "asks": [  
        [  
          "9638.2",  
          "12"  
        ]  
      ]  
    }

---

# 深度信息

## 接口描述[​](/docs/zh-CN/derivatives/coin-margined-futures/market-data/rest-api/Order-Book#接口描述 "接口描述的直接链接")

查询交易对深度

## HTTP请求[​](/docs/zh-CN/derivatives/coin-margined-futures/market-data/rest-api/Order-Book#http请求 "HTTP请求的直接链接")

GET `/dapi/v1/depth`

## 请求权重[​](/docs/zh-CN/derivatives/coin-margined-futures/market-data/rest-api/Order-Book#请求权重 "请求权重的直接链接")

limit| 权重  
---|---  
5, 10, 20, 50| 2  
100| 5  
500| 10  
1000| 20  
  
## 请求参数[​](/docs/zh-CN/derivatives/coin-margined-futures/market-data/rest-api/Order-Book#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
symbol| STRING| YES| 交易对  
limit| INT| NO| 默认 500; 可选值:[5, 10, 20, 50, 100, 500, 1000]  
  
## 响应示例[​](/docs/zh-CN/derivatives/coin-margined-futures/market-data/rest-api/Order-Book#响应示例 "响应示例的直接链接")
    
    
    {  
      "lastUpdateId": 16769853,  
      "symbol": "BTCUSD_PERP", // 交易对  
      "pair": "BTCUSD",		 // 标的交易对  
      "E": 1591250106370,   // 消息时间  
      "T": 1591250106368,   // 撮合时间  
      "bids": [				 // 买单  
        [  
          "9638.0",     	// 价格  
          "431"    			// 数量  
        ]  
      ],  
      "asks": [				// 卖单  
        [  
          "9638.2",			// 价格  
          "12"				// 数量  
        ]  
      ]  
    }