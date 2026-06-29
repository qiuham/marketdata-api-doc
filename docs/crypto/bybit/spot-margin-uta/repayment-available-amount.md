---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/spot-margin-uta/repayment-available-amount
api_type: REST
updated_at: 2026-06-29 19:32:50.493066
---

# Get Status And Leverage

Query the Spot margin status and leverage

### HTTP Request

GET`/v5/spot-margin-trade/state`

### Request Parameters

None

### Response Parameters

Parameter| Type| Comments  
---|---|---  
spotLeverage| string| Spot margin leverage. Returns `""` if the margin trade is turned off  
spotMarginMode| string| Spot margin status. `1`: on, `0`: off  
effectiveLeverage| string| actual leverage ratio. Precision retains 2 decimal places, truncate downwards  
[](/docs/api-explorer/v5/spot-margin-uta/status)

* * *

### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/spot-margin-trade/state HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1692696840996  
    X-BAPI-RECV-WINDOW: 5000  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.spot_margin_trade_get_status_and_leverage())  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
      testnet: true,  
      key: 'xxxxxxxxxxxxxxxxxx',  
      secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
      .getSpotMarginState()  
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
            "spotLeverage": "10",  
            "spotMarginMode": "1",  
            "effectiveLeverage": "1"  
        },  
        "retExtInfo": {},  
        "time": 1692696841231  
    }

---

# 查詢開關狀態和倍數

查詢統一帳戶下槓桿交易的開關狀態和槓桿倍數

> **覆蓋範圍: 全倉槓桿 (統一帳戶)**

### HTTP 請求

GET`/v5/spot-margin-trade/state`

### 請求參數

無

### 響應參數

參數| 類型| 說明  
---|---|---  
spotLeverage| string| 槓桿倍數. 如果處於關閉狀態的話, 則返回 `""`  
spotMarginMode| string| 開關狀態. `1`: 開啟, `0`: 關閉  
effectiveLeverage| string| 實際借貸槓桿倍數。 精度保留2位小數，向下截取  
  
### 請求示例

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/spot-margin-trade/state HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1692696840996  
    X-BAPI-RECV-WINDOW: 5000  
    
    
    
      
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
      testnet: true,  
      key: 'xxxxxxxxxxxxxxxxxx',  
      secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
      .getSpotMarginState()  
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
            "spotLeverage": "10",  
            "spotMarginMode": "1",  
            "effectiveLeverage": "1"  
        },  
        "retExtInfo": {},  
        "time": 1692696841231  
    }