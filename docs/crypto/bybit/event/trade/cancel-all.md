---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/event/trade/cancel-all
api_type: Trading
updated_at: 2026-11-13 19:22:32.607128
---

# Cancel All Quotes

Cancel all active Event Contract quotes that match the supplied filters.

info

  * Only **Event Contract maker accounts** are allowed to access this endpoint.



### HTTP Request

POST`/v5/event/cancel-all`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
symbol| **true**|  string| Symbol name  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
list| array| Cancelled order list  
> orderId| string| Order ID  
> orderLinkId| string| User-defined order ID  
success| string| `1`: success; `0`: failed  
  
* * *

### Request Example
    
    
    POST /v5/event/cancel-all HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1707381118116  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "symbol": "ETHUSDT-28AUG26-2450-2570-OUT"  
    }  
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "list": [  
                {  
                    "orderId": "96fc8deb-6b65-4af6-8666-38bf7e96aaab",  
                    "orderLinkId": "cjm1150"  
                },  
                {  
                    "orderId": "3f5edf32-d94d-41cf-87ee-0b9a004a3de6",  
                    "orderLinkId": "cjm1143"  
                },  
                {  
                    "orderId": "69b32753-f232-49e5-8a08-296e644d91b2",  
                    "orderLinkId": "cjm1145"  
                }  
            ],  
            "success": "1"  
        },  
        "retExtInfo": {},  
        "time": 1793762591450  
    }

---

# 撤銷全部報價

撤銷指定 Event Contract 交易對的全部有效報價。

信息

  * 僅 **Event Contract maker 帳戶** 可訪問此接口。



### HTTP 請求

POST`/v5/event/cancel-all`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
symbol| **true**|  string| 交易對名稱  
  
### 返回參數

參數| 類型| 說明  
---|---|---  
list| array| 已撤銷的訂單列表  
> orderId| string| 訂單 ID  
> orderLinkId| string| 用戶自定義訂單 ID  
success| string| `1`：成功；`0`：失敗  
  
* * *

### 請求示例
    
    
    POST /v5/event/cancel-all HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1707381118116  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "symbol": "ETHUSDT-28AUG26-2450-2570-OUT"  
    }  
    

### 返回示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "list": [  
                {  
                    "orderId": "96fc8deb-6b65-4af6-8666-38bf7e96aaab",  
                    "orderLinkId": "cjm1150"  
                },  
                {  
                    "orderId": "3f5edf32-d94d-41cf-87ee-0b9a004a3de6",  
                    "orderLinkId": "cjm1143"  
                },  
                {  
                    "orderId": "69b32753-f232-49e5-8a08-296e644d91b2",  
                    "orderLinkId": "cjm1145"  
                }  
            ],  
            "success": "1"  
        },  
        "retExtInfo": {},  
        "time": 1793762591450  
    }