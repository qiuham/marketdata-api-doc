---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/alpha/lp/stake
api_type: REST
updated_at: 2026-07-19 18:45:29.613314
---

# Get Order Book

Query the full order book snapshot (bid/ask depth) for prediction outcome tokens. Useful for estimating price impact before placing a large order.

info

  * Maximum 20 token IDs per request
  * Returns all price levels with available quantity
  * For current best price only, use [Get Token Price](/docs/v5/alpha/prediction/token-price) instead



### HTTP Request

POST`/v5/alpha/prediction/order-book`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
tokenIds| **true**|  array| List of outcome token IDs. Maximum 20  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
tokenId| string| Outcome token ID  
bids| array| Buy orders sorted by price descending  
> price| string| Bid price  
> size| string| Available quantity (shares)  
asks| array| Sell orders sorted by price ascending  
> price| string| Ask price  
> size| string| Available quantity (shares)  
  
### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    POST /v5/alpha/prediction/order-book HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1704067200000  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "tokenIds": ["token_yes_123"]  
    }  
    
    
    
      
    
    
    
      
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": [  
            {  
                "tokenId": "token_yes_123",  
                "bids": [  
                    {"price": "0.64", "size": "1000"},  
                    {"price": "0.63", "size": "2500"}  
                ],  
                "asks": [  
                    {"price": "0.66", "size": "800"},  
                    {"price": "0.67", "size": "1500"}  
                ]  
            }  
        ],  
        "retExtInfo": {},  
        "time": 1704067200000  
    }

---

# 獲取盤口

查詢預測市場結果代幣的完整盤口快照（買賣深度）。適合在下大單前預估價格衝擊。如僅需當前最優價格，請使用 [獲取代幣價格](/docs/zh-TW/v5/alpha/prediction/token-price)。

信息

  * 每次請求最多 20 個代幣 ID
  * 返回所有可用數量的價格檔位



### HTTP 請求

POST`/v5/alpha/prediction/order-book`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
tokenIds| **true**|  array| 結果代幣 ID 列表，最多 20 個  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
tokenId| string| 結果代幣 ID  
bids| array| 買單，按價格降序排列  
> price| string| 買入價格  
> size| string| 可用數量（份額）  
asks| array| 賣單，按價格升序排列  
> price| string| 賣出價格  
> size| string| 可用數量（份額）  
  
### 請求示例

  * HTTP
  * Python
  * Node.js


    
    
    POST /v5/alpha/prediction/order-book HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1704067200000  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "tokenIds": ["token_yes_123"]  
    }  
    
    
    
      
    
    
    
      
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": [  
            {  
                "tokenId": "token_yes_123",  
                "bids": [  
                    {"price": "0.64", "size": "1000"},  
                    {"price": "0.63", "size": "2500"}  
                ],  
                "asks": [  
                    {"price": "0.66", "size": "800"},  
                    {"price": "0.67", "size": "1500"}  
                ]  
            }  
        ],  
        "retExtInfo": {},  
        "time": 1704067200000  
    }