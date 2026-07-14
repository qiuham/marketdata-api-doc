---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/user/sign-agreement
api_type: REST
updated_at: 2026-07-14 18:57:50.254575
---

# Get Sub UID List (Limited)

Get at most 1,000 sub UID of master account, please use [Get Sub UID List (Unlimited)](/docs/v5/user/page-subuid) if you have more subaccounts. Use **master user's api key** **only**.

tip

The API key must have one of the below permissions in order to call this endpoint..

  * master API key: "Account Transfer", "Subaccount Transfer", "Withdrawal"



### HTTP Request

GET`/v5/user/query-sub-members`

### Request Parameters

None

### Response Parameters

Parameter| Type| Comments  
---|---|---  
subMembers| array| Object  
> uid| string| Sub user Id  
> username| string| Username  
> memberType| integer| `1`: normal subaccount, `6`: custodial sub account  
> status| integer| The status of the user account

  * `1`: normal
  * `2`: login banned
  * `4`: frozen 

  
> accountMode| integer| The account mode of the user account

  * `1`: Classic Account
  * `3`: UTA1.0
  * `4`: UTA1.0 Pro
  * `5`: UTA2.0
  * `6`: UTA2.0 Pro

  
> remark| string| The remark  
  
### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/user/query-sub-members HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1676430318405  
    X-BAPI-RECV-WINDOW: 5000  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.get_sub_uid())  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
      testnet: true,  
      key: 'xxxxxxxxxxxxxxxxxx',  
      secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
      .getSubUIDList()  
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
            "subMembers": [  
                {  
                    "uid": "106314365",  
                    "username": "xxxx02",  
                    "memberType": 1,  
                    "status": 1,  
                    "remark": "",  
                    "accountMode": 5  
                },  
                {  
                    "uid": "106279879",  
                    "username": "xxxx01",  
                    "memberType": 1,  
                    "status": 1,  
                    "remark": "",  
                    "accountMode": 6  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1760388036728  
    }

---

# 查詢子帳戶UID列表 (限制)

最多返回1000個子帳戶, 適合子帳戶較少的母帳戶調用, 需使用**母** 帳戶的API key。如您有較多的子帳戶, 請使用[查詢子帳戶UID列表 (無限制)](/docs/zh-TW/v5/user/page-subuid)接口。

提示

在調用接口時，使用的API key至少需要擁有以下其中一種權限

  * 母API key: "Account Transfer（資產帳戶劃轉）", "Subaccount Transfer（母子帳戶劃轉）", "Withdrawal（提幣）"



### HTTP 請求

GET`/v5/user/query-sub-members`

### 請求參數

無

### 返回參數

參數| 類型| 說明  
---|---|---  
subMembers| array| Object  
> uid| string| 子帳戶userId  
> username| string| 用戶名  
> memberType| integer| `1`: 普通子帳戶, `6`: 託管子帳戶  
> status| integer| 帳戶狀態.

  * `1`: 正常
  * `2`: 登陸封禁
  * `4`: 凍結 

  
> accountMode| integer| 帳戶模式.

  * `1`: 經典帳戶
  * `3`: UTA帳戶
  * `4`: UTA1.0 Pro 帳戶
  * `5`: UTA2.0 帳戶
  * `6`: UTA2.0 Pro 帳戶

  
> remark| string| 備註  
  
### 請求示例

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/user/query-sub-members HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1676430318405  
    X-BAPI-RECV-WINDOW: 5000  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.get_sub_uid())  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
      testnet: true,  
      key: 'xxxxxxxxxxxxxxxxxx',  
      secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
      .getSubUIDList()  
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
            "subMembers": [  
                {  
                    "uid": "106314365",  
                    "username": "xxxx02",  
                    "memberType": 1,  
                    "status": 1,  
                    "remark": "",  
                    "accountMode": 5  
                },  
                {  
                    "uid": "106279879",  
                    "username": "xxxx01",  
                    "memberType": 1,  
                    "status": 1,  
                    "remark": "",  
                    "accountMode": 6  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1760388036728  
    }