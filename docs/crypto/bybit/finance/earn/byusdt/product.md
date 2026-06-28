---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/finance/earn/byusdt/product
api_type: REST
updated_at: 2026-05-27 19:17:22.046784
---

# Get Daily Yield Records

### HTTP Request

GET`/v5/earn/token/yield`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
coin| **true**|  string| Token coin. Currently only `BYUSDT` is supported  
startTime| false| integer| Start timestamp in seconds  
endTime| false| integer| End timestamp in seconds  
cursor| false| string| Pagination cursor. Use `nextPageCursor` from the previous response  
limit| false| integer| Number of items per page. Default: `5`  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
list| array| Daily yield record list  
> yield| string| Base yield amount  
> bonusYield| string| Bonus yield amount  
> status| string| Status: `Success`, `Processing`  
> createdTime| string| Record time, unix timestamp in seconds  
nextPageCursor| string| Cursor for the next page. Empty string means no more data  
  
* * *

### Request Example
    
    
    GET /v5/earn/token/yield?coin=BYUSDT&limit=5 HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1741651200000  
    X-BAPI-RECV-WINDOW: 5000  
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "success",  
        "result": {  
            "list": [  
                {  
                    "yield": "0.50",  
                    "bonusYield": "0.20",  
                    "status": "Success",  
                    "createdTime": "1710691200"  
                }  
            ],  
            "nextPageCursor": "eyJpZCI6MTIzNDU2fQ=="  
        },  
        "retExtInfo": {},  
        "time": 1741651200000  
    }

---

# 查詢每日收益記錄

### HTTP 請求

GET`/v5/earn/token/yield`

### 請求參數

參數| 必填| 類型| 說明  
---|---|---|---  
coin| **true**|  string| 代幣幣種。目前僅支援 `BYUSDT`  
startTime| false| integer| 開始時間，秒級時間戳  
endTime| false| integer| 結束時間，秒級時間戳  
cursor| false| string| 分頁游標。使用上次響應中的 `nextPageCursor`  
limit| false| integer| 每頁返回數量。預設：`5`  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
list| array| 每日收益記錄列表  
> yield| string| 基礎收益金額  
> bonusYield| string| 加成收益金額  
> status| string| 狀態：`Success`（成功）、`Processing`（處理中）  
> createdTime| string| 記錄時間，秒級 Unix 時間戳  
nextPageCursor| string| 下一頁游標，為空表示無更多資料  
  
* * *

### 請求示例
    
    
    GET /v5/earn/token/yield?coin=BYUSDT&limit=5 HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1741651200000  
    X-BAPI-RECV-WINDOW: 5000  
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "success",  
        "result": {  
            "list": [  
                {  
                    "yield": "0.50",  
                    "bonusYield": "0.20",  
                    "status": "Success",  
                    "createdTime": "1710691200"  
                }  
            ],  
            "nextPageCursor": "eyJpZCI6MTIzNDU2fQ=="  
        },  
        "retExtInfo": {},  
        "time": 1741651200000  
    }