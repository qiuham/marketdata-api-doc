---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/rfq/trade/accept-other-quote
api_type: Trading
updated_at: 2026-05-27 19:21:33.262170
---

# Cancel All RFQs

Cancel all active RFQs. **Up to 50 requests per second**

info

  * Inquirer cancels order: Cancel the inquiry, all its corresponding quotes becoming invalid
  * Quoter cancels the order: The inquiry is not affected, but the quote becomes invalid



### HTTP Request

POST`/v5/rfq/cancel-all-rfq`

### Request Parameters

None

### Response Parameters

Parameter| Type| Comments  
---|---|---  
result| array of objects|   
> rfqId| string| Inquiry ID  
> rfqLinkId| string| Custom inquiry ID  
> code| string| Whether or not the cancellations were a success, `0`: success  
> msg| string| Cancellation failure reason  
  
### Request Example

  * HTTP
  * Python


    
    
    POST /v5/rfq/cancel-all-rfq HTTP/1.1  
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
                "rfqId": "175766967076315412093641573648082",  
                "rfqLinkId": "",  
                "code": 0,  
                "msg": ""  
            }  
        ],  
        "retExtInfo": {},  
        "time": 1757669676581  
    }

---

# 取消所有詢價單

取消所有您的詢價單。**每秒最多 50 次請求**

信息

  * 詢價方取消訂單：取消詢價單，所有報價均失效。
  * 報價方取消訂單：詢價單不受影響，報價單失效。



### HTTP 請求

POST`/v5/rfq/cancel-all-rfq`

### 請求參數

無

### 響應參數

參數| 類型| 說明  
---|---|---  
result| array of objects| 詢價單資料  
> rfqId| string| 詢價單 ID  
> rfqLinkId| string| 詢價單自定義 ID  
> code| string| 取消成功或失敗，0 表示取消成功  
> msg| string| 取消失敗原因  
  
### 請求示例
    
    
    POST /v5/rfq/cancel-all-rfq HTTP/1.1  
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
                "rfqId": "175766967076315412093641573648082",  
                "rfqLinkId": "",  
                "code": 0,  
                "msg": ""  
            }  
        ],  
        "retExtInfo": {},  
        "time": 1757669676581  
    }