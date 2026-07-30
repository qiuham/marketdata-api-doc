---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/new-crypto-loan/fixed/borrow-order
api_type: REST
updated_at: 2026-07-30 19:01:32.476178
---

# Cancel Borrow Order

> Permission: "Spot trade"  
>  UID rate limit: 1 req / second

### HTTP Request

POST`/v5/crypto-loan-fixed/borrow-order-cancel`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
orderId| **true**|  string| Order ID of fixed borrow order  
  
### Response Parameters

None

### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    POST /v5/crypto-loan-fixed/borrow-order-cancel HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: XXXXXX  
    X-BAPI-TIMESTAMP: 1752652457987  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
    Content-Length: 26  
      
    {  
        "orderId": "13009"  
    }  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.create_lending_order_fixed_crypto_loan(  
        orderId="13009",  
    ))  
    
    
    
      
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "ok",  
        "result": {},  
        "retExtInfo": {},  
        "time": 1752652458684  
    }

---

# 撤銷借款單

> 權限: "現貨"  
>  頻率: 1次/秒

### HTTP 請求

POST`/v5/crypto-loan-fixed/borrow-order-cancel`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
orderId| **true**|  string| 借款單ID  
  
### 響應參數

無

### 請求示例

  * HTTP
  * Python
  * Node.js


    
    
    POST /v5/crypto-loan-fixed/borrow-order-cancel HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: XXXXXX  
    X-BAPI-TIMESTAMP: 1752652457987  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
    Content-Length: 26  
      
    {  
        "orderId": "13009"  
    }  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.create_lending_order_fixed_crypto_loan(  
        orderId="13009",  
    ))  
    
    
    
      
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "ok",  
        "result": {},  
        "retExtInfo": {},  
        "time": 1752652458684  
    }