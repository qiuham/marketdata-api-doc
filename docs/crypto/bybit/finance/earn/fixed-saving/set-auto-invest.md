---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/finance/earn/fixed-saving/set-auto-invest
api_type: REST
updated_at: 2026-11-13 19:23:19.060577
---

# Set Auto-Invest

API ker permission: `Earn`  
API rate limit: 5 reqs / sec

info

  * Auto-invest can only be enabled on products where `allowAutoReinvest` is `true`.
  * The position must be active and not undergoing early redemption processing.



### HTTP Request

POST`/v5/earn/fixed-term/position/auto-invest`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
productId| **true**|  string| Product ID  
category| **true**|  string| Product sub-type: `FixedTermSaving`, `FundPool`, `FundPoolPremium`  
positionId| **true**|  string| Position ID  
status| **true**|  string| Auto-invest setting: `Enable` or `Disable`  
  
### Response Parameters

None

* * *

### Request Example
    
    
    POST /v5/earn/fixed-term/position/auto-invest HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1741651200000  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "productId": "23",  
        "category": "FundPool",  
        "positionId": "19454",  
        "status": "Enable"  
    }  
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "",  
        "result": {},  
        "retExtInfo": {},  
        "time": 1776075584538  
    }

---

# 設定自動續投

API key權限：`Earn`  
API 頻率限制：每秒5次

信息

  * 自動續投只能在 `allowAutoReinvest` 為 `true` 的產品上啟用。
  * 持倉必須為活躍狀態且未進行提前贖回處理。



### HTTP 請求

POST`/v5/earn/fixed-term/position/auto-invest`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
productId| **true**|  string| 產品ID  
category| **true**|  string| 產品子類型：`FixedTermSaving`、`FundPool`、`FundPoolPremium`  
positionId| **true**|  string| 持倉ID  
status| **true**|  string| 自動續投設置：`Enable` 或 `Disable`  
  
### 響應參數

無

* * *

### 請求示例
    
    
    POST /v5/earn/fixed-term/position/auto-invest HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1741651200000  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "productId": "23",  
        "category": "FundPool",  
        "positionId": "19454",  
        "status": "Enable"  
    }  
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "",  
        "result": {},  
        "retExtInfo": {},  
        "time": 1776075584538  
    }