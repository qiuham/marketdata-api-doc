---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/finance/advanced-earn/double-win/est-redeem
api_type: REST
updated_at: 2026-11-13 19:22:45.996605
---

# Get Redeem Estimated Amount

info

  * Requires Earn permission on the API key.
  * This is a **required prerequisite** before placing a Redeem order. Pass the returned `estRedeemAmount` in `doubleWinRedeemExtra` when calling [Place Order](/docs/v5/finance/advanced-earn/double-win/create-order).



### HTTP Request

GET`/v5/earn/advance/get-redeem-est-amount-list`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
category| **true**|  string| Product category. `DoubleWin`  
positionIds| **true**|  string| Comma-separated position IDs, max 5. e.g. `5001,5002`  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
list| array| Object  
> success| bool| Whether the estimation succeeded for this position  
> positionId| string| Position ID  
> estRedeemAmount| string| Estimated redeem amount in `investCoin`  
> estRedeemTime| string| Estimated time to receive funds after redemption, Unix timestamp in ms  
> slippageRate| string| Slippage tolerance rate for this redemption, e.g. `"0.05"` = 5%  
  
* * *

### Request Example
    
    
    GET /v5/earn/advance/get-redeem-est-amount-list?category=DoubleWin&positionIds=2847 HTTP/1.1  
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
                    "success": false,  
                    "positionId": "2847",  
                    "estRedeemAmount": "0",  
                    "estRedeemTime": "0",  
                    "slippageRate": "0.9"  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1775107977370  
    }

---

# 查詢贖回預估金額

信息

  * API 金鑰需要具備 Earn（理財）權限。
  * 這是提交贖回訂單前的**必要前置步驟** 。請將返回的 `estRedeemAmount` 透過 `doubleWinRedeemExtra` 傳入[創建訂單](/docs/zh-TW/v5/finance/advanced-earn/double-win/create-order)。



### HTTP 請求

GET`/v5/earn/advance/get-redeem-est-amount-list`

### 請求參數

參數| 必填| 類型| 說明  
---|---|---|---  
category| **true**|  string| 產品類別，`DoubleWin`  
positionIds| **true**|  string| 倉位 ID 列表（逗號分隔），最多 5 個，例如：`2847,2848`  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
list| array| 列表  
> success| bool| 是否成功獲取該倉位的預估金額  
> positionId| string| 倉位 ID  
> estRedeemAmount| string| 以 `investCoin` 計的預估贖回金額  
> estRedeemTime| string| 預計贖回到帳時間，毫秒級 Unix 時間戳  
> slippageRate| string| 此次贖回的滑點容忍率，例如：`"0.9"` = 90%  
  
* * *

### 請求示例
    
    
    GET /v5/earn/advance/get-redeem-est-amount-list?category=DoubleWin&positionIds=2847 HTTP/1.1  
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
                    "success": false,  
                    "positionId": "2847",  
                    "estRedeemAmount": "0",  
                    "estRedeemTime": "0",  
                    "slippageRate": "0.9"  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1775107977370  
    }