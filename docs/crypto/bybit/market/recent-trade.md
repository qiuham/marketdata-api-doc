---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/market/recent-trade
api_type: Market Data
updated_at: 2026-05-27 19:18:33.823744
---

# Get RPI Orderbook

Query for orderbook depth data.

> **Covers: Spot / USDT contract / USDC contract / Inverse contract /**

  * Contract: 50-level of RPI orderbook data
  * Spot: 50-level of RPI orderbook data



info

  * The response is in the snapshot format.



### HTTP Request

GET`/v5/market/rpi_orderbook`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
[category](/docs/v5/enum#category)| false| string| Product type. `spot`, `linear`, `inverse`  
symbol| **true**|  string| Symbol name, like `BTCUSDT`, uppercase only  
limit| **true**|  integer| Limit size for each bid and ask: [1, 50]  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
s| string| Symbol name  
> b| array| Bids. For `snapshot` stream. Sorted by price in descending order  
>> b[0]| string| Bid price  
>> b[1]| string| None RPI bid size 

  * The delta data has size=0, which means that all quotations for this price have been filled or cancelled

  
>> b[2]| string| RPI bid size 

  * When a bid RPI order crosses with a non-RPI ask price, the quantity of the bid RPI becomes invalid and is hidden

  
> a| array| Asks. For `snapshot` stream. Sorted by price in ascending order  
>> a[0]| string| Ask price  
>> a[1]| string| None RPI ask size 

  * The delta data has size=0, which means that all quotations for this price have been filled or cancelled

  
>> a[2]| string| RPI ask size 

  * When an ask RPI order crosses with a non-RPI bid price, the quantity of the ask RPI becomes invalid and is hidden

  
ts| integer| The timestamp (ms) that the system generates the data  
u| integer| Update ID, is always in sequence corresponds to `u` in the 50-level [WebSocket RPI orderbook stream](https://bybit-exchange.github.io/docs/v5/websocket/public/orderbook-rpi)  
seq| integer| Cross sequence 

  * You can use this field to compare different levels orderbook data, and for the smaller seq, then it means the data is generated earlier. 

  
cts| integer| The timestamp from the matching engine when this orderbook data is produced. It can be correlated with `T` from [public trade channel](/docs/v5/websocket/public/trade)  
  
* * *

### Request Example

  * HTTP
  * Python
  * Go
  * Java
  * Node.js


    
    
    GET /v5/market/rpi_orderbook?category=spot&symbol=BTCUSDT HTTP/1.1  
    Host: api-testnet.bybit.com  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.get_rpi_orderbook(  
        category="spot",  
        symbol="BTCUSDT",  
        limit=50  
    ))  
    
    
    
      
    
    
    
      
    
    
    
      
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "s": "BTCUSDT",  
            "a": [  
                [  
                    "116600.00",  
                    "4.428",  
                    "0.000"  
                ]  
            ],  
            "b": [  
                [  
                    "116599.90",  
                    "3.721",  
                    "0.000"  
                ]  
            ],  
            "ts": 1758078286128,  
            "u": 28419362,  
            "seq": 454803359210,  
            "cts": 1758078286118  
        },  
        "retExtInfo": {},  
        "time": 1758078286162  
    }

---

# RPI Orderbook (深度)

獲取深度數據

> **覆蓋範圍: 現貨 / USDT永續 / USDT交割 / USDC永續 / USDC交割 / 反向合約**

  * 期貨: 最多返回50檔的數據.
  * 現貨: 最多返回50檔的數據.



提示

響應是當前時間的切片數據

### HTTP請求

GET`/v5/market/rpi_orderbook`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
[category](/docs/zh-TW/v5/enum#category)| false| string| 產品類型. `spot`, `linear`, `inverse`  
symbol| **true**|  string| 合約名稱，例如“BTCUSDT”，僅限大寫  
limit| **true**|  integer| 深度限制: [1, 50]  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
s| string| 合約名稱  
> b| array| Bid, 買方. `snapshot`數據，是按照價格從大到小  
>> b[0]| string| 買方報價  
>> b[1]| string| 買方非RPI數量 

  * 增量數據的推送當出現size=0時，這意味著該價位的報價單全部成交或者全部撤銷

  
>> b[2]| string| 買方RPI數量 

  * 當買方RPI與賣方非RPI價格交叉，買方RPI數量失效隱藏

  
> a| array| Ask, 賣方. `snapshot`數據，是按照價格從小到大  
>> a[0]| string| 賣方報價  
>> a[1]| string| 賣方非RPI數量 

  * 增量數據的推送當出現size=0時，這意味著該價位的報價單全部成交或者全部撤銷

  
>> a[2]| string| 賣方RPI數量 

  * 當賣方RPI與買方非RPI價格交叉，賣方RPI數量失效隱藏

｜  
ts| integer| 行情服務生成數據的時間戳 (毫秒)  
u| integer| 更新id, 對應[RPI 深度](https://bybit-exchange.github.io/docs/v5/websocket/public/orderbook-rpi) 中的 `u`  
seq| integer| 撮合版本號 

  * 該字段可以用於關聯不同檔位的orderbook, 如果值越小, 則說明數據生成越早

  
cts| integer| 產生此訂單簿數據時來自撮合引擎的時間戳. 可用於與[平台成交](/docs/zh-TW/v5/websocket/public/trade)頻道中的`T`進行關聯  
  
* * *

### 請求示例

  * HTTP
  * Python
  * Go
  * Java
  * Node.js


    
    
    GET /v5/market/rpi_orderbook?category=spot&symbol=BTCUSDT HTTP/1.1  
    Host: api-testnet.bybit.com  
    
    
    
      
    
    
    
      
    
    
    
      
    
    
    
      
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "s": "BTCUSDT",  
            "a": [  
                [  
                    "116600.00",  
                    "4.428",  
                    "0.000"  
                ]  
            ],  
            "b": [  
                [  
                    "116599.90",  
                    "3.721",  
                    "0.000"  
                ]  
            ],  
            "ts": 1758078286128,  
            "u": 28419362,  
            "seq": 454803359210,  
            "cts": 1758078286118  
        },  
        "retExtInfo": {},  
        "time": 1758078286162  
    }