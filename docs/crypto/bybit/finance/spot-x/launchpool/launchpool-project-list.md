---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/finance/spot-x/launchpool/launchpool-project-list
api_type: REST
updated_at: 2026-10-07 18:52:15.519239
---

# Get Token Splash Project List

Query the Token Splash activity (project) list. Results are sorted by creation time descending (newest first) and support cursor-based pagination.

info

  * Authentication is **not** required
  * Only released, main-site public activities are returned
  * `nextPageCursor` being an empty string indicates the last page
  * `activityEndTime` = max(`announceTime`, `tradeAnnounceTime`)
  * `registrationStartTime` = min of non-zero values among `signUpBeginTime` and `tradeSignUpBeginTime`



### HTTP Request

GET`/v5/spot-x/token-splash/project/list`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
status| **true**|  integer| Activity phase filter. `0`: Upcoming (registration not yet started); `1`: Ongoing; `2`: Ended (announcement time has passed)  
projectId| false| string| Exact activity code. Use to query a single project  
activityCoin| false| string| Filter by activity coin symbol (case-insensitive), e.g. `BTC`, `ETH`  
cursor| false| string| Pagination cursor returned as `nextPageCursor` in the previous response. Omit for the first page  
limit| false| integer| Number of items per page. Default: `10`. Max: `10`  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
list| array| Activity items for the current page  
> status| integer| Activity status. `0`: Upcoming; `1`: Ongoing; `2`: Ended  
> projectId| string| Unique activity code  
> activityCoin| string| The coin that the activity is centered on  
> rewardCoin| string| The coin distributed as the reward. Resolved in priority order: new pool token → old pool token → trade pool token  
> totalReward| string| Total reward pool size (sum of new, old, and trade prize pool amounts)  
> participantCount| string| Total number of registered participants  
> registrationStartTime| string| Earliest registration start time, Unix timestamp in milliseconds. Equals `min(signUpBeginTime, tradeSignUpBeginTime)`, ignoring zero values  
> activityEndTime| string| Activity end time, Unix timestamp in milliseconds. Equals `max(announceTime, tradeAnnounceTime)`  
nextPageCursor| string| Cursor for the next page. Empty string means last page  
  
* * *

### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/spot-x/token-splash/project/list?status=1&limit=10 HTTP/1.1  
    Host: api.bybit.com  
    
    
    
      
    
    
    
      
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "list": [  
                {  
                    "status": 1,  
                    "projectId": "TOKENSPLASH_BTC_2024Q1",  
                    "activityCoin": "BTC",  
                    "rewardCoin": "USDT",  
                    "totalReward": "100000",  
                    "participantCount": "3456",  
                    "registrationStartTime": "1704067200000",  
                    "activityEndTime": "1706745600000"  
                }  
            ],  
            "nextPageCursor": "eyJpZCI6MTIzfQ=="  
        },  
        "retExtInfo": {},  
        "time": 1705000000000  
    }

---

# 查詢 Token Splash 項目列表

查詢 Token Splash 活動（項目）列表。結果按創建時間倒序排列（最新優先），支持游標分頁。

信息

  * 無需鑒權
  * 僅返回已發布的主站公開活動
  * `nextPageCursor` 為空字符串時表示已到最後一頁
  * `activityEndTime` = max(`announceTime`, `tradeAnnounceTime`)
  * `registrationStartTime` = `signUpBeginTime` 和 `tradeSignUpBeginTime` 中非零值的最小值



### HTTP 請求

GET`/v5/spot-x/token-splash/project/list`

### 請求參數

參數| 是否必須| 類型| 說明  
---|---|---|---  
status| **true**|  integer| 活動階段篩選。`0`: 即將開始（報名未開始）；`1`: 進行中；`2`: 已結束（公告時間已過）  
projectId| false| string| 精確活動代碼，用於查詢單個項目  
activityCoin| false| string| 按活動幣種篩選（大小寫不敏感），如 `BTC`、`ETH`  
cursor| false| string| 分頁游標，傳入上一次響應中的 `nextPageCursor`。首頁請求無需傳入  
limit| false| integer| 每頁數量，默認 `10`，最大 `10`  
  
### 返回參數

參數| 類型| 說明  
---|---|---  
list| array| 當前頁的活動列表  
> status| integer| 活動狀態。`0`: 即將開始；`1`: 進行中；`2`: 已結束  
> projectId| string| 唯一活動代碼  
> activityCoin| string| 活動對應的幣種  
> rewardCoin| string| 實際發放的獎勵幣種。優先級順序：新池代幣 → 舊池代幣 → 交易池代幣  
> totalReward| string| 獎勵池總量（新池、舊池及交易池金額之和）  
> participantCount| string| 已報名參與人數  
> registrationStartTime| string| 最早報名開始時間，毫秒級 Unix 時間戳。等於 `signUpBeginTime` 和 `tradeSignUpBeginTime` 中非零值的最小值  
> activityEndTime| string| 活動結束時間，毫秒級 Unix 時間戳。等於 `max(announceTime, tradeAnnounceTime)`  
nextPageCursor| string| 下一頁游標，為空字符串時表示已到最後一頁  
  
* * *

### 請求示例

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/spot-x/token-splash/project/list?status=1&limit=10 HTTP/1.1  
    Host: api.bybit.com  
    
    
    
      
    
    
    
      
    

### 返回示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "list": [  
                {  
                    "status": 1,  
                    "projectId": "TOKENSPLASH_BTC_2024Q1",  
                    "activityCoin": "BTC",  
                    "rewardCoin": "USDT",  
                    "totalReward": "100000",  
                    "participantCount": "3456",  
                    "registrationStartTime": "1704067200000",  
                    "activityEndTime": "1706745600000"  
                }  
            ],  
            "nextPageCursor": "eyJpZCI6MTIzfQ=="  
        },  
        "retExtInfo": {},  
        "time": 1705000000000  
    }