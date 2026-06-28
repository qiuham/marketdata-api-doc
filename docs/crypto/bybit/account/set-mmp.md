---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/account/set-mmp
api_type: Account
updated_at: 2026-05-27 19:14:15.832333
---

# Set Spot Hedging

You can turn on/off Spot hedging feature in Portfolio margin

### HTTP Request

POST`/v5/account/set-hedging-mode`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
setHedgingMode| **true**|  string| `ON`, `OFF`  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
retCode| integer| Result code  
retMsg| string| Result message  
[](/docs/api-explorer/v5/account/set-spot-hedge)

* * *

### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    POST /v5/account/set-hedging-mode HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1700117968580  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
    Content-Length: 31  
      
    {  
        "setHedgingMode": "OFF"  
    }  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.set_hedging_mode(  
        setHedgingMode="OFF"  
    ))  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
      testnet: true,  
      key: 'xxxxxxxxxxxxxxxxxx',  
      secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
      .setSpotHedging({  
        setHedgingMode: 'ON' | 'OFF',  
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
        "retMsg": "SUCCESS"  
    }

---

# 設置現貨對衝

您可以開關現貨對從功能, 僅限統一帳戶組合保證金模式下

### HTTP 請求

POST`/v5/account/set-hedging-mode`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
setHedgingMode| **true**|  string| `ON`, `OFF`  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
retCode| integer| Result code  
retMsg| string| Result message  
[](/docs/zh-TW/api-explorer/v5/account/set-spot-hedge)

* * *

### 請求示例

  * HTTP
  * Python
  * Node.js


    
    
    POST /v5/account/set-hedging-mode HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1700117968580  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
    Content-Length: 31  
      
    {  
        "setHedgingMode": "OFF"  
    }  
    
    
    
      
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
      testnet: true,  
      key: 'xxxxxxxxxxxxxxxxxx',  
      secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
      .setSpotHedging({  
        setHedgingMode: 'ON' | 'OFF',  
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
        "retMsg": "SUCCESS"  
    }