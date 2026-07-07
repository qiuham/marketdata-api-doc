---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/finance/earn/byusdt/hourly-yield
api_type: REST
updated_at: 2026-07-07 19:12:27.637650
---

# Place Order

info

  * Orders are processed asynchronously. A successful response means the order was accepted, not that it has been settled. Use [Get Order List](/docs/v5/finance/earn/byusdt/order) to track order status.
  * `orderLinkId` is used for idempotency — resubmitting the same `orderLinkId` returns an error indicating the order already exists.
  * **Mint** : Transfers USDT from your Flexible Saving account to mint byUSDT.
  * **Redeem** : Burns byUSDT and returns USDT to your Unified Trading Account (UTA).



### HTTP Request

POST`/v5/earn/token/place-order`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
coin| **true**|  string| Token coin. Currently only `BYUSDT` is supported  
orderLinkId| **true**|  string| User-customised order ID (max 36 characters). Used for idempotency and order lookup  
orderType| **true**|  string| Order type: `Mint` (USDT → byUSDT), `Redeem` (byUSDT → USDT)  
amount| **true**|  string| Order amount (decimal string). For `Mint`: USDT quantity; for `Redeem`: byUSDT quantity  
accountType| **true**|  string| Account type. For `Mint`: must be `FlexibleSaving`; for `Redeem`: must be `UNIFIED`  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
orderId| string| System-generated order ID (UUID)  
orderLinkId| string| User-customised order ID  
  
* * *

### Request Example
    
    
    POST /v5/earn/token/place-order HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1741651200000  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "coin": "BYUSDT",  
        "orderLinkId": "my-order-001",  
        "orderType": "Mint",  
        "amount": "100.00",  
        "accountType": "FlexibleSaving"  
    }  
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "success",  
        "result": {  
            "orderId": "550e8400-e29b-41d4-a716-446655440000",  
            "orderLinkId": "my-order-001"  
        },  
        "retExtInfo": {},  
        "time": 1741651200000  
    }

---

# 下單

信息

  * 訂單為非同步處理。成功響應表示訂單已被接受，而非已完成結算。請使用[查詢訂單列表](/docs/zh-TW/v5/finance/earn/byusdt/order)追蹤訂單狀態。
  * `orderLinkId` 用於保證冪等性——重複提交相同的 `orderLinkId` 時，系統將返回訂單已存在的錯誤。
  * **Mint（鑄造）** ：將 USDT 從活期理財帳戶轉入，鑄造 byUSDT。
  * **Redeem（贖回）** ：銷毀 byUSDT，將 USDT 返還至統一交易帳戶（UTA）。



### HTTP 請求

POST`/v5/earn/token/place-order`

### 請求參數

參數| 必填| 類型| 說明  
---|---|---|---  
coin| **true**|  string| 代幣幣種。目前僅支援 `BYUSDT`  
orderLinkId| **true**|  string| 用戶自定義訂單 ID（最多 36 個字元），用於冪等性控制及訂單查詢  
orderType| **true**|  string| 訂單類型：`Mint`（USDT → byUSDT）、`Redeem`（byUSDT → USDT）  
amount| **true**|  string| 訂單金額（十進位字串）。`Mint` 時為 USDT 數量；`Redeem` 時為 byUSDT 數量  
accountType| **true**|  string| 帳戶類型。`Mint` 時必須為 `FlexibleSaving`；`Redeem` 時必須為 `UNIFIED`  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
orderId| string| 系統生成的訂單 ID（UUID）  
orderLinkId| string| 用戶自定義訂單 ID  
  
* * *

### 請求示例
    
    
    POST /v5/earn/token/place-order HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1741651200000  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "coin": "BYUSDT",  
        "orderLinkId": "my-order-001",  
        "orderType": "Mint",  
        "amount": "100.00",  
        "accountType": "FlexibleSaving"  
    }  
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "success",  
        "result": {  
            "orderId": "550e8400-e29b-41d4-a716-446655440000",  
            "orderLinkId": "my-order-001"  
        },  
        "retExtInfo": {},  
        "time": 1741651200000  
    }