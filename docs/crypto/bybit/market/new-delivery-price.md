---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/market/new-delivery-price
api_type: Market Data
updated_at: 2026-07-03 19:14:20.132041
---

# Get Premium Index Price Kline

Query for historical [premium index](https://www.bybit.com/data/basic/linear/index-price/premium-index?symbol=BTCUSDT) klines. Charts are returned in groups based on the requested interval.

> **Covers: USDT and USDC perpetual**

### HTTP Request

GET`/v5/market/premium-index-price-kline`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
[category](/docs/v5/enum#category)| false| string| Product type. `linear`  
symbol| **true**|  string| Symbol name, like `BTCUSDT`, uppercase only  
[interval](/docs/v5/enum#interval)| **true**|  string| Kline interval. `1`,`3`,`5`,`15`,`30`,`60`,`120`,`240`,`360`,`720`,`D`,`W`,`M`  
start| false| integer| The start timestamp (ms)  
end| false| integer| The end timestamp (ms)  
limit| false| integer| Limit for data size per page. [`1`, `1000`]. Default: `200`  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
[category](/docs/v5/enum#category)| string| Product type  
symbol| string| Symbol name  
list| array| 

  * An string array of individual candle
  * Sort in reverse by `start`

  
> list[0]| string| Start time of the candle (ms)  
> list[1]| string| Open price  
> list[2]| string| Highest price  
> list[3]| string| Lowest price  
> list[4]| string| Close price. _Is the last traded price when the candle is not closed_  
[](/docs/api-explorer/v5/market/premium-index-kline)

* * *

### Request Example

  * HTTP
  * Python
  * Go
  * Java
  * Node.js


    
    
    GET /v5/market/premium-index-price-kline?category=linear&symbol=BTCUSDT&interval=D&start=1652112000000&end=1652544000000 HTTP/1.1  
    Host: api-testnet.bybit.com  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP()  
    print(session.get_premium_index_price_kline(  
        category="linear",  
        symbol="BTCUSDT",  
        inverval="D",  
        start=1652112000000,  
        end=1652544000000,  
    ))  
    
    
    
    import (  
        "context"  
        "fmt"  
        bybit "github.com/bybit-exchange/bybit.go.api"  
    )  
    client := bybit.NewBybitHttpClient("", "", bybit.WithBaseURL(bybit.TESTNET))  
    params := map[string]interface{}{"category": "spot", "symbol": "BTCUSDT", "interval": "1"}  
    client.NewUtaBybitServiceWithParams(params).GetPremiumIndexPriceKline(context.Background())  
    
    
    
    import com.bybit.api.client.domain.CategoryType;  
    import com.bybit.api.client.domain.market.*;  
    import com.bybit.api.client.domain.market.request.MarketDataRequest;  
    import com.bybit.api.client.service.BybitApiClientFactory;  
    var client = BybitApiClientFactory.newInstance().newAsyncMarketDataRestClient();  
    var marketKLineRequest = MarketDataRequest.builder().category(CategoryType.LINEAR).symbol("BTCUSDT").marketInterval(MarketInterval.WEEKLY).build();  
    client.getPremiumIndexPriceLinesData(marketKLineRequest, System.out::println);  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
        testnet: true,  
    });  
      
    client  
        .getPremiumIndexPriceKline({  
            category: 'linear',  
            symbol: 'BTCUSDT',  
            interval: 'D',  
            start: 1652112000000,  
            end: 1652544000000,  
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
            "symbol": "BTCUSDT",  
            "category": "linear",  
            "list": [  
                [  
                    "1652486400000",  
                    "-0.000587",  
                    "-0.000344",  
                    "-0.000480",  
                    "-0.000344"  
                ],  
                [  
                    "1652400000000",  
                    "-0.000989",  
                    "-0.000561",  
                    "-0.000587",  
                    "-0.000587"  
                ]  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1672765216291  
    }

---

# 查詢溢價指數價格K線數據

查詢溢價指數價格K線數據

> **覆蓋範圍: USDT和USDC永續**

### HTTP請求

GET`/v5/market/premium-index-price-kline`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
[category](/docs/zh-TW/v5/enum#category)| false| string| 產品類型. `linear`

  * 當`category`不指定時, 默認是`linear`

  
symbol| **true**|  string| 合約名稱  
[interval](/docs/zh-TW/v5/enum#interval)| **true**|  string| 時間粒度. `1`,`3`,`5`,`15`,`30`,`60`,`120`,`240`,`360`,`720`,`D`,`M`,`W`  
start| false| integer| 開始時間戳 (毫秒)  
end| false| integer| 結束時間戳 (毫秒)  
limit| false| integer| 每頁數量限制. [`1`, `1000`]. 默認: `200`  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
[category](/docs/zh-TW/v5/enum#category)| string| 產品類型  
symbol| string| 合約名稱  
list| array| 

  * 一個字符串數組構成單個蠟燭
  * 按照`startTime`降序排列

  
> list[0]| string| 蠟燭的開始時間戳 (毫秒)  
> list[1]| string| 開始價格  
> list[2]| string| 最高價格  
> list[3]| string| 最低價格  
> list[4]| string| 結束價格. _如果蠟燭尚未結束，則表示為最新成交價格_  
[](/docs/zh-TW/api-explorer/v5/market/premium-index-kline)

* * *

### 請求示例

  * HTTP
  * Python
  * Go
  * Java
  * Node.js


    
    
    GET /v5/market/premium-index-price-kline?category=linear&symbol=BTCUSDT&interval=D&start=1652112000000&end=1652544000000 HTTP/1.1  
    Host: api-testnet.bybit.com  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP()  
    print(session.get_premium_index_price_kline(  
        category="linear",  
        symbol="BTCUSDT",  
        inverval="D",  
        start=1652112000000,  
        end=1652544000000,  
    ))  
    
    
    
    import (  
        "context"  
        "fmt"  
        bybit "github.com/bybit-exchange/bybit.go.api"  
    )  
    client := bybit.NewBybitHttpClient("", "", bybit.WithBaseURL(bybit.TESTNET))  
    params := map[string]interface{}{"category": "spot", "symbol": "BTCUSDT", "interval": "1"}  
    client.NewUtaBybitServiceWithParams(params).GetPremiumIndexPriceKline(context.Background())  
    
    
    
    import com.bybit.api.client.domain.CategoryType;  
    import com.bybit.api.client.domain.market.*;  
    import com.bybit.api.client.domain.market.request.MarketDataRequest;  
    import com.bybit.api.client.service.BybitApiClientFactory;  
    var client = BybitApiClientFactory.newInstance().newAsyncMarketDataRestClient();  
    var marketKLineRequest = MarketDataRequest.builder().category(CategoryType.LINEAR).symbol("BTCUSDT").marketInterval(MarketInterval.WEEKLY).build();  
    client.getPremiumIndexPriceLinesData(marketKLineRequest, System.out::println);  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
        testnet: true,  
    });  
      
    client  
        .getPremiumIndexPriceKline({  
            category: 'linear',  
            symbol: 'BTCUSDT',  
            interval: 'D',  
            start: 1652112000000,  
            end: 1652544000000,  
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
            "symbol": "BTCPERP",  
            "category": "linear",  
            "list": [  
                [  
                    "1672026540000",  
                    "0.000000",  
                    "0.000000",  
                    "0.000000",  
                    "0.000000"  
                ],  
                [  
                    "1672026480000",  
                    "0.000000",  
                    "0.000000",  
                    "0.000000",  
                    "0.000000"  
                ]  
                ]  
        },  
        "retExtInfo": {},  
        "time": 1672026605042  
    }