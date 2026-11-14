---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/bot/dca/create
api_type: REST
updated_at: 2026-11-13 19:21:56.692309
---

# Create DCA Bot

Create a new DCA (Dollar-Cost Averaging) bot that automatically invests at regular intervals across specified trading pairs.

info

  * **How it works:**  
The bot buys a fixed amount of each configured trading pair at every `frequency_in_second` interval, regardless of market price.

  * **Supported trading pairs:**  
Maximum **5** pairs per bot.

  * **Minimum frequency:**  
10 seconds. Common values: `600` (10 min), `3600` (1 hour), `86400` (1 day).

  * **`max_invest_amount`:**  
Optional cap on total cumulative investment. The bot auto-closes when cumulative spending reaches this amount.

  * **Response`bot_id`:**  
Returned on success. Use this ID for subsequent [Close](/docs/v5/bot/dca/close) operations.

  * **Rate limit:**  
3 requests per second per UID.

  * **Subject to compliance wall and KYC verification.**  
If the user is banned (status_code=421), `ban_reason_text` provides a localized explanation.




### HTTP Request

POST`/v5/dca/create-bot`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
parameters| **true**|  object| DCA bot configuration object (see below)  
> frequency_in_second| **true**|  integer| Investment frequency in seconds. Minimum `10`. Common: `600` (10 min), `3600` (1 hr), `86400` (1 day)  
> quote_coin| **true**|  string| Quote token used for purchasing (e.g. `USDT`, `USDC`)  
> pairs| **true**|  array| Trading pairs to invest in. Maximum 5 pairs  
>> base| **true**|  string| coin to be invested (e.g. `BTC`)  
>> amount| **true**|  string| Per-round investment amount in quote coin (decimal string, e.g. `"10"` for 10 USDT)  
> max_invest_amount| false| string| Optional. Maximum total investment in quote coin (decimal string). Bot auto-closes when reached  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
status_code| integer| `200` = success, `421` = user banned  
bot_id| integer| Created DCA bot ID. Use for subsequent close operations  
debug_msg| string| Reason for creation failure (testnet: debug info)  
ban_reason_text| string| Ban reason in user's locale. Returned only when `status_code=421`  
  
* * *

### Request Example
    
    
    POST /v5/dca/create-bot HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1672211928338  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "parameters": {  
            "frequency_in_second": "600",  
            "quote_coin": "USDT",  
            "max_invest_amount": "2000",  
            "pairs": [  
                {  
                    "base": "BTC",  
                    "amount": "66"  
                },  
                {  
                    "base": "ETH",  
                    "amount": "88"  
                }  
            ]  
        }  
    }  
    

### Response Example
    
    
    {  
        "status_code": 200,  
        "bot_id": 9876543210,  
        "debug_msg": "",  
        "ban_reason_text": ""  
    }

---

# 創建定投機器人

創建一個新的定投（DCA）機器人，按固定時間間隔自動在指定交易對上投資。

信息

  * **運作方式：**  
機器人每隔 `frequency_in_second` 秒買入每個配置交易對的固定金額，無論市場價格如何。

  * **支持的交易對：**  
每個機器人最多 **5** 個交易對。

  * **最小頻率：**  
10 秒。常用值：`600`（10 分鐘）、`3600`（1 小時）、`86400`（1 天）。

  * **`max_invest_amount`：**  
可選的累計投資上限。當累計消費達到此金額時，機器人自動關閉。

  * **響應`bot_id`：**  
成功時返回，用於後續[關閉](/docs/zh-TW/v5/bot/dca/close)操作。

  * **頻率限制：**  
每個 UID 每秒最多 3 次請求。

  * **受合規管控及 KYC 驗證約束。**  
若用戶被封禁（status_code=421），`ban_reason_text` 提供本地化說明。




### HTTP請求

POST`/v5/dca/create-bot`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
parameters| **true**|  object| 定投機器人配置對象（詳見下方）  
> frequency_in_second| **true**|  integer| 投資頻率（秒）。最小 `10`。常用：`600`（10 分鐘）、`3600`（1 小時）、`86400`（1 天）  
> quote_coin| **true**|  string| 購買所用報價幣種（例如 `USDT`、`USDC`）  
> pairs| **true**|  array| 要投資的交易對。最多 5 個  
>> base| **true**|  string| 待投資的幣種（例如 `BTC`）  
>> amount| **true**|  string| 每輪投資金額，以報價幣種計（小數字符串，例如 `"10"` 表示 10 USDT）  
> max_invest_amount| false| string| 可選。以報價幣種計的最大總投資金額（小數字符串）。達到後機器人自動關閉  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
status_code| integer| `200` = 成功，`421` = 用戶被封禁  
bot_id| integer| 已創建的定投機器人 ID，用於後續關閉操作  
debug_msg| string| 創建失敗原因（測試網：調試信息）  
ban_reason_text| string| 用戶語言的封禁原因，僅當 `status_code=421` 時返回  
  
* * *

### 請求示例
    
    
    POST /v5/dca/create-bot HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1672211928338  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "parameters": {  
            "frequency_in_second": "600",  
            "quote_coin": "USDT",  
            "max_invest_amount": "2000",  
            "pairs": [  
                {  
                    "base": "BTC",  
                    "amount": "66"  
                },  
                {  
                    "base": "ETH",  
                    "amount": "88"  
                }  
            ]  
        }  
    }  
    

### 響應示例
    
    
    {  
        "status_code": 200,  
        "bot_id": 9876543210,  
        "debug_msg": "",  
        "ban_reason_text": ""  
    }