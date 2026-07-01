---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/finance/advanced-earn/smart-lvg/position
api_type: REST
updated_at: 2026-07-01 19:28:22.795922
---

# Get Product Quote

info

Does not need authentication. **Up to 50 requests** per second per IP.

### HTTP Request

GET`/v5/earn/advance/product-extra-info`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
category| **true**|  string| Product category. `SmartLeverage`  
productId| **true**|  string| Product ID  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
category| string| `SmartLeverage`  
productId| string| Product ID  
breakevenPrice| string| Breakeven price — the best available institutional quote. Empty if no active quote  
currentPrice| string| Current market price of the underlying asset. Used as reference for `initialPrice`  
expireAt| string| Quote expiry time, Unix timestamp in ms. Empty if no active quote  
maxInvestmentAmount| string| Maximum single order amount at current quote. Empty if no active quote  
  
note

`breakevenPrice`, `expireAt`, and `maxInvestmentAmount` may be empty when no institutional quote is available. `currentPrice` is sourced directly from the market feed and is always present.

### Request Example
    
    
    GET /v5/earn/advance/product-extra-info?category=SmartLeverage&productId=12999 HTTP/1.1  
    Host: api-testnet.bybit.com  
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "",  
        "result": {  
            "productId": "12999",  
            "breakevenPrice": "68650.62",  
            "expireAt": "1775036984839",  
            "maxInvestmentAmount": "1000",  
            "currentPrice": "68403.67",  
            "category": "SmartLeverage"  
        },  
        "retExtInfo": {},  
        "time": 1775036429311  
    }

---

# 查詢產品報價

信息

無需身份驗證。每個 IP 每秒**最多 50 次請求** 。

### HTTP 請求

GET`/v5/earn/advance/product-extra-info`

### 請求參數

參數| 必填| 類型| 說明  
---|---|---|---  
category| **true**|  string| 產品類別，`SmartLeverage`  
productId| **true**|  string| 產品 ID  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
category| string| `SmartLeverage`  
productId| string| 產品 ID  
breakevenPrice| string| 損益平衡價格——最優機構報價。若無有效報價則為空  
currentPrice| string| 標的資產的當前市場價格。用作 `initialPrice` 的參考  
expireAt| string| 報價到期時間，毫秒級 Unix 時間戳。若無有效報價則為空  
maxInvestmentAmount| string| 當前報價下的最大單筆訂單金額。若無有效報價則為空  
  
備註

當無機構報價時，`breakevenPrice`、`expireAt` 和 `maxInvestmentAmount` 可能為空。`currentPrice` 直接來自市場行情，始終存在。

### 請求示例
    
    
    GET /v5/earn/advance/product-extra-info?category=SmartLeverage&productId=12999 HTTP/1.1  
    Host: api-testnet.bybit.com  
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "",  
        "result": {  
            "productId": "12999",  
            "breakevenPrice": "68650.62",  
            "expireAt": "1775036984839",  
            "maxInvestmentAmount": "1000",  
            "currentPrice": "68403.67",  
            "category": "SmartLeverage"  
        },  
        "retExtInfo": {},  
        "time": 1775036429311  
    }