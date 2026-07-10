---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/spread/trade/cancel-all
api_type: Trading
updated_at: 2026-07-10 19:06:26.658867
---

# Create Order

Place a spread combination order. **Up to 50 open orders** per account.

### HTTP Request

POST`/v5/spread/order/create`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
symbol| **true**|  string| Spread combination symbol name  
side| **true**|  string| Order side. `Buy`, `Sell`  
orderType| **true**|  string| `Limit`, `Market`  
qty| **true**|  string| Order qty  
price| false| string| Order price  
orderLinkId| false| string| User customised order ID, a max of 45 characters. Combinations of numbers, letters (upper and lower cases), dashes, and underscores are supported.  
timeInForce| false| string| [Time in force](https://www.bybit.com/en/help-center/article/What-Are-Time-In-Force-TIF-GTC-IOC-FOK). `IOC`, `FOK`, `GTC`, `PostOnly`  
  
info

The acknowledgement of an place order request indicates that the request was sucessfully accepted. This request is asynchronous so please use the websocket to confirm the order status.

### Response Parameters

Parameter| Type| Comments  
---|---|---  
orderId| string| Spread combination order ID  
orderLinkId| string| User customised order ID  
  
### Request Example

  * HTTP
  * Python


    
    
    POST /v5/spread/order/create HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: XXXXXX  
    X-BAPI-TIMESTAMP: 1744079410023  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
    Content-Length: 191  
      
    {  
        "symbol": "SOLUSDT_SOL/USDT",  
        "side": "Buy",  
        "orderType": "Limit",  
        "qty": "0.1",  
        "price": "21",  
        "orderLinkId": "1744072052193428479",  
        "timeInForce": "PostOnly"  
    }  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.spread_place_order(  
        symbol="SOLUSDT_SOL/USDT",  
        side="Buy",  
        orderType="Limit",  
        qty="0.1",  
        price="21",  
        orderLinkId="1744072052193428479",  
        timeInForce="PostOnly"  
    ))  
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "orderId": "1b00b997-d825-465e-ad1d-80b0eb1955af",  
            "orderLinkId": "1744072052193428479"  
        },  
        "retExtInfo": {},  
        "time": 1744075839332  
    }

---

# 創建價差委托單

每個帳戶最多支持50個活動單

### HTTP請求

POST`/v5/spread/order/create`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
symbol| **true**|  string| 價差產品名稱  
side| **true**|  string| 訂單方向, `Buy`, `Sell`  
orderType| **true**|  string| 訂單類型 `Limit`, `Market`  
qty| **true**|  string| 訂單數量  
price| **true**|  string| 訂單價格  
orderLinkId| **true**|  string| 用戶自定義訂單ID, 最多 45 個字元。支援數字、字母（大寫和小寫）、破折號和底線的組合  
timeInForce| **true**|  string| [訂單執行策略](https://www.bybit.com/en/help-center/article/What-Are-Time-In-Force-TIF-GTC-IOC-FOK) `IOC`, `FOK`, `GTC`, `PostOnly`  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
orderId| string| 價差訂單ID  
orderLinkId| string| 用戶自定義訂單ID  
  
### 請求示例
    
    
    POST /v5/spread/order/create HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: XXXXXX  
    X-BAPI-TIMESTAMP: 1744079410023  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
    Content-Length: 191  
      
    {  
        "symbol": "SOLUSDT_SOL/USDT",  
        "side": "Buy",  
        "orderType": "Limit",  
        "qty": "0.1",  
        "price": "21",  
        "orderLinkId": "1744072052193428479",  
        "timeInForce": "PostOnly"  
    }  
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "orderId": "1b00b997-d825-465e-ad1d-80b0eb1955af",  
            "orderLinkId": "1744072052193428479"  
        },  
        "retExtInfo": {},  
        "time": 1744075839332  
    }