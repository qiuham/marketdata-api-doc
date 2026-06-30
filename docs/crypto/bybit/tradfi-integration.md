---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/tradfi-integration
api_type: REST
updated_at: 2026-06-30 19:31:40.800126
---

# Get Friend Referrals

tip

Any permission can access this endpoint.

### HTTP Request

GET`/v5/user/invitation/referrals`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
status| false| string| Invitation relationship status, `0`: alive; `1`: invalid. By default, returns all status  
size| false| string| Data size per page [1, 100]. Return 20 records by default  
cursor| false| string| Cursor. Use the `nextCursor` token from the response to retrieve the next page of the result set  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
nextCursor| string| The next page cursor value  
records| array| Object  
> id| string| ID, internal userd  
> inviteeUid| string| Invitee userID  
> status| integer| Invitation relationship status, `0`: alive; `1`: invalid  
> createdAt| string| Created timestamp  
> updatedAt| string| Updated timestamp  
  
### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/user/invitation/referrals?status=0&size=5&cursor=6867 HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: XXXXXX  
    X-BAPI-TIMESTAMP: 1772095760290  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.get_friend_referrals(  
        status="0",  
        size="5",  
        cursor="6867"  
    ))  
    
    
    
      
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "",  
        "result": {  
            "nextCursor": "",  
            "records": [  
                {  
                    "id": "6866",  
                    "inviteeUid": "1447787",  
                    "status": 0,  
                    "createdAt": "1681206247",  
                    "updatedAt": "1681206247"  
                },  
                {  
                    "id": "6863",  
                    "inviteeUid": "1447350",  
                    "status": 0,  
                    "createdAt": "1681192249",  
                    "updatedAt": "1681192248"  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1772095760428  
    }

---

# 查詢好友被邀請人

提示

  * 任意權限可以訪問該接口



### HTTP 請求

GET`/v5/user/invitation/referrals`

### 請求參數

參數| 是否必須| 類型| 說明  
---|---|---|---  
status| false| string| 邀請關係狀態, `0`: 存活; `1`: 失效. 默認返回全部狀態  
size| false| string| 每頁數量限制. [`1`, `100`]. 默認: `20`  
cursor| false| string| 游標，用於翻頁  
  
### 返回參數

參數| 類型| 說明  
---|---|---  
nextCursor| string| 游標，用於翻頁  
records| array| Object  
> id| string| ID, 內部使用  
> inviteeUid| string| 被邀請人uid  
> status| integer| 邀請關係狀態, `0`: 存活; `1`: 失效  
> createdAt| string| 紀錄創建時間戳  
> updatedAt| string| 紀錄更新時間戳  
  
### 請求示例
    
    
    GET /v5/user/invitation/referrals?status=0&size=5&cursor=6867 HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: XXXXXX  
    X-BAPI-TIMESTAMP: 1772095760290  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "",  
        "result": {  
            "nextCursor": "",  
            "records": [  
                {  
                    "id": "6866",  
                    "inviteeUid": "1447787",  
                    "status": 0,  
                    "createdAt": "1681206247",  
                    "updatedAt": "1681206247"  
                },  
                {  
                    "id": "6863",  
                    "inviteeUid": "1447350",  
                    "status": 0,  
                    "createdAt": "1681192249",  
                    "updatedAt": "1681192248"  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1772095760428  
    }