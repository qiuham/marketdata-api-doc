---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/alpha/prediction/order-list
api_type: REST
updated_at: 2026-11-13 19:21:10.985026
---

# Get Order List

Query the authenticated user's prediction market order history. Use this after placing a buy or sell order to check the final execution status. FOK orders will show as `FILLED` or `CANCELLED`.

### HTTP Request

POST`/v5/alpha/prediction/order-list`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
status| false| integer| Filter by order status. Refer to [predictionOrderStatus](/docs/v5/enum#predictionorderstatus-prediction-market--order-status)  
tokenId| false| string| Filter by outcome token ID  
eventId| false| string| Filter by event ID  
side| false| integer| Filter by trade direction. Refer to [predictionSide](/docs/v5/enum#predictionside-prediction-market--trade-direction)  
days| false| integer| Look back N days. Max: `90`  
limit| false| integer| Number of records per page  
pageIndex| false| integer| Page number starting from `1`  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
orders| array| Order records  
> orderNo| string| Order number  
> tokenId| string| Outcome token ID  
> eventId| string| Event ID  
> side| integer| Trade direction. Refer to [predictionSide](/docs/v5/enum#predictionside-prediction-market--trade-direction)  
> orderType| integer| Order type. Refer to [predictionOrderType](/docs/v5/enum#predictionordertype-prediction-market--order-type)  
> orderAmount| string| BUY: USDC invested. SELL: shares sold  
> filledSize| string| Filled shares (BUY) or shares sold (SELL)  
> filledPrice| string| Average execution price  
> totalFee| string| Total platform fee charged (USDC)  
> status| integer| Order status. Refer to [predictionOrderStatus](/docs/v5/enum#predictionorderstatus-prediction-market--order-status)  
> createdAt| integer| Order creation timestamp (UTC milliseconds)  
> updatedAt| integer| Last update timestamp (UTC milliseconds)  
total| integer| Total matching records  
pageIndex| integer| Current page number  
  
### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    POST /v5/alpha/prediction/order-list HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1704067200000  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "limit": 20,  
        "pageIndex": 1,  
        "days": 7  
    }  
    
    
    
      
    
    
    
      
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "orders": [  
                {  
                    "orderNo": "ord_buy_20240101_001",  
                    "tokenId": "token_yes_123",  
                    "eventId": "event_123",  
                    "side": 1,  
                    "orderType": 1,  
                    "orderAmount": "100",  
                    "filledSize": "153.84",  
                    "filledPrice": "0.65",  
                    "totalFee": "1.00",  
                    "status": 2,  
                    "createdAt": 1704067200000,  
                    "updatedAt": 1704067205000  
                }  
            ],  
            "total": 1,  
            "pageIndex": 1  
        },  
        "retExtInfo": {},  
        "time": 1704067200000  
    }

---

# 獲取委托記錄

查詢已登錄用戶的預測市場委托歷史。在下達買入或賣出委托後，可調用此接口查詢最終成交狀態。FOK 委托將顯示為 `FILLED` 或 `CANCELLED`。

### HTTP 請求

POST`/v5/alpha/prediction/order-list`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
status| false| integer| 按委托狀態篩選。參考 [predictionOrderStatus](/docs/zh-TW/v5/enum#predictionorderstatus-prediction-market--order-status)  
tokenId| false| string| 按結果代幣 ID 篩選  
eventId| false| string| 按賽事 ID 篩選  
side| false| integer| 按交易方向篩選。參考 [predictionSide](/docs/zh-TW/v5/enum#predictionside-prediction-market--trade-direction)  
days| false| integer| 回溯天數，最大 `90`  
limit| false| integer| 每頁記錄數  
pageIndex| false| integer| 頁碼，從 `1` 開始  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
orders| array| 委托記錄  
> orderNo| string| 委托號  
> tokenId| string| 結果代幣 ID  
> eventId| string| 賽事 ID  
> side| integer| 交易方向。參考 [predictionSide](/docs/zh-TW/v5/enum#predictionside-prediction-market--trade-direction)  
> orderType| integer| 委托類型。參考 [predictionOrderType](/docs/zh-TW/v5/enum#predictionordertype-prediction-market--order-type)  
> orderAmount| string| 買入：投入的 USDC；賣出：賣出的份額  
> filledSize| string| 已成交份額（買入）或已賣出份額（賣出）  
> filledPrice| string| 平均成交價格  
> totalFee| string| 總手續費（USDC）  
> status| integer| 委托狀態。參考 [predictionOrderStatus](/docs/zh-TW/v5/enum#predictionorderstatus-prediction-market--order-status)  
> createdAt| integer| 委托創建時間戳（UTC 毫秒）  
> updatedAt| integer| 最後更新時間戳（UTC 毫秒）  
total| integer| 符合條件的總記錄數  
pageIndex| integer| 當前頁碼  
  
### 請求示例

  * HTTP
  * Python
  * Node.js


    
    
    POST /v5/alpha/prediction/order-list HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1704067200000  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "limit": 20,  
        "pageIndex": 1,  
        "days": 7  
    }  
    
    
    
      
    
    
    
      
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "orders": [  
                {  
                    "orderNo": "ord_buy_20240101_001",  
                    "tokenId": "token_yes_123",  
                    "eventId": "event_123",  
                    "side": 1,  
                    "orderType": 1,  
                    "orderAmount": "100",  
                    "filledSize": "153.84",  
                    "filledPrice": "0.65",  
                    "totalFee": "1.00",  
                    "status": 2,  
                    "createdAt": 1704067200000,  
                    "updatedAt": 1704067205000  
                }  
            ],  
            "total": 1,  
            "pageIndex": 1  
        },  
        "retExtInfo": {},  
        "time": 1704067200000  
    }