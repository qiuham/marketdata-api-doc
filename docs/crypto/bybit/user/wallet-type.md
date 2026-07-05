---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/user/wallet-type
api_type: REST
updated_at: 2026-07-05 19:12:51.888663
---

# Dcp

Subscribe to the dcp stream to trigger DCP function.

For example, connection A subscribes "dcp.xxx", connection B does not and connection C subscribes "dcp.xxx".

  1. If A is alive, B is dead, C is alive, then this case will not trigger DCP.
  2. If A is alive, B is dead, C is dead, then this case will not trigger DCP.
  3. If A is dead, B is alive, C is dead, then DCP is triggered when reach the timeWindow threshold



To sum up, for those private connections subscribing "dcp" topic are all dead, then DCP will be triggered.

**Topic:** `dcp.future`, `dcp.spot`, `dcp.option`

### Subscribe Example
    
    
    {  
        "op": "subscribe",  
        "args": [  
            "dcp.future"  
        ]  
    }

---

# 斷線保護 (期權)

通過訂閱DCP流來觸發功能

**舉例:** 私有連接A訂閱了"dcp.xxx", 私有連接B沒有訂閱"dcp.xxx", 私有連接C訂閱了"dcp.xxx".

  1. 如果連接A在線, 連接B斷線, 連接C在線, 那麼這種情況下不會觸發DCP功能.
  2. 如果連接A在線, 連接B斷線, 連接C斷線, 那麼這種情況下不會觸發DCP功能.
  3. 如果連接A斷線, 連接B在線, 連接C斷線, 那麼這種情況下就會當達到時間窗口的閾值後觸發斷線保護機制.



綜上, 只有當所有訂閱了"dcp.xxx"的私有連接斷線後, 斷線保護機制才會被觸發.

**Topic:** `dcp.future`, `dcp.spot`, `dcp.option`

### 訂閱示例
    
    
    {  
        "op": "subscribe",  
        "args": [  
            "dcp.future"  
        ]  
    }