---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/sbe/sbe-basic-info
api_type: REST
updated_at: 2026-06-29 19:32:31.024655
---

# Get Coin State

### HTTP Request

GET`/v5/spot-margin-trade/coinstate`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
currency| false| string| Coin name, uppercase only  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
list| arrayList| Object  
> currency| string| Coin name, uppercase only  
> spotLeverage| string| Spot margin leverage. Returns "" if spot margin mode is turned off  
  
* * *

### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/spot-margin-trade/coinstate HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1692696840996  
    X-BAPI-RECV-WINDOW: 5000  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.spot_margin_trade_get_coin_state(  
        currency="BTC"  
    ))  
    
    
    
      
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "Success",  
        "result": {  
            "list": [  
                {  
                    "spotLeverage": 3,  
                    "currency": "BTC"  
                },  
                {  
                    "spotLeverage": 4,  
                    "currency": "ETH"  
                },  
                {  
                    "spotLeverage": 4,  
                    "currency": "AVAX"  
                },  
                {  
                    "spotLeverage": 4,  
                    "currency": "EOS"  
                },  
                {  
                    "spotLeverage": 4,  
                    "currency": "XRP"  
                },  
                {  
                    "spotLeverage": 4,  
                    "currency": "USDT"  
                },  
                {  
                    "spotLeverage": 4,  
                    "currency": "GALA"  
                },  
                {  
                    "spotLeverage": 4,  
                    "currency": "DOGE"  
                },  
                {  
                    "spotLeverage": 4,  
                    "currency": "BIT"  
                },  
                {  
                    "spotLeverage": 4,  
                    "currency": "BTC3S"  
                },  
                {  
                    "spotLeverage": 4,  
                    "currency": "BTC3L"  
                },  
                {  
                    "spotLeverage": 4,  
                    "currency": "EUR"  
                },  
                {  
                    "spotLeverage": 4,  
                    "currency": "USDC"  
                },  
                {  
                    "spotLeverage": 4,  
                    "currency": "UNI"  
                },  
                {  
                    "spotLeverage": 4,  
                    "currency": "SOL"  
                },  
                {  
                    "spotLeverage": 4,  
                    "currency": "ADA"  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1756273703314  
    }

---

# 查詢幣種槓桿

### HTTP 請求

GET`/v5/spot-margin-trade/coinstate`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
currency| false| string| 幣名稱，僅限大寫  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
list| arrayList| Object  
> currency| string| 幣名稱，僅限大寫  
> spotLeverage| string| 現貨借貸槓桿。如果現貨借貸模式關閉，則返回“”  
  
* * *

### 請求示例

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/spot-margin-trade/coinstate HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1692696840996  
    X-BAPI-RECV-WINDOW: 5000  
    
    
    
      
    
    
    
      
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "Success",  
        "result": {  
            "list": [  
                {  
                    "spotLeverage": 3,  
                    "currency": "BTC"  
                },  
                {  
                    "spotLeverage": 4,  
                    "currency": "ETH"  
                },  
                {  
                    "spotLeverage": 4,  
                    "currency": "AVAX"  
                },  
                {  
                    "spotLeverage": 4,  
                    "currency": "EOS"  
                },  
                {  
                    "spotLeverage": 4,  
                    "currency": "XRP"  
                },  
                {  
                    "spotLeverage": 4,  
                    "currency": "USDT"  
                },  
                {  
                    "spotLeverage": 4,  
                    "currency": "GALA"  
                },  
                {  
                    "spotLeverage": 4,  
                    "currency": "DOGE"  
                },  
                {  
                    "spotLeverage": 4,  
                    "currency": "BIT"  
                },  
                {  
                    "spotLeverage": 4,  
                    "currency": "BTC3S"  
                },  
                {  
                    "spotLeverage": 4,  
                    "currency": "BTC3L"  
                },  
                {  
                    "spotLeverage": 4,  
                    "currency": "EUR"  
                },  
                {  
                    "spotLeverage": 4,  
                    "currency": "USDC"  
                },  
                {  
                    "spotLeverage": 4,  
                    "currency": "UNI"  
                },  
                {  
                    "spotLeverage": 4,  
                    "currency": "SOL"  
                },  
                {  
                    "spotLeverage": 4,  
                    "currency": "ADA"  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1756273703314  
    }