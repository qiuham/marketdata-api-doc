---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/sbe/trade/order-entry
api_type: Trading
updated_at: 2026-07-28 19:04:10.466299
---

# Get Currency Data

info

If the borrowable switch is disabled (`false`), the related configuration fields will return `""`.

### HTTP Request

GET`/v5/spot-margin-trade/currency-data`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
currency| false| string| Coin name, uppercase only  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
list| array| Object  
> currency| string| Coin name  
> flexibleManualBorrowable| boolean| Whether flexible manual borrow is enabled. `true`: enabled, `false`: disabled  
> minFlexibleManualBorrowQty| string| Min flexible manual borrow qty  
> flexibleManualBorrowAccuracy| string| Coin precision for flexible manual borrow  
> fixedManualBorrowable| boolean| Whether fixed manual borrow is enabled. `true`: enabled, `false`: disabled  
> minFixedManualBorrowQty| string| Min fixed manual borrow qty  
> fixedManualBorrowAccuracy| string| Coin precision for fixed manual borrow  
> fixedInterestRateAccuracy| string| Coin precision for fixed manual borrow interest rate.  
> minFixedInterestRate| string| Min fixed manual borrow interest rate, e.g.: `0.01`  
> maxFixedInterestRate| string| Max fixed manual borrow interest rate, e.g.: `0.8`  
  
* * *

### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/spot-margin-trade/currency-data?currency=BTC HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1773220082000  
    X-BAPI-RECV-WINDOW: 5000  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.spot_margin_trade_get_currency_data(  
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
                    "flexibleManualBorrowable": true,  
                    "minFlexibleManualBorrowQty": "0.001",  
                    "flexibleManualBorrowAccuracy": "8",  
                    "fixedManualBorrowable": false,  
                    "minFixedManualBorrowQty": "",  
                    "fixedManualBorrowAccuracy": "",  
                    "fixedInterestRateAccuracy": "",  
                    "minFixedInterestRate": "",  
                    "maxFixedInterestRate": ""  
                }  
            ]  
        },  
        "retExtInfo": "{}",  
        "time": 1773220082091  
    }

---

# 查詢借幣幣種數據

信息

若借貸開關為關閉狀態（`false`），相關配置字段將返回 `""`。

### HTTP 請求

GET`/v5/spot-margin-trade/currency-data`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
currency| false| string| 幣種名稱，僅限大寫  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
list| array| Object  
> currency| string| 幣種名稱  
> flexibleManualBorrowable| boolean| 是否開啟活期借幣。`true`：開啟，`false`：關閉  
> minFlexibleManualBorrowQty| string| 活期最小借幣數量  
> flexibleManualBorrowAccuracy| string| 活期借幣精度  
> fixedManualBorrowable| boolean| 是否開啟定期借幣。`true`：開啟，`false`：關閉  
> minFixedManualBorrowQty| string| 定期最小借幣數量  
> fixedManualBorrowAccuracy| string| 定期借幣精度  
> fixedInterestRateAccuracy| string| 定期借幣利率精度  
> minFixedInterestRate| string| 最小借幣利率，例如：`0.01`  
> maxFixedInterestRate| string| 最大借幣利率，例如：`0.8`  
  
* * *

### 請求示例

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/spot-margin-trade/currency-data?currency=BTC HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1773220082000  
    X-BAPI-RECV-WINDOW: 5000  
    
    
    
      
    
    
    
      
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "list": [  
                {  
                    "currency": "BTC",  
                    "flexibleManualBorrowable": true,  
                    "minFlexibleManualBorrowQty": "0.001",  
                    "flexibleManualBorrowAccuracy": "8",  
                    "fixedManualBorrowable": false,  
                    "minFixedManualBorrowQty": "",  
                    "fixedManualBorrowAccuracy": "",  
                    "fixedInterestRateAccuracy": "",  
                    "minFixedInterestRate": "",  
                    "maxFixedInterestRate": ""  
                }  
            ]  
        },  
        "retExtInfo": "{}",  
        "time": 1773220082091  
    }