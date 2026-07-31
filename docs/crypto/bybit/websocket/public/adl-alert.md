---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/websocket/public/adl-alert
api_type: WebSocket
updated_at: 2026-07-31 19:03:48.590383
---

# All Liquidation

Subscribe to the liquidation stream, push all liquidations that occur on Bybit.

> **Covers: USDT contract / USDC contract / Inverse contract**

Push frequency: **500ms**

**Topic:**  
`allLiquidation.{symbol}` e.g., allLiquidation.BTCUSDT

### Response Parameters

Parameter| Type| Comments  
---|---|---  
topic| string| Topic name  
type| string| Data type. `snapshot`  
ts| number| The timestamp (ms) that the system generates the data  
data| Object|   
> T| number| The updated timestamp (ms)  
> s| string| Symbol name  
> S| string| Position side. `Buy`,`Sell`. When you receive a `Buy` update, this means that a long position has been liquidated  
> v| string| Executed size  
> p| string| [Bankruptcy price](https://www.bybit.com/en-US/help-center/s/article/Bankruptcy-Price-USDT-Contract)  
  
### Subscribe Example
    
    
    from pybit.unified_trading import WebSocket  
    from time import sleep  
    ws = WebSocket(  
        testnet=True,  
        channel_type="linear",  
    )  
    def handle_message(message):  
        print(message)  
    ws.all_liquidation_stream("ROSEUSDT", handle_message)  
    while True:  
        sleep(1)  
    

### Response Example
    
    
    {  
        "topic": "allLiquidation.ROSEUSDT",  
        "type": "snapshot",  
        "ts": 1739502303204,  
        "data": [  
            {  
                "T": 1739502302929,  
                "s": "ROSEUSDT",  
                "S": "Sell",  
                "v": "20000",  
                "p": "0.04499"  
            }  
        ]  
    }

---

# 完整強平推送

訂閱Bybit平台上的強平推送

> **覆蓋範圍: USDT永續 / USDT交割 / USDC永續 / USDC交割 / 反向合約**

推送頻率: **500毫秒**

**Topic:**  
`allLiquidation.{symbol}` e.g., allLiquidation.BTCUSDT

### 響應參數

參數| 類型| 說明  
---|---|---  
topic| string| Topic名  
type| string| 數據類型. `snapshot`  
ts| number| 行情服務生成數據的時間戳 (毫秒)  
data| Object|   
> T| number| 數據更新時間戳 (毫秒)  
> s| string| 合約名稱  
> S| string| 被平的倉位方向. `Buy`,`Sell`

  * 如果您收到一條Buy的推送更新, 則表明有一個多倉被強平了

  
> v| string| 成交數量  
> p| string| 破產價格  
  
### 訂閱示例
    
    
    from pybit.unified_trading import WebSocket  
    from time import sleep  
    ws = WebSocket(  
        testnet=True,  
        channel_type="linear",  
    )  
    def handle_message(message):  
        print(message)  
    ws.all_liquidation_stream("ROSEUSDT", handle_message)  
    while True:  
        sleep(1)  
    

### 消息示例
    
    
    {  
        "topic": "allLiquidation.ROSEUSDT",  
        "type": "snapshot",  
        "ts": 1739502303204,  
        "data": [  
            {  
                "T": 1739502302929,  
                "s": "ROSEUSDT",  
                "S": "Sell",  
                "v": "20000",  
                "p": "0.04499"  
            }  
        ]  
    }