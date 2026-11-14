---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/asset/deposit/set-deposit-acct
api_type: REST
updated_at: 2026-11-13 19:21:37.673637
---

# Set Deposit Account

Set auto transfer account after deposit. The same function as the setting for Deposit on [web GUI](https://www.bybit.com/app/user/settings)

info

  * Your funds will be deposited into `FUND` wallet by default. You can set the wallet for auto-transfer after deposit by this API.
  * Only **main** UID can access.



### HTTP Request

POST`/v5/asset/deposit/deposit-to-account`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
[accountType](/docs/v5/enum#accounttype)| **true**|  string| Account type `UNIFIED`, `FUND`, `EARN`(if the coin does not support flexible saving, the funds would be transferred to funding wallet)  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
status| integer| Request result: 

  * `1`: SUCCESS
  * `0`: FAIL

  
[](/docs/api-explorer/v5/asset/set-deposit-acct)

* * *

### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    POST /v5/asset/deposit/deposit-to-account HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1676887913670  
    X-BAPI-RECV-WINDOW: 50000  
    Content-Type: application/json  
      
    {  
        "accountType": "CONTRACT"  
    }  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.set_deposit_account(  
        accountType="CONTRACT",  
    ))  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
      testnet: true,  
      key: 'xxxxxxxxxxxxxxxxxx',  
      secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
      .setDepositAccount({  
        accountType: 'CONTRACT'  
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
        "retMsg": "success",  
        "result": {  
            "status": 1  
        },  
        "retExtInfo": {},  
        "time": 1676887914363  
    }

---

# 設置充值帳戶

設置充值後的自動轉入帳戶類型。該功能與[網頁端](https://www.bybit.com/app/user/settings)-設置-充值保持一致。

信息

  * 資金會默認充值至資金帳戶, 通過該接口設置自動劃轉帳戶後，系統將會自動劃轉至目標帳戶。
  * 僅支持**主帳號** 調用。



### HTTP 請求

POST`/v5/asset/deposit/deposit-to-account`

### 請求參數

參數| 是否必須| 類型| 說明  
---|---|---|---  
[accountType](/docs/zh-TW/v5/enum#accounttype)| **true**|  string| 帳戶類型 

  * `UNIFIED（統一帳戶）`
  * `FUND（資金帳戶）`
  * `EARN（理財帳戶）`

  
  
### 返回參數

參數| 類型| 說明  
---|---|---  
status| integer| 請求狀態: 

  * `1`: 修改成功
  * `0`: 修改失敗

  
[](/docs/zh-TW/api-explorer/v5/asset/set-deposit-acct)

* * *

### 請求示例

  * HTTP
  * Python
  * Node.js


    
    
    POST /v5/asset/deposit/deposit-to-account HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1676887913670  
    X-BAPI-RECV-WINDOW: 50000  
    Content-Type: application/json  
      
    {  
        "accountType": "CONTRACT"  
    }  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.set_deposit_account(  
        accountType="CONTRACT",  
    ))  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
      testnet: true,  
      key: 'xxxxxxxxxxxxxxxxxx',  
      secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
      .setDepositAccount({  
        accountType: 'CONTRACT'  
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
        "retMsg": "success",  
        "result": {  
            "status": 1  
        },  
        "retExtInfo": {},  
        "time": 1676887914363  
    }