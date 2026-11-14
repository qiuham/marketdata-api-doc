---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/alpha/prediction/token-price
api_type: REST
updated_at: 2026-11-13 19:21:17.759596
---

# Get Token Price

Query the current best bid/ask prices for prediction outcome tokens. Use this for quick price checks; for full depth, see [Get Order Book](/docs/v5/alpha/prediction/order-book).

info

  * Maximum 20 token IDs per request
  * Prices are on a 0–1 scale representing implied probability (e.g., `0.65` = 65% chance)



### HTTP Request

POST`/v5/alpha/prediction/token-price`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
tokenIds| **true**|  array| List of outcome token IDs to query. Maximum 20  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
tokenId| string| Outcome token ID  
bestBid| string| Best bid price (0–1)  
bestAsk| string| Best ask price (0–1)  
lastPrice| string| Last traded price (0–1)  
volume24h| string| 24-hour trading volume in USDC  
updateTime| integer| Price last update timestamp (UTC milliseconds)  
  
### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    POST /v5/alpha/prediction/token-price HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1704067200000  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "tokenIds": ["token_yes_123", "token_no_123"]  
    }  
    
    
    
      
    
    
    
      
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": [  
            {  
                "tokenId": "token_yes_123",  
                "bestBid": "0.64",  
                "bestAsk": "0.66",  
                "lastPrice": "0.65",  
                "volume24h": "50000",  
                "updateTime": 1704067200000  
            },  
            {  
                "tokenId": "token_no_123",  
                "bestBid": "0.34",  
                "bestAsk": "0.36",  
                "lastPrice": "0.35",  
                "volume24h": "48000",  
                "updateTime": 1704067200000  
            }  
        ],  
        "retExtInfo": {},  
        "time": 1704067200000  
    }

---

# 獲取代幣價格

查詢預測市場結果代幣的當前最優買賣價格。如需完整深度，請使用 [獲取盤口](/docs/zh-TW/v5/alpha/prediction/order-book)。

信息

  * 每次請求最多 20 個代幣 ID
  * 價格採用 0–1 標度，代表隱含概率（如 `0.65` = 65% 概率）



### HTTP 請求

POST`/v5/alpha/prediction/token-price`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
tokenIds| **true**|  array| 要查詢的結果代幣 ID 列表，最多 20 個  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
tokenId| string| 結果代幣 ID  
bestBid| string| 最優買入價（0–1）  
bestAsk| string| 最優賣出價（0–1）  
lastPrice| string| 最新成交價（0–1）  
volume24h| string| 24 小時交易量（USDC）  
updateTime| integer| 價格最後更新時間戳（UTC 毫秒）  
  
### 請求示例

  * HTTP
  * Python
  * Node.js


    
    
    POST /v5/alpha/prediction/token-price HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1704067200000  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "tokenIds": ["token_yes_123", "token_no_123"]  
    }  
    
    
    
      
    
    
    
      
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": [  
            {  
                "tokenId": "token_yes_123",  
                "bestBid": "0.64",  
                "bestAsk": "0.66",  
                "lastPrice": "0.65",  
                "volume24h": "50000",  
                "updateTime": 1704067200000  
            },  
            {  
                "tokenId": "token_no_123",  
                "bestBid": "0.34",  
                "bestAsk": "0.36",  
                "lastPrice": "0.35",  
                "volume24h": "48000",  
                "updateTime": 1704067200000  
            }  
        ],  
        "retExtInfo": {},  
        "time": 1704067200000  
    }