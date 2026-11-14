---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/crypto-loan/loan-coin
api_type: REST
updated_at: 2026-11-13 19:22:26.174343
---

# Get Borrowable Coins

info

Does not need authentication.

danger

Borrowed coins can be returned at any time before the due date. You'll be charged 3 times the hourly interest during the overdue period. Your collateral will be liquidated to repay a loan and the interest if you fail to make the repayment 48 hours after the due time.

### HTTP Request

GET`/v5/crypto-loan/loanable-data`

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
vipCoinList| array| Object  
> list| array| Object  
>> borrowingAccuracy| integer| The number of decimal places (precision) of this coin  
>> currency| string| Coin name  
>> flexibleHourlyInterestRate| string| Flexible hourly variable interest rate 

  * Flexible Crypto Loans offer an hourly variable interest rate, calculated based on the actual borrowing time per hour, with the option for early repayment
  * Is `""` if the coin does not support flexible loan

  
>> hourlyInterestRate7D| string| Hourly interest rate for 7 days loan. Is `""` if the coin does not support 7 days loan  
>> hourlyInterestRate14D| string| Hourly interest rate for 14 days loan. Is `""` if the coin does not support 14 days loan  
>> hourlyInterestRate30D| string| Hourly interest rate for 30 days loan. Is `""` if the coin does not support 30 days loan  
>> hourlyInterestRate90D| string| Hourly interest rate for 90 days loan. Is `""` if the coin does not support 90 days loan  
>> hourlyInterestRate180D| string| Hourly interest rate for 180 days loan. Is `""` if the coin does not support 180 days loan  
>> maxBorrowingAmount| string| Max. amount to borrow  
>> minBorrowingAmount| string| Min. amount to borrow  
> vipLevel| string| VIP level  
  
### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/crypto-loan/loanable-data?currency=USDT&vipLevel=VIP0 HTTP/1.1  
    Host: api.bybit.com  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
    )  
    print(session.get_borrowable_coins(  
        currency="USDT",  
        vipLevel="VIP0",  
    ))  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
      testnet: true,  
      key: 'xxxxxxxxxxxxxxxxxx',  
      secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
      .getBorrowableCoins({  
        currency: 'USDT',  
        vipLevel: 'VIP0',  
      })  
      .then((response) => {  
        console.log(response);  
      })  
      .catch((error) => {  
        console.error(error);  
      });  
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "request.success",  
        "result": {  
            "vipCoinList": [  
                {  
                    "list": [  
                        {  
                            "borrowingAccuracy": 4,  
                            "currency": "USDT",  
                            "flexibleHourlyInterestRate": "0.0000090346",  
                            "hourlyInterestRate14D": "0.0000207796",  
                            "hourlyInterestRate180D": "",  
                            "hourlyInterestRate30D": "0.00002349",  
                            "hourlyInterestRate7D": "0.0000180692",  
                            "hourlyInterestRate90D": "",  
                            "maxBorrowingAmount": "8000000",  
                            "minBorrowingAmount": "20"  
                        }  
                    ],  
                    "vipLevel": "VIP0"  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1728619315868  
    }

---

# 查詢可借幣種

信息

不需要鑒權

### HTTP 請求

GET`/v5/crypto-loan/loanable-data`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
vipLevel| false| string| Vip等級 

  * `VIP0`, `VIP1`, `VIP2`, `VIP3`, `VIP4`, `VIP5`, `VIP99`(至尊VIP)
  * `PRO1`, `PRO2`, `PRO3`, `PRO4`, `PRO5`, `PRO6`

  
currency| false| string| 幣種名稱  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
vipCoinList| array| Object  
> list| array| Object  
>> borrowingAccuracy| integer| 借貸幣種精度  
>> currency| string| 幣種名稱  
>> flexibleHourlyInterestRate| string| 活期每小時利率

  * 活期質押借幣採用小時浮動利率，按實際借款時長每小時計算利息，可提前還款
  * 如果借貸幣種不支持活期, 則總是`""`

  
>> hourlyInterestRate7D| string| 7天定期每小時利率

  * 利息以實際借款每小時計算利息, 可提前還款, 逾期後每小時將收取3倍小時利息, 逾期超過48小時, 您的抵押資產將被清算以償還貸款和利息
  * 如果借貸幣種不支持7天定期, 則總是`""`

  
>> hourlyInterestRate14D| string| 14天定期每小時利率

  * 利息以實際借款每小時計算利息, 可提前還款, 逾期後每小時將收取3倍小時利息, 逾期超過48小時, 您的抵押資產將被清算以償還貸款和利息
  * 如果借貸幣種不支持14天定期, 則總是`""`

  
>> hourlyInterestRate30D| string| 30天定期每小時利率

  * 利息以實際借款每小時計算利息, 可提前還款, 逾期後每小時將收取3倍小時利息, 逾期超過48小時, 您的抵押資產將被清算以償還貸款和利息
  * 如果借貸幣種不支持30天定期, 則總是`""`

  
>> hourlyInterestRate90D| string| 90天定期每小時利率

  * 利息以實際借款每小時計算利息, 可提前還款, 逾期後每小時將收取3倍小時利息, 逾期超過48小時, 您的抵押資產將被清算以償還貸款和利息
  * 如果借貸幣種不支持90天定期, 則總是`""`

  
>> hourlyInterestRate180D| string| 180天定期每小時利率

  * 利息以實際借款每小時計算利息, 可提前還款, 逾期後每小時將收取3倍小時利息, 逾期超過48小時, 您的抵押資產將被清算以償還貸款和利息
  * 如果借貸幣種不支持180天定期, 則總是`""`

  
>> maxBorrowingAmount| string| 借幣上限  
>> minBorrowingAmount| string| 單次最低可借金額  
> vipLevel| string| Vip等級  
  
### 請求示例

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/crypto-loan/loanable-data?currency=USDT&vipLevel=VIP0 HTTP/1.1  
    Host: api.bybit.com  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
    )  
    print(session.get_borrowable_coins(  
        currency="USDT",  
        vipLevel="VIP0",  
    ))  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
      testnet: true,  
      key: 'xxxxxxxxxxxxxxxxxx',  
      secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
      .getBorrowableCoins({  
        currency: 'USDT',  
        vipLevel: 'VIP0',  
      })  
      .then((response) => {  
        console.log(response);  
      })  
      .catch((error) => {  
        console.error(error);  
      });  
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "request.success",  
        "result": {  
            "vipCoinList": [  
                {  
                    "list": [  
                        {  
                            "borrowingAccuracy": 4,  
                            "currency": "USDT",  
                            "flexibleHourlyInterestRate": "0.0000090346",  
                            "hourlyInterestRate14D": "0.0000207796",  
                            "hourlyInterestRate180D": "",  
                            "hourlyInterestRate30D": "0.00002349",  
                            "hourlyInterestRate7D": "0.0000180692",  
                            "hourlyInterestRate90D": "",  
                            "maxBorrowingAmount": "8000000",  
                            "minBorrowingAmount": "20"  
                        }  
                    ],  
                    "vipLevel": "VIP0"  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1728619315868  
    }