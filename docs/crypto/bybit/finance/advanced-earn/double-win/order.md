---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/finance/advanced-earn/double-win/order
api_type: REST
updated_at: 2026-11-13 19:22:46.049875
---

# Get Order Info

info

  * Requires Earn permission on the API key.



### HTTP Request

GET`/v5/earn/advance/order`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
category| **true**|  string| Product category. `DoubleWin`  
productId| false| string| Filter by product ID  
orderId| false| string| Filter by order ID  
orderLinkId| false| string| Filter by user customised order ID  
startTime| false| string| Start time (order creation time), Unix timestamp in ms  
endTime| false| string| End time, Unix timestamp in ms  
limit| false| int| Number of items per page. Default: 20, Max: 20  
cursor| false| string| Pagination cursor. Use `nextPageCursor` from previous response  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
category| string| Product category. `DoubleWin`  
nextPageCursor| string| Next page cursor. Empty string if no more data  
list| array| Object  
> orderId| string| Order ID  
> orderLinkId| string| User customised order ID  
> productId| string| Product ID  
> category| string| Product category  
> orderType| string| `Stake`: subscribe; `Redeem`: early redemption  
> investCoin| string| Investment coin, e.g. `USDT`  
> amount| string| Order amount  
> underlyingAsset| string| Underlying asset, e.g. `BTC`, `ETH`  
> leverage| string| Leverage multiplier  
> initialPrice| string| Underlying asset index price at order time  
> lowerPrice| string| Lower bound of the price range  
> upperPrice| string| Upper bound of the price range  
> duration| string| Product term, e.g. `1d`, `3d`  
> settlementTime| string| Settlement time, Unix timestamp in ms  
> createdTime| string| Order creation time, Unix timestamp in ms  
> updatedTime| string| Order last updated time, Unix timestamp in ms  
> status| string| `Pending`: confirming; `Success`: order successful, position created; `Settled`: settled (on expiry or early redemption); `Fail`: order failed  
> settlementPrice| string| Settlement price. Only available when `status=Settled`  
> pnl| string| Profit and loss amount. Only available when `status=Settled`  
> refundStatus| string| Refund status. Only valid when `status=Fail`: `Processing` (refund in progress), `Processed` (refund completed)  
> accountType| string| Staking account: `FUND` or `UNIFIED`  
> toAccountType| string| Account that receives the settlement. Only available when `status=Settled` or `status=Fail`  
  
* * *

### Request Example
    
    
    GET /v5/earn/advance/order?category=DoubleWin&orderId=97f198e9-b14b-4703-b4a6-a4aa06ba1499 HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1672280218882  
    X-BAPI-RECV-WINDOW: 5000  
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "",  
        "result": {  
            "category": "DoubleWin",  
            "list": [  
                {  
                    "orderId": "05184c23-8a98-456c-a2af-0ef1c45116cc",  
                    "orderLinkId": "usdt-earn-009",  
                    "productId": "14084",  
                    "category": "DoubleWin",  
                    "orderType": "Stake",  
                    "investCoin": "USDT",  
                    "amount": "150",  
                    "underlyingAsset": "BTC",  
                    "initialPrice": "66445.69",  
                    "lowerPrice": "66245.69",  
                    "upperPrice": "66645.69",  
                    "leverage": "9.3309793178843419",  
                    "settlementTime": "1775203200000",  
                    "duration": "1d",  
                    "createdTime": "1775107011000",  
                    "updatedTime": "1775107011000",  
                    "status": "Success",  
                    "settlementPrice": "",  
                    "pnl": "",  
                    "refundStatus": "",  
                    "accountType": "FUND",  
                    "toAccountType": ""  
                }  
            ],  
            "nextPageCursor": ""  
        },  
        "retExtInfo": {},  
        "time": 1775107200953  
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
category| **true**|  string| 產品類別，`DoubleWin`  
productId| false| string| 按產品 ID 篩選  
orderId| false| string| 按訂單 ID 篩選  
orderLinkId| false| string| 按用戶自定義訂單 ID 篩選  
startTime| false| string| 開始時間（訂單創建時間），毫秒級 Unix 時間戳  
endTime| false| string| 結束時間，毫秒級 Unix 時間戳  
limit| false| int| 每頁返回數量。預設：20，最大：20  
cursor| false| string| 分頁游標。使用上次響應中的 `nextPageCursor`  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
category| string| 產品類別，`DoubleWin`  
nextPageCursor| string| 下一頁游標，為空字串表示無更多資料  
list| array| 列表  
> orderId| string| 訂單 ID  
> orderLinkId| string| 用戶自定義訂單 ID  
> productId| string| 產品 ID  
> category| string| 產品類別  
> orderType| string| `Stake`：申購；`Redeem`：提前贖回  
> investCoin| string| 投資幣種，例如：`USDT`  
> amount| string| 訂單金額  
> underlyingAsset| string| 標的資產，例如：`BTC`, `ETH`  
> leverage| string| 槓桿倍數  
> initialPrice| string| 下單時的標的資產指數價格  
> lowerPrice| string| 價格區間下限  
> upperPrice| string| 價格區間上限  
> duration| string| 產品期限，例如：`1d`, `3d`  
> settlementTime| string| 結算時間，毫秒級 Unix 時間戳  
> createdTime| string| 訂單創建時間，毫秒級 Unix 時間戳  
> updatedTime| string| 訂單最後更新時間，毫秒級 Unix 時間戳  
> status| string| `Pending`：確認中；`Success`：訂單成功，已創建倉位；`Settled`：已結算（到期結算或提前贖回完成）；`Fail`：訂單失敗  
> settlementPrice| string| 結算價格。僅在 `status=Settled` 時有值  
> pnl| string| 盈虧金額。僅在 `status=Settled` 時有值  
> refundStatus| string| 退款狀態。僅在 `status=Fail` 時有效：`Processing`（退款處理中），`Processed`（退款完成）  
> accountType| string| 申購帳戶：`FUND`（資金帳戶），`UNIFIED`（統一帳戶）  
> toAccountType| string| 結算到帳帳戶。僅在 `status=Settled` 或 `status=Fail` 時有值  
  
* * *

### 請求示例
    
    
    GET /v5/earn/advance/order?category=DoubleWin&orderId=97f198e9-b14b-4703-b4a6-a4aa06ba1499 HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1672280218882  
    X-BAPI-RECV-WINDOW: 5000  
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "",  
        "result": {  
            "category": "DoubleWin",  
            "list": [  
                {  
                    "orderId": "05184c23-8a98-456c-a2af-0ef1c45116cc",  
                    "orderLinkId": "usdt-earn-009",  
                    "productId": "14084",  
                    "category": "DoubleWin",  
                    "orderType": "Stake",  
                    "investCoin": "USDT",  
                    "amount": "150",  
                    "underlyingAsset": "BTC",  
                    "initialPrice": "66445.69",  
                    "lowerPrice": "66245.69",  
                    "upperPrice": "66645.69",  
                    "leverage": "9.3309793178843419",  
                    "settlementTime": "1775203200000",  
                    "duration": "1d",  
                    "createdTime": "1775107011000",  
                    "updatedTime": "1775107011000",  
                    "status": "Success",  
                    "settlementPrice": "",  
                    "pnl": "",  
                    "refundStatus": "",  
                    "accountType": "FUND",  
                    "toAccountType": ""  
                }  
            ],  
            "nextPageCursor": ""  
        },  
        "retExtInfo": {},  
        "time": 1775107200953  
    }