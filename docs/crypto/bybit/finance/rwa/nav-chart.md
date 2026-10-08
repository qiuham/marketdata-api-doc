---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/finance/rwa/nav-chart
api_type: REST
updated_at: 2026-10-08 18:48:48.422538
---

# Get NAV Chart

info

  * Authentication is not required.
  * `startTime` defaults to 7 days before `endTime`. `endTime` defaults to current time.
  * The time span (`endTime - startTime`) must not exceed 180 days.
  * **Rate Limit:** 20 req/s (IP)



### HTTP Request

GET`/v5/earn/rwa/nav-chart`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
productId| **true**|  integer| Product ID  
startTime| false| integer| Start timestamp (Unix seconds). Default: `endTime - 7 days`  
endTime| false| integer| End timestamp (Unix seconds). Default: now  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
productId| integer| Product ID  
list| array| NAV data points in ascending order by date  
> date| string| Date in `YYYY-MM-DD` format (UTC)  
> nav| string| NAV (Net Asset Value per share) on the given date  
  
* * *

### Request Example
    
    
    GET /v5/earn/rwa/nav-chart?productId=1001 HTTP/1.1  
    Host: api.bybit.com  
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "success",  
        "result": {  
            "productId": 1001,  
            "list": [  
                {  
                    "date": "2024-03-10",  
                    "nav": "1.024"  
                },  
                {  
                    "date": "2024-03-11",  
                    "nav": "1.025"  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1710691200000  
    }

---

# 獲取NAV歷史數據

信息

  * 無需身份驗證。
  * `startTime` 默認為 `endTime` 的 7 天前；`endTime` 默認為當前時間。
  * 時間跨度（`endTime - startTime`）不得超過 180 天。
  * **頻率限制：** 20 次/秒（IP）



### HTTP 請求

GET`/v5/earn/rwa/nav-chart`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
productId| **true**|  integer| 產品 ID  
startTime| false| integer| 起始時間戳（Unix 秒）。默認：`endTime - 7 天`  
endTime| false| integer| 結束時間戳（Unix 秒）。默認：當前時間  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
productId| integer| 產品 ID  
list| array| NAV 數據點列表，按日期升序排列  
> date| string| 日期，格式 `YYYY-MM-DD`（UTC）  
> nav| string| 當日 NAV（單份淨值）  
  
* * *

### 請求示例
    
    
    GET /v5/earn/rwa/nav-chart?productId=1001 HTTP/1.1  
    Host: api.bybit.com  
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "success",  
        "result": {  
            "productId": 1001,  
            "list": [  
                {  
                    "date": "2024-03-10",  
                    "nav": "1.024"  
                },  
                {  
                    "date": "2024-03-11",  
                    "nav": "1.025"  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1710691200000  
    }