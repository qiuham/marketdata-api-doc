---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/rate-limit/rules-for-pros/apilimit-query
api_type: REST
updated_at: 2026-07-10 19:04:58.360434
---

# Get All Rate Limits

> API rate limit: 50 req per second

info

  * Query for all your UID-level rate limits, including all master accounts and subaccounts.



### HTTP Request

GET`/v5/apilimit/query-all`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
limit| false| string| Limit for data size per page. [`1`, `1000`]. Default: `1000`  
cursor| false| string| Cursor. Use the `nextPageCursor` token from the response to retrieve the next page of the result set  
uids| false| string| Multiple UIDs across different master accounts, separated by commas. Returns all master accounts and subaccounts by default  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
nextPageCursor| string| Refer to the `cursor` request parameter  
list| array| Object  
> uids| string| Multiple UIDs separated by commas  
> [bizType](/docs/v5/enum#biztype)| string| Business type  
> rate| integer| API Rate limit per second  
  
### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/apilimit/query-all HTTP/1.1  
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
    print(session.get_all_api_rate_limits())  
    
    
    
      
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "success",  
        "result": {  
            "list": [  
                {  
                    "uids": "104270393,1674166,1190923,101446030",  
                    "bizType": "SPOT",  
                    "rate": 223  
                },  
                {  
                    "uids": "104074050,104394193,104126066",  
                    "bizType": "OPTIONS",  
                    "rate": 223  
                },  
                {  
                    "uids": "104154966,103803484,103995540,100445068",  
                    "bizType": "DERIVATIVES",  
                    "rate": 298  
                }  
            ],  
            "nextPageCursor": ""  
        },  
        "retExtInfo": {},  
        "time": 1758857701702  
    }

---

# 查詢所有 API 限速

### 查詢所有 API 限速

> API 限速：每秒 50 次請求  
> 

信息

  * 查詢所有 UID 等級的限速，包括主帳戶及所有子帳戶。
  * 僅允許透過main UID或來自sub-INS API key的子帳戶 UID 進行查詢



### HTTP 請求

GET`/v5/apilimit/query-all`

### 請求參數

參數| 必填| 類型| 說明  
---|---|---|---  
limit| false| string| 每頁資料大小限制。[`1`, `1000`]。預設值：`1000`  
cursor| false| string| 游標。使用回應中的 `nextPageCursor` 令牌以取得下一頁結果集  
uids| false| string| 跨主帳戶的多個 UID，以逗號分隔。預設返回所有主帳戶及子帳戶的限速  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
nextPageCursor| string| 用於取得下一頁資料  
list| array| Object  
> uids| string| 多個 UID，以逗號分隔。  
> [bizType](/docs/zh-TW/v5/enum#biztype)| string| 業務類型  
> rate| integer| 每秒 API 限速  
  
### 請求範例
    
    
    GET /v5/apilimit/query-all HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1728460942776  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
    Content-Length: 2  
    

### 響應範例
    
    
    {  
        "retCode": 0,  
        "retMsg": "success",  
        "result": {  
            "list": [  
                {  
                    "uids": "104270393,1674166,1190923,101446030",  
                    "bizType": "SPOT",  
                    "rate": 223  
                },  
                {  
                    "uids": "104074050,104394193,104126066",  
                    "bizType": "OPTIONS",  
                    "rate": 223  
                },  
                {  
                    "uids": "104154966,103803484,103995540,100445068",  
                    "bizType": "DERIVATIVES",  
                    "rate": 298  
                }  
            ],  
            "nextPageCursor": ""  
        },  
        "retExtInfo": {},  
        "time": 1758857701702  
    }