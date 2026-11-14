---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/asset/fiat-convert/balance-query
api_type: REST
updated_at: 2026-11-13 19:21:40.728639
---

# Get Balance

### HTTP Request

GET`/v5/fiat/balance-query`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
currency| false| string| `Fiat`: fiat currency code (ISO 4217) etc: KZT. not set will query all fiat balance list  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
result| object| object  
> totalBalance| string| Total balance  
> balance| string| Available balance  
> frozenBalance| string| Frozen balance  
> currency| string| Currency  
  
### Request Example

  * HTTP
  * Python


    
    
    GET /v5/fiat/balance-query HTTP/1.1    
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1720074159814  
    X-BAPI-RECV-WINDOW: 5000  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.get_fiat_balance())  
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "success",  
        "result": [  
            {  
                "currency": "GEL",  
                "totalBalance": "100000",  
                "balance": "100000",  
                "frozenBalance": "0"  
            }  
        ]  
    }

---

# 获取餘額

### HTTP 請求

GET`/v5/fiat/balance-query`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
currency| false| string| `Fiat`：法定貨幣代碼（ISO 4217），例如：KZT。若不填，則會查詢所有法幣餘額列表  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
result| object|   
> totalBalance| string| 總餘額  
> balance| string| 可用餘額  
> frozenBalance| string| 凍結餘額  
> currency| string| 幣種  
  
### 請求示例

  * HTTP


    
    
    GET /v5/fiat/balance-query HTTP/1.1    
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1720074159814  
    X-BAPI-RECV-WINDOW: 5000  
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "success",  
        "result": [  
            {  
                "currency": "GEL",  
                "totalBalance": "100000",  
                "balance": "100000",  
                "frozenBalance": "0"  
            }  
        ]  
    }