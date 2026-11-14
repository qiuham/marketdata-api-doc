---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/alpha/prediction/sports-timeline-stages
api_type: REST
updated_at: 2026-11-13 19:21:17.732514
---

# Get Sports Timeline Stages

Query the tournament timeline stages for a sports prediction event. Returns all stages with their status (Done, Active, Upcoming) and associated match counts. Useful for displaying tournament bracket progress.

### HTTP Request

GET`/v5/alpha/prediction/sports/timeline-stages`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
eventType| **true**|  integer| Sports event type. Refer to [predictionEventType](/docs/v5/enum#predictioneventtype-prediction-market--event-type). Phase 1: `1` (FIFA_2026)  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
eventType| integer| Sports event type  
stages| array| Tournament stage timeline  
> stageCode| string| Stage code. Refer to [predictionStageCode](/docs/v5/enum#predictionstagecode-prediction-market--stage-code)  
> stageName| string| Localized stage display name  
> status| integer| Stage status. Refer to [predictionTimelineStatus](/docs/v5/enum#predictiontimelinestatus-prediction-market--timeline-status)  
> matchCount| integer| Total number of matches in this stage  
> startTime| integer| Stage start timestamp (UTC milliseconds)  
> endTime| integer| Stage end timestamp (UTC milliseconds)  
  
### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/alpha/prediction/sports/timeline-stages?eventType=1 HTTP/1.1  
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
            "eventType": 1,  
            "stages": [  
                {  
                    "stageCode": "Groups",  
                    "stageName": "Group Stage",  
                    "status": 2,  
                    "matchCount": 48,  
                    "startTime": 1748995200000,  
                    "endTime": 1751500800000  
                },  
                {  
                    "stageCode": "R32",  
                    "stageName": "Round of 32",  
                    "status": 3,  
                    "matchCount": 16,  
                    "startTime": 1751587200000,  
                    "endTime": 1752192000000  
                },  
                {  
                    "stageCode": "R16",  
                    "stageName": "Round of 16",  
                    "status": 3,  
                    "matchCount": 8,  
                    "startTime": 1752278400000,  
                    "endTime": 1752624000000  
                },  
                {  
                    "stageCode": "QF",  
                    "stageName": "Quarter-Finals",  
                    "status": 3,  
                    "matchCount": 4,  
                    "startTime": 1752710400000,  
                    "endTime": 1752883200000  
                },  
                {  
                    "stageCode": "SF",  
                    "stageName": "Semi-Finals",  
                    "status": 3,  
                    "matchCount": 2,  
                    "startTime": 1752969600000,  
                    "endTime": 1753056000000  
                },  
                {  
                    "stageCode": "Final",  
                    "stageName": "Final",  
                    "status": 3,  
                    "matchCount": 1,  
                    "startTime": 1753142400000,  
                    "endTime": 1753228800000  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1704067200000  
    }

---

# 獲取賽事時間軸階段

查詢體育預測賽事的賽制時間軸階段，返回每個階段的狀態（已完成、進行中、即將開始）及關聯比賽場數，用於展示賽制進程。

### HTTP 請求

GET`/v5/alpha/prediction/sports/timeline-stages`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
eventType| **true**|  integer| 體育賽事類型。參考 [predictionEventType](/docs/zh-TW/v5/enum#predictioneventtype-prediction-market--event-type)。第一階段：`1`（FIFA_2026）  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
eventType| integer| 體育賽事類型  
stages| array| 賽制時間軸階段列表  
> stageCode| string| 階段代碼。參考 [predictionStageCode](/docs/zh-TW/v5/enum#predictionstagecode-prediction-market--stage-code)  
> stageName| string| 階段本地化顯示名稱  
> status| integer| 階段狀態。參考 [predictionTimelineStatus](/docs/zh-TW/v5/enum#predictiontimelinestatus-prediction-market--timeline-status)  
> matchCount| integer| 該階段的總比賽場數  
> startTime| integer| 階段開始時間戳（UTC 毫秒）  
> endTime| integer| 階段結束時間戳（UTC 毫秒）  
  
### 請求示例

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/alpha/prediction/sports/timeline-stages?eventType=1 HTTP/1.1  
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
            "eventType": 1,  
            "stages": [  
                {  
                    "stageCode": "Groups",  
                    "stageName": "Group Stage",  
                    "status": 2,  
                    "matchCount": 48,  
                    "startTime": 1748995200000,  
                    "endTime": 1751500800000  
                },  
                {  
                    "stageCode": "Final",  
                    "stageName": "Final",  
                    "status": 3,  
                    "matchCount": 1,  
                    "startTime": 1753142400000,  
                    "endTime": 1753228800000  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1704067200000  
    }