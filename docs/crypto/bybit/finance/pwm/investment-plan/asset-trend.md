---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/finance/pwm/investment-plan/asset-trend
api_type: REST
updated_at: 2026-05-27 19:17:57.067445
---

# Get Asset Trend

### HTTP Request

GET`/v5/earn/pwm/investment-plan/asset-trend`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
planId| **true**|  string| Investment plan ID  
startTime| false| int| Start timestamp (ms). Default: current time minus 7 days  
endTime| false| int| End timestamp (ms). Default: current time  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
planId| string| Investment plan ID  
dataPoints| array| Asset data point list, sorted in ascending order by date  
> date| string| Date in `YYYY-MM-DD` format  
> assetValueUsd| string| Total plan assets on that day (USD valuation), taken from the daily settlement snapshot  
  
* * *

### Request Example
    
    
    GET /v5/earn/pwm/investment-plan/asset-trend?planId=10001 HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1741651200000  
    X-BAPI-RECV-WINDOW: 5000  
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "result": {  
            "planId": "10001",  
            "dataPoints": [  
                {  
                    "date": "2024-11-01",  
                    "assetValueUsd": "198500.00"  
                },  
                {  
                    "date": "2024-11-02",  
                    "assetValueUsd": "199100.00"  
                }  
            ]  
        }  
    }

---

# 查詢資產趨勢曲線

### HTTP 請求

GET`/v5/earn/pwm/investment-plan/asset-trend`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
planId| **true**|  string| 投資計劃ID  
startTime| false| int| 起始時間戳（ms），默認當前時間-7天  
endTime| false| int| 結束時間戳（ms），默認當前時間  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
planId| string| 投資計劃ID  
dataPoints| array| 資產數據點列表，按日期升序排列  
> date| string| 日期，格式 `YYYY-MM-DD`  
> assetValueUsd| string| 當日計劃總資產（USD估值），取每日結算快照值  
  
* * *

### 請求示例
    
    
    GET /v5/earn/pwm/investment-plan/asset-trend?planId=10001 HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1741651200000  
    X-BAPI-RECV-WINDOW: 5000  
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "result": {  
            "planId": "10001",  
            "dataPoints": [  
                {  
                    "date": "2024-11-01",  
                    "assetValueUsd": "198500.00"  
                },  
                {  
                    "date": "2024-11-02",  
                    "assetValueUsd": "199100.00"  
                }  
            ]  
        }  
    }