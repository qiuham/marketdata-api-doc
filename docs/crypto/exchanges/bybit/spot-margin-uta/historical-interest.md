---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/spot-margin-uta/historical-interest
api_type: REST
updated_at: 2026-05-27 19:22:13.494355
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

# Unicorn! · GitHub