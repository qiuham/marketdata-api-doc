---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/finance/advanced-earn/discount-buy/create-order
api_type: REST
updated_at: 2026-06-29 19:27:41.453679
---

# Get Position Info

info

  * Requires Earn permission on the API key.
  * Returns active positions only. Settled positions are not returned.
  * MNT positions are not included in the response.



### HTTP Request

GET`/v5/earn/advance/position`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
category| **true**|  string| Product category. `DiscountBuy`  
productId| false| string| Filter by product ID  
coin| false| string| Filter by underlying coin, e.g. `USDT`  
limit| false| int| Number of items per page  
cursor| false| string| Pagination cursor. Use `nextPageCursor` from previous response  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
nextPageCursor| string| Cursor for the next page. Empty string if no more data  
list| array| Object  
> positionId| string| Position ID  
> productId| string| Product ID  
> category| string| Product category. `DiscountBuy`  
> coin| string| Investment coin, e.g. `USDT`  
> underlyingAsset| string| Underlying asset, e.g. `BTC`, `ETH`  
> amount| string| Investment amount  
> purchasePrice| string| Anchor buy price locked at order time  
> knockoutPrice| string| Knockout price  
> knockoutCouponE8| string| Annualized interest rate in e8 precision. Actual rate = `knockoutCouponE8` / 1e8  
> status| string| Position status: `Active` (holding); `Settling` (settlement in progress)  
> orderId| string| Associated order ID  
> duration| string| Product duration, e.g. `7d`  
> settlementTime| string| Settlement time, Unix timestamp in ms  
> accountType| string| Deduction account: `FUND` or `UNIFIED`  
> toAccountType| string| Settlement credit account. Always `FUND`  
> settleType| string| Settlement preference when exercised: `Base` = receive underlying asset; `Quote` = receive USDT. Has no effect upon knockout  
> expectReceiveAt| string| Expected settlement credit time, Unix timestamp in ms. Equal to `settlementTime` \+ 15 minutes  
  
### Request Example
    
    
    GET /v5/earn/advance/position?category=DiscountBuy&productId=7037 HTTP/1.1  
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
                    "positionId": "11959",  
                    "productId": "7037",  
                    "category": "DiscountBuy",  
                    "coin": "USDT",  
                    "underlyingAsset": "BTC",  
                    "amount": "200",  
                    "purchasePrice": "74019",  
                    "knockoutPrice": "76050",  
                    "knockoutCouponE8": "1000000",  
                    "status": "Active",  
                    "orderId": "38f6f5ce-57e2-4d69-b4d3-c39464389ccb",  
                    "duration": "1d",  
                    "settlementTime": "1776240000000",  
                    "accountType": "FUND",  
                    "toAccountType": "FUND",  
                    "settleType": "Base",  
                    "expectReceiveAt": "1776240900000"  
                }  
            ],  
            "nextPageCursor": ""  
        },  
        "retExtInfo": {},  
        "time": 1776154219022  
    }

---

# 查詢倉位資訊

信息

  * API 金鑰需要具備 Earn（理財）權限。
  * 僅返回持倉中的倉位，已結算倉位不會包含在內。
  * 返回數據不包含 MNT 倉位。



### HTTP 請求

GET`/v5/earn/advance/position`

### 請求參數

參數| 必填| 類型| 說明  
---|---|---|---  
category| **true**|  string| 產品類別，`DiscountBuy`  
productId| false| string| 按產品 ID 篩選  
coin| false| string| 按標的資產篩選，例如：`BTC`  
limit| false| int| 每頁返回數量  
cursor| false| string| 分頁游標，使用上次響應中的 `nextPageCursor`  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
nextPageCursor| string| 下一頁游標，為空字串表示無更多資料  
list| array| 列表  
> positionId| string| 倉位 ID  
> productId| string| 產品 ID  
> category| string| 產品類別，`DiscountBuy`  
> coin| string| 投資幣種，例如：`USDT`  
> underlyingAsset| string| 標的資產，例如：`BTC`, `ETH`  
> amount| string| 投資金額  
> purchasePrice| string| 下單時鎖定的錨定買入價  
> knockoutPrice| string| 敲出價  
> knockoutCouponE8| string| 年化息率（e8 精度），實際利率 = `knockoutCouponE8` / 1e8  
> status| string| 倉位狀態：`Active`（持倉中），`Settling`（結算處理中）  
> orderId| string| 關聯訂單 ID  
> duration| string| 產品期限，例如：`7d`  
> settlementTime| string| 結算時間，毫秒級 Unix 時間戳  
> accountType| string| 扣款帳戶：`FUND`（資金帳戶），`UNIFIED`（統一帳戶）  
> toAccountType| string| 結算入帳帳戶，固定為 `FUND`  
> settleType| string| 行權結算方式：`Base` = 收取標的資產；`Quote` = 收取 USDT。敲出時此參數無效  
> expectReceiveAt| string| 預計到帳時間，毫秒級 Unix 時間戳，等於 `settlementTime` \+ 15 分鐘  
  
### 請求示例
    
    
    GET /v5/earn/advance/position?category=DiscountBuy&productId=7037 HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1776154219022  
    X-BAPI-RECV-WINDOW: 5000  
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "",  
        "result": {  
            "category": "",  
            "list": [  
                {  
                    "positionId": "11959",  
                    "productId": "7037",  
                    "category": "DiscountBuy",  
                    "coin": "USDT",  
                    "underlyingAsset": "BTC",  
                    "amount": "200",  
                    "purchasePrice": "74019",  
                    "knockoutPrice": "76050",  
                    "knockoutCouponE8": "1000000",  
                    "status": "Active",  
                    "orderId": "38f6f5ce-57e2-4d69-b4d3-c39464389ccb",  
                    "duration": "1d",  
                    "settlementTime": "1776240000000",  
                    "accountType": "FUND",  
                    "toAccountType": "FUND",  
                    "settleType": "Base",  
                    "expectReceiveAt": "1776240900000"  
                }  
            ],  
            "nextPageCursor": ""  
        },  
        "retExtInfo": {},  
        "time": 1776154219022  
    }