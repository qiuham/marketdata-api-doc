---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/market/mark-kline
api_type: Market Data
updated_at: 2026-07-21 18:58:55.630022
---

# Get Mark Price Kline

Query for historical [mark price](https://www.bybit.com/en-US/help-center/s/article/Glossary-Bybit-Trading-Terms) klines. Charts are returned in groups based on the requested interval.

> **Covers: USDT contract / USDC contract / Inverse contract / Options**

### HTTP Request

GET`/v5/market/mark-price-kline`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
[category](/docs/v5/enum#category)| false| string| Product type. `linear`,`inverse`, `option`

  * When `category` is not passed, use `linear` by default

  
symbol| **true**|  string| Symbol name, like `BTCUSDT`, uppercase only  
[interval](/docs/v5/enum#interval)| **true**|  string| Kline interval. `1`,`3`,`5`,`15`,`30`,`60`,`120`,`240`,`360`,`720`,`D`,`M`,`W`  
start| false| integer| The start timestamp (ms)  
end| false| integer| The end timestamp (ms)  
limit| false| integer| Limit for data size per page. futures: [`1`, `1000`], option: [`1`, `500`]. Default: `200`  
  
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
[](/docs/api-explorer/v5/market/mark-kline)

* * *

### Request Example

  * HTTP
  * Python
  * Go
  * Java
  * Node.js


    
    
    GET /v5/market/mark-price-kline?category=linear&symbol=BTCUSDT&interval=15&start=1670601600000&end=1670608800000&limit=1 HTTP/1.1  
    Host: api-testnet.bybit.com  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(testnet=True)  
    print(session.get_mark_price_kline(  
        category="linear",  
        symbol="BTCUSDT",  
        interval=15,  
        start=1670601600000,  
        end=1670608800000,  
        limit=1,  
    ))  
    
    
    
    import (  
        "context"  
        "fmt"  
        bybit "github.com/bybit-exchange/bybit.go.api"  
    )  
    client := bybit.NewBybitHttpClient("", "", bybit.WithBaseURL(bybit.TESTNET))  
    params := map[string]interface{}{"category": "spot", "symbol": "BTCUSDT", "interval": "1"}  
    client.NewUtaBybitServiceWithParams(params).GetMarkPriceKline(context.Background())  
    
    
    
    import com.bybit.api.client.domain.CategoryType;  
    import com.bybit.api.client.domain.market.*;  
    import com.bybit.api.client.domain.market.request.MarketDataRequest;  
    import com.bybit.api.client.service.BybitApiClientFactory;  
    var client = BybitApiClientFactory.newInstance().newAsyncMarketDataRestClient();  
    var marketKLineRequest = MarketDataRequest.builder().category(CategoryType.LINEAR).symbol("BTCUSDT").marketInterval(MarketInterval.WEEKLY).build();  
    client.getMarketPriceLinesData(marketKLineRequest, System.out::println);  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
        testnet: true,  
    });  
      
    client  
        .getMarkPriceKline({  
            category: 'linear',  
            symbol: 'BTCUSD',  
            interval: '15',  
            start: 1670601600000,  
            end: 1670608800000,  
            limit: 1,  
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
                "1670608800000",  
                "17164.16",  
                "17164.16",  
                "17121.5",  
                "17131.64"  
                ]  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1672026361839  
    }

---

# 查詢標記價格K線數據

查詢標記價格K線

> **覆蓋範圍: USDT永續 / USDT交割 / USDC永續 / USDC交割 / 反向合約 / 期權**

### HTTP請求

GET`/v5/market/mark-price-kline`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
[category](/docs/zh-TW/v5/enum#category)| false| string| 產品類型. `linear`,`inverse`,`option`

  * 當`category`不指定時, 默認是`linear`

  
symbol| **true**|  string| 合約名稱  
[interval](/docs/zh-TW/v5/enum#interval)| **true**|  string| 時間粒度. `1`,`3`,`5`,`15`,`30`,`60`,`120`,`240`,`360`,`720`,`D`,`M`,`W`  
start| false| integer| 開始時間戳 (毫秒)  
end| false| integer| 結束時間戳 (毫秒)  
limit| false| integer| 每頁數量限制. 合約: [`1`, `1000`], 期權: [`1`, `500`]. 默認: `200`  
  
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
[](/docs/zh-TW/api-explorer/v5/market/mark-kline)

* * *

### 請求示例

  * HTTP
  * Python
  * Go
  * Java
  * Node.js


    
    
    GET /v5/market/mark-price-kline?category=linear&symbol=BTCUSDT&interval=15&start=1670601600000&end=1670608800000&limit=1 HTTP/1.1  
    Host: api-testnet.bybit.com  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(testnet=True)  
    print(session.get_mark_price_kline(  
        category="linear",  
        symbol="BTCUSDT",  
        interval=15,  
        start=1670601600000,  
        end=1670608800000,  
        limit=1,  
    ))  
    
    
    
    import (  
        "context"  
        "fmt"  
        bybit "github.com/bybit-exchange/bybit.go.api"  
    )  
    client := bybit.NewBybitHttpClient("", "", bybit.WithBaseURL(bybit.TESTNET))  
    params := map[string]interface{}{"category": "spot", "symbol": "BTCUSDT", "interval": "1"}  
    client.NewUtaBybitServiceWithParams(params).GetMarkPriceKline(context.Background())  
    
    
    
    import com.bybit.api.client.domain.CategoryType;  
    import com.bybit.api.client.domain.market.*;  
    import com.bybit.api.client.domain.market.request.MarketDataRequest;  
    import com.bybit.api.client.service.BybitApiClientFactory;  
    var client = BybitApiClientFactory.newInstance().newAsyncMarketDataRestClient();  
    var marketKLineRequest = MarketDataRequest.builder().category(CategoryType.LINEAR).symbol("BTCUSDT").marketInterval(MarketInterval.WEEKLY).build();  
    client.getMarketPriceLinesData(marketKLineRequest, System.out::println);  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
        testnet: true,  
    });  
      
    client  
        .getMarkPriceKline({  
            category: 'linear',  
            symbol: 'BTCUSD',  
            interval: '15',  
            start: 1670601600000,  
            end: 1670608800000,  
            limit: 1,  
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
            "symbol": "BTCUSDT",  
            "category": "linear",  
            "list": [  
                [  
                "1670608800000",  
                "17164.16",  
                "17164.16",  
                "17121.5",  
                "17131.64"  
                ]  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1672026361839  
    }