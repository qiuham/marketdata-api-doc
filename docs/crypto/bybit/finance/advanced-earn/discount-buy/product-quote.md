---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/finance/advanced-earn/discount-buy/product-quote
api_type: REST
updated_at: 2026-07-18 18:54:48.169091
---

# Place Order

info

  * Requires Earn permission on the API key.
  * The order is processed asynchronously. A successful response means the order has been accepted, not settled. Use [Get Order Info](/docs/v5/finance/advanced-earn/double-win/order) to track the order status (`Pending` → `Success`).
  * `orderLinkId` is used for idempotency — resubmitting the same `orderLinkId` returns an error indicating the order already exists.
  * **Stake** : must pass `doubleWinStakeExtra`. For fixed range products, use the `leverage` from [Get Fixed Product Quote](/docs/v5/finance/advanced-earn/double-win/product-quote). For RFQ products, use the `leverage` from [Get Custom Product Quote](/docs/v5/finance/advanced-earn/double-win/leverage) and include `lowerPrice` / `upperPrice`. The order must be placed before the quote's `expireTime`.
  * **Redeem** : must call [Get Redeem Estimated Amount](/docs/v5/finance/advanced-earn/double-win/est-redeem) first to obtain `estRedeemAmount`, then pass it in `doubleWinRedeemExtra`.



### HTTP Request

POST`/v5/earn/advance/place-order`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
category| **true**|  string| Product category. `DoubleWin`  
productId| **true**|  string| Product ID  
orderType| **true**|  string| `Stake`: subscribe; `Redeem`: early redemption  
amount| false| string| Order amount. **Required** for `Stake`  
accountType| **true**|  string| Account type: `FUND` or `UNIFIED`. Not required for `Redeem`  
coin| **true**|  string| Coin name, e.g. `USDT`. Not required for `Redeem`  
orderLinkId| **true**|  string| User customised order ID (max 36 characters, alphanumeric and `_-`)  
doubleWinStakeExtra| false| Object| Required when `orderType=Stake`  
> leverage| **true**|  string| Leverage multiplier obtained from [Get Fixed Product Quote](/docs/v5/finance/advanced-earn/double-win/product-quote) or [Get Custom Product Quote](/docs/v5/finance/advanced-earn/double-win/leverage). Maximum 2 decimal places, must not exceed the quoted maximum  
> initialPrice| **true**|  string| Current index price of the underlying asset at order time. Recommend using `currentPrice` from [Get Fixed Product Quote](/docs/v5/finance/advanced-earn/double-win/product-quote)  
> lowerPrice| false| string| **RFQ only.** Custom lower bound of price range. Must match the value used in [Get Custom Product Quote](/docs/v5/finance/advanced-earn/double-win/leverage)  
> upperPrice| false| string| **RFQ only.** Custom upper bound of price range. Must match the value used in [Get Custom Product Quote](/docs/v5/finance/advanced-earn/double-win/leverage)  
doubleWinRedeemExtra| false| Object| Required when `orderType=Redeem`  
> positionId| **true**|  string| Position ID to redeem, obtained from [Get Position Info](/docs/v5/finance/advanced-earn/double-win/position)  
> estRedeemAmount| **true**|  string| Estimated redeem amount from [Get Redeem Estimated Amount](/docs/v5/finance/advanced-earn/double-win/est-redeem)  
> isSlippageProtected| false| bool| Whether to enable slippage protection. Default: `false`. If enabled, the order fails when the actual redeem amount deviates significantly from `estRedeemAmount`  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
orderId| string| System-generated order ID  
orderLinkId| string| User customised order ID  
  
* * *

### Request Example

**Stake (Fixed Range)**
    
    
     POST /v5/earn/advance/place-order HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1672211928338  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "category": "DoubleWin",  
        "productId": "14084",  
        "coin": "USDT",  
        "amount": "150",  
        "orderType": "Stake",  
        "accountType": "FUND",  
        "orderLinkId": "usdt-earn-009",  
        "doubleWinStakeExtra": {  
            "initialPrice": "66445.69",  
            "leverage": "9"  
        }  
    }  
    

**Stake (RFQ Custom Range)**
    
    
     POST /v5/earn/advance/place-order HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1672211928338  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "category": "DoubleWin",  
        "productId": "14084",  
        "coin": "USDT",  
        "amount": "150",  
        "orderType": "Stake",  
        "accountType": "FUND",  
        "orderLinkId": "usdt-earn-009",  
        "doubleWinStakeExtra": {  
            "initialPrice": "66445.69",  
            "leverage": "9"  
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
        "category": "DoubleWin",  
        "productId": "14092",  
        "coin": "USDT",  
        "amount": "200",  
        "orderType": "Stake",  
        "accountType": "FUND",  
        "orderLinkId": "usdt-earn-010",  
        "doubleWinStakeExtra": {  
            "initialPrice": "66333.94",  
            "lowerPrice": "63000",  
            "upperPrice": "70000",  
            "leverage": "245.18"  
        }  
    }  
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "",  
        "result": {  
            "orderId": "05184c23-8a98-456c-a2af-0ef1c45116cc",  
            "orderLinkId": "usdt-earn-009"  
        },  
        "retExtInfo": {},  
        "time": 1775107011430  
    }

---

# 創建訂單

信息

  * API 金鑰需要具備 Earn（理財）權限。
  * 訂單採非同步處理。響應成功僅代表訂單已被接受，而非已結算。請使用[查詢訂單資訊](/docs/zh-TW/v5/finance/advanced-earn/double-win/order)來追蹤訂單狀態（`Pending` → `Success`）。
  * `orderLinkId` 用於保證冪等性——重複提交相同的 `orderLinkId` 時，系統將返回訂單已存在的錯誤。
  * **申購（Stake）** ：必須傳入 `doubleWinStakeExtra`。固定區間產品請使用[查詢固定產品報價](/docs/zh-TW/v5/finance/advanced-earn/double-win/product-quote)中的 `leverage`；RFQ 產品請使用[查詢自選區間產品報價](/docs/zh-TW/v5/finance/advanced-earn/double-win/leverage)中的 `leverage`，並傳入 `lowerPrice` 和 `upperPrice`。須在報價的 `expireTime` 前完成下單。
  * **贖回（Redeem）** ：必須先調用[查詢贖回預估金額](/docs/zh-TW/v5/finance/advanced-earn/double-win/est-redeem)獲取 `estRedeemAmount`，再透過 `doubleWinRedeemExtra` 傳入。



### HTTP 請求

POST`/v5/earn/advance/place-order`

### 請求參數

參數| 必填| 類型| 說明  
---|---|---|---  
category| **true**|  string| 產品類別，`DoubleWin`  
productId| **true**|  string| 產品 ID  
orderType| **true**|  string| 訂單類型：`Stake`（申購），`Redeem`（提前贖回）  
amount| false| string| 訂單金額。`Stake` 訂單必填  
accountType| **true**|  string| 帳戶類型：`FUND`（資金帳戶），`UNIFIED`（統一帳戶）。`Redeem` 訂單無需填寫  
coin| **true**|  string| 幣種名稱，例如：`USDT`。`Redeem` 訂單無需填寫  
orderLinkId| **true**|  string| 用戶自定義訂單 ID（最多 36 個字元，支援英數字及 `_-`）  
doubleWinStakeExtra| false| Object| `orderType=Stake` 時必填  
> leverage| **true**|  string| 槓桿倍數，從[查詢固定產品報價](/docs/zh-TW/v5/finance/advanced-earn/double-win/product-quote)或[查詢自選區間產品報價](/docs/zh-TW/v5/finance/advanced-earn/double-win/leverage)獲取。最多 2 位小數，不可超過報價返回的最大值  
> initialPrice| **true**|  string| 下單時的標的資產指數價格。建議使用[查詢固定產品報價](/docs/zh-TW/v5/finance/advanced-earn/double-win/product-quote)返回的 `currentPrice`  
> lowerPrice| false| string| **僅 RFQ 產品需填寫。** 自選價格區間下限，須與[查詢自選區間產品報價](/docs/zh-TW/v5/finance/advanced-earn/double-win/leverage)中使用的值一致  
> upperPrice| false| string| **僅 RFQ 產品需填寫。** 自選價格區間上限，須與[查詢自選區間產品報價](/docs/zh-TW/v5/finance/advanced-earn/double-win/leverage)中使用的值一致  
doubleWinRedeemExtra| false| Object| `orderType=Redeem` 時必填  
> positionId| **true**|  string| 要贖回的倉位 ID，從[查詢倉位資訊](/docs/zh-TW/v5/finance/advanced-earn/double-win/position)獲取  
> estRedeemAmount| **true**|  string| 預估贖回金額，從[查詢贖回預估金額](/docs/zh-TW/v5/finance/advanced-earn/double-win/est-redeem)獲取  
> isSlippageProtected| false| bool| 是否啟用贖回滑點保護。預設值：`false`。啟用後，當實際贖回金額與 `estRedeemAmount` 偏差過大時，贖回訂單將失敗  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
orderId| string| 系統生成的訂單 ID  
orderLinkId| string| 用戶自定義訂單 ID  
  
* * *

### 請求示例

**申購（固定區間）**
    
    
     POST /v5/earn/advance/place-order HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1672211928338  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "category": "DoubleWin",  
        "productId": "14084",  
        "coin": "USDT",  
        "amount": "150",  
        "orderType": "Stake",  
        "accountType": "FUND",  
        "orderLinkId": "usdt-earn-009",  
        "doubleWinStakeExtra": {  
            "initialPrice": "66445.69",  
            "leverage": "9"  
        }  
    }  
    

**申購（RFQ 自選區間）**
    
    
     POST /v5/earn/advance/place-order HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1672211928338  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "category": "DoubleWin",  
        "productId": "14092",  
        "coin": "USDT",  
        "amount": "200",  
        "orderType": "Stake",  
        "accountType": "FUND",  
        "orderLinkId": "usdt-earn-010",  
        "doubleWinStakeExtra": {  
            "initialPrice": "66333.94",  
            "lowerPrice": "63000",  
            "upperPrice": "70000",  
            "leverage": "245.18"  
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
        "category": "DoubleWin",  
        "productId": "14084",  
        "orderType": "Redeem",  
        "orderLinkId": "usdt-redeem-001",  
        "doubleWinRedeemExtra": {  
            "positionId": "2848",  
            "estRedeemAmount": "148.50",  
            "isSlippageProtected": true  
        }  
    }  
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "",  
        "result": {  
            "orderId": "05184c23-8a98-456c-a2af-0ef1c45116cc",  
            "orderLinkId": "usdt-earn-009"  
        },  
        "retExtInfo": {},  
        "time": 1775107011430  
    }