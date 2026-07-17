---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/order/pre-check-order
api_type: Trading
updated_at: 2026-07-17 18:51:54.338992
---

# Pre Check Order

This endpoint is used to calculate the changes in IMR and MMR of UTA account before and after placing an order.

info

  1. This endpoint supports orders with category = `inverse`,`linear`,`option`.   

  2. Only Cross Margin mode and Portfolio Margin mode are supported, isolated margin mode is not supported.  

  3. category = `inverse` is not supported in Cross Margin mode.  

  4. Conditional order is not supported.  

  5. If `retCode` is neither 0 nor 110007, `result` will return an empty json. `future_order_id`, `future_order_link_id` will be displayed in the `retExtInfo` json.
  6. If `retCode` is 110007, `result` will return an empty json. `future_order_id`, `future_order_link_id`, `post_imr_e4`, and `post_mmr_e4` will be displayed in the `retExtInfo` json.



### HTTP Request

POST`/v5/order/pre-check`

### Request Parameters

refer to [create order request](/docs/v5/order/create-order#request-parameters)

### Response Parameters

Parameter| Type| Comments  
---|---|---  
orderId| string| Order ID  
orderLinkId| string| User customised order ID  
preImrE4| int| Initial margin rate before checking, keep four decimal places. For examples, 30 means IMR = 30/1e4 = 0.30%  
preMmrE4| int| Maintenance margin rate before checking, keep four decimal places. For examples, 30 means MMR = 30/1e4 = 0.30%  
postImrE4| int| Initial margin rate calculated after checking, keep four decimal places. For examples, 30 means IMR = 30/1e4 = 0.30%  
postMmrE4| int| Maintenance margin rate calculated after checking, keep four decimal places. For examples, 30 means MMR = 30/1e4 = 0.30%  
  
* * *

### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    POST /v5/order/pre-check HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1672211928338  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    // Spot Limit order with market tp sl  
    {"category": "spot","symbol": "BTCUSDT","side": "Buy","orderType": "Limit","qty": "0.01","price": "28000","timeInForce": "PostOnly","takeProfit": "35000","stopLoss": "27000","tpOrderType": "Market","slOrderType": "Market"}  
      
    // Spot Limit order with limit tp sl  
    {"category": "spot","symbol": "BTCUSDT","side": "Buy","orderType": "Limit","qty": "0.01","price": "28000","timeInForce": "PostOnly","takeProfit": "35000","stopLoss": "27000","tpLimitPrice": "36000","slLimitPrice": "27500","tpOrderType": "Limit","slOrderType": "Limit"}  
      
    // Spot PostOnly normal order  
    {"category":"spot","symbol":"BTCUSDT","side":"Buy","orderType":"Limit","qty":"0.1","price":"15600","timeInForce":"PostOnly","orderLinkId":"spot-test-01","isLeverage":0,"orderFilter":"Order"}  
      
    // Spot TP/SL order  
    {"category":"spot","symbol":"BTCUSDT","side":"Buy","orderType":"Limit","qty":"0.1","price":"15600","triggerPrice": "15000", "timeInForce":"Limit","orderLinkId":"spot-test-02","isLeverage":0,"orderFilter":"tpslOrder"}  
      
    // Spot margin normal order (UTA)  
    {"category":"spot","symbol":"BTCUSDT","side":"Buy","orderType":"Limit","qty":"0.1","price":"15600","timeInForce":"GTC","orderLinkId":"spot-test-limit","isLeverage":1,"orderFilter":"Order"}  
      
    // Spot Market Buy order, qty is quote currency  
    {"category":"spot","symbol":"BTCUSDT","side":"Buy","orderType":"Market","qty":"200","timeInForce":"IOC","orderLinkId":"spot-test-04","isLeverage":0,"orderFilter":"Order"}  
      
      
    // USDT Perp open long position (one-way mode)  
    {"category":"linear","symbol":"BTCUSDT","side":"Buy","orderType":"Limit","qty":"1","price":"25000","timeInForce":"GTC","positionIdx":0,"orderLinkId":"usdt-test-01","reduceOnly":false,"takeProfit":"28000","stopLoss":"20000","tpslMode":"Partial","tpOrderType":"Limit","slOrderType":"Limit","tpLimitPrice":"27500","slLimitPrice":"20500"}  
      
    // USDT Perp close long position (one-way mode)  
    {"category": "linear", "symbol": "BTCUSDT", "side": "Sell", "orderType": "Limit", "qty": "1", "price": "30000", "timeInForce": "GTC", "positionIdx": 0, "orderLinkId": "usdt-test-02", "reduceOnly": true}  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.pre_check_order(  
        category="spot",  
        symbol="BTCUSDT",  
        side="Buy",  
        orderType="Limit",  
        qty="0.1",  
        price="28000",  
        timeInForce="PostOnly",  
        takeProfit="35000",  
        stopLoss="27000",  
        tpOrderType="Market",  
        slOrderType="Market",  
    ))  
    
    
    
      
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "orderId": "24920bdb-4019-4e37-ad1c-876e3a855ac3",  
            "orderLinkId": "test129",  
            "preImrE4": 30,  
            "preMmrE4": 21,  
            "postImrE4": 357,  
            "postMmrE4": 294  
        },  
        "retExtInfo": {},  
        "time": 1749541599589  
    }

---

# 預下單

此接口用於計算UTA帳戶下單前後IMR、MMR的變化。

信息

  1. 此接口只支持期貨和期權的訂單。   

  2. 僅支持全倉模式和組合保證金模式，不支援逐倉模式。   

  3. 全倉模式下不支持反向訂單。   

  4. 不支持條件訂單。   

  5. 如果`retCode`既不是0也不是110007，`result`將回傳空json。 `future_order_id`，`future_order_link_id` 會顯示在`retExtInfo`這個json裡。
  6. 如果`retCode` 是 110007，`result`將回傳空json。 `future_order_id`，`future_order_link_id`，`post_imr_e4`，`post_mmr_e4`會顯示在`retExtInfo`這個json裡。



### HTTP請求

POST`/v5/order/pre-check`

### 請求參數

參考 [create order request](/docs/zh-TW/v5/order/create-order#request-parameters)

### 響應參數

參數| 類型| 說明  
---|---|---  
orderId| string| 訂單ID  
orderLinkId| string| 用戶自定義訂單ID  
preImrE4| int| 預下單前的初始保證金率，保留小數點後四位。例如，30 表示 IMR = 30/1e4 = 0.30%  
preMmrE4| int| 預下單前的維持保證金率，保留小數點後四位。例如：30 表示 MMR = 30/1e4 = 0.30%  
postImrE4| int| 預下單後計算的初始保證金率，保留小數點後四位。例如：30 表示 IMR = 30/1e4 = 0.30%  
postMmrE4| int| 預下單後計算的維持保證金率，保留小數點後四位。例如：30 表示 MMR = 30/1e4 = 0.30%  
  
* * *

### 請求示例

  * HTTP
  * Python
  * Node.js


    
    
    POST /v5/order/pre-check HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1672211928338  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    // Spot Limit order with market tp sl  
    {"category": "spot","symbol": "BTCUSDT","side": "Buy","orderType": "Limit","qty": "0.01","price": "28000","timeInForce": "PostOnly","takeProfit": "35000","stopLoss": "27000","tpOrderType": "Market","slOrderType": "Market"}  
      
    // Spot Limit order with limit tp sl  
    {"category": "spot","symbol": "BTCUSDT","side": "Buy","orderType": "Limit","qty": "0.01","price": "28000","timeInForce": "PostOnly","takeProfit": "35000","stopLoss": "27000","tpLimitPrice": "36000","slLimitPrice": "27500","tpOrderType": "Limit","slOrderType": "Limit"}  
      
    // Spot PostOnly normal order  
    {"category":"spot","symbol":"BTCUSDT","side":"Buy","orderType":"Limit","qty":"0.1","price":"15600","timeInForce":"PostOnly","orderLinkId":"spot-test-01","isLeverage":0,"orderFilter":"Order"}  
      
    // Spot TP/SL order  
    {"category":"spot","symbol":"BTCUSDT","side":"Buy","orderType":"Limit","qty":"0.1","price":"15600","triggerPrice": "15000", "timeInForce":"Limit","orderLinkId":"spot-test-02","isLeverage":0,"orderFilter":"tpslOrder"}  
      
    // Spot margin normal order (UTA)  
    {"category":"spot","symbol":"BTCUSDT","side":"Buy","orderType":"Limit","qty":"0.1","price":"15600","timeInForce":"GTC","orderLinkId":"spot-test-limit","isLeverage":1,"orderFilter":"Order"}  
      
    // Spot Market Buy order, qty is quote currency  
    {"category":"spot","symbol":"BTCUSDT","side":"Buy","orderType":"Market","qty":"200","timeInForce":"IOC","orderLinkId":"spot-test-04","isLeverage":0,"orderFilter":"Order"}  
      
      
    // USDT Perp open long position (one-way mode)  
    {"category":"linear","symbol":"BTCUSDT","side":"Buy","orderType":"Limit","qty":"1","price":"25000","timeInForce":"GTC","positionIdx":0,"orderLinkId":"usdt-test-01","reduceOnly":false,"takeProfit":"28000","stopLoss":"20000","tpslMode":"Partial","tpOrderType":"Limit","slOrderType":"Limit","tpLimitPrice":"27500","slLimitPrice":"20500"}  
      
    // USDT Perp close long position (one-way mode)  
    {"category": "linear", "symbol": "BTCUSDT", "side": "Sell", "orderType": "Limit", "qty": "1", "price": "30000", "timeInForce": "GTC", "positionIdx": 0, "orderLinkId": "usdt-test-02", "reduceOnly": true}  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.pre_check_order(  
        category="spot",  
        symbol="BTCUSDT",  
        side="Buy",  
        orderType="Limit",  
        qty="0.1",  
        price="28000",  
        timeInForce="PostOnly",  
        takeProfit="35000",  
        stopLoss="27000",  
        tpOrderType="Market",  
        slOrderType="Market",  
    ))  
    
    
    
      
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "orderId": "24920bdb-4019-4e37-ad1c-876e3a855ac3",  
            "orderLinkId": "test129",  
            "preImrE4": 30,  
            "preMmrE4": 21,  
            "postImrE4": 357,  
            "postMmrE4": 294  
        },  
        "retExtInfo": {},  
        "time": 1749541599589  
    }