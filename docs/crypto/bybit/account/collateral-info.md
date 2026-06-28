---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/account/collateral-info
api_type: Account
updated_at: 2026-05-27 19:13:58.817684
---

# Get Fee Rate

Get the trading fee rate.

### HTTP Request

GET`/v5/account/fee-rate`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
category| **true**|  string| Product type. `spot`, `linear`, `inverse`, `option`  
symbol| false| string| Symbol name, like `BTCUSDT`, uppercase only. Valid for `linear`, `inverse`, `spot`  
baseCoin| false| string| Base coin, uppercase only. `SOL`, `BTC`, `ETH`. Valid for `option`  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
category| string| Product type. `spot`, `option`. _Derivatives does not have this field_  
list| array| Object  
> symbol| string| Symbol name. Keeps `""` for Options  
> baseCoin| string| Base coin. `SOL`, `BTC`, `ETH`

  * Spot and Derivatives does not have this field

  
> takerFeeRate| string| Taker fee rate  
> makerFeeRate| string| Maker fee rate  
[](/docs/api-explorer/v5/account/fee-rate)

* * *

### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/account/fee-rate?symbol=ETHUSDT HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1676360412362  
    X-BAPI-RECV-WINDOW: 5000  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.get_fee_rates(  
        symbol="ETHUSDT",  
    ))  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
        testnet: true,  
        key: 'xxxxxxxxxxxxxxxxxx',  
        secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
        .getFeeRate({  
            category: 'linear',  
            symbol: 'ETHUSDT',  
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
        "retMsg": "OK",  
        "result": {  
            "list": [  
                {  
                    "symbol": "ETHUSDT",  
                    "takerFeeRate": "0.0006",  
                    "makerFeeRate": "0.0001"  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1676360412576  
    }

---

# 查詢手續費率

查詢交易手續費率

### HTTP 請求

GET`/v5/account/fee-rate`參數| 是否必需| 類型| 說明  
---|---|---|---  
category| **true**|  string| 產品類型. `spot`, `linear`, `inverse`, `option`  
symbol| false| string| 合約名稱. 僅`spot`, `linear`, `inverse`有效  
baseCoin| false| string| 交易幣種. `SOL`, `BTC`, `ETH`.僅`option`有效  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
category| string| 產品類型. `spot`, `option`. _期貨不返回該字段_  
list| array| Object  
> symbol| string| 合約名稱. 期權總是為`""`  
> baseCoin| string| 交易幣種. `SOL`, `BTC`, `ETH`

  * 現貨和期貨不返回該字段

  
> takerFeeRate| string| 吃單手續費率  
> makerFeeRate| string| 掛單手續費率  
[](/docs/zh-TW/api-explorer/v5/account/fee-rate)

* * *

### 請求示例

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/account/fee-rate?symbol=ETHUSDT HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1676360412362  
    X-BAPI-RECV-WINDOW: 5000  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.get_fee_rates(  
        symbol="ETHUSDT",  
    ))  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
        testnet: true,  
        key: 'xxxxxxxxxxxxxxxxxx',  
        secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
        .getFeeRate({  
            category: 'linear',  
            symbol: 'ETHUSDT',  
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
        "retMsg": "OK",  
        "result": {  
            "list": [  
                {  
                    "symbol": "ETHUSDT",  
                    "takerFeeRate": "0.0006",  
                    "makerFeeRate": "0.0001"  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1676360412576  
    }