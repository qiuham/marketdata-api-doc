---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/finance/pwm/asset-manager/manage-investment-plan
api_type: REST
updated_at: 2026-06-29 19:29:10.933356
---

# Manage Investment Plan

info

  1. Fund configuration (`updateFunds`) can only be modified when the plan is in **`Init`** , **`PendingSubscription`** , or **`Active`** status.
  2. Plans in **`Deleted`** or **`Closed`** status do not allow adding new funds.
  3. Any fund being added or updated must be in **`PendingSubscribe`** (pending subscription) status.



### HTTP Request

POST`/v5/earn/pwm/asset-manager/manage-investment-plan`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
planId| **true**|  string| Investment plan ID  
updateStatus| false| string| Update plan status. Options: `Closed` / `Deleted`. Status is unchanged if omitted  
updateFunds| false| array| Fund list to update. If a matching `fundId` exists, the amount is updated; otherwise a new fund is added. Max 10 entries. Returns an error if duplicate `fundId` entries are present  
> fundId| **true**|  string| Fund ID  
> amount| **true**|  string| Configured amount (base coin)  
reqLinkId| **true**|  string| User-defined request ID, max 36 characters, used for idempotency  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
planId| string| Investment plan ID  
status| string| Current plan status: `PendingSubscription` / `Active` / `Closed` / `Deleted`  
updatedTime| string| Status update timestamp (milliseconds)  
updateFunds| array| Fund configuration bound to the investment plan after the update  
> fundId| string| Fund ID  
> amount| string| Configured amount (base coin)  
  
* * *

### Request Example
    
    
    POST /v5/earn/pwm/asset-manager/manage-investment-plan HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1741651200000  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "planId": "10088",  
        "updateStatus": "Closed",  
        "updateFunds": [  
            {  
                "fundId": "430",  
                "amount": "100000"  
            },  
            {  
                "fundId": "2005",  
                "amount": "270000"  
            }  
        ],  
        "reqLinkId": "manage-plan-001"  
    }  
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "success",  
        "result": {  
            "planId": "10088",  
            "status": "Closed",  
            "updateFunds": [  
                {  
                    "fundId": "430",  
                    "amount": "100000"  
                },  
                {  
                    "fundId": "2005",  
                    "amount": "270000"  
                }  
            ],  
            "updatedTime": "1701700000000"  
        }  
    }

---

# 編輯投資計劃狀態和基金配置

信息

  1. 僅在投資計劃狀態為 **`Init`** 、**`PendingSubscription`** 或 **`Active`** 時，才能修改基金配置（`updateFunds`）。
  2. 狀態為 **`Deleted`** 或 **`Closed`** 的投資計劃不允許添加基金。
  3. 添加或更新的基金必須處於 **`PendingSubscribe`** （待申購）狀態。



### HTTP 請求

POST`/v5/earn/pwm/asset-manager/manage-investment-plan`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
planId| **true**|  string| 投資計劃ID  
updateStatus| false| string| 更新投資計劃狀態，可選值：`Closed` / `Deleted`，不傳則不修改狀態  
updateFunds| false| array| 更新的基金列表。若有對應 `fundId` 則更新 amount；若沒有則添加新基金。最多10條，若包含重複 `fundId` 直接報錯  
> fundId| **true**|  string| 基金ID  
> amount| **true**|  string| 配置金額（本位幣）  
reqLinkId| **true**|  string| 用戶自定義請求ID，最長36字符，用於防重  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
planId| string| 投資計劃ID  
status| string| 當前計劃狀態：`PendingSubscription`（待申購）/ `Active`（運行中）/ `Closed`（已關閉）/ `Deleted`（已刪除）  
updatedTime| string| 狀態更新時間戳（毫秒）  
updateFunds| array| 更新後投資計劃綁定的基金信息  
> fundId| string| 基金ID  
> amount| string| 配置金額（本位幣）  
  
* * *

### 請求示例
    
    
    POST /v5/earn/pwm/asset-manager/manage-investment-plan HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1741651200000  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "planId": "10088",  
        "updateStatus": "Closed",  
        "updateFunds": [  
            {  
                "fundId": "430",  
                "amount": "100000"  
            },  
            {  
                "fundId": "2005",  
                "amount": "270000"  
            }  
        ],  
        "reqLinkId": "manage-plan-001"  
    }  
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "success",  
        "result": {  
            "planId": "10088",  
            "status": "Closed",  
            "updateFunds": [  
                {  
                    "fundId": "430",  
                    "amount": "100000"  
                },  
                {  
                    "fundId": "2005",  
                    "amount": "270000"  
                }  
            ],  
            "updatedTime": "1701700000000"  
        }  
    }