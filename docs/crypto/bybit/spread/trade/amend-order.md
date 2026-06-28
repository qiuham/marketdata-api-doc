---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/spread/trade/amend-order
api_type: Trading
updated_at: 2026-05-27 19:22:30.481111
---

# Cancel All Orders

Cancel all open orders

### HTTP Request

POST`/v5/spread/order/cancel-all`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
symbol| false| string| Spread combination symbol name 

  * When a symbol is specified, all orders for that symbol will be cancelled regardless of the `cancelAll` field.
  * When a symbol is not specified and `cancelAll`=true, all orders, regardless of the symbol, will be cancelled

  
cancelAll| false| boolean| `true`, `false`  
  
info

The acknowledgement of cancel all orders request indicates that the request was sucessfully accepted. This request is asynchronous so please use the websocket to confirm the order status.

### Response Parameters

Parameter| Type| Comments  
---|---|---  
list| array<object>|   
> orderId| string| Order ID  
> orderLinkId| string| User customised order ID  
success| string| The field can be ignored  
  
### Request Example

  * HTTP
  * Python


    
    
    POST /v5/spread/order/cancel-all HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: XXXXXX  
    X-BAPI-TIMESTAMP: 1744090967121  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
    Content-Length: 49  
      
    {  
        "symbol": null,  
        "cancelAll": true  
    }  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.spread_cancel_all_orders(  
        cancelAll=True  
    ))  
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "list": [  
                {  
                    "orderId": "11ec47f3-f0a2-4b2a-b302-236f2a2d53a2",  
                    "orderLinkId": ""  
                }  
            ],  
            "success": "1"  
        },  
        "retExtInfo": {},  
        "time": 1744090940933  
    }

---

# 價差-全部撤單

### HTTP請求

POST`/v5/spread/order/cancel-all`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
symbol| false| string| 價差產品名稱 

  * 當指定`symbol`時, 這個symbol的所有活動單都會被取消, 不管`cancelAll`參數如何設置.
  * 當不指定`symbol`時, 並且`cancelAll`=true, 所有symbol的活動單都會被取消

  
cancelAll| false| boolean| `true`, `false`  
  
信息

ack僅表示請求被成功接受. 請使用websocket-order推送來確認訂單狀態

### 響應參數

參數| 類型| 說明  
---|---|---  
list| array<object>|   
> orderId| string| 價差訂單ID  
> orderLinkId| string| 用戶自定義訂單ID  
success| string| 該字段可以忽略, 無實際意義  
  
### 請求示例
    
    
    POST /v5/spread/order/cancel-all HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: XXXXXX  
    X-BAPI-TIMESTAMP: 1744090967121  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
    Content-Length: 49  
      
    {  
         
        "symbol": null,  
        "cancelAll": true  
    }  
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "list": [  
                {  
                    "orderId": "11ec47f3-f0a2-4b2a-b302-236f2a2d53a2",  
                    "orderLinkId": ""  
                }  
            ],  
            "success": "1"  
        },  
        "retExtInfo": {},  
        "time": 1744090940933  
    }