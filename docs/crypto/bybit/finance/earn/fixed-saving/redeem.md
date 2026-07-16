---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/finance/earn/fixed-saving/redeem
api_type: REST
updated_at: 2026-07-16 18:53:07.206137
---

# Get Airdrop Daily PnL Records

You can query up to 3 months of historical data.

info

  * API key permission: `Earn`
  * Only **completed** (already distributed) yield records are returned. Pending, failed, and zero-amount records are excluded.
  * Users with no byfi earn history will receive a successful response with an empty list.



### HTTP Request

GET`/v5/earn/hold-to-earn/yield-history`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
timeStart| false| integer| Start time (Unix seconds). Cannot be earlier than current time minus 3 months, otherwise returns `INVALIDARGUMENTS`  
timeEnd| false| integer| End time (Unix seconds). Requires `timeStart ≤ timeEnd`  
limit| **true**|  integer| Page size. Range: `1` to `49`. Returns `INVALIDARGUMENTS` if out of range  
cursor| false| string| Pagination cursor. Omit on the first request; pass the `nextCursor` value from the previous response for subsequent pages. Treat the cursor as opaque — do not parse or modify it  
  
info

When both `timeStart` and `timeEnd` are `0`, the query defaults to the last 3 months.

### Response Parameters

Parameter| Type| Comments  
---|---|---  
nextCursor| string| Next page cursor. Empty string indicates the last page. Pass it back as `cursor` in the next request  
airdropDailyPnls| array| Yield records list, sorted by distribution date newest first  
> coinName| string| Investment coin name  
> yieldCoinName| string| Yield coin name. Differs from `coinName` for cross-coin airdrops  
> effectiveAmount| string| Effective principal for that day, e.g., `"10000.00"`  
> pnl| string| Actual yield distributed that day, e.g., `"0.27397260"`  
> apy| string| Annualized yield for that day, e.g., `"10%"`  
> createdAt| integer| Yield distribution time (Unix seconds)  
  
* * *

### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/earn/hold-to-earn/yield-history?timeStart=1739952000&timeEnd=1747728000&limit=20 HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1741651200000  
    X-BAPI-RECV-WINDOW: 5000  
    
    
    
      
    
    
    
      
    

### Response Example
    
    
    {  
        "nextCursor": "eyJsYXN0SWQiOjEwMDE5MH0=",  
        "airdropDailyPnls": [  
            {  
                "coinName": "USDE",  
                "yieldCoinName": "USDE",  
                "effectiveAmount": "10000.00",  
                "pnl": "0.27397260",  
                "apy": "10%",  
                "createdAt": 1747641600  
            },  
            {  
                "coinName": "USDE",  
                "yieldCoinName": "USDE",  
                "effectiveAmount": "10000.00",  
                "pnl": "0.27397260",  
                "apy": "10%",  
                "createdAt": 1747555200  
            }  
        ]  
    }  
    

### Pagination Example

To fetch the next page, pass the `nextCursor` from the previous response back as `cursor`:
    
    
    GET /v5/earn/hold-to-earn/yield-history?limit=20&cursor=eyJsYXN0SWQiOjEwMDE5MH0= HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1741651200000  
    X-BAPI-RECV-WINDOW: 5000  
    

An empty `nextCursor` in the response indicates you have reached the last page.

---

# 查詢空投每日收益記錄

可查詢最近 3 個月的歷史收益數據。

信息

  * API key 需要 `理財` 權限
  * 僅返回**已發放** （`status = complete`）的收益記錄，未發放、失敗及金額為零的記錄均不可見。
  * 非 byfi earn 歷史用戶調用將直接返回成功狀態及空列表。



### HTTP 請求

GET`/v5/earn/hold-to-earn/yield-history`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
timeStart| false| integer| 起始時間（Unix 秒）。**不得早於「當前時間 - 3 個月」** ，否則返回 `INVALIDARGUMENTS`  
timeEnd| false| integer| 結束時間（Unix 秒）。要求 `timeStart ≤ timeEnd`  
limit| **true**|  integer| 單頁大小，範圍：`1` 至 `49`。超出範圍返回 `INVALIDARGUMENTS`  
cursor| false| string| 翻頁游標。首次查詢不傳；後續翻頁傳入上一次響應中的 `nextCursor`。游標對接入方不透明，**僅作整體回傳，不要解析或拼接**  
  
信息

當 `timeStart` 與 `timeEnd` 同時為 `0` 時，自動查詢最近 3 個月的數據。

### 響應參數

參數| 類型| 說明  
---|---|---  
nextCursor| string| 下一頁游標。空字符串表示已到尾頁；翻頁時將其原樣傳回 `cursor` 即可  
airdropDailyPnls| array| 收益記錄列表，按發放日倒序排列（較新在前）  
> coinName| string| 投資幣種名稱  
> yieldCoinName| string| 收益幣種名稱。跨幣種空投時與 `coinName` 不同  
> effectiveAmount| string| 當日計息本金（已格式化字符串，如 `"10000.00"`）  
> pnl| string| 當日實際發放收益（已格式化字符串，如 `"0.27397260"`）  
> apy| string| 該日折算年化收益文案（如 `"10%"`）  
> createdAt| integer| 收益發放時間（Unix 秒）  
  
* * *

### 請求示例

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/earn/hold-to-earn/yield-history?timeStart=1739952000&timeEnd=1747728000&limit=20 HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1741651200000  
    X-BAPI-RECV-WINDOW: 5000  
    
    
    
      
    
    
    
      
    

### 響應示例
    
    
    {  
        "nextCursor": "eyJsYXN0SWQiOjEwMDE5MH0=",  
        "airdropDailyPnls": [  
            {  
                "coinName": "USDE",  
                "yieldCoinName": "USDE",  
                "effectiveAmount": "10000.00",  
                "pnl": "0.27397260",  
                "apy": "10%",  
                "createdAt": 1747641600  
            },  
            {  
                "coinName": "USDE",  
                "yieldCoinName": "USDE",  
                "effectiveAmount": "10000.00",  
                "pnl": "0.27397260",  
                "apy": "10%",  
                "createdAt": 1747555200  
            }  
        ]  
    }  
    

### 翻頁示例

繼續向後翻頁時，將上一次響應中的 `nextCursor` 原樣傳回 `cursor`：
    
    
    GET /v5/earn/hold-to-earn/yield-history?limit=20&cursor=eyJsYXN0SWQiOjEwMDE5MH0= HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1741651200000  
    X-BAPI-RECV-WINDOW: 5000  
    

當響應中的 `nextCursor` 為空字符串時，表示已到達尾頁。