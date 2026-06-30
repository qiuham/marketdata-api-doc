---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/market/rpi-orderbook
api_type: Market Data
updated_at: 2026-06-30 19:28:14.564294
---

# Get Collateral Coins

info

Does not need authentication.

### HTTP Request

GET`/v5/crypto-loan-common/collateral-data`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
currency| false| string| Coin name, uppercase only  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
collateralRatioConfigList| array| Object  
> collateralRatioList| array| Object  
>> collateralRatio| string| Collateral ratio  
>> maxValue| string| Max qty  
>> minValue| string| Min qty  
> currencies| string| Currenies with the same collateral ratio, e.g., `BTC,ETH,XRP`  
currencyLiquidationList| array| Object  
> currency| string| Coin name  
> liquidationOrder| integer| Liquidation order  
  
### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/crypto-loan-common/collateral-data?currency=BTC HTTP/1.1  
    Host: api-testnet.bybit.com  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
    )  
    print(session.get_collateral_coins_new_crypto_loan(  
        currency="BTC",  
        amount="0.08",  
        direction="1",  
    ))  
    
    
    
      
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "ok",  
        "result": {  
            "collateralRatioConfigList": [  
                {  
                    "collateralRatioList": [  
                        {  
                            "collateralRatio": "0.8",  
                            "maxValue": "10000",  
                            "minValue": "0"  
                        },  
                        {  
                            "collateralRatio": "0.7",  
                            "maxValue": "20000",  
                            "minValue": "10000"  
                        },  
                        {  
                            "collateralRatio": "0.5",  
                            "maxValue": "30000",  
                            "minValue": "20000"  
                        },  
                        {  
                            "collateralRatio": "0.4",  
                            "maxValue": "99999999999",  
                            "minValue": "30000"  
                        }  
                    ],  
                    "currencies": "ATOM,AAVE,BTC,BOB"  
                }  
            ],  
            "currencyLiquidationList": [  
                {  
                    "currency": "BTC",  
                    "liquidationOrder": 1  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1752627381571  
    }

---

# 查詢質押幣種

信息

不需要鑒權

### HTTP 請求

GET`/v5/crypto-loan-common/collateral-data`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
currency| false| string| 幣種名稱  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
collateralRatioConfigList| array| Object  
> collateralRatioList| array| Object  
>> collateralRatio| string| 抵押率  
>> maxValue| string| 最大數量  
>> minValue| string| 最小數量  
> currencies| string| 具有相同抵押率的幣種，例如：`BTC,ETH,XRP`  
currencyLiquidationList| array| Object  
> currency| string| 幣種名稱  
> liquidationOrder| integer| 清算順序  
  
### 請求示例

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/crypto-loan-common/collateral-data?currency=BTC HTTP/1.1  
    Host: api-testnet.bybit.com  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
    )  
    print(session.get_collateral_coins_new_crypto_loan(  
        currency="BTC",  
        amount="0.08",  
        direction="1",  
    ))  
    
    
    
      
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "ok",  
        "result": {  
            "collateralRatioConfigList": [  
                {  
                    "collateralRatioList": [  
                        {  
                            "collateralRatio": "0.8",  
                            "maxValue": "10000",  
                            "minValue": "0"  
                        },  
                        {  
                            "collateralRatio": "0.7",  
                            "maxValue": "20000",  
                            "minValue": "10000"  
                        },  
                        {  
                            "collateralRatio": "0.5",  
                            "maxValue": "30000",  
                            "minValue": "20000"  
                        },  
                        {  
                            "collateralRatio": "0.4",  
                            "maxValue": "99999999999",  
                            "minValue": "30000"  
                        }  
                    ],  
                    "currencies": "ATOM,AAVE,BTC,BOB"  
                }  
            ],  
            "currencyLiquidationList": [  
                {  
                    "currency": "BTC",  
                    "liquidationOrder": 1  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1752627381571  
    }