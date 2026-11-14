---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/asset/transfer/transferable-coin
api_type: REST
updated_at: 2026-11-13 19:21:49.990595
---

# Get Transferable Coin

Query the transferable coin list between each [account type](/docs/v5/enum#accounttype)

### HTTP Request

GET`/v5/asset/transfer/query-transfer-coin-list`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
[fromAccountType](/docs/v5/enum#accounttype)| **true**|  string| From account type  
[toAccountType](/docs/v5/enum#accounttype)| **true**|  string| To account type  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
list| array| A list of coins (as strings)  
[](/docs/api-explorer/v5/asset/transferable-coin)

* * *

### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/asset/transfer/query-transfer-coin-list?fromAccountType=UNIFIED&toAccountType=CONTRACT HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1672144322595  
    X-BAPI-RECV-WINDOW: 5000  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.get_transferable_coin(  
        fromAccountType="UNIFIED",  
        toAccountType="CONTRACT",  
    ))  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
      testnet: true,  
      key: 'xxxxxxxxxxxxxxxxxx',  
      secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
      .getTransferableCoinList('UNIFIED', 'CONTRACT')  
      .then((response) => {  
        console.log(response);  
      })  
      .catch((error) => {  
        console.error(error);  
      });  
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "success",  
        "result": {  
            "list": [  
                "BTC",  
                "ETH"  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1672144322954  
    }

---

# 帳戶類型間可劃轉的幣種

### HTTP 請求

GET`/v5/asset/transfer/query-transfer-coin-list`

### HTTP 請求

參數| 是否必需| 類型| 說明  
---|---|---|---  
[fromAccountType](/docs/zh-TW/v5/enum#accounttype)| **true**|  string| 劃出帳戶類型  
[toAccountType](/docs/zh-TW/v5/enum#accounttype)| **true**|  string| 劃入帳戶類型  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
list| array| 幣種數組  
[](/docs/zh-TW/api-explorer/v5/asset/transferable-coin)

* * *

### 請求示例

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/asset/transfer/query-transfer-coin-list?fromAccountType=UNIFIED&toAccountType=CONTRACT HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1672144322595  
    X-BAPI-RECV-WINDOW: 5000  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.get_transferable_coin(  
        fromAccountType="UNIFIED",  
        toAccountType="CONTRACT",  
    ))  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
      testnet: true,  
      key: 'xxxxxxxxxxxxxxxxxx',  
      secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
      .getTransferableCoinList('UNIFIED', 'CONTRACT')  
      .then((response) => {  
        console.log(response);  
      })  
      .catch((error) => {  
        console.error(error);  
      });  
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "success",  
        "result": {  
            "list": [  
                "BTC",  
                "ETH"  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1672144322954  
    }