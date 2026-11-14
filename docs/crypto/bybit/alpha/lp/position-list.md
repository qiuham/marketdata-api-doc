---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/alpha/lp/position-list
api_type: REST
updated_at: 2026-11-13 19:21:04.225167
---

# Get LP Position List

Query the user's LP positions with real-time valuation, earned rewards, and APY.

info

  * Use this to display the user's LP portfolio, or to confirm position changes after [Execute LP Stake](/docs/v5/alpha/lp/stake) / [Execute LP Redeem](/docs/v5/alpha/lp/redeem)
  * For pool details, use [Get LP Pool Info](/docs/v5/alpha/lp/pool-info) instead
  * **Rate Limit:** 3 req/s (per user), 2000 req/s (global)



### HTTP Request

POST`/v5/alpha/lp/position-list`

### Request Parameters

None

### Response Parameters

Parameter| Type| Comments  
---|---|---  
positions| array| Position list  
> positionId| integer| Position identifier  
> poolAddress| string| Pool contract address  
> poolName| string| Pool name  
> stakedAmount| string| Total staked amount in payment token  
> stakedTokenCode| string| Staked token code  
> stakedTokenSymbol| string| Staked token symbol  
> currentValueUsd| string| Current position value in USD  
> earnedRewardsUsd| string| Total earned rewards in USD  
> unrealizedPnl| string| Unrealized profit/loss  
> realizedPnl| string| Realized profit/loss  
> apy| string| Current APY for this position  
> token0Amount| string| Amount of token0 in position  
> token0Symbol| string| Token0 symbol  
> token1Amount| string| Amount of token1 in position  
> token1Symbol| string| Token1 symbol  
> rangeUpper| string| Position upper range/price  
> rangeLower| string| Position lower range/price  
> createTime| integer| Position creation time (Unix seconds)  
> updateTime| integer| Last update time (Unix seconds)  
> status| integer| Position status. `1`: Active, `2`: Closed, `3`: Processing  
  
* * *

### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    POST /v5/alpha/lp/position-list HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1704067200000  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {}  
    
    
    
      
    
    
    
      
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "positions": [  
                {  
                    "positionId": 12345,  
                    "poolAddress": "0x1234567890abcdef",  
                    "poolName": "ETH-USDC Pool",  
                    "stakedAmount": "1000",  
                    "stakedTokenCode": "CEX_1",  
                    "stakedTokenSymbol": "USDT",  
                    "currentValueUsd": "1050.25",  
                    "earnedRewardsUsd": "50.25",  
                    "unrealizedPnl": "30.00",  
                    "realizedPnl": "20.25",  
                    "apy": "12.5",  
                    "token0Amount": "0.3",  
                    "token0Symbol": "ETH",  
                    "token1Amount": "600",  
                    "token1Symbol": "USDC",  
                    "rangeUpper": "2000",  
                    "rangeLower": "1800",  
                    "createTime": 1704067200,  
                    "updateTime": 1704067260,  
                    "status": 1  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1704067300000  
    }

---

# 查詢 LP 倉位列表

查詢用戶的 LP 倉位，包含實時估值、已獲收益和 APY。

信息

  * 可用本接口展示用戶的 LP 持倉，或在執行 [執行 LP 質押](/docs/zh-TW/v5/alpha/lp/stake) / [執行 LP 贖回](/docs/zh-TW/v5/alpha/lp/redeem) 後確認倉位變更
  * 查詢礦池詳情請使用 [查詢 LP 礦池詳情](/docs/zh-TW/v5/alpha/lp/pool-info)
  * **頻率限制：** 3 次/秒（用戶），2000 次/秒（全局）



### HTTP 請求

POST`/v5/alpha/lp/position-list`

### 請求參數

無

### 響應參數

參數| 類型| 說明  
---|---|---  
positions| array| 倉位列表  
> positionId| integer| 倉位標識符  
> poolAddress| string| 礦池合約地址  
> poolName| string| 礦池名稱  
> stakedAmount| string| 支付代幣的總質押數量  
> stakedTokenCode| string| 質押代幣代碼  
> stakedTokenSymbol| string| 質押代幣符號  
> currentValueUsd| string| 倉位當前 USD 價值  
> earnedRewardsUsd| string| 已獲總收益（USD）  
> unrealizedPnl| string| 未實現盈虧  
> realizedPnl| string| 已實現盈虧  
> apy| string| 當前倉位 APY  
> token0Amount| string| 倉位中 token0 的數量  
> token0Symbol| string| token0 符號  
> token1Amount| string| 倉位中 token1 的數量  
> token1Symbol| string| token1 符號  
> rangeUpper| string| 倉位價格/範圍上限  
> rangeLower| string| 倉位價格/範圍下限  
> createTime| integer| 倉位創建時間（Unix 秒）  
> updateTime| integer| 最近更新時間（Unix 秒）  
> status| integer| 倉位狀態。`1`: 活躍，`2`: 已關閉，`3`: 處理中  
  
* * *

### 請求示例

  * HTTP
  * Python
  * Node.js


    
    
    POST /v5/alpha/lp/position-list HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1704067200000  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {}  
    
    
    
      
    
    
    
      
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "positions": [  
                {  
                    "positionId": 12345,  
                    "poolAddress": "0x1234567890abcdef",  
                    "poolName": "ETH-USDC Pool",  
                    "stakedAmount": "1000",  
                    "stakedTokenCode": "CEX_1",  
                    "stakedTokenSymbol": "USDT",  
                    "currentValueUsd": "1050.25",  
                    "earnedRewardsUsd": "50.25",  
                    "unrealizedPnl": "30.00",  
                    "realizedPnl": "20.25",  
                    "apy": "12.5",  
                    "token0Amount": "0.3",  
                    "token0Symbol": "ETH",  
                    "token1Amount": "600",  
                    "token1Symbol": "USDC",  
                    "rangeUpper": "2000",  
                    "rangeLower": "1800",  
                    "createTime": 1704067200,  
                    "updateTime": 1704067260,  
                    "status": 1  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1704067300000  
    }