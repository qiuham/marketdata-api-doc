---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/crypto-loan/collateral-coin
api_type: REST
updated_at: 2026-05-27 19:16:21.494517
---

# Get Collateral Coins

info

Does not need authentication.

### HTTP Request

GET`/v5/crypto-loan/collateral-data`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
vipLevel| false| string| VIP level 

  * `VIP0`, `VIP1`, `VIP2`, `VIP3`, `VIP4`, `VIP5`, `VIP99`(supreme VIP)
  * `PRO1`, `PRO2`, `PRO3`, `PRO4`, `PRO5`, `PRO6`

  
currency| false| string| Coin name, uppercase only  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
vipCoinList| array| Object  
> list| array| Object  
>> collateralAccuracy| integer| Valid collateral coin precision  
>> initialLTV| string| The Initial LTV ratio determines the initial amount of coins that can be borrowed. The initial LTV ratio may vary for different collateral  
>> marginCallLTV| string| If the LTV ratio (Loan Amount/Collateral Amount) reaches the threshold, you will be required to add more collateral to your loan  
>> liquidationLTV| string| If the LTV ratio (Loan Amount/Collateral Amount) reaches the threshold, Bybit will liquidate your collateral assets to repay your loan and interest in full  
>> maxLimit| string| Collateral limit  
> vipLevel| string| VIP level  
  
### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/crypto-loan/collateral-data?currency=ETH&vipLevel=PRO1 HTTP/1.1  
    Host: api.bybit.com  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
    )  
    print(session.get_collateral_coins(  
        currency="ETH",  
        vipLevel="PRO1",  
    ))  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
      testnet: true,  
      key: 'xxxxxxxxxxxxxxxxxx',  
      secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
      .getCollateralCoins({  
        currency: 'ETH',  
        vipLevel: 'PRO1',  
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
            "vipCoinList": [  
                {  
                    "list": [  
                        {  
                            "collateralAccuracy": 8,  
                            "currency": "ETH",  
                            "initialLTV": "0.8",  
                            "liquidationLTV": "0.95",  
                            "marginCallLTV": "0.87",  
                            "maxLimit": "32000"  
                        }  
                    ],  
                    "vipLevel": "PRO1"  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1728618590498  
    }

---

# 查詢質押幣種

信息

不需要鑒權

### HTTP 請求

GET`/v5/crypto-loan/collateral-data`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
vipLevel| false| string| Vip等級 

  * `VIP0`, `VIP1`, `VIP2`, `VIP3`, `VIP4`, `VIP5`, `VIP99`(至尊VIP)
  * `PRO1`, `PRO2`, `PRO3`, `PRO4`, `PRO5`, `PRO6`

  
currency| false| string| 幣種名稱  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
vipCoinList| array| Object  
> list| array| Object  
>> collateralAccuracy| integer| 質押幣種精度  
>> initialLTV| string| 初始質押率, 初始 LTV 決定了最初可借入的資產金額，因質押資產而異  
>> marginCallLTV| string| 追加保證金率, 如果 LTV (待還本息/質押金額) 達到此閾值，系統會提醒您追加質押資產  
>> liquidationLTV| string| 強平質押率, 如果 LTV (待還本息/質押金額) 達到此閾值，系統會對您的質押資產進行強制平倉，以全額償還本金和利息。  
>> maxLimit| string| 抵押限額  
> vipLevel| string| Vip等級  
  
### 請求示例

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/crypto-loan/collateral-data?currency=ETH&vipLevel=PRO1 HTTP/1.1  
    Host: api.bybit.com  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
    )  
    print(session.get_collateral_coins(  
        currency="ETH",  
        vipLevel="PRO1",  
    ))  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
      testnet: true,  
      key: 'xxxxxxxxxxxxxxxxxx',  
      secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
      .getCollateralCoins({  
        currency: 'ETH',  
        vipLevel: 'PRO1',  
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
            "vipCoinList": [  
                {  
                    "list": [  
                        {  
                            "collateralAccuracy": 8,  
                            "currency": "ETH",  
                            "initialLTV": "0.8",  
                            "liquidationLTV": "0.95",  
                            "marginCallLTV": "0.87",  
                            "maxLimit": "32000"  
                        }  
                    ],  
                    "vipLevel": "PRO1"  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1728618590498  
    }