---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/crypto-loan/unpaid-loan-order
api_type: REST
updated_at: 2026-11-13 19:22:29.272690
---

# Get Unpaid Loans

Query for your ongoing loans.

> Permission: "Spot trade"

### HTTP Request

GET`/v5/crypto-loan/ongoing-orders`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
orderId| false| string| Loan order ID  
loanCurrency| false| string| Loan coin name  
collateralCurrency| false| string| Collateral coin name  
loanTermType| false| string| 

  * `1`: fixed term, when query this type, `loanTerm` must be filled
  * `2`: flexible term

By default, query all types  
loanTerm| false| string| `7`, `14`, `30`, `90`, `180` days, working when `loanTermType`=1  
limit| false| string| Limit for data size per page. [`1`, `100`]. Default: `10`  
cursor| false| string| Cursor. Use the `nextPageCursor` token from the response to retrieve the next page of the result set  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
list| array| Object  
> collateralAmount| string| Collateral amount  
> collateralCurrency| string| Collateral coin  
> currentLTV| string| Current LTV  
> expirationTime| string| Loan maturity time, keeps `""` for flexible loan  
> hourlyInterestRate| string| Hourly interest rate 

  * Flexible loan, it is real-time interest rate
  * Fixed term loan: it is fixed term interest rate

  
> loanCurrency| string| Loan coin  
> loanTerm| string| Loan term, `7`, `14`, `30`, `90`, `180` days, keep `""` for flexible loan  
> orderId| string| Loan order ID  
> residualInterest| string| Unpaid interest  
> residualPenaltyInterest| string| Unpaid penalty interest  
> totalDebt| string| Unpaid principal  
nextPageCursor| string| Refer to the `cursor` request parameter  
  
### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/crypto-loan/ongoing-orders?orderId=1793683005081680384 HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1728630979731  
    X-BAPI-RECV-WINDOW: 5000  
    
    
    
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
      .getUnpaidLoanOrders({ orderId: '1793683005081680384' })  
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
            "list": [  
                {  
                    "collateralAmount": "0.0964687",  
                    "collateralCurrency": "BTC",  
                    "currentLTV": "0.4161",  
                    "expirationTime": "1731149999000",  
                    "hourlyInterestRate": "0.0000010633",  
                    "loanCurrency": "USDT",  
                    "loanTerm": "30",  
                    "orderId": "1793683005081680384",  
                    "residualInterest": "0.04016",  
                    "residualPenaltyInterest": "0",  
                    "totalDebt": "1888.005198"  
                }  
            ],  
            "nextPageCursor": ""  
        },  
        "retExtInfo": {},  
        "time": 1728630980861  
    }

---

# 查詢進行中的借貸訂單

> 權限: "現貨交易"

### HTTP 請求

GET`/v5/crypto-loan/ongoing-orders`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
orderId| false| string| 借貸訂單ID  
loanCurrency| false| string| 借貸幣種  
collateralCurrency| false| string| 質押幣種  
loanTermType| false| string| 

  * `1`: 定期, 當查詢定期時, `loanTerm`字段必傳
  * `2`: 活期

默認查詢所有期限類型  
loanTerm| false| string| `7`, `14`, `30`, `90`, `180`天, 當`loanTermType`=1時有效  
limit| false| string| 每頁數量限制. [`1`, `100`]. 默認: `10`  
cursor| false| string| 游標，用於分頁  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
list| array| Object  
> collateralAmount| string| 質押金額  
> collateralCurrency| string| 質押幣種  
> currentLTV| string| 當前的LTV  
> expirationTime| string| 借貸到期時間, 活期總是`""`  
> hourlyInterestRate| string| 按小時計利率 

  * 活期借貸: 實時利率
  * 定期借貸: 定期固定利率

  
> loanCurrency| string| 借貸幣種  
> loanTerm| string| 借貸期限, `7`, `14`, `30`, `90`, `180`天, 活期總是`""`  
> orderId| string| 借貸訂單ID  
> residualInterest| string| 未償還利息  
> residualPenaltyInterest| string| 未償還罰息  
> totalDebt| string| 未償還本金  
nextPageCursor| string| 下一頁游標  
  
### 請求示例

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/crypto-loan/ongoing-orders?orderId=1793683005081680384 HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1728630979731  
    X-BAPI-RECV-WINDOW: 5000  
    
    
    
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
      .getUnpaidLoanOrders({ orderId: '1793683005081680384' })  
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
            "list": [  
                {  
                    "collateralAmount": "0.0964687",  
                    "collateralCurrency": "BTC",  
                    "currentLTV": "0.4161",  
                    "expirationTime": "1731149999000",  
                    "hourlyInterestRate": "0.0000010633",  
                    "loanCurrency": "USDT",  
                    "loanTerm": "30",  
                    "orderId": "1793683005081680384",  
                    "residualInterest": "0.04016",  
                    "residualPenaltyInterest": "0",  
                    "totalDebt": "1888.005198"  
                }  
            ],  
            "nextPageCursor": ""  
        },  
        "retExtInfo": {},  
        "time": 1728630980861  
    }