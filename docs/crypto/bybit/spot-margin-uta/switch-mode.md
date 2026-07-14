---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/spot-margin-uta/switch-mode
api_type: REST
updated_at: 2026-07-14 18:57:04.340796
---

# Toggle Margin Trade

Turn on / off spot margin trade

caution

Your account needs to activate spot margin first; i.e., you must have finished the quiz on web / app.

### HTTP Request

POST`/v5/spot-margin-trade/switch-mode`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
spotMarginMode| **true**|  string| `1`: on, `0`: off  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
spotMarginMode| string| Spot margin status. `1`: on, `0`: off  
[](/docs/api-explorer/v5/spot-margin-uta/switch-mode)

* * *

### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    POST /v5/spot-margin-trade/switch-mode HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1672297794480  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "spotMarginMode": "0"  
    }  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.spot_margin_trade_toggle_margin_trade(  
        spotMarginMode="0",  
    ))  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
      testnet: true,  
      key: 'xxxxxxxxxxxxxxxxxx',  
      secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
      .toggleSpotMarginTrade('0')  
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
            "spotMarginMode": "0"  
        },  
        "retExtInfo": {},  
        "time": 1672297795542  
    }

---

# 全倉槓桿開關

全倉槓桿開關

> **覆蓋範圍: 全倉槓桿 (統一帳戶)**

警告

您的帳戶需要先開啟全倉槓桿

### HTTP 請求

POST`/v5/spot-margin-trade/switch-mode`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
spotMarginMode| **true**|  string| `1`: 開啟，`0`: 關閉  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
spotMarginMode| string| 全倉槓桿狀態（`1`: 開啟，`0`: 關閉）  
[](/docs/zh-TW/api-explorer/v5/spot-margin-uta/switch-mode)

* * *

### 請求示例

  * HTTP
  * Python
  * Node.js


    
    
    POST /v5/spot-margin-trade/switch-mode HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1672297794480  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "spotMarginMode": "0"  
    }  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.spot_margin_trade_toggle_margin_trade(  
        spotMarginMode="0",  
    ))  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
      testnet: true,  
      key: 'xxxxxxxxxxxxxxxxxx',  
      secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
      .toggleSpotMarginTrade('0')  
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
            "spotMarginMode": "0"  
        },  
        "retExtInfo": {},  
        "time": 1672297795542  
    }