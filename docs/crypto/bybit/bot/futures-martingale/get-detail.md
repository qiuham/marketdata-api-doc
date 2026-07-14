---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/bot/futures-martingale/get-detail
api_type: REST
updated_at: 2026-07-14 18:51:42.349036
---

# Get Grid Bot Detail

Retrieve comprehensive details for a specific spot grid bot, including configuration, status, profit metrics, arbitrage count, TP/SL settings, and close reason.

info

  * **`grid_id`:**  
Obtained from the [Create Spot Grid Bot](/docs/v5/bot/spot-grid/create) response or grid list queries.

  * **APR fields:**  
`grid_apr` and `total_apr` are returned as decimal ratios (e.g. `"0.15"` means 15% APR). Multiply by 100 to convert to percentage.

  * **`current_profit` / `current_per`:**  
Only present for bots in `RUNNING` state.

  * **Rate limit:**  
10 requests per second per UID.




### HTTP Request

POST`/v5/grid/query-grid-detail`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
grid_id| **true**|  string| Grid bot ID to query  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
status_code| integer| Business status code  
debug_msg| string| Debug message (testnet only)  
detail| object| Grid bot detail object (see below)  
> grid_id| integer| Grid bot ID  
> symbol| string| Trading pair (e.g. `BTCUSDT`)  
> base_token| string| Base token symbol (e.g. `BTC`)  
> quote_token| string| Quote token symbol (e.g. `USDT`)  
> status| string| Bot lifecycle status: `RAW`, `REJECTED`, `NEW`, `INITIALIZING`, `RUNNING`, `CANCELLING`, `COMPLETED`  
> max_price| string| Grid upper price bound (decimal string)  
> min_price| string| Grid lower price bound (decimal string)  
> cell_number| integer| Number of active grid intervals  
> total_investment| string| Total investment amount in quote token (decimal string)  
> total_profit| string| Total profit in quote token (decimal string)  
> grid_profit| string| Grid arbitrage profit in quote token (decimal string)  
> grid_apr| string| Grid APR as decimal ratio (e.g. `"0.15"` = 15%)  
> total_apr| string| Total APR as decimal ratio (e.g. `"0.2"` = 20%)  
> arbitrage_num| integer| Total number of completed arbitrage trades  
> arbitrage_num_24| integer| Number of arbitrage trades in the last 24 hours  
> current_price| string| Current market price (decimal string)  
> current_profit| string| Current unrealized P&L for running bots (decimal string)  
> current_per| string| Current P&L as decimal ratio (e.g. `"0.05"` = 5%)  
> equity| string| Current equity in quote token (decimal string)  
> entry_price| string| Entry trigger price if set (decimal string)  
> stop_loss_price| string| Stop-loss price if set (decimal string)  
> take_profit_price| string| Take-profit price if set (decimal string)  
> close_reason| string| Reason for closure: `UNKNOWN`, `CLOSED_MANUALLY`, `CLOSED_FAILED_INITIATION`, `CLOSED_SYMBOL_DELISTED`, `CLOSED_STOP_LOSS`, `CLOSED_TAKE_PROFIT`, `CLOSED_USER_BAN`, `CLOSED_TRAILING_STOP`, `CLOSE_STANDARD_CLEARANCE`, `CLOSE_TAX_TAG_CHANGE`  
> bot_close_code| string| Close code: `Unknown`, `Failed initiation`, `Canceled manually`, `Auto canceled (other)`, `Auto canceled (take-profit)`, `Auto canceled (stop-loss)`, `Trailing stop`  
> ts_percent| string| Trailing stop callback as decimal ratio (e.g. `"0.05"` = 5%)  
> is_support_ts| boolean| Whether the symbol supports trailing stop  
> enable_trailing| boolean| Whether grid trailing is enabled  
> limit_up_price| string| Upper limit price for grid trailing (decimal string)  
> ori_max_price| string| Original max price before trailing shift  
> ori_min_price| string| Original min price before trailing shift  
> ori_cell_number| integer| Original grid count before trailing shift  
> allow_follow| integer| Whether copy-trading is allowed: `1` yes, `0` no  
> follow_num| integer| Number of copy-trade followers  
> operation_time| integer| Milliseconds since bot creation  
> create_time| integer| Creation timestamp (Unix milliseconds)  
> end_time| integer| End timestamp (Unix milliseconds). `0` if still running  
> used_reward_amount| string| Total voucher amount used in quote token (decimal string)  
> settlement_assets| string| Settlement asset information on close  
> account_type| string| Account type: `Unspecified`, `Derivatives account`, `Unified account`, `Account upgrading`, `Spot account`, `UTA account`, `Fund account`  
> cum_withdrew_amount| string| Cumulative withdrawn profit in quote token (decimal string)  
  
* * *

### Request Example
    
    
    POST /v5/grid/query-grid-detail HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1672211928338  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {"grid_id":1234567890}  
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "",  
        "result": {  
            "status_code": 200,  
            "detail": {  
                "grid_id": "612340768081708828",  
                "symbol": "MNTUSDT",  
                "base_token": "MNT",  
                "quote_token": "USDT",  
                "total_investment": "200",  
                "total_profit": "40.4186",  
                "max_price": "1.0968",  
                "min_price": "0.3656",  
                "cell_number": 50,  
                "grid_profit": "61.3113",  
                "grid_apr": "111.893143923675",  
                "total_apr": "73.763945",  
                "arbitrage_num": 291,  
                "arbitrage_num_24": 0,  
                "allow_follow": 1,  
                "operation_time": "986587",  
                "status": "RUNNING",  
                "entry_price": "",  
                "stop_loss_price": "",  
                "take_profit_price": "",  
                "current_price": "0.7279",  
                "close_reason": "UNKNOWN_GridCloseReason",  
                "bot_close_code": "BOT_CLOSE_CODE_UNKNOWN",  
                "follow_num": 0,  
                "create_time": "1774513139000",  
                "end_time": "0",  
                "used_reward_amount": "",  
                "settlement_assets": "",  
                "account_type": "BOT_ACCOUNT_TYPE_FUND",  
                "cum_withdrew_amount": "0",  
                "current_profit": "40.4186",  
                "current_per": "0.202093",  
                "spot_symbol_status": "ONLINE",  
                "used_reward_id": "",  
                "taker_fee_rate": "0.0006",  
                "maker_fee_rate": "0.0004",  
                "equity": "237.412782",  
                "ts_exit_equity": "0",  
                "ts_percent": "0",  
                "is_support_ts": true,  
                "enable_trailing": false,  
                "limit_up_price": "",  
                "ori_max_price": "",  
                "ori_min_price": "",  
                "ori_cell_number": 0  
            },  
            "debug_msg": ""  
        },  
        "retExtInfo": {},  
        "time": 1774514125596  
    }

---

# 查詢網格機器人詳情

查詢指定現貨網格機器人的完整詳情，包括配置、狀態、利潤指標、套利次數、止盈止損設置及關閉原因。

信息

  * **`grid_id`：**  
從[創建現貨網格機器人](/docs/zh-TW/v5/bot/spot-grid/create)響應或網格列表查詢中獲取。

  * **APR 字段：**  
`grid_apr` 和 `total_apr` 以小數比例返回（例如 `"0.15"` 表示 15% APR）。乘以 100 可轉換為百分比。

  * **`current_profit` / `current_per`：**  
僅在機器人為 `RUNNING` 狀態時返回。

  * **頻率限制：**  
每個 UID 每秒最多 10 次請求。




### HTTP請求

POST`/v5/grid/query-grid-detail`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
grid_id| **true**|  string| 要查詢的網格機器人 ID  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
status_code| integer| 業務狀態碼  
debug_msg| string| 調試信息（僅測試網）  
detail| object| 網格機器人詳情對象（詳見下方）  
> grid_id| integer| 網格機器人 ID  
> symbol| string| 交易對名稱（例如 `BTCUSDT`）  
> base_token| string| 基礎幣種（例如 `BTC`）  
> quote_token| string| 報價幣種（例如 `USDT`）  
> status| string| 機器人生命週期狀態：`RAW`、`REJECTED`、`NEW`、`INITIALIZING`、`RUNNING`、`CANCELLING`、`COMPLETED`  
> max_price| string| 網格價格上限（小數字符串）  
> min_price| string| 網格價格下限（小數字符串）  
> cell_number| integer| 活躍網格間隔數量  
> total_investment| string| 報價幣種總投資金額（小數字符串）  
> total_profit| string| 報價幣種總利潤（小數字符串）  
> grid_profit| string| 網格套利利潤，以報價幣種計（小數字符串）  
> grid_apr| string| 網格 APR，小數比例（例如 `"0.15"` = 15%）  
> total_apr| string| 總 APR，小數比例（例如 `"0.2"` = 20%）  
> arbitrage_num| integer| 已完成套利交易總次數  
> arbitrage_num_24| integer| 過去 24 小時套利交易次數  
> current_price| string| 當前市場價格（小數字符串）  
> current_profit| string| 運行中機器人的當前未實現盈虧（小數字符串）  
> current_per| string| 當前盈虧小數比例（例如 `"0.05"` = 5%）  
> equity| string| 報價幣種當前淨值（小數字符串）  
> entry_price| string| 設置的入場觸發價格（小數字符串）  
> stop_loss_price| string| 設置的止損價格（小數字符串）  
> take_profit_price| string| 設置的止盈價格（小數字符串）  
> close_reason| string| 關閉原因：`UNKNOWN`、`CLOSED_MANUALLY`、`CLOSED_FAILED_INITIATION`、`CLOSED_SYMBOL_DELISTED`、`CLOSED_STOP_LOSS`、`CLOSED_TAKE_PROFIT`、`CLOSED_USER_BAN`、`CLOSED_TRAILING_STOP`、`CLOSE_STANDARD_CLEARANCE`、`CLOSE_TAX_TAG_CHANGE`  
> bot_close_code| string| 關閉代碼：`Unknown`、`Failed initiation`、`Canceled manually`、`Auto canceled (other)`、`Auto canceled (take-profit)`、`Auto canceled (stop-loss)`、`Trailing stop`  
> ts_percent| string| 移動止損回撥小數比例（例如 `"0.05"` = 5%）  
> is_support_ts| boolean| 該交易對是否支持移動止損  
> enable_trailing| boolean| 是否啓用網格追蹤  
> limit_up_price| string| 網格追蹤上限價格（小數字符串）  
> ori_max_price| string| 追蹤移動前的原始最高價格  
> ori_min_price| string| 追蹤移動前的原始最低價格  
> ori_cell_number| integer| 追蹤移動前的原始網格數量  
> allow_follow| integer| 是否允許跟單：`1` 是，`0` 否  
> follow_num| integer| 跟單跟隨者數量  
> operation_time| integer| 自機器人創建以來的毫秒數  
> create_time| integer| 創建時間戳（Unix 毫秒）  
> end_time| integer| 結束時間戳（Unix 毫秒），運行中返回 `0`  
> used_reward_amount| string| 已使用的憑證金額，以報價幣種計（小數字符串）  
> settlement_assets| string| 關閉時的資產結算信息  
> account_type| string| 帳戶類型：`Unspecified`、`Derivatives account`、`Unified account`、`Account upgrading`、`Spot account`、`UTA account`、`Fund account`  
> cum_withdrew_amount| string| 累計提取利潤，以報價幣種計（小數字符串）  
  
* * *

### 請求示例
    
    
    POST /v5/grid/query-grid-detail HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1672211928338  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {"grid_id":1234567890}  
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "",  
        "result": {  
            "status_code": 200,  
            "detail": {  
                "grid_id": "612340768081708828",  
                "symbol": "MNTUSDT",  
                "base_token": "MNT",  
                "quote_token": "USDT",  
                "total_investment": "200",  
                "total_profit": "40.4186",  
                "max_price": "1.0968",  
                "min_price": "0.3656",  
                "cell_number": 50,  
                "grid_profit": "61.3113",  
                "grid_apr": "111.893143923675",  
                "total_apr": "73.763945",  
                "arbitrage_num": 291,  
                "arbitrage_num_24": 0,  
                "allow_follow": 1,  
                "operation_time": "986587",  
                "status": "RUNNING",  
                "entry_price": "",  
                "stop_loss_price": "",  
                "take_profit_price": "",  
                "current_price": "0.7279",  
                "close_reason": "UNKNOWN_GridCloseReason",  
                "bot_close_code": "BOT_CLOSE_CODE_UNKNOWN",  
                "follow_num": 0,  
                "create_time": "1774513139000",  
                "end_time": "0",  
                "used_reward_amount": "",  
                "settlement_assets": "",  
                "account_type": "BOT_ACCOUNT_TYPE_FUND",  
                "cum_withdrew_amount": "0",  
                "current_profit": "40.4186",  
                "current_per": "0.202093",  
                "spot_symbol_status": "ONLINE",  
                "used_reward_id": "",  
                "taker_fee_rate": "0.0006",  
                "maker_fee_rate": "0.0004",  
                "equity": "237.412782",  
                "ts_exit_equity": "0",  
                "ts_percent": "0",  
                "is_support_ts": true,  
                "enable_trailing": false,  
                "limit_up_price": "",  
                "ori_max_price": "",  
                "ori_min_price": "",  
                "ori_cell_number": 0  
            },  
            "debug_msg": ""  
        },  
        "retExtInfo": {},  
        "time": 1774514125596  
    }