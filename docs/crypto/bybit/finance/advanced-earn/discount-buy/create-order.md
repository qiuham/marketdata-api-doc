---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/finance/advanced-earn/discount-buy/create-order
api_type: REST
updated_at: 2026-07-04 19:05:28.917182
---

# Place Order

info

  * Requires Earn permission on the API key.
  * The order is processed asynchronously. A successful response means the order has been accepted, not settled. Use [Get Order Info](/docs/v5/finance/advanced-earn/discount-buy/order) to track the order status.
  * `orderLinkId` is used for idempotency — resubmitting the same `orderLinkId` returns an error indicating the order already exists.
  * You must call [Get Product Quote](/docs/v5/finance/advanced-earn/discount-buy/product-quote) first and pass the returned quote values in `discountBuyExtra`.
  * **Only`DiscountBuy` products are supported.** Ultra Discount Buy and Interest Card products are not supported by this API.



### HTTP Request

POST`/v5/earn/advance/place-order`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
category| **true**|  string| Product category. `DiscountBuy`  
productId| **true**|  string| Product ID  
orderType| **true**|  string| Fixed value: `Stake`  
amount| **true**|  string| Investment amount in USDT. Precision is determined by `orderPrecisionDigital` from [Get Product Info](/docs/v5/finance/advanced-earn/discount-buy/product-info)  
coin| **true**|  string| Investment coin. `USDT`  
accountType| **true**|  string| Deduction account: `FUND` or `UNIFIED` (requires Unified Trading Account to be enabled)  
orderLinkId| **true**|  string| User customised order ID. Max 40 characters, alphanumeric and `_-` only  
discountBuyExtra| **true**|  Object| Discount Buy pricing parameters  
> initialPrice| **true**|  string| Current index price of the underlying asset at order time. Use `currentPrice` from [Get Product Quote](/docs/v5/finance/advanced-earn/discount-buy/product-quote). Max 8 decimal places  
> purchasePrice| **true**|  string| Anchor buy price from [Get Product Quote](/docs/v5/finance/advanced-earn/discount-buy/product-quote). Max 8 decimal places  
> knockoutPrice| **true**|  string| Knockout price from [Get Product Quote](/docs/v5/finance/advanced-earn/discount-buy/product-quote). Max 8 decimal places  
> knockoutCouponE8| **true**|  string| Annualized interest rate in e8 precision from [Get Product Quote](/docs/v5/finance/advanced-earn/discount-buy/product-quote)  
> settleType| **true**|  string| Settlement preference when exercised: `Base` = receive underlying asset (quantity = amount / purchasePrice); `Quote` = receive USDT (amount = amount / purchasePrice × settlementPrice). Has no effect upon knockout — USDT principal + interest is always returned  
> instUid| **true**|  string| Market maker institution ID from [Get Product Quote](/docs/v5/finance/advanced-earn/discount-buy/product-quote)  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
orderId| string| System-generated order ID  
orderLinkId| string| User customised order ID echoed back  
  
### Request Example
    
    
    POST /v5/earn/advance/place-order HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1713600000000  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "category": "DiscountBuy",  
        "productId": "7037",  
        "orderType": "Stake",  
        "amount": "200",  
        "coin": "USDT",  
        "accountType": "FUND",  
        "orderLinkId": "my-order-001",  
        "discountBuyExtra": {  
            "initialPrice": "74571.32",  
            "purchasePrice": "74019",  
            "knockoutPrice": "76050",  
            "knockoutCouponE8": "1000000",  
            "settleType": "Base",  
            "instUid": "100307526"  
        }  
    }  
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "",  
        "result": {  
            "orderId": "38f6f5ce-57e2-4d69-b4d3-c39464389ccb",  
            "orderLinkId": "my-order-001"  
        },  
        "retExtInfo": {},  
        "time": 1776154116919  
    }

---

# 創建訂單

信息

  * API 金鑰需要具備 Earn（理財）權限。
  * 訂單採非同步處理。響應成功僅代表訂單已被接受，而非已結算。請使用[查詢訂單資訊](/docs/zh-TW/v5/finance/advanced-earn/discount-buy/order)追蹤訂單狀態。
  * `orderLinkId` 用於保證冪等性——重複提交相同的 `orderLinkId` 時，系統將返回訂單已存在的錯誤。
  * 下單前必須先呼叫[查詢產品報價](/docs/zh-TW/v5/finance/advanced-earn/discount-buy/product-quote)，並將返回的報價參數傳入 `discountBuyExtra`。
  * **僅支援普通`DiscountBuy` 產品。** 超級折扣購（Ultra Discount Buy）及利息卡（Interest Card）產品不支援此 API。



### HTTP 請求

POST`/v5/earn/advance/place-order`

### 請求參數

參數| 必填| 類型| 說明  
---|---|---|---  
category| **true**|  string| 產品類別，`DiscountBuy`  
productId| **true**|  string| 產品 ID  
orderType| **true**|  string| 固定值：`Stake`  
amount| **true**|  string| 投資金額（USDT），精度由[查詢產品資訊](/docs/zh-TW/v5/finance/advanced-earn/discount-buy/product-info)中的 `orderPrecisionDigital` 決定  
coin| **true**|  string| 投資幣種，`USDT`  
accountType| **true**|  string| 扣款帳戶：`FUND`（資金帳戶）或 `UNIFIED`（統一交易帳戶）  
orderLinkId| **true**|  string| 用戶自定義訂單 ID。最多 40 個字元，僅支援字母、數字及 `_-`  
discountBuyExtra| **true**|  Object| 折扣購報價參數  
> initialPrice| **true**|  string| 下單時標的資產的當前市場價格，建議使用[查詢產品報價](/docs/zh-TW/v5/finance/advanced-earn/discount-buy/product-quote)中的 `currentPrice`，最多 8 位小數  
> purchasePrice| **true**|  string| 來自[查詢產品報價](/docs/zh-TW/v5/finance/advanced-earn/discount-buy/product-quote)的錨定買入價，最多 8 位小數  
> knockoutPrice| **true**|  string| 來自[查詢產品報價](/docs/zh-TW/v5/finance/advanced-earn/discount-buy/product-quote)的敲出價，最多 8 位小數  
> knockoutCouponE8| **true**|  string| 來自[查詢產品報價](/docs/zh-TW/v5/finance/advanced-earn/discount-buy/product-quote)的年化息率（e8 精度）  
> settleType| **true**|  string| 行權結算方式：`Base` = 收取標的資產（數量 = amount / purchasePrice）；`Quote` = 收取 USDT（金額 = amount / purchasePrice × settlementPrice）。敲出時此參數無效，無論傳何值均返還 USDT 本金 + 利息  
> instUid| **true**|  string| 來自[查詢產品報價](/docs/zh-TW/v5/finance/advanced-earn/discount-buy/product-quote)的做市商機構 ID  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
orderId| string| 系統生成的訂單 ID  
orderLinkId| string| 用戶自定義訂單 ID（原樣返回）  
  
### 請求示例
    
    
    POST /v5/earn/advance/place-order HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1776154116919  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "category": "DiscountBuy",  
        "productId": "7037",  
        "orderType": "Stake",  
        "amount": "200",  
        "coin": "USDT",  
        "accountType": "FUND",  
        "orderLinkId": "my-order-001",  
        "discountBuyExtra": {  
            "initialPrice": "74571.32",  
            "purchasePrice": "74019",  
            "knockoutPrice": "76050",  
            "knockoutCouponE8": "1000000",  
            "settleType": "Base",  
            "instUid": "100307526"  
        }  
    }  
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "",  
        "result": {  
            "orderId": "38f6f5ce-57e2-4d69-b4d3-c39464389ccb",  
            "orderLinkId": "my-order-001"  
        },  
        "retExtInfo": {},  
        "time": 1776154116919  
    }