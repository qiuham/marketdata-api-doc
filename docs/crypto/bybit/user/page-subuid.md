---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/user/page-subuid
api_type: REST
updated_at: 2026-07-01 19:33:03.079940
---

# Sign Agreement

To trade commodity contracts, please complete the agreement signing first. Once completed, you will be able to trade all metals commodity contracts.

info

  * Only the master account can sign the agreement via this endpoint. Subaccounts are not supported for this action.
  * Once the master account has signed, all subaccounts will be eligible to trade.
  * The API key must have at least one of the following permissions to call this endpoint: Account Transfer, Subaccount Transfer, or Withdrawal.



### HTTP Request

POST`/v5/user/agreement`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
category| false| integer| `2`: Metals commodity contracts (XAU & XAG). Stock perps share this agreement  
`3`: Crude oil commodity contract  
 _Either`category` or `categoryV2` is required. This field remains supported, but new enum values will no longer be added here — use `categoryV2` instead._  
categoryV2| false| integer| `1`: Metals commodity contracts (XAU & XAG). Stock perps share this agreement  
`2`: Crude oil commodity contract  
 _Either`category` or `categoryV2` is required. Recommend using this field; new enum values will be added here going forward._  
agree| **true**|  boolean| `true`  
  
### Response Parameters

None

### Request Example

  * HTTP
  * Python


    
    
    POST /v5/user/agreement HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: XXXXXX  
    X-BAPI-TIMESTAMP: 1772695036541  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
    Content-Length: 40  
      
    {  
        "agree": true,  
        "categoryV2": 2  
    }  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.sign_agreement(  
        category=2,  
        agree=True  
    ))  
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "success",  
        "result": {},  
        "retExtInfo": {},  
        "time": 1772695037330  
    }

---

# 簽署協議

通過該接口, 您可以完成貴金融合約協議的簽署, 只有在完成簽署後, 才能進行交易貴金屬合約

信息

  * 請使用母帳戶調用接口, 子帳戶不支持。一旦母帳戶簽署後，所有子帳戶都可以交易
  * API key權限需要擁有其中之一"帳戶劃轉, 母子帳戶劃轉, 提幣"



### HTTP 請求

POST`/v5/user/agreement`

### 請求參數

參數| 是否必須| 類型| 說明  
---|---|---|---  
category| false| integer| `2`: 貴金屬(黃金、白銀)合約協議，股票永續合約共用此協議  
`3`: 原油合約協議  
 _`category` 與 `categoryV2` 二選一必傳。該字段仍然可用，但後續新增的枚舉值將不再添加至此字段，請使用 `categoryV2`。_  
categoryV2| false| integer| `1`: 貴金屬(黃金、白銀)合約協議，股票永續合約共用此協議  
`2`: 原油合約協議  
 _`category` 與 `categoryV2` 二選一必傳。建議使用此字段，後續新增的枚舉值將統一添加至此字段。_  
agree| **true**|  boolean| `true`  
  
### 返回參數

無

### 請求示例
    
    
    POST /v5/user/agreement HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: XXXXXX  
    X-BAPI-TIMESTAMP: 1772695036541  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
    Content-Length: 40  
      
    {  
        "agree": true,  
        "categoryV2": 2  
    }  
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "success",  
        "result": {},  
        "retExtInfo": {},  
        "time": 1772695037330  
    }