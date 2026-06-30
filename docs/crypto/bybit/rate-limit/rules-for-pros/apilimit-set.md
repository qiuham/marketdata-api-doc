---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/rate-limit/rules-for-pros/apilimit-set
api_type: REST
updated_at: 2026-06-30 19:29:55.254569
---

# Set Rate Limit

> API rate limit: 50 req per second

info

  * If the UID requesting this endpoint is a master account, UIDs passed to the `uids` parameter must be subaccounts of the master account.
  * If the UID requesting this endpoint is not a master account, the UID passed to the `uids` parameter must be the UID of the subaccount requesting this endpoint.
  * Only institutional users can request this endpoint.



### HTTP Request

POST`/v5/apilimit/set`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
list| **true**|  array| Object  
> uids| **true**|  string| Multiple UIDs separated by commas  
> [bizType](/docs/v5/enum#biztype)| **true**|  string| Business type  
> rate| **true**|  integer| API rate limit per second  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
list| array| Object  
> uids| string| Multiple UIDs separated by commas  
> [bizType](/docs/v5/enum#biztype)| string| Business type  
> rate| integer| API rate limit per second  
> success| boolean| Whether or not the request was successful  
> [msg](/docs/v5/enum#msg)| string| Result message  
  
### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    POST /v5/apilimit/set HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1711420489915  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "list": [  
            {  
                "uids": "106293838",  
                "bizType": "DERIVATIVES",  
                "rate": 50  
            }  
        ]  
    }  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.set_api_rate_limit(  
        list=[  
            {  
                "uids": "106293838",  
                "bizType": "DERIVATIVES",  
                "rate": 50  
            }  
        ]  
    ))  
    
    
    
      
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "success",  
        "result": {  
            "result": [  
                {  
                    "uids": "290118",  
                    "bizType": "SPOT",  
                    "rate": 600,  
                    "success": true,  
                    "msg": "API limit updated successfully"  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1754894296913  
    }

---

# 設定 API 速率限制

### 設定 API 速率限制

> API 速率限制：每秒 50 個請求

信息

  * 如果請求接口使用者是母帳戶，需要提頻的uid必須是所屬該母帳戶
  * 如果請求使用者非母帳戶，則提頻的uid必須是自己
  * UID必須屬於機構用户



### HTTP 請求

POST`/v5/apilimit/set`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
list| true| array| Object  
> uids| true| string| uid列表，多個以逗號隔開  
> [bizType](/docs/zh-TW/v5/enum#biztype)| true| string| 業務類型  
> rate| true| integer| api rate limit 每秒頻率  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
list| array| Object  
> uids| string| uid列表，多個以逗號隔開  
> [bizType](/docs/zh-TW/v5/enum#biztype)| string| 業務類型  
> rate| integer| api rate limit 每秒頻率  
> success| boolean| 是否成功  
> [msg](/docs/zh-TW/v5/enum#msg)| string| 結果訊息  
  
### 請求實例
    
    
    POST /v5/apilimit/set HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1711420489915  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "list": [  
            {  
                "uids": "106293838",  
                "bizType": "DERIVATIVES",  
                "rate": 50  
            }  
        ]  
    }  
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "success",  
        "result": {  
            "result": [  
                {  
                    "uids": "290118",  
                    "bizType": "SPOT",  
                    "rate": 600,  
                    "success": true,  
                    "msg": "API limit updated successfully"  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1754894296913  
    }