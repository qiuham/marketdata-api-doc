---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/new-crypto-loan/flexible/repay-collateral
api_type: REST
updated_at: 2026-06-30 19:28:44.525966
---

# Collateral Repayment

> Permission: "Spot trade"  
>  UID rate limit: 1 req / second

info

  * Pay interest first, then repay the principal.
  * There are limits on the repayment amount in a single transaction. Please read this [announcement](https://announcements.bybit.com/article/crypto-loan-manual-repayment-update-bltde33509ddde5e8fd/) before repaying with collateral
  * When repaying with collateral, Bybit will charge a repayment fee. The applicable fee rate is the higher of the repayment fee rates for the collateral asset and the debt asset. You can call this endpoint: [View fee rates by asset](https://www.bybit.com/x-api/spot/api/fixed-loan/v1/coin-config) to get "reapyFee" where "pledgeEnable" = 1 for coins' repayment fee rates 



### HTTP Request

POST`/v5/crypto-loan-flexible/repay-collateral`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
loanCurrency| **true**|  string| Loan coin name  
collateralCoin| **true**|  string| Collateral currencies: Use commas to separate multiple collateral currencies  
amount| **true**|  string| Repay amount  
  
### Response Parameters

None

### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    POST /v5/crypto-loan-flexible/repay-collateral HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: XXXXXX  
    X-BAPI-TIMESTAMP: 1752569628364  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
    Content-Length: 52  
      
    {  
      "loanCurrency": "USDT",  
      "amount": "500",  
      "collateralCoin":"BTC"  
    }  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.collateral_repayment_flexible_crypto_loan(  
        loanCurrency="USDT",  
        amount="500",  
        collateralCoin="BTC",  
    ))  
    
    
    
      
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "ok",  
        "result": {},  
        "retExtInfo": {},  
        "time": 1756971550401  
    }

---

# 抵押品還款

> 權限: "現貨"  
>  頻率: 1次/秒

信息

  * 優先還款利息，再還款本金。
  * 單筆還款金額有限制, 在使用抵押品還款前, 請仔細閱讀該[公告](https://announcements.bybit.com/article/crypto-loan-manual-repayment-update-bltde33509ddde5e8fd/)
  * 使用抵押物還款時，Bybit 將收取還款手續費。適用的手續費率為抵押資產和債務資產的還款手續費率中較高的一個。 您可以調此接口：[按資產查看手續費率](https://www.bybit.com/x-api/spot/api/fixed-loan/v1/coin-config) 取得"reapyFee"，其中"pledgeEnable"= 1，以查看各幣種的還款手續費率。



### HTTP 請求

POST`/v5/crypto-loan-flexible/repay-collateral`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
loanCurrency| **true**|  string| 借款幣種  
collateralCoin| **true**|  string| 抵押品幣種: 多個抵押品幣種使用英文逗號分開  
amount| **true**|  string| 還款金額  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
  
無

### 請求示例

  * HTTP
  * Python
  * Node.js


    
    
    POST /v5/crypto-loan-flexible/repay-collateral HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: XXXXXX  
    X-BAPI-TIMESTAMP: 1752569628364  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
    Content-Length: 52  
      
    {  
      "loanCurrency": "USDT",  
      "amount": "500",  
      "collateralCoin":"BTC"  
    }  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.collateral_repayment_flexible_crypto_loan(  
        loanCurrency="USDT",  
        amount="500",  
        collateralCoin="BTC",  
    ))  
    
    
    
      
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "ok",  
        "result": {},  
        "retExtInfo": {},  
        "time": 1756971550401  
    }