---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/finance/earn/byusdt/hourly-yield
api_type: REST
updated_at: 2026-06-29 19:28:34.647580
---

# Get Product Info

### HTTP Request

GET`/v5/earn/token/product`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
coin| **true**|  string| Token coin. Currently only `BYUSDT` is supported  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
productId| string| Product ID  
coin| string| Token coin  
mintFeeRateE8| string| Mint fee rate in e8 precision (e.g. `5000000` = 0.05%)  
redeemFeeRateE8| string| Redeem fee rate in e8 precision  
minInvestment| string| Minimum investment amount (in USDT)  
userHolding| string| User's current byUSDT holdings. Return `""` without authentication  
leftQuota| string| Remaining mintable quota. Return `""` without authentication  
canMint| boolean| Whether minting is currently available. Return `false` without authentication  
savingsBalance| string| User's USDT balance in Flexible Saving account (available for Mint). Return `""` without authentication  
aprE8| string| Base APR in e8 precision. Divide by 10^8 to get the actual rate  
bonusAprE8| string| Bonus APR in e8 precision (returned when user is eligible). Divide by 10^8 to get the actual rate  
bonusMaxAmount| string| Maximum principal eligible for bonus APR. Principal exceeding this amount earns only the base APR  
baseCoinPrecision| integer| Decimal precision for USDT amounts  
tokenPrecision| integer| Decimal precision for byUSDT amounts  
  
* * *

### Request Example
    
    
    GET /v5/earn/token/product?coin=BYUSDT HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXXXX  
    X-BAPI-API-KEY: XXXXXXX  
    X-BAPI-TIMESTAMP: 1775179312802  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "",  
        "result": {  
            "productId": "1",  
            "coin": "BYUSDT",  
            "mintFeeRateE8": "0",  
            "redeemFeeRateE8": "100000",  
            "minInvestment": "1",  
            "userHolding": "588",  
            "leftQuota": "999412",  
            "canMint": true,  
            "savingsBalance": "1412",  
            "aprE8": "60000000",  
            "bonusAprE8": "0",  
            "bonusMaxAmount": "",  
            "baseCoinPrecision": 4,  
            "tokenPrecision": 4  
        },  
        "retExtInfo": {},  
        "time": 1775179313444  
    }

---

# 查詢產品資訊

### HTTP 請求

GET`/v5/earn/token/product`

### 請求參數

參數| 必填| 類型| 說明  
---|---|---|---  
coin| **true**|  string| 代幣幣種。目前僅支援 `BYUSDT`  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
productId| string| 產品 ID  
coin| string| 代幣幣種  
mintFeeRateE8| string| 鑄造手續費率（e8 精度，例如 `5000000` = 0.05%）  
redeemFeeRateE8| string| 贖回手續費率（e8 精度）  
minInvestment| string| 最低投資金額（以 USDT 計）  
userHolding| string| 用戶當前 byUSDT 持倉量。未身份驗證時返回 `""`  
leftQuota| string| 剩餘可鑄造額度。未身份驗證時返回 `""`  
canMint| boolean| 當前是否可進行鑄造。未身份驗證時返回 `false`  
savingsBalance| string| 用戶活期理財帳戶的 USDT 餘額（可用於鑄造）。未身份驗證時返回 `""`  
aprE8| string| 基礎年化利率（e8 精度）。除以 10^8 可得實際利率  
bonusAprE8| string| 加成年化利率（e8 精度，符合條件的用戶才返回）。除以 10^8 可得實際利率  
bonusMaxAmount| string| 可享受加成年化利率的最大本金上限。超出部分僅享受基礎年化利率  
baseCoinPrecision| integer| USDT 金額的小數精度  
tokenPrecision| integer| byUSDT 金額的小數精度  
  
* * *

### 請求示例
    
    
    GET /v5/earn/token/product?coin=BYUSDT HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXXXX  
    X-BAPI-API-KEY: XXXXXXX  
    X-BAPI-TIMESTAMP: 1775179312802  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "",  
        "result": {  
            "productId": "1",  
            "coin": "BYUSDT",  
            "mintFeeRateE8": "0",  
            "redeemFeeRateE8": "100000",  
            "minInvestment": "1",  
            "userHolding": "588",  
            "leftQuota": "999412",  
            "canMint": true,  
            "savingsBalance": "1412",  
            "aprE8": "60000000",  
            "bonusAprE8": "0",  
            "bonusMaxAmount": "",  
            "baseCoinPrecision": 4,  
            "tokenPrecision": 4  
        },  
        "retExtInfo": {},  
        "time": 1775179313444  
    }