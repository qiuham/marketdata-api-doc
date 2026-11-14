---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/finance/spot-x/launchpool/launchpool-user-history
api_type: REST
updated_at: 2026-11-13 19:23:41.810126
---

# Get Launchpool User History

Query the authenticated user's completed Launchpool staking position history.

info

  * Authentication is required
  * Returns historical (ended) staking positions, not individual transactions
  * `startTime` and `endTime` filter by the staking period, not record creation time, and must be provided **together**



### HTTP Request

POST`/v5/spot-x/launchpool/user/history`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
stakeCoin| false| string| Filter by stake coin symbol, e.g. `USDT`  
rewardCoin| false| string| Filter by reward coin symbol, e.g. `BTC`  
startTime| false| string| Staking period start filter, 13-digit Unix timestamp in milliseconds. Filters positions whose staking start time is on or after this value. Must be used together with `endTime`  
endTime| false| string| Staking period end filter, 13-digit Unix timestamp in milliseconds. Filters positions whose staking end time is on or before this value. Must be used together with `startTime`  
pageSize| false| integer| Number of records per page. Default: `10`. Max: `10`  
current| false| integer| Page number (1-based). Default: `1`. Max: `100`  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
list| array| Completed staking position records for the current page  
> stakeCoin| string| The coin that was staked in this position  
> rewardCoin| string| The coin earned as reward  
> totalReward| string| Total reward earned for this completed position  
> stakeStartTime| string| Position staking start time, Unix timestamp in milliseconds  
> stakeEndTime| string| Position staking end time (auto-redeem time), Unix timestamp in milliseconds  
total| integer| Total number of records matching the filter  
pageSize| integer| Page size used for this response  
current| integer| Current page number  
  
* * *

### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    POST /v5/spot-x/launchpool/user/history HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1705000000000  
    X-BAPI-RECV-WINDOW: 5000  
    X-BAPI-SIGN: XXXXX  
    Content-Type: application/json  
      
    {  
        "stakeCoin": "USDT",  
        "rewardCoin": "BTC",  
        "pageSize": 10,  
        "current": 1  
    }  
    
    
    
      
    
    
    
      
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "list": [  
                {  
                    "stakeCoin": "USDT",  
                    "rewardCoin": "BTC",  
                    "totalReward": "0.00250",  
                    "stakeStartTime": "1704067200000",  
                    "stakeEndTime": "1706745600000"  
                },  
                {  
                    "stakeCoin": "MNT",  
                    "rewardCoin": "BTC",  
                    "totalReward": "0.00080",  
                    "stakeStartTime": "1701388800000",  
                    "stakeEndTime": "1704067200000"  
                }  
            ],  
            "total": 12,  
            "pageSize": 10,  
            "current": 1  
        },  
        "retExtInfo": {},  
        "time": 1705000000000  
    }

---

# 查詢 Launchpool 用戶歷史倉位

查詢當前用戶已完成的 Launchpool 質押倉位歷史記錄。

信息

  * 需要鑒權
  * 返回已結束的質押倉位記錄，而非單筆操作流水
  * `startTime` 和 `endTime` 按質押期間篩選（非記錄創建時間），必須同時傳入



### HTTP 請求

POST`/v5/spot-x/launchpool/user/history`

### 請求參數

參數| 是否必須| 類型| 說明  
---|---|---|---  
stakeCoin| false| string| 按質押幣種篩選，如 `USDT`  
rewardCoin| false| string| 按獎勵幣種篩選，如 `BTC`  
startTime| false| string| 質押期間開始篩選，13 位毫秒級 Unix 時間戳。篩選質押開始時間大於等於該值的倉位。必須與 `endTime` 同時傳入  
endTime| false| string| 質押期間結束篩選，13 位毫秒級 Unix 時間戳。篩選質押結束時間小於等於該值的倉位。必須與 `startTime` 同時傳入  
pageSize| false| integer| 每頁記錄數，默認 `10`，最大 `10`  
current| false| integer| 頁碼（從 1 開始），默認 `1`，最大 `100`  
  
### 返回參數

參數| 類型| 說明  
---|---|---  
list| array| 當前頁的已完成質押倉位記錄  
> stakeCoin| string| 該倉位質押的幣種  
> rewardCoin| string| 該倉位獲得獎勵的幣種  
> totalReward| string| 該已完成倉位的累計獎勵總量  
> stakeStartTime| string| 倉位質押開始時間，毫秒級 Unix 時間戳  
> stakeEndTime| string| 倉位質押結束時間（自動贖回時間），毫秒級 Unix 時間戳  
total| integer| 符合篩選條件的記錄總數  
pageSize| integer| 本次響應使用的每頁條數  
current| integer| 當前頁碼  
  
* * *

### 請求示例

  * HTTP
  * Python
  * Node.js


    
    
    POST /v5/spot-x/launchpool/user/history HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1705000000000  
    X-BAPI-RECV-WINDOW: 5000  
    X-BAPI-SIGN: XXXXX  
    Content-Type: application/json  
      
    {  
        "stakeCoin": "USDT",  
        "rewardCoin": "BTC",  
        "pageSize": 10,  
        "current": 1  
    }  
    
    
    
      
    
    
    
      
    

### 返回示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "list": [  
                {  
                    "stakeCoin": "USDT",  
                    "rewardCoin": "BTC",  
                    "totalReward": "0.00250",  
                    "stakeStartTime": "1704067200000",  
                    "stakeEndTime": "1706745600000"  
                },  
                {  
                    "stakeCoin": "MNT",  
                    "rewardCoin": "BTC",  
                    "totalReward": "0.00080",  
                    "stakeStartTime": "1701388800000",  
                    "stakeEndTime": "1704067200000"  
                }  
            ],  
            "total": 12,  
            "pageSize": 10,  
            "current": 1  
        },  
        "retExtInfo": {},  
        "time": 1705000000000  
    }