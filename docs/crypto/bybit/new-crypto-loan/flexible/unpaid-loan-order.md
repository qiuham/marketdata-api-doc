---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/new-crypto-loan/flexible/unpaid-loan-order
api_type: REST
updated_at: 2026-07-01 19:30:30.449600
---

# Obtain Max Loan Amount

> Permission: "Spot trade"  
>  UID rate limit: 5 req / second

### HTTP Request

POST`/v5/crypto-loan-common/max-loan`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
currency| **true**|  string| Coin to borrow  
collateralList| false| array<object>|   
> amount| **true**|  string| Collateral amount. Only check funding account balance  
> ccy| **true**|  string| Collateral coin. Both `amount` & `ccy` are required, when you pass "collateralList"  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
currency| string| Coin to borrow  
maxLoan| string| Based on your current collateral, and with the option to add more collateral, you can borrow up to `maxLoan`  
notionalUsd| string| Nontional USD value  
remainingQuota| string| The **remaining** individual platform borrowing limit (shared between main and sub accounts)  
  
### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    POST /v5/crypto-loan-common/max-loan HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: XXXXXX  
    X-BAPI-TIMESTAMP: 1768532512103  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
    Content-Length: 208  
      
    {  
        "currency": "BTC",  
        "collateralList": [  
            {  
                "ccy": "XRP",  
                "amount": "1000"  
            },  
            {  
                "ccy": "USDT",  
                "amount": "1000"  
            }  
        ]  
    }  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.get_max_loan_amount_new_crypto_loan(  
        currency="BTC",  
        collateralList=[  
            {  
                "ccy": "XRP",  
                "amount": "1000"  
            },  
            {  
                "ccy": "USDT",  
                "amount": "1000"  
            }  
        ]  
    ))  
    
    
    
      
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "ok",  
        "result": {  
            "currency": "BTC",  
            "maxLoan": "0.1722",  
            "notionalUsd": "16456.06",  
            "remainingQuota": "9999999.9421"  
        },  
        "retExtInfo": {},  
        "time": 1768533990031  
    }

---

# 獲取最大可借

> 權限: "現貨"  
>  頻率: 5次/秒

### HTTP 請求

POST`/v5/crypto-loan-common/max-loan`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
currency| **true**|  string| 借款幣種  
collateralList| false| array<object>|   
> amount| **true**|  string| 抵押品金額. 僅檢查資金錢包可用  
> ccy| **true**|  string| 抵押品幣種. 當要傳入"collateralList"時, `amount` & `ccy`兩個參數必填  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
currency| string| 借款幣種  
maxLoan| string| 根據已抵押數額, 以及入參時是否新增抵押, 計算出最多可借金額  
notionalUsd| string| 美元價值  
remainingQuota| string| 該帳戶(母子帳戶共享)在平台上**剩餘** 可借額度  
  
### 請求示例

  * HTTP
  * Python
  * Node.js


    
    
    POST /v5/crypto-loan-common/max-loan HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: XXXXXX  
    X-BAPI-TIMESTAMP: 1768532512103  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
    Content-Length: 208  
      
    {  
        "currency": "BTC",  
        "collateralList": [  
            {  
                "ccy": "XRP",  
                "amount": "1000"  
            },  
            {  
                "ccy": "USDT",  
                "amount": "1000"  
            }  
        ]  
    }  
    
    
    
      
    
    
    
      
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "ok",  
        "result": {  
            "currency": "BTC",  
            "maxLoan": "0.1722",  
            "notionalUsd": "16456.06",  
            "remainingQuota": "9999999.9421"  
        },  
        "retExtInfo": {},  
        "time": 1768533990031  
    }