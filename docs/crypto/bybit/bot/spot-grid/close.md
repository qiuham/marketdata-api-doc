---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/bot/spot-grid/close
api_type: REST
updated_at: 2026-11-13 19:22:06.339406
---

# Close Grid Bot

Close a running spot grid bot with a specified settlement mode.

info

  * **Bot state requirement:**  
The bot must be in a closeable state (`NEW` or `RUNNING`). Bots already in `CANCELLING` or `COMPLETED` state cannot be closed again (returns status_code=405).

  * **Settlement mode (`close_mode`):**  
`2`: Base token mode — convert all holdings to base token  
`3`: Quote token mode — convert all holdings to quote token (e.g. USDT)  
`4`: Base + Quote mode — return assets as-is without conversion

  * **Rate limit:**  
3 requests per second per UID.




### HTTP Request

POST`/v5/grid/close-grid`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
grid_id| **true**|  string| Grid bot ID to close, obtained from [Create Spot Grid Bot](/docs/v5/bot/spot-grid/create) response  
close_mode| **true**|  string| Asset settlement mode: `2` Base token, `3` Quote token (e.g. USDT), `4` Base + Quote token  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
status_code| integer| `200` = success, non-zero = error  
debug_msg| string| Debug message (testnet only)  
  
* * *

### Request Example
    
    
    POST /v5/grid/close-grid HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1672211928338  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "bot_id": "612340768081708828"  
    }  
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "",  
        "result": {  
            "status_code": 200,  
            "debug_msg": ""  
        },  
        "retExtInfo": {},  
        "time": 1774513501331  
    }

---

# 關閉網格機器人

以指定的結算模式關閉一個正在運行的現貨網格機器人。

信息

  * **機器人狀態要求：**  
機器人必須處於可關閉狀態（`NEW` 或 `RUNNING`）。已處於 `CANCELLING` 或 `COMPLETED` 狀態的機器人無法再次關閉（返回 status_code=405）。

  * **結算模式（`close_mode`）：**  
`2`：基礎幣模式 — 將所有資產轉換為基礎幣  
`3`：報價幣模式 — 將所有資產轉換為報價幣（例如 USDT）  
`4`：基礎幣 + 報價幣模式 — 按原樣返回資產，不做轉換

  * **頻率限制：**  
每個 UID 每秒最多 3 次請求。




### HTTP請求

POST`/v5/grid/close-grid`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
grid_id| **true**|  string| 要關閉的網格機器人 ID，從[創建現貨網格機器人](/docs/zh-TW/v5/bot/spot-grid/create)響應中獲取  
close_mode| **true**|  string| 資產結算模式：`2` 基礎幣，`3` 報價幣（例如 USDT），`4` 基礎幣+報價幣  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
status_code| integer| `200` = 成功，非零 = 錯誤  
debug_msg| string| 調試信息（僅測試網）  
  
* * *

### 請求示例
    
    
    POST /v5/grid/close-grid HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1672211928338  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "bot_id": "612340768081708828"  
    }  
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "",  
        "result": {  
            "status_code": 200,  
            "debug_msg": ""  
        },  
        "retExtInfo": {},  
        "time": 1774513501331  
    }