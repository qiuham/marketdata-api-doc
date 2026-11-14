---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/alpha/prediction/engine-status
api_type: REST
updated_at: 2026-11-13 19:21:07.729176
---

# Get Engine Status

Query the availability status of the prediction market matching engine. When the engine is unavailable, buy and sell orders cannot be submitted.

info

  * Call this endpoint before placing any buy or sell order to verify the engine is available
  * If `available=false`, do not proceed with trading



### HTTP Request

GET`/v5/alpha/prediction/engine-status`

### Request Parameters

None

### Response Parameters

Parameter| Type| Comments  
---|---|---  
available| boolean| Whether the matching engine is currently available for trading  
  
### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/alpha/prediction/engine-status HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1704067200000  
    X-BAPI-RECV-WINDOW: 5000  
    
    
    
      
    
    
    
      
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "available": true  
        },  
        "retExtInfo": {},  
        "time": 1704067200000  
    }

---

# 獲取撮合引擎狀態

查詢預測市場撮合引擎的可用狀態。當引擎不可用時，無法提交買入或賣出委托。

信息

  * 在提交任何買入或賣出委托前，請先調用此接口確認引擎可用
  * 若 `available=false`，請勿進行交易



### HTTP 請求

GET`/v5/alpha/prediction/engine-status`

### 請求參數

無

### 響應參數

參數| 類型| 說明  
---|---|---  
available| boolean| 撮合引擎當前是否可用於交易  
  
### 請求示例

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/alpha/prediction/engine-status HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1704067200000  
    X-BAPI-RECV-WINDOW: 5000  
    
    
    
      
    
    
    
      
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "available": true  
        },  
        "retExtInfo": {},  
        "time": 1704067200000  
    }