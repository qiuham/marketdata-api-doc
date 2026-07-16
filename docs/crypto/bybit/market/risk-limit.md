---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/market/risk-limit
api_type: Market Data
updated_at: 2026-07-16 18:54:13.213508
---

# Get Bybit Server Time

info

  * During periods of extreme market volatility, this interface may experience increased latency or temporary delays in data delivery



### HTTP Request

GET`/v5/market/time`

### Request Parameters

None

### Response Parameters

Parameter| Type| Comments  
---|---|---  
timeSecond| string| Bybit server timestamp (sec)  
timeNano| string| Bybit server timestamp (nano)  
[](/docs/api-explorer/v5/market/time)

* * *

### Request Example

  * HTTP
  * Python
  * Java
  * Go
  * Node.js


    
    
    GET /v5/market/time HTTP/1.1  
    Host: api.bybit.com  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(testnet=True)  
    print(session.get_server_time())  
    
    
    
    import com.bybit.api.client.service.BybitApiClientFactory;  
    var client = BybitApiClientFactory.newInstance().newAsyncMarketDataRestClient();  
    client.getServerTime(System.out::println);  
    
    
    
    import (  
        "context"  
        "fmt"  
        bybit "github.com/bybit-exchange/bybit.go.api"  
    )  
    client := bybit.NewBybitHttpClient("", "", bybit.WithBaseURL(bybit.TESTNET))  
    client.NewUtaBybitServiceNoParams().GetServerTime(context.Background())  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
      testnet: true,  
    });  
      
    client  
      .getServerTime()  
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
            "timeSecond": "1688639403",  
            "timeNano": "1688639403423213947"  
        },  
        "retExtInfo": {},  
        "time": 1688639403423  
    }

---

# Bybit服務器時間

獲取Bybit服務器時間

信息

  * 在極端市場波動期間, 此介面可能會出現延遲增加或資料傳遞暫時延遲的情況



### HTTP 請求

GET`/v5/market/time`

### 請求參數

無

### 響應參數

參數| 類型| 說明  
---|---|---  
timeSecond| string| Bybit服務器時間戳 (秒)  
timeNano| string| Bybit 服務器時間戳 (微秒)  
[](/docs/zh-TW/api-explorer/v5/market/time)

* * *

### 請求示例

  * HTTP
  * Python
  * Go
  * Java
  * Node.js


    
    
    GET /v5/market/time HTTP/1.1  
    Host: api.bybit.com  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(testnet=True)  
    print(session.get_server_time())  
    
    
    
    import (  
        "context"  
        "fmt"  
        bybit "github.com/bybit-exchange/bybit.go.api"  
    )  
    client := bybit.NewBybitHttpClient("", "", bybit.WithBaseURL(bybit.TESTNET))  
    client.NewUtaBybitServiceNoParams().GetServerTime(context.Background())  
    
    
    
    import com.bybit.api.client.service.BybitApiClientFactory;  
    var client = BybitApiClientFactory.newInstance().newAsyncMarketDataRestClient();  
    client.getServerTime(System.out::println);  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
      testnet: true,  
    });  
      
    client  
      .getServerTime()  
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
            "timeSecond": "1688639403",  
            "timeNano": "1688639403423213947"  
        },  
        "retExtInfo": {},  
        "time": 1688639403423  
    }