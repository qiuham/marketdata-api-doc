---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/finance/advanced-earn/liquidity-mining/yield-records
api_type: REST
updated_at: 2026-05-27 19:17:04.333163
---

# Get Redeem Estimated Amount

info

  * Need authentication. **Up to 10 requests** per second.
  * Requires Earn permission on the API key.
  * This is a **required prerequisite** before placing a Redeem order. The result is cached server-side for 10 minutes and validated when the redeem order is submitted. If the cache expires, call this endpoint again before retrying.



### HTTP Request

GET`/v5/earn/advance/get-redeem-est-amount-list`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
category| **true**|  string| Product type. `SmartLeverage`  
positionIds| **true**|  string| Comma-separated position IDs to query, max 5. e.g. `897,898`  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
list| array| Object  
> success| bool| Whether the estimation was successful for this position  
> positionId| string| Position ID  
> estRedeemAmount| string| Estimated redeem amount in `investCoin`  
> estRedeemTime| string| Estimated time to receive funds, Unix timestamp in ms  
> slippageRate| string| Slippage tolerance rate for this redemption  
  
* * *

### Request Example
    
    
    GET /v5/earn/advance/get-redeem-est-amount-list?category=SmartLeverage&positionIds=1277,1260 HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1672280218882  
    X-BAPI-RECV-WINDOW: 5000  
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "",  
        "result": {  
            "list": [  
                {  
                    "success": true,  
                    "positionId": "1260",  
                    "estRedeemAmount": "975.0977",  
                    "estRedeemTime": "1775038305626",  
                    "slippageRate": "0.97"  
                },  
                {  
                    "success": true,  
                    "positionId": "1277",  
                    "estRedeemAmount": "76.8356",  
                    "estRedeemTime": "1775038305615",  
                    "slippageRate": "0.97"  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1775038005629  
    }

---

# 查詢贖回預估金額

信息

  * 需要身份驗證。每秒**最多 10 次請求** 。
  * API 金鑰需要具備 Earn（理財）權限。
  * 這是提交贖回訂單前的**必要前置步驟** 。結果在服務端快取 10 分鐘，並在提交贖回訂單時進行驗證。若快取已過期，請在重試前重新調用本接口。



### HTTP 請求

GET`/v5/earn/advance/get-redeem-est-amount-list`

### 請求參數

參數| 必填| 類型| 說明  
---|---|---|---  
category| **true**|  string| 產品類型，`SmartLeverage`  
positionIds| **true**|  string| 要查詢的倉位 ID（逗號分隔），最多 5 個，例如：`897,898`  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
list| array| 列表  
> success| bool| 是否成功獲取  
> positionId| string| 倉位 ID  
> estRedeemAmount| string| 以 `investCoin` 計的預估贖回金額  
> estRedeemTime| string| 預計到帳時間，毫秒級 Unix 時間戳  
> slippageRate| string| 此次贖回的滑點容忍率  
  
* * *

### 請求示例
    
    
    GET /v5/earn/advance/get-redeem-est-amount-list?category=SmartLeverage&positionIds=1277,1260 HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1672280218882  
    X-BAPI-RECV-WINDOW: 5000  
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "",  
        "result": {  
            "list": [  
                {  
                    "success": true,  
                    "positionId": "1260",  
                    "estRedeemAmount": "975.0977",  
                    "estRedeemTime": "1775038305626",  
                    "slippageRate": "0.97"  
                },  
                {  
                    "success": true,  
                    "positionId": "1277",  
                    "estRedeemAmount": "76.8356",  
                    "estRedeemTime": "1775038305615",  
                    "slippageRate": "0.97"  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1775038005629  
    }