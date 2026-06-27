---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/abandon/borrow
api_type: REST
updated_at: 2026-05-27 19:13:36.382802
---

# Borrow

> Permission: "Spot trade"

info

  * The loan funds are released to the Funding wallet.
  * The collateral funds are deducted from the Funding wallet, so make sure you have enough collateral amount in the Funding wallet.



### HTTP Request

POST`/v5/crypto-loan/borrow`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
loanCurrency| **true**|  string| Loan coin name  
loanAmount| false| string| Amount to borrow

  * **Required** when collateral amount is not filled

  
loanTerm| false| string| Loan term 

  * flexible term: `null` or not passed
  * fixed term: `7`, `14`, `30`, `90`, `180` days

  
collateralCurrency| **true**|  string| Currency used to mortgage  
collateralAmount| false| string| Amount to mortgage

  * **Required** when loan amount is not filled

  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
orderId| string| Loan order ID  
  
### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    POST /v5/crypto-loan/borrow HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1728629356551  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
    Content-Length: 140  
      
    {  
        "loanCurrency": "USDT",  
        "loanAmount": "550",  
        "collateralCurrency": "BTC",  
        "loanTerm": null,  
        "collateralAmount": null  
    }  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.borrow_crypto_loan(  
            loanCurrency="USDT",  
            loanAmount="550",  
            collateralCurrency="BTC",  
            loanTerm=None,  
            collateralAmount=None,  
    ))  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
      testnet: true,  
      key: 'xxxxxxxxxxxxxxxxxx',  
      secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
      .borrowCryptoLoan({  
        loanCurrency: 'USDT',  
        loanAmount: '550',  
        collateralCurrency: 'BTC',  
        loanTerm: null,  
        collateralAmount: null,  
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
            "orderId": "1794267532472646144"  
        },  
        "retExtInfo": {},  
        "time": 1728629357820  
    }

---

# 借款

> 權限: "現貨交易"

信息

  * 借款發放到資金帳戶
  * 質押金將從資金帳戶扣減, 因此確保資金帳戶有足額質押幣種



### HTTP 請求

POST`/v5/crypto-loan/borrow`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
loanCurrency| **true**|  string| 借貸幣種  
loanAmount| false| string| 借貸金額

  * 當抵押金額未填時, 該字段**必填**

  
loanTerm| false| string| 借貸期限 

  * 活期: 傳`null`或者不傳字段
  * 定期: `7`, `14`, `30`, `90`, `180` 天

  
collateralCurrency| **true**|  string| 質押幣種  
collateralAmount| false| string| 質押金額

  * 當借貸金額未填時, 該字段**必填**

  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
orderId| string| 借貸訂單ID  
  
### 請求示例

  * HTTP
  * Python
  * Node.js


    
    
    POST /v5/crypto-loan/borrow HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1728629356551  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
    Content-Length: 140  
      
    {  
        "loanCurrency": "USDT",  
        "loanAmount": "550",  
        "collateralCurrency": "BTC",  
        "loanTerm": null,  
        "collateralAmount": null  
    }  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.borrow_crypto_loan(  
            loanCurrency="USDT",  
            loanAmount="550",  
            collateralCurrency="BTC",  
            loanTerm=None,  
            collateralAmount=None,  
    ))  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
      testnet: true,  
      key: 'xxxxxxxxxxxxxxxxxx',  
      secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
      .borrowCryptoLoan({  
        loanCurrency: 'USDT',  
        loanAmount: '550',  
        collateralCurrency: 'BTC',  
        loanTerm: null,  
        collateralAmount: null,  
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
            "orderId": "1794267532472646144"  
        },  
        "retExtInfo": {},  
        "time": 1728629357820  
    }