---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/spot-margin-uta/historical-interest
api_type: REST
updated_at: 2026-07-17 18:53:25.010257
---

# Get Position Tiers

info

  * If `currency` is passed in the input parameter, query by currency; if `currency` is not passed in the input parameter, query all configured currencies



### HTTP Request

GET`/v5/spot-margin-trade/position-tiers`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
currency| false| string| Coin name, uppercase only  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
list| array| Object  
> currency| string| Coin name, uppercase only  
> positionTiersRatioList| string| Object  
>> tier| string| Tiers. Display from small to large  
>> borrowLimit| string| Tiers Accumulation Borrow limit  
>> positionMMR| string| Loan Maintenance Margin Rate. Precision 8 decimal places  
>> positionIMR| string| Loan Initial Margin Rate. Precision 8 decimal places  
>> maxLeverage| string| Max Loan Leverage  
  
* * *

### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/spot-margin-trade/position-tiers?currency=BTC HTTP/1.1  
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
    print(session.spot_margin_trade_get_position_tiers(  
        currency="BTC"  
    ))  
    
    
    
      
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "list": [  
                {  
                    "currency": "BTC",  
                    "positionTiersRatioList": [  
                        {  
                            "tier": "1",  
                            "borrowLimit": "390",  
                            "positionMMR": "0.04",  
                            "positionIMR": "0.2",  
                            "maxLeverage": "5"  
                        },  
                        {  
                            "tier": "2",  
                            "borrowLimit": "391",  
                            "positionMMR": "0.04",  
                            "positionIMR": "0.25",  
                            "maxLeverage": "4"  
                        },  
                        {  
                            "tier": "3",  
                            "borrowLimit": "392",  
                            "positionMMR": "0.04",  
                            "positionIMR": "0.33333333",  
                            "maxLeverage": "3"  
                        },  
                        {  
                            "tier": "4",  
                            "borrowLimit": "393",  
                            "positionMMR": "0.04",  
                            "positionIMR": "0.5",  
                            "maxLeverage": "2"  
                        }  
                    ]  
                }  
            ]  
        },  
        "retExtInfo": "{}",  
        "time": 1756272543440  
    }

---

# 查詢借貸倉位風險訊息

信息

  * 如果輸入參數中傳入了 `currency`，則按幣查詢；如果輸入參數中沒有傳入 `currency`，則查詢所有已配置的幣



### HTTP 請求

GET`/v5/spot-margin-trade/position-tiers`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
currency| false| string| 幣名稱，僅限大寫  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
list| array| Object  
> currency| string| 幣名稱，僅限大寫  
> positionTiersRatioList| string| Object  
>> tier| string| 等級。從小到大顯示  
>> borrowLimit| string| 等級累積借款限額  
>> positionMMR| string| 借款佔用維持保證金比率。精確到8位小數  
>> positionIMR| string| 借款佔用初始保證金比率。精確到8位小數  
>> maxLeverage| string| 最大借貸槓桿  
  
* * *

### 請求示例

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/spot-margin-trade/position-tiers?currency=BTC HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1692696840996  
    X-BAPI-RECV-WINDOW: 5000  
    
    
    
      
    
    
    
      
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "list": [  
                {  
                    "currency": "BTC",  
                    "positionTiersRatioList": [  
                        {  
                            "tier": "1",  
                            "borrowLimit": "390",  
                            "positionMMR": "0.04",  
                            "positionIMR": "0.2",  
                            "maxLeverage": "5"  
                        },  
                        {  
                            "tier": "2",  
                            "borrowLimit": "391",  
                            "positionMMR": "0.04",  
                            "positionIMR": "0.25",  
                            "maxLeverage": "4"  
                        },  
                        {  
                            "tier": "3",  
                            "borrowLimit": "392",  
                            "positionMMR": "0.04",  
                            "positionIMR": "0.33333333",  
                            "maxLeverage": "3"  
                        },  
                        {  
                            "tier": "4",  
                            "borrowLimit": "393",  
                            "positionMMR": "0.04",  
                            "positionIMR": "0.5",  
                            "maxLeverage": "2"  
                        }  
                    ]  
                }  
            ]  
        },  
        "retExtInfo": "{}",  
        "time": 1756272543440  
    }