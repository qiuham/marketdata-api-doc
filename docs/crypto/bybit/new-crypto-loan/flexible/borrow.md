---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/new-crypto-loan/flexible/borrow
api_type: REST
updated_at: 2026-08-17 18:44:51.561648
---

# Repay

Fully or partially repay a loan. If interest is due, that is paid off first, with the loaned amount being paid off only after due interest.

> Permission: "Spot trade"  
>  UID rate limit: 1 req / second

info

  * The repaid amount will be deducted from the Funding wallet.
  * The collateral amount will not be auto returned when you don't fully repay the debt, but you can also adjust collateral amount



### HTTP Request

POST`/v5/crypto-loan-flexible/repay`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
loanCurrency| **true**|  string| Loan coin name  
amount| **true**|  string| Amount to repay  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
repayId| string| Repayment transaction ID  
  
### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    POST /v5/crypto-loan-flexible/repay HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: XXXXXX  
    X-BAPI-TIMESTAMP: 1752569628364  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
    Content-Length: 52  
      
    {  
        "loanCurrency": "BTC",  
        "amount": "0.005"  
    }  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.repay_flexible_crypto_loan(  
        loanCurrency="BTC",  
        loanAmount="0.005",  
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

您可以選擇提前還款, 並且支持部分還款, 如果存在利息, 將優先還利息

> 權限: "現貨"  
>  頻率: 1次/秒

信息

  * 還款金額將從資金帳戶扣除
  * 非完全還清操作, 系統將不會主動退還質押金, 但是您可以自行減少質押金



### HTTP 請求

POST`/v5/crypto-loan-flexible/repay`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
loanCurrency| **true**|  string| 借款幣種  
amount| **true**|  string| 還款金額  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
repayId| string| 還款訂單ID  
  
### 請求示例

  * HTTP
  * Python
  * Node.js


    
    
    POST /v5/crypto-loan-flexible/repay HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: XXXXXX  
    X-BAPI-TIMESTAMP: 1752569628364  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
    Content-Length: 52  
      
    {  
        "loanCurrency": "BTC",  
        "amount": "0.005"  
    }  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.repay_flexible_crypto_loan(  
        loanCurrency="BTC",  
        loanAmount="0.005",  
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