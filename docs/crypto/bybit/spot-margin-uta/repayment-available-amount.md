---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/spot-margin-uta/repayment-available-amount
api_type: REST
updated_at: 2026-05-27 19:22:17.515764
---

# Get Available Amount to Repay

### HTTP Request

GET`/v5/spot-margin-trade/repayment-available-amount`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
currency| **true**|  string| Coin name, uppercase only  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
currency| string| Coin name, uppercase only  
lossLessRepaymentAmount| string| Repayment amount = min(spot coin available balance, coin borrow amount)  
  
* * *

### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/spot-margin-trade/repayment-available-amount?currency=BTC HTTP/1.1  
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
    print(session.spot_margin_trade_get_repayment_available_amount(  
        currency="BTC"  
    ))  
    
    
    
      
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "Success",  
        "result": {  
            "lossLessRepaymentAmount": "0.02000000",  
            "currency": "BTC"  
        },  
        "retExtInfo": {},  
        "time": 1756273388821  
    }

---

# 查詢負債幣種可還款金額

### HTTP 請求

GET`/v5/spot-margin-trade/repayment-available-amount`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
currency| **true**|  string| 幣名稱，僅限大寫  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
currency| string| 幣名稱，僅限大寫  
lossLessRepaymentAmount| string| 還款金額=min(現貨幣可用餘額，借幣金額)  
  
* * *

### 請求示例

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/spot-margin-trade/repayment-available-amount?currency=BTC HTTP/1.1  
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
            "lossLessRepaymentAmount": "0.02000000",  
            "currency": "BTC"  
        },  
        "retExtInfo": {},  
        "time": 1756273388821  
    }