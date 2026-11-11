---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/finance/pwm/investment-plan/fund-nav
api_type: REST
updated_at: 2026-11-11 14:01:06.426354
---

# Invest More

### HTTP Request

POST`/v5/earn/pwm/investment-plan/invest-more`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
planId| **true**|  string| Investment plan ID. Must be in `Active` status  
accountType| false| string| Source account type. Default: `FUND`  
category| **true**|  string| Product type  
productId| **true**|  string| Product ID  
amount| **true**|  string| Additional investment amount (base coin)  
orderLinkId| **true**|  string| User-defined order ID, max 36 characters, used for idempotency  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
planId| string| Investment plan ID  
category| string| Product type  
productId| string| Product ID  
coin| string| Subscription coin  
amount| string| Additional investment amount (base coin)  
status| string| Subscription status: `Success` / `Pending` / `failed`  
orderLinkId| string| User-defined order ID  
orderId| string| System-generated order ID  
  
* * *

### Request Example
    
    
    POST /v5/earn/pwm/investment-plan/invest-more HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1741651200000  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "planId": "10001",  
        "accountType": "FUND",  
        "category": "equityFund",  
        "productId": "2001",  
        "amount": "20000.00",  
        "orderLinkId": "xxx"  
    }  
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "result": {  
            "planId": "10001",  
            "category": "equityFund",  
            "productId": "2001",  
            "coin": "USDT",  
            "amount": "20000.00",  
            "status": "Pending",  
            "orderId": "ORD20241115002",  
            "orderLinkId": "xxx"  
        }  
    }

---

# 追加申購

### HTTP 請求

POST`/v5/earn/pwm/investment-plan/invest-more`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
planId| **true**|  string| 投資計劃ID，須為 `Active` 狀態  
accountType| false| string| 資金來源賬戶類型，默認 `FUND`  
category| **true**|  string| 產品類型  
productId| **true**|  string| 產品ID  
amount| **true**|  string| 追加金額（本位幣）  
orderLinkId| **true**|  string| 用戶自定義訂單ID，最長36字符，用於防重  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
planId| string| 投資計劃ID  
category| string| 產品類型  
productId| string| 產品ID  
coin| string| 申購幣種  
amount| string| 追加金額（本位幣）  
status| string| 申購狀態：`Success` / `Pending` / `failed`  
orderLinkId| string| 用戶自定義訂單ID  
orderId| string| 系統生成的訂單ID  
  
* * *

### 請求示例
    
    
    POST /v5/earn/pwm/investment-plan/invest-more HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1741651200000  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "planId": "10001",  
        "accountType": "FUND",  
        "category": "equityFund",  
        "productId": "2001",  
        "amount": "20000.00",  
        "orderLinkId": "xxx"  
    }  
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "result": {  
            "planId": "10001",  
            "category": "equityFund",  
            "productId": "2001",  
            "coin": "USDT",  
            "amount": "20000.00",  
            "status": "Pending",  
            "orderId": "ORD20241115002",  
            "orderLinkId": "xxx"  
        }  
    }