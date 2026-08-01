---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/otc/margin-coin-convert-info
api_type: REST
updated_at: 2026-08-01 18:52:30.740288
---

# Repay

You can repay the INS loan by calling this API.

info

  * Only the designated Risk Unit UID is allowed to call this API. To obtain the designated Risk Unit UID, please refer to the `parentUid` from [Get LTV](/docs/v5/otc/ltv-convert)
  * The repayment is processed asynchronously and usually takes 2–3 minutes.
  * Pease confirm the repayment status via [Get Repayment Orders](/docs/v5/otc/repay-info) before initiating the next repayment. **Note** that the repayment record will not appear in the response until 2–3 minutes later.



### HTTP Request

POST`/v5/ins-loan/repay-loan`

IMPORTANT

  1. **Please note this API can only be used when urgent. Make sure contact RM before executing**
  2. When repay, principal amount will be deducted from Unified wallet, the interest **not include**



### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
token| **true**|  string| Coin name  
quantity| **true**|  string| The qty to be repaid  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
repayOrderStatus| string| `P`: processing  
  
### Request Example

  * HTTP
  * Python


    
    
    POST /v5/ins-loan/repay-loan HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-API-KEY: XXXXX  
    X-BAPI-TIMESTAMP: 1767605784035  
    X-BAPI-RECV-WINDOW: 5000  
    X-BAPI-SIGN: XXXXX  
    Content-Type: application/json  
    Content-Length: 49  
      
    {  
        "token": "USDT",  
        "quantity": "500000"  
    }  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.repay_loan(  
        token="USDT",  
        quantity="500000"  
    ))  
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "success",  
        "result": {  
            "repayOrderStatus": "P"  
        },  
        "retExtInfo": {},  
        "time": 1767580441965  
    }

---

# 還款

您可以透過调用此接口來償還机构借贷

信息

  * 僅允許風險單元主UID調用此API. 要了解風險單元主UID, 可以參考請參考 [查詢風險率](/docs/zh-TW/v5/otc/ltv-convert) 裏的`parentUid`字段.
  * 還款為異步處理, 通常需要 2–3 分鐘完成.
  * 在發起下一筆還款前，請先透過 [查詢借貸訂單信息](/docs/zh-TW/v5/otc/repay-info) 確認還款狀態。請注意，還款紀錄會在 2–3 分鐘後才會出現在回傳結果中.



### HTTP 請求

POST`/v5/ins-loan/repay-loan`

重要

  1. **請注意該接口僅限緊急時使用。確保您在要使用該接口還款前, 先跟客戶經理溝通**
  2. 還款時，是從統一錢包中扣除本金金額，不包含利息。



### 請求參數

參數| 是否必須| 類型| 說明  
---|---|---|---  
token| **true**|  string| 還款幣種  
quantity| **true**|  string| 還款金額  
  
### 返回參數

參數| 類型| 說明  
---|---|---  
repayOrderStatus| string| `P`: 處理中  
  
### 請求示例
    
    
    POST /v5/ins-loan/repay-loan HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-API-KEY: XXXXX  
    X-BAPI-TIMESTAMP: 1767605784035  
    X-BAPI-RECV-WINDOW: 5000  
    X-BAPI-SIGN: XXXXX  
    Content-Type: application/json  
    Content-Length: 49  
      
    {  
        "token": "USDT",  
        "quantity": "500000"  
    }  
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "success",  
        "result": {  
            "repayOrderStatus": "P"  
        },  
        "retExtInfo": {},  
        "time": 1767580441965  
    }