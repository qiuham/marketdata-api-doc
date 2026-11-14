---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/market/index-kline
api_type: Market Data
updated_at: 2026-11-13 19:23:50.194713
---

# Get Index Price Kline

Query for historical [index price](https://www.bybit.com/en-US/help-center/s/article/Glossary-Bybit-Trading-Terms) klines. Charts are returned in groups based on the requested interval.

> **Covers: USDT contract / USDC contract / Inverse contract**

### HTTP Request

GET`/v5/market/index-price-kline`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
[category](/docs/v5/enum#category)| false| string| Product type. `linear`,`inverse`

  * When `category` is not passed, use `linear` by default

  
symbol| **true**|  string| Symbol name, like `BTCUSDT`, uppercase only  
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
[](/docs/api-explorer/v5/market/index-kline)

* * *

### Request Example

  * HTTP
  * Python
  * Go
  * Java
  * Node.js


    
    
    GET /v5/market/index-price-kline?category=inverse&symbol=BTCUSDZ22&interval=1&start=1670601600000&end=1670608800000&limit=2 HTTP/1.1  
    Host: api-testnet.bybit.com  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(testnet=True)  
    print(session.get_index_price_kline(  
        category="inverse",  
        symbol="BTCUSDZ22",  
        interval=1,  
        start=1670601600000,  
        end=1670608800000,  
        limit=2,  
    ))  
    
    
    
    import (  
        "context"  
        "fmt"  
        bybit "github.com/bybit-exchange/bybit.go.api"  
    )  
    client := bybit.NewBybitHttpClient("", "", bybit.WithBaseURL(bybit.TESTNET))  
    params := map[string]interface{}{"category": "spot", "symbol": "BTCUSDT", "interval": "1"}  
    client.NewUtaBybitServiceWithParams(params).GetIndexPriceKline(context.Background())  
    
    
    
    import com.bybit.api.client.domain.CategoryType;  
    import com.bybit.api.client.domain.market.*;  
    import com.bybit.api.client.domain.market.request.MarketDataRequest;  
    import com.bybit.api.client.service.BybitApiClientFactory;  
    var client = BybitApiClientFactory.newInstance().newAsyncMarketDataRestClient();  
    var marketKLineRequest = MarketDataRequest.builder().category(CategoryType.LINEAR).symbol("BTCUSDT").marketInterval(MarketInterval.WEEKLY).build();  
    client.getIndexPriceLinesData(marketKLineRequest, System.out::println);  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
        testnet: true,  
    });  
      
    client  
        .getIndexPriceKline({  
            category: 'inverse',  
            symbol: 'BTCUSDZ22',  
            interval: '1',  
            start: 1670601600000,  
            end: 1670608800000,  
            limit: 2,  
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
            "symbol": "BTCUSDZ22",  
            "category": "inverse",  
            "list": [  
                [  
                    "1670608800000",  
                    "17167.00",  
                    "17167.00",  
                    "17161.90",  
                    "17163.07"  
                ],  
                [  
                    "1670608740000",  
                    "17166.54",  
                    "17167.69",  
                    "17165.42",  
                    "17167.00"  
                ]  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1672026471128  
    }

---

# 查詢指數價格K線數據

查詢指數價格K線

> **覆蓋範圍: USDT永續 / USDC交割 / USDC永續 / USDC交割 / 反向合約**

### HTTP請求

GET`/v5/market/index-price-kline`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
[category](/docs/zh-TW/v5/enum#category)| false| string| 產品類型. `linear`,`inverse`

  * 當`category`不指定時, 默認是`linear`

  
symbol| **true**|  string| 合約名稱  
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
[](/docs/zh-TW/api-explorer/v5/market/index-kline)

* * *

### 請求示例

  * HTTP
  * Python
  * Go
  * Java
  * Node.js


    
    
    GET /v5/market/index-price-kline?category=inverse&symbol=BTCUSDZ22&interval=1&start=1670601600000&end=1670608800000&limit=2 HTTP/1.1  
    Host: api-testnet.bybit.com  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(testnet=True)  
    print(session.get_index_price_kline(  
        category="inverse",  
        symbol="BTCUSDZ22",  
        interval=1,  
        start=1670601600000,  
        end=1670608800000,  
        limit=2,  
    ))  
    
    
    
    import (  
        "context"  
        "fmt"  
        bybit "github.com/bybit-exchange/bybit.go.api"  
    )  
    client := bybit.NewBybitHttpClient("", "", bybit.WithBaseURL(bybit.TESTNET))  
    params := map[string]interface{}{"category": "spot", "symbol": "BTCUSDT", "interval": "1"}  
    client.NewUtaBybitServiceWithParams(params).GetIndexPriceKline(context.Background())  
    
    
    
    import com.bybit.api.client.domain.CategoryType;  
    import com.bybit.api.client.domain.market.*;  
    import com.bybit.api.client.domain.market.request.MarketDataRequest;  
    import com.bybit.api.client.service.BybitApiClientFactory;  
    var client = BybitApiClientFactory.newInstance().newAsyncMarketDataRestClient();  
    var marketKLineRequest = MarketDataRequest.builder().category(CategoryType.LINEAR).symbol("BTCUSDT").marketInterval(MarketInterval.WEEKLY).build();  
    client.getIndexPriceLinesData(marketKLineRequest, System.out::println);  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
        testnet: true,  
    });  
      
    client  
        .getIndexPriceKline({  
            category: 'inverse',  
            symbol: 'BTCUSDZ22',  
            interval: '1',  
            start: 1670601600000,  
            end: 1670608800000,  
            limit: 2,  
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
            "symbol": "BTCUSDZ22",  
            "category": "inverse",  
            "list": [  
                [  
                    "1670608800000",  
                    "17167.00",  
                    "17167.00",  
                    "17161.90",  
                    "17163.07"  
                ],  
                [  
                    "1670608740000",  
                    "17166.54",  
                    "17167.69",  
                    "17165.42",  
                    "17167.00"  
                ]  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1672026471128  
    }