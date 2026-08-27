---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/otc/repay-info
api_type: REST
updated_at: 2026-08-27 21:45:55.873243
---

# Set Auto Add Margin

Turn on/off auto-add-margin for **isolated** margin position

### HTTP Request

POST`/v5/position/set-auto-add-margin`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
[category](/docs/v5/enum#category)| **true**|  string| Product type `linear` (USDT Contract, USDC Contract)  
symbol| **true**|  string| Symbol name, like `BTCUSDT`, uppercase only  
autoAddMargin| **true**|  integer| Turn on/off. `0`: off. `1`: on  
[positionIdx](/docs/v5/enum#positionidx)| false| integer| Used to identify positions in different position modes. For hedge mode position, this param is **required**

  * `0`: one-way mode
  * `1`: hedge-mode Buy side
  * `2`: hedge-mode Sell side

  
  
### Response Parameters

None

[](/docs/api-explorer/v5/position/auto-add-margin)

* * *

### Request Example

  * HTTP
  * Python
  * Java
  * Node.js


    
    
    POST /v5/position/set-auto-add-margin HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN-TYPE: 2  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1675255134857  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "category": "linear",  
        "symbol": "BTCUSDT",  
        "autoAddmargin": 1,  
        "positionIdx": null  
    }  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.set_auto_add_margin(  
        category="linear",  
        symbol="BTCUSDT",  
        autoAddmargin=1,  
    ))  
    
    
    
    import com.bybit.api.client.domain.*;  
    import com.bybit.api.client.domain.position.*;  
    import com.bybit.api.client.domain.position.request.*;  
    import com.bybit.api.client.service.BybitApiClientFactory;  
    var client = BybitApiClientFactory.newInstance().newAsyncPositionRestClient();  
    var setAutoAddMarginRequest = PositionDataRequest.builder().category(CategoryType.LINEAR).symbol("BTCUSDT").autoAddMargin(AutoAddMargin.ON).build();  
    client.setAutoAddMargin(setAutoAddMarginRequest, System.out::println);  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
        testnet: true,  
        key: 'xxxxxxxxxxxxxxxxxx',  
        secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
        .setAutoAddMargin({  
            category: 'linear',  
            symbol: 'BTCUSDT',  
            autoAddMargin: 1,  
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
        "time": 1675255135069  
    }

---

# 設置自動追加保證金

開關自動追加保證金，僅適用於**逐倉** 保證金模式

### HTTP 請求

POST`/v5/position/set-auto-add-margin`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
[category](/docs/zh-TW/v5/enum#category)| **true**|  string| 產品類型 `linear`  
symbol| **true**|  string| 合約名稱  
autoAddMargin| **true**|  integer| 是否自動追加保證金. `0`: 關閉. `1`: 開啟  
[positionIdx](/docs/zh-TW/v5/enum#positionidx)| false| integer| 倉位標識，用於標識不同倉位, 雙向持倉模式下，該字段**必傳**

  * `0`: 單向持倉模式
  * `1`: 買側雙向持倉模式
  * `2`: 賣側雙向持倉模式

  
[](/docs/zh-TW/api-explorer/v5/position/auto-add-margin)

* * *

### 響應參數

無

### 請求示例

  * HTTP
  * Python
  * Java
  * Node.js


    
    
    POST /v5/position/set-auto-add-margin HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN-TYPE: 2  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1675255134857  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "category": "linear",  
        "symbol": "BTCUSDT",  
        "autoAddmargin": 1,  
        "positionIdx": null  
    }  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.set_auto_add_margin(  
        category="linear",  
        symbol="BTCUSDT",  
        autoAddmargin=1,  
    ))  
    
    
    
    import com.bybit.api.client.domain.*;  
    import com.bybit.api.client.domain.position.*;  
    import com.bybit.api.client.domain.position.request.*;  
    import com.bybit.api.client.service.BybitApiClientFactory;  
    var client = BybitApiClientFactory.newInstance().newAsyncPositionRestClient();  
    var setAutoAddMarginRequest = PositionDataRequest.builder().category(CategoryType.LINEAR).symbol("BTCUSDT").autoAddMargin(AutoAddMargin.ON).build();  
    client.setAutoAddMargin(setAutoAddMarginRequest, System.out::println);  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
        testnet: true,  
        key: 'xxxxxxxxxxxxxxxxxx',  
        secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
        .setAutoAddMargin({  
            category: 'linear',  
            symbol: 'BTCUSDT',  
            autoAddMargin: 1,  
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
        "time": 1675255135069  
    }