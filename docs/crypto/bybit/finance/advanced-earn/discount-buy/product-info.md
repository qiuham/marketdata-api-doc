---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/finance/advanced-earn/discount-buy/product-info
api_type: REST
updated_at: 2026-11-13 19:22:42.713733
---

# Get Product Info

info

Does not need authentication

### HTTP Request

GET`/v5/earn/advance/product`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
category| **true**|  string| Product category. `DiscountBuy`  
coin| false| string| Filter by underlying asset, e.g. `BTC`, `ETH`  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
list| array| Object  
> category| string| Product category. `DiscountBuy`  
> productId| string| Product ID  
> coin| string| Investment coin, e.g. `USDT`  
> underlyingAsset| string| Underlying asset, e.g. `BTC`, `ETH`  
> settlementTime| string| Settlement time, Unix timestamp in ms  
> duration| string| Product duration, e.g. `7d`  
> isVipProduct| bool| Whether this is a VIP-exclusive product  
> subscribeStartAt| string| Subscription start time, Unix timestamp in ms  
> subscribeEndAt| string| Subscription end time, Unix timestamp in ms  
> minPurchaseAmount| string| Minimum purchase amount  
> remainingAmount| string| Remaining purchasable quota for this product  
> orderPrecisionDigital| int| Order amount precision (decimal places)  
> expectReceiveAt| string| Expected settlement credit time, Unix timestamp in ms. Equal to `settlementTime` \+ 15 minutes  
  
### Request Example
    
    
    GET /v5/earn/advance/product?category=DiscountBuy&coin=BTC HTTP/1.1  
    Host: api-testnet.bybit.com  
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "",  
        "result": {  
            "category": "",  
            "list": [  
                {  
                    "category": "DiscountBuy",  
                    "productId": "7038",  
                    "coin": "USDT",  
                    "underlyingAsset": "BTC",  
                    "settlementTime": "1776240000000",  
                    "duration": "1d",  
                    "isVipProduct": true,  
                    "subscribeStartAt": "1776124800000",  
                    "subscribeEndAt": "1776211199000",  
                    "minPurchaseAmount": "100",  
                    "remainingAmount": "10000000",  
                    "orderPrecisionDigital": 4,  
                    "expectReceiveAt": "1776240900000"  
                },  
                {  
                    "category": "DiscountBuy",  
                    "productId": "7037",  
                    "coin": "USDT",  
                    "underlyingAsset": "BTC",  
                    "settlementTime": "1776240000000",  
                    "duration": "1d",  
                    "isVipProduct": false,  
                    "subscribeStartAt": "1776124800000",  
                    "subscribeEndAt": "1776211199000",  
                    "minPurchaseAmount": "100",  
                    "remainingAmount": "9998547.575",  
                    "orderPrecisionDigital": 4,  
                    "expectReceiveAt": "1776240900000"  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1776152654908  
    }

---

# 查詢產品資訊

信息

無需身份驗證

備註

僅返回當前可申購的產品。已下線、不在申購窗口內或已售罄的產品不會包含在內。

### HTTP 請求

GET`/v5/earn/advance/product`

### 請求參數

參數| 必填| 類型| 說明  
---|---|---|---  
category| **true**|  string| 產品類別，`DiscountBuy`  
coin| false| string| 標的資產篩選，例如：`BTC`, `ETH`  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
list| array| 列表  
> category| string| 產品類別，`DiscountBuy`  
> productId| string| 產品 ID  
> coin| string| 投資幣種，例如：`USDT`  
> underlyingAsset| string| 標的資產，例如：`BTC`, `ETH`  
> settlementTime| string| 結算時間，毫秒級 Unix 時間戳  
> duration| string| 產品期限，例如：`7d`  
> isVipProduct| bool| 是否為 VIP 專屬產品  
> subscribeStartAt| string| 申購開始時間，毫秒級 Unix 時間戳  
> subscribeEndAt| string| 申購結束時間，毫秒級 Unix 時間戳  
> minPurchaseAmount| string| 最小單筆申購金額  
> remainingAmount| string| 產品剩餘可申購額度  
> orderPrecisionDigital| int| 訂單金額精度（小數位數）  
> expectReceiveAt| string| 預計到帳時間，毫秒級 Unix 時間戳，等於 `settlementTime` \+ 15 分鐘  
  
### 請求示例
    
    
    GET /v5/earn/advance/product?category=DiscountBuy&coin=BTC HTTP/1.1  
    Host: api-testnet.bybit.com  
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "",  
        "result": {  
            "category": "",  
            "list": [  
                {  
                    "category": "DiscountBuy",  
                    "productId": "7038",  
                    "coin": "USDT",  
                    "underlyingAsset": "BTC",  
                    "settlementTime": "1776240000000",  
                    "duration": "1d",  
                    "isVipProduct": true,  
                    "subscribeStartAt": "1776124800000",  
                    "subscribeEndAt": "1776211199000",  
                    "minPurchaseAmount": "100",  
                    "remainingAmount": "10000000",  
                    "orderPrecisionDigital": 4,  
                    "expectReceiveAt": "1776240900000"  
                },  
                {  
                    "category": "DiscountBuy",  
                    "productId": "7037",  
                    "coin": "USDT",  
                    "underlyingAsset": "BTC",  
                    "settlementTime": "1776240000000",  
                    "duration": "1d",  
                    "isVipProduct": false,  
                    "subscribeStartAt": "1776124800000",  
                    "subscribeEndAt": "1776211199000",  
                    "minPurchaseAmount": "100",  
                    "remainingAmount": "9998547.575",  
                    "orderPrecisionDigital": 4,  
                    "expectReceiveAt": "1776240900000"  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1776152654908  
    }