---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/market/kline
api_type: Market Data
updated_at: 2026-05-27 19:18:24.002595
---

# Get Long Short Ratio

This refers to the net long and short positions as percentages of all position holders during the selected time.   
Long account ratio = Number of holders with long positions / Total number of holders   
Short account ratio = Number of holders with short positions / Total number of holders   
Long-short account ratio = Long account ratio / Short account ratio

info

  * The earliest query start time is July 20, 2020
  * During periods of extreme market volatility, this interface may experience increased latency or temporary delays in data delivery



### HTTP Request

GET`/v5/market/account-ratio`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
[category](/docs/v5/enum#category)| **true**|  string| Product type. `linear`(USDT Contract),`inverse`  
[symbol](/docs/v5/enum#symbol)| **true**|  string| Symbol name, like `BTCUSDT`, uppercase only  
[period](/docs/v5/enum#datarecordingperiod)| **true**|  string| Data recording period. `5min`, `15min`, `30min`, `1h`, `4h`, `1d`  
startTime| false| string| The start timestamp (ms)  
endTime| false| string| The end timestamp (ms)  
limit| false| integer| Limit for data size per page. [`1`, `500`]. Default: `50`  
cursor| false| string| Cursor. Use the `nextPageCursor` token from the response to retrieve the next page of the result set  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
list| array| Object  
> symbol| string| Symbol name  
> buyRatio| string| The ratio of the number of long position  
> sellRatio| string| The ratio of the number of short position  
> timestamp| string| Timestamp (ms)  
nextPageCursor| string| Refer to the `cursor` request parameter  
[](/docs/api-explorer/v5/market/long-short-ratio)

* * *

### Request Example

  * HTTP
  * Python
  * GO
  * Java
  * Node.js


    
    
    GET /v5/market/account-ratio?category=linear&symbol=BTCUSDT&period=1h&limit=2&startTime=1696089600000&endTime=1696262400000 HTTP/1.1  
    Host: api-testnet.bybit.com  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.get_long_short_ratio(  
        category="linear",  
        symbol="BTCUSDT",  
        period="1h",  
        limit=2,  
        startTime="1696089600000",  
        endTime="1696262400000"  
    ))  
    
    
    
    import (  
        "context"  
        "fmt"  
        bybit "github.com/bybit-exchange/bybit.go.api"  
    )  
    client := bybit.NewBybitHttpClient("", "", bybit.WithBaseURL(bybit.TESTNET))  
    params := map[string]interface{}{"category": "linear", "symbol": "BTCUSDT", "period": "5min"}  
    client.NewUtaBybitServiceWithParams(params).GetLongShortRatio(context.Background())  
    
    
    
    import com.bybit.api.client.domain.CategoryType;  
    import com.bybit.api.client.domain.market.*;  
    import com.bybit.api.client.domain.market.request.MarketDataRequest;  
    import com.bybit.api.client.service.BybitApiClientFactory;  
    var client = BybitApiClientFactory.newInstance().newAsyncMarketDataRestClient();  
    var marketAccountRatioRequest = MarketDataRequest.builder().category(CategoryType.LINEAR).symbol("BTCUSDT").dataRecordingPeriod(DataRecordingPeriod.FIFTEEN_MINUTES).limit(10).build();  
    client.getMarketAccountRatio(marketAccountRatioRequest, System.out::println);  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
      testnet: true,  
    });  
      
    client  
      .getLongShortRatio({  
        category: 'linear',  
        symbol: 'BTCUSDT',  
        period: '1h',  
        limit: 100,  
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
            "list": [  
                {  
                    "symbol": "BTCUSDT",  
                    "buyRatio": "0.49",  
                    "sellRatio": "0.51",  
                    "timestamp": "1696262400000"  
                },  
                {  
                    "symbol": "BTCUSDT",  
                    "buyRatio": "0.4927",  
                    "sellRatio": "0.5073",  
                    "timestamp": "1696258800000"  
                }  
            ],  
            "nextPageCursor": "lastid%3D0%26lasttime%3D1696258800"  
        },  
        "retExtInfo": {},  
        "time": 1731567491688  
    }

---

# 查詢多空比

指選定時間內淨多頭部位和淨空頭部位佔所有持有者的百分比。  
多頭帳戶比例 = 多頭持倉者數 / 總持倉者數量   
空頭帳戶比例 = 空頭持倉者數 / 總持倉者數   
多空帳戶比例 = 多頭帳戶比例 / 空頭帳戶比例   


信息

  * 查詢起始時間最早為2020年7月20日
  * 在極端市場波動期間, 此介面可能會出現延遲增加或資料傳遞暫時延遲的情況



### HTTP請求

GET`/v5/market/account-ratio`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
[category](/docs/zh-TW/v5/enum#category)| **true**|  string| 產品類型. `linear`(USDT永續, USDT交割),`inverse`  
[symbol](/docs/zh-TW/v5/enum#symbol)| **true**|  string| 合約名稱  
[period](/docs/zh-TW/v5/enum#datarecordingperiod)| **true**|  string| 數據週期. `5min`, `15min`, `30min`, `1h`, `4h`, `1d`  
startTime| false| string| 開始時間戳 (毫秒)  
endTime| false| string| 結束時間戳 (毫秒)  
limit| false| integer| 每頁數量限制. [`1`, `500`]. 默認: `50`  
cursor| false| string| 游標，用於分頁  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
list| array| Object  
> symbol| string| 合約名稱  
> buyRatio| string| 持有多倉比例  
> sellRatio| string| 持有空倉的比例  
> timestamp| string| 時間戳 (毫秒)  
nextPageCursor| string| 游標，用於分頁  
[](/docs/zh-TW/api-explorer/v5/market/long-short-ratio)

* * *

### 請求示例

  * HTTP
  * Python
  * GO
  * Java
  * Node.js


    
    
    GET /v5/market/account-ratio?category=linear&symbol=BTCUSDT&period=1h&limit=2&startTime=1696089600000&endTime=1696262400000 HTTP/1.1  
    Host: api-testnet.bybit.com  
    
    
    
      
    
    
    
    import (  
        "context"  
        "fmt"  
        bybit "github.com/bybit-exchange/bybit.go.api"  
    )  
    client := bybit.NewBybitHttpClient("", "", bybit.WithBaseURL(bybit.TESTNET))  
    params := map[string]interface{}{"category": "linear", "symbol": "BTCUSDT", "period": "5min"}  
    client.NewUtaBybitServiceWithParams(params).GetLongShortRatio(context.Background())  
    
    
    
    import com.bybit.api.client.domain.CategoryType;  
    import com.bybit.api.client.domain.market.*;  
    import com.bybit.api.client.domain.market.request.MarketDataRequest;  
    import com.bybit.api.client.service.BybitApiClientFactory;  
    var client = BybitApiClientFactory.newInstance().newAsyncMarketDataRestClient();  
    var marketAccountRatioRequest = MarketDataRequest.builder().category(CategoryType.LINEAR).symbol("BTCUSDT").dataRecordingPeriod(DataRecordingPeriod.FIFTEEN_MINUTES).limit(10).build();  
    client.getMarketAccountRatio(marketAccountRatioRequest, System.out::println);  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
      testnet: true,  
    });  
      
    client  
      .getLongShortRatio({  
        category: 'linear',  
        symbol: 'BTCUSDT',  
        period: '1h',  
        limit: 100,  
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
            "list": [  
                {  
                    "symbol": "BTCUSDT",  
                    "buyRatio": "0.49",  
                    "sellRatio": "0.51",  
                    "timestamp": "1696262400000"  
                },  
                {  
                    "symbol": "BTCUSDT",  
                    "buyRatio": "0.4927",  
                    "sellRatio": "0.5073",  
                    "timestamp": "1696258800000"  
                }  
            ],  
            "nextPageCursor": "lastid%3D0%26lasttime%3D1696258800"  
        },  
        "retExtInfo": {},  
        "time": 1731567491688  
    }