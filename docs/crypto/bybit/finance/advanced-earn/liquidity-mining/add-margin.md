---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/finance/advanced-earn/liquidity-mining/add-margin
api_type: REST
updated_at: 2026-11-13 19:22:52.914652
---

# Add Margin

info

  * Need authentication. **Up to 5 requests** per second per UID. Requires Earn permission on the API key.
  * Adds additional margin (in quoteCoin) to a leveraged position to reduce liquidation risk.
  * Orders are processed asynchronously. A successful response means the order was accepted. Use [Get Order Info](/docs/v5/finance/advanced-earn/liquidity-mining/order) to track order status.
  * `orderLinkId` is used for idempotency — resubmitting the same `orderLinkId` returns an error indicating the order already exists.
  * Only one pending order is allowed per position at a time.



### HTTP Request

POST`/v5/earn/liquidity-mining/add-margin`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
productId| **true**|  string| Product ID  
orderLinkId| **true**|  string| User-customised order ID (max 40 characters)  
positionId| **true**|  string| Position ID to add margin to. Obtain from [Get Position Info](/docs/v5/finance/advanced-earn/liquidity-mining/position)  
amount| **true**|  string| Amount of quoteCoin to add as margin (e.g. USDT)  
quoteAccountType| **true**|  string| Source account for the margin: `FUND`, `UNIFIED`  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
orderId| string| System-generated order ID  
orderLinkId| string| User-customised order ID  
  
* * *

### Request Example
    
    
    POST /v5/earn/liquidity-mining/add-margin HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1741651200000  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "productId": "5",  
        "orderLinkId": "lm-add-m-01",  
        "positionId": "1498",  
        "amount": "1000",  
        "quoteAccountType": "FUND"  
    }  
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "",  
        "result": {  
            "orderId": "91720e72-86f8-4ee7-a22c-47f01a9a14e9",  
            "orderLinkId": "lm-add-m-01"  
        },  
        "retExtInfo": {},  
        "time": 1775124668762  
    }

---

# 追加保證金

信息

  * 需要身份驗證。每個 UID 每秒**最多 5 次請求** 。API 金鑰需要具備 Earn（理財）權限。
  * 向槓桿持倉追加額外保證金（以計價幣種計），以降低強制平倉風險。
  * 訂單為非同步處理。成功響應表示訂單已被接受。請使用[查詢訂單資訊](/docs/zh-TW/v5/finance/advanced-earn/liquidity-mining/order)追蹤訂單狀態。
  * `orderLinkId` 用於保證冪等性——重複提交相同的 `orderLinkId` 時，系統將返回訂單已存在的錯誤。
  * 每個持倉同一時間只允許存在一筆待處理訂單。



### HTTP 請求

POST`/v5/earn/liquidity-mining/add-margin`

### 請求參數

參數| 必填| 類型| 說明  
---|---|---|---  
productId| **true**|  string| 產品 ID  
orderLinkId| **true**|  string| 用戶自定義訂單 ID（最多 40 個字元）  
positionId| **true**|  string| 要追加保證金的持倉 ID。可從[查詢持倉資訊](/docs/zh-TW/v5/finance/advanced-earn/liquidity-mining/position)獲取  
amount| **true**|  string| 追加的計價幣種保證金金額（例如 USDT）  
quoteAccountType| **true**|  string| 保證金來源帳戶：`FUND`、`UNIFIED`  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
orderId| string| 系統生成的訂單 ID  
orderLinkId| string| 用戶自定義訂單 ID  
  
* * *

### 請求示例
    
    
    POST /v5/earn/liquidity-mining/add-margin HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1741651200000  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "productId": "5",  
        "orderLinkId": "lm-add-m-01",  
        "positionId": "1498",  
        "amount": "1000",  
        "quoteAccountType": "FUND"  
    }  
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "",  
        "result": {  
            "orderId": "91720e72-86f8-4ee7-a22c-47f01a9a14e9",  
            "orderLinkId": "lm-add-m-01"  
        },  
        "retExtInfo": {},  
        "time": 1775124668762  
    }