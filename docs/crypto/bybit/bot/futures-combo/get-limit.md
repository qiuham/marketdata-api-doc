---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/bot/futures-combo/get-limit
api_type: REST
updated_at: 2026-07-01 19:26:54.588331
---

# Get Grid Bot Detail

Retrieve comprehensive details for a specific futures grid bot, including configuration, status, PnL metrics, position info, margin balances, and timestamps.

info

  * **`bot_id`:**  
Obtained from the [Create Futures Grid Bot](/docs/v5/bot/futures-grid/create) response or bot listing endpoints.

  * **PnL fields:**  
`pnl` is the total cumulative PnL. `grid_profit` covers only grid trade profit. `realised_pnl` and `unrealised_pnl` break down the total PnL further.

  * **Rate limit:**  
10 requests per second per UID.




### HTTP Request

POST`/v5/fgridbot/detail`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
bot_id| **true**|  string| Bot ID to query  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
status_code| integer| `0` = success, non-zero = error  
debug_msg| string| Debug message (testnet only)  
detail| object| Grid bot detail object (see below)  
> bot_id| string| Unique grid bot ID  
> symbol| string| Trading pair (e.g. `BTCUSDT`)  
> base_token| string| Base coin (e.g. `BTC`)  
> quote_token| string| Quote coin (e.g. `USDT`)  
> status| string| Bot lifecycle status: `Unspecified`, `Rejected`, `New`, `Initializing`, `Running`, `Cancelling`, `Completed`, `Await activation`  
> grid_mode| string| Strategy direction: `Unspecified`, `Neutral`, `Long`, `Short`  
> grid_type| string| Grid spacing type: `Unspecified`, `Arithmetic`, `Geometric`  
> min_price| string| Grid lower price bound (decimal string)  
> max_price| string| Grid upper price bound (decimal string)  
> cell_number| integer| Number of grid levels  
> leverage| string| Initial leverage multiplier (e.g. `"5"` means 5x)  
> real_leverage| string| Actual effective leverage (e.g. `"4.8"` means 4.8x)  
> total_investment| string| Total investment including additional top-ups (decimal string)  
> total_value| string| Total position value in quote currency (decimal string)  
> current_position| string| Current position size in contracts (decimal string)  
> pnl| string| Cumulative total PnL in quote currency (decimal string)  
> pnl_per| string| PnL as percentage of total investment (e.g. `"0.0505"` means 5.05%)  
> grid_profit| string| Profit from grid trades only (decimal string)  
> grid_apr| string| Annualized grid profit rate as percentage (e.g. `"0.365"` means 36.5% APR)  
> total_apr| string| Total annualized profit rate as percentage (e.g. `"0.42"` means 42% APR)  
> realised_pnl| string| Cumulative realized PnL (decimal string)  
> unrealised_pnl| string| Unrealized PnL based on mark price (decimal string)  
> funding_fee| string| Cumulative funding fee (decimal string, positive = received, negative = paid)  
> position_balance| string| Position margin balance (decimal string)  
> available_balance| string| Available (free) margin balance (decimal string)  
> total_order_balance| string| Margin locked in pending orders (decimal string)  
> equity| string| Running equity value (decimal string)  
> last_price| string| Current last traded price  
> mark_price| string| Current mark price  
> liquidation_price| string| Estimated liquidation price  
> stop_loss_per| string| Stop-loss as percentage (e.g. `"0.1"` means 10%)  
> take_profit_per| string| Take-profit as percentage (e.g. `"0.2"` means 20%)  
> stop_loss_price| string| Stop-loss price  
> take_profit_price| string| Take-profit price  
> tp_sl_type| string| TP/SL trigger mode: `Unspecified`, `Both %`, `Both price`, `TP price+SL %`, `TP %+SL price`  
> entry_price| string| Entry trigger price  
> real_close_price| string| Actual price when bot was stopped  
> min_price_precision| string| Minimum price precision for the symbol  
> tick_size| string| Tick size — minimum price increment  
> trailing_stop_per| string| Trailing stop callback as percentage (e.g. `"0.05"` means 5%)  
> trailing_stop_exit_equity| string| Equity at trailing stop exit (decimal string)  
> close_reason| string| `Unspecified`, `Init failure`, `User stopped`, `Take-profit triggered`, `Insufficient order balance`, `Liquidation`, `Contract delisted`, `FBU trigger failed`, `Asset transfer failed`, `Stop-loss triggered`, `Reduce-only`, `Risk limit`, `System anomaly — fallback stop`, `Close price worse than bankruptcy price`, `User banned`, `Neutral grid hit top price`, `Neutral grid hit bottom price`, `CopyTrade master stopped`, `CopyTrade follower insufficient balance`, `CopyTrade bad entry timing`, `Negative arbitrage`, `Trailing stop`, `Compliance clearance`, `ADL (Auto-Deleveraging)`  
> bot_close_code| string| `Unspecified`, `Failed initiation`, `Canceled manually by user`, `Canceled automatically (other)`, `Canceled by take-profit trigger`, `Canceled by stop-loss trigger`, `Canceled by liquidation`, `DCA reached max investment`, `User account banned`, `Neutral grid hit top price`, `Neutral grid hit bottom price`, `Martingale round take-profit triggered`, `Symbol delisted`, `Negative arbitrage`, `Trailing stop exit`, `Compliance clearance`, `ADL (Auto-Deleveraging)`  
> futures_pos_side| string| `Unspecified`, `Short position`, `Long position`  
> arbitrage_num| integer| Total arbitrage (grid fill) count  
> arbitrage_num_24| integer| Arbitrage count in last 24 hours  
> min_profit| string| Minimum per-grid profit rate as percentage  
> max_profit| string| Maximum per-grid profit rate as percentage  
> move_up_price| string| Move-up max price for grid shifting  
> move_down_price| string| Move-down min price for grid shifting  
> curr_min_price| string| Current effective minimum grid price  
> curr_max_price| string| Current effective maximum grid price  
> i_m_rate| string| Initial margin rate as decimal ratio (e.g. `"0.1"` = 10%)  
> m_m_rate| string| Maintenance margin rate as decimal ratio (e.g. `"0.005"` = 0.5%)  
> account_type| string| `Unspecified`, `Derivative account`, `Unified margin account`, `Account upgrading`, `Spot account`, `UTA (Unified Trading Account)`, `Fund account`  
> allow_follow| integer| Whether copy-trading is allowed: `1` yes, `0` no  
> follow_num| integer| Number of users copying this bot  
> copy_trade_is_master| boolean| Whether this bot is a copy-trade master  
> copy_trade_follower_num| string| Number of copy-trade followers  
> used_reward_amount| string| Total voucher/reward amount used  
> used_reward_id| string| ID of the first insurance voucher used  
> init_bonus| string| Initial bonus amount  
> used_bonus_amount| string| Bonus amount already consumed  
> settlement_assets| string| Settlement asset info  
> cum_withdrew_amount| string| Cumulative withdrawn margin amount  
> current_profit| string| Current running PnL (decimal string)  
> current_per| string| Current running PnL as percentage (e.g. `"0.032"` means 3.2%)  
> taker_fee_rate| string| Taker fee rate as decimal ratio (e.g. `"0.0006"` = 0.06%)  
> maker_fee_rate| string| Maker fee rate as decimal ratio (e.g. `"0.0001"` = 0.01%)  
> operation_time| string| Milliseconds since bot creation  
> create_time| string| Bot creation timestamp (Unix milliseconds)  
> modify_time| string| Last update timestamp (Unix milliseconds)  
> end_time| string| Bot end timestamp (Unix milliseconds), `0` if still running  
> adl_rank_indicator| integer| ADL (Auto-Deleveraging) rank indicator  
  
* * *

### Request Example
    
    
    POST /v5/fgridbot/detail HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1672211928338  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "bot_id": "612330315406398322"  
    }  
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "success",  
        "result": {  
            "status_code": 0,  
            "detail": {  
                "bot_id": "612330315406398322",  
                "symbol": "BTCUSDT",  
                "status": "FUTURE_GRID_STATUS_COMPLETED",  
                "base_token": "BTC",  
                "quote_token": "USDT",  
                "min_price": "230000",  
                "max_price": "800000",  
                "cell_number": 88,  
                "grid_type": "FUTURE_GRID_TYPE_GEOMETRIC",  
                "grid_mode": "FUTURE_GRID_MODE_LONG",  
                "stop_loss_per": "",  
                "take_profit_per": "0.28",  
                "real_leverage": "6",  
                "total_investment": "950",  
                "total_value": "",  
                "current_position": "",  
                "arbitrage_num": 0,  
                "arbitrage_num_24": 0,  
                "pnl": "0",  
                "pnl_per": "0.0000",  
                "grid_profit": "0",  
                "grid_apr": "0",  
                "total_apr": "0",  
                "last_price": "",  
                "liquidation_price": "",  
                "realised_pnl": "",  
                "unrealised_pnl": "",  
                "funding_fee": "",  
                "position_balance": "",  
                "available_balance": "",  
                "total_order_balance": "",  
                "close_reason": "F_GRID_BOT_STOP_TYPE_TRIGGER_FBU_FAIL",  
                "allow_follow": 1,  
                "operation_time": "1110",  
                "create_time": "1774506909414",  
                "modify_time": "1774506910524",  
                "end_time": "1774506910522",  
                "min_profit": "8.1959",  
                "max_profit": "8.1959",  
                "leverage": "6",  
                "mark_price": "",  
                "bot_close_code": "BOT_CLOSE_CODE_FAILED_INITIATION",  
                "futures_pos_side": "FUTURES_POSITION_SIDE_UNSPECIFIED",  
                "follow_num": 0,  
                "entry_price": "370000",  
                "stop_loss_price": "200000",  
                "take_profit_price": "",  
                "tp_sl_type": "TP_SL_TYPE_TP_PERCENT_SL_PRICE",  
                "real_close_price": "",  
                "min_price_precision": "0.01",  
                "tick_size": "0.10",  
                "used_reward_amount": "",  
                "settlement_assets": "950 USDT",  
                "account_type": "BOT_ACCOUNT_TYPE_FUND",  
                "cum_withdrew_amount": "0",  
                "current_profit": "",  
                "current_per": "",  
                "copy_trade_is_master": false,  
                "copy_trade_follower_num": "0",  
                "init_bonus": "0",  
                "used_bonus_amount": "",  
                "used_reward_id": "",  
                "taker_fee_rate": "0.00028",  
                "maker_fee_rate": "0.0001",  
                "equity": "0",  
                "trailing_stop_exit_equity": "0",  
                "trailing_stop_per": "0.18",  
                "i_m_rate": "",  
                "m_m_rate": "",  
                "move_up_price": "",  
                "move_down_price": "",  
                "curr_min_price": "",  
                "curr_max_price": "",  
                "adl_rank_indicator": 0  
            },  
            "debug_msg": ""  
        },  
        "retExtInfo": {},  
        "time": 1774508203378  
    }

---

# 查詢網格機器人詳情

查詢指定合約網格機器人的完整詳情，包括配置、狀態、盈虧指標、倉位信息、保證金餘額及時間戳。

信息

  * **`bot_id`：**  
從[創建合約網格機器人](/docs/zh-TW/v5/bot/futures-grid/create)響應或機器人列表端點中獲取。

  * **盈虧字段：**  
`pnl` 為累計總盈虧。`grid_profit` 僅涵蓋網格交易利潤。`realised_pnl` 和 `unrealised_pnl` 進一步細分總盈虧。

  * **頻率限制：**  
每個 UID 每秒最多 10 次請求。




### HTTP請求

POST`/v5/fgridbot/detail`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
bot_id| **true**|  string| 要查詢的機器人 ID  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
status_code| integer| `0` = 成功，非零 = 錯誤  
debug_msg| string| 調試信息（僅測試網）  
detail| object| 網格機器人詳情對象（詳見下方）  
> bot_id| string| 唯一網格機器人 ID  
> symbol| string| 交易對名稱（例如 `BTCUSDT`）  
> base_token| string| 基礎幣種（例如 `BTC`）  
> quote_token| string| 報價幣種（例如 `USDT`）  
> status| string| 機器人生命週期狀態：`Unspecified`、`Rejected`、`New`、`Initializing`、`Running`、`Cancelling`、`Completed`、`Await activation`  
> grid_mode| string| 策略方向：`Unspecified`、`Neutral`、`Long`、`Short`  
> grid_type| string| 網格間距類型：`Unspecified`、`Arithmetic`、`Geometric`  
> min_price| string| 網格價格下限（小數字符串）  
> max_price| string| 網格價格上限（小數字符串）  
> cell_number| integer| 網格層數  
> leverage| string| 初始槓桿倍數（例如 `"5"` 表示 5 倍）  
> real_leverage| string| 實際有效槓桿（例如 `"4.8"` 表示 4.8 倍）  
> total_investment| string| 總投資金額，含追加投入（小數字符串）  
> total_value| string| 總倉位價值，以報價幣種計（小數字符串）  
> current_position| string| 當前持倉合約數量（小數字符串）  
> pnl| string| 累計總盈虧，以報價幣種計（小數字符串）  
> pnl_per| string| 盈虧佔總投資的百分比（例如 `"0.0505"` 表示 5.05%）  
> grid_profit| string| 僅網格交易利潤（小數字符串）  
> grid_apr| string| 網格利潤年化收益率百分比（例如 `"0.365"` 表示 36.5% APR）  
> total_apr| string| 總年化收益率百分比（例如 `"0.42"` 表示 42% APR）  
> realised_pnl| string| 累計已實現盈虧（小數字符串）  
> unrealised_pnl| string| 基於標記價格的未實現盈虧（小數字符串）  
> funding_fee| string| 累計資金費（小數字符串，正值 = 收入，負值 = 支出）  
> position_balance| string| 倉位保證金餘額（小數字符串）  
> available_balance| string| 可用（空閒）保證金餘額（小數字符串）  
> total_order_balance| string| 掛單鎖定保證金（小數字符串）  
> equity| string| 當前淨值（小數字符串）  
> last_price| string| 當前最新成交價格  
> mark_price| string| 當前標記價格  
> liquidation_price| string| 預估強平價格  
> stop_loss_per| string| 止損百分比（例如 `"0.1"` 表示 10%）  
> take_profit_per| string| 止盈百分比（例如 `"0.2"` 表示 20%）  
> stop_loss_price| string| 止損價格  
> take_profit_price| string| 止盈價格  
> tp_sl_type| string| 止盈止損觸發模式：`Unspecified`、`Both %`、`Both price`、`TP price+SL %`、`TP %+SL price`  
> entry_price| string| 入場觸發價格  
> real_close_price| string| 機器人停止時的實際價格  
> min_price_precision| string| 該交易對的最小價格精度  
> tick_size| string| 最小價格增量  
> trailing_stop_per| string| 移動止損回撥百分比（例如 `"0.05"` 表示 5%）  
> trailing_stop_exit_equity| string| 移動止損退出時的淨值（小數字符串）  
> close_reason| string| `Unspecified`、`Init failure`、`User stopped`、`Take-profit triggered`、`Insufficient order balance`、`Liquidation`、`Contract delisted`、`FBU trigger failed`、`Asset transfer failed`、`Stop-loss triggered`、`Reduce-only`、`Risk limit`、`System anomaly — fallback stop`、`Close price worse than bankruptcy price`、`User banned`、`Neutral grid hit top price`、`Neutral grid hit bottom price`、`CopyTrade master stopped`、`CopyTrade follower insufficient balance`、`CopyTrade bad entry timing`、`Negative arbitrage`、`Trailing stop`、`Compliance clearance`、`ADL (Auto-Deleveraging)`  
> bot_close_code| string| `Unspecified`、`Failed initiation`、`Canceled manually by user`、`Canceled automatically (other)`、`Canceled by take-profit trigger`、`Canceled by stop-loss trigger`、`Canceled by liquidation`、`DCA reached max investment`、`User account banned`、`Neutral grid hit top price`、`Neutral grid hit bottom price`、`Martingale round take-profit triggered`、`Symbol delisted`、`Negative arbitrage`、`Trailing stop exit`、`Compliance clearance`、`ADL (Auto-Deleveraging)`  
> futures_pos_side| string| `Unspecified`、`Short position`、`Long position`  
> arbitrage_num| integer| 總套利（網格成交）次數  
> arbitrage_num_24| integer| 過去 24 小時套利次數  
> min_profit| string| 最低每格利潤率百分比  
> max_profit| string| 最高每格利潤率百分比  
> move_up_price| string| 網格移動的最高上限價格  
> move_down_price| string| 網格移動的最低下限價格  
> curr_min_price| string| 當前有效網格最低價格  
> curr_max_price| string| 當前有效網格最高價格  
> i_m_rate| string| 初始保證金率（小數比例，例如 `"0.1"` = 10%）  
> m_m_rate| string| 維持保證金率（小數比例，例如 `"0.005"` = 0.5%）  
> account_type| string| `Unspecified`、`Derivative account`、`Unified margin account`、`Account upgrading`、`Spot account`、`UTA (Unified Trading Account)`、`Fund account`  
> allow_follow| integer| 是否允許跟單：`1` 是，`0` 否  
> follow_num| integer| 跟單此機器人的用戶數量  
> copy_trade_is_master| boolean| 此機器人是否為跟單主策略  
> copy_trade_follower_num| string| 跟單跟隨者數量  
> used_reward_amount| string| 已使用的憑證/獎勵總金額  
> used_reward_id| string| 首個使用的保險憑證 ID  
> init_bonus| string| 初始獎勵金額  
> used_bonus_amount| string| 已消耗的獎勵金額  
> settlement_assets| string| 結算資產信息  
> cum_withdrew_amount| string| 累計提取保證金金額  
> current_profit| string| 當前運行盈虧（小數字符串）  
> current_per| string| 當前運行盈虧百分比（例如 `"0.032"` 表示 3.2%）  
> taker_fee_rate| string| 吃單手續費率（小數比例，例如 `"0.0006"` = 0.06%）  
> maker_fee_rate| string| 掛單手續費率（小數比例，例如 `"0.0001"` = 0.01%）  
> operation_time| string| 自機器人創建以來的毫秒數  
> create_time| string| 機器人創建時間戳（Unix 毫秒）  
> modify_time| string| 最後更新時間戳（Unix 毫秒）  
> end_time| string| 機器人結束時間戳（Unix 毫秒），運行中返回 `0`  
> adl_rank_indicator| integer| ADL（自動減倉）排名指標  
  
* * *

### 請求示例
    
    
    POST /v5/fgridbot/detail HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1672211928338  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "bot_id": "612330315406398322"  
    }  
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "success",  
        "result": {  
            "status_code": 0,  
            "detail": {  
                "bot_id": "612330315406398322",  
                "symbol": "BTCUSDT",  
                "status": "FUTURE_GRID_STATUS_COMPLETED",  
                "base_token": "BTC",  
                "quote_token": "USDT",  
                "min_price": "230000",  
                "max_price": "800000",  
                "cell_number": 88,  
                "grid_type": "FUTURE_GRID_TYPE_GEOMETRIC",  
                "grid_mode": "FUTURE_GRID_MODE_LONG",  
                "stop_loss_per": "",  
                "take_profit_per": "0.28",  
                "real_leverage": "6",  
                "total_investment": "950",  
                "total_value": "",  
                "current_position": "",  
                "arbitrage_num": 0,  
                "arbitrage_num_24": 0,  
                "pnl": "0",  
                "pnl_per": "0.0000",  
                "grid_profit": "0",  
                "grid_apr": "0",  
                "total_apr": "0",  
                "last_price": "",  
                "liquidation_price": "",  
                "realised_pnl": "",  
                "unrealised_pnl": "",  
                "funding_fee": "",  
                "position_balance": "",  
                "available_balance": "",  
                "total_order_balance": "",  
                "close_reason": "F_GRID_BOT_STOP_TYPE_TRIGGER_FBU_FAIL",  
                "allow_follow": 1,  
                "operation_time": "1110",  
                "create_time": "1774506909414",  
                "modify_time": "1774506910524",  
                "end_time": "1774506910522",  
                "min_profit": "8.1959",  
                "max_profit": "8.1959",  
                "leverage": "6",  
                "mark_price": "",  
                "bot_close_code": "BOT_CLOSE_CODE_FAILED_INITIATION",  
                "futures_pos_side": "FUTURES_POSITION_SIDE_UNSPECIFIED",  
                "follow_num": 0,  
                "entry_price": "370000",  
                "stop_loss_price": "200000",  
                "take_profit_price": "",  
                "tp_sl_type": "TP_SL_TYPE_TP_PERCENT_SL_PRICE",  
                "real_close_price": "",  
                "min_price_precision": "0.01",  
                "tick_size": "0.10",  
                "used_reward_amount": "",  
                "settlement_assets": "950 USDT",  
                "account_type": "BOT_ACCOUNT_TYPE_FUND",  
                "cum_withdrew_amount": "0",  
                "current_profit": "",  
                "current_per": "",  
                "copy_trade_is_master": false,  
                "copy_trade_follower_num": "0",  
                "init_bonus": "0",  
                "used_bonus_amount": "",  
                "used_reward_id": "",  
                "taker_fee_rate": "0.00028",  
                "maker_fee_rate": "0.0001",  
                "equity": "0",  
                "trailing_stop_exit_equity": "0",  
                "trailing_stop_per": "0.18",  
                "i_m_rate": "",  
                "m_m_rate": "",  
                "move_up_price": "",  
                "move_down_price": "",  
                "curr_min_price": "",  
                "curr_max_price": "",  
                "adl_rank_indicator": 0  
            },  
            "debug_msg": ""  
        },  
        "retExtInfo": {},  
        "time": 1774508203378  
    }