---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/websocket/private/position
api_type: WebSocket
updated_at: 2026-07-18 19:09:39.888548
---

# ADL Alert

Subscribe to ADL alerts and insurance pool information.

> **Covers: USDT Perpetual / USDT Delivery / USDC Perpetual / USDC Delivery / Inverse Contracts**

Push frequency: **1s**

**Topic:**  
`adlAlert.{coin}`

Available filters:

  * `adlAlert.USDT` for USDT Perpetual/Delivery
  * `adlAlert.USDC` for USDC Perpetual/Delivery
  * `adlAlert.inverse` for Inverse contracts.



For more information on how ADL is triggered, see the [ADL endpoint](/docs/v5/market/adl-alert).

### Response Parameters

Parameter| Type| Comments  
---|---|---  
list| array| Object  
> c| string| Token of the insurance pool  
> s| string| Trading pair name  
> b| string| Balance of the insurance fund. Used to determine if ADL is triggered. For shared insurance pool, the "b" field will follow a T+1 refresh mechanism and will be updated daily at 00:00 UTC.  
> mb| string| Deprecated, always return "". Maximum balance of the insurance pool in the last 8 hours  
> i_pr| string| PnL ratio threshold for triggering **contract PnL drawdown ADL**

  * ADL is triggered when the symbol's PnL drawdown ratio in the last 8 hours exceeds this value

  
> pr| string| Symbol's PnL drawdown ratio in the last 8 hours. Used to determine whether ADL is triggered or stopped  
> adl_tt| string| Trigger threshold for **contract PnL drawdown ADL**

  * This condition is only effective when the insurance pool balance is greater than this value; if so, an 8 hours drawdown exceeding n% may trigger ADL

  
> adl_sr| string| Stop ratio threshold for **contract PnL drawdown ADL**

  * ADL stops when the symbol's 8 hours drawdown ratio falls below this value

  
  
### Subscribe Example
    
    
    {"op": "subscribe", "args": ["adlAlert.USDT"]}  
    

### Response Example
    
    
    {  
      "topic": "adlAlert.USDT",  
      "type": "snapshot",  
      "ts": 1757736794000,  
      "data": [  
        {  
          "c": "USDT",  
          "s": "FWOGUSDT",  
          "b": -5421.29889888,  
          "mb": -5421.29889888,  
          "i_pr": -0.3,  
          "pr": 0,  
          "adl_tt": 10000,  
          "adl_sr": -0.25  
        },  
        {  
          "c": "USDT",  
          "s": "ZORAUSDT",  
          "b": 19873.46255153,  
          "mb": 19874.97612833,  
          "i_pr": -0.3,  
          "pr": 0.000174,  
          "adl_tt": 10000,  
          "adl_sr": -0.25  
        },  
        {  
          "c": "USDT",  
          "s": "BERAUSDT",  
          "b": 453.36427074,  
          "mb": 453.36427074,  
          "i_pr": -0.3,  
          "pr": 0.24576,  
          "adl_tt": 10000,  
          "adl_sr": -0.25  
        },  
        ...,  
      ]  
    }

---

# ADL告警

訂閱按組劃分保險池 ADL 告警及相關資訊

> **覆蓋範圍：USDT 永續 / USDT 交割 / USDC 永續 / USDC 交割 / 反向合約**

推送頻率: **1秒**

**Topic:**  
`adlAlert.{coin}`

可用類型為:

  * `adlAlert.USDT` 用於USDT 永續、交割
  * `adlAlert.USDC` 用於USDC 永續、交割
  * `adlAlert.inverse` 用於反向合約



規則詳情請參考 [查詢ADL告警](/docs/zh-TW/v5/market/adl-alert)

### 響應參數

參數| 類型| 說明  
---|---|---  
list| array| Object  
> c| string| 保險池所屬幣種  
> s| string| 交易對名稱  
> b| string| 保險基金餘額，用於判斷是否觸發 ADL。對於共用保險池，balance 將採用 T+1 刷新機制，並於每日 UTC 時間 00:00 更新。  
> mb| string| 被棄用，並將傳回空字串。最近 8 小時內的保險池最大餘額  
> i_pr| string| 觸發 **合約盈虧回撤 ADL** 的盈虧比例閾值 

  * 當 symbol 在 8 小時內的盈虧回撤比例大於該值時，觸發 ADL

  
> pr| string| symbol 在 8 小時內的回撤比例，用於判斷 ADL 是否觸發或停止  
> adl_tt| string| **合約盈虧回撤 ADL** 的觸發閾值 

  * 僅當保險池餘額大於該值時，8 小時內回撤 n% 的觸發條件才會生效

  
> adl_sr| string| **合約盈虧回撤 ADL** 的停止比例閾值 

  * 當 symbol 在 8 小時內的回撤比例小於該值時，ADL 停止

  
  
### 訂閱示例
    
    
    {"op": "subscribe", "args": ["adlAlert.USDT"]}  
    

### 響應示例
    
    
    {  
      "topic": "adlAlert.USDT",  
      "type": "snapshot",  
      "ts": 1757736794000,  
      "data": [  
        {  
          "c": "USDT",  
          "s": "FWOGUSDT",  
          "b": -5421.29889888,  
          "mb": -5421.29889888,  
          "i_pr": -0.3,  
          "pr": 0,  
          "adl_tt": 10000,  
          "adl_sr": -0.25  
        },  
        {  
          "c": "USDT",  
          "s": "ZORAUSDT",  
          "b": 19873.46255153,  
          "mb": 19874.97612833,  
          "i_pr": -0.3,  
          "pr": 0.000174,  
          "adl_tt": 10000,  
          "adl_sr": -0.25  
        },  
        {  
          "c": "USDT",  
          "s": "BERAUSDT",  
          "b": 453.36427074,  
          "mb": 453.36427074,  
          "i_pr": -0.3,  
          "pr": 0.24576,  
          "adl_tt": 10000,  
          "adl_sr": -0.25  
        },  
        ...,  
      ]  
    }