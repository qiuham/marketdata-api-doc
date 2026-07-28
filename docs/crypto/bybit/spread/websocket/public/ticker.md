---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/spread/websocket/public/ticker
api_type: WebSocket
updated_at: 2026-07-28 19:04:56.418077
---

# Ticker

Subscribe to the ticker stream.

Push frequency: **100ms**

**Topic:**  
`tickers.{symbol}`

### Response Parameters

Parameter| Type| Comments  
---|---|---  
topic| string| Topic name  
type| string| Data type. `snapshot`  
ts| number| The timestamp (ms) that the system generates the data  
data| map| Object  
> symbol| string| Spread combination symbol name  
> bidPrice| string| Bid 1 price  
> bidSize| string| Bid 1 size  
> askPrice| string| Ask 1 price  
> askSize| string| Ask 1 size  
> lastPrice| string| Last trade price  
> highPrice24h| string| The highest price in the last 24 hours  
> lowPrice24h| string| The lowest price in the last 24 hours  
> prevPrice24h| string| Price 24 hours ago  
> volume24h| string| Volume for 24h  
  
### Subscribe Example
    
    
    {  
        "op": "subscribe",  
        "args": [  
            "tickers.SOLUSDT_SOL/USDT"  
        ]  
    }  
    

### Event Example
    
    
    {  
        "topic": "tickers.SOLUSDT_SOL/USDT",  
        "ts": 1744168585009,  
        "type": "snapshot",  
        "data": {  
            "symbol": "SOLUSDT_SOL/USDT",  
            "bidPrice": "20.3359",  
            "bidSize": "1.7",  
            "askPrice": "",  
            "askSize": "",  
            "lastPrice": "21.8182",  
            "highPrice24h": "24.2356",  
            "lowPrice24h": "-3",  
            "prevPrice24h": "22.1468",  
            "volume24h": "23309.9"  
        }  
    }

---

# 行情

訂閱行情數據推送

推送頻率: **100ms**

**Topic:**  
`tickers.{symbol}`

### 響應參數

參數| 類型| 說明  
---|---|---  
topic| string| Topic名  
type| string| 數據類型. `snapshot`  
ts| number| 行情服務生成數據的時間戳 (毫秒)  
data| map| Object  
> symbol| string| 價差產品名稱  
> bidPrice| string| 買1價  
> bidSize| string| 買1數量  
> askPrice| string| 賣1價  
> askSize| string| 賣1數量  
> lastPrice| string| 最後成交個價  
> highPrice24h| string| 最近24小時的最高價  
> lowPrice24h| string| 最近24小時的最低價  
> prevPrice24h| string| 24小時前的整點市價  
> volume24h| string| 最近24小時成交量  
  
### 訂閱示例
    
    
    {  
        "op": "subscribe",  
        "args": [  
            "tickers.SOLUSDT_SOL/USDT"  
        ]  
    }  
    

### 推送示例
    
    
    {  
        "topic": "tickers.SOLUSDT_SOL/USDT",  
        "ts": 1744168585009,  
        "type": "snapshot",  
        "data": {  
            "symbol": "SOLUSDT_SOL/USDT",  
            "bidPrice": "20.3359",  
            "bidSize": "1.7",  
            "askPrice": "",  
            "askSize": "",  
            "lastPrice": "21.8182",  
            "highPrice24h": "24.2356",  
            "lowPrice24h": "-3",  
            "prevPrice24h": "22.1468",  
            "volume24h": "23309.9"  
        }  
    }