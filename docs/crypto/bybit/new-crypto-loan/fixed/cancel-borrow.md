---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/new-crypto-loan/fixed/cancel-borrow
api_type: REST
updated_at: 2026-09-24 18:46:21.535517
---

# Get Renew Order Info

> Permission: "Spot trade"  
>  UID rate limit: 5 req / second

### HTTP Request

GET`/v5/crypto-loan-fixed/renew-info`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
orderId| false| string| Loan order ID  
orderCurrency| false| string| Loan coin name  
limit| false| string| Limit for data size per page. [`1`, `100`]. Default: `10`  
cursor| false| string| Cursor. Use the `nextPageCursor` token from the response to retrieve the next page of the result set  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
list| array| Object  
> borrowCurrency| string| Borrow currency  
> amount| string| loan amount  
> autoRepay| integer| `1`: Auto Repayment; `2`: Transfer to flexible loan; `0`: No Automatic Repayment. Compatible with existing orders;  
> contractNo| string| Contract number  
> dueTime| string| Due time  
> orderId| integer| Order Id  
> loanId| string| Loan Id  
> renewLoanNo| string| Renew Loan number  
> time| string| timestamps  
nextPageCursor| string| Refer to the `cursor` request parameter  
  
### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/crypto-loan-fixed/renew-info HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: XXXXXX  
    X-BAPI-TIMESTAMP: 1752655239825  
    X-BAPI-RECV-WINDOW: 5000  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.get_renewal_orders_fixed_crypto_loan())  
    
    
    
      
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "ok",  
        "result": {  
            "list": [  
                {  
                    "amount": "11",  
                    "autoRepay": 2,  
                    "borrowCurrency": "USDT",  
                    "contractNo": "2092164378648656896",  
                    "dueTime": "1766750400000",  
                    "loanId": "2364",  
                    "orderId": 49,  
                    "renewLoanNo": "2092170365690461952",  
                    "time": "1764142142913"  
                }  
            ],  
            "nextPageCursor": ""  
        },  
        "retExtInfo": {},  
        "time": 1764208336537  
    }

---

# 查詢個人續借訂單

> 權限: "現貨"  
>  頻率: 5次/秒

### HTTP 請求

GET`/v5/crypto-loan-fixed/renew-info`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
orderId| false| string| 借款訂單 ID  
orderCurrency| false| string| 借款幣種名稱  
limit| false| string| 每頁數量限制. [`1`, `100`]. 默認: `10`  
cursor| false| string| 游標，用於分頁  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
list| array| Object  
> borrowCurrency| string| 放款幣種  
> amount| string| 放款金額  
> autoRepay| integer| `1`:自動還款; `2`:轉活期; `0`: 不自動還款. 兼容存量訂單;  
> contractNo| string| 合約編號  
> dueTime| string| 到期時間  
> orderId| integer| 訂單編號  
> loanId| string| 貸款編號  
> renewLoanNo| string| 續貸編號  
> time| string| 時間戳  
nextPageCursor| string| 請參考 `cursor` 請求參數  
  
### 請求示例

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/crypto-loan-fixed/renew-info HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: XXXXXX  
    X-BAPI-TIMESTAMP: 1752655239825  
    X-BAPI-RECV-WINDOW: 5000  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.get_renewal_orders_fixed_crypto_loan())  
    
    
    
      
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "ok",  
        "result": {  
            "list": [  
                {  
                    "amount": "11",  
                    "autoRepay": 2,  
                    "borrowCurrency": "USDT",  
                    "contractNo": "2092164378648656896",  
                    "dueTime": "1766750400000",  
                    "loanId": "2364",  
                    "orderId": 49,  
                    "renewLoanNo": "2092170365690461952",  
                    "time": "1764142142913"  
                }  
            ],  
            "nextPageCursor": ""  
        },  
        "retExtInfo": {},  
        "time": 1764208336537  
    }