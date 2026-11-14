---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/spot-margin-uta/get-trade-auto-repay
api_type: REST
updated_at: 2026-11-13 19:25:13.694537
---

# Get Trade Auto Repay

Retrieve the authenticated Unified account's trade auto repayment switch.

info

This saved setting applies only to Cross and Portfolio margin modes. It has no effect in Isolated mode. It is separate from the scheduled automatic repayment settings returned by [Get Auto Repay Mode](/docs/v5/spot-margin-uta/get-auto-repay-mode).

### HTTP Request

GET`/v5/spot-margin-trade/get-trade-auto-repay`

### Request Parameters

None.

* * *

### Response Parameters

Parameter| Type| Comments  
---|---|---  
autoRepay| string| Saved switch state. `1`: enabled; `0`: disabled.  
  
### Request Example

  * HTTP


    
    
    GET /v5/spot-margin-trade/get-trade-auto-repay HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1792117143000  
    X-BAPI-RECV-WINDOW: 5000  
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "success",  
        "result": {  
            "autoRepay": "1"  
        },  
        "retExtInfo": {},  
        "time": 1792117143000  
    }

---

# 查詢交易自動還款開關

查詢已驗證統一帳戶的交易自動還款開關。

信息

此保存的設定僅適用於全倉和組合保證金模式，在逐倉模式下不生效。此開關與 [查詢現貨自動還款模式](/docs/zh-TW/v5/spot-margin-uta/get-auto-repay-mode) 返回的定時自動還款設定相互獨立。

### HTTP 請求

GET`/v5/spot-margin-trade/get-trade-auto-repay`

### 請求參數

無。

* * *

### 響應參數

參數| 類型| 說明  
---|---|---  
autoRepay| string| 保存的開關狀態。`1`：開啟；`0`：關閉。  
  
### 請求示例

  * HTTP


    
    
    GET /v5/spot-margin-trade/get-trade-auto-repay HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1792117143000  
    X-BAPI-RECV-WINDOW: 5000  
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "success",  
        "result": {  
            "autoRepay": "1"  
        },  
        "retExtInfo": {},  
        "time": 1792117143000  
    }