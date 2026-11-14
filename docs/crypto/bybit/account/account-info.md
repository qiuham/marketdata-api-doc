---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/account/account-info
api_type: Account
updated_at: 2026-11-13 19:20:42.654804
---

# Get Account Info

Query the account information, like margin mode, account mode, etc.

### HTTP Request

GET`/v5/account/info`

### Request Parameters

None

### Response Parameters

Parameter| Type| Comments  
---|---|---  
[unifiedMarginStatus](/docs/v5/enum#unifiedmarginstatus)| integer| Account status  
marginMode| string| `ISOLATED_MARGIN`, `REGULAR_MARGIN`, `PORTFOLIO_MARGIN`  
isMasterTrader| boolean| Whether this account is a leader (copytrading). `true`, `false`  
spotHedgingStatus| string| Whether the unified account enables Spot hedging. `ON`, `OFF`  
updatedTime| string| Account data updated timestamp (ms)  
dcpStatus| string| deprecated, always `OFF`. Please use [Get DCP Info](/docs/v5/account/dcp-info)  
timeWindow| integer| deprecated, always `0`. Please use [Get DCP Info](/docs/v5/account/dcp-info)  
smpGroup| integer| deprecated, always `0`. Please query [Get SMP Group ID](/docs/v5/account/smp-group) endpoint  
[](/docs/api-explorer/v5/account/account-info)

* * *

### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/account/info HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1672129307221  
    X-BAPI-RECV-WINDOW: 5000  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.get_account_info())  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
        testnet: true,  
        key: 'xxxxxxxxxxxxxxxxxx',  
        secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
        .getAccountInfo()  
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
            "marginMode": "REGULAR_MARGIN",  
            "updatedTime": "1697078946000",  
            "unifiedMarginStatus": 4,  
            "dcpStatus": "OFF",  
            "timeWindow": 10,  
            "smpGroup": 0,  
            "isMasterTrader": false,  
            "spotHedgingStatus": "OFF"  
        }  
    }

---

# 查詢賬戶配置

該接口可以查詢統一帳戶的保證金模式, 當前帳戶模式等配置

### HTTP 請求

GET`/v5/account/info`

### 請求參數

無

### 響應參數

參數| 類型| 說明  
---|---|---  
[unifiedMarginStatus](/docs/zh-TW/v5/enum#unifiedmarginstatus)| integer| 帳戶狀態類型  
marginMode| string| `ISOLATED_MARGIN`(逐倉保證金)  
`REGULAR_MARGIN`（全倉保證金）  
`PORTFOLIO_MARGIN`（組合保證金）  
isMasterTrader| boolean| 是否為帶單帳戶. `true`, `false`  
spotHedgingStatus| string| 是否開啟現貨對衝. `ON`, `OFF`  
updatedTime| string| 賬戶數據更新的時間，毫秒時間戳  
dcpStatus| string| **廢棄** 字段, 總是`OFF`. 請使用[查詢DCP配置](/docs/zh-TW/v5/account/dcp-info)  
timeWindow| integer| **廢棄** 字段, 總是`0`. 請使用[查詢DCP配置](/docs/zh-TW/v5/account/dcp-info)  
smpGroup| integer| **廢棄** 字段, 總是`0`. 請調用[查詢SMP組ID](/docs/zh-TW/v5/account/smp-group)  
[](/docs/zh-TW/api-explorer/v5/account/account-info)

* * *

### 請求示例

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/account/info HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1672129307221  
    X-BAPI-RECV-WINDOW: 5000  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.get_account_info())  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
        testnet: true,  
        key: 'xxxxxxxxxxxxxxxxxx',  
        secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
        .getAccountInfo()  
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
            "marginMode": "REGULAR_MARGIN",  
            "updatedTime": "1697078946000",  
            "unifiedMarginStatus": 4,  
            "dcpStatus": "OFF",  
            "timeWindow": 10,  
            "smpGroup": 0,  
            "isMasterTrader": false,  
            "spotHedgingStatus": "OFF"  
        }  
    }