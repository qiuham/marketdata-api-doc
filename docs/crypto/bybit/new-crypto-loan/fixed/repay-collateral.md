---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/new-crypto-loan/fixed/repay-collateral
api_type: REST
updated_at: 2026-07-17 18:51:22.425122
---

# Create Supply Order

> Permission: "Spot trade"  
>  UID rate limit: 1 req / second

### HTTP Request

POST`/v5/crypto-loan-fixed/supply`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
orderCurrency| **true**|  string| Currency to supply  
orderAmount| **true**|  string| Amount to supply  
annualRate| **true**|  string| Customizable annual interest rate, e.g., `0.02` means 2%  
term| **true**|  string| Fixed term `7`: 7 days; `14`: 14 days; `30`: 30 days; `90`: 90 days; `180`: 180 days  
availableSource| false| string| Source account for supply. `0`: Funding Account; `1`: Earn Flexible Account; `2`: ALL. Default: `0`  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
orderId| string| Supply order ID  
  
### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    POST /v5/crypto-loan-fixed/supply HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: XXXXXX  
    X-BAPI-TIMESTAMP: 1752652261840  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
    Content-Length: 104  
      
    {  
        "orderCurrency": "USDT",  
        "orderAmount": "2002.21",  
        "annualRate": "0.35",  
        "term": "7"  
    }  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.create_lending_order_fixed_crypto_loan(  
        orderCurrency="USDT",  
        orderAmount="2002.21",  
        annualRate="0.35",  
        term="7",  
    ))  
    
    
    
      
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "ok",  
        "result": {  
            "orderId": "13007"  
        },  
        "retExtInfo": {},  
        "time": 1752633650147  
    }

---

# 創建存款單

> 權限: "現貨"  
>  頻率: 1次/秒

### HTTP 請求

POST`/v5/crypto-loan-fixed/supply`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
orderCurrency| **true**|  string| 出借幣種  
orderAmount| **true**|  string| 出借金額  
annualRate| **true**|  string| 可自訂年利率，例如 `0.02` 表示 2%  
term| **true**|  string| 固定期限 `7`: 7 天；`14`: 14 天；`30`: 30 天；`90`: 90 天；`180`: 180 天  
availableSource| false| string| 出借資金來源帳戶。`0`: 資金帳戶；`1`: 靈活賺幣帳戶；`2`: 全部。預設值：`0`  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
orderId| string| 存款單ID  
  
### 請求示例

  * HTTP
  * Python
  * Node.js


    
    
    POST /v5/crypto-loan-fixed/supply HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: XXXXXX  
    X-BAPI-TIMESTAMP: 1752652261840  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
    Content-Length: 104  
      
    {  
        "orderCurrency": "USDT",  
        "orderAmount": "2002.21",  
        "annualRate": "0.35",  
        "term": "7"  
    }  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.create_lending_order_fixed_crypto_loan(  
        orderCurrency="USDT",  
        orderAmount="2002.21",  
        annualRate="0.35",  
        term="7",  
    ))  
    
    
    
      
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "ok",  
        "result": {  
            "orderId": "13007"  
        },  
        "retExtInfo": {},  
        "time": 1752633650147  
    }