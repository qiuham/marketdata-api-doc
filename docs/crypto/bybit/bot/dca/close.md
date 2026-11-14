---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/bot/dca/close
api_type: REST
updated_at: 2026-11-13 19:21:56.666403
---

# Close DCA Bot

Close a running DCA (Dollar-Cost Averaging) bot with a specified settlement mode.

info

  * **Bot state requirement:**  
The bot must be in a closeable state. Bots that are currently mid-investment cycle may not be closeable (returns status_code=503).

  * **Settlement mode (`close_mode`):**  
`2`: Base token mode — convert all holdings to base tokens  
`3`: Quote token mode — convert all holdings to quote token (e.g. USDT)

  * **Rate limit:**  
3 requests per second per UID.




### HTTP Request

POST`/v5/dca/close-bot`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
bot_id| **true**|  string| DCA bot ID to close, obtained from [Create Spot DCA Bot](/docs/v5/bot/dca/create) response  
close_mode| **true**|  string| Asset settlement mode: `2` Base token, `3` Quote token (e.g. USDT)  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
status_code| integer| `200` = success, non-zero = error  
bot_id| string| The closed DCA bot ID  
close_mode| string| The settlement mode used, `DCA_BASE_MODE`, `DCA_QUOTE_MODE`  
debug_msg| string| Debug message (testnet only)  
  
* * *

### Request Example
    
    
    POST /v5/dca/close-bot HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1672211928338  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "bot_id": "612349292702654770",  
        "close_mode": 2  
    }  
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "",  
        "result": {  
            "status_code": 200,  
            "bot_id": "612349292702654770",  
            "close_mode": "DCA_BASE_MODE",  
            "debug_msg": ""  
        },  
        "retExtInfo": {},  
        "time": 1774518356929  
    }

---

# 關閉定投機器人

以指定的結算模式關閉一個正在運行的定投（DCA）機器人。

信息

  * **機器人狀態要求：**  
機器人必須處於可關閉狀態。當前處於投資週期中的機器人可能無法關閉（返回 status_code=503）。

  * **結算模式（`close_mode`）：**  
`2`：基礎幣模式 — 將所有資產轉換為基礎幣  
`3`：報價幣模式 — 將所有資產轉換為報價幣（例如 USDT）

  * **頻率限制：**  
每個 UID 每秒最多 3 次請求。




### HTTP請求

POST`/v5/dca/close-bot`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
bot_id| **true**|  string| 要關閉的定投機器人 ID，從[創建現貨定投機器人](/docs/zh-TW/v5/bot/dca/create)響應中獲取  
close_mode| **true**|  string| 資產結算模式：`2` 基礎幣，`3` 報價幣（例如 USDT）  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
status_code| integer| `200` = 成功，非零 = 錯誤  
bot_id| string| 已關閉的定投機器人 ID  
close_mode| string| 所使用的結算模式：`DCA_BASE_MODE`、`DCA_QUOTE_MODE`  
debug_msg| string| 調試信息（僅測試網）  
  
* * *

### 請求示例
    
    
    POST /v5/dca/close-bot HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1672211928338  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "bot_id": "612349292702654770",  
        "close_mode": 2  
    }  
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "",  
        "result": {  
            "status_code": 200,  
            "bot_id": "612349292702654770",  
            "close_mode": "DCA_BASE_MODE",  
            "debug_msg": ""  
        },  
        "retExtInfo": {},  
        "time": 1774518356929  
    }