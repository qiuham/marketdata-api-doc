---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/websocket/public/order-price-limit
api_type: WebSocket
updated_at: 2026-07-21 19:02:29.870947
---

# Order Price Limit

Subscribe to Get Order Price Limit.

For derivative trading order price limit, refer to [announcement](https://announcements.bybit.com/en/article/update-contract-price-limit-enhancement-bltf9ebdcebe3089641/)  
For spot trading order price limit, refer to [announcement](https://announcements.bybit.com/en/article/title-adjustments-to-bybit-s-spot-trading-limit-order-mechanism-blt786c0c5abf865983/)  


Push frequency: **300ms**

**Topic:**  
`priceLimit.{symbol}`  


### Response Parameters

Parameter| Type| Comments  
---|---|---  
topic| string| Topic name  
ts| number| The timestamp (ms) that the system generates the data  
data| array| Object.  
> symbol| string| Symbol name  
> buyLmt| string| Highest Bid Price  
> sellLmt| string| Lowest Ask Price  
  
### Subscribe Example

  * JSON
  * Python


    
    
    {  
        "op": "subscribe",  
        "args": [  
            "priceLimit.BTCUSDT"  
        ]  
    }  
    
    
    
    from pybit.unified_trading import WebSocket  
    from time import sleep  
    ws = WebSocket(  
        testnet=True,  
        channel_type="linear",  
    )  
    def handle_message(message):  
        print(message)  
    ws.price_limit_stream(  
        symbol="BTCUSDT",  
        callback=handle_message  
    )  
    while True:  
        sleep(1)  
    

### Response Example
    
    
    {  
        "topic": "priceLimit.BTCUSDT",  
        "data": {  
            "symbol": "BTCUSDT",  
            "buyLmt": "114450.00",  
            "sellLmt": "103550.00"  
        },  
        "ts": 1750059683782  
    }

---

# 訂單價格限制

訂閱訂單價格限制的推送.  
衍生性商品交易訂單價格限制，請參考[公告](https://announcements.bybit.com/en/article/update-contract-price-limit-enhancement-bltf9ebdcebe3089641/)  
現貨交易訂單價格限制，請參考[公告](https://announcements.bybit.com/en/article/title-adjustments-to-bybit-s-spot-trading-limit-order-mechanism-blt786c0c5abf865983/)  


推送頻率: **300毫秒**

**Topic:**  
`priceLimit.{symbol}`

### 響應參數

參數| 類型| 說明  
---|---|---  
topic| string| Topic名  
ts| number| 行情服務生成數據的時間戳 (毫秒)  
data| array| Object.  
> symbol| string| 合約名稱  
> buyLmt| string| 最高買價  
> sellLmt| string| 最低賣價  
  
### 訂閱示例

  * JSON
  * Python


    
    
    {  
        "op": "subscribe",  
        "args": [  
            "priceLimit.BTCUSDT"  
        ]  
    }  
    
    
    
    from pybit.unified_trading import WebSocket  
    from time import sleep  
    ws = WebSocket(  
        testnet=True,  
        channel_type="linear",  
    )  
    def handle_message(message):  
        print(message)  
    ws.price_limit_stream(  
        symbol="BTCUSDT",  
        callback=handle_message  
    )  
    while True:  
        sleep(1)  
    

### 響應示例
    
    
    {  
        "topic": "priceLimit.BTCUSDT",  
        "data": {  
            "symbol": "BTCUSDT",  
            "buyLmt": "114450.00",  
            "sellLmt": "103550.00"  
        },  
        "ts": 1750059683782  
    }