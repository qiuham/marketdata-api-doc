---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/crypto-loan/adjust-collateral
api_type: REST
updated_at: 2026-11-13 19:22:22.753286
---

# Adjust Collateral Amount

You can increase or reduce your collateral amount. When you reduce, please obey the [max. allowed reduction amount](https://bybit-exchange.github.io/docs/v5/crypto-loan/reduce-max-collateral-amt).

> Permission: "Spot trade"

info

  * The adjusted collateral amount will be returned to or deducted from the Funding wallet.



### HTTP Request

POST`/v5/crypto-loan/adjust-ltv`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
orderId| **true**|  string| Loan order ID  
amount| **true**|  string| Adjustment amount  
direction| **true**|  string| `0`: add collateral; `1`: reduce collateral  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
adjustId| string| Collateral adjustment transaction ID  
  
### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    POST /v5/crypto-loan/adjust-ltv HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1728635421137  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
    Content-Length: 85  
      
    {  
        "orderId": "1794267532472646144",  
        "amount": "0.001",  
        "direction": "1"  
    }  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.adjust_collateral_amount(  
        orderId="1794267532472646144",  
        amount="0.001",  
        direction="1",  
    ))  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
      testnet: true,  
      key: 'xxxxxxxxxxxxxxxxxx',  
      secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
      .adjustCollateralAmount({  
        orderId: '1794267532472646144',  
        amount: '0.001',  
        direction: '1',  
      })  
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
            "adjustId": "1794318409405331968"  
        },  
        "retExtInfo": {},  
        "time": 1728635422833  
    }

---

# 調整質押金額

您可以增加或減少質押金額. 選擇減少時, 請先確認允許減少的最大質押數量

> 權限: "現貨交易"

信息

  * 調整的質押數量會在資金帳戶進行返還或者扣減



### HTTP 請求

POST`/v5/crypto-loan/adjust-ltv`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
orderId| **true**|  string| 借貸訂單ID  
amount| **true**|  string| 調整金額  
direction| **true**|  string| `0`: 增加質押金; `1`: 減少質押金  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
adjustId| string| 質押金調整交易ID  
  
### 請求示例

  * HTTP
  * Python
  * Node.js


    
    
    POST /v5/crypto-loan/adjust-ltv HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1728635421137  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
    Content-Length: 85  
      
    {  
        "orderId": "1794267532472646144",  
        "amount": "0.001",  
        "direction": "1"  
    }  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.adjust_collateral_amount(  
        orderId="1794267532472646144",  
        amount="0.001",  
        direction="1",  
    ))  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
      testnet: true,  
      key: 'xxxxxxxxxxxxxxxxxx',  
      secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
      .adjustCollateralAmount({  
        orderId: '1794267532472646144',  
        amount: '0.001',  
        direction: '1',  
      })  
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
            "adjustId": "1794318409405331968"  
        },  
        "retExtInfo": {},  
        "time": 1728635422833  
    }