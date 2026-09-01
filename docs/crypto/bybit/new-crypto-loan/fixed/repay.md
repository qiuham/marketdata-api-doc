---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/new-crypto-loan/fixed/repay
api_type: REST
updated_at: 2026-09-01 18:45:13.811230
---

# Repay

> Permission: "Spot trade"  
>  UID rate limit: 1 req / second

### HTTP Request

POST`/v5/crypto-loan-fixed/fully-repay`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
loanId| false| string| Loan contract ID. Either `loanId` or `loanCurrency` needs to be passed  
loanCurrency| false| string| Loan coin. Either `loanId` or `loanCurrency` needs to be passed  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
repayId| string| Repayment transaction ID  
  
### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    POST /v5/crypto-loan-fixed/fully-repay HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: XXXXXX  
    X-BAPI-TIMESTAMP: 1752656296791  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
    Content-Length: 50  
      
    {  
        "loanId": "570",  
        "loanCurrency": "ETH"  
    }  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.repay_fixed_crypto_loan(  
        loanId="570",  
        loanCurrency="ETH",  
    ))  
    
    
    
      
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "ok",  
        "result": {  
            "repayId": "1771"  
        },  
        "retExtInfo": {},  
        "time": 1752569614549  
    }

---

# 還款

> 權限: "現貨"  
>  頻率: 1次/秒

### HTTP 請求

POST`/v5/crypto-loan-fixed/fully-repay`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
loanId| false| string| 借款合同ID. `loanId` 和 `loanCurrency`必須傳其中一個  
loanCurrency| false| string| 借款幣種. `loanId` 和 `loanCurrency`必須傳其中一個  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
repayId| string| 還款訂單ID  
  
### 請求示例

  * HTTP
  * Python
  * Node.js


    
    
    POST /v5/crypto-loan-fixed/fully-repay HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: XXXXXX  
    X-BAPI-TIMESTAMP: 1752656296791  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
    Content-Length: 50  
      
    {  
        "loanId": "570",  
        "loanCurrency": "ETH"  
    }  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.repay_fixed_crypto_loan(  
        loanId="570",  
        loanCurrency="ETH",  
    ))  
    
    
    
      
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "ok",  
        "result": {  
            "repayId": "1771"  
        },  
        "retExtInfo": {},  
        "time": 1752569614549  
    }