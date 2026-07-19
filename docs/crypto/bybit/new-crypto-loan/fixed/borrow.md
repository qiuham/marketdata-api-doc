---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/new-crypto-loan/fixed/borrow
api_type: REST
updated_at: 2026-07-19 18:50:28.571054
---

# Get Borrow Contract Info

> Permission: "Spot trade"  
>  UID rate limit: 5 req / second

### HTTP Request

GET`/v5/crypto-loan-fixed/borrow-contract-info`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
orderId| false| string| Loan order ID  
loanId| false| string| Loan ID  
orderCurrency| false| string| Loan coin name  
term| false| string| Fixed term `7`: 7 days; `14`: 14 days; `30`: 30 days; `90`: 90 days; `180`: 180 days  
limit| false| string| Limit for data size per page. [`1`, `100`]. Default: `10`  
cursor| false| string| Cursor. Use the `nextPageCursor` token from the response to retrieve the next page of the result set  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
list| array| Object  
> annualRate| string| Annual rate for the borrowing  
> autoRepay| string| Deprecated. `"true"`: enable auto repay, default; `"false"`: disable auto repay  
> borrowCurrency| string| Loan coin  
> borrowTime| string| Loan order timestamp  
> interestPaid| string| Paid interest  
> loanId| string| Loan contract ID  
> orderId| string| Loan order ID  
> repaymentTime| string| Time to repay  
> residualPenaltyInterest| string| Unpaid interest  
> residualPrincipal| string| Unpaid principal  
> status| integer| Loan order status `1`: unrepaid; `2`: fully repaid; `3`: overdue  
> term| string| Fixed term `7`: 7 days; `14`: 14 days; `30`: 30 days; `90`: 90 days; `180`: 180 days  
> repayType| string| `1`:Auto Repayment; `2`:Transfer to flexible loan; `0`: No Automatic Repayment. Compatible with existing orders;  
nextPageCursor| string| Refer to the `cursor` request parameter  
  
### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/crypto-loan-fixed/borrow-contract-info?orderCurrency=ETH HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: XXXXXX  
    X-BAPI-TIMESTAMP: 1752652691909  
    X-BAPI-RECV-WINDOW: 5000  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.get_borrowing_contract_info_fixed_crypto_loan(  
        collateralCurrency="ETH",  
    ))  
    
    
    
      
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "ok",  
        "result": {  
            "list": [  
                {  
                    "annualRate": "0.022",  
                    "autoRepay": "true",  
                    "borrowCurrency": "ETH",  
                    "borrowTime": "1752633756068",  
                    "interestPaid": "0.002531506849315069",  
                    "loanId": "571",  
                    "orderId": "13007",  
                    "repayType": "1",  
                    "repaymentTime": "1755225756068",  
                    "residualPenaltyInterest": "0",  
                    "residualPrincipal": "1.4",  
                    "status": 1,  
                    "term": "30"  
                },  
                {  
                    "annualRate": "0.022",  
                    "autoRepay": "true",  
                    "borrowCurrency": "ETH",  
                    "borrowTime": "1752633696068",  
                    "interestPaid": "0.00018082191780822",  
                    "loanId": "570",  
                    "orderId": "13007",  
                    "repayType": "1",  
                    "repaymentTime": "1755225696068",  
                    "residualPenaltyInterest": "0",  
                    "residualPrincipal": "0.1",  
                    "status": 1,  
                    "term": "30"  
                }  
            ],  
            "nextPageCursor": "568"  
        },  
        "retExtInfo": {},  
        "time": 1752652692603  
    }

---

# 查詢借款合同

> 權限: "現貨"  
>  頻率: 5次/秒

### HTTP 請求

GET`/v5/crypto-loan-fixed/borrow-contract-info`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
orderId| false| string| 借款訂單ID  
loanId| false| string| 借款合同ID  
orderCurrency| false| string| 借款幣種  
term| false| string| 借款期限 `7`: 7天; `14`: 14天; `30`: 30天; `90`: 90天; `180`: 180天  
limit| false| string| 每頁數量限制. [`1`, `100`]. 默認: `10`  
cursor| false| string| 游標，用於分頁  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
list| array| Object  
> annualRate| string| 借款年化利率  
> autoRepay| string| 已廢棄。`"true"`: 開啟自動還款; `"false"`: 關閉自動還款  
> borrowCurrency| string| 借款幣種  
> borrowTime| string| 借款時間  
> interestPaid| string| 已支付利息  
> loanId| string| 借款合同ID  
> orderId| string| 借款訂單ID  
> repaymentTime| string| 還款到期時間  
> residualPenaltyInterest| string| 未繳利息  
> residualPrincipal| string| 未繳本金  
> status| integer| 借款訂單狀態 `1`: 未償還；`2`: 已全額償還；`3`: 逾期  
> term| string| 固定期限 `7`: 7 天；`14`: 14 天；`30`: 30 天；`90`: 90 天；`180`: 180 天  
> repayType| string| `1`:自動還款; `2`:轉活期; `0`: 不自動還款. 兼容存量訂單;  
nextPageCursor| string| 下一頁游標  
  
### 請求示例

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/crypto-loan-fixed/borrow-contract-info?orderCurrency=ETH HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: XXXXXX  
    X-BAPI-TIMESTAMP: 1752652691909  
    X-BAPI-RECV-WINDOW: 5000  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.get_borrowing_contract_info_fixed_crypto_loan(  
        collateralCurrency="ETH",  
    ))  
    
    
    
      
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "ok",  
        "result": {  
            "list": [  
                {  
                    "annualRate": "0.022",  
                    "autoRepay": "true",  
                    "borrowCurrency": "ETH",  
                    "borrowTime": "1752633756068",  
                    "interestPaid": "0.002531506849315069",  
                    "loanId": "571",  
                    "orderId": "13007",  
                    "repayType": "1",  
                    "repaymentTime": "1755225756068",  
                    "residualPenaltyInterest": "0",  
                    "residualPrincipal": "1.4",  
                    "status": 1,  
                    "term": "30"  
                },  
                {  
                    "annualRate": "0.022",  
                    "autoRepay": "true",  
                    "borrowCurrency": "ETH",  
                    "borrowTime": "1752633696068",  
                    "interestPaid": "0.00018082191780822",  
                    "loanId": "570",  
                    "orderId": "13007",  
                    "repayType": "1",  
                    "repaymentTime": "1755225696068",  
                    "residualPenaltyInterest": "0",  
                    "residualPrincipal": "0.1",  
                    "status": 1,  
                    "term": "30"  
                }  
            ],  
            "nextPageCursor": "568"  
        },  
        "retExtInfo": {},  
        "time": 1752652692603  
    }