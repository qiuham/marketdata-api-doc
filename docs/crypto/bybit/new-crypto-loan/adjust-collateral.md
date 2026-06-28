---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/new-crypto-loan/adjust-collateral
api_type: REST
updated_at: 2026-05-27 19:18:38.569363
---

# Adjust Collateral Amount

You can increase or reduce your collateral amount. When you reduce, please obey the [Get Max. Allowed Collateral Reduction Amount](/docs/v5/new-crypto-loan/reduce-max-collateral-amt)

> Permission: "Spot trade"  
>  UID rate limit: 1 req / second

info

  * The adjusted collateral amount will be returned to or deducted from the Funding wallet.



### HTTP Request

POST`/v5/crypto-loan-common/adjust-ltv`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
currency| **true**|  string| Collateral coin  
amount| **true**|  string| Adjustment amount  
direction| **true**|  string| `0`: add collateral; `1`: reduce collateral  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
adjustId| long| Collateral adjustment transaction ID  
  
### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    POST /v5/crypto-loan-common/adjust-ltv HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: XXXXXX  
    X-BAPI-TIMESTAMP: 1752627997649  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
    Content-Length: 69  
      
    {  
        "currency": "BTC",  
        "amount": "0.08",  
        "direction": "1"  
    }  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.adjust_collateral_amount_new_crypto_loan(  
        currency="BTC",  
        amount="0.08",  
        direction="1",  
    ))  
    
    
    
      
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "ok",  
        "result": {  
            "adjustId": 27511  
        },  
        "retExtInfo": {},  
        "time": 1752627997915  
    }

---

# 調整質押金額

您可以增加或減少質押金額. 選擇減少時, 請先確認[允許減少的最大質押數量](/docs/zh-TW/v5/new-crypto-loan/reduce-max-collateral-amt)

> 權限: "現貨"  
>  頻率: 1次/秒

信息

  * 調整的質押數量會在資金帳戶進行返還或者扣減



### HTTP 請求

POST`/v5/crypto-loan-common/adjust-ltv`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
currency| **true**|  string| 質押幣種  
amount| **true**|  string| 調整金額  
direction| **true**|  string| `0`: 增加質押金; `1`: 減少質押金  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
adjustId| long| 質押金調整交易ID  
  
### 請求示例

  * HTTP
  * Python
  * Node.js


    
    
    POST /v5/crypto-loan-common/adjust-ltv HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: XXXXXX  
    X-BAPI-TIMESTAMP: 1752627997649  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
    Content-Length: 69  
      
    {  
        "currency": "BTC",  
        "amount": "0.08",  
        "direction": "1"  
    }  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.adjust_collateral_amount_new_crypto_loan(  
        currency="BTC",  
        amount="0.08",  
        direction="1",  
    ))  
    
    
    
      
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "ok",  
        "result": {  
            "adjustId": 27511  
        },  
        "retExtInfo": {},  
        "time": 1752627997915  
    }