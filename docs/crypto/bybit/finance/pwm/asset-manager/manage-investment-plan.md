---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/finance/pwm/asset-manager/manage-investment-plan
api_type: REST
updated_at: 2026-07-07 19:13:01.513939
---

# Create Customize Investment Plan

info

The total number of **Active** and **Pending** plans for the current user cannot exceed **20**.

### HTTP Request

POST`/v5/earn/pwm/customize-plan/create`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
accountType| false| string| Source account type. Default: `FUND`  
products| **true**|  array| Product configuration list. At least 1 item required  
> category| **true**|  string| Pass through from product query result. Product category: `multiCoinEarning` / `fixedYield` / `equityFund` / `onchainEarn`  
> productId| **true**|  string| Pass through from product query result. May be `0`  
> fundName| **true**|  string| Pass through from product query result. May be empty  
> amount| **true**|  string| Subscription amount (base coin)  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
planId| string| Newly created investment plan ID  
planName| string| Investment plan name, auto-generated in the format `PWM-{planId}`  
status| string| Plan status. Created and subscribed in one step — `Active` upon success  
orderLinkId| string| User-defined order ID  
  
* * *

### Request Example
    
    
    POST /v5/earn/pwm/customize-plan/create HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1741651200000  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "accountType": "FUND",  
        "products": [  
            {  
                "category": "equityFund",  
                "productId": "2001",  
                "fundName": "Market Neutral Alpha",  
                "amount": "100000.00"  
            },  
            {  
                "category": "multiCoinEarning",  
                "productId": "430",  
                "fundName": "",  
                "amount": "50000.00"  
            }  
        ]  
    }  
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "result": {  
            "planId": "10050",  
            "planName": "PWM-10050",  
            "status": "Active",  
            "orderLinkId": "xxx"  
        }  
    }

---

# 創建自定義投資計劃（直客模式）

信息

當前用戶 **Active** （運行中）和 **Pending** （待處理）狀態的計劃總數不能超過 **20** 個。

### HTTP 請求

POST`/v5/earn/pwm/customize-plan/create`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
accountType| false| string| 資金來源賬戶類型，默認 `FUND`  
products| **true**|  array| 產品配置列表，至少 1 個  
> category| **true**|  string| 透傳product查詢結果，產品類別：`multiCoinEarning` / `fixedYield` / `equityFund` / `onchainEarn`  
> productId| **true**|  string| 透傳product查詢結果，可能為 `0`  
> fundName| **true**|  string| 透傳product查詢結果，可能為空  
> amount| **true**|  string| 申購金額（本位幣）  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
planId| string| 新創建的投資計劃ID  
planName| string| 投資計劃名稱，自動生成格式為 `PWM-{planId}`  
status| string| 計劃狀態，創建即申購，成功後為 `Active`  
orderLinkId| string| 用戶自定義訂單ID  
  
* * *

### 請求示例
    
    
    POST /v5/earn/pwm/customize-plan/create HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1741651200000  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "accountType": "FUND",  
        "products": [  
            {  
                "category": "equityFund",  
                "productId": "2001",  
                "fundName": "Market Neutral Alpha",  
                "amount": "100000.00"  
            },  
            {  
                "category": "multiCoinEarning",  
                "productId": "430",  
                "fundName": "",  
                "amount": "50000.00"  
            }  
        ]  
    }  
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "result": {  
            "planId": "10050",  
            "planName": "PWM-10050",  
            "status": "Active",  
            "orderLinkId": "xxx"  
        }  
    }