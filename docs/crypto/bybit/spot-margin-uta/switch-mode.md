---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/spot-margin-uta/switch-mode
api_type: REST
updated_at: 2026-07-09 19:12:26.743064
---

# Get VIP Margin Data

This margin data is for **Unified account** in particular.

info

Does not need authentication.

### HTTP Request

GET`/v5/spot-margin-trade/data`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
[vipLevel](/docs/v5/enum#viplevel)| false| string| VIP level  
currency| false| string| Coin name, uppercase only  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
vipCoinList| array| Object  
> list| array| Object  
>> borrowable| boolean| Whether it is allowed to be borrowed  
>> collateralRatio| string| Due to the new Tiered Collateral value logic, this field will no longer be accurate starting on February 19, 2025. Please refer to [Get Tiered Collateral Ratio](/docs/v5/spot-margin-uta/tier-collateral-ratio)  
>> currency| string| Coin name  
>> hourlyBorrowRate| string| Borrow interest rate per hour  
>> liquidationOrder| string| Liquidation order  
>> marginCollateral| boolean| Whether it can be used as a margin collateral currency  
>> maxBorrowingAmount| string| Max borrow amount  
> vipLevel| string| VIP level  
[](/docs/api-explorer/v5/spot-margin-uta/vip-margin)

* * *

### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/spot-margin-trade/data?vipLevel=No VIP&currency=BTC HTTP/1.1  
    Host: api-testnet.bybit.com  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.spot_margin_trade_get_vip_margin_data())  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
      testnet: true,  
      key: 'xxxxxxxxxxxxxxxxxx',  
      secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
      .getVIPMarginData({  
        vipLevel: 'No VIP',  
        currency: 'BTC',  
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
        "retMsg": "success",  
        "result": {  
            "vipCoinList": [  
                {  
                    "list": [  
                        {  
                            "borrowable": true,  
                            "collateralRatio": "0.95",  
                            "currency": "BTC",  
                            "hourlyBorrowRate": "0.0000015021220000",  
                            "liquidationOrder": "11",  
                            "marginCollateral": true,  
                            "maxBorrowingAmount": "3"  
                        }  
                    ],  
                    "vipLevel": "No VIP"  
                }  
            ]  
        }  
    }

---

# 查詢不同VIP的槓桿數據

查詢**統一帳戶** 下不同VIP等級的槓桿數據

信息

不需要鑒權

### HTTP 請求

GET`/v5/spot-margin-trade/data`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
[vipLevel](/docs/zh-TW/v5/enum#viplevel)| false| string| VIP 等級  
currency| false| string| 幣種名稱  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
vipCoinList| array| Object  
> list| array| Object  
>> borrowable| boolean| 幣種是否支持借貸  
>> collateralRatio| string| 由於新的階梯價值率邏輯, 該字段從2025年2月19日開始不再準確。請使用[查詢階梯價值率](/docs/zh-TW/v5/spot-margin-uta/tier-collateral-ratio)  
>> currency| string| 幣種名稱  
>> hourlyBorrowRate| string| 每小時借貸利率  
>> liquidationOrder| string| 強平順序  
>> marginCollateral| boolean| 幣種是否支持作為保證金  
>> maxBorrowingAmount| string| 最大借貸額度  
> vipLevel| string| VIP 等級  
[](/docs/zh-TW/api-explorer/v5/spot-margin-uta/vip-margin)

* * *

### 請求示例

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/spot-margin-trade/data?vipLevel=No VIP&currency=BTC HTTP/1.1  
    Host: api-testnet.bybit.com  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.spot_margin_trade_get_vip_margin_data())  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
      testnet: true,  
      key: 'xxxxxxxxxxxxxxxxxx',  
      secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
      .getVIPMarginData({  
        vipLevel: 'No VIP',  
        currency: 'BTC',  
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
        "retMsg": "success",  
        "result": {  
            "vipCoinList": [  
                {  
                    "list": [  
                        {  
                            "borrowable": true,  
                            "collateralRatio": "0.95",  
                            "currency": "BTC",  
                            "hourlyBorrowRate": "0.0000015020640000",  
                            "liquidationOrder": "11",  
                            "marginCollateral": true,  
                            "maxBorrowingAmount": "3"  
                        }  
                    ],  
                    "vipLevel": "No VIP"  
                }  
            ]  
        }  
    }