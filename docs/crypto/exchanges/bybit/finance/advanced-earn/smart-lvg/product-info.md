---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/finance/advanced-earn/smart-lvg/product-info
api_type: REST
updated_at: 2026-05-27 19:17:08.963519
---

# Get Product Info

info

Does not need authentication. **Up to 50 requests** per second per IP .

### HTTP Request

GET`/v5/earn/advance/product`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
category| **true**|  string| Product category. `SmartLeverage`  
coin| false| string| Underlying asset to filter by, uppercase only, e.g. `BTC`, `ETH`  
duration| false| string| Product duration, e.g. `1d`, `3d`, `6d`, `12d`  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
category| string| Product category  
list| array| Object  
> category| string| Product category  
> productId| string| Product ID  
> investCoin| string| Investment coin, e.g. `USDT`  
> underlyingAsset| string| Underlying asset (price-anchored), e.g. `BTC`, `ETH`  
> direction| string| Trade direction: `Long`, `Short`  
> leverage| string| Fixed leverage multiplier, e.g. `3`, `5`  
> duration| string| Product duration, e.g. `1d`, `3d`  
> subscribeStartAt| string| Subscription start time, Unix timestamp in ms  
> subscribeEndAt| string| Subscription end time, Unix timestamp in ms  
> settlementTime| string| Settlement time, Unix timestamp in ms  
> expectReceiveAt| string| Expected time to receive the transfer, Unix timestamp in ms  
> minPurchaseAmount| string| Minimum single order amount  
> remainingAmount| string| Remaining available quota  
> orderPrecisionDigital| int| Order amount precision  
  
### Request Example
    
    
    GET /v5/earn/advance/product?category=SmartLeverage&coin=BTC HTTP/1.1  
    Host: api-testnet.bybit.com  
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "",  
        "result": {  
            "category": "SmartLeverage",  
            "list": [  
                {  
                    "category": "SmartLeverage",  
                    "productId": "13015",  
                    "investCoin": "USDT",  
                    "underlyingAsset": "BTC",  
                    "direction": "Short",  
                    "leverage": "10",  
                    "duration": "7d",  
                    "expectReceiveAt": "1775635800000",  
                    "subscribeStartAt": "1775001600000",  
                    "subscribeEndAt": "1775087999000",  
                    "settlementTime": "1775635200000",  
                    "minPurchaseAmount": "10",  
                    "remainingAmount": "9994748366.907",  
                    "orderPrecisionDigital": 4  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1775001977686  
    }

---

# 查詢產品資訊

信息

無需身份驗證。每個 IP 每秒**最多 50 次請求** 。

### HTTP 請求

GET`/v5/earn/advance/product`

### 請求參數

參數| 必填| 類型| 說明  
---|---|---|---  
category| **true**|  string| 產品類別，`SmartLeverage`  
coin| false| string| 標的資產篩選，僅限大寫，例如：`BTC`, `ETH`  
duration| false| string| 產品期限，例如：`1d`, `3d`, `6d`, `12d`  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
category| string| 產品類別  
list| array| 列表  
> category| string| 產品類別  
> productId| string| 產品 ID  
> investCoin| string| 投資幣種，例如：`USDT`  
> underlyingAsset| string| 標的資產（價格錨定），例如：`BTC`, `ETH`  
> direction| string| 交易方向：`Long`（多頭），`Short`（空頭）  
> leverage| string| 固定槓桿倍數，例如：`3`, `5`  
> duration| string| 產品期限，例如：`1d`, `3d`  
> subscribeStartAt| string| 申購開始時間，毫秒級 Unix 時間戳  
> subscribeEndAt| string| 申購結束時間，毫秒級 Unix 時間戳  
> settlementTime| string| 結算時間，毫秒級 Unix 時間戳  
> expectReceiveAt| string| 預計到帳時間，毫秒級 Unix 時間戳  
> minPurchaseAmount| string| 最小單筆申購金額  
> remainingAmount| string| 剩餘可用額度  
> orderPrecisionDigital| int| 訂單金額精度  
  
### 請求示例
    
    
    GET /v5/earn/advance/product?category=SmartLeverage&coin=BTC HTTP/1.1  
    Host: api-testnet.bybit.com  
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "",  
        "result": {  
            "category": "SmartLeverage",  
            "list": [  
                {  
                    "category": "SmartLeverage",  
                    "productId": "13015",  
                    "investCoin": "USDT",  
                    "underlyingAsset": "BTC",  
                    "direction": "Short",  
                    "leverage": "10",  
                    "duration": "7d",  
                    "expectReceiveAt": "1775635800000",  
                    "subscribeStartAt": "1775001600000",  
                    "subscribeEndAt": "1775087999000",  
                    "settlementTime": "1775635200000",  
                    "minPurchaseAmount": "10",  
                    "remainingAmount": "9994748366.907",  
                    "orderPrecisionDigital": 4  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1775001977686  
    }