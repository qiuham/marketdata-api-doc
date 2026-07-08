---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/strategy/strategy-list
api_type: REST
updated_at: 2026-07-08 19:04:56.086723
---

# Create Sub UID

Create a new sub user id. Use **master** account's api key.

tip

The API key must have one of the below permissions in order to call this endpoint

  * master API key: "Account Transfer", "Subaccount Transfer", "Withdrawal"



### HTTP Request

POST`/v5/user/create-sub-member`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
username| **true**|  string| Username of the new sub user. 

  * 6-16 characters, must include both numbers and letters.
  * Cannot be the same as the existing or deleted usernames.

  
password| false| string| Password for the new sub user. 

  * 8-30 characters, must include numbers, upper and lowercase letters.

  
memberType| **true**|  integer| `1`: normal subaccount, `6`: [custodial subaccount](https://www.bybit.com/en/help-center/article?id=000001683)  
switch| false| integer| 

  * `0`: turn off quick login (default)
  * `1`: turn on quick login.

  
isUta| false| boolean| **Deprecated** param, always UTA account  
note| false| string| Set a remark  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
uid| string| Sub user Id  
username| string| Username of the new sub user. 

  * 6-16 characters, must include both numbers and letters.
  * Cannot be the same as the existing or deleted usernames.

  
memberType| integer| `1`: normal subaccount, `6`: [custodial subaccount](https://www.bybit.com/en/help-center/article?id=000001683)  
status| integer| The status of the user account

  * `1`: normal
  * `2`: login banned
  * `4`: frozen 

  
remark| string| The remark  
  
### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    POST /v5/user/create-sub-member HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1676429344202  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "username": "xxxxx",  
        "memberType": 1,  
        "switch": 1,  
        "note": "test"  
    }  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.create_sub_uid(  
        username="xxxxx",  
        memberType=1,  
        switch=1,  
        note="test",  
    ))  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
      testnet: true,  
      key: 'xxxxxxxxxxxxxxxxxx',  
      secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
      .createSubMember({  
        username: 'xxxxx',  
        memberType: 1,  
        switch: 1,  
        note: 'test',  
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
            "uid": "53888000",  
            "username": "xxxxx",  
            "memberType": 1,  
            "status": 1,  
            "remark": "test"  
        },  
        "retExtInfo": {},  
        "time": 1676429344734  
    }

---

# 新建子帳戶

創建新的子帳戶。需使用**母** 帳戶的API key。

提示

在調用接口時，使用的API key至少需要擁有以下其中一種權限

  * 母API key: "Account Transfer（資產帳戶劃轉）", "Subaccount Transfer（母子帳戶劃轉）", "Withdrawal（提幣）"



### HTTP 請求

POST`/v5/user/create-sub-member`

### 請求參數

參數| 是否必須| 類型| 說明  
---|---|---|---  
username| **true**|  string| 給新的子帳戶創建一個用戶名。

  * 6-16位字符，須同時含有數字和字母。
  * 不能與已存在或已刪除的帳戶用戶名重複。

  
password| false| string| 給新的子帳戶設置一個密碼。

  * 8-30位字符，須同時含有數字和大小寫字母。

  
memberType| **true**|  integer| `1`: 普通子帳戶, `6`: 託管子帳戶  
switch| false| integer| 

  * `0`: 關閉快捷登陸 (默認關閉)
  * `1`: 打開快捷登陸.

  
isUta| false| boolean| **廢棄** , 總是創建UTA子帳戶  
note| false| string| 設置備註  
  
### 返回參數

參數| 類型| 說明  
---|---|---  
uid| string| 子帳戶userId  
username| string| 給新的子帳戶創建一個用戶名 

  * 6-16位字符，須同時含有數字和字母。
  * 不能與已存在或已刪除的帳戶用戶名重複。

  
memberType| integer| `1`: 普通子帳戶, `6`: 託管子帳戶  
status| integer| 帳戶狀態

  * `1`: 正常
  * `2`: 登陸封禁
  * `4`: 凍結 

  
remark| string| 設置的備註  
  
### 請求示例

  * HTTP
  * Python
  * Node.js


    
    
    POST /v5/user/create-sub-member HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1676429344202  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "username": "xxxxx",  
        "memberType": 1,  
        "switch": 1,  
        "note": "test"  
    }  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.create_sub_uid(  
        username="xxxxx",  
        memberType=1,  
        switch=1,  
        note="test",  
    ))  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
      testnet: true,  
      key: 'xxxxxxxxxxxxxxxxxx',  
      secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
      .createSubMember({  
        username: 'xxxxx',  
        memberType: 1,  
        switch: 1,  
        note: 'test',  
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
            "uid": "53888000",  
            "username": "xxxxx",  
            "memberType": 1,  
            "status": 1,  
            "remark": "test"  
        },  
        "retExtInfo": {},  
        "time": 1676429344734  
    }