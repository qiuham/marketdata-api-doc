---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/finance/rwa/position
api_type: REST
updated_at: 2026-11-12 18:29:28.224173
---

# Get Product List

info

  * Authentication is optional. The `userQuota` field is only populated for authenticated requests.
  * **Rate Limit:** 20 req/s (IP)



### HTTP Request

GET`/v5/earn/rwa/product`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
coin| false| string| Settlement coin filter (uppercase), e.g. `USDC`. Returns all if omitted  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
list| array| Product list  
> productId| integer| Product ID  
> coin| string| Settlement coin name (e.g. `USDC`)  
> assetSymbol| string| Underlying asset symbol (e.g. `IGBF`); also serves as the asset name  
> manager| string| Asset manager name  
> baseApr| string| Base APR as decimal string (e.g. `"0.055"` = 5.5%)  
> bonusApr| string| Bonus APR (sum of all active bonus items); empty string when no bonus is active  
> savingType| string| Saving type: `Flexible`, `Fixed`  
> duration| integer| Lock-up duration in days; `0` for Flexible products  
> nav| string| Latest NAV (Net Asset Value per share), truncated to `sharePrecision`  
> minStakeAmount| string| Minimum stake amount (in settlement coin)  
> maxStakeAmount| string| Per-order maximum stake amount; empty string = unlimited  
> userMaxAmount| string| Per-user maximum holding amount; empty string = unlimited  
> userQuota| string| User's remaining stake quota for this product; empty string = unlimited or unauthenticated request  
> minRedeemShare| string| Minimum redeem share quantity  
> redeemFeeRate| string| Redeem fee rate as decimal string (e.g. `"0.001"` = 0.1%)  
> subscriptionFee| string| Subscription fee rate as decimal string (e.g. `"0.001"` = 0.1%)  
> extLink| string| External link to asset details page  
> amountPrecision| integer| Settlement-coin amount precision (decimal places)  
> sharePrecision| integer| Asset share precision (decimal places)  
  
* * *

### Request Example
    
    
    GET /v5/earn/rwa/product?coin=USDC HTTP/1.1  
    Host: api.bybit.com  
    

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
                    "manager": "BlackRock",  
                    "baseApr": "0.055",  
                    "bonusApr": "0.02",  
                    "savingType": "Flexible",  
                    "duration": 0,  
                    "nav": "1.025",  
                    "minStakeAmount": "10",  
                    "maxStakeAmount": "100000",  
                    "userMaxAmount": "50000",  
                    "userQuota": "49500",  
                    "minRedeemShare": "1",  
                    "redeemFeeRate": "0.001",  
                    "subscriptionFee": "0",  
                    "extLink": "https://example.com/igbf",  
                    "amountPrecision": 2,  
                    "sharePrecision": 6  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1710691200000  
    }

---

# 獲取產品列表

信息

  * 無需身份驗證。`userQuota` 欄位僅在已驗證請求時返回。
  * **頻率限制：** 20 次/秒（IP）



### HTTP 請求

GET`/v5/earn/rwa/product`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
coin| false| string| 結算幣種篩選（大寫），例如 `USDC`。不填則返回所有  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
list| array| 產品列表  
> productId| integer| 產品 ID  
> coin| string| 結算幣種（如 `USDC`）  
> assetSymbol| string| 標的資產代號（如 `IGBF`），同時作為資產名稱  
> manager| string| 資產管理方名稱  
> baseApr| string| 基礎年化利率，十進制字符串（如 `"0.055"` = 5.5%）  
> bonusApr| string| 額外獎勵年化利率（所有生效獎勵項之和）；無獎勵時為空字符串  
> savingType| string| 產品類型：`Flexible`（活期）、`Fixed`（定期）  
> duration| integer| 鎖倉天數；活期產品為 `0`  
> nav| string| 最新 NAV（單份淨值），精度截斷至 `sharePrecision`  
> minStakeAmount| string| 最低認購金額（結算幣種）  
> maxStakeAmount| string| 單筆最高認購金額；空字符串 = 無限制  
> userMaxAmount| string| 用戶最大持有金額；空字符串 = 無限制  
> userQuota| string| 用戶剩餘可認購額度；空字符串 = 無限制或未驗證請求  
> minRedeemShare| string| 最低贖回份額  
> redeemFeeRate| string| 贖回費率，十進制字符串（如 `"0.001"` = 0.1%）  
> subscriptionFee| string| 認購費率，十進制字符串（如 `"0.001"` = 0.1%）  
> extLink| string| 資產詳情頁外部鏈接  
> amountPrecision| integer| 結算幣種金額精度（小數位數）  
> sharePrecision| integer| 資產份額精度（小數位數）  
  
* * *

### 請求示例
    
    
    GET /v5/earn/rwa/product?coin=USDC HTTP/1.1  
    Host: api.bybit.com  
    

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
                    "manager": "BlackRock",  
                    "baseApr": "0.055",  
                    "bonusApr": "0.02",  
                    "savingType": "Flexible",  
                    "duration": 0,  
                    "nav": "1.025",  
                    "minStakeAmount": "10",  
                    "maxStakeAmount": "100000",  
                    "userMaxAmount": "50000",  
                    "userQuota": "49500",  
                    "minRedeemShare": "1",  
                    "redeemFeeRate": "0.001",  
                    "subscriptionFee": "0",  
                    "extLink": "https://example.com/igbf",  
                    "amountPrecision": 2,  
                    "sharePrecision": 6  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1710691200000  
    }