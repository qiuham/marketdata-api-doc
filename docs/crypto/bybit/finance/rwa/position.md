---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/finance/rwa/position
api_type: REST
updated_at: 2026-06-29 19:29:37.893432
---

# Get Position List

info

  * **Rate Limit:** 10 req/s (UID)



### HTTP Request

GET`/v5/earn/rwa/position`

### Request Parameters

None

### Response Parameters

Parameter| Type| Comments  
---|---|---  
list| array| Position list  
> productId| integer| Product ID  
> coin| string| Settlement coin  
> assetSymbol| string| Underlying asset symbol  
> effectiveShare| string| Effective (redeemable) share quantity  
> processingStakeAmount| string| Stake amount pending settlement (during T+N window)  
> processingRedeemShare| string| Share quantity pending redemption settlement  
> bonusEarned| string| Cumulative bonus earned (in settlement coin)  
> nav| string| Current NAV (Net Asset Value per share)  
> holdAmount| string| Hold value (`effectiveShare × nav`, in settlement coin)  
> duration| integer| Lock-up duration in days; `0` for Flexible products  
  
* * *

### Request Example
    
    
    GET /v5/earn/rwa/position HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1710691200000  
    X-BAPI-RECV-WINDOW: 5000  
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "success",  
        "result": {  
            "list": [  
                {  
                    "productId": 1001,  
                    "coin": "USDC",  
                    "assetSymbol": "IGBF",  
                    "effectiveShare": "100",  
                    "processingStakeAmount": "50",  
                    "processingRedeemShare": "10",  
                    "bonusEarned": "1.25",  
                    "nav": "1.025",  
                    "holdAmount": "102.50",  
                    "duration": 0  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1710691200000  
    }

---

# 獲取持倉列表

信息

  * **頻率限制：** 10 次/秒（UID）



### HTTP 請求

GET`/v5/earn/rwa/position`

### 請求參數

無

### 響應參數

參數| 類型| 說明  
---|---|---  
list| array| 持倉列表  
> productId| integer| 產品 ID  
> coin| string| 結算幣種  
> assetSymbol| string| 標的資產代號  
> effectiveShare| string| 有效（可贖回）份額數量  
> processingStakeAmount| string| 待結算認購金額（T+N 窗口期內）  
> processingRedeemShare| string| 待結算贖回份額數量  
> bonusEarned| string| 累計獲得的獎勵金額（結算幣種）  
> nav| string| 當前 NAV（單份淨值）  
> holdAmount| string| 持有市值（`effectiveShare × nav`，結算幣種）  
> duration| integer| 鎖倉天數；活期產品為 `0`  
  
* * *

### 請求示例
    
    
    GET /v5/earn/rwa/position HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1710691200000  
    X-BAPI-RECV-WINDOW: 5000  
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "success",  
        "result": {  
            "list": [  
                {  
                    "productId": 1001,  
                    "coin": "USDC",  
                    "assetSymbol": "IGBF",  
                    "effectiveShare": "100",  
                    "processingStakeAmount": "50",  
                    "processingRedeemShare": "10",  
                    "bonusEarned": "1.25",  
                    "nav": "1.025",  
                    "holdAmount": "102.50",  
                    "duration": 0  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1710691200000  
    }