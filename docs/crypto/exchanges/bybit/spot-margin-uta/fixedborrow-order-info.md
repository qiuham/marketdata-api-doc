---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/spot-margin-uta/fixedborrow-order-info
api_type: REST
updated_at: 2026-05-27 19:22:09.344900
---

# Renew Fixed-Rate Borrow

### HTTP Request

POST`/v5/spot-margin-trade/fixedborrow-renew`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
loanId| **true**|  string| Loan ID  
qty| false| string| Renewal quantity. If not specified, the entire remaining amount will be renewed; if specified, the renewal will be based on the entered quantity  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
result| string| `Success` / `Failure`  
  
* * *

### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    POST /v5/spot-margin-trade/fixedborrow-renew HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1692696840996  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "loanId": "2092341042506646784"  
    }  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.spot_margin_trade_fixed_borrow_renew(  
        loanId="2092341042506646784"  
    ))  
    
    
    
      
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "success",  
        "result": "Success",  
        "retExtInfo": {},  
        "time": 1775617874744  
    }

---

# 固定利率借款續借

### HTTP 請求

POST`/v5/spot-margin-trade/fixedborrow-renew`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
loanId| **true**|  string| 借款合約 ID  
qty| false| string| 續借數量。未輸入則將剩餘全部金額續借；輸入則按輸入的數量續借  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
result| string| `Success`：成功 / `Failure`：失敗  
  
* * *

### 請求示例

  * HTTP
  * Python
  * Node.js


    
    
    POST /v5/spot-margin-trade/fixedborrow-renew HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1692696840996  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "loanId": "2092341042506646784"  
    }  
    
    
    
      
    
    
    
      
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "success",  
        "result": "Success",  
        "retExtInfo": {},  
        "time": 1775617874744  
    }