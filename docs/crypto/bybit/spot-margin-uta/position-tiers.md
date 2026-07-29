---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/spot-margin-uta/position-tiers
api_type: REST
updated_at: 2026-07-29 18:53:29.938213
---

# Set Leverage

Set the user's maximum leverage in spot cross margin

caution

Your account needs to activate spot margin first; i.e., you must have finished the quiz on web / app.   
The updated leverage must be less than or equal to the maximum leverage of the currency

### HTTP Request

POST`/v5/spot-margin-trade/set-leverage`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
leverage| **true**|  string| Leverage. [`2`, `10`].  
currency| false| string| Coin name, uppercase only  
[](/docs/api-explorer/v5/spot-margin-uta/set-leverage)

* * *

### Response Parameters

None

### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    POST /v5/spot-margin-trade/set-leverage HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1672299806626  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "leverage": "4"  
    }  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.spot_margin_trade_set_leverage(  
        leverage="4",  
    ))  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
      testnet: true,  
      key: 'xxxxxxxxxxxxxxxxxx',  
      secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
      .setSpotMarginLeverage('4')  
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
        "time": 1672710944282  
    }

---

# 全倉槓桿設置

全倉槓桿設置用戶最大槓桿倍數

> **覆蓋範圍: 全倉槓桿 (統一帳戶)**

警告

需要先開啟全倉槓桿，才能調整槓桿。  
更新後的槓桿必須小於或等於該幣的最大槓桿

### HTTP 請求

POST`/v5/spot-margin-trade/set-leverage`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
leverage| **true**|  string| 槓桿倍數 (整數), 支持區間 [`2`, `10`]  
currency| false| string| 幣名稱，僅限大寫  
[](/docs/zh-TW/api-explorer/v5/spot-margin-uta/set-leverage)

* * *

### 響應參數

無

### 請求示例

  * HTTP
  * Python
  * Node.js


    
    
    POST /v5/spot-margin-trade/set-leverage HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1672299806626  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "leverage": "4"  
    }  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.spot_margin_trade_set_leverage(  
        leverage="4",  
    ))  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
      testnet: true,  
      key: 'xxxxxxxxxxxxxxxxxx',  
      secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
      .setSpotMarginLeverage('4')  
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
        "time": 1672710944282  
    }