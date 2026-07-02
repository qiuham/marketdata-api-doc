---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/abandon/account-info
api_type: REST
updated_at: 2026-07-02 19:13:37.918466
---

# Get Lending Coin Info

Get the basic information of lending coins

info

All `v5/lending` APIs need **SPOT** permission.

### HTTP Request

GET`/v5/lending/info`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
coin| false| string| Coin name. Return all currencies by default  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
list| array| Object  
> coin| string| Coin name  
> maxRedeemQty| string| The maximum redeemable qty per day (measured from 0 - 24 UTC)  
> minPurchaseQty| string| The minimum qty that can be deposited per request  
> precision| string| Deposit quantity accuracy  
> rate| string| Annualized interest rate. e.g. 0.0002 means 0.02%  
> loanToPoolRatio| string| Capital utilization rate. e.g. 0.0004 means 0.04%  
> actualApy| string| The actual annualized interest rate  
  
### Request Example
    
    
    GET /v5/lending/info?coin=ETH HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1682045949295  
    X-BAPI-RECV-WINDOW: 5000  
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "list": [  
                {  
                    "actualApy": "0.003688421873941958",  
                    "coin": "ETH",  
                    "loanToPoolRatio": "0.16855491872747133044",  
                    "maxRedeemQty": "161",  
                    "minPurchaseQty": "0.03",  
                    "precision": "8",  
                    "rate": "0.003411300771389848"  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1682045942972  
    }

---

# 查詢可存入幣種信息

查詢可存入幣種的基本信息

信息

所有`v5/lending`的接口都需要**現貨** 權限

### HTTP 請求

GET`/v5/lending/info`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
coin| false| string| 幣種名稱  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
list| array| Object  
> coin| string| 幣種名稱  
> maxRedeemQty| string| 單用戶每天最大可贖回數量 (0 - 24 UTC)  
> minPurchaseQty| string| 單筆最小存入數量  
> precision| string| 精度  
> rate| string| 年化利率. 比如: 返回0.0002 表示 0.02%  
> loanToPoolRatio| string| 資金使用率. e.g. 0.0004 means 0.04%  
> actualApy| string| 實際年化利率  
  
### 請求示例
    
    
    GET /v5/lending/info?coin=ETH HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1682045949295  
    X-BAPI-RECV-WINDOW: 5000  
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "list": [  
                {  
                    "actualApy": "0.003688421873941958",  
                    "coin": "ETH",  
                    "loanToPoolRatio": "0.16855491872747133044",  
                    "maxRedeemQty": "161",  
                    "minPurchaseQty": "0.03",  
                    "precision": "8",  
                    "rate": "0.003411300771389848"  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1682045942972  
    }