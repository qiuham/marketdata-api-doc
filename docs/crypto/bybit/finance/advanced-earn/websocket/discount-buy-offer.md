---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/finance/advanced-earn/websocket/discount-buy-offer
api_type: WebSocket
updated_at: 2026-11-13 19:23:02.687271
---

# Discount Buy Offers

### WebSocket public URL

  * **Mainnet:**  
Earn: `wss://stream.bybit.com/v5/public/fp`  


  * **Testnet:**  
Earn: `wss://stream-testnet.bybit.com/v5/public/fp`  





info

  * Subscribing to this topic does not require authentication.
  * **Recommended usage** : call [Get Product Quote](/docs/v5/finance/advanced-earn/discount-buy/product-quote) on initialization to get the current quote, then subscribe to this topic to maintain a live view. If the WebSocket disconnects, call [Get Product Quote](/docs/v5/finance/advanced-earn/discount-buy/product-quote) to refresh before re-subscribing.



### Topic: `earn.discountbuy.offers`

### Response Parameters

Parameter| Type| Comments  
---|---|---  
topic| string| Topic name. `earn.discountbuy.offers`  
data| array| Object  
> p| string| Product ID  
> c| string| Current index price of the underlying asset  
> b| string| Anchor buy price  
> k| string| Knockout price  
> e| string| Annualized interest rate in e8 precision. Actual rate = `knockoutCouponE8` / 1e8  
> m| string| Maximum investment amount for this quote  
> i| string| Market maker institution ID. Must be passed as-is when placing an order  
> x| string| Quote expiry time, Unix timestamp in ms. `0` means no expiry is set by the institution  
  
### Push Example
    
    
    {  
        "topic": "earn.discountbuy.offers",  
        "data": [  
            {  
                "p": "12723",  
                "c": "74551.1",  
                "b": "73847",  
                "k": "75300",  
                "e": "10000000",  
                "m": "950000",  
                "i": "103489231",  
                "x": "1776154870336"  
            }  
        ]  
    }

---

# 折價買幣報價

### WebSocket 公共頻道網址

  * **主網：**  
Earn: `wss://stream.bybit.com/v5/public/fp`  


  * **測試網：**  
Earn: `wss://stream-testnet.bybit.com/v5/public/fp`  





信息

  * 訂閱此頻道無需身份驗證。
  * **建議使用方式** ：初始化時先調用[查詢產品報價](/docs/zh-TW/v5/finance/advanced-earn/discount-buy/product-quote)取得當前報價，再訂閱此頻道維持即時報價視圖。若 WebSocket 連線中斷，請重新調用[查詢產品報價](/docs/zh-TW/v5/finance/advanced-earn/discount-buy/product-quote)更新數據後再訂閱。



### 頻道：`earn.discountbuy.offers`

### 響應參數

參數| 類型| 說明  
---|---|---  
topic| string| 頻道名稱，`earn.discountbuy.offers`  
data| array| 列表  
> p| string| 產品 ID  
> c| string| 標的資產當前市場價格  
> b| string| 錨定買入價  
> k| string| 敲出價  
> e| string| 年化息率（e8 精度），實際利率 = `knockoutCouponE8` / 1e8  
> m| string| 當前報價下的最大可投金額  
> i| string| 做市商機構 ID，下單時必須原樣傳入  
> x| string| 報價到期時間，毫秒級 Unix 時間戳。`0` 表示機構未設定有效期  
  
### 推送示例
    
    
    {  
        "topic": "earn.discountbuy.offers",  
        "data": [  
            {  
                "p": "12723",  
                "c": "74551.1",  
                "b": "73847",  
                "k": "75300",  
                "e": "10000000",  
                "m": "950000",  
                "i": "103489231",  
                "x": "1776154870336"  
            }  
        ]  
    }