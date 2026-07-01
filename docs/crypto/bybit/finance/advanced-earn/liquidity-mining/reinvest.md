---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/finance/advanced-earn/liquidity-mining/reinvest
api_type: REST
updated_at: 2026-07-01 19:28:16.447329
---

# Place Order

info

  * Need authentication. **Up to 5 requests** per second.
  * Requires Earn permission on the API key.
  * The order is processed asynchronously. A successful response means the order has been accepted, not settled. Use [Get Order Info](/docs/v5/finance/advanced-earn/smart-lvg/order) to track the order status (Pending → Success).
  * `orderLinkId` is used for idempotency — resubmitting the same `orderLinkId` returns an error indicating the order already exists.
  * **Stake** : must pass `smartLeverageStakeExtra` with `initialPrice` and `breakevenPrice`. Stake slippage protection is enforced: order fails if actual price deviates more than ±5% from `initialPrice` (error code 180030).
  * **Redeem** : must call [Get Redeem Estimated Amount](/docs/v5/finance/advanced-earn/smart-lvg/est-redeem) first to obtain `estRedeemAmount`. The result is cached for 10 minutes and validated server-side when placing the redeem order.



### HTTP Request

POST`/v5/earn/advance/place-order`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
category| **true**|  string| Product type. `SmartLeverage`  
productId| **true**|  string| Product ID  
orderType| **true**|  string| Order type: `Stake` (subscribe), `Redeem` (early redemption)  
amount| false| string| Order amount. **Required** for `Stake`  
accountType| **true**|  string| Account type: `FUND`, `UNIFIED`  
coin| **true**|  string| Coin name. Not required for `Redeem` orders  
orderLinkId| **true**|  string| User customised order ID (max 36 characters)  
smartLeverageStakeExtra| false| Object| Required when `orderType=Stake`  
> initialPrice| **true**|  string| Underlying asset price at order time, used for slippage protection (±5%). Recommend using `currentPrice` from [Get Product Quote](/docs/v5/finance/advanced-earn/smart-lvg/product-quote)  
> breakevenPrice| **true**|  string| Breakeven price selected by user. Obtain from [Get Product Quote](/docs/v5/finance/advanced-earn/smart-lvg/product-quote)  
smartLeverageRedeemExtra| false| Object| Required when `orderType=Redeem`  
> positionId| **true**|  string| Position ID to redeem  
> estRedeemAmount| **true**|  string| Estimated redeem amount, obtained from the Get Redeem Estimated Amount API. Cached for 10 minutes server-side  
> isSlippageProtected| false| bool| Whether to enable slippage protection for redemption. Default: `false`. If enabled, the redeem order fails when the actual redeem amount deviates significantly from `estRedeemAmount`  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
orderId| string| System-generated order ID  
orderLinkId| string| User customised order ID  
  
* * *

### Request Example

**Stake**
    
    
     POST /v5/earn/advance/place-order HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1672211928338  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "category": "SmartLeverage",  
        "productId": "12999",  
        "coin": "USDT",  
        "orderType": "Stake",  
        "amount": "100",  
        "accountType": "FUND",  
        "orderLinkId": "usdt-earn-007",  
        "smartLeverageStakeExtra": {  
            "initialPrice": "68403",  
            "breakevenPrice": "68650"  
        }  
    }  
    

**Redeem**
    
    
     POST /v5/earn/advance/place-order HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1672211928338  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "category": "SmartLeverage",  
        "productId": "12999",  
        "orderType": "Redeem",  
        "accountType": "FUND",  
        "orderLinkId": "usdt-earn-008",  
        "smartLeverageRedeemExtra": {  
            "positionId": "1277",  
            "estRedeemAmount": "77.8469",  
            "isSlippageProtected": true  
        }  
    }  
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "",  
        "result": {  
            "orderId": "97f198e9-b14b-4703-b4a6-a4aa06ba1499",  
            "orderLinkId": "usdt-earn-004"  
        },  
        "retExtInfo": {},  
        "time": 1773815412459  
    }

---

# 創建訂單

信息

  * 需要身份驗證。每秒**最多 5 次請求** 。
  * API 金鑰需要具備 Earn（理財）權限。
  * 訂單採非同步處理。響應成功僅代表訂單已被接受，而非已結算。請使用[查詢訂單資訊](/docs/zh-TW/v5/finance/advanced-earn/smart-lvg/order)來追蹤訂單狀態（Pending → Success）。
  * `orderLinkId` 用於保證冪等性——重複提交相同的 `orderLinkId` 時，系統將返回訂單已存在的錯誤。
  * **申購（Stake）** ：必須傳入 `smartLeverageStakeExtra`，包含 `initialPrice` 和 `breakevenPrice`。系統將強制執行申購滑點保護：若實際價格與 `initialPrice` 偏差超過 ±5%，訂單將失敗（錯誤代碼 180030）。
  * **贖回（Redeem）** ：必須先通過[查詢贖回預估金額](/docs/zh-TW/v5/finance/advanced-earn/smart-lvg/est-redeem)獲取 `estRedeemAmount`。結果在服務端快取 10 分鐘，並在提交贖回訂單時進行驗證。



### HTTP 請求

POST`/v5/earn/advance/place-order`

### 請求參數

參數| 必填| 類型| 說明  
---|---|---|---  
category| **true**|  string| 產品類型，`SmartLeverage`  
productId| **true**|  string| 產品 ID  
orderType| **true**|  string| 訂單類型：`Stake`（申購），`Redeem`（提前贖回）  
amount| false| string| 訂單金額。`Stake` 訂單必填  
accountType| **true**|  string| 帳戶類型：`FUND`（資金帳戶），`UNIFIED`（統一帳戶）  
coin| **true**|  string| 幣種名稱。`Redeem` 訂單無需填寫  
orderLinkId| **true**|  string| 用戶自定義訂單 ID（最多 36 個字元）  
smartLeverageStakeExtra| false| Object| `orderType=Stake` 時必填  
> initialPrice| **true**|  string| 下單時的標的資產價格，用於滑點保護（±5%）。建議使用[查詢產品報價](/docs/zh-TW/v5/finance/advanced-earn/smart-lvg/product-quote)中的 `currentPrice`  
> breakevenPrice| **true**|  string| 用戶選擇的損益平衡價格。從[查詢產品報價](/docs/zh-TW/v5/finance/advanced-earn/smart-lvg/product-quote)獲取  
smartLeverageRedeemExtra| false| Object| `orderType=Redeem` 時必填  
> positionId| **true**|  string| 要贖回的倉位 ID  
> estRedeemAmount| **true**|  string| 預估贖回金額，從查詢贖回預估金額 API 獲取。服務端快取 10 分鐘  
> isSlippageProtected| false| bool| 是否啟用贖回滑點保護。預設值：`false`。啟用後，當實際贖回金額與 `estRedeemAmount` 偏差過大時，贖回訂單將失敗  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
orderId| string| 系統生成的訂單 ID  
orderLinkId| string| 用戶自定義訂單 ID  
  
* * *

### 請求示例

**申購（Stake）**
    
    
     POST /v5/earn/advance/place-order HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1672211928338  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "category": "SmartLeverage",  
        "productId": "12999",  
        "coin": "USDT",  
        "orderType": "Stake",  
        "amount": "100",  
        "accountType": "FUND",  
        "orderLinkId": "usdt-earn-007",  
        "smartLeverageStakeExtra": {  
            "initialPrice": "68403",  
            "breakevenPrice": "68650"  
        }  
    }  
    

**贖回（Redeem）**
    
    
     POST /v5/earn/advance/place-order HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1672211928338  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "category": "SmartLeverage",  
        "productId": "12999",  
        "orderType": "Redeem",  
        "accountType": "FUND",  
        "orderLinkId": "usdt-earn-008",  
        "smartLeverageRedeemExtra": {  
            "positionId": "1277",  
            "estRedeemAmount": "77.8469",  
            "isSlippageProtected": true  
        }  
    }  
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "",  
        "result": {  
            "orderId": "97f198e9-b14b-4703-b4a6-a4aa06ba1499",  
            "orderLinkId": "usdt-earn-004"  
        },  
        "retExtInfo": {},  
        "time": 1773815412459  
    }