---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/finance/pwm/asset-manager/create-fund
api_type: REST
updated_at: 2026-10-07 18:49:10.930600
---

# Create Investment Plan

info

  1. Each institution can create a maximum of **10 investment plans**. Each user can hold a maximum of **20 investment plans**.
  2. The fund must be in **`PendingSubscribe`** (pending subscription) status. Otherwise, error code `180040` is returned.



### HTTP Request

POST`/v5/earn/pwm/asset-manager/create-investment-plan`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
accountUid| **true**|  string| Target user UID  
planName| **true**|  string| Investment plan name, max 50 characters  
planType| **true**|  string| Plan type: `stable` / `advanced`  
investmentDistribution| **true**|  array| Fund configuration list. At least 1 fund required  
> productId| **true**|  string| Fund ID (must be a fund under this institution's management)  
> amount| **true**|  string| Configured amount (base coin)  
reqLinkId| **true**|  string| User-defined request ID, max 36 characters, used for idempotency  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
planId| string| Unique identifier of the newly created investment plan  
planType| string| Plan type: `stable` / `advanced`  
accountUid| string| Target user UID  
status| string| Plan status. Fixed as `PendingSubscription` upon creation  
createdTime| string| Creation timestamp (milliseconds)  
  
* * *

### Request Example
    
    
    POST /v5/earn/pwm/asset-manager/create-investment-plan HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1741651200000  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "accountUid": "800001",  
        "planName": "Conservative Growth Plan",  
        "planType": "stable",  
        "investmentDistribution": [  
            {  
                "productId": "12345",  
                "amount": "100000.00"  
            }  
        ],  
        "reqLinkId": "create-plan-001"  
    }  
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "success",  
        "result": {  
            "planId": "10088",  
            "planType": "stable",  
            "accountUid": "800001",  
            "status": "pending_subscribe",  
            "createdTime": "1640000000000"  
        }  
    }

---

# 機構創建投資計劃

信息

  1. 每個機構最多創建 **10 個投資計劃** 。每個用戶最多擁有 **20 個投資計劃** 。
  2. 基金狀態必須為 **`PendingSubscribe`** （待申購），否則返回錯誤碼 `180040`。



### HTTP 請求

POST`/v5/earn/pwm/asset-manager/create-investment-plan`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
accountUid| **true**|  string| 目標用戶UID  
planName| **true**|  string| 投資計劃名稱，最大50字符  
planType| **true**|  string| 計劃類型：`stable`（穩健增值）/ `advanced`（進階收益）  
investmentDistribution| **true**|  array| 基金配置列表，至少包含1個基金  
> productId| **true**|  string| 基金ID（必須是該機構管轄的基金）  
> amount| **true**|  string| 配置金額（本位幣）  
reqLinkId| **true**|  string| 用戶自定義請求ID，最長36字符，用於冪等  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
planId| string| 新創建的投資計劃唯一標識  
planType| string| 計劃類型：`stable` / `advanced`  
accountUid| string| 目標用戶UID  
status| string| 計劃狀態，創建後固定為 `PendingSubscription`  
createdTime| string| 創建時間戳（毫秒）  
  
* * *

### 請求示例
    
    
    POST /v5/earn/pwm/asset-manager/create-investment-plan HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1741651200000  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "accountUid": "800001",  
        "planName": "Conservative Growth Plan",  
        "planType": "stable",  
        "investmentDistribution": [  
            {  
                "productId": "12345",  
                "amount": "100000.00"  
            }  
        ],  
        "reqLinkId": "create-plan-001"  
    }  
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "success",  
        "result": {  
            "planId": "10088",  
            "planType": "stable",  
            "accountUid": "800001",  
            "status": "pending_subscribe",  
            "createdTime": "1640000000000"  
        }  
    }