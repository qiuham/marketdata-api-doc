---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/crypto-loan/reduce-max-collateral-amt
api_type: REST
updated_at: 2026-11-13 19:22:26.227197
---

# Get Max. Allowed Collateral Reduction Amount

Query for the maximum amount by which collateral may be reduced by.

> Permission: "Spot trade"

### HTTP Request

GET`/v5/crypto-loan/max-collateral-amount`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
orderId| **true**|  string| Loan coin ID  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
maxCollateralAmount| string| Max. reduction collateral amount  
  
### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/crypto-loan/max-collateral-amount?orderId=1794267532472646144 HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1728634289933  
    X-BAPI-RECV-WINDOW: 5000  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.get_max_allowed_collateral_reduction_amount(  
            orderId="1794267532472646144",  
    ))  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
      testnet: true,  
      key: 'xxxxxxxxxxxxxxxxxx',  
      secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
      .getMaxAllowedReductionCollateralAmount({ orderId: '1794267532472646144' })  
      .then((response) => {  
        console.log(response);  
      })  
      .catch((error) => {  
        console.error(error);  
      });  
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "request.success",  
        "result": {  
            "maxCollateralAmount": "0.00210611"  
        },  
        "retExtInfo": {},  
        "time": 1728634291554  
    }

---

# 查詢最大可減少的質押金額

查詢某個借貸訂單允許的最大可減少質押金額

> 權限: "現貨交易"

### HTTP 請求

GET`/v5/crypto-loan/max-collateral-amount`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
orderId| **true**|  string| 借貸訂單ID  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
maxCollateralAmount| string| 最大可減少金額  
  
### 請求示例

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/crypto-loan/max-collateral-amount?orderId=1794267532472646144 HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1728634289933  
    X-BAPI-RECV-WINDOW: 5000  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.get_max_allowed_collateral_reduction_amount(  
            orderId="1794267532472646144",  
    ))  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
      testnet: true,  
      key: 'xxxxxxxxxxxxxxxxxx',  
      secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
      .getMaxAllowedReductionCollateralAmount({ orderId: '1794267532472646144' })  
      .then((response) => {  
        console.log(response);  
      })  
      .catch((error) => {  
        console.error(error);  
      });  
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "request.success",  
        "result": {  
            "maxCollateralAmount": "0.00210611"  
        },  
        "retExtInfo": {},  
        "time": 1728634291554  
    }