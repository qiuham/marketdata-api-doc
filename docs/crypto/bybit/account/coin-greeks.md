---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/account/coin-greeks
api_type: Account
updated_at: 2026-05-27 19:13:56.669388
---

# Get Coin Greeks

Get current account Greeks information

info

  * During periods of extreme market volatility, this interface may experience increased latency or temporary delays in data delivery



### HTTP Request

GET`/v5/asset/coin-greeks`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
baseCoin| false| string| Base coin, uppercase only. If not passed, all supported base coin greeks will be returned by default  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
list| array| Object  
> baseCoin| string| Base coin. e.g.,`BTC`,`ETH`,`SOL`  
> totalDelta| string| Delta value  
> totalGamma| string| Gamma value  
> totalVega| string| Vega value  
> totalTheta| string| Theta value  
[](/docs/api-explorer/v5/account/coin-greeks)

* * *

### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/asset/coin-greeks?baseCoin=BTC HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1672287887610  
    X-BAPI-RECV-WINDOW: 5000  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.get_coin_greeks(  
        baseCoin="BTC",  
    ))  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
        testnet: true,  
        key: 'xxxxxxxxxxxxxxxxxx',  
        secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
        .getCoinGreeks('BTC')  
        .then((response) => {  
            console.log(response);  
        })  
        .catch((error) => {  
            console.error(error);  
        });  
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "list": [  
                {  
                    "baseCoin": "BTC",  
                    "totalDelta": "0.00004001",  
                    "totalGamma": "-0.00000009",  
                    "totalVega": "-0.00039689",  
                    "totalTheta": "0.01243824"  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1672287887942  
    }

---

# 查詢Greeks信息

獲取當前賬戶Greeks信息

信息

  * 在極端市場波動期間, 此介面可能會出現延遲增加或資料傳遞暫時延遲的情況



### HTTP 請求

GET`/v5/asset/coin-greeks`

### 請求參數

參數| 是否必需| 類型| 類型  
---|---|---|---  
baseCoin| false| string| baseCoin- 不傳入, 默認返回全部baseCoin的greeks  
  
### 響應參數

參數| 類型| 類型  
---|---|---  
list| array| Object  
> baseCoin| string| baseCoin 例如: BTC、ETH、SOL etc  
> totalDelta| string| Delta值  
> totalGamma| string| Gamma值  
> totalVega| string| Vega值  
> totalTheta| string| Theta值  
[](/docs/zh-TW/api-explorer/v5/account/coin-greeks)

* * *

### 請求示例

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/asset/coin-greeks?baseCoin=BTC HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1672287887610  
    X-BAPI-RECV-WINDOW: 5000  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.get_coin_greeks(  
        baseCoin="BTC",  
    ))  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
        testnet: true,  
        key: 'xxxxxxxxxxxxxxxxxx',  
        secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
        .getCoinGreeks('BTC')  
        .then((response) => {  
            console.log(response);  
        })  
        .catch((error) => {  
            console.error(error);  
        });  
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "list": [  
                {  
                    "baseCoin": "BTC",  
                    "totalDelta": "0.00004001",  
                    "totalGamma": "-0.00000009",  
                    "totalVega": "-0.00039689",  
                    "totalTheta": "0.01243824"  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1672287887942  
    }