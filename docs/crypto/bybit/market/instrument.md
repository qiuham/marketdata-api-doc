---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/market/instrument
api_type: Market Data
updated_at: 2026-06-30 19:27:55.908474
---

# Get Historical Volatility

Query option historical volatility

> **Covers: Option**

info

  * The data is hourly.
  * If both `startTime` and `endTime` are not specified, it will return the most recent 1 hours worth of data.
  * `startTime` and `endTime` are a pair of params. Either both are passed or they are not passed at all.
  * This endpoint can query the last 2 years worth of data, but make sure [`endTime` \- `startTime`] <= 30 days.



### HTTP Request

GET`/v5/market/historical-volatility`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
category| **true**|  string| Product type. `option`  
baseCoin| false| string| Base coin, uppercase only. Default: return BTC data  
quoteCoin| false| string| Quote coin, `USD` or `USDT`. Default: return quoteCoin=USD  
[period](/docs/v5/enum#optionperiod)| false| integer| Period. If not specified, it will return data with a 7-day average by default  
startTime| false| integer| The start timestamp (ms)  
endTime| false| integer| The end timestamp (ms)  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
category| string| Product type  
list| array| Object  
> period| integer| Period  
> value| string| Volatility  
> time| string| Timestamp (ms)  
[](/docs/api-explorer/v5/market/iv)

* * *

### Request Example

  * HTTP
  * Python
  * Java
  * Node.js


    
    
    GET /v5/market/historical-volatility?category=option&baseCoin=ETH&period=30 HTTP/1.1  
    Host: api-testnet.bybit.com  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(testnet=True)  
    print(session.get_historical_volatility(  
        category="option",  
        baseCoin="ETH",  
        period=30,  
    ))  
    
    
    
    import com.bybit.api.client.domain.CategoryType;  
    import com.bybit.api.client.domain.market.*;  
    import com.bybit.api.client.domain.market.request.MarketDataRequest;  
    import com.bybit.api.client.service.BybitApiClientFactory;  
    var client = BybitApiClientFactory.newInstance().newAsyncMarketDataRestClient();  
    var historicalVolatilityRequest = MarketDataRequest.builder().category(CategoryType.OPTION).optionPeriod(7).build();  
    client.getHistoricalVolatility(historicalVolatilityRequest, System.out::println);  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
        testnet: true,  
    });  
      
    client  
        .getHistoricalVolatility({  
            category: 'option',  
            baseCoin: 'ETH',  
            period: 30,  
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
        "retMsg": "SUCCESS",  
        "category": "option",  
        "result": [  
            {  
                "period": 30,  
                "value": "0.45024716",  
                "time": "1672052400000"  
            }  
        ]  
    }

---

# 查詢期權波動率

獲取期權的歷史波動率數據

> **覆蓋範圍: 期權**

信息

  * 數據為每小時數據.
  * 若沒有入参時間，則默認返回最近1小時的數據，即最近的一條數據.
  * `starTime` 和 `endTime` 要麼都傳，要麼都不傳
  * 接口支持查詢過去2年的數據, 但確保[`endTime` \- `startTime`] 小於等於30天.



### HTTP請求

GET`/v5/market/historical-volatility`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
category| **true**|  string| 產品類型. `option`  
baseCoin| false| string| 交易幣種. 不傳則默認返回BTC數據  
quoteCoin| false| string| 報價幣種, `USD` 或 `USDT`. 不傳則默認返回quoteCoin=USD數據  
[period](/docs/zh-TW/v5/enum#optionperiod)| false| string| 週期. 不傳則默認返回7天加權的數據  
startTime| false| integer| 開始時間戳 (毫秒)  
endTime| false| integer| 結束時間戳 (毫秒)  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
category| string| 產品類型  
list| array| Object  
> period| string| 週期  
> value| string| 波動率  
> time| string| 數據生成時間戳 (毫秒)  
[](/docs/zh-TW/api-explorer/v5/market/iv)

* * *

### 請求示例

  * HTTP
  * Python
  * GO
  * Java
  * Node.js


    
    
    GET /v5/market/historical-volatility?category=option&baseCoin=ETH&period=30 HTTP/1.1  
    Host: api-testnet.bybit.com  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(testnet=True)  
    print(session.get_historical_volatility(  
        category="option",  
        baseCoin="ETH",  
        period=30,  
    ))  
    
    
    
    import (  
        "context"  
        "fmt"  
        bybit "github.com/bybit-exchange/bybit.go.api"  
    )  
    client := bybit.NewBybitHttpClient("", "", bybit.WithBaseURL(bybit.TESTNET))  
    params := map[string]interface{}{"category": "option", "baseCoin": "BTC"}  
    client.NewUtaBybitServiceWithParams(params).GetHistoryVolatility(context.Background())  
    
    
    
    import com.bybit.api.client.domain.CategoryType;  
    import com.bybit.api.client.domain.market.*;  
    import com.bybit.api.client.domain.market.request.MarketDataRequest;  
    import com.bybit.api.client.service.BybitApiClientFactory;  
    var client = BybitApiClientFactory.newInstance().newAsyncMarketDataRestClient();  
    var historicalVolatilityRequest = MarketDataRequest.builder().category(CategoryType.OPTION).optionPeriod(7).build();  
    client.getHistoricalVolatility(historicalVolatilityRequest, System.out::println);  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
        testnet: true,  
    });  
      
    client  
        .getHistoricalVolatility({  
            category: 'option',  
            baseCoin: 'ETH',  
            period: 30,  
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
        "retMsg": "SUCCESS",  
        "category": "option",  
        "result": [  
            {  
                "period": 7,  
                "value": "0.27545620",  
                "time": "1672232400000"  
            }  
        ]  
    }