---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/finance/advanced-earn/websocket/double-win-offer
api_type: WebSocket
updated_at: 2026-05-27 19:17:12.324668
---

# Double Win Offers

### WebSocket public URL

  * **Mainnet:**  
Earn: `wss://stream.bybit.com/v5/public/fp`  


  * **Testnet:**  
Earn: `wss://stream-testnet.bybit.com/v5/public/fp`  





info

  * Subscribing to this topic does not require authentication.
  * This topic pushes **fixed price range products** (`isRfqProduct=false`) only. For RFQ products, use [Get Custom Product Quote](/docs/v5/finance/advanced-earn/double-win/leverage) to obtain a quote on demand.
  * **Recommended usage** : call [Get Fixed Product Quote](/docs/v5/finance/advanced-earn/double-win/product-quote) on initialization to get the current quote, then subscribe to this topic to maintain a live view. If the WebSocket disconnects, call [Get Fixed Product Quote](/docs/v5/finance/advanced-earn/double-win/product-quote) to refresh before re-subscribing.



### Topic: `earn.doublewin.offers`

### Response Parameters

Parameter| Type| Comments  
---|---|---  
topic| string| Topic name. `earn.doublewin.offers`  
data| array| Object  
> p| string| Product ID  
> c| string| Current index price of the underlying asset  
> l| string| Current maximum leverage multiplier  
> m| string| Maximum single order amount at current quote  
> e| string| Quote expiry time, Unix timestamp in ms  
  
### Push Example
    
    
    {  
        "topic": "earn.doublewin.offers",  
        "data": [  
            {  
                "p": "14082",  
                "c": "2050.99",  
                "l": "37.78",  
                "m": "1000",  
                "e": "1775111431407"  
            },  
            {  
                "p": "14083",  
                "c": "2050.99",  
                "l": "75.57",  
                "m": "700",  
                "e": "1775111431552"  
            },  
            {  
                "p": "14088",  
                "c": "66647.87",  
                "l": "23.25",  
                "m": "500",  
                "e": "1775111432115"  
            },  
            {  
                "p": "14089",  
                "c": "66647.87",  
                "l": "23.25",  
                "m": "1000",  
                "e": "1775111432115"  
            }  
        ]  
    }

---

# 漲跌雙贏報價

### WebSocket 公共頻道網址

  * **主網：**  
Earn: `wss://stream.bybit.com/v5/public/fp`  


  * **測試網：**  
Earn: `wss://stream-testnet.bybit.com/v5/public/fp`  





信息

  * 訂閱此頻道無需身份驗證。
  * 本頻道**僅推送固定區間產品** （`isRfqProduct=false`）。RFQ 產品需調用[查詢自選區間產品報價](/docs/zh-TW/v5/finance/advanced-earn/double-win/leverage)進行主動詢價。
  * **推薦使用方式** ：初始化時調用[查詢固定產品報價](/docs/zh-TW/v5/finance/advanced-earn/double-win/product-quote)獲取當前報價，再訂閱本頻道保持即時更新。WebSocket 斷線後，請先調用[查詢固定產品報價](/docs/zh-TW/v5/finance/advanced-earn/double-win/product-quote)重新整理，再重新訂閱。



### 頻道：`earn.doublewin.offers`

### 響應參數

參數| 類型| 說明  
---|---|---  
topic| string| 頻道名稱，`earn.doublewin.offers`  
data| array| 列表  
> p| string| 產品 ID  
> c| string| 標的資產當前指數價格  
> l| string| 當前最大槓桿倍數  
> m| string| 當前報價下的最大單筆下單金額  
> e| string| 報價到期時間，毫秒級 Unix 時間戳  
  
### 推送示例
    
    
    {  
        "topic": "earn.doublewin.offers",  
        "data": [  
            {  
                "p": "14082",  
                "c": "2050.99",  
                "l": "37.78",  
                "m": "1000",  
                "e": "1775111431407"  
            },  
            {  
                "p": "14083",  
                "c": "2050.99",  
                "l": "75.57",  
                "m": "700",  
                "e": "1775111431552"  
            },  
            {  
                "p": "14088",  
                "c": "66647.87",  
                "l": "23.25",  
                "m": "500",  
                "e": "1775111432115"  
            },  
            {  
                "p": "14089",  
                "c": "66647.87",  
                "l": "23.25",  
                "m": "1000",  
                "e": "1775111432115"  
            }  
        ]  
    }