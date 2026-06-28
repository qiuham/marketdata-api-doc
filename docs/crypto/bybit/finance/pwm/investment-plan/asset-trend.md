---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/finance/pwm/investment-plan/asset-trend
api_type: REST
updated_at: 2026-06-28 19:11:45.599694
---

# Get Fund Historical NAV

info

The maximum allowed time range between `startTime` and `endTime` is **180 days**.

### HTTP Request

GET`/v5/earn/pwm/investment-plan/fund-nav`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
fundId| **true**|  string| Fund ID  
startTime| false| int| Start timestamp (ms). Default: current time minus 7 days  
endTime| false| int| End timestamp (ms). Default: current time  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
fundId| string| Fund ID  
fundName| string| Fund name  
coin| string| Fund denomination coin  
currentNav| string| Latest NAV (= currentShareValue / initialShareValue)  
dataPoints| array| NAV data point list, sorted in ascending order by date  
> date| string| Date in `YYYY-MM-DD` format  
> nav| string| NAV for that day, taken from the daily settlement snapshot  
  
* * *

### Request Example
    
    
    GET /v5/earn/pwm/investment-plan/fund-nav?fundId=2001 HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1741651200000  
    X-BAPI-RECV-WINDOW: 5000  
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "result": {  
            "fundId": "2001",  
            "fundName": "Market Neutral Alpha",  
            "coin": "USDT",  
            "currentNav": "1.035",  
            "dataPoints": [  
                {  
                    "date": "2024-11-01",  
                    "nav": "1.028"  
                },  
                {  
                    "date": "2024-11-02",  
                    "nav": "1.031"  
                }  
            ]  
        }  
    }

---

# 查詢基金歷史淨值

信息

`startTime` 與 `endTime` 的時間範圍最多為 **180 天** 。

### HTTP 請求

GET`/v5/earn/pwm/investment-plan/fund-nav`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
fundId| **true**|  string| 基金ID  
startTime| false| int| 起始時間戳（ms），默認當前時間-7天  
endTime| false| int| 結束時間戳（ms），默認當前時間  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
fundId| string| 基金ID  
fundName| string| 基金名稱  
coin| string| 基金計價幣種  
currentNav| string| 最新淨值（= currentShareValue / initialShareValue）  
dataPoints| array| 淨值數據點列表，按日期升序排列  
> date| string| 日期，格式 `YYYY-MM-DD`  
> nav| string| 當日淨值，取每日結算快照  
  
* * *

### 請求示例
    
    
    GET /v5/earn/pwm/investment-plan/fund-nav?fundId=2001 HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1741651200000  
    X-BAPI-RECV-WINDOW: 5000  
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "result": {  
            "fundId": "2001",  
            "fundName": "Market Neutral Alpha",  
            "coin": "USDT",  
            "currentNav": "1.035",  
            "dataPoints": [  
                {  
                    "date": "2024-11-01",  
                    "nav": "1.028"  
                },  
                {  
                    "date": "2024-11-02",  
                    "nav": "1.031"  
                }  
            ]  
        }  
    }