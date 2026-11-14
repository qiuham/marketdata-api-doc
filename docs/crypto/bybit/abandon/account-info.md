---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/abandon/account-info
api_type: REST
updated_at: 2026-11-13 19:20:36.534498
---

# Get Lending Account Info

### HTTP Request

GET`/v5/lending/account`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
coin| **true**|  string| Coin name  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
coin| string| Coin name  
principalInterest| string| User Redeemable interest  
principalQty| string| Leftover quantity you can redeem for today (measured from 0 - 24 UTC), formula: min(the rest amount of principle, the amount that the user can redeem on the day)  
principalTotal| string| Total amount redeemable by user  
quantity| string| Current deposit quantity  
  
### Request Example
    
    
    GET /v5/lending/account?coin=ETH HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1682049556563  
    X-BAPI-RECV-WINDOW: 5000  
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "coin": "BTC",  
            "principalInterest": "0",  
            "principalQty": "1",  
            "principalTotal": "1",  
            "quantity": "1"  
        },  
        "retExtInfo": {},  
        "time": 1682049706988  
    }

---

# 查詢余幣寶帳戶信息

### HTTP 請求

GET`/v5/lending/account`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
coin| **true**|  string| 幣種名稱  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
coin| string| 幣種名稱  
principalInterest| string| 可贖回收益  
principalQty| string| 可贖回本金金額, 計算公式: min(用戶剩餘本金, 用戶當日可贖回額度)  
principalTotal| string| 可贖回總計  
quantity| string| 當前存入本金  
  
### 請求示例
    
    
    GET /v5/lending/account?coin=ETH HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1682049556563  
    X-BAPI-RECV-WINDOW: 5000  
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "coin": "BTC",  
            "principalInterest": "0",  
            "principalQty": "1",  
            "principalTotal": "1",  
            "quantity": "1"  
        },  
        "retExtInfo": {},  
        "time": 1682049706988  
    }