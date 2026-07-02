---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/new-crypto-loan/fixed/supply-market
api_type: REST
updated_at: 2026-07-02 19:19:40.668413
---

# Get Borrowing History

> Permission: "Spot trade"  
>  UID rate limit: 5 req / second

### HTTP Request

GET`/v5/crypto-loan-flexible/borrow-history`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
orderId| false| string| Loan order ID  
loanCurrency| false| string| Loan coin name  
limit| false| string| Limit for data size per page. [`1`, `100`]. Default: `10`  
cursor| false| string| Cursor. Use the `nextPageCursor` token from the response to retrieve the next page of the result set  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
list| array| Object  
> borrowTime| long| The timestamp to borrow  
> initialLoanAmount| string| Loan amount  
> loanCurrency| string| Loan coin  
> orderId| string| Loan order ID  
> status| integer| Loan order status `1`: success; `2`: processing; `3`: fail  
nextPageCursor| string| Refer to the `cursor` request parameter  
  
### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/crypto-loan-flexible/borrow-history?limit=2 HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: XXXXXX  
    X-BAPI-TIMESTAMP: 1752570519918  
    X-BAPI-RECV-WINDOW: 5000  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.get_borrowing_history_flexible_crypto_loan(  
        limit="2",  
    ))  
    
    
    
      
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "ok",  
        "result": {  
            "list": [  
                {  
                    "borrowTime": 1752569950643,  
                    "initialLoanAmount": "0.006",  
                    "loanCurrency": "BTC",  
                    "orderId": "1364",  
                    "status": 1  
                },  
                {  
                    "borrowTime": 1752569209643,  
                    "initialLoanAmount": "0.1",  
                    "loanCurrency": "BTC",  
                    "orderId": "1363",  
                    "status": 1  
                }  
            ],  
            "nextPageCursor": "1363"  
        },  
        "retExtInfo": {},  
        "time": 1752570519414  
    }

---

# 查詢借款歷史

> 權限: "現貨"  
>  頻率: 5次/秒

### HTTP 請求

GET`/v5/crypto-loan-flexible/borrow-history`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
orderId| false| string| 借款單ID  
loanCurrency| false| string| 借款幣種  
limit| false| string| 每頁數量限制. [`1`, `100`]. 默認: `10`  
cursor| false| string| 游標，用於分頁  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
list| array| Object  
> borrowTime| long| 借款時間戳  
> initialLoanAmount| string| 借款金額  
> loanCurrency| string| 借款幣種  
> orderId| string| 借款訂單ID  
> status| integer| 借款訂單狀態 `1`: 成功；`2`: 處理中；`3`: 失敗  
nextPageCursor| string| 下一頁游標  
  
### 請求示例

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/crypto-loan-flexible/borrow-history?limit=2 HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: XXXXXX  
    X-BAPI-TIMESTAMP: 1752570519918  
    X-BAPI-RECV-WINDOW: 5000  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.get_borrowing_history_flexible_crypto_loan(  
        limit="2",  
    ))  
    
    
    
      
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "ok",  
        "result": {  
            "list": [  
                {  
                    "borrowTime": 1752569950643,  
                    "initialLoanAmount": "0.006",  
                    "loanCurrency": "BTC",  
                    "orderId": "1364",  
                    "status": 1  
                },  
                {  
                    "borrowTime": 1752569209643,  
                    "initialLoanAmount": "0.1",  
                    "loanCurrency": "BTC",  
                    "orderId": "1363",  
                    "status": 1  
                }  
            ],  
            "nextPageCursor": "1363"  
        },  
        "retExtInfo": {},  
        "time": 1752570519414  
    }