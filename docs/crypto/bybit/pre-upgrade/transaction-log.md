---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/pre-upgrade/transaction-log
api_type: REST
updated_at: 2026-08-20 18:45:27.277520
---

# Get Rate Limit Cap

> API rate limit: 50 req per second

info

  * Get your institutions's total rate limit usage and cap, across the board.
  * Main UIDs or sub UIDs can query this endpoint, but a main UID can only see the rate limits of subs below it, and not the subs of other main UIDs.



### HTTP Request

GET`/v5/apilimit/query-cap`

### Request Parameters

None

### Response Parameters

Parameter| Type| Comments  
---|---|---  
list| array| Object  
> [bizType](/docs/v5/enum#biztype)| string| Business type  
> totalRate| integer| Total API rate limit usage accross all subaccounts and master account  
> insCap| integer| Institutional-level API rate limit per second (depends on your pro level)  
> uidCap| integer| UID-level API rate limit per second  
  
### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/apilimit/query-cap HTTP/1.1  
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
    print(session.get_api_rate_limit_cap())  
    
    
    
      
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "success",  
        "result": {  
            "list": [  
                {  
                    "insCap": "30000",  
                    "uidCap": "600",  
                    "totalRate": "29882",  
                    "bizType": "SPOT"  
                },  
                {  
                    "insCap": "30000",  
                    "uidCap": "600",  
                    "totalRate": "29882",  
                    "bizType": "OPTIONS"  
                },  
                {  
                    "insCap": "40000",  
                    "uidCap": "800",  
                    "totalRate": "39932",  
                    "bizType": "DERIVATIVES"  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1758857589872  
    }

---

# 查詢 Ins level的限頻上限和使用量

### 查詢 Ins level的限頻上限和使用量

> API 限頻：每秒 50 次請求  
> 

信息

  * 查詢 Ins 等級的限頻上限和使用量
  * 僅允許透過main UID或來自sub-INS的子帳戶 UID 的API key進行查詢
  * 目前已刪除的子帳戶仍會占用限頻額度，我們正在優化中。



### HTTP 請求

GET`/v5/apilimit/query-cap`

### 請求參數

無

### 響應參數

參數| 類型| 說明  
---|---|---  
list| array| Object  
> [bizType](/docs/zh-TW/v5/enum#biztype)| string| 業務類型  
> totalRate| integer| 所有子帳號與主帳號的 API 限頻總使用量  
> insCap| integer| 基於 Ins 等級的每秒 API 限頻  
> uidCap| integer| 基於 UID 等級的每秒 API 限頻  
  
### 請求範例
    
    
    GET /v5/apilimit/query-cap HTTP/1.1  
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
                    "insCap": "30000",  
                    "uidCap": "600",  
                    "totalRate": "29882",  
                    "bizType": "SPOT"  
                },  
                {  
                    "insCap": "30000",  
                    "uidCap": "600",  
                    "totalRate": "29882",  
                    "bizType": "OPTIONS"  
                },  
                {  
                    "insCap": "40000",  
                    "uidCap": "800",  
                    "totalRate": "39932",  
                    "bizType": "DERIVATIVES"  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1758857589872  
    }