---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/finance/advanced-earn/liquidity-mining/add-liquidity
api_type: REST
updated_at: 2026-05-27 19:16:54.248209
---

# Claim Interest

info

  * Need authentication. **Up to 5 requests** per second per UID. Requires Earn permission on the API key.
  * Claims all available yield for the specified product. Pass `productId=-1` to claim yield across all your liquidity mining positions at once.
  * Yield is credited to your default account. Account type cannot be specified.



### HTTP Request

POST`/v5/earn/liquidity-mining/claim-interest`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
productId| **true**|  string| Product ID. Pass `-1` to claim interest from all positions at once  
  
### Response Parameters

None

* * *

### Request Example
    
    
    POST /v5/earn/liquidity-mining/claim-interest HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1741651200000  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
         
        "productId": "-1"  
    }  
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "",  
        "result": {},  
        "retExtInfo": {},  
        "time": 1741651200000  
    }

---

# 領取利息

信息

  * 需要身份驗證。每個 UID 每秒**最多 5 次請求** 。API 金鑰需要具備 Earn（理財）權限。
  * 領取指定產品的所有可用收益。傳入 `productId=-1` 可一次性領取所有流動性挖礦持倉的收益。
  * 收益將存入預設帳戶，無法指定帳戶類型。



### HTTP 請求

POST`/v5/earn/liquidity-mining/claim-interest`

### 請求參數

參數| 必填| 類型| 說明  
---|---|---|---  
productId| **true**|  string| 產品 ID。傳入 `-1` 可一次性領取所有持倉的利息  
  
### 響應參數

無

* * *

### 請求示例
    
    
    POST /v5/earn/liquidity-mining/claim-interest HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1741651200000  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
         
        "productId": "-1"  
    }  
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "",  
        "result": {},  
        "retExtInfo": {},  
        "time": 1741651200000  
    }