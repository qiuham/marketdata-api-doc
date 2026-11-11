---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/event/trade/submit-quote
api_type: Trading
updated_at: 2026-11-11 18:28:41.739706
---

# Submit Quote

Submit a payout ratio quote for an Event Contract symbol.

info

  * Only **Event Contract maker accounts** are allowed to access this endpoint.



### HTTP Request

POST`/v5/event/quotes`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
symbol| **true**|  string| Symbol name, e.g. `ETHUSDT-28AUG26-2450-2570-OUT`  
orderLinkId| **true**|  string| User-defined order ID  
grossPayoutRatio| **true**|  string| Gross payout ratio reported by the institution  
amount| **true**|  string| Amount for this quote (settle coin)  
cancelAfterMs| false| integer| Automatically cancel the order after this many milliseconds. `0` uses the instrument's [`quoteMaxValidMs`](/docs/v5/event/market/instrument-info) configuration. A non-zero value must not exceed `quoteMaxValidMs`  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
orderLinkId| string| User-defined order ID  
orderId| string| Order ID  
  
* * *

### Request Example
    
    
    POST /v5/event/quotes HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1694402559000  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "orderLinkId": "xxxx",  
        "symbol": "ETHUSDT-28AUG26-2450-2570-OUT",  
        "grossPayoutRatio": "0.5",  
        "amount": "100",  
        "cancelAfterMs": 5000  
    }  
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "orderLinkId": "xxxxxx",  
            "orderId": "xxxxxxxxxxefffff"  
        },  
        "retExtInfo": {},  
        "time": 1672217377164  
    }

---

# 提交報價

為 Event Contract 交易對提交賠付比率報價。

信息

  * 僅 **Event Contract maker 帳戶** 可訪問此接口。



### HTTP 請求

POST`/v5/event/quotes`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
symbol| **true**|  string| 交易對名稱，如 `ETHUSDT-28AUG26-2450-2570-OUT`  
orderLinkId| **true**|  string| 用戶自定義訂單 ID  
grossPayoutRatio| **true**|  string| 機構報出的毛賠付比率  
amount| **true**|  string| 本次報價金額（結算幣種）  
cancelAfterMs| 否| integer| 下單後經過指定毫秒數自動撤銷訂單。`0` 使用該合約的 [`quoteMaxValidMs`](/docs/zh-TW/v5/event/market/instrument-info) 配置值；非 `0` 的值不得超過 `quoteMaxValidMs`  
  
### 返回參數

參數| 類型| 說明  
---|---|---  
orderLinkId| string| 用戶自定義訂單 ID  
orderId| string| 訂單 ID  
  
* * *

### 請求示例
    
    
    POST /v5/event/quotes HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1694402559000  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "orderLinkId": "xxxx",  
        "symbol": "ETHUSDT-28AUG26-2450-2570-OUT",  
        "grossPayoutRatio": "0.5",  
        "amount": "100",  
        "cancelAfterMs": 5000  
    }  
    

### 返回示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "orderLinkId": "xxxxxx",  
            "orderId": "xxxxxxxxxxefffff"  
        },  
        "retExtInfo": {},  
        "time": 1672217377164  
    }