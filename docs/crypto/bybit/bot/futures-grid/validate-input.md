---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/bot/futures-grid/validate-input
api_type: REST
updated_at: 2026-07-02 19:16:18.923016
---

# Create Martingale Bot

Create a new futures Martingale trading bot. The bot opens an initial position and adds to it when price moves against the position, then takes profit when price reverses.

info

  * **How it works:**  
The bot opens an initial position and scales into it when price moves adversely by `price_float_percent`. Each add multiplies the base position size by `add_position_percent`. When the accumulated position reaches the round take-profit (`round_tp_percent`), the bot closes and optionally restarts.

  * **Mode (`martingale_mode`):**  
`1`: Long — buys on dips, profits on price reversal up  
`2`: Short — sells on rallies, profits on price reversal down

  * **Auto-cycle (`auto_cycle_toggle`):**  
`1`: Enable — restart after each round take-profit  
`2`: Disable — stop after a single round take-profit

  * **Prerequisites:**  
Call [Get Futures Martingale Limit](/docs/v5/bot/futures-martingale/get-limit) before this endpoint to validate parameter ranges.

  * **Rate limit:**  
10 requests per second per UID.

  * **Subject to compliance wall, GEO IP check, and KYC verification.**




### HTTP Request

POST`/v5/fmartingalebot/create`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
symbol| **true**|  string| Trading pair symbol, uppercase only (e.g. `BTCUSDT`)  
martingale_mode| **true**|  integer| Strategy direction: `1` Long (buy dips), `2` Short (sell rallies)  
leverage| **true**|  string| Position leverage multiplier (e.g. `"5"` means 5x). Must be >= 1  
price_float_percent| **true**|  string| Price movement percentage to trigger a position add (e.g. `"0.015"` means add when price moves 1.5% against the position)  
add_position_percent| **true**|  string| Position add scaling as percentage of base position size (e.g. `"1.1"` = 1.1x base; `"2"` = 2x base)  
add_position_num| **true**|  integer| Maximum number of position adds per round  
init_margin| **true**|  string| Initial investment in quote currency (decimal string, e.g. `"1000"` for 1000 USDT)  
round_tp_percent| **true**|  string| Single round take-profit as percentage (e.g. `"0.03"` means close when profit reaches 3%)  
auto_cycle_toggle| false| integer| Auto-cycle mode: `1` Enable (restart after TP), `2` Disable (stop after single TP)  
sl_percent| false| string| Stop-loss as percentage of total margin (e.g. `"0.2"` means close when loss reaches 20%). Leave empty if not set  
entry_price| false| string| Entry trigger price as absolute price (decimal string). Leave empty if not set  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
status_code| integer| `0` = success, `421` = user banned  
bot_id| integer| Unique bot ID. Use for [Get Detail](/docs/v5/bot/futures-martingale/get-detail) and [Close](/docs/v5/bot/futures-martingale/close)  
ban_reason_text| string| Ban reason in user's locale. Returned only when `status_code=421`  
debug_msg| string| Debug message (testnet only)  
  
* * *

### Request Example
    
    
    POST /v5/fmartingalebot/create HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1672211928338  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "symbol": "MNTUSDT",  
        "martingale_mode": 1,  
        "leverage": "5",  
        "price_float_percent": "0.16",  
        "add_position_percent": "1.8",  
        "add_position_num": 5,  
        "round_tp_percent": "0.1",  
        "init_margin": "650",  
        "sl_percent": "0.5",  
        "entry_price": "0.56",  
        "auto_cycle_toggle": 2  
    }  
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "success",  
        "result": {  
            "status_code": 0,  
            "debug_msg": "",  
            "ban_reason_text": "",  
            "bot_id": "612335280740902531"  
        },  
        "retExtInfo": {},  
        "time": 1774509868961  
    }

---

# 創建馬丁格爾機器人

創建一個新的合約馬丁格爾交易機器人。機器人建立初始倉位，當價格逆勢移動時加倉，反轉後止盈。

信息

  * **運作方式：**  
機器人開立初始倉位，當價格逆勢移動 `price_float_percent` 時追加倉位。每次追加倉位以 `add_position_percent` 倍基礎倉位規模擴大。當累計倉位達到單輪止盈目標（`round_tp_percent`）時，機器人平倉並可選擇重新啟動。

  * **模式（`martingale_mode`）：**  
`1`：做多 — 逢跌買入，價格反彈時獲利  
`2`：做空 — 逢漲賣出，價格回落時獲利

  * **自動循環（`auto_cycle_toggle`）：**  
`1`：啓用 — 每輪止盈後重新啟動  
`2`：停用 — 單輪止盈後停止

  * **前置條件：**  
在調用本端點前，請先調用[查詢合約馬丁格爾限制參數](/docs/zh-TW/v5/bot/futures-martingale/get-limit)，驗證參數範圍。

  * **頻率限制：**  
每個 UID 每秒最多 10 次請求。

  * **受合規管控、地理位置 IP 限制及 KYC 驗證約束。**




### HTTP請求

POST`/v5/fmartingalebot/create`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
symbol| **true**|  string| 交易對名稱，僅大寫（例如 `BTCUSDT`）  
martingale_mode| **true**|  integer| 策略方向：`1` 做多（逢跌買入），`2` 做空（逢漲賣出）  
leverage| **true**|  string| 倉位槓桿倍數（例如 `"5"` 表示 5 倍），必須 >= 1  
price_float_percent| **true**|  string| 觸發追加倉位的價格變動百分比（例如 `"0.015"` 表示逆勢移動 1.5% 時追加）  
add_position_percent| **true**|  string| 追加倉位規模，以基礎倉位規模百分比計（例如 `"1.1"` = 1.1 倍基礎倉位；`"2"` = 2 倍基礎倉位）  
add_position_num| **true**|  integer| 每輪最大追加倉位次數  
init_margin| **true**|  string| 初始投資金額，以報價幣種計（小數字符串，例如 `"1000"` 表示 1000 USDT）  
round_tp_percent| **true**|  string| 單輪止盈百分比（例如 `"0.03"` 表示盈利達 3% 時平倉）  
auto_cycle_toggle| false| integer| 自動循環模式：`1` 啓用（止盈後重啓），`2` 停用（單輪止盈後停止）  
sl_percent| false| string| 止損百分比，以總保證金為基準（例如 `"0.2"` 表示虧損達 20% 時平倉）。不設置請留空  
entry_price| false| string| 入場觸發價格，以絕對價格計（小數字符串）。不設置請留空  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
status_code| integer| `0` = 成功，`421` = 用戶被封禁  
bot_id| integer| 唯一機器人 ID，用於[查詢詳情](/docs/zh-TW/v5/bot/futures-martingale/get-detail)和[關閉](/docs/zh-TW/v5/bot/futures-martingale/close)  
ban_reason_text| string| 用戶語言的封禁原因，僅當 `status_code=421` 時返回  
debug_msg| string| 調試信息（僅測試網）  
  
* * *

### 請求示例
    
    
    POST /v5/fmartingalebot/create HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1672211928338  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "symbol": "MNTUSDT",  
        "martingale_mode": 1,  
        "leverage": "5",  
        "price_float_percent": "0.16",  
        "add_position_percent": "1.8",  
        "add_position_num": 5,  
        "round_tp_percent": "0.1",  
        "init_margin": "650",  
        "sl_percent": "0.5",  
        "entry_price": "0.56",  
        "auto_cycle_toggle": 2  
    }  
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "success",  
        "result": {  
            "status_code": 0,  
            "debug_msg": "",  
            "ban_reason_text": "",  
            "bot_id": "612335280740902531"  
        },  
        "retExtInfo": {},  
        "time": 1774509868961  
    }