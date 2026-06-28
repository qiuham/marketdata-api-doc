---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/position/position-mode
api_type: Position
updated_at: 2026-06-28 19:13:43.551203
---

# Get Pre-upgrade Closed PnL

Query user's closed profit and loss records from before you upgraded the account to a Unified account. The results are sorted by `updatedTime` in descending order. it only supports to query USDT perpetual, Inverse perpetual and Inverse Futures.

info

By `category`="linear", you can query USDT Perps data occurred during classic account  
By `category`="inverse", you can query Inverse Contract data occurred during **classic account or[UTA1.0](/docs/v5/acct-mode#uta-10)**

### HTTP Request

GET`/v5/pre-upgrade/position/closed-pnl`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
[category](/docs/v5/enum#category)| **true**|  string| Product type `linear`, `inverse`  
symbol| **true**|  string| Symbol name, like `BTCUSDT`, uppercase only  
startTime| false| integer| The start timestamp (ms) 

  * startTime and endTime are not passed, return 7 days by default
  * Only startTime is passed, return range between startTime and startTime+7 days
  * Only endTime is passed, return range between endTime-7 days and endTime
  * If both are passed, the rule is endTime - startTime <= 7 days

  
endTime| false| integer| The end timestamp (ms)  
limit| false| integer| Limit for data size per page. [`1`, `100`]. Default: `50`  
cursor| false| string| Cursor. Use the `nextPageCursor` token from the response to retrieve the next page of the result set  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
category| string| Product type  
list| array| Object  
> symbol| string| Symbol name  
> orderId| string| Order ID  
> side| string| `Buy`, `Side`  
> qty| string| Order qty  
> orderPrice| string| Order price  
> [orderType](/docs/v5/enum#ordertype)| string| Order type. `Market`,`Limit`  
> execType| string| Exec type. `Trade`, `BustTrade`, `SessionSettlePnL`, `Settle`  
> closedSize| string| Closed size  
> cumEntryValue| string| Cumulated Position value  
> avgEntryPrice| string| Average entry price  
> cumExitValue| string| Cumulated exit position value  
> avgExitPrice| string| Average exit price  
> closedPnl| string| Closed PnL  
> fillCount| string| The number of fills in a single order  
> leverage| string| leverage  
> createdTime| string| The created time (ms)  
> updatedTime| string| The updated time (ms)  
nextPageCursor| string| Refer to the `cursor` request parameter  
  
### Request Example
    
    
    GET /v5/pre-upgrade/position/closed-pnl?category=linear&symbol=BTCUSDT HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1682580911998  
    X-BAPI-RECV-WINDOW: 5000  
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "list": [  
                {  
                    "symbol": "BTCUSDT",  
                    "orderId": "67836246-460e-4c52-a009-af0c3e1d12bc",  
                    "side": "Sell",  
                    "qty": "0.200",  
                    "orderPrice": "27203.40",  
                    "orderType": "Market",  
                    "execType": "Trade",  
                    "closedSize": "0.200",  
                    "cumEntryValue": "5588.88",  
                    "avgEntryPrice": "27944.40",  
                    "cumExitValue": "5726.4252",  
                    "avgExitPrice": "28632.13",  
                    "closedPnl": "204.25510011",  
                    "fillCount": "22",  
                    "leverage": "10",  
                    "createdTime": "1682487465732",  
                    "updatedTime": "1682487465732"  
                }  
            ],  
            "category": "linear",  
            "nextPageCursor": ""  
        },  
        "retExtInfo": {},  
        "time": 1682580912259  
    }

---

# 查詢升級前平倉盈虧

支持查詢升級到統一帳戶之前發生的USDT永續 / 反向合約, 返回結果按照`updatedTime`降序排列

通過category=linear, 查詢到在經典帳戶期間產生的USDT永續數據  
通過category=inverse, 查詢到在經典帳戶或者統一帳戶1.0期間產生的反向合約數據

### HTTP 請求

GET`/v5/pre-upgrade/position/closed-pnl`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
[category](/docs/zh-TW/v5/enum#category)| **true**|  string| 產品類型

  * `linear`, `inverse`

  
symbol| **true**|  string| 合約名稱  
startTime| false| integer| 開始時間戳 (毫秒) 

  * startTime 和 endTime都不傳入, 則默認返回最近7天的數據
  * startTime 和 endTime都傳入的話, 則確保endTime - startTime <= 7天
  * 若只傳startTime，則查詢startTime和startTime+7天的數據
  * 若只傳endTime，則查詢endTime-7天和endTime的數據

  
endTime| false| integer| 結束時間戳 (毫秒)  
limit| false| integer| 每頁數量限制. [`1`, `100`]. 默認: `50`  
cursor| false| string| 游標，用於翻頁  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
[category](/docs/zh-TW/v5/enum#category)| string| 產品類型  
list| array| Object  
> symbol| string| 合約名稱  
> orderId| string| 訂單Id  
> side| string| 買賣方向 `Buy`, `Side`  
> qty| string| 訂單數量  
> orderPrice| string| 訂單價格  
> [orderType](/docs/zh-TW/v5/enum#ordertype)| string| 訂單類型. `Market`,`Limit`  
> execType| string| 執行類型. `Trade`, `BustTrade`, `SessionSettlePnL`, `Settle`  
> closedSize| string| 平倉數量  
> cumEntryValue| string| 被平倉位的累計入場價值  
> avgEntryPrice| string| 平均入場價格  
> cumExitValue| string| 被平倉位的累計出場價值  
> avgExitPrice| string| 平均出場價格  
> closedPnl| string| 被平倉位的盈虧  
> fillCount| string| 成交筆數  
> leverage| string| 持倉槓桿  
> createdTime| string| 創建時間 (毫秒)  
> updatedTime| string| 更新時間 (毫秒)  
nextPageCursor| string| 游標，用於翻頁  
  
### 請求示例
    
    
    GET /v5/pre-upgrade/position/closed-pnl?category=linear&symbol=BTCUSDT HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1682580911998  
    X-BAPI-RECV-WINDOW: 5000  
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "list": [  
                {  
                    "symbol": "BTCUSDT",  
                    "orderId": "67836246-460e-4c52-a009-af0c3e1d12bc",  
                    "side": "Sell",  
                    "qty": "0.200",  
                    "orderPrice": "27203.40",  
                    "orderType": "Market",  
                    "execType": "Trade",  
                    "closedSize": "0.200",  
                    "cumEntryValue": "5588.88",  
                    "avgEntryPrice": "27944.40",  
                    "cumExitValue": "5726.4252",  
                    "avgExitPrice": "28632.13",  
                    "closedPnl": "204.25510011",  
                    "fillCount": "22",  
                    "leverage": "10",  
                    "createdTime": "1682487465732",  
                    "updatedTime": "1682487465732"  
                }  
            ],  
            "category": "linear",  
            "nextPageCursor": ""  
        },  
        "retExtInfo": {},  
        "time": 1682580912259  
    }