---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/alpha/lp/pay-token-price
api_type: REST
updated_at: 2026-11-13 19:21:04.142464
---

# Get LP Pay Token Price

Query current USD prices for one or more payment tokens. Supports batch queries in a single request.

info

  * Supports up to 50 token codes per request
  * Use this to calculate USD value of stake amounts before confirming with users
  * **Rate Limit:** 5 req/s (per user), 5000 req/s (global)



### HTTP Request

POST`/v5/alpha/lp/pay-token-price`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
tokenCode| **true**|  array| Array of token codes to query, e.g. `["CEX_1", "CEX_2"]`. Max 50 items  
chainCode| false| string| Filter by blockchain identifier  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
prices| array| Token price list  
> tokenCode| string| Token identifier  
> tokenSymbol| string| Token symbol  
> priceUsd| string| Current price in USD  
> chainCode| string| Blockchain identifier  
> updateTime| integer| Price update timestamp (Unix seconds)  
  
* * *

### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    POST /v5/alpha/lp/pay-token-price HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1704067200000  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "tokenCode": ["CEX_1", "CEX_2"]  
    }  
    
    
    
      
    
    
    
      
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "prices": [  
                {  
                    "tokenCode": "CEX_1",  
                    "tokenSymbol": "USDT",  
                    "priceUsd": "1.00",  
                    "chainCode": "ETH",  
                    "updateTime": 1704067200  
                },  
                {  
                    "tokenCode": "CEX_2",  
                    "tokenSymbol": "USDC",  
                    "priceUsd": "0.9998",  
                    "chainCode": "ETH",  
                    "updateTime": 1704067200  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1704067200000  
    }

---

# 查詢 LP 支付代幣價格

查詢一種或多種支付代幣的當前 USD 價格，支持批量查詢。

信息

  * 每次請求最多支持 50 個代幣代碼
  * 可在用戶確認質押前調用本接口計算質押金額的 USD 價值
  * **頻率限制：** 5 次/秒（用戶），5000 次/秒（全局）



### HTTP 請求

POST`/v5/alpha/lp/pay-token-price`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
tokenCode| **true**|  array| 待查詢的代幣代碼數組，如 `["CEX_1", "CEX_2"]`，最多 50 個  
chainCode| false| string| 按區塊鏈標識符過濾  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
prices| array| 代幣價格列表  
> tokenCode| string| 代幣標識符  
> tokenSymbol| string| 代幣符號  
> priceUsd| string| 當前 USD 價格  
> chainCode| string| 區塊鏈標識符  
> updateTime| integer| 價格更新時間（Unix 秒）  
  
* * *

### 請求示例

  * HTTP
  * Python
  * Node.js


    
    
    POST /v5/alpha/lp/pay-token-price HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1704067200000  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "tokenCode": ["CEX_1", "CEX_2"]  
    }  
    
    
    
      
    
    
    
      
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "prices": [  
                {  
                    "tokenCode": "CEX_1",  
                    "tokenSymbol": "USDT",  
                    "priceUsd": "1.00",  
                    "chainCode": "ETH",  
                    "updateTime": 1704067200  
                },  
                {  
                    "tokenCode": "CEX_2",  
                    "tokenSymbol": "USDC",  
                    "priceUsd": "0.9998",  
                    "chainCode": "ETH",  
                    "updateTime": 1704067200  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1704067200000  
    }