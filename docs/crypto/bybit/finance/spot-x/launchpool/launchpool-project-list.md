---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/finance/spot-x/launchpool/launchpool-project-list
api_type: REST
updated_at: 2026-08-09 18:44:10.190993
---

# Get Token Splash User Activity Params

Query the authenticated user's participation details and trade-task progress for Token Splash activities.

info

  * Authentication is required
  * Only returns activities where the user has already registered
  * Only trade-task activities are returned (deposit-only task types are excluded)
  * Only activities that have not yet reached their announcement time are returned (rewards not yet distributed)
  * Estimated reward formula: `min(tradedAmount / tradeRequiredAmount, 1) × maxRewardAmount`, truncated to 4 decimal places



### HTTP Request

GET`/v5/spot-x/token-splash/user/activity-params`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
projectId| false| string| Filter by exact activity code. Returns data for a single project when provided  
activityCoin| false| string| Filter by activity coin symbol (case-insensitive), e.g. `BTC`, `ETH`  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
list| array| User activity items. Empty array if the user has not registered for any matching activity  
> projectId| string| Unique activity code  
> activityCoin| string| The coin that the activity is centered on  
> tradeTask| object| Trade task details and the user's current progress  
>> tradeRequiredAmount| string| Total trade volume required to earn the full reward  
>> tradeUnit| string| The coin unit for the trade task  
>> tradedAmount| string| Trade volume the user has accumulated so far  
>> maxRewardAmount| string| Maximum reward the user can earn if the full required volume is traded  
>> estimatedRewardAmount| string| Estimated reward based on current progress, truncated to 4 decimal places. Formula: `min(tradedAmount / tradeRequiredAmount, 1) × maxRewardAmount`  
>> rewardCoin| string| Coin in which the trade-task reward is distributed  
  
* * *

### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/spot-x/token-splash/user/activity-params HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1705000000000  
    X-BAPI-RECV-WINDOW: 5000  
    X-BAPI-SIGN: XXXXX  
    
    
    
      
    
    
    
      
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "list": [  
                {  
                    "projectId": "TOKENSPLASH_BTC_2024Q1",  
                    "activityCoin": "BTC",  
                    "tradeTask": {  
                        "tradeRequiredAmount": "0.5",  
                        "tradeUnit": "BTC",  
                        "tradedAmount": "0.3",  
                        "maxRewardAmount": "200",  
                        "estimatedRewardAmount": "120.0000",  
                        "rewardCoin": "USDT"  
                    }  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1705000000000  
    }

---

# 查詢 Token Splash 用戶活動參數

查詢當前用戶在 Token Splash 活動中的參與詳情及交易任務進度。

信息

  * 需要鑒權
  * 僅返回用戶已報名的活動
  * 僅返回交易任務類活動（不含純入金任務類型）
  * 僅返回尚未到達公告時間的活動（獎勵尚未發放）
  * 預估獎勵計算公式：`min(tradedAmount / tradeRequiredAmount, 1) × maxRewardAmount`，截斷至 4 位小數



### HTTP 請求

GET`/v5/spot-x/token-splash/user/activity-params`

### 請求參數

參數| 是否必須| 類型| 說明  
---|---|---|---  
projectId| false| string| 精確活動代碼，傳入時僅返回該項目數據  
activityCoin| false| string| 按活動幣種篩選（大小寫不敏感），如 `BTC`、`ETH`  
  
### 返回參數

參數| 類型| 說明  
---|---|---  
list| array| 用戶活動列表。若用戶未報名任何匹配活動則返回空數組  
> projectId| string| 唯一活動代碼  
> activityCoin| string| 活動對應的幣種  
> tradeTask| object| 交易任務詳情及用戶當前進度  
>> tradeRequiredAmount| string| 達到全額獎勵所需的交易量  
>> tradeUnit| string| 交易任務的幣種單位  
>> tradedAmount| string| 用戶目前已累計的交易量  
>> maxRewardAmount| string| 完成全部所需交易量可獲得的最大獎勵  
>> estimatedRewardAmount| string| 基於當前進度的預估獎勵，截斷至 4 位小數。計算公式：`min(tradedAmount / tradeRequiredAmount, 1) × maxRewardAmount`  
>> rewardCoin| string| 交易任務獎勵的發放幣種  
  
* * *

### 請求示例

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/spot-x/token-splash/user/activity-params HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1705000000000  
    X-BAPI-RECV-WINDOW: 5000  
    X-BAPI-SIGN: XXXXX  
    
    
    
      
    
    
    
      
    

### 返回示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "list": [  
                {  
                    "projectId": "TOKENSPLASH_BTC_2024Q1",  
                    "activityCoin": "BTC",  
                    "tradeTask": {  
                        "tradeRequiredAmount": "0.5",  
                        "tradeUnit": "BTC",  
                        "tradedAmount": "0.3",  
                        "maxRewardAmount": "200",  
                        "estimatedRewardAmount": "120.0000",  
                        "rewardCoin": "USDT"  
                    }  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1705000000000  
    }