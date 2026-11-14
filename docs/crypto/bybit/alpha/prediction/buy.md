---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/alpha/prediction/buy
api_type: REST
updated_at: 2026-11-13 19:21:07.703778
---

# Execute Buy

Execute a buy order for prediction outcome tokens, paying USDC to receive outcome token shares.

info

  * Must call [Get Engine Status](/docs/v5/alpha/prediction/engine-status) first to verify the engine is available
  * Must call [Get Event Detail](/docs/v5/alpha/prediction/event-detail) to obtain `tokenId` and verify the market is open
  * Must call [Get Order Estimate](/docs/v5/alpha/prediction/order-estimate) to preview the order
  * Must display the estimate to the user and obtain explicit confirmation before calling this endpoint
  * Phase 1 supports `orderType=1` (FOK) only — orders that cannot be fully filled are cancelled
  * A `200` response is an acknowledgment only — use [Get Order List](/docs/v5/alpha/prediction/order-list) to check the final fill status



### HTTP Request

POST`/v5/alpha/prediction/buy`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
tokenId| **true**|  string| Outcome token ID to buy (from [Get Event Detail](/docs/v5/alpha/prediction/event-detail))  
amount| **true**|  string| USDC amount to invest (positive decimal as string)  
payTokenCode| **true**|  string| Payment token code. Phase 1 fixed to `USDC`  
orderType| **true**|  integer| Order type. Refer to [predictionOrderType](/docs/v5/enum#predictionordertype-prediction-market--order-type). Phase 1: `1` (FOK) only  
slippage| **true**|  string| Maximum acceptable price slippage as decimal. `0.05` = 5% tolerance  
eventId| **true**|  string| Event ID associated with the token  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
orderNo| string| Order number. Use with [Get Order List](/docs/v5/alpha/prediction/order-list) to check fill status  
  
### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    POST /v5/alpha/prediction/buy HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1704067200000  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "tokenId": "token_yes_123",  
        "amount": "100",  
        "payTokenCode": "USDC",  
        "orderType": 1,  
        "slippage": "0.05",  
        "eventId": "event_123"  
    }  
    
    
    
      
    
    
    
      
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "orderNo": "ord_buy_20240101_001"  
        },  
        "retExtInfo": {},  
        "time": 1704067200000  
    }

---

# 執行買入

執行預測市場結果代幣的買入委托，支付 USDC 獲取結果代幣份額。

信息

  * 必須先調用 [獲取撮合引擎狀態](/docs/zh-TW/v5/alpha/prediction/engine-status) 確認引擎可用
  * 必須先調用 [獲取賽事詳情](/docs/zh-TW/v5/alpha/prediction/event-detail) 獲取 `tokenId` 並確認市場開放
  * 必須先調用 [獲取委托預估](/docs/zh-TW/v5/alpha/prediction/order-estimate) 預覽委托結果
  * 必須向用戶展示預估結果並取得明確確認後，方可調用本接口
  * 第一階段僅支持 `orderType=1`（FOK）——無法完全成交的委托將被取消
  * `200` 響應僅表示委托已受理，請調用 [獲取委托記錄](/docs/zh-TW/v5/alpha/prediction/order-list) 查詢最終成交狀態



### HTTP 請求

POST`/v5/alpha/prediction/buy`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
tokenId| **true**|  string| 要買入的結果代幣 ID（從 [獲取賽事詳情](/docs/zh-TW/v5/alpha/prediction/event-detail) 獲取）  
amount| **true**|  string| 投入的 USDC 金額（正數字符串）  
payTokenCode| **true**|  string| 支付代幣代碼，第一階段固定為 `USDC`  
orderType| **true**|  integer| 委托類型。參考 [predictionOrderType](/docs/zh-TW/v5/enum#predictionordertype-prediction-market--order-type)。第一階段：`1`（FOK）  
slippage| **true**|  string| 最大可接受滑點（小數）。`0.05` = 5% 容忍度  
eventId| **true**|  string| 代幣對應的賽事 ID  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
orderNo| string| 委托號。請調用 [獲取委托記錄](/docs/zh-TW/v5/alpha/prediction/order-list) 查詢成交狀態  
  
### 請求示例

  * HTTP
  * Python
  * Node.js


    
    
    POST /v5/alpha/prediction/buy HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1704067200000  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "tokenId": "token_yes_123",  
        "amount": "100",  
        "payTokenCode": "USDC",  
        "orderType": 1,  
        "slippage": "0.05",  
        "eventId": "event_123"  
    }  
    
    
    
      
    
    
    
      
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "orderNo": "ord_buy_20240101_001"  
        },  
        "retExtInfo": {},  
        "time": 1704067200000  
    }