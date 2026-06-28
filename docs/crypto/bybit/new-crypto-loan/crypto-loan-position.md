---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/new-crypto-loan/crypto-loan-position
api_type: REST
updated_at: 2026-05-27 19:18:41.372140
---

# Create Borrow Order

> Permission: "Spot trade"  
>  UID rate limit: 1 req / second

info

  * The loan funds are released to the Funding wallet.
  * The collateral funds are deducted from the Funding wallet, so make sure you have enough collateral amount in the Funding wallet.



### HTTP Request

POST`/v5/crypto-loan-fixed/borrow`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
orderCurrency| **true**|  string| Currency to borrow  
orderAmount| **true**|  string| Amount to borrow  
annualRate| **true**|  string| Customizable annual interest rate, e.g., `0.02` means 2%  
term| **true**|  string| Fixed term `7`: 7 days; `14`: 14 days; `30`: 30 days; `90`: 90 days; `180`: 180 days  
autoRepay| false| string| Deprecated. Enable Auto-Repay to have assets in your Funding Account automatically repay your loan upon Borrowing order expiration, preventing overdue penalties. Ensure your Funding Account maintains sufficient amount for repayment to avoid automatic repayment failures.  
`"true"`: enable, default; `"false"`: disable  
repayType| false| string| `1`:Auto Repayment (default); Enable "Auto Repayment" to automatically repay your loan using assets in your funding account when it dues, avoiding overdue penalties. `2`:Transfer to flexible loan  
collateralList| false| array<object>| Collateral coin list, supports putting up to 100 currency in the array  
> currency| false| string| Currency used to mortgage  
> amount| false| string| Amount to mortgage  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
orderId| string| Loan order ID  
  
### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    POST /v5/crypto-loan-fixed/borrow HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: XXXXXX  
    X-BAPI-TIMESTAMP: 1752633649752  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
    Content-Length: 208  
      
    {  
        "orderCurrency": "ETH",  
        "orderAmount": "1.5",  
        "annualRate": "0.022",  
        "term": "30",  
        "autoRepay": "true",  
        "collateralList": {  
            "currency": "BTC",  
            "amount": "0.1"  
        }  
    }  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.borrow_fixed_crypto_loan(  
        loanCurrency="ETH",  
        loanAmount="1.5",  
        annualRate="0.022",  
        term="30",  
        autoRepay="true",  
        collateralList={  
            "currency": "BTC",  
            "amount": "0.1",  
        },  
    ))  
    
    
    
      
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "ok",  
        "result": {  
            "orderId": "13007"  
        },  
        "retExtInfo": {},  
        "time": 1752633650147  
    }

---

# 創建借款單

> 權限: "現貨"  
>  頻率: 1次/秒

信息

  * 借款發放到資金帳戶
  * 質押金將從資金帳戶扣減, 因此確保資金帳戶有足額質押幣種



### HTTP 請求

POST`/v5/crypto-loan-fixed/borrow`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
orderCurrency| **true**|  string| 借入幣種  
orderAmount| **true**|  string| 借入金額  
annualRate| **true**|  string| 可自訂年利率，例如 `0.02` 表示 2%  
term| **true**|  string| 固定期限 `7`: 7 天；`14`: 14 天；`30`: 30 天；`90`: 90 天；`180`: 180 天  
autoRepay| false| string| 已廢棄。啟用「自動還款」可在借款訂單到期時，自動使用資金帳戶中的資產還款，以避免逾期罰款。請確保資金帳戶中有足夠金額，以避免自動還款失敗。  
`"true"`：啟用，預設值；`"false"`：停用  
repayType| false| string| `1`:自動還款. (默认值); 啟用「自動還款」可在藉款訂單到期時，自動使用資金帳戶中的資產還款，以避免逾期罰款; `2`:轉活期;  
collateralList| false| array<object>| 抵押幣種清單，最多支持陣列中放入 100 種幣種  
> currency| false| string| 用於抵押的幣種  
> amount| false| string| 抵押金額  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
orderId| string| 借款單ID  
  
### 請求示例

  * HTTP
  * Python
  * Node.js


    
    
    POST /v5/crypto-loan-fixed/borrow HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: XXXXXX  
    X-BAPI-TIMESTAMP: 1752633649752  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
    Content-Length: 208  
      
    {  
        "orderCurrency": "ETH",  
        "orderAmount": "1.5",  
        "annualRate": "0.022",  
        "term": "30",  
        "autoRepay": "true",  
        "collateralList": {  
            "currency": "BTC",  
            "amount": "0.1"  
        }  
    }  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.borrow_fixed_crypto_loan(  
        loanCurrency="ETH",  
        loanAmount="1.5",  
        annualRate="0.022",  
        term="30",  
        autoRepay="true",  
        collateralList={  
            "currency": "BTC",  
            "amount": "0.1",  
        },  
    ))  
    
    
    
      
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "ok",  
        "result": {  
            "orderId": "13007"  
        },  
        "retExtInfo": {},  
        "time": 1752633650147  
    }