---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/spread/websocket/private/order
api_type: WebSocket
updated_at: 2026-07-01 19:32:39.945970
---

# Trade

Subscribe to the public trades stream.

After subscription, you will be pushed trade messages in real-time.

Push frequency: **real-time**

**Topic:**  
`publicTrade.{symbol}`

### Response Parameters

Parameter| Type| Comments  
---|---|---  
topic| string| Topic name  
type| string| Data type. `snapshot`  
ts| number| The timestamp (ms) that the system generates the data  
data| array| Object. Sorted by the time the trade was matched in ascending order  
> T| number| The timestamp (ms) that the order is filled  
> s| string| Symbol name  
> S| string| Side of taker. `Buy`,`Sell`  
> v| string| Trade size  
> p| string| Trade price  
> [L](/docs/v5/enum#tickdirection)| string| Direction of price change  
> i| string| Trade ID  
> seq| integer| Cross sequence  
  
### Subscribe Example
    
    
    {  
        "op": "subscribe",  
        "id": "test-001-perp",  
        "args": [  
            "publicTrade.SOLUSDT_SOL/USDT"  
        ]  
    }  
    

### Response Example
    
    
    {  
        "topic": "publicTrade.SOLUSDT_SOL/USDT",  
        "ts": 1744170142723,  
        "type": "snapshot",  
        "data": [  
            {  
                "T": 1744170142720,  
                "s": "SOLUSDT_SOL/USDT",  
                "S": "Sell",  
                "v": "2.5",  
                "p": "19.3928",  
                "L": "MinusTick",  
                "i": "31d0fc58-933b-57b3-8378-f73da06da843",  
                "seq": 1783284617  
            }  
        ]  
    }

---

# 平台成交

訂閱Bybit平台上價差交易最近成交的推送.  
從用戶訂閱開始, 實時推送增量交易歷史, 有成交數據就推送.

推送頻率: **real-time**

**Topic:**  
`publicTrade.{symbol}`  


### 響應參數

參數| 類型| 說明  
---|---|---  
topic| string| Topic名  
type| string| 數據類型. `snapshot`  
ts| number| 行情服務生成數據的時間戳 (毫秒)  
data| array| Object. 如有多條, 則數組中的元素按照匹配時間升序排序  
> T| number| 成交時間戳 (毫秒)  
> s| array| 合約名稱  
> S| string| 吃單方向. `Buy`,`Sell`  
> v| string| 成交數量  
> p| string| 成交價格  
> [L](/docs/zh-TW/v5/enum#tickdirection)| string| 價格變化的方向. _期權沒有該字段_  
> i| string| 成交Id  
> seq| integer| 撮合版本號  
  
### 訂閱示例
    
    
    {  
        "op": "subscribe",  
        "id": "test-001-perp",  
        "args": [  
            "publicTrade.SOLUSDT_SOL/USDT"  
        ]  
    }  
    

### 推送示例
    
    
    {  
        "topic": "publicTrade.SOLUSDT_SOL/USDT",  
        "ts": 1744170142723,  
        "type": "snapshot",  
        "data": [  
            {  
                "T": 1744170142720,  
                "s": "SOLUSDT_SOL/USDT",  
                "S": "Sell",  
                "v": "2.5",  
                "p": "19.3928",  
                "L": "MinusTick",  
                "i": "31d0fc58-933b-57b3-8378-f73da06da843",  
                "seq": 1783284617  
            }  
        ]  
    }