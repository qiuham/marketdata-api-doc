---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/abandon/order-record
api_type: REST
updated_at: 2026-11-13 19:20:39.583460
---

# Get Order Records

Get lending or redeem history

### HTTP Request

GET`/v5/lending/history-order`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
coin| false| string| Coin name  
orderId| false| string| Order ID  
startTime| false| long| The start timestamp (ms)  
endTime| false| long| The end timestamp (ms)  
limit| false| integer| Limit for data size per page. [`1`, `500`]. Default: `50`  
orderType| false| string| Order type. `1`: deposit, `2`: redemption, `3`: Payment of proceeds  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
list| array| Object  
> coin| string| Coin name  
> createdTime| string| Created timestamp (ms)  
> orderId| string| Order ID  
> quantity| string| quantity  
> serialNo| string| Serial No  
> status| string| Order status. `0`: Initial, `1`: Processing, `2`: Success, `10`: Failed, `11`: Cancelled  
> updatedTime| string| Updated timestamp (ms)  
  
### Request Example
    
    
    GET /v5/lending/history-order?orderNo=1403517113428086272 HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1682049395799  
    X-BAPI-RECV-WINDOW: 5000  
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "list": [  
                {  
                    "coin": "BTC",  
                    "createdTime": "1682048277963",  
                    "orderId": "1403517113428086272",  
                    "orderType": "2",  
                    "quantity": "0.1",  
                    "serialNo": "14035171132183710722373",  
                    "status": "2",  
                    "updatedTime": "1682048278245"  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1682049395967  
    }

---

# 查詢訂單歷史

查詢存入/贖回/收益發放的訂單歷史

### HTTP 請求

GET`/v5/lending/history-order`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
coin| false| string| 幣種名稱  
orderId| false| string| 訂單ID  
startTime| false| long| 開始時間戳 (毫秒)  
endTime| false| long| 結束時間戳 (毫秒)  
limit| false| integer| 每頁數量限制. [`1`, `500`]. 默認: `50`  
orderType| false| string| 訂單類型. `1`: 存入, `2`: 贖回, `3`: 收益發放  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
list| array| Object  
> coin| string| 幣種名稱  
> createdTime| string| 創建時間戳 (毫秒)  
> orderId| string| 訂單ID  
> quantity| string| 數量  
> serialNo| string| 序列號  
> status| string| 訂單狀態. `0`: 初始, `1`: 處理中, `2`: 成功, `10`: 失敗, `11`: 已撤銷  
updatedTime| string| 更新時間戳 (毫秒)  
  
### 請求示例
    
    
    GET /v5/lending/history-order?orderNo=1403517113428086272 HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1682049395799  
    X-BAPI-RECV-WINDOW: 5000  
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "list": [  
                {  
                    "coin": "BTC",  
                    "createdTime": "1682048277963",  
                    "orderId": "1403517113428086272",  
                    "orderType": "2",  
                    "quantity": "0.1",  
                    "serialNo": "14035171132183710722373",  
                    "status": "2",  
                    "updatedTime": "1682048278245"  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1682049395967  
    }