---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/bot/spot-grid/validate-input
api_type: REST
updated_at: 2026-11-13 19:22:09.326646
---

# Validate Grid Input

Validate spot grid bot parameters before creation. Returns acceptable ranges for each parameter and a check code indicating any validation errors.

info

  * **When to call:**  
Always call this endpoint before [Create Spot Grid Bot](/docs/v5/bot/spot-grid/create) to ensure parameters are within valid bounds.

  * **`check_code`:**  
`SPOT_CHECK_CODE_SUCCESS_UNSPECIFIED` (value `0`) means all parameters are valid. Any other value identifies the specific parameter that is out of range.

  * **Authentication:**  
This endpoint does **not** require authentication (guest mode).

  * **Rate limit:**  
100 requests per second per IP.




### HTTP Request

POST`/v5/grid/validate-input`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
symbol| **true**|  string| Trading pair symbol, uppercase only (e.g. `BTCUSDT`)  
cell_number| **true**|  integer| Number of grid intervals, minimum 2  
min_price| **true**|  string| Lower bound of the grid price range (decimal string)  
max_price| **true**|  string| Upper bound of the grid price range. Must be greater than `min_price` (decimal string)  
invest_mode| false| integer| Investment mode: `0` Quote only (default), `1` Base only, `2` Base + Quote  
base_investment| false| string| Investment in base token (decimal string). **Required** when `invest_mode` is `1` or `2`  
quote_investment| false| string| Investment in quote token (decimal string). **Required** when `invest_mode` is `0` or `2`  
stop_loss| false| string| Stop-loss as absolute price (decimal string)  
take_profit| false| string| Take-profit as absolute price (decimal string)  
entry_price| false| string| Entry trigger as absolute price (decimal string)  
ts_percent| false| string| Trailing stop callback ratio, range `[0, 0.99]` (e.g. `"0.05"` means 5%)  
enable_trailing| false| boolean| Whether to enable grid trailing. Requires `cell_number >= 5`  
limit_up_price| false| string| Upper limit price for grid trailing (decimal string)  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
status_code| integer| `0` or `200` = success  
debug_msg| string| Debug message (testnet only)  
check_code| string| Validation result code. `SPOT_CHECK_CODE_SUCCESS_UNSPECIFIED` = OK. See check code table below  
investment| object| Acceptable range for total investment (`from` / `to`, decimal strings)  
profit| object| Acceptable per-grid profit rate range as decimal ratio (`from` / `to`)  
cell_number| object| Acceptable grid count range (`from` / `to`)  
min_price| object| Acceptable lower price bound range (`from` / `to`)  
max_price| object| Acceptable upper price bound range (`from` / `to`)  
stop_loss| object| Acceptable stop-loss price range (`from` / `to`)  
take_profit| object| Acceptable take-profit price range (`from` / `to`)  
entry_price| object| Acceptable entry price range (`from` / `to`)  
base_investment| object| Acceptable base token investment range (`from` / `to`)  
cell_distance| string| Grid interval distance in quote token price units (decimal string)  
ts_percent| object| Acceptable trailing stop ratio range (`from` / `to`)  
limit_up_price| object| Acceptable trailing upper limit price range (`from` / `to`)  
  
#### Check Code Values

check_code| Description  
---|---  
`SPOT_CHECK_CODE_SUCCESS_UNSPECIFIED`| OK — no error  
`SPOT_CHECK_CODE_LOW_PRICE_TOO_LOW`| `min_price` too low  
`SPOT_CHECK_CODE_LOW_PRICE_TOO_HIGH`| `min_price` too high  
`SPOT_CHECK_CODE_HIGH_PRICE_TOO_LOW`| `max_price` too low  
`SPOT_CHECK_CODE_HIGH_PRICE_TOO_HIGH`| `max_price` too high  
`SPOT_CHECK_CODE_GRID_NO_TOO_LOW`| `cell_number` too few  
`SPOT_CHECK_CODE_GRID_NO_TOO_HIGH`| `cell_number` too many  
`SPOT_CHECK_CODE_INVESTMENT_TOO_LOW`| Investment too low  
`SPOT_CHECK_CODE_INVESTMENT_TOO_HIGH`| Investment too high  
`SPOT_CHECK_CODE_TP_TOO_LOW`| Take-profit too low  
`SPOT_CHECK_CODE_TP_TOO_HIGH`| Take-profit too high  
`SPOT_CHECK_CODE_SL_TOO_LOW`| Stop-loss too low  
`SPOT_CHECK_CODE_SL_TOO_HIGH`| Stop-loss too high  
`SPOT_CHECK_CODE_EP_TOO_LOW`| Entry price too low  
`SPOT_CHECK_CODE_EP_TOO_HIGH`| Entry price too high  
`SPOT_CHECK_CODE_TS_PERCENT_TOO_LOW`| Trailing stop percentage too low  
`SPOT_CHECK_CODE_TS_PERCENT_TOO_HIGH`| Trailing stop percentage too high  
`SPOT_CHECK_CODE_TP_TOO_LOW_THAN_MARKET`| Take-profit too low relative to market price  
`SPOT_CHECK_CODE_SL_TOO_HIGH_THAN_MARKET`| Stop-loss too high relative to market price  
`SPOT_CHECK_CODE_LIMIT_UP_PRICE_TOO_LOW`| `limit_up_price` too low  
`SPOT_CHECK_CODE_LIMIT_UP_PRICE_TOO_HIGH`| `limit_up_price` too high  
`SPOT_CHECK_CODE_CAN_NOT_ENABLE_TRAILING_UP`| `cell_number < 5`, trailing not allowed  
`SPOT_CHECK_CODE_ENTRY_PRICE_FORBIDDEN_TRAILING_UP`| Entry price out of grid range, trailing not allowed  
`SPOT_CHECK_CODE_LAST_PRICE_FORBIDDEN_TRAILING_UP`| Market price out of grid range, trailing not allowed  
`SPOT_CHECK_CODE_INVESTMENT_FORBIDDEN_TRAILING_UP`| Investment too small for trailing  
  
* * *

### Request Example
    
    
    POST /v5/grid/validate-input HTTP/1.1  
    Host: api-testnet.bybit.com  
    Content-Type: application/json  
      
    {  
        "symbol": "MNTUSDT",  
        "max_price": "1.2",  
        "min_price": "0.3",  
        "quote_investment": "",  
        "base_investment": "300",  
        "invest_mode": 1,  
        "cell_number": 66,  
        "entry_price": "0.4"  
    }  
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "",  
        "result": {  
            "status_code": 200,  
            "debug_msg": "",  
            "investment": {  
                "from": "0",  
                "to": "0"  
            },  
            "profit": {  
                "from": "0.0114",  
                "to": "0.0453"  
            },  
            "cell_number": {  
                "from": "2",  
                "to": "562"  
            },  
            "min_price": {  
                "from": "0.1568",  
                "to": "3.92"  
            },  
            "max_price": {  
                "from": "0.3012",  
                "to": "40"  
            },  
            "stop_loss": {  
                "from": "0",  
                "to": "0.3"  
            },  
            "take_profit": {  
                "from": "1.2",  
                "to": ""  
            },  
            "entry_price": {  
                "from": "0.2352",  
                "to": "0.784"  
            },  
            "cell_distance": "0.0136",  
            "check_code": "SPOT_CHECK_CODE_SUCCESS_UNSPECIFIED",  
            "base_investment": {  
                "from": "228.36",  
                "to": "1366590.08"  
            },  
            "ts_percent": {  
                "from": "0.03",  
                "to": "0.99"  
            },  
            "limit_up_price": {  
                "from": "1.2112",  
                "to": "3.9065"  
            }  
        },  
        "retExtInfo": {},  
        "time": 1774513367099  
    }

---

# 驗證網格輸入

在創建現貨網格機器人前驗證參數。返回各參數的可接受範圍及表示驗證錯誤的校驗碼。

信息

  * **何時調用：**  
在調用[創建現貨網格機器人](/docs/zh-TW/v5/bot/spot-grid/create)之前，務必先調用此端點，確保參數在有效範圍內。

  * **`check_code`：**  
`SPOT_CHECK_CODE_SUCCESS_UNSPECIFIED`（值 `0`）表示所有參數均有效。其他值表示超出範圍的具體參數。

  * **身份驗證：**  
此端點**無需** 身份驗證（訪客模式）。

  * **頻率限制：**  
每個 IP 每秒最多 100 次請求。




### HTTP請求

POST`/v5/grid/validate-input`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
symbol| **true**|  string| 交易對名稱，僅大寫（例如 `BTCUSDT`）  
cell_number| **true**|  integer| 網格間隔數量，最小為 2  
min_price| **true**|  string| 網格價格範圍下限（小數字符串）  
max_price| **true**|  string| 網格價格範圍上限，必須大於 `min_price`（小數字符串）  
invest_mode| false| integer| 投資模式：`0` 僅報價幣（默認），`1` 僅基礎幣，`2` 基礎幣+報價幣  
base_investment| false| string| 基礎幣種投資金額（小數字符串）。`invest_mode` 為 `1` 或 `2` 時**必填**  
quote_investment| false| string| 報價幣種投資金額（小數字符串）。`invest_mode` 為 `0` 或 `2` 時**必填**  
stop_loss| false| string| 止損絕對價格（小數字符串）  
take_profit| false| string| 止盈絕對價格（小數字符串）  
entry_price| false| string| 入場觸發絕對價格（小數字符串）  
ts_percent| false| string| 移動止損回撥比例，範圍 `[0, 0.99]`（例如 `"0.05"` 表示 5%）  
enable_trailing| false| boolean| 是否啓用網格追蹤。要求 `cell_number >= 5`  
limit_up_price| false| string| 網格追蹤上限價格（小數字符串）  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
status_code| integer| `0` 或 `200` = 成功  
debug_msg| string| 調試信息（僅測試網）  
check_code| string| 驗證結果碼。`SPOT_CHECK_CODE_SUCCESS_UNSPECIFIED` = 正常。詳見下方校驗碼表  
investment| object| 可接受的總投資金額範圍（`from` / `to`，小數字符串）  
profit| object| 可接受的每格利潤率範圍，小數比例（`from` / `to`）  
cell_number| object| 可接受的網格數量範圍（`from` / `to`）  
min_price| object| 可接受的價格下限範圍（`from` / `to`）  
max_price| object| 可接受的價格上限範圍（`from` / `to`）  
stop_loss| object| 可接受的止損價格範圍（`from` / `to`）  
take_profit| object| 可接受的止盈價格範圍（`from` / `to`）  
entry_price| object| 可接受的入場價格範圍（`from` / `to`）  
base_investment| object| 可接受的基礎幣種投資金額範圍（`from` / `to`）  
cell_distance| string| 網格間隔距離，以報價幣種價格單位計（小數字符串）  
ts_percent| object| 可接受的移動止損比例範圍（`from` / `to`）  
limit_up_price| object| 可接受的追蹤上限價格範圍（`from` / `to`）  
  
#### 校驗碼說明

check_code| 說明  
---|---  
`SPOT_CHECK_CODE_SUCCESS_UNSPECIFIED`| 正常 — 無錯誤  
`SPOT_CHECK_CODE_LOW_PRICE_TOO_LOW`| `min_price` 過低  
`SPOT_CHECK_CODE_LOW_PRICE_TOO_HIGH`| `min_price` 過高  
`SPOT_CHECK_CODE_HIGH_PRICE_TOO_LOW`| `max_price` 過低  
`SPOT_CHECK_CODE_HIGH_PRICE_TOO_HIGH`| `max_price` 過高  
`SPOT_CHECK_CODE_GRID_NO_TOO_LOW`| `cell_number` 過少  
`SPOT_CHECK_CODE_GRID_NO_TOO_HIGH`| `cell_number` 過多  
`SPOT_CHECK_CODE_INVESTMENT_TOO_LOW`| 投資金額過低  
`SPOT_CHECK_CODE_INVESTMENT_TOO_HIGH`| 投資金額過高  
`SPOT_CHECK_CODE_TP_TOO_LOW`| 止盈價格過低  
`SPOT_CHECK_CODE_TP_TOO_HIGH`| 止盈價格過高  
`SPOT_CHECK_CODE_SL_TOO_LOW`| 止損價格過低  
`SPOT_CHECK_CODE_SL_TOO_HIGH`| 止損價格過高  
`SPOT_CHECK_CODE_EP_TOO_LOW`| 入場價格過低  
`SPOT_CHECK_CODE_EP_TOO_HIGH`| 入場價格過高  
`SPOT_CHECK_CODE_TS_PERCENT_TOO_LOW`| 移動止損百分比過低  
`SPOT_CHECK_CODE_TS_PERCENT_TOO_HIGH`| 移動止損百分比過高  
`SPOT_CHECK_CODE_TP_TOO_LOW_THAN_MARKET`| 止盈價格低於市場價格  
`SPOT_CHECK_CODE_SL_TOO_HIGH_THAN_MARKET`| 止損價格高於市場價格  
`SPOT_CHECK_CODE_LIMIT_UP_PRICE_TOO_LOW`| `limit_up_price` 過低  
`SPOT_CHECK_CODE_LIMIT_UP_PRICE_TOO_HIGH`| `limit_up_price` 過高  
`SPOT_CHECK_CODE_CAN_NOT_ENABLE_TRAILING_UP`| `cell_number < 5`，不允許追蹤  
`SPOT_CHECK_CODE_ENTRY_PRICE_FORBIDDEN_TRAILING_UP`| 入場價格超出網格範圍，不允許追蹤  
`SPOT_CHECK_CODE_LAST_PRICE_FORBIDDEN_TRAILING_UP`| 市場價格超出網格範圍，不允許追蹤  
`SPOT_CHECK_CODE_INVESTMENT_FORBIDDEN_TRAILING_UP`| 投資金額不足以支持追蹤  
  
* * *

### 請求示例
    
    
    POST /v5/grid/validate-input HTTP/1.1  
    Host: api-testnet.bybit.com  
    Content-Type: application/json  
      
    {  
        "symbol": "MNTUSDT",  
        "max_price": "1.2",  
        "min_price": "0.3",  
        "quote_investment": "",  
        "base_investment": "300",  
        "invest_mode": 1,  
        "cell_number": 66,  
        "entry_price": "0.4"  
    }  
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "",  
        "result": {  
            "status_code": 200,  
            "debug_msg": "",  
            "investment": {  
                "from": "0",  
                "to": "0"  
            },  
            "profit": {  
                "from": "0.0114",  
                "to": "0.0453"  
            },  
            "cell_number": {  
                "from": "2",  
                "to": "562"  
            },  
            "min_price": {  
                "from": "0.1568",  
                "to": "3.92"  
            },  
            "max_price": {  
                "from": "0.3012",  
                "to": "40"  
            },  
            "stop_loss": {  
                "from": "0",  
                "to": "0.3"  
            },  
            "take_profit": {  
                "from": "1.2",  
                "to": ""  
            },  
            "entry_price": {  
                "from": "0.2352",  
                "to": "0.784"  
            },  
            "cell_distance": "0.0136",  
            "check_code": "SPOT_CHECK_CODE_SUCCESS_UNSPECIFIED",  
            "base_investment": {  
                "from": "228.36",  
                "to": "1366590.08"  
            },  
            "ts_percent": {  
                "from": "0.03",  
                "to": "0.99"  
            },  
            "limit_up_price": {  
                "from": "1.2112",  
                "to": "3.9065"  
            }  
        },  
        "retExtInfo": {},  
        "time": 1774513367099  
    }