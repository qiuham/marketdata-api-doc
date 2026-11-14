---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/finance/advanced-earn/liquidity-mining/yield-records
api_type: REST
updated_at: 2026-11-13 19:22:59.328971
---

# Get Yield Records

info

  * Need authentication. **Up to 10 requests** per second per UID. Requires Earn permission on the API key.
  * Returns yield claim history, including both manual claims and yields settled on removal.



### HTTP Request

GET`/v5/earn/liquidity-mining/yield-records`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
baseCoin| false| string| Filter by base coin, e.g. `BTC`, `ETH`  
quoteCoin| false| string| Filter by quote coin, e.g. `USDT`  
startTime| false| string| Start time, unix timestamp in milliseconds  
endTime| false| string| End time, unix timestamp in milliseconds  
limit| false| integer| Number of items per page. Default: `20`, Max: `50`  
cursor| false| string| Pagination cursor. Use `nextPageCursor` from the previous response  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
records| array| Yield record list  
> coin| string| Yield coin received  
> amount| string| Amount received  
> baseCoin| string| Base coin of the pool, e.g. `BTC`  
> quoteCoin| string| Quote coin of the pool, e.g. `USDT`  
> type| string| Claim type: `Manual` (manually claimed), `RemoveLiquidity` (yield settled on removal)  
> status| string| Record status: `Complete`, `Processing`  
> createdTime| string| Record creation time, unix timestamp in milliseconds  
nextPageCursor| string| Cursor for next page. Empty string means no more data  
  
* * *

### Request Example
    
    
    GET /v5/earn/liquidity-mining/yield-records?baseCoin=ETH HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1741651200000  
    X-BAPI-RECV-WINDOW: 5000  
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "",  
        "result": {  
            "records": [  
                {  
                    "coin": "USDT",  
                    "amount": "0.0098",  
                    "baseCoin": "ETH",  
                    "quoteCoin": "USDT",  
                    "type": "Manual",  
                    "status": "Complete",  
                    "createdTime": "1775125850000"  
                }  
            ],  
            "nextPageCursor": ""  
        },  
        "retExtInfo": {},  
        "time": 1775126002035  
    }

---

# 查詢收益記錄

信息

  * 需要身份驗證。每個 UID 每秒**最多 10 次請求** 。API 金鑰需要具備 Earn（理財）權限。
  * 返回收益領取歷史記錄，包括手動領取及移除流動性時結算的收益。



### HTTP 請求

GET`/v5/earn/liquidity-mining/yield-records`

### 請求參數

參數| 必填| 類型| 說明  
---|---|---|---  
baseCoin| false| string| 按基礎幣種篩選，例如：`BTC`, `ETH`  
quoteCoin| false| string| 按計價幣種篩選，例如：`USDT`  
startTime| false| string| 開始時間，毫秒級 Unix 時間戳  
endTime| false| string| 結束時間，毫秒級 Unix 時間戳  
limit| false| integer| 每頁返回數量。預設：`20`，最大：`50`  
cursor| false| string| 分頁游標。使用上次響應中的 `nextPageCursor`  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
records| array| 收益記錄列表  
> coin| string| 收到的收益幣種  
> amount| string| 收到的金額  
> baseCoin| string| 流動性池的基礎幣種，例如：`BTC`  
> quoteCoin| string| 流動性池的計價幣種，例如：`USDT`  
> type| string| 領取類型：`Manual`（手動領取），`RemoveLiquidity`（移除流動性時結算）  
> status| string| 記錄狀態：`Complete`（已完成）、`Processing`（處理中）  
> createdTime| string| 記錄建立時間，毫秒級 Unix 時間戳  
nextPageCursor| string| 下一頁游標，為空表示無更多資料  
  
* * *

### 請求示例
    
    
    GET /v5/earn/liquidity-mining/yield-records?baseCoin=ETH HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1741651200000  
    X-BAPI-RECV-WINDOW: 5000  
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "",  
        "result": {  
            "records": [  
                {  
                    "coin": "USDT",  
                    "amount": "0.0098",  
                    "baseCoin": "ETH",  
                    "quoteCoin": "USDT",  
                    "type": "Manual",  
                    "status": "Complete",  
                    "createdTime": "1775125850000"  
                }  
            ],  
            "nextPageCursor": ""  
        },  
        "retExtInfo": {},  
        "time": 1775126002035  
    }