---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/spread/trade/cancel-order
api_type: Trading
updated_at: 2026-07-02 19:21:49.242353
---

# Get Open Orders

info

  * During periods of extreme market volatility, this interface may experience increased latency or temporary delays in data delivery



### HTTP Request

GET`/v5/spread/order/realtime`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
symbol| false| string| Spread combination symbol name  
baseCoin| false| string| Base coin  
orderId| false| string| Spread combination order ID  
orderLinkId| false| string| User customised order ID  
limit| false| integer| Limit for data size per page. [`1`, `50`]. Default: `20`  
cursor| false| string| Cursor. Use the `nextPageCursor` token from the response to retrieve the next page of the result set  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
list| array<object>| Order info  
> symbol| string| Spread combination symbol name  
> baseCoin| string| Base coin  
> orderType| string| Order type, `Market`, `Limit`  
> orderLinkId| string| User customised order ID  
> side| string| Side, `Buy`, `Sell`  
> timeInForce| string| Time in force, `GTC`, `FOK`, `IOC`, `PostOnly`  
> orderId| string| Spread combination order ID  
> leavesQty| string| The remaining qty not executed  
> orderStatus| string| Order status, `New`, `PartiallyFilled`  
> cumExecQty| string| Cumulative executed order qty  
> price| string| Order price  
> qty| string| Order qty  
> createdTime| string| Order created timestamp (ms)  
> updatedTime| string| Order updated timestamp (ms)  
nextPageCursor| string| Refer to the `cursor` request parameter  
  
### Request Example

  * HTTP
  * Python


    
    
    GET /v5/spread/order/realtime HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: XXXXXX  
    X-BAPI-TIMESTAMP: 1744096099520  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.spread_get_open_orders())  
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "nextPageCursor": "aaaee090-fab3-42ea-aea0-c9fbfe6c4bc4%3A1744096099767%2Caaaee090-fab3-42ea-aea0-c9fbfe6c4bc4%3A1744096099767",  
            "list": [  
                {  
                    "symbol": "SOLUSDT_SOL/USDT",  
                    "orderType": "Limit",  
                    "updatedTime": "1744096099771",  
                    "orderLinkId": "",  
                    "side": "Buy",  
                    "orderId": "aaaee090-fab3-42ea-aea0-c9fbfe6c4bc4",  
                    "leavesQty": "0.1",  
                    "orderStatus": "New",  
                    "cumExecQty": "0",  
                    "price": "-4",  
                    "qty": "0.1",  
                    "createdTime": "1744096099767",  
                    "timeInForce": "PostOnly",  
                    "baseCoin": "SOL"  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1744096103435  
    }

---

# 查詢價差活動單

信息

  * 在極端市場波動期間, 此介面可能會出現延遲增加或資料傳遞暫時延遲的情況



### HTTP請求

GET`/v5/spread/order/realtime`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
symbol| false| string| 價差產品名稱  
baseCoin| false| string| 交易幣種  
orderId| false| string| 價差訂單ID  
orderLinkId| false| string| 用戶自定義ID  
limit| false| integer| 每頁數量限制. [`1`, `50`]. 默認: `20`  
cursor| false| string| 游標，用於翻頁  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
list| array<object>| 訂單信息  
> symbol| string| 價差產品名稱  
> orderType| string| 訂單類型, `Market`, `Limit`  
> updatedTime| string| 訂單更新時間 (毫秒)  
> orderId| string| 價差訂單ID  
> orderLinkId| string| 用戶自定義ID  
> side| string| 訂單方向, `Buy`, `Sell`  
> leavesQty| string| 剩餘未成交數量  
> orderStatus| string| 訂單狀態, `New`, `PartiallyFilled`  
> cumExecQty| string| 累計成交數量  
> price| string| 訂單價格  
> qty| string| 訂單數量  
> createdTime| string| 訂單創建時間 (毫秒)  
> timeInForce| string| 訂單執行策略, `GTC`, `FOK`, `IOC`, `PostOnly`  
> baseCoin| string| 交易幣種  
nextPageCursor| string| 游標，用於翻頁  
  
### 請求示例
    
    
    GET /v5/spread/order/realtime HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: XXXXXX  
    X-BAPI-TIMESTAMP: 1744096099520  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "nextPageCursor": "aaaee090-fab3-42ea-aea0-c9fbfe6c4bc4%3A1744096099767%2Caaaee090-fab3-42ea-aea0-c9fbfe6c4bc4%3A1744096099767",  
            "list": [  
                {  
                    "symbol": "SOLUSDT_SOL/USDT",  
                    "orderType": "Limit",  
                    "updatedTime": "1744096099771",  
                    "orderLinkId": "",  
                    "side": "Buy",  
                    "orderId": "aaaee090-fab3-42ea-aea0-c9fbfe6c4bc4",  
                    "leavesQty": "0.1",  
                    "orderStatus": "New",  
                    "cumExecQty": "0",  
                    "price": "-4",  
                    "qty": "0.1",  
                    "createdTime": "1744096099767",  
                    "timeInForce": "PostOnly",  
                    "baseCoin": "SOL"  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1744096103435  
    }