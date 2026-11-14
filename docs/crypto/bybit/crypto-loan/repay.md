---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/crypto-loan/repay
api_type: REST
updated_at: 2026-11-13 19:22:26.253647
---

# Repay

Fully or partially repay a loan. If interest is due, that is paid off first, with the loaned amount being paid off only after due interest.

> Permission: "Spot trade"

info

  * The repaid amount will be deducted from the Funding wallet.
  * The collateral amount will not be auto returned when you don't fully repay the debt, but you can also adjust collateral amount



### HTTP Request

POST`/v5/crypto-loan/repay`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
orderId| **true**|  string| Loan order ID  
amount| **true**|  string| Repay amount  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
repayId| string| Repayment transaction ID  
  
### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    POST /v5/crypto-loan/repay HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1728629785224  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
    Content-Length: 61  
      
    {  
        "orderId": "1794267532472646144",  
        "amount": "100"  
    }  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.repay_crypto_loan(  
            orderId="1794267532472646144",  
            amount="100",  
    ))  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
      testnet: true,  
      key: 'xxxxxxxxxxxxxxxxxx',  
      secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
      .repayCryptoLoan({  
        orderId: '1794267532472646144',  
        amount: '100',  
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
            "repayId": "1794271131730737664"  
        },  
        "retExtInfo": {},  
        "time": 1728629786884  
    }

---

# 還款

您可以選擇提前還款, 並且支持部分還款, 如果存在利息, 將優先還利息

> 權限: "現貨交易"

信息

  * 還款金額將從資金帳戶扣除
  * 非完全還清操作, 系統將不會主動退還質押金, 但是您可以自行減少質押金



### HTTP 請求

POST`/v5/crypto-loan/repay`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
orderId| **true**|  string| 借貸訂單ID  
amount| **true**|  string| 還款金額  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
repayId| string| 還款交易ID  
  
### 請求示例

  * HTTP
  * Python
  * Node.js


    
    
    POST /v5/crypto-loan/repay HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1728629785224  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
    Content-Length: 61  
      
    {  
        "orderId": "1794267532472646144",  
        "amount": "100"  
    }  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.repay_crypto_loan(  
            orderId="1794267532472646144",  
            amount="100",  
    ))  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
      testnet: true,  
      key: 'xxxxxxxxxxxxxxxxxx',  
      secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
      .repayCryptoLoan({  
        orderId: '1794267532472646144',  
        amount: '100',  
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
            "repayId": "1794271131730737664"  
        },  
        "retExtInfo": {},  
        "time": 1728629786884  
    }