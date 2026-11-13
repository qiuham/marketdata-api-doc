---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/finance/earn/fixed-saving/place-order
api_type: REST
updated_at: 2026-11-13 18:27:40.814979
---

# Place Order

API ker permission: `Earn`  
API rate limit: 5 reqs / sec

info

  * Orders are processed asynchronously. A successful response means the order was accepted, not that it has been settled. Use [Get Order List](/docs/v5/finance/earn/fixed-saving/order) to track order status.
  * `orderLinkId` is used for idempotency — resubmitting the same `orderLinkId` returns an error indicating the order already exists.
  * `auto_invest` is only applicable when `category` is `FundPool`; it is ignored for other product types.
  * Supported account types: `FUND`, `UNIFIED`.



### HTTP Request

POST`/v5/earn/fixed-term/place-order`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
productId| **true**|  string| Product ID  
category| **true**|  string| Product sub-type: `FixedTermSaving`, `FundPool`, `FundPoolPremium`  
coin| **true**|  string| Coin name, e.g. `BTC`, `ETH`  
amount| **true**|  string| Subscription amount (must be > 0)  
accountType| **true**|  string| Account type: `FUND` or `UNIFIED`  
orderLinkId| **true**|  string| User-customised idempotent ID (max 36 characters)  
autoInvest| false| boolean| Enable auto-reinvest. Only effective when `category` is `FundPool`  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
orderId| string| System-generated order ID  
orderLinkId| string| User-customised idempotent ID  
  
* * *

### Request Example
    
    
    POST /v5/earn/fixed-term/place-order HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1741651200000  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "category": "FixedTermSaving",  
        "accountType": "FUND",  
        "amount": "201",  
        "coin": "USDT",  
        "productId": "724",  
        "orderLinkId": "usdt-fixdearn-001"  
    }  
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "",  
        "result": {  
            "orderId": "86468516-5497-4a2b-8c4c-f9c58e01e12c",  
            "orderLinkId": "usdt-fixdearn-001"  
        },  
        "retExtInfo": {},  
        "time": 1776068177658  
    }

---

# 下單

API key權限：`Earn`  
API 頻率限制：每秒5次

信息

  * 訂單非同步處理。成功響應表示訂單已被接受，而非已結算。請使用[取得訂單列表](/docs/zh-TW/v5/finance/earn/fixed-saving/order)追蹤訂單狀態。
  * `orderLinkId` 用於保證冪等性——重複提交相同的 `orderLinkId` 時，系統將返回訂單已存在的錯誤。
  * `autoInvest` 僅在 `category` 為 `FundPool` 時有效，對其他產品類型無效。
  * 支持的帳戶類型：`FUND`、`UNIFIED`。



### HTTP 請求

POST`/v5/earn/fixed-term/place-order`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
productId| **true**|  string| 產品ID  
category| **true**|  string| 產品子類型：`FixedTermSaving`、`FundPool`、`FundPoolPremium`  
coin| **true**|  string| 幣種名稱，例如 `BTC`、`ETH`  
amount| **true**|  string| 訂閱金額（必須 > 0）  
accountType| **true**|  string| 帳戶類型：`FUND` 或 `UNIFIED`  
orderLinkId| **true**|  string| 用戶自訂冪等ID（最多36個字符）  
autoInvest| false| boolean| 啟用自動續投。僅在 `category` 為 `FundPool` 時有效  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
orderId| string| 系統生成的訂單ID  
orderLinkId| string| 用戶自訂冪等ID  
  
* * *

### 請求示例
    
    
    POST /v5/earn/fixed-term/place-order HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1741651200000  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "category": "FixedTermSaving",  
        "accountType": "FUND",  
        "amount": "201",  
        "coin": "USDT",  
        "productId": "724",  
        "orderLinkId": "usdt-fixdearn-001"  
    }  
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "",  
        "result": {  
            "orderId": "86468516-5497-4a2b-8c4c-f9c58e01e12c",  
            "orderLinkId": "usdt-fixdearn-001"  
        },  
        "retExtInfo": {},  
        "time": 1776068177658  
    }