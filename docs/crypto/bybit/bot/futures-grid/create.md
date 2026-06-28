---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/bot/futures-grid/create
api_type: REST
updated_at: 2026-05-27 19:15:43.831573
---

# Create Grid Bot

Create a new futures grid trading bot that automatically places grid orders within a specified price range.

info

  * **Prerequisites:**  
Call [Validate Grid Input](/docs/v5/bot/futures-grid/validate-input) before this endpoint to ensure parameters are within valid bounds.

  * **Grid mode (`grid_mode`):**  
`1`: Neutral — no directional bias  
`2`: Long — bullish strategy  
`3`: Short — bearish strategy

  * **Grid type (`grid_type`):**  
`1`: Arithmetic — equal price difference between grids  
`2`: Geometric — equal price ratio between grids

  * **TP/SL type (`tp_sl_type`):**  
`1`: Both TP and SL by percentage  
`2`: Both TP and SL by price  
`3`: TP by price, SL by percentage  
`4`: TP by percentage, SL by price

  * **Response`bot_id`:**  
Returned on success. Use this ID for [Get Detail](/docs/v5/bot/futures-grid/get-detail) and [Close](/docs/v5/bot/futures-grid/close).

  * **`check_code`:**  
Returned in the response to indicate specific validation errors. `FGRID_CHECK_CODE_SUCCESS` = OK.

  * **Rate limit:**  
10 requests per second per UID.

  * **Subject to compliance wall and KYC verification.**




### HTTP Request

POST`/v5/fgridbot/create`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
symbol| **true**|  string| Trading pair symbol, uppercase only (e.g. `BTCUSDT`)  
grid_mode| **true**|  integer| Strategy direction: `1` Neutral, `2` Long, `3` Short  
min_price| **true**|  string| Lower price bound of the grid range (decimal string)  
max_price| **true**|  string| Upper price bound of the grid range (decimal string)  
cell_number| **true**|  integer| Number of grid levels, minimum 2  
leverage| **true**|  string| Position leverage multiplier (e.g. `"5"` means 5x). Must be >= 1  
grid_type| **true**|  integer| Grid spacing type: `1` Arithmetic, `2` Geometric  
total_investment| **true**|  string| Initial investment in quote currency (decimal string, e.g. `"1000"` for 1000 USDT)  
take_profit_per| false| string| Take-profit as percentage (e.g. `"0.2"` means 20%). Used when `tp_sl_type` includes percentage-based TP  
stop_loss_per| false| string| Stop-loss as percentage (e.g. `"0.1"` means 10%). Used when `tp_sl_type` includes percentage-based SL  
take_profit_price| false| string| Take-profit trigger price (decimal string). Used when `tp_sl_type` includes price-based TP  
stop_loss_price| false| string| Stop-loss trigger price (decimal string). Used when `tp_sl_type` includes price-based SL  
tp_sl_type| false| integer| TP/SL trigger mode: `1` Both by %, `2` Both by price, `3` TP price+SL %, `4` TP %+SL price  
entry_price| false| string| Optional entry trigger price for delayed activation (decimal string)  
trailing_stop_per| false| string| Trailing stop exit as percentage (e.g. `"0.05"` means 5%)  
move_up_price| false| string| Move-up price for grid shifting, not applicable when "grid_type"=`2`  
move_down_price| false| string| Move-down price for grid shifting, not applicable when "grid_type"=`2`  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
status_code| integer| `0` = success, `421` = user banned  
bot_id| integer| Unique bot ID. Use for [Get Detail](/docs/v5/bot/futures-grid/get-detail) and [Close](/docs/v5/bot/futures-grid/close)  
check_code| string| Validation result. `FGRID_CHECK_CODE_SUCCESS` = OK. See [Validate Futures Grid Input](/docs/v5/bot/futures-grid/validate-input) for full list  
ban_reason_text| string| Ban reason in user's locale. Returned only when `status_code=421`  
debug_msg| string| Debug message (testnet only)  
  
* * *

### Request Example
    
    
    POST /v5/fgridbot/create HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1672211928338  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "symbol": "BTCUSDT",  
        "grid_mode": 2,  
        "min_price": "230000",  
        "max_price": "800000",  
        "cell_number": 88,  
        "leverage": "6",  
        "grid_type": 2,  
        "total_investment": "950",  
        "entry_price": "370000",  
        "trailing_stop_per": "0.18",  
        "tp_sl_type": 4,  
        "stop_loss_price": "200000",  
        "take_profit_per": "0.28"  
    }  
      
      
      
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "success",  
        "result": {  
            "status_code": 200,  
            "debug_msg": "",  
            "bot_id": "612330315406398322",  
            "check_code": "FGRID_CHECK_CODE_UNSPECIFIED",  
            "ban_reason_text": ""  
        },  
        "retExtInfo": {},  
        "time": 1774506909426  
    }

---

# 創建網格機器人

創建一個新的合約網格交易機器人，在指定價格範圍內自動掛出網格訂單。

信息

  * **前置條件：**  
在調用本端點前，請先調用[驗證網格輸入](/docs/zh-TW/v5/bot/futures-grid/validate-input)，確保參數在有效範圍內。

  * **網格模式（`grid_mode`）：**  
`1`：中性 — 無方向偏好  
`2`：做多 — 看漲策略  
`3`：做空 — 看跌策略

  * **網格類型（`grid_type`）：**  
`1`：等差 — 網格之間價格差相等  
`2`：等比 — 網格之間價格比例相等

  * **止盈止損類型（`tp_sl_type`）：**  
`1`：止盈止損均按百分比  
`2`：止盈止損均按價格  
`3`：止盈按價格，止損按百分比  
`4`：止盈按百分比，止損按價格

  * **響應`bot_id`：**  
成功時返回，用於[查詢詳情](/docs/zh-TW/v5/bot/futures-grid/get-detail)和[關閉](/docs/zh-TW/v5/bot/futures-grid/close)。

  * **`check_code`：**  
響應中返回，表示具體驗證錯誤。`FGRID_CHECK_CODE_SUCCESS` = 正常。

  * **頻率限制：**  
每個 UID 每秒最多 10 次請求。

  * **受合規管控及 KYC 驗證約束。**




### HTTP請求

POST`/v5/fgridbot/create`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
symbol| **true**|  string| 交易對名稱，僅大寫（例如 `BTCUSDT`）  
grid_mode| **true**|  integer| 策略方向：`1` 中性，`2` 做多，`3` 做空  
min_price| **true**|  string| 網格價格範圍下限（小數字符串）  
max_price| **true**|  string| 網格價格範圍上限（小數字符串）  
cell_number| **true**|  integer| 網格層數，最小為 2  
leverage| **true**|  string| 倉位槓桿倍數（例如 `"5"` 表示 5 倍），必須 >= 1  
grid_type| **true**|  integer| 網格間距類型：`1` 等差，`2` 等比  
total_investment| **true**|  string| 初始投資金額，以報價幣種計（小數字符串，例如 `"1000"` 表示 1000 USDT）  
take_profit_per| false| string| 止盈百分比（例如 `"0.2"` 表示 20%），當 `tp_sl_type` 包含百分比止盈時使用  
stop_loss_per| false| string| 止損百分比（例如 `"0.1"` 表示 10%），當 `tp_sl_type` 包含百分比止損時使用  
take_profit_price| false| string| 止盈觸發價格（小數字符串），當 `tp_sl_type` 包含價格止盈時使用  
stop_loss_price| false| string| 止損觸發價格（小數字符串），當 `tp_sl_type` 包含價格止損時使用  
tp_sl_type| false| integer| 止盈止損觸發模式：`1` 均按百分比，`2` 均按價格，`3` 止盈按價格+止損按百分比，`4` 止盈按百分比+止損按價格  
entry_price| false| string| 可選入場觸發價格，用於延遲啓動（小數字符串）  
trailing_stop_per| false| string| 移動止損退出百分比（例如 `"0.05"` 表示 5%）  
move_up_price| false| string| 網格移動上限價格，`grid_type`=`2` 時不適用  
move_down_price| false| string| 網格移動下限價格，`grid_type`=`2` 時不適用  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
status_code| integer| `0` = 成功，`421` = 用戶被封禁  
bot_id| integer| 唯一機器人 ID，用於[查詢詳情](/docs/zh-TW/v5/bot/futures-grid/get-detail)和[關閉](/docs/zh-TW/v5/bot/futures-grid/close)  
check_code| string| 驗證結果。`FGRID_CHECK_CODE_SUCCESS` = 正常。詳見[驗證合約網格輸入](/docs/zh-TW/v5/bot/futures-grid/validate-input)  
ban_reason_text| string| 用戶語言的封禁原因，僅當 `status_code=421` 時返回  
debug_msg| string| 調試信息（僅測試網）  
  
* * *

### 請求示例
    
    
    POST /v5/fgridbot/create HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1672211928338  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "symbol": "BTCUSDT",  
        "grid_mode": 2,  
        "min_price": "230000",  
        "max_price": "800000",  
        "cell_number": 88,  
        "leverage": "6",  
        "grid_type": 2,  
        "total_investment": "950",  
        "entry_price": "370000",  
        "trailing_stop_per": "0.18",  
        "tp_sl_type": 4,  
        "stop_loss_price": "200000",  
        "take_profit_per": "0.28"  
    }  
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "success",  
        "result": {  
            "status_code": 200,  
            "debug_msg": "",  
            "bot_id": "612330315406398322",  
            "check_code": "FGRID_CHECK_CODE_UNSPECIFIED",  
            "ban_reason_text": ""  
        },  
        "retExtInfo": {},  
        "time": 1774506909426  
    }