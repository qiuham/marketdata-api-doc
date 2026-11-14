---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/alpha/prediction/sell
api_type: REST
updated_at: 2026-11-13 19:21:14.298352
---

# Execute Sell

Execute a sell order for prediction outcome token shares, exchanging shares for USDC.

info

  * Must call [Get Engine Status](/docs/v5/alpha/prediction/engine-status) first to verify the engine is available
  * Must call [Get Position List](/docs/v5/alpha/prediction/position-list) to confirm the position exists and check available `shares`
  * Must call [Get Order Estimate](/docs/v5/alpha/prediction/order-estimate) to preview the sell order
  * Must display the estimate to the user and obtain explicit confirmation before calling this endpoint
  * Phase 1 supports `orderType=1` (FOK) only — orders that cannot be fully filled are cancelled
  * `size` is in shares, not USDC
  * A `200` response is an acknowledgment only — use [Get Order List](/docs/v5/alpha/prediction/order-list) to check the final fill status



### HTTP Request

POST`/v5/alpha/prediction/sell`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
tokenId| **true**|  string| Outcome token ID to sell (from [Get Position List](/docs/v5/alpha/prediction/position-list))  
size| **true**|  string| Number of shares to sell (positive decimal as string)  
orderType| **true**|  integer| Order type. Refer to [predictionOrderType](/docs/v5/enum#predictionordertype-prediction-market--order-type). Phase 1: `1` (FOK) only  
slippage| **true**|  string| Maximum acceptable price slippage as decimal. `0.05` = 5% tolerance  
eventId| **true**|  string| Event ID associated with the token  
toTokenCode| false| string| Destination token code. Phase 1 fixed to `USDC`  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
orderNo| string| Order number. Use with [Get Order List](/docs/v5/alpha/prediction/order-list) to check fill status  
  
### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    POST /v5/alpha/prediction/sell HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1704067200000  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "tokenId": "token_yes_123",  
        "size": "50",  
        "orderType": 1,  
        "slippage": "0.05",  
        "eventId": "event_123",  
        "toTokenCode": "USDC"  
    }  
    
    
    
      
    
    
    
      
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "orderNo": "ord_sell_20240101_001"  
        },  
        "retExtInfo": {},  
        "time": 1704067200000  
    }

---

# 執行賣出

執行預測市場結果代幣份額的賣出委托，將份額兌換為 USDC。

信息

  * 必須先調用 [獲取撮合引擎狀態](/docs/zh-TW/v5/alpha/prediction/engine-status) 確認引擎可用
  * 必須先調用 [獲取持倉列表](/docs/zh-TW/v5/alpha/prediction/position-list) 確認持倉存在並查看可用 `shares`
  * 必須先調用 [獲取委托預估](/docs/zh-TW/v5/alpha/prediction/order-estimate) 預覽賣出委托
  * 必須向用戶展示預估結果並取得明確確認後，方可調用本接口
  * 第一階段僅支持 `orderType=1`（FOK）——無法完全成交的委托將被取消
  * `size` 為份額數量，非 USDC 金額
  * `200` 響應僅表示委托已受理，請調用 [獲取委托記錄](/docs/zh-TW/v5/alpha/prediction/order-list) 查詢最終成交狀態



### HTTP 請求

POST`/v5/alpha/prediction/sell`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
tokenId| **true**|  string| 要賣出的結果代幣 ID（從 [獲取持倉列表](/docs/zh-TW/v5/alpha/prediction/position-list) 獲取）  
size| **true**|  string| 賣出的份額數量（正數字符串）  
orderType| **true**|  integer| 委托類型。參考 [predictionOrderType](/docs/zh-TW/v5/enum#predictionordertype-prediction-market--order-type)。第一階段：`1`（FOK）  
slippage| **true**|  string| 最大可接受滑點（小數）。`0.05` = 5% 容忍度  
eventId| **true**|  string| 代幣對應的賽事 ID  
toTokenCode| false| string| 目標代幣代碼，第一階段固定為 `USDC`  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
orderNo| string| 委托號。請調用 [獲取委托記錄](/docs/zh-TW/v5/alpha/prediction/order-list) 查詢成交狀態  
  
### 請求示例

  * HTTP
  * Python
  * Node.js


    
    
    POST /v5/alpha/prediction/sell HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1704067200000  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "tokenId": "token_yes_123",  
        "size": "50",  
        "orderType": 1,  
        "slippage": "0.05",  
        "eventId": "event_123",  
        "toTokenCode": "USDC"  
    }  
    
    
    
      
    
    
    
      
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "orderNo": "ord_sell_20240101_001"  
        },  
        "retExtInfo": {},  
        "time": 1704067200000  
    }