---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/rate-limit/rules-for-vips
api_type: REST
updated_at: 2026-08-10 18:48:55.480724
---

# Accept non-LP Quote

Accept non-LP Quote. **Up to 50 requests** per second.

info

  * Accepts non-LP quotes.



### HTTP Request

POST`/v5/rfq/accept-other-quote`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
rfqId| **true**|  string| Inquiry ID  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
result| object|   
> rfqId| string| Inquiry ID  
  
### Request Example

  * HTTP
  * Python


    
    
    POST /v5/rfq/accept-other-quote HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: XXXXXX  
    X-BAPI-TIMESTAMP: 1744083949347  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
    Content-Length: 115  
      
    {  
      "rfqId":"1754364447601610516653123084412812",   
    }  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.accept_other_quote(  
        rfqId="1754364447601610516653123084412812"  
    ))  
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "rfqId": "1754364447601610516653123084412812"  
        },  
        "retExtInfo": {},  
        "time": 1757405933132  
    }

---

# 接受非 LP 報價

接受非 LP 報價 **每秒最多 50 個請求**

信息

  * 用戶确认接受非 LP 報價



### HTTP 請求

POST`/v5/rfq/accept-other-quote`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
rfqId| **true**|  string| 詢價单ID  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
result| object|   
> rfqId| string| 詢價单ID  
  
### 請求示例
    
    
    POST /v5/rfq/accept-other-quote HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: XXXXXX  
    X-BAPI-TIMESTAMP: 1744083949347  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
    Content-Length: 115  
      
    {  
      "rfqId":"1754364447601610516653123084412812",   
    }  
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "rfqId": "1754364447601610516653123084412812"  
        },  
        "retExtInfo": {},  
        "time": 1757405933132  
    }