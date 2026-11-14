---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/spot-margin-uta/set-trade-auto-repay
api_type: REST
updated_at: 2026-11-13 19:25:18.262876
---

# Set Trade Auto Repay

Enable or disable automatic repayment after an eligible spot trade credits a coin to the Unified account. When enabled, the credited coin can repay its own flexible-rate liability without asset conversion. This setting is disabled by default.

info

Trade auto repayment runs only in Cross and Portfolio margin modes. An Isolated margin account can save this setting, but no trade auto repayment runs while it remains in Isolated mode. This setting is separate from scheduled automatic repayment configured through [Set Auto Repay Mode](/docs/v5/spot-margin-uta/set-auto-repay-mode).

### HTTP Request

POST`/v5/spot-margin-trade/set-trade-auto-repay`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
autoRepay| **true**|  string| `1`: enable trade auto repayment; `0`: disable trade auto repayment.  
  
* * *

### Response Parameters

Parameter| Type| Comments  
---|---|---  
autoRepay| string| Saved switch state. `1`: enabled; `0`: disabled.  
  
### Request Example

  * HTTP


    
    
    POST /v5/spot-margin-trade/set-trade-auto-repay HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1792117143000  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "autoRepay": "1"  
    }  
    

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

# 設定交易自動還款開關

開啟或關閉合格現貨交易將幣種存入統一帳戶後的自動還款功能。開啟後，入帳幣種可在無資產兌換的情況下償還同幣種的浮動利率負債。此設定預設為關閉。

信息

交易自動還款僅在全倉和組合保證金模式下運行。逐倉帳戶可以保存此設定，但在維持逐倉模式期間不會執行交易自動還款。此設定與透過 [設定現貨自動還款模式](/docs/zh-TW/v5/spot-margin-uta/set-auto-repay-mode) 設定的定時自動還款相互獨立。

### HTTP 請求

POST`/v5/spot-margin-trade/set-trade-auto-repay`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
autoRepay| **true**|  string| `1`：開啟交易自動還款；`0`：關閉交易自動還款。  
  
* * *

### 響應參數

參數| 類型| 說明  
---|---|---  
autoRepay| string| 保存的開關狀態。`1`：開啟；`0`：關閉。  
  
### 請求示例

  * HTTP


    
    
    POST /v5/spot-margin-trade/set-trade-auto-repay HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1792117143000  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "autoRepay": "1"  
    }  
    

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