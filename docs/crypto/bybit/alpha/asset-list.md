---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/alpha/asset-list
api_type: REST
updated_at: 2026-06-28 19:07:55.446155
---

# Get Asset List

Query user's on-chain token portfolio including holdings, market value, and PnL.

info

  * Only returns tokens with non-zero balance; zero-balance tokens are filtered out
  * Assets are sorted by USD value descending
  * Use `tradeFlag` to determine if a token can be sold via [Execute Redeem](/docs/v5/alpha/trade-redeem)
  * Use `tokenCode` from the response for quote and execution requests
  * Use `chainCode` \+ `tokenAddress` to call [Get Token Details](/docs/v5/alpha/biz-token-details) for more info



### HTTP Request

POST`/v5/alpha/trade/asset-list`

### Request Parameters

None

### Response Parameters

Parameter| Type| Comments  
---|---|---  
totalAssetUsd| string| Total portfolio value in USD  
assetList| array| Token holdings list  
> chainCode| string| Blockchain code, e.g. `ETH`, `SOL`, `BSC`  
> chainIconUrl| string| Chain icon URL  
> tokenAddress| string| Token contract address  
> tokenCode| string| Token code in `DEX_<id>` format. Use this in quote and execution requests  
> tokenSymbol| string| Token symbol  
> tokenDecimals| integer| Token decimal precision  
> tokenIconUrlDay| string| Token icon URL (light mode)  
> tokenIconUrlNight| string| Token icon URL (dark mode)  
> tokenAmount| string| Holding quantity  
> tokenAmountUsd| string| Holding value in USD  
> tradeFlag| integer| Whether tradable. `0`: Not tradable, `1`: Tradable  
> pnl| string| Unrealized profit/loss in USD. Positive = profit. Null if no cost basis available  
> pnlRatio| string| PnL ratio as decimal, e.g. `0.15` = +15%. Null if no cost basis available  
> costPrice| string| Average cost price. Null if no cost basis available  
> lastPrice| string| Current market price  
> costTotalValue| string| Total cost basis in USD. Null if no cost basis available  
> assetStatus| integer| Token lifecycle status. `0`: Running, `1`: Delisting soon, `2`: Delisted  
> announcementUrl| string| Delisting announcement URL. Present when `assetStatus` is `1` or `2`  
> estimatedOfflineTime| integer| Estimated delisting timestamp (ms). Present when `assetStatus=1`  
> delistingTime| integer| Actual delisting timestamp (ms). Present when `assetStatus=2`  
  
### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    POST /v5/alpha/trade/asset-list HTTP/1.1  
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
            "totalAssetUsd": "1250.50",  
            "assetList": [  
                {  
                    "chainCode": "SOL",  
                    "chainIconUrl": "https://example.com/sol.png",  
                    "tokenAddress": "0xabc...",  
                    "tokenCode": "DEX_123",  
                    "tokenSymbol": "PEPE",  
                    "tokenDecimals": 18,  
                    "tokenIconUrlDay": "https://example.com/pepe-day.png",  
                    "tokenIconUrlNight": "https://example.com/pepe-night.png",  
                    "tokenAmount": "50000000",  
                    "tokenAmountUsd": "500.00",  
                    "tradeFlag": 1,  
                    "pnl": "75.00",  
                    "pnlRatio": "0.15",  
                    "costPrice": "0.0000085",  
                    "lastPrice": "0.00001",  
                    "costTotalValue": "425.00",  
                    "assetStatus": 0  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1704067200000  
    }

---

# 查詢資產列表

查詢用戶的鏈上代幣持倉，包含持倉數量、市值及盈虧信息。

信息

  * 僅返回餘額不為零的代幣，零餘額代幣不在返回列表中
  * 資產按 USD 價值倒序排列
  * 使用 `tradeFlag` 判斷代幣是否可通過 [執行贖回](/docs/zh-TW/v5/alpha/trade-redeem) 賣出
  * 使用返回的 `tokenCode` 用於報價及執行接口
  * 使用 `chainCode` \+ `tokenAddress` 調用 [獲取代幣詳情](/docs/zh-TW/v5/alpha/biz-token-details) 獲取更多信息



### HTTP 請求

POST`/v5/alpha/trade/asset-list`

### 請求參數

無

### 響應參數

參數| 類型| 說明  
---|---|---  
totalAssetUsd| string| 持倉總市值（USD）  
assetList| array| 代幣持倉列表  
> chainCode| string| 區塊鏈代碼，如 `ETH`、`SOL`、`BSC`  
> chainIconUrl| string| 鏈圖標 URL  
> tokenAddress| string| 代幣合約地址  
> tokenCode| string| `DEX_<id>` 格式的代幣代碼，用於報價及執行接口  
> tokenSymbol| string| 代幣符號  
> tokenDecimals| integer| 代幣小數精度  
> tokenIconUrlDay| string| 代幣圖標 URL（淺色模式）  
> tokenIconUrlNight| string| 代幣圖標 URL（深色模式）  
> tokenAmount| string| 持倉數量  
> tokenAmountUsd| string| 持倉市值（USD）  
> tradeFlag| integer| 是否可交易。`0`: 不可交易，`1`: 可交易  
> pnl| string| 未實現盈虧（USD），正數為盈利。無成本數據時為 null  
> pnlRatio| string| 盈虧比率（小數），如 `0.15` = +15%。無成本數據時為 null  
> costPrice| string| 平均成本價。無成本數據時為 null  
> lastPrice| string| 當前市場價格  
> costTotalValue| string| 總成本（USD）。無成本數據時為 null  
> assetStatus| integer| 代幣生命週期狀態。`0`: 運行中，`1`: 即將下線，`2`: 已下線  
> announcementUrl| string| 下線公告 URL。`assetStatus` 為 `1` 或 `2` 時存在  
> estimatedOfflineTime| integer| 預計下線時間（ms）。`assetStatus=1` 時存在  
> delistingTime| integer| 實際下線時間（ms）。`assetStatus=2` 時存在  
  
### 請求示例

  * HTTP
  * Python
  * Node.js


    
    
    POST /v5/alpha/trade/asset-list HTTP/1.1  
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
            "totalAssetUsd": "1250.50",  
            "assetList": [  
                {  
                    "chainCode": "SOL",  
                    "chainIconUrl": "https://example.com/sol.png",  
                    "tokenAddress": "0xabc...",  
                    "tokenCode": "DEX_123",  
                    "tokenSymbol": "PEPE",  
                    "tokenDecimals": 18,  
                    "tokenIconUrlDay": "https://example.com/pepe-day.png",  
                    "tokenIconUrlNight": "https://example.com/pepe-night.png",  
                    "tokenAmount": "50000000",  
                    "tokenAmountUsd": "500.00",  
                    "tradeFlag": 1,  
                    "pnl": "75.00",  
                    "pnlRatio": "0.15",  
                    "costPrice": "0.0000085",  
                    "lastPrice": "0.00001",  
                    "costTotalValue": "425.00",  
                    "assetStatus": 0  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1704067200000  
    }