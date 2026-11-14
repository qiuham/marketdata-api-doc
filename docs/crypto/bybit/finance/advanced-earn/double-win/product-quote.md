---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/finance/advanced-earn/double-win/product-quote
api_type: REST
updated_at: 2026-11-13 19:22:49.623141
---

# Get Fixed Product Quote

info

Does not need authentication

note

This endpoint applies to **fixed price range products** (`isRfqProduct=false`) only. For RFQ products, use [Get Custom Product Quote](/docs/v5/finance/advanced-earn/double-win/leverage) to obtain a quote.

You can also subscribe to the WebSocket topic [`earn.doublewin.offers`](/docs/v5/finance/advanced-earn/websocket/double-win-offer) to receive real-time quote updates.

### HTTP Request

GET`/v5/earn/advance/product-extra-info`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
category| **true**|  string| Product category. `DoubleWin`  
productId| **true**|  string| Product ID  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
category| string| `DoubleWin`  
productId| string| Product ID  
leverage| string| Current maximum leverage multiplier. Empty if no active quote  
expireTime| string| Quote expiry time, Unix timestamp in ms. The quote must be used before this time. Empty if no active quote  
maxInvestmentAmount| string| Maximum single order amount at current quote. Empty if no active quote  
currentPrice| string| Current index price of the underlying asset. Use as `initialPrice` when placing an order  
  
### Request Example
    
    
    GET /v5/earn/advance/product-extra-info?category=DoubleWin&productId=20001 HTTP/1.1  
    Host: api-testnet.bybit.com  
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "",  
        "result": {  
            "productId": "14084",  
            "leverage": "9.30452991038687184855947115",  
            "expireTime": "1775102611946",  
            "maxInvestmentAmount": "1000",  
            "currentPrice": "66628.76",  
            "category": "DoubleWin"  
        },  
        "retExtInfo": {},  
        "time": 1775102648543  
    }

---

# 查詢固定產品報價

信息

無需身份驗證

備註

僅接口適用於**固定區間產品** （`isRfqProduct=false`）。如需 RFQ 產品的報價，請使用[查詢自選區間產品報價](/docs/zh-TW/v5/finance/advanced-earn/double-win/leverage)。

您也可以訂閱 WebSocket 頻道 [`earn.doublewin.offers`](/docs/zh-TW/v5/finance/advanced-earn/websocket/double-win-offer) 以接收即時報價推送。

### HTTP 請求

GET`/v5/earn/advance/product-extra-info`

### 請求參數

參數| 必填| 類型| 說明  
---|---|---|---  
category| **true**|  string| 產品類別，`DoubleWin`  
productId| **true**|  string| 產品 ID  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
category| string| `DoubleWin`  
productId| string| 產品 ID  
leverage| string| 當前最大槓桿倍數。若無有效報價則為空  
expireTime| string| 報價到期時間，毫秒級 Unix 時間戳。需在此時間前完成下單。若無有效報價則為空  
maxInvestmentAmount| string| 當前報價下的最大單筆下單金額。若無有效報價則為空  
currentPrice| string| 標的資產當前指數價格，可作為下單時 `initialPrice` 的參考  
  
### 請求示例
    
    
    GET /v5/earn/advance/product-extra-info?category=DoubleWin&productId=20001 HTTP/1.1  
    Host: api-testnet.bybit.com  
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "",  
        "result": {  
            "productId": "14084",  
            "leverage": "9.30452991038687184855947115",  
            "expireTime": "1775102611946",  
            "maxInvestmentAmount": "1000",  
            "currentPrice": "66628.76",  
            "category": "DoubleWin"  
        },  
        "retExtInfo": {},  
        "time": 1775102648543  
    }