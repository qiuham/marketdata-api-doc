---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/alpha/prediction/price-history
api_type: REST
updated_at: 2026-11-13 19:21:14.272365
---

# Get Price History

Query historical price data for a prediction outcome token. Returns OHLC candlestick data for charting and analysis.

### HTTP Request

POST`/v5/alpha/prediction/price-history`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
tokenId| **true**|  string| Outcome token ID  
interval| **true**|  string| Time interval. Refer to [predictionPriceInterval](/docs/v5/enum#predictionpriceinterval-prediction-market--price-interval)  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
tokenId| string| Outcome token ID  
interval| string| Time interval used  
list| array| OHLC candlestick records, newest first  
> openTime| integer| Candle open timestamp (UTC milliseconds)  
> open| string| Open price  
> high| string| High price  
> low| string| Low price  
> close| string| Close price  
> volume| string| Trading volume in USDC for this candle  
  
### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    POST /v5/alpha/prediction/price-history HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1704067200000  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "tokenId": "token_yes_123",  
        "interval": "1H"  
    }  
    
    
    
      
    
    
    
      
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "tokenId": "token_yes_123",  
            "interval": "1H",  
            "list": [  
                {  
                    "openTime": 1704067200000,  
                    "open": "0.63",  
                    "high": "0.68",  
                    "low": "0.62",  
                    "close": "0.65",  
                    "volume": "12500"  
                },  
                {  
                    "openTime": 1704063600000,  
                    "open": "0.60",  
                    "high": "0.64",  
                    "low": "0.59",  
                    "close": "0.63",  
                    "volume": "9800"  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1704067200000  
    }

---

# 獲取歷史價格

查詢預測市場結果代幣的歷史價格數據，返回 OHLC K 線數據，用於圖表展示與分析。

### HTTP 請求

POST`/v5/alpha/prediction/price-history`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
tokenId| **true**|  string| 結果代幣 ID  
interval| **true**|  string| 時間週期。參考 [predictionPriceInterval](/docs/zh-TW/v5/enum#predictionpriceinterval-prediction-market--price-interval)  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
tokenId| string| 結果代幣 ID  
interval| string| 所用時間週期  
list| array| OHLC K 線記錄，最新在前  
> openTime| integer| K 線開盤時間戳（UTC 毫秒）  
> open| string| 開盤價  
> high| string| 最高價  
> low| string| 最低價  
> close| string| 收盤價  
> volume| string| 該 K 線交易量（USDC）  
  
### 請求示例

  * HTTP
  * Python
  * Node.js


    
    
    POST /v5/alpha/prediction/price-history HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1704067200000  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "tokenId": "token_yes_123",  
        "interval": "1H"  
    }  
    
    
    
      
    
    
    
      
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "tokenId": "token_yes_123",  
            "interval": "1H",  
            "list": [  
                {  
                    "openTime": 1704067200000,  
                    "open": "0.63",  
                    "high": "0.68",  
                    "low": "0.62",  
                    "close": "0.65",  
                    "volume": "12500"  
                },  
                {  
                    "openTime": 1704063600000,  
                    "open": "0.60",  
                    "high": "0.64",  
                    "low": "0.59",  
                    "close": "0.63",  
                    "volume": "9800"  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1704067200000  
    }