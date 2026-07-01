---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/spot-margin-uta/tier-collateral-ratio
api_type: REST
updated_at: 2026-07-01 19:32:22.687701
---

# Get Orderbook

Query spread orderbook depth data.

### HTTP Request

GET`/v5/spread/orderbook`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
symbol| **true**|  string| Spread combination symbol name  
limit| false| integer| Limit size for each bid and ask [`1`, `25`]. Default: `1`  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
s| string| Spread combination symbol name  
b| array| Bid, buyer. Sorted by price in descending order  
> b[0]| string| Bid price  
> b[1]| string| Bid size  
a| array| Ask, seller. Sorted by price in ascending order  
> a[0]| string| Ask price  
> a[1]| string| Ask size  
ts| integer| The timestamp (ms) that the system generates the data  
u| integer| Update ID. Is always in sequence. Corresponds to `u` in the 25-level [WebSocket orderbook stream](https://bybit-exchange.github.io/docs/v5/spread/websocket/public/orderbook)  
seq| integer| Cross sequence  
cts| integer| The timestamp from the matching engine when this orderbook data is produced. It can be correlated with `T` from [public trade channel](/docs/v5/spread/websocket/public/trade)  
  
### Request Example

  * HTTP
  * Python


    
    
    GET /v5/spread/orderbook?symbol=SOLUSDT_SOL/USDT&limit=1 HTTP/1.1  
    Host: api-testnet.bybit.com  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.spread_get_orderbook(  
        symbol="SOLUSDT_SOL/USDT",  
        limit=1  
    ))  
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "Success",  
        "result": {  
            "s": "SOLUSDT_SOL/USDT",  
            "b": [  
                [  
                    "21.0000",  
                    "0.1"  
                ]  
            ],  
            "a": [  
                [  
                    "23.0107",  
                    "4.6"  
                ]  
            ],  
            "u": 46977,  
            "ts": 1744077242177,  
            "seq": 213110,  
            "cts": 1744076329043  
        },  
        "retExtInfo": {},  
        "time": 1744077243583  
    }

---

# 查詢深度

### HTTP請求

GET`/v5/spread/orderbook`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
symbol| **true**|  string| 價差產品名稱  
limit| false| integer| 深度限制 [`1`, `25`]. 默認: `1`  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
s| string| 價差產品名稱  
b| array| Bid, 買方. 按照價格從大到小  
> b[0]| string| 買方報價  
> b[1]| string| 買方數量  
a| array| Ask, 賣方. 按照價格從小到大  
> a[0]| string| 賣方報價  
> a[1]| string| 賣方數量  
ts| integer| 行情服務生成數據時間戳（毫秒）  
u| integer| 表示數據連續性的id, 它和wss推送裡的25檔的`u`對齊  
seq| integer| 撮合版本號  
cts| integer| 產生此訂單簿數據時來自撮合引擎的時間戳. 可用於與平台成交頻道中的T進行關聯  
  
### 請求示例
    
    
    GET /v5/spread/orderbook?symbol=SOLUSDT_SOL/USDT&limit=1 HTTP/1.1  
    Host: api-testnet.bybit.com  
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "Success",  
        "result": {  
            "s": "SOLUSDT_SOL/USDT",  
            "b": [  
                [  
                    "21.0000",  
                    "0.1"  
                ]  
            ],  
            "a": [  
                [  
                    "23.0107",  
                    "4.6"  
                ]  
            ],  
            "u": 46977,  
            "ts": 1744077242177,  
            "seq": 213110,  
            "cts": 1744076329043  
        },  
        "retExtInfo": {},  
        "time": 1744077243583  
    }