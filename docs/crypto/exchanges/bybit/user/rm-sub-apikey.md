---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/user/rm-sub-apikey
api_type: REST
updated_at: 2026-05-27 19:23:04.937288
---

# Delete Sub UID

Delete a sub UID. If a sub-account’s asset balance is greater than 0.001 USDT, it cannot be deleted.  
Use **master** user's api key**.

tip

The API key must have one of the below permissions in order to call this endpoint

  * master API key: "Account Transfer", "Subaccount Transfer", "Withdrawal"



### HTTP Request

POST`/v5/user/del-submember`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
subMemberId| **true**|  string| Sub UID  
  
### Response Parameters

None

### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    POST /v5/user/del-submember HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1698907012755  
    X-BAPI-RECV-WINDOW: 5000  
    X-BAPI-SIGN: XXXXXX  
    Content-Type: application/json  
    Content-Length: 34  
      
    {  
        "subMemberId": "112725187"  
    }  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.delete_sub_uid(  
        subMemberId="112725187"  
    ))  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
      testnet: true,  
      key: 'xxxxxxxxxxxxxxxxxx',  
      secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
      .deleteSubMember({  
        subMemberId: 'subUID',  
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
        "retMsg": "OK",  
        "result": {},  
        "retExtInfo": {},  
        "time": 1698907012962  
    }

---

# 刪除子帳戶

刪除子帳戶. 如果子帳號資產餘額大於 0.001U, 禁止刪除

  
僅可使用**母**帳戶api key調用.

提示

在調用接口時，使用的API key至少需要擁有以下其中一種權限

  * 母API key: "Account Transfer（資產帳戶劃轉）", "Subaccount Transfer（母子帳戶劃轉）", "Withdrawal（提幣）"



### HTTP 請求

POST`/v5/user/del-submember`

### 請求參數

參數| 是否必須| 類型| 說明  
---|---|---|---  
subMemberId| **true**|  string| Sub UID  
  
### 返回參數

無

### 請求示例

  * HTTP
  * Python
  * Node.js


    
    
    POST /v5/user/del-submember HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1698907012755  
    X-BAPI-RECV-WINDOW: 5000  
    X-BAPI-SIGN: XXXXXX  
    Content-Type: application/json  
    Content-Length: 34  
      
    {  
        "subMemberId": "112725187"  
    }  
    
    
    
      
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
      testnet: true,  
      key: 'xxxxxxxxxxxxxxxxxx',  
      secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
      .deleteSubMember({  
        subMemberId: 'subUID',  
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
        "retMsg": "OK",  
        "result": {},  
        "retExtInfo": {},  
        "time": 1698907012962  
    }