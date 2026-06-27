---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/new-crypto-loan/fixed/supply-market
api_type: REST
updated_at: 2026-05-27 19:18:57.753731
---

# Borrow

> Permission: "Spot trade"  
>  UID rate limit: 1 req / second

info

  * The loan funds are released to the Funding wallet.
  * The collateral funds are deducted from the Funding wallet, so make sure you have enough collateral amount in the Funding wallet.



### HTTP Request

POST`/v5/crypto-loan-flexible/borrow`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
loanCurrency| **true**|  string| Loan coin name  
loanAmount| **true**|  string| Amount to borrow  
collateralList| false| array<object>| Collateral coin list, supports putting up to 100 currency in the array  
> currency| false| string| Currency used to mortgage  
> amount| false| string| Amount to mortgage  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
orderId| string| Loan order ID  
  
### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    POST /v5/crypto-loan-flexible/borrow HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: XXXXXX  
    X-BAPI-TIMESTAMP: 1752569210041  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
    Content-Length: 244  
      
    {  
        "loanCurrency": "BTC",  
        "loanAmount": "0.1",  
        "collateralList": [  
            {  
                "currency": "USDT",  
                "amount": "1000"  
            },  
            {  
                "currency": "ETH",  
                "amount": "1"  
            }  
        ]  
    }  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.borrow_flexible_crypto_loan(  
        loanCurrency="BTC",  
        loanAmount="0.1",  
        collateralList=[  
            {  
                "currency": "USDT",  
                "amount": "1000"  
            },  
            {  
                "currency": "ETH",  
                "amount": "1"  
            }  
        ]  
    ))  
    
    
    
      
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "ok",  
        "result": {  
            "orderId": "1363"  
        },  
        "retExtInfo": {},  
        "time": 1752569209682  
    }

---

# 借款

> 權限: "現貨"  
>  頻率: 1次/秒

信息

  * 借款發放到資金帳戶
  * 質押金將從資金帳戶扣減, 因此確保資金帳戶有足額質押幣種



### HTTP 請求

POST`/v5/crypto-loan-flexible/borrow`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
loanCurrency| **true**|  string| 借款幣種名稱  
loanAmount| **true**|  string| 借款金額  
collateralList| false| array<object>| 抵押幣種清單，最多支持放入 100 種幣種  
> currency| false| string| 用於抵押的幣種  
> amount| false| string| 抵押金額  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
orderId| string| 借款單ID  
  
### 請求示例

  * HTTP
  * Python
  * Node.js


    
    
    POST /v5/crypto-loan-flexible/borrow HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: XXXXXX  
    X-BAPI-TIMESTAMP: 1752569210041  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
    Content-Length: 244  
      
    {  
        "loanCurrency": "BTC",  
        "loanAmount": "0.1",  
        "collateralList": [  
            {  
                "currency": "USDT",  
                "amount": "1000"  
            },  
            {  
                "currency": "ETH",  
                "amount": "1"  
            }  
        ]  
    }  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.borrow_flexible_crypto_loan(  
        loanCurrency="BTC",  
        loanAmount="0.1",  
        collateralList=[  
            {  
                "currency": "USDT",  
                "amount": "1000"  
            },  
            {  
                "currency": "ETH",  
                "amount": "1"  
            }  
        ]  
    ))  
    
    
    
      
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "ok",  
        "result": {  
            "orderId": "1363"  
        },  
        "retExtInfo": {},  
        "time": 1752569209682  
    }