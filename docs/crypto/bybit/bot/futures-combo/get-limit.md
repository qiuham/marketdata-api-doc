---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/bot/futures-combo/get-limit
api_type: REST
updated_at: 2026-11-13 19:21:59.864052
---

# Get Bot Parameter Limit

Validate futures combo bot input parameters and return allowable ranges. Use before creating a combo bot to ensure parameters are within valid bounds.

info

  * **When to call:**  
Always call this endpoint before [Create Futures Combo Bot](/docs/v5/bot/futures-combo/create).

  * **`check_code`:**  
`LIMIT_CHECK_CODE_SUCCESS_UNSPECIFIED` = all parameters are valid. Any other value identifies the specific parameter out of range.

  * **Rate limit:**  
10 requests per second per UID.




### HTTP Request

POST`/v5/fcombobot/getlimit`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
leverage| **true**|  string| Position leverage multiplier (e.g. `"5"` means 5x). Must be >= 1  
init_margin| **true**|  string| Initial investment in quote currency (decimal string)  
adjust_position_mode| **true**|  integer| Rebalancing trigger mode: `1` Time, `2` Percentage, `3` Time or %, `4` Manual, `5` On settings change, `6` On transfer  
symbol_settings| **true**|  array<object>| Per-symbol portfolio configuration  
> symbol| **true**|  string| Trading pair symbol (e.g. `BTCUSDT`)  
> target_position_percent| **true**|  string| Target portfolio weight as percentage. All symbols must sum to 1  
> side| **true**|  integer| Position direction: `1` Long, `2` Short  
adjust_position_percent| false| string| Rebalancing drift threshold as percentage  
adjust_position_time_interval| false| integer| Rebalancing time interval in seconds  
sl_percent| false| string| Stop-loss as percentage (e.g. `"0.2"` means 20%)  
tp_percent| false| string| Take-profit as percentage (e.g. `"0.5"` means 50%)  
trailing_stop_percent| false| string| Trailing stop callback as percentage (e.g. `"0.05"` means 5%)  
need_to_slippage| false| boolean| Whether to include slippage calculation  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
status_code| integer| `0` = success, non-zero = error  
debug_msg| string| Debug message (testnet only)  
check_code| string| Validation result. See check code table below  
init_margin| object| Acceptable initial margin range (`min` / `max`, decimal strings in quote currency)  
leverage| object| Acceptable leverage range (`min` / `max`)  
adjust_position_percent| object| Acceptable rebalancing drift threshold range (`min` / `max`)  
adjust_position_time_interval| object| Acceptable rebalancing time interval range in seconds (`min` / `max`)  
sl_percent| object| Acceptable stop-loss percentage range (`min` / `max`)  
tp_percent| object| Acceptable take-profit percentage range (`min` / `max`)  
trailing_stop_percent| object| Acceptable trailing stop percentage range (`min` / `max`)  
  
#### Check Code Values

check_code| Description  
---|---  
`LIMIT_CHECK_CODE_SUCCESS_UNSPECIFIED`| OK — no error  
`LIMIT_CHECK_CODE_SYMBOL_NUM_TOO_LOW`| Symbol count too low  
`LIMIT_CHECK_CODE_SYMBOL_NUM_TOO_HIGH`| Symbol count too high  
`LIMIT_CHECK_CODE_ADJUST_POSITION_PERCENT_TOO_LOW`| Rebalancing threshold too low  
`LIMIT_CHECK_CODE_ADJUST_POSITION_PERCENT_TOO_HIGH`| Rebalancing threshold too high  
`LIMIT_CHECK_CODE_ADJUST_POSITION_TIME_INTERVAL_TOO_LOW`| Rebalancing time interval too short  
`LIMIT_CHECK_CODE_ADJUST_POSITION_TIME_INTERVAL_TOO_HIGH`| Rebalancing time interval too long  
`LIMIT_CHECK_CODE_INIT_MARGIN_TOO_HIGH`| Initial margin too high  
`LIMIT_CHECK_CODE_INIT_MARGIN_TOO_LOW`| Initial margin too low  
`LIMIT_CHECK_CODE_SL_PER_TOO_HIGH`| Stop-loss percentage too high  
`LIMIT_CHECK_CODE_SL_PER_TOO_LOW`| Stop-loss percentage too low  
`LIMIT_CHECK_CODE_TP_PER_TOO_HIGH`| Take-profit percentage too high  
`LIMIT_CHECK_CODE_TP_PER_TOO_LOW`| Take-profit percentage too low  
`LIMIT_CHECK_CODE_LEVERAGE_TOO_HIGH`| Leverage too high  
`LIMIT_CHECK_CODE_LEVERAGE_TOO_LOW`| Leverage too low  
`LIMIT_CHECK_CODE_TRAILING_STOP_PERCENT_TOO_LOW`| Trailing stop percentage too low  
`LIMIT_CHECK_CODE_TRAILING_STOP_PERCENT_TOO_HIGH`| Trailing stop percentage too high  
  
* * *

### Request Example
    
    
    POST /v5/fcombobot/getlimit HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1672211928338  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "leverage": "5",  
        "init_margin": "500",  
        "adjust_position_mode": 3,  
        "adjust_position_percent": "0.05",  
        "adjust_position_time_interval": 3600,  
        "symbol_settings": [  
            {  
                "symbol": "BTCUSDT",  
                "target_position_percent": "0.5",  
                "side": 1  
            },  
            {  
                "symbol": "ETHUSDT",  
                "target_position_percent": "0.5",  
                "side": 2  
            }  
        ],  
        "sl_percent": "0.2",  
        "tp_percent": "0.5",  
        "need_to_slippage": false  
    }  
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "success",  
        "result": {  
            "status_code": 0,  
            "debug_msg": "",  
            "check_code": "LIMIT_CHECK_CODE_SUCCESS_UNSPECIFIED",  
            "adjust_position_percent": {  
                "max": "0.5",  
                "min": "0.01"  
            },  
            "adjust_position_time_interval": {  
                "max": "2419200",  
                "min": "1800"  
            },  
            "init_margin": {  
                "max": "576840",  
                "min": "352.3"  
            },  
            "sl_percent": {  
                "max": "0.99",  
                "min": "0.01"  
            },  
            "tp_percent": {  
                "max": "100",  
                "min": "0.01"  
            },  
            "leverage": {  
                "max": "100",  
                "min": "1"  
            },  
            "trailing_stop_percent": {  
                "max": "0.99",  
                "min": "0.05"  
            }  
        },  
        "retExtInfo": {},  
        "time": 1774505009140  
    }

---

# 查詢機器人限制參數

驗證合約拼盤機器人的輸入參數並返回允許的範圍。在創建拼盤機器人之前調用，以確保參數在有效範圍內。

信息

  * **何時調用：**  
在調用[創建合約拼盤機器人](/docs/zh-TW/v5/bot/futures-combo/create)之前，務必先調用此端點。

  * **`check_code`：**  
`LIMIT_CHECK_CODE_SUCCESS_UNSPECIFIED` = 所有參數均有效。其他值表示超出範圍的具體參數。

  * **頻率限制：**  
每個 UID 每秒最多 10 次請求。




### HTTP請求

POST`/v5/fcombobot/getlimit`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
leverage| **true**|  string| 倉位槓桿倍數（例如 `"5"` 表示 5 倍），必須 >= 1  
init_margin| **true**|  string| 初始投資金額，以報價幣種計（小數字符串）  
adjust_position_mode| **true**|  integer| 再平衡觸發模式：`1` 按時間，`2` 按百分比，`3` 時間或百分比，`4` 手動，`5` 設置修改時，`6` 轉入時  
symbol_settings| **true**|  array<object>| 各交易對投資拼盤配置  
> symbol| **true**|  string| 交易對名稱（例如 `BTCUSDT`）  
> target_position_percent| **true**|  string| 目標倉位權重百分比，所有交易對之和必須為 1  
> side| **true**|  integer| 倉位方向：`1` 做多，`2` 做空  
adjust_position_percent| false| string| 再平衡偏離閾值百分比  
adjust_position_time_interval| false| integer| 再平衡時間間隔（秒）  
sl_percent| false| string| 止損百分比（例如 `"0.2"` 表示 20%）  
tp_percent| false| string| 止盈百分比（例如 `"0.5"` 表示 50%）  
trailing_stop_percent| false| string| 移動止損回撥百分比（例如 `"0.05"` 表示 5%）  
need_to_slippage| false| boolean| 是否包含滑點計算  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
status_code| integer| `0` = 成功，非零 = 錯誤  
debug_msg| string| 調試信息（僅測試網）  
check_code| string| 驗證結果，詳見下方校驗碼表  
init_margin| object| 可接受的初始保證金範圍（`min` / `max`，報價幣種小數字符串）  
leverage| object| 可接受的槓桿範圍（`min` / `max`）  
adjust_position_percent| object| 可接受的再平衡偏離閾值範圍（`min` / `max`）  
adjust_position_time_interval| object| 可接受的再平衡時間間隔範圍（秒，`min` / `max`）  
sl_percent| object| 可接受的止損百分比範圍（`min` / `max`）  
tp_percent| object| 可接受的止盈百分比範圍（`min` / `max`）  
trailing_stop_percent| object| 可接受的移動止損百分比範圍（`min` / `max`）  
  
#### 校驗碼說明

check_code| 說明  
---|---  
`LIMIT_CHECK_CODE_SUCCESS_UNSPECIFIED`| 正常 — 無錯誤  
`LIMIT_CHECK_CODE_SYMBOL_NUM_TOO_LOW`| 交易對數量過少  
`LIMIT_CHECK_CODE_SYMBOL_NUM_TOO_HIGH`| 交易對數量過多  
`LIMIT_CHECK_CODE_ADJUST_POSITION_PERCENT_TOO_LOW`| 再平衡閾值過低  
`LIMIT_CHECK_CODE_ADJUST_POSITION_PERCENT_TOO_HIGH`| 再平衡閾值過高  
`LIMIT_CHECK_CODE_ADJUST_POSITION_TIME_INTERVAL_TOO_LOW`| 再平衡時間間隔過短  
`LIMIT_CHECK_CODE_ADJUST_POSITION_TIME_INTERVAL_TOO_HIGH`| 再平衡時間間隔過長  
`LIMIT_CHECK_CODE_INIT_MARGIN_TOO_HIGH`| 初始保證金過高  
`LIMIT_CHECK_CODE_INIT_MARGIN_TOO_LOW`| 初始保證金過低  
`LIMIT_CHECK_CODE_SL_PER_TOO_HIGH`| 止損百分比過高  
`LIMIT_CHECK_CODE_SL_PER_TOO_LOW`| 止損百分比過低  
`LIMIT_CHECK_CODE_TP_PER_TOO_HIGH`| 止盈百分比過高  
`LIMIT_CHECK_CODE_TP_PER_TOO_LOW`| 止盈百分比過低  
`LIMIT_CHECK_CODE_LEVERAGE_TOO_HIGH`| 槓桿過高  
`LIMIT_CHECK_CODE_LEVERAGE_TOO_LOW`| 槓桿過低  
`LIMIT_CHECK_CODE_TRAILING_STOP_PERCENT_TOO_LOW`| 移動止損百分比過低  
`LIMIT_CHECK_CODE_TRAILING_STOP_PERCENT_TOO_HIGH`| 移動止損百分比過高  
  
* * *

### 請求示例
    
    
    POST /v5/fcombobot/getlimit HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1672211928338  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "leverage": "5",  
        "init_margin": "500",  
        "adjust_position_mode": 3,  
        "adjust_position_percent": "0.05",  
        "adjust_position_time_interval": 3600,  
        "symbol_settings": [  
            {  
                "symbol": "BTCUSDT",  
                "target_position_percent": "0.5",  
                "side": 1  
            },  
            {  
                "symbol": "ETHUSDT",  
                "target_position_percent": "0.5",  
                "side": 2  
            }  
        ],  
        "sl_percent": "0.2",  
        "tp_percent": "0.5",  
        "need_to_slippage": false  
    }  
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "success",  
        "result": {  
            "status_code": 0,  
            "debug_msg": "",  
            "check_code": "LIMIT_CHECK_CODE_SUCCESS_UNSPECIFIED",  
            "adjust_position_percent": {  
                "max": "0.5",  
                "min": "0.01"  
            },  
            "adjust_position_time_interval": {  
                "max": "2419200",  
                "min": "1800"  
            },  
            "init_margin": {  
                "max": "576840",  
                "min": "352.3"  
            },  
            "sl_percent": {  
                "max": "0.99",  
                "min": "0.01"  
            },  
            "tp_percent": {  
                "max": "100",  
                "min": "0.01"  
            },  
            "leverage": {  
                "max": "100",  
                "min": "1"  
            },  
            "trailing_stop_percent": {  
                "max": "0.99",  
                "min": "0.05"  
            }  
        },  
        "retExtInfo": {},  
        "time": 1774505009140  
    }