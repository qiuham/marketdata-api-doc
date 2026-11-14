---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/bot/spot-grid/create
api_type: REST
updated_at: 2026-11-13 19:22:06.364404
---

# Create Grid Bot

Create a new spot grid trading bot with a specified trading pair, price range, grid count, and investment amount.

info

  * **Prerequisites:**  
Call [Validate Spot Grid Input](/docs/v5/bot/spot-grid/validate-input) before this endpoint to ensure parameters are within valid ranges.  
User must be authenticated and pass KYC/compliance checks.

  * **Investment mode (`invest_mode`):**  
`0`: Quote only (default) — invest in quote token (e.g. USDT)  
`1`: Base only — invest in base token (e.g. BTC)  
`2`: Base + Quote — split investment across both tokens

  * **Grid trailing (`enable_trailing`):**  
When enabled, the grid automatically shifts as price moves. Requires `cell_number >= 5`.

  * **Response`grid_id`:**  
Returned on success. Use this ID for subsequent [Get Detail](/docs/v5/bot/spot-grid/get-detail) and [Close](/docs/v5/bot/spot-grid/close) operations.

  * **Rate limit:**  
3 requests per second per UID.

  * **Subject to compliance wall and KYC verification.**  
If the user is banned (status_code=421), `ban_reason_text` provides a localized explanation.




### HTTP Request

POST`/v5/grid/create-grid`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
symbol| **true**|  string| Trading pair symbol, uppercase only (e.g. `BTCUSDT`)  
max_price| **true**|  string| Upper bound of the grid price range (decimal string)  
min_price| **true**|  string| Lower bound of the grid price range (decimal string)  
cell_number| **true**|  integer| Number of grid intervals, minimum 2  
invest_mode| false| integer| Investment mode. `0`: Quote only (default), `1`: Base only, `2`: Base + Quote  
base_investment| false| string| Investment in base token (decimal string). **Required** when `invest_mode` is `1` or `2`  
quote_investment| false| string| Investment in quote token (decimal string). **Required** when `invest_mode` is `0` or `2`  
entry_price| false| string| Entry trigger price (decimal string). Bot activates when market price reaches this level  
stop_loss_price| false| string| Stop-loss trigger price (decimal string)  
take_profit_price| false| string| Take-profit trigger price (decimal string)  
ts_percent| false| string| Trailing stop callback ratio, range `[0, 0.99]` (e.g. `"0.05"` means 5%)  
enable_trailing| false| boolean| Enable grid trailing (auto-shift). Requires `cell_number >= 5`. Default: `false`  
limit_up_price| false| string| Upper limit price for grid trailing (decimal string), usd when "enable_trailing"=`true`  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
status_code| integer| `200` = success, `421` = user banned  
grid_id| integer| Created grid bot ID. Use for subsequent queries and close operations  
ban_reason_text| string| Ban reason in user's locale. Returned only when `status_code=421`  
debug_msg| string| Debug message (testnet only)  
  
* * *

### Request Example
    
    
    POST /v5/grid/create-grid HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1672211928338  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "symbol": "MNTUSDT",  
        "max_price": "1.0968",  
        "min_price": "0.3656",  
        "quote_investment": "200",  
        "base_investment": "",  
        "invest_mode": 0,  
        "cell_number": 50  
    }  
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "",  
        "result": {  
            "status_code": 200,  
            "debug_msg": "",  
            "grid_id": "612340768081708828",  
            "ban_reason_text": ""  
        },  
        "retExtInfo": {},  
        "time": 1774513139729  
    }

---

# 創建網格機器人

創建一個新的現貨網格交易機器人，指定交易對、價格範圍、網格數量及投資金額。

信息

  * **前置條件：**  
在調用本端點前，請先調用[驗證現貨網格輸入](/docs/zh-TW/v5/bot/spot-grid/validate-input)，確保參數在有效範圍內。  
用戶必須完成身份驗證及 KYC 合規審核。

  * **投資模式（`invest_mode`）：**  
`0`：僅報價幣（默認）— 以報價幣種投資（例如 USDT）  
`1`：僅基礎幣 — 以基礎幣種投資（例如 BTC）  
`2`：基礎幣 + 報價幣 — 跨兩種幣種分配投資

  * **網格追蹤（`enable_trailing`）：**  
啓用後，網格隨價格自動移動。要求 `cell_number >= 5`。

  * **響應`grid_id`：**  
成功時返回，用於後續[查詢詳情](/docs/zh-TW/v5/bot/spot-grid/get-detail)和[關閉](/docs/zh-TW/v5/bot/spot-grid/close)操作。

  * **頻率限制：**  
每個 UID 每秒最多 3 次請求。

  * **受合規管控及 KYC 驗證約束。**  
若用戶被封禁（status_code=421），`ban_reason_text` 提供本地化說明。




### HTTP請求

POST`/v5/grid/create-grid`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
symbol| **true**|  string| 交易對名稱，僅大寫（例如 `BTCUSDT`）  
max_price| **true**|  string| 網格價格範圍上限（小數字符串）  
min_price| **true**|  string| 網格價格範圍下限（小數字符串）  
cell_number| **true**|  integer| 網格間隔數量，最小為 2  
invest_mode| false| integer| 投資模式。`0`：僅報價幣（默認），`1`：僅基礎幣，`2`：基礎幣+報價幣  
base_investment| false| string| 基礎幣種投資金額（小數字符串）。`invest_mode` 為 `1` 或 `2` 時**必填**  
quote_investment| false| string| 報價幣種投資金額（小數字符串）。`invest_mode` 為 `0` 或 `2` 時**必填**  
entry_price| false| string| 入場觸發價格（小數字符串），市場價格到達此水平時機器人啓動  
stop_loss_price| false| string| 止損觸發價格（小數字符串）  
take_profit_price| false| string| 止盈觸發價格（小數字符串）  
ts_percent| false| string| 移動止損回撥比例，範圍 `[0, 0.99]`（例如 `"0.05"` 表示 5%）  
enable_trailing| false| boolean| 啓用網格追蹤（自動移動）。要求 `cell_number >= 5`。默認：`false`  
limit_up_price| false| string| 網格追蹤上限價格（小數字符串），`enable_trailing`=`true` 時使用  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
status_code| integer| `200` = 成功，`421` = 用戶被封禁  
grid_id| integer| 已創建的網格機器人 ID，用於後續查詢和關閉操作  
ban_reason_text| string| 用戶語言的封禁原因，僅當 `status_code=421` 時返回  
debug_msg| string| 調試信息（僅測試網）  
  
* * *

### 請求示例
    
    
    POST /v5/grid/create-grid HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1672211928338  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "symbol": "MNTUSDT",  
        "max_price": "1.0968",  
        "min_price": "0.3656",  
        "quote_investment": "200",  
        "base_investment": "",  
        "invest_mode": 0,  
        "cell_number": 50  
    }  
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "",  
        "result": {  
            "status_code": 200,  
            "debug_msg": "",  
            "grid_id": "612340768081708828",  
            "ban_reason_text": ""  
        },  
        "retExtInfo": {},  
        "time": 1774513139729  
    }