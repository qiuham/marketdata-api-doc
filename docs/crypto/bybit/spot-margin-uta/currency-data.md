---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/spot-margin-uta/currency-data
api_type: REST
updated_at: 2026-07-11 18:50:25.888374
---

# Fixed-Rate Borrow

### HTTP Request

POST`/v5/spot-margin-trade/fixedborrow`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
orderCurrency| **true**|  string| Currency to borrow  
orderAmount| **true**|  string| Amount to borrow  
annualRate| **true**|  string| Customizable annual interest rate, e.g., `0.02` means 2%  
term| **true**|  string| Fixed term. `7`: 7 days; `14`: 14 days; `30`: 30 days; `90`: 90 days; `180`: 180 days  
repayType| false| string| `1`: Auto Repayment (default). Enable "Auto Repayment" to automatically repay your loan using assets in your UTA account when it is due, avoiding overdue penalties. `2`: Transfer to flexible loan  
strategyType| false| string| Fill strategy. `PARTIAL`: Allow partial fill (default); `FULL`: Full fill only. Must be uppercase; any other value is rejected  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
orderId| string| Loan order ID  
  
* * *

### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    POST /v5/spot-margin-trade/fixedborrow HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1692696840996  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "orderCurrency": "BTC",  
        "orderAmount": "0.01",  
        "annualRate": "0.02",  
        "term": "30"  
    }  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.spot_margin_trade_fixed_borrow(  
        orderCurrency="BTC",  
        orderAmount="0.01",  
        annualRate="0.02",  
        term="30"  
    ))  
    
    
    
      
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "success",  
        "result": {  
            "orderId": "FIXED_BORROW_4563567182f746ec9f73e4357264d8c7187"  
        },  
        "retExtInfo": {},  
        "time": 1775616124837  
    }

---

# 固定利率借款

### HTTP 請求

POST`/v5/spot-margin-trade/fixedborrow`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
orderCurrency| **true**|  string| 借款幣種  
orderAmount| **true**|  string| 借款金額  
annualRate| **true**|  string| 自定義年化利率，例如 `0.02` 表示 2%  
term| **true**|  string| 借款期限。`7`：7天；`14`：14天；`30`：30天；`90`：90天；`180`：180天  
repayType| false| string| `1`：自動還款（默認）。開啟「自動還款」後，借款到期時將自動使用 UTA 帳戶資產還款，避免逾期罰息。`2`：轉為活期借款  
strategyType| false| string| 成交策略。`PARTIAL`：允許部分成交（默認）；`FULL`：僅全額成交。必須大寫，其他值均會被拒絕  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
orderId| string| 借款訂單 ID  
  
* * *

### 請求示例

  * HTTP
  * Python
  * Node.js


    
    
    POST /v5/spot-margin-trade/fixedborrow HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1692696840996  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "orderCurrency": "BTC",  
        "orderAmount": "0.01",  
        "annualRate": "0.02",  
        "term": "30"  
    }  
    
    
    
      
    
    
    
      
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "success",  
        "result": {  
            "orderId": "FIXED_BORROW_4563567182f746ec9f73e4357264d8c7187"  
        },  
        "retExtInfo": {},  
        "time": 1775616124837  
    }