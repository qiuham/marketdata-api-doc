---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/finance/spot-x/launchpool/launchpool-current-staking
api_type: REST
updated_at: 2026-08-08 18:44:08.918503
---

# Get Launchpool Current Staking

Query the authenticated user's active staking positions across all ongoing Launchpool activities, including a USD-denominated portfolio summary and per-position details.

info

  * Authentication is required
  * Returns up to **30** positions, covering all active staking positions without pagination



### HTTP Request

GET`/v5/spot-x/launchpool/user/current-staking`

### Request Parameters

No request parameters required.

### Response Parameters

Parameter| Type| Comments  
---|---|---  
totalInvestmentUsd| string| Total USD value of all active staking positions  
totalEarningsUsd| string| Total USD value of accumulated earnings across all positions  
todayEarningsUsd| string| Today's earnings across all positions, in USD  
list| array| Per-position staking details. Up to 30 items  
> stakeCoin| string| The coin staked into this position  
> rewardCoin| string| The coin earned as reward  
> stakeAmount| string| Total amount currently staked  
> totalReward| string| Accumulated reward earned so far  
> autoRedeemDate| string| Auto-redeem time, Unix timestamp in milliseconds. The principal will be automatically returned on this date. Empty string if not set  
  
* * *

### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/spot-x/launchpool/user/current-staking HTTP/1.1  
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
            "totalInvestmentUsd": "15000.00",  
            "totalEarningsUsd": "120.50",  
            "todayEarningsUsd": "8.20",  
            "list": [  
                {  
                    "stakeCoin": "USDT",  
                    "rewardCoin": "BTC",  
                    "stakeAmount": "10000",  
                    "totalReward": "0.00120",  
                    "autoRedeemDate": "1706745600000"  
                },  
                {  
                    "stakeCoin": "MNT",  
                    "rewardCoin": "BTC",  
                    "stakeAmount": "50000",  
                    "totalReward": "0.00050",  
                    "autoRedeemDate": "1706745600000"  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1705000000000  
    }

---

# 查詢 Launchpool 當前質押倉位

查詢當前用戶在所有進行中 Launchpool 活動中的有效質押倉位，包含 USD 計價的資產組合摘要及各倉位詳情。

信息

  * 需要鑒權
  * 最多返回 **30** 條倉位記錄，涵蓋所有有效質押倉位，無需分頁



### HTTP 請求

GET`/v5/spot-x/launchpool/user/current-staking`

### 請求參數

無請求參數。

### 返回參數

參數| 類型| 說明  
---|---|---  
totalInvestmentUsd| string| 所有有效質押倉位的 USD 總價值  
totalEarningsUsd| string| 所有倉位累計收益的 USD 總額  
todayEarningsUsd| string| 今日所有倉位的 USD 收益合計  
list| array| 各倉位質押詳情，最多 30 條  
> stakeCoin| string| 該倉位質押的幣種  
> rewardCoin| string| 該倉位獲得獎勵的幣種  
> stakeAmount| string| 當前質押總量  
> totalReward| string| 截至目前的累計獎勵  
> autoRedeemDate| string| 自動贖回時間，毫秒級 Unix 時間戳。到期後本金將自動返還。未設置時為空字符串  
  
* * *

### 請求示例

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/spot-x/launchpool/user/current-staking HTTP/1.1  
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
            "totalInvestmentUsd": "15000.00",  
            "totalEarningsUsd": "120.50",  
            "todayEarningsUsd": "8.20",  
            "list": [  
                {  
                    "stakeCoin": "USDT",  
                    "rewardCoin": "BTC",  
                    "stakeAmount": "10000",  
                    "totalReward": "0.00120",  
                    "autoRedeemDate": "1706745600000"  
                },  
                {  
                    "stakeCoin": "MNT",  
                    "rewardCoin": "BTC",  
                    "stakeAmount": "50000",  
                    "totalReward": "0.00050",  
                    "autoRedeemDate": "1706745600000"  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1705000000000  
    }