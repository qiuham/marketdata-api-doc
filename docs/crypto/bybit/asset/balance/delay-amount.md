---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/asset/balance/delay-amount
api_type: REST
updated_at: 2026-07-16 18:50:06.627089
---

# Confirm a Quote

info

  * API key permission: `Convert`
  * API rate limit: `5 req /s`
  * The exchange is async; please check the final status by calling the query [Get Exchange History](/docs/v5/asset/convert-small-balance/exchange-history).
  * Make sure you confirm the quote before it expires.



### HTTP Request

POST`/v5/asset/covert/small-balance-execute`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
quoteId| **true**|  string| The quote ID from [Request a Quote](/docs/v5/asset/convert-small-balance/request-quote#response-parameters)  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
quoteId| string| Quote ID  
exchangeTxId| string| Exchange ID, the same value as `quoteId`  
submitTime| string| Submit ts  
status| string| `init`, `processing`, `success`, `failure`, `partial_fulfillment`  
msg| string| By default is `""`  
  
### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    POST /v5/asset/covert/small-balance-execute HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-API-KEY: XXXXXX  
    X-BAPI-TIMESTAMP: 1766128195297  
    X-BAPI-RECV-WINDOW: 5000  
    X-BAPI-SIGN: XXXXXX  
    Content-Type: application/json  
    Content-Length: 49  
      
    {  
        "quoteId": "1010075157602517596339322880"  
    }  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.confirm_a_quote_small_balance(  
        quoteId="1010075157602517596339322880",  
    ))  
    
    
    
      
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "ok",  
        "result": {  
            "quoteId": "1010075157602517596339322880",  
            "exchangeTxId": "1010075157602517596339322880",  
            "submitTime": "1766128195512",  
            "status": "processing",  
            "msg": ""  
        },  
        "retExtInfo": {},  
        "time": 1766128195512  
    }

---

# 確認報價

信息

  * API密鑰權限: `Convert`
  * API速率限制: `5 req /s`
  * 兌換為異步操作；請通過調用 [獲取兌換記錄](/docs/zh-TW/v5/asset/convert-small-balance/exchange-history) 查詢最終狀態。
  * 請確保在報價過期之前確認報價。



### HTTP 請求

POST`/v5/asset/covert/small-balance-execute`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
quoteId| **true**|  string| 來自 [請求報價](/docs/zh-TW/v5/asset/convert-small-balance/request-quote#response-parameters) 的報價ID  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
quoteId| string| 報價ID  
exchangeTxId| string| 兌換ID，與 `quoteId` 值相同  
submitTime| string| 提交時間戳  
status| string| `init`, `processing`, `success`, `failure`, `partial_fulfillment`  
msg| string| 默認為 `""`  
  
### 請求示例

  * HTTP
  * Python


    
    
    POST /v5/asset/covert/small-balance-execute HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-API-KEY: XXXXXX  
    X-BAPI-TIMESTAMP: 1766128195297  
    X-BAPI-RECV-WINDOW: 5000  
    X-BAPI-SIGN: XXXXXX  
    Content-Type: application/json  
    Content-Length: 49  
      
    {  
        "quoteId": "1010075157602517596339322880"  
    }  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.confirm_a_quote_small_balance(  
        quoteId="1010075157602517596339322880",  
    ))  
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "ok",  
        "result": {  
            "quoteId": "1010075157602517596339322880",  
            "exchangeTxId": "1010075157602517596339322880",  
            "submitTime": "1766128195512",  
            "status": "processing",  
            "msg": ""  
        },  
        "retExtInfo": {},  
        "time": 1766128195512  
    }