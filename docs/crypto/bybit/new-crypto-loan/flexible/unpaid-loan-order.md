---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/new-crypto-loan/flexible/unpaid-loan-order
api_type: REST
updated_at: 2026-07-03 19:14:58.776244
---

# Get Borrowable Coins

info

Does not need authentication.

### HTTP Request

GET`/v5/crypto-loan-common/loanable-data`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
vipLevel| false| string| VIP level 

  * `VIP0`, `VIP1`, `VIP2`, `VIP3`, `VIP4`, `VIP5`, `VIP99`(supreme VIP)
  * `PRO1`, `PRO2`, `PRO3`, `PRO4`, `PRO5`, `PRO6`

  
currency| false| string| Coin name, uppercase only  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
list| array| Object  
> currency| string| Coin name  
> fixedBorrowable| boolean| Whether support fixed loan  
> fixedBorrowingAccuracy| integer| Coin precision for fixed loan  
> flexibleBorrowable| boolean| Whether support flexible loan  
> flexibleBorrowingAccuracy| integer| Coin precision for flexible loan  
> maxBorrowingAmount| string| Max borrow limit  
> minFixedBorrowingAmount| string| Minimum amount for each fixed loan order  
> minFlexibleBorrowingAmount| string| Minimum amount for each flexible loan order  
> vipLevel| string| VIP level  
> flexibleAnnualizedInterestRate| integer| The annualized interest rate for flexible borrowing. If the loan currency does not support flexible borrowing, it will always be """"  
> annualizedInterestRate7D| string| The lowest annualized interest rate for fixed borrowing for 7 days that the market can currently provide. If there is no lending in the current market, then it is empty string  
> annualizedInterestRate14D| string| The lowest annualized interest rate for fixed borrowing for 14 days that the market can currently provide. If there is no lending in the current market, then it is empty string  
> annualizedInterestRate30D| string| The lowest annualized interest rate for fixed borrowing for 30 days that the market can currently provide. If there is no lending in the current market, then it is empty string  
> annualizedInterestRate60D| string| The lowest annualized interest rate for fixed borrowing for 60 days that the market can currently provide. If there is no lending in the current market, then it is empty string  
> annualizedInterestRate90D| string| The lowest annualized interest rate for fixed borrowing for 90 days that the market can currently provide. If there is no lending in the current market, then it is empty string  
> annualizedInterestRate180D| string| The lowest annualized interest rate for fixed borrowing for 180 days that the market can currently provide. If there is no lending in the current market, then it is empty string  
  
### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/crypto-loan-common/loanable-data?currency=ETH&vipLevel=VIP5 HTTP/1.1  
    Host: api-testnet.bybit.com  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
    )  
    print(session.get_borrowable_coins_new_crypto_loan())  
    
    
    
      
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "ok",  
        "result": {  
            "list": [  
                {  
                    "currency": "ETH",  
                    "fixedBorrowable": true,  
                    "fixedBorrowingAccuracy": 6,  
                    "flexibleBorrowable": true,  
                    "flexibleBorrowingAccuracy": 4,  
                    "maxBorrowingAmount": "1100",  
                    "minFixedBorrowingAmount": "0.1",  
                    "minFlexibleBorrowingAmount": "0.001",  
                    "vipLevel": "VIP5",  
                    "annualizedInterestRate14D": "0.08",  
                    "annualizedInterestRate180D": "",  
                    "annualizedInterestRate30D": "",  
                    "annualizedInterestRate60D": "",  
                    "annualizedInterestRate7D": "",  
                    "annualizedInterestRate90D": "",  
                    "flexibleAnnualizedInterestRate": "0.001429799316"  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1752573126653  
    }

---

# 查詢可借貸幣種

信息

不需要鑒權

### HTTP 請求

GET`/v5/crypto-loan-common/loanable-data`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
vipLevel| false| string| Vip等級 

  * `VIP0`, `VIP1`, `VIP2`, `VIP3`, `VIP4`, `VIP5`, `VIP99`(supreme VIP)
  * `PRO1`, `PRO2`, `PRO3`, `PRO4`, `PRO5`, `PRO6`

  
currency| false| string| 幣種名稱  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
list| array| Object  
> currency| string| 幣種名稱  
> fixedBorrowable| boolean| 是否支持定期借款  
> fixedBorrowingAccuracy| integer| 定期借款的幣種精度  
> flexibleBorrowable| boolean| 是否支持活期借款  
> flexibleBorrowingAccuracy| integer| 活期借款的幣種精度  
> maxBorrowingAmount| string| 最大借款限額  
> minFixedBorrowingAmount| string| 每筆定期借款訂單的最低金額  
> minFlexibleBorrowingAmount| string| 每筆活期借款訂單的最低金額  
> vipLevel| string| VIP 等級  
> flexibleAnnualizedInterestRate| integer| 活期年化借款利率。如果借貸幣種不支持活期, 則總是空字符串  
> annualizedInterestRate7D| string| 市場目前可提供的7天最低借款年化利率。如果當前市場無存款單，則是空字符串  
> annualizedInterestRate14D| string| 市場目前可提供的14天最低借款年化利率。如果當前市場無存款單，則是空字符串  
> annualizedInterestRate30D| string| 市場目前可提供的30天最低借款年化利率。如果當前市場無存款單，則是空字符串  
> annualizedInterestRate60D| string| 市場目前可提供的60天最低借款年化利率。如果當前市場無存款單，則是空字符串  
> annualizedInterestRate90D| string| 市場目前可提供的90天最低借款年化利率。如果當前市場無存款單，則是空字符串  
> annualizedInterestRate180D| string| 市場目前可提供的180天最低借款年化利率。如果當前市場無存款單，則是空字符串  
  
### 請求示例

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/crypto-loan-common/loanable-data?currency=ETH&vipLevel=VIP5 HTTP/1.1  
    Host: api-testnet.bybit.com  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
    )  
    print(session.get_borrowable_coins_new_crypto_loan())  
    
    
    
      
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "ok",  
        "result": {  
            "list": [  
                {  
                    "currency": "ETH",  
                    "fixedBorrowable": true,  
                    "fixedBorrowingAccuracy": 6,  
                    "flexibleBorrowable": true,  
                    "flexibleBorrowingAccuracy": 4,  
                    "maxBorrowingAmount": "1100",  
                    "minFixedBorrowingAmount": "0.1",  
                    "minFlexibleBorrowingAmount": "0.001",  
                    "vipLevel": "VIP5",  
                    "annualizedInterestRate14D": "0.08",  
                    "annualizedInterestRate180D": "",  
                    "annualizedInterestRate30D": "",  
                    "annualizedInterestRate60D": "",  
                    "annualizedInterestRate7D": "",  
                    "annualizedInterestRate90D": "",  
                    "flexibleAnnualizedInterestRate": "0.001429799316"  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1752573126653  
    }