---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/finance/rwa/place-order
api_type: REST
updated_at: 2026-11-13 19:23:38.516887
---

# Place Order

info

  * Orders are processed asynchronously. A successful response means the order was accepted, not settled. Use [Get Order List](/docs/v5/finance/rwa/order) to track order status.
  * `orderLinkId` is **required** and must be unique per UID within RWA business scope. Reusing a previous `orderLinkId` returns error `180025 ORDER_ALREADY_EXISTS`.
  * **Stake** : deducts settlement coin from `accountType` and allocates shares at next NAV.
  * **Redeem** : locks shares and refunds settlement coin to `accountType` after settlement (T+N).
  * **Rate Limit:** 5 req/s (UID)



### HTTP Request

POST`/v5/earn/rwa/place-order`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
productId| **true**|  integer| Product ID  
orderType| **true**|  string| Order type: `Stake` (subscription), `Redeem` (redemption)  
coin| **true**|  string| Settlement coin (uppercase), e.g. `USDC`  
orderLinkId| **true**|  string| User-defined idempotency key. Max 36 characters, allowed charset `[a-zA-Z0-9-_]`. Must be unique per UID within RWA scope  
stakeAmount| false| string| Stake amount in settlement coin (decimal string). **Required when`orderType=Stake`**, ignored otherwise  
redeemShares| false| string| Redeem share quantity (decimal string). **Required when`orderType=Redeem`**, ignored otherwise  
accountType| false| string| Source/destination account: `FUND`, `UNIFIED`. Default: `FUND`  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
orderId| string| System-generated order ID (UUID)  
orderLinkId| string| User-defined order ID (echoed back)  
  
* * *

### Request Example
    
    
    POST /v5/earn/rwa/place-order HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1710691200000  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "productId": 1001,  
        "orderType": "Stake",  
        "coin": "USDC",  
        "stakeAmount": "100",  
        "accountType": "FUND",  
        "orderLinkId": "my-stake-001"  
    }  
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "success",  
        "result": {  
            "orderId": "550e8400-e29b-41d4-a716-446655440000",  
            "orderLinkId": "my-stake-001"  
        },  
        "retExtInfo": {},  
        "time": 1710691200000  
    }

---

# 下單（認購/贖回）

信息

  * 訂單為異步處理。成功響應僅表示訂單已被接受，並非已完成結算。請使用 [獲取訂單列表](/docs/zh-TW/v5/finance/rwa/order) 追蹤訂單狀態。
  * `orderLinkId` **必填** ，且在 RWA 業務範圍內每個 UID 必須唯一。重複使用已存在的 `orderLinkId` 將返回錯誤 `180025 ORDER_ALREADY_EXISTS`。
  * **認購（Stake）** ：從 `accountType` 扣除結算幣種，按下一個 NAV 分配份額。
  * **贖回（Redeem）** ：鎖定份額，T+N 結算後將結算幣種退回至 `accountType`。
  * **頻率限制：** 5 次/秒（UID）



### HTTP 請求

POST`/v5/earn/rwa/place-order`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
productId| **true**|  integer| 產品 ID  
orderType| **true**|  string| 訂單類型：`Stake`（認購）、`Redeem`（贖回）  
coin| **true**|  string| 結算幣種（大寫），如 `USDC`  
orderLinkId| **true**|  string| 用戶自定義冪等鍵。最長 36 位，允許字符集 `[a-zA-Z0-9-_]`，在 RWA 業務範圍內每個 UID 必須唯一  
stakeAmount| false| string| 認購金額（結算幣種，十進制字符串）。**`orderType=Stake` 時必填**，否則忽略  
redeemShares| false| string| 贖回份額（十進制字符串）。**`orderType=Redeem` 時必填**，否則忽略  
accountType| false| string| 資金來源/目標賬戶：`FUND`、`UNIFIED`。默認：`FUND`  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
orderId| string| 系統生成的訂單 ID（UUID）  
orderLinkId| string| 用戶自定義訂單 ID（原樣返回）  
  
* * *

### 請求示例
    
    
    POST /v5/earn/rwa/place-order HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1710691200000  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "productId": 1001,  
        "orderType": "Stake",  
        "coin": "USDC",  
        "stakeAmount": "100",  
        "accountType": "FUND",  
        "orderLinkId": "my-stake-001"  
    }  
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "success",  
        "result": {  
            "orderId": "550e8400-e29b-41d4-a716-446655440000",  
            "orderLinkId": "my-stake-001"  
        },  
        "retExtInfo": {},  
        "time": 1710691200000  
    }