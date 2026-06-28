---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/finance/advanced-earn/websocket/smart-lvg-offer
api_type: WebSocket
updated_at: 2026-06-28 19:10:59.059359
---

# Get History APR

info

No authentication required

### HTTP Request

GET`/v5/earn/token/history-apr`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
coin| **true**|  string| Token coin. Currently only `BYUSDT` is supported  
range| **true**|  integer| Time range: `1` = 7 days, `2` = 30 days, `3` = 180 days  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
list| array| Historical APR list  
> timestamp| string| Date, unix timestamp in seconds  
> aprE8| string| APR value in e8 precision. Divide by 10^8 to get the actual rate  
  
* * *

### Request Example
    
    
    GET /v5/earn/token/history-apr?coin=BYUSDT&range=1 HTTP/1.1  
    Host: api.bybit.com  
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "",  
        "result": {  
            "list": [  
                {  
                    "timestamp": "1774569600",  
                    "aprE8": "2000000"  
                },  
                {  
                    "timestamp": "1774656000",  
                    "aprE8": "2000000"  
                },  
                {  
                    "timestamp": "1774742400",  
                    "aprE8": "2000000"  
                },  
                {  
                    "timestamp": "1774828800",  
                    "aprE8": "52750000"  
                },  
                {  
                    "timestamp": "1774915200",  
                    "aprE8": "60000000"  
                },  
                {  
                    "timestamp": "1775001600",  
                    "aprE8": "108070000"  
                },  
                {  
                    "timestamp": "1775088000",  
                    "aprE8": "96290000"  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1775180579207  
    }

---

# 查詢歷史年化利率

信息

無需身份驗證

### HTTP 請求

GET`/v5/earn/token/history-apr`

### 請求參數

參數| 必填| 類型| 說明  
---|---|---|---  
coin| **true**|  string| 代幣幣種。目前僅支援 `BYUSDT`  
range| **true**|  integer| 時間範圍：`1` = 7 天，`2` = 30 天，`3` = 180 天  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
list| array| 歷史年化利率列表  
> timestamp| string| 日期，秒級 Unix 時間戳  
> aprE8| string| e8 精度的年化利率。除以 10^8 可得實際利率  
  
* * *

### 請求示例
    
    
    GET /v5/earn/token/history-apr?coin=BYUSDT&range=1 HTTP/1.1  
    Host: api.bybit.com  
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "",  
        "result": {  
            "list": [  
                {  
                    "timestamp": "1774569600",  
                    "aprE8": "2000000"  
                },  
                {  
                    "timestamp": "1774656000",  
                    "aprE8": "2000000"  
                },  
                {  
                    "timestamp": "1774742400",  
                    "aprE8": "2000000"  
                },  
                {  
                    "timestamp": "1774828800",  
                    "aprE8": "52750000"  
                },  
                {  
                    "timestamp": "1774915200",  
                    "aprE8": "60000000"  
                },  
                {  
                    "timestamp": "1775001600",  
                    "aprE8": "108070000"  
                },  
                {  
                    "timestamp": "1775088000",  
                    "aprE8": "96290000"  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1775180579207  
    }