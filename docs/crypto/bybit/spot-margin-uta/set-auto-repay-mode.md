---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/spot-margin-uta/set-auto-repay-mode
api_type: REST
updated_at: 2026-10-23 18:50:56.474137
---

# Get Tiered Collateral Ratio

UTA loan tiered collateral ratio

info

Does not need authentication.

### HTTP Request

GET`/v5/spot-margin-trade/collateral`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
currency| false| string| Coin name, uppercase only  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
list| array| Object  
> currency| string| Coin name  
> collateralRatioList| array| Object  
>> maxQty| string| Upper limit(in coin) of the tiered range, `""` means positive infinity  
>> minQty| string| lower limit(in coin) of the tiered range  
>> collateralRatio| string| Collateral ratio  
  
### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/spot-margin-trade/collateral?currency=BTC HTTP/1.1  
    Host: api-testnet.bybit.com  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
    )  
    print(session.get_tiered_collateral_ratio(  
        currency="BTC",  
    ))  
    
    
    
      
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "list": [  
                {  
                    "currency": "BTC",  
                    "collateralRatioList": [  
                        {  
                            "minQty": "0",  
                            "maxQty": "1000000",  
                            "collateralRatio": "0.85"  
                        },  
                        {  
                            "minQty": "1000000",  
                            "maxQty": "",  
                            "collateralRatio": "0"  
                        }  
                    ]  
                }  
            ]  
        },  
        "retExtInfo": "{}",  
        "time": 1739848984945  
    }

---

# 查詢階梯價值率

查詢統一帳戶借貸的階梯價值率

信息

不需要鑒權

### HTTP 請求

GET`/v5/spot-margin-trade/collateral`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
currency| false| string| 幣種名稱  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
list| array| Object  
> currency| string| 幣種名稱  
> collateralRatioList| array| Object  
>> maxQty| string| 梯度區間上限, 單位是幣種, 如"BTC", `""`表示正無窮  
>> minQty| string| 梯度區間下限, 單位是幣種, 如"BTC", 最小值是0  
>> collateralRatio| string| 抵押率  
  
### 請求示例

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/spot-margin-trade/collateral?currency=BTC HTTP/1.1  
    Host: api-testnet.bybit.com  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
    )  
    print(session.get_tiered_collateral_ratio(  
        currency="BTC",  
    ))  
    
    
    
      
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "list": [  
                {  
                    "currency": "BTC",  
                    "collateralRatioList": [  
                        {  
                            "minQty": "0",  
                            "maxQty": "1000000",  
                            "collateralRatio": "0.85"  
                        },  
                        {  
                            "minQty": "1000000",  
                            "maxQty": "",  
                            "collateralRatio": "0"  
                        }  
                    ]  
                }  
            ]  
        },  
        "retExtInfo": "{}",  
        "time": 1739848984945  
    }