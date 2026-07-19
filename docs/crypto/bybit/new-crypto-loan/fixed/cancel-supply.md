---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/new-crypto-loan/fixed/cancel-supply
api_type: REST
updated_at: 2026-07-19 18:50:34.626052
---

# Renew Borrow Order

> Permission: "Spot trade"  
>  UID rate limit: 1 req / second

info

  * The loan funds are released to the Funding wallet.
  * The collateral funds are deducted from the Funding wallet, so make sure you have enough collateral amount in the Funding wallet.
  * This endpoint allows you to re-borrow the principal that was previously repaid. The renewal amount is the same as the amount previously repaid on this loan.



### HTTP Request

POST`/v5/crypto-loan-fixed/renew`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
loanId| **true**|  string| Loan ID  
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


    
    
    POST /v5/crypto-loan-fixed/renew HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: XXXXXX  
    X-BAPI-TIMESTAMP: 1752633649752  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
    Content-Length: 208  
      
    {  
        "loanId": "2364",  
        "collateralList": {"currency": "ETH","amount": "1"}  
    }  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.renew_fixed_crypto_loan(  
        loanId="2364",  
        collateralList={  
            "currency": "ETH",  
            "amount": "1",  
        },  
    ))  
    
    
    
      
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "ok",  
        "result": {  
            "orderId": 49  
        },  
        "retExtInfo": {},  
        "time": 1764142142931  
    }

---

# 創建續借單

> 權限: "現貨"  
>  頻率: 1次/秒

信息

  * 借款發放到資金帳戶
  * 質押金將從資金帳戶扣減, 因此確保資金帳戶有足額質押幣種
  * 此接口可讓您重新借入先前已償還的本金。續借金額就是之前這筆貸款還款的金額



### HTTP 請求

POST`/v5/crypto-loan-fixed/renew`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
loanId| **true**|  string| 貸款ID  
collateralList| false| array<object>| 抵押幣種清單，最多支持陣列中放入 100 種幣種  
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


    
    
    POST /v5/crypto-loan-fixed/renew HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: XXXXXX  
    X-BAPI-TIMESTAMP: 1752633649752  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
    Content-Length: 208  
      
    {  
        "loanId": "2364",  
        "collateralList": {"currency": "ETH","amount": "1"}  
    }  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.renew_fixed_crypto_loan(  
        loanId="2364",  
        collateralList={  
            "currency": "ETH",  
            "amount": "1",  
        },  
    ))  
    
    
    
      
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "ok",  
        "result": {  
            "orderId": 49  
        },  
        "retExtInfo": {},  
        "time": 1764142142931  
    }