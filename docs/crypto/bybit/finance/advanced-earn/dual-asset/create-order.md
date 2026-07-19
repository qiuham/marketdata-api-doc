---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/finance/advanced-earn/dual-asset/create-order
api_type: REST
updated_at: 2026-07-19 18:48:19.144752
---

# Get Product Info

info

Does not need authentication. **Up to 50 requests** per second per IP .

[Bybit Dual Asset FAQ](https://www.bybit.com/en/help-center/article/Dual-Asset-Mining-FAQ)

### HTTP Request

GET `/v5/earn/advance/product`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
[category](/docs/v5/enum#advanced-earn-category)| **true**|  string| Product category,`DualAssets`  
coin| false| string| Coin name, uppercase only  
duration| false| string| Product duration, eg:8h, 1d, 3d, 6d, 12d  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
[category](/docs/v5/enum#advanced-earn-category)| string| `DualAssets`  
list| array| Object  
> [category](/docs/v5/enum#advanced-earn-category)| string| `DualAssets`  
> productId| string| Product ID  
> baseCoin| string| Base Coin  
> quoteCoin| string| Quote Coin  
> expectReceiveAt| string| Expected time to receive the transfer, Unix timestamp in milliseconds  
> duration| string| Product duration, eg:8h, 1d, 3d  
> [status](/docs/v5/enum#advanced-earn-product-status)| string| `Available`,`NotAvailable`  
> isVipProduct| boolean| Whether it is a VIP product  
> subscribeStartAt| string| Subscription start time, Unix timestamp in ms  
> subscribeEndAt| string| Subscription end time, Unix timestamp in ms  
> applyStartAt| string| Interest accrual start time, Unix timestamp in ms  
> settlementTime| string| Interest accrual end time, Unix timestamp in ms  
> minPurchaseQuoteAmount| string| Minimum purchase amount in quote currency  
> minPurchaseBaseAmount| string| Minimum purchase amount in base currency  
> remainingAmountQuote| string| Remaining quota for Buy Low direction  
> remainingAmountBase| string| Remaining quota for Sell High direction  
> orderPrecisionDigitalQuote| int| Precision for Buy Low direction  
> orderPrecisionDigitalBase| int| Precision for Sell High direction  
  
### Request Example

  * HTTP


    
    
    GET /v5/earn/advance/product?category=DualAssets&coin=XRP HTTP/1.1  
    Host: api-testnet.bybit.com  
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "",  
        "result": {  
            "category": "DualAssets",  
            "list": [  
                {  
                    "category": "DualAssets",  
                    "productId": "36340",  
                    "baseCoin": "XRP",  
                    "quoteCoin": "USDT",  
                    "expectReceiveAt": "1773908399000",  
                    "duration": "1d",  
                    "status": "Available",  
                    "isVipProduct": false,  
                    "subscribeStartAt": "1773734400000",  
                    "subscribeEndAt": "1773820799000",  
                    "applyStartAt": "1773734400000",  
                    "settlementTime": "1773907199000",  
                    "minPurchaseQuoteAmount": "10",  
                    "minPurchaseBaseAmount": "10",  
                    "remainingAmountQuote": "1000000",  
                    "remainingAmountBase": "10000",  
                    "orderPrecisionDigitalQuote": 4,  
                    "orderPrecisionDigitalBase": 2  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1773814359231  
    }

---

# 查詢產品資訊

信息

無需身份驗證。每個 IP 每秒**最多 50 次請求** 。

[Bybit 雙幣投資常見問題解答](https://www.bybit.com/en/help-center/article/Dual-Asset-Mining-FAQ)

### HTTP 請求

GET `/v5/earn/advance/product`

### 請求參數

參數| 必填| 類型| 說明  
---|---|---|---  
[category](/docs/zh-TW/v5/enum#advanced-earn-category)| **true**|  string| 產品類別，`DualAssets`  
coin| false| string| 幣種名稱，僅限大寫  
duration| false| string| 產品期限，例如：8h, 1d, 3d, 6d, 12d  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
[category](/docs/zh-TW/v5/enum#advanced-earn-category)| string| `DualAssets`  
list| array| 列表  
> [category](/docs/zh-TW/v5/enum#advanced-earn-category)| string| `DualAssets`  
> productId| string| 產品 ID  
> baseCoin| string| 基礎幣種 (Base Coin)  
> quoteCoin| string| 計價幣種 (Quote Coin)  
> expectReceiveAt| string| 預計到帳時間，毫秒級 Unix 時間戳  
> duration| string| 產品期限，例如：8h, 1d, 3d  
> [status](/docs/zh-TW/v5/enum#advanced-earn-product-status)| string| `Available` (可用), `NotAvailable` (不可用)  
> isVipProduct| boolean| 是否為 VIP 產品  
> subscribeStartAt| string| 申購開始時間，毫秒級 Unix 時間戳  
> subscribeEndAt| string| 申購結束時間，毫秒級 Unix 時間戳  
> applyStartAt| string| 計息開始時間，毫秒級 Unix 時間戳  
> settlementTime| string| 計息結束時間（結算時間），毫秒級 Unix 時間戳  
> minPurchaseQuoteAmount| string| 計價幣種的最小申購金額  
> minPurchaseBaseAmount| string| 基礎幣種的最小申購金額  
> remainingAmountQuote| string| 低買 (Buy Low) 方向的剩餘額度  
> remainingAmountBase| string| 高賣 (Sell High) 方向的剩餘額度  
> orderPrecisionDigitalQuote| int| 低買方向的訂單精度  
> orderPrecisionDigitalBase| int| 高賣方向的訂單精度  
  
### 請求示例

  * HTTP


    
    
    GET /v5/earn/advance/product?category=DualAssets&coin=XRP HTTP/1.1  
    Host: api-testnet.bybit.com  
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "",  
        "result": {  
            "category": "DualAssets",  
            "list": [  
                {  
                    "category": "DualAssets",  
                    "productId": "36340",  
                    "baseCoin": "XRP",  
                    "quoteCoin": "USDT",  
                    "expectReceiveAt": "1773908399000",  
                    "duration": "1d",  
                    "status": "Available",  
                    "isVipProduct": false,  
                    "subscribeStartAt": "1773734400000",  
                    "subscribeEndAt": "1773820799000",  
                    "applyStartAt": "1773734400000",  
                    "settlementTime": "1773907199000",  
                    "minPurchaseQuoteAmount": "10",  
                    "minPurchaseBaseAmount": "10",  
                    "remainingAmountQuote": "1000000",  
                    "remainingAmountBase": "10000",  
                    "orderPrecisionDigitalQuote": 4,  
                    "orderPrecisionDigitalBase": 2  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1773814359231  
    }