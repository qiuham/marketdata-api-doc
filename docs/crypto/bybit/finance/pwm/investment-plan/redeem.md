---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/finance/pwm/investment-plan/redeem
api_type: REST
updated_at: 2026-05-27 19:18:06.075466
---

# Get Fund Transfer Records

info

This endpoint must be called using the API key of the fund custodian sub-account.

### HTTP Request

GET`/v5/earn/pwm/query-fund-transfer-result`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
transferId| false| string| Transfer request ID. If omitted, returns up to the 20 most recent non-terminal transfer records within the past month. Records older than one month may have been archived  
fromUserId| false| int64| Source UID  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
transferId| string| Transfer ID  
status| string| Transfer status: `SUCCESS` / `FAILED` / `PROCESSING`  
fromUserId| int64| Source UID  
toUserId| int64| Destination UID  
amount| string| Transfer amount  
coin| string| Coin  
  
* * *

### Request Example
    
    
    GET /v5/earn/pwm/query-fund-transfer-result?transferId=4fdf-re-4343-frewr HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1741651200000  
    X-BAPI-RECV-WINDOW: 5000  
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "success",  
        "result": {  
            "transferId": "4fdf-re-4343-frewr",  
            "status": "SUCCESS",  
            "fromUserId": 1237488,  
            "toUserId": 1237489,  
            "amount": "12.3456",  
            "coin": "USDT"  
        }  
    }

---

# 查詢劃轉流水

信息

此接口必須使用基金托管子賬號的 API Key 操作。

### HTTP 請求

GET`/v5/earn/pwm/query-fund-transfer-result`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
transferId| false| string| 劃轉請求ID。不傳默認返回最近20條（一個月內）未到終態的劃轉記錄，超過時間的記錄可能已歸檔  
fromUserId| false| int64| 資金劃出UID  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
transferId| string| 劃轉ID  
status| string| 劃轉狀態：`SUCCESS`（劃轉成功）/ `FAILED`（劃轉失敗）/ `PROCESSING`（劃轉中）  
fromUserId| int64| 資金劃出UID  
toUserId| int64| 資金劃入UID  
amount| string| 劃轉金額  
coin| string| 幣種  
  
* * *

### 請求示例
    
    
    GET /v5/earn/pwm/query-fund-transfer-result?transferId=4fdf-re-4343-frewr HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1741651200000  
    X-BAPI-RECV-WINDOW: 5000  
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "success",  
        "result": {  
            "transferId": "4fdf-re-4343-frewr",  
            "status": "SUCCESS",  
            "fromUserId": 1237488,  
            "toUserId": 1237489,  
            "amount": "12.3456",  
            "coin": "USDT"  
        }  
    }