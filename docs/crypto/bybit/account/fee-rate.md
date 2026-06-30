---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/account/fee-rate
api_type: Account
updated_at: 2026-06-30 19:22:04.675950
---

# Get MMP State

### HTTP Request

GET`/v5/account/mmp-state`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
baseCoin| **true**|  string| Base coin, uppercase only  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
result| array| Object  
> baseCoin| string| Base coin  
> mmpEnabled| boolean| Whether the account is enabled mmp  
> window| string| Time window (ms)  
> frozenPeriod| string| Frozen period (ms)  
> qtyLimit| string| Trade qty limit  
> deltaLimit| string| Delta limit  
> vegaLimit| string| Vega limit  
> mmpFrozenUntil| string| Unfreeze timestamp (ms)  
> mmpFrozen| boolean| Whether the mmp is triggered. 

  * `true`: mmpFrozenUntil is meaningful
  * `false`: please ignore the value of mmpFrozenUntil

  
  
### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    POST /v5/account/mmp-reset HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1675842997277  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "baseCoin": "ETH"  
    }  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.get_mmp_state(  
        baseCoin="ETH",  
    ))  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
        testnet: true,  
        key: 'xxxxxxxxxxxxxxxxxx',  
        secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
        .getMMPState('ETH')  
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
            "result": [  
                {  
                    "baseCoin": "BTC",  
                    "mmpEnabled": true,  
                    "window": "5000",  
                    "frozenPeriod": "100000",  
                    "qtyLimit": "0.01",  
                    "deltaLimit": "0.01",  
                    "vegaLimit": "500000",  
                    "mmpFrozenUntil": "1675760625519",  
                    "mmpFrozen": false  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1675843188984  
    }

---

# 查詢市商保護配置信息

### HTTP 請求

GET`/v5/account/mmp-state`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
baseCoin| **true**|  string| Base coin  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
result| array| Object  
> baseCoin| string| 交易幣種  
> mmpEnabled| boolean| 帳戶是否開啟了mmp  
> window| string| 時間窗口 (毫秒)  
> frozenPeriod| string| 凍結時間長度 (毫秒)  
> qtyLimit| string| 成交數量上限  
> deltaLimit| string| Delta值上限  
> vegaLimit| string| Vega 上限  
> mmpFrozenUntil| string| 解凍時間戳 (毫秒)  
> mmpFrozen| boolean| 當前是否觸發了mmp凍結. 

  * `true`: mmpFrozenUntil的值有意義
  * `false`: 請忽略mmpFrozenUntil字段的值

  
  
### 請求示例

  * HTTP
  * Python
  * Node.js


    
    
    POST /v5/account/mmp-reset HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1675842997277  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "baseCoin": "ETH"  
    }  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.get_mmp_state(  
        baseCoin="ETH",  
    ))  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
        testnet: true,  
        key: 'xxxxxxxxxxxxxxxxxx',  
        secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
        .getMMPState('ETH')  
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
            "result": [  
                {  
                    "baseCoin": "BTC",  
                    "mmpEnabled": true,  
                    "window": "5000",  
                    "frozenPeriod": "100000",  
                    "qtyLimit": "0.01",  
                    "deltaLimit": "0.01",  
                    "vegaLimit": "500000",  
                    "mmpFrozenUntil": "1675760625519",  
                    "mmpFrozen": false  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1675843188984  
    }