---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/usds-margined-futures/market-data/websocket-api
api_type: WebSocket
updated_at: 2026-01-15T23:47:03.526249
---

# Order Book

## API Description[​](/docs/derivatives/usds-margined-futures/market-data/websocket-api#api-description "Direct link to API Description")

Get current order book. Note that this request returns limited market depth. If you need to continuously monitor order book updates, please consider using Websocket Market Streams:

  * `<symbol>@depth<levels>`
  * `<symbol>@depth`



You can use `depth` request together with `<symbol>@depth` streams to maintain a local order book.

## Method[​](/docs/derivatives/usds-margined-futures/market-data/websocket-api#method "Direct link to Method")

`depth`

**Note** :

> Retail Price Improvement(RPI) orders are not visible and excluded in the response message.

## Request[​](/docs/derivatives/usds-margined-futures/market-data/websocket-api#request "Direct link to Request")
    
    
    {  
        "id": "51e2affb-0aba-4821-ba75-f2625006eb43",  
        "method": "depth",  
        "params": {  
          "symbol": "BTCUSDT"  
        }  
    }  
    

## Request Weight[​](/docs/derivatives/usds-margined-futures/market-data/websocket-api#request-weight "Direct link to Request Weight")

Adjusted based on the limit:

Limit| Weight  
---|---  
5, 10, 20, 50| 2  
100| 5  
500| 10  
1000| 20  
  
## Request Parameters[​](/docs/derivatives/usds-margined-futures/market-data/websocket-api#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
symbol| STRING| YES|   
limit| INT| NO| Default 500; Valid limits:[5, 10, 20, 50, 100, 500, 1000]  
  
## Response Example[​](/docs/derivatives/usds-margined-futures/market-data/websocket-api#response-example "Direct link to Response Example")
    
    
    {  
      "id": "51e2affb-0aba-4821-ba75-f2625006eb43",  
      "status": 200,  
      "result": {  
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
      },  
      "rateLimits": [  
        {  
          "rateLimitType": "REQUEST_WEIGHT",  
          "interval": "MINUTE",  
          "intervalNum": 1,  
          "limit": 2400,  
          "count": 5  
        }  
      ]  
    }

---

# 深度信息

## 接口描述[​](/docs/zh-CN/derivatives/usds-margined-futures/market-data/websocket-api#接口描述 "接口描述的直接链接")

获取有限档订单薄信息

## 方式[​](/docs/zh-CN/derivatives/usds-margined-futures/market-data/websocket-api#方式 "方式的直接链接")

`depth`

**注意：** 响应消息不包含RPI订单，其不可见。

## 请求[​](/docs/zh-CN/derivatives/usds-margined-futures/market-data/websocket-api#请求 "请求的直接链接")
    
    
    {  
        "id": "51e2affb-0aba-4821-ba75-f2625006eb43",  
        "method": "depth",  
        "params": {  
          "symbol": "BTCUSDT"  
        }  
    }  
    

## 请求权重[​](/docs/zh-CN/derivatives/usds-margined-futures/market-data/websocket-api#请求权重 "请求权重的直接链接")

limit| 权重  
---|---  
5, 10, 20, 50| 2  
100| 5  
500| 10  
1000| 20  
  
## 请求参数[​](/docs/zh-CN/derivatives/usds-margined-futures/market-data/websocket-api#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
symbol| STRING| YES| 交易对  
limit| INT| NO| 默认 500; 可选值:[5, 10, 20, 50, 100, 500, 1000]  
  
## 响应示例[​](/docs/zh-CN/derivatives/usds-margined-futures/market-data/websocket-api#响应示例 "响应示例的直接链接")
    
    
    {  
      "id": "51e2affb-0aba-4821-ba75-f2625006eb43",  
      "status": 200,  
      "result": {  
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
      },  
      "rateLimits": [  
        {  
          "rateLimitType": "REQUEST_WEIGHT",  
          "interval": "MINUTE",  
          "intervalNum": 1,  
          "limit": 2400,  
          "count": 5  
        }  
      ]  
    }