---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/new-crypto-loan/flexible/repay-collateral
api_type: REST
updated_at: 2026-07-29 18:51:38.897168
---

# Get Repayment History

> Permission: "Spot trade"  
>  UID rate limit: 5 req / second

### HTTP Request

GET`/v5/crypto-loan-flexible/repayment-history`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
repayId| false| string| Repayment tranaction ID  
loanCurrency| false| string| Loan coin name  
limit| false| string| Limit for data size per page. [`1`, `100`]. Default: `10`  
cursor| false| string| Cursor. Use the `nextPageCursor` token from the response to retrieve the next page of the result set  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
list| array| Object  
> loanCurrency| string| Loan coin  
> repayAmount| string| Repayment amount  
> repayId| string| Repayment transaction ID  
> repayStatus| integer| Repayment status, `1`: success; `2`: processing; `3`: fail  
> repayTime| long| Repay timestamp  
> repayType| integer| Repayment type, `1`: repay by user; `2`: repay by liquidation; `5`: repay by delisting; `6`: repay by delay liquidation; `7`: repay by currency  
nextPageCursor| string| Refer to the `cursor` request parameter  
  
### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/crypto-loan-flexible/repayment-history?loanCurrency=BTC HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: XXXXXX  
    X-BAPI-TIMESTAMP: 1752570746227  
    X-BAPI-RECV-WINDOW: 5000  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.get_repayment_history_flexible_crypto_loan(  
        loanCurrency="BTC",  
    ))  
    
    
    
      
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "ok",  
        "result": {  
            "list": [  
                {  
                    "loanCurrency": "BTC",  
                    "repayAmount": "0.007",  
                    "repayId": "1773",  
                    "repayStatus": 1,  
                    "repayTime": 1752570731274,  
                    "repayType": 1  
                },  
                {  
                    "loanCurrency": "BTC",  
                    "repayAmount": "0.006",  
                    "repayId": "1772",  
                    "repayStatus": 1,  
                    "repayTime": 1752570726038,  
                    "repayType": 1  
                },  
                {  
                    "loanCurrency": "BTC",  
                    "repayAmount": "0.005",  
                    "repayId": "1771",  
                    "repayStatus": 1,  
                    "repayTime": 1752569614528,  
                    "repayType": 1  
                }  
            ],  
            "nextPageCursor": "1769"  
        },  
        "retExtInfo": {},  
        "time": 1752570745493  
    }

---

# 查詢還款歷史

> 權限: "現貨"  
>  頻率: 5次/秒

### HTTP 請求

GET`/v5/crypto-loan-flexible/repayment-history`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
repayId| false| string| 還款訂單ID  
loanCurrency| false| string| 借款幣種  
limit| false| string| 每頁數量限制. [`1`, `100`]. 默認: `10`  
cursor| false| string| 游標，用於分頁  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
list| array| Object  
> loanCurrency| string| 借款幣種  
> repayAmount| string| 還款金額  
> repayId| string| 還款交易 ID  
> repayStatus| integer| 還款狀態，`1`: 成功；`2`: 處理中；`3`: 失敗  
> repayTime| long| 還款時間戳  
> repayType| integer| 還款類型，`1`: 用戶還款；`2`: 強制平倉還款；`5`: 下架還款；`6`: 延期強平還款；`7`: 兌幣還款  
nextPageCursor| string| 下一頁游標  
  
### 請求示例

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/crypto-loan-flexible/repayment-history?loanCurrency=BTC HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: XXXXXX  
    X-BAPI-TIMESTAMP: 1752570746227  
    X-BAPI-RECV-WINDOW: 5000  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.get_repayment_history_flexible_crypto_loan(  
        loanCurrency="BTC",  
    ))  
    
    
    
      
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "ok",  
        "result": {  
            "list": [  
                {  
                    "loanCurrency": "BTC",  
                    "repayAmount": "0.007",  
                    "repayId": "1773",  
                    "repayStatus": 1,  
                    "repayTime": 1752570731274,  
                    "repayType": 1  
                },  
                {  
                    "loanCurrency": "BTC",  
                    "repayAmount": "0.006",  
                    "repayId": "1772",  
                    "repayStatus": 1,  
                    "repayTime": 1752570726038,  
                    "repayType": 1  
                },  
                {  
                    "loanCurrency": "BTC",  
                    "repayAmount": "0.005",  
                    "repayId": "1771",  
                    "repayStatus": 1,  
                    "repayTime": 1752569614528,  
                    "repayType": 1  
                }  
            ],  
            "nextPageCursor": "1769"  
        },  
        "retExtInfo": {},  
        "time": 1752570745493  
    }