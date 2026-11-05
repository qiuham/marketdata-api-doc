---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/finance/advanced-earn/double-win/leverage
api_type: REST
updated_at: 2026-11-05 18:35:55.784710
---

# Get Position Info

info

  * Requires Earn permission on the API key.
  * Returns active positions only. Settled positions are not returned.



### HTTP Request

GET`/v5/earn/advance/position`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
category| **true**|  string| Product category. `DoubleWin`  
productId| false| string| Filter by product ID  
coin| false| string| Filter by underlying asset, e.g. `BTC`, `ETH`  
limit| false| int| Number of items per page. Default: 20, Max: 20  
cursor| false| string| Pagination cursor. Use `nextPageCursor` from previous response  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
category| string| Product category. `DoubleWin`  
nextPageCursor| string| Cursor for the next page. Empty string if no more data  
list| array| Object  
> positionId| string| Position ID  
> productId| string| Product ID  
> category| string| Product category  
> investCoin| string| Investment coin, e.g. `USDT`  
> underlyingAsset| string| Underlying asset, e.g. `BTC`, `ETH`  
> amount| string| Position amount in `investCoin`  
> leverage| string| Leverage multiplier  
> initialPrice| string| Underlying asset index price at position creation  
> lowerPrice| string| Lower bound of the price range  
> upperPrice| string| Upper bound of the price range  
> duration| string| Product term, e.g. `1d`, `3d`  
> settlementTime| string| Settlement time, Unix timestamp in ms  
> createdTime| string| Position creation time, Unix timestamp in ms  
> status| string| `Active`: holding; `Redeeming`: early redemption in progress  
> redeemable| bool| Whether the position can be redeemed now. `false` if a pending redeem order exists or less than 30 minutes remain until settlement  
> accountType| string| Staking account: `FUND` or `UNIFIED`  
> orderId| string| Staking order ID  
  
* * *

### Request Example
    
    
    GET /v5/earn/advance/position?category=DoubleWin&productId=20001 HTTP/1.1  
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
                    "positionId": "2848",  
                    "productId": "14084",  
                    "category": "DoubleWin",  
                    "investCoin": "USDT",  
                    "underlyingAsset": "BTC",  
                    "amount": "150",  
                    "leverage": "9.3309793178843419",  
                    "initialPrice": "66445.69",  
                    "lowerPrice": "66245.69",  
                    "upperPrice": "66645.69",  
                    "duration": "1d",  
                    "settlementTime": "1775203200000",  
                    "createdTime": "1775107014000",  
                    "status": "Active",  
                    "redeemable": true,  
                    "accountType": "FUND",  
                    "orderId": "05184c23-8a98-456c-a2af-0ef1c45116cc"  
                }  
            ],  
            "nextPageCursor": ""  
        },  
        "retExtInfo": {},  
        "time": 1775107714828  
    }

---

# 查詢倉位資訊

信息

  * API 金鑰需要具備 Earn（理財）權限。
  * 僅返回活躍倉位，已結算的倉位不返回。



### HTTP 請求

GET`/v5/earn/advance/position`

### 請求參數

參數| 必填| 類型| 說明  
---|---|---|---  
category| **true**|  string| 產品類別，`DoubleWin`  
productId| false| string| 按產品 ID 篩選  
coin| false| string| 按標的資產篩選，例如：`BTC`, `ETH`  
limit| false| int| 每頁返回數量。預設：20，最大：20  
cursor| false| string| 分頁游標。使用上次響應中的 `nextPageCursor`  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
category| string| 產品類別，`DoubleWin`  
nextPageCursor| string| 下一頁游標，為空字串表示無更多資料  
list| array| 列表  
> positionId| string| 倉位 ID  
> productId| string| 產品 ID  
> category| string| 產品類別  
> investCoin| string| 投資幣種，例如：`USDT`  
> underlyingAsset| string| 標的資產，例如：`BTC`, `ETH`  
> amount| string| 倉位金額，單位為 `investCoin`  
> leverage| string| 槓桿倍數  
> initialPrice| string| 建倉時的標的資產指數價格  
> lowerPrice| string| 價格區間下限  
> upperPrice| string| 價格區間上限  
> duration| string| 產品期限，例如：`1d`, `3d`  
> settlementTime| string| 結算時間，毫秒級 Unix 時間戳  
> createdTime| string| 倉位創建時間，毫秒級 Unix 時間戳  
> status| string| `Active`：持倉中；`Redeeming`：提前贖回進行中  
> redeemable| bool| 是否可立即贖回。若存在待處理的贖回訂單，或距結算時間不足 30 分鐘，則為 `false`  
> accountType| string| 申購帳戶：`FUND`（資金帳戶），`UNIFIED`（統一帳戶）  
> orderId| string| 申購訂單 ID  
  
* * *

### 請求示例
    
    
    GET /v5/earn/advance/position?category=DoubleWin&productId=20001 HTTP/1.1  
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
                    "positionId": "2848",  
                    "productId": "14084",  
                    "category": "DoubleWin",  
                    "investCoin": "USDT",  
                    "underlyingAsset": "BTC",  
                    "amount": "150",  
                    "leverage": "9.3309793178843419",  
                    "initialPrice": "66445.69",  
                    "lowerPrice": "66245.69",  
                    "upperPrice": "66645.69",  
                    "duration": "1d",  
                    "settlementTime": "1775203200000",  
                    "createdTime": "1775107014000",  
                    "status": "Active",  
                    "redeemable": true,  
                    "accountType": "FUND",  
                    "orderId": "05184c23-8a98-456c-a2af-0ef1c45116cc"  
                }  
            ],  
            "nextPageCursor": ""  
        },  
        "retExtInfo": {},  
        "time": 1775107714828  
    }