---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/finance/earn/fixed-saving/position
api_type: REST
updated_at: 2026-07-01 19:28:51.958527
---

# Redeem

API ker permission: `Earn`  
API rate limit: 5 reqs / sec

info

  * Early redemption is only supported for category=`FundPool` products where `allowEarlyRedemption` is `true`. Calling this endpoint for other product types returns an error.
  * The position must have been held for at least `redemptionLimitDuration` before early redemption is allowed.
  * Redeemed funds are always returned to the `FUND` account.



### HTTP Request

POST`/v5/earn/fixed-term/redeem`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
productId| **true**|  string| Product ID  
category| **true**|  string| Product sub-type: `FundPool`  
positionId| **true**|  string| Position ID to redeem  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
redeemAmount| string| Estimated redemption amount (principal)  
estEarnings| string| Estimated earnings at early redemption APY  
  
* * *

### Request Example
    
    
    POST /v5/earn/fixed-term/redeem HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1741651200000  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "productId": 1001,  
        "category": "FundPool",  
        "positionId": 200001  
    }  
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "",  
        "result": {  
            "redeemAmount": "0.1",  
            "estEarnings": "0.00002191"  
        },  
        "retExtInfo": {},  
        "time": 1776075665623  
    }

---

# 提前贖回

API key權限：`Earn`  
API 頻率限制：每秒5次

信息

  * 提前贖回僅支持 category=`FundPool` 且 `allowEarlyRedemption` 為 `true` 的產品。對其他產品類型調用此端點將返回錯誤。
  * 持倉必須已持有至少 `redemptionLimitDuration` 的時間後才允許提前贖回。
  * 贖回資金始終返回至 `FUND` 帳戶。



### HTTP 請求

POST`/v5/earn/fixed-term/redeem`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
productId| **true**|  string| 產品ID  
category| **true**|  string| 產品子類型：`FundPool`  
positionId| **true**|  string| 要贖回的持倉ID  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
redeemAmount| string| 預計贖回金額（本金）  
estEarnings| string| 按提前贖回APY計算的預計收益  
  
* * *

### 請求示例
    
    
    POST /v5/earn/fixed-term/redeem HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1741651200000  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "productId": 1001,  
        "category": "FundPool",  
        "positionId": 200001  
    }  
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "",  
        "result": {  
            "redeemAmount": "0.1",  
            "estEarnings": "0.00002191"  
        },  
        "retExtInfo": {},  
        "time": 1776075665623  
    }