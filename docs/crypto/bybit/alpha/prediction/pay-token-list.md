---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/alpha/prediction/pay-token-list
api_type: REST
updated_at: 2026-11-13 19:21:11.010048
---

# Get Payment Token List

Query available payment tokens for prediction market trading. Phase 1 supports USDC only.

info

  * Requires API key authentication



### HTTP Request

GET`/v5/alpha/prediction/pay-token-list`

### Request Parameters

None

### Response Parameters

Parameter| Type| Comments  
---|---|---  
tokenCode| string| Payment token code, e.g. `USDC`  
symbol| string| Token symbol  
tokenDecimals| integer| Token decimal precision  
tokenIconUrlDay| string| Token icon URL (light mode)  
tokenIconUrlNight| string| Token icon URL (dark mode)  
supportChains| array| Supported blockchain codes, e.g. `["POLYGON"]`  
  
### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/alpha/prediction/pay-token-list HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1704067200000  
    X-BAPI-RECV-WINDOW: 5000  
    
    
    
      
    
    
    
      
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": [  
            {  
                "tokenCode": "USDC",  
                "symbol": "USDC",  
                "tokenDecimals": 6,  
                "tokenIconUrlDay": "https://example.com/usdc-day.png",  
                "tokenIconUrlNight": "https://example.com/usdc-night.png",  
                "supportChains": ["POLYGON"]  
            }  
        ],  
        "retExtInfo": {},  
        "time": 1704067200000  
    }

---

# 獲取支付代幣列表

查詢預測市場可用的支付代幣。第一階段僅支持 USDC。

信息

  * 需要 API Key 認證



### HTTP 請求

GET`/v5/alpha/prediction/pay-token-list`

### 請求參數

無

### 響應參數

參數| 類型| 說明  
---|---|---  
tokenCode| string| 支付代幣代碼，如 `USDC`  
symbol| string| 代幣符號  
tokenDecimals| integer| 代幣小數精度  
tokenIconUrlDay| string| 代幣圖標 URL（淺色模式）  
tokenIconUrlNight| string| 代幣圖標 URL（深色模式）  
supportChains| array| 支持的區塊鏈代碼列表，如 `["POLYGON"]`  
  
### 請求示例

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/alpha/prediction/pay-token-list HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1704067200000  
    X-BAPI-RECV-WINDOW: 5000  
    
    
    
      
    
    
    
      
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": [  
            {  
                "tokenCode": "USDC",  
                "symbol": "USDC",  
                "tokenDecimals": 6,  
                "tokenIconUrlDay": "https://example.com/usdc-day.png",  
                "tokenIconUrlNight": "https://example.com/usdc-night.png",  
                "supportChains": ["POLYGON"]  
            }  
        ],  
        "retExtInfo": {},  
        "time": 1704067200000  
    }