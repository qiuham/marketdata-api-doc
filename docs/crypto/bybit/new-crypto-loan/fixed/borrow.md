---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/new-crypto-loan/fixed/borrow
api_type: REST
updated_at: 2026-09-22 18:46:37.056175
---

# Get Borrowing Market

info

Does not need authentication.

If you want to borrow, you can use this endpoint to check whether there are any suitable counterparty supply orders available.

### HTTP Request

GET`/v5/crypto-loan-fixed/borrow-order-quote`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
orderCurrency| **true**|  string| Coin name  
orderBy| **true**|  string| Order by, `apy`: annual rate; `term`; `quantity`  
term| false| string| Fixed term `7`: 7 days; `14`: 14 days; `30`: 30 days; `90`: 90 days; `180`: 180 days  
sort| false| integer| `0`: ascend, default; `1`: descend  
limit| false| integer| Limit for data size per page. [`1`, `100`]. Default: `10`  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
list| array| Object  
> orderCurrency| string| Coin name  
> term| integer| Fixed term `7`: 7 days; `14`: 14 days; `30`: 30 days; `90`: 90 days; `180`: 180 days  
> annualRate| string| Annual rate  
> qty| string| Quantity  
  
### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/crypto-loan-fixed/borrow-order-quote?orderCurrency=USDT&orderBy=apy HTTP/1.1  
    Host: api-testnet.bybit.com  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.get_borrowing_market_fixed_crypto_loan(  
        orderCurrency="USDT",  
        orderBy="apy",  
    ))  
    
    
    
      
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "ok",  
        "result": {  
            "list": [  
                {  
                    "annualRate": "0.04",  
                    "orderCurrency": "USDT",  
                    "qty": "988.78",  
                    "term": 14  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1752719158890  
    }

---

# 查詢可借市場

信息

公共接口, 無需鑒權

如果您是借款方, 可通過該接口查詢到市場上可匹配的存款單報價

### HTTP 請求

GET`/v5/crypto-loan-fixed/borrow-order-quote`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
orderCurrency| **true**|  string| 幣種名稱  
term| false| string| 固定期限 `7`: 7 天；`14`: 14 天；`30`: 30 天；`90`: 90 天；`180`: 180 天  
orderBy| **true**|  string| 排序依據，`apy`: 年化利率；`term`: 期限；`quantity`: 數量  
sort| false| integer| `0`: 升序，預設；`1`: 降序  
limit| false| string| 每頁數量限制. [`1`, `100`]. 默認: `10`  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
list| array| Object  
> orderCurrency| string| 幣種名稱  
> term| integer| 固定期限 `7`: 7 天；`14`: 14 天；`30`: 30 天；`90`: 90 天；`180`: 180 天  
> annualRate| string| 年化利率  
> qty| string| 數量  
  
### 請求示例

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/crypto-loan-fixed/borrow-order-quote?orderCurrency=USDT&orderBy=apy HTTP/1.1  
    Host: api-testnet.bybit.com  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.get_borrowing_market_fixed_crypto_loan(  
        orderCurrency="USDT",  
        orderBy="apy",  
    ))  
    
    
    
      
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "ok",  
        "result": {  
            "list": [  
                {  
                    "annualRate": "0.04",  
                    "orderCurrency": "USDT",  
                    "qty": "988.78",  
                    "term": 14  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1752719158890  
    }