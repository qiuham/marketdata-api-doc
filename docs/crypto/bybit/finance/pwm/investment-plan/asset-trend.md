---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/finance/pwm/investment-plan/asset-trend
api_type: REST
updated_at: 2026-07-05 19:08:58.749781
---

# Claim Withdrawable Funds

### HTTP Request

POST`/v5/earn/pwm/investment-plan/claim`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
planId| **true**|  string| Investment plan ID. Must be in `Active` status  
toAccountType| false| string| Target account type. Default: `FUND`  
orderLinkId| **true**|  string| User-defined order ID, max 36 characters, used for idempotency  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
planId| string| Investment plan ID  
toAccountType| int| Target account type for the transfer  
status| string| Claim status: `Success` / `processing`  
createdTime| string| Claim timestamp (milliseconds)  
  
* * *

### Request Example
    
    
    POST /v5/earn/pwm/investment-plan/claim HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1741651200000  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "planId": "10001",  
        "toAccountType": "FUND",  
        "orderLinkId": "claim-order-001"  
    }  
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "result": {  
            "planId": "10001",  
            "toAccountType": 6,  
            "status": "Success",  
            "createdTime": "1701400000000"  
        }  
    }

---

# 領取可提取資金

### HTTP 請求

POST`/v5/earn/pwm/investment-plan/claim`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
planId| **true**|  string| 投資計劃ID，須為 `Active` 狀態  
toAccountType| false| string| 目標賬戶類型，默認 `FUND`  
orderLinkId| **true**|  string| 用戶自定義訂單ID，最長36字符，用於防重  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
planId| string| 投資計劃ID  
toAccountType| int| 到賬目標賬戶類型  
status| string| 提取狀態：`Success`（成功）/ `processing`（處理中）  
createdTime| string| 提取時間戳（毫秒）  
  
* * *

### 請求示例
    
    
    POST /v5/earn/pwm/investment-plan/claim HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1741651200000  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "planId": "10001",  
        "toAccountType": "FUND",  
        "orderLinkId": "claim-order-001"  
    }  
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "result": {  
            "planId": "10001",  
            "toAccountType": 6,  
            "status": "Success",  
            "createdTime": "1701400000000"  
        }  
    }