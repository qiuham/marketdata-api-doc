---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/new-crypto-loan/reduce-max-collateral-amt
api_type: REST
updated_at: 2026-05-27 19:19:09.102439
---

# Get Max. Allowed Collateral Reduction Amount

Retrieve the maximum redeemable amount of your collateral asset based on LTV.

> Permission: "Spot trade"  
>  UID rate limit: 5 req / second

### HTTP Request

GET`/v5/crypto-loan-common/max-collateral-amount`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
currency| **true**|  string| Collateral coin  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
maxCollateralAmount| string| Maximum reduction amount  
  
### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/crypto-loan-common/max-collateral-amount?currency=BTC HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: XXXXXX  
    X-BAPI-TIMESTAMP: 1752627687351  
    X-BAPI-RECV-WINDOW: 5000  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.get_max_allowed_collateral_reduction_amount_new_crypto_loan(  
        collateralCurrency="BTC",  
    ))  
    
    
    
      
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "ok",  
        "result": {  
            "maxCollateralAmount": "0.08585184"  
        },  
        "retExtInfo": {},  
        "time": 1752627687596  
    }

---

# 查詢最大可減少的質押金額

查詢某個借貸訂單允許的最大可減少質押金額

> 權限: "現貨"  
>  頻率: 5次/秒

### HTTP 請求

GET`/v5/crypto-loan-common/max-collateral-amount`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
currency| **true**|  string| 質押幣種  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
maxCollateralAmount| string| 最大可減少金額  
  
### 請求示例

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/crypto-loan-common/max-collateral-amount?currency=BTC HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: XXXXXX  
    X-BAPI-TIMESTAMP: 1752627687351  
    X-BAPI-RECV-WINDOW: 5000  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.get_max_allowed_collateral_reduction_amount_new_crypto_loan(  
        collateralCurrency="BTC",  
    ))  
    
    
    
      
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "ok",  
        "result": {  
            "maxCollateralAmount": "0.08585184"  
        },  
        "retExtInfo": {},  
        "time": 1752627687596  
    }