---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/finance/advanced-earn/double-win/leverage
api_type: REST
updated_at: 2026-06-30 19:25:41.145233
---

# Get Custom Product Quote

info

  * Requires Earn permission on the API key.
  * This endpoint is **only for RFQ products** (`isRfqProduct=true`). For fixed price range products, use [Get Fixed Product Quote](/docs/v5/finance/advanced-earn/double-win/product-quote) or subscribe to the WebSocket topic [`earn.doublewin.offers`](/docs/v5/finance/advanced-earn/websocket/double-win-offer).



tip

**How to use RFQ custom price range:**

  1. Call [Get Product Info](/docs/v5/finance/advanced-earn/double-win/product-info) to obtain `priceTickSize`, `minDeviationRatio`, and `maxDeviationRatio`.
  2. Choose a `lowerPrice` and `upperPrice` within the allowed deviation range, both must be multiples of `priceTickSize`.
  3. Call this endpoint with the chosen prices to get a `leverage` quote and its `expireTime`.
  4. Place the order before `expireTime` using the returned `leverage`.



### HTTP Request

GET`/v5/earn/advance/double-win-leverage`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
productId| **true**|  string| Product ID  
initialPrice| **true**|  string| Current index price of the underlying asset  
lowerPrice| **true**|  string| Custom lower bound of price range. Must be a multiple of `priceTickSize` and less than `initialPrice`  
upperPrice| **true**|  string| Custom upper bound of price range. Must be a multiple of `priceTickSize` and greater than `initialPrice`  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
productId| string| Product ID  
initialPrice| string| Echo back of the submitted `initialPrice`  
lowerPrice| string| Echo back of the submitted `lowerPrice`  
upperPrice| string| Echo back of the submitted `upperPrice`  
leverage| string| Leverage multiplier for the given price range, e.g. `"3.2"`  
expireTime| string| Quote expiry time, Unix timestamp in ms. The order must be placed before this time  
maxInvestmentAmount| string| Maximum single order amount for this quote  
  
### Request Example
    
    
    GET /v5/earn/advance/double-win-leverage?productId=14092&initialPrice=66333.94&lowerPrice=63000&upperPrice=70000 HTTP/1.1  
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
            "productId": "14092",  
            "initialPrice": "66333.94",  
            "lowerPrice": "63000",  
            "upperPrice": "70000",  
            "leverage": "241.15",  
            "expireTime": "1775106748000",  
            "maxInvestmentAmount": "10000"  
        },  
        "retExtInfo": {},  
        "time": 1775106718961  
    }

---

# 查詢自選區間產品報價

信息

  * API 金鑰需要具備 Earn（理財）權限。
  * 此接口**僅適用於 RFQ 產品** （`isRfqProduct=true`）。固定區間產品請使用[查詢固定產品報價](/docs/zh-TW/v5/finance/advanced-earn/double-win/product-quote)，或訂閱 WebSocket 頻道 [`earn.doublewin.offers`](/docs/zh-TW/v5/finance/advanced-earn/websocket/double-win-offer)。



提示

**RFQ 自選區間使用流程：**

  1. 通過[查詢產品資訊](/docs/zh-TW/v5/finance/advanced-earn/double-win/product-info)獲取 `priceTickSize`、`minDeviationRatio` 和 `maxDeviationRatio`。
  2. 在允許的偏離範圍內選擇 `lowerPrice` 和 `upperPrice`，兩者均須為 `priceTickSize` 的整數倍。
  3. 攜帶所選價格調用本接口，獲取 `leverage` 報價及其 `expireTime`。
  4. 在 `expireTime` 前使用返回的 `leverage` 完成下單。



### HTTP 請求

GET`/v5/earn/advance/double-win-leverage`

### 請求參數

參數| 必填| 類型| 說明  
---|---|---|---  
productId| **true**|  string| 產品 ID  
initialPrice| **true**|  string| 標的資產當前指數價格  
lowerPrice| **true**|  string| 自選價格區間下限，須為 `priceTickSize` 的整數倍，且小於 `initialPrice`  
upperPrice| **true**|  string| 自選價格區間上限，須為 `priceTickSize` 的整數倍，且大於 `initialPrice`  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
productId| string| 產品 ID  
initialPrice| string| 請求中傳入的 `initialPrice`（原值返回）  
lowerPrice| string| 請求中傳入的 `lowerPrice`（原值返回）  
upperPrice| string| 請求中傳入的 `upperPrice`（原值返回）  
leverage| string| 對應所選價格區間的槓桿倍數，例如：`"241.15"`  
expireTime| string| 報價到期時間，毫秒級 Unix 時間戳，須在此時間前完成下單  
maxInvestmentAmount| string| 本次報價下的最大單筆下單金額  
  
### 請求示例
    
    
    GET /v5/earn/advance/double-win-leverage?productId=14092&initialPrice=66333.94&lowerPrice=63000&upperPrice=70000 HTTP/1.1  
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
            "productId": "14092",  
            "initialPrice": "66333.94",  
            "lowerPrice": "63000",  
            "upperPrice": "70000",  
            "leverage": "241.15",  
            "expireTime": "1775106748000",  
            "maxInvestmentAmount": "10000"  
        },  
        "retExtInfo": {},  
        "time": 1775106718961  
    }