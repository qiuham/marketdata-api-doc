---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/spot-margin-uta/fixedborrow-order-cancel
api_type: REST
updated_at: 2026-11-13 19:25:10.403387
---

# Cancel Fixed-Rate Borrow Order

Request cancellation of an eligible fixed-rate borrow order. The order must be in a cancellable state. The response does not include a final order status; query the order later to confirm its status.

### HTTP Request

POST`/v5/spot-margin-trade/fixedborrow-order-cancel`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
orderId| **true**|  string| Fixed-rate borrow order ID  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
result| object| Empty object. Check `retCode` to confirm the cancellation request was accepted  
  
* * *

### Request Example

  * HTTP


    
    
    POST /v5/spot-margin-trade/fixedborrow-order-cancel HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1792117143000  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "orderId": "FIXED_BORROW_example"  
    }  
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {},  
        "retExtInfo": {},  
        "time": 1792117143000  
    }

---

# 取消固定利率借款訂單

申請取消符合條件的固定利率借款訂單。訂單必須處於可取消狀態。響應不包含最終訂單狀態，請後續查詢訂單以確認其最終狀態。

### HTTP 請求

POST`/v5/spot-margin-trade/fixedborrow-order-cancel`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
orderId| **true**|  string| 固定利率借款訂單 ID  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
result| object| 空物件。請檢查 `retCode` 以確認取消請求是否已受理  
  
* * *

### 請求示例

  * HTTP


    
    
    POST /v5/spot-margin-trade/fixedborrow-order-cancel HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1792117143000  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "orderId": "FIXED_BORROW_example"  
    }  
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {},  
        "retExtInfo": {},  
        "time": 1792117143000  
    }