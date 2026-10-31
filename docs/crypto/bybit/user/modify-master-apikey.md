---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/user/modify-master-apikey
api_type: REST
updated_at: 2026-10-31 18:38:44.179856
---

# Get Referral Code

Query the referral codes owned by the current user and their corresponding referral registration links.

info

  * Sub-accounts will return the master account's referral codes
  * Only active (non-expired) referral codes are returned



### HTTP Request

GET`/v5/user/invitation/code`

### Request Parameters

No request parameters required. User identity is derived from the API Key.

### Response Parameters

Parameter| Type| Comments  
---|---|---  
referralCodes| array| List of referral codes owned by the user  
> referralCode| string| The referral code string  
> referralLink| string| The referral registration link for the user's site. URL structure: `https://{domain}/{lang}/invite/?ref={referralCode}`  
> scene| integer| Referral code scene type. `1`: Affiliate; `2`: Friend  
  
* * *

### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/user/invitation/code HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1753286400000  
    X-BAPI-RECV-WINDOW: 5000  
    X-BAPI-SIGN: XXXXX  
    
    
    
      
    
    
    
      
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "referralCodes": [  
                {  
                    "referralCode": "AFFIL001",  
                    "referralLink": "https://www.bybit.com/en/invite/?ref=AFFIL001",  
                    "scene": 1  
                },  
                {  
                    "referralCode": "FRIEND01",  
                    "referralLink": "https://www.bybit.com/ru-RU/invite/?ref=FRIEND01",  
                    "scene": 2  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1753286400000  
    }

---

# 查詢邀請碼

查詢當前用戶持有的邀請碼及其對應站點的邀請注冊鏈接。

信息

  * 子帳號將返回母帳號的邀請碼
  * 僅返回有效期內（未過期）的邀請碼



### HTTP 請求

GET`/v5/user/invitation/code`

### 請求參數

無請求參數。用戶身份從 API Key 中獲取。

### 返回參數

參數| 類型| 說明  
---|---|---  
referralCodes| array| 用戶持有的邀請碼列表  
> referralCode| string| 邀請碼字符串  
> referralLink| string| 對應站點的邀請注冊鏈接。URL 結構：`https://{domain}/{lang}/invite/?ref={referralCode}`  
> scene| integer| 邀請碼場景類型。`1`: 代理商（Affiliate）；`2`: 好友（Friend）  
  
* * *

### 請求示例

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/user/invitation/code HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1753286400000  
    X-BAPI-RECV-WINDOW: 5000  
    X-BAPI-SIGN: XXXXX  
    
    
    
      
    
    
    
      
    

### 返回示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "referralCodes": [  
                {  
                    "referralCode": "AFFIL001",  
                    "referralLink": "https://www.bybit.com/en/invite/?ref=AFFIL001",  
                    "scene": 1  
                },  
                {  
                    "referralCode": "FRIEND01",  
                    "referralLink": "https://www.bybit.com/ru-RU/invite/?ref=FRIEND01",  
                    "scene": 2  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1753286400000  
    }