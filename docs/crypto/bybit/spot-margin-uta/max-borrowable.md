---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/spot-margin-uta/max-borrowable
api_type: REST
updated_at: 2026-06-29 19:32:45.967963
---

# Get Max Borrowable Amount

### HTTP Request

GET`/v5/spot-margin-trade/max-borrowable`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
currency| **true**|  string| Coin name, uppercase only  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
currency| string| Coin name, uppercase only  
maxLoan| string| Max borrowable amount  
  
* * *

### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/spot-margin-trade/max-borrowable?currency=BTC HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1692696840996  
    X-BAPI-RECV-WINDOW: 5000  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.spot_margin_trade_get_max_borrowable(  
        currency="BTC"  
    ))  
    
    
    
      
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "Success",  
        "result": {  
            "maxLoan": "17.54689892",  
            "currency": "BTC"  
        },  
        "retExtInfo": {},  
        "time": 1756261353733  
    }

---

# 查詢最大可借數

### HTTP 請求

GET`/v5/spot-margin-trade/max-borrowable`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
currency| **true**|  string| 幣名稱，僅限大寫  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
currency| string| 幣名稱，僅限大寫  
maxLoan| string| 最高可藉金額  
  
* * *

### 請求示例

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/spot-margin-trade/max-borrowable?currency=BTC HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1692696840996  
    X-BAPI-RECV-WINDOW: 5000  
    
    
    
      
    
    
    
      
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "Success",  
        "result": {  
            "maxLoan": "17.54689892",  
            "currency": "BTC"  
        },  
        "retExtInfo": {},  
        "time": 1756261353733  
    }