---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/websocket/public/orderbook-rpi
api_type: WebSocket
updated_at: 2026-05-27 19:23:26.277711
---

# RPI Orderbook

Subscribe to the orderbook stream including RPI quote

### Depths

**Spot, Perpetual & Futures:**  
Level 50 data, push frequency: **100ms**  


**Topic:**  
`orderbook.rpi.{symbol}` e.g., orderbook.rpi.BTCUSDT

### Response Parameters

Parameter| Type| Comments  
---|---|---  
topic| string| Topic name  
type| string| Data type. `snapshot`,`delta`  
ts| number| The timestamp (ms) that the system generates the data  
data| map| Object  
> s| string| Symbol name  
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

  
> u| integer| Update ID

  * Occasionally, you'll receive "u"=1, which is a snapshot data due to the restart of the service. So please overwrite your local orderbook

  
> seq| integer| Cross sequence 

  * You can use this field to compare different levels orderbook data, and for the smaller seq, then it means the data is generated earlier. 

  
cts| number| The timestamp from the matching engine when this orderbook data is produced. It can be correlated with `T` from [public trade channel](/docs/v5/websocket/public/trade)  
  
### Subscribe Example

  * JSON
  * Python


    
    
    {  
        "op": "subscribe",  
        "args": [  
            "orderbook.rpi.BTCUSDT"  
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
    ws.rpi_orderbook_stream(  
        symbol="BTCUSDT",  
        callback=handle_message  
    )  
    while True:  
        sleep(1)  
    

### Subscribe Success Response
    
    
    {  
        "success": true,  
        "ret_msg": "subscribe",  
        "conn_id": "f6b17b77-48b6-4c5c-b5ec-4a1c733f5763",  
        "op": "subscribe"  
    }  
    

### Response Example
    
    
    {  
        "topic": "orderbook.rpi.BTCUSDT",  
        "ts": 1752472188075,  
        "type": "delta",  
        "data": {  
            "s": "BTCUSDT",  
            "b": [  
                [  
                    "121975.1",  
                    "0.114259",  
                    "0"  
                ],  
                [  
                    "121969.9",  
                    "0",  
                    "0"  
                ],  
                [  
                    "121960.5",  
                    "0",  
                    "0.163986"  
                ]  
            ],  
            "a": [  
                [  
                    "121990.8",  
                    "0.441585",  
                    "0.78821"  
                ],  
                [  
                    "121996.1",  
                    "0.016393",  
                    "0"  
                ],  
                [  
                    "122018.5",  
                    "0",  
                    "0"  
                ]  
            ],  
            "u": 2258980,  
            "seq": 79683241099  
        },  
        "cts": 1752472188067  
    }

---

# RPI 深度

訂閱訂單簿推送, 包含RPI報價數據

### 檔位

**現貨 & 期貨:**  
50檔深度, 推送頻率: **100ms**  


**Topic:**  
`orderbook.rpi.{symbol}` e.g., orderbook.rpi.BTCUSDT

### 響應參數

參數| 類型| 說明  
---|---|---  
topic| string| Topic名  
type| string| 數據類型. `snapshot`,`delta`  
ts| number| 行情服務生成數據的時間戳 (毫秒)  
data| map| Object  
> s| string| 合約名稱  
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

  
> u| integer| 更新id 

  * 一般情況下該id是連續的。偶爾會因後台的重啟而發送"u"=1的全量數據，接收到後請覆蓋本地保存的orderbook

  
> seq| integer| 撮合版本號 

  * 該字段可以用於關聯不同檔位的orderbook, 如果值越小, 則說明數據生成越早

  
cts| number| 產生此訂單簿數據時來自撮合引擎的時間戳. 可用於與[平台成交](/docs/zh-TW/v5/websocket/public/trade)頻道中的`T`進行關聯  
  
### 訂閱示例

  * JSON
  * Python


    
    
    {  
        "op": "subscribe",  
        "args": [  
            "orderbook.rpi.BTCUSDT"  
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
    ws.rpi_orderbook_stream(  
        symbol="BTCUSDT",  
        callback=handle_message  
    )  
    while True:  
        sleep(1)  
    

### 訂閱成功響應
    
    
    {  
        "success": true,  
        "ret_msg": "subscribe",  
        "conn_id": "f6b17b77-48b6-4c5c-b5ec-4a1c733f5763",  
        "op": "subscribe"  
    }  
    

### 消息示例
    
    
    {  
        "topic": "orderbook.rpi.BTCUSDT",  
        "ts": 1752472188075,  
        "type": "delta",  
        "data": {  
            "s": "BTCUSDT",  
            "b": [  
                [  
                    "121975.1",  
                    "0.114259",  
                    "0"  
                ],  
                [  
                    "121969.9",  
                    "0",  
                    "0"  
                ],  
                [  
                    "121960.5",  
                    "0",  
                    "0.163986"  
                ]  
            ],  
            "a": [  
                [  
                    "121990.8",  
                    "0.441585",  
                    "0.78821"  
                ],  
                [  
                    "121996.1",  
                    "0.016393",  
                    "0"  
                ],  
                [  
                    "122018.5",  
                    "0",  
                    "0"  
                ]  
            ],  
            "u": 2258980,  
            "seq": 79683241099  
        },  
        "cts": 1752472188067  
    }