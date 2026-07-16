---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/finance/advanced-earn/liquidity-mining/add-liquidity
api_type: REST
updated_at: 2026-07-16 18:52:21.009437
---

# Get Liquidation Records

info

  * Need authentication. **Up to 10 requests** per second per UID. Requires Earn permission on the API key.
  * Returns historical liquidation records for your leveraged liquidity mining positions.



### HTTP Request

GET`/v5/earn/liquidity-mining/liquidation-records`

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
records| array| Liquidation record list  
> baseCoin| string| Base coin of the pool, e.g. `BTC`  
> quoteCoin| string| Quote coin of the pool, e.g. `USDT`  
> baseAmount| string| Returned baseCoin amount after liquidation  
> quoteAmount| string| Returned quoteCoin amount after liquidation  
> liquidationPrice| string| Liquidation price (baseCoin priced in quoteCoin)  
> liquidationTime| string| Liquidation time, unix timestamp in milliseconds  
nextPageCursor| string| Cursor for next page. Empty string means no more data  
  
* * *

### Request Example
    
    
    GET /v5/earn/liquidity-mining/liquidation-records?baseCoin=BTC&limit=20 HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1741651200000  
    X-BAPI-RECV-WINDOW: 5000  
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "records": [  
                {  
                    "baseCoin": "BTC",  
                    "quoteCoin": "USDT",  
                    "baseAmount": "0.05234",  
                    "quoteAmount": "1580.21",  
                    "liquidationPrice": "30200.00",  
                    "liquidationTime": "1741824000000"  
                }  
            ],  
            "nextPageCursor": ""  
        },  
        "retExtInfo": {},  
        "time": 1741824100000  
    }

---

# 查詢爆倉記錄

信息

  * 需要身份驗證。每個 UID 每秒**最多 10 次請求** 。API 金鑰需要具備 Earn（理財）權限。
  * 返回槓桿流動性挖礦持倉的歷史強制平倉記錄。



### HTTP 請求

GET`/v5/earn/liquidity-mining/liquidation-records`

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
records| array| 強制平倉記錄列表  
> baseCoin| string| 流動性池的基礎幣種，例如：`BTC`  
> quoteCoin| string| 流動性池的計價幣種，例如：`USDT`  
> baseAmount| string| 強制平倉後返還的基礎幣種金額  
> quoteAmount| string| 強制平倉後返還的計價幣種金額  
> liquidationPrice| string| 強制平倉價格（基礎幣種以計價幣種計價）  
> liquidationTime| string| 強制平倉時間，毫秒級 Unix 時間戳  
nextPageCursor| string| 下一頁游標，為空表示無更多資料  
  
* * *

### 請求示例
    
    
    GET /v5/earn/liquidity-mining/liquidation-records?baseCoin=BTC&limit=20 HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1741651200000  
    X-BAPI-RECV-WINDOW: 5000  
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "records": [  
                {  
                    "baseCoin": "BTC",  
                    "quoteCoin": "USDT",  
                    "baseAmount": "0.05234",  
                    "quoteAmount": "1580.21",  
                    "liquidationPrice": "30200.00",  
                    "liquidationTime": "1741824000000"  
                }  
            ],  
            "nextPageCursor": ""  
        },  
        "retExtInfo": {},  
        "time": 1741824100000  
    }