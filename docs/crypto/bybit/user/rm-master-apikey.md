---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/user/rm-master-apikey
api_type: REST
updated_at: 2026-07-06 19:31:34.078030
---

# Delete Sub API Key

Delete the api key of sub account. Use the sub api key pending to be delete to call the endpoint or use the master api key to delete corresponding sub account api key

tip

The API key must have one of the below permissions in order to call this endpoint.

  * sub API key: "Account Transfer", "Sub Member Transfer"
  * master API Key: "Account Transfer", "Sub Member Transfer", "Withdrawal"



danger

BE CAREFUL! The Sub account API key will be invalid immediately after calling the endpoint.

### HTTP Request

POST`/v5/user/delete-sub-api`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
apikey| false| string| Sub account api key 

  * You must pass this param when you use master account manage sub account api key settings
  * If you use corresponding sub uid api key call this endpoint, `apikey` param cannot be passed, otherwise throwing an error

  
  
### Response Parameters

None

### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    POST /v5/user/delete-sub-api HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1676431922953  
    X-BAPI-RECV-WINDOW: 5000  
    X-BAPI-SIGN: XXXXXX  
    Content-Type: application/json  
      
    {  
      
    }  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.delete_sub_api_key())  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
      testnet: true,  
      key: 'xxxxxxxxxxxxxxxxxx',  
      secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
      .deleteSubApiKey()  
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
        "result": {},  
        "retExtInfo": {},  
        "time": 1676431924719  
    }

---

# 刪除子帳戶下的API Key

刪除子帳戶下的api key。使用待刪除的子帳戶api key調用接口或者使用母帳戶調用刪除指定api key

提示

在調用接口時，使用的API key至少需要擁有以下其中一種權限

  * 子API key: "Account Transfer（資產帳戶劃轉）", "Subaccount Transfer（母子帳戶劃轉）"
  * 母API key: "Account Transfer（資產帳戶劃轉）", "Subaccount Transfer（母子帳戶劃轉）", "Withdrawal（提幣）"



危險

當心! 用於調用本接口後, 對應的子帳戶api key會立馬失效。

### HTTP 請求

POST`/v5/user/delete-sub-api`

### 請求參數

參數| 是否必須| 類型| 說明  
---|---|---|---  
apikey| false| string| 子帳戶的api key 

  * 當您要使用母帳戶來管理子帳戶的key時, 該字段必傳
  * 如果您是用對應的子帳戶api key修改本身, 該字段請不要傳入, 否則報錯

  
  
### 返回參數

無

### 請求示例

  * HTTP
  * Python
  * Node.js


    
    
    POST /v5/user/delete-sub-api HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1676431922953  
    X-BAPI-RECV-WINDOW: 5000  
    X-BAPI-SIGN: XXXXXX  
    Content-Type: application/json  
      
    {  
      
    }  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.delete_sub_api_key())  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
      testnet: true,  
      key: 'xxxxxxxxxxxxxxxxxx',  
      secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
      .deleteSubApiKey()  
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
        "result": {},  
        "retExtInfo": {},  
        "time": 1676431924719  
    }