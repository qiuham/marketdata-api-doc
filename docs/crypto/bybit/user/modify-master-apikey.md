---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/user/modify-master-apikey
api_type: REST
updated_at: 2026-07-19 18:53:32.667530
---

# Get Sub UID List (Unlimited)

This API is applicable to the client who has over 10k sub accounts. Use **master user's api key** **only**.

tip

The API key must have one of the below permissions in order to call this endpoint..

  * master API key: "Account Transfer", "Subaccount Transfer", "Withdrawal"



### HTTP Request

GET`/v5/user/submembers`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
pageSize| false| string| Data size per page. Return up to 100 records per request  
nextCursor| false| string| Cursor. Use the `nextCursor` token from the response to retrieve the next page of the result set  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
subMembers| array| Object  
> uid| string| Sub user Id  
> username| string| Username  
> memberType| integer| `1`: standard subaccount, `6`: [custodial subaccount](https://www.bybit.com/en/help-center/article?id=000001683)  
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
nextCursor| string| The next page cursor value. "0" means no more pages  
  
### Request Example

  * HTTP
  * Python


    
    
    GET /v5/user/submembers?pageSize=1 HTTP/1.1  
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
    print(session.get_sub_uid_list_unlimited(  
        pageSize="1",  
    ))  
    

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
            ],  
            "nextCursor": "0"  
        },  
        "retExtInfo": {},  
        "time": 1760388041006  
    }

---

# 查詢子帳戶UID列表 (無限制)

通過翻頁獲取當前母帳戶下所有的子帳戶列表，適合超過擁有1萬個子帳戶的母帳戶進行調用。需使用**母** 帳戶的API key。

提示

在調用接口時，使用的API key至少需要擁有以下其中一種權限

  * 母API key: "Account Transfer（資產帳戶劃轉）", "Subaccount Transfer（母子帳戶劃轉）", "Withdrawal（提幣）"



### HTTP 請求

GET`/v5/user/submembers`

### 請求參數

參數| 是否必須| 類型| 說明  
---|---|---|---  
pageSize| false| string| 數據頁大小. 每次至多返回100條  
nextCursor| false| string| 游標. 傳入響應中的`nextCursor`來獲取下一頁的數據  
  
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
nextCursor| string| 下一頁數據的游標. 返回"0"表示沒有更多的數據了  
  
### 請求示例

  * HTTP
  * Python


    
    
    GET /v5/user/submembers?pageSize=1 HTTP/1.1  
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
    print(session.get_sub_uid_list_unlimited(  
        pageSize="1",  
    ))  
    

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
            ],  
            "nextCursor": "0"  
        },  
        "retExtInfo": {},  
        "time": 1760388041006  
    }