---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/bot/futures-martingale/get-detail
api_type: REST
updated_at: 2026-11-13 19:22:06.286583
---

# Get Martingale Bot Detail

Retrieve comprehensive details for a specific futures Martingale bot, including configuration, status, PnL metrics, position info, round progress, and timestamps.

info

  * **`bot_id`:**  
Obtained from the [Create Futures Martingale Bot](/docs/v5/bot/futures-martingale/create) response or bot listing endpoints.

  * **Round progress:**  
`completed_rounds` shows how many full Martingale rounds have been executed. `current_round` is the active round. `current_added_pos_num` shows how many position adds have occurred in the current round.

  * **Rate limit:**  
10 requests per second per UID.




### HTTP Request

POST`/v5/fmartingalebot/detail`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
bot_id| **true**|  string| Bot ID to query  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
status_code| integer| `0` = success, non-zero = error  
debug_msg| string| Debug message (testnet only)  
fmart_detail| object| Martingale bot detail object (see below)  
> bot_id| string| Unique Martingale bot ID  
> symbol| string| Trading pair (e.g. `BTCUSDT`)  
> base_token| string| Base coin (e.g. `BTC`)  
> quote_token| string| Quote coin (e.g. `USDT`)  
> bot_display_status| string| UI display status: `Unspecified`, `Initializing`, `Awaiting activation`, `Running`, `Cancelling`, `Completed`  
> fmart_mode| string| Strategy direction: `Unspecified`, `Long`, `Short`  
> leverage| string| Position leverage multiplier (e.g. `"5"` means 5x)  
> actual_leverage| string| Actual effective leverage (e.g. `"4.8"` means 4.8x)  
> single_round_target_profit_per| string| Single round take-profit target as percentage (e.g. `"0.03"` means 3%)  
> add_pos_num| string| User-configured maximum add position count  
> add_pos_per| string| Position add scaling as percentage of base position (e.g. `"1"` = 1x base)  
> price_float_per| string| Price movement trigger as percentage (e.g. `"0.015"` means 1.5%)  
> entry_price| string| Entry trigger price (decimal string). Empty if not set  
> sl_per| string| Stop-loss as percentage (e.g. `"0.2"` means 20%). Empty if not set  
> total_margin| string| Total margin including additional top-ups (decimal string)  
> pnl| string| Cumulative total PnL in quote currency (decimal string)  
> pnl_per| string| Total PnL as percentage of total margin (e.g. `"0.0505"` means 5.05%)  
> realized_pnl| string| Cumulative realized PnL (decimal string)  
> unrealized_pnl| string| Unrealized PnL based on mark price (decimal string)  
> net_funding_fee| string| Cumulative net funding fee (decimal string, positive = received, negative = paid)  
> total_apr| string| Total annualized profit rate as percentage (e.g. `"0.365"` means 36.5% APR)  
> completed_rounds| integer| Number of completed Martingale rounds  
> current_round| integer| Current round number  
> current_added_pos_num| integer| Number of position adds in current round  
> pos_size| string| Current position size in contracts (decimal string)  
> avg_pos_price| string| Average position entry price (decimal string)  
> pos_balance| string| Position margin balance (decimal string)  
> order_balance| string| Margin locked in pending orders (decimal string)  
> available_balance| string| Available (free) margin balance (decimal string)  
> mark_price| string| Current mark price  
> current_price| string| Current market price  
> estimated_liq_price| string| Estimated liquidation price  
> auto_cycle| string| Auto-cycle mode: `Unspecified`, `Enabled`, `Disabled`  
> stop_type| string| Stop reason: `Unspecified`, `Init failure`, `User stopped`, `Liquidation`, `Symbol delisted`, `Stop-loss triggered`, `System stopped`, `User banned`, `Single round take-profit (auto-cycle off)`, `Insufficient order balance`, `Reduce-only`, `Bankruptcy price breach`, `Negative arbitrage`, `Compliance clearance`, `ADL (Auto-Deleveraging)`  
> close_code| string| UI close code: `Unspecified`, `Failed initiation`, `Canceled manually by user`, `Canceled automatically (other)`, `Canceled by take-profit trigger`, `Canceled by stop-loss trigger`, `Canceled by liquidation`, `DCA reached max investment`, `User account banned`, `Neutral grid hit top price`, `Neutral grid hit bottom price`, `Martingale round take-profit triggered`, `Symbol delisted`, `Negative arbitrage`, `Compliance clearance`, `ADL (Auto-Deleveraging)`  
> close_price| string| Actual price when bot was stopped  
> tick_size| string| Minimum price increment  
> settlement_assets| string| Settlement asset transfer details  
> follow_num| integer| Number of users copying this bot  
> used_reward_amount| string| Total voucher/reward amount used  
> used_reward_id| string| ID of the first insurance voucher used  
> total_bonus| string| Total bonus amount  
> operation_time| string| seconds since bot creation  
> create_time| string| Bot creation timestamp (Unix seconds)  
> modify_time| string| Last update timestamp (Unix seconds)  
> end_time| string| Bot end timestamp (Unix seconds), `0` if still running  
> running_duration| string| Running duration in seconds  
> adl_rank_indicator| integer| ADL (Auto-Deleveraging) rank indicator  
  
* * *

### Request Example
    
    
    POST /v5/fmartingalebot/detail HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1672211928338  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "bot_id": "612335724699611830"  
    }  
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "success",  
        "result": {  
            "status_code": 0,  
            "debug_msg": "",  
            "fmart_detail": {  
                "bot_id": "612335724699611830",  
                "symbol": "MNTUSDT",  
                "bot_display_status": "F_MART_BOT_DISPLAY_STATUS_RUNNING",  
                "fmart_mode": "F_MART_MODE_MARTINGALE_MODE_LONG",  
                "base_token": "MNT",  
                "quote_token": "USDT",  
                "leverage": "5",  
                "single_round_target_profit_per": "0.1",  
                "add_pos_num": "5",  
                "add_pos_per": "1.8",  
                "price_float_per": "0.16",  
                "entry_price": "0.7039",  
                "sl_per": "0.5",  
                "total_margin": "1000",  
                "pnl": "1.41687",  
                "pnl_per": "0.0014",  
                "realized_pnl": "-0.02684394",  
                "unrealized_pnl": "1.44372",  
                "completed_rounds": 0,  
                "current_round": 1,  
                "current_added_pos_num": 1,  
                "pos_size": "136.2",  
                "avg_pos_price": "0.7039",  
                "pos_balance": "19.36433252",  
                "order_balance": "34.68510157",  
                "available_balance": "946.66328797",  
                "mark_price": "0.70966",  
                "estimated_liq_price": "0",  
                "actual_leverage": "4.64",  
                "auto_cycle": "AUTO_CYCLE_TOGGLE_AUTO_CYCLE_TOGGLE_UNKNOWN_UNSPECIFIED",  
                "operation_time": "56",  
                "create_time": "1774510133",  
                "modify_time": "1774510133",  
                "end_time": "1774510133",  
                "stop_type": "F_MART_BOT_STOP_TYPE_STOP_TYPE_UNKNOWN_UNSPECIFIED",  
                "settlement_assets": "",  
                "tick_size": "0.0001",  
                "close_price": "0",  
                "current_price": "0.7145",  
                "running_duration": "56",  
                "close_code": "BOT_CLOSE_CODE_FAILED_INITIATION",  
                "net_funding_fee": "0",  
                "total_apr": "0.511",  
                "follow_num": 0,  
                "used_reward_amount": "",  
                "used_reward_id": "",  
                "total_bonus": "0",  
                "adl_rank_indicator": 2  
            }  
        },  
        "retExtInfo": {},  
        "time": 1774510189737  
    }

---

# 查詢馬丁格爾機器人詳情

查詢指定合約馬丁格爾機器人的完整詳情，包括配置、狀態、盈虧指標、倉位信息、輪次進度及時間戳。

信息

  * **`bot_id`：**  
從[創建合約馬丁格爾機器人](/docs/zh-TW/v5/bot/futures-martingale/create)響應或機器人列表端點中獲取。

  * **輪次進度：**  
`completed_rounds` 顯示已完成的馬丁格爾輪次數。`current_round` 為當前活躍輪次。`current_added_pos_num` 顯示當前輪次已追加倉位的次數。

  * **頻率限制：**  
每個 UID 每秒最多 10 次請求。




### HTTP請求

POST`/v5/fmartingalebot/detail`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
bot_id| **true**|  string| 要查詢的機器人 ID  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
status_code| integer| `0` = 成功，非零 = 錯誤  
debug_msg| string| 調試信息（僅測試網）  
fmart_detail| object| 馬丁格爾機器人詳情對象（詳見下方）  
> bot_id| string| 唯一馬丁格爾機器人 ID  
> symbol| string| 交易對名稱（例如 `BTCUSDT`）  
> base_token| string| 基礎幣種（例如 `BTC`）  
> quote_token| string| 報價幣種（例如 `USDT`）  
> bot_display_status| string| UI 顯示狀態：`Unspecified`、`Initializing`、`Awaiting activation`、`Running`、`Cancelling`、`Completed`  
> fmart_mode| string| 策略方向：`Unspecified`、`Long`、`Short`  
> leverage| string| 倉位槓桿倍數（例如 `"5"` 表示 5 倍）  
> actual_leverage| string| 實際有效槓桿（例如 `"4.8"` 表示 4.8 倍）  
> single_round_target_profit_per| string| 單輪止盈目標百分比（例如 `"0.03"` 表示 3%）  
> add_pos_num| string| 用戶設定的最大追加倉位次數  
> add_pos_per| string| 追加倉位規模，以基礎倉位百分比計（例如 `"1"` = 1 倍基礎倉位）  
> price_float_per| string| 觸發追加倉位的價格變動百分比（例如 `"0.015"` 表示 1.5%）  
> entry_price| string| 入場觸發價格（小數字符串）。未設置則為空  
> sl_per| string| 止損百分比（例如 `"0.2"` 表示 20%）。未設置則為空  
> total_margin| string| 總保證金（含追加投資，小數字符串）  
> pnl| string| 累計總盈虧，以報價幣種計（小數字符串）  
> pnl_per| string| 總盈虧佔總保證金的百分比（例如 `"0.0505"` 表示 5.05%）  
> realized_pnl| string| 累計已實現盈虧（小數字符串）  
> unrealized_pnl| string| 基於標記價格的未實現盈虧（小數字符串）  
> net_funding_fee| string| 累計淨資金費（小數字符串，正值 = 收入，負值 = 支出）  
> total_apr| string| 總年化收益率百分比（例如 `"0.365"` 表示 36.5% APR）  
> completed_rounds| integer| 已完成的馬丁格爾輪次數  
> current_round| integer| 當前輪次編號  
> current_added_pos_num| integer| 當前輪次已追加倉位的次數  
> pos_size| string| 當前持倉合約數量（小數字符串）  
> avg_pos_price| string| 平均持倉入場價格（小數字符串）  
> pos_balance| string| 倉位保證金餘額（小數字符串）  
> order_balance| string| 掛單鎖定保證金（小數字符串）  
> available_balance| string| 可用（空閒）保證金餘額（小數字符串）  
> mark_price| string| 當前標記價格  
> current_price| string| 當前市場價格  
> estimated_liq_price| string| 預估強平價格  
> auto_cycle| string| 自動循環模式：`Unspecified`、`Enabled`、`Disabled`  
> stop_type| string| 停止原因：`Unspecified`、`Init failure`、`User stopped`、`Liquidation`、`Symbol delisted`、`Stop-loss triggered`、`System stopped`、`User banned`、`Single round take-profit (auto-cycle off)`、`Insufficient order balance`、`Reduce-only`、`Bankruptcy price breach`、`Negative arbitrage`、`Compliance clearance`、`ADL (Auto-Deleveraging)`  
> close_code| string| UI 關閉代碼：`Unspecified`、`Failed initiation`、`Canceled manually by user`、`Canceled automatically (other)`、`Canceled by take-profit trigger`、`Canceled by stop-loss trigger`、`Canceled by liquidation`、`DCA reached max investment`、`User account banned`、`Neutral grid hit top price`、`Neutral grid hit bottom price`、`Martingale round take-profit triggered`、`Symbol delisted`、`Negative arbitrage`、`Compliance clearance`、`ADL (Auto-Deleveraging)`  
> close_price| string| 機器人停止時的實際價格  
> tick_size| string| 最小價格增量  
> settlement_assets| string| 結算資產轉移詳情  
> follow_num| integer| 跟單此機器人的用戶數量  
> used_reward_amount| string| 已使用的憑證/獎勵總金額  
> used_reward_id| string| 首個使用的保險憑證 ID  
> total_bonus| string| 總獎勵金額  
> operation_time| string| 自機器人創建以來的秒數  
> create_time| string| 機器人創建時間戳（Unix 秒）  
> modify_time| string| 最後更新時間戳（Unix 秒）  
> end_time| string| 機器人結束時間戳（Unix 秒），運行中返回 `0`  
> running_duration| string| 運行時長（秒）  
> adl_rank_indicator| integer| ADL（自動減倉）排名指標  
  
* * *

### 請求示例
    
    
    POST /v5/fmartingalebot/detail HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1672211928338  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "bot_id": "612335724699611830"  
    }  
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "success",  
        "result": {  
            "status_code": 0,  
            "debug_msg": "",  
            "fmart_detail": {  
                "bot_id": "612335724699611830",  
                "symbol": "MNTUSDT",  
                "bot_display_status": "F_MART_BOT_DISPLAY_STATUS_RUNNING",  
                "fmart_mode": "F_MART_MODE_MARTINGALE_MODE_LONG",  
                "base_token": "MNT",  
                "quote_token": "USDT",  
                "leverage": "5",  
                "single_round_target_profit_per": "0.1",  
                "add_pos_num": "5",  
                "add_pos_per": "1.8",  
                "price_float_per": "0.16",  
                "entry_price": "0.7039",  
                "sl_per": "0.5",  
                "total_margin": "1000",  
                "pnl": "1.41687",  
                "pnl_per": "0.0014",  
                "realized_pnl": "-0.02684394",  
                "unrealized_pnl": "1.44372",  
                "completed_rounds": 0,  
                "current_round": 1,  
                "current_added_pos_num": 1,  
                "pos_size": "136.2",  
                "avg_pos_price": "0.7039",  
                "pos_balance": "19.36433252",  
                "order_balance": "34.68510157",  
                "available_balance": "946.66328797",  
                "mark_price": "0.70966",  
                "estimated_liq_price": "0",  
                "actual_leverage": "4.64",  
                "auto_cycle": "AUTO_CYCLE_TOGGLE_AUTO_CYCLE_TOGGLE_UNKNOWN_UNSPECIFIED",  
                "operation_time": "56",  
                "create_time": "1774510133",  
                "modify_time": "1774510133",  
                "end_time": "1774510133",  
                "stop_type": "F_MART_BOT_STOP_TYPE_STOP_TYPE_UNKNOWN_UNSPECIFIED",  
                "settlement_assets": "",  
                "tick_size": "0.0001",  
                "close_price": "0",  
                "current_price": "0.7145",  
                "running_duration": "56",  
                "close_code": "BOT_CLOSE_CODE_FAILED_INITIATION",  
                "net_funding_fee": "0",  
                "total_apr": "0.511",  
                "follow_num": 0,  
                "used_reward_amount": "",  
                "used_reward_id": "",  
                "total_bonus": "0",  
                "adl_rank_indicator": 2  
            }  
        },  
        "retExtInfo": {},  
        "time": 1774510189737  
    }