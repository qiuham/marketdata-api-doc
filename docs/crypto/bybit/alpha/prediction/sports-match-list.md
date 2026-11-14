---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/alpha/prediction/sports-match-list
api_type: REST
updated_at: 2026-11-13 19:21:17.702352
---

# Get Sports Match List

Query the list of sports matches available in the prediction market. Supports filtering by competition type, match status, and date range. Phase 1 supports FIFA 2026 World Cup (`eventType=1`).

### HTTP Request

POST`/v5/alpha/prediction/sports/match-list`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
eventType| **true**|  integer| Sports event type. Refer to [predictionEventType](/docs/v5/enum#predictioneventtype-prediction-market--event-type). Phase 1: `1` (FIFA_2026)  
status| false| integer| Match status filter. Refer to [predictionMatchStatus](/docs/v5/enum#predictionmatchstatus-prediction-market--match-status)  
startTime| false| integer| Filter matches starting after this timestamp (UTC milliseconds)  
endTime| false| integer| Filter matches starting before this timestamp (UTC milliseconds)  
stageCode| false| string| Filter by tournament stage. Refer to [predictionStageCode](/docs/v5/enum#predictionstagecode-prediction-market--stage-code)  
limit| false| integer| Number of records per page  
pageIndex| false| integer| Page number starting from `1`  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
list| array| Match records  
> matchId| string| Match ID  
> eventType| integer| Sports event type. Refer to [predictionEventType](/docs/v5/enum#predictioneventtype-prediction-market--event-type)  
> stageCode| string| Tournament stage. Refer to [predictionStageCode](/docs/v5/enum#predictionstagecode-prediction-market--stage-code)  
> homeTeam| string| Home team name  
> awayTeam| string| Away team name  
> matchTime| integer| Match start timestamp (UTC milliseconds)  
> status| integer| Match status. Refer to [predictionMatchStatus](/docs/v5/enum#predictionmatchstatus-prediction-market--match-status)  
> eventId| string| Linked prediction event ID (if markets are available)  
total| integer| Total matching records  
pageIndex| integer| Current page number  
pageSize| integer| Items per page  
  
### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    POST /v5/alpha/prediction/sports/match-list HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1704067200000  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "eventType": 1,  
        "status": 2,  
        "limit": 20,  
        "pageIndex": 1  
    }  
    
    
    
      
    
    
    
      
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "list": [  
                {  
                    "matchId": "match_001",  
                    "eventType": 1,  
                    "stageCode": "Groups",  
                    "homeTeam": "Argentina",  
                    "awayTeam": "Brazil",  
                    "matchTime": 1750000000000,  
                    "status": 2,  
                    "eventId": "event_123"  
                }  
            ],  
            "total": 1,  
            "pageIndex": 1,  
            "pageSize": 20  
        },  
        "retExtInfo": {},  
        "time": 1704067200000  
    }

---

# 獲取體育賽事列表

查詢預測市場中的體育賽事列表，支持按賽制類型、賽事狀態及時間範圍篩選。第一階段支持 2026 FIFA 世界杯（`eventType=1`）。

### HTTP 請求

POST`/v5/alpha/prediction/sports/match-list`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
eventType| **true**|  integer| 體育賽事類型。參考 [predictionEventType](/docs/zh-TW/v5/enum#predictioneventtype-prediction-market--event-type)。第一階段：`1`（FIFA_2026）  
status| false| integer| 賽事狀態篩選。參考 [predictionMatchStatus](/docs/zh-TW/v5/enum#predictionmatchstatus-prediction-market--match-status)  
startTime| false| integer| 篩選此時間戳之後開始的賽事（UTC 毫秒）  
endTime| false| integer| 篩選此時間戳之前開始的賽事（UTC 毫秒）  
stageCode| false| string| 按賽制階段篩選。參考 [predictionStageCode](/docs/zh-TW/v5/enum#predictionstagecode-prediction-market--stage-code)  
limit| false| integer| 每頁記錄數  
pageIndex| false| integer| 頁碼，從 `1` 開始  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
list| array| 賽事記錄  
> matchId| string| 比賽 ID  
> eventType| integer| 體育賽事類型。參考 [predictionEventType](/docs/zh-TW/v5/enum#predictioneventtype-prediction-market--event-type)  
> stageCode| string| 賽制階段。參考 [predictionStageCode](/docs/zh-TW/v5/enum#predictionstagecode-prediction-market--stage-code)  
> homeTeam| string| 主隊名稱  
> awayTeam| string| 客隊名稱  
> matchTime| integer| 比賽開始時間戳（UTC 毫秒）  
> status| integer| 賽事狀態。參考 [predictionMatchStatus](/docs/zh-TW/v5/enum#predictionmatchstatus-prediction-market--match-status)  
> eventId| string| 關聯的預測賽事 ID（如有開放市場）  
total| integer| 符合條件的總記錄數  
pageIndex| integer| 當前頁碼  
pageSize| integer| 每頁記錄數  
  
### 請求示例

  * HTTP
  * Python
  * Node.js


    
    
    POST /v5/alpha/prediction/sports/match-list HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1704067200000  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "eventType": 1,  
        "status": 2,  
        "limit": 20,  
        "pageIndex": 1  
    }  
    
    
    
      
    
    
    
      
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "list": [  
                {  
                    "matchId": "match_001",  
                    "eventType": 1,  
                    "stageCode": "Groups",  
                    "homeTeam": "Argentina",  
                    "awayTeam": "Brazil",  
                    "matchTime": 1750000000000,  
                    "status": 2,  
                    "eventId": "event_123"  
                }  
            ],  
            "total": 1,  
            "pageIndex": 1,  
            "pageSize": 20  
        },  
        "retExtInfo": {},  
        "time": 1704067200000  
    }