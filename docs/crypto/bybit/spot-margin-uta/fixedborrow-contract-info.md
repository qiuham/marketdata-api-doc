---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/spot-margin-uta/fixedborrow-contract-info
api_type: REST
updated_at: 2026-07-08 19:04:06.779900
---

# Get Fixed-Rate Borrow Contract Info

info

  * Results are returned in descending order by `borrowTime`.



### HTTP Request

GET`/v5/spot-margin-trade/fixedborrow-contract-info`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
orderId| false| string| Loan order ID  
orderCurrency| false| string| Loan coin name  
term| false| string| Fixed term. `7`: 7 days; `14`: 14 days; `30`: 30 days; `90`: 90 days; `180`: 180 days  
limit| false| string| Limit for data size per page. [1, 100]. Default: `10`  
cursor| false| string| Cursor. Use the `nextPageCursor` token from the response to retrieve the next page of the result set  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
list| array| Object  
> annualRate| string| Annual rate for the borrowing  
> borrowCurrency| string| Loan coin  
> borrowTime| string| Loan order timestamp  
> interestPaid| string| Paid interest  
> loanId| string| Loan contract ID  
> orderId| string| Loan order ID  
> repaymentTime| string| Time to repay  
> residualPenaltyInterest| string| Unpaid interest  
> residualPrincipal| string| Unpaid principal  
> status| integer| Loan contract status. `1`: Unrepaid; `2`: Fully repaid; `3`: Overdue  
> term| string| Fixed term. `7`: 7 days; `14`: 14 days; `30`: 30 days; `90`: 90 days; `180`: 180 days  
> repayType| string| `1`: Auto Repayment; `2`: Transfer to flexible loan; `0`: No Automatic Repayment (compatible with existing orders)  
> strategyType| string| `PARTIAL`: Allow partial fill; `FULL`: Full fill only  
nextPageCursor| string| Refer to the `cursor` request parameter  
  
* * *

### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/spot-margin-trade/fixedborrow-contract-info?orderCurrency=USDT&limit=10 HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1692696840996  
    X-BAPI-RECV-WINDOW: 5000  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.spot_margin_trade_get_fixed_borrow_contract_info(  
        orderCurrency="USDT",  
        limit="10"  
    ))  
    
    
    
      
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "success",  
        "result": {  
            "list": [  
                {  
                    "annualRate": "1.000000000000000000",  
                    "borrowCurrency": "USDT",  
                    "borrowTime": "1764162490000",  
                    "interestPaid": "1.065753424657534247",  
                    "loanId": "2092341042506646784",  
                    "orderId": "FIXED_BORROW_a17089fc526441faa52eb99b0b9feb69185",  
                    "repaymentTime": "1764288000000",  
                    "residualPenaltyInterest": "0",  
                    "residualPrincipal": "0.000000000000000000",  
                    "status": 3,  
                    "term": "1",  
                    "repayType": "1",  
                    "strategyType": "PARTIAL"  
                },  
                {  
                    "annualRate": "1.000000000000000000",  
                    "borrowCurrency": "USDT",  
                    "borrowTime": "1764149170000",  
                    "interestPaid": "0.030136986301369864",  
                    "loanId": "2092229306860452864",  
                    "orderId": "FIXED_BORROW_a17089fc526441faa52eb99b0b9feb69185",  
                    "repaymentTime": "1764244800000",  
                    "residualPenaltyInterest": "0",  
                    "residualPrincipal": "0.000000000000000000",  
                    "status": 3,  
                    "term": "1",  
                    "repayType": "1",  
                    "strategyType": "PARTIAL"  
                },  
                {  
                    "annualRate": "1.000000000000000000",  
                    "borrowCurrency": "USDT",  
                    "borrowTime": "1764120790000",  
                    "interestPaid": "1.643835616438356165",  
                    "loanId": "2091991237922142464",  
                    "orderId": "FIXED_BORROW_a17089fc526441faa52eb99b0b9feb69185",  
                    "repaymentTime": "1764244800000",  
                    "residualPenaltyInterest": "0",  
                    "residualPrincipal": "0.000000000000000000",  
                    "status": 3,  
                    "term": "1",  
                    "repayType": "1",  
                    "strategyType": "PARTIAL"  
                }  
            ],  
            "nextPageCursor": "0"  
        },  
        "retExtInfo": {},  
        "time": 1775617311081  
    }

---

# 查詢固定利率借款合約信息

信息

  * 結果按 `borrowTime` 時間倒序返回。



### HTTP 請求

GET`/v5/spot-margin-trade/fixedborrow-contract-info`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
orderId| false| string| 借款訂單 ID  
orderCurrency| false| string| 借款幣種  
term| false| string| 借款期限。`7`：7天；`14`：14天；`30`：30天；`90`：90天；`180`：180天  
limit| false| string| 每頁返回數量，[1, 100]，默認：`10`  
cursor| false| string| 翻頁游標，使用上一次響應中的 `nextPageCursor` 獲取下一頁數據  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
list| array| Object  
> annualRate| string| 借款年化利率  
> borrowCurrency| string| 借款幣種  
> borrowTime| string| 借款時間戳  
> interestPaid| string| 已還利息  
> loanId| string| 借款合約 ID  
> orderId| string| 借款訂單 ID  
> repaymentTime| string| 還款時間  
> residualPenaltyInterest| string| 未還利息  
> residualPrincipal| string| 未還本金  
> status| integer| 借款合約狀態。`1`：未還款；`2`：已全部還款；`3`：已逾期  
> term| string| 借款期限。`7`：7天；`14`：14天；`30`：30天；`90`：90天；`180`：180天  
> repayType| string| `1`：自動還款；`2`：轉為活期借款；`0`：不自動還款（兼容舊訂單）  
> strategyType| string| `PARTIAL`：允許部分成交；`FULL`：僅允許全部成交  
nextPageCursor| string| 參考請求參數 `cursor`  
  
* * *

### 請求示例

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/spot-margin-trade/fixedborrow-contract-info?orderCurrency=USDT&limit=10 HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1692696840996  
    X-BAPI-RECV-WINDOW: 5000  
    
    
    
      
    
    
    
      
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "success",  
        "result": {  
            "list": [  
                {  
                    "annualRate": "1.000000000000000000",  
                    "borrowCurrency": "USDT",  
                    "borrowTime": "1764162490000",  
                    "interestPaid": "1.065753424657534247",  
                    "loanId": "2092341042506646784",  
                    "orderId": "FIXED_BORROW_a17089fc526441faa52eb99b0b9feb69185",  
                    "repaymentTime": "1764288000000",  
                    "residualPenaltyInterest": "0",  
                    "residualPrincipal": "0.000000000000000000",  
                    "status": 3,  
                    "term": "1",  
                    "repayType": "1",  
                    "strategyType": "PARTIAL"  
                },  
                {  
                    "annualRate": "1.000000000000000000",  
                    "borrowCurrency": "USDT",  
                    "borrowTime": "1764149170000",  
                    "interestPaid": "0.030136986301369864",  
                    "loanId": "2092229306860452864",  
                    "orderId": "FIXED_BORROW_a17089fc526441faa52eb99b0b9feb69185",  
                    "repaymentTime": "1764244800000",  
                    "residualPenaltyInterest": "0",  
                    "residualPrincipal": "0.000000000000000000",  
                    "status": 3,  
                    "term": "1",  
                    "repayType": "1",  
                    "strategyType": "PARTIAL"  
                },  
                {  
                    "annualRate": "1.000000000000000000",  
                    "borrowCurrency": "USDT",  
                    "borrowTime": "1764120790000",  
                    "interestPaid": "1.643835616438356165",  
                    "loanId": "2091991237922142464",  
                    "orderId": "FIXED_BORROW_a17089fc526441faa52eb99b0b9feb69185",  
                    "repaymentTime": "1764244800000",  
                    "residualPenaltyInterest": "0",  
                    "residualPrincipal": "0.000000000000000000",  
                    "status": 3,  
                    "term": "1",  
                    "repayType": "1",  
                    "strategyType": "PARTIAL"  
                }  
            ],  
            "nextPageCursor": "0"  
        },  
        "retExtInfo": {},  
        "time": 1775617311081  
    }