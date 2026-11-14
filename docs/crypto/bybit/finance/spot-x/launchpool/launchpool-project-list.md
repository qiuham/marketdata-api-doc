---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/finance/spot-x/launchpool/launchpool-project-list
api_type: REST
updated_at: 2026-11-13 19:23:41.781072
---

# Get Launchpool Project List

Query the Launchpool activity (project) list. Results are sorted by creation time descending (newest first) and support cursor-based pagination.

info

  * Authentication is **not** required
  * Only online, main-site public activities are returned
  * `nextPageCursor` being an empty string indicates the last page



### HTTP Request

GET`/v5/spot-x/launchpool/project/list`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
status| **true**|  integer| Activity phase filter. `0`: Upcoming; `1`: Ongoing; `2`: Ended  
activityCoin| false| string| Filter by reward coin symbol (case-insensitive), e.g. `BTC`, `ETH`  
projectId| false| string| Exact activity code. Use to query a single project  
cursor| false| string| Pagination cursor returned as `nextPageCursor` in the previous response. Omit for the first page  
limit| false| integer| Number of items per page. Default: `10`. Max: `10`  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
list| array| List of Launchpool activity objects  
> projectId| string| Unique activity code  
> activityCoin| string| The reward coin of the activity  
> rewardCoin| string| The coin distributed as the reward  
> status| integer| Activity status. `0`: Upcoming; `1`: Ongoing; `2`: Ended  
> totalReward| string| Sum of all pool reward amounts  
> stakeStartTime| string| Staking start time, Unix timestamp in milliseconds  
> stakeEndTime| string| Staking end time (auto-redeem time), Unix timestamp in milliseconds  
> totalParticipantCount| string| Total number of participants across all pools  
> pools| array| Per-pool staking details for this activity  
>> poolId| string| Unique pool code  
>> stakeCoin| string| The coin users stake into this pool  
>> apr| string| Calculated annual percentage rate for this pool  
>> totalStakedAmount| string| Total amount currently staked in this pool  
>> participantCount| string| Number of participants in this pool  
nextPageCursor| string| Cursor for the next page. Empty string means last page  
  
* * *

### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/spot-x/launchpool/project/list?status=1&limit=10 HTTP/1.1  
    Host: api.bybit.com  
    
    
    
      
    
    
    
      
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "list": [  
                {  
                    "projectId": "LAUNCHPOOL_BTC_2024Q1",  
                    "activityCoin": "BTC",  
                    "rewardCoin": "BTC",  
                    "status": 1,  
                    "totalReward": "10",  
                    "stakeStartTime": "1704067200000",  
                    "stakeEndTime": "1706745600000",  
                    "totalParticipantCount": "5000",  
                    "pools": [  
                        {  
                            "poolId": "POOL_BTC_USDT",  
                            "stakeCoin": "USDT",  
                            "apr": "15.50",  
                            "totalStakedAmount": "1000000",  
                            "participantCount": "3000"  
                        },  
                        {  
                            "poolId": "POOL_BTC_MNT",  
                            "stakeCoin": "MNT",  
                            "apr": "20.00",  
                            "totalStakedAmount": "500000",  
                            "participantCount": "2000"  
                        }  
                    ]  
                }  
            ],  
            "nextPageCursor": "eyJpZCI6MTIzfQ=="  
        },  
        "retExtInfo": {},  
        "time": 1705000000000  
    }

---

# 查詢 Launchpool 項目列表

查詢 Launchpool 活動（項目）列表。結果按創建時間倒序排列（最新優先），支持游標分頁。

信息

  * 無需鑒權
  * 僅返回主站已上線的公開活動
  * `nextPageCursor` 為空字符串時表示已到最後一頁



### HTTP 請求

GET`/v5/spot-x/launchpool/project/list`

### 請求參數

參數| 是否必須| 類型| 說明  
---|---|---|---  
status| **true**|  integer| 活動階段篩選。`0`: 即將開始；`1`: 進行中；`2`: 已結束  
activityCoin| false| string| 按獎勵幣種篩選（大小寫不敏感），如 `BTC`、`ETH`  
projectId| false| string| 精確活動代碼，用於查詢單個項目  
cursor| false| string| 分頁游標，傳入上一次響應中的 `nextPageCursor`。首頁請求無需傳入  
limit| false| integer| 每頁數量，默認 `10`，最大 `10`  
  
### 返回參數

參數| 類型| 說明  
---|---|---  
list| array| Launchpool 活動對象列表  
> projectId| string| 唯一活動代碼  
> activityCoin| string| 活動獎勵幣種  
> rewardCoin| string| 實際發放的獎勵幣種  
> status| integer| 活動狀態。`0`: 即將開始；`1`: 進行中；`2`: 已結束  
> totalReward| string| 所有礦池獎勵總量  
> stakeStartTime| string| 質押開始時間，毫秒級 Unix 時間戳  
> stakeEndTime| string| 質押結束時間（自動贖回時間），毫秒級 Unix 時間戳  
> totalParticipantCount| string| 所有礦池參與人數總計  
> pools| array| 該活動下各礦池的質押詳情  
>> poolId| string| 唯一礦池代碼  
>> stakeCoin| string| 用戶質押的幣種  
>> apr| string| 該礦池的年化利率  
>> totalStakedAmount| string| 該礦池當前質押總量  
>> participantCount| string| 該礦池參與人數  
nextPageCursor| string| 下一頁游標，為空字符串時表示已到最後一頁  
  
* * *

### 請求示例

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/spot-x/launchpool/project/list?status=1&limit=10 HTTP/1.1  
    Host: api.bybit.com  
    
    
    
      
    
    
    
      
    

### 返回示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "list": [  
                {  
                    "projectId": "LAUNCHPOOL_BTC_2024Q1",  
                    "activityCoin": "BTC",  
                    "rewardCoin": "BTC",  
                    "status": 1,  
                    "totalReward": "10",  
                    "stakeStartTime": "1704067200000",  
                    "stakeEndTime": "1706745600000",  
                    "totalParticipantCount": "5000",  
                    "pools": [  
                        {  
                            "poolId": "POOL_BTC_USDT",  
                            "stakeCoin": "USDT",  
                            "apr": "15.50",  
                            "totalStakedAmount": "1000000",  
                            "participantCount": "3000"  
                        },  
                        {  
                            "poolId": "POOL_BTC_MNT",  
                            "stakeCoin": "MNT",  
                            "apr": "20.00",  
                            "totalStakedAmount": "500000",  
                            "participantCount": "2000"  
                        }  
                    ]  
                }  
            ],  
            "nextPageCursor": "eyJpZCI6MTIzfQ=="  
        },  
        "retExtInfo": {},  
        "time": 1705000000000  
    }