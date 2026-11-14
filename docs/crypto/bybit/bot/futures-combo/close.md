---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/bot/futures-combo/close
api_type: REST
updated_at: 2026-11-13 19:21:59.776197
---

# Close Bot

Close a running futures combo trading bot. The bot will cancel all pending orders and close all positions across the portfolio.

info

  * **Bot state requirement:**  
Only bots in a running state can be closed. The `bot_id` can be obtained from the [Create Futures Combo Bot](/docs/v5/bot/futures-combo/create) response or from [Get Futures Combo Bot Detail](/docs/v5/bot/futures-combo/get-detail).

  * **After closing:**  
Use [Get Futures Combo Bot Detail](/docs/v5/bot/futures-combo/get-detail) to check the final PnL and close reason.

  * **Rate limit:**  
10 requests per second per UID.




### HTTP Request

POST`/v5/fcombobot/close`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
bot_id| **true**|  string| Bot ID to close, obtained from [Create Futures Combo Bot](/docs/v5/bot/futures-combo/create) response  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
status_code| integer| `0` = success, non-zero = error  
debug_msg| string| Debug message (testnet only)  
  
* * *

### Request Example
    
    
    POST /v5/fcombobot/close HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1672211928338  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "bot_id": "612324421335537259"  
    }  
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "success",  
        "result": {  
            "status_code": 0,  
            "debug_msg": ""  
        },  
        "retExtInfo": {},  
        "time": 1774503410522  
    }

---

# 關閉拼盤機器人

關閉一個正在運行的合約拼盤交易機器人。機器人將取消所有掛單並平倉投資組合中的所有倉位。

信息

  * **機器人狀態要求：**  
只有處於運行狀態的機器人才能被關閉。`bot_id` 可從[創建合約拼盤機器人](/docs/zh-TW/v5/bot/futures-combo/create)響應或[查詢合約拼盤機器人詳情](/docs/zh-TW/v5/bot/futures-combo/get-detail)中獲取。

  * **關閉後：**  
使用[查詢合約拼盤機器人詳情](/docs/zh-TW/v5/bot/futures-combo/get-detail)查看最終盈虧及關閉原因。

  * **頻率限制：**  
每個 UID 每秒最多 10 次請求。




### HTTP請求

POST`/v5/fcombobot/close`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
bot_id| **true**|  string| 要關閉的機器人 ID，從[創建合約拼盤機器人](/docs/zh-TW/v5/bot/futures-combo/create)響應中獲取  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
status_code| integer| `0` = 成功，非零 = 錯誤  
debug_msg| string| 調試信息（僅測試網）  
  
* * *

### 請求示例
    
    
    POST /v5/fcombobot/close HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1672211928338  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "bot_id": "612324421335537259"  
    }  
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "success",  
        "result": {  
            "status_code": 0,  
            "debug_msg": ""  
        },  
        "retExtInfo": {},  
        "time": 1774503410522  
    }