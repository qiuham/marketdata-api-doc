---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/spot-margin-uta/flexible-available-inventory
api_type: REST
updated_at: 2026-07-12 18:52:24.753142
---

# Get Flexible Available Inventory

Retrieve the flexible available inventory for a specified cryptocurrency in spot margin trading. The returned value equals min(platform total lendable amount, UTA user remaining borrowing limit).

info

  * Unified account only



### HTTP Request

GET`/v5/spot-margin-trade/flexible-available-inventory`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
currency| **true**|  string| Coin name, uppercase only. e.g. `BTC`  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
currency| string| Coin name  
availableInventory| string| Available inventory for the specified coin. Displayed value = min(platform total lendable amount, UTA user remaining borrowing limit)  
updateTime| string| Last update timestamp in milliseconds  
  
* * *

### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/spot-margin-trade/flexible-available-inventory?currency=BTC HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1756261353733  
    X-BAPI-RECV-WINDOW: 5000  
    X-BAPI-SIGN: XXXXX  
    
    
    
      
    
    
    
      
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "Success",  
        "result": {  
            "currency": "BTC",  
            "availableInventory": "17.54689892",  
            "updateTime": "1756261353733"  
        },  
        "retExtInfo": {},  
        "time": 1756261353733  
    }

---

# 查詢靈活借貸可借額度

查詢現貨槓桿交易中指定幣種的靈活借貸可借額度。返回值 = min（平台可出借總額，UTA 用戶剩餘借幣上限）。

信息

  * 僅支持統一帳戶



### HTTP 請求

GET`/v5/spot-margin-trade/flexible-available-inventory`

### 請求參數

參數| 是否必須| 類型| 說明  
---|---|---|---  
currency| **true**|  string| 幣種名稱，僅大寫。如 `BTC`  
  
### 返回參數

參數| 類型| 說明  
---|---|---  
currency| string| 幣種名稱  
availableInventory| string| 指定幣種的可借額度。顯示值 = min（平台可出借總額，UTA 用戶剩餘借幣上限）  
updateTime| string| 最後更新時間戳（毫秒）  
  
* * *

### 請求示例

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/spot-margin-trade/flexible-available-inventory?currency=BTC HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1756261353733  
    X-BAPI-RECV-WINDOW: 5000  
    X-BAPI-SIGN: XXXXX  
    
    
    
      
    
    
    
      
    

### 返回示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "Success",  
        "result": {  
            "currency": "BTC",  
            "availableInventory": "17.54689892",  
            "updateTime": "1756261353733"  
        },  
        "retExtInfo": {},  
        "time": 1756261353733  
    }