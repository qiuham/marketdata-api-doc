---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/rfq/trade/cancel-all-rfq
api_type: Trading
updated_at: 2026-07-13 19:03:52.730828
---

# Cancel RFQ

Cancel RFQ. **Up to 50 requests per second**

info

  * You must pass either rfqId or rfqLinkId.
  * If both rfqId and rfqLinkId are passed, only rfqId is considered.



### HTTP Request

POST`/v5/rfq/cancel-rfq`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
rfqId|  _false_|  string| Inquiry ID  
rfqLinkId|  _false_|  string| Custom inquiry ID  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
rfqId| string| Inquiry ID  
rfqLinkId| string| Custom inquiry ID  
  
### Request Example

  * HTTP
  * Python


    
    
    POST /v5/rfq/cancel-rfq HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: XXXXXX  
    X-BAPI-TIMESTAMP: 1744083949347  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
    Content-Length: 115  
      
    {  
        "rfqId": "1756871488168105512459181956436945"  
    }  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.cancel_rfq(  
        rfqId="1756871488168105512459181956436945"  
    ))  
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "rfqId": "1756871488168105512459181956436945",  
            "rfqLinkId": ""  
        },  
        "retExtInfo": {},  
        "time": 1756871494507  
    }

---

# 取消詢價單

取消詢價單。**每秒最多 50 次請求**

信息

  * 至少需傳遞 rfqId 或 rfqLinkId。
  * 若同時傳遞 rfqId 和 rfqLinkId，則以 rfqId 為準。



### HTTP 請求

POST`/v5/rfq/cancel-rfq`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
rfqId| **false**|  string| 詢價單 ID  
rfqLinkId| **false**|  string| 詢價單自定義 ID  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
rfqId| string| 詢價單 ID  
rfqLinkId| string| 詢價單自定義 ID  
  
### 請求示例
    
    
    POST /v5/rfq/cancel-rfq HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: XXXXXX  
    X-BAPI-TIMESTAMP: 1744083949347  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
    Content-Length: 115  
      
    {  
        "rfqId": "1756871488168105512459181956436945"  
    }  
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "rfqId": "1756871488168105512459181956436945",  
            "rfqLinkId": ""  
        },  
        "retExtInfo": {},  
        "time": 1756871494507  
    }