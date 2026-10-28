---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/user/friend-referral
api_type: REST
updated_at: 2026-10-28 18:42:31.375579
---

# Get Fund Custodial Sub Acct

The institutional client can query the fund custodial sub accounts.

tip

The API key must have one of the below permissions in order to call this endpoint..

  * master API key: "Account Transfer", "Subaccount Transfer", "Withdrawal"



### HTTP Request

GET`/v5/user/escrow_sub_members`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
pageSize| false| string| Data size per page. Return up to 100 records per request  
nextCursor| false| string| Cursor. Use the `nextCursor` token from the response to retrieve the next page of the result set  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
subMembers| array| Object  
> uid| string| Sub userId  
> username| string| User name  
> memberType| integer| `12`: Fund custodial account  
> status| integer| Account state.

  * `1`: normal
  * `2`: forbidden login
  * `4`: frozen 

  
> accountMode| integer| Account mode.

  * `1`: classic account
  * `3`: UTA account 

  
> remark| string| Remark  
nextCursor| string| The next page cursor value. "0" means no more pages  
  
### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/user/escrow_sub_members?pageSize=2 HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1739763787703  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.get_escrow_sub_members(  
        pageSize="2"  
    ))  
    
    
    
      
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "",  
        "result": {  
            "subMembers": [  
                {  
                    "uid": "104274894",  
                    "username": "Private_Wealth_Management",  
                    "memberType": 12,  
                    "status": 1,  
                    "remark": "earn fund",  
                    "accountMode": 3  
                },  
                {  
                    "uid": "104274884",  
                    "username": "Private_Wealth_Management",  
                    "memberType": 12,  
                    "status": 1,  
                    "remark": "earn fund",  
                    "accountMode": 3  
                }  
            ],  
            "nextCursor": "344"  
        },  
        "retExtInfo": {},  
        "time": 1739763788699  
    }

---

# 查詢基金託管子帳戶列表

託管機構可以通過這個接口查詢到基金託管子帳戶列表

提示

在調用接口時，使用的API key至少需要擁有以下其中一種權限

  * 母API key: "Account Transfer（資產帳戶劃轉）", "Subaccount Transfer（母子帳戶劃轉）", "Withdrawal（提幣）"



### HTTP 請求

GET`/v5/user/escrow_sub_members`

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
> memberType| integer| `12`: 基金託管子帳戶  
> status| integer| 帳戶狀態.

  * `1`: 正常
  * `2`: 登陸封禁
  * `4`: 凍結 

  
> accountMode| integer| 帳戶模式.

  * `1`: 經典帳戶
  * `3`: UTA帳戶 

  
> remark| string| 備註  
nextCursor| string| 下一頁數據的游標. 返回"0"表示沒有更多的數據了  
  
### 請求示例

  * HTTP
  * Python


    
    
    GET /v5/user/escrow_sub_members?pageSize=2 HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1739763787703  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
    
    
    
      
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "",  
        "result": {  
            "subMembers": [  
                {  
                    "uid": "104274894",  
                    "username": "Private_Wealth_Management",  
                    "memberType": 12,  
                    "status": 1,  
                    "remark": "earn fund",  
                    "accountMode": 3  
                },  
                {  
                    "uid": "104274884",  
                    "username": "Private_Wealth_Management",  
                    "memberType": 12,  
                    "status": 1,  
                    "remark": "earn fund",  
                    "accountMode": 3  
                }  
            ],  
            "nextCursor": "344"  
        },  
        "retExtInfo": {},  
        "time": 1739763788699  
    }