---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/new-crypto-loan/flexible/loan-orders
api_type: REST
updated_at: 2026-10-06 18:52:12.953166
---

# Get Flexible Loans

Query for your ongoing loans

> Permission: "Spot trade"  
>  UID rate limit: 5 req / second

### HTTP Request

GET`/v5/crypto-loan-flexible/ongoing-coin`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
loanCurrency| false| string| Loan coin name  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
list| array| Object  
> hourlyInterestRate| string| Latest hourly flexible interest rate  
> loanCurrency| string| Loan coin  
> totalDebt| string| Unpaid principal and interest  
> unpaidAmount| string| Unpaid principal  
> unpaidInterest| string| Unpaid interest  
  
### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/crypto-loan-flexible/ongoing-coin?loanCurrency=BTC HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: XXXXXX  
    X-BAPI-TIMESTAMP: 1752570124973  
    X-BAPI-RECV-WINDOW: 5000  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.get_flexible_loans_flexible_crypto_loan(  
        loanCurrency="BTC",  
    ))  
    
    
    
      
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "ok",  
        "result": {  
            "list": [  
                {  
                    "hourlyInterestRate": "0.0000018847396",  
                    "loanCurrency": "ETH",  
                    "totalDebt": "0.10000019",  
                    "unpaidAmount": "0.1",  
                    "unpaidInterest": "0.00000019"  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1760452029499  
    }

---

# 查詢借款中信息

> 權限: "現貨"  
>  頻率: 5次/秒

### HTTP 請求

GET`/v5/crypto-loan-flexible/ongoing-coin`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
loanCurrency| false| string| 借款幣種  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
list| array| Object  
> hourlyInterestRate| string| 最新每小時彈性利率  
> loanCurrency| string| 借款幣種  
> totalDebt| string| 未償還本金與利息總額  
> unpaidAmount| string| 未償還本金  
> unpaidInterest| string| 未償還利息  
  
### 請求示例

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/crypto-loan-flexible/ongoing-coin?loanCurrency=BTC HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: XXXXXX  
    X-BAPI-TIMESTAMP: 1752570124973  
    X-BAPI-RECV-WINDOW: 5000  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.get_flexible_loans_flexible_crypto_loan(  
        loanCurrency="BTC",  
    ))  
    
    
    
      
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "ok",  
        "result": {  
            "list": [  
                {  
                    "hourlyInterestRate": "0.0000018847396",  
                    "loanCurrency": "ETH",  
                    "totalDebt": "0.10000019",  
                    "unpaidAmount": "0.1",  
                    "unpaidInterest": "0.00000019"  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1760452029499  
    }