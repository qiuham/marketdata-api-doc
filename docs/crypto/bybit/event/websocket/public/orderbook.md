---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/event/websocket/public/orderbook
api_type: WebSocket
updated_at: 2026-11-13 19:22:39.345089
---

# Orderbook

Subscribe to the Event Contract orderbook stream. Supports **25 levels**.

Push frequency: **20ms**

**Topic:**  
`orderbook.25.{symbol}` e.g., `orderbook.25.ETHUSDT-28AUG26-2450-2570-OUT`

### Process snapshot/delta

Once you have subscribed successfully, you will receive a `snapshot`. The WebSocket will keep pushing `delta` messages every time the orderbook changes. If you receive a new `snapshot` message, you will have to reset your local orderbook.

To apply `delta` updates:

  * If you receive a size of `0`, delete the entry
  * If you receive an entry that does not exist, insert it
  * If the entry exists, update the size



### Response Parameters

Parameter| Type| Comments  
---|---|---  
topic| string| Topic name  
type| string| Data type: `snapshot`, `delta`  
ts| number| Timestamp (ms) when the system generates the data  
data| map| Object  
> s| string| Symbol name  
> r| array| Payout ratio orderbook entries. Up to 25 levels.  
>> r[0]| string| Payout ratio (price)  
>> r[1]| string| Order value (size). Size `0` means the entry should be deleted.  
> u| integer| Update ID. If `u`=1, it is a snapshot caused by a service restart — overwrite your local orderbook.  
> seq| integer| Cross sequence. Smaller seq means earlier data.  
cts| number| Timestamp from the matching engine when this data is produced  
  
### Subscribe Example
    
    
    {  
        "op": "subscribe",  
        "args": [  
            "orderbook.25.ETHUSDT-28AUG26-2450-2570-OUT"  
        ]  
    }  
    

### Response Example

  * Snapshot
  * Delta


    
    
    {  
        "topic": "orderbook.25.ETHUSDT-28AUG26-2450-2570-OUT",  
        "ts": 1787794783020,  
        "type": "snapshot",  
        "data": {  
            "s": "ETHUSDT-28AUG26-2450-2570-OUT",  
            "r": [  
                ["3.5", "14900"],  
                ["2.28", "500"],  
                ["2.07", "500"]  
            ],  
            "u": 702,  
            "seq": 49115  
        },  
        "cts": 1787794647814  
    }  
    
    
    
    {  
        "topic": "orderbook.25.ETHUSDT-28AUG26-2450-2570-OUT",  
        "ts": 1787798930119,  
        "type": "delta",  
        "data": {  
            "s": "ETHUSDT-28AUG26-2450-2570-OUT",  
            "r": [  
                ["2.39", "0"]  
            ],  
            "u": 724,  
            "seq": 50266  
        },  
        "cts": 1787798930117  
    }

---

# 訂單簿

訂閱 Event Contract 訂單簿數據流，支持 **25 檔** 行情。

推送頻率：**20ms**

**Topic：**  
`orderbook.25.{symbol}`，如 `orderbook.25.ETHUSDT-28AUG26-2450-2570-OUT`

### 快照/增量處理說明

訂閱成功後，首先收到 `snapshot` 全量數據。之後每次訂單簿變動，系統推送 `delta` 增量數據。若收到新的 `snapshot`，需重置本地訂單簿。

增量更新規則：

  * 收到 size = `0`：刪除該條目
  * 收到不存在的條目：插入新條目
  * 收到已存在的條目：更新 size



### 返回參數

參數| 類型| 說明  
---|---|---  
topic| string| Topic 名稱  
type| string| 數據類型：`snapshot`、`delta`  
ts| number| 系統生成數據的時間戳（毫秒）  
data| map| 對象  
> s| string| 交易對名稱  
> r| array| 賠付比率訂單簿條目，最多 25 檔  
>> r[0]| string| 賠付比率（價格）  
>> r[1]| string| 訂單金額（數量）。為 `0` 時表示該條目需刪除  
> u| integer| 更新 ID。若 `u`=1，表示服務重啟後的快照，需重置本地訂單簿  
> seq| integer| 跨業務序號，seq 越小說明數據越早生成  
cts| number| 撮合引擎生成此數據的時間戳  
  
### 訂閱示例
    
    
    {  
        "op": "subscribe",  
        "args": [  
            "orderbook.25.ETHUSDT-28AUG26-2450-2570-OUT"  
        ]  
    }  
    

### 推送示例

  * Snapshot
  * Delta


    
    
    {  
        "topic": "orderbook.25.ETHUSDT-28AUG26-2450-2570-OUT",  
        "ts": 1787794783020,  
        "type": "snapshot",  
        "data": {  
            "s": "ETHUSDT-28AUG26-2450-2570-OUT",  
            "r": [  
                ["3.5", "14900"],  
                ["2.28", "500"],  
                ["2.07", "500"]  
            ],  
            "u": 702,  
            "seq": 49115  
        },  
        "cts": 1787794647814  
    }  
    
    
    
    {  
        "topic": "orderbook.25.ETHUSDT-28AUG26-2450-2570-OUT",  
        "ts": 1787798930119,  
        "type": "delta",  
        "data": {  
            "s": "ETHUSDT-28AUG26-2450-2570-OUT",  
            "r": [  
                ["2.39", "0"]  
            ],  
            "u": 724,  
            "seq": 50266  
        },  
        "cts": 1787798930117  
    }