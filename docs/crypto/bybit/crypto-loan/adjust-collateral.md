---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/crypto-loan/adjust-collateral
api_type: REST
updated_at: 2026-07-20 19:08:58.072967
---

# Get Completed Loan History

Query for the last 6 months worth of your completed (fully paid off) loans.

> Permission: "Spot trade"

### HTTP Request

GET`/v5/crypto-loan/borrow-history`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
orderId| false| string| Loan order ID  
loanCurrency| false| string| Loan coin name  
collateralCurrency| false| string| Collateral coin name  
limit| false| string| Limit for data size per page. [`1`, `100`]. Default: `10`  
cursor| false| string| Cursor. Use the `nextPageCursor` token from the response to retrieve the next page of the result set  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
list| array| Object  
> borrowTime| string| The timestamp to borrow  
> collateralCurrency| string| Collateral coin  
> expirationTime| string| Loan maturity time, keeps `""` for flexible loan  
> hourlyInterestRate| string| Hourly interest rate 

  * Flexible loan, it is real-time interest rate
  * Fixed term loan: it is fixed term interest rate

  
> initialCollateralAmount| string| Initial amount to mortgage  
> initialLoanAmount| string| Initial loan amount  
> loanCurrency| string| Loan coin  
> loanTerm| string| Loan term, `7`, `14`, `30`, `90`, `180` days, keep `""` for flexible loan  
> orderId| string| Loan order ID  
> repaidInterest| string| Total interest repaid  
> repaidPenaltyInterest| string| Total penalty interest repaid  
> status| integer| Loan order status `1`: fully repaid manually; `2`: fully repaid by liquidation  
nextPageCursor| string| Refer to the `cursor` request parameter  
  
### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/crypto-loan/borrow-history?orderId=1793683005081680384 HTTP/1.1  
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
    print(session.get_completed_loan_history(  
            orderId="1793683005081680384",  
    ))  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
      testnet: true,  
      key: 'xxxxxxxxxxxxxxxxxx',  
      secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
      .getCompletedLoanOrderHistory({ orderId: '1794267532472646144' })  
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
                    "borrowTime": "1728546174028",  
                    "collateralCurrency": "BTC",  
                    "expirationTime": "1729148399000",  
                    "hourlyInterestRate": "0.0000010241",  
                    "initialCollateralAmount": "0.0494727",  
                    "initialLoanAmount": "1",  
                    "loanCurrency": "ETH",  
                    "loanTerm": "7",  
                    "orderId": "1793569729874260992",  
                    "repaidInterest": "0.00000515",  
                    "repaidPenaltyInterest": "0",  
                    "status": 1  
                }  
            ],  
            "nextPageCursor": ""  
        },  
        "retExtInfo": {},  
        "time": 1728632014857  
    }

---

# 查詢已結清的借貸歷史訂單

> 權限: "現貨交易"

信息

支持查詢過去6個月的已完結訂單紀錄

### HTTP 請求

GET`/v5/crypto-loan/borrow-history`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
orderId| false| string| 借貸訂單ID  
loanCurrency| false| string| 借貸幣種  
collateralCurrency| false| string| 質押幣種  
limit| false| string| 每頁數量限制. [`1`, `100`]. 默認: `10`  
cursor| false| string| 游標，用於分頁  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
list| array| Object  
> borrowTime| string| 借貸時間  
> collateralCurrency| string| 質押幣種  
> expirationTime| string| 借貸到期時間, 活期借貸總是 `""`  
> hourlyInterestRate| string| 按小時計利率 

  * 活期借貸: 實時利率
  * 定期借貸: 定期固定利率

  
> initialCollateralAmount| string| 初始質押金額  
> initialLoanAmount| string| 初始借貸金額  
> loanCurrency| string| 借貸幣種  
> loanTerm| string| 借貸期限 `7`, `14`, `30`, `90`, `180`天, 活期總是`""`  
> orderId| string| 借貸訂單ID  
> repaidInterest| string| 總償還利息金額  
> repaidPenaltyInterest| string| 總償還罰息金額  
> status| integer| 償還方式 `1`: 主動還清`2`: 強平還清  
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
    print(session.get_completed_loan_history(  
            orderId="1793683005081680384",  
    ))  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
      testnet: true,  
      key: 'xxxxxxxxxxxxxxxxxx',  
      secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
      .getCompletedLoanOrderHistory({ orderId: '1794267532472646144' })  
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
                    "borrowTime": "1728546174028",  
                    "collateralCurrency": "BTC",  
                    "expirationTime": "1729148399000",  
                    "hourlyInterestRate": "0.0000010241",  
                    "initialCollateralAmount": "0.0494727",  
                    "initialLoanAmount": "1",  
                    "loanCurrency": "ETH",  
                    "loanTerm": "7",  
                    "orderId": "1793569729874260992",  
                    "repaidInterest": "0.00000515",  
                    "repaidPenaltyInterest": "0",  
                    "status": 1  
                }  
            ],  
            "nextPageCursor": ""  
        },  
        "retExtInfo": {},  
        "time": 1728632014857  
    }