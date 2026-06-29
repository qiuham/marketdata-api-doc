---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/rfq/trade/accept-other-quote
api_type: Trading
updated_at: 2026-06-29 19:31:57.829170
---

# Cancel All Quotes

Cancel all active quotes. **Up to 50 requests per second**

### HTTP Request

POST`/v5/rfq/cancel-all-quotes`

### Request Parameters

None

### Response Parameters

Parameter| Type| Comments  
---|---|---  
result| Object|   
> rfqId| string| Inquiry ID  
> quoteId| string| Quote ID  
> quoteLinkId| string| Custom quote ID  
> code| string| Whether or not cancellation was a success, `0`: success  
> msg| string| Cancellation failure reason  
  
### Request Example

  * HTTP
  * Python


    
    
    POST /v5/rfq/cancel-all-quotes HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: XXXXXX  
    X-BAPI-TIMESTAMP: 1744083949347  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
    Content-Length: 115  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.cancel_all_quotes())  
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": [  
            {  
                "rfqId": "175740723913299909861293671607573",  
                "quoteLinkId": "",  
                "quoteId": "1757407497684679708210572531298710",  
                "code": 0,  
                "msg": ""  
            }  
        ],  
        "retExtInfo": {},  
        "time": 1757407503982  
    }

---

# 取消所有報價單

取消所有報價單。**每秒最多 50 次請求**

### HTTP 請求

POST`/v5/rfq/cancel-all-quotes`

### 請求參數

無

### 響應參數

參數| 類型| 說明  
---|---|---  
result| object|   
> data| Array of object|   
>> rfqId| string| 詢價單 ID  
>> quoteId| string| 報價單 ID  
>> quoteLinkId| string| 報價單自定義 ID  
>> code| string| 取消成功或失敗，0 表示取消成功  
>> msg| string| 取消失敗原因  
  
### 請求示例
    
    
    POST /v5/rfq/cancel-all-quotes HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: XXXXXX  
    X-BAPI-TIMESTAMP: 1744083949347  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
    Content-Length: 115  
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": [  
            {  
                "rfqId": "175740723913299909861293671607573",  
                "quoteLinkId": "",  
                "quoteId": "1757407497684679708210572531298710",  
                "code": 0,  
                "msg": ""  
            }  
        ],  
        "retExtInfo": {},  
        "time": 1757407503982  
    }