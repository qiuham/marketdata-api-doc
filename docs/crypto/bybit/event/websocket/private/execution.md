---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/event/websocket/private/execution
api_type: WebSocket
updated_at: 2026-11-11 18:28:42.983359
---

# Trade

Subscribe to the Event Contract public trade stream. Pushed in real-time after each trade.

Push frequency: **real-time**

**Topic:**  
`publicTrade.{symbol}` e.g., `publicTrade.ETHUSDT-28AUG26-2450-2570-OUT`

### Response Parameters

Parameter| Type| Comments  
---|---|---  
topic| string| Topic name  
type| string| Data type: `snapshot`  
ts| number| Timestamp (ms) when the system generates the data  
data| array| Object. Sorted by trade time in ascending order.  
> T| number| Timestamp (ms) when the order is filled  
> s| string| Symbol name  
> r| string| Payout ratio (trade price)  
> a| string| Trade amount (order value)  
> i| string| Trade ID  
> seq| integer| Cross sequence  
  
### Subscribe Example
    
    
    {  
        "op": "subscribe",  
        "args": [  
            "publicTrade.ETHUSDT-28AUG26-2450-2570-OUT"  
        ]  
    }  
    

### Response Example
    
    
    {  
        "topic": "publicTrade.ETHUSDT-28AUG26-2450-2570-OUT",  
        "ts": 1787794797536,  
        "type": "snapshot",  
        "data": [  
            {  
                "T": 1787794797534,  
                "s": "ETHUSDT-28AUG26-2450-2570-OUT",  
                "r": "3.5",  
                "a": "100",  
                "i": "ea89cadf-6471-5fd4-8248-20b470d8478b",  
                "seq": 49139  
            }  
        ]  
    }

---

# 成交

訂閱 Event Contract 公共成交數據流，每筆成交實時推送。

推送頻率：**實時**

**Topic：**  
`publicTrade.{symbol}`，如 `publicTrade.ETHUSDT-28AUG26-2450-2570-OUT`

### 返回參數

參數| 類型| 說明  
---|---|---  
topic| string| Topic 名稱  
type| string| 數據類型：`snapshot`  
ts| number| 系統生成數據的時間戳（毫秒）  
data| array| 對象，按成交時間升序排列  
> T| number| 訂單成交時間戳（毫秒）  
> s| string| 交易對名稱  
> r| string| 賠付比率（成交價格）  
> a| string| 成交金額（訂單金額）  
> i| string| 成交 ID  
> seq| integer| 跨業務序號  
  
### 訂閱示例
    
    
    {  
        "op": "subscribe",  
        "args": [  
            "publicTrade.ETHUSDT-28AUG26-2450-2570-OUT"  
        ]  
    }  
    

### 推送示例
    
    
    {  
        "topic": "publicTrade.ETHUSDT-28AUG26-2450-2570-OUT",  
        "ts": 1787794797536,  
        "type": "snapshot",  
        "data": [  
            {  
                "T": 1787794797534,  
                "s": "ETHUSDT-28AUG26-2450-2570-OUT",  
                "r": "3.5",  
                "a": "100",  
                "i": "ea89cadf-6471-5fd4-8248-20b470d8478b",  
                "seq": 49139  
            }  
        ]  
    }