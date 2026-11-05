---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/finance/advanced-earn/liquidity-mining/yield-records
api_type: REST
updated_at: 2026-11-05 18:36:20.244546
---

# Get Order Info

info

  * Need authentication. **Up to 10 requests** per second.
  * Query your order history. Requires Earn permission on the API key.



### HTTP Request

GET`/v5/earn/advance/order`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
category| **true**|  string| Product type. `SmartLeverage`  
productId| false| string| Product ID  
orderId| false| string| Order ID  
orderLinkId| false| string| User customised order ID  
startTime| false| string| Start time (order creation time), unix timestamp in milliseconds  
endTime| false| string| End time, unix timestamp in milliseconds  
limit| false| int| Number of items per page. Default: 20, Max: 20  
cursor| false| string| Pagination cursor. Use nextPageCursor from previous response  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
category| string| Product category  
nextPageCursor| string| Next page cursor, empty means no more data  
list| array| Order list  
> orderId| string| Order ID  
> orderLinkId| string| User customised order ID  
> productId| string| Product ID  
> category| string| Product category  
> orderType| string| `Stake`: Subscribe. `Redeem`: Early redemption  
> amount| string| Order amount  
> createdTime| string| Created time, unix timestamp in ms  
> status| string| `Pending`: Order confirming, `Success`: Order successful (position created), `Settled`: Position settled, `Fail`: Order failed  
> duration| string| Product term, e.g. `1d`, `2d`, `3d`  
> accountType| string| Account type  
> settlementTime| string| Settlement time, unix timestamp in ms  
> refundStatus| string| Refund status. Only valid when status=`Fail`, `Processing`, `Processed`  
> investCoin| string| Investment coin, e.g. `USDT`  
> underlyingAsset| string| Underlying asset, e.g. `BTC`, `ETH`  
> direction| string| `Long`, `Short`  
> leverage| string| Fixed leverage multiplier  
> breakevenPrice| string| Breakeven price  
> initialPrice| string| Underlying asset price at order time  
> settlementPrice| string| Settlement price. Only available when `status=Settled`  
> pnl| string| Profit and loss. Only available when `status=Settled`  
> toAccountType| string| The account back to when redeem. Only available when `status=Settled` or `status=Fail`  
  
* * *

### Request Example
    
    
    GET /v5/earn/advance/order?category=SmartLeverage&orderId=3e7d23fb-acc4-4853-9e32-ab0c0eb43985 HTTP/1.1  
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
            "category": "SmartLeverage",  
            "list": [  
                {  
                    "orderId": "3e7d23fb-acc4-4853-9e32-ab0c0eb43985",  
                    "orderLinkId": "usdt-earn-008",  
                    "productId": "12999",  
                    "category": "SmartLeverage",  
                    "orderType": "Redeem",  
                    "investCoin": "USDT",  
                    "amount": "100",  
                    "underlyingAsset": "BTC",  
                    "direction": "Long",  
                    "leverage": "200",  
                    "breakevenPrice": "68622.69",  
                    "initialPrice": "68403",  
                    "settlementTime": "1775038327000",  
                    "duration": "2d",  
                    "createdTime": "1775038326000",  
                    "status": "Settled",  
                    "settlementPrice": "68566.72",  
                    "pnl": "83.6876",  
                    "refundStatus": "",  
                    "accountType": "",  
                    "toAccountType": "FUND"  
                }  
            ],  
            "nextPageCursor": ""  
        },  
        "retExtInfo": {},  
        "time": 1775038381558  
    }

---

# 查詢訂單資訊

信息

  * 需要身份驗證。每秒**最多 10 次請求** 。
  * 查詢訂單歷史記錄。API 金鑰需要具備 Earn（理財）權限。



### HTTP 請求

GET`/v5/earn/advance/order`

### 請求參數

參數| 必填| 類型| 說明  
---|---|---|---  
category| **true**|  string| 產品類型，`SmartLeverage`  
productId| false| string| 產品 ID  
orderId| false| string| 訂單 ID  
orderLinkId| false| string| 用戶自定義訂單 ID  
startTime| false| string| 開始時間（訂單創建時間），毫秒級 Unix 時間戳  
endTime| false| string| 結束時間，毫秒級 Unix 時間戳  
limit| false| int| 每頁返回數量。預設：20，最大：20  
cursor| false| string| 分頁游標。使用上次響應中的 nextPageCursor  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
category| string| 產品類別  
nextPageCursor| string| 下一頁游標，為空表示無更多資料  
list| array| 訂單列表  
> orderId| string| 訂單 ID  
> orderLinkId| string| 用戶自定義訂單 ID  
> productId| string| 產品 ID  
> category| string| 產品類別  
> orderType| string| `Stake`：申購。`Redeem`：提前贖回  
> amount| string| 訂單金額  
> createdTime| string| 創建時間，毫秒級 Unix 時間戳  
> status| string| `Pending`：訂單確認中，`Success`：訂單成功（已創建倉位），`Settled`：倉位已結算，`Fail`：訂單失敗  
> duration| string| 產品期限，例如：`1d`, `2d`, `3d`  
> accountType| string| 帳戶類型  
> settlementTime| int64| 結算時間，毫秒級 Unix 時間戳  
> refundStatus| string| 退款狀態。僅在 status=`Fail` 時有效，`Processing`（處理中），`Processed`（已處理）  
> investCoin| string| 投資幣種，例如：`USDT`  
> underlyingAsset| string| 標的資產，例如：`BTC`, `ETH`  
> direction| string| `Long`（多頭），`Short`（空頭）  
> leverage| string| 固定槓桿倍數  
> breakevenPrice| string| 損益平衡價格  
> initialPrice| string| 下單時的標的資產價格  
> settlementPrice| string| 結算價格。僅在 `status=Settled` 時有值  
> pnl| string| 盈虧。僅在 `status=Settled` 時有值  
> toAccountType| string| 贖回後返回的帳戶。僅在 `status=Settled` 或 `status=Fail` 時有值  
  
* * *

### 請求示例
    
    
    GET /v5/earn/advance/order?category=SmartLeverage&orderId=3e7d23fb-acc4-4853-9e32-ab0c0eb43985 HTTP/1.1  
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
            "category": "SmartLeverage",  
            "list": [  
                {  
                    "orderId": "3e7d23fb-acc4-4853-9e32-ab0c0eb43985",  
                    "orderLinkId": "usdt-earn-008",  
                    "productId": "12999",  
                    "category": "SmartLeverage",  
                    "orderType": "Redeem",  
                    "investCoin": "USDT",  
                    "amount": "100",  
                    "underlyingAsset": "BTC",  
                    "direction": "Long",  
                    "leverage": "200",  
                    "breakevenPrice": "68622.69",  
                    "initialPrice": "68403",  
                    "settlementTime": "1775038327000",  
                    "duration": "2d",  
                    "createdTime": "1775038326000",  
                    "status": "Settled",  
                    "settlementPrice": "68566.72",  
                    "pnl": "83.6876",  
                    "refundStatus": "",  
                    "accountType": "",  
                    "toAccountType": "FUND"  
                }  
            ],  
            "nextPageCursor": ""  
        },  
        "retExtInfo": {},  
        "time": 1775038381558  
    }