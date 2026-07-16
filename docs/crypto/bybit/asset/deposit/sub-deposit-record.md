---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/asset/deposit/sub-deposit-record
api_type: REST
updated_at: 2026-07-16 18:50:29.002192
---

# Confirm a Quote

info

  1. The exchange is async; please check the final status by calling the convert history API.
  2. Make sure you confirm the quote before it expires.



### HTTP Request

POST`/v5/fiat/trade-execute`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
quoteTxId| **true**|  string| The quote tx ID from [Request a Quote](/docs/v5/asset/fiat-convert/quote-apply#response-parameters)  
subUserId| **true**|  string| The user's sub userId in bybit  
webhookUrl| false| string| API URL to call when order is successful or failed (max 256 characters)  
MerchantRequestId| false| string| Customised request ID(maximum length of 36)

  * Generally it is useless, but it is convenient to track the quote request internally if you fill this field

  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
tradeNo| string| Trade order No  
merchantRequestId| string| Customised request ID  
  
### Request Example

  * HTTP
  * Python


    
    
    POST /v5/fiat/trade-execute HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1720071899789  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
    Content-Length: 52  
      
    {  
        "quoteTxId": "QuoteTaxId123456",  
        "subUserId":"43456"  
    }  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.confirm_a_quote_fiat_convert(  
        quoteTxId="QuoteTaxId123456",  
        subUserId="43456"  
    ))  
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "success",  
        "result": {  
            "tradeNo": "TradeNo123456",  
            "merchantRequestId": ""  
        }  
    }

---

# 確認報價

信息

  1. 兌換是異步的；請通過調用查詢結果 API 確認最終狀態 
  2. 請確保在報價過期之前確認報價



### HTTP 請求

POST`/v5/fiat/trade-execute`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
quoteTxId| **true**|  string| 報價交易 ID，來源於 [申請報價](/docs/zh-TW/v5/asset/fiat-convert/quote-apply#response-parameters)  
subUserId| **true**|  string| 用戶在 Bybit 平台的子用戶 ID  
webhookUrl| false| string| 當訂單成功或失敗時調用的 API URL（最多 256 個字符）  
merchantRequestId| false| string| 自定義請求 ID（最大長度為 36）

  * 通常無需填寫，但如果填寫此字段，便於內部跟踪報價請求

  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
tradeNo| string| 交易訂單號  
merchantRequestId| string| 自定義請求 ID  
  
### 請求示例

  * HTTP


    
    
    POST /v5/fiat/trade-execute HTTP/1.1    
    Host: api-testnet.bybit.com    
    X-BAPI-SIGN: XXXXXX    
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx    
    X-BAPI-TIMESTAMP: 1720071899789    
    X-BAPI-RECV-WINDOW: 5000    
    Content-Type: application/json    
    Content-Length: 52    
      
    {  
        "quoteTxId": "QuoteTaxId123456",  
        "subUserId":"43456"  
    }  
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "success",  
        "result": {  
            "tradeNo": "TradeNo123456",  
            "merchantRequestId": ""  
        }  
    }