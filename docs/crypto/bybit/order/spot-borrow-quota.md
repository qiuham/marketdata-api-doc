---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/order/spot-borrow-quota
api_type: Trading
updated_at: 2026-10-06 18:52:38.921312
---

# Get Delay Liquidation Status

Query the current LTV, liquidation status, and delay liquidation timing information for an institutional loan account.

info

  * The API key must belong to an institutional lending account.
  * Rate limit: 2 requests per second per UID per endpoint (`2 req/s/uid/path`).



### HTTP Request

GET`/v5/ins-loan/delay-liq-status`

### Request Parameters

None.

### Response Parameters

Parameter| Type| Comments  
---|---|---  
ltv| string| Current LTV (Loan-to-Value) ratio  
liquidationStatus| integer| Liquidation status 

  * `0`: Normal
  * `1`: Passive liquidation in progress
  * `2`: Callback liquidation in progress
  * `3`: Delay liquidation in progress

  
delayLiqStartTime| string| Delay liquidation start time (Unix timestamp in milliseconds). Only populated when `liquidationStatus` = `3`. Returns `"0"` in normal status.  
delayLiqRemainingSec| string| Remaining seconds of the delay liquidation grace period. Only populated when `liquidationStatus` = `3`. Returns an empty string in normal status.  
  
### Request Example

  * HTTP


    
    
    GET /v5/ins-loan/delay-liq-status HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1789012718462  
    X-BAPI-RECV-WINDOW: 5000  
    X-BAPI-SIGN: XXXXX  
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "",  
        "result": {  
            "ltv": "0.8523",  
            "liquidationStatus": 0,  
            "delayLiqStartTime": "0",  
            "delayLiqRemainingSec": ""  
        },  
        "retExtInfo": {},  
        "time": 1789012718462  
    }

---

# 查詢延遲強平狀態

查詢機構借貸帳戶當前的風險率（LTV）、強平狀態及延遲強平時間信息。

信息

  * API Key 必須屬於機構借貸帳戶。
  * 限流：每個 UID 的此接口每秒最多 2 次請求（`2 req/s/uid/path`）。



### HTTP 請求

GET`/v5/ins-loan/delay-liq-status`

### 請求參數

無。

### 返回參數

參數| 類型| 說明  
---|---|---  
ltv| string| 當前風險率（LTV，貸款價值比）  
liquidationStatus| integer| 強平狀態 

  * `0`：正常
  * `1`：被動強平中
  * `2`：回調強平中
  * `3`：延遲強平中

  
delayLiqStartTime| string| 延遲強平開始時間，Unix 時間戳（毫秒）。僅當 `liquidationStatus` = `3` 時有值，正常狀態下返回 `"0"`。  
delayLiqRemainingSec| string| 延遲強平寬限期的剩餘秒數。僅當 `liquidationStatus` = `3` 時有值，正常狀態下返回空字串。  
  
### 請求示例

  * HTTP


    
    
    GET /v5/ins-loan/delay-liq-status HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1789012718462  
    X-BAPI-RECV-WINDOW: 5000  
    X-BAPI-SIGN: XXXXX  
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "",  
        "result": {  
            "ltv": "0.8523",  
            "liquidationStatus": 0,  
            "delayLiqStartTime": "0",  
            "delayLiqRemainingSec": ""  
        },  
        "retExtInfo": {},  
        "time": 1789012718462  
    }