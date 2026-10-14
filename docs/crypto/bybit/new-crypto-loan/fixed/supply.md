---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/new-crypto-loan/fixed/supply
api_type: REST
updated_at: 2026-10-14 18:51:02.886840
---

# Get Available Inventory

> Permission: "Spot trade"  
>  UID rate limit: 5 req / second

### HTTP Request

GET`/v5/crypto-loan-flexible/available-inventory`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
currency| **true**|  string| Coin name, uppercase only  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
currency| string| Coin name  
availableInventory| string| Available inventory of the lending pool  
updateTime| string| Update timestamp  
  
### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/crypto-loan-flexible/available-inventory?currency=USDT HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: XXXXXX  
    X-BAPI-TIMESTAMP: XXXXXX  
    X-BAPI-RECV-WINDOW: 5000  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.get_available_inventory_flexible_crypto_loan(  
        currency="USDT",  
    ))  
    
    
    
      
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "currency": "USDT",  
            "availableInventory": "100000000",  
            "updateTime": "1699272487"  
        },  
        "retExtInfo": {},  
        "time": 1678886400000  
    }

---

# 查詢活期可借存量

> 權限: "現貨"  
>  頻率: 5次/秒

### HTTP 請求

GET`/v5/crypto-loan-flexible/available-inventory`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
currency| **true**|  string| 幣種名稱，僅限大寫  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
currency| string| 幣種名稱  
availableInventory| string| 借貸池可用存量  
updateTime| string| 更新時間戳  
  
### 請求示例

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/crypto-loan-flexible/available-inventory?currency=USDT HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: XXXXXX  
    X-BAPI-TIMESTAMP: XXXXXX  
    X-BAPI-RECV-WINDOW: 5000  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.get_available_inventory_flexible_crypto_loan(  
        currency="USDT",  
    ))  
    
    
    
      
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "currency": "USDT",  
            "availableInventory": "100000000",  
            "updateTime": "1699272487"  
        },  
        "retExtInfo": {},  
        "time": 1678886400000  
    }