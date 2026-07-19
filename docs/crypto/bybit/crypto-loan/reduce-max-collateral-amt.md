---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/crypto-loan/reduce-max-collateral-amt
api_type: REST
updated_at: 2026-07-19 18:47:55.323289
---

# Get Loan Repayment History

Query for loan repayment transactions. A loan may be repaid in multiple repayments.

> Permission: "Spot trade"

info

  * Supports querying for the last 6 months worth of completed loan orders.
  * Only successful repayments can be queried for.



### HTTP Request

GET`/v5/crypto-loan/repayment-history`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
orderId| false| string| Loan order ID  
repayId| false| string| Repayment tranaction ID  
loanCurrency| false| string| Loan coin name  
limit| false| string| Limit for data size per page. [`1`, `100`]. Default: `10`  
cursor| false| string| Cursor. Use the `nextPageCursor` token from the response to retrieve the next page of the result set  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
list| array| Object  
> collateralCurrency| string| Collateral coin  
> collateralReturn| string| Amount of collateral returned as a result of this repayment. `"0"` if this isn't the final loan repayment  
> loanCurrency| string| Loan coin  
> loanTerm| string| Loan term, `7`, `14`, `30`, `90`, `180` days, keep `""` for flexible loan  
> orderId| string| Loan order ID  
> repayAmount| string| Repayment amount  
> repayId| string| Repayment transaction ID  
> repayStatus| integer| Repayment status, `1`: success; `2`: processing  
> repayTime| string| Repay timestamp  
> repayType| string| Repayment type, `1`: repay by user; `2`: repay by liquidation  
nextPageCursor| string| Refer to the `cursor` request parameter  
  
### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/crypto-loan/repayment-history?repayId=1794271131730737664 HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1728633716794  
    X-BAPI-RECV-WINDOW: 5000  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.get_loan_repayment_history(  
            repayId="1794271131730737664",  
    ))  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
      testnet: true,  
      key: 'xxxxxxxxxxxxxxxxxx',  
      secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
      .getRepaymentHistory({ repayId: '1794271131730737664' })  
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
                    "collateralCurrency": "BTC",  
                    "collateralReturn": "0",  
                    "loanCurrency": "USDT",  
                    "loanTerm": "",  
                    "orderId": "1794267532472646144",  
                    "repayAmount": "100",  
                    "repayId": "1794271131730737664",  
                    "repayStatus": 1,  
                    "repayTime": "1728629786875",  
                    "repayType": "1"  
                }  
            ],  
            "nextPageCursor": ""  
        },  
        "retExtInfo": {},  
        "time": 1728633717935  
    }

---

# 查詢還款紀錄

> 權限: "現貨交易"

信息

  * 支持查詢過去6個月的還款紀錄
  * 僅返還交易成功的還款紀錄



### HTTP 請求

GET`/v5/crypto-loan/repayment-history`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
orderId| false| string| 借貸訂單ID  
repayId| false| string| 還款交易ID  
loanCurrency| false| string| 借貸幣種  
limit| false| string| 每頁數量限制. [`1`, `100`]. 默認: `10`  
cursor| false| string| 游標，用於分頁  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
list| array| Object  
> collateralCurrency| string| 質押幣種  
> collateralReturn| string| 因次還款而返還的質押金額. 如果本次還款操作沒有全部還清借貸, 那麼系統不會主動返還質押金  
> loanCurrency| string| 借貸幣種  
> loanTerm| string| 借貸期限, `7`, `14`, `30`, `90`, `180`天, 活期總是`""`  
> orderId| string| 借貸訂單ID  
> repayAmount| string| 本次還款金額  
> repayId| string| 還款交易ID  
> repayStatus| integer| 還款狀態, `1`: 成功; `2`: 進行中  
> repayTime| string| 還款時間  
> repayType| string| 還款類型, `1`: 用戶主動還款; `2`: 強平導致的還款  
nextPageCursor| string| 下一頁游標  
  
### 請求示例

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/crypto-loan/repayment-history?repayId=1794271131730737664 HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1728633716794  
    X-BAPI-RECV-WINDOW: 5000  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.get_loan_repayment_history(  
            repayId="1794271131730737664",  
    ))  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
      testnet: true,  
      key: 'xxxxxxxxxxxxxxxxxx',  
      secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
      .getRepaymentHistory({ repayId: '1794271131730737664' })  
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
                    "collateralCurrency": "BTC",  
                    "collateralReturn": "0",  
                    "loanCurrency": "USDT",  
                    "loanTerm": "",  
                    "orderId": "1794267532472646144",  
                    "repayAmount": "100",  
                    "repayId": "1794271131730737664",  
                    "repayStatus": 1,  
                    "repayTime": "1728629786875",  
                    "repayType": "1"  
                }  
            ],  
            "nextPageCursor": ""  
        },  
        "retExtInfo": {},  
        "time": 1728633717935  
    }