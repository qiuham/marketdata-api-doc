---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/spread/trade/create-order
api_type: Trading
updated_at: 2026-05-27 19:22:33.881151
---

# Get Max Qty

Query the maximum order quantity for the given symbol.

### HTTP Request

GET`/v5/spread/max-qty`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
symbol| **true**|  string| Spread symbol name  
side| **true**|  string| Order side. `1`: Buy, `2`: Sell  
orderPrice| **true**|  string| Order price  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
ab| string| Maximum order quantity  
  
### Request Example
    
    
    GET /v5/spread/max-qty?symbol=SOLUSDT_SOL/USDT&side=1&orderPrice=50000 HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: XXXXXX  
    X-BAPI-TIMESTAMP: 1773230920000  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "Success",  
        "result": {  
            "ab": "1992.55199490"  
        },  
        "retExtInfo": {},  
        "time": 1774318807656  
    }

---

# 查詢最大下單數量

查詢指定交易對的最大下單數量。

### HTTP請求

GET`/v5/spread/max-qty`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
symbol| **true**|  string| 價差交易對名稱  
side| **true**|  string| 訂單方向. `1`: 買, `2`: 賣  
orderPrice| **true**|  string| 下單價格  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
ab| string| 最大下單數量  
  
### 請求示例
    
    
    GET /v5/spread/max-qty?symbol=SOLUSDT_SOL/USDT&side=1&orderPrice=50000 HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: XXXXXX  
    X-BAPI-TIMESTAMP: 1773230920000  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "Success",  
        "result": {  
            "ab": "1992.55199490"  
        },  
        "retExtInfo": {},  
        "time": 1774318807656  
    }