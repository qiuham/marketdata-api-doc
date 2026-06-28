---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/alpha/order-list
api_type: REST
updated_at: 2026-05-27 19:14:34.463776
---

# Get Order List

Query user's on-chain trade order history with status, fees, and execution details.

info

  * Supports filtering by trade type, order status, token, and time range
  * Maximum query range is 90 days; orders sorted by creation time descending
  * Order status flow: `1` (Processing) → `2` (Success) or `3` (Failed)
  * On-chain confirmation typically takes 10–60 seconds
  * Use this endpoint after [Execute Purchase](/docs/v5/alpha/trade-purchase) or [Execute Redeem](/docs/v5/alpha/trade-redeem) to confirm the final order status



### HTTP Request

POST`/v5/alpha/trade/order-list`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
tradeType| false| integer| Filter by trade type. `0`: All (default), `1`: Purchase, `2`: Redeem  
tokenCode| false| string| Filter by token code  
orderStatus| false| array| Filter by order status (multiple values allowed). `1`: Processing, `2`: Success, `3`: Failed  
days| false| integer| Query last N days. Range: [0, 90]. `0` uses system default (90 days). Default: `0`  
limit| **true**|  integer| Results per page. Range: [1, 100]  
pageIndex| **true**|  integer| Page number (1-based)  
direction| false| string| Pagination direction. `prev`, `next`  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
total| integer| Total order count matching the filter  
pageIndex| integer| Current page number  
orders| array| Order list  
> orderType| integer| Order type. `1`: Market order, `2`: Limit order  
> tradeType| integer| Trade type. `1`: Purchase, `2`: Redeem  
> orderNo| string| System order number  
> orderStatus| integer| Order status. `1`: Processing, `2`: Success, `3`: Failed  
> fromTokenCode| string| Source token code  
> fromTokenAmount| string| Intended payment amount  
> fromTokenSymbol| string| Source token symbol  
> fromTokenDecimals| integer| Source token decimal precision  
> fromTokenIconUrlDay| string| Source token icon URL (light mode)  
> fromTokenIconUrlNight| string| Source token icon URL (dark mode)  
> fromChainCode| string| Source chain code  
> fromChainIconUrl| string| Source chain icon URL  
> toTokenCode| string| Target token code  
> toTokenAmount| string| Actual amount received (populated after completion)  
> toTokenSymbol| string| Target token symbol  
> toTokenDecimals| integer| Target token decimal precision  
> toTokenIconUrlDay| string| Target token icon URL (light mode)  
> toTokenIconUrlNight| string| Target token icon URL (dark mode)  
> toChainCode| string| Target chain code  
> toChainIconUrl| string| Target chain icon URL  
> gasTokenSymbol| string| Native gas token symbol, e.g. `ETH`, `SOL`, `BNB`  
> gasOnchain| string| On-chain gas fee in native token  
> gasUsd| string| Gas fee in USD. May be null if order is still processing  
> platformFee| string| Platform fee  
> platformFeeUsd| string| Platform fee in USD. May be null if order is still processing  
> quoteMode| integer| Quote mode used  
> createTime| integer| Order creation time (Unix timestamp in seconds)  
> executionTime| integer| Order completion time (Unix timestamp in seconds)  
> failureReasonCode| string| Failure reason code, only present when `orderStatus=3`. `ERR999`: Unknown, `ERR101`: System exception, `ERR102`: Execution timeout, `ERR103`: Insufficient balance, `ERR104`: Broadcast failed, `ERR105`: On-chain execution failed, `ERR106`: Trade loss too large, `ERR107`: Liquidity range too large  
> source| string| Trade source identifier  
> swapRate| string| Actual exchange rate  
> actualFromTokenAmount| string| Actual amount paid  
  
### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    POST /v5/alpha/trade/order-list HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1704067200000  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "tradeType": 0,  
        "days": 7,  
        "limit": 20,  
        "pageIndex": 1  
    }  
    
    
    
      
    
    
    
      
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "total": 1,  
            "pageIndex": 1,  
            "orders": [  
                {  
                    "orderType": 1,  
                    "tradeType": 1,  
                    "orderNo": "ORD_20240101_001",  
                    "orderStatus": 2,  
                    "fromTokenCode": "CEX_1",  
                    "fromTokenAmount": "100",  
                    "fromTokenSymbol": "USDT",  
                    "fromTokenDecimals": 6,  
                    "fromChainCode": "ETH",  
                    "toTokenCode": "DEX_123",  
                    "toTokenAmount": "12450000",  
                    "toTokenSymbol": "PEPE",  
                    "toTokenDecimals": 18,  
                    "toChainCode": "ETH",  
                    "gasTokenSymbol": "ETH",  
                    "gasOnchain": "0.0003",  
                    "gasUsd": "0.30",  
                    "platformFee": "0.20",  
                    "platformFeeUsd": "0.20",  
                    "quoteMode": 0,  
                    "createTime": 1704067200,  
                    "executionTime": 1704067230,  
                    "swapRate": "124500",  
                    "actualFromTokenAmount": "100"  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1704067300000  
    }

---

# 查詢訂單列表

查詢用戶的鏈上交易訂單歷史，包含訂單狀態、手續費及執行詳情。

信息

  * 支持按交易類型、訂單狀態、代幣及時間範圍篩選
  * 最大查詢範圍為 90 天，結果按創建時間倒序排列
  * 訂單狀態流轉：`1`（處理中）→ `2`（成功）或 `3`（失敗）
  * 鏈上確認通常需要 10–60 秒
  * 調用 [執行購買](/docs/zh-TW/v5/alpha/trade-purchase) 或 [執行贖回](/docs/zh-TW/v5/alpha/trade-redeem) 後，可使用此接口確認最終訂單狀態



### HTTP 請求

POST`/v5/alpha/trade/order-list`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
tradeType| false| integer| 按交易類型篩選。`0`: 全部（默認），`1`: 購買，`2`: 贖回  
tokenCode| false| string| 按代幣代碼篩選  
orderStatus| false| array| 按訂單狀態篩選（支持多個值）。`1`: 處理中，`2`: 成功，`3`: 失敗  
days| false| integer| 查詢最近 N 天。範圍：[0, 90]。`0` 使用系統默認（90 天）。默認：`0`  
limit| **true**|  integer| 每頁條數。範圍：[1, 100]  
pageIndex| **true**|  integer| 頁碼（從 1 開始）  
direction| false| string| 翻頁方向。`prev`、`next`  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
total| integer| 符合篩選條件的訂單總數  
pageIndex| integer| 當前頁碼  
orders| array| 訂單列表  
> orderType| integer| 訂單類型。`1`: 市價單，`2`: 限價單  
> tradeType| integer| 交易類型。`1`: 購買，`2`: 贖回  
> orderNo| string| 系統訂單號  
> orderStatus| integer| 訂單狀態。`1`: 處理中，`2`: 成功，`3`: 失敗  
> fromTokenCode| string| 源代幣代碼  
> fromTokenAmount| string| 預計支付數量  
> fromTokenSymbol| string| 源代幣符號  
> fromTokenDecimals| integer| 源代幣小數精度  
> fromTokenIconUrlDay| string| 源代幣圖標 URL（淺色模式）  
> fromTokenIconUrlNight| string| 源代幣圖標 URL（深色模式）  
> fromChainCode| string| 源鏈代碼  
> fromChainIconUrl| string| 源鏈圖標 URL  
> toTokenCode| string| 目標代幣代碼  
> toTokenAmount| string| 實際接收數量（完成後填充）  
> toTokenSymbol| string| 目標代幣符號  
> toTokenDecimals| integer| 目標代幣小數精度  
> toTokenIconUrlDay| string| 目標代幣圖標 URL（淺色模式）  
> toTokenIconUrlNight| string| 目標代幣圖標 URL（深色模式）  
> toChainCode| string| 目標鏈代碼  
> toChainIconUrl| string| 目標鏈圖標 URL  
> gasTokenSymbol| string| 原生 Gas 代幣符號，如 `ETH`、`SOL`、`BNB`  
> gasOnchain| string| 鏈上 Gas 費用（原生代幣單位）  
> gasUsd| string| Gas 費用（USD）。訂單處理中時可能為 null  
> platformFee| string| 平台手續費  
> platformFeeUsd| string| 平台手續費（USD）。訂單處理中時可能為 null  
> quoteMode| integer| 使用的報價模式  
> createTime| integer| 訂單創建時間（Unix 時間戳，秒）  
> executionTime| integer| 訂單完成時間（Unix 時間戳，秒）  
> failureReasonCode| string| 失敗原因代碼，僅當 `orderStatus=3` 時存在。`ERR999`: 未知原因，`ERR101`: 系統異常，`ERR102`: 執行超時，`ERR103`: 餘額不足，`ERR104`: 廣播失敗，`ERR105`: 鏈上執行失敗，`ERR106`: 交易損耗過大，`ERR107`: 流動性範圍過大  
> source| string| 交易來源標識  
> swapRate| string| 實際兌換匯率  
> actualFromTokenAmount| string| 實際支付數量  
  
### 請求示例

  * HTTP
  * Python
  * Node.js


    
    
    POST /v5/alpha/trade/order-list HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1704067200000  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "tradeType": 0,  
        "days": 7,  
        "limit": 20,  
        "pageIndex": 1  
    }  
    
    
    
      
    
    
    
      
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "total": 1,  
            "pageIndex": 1,  
            "orders": [  
                {  
                    "orderType": 1,  
                    "tradeType": 1,  
                    "orderNo": "ORD_20240101_001",  
                    "orderStatus": 2,  
                    "fromTokenCode": "CEX_1",  
                    "fromTokenAmount": "100",  
                    "fromTokenSymbol": "USDT",  
                    "fromTokenDecimals": 6,  
                    "fromChainCode": "ETH",  
                    "toTokenCode": "DEX_123",  
                    "toTokenAmount": "12450000",  
                    "toTokenSymbol": "PEPE",  
                    "toTokenDecimals": 18,  
                    "toChainCode": "ETH",  
                    "gasTokenSymbol": "ETH",  
                    "gasOnchain": "0.0003",  
                    "gasUsd": "0.30",  
                    "platformFee": "0.20",  
                    "platformFeeUsd": "0.20",  
                    "quoteMode": 0,  
                    "createTime": 1704067200,  
                    "executionTime": 1704067230,  
                    "swapRate": "124500",  
                    "actualFromTokenAmount": "100"  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1704067300000  
    }