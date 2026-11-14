---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/alpha/prediction/portfolio-summary
api_type: REST
updated_at: 2026-11-13 19:21:11.034449
---

# Get Portfolio Summary

Query the authenticated user's overall prediction market portfolio summary, including total invested value, current value, realized and unrealized P&L.

### HTTP Request

POST`/v5/alpha/prediction/portfolio-summary`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
eventType| false| integer| Filter by event type. Refer to [predictionEventType](/docs/v5/enum#predictioneventtype-prediction-market--event-type)  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
positionValue| string| Current total market value of all open positions (USDC)  
positionValueUsd| string| Current total market value denominated in USD  
biggestWin| string| Largest single realized profit (USDC)  
winRate| string| Win rate as decimal ratio (e.g. `"0.67"` = 67%)  
winCount| integer| Number of winning closed positions  
lossCount| integer| Number of losing closed positions  
  
### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    POST /v5/alpha/prediction/portfolio-summary HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1704067200000  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {}  
    
    
    
      
    
    
    
      
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "positionValue": "580.00",  
            "positionValueUsd": "580.00",  
            "biggestWin": "120.00",  
            "winRate": "0.67",  
            "winCount": 10,  
            "lossCount": 5  
        },  
        "retExtInfo": {},  
        "time": 1704067200000  
    }

---

# 獲取資產概覽

查詢已登錄用戶的預測市場資產概覽，包含持倉總市值、最大盈利及勝率統計。

### HTTP 請求

POST`/v5/alpha/prediction/portfolio-summary`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
eventType| false| integer| 按賽事類型篩選。參考 [predictionEventType](/docs/zh-TW/v5/enum#predictioneventtype-prediction-market--event-type)  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
positionValue| string| 所有開倉持倉的當前總市值（USDC）  
positionValueUsd| string| 所有開倉持倉的當前總市值（USD）  
biggestWin| string| 單筆最大已實現盈利（USDC）  
winRate| string| 勝率（小數比率，如 `"0.67"` = 67%）  
winCount| integer| 盈利平倉持倉數量  
lossCount| integer| 虧損平倉持倉數量  
  
### 請求示例

  * HTTP
  * Python
  * Node.js


    
    
    POST /v5/alpha/prediction/portfolio-summary HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1704067200000  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {}  
    
    
    
      
    
    
    
      
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "positionValue": "580.00",  
            "positionValueUsd": "580.00",  
            "biggestWin": "120.00",  
            "winRate": "0.67",  
            "winCount": 10,  
            "lossCount": 5  
        },  
        "retExtInfo": {},  
        "time": 1704067200000  
    }