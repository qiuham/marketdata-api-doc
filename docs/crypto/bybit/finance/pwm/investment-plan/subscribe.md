---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/finance/pwm/investment-plan/subscribe
api_type: REST
updated_at: 2026-11-13 19:23:35.326079
---

# Subscribe Investment Plan

### HTTP Request

POST`/v5/earn/pwm/investment-plan/subscribe`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
planId| **true**|  string| Investment plan ID. Must be in `PendingSubscription` status  
accountType| false| string| Source account type. Default: `FUND`  
orderLinkId| **true**|  string| User-defined order ID, max 36 characters, used for idempotency  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
planId| string| Investment plan ID  
status| string| Plan status after subscription. Changes to `Active` upon first successful subscription  
orderLinkId| string| User-defined order ID  
  
* * *

### Request Example
    
    
    POST /v5/earn/pwm/investment-plan/subscribe HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1741651200000  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "planId": "10001",  
        "accountType": "FUND",  
        "orderLinkId": "xxx"  
    }  
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "result": {  
            "planId": "10001",  
            "status": "Active",  
            "orderLinkId": "xxx"  
        }  
    }

---

# 一鍵申購

### HTTP 請求

POST`/v5/earn/pwm/investment-plan/subscribe`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
planId| **true**|  string| 投資計劃ID，須為 `PendingSubscription` 狀態  
accountType| false| string| 資金來源賬戶類型，默認 `FUND`  
orderLinkId| **true**|  string| 用戶自定義訂單ID，最長36字符，用於防重  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
planId| string| 投資計劃ID  
status| string| 申購後計劃狀態，首次申購成功後變為 `Active`  
orderLinkId| string| 用戶自定義訂單ID  
  
* * *

### 請求示例
    
    
    POST /v5/earn/pwm/investment-plan/subscribe HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1741651200000  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "planId": "10001",  
        "accountType": "FUND",  
        "orderLinkId": "xxx"  
    }  
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "result": {  
            "planId": "10001",  
            "status": "Active",  
            "orderLinkId": "xxx"  
        }  
    }