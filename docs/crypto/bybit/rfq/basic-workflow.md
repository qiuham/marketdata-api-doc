---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/rfq/basic-workflow
api_type: REST
updated_at: 2026-09-23 18:46:45.245371
---

# Cancel Quote

Cancel a quote. **Up to 50 requests per second**

info

  * You must pass one of the following params: quoteId, rfqId, and quoteLinkId.
  * If quoteId, rfqId, and quoteLinkId are all passed, they are read in this priority: quoteId > quoteLinkId > rfqId.



### HTTP Request

POST`/v5/rfq/cancel-quote`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
quoteId|  _false_|  string| Quote ID  
rfqId|  _false_|  string| Inquiry ID  
quoteLinkId|  _false_|  string| Custom quote ID  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
result| object|   
rfqId| string| Inquiry ID  
quoteId| string| Quote ID  
quoteLinkId| string| Custom quote ID  
  
### Request Example

  * HTTP
  * Python


    
    
    POST /v5/rfq/cancel-quote HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: XXXXXX  
    X-BAPI-TIMESTAMP: 1744083949347  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
    Content-Length: 115  
      
    {  
        "quoteId":"1754364447601610516653123084412812"    
    }  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.cancel_quote(  
        quoteId="1754364447601610516653123084412812"  
    ))  
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "rfqId": "175740723913299909861293671607573",  
            "quoteId": "1757407443083427576602342578477746",  
            "quoteLinkId": ""  
        },  
        "retExtInfo": {},  
        "time": 1757407457635  
    }

---

# 取消報價單

取消報價單。**每秒最多 50 次請求**

信息

  * 至少需傳遞 quoteId、rfqId 或 quoteLinkId。
  * 若同時傳遞 quoteId、rfqId 和 quoteLinkId，則優先以 quoteId 為準，優先順序判斷為：quoteId > quoteLinkId > rfqId。



### HTTP 請求

POST`/v5/rfq/cancel-quote`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
quoteId| **false**|  string| 報價單 ID  
rfqId| **false**|  string| 詢價單 ID  
quoteLinkId| **false**|  string| 報價單自定義 ID  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
result| object|   
rfqId| string| 詢價單 ID  
quoteId| string| 報價單 ID  
quoteLinkId| string| 報價單自定義 ID  
  
### 請求示例
    
    
    POST /v5/rfq/cancel-quote HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: XXXXXX  
    X-BAPI-TIMESTAMP: 1744083949347  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
    Content-Length: 115  
      
    {  
        "quoteId":"1754364447601610516653123084412812"    
    }  
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "rfqId": "175740723913299909861293671607573",  
            "quoteId": "1757407443083427576602342578477746",  
            "quoteLinkId": ""  
        },  
        "retExtInfo": {},  
        "time": 1757407457635  
    }