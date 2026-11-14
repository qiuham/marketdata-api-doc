---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/spot-margin-uta/fixed-available-inventory
api_type: REST
updated_at: 2026-11-13 19:25:07.151821
---

# Get Fixed-Rate Available Inventory

Query available inventory for fixed-rate borrowing by specifying currency, term, and annual rate. The returned value equals min(platform total lendable amount, UTA user remaining borrowing limit, `borrowLimit` of the current leverage tier from [Get Position Tiers](/docs/v5/spot-margin-uta/position-tiers)), rounded down to borrow precision.

info

  * Unified account only
  * All three parameters (`currency`, `term`, `annualRate`) are required



### HTTP Request

GET`/v5/spot-margin-trade/fixed-available-inventory`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
currency| **true**|  string| Coin name, uppercase only. e.g. `USDT`, `BTC`  
term| **true**|  string| Loan term in days. e.g. `7`, `14`, `30`, `90`, `180`  
annualRate| **true**|  string| Annual interest rate. e.g. `0.02` means 2%  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
currency| string| Coin name  
term| string| Loan term in days  
annualRate| string| Annual interest rate  
availableInventory| string| Available inventory for borrowing. Displayed value = min(platform total lendable amount, UTA user remaining borrowing limit, `borrowLimit` of the current leverage tier from [Get Position Tiers](/docs/v5/spot-margin-uta/position-tiers))  
updateTime| string| Last update timestamp in seconds  
  
* * *

### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/spot-margin-trade/fixed-available-inventory?currency=USDT&term=7&annualRate=0.02 HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1699272487000  
    X-BAPI-RECV-WINDOW: 5000  
    X-BAPI-SIGN: XXXXX  
    
    
    
      
    
    
    
      
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "currency": "USDT",  
            "term": "7",  
            "annualRate": "0.02",  
            "availableInventory": "500000",  
            "updateTime": "1699272487"  
        },  
        "retExtInfo": {},  
        "time": 1672221263862  
    }

---

# 查詢定期借貸可借額度

查詢指定幣種、借款期限及年化利率下的定期借貸可借額度。返回值 = min（平台可出借總額，UTA 用戶剩餘借幣上限，[查詢持倉層級](/docs/zh-TW/v5/spot-margin-uta/position-tiers)中當前槓桿檔位的 `borrowLimit`），向下取整至借幣精度。

信息

  * 僅支持統一帳戶
  * `currency`、`term`、`annualRate` 三個參數均為必填



### HTTP 請求

GET`/v5/spot-margin-trade/fixed-available-inventory`

### 請求參數

參數| 是否必須| 類型| 說明  
---|---|---|---  
currency| **true**|  string| 幣種名稱，僅大寫。如 `USDT`、`BTC`  
term| **true**|  string| 借款天數。如 `7`、`14`、`30`、`90`、`180`  
annualRate| **true**|  string| 年化利率。如 `0.02` 表示 2%  
  
### 返回參數

參數| 類型| 說明  
---|---|---  
currency| string| 幣種名稱  
term| string| 借款天數  
annualRate| string| 年化利率  
availableInventory| string| 可借額度。顯示值 = min（平台可出借總額，UTA 用戶剩餘借幣上限，[查詢持倉層級](/docs/zh-TW/v5/spot-margin-uta/position-tiers)中當前槓桿檔位的 `borrowLimit`）  
updateTime| string| 最後更新時間戳（秒）  
  
* * *

### 請求示例

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/spot-margin-trade/fixed-available-inventory?currency=USDT&term=7&annualRate=0.02 HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1699272487000  
    X-BAPI-RECV-WINDOW: 5000  
    X-BAPI-SIGN: XXXXX  
    
    
    
      
    
    
    
      
    

### 返回示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "currency": "USDT",  
            "term": "7",  
            "annualRate": "0.02",  
            "availableInventory": "500000",  
            "updateTime": "1699272487"  
        },  
        "retExtInfo": {},  
        "time": 1672221263862  
    }