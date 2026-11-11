---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/finance/advanced-earn/liquidity-mining/order
api_type: REST
updated_at: 2026-11-11 18:28:49.585638
---

# Reinvest

info

  * Need authentication. **Up to 5 requests** per second per UID. Requires Earn permission on the API key.
  * Reinvests the claimable yield of the specified position back into the pool.
  * Orders are processed asynchronously. A successful response means the order was accepted. Use [Get Order Info](/docs/v5/finance/advanced-earn/liquidity-mining/order) to track order status.
  * `orderLinkId` is used for idempotency — resubmitting the same `orderLinkId` returns an error indicating the order already exists.
  * Only one pending order is allowed per position at a time.



### HTTP Request

POST`/v5/earn/liquidity-mining/reinvest`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
productId| **true**|  string| Product ID  
orderLinkId| **true**|  string| User-customised order ID (max 40 characters)  
positionId| **true**|  string| Position ID to reinvest. Obtain from [Get Position Info](/docs/v5/finance/advanced-earn/liquidity-mining/position)  
leverage| false| string| Leverage multiplier (integer only); defaults to `"1"` (no leverage)  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
orderId| string| System-generated order ID  
orderLinkId| string| User-customised order ID  
  
* * *

### Request Example
    
    
    POST /v5/earn/liquidity-mining/reinvest HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1741651200000  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "productId": "5",  
        "orderLinkId": "lm-reinvest-01",  
        "positionId": "1498"  
    }  
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "",  
        "result": {  
            "orderId": "c3d4e5f6-a7b8-9012-cdef-123456789012",  
            "orderLinkId": "lm-reinvest-01"  
        },  
        "retExtInfo": {},  
        "time": 1741651200000  
    }

---

# 複利再投

信息

  * 需要身份驗證。每個 UID 每秒**最多 5 次請求** 。API 金鑰需要具備 Earn（理財）權限。
  * 將指定持倉的可領取收益再投入流動性池。
  * 訂單為非同步處理。成功響應表示訂單已被接受。請使用[查詢訂單資訊](/docs/zh-TW/v5/finance/advanced-earn/liquidity-mining/order)追蹤訂單狀態。
  * `orderLinkId` 用於保證冪等性——重複提交相同的 `orderLinkId` 時，系統將返回訂單已存在的錯誤。
  * 每個持倉同一時間只允許存在一筆待處理訂單。



### HTTP 請求

POST`/v5/earn/liquidity-mining/reinvest`

### 請求參數

參數| 必填| 類型| 說明  
---|---|---|---  
productId| **true**|  string| 產品 ID  
orderLinkId| **true**|  string| 用戶自定義訂單 ID（最多 40 個字元）  
positionId| **true**|  string| 要執行再投資的持倉 ID。可從[查詢持倉資訊](/docs/zh-TW/v5/finance/advanced-earn/liquidity-mining/position)獲取  
leverage| false| string| 槓桿倍數（僅限整數）；默認為 `"1"`（不使用槓桿）  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
orderId| string| 系統生成的訂單 ID  
orderLinkId| string| 用戶自定義訂單 ID  
  
* * *

### 請求示例
    
    
    POST /v5/earn/liquidity-mining/reinvest HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1741651200000  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "productId": "5",  
        "orderLinkId": "lm-reinvest-01",  
        "positionId": "1498"  
    }  
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "",  
        "result": {  
            "orderId": "c3d4e5f6-a7b8-9012-cdef-123456789012",  
            "orderLinkId": "lm-reinvest-01"  
        },  
        "retExtInfo": {},  
        "time": 1741651200000  
    }