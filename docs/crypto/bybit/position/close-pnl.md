---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/position/close-pnl
api_type: Position
updated_at: 2026-08-24 18:46:03.469509
---

# Set Leverage

info

According to the risk limit, leverage affects the maximum position value that can be opened, that is, the greater the leverage, the smaller the maximum position value that can be opened, and vice versa. [Learn more](https://www.bybit.com/en/help-center/article/Risk-Limit-Perpetual-and-FuturesBybit_Perpetual_Contract_mechanism)

### HTTP Request

POST`/v5/position/set-leverage`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
[category](/docs/v5/enum#category)| **true**|  string| Product type `linear`, `inverse`  
symbol| **true**|  string| Symbol name, like `BTCUSDT`, uppercase only  
buyLeverage| **true**|  string| [`1`, max leverage]

  * one-way mode: `buyLeverage` must be the same as `sellLeverage`
  * Hedge mode:   
isolated margin: `buyLeverage` and `sellLeverage` can be different;   
cross margin: `buyLeverage` must be the same as `sellLeverage`

  
sellLeverage| **true**|  string| [`1`, max leverage]  
[](/docs/api-explorer/v5/position/leverage)

* * *

### Response Parameters

None

### Request Example

  * HTTP
  * Python
  * Java
  * Node.js


    
    
    POST /v5/position/set-leverage HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1672281605082  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "category": "linear",  
        "symbol": "BTCUSDT",  
        "buyLeverage": "6",  
        "sellLeverage": "6"  
      
    }  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.set_leverage(  
        category="linear",  
        symbol="BTCUSDT",  
        buyLeverage="6",  
        sellLeverage="6",  
    ))  
    
    
    
    import com.bybit.api.client.domain.*;  
    import com.bybit.api.client.domain.position.*;  
    import com.bybit.api.client.domain.position.request.*;  
    import com.bybit.api.client.service.BybitApiClientFactory;  
    var client = BybitApiClientFactory.newInstance().newAsyncPositionRestClient();  
    var setLeverageRequest = PositionDataRequest.builder().category(CategoryType.LINEAR).symbol("BTCUSDT").buyLeverage("5").sellLeverage("5").build();  
    client.setPositionLeverage(setLeverageRequest, System.out::println);  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
        testnet: true,  
        key: 'xxxxxxxxxxxxxxxxxx',  
        secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
        .setLeverage({  
            category: 'linear',  
            symbol: 'BTCUSDT',  
            buyLeverage: '6',  
            sellLeverage: '6',  
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
        "time": 1672281607343  
    }

---

# 設置槓桿

信息

根據風險限額, 槓桿影響最大可開數量, 即槓桿越大, 最大可開倉數量越小, 反之亦然。[了解更多](https://www.bybit.com/zh-MY/help-center/article/Risk-Limit-Perpetual-and-FuturesBybit_Perpetual_Contract_mechanism)

### HTTP 請求

POST`/v5/position/set-leverage`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
[category](/docs/zh-TW/v5/enum#category)| **true**|  string| 產品類型 `linear`, `inverse`  
symbol| **true**|  string| 合約名稱  
buyLeverage| **true**|  string| [`1`, 最大槓桿數]

  * 單倉: `buyLeverage` 必須等於`sellLeverage`
  * 雙倉:   
逐倉保證金: `buyLeverage`可以與`sellLeverage`不相等;   
全倉保證金: `buyLeverage` 必須等於`sellLeverage`

  
sellLeverage| **true**|  string| [`1`, 最大槓桿數]  
[](/docs/zh-TW/api-explorer/v5/position/leverage)

* * *

### 響應參數

無

### 請求示例

  * HTTP
  * Python
  * Java
  * Node.js


    
    
    POST /v5/position/set-leverage HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1672281605082  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "category": "linear",  
        "symbol": "BTCUSDT",  
        "buyLeverage": "6",  
        "sellLeverage": "6"  
      
    }  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.set_leverage(  
        category="linear",  
        symbol="BTCUSDT",  
        buyLeverage="6",  
        sellLeverage="6",  
    ))  
    
    
    
    import com.bybit.api.client.domain.*;  
    import com.bybit.api.client.domain.position.*;  
    import com.bybit.api.client.domain.position.request.*;  
    import com.bybit.api.client.service.BybitApiClientFactory;  
    var client = BybitApiClientFactory.newInstance().newAsyncPositionRestClient();  
    var setLeverageRequest = PositionDataRequest.builder().category(CategoryType.LINEAR).symbol("BTCUSDT").buyLeverage("5").sellLeverage("5").build();  
    client.setPositionLeverage(setLeverageRequest, System.out::println);  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
        testnet: true,  
        key: 'xxxxxxxxxxxxxxxxxx',  
        secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
        .setLeverage({  
            category: 'linear',  
            symbol: 'BTCUSDT',  
            buyLeverage: '6',  
            sellLeverage: '6',  
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
        "time": 1672281607343  
    }