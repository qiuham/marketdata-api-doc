---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/finance/advanced-earn/dual-asset/product-quote
api_type: REST
updated_at: 2026-06-30 19:25:55.382069
---

# Add Liquidity

info

  * Need authentication. **Up to 5 requests** per second per UID. Requires Earn permission on the API key.
  * Orders are processed asynchronously. A successful response means the order was accepted, not that it has been settled. Use [Get Order Info](/docs/v5/finance/advanced-earn/liquidity-mining/order) to track order status (`Processing` → `Success`).
  * `orderLinkId` is used for idempotency — resubmitting the same `orderLinkId` returns an error indicating the order already exists.
  * At least one of `quoteAmount` or `baseAmount` must be provided.



### HTTP Request

POST`/v5/earn/liquidity-mining/add-liquidity`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
productId| **true**|  string| Product ID  
orderLinkId| **true**|  string| User-customised order ID (max 40 characters)  
quoteAmount| false| string| Amount of quoteCoin to inject (e.g. USDT). At least one of `quoteAmount` or `baseAmount` is required  
baseAmount| false| string| Amount of baseCoin to inject (e.g. BTC). At least one of `quoteAmount` or `baseAmount` is required  
quoteAccountType| false| string| Source account for quoteCoin: `FUND`, `UNIFIED`. Required when providing `quoteAmount`  
baseAccountType| false| string| Source account for baseCoin: `FUND`, `UNIFIED`. Required when providing `baseAmount`  
leverage| false| string| Leverage multiplier. Defaults to `1` (no leverage) if not provided  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
orderId| string| System-generated order ID  
orderLinkId| string| User-customised order ID  
  
* * *

### Request Example
    
    
    POST /v5/earn/liquidity-mining/add-liquidity HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1741651200000  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "productId": "36",  
        "coin": "USDT",  
        "quoteAmount": "200",  
        "quoteAccountType": "FUND",  
        "orderLinkId": "lm-001",  
        "leverage": "2"  
    }  
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "",  
        "result": {  
            "orderId": "5e651d09-6169-4f72-a609-8622ff421d19",  
            "orderLinkId": "lm-001"  
        },  
        "retExtInfo": {},  
        "time": 1775123507299  
    }

---

# 增加流動性

信息

  * 需要身份驗證。每個 UID 每秒**最多 5 次請求** 。API 金鑰需要具備 Earn（理財）權限。
  * 訂單為非同步處理。成功響應表示訂單已被接受，而非已結算。請使用[查詢訂單資訊](/docs/zh-TW/v5/finance/advanced-earn/liquidity-mining/order)追蹤訂單狀態（`Processing` → `Success`）。
  * `orderLinkId` 用於保證冪等性——重複提交相同的 `orderLinkId` 時，系統將返回訂單已存在的錯誤。
  * `quoteAmount` 與 `baseAmount` 至少須提供其中一個。



### HTTP 請求

POST`/v5/earn/liquidity-mining/add-liquidity`

### 請求參數

參數| 必填| 類型| 說明  
---|---|---|---  
productId| **true**|  string| 產品 ID  
orderLinkId| **true**|  string| 用戶自定義訂單 ID（最多 40 個字元）  
quoteAmount| false| string| 注入的計價幣種金額（例如 USDT）。`quoteAmount` 與 `baseAmount` 至少須提供其中一個  
baseAmount| false| string| 注入的基礎幣種金額（例如 BTC）。`quoteAmount` 與 `baseAmount` 至少須提供其中一個  
quoteAccountType| false| string| 計價幣種來源帳戶：`FUND`、`UNIFIED`。提供 `quoteAmount` 時必填  
baseAccountType| false| string| 基礎幣種來源帳戶：`FUND`、`UNIFIED`。提供 `baseAmount` 時必填  
leverage| false| string| 槓桿倍數。不提供時預設為 `1`（不使用槓桿）  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
orderId| string| 系統生成的訂單 ID  
orderLinkId| string| 用戶自定義訂單 ID  
  
* * *

### 請求示例
    
    
    POST /v5/earn/liquidity-mining/add-liquidity HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1741651200000  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "productId": "36",  
        "coin": "USDT",  
        "quoteAmount": "200",  
        "quoteAccountType": "FUND",  
        "orderLinkId": "lm-001",  
        "leverage": "2"  
    }  
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "",  
        "result": {  
            "orderId": "5e651d09-6169-4f72-a609-8622ff421d19",  
            "orderLinkId": "lm-001"  
        },  
        "retExtInfo": {},  
        "time": 1775123507299  
    }