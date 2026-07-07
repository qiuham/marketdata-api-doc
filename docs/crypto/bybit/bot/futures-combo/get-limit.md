---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/bot/futures-combo/get-limit
api_type: REST
updated_at: 2026-07-07 19:10:50.217641
---

# Close Grid Bot

Close a running futures grid trading bot. The bot will cancel all pending grid orders and close positions.

info

  * **Bot state requirement:**  
Only bots in a running state can be closed. The `bot_id` can be obtained from the [Create Futures Grid Bot](/docs/v5/bot/futures-grid/create) response or from [Get Futures Grid Bot Detail](/docs/v5/bot/futures-grid/get-detail).

  * **After closing:**  
Use [Get Futures Grid Bot Detail](/docs/v5/bot/futures-grid/get-detail) to check the final PnL and close reason.

  * **Rate limit:**  
10 requests per second per UID.




### HTTP Request

POST`/v5/fgridbot/close`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
bot_id| **true**|  string| Bot ID to close, obtained from [Create Futures Grid Bot](/docs/v5/bot/futures-grid/create) response  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
status_code| integer| `0` = success, non-zero = error  
bot_id| string| The closed bot ID  
debug_msg| string| Debug message (testnet only)  
  
* * *

### Request Example
    
    
    POST /v5/fgridbot/close HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1672211928338  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "bot_id": "612330315406398322"  
    }  
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "success",  
        "result": {  
            "status_code": 200,  
            "debug_msg": "bot has already been canceled",  
            "bot_id": "612330315406398322"  
        },  
        "retExtInfo": {},  
        "time": 1774508410683  
    }

---

# 關閉網格機器人

關閉一個正在運行的合約網格交易機器人。機器人將取消所有掛單網格訂單並平倉。

信息

  * **機器人狀態要求：**  
只有處於運行狀態的機器人才能被關閉。`bot_id` 可從[創建合約網格機器人](/docs/zh-TW/v5/bot/futures-grid/create)響應或[查詢合約網格機器人詳情](/docs/zh-TW/v5/bot/futures-grid/get-detail)中獲取。

  * **關閉後：**  
使用[查詢合約網格機器人詳情](/docs/zh-TW/v5/bot/futures-grid/get-detail)查看最終盈虧及關閉原因。

  * **頻率限制：**  
每個 UID 每秒最多 10 次請求。




### HTTP請求

POST`/v5/fgridbot/close`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
bot_id| **true**|  string| 要關閉的機器人 ID，從[創建合約網格機器人](/docs/zh-TW/v5/bot/futures-grid/create)響應中獲取  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
status_code| integer| `0` = 成功，非零 = 錯誤  
bot_id| string| 已關閉的機器人 ID  
debug_msg| string| 調試信息（僅測試網）  
  
* * *

### 請求示例
    
    
    POST /v5/fgridbot/close HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1672211928338  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "bot_id": "612330315406398322"  
    }  
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "success",  
        "result": {  
            "status_code": 200,  
            "debug_msg": "bot has already been canceled",  
            "bot_id": "612330315406398322"  
        },  
        "retExtInfo": {},  
        "time": 1774508410683  
    }