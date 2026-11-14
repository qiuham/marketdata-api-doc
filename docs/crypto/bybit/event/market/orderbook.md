---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/event/market/orderbook
api_type: Market Data
updated_at: 2026-11-13 19:22:32.581032
---

# Get Orderbook

Query 25-level orderbook data for an Event Contract symbol.

### HTTP Request

GET`/v5/event/orderbook`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
symbol| **true**|  string| Symbol name, e.g. `ETHUSDT-28AUG26-2450-2570-OUT`  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
s| string| Symbol name  
r| array| Orderbook entries. Up to 25 levels. Each entry is `[payoutRatio, orderValue]`  
ts| integer| Matching engine timestamp in milliseconds  
u| integer| Update ID  
seq| integer| Cross sequence number  
cts| integer| Creation timestamp in milliseconds  
  
* * *

### Request Example
    
    
    GET /v5/event/orderbook?symbol=ETHUSDT-28AUG26-2450-2570-OUT HTTP/1.1  
    Host: api.bybit.com  
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "s": "BTCUSDT-5MIN-UP",  
            "r": [  
                [  
                    "0.90",  
                    "50000"  
                ]  
            ],  
            "ts": 1716863719031,  
            "u": 230704,  
            "seq": 1432604333,  
            "cts": 1716863718905  
        },  
        "retExtInfo": {},  
        "time": 1716863719382  
    }

---

# 查詢訂單簿

查詢 Event Contract 交易對的 25 檔訂單簿數據。

### HTTP 請求

GET`/v5/event/orderbook`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
symbol| **true**|  string| 交易對名稱，如 `ETHUSDT-28AUG26-2450-2570-OUT`  
  
### 返回參數

參數| 類型| 說明  
---|---|---  
s| string| 交易對名稱  
r| array| 訂單簿條目，最多 25 檔。每條格式為 `[賠付比率, 訂單金額]`  
ts| integer| 撮合引擎時間戳（毫秒）  
u| integer| 更新 ID  
seq| integer| 跨業務序號  
cts| integer| 創建時間戳（毫秒）  
  
* * *

### 請求示例
    
    
    GET /v5/event/orderbook?symbol=ETHUSDT-28AUG26-2450-2570-OUT HTTP/1.1  
    Host: api.bybit.com  
    

### 返回示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "s": "BTCUSDT-5MIN-UP",  
            "r": [  
                [  
                    "0.90",  
                    "50000"  
                ]  
            ],  
            "ts": 1716863719031,  
            "u": 230704,  
            "seq": 1432604333,  
            "cts": 1716863718905  
        },  
        "retExtInfo": {},  
        "time": 1716863719382  
    }