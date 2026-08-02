---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/websocket/public/kline
api_type: WebSocket
updated_at: 2026-08-02 18:55:10.896389
---

# Orderbook

Subscribe to the orderbook stream. Supports different depths.

info

[Retail Price Improvement (RPI)](https://www.bybit.com/en/help-center/article/Retail-Price-Improvement-RPI-Order) orders will not be included in the messages.

### Depths

**Linear & inverse:**  
Level 1 data, push frequency: **10ms**  
Level 50 data, push frequency: **20ms**  
Level 200 data, push frequency: **100ms**  
Level 1000 data, push frequency: **200ms**  


**Spot:**  
Level 1 data, push frequency: **10ms**  
Level 50 data, push frequency: **20ms**  
Level 200 data, push frequency: **100ms**  
Level 1000 data, push frequency: **200ms**  


**Option:**  
Level 25 data, push frequency: **20ms**  
Level 100 data, push frequency: **100ms**  


**Topic:**  
`orderbook.{depth}.{symbol}` e.g., orderbook.1.BTCUSDT

### Process snapshot/delta

To process `snapshot` and `delta` messages, please follow these rules:

Once you have subscribed successfully, you will receive a `snapshot`. The WebSocket will keep pushing `delta` messages every time the orderbook changes. If you receive a new `snapshot` message, you will have to reset your local orderbook. If there is a problem on Bybit's end, a `snapshot` will be re-sent, which is guaranteed to contain the latest data.

To apply `delta` updates:

  * If you receive an amount that is `0`, delete the entry
  * If you receive an amount that does not exist, insert it
  * If the entry exists, you simply update the value



See working code examples of this logic in the [FAQ](https://bybit-exchange.github.io/docs/faq#how-can-i-process-websocket-snapshot-and-delta-messages).

info

  * Linear, inverse, spot level 1 data: if 3 seconds have elapsed without a change in the orderbook, a `snapshot` message will be pushed again, and the field `u` will be the same as that in the previous message.
  * **Linear, inverse, spot level 1 data has`snapshot` message only**
  * **PreLaunch contracts** : there is no feed until `ContinuousTrading` stage



reminder

  * Spot (all levels) & Futures (Level 1): the "ts" field appears **before** the "type" field in the JSON message, e.g., `{"toptic": "orderbook.1.BTCUSDT", "ts": "1772694601512", "type": "snapshot", ...}`
  * Futures (all other levels): the "ts" field appears **after** the "type" field in the JSON message, e.g., `{"toptic": "orderbook.50.BTCUSDT", "type": "delta", "ts": "1772694601512", ...}`



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
  * For level 1 of linear, inverse Perps and Futures, the snapshot data will be pushed again when there is no change in 3 seconds, and the "u" will be the same as that in the previous message

  
> seq| integer| Cross sequence 

  * You can use this field to compare different levels orderbook data, and for the smaller seq, then it means the data is generated earlier. 

  
cts| number| The timestamp from the matching engine when this orderbook data is produced. It can be correlated with `T` from [public trade channel](/docs/v5/websocket/public/trade)  
  
### Subscribe Example
    
    
    from pybit.unified_trading import WebSocket  
    from time import sleep  
    ws = WebSocket(  
        testnet=True,  
        channel_type="linear",  
    )  
    def handle_message(message):  
        print(message)  
    ws.orderbook_stream(  
        depth=50,  
        symbol="BTCUSDT",  
        callback=handle_message  
    )  
    while True:  
        sleep(1)  
    

### Response Example

  * Snapshot
  * Delta


    
    
    {  
        "topic": "orderbook.50.BTCUSDT",  
        "type": "snapshot",  
        "ts": 1672304484978,  
        "data": {  
            "s": "BTCUSDT",  
            "b": [  
                ...,  
                [  
                    "16493.50",  
                    "0.006"  
                ],  
                [  
                    "16493.00",  
                    "0.100"  
                ]  
            ],  
            "a": [  
                [  
                    "16611.00",  
                    "0.029"  
                ],  
                [  
                    "16612.00",  
                    "0.213"  
                ],  
                ...,  
            ],  
        "u": 18521288,  
        "seq": 7961638724  
        },  
        "cts": 1672304484976  
    }  
    
    
    
    {  
        "topic": "orderbook.50.BTCUSDT",  
        "type": "delta",  
        "ts": 1687940967466,  
        "data": {  
            "s": "BTCUSDT",  
            "b": [  
                [  
                    "30247.20",  
                    "30.028"  
                ],  
                [  
                    "30245.40",  
                    "0.224"  
                ],  
                [  
                    "30242.10",  
                    "1.593"  
                ],  
                [  
                    "30240.30",  
                    "1.305"  
                ],  
                [  
                    "30240.00",  
                    "0"  
                ]  
            ],  
            "a": [  
                [  
                    "30248.70",  
                    "0"  
                ],  
                [  
                    "30249.30",  
                    "0.892"  
                ],  
                [  
                    "30249.50",  
                    "1.778"  
                ],  
                [  
                    "30249.60",  
                    "0"  
                ],  
                [  
                    "30251.90",  
                    "2.947"  
                ],  
                [  
                    "30252.20",  
                    "0.659"  
                ],  
                [  
                    "30252.50",  
                    "4.591"  
                ]  
            ],  
            "u": 177400507,  
            "seq": 66544703342  
        },  
        "cts": 1687940967464  
    }

---

# 深度

訂閱不同深度的推送

提示

  * 訂閱成功後，會立即得到一個當前快照包的推送消息.
  * websocket將會繼續推送這些增量數據. 收到snapshot的報文，就需要重置本地的orderbook.
  * `snapshot`=全量orderbook, `delta`=增量orderbook
  * 如果因為Bybit服務原因，會重新發送snapshot報文，該報文已保證是最新且準確的.



信息

  * USDT合約, USDC合約, 反向合約以及現貨 1檔數據: 若3秒內無變化, 將會再次推送**snapshot** 數據, 此消息中的字段`u`和前一條消息裡的“u”保持一樣
  * **USDT合約, USDC合約, 反向合約以及現貨 1檔數據: 只推送`snapshot`消息**
  * **盤前合約** : 直到`ContinuousTrading`(連續競價)階段, orderbook數據才會下發



提醒

  * 現貨所有檔位 & 合約1檔: 在收到的JSON消息中, "ts" 字段出現在"type"字段之**前** , 例如, `{"toptic": "orderbook.1.BTCUSDT", "ts": "1772694601512", "type": "snapshot", ...}`
  * 合約其他檔位: 在收到的JSON消息中, "ts" 字段出現在"type"字段之**後** , 例如, `{"toptic": "orderbook.50.BTCUSDT", "type": "delta", "ts": "1772694601512", ...}`



**USDT合約和USDC合約 & 反向合約:**  
1 檔數據, 推送頻率: **10ms**  
50 檔數據, 推送頻率: **20ms**  
200 檔數據, 推送頻率: **100ms**  
1000 檔數據, 推送頻率: **200ms**  


**現貨:**  
1 檔數據, 推送頻率: **10ms**  
50 檔數據, 推送頻率: **20ms**  
200 檔數據, 推送頻率: **100ms**  
1000 檔數據, 推送頻率: **200ms**  


**期權:**  
25 檔數據, 推送頻率: **20ms**  
100 檔數據, 推送頻率: **100ms**  


**Topic:**  
`orderbook.{depth}.{symbol}` e.g., orderbook.1.BTCUSDT

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
>> b[1]| string| 買方數量 

  * 增量數據的推送當出現size=0時，這意味著該價位的報價單全部成交或者全部撤銷

  
> a| array| Ask, 賣方. `snapshot`數據，是按照價格從小到大  
>> a[0]| string| 賣方報價  
>> a[1]| string| 賣方數量 

  * 增量數據的推送當出現size=0時，這意味著該價位的報價單全部成交或者全部撤銷

  
> u| integer| 更新id 

  * 一般情況下該id是連續的。偶爾會因後台的重啟而發送"u"=1的全量數據，接收到後請覆蓋本地保存的orderbook
  * 對於期貨的1檔推送, 3秒內無變化, 則會強推一個snapshot數據, 此消息裡的"u"的值和前一條消息裡的保持一致

  
> seq| integer| 撮合版本號 

  * 該字段可以用於關聯不同檔位的orderbook, 如果值越小, 則說明數據生成越早

  
cts| number| 產生此訂單簿數據時來自撮合引擎的時間戳. 可用於與[平台成交](/docs/zh-TW/v5/websocket/public/trade)頻道中的`T`進行關聯  
  
### 訂閱示例
    
    
    from pybit.unified_trading import WebSocket  
    from time import sleep  
    ws = WebSocket(  
        testnet=True,  
        channel_type="linear",  
    )  
    def handle_message(message):  
        print(message)  
    ws.orderbook_stream(  
        depth=50,  
        symbol="BTCUSDT",  
        callback=handle_message  
    )  
    while True:  
        sleep(1)  
    

### 響應示例

  * 全量
  * 增量


    
    
    {  
        "topic": "orderbook.50.BTCUSDT",  
        "type": "snapshot",  
        "ts": 1672304484978,  
        "data": {  
            "s": "BTCUSDT",  
            "b": [  
                ...,  
                [  
                    "16493.50",  
                    "0.006"  
                ],  
                [  
                    "16493.00",  
                    "0.100"  
                ]  
            ],  
            "a": [  
                [  
                    "16611.00",  
                    "0.029"  
                ],  
                [  
                    "16612.00",  
                    "0.213"  
                ],  
                ...,  
            ],  
        "u": 18521288,  
        "seq": 7961638724  
        }  
        "cts": 1672304484976  
    }  
    
    
    
    {  
        "topic": "orderbook.50.BTCUSDT",  
        "type": "delta",  
        "ts": 1687940967466,  
        "data": {  
            "s": "BTCUSDT",  
            "b": [  
                [  
                    "30247.20",  
                    "30.028"  
                ],  
                [  
                    "30245.40",  
                    "0.224"  
                ],  
                [  
                    "30242.10",  
                    "1.593"  
                ],  
                [  
                    "30240.30",  
                    "1.305"  
                ],  
                [  
                    "30240.00",  
                    "0"  
                ]  
            ],  
            "a": [  
                [  
                    "30248.70",  
                    "0"  
                ],  
                [  
                    "30248.90",  
                    "3.525"  
                ],  
                [  
                    "30249.00",  
                    "2.327"  
                ],  
                [  
                    "30249.60",  
                    "0"  
                ],  
                [  
                    "30249.80",  
                    "2.178"  
                ],  
                [  
                    "30249.90",  
                    "4.685"  
                ],  
                [  
                    "30250.00",  
                    "9.907"  
                ],  
                [  
                    "30250.10",  
                    "1.070"  
                ],  
                [  
                    "30251.60",  
                    "2.239"  
                ],  
                [  
                    "30251.90",  
                    "2.947"  
                ],  
                [  
                    "30252.20",  
                    "0.659"  
                ],  
                [  
                    "30252.50",  
                    "4.591"  
                ]  
            ],  
            "u": 177400507,  
            "seq": 66544703342  
        }  
        "cts": 1687940967464  
    }