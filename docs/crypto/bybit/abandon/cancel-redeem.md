---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/abandon/cancel-redeem
api_type: REST
updated_at: 2026-11-13 19:20:36.613390
---

# Cancel Redeem

Cancel the withdrawal operation.

### HTTP Request

POST`/v5/lending/redeem-cancel`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
coin| false| string| Coin name  
orderId| false| string| The order ID of redemption  
serialNo| false| string| Serial no. The customised ID of redemption  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
orderId| string| Order ID  
serialNo| string| Serial No  
updatedTime| string| Updated timestamp (ms)  
  
### Request Example
    
    
    POST /v5/lending/redeem-cancel HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1682048277724  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "coin": "BTC",  
        "orderId": "1403517113428086272",  
        "serialNo": null  
    }  
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "orderId": "1403517113428086272",  
            "serialNo": "linear004",  
            "updatedTime": "1682048277963"  
        },  
        "retExtInfo": {},  
        "time": 1682048278001  
    }

---

# 撤銷贖回

### HTTP 請求

POST`/v5/lending/redeem-cancel`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
coin| false| string| Coin name  
orderId| false| string| The order ID of redemption  
serialNo| false| string| Serial no. The customised ID of redemption  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
orderId| string| Order ID  
serialNo| string| Serial No  
updatedTime| string| Updated timestamp (ms)  
  
### 請求示例
    
    
    POST /v5/lending/redeem-cancel HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1682048277724  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "coin": "BTC",  
        "orderId": "1403517113428086272",  
        "serialNo": null  
    }  
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "orderId": "1403517113428086272",  
            "serialNo": "linear004",  
            "updatedTime": "1682048277963"  
        },  
        "retExtInfo": {},  
        "time": 1682048278001  
    }