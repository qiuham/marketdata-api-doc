---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/new-crypto-loan/fixed/available-inventory
api_type: REST
updated_at: 2026-10-31 18:35:08.910524
---

# Get Available Inventory

> Permission: "Spot trade"  
>  UID rate limit: 5 req / second

### HTTP Request

GET`/v5/crypto-loan-fixed/available-inventory`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
currency| **true**|  string| Coin name, uppercase only  
term| **true**|  string| Fixed term `7`: 7 days; `14`: 14 days; `30`: 30 days; `90`: 90 days; `180`: 180 days  
annualRate| **true**|  string| Customizable annual interest rate, e.g., `0.02` means 2%  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
currency| string| Coin name  
term| string| Loan term  
annualRate| string| Annual borrow rate  
availableInventory| string| Available inventory of the lending pool  
updateTime| string| Update timestamp  
  
### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/crypto-loan-fixed/available-inventory?currency=USDT&term=7&annualRate=0.02 HTTP/1.1  
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
    print(session.get_available_inventory_fixed_crypto_loan(  
        currency="USDT",  
        term="7",  
        annualRate="0.02",  
    ))  
    
    
    
      
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "currency": "USDT",  
            "term": "7",  
            "annualRate": "0.02",  
            "availableInventory": "50000000",  
            "updateTime": "1699272487"  
        },  
        "retExtInfo": {},  
        "time": 1678886400000  
    }

---

# 查詢定期可借存量

> 權限: "現貨"  
>  頻率: 5次/秒

### HTTP 請求

GET`/v5/crypto-loan-fixed/available-inventory`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
currency| **true**|  string| 幣種名稱，僅限大寫  
term| **true**|  string| 固定期限 `7`: 7 天；`14`: 14 天；`30`: 30 天；`90`: 90 天；`180`: 180 天  
annualRate| **true**|  string| 可自訂年利率，例如 `0.02` 表示 2%  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
currency| string| 幣種名稱  
term| string| 借款期限  
annualRate| string| 借款年利率  
availableInventory| string| 借貸池可用存量  
updateTime| string| 更新時間戳  
  
### 請求示例

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/crypto-loan-fixed/available-inventory?currency=USDT&term=7&annualRate=0.02 HTTP/1.1  
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
    print(session.get_available_inventory_fixed_crypto_loan(  
        currency="USDT",  
        term="7",  
        annualRate="0.02",  
    ))  
    
    
    
      
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "currency": "USDT",  
            "term": "7",  
            "annualRate": "0.02",  
            "availableInventory": "50000000",  
            "updateTime": "1699272487"  
        },  
        "retExtInfo": {},  
        "time": 1678886400000  
    }