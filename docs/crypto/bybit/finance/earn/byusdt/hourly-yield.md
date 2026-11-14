---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/finance/earn/byusdt/hourly-yield
api_type: REST
updated_at: 2026-11-13 19:23:06.035842
---

# Get Hourly Yield Records

### HTTP Request

GET`/v5/earn/token/hourly-yield`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
coin| **true**|  string| Token coin. Currently only `BYUSDT` is supported  
startTime| false| integer| Start timestamp in seconds  
endTime| false| integer| End timestamp in seconds  
cursor| false| string| Pagination cursor. Use `nextPageCursor` from the previous response  
limit| false| integer| Number of items per page. Default: `20`  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
list| array| Hourly yield record list  
> effectiveAmount| string| Principal amount used to calculate yield for this hour  
> yield| string| Yield amount for this hour  
> rewardType| integer| Yield type: `0` = base yield, `1` = bonus yield  
> aprE8| string| Actual APR applied for this hour in e8 precision. Divide by 10^8 to get the actual rate  
> hourlyDate| string| Start of the yield hour, unix timestamp in seconds  
> createdTime| string| Record creation time, unix timestamp in seconds  
nextPageCursor| string| Cursor for the next page. Empty string means no more data  
  
* * *

### Request Example
    
    
    GET /v5/earn/token/hourly-yield?coin=BYUSDT&limit=20 HTTP/1.1  
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
                    "effectiveAmount": "500.00",  
                    "yield": "0.02",  
                    "rewardType": 0,  
                    "aprE8": "500000000",  
                    "hourlyDate": "1710691200",  
                    "createdTime": "1710694800"  
                }  
            ],  
            "nextPageCursor": "eyJpZCI6MTIzNDU2fQ=="  
        },  
        "retExtInfo": {},  
        "time": 1741651200000  
    }

---

# 查詢每小時收益記錄

### HTTP 請求

GET`/v5/earn/token/hourly-yield`

### 請求參數

參數| 必填| 類型| 說明  
---|---|---|---  
coin| **true**|  string| 代幣幣種。目前僅支援 `BYUSDT`  
startTime| false| integer| 開始時間，秒級時間戳  
endTime| false| integer| 結束時間，秒級時間戳  
cursor| false| string| 分頁游標。使用上次響應中的 `nextPageCursor`  
limit| false| integer| 每頁返回數量。預設：`20`  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
list| array| 每小時收益記錄列表  
> effectiveAmount| string| 本小時用於計算收益的本金金額  
> yield| string| 本小時的收益金額  
> rewardType| integer| 收益類型：`0` = 基礎收益，`1` = 加成收益  
> aprE8| string| 本小時實際適用的年化利率（e8 精度）。除以 10^8 可得實際利率  
> hourlyDate| string| 收益小時的起始時間，秒級 Unix 時間戳  
> createdTime| string| 記錄建立時間，秒級 Unix 時間戳  
nextPageCursor| string| 下一頁游標，為空表示無更多資料  
  
* * *

### 請求示例
    
    
    GET /v5/earn/token/hourly-yield?coin=BYUSDT&limit=20 HTTP/1.1  
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
                    "effectiveAmount": "500.00",  
                    "yield": "0.02",  
                    "rewardType": 0,  
                    "aprE8": "500000000",  
                    "hourlyDate": "1710691200",  
                    "createdTime": "1710694800"  
                }  
            ],  
            "nextPageCursor": "eyJpZCI6MTIzNDU2fQ=="  
        },  
        "retExtInfo": {},  
        "time": 1741651200000  
    }