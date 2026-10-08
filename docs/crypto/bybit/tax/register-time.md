---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/tax/register-time
api_type: REST
updated_at: 2026-10-08 18:52:30.256100
---

# Get User Register Date

Get User Register Date

### HTTP Request

POST `/fht/compliance/tax/v3/private/registertime`

### Request Parameters

None

### Response Parameters

Parameter| Type| Comments  
---|---|---  
registerTime| string| UNIX Time. This is in seconds. Date that the specific user registers on the platform  
  
### Request Example
    
    
    POST /fht/compliance/tax/v3/private/registertime HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN-TYPE: 2  
    X-BAPI-SIGN: xxxxxxxxxxxxxx  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1671183584043  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
    {}  
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "registerTime": "1634515200"  
        },  
        "retExtInfo": {},  
        "time": 1671183584270  
    }

---

# 查詢特定用戶在平台註冊日期

### HTTP 請求

POST `/fht/compliance/tax/v3/private/registertime`

### 請求參數

無

### 響應參數

參數| 類型| 說明  
---|---|---  
registerTime| string| 特定用戶在平台上註冊的日期 (秒級unix時間戳)  
  
### 請求示例
    
    
    POST /fht/compliance/tax/v3/private/registertime HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN-TYPE: 2  
    X-BAPI-SIGN: xxxxxxxxxxxxxx  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1671183584043  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
    {}  
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "registerTime": "1634515200"  
        },  
        "retExtInfo": {},  
        "time": 1671183584270  
    }