---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/alpha/prediction/order-estimate
api_type: REST
updated_at: 2026-07-23 18:52:17.872826
---

# Get Position History

Query the authenticated user's closed prediction market positions. Includes settlement results (WIN/LOSE) for resolved events.

### HTTP Request

POST`/v5/alpha/prediction/position-history`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
tokenId| false| string| Filter by outcome token ID  
eventId| false| string| Filter by event ID  
result| false| integer| Filter by position outcome. Refer to [predictionPositionResult](/docs/v5/enum#predictionpositionresult-prediction-market--position-result)  
days| false| integer| Look back N days. Max: `90`  
limit| false| integer| Number of records per page  
pageIndex| false| integer| Page number starting from `1`  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
positions| array| Closed position records  
> positionId| string| Position ID  
> tokenId| string| Outcome token ID  
> eventId| string| Event ID  
> outcomeName| string| Outcome label (e.g., `YES`, `NO`)  
> shares| string| Total shares that were held  
> cost| string| Total USDC cost of this position  
> avgPrice| string| Average cost price per share  
> exitPrice| string| Price at which the position was closed  
> realizedPnl| string| Realized profit/loss (USDC). Positive = profit  
> realizedPnlRate| string| Realized P&L as decimal ratio  
> result| integer| Position outcome. Refer to [predictionPositionResult](/docs/v5/enum#predictionpositionresult-prediction-market--position-result)  
> closedAt| integer| Position close timestamp (UTC milliseconds)  
total| integer| Total matching records  
  
### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    POST /v5/alpha/prediction/position-history HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1704067200000  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "limit": 20,  
        "pageIndex": 1,  
        "days": 30  
    }  
    
    
    
      
    
    
    
      
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "positions": [  
                {  
                    "positionId": "pos_456",  
                    "tokenId": "token_yes_456",  
                    "eventId": "event_456",  
                    "outcomeName": "YES",  
                    "shares": "200",  
                    "cost": "140.00",  
                    "avgPrice": "0.70",  
                    "exitPrice": "1.00",  
                    "realizedPnl": "60.00",  
                    "realizedPnlRate": "0.429",  
                    "result": 1,  
                    "closedAt": 1704153600000  
                }  
            ],  
            "total": 1  
        },  
        "retExtInfo": {},  
        "time": 1704067200000  
    }

---

# 獲取歷史持倉

查詢已登錄用戶的預測市場已平倉記錄，包含已結算賽事的結果（WIN/LOSE）。

### HTTP 請求

POST`/v5/alpha/prediction/position-history`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
tokenId| false| string| 按結果代幣 ID 篩選  
eventId| false| string| 按賽事 ID 篩選  
result| false| integer| 按倉位結果篩選。參考 [predictionPositionResult](/docs/zh-TW/v5/enum#predictionpositionresult-prediction-market--position-result)  
days| false| integer| 回溯天數，最大 `90`  
limit| false| integer| 每頁記錄數  
pageIndex| false| integer| 頁碼，從 `1` 開始  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
positions| array| 已平倉記錄  
> positionId| string| 持倉 ID  
> tokenId| string| 結果代幣 ID  
> eventId| string| 賽事 ID  
> outcomeName| string| 結果標籤（如 `YES`、`NO`）  
> shares| string| 持有的總份額  
> cost| string| 本倉位的總 USDC 成本  
> avgPrice| string| 每份額的平均成本價  
> exitPrice| string| 平倉價格  
> realizedPnl| string| 已實現盈虧（USDC），正數為盈利  
> realizedPnlRate| string| 已實現盈虧比率  
> result| integer| 倉位結果。參考 [predictionPositionResult](/docs/zh-TW/v5/enum#predictionpositionresult-prediction-market--position-result)  
> closedAt| integer| 平倉時間戳（UTC 毫秒）  
total| integer| 符合條件的總記錄數  
  
### 請求示例

  * HTTP
  * Python
  * Node.js


    
    
    POST /v5/alpha/prediction/position-history HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1704067200000  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "limit": 20,  
        "pageIndex": 1,  
        "days": 30  
    }  
    
    
    
      
    
    
    
      
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "positions": [  
                {  
                    "positionId": "pos_456",  
                    "tokenId": "token_yes_456",  
                    "eventId": "event_456",  
                    "outcomeName": "YES",  
                    "shares": "200",  
                    "cost": "140.00",  
                    "avgPrice": "0.70",  
                    "exitPrice": "1.00",  
                    "realizedPnl": "60.00",  
                    "realizedPnlRate": "0.429",  
                    "result": 1,  
                    "closedAt": 1704153600000  
                }  
            ],  
            "total": 1  
        },  
        "retExtInfo": {},  
        "time": 1704067200000  
    }