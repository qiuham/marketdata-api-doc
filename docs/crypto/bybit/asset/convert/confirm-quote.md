---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/asset/convert/confirm-quote
api_type: REST
updated_at: 2026-07-21 18:55:12.228396
---

# Confirm a Quote

info

  1. The exchange is async; please check the final status by calling the query result API.
  2. Make sure you confirm the quote before it expires.



### HTTP Request

POST`/v5/asset/exchange/convert-execute`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
quoteTxId| **true**|  string| The quote tx ID from [Request a Quote](/docs/v5/asset/convert/apply-quote#response-parameters)  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
quoteTxId| string| Quote transaction ID  
exchangeStatus| string| Exchange status 

  * init
  * processing
  * success
  * failure

  
  
### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    POST /v5/asset/exchange/convert-execute HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1720071899789  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
    Content-Length: 52  
      
    {  
        "quoteTxId": "10100108106409343501030232064"  
    }  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.confirm_a_quote(  
        quoteTxId="10100108106409343501030232064",  
    ))  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
      testnet: true,  
      key: 'xxxxxxxxxxxxxxxxxx',  
      secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
      .confirmConvertQuote({  
        quoteTxId: '10100108106409343501030232064',  
      })  
      .then((response) => {  
        console.log(response);  
      })  
      .catch((error) => {  
        console.error(error);  
      });  
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "ok",  
        "result": {  
            "exchangeStatus": "processing",  
            "quoteTxId": "10100108106409343501030232064"  
        },  
        "retExtInfo": {},  
        "time": 1720071900529  
    }

---

# 確認報價

信息

  1. 該接口是異步的, 請通過查詢請求確認最終兌換結果
  2. 確保您在報價單過期前確認該報價, 否則失效



### HTTP 請求

POST`/v5/asset/exchange/convert-execute`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
quoteTxId| **true**|  string| 報價單ID, 來自於[提交報價的響應](/docs/zh-TW/v5/asset/convert/apply-quote#response-parameters)  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
quoteTxId| string| 報價單ID  
exchangeStatus| string| 兌換狀態 

  * init
  * processing
  * success
  * failure

  
  
### 請求示例

  * HTTP
  * Python
  * Node.js


    
    
    POST /v5/asset/exchange/convert-execute HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1720071899789  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
    Content-Length: 52  
      
    {  
        "quoteTxId": "10100108106409343501030232064"  
    }  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.confirm_a_quote(  
        quoteTxId="10100108106409343501030232064",  
    ))  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
      testnet: true,  
      key: 'xxxxxxxxxxxxxxxxxx',  
      secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
      .confirmConvertQuote({  
        quoteTxId: '10100108106409343501030232064',  
      })  
      .then((response) => {  
        console.log(response);  
      })  
      .catch((error) => {  
        console.error(error);  
      });  
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "ok",  
        "result": {  
            "exchangeStatus": "processing",  
            "quoteTxId": "10100108106409343501030232064"  
        },  
        "retExtInfo": {},  
        "time": 1720071900529  
    }