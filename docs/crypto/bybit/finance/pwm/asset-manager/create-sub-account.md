---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/finance/pwm/asset-manager/create-sub-account
api_type: REST
updated_at: 2026-10-08 18:48:28.393771
---

# Settle Fund Profit

info

This endpoint only applies to funds in **Active** status. Calling it on a **Closed** fund will return error code `180040`.

### HTTP Request

POST`/v5/earn/pwm/asset-manager/settle-profit`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
fundId| **true**|  string| Fund ID  
reqLinkId| **true**|  string| User-defined request ID, max 36 characters, used for idempotency  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
fundId| string| Fund ID  
status| string| Profit settlement status: `Processing` / `Completed` / `Failed`. After execution, the status of the current order can be queried using the same `reqLinkId`  
totalProfitShared| string| Total profit sharing amount settled in this round (base coin)  
instIncome| string| Institution income in this round (base coin)  
coin| string| Fund denomination coin  
createdTime| string| Settlement timestamp (milliseconds)  
  
* * *

### Request Example
    
    
    POST /v5/earn/pwm/asset-manager/settle-profit HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1741651200000  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "fundId": "12323",  
        "reqLinkId": "settle-001"  
    }  
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "success",  
        "result": {  
            "fundId": "12323",  
            "status": "Processing",  
            "totalProfitShared": "2.73",  
            "instIncome": "1.5",  
            "coin": "BTC",  
            "createdTime": "1700000000000"  
        }  
    }

---

# 執行指定基金的分潤

信息

僅對 **Active（運行中）** 狀態的基金有效。對 **Closed（已關閉）** 狀態的基金調用將返回 error code `180040`。

### HTTP 請求

POST`/v5/earn/pwm/asset-manager/settle-profit`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
fundId| **true**|  string| 基金ID  
reqLinkId| **true**|  string| 用戶自定義請求ID，最長36字符，用於冪等  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
fundId| string| 基金ID  
status| string| 分潤狀態：`Processing`（分潤處理中）/ `Completed`（分潤完成）/ `Failed`（分潤失敗）。執行分潤後可以通過同一個 `reqLinkId` 查詢當前訂單的執行狀態  
totalProfitShared| string| 本次利潤分成結算總額（本位幣）  
instIncome| string| 機構本次收入（本位幣）  
coin| string| 基金計價幣種  
createdTime| string| 結算時間戳（毫秒）  
  
* * *

### 請求示例
    
    
    POST /v5/earn/pwm/asset-manager/settle-profit HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1741651200000  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "fundId": "12323",  
        "reqLinkId": "settle-001"  
    }  
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "success",  
        "result": {  
            "fundId": "12323",  
            "status": "Processing",  
            "totalProfitShared": "2.73",  
            "instIncome": "1.5",  
            "coin": "BTC",  
            "createdTime": "1700000000000"  
        }  
    }