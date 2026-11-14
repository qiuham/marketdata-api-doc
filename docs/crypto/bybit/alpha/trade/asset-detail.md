---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/alpha/trade/asset-detail
api_type: Trading
updated_at: 2026-11-13 19:21:17.786079
---

# Get Asset Detail

Query detailed holding information for a specific on-chain token, including PnL and cost basis.

info

  * Token is identified by `chainCode` \+ `tokenAddress` — get these from [Get Asset List](/docs/v5/alpha/trade/asset-list) or [Get Biz Token List](/docs/v5/alpha/trade/biz-token-list)
  * Response wraps the asset in an `assetList` array with 0 or 1 element; an empty array means the user does not hold this token
  * Use `tradeFlag` to determine if the token can be sold via [Execute Redeem](/docs/v5/alpha/trade/trade-redeem)



### HTTP Request

POST`/v5/alpha/trade/asset-detail`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
chainCode| **true**|  string| Blockchain code, e.g. `ETH`, `SOL`, `BSC`  
tokenAddress| **true**|  string| Token contract address on the specified chain  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
assetList| array| Asset details. Contains 0 or 1 element. Empty if user does not hold this token  
> chainCode| string| Blockchain code  
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
> pnl| string| Unrealized PnL in USD. Positive = profit. Null if no cost basis available  
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


    
    
    POST /v5/alpha/trade/asset-detail HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1704067200000  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "chainCode": "ETH",  
        "tokenAddress": "0x6982508145454ce325ddbe47a25d4ec3d2311933"  
    }  
    
    
    
      
    
    
    
      
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "assetList": [  
                {  
                    "chainCode": "ETH",  
                    "chainIconUrl": "https://example.com/eth.png",  
                    "tokenAddress": "0x6982508145454ce325ddbe47a25d4ec3d2311933",  
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

# 查詢資產詳情

查詢指定鏈上代幣的持倉詳情，包含盈虧及成本數據。

信息

  * 代幣通過 `chainCode` \+ `tokenAddress` 識別 — 可從 [查詢資產列表](/docs/zh-TW/v5/alpha/trade/asset-list) 或 [獲取業務代幣列表](/docs/zh-TW/v5/alpha/trade/biz-token-list) 獲取
  * 響應中 `assetList` 數組包含 0 或 1 個元素；空數組表示用戶未持有該代幣
  * 使用 `tradeFlag` 判斷代幣是否可通過 [執行贖回](/docs/zh-TW/v5/alpha/trade/trade-redeem) 賣出



### HTTP 請求

POST`/v5/alpha/trade/asset-detail`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
chainCode| **true**|  string| 區塊鏈代碼，如 `ETH`、`SOL`、`BSC`  
tokenAddress| **true**|  string| 指定鏈上的代幣合約地址  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
assetList| array| 資產詳情，包含 0 或 1 個元素。空數組表示用戶未持有該代幣  
> chainCode| string| 區塊鏈代碼  
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


    
    
    POST /v5/alpha/trade/asset-detail HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1704067200000  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "chainCode": "ETH",  
        "tokenAddress": "0x6982508145454ce325ddbe47a25d4ec3d2311933"  
    }  
    
    
    
      
    
    
    
      
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "assetList": [  
                {  
                    "chainCode": "ETH",  
                    "chainIconUrl": "https://example.com/eth.png",  
                    "tokenAddress": "0x6982508145454ce325ddbe47a25d4ec3d2311933",  
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