---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/pre-upgrade/order-list
api_type: REST
updated_at: 2026-05-27 19:21:20.284039
---

# Get Pre-upgrade USDC Session Settlement

Query session settlement records of USDC perpetual before you upgrade the account to Unified account.

info

  * By category="option", you can query USDC Perps settlement data occurred during classic account
  * USDC Perpeual support the recent 6 months data. Please download older data via GUI



### HTTP Request

GET`/v5/pre-upgrade/asset/settlement-record`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
[category](/docs/v5/enum#category)| **true**|  string| Product type `linear`  
symbol| false| string| Symbol name, like `BTCUSDT`, uppercase only  
limit| false| integer| Limit for data size per page. [`1`, `50`]. Default: `20`  
cursor| false| string| Cursor. Used for pagination  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
category| string| Product type  
list| array| Object  
> symbol| string| Symbol name  
> side| string| `Buy`,`Sell`  
> size| string| Position size  
> sessionAvgPrice| string| Settlement price  
> markPrice| string| Mark price  
> realisedPnl| string| Realised PnL  
> createdTime| string| Created time (ms)  
nextPageCursor| string| Cursor. Used for pagination  
  
### Request Example

  * HTTP
  * Python


    
    
    GET /v5/pre-upgrade/asset/settlement-record?category=linear&symbol=ETHPERP&limit=1 HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1686809850982  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
    
    
    
      
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "nextPageCursor": "25%3A0%2C25%3A0",  
            "category": "linear",  
            "list": [  
                {  
                    "realisedPnl": "45.76",  
                    "symbol": "ETHPERP",  
                    "side": "Sell",  
                    "markPrice": "1668.44",  
                    "size": "-0.5",  
                    "createdTime": "1686787200000",  
                    "sessionAvgPrice": "1668.41"  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1686809851749  
    }

---

# 查詢升級前USDC結算紀錄

查詢升級到統一帳戶之前發生的USDC永續的結算紀錄

信息

  * 僅支持查詢最近6個月的數據, 對於更老的數據, 請前往網頁端下載
  * 通過category=linear, 查詢到在經典帳戶期間產生的USDC永續結算數據



### HTTP 請求

GET`/v5/pre-upgrade/asset/settlement-record`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
[category](/docs/zh-TW/v5/enum#category)| **true**|  string| 產品類型. `linear`  
symbol| false| string| 合約名稱  
limit| false| integer| 每頁數量限制. [`1`, `50`]. 默認: `20`  
cursor| false| string| 游標，用於翻頁  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
category| string| 產品類型  
list| array| Object  
> symbol| string| 合約名稱  
> side| string| `Buy`,`Sell`  
> size| string| 倉位大小  
> sessionAvgPrice| string| 結算價格  
> markPrice| string| 標記價格  
> realisedPnl| string| 已實現盈虧  
> createdTime| string| 結算時間 (毫秒)  
nextPageCursor| string| 游標，用於翻頁  
  
### 請求示例

  * HTTP
  * Python


    
    
    GET /v5/pre-upgrade/asset/settlement-record?category=linear&symbol=ETHPERP&limit=1 HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1686809850982  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
    
    
    
      
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "nextPageCursor": "25%3A0%2C25%3A0",  
            "category": "linear",  
            "list": [  
                {  
                    "realisedPnl": "45.76",  
                    "symbol": "ETHPERP",  
                    "side": "Sell",  
                    "markPrice": "1668.44",  
                    "size": "-0.5",  
                    "createdTime": "1686787200000",  
                    "sessionAvgPrice": "1668.41"  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1686809851749  
    }