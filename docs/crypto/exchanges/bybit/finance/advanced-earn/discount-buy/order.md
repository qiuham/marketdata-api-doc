---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/finance/advanced-earn/discount-buy/order
api_type: REST
updated_at: 2026-05-27 19:16:35.321826
---

# Get Order Info

info

  * Requires Earn permission on the API key.



### HTTP Request

GET`/v5/earn/advance/order`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
category| **true**|  string| Product category. `DiscountBuy`  
orderId| false| string| Filter by order ID  
orderLinkId| false| string| Filter by user customised order ID  
productId| false| string| Filter by product ID  
startTime| false| int| Start time (order creation time), Unix timestamp in ms  
endTime| false| int| End time, Unix timestamp in ms  
limit| false| int| Number of items per page  
cursor| false| string| Pagination cursor. Use `nextPageCursor` from previous response  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
nextPageCursor| string| Next page cursor. Empty string if no more data  
list| array| Object  
> orderId| string| Order ID  
> orderLinkId| string| User customised order ID  
> productId| string| Product ID  
> category| string| Product category. `DiscountBuy`  
> orderType| string| Fixed value: `Stake`  
> amount| string| Investment amount  
> coin| string| Investment coin, e.g. `USDT`  
> underlyingAsset| string| Underlying asset, e.g. `BTC`, `ETH`  
> status| string| Order status: `Pending` (processing); `Success` (order accepted, position created); `Settled` (product settled — knocked out or exercised); `Fail` (order failed)  
> createdTime| string| Order creation time, Unix timestamp in ms  
> purchasePrice| string| Anchor buy price  
> knockoutPrice| string| Knockout price  
> knockoutCouponE8| string| Annualized interest rate in e8 precision. Actual rate = `knockoutCouponE8` / 1e8  
> duration| string| Product duration, e.g. `7d`  
> settlementTime| string| Settlement time, Unix timestamp in ms  
> accountType| string| Deduction account: `FUND` or `UNIFIED`  
> toAccountType| string| Settlement credit account. `FUND` when `status=Settled`; deduction account when `status=Fail`  
> settleType| string| Settlement preference when exercised: `Base` = receive underlying asset; `Quote` = receive USDT. Has no effect upon knockout  
> settlementPrice| string| Settlement price (30-min TWAP before `settlementTime`). Only available when `status=Settled`  
> settlementCoin| string| Settlement coin. Only available when `status=Settled`  
> settlementAmount| string| Settlement amount. Only available when `status=Settled`. See calculation rules below  
> isVip| bool| Whether this is a VIP product order  
> refundStatus| string| Refund status. Only valid when `status=Fail`: `REFUNDING` (refund in progress), `REFUND_DONE` (refund completed). Empty string for other statuses  
  
### Request Example
    
    
    GET /v5/earn/advance/order?category=DiscountBuy&orderLinkId=my-order-001 HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1713600000000  
    X-BAPI-RECV-WINDOW: 5000  
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "",  
        "result": {  
            "category": "",  
            "list": [  
                {  
                    "orderId": "38f6f5ce-57e2-4d69-b4d3-c39464389ccb",  
                    "orderLinkId": "my-order-001",  
                    "productId": "7037",  
                    "category": "DiscountBuy",  
                    "orderType": "Stake",  
                    "amount": "200",  
                    "coin": "USDT",  
                    "underlyingAsset": "BTC",  
                    "status": "Success",  
                    "createdTime": "1776154116000",  
                    "purchasePrice": "74019",  
                    "knockoutPrice": "76050",  
                    "knockoutCouponE8": "1000000",  
                    "duration": "1d",  
                    "settlementTime": "1776240000000",  
                    "accountType": "FUND",  
                    "toAccountType": "",  
                    "settlementPrice": "",  
                    "settlementCoin": "",  
                    "settlementAmount": "",  
                    "settleType": "Base",  
                    "isVip": false,  
                    "refundStatus": ""  
                }  
            ],  
            "nextPageCursor": ""  
        },  
        "retExtInfo": {},  
        "time": 1776154473104  
    }

---

# 查詢訂單資訊

信息

  * API 金鑰需要具備 Earn（理財）權限。



### HTTP 請求

GET`/v5/earn/advance/order`

### 請求參數

參數| 必填| 類型| 說明  
---|---|---|---  
category| **true**|  string| 產品類別，`DiscountBuy`  
orderId| false| string| 按訂單 ID 篩選  
orderLinkId| false| string| 按用戶自定義訂單 ID 篩選  
productId| false| string| 按產品 ID 篩選  
startTime| false| int| 開始時間（訂單創建時間），毫秒級 Unix 時間戳  
endTime| false| int| 結束時間，毫秒級 Unix 時間戳  
limit| false| int| 每頁返回數量  
cursor| false| string| 分頁游標，使用上次響應中的 `nextPageCursor`  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
nextPageCursor| string| 下一頁游標，為空字串表示無更多資料  
list| array| 列表  
> orderId| string| 訂單 ID  
> orderLinkId| string| 用戶自定義訂單 ID  
> productId| string| 產品 ID  
> category| string| 產品類別，`DiscountBuy`  
> orderType| string| 固定值：`Stake`  
> amount| string| 投資金額  
> coin| string| 投資幣種，例如：`USDT`  
> underlyingAsset| string| 標的資產，例如：`BTC`, `ETH`  
> status| string| 訂單狀態：`Pending`（處理中），`Success`（訂單成功，已創建倉位），`Settled`（產品已結算，敲出或行權），`Fail`（訂單失敗）  
> createdTime| string| 創建時間，毫秒級 Unix 時間戳  
> purchasePrice| string| 錨定買入價  
> knockoutPrice| string| 敲出價  
> knockoutCouponE8| string| 年化息率（e8 精度），實際利率 = `knockoutCouponE8` / 1e8  
> duration| string| 產品期限，例如：`7d`  
> settlementTime| string| 結算時間，毫秒級 Unix 時間戳  
> accountType| string| 扣款帳戶：`FUND`（資金帳戶），`UNIFIED`（統一帳戶）  
> toAccountType| string| 結算入帳帳戶。`status=Settled` 時固定為 `FUND`；`status=Fail` 時為扣款帳戶  
> settleType| string| 行權結算方式：`Base` = 收取標的資產；`Quote` = 收取 USDT。敲出時此參數無效  
> settlementPrice| string| 結算價（`settlementTime` 前 30 分鐘 TWAP），僅 `status=Settled` 時有值  
> settlementCoin| string| 結算幣種，僅 `status=Settled` 時有值  
> settlementAmount| string| 結算金額，僅 `status=Settled` 時有值，計算規則見下表  
> isVip| bool| 是否為 VIP 產品訂單  
> refundStatus| string| 退款狀態，僅 `status=Fail` 時有效：`REFUNDING`（退款處理中），`REFUND_DONE`（退款完成）。其他狀態為空字串  
  
#### 結算金額計算規則

結算結果| 條件| `settlementCoin`| `settlementAmount`  
---|---|---|---  
敲出| `settlementPrice` >= `knockoutPrice`| `USDT`| `amount × (1 + knockoutCouponE8/1e8 × 期限天數/365)`  
行權（Base）| `settlementPrice` < `knockoutPrice` 且 `settleType=Base`| 標的資產| `amount / purchasePrice`  
行權（Quote）| `settlementPrice` < `knockoutPrice` 且 `settleType=Quote`| `USDT`| `amount / purchasePrice × settlementPrice`  
  
### 請求示例
    
    
    GET /v5/earn/advance/order?category=DiscountBuy&orderLinkId=my-order-001 HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1776154473104  
    X-BAPI-RECV-WINDOW: 5000  
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "",  
        "result": {  
            "category": "",  
            "list": [  
                {  
                    "orderId": "38f6f5ce-57e2-4d69-b4d3-c39464389ccb",  
                    "orderLinkId": "my-order-001",  
                    "productId": "7037",  
                    "category": "DiscountBuy",  
                    "orderType": "Stake",  
                    "amount": "200",  
                    "coin": "USDT",  
                    "underlyingAsset": "BTC",  
                    "status": "Success",  
                    "createdTime": "1776154116000",  
                    "purchasePrice": "74019",  
                    "knockoutPrice": "76050",  
                    "knockoutCouponE8": "1000000",  
                    "duration": "1d",  
                    "settlementTime": "1776240000000",  
                    "accountType": "FUND",  
                    "toAccountType": "",  
                    "settlementPrice": "",  
                    "settlementCoin": "",  
                    "settlementAmount": "",  
                    "settleType": "Base",  
                    "isVip": false,  
                    "refundStatus": ""  
                }  
            ],  
            "nextPageCursor": ""  
        },  
        "retExtInfo": {},  
        "time": 1776154473104  
    }