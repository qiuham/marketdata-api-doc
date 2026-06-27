---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/rate-limit
api_type: REST
updated_at: 2026-05-27 19:21:23.810785
---

# Get Rate Limit

> API rate limit: 50 req per second

info

  * A master account can query its own and its subaccounts' API rate limit.
  * A subaccount can only query its own API rate limit.



### HTTP Request

GET`/v5/apilimit/query`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
uids| **true**|  string| Multiple UIDs separated by commas  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
list| array| Object  
> uids| string| Multiple UIDs separated by commas  
> [bizType](/docs/v5/enum#biztype)| string| Business type  
> rate| integer| API rate limit per second  
  
### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/apilimit/query?uids=290118 HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1728460942776  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
    Content-Length: 2  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.get_api_rate_limit(  
        uids="290118"  
    ))  
    
    
    
      
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "success",  
        "result": {  
            "list": [  
                {  
                    "uids": "290118",  
                    "bizType": "SPOT",  
                    "rate": 600  
                },  
                {  
                    "uids": "290118",  
                    "bizType": "DERIVATIVES",  
                    "rate": 400  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1754894341984  
    }

---

# 查詢 API 速率限制

### 查詢 API 速率限制

> API 速率限制：每秒 50 個請求

信息

  * 母帳戶能查詢自己和子帳戶的頻率
  * 子帳戶只能查詢自己的頻率



### HTTP 請求

GET`/v5/apilimit/query`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
uids| true| string| uid列表，多個以逗號隔開  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
list| array| Object  
> uids| string| uid列表，多個以逗號隔開  
> [bizType](/docs/zh-TW/v5/enum#biztype)| string| 業務類型  
> rate| integer| api rate limit 每秒頻率  
  
### 響應參數
    
    
    GET /v5/apilimit/query?uids=290118 HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1728460942776  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
    Content-Length: 2  
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "success",  
        "result": {  
            "list": [  
                {  
                    "uids": "290118",  
                    "bizType": "SPOT",  
                    "rate": 600  
                },  
                {  
                    "uids": "290118",  
                    "bizType": "DERIVATIVES",  
                    "rate": 400  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1754894341984  
    }