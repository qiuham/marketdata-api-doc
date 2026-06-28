---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/bot/futures-martingale/create
api_type: REST
updated_at: 2026-05-27 19:15:49.601233
---

# Get Bot Parameter Limit

Validate futures Martingale bot input parameters and return allowable ranges. Use before creating a Martingale bot to ensure parameters are within valid bounds.

info

  * **When to call:**  
Always call this endpoint before [Create Futures Martingale Bot](/docs/v5/bot/futures-martingale/create).

  * **`check_code`:**  
`F_MART_LIMIT_CHECK_CODE_F_MART_CHECK_CODE_SUCCESS_UNSPECIFIED` = all parameters are valid. Any other value identifies the specific parameter out of range.

  * **Rate limit:**  
100 requests per second per IP.




### HTTP Request

POST`/v5/fmartingalebot/getlimit`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
symbol| **true**|  string| Trading pair symbol, uppercase only (e.g. `BTCUSDT`)  
martingale_mode| **true**|  integer| Strategy direction: `1` Long, `2` Short  
leverage| **true**|  string| Position leverage multiplier (e.g. `"5"` means 5x). Must be >= 1  
price_float_percent| false| string| Price movement trigger as percentage (e.g. `"0.015"` means 1.5%)  
add_position_percent| false| string| Position add scaling as percentage of base position (e.g. `"1"` = 1x)  
add_position_num| false| integer| Maximum number of position adds per round  
init_margin| false| string| Initial investment in quote currency (decimal string)  
round_tp_percent| false| string| Single round take-profit as percentage (e.g. `"0.03"` means 3%)  
sl_percent| false| string| Stop-loss as percentage (e.g. `"0.2"` means 20%)  
entry_price| false| string| Entry trigger price (decimal string)  
need_to_slippage| false| boolean| Whether to include slippage calculation  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
status_code| integer| `0` = success, non-zero = error  
debug_msg| string| Debug message (testnet only)  
check_code| string| Validation result. See check code table below  
price_float_percent| object| Acceptable price float percentage range (`min` / `max`)  
add_position_percent| object| Acceptable add position percentage range (`min` / `max`)  
add_position_num| object| Acceptable add position count range (`min` / `max`)  
init_margin| object| Acceptable initial margin range (`min` / `max`, decimal strings in quote currency)  
round_tp_percent| object| Acceptable round take-profit percentage range (`min` / `max`)  
sl_percent| object| Acceptable stop-loss percentage range (`min` / `max`)  
entry_price| object| Acceptable entry price range (`min` / `max`)  
leverage| object| Acceptable leverage range (`min` / `max`)  
  
#### Check Code Values

check_code| Description  
---|---  
`F_MART_LIMIT_CHECK_CODE_F_MART_CHECK_CODE_SUCCESS_UNSPECIFIED`| OK — no error  
`F_MART_LIMIT_CHECK_CODE_F_MART_PRICE_FLOAT_PERCENT_TOO_HIGH`| Price float percentage too high  
`F_MART_LIMIT_CHECK_CODE_F_MART_PRICE_FLOAT_PERCENT_TOO_LOW`| Price float percentage too low  
`F_MART_LIMIT_CHECK_CODE_F_MART_ADD_POSITION_PERCENT_TOO_HIGH`| Add position percentage too high  
`F_MART_LIMIT_CHECK_CODE_F_MART_ADD_POSITION_PERCENT_TOO_LOW`| Add position percentage too low  
`F_MART_LIMIT_CHECK_CODE_F_MART_ADD_POSITION_NUM_TOO_HIGH`| Add position count too high  
`F_MART_LIMIT_CHECK_CODE_F_MART_ADD_POSITION_NUM_TOO_LOW`| Add position count too low  
`F_MART_LIMIT_CHECK_CODE_F_MART_INIT_MARGIN_TOO_HIGH`| Initial margin too high  
`F_MART_LIMIT_CHECK_CODE_F_MART_INIT_MARGIN_TOO_LOW`| Initial margin too low  
`F_MART_LIMIT_CHECK_CODE_F_MART_ROUND_TARGET_TP_PERCENT_TOO_HIGH`| Round TP percentage too high  
`F_MART_LIMIT_CHECK_CODE_F_MART_ROUND_TARGET_TP_PERCENT_TOO_LOW`| Round TP percentage too low  
`F_MART_LIMIT_CHECK_CODE_F_MART_SL_PER_TOO_HIGH`| Stop-loss percentage too high  
`F_MART_LIMIT_CHECK_CODE_F_MART_SL_PER_TOO_LOW`| Stop-loss percentage too low  
`F_MART_LIMIT_CHECK_CODE_F_MART_ENTRY_PRICE_TOO_HIGH`| Entry price too high  
`F_MART_LIMIT_CHECK_CODE_F_MART_ENTRY_PRICE_TOO_LOW`| Entry price too low  
`F_MART_LIMIT_CHECK_CODE_F_MART_LEVERAGE_TOO_HIGH`| Leverage too high  
`F_MART_LIMIT_CHECK_CODE_F_MART_LEVERAGE_TOO_LOW`| Leverage too low  
  
* * *

### Request Example
    
    
    POST /v5/fmartingalebot/getlimit HTTP/1.1  
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
        "init_margin": "1000",  
        "sl_percent": "0.5",  
        "auto_cycle_toggle": 2  
    }  
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "success",  
        "result": {  
            "status_code": 0,  
            "debug_msg": "",  
            "check_code": "F_MART_LIMIT_CHECK_CODE_F_MART_CHECK_CODE_SUCCESS_UNSPECIFIED",  
            "price_float_percent": {  
                "max": "0.199",  
                "min": "0.001"  
            },  
            "add_position_percent": {  
                "max": "2",  
                "min": "1"  
            },  
            "add_position_num": {  
                "max": "10",  
                "min": "1"  
            },  
            "init_margin": {  
                "max": "34004.22",  
                "min": "0.7682"  
            },  
            "round_tp_percent": {  
                "max": "4.45",  
                "min": "0.01"  
            },  
            "sl_percent": {  
                "max": "1",  
                "min": "0"  
            },  
            "entry_price": {  
                "max": "0.7086",  
                "min": "0.2105"  
            },  
            "leverage": {  
                "max": "20",  
                "min": "1"  
            }  
        },  
        "retExtInfo": {},  
        "time": 1774510798514  
    }

---

# 查詢機器人限制參數

驗證合約馬丁格爾機器人的輸入參數並返回允許的範圍。在創建馬丁格爾機器人之前調用，以確保參數在有效範圍內。

信息

  * **何時調用：**  
在調用[創建合約馬丁格爾機器人](/docs/zh-TW/v5/bot/futures-martingale/create)之前，務必先調用此端點。

  * **`check_code`：**  
`F_MART_LIMIT_CHECK_CODE_F_MART_CHECK_CODE_SUCCESS_UNSPECIFIED` = 所有參數均有效。其他值表示超出範圍的具體參數。

  * **頻率限制：**  
每個 IP 每秒最多 100 次請求。




### HTTP請求

POST`/v5/fmartingalebot/getlimit`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
symbol| **true**|  string| 交易對名稱，僅大寫（例如 `BTCUSDT`）  
martingale_mode| **true**|  integer| 策略方向：`1` 做多，`2` 做空  
leverage| **true**|  string| 倉位槓桿倍數（例如 `"5"` 表示 5 倍），必須 >= 1  
price_float_percent| false| string| 觸發追加倉位的價格變動百分比（例如 `"0.015"` 表示 1.5%）  
add_position_percent| false| string| 追加倉位規模，以基礎倉位規模百分比計（例如 `"1"` = 1 倍）  
add_position_num| false| integer| 每輪最大追加倉位次數  
init_margin| false| string| 初始投資金額，以報價幣種計（小數字符串）  
round_tp_percent| false| string| 單輪止盈百分比（例如 `"0.03"` 表示 3%）  
sl_percent| false| string| 止損百分比（例如 `"0.2"` 表示 20%）  
entry_price| false| string| 入場觸發價格（小數字符串）  
need_to_slippage| false| boolean| 是否包含滑點計算  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
status_code| integer| `0` = 成功，非零 = 錯誤  
debug_msg| string| 調試信息（僅測試網）  
check_code| string| 驗證結果，詳見下方校驗碼表  
price_float_percent| object| 可接受的價格浮動百分比範圍（`min` / `max`）  
add_position_percent| object| 可接受的追加倉位百分比範圍（`min` / `max`）  
add_position_num| object| 可接受的追加倉位次數範圍（`min` / `max`）  
init_margin| object| 可接受的初始保證金範圍（`min` / `max`，報價幣種小數字符串）  
round_tp_percent| object| 可接受的單輪止盈百分比範圍（`min` / `max`）  
sl_percent| object| 可接受的止損百分比範圍（`min` / `max`）  
entry_price| object| 可接受的入場價格範圍（`min` / `max`）  
leverage| object| 可接受的槓桿範圍（`min` / `max`）  
  
#### 校驗碼說明

check_code| 說明  
---|---  
`F_MART_LIMIT_CHECK_CODE_F_MART_CHECK_CODE_SUCCESS_UNSPECIFIED`| 正常 — 無錯誤  
`F_MART_LIMIT_CHECK_CODE_F_MART_PRICE_FLOAT_PERCENT_TOO_HIGH`| 價格浮動百分比過高  
`F_MART_LIMIT_CHECK_CODE_F_MART_PRICE_FLOAT_PERCENT_TOO_LOW`| 價格浮動百分比過低  
`F_MART_LIMIT_CHECK_CODE_F_MART_ADD_POSITION_PERCENT_TOO_HIGH`| 追加倉位百分比過高  
`F_MART_LIMIT_CHECK_CODE_F_MART_ADD_POSITION_PERCENT_TOO_LOW`| 追加倉位百分比過低  
`F_MART_LIMIT_CHECK_CODE_F_MART_ADD_POSITION_NUM_TOO_HIGH`| 追加倉位次數過多  
`F_MART_LIMIT_CHECK_CODE_F_MART_ADD_POSITION_NUM_TOO_LOW`| 追加倉位次數過少  
`F_MART_LIMIT_CHECK_CODE_F_MART_INIT_MARGIN_TOO_HIGH`| 初始保證金過高  
`F_MART_LIMIT_CHECK_CODE_F_MART_INIT_MARGIN_TOO_LOW`| 初始保證金過低  
`F_MART_LIMIT_CHECK_CODE_F_MART_ROUND_TARGET_TP_PERCENT_TOO_HIGH`| 單輪止盈百分比過高  
`F_MART_LIMIT_CHECK_CODE_F_MART_ROUND_TARGET_TP_PERCENT_TOO_LOW`| 單輪止盈百分比過低  
`F_MART_LIMIT_CHECK_CODE_F_MART_SL_PER_TOO_HIGH`| 止損百分比過高  
`F_MART_LIMIT_CHECK_CODE_F_MART_SL_PER_TOO_LOW`| 止損百分比過低  
`F_MART_LIMIT_CHECK_CODE_F_MART_ENTRY_PRICE_TOO_HIGH`| 入場價格過高  
`F_MART_LIMIT_CHECK_CODE_F_MART_ENTRY_PRICE_TOO_LOW`| 入場價格過低  
`F_MART_LIMIT_CHECK_CODE_F_MART_LEVERAGE_TOO_HIGH`| 槓桿過高  
`F_MART_LIMIT_CHECK_CODE_F_MART_LEVERAGE_TOO_LOW`| 槓桿過低  
  
* * *

### 請求示例
    
    
    POST /v5/fmartingalebot/getlimit HTTP/1.1  
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
        "init_margin": "1000",  
        "sl_percent": "0.5",  
        "auto_cycle_toggle": 2  
    }  
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "success",  
        "result": {  
            "status_code": 0,  
            "debug_msg": "",  
            "check_code": "F_MART_LIMIT_CHECK_CODE_F_MART_CHECK_CODE_SUCCESS_UNSPECIFIED",  
            "price_float_percent": {  
                "max": "0.199",  
                "min": "0.001"  
            },  
            "add_position_percent": {  
                "max": "2",  
                "min": "1"  
            },  
            "add_position_num": {  
                "max": "10",  
                "min": "1"  
            },  
            "init_margin": {  
                "max": "34004.22",  
                "min": "0.7682"  
            },  
            "round_tp_percent": {  
                "max": "4.45",  
                "min": "0.01"  
            },  
            "sl_percent": {  
                "max": "1",  
                "min": "0"  
            },  
            "entry_price": {  
                "max": "0.7086",  
                "min": "0.2105"  
            },  
            "leverage": {  
                "max": "20",  
                "min": "1"  
            }  
        },  
        "retExtInfo": {},  
        "time": 1774510798514  
    }