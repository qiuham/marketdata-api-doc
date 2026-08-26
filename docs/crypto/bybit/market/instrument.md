---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/market/instrument
api_type: Market Data
updated_at: 2026-08-26 19:13:44.640749
---

# Get Kline

Query for historical klines (also known as candles/candlesticks). Charts are returned in groups based on the requested interval.

> **Covers: Spot / USDT contract / USDC contract / Inverse contract**

### HTTP Request

GET`/v5/market/kline`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
[category](/docs/v5/enum#category)| false| string| Product type. `spot`,`linear`,`inverse`

  * When `category` is not passed, use `linear` by default

  
[symbol](/docs/v5/enum#symbol)| **true**|  string| Symbol name, like `BTCUSDT`, uppercase only  
[interval](/docs/v5/enum#interval)| **true**|  string| Kline interval. `1`,`3`,`5`,`15`,`30`,`60`,`120`,`240`,`360`,`720`,`D`,`W`,`M`  
start| false| integer| The start timestamp (ms)  
end| false| integer| The end timestamp (ms)  
limit| false| integer| Limit for data size per page. [`1`, `1000`]. Default: `200`  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
category| string| Product type  
symbol| string| Symbol name  
list| array| 

  * An string array of individual candle
  * Sort in reverse by `startTime`

  
> list[0]: startTime| string| Start time of the candle (ms)  
> list[1]: openPrice| string| Open price  
> list[2]: highPrice| string| Highest price  
> list[3]: lowPrice| string| Lowest price  
> list[4]: closePrice| string| Close price. _Is the last traded price when the candle is not closed_  
> list[5]: volume| string| Trade volume 

  * USDT or USDC contract: unit is base coin (e.g., BTC)
  * Inverse contract: unit is quote coin (e.g., USD)

  
> list[6]: turnover| string| Turnover. 

  * USDT or USDC contract: unit is quote coin (e.g., USDT)
  * Inverse contract: unit is base coin (e.g., BTC)

  
[](/docs/api-explorer/v5/market/kline)

* * *

### Request Example

  * HTTP
  * Python
  * Go
  * Java
  * Node.js


    
    
    GET /v5/market/kline?category=inverse&symbol=BTCUSD&interval=60&start=1670601600000&end=1670608800000 HTTP/1.1  
    Host: api-testnet.bybit.com  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(testnet=True)  
    print(session.get_kline(  
        category="inverse",  
        symbol="BTCUSD",  
        interval=60,  
        start=1670601600000,  
        end=1670608800000,  
    ))  
    
    
    
    import (  
        "context"  
        "fmt"  
        bybit "github.com/bybit-exchange/bybit.go.api"  
    )  
    client := bybit.NewBybitHttpClient("", "", bybit.WithBaseURL(bybit.TESTNET))  
    params := map[string]interface{}{"category": "spot", "symbol": "BTCUSDT", "interval": "1"}  
    client.NewUtaBybitServiceWithParams(params).GetMarketKline(context.Background())  
    
    
    
    import com.bybit.api.client.domain.CategoryType;  
    import com.bybit.api.client.domain.market.*;  
    import com.bybit.api.client.domain.market.request.MarketDataRequest;  
    import com.bybit.api.client.service.BybitApiClientFactory;  
    var client = BybitApiClientFactory.newInstance().newAsyncMarketDataRestClient();  
    var marketKLineRequest = MarketDataRequest.builder().category(CategoryType.LINEAR).symbol("BTCUSDT").marketInterval(MarketInterval.WEEKLY).build();  
    client.getMarketLinesData(marketKLineRequest, System.out::println);  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
        testnet: true,  
    });  
      
    client  
        .getKline({  
            category: 'inverse',  
            symbol: 'BTCUSD',  
            interval: '60',  
            start: 1670601600000,  
            end: 1670608800000,  
        })  
        .then((response) => {  
            console.log(response);  
        })  
        .catch((error) => {  
            console.error(error);  
        });  
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "symbol": "BTCUSD",  
            "category": "inverse",  
            "list": [  
                [  
                    "1670608800000",  
                    "17071",  
                    "17073",  
                    "17027",  
                    "17055.5",  
                    "268611",  
                    "15.74462667"  
                ],  
                [  
                    "1670605200000",  
                    "17071.5",  
                    "17071.5",  
                    "17061",  
                    "17071",  
                    "4177",  
                    "0.24469757"  
                ],  
                [  
                    "1670601600000",  
                    "17086.5",  
                    "17088",  
                    "16978",  
                    "17071.5",  
                    "6356",  
                    "0.37288112"  
                ]  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1672025956592  
    }

---

# 查詢市場價格K線數據

查詢市場價格K線數據

> **覆蓋範圍: 現貨 / USDT永續 / USDT交割 / USDC永續 / USDC交割 / 反向合約**

### HTTP請求

GET`/v5/market/kline`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
[category](/docs/zh-TW/v5/enum#category)| false| string| 產品類型. `spot`,`linear`,`inverse`

  * 當`category`不指定時, 默認是`linear`

  
[symbol](/docs/zh-TW/v5/enum#symbol)| **true**|  string| 合約名稱  
[interval](/docs/zh-TW/v5/enum#interval)| **true**|  string| 時間粒度. `1`,`3`,`5`,`15`,`30`,`60`,`120`,`240`,`360`,`720`,`D`,`M`,`W`  
start| false| integer| 開始時間戳 (毫秒)  
end| false| integer| 結束時間戳 (毫秒)  
limit| false| integer| 每頁數量限制. [`1`, `1000`]. 默認: `200`  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
category| string| 產品類型  
symbol| string| 合約名稱  
list| array| 

  * 一個字符串數組構成單個蠟燭
  * 按照`startTime`降序排列

  
> list[0]: startTime| string| 蠟燭的開始時間戳 (毫秒)  
> list[1]: openPrice| string| 開始價格  
> list[2]: highPrice| string| 最高價格  
> list[3]: lowPrice| string| 最低價格  
> list[4]: closePrice| string| 結束價格. _如果蠟燭尚未結束，則表示為最新成交價格_  
> list[5]: volume| string| 交易量 

  * U本位合約: 單位是base coin (比如, BTC)
  * 幣本位合約: 單位是報價幣種 (e.g., USD)

  
> list[6]: turnover| string| 交易額 

  * U本位合約: 單位是報價幣種(比如, USDT)
  * 幣本位合約: 單位是base coin (e.g., BTC)

  
[](/docs/zh-TW/api-explorer/v5/market/kline)

* * *

### 請求示例

  * HTTP
  * Python
  * Go
  * Java
  * Node.js


    
    
    GET /v5/market/kline?category=inverse&symbol=BTCUSD&interval=60&start=1670601600000&end=1670608800000 HTTP/1.1  
    Host: api-testnet.bybit.com  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(testnet=True)  
    print(session.get_kline(  
        category="inverse",  
        symbol="BTCUSD",  
        interval=60,  
        start=1670601600000,  
        end=1670608800000,  
    ))  
    
    
    
    import (  
        "context"  
        "fmt"  
        bybit "github.com/bybit-exchange/bybit.go.api"  
    )  
    client := bybit.NewBybitHttpClient("", "", bybit.WithBaseURL(bybit.TESTNET))  
    params := map[string]interface{}{"category": "spot", "symbol": "BTCUSDT", "interval": "1"}  
    client.NewUtaBybitServiceWithParams(params).GetMarketKline(context.Background())  
    
    
    
    import com.bybit.api.client.domain.CategoryType;  
    import com.bybit.api.client.domain.market.*;  
    import com.bybit.api.client.domain.market.request.MarketDataRequest;  
    import com.bybit.api.client.service.BybitApiClientFactory;  
    var client = BybitApiClientFactory.newInstance().newAsyncMarketDataRestClient();  
    var marketKLineRequest = MarketDataRequest.builder().category(CategoryType.LINEAR).symbol("BTCUSDT").marketInterval(MarketInterval.WEEKLY).build();  
    client.getMarketLinesData(marketKLineRequest, System.out::println);  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
        testnet: true,  
    });  
      
    client  
        .getKline({  
            category: 'inverse',  
            symbol: 'BTCUSD',  
            interval: '60',  
            start: 1670601600000,  
            end: 1670608800000,  
        })  
        .then((response) => {  
            console.log(response);  
        })  
        .catch((error) => {  
            console.error(error);  
        });  
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "symbol": "BTCUSD",  
            "category": "inverse",  
            "list": [  
                [  
                    "1670608800000",  
                    "17071",  
                    "17073",  
                    "17027",  
                    "17055.5",  
                    "268611",  
                    "15.74462667"  
                ],  
                [  
                    "1670605200000",  
                    "17071.5",  
                    "17071.5",  
                    "17061",  
                    "17071",  
                    "4177",  
                    "0.24469757"  
                ],  
                [  
                    "1670601600000",  
                    "17086.5",  
                    "17088",  
                    "16978",  
                    "17071.5",  
                    "6356",  
                    "0.37288112"  
                ]  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1672025956592  
    }