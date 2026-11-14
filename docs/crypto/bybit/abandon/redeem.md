---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/abandon/redeem
api_type: REST
updated_at: 2026-11-13 19:20:39.609238
---

# Redeem Funds

Withdraw funds from the Bybit asset pool.

tip

There will be two redemption records: one for the redeemed quantity, and the other one is for the total interest occurred.

### HTTP Request

POST`/v5/lending/redeem`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
coin| **true**|  string| Coin name  
quantity| **ture**|  string| Redemption quantity  
serialNo| false| string| Serial no. A customised ID, and it will automatically generated if not passed  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
coin| string| Coin name  
createdTime| string| Created timestamp (ms)  
orderId| string| Order ID  
principalQty| string| Redemption quantity  
serialNo| string| Serial No  
status| string| Order status. `0`: Initial, `1`: Processing, `2`: Success, `10`: Failed  
updatedTime| string| Updated timestamp (ms)  
  
### Request Example
    
    
    POST /v5/lending/redeem HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1682048277724  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "coin": "BTC",  
        "quantity": "0.1",  
        "serialNo": null  
    }  
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "coin": "BTC",  
            "createdTime": "1682048277963",  
            "orderId": "1403517113428086272",  
            "principalQty": "0.1",  
            "serialNo": "14035171132183710722373",  
            "status": "0",  
            "updatedTime": "1682048277963"  
        },  
        "retExtInfo": {},  
        "time": 1682048278001  
    }

---

# 贖回資金

提示

在贖回本金時，系統還會自動贖回當前的收益。

### HTTP 請求

POST`/v5/lending/redeem`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
coin| **true**|  string| 幣種名稱  
quantity| **ture**|  string| 贖回數量  
serialNo| false| string| 序列號，即自定義ID. 若不傳入，則系統自建  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
coin| string| 幣種名稱  
createdTime| string| 創建時間戳 (毫秒)  
orderId| string| 訂單ID  
principalQty| string| 贖回數量  
serialNo| string| 序列號  
status| string| 訂單狀態. `0`: 初始, `1`: 處理中, `2`: 成功, `10`: 失敗  
updatedTime| string| 更新時間戳 (毫秒)  
  
### 請求示例
    
    
    POST /v5/lending/redeem HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1682048277724  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "coin": "BTC",  
        "quantity": "0.1",  
        "serialNo": null  
    }  
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "coin": "BTC",  
            "createdTime": "1682048277963",  
            "orderId": "1403517113428086272",  
            "principalQty": "0.1",  
            "serialNo": "14035171132183710722373",  
            "status": "0",  
            "updatedTime": "1682048277963"  
        },  
        "retExtInfo": {},  
        "time": 1682048278001  
    }