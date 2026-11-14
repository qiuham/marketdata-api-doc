---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/abandon/tpsl-mode
api_type: REST
updated_at: 2026-11-13 19:20:42.627278
---

# Set TP/SL Mode

tip

 _To some extent, this endpoint is**deprecated** because now tpsl is based on order level. This API was used for position level change before._

_However, you still can use it to set an implicit tpsl mode for a certain symbol because when you don't pass "tpslMode" in the place order or trading stop request, system will get the tpslMode by the default setting._

Set TP/SL mode to Full or Partial

info

For partial TP/SL mode, you can set the TP/SL size smaller than position size.

### HTTP Request

POST`/v5/position/set-tpsl-mode`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
[category](/docs/v5/enum#category)| **true**|  string| Product type `linear`, `inverse`  
symbol| **true**|  string| Symbol name, like `BTCUSDT`, uppercase only  
tpSlMode| **true**|  string| TP/SL mode. `Full`,`Partial`  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
tpSlMode| string| `Full`,`Partial`  
[](/docs/api-explorer/v5/position/tpsl-mode)

* * *

### Request Example

  * HTTP
  * Python
  * Java
  * Node.js


    
    
    POST /v5/position/set-tpsl-mode HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1672279325035  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "symbol": "XRPUSDT",  
        "category": "linear",  
        "tpSlMode": "Full"  
    }  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.set_tp_sl_mode(  
        symbol="XRPUSDT",  
        category="linear",  
        tpSlMode="Full",  
    ))  
    
    
    
    import com.bybit.api.client.domain.*;  
    import com.bybit.api.client.domain.position.*;  
    import com.bybit.api.client.domain.position.request.*;  
    import com.bybit.api.client.service.BybitApiClientFactory;  
    var client = BybitApiClientFactory.newInstance().newAsyncPositionRestClient();  
    var setTpSlRequest = PositionDataRequest.builder().category(CategoryType.LINEAR).symbol("BTCUSDT").tpslMode(TpslMode.PARTIAL).build();  
    client.swithMarginRequest(setTpSlRequest, System.out::println);  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
        testnet: true,  
        key: 'xxxxxxxxxxxxxxxxxx',  
        secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
        .setTPSLMode({  
            symbol: 'XRPUSDT',  
            category: 'linear',  
            tpSlMode: 'Full',  
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
            "tpSlMode": "Full"  
        },  
        "retExtInfo": {},  
        "time": 1672279322666  
    }

---

# 設置止盈止損模式

提示

 _某種程度上來說，該接口已經**廢棄** , 原因在於新版的止盈止損機制是基於訂單維度. 這個接口當初主要是用於倉位維度的止盈止損_

 _但是, 您仍然可以使用該接口, 為某個合約設置一個隱式的止盈止損模式, 因為當您在下單接口或者設置止盈止損接口時, 不傳入字段"tpslMode"時, 系統將會獲取一個默認值, 該 默認值實際上是源於是否調用過該接口做過修改, 不曾修改過的symbol, 都是默認Full_

可以將止盈止損模式設置為部分止盈止損或者全部止盈止損

信息

在部分止盈止損下，您可以設置小於倉位大小的止盈止損數量

### HTTP 請求

POST`/v5/position/set-tpsl-mode`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
[category](/docs/zh-TW/v5/enum#category)| **true**|  string| 產品類型 `linear`, `inverse`  
symbol| **true**|  string| 合約名稱  
tpSlMode| **true**|  string| TP/SL模式. `Full`,`Partial`  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
tpSlMode| string| `Full`,`Partial`  
[](/docs/zh-TW/api-explorer/v5/position/tpsl-mode)

* * *

### 請求示例

  * HTTP
  * Python
  * Java
  * Node.js


    
    
    POST /v5/position/set-tpsl-mode HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1672279325035  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "symbol": "XRPUSDT",  
        "category": "linear",  
        "tpSlMode": "Full"  
    }  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.set_tp_sl_mode(  
        symbol="XRPUSDT",  
        category="linear",  
        tpSlMode="Full",  
    ))  
    
    
    
    import com.bybit.api.client.domain.*;  
    import com.bybit.api.client.domain.position.*;  
    import com.bybit.api.client.domain.position.request.*;  
    import com.bybit.api.client.service.BybitApiClientFactory;  
    var client = BybitApiClientFactory.newInstance().newAsyncPositionRestClient();  
    var setTpSlRequest = PositionDataRequest.builder().category(CategoryType.LINEAR).symbol("BTCUSDT").tpslMode(TpslMode.PARTIAL).build();  
    client.swithMarginRequest(setTpSlRequest, System.out::println);  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
        testnet: true,  
        key: 'xxxxxxxxxxxxxxxxxx',  
        secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
        .setTPSLMode({  
            symbol: 'XRPUSDT',  
            category: 'linear',  
            tpSlMode: 'Full',  
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
            "tpSlMode": "Full"  
        },  
        "retExtInfo": {},  
        "time": 1672279322666  
    }