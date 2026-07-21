---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/finance/advanced-earn/double-win/product-info
api_type: REST
updated_at: 2026-07-21 18:57:06.027208
---

# Get Product Info

info

Does not need authentication

### HTTP Request

GET`/v5/earn/advance/product`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
category| **true**|  string| Product category. `DoubleWin`  
coin| false| string| Underlying asset to filter by, uppercase only, e.g. `BTC`, `ETH`  
duration| false| string| Product duration, e.g. `1d`, `2d`, `3d`  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
category| string| Product category. `DoubleWin`  
list| array| Object  
> category| string| Product category  
> productId| string| Product ID  
> investCoin| string| Investment coin, e.g. `USDT`  
> underlyingAsset| string| Underlying asset, e.g. `BTC`, `ETH`  
> duration| string| Product duration, e.g. `1d`, `2d`, `3d`  
> subscribeStartAt| string| Subscription start time, Unix timestamp in ms  
> subscribeEndAt| string| Subscription end time, Unix timestamp in ms  
> settlementTime| string| Settlement time, Unix timestamp in ms  
> expectReceiveAt| string| Expected time to receive settlement funds, Unix timestamp in ms  
> minPurchaseAmount| string| Minimum single order amount  
> orderPrecisionDigital| int| Order amount precision (decimal places)  
> isRfqProduct| bool| `false`: fixed price range product; `true`: RFQ custom price range product  
> lowerPriceBuffer| string| **Fixed range only** (`isRfqProduct=false`). Lower price buffer offset. Actual lower price = `initialPrice - lowerPriceBuffer`  
> upperPriceBuffer| string| **Fixed range only** (`isRfqProduct=false`). Upper price buffer offset. Actual upper price = `initialPrice + upperPriceBuffer`  
> minDeviationRatio| string| **RFQ only** (`isRfqProduct=true`). Minimum allowed deviation ratio of the custom price from current price  
> maxDeviationRatio| string| **RFQ only** (`isRfqProduct=true`). Maximum allowed deviation ratio of the custom price from current price  
> priceTickSize| string| **RFQ only** (`isRfqProduct=true`). Price tick size. Custom lower/upper prices must be a multiple of this value  
  
### Request Example
    
    
    GET /v5/earn/advance/product?category=DoubleWin&coin=BTC HTTP/1.1  
    Host: api-testnet.bybit.com  
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "",  
        "result": {  
            "category": "DoubleWin",  
            "list": [  
                {  
                    "category": "DoubleWin",  
                    "productId": "14092",  
                    "investCoin": "USDT",  
                    "underlyingAsset": "BTC",  
                    "duration": "2d",  
                    "expectReceiveAt": "1775290500000",  
                    "minPurchaseAmount": "10",  
                    "subscribeStartAt": "1775088000000",  
                    "subscribeEndAt": "1775174399000",  
                    "settlementTime": "1775289600000",  
                    "orderPrecisionDigital": 4,  
                    "isRfqProduct": true,  
                    "lowerPriceBuffer": "",  
                    "upperPriceBuffer": "",  
                    "minDeviationRatio": "0.01",  
                    "maxDeviationRatio": "0.15",  
                    "priceTickSize": "500"  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1775100184409  
    }

---

# 查詢產品資訊

信息

無需身份驗證

### HTTP 請求

GET`/v5/earn/advance/product`

### 請求參數

參數| 必填| 類型| 說明  
---|---|---|---  
category| **true**|  string| 產品類別，`DoubleWin`  
coin| false| string| 標的資產篩選，僅限大寫，例如：`BTC`, `ETH`  
duration| false| string| 產品期限篩選，例如：`1d`, `2d`, `3d`  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
category| string| 產品類別，`DoubleWin`  
list| array| 列表  
> category| string| 產品類別  
> productId| string| 產品 ID  
> investCoin| string| 投資幣種，例如：`USDT`  
> underlyingAsset| string| 標的資產，例如：`BTC`, `ETH`  
> duration| string| 產品期限，例如：`1d`, `2d`, `3d`  
> subscribeStartAt| string| 申購開始時間，毫秒級 Unix 時間戳  
> subscribeEndAt| string| 申購結束時間，毫秒級 Unix 時間戳  
> settlementTime| string| 結算時間，毫秒級 Unix 時間戳  
> expectReceiveAt| string| 預計結算資金到帳時間，毫秒級 Unix 時間戳  
> minPurchaseAmount| string| 最小單筆申購金額  
> orderPrecisionDigital| int| 訂單金額精度（小數位數）  
> isRfqProduct| bool| `false`：固定區間產品；`true`：RFQ 自選區間產品  
> lowerPriceBuffer| string| **僅固定區間產品有效** （`isRfqProduct=false`）。價格緩衝區間（下限），實際下限價格 = `initialPrice - lowerPriceBuffer`  
> upperPriceBuffer| string| **僅固定區間產品有效** （`isRfqProduct=false`）。價格緩衝區間（上限），實際上限價格 = `initialPrice + upperPriceBuffer`  
> minDeviationRatio| string| **僅 RFQ 產品有效** （`isRfqProduct=true`）。自選價格偏離當前價格的最小允許比例  
> maxDeviationRatio| string| **僅 RFQ 產品有效** （`isRfqProduct=true`）。自選價格偏離當前價格的最大允許比例  
> priceTickSize| string| **僅 RFQ 產品有效** （`isRfqProduct=true`）。價格步長，自選下限/上限價格須為此值的整數倍  
  
### 請求示例
    
    
    GET /v5/earn/advance/product?category=DoubleWin&coin=BTC HTTP/1.1  
    Host: api-testnet.bybit.com  
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "",  
        "result": {  
            "category": "DoubleWin",  
            "list": [  
                {  
                    "category": "DoubleWin",  
                    "productId": "14092",  
                    "investCoin": "USDT",  
                    "underlyingAsset": "BTC",  
                    "duration": "2d",  
                    "expectReceiveAt": "1775290500000",  
                    "minPurchaseAmount": "10",  
                    "subscribeStartAt": "1775088000000",  
                    "subscribeEndAt": "1775174399000",  
                    "settlementTime": "1775289600000",  
                    "orderPrecisionDigital": 4,  
                    "isRfqProduct": true,  
                    "lowerPriceBuffer": "",  
                    "upperPriceBuffer": "",  
                    "minDeviationRatio": "0.01",  
                    "maxDeviationRatio": "0.15",  
                    "priceTickSize": "500"  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1775100184409  
    }