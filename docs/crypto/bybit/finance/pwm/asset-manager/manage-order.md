---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/finance/pwm/asset-manager/manage-order
api_type: REST
updated_at: 2026-05-27 19:17:49.962567
---

# Manage Order

### HTTP Request

POST`/v5/earn/pwm/asset-manager/manage-order`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
orderId| **true**|  string| Order ID. Must be in `Pending Review` status  
action| **true**|  string| Action to perform: `approve` / `reject`  
reqLinkId| **true**|  string| User-defined request ID, max 36 characters, used for idempotency  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
orderId| string| Order ID  
fundId| string| Fund ID  
accountUid| string| Fund main account UID  
orderStatus| string| Current order status: `PendingReview` / `Pass` / `Rejected` / `Processing` / `Success` / `Failed`. After approval or rejection, the execution status can be queried using the same `reqLinkId`  
orderType| string| Order type: `Subscribe` / `Redeem`  
action| string| Action performed: `approve` / `reject`  
coin| string| Coin  
amount| string| Order amount (base coin). Subscription orders only; empty for redemption orders  
shares| string| Order shares. Redemption orders only; empty for subscription orders  
updatedTime| string| Order update timestamp (milliseconds)  
  
* * *

### Request Example
    
    
    POST /v5/earn/pwm/asset-manager/manage-order HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1741651200000  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "orderId": "500002",  
        "action": "approve",  
        "reqLinkId": "manage-order-001"  
    }  
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "success",  
        "result": {  
            "orderId": "500002",  
            "fundId": "100001",  
            "accountUid": "800001",  
            "orderStatus": "PendingReview",  
            "orderType": "Subscribe",  
            "action": "Approve",  
            "coin": "BTC",  
            "amount": "10.00000000",  
            "shares": "",  
            "updatedTime": "1700100000000"  
        }  
    }

---

# 處理申購/贖回訂單

### HTTP 請求

POST`/v5/earn/pwm/asset-manager/manage-order`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
orderId| **true**|  string| 訂單ID，須為 `Pending Review` 狀態  
action| **true**|  string| 處理動作：`approve`（批准）/ `reject`（拒絕）  
reqLinkId| **true**|  string| 用戶自定義請求ID，最長36字符，用於冪等  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
orderId| string| 訂單ID  
fundId| string| 基金ID  
accountUid| string| 基金主賬戶UID  
orderStatus| string| 當前訂單狀態：`PendingReview`（待審核）/ `Pass`（審核通過）/ `Rejected`（審核拒絕）/ `Processing`（處理中）/ `Success`（成功）/ `Failed`（失敗）。審批通過或拒絕後可以通過同一個 `reqLinkId` 查詢當前訂單的執行狀態  
orderType| string| 訂單類型：`Subscribe`（申購）/ `Redeem`（贖回）  
action| string| 執行的處理動作：`approve` / `reject`  
coin| string| 幣種  
amount| string| 訂單金額（本位幣），僅申購訂單有值，贖回訂單為空  
shares| string| 訂單份額，僅贖回訂單有值，申購訂單為空  
updatedTime| string| 訂單更新時間戳（毫秒）  
  
* * *

### 請求示例
    
    
    POST /v5/earn/pwm/asset-manager/manage-order HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1741651200000  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "orderId": "500002",  
        "action": "approve",  
        "reqLinkId": "manage-order-001"  
    }  
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "success",  
        "result": {  
            "orderId": "500002",  
            "fundId": "100001",  
            "accountUid": "800001",  
            "orderStatus": "PendingReview",  
            "orderType": "Subscribe",  
            "action": "Approve",  
            "coin": "BTC",  
            "amount": "10.00000000",  
            "shares": "",  
            "updatedTime": "1700100000000"  
        }  
    }