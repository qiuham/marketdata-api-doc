---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/spread/market/tickers
api_type: Market Data
updated_at: 2026-07-01 19:32:28.394696
---

# Cancel Order

### HTTP Request

POST`/v5/spread/order/cancel`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
orderId| false| string| Spread combination order ID. Either `orderId` or `orderLinkId` is **required**  
orderLinkId| false| string| User customised order ID. Either `orderId` or `orderLinkId` is **required**  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
orderId| string| Order ID  
orderLinkId| string| User customised order ID  
  
info

The acknowledgement of an cancel order request indicates that the request was sucessfully accepted. This request is asynchronous so please use the websocket to confirm the order status.

### Request Example

  * HTTP
  * Python


    
    
    POST /v5/spread/order/cancel HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXXXX  
    X-BAPI-API-KEY: XXXXXXX  
    X-BAPI-TIMESTAMP: 1744090699418  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
    Content-Length: 48  
      
    {  
        "orderLinkId": "1744072052193428476"  
    }  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.spread_cancel_order(  
        orderLinkId="1744072052193428476"  
    ))  
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "orderId": "4496253b-b55b-4407-8c5c-29629d169caf",  
            "orderLinkId": "1744072052193428476"  
        },  
        "retExtInfo": {},  
        "time": 1744090702715  
    }

---

# 撤銷價差委託單

### HTTP請求

POST`/v5/spread/order/cancel`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
orderId| false| string| 價差訂單ID. `orderId` 和 `orderLinkId` 必傳其中一個  
orderLinkId| false| string| 用戶自定義ID. `orderId` 和 `orderLinkId` 必傳其中一個  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
orderId| string| 價差訂單ID  
orderLinkId| string| 用戶自定義ID  
  
信息

ack僅表示請求被成功接受. 請使用websocket-order推送來確認訂單狀態

### 請求示例
    
    
    POST /v5/spread/order/cancel HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXXXX  
    X-BAPI-API-KEY: XXXXXXX  
    X-BAPI-TIMESTAMP: 1744090699418  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
    Content-Length: 48  
      
    {  
        "orderLinkId": "1744072052193428476"  
    }  
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "orderId": "4496253b-b55b-4407-8c5c-29629d169caf",  
            "orderLinkId": "1744072052193428476"  
        },  
        "retExtInfo": {},  
        "time": 1744090702715  
    }