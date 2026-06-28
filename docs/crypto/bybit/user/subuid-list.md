---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/user/subuid-list
api_type: REST
updated_at: 2026-05-27 19:23:08.404366
---

# Get UID Wallet Type

Get available wallet types for the master account or sub account

tip

  * Master api key: you can get master account and appointed sub account available wallet types, and support up to 200 sub UID in one request.
  * Sub api key: you can get its own available wallet types



### HTTP Request

GET`/v5/user/get-member-type`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
memberIds| false| string| 

  * Query itself wallet types when not passed
  * When use master api key to query sub UID, master UID data is always returned in the top of the array
  * Multiple sub UID are supported, separated by commas
  * This param is ignored when you use sub account api key

  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
accounts| array| Object  
> uid| string| Master/Sub user Id  
> [accountType](/docs/v5/enum#accounttype)| array| Wallets array. `FUND`,`UNIFIED`  
[](/docs/api-explorer/v5/user/wallet-type)

* * *

### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/user/get-member-type HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1686884973961  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.get_uid_wallet_type(  
        memberIds="subUID1,subUID2"  
    ))  
    
    
    
    // https://api.bybit.com/v5/user/get-member-type  
      
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
      testnet: true,  
      key: 'xxxxxxxxxxxxxxxxxx',  
      secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
      .getUIDWalletType({  
        memberIds: 'subUID1,subUID2',  
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
        "retMsg": "",  
        "result": {  
            "accounts": [  
                {  
                    "uid": "533285",  
                    "accountType": [  
                        "UNIFIED",  
                        "FUND"  
                    ]  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1686884974151  
    }

---

# 查詢帳戶支持的錢包類型

查詢母帳戶或者子帳戶下支持的錢包類型

提示

  * 使用母帳戶api key: 您可以查詢到母帳戶以及指定的子帳戶的錢包類型, 子帳戶的uid最多單次可查詢200個.
  * 使用子帳戶api key: 僅能查詢自身的錢包類型



最佳實踐

"FUND" - 這個資金錢包, 如果您從未存入或者轉入過資金, 該接口返回的數組裡將不會呈現該枚舉值, 但實際上您的帳戶總是擁有該錢包.

  * `["SPOT","OPTION","FUND","CONTRACT"]` : 經典帳戶並且資金錢包曾經操作過
  * `["SPOT","OPTION","CONTRACT"]` : 經典帳戶並且資金錢包不曾操作過
  * `["SPOT","UNIFIED","FUND","CONTRACT"]` : UMA帳戶並且資金錢包曾經操作過. (等強制或主動升級到UTA後, 就沒有UMA帳戶的概念了)
  * `["SPOT","UNIFIED","CONTRACT"]` : UMA帳戶並且資金錢包不曾操作過. (等強制或主動升級到UTA後, 就沒有UMA帳戶的概念了)
  * `["UNIFIED""FUND","CONTRACT"]` : UTA帳戶並且資金錢包曾經操作過
  * `["UNIFIED","CONTRACT"]` : UTA帳戶並且資金錢包不曾操作過



### HTTP 請求

GET`/v5/user/get-member-type`

### 請求參數

參數| 是否必須| 類型| 說明  
---|---|---|---  
memberIds| false| string| 

  * 不入参時, 僅查詢自身
  * 當使用母帳戶api key查詢子uid時, 母帳戶的數據總是返回且在數組的第一個
  * 支持輸入多個子uid, 用逗號隔開, 單次查詢最多支持200個
  * 子帳戶api key查詢時, 該入参將會被忽略

  
  
### 返回參數

參數| 類型| 說明  
---|---|---  
accounts| array| Object  
> uid| string| 母/子 uid  
> [accountType](/docs/zh-TW/v5/enum#accounttype)| array| `SPOT`, `CONTRACT`, `FUND`, `OPTION`, `UNIFIED`. 請查閱上面的最佳實踐來理解返回的值  
[](/docs/zh-TW/api-explorer/v5/user/wallet-type)

* * *

### 請求示例

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/user/get-member-type HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1686884973961  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
    
    
    
      
    
    
    
    // https://api.bybit.com/v5/user/get-member-type  
      
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
      testnet: true,  
      key: 'xxxxxxxxxxxxxxxxxx',  
      secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
      .getUIDWalletType({  
        memberIds: 'subUID1,subUID2',  
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
        "retMsg": "",  
        "result": {  
            "accounts": [  
                {  
                    "uid": "24617703",  
                    "accountType": [  
                        "SPOT",  
                        "OPTION",  
                        "FUND",  
                        "CONTRACT"  
                    ]  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1686895670002  
    }