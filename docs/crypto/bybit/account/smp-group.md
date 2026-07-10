---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/account/smp-group
api_type: Account
updated_at: 2026-07-10 18:57:00.221213
---

# Get SMP Group ID

Query the SMP group ID of self match prevention

### HTTP Request

GET`/v5/account/smp-group`

### Request Parameters

None

### Response Parameters

Parameter| Type| Comments  
---|---|---  
smpGroup| integer| Smp group ID. If the UID has no group, it is `0` by default  
  
### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/account/smp-group HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1702363848192  
    X-BAPI-RECV-WINDOW: 5000  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.get_smp_group())  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
      testnet: true,  
      key: 'xxxxxxxxxxxxxxxxxx',  
      secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
      .getSMPGroup()  
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
            "smpGroup": 0  
        },  
        "retExtInfo": {},  
        "time": 1702363848539  
    }

---

# 查詢SMP組ID

查詢自成交攔截的SMP交易群組ID

### HTTP 請求

GET`/v5/account/smp-group`

### 請求參數

無

### 響應參數

參數| 類型| 說明  
---|---|---  
smpGroup| integer| 所屬Smp組ID. 如果uid不屬於任何組, 則默認為`0`  
  
### 請求示例

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/account/smp-group HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1702363848192  
    X-BAPI-RECV-WINDOW: 5000  
    
    
    
      
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
      testnet: true,  
      key: 'xxxxxxxxxxxxxxxxxx',  
      secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
      .getSMPGroup()  
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
            "smpGroup": 0  
        },  
        "retExtInfo": {},  
        "time": 1702363848539  
    }