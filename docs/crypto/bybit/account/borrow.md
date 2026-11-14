---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/account/borrow
api_type: Account
updated_at: 2026-11-13 19:20:42.714417
---

# Manual Borrow

info

Borrowing via OpenAPI endpoint supports variable rate borrowing only.

### HTTP Request

POST`/v5/account/borrow`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
coin| **true**|  string| coin name, uppercase only  
amount| **true**|  string| Borrow amount  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
result| array| Object  
> coin| string| coin name, uppercase only  
> amount| string| Borrow amount  
  
### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    POST /v5/account/borrow HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1675842997277  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "coin":"BTC",  
        "amount":"0.01"  
    }  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.borrow(  
        coin="BTC",  
        amount="0.01"  
    ))  
    
    
    
      
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "success",  
        "result": {  
            "coin": "BTC",  
            "amount": "0.01"  
        },  
        "retExtInfo": {},  
        "time": 1756197991955  
    }

---

# 手工借款

信息

透過 OpenAPI 端點借款僅支持浮動利率借款。

### HTTP 請求

POST`/v5/account/borrow`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
coin| **true**|  string| 幣名稱，僅限大寫  
amount| **true**|  string| 借款金額  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
result| array| Object  
> coin| string| 幣名稱，僅限大寫  
> amount| string| 借款金額  
  
### 請求示例

  * HTTP
  * Python
  * Node.js


    
    
    POST /v5/account/borrow HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1675842997277  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "coin":"BTC",  
        "amount":"0.01"  
    }  
    
    
    
      
    
    
    
      
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "success",  
        "result": {  
            "coin": "BTC",  
            "amount": "0.01"  
        },  
        "retExtInfo": {},  
        "time": 1756197991955  
    }