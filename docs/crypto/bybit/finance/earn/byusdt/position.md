---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/finance/earn/byusdt/position
api_type: REST
updated_at: 2026-11-13 19:23:09.316904
---

# Get Position Info

### HTTP Request

GET`/v5/earn/token/position`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
coin| **true**|  string| Token coin. Currently only `BYUSDT` is supported  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
totalAmount| string| Total byUSDT holdings  
totalYield| string| Cumulative total yield earned  
yesterdayYield| string| Yesterday's yield  
aprE8| integer| Base APR in e8 precision. Divide by 10^8 to get the actual rate  
bonusAprE8| integer| Bonus APR in e8 precision (returned when user is eligible). Divide by 10^8 to get the actual rate  
bonusMaxAmount| string| Maximum principal eligible for bonus APR  
hasQuota| boolean| Whether there is remaining mintable quota  
  
* * *

### Request Example
    
    
    GET /v5/earn/token/position?coin=BYUSDT HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1741651200000  
    X-BAPI-RECV-WINDOW: 5000  
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "",  
        "result": {  
            "totalAmount": "696",  
            "totalYield": "0",  
            "yesterdayYield": "0",  
            "aprE8": "60000000",  
            "bonusAprE8": "0",  
            "bonusMaxAmount": "",  
            "hasQuota": true  
        },  
        "retExtInfo": {},  
        "time": 1775180113373  
    }

---

# 查詢持倉資訊

### HTTP 請求

GET`/v5/earn/token/position`

### 請求參數

參數| 必填| 類型| 說明  
---|---|---|---  
coin| **true**|  string| 代幣幣種。目前僅支援 `BYUSDT`  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
totalAmount| string| byUSDT 持倉總量  
totalYield| string| 累計已獲得的收益總額  
yesterdayYield| string| 昨日收益  
aprE8| integer| 基礎年化利率（e8 精度）。除以 10^8 可得實際利率  
bonusAprE8| integer| 加成年化利率（e8 精度，符合條件的用戶才返回）。除以 10^8 可得實際利率  
bonusMaxAmount| string| 可享受加成年化利率的最大本金上限  
hasQuota| boolean| 是否有剩餘可鑄造額度  
  
* * *

### 請求示例
    
    
    GET /v5/earn/token/position?coin=BYUSDT HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1741651200000  
    X-BAPI-RECV-WINDOW: 5000  
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "",  
        "result": {  
            "totalAmount": "696",  
            "totalYield": "0",  
            "yesterdayYield": "0",  
            "aprE8": "60000000",  
            "bonusAprE8": "0",  
            "bonusMaxAmount": "",  
            "hasQuota": true  
        },  
        "retExtInfo": {},  
        "time": 1775180113373  
    }