---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/account/reset-mmp
api_type: Account
updated_at: 2026-11-13 19:20:52.096447
---

# Reset MMP

info

  * Once the mmp triggered, you can unfreeze the account by this endpoint, then `qtyLimit`, `deltaLimit` and `vegaLimit` will be reset to 0.
  * If the account is not frozen, reset action can also remove previous accumulation, i.e., `qtyLimit`, `deltaLimit` and `vegaLimit` will be reset to 0.



### HTTP Request

POST`/v5/account/mmp-reset`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
baseCoin| **true**|  string| Base coin, uppercase only  
  
### Response Parameters

None

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
    print(session.reset_mmp(  
        baseCoin="ETH",  
    ))  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
        testnet: true,  
        key: 'xxxxxxxxxxxxxxxxxx',  
        secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
        .resetMMP('ETH')  
        .then((response) => {  
            console.log(response);  
        })  
        .catch((error) => {  
            console.error(error);  
        });  
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "success"  
    }

---

# 重置市商保護凍結

信息

  * 一旦mmp被觸發, 您的帳戶可以調用該接口進行主動解凍, 解凍後, `qtyLimit`、`deltaLimit` 和 `vegaLimit` 就重置為0.
  * 若帳戶沒有被凍結, 該重置接口能夠清除之前的交易, 即不計算重置前發生的總數量和淨交易delta, `qtyLimit`、`deltaLimit` 和 `vegaLimit` 就重置為0.



### HTTP 請求

POST`/v5/account/mmp-reset`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
baseCoin| **true**|  string| 交易幣種  
  
### 響應參數

無

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
    print(session.reset_mmp(  
        baseCoin="ETH",  
    ))  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
        testnet: true,  
        key: 'xxxxxxxxxxxxxxxxxx',  
        secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
        .resetMMP('ETH')  
        .then((response) => {  
            console.log(response);  
        })  
        .catch((error) => {  
            console.error(error);  
        });  
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "success"  
    }