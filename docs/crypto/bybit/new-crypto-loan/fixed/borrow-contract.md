---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/new-crypto-loan/fixed/borrow-contract
api_type: REST
updated_at: 2026-10-22 18:47:19.937280
---

# Cancel Supply Order

> Permission: "Spot trade"  
>  UID rate limit: 1 req / second

### HTTP Request

POST`/v5/crypto-loan-fixed/supply-order-cancel`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
orderId| **true**|  string| Order ID of fixed supply order  
refundedAccount| false| string| Account to receive the refund. `0`: Funding Account; `1`: EasyEarn. Default: `0`  
  
### Response Parameters

None

### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    POST /v5/crypto-loan-fixed/supply-order-cancel HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: XXXXXX  
    X-BAPI-TIMESTAMP: 1752652612736  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
    Content-Length: 26  
      
    {  
        "orderId": "13577"  
    }  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.cancel_lending_order_fixed_crypto_loan(  
        orderId="13577",  
    ))  
    
    
    
      
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "ok",  
        "result": {},  
        "retExtInfo": {},  
        "time": 1752652613638  
    }

---

# 撤銷存款單

> 權限: "現貨"  
>  頻率: 1次/秒

### HTTP 請求

POST`/v5/crypto-loan-fixed/supply-order-cancel`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
orderId| **true**|  string| 存款單ID  
refundedAccount| false| string| 退款返回的目標帳戶。`0`: 資金帳戶；`1`: EasyEarn。預設值：`0`  
  
### 響應參數

無

### 請求示例

  * HTTP
  * Python
  * Node.js


    
    
    POST /v5/crypto-loan-fixed/supply-order-cancel HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: XXXXXX  
    X-BAPI-TIMESTAMP: 1752652612736  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
    Content-Length: 26  
      
    {  
        "orderId": "13577"  
    }  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.cancel_lending_order_fixed_crypto_loan(  
        orderId="13577",  
    ))  
    
    
    
      
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "ok",  
        "result": {},  
        "retExtInfo": {},  
        "time": 1752652613638  
    }