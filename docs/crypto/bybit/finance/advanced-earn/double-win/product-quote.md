---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/finance/advanced-earn/double-win/product-quote
api_type: REST
updated_at: 2026-11-12 18:29:05.811535
---

# Get Position Info

info

  * Need authentication. **Up to 10 requests** per second.
  * Query your active Dual Assets positions. Requires Earn permission on the API key.



### HTTP Request

GET `/v5/earn/advance/position`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
[category](/docs/v5/enum#advanced-earn-category)| **true**|  string| Product type, e.g. `DualAssets`  
productId| false| string| Product ID  
coin| false| string| Coin  
limit| false| int| Number of items per page. Default: 20, Max: 20  
cursor| false| string| Pagination cursor. Use nextPageCursor from previous response  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
[category](/docs/v5/enum#advanced-earn-category)| string| `DualAssets`  
nextPageCursor| string| Cursor for the next page. Empty string if no more data  
list| array| Object  
> positionId| string| Position ID  
> productId| string| Product ID  
> [category](/docs/v5/enum#advanced-earn-category)| string| Product category, `DualAssets`  
> baseCoin| string| Base coin  
> quoteCoin| string| Quote coin  
> investCoin| string| Invest coin. `BuyLow`: same as quoteCoin; `SellHigh`: same as baseCoin  
> amount| string| Position amount, unit is investCoin  
> apyE8| string| Confirmed annualized yield in e8 precision  
> direction| string| Direction: `BuyLow`, `SellHigh`  
> targetPrice| string| Target price in USDT  
> settlementTime| string| Settlement time, unix timestamp in ms  
> [status](/docs/v5/enum#advanced-earn-position-status)| string| `Active`: Staking, `Redeeming`: Redeeming  
> orderId| string| Staking order ID  
> duration| string| Product term, e.g. 8h, 1d, 2d, 3d  
> expectReturnCoin| string| Expected settlement coin  
> expectReturnAmount| string| Expected settlement amount  
> accountType| string| Staking account: `FUND`, `UNIFIED`  
> toAccountType| string| Settlement account: `FUND`, currently only supports settlement to `Fund` account  
> yieldStartAt| int64| Yield start time, unix timestamp in ms  
> yieldEndAt| int64| Yield end time, unix timestamp in ms  
  
* * *

### Request Example

  * HTTP


    
    
    GET /v5/earn/advance/position?category=DualAssets HTTP/1.1  
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
            "category": "DualAssets",  
            "list": [  
                {  
                    "positionId": "19035",  
                    "productId": "36320",  
                    "category": "DualAssets",  
                    "baseCoin": "ETH",  
                    "quoteCoin": "USDT",  
                    "investCoin": "USDT",  
                    "amount": "20",  
                    "apyE8": "902700000",  
                    "direction": "BuyLow",  
                    "targetPrice": "2325",  
                    "settlementTime": "1774079999000",  
                    "status": "Active",  
                    "orderId": "ef9644c2-0c98-40e5-ae33-8aa5b6d85058",  
                    "duration": "3d",  
                    "expectReturnCoin": "USDT",  
                    "expectReturnAmount": "21.4838",  
                    "accountType": "UNIFIED",  
                    "toAccountType": "FUND",  
                    "yieldStartAt": "1773820799000",  
                    "yieldEndAt": "1774079999000"  
                }  
            ],  
            "nextPageCursor": ""  
        },  
        "retExtInfo": {},  
        "time": 1773815399307  
    }

---

# 查詢倉位資訊

信息

  * 需要身份驗證。每秒**最多 10 次請求** 。
  * 查詢您當前生效的雙幣投資倉位。API 金鑰需要具備 Earn (理財) 權限。



### HTTP 請求

GET `/v5/earn/advance/position`

### 請求參數

參數| 必填| 類型| 說明  
---|---|---|---  
[category](/docs/zh-TW/v5/enum#advanced-earn-category)| **true**|  string| 產品類型，例如 `DualAssets`  
productId| false| string| 產品 ID  
coin| false| string| 幣種  
limit| false| int| 每頁數量。預設值：20，最大值：20  
cursor| false| string| 分頁游標。請使用上一次請求返回的 `nextPageCursor`  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
[category](/docs/zh-TW/v5/enum#advanced-earn-category)| string| `DualAssets`  
nextPageCursor| string| 下一頁的游標。如果沒有更多資料則為空字串  
list| array| 列表  
> positionId| string| 倉位 ID  
> productId| string| 產品 ID  
> [category](/docs/zh-TW/v5/enum#advanced-earn-category)| string| 產品類別，`DualAssets`  
> baseCoin| string| 基礎幣種 (Base Coin)  
> quoteCoin| string| 計價幣種 (Quote Coin)  
> investCoin| string| 投資幣種。`BuyLow` (低買)：與計價幣種相同；`SellHigh` (高賣)：與基礎幣種相同  
> amount| string| 倉位數量，單位為 `investCoin` (投資幣種)  
> apyE8| string| 已確認的年化收益率（e8 精度）  
> direction| string| 方向：`BuyLow` (低買), `SellHigh` (高賣)  
> targetPrice| string| 目標價格（掛鉤價），單位為 USDT  
> settlementTime| string| 結算時間，毫秒級 Unix 時間戳  
> [status](/docs/zh-TW/v5/enum#advanced-earn-position-status)| string| `Active`: 申購中 (生效中), `Redeeming`: 贖回中  
> orderId| string| 申購訂單 ID  
> duration| string| 產品期限，例如 8h, 1d, 2d, 3d  
> expectReturnCoin| string| 預計結算幣種  
> expectReturnAmount| string| 預計結算數量  
> accountType| string| 申購帳戶：`FUND` (資金帳戶), `UNIFIED` (統一帳戶)  
> toAccountType| string| 結算帳戶：`FUND`，目前僅支援結算至資金帳戶 (Fund)  
> yieldStartAt| int64| 計息開始時間，毫秒級 Unix 時間戳  
> yieldEndAt| int64| 計息結束時間，毫秒級 Unix 時間戳  
  
* * *

### 請求示例

  * HTTP


    
    
    GET /v5/earn/advance/position?category=DualAssets HTTP/1.1  
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
            "category": "DualAssets",  
            "list": [  
                {  
                    "positionId": "19035",  
                    "productId": "36320",  
                    "category": "DualAssets",  
                    "baseCoin": "ETH",  
                    "quoteCoin": "USDT",  
                    "investCoin": "USDT",  
                    "amount": "20",  
                    "apyE8": "902700000",  
                    "direction": "BuyLow",  
                    "targetPrice": "2325",  
                    "settlementTime": "1774079999000",  
                    "status": "Active",  
                    "orderId": "ef9644c2-0c98-40e5-ae33-8aa5b6d85058",  
                    "duration": "3d",  
                    "expectReturnCoin": "USDT",  
                    "expectReturnAmount": "21.4838",  
                    "accountType": "UNIFIED",  
                    "toAccountType": "FUND",  
                    "yieldStartAt": "1773820799000",  
                    "yieldEndAt": "1774079999000"  
                }  
            ],  
            "nextPageCursor": ""  
        },  
        "retExtInfo": {},  
        "time": 1773815399307  
    }