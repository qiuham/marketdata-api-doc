---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/abandon/cross-isolate
api_type: REST
updated_at: 2026-11-13 19:20:37.320346
---

# Switch Cross/Isolated Margin

Select cross margin mode or isolated margin mode per symbol level

### HTTP Request

POST`/v5/position/switch-isolated`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
[category](/docs/v5/enum#category)| **true**|  string| Product type 

  * [UTA2.0](/docs/v5/acct-mode#uta-20): not supported
  * [UTA1.0](/docs/v5/acct-mode#uta-10): `inverse`
  * Classic: `linear`(USDT Preps), `inverse`

  
symbol| **true**|  string| Symbol name, like `BTCUSDT`, uppercase only  
tradeMode| **true**|  integer| `0`: cross margin. `1`: isolated margin  
buyLeverage| **true**|  string| The value must be equal to `sellLeverage` value  
sellLeverage| **true**|  string| The value must be equal to `buyLeverage` value  
[](/docs/api-explorer/v5/position/cross-isolate)

* * *

### Response Parameters

None

### Request Example

  * HTTP
  * Python
  * Java
  * Node.js


    
    
    POST /v5/position/switch-isolated HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN-TYPE: 2  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1675248447965  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
    Content-Length: 121  
      
    {  
        "category": "linear",  
        "symbol": "ETHUSDT",  
        "tradeMode": 1,  
        "buyLeverage": "10",  
        "sellLeverage": "10"  
    }  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.switch_margin_mode(  
        category="linear",  
        symbol="ETHUSDT",  
        tradeMode=1,  
        buyLeverage="10",  
        sellLeverage="10",  
    ))  
    
    
    
    import com.bybit.api.client.domain.*;  
    import com.bybit.api.client.domain.position.*;  
    import com.bybit.api.client.domain.position.request.*;  
    import com.bybit.api.client.service.BybitApiClientFactory;  
    var client = BybitApiClientFactory.newInstance().newAsyncPositionRestClient();  
    var switchMarginRequest = PositionDataRequest.builder().category(CategoryType.LINEAR).symbol("BTC-31MAR23").tradeMode(MarginMode.CROSS_MARGIN).buyLeverage("5").sellLeverage("5").build();  
    client.swithMarginRequest(switchMarginRequest, System.out::println);  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
        testnet: true,  
        key: 'xxxxxxxxxxxxxxxxxx',  
        secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
        .switchIsolatedMargin({  
            category: 'linear',  
            symbol: 'ETHUSDT',  
            tradeMode: 1,  
            buyLeverage: '10',  
            sellLeverage: '10',  
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
        "result": {},  
        "retExtInfo": {},  
        "time": 1675248433635  
    }

---

# 切換全倉/逐倉保證金(交易對)

選擇全倉保證金或者是逐倉保證金，請參閱[這裡](https://www.bybit.com/zh-TW/help-center/bybitHC_Article/?language=en_US&id=000001053)了解關於全倉/逐倉保證金模式。

### HTTP 請求

POST`/v5/position/switch-isolated`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
[category](/docs/zh-TW/v5/enum#category)| **true**|  string| 產品類型 

  * [統一帳戶2.0](/docs/zh-TW/v5/acct-mode#%E7%B5%B1%E4%B8%80%E5%B8%B3%E6%88%B620): 不適用
  * [統一帳戶1.0](/docs/zh-TW/v5/acct-mode#%E7%B5%B1%E4%B8%80%E5%B8%B3%E6%88%B610): `inverse`
  * 經典帳戶: `linear`, `inverse`

  
symbol| **true**|  string| 合約名稱  
tradeMode| **true**|  integer| `0`: 全倉. `1`: 逐倉  
buyLeverage| **true**|  string| 買側槓桿倍數. 必須與`sellLeverage`的值保持相同  
sellLeverage| **true**|  string| 賣側槓桿倍數. 必須與`buyLeverage`的值保持相同  
[](/docs/zh-TW/api-explorer/v5/position/cross-isolate)

* * *

### 響應參數

無

### 請求示例

  * HTTP
  * Python
  * Java
  * Node.js


    
    
    POST /v5/position/switch-isolated HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN-TYPE: 2  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1675248447965  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
    Content-Length: 121  
      
    {  
        "category": "linear",  
        "symbol": "ETHUSDT",  
        "tradeMode": 1,  
        "buyLeverage": "10",  
        "sellLeverage": "10"  
    }  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.switch_margin_mode(  
        category="linear",  
        symbol="ETHUSDT",  
        tradeMode=1,  
        buyLeverage="10",  
        sellLeverage="10",  
    ))  
    
    
    
    import com.bybit.api.client.domain.*;  
    import com.bybit.api.client.domain.position.*;  
    import com.bybit.api.client.domain.position.request.*;  
    import com.bybit.api.client.service.BybitApiClientFactory;  
    var client = BybitApiClientFactory.newInstance().newAsyncPositionRestClient();  
    var switchMarginRequest = PositionDataRequest.builder().category(CategoryType.LINEAR).symbol("BTC-31MAR23").tradeMode(MarginMode.CROSS_MARGIN).buyLeverage("5").sellLeverage("5").build();  
    client.swithMarginRequest(switchMarginRequest, System.out::println);  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
        testnet: true,  
        key: 'xxxxxxxxxxxxxxxxxx',  
        secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
        .switchIsolatedMargin({  
            category: 'linear',  
            symbol: 'ETHUSDT',  
            tradeMode: 1,  
            buyLeverage: '10',  
            sellLeverage: '10',  
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
        "result": {},  
        "retExtInfo": {},  
        "time": 1675248433635  
    }