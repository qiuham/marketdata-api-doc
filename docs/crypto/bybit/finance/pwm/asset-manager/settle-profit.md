---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/finance/pwm/asset-manager/settle-profit
api_type: REST
updated_at: 2026-06-28 19:11:39.730635
---

# Fund Transfer Between Sub-Accounts

info

This endpoint must be called using the API key of the fund custodian sub-account.

### HTTP Request

POST`/v5/earn/pwm/fund-transfer`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
transferId| **true**|  string| Transfer request ID  
fromUserId| **true**|  int64| Source UID. Must be a custodian sub-account of the current fund  
toUserId| **true**|  int64| Destination UID. Must be a custodian sub-account of the current fund  
amount| **true**|  string| Transfer amount  
coin| **true**|  string| Coin name  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
transferId| string| Transfer ID  
status| string| Transfer status: `SUCCESS` / `FAILED` / `PROCESSING`  
  
* * *

### Request Example
    
    
    POST /v5/earn/pwm/fund-transfer HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1741651200000  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "transferId": "4fdf-re-4343-frewr",  
        "fromUserId": 800001,  
        "toUserId": 800002,  
        "amount": "1.00",  
        "coin": "BTC"  
    }  
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "success",  
        "result": {  
            "transferId": "4fdf-re-4343-frewr",  
            "status": "SUCCESS"  
        }  
    }

---

# 基金托管子賬號間資金劃轉

信息

此接口必須使用基金托管子賬號的 API Key 操作。

### HTTP 請求

POST`/v5/earn/pwm/fund-transfer`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
transferId| **true**|  string| 劃轉請求ID  
fromUserId| **true**|  int64| 資金劃出UID（必須是當前基金的基金托管賬號）  
toUserId| **true**|  int64| 資金劃入UID（必須是當前基金的基金托管賬號）  
amount| **true**|  string| 劃轉金額  
coin| **true**|  string| 幣種名稱  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
transferId| string| 劃轉ID  
status| string| 劃轉狀態：`SUCCESS`（劃轉成功）/ `FAILED`（劃轉失敗）/ `PROCESSING`（劃轉中）  
  
* * *

### 請求示例
    
    
    POST /v5/earn/pwm/fund-transfer HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1741651200000  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "transferId": "4fdf-re-4343-frewr",  
        "fromUserId": 800001,  
        "toUserId": 800002,  
        "amount": "1.00",  
        "coin": "BTC"  
    }  
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "success",  
        "result": {  
            "transferId": "4fdf-re-4343-frewr",  
            "status": "SUCCESS"  
        }  
    }