---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/finance/advanced-earn/smart-lvg/create-order
api_type: REST
updated_at: 2026-07-23 18:55:12.724906
---

# Get Position Info

info

  * Need authentication. **Up to 10 requests** per second.
  * Query your active positions. Requires Earn permission on the API key.



### HTTP Request

GET`/v5/earn/advance/position`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
category| **true**|  string| Product type. `SmartLeverage`  
productId| false| string| Product ID  
coin| false| string| Underlying asset to filter by, e.g. `BTC`, `ETH`  
limit| false| int| Number of items per page. Default: 20, Max: 20  
cursor| false| string| Pagination cursor. Use nextPageCursor from previous response  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
category| string| Product category  
nextPageCursor| string| Cursor for the next page. Empty string if no more data  
list| array| Object  
> positionId| string| Position ID  
> productId| string| Product ID  
> category| string| Product category  
> investCoin| string| Investment coin  
> amount| string| Position amount, unit is investCoin  
> duration| string| Product term, e.g. `1d`, `2d`, `3d`  
> settlementTime| string| Settlement time, unix timestamp in ms  
> accountType| string| Staking account: `FUND`, `UNIFIED`  
> orderId| string| Staking order ID  
> underlyingAsset| string| Underlying asset, e.g. `BTC`, `ETH`  
> direction| string| `Long`, `Short`  
> leverage| string| Fixed leverage multiplier, e.g. `3`, `5`  
> breakevenPrice| string| Breakeven price (precision-adjusted)  
> initialPrice| string| Underlying asset price at position creation (precision-adjusted)  
> status| string| `Active`: Staking, `Redeeming`: Redeeming, `Settled`: Settled  
> createdTime| string| Position creation time, unix timestamp in ms  
> redeemable| bool| Whether the position can be redeemed now. `false` if: global redemption is disabled, a pending redeem order exists, or less than 60 minutes remain until settlement  
> orderLinkId| string| User customised order ID  
  
* * *

### Request Example
    
    
    GET /v5/earn/advance/position?category=SmartLeverage&productId=12959 HTTP/1.1  
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
                    "positionId": "1252",  
                    "productId": "12959",  
                    "category": "SmartLeverage",  
                    "investCoin": "USDT",  
                    "underlyingAsset": "BTC",  
                    "direction": "Long",  
                    "leverage": "50",  
                    "amount": "1000",  
                    "breakevenPrice": "67367.16",  
                    "initialPrice": "67243.31",  
                    "duration": "1d",  
                    "settlementTime": "1774944000000",  
                    "createdTime": "1774838832000",  
                    "status": "Active",  
                    "redeemable": false,  
                    "accountType": "FUND",  
                    "orderLinkId": "",  
                    "orderId": "d7be0f06-af7b-4ae8-bd2f-37000d67edf2"  
                }  
            ],  
            "nextPageCursor": ""  
        },  
        "retExtInfo": {},  
        "time": 1775038447882  
    }

---

# 查詢倉位資訊

信息

  * 需要身份驗證。每秒**最多 10 次請求** 。
  * 查詢持倉中的倉位。API 金鑰需要具備 Earn（理財）權限。



### HTTP 請求

GET`/v5/earn/advance/position`

### 請求參數

參數| 必填| 類型| 說明  
---|---|---|---  
category| **true**|  string| 產品類型，`SmartLeverage`  
productId| false| string| 產品 ID  
coin| false| string| 標的資產篩選，例如：`BTC`, `ETH`  
limit| false| int| 每頁返回數量。預設：20，最大：20  
cursor| false| string| 分頁游標。使用上次響應中的 nextPageCursor  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
category| string| 產品類別  
nextPageCursor| string| 下一頁游標，為空字串表示無更多資料  
list| array| 列表  
> positionId| string| 倉位 ID  
> productId| string| 產品 ID  
> category| string| 產品類別  
> investCoin| string| 投資幣種  
> amount| string| 倉位金額，單位為 investCoin  
> duration| string| 產品期限，例如：`1d`, `2d`, `3d`  
> settlementTime| string| 結算時間，毫秒級 Unix 時間戳  
> accountType| string| 申購帳戶：`FUND`（資金帳戶），`UNIFIED`（統一帳戶）  
> orderId| string| 申購訂單 ID  
> underlyingAsset| string| 標的資產，例如：`BTC`, `ETH`  
> direction| string| `Long`（多頭），`Short`（空頭）  
> leverage| string| 固定槓桿倍數，例如：`3`, `5`  
> breakevenPrice| string| 損益平衡價格（精度調整後）  
> initialPrice| string| 創建倉位時的標的資產價格（精度調整後）  
> status| string| `Active`：持倉中，`Redeeming`：贖回中，`Settled`：已結算  
> createdTime| string| 倉位創建時間，毫秒級 Unix 時間戳  
> redeemable| bool| 是否可立即贖回。若全域贖回已禁用、存在待處理的贖回訂單，或距結算時間不足 60 分鐘，則為 `false`  
> orderLinkId| string| 用戶自定義訂單 ID  
  
* * *

### 請求示例
    
    
    GET /v5/earn/advance/position?category=SmartLeverage&productId=12959 HTTP/1.1  
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
                    "positionId": "1252",  
                    "productId": "12959",  
                    "category": "SmartLeverage",  
                    "investCoin": "USDT",  
                    "underlyingAsset": "BTC",  
                    "direction": "Long",  
                    "leverage": "50",  
                    "amount": "1000",  
                    "breakevenPrice": "67367.16",  
                    "initialPrice": "67243.31",  
                    "duration": "1d",  
                    "settlementTime": "1774944000000",  
                    "createdTime": "1774838832000",  
                    "status": "Active",  
                    "redeemable": false,  
                    "accountType": "FUND",  
                    "orderLinkId": "",  
                    "orderId": "d7be0f06-af7b-4ae8-bd2f-37000d67edf2"  
                }  
            ],  
            "nextPageCursor": ""  
        },  
        "retExtInfo": {},  
        "time": 1775038447882  
    }