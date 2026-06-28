---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/finance/advanced-earn/discount-buy/product-info
api_type: REST
updated_at: 2026-05-27 19:16:38.040778
---

# Get Product Quote

info

Does not need authentication

note

  * You **must** call this endpoint before placing an order to obtain the latest pricing parameters. Pass the returned values as-is into the order request.
  * You can also subscribe to the WebSocket topic [`earn.discountbuy.offers`](/docs/v5/finance/advanced-earn/websocket/discount-buy-offer) to receive real-time quote updates.



### HTTP Request

GET`/v5/earn/advance/product-extra-info`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
category| **true**|  string| Product category. `DiscountBuy`  
productId| false| string| Product ID. Returns quotes for all products if not provided  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
offers| array| Object  
> productId| string| Product ID  
> currentPrice| string| Current index price of the underlying asset  
> purchasePrice| string| Anchor buy price  
> knockoutPrice| string| Knockout price  
> knockoutCouponE8| string| Annualized interest rate in e8 precision. Actual rate = `knockoutCouponE8` / 1e8  
> maxInvestmentAmount| string| Maximum investment amount for this quote  
> instUid| string| Market maker institution ID. **Must be passed as-is when placing an order**  
> expiredAt| string| Quote expiry time, Unix timestamp in ms. `0` means no expiry is set by the institution  
  
### Request Example
    
    
    GET /v5/earn/advance/product-extra-info?category=DiscountBuy&productId=7037 HTTP/1.1  
    Host: api-testnet.bybit.com  
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "",  
        "result": {  
            "offers": [  
                {  
                    "productId": "7037",  
                    "currentPrice": "74514.26",  
                    "purchasePrice": "74014",  
                    "knockoutPrice": "76000",  
                    "knockoutCouponE8": "1000000",  
                    "maxInvestmentAmount": "100000",  
                    "instUid": "100307526",  
                    "expiredAt": "1776153608188",  
                    "category": "DiscountBuy"  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1776153594375  
    }

---

# 查詢產品報價

信息

無需身份驗證

備註

  * 下單前**必須** 先調用此接口取得最新報價參數，並將返回值原樣傳入下單請求。
  * 您也可以訂閱 WebSocket 頻道 [`earn.discountbuy.offers`](/docs/zh-TW/v5/finance/advanced-earn/websocket/discount-buy-offer)，接收即時報價推送。



### HTTP 請求

GET`/v5/earn/advance/product-extra-info`

### 請求參數

參數| 必填| 類型| 說明  
---|---|---|---  
category| **true**|  string| 產品類別，`DiscountBuy`  
productId| false| string| 產品 ID。不傳則返回所有產品報價  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
offers| array| 列表  
> productId| string| 產品 ID  
> currentPrice| string| 標的資產當前市場價格  
> purchasePrice| string| 錨定買入價。行權結算時，標的資產將以此價格買入  
> knockoutPrice| string| 敲出價。結算價 >= `knockoutPrice` 時敲出，返還 USDT 本金 + 利息  
> knockoutCouponE8| string| 年化息率（e8 精度），實際利率 = `knockoutCouponE8` / 1e8，敲出時按此計算利息  
> maxInvestmentAmount| string| 當前報價下的最大可投金額  
> instUid| string| 做市商機構 ID，**下單時必須原樣傳入**  
> expiredAt| string| 報價到期時間，毫秒級 Unix 時間戳。`0` 表示機構未設定有效期  
  
### 請求示例
    
    
    GET /v5/earn/advance/product-extra-info?category=DiscountBuy&productId=7037 HTTP/1.1  
    Host: api-testnet.bybit.com  
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "",  
        "result": {  
            "offers": [  
                {  
                    "productId": "7037",  
                    "currentPrice": "74514.26",  
                    "purchasePrice": "74014",  
                    "knockoutPrice": "76000",  
                    "knockoutCouponE8": "1000000",  
                    "maxInvestmentAmount": "100000",  
                    "instUid": "100307526",  
                    "expiredAt": "1776153608188",  
                    "category": "DiscountBuy"  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1776153594375  
    }