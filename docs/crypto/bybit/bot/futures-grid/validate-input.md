---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/bot/futures-grid/validate-input
api_type: REST
updated_at: 2026-11-13 19:22:03.090285
---

# Validate Grid Input

Validate futures grid bot input parameters and return allowable ranges. Use before creating a futures grid bot to ensure parameters are within valid bounds.

info

  * **When to call:**  
Always call this endpoint before [Create Futures Grid Bot](/docs/v5/bot/futures-grid/create).

  * **`check_code`:**  
`FGRID_CHECK_CODE_SUCCESS` = all parameters are valid. Any other value identifies the specific parameter that is out of range.

  * **Rate limit:**  
10 requests per second per UID.




### HTTP Request

POST`/v5/fgridbot/validate`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
symbol| **true**|  string| Trading pair symbol, uppercase only (e.g. `BTCUSDT`)  
cell_number| **true**|  integer| Number of grid levels, minimum 2  
min_price| **true**|  string| Lower price bound of the grid range (decimal string)  
max_price| **true**|  string| Upper price bound of the grid range (decimal string)  
leverage| **true**|  string| Position leverage, must be >= 1 (e.g. `"5"`)  
grid_type| **true**|  integer| Grid spacing type: `1` Arithmetic, `2` Geometric  
grid_mode| **true**|  integer| Strategy direction: `1` Neutral, `2` Long, `3` Short  
stop_loss_price| false| string| Stop-loss trigger price (decimal string). Used when `tp_sl_type` includes price-based SL  
take_profit_price| false| string| Take-profit trigger price (decimal string). Used when `tp_sl_type` includes price-based TP  
tp_sl_type| false| integer| TP/SL trigger mode: `1` Both %, `2` Both price, `3` TP price+SL %, `4` TP %+SL price  
entry_price| false| string| Entry trigger price for delayed activation (decimal string)  
stop_loss_per| false| string| Stop-loss as percentage (e.g. `"10"` means 10%). Used when `tp_sl_type` includes percentage-based SL  
take_profit_per| false| string| Take-profit as percentage (e.g. `"20"` means 20%). Used when `tp_sl_type` includes percentage-based TP  
trailing_stop_per| false| string| Trailing stop callback as percentage (e.g. `"5"` means 5%)  
init_margin| false| string| Initial margin amount in quote currency (decimal string)  
move_up_price| false| string| Move-up price for grid shifting  
move_down_price| false| string| Move-down price for grid shifting  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
status_code| integer| `0` = success, non-zero = error  
debug_msg| string| Debug message (testnet only)  
check_code| string| Validation result. `FGRID_CHECK_CODE_SUCCESS` = OK. See check code table below  
investment| object| Acceptable investment amount range (`from` / `to`, decimal strings in quote currency)  
profit| object| Acceptable per-grid profit rate range as percentage (`from` / `to`)  
cell_number| object| Acceptable grid count range (`from` / `to`)  
min_price| object| Acceptable lower price bound range (`from` / `to`)  
max_price| object| Acceptable upper price bound range (`from` / `to`)  
leverage| object| Acceptable leverage range (`from` / `to`)  
stop_loss| object| Acceptable stop-loss percentage range (`from` / `to`)  
take_profit| object| Acceptable take-profit percentage range (`from` / `to`)  
take_profit_price| object| Acceptable take-profit price range (`from` / `to`)  
stop_loss_price| object| Acceptable stop-loss price range (`from` / `to`)  
entry_price| object| Acceptable entry price range (`from` / `to`)  
trailing_stop_per| object| Acceptable trailing stop percentage range (`from` / `to`)  
long_liq_price| string| Estimated liquidation price for long direction  
short_liq_price| string| Estimated liquidation price for short direction  
move_up_price| object| Acceptable move-up price range (`from` / `to`)  
move_down_price| object| Acceptable move-down price range (`from` / `to`)  
cell_gtv0_per| string| Extra grid count allowance for VIP users (percentage relative to non-VIP)  
  
#### Check Code Values (selected)

check_code| Description  
---|---  
`FGRID_CHECK_CODE_SUCCESS`| OK — no error  
`FGRID_CHECK_CODE_LOW_PRICE_TOO_LOW`| Min price too low  
`FGRID_CHECK_CODE_LOW_PRICE_TOO_HIGH`| Min price too high  
`FGRID_CHECK_CODE_HIGH_PRICE_TOO_LOW`| Max price too low  
`FGRID_CHECK_CODE_HIGH_PRICE_TOO_HIGH`| Max price too high  
`FGRID_CHECK_CODE_GRID_NO_TOO_LOW`| Grid count too low (min 2)  
`FGRID_CHECK_CODE_GRID_NO_TOO_HIGH`| Grid count too high  
`FGRID_CHECK_CODE_INVESTMENT_TOO_LOW`| Investment too low  
`FGRID_CHECK_CODE_INVESTMENT_TOO_HIGH`| Investment too high  
`FGRID_CHECK_CODE_LEVERAGE_TOO_LOW`| Leverage too low (min 1)  
`FGRID_CHECK_CODE_LEVERAGE_TOO_HIGH`| Leverage too high  
`FGRID_CHECK_CODE_TP_TOO_LOW`| Take-profit ratio too low  
`FGRID_CHECK_CODE_TP_TOO_HIGH`| Take-profit ratio too high  
`FGRID_CHECK_CODE_SL_TOO_LOW`| Stop-loss ratio too low  
`FGRID_CHECK_CODE_SL_TOO_HIGH`| Stop-loss ratio too high  
`FGRID_CHECK_CODE_SL_CAUSE_LIQUIDATION`| Stop-loss would cause liquidation  
`FGRID_CHECK_CODE_RISK_LIMIT`| Cannot set leverage due to risk limit  
`FGRID_CHECK_CODE_OI_POS_LIMIT`| Open interest position limit exceeded  
`FGRID_CHECK_CODE_SYMBOL_NOT_EXISTS`| Symbol does not exist  
`FGRID_CHECK_CODE_USER_BANNED`| User banned  
`FGRID_CHECK_CODE_INVALID_TRAILING_STOP_PERCENT`| Invalid trailing stop percentage  
  
* * *

### Request Example
    
    
    POST /v5/fgridbot/validate HTTP/1.1  
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
        "grid_type": 2  
    }  
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "success",  
        "result": {  
            "status_code": 200,  
            "debug_msg": "",  
            "investment": {  
                "from": "7900.3349",  
                "to": "26748800"  
            },  
            "profit": {  
                "from": "8.1959",  
                "to": "8.1959"  
            },  
            "cell_number": {  
                "from": "3",  
                "to": "1562"  
            },  
            "min_price": {  
                "from": "56930.2",  
                "to": "1997760.4"  
            },  
            "max_price": {  
                "from": "479430.7",  
                "to": "1999999.8"  
            },  
            "leverage": {  
                "from": "1",  
                "to": "50"  
            },  
            "stop_loss": {  
                "from": "0",  
                "to": "100"  
            },  
            "take_profit": {  
                "from": "0",  
                "to": "500"  
            },  
            "check_code": "FGRID_CHECK_CODE_UNSPECIFIED",  
            "take_profit_price": {  
                "from": "800000",  
                "to": "1999999.8"  
            },  
            "stop_loss_price": {  
                "from": "56930.2",  
                "to": "230000"  
            },  
            "entry_price": {  
                "from": "142325.4",  
                "to": "479162.1"  
            },  
            "cell_gtv0_per": "71.88",  
            "trailing_stop_per": {  
                "from": "0.05",  
                "to": "0.99"  
            },  
            "long_liq_price": "",  
            "short_liq_price": "",  
            "move_up_price": {  
                "from": "811412.8",  
                "to": "1999999.8"  
            },  
            "move_down_price": {  
                "from": "0.1",  
                "to": "226764.9"  
            }  
        },  
        "retExtInfo": {},  
        "time": 1774508649318  
    }

---

# 驗證網格輸入

驗證合約網格機器人的輸入參數並返回允許的範圍。在創建合約網格機器人之前調用，以確保參數在有效範圍內。

信息

  * **何時調用：**  
在調用[創建合約網格機器人](/docs/zh-TW/v5/bot/futures-grid/create)之前，務必先調用此端點。

  * **`check_code`：**  
`FGRID_CHECK_CODE_SUCCESS` = 所有參數均有效。其他值表示超出範圍的具體參數。

  * **頻率限制：**  
每個 UID 每秒最多 10 次請求。




### HTTP請求

POST`/v5/fgridbot/validate`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
symbol| **true**|  string| 交易對名稱，僅大寫（例如 `BTCUSDT`）  
cell_number| **true**|  integer| 網格層數，最小為 2  
min_price| **true**|  string| 網格價格範圍下限（小數字符串）  
max_price| **true**|  string| 網格價格範圍上限（小數字符串）  
leverage| **true**|  string| 倉位槓桿，必須 >= 1（例如 `"5"`）  
grid_type| **true**|  integer| 網格間距類型：`1` 等差，`2` 等比  
grid_mode| **true**|  integer| 策略方向：`1` 中性，`2` 做多，`3` 做空  
stop_loss_price| false| string| 止損觸發價格（小數字符串），當 `tp_sl_type` 包含價格止損時使用  
take_profit_price| false| string| 止盈觸發價格（小數字符串），當 `tp_sl_type` 包含價格止盈時使用  
tp_sl_type| false| integer| 止盈止損觸發模式：`1` 均按百分比，`2` 均按價格，`3` 止盈按價格+止損按百分比，`4` 止盈按百分比+止損按價格  
entry_price| false| string| 延遲啓動的入場觸發價格（小數字符串）  
stop_loss_per| false| string| 止損百分比（例如 `"10"` 表示 10%），當 `tp_sl_type` 包含百分比止損時使用  
take_profit_per| false| string| 止盈百分比（例如 `"20"` 表示 20%），當 `tp_sl_type` 包含百分比止盈時使用  
trailing_stop_per| false| string| 移動止損回撥百分比（例如 `"5"` 表示 5%）  
init_margin| false| string| 初始保證金金額，以報價幣種計（小數字符串）  
move_up_price| false| string| 網格移動上限價格  
move_down_price| false| string| 網格移動下限價格  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
status_code| integer| `0` = 成功，非零 = 錯誤  
debug_msg| string| 調試信息（僅測試網）  
check_code| string| 驗證結果。`FGRID_CHECK_CODE_SUCCESS` = 正常。詳見下方校驗碼表  
investment| object| 可接受的投資金額範圍（`from` / `to`，報價幣種小數字符串）  
profit| object| 可接受的每格利潤率範圍百分比（`from` / `to`）  
cell_number| object| 可接受的網格數量範圍（`from` / `to`）  
min_price| object| 可接受的價格下限範圍（`from` / `to`）  
max_price| object| 可接受的價格上限範圍（`from` / `to`）  
leverage| object| 可接受的槓桿範圍（`from` / `to`）  
stop_loss| object| 可接受的止損百分比範圍（`from` / `to`）  
take_profit| object| 可接受的止盈百分比範圍（`from` / `to`）  
take_profit_price| object| 可接受的止盈價格範圍（`from` / `to`）  
stop_loss_price| object| 可接受的止損價格範圍（`from` / `to`）  
entry_price| object| 可接受的入場價格範圍（`from` / `to`）  
trailing_stop_per| object| 可接受的移動止損百分比範圍（`from` / `to`）  
long_liq_price| string| 做多方向的預估強平價格  
short_liq_price| string| 做空方向的預估強平價格  
move_up_price| object| 可接受的移動上限價格範圍（`from` / `to`）  
move_down_price| object| 可接受的移動下限價格範圍（`from` / `to`）  
cell_gtv0_per| string| VIP 用戶的額外網格數量比例（相對於非 VIP）  
  
#### 校驗碼說明（部分）

check_code| 說明  
---|---  
`FGRID_CHECK_CODE_SUCCESS`| 正常 — 無錯誤  
`FGRID_CHECK_CODE_LOW_PRICE_TOO_LOW`| 最低價格過低  
`FGRID_CHECK_CODE_LOW_PRICE_TOO_HIGH`| 最低價格過高  
`FGRID_CHECK_CODE_HIGH_PRICE_TOO_LOW`| 最高價格過低  
`FGRID_CHECK_CODE_HIGH_PRICE_TOO_HIGH`| 最高價格過高  
`FGRID_CHECK_CODE_GRID_NO_TOO_LOW`| 網格數量過少（最小為 2）  
`FGRID_CHECK_CODE_GRID_NO_TOO_HIGH`| 網格數量過多  
`FGRID_CHECK_CODE_INVESTMENT_TOO_LOW`| 投資金額過低  
`FGRID_CHECK_CODE_INVESTMENT_TOO_HIGH`| 投資金額過高  
`FGRID_CHECK_CODE_LEVERAGE_TOO_LOW`| 槓桿過低（最小為 1）  
`FGRID_CHECK_CODE_LEVERAGE_TOO_HIGH`| 槓桿過高  
`FGRID_CHECK_CODE_TP_TOO_LOW`| 止盈比例過低  
`FGRID_CHECK_CODE_TP_TOO_HIGH`| 止盈比例過高  
`FGRID_CHECK_CODE_SL_TOO_LOW`| 止損比例過低  
`FGRID_CHECK_CODE_SL_TOO_HIGH`| 止損比例過高  
`FGRID_CHECK_CODE_SL_CAUSE_LIQUIDATION`| 止損設置將導致強平  
`FGRID_CHECK_CODE_RISK_LIMIT`| 因風險限額無法設置槓桿  
`FGRID_CHECK_CODE_OI_POS_LIMIT`| 超出持倉限額  
`FGRID_CHECK_CODE_SYMBOL_NOT_EXISTS`| 交易對不存在  
`FGRID_CHECK_CODE_USER_BANNED`| 用戶被封禁  
`FGRID_CHECK_CODE_INVALID_TRAILING_STOP_PERCENT`| 移動止損百分比無效  
  
* * *

### 請求示例
    
    
    POST /v5/fgridbot/validate HTTP/1.1  
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
        "grid_type": 2  
    }  
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "success",  
        "result": {  
            "status_code": 200,  
            "debug_msg": "",  
            "investment": {  
                "from": "7900.3349",  
                "to": "26748800"  
            },  
            "profit": {  
                "from": "8.1959",  
                "to": "8.1959"  
            },  
            "cell_number": {  
                "from": "3",  
                "to": "1562"  
            },  
            "min_price": {  
                "from": "56930.2",  
                "to": "1997760.4"  
            },  
            "max_price": {  
                "from": "479430.7",  
                "to": "1999999.8"  
            },  
            "leverage": {  
                "from": "1",  
                "to": "50"  
            },  
            "stop_loss": {  
                "from": "0",  
                "to": "100"  
            },  
            "take_profit": {  
                "from": "0",  
                "to": "500"  
            },  
            "check_code": "FGRID_CHECK_CODE_UNSPECIFIED",  
            "take_profit_price": {  
                "from": "800000",  
                "to": "1999999.8"  
            },  
            "stop_loss_price": {  
                "from": "56930.2",  
                "to": "230000"  
            },  
            "entry_price": {  
                "from": "142325.4",  
                "to": "479162.1"  
            },  
            "cell_gtv0_per": "71.88",  
            "trailing_stop_per": {  
                "from": "0.05",  
                "to": "0.99"  
            },  
            "long_liq_price": "",  
            "short_liq_price": "",  
            "move_up_price": {  
                "from": "811412.8",  
                "to": "1999999.8"  
            },  
            "move_down_price": {  
                "from": "0.1",  
                "to": "226764.9"  
            }  
        },  
        "retExtInfo": {},  
        "time": 1774508649318  
    }