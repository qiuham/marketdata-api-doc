---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/spot-margin-uta/liability
api_type: REST
updated_at: 2026-07-28 19:04:25.076445
---

# Get Liability Info

### HTTP Request

GET`/v5/spot-margin-trade/liability`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
currency| **true**|  string| Coin name, uppercase only  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
currency| string| Coin name, uppercase only  
totalBorrowAmount| string| Total liability = borrowSize  
fixedBorrowAmount| string| Fixed-rate liability  
flexibleBorrowAmount| string| Floating-rate liability = borrowSize - fixedBorrowAmount  
spotTotalBorrow| string| Spot liability + open order liability  
derivativesBorrow| string| Derivatives liability = borrowSize - spotBorrow - reservation  
  
* * *

### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/spot-margin-trade/liability?currency=BTC HTTP/1.1  
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
    print(session.spot_margin_trade_get_liability(  
        currency="BTC"  
    ))  
    
    
    
      
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "Success",  
        "result": {  
            "currency": "BTC",  
            "totalBorrowAmount": "0.05000000",  
            "fixedBorrowAmount": "0.02000000",  
            "flexibleBorrowAmount": "0.03000000",  
            "spotTotalBorrow": "0.04000000",  
            "derivativesBorrow": "0.01000000"  
        },  
        "retExtInfo": {},  
        "time": 1756273388821  
    }

---

# 查詢負債信息

### HTTP 請求

GET`/v5/spot-margin-trade/liability`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
currency| **true**|  string| 幣名稱，僅限大寫  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
currency| string| 幣名稱，僅限大寫  
totalBorrowAmount| string| 總負債 = borrowSize  
fixedBorrowAmount| string| 固定利率負債  
flexibleBorrowAmount| string| 活期利率負債 = borrowSize - fixedBorrowAmount  
spotTotalBorrow| string| 現貨負債 + 掛單負債  
derivativesBorrow| string| 衍生品負債 = borrowSize - spotBorrow - reservation  
  
* * *

### 請求示例

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/spot-margin-trade/liability?currency=BTC HTTP/1.1  
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
            "currency": "BTC",  
            "totalBorrowAmount": "0.05000000",  
            "fixedBorrowAmount": "0.02000000",  
            "flexibleBorrowAmount": "0.03000000",  
            "spotTotalBorrow": "0.04000000",  
            "derivativesBorrow": "0.01000000"  
        },  
        "retExtInfo": {},  
        "time": 1756273388821  
    }