---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/account/set-collateral
api_type: Account
updated_at: 2026-05-27 19:14:12.428339
---

# Set Margin Mode

Default is regular margin mode

### HTTP Request

POST`/v5/account/set-margin-mode`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
setMarginMode| **true**|  string| `ISOLATED_MARGIN`, `REGULAR_MARGIN`(i.e. Cross margin), `PORTFOLIO_MARGIN`  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
reasons| array| Object. If requested successfully, it is an empty array  
> reasonCode| string| Fail reason code  
> reasonMsg| string| Fail reason msg  
[](/docs/api-explorer/v5/account/set-margin-mode)

* * *

### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    POST /v5/account/set-margin-mode HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1672134396332  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "setMarginMode": "PORTFOLIO_MARGIN"  
    }  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.set_margin_mode(  
        setMarginMode="PORTFOLIO_MARGIN",  
    ))  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
        testnet: true,  
        key: 'xxxxxxxxxxxxxxxxxx',  
        secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
        .setMarginMode('PORTFOLIO_MARGIN')  
        .then((response) => {  
            console.log(response);  
        })  
        .catch((error) => {  
            console.error(error);  
        });  
    

### Response Example
    
    
    {  
        "retCode": 3400045,  
        "retMsg": "Set margin mode failed",  
        "result": {  
            "reasons": [  
                {  
                    "reasonCode": "3400000",  
                    "reasonMsg": "Equity needs to be equal to or greater than 1000 USDC"  
                }  
            ]  
        }  
    }

---

# 設置保證金模式(帳戶)

用戶如果不設置，默認按全倉保證金

### HTTP 請求

POST`/v5/account/set-margin-mode`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
setMarginMode| **true**|  string| `ISOLATED_MARGIN`(逐倉保證金模式)  
`REGULAR_MARGIN`（全倉保證金模式）  
`PORTFOLIO_MARGIN`（組合保證金模式）  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
reasons| array| Object. 若請求提交成功, 則返回空數組  
> reasonCode| string| 失敗錯誤碼  
> reasonMsg| string| 失敗錯誤消息  
[](/docs/zh-TW/api-explorer/v5/account/set-margin-mode)

* * *

### 請求示例

  * HTTP
  * Python
  * Node.js


    
    
    POST /v5/account/set-margin-mode HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1672134396332  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "setMarginMode": "PORTFOLIO_MARGIN"  
    }  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.set_margin_mode(  
        setMarginMode="PORTFOLIO_MARGIN",  
    ))  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
        testnet: true,  
        key: 'xxxxxxxxxxxxxxxxxx',  
        secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
        .setMarginMode('PORTFOLIO_MARGIN')  
        .then((response) => {  
            console.log(response);  
        })  
        .catch((error) => {  
            console.error(error);  
        });  
    

### 響應示例
    
    
    {  
        "retCode": 3400045,  
        "retMsg": "Set margin mode failed",  
        "result": {  
            "reasons": [  
                {  
                    "reasonCode": "3400000",  
                    "reasonMsg": "Equity needs to be equal to or greater than 1000 USDC"  
                }  
            ]  
        }  
    }