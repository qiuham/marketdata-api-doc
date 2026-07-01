---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/market/kline
api_type: Market Data
updated_at: 2026-07-01 19:29:49.197018
---

# Get Open Interest

Get the [open interest](https://www.bybit.com/en-US/help-center/s/article/Glossary-Bybit-Trading-Terms) of each symbol.

> **Covers: USDT contract / USDC contract / Inverse contract**

info

  * The upper limit time you can query is the launch time of the symbol.
  * During periods of extreme market volatility, this interface may experience increased latency or temporary delays in data delivery



### HTTP Request

GET`/v5/market/open-interest`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
[category](/docs/v5/enum#category)| **true**|  string| Product type. `linear`,`inverse`  
symbol| **true**|  string| Symbol name, like `BTCUSDT`, uppercase only  
[intervalTime](/docs/v5/enum#intervaltime)| **true**|  string| Interval time. `5min`,`15min`,`30min`,`1h`,`4h`,`1d`  
startTime| false| integer| The start timestamp (ms)  
endTime| false| integer| The end timestamp (ms)  
limit| false| integer| Limit for data size per page. [`1`, `200`]. Default: `50`  
cursor| false| string| Cursor. Used to paginate  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
category| string| Product type  
symbol| string| Symbol name  
list| array| Object  
> openInterest| string| Open interest. The value is the sum of both sides.   
The unit of value, e.g., BTCUSD(inverse) is USD, BTCUSDT(linear) is BTC  
> singleOpenInterest| string| Open interest. The value is the single side.   
The unit of value, e.g., BTCUSD(inverse) is USD, BTCUSDT(linear) is BTC  
> timestamp| string| The timestamp (ms)  
nextPageCursor| string| Used to paginate  
[](/docs/api-explorer/v5/market/open-interest)

* * *

### Request Example

  * HTTP
  * Python
  * GO
  * Java
  * Node.js


    
    
    GET /v5/market/open-interest?limit=5&category=inverse&intervalTime=1d&symbol=BTCUSD HTTP/1.1  
    Host: api-testnet.bybit.com  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(testnet=True)  
    print(session.get_open_interest(  
        category="inverse",  
        symbol="BTCUSD",  
        intervalTime="5min",  
        startTime=1669571100000,  
        endTime=1669571400000,  
    ))  
    
    
    
    import (  
        "context"  
        "fmt"  
        bybit "github.com/bybit-exchange/bybit.go.api"  
    )  
    client := bybit.NewBybitHttpClient("", "", bybit.WithBaseURL(bybit.TESTNET))  
    params := map[string]interface{}{"category": "linear", "symbol": "BTCUSDT"}  
    client.NewUtaBybitServiceWithParams(params).GetOpenInterests(context.Background())  
    
    
    
    import com.bybit.api.client.domain.CategoryType;  
    import com.bybit.api.client.domain.market.*;  
    import com.bybit.api.client.domain.market.request.MarketDataRequest;  
    import com.bybit.api.client.service.BybitApiClientFactory;  
    var client = BybitApiClientFactory.newInstance().newAsyncMarketDataRestClient();  
    var openInterest = MarketDataRequest.builder().category(CategoryType.LINEAR).symbol("BTCUSDT").marketInterval(MarketInterval.FIVE_MINUTES).build();  
    client.getOpenInterest(openInterest, System.out::println);  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
        testnet: true,  
    });  
      
    client  
        .getOpenInterest({  
            category: 'inverse',  
            symbol: 'BTCUSD',  
            intervalTime: '5min',  
            startTime: 1669571100000,  
            endTime: 1669571400000,  
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
                {  
                    "openInterest": "63910691.00000000",  
                    "singleOpenInterest": "31955346",  
                    "timestamp": "1780963200000"  
                },  
                {  
                    "openInterest": "63910691.00000000",  
                    "singleOpenInterest": "31955346",  
                    "timestamp": "1780876800000"  
                },  
                {  
                    "openInterest": "63910691.00000000",  
                    "singleOpenInterest": "31955346",  
                    "timestamp": "1780790400000"  
                },  
                {  
                    "openInterest": "63942311.00000000",  
                    "singleOpenInterest": "31971156",  
                    "timestamp": "1780704000000"  
                },  
                {  
                    "openInterest": "63942311.00000000",  
                    "singleOpenInterest": "31971156",  
                    "timestamp": "1780617600000"  
                }  
            ],  
            "nextPageCursor": "lastid%3D19408935%26lasttime%3D1780617600"  
        },  
        "retExtInfo": {},  
        "time": 1780994051392  
    }

---

# 查詢未平倉合約持倉數量

查詢各個合約市場內所有未平倉的數量

> **覆蓋範圍: USDT永續 / USDC永續 / USDC交割 / 反向合約**

信息

  * 最久可以查詢到自合約上線開始的數據
  * 在極端市場波動期間, 此介面可能會出現延遲增加或資料傳遞暫時延遲的情況



### HTTP請求

GET`/v5/market/open-interest`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
[category](/docs/zh-TW/v5/enum#category)| **true**|  string| 產品類型. `linear`,`inverse`  
symbol| **true**|  string| 合約名稱  
[intervalTime](/docs/zh-TW/v5/enum#intervaltime)| **true**|  string| 時間粒度. `5min` `15min` `30min` `1h` `4h` `1d`  
startTime| false| integer| 開始時間戳 (毫秒)  
endTime| false| integer| 結束時間戳 (毫秒)  
limit| false| integer| 每頁數量限制. [`1`, `200`]. 默認: `50`  
cursor| false| string| 游標，用於翻頁  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
category| string| 產品類型  
symbol| string| 合約名稱  
list| array| Object  
> openInterest| string| 未平倉合約數量, 數值為雙邊的和  
這個數值的單位是, 比如, BTCUSDT永續是BTC, BTCUSD反向合約是USD  
> singleOpenInterest| string| 未平倉合約數量, 數值為單邊的值  
這個數值的單位是, 比如, BTCUSDT永續是BTC, BTCUSD反向合約是USD  
> timestamp| string| 數據產生的時間戳（毫秒）  
nextPageCursor| string| 游標，用於翻頁  
[](/docs/zh-TW/api-explorer/v5/market/open-interest)

* * *

### 請求示例

  * HTTP
  * Python
  * GO
  * Java
  * Node.js


    
    
    GET /v5/market/open-interest?limit=5&category=inverse&intervalTime=1d&symbol=BTCUSD HTTP/1.1  
    Host: api-testnet.bybit.com  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(testnet=True)  
    print(session.get_open_interest(  
        category="inverse",  
        symbol="BTCUSD",  
        intervalTime="5min",  
        startTime=1669571100000,  
        endTime=1669571400000,  
    ))  
    
    
    
    import (  
        "context"  
        "fmt"  
        bybit "github.com/bybit-exchange/bybit.go.api"  
    )  
    client := bybit.NewBybitHttpClient("", "", bybit.WithBaseURL(bybit.TESTNET))  
    params := map[string]interface{}{"category": "linear", "symbol": "BTCUSDT"}  
    client.NewUtaBybitServiceWithParams(params).GetOpenInterests(context.Background())  
    
    
    
    import com.bybit.api.client.domain.CategoryType;  
    import com.bybit.api.client.domain.market.*;  
    import com.bybit.api.client.domain.market.request.MarketDataRequest;  
    import com.bybit.api.client.service.BybitApiClientFactory;  
    var client = BybitApiClientFactory.newInstance().newAsyncMarketDataRestClient();  
    var openInterest = MarketDataRequest.builder().category(CategoryType.LINEAR).symbol("BTCUSDT").marketInterval(MarketInterval.FIVE_MINUTES).build();  
    client.getOpenInterest(openInterest, System.out::println);  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
        testnet: true,  
    });  
      
    client  
        .getOpenInterest({  
            category: 'inverse',  
            symbol: 'BTCUSD',  
            intervalTime: '5min',  
            startTime: 1669571100000,  
            endTime: 1669571400000,  
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
                {  
                    "openInterest": "63910691.00000000",  
                    "singleOpenInterest": "31955346",  
                    "timestamp": "1780963200000"  
                },  
                {  
                    "openInterest": "63910691.00000000",  
                    "singleOpenInterest": "31955346",  
                    "timestamp": "1780876800000"  
                },  
                {  
                    "openInterest": "63910691.00000000",  
                    "singleOpenInterest": "31955346",  
                    "timestamp": "1780790400000"  
                },  
                {  
                    "openInterest": "63942311.00000000",  
                    "singleOpenInterest": "31971156",  
                    "timestamp": "1780704000000"  
                },  
                {  
                    "openInterest": "63942311.00000000",  
                    "singleOpenInterest": "31971156",  
                    "timestamp": "1780617600000"  
                }  
            ],  
            "nextPageCursor": "lastid%3D19408935%26lasttime%3D1780617600"  
        },  
        "retExtInfo": {},  
        "time": 1780994051392  
    }