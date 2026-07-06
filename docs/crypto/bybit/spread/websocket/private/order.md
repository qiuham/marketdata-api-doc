---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/spread/websocket/private/order
api_type: WebSocket
updated_at: 2026-07-06 19:31:10.514960
---

# Orderbook

Subscribe to the spread orderbook stream.

### Depths

Level 25 data, push frequency: **20ms**

**Topic:**  
`orderbook.{depth}.{symbol}` e.g., orderbook.25.SOLUSDT_SOL/USDT

### Process snapshot/delta

To process `snapshot` and `delta` messages, please follow these rules:

Once you have subscribed successfully, you will receive a `snapshot`. The WebSocket will keep pushing `delta` messages every time the orderbook changes. If you receive a new `snapshot` message, you will have to reset your local orderbook. If there is a problem on Bybit's end, a `snapshot` will be re-sent, which is guaranteed to contain the latest data.

To apply `delta` updates:

  * If you receive an amount that is `0`, delete the entry
  * If you receive an amount that does not exist, insert it
  * If the entry exists, you simply update the value



See working code examples of this logic in the [FAQ](https://bybit-exchange.github.io/docs/faq#how-can-i-process-websocket-snapshot-and-delta-messages).

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
>> b[1]| string| Bid size 

  * The delta data has size=0, which means that all quotations for this price have been filled or cancelled

  
> a| array| Asks. For `snapshot` stream. Sorted by price in ascending order  
>> a[0]| string| Ask price  
>> a[1]| string| Ask size 

  * The delta data has size=0, which means that all quotations for this price have been filled or cancelled

  
> u| integer| Update ID

  * Occasionally, you'll receive "u"=1, which is a snapshot data due to the restart of the service. So please overwrite your local orderbook

  
> seq| integer| Cross sequence  
cts| number| The timestamp from the matching engine when this orderbook data is produced. It can be correlated with `T` from [public trade channel](/docs/v5/spread/websocket/public/trade)  
  
### Subscribe Example
    
    
    {  
        "op": "subscribe",  
        "args": ["orderbook.25.SOLUSDT_SOL/USDT"]  
    }  
    

### Event Example
    
    
    {  
        "topic": "orderbook.25.SOLUSDT_SOL/USDT",  
        "ts": 1744165512257,  
        "type": "delta",  
        "data": {  
            "s": "SOLUSDT_SOL/USDT",  
            "b": [],  
            "a": [  
                [  
                    "22.3755",  
                    "4.7"  
                ]  
            ],  
            "u": 64892,  
            "seq": 299084  
        },  
        "cts": 1744165512234  
    }

---

# 深度

訂閱深度的推送

**Topic:**  
`orderbook.{depth}.{symbol}` e.g., orderbook.25.SOLUSDT_SOL/USDT

25 檔數據, 推送頻率: **20ms**

信息

  * 訂閱成功後，會立即得到一個當前快照包的推送消息.
  * websocket將會繼續推送這些增量數據. 收到snapshot的報文，就需要重置本地的orderbook.
  * `snapshot`=全量orderbook, `delta`=增量orderbook
  * 如果因為Bybit服務原因，會重新發送snapshot報文，該報文已保證是最新且準確的.



### 響應參數

參數| 類型| 說明  
---|---|---  
topic| string| Topic名  
type| string| 數據類型. `snapshot`,`delta`  
ts| number| 行情服務生成數據的時間戳 (毫秒)  
data| map| Object  
> s| string| 價差產品名稱  
> b| array| Bid, 買方. `snapshot`數據，是按照價格從大到小  
>> b[0]| string| 買方報價  
>> b[1]| string| 買方數量 

  * 增量數據的推送當出現size=0時，這意味著該價位的報價單全部成交或者全部撤銷

  
> a| array| Ask, 賣方. `snapshot`數據，是按照價格從小到大  
>> a[0]| string| 賣方報價  
>> a[1]| string| 賣方數量 

  * 增量數據的推送當出現size=0時，這意味著該價位的報價單全部成交或者全部撤銷

  
> u| integer| 更新id 

  * 一般情況下該id是連續的。偶爾會因後台的重啟而發送"u"=1的全量數據，接收到後請覆蓋本地保存的orderbook

  
> seq| integer| 撮合版本號  
cts| number| 產生此訂單簿數據時來自撮合引擎的時間戳. 可用於與[平台成交](/docs/zh-TW/v5/spread/websocket/public/trade)頻道中的`T`進行關聯  
  
### 訂閱示例
    
    
    {  
        "op": "subscribe",  
        "args": ["orderbook.25.SOLUSDT_SOL/USDT"]  
    }  
    

### 推送示例
    
    
    {  
        "topic": "orderbook.25.SOLUSDT_SOL/USDT",  
        "ts": 1744165512257,  
        "type": "delta",  
        "data": {  
            "s": "SOLUSDT_SOL/USDT",  
            "b": [],  
            "a": [  
                [  
                    "22.3755",  
                    "4.7"  
                ]  
            ],  
            "u": 64892,  
            "seq": 299084  
        },  
        "cts": 1744165512234  
    }