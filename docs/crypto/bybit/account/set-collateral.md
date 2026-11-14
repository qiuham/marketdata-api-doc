---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/account/set-collateral
api_type: Account
updated_at: 2026-11-13 19:20:52.122757
---

# Set Collateral Coin

You can decide whether the assets in the Unified account needs to be collateral coins.

### HTTP Request

POST`/v5/account/set-collateral-switch`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
coin| **true**|  string| Coin name, uppercase only 

  * You can get collateral coin from [here](/docs/v5/account/collateral-info)
  * USDT, USDC cannot be set

  
collateralSwitch| **true**|  string| `ON`: switch on collateral, `OFF`: switch off collateral  
  
### Response Parameters

None

[](/docs/api-explorer/v5/account/set-collateral)

* * *

### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    POST /v5/account/set-collateral-switch HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1690513916181  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
    Content-Length: 55  
      
    {  
        "coin": "BTC",  
        "collateralSwitch": "ON"  
    }  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.set_collateral_coin(  
        coin="BTC",  
        collateralSwitch="ON"  
    ))  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
      testnet: true,  
      key: 'xxxxxxxxxxxxxxxxxx',  
      secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
      .setCollateralCoin({  
        coin: 'BTC',  
        collateralSwitch: 'ON',  
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
        "result": {},  
        "retExtInfo": {},  
        "time": 1690515818656  
    }

---

# 設置抵押品幣種

用戶可以自行決定是否開啟統一帳戶中幣種是否進行抵押，默認都是**關閉** 的

### HTTP 請求

POST`/v5/account/set-collateral-switch`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
coin| **true**|  string| 幣種名稱 

  * 您可以從[這裡](/docs/zh-TW/v5/account/collateral-info)獲取抵押品幣種
  * USDT, USDC不支持設置

  
collateralSwitch| **true**|  string| `ON`: 開啟抵押, `OFF`: 關閉抵押  
  
### 響應參數

無

[](/docs/zh-TW/api-explorer/v5/account/set-collateral)

* * *

### 請求示例

  * HTTP
  * Python
  * Node.js


    
    
    POST /v5/account/set-collateral-switch HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1690513916181  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
    Content-Length: 55  
      
    {  
        "coin": "BTC",  
        "collateralSwitch": "ON"  
    }  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.set_collateral_coin(  
        coin="BTC",  
        collateralSwitch="ON"  
    ))  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
      testnet: true,  
      key: 'xxxxxxxxxxxxxxxxxx',  
      secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
      .setCollateralCoin({  
        coin: 'BTC',  
        collateralSwitch: 'ON',  
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
        "result": {},  
        "retExtInfo": {},  
        "time": 1690515818656  
    }