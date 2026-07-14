---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/spot-margin-uta/tier-collateral-ratio
api_type: REST
updated_at: 2026-07-14 18:57:07.575411
---

# Get Recent Public Trades

Query recent public spread trading history in Bybit.

### HTTP Request

GET`/v5/spread/recent-trade`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
symbol| **true**|  string| Spread combination symbol name  
limit| false| integer| Limit for data size per page [`1`,`1000`], default: `500`  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
list| array<object>| Public trade info  
> execId| string| Execution ID  
> symbol| string| Spread combination symbol name  
> price| string| Trade price  
> size| string| Trade size  
> side| string| Side of taker `Buy`, `Sell`  
> time| string| Trade time (ms)  
> seq| string| Cross sequence  
  
### Request Example

  * HTTP
  * Python


    
    
    GET /v5/spread/recent-trade?symbol=SOLUSDT_SOL/USDT&limit=2 HTTP/1.1  
    Host: api-testnet.bybit.com  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.spread_get_public_trade_history(  
        symbol="SOLUSDT_SOL/USDT",  
        limit=2  
    ))  
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "Success",  
        "result": {  
            "list": [  
                {  
                    "execId": "c8512970-d6fb-5039-93a5-b4196dffbe88",  
                    "symbol": "SOLUSDT_SOL/USDT",  
                    "price": "20.2805",  
                    "size": "3.3",  
                    "side": "Sell",  
                    "time": "1744078324035",  
                    "seq":"123456"  
                },  
                {  
                    "execId": "92b0002e-c49d-5618-a195-4140d7e10a2b",  
                    "symbol": "SOLUSDT_SOL/USDT",  
                    "price": "20.843",  
                    "size": "2.2",  
                    "side": "Buy",  
                    "time": "1744078322010",  
                    "seq":"123450"  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1744078324682  
    }

---

# 查詢最近公共成交

### HTTP請求

GET`/v5/spread/recent-trade`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
symbol| **true**|  string| 價差產品名稱  
limit| false| integer| 每頁數量限制 [1,1000], 默認: `500`  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
list| array<object>| 成交信息  
> execId| string| 成交id  
> symbol| string| 價差產品名稱  
> price| string| 成交價格  
> size| string| 成交數量  
> side| string| 吃單方向 `Buy`, `Sell`  
> time| string| 成交時間戳 (毫秒)  
> seq| string| 撮合版本號  
  
### 請求示例
    
    
    GET /v5/spread/recent-trade?symbol=SOLUSDT_SOL/USDT&limit=2 HTTP/1.1  
    Host: api-testnet.bybit.com  
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "Success",  
        "result": {  
            "list": [  
                {  
                    "execId": "c8512970-d6fb-5039-93a5-b4196dffbe88",  
                    "symbol": "SOLUSDT_SOL/USDT",  
                    "price": "20.2805",  
                    "size": "3.3",  
                    "side": "Sell",  
                    "time": "1744078324035",  
                    "seq":"123456"  
                },  
                {  
                    "execId": "92b0002e-c49d-5618-a195-4140d7e10a2b",  
                    "symbol": "SOLUSDT_SOL/USDT",  
                    "price": "20.843",  
                    "size": "2.2",  
                    "side": "Buy",  
                    "time": "1744078322010",  
                    "seq":"123450"  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1744078324682  
    }