---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/event/trade/cancel-quote
api_type: Trading
updated_at: 2026-11-13 19:22:32.631511
---

# Cancel Quote

Cancel a submitted Event Contract quote.

info

  * Only **Event Contract maker accounts** are allowed to access this endpoint.



### HTTP Request

POST`/v5/event/cancel`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
orderLinkId| false| string| User-defined order ID (Quote ID)  
orderId| false| string| Order ID  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
orderLinkId| string| User-defined order ID  
orderId| string| Order ID  
  
* * *

### Request Example
    
    
    POST /v5/event/cancel HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1694402559000  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "orderLinkId": "xxxxxx",  
        "orderId": "xxxxxxxxxxefffff"  
    }  
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "orderLinkId": "xxxxxx",  
            "orderId": "xxxxxxxxxxefffff"  
        },  
        "retExtInfo": {},  
        "time": 1672217377164  
    }

---

# 撤銷報價

撤銷已提交的 Event Contract 報價。

信息

  * 僅 **Event Contract maker 帳戶** 可訪問此接口。



### HTTP 請求

POST`/v5/event/cancel`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
orderLinkId| 否| string| 用戶自定義訂單 ID（報價 ID）  
orderId| 否| string| 訂單 ID  
  
### 返回參數

參數| 類型| 說明  
---|---|---  
orderLinkId| string| 用戶自定義訂單 ID  
orderId| string| 訂單 ID  
  
* * *

### 請求示例
    
    
    POST /v5/event/cancel HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1694402559000  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "orderLinkId": "xxxxxx",  
        "orderId": "xxxxxxxxxxefffff"  
    }  
    

### 返回示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "orderLinkId": "xxxxxx",  
            "orderId": "xxxxxxxxxxefffff"  
        },  
        "retExtInfo": {},  
        "time": 1672217377164  
    }