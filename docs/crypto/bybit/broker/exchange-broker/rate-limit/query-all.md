---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/broker/exchange-broker/rate-limit/query-all
api_type: REST
updated_at: 2026-05-27 19:16:04.423787
---

# Get All Rate Limits

> API rate limit: 1 req per second

info

  * Use the master account to query for all your UID-level rate limits, including all master accounts and subaccounts.
  * Only exchange broker account can call this endpoint
  * The accounts that have never had a rate limit configured via [Set Rate Limit](/docs/v5/broker/exchange-broker/rate-limit/set) will not appear in the response and will use the default rate limit.



### HTTP Request

GET`/v5/broker/apilimit/query-all`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
limit| false| string| Limit for data size per page. [`1`, `1000`]. Default: `1000`  
cursor| false| string| Cursor. Use the `nextPageCursor` token from the response to retrieve the next page of the result set  
uids| false| string| Multiple UIDs across different master accounts, separated by commas. Returns all subaccounts by default  
  
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


    
    
    GET /v5/broker/apilimit/query-all HTTP/1.1  
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
    print(session.get_broker_all_rate_limits())  
    
    
    
      
    

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

> API 限速：每秒 1 次請求  
> 

信息

  * 使用主帳戶查詢您所有 UID 層級的速率限制，包括所有主帳戶下的子帳戶
  * 僅交易所經紀商帳戶可以調用此接口
  * 從未透過[設置速率](/docs/zh-TW/v5/broker/exchange-broker/rate-limit/set)接口設定過速率限制的帳戶將不會出現在響應中，並會使用預設的速率限制



### HTTP 請求

GET`/v5/broker/apilimit/query-all`

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
    
    
    GET /v5/broker/apilimit/query-all HTTP/1.1  
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