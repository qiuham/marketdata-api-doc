---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/market/adl-alert
api_type: Market Data
updated_at: 2026-06-30 19:27:47.979564
---

# Get Funding Rate History

Query for historical funding rates. Each symbol has a different funding interval. For example, if the interval is 8 hours and the current time is UTC 12, then it returns the last funding rate, which settled at UTC 8.

To query the funding rate interval, please refer to the [instruments-info](/docs/v5/market/instrument) endpoint.

> **Covers: USDT and USDC perpetual / Inverse perpetual**

info

  * Passing only `startTime` returns an error.
  * Passing only `endTime` returns 200 records up till `endTime`.
  * Passing neither returns 200 records up till the current time.



### HTTP Request

GET`/v5/market/funding/history`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
[category](/docs/v5/enum#category)| **true**|  string| Product type. `linear`,`inverse`  
symbol| **true**|  string| Symbol name, like `BTCUSDT`, uppercase only  
startTime| false| integer| The start timestamp (ms)  
endTime| false| integer| The end timestamp (ms)  
limit| false| integer| Limit for data size per page. [`1`, `200`]. Default: `200`  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
category| string| Product type  
list| array| Object  
> symbol| string| Symbol name  
> fundingRate| string| Funding rate  
> fundingRateTimestamp| string| Funding rate timestamp (ms)  
[](/docs/api-explorer/v5/market/history-fund-rate)

* * *

### Request Example

  * HTTP
  * Python
  * GO
  * Java
  * Node.js


    
    
    GET /v5/market/funding/history?category=linear&symbol=ETHPERP&limit=1 HTTP/1.1  
    Host: api-testnet.bybit.com  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP()  
    print(session.get_funding_rate_history(  
        category="linear",  
        symbol="ETHPERP",  
        limit=1,  
    ))  
    
    
    
    import (  
        "context"  
        "fmt"  
        bybit "github.com/bybit-exchange/bybit.go.api"  
    )  
    client := bybit.NewBybitHttpClient("", "", bybit.WithBaseURL(bybit.TESTNET))  
    params := map[string]interface{}{"category": "spot", "symbol": "BTCUSDT"}  
    client.NewUtaBybitServiceWithParams(params).GetFundingRateHistory(context.Background())  
    
    
    
    import com.bybit.api.client.domain.CategoryType;  
    import com.bybit.api.client.domain.market.*;  
    import com.bybit.api.client.domain.market.request.MarketDataRequest;  
    import com.bybit.api.client.service.BybitApiClientFactory;  
    var client = BybitApiClientFactory.newInstance().newAsyncMarketDataRestClient();  
    var fundingHistoryRequest = MarketDataRequest.builder().category(CategoryType.LINEAR).symbol("BTCUSD).startTime(1632046800000L).endTime(1632133200000L).limit(150).build();  
    client.getFundingHistory(fundingHistoryRequest, System.out::println);  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
        testnet: true,  
    });  
      
    client  
        .getFundingRateHistory({  
            category: 'linear',  
            symbol: 'ETHPERP',  
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
            "category": "linear",  
            "list": [  
                {  
                    "symbol": "ETHPERP",  
                    "fundingRate": "0.0001",  
                    "fundingRateTimestamp": "1672041600000"  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1672051897447  
    }

---

# 查詢歷史資金費率

查詢資金費率，每個symbol的資金費率產生週期不同。假設資金費率為8小時，當前時間是UTC12點，則返回的是上一個結算即UTC8點產生的資金費率。如要查詢symbol的資金費率時間間隔，請查詢[可交易產品規格](/docs/zh-TW/v5/market/instrument)接口

> **覆蓋範圍: USDT和USDC永續 / 反向永續**

時間入参規則

  * 只傳`startTime`會報錯
  * 只傳`endTime`，則返回endTime往前的200條數據
  * 都不傳，返回當前時間的往前200條數據



### HTTP請求

GET`/v5/market/funding/history`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
[category](/docs/zh-TW/v5/enum#category)| **true**|  string| 產品類型. `linear`,`inverse`  
symbol| **true**|  string| 合約名稱  
startTime| false| integer| 開始時間戳 (毫秒)  
endTime| false| integer| 結束時間戳 (毫秒)  
limit| false| integer| 每頁數量限制. [`1`, `200`]. 默認: `200`  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
category| string| 產品類型  
list| array| Object  
> symbol| string| 合約名稱  
> fundingRate| string| 資金費率  
> fundingRateTimestamp| string| 資金費率時間戳 (毫秒)  
[](/docs/zh-TW/api-explorer/v5/market/history-fund-rate)

* * *

### 請求示例

  * HTTP
  * Python
  * GO
  * Java
  * Node.js


    
    
    GET /v5/market/funding/history?category=linear&symbol=ETHPERP&limit=1 HTTP/1.1  
    Host: api-testnet.bybit.com  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP()  
    print(session.get_funding_rate_history(  
        category="linear",  
        symbol="ETHPERP",  
        limit=1,  
    ))  
    
    
    
    import (  
        "context"  
        "fmt"  
        bybit "github.com/bybit-exchange/bybit.go.api"  
    )  
    client := bybit.NewBybitHttpClient("", "", bybit.WithBaseURL(bybit.TESTNET))  
    params := map[string]interface{}{"category": "linear", "symbol": "BTCUSDT"}  
    client.NewUtaBybitServiceWithParams(params).GetFundingRateHistory(context.Background())  
    
    
    
    import com.bybit.api.client.domain.CategoryType;  
    import com.bybit.api.client.domain.market.*;  
    import com.bybit.api.client.domain.market.request.MarketDataRequest;  
    import com.bybit.api.client.service.BybitApiClientFactory;  
    var client = BybitApiClientFactory.newInstance().newAsyncMarketDataRestClient();  
    var fundingHistoryRequest = MarketDataRequest.builder().category(CategoryType.LINEAR).symbol("BTCUSD).startTime(1632046800000L).endTime(1632133200000L).limit(150).build();  
    client.getFundingHistory(fundingHistoryRequest, System.out::println);  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
        testnet: true,  
    });  
      
    client  
        .getFundingRateHistory({  
            category: 'linear',  
            symbol: 'ETHPERP',  
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
            "category": "linear",  
            "list": [  
                {  
                    "symbol": "ETHPERP",  
                    "fundingRate": "0.0001",  
                    "fundingRateTimestamp": "1672041600000"  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1672051897447  
    }