---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/spread/market/instrument
api_type: Market Data
updated_at: 2026-07-02 19:21:42.858860
---

# Amend Order

info

You can only modify **unfilled** or **partially filled** orders.

### HTTP Request

POST`/v5/spread/order/amend`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
symbol| **true**|  string| Spread combination symbol name  
orderId| false| string| Spread combination order ID. Either `orderId` or `orderLinkId` is **required**  
orderLinkId| false| string| User customised order ID. Either `orderId` or `orderLinkId` is **required**  
qty| false| string| Order quantity after modification. Either `qty` or `price` is **required**  
price| false| string| Order price after modification 

  * Either `qty` or `price` is **required**
  * price="" means the price remains unchanged, while price="0" updates the price to 0.

  
  
info

The acknowledgement of an amend order request indicates that the request was sucessfully accepted. This request is asynchronous so please use the websocket to confirm the order status.

### Response Parameters

Parameter| Type| Comments  
---|---|---  
orderId| string| Order ID  
orderLinkId| string| User customised order ID  
  
### Request Example

  * HTTP
  * Python


    
    
    POST /v5/spread/order/amend HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: XXXXXX  
    X-BAPI-TIMESTAMP: 1744083949347  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
    Content-Length: 115  
      
    {  
        "symbol": "SOLUSDT_SOL/USDT",  
        "orderLinkId": "1744072052193428475",  
        "price": "14",  
        "qty": "0.2"  
    }  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.spread_amend_order(  
        symbol="SOLUSDT_SOL/USDT",  
        orderLinkId="1744072052193428475",  
        price="14",  
        qty="0.2"  
    ))  
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "orderId": "b0e6c938-9731-4122-8552-01e6dc06b303",  
            "orderLinkId": "1744072052193428475"  
        },  
        "retExtInfo": {},  
        "time": 1744083952599  
    }

---

# 修改價差委託單

信息

您只能修改那些 _未成交_ 或者 _部分成交_ 的訂單。

### HTTP請求

POST`/v5/spread/order/amend`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
symbol| **true**|  string| 價差產品名稱  
orderId| false| string| 價差訂單ID. `orderId` 和 `orderLinkId` 必傳其中一個  
orderLinkId| false| string| 用戶自定義訂單ID. `orderId` 和 `orderLinkId` 必傳其中一個  
qty| false| string| 訂單數量 

  * `qty`和`price`必須傳其中一個

  
price| false| string| 訂單價格

  * `qty`和`price`必須傳其中一個
  * 傳price="" 表示價格不變, 如果設置price="0" 表示價格將修改為0.

  
  
信息

ack僅表示請求被成功接受. 請使用websocket-order推送來確認訂單狀態

### 響應參數

參數| 類型| 說明  
---|---|---  
orderId| string| 價差訂單ID  
orderLinkId| string| 用戶自定義訂單ID  
  
### 請求示例
    
    
    POST /v5/spread/order/amend HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: XXXXXX  
    X-BAPI-TIMESTAMP: 1744083949347  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
    Content-Length: 115  
      
    {  
        "symbol": "SOLUSDT_SOL/USDT",  
        "orderLinkId": "1744072052193428475",  
        "price": "14",  
        "qty": "0.2"  
    }  
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "orderId": "b0e6c938-9731-4122-8552-01e6dc06b303",  
            "orderLinkId": "1744072052193428475"  
        },  
        "retExtInfo": {},  
        "time": 1744083952599  
    }