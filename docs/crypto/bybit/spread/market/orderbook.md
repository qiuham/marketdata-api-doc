---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/spread/market/orderbook
api_type: Market Data
updated_at: 2026-10-19 18:54:22.167608
---

# Get Tickers

Query for the latest price snapshot, best bid/ask price, and trading volume of different spread combinations in the last 24 hours.

info

  * During periods of extreme market volatility, this interface may experience increased latency or temporary delays in data delivery



### HTTP Request

GET`/v5/spread/tickers`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
symbol| **true**|  string| Spread combination symbol name  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
list| array<object>| Ticker info  
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
  
### Request Example

  * HTTP
  * Python


    
    
    GET /v5/spread/tickers?symbol=SOLUSDT_SOL/USDT HTTP/1.1  
    Host: api-testnet.bybit.com  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.spread_get_tickers(  
        symbol="SOLUSDT_SOL/USDT"  
    ))  
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "Success",  
        "result": {  
            "list": [  
                {  
                    "symbol": "SOLUSDT_SOL/USDT",  
                    "bidPrice": "",  
                    "bidSize": "",  
                    "askPrice": "",  
                    "askSize": "",  
                    "lastPrice": "19.444",  
                    "highPrice24h": "23.8353",  
                    "lowPrice24h": "0",  
                    "prevPrice24h": "20",  
                    "volume24h": "24694.9"  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1744079413254  
    }

---

# 查詢最新行情信息

可獲取到快照的最新市場價格，最佳買賣價格，以及過去時間內的交易量等.

警告

  * 在極端市場波動期間, 此介面可能會出現延遲增加或資料傳遞暫時延遲的情況



### HTTP請求

GET`/v5/spread/tickers`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
symbol| **true**|  string| 價差產品名稱  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
list| array<object>| 行情信息  
> symbol| string| 價差產品名稱  
> bidPrice| string| 買1價  
> bidSize| string| 買1價的數量  
> askPrice| string| 賣1價  
> askSize| string| 賣1價的數量  
> lastPrice| string| 最新市場成交價  
> highPrice24h| string| 最近24小時的最高價  
> lowPrice24h| string| 最近24小時的最低價  
> prevPrice24h| string| 24小時前的整點市價  
> volume24h| string| 最近24小時成交量  
  
### 請求示例
    
    
    GET /v5/spread/tickers?symbol=SOLUSDT_SOL/USDT HTTP/1.1  
    Host: api-testnet.bybit.com  
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "Success",  
        "result": {  
            "list": [  
                {  
                    "symbol": "SOLUSDT_SOL/USDT",  
                    "bidPrice": "",  
                    "bidSize": "",  
                    "askPrice": "",  
                    "askSize": "",  
                    "lastPrice": "19.444",  
                    "highPrice24h": "23.8353",  
                    "lowPrice24h": "0",  
                    "prevPrice24h": "20",  
                    "volume24h": "24694.9"  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1744079413254  
    }